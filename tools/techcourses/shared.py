# -*- coding: utf-8 -*-
"""Shared data for the technical-workforce courses (HD technician, water treatment, biomedical).
Edited by hand; consumed by generate_tech_courses.py. American English only."""

RETRIEVED = "November 23, 2026"

# Added to the nursing course abbreviation table (token -> (expansion, plain note)).
ABBR = {
    "AAMI": ("Association for the Advancement of Medical Instrumentation", "A standards body whose dialysis water standards are widely used."),
    "AED": ("automated external defibrillator", "A portable device that can restart a normal heart rhythm with an electric shock."),
    "CAPA": ("corrective and preventive action", "A written plan that fixes a problem and stops it from coming back."),
    "CCHT": ("Certified Clinical Hemodialysis Technician", "A United States credential; it is not a Philippine license."),
    "CHT": ("Certified Hemodialysis Technologist/Technician", "A United States credential; it is not a Philippine license."),
    "CIP": ("clean-in-place", "Cleaning a system by circulating chemicals through it without taking it apart."),
    "CMS": ("Centers for Medicare & Medicaid Services", "The United States agency that sets conditions for dialysis facilities there."),
    "EBCT": ("empty-bed contact time", "How long water stays in contact with the carbon in a tank; longer contact removes more chlorine."),
    "EPO": ("erythropoietin", "A kidney hormone that tells the bone marrow to make red blood cells."),
    "ESD": ("electrostatic discharge", "A small static shock that can damage electronic parts."),
    "GFCI": ("ground-fault circuit interrupter", "A safety device that cuts power when current leaks to ground."),
    "HDF": ("hemodiafiltration", "A form of dialysis that adds large-volume convection to diffusion."),
    "HEPA": ("high-efficiency particulate air", "A type of fine air filter."),
    "IEC": ("International Electrotechnical Commission", "The body that publishes electrical safety standards for medical equipment."),
    "IFU": ("instructions for use", "The manufacturer&rsquo;s official directions for a device or product."),
    "LAL": ("Limulus amebocyte lysate", "The laboratory test used to measure endotoxin."),
    "LOTO": ("lockout/tagout", "Locking and labeling an energy source so equipment cannot start while someone works on it."),
    "MEI": ("Medical Education Institute", "Publisher of the Core Curriculum for the Dialysis Technician."),
    "NIDDK": ("National Institute of Diabetes and Digestive and Kidney Diseases", ""),
    "NTU": ("nephelometric turbidity unit", "A measure of how cloudy water is."),
    "PM": ("preventive maintenance", "Scheduled service done before something breaks."),
    "SDI": ("silt density index", "A test of how quickly fine particles plug a filter; it predicts membrane fouling."),
    "SDS": ("safety data sheet", "The document that lists a chemical&rsquo;s hazards and first aid."),
    "SOP": ("standard operating procedure", "The unit&rsquo;s approved written steps for a task."),
    "TCV": ("total cell volume", "The fluid volume of a dialyzer&rsquo;s fiber bundle; it falls as fibers clot."),
    "TDS": ("total dissolved solids", "The amount of dissolved minerals and salts in water."),
    "TMP": ("transmembrane pressure", "The pressure difference across the dialyzer membrane that pushes water out of the blood."),
    "UPS": ("uninterruptible power supply", "A battery unit that keeps equipment running briefly when power fails."),
    "UV": ("ultraviolet", "Light used to kill microbes in water."),
    "WHO": ("World Health Organization", ""),
}

