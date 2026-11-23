# -*- coding: utf-8 -*-
"""Hemodialysis Technician track: added practice lessons (machine operation, priming, alarms, machine
disinfection, and dialyzer reprocessing by manual, semi-automated, and automated methods).

ADD[module id] = {"extra": [(after_section_number, id, nav, h2, html)], "quiz_extra": [(stem, options, answer, why)],
                  "skills_extra": [(text, critical)]}
Merged into the Markdown-sourced modules by generate_tech_courses.py."""

ADD = {}

# ───────────────────────── Module 06: operation, priming, machine disinfection ─────────────────────────
ADD["06"] = {
"extra": [
(3, "operate", "Operating the machine", "Operating the machine: from switch-on to shutdown", """
{{plain:Every machine model has its own screens and buttons, but all of them move through the same stages in the same order. If you know the stages, you can find your place on any model, and you can tell when a step has been skipped.}}
{{flow:The stages of one machine day|Switch on and self-test::The machine checks its own sensors, pumps, clamps, and alarms.|Rinse::Any stored disinfectant or stagnant water is flushed out.|Connect concentrates::Acid and bicarbonate, matched to the prescription.|Stabilize::Conductivity and temperature settle inside their limits.|Set up and prime::Lines and dialyzer are mounted and filled with saline.|Pre-treatment checks::Alarms, pressures, dialysate, residual disinfectant.|Treatment::The nurse connects the patient; you observe and report.|End and strip::Blood is returned by the nurse; the used circuit is removed and discarded safely.|Disinfect::Outside surfaces and the internal fluid path.|Shutdown and record::The machine log is completed.}}
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What the machine is doing</th><th>What you do</th><th>Never</th></tr></thead>
<tbody>
<tr><td>Self-test</td><td>Testing the air detector, clamp, blood leak detector, pressure sensors, conductivity and temperature limits, and the alarm sound</td><td>Keep the doors closed and the lines as the screen asks. Read the result; do not assume it passed</td><td>Skip or override a failed test</td></tr>
<tr><td>Concentrates</td><td>Drawing acid and bicarbonate and mixing them with treated water</td><td>Read both labels against the prescription. Check expiry and that the bicarbonate was mixed or opened within the allowed time</td><td>Guess from the color of the container or cap</td></tr>
<tr><td>Stabilize</td><td>Holding dialysate in bypass until conductivity and temperature are in range</td><td>Wait. Confirm the displayed values are stable and in the expected range</td><td>Attach dialysate lines to the dialyzer while the machine is still in bypass alarm</td></tr>
<tr><td>Set up</td><td>Nothing; this stage is yours</td><td>Mount the dialyzer, arterial and venous lines, and pressure lines with transducer protectors. Seat the venous line fully in the air detector and clamp</td><td>Use a set or dialyzer from an open or damaged package</td></tr>
<tr><td>During treatment</td><td>Controlling flows and fluid removal; watching its sensors</td><td>Keep the access and connections uncovered and in view. Record readings at the interval your unit sets. Report changes to the nurse</td><td>Change a treatment setting unless your unit authorizes it and the nurse directs it</td></tr>
<tr><td>After treatment</td><td>Draining; waiting for the disinfection program</td><td>Clamp, remove, and discard the circuit as infectious waste. Wipe all outside surfaces. Start the disinfection program your unit requires</td><td>Carry an unclamped, dripping circuit across the room</td></tr>
</tbody></table></div>
{{key:The manufacturer&rsquo;s instructions for use and your unit&rsquo;s written procedure decide the exact steps. This table tells you what each step is for, so that you notice when one is missing.}}
"""),
(3, "priming", "Priming", "Priming the dialyzer and blood lines, step by step", """
<p>A new dialyzer and blood lines are full of air, and the dialyzer may contain traces of the substances used to make and sterilize it. Priming replaces the air with saline and rinses the dialyzer before blood enters it.</p>
{{cards:What priming achieves|Removes air::Air in the fibers blocks them, so less blood is cleaned, and air in the line is a danger to the patient.|Rinses the dialyzer::Washes out manufacturing and sterilization residues, or the germicide in a reprocessed dialyzer.|Wets the membrane::A wet membrane works properly from the first minute.|Tests the circuit::A leak, a kink, or a loose connection shows up with saline, not with blood.|Readies the machine::The machine can complete its pressure and alarm checks on a filled circuit.}}
{{flow:Priming a new dialyzer, in general terms|Check and wash::Hand hygiene and gloves. Confirm the dialyzer and lines match the prescription. Check packages and expiry.|Mount::Dialyzer in its holder. Arterial line through the blood pump. Venous chamber in its holder. Venous line in the air detector and clamp.|Connect saline::Spike the saline bag using clean technique and connect it to the arterial side as the set is designed.|Fill the arterial line::Let saline push the air ahead of it. Fill the arterial chamber to its mark.|Prime the dialyzer::Run the pump at the priming speed. Saline enters at the bottom of the blood side and pushes air out at the top. Tap and rotate gently to free trapped bubbles.|Fill the venous side::Set the venous chamber level, usually about three quarters full.|Connect dialysate::Only when the machine is out of bypass. Dialysate enters at the bottom and flows opposite to the blood. Clear air from the dialysate side.|Rinse and recirculate::Pass the saline volume the dialyzer&rsquo;s instructions state, then recirculate if your procedure calls for it.|Final check::No air anywhere, all caps and clamps correct, levels set, machine checks passed.}}
<div class="table-wrap"><table>
<thead><tr><th>Common priming error</th><th>What it causes</th><th>How to prevent it</th></tr></thead>
<tbody>
<tr><td>Pump run too fast at the start</td><td>Air trapped inside the fibers, seen as pale streaks; lower clearance and more clotting</td><td>Use the priming speed in the procedure; fill from the bottom upward</td></tr>
<tr><td>Dialyzer left with the wrong end up</td><td>Air cannot escape</td><td>Blood side fills bottom to top; turn the dialyzer as the procedure states</td></tr>
<tr><td>Too little saline passed through</td><td>Residues reach the patient; reactions in the first minutes of treatment</td><td>Measure the volume against the instructions; do not judge by eye</td></tr>
<tr><td>Venous line not fully seated in the air detector</td><td>The detector cannot see air</td><td>Press the line in until it sits flat; close the door</td></tr>
<tr><td>Transducer protector wet with saline</td><td>False pressure readings</td><td>Clamp pressure lines while filling chambers; replace a wet protector</td></tr>
<tr><td>Touching the open ends of lines or the saline spike</td><td>Contamination of the blood path</td><td>Keep caps on until the moment of connection; replace anything that touches a non-sterile surface</td></tr>
<tr><td>Primed circuit left standing for a long time</td><td>Growth of bacteria in warm saline and dialysate</td><td>Follow your unit&rsquo;s time limit; if it is exceeded, discard and set up again</td></tr>
</tbody></table></div>
<p><strong>A reprocessed dialyzer adds four steps.</strong> They are covered in full in Module 11. First, two people confirm that the name on the dialyzer is the patient&rsquo;s. Second, test that germicide is present before rinsing, which proves the dialyzer stayed disinfected in storage. Third, rinse and recirculate exactly as the procedure states. Fourth, test that the germicide is gone, and record the result, before the nurse connects the patient.[[aami_reuse]]</p>
{{stop:If you see air in the circuit, a leak, or a positive residual germicide test, the circuit is not ready. Tell the nurse. Do not hand it over hoping the machine will catch it.}}
"""),
(3, "mdisinfect", "Machine disinfection", "Disinfecting the machine: the operator&rsquo;s part", """
<p>There are two different jobs, and both are needed after every patient.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>Outside surfaces</th><th>Inside fluid path</th></tr></thead>
<tbody>
<tr><td>What is contaminated</td><td>The screen, front panel, clamps, pole, holders, and sides, by gloved hands and blood splashes</td><td>The tubing, valves, and chambers that carry dialysate, by bacteria growing in warm fluid</td></tr>
<tr><td>How it is cleaned</td><td>Wiped with the disinfectant your unit has approved, kept wet for the full contact time on the label</td><td>A built-in program using heat, a chemical, or both</td></tr>
<tr><td>When</td><td>After every patient, as part of station turnover (Module 5)</td><td>As your unit&rsquo;s policy and the manual state: commonly a rinse or disinfection between patients and a full program at the end of the day</td></tr>
<tr><td>How you know it worked</td><td>Every surface was wiped and stayed wet for the contact time</td><td>The machine reports the program complete, and after a chemical program the residual test is negative</td></tr>
</tbody></table></div>
{{flow:An internal disinfection program, operator steps|Remove the circuit::No dialyzer or blood lines on the machine. Dialysate connectors on their rinse ports.|Choose the program::The one your procedure names for this time of day.|Check the supply::The correct disinfectant container is connected, in date, and not empty.|Start and leave it::Do not interrupt. Label the machine so nobody uses it.|Rinse::The machine rinses itself after a chemical program.|Test::Use the correct test strip to show the chemical is gone.|Record::Program, agent, time, test result, your name.}}
<div class="table-wrap"><table>
<thead><tr><th>Program type</th><th>What it is for</th><th>Operator points</th></tr></thead>
<tbody>
<tr><td>Rinse</td><td>Flushes used dialysate; it does not disinfect</td><td>Never counted as disinfection</td></tr>
<tr><td>Heat, or heat with citric acid</td><td>Kills microbes; citric acid also removes scale</td><td>Surfaces and drain line become hot. Allow the cool-down</td></tr>
<tr><td>Acid descaling</td><td>Dissolves the white crust that bicarbonate leaves</td><td>Scale shelters bacteria and upsets sensors, so this program is not optional</td></tr>
<tr><td>Bleach or another chemical disinfectant</td><td>Kills microbes and removes protein and fat film</td><td>Wear the protective equipment on the label. Never mix bleach with acid. Residual test required</td></tr>
</tbody></table></div>
{{stop:Three things take a machine off the floor until they are settled: a disinfection program that did not finish, a positive residual test, and a machine that has stood unused longer than your unit allows without disinfection. Label it and tell the nurse.}}
<p>Machines assigned to patients with hepatitis B stay with those patients, and their outside surfaces need particular care at turnover.[[cdc_dialysis]][[doh2012]] The internal program is the same; the assignment is what protects other patients.</p>
"""),
],
"quiz_extra": [
("What is the main reason a dialyzer is primed from the bottom upward at a slow pump speed?",
 ["It saves saline", "Rising fluid pushes the air out ahead of it and does not trap it in the fibers", "It warms the saline", "It tests the blood leak detector"], 1,
 "Air trapped in fibers blocks them and lowers clearance."),
("A primed circuit shows pale streaks along the dialyzer. What do they most likely mean?",
 ["Normal membrane color", "Air trapped in the fibers", "Too much heparin", "Dialysate is too warm"], 1,
 "Streaks are air-locked fibers; the dialyzer needs further priming or replacement by the unit&rsquo;s procedure."),
("Which statement about the machine&rsquo;s rinse program is correct?",
 ["It disinfects the fluid path", "It flushes fluid but does not disinfect", "It replaces the residual test", "It removes scale"], 1,
 "A rinse is never counted as disinfection."),
("After a chemical disinfection program, what must be shown before the machine is used?",
 ["The cabinet is warm", "A negative residual test with the correct strip", "The screen is clean", "The concentrate is full"], 1,
 "Only the residual test proves the chemical has been rinsed out."),
("When should the dialysate lines be connected to the dialyzer?",
 ["Before the machine is switched on", "When the machine is out of bypass with conductivity and temperature in range", "During the self-test", "After the patient is connected"], 1,
 "Dialysate that is out of range must not reach the dialyzer."),
],
"skills_extra": [
("Primes a dialyzer and blood lines on a training machine with no visible air, the correct saline volume, and correct chamber levels.", True),
("Starts the internal disinfection program named in the procedure and performs the residual test afterward.", True),
],
}

