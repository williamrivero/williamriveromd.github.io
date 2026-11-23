# -*- coding: utf-8 -*-
"""Hemodialysis Technician track, Module 04 (Principles of Hemodialysis): deeper lessons.
The prescription line by line, fluid removal arithmetic, what changes clearance at the chair,
and adequacy sampling and targets."""

ADD = {
"extra": [
(2, "rxlines", "The prescription", "Reading the dialysis prescription line by line", """
{{plain:The prescription is the nephrologist&rsquo;s written order for one patient&rsquo;s treatment. Every line is a setting or a supply that you will touch during setup. Your job is to make the station match the order exactly, and to speak up when it does not.}}
{{fig:hd_params|The parts of a hemodialysis prescription. Each part appears as one line in the table below.}}
<div class="table-wrap"><table>
<thead><tr><th>Line</th><th>What it is</th><th>Common adult values</th><th>What the technician checks</th></tr></thead>
<tbody>
<tr><td>Dialyzer</td><td>The filter: its model, membrane surface area, and whether it is low-flux or high-flux (flux means how easily water and larger molecules pass)</td><td>Varies by patient size and unit stock</td><td>The model on the package matches the order. Package intact, in date. A reprocessed dialyzer carries this patient&rsquo;s name</td></tr>
<tr><td>Treatment time</td><td>Minutes of actual dialysis, not minutes in the chair</td><td>Commonly 4 hours, three times a week</td><td>The time set on the machine equals the order. Start and end times are recorded</td></tr>
<tr><td>Blood flow rate</td><td>How fast the blood pump moves blood through the dialyzer</td><td>Commonly 250 to 400 mL per minute, depending on the access</td><td>The pump setting equals the order, and the arterial pressure allows it (Module 9)</td></tr>
<tr><td>Dialysate flow rate</td><td>How fast fresh dialysate passes the fibers</td><td>Commonly 500 mL per minute; some orders use up to 800</td><td>The machine setting equals the order</td></tr>
<tr><td>Dialysate composition</td><td>Sodium, potassium, calcium, and bicarbonate levels, set by the concentrates and the machine</td><td>Commonly sodium 135 to 140, potassium 2 to 3, bicarbonate 30 to 38 (all in mEq/L), calcium 2.5 to 3.0 mEq/L</td><td>Acid and bicarbonate labels match the order. Conductivity is stable and in range</td></tr>
<tr><td>Dialysate temperature</td><td>Warmth of the dialysate reaching the dialyzer</td><td>Commonly 36 to 37&deg;C; some orders are slightly cooler</td><td>The displayed temperature equals the order and is stable</td></tr>
<tr><td>Fluid removal goal</td><td>The ultrafiltration volume for this session</td><td>Different every session</td><td>Today&rsquo;s weight was measured correctly. The goal entered is the one the nurse confirmed</td></tr>
<tr><td>Anticoagulation</td><td>Medicine, usually heparin, that keeps blood from clotting in the circuit</td><td>Set per patient; some patients receive none</td><td>Nothing is prepared or given by the technician. Watch the circuit for clotting and report it</td></tr>
<tr><td>Access and needles</td><td>Which access is used and the needle size</td><td>Per patient</td><td>The correct supplies are at the station for the nurse</td></tr>
</tbody></table></div>
<p>These values are typical figures from standard teaching texts, not targets.[[mei7]] The order in front of you is the only correct value for that patient.</p>
{{cards:Who may change a line|Nephrologist::Writes and changes the prescription.|Nurse::Carries out the order, confirms the fluid goal for the session, gives medication, and adjusts settings within the unit&rsquo;s protocols.|Technician::Sets up to match the order, checks, observes, records, and reports. Changes a setting only when unit policy allows it and the nurse directs it.}}
{{stop:If any line is missing, unreadable, or different from what is on the machine or the supplies, do not choose the value that looks usual. Hold the setup and ask the nurse.}}
"""),
(3, "ufmath", "Fluid removal math", "Fluid removal arithmetic, with worked examples", """
<p>Section 3 separated weight gain, target weight, and the prescribed goal. This lesson shows how the goal is usually built, so that you can check the arithmetic and notice an entry that cannot be right. The nurse confirms the final number.</p>
{{formula:<strong>Weight to lose (kg)</strong> = pre-dialysis weight &minus; target weight<br><strong>Total ultrafiltration volume (mL)</strong> = weight to lose &times; 1,000 + fluids given or taken during treatment, as your unit counts them<br><strong>Hourly rate (mL per hour)</strong> = total volume &divide; treatment hours<br><strong>Rate for body size (mL per kg per hour)</strong> = hourly rate &divide; weight in kg}}
<p>One kilogram of fluid is treated as 1 liter, or 1,000 mL. Fluids that enter the patient during the session add to what must come off. These include the saline used to return the blood at the end (rinse-back), any priming saline that goes to the patient, saline given during treatment, and drinks. Units count these differently, and some machines add them automatically. Learn your unit&rsquo;s method and use only that one.</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Example A: fictional Mrs. Santos</th><th>Result</th></tr></thead>
<tbody>
<tr><td>Weight to lose</td><td>68.5 kg &minus; 66.0 kg</td><td>2.5 kg = 2,500 mL</td></tr>
<tr><td>Add fluids in</td><td>Rinse-back and prime counted by this unit as 300 mL, plus a 200 mL drink</td><td>2,500 + 500 = 3,000 mL</td></tr>
<tr><td>Hourly rate</td><td>3,000 mL &divide; 4 hours</td><td>750 mL per hour</td></tr>
<tr><td>Rate for body size</td><td>750 &divide; 66 kg</td><td>About 11.4 mL per kg per hour</td></tr>
</tbody></table></div>
<p>The weight used in the last step is the one your unit&rsquo;s protocol names, commonly the target weight.</p>
<div class="table-wrap"><table>
<thead><tr><th>Example B: same volume, different patients</th><th>50 kg patient</th><th>80 kg patient</th></tr></thead>
<tbody>
<tr><td>Total volume and time</td><td>3,200 mL in 4 hours</td><td>3,200 mL in 4 hours</td></tr>
<tr><td>Hourly rate</td><td>800 mL per hour</td><td>800 mL per hour</td></tr>
<tr><td>Rate for body size</td><td>800 &divide; 50 = 16 mL per kg per hour</td><td>800 &divide; 80 = 10 mL per kg per hour</td></tr>
</tbody></table></div>
{{plain:The same 800 mL per hour is a much heavier load for the smaller patient. Fluid is taken from the blood, and the blood refills from the tissues only so fast. When removal outruns refilling, blood pressure falls and cramps begin.}}
<p>For this reason many units ask staff to report a rate above a set figure before treatment starts. A commonly used figure is about 10 to 13 mL per kg per hour; your unit&rsquo;s protocol gives the one that applies. The nurse and nephrologist decide what to do, for example a longer session or a smaller goal.</p>
<div class="table-wrap"><table>
<thead><tr><th>Entry that should make you stop</th><th>Likely cause</th></tr></thead>
<tbody>
<tr><td>Pre-weight lower than target weight</td><td>Wrong patient record, scale error, or a real weight loss the nurse must assess</td></tr>
<tr><td>Gain of 6 kg in two days</td><td>Patient weighed with shoes, bag, or wheelchair; kg and pounds mixed up; or a real and dangerous gain</td></tr>
<tr><td>Goal of 250 mL where 2,500 mL was expected</td><td>A missing zero or a misplaced decimal</td></tr>
<tr><td>Time shortened but goal unchanged</td><td>The hourly rate has risen without anyone deciding it should</td></tr>
</tbody></table></div>
{{key:If a patient arrives late and the session is cut from 4 hours to 3, a 3,000 mL goal rises from 750 to 1,000 mL per hour. Tell the nurse before the machine is set, not after.}}
"""),
(4, "chairclear", "Clearance at the chair", "What changes clearance at the chair", """
<p>Clearance is the volume of blood completely cleaned of a waste in one minute. The prescription assumes a clearance that is only delivered if the session runs as written. Most losses are ordinary, and a technician is often the first person able to see them.</p>
{{fig:kidney_vs_dialyzer|A dialyzer cleans more blood at a higher blood flow, but only while it runs. Flow and time are the two things the chairside team can protect.}}
<div class="table-wrap"><table>
<thead><tr><th>Cause</th><th>Effect</th><th>What you can observe</th></tr></thead>
<tbody>
<tr><td>Blood flow run below the order</td><td>Less blood passes the membrane each minute</td><td>Pump setting lower than the order; a very negative arterial pressure, which means the pump is delivering less than it displays</td></tr>
<tr><td>Time not fully delivered</td><td>Less total cleaning; larger molecules suffer most</td><td>Late start, long alarm stops, patient asks to come off early</td></tr>
<tr><td>Clotted fibers</td><td>Less working membrane</td><td>Dark streaks in the dialyzer, dark blood in the chambers, rising venous or transmembrane pressure</td></tr>
<tr><td>Access recirculation: cleaned blood is drawn straight back into the arterial needle</td><td>The dialyzer re-cleans the same blood</td><td>Needles close together or lines reversed; a narrowed access; results that fall with no other explanation</td></tr>
<tr><td>Air-locked fibers from poor priming</td><td>Less working membrane</td><td>Pale streaks at the start of treatment</td></tr>
<tr><td>Dialysate flow or concentrate problem</td><td>Weaker gradient; time in bypass does not count as dialysis</td><td>Repeated conductivity or flow alarms; wrong dialysate flow setting</td></tr>
<tr><td>Wrong dialyzer</td><td>Smaller surface than ordered</td><td>Package does not match the order</td></tr>
</tbody></table></div>
<p><strong>Liters processed</strong> is a useful chairside figure. It is the blood flow multiplied by the minutes the pump actually ran, and most machines display it.</p>
{{formula:<strong>Liters processed</strong> = blood flow (mL per minute) &times; minutes run &divide; 1,000<br>As ordered: 300 &times; 240 = 72,000 mL = 72 liters<br>As delivered: 250 &times; 225 = 56,250 mL = about 56 liters, which is about 22 percent less}}
<p><strong>Minutes add up.</strong> A fictional patient starts 10 minutes late and signs off 5 minutes early at every session. That is 15 minutes lost each time. At 13 sessions in a month, 15 &times; 13 = 195 minutes, or 3 hours 15 minutes. He has missed most of one full treatment without missing a single appointment.</p>
<div class="table-wrap"><table>
<thead><tr><th>Where time is lost</th><th>What the technician can do</th></tr></thead>
<tbody>
<tr><td>Late starts</td><td>Have the machine tested, primed, and ready before the patient&rsquo;s scheduled time</td></tr>
<tr><td>Alarm stops</td><td>Respond at once and call the nurse early. Record how long the pump was stopped</td></tr>
<tr><td>Early sign-off</td><td>Tell the nurse as soon as the patient asks. Never agree to it yourself; the nurse explains the risk and documents the request</td></tr>
<tr><td>Clock errors</td><td>Record actual start and end times, not the scheduled ones</td></tr>
</tbody></table></div>
{{key:Record what was delivered, not what was ordered. A chart that always says 4 hours and 300 mL per minute hides the reason a patient&rsquo;s results are falling.}}
"""),
(4, "adequacy", "Samples and targets", "Adequacy samples and targets: why timing matters", """
<p>Drawing blood is the nurse&rsquo;s task. The technician often prepares tubes and labels, notes times, and may be asked to slow the pump on the nurse&rsquo;s instruction. Knowing why each step exists helps you assist correctly and notice a sample that will mislead.</p>
<div class="table-wrap"><table>
<thead><tr><th>Sample</th><th>When and how it is drawn</th><th>What goes wrong</th><th>How the result is misleading</th></tr></thead>
<tbody>
<tr><td>Pre-dialysis</td><td>Before treatment starts, and before saline or heparin can mix with it</td><td>Sample diluted with saline from a primed needle line or a catheter; drawn after dialysis has begun</td><td>BUN reads lower than it really is, so the session looks less effective</td></tr>
<tr><td>Post-dialysis</td><td>At the end of the full treatment, by a slow-flow method: fluid removal is stopped, the blood pump is slowed (commonly to about 100 mL per minute for about 15 seconds), and the sample is taken from the arterial port</td><td>Drawn at full blood flow, so cleaned blood recirculating through the access is in the sample</td><td>BUN reads too low, so the session looks better than it was</td></tr>
<tr><td>Post-dialysis</td><td>As above</td><td>Drawn many minutes after the pump stopped. Urea moves back into the blood from the tissues, called rebound</td><td>BUN reads higher; results cannot be compared with last month</td></tr>
<tr><td>Either</td><td>Both from the same session, labeled at the chair</td><td>Tubes mislabeled or swapped</td><td>The result is meaningless or belongs to another patient</td></tr>
</tbody></table></div>
<p>The slow-flow step exists to clear recirculated blood from the arterial line while leaving too little time for rebound. The speed and seconds are set in your unit&rsquo;s procedure; the nurse gives the instruction.</p>
{{plain:Kt/V compares how much blood was cleaned (clearance multiplied by time) with the size of the patient&rsquo;s body water. A Kt/V of 1.2 means the volume cleaned was 1.2 times the patient&rsquo;s body water. A bigger patient needs more cleaning to reach the same number.}}
<div class="table-wrap"><table>
<thead><tr><th>Measure</th><th>Commonly cited guideline minimum, three sessions a week</th><th>Notes</th></tr></thead>
<tbody>
<tr><td>Urea reduction ratio (URR)</td><td>65 percent or more</td><td>Simple to calculate; ignores fluid removed and body size</td></tr>
<tr><td>Single-pool Kt/V</td><td>1.2 or more delivered at each session; many units aim for 1.4 so that the minimum is reliably met</td><td>Calculated by the laboratory, the machine, or software, not by hand</td></tr>
</tbody></table></div>
<p>These are minimums from standard guidelines and teaching texts, not goals to stop at, and the nephrologist sets the target for each patient.[[mei7]]</p>
<p><strong>Worked example.</strong> Pre-dialysis BUN 80 mg/dL, post-dialysis BUN 30 mg/dL. URR = (80 &minus; 30) &divide; 80 &times; 100 = 62.5 percent. This is below the 65 percent minimum. The nurse and nephrologist decide what it means, but they will ask questions the technician&rsquo;s records answer: Was the full time delivered? What was the actual blood flow? Was the dialyzer streaked? Were there long alarm stops?</p>
{{stop:Tell the nurse before the samples leave the unit if the post-dialysis sample was drawn without slowing the pump, the session ended early, or a tube is unlabeled. A wrong sample sent today becomes a wrong decision next month.}}
"""),
],
"quiz_extra": [
("A patient&rsquo;s pre-dialysis weight is 72.0 kg and the target weight is 70.0 kg. The unit counts 400 mL for rinse-back and drinks. The session is 4 hours. What is the hourly ultrafiltration rate?",
 ["500 mL per hour", "600 mL per hour", "800 mL per hour", "2,400 mL per hour"], 1,
 "2,000 mL plus 400 mL is 2,400 mL, and 2,400 divided by 4 hours is 600 mL per hour."),
("Two patients each have 3,200 mL to remove in 4 hours. One weighs 50 kg and the other 80 kg. Which statement is correct?",
 ["Both carry the same load because the hourly rate is the same", "The 80 kg patient has the higher rate per kg", "The rate per kg cannot be worked out", "The 50 kg patient has the higher rate per kg, 16 mL per kg per hour"], 3,
 "800 divided by 50 is 16 mL per kg per hour, against 10 for the 80 kg patient."),
("The order says blood flow 300 mL per minute, but the chart shows the pump ran at 250 all session. Who decides whether the prescription changes?",
 ["The nephrologist, after the nurse is told", "The technician, by recording 300", "The patient", "The machine"], 0,
 "The technician records what was delivered and reports it; the prescription belongs to the nephrologist."),
("A patient loses 15 minutes at each of 13 sessions in a month. How much treatment time is lost?",
 ["45 minutes", "1 hour 30 minutes", "3 hours 15 minutes", "13 hours"], 2,
 "15 times 13 is 195 minutes, which is 3 hours 15 minutes."),
("Why is the blood pump slowed briefly before the post-dialysis BUN sample is drawn?",
 ["To warm the sample", "To clear recirculated, already cleaned blood from the arterial line", "To add heparin to the sample", "To let urea rebound fully"], 1,
 "A sample containing recirculated blood has a falsely low BUN and makes the session look better than it was."),
("Pre-dialysis BUN is 80 mg/dL and post-dialysis BUN is 30 mg/dL. What is the URR, and how does it compare with the commonly cited minimum?",
 ["37.5 percent, above the minimum", "70 percent, above the minimum", "50 percent, below the minimum", "62.5 percent, below the 65 percent minimum"], 3,
 "(80 minus 30) divided by 80 is 62.5 percent."),
("A late patient&rsquo;s session is cut from 4 hours to 3, and the 3,000 mL goal is unchanged. What should the technician do?",
 ["Set the machine and say nothing", "Lower the goal to 2,250 mL", "Tell the nurse that the rate would rise from 750 to 1,000 mL per hour before the machine is set", "Raise the blood flow to make up the time"], 2,
 "The hourly rate has risen without a decision; the nurse must confirm the goal."),
],
"skills_extra": [
("Checks a mock setup against a mock prescription line by line and reports each mismatch to the preceptor before proceeding.", True),
("Calculates total ultrafiltration volume, hourly rate, and rate per kg per hour from a mock record using the unit&rsquo;s method, and states when the rate must be reported.", False),
("Records actual start time, end time, blood flow, and minutes of pump stoppage on a mock flow sheet.", False),
],
}
