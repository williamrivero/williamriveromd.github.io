# -*- coding: utf-8 -*-
"""Water Treatment System Technician study series (branch of the Hemodialysis Technician series).
Modules are authored natively in m01.py ... m06.py."""

COURSE = {
    "title": "Water Treatment System Technician",
    "short": "Water Treatment Technician",
    "hub_slug": "water-treatment-technician",
    "label": "Study series for dialysis water treatment technicians",
    "tag": "Technician Education",
    "audience": "Dialysis water treatment technicians and trainees &middot; chief technicians, head nurses, and medical directors who supervise the water system",
    "audience_type": "Dialysis water treatment technicians",
    "level": "Allied health and technical staff, college reading level",
    "review_date": "2026-11-23",
    "draw": 5,
    "mastery": "4 of 5",
    "keywords": "dialysis water treatment technician, hemodialysis water system training, reverse osmosis dialysis, carbon tank chlorine test, dialysis water quality ISO 23500, endotoxin dialysis water, water room technician Philippines",
    "page_title": "Water Treatment System Technician: A Study Series for Dialysis Units",
    "desc": ("A free six-module study series for the technicians who run the dialysis water room: why dialysis water is different, pretreatment and carbon tanks, "
             "reverse osmosis and the distribution loop, daily monitoring, sampling and disinfection, and responding to failures. Plain language, many figures, "
             "a case, a skills checklist, and a self-assessment in every module."),
    "h1": "Water Treatment System <em>Technician</em>",
    "sub": "A six-module study series for the people who make dialysis water safe. Every patient in the unit is connected to the same water, so one good technician protects all of them at once.",
    "disclaimer": ("Educational study material for dialysis water treatment staff. Does not replace the medical director&rsquo;s direction, approved unit procedures, "
                   "manufacturer instructions, the standard edition your facility follows, DOH licensing requirements, or supervised training."),
    "scope_note": ("This module is study material for dialysis water treatment technicians. It explains the reasons behind safe practice; it does not replace your unit&rsquo;s "
                   "approved procedures, the manufacturer&rsquo;s instructions for your equipment, or the limits your facility has adopted. Limits quoted here come from the "
                   "international standard and are given so the numbers make sense; your facility&rsquo;s written limits and action levels are the ones you work to. Every case is fictional."),
    "branch_img": "water-treatment-technician-card.webp",
    "branch_role": "Specialist branch &middot; water room",
    "branch_blurb": "Pretreatment, carbon tanks, reverse osmosis, the distribution loop, daily testing, sampling, and disinfection.",
    "hero_file": "dialysis-water-treatment-systems-vignette-hero",
    "hero_alt": "A water treatment technician checking the pressure gauges on a reverse osmosis unit.",
    "start_h2": "The one system every patient shares",
    "start_html": """
<p>A dialysis patient&rsquo;s blood meets more than 300 liters of water every week, separated from it only by a thin membrane. If that water carries chlorine, metals, or bacterial fragments, every patient on the shift is exposed at the same moment. The water treatment technician is the person who prevents that.</p>
{{fig:wts_train}}
<p>This series has six modules. It explains what each tank and membrane removes, what each daily test proves, how to take a sample that means something, how the system is disinfected, and exactly what to do when a result is out of range. It assumes you have studied the <a href="hemodialysis-technician.html">Hemodialysis Technician</a> series, especially its module on water, concentrates, and dialysate.</p>
{{cards:What a water treatment technician does|Operates::Runs and watches the filters, softener, carbon tanks, reverse osmosis unit, and loop.|Tests::Checks chlorine, hardness, pressures, and water quality at set times, and records the real numbers.|Samples::Collects water for bacteria, endotoxin, and chemical testing using clean technique.|Disinfects::Carries out scheduled disinfection and proves the chemical is rinsed out.|Stops and reports::Holds treatments and alerts the nurse and medical director when a limit is crossed.}}
""",
    "is_not": ("It is study material. It is not a license or a certificate, and it does not make you competent on a system you have not been trained on. "
               "The medical director is responsible for the quality of dialysis water, and the facility works to the limits it has adopted from the applicable standard and regulation.[[iso23500_1]][[doh2012]] "
               "Every system is built differently: learn yours from its drawings, its manual, and a preceptor."),
    "pathway_note": """
<p>This branch suits technicians who like systems, measurements, and routine. It needs patience with logs and the confidence to stop a shift when a number is wrong.</p>
""",
    "modules_h2": "Six modules, in order",
    "modules_intro": "Study the modules in order. The first three explain the system; the last three explain how to watch it, test it, clean it, and respond when it fails.",
    "syllabus_note": "Each module takes about 45 to 60 minutes to read and work through. Supervised practice in the water room takes far longer and is set by your facility.",
    "assessment_html": """
<p>The questions at the end of each module are for practice. Each visit draws five from a bank of eight, and every question explains its best answer.</p>
<p>Competence in the water room is shown on the equipment: performing a chlorine test correctly, drawing a clean sample, reading a trend, and carrying out a disinfection with a documented rinse. Each module has a skills checklist for a preceptor to complete while watching you work.</p>
""",
    "sources_html": """
<p>Water quality limits and system requirements follow the international standard series ISO 23500 (2024), which covers water treatment equipment, dialysis water, concentrates, and dialysis fluid.[[iso23500_1]][[iso23500_2]][[iso23500_3]][[iso23500_5]] Philippine requirements come from the Department of Health (DOH) licensing order for dialysis facilities and its guidance on monitoring dialysis water, and from the Philippine Society of Nephrology (PSN) guidelines.[[doh2012]][[doh_water]][[psn2024]] Background on why each contaminant matters draws on published reviews and on the Centers for Disease Control and Prevention (CDC).[[ward2011]][[coulliette2013]][[cdc_water]]</p>
<p>Standards are revised from time to time, and facilities adopt specific editions. Where this series gives a number, check it against the edition and the written limits your facility uses.</p>
""",
    "trainer_h2": "Using the series to train water room staff",
    "trainer_html": """
<p>Use the six modules as guided study alongside hands-on training on your own system. A practical sequence is one module a week, each followed by supervised practice of its checklist in the water room.</p>
{{flow:Suggested sequence|Walk the system::Trace every pipe from feed water to drain with the drawing in hand.|Study the module::Read, work the case, and take the self-assessment.|Demonstrate::The preceptor performs the skill and explains each step.|Practice::The learner performs it under observation, several times.|Sign off::Record competence on the unit&rsquo;s own form.}}
<p>The medical director should approve the limits, action levels, and procedures the learner is taught.[[iso23500_1]]</p>
""",
    "completion_html": """
<ul>
<li>All six self-assessments attempted, with missed questions reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated satisfactorily on the unit&rsquo;s own system.</li>
<li>At least one full disinfection and one microbiological sampling round performed under observation.</li>
<li>One out-of-range scenario handled in simulation, including the hold, the report, and the record.</li>
</ul>
<p>These are proposals for the facility to adapt.</p>
""",
    "related": [("dialysis-water-treatment-systems.html", "The full clinical and engineering reference."),
                ("hemodiafiltration-deep-dive.html", "Why ultrapure fluid matters for newer therapies.")],
}

