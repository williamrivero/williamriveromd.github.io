# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 15: Emergencies and pediatric resuscitation readiness. POD voice. Fictional cases. No drug doses."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Recognize early warning signs in a child on dialysis before blood pressure falls.",
        "Take the first nursing actions for the main dialysis emergencies: hyperkalemia, hypotension, air in the circuit, bleeding and disconnection, dialyzer reactions, seizures and hypoglycemia.",
        "Prepare the pediatric emergency equipment and the team for a resuscitation at the dialysis chair.",
        "Hand over a child in an emergency with a structured format.",
    ],
    "big": """
<p>Most children on dialysis never have a dialysis emergency, which is why staff forget what to do when one happens. Children also hide trouble well: their hearts speed up and their vessels tighten, so blood pressure stays normal until it suddenly does not. Emergencies in children are often recognized late and treated well; the aim is to recognize them early.</p>
<p>Your work in this module is to see the early signs, take the first protective actions in seconds, and call a team that already knows its roles.</p>
{{plain:Think of a child&rsquo;s circulation as a tightrope walker with a long pole. The pole (compensation) keeps the walker steady through many wobbles, so from the ground everything looks fine. When the pole is finally lost, the fall is fast.}}
<p>The picture has a limit. You can see the pole if you know where to look: a rising heart rate, slower capillary refill, cool hands, a change in behavior. These are the wobbles. Watching for them is how you act before the fall.</p>
{{cards:Key terms for this module|Compensated shock::Poor tissue perfusion with blood pressure still normal.|Capillary refill time::Seconds for color to return after pressing a fingertip or sternum.|Hyperkalemia::High blood potassium; can cause dangerous heart rhythms.|Air embolism::Air entering the bloodstream from the circuit.|Pediatric resuscitation::Age-specific life support taught in courses such as Pediatric Advanced Life Support (PALS).}}
""",
    "case": {"title": "The missed Friday", "html": """
<p><strong>Rey Fernandez, 15</strong>, 45 kilograms, missed Friday&rsquo;s hemodialysis for a school event and arrives Monday morning. He feels weak, his legs feel &ldquo;heavy&rdquo;, and his pulse is slow and irregular. The monitor shows tall, peaked T waves. His pre-dialysis potassium sample has just been sent. <strong>Nurse Mae</strong> is setting up.</p>
""", "questions": ["What does Mae suspect, and what does she do in the first minute?",
                  "Should she wait for the laboratory result before calling?",
                  "What does the team need to have ready?"]},
    "sections": [
        ("recognize-early", "Early warning", "Recognize early", """
<p>In children, falling perfusion shows first in heart rate, skin and behavior. Low blood pressure is a late sign (Module 4).</p>
{{fig:pdn15_a}}
<div class="table-wrap"><table>
<thead><tr><th>Domain</th><th>Early warning</th></tr></thead>
<tbody>
<tr><td>Behavior</td><td>Unusually quiet, irritable, restless, confused, hard to wake, floppy in an infant</td></tr>
<tr><td>Circulation</td><td>Heart rate rising above the child&rsquo;s baseline, capillary refill slowing, cool or mottled hands and feet</td></tr>
<tr><td>Breathing</td><td>Fast breathing, grunting, flaring, retractions; consider fluid overload, pleural leak in PD, or acidosis</td></tr>
<tr><td>Symptoms</td><td>Chest pain, abdominal pain, severe headache, muscle weakness, palpitations</td></tr>
</tbody></table></div>
<p>Use your unit&rsquo;s pediatric early warning score if it has one, and trust your concern even when the score is low.</p>
{{key:Behavior, heart rate and capillary refill change before blood pressure. Call on the wobble, not the fall.}}
"""),
        ("dialysis-emergencies", "Emergencies", "Dialysis emergencies: first actions", """
<p>For each emergency below, the first nursing actions protect the child in seconds. Treatments such as medicines follow the unit&rsquo;s emergency protocol and the team&rsquo;s orders. The 2025 American Heart Association guidance on special circumstances of resuscitation covers adult and pediatric life-threatening hyperkalemia among other situations.[[aha2025_special]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Emergency</th><th>What you see</th><th>First nursing actions</th></tr></thead>
<tbody>
<tr><td>Hyperkalemia</td><td>Weakness, slow or irregular pulse, peaked T waves or other ECG changes; often after missed sessions</td><td>Monitor, call the team at once, prepare emergency drugs per protocol, do not wait for the laboratory value if the ECG is abnormal</td></tr>
<tr><td>Hypotension</td><td>Yawning, pallor, rising heart rate, then falling pressure</td><td>Lay flat, reduce or stop ultrafiltration per protocol, call; fluids only as ordered</td></tr>
<tr><td>Air in the circuit</td><td>Air detector alarm, foam in the venous line, sudden breathlessness or chest pain</td><td>Stop the pump, clamp the venous line, call for help, position as trained, oxygen per protocol</td></tr>
<tr><td>Bleeding or disconnection</td><td>Blood at a connection or needle site; a separated line</td><td>Stop the pump, clamp the catheter and line, apply pressure, call; estimate loss</td></tr>
<tr><td>Dialyzer or drug reaction</td><td>Itching, flushing, breathlessness, wheeze, hypotension early in the session</td><td>Stop, do not return the blood if a severe reaction is suspected (per protocol), call</td></tr>
<tr><td>Seizure</td><td>Convulsion, often with disequilibrium, hypoglycemia or hypertension</td><td>Protect the child and access, stop the pump per protocol, check glucose, call</td></tr>
<tr><td>Hypoglycemia</td><td>Sweating, shakiness, drowsiness, especially in infants</td><td>Check glucose, treat per protocol, call</td></tr>
</tbody></table></div>
{{fig:pdn15_b}}
{{key:Stop the pump, clamp, call. Then follow the protocol. In children, the first ten seconds are nursing seconds.}}
"""),
        ("the-team-response", "Team response", "The team response", """
<p>A resuscitation at a dialysis chair is harder than on a ward: the child is connected to a machine, the lines can pull, and the family is often in the room. Preparation decides the outcome.</p>
<ul>
<li><strong>Equipment:</strong> a pediatric emergency cart with sizes for the children you treat, a weight-based drug reference approved by the unit, suction, oxygen and bag-valve masks of the right sizes, a defibrillator with pediatric pads, checked and logged daily.</li>
<li><strong>Roles:</strong> leader, airway, compressions, drugs and recorder, machine and access (stop, clamp, decide on blood return with the leader), family support.</li>
<li><strong>Credentials:</strong> pediatric resuscitation training as your employer requires; the Philippine regional licensing tool lists basic life support for nurses and at least one nurse trained in advanced cardiac life support each shift, which is an adult standard, so pediatric preparation is a local decision.</li>
<li><strong>Drills:</strong> rare events are practiced in simulation and recorded as simulation.</li>
</ul>
<p>Hand over with a structured format such as I-PASS or SBAR, including dialysis details: time stopped, fluid removed, blood returned or not, last potassium, access type.[[starmer2014]]</p>
{{scene:Monday, 7:10 a.m.|<p>Mae sees peaked T waves and a slow, irregular pulse in a teenager who missed a session. She keeps Rey on the monitor, calls the pediatric nephrologist and the emergency team immediately, and brings the emergency cart. She does not wait for the potassium result. While the team gives treatment per protocol, she prepares for urgent dialysis as ordered.</p><p class="tc-scene-take">An abnormal ECG after a missed session is treated as hyperkalemia now, not after the laboratory calls back.</p>}}
{{key:Check the cart daily, know your role before the emergency, and hand over the dialysis details every time.}}
"""),
    ],
    "debrief": ["""
<p><strong>Suspicion and the first minute.</strong> Life-threatening hyperkalemia after a missed session. Mae keeps him monitored, calls the team at once, brings the cart, and prepares emergency drugs and urgent dialysis per protocol.</p>
<p><strong>Wait for the laboratory?</strong> No. ECG changes with symptoms after a missed session justify immediate action; the result confirms but does not delay.</p>
<p><strong>Readiness.</strong> A checked pediatric cart, a weight-based drug reference, defibrillator with suitable pads, assigned roles and a prepared dialysis setup. Afterward, the team reviews why the session was missed and plans with Rey for school events (Module 19).</p>
"""],
    "skills": {"title": "Emergency readiness", "intro": "Simulate each scenario at least once.",
               "items": [("Identifies early warning signs in a child before hypotension", True),
                         ("Performs stop-the-pump and clamp actions for air, bleeding and disconnection", True),
                         ("Calls the team for ECG changes after a missed session without waiting for laboratory results", True),
                         ("Checks the pediatric emergency cart and logs the check", False),
                         ("Takes a team role in a simulated resuscitation and gives a structured handoff with dialysis details", False)]},
    "quiz": [
        ('In children, which is usually a late sign of shock?',
         ['Rising heart rate', 'Restlessness', 'Slow capillary refill', 'Low blood pressure'], 3,
         'Compensation keeps pressure up until it fails.'),
        ('Compensated shock means:',
         ['Poor perfusion with blood pressure still normal', 'Normal perfusion', 'Low blood pressure only', 'No shock'], 0,
         'The tightrope walker still holds the pole.'),
        ('Weakness, slow irregular pulse and peaked T waves after a missed session suggest:',
         ['Hypoglycemia', 'Hyperkalemia', 'Air embolism', 'Dialyzer reaction'], 1,
         'Treat as urgent.'),
        ('With ECG changes, should you wait for the potassium result before calling?',
         ['Yes', 'Only at night', 'No, call the team at once', 'Only if the parent agrees'], 2,
         'The result confirms; it does not delay.'),
        ('First actions for an air detector alarm with foam in the venous line:',
         ['Silence the alarm and continue', 'Increase blood flow', 'Disconnect and leave', 'Stop the pump, clamp the venous line, call, position as trained'], 3,
         'Stop, clamp, call.'),
        ('A line separates and blood is flowing:',
         ['Stop the pump, clamp catheter and line, apply pressure, call', 'Reconnect quickly without clamping', 'Wait', 'Give fluids'], 0,
         'Small children lose meaningful volume fast.'),
        ('Itching, flushing and wheeze early in the session suggest:',
         ['Disequilibrium', 'A dialyzer or drug reaction', 'Hyperkalemia', 'Hypoglycemia'], 1,
         'Stop and follow the reaction protocol.'),
        ('During a seizure on dialysis, check:',
         ['Kt/V', 'Water log', 'Blood glucose', 'Height'], 2,
         'Hypoglycemia is a reversible cause.'),
        ('Infants on dialysis are particularly prone to:',
         ['Gout', 'Hypertension only', 'Nothing', 'Hypoglycemia'], 3,
         'Check glucose when drowsy or sweaty.'),
        ('The pediatric emergency cart should be:',
         ['Checked and logged daily', 'Checked monthly', 'Checked after use only', 'Optional'], 0,
         'Preparation decides outcome.'),
        ('Which role is specific to a dialysis resuscitation?',
         ['Recorder', 'Machine and access: stop, clamp, decide on blood return with the leader', 'Airway', 'Compressions'], 1,
         'The circuit needs an owner.'),
        ('The Philippine regional licensing tool&rsquo;s life-support requirement is:',
         ['A pediatric standard', 'Not stated', 'An adult standard (BLS, and ACLS each shift); pediatric preparation is local', 'PALS for all'], 2,
         'Employers set pediatric credentials.'),
        ('A handoff after a dialysis emergency should include:',
         ['Only vital signs', 'The child&rsquo;s school', 'Nothing', 'Time stopped, fluid removed, blood returned or not, last potassium, access'], 3,
         'Dialysis details change treatment.'),
        ('Rare emergencies in training are:',
         ['Practiced in simulation and recorded as simulation', 'Practiced on real children', 'Skipped', 'Only read about'], 0,
         'No child is exposed to risk for training.'),
        ('Your concern is high but the early warning score is low. You:',
         ['Ignore your concern', 'Act on your concern and escalate', 'Wait for the score to rise', 'Ask the parent'], 1,
         'Scores support judgment; they do not replace it.'),
    ],
    "terms": [("Compensated shock", "Poor perfusion while blood pressure is still normal."),
              ("Capillary refill time", "Seconds for color to return after pressing the skin."),
              ("Hyperkalemia", "High blood potassium."),
              ("Air embolism", "Air entering the bloodstream from the circuit."),
              ("PALS", "Pediatric Advanced Life Support."),
              ("SBAR", "Situation, background, assessment, recommendation: a structured way to report.")],
    "readings": [("potassium-hyperkalemia-ckd.html", "Potassium and hyperkalemia in kidney disease."),
                 ("code-blue-acls-dialysis-unit.html", "Running a code in a dialysis unit."),
                 ("hemodialysis-complications.html", "Hemodialysis complications.")],
    "calcs": [],
}
