# -*- coding: utf-8 -*-
"""Hemodialysis Technician track, Module 07 (Water Treatment, Concentrates, and Dialysate): deeper lessons
at chairside and daily-check level. Reading the daily water log, the total chlorine and hardness tests,
handling concentrates, what patients experience when water or dialysate is wrong, and a worked failed test.
The Water Treatment Technician track covers the system itself in depth."""

ADD = {
"extra": [
(2, "dailylog", "Daily water log", "Reading the daily water log, line by line", """
{{plain:Think of the water log as the weight chart a barangay health worker keeps for a growing child. One visit tells you whether the child is well today. A line of visits tells you whether the child is slowly falling behind, long before anyone looks sick. Each line of the water log is one visit for one part of the system.}}
<p>The picture has a limit. A health worker who sees a problem refers the child; she does not treat the child herself. Your position is the same. You do not repair the water system. Your work is to read each line, know what it protects, and know when to stop and report.</p>
{{fig:wts_hero|Readings are taken at the equipment, at the same points and in the same order every day.}}
<div class="table-wrap"><table>
<thead><tr><th>Log line</th><th>What it means</th><th>Out of range when</th></tr></thead>
<tbody>
<tr><td>Incoming water pressure</td><td>Whether the building is supplying enough water to the system</td><td>Below the minimum on your log sheet</td></tr>
<tr><td>Pressure before and after each filter</td><td>The difference between the two gauges shows how clogged the filter has become</td><td>The difference grows past the limit on your log sheet, or changes suddenly from yesterday</td></tr>
<tr><td>Softener: hardness after the softener</td><td>Whether calcium and magnesium are being removed, which protects the reverse osmosis membrane downstream</td><td>Above the limit on your log sheet, commonly 1 grain per gallon (about 17 mg/L)</td></tr>
<tr><td>Softener: salt level and timer</td><td>The softener cleans itself with salt water at a set hour, when no treatment is running</td><td>Salt low or formed into a hard crust; timer showing the wrong time of day after a power interruption</td></tr>
<tr><td>Total chlorine after the carbon tanks</td><td>Whether the carbon is still removing chlorine and chloramine</td><td>Above 0.1 mg/L, or above your unit&rsquo;s lower action level</td></tr>
<tr><td>Reverse osmosis (RO): product water conductivity and percent rejection</td><td>How much dissolved salt the membrane is taking out</td><td>Conductivity above, or rejection below, the alarm setting on your log sheet; rejection is commonly expected to be 90 percent or more</td></tr>
<tr><td>RO: pressures and product flow</td><td>Whether the membrane is producing enough water</td><td>Outside the range on your log sheet, or drifting away from the usual values</td></tr>
<tr><td>Bacteria and endotoxin results (from the laboratory, commonly monthly)</td><td>Bacteria are counted as colonies (CFU). Endotoxin is a fragment of dead bacteria that causes fever</td><td>Dialysis water limits: bacteria below 100 CFU/mL and endotoxin below 0.25 EU/mL, with action commonly taken at half of each</td></tr>
</tbody></table></div>
<p>The chlorine, bacteria, and endotoxin figures are the widely used international limits.[[iso23500_3]] For every other line, use the limit printed on your log sheet. It was set for your own system, and a number from another unit does not apply.</p>
{{cards:Good logging habits|Write the number::Record the actual reading and its unit. A tick or the word OK tells the next reader nothing.|Read the trend::Compare today with the last several days. A reading that is still in range but moving steadily in one direction is worth reporting.|Never copy yesterday::An entry that was not measured is a false record, however likely the number.|Blank is not normal::A reading you missed is reported, not left empty for someone else to notice.}}
{{stop:Report to the nurse and the water technician, before patients start, any reading outside its limit, any reading you could not take, and any alarm on the water system. You do not adjust, bypass, or reset water equipment unless you have been trained and assigned to do so.}}
"""),
(2, "chlorinetest", "Chlorine and hardness", "Doing the total chlorine and hardness tests correctly", """
<p>City water carries chlorine and chloramine so that it is safe to drink, and the amount changes from day to day without notice. The carbon tanks take them out. Carbon gives no sign when it is used up: the water looks, smells, and flows the same. The test is the only warning you get. That is why it is done before each patient shift, or as often as your unit&rsquo;s policy states.</p>
{{flow:Total chlorine test|Run the system::Water must have flowed through the carbon tanks for at least 15 minutes, so that the sample shows working conditions.|Check the kit::It must be a total chlorine test that can read 0.1 mg/L, in date, with the correct reagent.|Go to the right port::The sample port after the first carbon tank, or the one your procedure names. Read the port label before you open it.|Flush the port::Let the water run briefly, then rinse the sample vial with that same water.|Fill exactly::Up to the mark on the vial, no more and no less.|Add reagent and time it::Mix as the kit instructs and wait the exact reaction time. Use a timer, not a guess.|Read at once::Against the color chart or on the meter, in good light.|Record::The time, the port, the result with its unit, the kit lot, and your name.|Act::If the result is above the limit, follow the next lesson and Section 4.}}
<div class="table-wrap"><table>
<thead><tr><th>Common error</th><th>Result</th><th>Prevention</th></tr></thead>
<tbody>
<tr><td>Using a free chlorine reagent or strip</td><td>Chloramine is missed, so the test reads falsely low</td><td>The label must say total chlorine</td></tr>
<tr><td>Sampling just after start-up</td><td>Water that sat in the carbon overnight reads lower than water that is flowing</td><td>Run for 15 minutes first</td></tr>
<tr><td>Reading too early or too late</td><td>The color has not developed yet, or has faded or darkened</td><td>Time the reaction exactly as the kit states</td></tr>
<tr><td>Expired or damp reagent or strips</td><td>The color cannot be trusted</td><td>Check the dates; keep containers closed and dry</td></tr>
<tr><td>Dirty vial or wrong sample volume</td><td>A false high or a false low</td><td>Rinse with sample water; fill to the mark</td></tr>
<tr><td>Wrong sample port</td><td>The result describes a different part of the system</td><td>Match the port label to the log line</td></tr>
<tr><td>Writing &ldquo;0&rdquo; when no color is seen</td><td>The kit cannot prove zero</td><td>Record the result as below the lowest value the kit can read</td></tr>
</tbody></table></div>
<p><strong>Hardness after the softener.</strong> Hardness means dissolved calcium and magnesium. A softener works like a sponge: it holds only so much before it must be wrung out, which for a softener means cleaning itself with salt water. So the test is commonly done at the end of the treatment day, when the softener is most used up and a failure is most likely to show.</p>
{{flow:Hardness test|Sample::From the port after the softener, with the water flowing.|Test::Use the unit&rsquo;s kit exactly as written, whether it is a strip or a drop-count test.|Compare::With the limit on the log sheet.|Look at the salt tank::Salt should be present, and not set into a hard crust with a hollow space underneath.|Record and report::A result above the limit goes to the water technician the same day.}}
{{key:A careless test is worse than no test, because it produces a number that reassures everyone. If you doubt a result, repeat it with a fresh sample and say so in the log.}}
"""),
(3, "concentrates", "Handling concentrates", "Acid and bicarbonate concentrates: handling them safely", """
<p>Think of the machine as a cook following a fixed recipe: so many parts water, so many parts of each concentrate, every minute of the session. It does not taste the result. The machine builds dialysate from three streams: treated water, acid concentrate, and bicarbonate concentrate. Despite its name, the acid concentrate carries most of the salts, including the potassium and calcium that differ from patient to patient. The bicarbonate concentrate is the buffer, the part that corrects acid in the blood.</p>
<p>The practical point is that the machine trusts whatever container it is given. The checks on the label are yours.</p>
<div class="table-wrap"><table>
<thead><tr><th>Check on the acid container</th><th>Why</th></tr></thead>
<tbody>
<tr><td>The potassium and calcium values on the label equal the prescription</td><td>These are the values that most often differ between patients, and conductivity cannot detect the difference</td></tr>
<tr><td>The mixing ratio family on the label matches the machine&rsquo;s setting and the bicarbonate product</td><td>Concentrates are made for particular proportioning ratios; a mismatch produces the wrong dialysate</td></tr>
<tr><td>Expiry date, intact seal, clear fluid with no crystals</td><td>Damaged or old product may not have the composition on the label</td></tr>
<tr><td>Read the words, not the cap or jug color</td><td>Color schemes differ between manufacturers</td></tr>
</tbody></table></div>
{{flow:Mixing bicarbonate from powder|Prepare::Hand hygiene and gloves. Use a container that has been cleaned and is dry.|Check the powder::The correct product for the machine, in date, with the bag intact and dry.|Add treated water::Dialysis water only, never tap water, up to the volume mark the product states.|Add all the powder::One full bag to its stated volume. Never part of a bag.|Mix gently::Until the powder is fully dissolved and the solution is clear, as the instructions state. Do not shake hard or mix longer than directed.|Label::The date and time mixed, your initials, and the discard time.|Use in time::Within the limit the manufacturer and unit policy state.}}
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>Reason</th></tr></thead>
<tbody>
<tr><td>Never top up a partly used container with fresh solution</td><td>Bacteria from the old solution seed the new batch, and the mixing time on the label is no longer true</td></tr>
<tr><td>Discard mixed bicarbonate at its time limit</td><td>Bicarbonate solution has no preservative, and bacteria grow in it readily</td></tr>
<tr><td>Do not over-mix, and keep containers capped</td><td>Bicarbonate loses carbon dioxide to the air, which changes its pH</td></tr>
<tr><td>Rinse containers with treated water, disinfect them on the unit&rsquo;s schedule, and store them upside down to dry</td><td>A wet container left standing grows a film of bacteria</td></tr>
<tr><td>Keep pick-up wands off the floor and wipe them at turnover</td><td>The wand goes straight into the fluid</td></tr>
<tr><td>Never pour acid and bicarbonate concentrates together</td><td>They react and form a hard white scale</td></tr>
</tbody></table></div>
{{stop:Do not use a container that is unlabeled, past its time, or cloudy, or that has undissolved powder in it. Set it aside, tell the nurse, and prepare a fresh one.}}
"""),
(4, "patientsigns", "When water is wrong", "What patients experience when water or dialysate is wrong", """
{{plain:Picture a fiesta where every guest eats from the same pot of adobo. One guest with a stomachache may have eaten something at home. Five guests sick within the same hour point to the pot. On a dialysis shift every patient shares the same water, so several patients with the same complaint within minutes of each other point to the water or the dialysate until proven otherwise.}}
<p>The picture has a limit. At a fiesta the pot can wait until everyone has gone home. On a shift the patients are still connected, so the pattern has to be spoken the moment you see it. The technician walking the floor is often the first person in a position to see it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>What it does</th><th>Signs, often in several patients</th><th>Technician&rsquo;s first action</th></tr></thead>
<tbody>
<tr><td>Chloramine or chlorine passing the carbon</td><td>Damages red blood cells so that they burst, which is called hemolysis</td><td>Chest or back pain, shortness of breath, nausea, falling blood pressure; blood in the lines may look darker or a clear cherry red. Over weeks, anemia worsens across the unit</td><td>Call the nurse at once and say that more than one patient is affected. Check when the last chlorine test was done</td></tr>
<tr><td>Dialysate too dilute (low conductivity)</td><td>Water moves into red cells; hemolysis</td><td>Cramps, headache, nausea, low blood pressure, and the signs of hemolysis above</td><td>Call the nurse. Report the conductivity reading and any alarm. Check the concentrate containers and wands</td></tr>
<tr><td>Dialysate too concentrated (high conductivity)</td><td>Too much salt enters the patient</td><td>Intense thirst, headache, rising blood pressure</td><td>Call the nurse. Report the reading. Do not reset the alarm to keep going</td></tr>
<tr><td>Bacteria or endotoxin in water, concentrate, or dialysate</td><td>Endotoxin sets off a fever reaction</td><td>Shaking chills and fever, commonly starting in the first hour or two, with muscle aches, nausea, or low blood pressure</td><td>Call the nurse. Note which stations, which bicarbonate batch, and the time each patient started</td></tr>
<tr><td>Hard water (softener failure with poor RO performance)</td><td>Too much calcium and magnesium reach the patient</td><td>Nausea, vomiting, headache, weakness, high blood pressure</td><td>Call the nurse. Check the latest hardness and RO readings on the log</td></tr>
<tr><td>Dialysate too hot</td><td>Heat damages red cells</td><td>Feeling hot, flushed, signs of hemolysis</td><td>Call the nurse. Report the temperature on the display</td></tr>
</tbody></table></div>
<p>The nurse and the nephrologist decide whether treatments stop and what care each patient needs. Your part is to keep the evidence. Do not discard anything that may help find the cause: keep the concentrate containers, note the lot numbers, and leave the machines as they are unless the nurse directs otherwise.</p>
{{key:Say the pattern out loud: &ldquo;Station 4 and Station 7 both have chills, and both started at 6:10.&rdquo; One sentence that links two patients can protect everyone else on the shift.}}
"""),
(4, "failedtest", "A failed test: example", "Worked scenario: a failed chlorine test at shift start", """
<p>Section 4 gives the rule: hold, notify, and wait for release. This fictional example puts numbers and words on that rule. Many systems have two carbon tanks in a row. The first does most of the work, and the second is the backup, like a second lock on a door. The exact response belongs to your unit&rsquo;s written procedure; what follows is a common pattern.</p>
<div class="table-wrap"><table>
<thead><tr><th>Time</th><th>What happens</th><th>What it means</th></tr></thead>
<tbody>
<tr><td>05:10</td><td>The water system is started</td><td>The 15-minute run begins</td></tr>
<tr><td>05:30</td><td>Total chlorine after the first carbon tank reads 0.3 mg/L. The limit is 0.1 mg/L</td><td>Three times the limit. The first tank is letting chlorine through</td></tr>
<tr><td>05:32</td><td>The technician tells the charge nurse and asks that no patient be connected</td><td>The hold starts now, before any further testing</td></tr>
<tr><td>05:35</td><td>As the procedure directs, the test is repeated with a fresh sample, and a sample is taken after the second tank. Results: first tank 0.3 mg/L again; second tank below 0.1 mg/L</td><td>The reading is real, and the backup tank is still protecting the water</td></tr>
<tr><td>05:40</td><td>The technician reports to the water technician and the charge nurse</td><td>The people with authority decide</td></tr>
</tbody></table></div>
{{cards:The report, word for word|Situation::&ldquo;Total chlorine after the first carbon tank is 0.3 milligrams per liter at 05:30. Our limit is 0.1.&rdquo;|Confirmation::&ldquo;I repeated it at 05:35 with a fresh sample and it is again 0.3. After the second tank it reads below 0.1.&rdquo;|Status::&ldquo;The system ran 15 minutes before sampling. No patient is connected. I have asked the charge nurse to hold all starts.&rdquo;|Request::&ldquo;Please tell me whether we may start, and what testing you want during the shift. I will record your decision and the time.&rdquo;}}
<p>Notice what the report contains: the number and the limit, proof that the number is real, the state of the unit, and a clear request. In many procedures, a result within the limit after the second tank allows treatment to go ahead with more frequent testing while the first tank is serviced. That decision belongs to the person your unit authorizes, not to the technician who ran the test.</p>
<p><strong>If the second tank had also read above 0.1 mg/L:</strong> no treatment starts on that water, the hold continues, and the unit follows its contingency plan. If patients were already on treatment when a high result was found, the technician tells the nurse at once, and the nurse acts for the patients.</p>
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
