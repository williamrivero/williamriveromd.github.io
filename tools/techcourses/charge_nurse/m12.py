# -*- coding: utf-8 -*-
"""Dialysis Charge Nurse, Module 12: Leading the First Ten Minutes of an Emergency. Written for this series from published sources."""

MODULE = {
    "image_alt": "A charge nurse directing an emergency team at one dialysis chair while another nurse watches the rest of the floor.",
    "objectives": [
        "Explain why cardiac arrest happens on the dialysis floor and when risk is highest.",
        "Decide in seconds whether the dialysis circuit is the cause of a collapse or a bystander.",
        "Assign roles out loud, including one nurse who watches every other patient.",
        "Use directed, closed-loop communication under pressure.",
        "Hand off to the physician, the code team, or the ambulance crew with the dialysis details they need.",
    ],
    "big": """
{{plain:A good fire captain arriving at a burning house does not grab the hose. She stands where she can see everything, gives each firefighter one job, and makes sure someone is watching the house next door.}}
<p>The picture has a limit. A fire captain can step back because the fire does not change what she must do in the next minute. In a dialysis emergency, the patient is still connected to a circuit that may be the cause, such as air, blood loss, a reaction, or the wrong dialysate, and only someone at the chair can stop the pump, clamp, and decide whether to return the blood. So the charge nurse often leads with her hands busy for the first minute, then steps back to direct.</p>
<p>In a dialysis emergency, the charge nurse&rsquo;s hands are often needed too. But her first job is to lead: name the problem, assign the roles, decide what to do with the circuit, and keep the other patients safe. A patient with chronic kidney disease (CKD) can deteriorate in minutes, and a unit with eleven other machines running does not pause because one patient is in trouble.</p>
{{cards:Key terms for this module|Cardiopulmonary resuscitation (CPR)::Chest compressions and breathing support during cardiac arrest.|Defibrillator::A device that delivers a shock to restore a normal heart rhythm.|Shockable rhythm::A heart rhythm that a shock can correct.|Circuit::The lines, dialyzer, and machine through which blood flows outside the body.|Closed-loop communication::A command that is repeated back and reported done.|Watcher::The nurse assigned to every other patient during an emergency.}}
""",
    "case": {"title": "Bed 9 is not breathing", "html": """
<p>Tuesday, 7:05. Mr. Leonardo Ramos, 71, is an hour into his first session after the long gap. He slumps in his chair. No pulse. The charge nurse, Nurse Ana Villareal, is at Bed 2.</p>
<p>Eleven other patients are connected. Ana has three nurses: Arnel, Kris, and Mika. The physician on duty is on the ward, about five minutes away.</p>
""", "questions": ["What are Ana&rsquo;s first three commands?",
                  "What happens to the circuit?",
                  "Who watches the other eleven patients?"]},
    "sections": [
        ("why", "Arrest on the floor", "Why arrest happens on the dialysis floor", """
<p>Sudden cardiac death is the most common cause of death in patients on hemodialysis, and risk peaks after the long gap.[[hn_foley2011]][[hn_pun2007]] In a registry of 398 cardiac arrests in United States dialysis clinics, staff started CPR in 81.4% of cases and applied a defibrillator before the ambulance arrived in 52.3%. Staff-started CPR was associated with about three times the odds of leaving hospital alive. The first rhythm was not shockable in 66%.[[hn_pun2019]]</p>
<p>The lesson is that readiness and speed matter more than the rhythm. A unit that starts compressions in the first minute gives its patients the best chance the evidence shows.</p>
"""),
        ("circuit", "Cause or bystander", "Is the circuit the cause or a bystander?", """
<p>Ask in seconds: is there air in the venous line, blood on the floor, dark blood in the line, a wrong dialysate, or a pattern of symptoms in neighboring chairs?</p>
{{fig:cn12_circuit}}
<ul>
<li><strong>Yes: the circuit may be the cause.</strong> Stop the pump, clamp, and do not return blood that may contain air or hemolyzed cells.</li>
<li><strong>No: the circuit is a bystander.</strong> Per protocol, return the blood if it can be done quickly and safely, or disconnect, and start resuscitation without delay.</li>
</ul>
{{key:Do not return blood that may contain air or burst red cells. When in doubt, stop, clamp, and resuscitate.}}
"""),
        ("roles", "Roles out loud", "Roles out loud", """
<p>Say the roles aloud, using names: &ldquo;Arnel, compressions. Kris, defibrillator and airway bag. Mika, watch every other patient and tell me if anyone changes. I&rsquo;ll call the physician and lead.&rdquo;</p>
{{fig:cn12_roles}}
<p>The watcher is the role most often forgotten and the one most specific to dialysis. Eleven other patients are still connected, some still losing pressure, some with needles that can dislodge while everyone looks at Bed 9.</p>
"""),
        ("loop", "Closed-loop communication", "Directed, closed-loop communication", """
<p>Name the person, give one task, and expect a report back. In operating-theater emergency simulations, requests that used both a named recipient and a closed loop were completed every time, against 81% for requests that used neither or only one.[[cn_lee2025]] This was simulation, not patient outcomes, but the result fits what teams experience: unnamed requests (&ldquo;someone get the cart&rdquo;) are the ones nobody does.</p>
{{fig:cn12_closedloop}}
{{flow:Three beats|Name and task::&ldquo;Kris, bring the defibrillator.&rdquo;|Repeat back::&ldquo;Bringing the defibrillator.&rdquo;|Report done::&ldquo;Pads on.&rdquo;}}
"""),
        ("standards", "Standards", "Resuscitation standards", """
<p>Follow current basic and advanced life support guidance: the American Heart Association 2025 updates, and the European Resuscitation Council (ERC) 2025 chapter on special circumstances, which addresses patients on dialysis.[[aha2025_bls]][[erc2025_special]] High potassium is a reversible cause to consider in a dialysis patient; its treatment follows the physician&rsquo;s orders.</p>
"""),
        ("handoff", "The handoff out", "The handoff to the physician or ambulance", """
<p>When the physician, the code team, or the ambulance arrives, give a structured handoff: who, what happened and when, what was done, the dialysis details, and what is still pending.[[hn_starmer2014]] Dialysis details the receiving team cannot guess: time on the machine, fluid removed, the last potassium, the access type, and whether blood was returned.</p>
{{scene:Two emergencies at once|<p>At 7:09 Mika, the watcher, calls: &ldquo;Bed 4, pressure 88 over 50, he&rsquo;s yawning.&rdquo; Ana is leading the code at Bed 9. She does not leave. At the next rhythm check she sends Kris to Bed 4: &ldquo;Kris, Bed 4: stop fluid removal, lay him flat, recheck in two minutes, report to me.&rdquo; Kris repeats it back and goes. Arnel continues compressions; Ana takes the defibrillator. When two things happen at once, the charge nurse keeps the sicker patient and sends her most experienced available nurse to the other, with a named task and a report-back time.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>The first three commands.</strong> &ldquo;Bed 9, no pulse. Arnel, compressions. Kris, defibrillator. Mika, watch everyone else.&rdquo;</p>
<p><strong>The circuit.</strong> At 7:05:30 Ana checks: no air, no blood loss, normal line color. The circuit is a bystander. She stops the pump, returns the blood per protocol in under a minute because it is quick and safe, and disconnects. At 7:06 she calls the physician: &ldquo;Code at Bed 9.&rdquo; Pads are on at 7:06:30; the rhythm is not shockable; CPR continues.</p>
<p><strong>The other eleven.</strong> Mika watches them. At 7:09 she reports Bed 4&rsquo;s falling pressure, and Ana sends Kris with a named task. At 7:10 the physician arrives and Ana hands off: &ldquo;Mr. Ramos, 71, after the long gap, arrested at 7:05, one hour on dialysis, 0.9 liters removed, Friday potassium 6.1, fistula, blood returned and disconnected at 7:06; CPR since 7:05; not shockable at 7:07.&rdquo; Bed 4 was caught only because someone was watching.</p>
"""],
    "skills": {"title": "Leading the first ten minutes",
               "intro": "Two simulated emergencies on a training manikin at a dialysis chair: one where the circuit is a bystander, one with air or suspected hemolysis. A facilitator adds a second deterioration elsewhere.",
               "items": [
                   ("Recognizes the arrest and starts CPR within the first minute.", True),
                   ("Makes the circuit cause-or-bystander decision in seconds and states it.", True),
                   ("Does not return blood when air or hemolysis is suspected.", True),
                   ("Assigns roles by name, including the watcher.", True),
                   ("Uses directed, closed-loop commands.", False),
                   ("Handles a second deterioration without leaving the code leaderless.", False),
                   ("Gives a structured handoff with time on machine, fluid removed, last potassium, access, and blood return.", True),
               ],
               "placement": "Lead one unannounced emergency drill on your unit as team leader, with the head nurse observing."},
    "quiz": [
        ("Staff-started CPR in clinic arrests was associated with:",
         ["No change", "About three times the odds of leaving hospital alive", "Harm", "Fewer shocks"], 1,
         "Early CPR is the strongest lever."),
        ("In the registry, the first rhythm was not shockable in about:",
         ["10%", "33%", "66%", "95%"], 2,
         "Readiness and speed matter more than rhythm."),
        ("Suspected hemolysis during a collapse. What happens to the blood in the circuit?",
         ["Return it", "Do not return it", "Increase flow", "Wait"], 1,
         "Burst red cells release potassium."),
        ("Which role is most specific to dialysis emergencies?",
         ["Compressions", "The watcher of the other patients", "The recorder", "The runner"], 1,
         "Eleven other machines are still running."),
        ("In the simulations, requests with both a named recipient and a closed loop were completed:",
         ["50% of the time", "81% of the time", "Every time", "Never"], 2,
         "Against 81% for neither or one."),
        ("What should the handoff to an ambulance include?",
         ["Only the name", "Time on machine, fluid removed, last potassium, access, and whether blood was returned", "The bill", "Nothing"], 1,
         "Details the receiving team cannot guess."),
        ("When is the risk of arrest highest?",
         ["Midweek", "After the long gap", "On weekends", "It is constant"], 1,
         "The first session after the two-day gap."),
        ("The circuit is a bystander. What do you do?",
         ["Leave it running", "Return blood quickly if safe or disconnect, and start resuscitation", "Ignore it", "Call biomedical first"], 1,
         "Do not delay CPR."),
        ("Air is seen in the venous line at collapse. What do you do?",
         ["Return the blood", "Stop the pump, clamp, and do not return the blood", "Speed up", "Disconnect the arterial line only"], 1,
         "The circuit may be the cause."),
        ("Two emergencies at once. What does the charge nurse do?",
         ["Handle both herself", "Keep the sicker patient and send the most experienced available nurse to the other with a named task", "Wait", "Leave the code"], 1,
         "Delegate with a name, a task, and a report time."),
        ("What is the second beat of closed-loop communication?",
         ["Shouting", "Repeating the task back", "Walking away", "Writing it down later"], 1,
         "Name and task, repeat back, report done."),
        ("Which is a reversible cause to consider in a dialysis patient&rsquo;s arrest?",
         ["Hair loss", "High potassium", "Cold feet", "Hunger"], 1,
         "Treatment follows the physician&rsquo;s orders."),
        ("Which guidance should the unit follow for resuscitation?",
         ["Any website", "Current AHA and ERC life support guidance", "The patient&rsquo;s preference only", "None"], 1,
         "The ERC special circumstances chapter covers dialysis."),
        ("&ldquo;Someone get the cart!&rdquo; Why is this a weak command?",
         ["It is rude", "Nobody is named, so it may not be done", "Carts are heavy", "It is too long"], 1,
         "Unnamed requests are the ones nobody does."),
        ("What is the charge nurse&rsquo;s first job in an emergency?",
         ["Start compressions herself", "Lead: name the problem, assign roles, decide on the circuit, protect the others", "Call the family", "Write the record"], 1,
         "Her hands may help too, but leadership comes first."),
    ],
    "terms": [("Cardiopulmonary resuscitation (CPR)", "Chest compressions and breathing support."),
              ("Defibrillator", "A device that delivers a shock to restore a normal rhythm."),
              ("Shockable rhythm", "A heart rhythm that a shock can correct."),
              ("Circuit", "The lines, dialyzer, and machine outside the body."),
              ("Closed-loop communication", "A command repeated back and reported done."),
              ("European Resuscitation Council (ERC)", "The European body that publishes resuscitation guidelines.")],
    "readings": [("code-blue-acls-dialysis-unit.html", "Cardiac arrest response in a dialysis unit."),
                 ("cardiovascular-death-dialysis.html", "Why heart disease is the main cause of death on dialysis."),
                 ("potassium-hyperkalemia-ckd.html", "High potassium: causes, risks, and treatment.")],
    "calcs": ["calc-dialysis-charge-nurse-toolkit.html#c8"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("cn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
