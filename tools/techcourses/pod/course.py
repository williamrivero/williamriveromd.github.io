# -*- coding: utf-8 -*-
"""Physician on Duty in the Dialysis Unit: a study series for non-nephrologist physicians who cover hemodialysis shifts.
Blueprint: ~/Documents/Physicians-on-Duty/POD_HUB_MODULE_BLUEPRINT.md (v0.6). All content is written independently
from primary sources; no course material from any other training provider is used. Modules are authored natively in
m01.py, m02.py, ...; a module with "status": "planned" shows as "In preparation" on the course home page."""

_HB = "Illustrated clinical vignette, warm natural light, Filipino staff and patients, modern hemodialysis unit, no text in image. "

COURSE = {
    "title": "Physician on Duty in the Dialysis Unit",
    "short": "Physician on Duty",
    "hub_slug": "physician-on-duty",
    "label": "Study series for physicians on duty",
    "tag": "Physician Education",
    "icon": "🩺",
    "no_branch": True,
    "audience": "Physicians who cover hemodialysis shifts &middot; attending nephrologists, medical directors, and head nurses who orient them",
    "audience_type": "Physicians on duty in hemodialysis units",
    "level": "Licensed physicians, written in plain language",
    "review_date": "2026-11-23",
    "draw": 8,
    "mastery": "7 of 8",
    "keywords": ("physician on duty hemodialysis, dialysis duty physician training Philippines, hemodialysis complications management, "
                 "intradialytic hypotension, dialysis emergencies, ESKD physiology for physicians, hemodialysis unit orientation"),
    "page_title": "Physician on Duty in the Dialysis Unit: A Study Series",
    "desc": ("A free study series for physicians who cover hemodialysis shifts: how a patient without kidney function differs, how the treatment works, "
             "how to assess a patient before and after a session, and how to handle emergencies in the chair. Plain language, many figures, a case, "
             "a skills checklist, and a self-assessment in every module."),
    "h1": "Physician on Duty in the <em>Dialysis Unit</em>",
    "sub": ("A study series for physicians who cover hemodialysis shifts. Learn why a patient without kidney function is a different patient, "
            "and what to do when a session goes wrong."),
    "disclaimer": ("Educational study material for physicians. Does not replace the attending nephrologist&rsquo;s orders, the unit&rsquo;s protocols, "
                   "required certification courses, or supervised practice."),
    "scope_note": ("This module is study material for physicians on duty in hemodialysis units. It explains the reasoning behind common decisions; it is not a protocol. "
                   "At the chairside, follow your unit&rsquo;s protocol and ask the attending nephrologist for guidance. Doses and cut-off values are set by your unit. "
                   "Every case is fictional."),
    "branch_img": "physician-on-duty-card.webp",
    "branch_role": "Physicians",
    "branch_blurb": ("For physicians covering a hemodialysis shift: how patients without kidney function differ, how the treatment works, "
                     "assessment before and after a session, and emergencies in the chair."),
    "academy_meta": "32 modules planned &middot; first-shift modules open &middot; three tiers",
    "hero_alt": "A physician on duty talking with a nurse beside a patient on hemodialysis.",
    "start_h2": "The doctor in the room",
    "start_html": """
<p>For four hours at a time, a hemodialysis (HD) machine takes over part of the work of two failed kidneys. Most sessions are uneventful. Some are not: blood pressure falls, a patient has chest pain, a fever starts, or an alarm will not clear. The physician on duty is the doctor in the room when that happens.</p>
<p>Most physicians on duty are not nephrologists. Medical school teaches the healthy kidney and the failing kidney, but very little about the patient who has no kidney function at all and lives by a machine three times a week. That patient breaks many rules of general medicine. A liter of intravenous fluid that would help another patient can put this one in pulmonary edema. A &ldquo;normal&rdquo; laboratory result may be alarming, and an alarming one may be this patient&rsquo;s normal.</p>
{{cards:What this series will help you do|Understand the patient::Explain how a body without kidney function handles water, salt, potassium, acid, and medicines.|Understand the treatment::Know what the machine, the dialyzer, and the dialysis fluid are doing.|Assess::Decide whether it is safe to start a session and safe to send the patient home.|Respond::Act in the first minutes of an emergency in the chair.|Escalate::Call the attending nephrologist early, with the right facts.|Care over time::Recognize the long-term problems of patients on dialysis.}}
<p>The series is written in plain language. Every new term is explained when it first appears, and every module has figures, a case, a skills checklist, and a self-assessment.</p>
""",
    "is_not": ("It is study material written independently from published guidelines, textbooks, and research. It is not a certificate, and it does not replace the "
               "requirements for physicians on duty in the Philippines. The Philippine Society of Nephrology (PSN) standards for hemodialysis clinics expect a physician on duty "
               "to hold a current advanced cardiac life support (ACLS) certificate and a certificate from a PSN-conducted or PSN-accredited course for physicians on duty, "
               "and to work under the supervision of the attending nephrologist and the clinical head of the unit.[[psn2024]] This series is not that course and is not "
               "affiliated with or endorsed by PSN. Use it to prepare, to review, and to support orientation in your own unit."),
    "pathways_tag": "Three tiers",
    "pathways_h2": "Start with what you need for your first shift",
    "pathways_nav": "Tiers",
    "pathways_html": """
<p>The series has 32 modules in seven parts. You do not need all of them before your first duty. Each module is marked with one of three tiers.</p>
{{cards:The three tiers|First-Shift Essentials::Nine modules to finish before your first supervised shift: your role, the basic physiology, the machine, the access, the assessment, and the emergencies you are most likely to meet.|Core::Twenty modules to finish before you take duty on your own: the rest of the physiology and treatment, the remaining emergencies, and the long-term care of dialysis patients.|Advanced::Three modules for the months after: special patients, other treatment paths, and care outside the unit.}}
<p>Modules open as they are completed and reviewed. A module marked &ldquo;In preparation&rdquo; is planned but not yet published.</p>
""",
    "modules_h2": "Thirty-two modules in seven parts",
    "modules_intro": ("Study the modules in order within your tier. The parts follow a physician&rsquo;s own path: the patient, the treatment, one session, "
                      "emergencies, long-term care, and the unit."),
    "syllabus_note": "Each module takes about 45 to 75 minutes to read and work through. Skills checklists are completed on the unit with a preceptor.",
    "assessment_html": """
<p>The questions at the end of each module are for practice. Each visit draws eight from a bank of fifteen, and every question explains its best answer. The questions were written for this series.</p>
<p>Competence is shown on the unit, not on a screen: examining an access, assessing a patient before a session, responding to a fall in blood pressure, and calling the attending nephrologist with a clear report. Each module has a skills checklist for a preceptor, usually the attending nephrologist or a senior physician on duty, to complete while watching you work.</p>
""",
    "sources_html": """
<p>The series is built from published sources. Physiology follows standard textbooks.[[hall2021]][[daugirdas2015]] Clinical recommendations follow the guidelines of Kidney Disease: Improving Global Outcomes (KDIGO) and its conference reports, and the research they rest on.[[kdigo_bpvol2020]] Philippine expectations for physicians on duty come from the Department of Health (DOH) licensing order for dialysis facilities and the PSN standards for hemodialysis clinics.[[doh2012]][[psn2024]] Each module lists its own sources.</p>
<p>Where the evidence is strong, the text says so. Where a practice rests on observation, expert opinion, or local custom, the text says that instead. Doses and cut-off values are left to your unit&rsquo;s protocol and the attending nephrologist.</p>
""",
    "trainers_intro": ("An attending nephrologist, medical director, or senior physician on duty can use these modules as the guided-study part of unit orientation. "),
    "trainer_h2": "Using the series to orient a new physician on duty",
    "trainer_html": """
<p>The series supports unit orientation; it does not replace it. A practical plan is self-study of the First-Shift Essentials before the first day, a unit tour with the head nurse, two shifts observing an experienced physician on duty, and three shifts with backup on call, with the checklists signed along the way.</p>
{{flow:Suggested orientation sequence|Self-study::First-Shift Essentials, each self-assessment at 7 of 8.|Day 1::Unit tour, emergency cart, machine walk-through, unit protocols, contact list.|Shifts 1 and 2::Observe an experienced physician on duty. Complete the access and assessment checklists.|Shifts 3 to 5::Take duty with backup on call. Complete the emergency response checklists.|Within one month::Mock cardiac arrest and emergency take-off drill.|Within two months::Core modules complete; cleared for independent duty by the medical director.}}
<p>Record the physician&rsquo;s ACLS certificate and physician-on-duty course certificate, which the PSN standards expect.[[psn2024]]</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments: 7 of 8 on two different sets for each module, with every missed question reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated satisfactorily to a preceptor.</li>
<li>A mock cardiac arrest led as team leader, and one emergency take-off drill.</li>
<li>Current ACLS certificate and the physician-on-duty course certificate on file.</li>
<li>Clearance for independent duty by the medical director.</li>
</ul>
<p>These are proposals for each unit to adapt.</p>
""",
    "related": [("hemodialysis-complications.html", "The main complications of a session, written for patients and clinicians."),
                ("code-blue-acls-dialysis-unit.html", "Cardiac arrest response in a dialysis unit."),
                ("dry-weight-determination.html", "How dry weight is judged.")],
}

