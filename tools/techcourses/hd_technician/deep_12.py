# -*- coding: utf-8 -*-
"""Hemodialysis Technician track, Module 12 (Integrated Practice and Competency Assessment): added lessons.
Merged into the Markdown-sourced module by generate_tech_courses.py."""

ADD = {
"extra": [
(1, "walkthrough", "Opening walk-through", "Opening the shift: one walk-through, in order", """
{{plain:Earlier modules taught each check separately. On a real morning they happen in one pass, in an order that puts the slowest and most far-reaching checks first. Water comes first because a water problem stops every station. The patient comes last because nothing patient-specific should be touched until the station behind it is ready.}}
<div class="table-wrap"><table>
<thead><tr><th>Order</th><th>Area</th><th>What you confirm</th><th>Taught in</th><th>If it fails, you hold</th></tr></thead>
<tbody>
<tr><td>1</td><td>Handoff and logs</td><td>Anything on hold from the last shift; machines tagged out; notes left for you</td><td>Module 1</td><td>The item named, until its owner releases it</td></tr>
<tr><td>2</td><td>Water room</td><td>System running; gauges and readings in their logged ranges; no leaks or alarms; softener salt present</td><td>Module 7</td><td>All new starts on that system</td></tr>
<tr><td>3</td><td>Chlorine test</td><td>Total chlorine at the assigned sample point, with the correct reagent or strip in date; result, units, time, and your name written at once</td><td>Module 7</td><td>All new starts on that system</td></tr>
<tr><td>4</td><td>Concentrates</td><td>Acid and bicarbonate match the orders; labels, expiry, and mixing time checked</td><td>Modules 4 and 7</td><td>The stations fed by that container or batch</td></tr>
<tr><td>5</td><td>Emergency equipment</td><td>Cart, defibrillator, oxygen, and suction checked and signed; emergency packs at stations</td><td>Module 10</td><td>Nothing starts until the charge nurse knows</td></tr>
<tr><td>6</td><td>Each machine</td><td>Last disinfection recorded; self-test passed; conductivity and temperature stable; residual disinfectant test negative</td><td>Module 6</td><td>That machine, tagged</td></tr>
<tr><td>7</td><td>Each station</td><td>Surfaces disinfected and dry; clean supplies only; sharps container not overfilled; correct machine for the patient&rsquo;s hepatitis status</td><td>Module 5</td><td>That station</td></tr>
<tr><td>8</td><td>Circuit</td><td>Dialyzer and lines match the order; primed with no air; a reprocessed dialyzer identified by two people and tested for germicide</td><td>Modules 6 and 11</td><td>That setup</td></tr>
<tr><td>9</td><td>Patient</td><td>Two identifiers against today&rsquo;s order; weight, blood pressure, and temperature as assigned; &ldquo;Any change since last time?&rdquo;</td><td>Modules 1 and 9</td><td>Patient-specific work, until the nurse decides</td></tr>
<tr><td>10</td><td>Access</td><td>Access check as authorized; arm washed; nothing tight on it</td><td>Module 8</td><td>Use of that access</td></tr>
<tr><td>11</td><td>Records</td><td>Every check above has an entry with a time and a name; nothing written ahead of time</td><td>Modules 1 and 9</td><td>Your own signature, until it is true</td></tr>
</tbody></table></div>
{{key:The order protects you from the most common opening error: a fully prepared station that sits on water nobody has tested yet.}}
{{stop:A check that was not recorded is treated as not done. If you find a blank from the previous shift, report it. Do not fill it in for them.}}
"""),
(2, "timelines", "Three timed scenarios", "Three scenarios, minute by minute", """
<p>Each table follows one event from the first sign to the record. Read the middle column as the standard you will be assessed against, and the right column as the shortcut that feels reasonable at the time.</p>
<p><strong>Scenario 1. A failed chlorine test with patients arriving.</strong> The unit&rsquo;s limit for total chlorine is 0.1 milligram per liter (mg/L), the maximum in the standard most units follow.[[iso23500_3]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Time</th><th>Event</th><th>What a competent technician does</th><th>Common mistake</th></tr></thead>
<tbody>
<tr><td>05:40</td><td>Test at the assigned sample point reads 0.3 mg/L</td><td>Writes 0.3 mg/L, the time, and the sample point in the log immediately</td><td>Repeating the test until one passes and writing only that one</td></tr>
<tr><td>05:41</td><td>The reverse osmosis display looks normal</td><td>Knows the display does not measure chlorine. The hold stands</td><td>Deciding the strip must be wrong</td></tr>
<tr><td>05:42</td><td>Two machines are already in self-test</td><td>Tells the charge nurse and the water lead: result, point, time, and &ldquo;no patient is connected&rdquo;</td><td>Telling only a coworker</td></tr>
<tr><td>05:50</td><td>First patients are at the door</td><td>Tells them, &ldquo;We are finishing a safety check on the water. The nurse will update you.&rdquo;</td><td>Seating patients and priming &ldquo;to save time&rdquo;</td></tr>
<tr><td>06:05</td><td>The water lead takes corrective action and asks for further samples</td><td>Tests where asked and records every result, pass or fail</td><td>Recording only the final passing result</td></tr>
<tr><td>06:25</td><td>The designated person signs the release</td><td>Starts setup only after seeing the release entry</td><td>Starting on a verbal &ldquo;should be fine now&rdquo;</td></tr>
</tbody></table></div>
<p><strong>Scenario 2. A pre-weight far above usual.</strong> Mrs. Reyes&rsquo;s target weight is 58.0 kilograms (kg). She usually arrives about 2.5 kg above it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Time</th><th>Event</th><th>What a competent technician does</th><th>Common mistake</th></tr></thead>
<tbody>
<tr><td>10:02</td><td>The scale reads 64.2 kg</td><td>Confirms the scale read zero before she stepped on. Notices her jacket and shoulder bag</td><td>Writing 64.2 and moving on</td></tr>
<tr><td>10:03</td><td>Re-weighed without jacket, bag, or shoes: 63.4 kg</td><td>Records 63.4 kg as the pre-weight and notes that the first reading included a jacket and bag</td><td>Averaging the two readings</td></tr>
<tr><td>10:04</td><td>She says her ankles are swollen and she slept sitting up</td><td>Asks nothing leading. Notes her exact words and that she is breathing faster than usual</td><td>Telling her off about fluids</td></tr>
<tr><td>10:05</td><td>Station 3 is ready</td><td>Reports to the nurse before she is seated for setup: weight, gain, her words, what was seen</td><td>Entering a fluid removal goal from the arithmetic</td></tr>
<tr><td>10:10</td><td>The nurse assesses and calls the nephrologist</td><td>Takes blood pressure as assigned and stays within reach</td><td>Suggesting to the patient how much will be removed</td></tr>
</tbody></table></div>
{{formula:<strong>Gain above target weight</strong> = pre-weight &minus; target weight<br>Example: 63.4 kg &minus; 58.0 kg = 5.4 kg, which is about 5,400 mL of fluid. Her usual gain is about 2.5 kg, so today is more than double. You report this number; the nurse and nephrologist decide how much is removed and how fast.}}
<p><strong>Scenario 3. A venous pressure alarm with a wet sheet.</strong></p>
<div class="table-wrap"><table>
<thead><tr><th>Time</th><th>Event</th><th>What a competent technician does</th><th>Common mistake</th></tr></thead>
<tbody>
<tr><td>14:31:00</td><td>Low venous pressure alarm at Station 7. The patient is dozing under a blanket</td><td>Walks to the patient, not to the screen. Lifts the blanket</td><td>Pressing reset from the side of the machine</td></tr>
<tr><td>14:31:10</td><td>The sheet under the arm is wet and red. The venous needle is half out</td><td>Shouts, &ldquo;Nurse to Station 7, needle out, bleeding.&rdquo; Gloves on</td><td>Going to find the nurse quietly</td></tr>
<tr><td>14:31:20</td><td>The nurse arrives within seconds</td><td>Follows the unit&rsquo;s emergency procedure within training and does exactly what the nurse says. Hands over gauze and clamps</td><td>Pushing the needle back in</td></tr>
<tr><td>14:33</td><td>Bleeding is controlled. The patient is awake and pale</td><td>Takes blood pressure as directed. Notes the time and the size of the stain</td><td>Stripping the bed before anyone has judged the blood loss</td></tr>
<tr><td>14:45</td><td>The patient is stable</td><td>Writes times, what was seen, who was called, and what was done. Completes the incident report as the unit requires</td><td>Writing &ldquo;needle slipped, resolved&rdquo;</td></tr>
</tbody></table></div>
{{key:In all three scenarios the competent technician does the same four things: looks for themselves, writes the real number, tells the right person early, and waits for the person who owns the decision.}}
"""),
(4, "selfrate", "Rate yourself", "Rate yourself before the assessor does", """
<p>The five stations are scored on what the assessor sees you do. Knowing how the scoring works removes surprises.</p>
{{cards:How the practical stations are scored|Three ratings::Each criterion is marked satisfactory, needs practice, or not observed.|All or nothing per station::A station is passed only when every one of its criteria is satisfactory. Two out of three is not a pass.|Critical steps::Each station has at least one critical step. Missing it stops the simulation.|No averaging::A strong station does not make up for a weak one.|Retest::After feedback and practice, you repeat the station with a different scenario, so memorizing the first one does not help.|Say it aloud::The assessor can score only what is seen or heard. Speak your checks as you do them.}}
<p>Use the grid below a week before the assessment. Rate each skill honestly, then ask your preceptor to rate you on the same grid and compare.</p>
<div class="table-wrap"><table>
<thead><tr><th>Level</th><th>Name</th><th>What it looks like</th></tr></thead>
<tbody>
<tr><td>1</td><td>Needs supervision</td><td>Someone must stand beside you and correct steps</td></tr>
<tr><td>2</td><td>Performs with prompts</td><td>You complete it, but need a reminder for a step or for the order</td></tr>
<tr><td>3</td><td>Performs independently</td><td>Correct, complete, in order, without prompts, and you can say why each step is there</td></tr>
<tr><td>4</td><td>Can teach others</td><td>Level 3, and you can explain it and spot errors when a newer trainee does it</td></tr>
</tbody></table></div>
<div class="table-wrap"><table>
<thead><tr><th>Core competency</th><th>Module</th><th>My level</th><th>Preceptor&rsquo;s level</th></tr></thead>
<tbody>
<tr><td>Two-identifier check against today&rsquo;s order</td><td>1</td><td>___</td><td>___</td></tr>
<tr><td>Hand hygiene, glove changes, and station turnover with full contact time</td><td>5</td><td>___</td><td>___</td></tr>
<tr><td>Machine setup, priming, and pre-treatment checks</td><td>6</td><td>___</td><td>___</td></tr>
<tr><td>Total chlorine test, water log, and placing a hold</td><td>7</td><td>___</td><td>___</td></tr>
<tr><td>Concentrate check against the order</td><td>7</td><td>___</td><td>___</td></tr>
<tr><td>Access observation and protection, as authorized</td><td>8</td><td>___</td><td>___</td></tr>
<tr><td>Weight, vital signs, rounds, and charting at the time</td><td>9</td><td>___</td><td>___</td></tr>
<tr><td>Alarm response: patient, access, lines, screen</td><td>9</td><td>___</td><td>___</td></tr>
<tr><td>Emergency call, assigned role, and time log</td><td>10</td><td>___</td><td>___</td></tr>
<tr><td>Dialyzer reprocessing steps and tests, if the unit reuses</td><td>11</td><td>___</td><td>___</td></tr>
<tr><td>Factual report with a clear request and check-back</td><td>All</td><td>___</td><td>___</td></tr>
</tbody></table></div>
{{key:Level 3 on every row is the target for sign-off. Where you and your preceptor disagree by a level or more, ask to be watched doing that task. The gap is usually a step you do not know you are skipping.}}
"""),
(6, "examprep", "Exam study plan", "Studying for the cumulative examination", """
<p>The written examination samples every module in the proportions of the blueprint. Divide your study time the same way, then move extra hours toward your weakest area.</p>
{{formula:<strong>Hours for an area</strong> = total study hours &times; (questions in that area &divide; 100)<br>Example with 20 hours: Modules 1 to 3, 20 questions, 4 hours. Module 4, 15 questions, 3 hours. Module 5, 15 questions, 3 hours. Modules 6 and 7, 20 questions, 4 hours. Modules 8 to 10, 20 questions, 4 hours. Modules 11 and 12, 10 questions, 2 hours. Check: 4 + 3 + 3 + 4 + 4 + 2 = 20 hours.<br><strong>Target</strong>: 80% of 100 questions = 80 correct, so no more than 20 may be missed.}}
{{flow:A study method that works for this examination|Retake the self-assessments::All twelve, closed book. Mark every miss and every lucky guess.|Sort your misses::Did not know the fact, misread the question, or chose a tempting unsafe action.|Rebuild from the tables::Cover the right-hand columns of the troubleshooting tables and say them from memory.|Redo every calculation::Fluid gain, removal rate, percentages, and dilution, each on paper with units.|Explain aloud::Teach one topic to a coworker in two minutes. Gaps show up fast.|Rest::Sleep before the examination does more than a last late night of reading.}}
<div class="table-wrap"><table>
<thead><tr><th>Question pattern</th><th>How to approach it</th></tr></thead>
<tbody>
<tr><td>&ldquo;What should the technician do first?&rdquo;</td><td>Look for patient safety and calling the nurse before measuring, charting, or fixing</td></tr>
<tr><td>An option where the technician changes a setting, gives something, or decides the cause</td><td>Almost always outside scope, so almost always wrong</td></tr>
<tr><td>An option that resets, repeats a test until it passes, or waits for handoff</td><td>The tempting shortcut; rarely the answer</td></tr>
<tr><td>A calculation</td><td>Write the units on every line. Check that the answer is a sensible size</td></tr>
<tr><td>Two answers both look right</td><td>Choose the one that happens earlier in time or reaches the person who owns the decision</td></tr>
</tbody></table></div>
"""),
(6, "ninetydays", "Your first 90 days", "After sign-off: the first 90 days and staying competent", """
<p>Sign-off means you were observed doing each skill correctly. It does not mean you have met every situation. The first three months turn checked skills into steady habits. The plan below is a model to agree with your supervisor, who sets the actual targets.</p>
<div class="table-wrap"><table>
<thead><tr><th>By day</th><th>Consolidate</th><th>Evidence in your logbook</th><th>Review with</th></tr></thead>
<tbody>
<tr><td>30</td><td>The routine: opening walk-through, setup and priming, turnover, and charting, done correctly without prompts on the machine model you were signed off on</td><td>Opening checks completed on your own; no blank entries; any hold you placed and how it was released</td><td>Preceptor: one observed opening and one observed turnover</td></tr>
<tr><td>60</td><td>The exceptions: alarms, failed tests, unusual weights, access changes. Speed comes after accuracy</td><td>At least a few entries of the form &ldquo;what I saw, whom I told, what happened next&rdquo;; one near-miss report if one occurred</td><td>Charge nurse: feedback on the quality of your reports</td></tr>
<tr><td>90</td><td>The wider unit: a second machine model if the unit has one, the water room routine, an emergency drill in an assigned role</td><td>Additional sign-offs; drill attendance; one improvement you suggested</td><td>Supervisor: review of the self-rating grid and goals for the next year</td></tr>
</tbody></table></div>
{{cards:Staying competent after the first year|Regular reassessment::Units recheck core skills at intervals they set, commonly once a year, and whenever a new machine, dialyzer, or procedure arrives.|Incident learning::Read the unit&rsquo;s incident and near-miss summaries. Ask what changed afterward.|Drills::Take a different role each time: caller, runner, recorder.|Logbook::Keep it going after training. Date, task, machine model, anything unusual, and who verified it.|Certificates::Keep basic life support current, and know the expiry date of every certificate you hold.|Questions::An experienced technician still asks. &ldquo;I have not done this on this model&rdquo; is a professional statement.}}
{{key:Competence belongs to a task, a machine model, and a date. If any of the three changes, ask to be checked again before you work alone.}}
"""),
],
"quiz_extra": [
("In the opening walk-through, why are the water room and chlorine test done before stations are set up?",
 ["Water checks are the quickest", "A water problem stops every station, so finding it first avoids preparing stations that cannot be used", "The water log must be signed before the nurse arrives", "Machines cannot be switched on until the test is recorded"], 1,
 "Checks with the widest effect come first."),
("The total chlorine test reads 0.3 mg/L against a limit of 0.1 mg/L. A repeat test reads lower. What do you record?",
 ["Only the lower result", "The average of the two", "Nothing until the water lead arrives", "Both results with times and sample point, and the hold stays until the designated person releases it"], 3,
 "Every result is recorded, and a better second test does not cancel a failed first one."),
("A patient&rsquo;s target weight is 58.0 kg and the confirmed pre-weight is 63.4 kg. What is the gain above target weight?",
 ["5.4 kg", "4.6 kg", "6.2 kg", "5.0 kg"], 0,
 "63.4 minus 58.0 equals 5.4 kg, about 5,400 mL."),
("A low venous pressure alarm sounds and the patient is dozing under a blanket. What is your first move?",
 ["Reset the alarm and watch the pressure", "Check the alarm history", "Go to the patient and lift the blanket to see the access and lines", "Call the biomedical technician"], 2,
 "A fall in venous pressure can mean a dislodged needle bleeding out of sight."),
("At a practical station you perform two of three criteria satisfactorily and miss the third. What is the station result?",
 ["Passed, because most criteria were met", "Passed if another station was strong", "Recorded as not observed", "Not yet satisfactory; you practice and retest on a different scenario"], 3,
 "A station is satisfactory only when every criterion is, and stations are not averaged."),
("On the self-rating grid, which description matches &ldquo;performs independently&rdquo;?",
 ["Completes the task with one reminder", "Correct, complete, and in order without prompts, and can say why each step is there", "Needs a preceptor beside them", "Has watched the task several times"], 1,
 "Independence means no prompts and an understanding of the purpose of each step."),
("You were signed off on one machine model and the unit installs a different model. What should you do?",
 ["Ask to be trained and checked on the new model before working on it alone", "Use it, since the stages are the same", "Wait until the annual reassessment", "Ask a coworker to set it up and sign for it yourself"], 0,
 "Competence is specific to the task and the machine model."),
],
"skills_extra": [
("Completes the full opening walk-through in the taught order on the training unit, records each check as it is done, and places a hold on a planted failure.", True),
("Works through a timed scenario card aloud, stating at each time point the action, the person to be told, and the record to be made.", False),
("Completes the self-rating grid, compares it with the preceptor&rsquo;s ratings, and writes one practice goal for each row below level 3.", False),
],
}
