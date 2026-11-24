# -*- coding: utf-8 -*-
"""Dialysis Technician study series (Renal Technician Program; formerly titled Hemodialysis Technician; slugs unchanged).

Lesson text, cases, checklists and question banks come from the Markdown sources in src/NN/
(Study Guide.md, Self-Assessment.md, Answer Key.md), copied from ~/Documents/HD Technicians.
Everything in `enrich` below is added on top: the plain-words opener, extra figures, key points,
glossary terms and site reading. Edit the Markdown to change the lesson; edit here to change the extras."""

COURSE = {
    "title": "Dialysis Technician",
    "short": "Dialysis Technician",
    "hub_slug": "hemodialysis-technician",
    "label": "Study series for dialysis technicians",
    "tag": "Renal Technician Program",
    "audience": "Entry-level dialysis technicians and trainees &middot; preceptors, head nurses, and training providers",
    "audience_type": "Dialysis technicians",
    "level": "Entry-level allied health, college reading level",
    "review_date": "2026-11-23",
    "draw": 5,
    "exam_draw": 40,
    "mastery": "4 of 5",
    "keywords": "dialysis technician training Philippines, renal technician course, hemodialysis technician training Philippines, dialysis technician course, dialysis technician study guide, hemodialysis machine setup, dialysis water treatment basics, dialyzer reprocessing, dialysis technician competency checklist",
    "page_title": "Dialysis Technician: A 12-Module Study Series",
    "desc": ("A free 12-module study series for dialysis technicians in the Philippines: the dialysis unit and your role in it, "
             "kidney failure, how hemodialysis works, infection prevention, machines and the blood circuit, water and dialysate, vascular access, "
             "the treatment session, emergencies, and dialyzer reprocessing. Plain language and many figures, with a case, a skills checklist, and a self-assessment in every module."),
    "h1": "Dialysis <em>Technician</em>",
    "sub": "A twelve-module study series for the people who prepare and check the equipment that keeps dialysis patients alive. It is written in plain language, with a picture for every idea that needs one.",
    "disclaimer": ("Educational study material for dialysis technicians. It does not replace physician orders, the supervising nurse&rsquo;s direction, "
                   "approved unit procedures, manufacturer instructions, DOH licensing requirements, or supervised training."),
    "scope_note": ("This module is study material for dialysis technicians. It explains why safe practice works the way it does. It does not replace "
                   "the physician&rsquo;s orders, the supervising nurse&rsquo;s direction, your unit&rsquo;s approved procedures, or the manufacturer&rsquo;s "
                   "instructions for use. What a technician may do differs between countries and between facilities, so do only the tasks you are trained, "
                   "assigned, and signed off to do. Every case is fictional."),
    "branch_img": "hemodialysis-technician-01-dialysis-unit-technician-role-card.webp",
    "branch_role": "Foundation &middot; chairside",
    "branch_blurb": "Stations, machines, the blood circuit, the treatment session, and safe teamwork with the dialysis nurse.",
    "hero_alt": "A trainee technician and a nurse talk with a patient beside a dialysis machine.",
    "start_h2": "A study series for the people behind the machines",
    "start_html": """
<p>A hemodialysis (HD) technician prepares the station, sets up and checks the machine, helps watch the treatment, cleans and resets the station, and keeps the records that prove each step was done. The tasks are technical. The purpose behind them is plain: every patient receives the right treatment, on safe equipment, with clean water, every time.</p>
<p>The series has twelve modules. It begins with the dialysis unit and your place in the team, and moves through kidney failure and the science of dialysis. It then covers infection prevention, machines, water, vascular access, the treatment session, emergencies, and dialyzer reprocessing. The last module brings all of it together in a practical assessment.</p>
{{cards:What makes this series easier to study|Plain language::Written for a college-level reader. A technical term is explained the first time it appears, and again in the glossary.|Pictures first::Illustrations, flow strips, and tables let you see an idea before you read the detail.|Real shift problems::Every module opens with a fictional case from an ordinary shift and returns to it at the end.|Know your limits::Every module states plainly what a technician reports and what the nurse or physician decides.}}
<p>The series is free. It needs no account, and nothing you answer is sent to any server.</p>
""",
    "is_not": ("This is study material. It is not a license, a certificate of training, or proof of competence, and it carries no Continuing Professional "
               "Development (CPD) units. In the Philippines, the Department of Health (DOH) licenses dialysis facilities, and what a technician may do "
               "is set by the facility under that license and by the supervising nurse and nephrologist.[[doh2012]][[psn2024]] "
               "Skills are learned, and signed off, on real equipment with a preceptor."),
    "pathway_note": """
<p>Start with this series whichever role you are aiming for. Water treatment and biomedical technicians need the same foundation. The water they produce and the machines they repair end at a patient, and they must understand what that patient is going through.</p>
""",
    "modules_h2": "Twelve modules, in order",
    "modules_intro": "Study the modules in order, because each one builds on the one before. If you tick the box on a module&rsquo;s self-assessment, your result appears on that module&rsquo;s card here. It is stored only in this browser.",
    "syllabus_note": ("The hours are a proposed design for a provider-led program of about three months: 72 classroom hours, 60 skills-lab hours, and 168 "
                      "hours of supervised placement, 300 hours in all. They are a planning proposal. They are not a regulatory requirement."),
    "assessment_html": """
<p>The questions at the end of each module are for practice. Each visit draws five from a bank of fifteen, and every question explains its best answer. Retry as often as you like.</p>
<p>Skills work differently. Nobody learns to ride a motorcycle from the owner&rsquo;s manual, and nobody can learn or be judged on setting up a circuit, testing water for chlorine, or answering an alarm from a screen. Each module therefore has a skills checklist that a preceptor completes while watching you work on the unit&rsquo;s own equipment. Steps marked <span class="tc-crit">Critical</span> are the steps where a mistake can reach a patient. Every one of them must be done correctly before sign-off.</p>
{{cards:Three levels of learning a skill|Observed::You watched a qualified person do it. That is exposure, not permission.|Supervised practice::You did it while a preceptor watched and could step in.|Signed off::A preceptor recorded that you did it correctly and safely. Only then is it part of your assigned work.}}
""",
    "sources_html": """
<p>The scope follows Philippine expectations for dialysis facilities and internationally used technician curricula. Two Philippine sources set what applies locally: the DOH licensing order for dialysis facilities and the Philippine Society of Nephrology (PSN) guidelines for hemodialysis clinics.[[doh2012]][[psn2024]] International sources served as a check that nothing important was left out: the Medical Education Institute (MEI) Core Curriculum for the Dialysis Technician, the United States certification outlines for the Certified Clinical Hemodialysis Technician (CCHT) and Certified Hemodialysis Technologist/Technician (CHT), the United States federal personnel standard for dialysis technicians, and the infection-prevention guidance of the Centers for Disease Control and Prevention (CDC).[[mei7]][[nncc_ccht]][[bonent]][[cms494]][[cdc_dialysis]] Each module lists its own sources.</p>
<p>International credentials and rules are used here only to map topics. They do not apply to Philippine practice. Tasks such as needle insertion, catheter care, and giving medicines are assigned differently from one country to another.</p>
""",
    "trainer_h2": "A proposed 300-hour program",
    "trainer_html": """
<p>The series is built to be the guided-study part of a provider-led program for entry-level, in-center dialysis technicians. The proposed design runs for three calendar months: 72 classroom hours, 60 skills-lab hours, and 168 hours of supervised placement. It starts with the foundations of role and safety, moves through technology and treatment support, and ends with integrated assessment. The hours for each module are in the syllabus on the <a href="hemodialysis-technician.html#syllabus">course home page</a>.</p>
{{flow:Suggested teaching sequence for each module|Present the case::Ask learners for a first response before you teach anything.|Teach the lesson::Follow the objectives in order, with one worked example.|Revisit the case::Have learners explain and defend their response.|Skills lab::Simulate the checklist on training equipment.|Placement::Log one related activity, the level of supervision, and the preceptor&rsquo;s feedback.}}
<p>Record observation, simulation, and supervised performance separately. Patient-facing duties and sign-off follow the facility&rsquo;s authorization and Philippine regulation, not this series.[[doh2012]][[psn2024]]</p>
""",
    "completion_html": """
<ul>
<li>Module self-assessments: a suggested target of 12 of 15 across each module&rsquo;s full bank, with a review of every missed safety-critical item.</li>
<li>A separate written examination set by the provider: a proposed 100 items with an 80% target. The blueprint is in Module 12.</li>
<li>Five observed practical stations (Module 12): station turnover, equipment readiness, water quality, patient and access handoff, and emergency response.</li>
<li>A placement logbook reviewed by the preceptor.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated correctly.</li>
</ul>
<p>These are proposals for the provider to adapt. A self-assessment score is a record of study, nothing more.</p>
""",
    "related": [("dialysis-water-treatment-systems.html", "The reference for Module 7."),
                ("dialyzer-reprocessing-reuse.html", "The reference for Module 11."),
                ("code-blue-acls-dialysis-unit.html", "The reference for Module 10.")],
}

