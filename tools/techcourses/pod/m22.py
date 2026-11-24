# -*- coding: utf-8 -*-
"""Physician on Duty, Module 22: Diabetes on Dialysis.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty and a nurse at the chair of a sweaty, drowsy older Filipino man during dialysis. The nurse holds a glucose meter, and a meal tray beside the chair is untouched.",
    "objectives": [
        "Explain why insulin needs fall and low blood glucose becomes more likely as kidney function is lost.",
        "Interpret hemoglobin A1c (HbA1c) with caution in a dialysis patient, name the causes of a falsely low or high value, and describe what continuous glucose monitoring (CGM) and the glucose management indicator (GMI) add.",
        "Recognize and respond to low blood glucose around a session per your unit&rsquo;s protocol, and name the patients at highest risk.",
        "Sort the main diabetes medicine classes into those used, adjusted, or avoided on dialysis, with the guideline status of each.",
        "Perform a focused diabetic foot examination at the chair and decide which findings need same-day escalation.",
        "Recognize the eye, nerve, and stomach complications of diabetes that change how a dialysis session runs.",
    ],
    "big": """
{{plain:Picture a bathtub with a faucet and a drain. Insulin pours in from the faucet, and the kidney is part of the drain. In kidney failure the drain is half closed, so the same amount of insulin stays in the tub longer and its level runs high.}}
<p>The picture has a limit. The kidney is not only a drain. Between meals it is also a second faucet that pours glucose into the blood, and in kidney failure that faucet is turned down as well. Uremia also makes muscle and fat resist insulin, which pushes glucose up. The result is a wide swing in both directions, with lows that are easy to miss.[[galindo2020]]</p>
{{cards:Key terms for this module|Hemoglobin A1c (HbA1c)::The share of hemoglobin that carries glucose. It reflects average glucose over the life of the red cells, usually about three months.|Hypoglycemia::Low blood glucose. Studies in dialysis patients often use a value below 70 mg/dL.|Hypoglycemia unawareness::A low glucose without the usual warning symptoms of sweating, tremor, and hunger.|Counter-regulation::The hormones, such as glucagon, epinephrine, cortisol, and growth hormone, that raise glucose when it falls.|Continuous glucose monitoring (CGM)::A small sensor under the skin that reads glucose in the tissue fluid every few minutes.|Glucose management indicator (GMI)::An estimate of HbA1c calculated from the average CGM glucose.|Sulfonylurea::A tablet class, such as glibenclamide, that makes the pancreas release insulin whatever the glucose level.}}
<p>Diabetes is a leading cause of kidney failure, so many patients on your floor have it. Most of them dialyze through a session without a glucose problem. A few have a low that is silent, that mimics a falling pressure or a stroke, or that comes after they leave. Your work is to find the patients at risk, catch a low early per your unit&rsquo;s protocol, judge glucose control with the right tools, and use the hours in the chair to look at the feet.</p>
""",
    "case": {"title": "Sugar of 45 at hour two", "html": """
<p>Mr. Rodolfo Dimaculangan, 61, has had type 2 diabetes for 18 years. He dialyzes on Mondays, Wednesdays, and Fridays through a right arm fistula. Today is Wednesday. He takes premixed insulin twice a day. According to his daughter, he also takes &ldquo;the yellow tablet&rdquo; that a clinic doctor gave him last month. He skipped breakfast because he felt full and bloated, but he took his morning insulin.</p>
<p>At hour two, the nurse, Ms. Liza Panganiban, calls you to his chair. He is sweaty and slow to answer. His blood pressure has fallen from 150/80 to 112/64 mm Hg. His capillary glucose is 45 mg/dL (illustrative). Ms. Panganiban has already given the oral glucose that the unit&rsquo;s hypoglycemia protocol allows, and she has slowed fluid removal. His last HbA1c, from two months ago, was 6.1% (illustrative). His chart says &ldquo;well controlled.&rdquo;</p>
""", "questions": ["What do you do in the next ten minutes, in what order, and when do you recheck?",
                  "Why was his HbA1c a poor guide to his risk, and what would you look at instead?",
                  "What will you tell the attending nephrologist about his medicines and his dialysis day?"]},
    "sections": [
        ("insulin", "Why sugar falls lower", "Why insulin lasts longer and sugar falls lower", """
