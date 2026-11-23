# -*- coding: utf-8 -*-
"""Hemodialysis Technician track, Module 02: added lessons (kidney function loss at the chair, laboratory
values, fluid and weight arithmetic, accurate weight and vital signs)."""

ADD = {
"extra": [
(2, "atthechair", "Signs at the chair", "What each lost kidney function looks like at the chair", """
{{plain:Think of a house after the garbage collector stops coming. You never see the missing truck. You see what piles up at the gate, and you smell it before long. Kidney failure is like that. You will not see a failed kidney. You will see what its missing work leaves behind: extra water, extra potassium, extra acid, extra phosphate, too few red blood cells, and high blood pressure.}}
<p>The picture has a limit. Garbage at the gate is easy to see. Some of what builds up in a dialysis patient gives no sign at all until it is dangerous, and potassium is the clearest example. So you watch for what you can see, and you never take silence as safety. The table links each lost function to what you may notice and what to say.</p>
<div class="table-wrap"><table>
<thead><tr><th>Function lost</th><th>What builds up or runs short</th><th>What you may see or hear</th><th>What to tell the nurse</th></tr></thead>
<tbody>
<tr><td>Removing water and salt</td><td>Fluid in the blood vessels and tissues</td><td>A large weight gain. Swollen ankles, hands, or face. Tight shoes or rings. Breathlessness, worse lying flat. Higher blood pressure</td><td>Both weights and the gain. Report breathlessness at rest at once</td></tr>
<tr><td>Removing potassium</td><td>Potassium, a mineral that controls how muscle and heart cells fire</td><td>Often nothing at all. Sometimes weak or heavy legs, tingling, or a slow or irregular pulse. A missed session or a diet lapse makes it more likely</td><td>Weakness or an irregular pulse at once. Any missed session. Any flagged result</td></tr>
<tr><td>Removing acid</td><td>Acid; the blood&rsquo;s buffer, bicarbonate, runs low</td><td>Usually nothing. When severe, deep or fast breathing</td><td>Breathing that is faster or deeper than usual for this patient</td></tr>
<tr><td>Removing phosphate</td><td>Phosphate; over months it disturbs calcium and the bones</td><td>Itching and scratch marks. Bone or joint pain. A patient who says the phosphate binder tablets are skipped</td><td>The symptom, and what the patient said about the tablets</td></tr>
<tr><td>Making erythropoietin</td><td>Too few red blood cells (anemia)</td><td>Pale skin and inner eyelids. Tiredness. Breathlessness on effort. Feeling cold. Dizziness</td><td>New or worsening tiredness, breathlessness, or dizziness</td></tr>
<tr><td>Removing wastes</td><td>Urea and many other wastes (uremia)</td><td>Nausea, poor appetite, a metal taste, breath that smells of ammonia, itching, restless legs, drowsiness</td><td>New drowsiness or confusion at once. Other symptoms the same shift</td></tr>
<tr><td>Controlling blood pressure</td><td>Fluid, plus hormones that tighten the blood vessels</td><td>High readings before treatment. Headache</td><td>Any reading outside the limits your unit sets. Severe headache, chest pain, or a change in vision at once</td></tr>
</tbody></table></div>
{{key:Report the observation and the number, not the diagnosis. Say &ldquo;his pulse is irregular and he missed Saturday&rsquo;s session,&rdquo; not &ldquo;he has high potassium.&rdquo;}}
{{stop:Tell the nurse at once, before you finish any other task, if you see breathlessness at rest, chest pain, new confusion or drowsiness, sudden weakness, an irregular or very slow pulse, or a patient who simply looks much worse than usual.}}
"""),
(4, "labvalues", "Lab values", "Laboratory values on the chart: typical ranges and urgent results", """
<p>A reference range is the span of results a laboratory expects in healthy adults. The ranges below are typical values for teaching. Every laboratory prints its own range beside each result, and that printed range is the one you use. Many Philippine laboratories report in international units such as millimoles per liter; some use milligrams per deciliter. The same blood gives very different numbers in the two systems, so read the unit before you read the number.</p>
<p>The last column matters most at the chair. A dialysis patient is not a healthy adult, and several results sit outside the range every month by design or by the nature of the disease. Your work is not to interpret them. It is to notice the ones that are flagged, new, or different from last time, and to bring them to the nurse.</p>
<div class="table-wrap"><table>
<thead><tr><th>Test</th><th>What it tells the team</th><th>Typical adult reference range (laboratory-dependent)</th><th>What is usual in a hemodialysis patient</th></tr></thead>
<tbody>
<tr><td>Potassium</td><td>Risk to heart rhythm</td><td>3.5 to 5.0 mmol/L</td><td>Tends to be high before treatment. Too high and too low are both dangerous</td></tr>
<tr><td>Sodium</td><td>Balance of water and salt</td><td>135 to 145 mmol/L</td><td>Often near the low end when fluid intake is high</td></tr>
<tr><td>Bicarbonate, or total carbon dioxide</td><td>Acid buildup</td><td>About 22 to 29 mmol/L</td><td>Often low before treatment</td></tr>
<tr><td>Blood urea nitrogen (BUN)</td><td>A waste from protein</td><td>About 7 to 20 mg/dL (2.5 to 7.1 mmol/L)</td><td>High before treatment, lower after. The pair is used to measure adequacy (Module 4)</td></tr>
<tr><td>Creatinine</td><td>A waste from muscle</td><td>About 0.6 to 1.3 mg/dL (53 to 115 micromoles per liter)</td><td>Always well above the range. This is expected, not an emergency</td></tr>
<tr><td>Calcium, total</td><td>Bone and mineral balance</td><td>About 8.5 to 10.5 mg/dL (2.1 to 2.6 mmol/L)</td><td>Varies; the nephrologist sets the target</td></tr>
<tr><td>Phosphate</td><td>Bone and mineral balance</td><td>About 2.5 to 4.5 mg/dL (0.8 to 1.45 mmol/L)</td><td>Often high</td></tr>
<tr><td>Albumin</td><td>Protein stores and nutrition</td><td>About 3.5 to 5.0 g/dL (35 to 50 g/L)</td><td>Often low when the patient eats poorly or is ill</td></tr>
<tr><td>Hemoglobin</td><td>Oxygen-carrying protein in red cells</td><td>About 13.5 to 17.5 g/dL in men and 12.0 to 15.5 g/dL in women</td><td>Usually below the range. The nephrologist sets a lower target on purpose</td></tr>
<tr><td>Hepatitis B surface antigen, hepatitis C antibody</td><td>Infection status</td><td>Nonreactive</td><td>Decides machine and station assignment (Module 5)</td></tr>
</tbody></table></div>
{{cards:Reading any result safely|Right patient::Two identifiers on the report match the record.|Date and time::Is this today&rsquo;s result or last month&rsquo;s?|Before or after dialysis::A post-treatment potassium or BUN is expected to be lower.|Unit::The same result looks very different in mg/dL and in mmol/L.|Flag::High, low, or critical, as the laboratory marked it.|Trend::Compare it with the previous result, not only with the range.}}
<p>Some results cannot wait for the end of the shift. The reason is the same in each row: harm can arrive before the patient feels anything.</p>
<div class="table-wrap"><table>
<thead><tr><th>Tell the nurse at the same moment you see it</th><th>Why it cannot wait</th></tr></thead>
<tbody>
<tr><td>Any result the laboratory marks critical</td><td>The laboratory is saying that someone must act now</td></tr>
<tr><td>A potassium flagged high or low, even when the patient feels well</td><td>A dangerous potassium often gives no warning. Many laboratories treat about 6.0 mmol/L and above as critical; your laboratory&rsquo;s own limit applies</td></tr>
<tr><td>A hemoglobin flagged critically low, or much lower than the last result</td><td>It may mean bleeding</td></tr>
<tr><td>A hepatitis result newly reported as reactive</td><td>Station and machine assignment must be settled before the next setup[[cdc_dialysis]]</td></tr>
<tr><td>A result that seems to belong to another patient</td><td>Someone else may be missing a result</td></tr>
</tbody></table></div>
{{stop:If the laboratory telephones a result, hand the call to the nurse. Take it yourself only where your unit authorizes this; then write it down, read it back to the caller, and tell the nurse immediately. Never tell a patient what a result means. The nurse or the nephrologist does that.}}
"""),
(4, "weightmath", "Weight arithmetic", "Fluid and weight arithmetic, with worked examples", """
{{plain:Think of a rice sack on a market scale. Pour in one liter of water and the scale rises by about one kilogram; pour in 500 milliliters and it rises by about half a kilogram. A patient who makes little or no urine is like a sack with no hole in it. Almost everything he or she drinks stays in. That is why the weight change between treatments is read as fluid.}}
<p>The picture has a limit. A sack only gains. A person also eats, loses a little water through breath and sweat, and changes body tissue slowly over weeks. Over the two or three days between sessions, though, fluid is by far the largest part of the change, and that is the part the scale is used to measure.</p>
<p>Three weights matter. The <strong>pre-weight</strong> is measured on arrival. The <strong>post-weight</strong> is measured after treatment. The <strong>dry weight</strong> is the target post-treatment weight the nephrologist sets: the weight at which the patient carries no excess fluid and still feels well. Only the nephrologist changes it.</p>
{{formula:<strong>Interdialytic weight gain</strong> = today&rsquo;s pre-weight &minus; last post-weight.<br>Example: pre-weight 62.8 kg, last post-weight 60.5 kg. 62.8 &minus; 60.5 = 2.3 kg, or about 2.3 liters of fluid.}}
{{formula:<strong>Gain as a percent of dry weight</strong> = gain &divide; dry weight &times; 100.<br>Example: gain 2.3 kg, dry weight 60.0 kg. 2.3 &divide; 60.0 &times; 100 = 3.8 percent.}}
{{formula:<strong>Weight above dry weight</strong> = today&rsquo;s pre-weight &minus; dry weight.<br>Example: 62.8 &minus; 60.0 = 2.8 kg. This is larger than the gain of 2.3 kg because the patient left the last session 0.5 kg above dry weight.}}
<p><strong>Why the percent matters.</strong> The same gain is a heavier load for a smaller person. The table shows how far apart two patients with exactly the same gain can be.</p>
<div class="table-wrap"><table>
<thead><tr><th>Patient (fictional)</th><th>Dry weight</th><th>Gain</th><th>Calculation</th><th>Percent of dry weight</th></tr></thead>
<tbody>
<tr><td>Mrs. Lim</td><td>48.0 kg</td><td>2.9 kg</td><td>2.9 &divide; 48.0 &times; 100</td><td>6.0</td></tr>
<tr><td>Mr. Torres</td><td>80.0 kg</td><td>2.9 kg</td><td>2.9 &divide; 80.0 &times; 100</td><td>3.6</td></tr>
</tbody></table></div>
<p>Units commonly ask to be told when the gain passes a set percent of dry weight, often around 4 to 5 percent. Use the figure your unit sets. The nurse and the nephrologist decide how much fluid to remove. Your part is to supply numbers they can trust.</p>
{{formula:<strong>Patient weight on a wheelchair scale</strong> = total reading &minus; weight of the empty chair.<br>Example: total 86.4 kg, chair 18.2 kg. 86.4 &minus; 18.2 = 68.2 kg. Record that the patient was weighed in a chair, and weigh that chair itself, not a similar one.}}
{{formula:<strong>Weight lost in treatment</strong> = pre-weight &minus; post-weight.<br>Example: 62.8 &minus; 60.4 = 2.4 kg. Small differences from the fluid removal shown on the machine are expected, because of food, drink, and saline given during treatment. Report a difference larger than your unit accepts.}}
<p>Most weighing errors are small habits repeated. Each one below produces a number that looks real.</p>
<div class="table-wrap"><table>
<thead><tr><th>Weighing error</th><th>Effect</th><th>Prevention</th></tr></thead>
<tbody>
<tr><td>Scale not at zero, or standing on an uneven floor</td><td>Every weight on that shift is wrong</td><td>Check zero before the first patient and whenever the scale is moved</td></tr>
<tr><td>Shoes, jacket, bag, or phone on at one weighing and off at the other</td><td>A false gain or loss of up to a kilogram or more</td><td>Same clothing, shoes off, pockets empty, before and after</td></tr>
<tr><td>Patient holding a rail or a companion</td><td>A falsely low weight</td><td>Hands free once steady; use a chair scale for anyone unsteady</td></tr>
<tr><td>Digits swapped, such as 68.2 written as 62.8</td><td>A large false change</td><td>Say the number aloud, write it at the scale, and compare it with the last weight</td></tr>
<tr><td>Pre-weight entered in the post-weight space</td><td>The next gain is calculated from the wrong number</td><td>Read the column heading before you write</td></tr>
</tbody></table></div>
{{key:When a weight surprises you, weigh again before the patient sits down. Record what you found and tell the nurse both readings.}}
"""),
(4, "vitalsigns", "Accurate vital signs", "Measuring blood pressure, pulse, and temperature accurately", """
<p>The nurse acts on the numbers you record. A technique error does not produce a vague number. It produces a confident, wrong one, and nothing on the chart shows that it is wrong. That is why technique matters more than speed.</p>
<div class="table-wrap"><table>
<thead><tr><th>Measurement</th><th>Typical resting adult value</th><th>Note for dialysis</th></tr></thead>
<tbody>
<tr><td>Pulse</td><td>60 to 100 beats per minute</td><td>Report an irregular pulse even when the rate is in range</td></tr>
<tr><td>Breathing</td><td>12 to 20 breaths per minute</td><td>Count without telling the patient</td></tr>
<tr><td>Temperature</td><td>About 36.1 to 37.2&deg;C; fever is commonly defined as 38.0&deg;C or higher</td><td>Many dialysis patients run cooler than this. Report a rise above the patient&rsquo;s usual, and any chills, even below 38.0&deg;C</td></tr>
<tr><td>Blood pressure</td><td>Varies by person</td><td>Use the reporting limits your unit and the nephrologist set</td></tr>
</tbody></table></div>
{{flow:Blood pressure, step by step|Choose the arm::Never the arm with a fistula or graft. If neither arm can be used, ask the nurse.|Seat and rest::Back supported, feet flat, legs uncrossed, commonly five minutes of quiet rest.|Choose the cuff::The size marked for the patient&rsquo;s arm.|Place it::On bare skin, with the artery mark over the inner arm and the arm supported at heart level.|Measure::No talking, by the patient or by staff.|Record::The reading, the arm, the position, and the time.}}
<p>Each error in the next table pushes the reading in a predictable direction. Learn the direction, and you will know what a suspicious reading may be telling you about how it was taken.</p>
<div class="table-wrap"><table>
<thead><tr><th>Technique error</th><th>Effect on the reading</th></tr></thead>
<tbody>
<tr><td>Cuff too small for the arm</td><td>Falsely high</td></tr>
<tr><td>Cuff too large for the arm</td><td>Falsely low</td></tr>
<tr><td>Arm hanging below heart level, or unsupported</td><td>Falsely high</td></tr>
<tr><td>Arm raised above heart level</td><td>Falsely low</td></tr>
<tr><td>Patient talking, legs crossed, or just walked in</td><td>Falsely high</td></tr>
<tr><td>Cuff over a thick sleeve</td><td>Unreliable</td></tr>
<tr><td>Cuff on the access arm</td><td>May damage the access. Never done</td></tr>
<tr><td>Irregular pulse counted for 15 seconds and multiplied</td><td>Wrong rate. Count for a full minute</td></tr>
<tr><td>Pulse felt with your thumb</td><td>You may count your own pulse. Use two fingers</td></tr>
<tr><td>Oral temperature soon after a hot or cold drink</td><td>Falsely high or low. Wait the time your unit sets, commonly about 15 minutes</td></tr>
<tr><td>Infrared thermometer held at the wrong distance or on sweaty skin</td><td>Unreliable. Follow the device instructions</td></tr>
</tbody></table></div>
{{stop:Do not repeat a measurement until it looks acceptable and then record only the last one. If a reading is unexpected, check the patient, repeat it once with correct technique, record both readings, and tell the nurse.}}
"""),
],
"quiz_extra": [
("A patient&rsquo;s last post-weight was 71.5 kg. Today&rsquo;s pre-weight is 74.6 kg. What is the interdialytic weight gain?",
 ["2.1 kg", "3.1 kg", "3.6 kg", "4.1 kg"], 1,
 "74.6 minus 71.5 equals 3.1 kg, about 3.1 liters of fluid."),
("A patient with a dry weight of 75.0 kg has gained 3.0 kg. What is the gain as a percent of dry weight?",
 ["2.5 percent", "3.0 percent", "25 percent", "4.0 percent"], 3,
 "3.0 divided by 75.0, times 100, equals 4.0 percent."),
("A blood pressure cuff that is too small for the patient&rsquo;s arm gives a reading that is:",
 ["Falsely high", "Falsely low", "Accurate, but slower to appear", "Accurate if the arm is raised"], 0,
 "A cuff that is too small overestimates blood pressure; one that is too large underestimates it."),
("A patient in a wheelchair reads 92.6 kg on the platform scale. The empty wheelchair weighs 19.4 kg. What is the patient&rsquo;s weight?",
 ["72.2 kg", "74.2 kg", "73.2 kg", "112.0 kg"], 2,
 "92.6 minus 19.4 equals 73.2 kg."),
("A hepatitis B surface antigen result is newly reported as reactive for a patient due on the next shift. Why must the nurse know before setup?",
 ["The patient must be told by the technician", "Station and machine assignment must be decided first", "The dialyzer size changes", "The result changes the dry weight"], 1,
 "Infection status decides where and on which machine the patient is treated."),
("A patient&rsquo;s pulse feels irregular. How should the rate be counted?",
 ["For 15 seconds, multiplied by 4", "For 30 seconds, multiplied by 2", "For a full minute", "With the blood pressure machine only"], 2,
 "An irregular pulse is counted for a full minute and the irregularity is reported."),
("Why can a dangerously high potassium be missed at the chair?",
 ["It often causes no symptoms", "It always causes swelling first", "It only occurs after treatment", "It shows as a high temperature"], 0,
 "High potassium can be silent, which is why a flagged result is reported even when the patient feels well."),
],
"skills_extra": [
("Calculates interdialytic weight gain in kilograms and as a percent of dry weight from a mock record, stating both source weights.", True),
("Measures blood pressure on the non-access arm with the correct cuff size, the arm supported at heart level, after seated rest, and records arm and position.", True),
("Subtracts the empty wheelchair weight correctly and records how the patient was weighed.", False),
],
}