# Keyed references for natively authored modules and hub pages (APA 7 style, HTML).
REFS = {
    "doh2012": ("Department of Health (DOH). (2012). <em>Administrative Order No. 2012-0001: New rules and regulations governing "
                "the licensure and regulation of dialysis facilities in the Philippines</em>. "
                '<a href="https://hfsrb.doh.gov.ph/wp-content/uploads/2021/05/AO-2012-0001.pdf">https://hfsrb.doh.gov.ph/wp-content/uploads/2021/05/AO-2012-0001.pdf</a>'),
    "psn2024": ("Philippine Society of Nephrology (PSN) Committee on Hemodialysis. (2024). <em>Guidelines for nephrologists in the "
                "operation of hemodialysis clinics in the Philippines</em>. "
                '<a href="https://psn.org.ph/wp-content/uploads/2024/03/HD-Guidelines-for-Nephrologists-Final-Revision-3.14.24.pdf">https://psn.org.ph/wp-content/uploads/2024/03/HD-Guidelines-for-Nephrologists-Final-Revision-3.14.24.pdf</a>'),
    "mei7": ("Medical Education Institute (MEI). (n.d.). <em>Core curriculum for the dialysis technician</em> (7th ed.). "
             '<a href="https://mei.org/core-curriculum/">https://mei.org/core-curriculum/</a>'),
    "cms494": ("Centers for Medicare &amp; Medicaid Services (CMS). (n.d.). <em>42 CFR &sect; 494.140: Condition, personnel qualifications</em>. "
               '<a href="https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-494/subpart-D/section-494.140">https://www.ecfr.gov/current/title-42/chapter-IV/subchapter-G/part-494/subpart-D/section-494.140</a>'),
    "cdc_dialysis": ("Centers for Disease Control and Prevention (CDC). (2024). <em>Dialysis safety: Clinical safety</em>. "
                     '<a href="https://www.cdc.gov/dialysis-safety/hcp/clinical-safety/">https://www.cdc.gov/dialysis-safety/hcp/clinical-safety/</a>'),
    "cdc_water": ("Centers for Disease Control and Prevention (CDC). (2024). <em>Water use in dialysis</em>. "
                  '<a href="https://www.cdc.gov/dialysis-safety/hcp/recommendations-resources/water-use-in-dialysis.html">https://www.cdc.gov/dialysis-safety/hcp/recommendations-resources/water-use-in-dialysis.html</a>'),
    "nncc_ccht": ("Nephrology Nursing Certification Commission (NNCC). (n.d.). <em>Certified Clinical Hemodialysis Technician (CCHT)</em>. "
                  '<a href="https://www.nncc-exam.org/certification/ccht">https://www.nncc-exam.org/certification/ccht</a>'),
    "bonent": ("Board of Nephrology Examiners Nursing and Technology (BONENT). (n.d.). <em>Certified Hemodialysis Technologist/Technician (CHT)</em>. "
               '<a href="https://bonent.org/certified-hemodialysis-technologist-technician-cht/">https://bonent.org/certified-hemodialysis-technologist-technician-cht/</a>'),
    "iso23500_1": ("International Organization for Standardization (ISO). (2024). <em>Preparation and quality management of fluids for "
                   "haemodialysis and related therapies. Part 1: General requirements</em> (ISO 23500-1:2024)."),
    "iso23500_2": ("International Organization for Standardization (ISO). (2024). <em>Preparation and quality management of fluids for "
                   "haemodialysis and related therapies. Part 2: Water treatment equipment for haemodialysis applications and related therapies</em> (ISO 23500-2:2024)."),
    "iso23500_3": ("International Organization for Standardization (ISO). (2024). <em>Preparation and quality management of fluids for "
                   "haemodialysis and related therapies. Part 3: Water for haemodialysis and related therapies</em> (ISO 23500-3:2024)."),
    "iso23500_5": ("International Organization for Standardization (ISO). (2024). <em>Preparation and quality management of fluids for "
                   "haemodialysis and related therapies. Part 5: Quality of dialysis fluid for haemodialysis and related therapies</em> (ISO 23500-5:2024)."),
    "iec60601": ("International Electrotechnical Commission (IEC). (2020). <em>Medical electrical equipment. Part 1: General requirements for "
                 "basic safety and essential performance</em> (IEC 60601-1, Edition 3.2)."),
    "iec60601_2_16": ("International Electrotechnical Commission (IEC). (2018). <em>Medical electrical equipment. Part 2-16: Particular requirements for "
                      "basic safety and essential performance of haemodialysis, haemodiafiltration and haemofiltration equipment</em> (IEC 60601-2-16:2018)."),
    "iec62353": ("International Electrotechnical Commission (IEC). (2014). <em>Medical electrical equipment: Recurrent test and test after repair "
                 "of medical electrical equipment</em> (IEC 62353:2014)."),
    "who_maint": ("World Health Organization (WHO). (2011). <em>Medical equipment maintenance programme overview</em> (WHO Medical Device Technical Series). "
                  '<a href="https://www.who.int/publications/i/item/9789241501538">https://www.who.int/publications/i/item/9789241501538</a>'),
    "aami_reuse": ("Association for the Advancement of Medical Instrumentation (AAMI). (2008). <em>Reprocessing of hemodialyzers</em> (ANSI/AAMI RD47:2008/(R)2013)."),
    "doh_water": ("Department of Health (DOH). (n.d.). <em>Guidelines on the monitoring of water used for dialysis</em>. "
                  '<a href="https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/69036">https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/69036</a>'),
    "ward2011": ("Ward, R. A. (2011). Avoiding toxicity from water-borne contaminants in hemodialysis: New challenges in an era of increased demand for water. "
                 "<em>Advances in Chronic Kidney Disease, 18</em>(3), 207&ndash;213. "
                 '<a href="https://doi.org/10.1053/j.ackd.2011.01.007">https://doi.org/10.1053/j.ackd.2011.01.007</a>'),
    "coulliette2013": ("Coulliette, A. D., &amp; Arduino, M. J. (2013). Hemodialysis and water quality. <em>Seminars in Dialysis, 26</em>(4), 427&ndash;438. "
                       '<a href="https://doi.org/10.1111/sdi.12113">https://doi.org/10.1111/sdi.12113</a>'),
}

