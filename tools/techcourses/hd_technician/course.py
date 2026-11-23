# -*- coding: utf-8 -*-
"""Hemodialysis Technician study series.

Lesson text, cases, checklists and question banks come from the Markdown sources in src/NN/
(Study Guide.md, Self-Assessment.md, Answer Key.md), copied from ~/Documents/HD Technicians.
Everything in `enrich` below is added on top: the plain-words opener, extra figures, key points,
glossary terms and site reading. Edit the Markdown to change the lesson; edit here to change the extras."""

COURSE = {
    "title": "Hemodialysis Technician",
    "short": "Hemodialysis Technician",
    "hub_slug": "hemodialysis-technician",
    "label": "Study series for hemodialysis technicians",
    "tag": "Technician Education",
    "audience": "Entry-level hemodialysis technicians and trainees &middot; preceptors, head nurses, and training providers",
    "audience_type": "Hemodialysis technicians",
    "level": "Entry-level allied health, college reading level",
    "review_date": "2026-11-23",
    "draw": 5,
    "mastery": "4 of 5",
    "keywords": "hemodialysis technician training Philippines, dialysis technician course, dialysis technician study guide, hemodialysis machine setup, dialysis water treatment basics, dialyzer reprocessing, dialysis technician competency checklist",
    "page_title": "Hemodialysis Technician: A 12-Module Study Series",
    "desc": ("A free 12-module study series for hemodialysis technicians in the Philippines: the dialysis unit and the technician's role, "
             "kidney failure, how hemodialysis works, infection prevention, machines and the blood circuit, water and dialysate, vascular access, "
             "the treatment session, emergencies, and dialyzer reprocessing. Plain language, many figures, a case, a skills checklist, and a self-assessment in every module."),
    "h1": "Hemodialysis <em>Technician</em>",
    "sub": "A twelve-module study series for people who prepare, check, and look after the equipment that keeps dialysis patients alive. Written in plain language, with a picture for every idea that needs one.",
    "disclaimer": ("Educational study material for hemodialysis technicians. Does not replace physician orders, the supervising nurse&rsquo;s direction, "
                   "approved unit procedures, manufacturer instructions, DOH licensing requirements, or supervised training."),
    "scope_note": ("This module is study material for hemodialysis technicians. It explains the reasons behind safe practice; it does not replace "
                   "the physician&rsquo;s orders, the supervising nurse&rsquo;s direction, your unit&rsquo;s approved procedures, or the manufacturer&rsquo;s "
                   "instructions for use. What a technician may do differs between countries and between facilities: do only the tasks you are trained, "
                   "assigned, and signed off to do. Every case is fictional."),
    "branch_img": "hemodialysis-technician-01-dialysis-unit-technician-role-card.webp",
    "branch_role": "Foundation &middot; chairside",
    "branch_blurb": "Stations, machines, the blood circuit, the treatment session, and safe teamwork with the dialysis nurse.",
    "hero_alt": "A trainee technician and a nurse talk with a patient beside a dialysis machine.",
    "start_h2": "A study series for the people behind the machines",
    "start_html": """
<p>A hemodialysis (HD) technician prepares the station, sets up and checks the machine, helps watch the treatment, cleans and resets the station, and keeps the records that prove each step was done. The work is technical, but its purpose is simple: every patient gets the right treatment, on safe equipment, with clean water, every time.</p>
<p>This series has twelve modules. It starts with the dialysis unit and your place in the team, moves through kidney failure and the science of dialysis, then covers infection prevention, machines, water, vascular access, the treatment session, emergencies, and dialyzer reprocessing. The last module pulls everything together into a practical assessment.</p>
{{cards:What makes this series easier to study|Plain language::Written for a college-level reader. Every technical term is explained the first time it appears and again in the glossary.|Pictures first::Each module uses illustrations, flow strips, and tables so you can see the idea before you read the detail.|Real shift problems::Every module opens with a fictional case from an ordinary shift and returns to it at the end.|Know your limits::Each module says clearly what a technician reports and what the nurse or physician decides.}}
<p>The series is free, needs no account, and sends nothing you answer to any server.</p>
""",
    "is_not": ("It is study material. It is not a license, a certificate of training, or proof of competence, and it carries no Continuing Professional "
               "Development (CPD) units. In the Philippines, dialysis facilities are licensed by the Department of Health (DOH), and what a technician is "
               "allowed to do is set by the facility under that license and by the supervising nurse and nephrologist.[[doh2012]][[psn2024]] "
               "Skills are learned and signed off on real equipment with a preceptor."),
    "pathway_note": """
<p>Start with this series whichever role you are aiming for. Water treatment and biomedical technicians need the same foundation: they must understand what the patient at the end of the pipe or the machine is going through.</p>
""",
    "modules_h2": "Twelve modules, in order",
    "modules_intro": "Study the modules in order; each one builds on the last. If you tick the box on a module&rsquo;s self-assessment, your result appears on its card here, stored only in this browser.",
    "syllabus_note": ("The hours are a proposed course design for a provider-led program of about three months: 72 classroom hours, 60 skills-lab hours, and 168 "
                      "hours of supervised placement, 300 hours in all. They are a planning proposal, not a regulatory requirement."),
    "assessment_html": """
<p>The questions at the end of each module are for practice. Each visit draws five from a bank of fifteen, and every question explains its best answer. Retry as often as you like.</p>
<p>Skills are different. Setting up a circuit, testing water for chlorine, or responding to an alarm cannot be learned or judged from a screen. Each module therefore has a skills checklist that a preceptor completes while watching you work on the unit&rsquo;s own equipment. Steps marked <span class="tc-crit">Critical</span> are the ones where a mistake can reach a patient; all of them must be done correctly before sign-off.</p>
{{cards:Three levels of learning a skill|Observed::You watched a qualified person do it. This is exposure, not permission.|Supervised practice::You did it while a preceptor watched and could step in.|Signed off::A preceptor recorded that you did it correctly and safely. Only now is it part of your assigned work.}}
""",
    "sources_html": """
<p>The scope follows Philippine expectations for dialysis facilities and internationally used technician curricula. Philippine sources set what applies locally: the DOH licensing order for dialysis facilities and the Philippine Society of Nephrology (PSN) guidelines for hemodialysis clinics.[[doh2012]][[psn2024]] International sources were used to check that nothing important was left out: the Medical Education Institute (MEI) Core Curriculum for the Dialysis Technician, the United States certification outlines for the Certified Clinical Hemodialysis Technician (CCHT) and Certified Hemodialysis Technologist/Technician (CHT), the United States federal personnel standard for dialysis technicians, and the infection-prevention guidance of the Centers for Disease Control and Prevention (CDC).[[mei7]][[nncc_ccht]][[bonent]][[cms494]][[cdc_dialysis]] Each module lists its own sources.</p>
<p>International credentials and rules are used here to map topics only. They do not apply to Philippine practice, and tasks such as needle insertion, catheter care, and giving medicines are assigned differently in different countries.</p>
""",
    "trainer_h2": "A proposed 300-hour program",
    "trainer_html": """
<p>The series is designed to be the guided-study part of a provider-led program for entry-level, in-center hemodialysis technicians. The proposed design runs for three calendar months: 72 classroom hours, 60 skills-lab hours, and 168 hours of supervised placement. Start with role and safety foundations, move through technology and treatment support, and finish with integrated assessment. The module-by-module hours are in the syllabus on the <a href="hemodialysis-technician.html#syllabus">course home page</a>.</p>
{{flow:Suggested teaching sequence for each module|Present the case::Ask learners for a first response before teaching anything.|Teach the lesson::Follow the objectives in order, using one worked example.|Revisit the case::Have learners justify their response.|Skills lab::Simulate the checklist on training equipment.|Placement::Log one related activity, the supervision level, and preceptor feedback.}}
<p>Track observation, simulation, and supervised performance separately. Patient-facing duties and sign-off follow the facility&rsquo;s authorization and Philippine regulation, not this series.[[doh2012]][[psn2024]]</p>
""",
    "completion_html": """
<ul>
<li>Module self-assessments: a suggested target of 12 of 15 across each module&rsquo;s full bank, with review of any missed safety-critical item.</li>
<li>A separate written examination set by the provider: a proposed 100 items with an 80% target. The blueprint is in Module 12.</li>
<li>Five observed practical stations (Module 12): station turnover, equipment readiness, water quality, patient and access handoff, and emergency response.</li>
<li>A placement logbook reviewed by the preceptor.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated satisfactorily.</li>
</ul>
<p>These are proposals for the provider to adapt. A self-assessment score records study only.</p>
""",
    "related": [("dialysis-water-treatment-systems.html", "Reference for Module 7."),
                ("dialyzer-reprocessing-reuse.html", "Reference for Module 11."),
                ("code-blue-acls-dialysis-unit.html", "Reference for Module 10.")],
}

