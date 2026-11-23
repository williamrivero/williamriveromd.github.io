# -*- coding: utf-8 -*-
"""Biomedical Technician track, 12-module edition: new content for Modules 1 to 6.
compose.py combines this with sections reused from legacy/ (the original six modules). Format as in
water_treatment/deep_a.py."""

NEW = {}

NEW["01"] = {
    "image_alt": "A biomedical technician placing an out-of-service tag on a hemodialysis machine.",
    "keep": "01",
    "sections": [("L", "01", "role"), ("L", "01", "hazards"),
        ("decon", "Decontamination", "Decontaminating a machine before service", """
<p>Think of a machine coming off the treatment floor the way you would think of a cutting board after raw chicken. It may look clean, but it has had blood near it for hours. Treat it as contaminated inside and out until you have dealt with both.</p>
<p>The picture has a limit. You can see and scrub every side of a cutting board. A dialysis machine hides blood in places you cannot see from the outside, and some of those places are inside the cabinet. That is why decontamination follows a set order, not a quick wipe.</p>
{{flow:Before the cabinet is opened|Fluid path::Run the machine&rsquo;s own disinfection program to completion.|Outside::Wipe every external surface with the approved disinfectant, and observe its contact time.|Blood side parts::Inspect the pressure ports, the blood pump housing, and the venous clamp area for dried blood.|Transducer protectors::If blood or fluid has passed one, clean or replace the internal line and filter by the manual.|Yourself::Gloves and eye protection on; cuts covered.|Afterward::Remove gloves, clean your hands, and clean your tools.}}
<div class="table-wrap"><table>
<thead><tr><th>Where blood hides</th><th>What to do</th></tr></thead>
<tbody>
<tr><td>Behind the blood pump rotor</td><td>Remove the rotor by the manual and clean the housing</td></tr>
<tr><td>Inside pressure sensor ports</td><td>Follow the manual&rsquo;s internal decontamination; replace the internal protectors</td></tr>
<tr><td>Venous clamp and air detector slot</td><td>Clean with an approved agent that will not damage the sensor</td></tr>
<tr><td>Drip tray and base</td><td>Clean and disinfect; look for the source of any leak</td></tr>
<tr><td>Casters and rear panel</td><td>Often missed in routine wiping; clean them before the machine comes into the workshop</td></tr>
</tbody></table></div>
{{key:If you find blood inside a machine, tell the charge nurse. It means a protector failed or was wetted in use, and operators need to know.}}
<p>Protect yourself as well. Hepatitis B vaccination and a known antibody response are standard for anyone who handles dialysis equipment; ask your facility&rsquo;s occupational health contact about yours. Report a needlestick or a splash to the eye the same hour, and have it assessed, exactly as clinical staff do.</p>
"""),
        ("L", "01", "tagging"),
        ("manual", "The service manual", "Using the service manual", """
<p>A service manual is written for one model, and often for one software version. A manual that is almost right is a common source of wrong adjustments, because its numbers look reasonable and nothing warns you that they belong to a different machine.</p>
{{cards:Parts of a service manual you will use most|Flow diagram::Every component of the fluid path in order, with reference numbers.|Maintenance schedule::What is replaced and checked at each interval.|Calibration procedures::Step by step, with tolerances.|Fault tables::Alarm codes, with likely causes and checks.|Service mode::How to reach the technician&rsquo;s screens for tests and calibration.|Parts list::Part numbers and exploded drawings.|Test procedures::What must be tested after each kind of repair.}}
<div class="table-wrap"><table>
<thead><tr><th>Before you start, confirm</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Model and serial number on the machine&rsquo;s rating plate</td><td>Models that look alike can differ inside</td></tr>
<tr><td>Software version shown at start-up or in service mode</td><td>Procedures and limits change between versions</td></tr>
<tr><td>Manual revision and date</td><td>Manufacturers issue updates and corrections</td></tr>
<tr><td>Any safety notice or service bulletin for this model</td><td>It may change a procedure or require a part</td></tr>
<tr><td>Your own training status for this model</td><td>Authorization is per model, not per brand</td></tr>
</tbody></table></div>
<p>Service mode opens settings that can change how the machine treats patients. Leave nothing altered that the procedure did not tell you to alter, and exit service mode fully before you release the machine.</p>
"""),
        ("L", "01", "records")],
    "quiz_keep": [("01", [0, 1, 2, 3, 4, 5, 6, 7])],
    "quiz": [
        ("Before using a service procedure, which three things should match the machine in front of you?",
         ["Color, height, weight", "Model, software version, and manual revision", "Station number, shift, nurse", "Brand of concentrate"], 1,
         "Procedures and tolerances are specific to model and software version."),
        ("You find dried blood around an internal pressure port. What does this tell you?",
         ["Nothing unusual", "A transducer protector failed or was wetted in use; decontaminate by the manual and inform the charge nurse", "The heater is scaled", "The machine is new"], 1,
         "Blood inside the machine is an infection risk and a sign of a use problem to correct."),
    ],
}

