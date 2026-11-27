# -*- coding: utf-8 -*-
"""Resuscitation Lab, Module 07: Arrest in the Dialysis Chair: Machine, Circuit and Access. The core module.
Written for this series from published sources. DRAFT."""

MODULE = {
    "image_alt": "A circuit nurse clamping blood lines at a hemodialysis machine while colleagues compress the patient in the flattened chair.",
    "objectives": [
        "Act as the circuit nurse in an arrest: stop fluid removal and the blood pump, make the blood decision, and announce it, without ever delaying compressions or a shock.",
        "Decide whether the blood in the circuit is returned or discarded, and never return blood after air, hemolysis or a severe reaction.",
        "Defibrillate safely beside a dialysis machine: dry surfaces, hands off the patient and lines, and disconnection unless the machine is rated defibrillation-proof.",
        "Use a fistula needle or a dialysis catheter for resuscitation drugs safely, including aspirating the catheter lock and clamping between uses.",
        "Recognize and manage suspected air embolism, and explain where the guidelines disagree on positioning.",
    ],
    "big": """
{{plain:Picture a patient in arrest as a house on fire with a garden hose still attached and running. Before anyone can work safely, somebody has to turn off the tap and decide whether the water in the hose goes back into the tank or onto the ground. That person must not get in the way of the firefighters. In a dialysis arrest, the hose is the blood circuit, and that somebody is the circuit nurse.}}
<p>The picture has a limit. The &ldquo;water&rdquo; in a dialysis circuit is the patient&rsquo;s own blood, often a few hundred milliliters in an adult and a much larger share of the blood volume in a small child. Returning it can restore volume the patient badly needs; returning it after air, hemolysis or a reaction can kill. And the circuit is not just a hazard: the access that feeds it is already in a large vein, ready for drugs.</p>
<p>General resuscitation guidelines say almost nothing about this. The 2025 AHA special-circumstances chapter does not address cardiac arrest during hemodialysis; the ERC 2025 special-circumstances guideline does, in a few sentences: a trained dialysis nurse or technician operates the machine; stop dialysis and return the patient&rsquo;s blood volume with a fluid bolus; disconnect the patient unless the equipment is defibrillation-proof, and beware of wet surfaces; leave the access open and use it for drugs; and expect that dialysis may be needed early after ROSC.[[erc2025_special]] This module turns those sentences into a role. It matches the signed-off Card 1 of the Emergency Quick Cards line by line.</p>
{{cards:Key terms for this module|Circuit nurse::The dialysis nurse (or trained technician) who manages the machine and circuit during an arrest, and nothing else until the circuit is safe.|Blood return (rinse-back)::Returning the blood in the circuit to the patient with saline.|Clamp and disconnect::Stopping the pump, clamping the lines, and separating the patient from the circuit without returning the blood.|Defibrillation-proof::A rating given by the manufacturer that the equipment and its patient connections withstand a defibrillator shock.|Catheter lock::The anticoagulant or antimicrobial solution left in each catheter limb between sessions.|Watcher::The staff member who keeps every other patient safe during the arrest.}}
""",
    "case": {"title": "Station 7, the circuit", "html": """
<p>At 9:40 a.m., Mr. Arnel Gutierrez, 61, arrests two hours into his session (the same event as Module 5). He dialyzes through a left forearm fistula with two needles; his fluid removal goal is 3.2 L, and 2.1 L has been removed. The chair is wet near the arm where a saline bag dripped earlier.</p>
<p>Nurse Ms. Camille Ortiz is his assigned nurse. Compressions have started. The defibrillator is coming. Ms. Ortiz stands at the machine with her hands on the blood pump button. Another nurse calls out, &ldquo;Disconnect him so we can move him!&rdquo; The technician asks, &ldquo;Do we return the blood?&rdquo;</p>
""", "questions": ["What does Ms. Ortiz do in her first 60 seconds, and in what order?",
                  "Should the blood go back? What would change your answer?",
                  "What has to be true before the first shock?"]},
    "sections": [
        ("role", "The circuit nurse", "One person owns the circuit", """
<p>In most dialysis arrests the circuit is managed by whoever is closest, while also trying to help with compressions or fetch the cart. That splits attention at the worst moment. The ERC recommends that a trained dialysis nurse or technician operates the machine.[[erc2025_special]] This course names that person the circuit nurse: usually the patient&rsquo;s own nurse, who knows the access, the fluid removed, and the machine.</p>
{{fig:rl07_positions}}
<div class="table-wrap"><table>
<thead><tr><th>Circuit nurse does</th><th>Circuit nurse does not</th></tr></thead>
<tbody>
<tr><td>Stops fluid removal at once</td><td>Stop compressions to reach the machine</td></tr>
<tr><td>Stops the blood pump when the blood decision requires it</td><td>Leave the circuit to fetch equipment</td></tr>
<tr><td>Announces the blood decision aloud: &ldquo;Blood returned,&rdquo; or &ldquo;Clamped, not returned&rdquo;</td><td>Return blood after air, hemolysis or a severe reaction</td></tr>
<tr><td>Makes the access safe for drugs and tells the leader which port to use</td><td>Leave an access open, unclamped or unsecured</td></tr>
<tr><td>Reports time on the machine, fluid removed, and the last potassium</td><td>Restart dialysis without the attending nephrologist</td></tr>
</tbody></table></div>
<p>The circuit nurse works from the machine side of the chair and never crosses the compressor. In a three-person team, the circuit nurse makes the circuit safe in the first minute, then joins compressions or recording. The circuit decision is announced once, clearly, and the recorder writes it down with the time.</p>
{{key:The circuit has one owner. Stop fluid removal first, announce the blood decision aloud, and never stop compressions for the machine.}}
"""),
        ("blood", "Return or clamp", "Does the blood go back?", """
<p>The first action is the same in every arrest: stop fluid removal. A patient in arrest has no circulation to spare, and continued fluid removal only empties it further. What happens next depends on why the patient arrested and on whether the blood in the circuit is safe.</p>
{{fig:rl07_blood_decision}}
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>Blood decision</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Suspected air in the circuit or patient</td><td><strong>Clamp, do not return</strong></td><td>Returning pushes more air into the patient</td></tr>
<tr><td>Suspected hemolysis (translucent, port-wine blood)</td><td><strong>Clamp, do not return</strong></td><td>The blood carries potassium released from broken red cells</td></tr>
<tr><td>Severe dialyzer reaction or anaphylaxis</td><td><strong>Clamp, do not return</strong></td><td>The circuit blood carries the trigger</td></tr>
<tr><td>Line separation or needle dislodgement with an open line end</td><td>Do not return through the open end</td><td>Contamination and air</td></tr>
<tr><td>Any other arrest, circuit sound</td><td>Return the blood quickly with saline, or clamp and disconnect</td><td>Returns volume; the access stays in place for drugs</td></tr>
</tbody></table></div>
<p>The ERC states the principle as &ldquo;stop dialysis and return the patient&rsquo;s blood volume with a fluid bolus.&rdquo;[[erc2025_special]] Card 1 adds the exceptions, which come from the physiology of the circuit emergencies: never return blood after air, hemolysis or a dialyzer reaction. A saline bolus through the circuit also treats the hypovolemia that fluid removal may have caused; in the case, 2.1 L has been removed. How much saline, and how fast, is set by your unit protocol and the leader.</p>
<p>Rinse-back takes a few minutes on most machines. If it would take the circuit nurse away from anything more urgent, clamp and disconnect instead. In this unit&rsquo;s practice, blood that looks hemolyzed is never returned.</p>
{{key:Stop fluid removal, then decide: air, hemolysis, a severe reaction or an open line end mean clamp and do not return. Otherwise return the blood quickly with saline, or clamp and disconnect. Say the decision aloud.}}
"""),
        ("defib", "Defibrillating near the machine", "Defibrillation with a patient on the machine", """
<p>A shock passes current through the patient. Anything in contact with the patient during the shock, including a wet chair, a saline-soaked blanket, a person holding the blood lines, or metal connected to the patient, can carry current to staff or to equipment. The ERC advises disconnecting the patient from the machine unless the equipment is defibrillation-proof, and warns about wet surfaces.[[erc2025_special]]</p>
{{fig:rl07_defib_safety}}
<div class="table-wrap"><table>
<thead><tr><th>Before every shock</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Chair, blanket and floor around the patient dry; wipe or move wet drapes</td><td>Water conducts current to staff</td></tr>
<tr><td>Pads on dry skin, clear of the catheter exit site, dressings and the access arm</td><td>Current must go through the heart, not along wet skin</td></tr>
<tr><td>&ldquo;Everyone clear: patient, chair, lines, machine&rdquo;; the circuit nurse lets go of the lines</td><td>The blood lines are in contact with the patient</td></tr>
<tr><td>Machine status known: rated defibrillation-proof by the manufacturer, or disconnected</td><td>Protects the patient&rsquo;s connection and the device</td></tr>
<tr><td>Oxygen mask or tubing moved away from the chest during the shock</td><td>Sparks near oxygen are a fire risk</td></tr>
</tbody></table></div>
<p>Whether a particular dialysis machine is rated defibrillation-proof is written in the manufacturer&rsquo;s instructions for use, not on a wall poster, and it may differ between models in the same unit. Ask your biomedical technician to put the answer for each model in writing beside the crash cart. When in doubt, the circuit nurse clamps and disconnects before the first shock, which takes seconds and does not require returning the blood. Disconnecting must never delay a shock for VF: if the device is ready and the patient is in VF, the leader decides, and everyone stands clear of the patient, chair, lines and machine.</p>
{{key:Before every shock: dry surfaces, pads clear of the access, hands off the patient and the lines, and the machine either rated defibrillation-proof or disconnected.}}
"""),
        ("access", "Using the access", "The access is a resuscitation line, used safely", """
<p>A dialysis patient in arrest usually has a large-bore needle in a fistula or a central catheter already in place. The ERC says to leave the access open and use it for drug administration.[[erc2025_special]] &ldquo;Open&rdquo; means available and working, never an uncapped needle or an unclamped catheter limb. An open central catheter limb can draw air into the heart, especially when chest pressure falls.</p>
{{fig:rl07_access}}
<div class="table-wrap"><table>
<thead><tr><th>Access</th><th>How to use it for drugs</th><th>Hazard to avoid</th></tr></thead>
<tbody>
<tr><td>Fistula or graft, needles in place, circuit returned or clamped</td><td>Keep the venous needle secured and taped; give drugs through a saline-primed line on the venous needle, flushing after each drug</td><td>A dislodged needle; giving drugs through the arterial needle into a clotted segment</td></tr>
<tr><td>Fistula or graft, circuit still running</td><td>Drugs may go into the venous line port per protocol, after the circuit nurse confirms flow</td><td>Drugs lost in a stopped or clotted circuit</td></tr>
<tr><td>Tunneled or non-tunneled catheter</td><td>Aspirate the lock solution from the limb first (at least the labeled limb volume), flush with saline, give the drug, flush, clamp</td><td>Pushing heparin or citrate lock into the patient; air entry through an open limb</td></tr>
</tbody></table></div>
<p>The catheter lock is often concentrated heparin or citrate. Pushing it into a patient in arrest is a medication error, and aspirating it first is standard practice before any catheter use. Every catheter limb carries its fill volume printed on the clamp or hub; aspirate at least that much. Between drugs, the limb stays clamped with a syringe or a capped connector attached.</p>
<p>If the access is lost or unusable, the standard order applies: attempt a peripheral IV first (COR 1, LOE A), and use intraosseous access if IV attempts fail or are not feasible (COR 2a, LOE A).[[aha2025_als]] Do not place a peripheral IV in the fistula arm, except as a last resort decided by the leader.</p>
{{key:Use the access for drugs, but safely: aspirate every catheter lock first, flush before and after, clamp between uses, and keep fistula needles secured.}}
{{scene:The citrate push|<p>During a drill on a catheter patient, the drug nurse connected the epinephrine syringe straight to the venous limb. The circuit nurse stopped her: &ldquo;Lock first. Aspirate 2 milliliters, then flush.&rdquo; The drill paused for six seconds; compressions did not.</p>
<p class="tc-scene-take">The circuit nurse protects the access while the team protects the circulation.</p>}}
"""),
        ("air", "Air and the other patients", "Air embolism, and the twelve other patients", """
<p>Air enters the circuit through a loose connection before the blood pump, an empty saline bag, a cracked line, or an open catheter limb. A large volume reaching the right heart can block outflow to the lungs; air that crosses to the arterial side through a hole in the heart can reach the brain. Signs are sudden cough, chest tightness, breathlessness, confusion, or collapse, often with foam in the venous line or an air detector alarm (Card 5).[[mccarthy2016]][[greenberg2021]]</p>
{{fig:rl07_air}}
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Source</th></tr></thead>
<tbody>
<tr><td>Stop the blood pump; clamp the venous line; never override the air detector</td><td>Card 5 (dialysis practice)</td></tr>
<tr><td>Do not return the blood</td><td>Card 5</td></tr>
<tr><td>100% oxygen</td><td>AHA 2025, COR 1, LOE C-EO</td></tr>
<tr><td>Position: AHA &ldquo;supine or recovery position on a level surface&rdquo;; dialysis teaching &ldquo;left side, sometimes head down&rdquo;; never sit the patient up</td><td>AHA 2025, COR 2a, LOE C-EO; dialysis reviews</td></tr>
<tr><td>Hyperbaric oxygen is reasonable for life-threatening gas embolism</td><td>AHA 2025, COR 2a, LOE B-NR (adults)</td></tr>
<tr><td>No pulse: CPR flat on the back (Card 1)</td><td>All sources</td></tr>
</tbody></table></div>
<p>The guidelines disagree on position. The 2025 AHA recommendation for life-threatening gas embolism is to position the patient supine or in the recovery position on a level surface (COR 2a, LOE C-EO), with 100% oxygen (COR 1, LOE C-EO).[[aha2025_special]] Dialysis texts and reviews have long taught the left side, sometimes with the head down, to keep air in the right heart.[[mccarthy2016]] Both rest on expert opinion. Card 5 says &ldquo;position per your unit&rsquo;s protocol&rdquo; and flags the difference for clinical review; this course does the same. What no source supports is sitting the patient up, and every source agrees that CPR, if needed, is done flat on the back.</p>
<h3>The other patients</h3>
<p>An arrest takes four to six staff to one chair. Every other circuit keeps running. Needles dislodge, pressures fall, and alarms sound unanswered. The watcher, named at the start of the shift, stays with the other patients and does not join the arrest. If the arrest goes on, the charge nurse decides whether to hold new connections.</p>
{{key:Air: clamp, do not return, oxygen, flat (position per protocol), never sit up. And someone always watches the other patients.}}
{{call:Air below the venous chamber, an air alarm with symptoms, or any arrest on the machine: follow Card 1 or Card 5 now, call the physician-on-duty and the attending nephrologist, and arrange emergency transfer. Your unit protocol decides position and the blood decision; always ask the attending nephrologist for guidance before any restart.}}
"""),
    ],
    "debrief": ["""
<p><strong>The first 60 seconds, in order.</strong> Ms. Ortiz stops fluid removal at once. She looks for a circuit cause: no air in the venous line, no translucent blood, no sign of a reaction, no line apart. With none, she chooses the quick path: she returns the blood with saline per protocol (giving back volume after 2.1 L removed), or clamps and disconnects if rinse-back would take her away from anything more urgent. She announces, &ldquo;Fluid removal off. Blood returned,&rdquo; or &ldquo;Clamped and disconnected.&rdquo; She keeps the venous needle secured and flushed for drugs and tells the leader which port to use.</p>
<p><strong>Would the answer change?</strong> Yes, if there were foam in the venous line, port-wine blood, a reaction in the first minutes of the session, or an open line end. Then she clamps and does not return the blood.</p>
<p><strong>Before the first shock.</strong> The wet chair and blanket near the arm are wiped or moved; pads go on dry skin away from the fistula arm; the machine is disconnected unless it is rated defibrillation-proof; and Ms. Ortiz lets go of the lines when the leader calls &ldquo;clear.&rdquo; No one moves the patient off the chair unless the leader decides compressions cannot be done there.</p>
<p><strong>Afterward.</strong> Dialysis is not restarted without the attending nephrologist. Ms. Ortiz hands over: time on the machine (two hours), fluid removed (2.1 L), whether the blood was returned, the last potassium, and the access.</p>
"""],
    "skills": {"title": "Circuit nurse in a dialysis arrest",
               "intro": "On a manikin in a recliner connected to a training circuit (no patient, no live water connection), act as the circuit nurse during a facilitated arrest.",
               "items": [
                   ("Stops fluid removal within the first seconds and announces it.", True),
                   ("Identifies whether air, hemolysis, a severe reaction or an open line end is present before deciding on the blood.", True),
                   ("Never returns blood after air, hemolysis or a severe reaction.", True),
                   ("Returns blood with saline or clamps and disconnects, and announces the decision aloud for the recorder.", False),
                   ("Never interrupts compressions or crosses the compressor to reach the machine.", True),
                   ("Before a shock, ensures dry surfaces, releases the lines, and confirms the machine is defibrillation-proof or disconnected.", True),
                   ("Aspirates the catheter lock before using a catheter limb for drugs, flushes, and clamps between uses.", True),
                   ("Hands over time on machine, fluid removed, blood decision, last potassium and access.", False),
               ],
               "placement": "With your biomedical technician, find the manufacturer&rsquo;s statement on defibrillation for each machine model in your unit and post it beside the crash cart."},
    "terms": [("Circuit nurse", "The nurse who manages the machine and circuit during an arrest."),
              ("Rinse-back", "Returning the circuit blood to the patient with saline."),
              ("Defibrillation-proof", "A manufacturer rating that equipment withstands a defibrillator shock."),
              ("Catheter lock", "Anticoagulant or antimicrobial solution left in each catheter limb."),
              ("Limb fill volume", "The volume of a catheter limb, printed on its clamp or hub."),
              ("Air detector", "The machine sensor that stops the pump and clamps the venous line when it detects air.")],
    "readings": [("code-blue-acls-dialysis-unit.html", "The site guide to code blue in a dialysis unit.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rl_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["07"])