_E = {}

_E["01"] = {
    "navs": ["The shift", "Your role", "Handoff and records"],
    "big": """
{{plain:A dialysis unit runs like an airport. Many people do different jobs, every step is checked, and nothing moves forward until the check is complete. Your job as a technician is to prepare and check, to notice, and to report. You are never expected to decide alone.}}
{{cards:Key terms for this module|Station::One treatment place: a chair or bed, a dialysis machine, and the tubing set for one patient.|Two identifiers::Two facts that belong to one person only, such as full name and date of birth. A chair number is not one.|Escalate::Tell the right person now, clearly, because the problem is beyond your role.|SBAR::A four-part way to report: Situation, Background, Assessment, Recommendation.|Check-back::Repeating an instruction aloud so the other person can confirm you heard it correctly.|Near miss::An error that was caught before it reached the patient.}}
{{flow:The three habits this module teaches|Verify::Match the patient, the record, and the equipment before you act.|Pause::If anything does not match, stop the work that depends on it.|Report::Tell the nurse what you saw, what you did, and what you need.}}
""",
    "pre": {1: "{{fig:blood_circuit|One dialysis station: the patient, the chair, the machine, and the tubing circuit that carries blood through the dialyzer and back. Each station is prepared and checked for one patient at a time.}}",
            2: "{{cards:Who decides what|Technician::Prepares and checks equipment, performs assigned tasks, observes, records, and reports.|Dialysis nurse::Assesses the patient, directs care, and delegates and supervises tasks.|Nephrologist::Writes and changes the dialysis prescription.|Biomedical and water staff::Find and fix faults in machines and the water system, and clear them for use.}}",
            3: "{{flow:SBAR, step by step|Situation::What is happening right now, in one sentence.|Background::The facts that explain it.|Assessment::What you think the problem is, or simply what does not match.|Recommendation::What you need from the listener, and by when.}}"},
    "post": {1: "{{key:A clean station, a working machine, and a correctly identified patient are three separate checks. Passing one does not pass the others.}}",
             2: "{{stop:If either identifier does not match, stop patient-specific setup and tell the supervising nurse. Do not let &ldquo;she always sits there&rdquo; replace the check.}}"},
    "terms": [("Extracorporeal circuit", "The tubing and dialyzer that carry blood outside the body during treatment."),
              ("Delegated task", "A task a nurse assigns to you and remains responsible for supervising."),
              ("Objective note", "A record of what was seen, heard, measured, and done, with times, and without guesses or opinions."),
              ("Audit trail", "The record that shows who changed an entry, when, and why.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How near-miss reports feed the unit&rsquo;s quality program."),
                 ("dialysis-machine-assignment.html", "Why some machines and stations are reserved for certain patients.")],
}