_E = {}

_E["01"] = {
    "navs": ["The shift", "Your role", "Handoff and records"],
    "big": """
{{plain:A dialysis unit runs like an airport. Many people do different jobs, every step is checked, and nothing moves forward until the check is complete. A member of the ground crew does not fly the plane, but one who sees a fuel leak tells the captain before the plane moves. Your work as a technician is the same: prepare and check, notice, and report. You are never expected to decide alone.}}
<p>The picture has a limit. A bag sent to the wrong city can be flown back. A dialyzer, a dialysate, or a fluid goal set up for the wrong person goes into a patient&rsquo;s bloodstream, and it cannot be taken back. That is why the checks in this module come before the work, not after it.</p>
{{cards:Key terms for this module|Station::One treatment place: a chair or bed, a dialysis machine, and the tubing set for one patient.|Two identifiers::Two facts that belong to one person only, such as full name and date of birth. A chair number is not an identifier.|Escalate::Tell the right person now, in clear words, because the problem is beyond your role.|SBAR::A four-part way to report: Situation, Background, Assessment, Recommendation.|Check-back::Repeating an instruction aloud so that the other person can confirm you heard it correctly.|Near miss::An error that was caught before it reached the patient.}}
{{flow:The three habits this module teaches|Verify::Match the patient, the record, and the equipment before you act.|Pause::When anything does not match, stop the work that depends on it.|Report::Tell the nurse what you saw, what you did, and what you need.}}
""",
    "pre": {1: "{{fig:blood_circuit|One dialysis station: the patient, the chair, the machine, and the tubing circuit that takes blood through the dialyzer and back. A station is prepared and checked for one patient at a time.}}",
            2: "{{cards:Who decides what|Technician::Prepares and checks the equipment, performs assigned tasks, and observes, records, and reports.|Dialysis nurse::Assesses the patient, directs care, and delegates and supervises tasks.|Nephrologist::Writes the dialysis prescription and is the one who changes it.|Biomedical and water staff::Find and fix faults in the machines and the water system, and clear them for use.}}",
            3: "{{flow:SBAR, step by step|Situation::What is happening right now, in one sentence.|Background::The facts that explain it.|Assessment::What you think the problem is, or simply what does not match.|Recommendation::What you need from the listener, and by when.}}"},
    "post": {1: "{{key:Treat a clean station, a working machine, and a correctly identified patient as three separate checks. Passing one never passes the other two.}}",
             2: "{{stop:When either identifier does not match, stop patient-specific setup and tell the supervising nurse. A habit such as &ldquo;she always sits there&rdquo; never replaces the check.}}"},
    "terms": [("Extracorporeal circuit", "The tubing and the dialyzer that carry blood outside the body during treatment."),
              ("Delegated task", "A task that a nurse assigns to you. The nurse remains responsible for supervising it."),
              ("Objective note", "A record of what was seen, heard, measured, and done, with the times, and without guesses or opinions."),
              ("Audit trail", "The record that shows who changed an entry, when, and why.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How near-miss reports feed the unit&rsquo;s quality program."),
                 ("dialysis-machine-assignment.html", "Why some machines and stations are reserved for certain patients.")],
}

