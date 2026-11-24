# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 13: Downtime, Typhoons, and Getting Through the Day. Written for this series from published sources."""

MODULE = {
    "image_alt": "A charge nurse on the phone at the unit desk during a heavy rainstorm with a printed patient list and a flashlight.",
    "objectives": [
        "Act in the first fifteen minutes of a power, water, or system failure.",
        "Bring patients off safely when machines stop.",
        "Keep paper records when the electronic system is down, and enter them correctly later.",
        "Prepare the facts the physician needs to decide who is dialyzed first.",
        "Give patients clear instructions until their next session, and restart only on signed releases.",
    ],
    "big": """
{{plain:A patient on dialysis has a deadline measured in days, not weeks. A typhoon that closes a unit for three days can be life-threatening for someone whose kidneys do nothing.}}
<p>The head nurse prepares the unit before the typhoon season (Head Nurse Module 12): the contact tree, the generator, the downtime forms, the partner units. The charge nurse leads on the day the lights go out, for patients with chronic kidney disease (CKD) who cannot simply skip a session. That day rarely matches the plan exactly, so she needs the principles, not only the checklist.</p>
{{cards:Key terms for this module|Downtime::A period when power, water, or the electronic record is not available.|Hand-cranking::Returning blood manually when a machine stops, per the machine&rsquo;s instructions.|Downtime board::A paper list of every patient, their status, and the plan.|Late entry::A record written after the event, labeled late and dated with the true event time.|Contact tree::The order in which staff and patients are called.}}
""",
    "case": {"title": "Brownout at 8:10", "html": """
<p>A typhoon signal was raised overnight. At 8:10 the power fails. The generator starts, but the reverse osmosis unit and four machines do not restart. Fourteen patients are connected. The electronic record is down.</p>
<p>The charge nurse, Nurse Lorna Garcia, has three nurses and an assistant. Rain is coming through the window by the waiting area.</p>
""", "questions": ["What happens to the fourteen patients in the first fifteen minutes?",
                  "Who decides who is rescheduled first?",
                  "What is written, and where?"]},
    "sections": [
        ("evidence", "Why it matters", "Why disruption is dangerous", """
<p>In a United States cohort, exposure to a tropical storm was associated with a 55% higher risk of a missed session in the following week.[[hn_remigio2023]] After Hurricane Sandy, 26.3% of 357 surveyed patients missed dialysis, two thirds dialyzed somewhere other than their usual unit, and fewer than half carried a detailed medication list.[[hn_murakami2015]] A coordinated network can hold: in 94 clinics affected by Hurricane Katrina, the storm was not associated with excess mortality once other factors were accounted for.[[hn_kutner2009]] Preparation and coordination make the difference.</p>
"""),
        ("first15", "The first fifteen minutes", "The first fifteen minutes", """
{{fig:cn13_board}}
{{flow:First fifteen minutes|Check every patient::Who is still dialyzing, who has stopped, who looks unwell.|Disconnect safely where machines stopped::Return blood by hand-cranking or disconnect per the protocol and the machine&rsquo;s instructions; clamp; secure the access.|Confirm water before continuing::Machines on generator continue only if the technician confirms the water supply is safe.|Call::The head nurse, the technician, the biomedical lead, and the physician on duty.|Start the downtime board::Every patient, minutes delivered, fluid removed, status, plan.}}
<p>Patients before phones. A phone call can wait thirty seconds; a stopped machine with blood in the circuit cannot.</p>
"""),
        ("paper", "Paper records", "Paper when the system fails", """
<p>Keep downtime forms ready before the season: patient list, vital signs, fluid removed, time on the machine, medicines given, events. When the electronic record returns, enter the information as late entries with the true time of each event, labeled late. Do not back-date entries to make them look contemporaneous.</p>
"""),
        ("priority", "Who first", "Prioritizing with the physician", """
<p>When there are fewer chairs than patients, the attending nephrologist decides the order. The charge nurse supplies the facts: minutes delivered today, fluid removed, latest potassium, weight gain, symptoms, missed sessions this week, and whether the patient still passes urine.</p>
{{fig:cn13_priority}}
<p>Patients who usually cannot wait: high potassium, large weight gain, breathlessness, a missed session this week, and no urine output. The list is facts; the choice is the physician&rsquo;s.</p>
"""),
        ("patients", "Patients and families", "What patients need to hear", """
<p>Tell patients plainly what happened, when they will be dialyzed, the diet and fluid rules until then (less salt, less fluid, avoid high-potassium foods), and where to go if they become breathless. Make sure each one leaves with a phone number and, ideally, a medication list. After Hurricane Sandy, fewer than half of patients had one.[[hn_murakami2015]]</p>
{{scene:The patient who cannot reach the unit tomorrow|<p>Mrs. Elena Bautista lives across a river that floods. She says the road will be closed tomorrow. The charge nurse and the head nurse call the partner unit on her side of the river, send a transfer summary ahead (Module 16), and confirm a slot. Mrs. Bautista leaves with the address, the phone number, and her medication list in a plastic sleeve.</p>}}
"""),
        ("restart", "Restart", "Restart and the record", """
<p>The same rule as Module 11: restart only on signed releases for water and machines. Then write the day down: what failed, when, what was done, who decided, and which patients were moved. The head nurse uses this record to improve the plan before the next typhoon.</p>
"""),
    ],
    "debrief": ["""
<p><strong>The first fifteen minutes.</strong> Lorna and her team check every patient. The four whose machines stopped are brought off safely per protocol. The machines on generator continue only after the technician confirms the water supply; with the reverse osmosis unit down, he does not, so the remaining sessions are ended safely too. She calls the head nurse, technician, biomedical lead, and physician on duty, and starts the downtime board.</p>
<p><strong>Who decides.</strong> Fourteen patients averaged 1 hour 40 minutes. The afternoon has six chairs at the partner unit. Lorna lists each patient&rsquo;s time delivered, fluid removed, latest potassium, weight gain, symptoms, and missed sessions (Head Nurse toolkit #c11). The attending chooses six who cannot wait (two with potassium above 6, one breathless, three with gains above 4 kilograms). The other eight return the next morning with diet and fluid instructions and a phone number.</p>
<p><strong>What is written.</strong> Paper downtime forms for every patient, entered later as labeled late entries with true event times, and an event summary for the head nurse.</p>
"""],
    "skills": {"title": "Leading through downtime",
               "intro": "A tabletop exercise with the head nurse and the technician: a power failure at 8:10 with fourteen patients connected, followed by a flooded-road scenario.",
               "items": [
                   ("Checks every patient before making calls.", True),
                   ("Directs safe disconnection for stopped machines per protocol.", True),
                   ("Continues sessions on generator only with confirmed water.", True),
                   ("Starts and keeps a downtime board.", False),
                   ("Prepares a prioritization list of facts for the physician.", False),
                   ("Enters downtime records as labeled late entries with true event times.", True),
                   ("Gives each patient instructions, a phone number, and a medication list.", False),
                   ("Requires signed releases before restart.", True),
               ],
               "placement": "Before the next typhoon season, check that downtime forms, flashlights, and the contact tree are where the plan says, and run one tabletop with your team."},
    "quiz": [
        ("What is the first action when machines stop?",
         ["Phone everyone", "Check patients and disconnect safely", "Wait", "Restart the machines"], 1,
         "Patients before phones."),
        ("The generator is on but the water system is off. What do you do?",
         ["Continue all sessions", "No new connections; continue only on confirmed water", "Use tap water", "Ignore it"], 1,
         "Water must be confirmed safe."),
        ("How are downtime records entered later?",
         ["Back-dated to look normal", "Labeled late, with the true event time", "Not at all", "By the head nurse only"], 1,
         "Honest late entries."),
        ("Who chooses which patients are dialyzed first?",
         ["The charge nurse", "The attending nephrologist", "The patients", "The technician"], 1,
         "The charge nurse supplies the facts."),
        ("After Hurricane Sandy, about what share of surveyed patients missed dialysis?",
         ["2%", "26%", "75%", "100%"], 1,
         "26.3% of 357 patients."),
        ("Which patients usually cannot wait?",
         ["Stable, small gains", "High potassium, large gains, breathlessness, missed sessions, no urine", "Those who live nearby", "Alphabetical order"], 1,
         "The list is facts; the physician chooses."),
        ("What does restart require?",
         ["Power coming back", "Signed releases", "The physician&rsquo;s call only", "A patient request"], 1,
         "The same rule as Module 11."),
        ("Patients sent home need:",
         ["Nothing", "Diet and fluid rules, when to return, where to go if breathless, a phone number, a medication list", "Only a phone number", "A refund"], 1,
         "Fewer than half had a medication list after Sandy."),
        ("Exposure to a tropical storm in the United States cohort was associated with:",
         ["Fewer missed sessions", "A 55% higher risk of a missed session in the next week", "No change", "Lower mortality"], 1,
         "Disruption reaches patients quickly."),
        ("In the Katrina study, what made the difference?",
         ["Luck", "Coordination and preparation across the network", "Weather", "Nothing"], 1,
         "The storm was not associated with excess mortality in adjusted models."),
        ("What is hand-cranking?",
         ["Restarting the generator", "Returning blood manually when a machine stops, per its instructions", "Cleaning the machine", "Turning off alarms"], 1,
         "Done per the machine&rsquo;s instructions."),
        ("What goes on the downtime board?",
         ["Staff birthdays", "Every patient, minutes delivered, fluid removed, status, and plan", "Only names", "Nothing"], 1,
         "The shift&rsquo;s shared picture without electricity."),
        ("A patient&rsquo;s road will be closed tomorrow. What do you do?",
         ["Tell her to come anyway", "Arrange a partner unit with the head nurse and send a transfer summary", "Nothing", "Shorten her next session"], 1,
         "The summary travels with the patient."),
        ("Why keep downtime forms ready before the season?",
         ["To impress inspectors", "So the record continues when the system fails", "For PhilHealth only", "No reason"], 1,
         "There is no time to design forms during a brownout."),
        ("Who prepares the unit before the season, and who leads on the day?",
         ["Both the charge nurse", "The head nurse prepares; the charge nurse leads on the day", "Only the technician", "The physician"], 1,
         "Different horizons, shared plan."),
    ],
    "terms": [("Downtime", "A period without power, water, or the electronic record."),
              ("Hand-cranking", "Returning blood manually when a machine stops."),
              ("Downtime board", "A paper list of every patient, status, and plan."),
              ("Late entry", "A record written after the event, labeled late with the true time."),
              ("Contact tree", "The order in which staff and patients are called.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "Preparing for typhoons and floods on dialysis."),
                 ("climate-extremes-kidney-care.html", "Kidney care in an era of climate extremes."),
                 ("travel-dialysis-ckd.html", "Dialyzing away from your usual unit.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c11", "calc-dialysis-continuity-planner.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