READING_TITLES = {
    "dialysis-water-treatment-systems.html": "Hemodialysis Water Treatment Systems",
    "dialyzer-reprocessing-reuse.html": "Dialyzer Reprocessing and Reuse",
    "code-blue-acls-dialysis-unit.html": "Cardiac Arrest Response in a Dialysis Unit",
    "dialysis-qapi-vs-cqi.html": "Dialysis Center Quality Management",
    "dialysis-machine-assignment.html": "Dialysis Machine Assignment and Hepatitis Isolation",
    "kidney-functions.html": "What the Kidneys Do",
    "hemodialysis-modalities.html": "Hemodialysis Modalities",
    "dialysis-adequacy.html": "Dialysis Adequacy",
    "dialysis-access-care.html": "Dialysis Access Care",
    "dialysis-access-infection.html": "Dialysis Access Infection",
    "hemodialysis-access-lifeline.html": "Hemodialysis Access: A Lifeline for a Lifetime",
    "hemodialysis-complications.html": "Hemodialysis Complications",
    "fluid-management-dialysis.html": "Fluid Management Between Dialysis Sessions",
    "typhoon-disaster-preparedness-dialysis.html": "Typhoon and Disaster Preparedness in Dialysis",
    "peritoneal-dialysis-ckd.html": "Peritoneal Dialysis",
    "kidney-transplant.html": "Kidney Transplant",
    "home-hemodialysis-philippines.html": "Home Hemodialysis in the Philippines",
    "dialysis-prescription.html": "The Dialysis Prescription",
    "dry-weight-determination.html": "Finding True Dry Weight",
    "high-flux-hd-optimization.html": "High-Flux Hemodialysis Optimization",
    "hemodiafiltration-new-standard.html": "Is Hemodiafiltration the New Standard?",
    "el-nino-heat-dialysis.html": "El Ni&ntilde;o, Heat, and Dialysis",
}

CALCS = {
    "calc-dialysis-adequacy-ktv.html": ("Dialysis Adequacy (Kt/V and URR)", "Calculates the urea reduction ratio and Kt/V from pre- and post-dialysis results."),
    "calc-ufr-ceiling.html": ("Ultrafiltration Rate Check", "Converts a fluid goal and treatment time to mL per hour and mL per kg per hour."),
    "calc-idwg-fluid.html": ("Weight Gain Between Sessions", "Works out interdialytic weight gain as kilograms and as a percentage of target weight."),
    "calc-ro-recovery-dualpass.html": ("Reverse Osmosis Recovery and Rejection", "Calculates percent recovery and percent rejection for single- and dual-pass systems."),
    "calc-dialysis-water-reuse.html": ("Dialysis Water Use", "Estimates the water a unit uses and how much reject water could be recovered."),
    "calc-dialysis-qapi-scorecard.html": ("Dialysis Quality Scorecard", "Tracks a small set of unit quality indicators month to month."),
    "calc-dialysis-continuity-planner.html": ("Dialysis Continuity Planner", "Plans treatment capacity during a power, water, or staffing disruption."),
}