_E["02"] = {
    "navs": ["Blood to urine", "When kidneys fail", "AKI, CKD, failure", "Reading trends"],
    "big": """
{{plain:Picture the water filter under a kitchen sink, except that this one never switches off and also keeps the household accounts. Healthy kidneys clean the blood day and night, remove extra water, keep body salts in balance, and send signals that keep blood and bones healthy. When they fail, wastes and water stay in the body. Dialysis takes over part of the cleaning and water removal, a few hours at a time.}}
<p>The picture has a limit. A sink filter does one job, and the kidneys do several at once. Dialysis replaces only part of that work, and only during the hours a patient is connected. Between sessions, wastes and water build up again. That is why the weights, symptoms, and laboratory trends you learn to read and report in this module matter.</p>
{{fig:kidneys}}
{{cards:Key terms for this module|Nephron::The tiny working unit of the kidney. Each kidney has about a million.|Glomerulus::The filter at the start of each nephron.|Tubule::The tube after the filter. It takes back what the body needs.|Electrolytes::Body salts, such as sodium and potassium, that carry an electric charge.|Edema::Swelling caused by extra fluid in the tissues.|Anemia::Too few red blood cells. It causes tiredness and breathlessness.}}
""",
    "pre": {1: "{{fig:nephron}}",
            2: "{{fig:ckd_cascade|When nephrons are lost, several kidney jobs fail together. The table below gives the four main jobs in words.}}",
            4: "{{fig:fluid_overview}}{{formula:<strong>Weight change between sessions</strong> = today&rsquo;s weight before treatment &minus; the last weight after treatment.<br>Example: 69.4 kg &minus; 67.2 kg = 2.2 kg. One liter of water weighs about one kilogram, so the change suggests about 2.2 liters of fluid.}}"},
    "post": {3: "{{cards:Three terms on a timeline|Acute kidney injury::Kidney function falls over hours to days. It may recover.|Chronic kidney disease::A kidney problem that has lasted three months or longer.|Kidney failure::Function has fallen so low that dialysis, a transplant, or conservative care is needed.}}",
             4: "{{stop:New shortness of breath, chest pain, or confusion is never &ldquo;just fluid.&rdquo; Tell the nurse first, and finish your notes afterward.}}"},
    "terms": [("Urea and creatinine", "Waste products in the blood. Laboratories measure them to judge how well the kidneys, or dialysis, are cleaning the blood."),
              ("Potassium", "A body salt that controls the heart&rsquo;s rhythm. A high level can stop the heart without any warning sign."),
              ("Bicarbonate", "The body&rsquo;s main buffer against acid. Dialysis fluid supplies it."),
              ("Baseline", "What is usual for this patient. A change from baseline tells you more than a single number does."),
              ("Estimated GFR", "A calculation from a blood test that estimates how much blood the kidneys filter each minute.")],
    "readings": [("kidney-functions.html", "A fuller, illustrated tour of everything the kidneys do."),
                 ("fluid-management-dialysis.html", "What patients are taught about fluid between sessions.")],
    "calcs": ["calc-idwg-fluid.html"],
}

_E["03"] = {
    "navs": ["Five pathways", "Home dialysis", "Daily life", "Teach-back"],
    "big": """
{{plain:Choosing a treatment for kidney failure is a little like choosing how to get to work. A jeepney, a tricycle, a car, or working from home can each be the right answer, depending on where the person lives, what the person can manage, and what matters most to them. Kidney failure can be treated in more than one way, and no single way suits everyone. Patients often ask the technician first, because you are the person they see most.}}
<p>The picture has a limit. A commuter can pick a different ride tomorrow. Whether a treatment suits a patient depends on the patient, the home, and the local program, and the clinical team decides it. Your part is to listen, explain the basics with approved materials, and pass the question to the nurse or physician who can answer it for that patient.</p>
{{fig:modalities}}
{{cards:Key terms for this module|In-center hemodialysis::Dialysis done at a clinic by staff, usually three times a week.|Home hemodialysis::The same kind of treatment, done at home after training.|Peritoneal dialysis::Dialysis that uses the lining of the abdomen as the filter.|Transplant::A donated kidney placed by surgery.|Conservative kidney management::Active care for symptoms and comfort, without dialysis or a transplant.|Teach-back::Asking the patient to explain the plan in their own words, to check that your explanation worked.}}
""",
    "pre": {2: "{{fig:pd_exchange}}",
            4: "{{flow:Teach-back in four steps|Explain::One or two points, in plain words.|Ask::&ldquo;To be sure I explained it well, what will you do if&hellip;?&rdquo;|Listen::Notice anything that is missing or mixed up.|Explain again::Use different words, then ask again.}}"},
    "post": {1: "{{fig:tx_overview}}",
             3: "{{key:Treat a missed session as a safety problem, not a scheduling detail. Tell the nurse the same day.}}"},
    "terms": [("Care partner", "A family member or friend who is trained to help with home dialysis."),
              ("Cycler", "The machine that performs peritoneal dialysis exchanges automatically, usually overnight."),
              ("Exchange", "One round of draining the used peritoneal dialysis fluid and filling with fresh fluid."),
              ("Eligibility", "Whether a treatment is medically and practically suitable for one person. The clinical team decides it.")],
    "readings": [("hemodialysis-modalities.html", "The forms of dialysis compared in more detail."),
                 ("peritoneal-dialysis-ckd.html", "How peritoneal dialysis works day to day."),
                 ("kidney-transplant.html", "Who can receive a transplant and what follows."),
                 ("home-hemodialysis-philippines.html", "Home hemodialysis from a Philippine point of view.")],
}

