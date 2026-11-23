# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 10: Access, Conflict, and Transitions. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician and a social worker sitting with a patient and her son in a quiet consultation room beside a dialysis unit.",
    "objectives": [
        "Explain what predicts missed sessions, and replace the label non-adherent with a question about barriers.",
        "Separate a clinical disagreement, a complaint, an inability to pay, and a credible safety threat, and respond to each differently.",
        "Make the area safe first, secure the next treatment second, and make administrative decisions last.",
        "Review any proposed restriction or involuntary transfer with leadership and compliance, with a continuity plan in place.",
        "Connect patients to social assistance such as the Department of Social Welfare and Development (DSWD) AICS program and Malasakit Centers while keeping a separate care plan.",
        "Track referrals for access, transplant, peritoneal dialysis, and conservative care until an outcome is recorded.",
    ],
    "big": """
{{plain:When a patient misses dialysis, it is tempting to see a choice. More often you are looking at a collision: the session landed on the same hours as the last affordable ride, a work shift, a sick grandchild, or a fear nobody has asked about.}}
{{fig:dch10_compete}}
<p>The picture has a limit. Some patients do choose, after reflection, to dialyze less or to stop. That is a decision that deserves a physician&rsquo;s conversation, not a barrier to remove. The first job is to find out which you are facing.</p>
{{cards:Key terms for this module|Missed session::A scheduled treatment not received, for any reason.|Barrier::Anything outside the patient&rsquo;s preference that stands between the patient and the session.|Involuntary discharge::Ending a patient&rsquo;s place at a unit without the patient&rsquo;s agreement.|AICS::Assistance to Individuals in Crisis Situation, a DSWD program that can help with medical costs.|Malasakit Center::A one-stop office in government hospitals that coordinates financial assistance for patients.|Conservative kidney management::Planned care focused on symptoms and quality of life without dialysis.}}
""",
    "case": {"title": "The family at reception", "html": """
<p>Mrs. Perla Dizon, 54, has missed four sessions in three weeks since her husband&rsquo;s tricycle was sold. She also disputes a charge from last month. On Friday she arrives an hour late. When the receptionist says her slot was given away, her son, Mr. Carlo Dizon, shouts, slams his hand on the counter, and stands in front of the exit door. Two other patients are waiting with their families.</p>
<p>The owner, who is on site, tells the head nurse: &ldquo;Remove her from the schedule. We do not need this.&rdquo;</p>
""", "questions": ["What needs to happen at reception now?",
                  "Who makes sure Mrs. Dizon has a workable plan for her next treatment?",
                  "What would a defensible decision about her place at the unit require?"]},
    "sections": [
        ("why", "Why patients miss", "What predicts a missed session", """
<p>Missed sessions are common and they matter. Across 20 countries in the Dialysis Outcomes and Practice Patterns Study (DOPPS), the risk of missing at least one session in four months ranged from under 1% in Italy and Japan to 24% in the United States. Missing was more likely with younger age, less time on dialysis, shorter treatments, longer travel time to the unit, and symptoms of depression, and it was associated with higher mortality.[[dch_alsalmi2018]] In interviews, patients named transportation, feeling unwell, and competing demands as barriers, and asked for better transport and clearer explanations of the risk of skipping.[[dch_chenitz2014]]</p>
<p>Philippine figures on missed sessions were not found. Travel time, fares, and work are likely to weigh at least as heavily here. Calculator 12 tracks your unit&rsquo;s missed-treatment rate so you can see whether it is rising.</p>
{{key:Ask what happened before you label what happened.}}
<p>When a patient misses repeatedly, ask about transport, work, cost, caregiving, symptoms, language, and fear. Confirm the best way to reach them, with consent. Check clinical urgency with the attending nephrologist, then assign one person to address the barrier and confirm the next treatment.</p>
"""),
        ("sort", "Sorting the problem", "Four problems that look alike at the counter", """
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>Who handles it</th><th>What it needs</th></tr></thead>
<tbody>
<tr><td>Credible safety threat</td><td>Security or emergency process</td><td>Make the area safe now; a blocked exit is a safety issue</td></tr>
<tr><td>Clinical disagreement</td><td>Attending nephrologist</td><td>A conversation and a documented shared decision</td></tr>
<tr><td>Complaint</td><td>Named complaint owner</td><td>A clear route, a timeline, and feedback</td></tr>
<tr><td>Ability to pay</td><td>Claims lead and social worker</td><td>Review of the charge and referral for assistance</td></tr>
</tbody></table></div>
{{fig:dch10_order}}
<p>Order matters. First make the area safe. Second, secure the patient&rsquo;s next treatment. Third, and only then, consider any administrative decision. A sudden change in behavior around dialysis also warrants a medical assessment: confusion from uremia, low blood sugar, or a stroke can look like anger.</p>
{{call:Stop any removal from the schedule or involuntary transfer until immediate safety is secured, the patient&rsquo;s next treatment is confirmed, and leadership and compliance have reviewed the obligations involved.}}
"""),
        ("ivd", "Involuntary discharge", "Before any restriction or transfer", """
<p>Involuntary discharge from a dialysis unit can leave a patient with no regular treatment, and in practice with only emergency dialysis. In the United States, Black patients are overrepresented among planned and executed involuntary discharges, and communication failures and system incentives are among the suspected contributors.[[dch_edwards2023]] When it happens, a structured second chance can work: one program placed 7 of 12 discharged patients in a new unit for 77 to 650 days without recurrence of the disruptive behavior, using debriefing, coaching, a face-to-face interview with the medical director, and a formal social-work handoff.[[dch_allon2019]]</p>
<p>Clinical urgency, scope, and verified capacity are defensible inputs to scheduling. Anger, a disputed bill, or inconvenience are not. Before any restriction, document the behavior and the clinical and administrative decisions separately, consider reasonable accommodations, and confirm a receiving unit and a continuity plan.</p>
"""),
        ("help", "Assistance and referrals", "Social assistance and referrals that close", """
<p>Offer a social work referral early when money or transport threatens continuity. The DSWD Assistance to Individuals in Crisis Situation program lists dialysis among the medical needs it may help with, subject to assessment and its current rules.[[dch_dswd_aics]] Malasakit Centers in government hospitals coordinate financial assistance from several agencies in one place.[[dch_ra11463]] With the patient&rsquo;s permission, help assemble the documents, and agree who checks the outcome. Keep the care plan separate from the assistance request, so treatment never waits for a pending grant.</p>
{{fig:dch10_referral}}
<p>Referrals for access creation or salvage, transplant evaluation, peritoneal dialysis, conservative kidney management, and psychosocial support each need an owner who tracks them to acceptance and outcome. A referral sent is not a referral received.</p>
"""),
    ],
    "debrief": ["""
<p><strong>At reception now.</strong> Make the area safe: clear the exit, use your security or emergency process, and move other patients and families away. One calm staff member speaks with Mr. Dizon; another checks Mrs. Dizon, who is an hour late and has missed four sessions, for urgent symptoms. If she is unwell, she is assessed now, whatever happened at the counter.</p>
<p><strong>Her next treatment.</strong> The attending nephrologist decides how urgent it is; the head nurse or the physician on duty finds the slot today or confirms a placement elsewhere, by name. A social worker meets the family about transport and the disputed charge, which the claims lead reviews and answers with a date.</p>
<p><strong>A defensible decision.</strong> The owner&rsquo;s instruction is premature. Any restriction requires the behavior documented, the clinical and administrative decisions recorded separately, leadership and compliance review, reasonable accommodations considered, and a confirmed continuity plan. Removing her today, without a receiving unit, would leave a patient who has already missed four sessions with no treatment at all.</p>
"""],
    "skills": {"title": "Reception safety, access barriers, and continuity",
               "intro": "Simulate the reception incident and a follow-up meeting with the patient, her son, a social worker, and billing.",
               "items": [
                   ("Secures immediate safety, including a blocked exit, through the facility process.", True),
                   ("Checks the patient for urgent symptoms regardless of the incident.", True),
                   ("Secures the next treatment before any administrative decision.", True),
                   ("Asks about barriers rather than labeling the patient.", False),
                   ("Separates clinical, complaint, payment, and safety issues.", False),
                   ("Refers to social work and explains assistance pathways.", False),
                   ("Refers any proposed restriction to leadership and compliance with a continuity plan.", True),
                   ("Records clinical and administrative decisions separately.", False),
                   ("Names an owner for each open referral.", False),
               ],
               "placement": "Review every patient who missed two or more sessions last month. Record the reason in the patient&rsquo;s words and the action taken."},
    "quiz": [
        ("In DOPPS, which factor was associated with missed sessions?",
         ["Older age", "Longer travel time to the unit", "Longer treatments", "More years on dialysis"], 1,
         "Also younger age, shorter treatments, and depression."),
        ("How did the 4-month missed-treatment risk vary across DOPPS countries?",
         ["Little", "From under 1% to 24%", "From 10% to 12%", "It was not measured"], 1,
         "A more than 50-fold variation."),
        ("A patient has missed four sessions. What is the first question?",
         ["How do we discipline her?", "What is getting in the way?", "Can we fill her slot?", "Has she paid?"], 1,
         "Ask before you label."),
        ("A family member blocks an exit and shouts. What comes first?",
         ["Removing the patient from the schedule", "Making the area safe through the facility process", "Reviewing the bill", "Calling the owner"], 1,
         "Safety first."),
        ("What comes second?",
         ["A warning letter", "Securing the patient&rsquo;s next treatment", "A board meeting", "A refund"], 1,
         "Continuity before administration."),
        ("A patient becomes suddenly confused and aggressive during dialysis. What should be considered?",
         ["Discharge", "A medical cause such as low glucose, uremia, or stroke", "A billing dispute", "Nothing"], 1,
         "Behavior change can be clinical."),
        ("What did a structured second-chance program achieve after involuntary discharge?",
         ["No placements", "7 of 12 patients placed without recurrence", "All were readmitted to hospital", "All refused"], 1,
         "Debriefing, coaching, and a formal handoff."),
        ("Which is a defensible input to scheduling?",
         ["Anger", "A disputed bill", "Clinical urgency and verified capacity", "Inconvenience"], 2,
         "Scheduling follows clinical need and capacity."),
        ("What must be in place before any involuntary transfer?",
         ["The owner&rsquo;s approval only", "Leadership and compliance review, accommodations considered, and a confirmed continuity plan", "A police report", "Nothing"], 1,
         "Never leave a patient without treatment."),
        ("Which DSWD program can help with dialysis costs?",
         ["4Ps only", "Assistance to Individuals in Crisis Situation (AICS)", "TUPAD", "None"], 1,
         "Subject to assessment and current rules."),
        ("What is a Malasakit Center?",
         ["A dialysis chain", "A one-stop office in government hospitals that coordinates financial assistance", "A PhilHealth branch", "A private charity"], 1,
         "Established by RA 11463."),
        ("Should treatment wait for a pending assistance request?",
         ["Yes", "No; keep the care plan separate from the assistance request", "Only for new patients", "Only on weekends"], 1,
         "Treatment never waits for a grant."),
        ("When is a transplant referral complete?",
         ["When sent", "When received, accepted, and the next step recorded with an owner", "After one year", "When the patient asks"], 1,
         "Track referrals to outcome."),
        ("Who reviews a disputed charge?",
         ["The receptionist", "The claims lead, with compliance, returning the outcome to the patient", "The owner alone", "The patient"], 1,
         "Give a date and a route."),
        ("Why record clinical and administrative decisions separately?",
         ["For length", "So each can be reviewed on its own basis and clinical care is not driven by administrative motives", "Because PhilHealth requires it", "It does not matter"], 1,
         "Keep the reasons visible."),
    ],
    "terms": [("Missed session", "A scheduled treatment not received."),
              ("Barrier", "Something outside the patient&rsquo;s preference that blocks attendance."),
              ("Involuntary discharge", "Ending a patient&rsquo;s place without agreement."),
              ("AICS", "Assistance to Individuals in Crisis Situation, a DSWD program."),
              ("Malasakit Center", "A one-stop financial assistance office in government hospitals."),
              ("Conservative kidney management", "Planned care without dialysis, focused on symptoms and quality of life.")],
    "readings": [("starting-dialysis-new-beginning.html", "Why starting dialysis is not a death sentence, but a new beginning."),
                 ("incremental-dialysis.html", "Incremental dialysis: starting with the kidney function you still have.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
