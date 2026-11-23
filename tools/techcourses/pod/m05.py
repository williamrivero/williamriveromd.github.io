# -*- coding: utf-8 -*-
"""Physician on Duty, Module 05: Inside the Machine: How Blood Is Cleaned.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician and a dialysis nurse looking together at the screen of a hemodialysis machine while a patient rests in the chair.",
    "objectives": [
        "Trace the path of blood from the patient, through the circuit, and back, naming each component in order.",
        "Explain diffusion, ultrafiltration, and convection, and say which one removes which substance.",
        "Describe how dialyzers differ in membrane, surface area, and flux, and what the trials of flux found.",
        "Explain what the arterial, venous, and transmembrane pressure readings mean for the patient.",
        "Name each safety detector and the harm it is built to prevent.",
        "Read the machine screen and respond to a common alarm by examining the patient first.",
    ],
    "big": """
{{plain:Put a tea bag in a cup of hot water. Color and flavor move out through the paper into the water, and the leaves stay inside the bag. Nothing pushes them. They spread from where there is more to where there is less. A dialyzer works in a similar way. Blood stays on one side of a thin membrane, clean fluid passes on the other side, and wastes cross from the blood into the fluid.}}
<p>The picture has three limits. A cup of tea soon stops changing, because the water fills with color. The machine keeps fresh fluid flowing, so the movement continues. The dialyzer also removes water by pressure, which a tea bag cannot do. And the blood is outside the body while this happens. Most of the machine exists to make that safe.</p>
{{fig:kidney_vs_dialyzer|The dialyzer does a small part of the kidney&rsquo;s work, for a few hours at a time.}}
<p>The nurses and technicians operate the machine. You need to know what each number and each alarm says about the patient in the chair.</p>
{{cards:Key terms for this module|Extracorporeal circuit::The tubing and dialyzer that carry blood outside the body and back.|Dialyzer::The filter. Blood and dialysis fluid pass on opposite sides of its membrane.|Dialysis fluid::The prepared solution of water and salts that flows through the dialyzer, also called dialysate.|Diffusion::Movement of a dissolved substance from a higher concentration to a lower one.|Ultrafiltration::Movement of water across the membrane, driven by pressure.|Convection::Removal of dissolved substances that are carried along with the water.|Transmembrane pressure (TMP)::The pressure difference between the blood side and the fluid side of the membrane.|Bypass::A safety state in which dialysis fluid goes to the drain instead of to the dialyzer.}}
""",
    "case": {"title": "The venous pressure alarm", "html": """
<p>Mr. Ernesto Bautista, 63, started hemodialysis two months ago. His left forearm fistula was first needled three weeks ago. Today he is ninety minutes into a four-hour session, lying under a blanket, half asleep.</p>
<p>His machine sounds a high venous pressure alarm, and the blood pump stops. Liza, his nurse, straightens his arm, clears the alarm, and restarts the pump. It alarms again four minutes later, and again after that. A technician walking past says, &ldquo;His needle is small. Widen the venous limit so he can finish.&rdquo; Liza looks at you. Mr. Bautista opens his eyes and says that his arm feels tight.</p>
""", "questions": ["What is a high venous pressure alarm telling you about the circuit?",
                  "What do you check in the patient before anyone changes an alarm limit?",
                  "If the alarm had stayed silent, would that prove that the venous needle was in place?"]},
    "sections": [
        ("circuit", "The blood circuit", "The blood circuit, step by step", """
