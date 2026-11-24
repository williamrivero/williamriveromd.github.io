# -*- coding: utf-8 -*-
"""Physician on Duty, Module 07: Reading the Dialysis Order and Judging the Dose.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty and a nurse at a dialysis chair, comparing a paper dialysis order with the settings on the machine screen and a laboratory result slip.",
    "objectives": [
        "Read each line of a hemodialysis order, from the dialyzer to the fluid removal goal, and explain what each line controls.",
        "Recognize an order that does not fit today&rsquo;s patient, using the latest laboratory results and bedside findings, and report it to the attending nephrologist, who owns the prescription.",
        "Calculate and interpret the urea reduction ratio and single-pool Kt/V, confirm that the blood samples were collected correctly, and list the causes of a low result.",
        "Compare twice-weekly, thrice-weekly, and more frequent or longer schedules, citing what the randomized trials showed.",
        "Describe hemodiafiltration and expanded hemodialysis, and summarize what the trials and meta-analyses show, with absolute numbers.",
    ],
    "big": """
{{plain:Think of the dialysis order as a recipe. The dialysis fluid is the ingredients, the dialyzer is the oven, the blood and fluid flows are the heat, and the session length is the cooking time. Change any one of them and the dish comes out different. A recipe written for last month&rsquo;s guest may be wrong for the guest at the table today.}}
<p>The picture has a limit. Food does not answer back. A patient&rsquo;s heart, vessels, and access respond to the order in real time. A dialysis fluid potassium that suits a patient with a high pre-dialysis potassium can be dangerous for the same patient after two days of diarrhea.</p>
{{cards:Key terms for this module|Prescription::The attending nephrologist&rsquo;s written order for the session: dialyzer, time, flows, dialysis fluid composition, anticoagulation, fluid goal, and schedule.|Dialysis fluid (dialysate)::The fluid on the other side of the membrane. Its composition is part of the prescription.|Blood flow rate (Qb)::The speed of the blood pump, in mL per minute.|Dialysate flow rate (Qd)::The speed of the dialysis fluid through the dialyzer, in mL per minute.|Urea reduction ratio (URR)::The percent fall in blood urea during one session.|Kt/V::Dialyzer urea clearance (K) multiplied by session time (t), divided by body water (V). A measure of small-solute removal.|Hemodiafiltration (HDF)::Hemodialysis with a large volume of added convection, replaced with ultrapure fluid.}}
<p>You are the last physician to look at the order before the blood pump starts. Most orders fit the patient who arrives. A few do not: the potassium is low after vomiting, the catheter cannot give the written blood flow, or the patient has been leaving early. Your work is to recognize the mismatch, know which settings carry the most risk, read an adequacy result, and report clearly. You do not rewrite the prescription. That belongs to the attending nephrologist.</p>
""",
    "case": {"title": "The potassium bath no one questioned", "html": """
<p>Aling Merlinda Ocampo, 72, from Quezon City, has been on thrice-weekly hemodialysis for three years. She arrives for her Wednesday 10:00 a.m. session. She had diarrhea for two days and ate little. Nurse Paolo Dizon has her on the monitor. Her blood pressure is 112/70 mm Hg, and her pulse is 64 per minute and irregular. Her weight is 0.6 kg above her target. The point-of-care result from the morning sample shows a potassium of 3.1 mmol/L. These are illustrative values, not targets.</p>
<p>Her standing order has not changed in a year. It lists a dialysis fluid potassium of 1 mEq/L, four hours, a blood flow of 350 mL/min, a dialysate flow of 500 mL/min, and her usual dialyzer. Her medication list includes digoxin, started by her cardiologist last month. Her last monthly urea reduction ratio was 61%. In the months before, it was 68% to 70%. The session log shows that she signed off 40 minutes early twice last week.</p>
<p>Nurse Dizon has primed the circuit. He looks up and asks, &ldquo;Same order as always, Doc?&rdquo;</p>
""", "questions": ["Which line of the order does not fit today, and why is it dangerous for this patient now?",
                  "What could explain the fall in her urea reduction ratio, and what facts would you gather?",
                  "What do you say to the nurse now, and what exactly do you report to the attending nephrologist?"]},
    "sections": [
        ("order", "The order", "The order, line by line", """