<p>Start with normal physiology. The pancreas releases insulin into the portal vein. The liver removes much of it on the first pass, and the kidney removes much of what reaches the general circulation. The kidney filters insulin and breaks it down in the tubule cells. Injected insulin skips the liver altogether, so the kidney matters even more for a patient who injects.[[galindo2020]]</p>
<p>The kidney also makes glucose. Between meals and overnight, the cortex of the kidney builds new glucose from lactate, glutamine, and glycerol, a process called gluconeogenesis. The liver is the main source, but the kidney adds a real share.[[galindo2020]]</p>
{{fig:pod22_insulin}}
<h3>What breaks in kidney failure</h3>
<p>Each step in the chain weakens, and the effects add together.[[galindo2020]]</p>
<div class="table-wrap"><table>
<thead><tr><th>What changes</th><th>What it does to glucose</th><th>What you may notice</th></tr></thead>
<tbody>
<tr><td>The kidney clears less insulin, and uremia slows insulin breakdown in other tissues</td><td>Each dose acts longer and harder</td><td>A patient whose insulin needs have fallen as kidney function declined. Lows late in the day or overnight</td></tr>
<tr><td>Kidney gluconeogenesis is lost</td><td>Less glucose enters the blood between meals</td><td>Lows after a skipped meal or a long fast</td></tr>
<tr><td>Counter-regulatory hormone responses are blunted</td><td>A low is corrected more slowly</td><td>A low that recurs after treatment</td></tr>
<tr><td>Uremia causes insulin resistance in muscle and fat</td><td>Glucose rises after meals</td><td>Highs after meals and wide swings across the day</td></tr>
<tr><td>Drugs or their active products are cleared by the kidney</td><td>Sulfonylureas and their breakdown products build up</td><td>A low that lasts many hours</td></tr>
</tbody></table></div>
<p>These mechanisms come from a review of glycemic management in advanced chronic kidney disease (CKD) and rest on established physiology, not trials.[[galindo2020]] A patient may run high after meals and low before dialysis in the same week.</p>
<h3>What you do with this</h3>
<p>At the start of your shift, read the medication list. Mark every patient who takes insulin or a sulfonylurea, the two classes behind most serious lows. Expect insulin needs to be lower than the old regimen suggests. Never change a standing insulin order yourself. When you see a pattern of lows or highs, report it to the attending nephrologist with the values and times.</p>
{{key:Without kidneys, insulin stays longer and the body makes less glucose of its own. Expect lows, not only highs.}}
"""),
        ("dialysate", "The dialysate and glucose", "What the dialysate does to blood glucose", """
<p>Think of the dialysis fluid as a sea that the blood touches again and again for four hours. Small molecules in the blood drift toward the level in that sea. Glucose is small, so it diffuses (Module 5) toward the glucose concentration of the dialysis fluid.</p>
{{fig:pod22_dialysate}}
<p>The picture has a limit. Blood glucose does not stop at the level of the bath. Red cells take up glucose during treatment, and insulin given before the session is still driving glucose into muscle while the dialyzer removes it from the blood.[[galindo2020]] The result is that glucose can fall below the bath level.</p>
<h3>What the studies show</h3>
<p>Burmeister and colleagues dialyzed 20 patients with type 2 diabetes against three baths in turn: glucose-free, 55 mg/dL, and 90 mg/dL. Hypoglycemia, defined as a value below 70 mg/dL, occurred only with the glucose-free and the low-glucose baths. It occurred mainly in patients whose glucose was lower before dialysis.[[burmeister2015]] This was a small crossover study, so it suggests a pattern rather than proving one.</p>
<p>Hayashi and colleagues placed continuous sensors on 98 patients with type 2 diabetes who dialyzed against baths containing 100, 125, or 150 mg/dL glucose. Sensor glucose fell steadily during the session at every bath concentration. In half of the patients the lowest value fell below the bath concentration. Twenty-one percent had hemodialysis-related hypoglycemia, defined as a sensor value below 70 mg/dL during dialysis or between the end of dialysis and the next meal. Every one of those episodes was without symptoms.[[hayashi2021]] The study was observational and tested no change in practice. It shows that a glucose-containing bath does not make the session safe by itself.</p>
<h3>What you do with this</h3>
<p>Know the glucose concentration of the dialysis fluid your unit uses, and whether it is the same on every machine. Know when your unit&rsquo;s protocol calls for a glucose check: before the session, when symptoms appear, and before the patient goes home. The lowest value may come after the patient leaves.</p>
{{key:A glucose-containing bath lowers the risk of a low in the chair. It does not remove it, and the low may come after the patient leaves.}}
"""),
        ("hypo", "Low sugar in the chair", "Low sugar in the chair: recognize, respond, prevent", """
