# -*- coding: utf-8 -*-
"""Disaster Preparedness and Response, Module 09: Heat, Ashfall and Outbreaks."""

MODULE = {
    "image_alt": "Two staff in masks closing the windows of a dialysis unit while fine gray volcanic ash coats the parked cars outside.",
    "objectives": [
        "Protect patients on high heat-index days, from the trip to the unit to the waiting area, without loosening fluid limits.",
        "Protect the building, the water and air intakes, staff and patients during volcanic ashfall.",
        "Treat an infectious outbreak as a disaster: cohorting, staff shortage and supply strain.",
        "Know which agency warns for each hazard, and who decides each clinical change.",
    ],
    "big": """
{{plain:Some disasters do not arrive in one night. Heat, ashfall and outbreaks come slowly, stay for days or weeks, and wear a unit down. They are less like a storm and more like a long drought: the danger is not one moment but the slow loss of what the unit runs on.}}
<p>The picture has a limit. A drought only takes water; these hazards take different things. Heat works through the patient&rsquo;s trip and the waiting room. Ash works through the air and water intakes, the roads and the lungs. An outbreak works through staff and supplies, and through the risk that the unit itself spreads infection. Each needs its own small plan, built on the same unit plan (Module 3).</p>
<p>The site&rsquo;s <a href="../guides/el-nino-heat-dialysis.html">El Ni&ntilde;o and heat guide</a> explains for patients why heat is hard on people on dialysis.</p>
{{cards:Key terms for this module|Heat index::How hot it feels when humidity is added to the air temperature; PAGASA publishes daily forecasts.|Ashfall::Fine volcanic rock and glass that falls after an eruption; it is abrasive, slippery and harmful to breathe.|Volcano alert level::PHIVOLCS&rsquo;s scale for a volcano&rsquo;s activity.|Cohorting::Grouping patients with the same infection status by shift, zone or staff to limit spread.|Backup roster::A list of staff who can be called in when others are absent.|Intake::The opening through which the building draws outside air or the water system draws water.}}
""",
    "case": {"title": "Ash on the windshield", "html": """
<p>At dawn after an eruption, fine gray ash covers the cars and roads around a 12-station unit in Tanauan, Batangas. PHIVOLCS has raised the volcano&rsquo;s alert level. The first shift begins at 6:00 a.m. Patients arrive with ash on their clothes and hair; one older patient with chronic lung disease is coughing.</p>
<p>The windows of the waiting area are open, as usual, for ventilation. The water treatment room draws from a rooftop storage tank with a loose cover. Two staff call to say the roads from their towns are slippery and visibility is poor.</p>
""", "questions": ["What do you close, cover and clean before the first patient is connected?",
                  "What does the water treatment technician check?",
                  "How do you decide whether the coughing patient dialyzes as usual?"]},
    "sections": [
        ("heat", "Heat", "Heat-index days and the trip to the unit", """
<p>On hot days, the danger is often on the way to the unit: a jeepney ride, a walk in the sun, a long wait outside. Many dialysis patients are older, have heart disease, and cannot simply &ldquo;drink more water.&rdquo;</p>
{{fig:dp09_heat_and_the_journey}}
<ul>
<li><strong>From home and on the way:</strong> travel in the cooler part of the day where the schedule allows; shade, a hat or umbrella, a light towel.</li>
<li><strong>Waiting:</strong> a cool, shaded waiting area inside, with seats; nobody waits in the sun outside the unit.</li>
<li><strong>Fluid:</strong> the patient&rsquo;s fluid limit does not change on its own. Ice chips or sips from the measured cup help; any change to the fluid goal or prescription is the attending nephrologist&rsquo;s decision.</li>
<li><strong>Watch for heat illness:</strong> dizziness, confusion, cramps or hot dry skin on arrival are reported to the physician-on-duty before connection.</li>
</ul>
<p>Heat is not a minor hazard for this group. In a 2026 scoping review, extreme heat events were associated with 9% to 45% higher mortality among patients on kidney replacement therapy, across the studies that measured it.[[dp_sandal2026]] PAGASA publishes daily heat index forecasts with danger levels; the unit checks them in the hot dry season and reminds patients on the riskiest days.</p>
"""),
        ("ash", "Ashfall", "Volcanic ashfall", """
<p>Ash is abrasive, conducts electricity when wet, clogs filters, and irritates eyes and lungs. It reaches a dialysis unit through the air, the water, the roads and people&rsquo;s clothes.</p>
{{fig:dp09_ashfall_protections}}
<ul>
<li><strong>Close the building:</strong> keep windows and doors closed; cover outside air intakes as the building engineer advises.</li>
<li><strong>Protect the water:</strong> cover storage tanks and water intakes; the water treatment technician checks pre-filters and sediment filters more often, watches for falling pressure, and tests before treatments continue if ash may have entered the water.</li>
<li><strong>Seal the reverse osmosis (RO) room:</strong> keep it closed; ash on equipment is removed as the manufacturer advises, not with water on live electrical parts.</li>
<li><strong>Clean ash before entry:</strong> a place at the entrance to remove ash from clothes, hair, shoes and bags.</li>
<li><strong>Masks:</strong> staff and patients outdoors wear well-fitting masks (N95 where available), especially those with lung disease.</li>
<li><strong>Transport:</strong> ash makes roads slippery and reduces visibility; staff travel only when safe, and the plan&rsquo;s staff call-down applies (Module 3).</li>
</ul>
<p>PHIVOLCS raises and lowers the volcano alert level and advises on danger zones; the LDRRMO orders evacuations. A unit inside or near a danger zone uses those orders as triggers in its plan.</p>
"""),
        ("outbreak", "Outbreaks", "An infectious outbreak as a disaster", """
<p>An outbreak does not knock down the building, but it can stop a unit as surely as a flood: staff fall ill or must isolate, supplies of masks and gowns run short, and patients who cannot be dialyzed elsewhere must be treated without spreading infection. Reviews of disasters and kidney care stress the same answer for every kind of event: preparation and training before it, and a plan applied during and after it.[[dp_sever2024]]</p>
{{fig:dp09_outbreak_as_a_disaster}}
<ul>
<li><strong>Cohorting:</strong> separate infected and non-infected patients by shift or zone, with dedicated staff where possible, as the infection control protocol and the Department of Health&rsquo;s guidance direct.</li>
<li><strong>Staff shortage:</strong> a backup roster; minimum staffing for a safe shift; staff who are ill stay home.</li>
<li><strong>Supply strain:</strong> count and conserve personal protective equipment (PPE) and dialysis supplies; order early; do not run out of essentials.</li>
</ul>
<p>Outbreak rules change with each infection, so this module gives the frame and leaves the details to the unit&rsquo;s infection control nurse and the Department of Health&rsquo;s current guidance.</p>
{{call:A patient arriving with signs of heat illness, breathing difficulty after ash exposure, or fever during an outbreak: tell the physician-on-duty before connection. Follow your unit protocol, and always ask the attending nephrologist for guidance on any change to treatment.}}
"""),
    ],
    "debrief": ["""
<p><strong>Close, cover, clean.</strong> Close the waiting-area windows and doors; set up an ash-cleaning point at the entrance; cover outside air intakes as the engineer advises; check that the rooftop tank cover is secure.</p>
<p><strong>The water.</strong> The technician checks the tank, the pre-filters and the pressures, and tests before treatments continue if ash may have entered the water. If the water is in doubt, Module 8&rsquo;s water failure steps apply: no new starts until the water is released.</p>
<p><strong>The coughing patient.</strong> The physician-on-duty examines him before connection (breathing, oxygen saturation) and calls the attending nephrologist if he is unwell. He wears a mask, and the decision to dialyze as usual or send him to the hospital is clinical. The two staff with unsafe roads do not travel; the call-down and minimum staffing decide the shift.</p>
"""],
    "skills": {"title": "Slow hazards: heat, ash, outbreak",
               "intro": "In a tabletop (the ashfall or outbreak scenario on the practice page) or on a real hot-season day.",
               "items": [
                   ("Names the agency that warns for heat, ashfall and outbreaks.", False),
                   ("Keeps waiting patients out of the sun and does not change fluid limits without the nephrologist.", True),
                   ("Lists the ashfall steps: close, cover intakes, protect water, seal the RO room, clean ash at entry, masks.", False),
                   ("Asks the water technician to check and test before continuing treatments when ash may have entered the water.", True),
                   ("Describes cohorting, a backup roster and supply counts for an outbreak.", False),
               ],
               "placement": "Find your unit&rsquo;s air and water intakes with the building engineer and agree how each is covered during ashfall."},
    "terms": [("Heat index", "How hot it feels when humidity is added to the air temperature."),
              ("Ashfall", "Fine volcanic rock and glass that falls after an eruption."),
              ("Volcano alert level", "PHIVOLCS&rsquo;s scale for a volcano&rsquo;s activity."),
              ("Cohorting", "Grouping patients with the same infection status by shift, zone or staff."),
              ("Backup roster", "Staff who can be called in when others are absent."),
              ("Intake", "The opening through which the building draws air or the system draws water.")],
    "readings": [("el-nino-heat-dialysis.html", "Heat and dialysis: the patient guide."),
                 ("climate-extremes-kidney-care.html", "Climate extremes and kidney care.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("dp_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["09"])