<p>Every pressure reading and every alarm refers to a point on one loop of tubing.</p>
{{fig:blood_circuit}}
<p>Two words need care. The tubing that carries blood away from the patient is called the arterial line, usually marked red. The tubing that returns blood is the venous line, usually marked blue. These names describe direction only. In a patient with a fistula or graft, both needles sit in the same vessel.[[daugirdas2015]]</p>
{{flow:Follow the blood|Access::Blood leaves through the arterial needle or catheter limb.|Arterial line::The arterial pressure sensor measures here.|Blood pump::A roller squeezes the tubing and pushes blood forward at the prescribed flow.|Anticoagulant line::If heparin is prescribed, a syringe pump adds it after the blood pump.|Dialyzer::Wastes and water leave the blood here.|Venous chamber::It traps air bubbles. The venous pressure sensor measures here.|Air detector and clamp::A sensor checks for air. A clamp below it can shut the line at once.|Return::Blood goes back through the venous needle or catheter limb.}}
<p>The blood pump divides the circuit into two zones. Ahead of the pump, the pump is pulling, so the pressure in the tubing is below zero. After the pump, it is pushing, so the pressure is above zero.[[daugirdas2015]] This one fact explains two dangers. A loose connection ahead of the pump does not leak blood. It sucks air in. A loose connection after the pump does the opposite and loses blood.</p>
<p>When the pump stops, the blood in the circuit stands still, and still blood in plastic tubing soon clots. This is why the staff act quickly on an alarm.</p>
{{key:Before you read any number on the screen, look at the patient and then at the circuit. Check that every connection is tight, no line is kinked, the venous chamber has a visible level, and the access is uncovered.}}
"""),
        ("cleaning", "Three ways to clean", "Diffusion, ultrafiltration, and convection", """
<p>The dialyzer does two jobs. It removes dissolved wastes, and it removes water. The machine controls them separately.</p>
<h3>Diffusion: the tea bag</h3>
<p>Dissolved particles move at random. When a membrane separates two solutions, more particles cross from the crowded side than from the other, until both sides are equal.[[hall2021]] This is diffusion. It needs no pressure, only a difference in concentration.</p>
{{fig:pod05_teabag}}
<p>Urea and potassium are higher in the blood than in the dialysis fluid, so they leave the blood. Bicarbonate is higher in the dialysis fluid, so it moves the other way, as Module 2 explained. The composition of the dialysis fluid decides the direction for each substance, which is why it is part of the prescription.</p>
<p>Three things set how fast a substance diffuses: the concentration difference, the size of the molecule, and the flows and membrane area.[[daugirdas2015]] Urea and potassium are small and clear well. Larger wastes clear poorly by diffusion. A blood flow below the prescription delivers less dialysis than planned.</p>
<h3>Ultrafiltration: wringing the cloth</h3>
<p>Think of squeezing grated coconut in a cloth to make gata. Your hands raise the pressure inside the cloth, and liquid is forced through the weave. The solids stay behind. In the dialyzer, the machine makes the pressure on the blood side higher than on the fluid side, and water is pushed out of the blood.[[daugirdas2015]]</p>
{{fig:pod05_ufpressure}}
<p>The pressure difference across the membrane is the transmembrane pressure (TMP). The nurse does not set this pressure. The nurse enters the volume to remove and the time. The machine removes the programmed volume and displays the TMP that this required.[[daugirdas2015]]</p>
<p>The water comes from the plasma. Module 2 explained plasma refilling. The machine removes whatever volume it is told to remove. It does not know whether the patient&rsquo;s tissues can refill the vessels that fast.</p>
<h3>Convection: what the water carries</h3>
<p>The coconut milk that comes through the cloth carries whatever was dissolved in it. In the dialyzer, water pushed through the membrane drags dissolved substances along, up to the size that fits through the pores. This is convection.[[daugirdas2015]]</p>
{{fig:diff_conv|Diffusion moves small molecules down a concentration difference. Convection carries larger ones along with the water.}}
<p>In standard hemodialysis the volume of water removed is small, so diffusion does most of the cleaning.</p>
{{key:The two jobs are separate. A session can remove the planned fluid and still clean poorly, or the reverse.}}
"""),
        ("dialyzer", "The dialyzer", "The dialyzer: fibers, surface, and flux", """