<p>Module 05 explained the circuit. Each line of the order sets one part of it. Know the process, and you can predict what goes wrong when a line is wrong.</p>
{{fig:pod07_order}}
<p>The dialyzer&rsquo;s area and flux (its permeability) set the size of the exchange. Blood flow, dialysate flow, and time set its speed and duration. Removal of small molecules rises with flow, but with diminishing returns, because the dialyzer has a maximum it can clear. Time has no such ceiling. Every minute lost is dose lost.</p>
<p>The dialysis fluid composition sets which way each substance moves and how fast. Temperature changes vessel tone. Anticoagulation keeps the circuit open (Module 19). The fluid removal goal belongs to Module 08.</p>
<div class="table-wrap"><table>
<thead><tr><th>Line of the order</th><th>What it controls</th><th>Too low or short</th><th>Too high or long</th></tr></thead>
<tbody>
<tr><td>Dialyzer</td><td>Size and permeability of the membrane</td><td>Less clearance</td><td>A wrong dialyzer may trigger a known reaction</td></tr>
<tr><td>Session time</td><td>Total treatment</td><td>Underdialysis; faster fluid removal per hour</td><td>Longer chair time</td></tr>
<tr><td>Blood flow (Qb)</td><td>Blood passing the membrane each minute</td><td>Less clearance; a hidden cause of low Kt/V</td><td>Pressure alarms, access trauma, recirculation</td></tr>
<tr><td>Dialysate flow (Qd)</td><td>Fresh fluid along the membrane</td><td>Less clearance</td><td>Little added clearance</td></tr>
<tr><td>Potassium</td><td>Potassium gradient</td><td>Fast fall in potassium; arrhythmia</td><td>Too little removal</td></tr>
<tr><td>Calcium</td><td>Calcium in or out</td><td>Weaker contraction, low pressure</td><td>Calcium load</td></tr>
<tr><td>Sodium</td><td>Sodium balance, thirst</td><td>Cramps, low pressure</td><td>Thirst, weight gain, hypertension</td></tr>
<tr><td>Bicarbonate</td><td>Acid correction</td><td>Persistent acidosis</td><td>Alkalosis after the session</td></tr>
<tr><td>Temperature</td><td>Heat returned</td><td>Chills</td><td>Vessels open, pressure falls</td></tr>
<tr><td>Anticoagulation</td><td>Circuit clotting</td><td>Clotted dialyzer, lost dose</td><td>Bleeding</td></tr>
</tbody></table></div>
<p>The mechanisms in this table follow a standard dialysis text.[[daugirdas2015]]</p>
{{fig:hd_params|The main settings of a hemodialysis session and what each one moves.}}
<h3>What the trials say about the dialyzer</h3>
<p>The Kidney Disease Outcomes Quality Initiative (KDOQI) 2015 update recommends biocompatible high-flux or low-flux membranes (Guideline 5.1, graded 1B).[[kdoqi_hd2015]] In the Hemodialysis (HEMO) Study, 1,846 patients were randomized in a two-by-two design to standard or high dose, and to low-flux or high-flux membranes. Neither the higher dose nor high flux changed mortality (relative risks 0.96 and 0.92; both confidence intervals crossed 1).[[eknoyan2002]] The Membrane Permeability Outcome (MPO) trial, in 738 patients starting dialysis, also found no overall survival difference. Survival was better with high flux in a prespecified stratum with serum albumin at or below 4 g/dL.[[locatelli2009]] A subgroup finding in a neutral trial suggests a benefit. It does not prove one.</p>
<p>Your job is narrower: confirm with the nurse that what is set matches what is ordered.</p>
{{key:You check that the machine matches the order and that the order fits the patient. You do not choose the order.}}
"""),
        ("bath", "The bath", "The bath: potassium, calcium, sodium, bicarbonate, and temperature", """
<p>The blood moves toward the composition of the dialysis fluid. A large gap means fast movement, and the heart feels the speed.</p>
<h3>Potassium: the gradient sets the speed</h3>
<p>Almost all of the body&rsquo;s potassium sits inside cells. The dialyzer removes potassium from the blood, at a speed set by the gap between blood and dialysis fluid. Potassium leaves the cells to refill the blood more slowly. So a steep gradient lowers serum potassium quickly, while total body potassium falls much less.[[daugirdas2015]]</p>
<p>The heart muscle cell&rsquo;s resting charge depends on the ratio of potassium inside to outside the cell. A fast fall in blood potassium changes that ratio. The thick, stiff heart of many dialysis patients (Module 04) is prone to arrhythmia. Low potassium also increases digoxin&rsquo;s effect on the heart, which is established pharmacology.</p>
{{fig:pod07_kgradient}}
{{formula:<strong>Illustrative arithmetic, not a target.</strong> Potassium gradient = serum potassium &minus; dialysis fluid potassium.<br>Serum potassium 3.1 mmol/L with a 1 mEq/L bath: gradient 2.1.<br>The same patient with a 2 mEq/L bath: gradient 1.1.<br>The same patient with a 3 mEq/L bath: gradient 0.1.<br>What it tells you: how hard the bath pulls potassium out of this patient at the start. What it does not tell you: the right bath. That choice belongs to the attending nephrologist.}}
<p>The evidence on the bath is observational. In a review of 400 cardiac arrests in dialysis units, arrests occurred at about 7 per 100,000 sessions. Patients who arrested were nearly twice as likely as the general dialysis population to have been dialyzed against a 0 or 1 mEq/L potassium bath, 17.1% against 8.8%.[[karnik2001]] A case-control study of 502 arrests in clinics treating 43,200 patients found that a dialysis fluid potassium below 2 mEq/L was associated with sudden cardiac arrest, whatever the pre-dialysis potassium. A low calcium bath was also associated with arrest.[[pun2011]]</p>
<p>The Dialysis Outcomes and Practice Patterns Study (DOPPS) followed 37,765 patients in 12 countries. Compared with a dialysis fluid potassium of 3 mEq/L or more, the sudden death rate was higher with 1.5 mEq/L or less and with 2 to 2.5 mEq/L.[[jadoul2012]] These studies cannot exclude confounding, because sicker patients with high potassium receive low baths. Still, the association recurs across three data sets, and the mechanism fits.</p>
<h3>Calcium, bicarbonate, sodium, and temperature</h3>
<p>A low calcium bath lowers ionized calcium during the session, which can weaken heart contraction and lower pressure.[[daugirdas2015]] A high bicarbonate bath can leave the patient alkalotic at the end. In DOPPS, among 17,031 patients, each 4 mEq/L higher dialysis fluid bicarbonate was associated with higher mortality (hazard ratio 1.08, 95% confidence interval 1.01 to 1.15).[[tentori2013]] This is also observational.</p>
<p>Dialysis fluid sodium affects thirst, weight gain, and blood pressure. The large randomized RESOLVE trial of sodium had no published results at the time of writing, so this module makes no outcome claim about sodium.</p>
{{fig:pod07_cool}}
<p>Cooler dialysis fluid keeps skin vessels narrower; Module 13 covers its use for low pressure. The one large randomized trial of the bath, MyTEMP, assigned 84 centers and 15,413 patients to personalized cooler fluid or standard temperature. The primary outcome, cardiovascular death or hospital admission for heart attack, ischemic stroke, or heart failure, occurred in 21.4% against 22.4% (adjusted hazard ratio 1.00).[[mytemp2022]]</p>
<h3>What you do</h3>
<p>Compare today&rsquo;s potassium, intake, losses, and medicines with the bath ordered. Change the bath yourself only if your unit&rsquo;s protocol explicitly allows it.</p>
{{call:Stop and call the attending nephrologist before the session starts when a low-potassium bath is ordered for a patient with a low or falling serum potassium, a patient on digoxin, or a patient with recent vomiting or diarrhea. Call for any mismatch between the order and today&rsquo;s laboratory results.}}
{{key:The bath is part of the prescription. A low-potassium bath for a low-potassium patient is a dangerous order, however routine it looks.}}
"""),
        ("fit", "Does it fit", "Does this order fit today&rsquo;s patient?", """
