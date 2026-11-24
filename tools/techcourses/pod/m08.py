# -*- coding: utf-8 -*-
"""Physician on Duty, Module 08: Dry Weight: Finding the Right Amount of Fluid.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty and a nurse checking a patient&rsquo;s weight printout at the dialysis chair, the machine screen showing the fluid goal. The seated patient has slightly swollen ankles.",
    "objectives": [
        "Define dry weight (target weight) and explain why it is a clinical estimate that drifts with illness, appetite, and muscle loss.",
        "Perform a bedside volume assessment and state which signs are unreliable in dialysis patients.",
        "Calculate the session fluid goal, the hourly ultrafiltration rate per kilogram, and the minimum session time that keeps the rate within your unit&rsquo;s ceiling.",
        "Explain plasma refilling and why removing fluid faster than the tissues can refill drops the blood pressure.",
        "Describe lung ultrasound and bioimpedance in outline, and summarize what randomized trials of each have and have not shown.",
        "Recognize the clues that a target weight is set too high or too low, and escalate them with a structured report.",
    ],
    "big": """
{{plain:Picture a water tank with a fill line painted on its side. Every session, a drain empties the tank down to that line. The target weight is the line, and the drain is the dialysis machine.}}
<p>The picture has a limit. Nobody can see the line. It is drawn by clinical judgment and redrawn when the patient changes, and the tank itself changes size as the patient loses or gains flesh. Dry weight is an estimate that drifts, not a fixed property of the patient.</p>
{{cards:Key terms for this module|Dry weight (target weight)::The lowest weight after dialysis that the patient tolerates without symptoms or low pressure, and without signs of overload between sessions. It is a clinical estimate.|Interdialytic weight gain (IDWG)::The weight gained between the end of one session and the start of the next. It is mostly the salt and water taken in.|Ultrafiltration (UF)::Removal of water from the blood by pressure across the dialyzer membrane.|UF rate::The volume removed per hour, usually divided by body weight and written in milliliters per kilogram per hour (mL/kg/h).|Plasma refilling::Movement of fluid from the tissue spaces back into the blood vessels while the machine removes water from the blood.|Extracellular water::The water outside the cells: plasma plus the fluid between the cells. Overload lives here.|B-lines::Vertical bright streaks on lung ultrasound that appear when lung tissue holds extra water.|Bioimpedance spectroscopy::A bedside test that passes a tiny current through the body to estimate extracellular water.}}
<p>Most sessions run on a fluid goal that fits the patient and the booked time. A few do not: the goal is too large for the hours booked, or the patient has changed and the target has not. Your work is to check the arithmetic, notice the mismatch, and bring it to the attending nephrologist with numbers. The target belongs to the prescription, not to you.</p>
""",
    "case": {"title": "Four kilos over, three hours booked", "html": """
<p>Monday, 6:30 a.m., the first shift after the long weekend. Mang Teodoro &ldquo;Teddy&rdquo; Villanueva, 58, has diabetes and has been on dialysis for three years through a left forearm fistula. Nurse Liza Ramos tells you that his transport must leave early today, so the session is booked for 3 hours instead of his usual 4.</p>
<p>His pre-dialysis weight is 68.4 kilograms. The target weight on the order is 64.5 kilograms. His blood pressure is 168/94 mm Hg sitting, pulse 88 per minute, oxygen saturation 95% on room air, and respiratory rate 18 per minute. He has mild ankle edema and no crackles. He sleeps on two pillows &ldquo;as always.&rdquo; His post-dialysis weights over the last month reached the target each time. He says his appetite has been poor since a fever two weeks ago.</p>
<p>Ms. Ramos has entered a fluid goal of 4.2 liters: 3.9 kilograms of weight gain plus 0.3 liters for the rinse-back and his drinks during the session. She asks whether she may start. All values are illustrative.</p>
""", "questions": ["What hourly rate does this goal require in 3 hours and in 4, and how does each compare with your unit&rsquo;s ceiling?",
                  "Which findings support the current target weight, and which undercut it?",
                  "What do you write, whom do you call, and which options belong to the attending nephrologist?"]},
    "sections": [
        ("concept", "What dry weight is", "What dry weight is, and what it is not", """
