# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 03: Referral, Intake, and Equitable Access. Written for this series from published sources."""

MODULE = {
    "image_alt": "A coordinator speaking with an older patient and his wife at a dialysis unit bedside, holding a simple printed pathway leaflet.",
    "objectives": [
        "Explain why referral for transplant evaluation should happen early, ideally before dialysis starts.",
        "Run a first conversation that gives balanced information and a named contact.",
        "Identify the practical, financial, informational, and social barriers that stop people from completing steps.",
        "Close a referral loop with an acknowledgment from the receiving service.",
        "Use family-centered education to help candidates discuss living donation without pressure.",
    ],
    "big": """
{{plain:Getting a transplant is like climbing a staircase in the dark. There are about eight steps: being medically suitable, wanting a transplant, being referred, attending the first visit, finishing the workup, being accepted, being listed or finding a donor, and receiving the kidney. Many people stop on a step, not because they cannot climb, but because nobody turned on the light for the next one.}}
{{fig:rtc03_steps}}
<p>The picture has a limit. A staircase is the same for everyone. The transplant staircase is not: some people meet a missing step &mdash; no transport money, no one to watch the children, a referral letter that never arrived, a fear nobody asked about. The trial that defined these eight steps found that navigators helped people climb more of them, across race and sex.[[rtc_sullivan2012]] Your job in this module is to start early, find the missing steps, and make sure every referral actually lands.</p>
<p>Kidney Disease: Improving Global Outcomes (KDIGO) advises that people with chronic kidney disease (CKD) stages G4 to G5 who are expected to reach kidney failure be informed about, educated about, and considered for transplantation; that potential candidates be referred for evaluation at least 6 to 12 months before expected dialysis; and that a pre-emptive living-donor transplant is the preferred treatment for those who are eligible.[[rtc_kdigo2020]]</p>
{{cards:Key terms for this module|Pre-emptive transplant::A transplant done before dialysis starts.|Referral::A request from one service to another to evaluate a person. It is complete only when the receiving service acknowledges it.|Intake::The first structured conversation and the information gathered then.|Access barrier::Anything outside medical suitability that stops a person from completing a step.|Named contact::One person, with a working number, who the candidate can call about the next step.}}
""",
    "case": {"title": "The referral that went nowhere", "html": """
<p>Mr. Eduardo Manalo, 52, a tricycle driver from Bulacan, has CKD stage G4 with an estimated glomerular filtration rate (eGFR) of 17. His nephrologist wrote &ldquo;refer for transplant evaluation&rdquo; in May. It is now August. He has not been contacted.</p>
<p>His daughter, who works in Dubai, messages the transplant center&rsquo;s page: &ldquo;Is my father on your list? My cousin wants to donate but nobody told us what to do.&rdquo; Mr. Manalo&rsquo;s phone number in the referral letter is missing a digit. His clinic says the letter was &ldquo;given to the patient to bring.&rdquo;</p>
<p>When you reach him at last through the dialysis access clinic, he tells you he did not come because the bus fare to Quezon City is 180 pesos each way and he would lose a day of driving.</p>
""", "questions": ["Where did this referral fail, and what would have closed the loop?",
                  "What barriers do you see, and which can the program address?",
                  "How do you respond to the daughter and the cousin who wants to donate?"]},
    "sections": [
        ("early", "Start early and fairly", "Why referral timing matters", """
<p>Why refer before dialysis? Because evaluation takes months, living donors need their own evaluation, and a transplant done before dialysis avoids the risks of a dialysis access and of the dialysis years themselves. Cohort studies consistently associate transplantation with longer life and better quality of life than dialysis, though no trial has randomized people to the two.[[rtc_tonelli2011]] KDIGO&rsquo;s advice to refer 6 to 12 months before expected dialysis follows from this timing logic.[[rtc_kdigo2020]]</p>
<p>&ldquo;Fairly&rdquo; matters as much as &ldquo;early.&rdquo; KDIGO&rsquo;s first statement is that people with CKD G4 to G5 should be informed and considered regardless of socioeconomic status, sex, gender identity, or race and ethnicity.[[rtc_kdigo2020]] In practice, unfairness rarely looks like a refusal. It looks like a referral nobody followed, a form only in English, a clinic open only on weekdays, or an assumption that a poor patient &ldquo;will not be able to afford it&rdquo; before anyone checked the package.</p>
<div class="table-wrap"><table>
<thead><tr><th>Barrier</th><th>What it looks like</th><th>What the program can do</th></tr></thead>
<tbody>
<tr><td>Practical</td><td>Fare, distance, lost workdays, childcare</td><td>Cluster appointments on one day; schedule around dialysis; ask about local assistance</td></tr>
<tr><td>Financial</td><td>Fear of cost before any estimate exists</td><td>Explain the PhilHealth package early (Module 10); give a written estimate</td></tr>
<tr><td>Informational</td><td>Not knowing transplant is possible, or what a donor faces</td><td>Plain-language teaching in the person&rsquo;s language, with family invited</td></tr>
<tr><td>Social</td><td>No one to ask about donation; fear of burdening family</td><td>Family education sessions; never ask the patient to recruit a donor by pressure</td></tr>
<tr><td>System</td><td>Lost letters, wrong numbers, no named contact</td><td>Acknowledged referrals; a named coordinator; a register row</td></tr>
</tbody></table></div>
{{key:Refer early, and assume nothing about who can afford or manage a transplant until someone has asked and checked.}}
"""),
        ("intake", "Make intake useful", "The first conversation", """
<p>The first conversation sets whether a person comes back. Aim for three outcomes: the person understands the options, knows the next step, and has a named contact with a working number.</p>
<ul>
<li><strong>Balanced information.</strong> Transplant, dialysis, and conservative care are all legitimate choices. Explain what transplant involves &mdash; workup, waiting, surgery, lifelong medicines, and uncertainty &mdash; without selling it.</li>
<li><strong>Preferences.</strong> Language, best contact time, who may receive updates, and who may not.</li>
<li><strong>Open questions about barriers.</strong> &ldquo;What would make it hard for you to come to appointments here?&rdquo; works better than &ldquo;You can come every week, right?&rdquo;</li>
<li><strong>Living donation, carefully.</strong> Explain that some people receive a kidney from a relative or close friend, that a potential donor contacts the program privately, and that the program protects donors. Do not ask the patient to name or persuade anyone.</li>
</ul>
<p>Education that includes the family changes what families do. In a randomized trial in the United States, 152 wait-listed patients received transplant education at home with family and friends present, in a group at the center, or individually. Home education was followed by more patients with at least one living-donor inquiry (82% vs 61% vs 47%) and evaluation (65% vs 39% vs 27%). The difference in living-donor transplants at two years (15% vs 8% vs 6%) was not statistically significant.[[rtc_rodrigue2014]] The trial supports bringing the family into education; it does not show that this alone increases transplants, and it studied one population in one country.</p>
{{scene:The question nobody asked|<p>At intake, coordinator Ms. Joy Fernandez asks Mrs. Rosario Dela Cruz, 60, what would make appointments hard. After a pause, Mrs. Dela Cruz says she cares for a grandson with cerebral palsy every afternoon.</p>
<p>Ms. Fernandez books the workup tests on two mornings, at 7 a.m., and links the family to the hospital social worker.</p>
<p class="tc-scene-take">The barrier was not cost or distance. It surfaced only because someone asked an open question.</p>}}
{{key:Every first conversation ends with three things: the next step, the date, and a named contact with a working number.}}
"""),
        ("loop", "Close the referral loop", "Dispatch is not receipt", """
<p>A referral is a handoff between services, and handoffs fail at the seams. A letter given to the patient &ldquo;to bring&rdquo; is the weakest kind: it depends on the patient knowing where to go, being able to get there, and the letter surviving the trip.</p>
{{flow:A closed referral loop|Received::The program logs the referral the day it arrives and acknowledges it to the referring clinician.|Contact checked::The coordinator confirms phone, address, and language within the program&rsquo;s set time.|First contact::A named coordinator reaches the person and gives a next step.|First visit booked::Date, place, what to bring, and help with practical barriers.|Referrer updated::The referring clinician hears that the person was seen, or why not.}}
<p>If contact fails, the loop is still yours. Call the referring clinic, the dialysis unit, or the barangay health worker the referral names, using only what is needed to reach the person. Do not post on social media, and do not leave health details in a voicemail.</p>
{{scene:The wrong digit|<p>Coordinator Mr. Ben Aquino receives a referral with a 10-digit mobile number (Philippine mobile numbers have 11). The text bounces. Instead of filing it, he calls the referring clinic the same morning; the clinic secretary reads the correct number from the chart.</p>
<p>He reaches the patient by noon and books the first visit. He sends the referring nephrologist a one-line acknowledgment: received, contacted, visit booked for the 14th.</p>
<p class="tc-scene-take">One phone call to the referrer closed a loop that a filing cabinet would have left open for months.</p>}}
{{key:A referral closes when the person has been reached and the referrer knows the outcome. Until then it is an open row in your register.}}
"""),
        ("equity", "Measure who gets through", "Fairness you can see", """
<p>You cannot fix unfairness you cannot see. Keep a simple referral log with the date received, the date of first contact, the date of the first visit, and the outcome. Once a quarter, look at the same numbers by sex, age group, province, and whether the person is on dialysis or not yet. If people from one province take three times as long to reach a first visit, that is a barrier to investigate, not a fact of life. Module 19 shows how to define these measures properly.</p>
<p>Equity also means honesty with people who may not be eligible. A referral is a request for evaluation, not a promise. Explain at intake that the team will review whether transplant is safe and possible, and that a &ldquo;not now&rdquo; usually comes with a reason and a next step.</p>
{{key:Count referrals by group, not only in total. An average can look fair while a group falls through.}}
"""),
    ],
    "debrief": ["""
<p><strong>Where the referral failed.</strong> The letter was handed to the patient instead of sent and acknowledged; the phone number was wrong; nobody owned the follow-up. A closed loop would have logged receipt, checked contacts with the referring clinic, reached Mr. Manalo within days, and told his nephrologist the outcome.</p>
<p><strong>The barriers.</strong> Transport cost (360 pesos a round trip) and a lost day of income are practical and financial barriers. The program can cluster tests on one day, schedule around his dialysis access visits, link him to the social worker for assistance, and explain early what the PhilHealth package covers. Fear of cost may be hiding behind the fare.</p>
<p><strong>The daughter and the cousin.</strong> Reply to the daughter by private message without confirming any health details until Mr. Manalo authorizes it; invite her father to call the named coordinator. For the cousin, explain that potential donors contact the program directly and privately, give the donor intake number, and say that donors have their own evaluation and their own team. Never ask Mr. Manalo to persuade the cousin.</p>
"""],
    "skills": {"title": "Intake and referral loop",
               "intro": "Run a simulated intake and close a referral loop while your preceptor observes.",
               "items": [
                   ("Logs a referral and sends an acknowledgment to the referring clinician the same working day.", True),
                   ("Explains transplant, dialysis, and conservative care in balanced, plain language.", False),
                   ("Asks open questions about practical, financial, informational, and social barriers.", False),
                   ("Explains how a potential donor contacts the program privately, without asking the patient to recruit.", True),
                   ("Ends the intake with the next step, its date, and a named contact.", True),
                   ("Recovers a failed contact through the referrer without breaching privacy.", True),
               ],
               "placement": "Pull ten recent referrals. For each, record dates of receipt, first contact, and first visit, and mark which loops were closed back to the referrer."},
    "terms": [("Pre-emptive transplant", "A transplant done before dialysis starts."),
              ("Referral", "A request for evaluation; complete only when acknowledged."),
              ("Intake", "The first structured conversation."), ("Access barrier", "A nonmedical obstacle to completing a step."),
              ("Named contact", "One person with a working number for the next step.")],
    "readings": [("kidney-transplant.html", "What a patient reads about transplantation."),
                 ("transplant-prehabilitation.html", "Getting fit before transplant: what candidates can do while they wait.")],
    "calcs": ["calc-transplant-coordinator-toolkit.html#tool-2"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["03"])