_E["02"] = {
    "navs": ["Blood to urine", "When kidneys fail", "AKI, CKD, failure", "Reading trends"],
    "big": """
{{plain:Healthy kidneys are filters that never switch off. They clean the blood, remove extra water, keep body salts in balance, and send signals that keep blood and bones healthy. When they fail, wastes and water stay in the body. Dialysis does part of the cleaning and water removal, a few hours at a time.}}
{{fig:kidneys}}
{{cards:Key terms for this module|Nephron::The tiny working unit of the kidney. Each kidney has about a million.|Glomerulus::The filter at the start of each nephron.|Tubule::The tube after the filter that takes back what the body needs.|Electrolytes::Body salts such as sodium and potassium that carry an electric charge.|Edema::Swelling from extra fluid in the tissues.|Anemia::Too few red blood cells, which causes tiredness and breathlessness.}}
""",
    "pre": {1: "{{fig:nephron}}",
            2: "{{fig:ckd_cascade|When nephrons are lost, several kidney jobs fail together. Use the table below as the text version of the four main jobs.}}",
            4: "{{fig:fluid_overview}}{{formula:<strong>Weight change between sessions</strong> = today&rsquo;s weight before treatment &minus; the last weight after treatment.<br>Example: 69.4 kg &minus; 67.2 kg = 2.2 kg. One liter of water weighs about one kilogram, so this suggests about 2.2 liters of fluid.}}"},
    "post": {3: "{{cards:Three terms on a timeline|Acute kidney injury::Kidney function falls over hours to days. It may recover.|Chronic kidney disease::A kidney problem that has lasted three months or longer.|Kidney failure::Function is so low that dialysis, a transplant, or conservative care is needed.}}",
             4: "{{stop:New shortness of breath, chest pain, or confusion is never &ldquo;just fluid.&rdquo; Call the nurse first; finish your notes afterward.}}"},
    "terms": [("Urea and creatinine", "Waste products in the blood. Laboratories measure them to judge how well the kidneys or dialysis are cleaning the blood."),
              ("Potassium", "A body salt that controls heart rhythm. A high level can stop the heart without warning signs."),
              ("Bicarbonate", "The body&rsquo;s main buffer against acid. Dialysis fluid supplies it."),
              ("Baseline", "What is usual for this patient. A change from baseline matters more than a single number."),
              ("Estimated GFR", "A calculation from a blood test that estimates how much blood the kidneys filter each minute.")],
    "readings": [("kidney-functions.html", "A fuller, illustrated tour of everything the kidneys do."),
                 ("fluid-management-dialysis.html", "What patients are taught about fluid between sessions.")],
    "calcs": ["calc-idwg-fluid.html"],
}

_E["03"] = {
    "navs": ["Five pathways", "Home dialysis", "Daily life", "Teach-back"],
    "big": """
{{plain:Kidney failure can be treated in more than one way, and no single way suits everyone. Patients often ask the technician first, because you are the person they see most. Your part is to listen, explain the basics with approved materials, and pass the question to the nurse or physician who can answer it for that patient.}}
{{fig:modalities}}
{{cards:Key terms for this module|In-center hemodialysis::Dialysis done at a clinic by staff, usually three times a week.|Home hemodialysis::The same kind of treatment done at home after training.|Peritoneal dialysis::Dialysis that uses the lining of the abdomen as the filter.|Transplant::A donated kidney placed by surgery.|Conservative kidney management::Active care for symptoms and comfort without dialysis or transplant.|Teach-back::Asking the patient to explain the plan in their own words, to check your explanation worked.}}
""",
    "pre": {2: "{{fig:pd_exchange}}",
            4: "{{flow:Teach-back in four steps|Explain::One or two points, in plain words.|Ask::&ldquo;To be sure I explained it well, what will you do if&hellip;?&rdquo;|Listen::Is anything missing or mixed up?|Explain again::Use different words, then ask again.}}"},
    "post": {1: "{{fig:tx_overview}}",
             3: "{{key:A missed session is a safety problem, not a scheduling detail. Tell the nurse the same day.}}"},
    "terms": [("Care partner", "A family member or friend trained to help with home dialysis."),
              ("Cycler", "The machine that performs peritoneal dialysis exchanges automatically, usually overnight."),
              ("Exchange", "One round of draining used peritoneal dialysis fluid and filling with fresh fluid."),
              ("Eligibility", "Whether a treatment is medically and practically suitable for one person. The clinical team decides it.")],
    "readings": [("hemodialysis-modalities.html", "The forms of dialysis compared in more detail."),
                 ("peritoneal-dialysis-ckd.html", "How peritoneal dialysis works day to day."),
                 ("kidney-transplant.html", "Who can receive a transplant and what follows."),
                 ("home-hemodialysis-philippines.html", "Home hemodialysis from a Philippine point of view.")],
}