HOW_HTML = """
{{flow:How to work through a module|Objectives::Read what you should be able to do by the end.|Big picture::A plain-words summary and the key terms, before any detail.|Opening case::A fictional shift problem. Decide what you would do first.|Lesson::Short parts with pictures, tables, and worked examples.|Case review::Compare your answer with one sound response.|Skills checklist::Practice with a preceptor on real or training equipment.|Self-assessment::Five questions drawn from a larger bank, with explanations.}}
<p>New terms are explained the first time they appear, and every page ends with a glossary. Abbreviations are spelled out at first use. If a sentence still reads like jargon, check the glossary, then ask your preceptor to show you the real object on the unit: most of this work makes sense faster when you can see and touch the equipment.</p>
"""


# ── Renal Care Academy landing page (academy/index.html) ─────────────────────
ACADEMY = {
    "desc": ("Renal Care Academy is the staff-training section of Renal Care Matters: free, structured study series for nephrology and dialysis nurses, "
             "hemodialysis technicians, water treatment technicians, biomedical technicians, physicians on duty, and renal dietitians, each with cases, skills checklists, and self-assessments."),
    "keywords": "renal care academy, physician on duty course, dialysis staff training Philippines, nephrology nursing course, hemodialysis technician course, dialysis water treatment training, dialysis biomedical technician training, renal dietitian course",
    "sub": "Structured study series for the nurses, technicians, and other professionals who run kidney care. Separate from the guide library, and built for learning a role step by step.",
    "audience": "Dialysis and nephrology staff in training &middot; head nurses, chief technicians, educators, and medical directors",
    # href, card image, role line, title, blurb, meta line
    "nursing": ("nephrology-nursing.html", "nephrology-nursing-01-kidney-function-renal-assessment-vignette-hero.webp", "Registered nurses",
                "Nephrology Nursing &amp; Hemodialysis",
                "Kidney assessment, chronic kidney disease, acute kidney injury, hemodialysis, peritoneal dialysis, transplantation, quality improvement, and an advanced module on continuous therapy and hemodiafiltration.",
                "16 core modules + 1 advanced &middot; two learner paths &middot; educator page"),
    "planned": [],
    "about_html": """
<p>The guides on this site answer questions. The Academy teaches roles. Each track is a complete, ordered course of study for one job in kidney care, written so that a new staff member can work through it module by module alongside supervised practice on the unit.</p>
{{cards:How the Academy differs from the guide library|Built around a role::Each track follows what one kind of staff member needs to know and do, in the order they need it.|Ordered and complete::Modules are numbered and build on each other, with a syllabus and a course home.|Practice, not just reading::Every module has a fictional case, a skills checklist for a preceptor, and a self-assessment.|Made for trainers too::Each track has a page for educators and preceptors with printable checklists.}}
<p>Everything is free, needs no account, and sends nothing you answer to any server.</p>
""",
    "how_html": """
{{flow:Inside every module|Objectives::What you should be able to do by the end.|Lesson::Reasoning first, then the task, with figures and tables.|Case::A fictional situation from an ordinary shift.|Supervised practice::A checklist completed by a preceptor on real equipment.|Self-assessment::Questions drawn at random from a bank, with explanations.}}
<p>Modules link to the site&rsquo;s guides and calculators as further reading, so the Academy and the guide library support each other without being mixed together.</p>
""",
    "is_not": ("The Academy is self-study material. It is not a license, a certificate of training, or proof of competence, and it carries no Continuing Professional "
               "Development (CPD) units. Dialysis facilities in the Philippines are licensed by the Department of Health (DOH), and what each staff member may do is set "
               "by that license, the facility, and the supervising nurse and nephrologist.[[doh2012]][[psn2024]] Competence is shown in supervised practice and signed off by a preceptor or training provider."),
}