# ───────────────────────── Module 09: alarm guide ─────────────────────────
ADD["09"] = {
"extra": [
(3, "alarms", "Alarm guide", "A chairside guide to machine alarms", """
{{plain:An alarm is the machine asking a person to look. It tells you which sensor noticed a change, not what caused it and not whether the patient is safe. The order is always the same: patient first, access and lines second, machine screen third.}}
{{flow:Every alarm, every time|Look at the patient::Awake? Breathing comfortably? In pain? Bleeding?|Look at the access and lines::Needles or catheter in place, connections tight, no kinks, no blood on the sheet or floor.|Read the alarm::Say the exact words on the screen.|Mute, do not reset blindly::Muting the sound gives you time. Resetting before you find the cause restarts the hazard.|Call the nurse::At once for any alarm on the list of urgent alarms below, and for any alarm you cannot explain.|Record::Time, alarm, what was found, what was done, and by whom.}}
<div class="table-wrap"><table>
<thead><tr><th>Alarm</th><th>What the machine sensed</th><th>Common causes</th><th>What to check first</th><th>Urgency</th></tr></thead>
<tbody>
<tr><td>Arterial pressure low (more negative)</td><td>The pump is pulling harder than blood is arriving</td><td>Kinked arterial line; needle against the vessel wall; patient&rsquo;s arm bent; clotting needle or catheter; low blood pressure</td><td>Patient; arm position; line from access to pump</td><td>Call the nurse; the blood pump usually stops</td></tr>
<tr><td>Venous pressure high</td><td>Resistance to blood returning</td><td>Kinked venous line; clamp left on; clotting in the venous chamber or needle; needle out of position; swelling at the needle site</td><td>Access site for swelling or pain; line from chamber to access</td><td>Call the nurse; swelling at the site is urgent</td></tr>
<tr><td>Venous pressure low</td><td>Less resistance than before</td><td>Line separated; needle slipped out; blood pump slowed or stopped; clotting before the venous sensor</td><td><strong>Uncover the access. Look for blood.</strong></td><td>Urgent. A dislodged needle may cause only a small pressure change</td></tr>
<tr><td>Transmembrane pressure high</td><td>A large pressure difference across the membrane</td><td>Clotting dialyzer; high fluid removal rate; kinked dialysate or venous line</td><td>Dialyzer color; lines</td><td>Call the nurse</td></tr>
<tr><td>Air detector</td><td>Air or foam in the venous line</td><td>Low venous chamber level; loose connection before the pump; empty saline bag; line not seated in the detector</td><td>Do not open the clamp. Look for where air entered</td><td>Urgent. The clamp stays closed until the nurse clears the air</td></tr>
<tr><td>Blood leak</td><td>Blood, or something that looks like it, in used dialysate</td><td>Torn fibers; rarely air bubbles or a dirty sensor</td><td>Dialysate outflow line for a pink tinge</td><td>Urgent. The nurse confirms with a test strip and decides</td></tr>
<tr><td>Conductivity</td><td>Dialysate too weak or too strong</td><td>Empty or wrong concentrate; pick-up tube out of the fluid; crystals in a connector; low water supply</td><td>Concentrate containers and tubes</td><td>Machine goes to bypass. Call the nurse if it does not clear</td></tr>
<tr><td>Temperature</td><td>Dialysate too warm or too cool</td><td>Heater fault; cold water supply; low flow</td><td>Nothing to adjust at the chair</td><td>Machine goes to bypass. Report; biomedical check if repeated</td></tr>
<tr><td>Dialysate flow or water supply</td><td>Not enough water or flow</td><td>Water system problem; kinked inlet hose; closed wall valve</td><td>Other machines: one or several?</td><td>Several machines at once means a water system problem: tell the nurse and the water technician</td></tr>
<tr><td>Blood pump stopped or door open</td><td>Pump not turning</td><td>Door not latched; another alarm stopped it; power</td><td>The other alarm on the screen</td><td>Blood standing still clots within minutes. Call the nurse</td></tr>
<tr><td>Power failure</td><td>Mains supply lost</td><td>Outage; plug pulled; breaker tripped</td><td>Patient; whether the battery is running the blood pump</td><td>Follow the unit&rsquo;s power failure procedure (Module 10)</td></tr>
<tr><td>Heparin pump</td><td>Syringe empty, blocked, or not seated</td><td>Empty syringe; clamped line</td><td>Syringe and its line</td><td>Tell the nurse; medication is the nurse&rsquo;s responsibility</td></tr>
</tbody></table></div>
{{cards:Urgent: call the nurse immediately|Any alarm with a patient who looks or feels unwell::The patient decides the urgency, not the screen.|Blood visible anywhere outside the circuit::Stop and call.|Air detector::Never open the clamp yourself.|Blood leak::Until proven false.|Venous pressure that suddenly drops::Uncover the access.|An alarm that returns after reset::The cause has not been found.}}
<div class="table-wrap"><table>
<thead><tr><th>Unsafe habit</th><th>Why it is dangerous</th></tr></thead>
<tbody>
<tr><td>Resetting an alarm without looking</td><td>The pump restarts into the same problem</td></tr>
<tr><td>Widening pressure limits to stop a repeating alarm</td><td>The machine can no longer see the change it was warning about</td></tr>
<tr><td>Covering the access with a blanket</td><td>A dislodged needle bleeds unseen; the venous alarm may not sound</td></tr>
<tr><td>Turning the alarm volume down</td><td>Nobody hears it</td></tr>
<tr><td>Telling the next shift nothing</td><td>A machine with repeated unexplained alarms stays in use</td></tr>
</tbody></table></div>
{{key:What you may do at an alarm, and what belongs to the nurse, is set by your unit&rsquo;s policy. In every unit, looking at the patient, calling for help, and reporting exactly what the screen says are the technician&rsquo;s job.}}
"""),
],
"quiz_extra": [
("An alarm sounds. What do you look at first?",
 ["The alarm history", "The patient", "The concentrate container", "The clock"], 1,
 "Patient first, access and lines second, screen third."),
("The venous pressure reading drops suddenly during treatment. What must you do at once?",
 ["Reset the alarm", "Uncover and look at the access and the venous line", "Raise the blood flow", "Change the concentrate"], 1,
 "A fall in venous pressure can mean the line has separated or the needle has come out."),
("The air detector alarms and the venous clamp closes. Which action is correct?",
 ["Open the clamp so blood can flow", "Leave the clamp closed and call the nurse", "Reset until it clears", "Switch the machine off and on"], 1,
 "The clamp is what protects the patient from air."),
("Three machines alarm for low water supply at the same time. What does that suggest?",
 ["Three faulty machines", "A problem in the water system", "Three kinked hoses", "A power surge"], 1,
 "One machine or several is the question that separates a machine fault from a supply fault."),
("A venous pressure alarm keeps repeating. A colleague suggests widening the limits. Why is that unsafe?",
 ["It uses more electricity", "The machine could no longer detect the change it is warning about", "It makes the pump louder", "It is not unsafe"], 1,
 "Limits are a protection; the cause of the alarm has to be found."),
],
"skills_extra": [
("In a simulated alarm, looks at the patient and access first, reads the alarm aloud, and calls the nurse without resetting blindly.", True),
],
}