<p>Healthy kidneys match salt and water output to intake, hour by hour. Eat a salty meal, and the kidneys excrete the extra sodium and the water that travels with it. A patient on dialysis has little or no output. Every gram of salt eaten holds water in the extracellular space until the next session. The weight climbs between sessions, and the machine must remove it.</p>
{{fig:pod08_tank}}
<p>The fluid the patient carries before a session has two parts. The first is today&rsquo;s gain, the interdialytic weight gain (IDWG). The second is any overload left after the last session because the target was set too high. A consensus group of 18 authors put it this way: pre-dialysis volume overload is the sum of the weight gain and the overload left behind after dialysis.[[hecking2013]] The scale sees only the first part. The second part hides under the target.</p>
<h3>A working definition</h3>
<p>For this module, dry weight is the lowest weight after dialysis that the patient tolerates without symptoms or low pressure during or after the session, and without signs of overload between sessions.[[daugirdas2015]] This is a clinical definition, not a measured quantity. The Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference on blood pressure and volume in dialysis named the lack of an objective measure of extracellular volume as a central problem in this field.[[kdigo_bpvol2020]]</p>
<h3>Why the hidden part matters</h3>
<p>Chronic overload is associated with death. Wizemann and colleagues measured hydration with bioimpedance in 269 patients in three European centers and followed them for 3.5 years. Relative overhydration before dialysis was an independent predictor of death, with an adjusted hazard ratio of 2.10, second only to diabetes. Patients more than 15% above normal extracellular water, about 2.5 liters, had a gross mortality of 14.7%. The whole group&rsquo;s annual figure was 8.5%.[[wizemann2009]]</p>
<p>The weight gain itself carries a smaller signal. Kalantar-Zadeh and colleagues studied 34,107 patients in the United States. A gain of 4.0 kilograms or more, compared with 1.5 to 2.0 kilograms, was associated with cardiovascular death (hazard ratio 1.25).[[kalantar2009]] The consensus group concluded that chronic overload carries more than twice the mortality risk, while the risk linked to the gain alone is much smaller and is seen mainly with very large gains.[[hecking2013]]</p>
<p>All three sources are observational. Sicker and frailer patients may carry more water for reasons that also shorten life. These studies show an association. They do not show that lowering the target prolongs life.</p>
<p>For you, the target on the order is the attending nephrologist&rsquo;s current estimate. Use it for the arithmetic, never change it, and notice when the patient no longer fits it.</p>
{{key:The scale reading is a fact. The target weight is an estimate. Your job is to notice when the two stop agreeing.}}
"""),
        ("bedside", "Bedside assessment", "Assessing volume at the bedside, and its limits", """
