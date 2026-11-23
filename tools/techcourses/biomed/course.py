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
    "desc": ("A free six-module study series for biomedical technicians who maintain hemodialysis machines: the role and safe working, the dialysate side, "
             "the blood side and protective systems, preventive maintenance and calibration, disinfection and electrical safety testing, and troubleshooting and "
             "return to service. Plain language, many figures, a case, a skills checklist, and a self-assessment in every module."),
    "h1": "Hemodialysis Center <em>Biomedical Technician</em>",
    "sub": "A six-module study series for the people who keep dialysis machines accurate and safe. A machine that is slightly wrong is wrong for every patient who uses it.",
    "disclaimer": ("Educational study material for biomedical technicians. Does not replace the manufacturer&rsquo;s service manual and training, approved facility procedures, "
                   "applicable electrical and medical device regulations, or supervised practice."),
    "scope_note": ("This module is study material for biomedical technicians in dialysis. It explains how machines work and why maintenance steps exist; it is not a service manual. "
                   "Repairs, calibrations, and safety tests are done only by people trained and authorized for that machine model, using the manufacturer&rsquo;s service manual, "
                   "approved parts, and calibrated test equipment. Every case is fictional."),
    "branch_img": "dialysis-biomedical-technician-card.webp",
    "branch_role": "Specialist branch &middot; workshop",
    "branch_blurb": "How dialysis machines work inside, preventive maintenance, calibration, safety testing, troubleshooting, and return to service.",
    "hero_alt": "A biomedical technician servicing a hemodialysis machine in a workshop.",
    "start_h2": "The people who keep the machines honest",
    "start_html": """
<p>A hemodialysis (HD) machine mixes a fluid to a precise recipe, warms it to body temperature, pumps blood outside the body, removes an exact volume of water, and watches for air, blood leaks, and wrong pressures, for four hours at a time, several times a day. Each of those functions depends on sensors and pumps that drift, wear, and scale. The biomedical technician finds the drift before it reaches a patient.</p>
{{fig:blood_circuit|A dialysis machine in use. Everything the patient depends on here, from the blood pump to the air trap sensor, is maintained and tested by the biomedical technician.}}
<p>This series has six modules. It explains how the machine works on the fluid side and the blood side, how preventive maintenance and calibration are planned and recorded, how machines are disinfected and tested for electrical safety, and how to troubleshoot a fault and return a machine to service properly. It assumes you have studied the <a href="hemodialysis-technician.html">Hemodialysis Technician</a> series, especially the modules on principles, machines, and water.</p>
{{cards:What a dialysis biomedical technician does|Maintains::Carries out scheduled preventive maintenance by the manufacturer&rsquo;s plan.|Calibrates::Checks and adjusts sensors against reference instruments.|Tests safety::Verifies alarms, protective systems, and electrical safety.|Repairs::Finds and fixes faults with approved parts.|Documents and releases::Keeps the service history and formally returns equipment to use.}}
""",
    "is_not": ("It is study material. It is not manufacturer training, a license, or authorization to service any machine. Dialysis machines are medical devices built to "
               "international safety standards, and manufacturers train and certify technicians for specific models.[[iec60601_2_16]] Facilities are licensed by the Department of "
               "Health (DOH), which expects equipment to be maintained and records to be kept.[[doh2012]] Learn each model from its service manual, the manufacturer&rsquo;s course, and a preceptor."),
    "pathway_note": """
<p>This branch suits technicians with a background or strong interest in electronics, mechanics, or engineering who like fault-finding and precise measurement.</p>
""",
    "modules_h2": "Six modules, in order",
    "modules_intro": "Study the modules in order. The first three explain the machine; the last three explain how to keep it accurate, clean, safe, and documented.",
    "syllabus_note": "Each module takes about 45 to 60 minutes to read and work through. Workshop practice under supervision, and the manufacturer&rsquo;s own training, take far longer.",
    "assessment_html": """
<p>The questions at the end of each module are for practice. Each visit draws five from a bank of eight, and every question explains its best answer.</p>
<p>Competence is shown at the bench: completing a preventive maintenance visit by the manual, calibrating against a reference meter, proving that each alarm works, and writing a service record another technician can follow. Each module has a skills checklist for a preceptor or senior technician to complete while watching you work.</p>
""",
    "sources_html": """
<p>Machine safety requirements follow the international standards for medical electrical equipment and for hemodialysis equipment in particular, and periodic electrical safety testing follows the standard for recurrent tests.[[iec60601]][[iec60601_2_16]][[iec62353]] Maintenance program structure follows the World Health Organization (WHO) guidance on medical equipment maintenance.[[who_maint]] Fluid quality requirements that machines must help meet come from ISO 23500.[[iso23500_1]][[iso23500_5]] Philippine expectations come from the DOH licensing order for dialysis facilities and the Philippine Society of Nephrology (PSN) guidelines.[[doh2012]][[psn2024]]</p>
<p>For any specific machine, the manufacturer&rsquo;s service manual and instructions for use are the controlling documents. Where this series describes a typical design, yours may differ.</p>
""",
    "trainer_h2": "Using the series to train biomedical staff",
    "trainer_html": """
<p>Use the six modules as guided study alongside the manufacturer&rsquo;s training for each machine model and supervised bench work. A practical sequence is one module a week, each followed by its checklist on a machine that is out of clinical service.</p>
{{flow:Suggested sequence|Open the manual::Find the flow diagram and the maintenance schedule for the model.|Study the module::Read, work the case, and take the self-assessment.|Demonstrate::A senior technician performs the task and explains each step.|Practice::The learner performs it under observation on an out-of-service machine.|Sign off::Record competence per model on the facility&rsquo;s form.}}
""",
    "completion_html": """
<ul>
<li>All six self-assessments attempted, with missed questions reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated satisfactorily.</li>
<li>Manufacturer training completed for each machine model the technician will service.</li>
<li>One complete preventive maintenance visit and one fault repair documented and reviewed by a senior technician.</li>
</ul>
<p>These are proposals for the facility to adapt.</p>
""",
    "related": [("dialysis-qapi-vs-cqi.html", "Where equipment performance fits in the quality program."),
                ("dialysis-machine-assignment.html", "Why machine identity and location matter clinically.")],
}

