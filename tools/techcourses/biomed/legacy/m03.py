# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "A technician testing the air detector and venous clamp of a hemodialysis machine with a training tubing set.",
    "objectives": [
        "Describe how a roller blood pump moves blood and why occlusion and tubing size matter.",
        "Explain what arterial, venous, and transmembrane pressures indicate.",
        "Explain how the air detector, venous clamp, and blood leak detector work.",
        "Explain why every protective system is tested on a schedule, and what a protective system cannot see.",
    ],
    "big": """
{{plain:On the blood side the machine does three things: it moves blood with a roller pump, it watches pressures to judge how the circuit is behaving, and it stands guard for two dangers, air going into the patient and blood escaping through the membrane. The guards are sensors linked to a clamp and to the pump. A guard that has never been tested is only a hope.}}
{{fig:blood_circuit|The blood circuit with its monitoring points. Follow the path from the patient through the pump and dialyzer to the air trap and back.}}
{{cards:Key terms for this module|Roller pump::A pump whose rollers squeeze the tubing to push blood forward. Also called a peristaltic pump.|Occlusion::How firmly the rollers squeeze the tubing.|Arterial pressure::Pressure before the pump. Normally negative, because the pump is pulling.|Venous pressure::Pressure after the dialyzer, on the return line. Normally positive.|Transmembrane pressure::The pressure difference across the dialyzer membrane.|Protective system::A sensor and an automatic action that together stop a hazard without waiting for a person.}}
""",
    "case": {
        "title": "The alarm that did not sound",
        "html": """
<p>During a drill, a nurse notices that a training tubing set on machine 3 has several small bubbles moving past the air detector, and no alarm sounds. The venous chamber on this machine has been seated by a new operator. The machine&rsquo;s last preventive maintenance visit was eight months ago; the manual specifies six.</p>
""",
        "questions": ["Give two possible reasons the alarm did not sound.",
                      "What is done with machine 3 now?",
                      "What does the overdue maintenance visit have to do with it?"],
    },
    "sections": [
        ("pump", "Blood pump", "The blood pump", """
<p>The blood pump never touches blood. Its rollers squeeze a thick section of tubing, the pump segment, against a curved track and push the blood ahead of them. The flow shown on the screen is calculated from pump speed and the tubing size, not measured directly.</p>
{{cards:What makes displayed blood flow untrue|Wrong tubing size selected::The machine calculates flow for a different diameter.|Occlusion too loose::Blood slips back past the rollers; real flow is lower than shown.|Occlusion too tight::Red cells are crushed and the tubing wears.|Very negative arterial pressure::The pump segment partly collapses and delivers less than calculated.}}
<p>Checking pump speed and occlusion by the service manual is a standard maintenance task. So is checking the pump cover switch, which must stop the pump if the cover is opened.</p>
"""),
        ("pressure", "Pressures", "Reading the pressures", """
<div class="table-wrap"><table>
<thead><tr><th>Pressure</th><th>Where it is measured</th><th>Usual sign</th><th>What a change can mean</th></tr></thead>
<tbody>
<tr><td>Arterial (pre-pump)</td><td>Between the patient and the blood pump</td><td>Negative</td><td>More negative: poor flow from the access, a kink, a clotting needle</td></tr>
<tr><td>Venous</td><td>At the venous chamber, after the dialyzer</td><td>Positive</td><td>Higher: obstruction on the return side. Lower: disconnection, or the needle is out</td></tr>
<tr><td>Transmembrane</td><td>Calculated from blood-side and dialysate-side pressures</td><td>Varies</td><td>Rising: membrane clotting or high fluid removal</td></tr>
</tbody></table></div>
<p>Pressure sensors sit inside the machine and are connected to the blood tubing through small filters called transducer protectors, which keep blood out. A wet or blocked protector gives a false reading, and blood that passes one contaminates the machine internally, which then needs decontamination by the manual&rsquo;s method.</p>
{{stop:A venous pressure alarm does not reliably detect a needle that has slipped out, because the needle itself provides most of the resistance. Machines cannot replace a visible access. Never suggest that alarm limits make watching unnecessary.}}
"""),
        ("air", "Air and clamp", "The air detector and the venous clamp", """
<p>Air entering a vein can be fatal. Just below the venous chamber, the return line passes through an ultrasonic sensor: sound travels well through blood and poorly through air, so a bubble changes the signal. When the sensor detects air above its limit, two things must happen at once: the blood pump stops, and a clamp closes on the return line.[[iec60601_2_16]]</p>
{{flow:The air protection chain|Sense::The ultrasonic detector sees air or foam.|Stop::The blood pump halts.|Clamp::The venous clamp closes the return line.|Alarm::The operator is called.|Resolve::Air is removed by the clinical procedure before restart.}}
{{cards:Why the chain can fail|Tubing not seated::The line or chamber is not properly in the sensor.|Wrong tubing set::The sensor is set up for a different tube.|Sensor dirty or drifted::Gel, dried saline, or age.|Clamp weak::It closes but does not fully stop flow.}}
<p>You prove the chain by the service manual&rsquo;s test, typically by introducing a defined amount of air into a fluid-filled test line and confirming detection, pump stop, and a clamp that holds against a stated pressure.</p>
"""),
        ("leak", "Blood leak", "The blood leak detector", """
<p>If a fiber in the dialyzer breaks, blood enters the dialysate. A light beam passes through the used dialysate on its way to the drain; blood absorbs or scatters the light, and the detector alarms and stops the treatment functions the manual describes. Air bubbles, scale, and dirt on the sensor window can cause false alarms or, worse, reduce sensitivity. The detector is cleaned and its sensitivity checked at maintenance.</p>
{{fig:dialyzer_anatomy|A broken fiber lets blood into the dialysate that surrounds it. The blood leak detector looks for that blood in the used fluid.}}
"""),
        ("testing", "Testing", "Protective systems are only as good as their last test", """
{{cards:Three questions for every protective system|Does it sense?::Introduce the condition by the approved test method.|Does it act?::Pump stops, clamp closes, bypass switches.|Does it tell?::Audible and visible alarm.}}
<p>Machines test many of these functions themselves at start-up, and operators check them before each treatment. Your periodic tests go further, using defined test conditions and measuring instruments. The safety standard is built on the idea that no single fault should be able to harm the patient; an untested protective system is a hidden single fault waiting for a second one.[[iec60601]][[iec60601_2_16]]</p>
{{key:Never bypass, bridge, or disable a protective system to &ldquo;get through the shift.&rdquo; A machine with a protective system that cannot be made to work is out of service.}}
"""),
    ],
    "debrief": ["""
<p><strong>Case review.</strong> Two likely reasons: the venous line or chamber was not seated correctly in the detector, or the detector itself has lost sensitivity. Small bubbles may also be below the alarm limit by design, but that is for testing to show, not for assumption. Machine 3 is tagged out of service now. The technician reseats a correct training set and runs the air detector and clamp test from the service manual; if it fails, the sensor is cleaned, adjusted, or replaced and retested. The overdue maintenance visit matters because the periodic test is what would have found a drifting sensor. The visit is brought up to date, the gap is reported to the chief technician and charge nurse, and operators are shown again how to seat the chamber.</p>
"""],
    "skills": {
        "title": "Verifying blood-side protective systems",
        "intro": "Materials: an out-of-service machine, its service manual, a training tubing set, a calibrated pressure meter, and the test fixtures the manual specifies.",
        "items": [("Identifies the blood pump, pressure ports, air detector, venous clamp, and blood leak detector.", False),
                  ("Confirms the tubing size setting matches the tubing set in use.", False),
                  ("Checks that opening the pump cover stops the pump.", True),
                  ("Compares arterial and venous pressure readings with the calibrated meter by the manual&rsquo;s method.", True),
                  ("Performs the air detector test and confirms pump stop, clamp closure, and alarm.", True),
                  ("Performs the venous clamp holding test by the manual&rsquo;s method.", True),
                  ("Cleans and checks the blood leak detector as the manual states.", False),
                  ("Records each result with the test instrument&rsquo;s identity and calibration date.", False)],
        "placement": "Watch operators seat the venous chamber and line on five machines. Note anything that could affect the air detector and discuss it with the charge nurse.",
    },
    "quiz": [
        ("How does the machine arrive at the blood flow shown on the screen?",
         ["A flow sensor in the blood", "It calculates it from pump speed and tubing size", "From the patient&rsquo;s blood pressure", "From conductivity"], 1,
         "Displayed flow is calculated, so wrong tubing size or poor occlusion makes it untrue."),
        ("Why is pre-pump arterial pressure normally negative?",
         ["The sensor is faulty", "The pump is pulling blood from the access", "The dialyzer is clotted", "The venous clamp is closed"], 1,
         "Suction ahead of the pump produces negative pressure."),
        ("What must happen when the air detector senses air above its limit?",
         ["Only an alarm", "The blood pump stops and the venous clamp closes, with an alarm", "The heater switches off", "Dialysate flow increases"], 1,
         "Detection must trigger automatic action, not just a warning."),
        ("What does the blood leak detector examine?",
         ["Blood in the venous chamber", "Used dialysate, for blood that has crossed a broken membrane", "The water supply", "The patient&rsquo;s access"], 1,
         "It looks for blood in dialysate leaving the dialyzer."),
        ("What is the purpose of a transducer protector?",
         ["To cool the sensor", "To keep blood out of the machine&rsquo;s pressure sensor", "To measure flow", "To remove air"], 1,
         "It is a barrier filter; a wet one gives false readings."),
        ("Can a venous pressure alarm be relied on to detect a dislodged needle?",
         ["Yes, always", "No; pressure may change too little to alarm", "Only on new machines", "Only at low blood flow"], 1,
         "Most of the resistance is in the needle, so pressure can stay within limits. The access must remain visible."),
        ("A protective system cannot be made to pass its test before the next shift. What is correct?",
         ["Bridge it for today", "Widen the alarm limits", "Keep the machine out of service", "Ask the operator to watch closely"], 2,
         "A machine without a working protective system is not used."),
        ("Which is a likely cause of an air detector failing to alarm?",
         ["The venous line is not seated properly in the detector", "The dialysate is too warm", "The softener is regenerating", "The blood pump cover is closed"], 0,
         "Incorrect seating, a wrong tubing set, or a dirty or drifted sensor can all defeat detection."),
    ],
    "terms": [("Pump segment", "The thicker section of tubing that fits in the blood pump."),
              ("Ultrasonic", "Using sound waves above the range of hearing."),
              ("Single-fault safety", "The design rule that one failure alone must not harm the patient.")],
    "readings": [("hemodialysis-complications.html", "What the clinical team sees when things go wrong on the blood side."),
                 ("hemodialysis-access-lifeline.html", "The access your pressure readings depend on."),
                 ("high-flux-hd-optimization.html", "Why true blood flow matters for the treatment.")],
}
