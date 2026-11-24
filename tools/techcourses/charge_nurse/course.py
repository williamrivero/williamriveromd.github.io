# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse: a study series for the registered nurse who takes charge of one hemodialysis shift.
Built in the same format and voice as the Physician on Duty and Head Nurse tracks. All content is written independently
from primary sources; no course material from any other training provider is used. Modules are authored in m01.py to
m18.py. Blueprint: CHARGE-NURSE-BLUEPRINT-v2.md; prompts for every image: CHARGE-NURSE-IMAGE-PROMPTS.md
(both in /Volumes/Storage/Renal Care Academy/Charge Nurse/v2). DRAFT: awaiting Dr. Rivero's clinical sign-off."""

_HB = "Illustrated clinical vignette, warm natural light, Filipino staff and patients, modern hemodialysis unit, no text in image. "

COURSE = {
    "title": "Dialysis Charge Nurse",
    "short": "Charge Nurse",
    "hub_slug": "dialysis-charge-nurse",
    "label": "Study series for dialysis charge nurses",
    "tag": "Nephrology Nursing &middot; Role",
    "icon": "🧭",
    "no_branch": True,
    "audience": "Experienced hemodialysis nurses who take charge of a shift &middot; nurses being prepared for charge duty &middot; head nurses and educators who orient them",
    "audience_type": "Charge nurses in hemodialysis units",
    "level": "Registered nurses with dialysis experience, written in plain language",
    "review_date": "2026-11-24",
    "draw": 8,
    "mastery": "7 of 8",
    "exam_draw": 40,
    "keywords": ("dialysis charge nurse training Philippines, hemodialysis charge nurse, dialysis shift leadership, nurse assignment acuity, "
                 "intradialytic hypotension nursing, dialysis handoff I-PASS, dialysis emergency team leader, dialysis staffing ratio DOH PSN"),
    "page_title": "Dialysis Charge Nurse: A Study Series",
    "desc": ("A free study series for the nurse in charge of a hemodialysis shift: the opening sweep, a safe assignment, the live board, "
             "risk before connection, mid-session surveillance, the access, medicines, infection, water, emergencies, downtime, "
             "handoffs, delegation, patients and families, the record, and the integrated shift. Plain language, worked scenarios, a case, "
             "a skills checklist, and a self-assessment in every module."),
    "h1": "Dialysis <em>Charge Nurse</em>",
    "sub": ("A study series for the nurse who holds the next four hours of a hemodialysis unit. Learn why each check protects a patient, "
            "who decides what, and what to do when two things go wrong at once."),
    "disclaimer": ("Educational study material for nurses. Does not replace the attending nephrologist&rsquo;s orders, the unit&rsquo;s protocols, "
                   "required training and certification, or supervised practice."),
    "scope_note": ("This module is study material for charge nurses in hemodialysis units. It explains the reasoning behind common decisions; it is not a protocol. "
                   "On the floor, follow your unit&rsquo;s protocol and always ask the attending nephrologist for guidance. Doses, limits, and cut-off values are set by your unit. "
                   "Every case is fictional."),
    "branch_img": "dialysis-charge-nurse-card.webp",
    "branch_role": "Charge nurses",
    "branch_blurb": ("For the nurse in charge of a dialysis shift: opening the floor, a safe assignment, risk before connection, mid-session surveillance, "
                     "the first ten minutes of an emergency, handoffs that close the loop, and coaching on the floor."),
    "academy_meta": "18 modules &middot; one track &middot; a shift toolkit",
    "hero_alt": "A charge nurse at the center of a dialysis unit at dawn directing four staff members to their stations as the first patients are seated.",
    "start_h2": "The nurse who holds the next four hours",
    "start_html": """
<p>A head nurse plans the unit&rsquo;s month. A charge nurse holds the next four hours. At 5:45 in the morning the charge nurse is the person who knows that the machine at Bed 6 was released at 5:30, that the nurse covering Beds 9 to 12 has never connected a catheter alone, that Mr. Reyes gained 4.1 kilograms over the weekend, and that the physician on duty is on his way from the ward.</p>
<p>When one patient&rsquo;s pressure falls at 7:10 and another patient&rsquo;s needle alarm sounds at 7:11, the charge nurse decides who goes where. Most charge nurses learn this by doing it, often on the day the regular charge nurse calls in sick. Clinical skill carries over. Much of the rest does not: reading a staffing rule, building an assignment by need rather than headcount, keeping the whole floor in view while your own hands are busy, and saying the words that move a problem to the person who can fix it.</p>
{{cards:What this series will help you do|Open safely::Run five gates before the first connection, and hold with an owner and a time when one is closed.|Assign by need::Weight patients by what they need and match tasks to what each nurse can do alone.|See the floor::Keep a live board, round by the clock, and protect high-risk tasks from interruption.|Catch trouble early::Sort risk before connection and spot falling pressure, low sugar, and the patient who goes quiet.|Lead::Give each person one job in an emergency, and keep someone watching everyone else.|Close loops::Hand off actions and owners, not just facts, and delegate within the five rights.|Improve::Keep an honest record and make one recurring problem smaller.}}
<p>Charge duty is a role a staff nurse takes for a shift. It is not the head nurse post, which carries continuing responsibility for the unit and has its own track. Completing this series does not appoint anyone to either role; appointment is the employer&rsquo;s decision.</p>
""",
    "is_not": ("It is study material written independently from published guidelines, textbooks, research, and Philippine regulations. It is not a certificate. "
               "The Department of Health (DOH) licensing rules for dialysis facilities and the Philippine Society of Nephrology (PSN) standards for hemodialysis clinics "
               "set the requirements for dialysis nurses, including structured renal dialysis training and life support certificates.[[doh2012]][[psn2024]] "
               "Neither defines the charge nurse role separately. This series is not that training and is not affiliated with or endorsed by DOH, PSN, or PhilHealth. "
               "Use it to prepare, to review, and to support orientation in your own unit."),
    "pathways_tag": "One track, twelve weeks",
    "pathways_h2": "A module and a half a week",
    "pathways_nav": "Plan",
    "pathways_html": """
<p>The eighteen modules follow a charge shift from the first gate to the last handoff. Part 1 opens the floor. Part 2 watches the patients across many chairs. Part 3 guards the safety systems: infection, water, emergencies, and downtime. Part 4 is about people: handoffs, delegation, coaching, patients, and families. Part 5 brings it together: the record, improvement, ethics, and an integrated shift.</p>
{{cards:How to use the series|Read::About an hour and a half per module, with the shift toolkit open beside you.|Practice::About two hours with a facilitator on the unit, using the skills checklist.|Prove::A final exam, observed simulation stations, six supervised shifts, and one improvement project.}}
""",
    "modules_h2": "Eighteen modules in five parts",
    "modules_intro": ("Study the modules in order. Each one builds on the habits of the one before."),
    "syllabus_note": "Each module takes about 75 to 90 minutes to read and work through. Skills checklists are completed on the unit with a facilitator.",
    "assessment_html": """
<p>The questions at the end of each module are for practice. Each visit draws eight from a bank of fifteen, and every question explains its best answer. The questions were written for this series.</p>
<p>Competence is shown on the unit, not on a screen: opening a shift, building an assignment, leading a deterioration or bleeding emergency, holding for a water problem, handing off, and coaching. Each module has a skills checklist for a facilitator, usually the head nurse or an experienced charge nurse, to complete while watching you work. The final assessment adds an exam, seven observed stations, six supervised shifts, and an improvement project.</p>
""",
    "sources_html": """
<p>The series is built from published sources. Physiology follows standard dialysis texts.[[daugirdas2015]] Clinical statements follow the guidelines of the National Kidney Foundation Kidney Disease Outcomes Quality Initiative (KDOQI), the European Best Practice Guidelines, the United States Centers for Disease Control and Prevention, and the research they rest on.[[hn_kdoqi2015]][[ebpg2007]][[hn_cdc_core]] Philippine requirements come from the DOH licensing and water orders, the PSN standards, and PhilHealth circulars.[[doh2012]][[hn_doh2013]][[psn2024]][[hn_philhealth2024]] Leadership and communication content draws on research on handoffs, huddles, interruptions, delegation, and nurse staffing.[[hn_starmer2014]][[cn_westbrook2010]][[cn_ana_ncsbn2019]] Each module lists its own sources.</p>
<p>Where the evidence is strong, the text says so. Where a practice rests on observation, expert opinion, or local custom, the text says that instead. Limits, doses, and cut-off values are left to your unit&rsquo;s protocol and the attending nephrologist. Where Philippine data are missing, the series uses data from the United States and other countries and says so.</p>
""",
    "trainers_intro": ("A head nurse, nurse educator, or experienced charge nurse can use these modules as the guided-study part of charge-nurse orientation. "),
    "trainer_h2": "Using the series to prepare a charge nurse",
    "trainer_html": """
<p>The series supports orientation; it does not replace it. A practical plan is a module and a half a week, a facilitated practice session each week, and six supervised shifts with the checklists signed along the way.</p>
{{flow:Suggested sequence (twelve weeks)|Weeks 1 to 4::Modules 1 to 6. Shift 1 observes the opening sweep and the assignment. Shift 2 runs pre-dialysis risk sorting with a preceptor.|Weeks 5 to 8::Modules 7 to 12. Shift 3 leads mid-session rounds and the access and medication checks. Shift 4 runs the infection and water checks and one emergency drill as team leader.|Weeks 9 to 12::Modules 13 to 18. Shift 5 takes charge with a preceptor shadowing. Shift 6 takes charge with the preceptor at a distance and gives the end-of-shift handoff.|Final::Exam, observed stations including the integrated-shift capstone, the six shift attestations, and an improvement project presented to the head nurse.}}
<p>Record the nurse&rsquo;s license, renal dialysis training certificate, and life support certificates, which DOH and PSN expect of every dialysis nurse.[[doh2012]][[psn2024]] The answer keys for the instructor-scored written paper and the station score sheets stay with the education lead; they are not published here.</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments: 7 of 8 on two different sets for each module, with every missed question reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated satisfactorily to a facilitator.</li>
<li>Instructor-scored written paper 29 of 36 or higher; every observed station 8 of 10 or higher with every critical criterion met.</li>
<li>Six supervised shifts, at least 48 verified hours, each attested by the supervising nurse.</li>
<li>Improvement project 16 of 20 or higher, with no domain below 2.</li>
<li>Current license, renal dialysis training, and life support certificates on file.</li>
</ul>
<p>These are proposals for each unit to adapt. Completion is an educational record, not an appointment, a license, or an accreditation.</p>
""",
    "related": [("calc-dialysis-charge-nurse-toolkit.html", "Eight shift tools: station cover, assignment balance, breaks, lost minutes, heparin pump check, fall risk, risk sorter, and pressure drop."),
                ("code-blue-acls-dialysis-unit.html", "Cardiac arrest response in a dialysis unit."),
                ("calc-dialysis-head-nurse-toolkit.html", "Thirteen unit-level tools, from Kt/V to the disaster triage list.")],
}
P1, P2, P3, P4, P5 = ("Part 1 &middot; Taking the floor", "Part 2 &middot; Clinical oversight across many chairs",
                      "Part 3 &middot; Safety systems the charge nurse guards", "Part 4 &middot; People and communication",
                      "Part 5 &middot; Records, improvement, and integrity")
