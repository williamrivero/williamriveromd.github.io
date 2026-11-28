# -*- coding: utf-8 -*-
"""Disaster Preparedness and Response, Module 02: Know Your Unit's Hazards and Dependencies. DRAFT."""

MODULE = {
    "image_alt": "A safety nurse and a water treatment technician tracing pipes and cables behind a reverse osmosis unit with a clipboard and flashlight.",
    "objectives": [
        "Rate your unit&rsquo;s hazards by likelihood and impact, and explain why the rating is a local judgment, not a national standard.",
        "Draw your unit&rsquo;s dependency map: power, water, staff, supplies, transport, records and communications.",
        "Find the dependencies that fail together and the single points of failure, and propose a fix for each.",
        "Explain who owns the dependency map and when it is reviewed.",
    ],
    "big": """
{{plain:A dialysis unit is like a jeepney that needs fuel, a road, a driver and a working engine all at once. Lose any one and the trip stops. A hazard is whatever takes one of them away: a typhoon floods the road, a brownout empties the fuel, a fever outbreak keeps the drivers home.}}
<p>The picture has a limit: a jeepney has four needs, a dialysis unit has at least seven, and they are wired together in ways nobody sees until something fails. The water booster pump needs power. The generator needs diesel, which needs a truck, which needs a road. Staff need transport and, in a long event, somewhere to sleep. This module is about drawing those wires before a disaster draws them for you.</p>
<p>The work is owned by the Dialysis Clinical Head and the unit manager, with the safety nurse (or head nurse) running it. The <a href="dialysis-clinical-head-07-disaster-and-continuity.html">Dialysis Clinical Head, Module 7</a> teaches the map at leadership level; this module is how the whole team builds and checks it.</p>
{{cards:Key terms for this module|Hazard::Something that can cause harm: a typhoon, flood, earthquake, fire, outage or outbreak.|Vulnerability::How easily your unit is harmed by a hazard, given where it is and how it is built and run.|Dependency::Something the unit cannot treat patients without, such as power, treated water or staff.|Single point of failure::One part whose failure stops the whole service.|Fail together::Two dependencies that the same event takes away at the same time.|Buffer::Stored capacity that buys time: fuel, water, supplies, spare staff.}}
""",
    "case": {"title": "The map that missed the pump", "html": """
<p>A 20-station unit in San Fernando, Pampanga, has a standby generator that starts within a minute and passes its monthly test. During a two-hour brownout in July, the generator starts on time, the machines keep running, and then, eleven minutes later, every machine alarms for low water pressure.</p>
<p>The water treatment technician finds the cause: the water booster pump that feeds the reverse osmosis system is on the same breaker as the main supply, not on the generator circuit. The generator ran the machines but not the water that the machines needed. The storage tank had carried the unit for eleven minutes.</p>
""", "questions": ["Which two dependencies failed together, and why did nobody notice in the monthly generator test?",
                  "What should the generator test include from now on?",
                  "Who in your unit owns finding this kind of problem?"]},
    "sections": [
        ("hazards", "Rating hazards", "Which hazards matter most for your unit?", """
<p>A hazard and vulnerability assessment asks two questions about each hazard: how likely is it here, and how much would it hurt this unit if it happened? A unit beside a river in Marikina rates floods differently from a unit on the fourth floor of a hospital in Baguio.</p>
{{fig:dp02_hazard_matrix}}
<p>The matrix in the figure is an example, not a rating for your unit. Fill it in as a team once a year, before typhoon season, with what you know: past floods on your street, the age of the building, the reliability of your power line, the distance to the nearest unit that could take your patients. Two hazards in the top-right corner get a written action plan first.</p>
<p>The ratings are a local judgment. No Philippine regulation gives a dialysis-specific scoring method, and this course does not invent one. What matters is that the team agrees on the list and acts on the top of it.</p>
{{key:Rate likelihood and impact for your own unit, once a year, as a team. Act first on what is both likely and damaging.}}
"""),
        ("map", "The dependency map", "Seven things your unit runs on", """
<p>Every hazard reaches the patients through the same few dependencies. Draw them on one page with the chair in the middle.</p>
{{fig:dp02_dependency_web}}
<div class="table-wrap"><table>
<thead><tr><th>Dependency</th><th>What to write on the map</th><th>Ask</th></tr></thead>
<tbody>
<tr><td>Power</td><td>Utility line, generator, transfer switch, uninterruptible power supply (UPS) outlets, fuel</td><td>What runs on the generator, and for how long?</td></tr>
<tr><td>Water</td><td>Municipal supply, storage tank, booster pump, treatment train, reverse osmosis (RO)</td><td>How many hours does stored water last? What does the pump run on?</td></tr>
<tr><td>Staff</td><td>Where each person lives, how they travel, who can stay overnight</td><td>Who can still come in when the main road floods?</td></tr>
<tr><td>Supplies</td><td>Dialyzers, lines, concentrates, needles, medicines, oxygen, fuel</td><td>How many days of treatment are on the shelf, and above the flood line?</td></tr>
<tr><td>Transport</td><td>How patients come (tricycle, jeepney, family car), the unit van, ambulance access</td><td>Which patients cannot reach the unit if public transport stops?</td></tr>
<tr><td>Records</td><td>Electronic records, paper downtime forms, the patient list, prescriptions</td><td>Can another unit get a patient&rsquo;s prescription if your system is down?</td></tr>
<tr><td>Communications</td><td>Mobile networks, landline, messaging groups, two-way radio</td><td>How do you reach staff and patients when calls fail?</td></tr>
</tbody></table></div>
<p>The map is a unit document. The patient list and staff addresses on it are personal data under the Data Privacy Act (Republic Act No. 10173): keep them with the unit&rsquo;s records, share them only with the people who need them, and do not post them in open group chats.[[dp_ra10173]]</p>
"""),
        ("together", "What fails together", "Dependencies that fail together, and single points of failure", """
<p>The most dangerous lines on the map are the ones that connect two dependencies, because one event then takes both away. Power and water fail together when the booster pump is on mains power only. Staff and transport fail together when the same flooded road blocks both. Records and communications fail together when the electronic system and the phone system share one internet line.</p>
{{fig:dp02_single_point_of_failure}}
<p>A single point of failure is one part whose loss stops the whole service: one booster pump, one transfer switch, one person who knows the generator, one copy of the patient list. Each needs a fix, and the fixes are usually simple: put the pump on the generator circuit, train a second person, print the list, store fuel and supplies above the flood line.</p>
{{scene:Testing the whole chain|After the Pampanga case, the unit changed its monthly generator test. The technician now runs it with the machines in rinse mode and the water system running for 30 minutes, and checks the water pressure at the loop, not just the generator&rsquo;s voltage.}}
<p>A dependency map is only as good as its last test. The biomedical and water treatment technicians check the power and water lines on the map against what is really wired (the <a href="dialysis-unit-manager-12-business-continuity.html">Unit Manager, Module 12</a> turns the map into a business continuity plan, with an outage autonomy calculation). The water capacity calculator shows whether the water system can meet peak demand.</p>
{{key:Look for the lines between dependencies. Fix the single points of failure, and test the whole chain, not one machine.}}
"""),
        ("owner", "Who owns the map", "Who owns it and when it is checked", """
<p>The unit manager owns the map and its fixes; the Dialysis Clinical Head approves the clinical parts (which patients are most at risk when transport fails); the safety nurse (or head nurse) runs the review; the technicians check the power and water lines; the social worker and records officer check the patient and contact lists. The unit owner receives the list of fixes that need money.</p>
<p>Review it once a year before typhoon season, after any building or equipment change, and after any real disruption. The annual hazard review is the first drill on the drill table (Module 12).</p>
{{call:A single point of failure that could stop treatment for every patient (water, power, the only generator) is reported to the unit manager and the Dialysis Clinical Head the day it is found, with an interim plan. Follow your unit protocol, and always ask the attending nephrologist for guidance on any change to treatment.}}
"""),
    ],
    "debrief": ["""
<p><strong>What failed together.</strong> Power and water: the generator powered the machines, but the booster pump stayed on the utility line. The monthly test checked the generator alone, with no load on the water system, so the gap never showed.</p>
<p><strong>What the test should include.</strong> A run under real load: machines in rinse or a planned test, the water system running, and the loop pressure checked for at least as long as the storage tank lasts. Then the transfer back to utility power.</p>
<p><strong>Who owns it.</strong> The unit manager owns the fix; the water treatment and biomedical technicians find and test it; the safety nurse (or head nurse) puts it on the annual review. A dependency map drawn on paper without walking the wiring would have missed this pump too.</p>
"""],
    "skills": {"title": "Building your unit's dependency map",
               "intro": "With the technicians and the head nurse, build or update the unit&rsquo;s one-page dependency map.",
               "items": [
                   ("Lists all seven dependencies with the specific equipment, people or suppliers behind each.", True),
                   ("Walks the power and water lines with the technicians and confirms what runs on the generator.", True),
                   ("Marks at least two pairs of dependencies that fail together.", False),
                   ("Names each single point of failure with a proposed fix and an owner.", False),
                   ("Keeps the patient and staff lists on the map as unit records under the Data Privacy Act.", False),
                   ("Rates the unit&rsquo;s hazards by likelihood and impact with the team.", False),
               ],
               "placement": "Present the map and the top three fixes to the unit manager and the Dialysis Clinical Head."},
    "terms": [("Hazard", "Something that can cause harm, such as a typhoon or an outage."),
              ("Vulnerability", "How easily the unit is harmed by a hazard."),
              ("Dependency", "Something the unit cannot treat patients without."),
              ("Single point of failure", "One part whose failure stops the whole service."),
              ("Buffer", "Stored capacity that buys time."),
              ("Transfer switch", "The switch that moves the unit&rsquo;s load from the utility line to the generator.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "What patients are told to prepare.")],
    "calcs": ["calc-wts-capacity.html", "calc-dialysis-continuity-planner.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("dp_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["02"])
