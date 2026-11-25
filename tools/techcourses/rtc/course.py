# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator (RTC) track: course definition in the POD/DCH/MRO package schema.
Built from the handoff package (CURRICULUM-AND-BLUEPRINT.md v1) and the improved blueprint v2 (November 25, 2026).
Every case, name, and identifier in the series is fictional. Clinical and regulatory review status: draft."""

HUB = "transplant-coordinator"
_HB = ("Illustrated clinical vignette, warm natural light, Filipino staff, patients and families, modern Philippine transplant "
       "center, no text and no legible names or numbers in image. ")

COURSE = {
    "title": "Renal Transplant Coordinator",
    "short": "Transplant Coordinator",
    "hub_slug": HUB,
    "label": "Training track for the people who navigate kidney recipients and living donors",
    "tag": "Ancillary Staff",
    "icon": "🤝",
    "no_branch": True,
    "exam_stratify": True,
    "audience": ("Clinical transplant coordinators (usually registered nurses) and coordination-support staff in Philippine kidney "
                 "transplant programs &middot; Z Benefits coordinators &middot; transplant and dialysis staff who refer, prepare, or "
                 "follow recipients and living donors"),
    "audience_type": "Kidney transplant coordinators and coordination-support staff",
    "level": "College reading level; two learner paths (clinical and support)",
    "review_date": "2026-11-25",
    "draw": 5,
    "mastery": "4 of 5",
    "exam_draw": 20,
    "keywords": ("kidney transplant coordinator training Philippines, renal transplant coordinator course, living kidney donor advocate, "
                 "DOH AO 2021-0059 living donor, PhilHealth Z Benefits kidney transplant PC 2026-0019, Z Benefits coordinator, "
                 "KT data registry, hospital transplant ethics committee HTEC, organ offer call, donor follow-up"),
    "page_title": "Renal Transplant Coordinator: A Training Track",
    "desc": ("A free 20-module training track for kidney transplant coordinators in the Philippines: navigating the recipient and the "
             "living donor through medical, legal, ethical, and PhilHealth systems, with separate records, donor protection, closed "
             "loops, and lifelong follow-up."),
    "h1": "Renal Transplant <em>Coordinator</em>",
    "sub": ("A training track for the person who walks two people through a transplant: the recipient and the living donor. Learn to "
            "keep their journeys separate, get every decision made by the right person, close every loop with evidence, and stay with "
            "both of them for life."),
    "disclaimer": ("Educational material for transplant coordination staff. Completing it is an Academy learning record only. It is not "
                   "a DOH-recognized training credit, a PhilHealth requirement, a certification, or CPD units, and it does not appoint "
                   "anyone as a donor advocate or confer any clinical authority."),
    "scope_note": ("This module is study material for kidney transplant coordinators and coordination-support staff. It explains the "
                   "reasoning behind coordination decisions; it is not a hospital protocol, legal advice, or a benefits ruling. Rules "
                   "and rates change: confirm every rule against the current issuance and your facility&rsquo;s approved policy. "
                   "Medical decisions belong to the transplant team, donation ethics to the ethics committee, and benefits to "
                   "PhilHealth. Every case, name, and identifier is fictional."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Transplant coordinators",
    "branch_blurb": ("For the person who navigates the kidney recipient and the living donor through medical, legal, ethical, and "
                     "PhilHealth systems, from referral to lifelong follow-up."),
    "academy_meta": "20 modules &middot; two learner paths &middot; a seven-tool toolkit &middot; capstone",
    "hero_alt": ("A Filipino transplant coordinator walking a calm hospital corridor between two separate consultation rooms, one with "
                 "an adult kidney recipient and one with an adult living donor, each with their own clinician."),
    "start_h2": "Two people, four systems, one coordinator",
    "start_html": """