<p>Think of driving in fog with weak headlights. Each sign lights a little of the road, and none lights all of it. You combine weak signs and compare them with the last few sessions.</p>
<p>Each sign has its own physiology. Pitting edema appears only after a large expansion of the tissue spaces. Crackles need fluid in the air spaces, which comes late; water in the lung tissue is silent. The jugular venous pressure reflects right heart filling, which other heart disease can raise. Low albumin, heart failure, venous disease, and calcium channel blockers all cause edema without excess body water.</p>
<p>The Lung Water by Ultra-Sound Guided Treatment (LUST) investigators compared crackles and edema with lung ultrasound in 1,106 paired examinations from 79 high-risk patients. Crackles shared only 12% of their variance with lung water, and edema only 4%. Kappa values, which measure agreement beyond chance, ranged from 0.00 to 0.16. The area under the curve was 0.61 to 0.68 for crackles and 0.56 or lower for edema, where 0.5 is a coin toss.[[torino2016]]</p>
<p>Lung water can also rise with no symptoms. In a multicenter study of 392 patients, 45% had moderate to severe lung congestion on ultrasound. Of those, 71% had no or only slight symptoms of heart failure.[[zoccali2013]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Sign</th><th>What it reflects</th><th>Why it misleads in dialysis</th></tr></thead>
<tbody>
<tr><td>Weight trend</td><td>Salt and water gained between sessions</td><td>Cannot separate water from flesh. A patient losing muscle can hold more water at the same weight</td></tr>
<tr><td>Pre-dialysis blood pressure</td><td>Volume, vessel stiffness, and medicines together</td><td>Stiff arteries and missed tablets raise it without extra volume</td></tr>
<tr><td>Ankle edema</td><td>Fluid in the tissue spaces of the legs</td><td>Low albumin, venous disease, and calcium channel blockers cause it. Shared variance with lung water 4%[[torino2016]]</td></tr>
<tr><td>Crackles</td><td>Fluid in the air spaces</td><td>Late sign. Shared variance with lung water 12%[[torino2016]]</td></tr>
<tr><td>Jugular venous pressure</td><td>Right heart filling pressure</td><td>Raised by tricuspid regurgitation and right heart failure. Hard to see in a short, thick neck</td></tr>
<tr><td>Orthopnea</td><td>Lung congestion when lying flat</td><td>More specific, but many patients sleep propped up from habit. Ask what has changed</td></tr>
<tr><td>Cramps and low pressure late in sessions</td><td>The patient is reaching or passing true dry weight</td><td>Fast removal causes the same symptoms in an overloaded patient</td></tr>
</tbody></table></div>
<h3>What you do at the chair</h3>
<p>Run a structured assessment when a fluid goal looks large or the patient looks different. Module 11 covers the three-minute pre-dialysis check; this is the volume part of it, done in more depth.</p>
<ol>
<li>Review the last four to six sessions: pre- and post-dialysis weights, pre-dialysis pressure, and any cramps or low pressure.</li>
<li>Ask about breathlessness, orthopnea and any change in it, cramps, dizziness at home, appetite, and urine output.</li>
<li>Examine for edema, jugular venous pressure, and crackles.</li>
<li>Check the standing pressure if the patient has been dizzy after sessions.</li>
<li>Write what you found, not a verdict. &ldquo;Edema 1+ to the ankles, unchanged from last week&rdquo; helps the attending. &ldquo;Euvolemic&rdquo; does not.</li>
</ol>
{{key:No single bedside sign measures dry weight. Trends across sessions tell you more than one examination.}}
"""),
        ("goal", "Goal and hourly rate", "The fluid goal and the hourly rate", """
<p>Picture draining a pool through one pipe. Drain the same volume in three hours instead of four, and the water must run faster. The fluid goal is the volume. The ultrafiltration (UF) rate is the speed. Module 5 explained how the machine creates the flow; this section is the arithmetic.</p>
<h3>The arithmetic</h3>
<p>The formulas are definitions. The session goal in milliliters is the pre-dialysis weight minus the target weight, in kilograms, times 1,000, plus any fluid your unit&rsquo;s protocol adds: the rinse-back, saline flushes, or drinks on the chair. Units differ on what they add, so learn your unit&rsquo;s rule.</p>
<p>The UF rate in mL/kg/h is the goal divided by the session hours times the body weight. Studies differ on which weight they use; one large cohort used the post-dialysis weight.[[mermelstein2023]] Follow your unit&rsquo;s convention every time.</p>
{{flow:From the scale to the rate|Weight gain::Pre-dialysis weight minus target weight. In the case, 68.4 minus 64.5 = 3.9 kg.|Session goal::Weight gain in milliliters plus the fluid your unit&rsquo;s protocol adds. In the case, 3,900 + 300 = 4,200 mL.|Hourly volume::Goal divided by booked hours. 4,200 &divide; 3 = 1,400 mL per hour.|Rate per kilogram::Hourly volume divided by the weight your unit uses. 1,400 &divide; 64.5 = 21.7 mL/kg/h.|Compare::Set the rate beside your unit&rsquo;s ceiling. If it is above, call before the session starts.}}
{{formula:<strong>Worked example A: rate and time check (illustrative).</strong> Goal 4,200 mL. Weight used for normalization 64.5 kg (the target weight, in this example).<br>3 hours: 4,200 &divide; (3 &times; 64.5) = 4,200 &divide; 193.5 = 21.7 mL/kg/h.<br>4 hours: 4,200 &divide; (4 &times; 64.5) = 4,200 &divide; 258 = 16.3 mL/kg/h.<br>Minimum time at an illustrative ceiling of 13 mL/kg/h: 4,200 &divide; (13 &times; 64.5) = 4,200 &divide; 838.5 = 5.0 hours.<br>Formula: UF rate = goal &divide; (hours &times; weight), the definition used in the cohorts below.[[flythe2011]][[assimon2016]] The value 13 is used here only because those cohorts studied it as a cut-point. Your unit&rsquo;s ceiling is set by protocol.<br><em>What this tells you:</em> the booked time cannot remove this goal within the ceiling. <em>What it does not tell you:</em> whether the goal or the target is right.}}
<p>The site&rsquo;s <a href="calc-ufr-ceiling.html">UF rate ceiling calculator</a> and <a href="calc-ultrafiltration-rate.html">ultrafiltration rate calculator</a> do this arithmetic at the chair. The <a href="calc-idwg-fluid.html">weight gain and fluid calculator</a> handles the first two steps.</p>
<h3>Why the rate matters: the evidence</h3>
<p>Every study linking the rate to harm is observational. No randomized trial has yet shown that keeping the rate under any ceiling improves survival.</p>
<div class="table-wrap"><table>
<thead><tr><th>Study</th><th>Patients</th><th>What was compared</th><th>Finding</th><th>Design and limits</th></tr></thead>
<tbody>
<tr><td>Flythe and colleagues, 2011[[flythe2011]]</td><td>1,846, from the Hemodialysis (HEMO) Study</td><td>Above 13 versus 10 or less mL/kg/h</td><td>All-cause death, adjusted hazard ratio 1.59. Cardiovascular death 1.71. Risk began to rise above 10</td><td>Secondary analysis of trial data. Observational for this question</td></tr>
<tr><td>Assimon and colleagues, 2016[[assimon2016]]</td><td>118,394</td><td>Above 13 versus 13 or less. Above 10 versus 10 or less</td><td>Adjusted hazard ratio 1.31 and 1.22. Consistent across sex, race, vintage, session length, and body size</td><td>Retrospective cohort. Residual confounding possible. Authors call for randomized trials</td></tr>
<tr><td>Mermelstein and colleagues, 2023[[mermelstein2023]]</td><td>396,358</td><td>Rate in mL/h against post-dialysis weight</td><td>Risk depends on weight, but not in a one-to-one ratio</td><td>Retrospective cohort from one United States provider</td></tr>
</tbody></table></div>
<p>In the Mermelstein cohort, rates associated with a 20% and a 40% higher weight-specific mortality risk were 3W + 500 and 3W + 630 mL/h, where W is the post-dialysis weight in kilograms. They were about 70 mL/h higher in men than in women.[[mermelstein2023]] Because the constant does not scale with weight, the same risk level sits at a higher mL/kg/h in a small patient and a lower one in a heavy patient. For a 100-kilogram patient, 3W + 500 is 800 mL/h, only 8.0 mL/kg/h. A fixed ceiling in mL/kg/h is therefore relatively stricter for small patients and more lenient for heavy ones.</p>
{{formula:<strong>Worked example B: weight-indexed check (illustrative).</strong> Formula from Mermelstein and colleagues, with post-dialysis weight W.[[mermelstein2023]]<br>W = 64.5 kg. Average rate: 3 &times; 64.5 + 330 = 523.5 mL/h.<br>20% higher-risk level: 193.5 + 500 = 693.5 mL/h, which is 693.5 &divide; 64.5 = 10.8 mL/kg/h.<br>40% higher-risk level: 193.5 + 630 = 823.5 mL/h, which is 12.8 mL/kg/h.<br>Teddy&rsquo;s 3-hour plan: 4,200 &divide; 3 = 1,400 mL/h.<br>A 45-kg patient: 3 &times; 45 + 500 = 635 mL/h, which is 14.1 mL/kg/h. The same risk level sits at a higher mL/kg/h in a smaller patient.<br><em>What this tells you:</em> where a planned rate sits against one large cohort. <em>What it does not tell you:</em> a safe target. These are associations, averaged across men and women, not treatment goals.}}
<p>The KDIGO conference listed a slower fluid removal rate among the measures to consider for patients who drop their pressure. Its conclusions are conference statements, not graded recommendations.[[kdigo_bpvol2020]] Your unit&rsquo;s protocol sets the ceiling. Learn it, and learn which weight it divides by.</p>
{{call:Stop and call the attending nephrologist before the session starts when the goal would need a rate above your unit&rsquo;s ceiling in the booked time. Bring the weights, the goal, the hours, the rate, and the minimum time the ceiling would require. Do not shorten the goal or extend the session on your own.}}
{{key:Check the arithmetic at every chair where the goal looks large. A goal that fits four hours may not fit three.}}
"""),
        ("refill", "Plasma refilling", "Plasma refilling: why fast removal drops the pressure", """
<p>Picture the machine drinking from a small glass that is refilled from a large jug. The glass is the plasma, about 3 liters in an adult. The jug is the fluid between the cells, several times larger. If the machine drinks faster than the jug pours, the glass empties, however full the jug is.</p>
<p>The picture has a limit. The jug does not pour by gravity. Fluid moves back into the capillaries because of forces across the capillary wall, and those forces change during the session.</p>
{{fig:two_compartment|The plasma is the small compartment the machine draws from. The tissue spaces are the large compartment that refills it, at a limited speed.}}
<h3>The physiology</h3>
<p>Ultrafiltration removes water only from the plasma. Proteins, mainly albumin, stay behind. As water leaves, the protein in the plasma becomes more concentrated, and its oncotic pressure rises. That pressure pulls fluid from the tissue spaces into the capillaries. At the same time, an expanded tissue space has a higher pressure of its own, which pushes fluid toward the vessels. These are the Starling forces.[[hall2021]]</p>
{{fig:pod08_refill}}
<p>Refilling is fast when the tissue spaces are full and the albumin is normal. It slows as the patient approaches true dry weight, because the tissue pressure falls. It also slows with low albumin, with a warm dialysis fluid and opened skin vessels, and with posture changes.[[daugirdas2001]] When removal outruns refilling, blood volume falls. Less blood returns to the heart, and the heart pumps less. The pressure falls if the vessels and the heart cannot compensate. Module 13 covers those defenses and the response when they fail.</p>
<p>This is why an overloaded patient often tolerates removal early, and why the pressure tends to fall late, as refilling slows near the target. A plan to &ldquo;take off the rest in the last hour&rdquo; puts the fastest removal exactly where refilling is slowest. That is the most dangerous moment of the session.</p>
<h3>What monitoring can and cannot do</h3>
<p>Some machines track the relative change in blood volume from the concentration of the blood. A review of intradialytic hypotension judged absolute blood volume measures more promising than relative ones for predicting episodes, and found that feedback systems that change the UF rate automatically have not yet improved outcomes.[[sars2020]] A falling blood volume curve tells you that removal is outrunning refilling. It does not tell you where the true dry weight lies.</p>
{{key:Fluid leaves the blood quickly and returns from the tissues slowly. Speed, as much as volume, decides whether the pressure holds.}}
"""),
        ("tools", "Ultrasound and bioimpedance", "Lung ultrasound and bioimpedance in outline", """
<p>Two tools try to see what the stethoscope misses. Lung ultrasound counts the &ldquo;comet tails&rdquo; that wet lung tissue throws on the screen. Bioimpedance estimates extracellular water from how easily a tiny current passes through the body. Both measure fluid. Neither is an outcome.</p>
<p>A normal, air-filled lung reflects the ultrasound beam as horizontal repeating lines, called A-lines. When the thin walls between the small air units of the lung thicken with water, the beam produces vertical bright streaks, called B-lines. The more B-lines across the chest, the more water in the lung.[[zoccali2013]]</p>
{{fig:pod08_lus}}
<p>Bioimpedance spectroscopy uses the fact that cell membranes block low-frequency current. At low frequency the current travels around the cells, through the extracellular water. At high frequency it also passes through the cells. Comparing the two lets the device estimate extracellular and intracellular water, and from them an overhydration value.</p>
{{fig:pod08_bia}}
<h3>Lung ultrasound: what the evidence shows</h3>
<p>The prognostic signal is strong. In the 392-patient cohort, very severe congestion was associated with a 4.2-fold risk of death (hazard ratio 4.20) and a 3.2-fold risk of cardiac events (3.20), adjusted for heart failure class and other risk factors.[[zoccali2013]]</p>
<p>The treatment signal is weaker. The LUST trial randomized 367 high-cardiovascular-risk patients; in the active arm, the pre-dialysis lung scan guided UF and drug treatment. Over a mean of 1.49 years, congestion was relieved more often with ultrasound guidance (78% versus 56%). The primary composite of death, nonfatal myocardial infarction, and decompensated heart failure did not differ (hazard ratio 0.88, 95% confidence interval 0.63 to 1.24). Nor did hospitalization or patient-reported outcomes. A post hoc analysis suggested fewer recurrent heart failure episodes (0.37) and cardiovascular events (0.63).[[zoccali2021]] Post hoc results generate hypotheses. They do not prove benefit.</p>
<p>In a LUST substudy of 71 patients, ultrasound-guided dry weight reduction lowered 48-hour central systolic pressure by 6.3 mm Hg, against 0.5 mm Hg in controls, over 8 weeks.[[loutradis2020]] That is a surrogate. In 250 low-risk patients, a combined lung ultrasound and bioimpedance protocol did not reduce death or cardiovascular events (hazard ratio 1.09). It reduced dyspnea before dialysis (rate ratio 0.81) and increased cramps (rate ratio 1.26).[[siriopol2017]]</p>
<h3>Bioimpedance: what the evidence shows</h3>
<p>In 156 patients, bioimpedance guidance reduced left ventricular mass index by 10.2 g/m&sup2; more than usual care over one year, a surrogate.[[hur2013]] A single-center pilot of 131 patients reported an unadjusted mortality hazard ratio of 0.100. Events were few, caregivers were not masked, and the authors asked for a larger trial.[[onofriescu2014]] A review of 8 randomized trials with 1,443 patients found no significant difference in mortality or cardiovascular events. Overhydration and blood pressure fell, and urine output fell faster in the two trials with the largest change in fluid status.[[tabinor2018]]</p>
<p>The largest recent trial, BioImpedance Spectroscopy to maintain Renal Output (BISTRO), randomized 439 incident patients with residual kidney function in 34 United Kingdom centers. Time to anuria did not differ (cause-specific hazard ratio 0.751, 95% confidence interval 0.459 to 1.229), and neither did blood pressure or symptoms. Both arms used a standardized clinical fluid assessment, which the authors concluded preserved residual function well without bioimpedance. The trial recruited 85% of its target.[[davies2025]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Trial</th><th>Patients</th><th>What improved</th><th>What did not</th></tr></thead>
<tbody>
<tr><td>LUST, 2021[[zoccali2021]]</td><td>367, high cardiovascular risk</td><td>Lung congestion relieved more often</td><td>Death, myocardial infarction, and heart failure composite. Hospitalization. Patient-reported outcomes</td></tr>
<tr><td>LUST substudy, 2020[[loutradis2020]]</td><td>71, hypertensive</td><td>Central blood pressure and arterial stiffness (surrogates)</td><td>Not designed for clinical outcomes</td></tr>
<tr><td>Siriopol, 2017[[siriopol2017]]</td><td>250, low cardiovascular risk</td><td>Less dyspnea before dialysis</td><td>Death and cardiovascular events. More cramps</td></tr>
<tr><td>Hur, 2013[[hur2013]]</td><td>156</td><td>Less overload. Left ventricular mass (surrogate)</td><td>Not designed for clinical outcomes</td></tr>
<tr><td>Onofriescu, 2014[[onofriescu2014]]</td><td>131, one center</td><td>Unadjusted mortality, in a small unmasked pilot</td><td>Needs confirmation in a larger trial</td></tr>
<tr><td>BISTRO, 2025[[davies2025]]</td><td>439, incident, with urine output</td><td>No difference from a standardized clinical protocol</td><td>Time to anuria, blood pressure, symptoms</td></tr>
</tbody></table></div>
<p>For you, the point is to know what the tools show and where they stop. Use them only if you are trained and your unit&rsquo;s protocol allows it. Report the finding to the attending nephrologist, who decides the target.</p>
{{key:The tools find hidden fluid more reliably than the stethoscope, but finding fluid has not yet been shown to save lives. The decision stays clinical.}}
"""),
        ("wrong", "Target too high or low", "When the target is too high or too low", """
<p>Dry weight is a moving target. An illness melts muscle, so the same scale number holds more water. Recovery adds flesh, so the old target drains too much. The order stays the same until someone notices.</p>
{{fig:pod08_wetdry}}
<h3>Two ways to be wrong</h3>
<p>When the target is too high, the patient leaves every session still overloaded. The blood pressure rises, and water collects in the lungs, often silently.[[zoccali2013]] When the target is too low, the patient is underfilled at the end of each session, with cramps, late drops in pressure, and hours of exhaustion afterward. In patients who still pass urine, repeated underfilling may hasten the loss of that urine. Faster loss of residual function is associated with higher mortality in new dialysis patients.[[obi2016]] In the bioimpedance trials, urine output fell faster in the two trials that removed the most fluid.[[tabinor2018]]</p>
<h3>What happens when the target is pushed down</h3>
<p>The Dry-weight Reduction In hypertensive hemodialysis Patients (DRIP) trial randomized 150 hypertensive patients, 100 to dry weight probing and 50 to control. Without changing session time, the target fell by about 1 kilogram, and interdialytic ambulatory systolic pressure fell by 6.9 mm Hg at 4 weeks and 6.6 mm Hg at 8 weeks against control. Symptoms of low pressure during dialysis increased; quality of life did not worsen.[[agarwal2009drip]] DRIP shows a fall in blood pressure, a surrogate, over 8 weeks. It did not test death, cardiovascular events, or residual urine.</p>
<p>The trade-off is unsettled. A lower target lowers the pressure but may cost residual function and comfort, by amounts unknown for the individual patient.[[tabinor2018]][[davies2025]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Clues the target may be too high</th><th>Clues the target may be too low</th></tr></thead>
<tbody>
<tr><td>Pre-dialysis pressure trending up over several sessions</td><td>Cramps and low pressure late in most sessions</td></tr>
<tr><td>New or worsening orthopnea</td><td>Dizziness on standing after dialysis</td></tr>
<tr><td>Edema that does not clear by the end of the week</td><td>Long recovery time, exhausted for hours after each session</td></tr>
<tr><td>B-lines on lung ultrasound, where available</td><td>Shrinking urine output</td></tr>
<tr><td>Pressure that rises during sessions (Module 14)</td><td>Target reached easily, no signs of overload, appetite and weight improving</td></tr>
<tr><td>Poor appetite or recent illness with a stable weight, suggesting lost flesh replaced by water</td><td>Weight gain from better eating after a hospital stay, with the old target unchanged</td></tr>
</tbody></table></div>
{{fig:pod08_flesh}}
{{formula:<strong>Worked example C: gain as a share of target (illustrative).</strong> Teddy&rsquo;s gain: 3.9 kg &divide; 64.5 kg &times; 100 = 6.0%.<br><em>What this tells you:</em> how much salt and water he took in over the long gap, relative to his size. <em>What it does not tell you:</em> whether overload is hidden under the target. That is a separate question.[[hecking2013]]}}
{{formula:<strong>Worked example D: flesh or fluid, a decision walk-through (illustrative).</strong> Post-dialysis weights reach the target every session. Edema persists. Appetite fell after an illness. Pre-dialysis pressure has climbed over four sessions.<br>Step 1: suspect that lost flesh has been replaced by water at the same weight.<br>Step 2: list the clues, each with its session dates.<br>Step 3: report to the attending nephrologist with the four-session trend.<br>Step 4: the attending decides whether to probe the target down.<br><em>What this tells you:</em> which way the target may need to move. <em>What it does not tell you:</em> by how much. That is the attending&rsquo;s call.}}
<h3>What you do</h3>
<p>Document the pattern across sessions, not a single reading. Report it to the attending nephrologist in the situation, background, assessment, recommendation (SBAR) format. Proposing a review is your role. Writing a new target is not.</p>
{{call:Stop and call the attending nephrologist for any proposed change in target weight, from any source: a nurse, the patient, a relative, or another doctor. Report the pattern and the trend. Do not alter the target or the goal yourself.}}
{{key:A target weight is reviewed on a pattern, not on one session. Bring the pattern to the attending.}}
"""),
        ("cannot", "Goal not reachable", "When the goal cannot be reached safely", """
<p>Think of a bridge rated for a certain load. If the truck is too heavy, you do not drive faster. You split the load. When a fluid goal cannot be removed within the ceiling in the booked time, the answer is never to run the machine harder.</p>
<p>The limits are refilling speed and the reserve of the heart and vessels. Module 13 covers what happens when they are crossed.</p>
{{fig:pod08_notreach}}
<h3>Options belong to the attending nephrologist</h3>
<p>You list the options. The attending chooses. The usual choices are these:</p>
<ul>
<li>Accept a partial goal today and add a session in the next day or two.</li>
<li>Extend today&rsquo;s session, if the patient and the schedule allow.</li>
<li>Isolated UF, before or after the diffusion part of the session (Module 12).</li>
<li>Review salt intake and the dialysis fluid sodium (Module 7). Salt and fluid counseling with Filipino foods is in Module 23.</li>
<li>Revise the target weight, if the clues point that way.</li>
</ul>
{{flow:When the goal does not fit|Before the session::Calculate the goal and the rate for the booked time.|Over the ceiling?::If no, start per the order. If yes, do not start a plan that exceeds it.|Call::Give the attending nephrologist the weights, goal, hours, rate, minimum time, and your bedside findings.|Options::The attending chooses: partial goal and an extra session, a longer session, isolated UF, a salt and dialysis fluid review, or a revised target.|During the session::If symptoms appear, follow your unit&rsquo;s protocol and Module 13.|After the session::Record the post-dialysis weight, the gap to target, and what was agreed.}}
{{key:A goal that cannot be reached safely today is a prescription question, not a nursing failure. Bring it to the attending with the numbers.}}
"""),
    ],
    "debrief": ["""
<p><strong>What rate does the goal require?</strong> Using the target weight of 64.5 kilograms to normalize, 4,200 mL over 3 hours is 21.7 mL/kg/h. Over his usual 4 hours it is 16.3 mL/kg/h. Against an illustrative ceiling of 13 mL/kg/h, both are above it. Staying at 13 would take about 5 hours. Even his usual session would not fit this goal within that ceiling. In the cohorts that studied it, a rate above 13 was associated with higher mortality.[[flythe2011]][[assimon2016]] Use your unit&rsquo;s own ceiling and weight convention.</p>
<p><strong>Which findings support the target, and which undercut it?</strong> In favor: his post-dialysis weights reached the target every session last month, he has no crackles, and his oxygen saturation is acceptable. Against: his pressure is 168/94 mm Hg, he has ankle edema, and his appetite has been poor since a fever two weeks ago. A man who eats less loses flesh. If his weight still reaches 64.5 kilograms, water may have taken the place of that flesh, and the target may now be too high. Ask whether the two pillows are new. Absent crackles do not settle the question.[[torino2016]] His gain of 6.0% of target tells you what he took in over the long gap, not what hides under the target.[[hecking2013]]</p>
<p><strong>What do you write, whom do you call, and whose options are they?</strong> You write the weights, the goal, the two rates, the minimum time, and your bedside findings, including the appetite history. You call the attending nephrologist before the session starts, in SBAR form. The options belong to the attending: a partial goal today with an extra session this week, a longer session if transport can be rearranged, isolated UF, and a review of the target weight given the recent illness. You do not shorten the goal, extend the session, or change the target on your own.</p>
"""],
    "skills": {"title": "Volume assessment and fluid goal calculation at the chair",
               "intro": "Perform this assessment at a real dialysis chair while your preceptor observes. Use illustrative numbers if the patient&rsquo;s goal is routine, and talk through each step aloud.",
               "items": [
                   ("Confirms the patient&rsquo;s identity and reads the target weight and UF instructions on the current order.", False),
                   ("Checks that the scale was zeroed and that the patient was weighed in the usual clothing.", False),
                   ("Reviews the last four to six sessions: pre- and post-dialysis weights, pre-dialysis pressure, and any low pressure or cramps.", True),
                   ("Asks about orthopnea and any change in it, breathlessness, cramps, dizziness at home, appetite, and urine output.", False),
                   ("Examines for edema, jugular venous pressure, and crackles, and states the limits of each sign.", False),
                   ("Calculates the session goal, including the fluids your unit&rsquo;s protocol adds.", True),
                   ("Calculates the hourly UF rate per kilogram with the unit&rsquo;s chosen weight and compares it with the unit&rsquo;s ceiling.", True),
                   ("If the rate exceeds the ceiling, calls the attending nephrologist before the session starts, with the numbers.", True),
                   ("Lists the options for the attending without choosing among them.", False),
                   ("Does not change the target weight or the goal without an order.", True),
                   ("Documents the findings, the calculation, the call, and the agreed plan in the session record.", False),
               ],
               "placement": "For two weeks, calculate the UF rate for every patient whose goal looks large on your shifts. Keep a log of the rate, the booked time, and any symptoms. Review the log with your preceptor and pick one patient whose target you would ask the attending nephrologist to review, with the clue pattern that supports it."},
    "quiz": [
        ("Which statement best describes dry weight?",
         ["A weight measured precisely by the dialysis machine",
          "The patient&rsquo;s weight before kidney failure",
          "A clinical estimate of the lowest tolerated post-dialysis weight, which drifts as the patient changes",
          "The weight at which the patient has no edema"], 2,
         "No device measures dry weight directly. It is a clinical estimate, and it must be revised when the patient gains or loses flesh."),
        ("A consensus group described pre-dialysis volume overload as the sum of two parts. What are they?",
         ["The weight gain since the last session and the overload left after the last session",
          "Plasma volume and red cell volume",
          "Edema and crackles",
          "Salt intake and water intake"], 0,
         "The scale sees the gain. Overload left behind because the target is too high hides under the target."),
        ("In the LUST auscultation substudy, how well did crackles reflect lung water on ultrasound?",
         ["Very well, with an area under the curve above 0.9",
          "Well for severe congestion only",
          "Better than ultrasound",
          "Poorly, explaining about 12% of the variation"], 3,
         "Crackles shared about 12% of the variance with B-lines and edema about 4%. Their absence does not exclude lung water."),
        ("A man arrives 3.2 kilograms above target for a 4-hour session. His unit adds 0.2 liters for the rinse-back and normalizes to a target weight of 64 kilograms. What is his UF rate?",
         ["10.0 mL/kg/h",
          "13.3 mL/kg/h",
          "12.5 mL/kg/h",
          "16.0 mL/kg/h"], 1,
         "Goal 3,400 mL. 3,400 &divide; (4 &times; 64) = 3,400 &divide; 256 = 13.3 mL/kg/h. The numbers are illustrative."),
        ("What is the strongest evidence currently available that UF rates above 13 mL/kg/h are harmful?",
         ["Large randomized trials showing that lower rates prolong life",
          "Guideline recommendations graded 1A",
          "Large observational cohorts showing an association with mortality",
          "Animal studies"], 2,
         "The HEMO secondary analysis and a cohort of 118,394 patients found associations. No randomized trial has tested a ceiling."),
        ("According to the Mermelstein cohort, how does a fixed ceiling in mL/kg/h behave across body sizes?",
         ["It is relatively stricter for small patients and more lenient for heavy ones",
          "It is equally strict at every weight",
          "It is stricter for heavy patients",
          "It applies only to women"], 0,
         "Risk levels followed 3W plus a constant, so the same risk sits at a higher mL/kg/h in a small patient and a lower one in a heavy patient. A fixed ceiling restricts small patients more and heavy patients less."),
        ("Why does the blood pressure tend to fall late in a session in a patient near target?",
         ["The dialysis fluid becomes colder",
          "The heparin wears off",
          "The machine speeds up automatically",
          "Refilling slows as the tissue spaces empty, while removal continues"], 3,
         "Refilling depends on an expanded tissue space. Near true dry weight it slows, and removal outruns it."),
        ("A nurse proposes removing the remaining 1.5 liters in the last hour because the patient was dizzy earlier. What is the problem with this plan?",
         ["It places the fastest removal where refilling is slowest",
          "It wastes dialysis fluid",
          "It lengthens the session",
          "It lowers the dialysis dose"], 0,
         "The late session is when refilling is slowest. Fast removal there invites a sharp drop. Call the attending about the remaining goal."),
        ("What did the LUST randomized trial show?",
         ["Ultrasound guidance reduced death by half",
          "Ultrasound guidance relieved congestion more often but did not change the composite of death, myocardial infarction, and heart failure",
          "Ultrasound guidance increased deaths",
          "Ultrasound guidance improved quality of life"], 1,
         "Congestion was relieved in 78% versus 56%, but the primary outcome did not differ (hazard ratio 0.88). Post hoc benefits are hypotheses."),
        ("What was the main finding of the BISTRO trial?",
         ["Bioimpedance doubled survival",
          "Bioimpedance shortened time to anuria",
          "Bioimpedance lowered blood pressure substantially",
          "Bioimpedance guidance did not change time to anuria compared with a standardized clinical protocol"], 3,
         "The hazard ratio was 0.751 with a confidence interval crossing 1. The authors credit the standardized clinical protocol."),
        ("In the DRIP trial, probing the dry weight down by about 1 kilogram did what?",
         ["Lowered ambulatory systolic pressure by about 7 mm Hg, with more symptoms of low pressure during dialysis",
          "Reduced mortality",
          "Caused no change in blood pressure",
          "Worsened quality of life"], 0,
         "DRIP showed a blood pressure benefit, a surrogate, over 8 weeks. It did not test hard outcomes."),
        ("A woman has had cramps in the last hour of most sessions for three weeks. She is dizzy at home after dialysis, and her urine output has fallen. She has been eating well since a hospital stay. What is the most likely issue?",
         ["Her target weight is too high",
          "Her fistula is narrowing",
          "Her target weight is now too low because she has gained flesh",
          "Her dialysis fluid is too warm"], 2,
         "Weight gained as flesh makes the old target too low. Report the pattern; the attending decides."),
        ("A man&rsquo;s post-dialysis weights reach target every session, but his edema persists and his pre-dialysis pressure is climbing. He lost his appetite after pneumonia a month ago. What should you do?",
         ["Lower his target by 2 kilograms",
          "Report the pattern and the four-session trend to the attending nephrologist and suggest a target review",
          "Tell him to drink less and change nothing",
          "Start an antihypertensive medicine"], 1,
         "Lost flesh may have been replaced by water. Proposing a review is your role; writing a new target is not."),
        ("A relative asks you to lower her father&rsquo;s target weight because his ankles are swollen. What do you do?",
         ["Lower it by 0.5 kilograms as a trial",
          "Explain that edema always means overload",
          "Refuse to discuss it",
          "Assess him, document the findings, and call the attending nephrologist with the request"], 3,
         "Any proposed change in target weight, from any source, goes to the attending. Edema has causes other than overload."),
        ("A patient arrives 4.5 kilograms over target for a 3-hour session, and the rate would exceed your unit&rsquo;s ceiling. What is the best action?",
         ["Start the session and remove the full goal",
          "Remove 3 liters and add the rest next time without telling anyone",
          "Call the attending nephrologist before starting, with the weights, goal, hours, rate, and minimum time",
          "Raise the blood pump speed to remove fluid faster"], 2,
         "A goal that does not fit the ceiling is a prescription question. The attending chooses among the options."),
    ],
    "terms": [("Dry weight (target weight)", "The lowest weight after dialysis that the patient tolerates without symptoms or low pressure, and without signs of overload between sessions. A clinical estimate."),
              ("Interdialytic weight gain", "The weight gained between the end of one session and the start of the next."),
              ("Session fluid goal", "The volume to remove in one session: the weight above target plus the fluids the unit&rsquo;s protocol adds."),
              ("Ultrafiltration rate", "The volume removed per hour, usually divided by body weight and written in mL/kg/h."),
              ("Plasma refilling", "Movement of fluid from the tissue spaces back into the blood vessels during fluid removal."),
              ("Starling forces", "The pressures across the capillary wall, from fluid and from protein, that decide which way fluid moves."),
              ("Extracellular water", "Water outside the cells, in the plasma and between the cells."),
              ("B-lines", "Vertical bright streaks on lung ultrasound that indicate extra water in the lung tissue."),
              ("Bioimpedance spectroscopy", "A bedside test that estimates extracellular and intracellular water from how the body conducts current at different frequencies."),
              ("Surrogate outcome", "A measurement, such as blood pressure or heart muscle mass, used in place of an outcome the patient feels, such as death or hospitalization.")],
    "readings": [("dry-weight-determination.html", "How dry weight is judged at the bedside and when it should be reassessed."),
                 ("fluid-management-dialysis.html", "Salt and fluid advice that reduces weight gain between sessions."),
                 ("hd-volume-bp-tolerance-clinician.html", "A clinician&rsquo;s guide to volume, blood pressure, and tolerance of fluid removal.")],
    "calcs": ["calc-ufr-ceiling.html", "calc-ultrafiltration-rate.html", "calc-idwg-fluid.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
