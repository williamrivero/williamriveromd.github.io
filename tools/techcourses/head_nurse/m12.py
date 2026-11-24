# -*- coding: utf-8 -*-
"""Dialysis Head Nurse, Module 12: Keeping Dialysis Running Through a Disaster. Written for this series from published sources."""

MODULE = {
    "image_alt": "A head nurse on the phone at a dialysis unit desk during heavy rain, a printed patient list and a map in front of her.",
    "objectives": [
        "Explain why a dialysis patient&rsquo;s deadline in a disaster is counted in days.",
        "Summarize what the evidence from hurricanes and tropical storms shows, and what it does not.",
        "Prepare before the typhoon season: call lists, emergency cards, receiving agreements, and a disaster diet.",
        "Give the physician the facts needed to prioritize the roster, and close every transfer.",
        "Restart only through five signed gates, then reconcile who was missed.",
        "Turn a drill into a 90-day plan.",
    ],
    "big": """
{{plain:Most people can go a week without their usual medical care during a storm. A patient on hemodialysis has a deadline counted in days. Every day without treatment adds potassium and fluid, and the risk climbs fastest after the third day. Your plan is a race between that clock and the time it takes to find a working chair, a working road, and a working phone line.}}
<p>The picture has a limit. The clock does not run at the same speed for everyone. A patient who ate canned relief food and drank freely runs faster. The physician decides who goes first. You make sure the physician has the facts.</p>
{{fig:hn12_clock}}
{{cards:Key terms for this module|Receiving unit::Another dialysis unit that agrees to treat your patients when yours cannot.|Emergency card::A wallet card with the facts a strange unit needs to dialyze the patient safely.|Disaster diet::A short-term plan that limits potassium, salt, and fluid more tightly than usual, to buy time.|Incident command::A simple structure that names who leads, who communicates, and who handles logistics during a disaster.|Call-down drill::A test of the call list, done before it is needed.|Restart gates::Five signed checks before the unit treats patients again.}}
""",
    "case": {"title": "Signal No. 3", "html": """
<p>A strong typhoon makes landfall in the afternoon. At 2:10, the clinic loses power. The generator runs, but at 2:40 the water supply stops. Two patients, Mrs. Corazon Lim and Mr. Edgar Pineda, are on the machines. Fifteen more are scheduled for the evening and next morning.</p>
<p>Your planned receiving unit, in the next town, says it can take six patients tomorrow. The highway to it is flooded at one point. Three of the fifteen patients do not answer their phones.</p>
""", "questions": ["What happens to the two patients on the machines?",
                  "How are the fifteen prioritized, and by whom?",
                  "When can the unit restart, and what do you check afterward?"]},
    "sections": [
        ("clock", "The clock", "What the clock is measuring", """
<p>Potassium rises roughly with intake and time. Fluid builds up with every glass of water. Both are worse after a long gap.[[hn_foley2011]] In a disaster, intake changes too. Relief food is often canned, salty, and high in potassium, while bottled water may be the only safe drink. The result is overload and high potassium arriving together, often in a patient who cannot reach a phone. Earthquakes add a second wave: crush injuries cause sudden kidney injury and high potassium in people who were never on dialysis.[[hn_yoo2025]]</p>
<p>A disaster diet buys time. It is a bridge measured in days, not a substitute for dialysis. Patients should have it in writing from the dietitian and nephrologist before the season, not on the day.</p>
{{scene:Relief goods and two missed sessions|<p>After a typhoon, Mr. Andres Marquez, 62, cannot reach the unit for four days because the bridge to his barangay is closed. The relief packs his family receives contain rice, canned sardines, and instant noodles, and neighbors share bananas from their yard. He drinks bottled water whenever he is thirsty.</p>
<p>When he arrives on the fifth day, he is 5 kilograms above his dry weight, breathless, and weak, and his potassium is dangerously high. His relief food, which kept his family fed, was close to the worst diet for him: salt that drove thirst and fluid gain, and potassium from the canned fish and bananas. A written disaster diet given to him in June, telling him which relief foods to avoid and how much to drink, could have stretched those four days more safely. It would not have replaced dialysis, but it might have bought him time.</p>}}
"""),
        ("evidence", "What the evidence shows", "What hurricanes and storms have taught", """
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>Data</th><th>Strength</th></tr></thead>
<tbody>
<tr><td>Storms cause missed sessions</td><td>Tropical storm exposure was associated with 55% higher risk of a missed session over the following week (rate ratio 1.55; 95% confidence interval 1.22 to 1.98)[[hn_remigio2023]]</td><td>Cohort</td></tr>
<tr><td>Even prepared systems miss</td><td>After Hurricane Sandy, 26.3% of 357 surveyed patients missed dialysis, a median of two sessions. 66.1% dialyzed somewhere other than their own unit. Only 44.3% carried a detailed medication list[[hn_murakami2015]]</td><td>Survey</td></tr>
<tr><td>Preparation helps</td><td>Dialysis-specific preparedness was associated with fewer missed sessions (rate ratio 0.91)[[hn_murakami2015]]</td><td>Survey</td></tr>
<tr><td>A coordinated network can hold</td><td>In 94 clinics affected by Hurricane Katrina, the storm was not associated with excess mortality in adjusted models[[hn_kutner2009]]</td><td>Cohort</td></tr>
<tr><td>What works</td><td>A review of tropical cyclones grouped the lessons into mitigation, preparedness, response, and recovery[[hn_yang2024]]</td><td>Scoping review</td></tr>
</tbody></table></div>
<p>The Katrina finding is reassuring only because providers moved patients quickly. It is evidence that planning works, not that disasters are harmless. No trial has tested any disaster intervention.</p>
"""),
        ("before", "Before the season", "What to do before the typhoon season", """
{{cards:Before the season|Call list::Two numbers for each patient, a named family contact, the barangay, and the usual route to the unit. Test it with a call-down drill.|Emergency card::Carried at all times. Name, diagnosis, access, dry weight, last potassium and hemoglobin, medicines, PhilHealth status, unit contacts, and the alternate unit.|Disaster diet::Written by the dietitian, with a three-day medicine supply where the physician agrees.|Receiving agreements::At least two units in different directions, each with a named contact and a backup number.|Downtime kit::Paper forms, a printed patient list kept off-site, generator and water storage checks with facilities staff.}}
{{fig:hn12_card}}
<p>When a warning is issued, ask the nephrologist about moving sessions earlier so patients dialyze before landfall. Call every patient. Find out who will not be able to reach the unit.</p>
{{scene:Twenty-three wrong numbers|<p>In May, the unit runs a call-down drill. Each nurse calls her assigned patients and asks one question: &ldquo;If the unit closed tomorrow, where would you go?&rdquo;</p>
<p>Of 95 patients, 23 numbers are wrong or out of service, mostly because patients changed SIM cards. Eleven patients cannot name the alternate unit. The drill takes one afternoon. The fixes take two weeks: a second number and a family contact for each patient, emergency cards issued with the alternate unit printed on them, and a rule that phone numbers are confirmed at every monthly review. When the real typhoon comes in August, every patient is reached within three hours.</p>}}
"""),
        ("during", "During disruption", "Prioritizing and placing patients", """
<p>Activate incident command. For patients on the machines, follow the shutdown procedure. Whether blood is returned follows the protocol and the physician&rsquo;s direction (Module 7).</p>
<p>Give the physician, for each scheduled patient: the date of the last session, the last potassium, fluid status and symptoms, and any recent missed session. The physician decides the order. Patients furthest from their last session, and those with symptoms or a high potassium, usually go first.</p>
{{formula:<strong>Capacity gap</strong> = patients needing a session in the next 48 hours &minus; confirmed receiving slots.<br>15 &minus; 6 = 9. A gap above zero means calling the next receiving unit now.}}
{{flow:Closing each transfer|Accepted::A named person at the receiving unit accepts this patient.|Handoff::The emergency card and a summary are sent.|Transport::A route that is open, and a ride confirmed.|Told::The patient and family know where, when, and how.|Logged::Placement, time, and the accepting person&rsquo;s name in a secure log.}}
<p>Keep a fallback for patients who cannot be reached: barangay officials, local emergency services, and a second attempt by a named person at a set time.</p>
{{call:Stop and call the attending nephrologist and the clinical head as soon as the unit cannot treat scheduled patients. The physician prioritizes the roster. Follow your unit&rsquo;s disaster protocol while you call.}}
"""),
        ("restart", "Restart", "Restart through five signed gates", """
{{fig:hn12_restart}}
{{cards:Five restart gates|Building::Safe to occupy, power stable.|Staff::Qualified nurses and ACLS cover (Module 8).|Water and machines::Tested and released after the outage (Module 6).|Supplies and cart::Stock and emergency cart checked.|Records::Recovered, and paper downtime records entered.}}
<p>Then reconcile. Who was dialyzed where? Who was missed? Who needs an extra session or a laboratory test? Close the incident only when every patient on the roster has been accounted for.</p>
{{scene:Two names not yet accounted for|<p>Two days after the typhoon, the unit restarts. The reconciliation list shows that 93 of 95 patients were dialyzed somewhere or are confirmed safe. Two names have no entry.</p>
<p>The incident stays open. A named nurse calls both families. The first patient was dialyzed at a hospital emergency room and is well. The second has not been dialyzed for five days and is too weak to travel. The barangay officials help arrange transport, and she is dialyzed that afternoon. If the unit had closed the incident on the day it restarted, she would have been missed. The roster is the list of people, and it is finished only when every name is accounted for.</p>}}
{{key:A restart is a signed decision, not a feeling that things are back to normal.}}
<p><strong>The next 90 days.</strong> By day 30, list the gaps from the event or drill with owners, test the call list, and secure two written receiving agreements. By day 60, test one improvement with a PDSA cycle (Module 11) and issue emergency cards to at least half the patients. By day 90, review the measures with the clinical head, finish the cards, and schedule the next drill.</p>
"""),
    ],
    "debrief": ["""
<p><strong>The two on the machines.</strong> With water gone, the machines cannot continue safely for long. Follow the shutdown procedure for Mrs. Lim and Mr. Pineda. Ask the physician on duty whether to return their blood. If the circuits are intact and nothing suggests the fluid caused harm, return is usually part of the procedure. Record how much treatment each received, because they may need another session sooner.</p>
<p><strong>Prioritizing the fifteen.</strong> Call the attending nephrologist and the clinical head. Give them, for each patient, the last session date, last potassium, fluid and symptoms, and any recent missed session. The physician decides the order. Six go to the planned unit tomorrow by an open route. Call the second receiving unit for the other nine now, not tomorrow. For the three who do not answer, ask a named person to try again at a set time and contact their barangay. Log every placement with the name of the person who accepted the patient.</p>
<p><strong>Restart and afterward.</strong> The unit restarts only when the five gates are signed: building, staff, water and machines released, supplies and cart, records. Then reconcile all seventeen patients. Who dialyzed, where, when? Who needs an extra session? Who still has not been reached? Turn what you learned into the 90-day plan.</p>
"""],
    "skills": {"title": "Typhoon tabletop",
               "intro": "Lead a tabletop exercise with a mock roster, a power and water outage, and a receiving unit that becomes unavailable halfway through.",
               "items": [
                   ("Follows the shutdown procedure for connected patients and asks the physician about blood return.", True),
                   ("Calls the attending nephrologist and the clinical head promptly.", True),
                   ("Gives the physician the facts needed to prioritize, without deciding the order herself.", True),
                   ("Calculates the capacity gap and calls a second receiving unit.", True),
                   ("Closes each transfer with a named accepting person, handoff, transport, and patient notice.", True),
                   ("Sets a fallback for patients who cannot be reached.", False),
                   ("Keeps a secure placement log.", False),
                   ("Names the five restart gates and does not restart without them.", True),
                   ("Describes how every patient will be reconciled afterward.", False),
                   ("Outlines a 30, 60, and 90-day plan from the exercise.", False),
               ],
               "placement": "Before the next typhoon season, run a call-down drill of your full patient list. Record how many were reached within two hours, and fix every wrong number."},
    "quiz": [
        ("Why is a dialysis patient&rsquo;s deadline in a disaster counted in days?",
         ["Dialysis machines need daily servicing", "Potassium and fluid build up each day without treatment", "PhilHealth limits sessions", "Patients run out of medicine"], 1,
         "Risk rises fastest after the third day."),
        ("Why can relief food make things worse?",
         ["It is too sweet", "Canned food is often salty and high in potassium", "It contains no protein", "It is always spoiled"], 1,
         "Salt drives fluid gain and potassium drives arrhythmia."),
        ("What is a disaster diet?",
         ["A permanent new diet", "A short-term, stricter limit on potassium, salt, and fluid to buy days", "Fasting until dialysis", "A high-protein diet"], 1,
         "It is a bridge, not a substitute for dialysis."),
        ("After Hurricane Sandy, what fraction of surveyed patients carried a detailed medication list?",
         ["About 10%", "About 44%", "About 75%", "All of them"], 1,
         "Emergency cards close this gap."),
        ("What did the Hurricane Katrina study show?",
         ["Disasters are harmless", "A coordinated response that moved patients quickly prevented excess deaths", "Planning is unnecessary", "Patients should stay home"], 1,
         "The finding is evidence that planning works."),
        ("Tropical storm exposure was associated with what change in missed sessions?",
         ["No change", "About 55% higher risk over the following week", "Lower risk", "Higher risk only in winter"], 1,
         "Plan for it every rainy season."),
        ("Who decides which patients are placed first?",
         ["The head nurse", "The physician, using the facts you provide", "The patients", "The receiving unit"], 1,
         "It is a medical decision."),
        ("Which facts help the physician prioritize most?",
         ["Alphabetical order", "Days since the last session, last potassium, fluid status, and symptoms", "Years with the unit", "Who called first"], 1,
         "Risk builds with time, potassium, and fluid."),
        ("Fifteen patients need a session in 48 hours and six slots are confirmed. What is the capacity gap?",
         ["6", "9", "15", "21"], 1,
         "15 &minus; 6 = 9. Call the next receiving unit now."),
        ("What closes a patient transfer?",
         ["Publishing the receiving address", "A named acceptor, a handoff, transport, notice to the patient, and a log entry", "Marking the patient transferred", "Ending the incident call"], 1,
         "Acceptance and continuity are verified for each person."),
        ("What should receiving agreements include?",
         ["A single unit nearby", "At least two units in different directions, each with a named contact and backup number", "A verbal promise", "Only the hospital emergency room"], 1,
         "One road may be closed."),
        ("Which is one of the five restart gates?",
         ["A press release", "Water and machines tested and released", "A full roster for the month", "A new budget"], 1,
         "The others are building, staff, supplies and cart, and records."),
        ("When is a disaster incident closed?",
         ["When power returns", "When every patient on the roster has been accounted for", "After 24 hours", "When the storm signal is lifted"], 1,
         "Reconcile who was dialyzed, where, and who was missed."),
        ("What should be done when a warning is issued?",
         ["Wait for landfall", "Ask the nephrologist about moving sessions earlier and call every patient", "Close the unit", "Cancel all sessions"], 1,
         "Dialyzing before landfall buys time."),
        ("What is a call-down drill?",
         ["A fire drill", "A test of the patient call list before it is needed", "A staff meeting", "A machine test"], 1,
         "Wrong numbers are found in calm weather, not in a storm."),
    ],
    "terms": [("Receiving unit", "Another dialysis unit that agrees to treat your patients when yours cannot."),
              ("Emergency card", "A wallet card with the facts a strange unit needs."),
              ("Disaster diet", "A short-term, stricter limit on potassium, salt, and fluid."),
              ("Incident command", "A structure that names who leads, communicates, and handles logistics."),
              ("Call-down drill", "A test of the call list before it is needed."),
              ("Capacity gap", "Patients needing treatment minus confirmed slots."),
              ("Restart gates", "Five signed checks before the unit treats patients again."),
              ("Crush injury", "Muscle damage from being trapped, which releases potassium and can injure the kidneys.")],
    "readings": [("climate-extremes-kidney-care.html", "Kidney care in an era of climate extremes."),
                 ("fluid-management-dialysis.html", "Salt and fluid advice that buys time."),
                 ("hemodialysis-complications.html", "What happens when sessions are missed.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c11"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("hn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