<p>A living-donor kidney transplant joins two people for one operation. One of them is sick and hopes to be well. The other is healthy and is offering to take on a risk for someone else&rsquo;s benefit. Before that operation can happen, both of them must pass through four systems that do not talk to each other on their own: a <strong>medical</strong> system that decides whether it is safe, a <strong>legal</strong> system that decides whether the documents are true and the consent valid, an <strong>ethical</strong> system that decides whether the gift is free, and an <strong>insurance</strong> system that decides who pays. The renal transplant coordinator is the person who walks both of them through all four.</p>
<p>The coordinator does not decide whether a person is fit, whether a donation is ethical, or whether PhilHealth will pay. The coordinator makes sure that each of those decisions is made by the right person, on current evidence, on time, and written down; that each person knows what happens next; and that nothing is lost between departments. Good coordination is associated with more people completing the steps toward a transplant.[[rtc_sullivan2012]] It also means a donor can say no safely, and a recipient can be told &ldquo;not yet&rdquo; honestly.</p>
{{fig:rtc00_two_paths}}
{{cards:What this track will help you do|Keep two journeys separate::Open separate records, separate conversations, and a shared view that shows only what both may see.|Know who decides::Route suitability, consent, ethics review, benefits, and listing to the people who own them.|Protect the donor::Make it safe to ask, to wait, and to withdraw, and recognize inducement or pressure.|Navigate PhilHealth::Read the Z Benefits rules by version, keep the 180-day and 60-day clocks, and protect both people from avoidable cost.|Close every loop::Treat a referral sent, a specimen shipped, or a claim filed as open until someone confirms receipt.|Stay for life::Keep the recipient&rsquo;s medicines flowing and the donor&rsquo;s yearly check-ups happening, long after the operation.}}
<p>The track has two learner paths. <strong>Clinical coordinators</strong> hold a professional license (Philippine employers usually ask for a registered nurse) and do the clinical tasks their hospital assigns. <strong>Coordination-support staff</strong>, including Z Benefits coordinators, navigate records, documents, and funding; they learn the clinical content so they can recognize a problem and route it at once, never to assess or decide. Both paths study all twenty modules. Each module has a case, real situations, a skills checklist for a preceptor, and a self-assessment drawn from a bank of ten questions.</p>
""",
    "is_not": ("It is a training track written independently from published laws, regulations, guidelines, and research. It is not a "
               "DOH-recognized training certificate, a PhilHealth requirement, certification, CPD units, legal advice, or a benefits "
               "ruling. It does not make anyone a donor advocate, a procurement coordinator, or an ethics committee member. No national "
               "coordinator credential from the Philippine Society of Nephrology was found, and this track does not imply one. Clinical "
               "questions always go to the transplant team."),
    "pathways_tag": "Ten weeks",
    "pathways_h2": "Ten weeks of study, in five parts",
    "pathways_nav": "Parts",
    "pathways_html": """