_E["04"] = {
    "navs": ["The dialyzer", "Dialysate", "Fluid numbers", "Adequacy"],
    "big": """
{{plain:A dialyzer is a bundle of very thin hollow straws. Blood flows inside the straws, and a cleaning fluid called dialysate flows around them. Wastes pass through the straw walls into the fluid, and extra water is pushed out by pressure. That is the whole idea; the rest of this module is detail.}}
{{fig:dialyzer_anatomy}}
{{cards:Two everyday pictures|Tea bag = diffusion::Color spreads from the tea bag into the water because it is more concentrated inside. Nothing pushes it. Wastes such as urea leave the blood the same way.|Coffee press = ultrafiltration::Pushing the plunger forces water through a mesh. Pressure does the work. Extra water leaves the blood the same way.|River carrying sand = convection::Moving water drags dissolved substances along with it.}}
{{cards:Key terms for this module|Semipermeable membrane::A wall with pores that let water and small particles through but hold back blood cells and large proteins.|Dialysate::The prepared fluid that flows around the fibers and receives the wastes.|Countercurrent flow::Blood and dialysate flowing in opposite directions, which keeps cleaning efficient along the whole fiber.|Target weight::The weight the clinical team aims for at the end of treatment. Also called dry weight.|Ultrafiltration goal::The amount of fluid ordered to be removed in this session.}}
""",
    "pre": {1: "{{fig:diff_conv}}",
            3: "{{fig:two_compartment}}",
            4: "{{fig:hd_week}}"},
    "post": {2: "{{key:A normal conductivity reading shows the mix has the right overall strength. It does not show that the right concentrate was connected. Read the label as well as the display.}}",
             3: "{{stop:Never enter a fluid-removal number because it &ldquo;looks right.&rdquo; If the ordered goal is not confirmed, hold setup and ask the nurse.}}",
             4: "{{fig:bun_sampling}}"},
    "terms": [("Solute", "A substance dissolved in a liquid. Urea and potassium are solutes in blood."),
              ("Concentration gradient", "A difference in how much of a substance is on each side of a membrane. Substances move from the fuller side to the emptier side."),
              ("Clearance", "How much blood is completely cleaned of a substance each minute."),
              ("Interdialytic weight gain", "The weight gained between two sessions, mostly fluid."),
              ("Conductivity", "How well a fluid carries electricity. In dialysate it reflects the total amount of dissolved salts.")],
    "readings": [("dialysis-adequacy.html", "What Kt/V and the urea reduction ratio mean for patients."),
                 ("dialysis-prescription.html", "Each part of the prescription explained."),
                 ("dry-weight-determination.html", "How the clinical team finds the right target weight.")],
    "calcs": ["calc-dialysis-adequacy-ktv.html", "calc-ufr-ceiling.html", "calc-idwg-fluid.html"],
}

_E["05"] = {
    "navs": ["Standard Precautions", "Clean and used", "Waste and exposure", "Extra precautions"],
    "big": """
{{plain:In a dialysis unit, blood is outside the body all day, in every chair. Germs travel on hands, gloves, and shared equipment far more often than through the air. Infection prevention is therefore mostly about what your hands touch, in what order, and whether a surface stayed wet with disinfectant long enough.}}
{{cards:Key terms for this module|Standard Precautions::The basic steps used with every patient, every time, whether or not an infection is known.|Hand hygiene::Cleaning hands with alcohol rub or with soap and water.|Personal protective equipment::Gloves, gown, mask, and eye protection that keep blood off you.|Wet contact time::How long a surface must stay visibly wet with disinfectant for it to work. The product label gives the time.|Point of use::The place and moment where waste is produced. Waste is sorted there, not later.|Bloodborne virus::A virus carried in blood, such as hepatitis B, hepatitis C, or the human immunodeficiency virus (HIV).}}
{{flow:When to clean your hands in a dialysis unit|Before touching a patient::Including their access, chair, or machine.|Before a clean task::Such as handling supplies or connecting lines.|After blood or body fluid::Even if you wore gloves.|After touching a patient::Or the station around them.|After removing gloves::Gloves are not a substitute for clean hands.}}
""",
    "pre": {1: "{{fig:dai_prevention}}",
            4: "{{fig:machine_categories}}"},
    "post": {2: "{{key:If the surface dried before the label time, it was not disinfected. Wet it again and restart the clock.}}{{fig:dai_clinic}}",
             3: "{{stop:After a needlestick or a splash of blood to the eyes, mouth, or broken skin: give first aid at once, tell the nurse, and follow the exposure procedure the same hour. Do not wait until the end of the shift.}}"},
    "terms": [("Clean area", "A place kept for unused supplies and clean tasks only. Nothing used ever returns there."),
              ("Station turnover", "Clearing, cleaning, and disinfecting a station between two patients."),
              ("Sharps container", "A rigid, puncture-proof box for needles and other sharp items."),
              ("Occupational exposure", "Contact with blood through a needlestick, a cut, or a splash to the eyes, nose, mouth, or broken skin."),
              ("Surveillance", "Counting and tracking infections over time so the unit can see problems early.")],
    "readings": [("dialysis-access-infection.html", "How access infections happen and how they are prevented."),
                 ("dialysis-machine-assignment.html", "Machine assignment and isolation by hepatitis status.")],
}