_ROWS = [
    ("01", "taking-charge", "Taking Charge: Authority, Boundaries, and the Shift You Inherit", P1,
     "Who decides what, reading a rule by who wrote it, the two staffing ratios side by side, and the authority to pause.",
     "A charge nurse at 5:40 a.m. receiving the shift keys and a clipboard from the night nurse at the entrance of a quiet dialysis unit, machines dark behind them."),
    ("02", "the-opening-sweep", "The Opening Sweep: Five Gates Before the First Connection", P1,
     "People, physician, water and machines, emergency readiness, and stations; why a blank result is a red result; holding with an owner and a time.",
     "A charge nurse walking a quiet dialysis floor at dawn, pausing at a machine with a red tag while a technician checks the water room."),
    ("03", "building-the-assignment", "Building the Assignment: Acuity, Competence, and Breaks", P1,
     "Weighting patients by need, matching tasks to competence, keeping your own load light, and planning breaks so ratios never quietly double.",
     "Hands placing colored magnets on a dialysis assignment board while two nurses and an orientee look on."),
    ("04", "the-live-board", "The Live Board: Rounding, Huddles, and Interruptions", P1,
     "Three levels of awareness, a board the whole team can read, rounds by the clock, three-minute huddles, and tasks protected from interruption.",
     "A charge nurse standing still at the center of a busy dialysis unit, scanning the room while nurses work around her."),
    ("05", "sorting-risk-before-connection", "Sorting Risk Before Connection", P2,
     "The long gap, Now, Today, and This month, the speed of fluid removal, trends over snapshots, falls and glucose, and closing a result loop.",
     "A nurse weighing an older man before dialysis while the charge nurse reviews a trend on a tablet beside them."),
    ("06", "order-machine-minutes", "The Order, the Machine, and the Minutes", P2,
     "What each line of the order does, the read-aloud three-way check, why delivered time decides the dose, and the patient who asks to stop early.",
     "Two nurses reading a dialysis order aloud against the machine screen before connecting a waiting patient."),
    ("07", "mid-session-surveillance", "Mid-Session Surveillance: Pressure, Cramps, Glucose, and the Patient Who Goes Quiet", P2,
     "Why pressure falls, the first response inside the protocol, cramps, low blood sugar during dialysis, the drowsy patient, and falls at disconnection.",
     "A charge nurse crouching beside a drowsy older woman during dialysis while another nurse brings a glucose meter."),
    ("08", "access-oversight", "Watching Every Access on the Floor", P2,
     "Why the alarm misses a dislodged needle, the first minute of bleeding, findings that mean do not needle today, and catheters on a busy floor.",
     "A fistula arm with taped needles and a looped line resting on top of a blanket so the access stays visible."),
    ("09", "medicines-heparin-blood", "Medicines, Heparin, and Blood on the Floor", P2,
     "Reconciliation at every return, high-alert medicines, the independent double-check, pump arithmetic, and transfusion during dialysis.",
     "Two nurses performing an independent double-check of a syringe at a medication cart."),
    ("10", "infection-prevention-real-time", "Infection Prevention in Real Time", P3,
     "How dialysis units spread bloodborne infection, the core interventions, clean and dirty workflows, honest observation, and a possible cluster.",
     "A charge nurse observing hand hygiene at a dialysis station from a short distance."),
    ("11", "water-and-machines-hold-release", "Water and Machines: Hold, Escalate, Release", P3,
     "The water treatment chain, reading the log, a symptom pattern in neighboring chairs, machine alarms, and restarting only on signatures.",
     "A charge nurse and a water technician checking a test strip beside carbon tanks in a dialysis water room."),
    ("12", "first-ten-minutes-emergency", "Leading the First Ten Minutes of an Emergency", P3,
     "Arrest on the dialysis floor, circuit cause or bystander, roles out loud with a watcher, closed-loop commands, and the handoff out.",
     "A charge nurse directing an emergency team at one dialysis chair while another nurse watches the rest of the floor."),
    ("13", "downtime-and-disruption", "Downtime, Typhoons, and Getting Through the Day", P3,
     "The first fifteen minutes of a power or water failure, paper when the system fails, prioritizing with the physician, and a signed restart.",
     "A charge nurse on the phone at the unit desk during a heavy rainstorm with a printed patient list and a flashlight."),
    ("14", "handoffs-that-close-the-loop", "Handoffs That Close the Loop", P4,
     "Why structured handoffs work, I-PASS on the dialysis floor, Situation-Background-Assessment-Recommendation (SBAR) calls with read-back, bedside handover, and closing the board.",
     "Two charge nurses exchanging a handoff at the assignment board while a patient adds a comment."),
    ("15", "delegation-coaching-speaking-up", "Delegation, Coaching, and Speaking Up", P4,
     "The five rights of delegation, feedback that works, coaching on the floor, speaking up in a Filipino workplace, and when coaching is not enough.",
     "A senior nurse coaching a younger nurse quietly beside a dialysis chair."),
    ("16", "patients-families-transitions", "Patients, Families, and Transitions Beyond the Chair", P4,
     "Teach-back, treatment burden, admissions and transfers, red flags in other modalities, and goals-of-care requests.",
     "A charge nurse holding a picture card while a patient explains it back to him, her son beside her."),
    ("17", "record-claim-and-learning", "The Record, the Claim, and Learning From What Went Wrong", P5,
     "A good record, where the record meets the PhilHealth claim, never fabricating, responding to an incident, and improving one thing.",
     "A charge nurse comparing a nursing record with a machine session log at her desk."),
    ("18", "integrated-shift-capstone", "Ethics, Resilience, and the Integrated Shift", P5,
     "Choice and safety, privacy on an open floor, conflict, moral distress and fatigue, and a capstone shift from the first gate to the last handoff.",
     "A charge nurse resting for a moment at an empty nurses' station at the end of a shift."),
]
from pathlib import Path as _Path
_HERE = _Path(__file__).resolve().parent
MODULES = []
for _id, _slug, _title, _part, _sub, _brief in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part,
                    "card_img": f"dialysis-charge-nurse-{_id}-card.webp", "hero_brief": _HB + _brief,
                    **({} if (_HERE / f"m{_id}.py").exists() else {"status": "planned"})})