<p>The twenty modules follow the path two people take through a transplant program: how authority works and how they arrive, how they are evaluated and protected, how the operation is paid for and how a kidney is offered, how they leave hospital and stay well, and how the program keeps their data safe and gets better.</p>
{{cards:The five parts|Part 1 &middot; Foundations::Modules 1 to 3. The coordinator&rsquo;s role and authority, Philippine regulation and scope, referral and equitable access.|Part 2 &middot; Evaluation and protection::Modules 4 to 9. Recipient workup, compatibility and specimens, donor intake and protection, donor risk, legal documents and consent, the ethics committee.|Part 3 &middot; Funding and access::Modules 10 to 13. PhilHealth and other payers, claims and financial protection, the waiting list and deceased donation, organ offers and logistics.|Part 4 &middot; Continuity::Modules 14 to 18. Final readiness and handoff, medicines and discharge, urgent escalation, lifelong follow-up, psychosocial and special situations.|Part 5 &middot; Accountability::Modules 19 and 20. Registries, privacy, and quality; the integrated capstone and what other countries do.}}
""",
    "modules_h2": "Twenty modules in five parts",
    "modules_intro": ("Study the modules in order. Each one starts from why a coordination step exists, moves to what the rules and the "
                      "evidence say, and ends with what the coordinator does on the next shift."),
    "syllabus_note": ("Each module plans six hours: two of guided study, two of case workshop and assessment, and two of supervised "
                      "placement. That is 80 hours of modules and workshops plus 40 hours of placement, 120 hours in all. These are "
                      "educational planning hours, not a verified DOH or PhilHealth minimum."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions drawn at random from a bank of 10; a good target is 4 of 5 on two different sets. Every question explains why the best answer is best and why the others fail. The end-of-course self-study check draws one question from each of the twenty modules (20 in all); the proposed pass is 16. Module 20 is a 120-minute simulated case &mdash; a donor withdrawal, an expiring pre-authorization, a transfusion before an offer, and a night-time offer call &mdash; scored on five dimensions with listed critical failures that cannot be averaged away.</p>
""",
    "sources_html": """
<p>The track is built from published sources. Philippine requirements follow the Department of Health (DOH) administrative orders on transplant facilities, deceased donation, and living donation,[[rtc_doh2008]][[rtc_doh2010b]][[rtc_doh2021]] the Organ Donation Act and the anti-trafficking law,[[rtc_ra7170]][[rtc_ra10364]] PhilHealth&rsquo;s Z Benefits circulars, survey tool, and registry advisory,[[rtc_ph2024]][[rtc_ph2026]][[rtc_phsat]][[rtc_pa2026]][[rtc_ph2025a]] and the Data Privacy Act.[[rtc_ra10173]] Clinical frameworks follow the Kidney Disease: Improving Global Outcomes (KDIGO) guidelines on candidates, living donors, and recipients.[[rtc_kdigo2020]][[rtc_kdigo2017]][[rtc_kdigo2009]] Statements about outcomes rest on peer-reviewed trials, cohorts, and reviews of navigation, donor risk, donor costs, and adherence.[[rtc_sullivan2012]][[rtc_muzaale2014]][[rtc_fu2021]][[rtc_dew2007]]</p>
<p>Where the evidence is observational, the text says &ldquo;associated with.&rdquo; Rules from other countries appear only as comparisons, never as Philippine requirements. Regulatory statements were checked on November 25, 2026. PhilHealth Circular 2026-0019 was published on November 21, 2026 and takes effect 15 days after publication, so on the research date it was <strong>published but not yet effective</strong>; confirm its effective date, the legacy-case rule, and current forms before you rely on it.[[rtc_ph2026index]]</p>
""",
    "trainers_intro": ("A transplant program manager, a transplant nephrologist, or a senior coordinator can use these modules as the guided-study part of a new coordinator&rsquo;s orientation. "),
    "trainer_h2": "Using the track to prepare a transplant coordinator",
    "trainer_audience": "Transplant program managers, transplant nephrologists and surgeons, senior coordinators, donor advocates, social workers, and Z Benefits leads",
    "trainer_html": """
<p>The track supports orientation; it does not replace it. A practical plan is ten weeks at two modules a week, each paired with a supervised session in the learner&rsquo;s own program using fictional records, then 40 hours of placement as real cases allow. Bring the donor advocate, the social worker, the ethics committee secretariat, and the Z Benefits lead into the sessions that touch their decisions.</p>
{{flow:Suggested sequence|Weeks 1 to 2::Modules 1 to 3. Build the four-gate register, the source register, and an intake script; role-play a referral that stalls.|Weeks 3 to 5::Modules 4 to 9. Prepare a case conference, label and ship a mock specimen, run a private donor intake, assemble a legal packet, write an ethics submission.|Weeks 6 to 7::Modules 10 to 13. Time a pre-authorization, reconcile a returned claim, update a waiting-list record, run an offer-call drill with read-back.|Weeks 8 to 9::Modules 14 to 18. Hold a readiness huddle, run a discharge teach-back, route an urgent call, plan two follow-up schedules.|Week 10::Modules 19 and 20. Define a quality measure, audit access to a restricted donor record, run the capstone simulation.}}
<p><strong>Two paths, one standard of safety.</strong> Mark which stations are clinical-path only (for example, taking an urgent clinical history under protocol). Support-path learners demonstrate recognition and routing instead. Every <span class="tc-crit">Critical</span> item applies to both paths: never present a payment approval as clinical clearance, never share a donor&rsquo;s private reasons, never advance a case with an unresolved coercion concern, and never let a sent message stand for a confirmed handoff.</p>
<p><strong>The fourteen blank navigation templates</strong> in the handoff package (referral intake, two-person barrier register, donor private-contact log, legal packet manifest, ethics submission cover, pre-authorization tracker, claims evidence checklist, offer-call script, readiness huddle record, discharge teach-back record, urgent-call log, donor follow-up recall list, privacy access review, and capstone scoring sheet) are for training with fictional data. Store any real-case version only in your hospital&rsquo;s approved system.</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments: 4 of 5 on two different sets for each module, with every missed question reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated independently to a preceptor in simulation or supervised practice.</li>
<li>End-of-course self-study check: 16 of 20 or higher.</li>
<li>Capstone 16 of 20 or higher, every dimension at least 2 of 4, and no critical failure: disclosing a donor&rsquo;s private reasons, presenting a payment or a test result as clinical or ethical clearance, advancing a case with an unresolved coercion or identity concern, allowing a pre-authorization to lapse unflagged, accepting an offer detail without read-back, or treating a sent message as a closed loop.</li>
</ul>
<p>Completion is an Academy learning record. It is not DOH-recognized training credit, a PhilHealth requirement, certification, or CPD units.</p>
""",
    "related": [("calc-transplant-coordinator-toolkit.html", "Seven planning tools for the transplant coordinator."),
                ("kidney-transplant.html", "The patient guide to kidney transplantation."),
                ("transplant-nurse.html", "The Kidney Transplant Nurse subtrack, for bedside and clinic nursing care.")],
}

