# -*- coding: utf-8 -*-
"""Physician on Duty, Module 14: High Blood Pressure and the Breathless Patient.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty assessing a breathless older man seated upright in a dialysis chair with nasal oxygen, a nurse at the monitor.",
    "objectives": [
        "Explain why blood pressure readings taken in the dialysis unit mislead, and why home and ambulatory readings predict outcomes better.",
        "Explain why salt and water are the first target for long-term blood pressure control, citing the trial evidence.",
        "Distinguish a hypertensive emergency from an asymptomatic high reading, and act on each per your unit&rsquo;s protocol.",
        "Explain why pressure can rise during dialysis, and what is and is not known about its risk.",
        "Work through breathlessness in a dialysis patient by six causes, and manage the first minutes of acute pulmonary edema.",
        "Describe the main blood pressure drug classes, which ones dialysis removes, and why timing around the session matters, leaving doses to the attending nephrologist.",
    ],
    "big": """
{{plain:Think of an overfilled car tire. Pumping harder does not help, and neither does a stronger valve. The pressure falls only when you let some air out. In most dialysis patients the blood vessels are the tire, and salt and water are the extra air.}}
<p>The picture has a limit. A tire is passive, and the vessels are not. Arteries in kidney failure are stiff, and hormones and nerves keep them tight. So some patients stay hypertensive after the extra fluid is gone. Still, in kidney failure, salt intake sets the extracellular volume, and volume is the first thing to look at.[[sarafidis2017]]</p>
{{cards:Key terms for this module|Interdialytic period::The time between two dialysis sessions. The long interdialytic gap is the two-day gap over the weekend.|Ambulatory blood pressure monitoring::An automatic cuff worn for a day or more that records pressure at set intervals, day and night. In the dialysis studies in this module it covered the 44 hours between sessions.|Intradialytic hypertension::A rise in blood pressure from the start to the end of a session. Definitions differ between studies.|Hypertensive emergency::High blood pressure with new or worsening damage to an organ such as the brain, heart, aorta, eyes, or lungs.|Target-organ damage::Injury to the organs that high pressure harms first.|Pulmonary edema::Fluid that has leaked out of the lung vessels into the tissue and air sacs of the lung.|Dialyzable drug::A medicine that passes through the dialyzer membrane, so a session removes part of it.}}
<p>Most high readings in a dialysis unit are not emergencies. A few are: the patient who walks in with fluid in the lungs, or whose pressure rises with a headache and new weakness. Your work is to tell these apart within minutes, start the first steps per your unit&rsquo;s protocol, call the attending nephrologist, and name the long-term cause, usually salt and water.</p>
""",
    "case": {"title": "Breathless before the needles", "html": """
<p>It is Monday, 7:00 a.m. Mr. Ernesto Garcia, 66, known to the staff as Mang Ernie, has been on dialysis for five years through a right upper-arm fistula. He missed Friday&rsquo;s session to attend a family wake. He arrives sitting forward and speaks in short sentences.</p>
<p>Nurse Grace Lim has seated him upright, started oxygen by nasal cannula per protocol, and attached the monitor. His weight is 74.6 kg, and his target weight is 70.0 kg. Blood pressure is 192/104 mm Hg. Pulse is 108 and regular. Respiratory rate is 28 per minute. Oxygen saturation is 88% on room air and 91% on oxygen. You hear crackles to the middle of both lungs. He has no chest pain and no wheeze. Both ankles are swollen.</p>
<p>The electrocardiogram (ECG) shows sinus tachycardia with no new ST-segment change. Bedside glucose is 160 mg/dL. Potassium is pending. All values are illustrative.</p>
""", "questions": ["Which of the six causes of breathlessness are most likely, and which single finding would most change your plan?",
                  "Is this a hypertensive emergency, and does the answer change where he should be treated?",
                  "Dialyze here now, or transfer: what do you tell the attending nephrologist, and what do you write?"]},
    "sections": [
        ("measure", "Readings that mean something", "Blood pressure that means something", """
