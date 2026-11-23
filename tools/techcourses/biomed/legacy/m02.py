# -*- coding: utf-8 -*-
MODULE = {
    "image_alt": "The hydraulic compartment of a hemodialysis machine with a technician tracing the flow path.",
    "objectives": [
        "Trace the path of water and dialysate through a typical machine, from the water inlet to the drain.",
        "Explain what heating, degassing, proportioning, and conductivity monitoring each do.",
        "Explain how a balancing system and an ultrafiltration pump measure the fluid removed from the patient.",
        "Explain what bypass is and why it protects the patient.",
    ],
    "big": """
{{plain:On the fluid side, a dialysis machine follows a recipe. It takes treated water, warms it, removes air bubbles, adds two concentrates in exact proportion, checks the result, and only then lets it flow past the dialyzer. On the way back it measures exactly how much more fluid comes out than went in. That extra amount is the water removed from the patient.}}
{{flow:The dialysate path in a typical machine|Water inlet::Treated water enters through a pressure regulator.|Heater::Warms water to about body temperature.|Degassing::Removes dissolved air.|Proportioning::Adds acid and bicarbonate concentrates in a fixed ratio.|Conductivity and temperature check::Confirms the mix. If wrong, bypass.|Balancing system::Sends equal volumes to and from the dialyzer.|Ultrafiltration pump::Removes a measured extra volume.|Blood leak detector and drain::Checks used fluid for blood, then discards it.}}
{{cards:Key terms for this module|Hydraulics::The parts of the machine that handle fluid.|Proportioning::Mixing water and concentrates in a fixed ratio.|Conductivity::How well the fluid carries electricity; a measure of its total salt content.|Degassing::Removing dissolved air.|Balancing chamber::A device that forces the volume going to the dialyzer to equal the volume coming back.|Bypass::Diverting dialysate past the dialyzer to the drain when it is not safe.}}
""",
    "case": {
        "title": "Patients finishing above their target weight",
        "html": """
<p>Over two weeks, nurses notice that patients treated on machine 7 finish about 300 to 400 grams above the weight expected from the fluid removal set on the screen. Other machines do not show this. Machine 7 has no alarms and passes its self-tests every day.</p>
""",
        "questions": ["Which part of the machine controls the accuracy of fluid removal?",
                      "Why might the machine give no alarm?",
                      "What should happen to machine 7 today?"],
    },
    "sections": [
        ("prep", "Heat and degas", "Preparing the water: heating and degassing", """
<p>Water enters cold and under varying pressure. A regulator steadies the pressure, and a heater brings the water to roughly 35 to 37 degrees Celsius. Dialysate that is too hot damages red blood cells; too cold, and the patient shivers. Machines therefore measure temperature with more than one sensor and stop dialysate from reaching the dialyzer if it leaves the allowed range, with protection required before it exceeds about 41 degrees Celsius.[[iec60601_2_16]]</p>
<p>Cold water holds dissolved air, which comes out as bubbles when the water is warmed. Bubbles collect on conductivity sensors and give false readings, disturb the balancing system, and cover part of the dialyzer membrane. The degassing stage pulls the water under low pressure so that the air comes out and is vented before the concentrates are added.</p>
{{cards:When heating or degassing goes wrong|Heater scaled or failing::Slow warm-up, temperature alarms.|Temperature sensor drifted::Displayed temperature differs from a reference thermometer.|Degassing pump weak or leaking::Bubbles in the dialysate lines, unstable conductivity, fluid balance errors.}}
"""),
        ("mix", "Mixing", "Proportioning and conductivity", """
<p>Dialysate is made from three streams: treated water, acid concentrate, and bicarbonate concentrate. The machine mixes them in a fixed ratio that depends on the concentrate system it is set up for. Different ratio systems are not interchangeable: concentrates must match the machine&rsquo;s configuration.</p>
{{cards:Two ways machines proportion|Fixed-volume (volumetric)::Pumps or chambers deliver set volumes of each stream. Conductivity is then a check on the result.|Conductivity feedback (servo)::Pumps are adjusted until conductivity reaches the target. A second, independent sensor guards against a fault in the first.}}
<p>Conductivity is used because every dissolved salt adds to it. Final dialysate usually reads around 13 to 15 millisiemens per centimeter, depending on the prescription. But conductivity only measures the total. It cannot tell which salts are present, so a wrong concentrate can produce a believable number. That is why operators read the label and why your calibration of the sensor matters: all the machine&rsquo;s confidence in its mix rests on that one measurement.</p>
{{fig:diff_conv|What correct dialysate is for: its composition sets the direction and speed of exchange across the membrane. A machine that mixes wrongly changes the treatment.}}
{{key:The conductivity alarm protects against a wrong total. It cannot protect against the wrong recipe. Sensor accuracy is checked against a reference meter, not against the machine&rsquo;s own display.}}
"""),
        ("bypass", "Bypass", "Bypass: the safe state", """
<p>If conductivity or temperature leaves its limits, a valve diverts dialysate straight to the drain so that it never reaches the dialyzer. Blood keeps circulating, but no exchange takes place. This is bypass. It is the machine&rsquo;s way of saying, &ldquo;I do not trust this fluid.&rdquo;</p>
{{flow:What happens in a conductivity alarm|Sensor detects::Reading outside the alarm window.|Bypass valve switches::Dialysate goes to drain, not to the dialyzer.|Alarm sounds::The operator is alerted.|Cause corrected::For example an empty concentrate container.|Reading stabilizes::Only then does dialysate return to the dialyzer.}}
<p>When you test a machine, you prove that this chain works: that an out-of-range reading really does switch the valve, by the method in the service manual.</p>
"""),
        ("balance", "Fluid balance", "Balancing and ultrafiltration", """
<p>The amount of water removed from the patient must be accurate to within a small margin over a whole treatment. Most machines achieve this with a closed loop.</p>
{{flow:How a balancing system measures fluid removal|Equal in, equal out::A balancing chamber sends a set volume of fresh dialysate to the dialyzer and takes exactly the same volume of used dialysate back.|A closed loop::Because in equals out, the loop cannot gain or lose fluid by itself.|A separate pump::The ultrafiltration pump draws a measured extra volume out of the loop.|The only source::That extra volume can only come across the membrane, from the patient&rsquo;s blood.}}
{{formula:<strong>Fluid removed from the patient</strong> = volume pumped by the ultrafiltration pump (provided the balancing loop is tight and free of air).}}
<p>Two things spoil this accuracy without necessarily causing an alarm: a small internal leak in the balancing system or its valves, and an ultrafiltration pump that delivers slightly more or less than it reports. Air in the loop does the same. Service manuals therefore include a fluid balance test and an ultrafiltration pump calibration using a measuring cylinder or a calibrated scale. These are among the most important tests you perform.</p>
{{fig:two_compartment|Why accuracy matters to the patient: removing more water than intended can drop blood pressure; removing less leaves the patient overloaded.}}
"""),
    ],
    "debrief": ["""
<p><strong>Case review.</strong> Fluid removal accuracy depends on the balancing system and the ultrafiltration pump. A small leak in a balancing valve or a pump that under-delivers produces an error too small and too steady to trigger an alarm; the self-test checks that protective functions respond, not that the pump is perfectly calibrated. The pattern the nurses noticed, one machine and a consistent direction, is exactly the kind of evidence that points to a calibration problem. Machine 7 should be taken out of service today, given the fluid balance test and ultrafiltration pump calibration in its service manual, repaired if it fails, and released only with documented results. The nurses should be thanked: weights before and after treatment are an independent check on every machine in the unit.</p>
"""],
    "skills": {
        "title": "Tracing the hydraulic path and verifying dialysate",
        "intro": "Materials: an out-of-service machine, its flow diagram from the service manual, a calibrated reference conductivity and temperature meter, and a measuring cylinder.",
        "items": [("Traces the dialysate path on the flow diagram and points to each component on the machine.", False),
                  ("Explains what would happen downstream if degassing failed.", False),
                  ("Confirms the concentrate system the machine is configured for.", True),
                  ("Measures dialysate conductivity and temperature with the reference meter and compares with the display.", True),
                  ("States the allowed difference from the service manual and the action if it is exceeded.", True),
                  ("Demonstrates, by the manual&rsquo;s method, that an out-of-range condition puts the machine into bypass.", True),
                  ("Performs the ultrafiltration accuracy check by the manual&rsquo;s method and records the result.", False)],
        "placement": "With a senior technician, compare the flow diagrams of two different machine models and list what is the same and what differs.",
    },
    "quiz": [
        ("Why is water degassed before concentrates are added?",
         ["To cool it", "Air bubbles cause false conductivity readings and disturb fluid balance", "To remove chlorine", "To add oxygen"], 1,
         "Dissolved air released as bubbles interferes with sensors, the balancing system, and the membrane."),
        ("What does dialysate conductivity measure?",
         ["Potassium only", "The total amount of dissolved salts", "Bacteria", "Temperature"], 1,
         "Conductivity reflects total ionic content, not which salts are present."),
        ("What is bypass?",
         ["A way to skip maintenance", "Diverting dialysate to the drain so it does not reach the dialyzer", "A blood pump setting", "A type of concentrate"], 1,
         "Bypass is the safe state when dialysate temperature or conductivity is out of limits."),
        ("In a balancing-chamber machine, where does the fluid taken by the ultrafiltration pump come from?",
         ["The water inlet", "The concentrate container", "Across the membrane, from the patient&rsquo;s blood", "The drain"], 2,
         "The loop is closed and balanced, so any extra volume removed must cross the membrane."),
        ("One machine consistently leaves patients heavier than expected, with no alarms. What is the most likely area of fault?",
         ["The blood leak detector", "The fluid balance system or ultrafiltration pump calibration", "The power cord", "The screen"], 1,
         "A small, steady error in balancing or pump delivery may not trigger an alarm."),
        ("Why can a wrong concentrate sometimes produce a normal conductivity reading?",
         ["Conductivity sensors are always faulty", "Conductivity measures the total salts, not their identity", "Concentrates have no salts", "The heater corrects it"], 1,
         "Different recipes can give similar totals, which is why labels are checked."),
        ("Against what is a machine&rsquo;s conductivity sensor verified?",
         ["Its own display", "Another machine&rsquo;s display", "A calibrated reference meter", "The operator&rsquo;s judgment"], 2,
         "Only an independent, calibrated instrument can show whether the sensor is right."),
        ("Why must dialysate never be allowed to overheat?",
         ["It wastes electricity", "Overheated dialysate damages red blood cells", "It melts the tubing", "It increases conductivity"], 1,
         "Excess heat causes hemolysis, so machines have independent temperature protection."),
    ],
    "terms": [("Millisiemens per centimeter", "The unit of conductivity used for dialysate."),
              ("Servo control", "Adjusting a pump continuously until a measured value reaches its target."),
              ("Volumetric", "Based on measured volumes."),
              ("Hemolysis", "Red blood cells breaking apart.")],
    "readings": [("dialysis-prescription.html", "What each machine setting means clinically."),
                 ("dry-weight-determination.html", "Why accurate fluid removal matters."),
                 ("dialysis-water-treatment-systems.html", "The water your machines receive.")],
    "calcs": ["calc-ufr-ceiling.html"],
}
