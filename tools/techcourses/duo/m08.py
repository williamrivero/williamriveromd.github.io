# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 8: Safe capacity and the operating model. Written for this course from published sources."""

MODULE = {
    "image_alt": "An overhead miniature model of a twelve-station dialysis floor, nine stations lit and active, three dimmed.",
    "objectives": [
        "Calculate physical and safely staffed capacity in station-sessions a week.",
        "Explain why the narrowest resource, not the number of chairs, sets safe capacity.",
        "Hold make-up slots and protect the long-gap day in the schedule.",
        "List the outside services a unit cannot run without and secure each one in writing.",
    ],
    "big": """
{{plain:Capacity is like a pipe made of several sections. Water flows only as fast as the narrowest section allows. Twelve chairs and nine nurses-worth of safe coverage give you a nine-chair pipe.}}
<p>The picture has a limit. A pipe does not get tired. A nurse covering too many stations does, and the narrowing shows up as missed checks, late alarms, and mistakes, not as a slower flow. That is why capacity must be planned from the people and systems that make treatment safe.</p>
{{cards:Key terms for this module|Physical capacity::Usable stations &times; shifts &times; operating days.|Safely staffed capacity::The stations your cleared staff can safely cover, &times; shifts &times; days.|Make-up slot::A chair kept free for a patient who missed a session or needs an extra one.|Dependency::An outside service the unit cannot treat safely without, such as a hospital for emergencies.}}
<p>Your work is to plan from the narrowest gate, keep slack on purpose, and secure every dependency before you accept a patient who needs it.</p>
""",
    "case": {"title": "Sixty referrals", "html": """
<p>A unit in Calamba, Laguna, has 12 stations, one held for repair, three shifts a day, six days a week. The head nurse can safely staff nine stations per shift with the cleared nurses she has. Fifty patients dialyze now. A hospital wants to refer ten more within a month, and the owner, Mr. Edwin Sy, says, &ldquo;We have the chairs.&rdquo;</p>
""", "questions": ["What is the unit&rsquo;s safe capacity?", "How many patients can it support at three sessions a week?", "What must be true before the ten are accepted?"]},
    "sections": [
        ("stations", "Station-sessions", "From chairs to station-sessions", """
{{fig:duo08a}}
<p>Count capacity in station-sessions a week. Eleven usable stations &times; three shifts &times; six days gives 198 station-sessions. That is <strong>physical</strong> capacity: what the chairs and machines could do.</p>
<p>Now apply the gates. If cleared staff can safely cover nine stations per shift, safely staffed capacity is 9 &times; 3 &times; 6 = 162 station-sessions. At three sessions per patient per week, that supports 54 patients, with no slack. The DOH limit of four stations per nurse is a ceiling, not a target; acuity, breaks, and absence lower the real number.[[doh2012]]</p>
{{key:Plan from the narrowest gate. Physical capacity is the number you cannot exceed, not the one you plan to.}}
"""),
        ("staffed", "Slack", "Slack is a safety control", """
<p>A unit at 100% of safe capacity cannot reschedule a missed session, absorb a new start from the hospital, or cover a sick nurse. Rescheduling a missed treatment was associated with fewer hospitalizations than leaving it missed in a large United States provider.[[uom_cohen2020]] Keep a planned share of station-sessions free each week for make-up sessions, and protect them from routine booking.</p>
<p>The schedule also has a shape. The day after the long weekend gap carries the highest risk, as Module 2 explained.[[dch_foley2011]] Do not build an operating model that lengthens gaps to save a shift.</p>
{{key:Keep make-up slots free on purpose. They are not empty chairs; they are a safety reserve.}}
"""),
        ("gap", "Growth", "Growing safely", """
<p>To accept more patients, widen the narrowest gate first. If staffing limits capacity, hire and clear nurses before you accept referrals. If stations limit it, add stations through the license amendment in Module 3. If water limits it, the technical lead must confirm the system can produce enough for more sessions.</p>
<p>Use the capacity calculator with your own numbers, and show the board the physical figure, the staffed figure, the make-up reserve, and the census side by side.</p>
{{key:Widen the narrowest gate before you accept the next patient.}}
"""),
        ("dependencies", "Dependencies", "The services a unit cannot run without", """
{{fig:duo08b}}
<p>A dialysis unit leans on outside services every day. Each needs a written agreement, a named contact, and a backup.</p>
<div class="table-wrap"><table>
<thead><tr><th>Dependency</th><th>Why it matters</th><th>What to secure</th></tr></thead>
<tbody>
<tr><td>Hospital</td><td>Emergencies, admissions, and acute dialysis</td><td>Transfer agreement and a direct contact</td></tr>
<tr><td>Laboratory</td><td>Monthly tests and urgent potassium results</td><td>Turnaround times and critical-value calls</td></tr>
<tr><td>Ambulance</td><td>Transfers during a session</td><td>Response arrangement and contact</td></tr>
<tr><td>Access surgeon</td><td>Fistulas, grafts, and rescue of a failing access</td><td>Referral pathway and timelines</td></tr>
<tr><td>Water testing laboratory</td><td>Chemical and microbiological results</td><td>Schedule and chain of custody</td></tr>
<tr><td>Machine service</td><td>Repairs and preventive maintenance</td><td>Response time and loan machines</td></tr>
<tr><td>Power and water utilities</td><td>Every session</td><td>Generator, fuel, and water storage plan</td></tr>
</tbody></table></div>
{{key:No agreement, no patient who depends on it.}}
"""),
    ],
    "debrief": ["""
<p><strong>Safe capacity.</strong> Physical capacity is 198 station-sessions a week; safely staffed capacity is 162. The limiting resource is staffing.</p>
<p><strong>Patients supported.</strong> 162 &divide; 3 = 54, with no make-up slack. With 50 patients, the unit has room for perhaps two or three more while keeping some make-up slots, not ten.</p>
<p><strong>Before accepting ten.</strong> Hire and clear enough nurses to staff all eleven stations, repair the held station, confirm water capacity with the technical lead, and keep a make-up reserve. Then accept referrals in stages.</p>
"""],
    "skills": {"title": "Safe capacity sheet and dependency agreements",
               "intro": "Complete a safe capacity sheet for a real or fictional unit and list its dependency agreements.",
               "items": [("Calculates physical and safely staffed station-sessions.", False),
                         ("Names the limiting resource.", False),
                         ("Holds a stated make-up reserve out of routine booking.", True),
                         ("Refuses referrals beyond safely staffed capacity.", True),
                         ("Lists every dependency with an agreement, a contact, and a backup.", False),
                         ("Shows physical, staffed, reserve, and census side by side for the board.", False)],
               "placement": "With the head nurse, compare last month&rsquo;s schedule with safely staffed capacity."},
    "quiz": [
        ("Eleven usable stations, three shifts, six days. What is physical capacity?",
         ["66", "198", "162", "36"],
         1, "11 &times; 3 &times; 6 = 198 station-sessions a week."),
        ("Cleared staff can cover nine stations per shift. Safely staffed capacity is:",
         ["198", "162", "54", "27"],
         1, "9 &times; 3 &times; 6 = 162 station-sessions a week."),
        ("How many patients at three sessions a week can 162 station-sessions support with no slack?",
         ["54", "48", "60", "81"],
         0, "162 &divide; 3 = 54."),
        ("Why keep make-up slots free?",
         ["To reduce cleaning", "So a missed session can be rescheduled instead of lengthening the gap", "To save electricity", "To lower staff numbers"],
         1, "Rescheduling missed sessions is associated with fewer hospitalizations."),
        ("Staffing is the narrowest gate. What should happen before more referrals are accepted?",
         ["Buy more chairs", "Hire and clear more nurses", "Extend each session", "Raise prices"],
         1, "Widen the narrowest gate first."),
        ("Which outside service needs a written agreement before patients who need it are accepted?",
         ["The hospital for emergencies", "A catering service", "A uniform supplier", "A florist"],
         0, "Emergencies and admissions depend on a hospital agreement and a contact."),
    ],
    "terms": [("Census", "The number of patients regularly dialyzing at the unit.")],
    "readings": [],
    "calcs": ["calc-dialysis-owner-toolkit.html#c3", "calc-dialysis-clinical-head-toolkit.html#c1"],
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
