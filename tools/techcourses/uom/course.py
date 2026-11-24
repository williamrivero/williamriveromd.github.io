# -*- coding: utf-8 -*-
"""Dialysis Unit Operations Manager / Unit Manager in Hospital (UOM/UMH) track: course definition in the POD package schema.
Module text is generated from the v2 Markdown packet in src/ by packet_to_package.py. Every case and record is fictional."""

HUB = "dialysis-unit-manager"
_HB = "Illustrated vignette, warm natural light, Filipino staff and patients, modern hemodialysis unit, no text in image. "

COURSE = {
    "title": "Dialysis Unit Operations Manager",
    "short": "Unit Manager",
    "hub_slug": HUB,
    "label": "Training track for operations managers of freestanding and hospital hemodialysis units",
    "tag": "Administrative Staff",
    "icon": "🗂️",
    "no_branch": True,
    "audience": ("Operations managers of freestanding hemodialysis units (UOM) &middot; unit managers of hospital dialysis services (UMH) "
                 "&middot; head nurses, administrators, and accounting staff who share the manager&rsquo;s work"),
    "audience_type": "Hemodialysis unit operations managers",
    "level": "Managers and supervisors in adult hemodialysis services, written in plain language",
    "review_date": "2026-11-24",
    "draw": 5,
    "mastery": "4 of 5",
    "keywords": ("dialysis unit manager Philippines, hemodialysis operations manager training, dialysis unit administration, DOH hemodialysis "
                 "licensing, PhilHealth hemodialysis 156 sessions, dialysis water quality, dialysis staffing ratio, dialysis infection control, "
                 "dialysis payroll and benefits, dialysis business continuity typhoon"),
    "page_title": "Dialysis Unit Operations Manager: A Training Track",
    "desc": ("A free training track for people who run hemodialysis units: decision rights, licensing and inspection, staffing and "
             "competency, capacity, infection prevention, water readiness, emergencies, supplies, quality data, PhilHealth claims and "
             "privacy, budgets, continuity, freestanding and hospital operations, leadership, accounting, payroll, and benefits."),
    "h1": "Dialysis Unit <em>Operations Manager</em>",
    "sub": ("A training track for the person who keeps a hemodialysis unit running, built on Department of Health (DOH), PhilHealth, and Philippine Society of Nephrology (PSN) requirements. Learn who decides what, how to keep the evidence "
            "current, and what to do when staff, water, power, or money run short."),
    "disclaimer": ("Educational material for unit managers and supervisors. Completing it is an Academy learning record only. It does not "
                   "confer CPD units, Department of Health (DOH) or PhilHealth eligibility, or a management appointment, and it does not replace current regulations, "
                   "your facility&rsquo;s approved policies, or legal, tax, or labor advice."),
    "scope_note": ("This module is study material for operations managers of adult hemodialysis services. The manager runs systems; clinical "
                   "decisions belong to the attending nephrologist, the physician on duty, and the nursing lead, and technical release belongs "
                   "to the designated technician. Regulations, wage orders, and contribution tables change: confirm each rule against the "
                   "current issuance before you rely on it. Every case and record is fictional."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Unit managers",
    "branch_blurb": ("For operations managers of freestanding and hospital dialysis units: decision rights, licensing, staffing, capacity, "
                     "infection, water, emergencies, supplies, quality, claims, money, payroll, and benefits."),
    "academy_meta": "19 modules &middot; freestanding and hospital paths &middot; a capstone",
    "hero_alt": "A dialysis unit manager at a huddle board, with ribbons leading to the clinical team, the water room, the claims desk, and the staff roster.",
    "start_h2": "The person who keeps the unit open",
    "start_html": """
<p>A hemodialysis unit runs on a timetable that patients cannot skip. Each patient needs a chair, a tested machine, released water, a competent nurse, a physician on duty, the right supplies, and a claim that is paid, three times a week, every week. The operations manager is the person who makes sure those pieces arrive together, and who notices first when one of them will not.</p>
<p>You do not prescribe, assign nurses, or release a water system. You run the systems that let the people who do those things work safely: the roster, the evidence index, the schedule, the stockroom, the data, the claims, the budget, the payroll, and the plan for the day the power fails. Much of this track is about knowing which decisions are yours, which belong to someone else, and how to make sure every decision has an owner.</p>
{{fig:uom00_map}}
{{cards:What this track will help you do|Know who decides::Map decision rights, run a closed-loop opening huddle, and escalate so someone owns the problem.|Stay inspection-ready::Keep an evidence index current and write a corrective action that proves the fix worked.|Match capacity to safe staffing::Count stations, staff, and slots, and protect the long-gap day.|Keep the invisible barriers up::Close the loop on serology results, water logs, alarms, and recalls.|Follow the money::Trace a session from the chart to the PhilHealth payment, and a peso from the budget to the bank.|Pay people correctly::Run attendance, payroll, and statutory remittances that staff and regulators can trust.|Keep treating through a typhoon::Plan outages, transfers, and restarts so every patient is accounted for.}}
<p>The track is written in plain language. Every new term is explained when it first appears. Each module has figures, a field case, a supervised-practice checklist, and a self-assessment. Module 13 is for freestanding units and Module 14 for hospital units; study the one that fits your setting, or both.</p>
""",
    "exam_draw": 40,
    "is_not": ("It is a training track written independently from published laws, regulations, guidelines, and research. It is not a license, "
               "a Department of Health (DOH) or PhilHealth requirement, CPD credit, or legal, tax, or labor advice. It does not replace your appointment terms, your "
               "unit&rsquo;s approved policies, or the clinicians and technicians who own clinical and technical decisions."),
    "pathways_tag": "Four parts",
    "pathways_h2": "Nineteen modules in four parts",
    "pathways_nav": "Parts",
    "pathways_html": """
<p>The modules follow the order a new manager meets the work: first the authority and the barriers that keep patients safe, then the setting you work in, then the people and money behind the service, and last a capstone that joins them.</p>
{{cards:The four parts|Part 1 &middot; Running a safe unit::Modules 1 to 12. Decision rights, licensing, staffing, capacity, infection, water, emergencies, supplies, quality, claims, budgets, and continuity.|Part 2 &middot; Your setting::Module 13 for freestanding units, Module 14 for hospital units.|Part 3 &middot; People and money::Modules 15 to 18. Leadership and patient experience, accounting and controls, attendance and payroll, and benefits and remittances.|Part 4 &middot; Capstone::Module 19. An integrated readiness exercise and portfolio defense.}}
""",
    "modules_h2": "Nineteen modules in four parts",
    "modules_intro": ("Study the modules in order. Each one starts from why a control exists, moves to what the evidence and the rules say, "
                      "and ends with what a manager does on Monday morning."),
    "syllabus_note": ("Each module takes about 40 to 45 minutes to read, plus a 45-minute supervised practice at your own unit (the capstone "
                      "practice runs 120 minutes): about 14 hours of reading and 15 hours of practice in all."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions drawn at random from a bank of 15; the mastery mark is 4 of 5 on two different sets. The end-of-track examination draws 40 questions from all nineteen banks. The capstone is a timed readiness exercise followed by a portfolio defense before a senior manager and the unit&rsquo;s clinical leads.</p>
""",
    "sources_html": """
<p>The track is built from published sources. Philippine requirements follow the Department of Health (DOH) licensing and water orders, PhilHealth circulars, the Philippine Society of Nephrology (PSN) hemodialysis guidelines, the Data Privacy Act, the Labor Code, and the current wage and contribution issuances.[[doh2012]][[dch_doh2013]][[dch_philhealth2024]][[psn2024]][[dch_ra10173]][[uom_laborcode]] Clinical and operational statements follow the trials, cohorts, and guidelines they rest on, including the Centers for Disease Control and Prevention (CDC) dialysis recommendations and the International Organization for Standardization (ISO) water standard.[[uom_cdc2001]][[iso23500_1]][[uom_starmer2014]]</p>
<p>Where the evidence is strong, the text says so. Where a practice rests on observation, regulation, or expert opinion, the text says that instead. Where Philippine data are missing, the track uses data from the United States and other countries and says so. Regulatory and contribution figures were checked against public sources on November 24, 2026; they change often, so confirm them before use.</p>
""",
    "trainers_intro": ("A unit administrator, a senior operations manager, or a hospital department head can use these modules as the guided-study part of a new manager&rsquo;s orientation. "),
    "trainer_h2": "Using the track to prepare a new unit manager",
    "trainer_html": """
<p>The track supports orientation; it does not replace it. A practical plan is two modules a week over ten weeks, each paired with the supervised practice at the learner&rsquo;s own unit, then the capstone. Head nurses, the medical director, the water and biomedical technicians, and accounting staff should join the exercises that touch their work.</p>
{{flow:Suggested sequence|Weeks 1 to 3::Modules 1 to 6. Decision-rights map, evidence index, roster, capacity, infection, and water logs.|Weeks 4 to 6::Modules 7 to 12. Emergency drill, recall exercise, run chart, claim trace, budget, and outage plan.|Week 7::Module 13 or 14 for your setting.|Weeks 8 to 9::Modules 15 to 18. Coaching, month-end close, payroll cutoff, and remittance reconciliation.|Week 10::Module 19, the capstone exercise and portfolio defense.}}
<p>Keep signed assessments in the facility&rsquo;s approved system, and use fictional or de-identified data in every exercise.</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments: 4 of 5 on two different sets for each module, with every missed question reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every supervised-practice checklist demonstrated to a preceptor.</li>
<li>Capstone portfolio accepted by the review panel.</li>
</ul>
<p>Completion is an Academy learning record. It is not CPD credit, Department of Health (DOH) or PhilHealth eligibility, or a management appointment.</p>
""",
    "related": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement."),
                ("typhoon-disaster-preparedness-dialysis.html", "Typhoon preparedness for dialysis patients."),
                ("calc-dialysis-clinical-head-toolkit.html", "Calculators for safe capacity, supply, and continuity.")],
}

P1, P2, P3, P4 = ("Part 1 &middot; Running a safe unit", "Part 2 &middot; Your setting",
                  "Part 3 &middot; People and money", "Part 4 &middot; Capstone")

_ROWS = [
    ("01", "role-and-authority", "Who Runs the Dialysis Unit", P1,
     "Decision rights, the four authority lines, the closed-loop opening huddle, and escalation that ends with an owner."),
    ("02", "licensure-and-accreditation", "Licensure, Accreditation, and Survey Readiness", P1,
     "What the Department of Health (DOH) license, PhilHealth accreditation, and Philippine Society of Nephrology (PSN) attestation each cover, the evidence index, tracers, and a corrective and preventive action (CAPA) that works."),
    ("03", "workforce-and-competency", "Staffing, Rostering, and Competency", P1,
     "Ratios as ceilings, the relief factor, the competency matrix, and reallocating safely after an absence."),
    ("04", "capacity-and-access", "Capacity, Access, and Patient Flow", P1,
     "Station-sessions, the long-gap day, rescheduling after a missed session, referrals, and holiday weeks."),
    ("05", "infection-prevention", "Infection Prevention and Surveillance", P1,
     "How infections reach dialysis patients, the Centers for Disease Control and Prevention (CDC) core interventions, rates with denominators, and serology results that trigger action."),
    ("06", "water-safety", "Water and Dialysate Readiness", P1,
     "The water pathway, the log a manager must read, completeness checks, and the hold-and-release rule."),
    ("07", "incident-response", "Emergency Readiness and Incident Command", P1,
     "Incident command on a dialysis floor, the readiness checklist, alarms, drills, and evacuation."),
    ("08", "assets-and-inventory", "Equipment, Supplies, and Procurement", P1,
     "The asset register, lot traceability, reorder points, qualifying a substitute, and a one-hour recall."),
    ("09", "quality-and-data", "Quality Measurement and Improvement", P1,
     "Indicators with definitions, the data dictionary, run charts, Plan-Do-Study-Act (PDSA) cycles, and the quality assessment and performance improvement (QAPI) meeting."),
    ("10", "billing-and-information", "PhilHealth Claims, Documentation, and Privacy", P1,
     "The session-to-payment chain, where claims fail, the 156-session cap, and need-to-know privacy."),
    ("11", "finance-and-value", "Budgeting, Cost per Treatment, and Cash", P1,
     "Cost per treatment, break-even, revenue recognition versus cash, and why a profitable unit can run out of money."),
    ("12", "business-continuity", "Continuity During Outages and Disasters", P1,
     "The dialysis clock, a phased typhoon plan, outage autonomy, partner units, and a signed restart."),
    ("13", "freestanding-operations", "Running a Freestanding Unit", P2,
     "The freestanding ecosystem, transfers to hospital, healthcare waste, utilities, and contracts."),
    ("14", "hospital-operations", "Managing Hospital Dialysis Interfaces", P2,
     "Wards, the intensive care unit (ICU), and the emergency room as customers, structured handoffs, and balancing outpatient and inpatient demand."),
    ("15", "team-and-patient-experience", "Leadership, Communication, and Patient Experience", P3,
     "Burnout and safety, coaching conversations, grievances that become system fixes, and the so-called difficult patient."),
    ("16", "unit-accounting", "Unit Accounting, Internal Controls, and Month-End Close", P3,
     "Session-to-cash, segregation of duties, the three-way match, imprest funds, and investigating a variance."),
    ("17", "attendance-and-payroll", "Attendance, Timekeeping, and Salary Controls", P3,
     "Roster to timecard to payroll, premium pay, the payroll cutoff review, and a payslip staff can check."),
    ("18", "employee-benefits", "Employee Benefits, Leave, and Payroll Remittances", P3,
     "SSS, PhilHealth, and Pag-IBIG contributions, the remittance trace, 13th-month pay, and statutory leaves."),
    ("19", "integrated-practice", "Integrated Readiness and Improvement Capstone", P4,
     "A 72-hour typhoon exercise with injects, the integrated readiness dashboard, and a portfolio defense."),
]
MODULES = []
for _id, _slug, _title, _part, _sub in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part,
                    "card_img": f"{HUB}-{_id}-{_slug}-card.webp", "hero_brief": _HB + _sub})