<p>A dialyzer is a plastic cylinder packed with thousands of fine hollow fibers. The wall of each fiber is the membrane. Blood flows inside the fibers. Dialysis fluid flows around them.[[daugirdas2015]]</p>
{{fig:dialyzer_anatomy}}
<p>The two fluids run in opposite directions, which is called countercurrent flow. Blood that has lost most of its urea meets the freshest dialysis fluid, so a concentration difference remains along the whole fiber.[[daugirdas2015]]</p>
{{fig:pod05_fiber}}
<p>Dialyzers differ in three ways. The membrane material is usually a synthetic polymer. The surface area, which is the total area of the fiber walls, is chosen to fit the patient. The third is flux.</p>
<p>Flux causes the most confusion. It does not describe how well a dialyzer removes urea. A low-flux dialyzer with a large surface can remove urea well. Flux describes the pores. Larger pores pass more water for a given pressure, and they pass middle-sized molecules such as beta-2 microglobulin, a protein that builds up in kidney failure. Albumin and blood cells stay in the blood with both types.[[daugirdas2015]]</p>
{{fig:pod05_flux}}
<h3>What the trials of flux found</h3>
<p>Two randomized trials tested whether high flux helps patients live longer. The Hemodialysis (HEMO) Study assigned 1,846 patients on three sessions a week to low-flux or high-flux dialyzers. Death from any cause did not differ significantly between the groups (relative risk with high flux 0.92, 95% confidence interval 0.81 to 1.05).[[eknoyan2002]] The Membrane Permeability Outcome study assigned 738 patients new to hemodialysis and also found no significant difference overall. Among patients who began with a serum albumin of 4 g per dL or lower, a group defined before the trial started, survival was significantly higher with high-flux membranes.[[locatelli2009]]</p>
<p>The 2015 guideline of the United States Kidney Disease Outcomes Quality Initiative (KDOQI) recommends biocompatible membranes and accepts either high-flux or low-flux types.[[kdoqi_hd2015]] In summary, high-flux dialysis removes more middle-sized wastes, and a survival benefit for all patients has not been shown. The HEMO Study enrolled only patients on three sessions a week, so it does not speak directly to twice-weekly schedules.</p>
<p>Hemodiafiltration (HDF) adds a large volume of convection to diffusion and replaces the removed water with sterile fluid made by the machine. In a randomized trial of 1,360 patients, high-dose HDF resulted in fewer deaths from any cause than high-flux hemodialysis over a median of 30 months (hazard ratio 0.77).[[blankestijn2023]] A pooled analysis of five trials with 4,153 patients found a smaller reduction (hazard ratio 0.84).[[vernooij2024]] The first trial enrolled patients judged able to reach a high convection volume, and HDF needs machines and water quality that not every unit has.</p>
{{key:The choice of dialyzer belongs to the prescription. Check that the dialyzer on the machine is the one ordered for this patient.}}
"""),
        ("fluid", "The fluid side", "The dialysis fluid side and what guards it", """
<p>The blood circuit is the half of the machine you can see. The other half, inside the cabinet, makes the dialysis fluid.</p>
{{fig:machine_categories}}
<p>The machine mixes treated water with two concentrates in fixed proportions. One holds the acid and the salts, including potassium and calcium. The other holds bicarbonate. The machine warms the mixture to about body temperature and sends it to the dialyzer.[[daugirdas2015]]</p>
<p>A mistake in mixing cannot be seen, because dilute fluid looks the same as correct fluid. So the machine tests the fluid continuously before it reaches the dialyzer, using two sensors.</p>
<div class="table-wrap"><table>
<thead><tr><th>Sensor</th><th>What it measures</th><th>Harm if it failed</th></tr></thead>
<tbody>
<tr><td>Conductivity</td><td>How well the fluid carries an electric current, which reflects its total salt content, mostly sodium</td><td>Fluid that is too dilute makes red cells swell and burst. Fluid that is too concentrated raises blood sodium</td></tr>
<tr><td>Temperature</td><td>The warmth of the fluid entering the dialyzer</td><td>Overheated fluid destroys red cells. Cold fluid chills the patient</td></tr>
</tbody></table></div>
<p>Destruction of red cells is called hemolysis. Investigators from the United States Centers for Disease Control and Prevention named its most frequent causes during dialysis: chemical contamination, heat, and mechanical injury from blocked or kinked blood lines.[[duffy2000]] The two sensors guard against wrong mixing and heat.</p>
<p>When either sensor reads outside its limits, the machine goes into bypass. A valve sends the dialysis fluid straight to the drain, so none of it reaches the dialyzer. The blood pump keeps running, but no dialysis takes place.[[daugirdas2015]] Bypass is the machine protecting the patient.</p>
<p>Conductivity cannot tell potassium from sodium. A wrong concentrate with the right total salt content can pass the sensor. This is why staff check the concentrate label against the prescription at the start of each session.</p>
{{call:Stop and call for a conductivity or temperature alarm with the patient connected that does not clear at once. Do not allow anyone to override it. Examine the patient for chest or back pain, breathlessness, and a change in alertness, follow your unit&rsquo;s protocol, and call the attending nephrologist. If several machines alarm together, suspect the water or concentrate supply, and call the head nurse and the medical director as well.}}
"""),
        ("pressures", "Pressures", "What the pressure readings say about the patient", """
