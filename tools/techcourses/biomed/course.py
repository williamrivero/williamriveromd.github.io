# -*- coding: utf-8 -*-
"""Dialysis Biomedical Technician study series (branch of the Hemodialysis Technician series).
Modules are authored natively in m01.py ... m06.py."""

COURSE = {
    "title": "Hemodialysis Center Biomedical Technician",
    "short": "Dialysis Biomedical Technician",
    "hub_slug": "dialysis-biomedical-technician",
    "label": "Study series for dialysis biomedical technicians",
    "tag": "Technician Education",
    "audience": "Biomedical equipment technicians working in or for hemodialysis centers &middot; chief technicians, head nurses, and medical directors",
    "audience_type": "Biomedical equipment technicians",
    "level": "Technical staff, college reading level",
    "review_date": "2026-11-23",
    "draw": 5,
    "mastery": "4 of 5",
    "keywords": "dialysis biomedical technician, hemodialysis machine maintenance, dialysis machine preventive maintenance, dialysis machine calibration, electrical safety testing IEC 62353, dialysis equipment technician training Philippines",
    "page_title": "Hemodialysis Center Biomedical Technician: A Study Series",
    "desc": ("A free twelve-module study series for biomedical technicians who maintain hemodialysis machines: the role and safe working, electrical fundamentals, the dialysate side, "
             "fluid balance, the blood side, protective systems, preventive maintenance, calibration, disinfection, electrical safety and utilities, and troubleshooting "
             "and return to service. Plain language, many figures, a case, a skills checklist, and a self-assessment in every module."),
    "h1": "Hemodialysis Center <em>Biomedical Technician</em>",
    "sub": "A twelve-module study series for the people who keep dialysis machines accurate and safe. A machine that is slightly wrong is wrong for every patient who uses it.",
    "disclaimer": ("Educational study material for biomedical technicians. Does not replace the manufacturer&rsquo;s service manual and training, approved facility procedures, "
                   "applicable electrical and medical device regulations, or supervised practice."),
    "scope_note": ("This module is study material for biomedical technicians in dialysis. It explains how machines work and why maintenance steps exist; it is not a service manual. "
                   "Repairs, calibrations, and safety tests are done only by people trained and authorized for that machine model, using the manufacturer&rsquo;s service manual, "
                   "approved parts, and calibrated test equipment. Every case is fictional."),
    "branch_img": "dialysis-biomedical-technician-card.webp",
    "branch_role": "Specialist branch &middot; workshop",
    "branch_blurb": "How dialysis machines work inside, preventive maintenance, calibration, safety testing, troubleshooting, and return to service.",
    "hero_alt": "A biomedical technician at a workbench with a service manual, test meters, and an open hemodialysis machine.",
    "start_h2": "The people who keep the machines honest",
    "start_html": """
<p>A hemodialysis (HD) machine mixes a fluid to a precise recipe, warms it to body temperature, pumps blood outside the body, removes an exact volume of water, and watches for air, blood leaks, and wrong pressures, for four hours at a time, several times a day. Each of those functions depends on sensors and pumps that drift, wear, and scale. The biomedical technician finds the drift before it reaches a patient.</p>
{{fig:blood_circuit|A dialysis machine in use. Everything the patient depends on here, from the blood pump to the air trap sensor, is maintained and tested by the biomedical technician.}}
<p>This series has twelve modules, written to the level of a technician who maintains the center&rsquo;s machines independently. It explains the electrical basics, how the machine works on the fluid side and the blood side, how each protective system is tested, how preventive maintenance and calibration are planned and recorded, how machines are disinfected and tested for electrical safety, and how to troubleshoot a fault and return a machine to service properly. It assumes you have studied the <a href="hemodialysis-technician.html">Hemodialysis Technician</a> series, especially the modules on principles, machines, and water.</p>
{{cards:What a dialysis biomedical technician does|Maintains::Carries out scheduled preventive maintenance by the manufacturer&rsquo;s plan.|Calibrates::Checks and adjusts sensors against reference instruments.|Tests safety::Verifies alarms, protective systems, and electrical safety.|Repairs::Finds and fixes faults with approved parts.|Documents and releases::Keeps the service history and formally returns equipment to use.}}
""",
    "is_not": ("It is study material. It is not manufacturer training, a license, or authorization to service any machine. Dialysis machines are medical devices built to "
               "international safety standards, and manufacturers train and certify technicians for specific models.[[iec60601_2_16]] Facilities are licensed by the Department of "
               "Health (DOH), which expects equipment to be maintained and records to be kept.[[doh2012]] Learn each model from its service manual, the manufacturer&rsquo;s course, and a preceptor."),
    "pathway_note": """
<p>This branch suits technicians with a background or strong interest in electronics, mechanics, or engineering who like fault-finding and precise measurement.</p>
""",
    "modules_h2": "Twelve modules, in order",
    "modules_intro": "Study the modules in order. Modules 1 to 7 explain the machine; Modules 8 to 12 explain how to keep it accurate, clean, safe, and documented.",
    "syllabus_note": "Each module takes about 60 to 90 minutes to read and work through. Workshop practice under supervision, and the manufacturer&rsquo;s own training, take far longer.",
    "assessment_html": """
<p>The questions at the end of each module are for practice. Each visit draws five from a larger bank, and every question explains its best answer.</p>
<p>Competence is shown at the bench: completing a preventive maintenance visit by the manual, calibrating against a reference meter, proving that each alarm works, and writing a service record another technician can follow. Each module has a skills checklist for a preceptor or senior technician to complete while watching you work.</p>
""",
    "sources_html": """
<p>Machine safety requirements follow the international standards for medical electrical equipment and for hemodialysis equipment in particular, and periodic electrical safety testing follows the standard for recurrent tests.[[iec60601]][[iec60601_2_16]][[iec62353]] Maintenance program structure follows the World Health Organization (WHO) guidance on medical equipment maintenance.[[who_maint]] Fluid quality requirements that machines must help meet come from ISO 23500.[[iso23500_1]][[iso23500_5]] Philippine expectations come from the DOH licensing order for dialysis facilities and the Philippine Society of Nephrology (PSN) guidelines.[[doh2012]][[psn2024]]</p>
<p>For any specific machine, the manufacturer&rsquo;s service manual and instructions for use are the controlling documents. Where this series describes a typical design, yours may differ.</p>
""",
    "trainer_h2": "Using the series to train biomedical staff",
    "trainer_html": """
<p>Use the twelve modules as guided study alongside the manufacturer&rsquo;s training for each machine model and supervised bench work. A practical sequence is one module a week, each followed by its checklist on a machine that is out of clinical service.</p>
{{flow:Suggested sequence|Open the manual::Find the flow diagram and the maintenance schedule for the model.|Study the module::Read, work the case, and take the self-assessment.|Demonstrate::A senior technician performs the task and explains each step.|Practice::The learner performs it under observation on an out-of-service machine.|Sign off::Record competence per model on the facility&rsquo;s form.}}
""",
    "completion_html": """
<ul>
<li>All twelve self-assessments attempted, with missed questions reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated satisfactorily.</li>
<li>Manufacturer training completed for each machine model the technician will service.</li>
<li>One complete preventive maintenance visit and one fault repair documented and reviewed by a senior technician.</li>
<li>The four capstone stations in Module 12, with all critical steps satisfactory.</li>
</ul>
<p>These are proposals for the facility to adapt.</p>
""",
    "related": [("dialysis-qapi-vs-cqi.html", "Where equipment performance fits in the quality program."),
                ("dialysis-machine-assignment.html", "Why machine identity and location matter clinically.")],
}

