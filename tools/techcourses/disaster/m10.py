# -*- coding: utf-8 -*-
"""Disaster Preparedness and Response, Module 10: Keeping Everyone Dialyzed: Priority, Placement, Tracking.
Shortened sessions: Dr. Rivero's decision (blueprint decision 4), taught only under the six conditions in blueprint section 5."""

MODULE = {
    "image_alt": "A nurse on the phone in front of a whiteboard tracker with colored magnets while a physician reviews a laboratory sheet.",
    "objectives": [
        "Find every patient within 24 hours of a disruption and track each one on a board.",
        "Explain the medical priority roster: what goes into it and who sets it.",
        "State the six conditions under which shortened sessions may be used, and the evidence behind them.",
        "Place patients at receiving units with a complete handoff, and record every placement.",
    ],
    "big": """
{{plain:After a disaster, a dialysis unit is like a lifeboat with fewer seats than passengers. Somebody has to count everyone in the water, decide who comes aboard first, and wave down the other boats. Nobody is left without a plan, even if their seat is on another boat.}}
<p>The picture has a limit. In a lifeboat, the order is often first come, first served. In a dialysis unit, the order is set by medical need: the time since the last treatment, the last potassium, fluid status and symptoms. That judgment belongs to the attending nephrologist, never to whoever answers the phone. And unlike a lifeboat, a unit can shorten the trip for some passengers, but only under strict conditions.</p>
<p>Planning for this is what separates disasters with excess deaths from those without. After Hurricane Katrina, the storm was not significantly associated with mortality among patients from 94 clinics in adjusted models;[[dp_kutner2009]] after Hurricane Maria, many patients were dialyzed outside Puerto Rico and mortality did not change significantly.[[dp_rivera2022]] Both teams point to coordinated placement and tracking.</p>
{{cards:Key terms for this module|Tracking board::A board or list that shows where every patient is: reached, dialyzed elsewhere, not reached, in hospital.|Priority roster::The attending nephrologist&rsquo;s order for who dialyzes first when chairs, staff, water or power are short.|Shortened session::A session cut below the prescribed length because of a real shortage, by written order.|Receiving unit::Another unit that treats your patients when yours cannot.|Handoff::The written information sent with a patient so another unit can dialyze them safely.|Reconciliation::The final record of who was dialyzed where and when (Module 11).}}
""",
    "case": {"title": "Twelve chairs, forty patients", "html": """
<p>Two days after a typhoon, a 20-station unit in Tacloban has power from its generator but only enough treated water and staff for 12 chairs for one long shift. Forty patients are due. Two receiving units, one in Ormoc and one in Palo, can each take six patients tomorrow if transport is arranged.</p>
<p>The tracking board shows 31 patients reached, 4 dialyzed at a hospital, and 5 not reached. Among those reached are a man whose potassium was 6.9 mmol/L on his last session, a woman with breathlessness and a 4 kg gain, and a young man who feels well and dialyzed four days ago.</p>
""", "questions": ["Who decides who dialyzes today, and on what information?",
                  "Would shortened sessions help here, and under what conditions?",
                  "What goes with the patients sent to Ormoc and Palo?"]},
    "sections": [
        ("find", "Find every patient", "Find every patient within 24 hours", """
<p>The first job after any disruption is a count. The call-down (Module 3) becomes a tracking board, updated every few hours, with one row per patient. The 24-hour target is the unit&rsquo;s own measure of how well its plan works; no external standard is claimed.</p>
{{fig:dp10_find_every_patient}}
<div class="table-wrap"><table>
<thead><tr><th>Status</th><th>What to do next</th></tr></thead>
<tbody>
<tr><td>Reached</td><td>Confirm safety, symptoms and the next dialysis</td></tr>
<tr><td>Dialyzed elsewhere</td><td>Note the site, the date and the next plan</td></tr>
<tr><td>Not reached</td><td>Keep trying by phone and other contacts; the social worker, barangay health workers and the LDRRMO can help find people</td></tr>
<tr><td>In hospital</td><td>Confirm the location and coordinate care</td></tr>
</tbody></table></div>
<p>The board is a unit document holding personal data; keep it inside the unit and share only what each helper needs.[[dp_ra10173]] In Miyagi, Japan, a regional network built after the 2011 earthquake now shares hemodialysis reports (prescription, laboratory data, allergies) among participating units, partly as a disaster backup for moving patients.[[dp_ido2022]]</p>
"""),
        ("priority", "The priority roster", "Who dialyzes first", """
<p>When there are fewer sessions than patients, the attending nephrologist sets the order from four inputs: <strong>time since the last treatment, the last potassium, fluid status, and symptoms</strong> (with missed sessions folded into time since treatment). The charge nurse and the tracking board supply the facts; the nephrologist decides.</p>
{{fig:dp10_priority_roster}}
<ul>
<li><strong>First today:</strong> higher need now, such as a high potassium, breathlessness, a large weight gain, or the longest time since treatment.</li>
<li><strong>Next:</strong> needs dialysis soon.</li>
<li><strong>Can wait:</strong> stable, recently dialyzed; the emergency diet and a review, with a planned slot.</li>
</ul>
<p>The <a href="../guides/calc-dialysis-head-nurse-toolkit.html#c11">disaster triage list (Head Nurse toolkit, CALC-11)</a> helps organize the facts for the nephrologist; it does not make the decision. A patient&rsquo;s place on the list can change with a new symptom or a new laboratory result.</p>
"""),
        ("short", "Shortened sessions", "Shortened sessions: only when all six conditions hold", """
<p>Shortening sessions spreads limited capacity across more patients. It is a conditional option (Dr. Rivero&rsquo;s decision), never a routine prescription, and it is used only when all six conditions hold:</p>
{{fig:dp10_shortened_session_conditions}}
<ol>
<li><strong>A real shortage</strong> of chairs, staff, water or power, recorded by the Dialysis Clinical Head.</li>
<li><strong>A written order</strong> from the attending nephrologist for each patient or group.</li>
<li><strong>Time-limited,</strong> with a stated end date or review date.</li>
<li><strong>Not for patients the nephrologist marks as high risk</strong> (for example, a recent high potassium, fluid overload or symptoms); they keep their full session or move first to a receiving unit.</li>
<li><strong>Monitoring</strong> of potassium and fluid status while it lasts, with the emergency diet reinforced.</li>
<li><strong>A return to the full prescription</strong> as soon as capacity allows, recorded in the reconciliation (Module 11).</li>
</ol>
<p><strong>The evidence is thin.</strong> After the 2011 Great East Japan Earthquake, two units in Fukushima shortened sessions by 0.5 to 1 hour for a month, and laboratory findings in 90 patients did not worsen.[[dp_haga2013]] It was a small retrospective study. Say &ldquo;was not associated with worse laboratory findings in one small study,&rdquo; never &ldquo;is safe.&rdquo;</p>
{{key:Shortened sessions need all six conditions, a written order and an end date. High-risk patients keep full sessions or move first.}}
"""),
        ("place", "Placement and handoff", "Placing patients at receiving units", """
<p>A receiving unit can dialyze a patient safely only with the facts. Send a handoff with every patient, and confirm the place before the patient travels.</p>
{{fig:dp10_handoff_to_a_receiving_unit}}
<ol>
<li><strong>Confirm the receiving unit</strong> and the person who accepts the patient, by name.</li>
<li><strong>Send the handoff:</strong> the dialysis prescription, access type and side, last laboratory results (including potassium and hepatitis status), medicines, allergies, and dry weight.</li>
<li><strong>Arrange transport</strong> that is safe and arrives on time.</li>
<li><strong>Tell the patient and record the placement</strong> on the tracking board.</li>
</ol>
<p>After Hurricane Irma, 129 hemodialysis patients were evacuated from St. Thomas in the US Virgin Islands to San Juan, Puerto Rico, where local nephrologists and dialysis centers treated them; the officials&rsquo; report describes how dialysis, medical care, shelter, food and transport all had to be arranged together, and how the patients had to move again when Hurricane Maria approached.[[dp_aviles2021]] The continuity planner helps plan how many patients each receiving unit can take on which shifts.</p>
{{call:A patient not reached after 24 hours, a patient with symptoms who cannot reach any unit, or no receiving unit able to take a high-priority patient: tell the incident lead and the attending nephrologist at once. Follow your unit protocol, and always ask the attending nephrologist for guidance.}}
<div class="alert alert-amber"><div class="alert-icon">🧒</div><div class="alert-body"><h4>Units that dialyze children</h4><p>Few units can dialyze small children, so pediatric receiving units are named in advance. The pediatric nephrologist sets a weight-based emergency diet and the child&rsquo;s priority, and the handoff includes the child&rsquo;s weight, circuit and blood-line size, and the caregiver&rsquo;s contact.</p></div></div>
"""),
    ],
    "debrief": ["""
<p><strong>Who decides.</strong> The attending nephrologist, from the tracking board and each patient&rsquo;s time since treatment, last potassium, fluid status and symptoms. The man with a potassium of 6.9 mmol/L and the breathless woman with a 4 kg gain are likely first today; the young man who feels well and dialyzed four days ago is also overdue, so his place depends on the numbers for everyone else, and the nephrologist may send him to a receiving unit tomorrow.</p>
<p><strong>Shortened sessions.</strong> Possibly, if all six conditions hold: the shortage recorded by the Dialysis Clinical Head (water and staff for 12 chairs), a written order per patient or group, an end date, high-risk patients (the two above) excluded, potassium and fluid monitoring, and a return to full prescriptions recorded. It is one option among several, beside the receiving units.</p>
<p><strong>The handoff.</strong> For each of the twelve going to Ormoc and Palo: a named accepting person, the prescription, access type and side, last laboratory results with potassium and hepatitis status, medicines, allergies and dry weight; safe transport; the patient told; the placement on the board. The five not reached stay on the board until found.</p>
"""],
    "skills": {"title": "Tracking, priority and placement",
               "intro": "In a tabletop (the &ldquo;twelve chairs&rdquo; scenario on the practice page) or after a real disruption.",
               "items": [
                   ("Sets up a tracking board with the four statuses and updates it.", False),
                   ("Gathers time since last treatment, last potassium, fluid status and symptoms for the nephrologist without setting the priority.", True),
                   ("States all six conditions for shortened sessions.", True),
                   ("Excludes patients marked high risk from shortened sessions.", True),
                   ("Writes a complete handoff: prescription, access, last laboratory results with hepatitis status, medicines, allergies, dry weight.", True),
                   ("Confirms the accepting person by name before the patient travels and records the placement.", False),
               ],
               "placement": "Check that your unit&rsquo;s receiving-unit agreements list a named contact and the handoff they expect."},
    "terms": [("Tracking board", "A list showing where every patient is after a disruption."),
              ("Priority roster", "The nephrologist&rsquo;s order for who dialyzes first."),
              ("Shortened session", "A session cut below the prescription by written order during a real shortage."),
              ("Handoff", "The information sent with a patient to another unit."),
              ("Receiving unit", "Another unit that treats your patients when yours cannot.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "What patients are told about backup units.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c11", "calc-dialysis-continuity-planner.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("dp_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["10"])
