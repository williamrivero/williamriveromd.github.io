# -*- coding: utf-8 -*-
"""Renal Social Worker (SW) track: course definition in the POD/DCH/MRO/RTC package schema.
Built from the handoff package (01-CURRICULUM-BLUEPRINT.md v1.0.0) and the improved blueprint v2 (05-BLUEPRINT-V2-IMPROVED.md,
November 25, 2026). Every case, name, and identifier in the series is fictional. Review status: draft for social work and
nephrology sign-off."""

HUB = "social-worker"
_HB = ("Illustrated clinical vignette, warm natural light, Filipino social workers, patients and families, modern Philippine "
       "dialysis unit or hospital social service office, no text and no legible names or numbers in image. ")

COURSE = {
    "title": "Renal Social Worker",
    "short": "Social Worker",
    "hub_slug": HUB,
    "label": "Training track for social workers in kidney care",
    "tag": "Ancillary Staff",
    "icon": "🧭",
    "no_branch": True,
    "exam_stratify": True,
    "audience": ("Registered social workers in dialysis units, hospital medical social work departments, and kidney transplant "
                 "programs &middot; medical social workers rotating into kidney care &middot; navigation and support staff on the "
                 "orientation path"),
    "audience_type": "Registered social workers and navigation staff in kidney care",
    "level": "College reading level; two learner paths (professional and navigation orientation)",
    "review_date": "2026-11-25",
    "draw": 5,
    "mastery": "4 of 5",
    "exam_draw": 40,
    "keywords": ("renal social worker training Philippines, nephrology social work course, dialysis social worker, medical social work "
                 "kidney, psychosocial assessment dialysis, PhilHealth hemodialysis 156 sessions navigation, DSWD AICS PCSO medical "
                 "assistance dialysis, depression screening PHQ-9 dialysis, caregiver burden dialysis, living donor protection, "
                 "advance care planning kidney"),
    "page_title": "Renal Social Worker: A Training Track",
    "desc": ("A free 20-module training track for social workers in Philippine kidney care: psychosocial assessment, benefits and "
             "assistance navigation, depression and safety, families and caregivers, home therapy, transplant and donor protection, "
             "supportive care, and continuity."),
    "h1": "Renal Social <em>Worker</em>",
    "sub": ("A training track for the social worker who meets people at the moment kidney failure reaches their household. Learn to "
            "assess the whole situation, start from the person&rsquo;s own goal, remove the barriers between them and the care they "
            "chose, keep them safe, and stay with the family through every change."),
    "disclaimer": ("Educational material for social workers and navigation staff in kidney care. Completing it is an Academy learning "
                   "record only. It is not a Professional Regulation Commission (PRC) license, a specialty credential, CPD units, or DOH "
                   "or PhilHealth recognition, and it does not authorize anyone to practice beyond their own registration."),
    "scope_note": ("This module is study material for social workers and navigation staff in kidney care. It explains the reasoning "
                   "behind social work decisions; it is not a facility procedure, legal advice, a benefits ruling, or a mental health "
                   "diagnosis. Rules, assistance programs, and amounts change: confirm them against the current issuance and your "
                   "facility&rsquo;s approved policy. Medical treatment belongs to the nephrologist, benefits to PhilHealth, donation "
                   "ethics to the ethics committee, and psychiatric diagnosis to the mental health team. Every case, name, and "
                   "identifier is fictional."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Social workers",
    "branch_blurb": ("For the registered social worker in a dialysis unit, hospital, or transplant program: assessment, counseling within "
                     "competence, benefit and assistance navigation, safeguarding, families, and continuity across kidney care."),
    "academy_meta": "20 modules &middot; two learner paths &middot; a six-tool toolkit &middot; six observed stations",
    "hero_alt": ("A Filipino social worker seated at eye level beside an older man in a dialysis chair, listening, while his wife sits "
                 "close by and a nurse works at the next station."),
    "start_h2": "Kidney failure lands on a household",
    "start_html": """
<p>Kidney failure is diagnosed in one body, but it lands on a whole household. Three mornings a week disappear into dialysis. A job paid by the day ends. A daughter in high school becomes the person who knows the medicines. A tricycle fare of a few hundred pesos, multiplied by thirteen visits a month, becomes the reason a session is missed. The nephrologist sees the potassium. The renal social worker is the member of the team whose job is to see everything else.</p>
<p>Your work rests on three habits. Start from what the person wants, not from the form an agency needs. Turn what you learn into a formulation, a plain explanation of why things are happening, and then into a plan with owners and dates. And close every loop on evidence: a referral sent is an action, an outcome that reached the household is a result.</p>
{{fig:sw00_household}}
{{cards:What this track will help you do|Assess the whole situation::Run a private, strengths-based psychosocial assessment and write a formulation the team can use.|Navigate benefits honestly::Explain PhilHealth and assistance pathways by circular and date, without promising approval or amounts.|Make access affordable::Count what each visit really costs a household and find the gap before a session is missed.|Recognize distress and danger::Screen for depression, ask directly about safety, and hand over in person when someone is at risk.|Support families and donors::Plan for caregivers before they collapse, and protect a living donor&rsquo;s right to say no.|Stay through every change::Coordinate modality changes, transplant, transfers, disasters, supportive care, and bereavement.}}
<p>The track has two learner paths. The <strong>professional path</strong> is for registered social workers, who study all twenty modules and complete the observed stations and supervised practice. The <strong>navigation orientation</strong> is for navigators, assistants, and administrative partners, who study Modules 1 to 4, 6 to 9, 17, and 18 to learn recognition and handoff; it does not qualify anyone to conduct or sign a professional social work assessment. Each module has a timed case, real situations, a skills checklist for a supervisor, and a self-assessment drawn from a bank of ten questions.</p>
""",
    "is_not": ("It is a training track written independently from published laws, regulations, guidelines, and research. It is not a "
               "PRC license or specialty credential, CPD units, legal advice, a benefits ruling, or a psychotherapy qualification. "
               "No social worker staffing ratio or specialty certification was identified in the reviewed DOH dialysis order or the "
               "PSN 2024 hemodialysis guidelines; that finding is limited to the documents reviewed and does not mean no requirement "
               "applies to your facility. Clinical questions always go to the attending nephrologist."),
    "pathways_tag": "Six weeks",
    "pathways_h2": "Six weeks of study, in five parts",
    "pathways_nav": "Parts",
    "pathways_html": """
<p>The twenty modules follow the questions a renal social worker answers for every person: what the role is and how the system works, what is happening in this household and how to reach the help it needs, how the person is coping and whether they are safe, how they move through changes in treatment, and how the work is recorded, measured, and supervised.</p>
{{cards:The five parts|Part 1 &middot; Foundations::Modules 1 to 4. The role and its boundaries, the kidney physiology a social worker needs, Philippine requirements, and engagement across language and culture.|Part 2 &middot; Assessment and access::Modules 5 to 9. The psychosocial assessment, care plans and referrals, PhilHealth, assistance programs, and transport, work, housing, and food.|Part 3 &middot; Psychosocial care::Modules 10 to 13. Depression and anxiety, immediate safety and safeguarding, motivational conversations, and families and caregivers.|Part 4 &middot; Transitions::Modules 14 to 17. Modality and home therapy, transplant and donor protection, supportive care and bereavement, transfers and disasters.|Part 5 &middot; Accountability::Modules 18 to 20. Records and privacy, quality and supervision, and the integrated case conference.}}
""",
    "modules_h2": "Twenty modules in five parts",
    "modules_intro": ("Study the modules in order. Each one starts from a person&rsquo;s situation, moves to what the evidence and the "
                      "rules say, and ends with what you do on your next shift."),
    "syllabus_note": ("Each module plans one hour of guided study and one hour of case workshop and self-assessment (40 hours), with 16 "
                      "hours of supervised practice spread across the modules and a four-hour final assessment: 60 hours in all. These "
                      "are educational planning hours, not a PRC, DOH, or PhilHealth requirement."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions drawn at random from a bank of 10; a good target is 4 of 5 on two different sets. Every question explains why the best answer is best and why the others fail. The end-of-course self-study check draws two questions from each of the twenty modules (40 in all); the proposed pass is 32. The observed assessment on the trainer page has six stations, each passed at 8 of 10 with every critical criterion met; a high written score cannot make up for a safety failure.</p>
""",
    "sources_html": """
<p>The track is built from published sources. Philippine requirements follow the social work law and its amendment,[[sw_ra4373]][[sw_ra10847]] the PRC adoption of the social work code of ethics,[[sw_prc2023]] the DOH dialysis licensing order,[[sw_doh2012]] the PSN 2024 hemodialysis guidelines,[[sw_psn2024]] PhilHealth&rsquo;s hemodialysis, peritoneal dialysis, and kidney transplant circulars,[[sw_phic2024hd]][[sw_phic2024pd]][[sw_phic2026kt]] the DSWD, PCSO, and Malasakit Center assistance pathways,[[sw_dswd_aics]][[sw_pcso_map]][[sw_ra11463]] and the Data Privacy Act.[[ra10173]] Statements about outcomes rest on peer-reviewed trials, cohorts, and systematic reviews of depression, health literacy, travel and cost barriers, caregivers, transplant, and grief.[[palmer2013]][[sw_natale2019]][[sw_taylor2017]][[sw_moist2008]][[sw_villanueva2025]][[sw_gilbertson2019]]</p>
<p>Where the evidence is observational, the text says &ldquo;associated with.&rdquo; Rules from other countries appear only as comparisons. Several Philippine sources could be read only in part (the full DOH licensing checklist, the annexes of DOH Department Memorandum No. 2024-0372, the full PRC code annex, and the peritoneal dialysis circular); the modules say so where it matters. PhilHealth Circular 2026-0019 on kidney transplantation was published on November 21, 2026 and takes effect 15 days after publication; on the research date it was <strong>published but not yet effective</strong>.[[sw_phic2026kt]]</p>
""",
    "trainers_intro": ("A medical social work department head, a senior renal social worker, or a dialysis unit head can use these modules as the guided-study part of a new social worker&rsquo;s orientation. "),
    "trainer_h2": "Using the track to prepare a renal social worker",
    "trainer_audience": "Medical social work heads, senior social workers, dialysis clinical heads, head nurses, transplant program staff, and practicum supervisors",
    "trainer_html": """
<p>The track supports orientation; it does not replace it. A practical plan is six weeks at about ten hours a week: four modules a week with a two-hour supervised session in the learner&rsquo;s own unit, then a week of practicum consolidation and the final assessment. Use fictional cases in group sessions. Real cases belong only in supervised practice, inside your facility&rsquo;s approved records.</p>
{{flow:Suggested sequence|Week 1::Modules 1 to 4. Role map with absence cover, a dialysis week walk-through with a nurse, the source register, and an observed first interview.|Week 2::Modules 5 to 8. A full assessment and formulation, a care plan with a referral log, a benefit explanation without promises, and an assistance map for your area.|Week 3::Modules 9 to 12. An access-cost estimate with the toolkit, a PHQ-9 role-play with the safety pathway, and a motivational conversation.|Week 4::Modules 13 to 16. A caregiver plan, a home-therapy feasibility visit, a private donor interview simulation, and an advance care planning conversation.|Week 5::Modules 17 to 20. A transfer handoff with arrival confirmation, a factual note, a quality measure card, and the case conference.|Week 6::Practicum consolidation (6 hours) and the final assessment (4 hours): the written check and six observed stations.}}
<h3>The six observed stations</h3>
<p>Each station is scored out of 10; pass is 8 with every <span class="tc-crit">Critical</span> criterion met. <strong>1 Private intake:</strong> introduces role, confirms identity privately, explains confidentiality and its limits, asks permission before involving family. <strong>2 Formulation and plan:</strong> turns a fictional assessment into a formulation and a plan with owners, dates, and review. <strong>3 Benefit and assistance explanation:</strong> explains a PhilHealth or assistance pathway by version and date, with no promise of approval or amount. <strong>4 Distress and safety:</strong> completes a PHQ-9 role-play, asks item 9 directly, and follows the safety pathway on a positive answer. <strong>5 Family meeting:</strong> runs a short meeting with the patient&rsquo;s consent and keeps the patient&rsquo;s voice central. <strong>6 Note and referral:</strong> writes a factual note and a proportionate referral, and defines what will close the loop.</p>
<p><strong>Two paths, one standard of safety.</strong> Navigation staff do not run stations 2 and 4 as assessors; they demonstrate recognition and handoff instead. Every Critical item applies to both paths: never leave a person at immediate risk alone, never promise a benefit or an amount, never disclose more than the purpose needs, never sign an assessment you are not authorized to make, and never let a sent referral stand for a closed loop.</p>
<p><strong>The ten practice worksheets</strong> from the handoff package (psychosocial assessment and formulation, shared care plan, referral and resource log, benefit-navigation note, access cost estimate, distress conversation aid, caregiver and family plan, continuity handoff, workload and coverage, and quality measure card) are teaching forms, not official DOH forms. Use them with fictional data, and store any real-case version only in your facility&rsquo;s approved system.</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments: 4 of 5 on two different sets for each module, with every missed question reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated to a supervisor in simulation or supervised practice.</li>
<li>End-of-course self-study check: 32 of 40 or higher.</li>
<li>All six observed stations passed at 8 of 10 or higher with no critical failure: leaving a person at immediate risk alone, promising a benefit or an amount, disclosing beyond the purpose, signing outside one&rsquo;s authority, or treating a sent referral as a closed loop.</li>
<li>Sixteen hours of supervised practice documented and accepted by the supervisor, and a signed development plan.</li>
</ul>
<p>Completion is an Academy learning record. It is not a PRC license, a specialty credential, CPD units, or DOH or PhilHealth recognition.</p>
""",
    "related": [("calc-social-worker-toolkit.html", "Six planning tools for the renal social worker."),
                ("philhealth-z-packages.html", "The patient guide to PhilHealth hemodialysis, peritoneal dialysis, and transplant benefits."),
                ("calc-phq9.html", "The PHQ-9 depression screening calculator.")],
}

P1, P2, P3, P4, P5 = ("Part 1 &middot; Foundations", "Part 2 &middot; Assessment and access", "Part 3 &middot; Psychosocial care",
                      "Part 4 &middot; Transitions", "Part 5 &middot; Accountability")

_ROWS = [
    ("01", "role-and-professional-boundaries", "The Renal Social Worker: Role, Ethics, and Boundaries", P1,
     "Starting from the person&rsquo;s purpose, regulated practice and its edges, ethics you can see, and who decides what.",
     "A social worker introducing herself to an adult man and his wife in a quiet dialysis unit corner, holding a simple role card.", 1),
    ("02", "kidney-care-literacy", "Kidney Care Literacy for Social Workers", P1,
     "What the kidneys do, what dialysis can and cannot replace, the treatment options, and when a social fact becomes a clinical fact.",
     "A nurse showing a social worker a dialysis machine and a weekly treatment schedule on a whiteboard.", 0),
    ("03", "philippine-regulation-and-service-design", "Philippine Requirements and a Defensible Service Model", P1,
     "Who issues which rule, what the reviewed documents say and do not say, a service charter, and coverage and escalation.",
     "A social worker and a dialysis unit head reviewing printed rules and a service charter at an office table.", 0),
    ("04", "engagement-and-cultural-safety", "Engagement, Language Access, and Cultural Safety", P1,
     "The first five minutes, language and health literacy, family and culture without stereotype, and consent for family participation.",
     "A social worker seated at eye level with an older Filipino woman in a small private room, a visual card on the table.", 1),
    ("05", "psychosocial-assessment", "A Comprehensive Psychosocial Assessment", P2,
     "Domains and sources, strengths before deficits, the formulation, and writing it so the team can use it.",
     "A social worker taking notes during a private interview with a middle-aged man in a hospital social service office.", 1),
    ("06", "care-plans-and-case-management", "Care Plans, Referrals, and Case Management", P2,
     "Goals that belong to the person, actions with owners and dates, the referral loop, and review and closure.",
     "A social worker on the phone confirming a referral while checking a printed care plan with columns.", 1),
    ("07", "philhealth-navigation", "PhilHealth Navigation and Financial Protection", P2,
     "Reading a rule by version and date, the hemodialysis package, peritoneal dialysis and transplant benefits, and explaining without promising.",
     "A social worker explaining a printed benefit summary to a patient and her daughter at a hospital help desk.", 1),
    ("08", "assistance-and-resource-mobilization", "Assistance Pathways and Resource Mobilization", P2,
     "Mapping sources before applying, government assistance programs, factual social case studies, and tracking decisions, not submissions.",
     "A social worker helping a family organize documents into labeled folders at a government hospital assistance desk.", 1),
    ("09", "work-transport-and-social-determinants", "Transport, Work, Housing, Food, and Disability Access", P2,
     "The access equation, work and income, housing, food and water, and disability benefits.",
     "A patient arriving by tricycle at a dialysis unit entrance early in the morning, a social worker greeting him.", 1),
    ("10", "distress-and-mental-health", "Distress, Depression, Anxiety, and Stepped Support", P3,
     "How common distress is, screening honestly, what helps and how well, and stepped care with referral.",
     "A social worker sitting beside a man in a dialysis chair, listening closely, a nurse in the background.", 1),
    ("11", "crisis-and-safeguarding", "Immediate Safety, Safeguarding, Violence, and Exploitation", P3,
     "Asking directly about suicide, the safety pathway, abuse and exploitation of older adults, and violence in the home.",
     "A social worker speaking privately and calmly with an older woman in a closed consultation room.", 1),
    ("12", "behavior-change-and-treatment-barriers", "Motivational Conversations and Treatment Barriers", P3,
     "Describing instead of labeling, the spirit and skills of motivational interviewing, barrier-specific problem solving, and when to stop pushing.",
     "A social worker and a younger man talking in a dialysis unit, the man leaning forward and engaged.", 1),
    ("13", "family-caregivers-and-life-course", "Families, Caregivers, Children, and Changing Life Roles", P3,
     "Who cares and what it costs, caregiver assessment and backup, children in the household, and role loss.",
     "A tired Filipino woman caregiver speaking with a social worker in a hospital family room, holding a medicine pouch.", 1),
    ("14", "modality-and-home-therapy-support", "Modality Decisions, Home Therapy, and Practical Feasibility", P4,
     "What each modality asks of a household, home peritoneal dialysis feasibility, assisted options, and respecting choices.",
     "A social worker and a peritoneal dialysis nurse visiting a modest Filipino home, looking at a clean corner for supplies.", 1),
    ("15", "transplant-psychosocial-and-donor-protection", "Transplant Access, Psychosocial Preparation, and Donor Protection", P4,
     "The psychosocial evaluation and its limits, supporting candidates, the donor&rsquo;s separate path, and coercion and trafficking.",
     "A social worker in a private interview with an adult potential kidney donor, door closed, both seated.", 1),
    ("16", "supportive-care-grief-and-bereavement", "Supportive Care, Treatment Decisions, Grief, and Bereavement", P4,
     "Conservative kidney management, advance care planning, decisions to stop dialysis, and grief and bereavement follow-up.",
     "A family meeting with an older man, his wife and daughter, a nephrologist, and a social worker around a small table.", 1),
    ("17", "transfers-disasters-and-continuity", "Transfers, Disasters, and Continuity of Care", P4,
     "Transfer as a handoff, temporary dialysis away from home, typhoon and flood planning, and arrival confirmation.",
     "A social worker on the phone at a dialysis unit desk during heavy rain, a printed transfer checklist in hand.", 1),
    ("18", "documentation-privacy-and-digital-practice", "Documentation, Privacy, Telehealth, and Digital Boundaries", P5,
     "Writing facts, sources, and plans, privacy law for social workers, releasing information, and phones, chats, and remote sessions.",
     "A social worker typing a case note at a secure workstation in a quiet office, a privacy screen on the monitor.", 1),
    ("19", "quality-supervision-and-workload", "Quality Improvement, Supervision, and Workload", P5,
     "Measures that mean something, numerators and denominators, supervision and reflective practice, and safe workload.",
     "A social worker and a supervisor reviewing a simple run chart together in a small office.", 0),
    ("20", "integrated-case-and-readiness", "Integrated Case Conference and Readiness for Practice", P5,
     "Running a case conference, the integrated case, readiness and limits, and your development plan.",
     "A multidisciplinary case conference with a social worker presenting a family timeline to a nephrologist, nurse, and dietitian.", 0),
]
MODULES = []
for _id, _slug, _title, _part, _sub, _brief, _pl in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part, "hours": (1, 1, _pl),
                    "card_img": f"{HUB}-{_id}-card.webp", "hero_brief": _HB + _brief})
