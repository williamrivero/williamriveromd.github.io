# -*- coding: utf-8 -*-
"""Disaster Preparedness and Response, Module 03: The Unit Plan and Who Commands."""

MODULE = {
    "image_alt": "A small dialysis team around a table with a one-page plan, a printed phone tree and a two-way radio.",
    "objectives": [
        "Write the eight parts of a one-page activation plan for a dialysis unit.",
        "Describe a simple incident command structure for a dialysis unit, and explain why the safety nurse plans and drills but does not command during the event.",
        "Set activation triggers from PAGASA wind signals, PHIVOLCS reports and utility notices, and explain why the actions at each trigger are the unit&rsquo;s own choice.",
        "Keep communications working when mobile calls fail, and protect the call list as personal data.",
        "Describe what a receiving-unit agreement must contain, and how a unit fits into its hospital&rsquo;s DRRM-H plan or its LDRRMO.",
    ],
    "big": """
{{plain:A disaster plan is like the fire exit sign above a door: useful only if it is short, posted where people are, and the same for everyone. A thick binder in the manager&rsquo;s office is a library, not a plan.}}
<p>The sign has a limit: an exit sign tells you where to go, but a dialysis unit also has to decide who leads, who calls whom, which patients come early, and where they go if the unit closes. So the plan has two layers. The first is one page that anyone on the shift can open and follow. The second is the detail behind it (contact lists, agreements, the dependency map), kept up to date by the people who own it.</p>
<p>Reviews of disasters and kidney care keep finding the same gap: units with no written plan, or a plan nobody had practiced.[[dp_sever2023]][[dp_sandal2025]] After Hurricane Maria, a nephrology service in Puerto Rico listed its lessons: a plan shared with staff and patients before the storm, a registry of patients with updated phone numbers, relatives and an address rescuers can reach, a prearranged plan to move patients to another center, and attention to the staff&rsquo;s own needs.[[dp_bonilla2019]]</p>
{{cards:Key terms for this module|Activation::The moment the plan is switched on, by a named person, for a named trigger.|Trigger::A defined event that activates the plan or the next step of it, such as a wind signal.|Incident lead::The person who directs the response during the event.|Incident command::A simple structure that names who leads, who handles patients, equipment, tracking and outside contacts.|Call-down::Contacting every staff member and patient on the list in a set order.|Receiving-unit agreement::A written agreement that another unit will treat your patients if you cannot.}}
""",
    "case": {"title": "Signal No. 2 on a Sunday", "html": """
<p>At 11:00 a.m. on a Sunday, PAGASA raises Tropical Cyclone Wind Signal No. 2 for Bulacan. A 16-station unit in Malolos is closed on Sundays. Its head nurse, who is also its acting safety nurse because no safety nurse has been named, is at a family lunch. The unit&rsquo;s plan says: &ldquo;Signal No. 2: activate the call-down; ask the attending nephrologist about early dialysis.&rdquo;</p>
<p>The call list has 58 patients and 19 staff. The Monday&ndash;Wednesday&ndash;Friday group has 30 patients. The charge nurse for Monday lives in a barangay that flooded last year. One receiving unit is listed in the plan; its contact person retired in June.</p>
""", "questions": ["Who activates the plan, and who leads once it is active?",
                  "Who is called first, and in what order?",
                  "What has to be fixed on the plan before the next signal?"]},
    "sections": [
        ("plan", "The one-page plan", "One page anyone on the shift can follow", """
<p>The activation plan fits on one page, posted beside the nurses&rsquo; station and saved in the grab bag. Behind it sit the detailed documents, each with an owner.</p>
{{fig:dp03_one_page_plan}}
<div class="table-wrap"><table>
<thead><tr><th>Part</th><th>What it says</th><th>Owner of the detail</th></tr></thead>
<tbody>
<tr><td>Triggers</td><td>What switches the plan on, and what happens at each level</td><td>Unit manager, with the Dialysis Clinical Head</td></tr>
<tr><td>Who leads</td><td>The incident lead by shift, and the deputy</td><td>Unit manager</td></tr>
<tr><td>First calls</td><td>The attending nephrologist, the Dialysis Clinical Head, the unit manager, the technicians</td><td>Safety nurse (or head nurse)</td></tr>
<tr><td>Patients on machines</td><td>The rule: stay with them; protect in place; staff take patients off</td><td>Head nurse</td></tr>
<tr><td>Patients due today</td><td>Call-down, early dialysis decision, transport</td><td>Charge nurse, with the attending nephrologist</td></tr>
<tr><td>Receiving units</td><td>Names, contact persons, what to send</td><td>Unit manager and social worker</td></tr>
<tr><td>Supplies and power</td><td>Fuel, water, supply buffer, generator check</td><td>Technicians</td></tr>
<tr><td>Restart</td><td>The five signed gates (Module 11)</td><td>Head nurse and Dialysis Clinical Head</td></tr>
</tbody></table></div>
<p>A hospital-based unit writes its page inside the hospital&rsquo;s disaster plan, which the Department of Health frames through its DRRM-H policy and its Hospitals Safe from Disasters policy.[[dp_doh2019]][[dp_doh2013]] A freestanding unit writes its own page and coordinates warnings and evacuation routes with its city or municipal LDRRMO, set up under Republic Act No. 10121.[[dp_ra10121]]</p>
"""),
        ("command", "Who commands", "Incident command for a dialysis unit", """
<p>In an event, one person directs. In a dialysis unit that is the <strong>charge nurse, with the physician-on-duty</strong> (or the attending nephrologist by phone): they know the patients on the machines and can make clinical decisions. Four groups report to them.</p>
{{fig:dp03_command_chart}}
<ul>
<li><strong>Patient care (nurses).</strong> Keep patients safe, continue or stop dialysis as ordered, prepare for transfer if needed.</li>
<li><strong>Equipment and utilities (technicians).</strong> Keep key equipment working; check water, power and supplies; report any major problem.</li>
<li><strong>Tracking and records (records officer, social worker).</strong> Keep the patient list updated, track transfers and locations.</li>
<li><strong>Outside contacts.</strong> Receiving units, the hospital and the LDRRMO: confirm beds and services, report urgent needs.</li>
</ul>
<p><strong>The safety nurse plans and runs drills, but does not command during the event.</strong> The safety nurse (<a href="special-dialysis-nurse-roles-07-safety-and-emergency-preparedness.html">Special Dialysis Nurse Roles, Module 7</a>) knows the plan best and often becomes the incident lead&rsquo;s closest helper, but command stays with the people who carry clinical responsibility for the patients on that shift. Licensed engineers and technicians decide about the building, the water and the machines. Where no safety nurse is designated, the head nurse holds the planning role.</p>
{{key:One incident lead per shift, with a named deputy. The safety nurse plans; the charge nurse and the physician command; technicians decide about equipment.}}
"""),
        ("triggers", "Triggers", "Triggers: when the plan switches on", """
<p>A trigger turns a vague worry into a set time to act. PAGASA&rsquo;s five tropical cyclone wind signals each carry a wind threat and a lead time before the winds arrive: Signal No. 1, 39 to 61 km/h within 36 hours; No. 2, 62 to 88 km/h within 24 hours; No. 3, 89 to 117 km/h within 18 hours; No. 4, 118 to 184 km/h within 12 hours; and No. 5, 185 km/h or more within 12 hours.[[pagasa_tcws]] The lead time is what a unit uses.</p>
{{fig:dp03_trigger_ladder}}
<p>The actions in the figure are an example. Each unit sets its own, because a unit that floods at Signal No. 2 cannot wait for No. 4. A common pattern is: review the plan and the call list at Signal No. 1; start the call-down and ask the attending nephrologist about early dialysis at No. 2; arrange staff transport, stock up and set the last safe session time at No. 3; close and track patients at No. 4 or No. 5. Other triggers are a PHIVOLCS earthquake report or volcano alert, a utility notice of a long interruption, and the LDRRMO&rsquo;s evacuation advice.</p>
<p>Name the person who declares each trigger (usually the incident lead or the unit manager), and write the time of activation on the record. A plan that activates &ldquo;when things look bad&rdquo; activates too late.</p>
"""),
        ("comms", "Communications and agreements", "Calls that still get through, and someone to send patients to", """
<p>When networks are overloaded or towers lose power, voice calls fail first. Text messages often still get through, and a messaging group reaches many people at once. Build the call-down tree with more than one channel: text, call, messaging group, two-way radio between the unit and its generator room, and a runner on foot if all else fails.</p>
{{fig:dp03_communication_tree}}
<p>Order the call-down by risk. Staff first (so the unit knows who can come), then patients due in the next 24 hours, then the rest. Every patient&rsquo;s record shows two phone numbers and a family contact, checked before typhoon season.</p>
<p><strong>Receiving-unit agreements.</strong> A receiving unit is useful only if someone there answers and knows what to expect. A written agreement names the contact person and a deputy, how many extra patients the unit could take and on which shifts, what you will send (a handoff with the prescription, access, last laboratory results, hepatitis status and medicines; Module 10), and how patients will be transported. Check the contacts every year; people move on.</p>
<p>The call list is personal data. Keep it as a unit document under the Data Privacy Act, share it only with the staff doing the call-down, and delete forwarded copies after the event.[[dp_ra10173]]</p>
{{call:When a trigger is reached and the incident lead cannot be reached, the deputy activates the plan and informs the unit manager and the Dialysis Clinical Head. Follow your unit protocol, and always ask the attending nephrologist for guidance on early dialysis or any change to treatment.}}
"""),
    ],
    "debrief": ["""
<p><strong>Who activates and who leads.</strong> The plan names the trigger (Signal No. 2) and the person who activates it. On a Sunday that should be the on-call lead or the deputy, not whoever happens to read the news. Once active, the Monday charge nurse leads with the physician-on-duty; the acting safety nurse supports the call-down.</p>
<p><strong>Call order.</strong> Staff first, to know who can come in Monday, especially the charge nurse from the flood-prone barangay. Then the 30 Monday patients, with the attending nephrologist&rsquo;s decision on early dialysis. Then the rest.</p>
<p><strong>What to fix.</strong> Name a deputy for every role, replace the retired contact at the receiving unit and add a second unit, and check every patient&rsquo;s two phone numbers before the season. A call-down drill (Module 12) would have found the retired contact.</p>
"""],
    "skills": {"title": "Writing and testing the one-page plan",
               "intro": "With the head nurse and the unit manager, write or update the unit&rsquo;s one-page activation plan and test it in a short tabletop.",
               "items": [
                   ("Includes all eight parts: triggers, who leads, first calls, patients on machines, patients due today, receiving units, supplies and power, restart.", True),
                   ("Names the incident lead and a deputy for every shift.", True),
                   ("Sets triggers with the unit&rsquo;s own actions at each PAGASA signal level.", False),
                   ("Builds a call-down tree with at least two channels besides voice calls.", False),
                   ("Lists at least two receiving units with current contact persons.", True),
                   ("Keeps the call list as a protected unit document.", False),
               ],
               "placement": "Run a 20-minute walk-through of the plan with the next shift&rsquo;s charge nurse and record what was unclear."},
    "terms": [("Activation", "The moment the plan is switched on, by a named person, for a named trigger."),
              ("Trigger", "A defined event that activates the plan or its next step."),
              ("Incident lead", "The person who directs the response during the event."),
              ("Call-down", "Contacting every staff member and patient on the list in a set order."),
              ("Receiving-unit agreement", "A written agreement that another unit will treat your patients.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "How patients are told to prepare when a signal is raised.")],
    "calcs": ["calc-dialysis-continuity-planner.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("dp_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["03"])
