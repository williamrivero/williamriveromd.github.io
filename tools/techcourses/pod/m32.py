# -*- coding: utf-8 -*-
"""Physician on Duty, Module 32: Putting It Together: Bedside Skills and a Simulated Shift.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A preceptor holding a clipboard scoring sheet watches a young physician examine a practice arm with a fistula pad at a dialysis station.",
    "objectives": [
        "Write orders and event notes that are clear, timed, within the attending nephrologist&rsquo;s prescription, and free of error-prone abbreviations.",
        "Hand off a patient to the attending nephrologist and to an emergency room physician using a structured format, with a written transfer letter.",
        "Perform the ten core bedside skills of the series to the standard on each station&rsquo;s scoring sheet, including every Critical step.",
        "Prioritize several simultaneous problems on one shift and explain the order you chose.",
        "Explain what simulation, deliberate practice, and debriefing add to reading, with the strength of the evidence.",
        "Complete the written test and the Competency Passport, and state what a passing score does and does not show.",
    ],
    "big": """
{{plain:Think of learning to swim. A good book can teach you the stroke, the breathing, and why you kick from the hip. You can pass a written test on all of it. Then you step into the pool, and your body does something else. The earlier modules were the book. This module is the pool.}}
<p>The picture has a limit. A swimmer faces one task in calm water. A shift brings several at once. Knowing each module is not the same as acting on four problems in the right order while writing a note someone else can act on.</p>
{{cards:Key terms for this module|Objective structured clinical examination (OSCE)::A timed practice station in which an examiner scores observed actions against a written checklist.|Critical step::A step on a scoring sheet that must be done for the station to pass, whatever the total score.|Simulation::Practice of a clinical task in a realistic setting without risk to a real patient.|Deliberate practice::Repeated practice of a defined skill with immediate feedback and a clear standard to reach.|Debriefing::A guided discussion after a simulation in which the learner reviews what happened and why.|In situ simulation::Simulation run in the real unit, with the real equipment and the real team.|Entrustment::The decision that a trainee can carry out a professional task without supervision.|Handoff::The transfer of information and responsibility for a patient from one clinician to another.}}
<p>This module re-teaches nothing. Each station points back to the module that teaches it. Most of what you need you already know. A few skills, such as sorting a full floor and handing off under pressure, only develop with practice and feedback. Your work is to practice them until they hold under pressure, and to be signed off by people who watched you do it.</p>
""",
    "case": {"title": "A full floor", "html": """
<p>It is Tuesday, 10:15 a.m., on the first shift of a 12-station unit in Bulacan. You are the only physician in the building. In the next five minutes, four things happen.</p>
<p>At Station 3, Mrs. Erlinda Bautista, 66, is in hour two. She says she feels faint. Her pressure is 84/50 mm Hg (illustrative). At Station 7, the nurse, Mr. Paolo Reyes, reports foam in the venous drip chamber of Mr. Ramon Cruz&rsquo;s circuit and an air detector alarm. Mr. Cruz is coughing. At Station 9, Ms. Grace Villanueva, 34, who dialyzes through a tunneled catheter, has a temperature of 38.6 &deg;C and rigors 30 minutes into her session. At Station 12, Mr. Leonardo Garcia, 52, wants to stop now because his son&rsquo;s school has called. He is 1.5 kilograms above his dry weight (illustrative).</p>
<p>The charge nurse, Ms. Liza Ramos, stands beside you holding the telephone. At Station 7, the machine&rsquo;s air detector has already stopped the blood pump and closed the venous line clamp.</p>
""", "questions": ["In what order do you go to these four patients, and what do you delegate first?",
                  "For which patient must the blood not be returned, and for which is the session continued?",
                  "Whom do you call, in what order, and what do you write afterward?"]},
    "sections": [
        ("orders", "Orders", "Orders that cannot be misread", """