P1, P2, P3, P4, P5 = ("Part 1 &middot; Foundations", "Part 2 &middot; Evaluation and protection", "Part 3 &middot; Funding and access",
                      "Part 4 &middot; Continuity", "Part 5 &middot; Accountability")

_ROWS = [
    ("01", "role-and-navigation", "The Coordinator as Navigator for Two People", P1,
     "Two protected journeys, four systems at every gate, the barrier register, and coordinating within authority.",
     "A transplant coordinator at a whiteboard with two separate colored pathway columns, explaining next steps to a calm adult recipient."),
    ("02", "philippine-governance", "Philippine Regulation and Professional Scope", P1,
     "Who issues which rule, reading every rule by version and effective date, clinical versus support scope, and the local role charter.",
     "A transplant coordinator and a program manager reviewing a binder of printed issuances with colored date tabs in a hospital office."),
    ("03", "referral-and-access", "Referral, Intake, and Equitable Access", P1,
     "Referring early, a useful first conversation, the barriers that stop people, and closing the referral loop.",
     "A coordinator speaking with an older patient and his wife at a dialysis unit bedside, holding a simple printed pathway leaflet."),
    ("04", "recipient-workup", "Recipient Workup and Multidisciplinary Decisions", P2,
     "Organizing the workup by question, preparing a case conference, test expiry, and explaining deferral honestly.",
     "A transplant team case conference around a table, with a coordinator presenting a one-page summary on a screen."),
    ("05", "compatibility-and-specimens", "Compatibility and Safe Specimen Coordination", P2,
     "Blood group, tissue type, antibodies and crossmatch in plain words, sensitizing events, and the specimen chain.",
     "A coordinator checking labels on sealed blood specimen tubes against a request form before handing a transport box to a courier."),
    ("06", "donor-intake-and-protection", "Living Donor Intake and Protection", P2,
     "The private first conversation, Philippine donor safeguards, recognizing pressure and reward, and making withdrawal safe.",
     "A coordinator talking privately with an adult potential donor in a small quiet consultation room, door closed, both seated."),
    ("07", "donor-medical-evaluation", "Donor Medical Evaluation and Long-Term Risk", P2,
     "What the donor workup asks, honest numbers for short- and long-term risk, and planning care beyond discharge.",
     "A nephrologist explaining a simple risk chart to an adult donor while a coordinator takes notes beside them."),
    ("08", "legal-documents-and-consent", "Legal Documents and Informed Consent", P2,
     "Building a traceable legal packet, verifying documents through authorized channels, and consent as a process.",
     "A coordinator checking civil registry documents against a manifest checklist at a desk with a document scanner."),
    ("09", "ethics-and-safeguarding", "Ethics Committee Navigation and Safeguarding", P2,
     "Submitting for a real decision, support versus persuasion, trafficking and inducement, and communicating decisions safely.",
     "A hospital ethics committee meeting with members seated around a table and a coordinator submitting a sealed case file."),
    ("10", "insurance-and-authorization", "PhilHealth and Other Payers", P3,
     "Different approvals, the Z Benefits package by version, pre-authorization timing, and planning affordability across time.",
     "A Z Benefits coordinator explaining a printed cost plan to a recipient and his sister at a hospital billing counter."),
    ("11", "claims-and-financial-protection", "Claims Evidence, Denials, and Financial Protection", P3,
     "The 60-day window, returns versus denials, evidence that follows care, and protecting the donor from cost.",
     "A claims officer and a coordinator comparing a checklist with a claim folder on a desk in a small office."),
    ("12", "waiting-list-and-deceased-donation", "The Waiting List and Deceased Donation", P3,
     "Three different databases, active waiting, sensitizing updates, and the boundary with organ procurement.",
     "A coordinator on the phone updating a waiting-list record on a computer, with a wall calendar behind her."),
    ("13", "offers-and-logistics", "Organ Offer Calls and Retrieval Logistics", P3,
     "A structured offer call with read-back, bringing the right people together, and treating a discrepancy as a safety event.",
     "A coordinator at night at a nurses' station on a phone call, reading back details from a structured form."),
    ("14", "readiness-and-handoff", "Final Readiness and Perioperative Handoff", P4,
     "Readiness as a convergence of gates, holds tracked explicitly, and separate handoffs for each person.",
     "A preoperative huddle with surgeon, anesthesiologist, nurse, and coordinator reviewing a readiness board before surgery."),
    ("15", "medicines-and-discharge", "Medicines, Discharge, and Self-Management", P4,
     "Continuity starts before leaving, teaching actions not names, a feasible discharge, and the medicine supply runway.",
     "A coordinator doing teach-back with a recipient holding a labeled pill organizer while his wife watches."),
    ("16", "urgent-triage-and-escalation", "Symptoms, Graft Dysfunction, and Urgent Escalation", P4,
     "Why delay matters, a disciplined urgent contact, routing within scope, and closing the loop.",
     "A coordinator answering a phone call at a transplant clinic desk while writing on a structured urgent-call log."),
    ("17", "longitudinal-navigation", "Lifelong Follow-Up for Donor and Recipient", P4,
     "Two continuing-care plans, recall with respect, donor yearly checks, and navigating graft failure.",
     "A coordinator greeting a healthy adult donor at a clinic reception for a yearly check-up, smiling."),
    ("18", "psychosocial-and-special-situations", "Psychosocial Navigation and Special Situations", P4,
     "Making barriers speakable, money and mental health, overseas workers and foreign nationals, children, and pregnancy.",
     "A social worker and a coordinator talking with a worried family in a hospital family room."),
    ("19", "data-privacy-and-quality", "Registries, Privacy, and Quality", P5,
     "Registries and their purposes, the restricted donor record, defining measures, and equity review.",
     "A coordinator and a quality officer reviewing a run chart on a monitor in a quiet office."),
    ("20", "capstone-and-international-comparison", "Integrated Capstone and International Practice", P5,
     "A whole case from referral to follow-up, and what to borrow (and not borrow) from the United States, the United Kingdom, and Australia.",
     "A coordinator presenting a case timeline to a small group of colleagues in a training room."),
]
MODULES = []
for _id, _slug, _title, _part, _sub, _brief in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part, "hours": (2, 2, 2),
                    "card_img": f"{HUB}-{_id}-card.webp", "hero_brief": _HB + _brief})