<p>A pressure reading reports how hard the machine must work to move blood through one part of the circuit. Pressures are shown in millimeters of mercury (mm Hg).</p>
{{fig:pod05_pressures}}
<div class="table-wrap"><table>
<thead><tr><th>Reading</th><th>Where it is measured</th><th>What a change suggests</th></tr></thead>
<tbody>
<tr><td>Arterial pressure</td><td>Between the patient and the blood pump. Normally below zero</td><td>More negative: the access is not delivering blood easily</td></tr>
<tr><td>Venous pressure</td><td>At the venous chamber, after the dialyzer. Normally above zero</td><td>High: something resists the return of blood. Low: resistance is lost or flow has dropped</td></tr>
<tr><td>Transmembrane pressure</td><td>Calculated from the blood side and fluid side pressures</td><td>Rising: fibers are clotting, or fluid removal is fast for this dialyzer</td></tr>
</tbody></table></div>
<p>Alarm limits are set around each reading, following your unit&rsquo;s protocol. Watch the trend as well. A reading that drifts during a session, or differs from the patient&rsquo;s previous sessions, deserves a look even without an alarm.</p>
<h3>Arterial pressure and the blood flow you think you have</h3>
<p>The machine calculates blood flow from how fast the pump turns. When the arterial pressure is very negative, the soft tubing in the pump partly collapses, and each turn moves less blood. The screen then shows a higher flow than the patient receives.[[daugirdas2015]] A persistently poor arterial pressure is information about the access, and the attending nephrologist needs to hear it.</p>
<h3>Venous pressure and the needle that slips out</h3>
<p>It is natural to assume that a venous needle that comes out will trigger the low venous pressure alarm. Often it does not. Most of the venous pressure is created by the narrow needle, not by the patient&rsquo;s vein. When the needle slips out, blood still flows through it, and the pressure may fall very little.</p>
<p>A study of 99 patients measured the pressure inside the access. With the lower alarm limit set 30 to 40 mm Hg below the running pressure, as was usual practice, the investigators estimated that the alarm could be expected to detect a dislodged needle in nearly all grafts and in only 29% of fistulas.[[ribitsch2014]] In a laboratory simulation, the machine alarm sounded in 8 of 19 simulated dislodgements.[[frinak2023]] One study was an estimate from pressure measurements and the other a bench model, so neither gives a true clinical rate. Both point the same way.</p>
<p>A dislodged venous needle can lose a dangerous volume of blood within minutes while the pump keeps running. The defense is visual. Units keep the access and connections uncovered and taped according to protocol. This practice rests on expert recommendation, not on trials.</p>
{{call:Stop and call when a patient is bleeding from the access or the lines, or when the arm is swelling at a needle site. The nurse stops the blood pump and clamps the lines. Apply direct pressure to a bleeding site, assess the patient&rsquo;s circulation, follow your unit&rsquo;s protocol, and call the attending nephrologist. A wider alarm limit is never the answer to a repeating pressure alarm.}}
"""),
        ("detectors", "Safety detectors", "The safety detectors and what each one prevents", """
