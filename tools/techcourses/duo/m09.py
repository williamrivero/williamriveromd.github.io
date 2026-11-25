# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 9: Facility design and commissioning. Written for this course from published sources."""

MODULE = {
    "image_alt": "A young site engineer and a biomedical technician walking a nearly finished dialysis room, chairs still wrapped in plastic.",
    "objectives": [
        "Explain how layout controls infection, emergency response, and staff sightlines.",
        "Review a floor plan for zones, flows, isolation, and the water room.",
        "Describe commissioning as testing systems, not finishing construction.",
        "Hold opening day until every launch gate is passed.",
    ],
    "big": """
{{plain:A building is like the skeleton of a body. You cannot change it easily once it has grown, and everything else hangs on it. A doorway in the wrong place becomes a daily infection risk; a nurse station with no view of the chairs becomes a daily delay.}}
<p>The picture has a limit. A body heals; a building does not. That is why the cheapest time to get design right is on paper, before the first wall is built, with the clinical head, the head nurse, and the technical lead in the room.</p>
{{cards:Key terms for this module|Zone::An area with a set purpose and set rules, such as clean supply or soiled utility.|Flow::The path people, supplies, and waste take through the building.|Isolation area::A space where patients with certain infections dialyze separately.|Commissioning::Testing every system under real conditions before patients arrive.|Launch gate::The checklist that must be complete before the first patient is treated.}}
<p>Your work is to involve the right people in design, to follow the DOH design guidance rather than improvise, and to treat opening day as the reward for passing tests, not for finishing paint.</p>
""",
    "case": {"title": "Open on the fifteenth", "html": """
<p>A contractor tells the owner of a new unit in General Santos, Mr. Danilo Pacquing, that construction will finish on the 12th and that the unit can open on the 15th. The water system was installed on the 10th. The technical lead, Ms. Aileen Ramos, says the system needs a validation period with sampling results before it can be released. Twelve patients have been told they can start on the 15th.</p>
""", "questions": ["Why can the water not be used right away?", "What else must be tested before opening?", "What do you tell the twelve patients?"]},
    "sections": [
        ("flow", "Why layout matters", "Layout is a safety control", """
<p>Design decides how far a nurse walks to an alarm, whether clean and soiled supplies cross, where an infectious patient sits, and how quickly the floor can be evacuated. The DOH publishes planning and design guidelines for dialysis clinics; use them as the design brief, and have the CHD review your plans before construction.[[dch_doh_design2025]]</p>
<p>Bring three people into every design meeting: the clinical head, the head nurse, and the technical lead. Each sees risks an architect may not. The head nurse will ask whether she can see every chair from the station. The technical lead will ask how long the water loop is and where it can be sampled.</p>
{{key:Design with the people who will work in the room. Paper is the cheapest place to fix a mistake.}}
"""),
        ("zones", "Zones", "Zones and flows", """
{{fig:duo09a}}
<p>A dialysis unit has a treatment floor, an isolation room or area, a clean supply room, a soiled utility and waste area, a water treatment room, a nurse station, and a patient entry and waiting area. Patients enter one way; waste leaves another. Clean supplies never pass through the soiled area.</p>
<div class="table-wrap"><table>
<thead><tr><th>Zone</th><th>Design question</th></tr></thead>
<tbody>
<tr><td>Treatment floor</td><td>Can the nurse station see every chair? Is there room to reach a patient from both sides in an emergency?</td></tr>
<tr><td>Isolation</td><td>Is it separate, with its own sink and supplies, as the infection rules require?</td></tr>
<tr><td>Water room</td><td>Is it close to the floor, ventilated, accessible for service, and sized for growth?</td></tr>
<tr><td>Soiled utility and waste</td><td>Does waste leave without crossing clean areas?</td></tr>
<tr><td>Exits</td><td>Can every patient be disconnected and evacuated quickly?</td></tr>
</tbody></table></div>
{{key:Separate clean from soiled, give every chair a sightline, and keep the water room close.}}
"""),
        ("commissioning", "Commissioning", "Commissioning: test before you treat", """
<p>Construction ends when the walls are finished. Commissioning ends when every system has been shown to work. For a dialysis unit that means the water system validated and sampled with acceptable results and formally released by the technical lead; every machine tested and logged; the electrical supply and generator tested under load; emergency equipment checked; and staff trained and signed off on this unit&rsquo;s equipment.</p>
<p>Water takes the longest. A new system can release bacteria and chemicals from new pipes and membranes, and the results of sampling take time. Dialysis water standards, including the International Organization for Standardization (ISO) standard for dialysis fluids and the DOH water order, set what must be tested.[[dch_iso2024]][[dch_doh2013]] Plan the timeline around them, not around the contractor&rsquo;s finish date.</p>
{{key:Construction ends when the walls are done. Commissioning ends when the tests pass.}}
"""),
        ("launch", "Launch gate", "The launch gate", """
{{fig:duo09b}}
<p>Open only when five things are true: the water is validated and released by the technical lead, the machines are tested and logged, staff competencies are signed, an emergency drill has been run, and the license and permits are issued. If any is not yet true, the answer is &ldquo;not yet,&rdquo; and patients are told so honestly with a new date and a safe interim arrangement.</p>
{{stop:Do not treat the first patient until the water is released by the technical lead and the license is issued.}}
{{key:Opening day is a reward for passing tests.}}
"""),
    ],
    "debrief": ["""
<p><strong>Why the water must wait.</strong> A new system has to be validated and sampled, and the results reviewed and released by the technical lead. Five days is unlikely to be enough.</p>
<p><strong>What else must be tested.</strong> Machines, power and generator under load, emergency equipment, staff competency on these machines, an evacuation drill, and the license itself.</p>
<p><strong>The twelve patients.</strong> Tell them the truth, apologize, give a realistic new date, and confirm that each continues dialysis at the current unit until then. Ask the clinical head to confirm each patient&rsquo;s interim plan.</p>
"""],
    "skills": {"title": "Design review checklist, commissioning matrix, and launch gate",
               "intro": "Review a fictional floor plan with a clinical and technical colleague and complete a commissioning matrix.",
               "items": [("Checks zones, flows, isolation, sightlines, and exits against the DOH guidelines.", False),
                         ("Brings the clinical head, head nurse, and technical lead into the review.", False),
                         ("Lists every system to commission with its test and its owner.", False),
                         ("Holds opening until the technical lead releases the water.", True),
                         ("Holds opening until the license and permits are issued.", True),
                         ("Writes an honest message to patients when opening is delayed.", False)],
               "placement": "Walk your own unit with the head nurse and mark every chair she cannot see from the station."},
    "quiz": [
        ("Who should join design meetings besides the architect?",
         ["Only the owner", "The clinical head, head nurse, and technical lead", "The marketing officer", "The landlord"],
         1, "Each sees safety risks the architect may not."),
        ("Why must clean and soiled flows be separated?",
         ["For appearance", "To reduce the spread of infection", "To save floor space", "To reduce noise"],
         1, "Crossing flows carry contamination to clean supplies and patients."),
        ("When does commissioning end?",
         ["When the paint dries", "When every system has been tested and shown to work", "When the contractor is paid", "On the announced opening date"],
         1, "Construction and commissioning are different finishes."),
        ("Who releases a new water system for patient use?",
         ["The owner", "The contractor", "The technical lead, after validation results", "The billing officer"],
         2, "Water release is a protected technical decision."),
        ("The contractor finishes early, but water validation is incomplete. What is the right decision?",
         ["Open and sample later", "Delay opening and keep patients at their current unit", "Use bottled water", "Open half the stations"],
         1, "No patient is treated on unreleased water."),
        ("Which guideline should be the design brief for a Philippine dialysis clinic?",
         ["A hotel design manual", "The DOH planning and design guidelines for dialysis clinics", "A restaurant code", "A school building code"],
         1, "The DOH publishes planning and design guidelines for dialysis clinics."),
    ],
    "terms": [("Validation", "Sampling and testing that show a system produces water or fluid to standard."),
              ("Sightline", "A clear line of sight from the nurse station to a patient.")],
    "readings": [("dialysis-water-treatment-systems.html", "How a dialysis water system works.")],
    "calcs": [],
}


def _balance(quiz):
    """Spread the keyed answers across A to D, deterministically (same as tools/techcourses/uom/quizutil.py)."""
    out = []
    for i, (stem, opts, ans, why) in enumerate(quiz):
        opts = list(opts)
        target = (i * 3 + 1) % 4
        if target != ans:
            opts[target], opts[ans] = opts[ans], opts[target]
        out.append((stem, opts, target, why))
    return out


MODULE["quiz"] = _balance(MODULE["quiz"])
