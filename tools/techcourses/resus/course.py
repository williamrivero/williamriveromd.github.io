# -*- coding: utf-8 -*-
"""Dialysis Team Resuscitation Lab (ACLS, BLS & PALS): course definition in the POD/SW package schema.
Built from Dr. Rivero's Resuscitation Lab blueprint and the Emergency Readiness handoff, merged as Blueprint v2
(RESUSCITATION_LAB_BLUEPRINT_v2.md, November 28, 2026). Cross-track course in the Emergency Readiness section.
Every case, name, and identifier is fictional. Review status: DRAFT pending Dr. Rivero's clinical sign-off."""

HUB = "resuscitation-lab"
_HB = ("Illustrated clinical vignette, cinematic but calm, Filipino dialysis team, modern Philippine hemodialysis unit, "
       "realistic equipment (recliner dialysis chairs, hemodialysis machines, crash cart, defibrillator), no text and no legible "
       "names or numbers in image. ")

COURSE = {
    "title": "Dialysis Team Resuscitation Lab",
    "short": "Resuscitation Lab",
    "hub_slug": HUB,
    "label": "Team resuscitation practice for dialysis units",
    "tag": "Emergency Readiness",
    "icon": "⚡",
    "no_branch": True,
    "exam_stratify": True,
    "audience": ("Every member of the dialysis shift team: hemodialysis nurses, charge and head nurses, physicians-on-duty, attending "
                 "nephrologists, dialysis and biomedical technicians, nurse assistants and support staff &middot; pediatric dialysis teams "
                 "for Part 4"),
    "audience_type": "Dialysis shift teams (nurses, physicians, technicians, assistants)",
    "level": "College reading level; BLS-aligned core for every role, ALS- and PALS-aligned modules for licensed clinicians",
    "review_date": "2026-11-28",
    "draw": 5,
    "mastery": "4 of 5",
    "exam_draw": 39,
    "keywords": ("dialysis unit cardiac arrest training, ACLS review dialysis, BLS dialysis chair, PALS pediatric dialysis, hemodialysis "
                 "code blue drill, megacode dialysis, cardiac arrest during hemodialysis, hyperkalemic cardiac arrest, algorithm recognition, "
                 "rhythm recognition practice, AHA 2025 guidelines review, ERC 2025 hemodialysis, mock code dialysis Philippines"),
    "page_title": "Dialysis Team Resuscitation Lab: ACLS, BLS & PALS",
    "desc": ("A free 13-module team resuscitation reviewer for Philippine dialysis units: the basic algorithms, algorithm recognition, "
             "BLS at the chair, adult arrest and peri-arrest rhythms, arrest on the machine, hyperkalemia, pediatric resuscitation, "
             "ROSC and transfer, and interactive megacode drills."),
    "h1": "Dialysis Team <em>Resuscitation Lab</em>",
    "sub": ("Practice the first minutes. Coordinate every role. Improve with every drill. A BLS-, ALS- and PALS-aligned review for the "
            "whole dialysis team, built around the patient who collapses while connected to a machine."),
    "disclaimer": ("DRAFT pending clinical sign-off by Dr. William Gregory Rivero. Educational reviewer and practice resource for dialysis "
                   "teams. It is not an American Heart Association (AHA) course, it is not BLS, ACLS or PALS certification, and online "
                   "completion does not establish hands-on competence. Staff certify through an authorized training center. Your unit&rsquo;s "
                   "approved protocol, crash-cart stock and machine manufacturer&rsquo;s instructions govern every real event."),
    "scope_note": ("DRAFT, pending clinical sign-off. This module is study material for dialysis teams. It explains the reasoning behind "
                   "resuscitation decisions; it is not a unit protocol, an order set, or certification. Doses and energies are quoted from the "
                   "2025 American Heart Association (AHA) guidelines and the European Resuscitation Council (ERC) where named, so you can "
                   "recognize them; give medicines only within your license and your unit&rsquo;s approved protocol. Escalation always "
                   "follows your unit protocol, and you always ask the attending nephrologist for guidance. Every case, name, and identifier "
                   "is fictional."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Every dialysis shift team",
    "branch_blurb": ("A team reviewer and practice lab for the first minutes of an emergency on the dialysis floor: algorithms, recognition, "
                     "arrest on the machine, hyperkalemia, children, and megacode drills."),
    "academy_meta": "13 modules &middot; 17 interactive megacodes &middot; recognition lab &middot; facilitator kit &middot; five-tool toolkit",
    "hero_alt": ("A Filipino dialysis team resuscitating a man in a flattened dialysis recliner: one nurse compressing, one ventilating with "
                 "a bag-valve-mask, a nurse at the hemodialysis machine, and a physician watching the defibrillator screen."),
    "start_h2": "The arrest that happens on a machine",
    "start_html": """
<p>Cardiac arrest is the most feared event in a dialysis unit, and it is not rare. Dialysis clinics see sudden arrest often enough that resuscitation training for every staff member and a defibrillator on site are standard expectations abroad.[[pun2019]] When it happens, the patient is usually already in a chair, already monitored, already surrounded by trained people, and connected to an extracorporeal circuit that holds a few hundred milliliters of their blood. Those facts help and complicate at the same time.</p>
<p>A large registry study from the United States followed 398 arrests inside outpatient dialysis clinics. Two in three began with a rhythm that a shock cannot fix. Staff started CPR in 81.4% of events, and staff-started CPR was associated with about three times the odds of leaving hospital alive with good brain function. The study was observational, so it shows an association, not proof; but it also shows that in about one event in five, nobody started compressions before the ambulance came.[[pun2019]] This course exists to close that gap.</p>
{{cards:What this course will help your team do|Recognize the right algorithm::Tell arrest from respiratory arrest from a patient who is getting worse with a pulse, in seconds, and switch when the patient changes.|Start high-quality CPR at the chair::Flatten the recliner, compress at the right rate and depth, and keep pauses under 10 seconds.|Run the adult algorithms::Shockable and nonshockable arrest, bradycardia and tachycardia with a pulse, and the reversible causes that dominate in dialysis.|Manage the machine without delaying CPR::Stop fluid removal, decide whether the blood goes back, keep the access safe, and defibrillate safely.|Treat potassium as a dialysis team::Separate hyperkalemia with a pulse from hyperkalemic arrest, and know where the guidelines differ.|Practice as the real shift::Run megacodes with your actual staffing, debrief in five questions, and fix the system, not just the person.}}
<p>The course is cross-track. A nurse assistant needs the BLS modules and the circuit basics; a physician-on-duty needs everything. Each module says who it is for. Part 4 (children) is essential for pediatric dialysis teams and recommended for everyone. The <a href="resuscitation-lab-practice.html">Practice Lab</a> holds the algorithm recognition trainer, the timed megacodes, and the facilitator recorder; the <a href="emergency-cards.html">Emergency Quick Cards</a> are what you open during a real event.</p>
<div class="alert alert-red"><div class="alert-icon">⛔</div><div class="alert-body"><h4>DRAFT: pending clinical sign-off</h4><p>This course has not yet been signed off by Dr. William Gregory Rivero. It is not an AHA course and gives no certification. Your unit protocol decides every real event.</p></div></div>
""",
    "is_not": ("It is an original reviewer written from the 2025 AHA and AHA/American Academy of Pediatrics (AAP) guidelines, the 2025 "
               "European Resuscitation Council (ERC) special-circumstances guideline, kidney guidance, and peer-reviewed research. It is not "
               "the AHA BLS, ACLS or PALS course, it does not reproduce their manuals or algorithm charts, and it gives no certification or "
               "CPD units. Philippine rules require current BLS for dialysis nurses and current ACLS for the physician-on-duty and at least "
               "one nurse per shift;[[doh2012]][[psn2024]] those certificates come only from an authorized training center."),
    "pathways_tag": "Five parts",
    "pathways_h2": "Thirteen modules in five parts",
    "pathways_nav": "Parts",
    "pathways_html": """
<p>The modules follow the order of a real event: be ready, recognize which algorithm you are in, start BLS, run the adult algorithms, manage the dialysis-specific problems, adapt for children, and finish well after the pulse returns.</p>
{{cards:The five parts|Part 1 &middot; Readiness and recognition::Modules 1 to 3. Readiness before the collapse, how resuscitation algorithms think, and recognizing the right algorithm.|Part 2 &middot; Adult BLS and ALS::Modules 4 to 6. BLS at the dialysis chair, adult cardiac arrest, and bradycardia and tachycardia with a pulse.|Part 3 &middot; The dialysis difference::Modules 7 to 9. Arrest in the dialysis chair (the core module), hyperkalemia with a pulse and in arrest, and circuit emergencies that become resuscitations.|Part 4 &middot; Children::Modules 10 and 11. Pediatric BLS and the child who is getting worse; pediatric arrest and rhythms during dialysis.|Part 5 &middot; After the first minutes::Modules 12 and 13. Return of spontaneous circulation (ROSC), transfer and handover; team, code status, debriefing and practice.}}
<h3>Which modules for which role</h3>
<div class="table-wrap"><table>
<thead><tr><th>Role</th><th>Core path</th><th>Readiness level (draft)</th></tr></thead>
<tbody>
<tr><td>Nurse assistant, support staff, dietitian, social worker, OT/PT, records officer</td><td>Modules 1, 2, 3, 4, 7 (first two sections), 13</td><td>BLS</td></tr>
<tr><td>Dialysis, water treatment, biomedical and reprocessing technicians</td><td>Modules 1 to 4, 7, 9, 13</td><td>BLS</td></tr>
<tr><td>Hemodialysis, charge and head nurses; PD and transplant nurses</td><td>All modules; Part 4 recommended</td><td>ALS</td></tr>
<tr><td>Physician-on-duty, attending nephrologist, clinical head, trainees, vascular surgeon</td><td>All modules</td><td>ALS</td></tr>
<tr><td>Pediatric dialysis nurse, attending pediatric nephrologist</td><td>All modules; Part 4 essential</td><td>PALS</td></tr>
</tbody></table></div>
<p>The readiness levels are a draft Academy recommendation. Only two are verified Philippine rules: current BLS for dialysis nurses, and current ACLS for the physician-on-duty and at least one nurse on every shift.[[doh2012]][[psn2024]]</p>
""",
    "modules_h2": "Thirteen modules in five parts",
    "modules_intro": ("Study in order the first time. Each module opens with a timed case, teaches the algorithm with its reasons, and ends "
                      "with an interactive megacode you can run alone or with your team."),
    "syllabus_note": ("Each module plans 45 minutes of guided study, 30 minutes of interactive case and self-assessment, and a 15-minute team "
                      "drill: about 20 hours in all, plus the quarterly integrated megacode. These are educational planning hours, not a DOH, "
                      "PSN or certification requirement."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions drawn at random from a bank of 10; aim for 4 of 5 on two different sets. Every question explains the best answer and why the others fail. The end-of-course self-study check draws three questions from each module (39 in all); the proposed pass is 32. The observed assessment on the trainer page has five stations, each passed at 8 of 10 with every critical criterion met. A high written score never makes up for a safety-critical error: compressions not started, a shock delivered while someone touches the patient, contaminated blood returned, or an adult dose given to a child.</p>
<p>Separately, the <a href="resuscitation-lab-practice.html">Practice Lab</a> scores algorithm recognition and timed megacodes on your device only. Simulation success is an educational result, not a prediction of patient survival.</p>
""",
    "sources_html": """
<p>Adult content follows the 2025 AHA guidelines for adult basic life support,[[aha2025_bls]] adult advanced life support,[[aha2025_als]] special circumstances,[[aha2025_special]] post-cardiac arrest care,[[aha2025_post]] systems of care,[[aha2025_systems]] ethics,[[aha2025_ethics]] and resuscitation education.[[aha2025_education]] Pediatric content follows the 2025 AHA and American Academy of Pediatrics guidelines for pediatric basic and advanced life support.[[aha2025_pbls]][[aha2025_pals]] Dialysis-specific steps follow the ERC 2025 special-circumstances guideline, which has a section on cardiac arrest during hemodialysis that the AHA chapter does not,[[erc2025_special]] and the UK Kidney Association hyperkalemia guideline.[[an06_1]]</p>
<p>Where the AHA and the ERC disagree, most importantly on drug treatment of hyperkalemic cardiac arrest, the modules show both positions with their grades and leave the choice to your unit protocol. AHA grades are quoted as Class of Recommendation (COR) and Level of Evidence (LOE); they are never translated into another system. Research findings name the design and size, and observational findings say &ldquo;associated with.&rdquo; Sources were checked on November 28, 2026.</p>
""",
    "trainers_intro": ("A charge nurse, head nurse, physician-on-duty or clinical head can use this page as the facilitator kit for unit drills. "),
    "trainer_h2": "Facilitator kit: running resuscitation drills on a working dialysis floor",
    "trainer_audience": "Head and charge nurses, physicians-on-duty, dialysis clinical heads, unit educators, and certified BLS/ACLS instructors who run in-unit drills",
    "trainer_html": """
<p>The course supports in-unit practice; it does not replace an authorized BLS, ACLS or PALS course. Use it to keep certified skills alive between courses and to rehearse the parts no course teaches: the machine, the circuit, the access, and the other patients still dialyzing.</p>
{{flow:Proposed practice cadence (an Academy teaching choice, not an evidence-proven schedule)|Onboarding::Modules 1 to 4 and 7, a crash-cart and defibrillator orientation, an observed BLS skills check, and one team scenario.|Weekly::A five-minute skill refresher at shift handover: one recognition round, one compression check, or one cart check.|Monthly::A short team drill (one interactive case run on the shared display) with a five-question debrief.|Quarterly::An integrated megacode with role rotation, the facilitator recorder running, and a written system action list.|After any real event or equipment change::A targeted rehearsal of the step that went wrong, or of the new device.}}
<p>Spaced practice is supported: a 2026 systematic review of 15 comparative studies found spaced simulation training generally as effective as a single block, with some advantage for skill retention, and no study of patient outcomes.[[patocka2026]] Rapid cycle deliberate practice, where the facilitator stops, corrects and restarts, shortened simulated time to defibrillation and epinephrine in a 2024 review of nine studies, at very low certainty.[[abelairas2024]] Neither proves a survival benefit, and neither defines the best interval for a dialysis unit.</p>
<h3>Who runs each drill</h3>
<p>A drill with no named owner does not happen. The table is the Academy&rsquo;s suggested division of work; your unit may assign it differently, but every row needs a name, and a deputy for leave and night shifts.</p>
<div class="table-wrap"><table>
<thead><tr><th>Drill</th><th>Owns the schedule</th><th>Runs it (facilitator)</th><th>Takes part</th><th>Signs the record</th></tr></thead>
<tbody>
<tr><td>Weekly five-minute refresher at handover</td><td>Head nurse</td><td>Charge nurse on the shift</td><td>Everyone on that shift</td><td>Charge nurse</td></tr>
<tr><td>Monthly megacode (one interactive case run as a team, with the facilitator recorder)</td><td>Head nurse</td><td>Charge nurse or physician-on-duty with current ACLS (PALS for a pediatric case)</td><td>The shift team in rotating roles, plus a named watcher for the real patients</td><td>Head nurse</td></tr>
<tr><td>Quarterly integrated megacode</td><td>Dialysis Clinical Head</td><td>Unit educator or a certified BLS/ACLS instructor</td><td>Nurses, technicians, nursing assistants and the physician-on-duty</td><td>Dialysis Clinical Head</td></tr>
<tr><td>Onboarding scenario for a new staff member</td><td>Head nurse</td><td>Preceptor or unit educator</td><td>The new staff member with a small team</td><td>Head nurse</td></tr>
<tr><td>Same-day debrief after a real resuscitation</td><td>Charge nurse</td><td>Charge nurse or physician-on-duty</td><td>Everyone involved</td><td>Head nurse; system findings to the Dialysis Clinical Head</td></tr>
</tbody></table></div>
<p><strong>The facilitator does not play a role.</strong> The person running the drill watches, keeps the scenario moving and leads the debrief. In a small unit where that is impossible, record that the facilitator also took a role. A first-time facilitator runs one drill with an experienced facilitator observing (Module 13 skills checklist).</p>
<p><strong>Two rules for every drill.</strong> No drill on a working floor without a named watcher whose only job is the patients still dialyzing. Every system problem the drill finds gets an owner and a date, the same as a problem found in a real event.</p>
<p><strong>The practice record.</strong> For each drill, write the date, the scenario, who took which role, the one or two learning goals and whether they were met, the timeline from the recorder, and each action with its owner and date. The head nurse keeps the records; the Dialysis Clinical Head reviews them each quarter, with any real events.</p>
<h3>Before every drill</h3>
<ul>
<li><strong>Protect the real patients.</strong> Drill at a station that is empty, during a low-census period, with a named nurse who does not join the drill and watches every connected patient.</li>
<li><strong>Use real equipment, safely.</strong> The unit&rsquo;s own cart, defibrillator in training mode or a trainer device, a manikin in a recliner, a disconnected training circuit. Never use a live machine connected to water or power in a way that could harm staff.</li>
<li><strong>Assign roles from the real roster.</strong> Leader, compressor 1, compressor 2, airway, defibrillator and drugs, circuit nurse, recorder and timer, watcher, runner. Small teams combine roles; the role cards say which combine safely.</li>
<li><strong>Agree the learning goal.</strong> One or two targets per drill, for example &ldquo;first compression within 30 seconds of recognition&rdquo; or &ldquo;circuit decision announced within 2 minutes.&rdquo; These are local educational targets, not validated standards.</li>
</ul>
<h3>The five-question debrief</h3>
<p>What happened? What helped? What delayed care? What will change? Who owns that change, and when will the team rehearse again? Keep it short, keep it about the system, and write the action on the practice record. A structured debrief after simulation is associated with better learning outcomes than no debrief.[[cheng2014]]</p>
<h3>The five observed stations</h3>
<p>Each station is scored out of 10; pass is 8 with every <span class="tc-crit">Critical</span> criterion met. <strong>1 BLS at the chair:</strong> recognizes arrest, calls for help, flattens the recliner, starts compressions within the local target, applies pads, minimizes pauses. <strong>2 Arrest on the machine:</strong> the circuit nurse stops fluid removal and the blood pump, makes and announces the blood decision, keeps the access secured and clamped between uses, and never delays compressions or a shock. <strong>3 Adult megacode:</strong> leads a shockable and a nonshockable arrest with correct epinephrine timing and closed-loop orders. <strong>4 Peri-arrest rhythm:</strong> judges stability before treatment and chooses the correct pathway for a slow and a fast rhythm. <strong>5 Pediatric scenario</strong> (pediatric teams): calculates and double-checks weight-based dose, volume and energy aloud.</p>
<p><strong>Critical errors (each one fails the station):</strong> compressions not started; a shock delivered while anyone touches the patient, lines or wet chair; blood returned after air, hemolysis or a severe reaction; an access left open or unclamped; an adult dose or concentration given to a child; dialysis stopped in a stable hyperkalemic patient without the attending nephrologist.</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments: 4 of 5 on two different sets for each module, with every missed question reviewed.</li>
<li>Every interactive case completed at least once, with every safety-critical choice repeated until correct.</li>
<li>End-of-course self-study check: 32 of 39 or higher.</li>
<li>The observed stations for your role passed at 8 of 10 with no critical error.</li>
<li>A current BLS card (and ACLS or PALS where your role needs it) from an authorized training center, recorded by your head nurse.</li>
</ul>
<p>Completion is an Academy learning record. It is not BLS, ACLS or PALS certification, a CPD credit, or DOH or PSN recognition.</p>
""",
    "related": [("calc-resuscitation-lab-toolkit.html", "Five tools: CPR interruption analyzer, megacode timeline, pediatric dose-and-volume trainer, oxygen cylinder planner, drill rotation."),
                ("code-blue-acls-dialysis-unit.html", "The patient- and clinician-facing guide to code blue in a dialysis unit."),
                ("potassium-hyperkalemia-ckd.html", "The guide to potassium and hyperkalemia in kidney disease.")],
}

P1, P2, P3, P4, P5 = ("Part 1 &middot; Readiness and recognition", "Part 2 &middot; Adult BLS and ALS", "Part 3 &middot; The dialysis difference",
                      "Part 4 &middot; Children", "Part 5 &middot; After the first minutes")

_ROWS = [
    ("01", "readiness-before-collapse", "Ready Before the Collapse", P1,
     "Why dialysis units see arrests, the single chain of survival, the morning defibrillator and cart check, and the realities of freestanding units and ambulance transfer.",
     "A charge nurse and a technician checking a defibrillator and crash cart at dawn in an empty dialysis unit, chairs still covered.", 1),
    ("02", "algorithm-foundations", "How Resuscitation Algorithms Think", P1,
     "Triggers, the five decision questions, branches and why they matter, parallel team tasks, reassessment, and transitions between algorithms.",
     "A small team gathered at a whiteboard beside a dialysis chair while a physician sketches a branching decision path with arrows.", 0),
    ("03", "algorithm-recognition", "Recognizing the Right Algorithm", P1,
     "Arrest versus respiratory arrest versus deterioration with a pulse, shockable or not, stable or not, pulse or no pulse, and the potassium electrocardiogram (ECG).",
     "A nurse with two fingers on the neck of a pale man in a dialysis chair while looking at the bedside monitor showing a rhythm strip.", 0),
    ("04", "bls-at-the-chair", "BLS at the Dialysis Chair", P2,
     "Flattening the recliner, compressions that work, the defibrillator at the chair, bag-mask ventilation by two rescuers, and choking.",
     "A nurse giving chest compressions to a man in a fully flattened dialysis recliner while a second nurse seals a bag-valve-mask.", 1),
    ("05", "adult-cardiac-arrest", "Adult Cardiac Arrest: Shockable and Nonshockable", P2,
     "Shock-first logic for ventricular fibrillation (VF) and pulseless ventricular tachycardia (VT), epinephrine timing, antiarrhythmics, capnography, and the reversible causes that dominate in dialysis.",
     "A physician holding defibrillator paddles away while the team steps back from a flattened dialysis chair, all hands raised.", 1),
    ("06", "peri-arrest-rhythms", "Bradycardia and Tachycardia With a Pulse", P2,
     "Stability first, atropine and pacing, the bradycardia, renal failure, atrioventricular nodal blockade, shock and hyperkalemia (BRASH) syndrome, adenosine and its cautions, synchronized cardioversion, and when a rhythm becomes an arrest.",
     "A physician-on-duty reading a monitor with a fast rhythm while a nurse prepares synchronized cardioversion pads on a conscious patient.", 1),
    ("07", "arrest-in-the-dialysis-chair", "Arrest in the Dialysis Chair: Machine, Circuit and Access", P3,
     "The circuit nurse role, stopping fluid removal, whether the blood goes back, defibrillating near a machine, and using the access safely.",
     "A circuit nurse clamping blood lines at a hemodialysis machine while colleagues compress the patient in the flattened chair beside it.", 1),
    ("08", "hyperkalemia-with-pulse-and-in-arrest", "Hyperkalemia: With a Pulse and in Arrest", P3,
     "Membrane physiology, the potassium ECG and its blind spots, protect-shift-remove, where AHA and ERC disagree, and dialysis after the pulse returns.",
     "A physician comparing a 12-lead ECG with peaked T waves to a laboratory slip while a nurse keeps the patient connected and dialyzing.", 1),
    ("09", "circuit-emergencies", "Circuit Emergencies That Become Resuscitations", P3,
     "Needle dislodgement and hemorrhage, hemolysis, severe dialyzer reaction and anaphylaxis, hypoglycemia, and opioid-associated emergencies.",
     "A nurse pressing gauze on a forearm fistula site after a needle dislodgement, blood on the blanket, a second nurse checking the pulse.", 1),
    ("10", "pediatric-bls-and-deterioration", "Pediatric BLS and the Child Who Is Getting Worse", P4,
     "Infant and child definitions, the 2025 infant compression technique, respiratory failure first, and slow heart rate with poor perfusion.",
     "A pediatric dialysis nurse supporting the airway of a drowsy school-age child in a small dialysis bed while a colleague brings a pediatric bag-mask.", 1),
    ("11", "pediatric-arrest-and-dialysis", "Pediatric Arrest and Rhythms During Dialysis", P4,
     "Weight-based doses, volumes and energies said aloud, concentration traps, extracorporeal volume, and the circuit and access in a child.",
     "Two pediatric nurses double-checking a syringe label against a weight-based dose card beside a child on a small dialysis bed.", 1),
    ("12", "rosc-and-transfer", "Pulse Restored: ROSC, Transfer and Handover", P5,
     "Confirming ROSC, the first ten minutes after the pulse returns, what a freestanding unit can do, and a handover the ambulance can use.",
     "A nurse handing over a written summary to ambulance staff beside a stretcher while a monitor shows a regular rhythm.", 0),
    ("13", "team-code-status-and-debrief", "Team, Code Status, Debrief and Practice", P5,
     "Roles and closed-loop orders, leadership handover, code status and families, the five-question debrief, performance reports, and drill cadence.",
     "A dialysis team in a short standing debrief after a drill around a manikin in a recliner, the facilitator holding a clipboard.", 0),
]
MODULES = []
for _id, _slug, _title, _part, _sub, _brief, _pl in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part, "hours": (1, 1, _pl),
                    "card_img": f"{HUB}-{_id}-card.webp", "hero_brief": _HB + _brief})
