# -*- coding: utf-8 -*-
"""Biomedical Technician track, 12-module edition: new content for Modules 7 to 12."""

NEW = {}

NEW["07"] = {
    "image_alt": "A technician observing the venous clamp during a test with a training tubing set.",
    "objectives": [
        "Explain single-fault safety and why protective systems are independent of control systems.",
        "Describe how the air detector, venous clamp, and blood leak detector work and fail.",
        "Test each protective system by the manufacturer&rsquo;s method and document the result.",
        "Explain why protective systems are never bypassed, and what to do when one cannot be made to pass.",
    ],
    "big": """
{{plain:Think of the fire extinguisher on the wall of a carinderia. It hangs there for years and is never used. On the one night the cooking oil catches fire, it has to work in the first few seconds, and nobody will have time to read the label. A dialysis machine carries several such extinguishers. It is designed so that no single failure can harm the patient. For every quantity that could do harm, a second, independent system is watching, ready to stop the machine.}}
<p>The picture has a limit. An extinguisher can be weighed and its gauge read at a glance. A protective system cannot be checked by looking at it. A dirty sensor, a weak clamp spring, or a misaligned tube looks exactly like a working one. These systems sit idle for months and are needed for one second. The only way to know they will work in that second is to test them, properly, on schedule.</p>
{{cards:Key terms for this module|Protective system::A sensor plus an automatic action that stops a hazard without waiting for a person.|Single-fault safety::The rule that one failure alone must not harm the patient.|Safe state::What the machine does when it detects a hazard: stop the pump, close the clamp, go to bypass.|Alarm limit::The value at which an alarm triggers.|Functional test::Proving a system works by creating the condition it is meant to detect.|Bypassing::Disabling a protective system. Never done.}}
""",
    "case": ("L", "03"),
    "sections": [
        ("principle", "The principle", "Control systems and protective systems", """
<div class="table-wrap"><table>
<thead><tr><th>Hazard</th><th>Control system</th><th>Independent protective system</th><th>Safe state</th></tr></thead>
<tbody>
<tr><td>Dialysate too hot or too cold</td><td>Heater controlled by a temperature sensor</td><td>Second temperature sensor</td><td>Bypass; alarm</td></tr>
<tr><td>Wrong dialysate composition</td><td>Proportioning pumps</td><td>Protective conductivity cell</td><td>Bypass; alarm</td></tr>
<tr><td>Air entering the patient</td><td>Correct priming and level in the venous chamber</td><td>Air detector with venous clamp</td><td>Blood pump stops; clamp closes; alarm</td></tr>
<tr><td>Blood loss through the membrane</td><td>Dialyzer integrity</td><td>Blood leak detector</td><td>Alarm; blood pump and ultrafiltration stop as the manual describes</td></tr>
<tr><td>Blood loss to the environment</td><td>Secure connections</td><td>Venous pressure monitoring (limited), and the operator&rsquo;s eyes</td><td>Blood pump stops; alarm</td></tr>
<tr><td>Wrong fluid removal</td><td>Balancing system and ultrafiltration pump</td><td>Independent supervision of ultrafiltration, by design</td><td>Ultrafiltration stops; alarm</td></tr>
</tbody></table></div>
<p>Read each row from left to right. The control system makes the treatment happen. The protective system watches the result with its own sensor and acts if the result goes wrong. The international standard for hemodialysis equipment requires these protective systems, and it requires that they be independent of the control systems they supervise.[[iec60601_2_16]] Independence is the point. If the heater&rsquo;s own sensor fails and reads low, the heater keeps heating; a second sensor that shares nothing with the first is what catches it. A failed sensor must not be able to both cause a hazard and hide it.</p>
<p>Some limits are fixed by the manufacturer. Others, such as venous pressure limits, are set around the current reading by the machine or the operator. Your work is to verify the fixed ones and to prove that the adjustable ones respond. Where operators set them is not your decision.</p>
"""),
        ("L", "03", "air"), ("L", "03", "leak"),
        ("schedule", "Test schedule", "What is tested, by whom, and when", """
<p>Three levels of testing protect the patient, and each proves something the others cannot. Notice the last column. The machine&rsquo;s own start-up test is useful, but it checks that circuits respond, not that a sensor can still see a bubble through the tubing in front of it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Level</th><th>Who</th><th>When</th><th>What it proves</th><th>What it cannot prove</th></tr></thead>
<tbody>
<tr><td>Machine self-test</td><td>The machine</td><td>Every start-up</td><td>Alarms, sensors, and actuators respond electrically</td><td>That sensors are accurate or correctly aligned with the tubing</td></tr>
<tr><td>Pre-treatment check</td><td>The operator</td><td>Every treatment</td><td>Correct setup; lines seated; alarms can be heard</td><td>Sensor sensitivity</td></tr>
<tr><td>Periodic functional test</td><td>The biomedical technician</td><td>At each maintenance visit, and after related repairs</td><td>Each protective system detects a defined condition and reaches its safe state</td><td>Nothing about tomorrow, which is why there is a schedule</td></tr>
</tbody></table></div>
{{flow:A functional test, any protective system|Read the method::The manual defines the test condition and the pass criteria.|Set up::Training tubing, test fluid, test fixtures. No patient.|Create the condition::A defined air volume, a test solution for the blood leak detector, an out-of-limit temperature or conductivity.|Observe three things::Does it sense, does it act, does it tell.|Measure where required::Clamp holding pressure, response time.|Record::Pass or fail, values, date, your name, instruments used.}}
<div class="table-wrap"><table>
<thead><tr><th>System</th><th>Typical test idea</th><th>Common reason for failing</th></tr></thead>
<tbody>
<tr><td>Air detector</td><td>Introduce a defined bubble into a fluid-filled test line</td><td>Dirty sensor, wrong tubing, misalignment</td></tr>
<tr><td>Venous clamp</td><td>With the clamp closed, apply pressure and confirm no flow</td><td>Weak spring or solenoid; worn jaw</td></tr>
<tr><td>Blood leak detector</td><td>Pass a test solution or filter of defined strength</td><td>Dirty window; drift</td></tr>
<tr><td>Temperature protection</td><td>Simulate or produce an over-limit temperature</td><td>Sensor drift</td></tr>
<tr><td>Conductivity protection</td><td>Remove a concentrate or simulate an out-of-limit reading</td><td>Scaled cell; valve stuck</td></tr>
<tr><td>Cover and door switches</td><td>Open with the pump running</td><td>Misaligned or defeated switch</td></tr>
<tr><td>Audible alarm</td><td>Trigger any alarm</td><td>Volume turned down; speaker failed</td></tr>
<tr><td>Power failure alarm and battery</td><td>Unplug during operation, by the manual</td><td>Aged battery</td></tr>
</tbody></table></div>
"""),
        ("L", "03", "testing"),
        ("never", "Never bypass", "When a protective system fails its test", """
{{flow:If a test fails|Stop::The machine stays out of service.|Clean and reseat::Many failures are dirt or alignment.|Retest::By the same method.|Repair::Replace or adjust by the manual with approved parts.|Retest again::Then test anything else the repair disturbed.|Record::The failure, the cause, the fix, and the passing result.}}
<p>A failed test is the system doing its job: it showed you a weakness while no patient was connected. Follow the steps in order, and record the failure even when the retest passes.</p>
<p>Nuisance alarms deserve the same seriousness. An alarm that sounds for no visible reason teaches staff to silence it without looking, and then a real event is missed. When operators report repeated false alarms, treat the report as a fault to be found.</p>
{{stop:Tape over a switch, a jumper wire, a widened limit in service mode, a clamp propped open: each removes a protection that everyone else still believes is there. If you find one, the machine is out of service and the event is reported.}}
"""),
    ],
    "debrief": ("L", "03"),
    "skills": {"title": "Functional tests of the air detector, clamp, and blood leak detector",
        "intro": "Materials: an out-of-service machine, its service manual, a training tubing set, the manufacturer&rsquo;s test fixtures or solutions, a calibrated pressure meter, and a service record.",
        "items": [("Reads the test method and pass criteria in the manual before starting.", False),
                  ("Sets up with training tubing and confirms no patient connection.", True),
                  ("Performs the air detector test and confirms pump stop, clamp closure, and alarm.", True),
                  ("Performs the venous clamp holding test and records the pressure held.", True),
                  ("Cleans and tests the blood leak detector by the manual.", True),
                  ("Confirms cover and door switches stop the pump.", False),
                  ("Confirms the audible alarm and the power-failure alarm.", False),
                  ("Keeps the machine out of service if any test fails, and states the next steps.", True),
                  ("Records each result with instruments used.", False)],
        "placement": "Review one machine&rsquo;s start-up test log with a senior technician and look for tests that failed and passed on retry."},
    "quiz_keep": [("03", [2, 3, 6, 7])],
    "quiz": [
        ("What does single-fault safety mean?",
         ["The machine never fails", "One failure alone must not be able to harm the patient", "Only one alarm sounds at a time", "The machine has one fuse"], 1,
         "Independent protective systems catch a failure in the control system."),
        ("What can the machine&rsquo;s start-up self-test not prove?",
         ["That alarms respond electrically", "That sensors are accurate and correctly aligned with the tubing", "That the speaker works", "That valves switch"], 1,
         "Accuracy and alignment are shown by periodic functional tests."),
        ("Operators report frequent false blood leak alarms on one machine. How should this be treated?",
         ["Tell them to silence it", "As a fault to find and fix", "Widen the limit", "Ignore it"], 1,
         "False alarms teach staff to ignore real ones."),
        ("You find a jumper wire across a door switch. What do you do?",
         ["Leave it; it works", "Remove the machine from service, repair, and report", "Add tape", "Tell nobody"], 1,
         "A defeated safety device is a serious hidden hazard."),
    ],
    "terms": [("Independent", "Not sharing a sensor or circuit with the system it supervises."),
              ("Pass criteria", "The stated result a test must show to pass."),
              ("Response time", "How quickly a protective system acts after the condition appears.")],
    "readings": [("hemodialysis-complications.html", "What these hazards look like clinically."),
                 ("code-blue-acls-dialysis-unit.html", "Emergency response in the unit.")],
}

