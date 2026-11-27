# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 05: Volume assessment and fluid stewardship.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. SMART,
BaSICS, PLUS, SAFE, FACTT, CLASSIC, ADVOR, PUSH-AHF, FEAST and the VExUS derivation study checked against their PubMed
abstracts; KDIGO 2012 grades checked against the guideline text; AAP 2018 key action statement checked against the
PubMed abstract. No doses or infusion rates. Fictional case."""

MODULE = {
    "image_alt": "A Filipino internal medicine resident holds an ultrasound probe over the neck of a breathless young woman with dengue while an intern reads the fluid balance chart aloud at the bedside.",
    "objectives": [
        "<strong>Intern:</strong> Chart intake, output and a same-scale daily weight accurately, total the cumulative balance, and report a rising positive balance to your resident within the shift.",
        "<strong>Resident:</strong> Assess volume with examination and point-of-care ultrasound (POCUS), name the limit of each sign, and propose a fluid with its type, purpose and stop point.",
        "<strong>Fellow:</strong> Lead de-resuscitation: decide when fluid has stopped helping, plan diuretic therapy with natriuresis monitoring, and recognize when ultrafiltration or kidney replacement therapy (KRT) is needed.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the bag on the pole</span>Every intravenous bag is a prescription with a dose, a duration and a side effect. The <b>intern</b> owns the numbers: what went in, what came out, and what the scale says this morning. The <b>resident</b> owns the bedside judgment: does this patient need fluid, tolerate fluid, or need fluid removed? The <b>fellow</b> owns the turn: the moment the plan changes from giving to taking off, and the method used to take it off.</div>
{{plain:Picture a rice field beside an irrigation canal. The canal is narrow and carries water to the town. The field is wide and soaks up whatever spills over the canal bank. Pour water into the canal and some reaches the town, but much of it seeps into the field, where it does no work and is slow to drain back.}}
<p>The picture has a limit. A canal bank is fixed, and the wall of a capillary is not. In health, the endothelium and its sugar-rich lining, the glycocalyx, hold most protein inside the vessel, and the lymphatics return what leaks. In sepsis, dengue, burns and after major surgery, that barrier loosens. Fluid given into the vein then leaves the vessel faster, the tissues swell, and the lungs, gut and kidneys become waterlogged. The kidney is an encapsulated organ. When its interstitium swells and its venous pressure rises, its own perfusion pressure falls, so too much fluid can injure the organ the fluid was meant to protect.</p>
<p>The body does not sense water in the abstract. It senses pressure and stretch in the arteries, the atria and the afferent arteriole, and it adjusts sodium excretion to defend the filling of the arteries. A patient can therefore carry several liters of extra fluid in the tissues while the arteries still feel underfilled, as in heart failure, cirrhosis and the leaky phase of dengue. Edema and an empty circulation can coexist. That is why &ldquo;wet or dry&rdquo; is the wrong question at the bedside. The right questions are where the fluid is, whether more would raise cardiac output, and whether the patient can tolerate it.</p>
{{cards:Key numbers|SMART, 15,802 adults::Major adverse kidney events at 30 days 14.3% with balanced crystalloids versus 15.4% with saline (cluster-randomized trial)|BaSICS, 11,052 patients::90-day death 26.4% balanced versus 27.2% saline; adjusted hazard ratio 0.97 (double-blind trial)|PLUS, 5,037 patients::90-day death 21.8% balanced versus 22.0% saline (double-blind trial)|KDIGO 2012, AKI::Isotonic crystalloids rather than colloids for initial volume expansion, in the absence of hemorrhagic shock (2B)|FACTT, 1,000 patients::7-day balance about &minus;136 mL with a conservative strategy versus +6,992 mL liberal; ventilator-free days 14.6 versus 12.1}}
<p>Most fluid decisions on a medical ward are routine: a patient who cannot drink, a patient who is mildly dry. A few are dangerous in either direction: the patient in shock who needs volume now, and the patient who has received liters and is now drowning slowly. Your work is to give fluid for a reason, to say in advance what will make you stop, and to notice the day the plan must turn from filling to removing.</p>
""",
    "case": {"title": "Day six of the fever",
             "html": """
<p>Thursday, 3 a.m., a medical ward of a provincial hospital in Iloilo City. Ms. Maricel Javier, 27, a call-center agent, was admitted on day three of fever with dengue and warning signs: abdominal pain, persistent vomiting and a rising hematocrit. Her admission weight was 52 kg and her creatinine 0.7 mg/dL. Her fever broke on day four. Her hematocrit peaked at 48% that day and is 38% today, and her platelet count has risen from 22,000 to 61,000 per microliter.</p>
<p>She has received intravenous crystalloid without a break since admission. The charted cumulative balance is +5.8 liters over 72 hours, and her weight this evening is 56.5 kg on the same ward scale. Now she is breathless, with a respiratory rate of 28 per minute and an oxygen saturation of 92% on room air. You hear crackles at both bases. Her blood pressure is 104/62 mm Hg, her pulse 96 per minute, her hands warm, and capillary refill under two seconds. Her urine output over the last six hours is 125 mL, and this morning&rsquo;s creatinine was 1.3 mg/dL. The intravenous line is still running at the rate written on day three.</p>
<p>The intern, Dr. Bea Santos, calls the internal medicine resident on duty, Dr. Paolo Villareal: &ldquo;Doc, the nurse is asking for a fluid bolus because her urine output is low.&rdquo;</p>
""",
             "questions": ["What does the chart already tell you, and what should the intern report?",
                           "Will more fluid help her, and how will you find out at the bedside?",
                           "What is the plan for the next 24 hours, and who decides when to remove fluid?"]},
    "sections": [
        ("compartments", "Where water goes", "Compartments: where each liter actually goes", """
<p>Body water sits in two main spaces. Most of it is inside cells. The rest is extracellular, and only a fraction of the extracellular water is plasma, the part that fills the heart. Every infused fluid distributes according to what it carries, and you can predict its fate from its contents before you hang it.</p>
<p>Start with the causal chain. Sodium stays mostly outside cells because the sodium pump pushes it out, so water given with sodium spreads through the whole extracellular space, plasma and interstitium together. Glucose is metabolized, so a bag of dextrose in water becomes free water that spreads into every compartment, including cells, and adds very little to the plasma. Albumin is large; while the capillary barrier is intact it stays in the vessel longer and holds water with it. When the barrier fails, albumin leaks too, and the advantage shrinks.</p>
<div class="table-wrap"><table>
<thead><tr><th>Fluid</th><th>What it carries</th><th>Where it ends up</th><th>What you see if you give too much</th></tr></thead>
<tbody>
<tr><td>Dextrose in water</td><td>Glucose, which is metabolized, leaving free water</td><td>All compartments, mostly cells</td><td>A falling sodium; brain swelling in the worst case (Module 06)</td></tr>
<tr><td>Isotonic saline</td><td>Sodium and chloride at equal concentration, more chloride than plasma</td><td>Extracellular space, most of it outside the vessels</td><td>Edema, and a rising chloride with a falling bicarbonate (Module 08)</td></tr>
<tr><td>Balanced crystalloid</td><td>Sodium with less chloride, plus a buffer such as lactate, acetate or gluconate</td><td>Extracellular space, like saline</td><td>Edema; less chloride load</td></tr>
<tr><td>Albumin</td><td>Protein with an oncotic effect</td><td>More of it stays in the vessels while the barrier holds</td><td>Overload with less total volume; cost</td></tr>
</tbody></table></div>
<p>Two hidden sources often matter more than the bag the team argued about. The first is &ldquo;fluid creep&rdquo;: antibiotics, infusions run as carriers, flushes and the line kept open. The second is maintenance fluid that nobody stopped after the patient started eating. Malbrain and colleagues describe the four D&rsquo;s of fluid therapy as drug, dosing, duration and de-escalation: treat each fluid as a drug with indications and harms, and make de-escalation part of the plan from the start.[[ntr05_5]]</p>
<p>They also divide the course of a critical illness into four phases: resuscitation, optimization, stabilization and evacuation.[[ntr05_5]] The phases are a framework, not a trial result, but they give the team a shared language. On a ward round, saying &ldquo;she is in evacuation now&rdquo; changes the orders faster than any argument about the type of fluid.</p>
{{fig:ntr05_a}}
<div class="table-wrap"><table>
<thead><tr><th>Phase</th><th>The question</th><th>What the bedside usually shows</th><th>Your fluid stance</th></tr></thead>
<tbody>
<tr><td>Resuscitation</td><td>Is the patient in shock?</td><td>Low pressure, cold skin, confusion, rising lactate</td><td>Give volume quickly, in measured portions, and reassess after each</td></tr>
<tr><td>Optimization</td><td>Will more fluid raise cardiac output?</td><td>Pressure recovering; perfusion uncertain</td><td>Give only after a test of fluid responsiveness</td></tr>
<tr><td>Stabilization</td><td>Is the patient stable without new boluses?</td><td>Stable perfusion, positive balance</td><td>Maintenance only, and only if the patient cannot drink</td></tr>
<tr><td>Evacuation</td><td>Is the extra fluid now causing harm?</td><td>Edema, crackles, low oxygen, rising weight, congested organs</td><td>Stop fluids; remove fluid with diuretics or, if needed, ultrafiltration</td></tr>
</tbody></table></div>
{{key:Before you hang a bag, name its job: resuscitation, replacement, maintenance or a carrier. A fluid with no job should not be running.}}
"""),
        ("assess", "Assess honestly", "Assessing volume: what each sign can and cannot tell you", """
<p>Volume assessment is three separate questions, and mixing them causes most errors. Is the patient <b>hypoperfused</b>? Is the patient <b>fluid responsive</b>, meaning that more preload would raise cardiac output? Is the patient <b>fluid tolerant</b>, meaning that more fluid will not congest the lungs, liver, gut or kidneys? A patient can be responsive and intolerant at the same time. Healthy people are fluid responsive; responsiveness alone is not a reason to give fluid.</p>
<h3>The intern&rsquo;s numbers come first</h3>
<p>The single most useful volume test on a ward is a daily weight taken on the same scale, at the same time, in similar clothing, after voiding. Weight cannot tell you where the water is, but it tells you that it is there. The second is an honest balance chart: every oral and intravenous intake, every drain, stool and vomit, and the urine measured, not estimated. Insensible losses rise with fever and fast breathing, and the site&rsquo;s calculators estimate them. A cumulative balance written on the chart each morning shows the trend that single-day totals hide.</p>
<p>Many Philippine wards have no bed scale, and many families bring food and drinks that never reach the chart. Weigh the patient on the ward standing scale if they can stand, ask the watcher to keep a simple list of what the patient drank, and write &ldquo;estimated&rdquo; when the numbers are estimates. A chart that admits uncertainty is safer than one that pretends.</p>
<h3>The examination, with its limits</h3>
<div class="table-wrap"><table>
<thead><tr><th>Sign</th><th>What it reflects</th><th>The trap</th></tr></thead>
<tbody>
<tr><td>Jugular venous pressure</td><td>Right atrial pressure</td><td>Hard to see in short, thick necks; raised in tricuspid regurgitation, pulmonary hypertension and tamponade without excess volume</td></tr>
<tr><td>Peripheral edema</td><td>Interstitial fluid in dependent tissue</td><td>Present with low albumin, venous disease and calcium channel blockers; says nothing about the circulation</td></tr>
<tr><td>Basal crackles</td><td>Fluid in the alveoli, or other lung disease</td><td>Absent in early congestion; present in pneumonia and fibrosis</td></tr>
<tr><td>Skin turgor and dry mucosa</td><td>Interstitial and oral dryness</td><td>Unreliable in older adults and mouth breathers</td></tr>
<tr><td>Orthostatic pulse and pressure</td><td>Venous return when upright</td><td>Blunted by beta blockers and autonomic neuropathy</td></tr>
<tr><td>Capillary refill, skin temperature, mental state, urine output</td><td>Perfusion</td><td>Urine output falls in acute kidney injury (AKI) from any cause, not only from low volume</td></tr>
</tbody></table></div>
<h3>Point-of-care ultrasound</h3>
<p>Point-of-care ultrasound (POCUS) adds pictures of the inferior vena cava (IVC), the lungs, the heart and the venous Doppler of organs. Lung B-lines suggest interstitial fluid. A small, collapsing IVC in a spontaneously breathing patient suggests low right atrial pressure. A large IVC that does not collapse suggests high right atrial pressure, but so do right ventricular failure, tricuspid regurgitation, raised abdominal pressure and positive-pressure ventilation. A large IVC means high pressure; it does not by itself mean too much fluid.</p>
<p>The venous excess ultrasound (VExUS) score combines a dilated IVC with Doppler patterns in the hepatic, portal and intrarenal veins to grade venous congestion. In its derivation, a post hoc analysis of 145 cardiac surgery patients with 706 ultrasound assessments, a severe grade (severe flow abnormalities in more than one Doppler pattern with an IVC of 2 cm or more) was associated with later AKI, with a hazard ratio of 3.69, and an adjusted hazard ratio of 2.82. Detected at intensive care unit (ICU) admission, it had a positive likelihood ratio of 6.37 and outperformed central venous pressure.[[ntr05_6]] This was a single-center, post-surgical cohort. It shows that congestion measured this way predicts kidney injury. It does not show that treating to a VExUS grade improves outcomes.</p>
{{fig:ntr05_b}}
<p>For fluid responsiveness, a passive leg raise moves blood from the legs to the heart and is reversible; if a real-time measure of cardiac output or stroke volume rises, a fluid bolus would likely do the same. Without a way to measure output, a leg raise watched only by blood pressure is a weak test. Most provincial hospitals have a portable ultrasound machine somewhere; learn where it is kept and who is credentialed to use it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What you own in volume assessment</th></tr></thead>
<tbody>
<tr><td>Intern</td><td>Weight, intake, output and the cumulative balance; report a balance above the unit&rsquo;s threshold or a weight rise; examine and describe without concluding</td></tr>
<tr><td>Resident</td><td>Answer the three questions (perfusion, responsiveness, tolerance) in writing; do and document lung and IVC ultrasound if trained; write the stop point on every fluid order</td></tr>
<tr><td>Fellow</td><td>Integrate VExUS, echocardiography, natriuresis and kidney function into one volume plan; teach the limits of each sign</td></tr>
</tbody></table></div>
{{key:Answer three questions in order: is the patient hypoperfused, would more fluid raise output, and can the patient tolerate it? Give fluid only when the first two are yes and the third is not no.}}
"""),
        ("fluids", "Choose the fluid", "Choosing the fluid: balanced crystalloid, saline and albumin", """
<p>The chloride argument starts with physiology. Plasma chloride is lower than sodium; isotonic saline carries them in equal amounts. Large volumes of saline raise plasma chloride and lower bicarbonate, producing a hyperchloremic acidosis. Experimental work suggests that a high chloride load can also lower kidney blood flow. Balanced crystalloids replace part of the chloride with a buffer. The question for trials was whether this physiological difference changes outcomes that patients feel.</p>
<h3>What the trials show</h3>
<p>The Isotonic Solutions and Major Adverse Renal Events Trial (SMART) cluster-randomized 15,802 adults in five ICUs of one academic center to balanced crystalloids or saline by month. A major adverse kidney event within 30 days, a composite of death, new KRT or a creatinine persistently at 200% or more of baseline, occurred in 14.3% with balanced crystalloids and 15.4% with saline (marginal odds ratio 0.91). In-hospital death at 30 days was 10.3% versus 11.1%, a difference that did not reach significance.[[ntr05_1]] The absolute difference in the composite is about 1.1 percentage points, roughly one event avoided for every 90 or so patients. The trial was unblinded, from a single center, and its composite was driven by its components together, not by any one alone.</p>
<p>Two double-blind trials followed. The Balanced Solution versus Saline in Intensive Care Study (BaSICS) randomized 11,052 patients in 75 Brazilian ICUs. Death by 90 days was 26.4% with a balanced solution and 27.2% with saline (adjusted hazard ratio 0.97, 95% confidence interval 0.90 to 1.05). Patients received a median of 1.5 liters on the first day.[[ntr05_2]] The Plasma-Lyte 148 versus Saline (PLUS) trial randomized 5,037 patients in 53 ICUs in Australia and New Zealand. Death by 90 days was 21.8% versus 22.0%, and new KRT 12.7% versus 12.9%.[[ntr05_3]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Trial</th><th>Design and size</th><th>Main result (balanced versus saline)</th><th>What it means for you</th></tr></thead>
<tbody>
<tr><td>SMART, 2018</td><td>Cluster-randomized, unblinded, 15,802 adults</td><td>Kidney composite 14.3% versus 15.4%</td><td>A small kidney signal in a broad ICU population</td></tr>
<tr><td>BaSICS, 2021</td><td>Double-blind, 11,052 patients</td><td>90-day death 26.4% versus 27.2%, not significant</td><td>No mortality difference at modest volumes</td></tr>
<tr><td>PLUS, 2022</td><td>Double-blind, 5,037 patients</td><td>90-day death 21.8% versus 22.0%; new KRT 12.7% versus 12.9%</td><td>No mortality or KRT difference</td></tr>
</tbody></table></div>
<p>Read together, the trials say that the type of crystalloid matters less than the amount. A balanced crystalloid is a reasonable default, especially when chloride is already high or large volumes are expected. Saline remains appropriate when the patient is hypochloremic from vomiting, and in the many Philippine wards where it is the fluid in stock. Do not let the choice of bag distract the team from the volume running through it.</p>
<h3>Albumin</h3>
<p>The Saline versus Albumin Fluid Evaluation (SAFE) trial randomized 6,997 ICU patients to 4% albumin or saline for resuscitation. Deaths at 28 days were 726 and 729 (relative risk 0.99), with no difference in organ failure, days in the ICU or days of KRT.[[ntr05_4]] The Kidney Disease: Improving Global Outcomes (KDIGO) 2012 AKI guideline suggests isotonic crystalloids rather than colloids (albumin or starches) for initial expansion of intravascular volume in patients at risk for or with AKI, in the absence of hemorrhagic shock (2B), and recommends vasopressors together with fluids in vasomotor shock (1C).[[ntr05_11]] Albumin has specific uses, such as large-volume paracentesis and some patients with cirrhosis, that belong to other modules. In the Philippines it is usually paid out of pocket, so the indication should be one the family would accept if they understood the cost.</p>
<h3>Philippine practice: dengue and floods</h3>
<p>The World Health Organization (WHO) dengue guideline describes three phases: febrile, critical and recovery. Plasma leakage occurs in the critical phase, around defervescence, and lasts about 24 to 48 hours. In the recovery phase the leaked fluid is reabsorbed, and the guideline warns that continued intravenous fluid at that stage causes fluid overload, with pleural effusion, ascites and respiratory distress.[[ntr05_12]] The same patient therefore needs generous fluid on one day and none two days later. A falling hematocrit with rising platelets and a returning appetite signal recovery; a falling hematocrit with an unstable patient may signal bleeding. After floods, leptospirosis brings patients whose lungs may bleed and whose kidneys may fail; Module 09 covers it. In both, every liter must earn its place.</p>
{{key:Choose the crystalloid sensibly, then spend your attention on the volume. The trials found small or no differences between bags and large harms from too much of any of them.}}
"""),
        ("deresus", "Stop and remove", "De-resuscitation: stopping fluid and taking it off", """
<p>A positive balance is expected in the first hours of shock. A positive balance on day three is a decision someone forgot to make. The causal chain of harm runs like this: extra interstitial fluid widens the distance oxygen must travel, so the lungs stiffen and oxygenation falls; gut wall edema slows feeding and raises abdominal pressure; venous pressure rises, and the kidney, sitting in its capsule, loses perfusion pressure and filters less. The urine output falls, someone gives more fluid for the low urine output, and the cycle tightens.</p>
<h3>The evidence for less</h3>
<p>The Fluid and Catheter Treatment Trial (FACTT) randomized 1,000 patients with acute lung injury to a conservative or a liberal fluid protocol for seven days. The cumulative 7-day balance was about &minus;136 mL with the conservative strategy and +6,992 mL with the liberal one. Death at 60 days was 25.5% versus 28.4%, a difference that was not significant. The conservative strategy increased ventilator-free days (14.6 versus 12.1) and days outside the ICU (13.4 versus 11.2) without more shock, and dialysis in the first 60 days was 10% versus 14% (not significant).[[ntr05_7]] Ventilator-free days count time patients feel, but they are not survival.</p>
<p>The Conservative versus Liberal Approach to Fluid Therapy of Septic Shock in Intensive Care (CLASSIC) trial randomized 1,554 adults with septic shock, after at least 1 liter of fluid, to restricted or standard intravenous fluid. The restricted group received a median of 1,798 mL in the ICU and the standard group 3,811 mL. Death at 90 days was 42.3% versus 42.1%, and serious adverse events did not differ.[[ntr05_8]] Restriction halved the fluid without harm or benefit to survival. Together, the two trials tell you that once the patient is past early resuscitation, less fluid is at least as safe and may shorten time on the ventilator.</p>
<h3>Diuretics: when, and how to tell they work</h3>
<p>The KDIGO 2012 guideline recommends not using diuretics to prevent AKI (1B) and suggests not using them to treat AKI except in the management of volume overload (2C).[[ntr05_11]] Diuretics do not repair the kidney. They are tools for removing salt and water from a patient who has too much.</p>
<p>The response is measured in sodium, not only in milliliters. A large urine volume with little sodium removes water but little of the extracellular excess. The heart failure trials have tested this idea. In the Pragmatic Urinary Sodium-based Treatment Algorithm in Acute Heart Failure (PUSH-AHF) trial, 310 patients were randomized to natriuresis-guided therapy, with intensification when a spot urine sodium was below 70 mmol/L at set times, or to usual care. Sodium excretion over 24 hours was higher with guidance (409 versus 345 mmol), but death or heart failure readmission at 180 days occurred in 31% of each group.[[ntr05_10]] Natriuresis is a surrogate. The trial showed that guidance moves it, not that moving it changes outcomes.</p>
<p>The Acetazolamide in Decompensated Heart Failure with Volume Overload (ADVOR) trial added acetazolamide, which blocks proximal sodium reabsorption, to loop diuretics in 519 patients. Successful decongestion within three days occurred in 42.2% versus 30.5% (risk ratio 1.46), about 12 more decongested patients per 100. Death or heart failure readmission over three months was 29.7% versus 27.8%, not significantly different.[[ntr05_9]] Both trials enrolled patients with heart failure, not AKI, and the doses used belong to the trial protocols and your unit&rsquo;s formulary, not this module.</p>
{{flow:Turning from giving to removing|Recognize the turn::Perfusion stable for 24 hours or more, a rising weight or cumulative balance, new crackles, effusions, falling oxygen saturation, or venous congestion on ultrasound.|Stop what is running::Stop maintenance fluid in a patient who can drink. Concentrate drug infusions where possible. Count the carriers.|Decide on removal::Confirm that blood pressure and perfusion allow it. Agree the goal with the attending: a daily net balance or a target weight.|Measure the response::Urine volume and, where available, spot urine sodium after the dose; weight and balance every morning; potassium, magnesium and creatinine daily.|Escalate or stop::A poor response despite escalation, refractory hyperkalemia or acidosis, or worsening oxygenation means a call about ultrafiltration or KRT (Module 10). Reaching the goal means stop.}}
<p>A modest rise in creatinine during effective decongestion is common and, with improving congestion, often reflects changes in filtration pressure rather than new tubular injury. Do not stop a working decongestion plan for a small rise without discussing it with your attending, and do not continue it blindly if the patient is becoming hypotensive or the urine output is collapsing.</p>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What you own in de-resuscitation</th></tr></thead>
<tbody>
<tr><td>Intern</td><td>Notice a fluid order older than 24 hours and ask whether it is still needed; report the weight and balance trend each morning</td></tr>
<tr><td>Resident</td><td>Propose stopping fluid and starting removal, with a numeric daily goal and the laboratory monitoring, for the attending to approve</td></tr>
<tr><td>Fellow</td><td>Choose the diuretic strategy, judge the natriuretic response, manage diuretic resistance, and decide with the attending when ultrafiltration or KRT is needed</td></tr>
</tbody></table></div>
<div class="tc-keyp"><span class="tc-lab">In children</span>Children are given fluid by weight, and maintenance volumes follow the Holliday&ndash;Segar method. The American Academy of Pediatrics (AAP) 2018 guideline recommends isotonic maintenance fluids with appropriate potassium chloride and dextrose for patients 28 days to 18 years old, because they reduce hyponatremia (evidence quality A; strong recommendation).[[ntr05_13]] Boluses are not harmless: in the Fluid Expansion as Supportive Therapy (FEAST) trial of febrile African children with impaired perfusion, 48-hour mortality was 10.5% after saline boluses and 7.3% with no bolus; the setting excluded malnutrition and gastroenteritis and had no intensive care, so apply it with care.[[ntr05_14]] See <a href="attending-pediatric-nephrologist-03-fluids-sodium-acid-base.html">Attending Pediatric Nephrologist, Module 03</a>.</div>
{{call:Stop and call the attending nephrologist when, per unit protocol, but always ask the attending nephrologist for guidance:<ul><li>Oxygen saturation is falling or the work of breathing is rising in a patient with a positive balance</li><li>Diuretics produce little urine or little sodium despite escalation</li><li>Potassium or acidosis is worsening in an overloaded patient with AKI</li><li>Blood pressure falls during fluid removal</li><li>The team cannot agree whether the patient needs fluid or needs fluid removed</li></ul>}}
{{key:Write the stop point when you start the fluid. Re-ask the question every morning: is this patient still in resuscitation, or has the time come to take the water off?}}
"""),
    ],
    "debrief": ["""
<p><strong>What the chart says.</strong> The chart already holds the diagnosis. Her cumulative balance is +5.8 liters, and her weight has risen 4.5 kg, close to 9% of her admission weight. Her fever broke two days ago, her hematocrit is falling with rising platelets, and she is warm and well perfused: she has moved from the critical phase into recovery, when leaked plasma returns to the vessels. The line is still running at the day-three rate. Dr. Santos should report in SBAR form (situation, background, assessment, recommendation): breathless with saturation 92% and crackles; dengue day six, defervescence on day four, +5.8 liters and +4.5 kg; probable fluid overload in the recovery phase; request to hold the fluid and for the resident to see her now. She should not give the bolus while she waits.</p>
""", """
<p><strong>Will more fluid help?</strong> No signs point to hypoperfusion: warm hands, quick capillary refill, a pressure of 104/62 mm Hg in a young woman, and a pulse of 96. The low urine output in a congested patient in dengue recovery is not, on its own, a reason for fluid. Dr. Villareal examines her and, being trained, does a quick ultrasound: B-lines in both lower zones, small bilateral effusions, and an IVC of 2.3 cm with little respiratory variation. He might also look at the hepatic and portal vein Doppler; a severe VExUS pattern would support congestion. She may still be technically fluid responsive, but she is not fluid tolerant. Her rising creatinine fits congestion as well as it fits dryness.</p>
""", """
<p><strong>The plan, and who decides.</strong> Stop the intravenous fluid; she can drink. Give oxygen, sit her up, and check electrolytes, magnesium, a chest radiograph and a repeat hematocrit. Dr. Villareal calls the attending, who agrees on a diuretic trial now that perfusion is stable, with a net negative daily goal, urine output and a spot urine sodium after the first dose, daily weight, and potassium and creatinine checks. The nephrology fellow is asked to see her in the morning to judge the response and to plan escalation if her oxygenation worsens or the diuretic fails. Ultrafiltration or KRT is the attending&rsquo;s decision. Dr. Santos writes the cumulative balance on the chart every morning until the weight is back near 52 kg.</p>
"""],
    "skills": {"title": "Volume assessment and a fluid order with a stop point",
               "intro": "Complete with a preceptor on the ward or in simulation. Sign-off is local.",
               "items": [
                   ("Records a same-scale weight, totals intake and output including drains and estimated insensible loss, and writes the cumulative balance", False),
                   ("Answers the three volume questions (perfusion, responsiveness, tolerance) in a written note, citing the evidence for each", False),
                   ("Performs and documents lung and IVC ultrasound, stating at least two reasons a dilated IVC may not mean excess volume", False),
                   ("Writes a fluid order that names the job of the fluid, the type, the review time and the stop point", False),
                   ("Presents a de-resuscitation plan with a daily goal, natriuresis check and laboratory monitoring to the attending", False),
               ],
               "placement": "Medical ward, emergency room or ICU, during a dengue season or with a patient past early resuscitation"},
    "quiz": [
        ("An intern wants the most reliable bedside trend of total body fluid in a ward patient. What should she rely on most?",
         ["A daily weight on the same scale at the same time, with a cumulative balance written on the chart",
          "The degree of pitting edema at the ankles each shift",
          "The intake and output total for the last 8 hours only",
          "The patient&rsquo;s report of thirst"], 0,
         "A same-scale daily weight shows that fluid has accumulated, and a cumulative balance shows the trend that single-shift totals hide. Edema reflects interstitial fluid in dependent tissue and is changed by albumin, venous disease and drugs."),
        ("A ventilated patient has an inferior vena cava of 2.4 cm with no respiratory variation. What is the most accurate interpretation?",
         ["The patient is volume overloaded and needs a diuretic",
          "Right atrial pressure is probably high, but ventilation, right ventricular failure, tricuspid regurgitation or raised abdominal pressure can cause this without excess volume",
          "The patient is fluid responsive and should receive a bolus",
          "The finding excludes venous congestion of the kidney"], 1,
         "A large, fixed IVC means high right-sided pressure, not necessarily too much fluid. Positive-pressure ventilation alone can enlarge the IVC. Treat it as one piece of a combined assessment."),
        ("In the PUSH-AHF trial of natriuresis-guided diuretic therapy, what did guidance achieve?",
         ["Lower death or heart failure readmission at 180 days",
          "No change in urinary sodium excretion",
          "More sodium excretion over 24 hours (409 versus 345 mmol) without a difference in death or readmission at 180 days (31% in each group)",
          "A reduction in AKI"], 2,
         "Natriuresis is a surrogate. Guidance moved the surrogate but did not change the clinical composite. ADVOR showed more decongestion with acetazolamide, again without a difference in death or readmission."),
        ("In SMART, major adverse kidney events at 30 days occurred in 14.3% with balanced crystalloids and 15.4% with saline. What is the best summary for a teaching round?",
         ["Balanced crystalloids halve kidney events",
          "An absolute difference of about 1.1 percentage points in a composite outcome in an unblinded single-center trial; later double-blind trials showed no mortality difference",
          "Saline should never be used in the ICU",
          "The difference was driven by mortality alone, which was significantly lower"], 1,
         "Give absolute numbers: 1.1 points, about one composite event per 90 patients. BaSICS and PLUS, both double-blind, found no difference in 90-day death. Mortality in SMART did not differ significantly."),
        ("A patient with dengue is on day six, afebrile since day four, with a falling hematocrit, rising platelets, crackles, effusions and a weight 4 kg above admission. Urine output is low. The nurse asks for a fluid bolus. What is the best next step?",
         ["Give a crystalloid bolus for the low urine output",
          "Switch the maintenance fluid to albumin",
          "Increase the maintenance rate until urine output improves",
          "Stop intravenous fluid, assess for congestion, and call the resident and attending about fluid removal"], 3,
         "This is the recovery phase, when leaked plasma is reabsorbed; WHO warns that continued intravenous fluid then causes overload. Low urine output in a congested, well-perfused patient is not a fluid trigger."),
    ],
    "terms": [
        ("AAP", "American Academy of Pediatrics"),
        ("ADVOR", "Acetazolamide in Decompensated Heart Failure with Volume Overload (trial)"),
        ("AKI", "Acute kidney injury"),
        ("BaSICS", "Balanced Solution versus Saline in Intensive Care Study"),
        ("CLASSIC", "Conservative versus Liberal Approach to Fluid Therapy of Septic Shock in Intensive Care (trial)"),
        ("FACTT", "Fluid and Catheter Treatment Trial"),
        ("FEAST", "Fluid Expansion as Supportive Therapy (trial)"),
        ("ICU", "Intensive care unit"),
        ("IVC", "Inferior vena cava"),
        ("KDIGO", "Kidney Disease: Improving Global Outcomes"),
        ("KRT", "Kidney replacement therapy"),
        ("PLUS", "Plasma-Lyte 148 versus Saline (trial)"),
        ("POCUS", "Point-of-care ultrasound"),
        ("PUSH-AHF", "Pragmatic Urinary Sodium-based Treatment Algorithm in Acute Heart Failure (trial)"),
        ("SAFE", "Saline versus Albumin Fluid Evaluation (trial)"),
        ("SBAR", "Situation, background, assessment, recommendation"),
        ("SMART", "Isotonic Solutions and Major Adverse Renal Events Trial"),
        ("VExUS", "Venous excess ultrasound (score)"),
        ("WHO", "World Health Organization"),
    ],
    "readings": [
        ("dengue-aki-kidney.html", "Dengue and the Kidney"),
        ("pocus-nephrology.html", "Point-of-Care Ultrasound in Nephrology"),
        ("physician-on-duty-08-dry-weight.html", "Physician on Duty, Module 8: Dry Weight"),
        ("attending-nephrologist-05-aki-and-post-aki-care.html", "Attending Nephrologist, Module 5: AKI and Post-AKI Care"),
    ],
    "calcs": ["calc-urine-output-fluid-balance.html", "calc-fluid-overload.html", "calc-insensible-water-loss.html",
              "calc-vexus-grading.html", "calc-rap-ivc.html", "calc-maintenance-fluids.html", "calc-holliday-segar.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