# Card thumbnails cut from the circular hero of each page (prep_assets.hero_card).
CARD_CROPS = [
    ("dialysis-biomedical-technician-card.webp", "dialysis-biomedical-technician-vignette-hero.png", 0.5),
    ("dialysis-biomedical-technician-01-card.webp", "dialysis-biomedical-technician-01-role-and-safe-working-vignette-hero.png", 0.5),
    ("dialysis-biomedical-technician-02-card.webp", "dialysis-biomedical-technician-02-electrical-electronic-fundamentals-vignette-hero.png", 0.5),
    ("dialysis-biomedical-technician-03-card.webp", "dialysis-biomedical-technician-03-dialysate-water-heating-degassing-vignette-hero.png", 0.5),
    ("dialysis-biomedical-technician-04-card.webp", "dialysis-biomedical-technician-04-proportioning-conductivity-bypass-vignette-hero.png", 0.5),
    ("dialysis-biomedical-technician-05-card.webp", "dialysis-biomedical-technician-05-fluid-balance-ultrafiltration-vignette-hero.png", 0.5),
    ("dialysis-biomedical-technician-06-card.webp", "dialysis-biomedical-technician-06-blood-pump-pressures-heparin-pump-vignette-hero.png", 0.5),
    ("dialysis-biomedical-technician-07-card.webp", "dialysis-biomedical-technician-07-protective-systems-alarm-testing-vignette-hero.png", 0.5),
    ("dialysis-biomedical-technician-08-card.webp", "dialysis-biomedical-technician-08-preventive-maintenance-program-vignette-hero.png", 0.5),
    ("dialysis-biomedical-technician-09-card.webp", "dialysis-biomedical-technician-09-calibration-test-equipment-vignette-hero.png", 0.5),
    ("dialysis-biomedical-technician-10-card.webp", "dialysis-biomedical-technician-10-disinfection-descaling-fluid-hygiene-vignette-hero.png", 0.5),
    ("dialysis-biomedical-technician-11-card.webp", "dialysis-biomedical-technician-11-electrical-safety-facility-utilities-vignette-hero.png", 0.5),
    ("dialysis-biomedical-technician-12-card.webp", "dialysis-biomedical-technician-12-troubleshooting-life-cycle-capstone-vignette-hero.png", 0.5),
]