<p>An order is a relay baton. The runners can be fast and fit, but if the baton is dropped, or passed to the wrong hand, the race is lost. In a dialysis unit the runners are you, the nurse, and the attending nephrologist. The baton is the written or spoken order.</p>
<h3>What a sound order does, and how orders fail</h3>
<p>A sound order carries five facts from your head to the nurse&rsquo;s hands without loss: which patient, which drug or action, how much, by which route, and when. Every gap is filled by a guess, and guesses fail most at night and under pressure.</p>
<p>In one descriptive report from four hemodialysis units, clinical directors recorded 88 errors and adverse events over 64,541 treatments. Of 35 medication errors, omission of an ordered medicine was the most common, at 24 of 35 (69%). No patient needed admission because of an event.[[holley2006]] The report shows where to look first: the order written but never carried out.</p>
{{fig:pod32_order_sheet}}
<div class="table-wrap"><table>
<thead><tr><th>Weak order</th><th>What can go wrong</th><th>Clear order</th></tr></thead>
<tbody>
<tr><td>A brand name only</td><td>The nurse cannot find it in stock, or gives a different product</td><td>The generic name, with the brand in brackets if the unit stocks only one</td></tr>
<tr><td>&ldquo;U&rdquo; or &ldquo;IU&rdquo; for units</td><td>A handwritten U can be read as a zero, so the dose is multiplied tenfold</td><td>&ldquo;units&rdquo; written in full</td></tr>
<tr><td>A trailing zero or a bare decimal point</td><td>A dose read ten times too high or too low</td><td>No trailing zero. A zero before a leading decimal point</td></tr>
<tr><td>&ldquo;Give now&rdquo; called across the floor</td><td>No record, no read-back, wrong patient</td><td>A verbal order read back by the nurse, then written in the chart as soon as the emergency allows</td></tr>
<tr><td>&ldquo;Reduce the fluid goal&rdquo;</td><td>A change to the prescription without the nephrologist</td><td>&ldquo;Ultrafiltration paused at 10:20 per unit protocol. Attending nephrologist informed at 10:24. Advice: &hellip;&rdquo;</td></tr>
</tbody></table></div>
<h3>What you order, and what you do not</h3>
<p>Module 1 set the line of authority, and Module 7 explained each line of the dialysis order. You order within the prescription and within the unit&rsquo;s standing orders. Changes to the dialysis prescription belong to the attending nephrologist: the time, the fluid goal, the dialysis fluid, the anticoagulation, and the access plan. In an emergency you act on the unit&rsquo;s protocol first, then call. You do not write a new prescription.</p>
<p>When you order a medicine for a patient without kidney function, check its dose and its removal by dialysis. The renal medication safety calculator linked below is a quick lookup. Module 20 explains the reasoning.</p>
{{call:Stop and call the attending nephrologist before any order that would change the dialysis prescription: the session time, the fluid goal, the dialysis fluid, the anticoagulant, or the access plan. Follow your unit&rsquo;s protocol for the first minutes of an emergency while you call.}}
{{key:Write every order so that a nurse you have never met can carry it out correctly at 3 a.m. without calling you.}}
"""),
        ("handoff", "Handoffs", "Handing off to the nephrologist and the emergency room", """
<p>A handoff is a bridge. Whatever you know about the patient is lost if it does not cross, however well you knew it on your side of the river. Most handoffs in your work cross two bridges: the telephone call to the attending nephrologist, and the transfer to an emergency room.</p>
<h3>Why handoffs fail, and what a structure adds</h3>
<p>Under stress, a speaker leaves out what seems obvious. A fixed structure works as a checklist for speech. It reminds you to say what you would otherwise assume.</p>
<p>Module 1 taught the SBAR format: situation, background, assessment, recommendation. A systematic review of 11 studies found moderate evidence that introducing SBAR improved patient safety, especially for telephone communication, and noted that high-quality studies are few.[[muller2018]]</p>
<p>The I-PASS program goes further. I-PASS stands for illness severity, patient summary, action list, situation awareness and contingency planning, and synthesis by the receiver. In a prospective study of resident handoffs at nine hospitals covering 10,740 admissions, the program was associated with a fall in medical errors from 24.5 to 18.8 per 100 admissions and in preventable adverse events from 4.7 to 3.3 per 100 admissions. Oral handoffs did not take longer: 2.4 and 2.5 minutes per patient.[[starmer2014]] The design compared periods before and after, in pediatric resident teams, not in dialysis units. It supports a structured handoff. It does not show which structure is best for you.</p>
<p>Use SBAR for a short call that asks for advice. Use the fuller I-PASS items when responsibility passes to someone else. With either, the receiver repeats back the key facts and the plan.</p>
<h3>The transfer letter</h3>
<p>A call reaches one person. A letter travels with the patient to everyone at the receiving end.</p>
{{fig:pod32_transfer_letter}}
<div class="table-wrap"><table>
<thead><tr><th>Item in the letter</th><th>Why the receiving team needs it</th></tr></thead>
<tbody>
<tr><td>Identity, age, and dialysis status and schedule</td><td>Tells them the patient has no kidney function and when dialysis is next due</td></tr>
<tr><td>The access, and the arm to protect</td><td>Prevents blood pressure cuffs, needles, and lines on the fistula arm</td></tr>
<tr><td>The last session: time on, fluid removed, anticoagulant given</td><td>Explains low volume, and warns of bleeding risk after heparin</td></tr>
<tr><td>The event, what was done, and when</td><td>Avoids repeating or omitting treatment</td></tr>
<tr><td>Latest vital signs and results, with times</td><td>Gives a baseline to compare against</td></tr>
<tr><td>Hepatitis B, hepatitis C, and HIV (human immunodeficiency virus) status</td><td>Allows correct isolation if the hospital dialyzes the patient</td></tr>
<tr><td>Medicines and allergies</td><td>Prevents harmful prescribing on arrival</td></tr>
<tr><td>The attending nephrologist&rsquo;s name and number, and yours</td><td>Gives them someone to call</td></tr>
</tbody></table></div>
{{flow:Handoff to the emergency room|Call::Call the attending nephrologist before transfer, unless the delay would harm the patient.|Report::Call the receiving emergency room and give an SBAR report.|Letter::Send the transfer letter with the patient, with a copy kept in the chart.|Confirm::Confirm that the patient arrived and that the receiving physician has the letter.|Document::Record whom you spoke to, at what time, and what was agreed.}}
{{call:Stop and call the attending nephrologist before any transfer to the emergency room, unless the patient is in cardiac arrest or the delay would harm the patient. In that case, follow your unit&rsquo;s protocol, have a team member call while you act, or call as soon as the patient has left, and record why you could not call first.}}
{{key:Say it in a structure, send it in writing, and have the receiver repeat it back.}}
"""),
        ("stations", "Practice stations", "The ten core bedside skills as practice stations", """