CARD_CROPS = [
    ("water-treatment-technician-card.webp", "wts-treatment-train-flow.png", 0.5),
    ("water-treatment-technician-01-card.webp", "wts-water-quality-tiers.png", 0.5),
    ("water-treatment-technician-02-card.webp", "wts-source-water-comparison.png", 0.5),
    ("water-treatment-technician-03-card.webp", "wts-dual-pass-ro-detail.png", 0.5),
    ("water-treatment-technician-04-card.webp", "wts-capacity-sizing-sequence.png", 0.5),
    ("water-treatment-technician-05-card.webp", "wts-facility-layout-isolation-hdf-dualpass.png", 0.5),
    ("water-treatment-technician-06-card.webp", "wts-golden-rule-decision-flow.png", 0.5),
]

MODULES = [
    {"id": "01", "slug": "why-dialysis-water-is-different", "title": "Why Dialysis Water Is Different",
     "sub": "Why water that is safe to drink can harm a dialysis patient, what the main contaminants do, and who is responsible for what.",
     "card_img": "water-treatment-technician-01-card.webp"},
    {"id": "02", "slug": "pretreatment-filters-softener-carbon", "title": "Pretreatment: Filters, Softener, and Carbon Tanks",
     "sub": "What each pretreatment stage removes, how a softener regenerates, and why carbon tanks are the most important chemical safeguard in the room.",
     "card_img": "water-treatment-technician-02-card.webp"},
    {"id": "03", "slug": "reverse-osmosis-distribution-loop", "title": "Reverse Osmosis and the Distribution Loop",
     "sub": "How a reverse osmosis membrane works, how to calculate rejection and recovery, and how the loop delivers water without letting bacteria settle.",
     "card_img": "water-treatment-technician-03-card.webp"},
    {"id": "04", "slug": "daily-monitoring-logs-trends", "title": "Daily Monitoring, Logs, and Trends",
     "sub": "The checks done every day, how to perform a total chlorine test properly, and how to read a log for slow changes before they become failures.",
     "card_img": "water-treatment-technician-04-card.webp"},
    {"id": "05", "slug": "microbiology-sampling-disinfection", "title": "Bacteria, Endotoxin, Sampling, and Disinfection",
     "sub": "What biofilm is, the limits for bacteria and endotoxin, how to collect a sample that can be trusted, and how the system is disinfected and rinsed.",
     "card_img": "water-treatment-technician-05-card.webp"},
    {"id": "06", "slug": "failures-emergencies-quality", "title": "Failures, Emergencies, and Quality Records",
     "sub": "What to do when chlorine breaks through, the reverse osmosis unit fails, or the supply is cut, and how records and reviews keep it from happening again.",
     "card_img": "water-treatment-technician-06-card.webp"},
]