MODULES = [
    {"id": "01", "slug": "role-and-safe-working", "title": "The Biomedical Technician’s Role and Safe Working",
     "sub": "What the role covers, working safely with contaminated equipment, electricity, and chemicals, decontamination before service, and using the service manual.",
     "card_img": "dialysis-biomedical-technician-01-card.webp"},
    {"id": "02", "slug": "electrical-electronic-fundamentals", "title": "Electrical and Electronic Fundamentals",
     "sub": "Voltage, current, and resistance in plain terms; power, fuses, and earth; the sensors and actuators in a machine; and safe use of a multimeter.",
     "card_img": "dialysis-biomedical-technician-02-card.webp"},
    {"id": "03", "slug": "dialysate-water-heating-degassing", "title": "Dialysate Side I: Water Inlet, Heating, and Degassing",
     "sub": "How the machine regulates, warms, and degasses incoming water, how temperature is verified, and how to troubleshoot these stages.",
     "card_img": "dialysis-biomedical-technician-03-card.webp"},
    {"id": "04", "slug": "proportioning-conductivity-bypass", "title": "Dialysate Side II: Proportioning, Conductivity, and Bypass",
     "sub": "How dialysate is mixed and checked, how conductivity is measured and verified, what bypass does, and how to troubleshoot conductivity alarms.",
     "card_img": "dialysis-biomedical-technician-04-card.webp"},
    {"id": "05", "slug": "fluid-balance-ultrafiltration", "title": "Fluid Balance and Ultrafiltration Control",
     "sub": "How balancing systems and the ultrafiltration pump measure fluid removal, what transmembrane pressure tells you, and how accuracy is tested.",
     "card_img": "dialysis-biomedical-technician-05-card.webp"},
    {"id": "06", "slug": "blood-pump-pressures-heparin-pump", "title": "The Blood Side: Pump, Pressures, and Heparin Pump",
     "sub": "The roller pump and why displayed flow can be untrue, the pressure sensors, the heparin syringe pump, and their checks.",
     "card_img": "dialysis-biomedical-technician-06-card.webp"},
    {"id": "07", "slug": "protective-systems-alarm-testing", "title": "Protective Systems and Alarm Testing",
     "sub": "Single-fault safety, the air detector and clamp, the blood leak detector, how each is tested, and why none is ever bypassed.",
     "card_img": "dialysis-biomedical-technician-07-card.webp"},
    {"id": "08", "slug": "preventive-maintenance-program", "title": "The Preventive Maintenance Program",
     "sub": "The inventory, the maintenance calendar, a visit step by step, safety notices and software, and spare parts.",
     "card_img": "dialysis-biomedical-technician-08-card.webp"},
    {"id": "09", "slug": "calibration-test-equipment", "title": "Calibration and Test Equipment",
     "sub": "Calibration and tolerance, as-found and as-left values, reference instruments and their care, and the instrument register.",
     "card_img": "dialysis-biomedical-technician-09-card.webp"},
    {"id": "10", "slug": "disinfection-descaling-fluid-hygiene", "title": "Disinfection, Descaling, and Machine Fluid Hygiene",
     "sub": "Scale, film, and biofilm; the right program for each; residual testing; hoses and the drain air gap; and dialysis fluid filters.",
     "card_img": "dialysis-biomedical-technician-10-card.webp"},
    {"id": "11", "slug": "electrical-safety-facility-utilities", "title": "Electrical Safety Testing and Facility Utilities",
     "sub": "Why patients are vulnerable, inspection and testing, the utilities at each station, and what happens when power fails.",
     "card_img": "dialysis-biomedical-technician-11-card.webp"},
    {"id": "12", "slug": "troubleshooting-life-cycle-capstone", "title": "Troubleshooting, Life Cycle, and Capstone",
     "sub": "A method for any fault with a worked example, verification after repair, the machine file from acceptance to retirement, and four practical stations.",
     "card_img": "dialysis-biomedical-technician-12-card.webp"},
]
