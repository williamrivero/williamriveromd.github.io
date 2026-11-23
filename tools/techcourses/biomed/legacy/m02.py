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
{{plain:Think of the fluid side of a dialysis machine as a cook following a recipe for sinigang. Take clean water, warm it, let the bubbles out, add two ingredients in exact amounts, taste the result, and serve it only if it is right. On the way back from the table, the machine measures exactly how much more soup returns than went out. That extra amount is the water removed from the patient.}}
<p>The picture has a limit. A cook tastes with the tongue and can tell salt from sugar. The machine &ldquo;tastes&rdquo; with one electrical measurement that sees only the total amount of salt, not which salts are there. And no cook measures the bowl to the gram, but the machine must, for a whole treatment, with no one checking its arithmetic except you.</p>
{{flow:The dialysate path in a typical machine|Water inlet::Treated water enters through a pressure regulator.|Heater::Warms water to about body temperature.|Degassing::Removes dissolved air.|Proportioning::Adds acid and bicarbonate concentrates in a fixed ratio.|Conductivity and temperature check::Confirms the mix. If it is wrong, bypass.|Balancing system::Sends equal volumes to and from the dialyzer.|Ultrafiltration pump::Removes a measured extra volume.|Blood leak detector and drain::Checks the used fluid for blood, then discards it.}}
{{cards:Key terms for this module|Hydraulics::The parts of the machine that handle fluid.|Proportioning::Mixing water and concentrates in a fixed ratio.|Conductivity::How well the fluid carries electricity; a measure of its total salt content.|Degassing::Removing dissolved air.|Balancing chamber::A device that forces the volume going to the dialyzer to equal the volume coming back.|Bypass::Diverting dialysate past the dialyzer to the drain when it is not safe.}}
""",
    "case": {
        "title": "Patients finishing above their target weight",
        "html": """
<p>For two weeks, the nurses on the morning shift have been writing the same note. Patients treated on machine 7 finish about 300 to 400 grams above the weight expected from the fluid removal set on the screen. The charge nurse, Ms. Carmela Reyes, brings the weight sheets to the biomedical technician, Mr. Danilo Santiago, on a Friday afternoon.</p>
<p>The other machines do not show this pattern. Machine 7 has given no alarms, and it has passed its self-test every day.</p>
""",
        "questions": ["Which part of the machine controls the accuracy of fluid removal?",
                      "Why might the machine give no alarm?",
                      "What should happen to machine 7 today?"],
    },
    "sections": [
        ("prep", "Heat and degas", "Preparing the water: heating and degassing", """
<p>Water enters the machine cold and at a pressure that rises and falls with the plant. A regulator steadies the pressure, and a heater brings the water to roughly 35 to 37 degrees Celsius. Temperature matters to the patient in both directions. Dialysate that is too hot damages red blood cells. Dialysate that is too cold makes the patient shiver. For this reason machines measure temperature with more than one sensor, and they stop dialysate from reaching the dialyzer if it leaves the allowed range, with protection required before it exceeds about 41 degrees Celsius.[[iec60601_2_16]]</p>
<p>Cold water also holds dissolved air. You have seen this at home: bubbles form on the inside of a pot long before the water boils. In the machine, those bubbles collect on conductivity sensors and give false readings. They disturb the balancing system, and they cover part of the dialyzer membrane. The degassing stage holds the water under low pressure so that the air comes out of solution and is vented before the concentrates are added.</p>
{{cards:When heating or degassing goes wrong|Heater scaled or failing::Slow warm-up and temperature alarms.|Temperature sensor drifted::The displayed temperature differs from a reference thermometer.|Degassing pump weak or leaking::Bubbles in the dialysate lines, unstable conductivity, and fluid balance errors.}}
"""),
        ("mix", "Mixing", "Proportioning and conductivity", """