<p>A standing order fits the patient as they were at the last review. Since then they may have been admitted, started a medicine, or stopped eating. You check who is in the chair today.</p>
<p>Recent illness matters. In the review of 400 dialysis-unit cardiac arrests, 37% of the patients had been hospitalized in the 30 days before the arrest.[[karnik2001]] A patient back from the hospital needs a fresh look at the order.</p>
{{flow:Does this order fit today&rsquo;s patient?|Identity and version::Two identifiers and the current signed order.|Access::Can it deliver the ordered blood flow today (Modules 09 and 10)?|Weight and fluid goal::An unusual goal needs a reason (Module 08).|Latest laboratory results::Potassium, calcium, bicarbonate, hemoglobin, compared with the bath and plan.|Bleeding risk::Recent surgery, procedure, fall, or bleeding; check the anticoagulation (Module 19).|New medicines::Digoxin, QT-prolonging drugs, new blood pressure medicines.|Recent illness::Admission, vomiting, diarrhea, poor intake, or fever.|Decide and report::Proceed, change only what the protocol allows, or hold and call the attending nephrologist.}}
<p>Your unit&rsquo;s protocol allows some first steps without waiting for a call. Other changes belong to the attending nephrologist alone. Learn both lists before your first shift.</p>
<div class="table-wrap"><table>
<thead><tr><th>Usually allowed by unit protocol (first minutes, then call)</th><th>Attending nephrologist only</th></tr></thead>
<tbody>
<tr><td>Pausing or reducing fluid removal for low blood pressure</td><td>The dialysis fluid potassium, calcium, sodium, and bicarbonate</td></tr>
<tr><td>Running a lower blood flow when the access cannot safely give more</td><td>Session time and schedule</td></tr>
<tr><td>Holding the session start while you obtain a result or speak to the nephrologist</td><td>The dialyzer and the anticoagulation plan</td></tr>
<tr><td>Point-of-care tests listed in the protocol</td><td>Dry weight and the fluid removal goal for future sessions</td></tr>
<tr><td>Emergency steps in a written emergency protocol</td><td>Chronic medicines and the access plan</td></tr>
</tbody></table></div>
<p>The left column shows examples, not rules. If your protocol is silent, the change goes to the attending nephrologist.</p>
{{key:A circuit that is primed is not a reason to proceed. If the order does not fit, hold the start and call.}}
"""),
        ("dose", "Measuring dose", "Measuring the dose: URR and Kt/V", """