_E["04"] = {
    "navs": ["The dialyzer", "Dialysate", "Fluid numbers", "Adequacy"],
    "big": """
{{plain:Picture a dialyzer as a bundle of very thin hollow straws packed inside a tube. Blood flows inside the straws, and a cleaning fluid called dialysate flows around them. Wastes pass through the straw walls into the fluid, and extra water is pushed out by pressure. That is the whole idea. The rest of this module is detail.}}
<p>The picture has a limit. A drinking straw has a solid wall, and a dialyzer fiber does not. Its wall is a membrane with pores that let water and small particles through but hold back blood cells and large proteins. The three everyday pictures below show the three ways that substances cross it.</p>
{{fig:dialyzer_anatomy}}
{{cards:Three everyday pictures|Tea bag = diffusion::Color spreads out of a tea bag into the water because it is more concentrated inside the bag. Nothing pushes it. Wastes such as urea leave the blood the same way.|Coffee press = ultrafiltration::Pushing the plunger forces water through a mesh. Pressure does the work. Extra water leaves the blood the same way.|River carrying sand = convection::Moving water drags dissolved substances along with it.}}
{{cards:Key terms for this module|Semipermeable membrane::A wall with pores that let water and small particles through but hold back blood cells and large proteins.|Dialysate::The prepared fluid that flows around the fibers and receives the wastes.|Countercurrent flow::Blood and dialysate flowing in opposite directions. It keeps cleaning efficient along the whole length of the fiber.|Target weight::The weight the clinical team aims for at the end of treatment. It is also called dry weight.|Ultrafiltration goal::The amount of fluid ordered to be removed in this session.}}
""",
    "pre": {1: "{{fig:diff_conv}}",
            3: "{{fig:two_compartment}}",
            4: "{{fig:hd_week}}"},
    "post": {2: "{{key:A normal conductivity reading shows that the mix has the right overall strength. It does not show that the right concentrate was connected. Read the label as well as the display.}}",
             3: "{{stop:Enter a fluid-removal number only from the confirmed order, never because it &ldquo;looks right.&rdquo; If the ordered goal is not confirmed, hold setup and ask the nurse.}}",
             4: "{{fig:bun_sampling}}"},
    "terms": [("Solute", "A substance dissolved in a liquid. Urea and potassium are solutes in blood."),
              ("Concentration gradient", "A difference in how much of a substance is on each side of a membrane. The substance moves from the fuller side to the emptier side."),
              ("Clearance", "How much blood is completely cleaned of a substance each minute."),
              ("Interdialytic weight gain", "The weight gained between two sessions. Most of it is fluid."),
              ("Conductivity", "How well a fluid carries electricity. In dialysate it reflects the total amount of dissolved salts.")],
    "readings": [("dialysis-adequacy.html", "What Kt/V and the urea reduction ratio mean for patients."),
                 ("dialysis-prescription.html", "Each part of the prescription explained."),
                 ("dry-weight-determination.html", "How the clinical team finds the right target weight.")],
    "calcs": ["calc-dialysis-adequacy-ktv.html", "calc-ufr-ceiling.html", "calc-idwg-fluid.html"],
}

