# -*- coding: utf-8 -*-
"""Hemodialysis Technician track, Module 07 (Water Treatment, Concentrates, and Dialysate): deeper lessons
at chairside and daily-check level. Reading the daily water log, the total chlorine and hardness tests,
handling concentrates, what patients experience when water or dialysate is wrong, and a worked failed test.
The Water Treatment Technician track covers the system itself in depth."""

ADD = {
"extra": [
(2, "dailylog", "Daily water log", "Reading the daily water log, line by line", """
{{plain:The water log is a daily health record for the water system. Each line is one reading. A single reading tells you whether today is safe; a row of readings over many days tells you whether something is slowly failing. You do not need to repair the system. You need to read each line, know what it protects, and know when to stop and report.}}
{{fig:wts_hero|Readings are taken at the equipment, at the same points and in the same order every day.}}
<div class="table-wrap"><table>
<thead><tr><th>Log line</th><th>What it means</th><th>Out of range when</th></tr></thead>
<tbody>
<tr><td>Incoming water pressure</td><td>Whether the building is supplying enough water</td><td>Below the minimum on your log sheet</td></tr>
<tr><td>Pressure before and after each filter</td><td>The difference between the two gauges shows how clogged the filter is</td><td>The difference grows beyond the limit on your log sheet, or changes suddenly from yesterday</td></tr>
<tr><td>Softener: hardness after the softener</td><td>Whether calcium and magnesium are being removed, which protects the reverse osmosis membrane</td><td>Above the limit on your log sheet, commonly 1 grain per gallon (about 17 mg/L)</td></tr>
<tr><td>Softener: salt level and timer</td><td>The softener cleans itself with salt water at a set hour, when no treatment is running</td><td>Salt low or formed into a hard crust; timer showing the wrong time of day after a power interruption</td></tr>
<tr><td>Total chlorine after the carbon tanks</td><td>Whether the carbon is still removing chlorine and chloramine</td><td>Above 0.1 mg/L, or above your unit&rsquo;s lower action level</td></tr>
<tr><td>Reverse osmosis (RO): product water conductivity and percent rejection</td><td>How much dissolved salt the membrane is removing</td><td>Conductivity above, or rejection below, the alarm setting on your log sheet; rejection is commonly expected to be 90 percent or more</td></tr>
<tr><td>RO: pressures and product flow</td><td>Whether the membrane is producing enough water</td><td>Outside the range on your log sheet or drifting from the usual values</td></tr>
<tr><td>Bacteria and endotoxin results (from the laboratory, commonly monthly)</td><td>Bacteria are counted as colonies (CFU). Endotoxin is a fragment of dead bacteria that causes fever</td><td>Dialysis water limits: bacteria below 100 CFU/mL and endotoxin below 0.25 EU/mL, with action commonly taken at half of each</td></tr>
</tbody></table></div>
<p>The chlorine, bacteria, and endotoxin figures are the widely used international limits.[[iso23500_3]] For every other line, the limit printed on your log sheet is the one that applies, because it was set for your system.</p>
{{cards:Good logging habits|Write the number::Record the actual reading and its unit, never a tick or the word OK.|Read the trend::Compare with the last several days. A reading still in range but moving steadily is worth reporting.|Never copy yesterday::An entry that was not measured is a false record.|Blank is not normal::A missed reading is reported, not left empty.}}
{{stop:Any reading outside its limit, any reading you could not take, and any alarm on the water system is reported to the nurse and the water technician before patients start. You do not adjust, bypass, or reset water equipment unless you have been trained and assigned to do so.}}
"""),
(2, "chlorinetest", "Chlorine and hardness", "Doing the total chlorine and hardness tests correctly", """
<p>Chlorine and chloramine are added to city water to keep it safe to drink, and the amount changes from day to day without notice. The carbon tanks remove them, and carbon gives no warning when it is used up. The test is the only warning, which is why it is done before each patient shift, or as often as your unit&rsquo;s policy states.</p>
{{flow:Total chlorine test|Run the system::Water must have been flowing through the carbon tanks for at least 15 minutes, so the sample shows working conditions.|Check the kit::It must be a total chlorine test able to read 0.1 mg/L, in date, with the correct reagent.|Go to the right port::The sample port after the first carbon tank, or the one your procedure names. Read the port label.|Flush the port::Let water run briefly, then rinse the sample vial with that water.|Fill exactly::To the mark on the vial.|Add reagent and time it::Mix as the kit instructs and wait the exact reaction time. Use a timer.|Read at once::Against the color chart or on the meter, in good light.|Record::Time, port, result with unit, kit lot, and your name.|Act::If above the limit, follow the next lesson and Section 4.}}
<div class="table-wrap"><table>
<thead><tr><th>Common error</th><th>Result</th><th>Prevention</th></tr></thead>
<tbody>
<tr><td>Using a free chlorine reagent or strip</td><td>Chloramine is missed; the test reads falsely low</td><td>The label must say total chlorine</td></tr>
<tr><td>Sampling just after start-up</td><td>Water that sat in the carbon overnight reads lower than flowing water</td><td>Run for 15 minutes first</td></tr>
<tr><td>Reading too early or too late</td><td>Color not developed, or faded or darkened</td><td>Time the reaction as the kit states</td></tr>
<tr><td>Expired or damp reagent or strips</td><td>Unreliable color</td><td>Check dates; keep containers closed and dry</td></tr>
<tr><td>Dirty vial or wrong sample volume</td><td>False high or false low</td><td>Rinse with sample water; fill to the mark</td></tr>
<tr><td>Wrong sample port</td><td>The result describes a different part of the system</td><td>Match the port label to the log line</td></tr>
<tr><td>Writing &ldquo;0&rdquo; when no color is seen</td><td>The kit cannot prove zero</td><td>Record as below the lowest value the kit can read</td></tr>
</tbody></table></div>
<p><strong>Hardness after the softener.</strong> Hardness means dissolved calcium and magnesium. The softener holds a limited amount before it must clean itself with salt water. For that reason the test is commonly done at the end of the treatment day, when the softener is most used up and a failure is most likely to show.</p>
{{flow:Hardness test|Sample::From the port after the softener, with water flowing.|Test::Use the unit&rsquo;s kit exactly as written, whether a strip or a drop-count test.|Compare::Against the limit on the log sheet.|Look at the salt tank::Salt present, and not set into a hard crust with a hollow space beneath it.|Record and report::A result above the limit goes to the water technician the same day.}}
{{key:A test done carelessly is worse than no test, because it produces a reassuring number. If you doubt a result, repeat it with a fresh sample and say so in the log.}}
"""),
(3, "concentrates", "Handling concentrates", "Acid and bicarbonate concentrates: handling them safely", """
<p>The machine makes dialysate from three streams: treated water, acid concentrate, and bicarbonate concentrate. Despite its name, the acid concentrate carries most of the salts, including the potassium and calcium that differ from patient to patient. The bicarbonate concentrate is the buffer, the part that corrects acid in the blood.</p>
<div class="table-wrap"><table>
<thead><tr><th>Check on the acid container</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Potassium and calcium values on the label equal the prescription</td><td>These are the values most often different between patients, and conductivity cannot detect the difference</td></tr>
<tr><td>Mixing ratio family on the label matches the machine&rsquo;s setting and the bicarbonate product</td><td>Concentrates are made for particular proportioning ratios; a mismatch gives the wrong dialysate</td></tr>
<tr><td>Expiry date, intact seal, clear fluid with no crystals</td><td>Damaged or old product may not have the stated composition</td></tr>
<tr><td>Read the words, not the cap or jug color</td><td>Color schemes differ between manufacturers</td></tr>
</tbody></table></div>
{{flow:Mixing bicarbonate from powder|Prepare::Hand hygiene and gloves. Use a container that has been cleaned and is dry.|Check the powder::Correct product for the machine, in date, bag intact and dry.|Add treated water::Dialysis water only, never tap water, to the volume mark the product states.|Add all the powder::One full bag to its stated volume. Never a part bag.|Mix gently::Until fully dissolved and clear, as the instructions state. Do not shake hard or mix longer than directed.|Label::Date and time mixed, your initials, and the discard time.|Use in time::Within the limit the manufacturer and unit policy state.}}
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>Reason</th></tr></thead>
<tbody>
<tr><td>Never top up a partly used container with fresh solution</td><td>Bacteria from the old solution seed the new batch, and the mixing time on the label becomes false</td></tr>
<tr><td>Discard mixed bicarbonate at its time limit</td><td>Bicarbonate solution has no preservative and bacteria grow in it readily</td></tr>
<tr><td>Do not over-mix, and keep containers capped</td><td>Bicarbonate loses carbon dioxide to the air, which changes its pH</td></tr>
<tr><td>Rinse containers with treated water, disinfect them on the unit&rsquo;s schedule, and store them upside down to dry</td><td>A wet container left standing grows a bacterial film</td></tr>
<tr><td>Keep pick-up wands off the floor and wipe them at turnover</td><td>The wand goes straight into the fluid</td></tr>
<tr><td>Never pour acid and bicarbonate concentrates together</td><td>They react and form a hard white scale</td></tr>
</tbody></table></div>
{{stop:An unlabeled container, a container past its time, cloudy solution, or undissolved powder is not used. Set it aside, tell the nurse, and prepare a fresh one.}}
"""),
(4, "patientsigns", "When water is wrong", "What patients experience when water or dialysate is wrong", """
{{plain:Every patient on a shift shares the same water. One patient feeling unwell usually has a personal cause. Several patients developing the same complaint within minutes of each other points to the water or the dialysate until proven otherwise, and the technician walking the floor is often the first to see the pattern.}}
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>What it does</th><th>Signs, often in several patients</th><th>Technician&rsquo;s first action</th></tr></thead>
<tbody>
<tr><td>Chloramine or chlorine passing the carbon</td><td>Damages red blood cells so that they burst, called hemolysis</td><td>Chest or back pain, shortness of breath, nausea, falling blood pressure; blood in the lines may look darker or clear cherry-red. Over weeks, anemia worsens across the unit</td><td>Call the nurse at once and say that more than one patient is affected. Check when the last chlorine test was done</td></tr>
<tr><td>Dialysate too dilute (low conductivity)</td><td>Water enters red cells; hemolysis</td><td>Cramps, headache, nausea, low blood pressure, signs of hemolysis as above</td><td>Call the nurse. Report the conductivity reading and any alarm. Check the concentrate containers and wands</td></tr>
<tr><td>Dialysate too concentrated (high conductivity)</td><td>Too much salt enters the patient</td><td>Intense thirst, headache, rising blood pressure</td><td>Call the nurse. Report the reading. Do not reset the alarm to continue</td></tr>
<tr><td>Bacteria or endotoxin in water, concentrate, or dialysate</td><td>Endotoxin triggers a fever reaction</td><td>Shaking chills and fever, commonly beginning in the first hour or two, with muscle aches, nausea, or low blood pressure</td><td>Call the nurse. Note which stations, which bicarbonate batch, and the time each patient started</td></tr>
<tr><td>Hard water (softener failure with poor RO performance)</td><td>Excess calcium and magnesium reach the patient</td><td>Nausea, vomiting, headache, weakness, high blood pressure</td><td>Call the nurse. Check the latest hardness and RO readings on the log</td></tr>
<tr><td>Dialysate too hot</td><td>Heat damages red cells</td><td>Feeling hot, flushed, signs of hemolysis</td><td>Call the nurse. Report the displayed temperature</td></tr>
</tbody></table></div>
<p>The nurse and nephrologist decide whether treatments stop and what care the patients need. Do not discard anything that may be needed to find the cause: keep the concentrate containers, note lot numbers, and leave the machines as they are unless the nurse directs otherwise.</p>
{{key:Say the pattern out loud: &ldquo;Station 4 and Station 7 both have chills, and both started at 6:10.&rdquo; One sentence that links two patients can protect everyone else on the shift.}}
"""),
(4, "failedtest", "A failed test: example", "Worked scenario: a failed chlorine test at shift start", """
<p>Section 4 gives the rule: hold, notify, and wait for release. This fictional example puts numbers and words on it. Many systems have two carbon tanks in a row. The first does most of the work, and the second is the backup. The exact response belongs to your unit&rsquo;s written procedure; this is a common pattern.</p>
<div class="table-wrap"><table>
<thead><tr><th>Time</th><th>What happens</th><th>What it means</th></tr></thead>
<tbody>
<tr><td>05:10</td><td>Water system started</td><td>The 15-minute run begins</td></tr>
<tr><td>05:30</td><td>Total chlorine after the first carbon tank reads 0.3 mg/L. The limit is 0.1 mg/L</td><td>Three times the limit. The first tank is letting chlorine through</td></tr>
<tr><td>05:32</td><td>Technician tells the charge nurse and asks that no patient be connected</td><td>The hold starts now, before any further testing</td></tr>
<tr><td>05:35</td><td>As the procedure directs, the test is repeated with a fresh sample, and a sample is taken after the second tank. Results: first tank 0.3 mg/L again; second tank below 0.1 mg/L</td><td>The reading is real, and the backup tank is still protecting the water</td></tr>
<tr><td>05:40</td><td>Technician reports to the water technician and charge nurse</td><td>Those with authority decide</td></tr>
</tbody></table></div>
{{cards:The report, word for word|Situation::&ldquo;Total chlorine after the first carbon tank is 0.3 milligrams per liter at 05:30. Our limit is 0.1.&rdquo;|Confirmation::&ldquo;I repeated it at 05:35 with a fresh sample and it is again 0.3. After the second tank it reads below 0.1.&rdquo;|Status::&ldquo;The system ran 15 minutes before sampling. No patient is connected. I have asked the charge nurse to hold all starts.&rdquo;|Request::&ldquo;Please tell me whether we may start, and what testing you want during the shift. I will record your decision and the time.&rdquo;}}
<p>In many procedures, a result within the limit after the second tank allows treatment to go ahead with more frequent testing while the first tank is serviced. That is the decision of the person your unit authorizes, not of the technician who ran the test.</p>
<p><strong>If the second tank had also read above 0.1 mg/L:</strong> no treatment starts on that water, the hold continues, and the unit follows its contingency plan. If patients were already on treatment when a high result was found, the technician tells the nurse immediately, and the nurse acts for the patients.</p>
{{stop:Three things are never acceptable: starting patients &ldquo;while we wait for the call back,&rdquo; repeating the test until a passing number appears, and recording a result that was not measured.}}
"""),
],
"quiz_extra": [
("Before a total chlorine sample is taken at the start of the day, the water system should have been running for at least how long?",
 ["1 minute", "5 minutes", "15 minutes", "2 hours"], 2,
 "Flowing water shows how the carbon performs under working conditions; water that sat overnight reads falsely low."),
("Which widely used limit applies to total chlorine in water used for dialysis?",
 ["At most 0.1 mg/L", "At most 1.0 mg/L", "At most 4.0 mg/L", "Any level safe for drinking"], 0,
 "The widely used standard limit is 0.1 mg/L; drinking-water levels are far too high for dialysis."),
("Why is the hardness test commonly done at the end of the treatment day?",
 ["The water is warmer", "The laboratory is open", "The RO unit is switched off", "The softener is most used up then, so a failure is most likely to show"], 3,
 "Testing at the point of greatest exhaustion gives the earliest warning."),
("A bicarbonate container is one third full of solution mixed earlier. A coworker suggests adding freshly mixed solution to fill it. What is correct?",
 ["Acceptable if the solution is clear", "Never top up; use a clean container for the fresh batch and discard the old solution at its time limit", "Acceptable if the label is updated", "Acceptable if shaken well"], 1,
 "Topping up carries bacteria into the new batch and makes the mixing time on the label false."),
("Within ten minutes, three patients on the same shift report chest pain and shortness of breath, and the blood in their lines looks unusually clear and red. What should the technician suspect and do first?",
 ["Anxiety; reassure them", "Three separate access problems; reposition the arms", "A water or dialysate problem; call the nurse at once and say that several patients are affected", "A scale error; reweigh them"], 2,
 "The same complaint in several patients at once points to what they share: the water and dialysate."),
("Total chlorine after the first carbon tank is 0.3 mg/L and after the second tank is below 0.1 mg/L. Who decides whether treatments may start?",
 ["The person the unit authorizes, after the technician reports both results", "The technician who ran the test", "The first patient to arrive", "Nobody; treatments start because the second tank passed"], 0,
 "The technician holds, reports exact results, and records the decision; release belongs to the authorized person."),
("The acid concentrate label shows a different potassium value from the prescription, but machine conductivity is in range. What does this mean?",
 ["The concentrate is acceptable", "The prescription is wrong", "The conductivity meter is faulty", "Conductivity cannot detect the difference; hold the setup and tell the nurse"], 3,
 "Small differences in potassium or calcium do not move conductivity out of range."),
],
"skills_extra": [
("Performs a total chlorine test on a training sample: confirms run time, kit type and expiry, sample port, fill volume, and timed reaction, and records the result with its unit.", True),
("Mixes a batch of bicarbonate on a training setup with treated water, a full bag, and gentle mixing, and labels the container with date, time, initials, and discard time.", False),
("Reports a simulated failed chlorine test using situation, confirmation, status, and request, with exact values and times.", True),
],
}