CARD_CROPS = [
    ("dialysis-biomedical-technician-card.webp", "access-hd-blood-circuit.png", 0.4),
    ("dialysis-biomedical-technician-01-card.webp", "dialysis-machine-categories.png", 0.5),
    ("dialysis-biomedical-technician-02-card.webp", "hd-diffusion-convection.png", 0.5),
    ("dialysis-biomedical-technician-03-card.webp", "access-hd-blood-circuit.png", 0.4),
    ("dialysis-biomedical-technician-04-card.webp", "dialysis-hd-prescription-parameters.png", 0.5),
    ("dialysis-biomedical-technician-05-card.webp", "dialyzer-germicide-history-matrix.png", 0.5),
    ("dialysis-biomedical-technician-06-card.webp", "dialysis-qapi-vs-cqi-kpi-dashboard-mock.png", 0.5),
]

_HB = "Circular vignette, realistic clinical editorial illustration, Philippine dialysis center. "
MODULES = [
    {"id": "01", "slug": "role-and-safe-working", "title": "The Biomedical Technician&rsquo;s Role and Safe Working",
     "sub": "What the role covers, how to work safely with blood-contaminated equipment, electricity, water, and chemicals, and how a machine is taken out of and returned to use.",
     "card_img": "dialysis-biomedical-technician-01-card.webp",
     "hero_brief": _HB + "A biomedical technician in gloves and eye protection placing an 'out of service' tag on a hemodialysis machine in a workshop."},
    {"id": "02", "slug": "dialysate-side-hydraulics", "title": "Inside the Machine: The Dialysate Side",
     "sub": "How the machine heats, degasses, mixes, checks, and balances dialysate, and how it measures the water it removes from the patient.",
     "card_img": "dialysis-biomedical-technician-02-card.webp",
     "hero_brief": _HB + "Close view of the opened rear hydraulic compartment of a generic hemodialysis machine, with a technician tracing tubing against a flow diagram."},
    {"id": "03", "slug": "blood-side-protective-systems", "title": "The Blood Side and Protective Systems",
     "sub": "The blood pump, pressure monitoring, the air detector and clamp, and the blood leak detector: how each works and how each is proven to work.",
     "card_img": "dialysis-biomedical-technician-03-card.webp",
     "hero_brief": _HB + "A technician testing the air detector and venous clamp on the front panel of a generic hemodialysis machine using a training tubing set, no patient present."},
    {"id": "04", "slug": "preventive-maintenance-calibration", "title": "Preventive Maintenance and Calibration",
     "sub": "How a maintenance program is planned, what calibration means, why reference instruments must themselves be checked, and what a good service record contains.",
     "card_img": "dialysis-biomedical-technician-04-card.webp",
     "hero_brief": _HB + "A technician comparing a handheld reference conductivity and temperature meter with a dialysis machine display, with a maintenance checklist on a clipboard."},
    {"id": "05", "slug": "disinfection-descaling-electrical-safety", "title": "Disinfection, Descaling, and Electrical Safety Testing",
     "sub": "Why machines scale and grow bacteria inside, how they are cleaned, and how periodic electrical safety tests protect patients and staff.",
     "card_img": "dialysis-biomedical-technician-05-card.webp",
     "hero_brief": _HB + "A technician connecting an electrical safety analyzer to a hemodialysis machine power cord on a workshop bench."},
    {"id": "06", "slug": "troubleshooting-records-return-to-service", "title": "Troubleshooting, Records, and Return to Service",
     "sub": "A method for finding faults, the records every machine should have, how to release a machine after repair, and how equipment data feed quality review.",
     "card_img": "dialysis-biomedical-technician-06-card.webp",
     "hero_brief": _HB + "A technician and a charge nurse signing a return-to-service form beside a hemodialysis machine."},
]
for _m in MODULES:
    _m["title"] = _m["title"].replace("&rsquo;", "’")