_E["06"] = {
    "navs": ["Two circuits", "Safeguards", "Readiness checks", "Hold and report"],
    "big": """
{{plain:A dialysis machine runs two separate loops that meet only at the dialyzer. The blood loop takes blood out of the patient, through the dialyzer, and back. The fluid loop mixes dialysate, sends it past the fibers, and drains it. The machine watches both loops with sensors and stops if something looks wrong, but sensors miss things. Your eyes are the last safeguard.}}
{{fig:blood_circuit}}
{{cards:Key terms for this module|Extracorporeal circuit::The path blood takes outside the body: tubing, pump segment, dialyzer, and air trap.|Blood pump::A roller pump that squeezes the tubing to move blood.|Arterial and venous lines::By convention, the &ldquo;arterial&rdquo; line carries blood from the patient to the dialyzer and the &ldquo;venous&rdquo; line returns it.|Air detector::A sensor on the return line that stops the pump and clamps the line if it senses air.|Priming::Filling the circuit with fluid to remove air before blood enters.|Instructions for use::The manufacturer&rsquo;s official directions for the exact machine model in front of you.}}
""",
    "pre": {2: "{{cards:What each safeguard watches, and what it cannot see|Pressure monitors::Watch pressure at set points. They can miss a needle that has slipped out.|Air detector and clamp::Watch for air at one point on the return line. Tubing must be seated correctly.|Blood leak detector::Watches used dialysate for blood. It cannot see bleeding outside the circuit.|Conductivity and temperature::Watch the strength and warmth of dialysate. They cannot confirm which concentrate is connected.}}",
            3: "{{fig:hd_params}}"},
    "post": {2: "{{key:An alarm tells you where to look. Silence does not tell you everything is fine. Keep the access and all connections visible.}}",
             4: "{{stop:A machine that fails a required check is out of service until an authorized person clears it. Do not restart it &ldquo;to see if it passes this time&rdquo; and then use it.}}{{flow:When a machine fails a check|Hold::Take the machine out of use and label it.|Record::Write the machine number and the exact message.|Report::Tell the nurse and the biomedical contact. Say whether a patient is connected.|Replace::A substitute machine needs its own full set of checks.|Release::Only a designated person returns the machine to service.}}"},
    "terms": [("Pump segment", "The thicker section of blood tubing that fits inside the blood pump."),
              ("Venous chamber", "The drip chamber on the return line that traps air and small clots. Also called the air trap or bubble trap."),
              ("Transducer protector", "A small filter between the tubing and the machine&rsquo;s pressure sensor that keeps blood out of the machine."),
              ("Self-test", "The automatic checks a machine runs on its own alarms and sensors before treatment."),
              ("Residual disinfectant", "Traces of cleaning chemical left in the machine. A test must show none before use.")],
    "readings": [("high-flux-hd-optimization.html", "How blood flow and dialyzer type affect cleaning."),
                 ("dialysis-prescription.html", "What each machine setting corresponds to in the prescription.")],
}

_E["07"] = {
    "navs": ["Water pathway", "Quality checks", "Concentrates", "Hold and report"],
    "big": """
{{plain:Tap water is safe to drink but not safe for dialysis. A person drinks about 14 liters of water a week; a dialysis patient&rsquo;s blood is exposed to more than 300 liters, with only a thin membrane in between. Chemicals that are harmless in a glass of water can destroy red blood cells in a dialyzer. The water room exists to remove them, and the daily checks exist to prove it did.}}
{{fig:wts_train}}
{{cards:Key terms for this module|Feed water::The water coming into the unit from the city supply or a well.|Carbon tank::A tank of activated carbon that removes chlorine and chloramine.|Chloramine::A disinfectant added to city water. In dialysis it damages red blood cells.|Breakthrough::When a chemical gets past a treatment stage that should have removed it.|Reverse osmosis::Forcing water through a very fine membrane that holds back most dissolved salts, bacteria, and endotoxin.|Endotoxin::A fragment of dead bacteria that can cause fever and chills even when no live bacteria are present.|Concentrate::A strong salt solution that the machine dilutes with treated water to make dialysate.}}
""",
    "pre": {2: "{{fig:wts_tiers}}",
            4: "{{fig:wts_golden}}"},
    "post": {1: "{{key:Each stage protects the next one. Carbon protects the reverse osmosis membrane from chlorine; the softener protects it from scale. A skipped check upstream becomes a failure downstream.}}",
             3: "{{cards:Acid and bicarbonate concentrates|Acid concentrate::Supplies most of the salts, including potassium and calcium. Different formulas exist; the label must match the order.|Bicarbonate concentrate::Supplies the buffer that corrects acid in the blood. Once mixed it supports bacterial growth, so it has a short use time.|The machine mixes::One part of each concentrate with many parts of treated water, in a fixed ratio for that machine.}}",
             4: "{{stop:A total chlorine result above the unit&rsquo;s limit means no new treatments start on that water until an authorized person releases it. A second, better-looking test does not cancel the first one.}}"},
    "terms": [("Product water", "Water that has passed through the reverse osmosis unit and is ready for dialysis use. Also called permeate."),
              ("Reject water", "The stream that carries away what the reverse osmosis membrane held back."),
              ("Distribution loop", "The pipework that carries product water past every station and back again."),
              ("Hardness", "Dissolved calcium and magnesium. It forms scale that blocks membranes."),
              ("Action level", "A result lower than the maximum limit at which the unit must already act."),
              ("Proportioning", "Mixing water and concentrates in a fixed ratio to make dialysate.")],
    "readings": [("dialysis-water-treatment-systems.html", "The full clinical and engineering reference on water treatment.")],
    "calcs": ["calc-ro-recovery-dualpass.html"],
}