_E["05"] = {
    "navs": ["Standard Precautions", "Clean and used", "Waste and exposure", "Extra precautions"],
    "big": """
{{plain:Think of a busy carinderia kitchen at lunchtime. Raw meat, cooked rice, and clean plates pass through the same few hands, and sickness spreads on what those hands and cloths carry from one to the next, not through the air. A dialysis unit works the same way. Blood is outside the body all day, in every chair, and germs travel on hands, gloves, and shared equipment far more often than through the air.}}
<p>The picture has a limit. In a kitchen, dirt is often visible. In a dialysis unit it often is not, and a surface that looks clean may not be disinfected. You cannot judge by eye. Infection prevention is therefore mostly about what your hands touch, in what order, and whether a surface stayed wet with disinfectant long enough.</p>
{{cards:Key terms for this module|Standard Precautions::The basic steps used with every patient, every time, whether or not an infection is known.|Hand hygiene::Cleaning the hands with alcohol rub or with soap and water.|Personal protective equipment::Gloves, gown, mask, and eye protection that keep blood off you.|Wet contact time::How long a surface must stay visibly wet with disinfectant for the disinfectant to work. The product label gives the time.|Point of use::The place and moment where waste is produced. Waste is sorted there, not later.|Bloodborne virus::A virus carried in blood, such as hepatitis B, hepatitis C, or the human immunodeficiency virus (HIV).}}
{{flow:When to clean your hands in a dialysis unit|Before touching a patient::This includes the patient&rsquo;s access, chair, or machine.|Before a clean task::Such as handling supplies or connecting lines.|After blood or body fluid::Even if you wore gloves.|After touching a patient::Or the station around the patient.|After removing gloves::Gloves do not replace clean hands.}}
""",
    "pre": {1: "{{fig:dai_prevention}}",
            4: "{{fig:machine_categories}}"},
    "post": {2: "{{key:If the surface dried before the time on the label, it was not disinfected. Wet it again and start the clock over.}}{{fig:dai_clinic}}",
             3: "{{stop:After a needlestick, or a splash of blood to the eyes, mouth, or broken skin, give first aid at once, tell the nurse, and follow the exposure procedure within the same hour. Do not wait until the end of the shift.}}"},
    "terms": [("Clean area", "A place kept only for unused supplies and clean tasks. Nothing that has been used ever returns there."),
              ("Station turnover", "Clearing, cleaning, and disinfecting a station between two patients."),
              ("Sharps container", "A rigid, puncture-proof box for needles and other sharp items."),
              ("Occupational exposure", "Contact with blood through a needlestick, a cut, or a splash to the eyes, nose, mouth, or broken skin."),
              ("Surveillance", "Counting and tracking infections over time, so that the unit sees a problem early.")],
    "readings": [("dialysis-access-infection.html", "How access infections happen and how they are prevented."),
                 ("dialysis-machine-assignment.html", "Machine assignment and isolation by hepatitis status.")],
}

_E["06"] = {
    "navs": ["Two circuits", "Safeguards", "Readiness checks", "Hold and report"],
    "big": """
{{plain:A dialysis machine runs two separate loops that meet only at the dialyzer. The blood loop takes blood out of the patient, through the dialyzer, and back. The fluid loop mixes dialysate, sends it past the fibers, and drains it. The machine watches both loops with sensors, the way a guard watches a building through security cameras, and it stops when something looks wrong.}}
<p>The picture has a limit, and it is the limit of every camera. A sensor sees only the point where it sits. A needle that has slipped out, or a concentrate of the wrong formula, can pass without an alarm. Sensors miss things. Your eyes are the last safeguard.</p>
{{fig:blood_circuit}}
{{cards:Key terms for this module|Extracorporeal circuit::The path blood takes outside the body: the tubing, the pump segment, the dialyzer, and the air trap.|Blood pump::A roller pump that squeezes the tubing to move blood.|Arterial and venous lines::By convention, the &ldquo;arterial&rdquo; line carries blood from the patient to the dialyzer, and the &ldquo;venous&rdquo; line returns it.|Air detector::A sensor on the return line that stops the pump and clamps the line when it senses air.|Priming::Filling the circuit with fluid to remove the air before blood enters.|Instructions for use::The manufacturer&rsquo;s official directions for the exact machine model in front of you.}}
""",
    "pre": {2: "{{cards:What each safeguard watches, and what it cannot see|Pressure monitors::Watch the pressure at set points. They can miss a needle that has slipped out.|Air detector and clamp::Watch for air at one point on the return line. The tubing must be seated correctly for it to work.|Blood leak detector::Watches the used dialysate for blood. It cannot see bleeding outside the circuit.|Conductivity and temperature::Watch the strength and warmth of the dialysate. They cannot confirm which concentrate is connected.}}",
            3: "{{fig:hd_params}}"},
    "post": {2: "{{key:An alarm tells you where to look. Silence does not tell you that everything is fine. Keep the access and every connection in view.}}",
             4: "{{stop:A machine that fails a required check stays out of service until an authorized person clears it. Do not restart it &ldquo;to see if it passes this time&rdquo; and then use it.}}{{flow:When a machine fails a check|Hold::Take the machine out of use and label it.|Record::Write down the machine number and the exact message.|Report::Tell the nurse and the biomedical contact. Say whether a patient is connected.|Replace::A substitute machine needs its own full set of checks.|Release::Only a designated person returns the machine to service.}}"},
    "terms": [("Pump segment", "The thicker section of blood tubing that fits inside the blood pump."),
              ("Venous chamber", "The drip chamber on the return line that traps air and small clots. It is also called the air trap or bubble trap."),
              ("Transducer protector", "A small filter between the tubing and the machine&rsquo;s pressure sensor. It keeps blood out of the machine."),
              ("Self-test", "The automatic checks that a machine runs on its own alarms and sensors before treatment."),
              ("Residual disinfectant", "Traces of cleaning chemical left in the machine. A test must show none before use.")],
    "readings": [("high-flux-hd-optimization.html", "How blood flow and dialyzer type affect cleaning."),
                 ("dialysis-prescription.html", "What each machine setting corresponds to in the prescription.")],
}