<p>A driving test does not ask you to define a brake. It watches whether you press it at the right moment. Each station asks you to do, not to describe.</p>
<h3>How a station works</h3>
<p>Each station is an objective structured clinical examination (OSCE) station. It has a fictional scenario, a time limit, a scoring sheet, a set of Critical steps, and a debrief. The OSCE was designed to improve the validity and reliability of performance assessment, which had relied on long and short case examinations.[[khan2013]] A checklist makes the examiner look at the same actions in every learner. A Critical step marks an action whose omission could harm a patient, however well the rest was done.</p>
<p>Each station uses the skills checklist of its source module and tests whether you can perform it in order, on time, and aloud. The emergency content follows the sources each module used, including a core curriculum on hemodialysis emergencies.[[greenberg2021]][[daugirdas2015]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Station</th><th>Source module</th><th>Examples of Critical steps</th><th>Time allowed (set by the unit)</th></tr></thead>
<tbody>
<tr><td>1. Fistula or graft examination before cannulation</td><td>Module 9</td><td>Looks, feels for the thrill, listens for the bruit; names a finding that stops cannulation</td><td></td></tr>
<tr><td>2. Catheter exit site and flow check</td><td>Module 10</td><td>Inspects the exit site and tunnel; recognizes poor flow and states the unit&rsquo;s next step</td><td></td></tr>
<tr><td>3. Safe to start and safe to go home</td><td>Module 11</td><td>Identifies a patient who should not start; checks standing pressure and the access before discharge</td><td></td></tr>
<tr><td>4. Falling pressure and the hypotension ladder</td><td>Module 13</td><td>Lays the patient back, stops fluid removal, screens for a dangerous cause, calls</td><td></td></tr>
<tr><td>5. Electrocardiogram (ECG) for high potassium and arrhythmia, and the code at the chair</td><td>Modules 15 and 18</td><td>Recognizes the ECG pattern; starts resuscitation and directs the circuit</td><td></td></tr>
<tr><td>6. Circuit failure: air, hemolysis, dialyzer reaction, needle dislodgement</td><td>Module 16</td><td>Stops the blood pump, clamps the lines, does not return the blood when it must not be returned</td><td></td></tr>
<tr><td>7. The shivering catheter patient and blood cultures</td><td>Module 17</td><td>Separates catheter infection from a reaction; starts the fever protocol; calls</td><td></td></tr>
<tr><td>8. Bleeding on heparin</td><td>Module 19</td><td>Controls the bleeding site; reports heparin given; calls</td><td></td></tr>
<tr><td>9. Emergency take-off with manual blood return</td><td>Module 30</td><td>Assigns one staff member to each patient and names who watches the venous line; states when the blood must not be returned</td><td>Timed</td></tr>
<tr><td>10. Refusal of treatment and the incident report</td><td>Module 31</td><td>Checks capacity; explains risks; documents an informed refusal with witnesses</td><td></td></tr>
</tbody></table></div>
<p>Station 4 uses the session review calculator linked below. Other stations use the site&rsquo;s corrected QT, sepsis screening, and heparin-induced thrombocytopenia calculators. The sepsis scores were not derived in dialysis patients. Calculators support your judgment. They do not replace it.</p>
<h3>The scoring sheet</h3>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Critical?</th><th>Done</th><th>Not done</th><th>Assessor&rsquo;s comment</th></tr></thead>
<tbody>
<tr><td>1. Goes to the chair and checks response, breathing, and pulse</td><td>Yes</td><td>&#9744;</td><td>&#9744;</td><td></td></tr>
<tr><td>2. Asks for help and states the problem aloud</td><td>No</td><td>&#9744;</td><td>&#9744;</td><td></td></tr>
<tr><td>3. &hellip; (the source module&rsquo;s checklist)</td><td>&hellip;</td><td>&#9744;</td><td>&#9744;</td><td></td></tr>
<tr><td>Time taken against the unit&rsquo;s standard</td><td>&mdash;</td><td colspan="2">Minutes:</td><td></td></tr>
<tr><td>Result: pass or repeat. Assessor&rsquo;s name and signature, date</td><td>&mdash;</td><td colspan="2"></td><td></td></tr>
</tbody></table></div>
<h3>Critical steps are gates, not points</h3>
<p>A station passes only when every Critical step is done and the total meets the Medical Director&rsquo;s standard.</p>
{{formula:<strong>Illustrative station score, not a pass mark.</strong> Pass = all Critical steps done AND (steps done &divide; total steps &times; 100) &ge; the unit&rsquo;s percentage standard.<br>Station 4 has 12 steps, 4 of them Critical. A learner completes 10 of 12 steps: 10 &divide; 12 &times; 100 = 83%, with all 4 Critical steps done. Whether that passes depends on the percentage the Medical Director sets.<br>A second learner completes 11 of 12 steps (92%) but misses one Critical step. That learner does not pass, whatever the percentage.<br>What the number tells you: how much of the checklist was done. What it does not tell you: whether the omitted steps mattered. The Critical flag answers that.}}
{{formula:<strong>Illustrative results at the emergency take-off station (Station 9).</strong> 11 steps, 3 of them Critical.<br>Learner A: 10 of 11 = 91%, all 3 Critical steps done. Passes under any percentage standard up to 91%.<br>Learner B: 11 of 11 = 100%, but slower than the unit&rsquo;s time standard. Repeat the station.<br>Learner C: 9 of 11 = 82%, and missed &ldquo;names who watches the venous line,&rdquo; a Critical step. Does not pass.<br>Teaching point: the percentage and the time standard are educational judgments. They should be set by a recognized standard-setting method, not copied from another program.}}
{{key:A station is passed by doing every Critical step, aloud, in order, on time. Knowing the step is not enough.}}
"""),
        ("simulation", "Why practice", "Why practice beats reading, and what the evidence shows", """
<p>Back to the swimmer. Reading builds a map of the task. Under pressure, people do not consult maps; they do what they have rehearsed. Practice with feedback makes a known sequence automatic, which frees attention for the patient.</p>
<p>The picture has a limit. Practice does not replace understanding. A learner who rehearses steps without the reasons freezes when the case departs from the script. The series put the reasons first. This module adds the rehearsal.</p>
{{fig:pod32_reading_vs_practice}}
<h3>What the studies show</h3>
<p>Cook and colleagues pooled 609 studies with 35,226 trainees that compared technology-enhanced simulation with no training. Simulation was associated with large effects on knowledge (pooled effect size 1.20) and on skills (1.09 to 1.18), with effects on behaviors with patients of 0.79 to 0.81, and a moderate effect on direct patient outcomes (0.50, 95% confidence interval [CI] 0.34 to 0.66). Heterogeneity was large, and 405 of the studies used a single group tested before and after.[[cook2011]] An effect size is a difference expressed in standard deviations. Values near 0.8 or more are conventionally called large.</p>
<p>Beating no training is easy. Does simulation beat ordinary clinical teaching? McGaghie and colleagues pooled 14 studies of simulation with deliberate practice against traditional clinical education. The overall effect size for specific skill acquisition was 0.71 (95% CI 0.65 to 0.76).[[mcgaghie2011]] The number of studies was small.</p>
<p>Does any of this reach patients? A community hospital in Chicago required residents to reach a mastery standard on a simulator before inserting central venous catheters in its intensive care unit (ICU). Line infections fell from 3.82 to 1.29 per 1,000 catheter-days. After adjustment for severity of illness, the incidence rate ratio was 0.26 (95% CI 0.09 to 0.74), a 74% reduction.[[barsuk2014]] This was a before-and-after study at one hospital. Other changes over the same months could have contributed.</p>
<h3>Debriefing</h3>
<p>Much of the learning happens afterward, in the review. Cheng and colleagues found favorable effects for simulation with debriefing against no intervention across all outcomes (effect sizes 0.28 to 2.16). Video-assisted debriefing made a negligible difference over debriefing without video (0.10). The key features of debriefing were usually reported incompletely, so which method works best remains unclear.[[cheng2014]]</p>
<h3>Resuscitation training</h3>
<p>The 2025 American Heart Association (AHA) guideline on resuscitation education is the first full update of its education recommendations since 2020.[[aha2025_education]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Topic</th><th>2025 AHA recommendation</th><th>Class and level of evidence</th></tr></thead>
<tbody>
<tr><td>Teamwork training</td><td>Life support training for health care professionals should include a specific emphasis on teamwork</td><td>Class 1, LOE B-R</td></tr>
<tr><td>Booster sessions</td><td>Recommended when training is delivered in a single concentrated course</td><td>Class 1, LOE B-R</td></tr>
<tr><td>In situ training</td><td>Reasonable in addition to traditional training</td><td>Class 2a, LOE C-LD</td></tr>
<tr><td>Rapid-cycle deliberate practice</td><td>May be reasonable as part of basic or advanced life support training for health care personnel</td><td>Class 2b, LOE C-LD</td></tr>
<tr><td>Scripted debriefing</td><td>May be reasonable for instructors</td><td>Class 2b, LOE C-LD</td></tr>
</tbody></table></div>
<p>LOE means level of evidence: B-R is moderate-quality randomized evidence, and C-LD is limited data. Class 1 is strong; Classes 2a and 2b are weaker.</p>
<p>In situ simulation has a second use. Practicing in the real unit, with the real cart, exposes hidden hazards before a patient meets them. A systematic review of 15 emergency department studies found equipment problems in 83% of studies and teamwork or communication problems in 67%.[[grace2024]] Many studies did not report whether the hazards were fixed. A missing clamp found during practice is a success.</p>
<p>Two limits apply. Knowledge and skill scores are surrogates, not harm avoided. And none of these studies took place in a dialysis unit.</p>
{{key:Reading tells you what to do. Practice with feedback is how you become able to do it under pressure.}}
"""),
        ("shift", "Simulated shift", "The simulated shift: four problems at once", """
<p>Picture a nurse at a typhoon evacuation center. Everyone needs help, and every family is right that their need is real. The order in which help arrives decides who is harmed. A full dialysis floor is the same problem in a smaller room.</p>
<h3>The logic of the order</h3>
<p>The order below is built from the earlier modules and rests on how fast each problem can harm. It is a teaching synthesis, not a validated triage tool.</p>
{{fig:pod32_four_problems}}
{{flow:Sorting a full floor|First: threat to life now::Any threat to the airway, breathing, circulation, or consciousness. Any circuit event in which the blood must not be returned: air, hemolysis, a severe dialyzer reaction (Modules 15 and 16).|Second: worsening within minutes::A falling pressure, active bleeding, or high potassium with ECG changes (Modules 13, 18, and 19).|Third: a decision due this session::Fever in a patient with a catheter, or a patient asking to leave early (Modules 17 and 31).|Fourth: what can follow within the shift::Full notes, the incident report, and routine calls.|Throughout: delegate::Hand each protocol step to a named nurse before you move. The nurse continues the protocol while you go to the next patient.}}
<p>You are not the only pair of hands. Nurses start the first steps of most emergencies under the unit&rsquo;s protocol. Your job is to confirm, decide, and call. A quick look can also change a tier: a faint patient who turns out to be confused moves up.</p>
<p>The shock index, heart rate divided by systolic pressure, is a quick check of how a patient is coping. The site&rsquo;s shock index calculator is linked below. A number helps you sort. It does not decide for you.</p>
<h3>Worked walk-through</h3>
{{formula:<strong>Illustrative walk-through of the opening case, not a protocol.</strong><br>Order: Station 7 (possible air, threat to life) &rarr; Station 3 (falling pressure, minutes) &rarr; Station 9 (fever with a catheter, decision this session) &rarr; Station 12 (request to leave, conversation and consent).<br>Delegated before leaving Station 7: the call to the attending nephrologist, and the hypotension ladder at Station 3.<br>At Station 3, shock index = heart rate &divide; systolic pressure. With an illustrative pulse of 92 and a systolic pressure of 84: 92 &divide; 84 = 1.1.<br>What the shock index tells you: a higher value suggests more circulatory strain and should prompt a closer look. What it does not tell you: the cause, or whether she will recover with first steps. It was not derived in dialysis patients.}}
<h3>How the shift is scored</h3>
<p>Colleagues play patients and staff. Four or five events arrive close together. You state aloud what you are doing and why.</p>
<div class="table-wrap"><table>
<thead><tr><th>Domain</th><th>What the preceptor looks for</th><th>Critical?</th></tr></thead>
<tbody>
<tr><td>Order of actions</td><td>The immediate threat first, with a stated reason for each choice</td><td>Yes</td></tr>
<tr><td>Circuit decisions</td><td>Blood not returned when it must not be; blood pump stopped and lines clamped</td><td>Yes</td></tr>
<tr><td>Delegation</td><td>Each protocol step handed to a named nurse before you move</td><td>No</td></tr>
<tr><td>Calls</td><td>The attending nephrologist called at the right time, in SBAR, with a read-back of the advice</td><td>Yes</td></tr>
<tr><td>Orders</td><td>Within the prescription, read back, written promptly</td><td>Yes</td></tr>
<tr><td>Notes</td><td>Event notes with the eight elements of Module 31; an incident report for the air event</td><td>No</td></tr>
<tr><td>Debrief</td><td>Names one thing to do differently</td><td>No</td></tr>
</tbody></table></div>
{{call:During the simulated shift, state aloud when you would call the attending nephrologist and what you would say. Follow your unit&rsquo;s protocol for the first steps of each event. A missed call for any Stop-and-call trigger from Modules 13 to 19 or Module 30 is a failed Critical step.}}
{{key:Sort by threat to life, then by speed, then by what must be decided today. Hand off each task to a named person before you move.}}
"""),
        ("test", "Test and passport", "The written test, the passport, and what a score means", """
<p>A learner&rsquo;s permit is not a driver&rsquo;s license. Your written test is the permit. Your signed passport, earned while people watched you work, is the license.</p>
<h3>The written test</h3>
<p>The proposed test has 80 newly written items, sampling every module in proportion to its weight. First-Shift Essentials modules weigh most, because you need them on day one.</p>
{{formula:<strong>Illustrative test blueprint arithmetic.</strong> Items for a module = total items &times; that module&rsquo;s weight &divide; sum of all weights.<br>Weights: First-Shift Essentials (9 modules) = 2; Core (20 modules) = 1; Advanced (3 modules) = 0.5.<br>Sum of weights = 9 &times; 2 + 20 &times; 1 + 3 &times; 0.5 = 18 + 20 + 1.5 = 39.5.<br>Per Essentials module: 80 &times; 2 &divide; 39.5 = 4.05, about 4. Per Core module: 80 &times; 1 &divide; 39.5 = 2.03, about 2. Per Advanced module: 80 &times; 0.5 &divide; 39.5 = 1.01, about 1.<br>Check: 9 &times; 4 + 20 &times; 2 + 3 &times; 1 = 36 + 40 + 3 = 79. The remaining item goes to an emergency module.<br>What the arithmetic does: it makes the weights explicit. What it does not do: choose them. The weights are the Medical Director&rsquo;s educational judgment.}}
<div class="table-wrap"><table>
<thead><tr><th>Tier</th><th>Modules</th><th>Weight</th><th>Items per module</th><th>Items in the tier</th></tr></thead>
<tbody>
<tr><td>First-Shift Essentials</td><td>1, 2, 5, 9, 10, 11, 13, 15, 16</td><td>2</td><td>4</td><td>36</td></tr>
<tr><td>Core</td><td>3, 4, 6, 7, 8, 12, 14, 17 to 24, 26, 29 to 32</td><td>1</td><td>2</td><td>40</td></tr>
<tr><td>Advanced</td><td>25, 27, 28</td><td>0.5</td><td>1</td><td>3</td></tr>
<tr><td>Extra item</td><td>One emergency module</td><td>&mdash;</td><td>1</td><td>1</td></tr>
<tr><td><strong>Total</strong></td><td>32</td><td>&mdash;</td><td>&mdash;</td><td><strong>80</strong></td></tr>
</tbody></table></div>
<h3>What a score shows</h3>
<p>A written score shows study, not competence. The cut score, proposed at 80%, is an educational judgment for a recognized standard-setting method. Competence is shown at the stations and on supervised shifts.</p>
<p>Ten Cate proposed that competency-based training rest on entrustment: a decision, made by people who have watched the work, that a trainee can carry out a professional activity without supervision.[[tencate2005]] The passport records those decisions.</p>
{{fig:pod32_passport}}
<h3>The Competency Passport</h3>
<p>The passport is one page. It lists the skills checklists from each module, the ten stations, the simulated shift, the mock code and disaster drill, and the written test. It carries the advanced cardiovascular life support (ACLS) certificate that the Department of Health (DOH) licensing order for dialysis facilities, Administrative Order (AO) 2012-0001, requires of physicians on duty.[[doh2012]] It also carries the training certificates set out in the Philippine Society of Nephrology (PSN) guidelines for hemodialysis clinics.[[psn2024]] Each line has a date and a signature.</p>
{{key:A written score shows that you studied. A signature from someone who watched you work shows that you can do it.}}
"""),
        ("signoff", "Clearance", "Clearance for independent duty", """
<p>Before a new bridge opens, an engineer inspects it against a standard and signs. Clearance for independent duty works the same way.</p>
{{flow:From self-study to clearance|Self-study::The 32 modules, with each module&rsquo;s self-assessment.|Orientation::The unit, its protocols, its emergency cart, and its staff.|Shadow and supervised shifts::You work beside an experienced physician on duty, then under supervision.|Mock code and disaster drill::Run in the unit with the team you will work with.|Stations and simulated shift::All Critical steps satisfactory.|Written test::Passed at the cut score the Medical Director sets.|Clearance::The Medical Director signs the passport.}}
<p>The code station and the mock code follow the current AHA guidelines for basic life support and for systems of care.[[aha2025_bls]][[aha2025_systems]] The figure below, from the site&rsquo;s emergency series, shows what the team leader directs in the first minutes.</p>
{{fig:code_first5|The first five minutes of a cardiac arrest in a dialysis unit. The team leader directs both resuscitation and what happens to the circuit.}}
<p>Skills fade without use. Keep the passport current, and ask for a repeat station after a long absence or a serious event in which you were involved. A repeat is not a penalty.</p>
<h3>What is uncertain</h3>
{{cards:Honest limits of this module|No dialysis data::No study of simulation training for physicians on duty in dialysis units was found. Every effect estimate here is borrowed from other settings.|Surrogates::Most simulation evidence measures knowledge and skill scores. Patient-outcome evidence comes mostly from before-and-after studies.|Standards are judgments::Pass marks, time standards, and the written-test cut score are educational judgments, to be set by a recognized standard-setting method.|Debriefing::Which debriefing method works best is unclear.|The sorting logic::The order in the simulated shift is a teaching synthesis of earlier modules, not a validated triage tool.}}
{{key:Clearance is a signature from people who watched you work. Keep it current, and ask for a repeat when you have been away.}}
"""),
    ],
    "debrief": ["""
<p><strong>In what order, and what do you delegate first?</strong> Station 7 first. Foam in the venous drip chamber, an air detector alarm, and a coughing patient mean possible air embolism, an immediate threat to life. You confirm that the blood pump has stopped and the venous line is clamped, and you position Mr. Cruz and give oxygen as Module 16 describes. Before you leave him, you delegate twice: Ms. Ramos calls the attending nephrologist now, and a named nurse starts the hypotension ladder at Station 3. Station 3 comes second, because a falling pressure can worsen within minutes. Station 9 comes third: fever with rigors in a catheter patient needs a decision this session, and the fever protocol starts now. Station 12 comes last. Mr. Garcia is stable, and his request needs a calm conversation.</p>
<p><strong>Blood returned or not, and which sessions continue?</strong> The blood is not returned at Station 7, because air may remain in the venous line. The circuit is kept for inspection. At Station 3, the session usually continues once the pressure recovers, and the attending nephrologist decides the remaining fluid goal. At Station 9, the nephrologist decides whether the session continues. If it ends, the circuit is sound, and no cluster or contaminated fluid is suspected, the blood is returned per protocol (Module 17). At Station 12, Mr. Garcia may leave after an informed refusal that covers the risk of leaving above his dry weight, with a normal blood return.</p>
<p><strong>Whom do you call, and what do you write?</strong> The attending nephrologist hears about Station 7 first, at once. A combined SBAR update on Stations 3, 9, and 12 follows after you have examined each patient. If Mr. Cruz needs transfer, you call before he leaves and send a transfer letter with him. Afterward you write a timed event note for each patient, an incident report for the air event, and the informed refusal form for Mr. Garcia, signed by witnesses.</p>
"""],
    "skills": {"title": "The simulated shift, scored by the preceptor",
               "intro": "Run this shift with your preceptor and two colleagues playing patients and nurses. State aloud what you are doing and why. The preceptor scores each step.",
               "items": [
                   ("Receives the four reports and states aloud the order of response with a reason for each.", True),
                   ("Goes first to the patient with an immediate threat (possible air embolism) and confirms that the pump is stopped, the line clamped, and the blood not returned.", True),
                   ("Delegates the hypotension ladder to a named nurse before leaving that patient.", False),
                   ("Examines the hypotensive patient and screens for a dangerous cause (Module 13).", True),
                   ("Recognizes fever with a catheter and starts the unit&rsquo;s protocol.", True),
                   ("Calls the attending nephrologist at the right time with an SBAR report.", True),
                   ("Conducts the refusal conversation, checks capacity, and documents an informed refusal with witnesses.", False),
                   ("Writes clear, timed orders within the prescription and reads back verbal orders.", True),
                   ("Prepares a transfer letter that a receiving physician could act on.", False),
                   ("Writes event notes containing the eight elements of Module 31.", False),
                   ("Completes an incident report for the air event.", False),
                   ("Takes part in the debrief and names one thing to do differently.", False),
               ],
               "placement": "Over your supervised shifts, complete all ten stations and one simulated shift with a preceptor. Run at least one station in situ, in your own unit with its real equipment, and report any hazard you find to the charge nurse. Bring your passport to each session for signature."},
    "quiz": [
        ("In a descriptive report from four hemodialysis units, which medication error was most common?",
         ["A wrong dose", "Omission of an ordered medicine", "A wrong patient", "A wrong route"], 1,
         "Omission accounted for 24 of 35 medication errors."),
        ("At 2 a.m. you order a medicine across the floor during an emergency. What makes this verbal order safe?",
         ["The nurse remembers it until morning",
          "A second nurse hears it",
          "The nurse reads it back, and you write it in the chart as soon as the emergency allows",
          "You use the brand name so there is no confusion"], 2,
         "Read-back catches mishearing; writing makes it part of the record."),
        ("Why should &ldquo;units&rdquo; be written in full on an order?",
         ["A handwritten U can be read as a zero, multiplying the dose",
          "Pharmacies require it for billing",
          "It makes the order shorter",
          "It identifies the drug as a generic"], 0,
         "A misread U turns a dose into ten times the intended amount."),
        ("A nurse asks you to lower a patient&rsquo;s fluid goal for the rest of the session because his pressure keeps falling. What do you do?",
         ["Lower the goal yourself, because you are on duty",
          "Tell the nurse to continue at the original goal",
          "End the session and send him home",
          "Follow the unit&rsquo;s protocol for the falling pressure and call the attending nephrologist about the goal"], 3,
         "The fluid goal belongs to the prescription."),
        ("What did the I-PASS handoff study by Starmer and colleagues show?",
         ["Structured handoffs took twice as long",
          "A handoff program was associated with fewer medical errors and preventable adverse events, without longer handoffs",
          "Handoffs in dialysis units caused most errors",
          "SBAR was superior to I-PASS"], 1,
         "Errors fell from 24.5 to 18.8 per 100 admissions, in a before-after design."),
        ("A patient with a left arm fistula is transferred for chest pain. Which letter item most directly protects the access?",
         ["The allergy list",
          "The serology status",
          "The arm to protect, with no cuffs, needles, or lines on it",
          "The time of the last meal"], 2,
         "A blood pressure cuff or an intravenous line on the fistula arm can damage or clot the access."),
        ("A patient collapses in cardiac arrest at the chair. When do you call the attending nephrologist?",
         ["Before starting resuscitation",
          "During the first steps, through a team member who calls while you lead the resuscitation",
          "Only if the patient dies",
          "The next morning"], 1,
         "Calling yourself first would delay compressions. Module 15 has a team member call the attending nephrologist while you lead."),
        ("What is a Critical step on a station scoring sheet?",
         ["A step worth double points",
          "A step that only the Medical Director may perform",
          "A step that can be skipped if time is short",
          "A step that must be done for the station to pass, whatever the total score"], 3,
         "Critical steps are gates, not points."),
        ("A learner completes 11 of 12 steps (92%) at the hypotension station but does not screen for a dangerous cause, a Critical step. The unit&rsquo;s standard is 80%. What is the result?",
         ["Repeat the station", "Pass, because 92% exceeds 80%", "Pass with a comment", "Pass if the time standard was met"], 0,
         "A missed Critical step means the station is not passed, whatever the percentage."),
        ("What did the meta-analysis by Cook and colleagues find for simulation compared with no training?",
         ["No effect on knowledge",
          "Large effects on knowledge and skills, and a moderate effect on patient-related outcomes",
          "Harm to patients",
          "Effects only in dialysis units"], 1,
         "Pooled effect sizes were about 1.1 to 1.2 for knowledge and skills and 0.50 for patient outcomes."),
        ("What is the main limitation of the study by Barsuk and colleagues on central line infections?",
         ["It included too many hospitals",
          "It measured only knowledge",
          "It was a before-and-after study at one hospital, so other changes could have contributed",
          "It was conducted in dialysis units"], 2,
         "The 74% reduction is an association within one site, not proof of cause."),
        ("Four events arrive together: a coughing patient with foam in the venous line, a falling pressure, a feverish catheter patient, and a stable patient who wants to leave. Where do you go first?",
         ["The patient who wants to leave, before he unplugs himself",
          "The feverish patient, to draw cultures before antibiotics",
          "The patient with the falling pressure",
          "The coughing patient with foam in the venous line"], 3,
         "Possible air embolism is an immediate threat to life."),
        ("In the same shift, for which patient must the blood not be returned?",
         ["The patient with possible air in the venous line",
          "The patient with the falling pressure",
          "The patient who wants to leave early",
          "The feverish catheter patient whose circuit is sound"], 0,
         "Returning blood from a line that may contain air could send more air into the patient."),
        ("A colleague scores 95% on the written test. What does this show?",
         ["That the colleague is cleared for independent duty",
          "That the colleague has studied the material, not that the colleague can perform under pressure",
          "That the stations can be skipped",
          "That the colleague no longer needs ACLS"], 1,
         "Entrustment is a separate judgment by people who watched the work."),
        ("An in situ practice code in your unit finds that the suction unit on the emergency cart does not work. How should you view this?",
         ["As a failed drill",
          "As a reason to stop in situ practice",
          "As the learner&rsquo;s error",
          "As a success: a hidden hazard found before a real patient needed the equipment"], 3,
         "Finding latent safety threats is one purpose of in situ simulation."),
    ],
    "terms": [("Objective structured clinical examination (OSCE)", "A timed practice station scored against a written checklist by an observer."),
              ("Critical step", "A checklist step that must be done for a station to pass."),
              ("Deliberate practice", "Repeated practice of a defined skill with immediate feedback toward a clear standard."),
              ("Debriefing", "A guided review of a simulation, after it ends, of what happened and why."),
              ("In situ simulation", "Simulation run in the real clinical unit with its real equipment and team."),
              ("Latent safety threat", "A hidden hazard in equipment, systems, or teamwork that has not yet harmed a patient."),
              ("I-PASS", "A handoff structure: illness severity, patient summary, action list, situation awareness and contingency planning, synthesis by the receiver."),
              ("Entrustment", "The decision that a trainee can carry out a professional task without supervision."),
              ("Effect size", "A difference between groups expressed in standard deviations, used to compare results across studies."),
              ("Read-back", "Repetition of a verbal order or report by the receiver, confirmed by the sender.")],
    "readings": [("code-blue-acls-dialysis-unit.html", "Resuscitation in a dialysis unit, for the code station and the mock code."),
                 ("hemodialysis-complications.html", "An overview of the complications behind the emergency stations."),
                 ("hemodialysis-transfer-guide.html", "What to send and say when a dialysis patient is transferred.")],
    "calcs": ["calc-hd-session-review.html", "calc-shock-index.html", "calc-renal-med-safety.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
