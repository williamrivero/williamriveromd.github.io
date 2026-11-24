# -*- coding: utf-8 -*-
"""Dialysis Head Nurse: a study series for nurses who lead an adult maintenance hemodialysis unit.
Built in the same format and voice as the Physician on Duty track (pod-package). All content is written independently
from primary sources; no course material from any other training provider is used. Modules are authored in m01.py to
m13.py. Prompts for every figure are in ../IMAGE-PROMPTS.md."""

_HB = "Illustrated clinical vignette, warm natural light, Filipino staff and patients, modern hemodialysis unit, no text in image. "

COURSE = {
    "title": "Dialysis Head Nurse",
    "short": "Head Nurse",
    "hub_slug": "dialysis-head-nurse",
    "label": "Study series for dialysis head nurses",
    "tag": "Nursing Leadership",
    "icon": "🩺",
    "no_branch": True,
    "audience": "Head nurses and charge nurses in hemodialysis units &middot; senior dialysis nurses preparing to lead &middot; medical directors and nursing administrators who orient them",
    "audience_type": "Head nurses in hemodialysis units",
    "level": "Registered nurses with dialysis experience, written in plain language",
    "review_date": "2026-11-23",
    "draw": 8,
    "mastery": "7 of 8",
    "exam_draw": 39,
    "keywords": ("dialysis head nurse training Philippines, hemodialysis charge nurse, dialysis unit leadership, hemodialysis staffing ratio, "
                 "dialysis water safety, dialysis infection prevention, PhilHealth hemodialysis claims, dialysis disaster preparedness"),
    "page_title": "Dialysis Head Nurse: A Study Series",
    "desc": ("A free study series for nurses who lead a hemodialysis unit: opening a shift safely, reading trends across sessions, "
             "reconciling the order with the machine, protecting the access, keeping water and infection under control, leading in an "
             "emergency, staffing and coaching, PhilHealth records, improvement, disasters, and the schedule itself. Plain language, figures, a case, a skills "
             "checklist, and a self-assessment in every module."),
    "h1": "Dialysis <em>Head Nurse</em>",
    "sub": ("A study series for nurses who lead a hemodialysis unit. Learn why each check protects a patient, "
            "and what to do when the shift cannot open safely."),
    "disclaimer": ("Educational study material for nurses. Does not replace the attending nephrologist&rsquo;s orders, the unit&rsquo;s protocols, "
                   "required training and certification, or supervised practice."),
    "scope_note": ("This module is study material for head nurses in hemodialysis units. It explains the reasoning behind common decisions; it is not a protocol. "
                   "On the floor, follow your unit&rsquo;s protocol and ask the attending nephrologist for guidance. Doses, limits, and cut-off values are set by your unit. "
                   "Every case is fictional."),
    "branch_img": "dialysis-head-nurse-card.webp",
    "branch_role": "Head nurses",
    "branch_blurb": ("For nurses who lead a hemodialysis shift or unit: safe opening, staffing and delegation, water and infection control, "
                     "emergencies, records and PhilHealth, improvement, disasters, and the roster, absences, and replacements."),
    "academy_meta": "13 modules &middot; one track &middot; calculators in every module",
    "hero_alt": "A head nurse briefing her team at the entrance of a hemodialysis unit before the first patients arrive.",
    "start_h2": "The nurse who holds the floor",
    "start_html": """
<p>A hemodialysis (HD) unit runs on checks. Someone confirms that the water was tested, that each machine was released after repair, that enough nurses who can work alone are on the floor, and that the emergency cart is sealed. Someone notices that one patient&rsquo;s weight gain has crept up for three weeks, and that the afternoon shift loses half an hour every day to late starts. In most Philippine units, that someone is the head nurse.</p>
<p>Most head nurses learned the role by doing it. They were excellent dialysis nurses, and one day they were in charge. Clinical skill carries over. Much of the rest does not: reading a staffing rule, judging a water result, leading five people in a cardiac arrest, tracing a PhilHealth claim, and proving that a change worked.</p>
{{cards:What this series will help you do|Open safely::Decide whether a shift can open, and what to hold when it cannot.|Read the patient::Spot the trend across sessions that the single reading hides.|Reconcile::Make the order, the machine, and the record agree.|Protect::Keep the access, the water, and the station boundaries safe.|Lead::Assign roles in the first thirty seconds of an emergency.|Build the team::Staff, delegate, and coach so the next shift is safer.|Prove it::Measure, improve, and keep dialysis running through a typhoon.}}
<p>The series is written in plain language. Every new term is explained when it first appears, and every module has figures, a case, a calculator, a skills checklist, and a self-assessment.</p>
""",
    "is_not": ("It is study material written independently from published guidelines, textbooks, research, and Philippine regulations. It is not a certificate. "
               "The Department of Health (DOH) licensing rules for dialysis facilities and the Philippine Society of Nephrology (PSN) standards for hemodialysis clinics "
               "set the requirements for dialysis nurses and head nurses, including structured renal dialysis training and life support certificates.[[doh2012]][[psn2024]] "
               "This series is not that training and is not affiliated with or endorsed by DOH, PSN, or PhilHealth. Use it to prepare, to review, and to support orientation in your own unit."),
    "pathways_tag": "One track, thirteen weeks",
    "pathways_h2": "One module a week",
    "pathways_nav": "Plan",
    "pathways_html": """
<p>The thirteen modules follow a head nurse&rsquo;s own week: opening the shift, reading the patients, running the session, protecting the access, the water, and the stations, leading in an emergency, building the team, partnering with patients, keeping the records, improving, and keeping the unit open when the roads close. Module 13 covers the roster itself: how many nurses you need, swaps, absences, lateness, and replacements.</p>
{{cards:How to use the series|Read::About an hour and a half per module, with the calculator open beside you.|Practice::About two hours with a facilitator on the unit, using the skills checklist.|Prove::A final exam, three observed stations, and a 90-day improvement plan.}}
""",
    "modules_h2": "Thirteen modules in five parts",
    "modules_intro": ("Study the modules in order. Each one builds on the physiology and the habits of the one before."),
    "syllabus_note": "Each module takes about 75 to 90 minutes to read and work through. Skills checklists are completed on the unit with a facilitator.",
    "assessment_html": """
<p>The questions at the end of each module are for practice. Each visit draws eight from a bank of fifteen, and every question explains its best answer. The questions were written for this series.</p>
<p>Competence is shown on the unit, not on a screen: opening a shift, leading a bleeding emergency, containing a water problem, coaching a nurse, and building a fair roster. Each module has a skills checklist for a facilitator, usually the chief nurse, the medical director, or an experienced head nurse, to complete while watching you work. The final assessment adds a 13-item exam, four observed stations, and a written improvement plan.</p>
""",
    "sources_html": """
<p>The series is built from published sources. Physiology follows standard dialysis texts.[[daugirdas2015]] Clinical statements follow the guidelines of Kidney Disease: Improving Global Outcomes (KDIGO), the National Kidney Foundation Kidney Disease Outcomes Quality Initiative (KDOQI), and the research they rest on.[[hn_kdigo_anemia2026]][[hn_kdoqi2015]][[hn_lok2020]] Philippine requirements come from the DOH licensing and water orders, the PSN standards, the Philippine Nursing Act, and PhilHealth circulars.[[doh2012]][[hn_doh2013]][[psn2024]][[hn_ra9173]][[hn_philhealth2024]] Each module lists its own sources.</p>
<p>Where the evidence is strong, the text says so. Where a practice rests on observation, expert opinion, or local custom, the text says that instead. Limits, doses, and cut-off values are left to your unit&rsquo;s protocol and the attending nephrologist. Where Philippine data are missing, the series uses data from the United States and other countries and says so.</p>
""",
    "trainers_intro": ("A chief nurse, medical director, or experienced head nurse can use these modules as the guided-study part of leadership orientation. "),
    "trainer_h2": "Using the series to prepare a new head nurse",
    "trainer_html": """
<p>The series supports orientation; it does not replace it. A practical plan is one module a week with a facilitated practice session, two shifts shadowing an experienced head nurse, and supervised charge shifts, with the checklists signed along the way.</p>
{{flow:Suggested sequence|Weeks 1 to 4::Modules 1 to 4. Shadow two opening huddles. Complete the opening-gate and access checklists.|Weeks 5 to 8::Modules 5 to 8. Lead an infection observation audit and a water tabletop. Run one emergency drill as team leader.|Weeks 9 to 13::Modules 9 to 13. Run a claims tracer. Start one improvement test. Run a typhoon tabletop. Build a two-week roster.|Final::Exam, three observed stations, and the 90-day plan presented to the medical director.}}
<p>Record the nurse&rsquo;s license, renal dialysis training certificate, and life support certificates, which DOH and PSN expect.[[doh2012]][[psn2024]]</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments: 7 of 8 on two different sets for each module, with every missed question reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated satisfactorily to a facilitator.</li>
<li>Final exam 11 of 13 or higher, all four stations passed with every critical criterion, and the 90-day plan scored 8 of 10 or higher.</li>
<li>Current license, renal dialysis training, and life support certificates on file.</li>
</ul>
<p>These are proposals for each unit to adapt.</p>
""",
    "related": [("calc-dialysis-head-nurse-toolkit.html", "Thirteen calculators for running a safe shift."),
                ("hemodialysis-complications.html", "The main complications of a session, written for patients and clinicians."),
                ("code-blue-acls-dialysis-unit.html", "Cardiac arrest response in a dialysis unit.")],
}
P1, P2, P3, P4, P5 = ("Part 1 &middot; Opening the shift", "Part 2 &middot; Keeping the unit safe",
                      "Part 3 &middot; Leading people", "Part 4 &middot; Records, quality, and continuity",
                      "Part 5 &middot; The schedule and the people on it")