_E["08"] = {
    "navs": ["Access types", "Protecting it", "Warning changes", "The case"],
    "big": """
{{plain:To be dialyzed, a patient needs a way to move a large amount of blood out of the body and back, three times a week, for years. That way in is called the vascular access. Patients call it their lifeline, and they are right: without a working access there is no dialysis. A technician does not treat the access but is often the first to notice that something has changed.}}
{{fig:access_types3}}
{{cards:Key terms for this module|Fistula::A vein joined directly to an artery by surgery, so the vein grows large and strong enough for needles.|Graft::A soft synthetic tube placed under the skin to join an artery and a vein.|Catheter::A tube placed in a large vein in the neck or chest, with two ends outside the body.|Thrill::The buzzing you can feel over a working fistula or graft.|Bruit::The whooshing sound you can hear over it with a stethoscope.|Exit site::The place where a catheter comes out through the skin.}}
""",
    "pre": {2: "{{fig:save_veins}}",
            3: "{{fig:look_listen_feel}}"},
    "post": {1: "{{fig:access_circuit}}",
             2: "{{fig:catheter_safety}}",
             3: "{{fig:urgent_signs}}{{stop:No buzz where there is usually a buzz means the access may have clotted. Do not use it. Tell the nurse immediately; early treatment can save the access.}}"},
    "terms": [("Anastomosis", "The surgical join between the artery and the vein."),
              ("Maturation", "The weeks to months a new fistula needs to grow large and strong enough to use."),
              ("Stenosis", "A narrowing inside the access that slows blood flow and can lead to clotting."),
              ("Thrombosis", "A clot that blocks the access."),
              ("Cannulation", "Placing the dialysis needles in a fistula or graft. Who may do this depends on local rules and the facility."),
              ("Lumen", "One channel inside a catheter. A dialysis catheter has two.")],
    "readings": [("hemodialysis-access-lifeline.html", "The access from creation through a lifetime of use."),
                 ("dialysis-access-care.html", "How patients are taught to protect the access."),
                 ("dialysis-access-infection.html", "Recognizing and preventing access infection.")],
}

_E["09"] = {
    "navs": ["Three phases", "Before treatment", "During treatment", "Finish and handoff"],
    "big": """
{{plain:Every dialysis session has the same three parts: before, during, and after. Before, you make sure the right patient, the right order, and a ready machine have come together. During, you watch the patient and the machine and report changes. After, you record what happened, hand over, and reset the station. Most errors happen when a step is skipped because the shift is busy.}}
{{flow:One session at a glance|Arrive::Identify the patient with two identifiers.|Measure::Weight and assigned vital signs. Ask about new symptoms.|Verify::Order, dialyzer, dialysate, machine checks.|Treat::Scheduled observations. Access and lines stay visible.|Complete::Assigned measurements and records.|Turn over::Clear, clean, disinfect, and release the station.}}
{{cards:Key terms for this module|Pre-treatment weight::Today&rsquo;s weight before dialysis, compared with the target weight.|Vital signs::Blood pressure, pulse, temperature, and breathing rate.|Intradialytic::During the dialysis treatment.|Delivered time::How long the treatment actually ran, which may be less than ordered.|Check-back::Repeating an instruction so the giver can confirm it.}}
""",
    "pre": {2: "{{fig:fluid_overview|Before treatment, the scale shows how much fluid has built up. An unexpected weight is checked and reported, not corrected by guesswork.}}",
            3: "{{fig:idh}}"},
    "post": {2: "{{key:Never copy the last session&rsquo;s settings into today&rsquo;s treatment. Orders change, and the patient in front of you may not be the same weight, or even the same patient.}}",
             3: "{{cards:What to look at on every round|The patient::Awake? Comfortable? Any new symptom?|The access::Needles, tape, and connections visible and dry.|The lines::No kinks, no blood where it should not be.|The machine::Pressures and readings close to the last round.|The record::Entered at the time, with the real numbers.}}{{stop:Dizziness, nausea, cramps, chest pain, breathlessness, or blood at the access: tell the nurse at once. Do not change machine settings on your own.}}"},
    "terms": [("Treatment order", "The physician&rsquo;s written prescription for this patient&rsquo;s dialysis."),
              ("Flowsheet", "The treatment record where readings are entered at set times during the session."),
              ("Rinseback", "Returning the blood in the circuit to the patient at the end of treatment."),
              ("Handoff", "Passing responsibility and information to the next person, in a set order, so nothing is lost.")],
    "readings": [("hemodialysis-complications.html", "The common problems during treatment and why they happen."),
                 ("fluid-management-dialysis.html", "Fluid gain between sessions from the patient&rsquo;s side."),
                 ("dialysis-adequacy.html", "Why delivered time matters.")],
    "calcs": ["calc-ufr-ceiling.html", "calc-idwg-fluid.html"],
}

