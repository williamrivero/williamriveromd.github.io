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
{{plain:Think of the blood side of the machine as a jeepney route with a barker and two guards. The roller pump is the engine that keeps the blood moving. The pressure readings are the barker, calling out when the road ahead is blocked or the passengers are not boarding. The guards stand at the end of the route and watch for two dangers: air going into the patient and blood escaping through the membrane. Each guard is a sensor linked to a clamp and to the pump. A guard who has never been tested is only a hope.}}
<p>The picture has a limit. A human guard who falls asleep may still wake at a shout. A sensor that has drifted, or a tube that is not seated in it, does nothing at all, and it gives no sign that it has stopped watching. The only way to know that a guard is awake is to test it.</p>
{{fig:blood_circuit|The blood circuit with its monitoring points. Follow the path from the patient through the pump and dialyzer to the air trap and back.}}
{{cards:Key terms for this module|Roller pump::A pump whose rollers squeeze the tubing to push blood forward. Also called a peristaltic pump.|Occlusion::How firmly the rollers squeeze the tubing.|Arterial pressure::Pressure before the pump. Normally negative, because the pump is pulling.|Venous pressure::Pressure after the dialyzer, on the return line. Normally positive.|Transmembrane pressure::The pressure difference across the dialyzer membrane.|Protective system::A sensor and an automatic action that together stop a hazard without waiting for a person.}}
""",
    "case": {
        "title": "The alarm that did not sound",
        "html": """
<p>It is a Wednesday morning, and the unit is running its monthly air-alarm drill before the first patients arrive. The nurse, Ms. Rowena Villanueva, watches a training tubing set on machine 3. Several small bubbles move past the air detector. No alarm sounds.</p>
<p>The venous chamber on this machine was seated by a new operator. The biomedical technician, Mr. Arnel Bautista, checks the service log. The machine&rsquo;s last preventive maintenance visit was eight months ago. The manual specifies six.</p>
""",
        "questions": ["Give two possible reasons the alarm did not sound.",
                      "What is done with machine 3 now?",
                      "What does the overdue maintenance visit have to do with it?"],
    },
    "sections": [
        ("pump", "Blood pump", "The blood pump", """
<p>The blood pump never touches blood. Its rollers press a thick section of tubing, the pump segment, against a curved track and push the blood ahead of them, the way you push toothpaste along a tube with your thumb. The flow shown on the screen is calculated from the pump speed and the tubing size. It is not measured directly.</p>
<p>That calculation is only as true as its inputs. Anything that changes how much blood each turn of the rollers really moves makes the display wrong, and the screen will not show the difference.</p>
{{cards:What makes displayed blood flow untrue|Wrong tubing size selected::The machine calculates flow for a different diameter.|Occlusion too loose::Blood slips back past the rollers, so the real flow is lower than shown.|Occlusion too tight::Red cells are crushed and the tubing wears.|Very negative arterial pressure::The pump segment partly collapses and delivers less than calculated.}}
<p>Checking pump speed and occlusion by the service manual is a standard maintenance task. So is checking the pump cover switch, which must stop the pump if the cover is opened.</p>
"""),
        ("pressure", "Pressures", "Reading the pressures", """
<p>Each pressure reading tells you about one stretch of the circuit. Read it by asking where it is measured and which way it has moved.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pressure</th><th>Where it is measured</th><th>Usual sign</th><th>What a change can mean</th></tr></thead>
<tbody>
<tr><td>Arterial (pre-pump)</td><td>Between the patient and the blood pump</td><td>Negative</td><td>More negative: poor flow from the access, a kink, or a clotting needle</td></tr>
<tr><td>Venous</td><td>At the venous chamber, after the dialyzer</td><td>Positive</td><td>Higher: an obstruction on the return side. Lower: a disconnection, or the needle is out</td></tr>
<tr><td>Transmembrane</td><td>Calculated from the blood-side and dialysate-side pressures</td><td>Varies</td><td>Rising: membrane clotting or high fluid removal</td></tr>
</tbody></table></div>
<p>The pressure sensors sit inside the machine. They connect to the blood tubing through small filters called transducer protectors, which keep blood out. A wet or blocked protector gives a false reading. Blood that gets past one contaminates the inside of the machine, and the machine then needs decontamination by the manual&rsquo;s method.</p>
{{stop:A venous pressure alarm does not reliably detect a needle that has slipped out, because the needle itself provides most of the resistance. Machines cannot replace a visible access. Never suggest that alarm limits make watching unnecessary.}}
"""),
        ("air", "Air and clamp", "The air detector and the venous clamp", """