<p>Dialysate is made from three streams: treated water, acid concentrate, and bicarbonate concentrate. The machine mixes them in a fixed ratio, and that ratio depends on the concentrate system the machine is set up for. Ratio systems are not interchangeable. The concentrates must match the machine&rsquo;s configuration.</p>
{{cards:Two ways machines proportion|Fixed-volume (volumetric)::Pumps or chambers deliver set volumes of each stream. Conductivity is then a check on the result.|Conductivity feedback (servo)::Pumps are adjusted until conductivity reaches the target. A second, independent sensor guards against a fault in the first.}}
<p>Why conductivity? Pure water carries almost no electricity. Every dissolved salt adds charged particles, and each one makes the fluid carry current a little better. Final dialysate usually reads around 13 to 15 millisiemens per centimeter, depending on the prescription.</p>
<p>The weakness follows from the same physics. Conductivity measures only the total. It cannot tell which salts are present, so a wrong concentrate can still produce a believable number. That is why operators read the label, and why your calibration of the sensor matters: all of the machine&rsquo;s confidence in its mix rests on that one measurement.</p>
{{fig:diff_conv|What correct dialysate is for: its composition sets the direction and speed of exchange across the membrane. A machine that mixes wrongly changes the treatment.}}
{{key:The conductivity alarm protects against a wrong total. It cannot protect against the wrong recipe. Check sensor accuracy against a reference meter, not against the machine&rsquo;s own display.}}
"""),
        ("bypass", "Bypass", "Bypass: the safe state", """
<p>When conductivity or temperature leaves its limits, a valve sends the dialysate straight to the drain, so it never reaches the dialyzer. Blood keeps circulating, but no exchange takes place. This is bypass. It is the machine&rsquo;s way of saying, &ldquo;I do not trust this fluid.&rdquo;</p>
{{flow:What happens in a conductivity alarm|Sensor detects::The reading is outside the alarm window.|Bypass valve switches::Dialysate goes to the drain, not to the dialyzer.|Alarm sounds::The operator is alerted.|Cause corrected::For example, an empty concentrate container is replaced.|Reading stabilizes::Only then does dialysate return to the dialyzer.}}
<p>When you test a machine, your work is to prove that this chain holds: that an out-of-range reading really does switch the valve. Use the method in the service manual.</p>
"""),
        ("balance", "Fluid balance", "Balancing and ultrafiltration", """
<p>The water removed from the patient must be accurate to within a small margin over a whole treatment. A small error repeated every minute of a treatment becomes a large one. Most machines reach this accuracy with a closed loop.</p>
{{flow:How a balancing system measures fluid removal|Equal in, equal out::A balancing chamber sends a set volume of fresh dialysate to the dialyzer and takes exactly the same volume of used dialysate back.|A closed loop::Because in equals out, the loop cannot gain or lose fluid by itself.|A separate pump::The ultrafiltration pump draws a measured extra volume out of the loop.|The only source::That extra volume can come only across the membrane, from the patient&rsquo;s blood.}}
{{formula:<strong>Fluid removed from the patient</strong> = volume pumped by the ultrafiltration pump (provided the balancing loop is tight and free of air).}}
<p>Notice the condition in that formula. Three faults break it, and none of them is sure to cause an alarm: a small internal leak in the balancing system or its valves, an ultrafiltration pump that delivers slightly more or less than it reports, and air in the loop. For this reason service manuals include a fluid balance test and an ultrafiltration pump calibration, using a measuring cylinder or a calibrated scale. These are among the most important tests you perform.</p>
{{fig:two_compartment|Why accuracy matters to the patient: removing more water than intended can drop blood pressure; removing less leaves the patient overloaded.}}
"""),
    ],
    "debrief": ["""
<p><strong>Which part controls the accuracy of fluid removal?</strong> The balancing system and the ultrafiltration pump. Together they decide how much water leaves the patient.</p>
<p><strong>Why might the machine give no alarm?</strong> A small leak in a balancing valve, or a pump that delivers a little less than it reports, produces an error that is too small and too steady to cross an alarm limit. The self-test checks that the protective functions respond. It does not check that the pump is perfectly calibrated. The pattern the nurses found, one machine and an error always in the same direction, is exactly the kind of evidence that points to a calibration problem.</p>
<p><strong>What should happen to machine 7 today?</strong> Take it out of service today. Run the fluid balance test and the ultrafiltration pump calibration in its service manual. Repair it if it fails, and release it only with documented results. Then thank Ms. Reyes and her nurses. Weights before and after treatment are an independent check on every machine in the unit, and theirs found a fault the machine could not see in itself.</p>
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