_E["10"] = {
    "navs": ["Recognize", "First response", "Record and review", "Utility failures"],
    "big": """
{{plain:Most sessions are uneventful. A few are not, and trouble on dialysis can develop within minutes. In an emergency a technician has three jobs: recognize that something is wrong, call for help immediately, and then do the task you are given. You are not expected to diagnose the cause or change the treatment.}}
{{flow:Your first thirty seconds|See it::A patient who looks or says they feel suddenly unwell.|Call::Use the unit&rsquo;s emergency call. Say where you are and that you need help now.|Say what you saw::Symptoms, when they started, whether the patient is connected.|Take a task::Bring equipment, guide responders, or assist as directed.|Close the loop::Repeat the instruction and report when it is done.}}
{{cards:Key terms for this module|Hypotension::Low blood pressure. The most common problem during dialysis.|Needle dislodgement::A needle slipping out of the access. Blood loss can be fast and hidden under a blanket.|Hemolysis::Red blood cells breaking apart, for example from overheated or wrongly mixed dialysate or from chloramine.|Air embolism::Air entering the bloodstream. Rare, and an emergency.|Closed-loop communication::Repeating each instruction and confirming when it is completed.}}
""",
    "pre": {1: "{{fig:idh}}",
            2: "{{fig:code_roles}}",
            4: "{{fig:typhoon}}"},
    "post": {1: "{{fig:cramps}}{{stop:Chest pain, breathlessness, collapse, heavy bleeding, or a patient who cannot be woken: call for help first. Measurements and notes come after the call.}}",
             2: "{{fig:code_readiness}}{{fig:bls}}",
             4: "{{key:When water or power comes back, the screen coming back on is not a release. Equipment and utilities return to service only when the designated leads clear them.}}"},
    "terms": [("Anaphylaxis", "A sudden, severe allergic reaction with breathing difficulty, swelling, or collapse."),
              ("Emergency cart", "The trolley of resuscitation equipment and medicines. Know where it is before every shift."),
              ("Debrief", "A short team review after an event: what happened, what went well, what to change."),
              ("Contingency plan", "The unit&rsquo;s written plan for power, water, fire, flood, or evacuation.")],
    "readings": [("code-blue-acls-dialysis-unit.html", "Cardiac arrest response in a dialysis unit, in full."),
                 ("hemodialysis-complications.html", "Why complications during dialysis happen."),
                 ("typhoon-disaster-preparedness-dialysis.html", "Typhoon and disaster planning for dialysis.")],
    "calcs": ["calc-dialysis-continuity-planner.html"],
}

_E["11"] = {
    "navs": ["Single use or reuse", "Traceable records", "Hold and reject", "Equipment quality"],
    "big": """
{{plain:Some units clean, test, and disinfect a dialyzer so the same patient can use it again. This is called reprocessing or reuse. It is safe only when every step is done and recorded, because a mistake can give a patient someone else&rsquo;s dialyzer, a clotted dialyzer, or a dose of disinfectant. The rule that runs through this module: if you cannot prove it, do not use it.}}
{{fig:reuse_steps}}
{{cards:Key terms for this module|Single use::A dialyzer that is used once and discarded.|Reprocessing::Cleaning, testing, and disinfecting a dialyzer for the same patient&rsquo;s next treatment.|Total cell volume::The fluid volume of the fiber bundle. It falls as fibers clot, so it shows whether the dialyzer still cleans well.|Germicide::The chemical that kills microbes inside the stored dialyzer.|Residual test::A test before use that proves the germicide has been rinsed out.|Traceability::Being able to follow one dialyzer through every step, by its label and records.}}
""",
    "pre": {1: "{{fig:reuse_hero}}",
            4: "{{flow:From fault to return to service|Fault noticed::Record the exact message or what you saw.|Hold::Remove from use and label clearly.|Repair::Done by authorized service staff.|Post-service checks::Documented tests that the fault is resolved.|Release::A designated person signs the equipment back into service.}}"},
    "post": {2: "{{fig:reuse_germicide}}",
             3: "{{stop:An unreadable label, a missing test result, or a name that does not match means the dialyzer is held and reported. A passed test does not make up for a failed identity check.}}",
             4: "{{key:A closed work ticket and a normal screen are not a release. Look for the documented clearance.}}"},
    "terms": [("Use count", "How many times a dialyzer has been used. The program sets a maximum."),
              ("Pressure leak test", "A test that shows whether any fibers are broken."),
              ("Dwell time", "How long the germicide must stay in the dialyzer to work."),
              ("Preventive maintenance", "Scheduled service done before something breaks."),
              ("Disposition", "The recorded final decision on a device: released, held, rejected, or discarded.")],
    "readings": [("dialyzer-reprocessing-reuse.html", "The full guide to reprocessing, its history, and its risks."),
                 ("dialysis-qapi-vs-cqi.html", "How equipment problems are tracked in the unit&rsquo;s quality program.")],
}