<p>A smoke alarm with a dead battery stays silent during a fire. Hypoglycemia unawareness works the same way. Normally a falling glucose triggers epinephrine, which causes sweating, tremor, a fast pulse, and hunger. These are the warning symptoms. Autonomic neuropathy damages the nerves that carry the signal. Beta-blockers mute the response.</p>
<p>The picture has a limit. The brain still feels the low even when the alarm is silent. Starved of glucose, it produces neuroglycopenic signs: confusion, slow speech, drowsiness, odd behavior, weakness on one side, or a seizure. In the chair these are easy to mistake for something else.</p>
{{fig:idh|A falling pressure and a falling glucose can look alike in the chair: yawning, sweating, a quiet patient. Check both.}}
<p>Sweating, yawning, and a quiet patient look like a falling pressure (Module 13). Slurred speech or one-sided weakness looks like a stroke (Module 18). Drowsiness looks like &ldquo;tired after dialysis.&rdquo; A fingerstick settles each in two minutes, and a low and a falling pressure can occur together.</p>
<p>In the sensor study, every low during or after dialysis was silent.[[hayashi2021]] The decision to check cannot wait for classic symptoms.</p>
<h3>What the guideline says about monitoring</h3>
<p>In the Kidney Disease: Improving Global Outcomes (KDIGO) 2022 diabetes guideline, practice point 2.1.4 (ungraded) states that daily glycemic monitoring with CGM or self-monitoring of blood glucose may help prevent hypoglycemia when drugs that cause hypoglycemia are used. Practice point 2.1.5 (ungraded) prefers drugs with a lower risk of hypoglycemia for patients who do not monitor daily.[[kdigo_dm2022]]</p>
{{flow:Dialysis-day sugar plan|Before the session::Identify patients on insulin or a sulfonylurea. Ask about today&rsquo;s meals and the last insulin dose.|Check the risk factors::Use the walk-through below.|Watch::Treat sweating, drowsiness, confusion, an unexplained fall in pressure, or a patient who is &ldquo;not himself&rdquo; as a possible low.|Check::Capillary glucose from the hand without the access.|Treat per protocol::Follow your unit&rsquo;s hypoglycemia protocol, including the recheck interval.|Record::Use the card below.|Tell the nephrologist::Report every low the same day.}}
{{formula:<strong>Decision walk-through, illustrative. No score is validated.</strong> At the start of a session, ask five questions. (1) On insulin or a sulfonylurea? (2) Missed a meal today? (3) Pre-dialysis glucose lower than usual for this patient? (4) Known unawareness, or taking a beta-blocker? (5) Glucose-free or low-glucose bath? Each &ldquo;yes&rdquo; raises your vigilance and the frequency of checks your protocol allows.}}
<p>The factors in this walk-through come from the dialysate studies and the review of mechanisms.[[burmeister2015]][[hayashi2021]][[galindo2020]] The count tells you where to look first. It is not a probability, and a patient with no factor can still have a low.</p>
<h3>After a low</h3>
<p>A low from a sulfonylurea or a long-acting insulin can return hours after the first correction, because the drug is still acting.[[galindo2020]] The patient should not leave the unit until the recheck your protocol requires is normal and the attending nephrologist has agreed to the plan.</p>
{{cards:What to write after a low|Time and value::The time of the first reading and the meter value.|Last insulin::Type, time, and amount, from the patient or the chart.|Last meal::When and what, or that the meal was skipped.|Treatment::What was given under the protocol, and when.|Recheck::Each repeat value and its time.|Who was told::The attending nephrologist, the time of the call, and the advice received.}}
{{call:Stop and call the attending nephrologist when a low does not correct with the steps of your protocol, when a low comes with a seizure, a new neurologic sign, or reduced consciousness (follow Module 18 for the emergency), when lows recur across sessions, or when a patient will travel home alone or drive after a low.}}
{{key:Check the glucose of any patient on insulin or a sulfonylurea who is drowsy, sweaty, confused, or has an unexplained fall in pressure. Do not wait for classic symptoms.}}
"""),
        ("hba1c", "Why HbA1c misleads", "Why HbA1c misleads, and what to use beside it", """