<p>A pre-dialysis reading is a photograph taken at the worst moment of the week. Home readings are a video, and the arteries live with the video.</p>
<p>Three things distort the photograph. The pre-dialysis reading comes at the peak of fluid gain. The patient has hurried in and is anxious, which adds a white-coat effect. Technique is rushed. The post-dialysis reading has the opposite bias, because the machine has contracted the blood volume. Neither shows the average pressure between sessions.[[sarafidis2017]]</p>
{{fig:pod14_home_vs_unit}}
<h3>What the evidence shows</h3>
<p>Agarwal followed 326 hemodialysis patients for a mean of 32 months. Higher home and ambulatory systolic pressure was associated with higher all-cause mortality. Pre-dialysis and post-dialysis readings did not predict death (P = 0.17 and P = 0.997).[[agarwal2010]] An earlier cohort of 150 patients found the same pattern: home systolic pressure showed a graded relation with death across quartiles, and unit readings did not.[[alborzi2007]] Both were cohorts from one U.S. group. They show which reading carries prognostic information, not that lowering it to a given level saves lives.</p>
<p>A European consensus document states that the J- or U-shaped relation of unit readings with survival most likely reflects their low accuracy, and that high home or ambulatory pressure is clearly associated with shorter survival.[[sarafidis2017]] The Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference discussed measurement and targets in conference conclusions, not graded recommendations.[[kdigo_bpvol2020]]</p>
{{cards:Taking a reading you can trust|Rest::Seated, back supported, feet flat, for a few minutes first.|Cuff::Sized to the arm. A cuff that is too small reads falsely high.|Arm::Never the access arm.|Repeat::One high value is a prompt to recheck, not a diagnosis.|Trend::Compare with recent sessions and home readings.}}
{{formula:<strong>Worked example D (illustrative).</strong> Seven morning home readings, systolic: 152, 148, 160, 155, 149, 151, 158 mm Hg.<br>Average = sum &divide; number of readings = 1,073 &divide; 7 = 153.3 mm Hg.<br>The same patient&rsquo;s pre-dialysis reading on Monday, after the long gap, was 182 mm Hg.<br><strong>What it tells you:</strong> the pressure his arteries carry most of the week, the reading that carries prognostic weight.[[agarwal2010]][[alborzi2007]] <strong>What it does not tell you:</strong> whether 153 mm Hg is too high for him. The attending nephrologist sets his target.}}
{{key:Do not treat the pre-dialysis number. Treat the patient, and judge control from home readings.}}
"""),
        ("volume", "Salt and water first", "Why salt and water come first", """
<p>Without kidney function, the salt a patient eats stays in the body until the next session. Salt brings thirst, and the water stays with the salt (Module 2). The extra volume raises cardiac output first and, over weeks, vascular resistance. Stiff arteries, renin-angiotensin and sympathetic activation, sleep apnea, and erythropoiesis-stimulating agents (the injections for anemia) add to it.[[sarafidis2017]] Volume is the first cause to look for because it is common and treatable.</p>
<h3>The trial that tested it</h3>
<p>The Dry-Weight Reduction in Hypertensive Hemodialysis Patients (DRIP) trial randomized 150 hypertensive patients to have their target weight probed downward or to usual care. Over eight weeks, target weight fell by about 1 kg. Ambulatory systolic pressure between sessions fell by 6.9 mm Hg at four weeks and 6.6 mm Hg at eight weeks compared with control. Low-pressure symptoms during dialysis increased, and quality of life did not worsen.[[agarwal2009drip]] Probing worked even without overt signs of overload, so the benefit came from fluid the examination missed.[[georgianos2019]] The outcome was blood pressure, a surrogate, over eight weeks. DRIP did not test death or heart events.</p>
<p>A secondary analysis of DRIP showed that removing fluid lowered the post-dialysis starting point of the ambulatory curve.[[agarwal2009abpm]] In patients on three or more drugs, a 2024 review names volume as the most important treatable cause of resistance, once white-coat effect and missed doses are excluded.[[georgianos2024]] Module 8 covers how the target weight is judged.</p>
{{flow:Volume first, then drugs|Confirm::Repeated careful readings and home readings.|Check adherence::Which tablets, and when.|Look for hidden fluid::Weight gains, a pressure that climbs during sessions, breathlessness lying flat. Normal ankles do not exclude it.|Report::The attending nephrologist decides on target weight, session length, dialysis fluid, and salt advice.|Drugs after volume::Added or changed by the nephrologist when pressure stays high.}}
<h3>Lowering pressure helps; the right level is unknown</h3>
<p>A meta-analysis of eight randomized trials (1,679 patients, 495 cardiovascular events) found systolic pressure 4.5 mm Hg lower on active treatment. Treatment was associated with fewer cardiovascular events (relative risk 0.71), fewer deaths from any cause (0.80), and fewer cardiovascular deaths (0.71).[[heerspink2009]] The trials used different drugs in different patients. The abstract does not give event rates, so the absolute benefit cannot be stated from it.</p>
<p>The Blood Pressure in Dialysis (BID) pilot trial randomized 126 patients to an intensive or a standard pre-dialysis systolic range. Four patients died in the intensive arm and one in the standard arm, with nonsignificant excesses of cardiovascular events, admissions, and access clotting. The authors called it a possible safety signal in a trial too small to conclude.[[miskulin2018]] No adequately powered trial has defined a target. Do not add or change maintenance blood pressure medicines at the chair.</p>
{{key:In a dialysis patient with high pressure, ask first about salt and water. Drugs come after volume.}}
"""),
        ("drugs", "Drugs and dialysis", "Drug classes, removal by dialysis, and timing", """
