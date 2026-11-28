# -*- coding: utf-8 -*-
"""Disaster Preparedness and Response, Module 07: Fire and Evacuation."""

MODULE = {
    "image_alt": "A census nurse checking names at an assembly point while colleagues bring patients in wheelchairs and on a stretcher.",
    "objectives": [
        "Use RACE (rescue, alarm, contain, extinguish or evacuate) as a teaching aid for the first actions in a fire.",
        "Use a fire extinguisher with PASS, and know when not to fight a fire.",
        "Manage oxygen and smoke in a dialysis unit.",
        "Evacuate patients by mobility category, after an emergency take-off by staff with the blood rule.",
        "Account for every patient at the assembly point, with a named census nurse.",
    ],
    "big": """
{{plain:Evacuating a dialysis unit is like emptying a full jeepney through one door while several passengers are still tied to their seats. Somebody has to untie each one safely, somebody has to show the way, and somebody at the stop has to count heads before the jeepney drives off.}}
<p>The picture has a limit: in a fire, smoke and heat set the clock, and the people &ldquo;tied to their seats&rdquo; are connected to circuits holding their own blood. That is why a fire response in a dialysis unit has two parts that must happen together: the general fire actions every building uses, and the dialysis-specific take-off and census that no general course teaches.</p>
<p>In one Taiwanese hemodialysis unit, a project of tabletop simulation, drills and audits raised staff fire-response knowledge and skill scores from about 58% to 100%. That was one before-and-after project, so it shows that a unit can learn this, not proof of better outcomes.[[dp_lin2021]]</p>
{{cards:Key terms for this module|RACE::Rescue, alarm, contain, extinguish or evacuate: a memory aid for the first actions in a fire.|PASS::Pull, aim, squeeze, sweep: a memory aid for using an extinguisher.|Mobility category::How a patient leaves the building (walks alone, walks with help, wheelchair, stretcher), set before the event.|Assembly point::The agreed place outside where everyone gathers and is counted.|Census nurse::The named nurse who holds the patient list and accounts for every patient.|Horizontal evacuation::Moving people away from the fire to a safer area on the same floor, behind a closed fire door.}}
""",
    "case": {"title": "Smoke from the reprocessing room", "html": """
<p>At 2:10 p.m., a nurse smells smoke and sees it coming from under the door of the dialyzer reprocessing room at the end of a ground-floor unit in Cebu City. Twelve patients are connected. Three use wheelchairs; one, recovering from a stroke, came on a stretcher. The fire alarm has not sounded.</p>
<p>A technician runs toward the reprocessing room with an extinguisher. Two nurses start disconnecting patients nearest the door. Nobody has the patient list in hand. The assembly point, by the plan, is the parking lot across the street.</p>
""", "questions": ["What are the first four actions, and who does each?",
                  "How are the four patients who cannot walk moved, and by whom?",
                  "Who holds the census, and what happens if a name is missing at the assembly point?"]},
    "sections": [
        ("race", "RACE and PASS", "The first actions in a fire", """
<p>RACE is a teaching aid, not a strict order: in a real fire several things happen at once, done by different people.</p>
{{fig:dp07_race_sequence}}
<ul>
<li><strong>Rescue:</strong> move anyone in immediate danger away from the fire.</li>
<li><strong>Alarm:</strong> raise the alarm and call the Bureau of Fire Protection and the hospital&rsquo;s emergency number if hospital-based.</li>
<li><strong>Contain:</strong> close doors to slow smoke and fire.</li>
<li><strong>Extinguish or evacuate:</strong> fight only a small fire, with an exit behind you; otherwise evacuate.</li>
</ul>
{{fig:dp07_extinguisher_pass}}
<p>To use an extinguisher, PASS: pull the pin, aim at the base of the fire, squeeze the handle, sweep side to side. Only a small fire, only with a clear exit behind you, and only if you are trained. A staff member never leaves a connected patient alone to fetch an extinguisher; that job belongs to someone without a patient.</p>
"""),
        ("oxygen", "Oxygen and smoke", "Oxygen makes fire burn faster", """
<p>Oxygen does not burn, but it makes everything else burn faster and hotter. A dialysis unit stores oxygen cylinders for resuscitation and for patients who need it.</p>
{{fig:dp07_oxygen_and_fire}}
<ul>
<li>Turn off oxygen that is not in use, at the cylinder or wall outlet, if it is safe.</li>
<li>Move cylinders away from the fire if it is safe; keep them chained upright.</li>
<li>Never block exits with cylinders or equipment.</li>
</ul>
<p>Smoke kills before heat. Stay low, close doors behind you, and do not use elevators in a fire. In a hospital-based unit, horizontal evacuation (to a safer area on the same floor, behind a closed fire door) is often the first step; the hospital&rsquo;s plan decides.</p>
"""),
        ("takeoff", "Take-off and moving patients", "The emergency take-off, then out by mobility category", """
<p><strong>Take-off by staff.</strong> Patients are taken off by staff, one by one, with the same blood rule as in Module 6 and the Resuscitation Lab: blood that may contain air, is hemolyzed, or follows a severe reaction is never returned; otherwise return it if quick and safe, or clamp and disconnect. In a fire there is rarely time to return blood: clamp and disconnect is usually right. Close a central catheter&rsquo;s own clamps before separating the lines; fistula needles are secured or removed as the unit&rsquo;s protocol says, with pressure on the sites.</p>
<p><strong>Mobility categories, set before the event.</strong> Each patient&rsquo;s category is written on the evacuation sheet at the start of every shift: walks alone, walks with help, wheelchair, stretcher. Staff are assigned to the patients who cannot walk before anything happens. The printable evacuation sheet on the practice page lays this out by station.</p>
{{fig:dp07_evacuation_floor_plan}}
<p>Order of leaving follows danger first (patients nearest the fire), then the plan. Walking patients go with a staff member to the assembly point; staff return for those who need help, wheelchairs and stretchers as the incident lead directs. Physician-on-Duty, Module 30 teaches the same rule from the physician&rsquo;s side: patients who cannot walk are moved by staff assigned in advance, and everyone is counted at the assembly point.</p>
{{key:Staff take patients off with the blood rule; in a fire, clamp and disconnect is usually right. Mobility categories and helpers are set before the event, not during it.}}
"""),
        ("census", "The census", "Account for every patient", """
<p>The most common failure in a real evacuation is not knowing who is out. One named <strong>census nurse</strong> takes the patient list (from the grab bag or the evacuation sheet) and checks off every patient at the assembly point: patients, then staff, companions and visitors.</p>
{{fig:dp07_census_at_the_assembly_point}}
<p>If a name is missing, the census nurse reports at once to the incident lead, who tells the firefighters where the person was last seen. Staff do not re-enter a burning building to search. Everyone stays at the assembly point until the incident lead releases them, so the count stays true; patients who leave with family are recorded as leaving.</p>
<p>The <a href="special-dialysis-nurse-roles-07-safety-and-emergency-preparedness.html">safety nurse</a> plans the routes, the assembly point and the census list, and runs the yearly evacuation drill, always with no patients on machines (Module 12). The Fire Code&rsquo;s implementing rules call for fire exit drills &ldquo;with sufficient frequency&rdquo; where drills are required;[[dp_ra9514]] the yearly frequency is an Academy suggestion.</p>
{{call:A patient or staff member missing at the assembly point: report to the incident lead at once and tell the firefighters. Never re-enter a burning building. Follow your unit protocol, and always ask the attending nephrologist for guidance about patients whose treatment was cut short.}}
<div class="alert alert-amber"><div class="alert-icon">🧒</div><div class="alert-body"><h4>Units that dialyze children</h4><p>Plan car seats, strollers or carriers for small children, and keep the caregiver with the child. A child on a small circuit is taken off by staff with the pediatric team&rsquo;s method. Children are counted by name at the assembly point like everyone else, with their caregivers.</p></div></div>
"""),
    ],
    "debrief": ["""
<p><strong>The first actions.</strong> The nurse who saw the smoke raises the alarm (alarm), closes the reprocessing room door if it is safe (contain), and tells the charge nurse, who becomes incident lead. Someone without a patient calls the Bureau of Fire Protection. The technician may use the extinguisher only on a small fire with an exit behind him; reprocessing rooms hold chemicals, so if smoke keeps coming, he leaves and closes the door. Oxygen not in use is turned off.</p>
<p><strong>Moving patients.</strong> The incident lead orders evacuation. Nurses take patients off one by one: clamp and disconnect, catheter clamps closed before separating lines, pressure on fistula sites. Patients nearest the smoke go first. The three wheelchair users and the stretcher patient have assigned helpers on the evacuation sheet; walking patients go out with a staff member to the parking lot.</p>
<p><strong>The census.</strong> A named nurse takes the patient list and checks every name across the street. A missing name is reported to the incident lead and the firefighters; nobody goes back in. Two nurses disconnecting without a list, and a technician running alone at the fire, were the gaps; both are fixed by naming roles at the start of each shift.</p>
"""],
    "skills": {"title": "Fire response, take-off and census",
               "intro": "In a facilitated evacuation drill with no patients on machines, using manikins and a training circuit.",
               "items": [
                   ("States RACE and assigns each action to a person.", False),
                   ("Demonstrates PASS on a training extinguisher and states when not to fight a fire.", False),
                   ("Never leaves a connected patient alone to fetch an extinguisher.", True),
                   ("Performs the emergency take-off with the blood rule and closes catheter clamps before separating lines.", True),
                   ("Moves patients by their mobility category with the assigned helpers.", False),
                   ("As census nurse, accounts for every patient at the assembly point and reports any missing name at once.", True),
               ],
               "placement": "Walk the evacuation route from your station to the assembly point and time it."},
    "terms": [("Mobility category", "How a patient leaves the building, set before the event."),
              ("Assembly point", "The agreed place outside where everyone is counted."),
              ("Census nurse", "The nurse who holds the patient list and accounts for every patient."),
              ("Horizontal evacuation", "Moving away from the fire on the same floor, behind a closed fire door.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "The patient guide to disaster preparation.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("dp_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["07"])