P1, P2, P3, P4 = "Part 1 &middot; Starting out", "Part 2 &middot; The patient is different", "Part 3 &middot; The treatment", "Part 4 &middot; The session"
P5, P6, P7 = "Part 5 &middot; Emergencies in the chair", "Part 6 &middot; The long game", "Part 7 &middot; The unit and the system"
E_, C_, A_ = "Essentials", "Core", "Advanced"

_ROWS = [
    ("01", "your-role-on-the-dialysis-floor", "Your Role on the Dialysis Floor", P1, E_,
     "What a physician on duty is responsible for, who does what on the team, the shape of a shift, when to call the attending nephrologist, and how to report and record.",
     "A physician on duty talking with a nurse at the nurses&rsquo; station of a hemodialysis unit, patients on machines in the background."),
    ("02", "water-salt-potassium-acid", "Life Without Kidney Function I: Water, Salt, Potassium, and Acid", P2, E_,
     "What healthy kidneys do each day, what builds up between sessions, why a fluid bolus behaves differently, and why potassium and acid rise.",
     "A physician examining the ankles of a dialysis patient for swelling before a session, weighing scale nearby."),
    ("03", "uremia-residual-function-starting-dialysis", "Life Without Kidney Function II: Uremia, Residual Function, and Starting Dialysis", P2, C_,
     "The uremic syndrome, the toxins dialysis removes well and poorly, why leftover kidney function matters, and when dialysis begins.",
     ""),
    ("04", "heart-blood-bone-defenses", "Life Without Kidney Function III: Heart, Blood, Bone, and Defenses", P2, C_,
     "How kidney failure changes the heart and vessels, blood, bone, and immunity, and why common tests and medicines behave differently.",
     ""),
    ("05", "inside-the-machine", "Inside the Machine: How Blood Is Cleaned", P3, E_,
     "The blood circuit, the dialyzer, diffusion and ultrafiltration, the machine&rsquo;s monitors, and what the common alarms mean.",
     ""),
    ("06", "water-and-dialysate", "Water and Dialysate: The Hidden Half of the Treatment", P3, C_,
     "What is in dialysis fluid, how water is treated, which contaminants harm patients, and how to recognize a problem that affects several patients at once.",
     ""),
    ("07", "dialysis-order-and-dose", "Reading the Dialysis Order and Judging the Dose", P3, C_,
     "What each line of the dialysis order means, who may change it, how the dose of dialysis is measured, and what newer therapies add.",
     ""),
    ("08", "dry-weight", "Dry Weight: Finding the Right Amount of Fluid", P3, C_,
     "What dry weight is, how to judge volume at the bedside, how to calculate the fluid goal and rate, and why fast removal drops blood pressure.",
     ""),
    ("09", "fistulas-and-grafts", "The Lifeline I: Fistulas and Grafts", P3, E_,
     "How to examine a fistula or graft, recognize narrowing, clotting, infection, and aneurysm, and control bleeding.",
     ""),
    ("10", "catheters", "The Lifeline II: Catheters", P3, E_,
     "Catheter types, exit-site and tunnel checks, poor flow, infection, and catheter emergencies.",
     ""),
    ("11", "safe-to-start-safe-to-go-home", "Safe to Start, Safe to Go Home", P4, E_,
     "A focused assessment before the session, the decision to start, delay, or transfer, and the check before the patient leaves.",
     ""),
    ("12", "first-sessions-and-unusual-sessions", "First Sessions and Unusual Sessions", P4, C_,
     "The first dialysis, disequilibrium, the patient with acute kidney injury, the visiting patient, and isolated ultrafiltration.",
     ""),
    ("13", "when-the-pressure-falls", "When the Pressure Falls", P5, E_,
     "Why blood pressure falls during dialysis, the stepwise response, and how to tell a simple drop from a dangerous cause.",
     ""),
    ("14", "high-blood-pressure-breathless-patient", "High Blood Pressure and the Breathless Patient", P5, C_,
     "Rising pressure during dialysis, hypertensive emergency, the causes of breathlessness, and how blood pressure is managed between sessions.",
     ""),
    ("15", "heart-emergencies-in-the-chair", "Heart Emergencies in the Chair: Chest Pain, Arrhythmia, and Cardiac Arrest", P5, E_,
     "Sorting chest pain by cause, reading the electrocardiogram in a dialysis patient, and leading resuscitation beside a dialysis machine.",
     ""),
    ("16", "when-the-circuit-fails", "When the Circuit Fails: Air, Hemolysis, Reactions, and Blood Loss", P5, E_,
     "Air embolism, hemolysis, dialyzer reactions, needle dislodgement, and clotting, and when the blood must not be returned.",
     ""),
    ("17", "fever-and-bloodstream-infection", "The Shivering Patient: Fever and Bloodstream Infection", P5, C_,
     "Telling catheter infection from a pyrogenic reaction, drawing cultures, and recognizing sepsis in a dialysis patient.",
     ""),
    ("18", "potassium-sugar-and-the-brain", "The Confused or Seizing Patient: Potassium, Sugar, and the Brain", P5, C_,
     "High and low potassium, low blood sugar, seizures, altered consciousness, and stroke in the dialysis chair.",
     ""),
    ("19", "bleeding-and-heparin", "Bleeding and Heparin", P5, C_,
     "Why heparin is used, when to reduce or omit it, and how to manage bleeding from the access and elsewhere.",
     ""),
    ("20", "prescribing-without-kidneys", "Prescribing Without Kidneys", P6, C_,
     "The medicines dialysis patients take, rules for prescribing, timing doses around a session, and the common prescriptions that cause harm.",
     ""),
    ("21", "blood-and-bone", "Blood and Bone: Anemia and Mineral Disorders", P6, C_,
     "Why hemoglobin is low, how iron and stimulating agents are used, and what calcium, phosphate, and parathyroid hormone results mean.",
     ""),
    ("22", "diabetes-on-dialysis", "Diabetes on Dialysis", P6, C_,
     "Why insulin needs fall, how to prevent low blood sugar in the chair, which medicines are safe, and how to check the feet.",
     ""),
    ("23", "food-fluid-and-muscle", "Food, Fluid, and Muscle", P6, C_,
     "Protein needs on dialysis, signs of wasting, and practical advice on fluid, salt, potassium, and phosphate with Filipino foods.",
     ""),
    ("24", "symptoms-in-the-chair-and-at-home", "Symptoms in the Chair and at Home: Cramps, Itch, Sleep, Pain, and Fatigue", P6, C_,
     "Cramps, nausea, and headache during a session; itch, poor sleep, pain, and fatigue at home; and when a minor symptom signals a serious cause.",
     ""),
    ("25", "special-patients", "Special Patients: Frailty, Complex Illness, and Pregnancy", P6, A_,
     "Dialysis in heart failure, liver disease, cancer, and frailty, and what changes when a dialysis patient is pregnant.",
     ""),
    ("26", "the-person-in-the-chair", "The Person in the Chair: Mood, Burden, and Choices About Care", P6, C_,
     "Depression, missed sessions, caregiver strain, and how to respond when a patient wants to stop dialysis.",
     ""),
    ("27", "transplant-pd-conservative-care", "Other Roads: Transplant, Peritoneal Dialysis, and Conservative Care", P6, A_,
     "The other long-term paths, who suits each, and how to keep a patient ready for transplant.",
     ""),
    ("28", "outside-the-unit", "Outside the Unit: Surgery, Contrast, Hospital Stays, and Travel", P6, A_,
     "Timing dialysis around procedures, advice on contrast, protecting the access in hospital, and preparing for travel.",
     ""),
    ("29", "a-clean-unit", "A Clean Unit: Hepatitis, HIV, Tuberculosis, and Vaccines", P7, C_,
     "How infection spreads in a dialysis unit, isolation rules, screening, vaccines, and what to do after a needlestick.",
     ""),
    ("30", "when-the-power-or-water-fails", "When the Power or Water Fails", P7, C_,
     "The first ten minutes of a power, water, or building emergency, and how patients stay dialyzed when the unit cannot open.",
     ""),
    ("31", "rules-records-and-quality", "Rules, Records, and Quality", P7, C_,
     "The rules that govern dialysis units, what a physician signs, consent, data privacy, sound records, and how a unit measures its quality.",
     ""),
    ("32", "putting-it-together", "Putting It Together: Bedside Skills and a Simulated Shift", P7, C_,
     "Orders, handoffs, practice stations, and a simulated shift that brings the series together.",
     ""),
]
import re as _re


def re_m(f):
    return bool(_re.fullmatch(r"m\d\d\.py", f))


LIVE = {"01", "02"} | {f[1:3] for f in __import__("os").listdir(__import__("os").path.dirname(__file__) or ".") if re_m(f)}
MODULES = []
for _id, _slug, _title, _part, _tier, _sub, _brief in _ROWS:
    _d = {"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part, "tier": _tier,
          "card_img": f"physician-on-duty-{_id}-card.webp"}
    if _brief:
        _d["hero_brief"] = _HB + _brief
    if _id not in LIVE:
        _d["status"] = "planned"
    MODULES.append(_d)