<p>Picture a bucket with a hole in it. Some medicines leak out through the dialyzer; others stay. Small, water-soluble, weakly protein-bound drugs cross the membrane; large, fat-soluble, or protein-bound drugs do not. A removed drug loses part of its effect. A retained drug taken shortly before the session peaks during fluid removal and can deepen a fall in pressure (Module 13).[[inrig2010]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Class</th><th>Common use in dialysis patients</th><th>Removed by dialysis?</th><th>Timing note</th></tr></thead>
<tbody>
<tr><td>Angiotensin-converting enzyme (ACE) inhibitors</td><td>First-line in many patients, especially with diabetes or heart failure</td><td>Most yes (for example, lisinopril). Fosinopril no</td><td>Removal may limit low pressure in the session, but the effect may fade when pressure rises during dialysis</td></tr>
<tr><td>Angiotensin receptor blockers (ARBs)</td><td>Alternative to ACE inhibitors</td><td>No</td><td>Effect persists through the session</td></tr>
<tr><td>Water-soluble beta-blockers (atenolol, metoprolol)</td><td>After a recent heart attack, or with heart failure</td><td>Yes</td><td>Atenolol lasts long without kidney function; some patients take it after dialysis, three times a week, as ordered</td></tr>
<tr><td>Combined alpha- and beta-blockers (carvedilol, labetalol)</td><td>Heart failure, coronary disease</td><td>No, not significantly</td><td>Can blunt the heart rate response when pressure falls during the session</td></tr>
<tr><td>Calcium channel blockers (amlodipine, felodipine)</td><td>Widely used, effective when volume is high</td><td>No</td><td>Effect persists through the session</td></tr>
<tr><td>Alpha-blockers (doxazosin, prazosin)</td><td>Added in resistant hypertension</td><td>No</td><td>Avoid in patients with low pressure during dialysis</td></tr>
<tr><td>Hydralazine</td><td>Added in resistant hypertension</td><td>No</td><td>Causes a fast pulse, so it is usually given with a beta-blocker</td></tr>
<tr><td>Minoxidil</td><td>Reserved for hypertension that resists other drugs</td><td>Not extensively</td><td>Causes fluid retention, including fluid around the heart and lungs</td></tr>
</tbody></table></div>
<p>The table follows a review of blood pressure drugs in hemodialysis.[[inrig2010]] Removal also varies with the dialyzer, so check the label or a pharmacist for a specific drug. The European consensus advises choosing agents by comorbidity and by features such as removal by dialysis.[[sarafidis2017]]</p>
<h3>One trial comparing two classes</h3>
<p>The Hypertension in Hemodialysis Patients Treated with Atenolol or Lisinopril (HDPAL) trial randomized 200 patients with hypertension and a thickened left ventricle. Each drug was given three times a week after dialysis. Ambulatory pressure improved equally, though monthly home pressure stayed higher on lisinopril, and a safety board stopped the trial early. Serious cardiovascular events occurred in 28 patients on lisinopril (43 events) and 16 on atenolol (20 events), an incidence rate ratio of 2.36. Admissions for heart failure were also higher with lisinopril (rate ratio 3.13).[[agarwal2014hdpal]] It was one open-label trial stopped early, which tends to exaggerate differences.</p>
<p>At medicine reconciliation, note which drugs were taken and when. A retained drug taken shortly before the session may explain a fall; a dialyzable one may contribute to a rise.[[vanburen2016]] Report it. Module 20 covers dosing.</p>
<p><strong>Low pressure between sessions</strong> has its own causes: too many drugs, a target weight set too low, a failing heart, infection, and autonomic neuropathy. Report the pattern; Module 13 covers a fall during the session.</p>
{{key:Know which of your patient&rsquo;s drugs the dialyzer removes. Report the timing; leave the change to the nephrologist.}}
"""),
        ("rising", "Pressure that rises", "Pressure that rises during dialysis", """
<p>Picture a garden hose that tightens as the flow drops, when it should relax. Normally pressure drifts down as fluid is removed. In patients whose pressure rises, three findings recur: hidden extracellular fluid on bioimpedance despite modest gains, a surge in vascular resistance with little change in cardiac output, and a dialysis fluid sodium above serum sodium.[[vanburen2016]] Sympathetic and renin-angiotensin activity, endothelial dysfunction, and shifts in electrolytes are proposed contributors.[[iatridi2022]] These are associations and proposed mechanisms; no single cause has been proven.</p>
{{fig:pod14_intradialytic_rise}}
<h3>The risk depends on the definition</h3>
<p>In 1,748 new dialysis patients, 12.2% had a systolic rise of more than 10 mm Hg. Each 10 mm Hg rise was associated with a 6% higher hazard of death over two years, but the association was significant only in patients whose pre-dialysis systolic pressure was below 120 mm Hg.[[inrig2009]] In 3,198 patients, a rise of any size in at least 30% of sessions was present in 47% of patients and associated with a hazard ratio for death of 1.32. Rises of 10 or 20 mm Hg in at least 30% of sessions were not significantly associated.[[singh2022]] A meta-analysis of 32 studies and 127,080 patients estimated a pooled prevalence of 26.6%, with very high variation between studies, and a pooled hazard ratio for death of 1.37 from five studies.[[adejumo2024]]</p>
<p>In a Greek cohort of 242 patients, the association with death lost significance after adjustment for 44-hour ambulatory systolic pressure.[[iatridi2023]] All of these studies are observational. Much of the risk may come from high pressure between sessions.</p>
{{formula:<strong>Worked example C (illustrative): classifying the rises.</strong> Six sessions, change in systolic pressure from start to end (post minus pre): +12, +4, &minus;8, +15, +2, &minus;3 mm Hg.<br>Any rise (change of 0 or more): 4 of 6 sessions = 67%.<br>Rise of 10 mm Hg or more: 2 of 6 = 33%.<br>Rise of 20 mm Hg or more: 0 of 6 = 0%.<br>Using the definitions studied by Singh and colleagues, a pattern present in at least 30% of sessions, this patient meets the &ldquo;any rise&rdquo; and &ldquo;10 mm Hg&rdquo; definitions but not the &ldquo;20 mm Hg&rdquo; definition.[[singh2022]]<br><strong>What it tells you:</strong> the label depends on the definition you use. <strong>What it does not tell you:</strong> that this patient&rsquo;s rise causes harm, or what to do about it. The risk data are observational.}}
<h3>What you do at the chair</h3>
{{fig:pod14_rising_pathway}}
<p>Recheck with correct technique and ask about headache, chest pain, breathlessness, confusion, weakness, and vision. If none, continue per protocol and report the pattern; the nephrologist may review the target weight, dialysis fluid sodium, or drug list.[[vanburen2016]] If any, go to the next section.</p>
{{key:A pressure that climbs during dialysis is a clue to hidden fluid, not a reason for a reflex tablet.}}
"""),
        ("emergency", "Emergency or number", "Hypertensive emergency or a high number", """
<p>A smoke alarm is not a fire. The blood pressure number is the alarm. Damage to an organ is the fire.</p>
<p>Very high pressure can overwhelm the brain&rsquo;s protective control of blood flow, causing swelling and confusion (hypertensive encephalopathy), stroke, or bleeding. It loads the left ventricle, causing ischemia or pulmonary edema. It can tear the aorta (dissection) and cause retinal bleeding and optic disc swelling. A hypertensive emergency is high pressure with new or worsening damage to one of these organs.[[bress2024]]</p>
{{fig:pod14_target_organs}}
<h3>What the evidence says</h3>
<p>A 2024 American Heart Association (AHA) scientific statement on the acute care setting describes two groups. A hypertensive emergency involves acute target-organ damage and should be treated swiftly, usually with intravenous medicines, in a closely monitored setting. For a high reading without organ damage, the balance of benefit and harm from starting or increasing treatment is unclear. Clinicians treat about one-third of such readings, and observational studies suggest possible harm.[[bress2024]] A scientific statement is not a graded guideline, and it was written for hospitals, not dialysis units. The 2025 AHA and American College of Cardiology (ACC) guideline replaced the 2017 guideline.[[jones2025]] This module does not restate its thresholds or grades; use those in your unit&rsquo;s protocol.</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>High reading without organ damage</th><th>Hypertensive emergency</th></tr></thead>
<tbody>
<tr><td>What you see</td><td>A high number in a patient who feels well, or who has pain, anxiety, a full bladder, or missed tablets</td><td>A high number with headache and confusion, new weakness or speech change, chest pain, breathlessness with crackles, tearing back pain, or new visual loss</td></tr>
<tr><td>First steps</td><td>Recheck with correct technique after rest. Treat pain and anxiety. Ask about missed medicines and salt intake</td><td>Follow the unit&rsquo;s emergency protocol. Monitor, ECG, oxygen per protocol, brief neurologic examination</td></tr>
<tr><td>Where treated</td><td>Usually in the unit, with the session continuing per protocol</td><td>Usually an emergency room or monitored bed, with intravenous treatment</td></tr>
</tbody></table></div>
<p>Screen every severe reading: symptoms, orientation, speech, limb strength, ECG, saturation, and the fundi if you can.</p>
{{call:Stop and call the attending nephrologist at once for severe hypertension with any sign of target-organ damage: confusion, new weakness or speech change, severe headache, chest pain, tearing back pain, breathlessness with crackles, or new visual loss. Start the unit&rsquo;s emergency protocol and prepare for transfer while you call.}}
{{key:The number raises the question. The organs answer it.}}
"""),
        ("breathless", "Six causes", "The breathless dialysis patient: six causes", """
<p>Picture six doors into the same room. A breathless patient came through one of them. Open each before you decide which.</p>
{{fig:pod14_six_causes}}
<div class="table-wrap"><table>
<thead><tr><th>Door</th><th>Common causes</th><th>First clue at the chair</th><th>Where it is taught</th></tr></thead>
<tbody>
<tr><td>Fluid</td><td>Pulmonary edema from salt and water gain</td><td>Large weight gain, a missed or shortened session, crackles, swelling, worse lying flat, high pressure</td><td>This module</td></tr>
<tr><td>Heart</td><td>Acute coronary syndrome, arrhythmia, valve disease, fluid around the heart</td><td>Chest pain, an irregular or very fast pulse, ECG changes, low pressure with distended neck veins</td><td>Module 15</td></tr>
<tr><td>Lung</td><td>Pneumonia, pleural effusion, asthma, chronic obstructive pulmonary disease</td><td>Fever and cough, dullness at one base, wheeze</td><td>Your medicine training</td></tr>
<tr><td>Clot</td><td>Pulmonary embolism</td><td>Sudden onset, chest pain on breathing, fast pulse, a swollen leg, a clear chest</td><td>Your medicine training</td></tr>
<tr><td>Blood</td><td>Severe anemia</td><td>Pallor, breathlessness on effort, a falling hemoglobin, bleeding</td><td>Module 21</td></tr>
<tr><td>Reaction</td><td>Dialyzer reaction, anaphylaxis, air embolism</td><td>Onset during the session, often in the first minutes; itching, wheeze, flushing; foam in the venous line</td><td>Module 16</td></tr>
</tbody></table></div>
<p>Metabolic acidosis also causes fast breathing, especially after missed sessions.</p>
<h3>Why the examination misleads</h3>
<p>Fluid in the lungs is often silent until late. In a multicenter cohort of 392 hemodialysis patients, lung ultrasound showed moderate to severe congestion in 45%. Of those, 71% had no or only slight symptoms of heart failure.[[zoccali2013]] In the Lung Water by Ultrasound-Guided Treatment (LUST) study, crackles agreed poorly with lung water on ultrasound,[[torino2016]] and the absence of overt signs does not exclude excess fluid.[[georgianos2019]] Module 8 covers lung ultrasound.</p>
<h3>What you do</h3>
<p>Sit the patient upright and stay. Oxygen per protocol, with saturation before and after. Monitor on. A 12-lead ECG, read for ischemia and peaked T waves. Glucose, and potassium per protocol. Then decide which door is likely, and call. More than one can be open at once.</p>
{{key:Breathlessness has six doors. Fluid is the most common in a dialysis unit, but it is never the only one to check.}}
"""),
        ("edema", "Pulmonary edema", "Acute pulmonary edema in the chair", """
<p>The lungs are a sponge the body can no longer wring out. Only the machine can.</p>
<p>Fluid moves across the wall of a lung capillary according to the balance of pressures, the Starling forces. Pressure inside the capillary pushes fluid out. The protein in the plasma holds fluid in. Normally a small amount leaks out, and the lymph vessels carry it away. When pressure in the left atrium rises, pressure in the lung capillaries rises with it. Fluid leaves faster than the lymph vessels can remove it. It fills the tissue between the air sacs, then the air sacs themselves, and oxygen can no longer cross easily.[[hall2021]]</p>
<p>In a dialysis patient, volume gain is the usual cause. A stiff left ventricle turns a small extra volume into a steep rise in filling pressure (Module 4), and ischemia or very high blood pressure adds to the load.</p>
{{fig:pod14_flooded_lung}}
<h3>Why diuretics often do not help</h3>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>Why a diuretic may fail</th><th>What it means for you</th></tr></thead>
<tbody>
<tr><td>No urine output</td><td>A loop diuretic acts on the kidney tubule. With no filtration, there is no urine for it to increase</td><td>Fluid can leave only through the dialyzer</td></tr>
<tr><td>Little urine output</td><td>Diuretics reach their site of action by secretion into the tubule; low kidney blood flow and retained organic acids that compete for the same pathway limit how much arrives</td><td>Any effect is small and slow compared with the fluid to be removed</td></tr>
<tr><td>Meaningful residual urine output</td><td>Diuretics can increase urine and are associated with smaller weight gains in cohort data, which may reflect better residual function rather than the drug</td><td>The attending nephrologist may use one as part of the plan, never as a substitute for fluid removal in pulmonary edema</td></tr>
</tbody></table></div>
<p>The link with smaller weight gains is observational.[[inrig2010]]</p>
<h3>Treatment</h3>
<p>The definitive treatment is fluid removal by ultrafiltration (UF), which the attending nephrologist prescribes.[[daugirdas2015]] Oxygen, sitting upright, vasodilators, and noninvasive ventilation are bridges, used per your unit&rsquo;s protocol or in the emergency room. No comparative study shows whether dialysis in the unit or transfer first is better.</p>
{{formula:<strong>Worked example A (illustrative): mean arterial pressure.</strong> Mean arterial pressure (MAP) = diastolic + (systolic &minus; diastolic) &divide; 3.[[hall2021]]<br>Mang Ernie: 104 + (192 &minus; 104) &divide; 3 = 104 + 29.3 = 133.3 mm Hg.<br><strong>What it tells you:</strong> one number to track the response to first steps. <strong>What it does not tell you:</strong> a target. The site calculator for mean arterial pressure does this arithmetic.}}
{{formula:<strong>Worked example B (illustrative): the fluid to remove and the rate.</strong> Gain = arrival weight &minus; target weight = 74.6 &minus; 70.0 = 4.6 kg, or about 4,600 mL.<br>Rate if all of it were removed in 4 hours = 4,600 mL &divide; (4 h &times; 70 kg) = 16.4 mL/kg/h.<br>In a large cohort, rates above 13 mL/kg/h were associated with higher cardiovascular and overall mortality (Module 8).[[flythe2011]]<br><strong>What it tells you:</strong> removing the whole gain in one standard session would be fast. This is why the attending nephrologist may choose an extra session or isolated ultrafiltration (Module 12) rather than removing everything at once. <strong>What it does not tell you:</strong> the right goal today. That decision and the number belong to the nephrologist. The site calculators for weight gain and fluid removal rate do this arithmetic.}}
<h3>Dialyze now or transfer</h3>
<p>Transfer is favored by saturation that does not improve, tiring breathing, an ischemic ECG, chest pain, low pressure, arrhythmia, or altered consciousness. Dialysis in the unit is favored by an alert patient, stable on oxygen, with a free machine and enough staff. Your protocol sets the thresholds.</p>
{{call:Stop and call the attending nephrologist at once when oxygen saturation does not respond to the first steps, when the work of breathing rises, or when a breathless patient has chest pain, low pressure, an irregular pulse, or altered consciousness. Call for help in the unit and prepare for transfer while you call.}}
{{key:In a patient without urine, only the machine removes fluid from the lungs. Your job is to keep the patient safe until it can.}}
"""),
        ("prevent", "Prevention and call card", "Keeping it from happening again, and the call card", """
<p>The pressure problem lives at home: salt, a missed session, or a target weight that no longer fits.</p>
{{fig:fluid_overview|Fluid builds up between sessions. The bigger the gain, the higher the pressure and the greater the strain on the heart and lungs.}}
<p>Salt and Filipino foods are in Module 23, missed sessions in Module 26, and target weight in Module 8. In the HDPAL trial, a combined strategy of salt restriction, target weight adjustment, and medicines, guided by monthly home readings, improved ambulatory pressure whatever the stiffness of the patient&rsquo;s arteries. Its authors argue for a &ldquo;volume-first&rdquo; approach.[[georgianos2019]] That is an analysis within a trial, not a separate test of the strategy.</p>
<div class="table-wrap"><table>
<thead><tr><th>Ask about</th><th>Question to the patient or family</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Salt</td><td>&ldquo;What did you eat yesterday? Any dried fish, instant noodles, canned goods, bagoong, or patis?&rdquo;</td><td>Salt drives thirst, and thirst drives weight gain</td></tr>
<tr><td>Fluid</td><td>&ldquo;How much do you drink in a day, including soup and coffee?&rdquo;</td><td>Soups and drinks count as fluid</td></tr>
<tr><td>Sessions</td><td>&ldquo;Have you missed or shortened any sessions? What made it hard to come?&rdquo;</td><td>A missed session lengthens the gap and enlarges the gain</td></tr>
<tr><td>Medicines</td><td>&ldquo;Which tablets do you actually take, and at what time?&rdquo;</td><td>Missed doses and poorly timed doses both change pressure</td></tr>
<tr><td>Home readings</td><td>&ldquo;Do you check your pressure at home? May I see your log?&rdquo;</td><td>Home readings show control better than unit readings</td></tr>
<tr><td>Breathing at night</td><td>&ldquo;Can you lie flat? Do you wake up breathless?&rdquo;</td><td>An early sign of fluid in the lungs</td></tr>
</tbody></table></div>
<p>After every emergency, write a note naming the probable cause and the prevention question for the attending nephrologist.</p>
<p>Be exact about the blood in the circuit. Returning it gives back the blood held in the lines and the dialyzer. It is right when the session ends for a cause in the patient and the circuit is sound. It is wrong when the circuit may be the cause: air in the venous line, blood that may be hemolyzed, a suspected dialyzer reaction, or a clotted circuit. Module 16 covers those.</p>
{{flow:Call card: breathless or very high pressure in the chair|Recognize::Breathless at rest, speaking in short phrases, sitting forward, crackles, saturation below your unit&rsquo;s threshold. Or a severe reading with headache, confusion, weakness, speech change, chest pain, or change in vision.|First 2 minutes::Sit the patient upright and stay. Oxygen per protocol. Monitor on. Check airway and consciousness. 12-lead ECG. Bedside glucose. Send potassium per protocol. A brief neurologic examination if the pressure is severe.|Stop dialysis?::If not yet connected, do not connect until the attending nephrologist decides between dialysis now and transfer. If breathlessness began during the session, think first of a dialyzer reaction or air embolism and follow the Module 16 card. If connected for pulmonary edema, continue fluid removal only as the nephrologist orders.|Return the blood?::Yes, per protocol, when the session is stopped or transfer is decided and the circuit is sound. Do NOT return the blood if there is air in the venous line, if the blood may be hemolyzed, if a dialyzer reaction is suspected, or if the circuit may be contaminated or has clotted. Clamp the lines and keep the circuit for inspection.|Call::The attending nephrologist at once, using the Situation, Background, Assessment, Recommendation (SBAR) format from Module 1. Emergency room or transport per protocol for an unstable patient, an ischemic ECG, failing oxygenation, or neurologic signs.|Write::Time of onset. Vital signs and saturation series. Weight against target. Examination. ECG reading. Treatments given, with times and who ordered them. The call: who, when, and what was decided. Disposition.}}
"""),
    ],
    "debrief": ["""
<p><strong>Which causes are most likely?</strong> The fluid door is wide open. Mang Ernie missed a session, gained 4.6 kg, has crackles to mid-lung, swollen ankles, and a high pressure, and he sits forward to breathe. The heart door is next, because overload and ischemia travel together and age can hide chest pain; his ECG lowers but does not remove that worry. Clot, infection, and anemia fit less well, and a reaction is unlikely before connection. The finding that would most change your plan is an ischemic ECG or new chest pain, which shifts him toward transfer. A very high potassium would raise the urgency of dialysis (Module 18).</p>
<p><strong>Is this a hypertensive emergency?</strong> Yes, by definition. He has a very high pressure with acute damage to an organ, the lungs, in the form of pulmonary edema.[[bress2024]] But the driver is volume. A tablet would not remove the fluid and could make removal harder once the machine starts. Where he is treated depends on his stability and your unit&rsquo;s resources, not on the number.</p>
<p><strong>Dialyze or transfer?</strong> You call the attending nephrologist in the Situation, Background, Assessment, Recommendation (SBAR) format. &ldquo;Mr. Garcia, 66, missed Friday, 4.6 kg above target, breathless. Saturation 88% on room air, 91% on oxygen, pressure 192/104, crackles to mid-lung, no chest pain, no new ST change, potassium pending. I think this is pulmonary edema from fluid gain. He is alert and slightly better on oxygen. Dialyze here now, with what goal, or transfer?&rdquo; If dialysis is ordered now, the goal and rate are the nephrologist&rsquo;s; worked example B shows why all 4.6 kg may not come off at once. If he worsens, he goes to the emergency room. You write the items on the call card, plus the prevention question: why he missed the session, and what would help him come.</p>
"""],
    "skills": {"title": "Respiratory assessment, oxygen setup, and home blood pressure teaching",
               "intro": "Perform these steps on a simulated breathless patient in a dialysis chair, and teach home measurement to a colleague playing the patient, while your preceptor observes.",
               "items": [
                   ("Positions the breathless patient upright and stays with the patient.", True),
                   ("Applies oxygen per the unit&rsquo;s protocol and records saturation before and after.", True),
                   ("Attaches the monitor and records respiratory rate, pulse, pressure, and saturation.", False),
                   ("Records a 12-lead ECG within minutes and reads it for ischemia and for signs of high potassium.", True),
                   ("Examines for crackles, wheeze, jugular venous pressure, swelling, and unequal breath sounds, and names the six causes aloud.", False),
                   ("Screens a severe pressure reading for target-organ damage: symptoms, orientation, speech, limb strength, chest pain.", True),
                   ("Checks that the patient is not yet connected, or asks when breathlessness began if the session is running.", False),
                   ("Calls the attending nephrologist with an SBAR report and states the options of dialysis now or transfer.", True),
                   ("States when the blood in the circuit must not be returned.", True),
                   ("Does not give or change maintenance blood pressure medicines without an order.", False),
                   ("Teaches home measurement: rest first, correct cuff size, the non-access arm, timing, and keeping a log, with teach-back.", False),
                   ("Documents events, times, treatments, the call, and the plan.", False),
               ],
               "placement": "For two weeks, collect home blood pressure logs from three patients with high pre-dialysis readings. Average each log, compare it with the unit readings, and present one patient&rsquo;s pattern to your preceptor and the attending nephrologist."},
    "quiz": [
        ("In cohort studies of hemodialysis patients, which readings predicted death?",
         ["Pre-dialysis readings",
          "Home and ambulatory readings",
          "Post-dialysis readings",
          "The lowest reading during the session"], 1,
         "Home and ambulatory systolic pressure predicted mortality; pre- and post-dialysis readings did not."),
        ("Why does a pre-dialysis reading on Monday tend to overstate a patient&rsquo;s usual pressure?",
         ["Dialysis fluid raises pressure overnight",
          "Monday readings are taken on the access arm",
          "It comes at the peak of fluid gain after the long gap, often with a white-coat effect and hurried technique",
          "The pressure is always highest in the morning"], 2,
         "Peak volume, anxiety, and rushed technique push it up."),
        ("Mrs. Reyes has a pre-dialysis reading of 178/96 mm Hg. She feels well and has no headache, chest pain, or neurologic signs. Her home log averages 138 mm Hg systolic. What is the best action?",
         ["Give an extra dose of her blood pressure tablet before connecting",
          "Transfer her to the emergency room",
          "Recheck after rest with a correct cuff, proceed per protocol, and report the pattern",
          "Cancel today&rsquo;s session"], 2,
         "A high reading without organ damage is not an emergency, and her home log suggests the unit number overstates her usual pressure."),
        ("What did the DRIP trial show?",
         ["Lowering target weight by about 1 kg lowered ambulatory systolic pressure without worsening quality of life",
          "Lowering target weight reduced death",
          "Lowering target weight had no effect on pressure",
          "Lowering target weight caused no low-pressure symptoms during dialysis"], 0,
         "Ambulatory systolic pressure fell by about 7 mm Hg; low-pressure symptoms rose. Death was not studied."),
        ("A man takes four blood pressure drugs, and his home pressure stays high. He says he takes them all. What is the most important treatable cause to raise with the attending nephrologist?",
         ["Arterial stiffness",
          "Hidden volume overload",
          "Too little calcium in the dialysis fluid",
          "A drug allergy"], 1,
         "After white-coat effect and missed doses are excluded, volume is the most important treatable cause of resistance."),
        ("What did the BID pilot trial of blood pressure targets in dialysis show?",
         ["The intensive target clearly reduced heart attacks",
          "Both targets gave identical results in every outcome",
          "The trial defined the best target for dialysis patients",
          "A possible safety signal in the intensive arm, in a trial too small to conclude"], 3,
         "Four deaths versus one, with nonsignificant differences in other outcomes."),
        ("In the HDPAL trial, which statement is accurate?",
         ["Lisinopril lowered ambulatory pressure much more than atenolol",
          "Serious cardiovascular events were more frequent with lisinopril, and the trial was stopped early",
          "Atenolol caused more heart failure admissions",
          "The trial proved that beta-blockers suit every dialysis patient"], 1,
         "Pressure improved similarly; events were more frequent with lisinopril."),
        ("A patient&rsquo;s pressure rises from 150 to 172 mm Hg during most sessions. He takes lisinopril each morning. Which drug fact is most relevant to report?",
         ["Lisinopril is removed by dialysis, so its effect may fall during the session",
          "Lisinopril is not removed by dialysis",
          "Lisinopril causes fluid retention",
          "Lisinopril must be stopped on dialysis days"], 0,
         "Most ACE inhibitors are dialyzable; the nephrologist may consider a non-dialyzable agent."),
        ("Which statement about intradialytic hypertension is best supported?",
         ["Every rise of 20 mm Hg doubles the risk of death",
          "It has one agreed definition",
          "Its link with death is observational and may largely reflect high pressure between sessions",
          "Randomized trials show that treating it saves lives"], 2,
         "In one cohort the association lost significance after adjustment for 44-hour ambulatory pressure."),
        ("During a session, Mr. Santos&rsquo;s pressure rises to 196/108 mm Hg. He now has a severe headache and is confused. What do you do?",
         ["Continue and recheck in an hour",
          "Give an oral tablet and continue fluid removal",
          "Raise the fluid removal rate to lower the pressure",
          "Treat it as a possible hypertensive emergency: follow the emergency protocol, call the nephrologist, and prepare for transfer"], 3,
         "Headache with confusion suggests brain injury. Organ damage defines the emergency."),
        ("Which finding defines a hypertensive emergency?",
         ["A systolic reading above the unit&rsquo;s usual range",
          "High pressure with new or worsening target-organ damage",
          "High pressure in a patient who missed tablets",
          "High pressure that does not fall after one tablet"], 1,
         "The number alone does not define the emergency; organ damage does."),
        ("Mrs. Dela Cruz becomes breathless ten minutes after connection. She is itchy and wheezing, and has little fluid on board. What is the most likely door?",
         ["Reaction",
          "Fluid",
          "Blood",
          "Clot"], 0,
         "Early onset with itching and wheeze suggests a dialyzer reaction (Module 16)."),
        ("In a cohort of 392 hemodialysis patients, what proportion of those with moderate to severe lung congestion on ultrasound had no or only slight symptoms?",
         ["About 10%",
          "About 30%",
          "About 50%",
          "About 70%"], 3,
         "71% were asymptomatic or slightly symptomatic."),
        ("Mang Tonyo has no urine output and arrives with pulmonary edema. A colleague suggests a high dose of a loop diuretic instead of dialysis. What is the best reply?",
         ["Diuretics work well in anuric patients",
          "With no filtration, a diuretic has no urine to increase; fluid can be removed only by the dialyzer",
          "Diuretics work only during dialysis",
          "Diuretics are effective if given with oxygen"], 1,
         "A loop diuretic acts on the tubule. Without filtration there is no urine for it to increase."),
        ("A patient with pulmonary edema is connected and dialysis is running. His saturation keeps falling and he develops chest pain with new ST depression. The nephrologist advises transfer. What happens to the blood in the circuit?",
         ["Return it per protocol, since the circuit is sound and the cause lies in the patient",
          "Discard it, because blood is never returned in an emergency",
          "Keep the patient connected during transfer",
          "Return it only after the ECG normalizes"], 0,
         "The cause lies in the patient and the circuit is sound. Blood is not returned with air, hemolysis, a reaction, or a contaminated or clotted circuit."),
    ],
    "terms": [("Interdialytic period", "The time between two dialysis sessions."),
              ("Ambulatory blood pressure monitoring", "Automatic readings at set intervals over a day or more, often the 44 hours between sessions in dialysis studies."),
              ("White-coat effect", "A higher reading in a clinical setting than at home, caused by the setting itself."),
              ("Intradialytic hypertension", "A rise in blood pressure from the start to the end of a dialysis session. Definitions differ."),
              ("Hypertensive emergency", "High blood pressure with new or worsening damage to a target organ."),
              ("Target-organ damage", "Injury from high pressure to the brain, heart, lungs, aorta, or eyes."),
              ("Pulmonary edema", "Fluid that has leaked from the lung capillaries into the tissue and air sacs of the lung."),
              ("Starling forces", "The balance of pressure pushing fluid out of a capillary and plasma protein holding it in."),
              ("Dialyzable drug", "A medicine that crosses the dialyzer membrane, so a session removes part of it."),
              ("Mean arterial pressure", "The average pressure in the arteries over one heartbeat, estimated as diastolic plus one-third of the pulse pressure.")],
    "readings": [("managing-hypertension.html", "Blood pressure in kidney disease, including home measurement and the drug classes."),
                 ("hd-volume-bp-tolerance-clinician.html", "How volume, blood pressure, and tolerance of fluid removal connect in hemodialysis."),
                 ("heart-failure-ckd.html", "Heart failure in kidney disease, the background to pulmonary edema in the chair.")],
    "calcs": ["calc-bp-map.html", "calc-ufr-ceiling.html", "calc-idwg-fluid.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