<p>Picture the body water as a tank. Kt/V asks how many tank volumes were cleaned of urea in one session. K is the dialyzer&rsquo;s urea clearance; multiplied by time (t), it gives the volume cleared. V is the body water.</p>
{{fig:pod07_ktv}}
<h3>What urea represents, and what it does not</h3>
<p>Urea, a product of protein breakdown, crosses the membrane freely, so it marks small-solute removal. It does not measure middle molecules, protein-bound toxins, phosphate, or fluid (Module 03). Kt/V and the urea reduction ratio are surrogates. A good number does not mean the patient is well.</p>
<h3>Where the measure came from</h3>
<p>Gotch and Sargent re-analyzed the National Cooperative Dialysis Study, a randomized trial of urea levels and treatment times. They defined dose as Kt/V and showed that the probability of treatment failure rose sharply at low values.[[gotch1985]] Owen and colleagues then studied 13,473 patients. Compared with a urea reduction ratio of 65% to 69%, a ratio of 55% to 59% was associated with higher odds of death (odds ratio 1.28), and below 55% even higher (1.39). Serum albumin was a far stronger predictor of death than the urea reduction ratio.[[owen1993]] Nutrition and illness matter more than the urea number alone.</p>
<p>More is not always better. In the HEMO Study, an achieved single-pool Kt/V of 1.71 against 1.32 did not change mortality (relative risk 0.96, 95% confidence interval 0.84 to 1.10).[[eknoyan2002]]</p>
<h3>The targets, as the guideline states them</h3>
<p>KDOQI 2015 Guideline 3.1 recommends a target single-pool Kt/V (spKt/V) of 1.4 per session for patients treated thrice weekly, with a minimum delivered spKt/V of 1.2 (graded 1B). For schedules other than thrice weekly, Guideline 3.3 suggests a target standard Kt/V of 2.3 volumes per week, with a minimum delivered dose of 2.1, calculated by a method that includes fluid removal and residual kidney function (not graded). Guideline 4.1 recommends a minimum of 3 hours per session for thrice-weekly patients with low residual kidney function, below 2 mL/min (graded 1D).[[kdoqi_hd2015]] Your unit sets its own target and schedule.</p>
<h3>The formulas</h3>
<p>The urea reduction ratio is the percent fall in blood urea nitrogen (BUN). Single-pool Kt/V by the Daugirdas second-generation formula corrects for urea made and fluid removed during the session.[[daugirdas1993]] Equilibrated Kt/V (eKt/V) corrects for urea that returns from the tissues after the session ends.[[daugirdas1995]] The form shown below applies to an arteriovenous access (fistula or graft); a slightly different version is used for catheters.[[daugirdas2015]] Standard Kt/V compares schedules with different numbers of sessions per week and can include residual kidney clearance.[[daugirdas2010]]</p>
{{formula:<strong>Worked example, illustrative values only.</strong> Pre-dialysis BUN 70 mg/dL. Post-dialysis BUN 22 mg/dL. Session 4.0 hours. Fluid removed 3.0 L. Post-dialysis weight 60 kg.<br><strong>URR</strong> = (pre BUN &minus; post BUN) &divide; pre BUN = (70 &minus; 22) &divide; 70 = <strong>68.6%</strong>.<br><strong>spKt/V</strong> (Daugirdas second generation) = &minus;ln(R &minus; 0.008 &times; t) + (4 &minus; 3.5 &times; R) &times; UF &divide; W, where R = post &divide; pre BUN, t = hours, UF = liters removed, W = post-dialysis weight in kg.<br>R = 22 &divide; 70 = 0.314. &minus;ln(0.314 &minus; 0.032) = &minus;ln(0.282) = 1.265. (4 &minus; 3.5 &times; 0.314) &times; 3.0 &divide; 60 = 2.90 &times; 0.05 = 0.145. spKt/V = 1.265 + 0.145 = <strong>1.41</strong>.<br><strong>eKt/V</strong> &asymp; spKt/V &minus; 0.6 &times; spKt/V &divide; t + 0.03 = 1.41 &minus; 0.21 + 0.03 = <strong>1.23</strong>.<br>What it tells you: how much urea this session removed, by three related measures. What it does not tell you: whether the patient is well nourished, free of symptoms, or at the right weight. The attending nephrologist interprets the result.}}
<p>The site&rsquo;s Kt/V calculator (linked below) performs the urea reduction ratio and single-pool calculation from the same inputs. Use it to check your arithmetic, not to set a target.</p>
{{key:Kt/V is a floor, not a goal. A good number does not mean a well patient, and a low number has a cause you can find.}}
"""),
        ("sampling", "Blood samples", "Getting the blood samples right", """
<p>An adequacy result is two photographs, before and after. Take either at the wrong moment and the picture lies.</p>
<h3>The pre-dialysis sample</h3>
<p>The pre-dialysis sample must be pure blood. If saline or heparin from the needle or line enters the sample, the BUN is diluted and falsely low. A falsely low starting value makes the fall look smaller, and the dose looks lower than it was.[[daugirdas2015]]</p>
<h3>The post-dialysis sample</h3>
<p>Two hazards pull in opposite directions. The first is recirculation. Cleaned blood from the venous needle re-enters the arterial needle, so a sample drawn at full flow reads too low, and the dose looks better than it was. Slowing or stopping the blood pump for a short, set interval before the draw lets unmixed blood reach the sampling port.[[daugirdas2015]]</p>
<p>The second is rebound. After the session, urea moves back into the blood from tissues where it was removed more slowly, over roughly 30 to 60 minutes. A sample drawn late reads too high, and the dose looks worse than it was. This rebound is also why equilibrated Kt/V is lower than single-pool Kt/V.[[daugirdas1995]]</p>
{{flow:A correct adequacy draw|Before the session::Draw the pre-dialysis sample from the needle or catheter before any saline or heparin enters the line.|At the end of the session::Stop fluid removal as the protocol directs.|Slow or stop the pump::Use your unit&rsquo;s method, slow-flow or stop-pump, for the interval the protocol sets.|Draw from the arterial port::Take the post-dialysis sample promptly, before rebound begins.|Label and record::Note the actual session time, delivered blood flow, fluid removed, and post-dialysis weight. The formula needs all of them.}}
{{fig:bun_sampling|The pre-dialysis and post-dialysis samples. Dilution, recirculation, and rebound each distort the result in a predictable direction.}}
<div class="table-wrap"><table>
<thead><tr><th>Sampling error</th><th>Effect on post or pre BUN</th><th>Effect on the reported dose</th></tr></thead>
<tbody>
<tr><td>Saline or heparin in the pre-dialysis sample</td><td>Pre BUN falsely low</td><td>Dose looks lower than delivered</td></tr>
<tr><td>Post sample at full flow with recirculation</td><td>Post BUN falsely low</td><td>Dose looks higher than delivered</td></tr>
<tr><td>Post sample drawn late, after rebound</td><td>Post BUN falsely high</td><td>Dose looks lower than delivered</td></tr>
</tbody></table></div>
<p>You know your unit&rsquo;s method, check that it is followed, and make sure the actual time and blood flow are recorded. The KDOQI 2015 update describes the methods.[[kdoqi_hd2015]]</p>
{{key:Before you blame the prescription for a low result, ask how the samples were drawn.}}
"""),
        ("lowdose", "Low dose", "When the dose is low: access, time, flow, or sample?", """
