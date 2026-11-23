# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 07: The Dialysis Clock: Disasters and Continuity. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician at a dialysis unit desk during typhoon rain, on the phone, a printed patient tracker and a map in front of her.",
    "objectives": [
        "Explain why a patient on hemodialysis has a deadline measured in days, and why dialyzing early before a storm helps.",
        "Map the hazards and the dependencies that can fail together, including a backup site that shares your road or power line.",
        "Write an agreement with a receiving unit that names real capacity, contacts, records, transport, and billing.",
        "Activate a continuity plan and run a patient tracker until every displaced patient has an outcome or a named owner.",
        "Restart only when facility, water, machines, staff, supplies, and records are verified and signed.",
        "Lead an after-action review that produces owners, dates, and a repeat drill.",
    ],
    "big": """
{{plain:Every patient on hemodialysis carries a clock that starts at the end of each session. Without kidneys, potassium and water rise every hour the clock runs. A disaster does not stop the clock; it only removes the place where it gets reset.}}
{{fig:dch07_clock}}
<p>The picture has a limit. The clock does not run at the same speed for everyone. A patient with some remaining urine, a careful diet, and a low potassium can wait longer than a patient who gains three kilograms over a weekend. Who can wait, and for how long, is a physician&rsquo;s decision for each patient, which is why the tracker needs a clinician&rsquo;s priority on every row.</p>
{{cards:Key terms for this module|Continuity plan::The written plan that keeps dialysis going, or moves it, when the unit cannot operate normally.|Dependency::Anything the unit needs to run: power, water pressure, roads, staff, supplies, records, communications.|Incident command::A temporary structure that assigns roles such as commander, clinical lead, logistics, communications, and patient tracking.|Receiving unit::A dialysis facility that has agreed to treat your patients when you cannot.|Patient tracker::A list of every affected patient and their status until each has a confirmed outcome.|Stand-down::The decision to end the emergency response and return to normal operations.|LDRRMO::Local Disaster Risk Reduction and Management Office.}}
""",
    "case": {"title": "The road is flooded", "html": """
<p>Typhoon signal number 3 is raised over Bulacan on a Thursday afternoon. At 14:20, the access road to your twelve-station unit in Marilao floods knee-deep. Utility power fails and water pressure drops. The generator starts, but the reverse osmosis pump alarms. Four patients are mid-session. Eight more are due on the next shift, and one of them, Mrs. Norma Garcia, already missed Tuesday because of an earlier flood and is now breathless.</p>
<p>Your backup unit in Meycauayan confirms four slots for tonight. It is on the same main road. Mobile signal comes and goes.</p>
""", "questions": ["What do you do for the four patients already connected?",
                  "How do you decide who goes to the four slots, and what happens to the others?",
                  "When can the unit restart, and who signs?"]},
    "sections": [
        ("evidence", "What the evidence shows", "What disasters do to dialysis patients", """
<p>The risk of a dialysis patient is highest on the day after the usual two-day weekend gap, even in ordinary times.[[dch_foley2011]] A disaster stretches that gap. The evidence from hurricanes in the United States shows both the harm and what reduces it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>Finding</th><th>Strength and limits</th></tr></thead>
<tbody>
<tr><td>Hurricane Sandy, 2012</td><td>Of 13,836 patients in the affected area, 60% were dialyzed early before landfall. Early dialysis was associated with fewer emergency visits (adjusted odds ratio 0.80), fewer hospitalizations (0.79), and lower 30-day mortality (0.72)[[dch_lurie2015]]</td><td>Observational; patients who declined early dialysis may have differed</td></tr>
<tr><td>Hurricane Sandy, 2012, lower Manhattan</td><td>26% of surveyed patients missed dialysis, a median of two sessions; 66% were treated at a unit other than their own. Only 44% carried a detailed medication list[[dch_murakami2015]]</td><td>Cross-sectional survey</td></tr>
<tr><td>Hurricane Katrina, 2005</td><td>Among patients from 94 affected clinics, the hurricane was not associated with significantly increased mortality in adjusted analyses[[dch_kutner2009]]</td><td>Cohort; widespread relocation may have protected patients</td></tr>
<tr><td>After Katrina</td><td>About 24% of hemodialysis patients had symptoms of post-traumatic stress a year later, more often if they missed three or more sessions[[dch_hyre2007]]; depression was associated with higher mortality and hospitalization[[dch_edmondson2013]]</td><td>Cohort and cross-sectional</td></tr>
</tbody></table></div>
<p>Philippine dialysis data from typhoons were not found in the literature searched. The United States evidence supports two practical steps: dialyze patients early when a storm is forecast, if the attending nephrologists agree, and plan for patients to be treated at other units with records in hand.</p>
{{key:The most effective disaster intervention may happen two days before landfall: an extra session, a full patient card, and a phone tree that works.}}
"""),
        ("prepare", "Before the season", "Map hazards and the dependencies that fail together", """
<p>List the hazards your unit actually faces: typhoon and flood, earthquake, fire, extended power or water loss, equipment or information system failure, outbreak, and supply or staff disruption. For each, map the effect on three groups: patients connected now, patients due today, and patients already overdue.</p>
{{fig:dch07_shared}}
<p>Then look for shared dependencies. A backup unit that uses the same power feeder, the same water main, or the same flood-prone road will fail when you do. Find at least one receiving unit in a different direction.</p>
<div class="table-wrap"><table>
<thead><tr><th>A receiving agreement should name</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Activation contacts, with two ways to reach each</td><td>Mobile networks fail first</td></tr>
<tr><td>Real capacity: staffed, released stations and time slots</td><td>An available chair is not an accepted patient</td></tr>
<tr><td>Acceptance process and the records that travel</td><td>The receiving physician needs the order, access, infection status, and last results</td></tr>
<tr><td>Transport responsibility</td><td>Patients may not be able to get there</td></tr>
<tr><td>Billing and benefit handling, confirmed with the claims lead and PhilHealth</td><td>Prevents duplicate claims and protects access when payment is uncertain</td></tr>
<tr><td>Supplies, mutual obligations, and testing schedule</td><td>An agreement never tested is a hope</td></tr>
</tbody></table></div>
<p>Coordinate with the LDRRMO, emergency medical services, and, for hospital-based units, the hospital incident command, as the national disaster law expects.[[dch_ra10121]] Keep an offline, access-controlled patient roster and contact list, and give every patient an emergency card with their diagnosis, access, dry weight, medicines, last results, and unit contacts.[[dch_cdc_ep_patients]]</p>
"""),
        ("activate", "Activation", "Activate, account, and track", """
<p>At activation, open the command log, confirm the hazards, control affected operations, and account for every patient and staff member in the building. Use your chairside emergency procedures for patients on the machine. Then turn to the patients who are not in the building.</p>
{{fig:dch07_tracker}}
{{flow:One row of the tracker, one patient|Contact::Reached, by which route, at what time. If not, the fallback contact.|Clinical priority::Set by the attending nephrologist or physician on duty, not by the order of the list.|Placement::Accepted by name at a receiving unit, or referred for urgent assessment.|Transport::Arranged and confirmed.|Outcome::Treated, admitted, or still pending with a named owner and a next check time.}}
{{call:Stop and escalate to the LDRRMO, the receiving hospital, or emergency medical services any patient with urgent symptoms who cannot be placed. Do not stand down while any row on the tracker lacks an outcome or a named owner.}}
<p>Calculator 6 shows, for each patient, the hours since the last session and flags those past the usual long gap. It supports, and never replaces, the physician&rsquo;s priority.</p>
"""),
        ("restart", "Restart", "Restart is a signed decision", """
{{fig:dch07_restart}}
<p>Power returning restores one dependency. Before treating patients again, verify the facility is safe, the water system is within limits after the disruption, each machine is released, staffing and supplies are adequate, and records are available. The technical leads sign the technical release; you sign the clinical restart. Then review outstanding transfers, reconcile any downtime records (Module 12), and hold an after-action review within a week.</p>
<p>Walk the fire and evacuation plan with the facility safety officer at least once a year: who raises the alarm, who leads chairside emergency disconnection under the approved procedure, who accounts for everyone at the assembly point, and who helps patients who cannot walk. Assign fire-fighting only to those trained, and only with a clear escape route behind them.</p>
{{key:Ask what failed, what worked, who owns each fix, and how the next drill will show it changed.}}
"""),
    ],
    "debrief": ["""
<p><strong>The four connected patients.</strong> With the reverse osmosis pump alarming, treat the water supply as unverified. Follow your emergency procedure to end treatment safely; whether to return blood is a physician&rsquo;s call for each patient, depending on the circuit and the patient. Record the time and the delivered treatment for each, and make sure each has a plan for the next session.</p>
<p><strong>The four slots.</strong> Ask the attending nephrologists to rank the eight by clinical urgency. Mrs. Garcia, breathless after a missed session, needs urgent physician assessment now and may need the emergency department rather than a slot. Confirm acceptance by name at Meycauayan, then look for a second site in a different direction because Meycauayan shares your road. Escalate anyone you cannot place to the LDRRMO and the receiving hospital. Keep every row open until each has an outcome or a named owner.</p>
<p><strong>Restart.</strong> Not when the power returns. Only when the water system has been tested and released by the technical lead, the machines have been checked, staff and supplies are in place, and you have signed clinical restart. Then reconcile records, close the tracker, and schedule an after-action review and a repeat drill.</p>
"""],
    "skills": {"title": "Continuity activation and patient tracker",
               "intro": "Take part in the typhoon tabletop in the trainer guide as clinical lead, with role players for the receiving unit, transport, and a family member.",
               "items": [
                   ("Activates command and assigns clinical, logistics, communication, and tracking roles.", False),
                   ("Directs chairside procedures for connected patients according to the approved protocol.", True),
                   ("Obtains a physician&rsquo;s clinical priority for every displaced patient.", True),
                   ("Confirms receiving acceptance by patient name, not by number of slots.", True),
                   ("Identifies a shared dependency with the backup site and seeks a second site.", False),
                   ("Escalates any urgent patient who cannot be placed, with the escalation recorded.", True),
                   ("Accounts for every patient before stand-down.", True),
                   ("Holds restart until technical release and clinical authorization are both signed.", True),
                   ("Leads an after-action review that names owners, dates, and a repeat drill.", False),
               ],
               "placement": "Before the next typhoon season, test your call list, confirm two receiving agreements in different directions, and give every patient an emergency card. Record the percentage of numbers that connected."},
    "quiz": [
        ("Why does a disaster raise the risk for dialysis patients so quickly?",
         ["Machines break", "It lengthens the gap between sessions, during which potassium and fluid accumulate", "Staff panic", "Claims are delayed"], 1,
         "Risk is already highest after the usual two-day gap."),
        ("Before Hurricane Sandy, early dialysis was associated with what?",
         ["Higher mortality", "Fewer emergency visits and hospitalizations, and lower 30-day mortality", "No difference", "More infections"], 1,
         "Observational, but consistent with the mechanism."),
        ("What share of surveyed Manhattan patients missed dialysis after Sandy?",
         ["About 5%", "About 26%", "About 60%", "None"], 1,
         "A median of two sessions."),
        ("Your backup unit is on the same flood-prone road. What is the issue?",
         ["None", "A shared dependency: both may fail together", "It is too close", "It is too small"], 1,
         "Find a second site in a different direction."),
        ("The receiving unit says it has four chairs. Is that a confirmed transfer?",
         ["Yes", "No: confirm acceptance by patient name, time, staffing, transport, and handoff", "Yes if they are in the same city", "Only if PhilHealth agrees"], 1,
         "A chair is not an accepted patient."),
        ("Who sets each displaced patient&rsquo;s clinical priority?",
         ["The receptionist", "The attending nephrologist or physician on duty", "The order of the list", "The patient"], 1,
         "Priority is a clinical judgment."),
        ("Power is restored by generator. Can you restart?",
         ["Yes", "Not until water, machines, staffing, supplies, and records are verified and signed", "Yes for half the stations", "Only for urgent patients"], 1,
         "Power is one dependency of several."),
        ("When may you stand down?",
         ["When the rain stops", "When every patient on the tracker has an outcome or a named owner", "After four hours", "When the owner says so"], 1,
         "Account for everyone first."),
        ("What should a patient emergency card include?",
         ["Only the patient&rsquo;s name", "Diagnosis, access, dry weight, medicines, last results, and unit contacts", "The bill", "The owner&rsquo;s number"], 1,
         "It is the handoff when a patient arrives at a strange unit."),
        ("Which law sets the Philippine disaster coordination framework?",
         ["RA 10173", "RA 10121", "RA 9173", "RA 11463"], 1,
         "RA 10121, the Disaster Risk Reduction and Management Act."),
        ("Why keep an offline roster and contact list?",
         ["Tradition", "Power or network loss can disable the electronic system", "Inspectors prefer paper", "It is cheaper"], 1,
         "Protect it like any record."),
        ("What was found about post-traumatic stress after Katrina among hemodialysis patients?",
         ["None", "About 24% had symptoms, more if they missed three or more sessions", "All had symptoms", "Only staff were affected"], 1,
         "Missed sessions are psychological as well as physical harm."),
        ("A breathless patient who missed Tuesday calls during the flood. What first?",
         ["Add her to tomorrow&rsquo;s list", "Arrange urgent physician assessment or emergency department referral", "Tell her to wait", "Ask her to come anyway"], 1,
         "Urgent symptoms need urgent assessment, not a slot."),
        ("What should a receiving agreement settle about billing?",
         ["Nothing", "Who claims for the session, confirmed with the claims lead and PhilHealth", "The patient pays", "The receiving unit decides later"], 1,
         "Prevent duplicate claims and protect access."),
        ("What makes an after-action review useful?",
         ["A long report", "Owners, dates, and a repeat drill that tests the fix", "Blaming the weather", "A certificate"], 1,
         "Show the change in the next drill."),
    ],
    "terms": [("Continuity plan", "The plan that keeps dialysis going or moves it during disruption."),
              ("Dependency", "Anything the unit needs to run."),
              ("Shared dependency", "A dependency the backup site also relies on."),
              ("Incident command", "Temporary roles for managing an emergency."),
              ("Patient tracker", "A list of affected patients and their status until each has an outcome."),
              ("Stand-down", "Ending the emergency response."),
              ("LDRRMO", "Local Disaster Risk Reduction and Management Office."),
              ("Early dialysis", "An extra or advanced session before a forecast disaster.")],
    "readings": [("climate-extremes-kidney-care.html", "Nephrology in the era of climate extremes.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