<p>Think of HbA1c as a stain on red cells. Glucose sticks to hemoglobin slowly and permanently, so the stain builds up over each cell&rsquo;s life. If the cells are young, they have had less time to stain, and the reading is light even when glucose has been high.</p>
<p>The picture has a limit. Young cells are only one of several distortions in kidney failure, and some push the other way.[[galindo2020]][[peacock2008]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Factor</th><th>Direction of bias</th><th>Mechanism</th></tr></thead>
<tbody>
<tr><td>Shortened red-cell survival in uremia</td><td>Falsely low</td><td>Cells are removed before they gather a full stain</td></tr>
<tr><td>Erythropoiesis-stimulating agent (ESA) therapy</td><td>Falsely low</td><td>The marrow releases many new, lightly stained cells</td></tr>
<tr><td>Intravenous iron</td><td>Falsely low</td><td>Iron allows a burst of new cells</td></tr>
<tr><td>Iron deficiency without treatment</td><td>Falsely high</td><td>Older cells stay in circulation longer</td></tr>
<tr><td>Carbamylation of hemoglobin by urea</td><td>Falsely high with some laboratory methods</td><td>A urea product binds hemoglobin and can be read as glycated hemoglobin</td></tr>
</tbody></table></div>
<p>Peacock and colleagues compared 258 diabetic hemodialysis patients with 49 diabetic controls. In the dialysis patients, HbA1c rose with the hemoglobin level and fell as the ESA dose rose. HbA1c underestimated glucose control. Glycated albumin, a marker based on a blood protein, was not affected.[[peacock2008]] The study was cross-sectional and cannot give the size of the bias in one patient. Glycated albumin has its own problems. It is affected by protein loss and is not validated against outcomes.[[galindo2020]]</p>
{{fig:pod22_camera}}
<h3>What HbA1c is associated with in dialysis patients</h3>
<p>The Dialysis Outcomes and Practice Patterns Study (DOPPS) followed 9,201 diabetic hemodialysis patients in 12 countries. The association between HbA1c and death was U-shaped. Compared with an HbA1c of 7.0% to 7.9%, the adjusted hazard ratio was 1.35 for values below 5% and 1.38 for values of 9.0% or higher.[[ramirez2012]] The study was observational. A very low HbA1c may mark poor nutrition, frequent lows, or falsely low readings, and the study does not show that changing HbA1c changes survival.</p>
<h3>What the guideline says</h3>
<p>The KDIGO 2022 guideline makes four statements that apply here.[[kdigo_dm2022]] Recommendation 2.1.1 (1C) uses HbA1c to monitor control in diabetes and CKD. Practice point 2.1.2 (ungraded) states that the accuracy and precision of HbA1c decline in advanced CKD, especially in patients on dialysis, in whom its reliability is low. Practice point 2.1.3 (ungraded) states that a GMI derived from CGM can be used when HbA1c does not agree with measured glucose or symptoms. Recommendation 2.2.1 (1C) gives an individualized HbA1c target from below 6.5% to below 8.0%, but only for patients not treated with dialysis.</p>
<p>No guideline gives an HbA1c target for dialysis patients, and no trial has tested one. Galindo and colleagues suggest, from observational data, that a range of 7% to 8% appears most favorable in advanced CKD.[[galindo2020]] That is an inference, not a tested target, and targets belong to the attending nephrologist.</p>
<h3>Worked example 1: HbA1c to estimated average glucose</h3>
<p>The A1c-Derived Average Glucose (ADAG) study derived an equation that converts HbA1c to an estimated average glucose (eAG). It studied 507 people with and without diabetes. It did not study people with kidney failure.[[nathan2008]] The site&rsquo;s eAG calculator (calc-eag-hba1c) performs this conversion.</p>
{{formula:<strong>Illustrative calculation.</strong> ADAG equation: estimated average glucose (mg/dL) = 28.7 &times; HbA1c (%) &minus; 46.7.<br>HbA1c 6.1%: 28.7 &times; 6.1 = 175.07. Then 175.07 &minus; 46.7 = 128.4 mg/dL.<br>The patient&rsquo;s glucose log averages 210 mg/dL (illustrative). The HbA1c predicts an average about 80 mg/dL lower than the log shows.}}
<p>The gap tells you that the two measures disagree. In a dialysis patient on an ESA, the more likely explanation is an HbA1c biased low by young red cells, not a wrong glucose log.[[peacock2008]][[galindo2020]] The number does not tell you what the patient&rsquo;s true average is, and it does not set a target.</p>
<h3>What you do with this</h3>
<p>When HbA1c and the glucose readings disagree, believe the readings first and report the disagreement. Do not use a &ldquo;good&rdquo; HbA1c alone to call control good.</p>
{{key:In a dialysis patient, a &ldquo;good&rdquo; HbA1c can hide high sugars, and a low one can be a warning, not a success.}}
"""),
        ("cgm", "Glucose sensors", "Continuous glucose monitoring in dialysis patients", """
<p>A fingerstick is one photograph. A continuous sensor is a security camera. It shows when lows happen and whether they cluster on dialysis days.</p>
<p>The picture has a limit. A sensor reads glucose in the fluid around cells under the skin, which lags behind blood by several minutes. During dialysis, fluid removal shifts water out of the tissues, and in theory this could distort the reading. Accuracy must be tested, not assumed.[[villard2022]]</p>
<h3>What the accuracy studies show</h3>
<p>Accuracy is usually reported as the mean absolute relative difference (MARD) between the sensor and a laboratory glucose. A lower MARD means closer agreement. Error grids sort readings by whether the difference would mislead treatment.</p>
<div class="table-wrap"><table>
<thead><tr><th>Study</th><th>Patients and device</th><th>Main finding</th></tr></thead>
<tbody>
<tr><td>ALPHA, United Kingdom[[avari2023]]</td><td>40 adults on hemodialysis. Dexcom G6 and FreeStyle Libre 1 worn together</td><td>MARD 22.7% for the G6 and 11.3% for the Libre 1. Error-grid zones A and B held 98.9% and 99.8% of values</td></tr>
<tr><td>ALPHA-2, United Kingdom[[avari2025]]</td><td>10 adults. Dexcom G7</td><td>MARD 10.4% against laboratory glucose. 99.7% of pairs in zones A and B</td></tr>
<tr><td>Villard and colleagues, United States[[villard2022]]</td><td>20 participants. A factory-calibrated sensor over 181 days</td><td>MARD 13.8% to 14.4%. Median time in the range of 70 to 180 mg/dL only 38.5%</td></tr>
<tr><td>Narasaki and colleagues, United States[[narasaki2024]]</td><td>31 hospitalized hemodialysis patients. Dexcom G6</td><td>MARD about 20%, with sensor readings about 15 mg/dL higher than blood on average. Nearly all values in error-grid zones A and B</td></tr>
</tbody></table></div>
<p>These small studies each test one device, and accuracy differs by device. The Dexcom G6 agreed least well with laboratory glucose in the ALPHA study, and in the Narasaki study it read about 15 mg/dL higher than blood on average, which could hide a low.[[avari2023]][[narasaki2024]] Most readings fell in the error-grid zones that would not mislead treatment. No trial has shown that CGM reduces lows, admissions, or deaths in dialysis patients.[[narasaki2024]]</p>
<h3>Worked example 2: CGM mean glucose to GMI</h3>
<p>The GMI converts the average sensor glucose into a number on the HbA1c scale. Bergenstal and colleagues introduced the term and its equation.[[bergenstal2018]] KDIGO practice point 2.1.3 (ungraded) allows the GMI to index glycemia when HbA1c and measured glucose disagree.[[kdigo_dm2022]]</p>
{{formula:<strong>Illustrative calculation.</strong> GMI (%) = 3.31 + 0.02392 &times; mean sensor glucose (mg/dL).<br>Mean sensor glucose 190 mg/dL: 0.02392 &times; 190 = 4.545. Then 3.31 + 4.545 = 7.9%.<br>Laboratory HbA1c in the same period: 6.4% (illustrative). The difference is 7.9 &minus; 6.4 = 1.5 percentage points.}}
<p>A gap of this size says that the HbA1c is probably understating this patient&rsquo;s glucose. It does not say which number is the target, and the GMI equation was derived in people without kidney failure.[[bergenstal2018]] Report the discordance to the attending nephrologist. Do not choose a target.</p>
<h3>What you do with a sensor reading</h3>
<p>If a patient wears a sensor and it shows a low, or the patient has symptoms, confirm with a fingerstick before you act, per your unit&rsquo;s protocol. Ask your Medical Director whether the unit accepts sensor readings for decisions and where a sensor may be worn. Keep a sensor off the access arm unless your unit&rsquo;s policy says otherwise. That arm is reserved for cannulation and access care.</p>
{{key:A sensor shows patterns a single test cannot. Confirm any low or symptomatic reading with a fingerstick before you act.}}
"""),
        ("drugs", "Diabetes medicines", "Which diabetes medicines are used, adjusted, or avoided", """
<p>Picture a traffic-light card for diabetes medicines. Green is generally used, yellow adjusted, and red avoided. The picture has a limit. The colors below are for a patient on dialysis. Many sit in a different color in earlier CKD. Module 20 covers the general rules for prescribing without kidneys.</p>
<p>Three things decide the color. A drug or its active products may build up without kidney clearance. A drug that works in the kidney loses its effect when filtration stops. A drug that lowers glucose whatever the glucose level causes lows, and that risk rises when insulin clearance and kidney gluconeogenesis are lost.[[galindo2020]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Class</th><th>Kidney issue on dialysis</th><th>KDIGO 2022 statement and grade</th><th>Flag for the nephrologist</th></tr></thead>
<tbody>
<tr><td>Insulin</td><td><strong>Green:</strong> generally used, with lower needs and close monitoring. Cleared more slowly. Needs usually fall. Main cause of lows</td><td>Practice point 4.2.4 (ungraded): insulin or sulfonylurea doses may need reduction when a glucagon-like peptide-1 receptor agonist (GLP-1 RA) is added</td><td>Any low, any skipped-meal pattern, any regimen not reviewed since dialysis began</td></tr>
<tr><td>Sulfonylureas, such as glibenclamide (glyburide)</td><td><strong>Red</strong> for glibenclamide and other long-acting agents. Drug and active products build up. Lows may last many hours</td><td>Practice point 4.2.4 (ungraded), as above</td><td>Any sulfonylurea on a dialysis patient&rsquo;s list, especially a long-acting one</td></tr>
<tr><td>Metformin</td><td><strong>Red:</strong> avoided. Cleared by the kidney. Builds up without kidney function</td><td>Recommendation 4.1.1 (1B) applies at an estimated glomerular filtration rate (eGFR) of 30 mL/min/1.73 m&sup2; or more. The guideline algorithm stops metformin below 30</td><td>Metformin on a dialysis patient&rsquo;s list</td></tr>
<tr><td>Sodium-glucose cotransporter 2 (SGLT2) inhibitors</td><td><strong>Red:</strong> stopped at dialysis start. Act in the kidney tubule. Little glucose effect without filtration</td><td>Recommendation 1.3.1 (1A) applies at eGFR 20 or more. Practice point 1.3.6 (ungraded): continue below 20 unless not tolerated or kidney replacement therapy is started</td><td>An SGLT2 inhibitor still on the list after dialysis began</td></tr>
<tr><td>GLP-1 RA</td><td><strong>Yellow:</strong> specialist decision. Slow the stomach and cause nausea. Some are not recommended at very low kidney function</td><td>Recommendation 4.2.1 (1B): a long-acting GLP-1 RA when targets are not met on metformin and an SGLT2 inhibitor</td><td>Nausea, poor intake, or a new start by another doctor</td></tr>
<tr><td>Dipeptidyl peptidase-4 (DPP-4) inhibitors</td><td><strong>Yellow:</strong> used with adjustment. Kidney clearance differs by agent, so the dose depends on which one</td><td>No separate graded statement for dialysis patients. The dose depends on the agent</td><td>Check the agent and dose against your unit&rsquo;s drug reference</td></tr>
</tbody></table></div>
<p>These statements come from the KDIGO guideline. A joint American Diabetes Association (ADA) and KDIGO consensus report, which is not graded, aligned the two organizations on them.[[kdigo_dm2022]][[deboer2022]]</p>
<h3>What the evidence does not cover</h3>
<p>The large trials behind the SGLT2 inhibitor and GLP-1 RA statements showed cardiovascular and kidney benefits in patients with CKD who were not on dialysis. None of them enrolled dialysis patients for these outcomes. KDIGO&rsquo;s practice point on SGLT2 inhibitors says to stop them when kidney replacement therapy starts.[[kdigo_dm2022]] The site&rsquo;s SGLT2 inhibitor calculator (calc-sglt2i-eligibility) shows the eGFR bands in these statements, and the metformin calculator (calc-metformin-ckd-safety) shows why metformin is not used on dialysis.</p>
{{formula:<strong>Worked example 4, decision walk-through, illustrative.</strong> A new patient&rsquo;s list contains premixed insulin, glibenclamide, metformin, sitagliptin, and empagliflozin.<br>Metformin: Recommendation 4.1.1 (1B) applies at eGFR 30 or more, and the algorithm stops it below 30. Flag.<br>Empagliflozin, an SGLT2 inhibitor: practice point 1.3.6 says continue until kidney replacement therapy starts. Dialysis has started. Flag.<br>Glibenclamide and premixed insulin: both cause lows, and glibenclamide builds up. Practice point 4.2.4 applies if a GLP-1 RA is added. Flag both.<br>Sitagliptin, a DPP-4 inhibitor: the dose depends on kidney function. Check against the unit&rsquo;s drug reference. Flag.<br>Output: five flags for the attending nephrologist. No drug is started, stopped, or changed by you.}}
<h3>What you do with this</h3>
<p>At medication reconciliation (Module 20), flag the drugs in the last column and any diabetes medicine started by another doctor. Do not start, stop, or change doses. Send the list to the attending nephrologist, with any low from today.</p>
{{key:In a dialysis patient, the diabetes medicine most likely to cause harm today is the one that causes lows: insulin or a sulfonylurea.}}
"""),
        ("complications", "Feet, eyes, nerves, stomach", "Feet, eyes, nerves, and stomach", """
<p>Four hours in a chair, three times a week, is the most regular foot clinic most of these patients will ever attend.</p>
<p>The picture has a limit. Your job at the chair is to find a problem early and hand it to the right person the same day.</p>
<h3>Why the diabetic foot on dialysis is so fragile</h3>
<p>Three processes combine. Neuropathy removes the feeling of pain, so a stone in a shoe or a tight sandal wears a hole without complaint. Peripheral artery disease narrows the arteries, so a small wound does not get the blood it needs to heal. Calcification of the artery wall, common in kidney failure, makes the vessels stiff and the pulse hard to judge. Kidney failure adds poor healing and infection.</p>
<p>Ndip and colleagues examined 466 diabetic dialysis patients in the United Kingdom and the United States. Twelve percent had an active foot ulcer. Seventy-nine percent had neuropathy, 57% had peripheral artery disease, 34% had a past ulcer, and 18% had a prior amputation. Ninety-five percent were at high risk of foot complications.[[ndip2010]] The study was cross-sectional.</p>
<p>Lavery and colleagues followed 150 diabetic patients on dialysis and 150 diabetic patients with a past foot ulcer for 30 months. Foot ulcers occurred at the same rate in both groups. Amputations occurred at 58.0 per 1,000 person-years in the dialysis group and 13.3 in the ulcer-history group, as reported. Foot-related admissions were also more frequent in the dialysis group: 32.9% versus 14.0%.[[lavery2015]] This observational cohort from one health plan suggests that dialysis patients lose limbs more often once an ulcer appears.</p>
{{fig:pod22_footcheck}}
{{flow:Foot check at the chair|Look::Shoes and socks off. Check the top, sole, and heel of both feet for wounds, calluses, blisters, and color change.|Between the toes::Look for cracks, moist white skin, and fungal infection.|Pulses and warmth::Feel the pulses on the top of the foot and behind the inner ankle bone. Compare the warmth of both feet.|Sensation::Use your unit&rsquo;s tool, such as a nylon monofilament, if it uses one.|Footwear::Look inside the shoes for stones and rough seams.|Record and escalate::Compare with the last check. Escalate per the box below.}}
{{fig:pod22_footflags}}
{{call:Stop and call the attending nephrologist now for a foot colder or paler than the other, a newly blue toe, or fever with a foot wound. Call the same day for a new ulcer, a black toe, spreading redness, or pus.}}
<p>Do the check at the interval your unit sets.</p>
<h3>Eyes, nerves, and stomach</h3>
<p>Advanced diabetic eye disease can carry fragile new vessels. Ask about recent eye bleeding, laser treatment, or sudden visual loss, and report it, because the heparin plan belongs to the nephrologist (Module 19). Autonomic neuropathy blunts the vessel and pulse response to fluid removal (Module 13) and mutes the warning symptoms of a low.</p>
{{fig:pod22_stomach}}
<p>Gastroparesis needs a closer look. Insulin given with breakfast expects the meal&rsquo;s glucose within an hour or two. A slow stomach holds the food while the dialyzer removes glucose. The patient can be low in the chair and high in the evening when the meal finally empties. A meal during dialysis is reasonable for many patients and is supported by a nutrition consensus, but it can also lower the pressure.[[kistler2018]] Meal and insulin timing is a question for the attending nephrologist and the dietitian.</p>
{{key:Look at both feet with the shoes and socks off. A wound found today is a limb that can still be saved.}}
"""),
    ],
    "debrief": ["""
<p><strong>What do you do in the next ten minutes?</strong> Ms. Panganiban has given the oral glucose the protocol allows and slowed fluid removal. You go to the chair and check that Mr. Dimaculangan responds, can swallow safely, and is breathing comfortably. If he could not, Module 18 would apply. You recheck his pressure and count his pulse. You ask for a repeat glucose at the interval the protocol sets, and you stay until it is back in range. The fall in pressure follows Module 13. You call the attending nephrologist and agree on the rest of the session. Before he leaves, his final check must be normal, he must have eaten, and he must not travel alone.</p>
<p><strong>Why was his HbA1c a poor guide?</strong> An HbA1c of 6.1% converts to an estimated average glucose of about 128 mg/dL by the ADAG equation, but that equation was not derived in kidney failure. If he receives an ESA or iron, his red cells are young and lightly stained, so the HbA1c reads low. A low HbA1c in a patient on insulin and a sulfonylurea can also mean frequent lows, not good control. Look instead at his meter log or sensor report and the record of lows on dialysis days.</p>
<p><strong>What will you tell the attending nephrologist?</strong> Use the Situation, Background, Assessment, Recommendation (SBAR) format from Module 1: the low, the treatment, the rechecks, and the fall in pressure. Say that he took his premixed insulin but skipped breakfast because he felt full and bloated, which may point to a slow stomach. Ask the family to bring the &ldquo;yellow tablet.&rdquo; If it is a sulfonylurea such as glibenclamide, the low may return for hours. Flag the HbA1c as unreliable. Each change is the nephrologist&rsquo;s decision.</p>
"""],
    "skills": {"title": "Glucose check and diabetic foot examination at the chair",
               "intro": "Perform these steps on a patient at the chair, or on a colleague playing the patient, while your preceptor observes and plays the nurse.",
               "items": [
                   ("Identifies from the chart which patients take insulin or a sulfonylurea.", True),
                   ("Asks about today&rsquo;s meals and the time and amount of the last insulin dose before the session.", False),
                   ("Performs a capillary glucose check with correct technique on the hand without the access.", True),
                   ("Recognizes neuroglycopenic signs that mimic a falling pressure or a stroke, and states why a glucose check comes first.", False),
                   ("Applies the unit&rsquo;s hypoglycemia protocol in the correct order and rechecks at the interval it sets, without quoting an amount from memory.", True),
                   ("Documents the time, value, symptoms, treatment, recheck, and notification.", False),
                   ("Removes shoes and socks and inspects both feet, including the soles, heels, and between the toes.", False),
                   ("Palpates the foot pulses and compares the warmth of the two feet.", False),
                   ("Tests protective sensation with the unit&rsquo;s tool, if the unit uses one.", False),
                   ("Classifies the findings and escalates any red-flag finding to the attending nephrologist the same day.", True),
                   ("Explains to the patient, in plain Filipino or English, one practical way to avoid a low on dialysis days.", False),
               ],
               "placement": "For two weeks, list every patient on insulin or a sulfonylurea on your shifts, with the pre-dialysis glucose and any low. Perform and document a foot check on five patients. Review both with your preceptor and identify one patient whose pattern you will report to the attending nephrologist."},
    "quiz": [
        ("Why does a patient&rsquo;s insulin requirement often fall as kidney function is lost?",
         ["The pancreas makes more insulin in uremia",
          "The kidney clears less insulin, and kidney glucose production falls",
          "Dialysis fluid contains insulin",
          "Uremia makes muscle more sensitive to insulin"], 1,
         "Insulin lingers and the kidney adds less glucose between meals."),
        ("A man on premixed insulin skipped breakfast. At hour two he is sweaty and his pressure has fallen. What do you check first, beside the pressure?",
         ["A capillary glucose",
          "A serum potassium",
          "A chest radiograph",
          "His HbA1c"], 0,
         "A low and a falling pressure look alike and can occur together. A fingerstick takes two minutes."),
        ("In the sensor study by Hayashi and colleagues, dialysis fluid contained 100 to 150 mg/dL glucose. What did they find?",
         ["No patient had a low",
          "Lows occurred only with glucose-free fluid",
          "One in five patients had a low related to dialysis, and none had symptoms",
          "Sensor glucose rose during the session"], 2,
         "21% had silent lows despite a glucose-containing bath."),
        ("When may a low related to dialysis occur, according to the sensor data?",
         ["Only in the first hour",
          "Only when the dialysis fluid is glucose-free",
          "Only when the patient has symptoms",
          "During the session or after it, before the next meal"], 3,
         "The study counted lows between the end of dialysis and the next meal. The ride home is part of the risk."),
        ("Which change in a dialysis patient tends to make HbA1c falsely low?",
         ["A rising dose of an erythropoiesis-stimulating agent",
          "Untreated iron deficiency",
          "Carbamylation of hemoglobin",
          "A very high glucose log"], 0,
         "An ESA releases young, lightly glycated red cells."),
        ("A woman on insulin has an HbA1c of 5.6%. Her meter log shows readings from 50 to 320 mg/dL. Which interpretation is best?",
         ["Her control is excellent",
          "The meter is faulty",
          "The HbA1c may be biased low and may also reflect frequent lows. Report the discordance",
          "Her insulin should be increased"], 2,
         "In dialysis a low HbA1c can mean young red cells or frequent lows. The readings come first."),
        ("What does KDIGO 2022 Recommendation 2.2.1 (1C) say about HbA1c targets?",
         ["A target below 6.5% for all patients with diabetes",
          "An individualized target from below 6.5% to below 8.0%, for patients not treated with dialysis",
          "A target of 7% to 8% for dialysis patients",
          "That HbA1c should not be measured in CKD"], 1,
         "The recommendation excludes dialysis. No guideline gives an HbA1c target for dialysis patients."),
        ("In the DOPPS cohort, how was HbA1c associated with death in hemodialysis patients?",
         ["Lower was always better",
          "There was no association",
          "Higher was always better",
          "The association was U-shaped, lowest at 7.0% to 7.9%"], 3,
         "Risk rose at both ends. The data are observational."),
        ("A patient&rsquo;s sensor shows 62 mg/dL, but he looks well and is chatting. What do you do?",
         ["Ignore it because he has no symptoms",
          "Remove the sensor",
          "Treat with the full protocol without checking",
          "Confirm with a fingerstick and follow the protocol"], 3,
         "Sensors differ in accuracy in dialysis, and lows are often silent. Confirm, then act per protocol."),
        ("A mean sensor glucose is 190 mg/dL and the laboratory HbA1c is 6.4%. Using GMI = 3.31 + 0.02392 &times; mean glucose, what is the discordance?",
         ["About 1.5 percentage points, with the GMI higher",
          "None",
          "About 1.5 percentage points, with the HbA1c higher",
          "About 4.5 percentage points"], 0,
         "The GMI is about 7.9%. Report the gap."),
        ("A new patient&rsquo;s list includes metformin. What does KDIGO 2022 say?",
         ["Recommendation 4.1.1 (1B) applies at eGFR 30 or more, and the algorithm stops metformin below 30",
          "Metformin is preferred in dialysis",
          "Metformin is safe if given after dialysis",
          "There is no statement on metformin"], 0,
         "Flag it for the attending nephrologist. You do not stop it yourself."),
        ("A patient who has started dialysis is still taking empagliflozin. What is the best action?",
         ["Stop it yourself",
          "Double the dose to restore its effect",
          "Flag it for the attending nephrologist, citing the practice point to continue until kidney replacement therapy starts",
          "Leave it, because SGLT2 inhibitors protect the heart in dialysis"], 2,
         "Practice point 1.3.6 says continue until kidney replacement therapy starts."),
        ("Which diabetes medicine on a dialysis patient&rsquo;s list is most likely to cause a prolonged low?",
         ["A DPP-4 inhibitor",
          "Glibenclamide",
          "A GLP-1 receptor agonist alone",
          "An SGLT2 inhibitor"], 1,
         "Glibenclamide and its active products build up without kidneys. Lows can return hours after treatment."),
        ("During a foot check you find a dusky blue second toe on the left. The left foot is cooler than the right. What do you do?",
         ["Record it and review at the next session",
          "Advise the patient to soak the foot in warm water",
          "Call the attending nephrologist now",
          "Raise the leg and apply a compression bandage"], 2,
         "A dusky toe and a cold foot suggest a threatened blood supply. Hours matter, so escalate at once; prompt review can save the limb."),
        ("A woman with long-standing diabetes feels full and bloated after small meals. She is low in the chair and high in the evening. What is the likely link?",
         ["Gastroparesis delays the meal while insulin and the dialyzer lower glucose",
          "The dialysis fluid contains too much glucose",
          "Her HbA1c is falsely high",
          "She is taking metformin"], 0,
         "A slow stomach mismatches food and insulin. Report the pattern."),
    ],
    "terms": [("Hypoglycemia unawareness", "A low glucose without the usual warning symptoms of sweating, tremor, and hunger."),
              ("Neuroglycopenia", "Brain dysfunction from low glucose: confusion, slow speech, odd behavior, focal weakness, or seizure."),
              ("Kidney gluconeogenesis", "Production of new glucose by the kidney cortex, mainly between meals and overnight."),
              ("Hemoglobin A1c (HbA1c)", "The share of hemoglobin that carries glucose, reflecting average glucose over the life of the red cells."),
              ("Estimated average glucose (eAG)", "An average glucose calculated from HbA1c with the ADAG equation."),
              ("Glucose management indicator (GMI)", "An estimate of HbA1c calculated from the average glucose of a continuous sensor."),
              ("Mean absolute relative difference (MARD)", "The average percentage difference between a sensor and a laboratory glucose. Lower means closer agreement."),
              ("Glycated albumin", "A glucose marker based on albumin instead of red cells. It is affected by protein loss and is not validated against outcomes in dialysis."),
              ("Gastroparesis", "Slow emptying of the stomach caused by damage to its nerves."),
              ("Monofilament", "A thin nylon filament pressed against the sole to test protective feeling.")],
    "readings": [("diabetes-kidneys.html", "How diabetes damages the kidney and how treatment changes as kidney function falls."),
                 ("diabetes-tests.html", "What HbA1c, glucose logs, and sensor reports measure, with their limits."),
                 ("filipino-diabetic-diet.html", "Practical Filipino meal planning for diabetes, useful when advising on dialysis-day meals.")],
    "calcs": ["calc-eag-hba1c.html", "calc-metformin-ckd-safety.html", "calc-sglt2i-eligibility.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