<p>A low result has four common suspects. Check the cheapest first, the sample. Then the commonest, lost time. Then the blood flow and the access.</p>
{{flow:Low adequacy: access, time, flow, or sample?|Sample::Was the pre-dialysis sample clean? Was the post-dialysis sample drawn by the unit&rsquo;s method and on time? If not, report it and ask whether to repeat.|Time::Minutes ordered against minutes delivered: late starts, alarms, early sign-offs.|Blood flow::Ordered against actual flow, and alarms that forced the pump down.|Access::Recirculation or poor flow (Modules 09 and 10).|Dialyzer::Clotting, or a dialyzer different from the order.|Patient::A larger patient has a larger V.|Report::Call the attending nephrologist with the facts.}}
<p>Lost time also carries risk. In DOPPS, a treatment time below 210 minutes was associated with sudden death (hazard ratio 1.13), and so was a Kt/V below 1.2 (hazard ratio 1.10).[[jadoul2012]] These are associations from an observational cohort. Patients who shorten sessions may differ in other ways.</p>
{{formula:<strong>Illustrative arithmetic, simplified.</strong> Prescribed time 240 minutes. Delivered time 200 minutes, after two late starts and an early sign-off.<br>Time lost = 40 &divide; 240 = <strong>17%</strong> of the prescribed treatment.<br>Kt is clearance multiplied by time.[[gotch1985]] At constant clearance, Kt falls in proportion to time. A spKt/V of 1.41 would fall to about 1.41 &times; 200 &divide; 240 &asymp; <strong>1.18</strong>.<br>What it tells you: time lost at the chair is dose lost, and the loss is large enough to matter. What it does not tell you: the exact new Kt/V. The real relation is logarithmic and includes urea made during the session, so a measured Kt/V is still needed.}}
<p>The site&rsquo;s session review calculator (linked below) summarizes delivered time, flow, and events for your report.</p>
{{call:Stop and call the attending nephrologist when adequacy falls below the unit&rsquo;s target on two consecutive checks, or when a patient repeatedly signs off early or loses treatment time. Report delivered minutes, actual blood flow, access type and recent problems, clotting, and the sampling method used.}}
{{key:Time lost at the chair is dose lost. It shows up as a low result weeks later.}}
"""),
        ("schedule", "Schedules", "How often and how long: schedules compared", """