<p>Air entering a vein can be fatal. Just below the venous chamber, the return line passes through an ultrasonic sensor. Sound travels well through blood and poorly through air, so a bubble changes the signal. When the sensor detects air above its limit, two things must happen at once: the blood pump stops, and a clamp closes on the return line.[[iec60601_2_16]]</p>
{{flow:The air protection chain|Sense::The ultrasonic detector sees air or foam.|Stop::The blood pump halts.|Clamp::The venous clamp closes the return line.|Alarm::The operator is called.|Resolve::The clinical team removes the air by its procedure before restarting.}}
<p>Every link in this chain can fail on its own, and a failure in any one of them breaks the whole protection.</p>
{{cards:Why the chain can fail|Tubing not seated::The line or chamber is not properly in the sensor.|Wrong tubing set::The sensor is set up for a different tube.|Sensor dirty or drifted::Gel, dried saline, or age.|Clamp weak::It closes but does not fully stop flow.}}
<p>You prove the chain with the service manual&rsquo;s test. Typically, you introduce a defined amount of air into a fluid-filled test line, then confirm three things: the detector sees it, the pump stops, and the clamp holds against a stated pressure.</p>
"""),
        ("leak", "Blood leak", "The blood leak detector", """
<p>If a fiber in the dialyzer breaks, blood enters the dialysate. On its way to the drain, the used dialysate passes through a beam of light. Blood absorbs or scatters that light, and the detector alarms and stops the treatment functions the manual describes.</p>
<p>The same principle explains how the detector goes wrong. Air bubbles, scale, and dirt on the sensor window also block light. They can cause false alarms, or, worse, they can reduce the detector&rsquo;s sensitivity so that real blood is missed. At maintenance, you clean the detector and check its sensitivity.</p>
{{fig:dialyzer_anatomy|A broken fiber lets blood into the dialysate that surrounds it. The blood leak detector looks for that blood in the used fluid.}}
"""),
        ("testing", "Testing", "Protective systems are only as good as their last test", """
{{cards:Three questions for every protective system|Does it sense?::Introduce the condition by the approved test method.|Does it act?::The pump stops, the clamp closes, or bypass switches.|Does it tell?::An audible and visible alarm.}}
<p>Machines test many of these functions themselves at start-up, and operators check them before each treatment. Your periodic tests go further, with defined test conditions and measuring instruments. The safety standard is built on one idea: no single fault should be able to harm the patient. An untested protective system is a hidden single fault, waiting for a second one.[[iec60601]][[iec60601_2_16]]</p>
{{key:Never bypass, bridge, or disable a protective system to &ldquo;get through the shift.&rdquo; A machine with a protective system that cannot be made to work is out of service.}}
"""),
    ],
    "debrief": ["""
<p><strong>Two possible reasons the alarm did not sound.</strong> Either the venous line or chamber was not seated correctly in the detector, or the detector itself has lost sensitivity. It is also possible that bubbles this small fall below the alarm limit by design, but testing must show that. It cannot be assumed.</p>
<p><strong>What is done with machine 3 now?</strong> Tag it out of service now. Mr. Bautista reseats a correct training set and runs the air detector and clamp test from the service manual. If the machine fails, he cleans, adjusts, or replaces the sensor and tests it again.</p>
<p><strong>What does the overdue visit have to do with it?</strong> The periodic test is the one that would have found a drifting sensor. Bring the visit up to date, and report the gap to the chief technician and the charge nurse. Then show the operators again how to seat the chamber, so that the first possible cause cannot repeat.</p>
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