_E["07"] = {
    "navs": ["Water pathway", "Quality checks", "Concentrates", "Hold and report"],
    "big": """
{{plain:Tap water is safe to drink but not safe for dialysis. A person drinks about 14 liters of water a week. A dialysis patient&rsquo;s blood is exposed to more than 300 liters, with only a thin membrane in between. Chemicals that do no harm in a glass of water can destroy red blood cells in a dialyzer. The water room exists to remove them, and the daily checks exist to prove that it did.}}
<p>The comparison with a drinking glass has a limit. Water that looks and tastes clean in a glass usually is. Water for dialysis can be perfectly clear and still carry chloramine, endotoxin, or dissolved salts. Only a test shows what is in it, and only a recorded result proves that the test was done.</p>
{{fig:wts_train}}
{{cards:Key terms for this module|Feed water::The water that comes into the unit from the city supply or a well.|Carbon tank::A tank of activated carbon that removes chlorine and chloramine.|Chloramine::A disinfectant added to city water. In dialysis it damages red blood cells.|Breakthrough::When a chemical gets past a treatment stage that should have removed it.|Reverse osmosis::Forcing water through a very fine membrane that holds back most dissolved salts, bacteria, and endotoxin.|Endotoxin::A fragment of dead bacteria. It can cause fever and chills even when no live bacteria are present.|Concentrate::A strong salt solution that the machine dilutes with treated water to make dialysate.}}
""",
    "pre": {2: "{{fig:wts_tiers}}",
            4: "{{fig:wts_golden}}"},
    "post": {1: "{{key:Each stage protects the next one. Carbon protects the reverse osmosis membrane from chlorine, and the softener protects it from scale. A check skipped upstream becomes a failure downstream.}}",
             3: "{{cards:Acid and bicarbonate concentrates|Acid concentrate::Supplies most of the salts, including potassium and calcium. Different formulas exist, and the label must match the order.|Bicarbonate concentrate::Supplies the buffer that corrects acid in the blood. Once mixed, it supports bacterial growth, so its use time is short.|The machine mixes::One part of each concentrate with many parts of treated water, in a fixed ratio for that machine.}}",
             4: "{{stop:A total chlorine result above the unit&rsquo;s limit means that no new treatment starts on that water until an authorized person releases it. A second test that looks better does not cancel the first.}}"},
    "terms": [("Product water", "Water that has passed through the reverse osmosis unit and is ready for dialysis use. It is also called permeate."),
              ("Reject water", "The stream that carries away what the reverse osmosis membrane held back."),
              ("Distribution loop", "The pipework that carries product water past every station and back again."),
              ("Hardness", "Dissolved calcium and magnesium. They form scale that blocks membranes."),
              ("Action level", "A result below the maximum limit at which the unit must already act."),
              ("Proportioning", "Mixing water and concentrates in a fixed ratio to make dialysate.")],
    "readings": [("dialysis-water-treatment-systems.html", "The full clinical and engineering reference on water treatment.")],
    "calcs": ["calc-ro-recovery-dualpass.html"],
}