<p>Picture a leaking boat. Bail it three times a week and the water rises high between bailings. Bail a little every day and the level stays low. Water, potassium, and acid accumulate between sessions in the same way. The longer the gap, the higher they climb.</p>
<p>The picture has a limit. Dialysis removes urea fastest at the start of a session, when blood levels are highest. So more frequent sessions remove more than the same hours given in fewer sessions. Standard Kt/V, not single-pool Kt/V, is used to compare schedules.[[daugirdas2010]]</p>
{{fig:hd_week|The week of a thrice-weekly patient. Fluid and potassium rise most over the long gap.}}
<h3>What the trials of more frequent dialysis showed</h3>
<p>The Frequent Hemodialysis Network (FHN) Daily Trial randomized 245 patients to in-center hemodialysis six times a week or three times a week for 12 months. Weekly standard Kt/V was 3.54 against 2.49. Frequent dialysis improved both coprimary composites: death or a rise in left ventricular mass (hazard ratio 0.61, 95% confidence interval 0.46 to 0.82), and death or a fall in a physical health score (hazard ratio 0.70, 95% confidence interval 0.53 to 0.92). Vascular access interventions were more frequent with frequent dialysis.[[fhn2010]] Left ventricular mass is a surrogate. The trial was not powered for death alone.</p>
<p>The FHN Nocturnal Trial randomized 87 patients to home nocturnal dialysis six nights a week or conventional dialysis. It found no significant effect on either coprimary outcome. Phosphate and blood pressure control were better in the nocturnal group.[[rocco2011]] The small size limits what the neutral result can show.</p>
<p>KDOQI 2015 suggests that patients be offered in-center short frequent hemodialysis (Guideline 2.1, graded 2C). It recommends that patients considering it be informed of its risks: a possible increase in vascular access procedures (Guideline 2.2, graded 1B) and low blood pressure during dialysis (graded 1C).[[kdoqi_hd2015]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Schedule</th><th>Small-solute clearance per week</th><th>What trials showed</th><th>Burden and risk</th></tr></thead>
<tbody>
<tr><td>Twice weekly (incremental start)</td><td>Lower; relies on residual function</td><td>Small trials; see Module 03[[vilar2022]][[fernandezlucas2025]]</td><td>Fewer trips; two long gaps a week</td></tr>
<tr><td>Thrice weekly, conventional</td><td>The reference standard</td><td>The comparator in most trials[[eknoyan2002]]</td><td>One long gap each week</td></tr>
<tr><td>Short daily, in center</td><td>Higher standard Kt/V</td><td>Better composite outcomes in FHN; more access interventions[[fhn2010]]</td><td>Five or six trips a week</td></tr>
<tr><td>Long nocturnal, at home</td><td>Highest</td><td>Neutral coprimary outcomes in a small trial[[rocco2011]]</td><td>Home training and a partner</td></tr>
</tbody></table></div>
<p>The schedule is the attending nephrologist&rsquo;s decision. You know each patient&rsquo;s schedule and watch the long gap (Modules 02 and 15).</p>
{{key:A missed or shortened session costs more on a schedule with fewer sessions. Report it the same day.}}
"""),
        ("hdf", "Hemodiafiltration", "Hemodiafiltration and expanded hemodialysis: what the trials show", """
<p>Diffusion is tea spreading from a tea bag into still water. Small particles spread fast and large ones barely move. Convection is pouring the water through a sieve. The flow carries larger particles with it, whatever their size, up to the size of the holes.</p>
<p>The picture has a limit. A membrane&rsquo;s pores vary in size, and blood protein coats them during the session (Module 05). Hemodiafiltration adds a large volume of convection to standard diffusion. The water removed is replaced with ultrapure fluid that the machine makes online from dialysis fluid. Expanded hemodialysis uses a medium cut-off membrane that lets more middle molecules through by internal convection, without separate replacement fluid.</p>
{{fig:pod07_diffconv}}
<h3>The trials</h3>
<p>The open-label ESHOL trial randomized 906 patients in Spain to hemodialysis or high-efficiency postdilution online hemodiafiltration. Mortality was lower with hemodiafiltration (hazard ratio 0.70, 95% confidence interval 0.53 to 0.92).[[maduell2013]]</p>
<p>The CONVINCE trial randomized 1,360 patients in several European countries. All were judged able to reach a convection volume of at least 23 L per session. The hemodiafiltration group achieved a mean of 25.3 L. Over a median of 30 months, death occurred in 17.3% with hemodiafiltration and 21.9% with high-flux hemodialysis (hazard ratio 0.77, 95% confidence interval 0.65 to 0.93).[[blankestijn2023]] Quality of life declined in both groups, more slowly with hemodiafiltration. The clearest difference was in cognitive function: a decline of 0.95 units against 3.90 units.[[rose2024]] A prespecified subgroup analysis found no convincing difference in these effects across age, diabetes, cardiovascular disease, vintage, access, or residual urine.[[cromm2026]] A cost analysis estimated about &euro;27,000 to &euro;37,000 per quality-adjusted life-year in Europe, and its authors advise translating costs locally.[[schouten2025]]</p>
<p>An individual patient data meta-analysis pooled five trials and 4,153 patients. Over a median of 30 months, death occurred in 23.3% with hemodiafiltration and 27.0% with hemodialysis (hazard ratio 0.84, 95% confidence interval 0.74 to 0.95). Risk fell as convection volume rose.[[vernooij2024]] The 2026 Cochrane update included 62 studies and 6,897 participants. Convective therapy likely reduces death from any cause (risk ratio 0.88, 95% confidence interval 0.80 to 0.96) and cardiovascular death (risk ratio 0.78), both with moderate-certainty evidence. Effects on nonfatal cardiovascular events, fatigue, access problems, and hospitalization were inconclusive. Only four small studies, with 163 participants, tested expanded hemodialysis.[[vernooij2026]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Study</th><th>Design and size</th><th>Main finding</th><th>Limits</th></tr></thead>
<tbody>
<tr><td>ESHOL</td><td>Open-label randomized trial, 906</td><td>Death hazard ratio 0.70</td><td>Unblinded; one country[[maduell2013]]</td></tr>
<tr><td>CONVINCE</td><td>Pragmatic randomized trial, 1,360</td><td>Death 17.3% vs. 21.9%; hazard ratio 0.77</td><td>Only patients able to reach a high volume[[blankestijn2023]]</td></tr>
<tr><td>Pooled patient data</td><td>Meta-analysis of 5 trials, 4,153</td><td>Death 23.3% vs. 27.0%; hazard ratio 0.84</td><td>Trials differed in volume achieved[[vernooij2024]]</td></tr>
<tr><td>Cochrane 2026</td><td>Systematic review, 62 studies, 6,897</td><td>Death risk ratio 0.88, moderate certainty</td><td>Expanded hemodialysis barely tested[[vernooij2026]]</td></tr>
</tbody></table></div>
{{formula:<strong>Absolute numbers, calculated here from the published proportions.</strong> These numbers needed to treat were not reported by the trials.<br>CONVINCE: 21.9% &minus; 17.3% = 4.6 percentage points. 1 &divide; 0.046 &asymp; <strong>22</strong> patients treated for about 2.5 years to prevent one death.[[blankestijn2023]]<br>Pooled patient data: 27.0% &minus; 23.3% = 3.7 percentage points. 1 &divide; 0.037 &asymp; <strong>27</strong> patients over a median of 30 months.[[vernooij2024]]<br>What it tells you: the size of the benefit in patients like those in the trials. What it does not tell you: the benefit in patients who cannot reach a high convection volume.}}
<h3>What the evidence does not settle</h3>
<p>Trial patients had access good enough to reach a high volume; frail patients with weak access are underrepresented. Results of the UK H4RT trial were not found as published at the time of writing. Online hemodiafiltration needs ultrapure water and capable machines (Module 06). Whether units in the Philippines can deliver high-volume hemodiafiltration at scale, and at what cost, is a policy question for the Medical Director.</p>
<h3>What you do on a hemodiafiltration session</h3>
<p>The convection volume, often shown as substitution volume, is part of the prescription. It depends on blood flow. Check the machine summary at the end and record the blood flow achieved. The site&rsquo;s expanded hemodialysis toolkit covers medium cut-off membranes.</p>
{{call:Call the attending nephrologist when a hemodiafiltration session cannot reach the ordered convection volume, especially if the cause is a fall in blood flow from the access.}}
{{key:High-volume hemodiafiltration reduced deaths in trials of patients who could reach the volume. The volume, not the label, is what was tested.}}
"""),
    ],
    "debrief": ["""
<p><strong>Which line does not fit, and why is it dangerous now?</strong> The dialysis fluid potassium. A very low bath may have suited her when her potassium ran high. Today it is 3.1 mmol/L after diarrhea and poor intake, so the gradient is about 2.1 and her potassium would fall further and fast. She is 72, her pulse is irregular, and she takes digoxin, whose effect on the heart rises as potassium falls. Very low potassium baths were associated with cardiac arrest and sudden death in observational studies.</p>
<p><strong>What could explain the fall in her URR?</strong> Her log gives the first clue. Two early sign-offs of 40 minutes each cost about a sixth of those sessions. You would also check the sampling method on the draw day, the blood flow actually run, access problems or recirculation, dialyzer clotting, and any change in her weight. Poor intake also matters; in Owen&rsquo;s data, nutrition predicted outcome more strongly than the urea number.</p>
<p><strong>What do you say, and what do you report?</strong> To Nurse Dizon: &ldquo;Not yet. Please hold the start. Let&rsquo;s get a 12-lead electrocardiogram (ECG) per protocol while I call the attending.&rdquo; You do not change the bath yourself unless your unit&rsquo;s protocol explicitly allows it. You call the attending nephrologist using the SBAR format from Module 01 (situation, background, assessment, recommendation). Situation: a 72-year-old woman with an irregular pulse, about to start on a very low potassium bath. Background: two days of diarrhea, poor intake, digoxin since last month, potassium 3.1 mmol/L this morning. Assessment: the bath risks a fast fall in potassium in a patient prone to arrhythmia; her URR fell to 61% with two early sign-offs last week. Recommendation: a bath and plan for today, whether to check a digoxin level, and an adequacy review. You read back the new order and document it.</p>
"""],
    "skills": {"title": "Order verification at the chair, and the adequacy draw",
               "intro": "Perform this check on a simulated patient or on a real patient&rsquo;s order with your preceptor, who plays the nurse and observes.",
               "items": [
                   ("Confirms patient identity with two identifiers and confirms the current, signed order version.", True),
                   ("Matches the dialyzer, session time, blood flow, and dialysate flow on the machine to the order.", False),
                   ("Matches the dialysis fluid potassium, calcium, sodium, bicarbonate, and temperature to the order.", True),
                   ("Compares the bath with today&rsquo;s pre-dialysis potassium and asks about vomiting, diarrhea, poor intake, and digoxin.", True),
                   ("Checks the anticoagulation line against bleeding risk and recent procedures.", False),
                   ("Confirms that the access can deliver the ordered blood flow, and notes it if not.", False),
                   ("States aloud which deviations the unit&rsquo;s protocol allows and which need the attending nephrologist.", False),
                   ("On adequacy days, confirms that the pre-dialysis sample is drawn before saline or heparin enters the line.", True),
                   ("Confirms that the post-dialysis sample uses the unit&rsquo;s slow-flow or stop-pump method at the right time.", True),
                   ("Records delivered minutes, actual blood flow, fluid removed, post-dialysis weight, and any interruptions.", False),
                   ("Calculates the URR and spKt/V from a set of values and states what the result does and does not show.", False),
                   ("Reports any mismatch and the facts gathered in SBAR format, and reads back the advice received.", True),
               ],
               "placement": "For two weeks, check the order at the chair with the nurse for every patient you start. Keep a log of each mismatch you find and how it was resolved. On one adequacy day, watch both draws for three patients and compare the method with your unit&rsquo;s protocol. Review the log with your preceptor."},
    "quiz": [
        ("Which change in the order raises small-solute removal without a ceiling set by the dialyzer?",
         ["A higher blood flow",
          "A higher dialysate flow",
          "A longer session time",
          "A larger dialyzer"], 2,
         "Flow and dialyzer size have diminishing returns. Every minute adds dose."),
        ("A man on thrice-weekly dialysis has a pre-dialysis potassium of 3.3 mmol/L after three days of vomiting. His order lists a very low potassium bath. What should you do?",
         ["Start as ordered, because the order was signed",
          "Hold the start and call the attending nephrologist",
          "Start as ordered and recheck potassium in two hours",
          "Cancel the session and send him home"], 1,
         "A steep gradient would lower his potassium fast. The bath belongs to the nephrologist."),
        ("What did Karnik and colleagues find about potassium baths in dialysis-unit cardiac arrests?",
         ["Patients who arrested were nearly twice as likely to have been on a 0 or 1 mEq/L bath",
          "High potassium baths caused most arrests",
          "Bath potassium had no relation to arrest",
          "Randomized patients on low baths had more arrests"], 0,
         "17.1% of arrest patients were on a 0 or 1 mEq/L bath, against 8.8% of the dialysis population. The study was observational."),
        ("Why does digoxin make a low-potassium bath more dangerous?",
         ["Digoxin raises serum potassium",
          "Digoxin is removed by dialysis and loses its effect",
          "Digoxin blocks potassium removal",
          "Low potassium increases digoxin&rsquo;s effect on the heart"], 3,
         "Hypokalemia increases digoxin toxicity. This is established pharmacology."),
        ("What did the MyTEMP trial show about cooler dialysis fluid?",
         ["It halved cardiovascular deaths",
          "As a policy for all patients, it did not reduce cardiovascular death or hospitalization",
          "It increased mortality",
          "It improved Kt/V"], 1,
         "In 84 centers and 15,413 patients, the adjusted hazard ratio was 1.00."),
        ("What does Kt/V measure?",
         ["Removal of small solutes such as urea, relative to body water",
          "Removal of middle molecules",
          "Fluid removed during the session",
          "The patient&rsquo;s nutritional state"], 0,
         "Kt/V is a surrogate for small-solute removal. It does not measure middle molecules, fluid, or nutrition."),
        ("In the HEMO Study, what happened when the dose was raised above the standard?",
         ["Mortality fell by a third",
          "Mortality rose",
          "Mortality did not change",
          "The trial stopped early for benefit"], 2,
         "A single-pool Kt/V of 1.71 against 1.32 gave a relative risk of death of 0.96, with a confidence interval crossing 1."),
        ("Pre-dialysis BUN is 80 mg/dL and post-dialysis BUN is 24 mg/dL. What is the urea reduction ratio?",
         ["30%",
          "56%",
          "64%",
          "70%"], 3,
         "(80 &minus; 24) &divide; 80 = 0.70, or 70%."),
        ("A nurse draws the post-dialysis sample from the arterial line with the pump at full speed through a fistula with recirculation. How does this affect the result?",
         ["The dose looks higher than it was",
          "The dose looks lower than it was",
          "No effect, because the formula corrects it",
          "Only the pre-dialysis value is affected"], 0,
         "Cleaned blood lowers the post BUN, so the dose looks better."),
        ("Why is equilibrated Kt/V lower than single-pool Kt/V?",
         ["Urea is made faster after dialysis",
          "Urea moves back into the blood from tissues after the session",
          "The post sample is diluted with saline",
          "Fluid removal raises urea concentration"], 1,
         "Urea rebound from slower compartments raises blood urea after the session. Equilibrated Kt/V accounts for it."),
        ("Mr. Ramos&rsquo;s spKt/V has fallen from 1.45 to 1.15. His log shows full time and no alarms. On the adequacy day, a new nurse drew the post sample 45 minutes after the session ended. What is the most likely explanation?",
         ["A clotted dialyzer",
          "Access recirculation",
          "A sample drawn after rebound, making the dose look lower",
          "A smaller body water volume"], 2,
         "A late draw catches rebound, so the dose looks low. Report it and ask whether to repeat."),
        ("A patient lost 40 of 240 prescribed minutes in each session this month. Her usual spKt/V is 1.41. Using the simplified proportional estimate, what is her approximate spKt/V?",
         ["1.41",
          "1.30",
          "1.00",
          "1.18"], 3,
         "1.41 &times; 200 &divide; 240 &asymp; 1.18. The real relation is not linear, so a measured value is still needed."),
        ("What did the FHN Daily Trial show for six-times-weekly in-center dialysis?",
         ["Lower mortality as a single outcome",
          "Better composite outcomes of death or left ventricular mass, and death or physical health, with more access interventions",
          "No effect on any outcome",
          "Fewer access interventions"], 1,
         "Hazard ratios were 0.61 and 0.70 for the two composites. Left ventricular mass is a surrogate."),
        ("In CONVINCE, death occurred in 17.3% with hemodiafiltration and 21.9% with hemodialysis over about 2.5 years. What is the approximate number needed to treat to prevent one death?",
         ["5",
          "22",
          "46",
          "100"], 1,
         "The absolute difference is 4.6 percentage points, and 1 &divide; 0.046 &asymp; 22. This number was calculated from published proportions, not reported by the trial."),
        ("Ms. Lim is on online hemodiafiltration. Her fistula has been difficult and her blood flow is well below the order. The machine shows a low convection volume each session. What should you do?",
         ["Raise the substitution volume on the machine",
          "Switch her to hemodialysis yourself",
          "Ignore it, because hemodiafiltration is still running",
          "Record the delivered blood flow and volume, examine the access, and report to the attending nephrologist"], 3,
         "Convection volume depends on blood flow, and the access may be failing."),
    ],
    "terms": [("Prescription", "The attending nephrologist&rsquo;s written order for a dialysis session."),
              ("Dialysate potassium gradient", "The difference between serum potassium and dialysis fluid potassium. It sets the speed of potassium removal."),
              ("Urea reduction ratio (URR)", "The percent fall in blood urea nitrogen during one session."),
              ("Single-pool Kt/V (spKt/V)", "Kt/V calculated as if urea were in one well-mixed space, corrected for urea made and fluid removed during the session."),
              ("Equilibrated Kt/V (eKt/V)", "Kt/V corrected for urea that rebounds from the tissues after the session."),
              ("Standard Kt/V (stdKt/V)", "A weekly measure used to compare schedules with different numbers of sessions."),
              ("Recirculation", "Return of cleaned blood from the venous needle into the arterial needle, which lowers the efficiency of the session."),
              ("Urea rebound", "The rise in blood urea after a session as urea moves back from the tissues."),
              ("Convection volume", "The volume of water pushed across the membrane and replaced during hemodiafiltration."),
              ("Expanded hemodialysis", "Hemodialysis with a medium cut-off membrane that removes more middle molecules.")],
    "readings": [("dialysis-prescription.html", "The parts of a dialysis prescription and how the attending nephrologist sets them."),
                 ("dialysis-adequacy.html", "How adequacy is measured, and what a low result means."),
                 ("hemodiafiltration-new-standard.html", "Hemodiafiltration in more depth, with the trial evidence.")],
    "calcs": ["calc-dialysis-adequacy-ktv.html", "calc-hd-session-review.html", "calc-hdx-toolkit.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