<p>Each detector exists because of one way that blood outside the body can injure a patient.</p>
{{flow:What each detector protects against|Arterial pressure sensor::A starved pump and unnoticed loss of access flow.|Venous pressure sensor::A blocked return path and, less reliably, a disconnected one.|Air detector and venous clamp::Air entering the patient&rsquo;s vein.|Blood leak detector::Blood loss into the dialysis fluid through torn fibers.|Conductivity sensor::Dialysis fluid with the wrong salt content.|Temperature sensor::Dialysis fluid that is too hot or too cold.}}
<h3>Air</h3>
<p>Air enters where the circuit is below zero pressure, ahead of the blood pump. Common entry points are a loose arterial connection and an empty saline bag left open. The venous chamber traps small bubbles. Below it, a sensor checks the tubing. When it detects air, the machine stops the blood pump and shuts the venous clamp.[[daugirdas2015]]</p>
<p>The detector protects only a line that is seated in it. Air in the venous line is never pushed into the patient. The staff remove it by the unit&rsquo;s procedure, and blood is not returned through that line until the air is gone.</p>
<h3>Blood leak</h3>
<p>If some fibers tear, blood enters the dialysis fluid. A light sensor on the used fluid line detects it and stops the treatment.[[daugirdas2015]] The blood is often too little to see. The staff confirm it by testing the used fluid for blood, following the unit&rsquo;s procedure.</p>
<p>A blood leak matters for two reasons. The patient is losing blood. And a hole that lets blood out also lets dialysis fluid, which is clean but not sterile, touch the blood. Whether the blood in the circuit is returned depends on the size of the leak and on your unit&rsquo;s protocol.</p>
{{call:Stop and call for any blood-leak alarm. Do not allow the alarm to be overridden. The session does not continue on the same dialyzer unless the used fluid tests negative for blood and your unit&rsquo;s protocol allows it. Check the patient&rsquo;s blood pressure, heart rate, and temperature, follow your unit&rsquo;s protocol on whether blood is returned, and call the attending nephrologist.}}
<h3>What no detector sees</h3>
<p>The machine watches the circuit. It does not watch the patient. It has no sensor for chest pain, drowsiness, or blood running under a blanket. A quiet machine means the circuit is within its limits. It does not mean the patient is well.</p>
{{key:Three habits defeat the detectors: overriding an alarm without finding the cause, widening a limit to stop a repeating alarm, and covering the access.}}
"""),
        ("alarms", "Screen and alarms", "Reading the screen and responding to alarms", """