NEW["02"] = {
    "image_alt": "A technician holding multimeter probes over a training circuit board on an antistatic mat.",
    "objectives": [
        "Explain voltage, current, and resistance in plain terms, and relate them to faults.",
        "Trace mains power into a machine, and explain the role of fuses and protective earth.",
        "Identify the main sensors and actuators in a dialysis machine and say what each one does.",
        "Use a multimeter safely for voltage, continuity, and resistance checks.",
    ],
    "big": """
{{plain:Think of an aircon in a sari-sari store. A thermostat feels the room, a small board decides, and the compressor runs until the room is cool. Every function of a dialysis machine is a loop like that: a sensor measures something, a control board decides, and an actuator, meaning a pump, valve, or heater, does something about it. Once you can see those loops, the inside of the machine stops being a box of wires and becomes a set of small systems you can understand one at a time.}}
<p>The picture has a limit. If the aircon&rsquo;s thermostat fails, the store gets warm and someone complains. A dialysis machine cannot wait for a complaint. So it adds what the aircon lacks: a second, independent sensor that watches the loop and forces a safe state if the loop goes wrong.</p>
{{flow:One control loop|Sensor::Measures temperature, pressure, conductivity, flow, or position.|Control board::Compares the reading with the target.|Actuator::A heater, pump, or valve changes the process.|Result::The reading moves toward the target.|Protective sensor::Independently checks the result and can force a safe state.}}
{{cards:Key terms for this module|Voltage::The electrical push, measured in volts.|Current::The flow of electricity, measured in amperes.|Resistance::Opposition to flow, measured in ohms.|Fuse::A deliberate weak link that melts when current is too high.|Protective earth::The wire that carries fault current safely away from the metal case.|Sensor::A device that turns a physical quantity into an electrical signal.|Actuator::A device that turns an electrical signal into movement, flow, or heat.|Continuity::An unbroken electrical path.}}
""",
    "case": {"title": "The fuse that keeps blowing", "html": """
<p>On a Saturday evening, after the last shift, machine 8 blows its main fuse during heat disinfection. The junior technician on duty, Mr. Jomar Aquino, replaces it. It blows again. He then fits a fuse of a higher rating &ldquo;so it will stop tripping.&rdquo; The machine completes disinfection.</p>
<p>On Monday morning, the chief technician, Mr. Ramon Cruz, opens the workshop and notices that the heater area of machine 8 smells of hot plastic.</p>
""", "questions": ["What was the fuse telling you?",
                  "What is the danger of a higher-rated fuse?",
                  "What should have been done?"]},
    "sections": [
        ("basics", "Volts, amps, ohms", "Voltage, current, and resistance", """
<p>Picture the water pipes of a house. Voltage is like the water pressure. Current is like the flow in the pipe. Resistance is like the narrowness of the pipe. More pressure pushes more flow, and a narrower pipe lets less through. The three are tied together by one rule.</p>
{{formula:<strong>Voltage = current &times; resistance</strong> (Ohm&rsquo;s law)<br><strong>Power = voltage &times; current</strong><br>Illustration: a heater element of 30 ohms on a 230-volt supply draws about 230 &divide; 30 = 7.7 amperes and gives about 230 &times; 7.7 = 1,770 watts of heat.}}
<p>Most electrical faults are one of four kinds. Each changes resistance in a particular way, and each shows itself in a particular way.</p>
<div class="table-wrap"><table>
<thead><tr><th>Fault</th><th>In electrical terms</th><th>What you see</th></tr></thead>
<tbody>
<tr><td>Open circuit</td><td>A break: resistance is infinite, and no current flows</td><td>A pump or valve that does nothing; a sensor reading stuck at the end of its scale</td></tr>
<tr><td>Short circuit</td><td>An unintended low-resistance path, with very high current</td><td>A blown fuse, a tripped breaker, a burning smell</td></tr>
<tr><td>High-resistance joint</td><td>A loose or corroded connection</td><td>Intermittent faults, heat at the connector, readings that jump</td></tr>
<tr><td>Leakage to earth</td><td>Current finding a path to the case, often through moisture</td><td>Tripped earth-leakage protection; a failed electrical safety test</td></tr>
</tbody></table></div>
<p>Dialysis machines keep water and electricity in one cabinet, and moisture is behind a large share of their electrical faults. The sequence is slow and predictable. A small leak drips on a connector. The metal corrodes. Resistance rises, the joint heats, and eventually current leaks to the case. When you fix an electrical fault, look for water.</p>
"""),
        ("power", "Power and earth", "The power path, fuses, and protective earth", """
{{flow:From the wall to the electronics|Outlet::Live, neutral, and protective earth.|Power cord and plug::The earth pin is the longest, so it connects first.|Mains switch and fuses::Cut power and protect against overload.|Power supply::Converts mains voltage to the low voltages the boards use.|High-power parts::The heater and some pumps run at mains voltage.|Low-voltage parts::Boards, sensors, and small valves.}}
<p>The manufacturer chooses each fuse for three things: its current rating, its speed (fast or slow-blow), and its voltage rating. Replace a fuse only with the exact type in the manual. A fuse that blows once may simply have aged. A fuse that blows again has found a fault.</p>
{{stop:Never fit a fuse of a higher rating, and never bridge a fuse. The fuse protects the wiring from fire and the patient from a fault. If it blows twice, the machine is out of service until the cause is found.}}
<p>Protective earth is a separate idea from the fuse. The metal case is connected to earth. If a live wire ever touches the case, the current runs down the earth wire, the fuse blows, and the case never becomes dangerous to touch. Now consider a broken earth connection. The same fault makes the case live, and nothing trips. A person who touches it becomes the path to earth. This is why the earth path is tested on a schedule, and why Module 11 exists.[[iec60601]]</p>
<p>Much of this can be found before any meter is connected. Look first.</p>
<div class="table-wrap"><table>
<thead><tr><th>Visual check</th><th>Reject if</th></tr></thead>
<tbody>
<tr><td>Plug</td><td>Cracked, pins bent or loose, or signs of heat</td></tr>
<tr><td>Cord</td><td>Cut, crushed, taped, or stiff; strain relief pulled out</td></tr>
<tr><td>Inlet socket on the machine</td><td>Loose or discolored</td></tr>
<tr><td>Fuse holders</td><td>Wrong fuse fitted, or foil or wire bridging</td></tr>
<tr><td>Inside the cabinet</td><td>Water marks, corrosion, or a burnt smell</td></tr>
</tbody></table></div>
"""),
        ("parts", "Sensors and actuators", "The sensors and actuators in a dialysis machine", """
<p>Every loop in the machine begins with a sensor and ends with an actuator. Learn each one by asking three questions: what does it measure or do, how does it work, and how does it fail. The way it works usually tells you the way it fails.</p>
<div class="table-wrap"><table>
<thead><tr><th>Sensor</th><th>Measures</th><th>How it works, briefly</th><th>How it fails</th></tr></thead>
<tbody>
<tr><td>Temperature sensor</td><td>Dialysate temperature</td><td>Its electrical resistance changes with temperature</td><td>Drift; a scale coating slows its response</td></tr>
<tr><td>Conductivity cell</td><td>Dialysate conductivity</td><td>Passes a small current between electrodes in the fluid</td><td>Scale or air bubbles on the electrodes; drift</td></tr>
<tr><td>Pressure transducer</td><td>Blood-side and dialysate-side pressures</td><td>A thin diaphragm flexes and changes an electrical signal</td><td>Drift; a wet or blocked protector; diaphragm damage</td></tr>
<tr><td>Air detector</td><td>Air in the return line</td><td>Ultrasound passes well through liquid and poorly through air</td><td>Dirt, misalignment, or the wrong tubing</td></tr>
<tr><td>Blood leak detector</td><td>Blood in used dialysate</td><td>Blood absorbs light passed through the fluid</td><td>A dirty window; bubbles</td></tr>
<tr><td>Flow and level sensors</td><td>Dialysate flow; chamber levels</td><td>Various: turbines, floats, optical</td><td>Sticking; scale</td></tr>
<tr><td>Position switches</td><td>Doors, covers, pump rotor</td><td>Magnetic or mechanical</td><td>Misalignment; deliberate bypass</td></tr>
</tbody></table></div>
<div class="table-wrap"><table>
<thead><tr><th>Actuator</th><th>Does</th><th>How it fails</th></tr></thead>
<tbody>
<tr><td>Solenoid valves</td><td>Open and close fluid paths, including bypass</td><td>Stick open or closed with scale; the coil burns out; the seal leaks</td></tr>
<tr><td>Gear and piston pumps</td><td>Move dialysate, concentrates, and ultrafiltrate</td><td>Wear lowers delivery; seals leak; air locks</td></tr>
<tr><td>Blood pump motor</td><td>Turns the rollers at a set speed</td><td>Speed error; worn rollers or springs</td></tr>
<tr><td>Heater</td><td>Warms incoming water</td><td>Scale; an open element; a failed thermal cut-out</td></tr>
<tr><td>Venous clamp</td><td>Closes the return line on alarm</td><td>A weak spring or solenoid; does not fully occlude</td></tr>
<tr><td>Syringe (heparin) pump</td><td>Pushes a syringe at a set rate</td><td>Wrong syringe size setting; drive slip</td></tr>
</tbody></table></div>
{{key:Most machines have two sensors for each safety-critical quantity: one to control and one to protect. When you calibrate, verify both.}}
"""),
        ("meter", "Multimeter", "Using a multimeter safely", """
<p>A multimeter answers one question at a time. Your work is to ask the right question, on a circuit in the right state, with a meter you know is working.</p>
{{flow:Every measurement|Decide::What you expect to read, and whether the circuit should be live.|Select::Function and range, before you connect the probes.|Check the meter::Test it on a known source first.|Connect::One hand where possible; probes with insulated tips.|Read and compare::Against what you expected.|Remove::Probes first, then change the function.}}
<div class="table-wrap"><table>
<thead><tr><th>Function</th><th>Circuit state</th><th>Typical use</th></tr></thead>
<tbody>
<tr><td>AC voltage</td><td>Live</td><td>Is mains reaching the power supply or the heater?</td></tr>
<tr><td>DC voltage</td><td>Live</td><td>Are the power supply outputs correct at the test points in the manual?</td></tr>
<tr><td>Continuity (beeper)</td><td>Power off and unplugged</td><td>Is a fuse, wire, or switch unbroken?</td></tr>
<tr><td>Resistance</td><td>Power off and unplugged</td><td>A heater element, valve coil, or sensor, against the manual&rsquo;s value</td></tr>
</tbody></table></div>
{{stop:Resistance and continuity are measured only with the machine unplugged. Live measurements are made only when the manual calls for them, by someone trained to work on live equipment.}}
<p>Circuit boards are damaged by static electricity that you cannot feel. Wear a grounded wrist strap, work on an antistatic mat, hold boards by their edges, and carry them in antistatic bags. Boards are usually replaced as whole units, not repaired on site. Many are tied to a software version, so check the manual before you swap one, and record the board&rsquo;s serial number and software version in the service record.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What was the fuse telling you?</strong> That the heater circuit drew more current than the design allows, during heat disinfection, when the heater works hardest. The likely causes are a heater element breaking down, scale forcing the element to run hot, or moisture making a path to earth.</p>
<p><strong>What is the danger of a higher-rated fuse?</strong> It lets the excess current keep flowing. The wiring and connectors then overheat, and that is the smell of hot plastic Mr. Cruz noticed. The next step is a fire or a live case.</p>
<p><strong>What should have been done?</strong> Take the machine out of service after the second blown fuse. Fit only the specified fuse. Measure the heater element&rsquo;s resistance and its insulation to earth by the manual, and look for water. Repair, run an electrical safety test, and record it all. Machine 8, still carrying the wrong fuse, comes out of service now. Mr. Cruz should also talk with Mr. Aquino calmly, so that the reason for the rule stays with him.</p>
"""],
    "skills": {"title": "Multimeter basics on a de-energized training board",
        "intro": "Materials: a multimeter with a valid calibration label, a training board or an unplugged out-of-service machine, the service manual, a wrist strap, and an antistatic mat.",
        "items": [("Confirms the equipment is unplugged and locked out before resistance or continuity checks.", True),
                  ("Selects function and range before connecting the probes.", True),
                  ("Tests the meter on a known source.", False),
                  ("Checks a fuse for continuity and confirms its rating against the manual.", True),
                  ("Measures a heater element or valve coil resistance and compares with the manual.", False),
                  ("Inspects the plug, cord, and inlet and states what would reject each.", False),
                  ("Uses a wrist strap and handles a circuit board by its edges.", False),
                  ("Identifies five sensors and five actuators on the machine using the flow diagram.", False)],
        "placement": "With a senior technician, find the control sensor and the protective sensor for temperature and for conductivity on one machine model."},
    "quiz": [
        ("In the water picture of electricity, what is voltage most like?",
         ["The flow of water", "The water pressure", "The narrowness of the pipe", "The temperature"], 1,
         "Voltage is the push; current is the flow; resistance is the restriction."),
        ("A heater element of 23 ohms is connected to 230 volts. About how much current flows?",
         ["0.1 ampere", "10 amperes", "23 amperes", "230 amperes"], 1, "Current = voltage &divide; resistance = 230 &divide; 23 = 10 amperes."),
        ("A fuse blows a second time after replacement. What is correct?",
         ["Fit a higher-rated fuse", "Take the machine out of service and find the fault", "Wrap the fuse in foil", "Ignore it"], 1,
         "A repeated blown fuse signals a real fault; a larger fuse removes the protection."),
        ("What does the protective earth connection do?",
         ["Powers the display", "Carries fault current safely away so the case does not become live", "Measures conductivity", "Cools the heater"], 1,
         "It makes a fault blow the fuse instead of energizing the case."),
        ("Which measurement must only be made with the machine unplugged?",
         ["AC voltage", "DC voltage", "Resistance", "None"], 2, "Resistance and continuity are measured on dead circuits."),
        ("A sensor reading is jumping and a connector feels warm. What kind of fault is likely?",
         ["Open circuit", "High-resistance joint", "Software version", "Low water pressure"], 1,
         "Loose or corroded connections cause heat and intermittent readings."),
        ("Why do machines have two sensors for safety-critical quantities?",
         ["For decoration", "One controls and an independent one protects", "To use more power", "One is a spare kept switched off"], 1,
         "Independence means one failed sensor cannot both cause and hide a hazard."),
        ("How should a circuit board be handled?",
         ["By the components", "By its edges, with a grounded wrist strap", "With wet hands", "On a carpet"], 1,
         "Static discharge can damage components invisibly."),
    ],
    "terms": [("Ampere", "The unit of electrical current."), ("Ohm", "The unit of electrical resistance."),
              ("Solenoid", "A coil that moves a plunger when powered; used in valves and clamps."),
              ("Thermal cut-out", "A switch that opens if a heater gets too hot."),
              ("Rating plate", "The label on a machine giving model, serial number, and electrical ratings.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How equipment faults are tracked in the quality program.")],
}

NEW["03"] = {
    "image_alt": "A technician holding a reference thermometer probe at a dialysate sample point.",
    "objectives": [
        "Trace water from the inlet through pressure regulation, heat exchange, heating, and degassing.",
        "Explain how temperature is controlled and independently protected.",
        "Verify dialysate temperature against a reference instrument.",
        "Troubleshoot inlet, heating, and degassing faults.",
    ],
    "big": """
{{plain:Think of preparing water for a baby&rsquo;s bath. You open the tap to a steady flow, warm the water to body temperature, and let it settle before the baby goes in. Before the machine can mix dialysate, it does the same: it steadies the water pressure, warms the water to body temperature, and pulls out the dissolved air. These steps are unglamorous, and they cause a large share of everyday alarms. A machine that warms slowly, or that shows bubbles in its lines, is telling you about scale, a weak pump, or the water supply.}}
<p>The picture has a limit. At a bath, you test the water with your elbow and adjust as you go. The machine cannot feel. It trusts a temperature sensor, and it needs a second, independent sensor to catch the first one when it drifts. Your reference thermometer is the elbow the machine does not have.</p>
{{flow:Water preparation inside the machine|Inlet::Treated water enters through a filter and a pressure regulator.|Heat exchanger::Outgoing used dialysate gives its warmth to the incoming water.|Heater::Raises the water to the set temperature.|Degassing::A pump lowers the pressure so that dissolved air comes out and is vented.|Ready for mixing::Warm, bubble-free water goes on to the concentrate pumps.}}
{{cards:Key terms for this module|Pressure regulator::A valve that keeps inlet pressure steady.|Heat exchanger::A device that passes heat from outgoing fluid to incoming water without mixing them.|Degassing::Removing dissolved air.|Control sensor::The sensor the machine uses to regulate.|Protective sensor::An independent sensor that triggers an alarm and a safe state.|Reference thermometer::A calibrated thermometer used to check the machine.}}
""",
    "case": {"title": "Slow to warm on cold mornings", "html": """
<p>It is a cool week in January. At the five-thirty start, machine 4 takes twenty minutes longer than its neighbors to pass its start-up checks. Twice this week it has alarmed for low temperature in the first hour of treatment. The charge nurse, Ms. Teresita Ramos, asks the biomedical technician, Mr. Noel Mendoza, to look at it.</p>
<p>Mr. Mendoza pulls the records. Machine 4 was last descaled three months ago. The other machines are descaled monthly. The water room also reports that the feed water is several degrees colder than last month.</p>
""", "questions": ["Name two things that would make this machine slower to warm than its neighbors.",
                  "Which do you check first, and how?",
                  "What do you verify before returning it to use?"]},
    "sections": [
        ("inlet", "Water inlet", "The water inlet", """
<p>The machine expects water within a stated pressure and temperature range. You will find the figures in the instructions for use. Outside that range, the machine alarms or cannot keep up.</p>
<div class="table-wrap"><table>
<thead><tr><th>Part</th><th>Job</th><th>What goes wrong</th></tr></thead>
<tbody>
<tr><td>Inlet hose and connector</td><td>Brings water from the wall outlet</td><td>Kinks; biofilm in old hoses; leaks at the connector</td></tr>
<tr><td>Inlet filter or strainer</td><td>Stops particles</td><td>Plugs gradually; low-water alarms at peak demand</td></tr>
<tr><td>Inlet valve</td><td>Admits water when the machine calls for it</td><td>Sticks; leaks through when closed</td></tr>
<tr><td>Pressure regulator</td><td>Holds a steady pressure for the hydraulics</td><td>Drifts; the diaphragm wears; unstable flow downstream</td></tr>
<tr><td>Heat exchanger</td><td>Pre-warms incoming water with heat from used dialysate</td><td>Scale lowers efficiency; an internal leak would cross-connect fresh and used fluid</td></tr>
</tbody></table></div>
<p>When several machines alarm for low water at the same moment, the cause is in the supply they share. When only one does, look at its own hose, filter, and regulator. That one question, one machine or several, saves hours.</p>
"""),
        ("L", "02", "prep"),
        ("verify", "Verifying temperature", "Verifying dialysate temperature", """
<p>The machine&rsquo;s display shows what its own sensor believes. Verification asks a calibrated instrument the same question, under conditions where the answer can be trusted.</p>
{{flow:A temperature verification|Reference::A calibrated thermometer with a valid certificate.|Steady state::The machine in dialysis mode, with stable flow and temperature.|Sample point::As the manual specifies, usually at the dialyzer connectors with a test adapter.|Wait::Until the reference reading stops changing.|Compare::The reference against the display, at one or more set temperatures as the manual states.|Decide::Within tolerance, record. Outside, adjust by the manual, then repeat.}}
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>Likely meaning</th></tr></thead>
<tbody>
<tr><td>Display and reference agree</td><td>The control sensor is accurate</td></tr>
<tr><td>Display reads higher than the reference</td><td>Dialysate is cooler than shown; patients may feel cold</td></tr>
<tr><td>Display reads lower than the reference</td><td>Dialysate is warmer than shown; check the protective sensor urgently</td></tr>
<tr><td>Control and protective sensors disagree with each other</td><td>One has drifted; the machine may alarm intermittently</td></tr>
<tr><td>Reading swings up and down</td><td>Unstable flow, air, or failing heater control</td></tr>
</tbody></table></div>
<p>Notice which direction is dangerous. A display that reads low hides dialysate that is too warm, and warm dialysate damages red blood cells. Next, prove the protection: by the manual&rsquo;s method, show that a temperature beyond the limit produces an alarm and bypass. Typical set temperatures are around 35 to 37 degrees Celsius, and the standard requires protection before dialysate exceeds about 41 degrees Celsius.[[iec60601_2_16]]</p>
"""),
        ("trouble", "Troubleshooting", "Troubleshooting inlet, heating, and degassing", """
<p>Work from the simple and the shared toward the specific and the expensive. Most of the &ldquo;check first&rdquo; column below needs no tools.</p>
<div class="table-wrap"><table>
<thead><tr><th>Symptom</th><th>Check first</th><th>Then</th></tr></thead>
<tbody>
<tr><td>Low water or inlet pressure alarm</td><td>Is it one machine or several? Is the hose kinked? Is the wall outlet fully open?</td><td>Inlet filter, inlet valve, pressure regulator</td></tr>
<tr><td>Slow to reach temperature</td><td>Inlet water temperature; descaling history</td><td>Heater resistance, heat exchanger scale, power to the heater</td></tr>
<tr><td>Low temperature alarms during treatment</td><td>Same as above; the dialysate flow setting</td><td>Sensor verification</td></tr>
<tr><td>High temperature alarm</td><td>Is flow reduced or stopped? A heater with no flow overheats quickly</td><td>Heater control, sensors, thermal cut-out</td></tr>
<tr><td>Patients feel cold, display normal</td><td>Verify with a reference thermometer</td><td>Sensor calibration</td></tr>
<tr><td>Bubbles in the dialysate lines; unstable conductivity</td><td>Inlet connections drawing air; water unusually cold</td><td>Degassing pump pressure, restrictor, vent</td></tr>
<tr><td>Fluid balance errors with bubbles present</td><td>Degassing</td><td>Fluid balance test after repair</td></tr>
</tbody></table></div>
{{key:Scale is the common thread. It insulates heaters, coats sensors, blocks restrictors, and jams valves. Before you replace any part on a machine with repeated heating or degassing trouble, check its descaling history.}}
"""),
    ],
    "debrief": ["""
<p><strong>Two things that would make it slower to warm.</strong> Three months without descaling, so its heater and heat exchanger are probably coated with scale. And colder feed water, which exposes that weakness: a clean heater copes, a scaled one falls behind.</p>
<p><strong>What to check first, and how.</strong> Start with the simple things. Confirm the descaling record, run a descale by the manual, and inspect the inlet filter. Then measure the heater by the manual, and verify temperature against a reference thermometer.</p>
<p><strong>What to verify before it returns to use.</strong> Record the as-found and as-left temperatures. Prove the high-temperature alarm. Run disinfection and confirm a negative residual test. Put the machine back on the monthly descaling schedule, and find out why it dropped off the schedule in the first place. Then tell Ms. Ramos what you found and what was done.</p>
"""],
    "skills": {"title": "Temperature verification against a reference thermometer",
        "intro": "Materials: an out-of-service machine, its service manual, a calibrated reference thermometer with test adapter, and a service record.",
        "items": [("Checks the reference thermometer&rsquo;s identity and calibration due date.", True),
                  ("Brings the machine to steady dialysis conditions.", False),
                  ("Measures at the point the manual specifies and waits for a stable reading.", False),
                  ("Records as-found display and reference values.", True),
                  ("States the tolerance and decides correctly whether adjustment is needed.", True),
                  ("Demonstrates the high-temperature alarm and bypass by the manual&rsquo;s method.", True),
                  ("Inspects the inlet hose, filter, and connections.", False),
                  ("Records the result with the instrument&rsquo;s identity.", False)],
        "placement": "Compare the descaling records of all machines in the unit and list any that are off schedule."},
    "quiz_keep": [("02", [0, 7])],
    "quiz": [
        ("What does the heat exchanger do?",
         ["Cools the patient", "Uses warmth from used dialysate to pre-warm incoming water", "Mixes concentrates", "Removes air"], 1,
         "It recovers heat without mixing the two fluids."),
        ("Six machines alarm for low water at shift start. Where is the cause most likely?",
         ["Six inlet filters", "The water supply", "Six heaters", "The blood pumps"], 1, "Simultaneous alarms point to something shared."),
        ("The display reads lower than a reference thermometer. Why is this the more worrying direction?",
         ["Patients feel cold", "Dialysate is warmer than shown", "The heater is off", "It is not worrying"], 1,
         "A machine under-reading temperature may deliver dialysate that is too hot."),
        ("A heater has power but water is not flowing past it. What happens?",
         ["Nothing", "It overheats quickly", "It cools down", "Conductivity rises"], 1,
         "Heaters depend on flow to carry heat away; protection must cut power."),
        ("One machine warms slowly while its neighbors are normal. What do you check before replacing parts?",
         ["The paint", "Its descaling history and inlet filter", "The blood pump", "The software clock"], 1,
         "Scale and restricted inlet flow are the common causes."),
        ("Bubbles in the dialysate lines and unstable conductivity suggest a problem with which stage?",
         ["Blood leak detection", "Degassing", "The venous clamp", "The power cord"], 1,
         "Poor degassing lets air reach the sensors and the balancing system."),
    ],
    "terms": [("Strainer", "A coarse filter at the water inlet."), ("Restrictor", "A narrow passage used to create low pressure for degassing."),
              ("Steady state", "The condition when readings have stopped changing.")],
    "readings": [("dialysis-water-treatment-systems.html", "The water your machines receive, including pressure and temperature."),
                 ("dialysis-prescription.html", "Why dialysate temperature is prescribed.")],
}

NEW["04"] = {
    "image_alt": "A technician holding a reference conductivity meter probe in a dialysate sample.",
    "objectives": [
        "Explain how the machine proportions water and two concentrates, and why the concentrate system must match.",
        "Explain how conductivity is measured, temperature-compensated, and independently protected.",
        "Verify conductivity against a reference meter and prove bypass.",
        "Troubleshoot conductivity alarms, starting from shared and simple causes.",
    ],
    "big": """
{{plain:Think of the pharmacist at the corner botika who mixes a child&rsquo;s syrup from a powder. She adds water to the line on the bottle, shakes it, and checks the label before handing it over. At the mixing stage, the machine is that pharmacist. It combines water with an acid concentrate and a bicarbonate concentrate in exact proportion, then checks its own work by measuring how well the mixture conducts electricity. If the check fails, it sends the fluid to the drain instead of to the patient. Your work is to make sure that check is true.}}
<p>The picture has a limit. The pharmacist reads the label and knows which medicine is in the bottle. The machine cannot read labels. Its check sees only the total amount of dissolved salt, so it trusts that the right concentrates were connected and that it was configured for them.</p>
{{cards:Key terms for this module|Proportioning::Mixing water and concentrates in a fixed ratio.|Concentrate system::The particular ratio a machine is configured for.|Conductivity cell::The sensor that measures conductivity.|Temperature compensation::Correcting a conductivity reading to a standard temperature.|Bypass::Diverting dialysate to the drain when it is not safe.|Reference meter::A calibrated conductivity meter used to check the machine.}}
""",
    "case": {"title": "A machine from the other unit", "html": """
<p>On a Thursday, one of the unit&rsquo;s machines breaks down. To cover the gap, a machine is borrowed from the network&rsquo;s other center. It is the same model, but that center uses a different brand of concentrate.</p>
<p>On its first treatment, at eight in the morning, the conductivity will not stabilize, and the machine goes in and out of bypass. The nurse, Ms. Angelica Torres, finds the biomedical technician, Mr. Rodel Castillo, and asks him to &ldquo;adjust the conductivity so it stops alarming.&rdquo;</p>
""", "questions": ["What is the most likely explanation?",
                  "Why is adjusting the conductivity the wrong response?",
                  "What should be checked on any machine that moves between sites?"]},
    "sections": [("L", "02", "mix"),
        ("cells", "Measuring conductivity", "How conductivity is measured and compensated", """
<p>A conductivity cell passes a small alternating current between electrodes in the fluid. The more dissolved ions there are, the more easily current flows. Two things besides the salt content also change the reading, and both matter to you.</p>
<div class="table-wrap"><table>
<thead><tr><th>Influence</th><th>Effect</th><th>Consequence for your work</th></tr></thead>
<tbody>
<tr><td>Temperature</td><td>Conductivity rises by roughly 2 percent for each degree Celsius</td><td>Machines and meters correct the reading to a standard temperature. The machine and your reference meter must use the same reference temperature, or they will disagree while both are right</td></tr>
<tr><td>Deposits and air on the electrodes</td><td>Scale or bubbles reduce the contact area and lower the reading</td><td>A scaled cell makes the machine add more concentrate than intended</td></tr>
</tbody></table></div>
<p>Why does temperature matter so much? Warm ions move faster through water, so the same fluid carries current more easily when it is warm. The worked example shows how large that effect is.</p>
{{formula:<strong>Illustration.</strong> A dialysate reading 14.0 mS/cm at 25 &deg;C will read about 14.0 &times; (1 + 0.02 &times; 12) = 17.4 mS/cm at 37 &deg;C if no correction is applied. A disagreement of this size between two instruments nearly always means they are using different reference temperatures.}}
<p>Machines have at least two cells in the final dialysate: one that controls or monitors the mix, and an independent one that protects. Some machines also measure after the first concentrate is added, to check each stage. The flow diagram shows where each cell sits.</p>
"""),
        ("L", "02", "bypass"),
        ("verify", "Verifying conductivity", "Verifying conductivity with a reference meter", """
<p>A verification is only as good as the reference you compare against. Before you trust your meter to judge the machine, prove the meter itself.</p>
{{flow:A conductivity verification|Reference::A calibrated meter, checked that day against standard solution.|Match settings::The same reference temperature and units as the machine.|Steady state::Correct concentrates connected; the machine stable in dialysis mode.|Sample::From the point, and by the method, that the manual specifies; rinse the probe or cell with sample first.|Compare::The reference against the display, for each cell the manual lists.|Decide::Within tolerance, record. Outside, clean or descale, then calibrate by the manual and repeat.}}
<div class="table-wrap"><table>
<thead><tr><th>Common error</th><th>Result</th></tr></thead>
<tbody>
<tr><td>Meter not checked against standard solution</td><td>You may adjust a correct machine to match a wrong meter</td></tr>
<tr><td>Different reference temperatures</td><td>A false disagreement of several percent</td></tr>
<tr><td>Sample allowed to cool or sit</td><td>The reading drifts; bicarbonate dialysate loses carbon dioxide</td></tr>
<tr><td>Probe not rinsed with sample</td><td>Carry-over from the last measurement</td></tr>
<tr><td>Measuring before the machine is stable</td><td>Meaningless numbers</td></tr>
<tr><td>Wrong concentrate connected for the test</td><td>The machine appears out of calibration when it is not</td></tr>
</tbody></table></div>
<p>Once the reading is verified, prove the protection. By the manual&rsquo;s method, create an out-of-limit condition and confirm the alarm and bypass. Record the as-found and as-left values and the meter&rsquo;s identity.</p>
{{stop:Never adjust conductivity calibration to silence an alarm. Calibration is changed only when a verified reference shows the sensor is wrong.}}
"""),
        ("trouble", "Troubleshooting", "Troubleshooting conductivity alarms", """
<p>Read the pattern before you touch the machine. Who is affected, when it started, and which way the reading is off usually point to the cause.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pattern</th><th>Likely cause</th><th>First checks</th></tr></thead>
<tbody>
<tr><td>Several machines at once</td><td>Shared concentrate supply or water</td><td>Central tank level, batch, valve; water alarms</td></tr>
<tr><td>One machine, just after a container change</td><td>Pick-up tube out of the fluid, wrong product, or air drawn in</td><td>Container, label, pick-up tube and filter</td></tr>
<tr><td>One machine, low and unstable</td><td>Air: poor degassing or a loose concentrate connector</td><td>Bubbles in the lines; connectors; degassing</td></tr>
<tr><td>One machine, steadily off in one direction</td><td>Concentrate pump wear, a scaled cell, or the wrong concentrate system configured</td><td>Verify with a reference; pump delivery test; configuration</td></tr>
<tr><td>Bicarbonate-stage conductivity low, final normal or high</td><td>Bicarbonate supply weak or cartridge exhausted</td><td>Cartridge or batch; bicarbonate pump</td></tr>
<tr><td>Alarm appears after the machine was moved</td><td>Configuration does not match the concentrates at the new site</td><td>Configured concentrate system against the labels</td></tr>
<tr><td>Drifts over weeks, then alarms</td><td>Scale building on cells and in pumps</td><td>Descaling history</td></tr>
</tbody></table></div>
"""),
    ],
    "debrief": ["""
<p><strong>What is the most likely explanation?</strong> The machine is configured for the concentrate system used at the other center. With this center&rsquo;s concentrates, the fixed proportions produce a mixture the machine does not expect, so conductivity will not settle.</p>
<p><strong>Why is adjusting the conductivity wrong?</strong> Adjusting the calibration to stop the alarm would teach the machine to accept dialysate of the wrong composition. That is exactly what the alarm exists to prevent. Mr. Castillo should explain this to Ms. Torres plainly. The machine comes off the floor, and the nurse arranges another machine for the patient. Mr. Castillo then checks the configured concentrate system against the labels in use here. He reconfigures it by the manual only if that is permitted and he is trained to do it. Then he verifies conductivity with a reference meter, proves bypass, disinfects, and records.</p>
<p><strong>What to check on any machine that moves between sites.</strong> The concentrate configuration, the hepatitis isolation status, the software version, the maintenance status, and that the machine is entered in the receiving unit&rsquo;s inventory.</p>
"""],
    "skills": {"title": "Conductivity verification and bypass proof",
        "intro": "Materials: an out-of-service machine with the unit&rsquo;s concentrates, its service manual, a reference conductivity meter, standard solution, and a service record.",
        "items": [("Checks the reference meter&rsquo;s calibration date and verifies it against standard solution.", True),
                  ("Confirms the meter and the machine use the same reference temperature and units.", True),
                  ("Confirms the machine&rsquo;s configured concentrate system matches the concentrates connected.", True),
                  ("Samples by the manual&rsquo;s method at steady state.", False),
                  ("Records as-found readings for each conductivity cell.", False),
                  ("States the tolerance and decides correctly whether calibration is needed.", True),
                  ("Demonstrates alarm and bypass for an out-of-limit condition by the manual&rsquo;s method.", True),
                  ("Records as-left readings with the meter&rsquo;s identity.", False)],
        "placement": "List the concentrate system each machine in the unit is configured for and compare with the concentrates in the store."},
    "quiz_keep": [("02", [1, 2, 5, 6])],
    "quiz": [
        ("By roughly how much does conductivity change per degree Celsius?",
         ["0.02 percent", "2 percent", "20 percent", "It does not change"], 1, "About 2 percent per degree, which is why readings are temperature-compensated."),
        ("Your reference meter and the machine disagree by several percent, and both pass their own checks. What should you suspect first?",
         ["A failed cell", "Different reference temperatures", "A blood leak", "Low water pressure"], 1,
         "Mismatched temperature compensation gives a false disagreement."),
        ("A nurse asks you to adjust conductivity so an alarm stops. What is correct?",
         ["Adjust it", "Decline; find the cause and calibrate only if a verified reference shows the sensor is wrong", "Widen the alarm limits", "Disable bypass"], 1,
         "Calibration is not an alarm-silencing tool."),
        ("A machine borrowed from another center will not stabilize conductivity. What do you check?",
         ["Its paint", "Whether its configured concentrate system matches the concentrates in use", "Its casters", "The blood pump"], 1,
         "A mismatch between configuration and concentrate gives the wrong mixture."),
    ],
    "terms": [("Millisiemens per centimeter", "The unit of conductivity used for dialysate."),
              ("Reference temperature", "The temperature to which a conductivity reading is corrected, often 25 &deg;C."),
              ("Pick-up tube", "The tube that draws concentrate from its container.")],
    "readings": [("dialysis-prescription.html", "What dialysate composition means for the patient."),
                 ("dialysis-water-treatment-systems.html", "Concentrates and fluid quality.")],
}

NEW["05"] = {
    "image_alt": "A technician reading the level in a measuring cylinder beside a dialysis machine.",
    "objectives": [
        "Explain how balancing systems keep dialysate in and out equal, and how ultrafiltration is measured.",
        "Explain transmembrane pressure and what changes it.",
        "Outline the fluid balance test and the ultrafiltration accuracy check.",
        "Recognize silent fluid errors from clinical and technical clues.",
    ],
    "big": """
{{plain:Think of a gasoline pump at a station that gives a little less than the meter shows. No buzzer sounds. Each customer loses only a little, every time, and nobody notices until someone fills a measured can. Of everything a dialysis machine does, fluid removal is the function where a small, steady error does the most harm with the least warning. A machine that removes 5 percent too little leaves every patient slightly overloaded. One that removes too much drops blood pressures. Neither one necessarily alarms.}}
<p>The picture has a limit. A short-changed motorist loses money. A patient on a machine that over-removes or under-removes loses fluid balance, at every session, on a heart and blood vessels that are already strained. The machine&rsquo;s accuracy here rests on a closed loop that must be free of leaks and air, and on one pump that must deliver exactly what it reports. Your measured can is the measuring cylinder.</p>
{{cards:Key terms for this module|Balancing system::The part that makes dialysate in equal dialysate out.|Ultrafiltration pump::The pump that removes the extra volume, which comes from the patient.|Closed loop::A circuit that cannot gain or lose fluid except through the ultrafiltration pump.|Transmembrane pressure::The pressure difference across the dialyzer membrane.|Ultrafiltration coefficient::How much water a dialyzer lets through for each unit of pressure.|Volumetric check::Measuring a pump&rsquo;s output by collecting it.}}
""",
    "case": ("L", "02"),
    "sections": [("L", "02", "balance"),
        ("designs", "Two designs", "Two ways machines control fluid balance", """
<p>Machines reach the same goal, dialysate in equal to dialysate out, in one of two ways. The difference matters to you, because each design fails quietly in its own way, and each has its own tests.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Balancing chambers</th><th>Flow sensors</th></tr></thead>
<tbody>
<tr><td>Principle</td><td>Chambers of fixed volume, each divided by a flexible membrane, force equal volumes in and out</td><td>Sensors measure the flow going to the dialyzer and the flow coming back; the difference is the fluid removed</td></tr>
<tr><td>Ultrafiltration</td><td>A separate pump removes a measured volume from the closed loop</td><td>The return pump is controlled so that the measured difference matches the target</td></tr>
<tr><td>Accuracy depends on</td><td>Tight valves, no air, and an accurate ultrafiltration pump</td><td>Matched, clean, calibrated sensors</td></tr>
<tr><td>Typical quiet failure</td><td>A valve that leaks slightly; air in a chamber</td><td>One sensor drifting or coated</td></tr>
</tbody></table></div>
<p>Know which design each of your models uses. Both designs are disturbed by air, which is why degassing (Module 3) matters here. Both are also disturbed by leaks at the dialyzer connectors, which sit outside the machine but inside the loop.</p>
"""),
        ("tmp", "Transmembrane pressure", "Transmembrane pressure", """
<p>Water crosses the dialyzer membrane for the same reason water seeps through a cloth when you squeeze it: pressure is higher on one side than the other. In the dialyzer, pressure is higher on the blood side than on the dialysate side. That difference is the transmembrane pressure (TMP).</p>
{{formula:<strong>Transmembrane pressure = blood-side pressure &minus; dialysate-side pressure</strong><br><strong>Fluid removed per hour = ultrafiltration coefficient &times; transmembrane pressure</strong> (a simplified relationship)}}
<p>On a volumetric machine, the operator sets the volume to remove, and the machine produces whatever TMP is needed to remove it. So TMP is a result, not a setting, and a result carries information.</p>
<div class="table-wrap"><table>
<thead><tr><th>Observation</th><th>Possible meaning</th></tr></thead>
<tbody>
<tr><td>TMP rising steadily during a treatment</td><td>Fibers are clotting, so less membrane is available</td></tr>
<tr><td>TMP high from the start</td><td>A high fluid removal rate with a low-permeability dialyzer; a kinked dialysate line</td></tr>
<tr><td>TMP near zero or negative with a high-permeability dialyzer</td><td>Can be normal at low removal rates; fluid moves both ways within the dialyzer</td></tr>
<tr><td>TMP alarm on several different patients on one machine</td><td>A dialysate-side pressure sensor, or a restriction on the machine side</td></tr>
</tbody></table></div>
{{fig:dialyzer_anatomy|Water leaves the blood through the fiber walls under pressure. Clotted fibers reduce the working membrane area, and the machine must raise the pressure to remove the same volume.}}
"""),
        ("tests", "The tests", "The fluid balance test and the ultrafiltration check", """
<p>The exact method is in each service manual. The principles are the same everywhere: first prove that the loop is tight, then measure what the pump really delivers.</p>
{{flow:Fluid balance (tightness) test|Close the loop::A test connector replaces the dialyzer.|Zero ultrafiltration::The ultrafiltration pump is off.|Pressurize::The loop is held at a set pressure.|Watch::The pressure should hold; fluid should neither appear nor disappear.|Interpret::A falling pressure or a changing level means a leak or air.}}
{{flow:Ultrafiltration accuracy check|Set::A known ultrafiltration rate for a known time.|Collect::The pump&rsquo;s output, in a measuring cylinder or on a calibrated scale.|Compare::The collected volume with the volume the machine reports.|Decide::Within the manual&rsquo;s tolerance, record. Outside, calibrate or repair, then repeat.}}
{{formula:<strong>Illustration.</strong> The machine is set to remove 1,000 mL in one hour. You collect 960 mL. The error is (960 &minus; 1,000) &divide; 1,000 = &minus;4 percent: the machine removes less than it reports. Compare this with the tolerance in the manual.}}
<div class="table-wrap"><table>
<thead><tr><th>Good practice</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Use a cylinder or scale of known accuracy</td><td>Your measuring device must be better than the tolerance you are checking</td></tr>
<tr><td>Read the cylinder at eye level, at the bottom of the curve</td><td>Avoids reading error</td></tr>
<tr><td>Run long enough</td><td>Short tests magnify small errors</td></tr>
<tr><td>Remove all air first</td><td>Air gives false results in both directions</td></tr>
<tr><td>Do the tightness test before the accuracy check</td><td>A leaking loop makes pump calibration meaningless</td></tr>
</tbody></table></div>
"""),
        ("clues", "Silent errors", "Finding silent errors", """
<p>A silent error gives no alarm, but it still leaves traces. Most of them are found by other people first, which is why you ask.</p>
<div class="table-wrap"><table>
<thead><tr><th>Clue</th><th>Where it comes from</th><th>What it suggests</th></tr></thead>
<tbody>
<tr><td>Patients on one machine regularly finish above or below the expected weight</td><td>Nurses&rsquo; records</td><td>An ultrafiltration pump or balance error on that machine</td></tr>
<tr><td>More low blood pressure episodes on one machine</td><td>Nurses&rsquo; observations</td><td>Over-removal</td></tr>
<tr><td>Fluid on the floor or in the drip tray</td><td>Inspection</td><td>A leak; find out whether it is inside the balanced loop</td></tr>
<tr><td>Wet dialyzer connectors</td><td>Operators</td><td>Worn seals on the connectors; air drawn in or fluid lost</td></tr>
<tr><td>Bubbles in the dialysate lines</td><td>Inspection</td><td>A degassing fault; balance will be affected</td></tr>
<tr><td>The machine&rsquo;s own pressure-holding test fails intermittently</td><td>Start-up test log</td><td>A marginal valve or seal</td></tr>
</tbody></table></div>
{{key:Patient weights before and after treatment are an independent check on every machine, every day. Ask the nurses to tell you about any machine that seems to behave differently.}}
"""),
    ],
    "debrief": ("L", "02"),
    "skills": {"title": "Ultrafiltration accuracy check with a measuring cylinder",
        "intro": "Materials: an out-of-service machine, its service manual, the test connector, a measuring cylinder or calibrated scale, a timer, and a service record.",
        "items": [("States which fluid balance design the machine uses.", False),
                  ("Removes air from the loop before testing.", False),
                  ("Performs the tightness test by the manual and interprets the result.", True),
                  ("Sets the ultrafiltration rate and time the manual specifies.", False),
                  ("Collects and reads the volume correctly at eye level.", True),
                  ("Calculates the percent error and compares it with the tolerance.", True),
                  ("Calibrates or reports for repair if outside tolerance, then repeats the check.", False),
                  ("Records as-found and as-left values and the measuring device used.", False),
                  ("Inspects and replaces worn dialyzer connector seals.", False)],
        "placement": "Ask the charge nurse whether any machine is suspected of over- or under-removing fluid, and review that machine&rsquo;s test history."},
    "quiz_keep": [("02", [3, 4])],
    "quiz": [
        ("A machine is set to remove 2,000 mL and you collect 2,100 mL in the test. What is the error?",
         ["&minus;5 percent", "+5 percent", "+0.5 percent", "+50 percent"], 1, "(2,100 &minus; 2,000) &divide; 2,000 = +5 percent: it removes more than it reports."),
        ("Why is the tightness test done before the ultrafiltration accuracy check?",
         ["Tradition", "A leaking loop makes pump calibration meaningless", "It is faster", "It warms the machine"], 1,
         "Fluid entering or leaving through a leak would be mistaken for pump error."),
        ("Transmembrane pressure rises steadily through a treatment. What is a likely cause?",
         ["The heater is off", "Fibers are clotting", "The softener is exhausted", "The patient is cold"], 1,
         "Less open membrane means more pressure is needed for the same removal."),
        ("On a volumetric machine, what does the operator set?",
         ["The transmembrane pressure", "The volume to remove; the machine produces the pressure needed", "The conductivity cell constant", "The fuse rating"], 1,
         "Pressure is the result, not the setting."),
        ("Which is an independent daily check on every machine&rsquo;s fluid removal?",
         ["The self-test", "Patient weights before and after treatment", "The display brightness", "The alarm volume"], 1,
         "Weights reveal steady errors that produce no alarm."),
        ("Wet, worn seals on the dialyzer connectors can cause which problem?",
         ["High temperature", "Air drawn in or fluid lost from the balanced loop", "Blown fuses", "Blood pump speed error"], 1,
         "The connectors are part of the closed loop."),
    ],
    "terms": [("Meniscus", "The curved surface of a liquid in a cylinder; read at its lowest point."),
              ("Test connector", "A fitting that joins the two dialysate hoses in place of a dialyzer."),
              ("Backfiltration", "Movement of dialysate into the blood within part of a high-permeability dialyzer.")],
    "readings": [("dry-weight-determination.html", "Why accurate fluid removal matters clinically."),
                 ("high-flux-hd-optimization.html", "Fluid movement inside high-permeability dialyzers.")],
    "calcs": ["calc-ufr-ceiling.html"],
}

NEW["06"] = {
    "image_alt": "A technician fitting a training pump segment into an open roller blood pump.",
    "objectives": [
        "Explain how the roller pump moves blood, and what makes displayed flow differ from true flow.",
        "Interpret arterial, venous, and transmembrane pressures, and verify the sensors.",
        "Describe how the heparin syringe pump works and how its delivery is checked.",
        "Carry out blood-side checks at maintenance and troubleshoot common faults.",
    ],
    "big": """
{{plain:Think of a taxi meter. It does not measure the road. It counts the turns of the wheels and multiplies by the size of the tire. Put on a smaller tire, and the meter runs wrong while looking perfectly normal. The blood side of the machine works the same way. It looks simple: a pump, some tubing, and a few pressure readings. But the number the nurse trusts most, blood flow, is calculated, not measured, and it is only as true as the pump&rsquo;s adjustment and the tubing size it was told to use.}}
<p>The picture has a limit. A passenger can check a taxi fare against a map. Nobody at the chair can check blood flow by looking at it. The error shows up weeks later as a lower dialysis dose, if anyone thinks to compare machines. This module covers the pump, the pressures, and the small syringe pump that delivers blood thinner. Module 7 covers the safety systems.</p>
{{fig:blood_circuit|The blood circuit. This module follows the pump, the pressure monitoring points, and the heparin line.}}
{{cards:Key terms for this module|Roller pump::A pump whose rollers squeeze tubing to push blood forward.|Occlusion::How firmly the rollers squeeze the tubing.|Pump segment::The section of tubing inside the pump.|Arterial pressure::Pressure before the pump; normally negative.|Venous pressure::Pressure on the return side; normally positive.|Transducer protector::A filter that keeps blood out of the pressure sensor.|Syringe pump::A motor that pushes a syringe plunger at a set rate.}}
""",
    "case": {"title": "Adequacy falling on one machine", "html": """
<p>At the quarterly quality meeting, the attending nephrologist, Dr. Celia Navarro, raises a pattern she has followed for three months. Patients dialyzed on machine 5 have lower adequacy results than the same patients have on other machines. Their prescriptions, dialyzers, and treatment times are the same.</p>
<p>Machine 5 shows the prescribed blood flow on its screen at every session. The biomedical technician, Mr. Efren Dizon, checks the service log. Machine 5 had its blood pump rotor replaced four months ago.</p>
""", "questions": ["Why might true blood flow differ from the displayed value?",
                  "What do you check on machine 5?",
                  "What would you say to the nephrologist while you investigate?"]},
    "sections": [("L", "03", "pump"),
        ("pumpcheck", "Pump checks", "Checking the blood pump", """
<p>Each check below tests one input to the flow calculation, or one part that changes how much blood each turn of the rotor really moves.</p>
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>Method, in outline</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Tubing size configuration</td><td>Compare the setting with the pump segment actually used in the unit</td><td>Flow is calculated from speed and tubing size</td></tr>
<tr><td>Occlusion</td><td>By the manual: commonly a pressure-holding or fluid-column test with the rotor stationary</td><td>Too loose lowers real flow; too tight damages blood and tubing</td></tr>
<tr><td>Rotor speed</td><td>Count revolutions against a timer, or use service mode, at set speeds</td><td>Confirms that the motor does what the display says</td></tr>
<tr><td>Flow delivery</td><td>Where the manual provides it, collect the fluid pumped in a set time</td><td>The direct test of displayed against true flow</td></tr>
<tr><td>Rollers, springs, tubing guides</td><td>Inspect for wear, flat spots, and weak springs</td><td>Worn parts change occlusion</td></tr>
<tr><td>Cover switch</td><td>Open the cover with the pump running</td><td>The pump must stop</td></tr>
<tr><td>Hand crank</td><td>Present, fits, and turns freely</td><td>Needed to return blood if power fails</td></tr>
</tbody></table></div>
{{formula:<strong>Illustration.</strong> The display shows 300 mL/min. In a delivery test you collect 1,350 mL of fluid in 5 minutes: 1,350 &divide; 5 = 270 mL/min, which is 10 percent below the display. Over a four-hour treatment that is roughly 7 liters less blood processed than the record shows.}}
<p>Real flow also falls when the arterial pressure before the pump is very negative. The tubing partly collapses between roller passes, so each pass carries less. The cause is a clinical matter for the nurse, but it explains why a correctly calibrated pump can still deliver less than displayed when the access is poor.</p>
"""),
        ("L", "03", "pressure"),
        ("pverify", "Verifying pressures", "Verifying the pressure sensors", """
<p>A pressure sensor can be wrong in two ways: at zero, or at the top of its range. A good verification checks both, in both directions.</p>
{{flow:A pressure verification|Reference::A calibrated pressure meter with a valid certificate.|Zero::With the port open to air, the display should read zero.|Apply pressure::Connect the reference and a syringe or hand pump to the port, by the manual.|Compare::At several points across the range, positive and negative.|Decide::Within tolerance, record. Outside, calibrate by the manual and repeat.|Prove alarms::Show that readings beyond the limits alarm and stop the pump.}}
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td>Does not read zero when open to air</td><td>Zero drift; recalibrate</td></tr>
<tr><td>Correct at zero, wrong at higher pressures</td><td>Gain error; recalibrate or replace</td></tr>
<tr><td>Slow to respond</td><td>A blocked or wet internal protector or line</td></tr>
<tr><td>Reading drifts while pressure is held</td><td>A leak in the line to the sensor</td></tr>
</tbody></table></div>
"""),
        ("heparin", "Heparin pump", "The heparin syringe pump", """
<p>Many treatments use a small continuous dose of heparin to keep blood from clotting in the circuit. The machine&rsquo;s syringe pump pushes a syringe plunger at a rate the nurse sets. The rate on the display is calculated from how far the plunger travels and from the syringe&rsquo;s diameter. A wider syringe pushes out more for the same travel. So the pump must know exactly which syringe is fitted.</p>
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>Why</th></tr></thead>
<tbody>
<tr><td>The configured syringe brand and size match the syringes the unit buys</td><td>A different syringe diameter delivers a different volume for the same plunger travel</td></tr>
<tr><td>Delivery accuracy: run at a set rate for a set time, and measure the volume delivered</td><td>Confirms the drive</td></tr>
<tr><td>The holder and clamp grip the syringe firmly</td><td>A loose syringe is not driven reliably</td></tr>
<tr><td>End-of-syringe and blockage detection, by the manual</td><td>The pump should alarm, not push silently against a blockage</td></tr>
<tr><td>Stop time function</td><td>The pump should stop before the end of treatment when set to</td></tr>
</tbody></table></div>
{{stop:If the unit changes syringe supplier, tell the nurses and check the pump configuration on every machine before the new syringes are used. This is a medication delivery device.}}
"""),
        ("trouble", "Troubleshooting", "Troubleshooting the blood side", """
<p>Start with what the operators can see and what you can check without opening the machine. Move inward only when the simple checks pass.</p>
<div class="table-wrap"><table>
<thead><tr><th>Symptom</th><th>Check first</th><th>Then</th></tr></thead>
<tbody>
<tr><td>Lower adequacy on one machine</td><td>Tubing size setting; occlusion</td><td>Rotor speed; delivery test; rollers and springs</td></tr>
<tr><td>Pump noisy, or tubing walks out of the track</td><td>Tubing loaded correctly; the correct segment</td><td>Guides, rollers, rotor seating</td></tr>
<tr><td>Pressure reading stuck or sluggish</td><td>External transducer protector wet</td><td>Internal protector and line; sensor</td></tr>
<tr><td>Frequent arterial or venous alarms on many patients on one machine</td><td>Pressure verification</td><td>Sensor; leaks in the sensor lines</td></tr>
<tr><td>Circuits clotting more often on one machine</td><td>Heparin pump syringe configuration and delivery</td><td>Syringe holder; tell the nurse, as clinical causes are common</td></tr>
<tr><td>Pump does not stop when the cover is opened</td><td>Out of service immediately</td><td>Switch, magnet, wiring</td></tr>
</tbody></table></div>
"""),
    ],
    "debrief": ["""
<p><strong>Why might true flow differ from the display?</strong> Displayed blood flow is calculated from pump speed and tubing size. After a rotor replacement, the occlusion may have been left too loose, the rollers or springs may be the wrong ones, or the tubing size setting may have been changed. Any of these lowers the true flow while the screen still shows the prescribed value. Lower blood flow means less cleaning, which is what Dr. Navarro&rsquo;s results show.</p>
<p><strong>What to check on machine 5.</strong> Check the configured tubing size. Test occlusion by the manual. Verify the rotor speed, and do a delivery test if the manual provides one. Then read the service record from four months ago, to see whether occlusion was set and recorded after the rotor change.</p>
<p><strong>What to tell the nephrologist.</strong> Tell Dr. Navarro that the pattern points to the machine and that machine 5 is out of service while you check. When you finish, report what you found, including the as-found figures, so that the clinical team can review the affected treatments. Reviewing the patients is her decision. Giving her accurate numbers is yours.</p>
"""],
    "skills": {"title": "Pump occlusion and pressure verification",
        "intro": "Materials: an out-of-service machine, its service manual, the unit&rsquo;s tubing set, a calibrated pressure meter, a measuring cylinder, a timer, and the unit&rsquo;s heparin syringes.",
        "items": [("Confirms the tubing size setting matches the unit&rsquo;s tubing set.", True),
                  ("Performs the occlusion test by the manual and adjusts if required.", True),
                  ("Verifies rotor speed or flow delivery at the points the manual specifies.", False),
                  ("Inspects rollers, springs, and guides for wear.", False),
                  ("Confirms the cover switch stops the pump.", True),
                  ("Verifies arterial and venous pressure readings against the reference at zero and across the range.", True),
                  ("Confirms the heparin pump&rsquo;s syringe configuration and checks delivery accuracy.", True),
                  ("Confirms the hand crank is present and works.", False),
                  ("Records as-found and as-left values with instrument identities.", False)],
        "placement": "Ask the nephrologist or head nurse whether adequacy results are ever reviewed by machine, and offer the machine list to make that possible."},
    "quiz_keep": [("03", [0, 1, 4, 5])],
    "quiz": [
        ("The display shows 350 mL/min. A delivery test collects 1,575 mL in 5 minutes. What is the true flow?",
         ["315 mL/min", "350 mL/min", "385 mL/min", "1,575 mL/min"], 0, "1,575 &divide; 5 = 315 mL/min, 10 percent below the display."),
        ("The unit changes to a different brand of heparin syringe. What must be checked on every machine?",
         ["The heater", "The syringe pump&rsquo;s configured syringe type and its delivery", "The conductivity cell", "The casters"], 1,
         "Delivery is calculated from syringe diameter; a different syringe changes the dose."),
        ("A pressure display does not read zero with the port open to air. What is needed?",
         ["Nothing", "Zero calibration by the manual", "A new blood pump", "More heparin"], 1, "Zero drift is corrected by calibration."),
        ("Why must the hand crank be present on every machine?",
         ["To start the motor", "To return the patient&rsquo;s blood if power fails", "To adjust occlusion", "To open the cabinet"], 1,
         "It is part of the emergency procedure for power loss."),
    ],
    "terms": [("Gain error", "A sensor that is right at zero but increasingly wrong at higher values."),
              ("Rotor", "The rotating part of the blood pump that carries the rollers."),
              ("Delivery test", "Collecting the fluid a pump moves in a set time to measure its true flow.")],
    "readings": [("dialysis-adequacy.html", "How blood flow affects the dose of dialysis."),
                 ("hemodialysis-access-lifeline.html", "The access that the arterial pressure reflects.")],
}
