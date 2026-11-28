# -*- coding: utf-8 -*-
"""Disaster Preparedness and Response: course definition in the POD/SW package schema.
Built from Dr. Rivero's blueprint v1.1 (DISASTER_PREPAREDNESS_BLUEPRINT.md, November 28, 2026, decisions in section 13).
Cross-track course in the Emergency Readiness section, beside the Dialysis Team Resuscitation Lab.
Every case, name, and identifier is fictional. Review status: DRAFT pending Dr. Rivero's clinical sign-off."""

HUB = "disaster-preparedness"
_HB = ("Illustrated clinical vignette, calm and prepared, Filipino dialysis team, modern Philippine hemodialysis unit, realistic "
       "equipment, no text and no legible names or numbers in image, dignity always (no injuries, no panic). ")

COURSE = {
    "title": "Disaster Preparedness and Response",
    "short": "Disaster Preparedness",
    "hub_slug": HUB,
    "label": "Disaster readiness for the whole dialysis unit",
    "tag": "Emergency Readiness",
    "icon": "🌀",
    "no_branch": True,
    "exam_stratify": True,
    "audience": ("Every member of the dialysis unit: hemodialysis, charge, head and safety nurses, physicians-on-duty, the Dialysis "
                 "Clinical Head and attending nephrologists, dialysis, water treatment, biomedical and reprocessing technicians, nurse "
                 "assistants and support staff, social workers, records officers, dietitians, unit managers and owners"),
    "audience_type": "Whole dialysis unit (clinical, technical and management staff)",
    "level": "College reading level; core modules for every role, with planning and drill modules for leaders",
    "review_date": "2026-11-28",
    "draw": 5,
    "mastery": "4 of 5",
    "exam_draw": 36,
    "keywords": ("dialysis disaster preparedness Philippines, typhoon dialysis unit plan, earthquake during hemodialysis, fire evacuation "
                 "dialysis unit, power failure hemodialysis, manual blood return, water failure dialysis, ashfall dialysis, early dialysis "
                 "before typhoon, emergency kidney diet, dialysis patient emergency card, tabletop exercise dialysis, call-down drill, "
                 "restart gates dialysis unit, DRRM-H dialysis"),
    "page_title": "Disaster Preparedness and Response for Dialysis Units",
    "desc": ("A free 12-module disaster course for Philippine dialysis units: why disasters harm dialysis patients twice, the unit plan "
             "and command, ready patients, typhoons and floods, earthquakes, fire and evacuation, power and water failure, heat, ashfall "
             "and outbreaks, keeping everyone dialyzed, reopening safely, and running drills, with interactive cases and drill tools."),
    "h1": "Disaster <em>Preparedness and Response</em>",
    "sub": ("Keep every patient safe when the warning comes, when the ground shakes and when the lights go out, and keep every patient "
            "dialyzed until the unit reopens. A cross-track course and drill program for the whole dialysis unit."),
    "disclaimer": ("DRAFT pending clinical sign-off by Dr. William Gregory Rivero. Educational course and drill resource for dialysis units. "
                   "It is not a hospital disaster plan, a licensing requirement, or a substitute for your unit&rsquo;s approved protocol, "
                   "the machine manufacturer&rsquo;s instructions, or instructions from PAGASA, PHIVOLCS, the Bureau of Fire Protection or "
                   "your local disaster office. Clinical decisions in a disaster (early dialysis, shortened sessions, priority, diet) belong "
                   "to the attending nephrologist."),
    "scope_note": ("DRAFT, pending clinical sign-off. This module is study material for dialysis teams. It explains the reasoning behind "
                   "disaster decisions; it is not a unit protocol or an order set. Early dialysis, shortened sessions, priority rosters and "
                   "emergency diets are decisions of the attending nephrologist and the Dialysis Clinical Head. Escalation follows your "
                   "unit protocol, and you always ask the attending nephrologist for guidance. Every case, name, and identifier is "
                   "fictional."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Every dialysis unit",
    "branch_blurb": ("A disaster course and drill program for the whole unit: typhoons and floods, earthquakes, fire, power and water "
                     "failure, heat and ashfall, keeping every patient dialyzed, and reopening safely."),
    "academy_meta": "12 modules &middot; 10 interactive cases &middot; tabletop simulator &middot; call-down timer &middot; evacuation sheet",
    "hero_alt": ("Before typhoon season in a bright dialysis unit: a nurse lifts supply boxes onto a high shelf, a technician checks a "
                 "generator panel through an open door, and the head nurse holds a clipboard call list."),
    "start_h2": "Disasters hurt dialysis patients twice",
    "start_html": """
<p>A dialysis patient depends on electricity, treated water, transport and trained staff, all at once, three times a week. A typhoon can take away all four in one night. The first harm is the event itself: a patient on a machine when the ground shakes, the power fails or smoke fills the corridor. The second harm comes in the days after, when sessions are missed while the body keeps adding water, salt and potassium.[[dp_sever2023]]</p>
<p>The second harm is the larger one, and it is the one a plan can change. After Hurricane Katrina, 44% of 386 New Orleans patients missed at least one session, and missing three or more was associated with hospitalization; patients who did not know their unit&rsquo;s emergency plan were among the more likely to miss three or more.[[dp_anderson2009]] Before Hurricane Sandy, dialysis moved ahead of schedule was associated with fewer emergency visits, admissions and deaths in the following month.[[dp_lurie2015]] Both studies are observational, from the United States, where disasters have been studied. The Philippine lesson is the same: a unit that has planned, drilled and told its patients what to do keeps more of them dialyzed.</p>
{{cards:What this course will help your unit do|Know your hazards and dependencies::Map what your unit runs on, which things fail together, and fix the single points of failure before the season.|Activate one plan, with one command::Triggers tied to PAGASA signals, PHIVOLCS alerts and utility notices; named roles; a call-down that works when networks fail.|Prepare every patient::An emergency card, a three-day emergency kidney diet, a medicine supply, two phone numbers, and the rule on the machine: stay connected and wait for staff.|Protect the patients connected right now::Earthquake, fire, power or water failure: the first minutes at the chair, the emergency take-off, and the census at the assembly point.|Keep everyone dialyzed::Find every patient within 24 hours, place them by medical priority, and use shortened sessions only under six conditions.|Reopen safely and learn::Five signed restart gates, reconciliation of who was dialyzed where, care for tired staff, and drills that change practice.}}
{{fig:dp00_act_learn_practice}}
<p>The course is cross-track. Eight role tracks already carry a disaster module, and this course is the shared core they point to: one unit plan, one drill program, one set of rules. Each module says which roles need it. The <a href="disaster-preparedness-practice.html">practice page</a> holds the tabletop simulator, the call-down drill timer and the printable evacuation sheet. Cardiac arrest at the chair belongs to the <a href="resuscitation-lab.html">Dialysis Team Resuscitation Lab</a>; this course links to it and never re-teaches it.</p>
<div class="alert alert-red"><div class="alert-icon">⛔</div><div class="alert-body"><h4>DRAFT: pending clinical sign-off</h4><p>This course has not yet been signed off by Dr. William Gregory Rivero. Your unit protocol, the attending nephrologist and your local disaster authorities decide every real event.</p></div></div>
""",
    "is_not": ("It is an original course written from published disaster and dialysis research, Philippine law and policy (Republic Act "
               "No. 10121, the Department of Health&rsquo;s DRRM-H policy, the Fire Code), and public guidance from PAGASA, PHIVOLCS and "
               "the Office of Civil Defense. It is not a hospital disaster plan, it does not replace the hospital plan a hospital-based "
               "unit works inside, and it states no drill frequency as a legal requirement unless the law states it. Drill frequencies "
               "in this course are Academy suggestions."),
    "pathways_tag": "Four parts",
    "pathways_h2": "Twelve modules in four parts",
    "pathways_nav": "Parts",
    "pathways_html": """
<p>The modules follow the life of a disaster: understand and plan, prepare the people, respond to each hazard, then keep everyone dialyzed, reopen and practice.</p>
{{cards:The four parts|Part 1 &middot; Understand and plan::Modules 1 to 3. Why disasters hurt dialysis patients twice, your unit&rsquo;s hazards and dependencies, and the unit plan with its command roles.|Part 2 &middot; Ready patients::Module 4. The emergency card, the three-day emergency kidney diet, medicines, contacts, and what to do on the machine.|Part 3 &middot; Respond::Modules 5 to 9. Typhoons and floods, earthquakes, fire and evacuation, power and water failure, and heat, ashfall and outbreaks.|Part 4 &middot; Continue, reopen, practice::Modules 10 to 12. Priority, placement and tracking; reopening through five signed gates; running drills that change practice.}}
<h3>Which modules for which role</h3>
<div class="table-wrap"><table>
<thead><tr><th>Role group</th><th>Modules (draft)</th></tr></thead>
<tbody>
<tr><td>Hemodialysis, charge and head nurses</td><td>All modules; Modules 6 to 8 hands-on; emergency take-off drill passed</td></tr>
<tr><td>Safety nurse (or head nurse)</td><td>All modules, plus the Module 12 facilitator capstone</td></tr>
<tr><td>Physician-on-duty, Dialysis Clinical Head, attending nephrologist</td><td>Modules 1, 3, 5, 8, 10, 11</td></tr>
<tr><td>Technicians (dialysis, water treatment, biomedical, reprocessing)</td><td>Modules 1, 2, 6, 7, 8, 11</td></tr>
<tr><td>Nurse assistants, support staff</td><td>Modules 1, 6, 7; the evacuation drill</td></tr>
<tr><td>Unit manager, unit owner</td><td>Modules 1, 2, 3, 10, 11, 12</td></tr>
<tr><td>Social worker, records officer, dietitian</td><td>Modules 1, 3, 4, 10</td></tr>
</tbody></table></div>
<p>The role paths are a draft Academy recommendation for the unit to adapt.</p>
""",
    "modules_h2": "Twelve modules in four parts",
    "modules_intro": ("Study in order the first time. Each module opens with a fictional Philippine scenario, teaches the reasoning, and "
                      "ends with an interactive case, a skills checklist and a self-assessment."),
    "syllabus_note": ("Each module plans about 1.5 hours: guided study, the interactive case and the self-assessment, about 18 hours in "
                      "all, plus the unit drills. These are educational planning hours, not a DOH, PSN or licensing requirement."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions drawn at random from a bank of 10; aim for 4 of 5 on two different sets. Every question explains the best answer and why the others fail. The end-of-course self-study check draws three questions from each module (36 in all); the proposed pass is 29. Ten modules carry an interactive case with a unit board (time, alert level, power, water, patients connected, staff and roads); every case has at least one choice that breaks a hard rule, so you can see why the rule exists.</p>
<p>The drills on the <a href="disaster-preparedness-practice.html">practice page</a> (tabletop simulator, call-down timer, evacuation sheet) are team exercises, not individual scores. A high written score never makes up for a safety-critical error in a drill: a connected patient left alone, blood returned after air or hemolysis, an evacuation drill run with patients on machines, or a reopening without a signed water release.</p>
""",
    "sources_html": """
<p>The evidence comes mostly from United States hurricanes, Japanese earthquakes and international reviews, because those events were studied. Findings about missed sessions, early dialysis and outcomes are observational and are worded &ldquo;associated with&rdquo;; single-unit reports &ldquo;suggest&rdquo;; drill effectiveness is supported by low-quality evidence. No module says that a preparedness step prevents death.[[dp_sever2023]][[dp_sandal2025]][[dp_hsu2004]]</p>
<p>Philippine sources come first for rules and warnings: Republic Act No. 10121,[[dp_ra10121]] the Department of Health&rsquo;s DRRM-H policy and its hospital safety policy,[[dp_doh2019]][[dp_doh2013]] the Fire Code&rsquo;s implementing rules,[[dp_ra9514]] PAGASA&rsquo;s tropical cyclone wind signals,[[dp_pagasa_tcws]] and the Office of Civil Defense&rsquo;s quarterly Nationwide Simultaneous Earthquake Drill.[[dp_ocd_nsed]] Where an Academy module already teaches a step (the restart gates, manual blood return, the safety nurse role), this course repeats that module&rsquo;s rule and links to it. Sources were checked on November 28, 2026.</p>
""",
    "trainers_intro": ("The unit&rsquo;s safety nurse (or the head nurse, where none is designated) can use this page as the facilitator kit for disaster drills. "),
    "trainer_h2": "Facilitator kit: running disaster drills in a dialysis unit",
    "trainer_audience": "Safety nurses, head nurses, unit managers, Dialysis Clinical Heads and unit educators who run disaster drills",
    "trainer_html": """
<p>The course supports in-unit practice. Use it to rehearse the parts that general disaster training never reaches: the patients on machines, the circuit, the water room, the call list and the receiving units.</p>
<h3>Who facilitates</h3>
<p><strong>The unit&rsquo;s safety nurse facilitates disaster preparedness and response</strong> (<a href="special-dialysis-nurse-roles-07-safety-and-emergency-preparedness.html">Special Dialysis Nurse Roles, Module 7</a>): the nurse designated to plan, check readiness and run drills. Three people stand behind that role. The <strong>unit manager</strong> owns the disaster plan, the drill schedule, the receiving-unit agreements and the budget. The <strong>Dialysis Clinical Head</strong> leads the clinical decisions in a tabletop exercise: early dialysis, who is placed first, and the emergency diet with the dietitian. The <strong>unit owner</strong> receives the findings and funds the fixes.</p>
<p>Where no safety nurse is designated (most units today), <strong>the head nurse facilitates</strong>, and naming a safety nurse within the year is recommended. During a real event the safety nurse does not command: the charge nurse and the physician direct the response, and licensed engineers and technicians handle the building, water and machines.</p>
<h3>The drill program</h3>
<div class="table-wrap"><table>
<thead><tr><th>Drill</th><th>Owns the schedule</th><th>Runs it</th><th>Takes part</th><th>Signs the record</th></tr></thead>
<tbody>
<tr><td>Patient call-down check, before typhoon season</td><td>Unit manager</td><td>Safety nurse (or head nurse)</td><td>Charge nurses, records officer, social worker</td><td>Unit manager</td></tr>
<tr><td>Disaster tabletop, before typhoon season</td><td>Unit manager</td><td>Safety nurse (or head nurse), with the Dialysis Clinical Head leading clinical decisions</td><td>Head nurse, charge nurses, technicians (water and power), biomedical technician, social worker, records officer</td><td>Unit manager; findings to the owner</td></tr>
<tr><td>Power-loss and blood-return-without-power drill, twice a year</td><td>Head nurse</td><td>Safety nurse (or head nurse) with the biomedical technician</td><td>Nurses and technicians on the shift, at an empty station</td><td>Head nurse</td></tr>
<tr><td>Earthquake drill, timed with the quarterly NSED where possible</td><td>Unit manager</td><td>Safety nurse (or head nurse)</td><td>Whole shift; patients take part only in the &ldquo;protect in place&rdquo; step if they agree</td><td>Unit manager</td></tr>
<tr><td>Evacuation and patient-accounting drill, yearly</td><td>Unit manager</td><td>Safety nurse (or head nurse), with the building or facilities officer</td><td>Whole shift, with no patients on machines</td><td>Unit manager; findings to the owner</td></tr>
<tr><td>Same-day debrief after a real disruption</td><td>Unit manager</td><td>Safety nurse (or head nurse) or Dialysis Clinical Head</td><td>Everyone involved</td><td>Unit manager; findings to the owner</td></tr>
</tbody></table></div>
<p>All frequencies are Academy suggestions. The quarterly NSED is a national campaign the unit may join.[[dp_ocd_nsed]] The Fire Code&rsquo;s implementing rules call for fire exit drills &ldquo;with sufficient frequency&rdquo; where drills are required;[[dp_ra9514]] this course does not state a numeric legal requirement.</p>
<h3>Rules for every drill</h3>
<ul>
<li><strong>No drill on a working floor without a named watcher</strong> whose only job is the patients still dialyzing. No evacuation drill with patients on machines.</li>
<li><strong>Every finding gets an owner and a date,</strong> the same as a finding from a real event.</li>
<li><strong>One-page after-action report:</strong> objectives met or not; what worked; what failed; actions with owner and date; when the team will rehearse again. The unit manager keeps disaster records; the Dialysis Clinical Head reviews them each quarter with the resuscitation records.</li>
<li><strong>Hospital-based units drill inside the hospital plan</strong> and its emergency preparedness committee, framed by the DOH DRRM-H policy and the Hospitals Safe from Disasters policy.[[dp_doh2019]][[dp_doh2013]] Freestanding units coordinate evacuation routes and warnings with the local disaster risk reduction and management office (LDRRMO) under Republic Act No. 10121.[[dp_ra10121]]</li>
</ul>
<h3>What the evidence says about drills</h3>
<p>A systematic review of hospital mass-casualty training found that drills help staff learn procedures and expose problems, but study quality was low and none tested tabletop exercises.[[dp_hsu2004]] In one Taiwanese hemodialysis unit, tabletop simulation, drills and audits raised staff fire-response knowledge and skill scores from about 58% to 100%; that was one before-and-after project, so it shows feasibility, not proof.[[dp_lin2021]] Drill because it finds the problems before the disaster does, not because a trial has proved it saves lives.</p>
<h3>The observed stations</h3>
<p>Each station is scored out of 10; pass is 8 with every <span class="tc-crit">Critical</span> criterion met. <strong>1 Protect in place:</strong> during a simulated earthquake at an empty station with a manikin, protects the head and access arm, does not disconnect during shaking, then checks lines, needles and machine. <strong>2 Emergency take-off:</strong> on a training circuit, applies the blood rule and clamps and disconnects in sequence. <strong>3 Blood return without power:</strong> with the biomedical technician, returns the circuit by hand crank while watching the venous line. <strong>4 Evacuation and census:</strong> moves manikins by mobility category to the assembly point and accounts for every name. <strong>5 Call-down and handoff</strong> (leaders): runs a timed call-down and writes a receiving-unit handoff.</p>
<p><strong>Critical errors (each one fails the station):</strong> a connected patient left alone; disconnection during shaking; blood returned after air, hemolysis or a severe reaction; a central catheter left unclamped; an evacuation drill run with patients on machines; a patient missing from the census without a report; a reopening step taken without a signed water release.</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments: 4 of 5 on two different sets for each module, with every missed question reviewed.</li>
<li>Every interactive case completed at least once, with every harmful choice repeated until the safe choice is clear.</li>
<li>End-of-course self-study check: 29 of 36 or higher.</li>
<li>The observed stations for your role passed at 8 of 10 with no critical error.</li>
<li>Participation in at least one unit drill (tabletop, call-down, power-loss, earthquake or evacuation), recorded by the safety nurse or head nurse.</li>
</ul>
<p>Completion is an Academy learning record. It is not a DOH, PSN, BFP or Office of Civil Defense certificate, and it is not CPD credit.</p>
""",
    "related": [("typhoon-disaster-preparedness-dialysis.html", "The patient-facing guide to typhoon and disaster preparation for people on dialysis."),
                ("climate-extremes-kidney-care.html", "Climate extremes and kidney care, with the printable Kidney Emergency Card."),
                ("calc-dialysis-continuity-planner.html", "The dialysis continuity planner for capacity and placement during disruptions.")],
}

P1, P2, P3, P4 = ("Part 1 &middot; Understand and plan", "Part 2 &middot; Ready patients", "Part 3 &middot; Respond",
                  "Part 4 &middot; Continue, reopen, practice")

_ROWS = [
    ("01", "why-disasters-hurt-twice", "Why Disasters Hurt Dialysis Patients Twice", P1,
     "The causal chain from warning to restart, what the studies show and their limits, and the hazards a Philippine unit plans for.",
     "A freestanding dialysis clinic on a flooded street, its shutter half down; an older man and his daughter on a dry step across the street.", 0),
    ("02", "hazards-and-dependencies", "Know Your Unit's Hazards and Dependencies", P1,
     "A hazard assessment for a dialysis unit, the dependency map (power, water, staff, supplies, transport, records, communications), and the single points of failure.",
     "A safety nurse and a water treatment technician tracing pipes and cables behind a reverse osmosis unit with a clipboard.", 0),
    ("03", "unit-plan-and-command", "The Unit Plan and Who Commands", P1,
     "A one-page activation plan, simple incident command for a dialysis unit, triggers, communications when networks fail, and receiving-unit agreements.",
     "A small dialysis team around a one-page plan, a phone tree and a two-way radio.", 0),
    ("04", "ready-patients", "Ready Patients: Card, Diet, Medicines, Contacts", P2,
     "The emergency card, the three-day emergency kidney diet, medicines, contacts, and what to do on the machine: stay connected and wait for staff.",
     "An older man on hemodialysis and his daughter packing a go-bag at home.", 0),
    ("05", "typhoons-and-floods", "Typhoons and Floods", P3,
     "Before the season, when the signal is raised, during and after; early dialysis with the nephrologist; staff transport; flood water and leptospirosis exposure.",
     "A dialysis unit at dusk under a typhoon sky, staff moving supplies to high shelves.", 0),
    ("06", "earthquake-on-the-machine", "Earthquake on the Machine", P3,
     "Protect in place, the checks after the shaking, when to take patients off, the emergency take-off, and joining the quarterly earthquake drill.",
     "A nurse shielding a connected patient's head and access arm during shaking, the machine wheels locked.", 1),
    ("07", "fire-and-evacuation", "Fire and Evacuation", P3,
     "RACE and the extinguisher, oxygen and smoke, the emergency take-off for evacuation, mobility categories, the route, and the census at the assembly point.",
     "A census nurse checking names at an assembly point while patients arrive in wheelchairs and on a stretcher.", 1),
    ("08", "power-water-supplies", "Power, Water and Supplies", P3,
     "The first ten minutes of a power failure, blood return without power, generator and battery checks, water failure and contamination, and supply buffers.",
     "A biomedical technician checking a generator's fuel gauge at night, the unit glowing with emergency lights behind him.", 1),
    ("09", "heat-ashfall-outbreaks", "Heat, Ashfall and Outbreaks", P3,
     "Heat-index days and the trip to the unit, volcanic ashfall and the water and air intakes, and an infectious outbreak treated as a disaster.",
     "Two staff in masks closing the windows of a dialysis unit while fine gray ash coats the cars outside.", 0),
    ("10", "keeping-everyone-dialyzed", "Keeping Everyone Dialyzed: Priority, Placement, Tracking", P4,
     "Finding every patient within 24 hours, the medical priority roster, shortened sessions under six conditions, and placement at receiving units with a handoff.",
     "A nurse on the phone in front of a whiteboard tracker while a physician reviews a laboratory sheet.", 0),
    ("11", "reopening-and-recovery", "Reopening Safely and Recovering", P4,
     "The five signed restart gates, reconciliation of who was dialyzed where, staff fatigue and distress, and patients' distress after disasters.",
     "A head nurse and a water treatment technician signing a checklist at the water room door of a clean unit after a flood.", 0),
    ("12", "running-drills", "Running Drills That Change Practice", P4,
     "Exercise types, objectives and injects, the facilitator's script, the watcher rule, the hot wash, and the after-action report.",
     "A dialysis team leaning over a printed floor plan with tokens while a facilitator holds inject cards.", 0),
]
MODULES = []
for _id, _slug, _title, _part, _sub, _brief, _pl in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part, "hours": (1, 1 if _pl else 0.5, 0),
                    "card_img": f"{HUB}-{_id}-card.webp", "hero_brief": _HB + _brief})