<p>You do not need to learn the menus. Find a few items on the screen and compare each with the prescription and with the patient.</p>
{{fig:pod05_screen}}
<div class="table-wrap"><table>
<thead><tr><th>On the screen</th><th>Compare it with</th></tr></thead>
<tbody>
<tr><td>Blood flow rate</td><td>The prescribed flow, and the arterial pressure</td></tr>
<tr><td>Arterial, venous, and transmembrane pressure</td><td>Earlier readings today and in past sessions</td></tr>
<tr><td>Fluid removal goal, rate, and volume removed</td><td>The patient&rsquo;s blood pressure, symptoms, and weight gain</td></tr>
<tr><td>Time remaining</td><td>The prescribed time. Pauses for alarms shorten real treatment</td></tr>
<tr><td>Conductivity and temperature</td><td>The values set at the start</td></tr>
<tr><td>Blood pressure and pulse</td><td>The time of the reading. It may be old</td></tr>
</tbody></table></div>
<h3>What the machine does when it alarms</h3>
<p>Alarms fall into two families. For a blood-side alarm, the machine stops the blood pump and closes the venous clamp, so the cause must be found quickly. For a dialysis fluid alarm, the machine goes into bypass. Blood keeps moving, but no cleaning takes place.[[daugirdas2015]]</p>
{{flow:When any alarm sounds|Look at the patient::Awake, comfortable, breathing easily, and no blood on the bed or floor.|Look at the access::Uncover it. Check the needle sites or catheter connections.|Trace the circuit::Look for kinks, clamps, clots, air, and loose connections.|Read the alarm::Which sensor, and in which direction.|Let the nurse correct the cause::The alarm is cleared only after the cause is found.|Call if it repeats::An alarm that returns is a finding. Report it to the attending nephrologist.}}
<div class="table-wrap"><table>
<thead><tr><th>Alarm</th><th>Likely causes</th><th>What you check in the patient</th></tr></thead>
<tbody>
<tr><td>Arterial pressure too negative</td><td>Needle against the vessel wall; kinked line; poor fistula inflow; blocked catheter; low blood pressure</td><td>Blood pressure. The thrill (the buzz you feel) and the bruit (the whoosh you hear) over the access. Arm or neck position</td></tr>
<tr><td>Venous pressure high</td><td>Kinked line; clot in the venous chamber; needle out of position or through the vessel wall; narrowed vein beyond the needle</td><td>Swelling, pain, or tightness near the venous needle. Compare both arms</td></tr>
<tr><td>Venous pressure low</td><td>Needle dislodged; line separated; pump slowed; clot ahead of the sensor</td><td>Look for blood at once. Blood pressure, pulse, and color</td></tr>
<tr><td>Transmembrane pressure high</td><td>Fibers clotting; fast fluid removal</td><td>Dark streaks in the dialyzer. Blood pressure and cramps</td></tr>
<tr><td>Air detected</td><td>Loose connection ahead of the pump; empty infusion bag; low chamber level</td><td>Cough, chest tightness, breathlessness, alertness, oxygen saturation</td></tr>
<tr><td>Blood leak</td><td>Torn fibers. Air bubbles in the fluid can give a false alarm</td><td>Blood pressure, pulse, temperature. Fever or chills later</td></tr>
<tr><td>Conductivity or temperature</td><td>Empty or wrong concentrate; water supply problem; mixing or heater fault</td><td>Chest or back pain, breathlessness, confusion. The color of the blood in the venous line</td></tr>
</tbody></table></div>
<h3>When hemolysis is suspected</h3>
<p>Hemolysis during dialysis is rare. In an outbreak traced to narrowed blood tubing, 20 of 30 affected patients had high blood pressure and 18 had abdominal pain. Ten needed intensive care, and two died.[[duffy2000]] Chest or back pain, breathlessness, and translucent blood in the venous line, described as port-wine or cherry red, are other described signs.[[daugirdas2015]]</p>
<p>Burst red cells release potassium. When hemolysis is suspected, dialysis is stopped, the lines are clamped, and the blood in the circuit is not returned to the patient.[[daugirdas2015]] Follow your unit&rsquo;s protocol and call the attending nephrologist at once.</p>
{{key:An alarm is a question about the patient. Answer it at the chair, with your eyes and hands, before anyone touches the screen.}}
"""),
    ],
    "debrief": ["""