NEW["08"] = {
    "image_alt": "A technician marking a wall planner of machine maintenance visits.",
    "objectives": [
        "Build and maintain an equipment inventory for a dialysis center.",
        "Turn the manufacturer&rsquo;s maintenance schedule into a staggered calendar.",
        "Carry out a preventive maintenance visit in a set order.",
        "Manage spare parts, safety notices, and software updates.",
    ],
    "big": """
{{plain:A jeepney operator with a fleet of ten does not wait for a vehicle to break down on EDSA. He keeps a list of every unit, knows when each one is due for its oil change and brake check, and sends them to the shop one or two at a time so the routes stay covered. Preventive maintenance on dialysis machines works the same way. You know every machine you are responsible for, visit each one on a schedule set by its maker, replace the parts that wear, and test what matters, whether or not anyone has complained.}}
<p>The picture has a limit. A jeepney that breaks down costs a day&rsquo;s fares. A machine that fails during treatment affects a patient whose blood is outside the body. And many machine faults give no warning a driver would hear or feel. Preventive maintenance is the least dramatic part of the job and the part that prevents the most harm. A center that does it well has few emergencies.</p>
{{cards:Key terms for this module|Inventory::The list of every piece of equipment, with its identity and status.|Asset number::The center&rsquo;s own number for each item.|Maintenance interval::How often a visit is due, by months or operating hours.|Maintenance kit::The set of wearing parts replaced at a visit.|Safety notice::A manufacturer&rsquo;s formal warning requiring action.|Overdue::Past the due date. A reportable status.}}
""",
    "case": {"title": "Inspection month", "html": """
<p>It is a Monday morning in early August. You have just joined a center that has fourteen machines on a six-month maintenance interval. Going through the files, you find that nothing has been done since the last licensing inspection, eleven months ago. The next inspection is in three weeks.</p>
<p>At the morning huddle, the chief technician, Mr. Rodel Mendoza, 51, proposes doing all fourteen machines in the two weeks before the inspector arrives. The unit will keep running its usual three shifts. The head nurse, Ms. Carmela Aquino, asks how many machines will be out at once.</p>
""", "questions": ["How many visits were due in the past eleven months, and what does that make the status of every machine?",
                  "What are the risks of fourteen visits in two weeks?",
                  "What do you report now, and what would a sound plan look like from now on?"]},
    "sections": [("L", "04", "program"),
        ("inventory", "Inventory", "The equipment inventory", """
<p>You cannot maintain what you have not listed. A machine missing from the list has no due date, so no visit is ever scheduled for it, and nobody notices until something fails. The inventory is the foundation of the program and one of the first things an inspector asks for.[[who_maint]][[doh2012]] Each field in it has a job.</p>
<div class="table-wrap"><table>
<thead><tr><th>Field</th><th>Why it is there</th></tr></thead>
<tbody>
<tr><td>Asset number, model, serial number</td><td>Unique identity</td></tr>
<tr><td>Location and station; hepatitis isolation assignment</td><td>Where it is now, and where it must stay</td></tr>
<tr><td>Date installed; acceptance test reference</td><td>The start of its history</td></tr>
<tr><td>Software version</td><td>Procedures and notices depend on it</td></tr>
<tr><td>Configured concentrate system and tubing set</td><td>Must match the unit&rsquo;s supplies</td></tr>
<tr><td>Maintenance interval; last visit; next due</td><td>Drives the calendar</td></tr>
<tr><td>Operating hours at last visit</td><td>For hour-based intervals</td></tr>
<tr><td>Electrical safety test: last and next due</td><td>A separate schedule in many centers</td></tr>
<tr><td>Status: in service, out of service, on loan, retired</td><td>So that nobody uses the wrong machine</td></tr>
</tbody></table></div>
<p>The list covers more than dialysis machines. Include reverse osmosis units and water system components if they fall to you, reprocessing machines, the defibrillator, patient scales, blood pressure monitors, infusion pumps, and the test instruments themselves. Scales and blood pressure monitors look like simple equipment, but they drive clinical decisions: the weight decides how much fluid is removed, and the monitor catches low blood pressure. A scale reading two kilograms wrong is a treatment error.</p>
"""),
        ("visit", "A maintenance visit", "A preventive maintenance visit, step by step", """
<p>A visit follows a fixed order for a reason. You decontaminate before you open anything, so you are not working in used dialysate. You record before you replace, so the history shows how the machine was performing. You test last, so the tests cover everything you touched.</p>
{{flow:The order of a visit|Prepare::Confirm the machine is free. Check the kit, manual revision, safety notices, and test instruments.|Receive::Tag out. Ask operators about any problems. Read the alarm history if the machine keeps one.|Decontaminate::Disinfection program and external wipe.|Inspect::Cabinet, hoses, connectors, cord, casters; look for leaks, scale, corrosion.|Replace::Wearing parts from the kit, by the manual.|Verify and calibrate::Temperature, conductivity, pressures, flows, ultrafiltration.|Test protection::Each protective system.|Electrical safety::If due, or if the work affected it.|Finish::Disinfect, residual test, record, release to the charge nurse.}}
<div class="table-wrap"><table>
<thead><tr><th>Often skipped</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Asking the operators first</td><td>They know the intermittent problems that you will not see on the bench</td></tr>
<tr><td>Recording as-found values before replacing or adjusting anything</td><td>It shows how the machine was performing for patients</td></tr>
<tr><td>Checking the battery</td><td>It is needed only on the day the power fails, and it must work then</td></tr>
<tr><td>Inlet and drain hoses</td><td>Old hoses harbor biofilm, and they split</td></tr>
<tr><td>Casters and brakes</td><td>A machine that rolls can pull on the patient&rsquo;s lines</td></tr>
<tr><td>Updating the inventory</td><td>The next due date is calculated from it</td></tr>
</tbody></table></div>
"""),
        ("notices", "Notices and software", "Safety notices, recalls, and software updates", """
<p>A manufacturer keeps learning about its machines after they are sold, from the reports of the centers that use them. When it finds a problem, such as a part that fails early, a software error, or a procedure that needs to change, it issues a notice. A notice may ask for an inspection, a part change, or an update by a certain date. It protects your patients only if it reaches you and you act on it.</p>
{{flow:Handling a safety notice|Receive::Make sure notices reach the technician, not only the purchasing office.|Identify::Which of your machines are affected, by model, serial range, and software version.|Act::Carry out the action by the stated date.|Record::Per machine: notice reference, date done, by whom.|Inform::The chief technician, charge nurse, and medical director, especially if use must change meanwhile.|Close::Return any acknowledgment the manufacturer requires.}}
<p>Software updates change how a machine behaves, sometimes in ways no one sees until an alarm or a screen looks different. Install only versions supplied by the manufacturer for that model. Record the old and new versions, repeat the tests that the update instructions call for, and tell operators about any change they will see on the screen. Keep all machines of one model on the same version where you can. A nurse who moves between two machines of the same model expects them to behave alike; mixed versions confuse operators and technicians.</p>
"""),
        ("spares", "Spares", "Spare parts and downtime", """
<div class="table-wrap"><table>
<thead><tr><th>Keep on site</th><th>Reason</th></tr></thead>
<tbody>
<tr><td>Maintenance kits for visits due in the next quarter</td><td>So that no visit is late for lack of parts</td></tr>
<tr><td>Fuses of every specified type</td><td>They are cheap, and the wrong one is dangerous</td></tr>
<tr><td>Common seals, O-rings, and dialyzer connector seals</td><td>Small leaks are frequent</td></tr>
<tr><td>Transducer protectors and internal filters</td><td>They are replaced after contamination</td></tr>
<tr><td>Inlet and drain hoses</td><td>They are replaced on schedule</td></tr>
<tr><td>A few high-failure parts, chosen from your own repair history</td><td>They shorten downtime</td></tr>
<tr><td>Residual test strips and approved disinfectants</td><td>Without them, no machine can be released</td></tr>
</tbody></table></div>
<p>Buy parts from the manufacturer or its authorized distributor, store them as the label says, and use the oldest first. Then track downtime. For each fault, count the days from tagging out to release, and write down the reason for any wait. The reasons tell you where the program is weak. If most downtime is spent waiting for parts, the stock list needs changing. If it is spent waiting for a technician, the staffing or training does.</p>
{{fig:dashboard|A few indicators, such as visits done on time and days out of service, show whether the program is keeping up.}}
"""),
    ],
    "debrief": ["""
<p><strong>How many visits were due, and the status of every machine.</strong> About twenty-six. Fourteen machines on a six-month interval need about twenty-six visits in eleven months. None were done, so every machine is overdue, some by five months. That is a reportable status, not a paperwork gap.</p>
<p><strong>The risks of fourteen visits in two weeks.</strong> Rushed work, skipped tests, several machines out at once with shifts cancelled, and no kits or calibrated instruments ready. Ms. Aquino&rsquo;s question is the right one. The plan also produces records that all carry the same fortnight&rsquo;s dates, which tells an inspector exactly what happened.</p>
<p><strong>What to report now, and the plan from now on.</strong> The honest course is to report the overdue status to the medical director now. Prioritize machines by time since the last visit and by any reported problems, do as many properly as can be done without compromising treatment, and record truthfully. From now on, keep a calendar with two or three visits a month, order kits a quarter ahead, review an overdue list monthly, and put maintenance on the agenda of the quality meeting.</p>
"""],
    "skills": {"title": "Building a maintenance calendar and running a visit",
        "intro": "Materials: the equipment inventory, service manuals, a year planner, one maintenance kit, and a blank visit checklist.",
        "items": [("Lists every machine with model, serial number, interval, and last visit date.", False),
                  ("Calculates the number of visits due per year and spreads them across the calendar.", False),
                  ("Identifies any machine currently overdue and reports it.", True),
                  ("Checks for open safety notices affecting each model.", True),
                  ("Follows the visit order: prepare, receive, decontaminate, inspect, replace, verify, test, finish.", False),
                  ("Asks the operators about problems before starting.", False),
                  ("Records as-found values before adjusting.", True),
                  ("Updates the inventory with the visit date and next due date.", False),
                  ("Releases the machine formally to the charge nurse.", True)],
        "placement": "Bring your center&rsquo;s inventory up to date for five machines, including software version and concentrate configuration."},
    "quiz_keep": [("04", [0, 6])],
    "quiz": [
        ("A center has fourteen machines on a six-month interval. How many visits are due each year?",
         ["7", "14", "28", "84"], 2, "Fourteen machines, twice a year each, is twenty-eight visits."),
        ("Why should patient scales be in the equipment inventory?",
         ["They are heavy", "A wrong weight leads to wrong fluid removal", "They use electricity", "They are not needed"], 1,
         "Scales and blood pressure monitors drive clinical decisions and need checking."),
        ("What is the first step when a manufacturer&rsquo;s safety notice arrives?",
         ["File it", "Identify which machines are affected by model, serial range, and software version", "Ignore it if machines seem fine", "Wait for the next visit"], 1,
         "Action starts with knowing which of your machines are covered."),
        ("Before starting a maintenance visit, whom should you ask about the machine?",
         ["Nobody", "The operators who use it", "The supplier&rsquo;s accountant", "The patients"], 1,
         "Operators know the intermittent problems."),
        ("Most of your downtime is machines waiting for parts. What should change?",
         ["Nothing", "The spare parts stock list", "The alarm volume", "The shift schedule"], 1,
         "Downtime reasons tell you where the program is weak."),
        ("After a software update, what must be recorded?",
         ["Nothing", "The old and new versions, the tests repeated, and the date", "Only the technician&rsquo;s mood", "The room temperature"], 1,
         "Software version is part of the machine&rsquo;s identity and history."),
    ],
    "terms": [("Recall", "A manufacturer&rsquo;s instruction to return, replace, or correct a product."),
              ("Operating hours counter", "The machine&rsquo;s record of how long it has run."),
              ("Authorized distributor", "A supplier approved by the manufacturer to sell its parts.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "Maintenance indicators in the quality program.")],
    "calcs": ["calc-dialysis-qapi-scorecard.html"],
}

NEW["09"] = {
    "image_alt": "A technician comparing a handheld reference meter with a machine display.",
    "keep": "04",
    "objectives": [
        "Explain calibration, tolerance, and the meaning of as-found and as-left values.",
        "Decide whether a reading is within tolerance, taking the reference instrument&rsquo;s own accuracy into account.",
        "Look after reference instruments and standard solutions and keep an instrument register.",
        "Act correctly when a reference instrument is found to be wrong.",
    ],
    "big": """
{{plain:Think of a tailor measuring cloth for a barong. Her tape measure has stretched a little over the years. If she checks it against a steel ruler and finds it a few millimeters long over a meter, she can still cut a good shirt, because a few millimeters do not matter for a sleeve. If the tape is off by a few centimeters, the shirt will not fit. Calibration answers the tailor&rsquo;s question about the machine: is what it says true? You answer it by comparing the machine with an instrument you trust more, and correcting the difference if it is too large.}}
<p>The picture has a limit. The tailor&rsquo;s steel ruler is close enough to perfect for cloth. Your reference meter is not perfect at the scale you work at, and its own error can be a large share of the difference you are trying to judge. Two details therefore separate careful calibration from guesswork: knowing how large a difference is allowed, and knowing how far your own instrument can be trusted.</p>
{{cards:Key terms for this module|Calibration::Comparing with a trusted reference and adjusting to match.|Verification::Comparing without adjusting, to confirm a reading is within tolerance.|Tolerance::The allowed difference.|Accuracy::How close an instrument&rsquo;s reading is to the true value.|As found, as left::The reading before and after adjustment.|Traceable::Linked by documented calibrations to a national or international standard.|Standard solution::A liquid of precisely known value used to check a meter.}}
""",
    "sections": [("L", "04", "calibration"),
        ("tolerance", "Tolerance", "Deciding whether a reading is within tolerance", """
<p>Every calibration procedure gives a tolerance: the largest acceptable difference between the machine and the reference. Your reference instrument is not perfect either; its certificate states its accuracy. So any difference you measure carries the reference&rsquo;s own uncertainty with it. Work through the illustration below slowly, because it shows why a reading that passes can still deserve attention.</p>
{{formula:<strong>Illustration.</strong> The manual allows &plusmn;0.2 mS/cm for dialysate conductivity. Your reference meter is accurate to &plusmn;0.05 mS/cm. The machine shows 14.0 and the reference reads 14.15. The difference is 0.15: within tolerance, but close. The true difference could be anywhere from 0.10 to 0.20. Recording the as-found value lets the next visit see whether it is drifting.}}
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>Decision</th></tr></thead>
<tbody>
<tr><td>Well within tolerance</td><td>Record it; do not adjust</td></tr>
<tr><td>Within tolerance but close to the edge, or moving the same way at each visit</td><td>Record it, and adjust if the manual permits; look for the cause of the drift, such as scale</td></tr>
<tr><td>Outside tolerance</td><td>Record the as-found value; clean or descale if relevant; calibrate; record the as-left value; report</td></tr>
<tr><td>Far outside tolerance</td><td>As above, and tell the chief technician and the charge nurse the same day, because patients may have been affected</td></tr>
<tr><td>Cannot be brought within tolerance</td><td>Take it out of service; repair it; then calibrate</td></tr>
</tbody></table></div>
{{key:A reference instrument should be several times more accurate than the tolerance you are checking. If your meter&rsquo;s own accuracy is as wide as the tolerance, it cannot tell you whether the machine passes or fails.}}
"""),
        ("L", "04", "reference"),
        ("care", "Instrument care", "Looking after reference instruments", """
<p>A reference instrument is accurate on the day the laboratory signs its certificate. What happens to it between that day and the next certificate is in your hands. The common mistakes in the table below are mistakes of handling, not faults of the instrument.</p>
<div class="table-wrap"><table>
<thead><tr><th>Instrument</th><th>Daily care</th><th>Check between calibrations</th><th>Common mistakes</th></tr></thead>
<tbody>
<tr><td>Conductivity meter</td><td>Rinse the cell with clean water and then with sample; keep it free of scale</td><td>Standard solution of a value near dialysate, on the day of use</td><td>Old or contaminated standard solution; wrong reference temperature; air bubble in the cell</td></tr>
<tr><td>Reference thermometer</td><td>Keep the probe clean and straight</td><td>Compare with a second thermometer or an ice-point check, as its instructions allow</td><td>Reading before the probe has settled</td></tr>
<tr><td>Pressure meter</td><td>Keep fluid out of it, and use a protector</td><td>Zero check open to air; comparison with a second meter</td><td>Leaking test tubing</td></tr>
<tr><td>Measuring cylinder or scale</td><td>Keep it clean and dry, on a level surface</td><td>Known weights for the scale</td><td>Reading the cylinder from above; a scale not zeroed</td></tr>
<tr><td>Electrical safety analyzer</td><td>Keep the leads undamaged</td><td>Self-check by its manual</td><td>Using it past its calibration date</td></tr>
<tr><td>Multimeter</td><td>Keep the leads and probes intact</td><td>Known source check</td><td>Wrong function selected</td></tr>
</tbody></table></div>
<p>A standard solution is only as good as the way it is kept. It has an expiry date and a stated value at a stated temperature. Water evaporates from an open bottle and leaves the salts behind, so the solution becomes stronger than its label. A probe dipped into the stock carries rinse water and residue into it. So pour out what you need; never dip a probe into the stock bottle or pour used solution back. Close the bottle at once.</p>
{{cards:The instrument register|Identity::Each instrument numbered and labeled.|Certificate::Date, laboratory, and next due date.|Label on the instrument::Showing the due date.|Use log::Which machines it was used on, and when.|Checks::Standard solution and zero checks recorded.|Out-of-tolerance events::What was found and which machines were reviewed.}}
"""),
        ("L", "04", "records")],
    "quiz_keep": [("04", [1, 2, 3, 4, 5, 7])],
    "quiz": [
        ("The tolerance is &plusmn;0.5 &deg;C. The machine shows 37.0 and a reference thermometer reads 37.4. What is correct?",
         ["Outside tolerance", "Within tolerance; record the as-found value and watch the trend", "The thermometer is broken", "Replace the heater"], 1,
         "A difference of 0.4 is within &plusmn;0.5, but close enough to follow."),
        ("Why should you never dip a probe directly into the stock bottle of standard solution?",
         ["It is slippery", "It contaminates the stock and changes its value", "It is too cold", "It damages the bottle"], 1,
         "Pour out a portion and discard it after use."),
    ],
}

NEW["10"] = {
    "image_alt": "A technician reading a residual test strip against its color chart.",
    "objectives": [
        "Explain what scale, organic film, and biofilm are and how each affects the machine.",
        "Select the approved program and agent for descaling, cleaning, and disinfection.",
        "Carry out disinfection with a documented residual test.",
        "Maintain inlet and drain hoses and the dialysis fluid filters at the machine.",
    ],
    "big": """
{{plain:Think of the water dispenser in a busy office. The bottle is changed often, but if nobody cleans the spout and the drip tray, they grow a slimy film, and the clean water picks it up on the way out. The fluid path of a dialysis machine is warm, wet, and fed with bicarbonate and used dialysate. Left alone, it would scale up and grow bacteria within days. So the machine cleans itself with heat or chemicals. Your work is to make sure the right program runs with the right agent, that the chemical is gone afterward, and that the hoses and filters around the machine are not undoing the work.}}
<p>The picture has a limit. An office dispenser is cleaned with soap and rinsed by eye. A dialysis machine is cleaned with chemicals strong enough to harm a patient, and the only proof that they are gone is a test.</p>
{{cards:Key terms for this module|Scale::A hard crust of calcium carbonate.|Descaling::Dissolving scale with acid.|Organic film::Protein and fat deposits from used dialysate.|Disinfection::Killing microbes with heat or chemicals.|Residual test::A test that proves the chemical has been rinsed out.|Dialysis fluid filter::A filter on the machine that holds back bacteria and endotoxin.|Air gap::A physical break between the drain hose and the drain that prevents backflow.}}
""",
    "case": ("L", "05"),
    "sections": [("L", "05", "why"), ("L", "05", "programs"),
        ("failed", "Failed cycles", "When a disinfection cycle fails", """
<p>A disinfection cycle can fail loudly, with a message on the screen, or quietly, with a positive residual test or a high culture result days later. Read the table by its middle column. Most failures have a cause outside the program itself, so look for it before you rerun.</p>
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>Likely cause</th><th>What to do</th></tr></thead>
<tbody>
<tr><td>Machine reports disinfection incomplete</td><td>Empty or disconnected chemical container; intake valve stuck; power interruption</td><td>Check the container and pick-up; rerun; if it fails again, take the machine out of service</td></tr>
<tr><td>Heat disinfection does not reach temperature</td><td>Scaled or failing heater; low flow</td><td>Descale, check the heater, and rerun</td></tr>
<tr><td>Residual test still positive after the rinse</td><td>Rinse too short; a dead space holding chemical; wrong dilution</td><td>Rinse again and retest; if the result stays positive, find the cause before use</td></tr>
<tr><td>Residual strips out of date or the wrong type for the agent</td><td>Stock control</td><td>Obtain the correct strips; until then, the machine waits</td></tr>
<tr><td>Scale returns quickly</td><td>Descaling too infrequent; bicarbonate settings; hard water</td><td>Compare with the other machines, and ask the water technician</td></tr>
<tr><td>Dialysis fluid cultures high on one machine</td><td>Biofilm in hoses or the hydraulic path; overdue filter; contaminated bicarbonate connector</td><td>Replace the hoses and filter, disinfect repeatedly, and resample</td></tr>
<tr><td>Machine left idle for days</td><td>Stagnant water in the fluid path</td><td>Disinfect before use, as the manual and unit procedure state</td></tr>
</tbody></table></div>
{{key:When the machine says a program has finished, it tells you the steps ran. Only the residual test tells you the chemical is gone.}}
"""),
        ("hoses", "Hoses and drain", "Inlet hoses, drain hoses, and the air gap", """
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Risk</th><th>Practice</th></tr></thead>
<tbody>
<tr><td>Inlet hose from the wall outlet</td><td>Biofilm; stagnant water overnight; kinks</td><td>Keep it as short as practical, include it in disinfection by the unit&rsquo;s method, and replace it on schedule</td></tr>
<tr><td>Concentrate pick-up tubes and connectors</td><td>Bicarbonate crystals; bacterial growth on the bicarbonate side</td><td>Rinse and disinfect them with the machine, and inspect them for crystals and cracks</td></tr>
<tr><td>Drain hose</td><td>Backflow of drain contents into the machine</td><td>The end sits above the drain with an air gap; it is never pushed down into the drain or left under water</td></tr>
<tr><td>Drain itself</td><td>Blockage floods the station; splashing spreads contamination</td><td>Report slow drains, and keep the area clean</td></tr>
</tbody></table></div>
<p>The air gap deserves a moment, because it works by physics, not by a valve that can fail. If the end of the drain hose sits in standing waste water, and the pressure in the drain rises or the machine draws back, waste can be pulled up into the machine. Water cannot jump across open air. A visible gap between the hose end and the drain makes backflow physically impossible. Check it every time you move a machine.</p>
"""),
        ("filters", "Machine filters", "Dialysis fluid filters at the machine", """
{{fig:wts_pou}}
<p>Most modern machines pass dialysate through one or more fine filters before it reaches the dialyzer. The filters hold back bacteria and endotoxin, and they are what makes ultrapure dialysis fluid possible. For hemodiafiltration, where fluid is infused directly into the blood, they are the final safety barrier.[[iso23500_5]] A filter that is past its life or has a leak still lets fluid through, so the treatment runs normally and nothing on the screen looks wrong. That is why filters are managed by date and by test, not by appearance.</p>
<div class="table-wrap"><table>
<thead><tr><th>What to manage</th><th>How</th></tr></thead>
<tbody>
<tr><td>Life</td><td>Each filter has a maximum number of treatments, days, or disinfections, set by its maker. Write the installation date and the due date on the filter or its tag</td></tr>
<tr><td>Integrity</td><td>Many machines test filter integrity automatically. A failed test means replacement, not a retry until it passes</td></tr>
<tr><td>Disinfection</td><td>Filters are disinfected with the machine; use only agents that the filter tolerates</td></tr>
<tr><td>Replacement</td><td>Use clean technique, then follow the manual&rsquo;s priming and test steps</td></tr>
<tr><td>Records</td><td>For each machine: filter lot, date fitted, and date due</td></tr>
</tbody></table></div>
{{stop:An overdue or failed dialysis fluid filter means the machine is not producing fluid of the quality it claims. Replace the filter before the next treatment.}}
"""),
    ],
    "debrief": ("L", "05"),
    "skills": {"title": "Disinfection with residual test, hose check, and filter change",
        "intro": "Materials: an out-of-service machine, its manual, approved agents, residual strips for those agents, protective equipment, a replacement dialysis fluid filter, and the machine&rsquo;s record.",
        "items": [("Selects the program and agent approved for the stated purpose.", True),
                  ("Wears the protective equipment on the safety data sheet.", False),
                  ("Allows the full cycle and rinse to complete.", True),
                  ("Performs the residual test with the correct strip at the stated outlet and time.", True),
                  ("Inspects the inlet hose and concentrate connectors and states their replacement dates.", False),
                  ("Confirms the drain hose has an air gap.", True),
                  ("Checks the dialysis fluid filter&rsquo;s due date and replaces it by the manual if due.", True),
                  ("Records agent, program, times, residual result, and filter details.", False)],
        "placement": "Check the drain air gap and filter due date on every machine on the floor and report what you find."},
    "quiz_keep": [("05", [0, 1, 2, 3, 4])],
    "quiz": [
        ("The machine displays &ldquo;disinfection complete.&rdquo; What still has to be shown before use after a chemical program?",
         ["Nothing", "A negative residual test", "A full concentrate container", "A warm cabinet"], 1,
         "Completion of the program does not prove the chemical was rinsed out."),
        ("Why must the drain hose end above the drain with a visible gap?",
         ["To reduce noise", "To prevent waste water being drawn back into the machine", "To cool the hose", "For appearance"], 1,
         "An air gap makes backflow physically impossible."),
        ("A dialysis fluid filter fails its integrity test. What is correct?",
         ["Repeat until it passes", "Replace it by the manual", "Ignore it", "Disable the test"], 1,
         "A failed filter may pass bacteria and endotoxin."),
    ],
    "terms": [("Integrity test", "A test showing a filter has no leaks."),
              ("Ultrapure dialysis fluid", "Dialysis fluid with very low bacteria and endotoxin, produced by filtering at the machine."),
              ("Backflow", "Fluid moving backward into a clean system.")],
    "readings": [("dialysis-water-treatment-systems.html", "Fluid quality from the loop to the machine."),
                 ("hemodiafiltration-deep-dive.html", "Why ultrapure fluid and machine filters matter.")],
}

NEW["11"] = {
    "image_alt": "A technician connecting an electrical safety analyzer to a machine&rsquo;s power cord.",
    "objectives": [
        "Explain why dialysis patients are especially vulnerable to electrical faults.",
        "Carry out a visual inspection and an electrical safety test in the correct order.",
        "Describe the utilities each station needs and how each can fail.",
        "Work with the facility engineer on outlets, grounding, backup power, water, and drains.",
    ],
    "big": """
{{plain:Think of a new rice cooker plugged into an old, loose outlet with a tangle of extension cords behind it. The cooker may be in perfect condition, but the household is only as safe as the weakest connection in that chain. A dialysis machine is the same. It is safe only as part of a chain: the building&rsquo;s wiring, the wall outlet, the cord, and the machine&rsquo;s own protection. This module covers the periodic electrical test on the machine and the utilities at the station that the machine depends on: power, water, drain, and backup supply.}}
<p>The picture has a limit. A rice cooker touches dry hands for a moment. A dialysis machine is connected to a patient through blood and saline for hours, and a fault too small to notice at home can matter at the chair.</p>
{{cards:Key terms for this module|Protective earth::The grounding path that carries fault current away from the case.|Leakage current::Small unwanted current flowing to earth or through a person.|Insulation::Material that keeps electricity in its intended path.|Electrical safety analyzer::The instrument that measures earth resistance and leakage.|Grounded outlet::A socket with a working earth connection.|Backup power::A generator or battery supply used when mains fails.|Air gap::A break between drain hose and drain that prevents backflow.}}
""",
    "case": {"title": "A tingle from the machine case", "html": """
<p>It is Thursday, 11:10 in the morning, between shifts. The nurse, Ms. Rowena Pascual, 34, comes to the workshop. While rinsing her hands at the station sink, she rested her other hand on the metal side of machine 8 and felt a slight tingle. The machine works normally and shows no alarms.</p>
<p>You go to the station. Machine 8 is plugged into a multi-socket extension, because the wall outlet at that station &ldquo;has been loose for months.&rdquo; The schedule shows that a patient with a central venous catheter is due on machine 8 in an hour.</p>
""", "questions": ["What does the tingle tell you?",
                  "What is done with the machine and the station right now, and whom do you tell?",
                  "Which two separate problems need fixing, and how do you keep them from returning?"]},
    "sections": [
        ("why", "Why it matters", "Why dialysis patients are vulnerable", """
<p>Current that enters the body must pass through the skin, and dry skin resists electricity well. A dialysis patient has no such barrier at the access. The patient is connected to the machine by blood and saline, which conduct well, and some patients have a catheter whose tip lies close to the heart. A current too small for a healthy person to feel can then be dangerous. For this reason medical equipment is built with stricter limits than household appliances, and dialysis machines used with central venous catheters carry particular requirements.[[iec60601]][[iec60601_2_16]]</p>
{{cards:Layers of protection|Insulation::Keeps mains voltage inside the wiring.|Protective earth::Carries fault current away and blows the fuse.|Low leakage design::Limits the tiny currents that always flow.|Building protection::Grounded outlets and protective devices in the distribution board.|Inspection and testing::Finds a failed layer before a second one fails.}}
"""),
        ("L", "05", "electrical"),
        ("inspect", "Inspection first", "Visual inspection comes first", """
<p>A large share of electrical safety failures can be seen before any meter is connected. A cracked plug or a taped cord is a fault already, and finding it by eye first saves time. Inspect in the same order every time.</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Look for</th><th>If found</th></tr></thead>
<tbody>
<tr><td>Plug</td><td>Cracks, bent or discolored pins, a missing or loose earth pin</td><td>Replace it with the approved part, then test</td></tr>
<tr><td>Cord</td><td>Cuts, flattening, tape, stiffness, exposed inner wires at the ends</td><td>Replace; never tape</td></tr>
<tr><td>Strain relief</td><td>Cord pulled out of its grip</td><td>Repair it, and check the internal connections</td></tr>
<tr><td>Case and panels</td><td>Cracks, missing screws, panels that do not close</td><td>Repair before testing</td></tr>
<tr><td>Signs of fluid</td><td>Water marks, corrosion, crystals inside or under the cabinet</td><td>Find the leak, dry and clean, then test</td></tr>
<tr><td>Labels</td><td>Rating plate and warnings legible</td><td>Replace labels by the manual</td></tr>
<tr><td>Accessories</td><td>Non-standard adapters or extension leads</td><td>Remove them, and report</td></tr>
</tbody></table></div>
{{flow:Order of an electrical safety test|Visual inspection::Fix what you find first.|Protective earth resistance::Earth pin to exposed metal, flexing the cord while measuring.|Insulation or leakage tests::By the method the standard and the manual specify for this class of equipment.|Function check::The machine starts and runs normally.|Label and record::Date, results against limits, analyzer identity, next due date.}}
<p>The rating plate tells you the machine&rsquo;s protection class and the type of its patient connection, and the limits for leakage current depend on both. Take the limits from the standard and the service manual, and let the analyzer&rsquo;s automatic sequence apply them where it can. Flex the cord during the earth test. A broken strand inside the cord may touch its other end in one position and part in another, so a cord lying still can pass a test it would fail when a nurse moves the machine.[[iec62353]]</p>
"""),
        ("utilities", "Station utilities", "The utilities at each station", """
<div class="table-wrap"><table>
<thead><tr><th>Utility</th><th>What the machine needs</th><th>How it fails</th><th>Who fixes it</th></tr></thead>
<tbody>
<tr><td>Power outlet</td><td>Correct voltage; a working earth; a circuit that can carry the heater&rsquo;s load</td><td>Loose socket; earth not connected; overloaded circuit tripping during heat disinfection</td><td>Facility electrician</td></tr>
<tr><td>Treated water outlet</td><td>Pressure and flow within the machine&rsquo;s stated range</td><td>Low pressure at peak demand; leaking connector; dead leg when the station is unused</td><td>Water technician</td></tr>
<tr><td>Drain</td><td>Free flow; an air gap</td><td>Blockage; hose submerged; backflow</td><td>Facility maintenance; you check the air gap</td></tr>
<tr><td>Central concentrate outlets, if fitted</td><td>Correct formula; correct connector</td><td>Wrong line; crystals; leaks</td><td>Water technician</td></tr>
<tr><td>Backup power</td><td>Enough capacity for what the plan says it supplies</td><td>Generator does not start; changeover delay; supplies lights only</td><td>Facility engineer</td></tr>
</tbody></table></div>
<p>The machine draws on everything in this table, and a fault in any row reaches the patient through the machine. Outlets are tested, too. A simple outlet tester shows whether live, neutral, and earth are connected correctly. A qualified electrician measures earth quality and checks the protective devices in the distribution board. Keep a list of every station outlet with the date it was last verified.</p>
{{stop:Extension leads, multi-socket adapters, and two-pin adapters are not used for dialysis machines. They add resistance to the earth path, overload easily, and may have no earth at all.}}
"""),
        ("backup", "Backup power", "What happens when the power fails", """
<p>A power failure gives you no time to read a manual. Know, before it happens, what each machine does on mains failure. It differs between models.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Where to find the answer</th></tr></thead>
<tbody>
<tr><td>Does the machine have an internal battery, and what does it keep running?</td><td>Instructions for use. Commonly the blood pump, the air detector, and alarms for a limited time, so blood can be kept moving or returned; usually not the heater or dialysate preparation</td></tr>
<tr><td>How long does the battery last, and when was it last tested?</td><td>Manual; your maintenance record</td></tr>
<tr><td>Is there a hand crank for the blood pump?</td><td>On the machine; check it is present at every visit</td></tr>
<tr><td>What does the generator supply, and how long is the changeover?</td><td>Facility engineer; the unit&rsquo;s contingency plan</td></tr>
<tr><td>Does the water system run on backup power?</td><td>Water technician; contingency plan</td></tr>
<tr><td>Do machines restart correctly when power returns?</td><td>Test it, by the manual, on an out-of-service machine</td></tr>
</tbody></table></div>
{{fig:typhoon}}
<p>Batteries age silently. A battery that runs the machine at start-up may not last the minutes that a real outage demands. Test each machine&rsquo;s battery at the interval in its manual by running on battery for the stated time, and replace it at the stated age even if it still seems to work. After any power event, ask the nurses how the machines behaved. That is free information about your batteries.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What the tingle tells you.</strong> Current is flowing from the machine&rsquo;s case through Ms. Pascual to the grounded tap. The case is not properly earthed, there is leakage inside the machine, or both. For a patient with a central venous catheter this is a serious hazard.</p>
<p><strong>What happens right now, and whom you tell.</strong> Unplug machine 8 and tag it out of service, and do not use the station. Tell the charge nurse, who moves the patient to another station. The move is the nurse&rsquo;s decision; your part is to make sure no one connects a patient to machine 8 or that outlet.</p>
<p><strong>The two problems, and keeping them from returning.</strong> First, the machine: a visual inspection, then a full electrical safety test. Find the source of the leakage, often moisture or a damaged cord, and repair it. Second, the building: the electrician repairs and tests the loose wall outlet, and the extension lead is removed from the unit. Then ask how a loose outlet stayed unreported for months, and check the other stations.</p>
"""],
    "skills": {"title": "Electrical safety test with an analyzer",
        "intro": "Materials: an out-of-service machine, its service manual, an electrical safety analyzer with a valid calibration, an outlet tester, and the test record.",
        "items": [("Carries out the visual inspection in order and corrects or reports defects before testing.", True),
                  ("Checks the analyzer&rsquo;s calibration date and leads.", True),
                  ("Measures protective earth resistance while flexing the cord and compares with the limit.", True),
                  ("Performs the leakage or insulation tests by the manual&rsquo;s method and compares with the limits.", True),
                  ("Confirms the machine functions normally afterward.", False),
                  ("Tags the machine out of service if any test fails.", True),
                  ("Records values, limits, analyzer identity, and the next due date, and labels the machine.", False),
                  ("Checks the station outlet with an outlet tester and reports any fault to the facility electrician.", False),
                  ("Confirms no extension leads or adapters are in use at the station.", True)],
        "placement": "With the facility engineer, find out what the generator supplies in your unit and how long the changeover takes, and add it to the contingency plan if it is missing."},
    "quiz_keep": [("05", [5, 6, 7])],
    "quiz": [
        ("A nurse feels a tingle from a machine&rsquo;s metal case. What is the correct first action?",
         ["Ask her to wear gloves", "Unplug the machine, tag it out, and keep the station out of use", "Continue and test later", "Turn down the alarm"], 1,
         "A tingle means current is flowing through a person; the hazard is immediate."),
        ("Why is the power cord flexed during the protective earth test?",
         ["To warm it", "A broken strand may connect in one position only", "To stretch it", "It is not necessary"], 1,
         "Flexing reveals intermittent breaks."),
        ("Why are extension leads not used for dialysis machines?",
         ["They are the wrong color", "They add resistance to the earth path, overload, and may lack an earth", "They are too long", "They are expensive"], 1,
         "The earth path must be direct and reliable."),
        ("On mains failure, what does a machine&rsquo;s internal battery commonly keep running?",
         ["Everything, indefinitely", "The blood pump, air detector, and alarms for a limited time", "The heater only", "Nothing"], 1,
         "Batteries typically support the blood side briefly; check the model&rsquo;s instructions."),
        ("A machine passes its electrical safety test but its wall outlet has no earth. Is the patient protected?",
         ["Yes", "No; the earth path depends on the outlet and building wiring too", "Only at night", "Only with a new cord"], 1,
         "Protection is a chain from the building to the machine."),
    ],
    "terms": [("Protection class", "How a device protects against electric shock; Class I equipment relies on a protective earth."),
              ("Strain relief", "The grip that stops the cord being pulled out of its connection."),
              ("Distribution board", "The panel holding the building&rsquo;s circuit breakers and protective devices."),
              ("Outlet tester", "A plug-in device that shows whether an outlet is wired correctly.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "Power and water in disaster planning."),
                 ("code-blue-acls-dialysis-unit.html", "Electrical safety around defibrillation at the dialysis chair.")],
    "calcs": ["calc-dialysis-continuity-planner.html"],
}

NEW["12"] = {
    "image_alt": "A technician and a charge nurse signing a return-to-service form beside a machine.",
    "keep": "06",
    "sections": [("L", "06", "method"),
        ("worked", "Worked example", "A fault worked through from start to finish", """
<p>The method is easiest to learn by following one fault all the way through. Operators report that machine 11 gives a low conductivity alarm &ldquo;about once a shift.&rdquo; The alarm clears by itself, and the machine passes every start-up test. Intermittent faults like this one tempt you to replace parts until the complaints stop. Notice instead how each step below narrows the search.</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>What was done</th><th>What it showed</th></tr></thead>
<tbody>
<tr><td>Gather</td><td>Asked the operators for times; read the alarm history</td><td>Alarms cluster twenty to forty minutes after start, on different patients</td></tr>
<tr><td>One or several?</td><td>Checked neighboring machines on the same concentrate supply</td><td>No alarms elsewhere, so not the supply</td></tr>
<tr><td>Simple things</td><td>Inspected concentrate connectors and pick-up tubes</td><td>Bicarbonate connector seal worn; tiny bubbles in the line</td></tr>
<tr><td>Test one idea</td><td>Replaced the seal; ran the machine for an hour on the bench</td><td>No bubbles; no alarm</td></tr>
<tr><td>Ask why</td><td>Why did the seal wear? Checked the connector for bicarbonate crystals</td><td>Crystals found; the connector was not being rinsed in the disinfection routine</td></tr>
<tr><td>Verify</td><td>Conductivity against reference; bypass proof; fluid balance test because air had been entering</td><td>All within tolerance</td></tr>
<tr><td>Release</td><td>Disinfection, residual test, record, handover</td><td>The charge nurse was told the cause and asked to report any recurrence</td></tr>
<tr><td>Prevent</td><td>Checked the same connector on every machine; raised the rinsing step with the head nurse</td><td>Two more worn seals found and replaced</td></tr>
</tbody></table></div>
{{key:The repair was a seal worth a few pesos. The real value was in the last two rows: asking why it wore, and looking at every other machine.}}
"""),
        ("L", "06", "verify"),
        ("life", "Life cycle", "From acceptance to retirement", """
<p>A machine&rsquo;s file starts before its first patient and ends after its last. Think of the machine as a staff member with a career: it is chosen, checked on arrival, looked after for years, reviewed, and finally retired with a record of why.</p>
{{flow:The life of a machine|Selection::Technicians advise on serviceability, parts supply, and training.|Delivery and installation::Checked against the order; installed by the manual.|Acceptance testing::Proved safe and accurate before first use.|Service life::Maintenance, calibration, repairs, notices, updates.|Review::Fault history and costs looked at yearly.|Retirement::A documented decision; decontaminated; removed from the inventory.}}
<div class="table-wrap"><table>
<thead><tr><th>Acceptance test item</th><th>Purpose</th></tr></thead>
<tbody>
<tr><td>Inspection for transport damage; accessories and manuals present</td><td>You start from a complete, undamaged machine</td></tr>
<tr><td>Electrical safety test</td><td>It gives baseline values for later comparison</td></tr>
<tr><td>Configuration: concentrate system, tubing set, syringe type, language, limits</td><td>The machine matches this unit&rsquo;s supplies and practice</td></tr>
<tr><td>Verification of temperature, conductivity, pressures, flows, ultrafiltration</td><td>It is accurate on arrival</td></tr>
<tr><td>Functional tests of every protective system</td><td>It is safe on arrival</td></tr>
<tr><td>Disinfection and residual test</td><td>It is clean before first use</td></tr>
<tr><td>Entry in the inventory; maintenance dates set</td><td>The program now includes it</td></tr>
<tr><td>Operator training recorded</td><td>The users know this model</td></tr>
</tbody></table></div>
<p>A new machine is not proven safe because it is new. It may have been damaged in transport, or configured for different supplies. Acceptance testing is what turns a delivered box into a machine you can vouch for.</p>
<p>At the other end, retirement is considered when parts are no longer supplied, faults are frequent, repair cost approaches replacement cost, or the manufacturer ends support. A retired machine is decontaminated, clearly labeled, removed from the inventory, and disposed of by the facility&rsquo;s procedure. It is not quietly kept as a source of spare parts for machines in service unless the manufacturer permits it.</p>
"""),
        ("L", "06", "records"), ("L", "06", "quality"),
        ("capstone", "Capstone", "Capstone: four practical stations", """
<p>To finish the track, you show that you can do the work, not only describe it. A senior technician observes you at four stations on an out-of-service machine. Each station brings together skills from several modules. All critical steps must be satisfactory.</p>
<div class="table-wrap"><table>
<thead><tr><th>Station</th><th>Task</th><th>Critical steps</th></tr></thead>
<tbody>
<tr><td>1. Safe preparation</td><td>Take a machine out of service and prepare it for work</td><td>Tag; disinfection confirmed; isolated and locked out; correct manual</td></tr>
<tr><td>2. Verification</td><td>Verify conductivity and temperature against reference instruments and prove bypass</td><td>Instrument dates checked; as-found recorded; correct pass or fail decision; bypass shown</td></tr>
<tr><td>3. Protective systems and electrical safety</td><td>Test the air detector and clamp; run an electrical safety test</td><td>Pump stop and clamp closure shown; earth and leakage within limits; failed test means out of service</td></tr>
<tr><td>4. Fault and release</td><td>Find a simulated fault set by the assessor, repair, verify, and hand over</td><td>Simple and shared causes checked first; required post-repair tests done; residual test; handover to the charge nurse before the tag is removed</td></tr>
</tbody></table></div>
{{cards:To complete the track|All twelve self-assessments::Attempted, with missed items reviewed.|Every critical checklist step::Demonstrated.|Manufacturer training::Completed for each model you will service.|One full maintenance visit and one repair::Documented and reviewed.|Four capstone stations::All critical steps satisfactory.|Sign-off::Recorded per machine model.}}
"""),
    ],
    "quiz_keep": [("06", [0, 1, 2, 3, 4, 5, 6, 7])],
    "quiz": [
        ("A new machine arrives. What must happen before its first patient?",
         ["Nothing; it is new", "Acceptance testing, configuration for the unit, disinfection, and entry in the inventory", "Only plugging it in", "A coat of paint"], 1,
         "New machines can be damaged in transport or configured for different supplies."),
        ("After fixing a worn seal that caused an intermittent alarm, what is the most valuable next step?",
         ["Close the ticket", "Ask why it wore and check the same part on the other machines", "Order a new machine", "Raise the alarm limit"], 1,
         "Finding the cause and checking for the same problem elsewhere prevents repeats."),
    ],
}
