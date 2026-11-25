# -*- coding: utf-8 -*-
"""Dialysis Unit Owner (DUO) track: course definition in the POD package schema.
Built from Blueprint v2 (Dialysis Unit Owner folder, 09-blueprint-v2-improved.md). Every case, person and peso figure is fictional."""

HUB = "dialysis-unit-owner"
_HB = "Illustrated vignette, warm natural light, Filipino owners, staff and patients, modern hemodialysis unit, no text in image. "

COURSE = {
    "title": "Dialysis Unit Owner",
    "short": "Unit Owner",
    "hub_slug": HUB,
    "label": "Course for the people who own and govern hemodialysis services",
    "tag": "Administrative Staff",
    "icon": "🏛️",
    "no_branch": True,
    "audience": ("Owners and prospective owners of hemodialysis units &middot; investors, trustees, and board members &middot; "
                 "authorized governing representatives of single-site and multi-site services"),
    "audience_type": "Owners and governing boards of hemodialysis units",
    "level": "Governance level, no medical background needed; every clinical idea is explained in plain language",
    "review_date": "2026-11-25",
    "draw": 5,
    "mastery": "4 of 5",
    "exam_abbrev": ("PhilHealth: Philippine Health Insurance Corporation. CDC: Centers for Disease Control and Prevention. "
                    "DSCR: debt service coverage ratio. FTE: full-time equivalent. HEMO: the Hemodialysis Study. "
                    "ICH CAHPS: In-Center Hemodialysis Consumer Assessment of Healthcare Providers and Systems. "
                    "DOH: Department of Health. PSN: Philippine Society of Nephrology. PDD: PhilHealth Dialysis Database. "
                    "HMO: health maintenance organization. HHI: Herfindahl-Hirschman Index. FDA: Food and Drug Administration."),
    "exam_draw": 24,
    "exam_stratify": True,
    "keywords": ("dialysis unit owner training, dialysis clinic owner Philippines, hemodialysis governance, dialysis business ethics, "
                 "PhilHealth 6350 hemodialysis package, DOH dialysis licensing owner, dialysis break-even calculator, dialysis board quality dashboard, "
                 "for-profit dialysis outcomes, dialysis continuity typhoon"),
    "page_title": "Dialysis Unit Owner: A Governance Course",
    "desc": ("A free course for people who own and govern hemodialysis units: the owner's authority and its limits, kidney care for "
             "non-clinicians, Philippine licensing, protected clinical leadership, ethics, feasibility, capital, safe capacity, design, "
             "workforce, water and infection investment, PhilHealth stewardship, claims integrity, unit economics, cash, quality "
             "assurance, privacy, continuity, serious events, and responsible growth and exit."),
    "h1": "Dialysis Unit <em>Owner</em>",
    "sub": ("A course for the people who own and govern hemodialysis services. Learn what only an owner can decide, what an owner must "
            "never override, and how money, staffing, water, and data turn into safe treatment for people who cannot skip a session."),
    "disclaimer": ("Educational material for owners and governing boards. Academy learning completion record. This does not confer a DOH "
                   "license, PhilHealth accreditation, PSN attestation, professional eligibility, CPD credit or authority to undertake "
                   "clinical or technical duties. It does not replace current regulations, your entity&rsquo;s legal, tax, and labor "
                   "advisers, or the clinicians and technicians who own clinical and technical decisions."),
    "scope_note": ("This module is study material for owners and governing boards of adult maintenance hemodialysis services. The owner "
                   "supplies authority, resources, and assurance; clinical decisions belong to the attending nephrologist and the clinical "
                   "head, nursing assignments to the nursing lead, and technical release to the designated technician. Regulations and "
                   "payer rules change: confirm each one against the current issuance. Every case, person, and peso figure is fictional."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Owners and boards",
    "branch_blurb": ("For owners, investors and boards of dialysis units: authority and its limits, licensing, ethics, capital, safe "
                     "capacity, workforce, water and infection, PhilHealth, claims, money, quality, privacy, continuity, and exit."),
    "academy_meta": "24 modules &middot; 8 owner calculators &middot; a capstone",
    "hero_alt": "A dialysis unit owner walking the treatment floor with the head nurse, who is explaining a machine.",
    "start_h2": "The person who answers for the whole unit",
    "start_html": """
<p>Every hemodialysis unit has a person or a board that answers for all of it: the money, the building, the water, the staff, and, in the end, whether the people in the chairs are safe. That is the owner. Patients cannot skip dialysis the way a customer skips a shop. They come three times a week for life, or until a transplant, and a unit that closes or cuts corners does not lose customers. It loses patients.</p>
<p>An owner does not prescribe, assign nurses, or release a water system. An owner decides what the unit can afford, who leads it, what it will and will not do for money, and how it will know whether it is safe. Most of this course is about using that authority well and about the few decisions an owner must never take, however much a session is worth.</p>
{{cards:What this course will help you do|Know your lane::Map reserved, delegated, and protected decisions, and keep commercial pressure away from clinical and technical holds.|Understand the patient::Learn enough kidney physiology to see why the long weekend gap, a missed session, or a slow referral matters.|Build only what you can staff::Plan capacity from cleared staff and released water, not from installed chairs.|Follow the peso to the patient::See how a budget line becomes staffing, care, and outcomes, and what the evidence says about ownership and acquisitions.|Bill truthfully::Steward the PhilHealth package and charge patients honestly, in writing, before the first session.|Read the numbers yourself::Use eight owner calculators for break-even, capacity, staffing, cash, loans, projects, and the patient&rsquo;s yearly share.|Stay open through a crisis::Govern privacy, cyberattack, typhoon, and serious events so every patient is accounted for.}}
{{fig:duo00_calcs}}
<p>The course is written in plain language. Every clinical idea is explained when it first appears, and every module has a field case, a supervised exercise, and a self-assessment. The pesos in every example are invented for teaching; replace them with your own ledger.</p>
""",
    "is_not": ("It is a course written independently from published laws, regulations, guidelines, and research. It is not a license, an "
               "accreditation, a Department of Health (DOH) or PhilHealth requirement, CPD credit, or legal, tax, labor, or investment advice, "
               "and no regulator or society endorses it."),
    "pathways_tag": "Six stages",
    "pathways_h2": "Twenty-four modules in six stages",
    "pathways_nav": "Stages",
    "pathways_html": """
<p>The modules follow a deliberate order: authority and ethics first, then the service you build, then the people and safety systems inside it, then the payer and the money, then assurance, then resilience and transition. The financial plan comes after the safety plan on purpose. Revenue should rest on safely supported service, never the reverse.</p>
{{fig:duo00_map}}
{{cards:The six stages|Stage 1 &middot; Authority and ethics::Modules 1 to 5. The owner role, kidney care, licensing, protected clinical leadership, and patient rights.|Stage 2 &middot; The service you build::Modules 6 to 9. Feasibility, capital, safe capacity, and design and commissioning.|Stage 3 &middot; People and safety systems::Modules 10 to 13. Workforce, water and equipment, infection prevention, and procurement.|Stage 4 &middot; Payer and money::Modules 14 to 17. PhilHealth stewardship, claims integrity, unit economics, and cash.|Stage 5 &middot; Assurance::Modules 18 to 20. Quality dashboards, patient experience and growth, and information governance.|Stage 6 &middot; Resilience and transition::Modules 21 to 24. Disasters, serious events, expansion and exit, and the capstone.}}
""",
    "modules_h2": "Twenty-four modules in six stages",
    "modules_intro": ("Study the modules in order. Each one starts with a plain picture, traces how a governance choice reaches a patient, "
                      "shows what the evidence and the rules say, and ends with what an owner does at the next board meeting."),
    "syllabus_note": ("Plan about three hours per module (reading, the case, the calculator, and the supervised exercise); the capstone "
                      "takes six. The modules total 75 hours, and the final assessment and debrief two more: 77 hours in all. These are "
                      "Academy planning figures, not a regulatory requirement."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions drawn at random from a bank of 6; the mastery mark is 4 of 5 on two different sets. The end-of-course examination draws one question from every module, 24 in all, and the proposed pass mark is 20 of 24. Because the questions also appear in the modules, the capstone carries the main evidence of applied judgment: a written board pack, a signed decision log, and a first-ninety-days plan, defended before a panel that includes a clinical reviewer.</p>
""",
    "sources_html": """
<p>The course is built from published sources. Philippine requirements follow the Department of Health (DOH) licensing and water orders, PhilHealth circulars, the Philippine Society of Nephrology (PSN) hemodialysis guidelines, the Data Privacy Act, and the disaster risk reduction law.[[doh2012]][[dch_doh2013]][[dch_philhealth2024]][[psn2024]][[dch_ra10173]][[dch_ra10121]] Statements about outcomes follow the studies they rest on, including research on ownership, acquisitions, staffing, missed treatments, infection, cyberattacks, and disasters.[[duo_devereaux2002]][[duo_eliason2020]][[uom_plantinga2024]][[dch_foley2011]][[dch_rha2023]][[duo_neprash2022]][[uom_kelman2015]]</p>
<p>Most of that research is observational and from the United States. It shows associations, not proof, and the text says so each time. Where Philippine data are missing, the course says that too. Regulatory and payer figures were checked against public sources on November 25, 2026; confirm them before use.</p>
""",
    "trainers_intro": ("A board chair, an experienced owner, or a governance adviser working with the unit&rsquo;s clinical head can use these modules as the guided-study part of an owner&rsquo;s orientation. "),
    "trainer_h2": "Using the course to prepare an owner or a board",
    "trainer_html": """
<p>The course supports orientation; it does not replace it. A practical plan is two modules a week for twelve weeks, each paired with its supervised exercise at the learner&rsquo;s own unit, followed by the capstone. The clinical head, the head nurse, the technical lead, the unit manager, and the finance officer should join the exercises that touch their work, and a clinical reviewer should sit on the capstone panel.</p>
{{flow:Suggested sequence|Weeks 1 to 3::Modules 1 to 5. Charter, patient journey, compliance register, appointments, and conflicts register.|Weeks 4 to 5::Modules 6 to 9. Feasibility memo, capital plan, safe capacity sheet, and launch gate.|Weeks 6 to 7::Modules 10 to 13. Workforce plan, water and asset dashboard, infection resource plan, and supplier scorecard.|Weeks 8 to 9::Modules 14 to 17. Charge matrix, session-to-cash reconciliation, unit economics, and 13-week cash forecast.|Weeks 10 to 11::Modules 18 to 23. Dashboard, experience plan, access matrix, continuity map, serious-event checklist, and exit plan.|Week 12::Module 24, the capstone and portfolio defense.}}
<p>Use fictional or de-identified data in every exercise. Board reports never need patient names.</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments: 4 of 5 on two different sets for each module, with every missed question reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every supervised-exercise checklist demonstrated to the trainer.</li>
<li>Written portfolio of the 24 module outputs rated at least satisfactory.</li>
<li>End-of-course examination: 20 of 24, with missed items reviewed against their modules.</li>
<li>Capstone accepted by the panel with no critical failure. A high quiz score cannot compensate for an unsafe capstone decision.</li>
</ul>
<p>Academy learning completion record. This does not confer a DOH license, PhilHealth accreditation, PSN attestation, professional eligibility, CPD credit or authority to undertake clinical or technical duties.</p>
""",
    "related": [("calc-dialysis-owner-toolkit.html", "Eight calculators for break-even, capacity, staffing, cash, loans, projects, and the patient's share."),
                ("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement."),
                ("typhoon-disaster-preparedness-dialysis.html", "Typhoon preparedness for dialysis patients.")],
}

S1, S2, S3, S4, S5, S6 = ("Stage 1 &middot; Authority and ethics", "Stage 2 &middot; The service you build",
                          "Stage 3 &middot; People and safety systems", "Stage 4 &middot; Payer and money",
                          "Stage 5 &middot; Assurance", "Stage 6 &middot; Resilience and transition")

_ROWS = [
    ("01", "role-and-governance", "The Owner Role and the Governance Charter", S1, 3,
     "Legal entity, license, and appointees; reserved, delegated, and protected decisions; assurance that a control works; and the hold no owner overrides."),
    ("02", "kidney-care-and-patient-journey", "Kidney Care and the Patient Journey", S1, 3,
     "What the kidney does, why three sessions a week, the long weekend gap, missed sessions, and referral for transplant, home, or conservative care."),
    ("03", "licensing-and-compliance", "Philippine Licensing and the Compliance Register", S1, 3,
     "The Department of Health (DOH) license, PhilHealth accreditation, Philippine Society of Nephrology (PSN) attestation, local permits, and a register that proves each one."),
    ("04", "leadership-and-clinical-authority", "Leadership Appointments and Protected Clinical Authority", S1, 3,
     "Appointing a clinical head, a nursing lead, a technical lead, and a manager, with contract clauses that protect their judgment."),
    ("05", "ethics-and-patient-rights", "Ethics and Patient Rights in an Owner-Led Service", S1, 3,
     "Incentives that change care, conflicts of interest, grievances, and why involuntary discharge is a last resort."),
    ("06", "feasibility-and-community-access", "Feasibility and Community Access", S2, 3,
     "Need, travel time, competition, sensitivity analysis, and four gates before money is committed."),
    ("07", "capital-and-financing", "Capital Planning and Financing", S2, 3,
     "Sources and uses, debt and the debt service coverage ratio (DSCR), reserves, and distributions that wait for safety."),
    ("08", "safe-capacity-and-operating-model", "Safe Capacity and the Operating Model", S2, 3,
     "Station-sessions, staffed versus physical capacity, make-up slots, and the services a unit cannot run without."),
    ("09", "facility-design-and-commissioning", "Facility Design and Commissioning", S2, 3,
     "Zones and flows, isolation, the water room, commissioning tests, and the launch gate."),
    ("10", "workforce-and-employment", "Workforce Investment and Employment Oversight", S3, 3,
     "What the evidence says about staffing and outcomes, skill mix, full-time equivalents with relief, and the employer&rsquo;s duties."),
    ("11", "water-equipment-and-utilities", "Water, Equipment, and Utilities Assurance", S3, 3,
     "Why dialysis water can kill, the hold-and-release rule, the asset life cycle, and power and water backups."),
    ("12", "infection-prevention-investment", "Infection Prevention and Safety Investment", S3, 3,
     "Bloodstream infection risk, the core interventions, bloodborne viruses, and the owner&rsquo;s part in an outbreak."),
    ("13", "procurement-and-supply-chains", "Procurement, Supply Chains, and Conflicts", S3, 3,
     "Qualifying a substitute, related-party suppliers, stock runway, and a recall traced to the patient within an hour."),
    ("14", "philhealth-benefit-stewardship", "PhilHealth Participation and Benefit Stewardship", S4, 3,
     "The 6,350-peso package, eligibility and the dialysis database, what patients may be charged, and the yearly limit."),
    ("15", "claims-integrity-and-revenue", "Claims Integrity and Revenue Assurance", S4, 3,
     "The session-to-cash chain, exceptions and denials, and the line between correction and fraud."),
    ("16", "unit-economics-and-pricing", "Unit Economics and Transparent Pricing", S4, 3,
     "Fixed, variable, and step costs; contribution and break-even; sensitivity; and honest prices."),
    ("17", "cash-flow-and-controls", "Cash Flow, Working Capital, and Financial Controls", S4, 3,
     "Why profit is not cash, days sales outstanding, the 13-week forecast, and controls that stop money going missing."),
    ("18", "quality-dashboard-and-assurance", "Quality Dashboards and Board Assurance", S5, 3,
     "Indicators with denominators, run charts, what ownership studies show, and a dashboard that drives action."),
    ("19", "patient-experience-and-growth", "Patient Experience, Access, and Ethical Growth", S5, 3,
     "Hearing every patient, grievances as data, honest marketing, and growth only as fast as safe capacity."),
    ("20", "privacy-and-cybersecurity", "Privacy, Cybersecurity, and Information Governance", S5, 3,
     "The Data Privacy Act, ransomware and downtime, need-to-know access, and vendors who touch patient data."),
    ("21", "disaster-and-continuity", "Disasters, Emergency Coverage, and Continuity", S6, 3,
     "Why disasters kill dialysis patients, the dependency map, transfer agreements, and the restart gate."),
    ("22", "serious-events-and-insurance", "Serious Events, Insurance, and External Scrutiny", S6, 3,
     "The first hours after harm, honest disclosure, support for staff, insurance gaps, and regulators and media."),
    ("23", "expansion-and-responsible-exit", "Expansion, Acquisition, Succession, and Responsible Exit", S6, 3,
     "What happens after acquisitions, due diligence, succession, and closing or selling without losing a patient."),
    ("24", "integrated-owner-capstone", "Integrated Owner Capstone and the First 90 Days", S6, 6,
     "A board pack, a signed decision log, seventy-two hours of injects, and a first-ninety-days plan defended before a panel."),
]

MODULES = []
for _id, _slug, _title, _part, _hrs, _sub in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part,
                    "card_img": f"{HUB}-{_id}-{_slug}-card.webp", "hero_brief": _HB + _sub})