<p><strong>What is a high venous pressure alarm telling you?</strong> The machine is meeting resistance when it returns blood to Mr. Bautista. The venous sensor sits after the dialyzer, so the obstruction lies between the venous chamber and his vein. It could be a kinked line, a clot in the chamber, or a needle that has passed through the wall of a new, fragile fistula.</p>
<p><strong>What do you check before anyone changes a limit?</strong> The patient. Ask Liza to keep the pump stopped, lift the blanket, and look at the arm. A new fistula, an arm that feels tight, and a repeating high venous pressure together suggest infiltration, which means that blood is being pumped into the tissue around the vein. Look and feel for swelling above the venous needle, then trace the venous line. Widening the limit would have told the machine to keep pushing blood into his forearm.</p>
<p><strong>Would a silent alarm prove the needle was in place?</strong> No. Most of the venous pressure comes from the needle itself. If a needle slips out, the pressure may fall too little to cross the lower limit.[[ribitsch2014]] The reliable monitor is a visible access, and Mr. Bautista&rsquo;s arm was under a blanket.</p>
<p><strong>What happens next.</strong> The nurse manages the needle according to the unit&rsquo;s protocol. You examine the arm and call the attending nephrologist. Whether the session continues through a new needle site, and how the fistula is used next time, are the nephrologist&rsquo;s decisions. Record the alarm and what you found.</p>
"""],
    "skills": {"title": "Circuit and alarm walk-through on a training machine",
               "intro": "On a primed training machine with no patient connected, identify each component and alarm aloud while a senior dialysis nurse or technician observes.",
               "items": [
                   ("Traces the blood path from the arterial connector to the venous connector, naming each component in order.", True),
                   ("Points to the segment of the circuit that is below zero pressure and explains why air can enter there.", True),
                   ("Identifies the arterial pressure sensor and states what a more negative reading suggests about the access.", True),
                   ("Identifies the venous chamber and venous pressure sensor and gives two causes each for a high and a low reading.", True),
                   ("Identifies the air detector and venous clamp, and confirms that the venous line is seated in both.", True),
                   ("Shows the blood inlet, blood outlet, and the two dialysis fluid ports of the dialyzer, and explains countercurrent flow.", False),
                   ("Reads the dialyzer label and states its membrane type and whether it is low-flux or high-flux.", False),
                   ("Locates the acid and bicarbonate concentrates and checks the concentrate label against a sample prescription.", True),
                   ("Finds on the screen: blood flow, arterial pressure, venous pressure, transmembrane pressure, fluid removal goal and rate, time remaining, conductivity, and temperature.", True),
                   ("Explains what the machine does on a blood-side alarm and on a dialysis fluid alarm, including bypass.", False),
                   ("Locates the blood leak detector and states the two reasons a blood leak matters.", False),
                   ("With the observer triggering three alarms, states for each the likely causes and what to check in the patient before the alarm is cleared.", True),
                   ("States which alarms require a call to the attending nephrologist in this unit, and where the protocol is kept.", False),
               ],
               "placement": "During your supervised shifts, stand with the nurse for ten alarms. For each, write down the sensor, the cause that was found, and what was checked in the patient. Review the list with your preceptor."},
    "quiz": [
        ("In a patient with a forearm fistula, what does the term &ldquo;arterial line&rdquo; mean?",
         ["The tubing connected to an artery", "The tubing that carries blood from the patient toward the dialyzer",
          "The tubing that carries dialysis fluid", "The tubing that returns blood to the patient"], 1,
         "The names describe direction in the circuit. Both needles are in the same vessel."),
        ("A connection comes loose between the arterial needle and the blood pump. What is the main danger?",
         ["Blood sprays out under pressure", "The dialysis fluid becomes too concentrated",
          "Air is drawn into the circuit", "The transmembrane pressure rises"], 2,
         "The pump pulls on this segment, so air is sucked in."),
        ("Which process removes most of the urea and potassium in standard hemodialysis?",
         ["Diffusion down a concentration difference", "Convection with the water removed",
          "Adsorption onto the tubing", "Ultrafiltration by pressure"], 0,
         "Small molecules cross quickly by diffusion. Convection adds little in standard hemodialysis."),
        ("Why do blood and dialysis fluid run in opposite directions through the dialyzer?",
         ["To prevent clotting in the fibers", "To keep the blood warm",
          "To lower the venous pressure", "To keep a concentration difference along the whole length of the fibers"], 3,
         "Blood that is nearly clean meets the freshest fluid, so diffusion continues to the end."),
        ("A colleague says that a high-flux dialyzer &ldquo;gives a better urea clearance.&rdquo; What is the most accurate reply?",
         ["Correct, flux means urea removal", "Flux describes how easily water and larger molecules pass, not urea removal",
          "High-flux membranes let albumin through freely", "Flux refers to the blood flow rate"], 1,
         "Flux depends on pore size. Urea removal depends mostly on surface area and flows."),
        ("What did the HEMO Study find when it compared high-flux with low-flux dialyzers in 1,846 patients?",
         ["A large reduction in deaths with high flux", "More deaths with high flux",
          "No significant difference in death from any cause", "The trial did not study flux"], 2,
         "The relative risk was 0.92, with a confidence interval that includes no effect."),
        ("The machine goes into bypass after a conductivity alarm. What is happening?",
         ["Blood is being returned to the patient automatically", "Dialysis fluid is sent to the drain and does not reach the dialyzer",
          "The blood pump has reversed", "Fluid removal has doubled"], 1,
         "Bypass keeps fluid of the wrong composition away from the blood. No dialysis takes place meanwhile."),
        ("Why can a correct conductivity reading not confirm that the potassium level of the dialysis fluid is right?",
         ["Conductivity measures temperature", "Potassium does not conduct electricity",
          "The sensor is placed after the dialyzer", "Conductivity reflects total salt content, most of which is sodium"], 3,
         "The sensor cannot tell one salt from another, so staff check the concentrate label."),
        ("Mrs. Aquino is dialyzing through a new fistula. The high venous pressure alarm has sounded twice, and her arm hurts near the venous needle. What do you do first?",
         ["Uncover the arm and examine the venous needle site with the pump stopped", "Ask the nurse to raise the upper venous limit",
          "Ask the nurse to increase the blood flow", "Order an analgesic and continue"], 0,
         "This suggests infiltration. Look at the arm before anything on the machine is changed."),
        ("Mr. Ocampo is asleep with his fistula arm under a blanket. The machine is quiet. Why is this unsafe?",
         ["The blanket raises the arterial pressure", "The blanket causes clotting in the venous chamber",
          "A dislodged venous needle may not lower the venous pressure enough to trigger an alarm", "The air detector cannot work in the dark"], 2,
         "Most of the venous pressure comes from the needle itself. A visible access is the safeguard."),
        ("The arterial pressure becomes steadily more negative while the displayed blood flow is unchanged. What is the best interpretation?",
         ["The dialyzer is clotting", "The access is not supplying blood easily, and the true blood flow may be lower than displayed",
          "The dialysis fluid is too warm", "The venous needle has come out"], 1,
         "With strong suction the pump tubing partly collapses and delivers less than the screen shows."),
        ("The transmembrane pressure has climbed for an hour, and dark streaks are visible in the dialyzer. What is the most likely cause?",
         ["Air in the venous line", "A blood leak", "Dialysis fluid that is too dilute", "Clotting of the fibers"], 3,
         "Clotted fibers reduce the working membrane, so more pressure is needed to remove the same water."),
        ("Twenty minutes after a temperature alarm was overridden, Mr. Salonga reports back pain and breathlessness. The blood in his venous line looks translucent, like red wine. What applies to the blood in the circuit?",
         ["It is returned quickly to support his blood pressure", "It is returned slowly with saline",
          "It is not returned, because burst red cells release potassium", "It is returned after the dialyzer is changed"], 2,
         "These signs suggest hemolysis. Dialysis is stopped, the blood is not returned, and the attending nephrologist is called at once."),
        ("A blood-leak alarm sounds. No blood is visible in the fluid tubing, and a technician offers to override the alarm. What is the best response?",
         ["Do not override; assess the patient, have the used fluid tested per protocol, and call the attending nephrologist",
          "Allow the override, because no blood is visible", "Increase the fluid removal rate", "Ask the patient whether to continue"], 0,
         "A small leak may be invisible. Torn fibers mean blood loss and contact with non-sterile fluid."),
        ("Which statement about the randomized evidence for hemodiafiltration is accurate?",
         ["No randomized trial has been done", "One trial found fewer deaths with high-dose hemodiafiltration than with high-flux hemodialysis",
          "Trials show it increases deaths", "It has been shown to benefit only patients on low-flux dialysis"], 1,
         "The hazard ratio for death was 0.77 in selected patients able to reach a high convection volume."),
    ],
    "terms": [("Extracorporeal circuit", "The tubing and dialyzer that carry blood outside the body and back."),
              ("Dialysis fluid (dialysate)", "The prepared solution of water and salts that flows past the membrane."),
              ("Diffusion", "Movement of a dissolved substance from a higher concentration to a lower one."),
              ("Ultrafiltration", "Movement of water across the membrane, driven by a pressure difference."),
              ("Convection", "Removal of dissolved substances carried along with the water that crosses the membrane."),
              ("Countercurrent flow", "Blood and dialysis fluid moving in opposite directions through the dialyzer."),
              ("Flux", "How easily water and larger molecules pass through a membrane, which depends on pore size."),
              ("Transmembrane pressure", "The pressure difference between the blood side and the fluid side of the membrane."),
              ("Bypass", "A safety state in which dialysis fluid is sent to the drain instead of to the dialyzer."),
              ("Hemolysis", "Destruction of red blood cells, which releases their contents into the plasma.")],
    "readings": [("hemodialysis-modalities.html", "How standard hemodialysis, high-flux hemodialysis, and hemodiafiltration compare."),
                 ("high-flux-hd-optimization.html", "More detail on high-flux membranes and middle-sized wastes."),
                 ("dialysis-water-treatment-systems.html", "Where the water for the dialysis fluid comes from and how it is made safe.")],
    "calcs": [],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
