# -*- coding: utf-8 -*-
"""Dialysis Clinical Head (DCH) track: course definition in the Physician on Duty (POD) package schema.
Written for the Renal Care Academy from published sources. Every case and record in the series is fictional.
Hub slug follows the Head Nurse pattern (dialysis-head-nurse) rather than the handoff's suggested dialysis-unit-heads;
change HUB below if the repository convention differs."""

HUB = "dialysis-clinical-head"
_HB = "Illustrated clinical vignette, warm natural light, Filipino staff and patients, modern hemodialysis unit, no text in image. "

COURSE = {
    "title": "Dialysis Clinical Head",
    "short": "Clinical Head",
    "hub_slug": HUB,
    "label": "Training track for physician heads of hemodialysis services",
    "tag": "Renal Care Physicians",
    "icon": "🏛️",
    "no_branch": True,
    "audience": ("Physician heads of adult maintenance hemodialysis units &middot; nephrologists preparing to take an appointment &middot; "
                 "head nurses, operations managers, and quality leads who share the leadership table"),
    "audience_type": "Physician heads of hemodialysis services",
    "level": "Physicians with maintenance hemodialysis experience, written in plain language",
    "review_date": "2026-11-24",
    "draw": 8,
    "mastery": "7 of 8",
    "keywords": ("dialysis clinical head Philippines, hemodialysis medical director training, dialysis unit head, DOH dialysis licensing, "
                 "PhilHealth hemodialysis 156 sessions, dialysis water quality ISO 23500, dialysis disaster preparedness typhoon, "
                 "dialysis QAPI, dialysis unit governance, hemodiafiltration CONVINCE"),
    "page_title": "Dialysis Clinical Head: A Training Track",
    "desc": ("A free training track for physicians who head a hemodialysis service: the appointment and its authority, DOH licensing, "
             "PhilHealth claims, clinical oversight, water and infection, risk and quality, disasters, safe capacity, the workforce, "
             "patient access, money and conflicts of interest, downtime and privacy, serious events, and new services. "
             "Plain language, figures, a case, a skills checklist, calculators, and a self-assessment in every module."),
    "h1": "Dialysis <em>Clinical Head</em>",
    "sub": ("A training track for physicians who head a hemodialysis service. Learn why each control protects a patient, "
            "who owns each decision, and what to do when the unit cannot run safely."),
    "disclaimer": ("Educational material for physicians and unit leaders. Completing it is an Academy learning record only. It does not confer "
                   "CPD units, PSN attestation, DOH eligibility, PhilHealth accreditation, or appointment authority, and it does not replace "
                   "current regulations, your facility&rsquo;s bylaws and protocols, or legal advice."),
    "scope_note": ("This module is study material for physician heads of adult maintenance hemodialysis services. It explains the reasoning behind "
                   "common decisions; it is not a protocol and not legal advice. Regulations change: confirm every rule against the current text "
                   "and your regional office before you rely on it. Clinical limits are set by your unit&rsquo;s approved protocols and the attending "
                   "nephrologist. Every case and record is fictional."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Clinical heads",
    "branch_blurb": ("For physicians who head a hemodialysis service: authority and appointment, licensing, PhilHealth, oversight, water and "
                     "infection, risk, disasters, capacity, people, money, privacy, serious events, and growth."),
    "academy_meta": "14 modules &middot; a capstone &middot; calculators in every module",
    "hero_alt": "A physician clinical head reviewing a binder of signed release records with a head nurse and a water technician at the door of a dialysis unit.",
    "start_h2": "The physician who signs",
    "start_html": """
<p>A hemodialysis (HD) unit is a small hospital that runs on borrowed physiology. For four hours, three times a week, each patient&rsquo;s blood leaves the body, crosses a membrane bathed in about 120 liters of fluid your unit made from tap water, and comes back. Between sessions, the patient carries everything a kidney would have cleared. The unit is safe only when the water was released, the machines were tested, the staff on the floor can do what they are assigned, and someone notices when one of those is not true.</p>
<p>The clinical head is the physician whose name is on the appointment. You are accountable for the clinical system: the policies, the competency of the people who follow them, the quality program, and the decision to hold or restart a service when something fails. You are not the owner, the billing office, the water technician, or every patient&rsquo;s attending nephrologist. Much of this track is about knowing exactly where your authority starts and stops, and making sure every decision has an owner.</p>
{{cards:What this track will help you do|Take the job safely::Read an appointment, map who decides what, and refuse to sign what you cannot oversee.|Pass the inspection you did not prepare for::Trace a requirement from the rule to the floor and back.|Follow the money::Trace a session from the chart to the PhilHealth claim.|Hold the line::Stop a station, a shift, or a whole unit when a control fails, and restart it on evidence.|Count every patient::Run a disaster response that ends with every displaced patient accounted for.|Lead people and money::Defend safe staffing, resolve conflicts, and write a board brief an owner can act on.|Grow carefully::Judge a new service or technology on evidence, and plan your first 90 days.}}
{{fig:dch00_map}}
<p>The track is written in plain language. Every new term is explained when it first appears, and every module has figures, a case, a calculator, a skills checklist, and a self-assessment. Modules 9 to 14 rehearse the decisions that arrive with pressure attached: an owner, a family, a reporter, a regulator.</p>
""",
    "exam_draw": 40,
    "is_not": ("It is a training track written independently from published laws, regulations, guidelines, and research. It is not a "
               "license, a DOH or PhilHealth requirement, PSN attestation, CPD credit, or legal advice. It does not replace your appointment "
               "terms, your unit&rsquo;s approved policies, or the attending nephrologist, who is always asked for guidance on a patient&rsquo;s care."),
    "pathways_tag": "Five parts",
    "pathways_h2": "Nine weeks of study, in five parts",
    "pathways_nav": "Parts",
    "pathways_html": """
<p>The fourteen modules are grouped into five parts that follow the order a new clinical head meets the work: first the authority you hold, then the barriers that keep patients safe, then the days when the system is stressed, then the people and money that run it, and last the events that test it in public.</p>
{{cards:The five parts|Part 1 &middot; Authority and accountability::Modules 1 to 3. The appointment, licensing and inspection, and PhilHealth.|Part 2 &middot; Clinical and technical safety::Modules 4 to 6. Coverage and pathways, water and infection, risk and quality.|Part 3 &middot; Continuity and capacity::Modules 7 and 8. Disasters, safe capacity, supply, and the board brief.|Part 4 &middot; People, patients, and money::Modules 9 to 11. The workforce, access and conflict, and procurement.|Part 5 &middot; High-stakes events and change::Modules 12 to 14. Downtime and privacy, serious events, and new services.}}
""",
    "modules_h2": "Fourteen modules in five parts",
    "modules_intro": ("Study the modules in order. Each one starts from why a control exists, moves to what the evidence and the rules say, "
                      "and ends with what a clinical head does on Monday morning."),
    "syllabus_note": ("Each module takes about 60 to 90 minutes to read and work through, plus a practice session at your own unit "
                      "(about 18 to 20 hours of reading in all). Skills checklists are completed with a preceptor in simulation."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 8 questions drawn at random from a bank of 15; the mastery mark is 7 of 8 on two different sets. The end-of-track examination draws 40 questions from all fourteen banks. The capstone is a three-hour defense of a written unit plan before a senior clinical head, scored on ten gates, two of them critical.</p>
""",
    "sources_html": """
<p>The track is built from published sources. Philippine requirements follow the Department of Health (DOH) licensing and water orders, PhilHealth circulars, the Philippine Society of Nephrology (PSN) hemodialysis guidelines, and the laws on disaster risk reduction and data privacy.[[doh2012]][[dch_doh2013]][[dch_philhealth2024]][[dch_philhealth2024q]][[psn2024]][[dch_ra10121]][[dch_ra10173]] Clinical and operational statements follow the trials and guidelines they rest on, including the National Kidney Foundation Kidney Disease Outcomes Quality Initiative (KDOQI), the International Organization for Standardization (ISO) water standard, and the Centers for Disease Control and Prevention (CDC) dialysis recommendations.[[dch_kdoqi2015]][[dch_iso2024]][[dch_cdc_core]]</p>
<p>Where the evidence is strong, the text says so. Where a practice rests on observation, expert opinion, or local custom, the text says that instead. Where Philippine data are missing, the track uses data from the United States and other countries and says so. Regulatory statements were checked against public sources on November 24, 2026. One issuance, DOH Department Circular 2026-0112 on interim licensing of hemodialysis clinics, was confirmed by title only; its text must be read before any rule in it is applied.[[dch_doh2026]]</p>
""",
    "trainers_intro": ("A nephrology program director, a senior clinical head, or a hospital medical director can use these modules as the guided-study part of a clinical head&rsquo;s orientation. "),
    "trainer_h2": "Using the track to prepare a new clinical head",
    "trainer_html": """
<p>The track supports orientation; it does not replace it. A practical plan is one or two modules a week over nine weeks, each paired with a facilitated practice session at the learner&rsquo;s own unit, then the three-hour capstone. Head nurses, operations managers, quality leads, and claims staff should join the exercises, because the decisions in this track are made at a table, not alone.</p>
{{flow:Suggested sequence|Weeks 1 to 2::Modules 1 to 3. Build the authority matrix. Run an inspection tracer and a chart-to-claim trace.|Weeks 3 to 4::Modules 4 to 6. Run a shift-readiness huddle, a water-log review, and one risk assessment.|Weeks 5 to 6::Modules 7 and 8. Run the typhoon tabletop. Calculate safe capacity and reorder points.|Weeks 7 to 8::Modules 9 to 13. Role-play the owner, the family, and the reporter.|Week 9::Module 14 and the capstone defense.}}
<p>Keep signed assessments in the facility&rsquo;s approved system, and use fictional identifiers in every exercise.</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments: 7 of 8 on two different sets for each module, with every missed question reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated independently to a preceptor in simulation.</li>
<li>Capstone 8 of 10 or higher, with every critical gate passed.</li>
</ul>
<p>Completion is an Academy learning record. It is not CPD credit, PSN attestation, DOH eligibility, PhilHealth accreditation, or an appointment.</p>
""",
    "related": [("calc-dialysis-clinical-head-toolkit.html", "Twelve calculators for running a safe, accountable service."),
                ("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
}

P1, P2, P3, P4, P5 = ("Part 1 &middot; Authority and accountability", "Part 2 &middot; Clinical and technical safety",
                      "Part 3 &middot; Continuity and capacity", "Part 4 &middot; People, patients, and money",
                      "Part 5 &middot; High-stakes events and change")

_ROWS = [
    ("01", "governance-and-appointment", "Before You Sign: Authority and Appointment", P1,
     "What a clinical head owns, the authority matrix, the questions to settle with the owner, and when to refuse an appointment.",
     "A physician reading an appointment letter at a desk across from a clinic owner, a floor plan and a site list between them."),
    ("02", "licensing-and-inspection", "Licensing and Inspection Readiness", P1,
     "Which DOH rule governs what, changes that need approval first, the three-source tracer, and closing a finding with proof.",
     "A physician and a head nurse walking a dialysis unit with a floor plan, tracing the route from the entrance to a chair."),
    ("03", "philhealth-accreditation-and-claims", "PhilHealth: Accreditation, the Package, and the Claim", P1,
     "Provider status, the 156-session package and what it must include, the chart-to-claim trace, and talking to a patient about a disputed charge.",
     "A physician and a claims officer comparing a treatment record with a claim printout at a desk in a dialysis clinic."),
    ("04", "clinical-oversight-and-patient-rights", "Clinical Oversight: Coverage, Pathways, and Rights", P2,
     "Who covers each shift, the readiness huddle, care pathways that do not leak, the transfer handoff, and patient rights.",
     "A physician leading a short huddle with three nurses before the first shift, a patient list on a clipboard."),
    ("05", "infection-water-and-equipment", "Infection, Water, and Machines: The Invisible Barriers", P2,
     "Why dialysis is an infection-prone setting, what water can do to a patient, reading a water log, and two-signature release.",
     "A physician and a water technician examining a sample port and test log in a dialysis water room, carbon tanks behind them."),
    ("06", "risk-and-quality", "Risk Management and Proving Improvement", P2,
     "Writing a risk, scoring it honestly, the hierarchy of fixes, rates with denominators, and telling improvement from research.",
     "A physician and a quality lead in front of a run chart and risk register taped to the wall of a small dialysis office."),
    ("07", "disaster-and-continuity", "The Dialysis Clock: Disasters and Continuity", P3,
     "Why dialysis patients have a deadline in days, dependencies that fail together, the patient tracker, and a signed restart.",
     "A physician at a dialysis unit desk during typhoon rain, on the phone, a printed patient tracker and a map in front of her."),
    ("08", "capacity-supply-and-the-board", "Safe Capacity, Supply, and the Board Brief", P3,
     "Counting safe slots, the limiting resource, reorder points, and a one-page brief an owner can act on.",
     "A physician presenting a one-page brief to two clinic owners at a small conference table, a capacity chart on the screen."),
    ("09", "leading-the-workforce", "Leading the Workforce Under Pressure", P4,
     "Competence-matched staffing, protecting the person who speaks up, separating safety from discipline, and burnout.",
     "A physician speaking quietly with a charge nurse at the edge of a busy dialysis floor, an assignment board behind them."),
    ("10", "access-conflict-and-transitions", "Access, Conflict, and Transitions", P4,
     "Why patients miss sessions, safety before scheduling, involuntary transfer, social assistance, and closing referrals.",
     "A physician and a social worker sitting with a patient and her son in a quiet consultation room beside a dialysis unit."),
    ("11", "money-procurement-and-conflicts", "Money, Procurement, and Conflicts of Interest", P4,
     "Reading the finances, the cost of a shortage, qualifying a substitute, disclosure and recusal, and disputes between clinicians.",
     "A physician reviewing a supply forecast with an operations manager in a dialysis stockroom, boxes of dialyzers on the shelves."),
    ("12", "downtime-privacy-and-data", "When the System Goes Dark: Downtime and Privacy", P5,
     "The minimum safe data set, the paper bridge, reconciliation, and what the Data Privacy Act asks when a roster leaks.",
     "A physician and a nurse comparing a paper downtime record with a laptop screen at a dialysis nurses' station."),
    ("13", "serious-events-and-scrutiny", "Serious Events, Families, and Outside Scrutiny", P5,
     "The first fifteen minutes, looking for a shared exposure, talking with a family, the reporter on the line, and supporting staff.",
     "A physician speaking with a worried family in a private room near a dialysis unit, a nurse beside her."),
    ("14", "new-services-and-first-90-days", "New Services, Handover, and Your First 90 Days", P5,
     "Judging a new technology such as hemodiafiltration on evidence, staged launches with stop rules, handover, and a 30-60-90 plan.",
     "A physician walking a newly installed hemodiafiltration station with a biomedical engineer before it is released for use."),
]
MODULES = []
for _id, _slug, _title, _part, _sub, _brief in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part,
                    "card_img": f"{HUB}-{_id}-card.webp", "hero_brief": _HB + _brief})