# ───────────────────────── Module 11: reprocessing as a procedure ─────────────────────────
ADD["11"] = {
"extra": [
(1, "lifecycle", "Dialyzer life cycle", "The life of a reprocessed dialyzer", """
<p>A reused dialyzer belongs to one patient from its first treatment to the day it is discarded. Each use is one turn of the same cycle.</p>
{{flow:One dialyzer, from first use to discard|Assign and label::Before first use: patient&rsquo;s full name and a second identifier, dialyzer type, date. A warning mark if another patient has a similar name.|Baseline::The original total cell volume is measured and recorded, before the first treatment.|Treatment::Use number recorded.|Rinse-back and transport::After treatment the ports are capped and the dialyzer goes to the reprocessing room promptly, in a clean covered container.|Reprocess::Rinse and clean, test, fill with germicide, inspect, label.|Store::In the patient&rsquo;s own place, for at least the minimum contact time.|Pre-use checks::Identity, appearance, germicide present, rinse, germicide gone.|Discard::When any rejection rule is met. Recorded with the reason.}}
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Usual rule</th></tr></thead>
<tbody>
<tr><td>Which dialyzers may be reprocessed?</td><td>Only those the manufacturer labels for multiple use, and only where the medical director&rsquo;s policy and the patient&rsquo;s consent allow[[aami_reuse]][[doh2012]]</td></tr>
<tr><td>Which patients&rsquo; dialyzers are not reprocessed?</td><td>Patients with hepatitis B. Other exclusions, such as an active bloodstream infection, are set by the unit&rsquo;s policy and the physician[[cdc_dialysis]]</td></tr>
<tr><td>How soon must reprocessing start?</td><td>Within the time your procedure sets. If it will be delayed, the dialyzer is refrigerated as the procedure states, not left on a counter</td></tr>
<tr><td>How many times may it be reused?</td><td>Until it fails a test or reaches the unit&rsquo;s maximum number, whichever comes first</td></tr>
<tr><td>Can it ever be used for another patient?</td><td>Never</td></tr>
</tbody></table></div>
<div class="table-wrap"><table>
<thead><tr><th>Discard the dialyzer when</th><th>Because</th></tr></thead>
<tbody>
<tr><td>Total cell volume is below 80 percent of its original value</td><td>Too many fibers are blocked for the patient to receive the prescribed treatment</td></tr>
<tr><td>It fails the pressure leak test</td><td>A torn fiber lets blood and dialysate mix</td></tr>
<tr><td>It has reached the maximum number of uses</td><td>Unit policy</td></tr>
<tr><td>The label is missing, unreadable, or does not match</td><td>Identity cannot be proved</td></tr>
<tr><td>The casing, header, or a port is cracked or a cap is missing</td><td>Leaks and contamination</td></tr>
<tr><td>Many dark, clotted fibers or clots in the header remain after cleaning</td><td>Poor performance and risk of reactions</td></tr>
<tr><td>Germicide is absent or too weak when tested before use</td><td>The dialyzer may not have stayed disinfected</td></tr>
<tr><td>It has been stored longer than the germicide&rsquo;s allowed storage time</td><td>Germicide strength falls with time</td></tr>
<tr><td>The patient had an unexplained reaction during its last use</td><td>The dialyzer is held and reported until the cause is known</td></tr>
</tbody></table></div>
{{key:Discarding a doubtful dialyzer costs the price of a dialyzer. Using one costs far more. Nobody should be criticized for discarding.}}
"""),
(1, "coresteps", "The four core steps", "Four steps every method must complete", """
<p>Whether the work is done by hand or by a machine, the same four things have to happen, in the same order.[[aami_reuse]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>What is done</th><th>What it achieves</th><th>What goes wrong</th></tr></thead>
<tbody>
<tr><td>1. Rinse and clean</td><td>The blood side is flushed with treated water. Water is also pushed backward across the membrane from the dialysate side to lift clots out of the fibers. A cleaning agent may be used if the procedure allows</td><td>Removes blood and protein so the germicide can reach every surface</td><td>Too much pressure tears fibers; delay lets blood dry and set; the wrong cleaning agent damages the membrane</td></tr>
<tr><td>2. Test</td><td>Total cell volume is measured and compared with the original. A pressure test checks for leaks</td><td>Proves the dialyzer still cleans well and is intact</td><td>Uncalibrated equipment; comparing with the wrong baseline; recording a result that was not actually measured</td></tr>
<tr><td>3. Fill with germicide</td><td>Both the blood side and the dialysate side are filled completely with germicide at the correct strength, and all four ports are capped with disinfected caps</td><td>Kills microbes during storage</td><td>Air pockets leave surfaces untouched; wrong dilution; expired germicide; a cap left loose</td></tr>
<tr><td>4. Inspect, label, store</td><td>The outside is wiped with disinfectant. The dialyzer is looked at against the light. The label is completed. It is stored in the patient&rsquo;s place</td><td>Makes the dialyzer traceable and keeps it for the contact time</td><td>Label filled in later from memory; dialyzers of similar names stored side by side</td></tr>
</tbody></table></div>
<p><strong>Total cell volume in plain terms.</strong> It is the volume of fluid the fibers hold. A new dialyzer might hold 110 milliliters. If clots block one fifth of the fibers, it holds about 88 milliliters, which is 80 percent of the original, and it is at the limit.</p>
{{formula:<strong>Percent of original</strong> = current total cell volume &divide; original total cell volume &times; 100.<br>Example: original 115 mL, today 101 mL. 101 &divide; 115 &times; 100 = 88 percent. Pass.<br>Example: original 115 mL, today 90 mL. 90 &divide; 115 &times; 100 = 78 percent. Discard.}}
<p><strong>Contact time.</strong> A germicide needs time to work. For peracetic acid germicides the commonly stated minimum is 11 hours; other germicides differ. Use the time on the product&rsquo;s instructions and in your procedure. A dialyzer reprocessed after the evening shift may not be ready for an early morning treatment: check the time on the label, not the date alone.</p>
"""),
(1, "methods", "Three methods", "Manual, semi-automated, and automated reprocessing", """
{{plain:Units use three ways of working. In manual reprocessing a person does every step with simple equipment. In semi-automated reprocessing a device does some steps, usually rinsing and filling, and a person does the rest. In automated reprocessing a machine does the rinse, the tests, and the germicide fill in one program and records the results. In all three, a person still checks identity, connects the dialyzer, caps it, inspects it, and signs.}}
<div class="table-wrap"><table>
<thead><tr><th></th><th>Manual</th><th>Semi-automated</th><th>Automated</th></tr></thead>
<tbody>
<tr><td>Rinse and clean</td><td>By hand, at a rinse station with a pressure gauge</td><td>By the device, on a timer</td><td>By the machine, with controlled pressure and flow</td></tr>
<tr><td>Total cell volume</td><td>Measured by hand: the fluid in the fibers is pushed out with air into a measuring cylinder</td><td>Often by hand</td><td>Measured by the machine and compared with the stored baseline</td></tr>
<tr><td>Leak test</td><td>By hand: pressure is applied and the gauge watched for a fall</td><td>By hand or by the device</td><td>By the machine</td></tr>
<tr><td>Germicide dilution and fill</td><td>Diluted by hand; strength confirmed for each batch; filled by hand</td><td>Diluted and filled by the device</td><td>Diluted and filled by the machine</td></tr>
<tr><td>Record</td><td>Written by hand</td><td>Written by hand</td><td>Printed or stored by the machine, then checked and signed</td></tr>
<tr><td>Main strengths</td><td>Low equipment cost; works during a machine breakdown</td><td>More consistent rinsing and filling</td><td>Most consistent; less staff contact with germicide; automatic record</td></tr>
<tr><td>Main risks</td><td>Depends entirely on the person; easiest to skip or mis-measure a step</td><td>Steps done by hand between device steps can be missed</td><td>False confidence; a machine out of calibration fails every dialyzer the same way</td></tr>
</tbody></table></div>
{{flow:Manual reprocessing, step by step|Prepare::Protective equipment on. Check water pressure, germicide batch, and the patient&rsquo;s record.|Confirm identity::Read the label against the record before you begin.|Rinse the blood side::Treated water through the fibers until the outflow runs clear.|Reverse rinse::Water from the dialysate side across the membrane, within the pressure limit in the procedure, to lift clots.|Clean the headers::Only by the method your procedure allows.|Measure total cell volume::Push the fluid out of the fibers with air into a measuring cylinder. Read at eye level. Calculate the percent of original.|Leak test::Apply the stated pressure and watch the gauge for the stated time.|Fill with germicide::Both sides, no air pockets. Fresh disinfected caps on all four ports.|Wipe, inspect, label::Result, use number, date and time, your name.|Store::In the patient&rsquo;s place. Record the earliest time it can be used.}}
{{flow:Semi-automated reprocessing|Start-of-day checks::Device rinsed, germicide supply connected and in date, strength of the diluted germicide confirmed.|Confirm identity and connect::One dialyzer, one patient, one position.|Device cycle::Rinse, clean, and germicide fill run on the device.|Hand steps::Total cell volume and leak test where the device does not do them. This is the step most often forgotten.|Check the fill::No air; germicide present at the outlet.|Cap, wipe, inspect, label, store::As for manual.|Between dialyzers::The device&rsquo;s own rinse or disinfection step, as its manual states.}}
{{flow:Automated reprocessing|Start-of-day checks::Machine disinfected. Calibration check of volume and pressure with the reference the manufacturer supplies. Germicide connected and in date.|Confirm identity::Enter or scan the patient and dialyzer. The baseline on the screen must be this dialyzer&rsquo;s own.|Connect::All four connections firm and in the right positions.|Run the program::Do not interrupt it.|Read the result::Pass or fail, the measured volume, the leak test. A fail is a fail; do not rerun until it passes.|Remove and cap::Disinfected caps on all four ports.|Wipe, inspect, label::Attach or copy the machine&rsquo;s record. Sign.|Store::In the patient&rsquo;s place.}}
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>Likely cause</th><th>What to do</th></tr></thead>
<tbody>
<tr><td>Every dialyzer fails the volume test this morning</td><td>The machine or measuring equipment is out of calibration; low water pressure</td><td>Stop. Repeat the calibration check. Call the biomedical technician. Do not discard a whole shift&rsquo;s dialyzers on a faulty reading, and do not pass them on one either</td></tr>
<tr><td>Every dialyzer passes, month after month, with no discards</td><td>Tests are not being done or not being recorded honestly; equipment reading high</td><td>Tell the supervisor. Some failures are expected</td></tr>
<tr><td>Volume falls sharply for one patient</td><td>Clotting during treatment; delayed reprocessing</td><td>Discard if below 80 percent. Tell the nurse: the patient&rsquo;s anticoagulation may need review</td></tr>
<tr><td>Germicide test weak at the start of a batch</td><td>Wrong dilution; old concentrate; water flow fault</td><td>Do not use the batch. Remake and retest. Dialyzers already filled from it are reprocessed again</td></tr>
<tr><td>Air pocket seen in a stored dialyzer</td><td>Incomplete fill; loose cap</td><td>Reprocess again or discard, by procedure</td></tr>
<tr><td>Leak test fails after a strong reverse rinse</td><td>Pressure too high tore fibers</td><td>Discard. Check and correct the rinse pressure</td></tr>
<tr><td>Two dialyzers with similar names on one rack</td><td>Storage arrangement</td><td>Separate them and add name-alert labels to both</td></tr>
</tbody></table></div>
{{stop:No method checks identity for you. An automated machine will reprocess the wrong dialyzer perfectly. Read the label against the record at the start, and again before storage.}}
"""),
(1, "room", "Room and staff safety", "The reprocessing room and your own safety", """
<p>Germicides are chosen because they destroy living cells. They do the same to eyes, skin, and lungs. Used dialyzers also carry blood. The room is arranged, and you are dressed, with both in mind.</p>
<div class="table-wrap"><table>
<thead><tr><th>Requirement</th><th>What it looks like</th></tr></thead>
<tbody>
<tr><td>Protective equipment</td><td>Fluid-resistant gown or apron, gloves suited to the germicide, and eye and face protection whenever you handle used dialyzers or germicide</td></tr>
<tr><td>Ventilation</td><td>Working exhaust; no strong smell of germicide. A smell that makes eyes water is reported, not tolerated</td></tr>
<tr><td>Eyewash and spill kit</td><td>Present, in date, and you know where they are and how to use them</td></tr>
<tr><td>Safety data sheets</td><td>One for each chemical, in the room</td></tr>
<tr><td>Clean and dirty flow</td><td>Used dialyzers come in one side; reprocessed dialyzers leave by another. They never share a counter</td></tr>
<tr><td>Water</td><td>Treated water that meets the standard for dialysis water. Tap water is never used on a dialyzer[[iso23500_3]]</td></tr>
<tr><td>Storage</td><td>One labeled place per patient, away from heat and sunlight, with similar names kept apart</td></tr>
<tr><td>Germicide stock</td><td>In the original containers, in date, stored as the label states; opened containers dated</td></tr>
<tr><td>Equipment checks</td><td>Gauges, measuring cylinders, and reprocessing machines checked and calibrated on schedule, with records</td></tr>
<tr><td>Waste</td><td>Discarded dialyzers go into infectious waste (Module 5)</td></tr>
</tbody></table></div>
{{fig:reuse_germicide}}
{{flow:Germicide in the eyes or on the skin|Flush::Eyes at the eyewash, skin under running water, for the time on the safety data sheet. Start within seconds.|Remove::Contaminated clothing.|Tell::The nurse in charge, at once.|Get assessed::As the safety data sheet and unit policy direct.|Report::An incident report, so the cause is corrected.}}
"""),
(2, "preuse", "Before use", "At the chair: five checks before a reprocessed dialyzer is used", """
<p>These checks are the last barrier between a reprocessing error and the patient. Each one is done and recorded on the day of use, at the station.</p>
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>How</th><th>If it fails</th></tr></thead>
<tbody>
<tr><td>1. Identity</td><td>Two staff members read the full name and second identifier on the dialyzer against the patient&rsquo;s record. Where the patient is able, the patient reads the label too</td><td>Hold. Never &ldquo;correct&rdquo; a label at the chair</td></tr>
<tr><td>2. Appearance and time</td><td>Casing and ports intact, all caps on, no air pocket, fibers acceptably clean. Storage time longer than the minimum contact time and shorter than the maximum storage time</td><td>Hold or discard</td></tr>
<tr><td>3. Germicide present</td><td>Before rinsing, test a sample from the dialyzer with the presence test for that germicide</td><td>A negative test means the dialyzer may not be disinfected. Do not use</td></tr>
<tr><td>4. Rinse and prime</td><td>Rinse and recirculate exactly as the procedure states, with the dialysate side flowing</td><td>Repeat the full rinse</td></tr>
<tr><td>5. Germicide gone</td><td>Test a sample with the residual test for that germicide, at the point and time the procedure states. If connection is delayed after a negative test, test again as the procedure requires</td><td>Rinse again and retest. Never connect on a positive test</td></tr>
</tbody></table></div>
{{stop:The presence test and the residual test use different strips and answer opposite questions. One proves the germicide was there. The other proves it has gone. Using the wrong strip gives a comforting and false answer.}}
<p>Tell the nurse immediately if a patient on a reprocessed dialyzer has burning at the access, chest tightness, breathlessness, itching, fever, or chills in the first part of treatment. These can be signs of germicide reaching the blood or of a contaminated dialyzer. The dialyzer and its records are kept for investigation, not thrown away.</p>
"""),
],
"quiz_extra": [
("A dialyzer&rsquo;s original total cell volume was 120 mL. Today it measures 93 mL. What is the correct decision?",
 ["Pass: it is above 90 mL", "Discard: it is below 80 percent of the original", "Reuse once more, then discard", "Retest until it passes"], 1,
 "93 divided by 120 is about 78 percent, which is below the 80 percent limit."),
("In automated reprocessing, which task still depends entirely on a person?",
 ["Measuring total cell volume", "Confirming the dialyzer belongs to the patient named in the record", "Diluting the germicide", "The leak test"], 1,
 "No machine verifies identity; it will reprocess the wrong dialyzer perfectly."),
("Why is water pushed backward across the membrane during rinsing?",
 ["To warm the dialyzer", "To lift clots out of the fibers", "To test for leaks", "To dilute the germicide"], 1,
 "Reverse rinsing dislodges clots; too much pressure can tear fibers."),
("Before rinsing a stored dialyzer at the chair, the germicide presence test is negative. What does that mean?",
 ["The dialyzer is ready", "The dialyzer may not have stayed disinfected and must not be used", "The rinse can be shortened", "The strip is always wrong"], 1,
 "No germicide in storage means no assurance of disinfection."),
("On one morning, every dialyzer fails the automated volume test. What is the most sensible first action?",
 ["Discard them all", "Stop and repeat the machine&rsquo;s calibration check", "Pass them by hand", "Ignore the results"], 1,
 "A fault shared by every dialyzer points to the equipment."),
("Which patient&rsquo;s dialyzer is not reprocessed?",
 ["A patient with diabetes", "A patient with hepatitis B", "A patient over 65", "A patient with a fistula"], 1,
 "Dialyzers from patients with hepatitis B are not reprocessed."),
("In semi-automated reprocessing, which step is most often missed?",
 ["Switching the device on", "The tests done by hand between device steps", "Wearing shoes", "Opening the door"], 1,
 "Hand steps that sit between automatic steps are easy to forget."),
("Germicide splashes into a technician&rsquo;s eye. What comes first?",
 ["Finish the dialyzer", "Flush at the eyewash immediately", "Write the incident report", "Wait to see if it hurts"], 1,
 "Flushing within seconds limits the injury; reporting follows."),
],
"skills_extra": [
("Calculates percent of original total cell volume from two readings and states pass or discard.", True),
("Demonstrates one complete reprocessing cycle on a training dialyzer by the unit&rsquo;s method, in protective equipment.", True),
("Performs the germicide presence test and the residual test with the correct strip for each, and records both.", True),
],
}