_ROWS = [
    ("01", "role-and-accountability", "Your Role on the Dialysis Floor", P1,
     "What a head nurse decides and what belongs to others, the five gates before opening, and the evidence a unit must keep.",
     "A head nurse briefing four nurses at the entrance of a dialysis unit before patients arrive, emergency cart and water room door in the background."),
    ("02", "renal-assessment-and-continuity", "Reading Trends Across Sessions", P1,
     "What builds up between sessions, why fast fluid removal drops pressure, which findings need action now, and how to close a result loop.",
     "A head nurse reviewing a weight and blood pressure trend on a tablet beside a patient being weighed before dialysis."),
    ("03", "prescription-and-safe-treatment", "The Order, the Machine, and the Record", P1,
     "How each line of the order works, the three-way check before connection, the dose of dialysis, and the minutes lost to short sessions.",
     "Two nurses reading a dialysis order aloud against a machine screen before connecting a patient."),
    ("04", "vascular-access-and-bleeding", "Protecting the Access", P2,
     "Examining the fistula, graft, and catheter, why the alarm misses a dislodged needle, and the first minute of access bleeding.",
     "A nurse examining a forearm fistula with a stethoscope while the patient watches, the arm uncovered on a pillow."),
    ("05", "infection-prevention", "Making Infection Prevention Visible", P2,
     "Why dialysis patients and units are prone to infection, the core interventions, audits with honest numbers, and a possible cluster.",
     "A head nurse observing hand hygiene at a dialysis station from a short distance, clipboard in hand."),
    ("06", "water-equipment-and-supplies", "Water, Machines, and Supplies", P2,
     "Why drinking water is not dialysis water, what each contaminant does, reading the water log, and the three documents for restart.",
     "A head nurse and a water technician checking a chlorine test kit beside the carbon tanks in a dialysis water room."),
    ("07", "deterioration-and-emergencies", "Leading the First Minutes of an Emergency", P3,
     "Whether the circuit is the cause or a bystander, when blood is not returned, the five voices, and the transfer handoff.",
     "A head nurse directing a small team at one dialysis chair during an emergency while another nurse watches the other patients."),
    ("08", "staffing-delegation-and-coaching", "Staffing, Delegation, and Coaching", P3,
     "How thin staffing reaches the patient, building a safe assignment, the five rights of delegation, and feedback that changes practice.",
     "A head nurse updating an assignment board with a nurse and an orientee before the shift."),
    ("09", "patient-partnership", "Partnering With Patients", P3,
     "Why patients shorten or miss sessions, teach-back, routine symptom questions, and closing referrals.",
     "A head nurse sitting at eye level with a patient in a dialysis chair, listening, the patient's daughter beside them."),
    ("10", "documentation-and-philhealth", "From the Chart to the PhilHealth Claim", P4,
     "Why documentation is a clinical act, the current PhilHealth hemodialysis rules, the claims tracer, and correcting a record.",
     "A head nurse and a billing officer comparing a nursing record with a machine log at a desk."),
    ("11", "incidents-and-improvement", "Learning From Incidents and Proving Improvement", P4,
     "Responding and reconstructing, the hierarchy of fixes, defining a measure, reading a run chart, and testing a change.",
     "A head nurse leading a short huddle in front of a run chart taped to a wall in a dialysis unit."),
    ("12", "disaster-and-service-leadership", "Keeping Dialysis Running Through a Disaster", P4,
     "Why dialysis patients have a deadline in days, preparing before the season, prioritizing with the physician, and a signed restart.",
     "A head nurse on the phone at a dialysis unit desk during heavy rain, a printed patient list and a map in front of her."),
    ("13", "scheduling-and-attendance", "The Schedule, Absences, and Replacements", P5,
     "How many nurses the roster needs, rest between shifts, fair swaps, same-day absences, lateness and due process, and replacing a nurse who leaves.",
     "At 5:20 in the morning a head nurse reads a message on her phone at the nurses' station and reaches for the desk telephone; the roster board behind her has one empty slot."),
]
MODULES = []
for _id, _slug, _title, _part, _sub, _brief in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part,
                    "card_img": f"dialysis-head-nurse-{_id}-card.webp", "hero_brief": _HB + _brief})