_E["12"] = {
    "navs": ["Close each hold", "Urgency", "Record and improve", "Five stations", "Logbook", "Exam blueprint"],
    "big": """
{{plain:This last module adds nothing new. It asks you to use everything together, the way a real shift demands: several checks at once, an interruption, a problem that is not yours to solve, and a record that must be right. If you can verify, pause, report, and document under pressure, you are ready for supervised practice.}}
{{flow:The pattern behind every module|Verify::Patient, order, station, machine, water.|Pause::Hold whatever depends on a check that failed.|Report::Tell the right person, with facts and a clear request.|Confirm::Repeat the instruction back.|Record::What you saw, did, and were told, with times.|Release::Only the designated person lifts a hold.}}
{{cards:Key terms for this module|Hold::A stop placed on a patient setup, a machine, or the water supply until a problem is cleared.|Release::Formal permission from the designated person to resume.|Near miss::A problem caught before it reached a patient. Reporting it helps the unit improve.|Plan-Do-Study-Act::A small test of a change: plan it, try it, study the result, act on what you learned.|Competency::A skill you have been observed doing correctly and safely.}}
""",
    "pre": {3: "{{fig:pdsa}}"},
    "post": {3: "{{fig:fishbone}}",
             2: "{{key:Urgent patient symptoms go to the nurse first. Equipment and water problems go to the nurse and the technical lead. If you are unsure which it is, tell the nurse.}}"},
    "terms": [("Simulation", "Practice on training equipment or a mannequin, where mistakes are safe."),
              ("Logbook", "Your record of what you observed and practiced during placement, signed by the preceptor."),
              ("Blueprint", "A table showing how many examination questions come from each topic.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "Quality management in a dialysis center."),
                 ("code-blue-acls-dialysis-unit.html", "Emergency response, reviewed before the practical stations."),
                 ("dialysis-water-treatment-systems.html", "Water treatment, reviewed before the water station.")],
    "calcs": ["calc-dialysis-qapi-scorecard.html"],
}

_ROWS = [
    ("01", "dialysis-unit-technician-role", "The Dialysis Unit and the Technician’s Role", (6, 4, 10),
     "How a dialysis unit runs during a shift, who does what, how to confirm a patient&rsquo;s identity, and how to report and record a problem."),
    ("02", "kidneys-kidney-failure", "Kidneys and Kidney Failure", (8, 2, 10),
     "What healthy kidneys do, what goes wrong when they fail, and how to read and report simple changes in weight, symptoms, and laboratory results."),
    ("03", "treatment-options-living-with-kidney-failure", "Treatment Options and Living with Kidney Failure", (8, 2, 10),
     "The five ways kidney failure is treated, what home dialysis involves, and how to listen, explain the basics, and refer questions."),
    ("04", "principles-of-hemodialysis", "Principles of Hemodialysis", (8, 4, 10),
     "How a dialyzer removes wastes and water, what dialysate is for, how the fluid numbers differ, and what adequacy tests measure."),
    ("05", "infection-prevention-waste-management", "Dialysis Infection Prevention and Waste Management", (6, 6, 14),
     "Hand hygiene, protective equipment, clean and used areas, station turnover and contact time, waste sorting, and what to do after a blood exposure."),
    ("06", "machines-dialyzers-extracorporeal-circuit", "Machines, Dialyzers, and the Extracorporeal Circuit", (6, 8, 16),
     "The blood path and the dialysate path, what each alarm watches and misses, readiness checks, and what to do when a machine fails a check."),
    ("07", "water-treatment-concentrates-dialysate", "Water Treatment, Concentrates, and Dialysate", (6, 6, 16),
     "How tap water becomes dialysis water, which test checks what, how concentrates become dialysate, and how to respond to an out-of-range result."),
    ("08", "vascular-access-recognition-protection", "Vascular Access Recognition and Protection", (6, 6, 14),
     "Fistulas, grafts, and catheters; how to protect the access in everyday care; and the changes that must be reported at once."),
    ("09", "the-hemodialysis-session", "The Hemodialysis Session", (6, 8, 18),
     "One treatment from arrival to station turnover: what to verify before, what to watch during, and how to finish and hand over."),
    ("10", "complications-emergency-response", "Complications and Emergency Response", (6, 6, 16),
     "Recognizing trouble during dialysis, calling for help, working in an emergency team, and responding to water, power, and facility failures."),
    ("11", "dialyzer-reprocessing-equipment-quality", "Dialyzer Reprocessing and Equipment Quality", (4, 4, 12),
     "Single use and same-patient reuse, the records that make a dialyzer traceable, when to hold or reject, and how equipment returns to service."),
    ("12", "integrated-practice-competency-assessment", "Integrated Practice and Competency Assessment", (2, 4, 22),
     "Everything together: readiness checks, urgent reports, records and improvement, five practical stations, the logbook, and the examination blueprint."),
]

MODULES = [{"id": i, "slug": s, "title": t, "hours": h, "sub": sub, "src": True, "enrich": _E[i],
            "case_title": "A name that almost matched" if i == "01" else ""} for i, s, t, h, sub in _ROWS]