_E["08"] = {
    "navs": ["Access types", "Protecting it", "Warning changes", "The case"],
    "big": """
{{plain:Picture an island town joined to the mainland by a single bridge. Everything the town needs crosses that bridge. To be dialyzed, a patient needs a way to move a large amount of blood out of the body and back, three times a week, for years. That way in is called the vascular access, and it is the patient&rsquo;s bridge. Patients call it their lifeline, and they are right: without a working access there is no dialysis.}}
<p>The picture has a limit. A bridge stays the same from week to week, and an access does not. It can narrow, clot, or become infected, and the first sign is often small: a buzz that feels different, a dressing that is wet, a needle site that bleeds longer than usual. A technician does not treat the access, but is often the first person to notice that something has changed.</p>
{{fig:access_types3}}
{{cards:Key terms for this module|Fistula::A vein joined directly to an artery by surgery, so that the vein grows large and strong enough for needles.|Graft::A soft synthetic tube placed under the skin to join an artery and a vein.|Catheter::A tube placed in a large vein in the neck or chest, with two ends outside the body.|Thrill::The buzzing you can feel over a working fistula or graft.|Bruit::The whooshing sound you can hear over it with a stethoscope.|Exit site::The place where a catheter comes out through the skin.}}
""",
    "pre": {2: "{{fig:save_veins}}",
            3: "{{fig:look_listen_feel}}"},
    "post": {1: "{{fig:access_circuit}}",
             2: "{{fig:catheter_safety}}",
             3: "{{fig:urgent_signs}}{{stop:No buzz where there is usually a buzz means that the access may have clotted. Do not use it. Tell the nurse immediately, because early treatment can save the access.}}"},
    "terms": [("Anastomosis", "The surgical join between the artery and the vein."),
              ("Maturation", "The weeks to months a new fistula needs to grow large and strong enough to use."),
              ("Stenosis", "A narrowing inside the access. It slows blood flow and can lead to clotting."),
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
{{plain:Every dialysis session has the same three parts, like a jeepney trip: boarding, the ride, and getting off. Before, you make sure that the right patient, the right order, and a ready machine have come together. During, you watch the patient and the machine and report changes. After, you record what happened, hand over, and reset the station.}}
<p>The picture has a limit. A trip you take every day invites shortcuts, and a dialysis session does not forgive them. Most errors happen when a step is skipped because the shift is busy. The sequence below exists so that a busy shift and a quiet one are run the same way.</p>
{{flow:One session at a glance|Arrive::Identify the patient with two identifiers.|Measure::Weight and the assigned vital signs. Ask about new symptoms.|Verify::The order, the dialyzer, the dialysate, and the machine checks.|Treat::Observations on schedule. The access and lines stay in view.|Complete::The assigned measurements and records.|Turn over::Clear, clean, disinfect, and release the station.}}
{{cards:Key terms for this module|Pre-treatment weight::Today&rsquo;s weight before dialysis, compared with the target weight.|Vital signs::Blood pressure, pulse, temperature, and breathing rate.|Intradialytic::During the dialysis treatment.|Delivered time::How long the treatment actually ran. It may be less than the time ordered.|Check-back::Repeating an instruction so that the person who gave it can confirm it.}}
""",
    "pre": {2: "{{fig:fluid_overview|Before treatment, the scale shows how much fluid has built up. An unexpected weight is checked and reported, never corrected by guesswork.}}",
            3: "{{fig:idh}}"},
    "post": {2: "{{key:Never copy the last session&rsquo;s settings into today&rsquo;s treatment. Orders change, and the patient in front of you may not weigh the same, or may not even be the same patient.}}",
             3: "{{cards:What to look at on every round|The patient::Awake? Comfortable? Any new symptom?|The access::Needles, tape, and connections in view and dry.|The lines::No kinks, and no blood where blood should not be.|The machine::Pressures and readings close to those of the last round.|The record::Entered at the time, with the real numbers.}}{{stop:Dizziness, nausea, cramps, chest pain, breathlessness, or blood at the access: tell the nurse at once. Do not change the machine settings on your own.}}"},
    "terms": [("Treatment order", "The physician&rsquo;s written prescription for this patient&rsquo;s dialysis."),
              ("Flowsheet", "The treatment record where readings are entered at set times during the session."),
              ("Rinseback", "Returning the blood in the circuit to the patient at the end of treatment."),
              ("Handoff", "Passing responsibility and information to the next person, in a set order, so that nothing is lost.")],
    "readings": [("hemodialysis-complications.html", "The common problems during treatment and why they happen."),
                 ("fluid-management-dialysis.html", "Fluid gain between sessions from the patient&rsquo;s side."),
                 ("dialysis-adequacy.html", "Why delivered time matters.")],
    "calcs": ["calc-ufr-ceiling.html", "calc-idwg-fluid.html"],
}

_E["10"] = {
    "navs": ["Recognize", "First response", "Record and review", "Utility failures"],
    "big": """
{{plain:Think of a lifeguard at a public pool. Most days nothing happens. When a swimmer goes under, the lifeguard does not stop to work out why. The lifeguard shouts for help and starts the task the team has practiced. Most dialysis sessions are uneventful, but trouble on dialysis can develop within minutes. In an emergency a technician has three jobs: recognize that something is wrong, call for help immediately, and then do the task you are given.}}
<p>The picture has a limit. A lifeguard often rescues alone, and you never do. You are not expected to diagnose the cause or to change the treatment. The nurse and the physician lead. What helps the patient most is how quickly you call and how exactly you carry out the task you are given.</p>
{{flow:Your first thirty seconds|See it::A patient who looks unwell, or says they suddenly feel unwell.|Call::Use the unit&rsquo;s emergency call. Say where you are and that you need help now.|Say what you saw::The symptoms, when they started, and whether the patient is connected.|Take a task::Bring equipment, guide the responders, or assist as directed.|Close the loop::Repeat the instruction, and report when it is done.}}
{{cards:Key terms for this module|Hypotension::Low blood pressure. It is the most common problem during dialysis.|Needle dislodgement::A needle slipping out of the access. Blood loss can be fast and hidden under a blanket.|Hemolysis::Red blood cells breaking apart, for example from overheated or wrongly mixed dialysate, or from chloramine.|Air embolism::Air entering the bloodstream. It is rare, and it is an emergency.|Closed-loop communication::Repeating each instruction, and confirming when it is completed.}}
""",
    "pre": {1: "{{fig:idh}}",
            2: "{{fig:code_roles}}",
            4: "{{fig:typhoon}}"},
    "post": {1: "{{fig:cramps}}{{stop:Chest pain, breathlessness, collapse, heavy bleeding, or a patient who cannot be woken: call for help first. Measurements and notes come after the call.}}",
             2: "{{fig:code_readiness}}{{fig:bls}}",
             4: "{{key:When water or power comes back, a screen that lights up again is not a release. Equipment and utilities return to service only when the designated leads clear them.}}"},
    "terms": [("Anaphylaxis", "A sudden, severe allergic reaction with difficulty breathing, swelling, or collapse."),
              ("Emergency cart", "The wheeled cart that holds the resuscitation equipment and medicines. Know where it is before every shift."),
              ("Debrief", "A short team review after an event: what happened, what went well, and what to change."),
              ("Contingency plan", "The unit&rsquo;s written plan for loss of power or water, fire, flood, or evacuation.")],
    "readings": [("code-blue-acls-dialysis-unit.html", "Cardiac arrest response in a dialysis unit, in full."),
                 ("hemodialysis-complications.html", "Why complications during dialysis happen."),
                 ("typhoon-disaster-preparedness-dialysis.html", "Typhoon and disaster planning for dialysis.")],
    "calcs": ["calc-dialysis-continuity-planner.html"],
}

_E["11"] = {
    "navs": ["Single use or reuse", "Traceable records", "Hold and reject", "Equipment quality"],
    "big": """
{{plain:Picture a household with twins that washes and reuses their feeding bottles. Reuse is safe only when each bottle is cleaned, rinsed free of soap, and handed back to the right child. Some dialysis units do the same with a dialyzer: they clean, test, and disinfect it so that the same patient can use it again. This is called reprocessing or reuse.}}
<p>The picture has a limit. A mix-up of feeding bottles between twins is a small matter. A mistake in reprocessing can give a patient someone else&rsquo;s dialyzer, a clotted dialyzer, or a dose of disinfectant. Reuse is safe only when every step is done and recorded. The rule that runs through this module: if you cannot prove it, do not use it.</p>
{{fig:reuse_steps}}
{{cards:Key terms for this module|Single use::A dialyzer that is used once and discarded.|Reprocessing::Cleaning, testing, and disinfecting a dialyzer for the same patient&rsquo;s next treatment.|Total cell volume::The fluid volume of the fiber bundle. It falls as fibers clot, so it shows whether the dialyzer still cleans well.|Germicide::The chemical that kills microbes inside the stored dialyzer.|Residual test::A test before use that proves the germicide has been rinsed out.|Traceability::Being able to follow one dialyzer through every step, by its label and its records.}}
""",
    "pre": {1: "{{fig:reuse_hero}}",
            4: "{{flow:From fault to return to service|Fault noticed::Record the exact message, or exactly what you saw.|Hold::Remove the equipment from use and label it clearly.|Repair::Done by authorized service staff.|Post-service checks::Documented tests showing that the fault is resolved.|Release::A designated person signs the equipment back into service.}}"},
    "post": {2: "{{fig:reuse_germicide}}",
             3: "{{stop:An unreadable label, a missing test result, or a name that does not match means the dialyzer is held and reported. A passed test never makes up for a failed identity check.}}",
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
{{plain:This last module adds nothing new. It is the road test after the driving lessons: the same rules, now in traffic. It asks you to use everything together, the way a real shift demands: several checks at once, an interruption, a problem that is not yours to solve, and a record that must be right.}}
<p>The comparison has a limit. A road test happens once, and a dialysis shift tests you every day. If you can verify, pause, report, and document under pressure, you are ready for supervised practice. Supervised practice is where that pattern becomes a habit.</p>
{{flow:The pattern behind every module|Verify::The patient, the order, the station, the machine, and the water.|Pause::Hold whatever depends on a check that failed.|Report::Tell the right person, with the facts and a clear request.|Confirm::Repeat the instruction back.|Record::What you saw, did, and were told, with the times.|Release::Only the designated person lifts a hold.}}
{{cards:Key terms for this module|Hold::A stop placed on a patient setup, a machine, or the water supply until a problem is cleared.|Release::Formal permission from the designated person to resume.|Near miss::A problem caught before it reached a patient. Reporting it helps the unit improve.|Plan-Do-Study-Act::A small test of a change: plan it, try it, study the result, and act on what you learned.|Competency::A skill you have been observed doing correctly and safely.}}
""",
    "pre": {3: "{{fig:pdsa}}"},
    "post": {3: "{{fig:fishbone}}",
             2: "{{key:Urgent patient symptoms go to the nurse first. Equipment and water problems go to the nurse and to the technical lead. If you are not sure which kind it is, tell the nurse.}}"},
    "terms": [("Simulation", "Practice on training equipment or a mannequin, where a mistake harms no one."),
              ("Logbook", "Your record of what you observed and practiced during placement, signed by the preceptor."),
              ("Blueprint", "A table that shows how many examination questions come from each topic.")],
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
     "The blood path and the dialysate path, operating the machine from switch-on to shutdown, priming step by step, machine disinfection, and what to do when a machine fails a check."),
    ("07", "water-treatment-concentrates-dialysate", "Water Treatment, Concentrates, and Dialysate", (6, 6, 16),
     "How tap water becomes dialysis water, which test checks what, how concentrates become dialysate, and how to respond to an out-of-range result."),
    ("08", "vascular-access-recognition-protection", "Vascular Access Recognition and Protection", (6, 6, 14),
     "Fistulas, grafts, and catheters; how to protect the access in everyday care; and the changes that must be reported at once."),
    ("09", "the-hemodialysis-session", "The Hemodialysis Session", (6, 8, 18),
     "One treatment from arrival to station turnover: what to verify before, what to watch during, a chairside guide to every machine alarm, and how to finish and hand over."),
    ("10", "complications-emergency-response", "Complications and Emergency Response", (6, 6, 16),
     "Recognizing trouble during dialysis, calling for help, working in an emergency team, and responding to water, power, and facility failures."),
    ("11", "dialyzer-reprocessing-equipment-quality", "Dialyzer Reprocessing and Equipment Quality", (4, 4, 12),
     "The life of a reprocessed dialyzer; manual, semi-automated, and automated reprocessing step by step; total cell volume and leak tests; germicide checks before use; and the records that make a dialyzer traceable."),
    ("12", "integrated-practice-competency-assessment", "Integrated Practice and Competency Assessment", (2, 4, 22),
     "Everything together: readiness checks, urgent reports, records and improvement, five practical stations, the logbook, and the examination blueprint."),
]

MODULES = [{"id": i, "slug": s, "title": t, "hours": h, "sub": sub, "src": True, "enrich": _E[i],
            "case_title": "A name that almost matched" if i == "01" else ""} for i, s, t, h, sub in _ROWS]

# Added practice lessons (practice_additions.py) and per-module deepening (deep_NN.py).
import importlib.util as _ilu
from pathlib import Path as _P
_sp = _ilu.spec_from_file_location("hd_practice_additions", _P(__file__).resolve().parent / "practice_additions.py")
_pm = _ilu.module_from_spec(_sp); _sp.loader.exec_module(_pm)
for _k, _v in _pm.ADD.items():
    _E[_k].update(_v)
for _f in sorted(_P(__file__).resolve().parent.glob("deep_*.py")):
    _k = _f.stem[-2:]
    _ds = _ilu.spec_from_file_location("hd_" + _f.stem, _f)
    _dm = _ilu.module_from_spec(_ds)
    try:
        _ds.loader.exec_module(_dm)
    except Exception:
        import os as _os
        if _os.environ.get("TC_LENIENT"):
            continue
        raise
    for _name, _val in _dm.ADD.items():
        _E[_k][_name] = list(_E[_k].get(_name, [])) + list(_val)
