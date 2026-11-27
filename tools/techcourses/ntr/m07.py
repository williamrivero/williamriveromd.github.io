# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 07: Potassium, magnesium and arrhythmia risk.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. UKKA severity
bands checked on the guideline site (July 2026 update); KDIGO 2020 conference described as a conference statement, not
a graded recommendation; Montague 2008, STOP ACEi, DIAMOND, HARMONIZE and Huang and Kuo 2007 checked against PubMed.
PhilHealth hemodialysis benefit as in the blueprint (confirm on date of service). No doses. Fictional case."""

MODULE = {
    "image_alt": "In a Tacloban emergency room after a typhoon, a Filipino resident points to wide QRS complexes on a cardiac monitor while an intern attaches electrocardiogram leads to a hemodialysis patient with a fistula in his left arm.",
    "objectives": [
        "<strong>Intern:</strong> Recognize electrocardiogram (ECG) danger signs of hyperkalemia and hypokalemia, put the patient on a cardiac monitor, and call your resident at once with the potassium, the ECG and the dialysis history.",
        "<strong>Resident:</strong> Run the stabilize, shift and remove sequence for hyperkalemia under supervision, monitor potassium and glucose for rebound and hypoglycemia, and treat hypokalemia with attention to magnesium.",
        "<strong>Fellow:</strong> Prevent recurrence by finding the cause, keeping renin&ndash;angiotensin&ndash;aldosterone system (RAAS) inhibitors where they protect the patient, choosing potassium binders that are available and affordable, and building a dialysis and disaster plan.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the heart&rsquo;s electrical margin</span>Potassium kills through the heart, sometimes within minutes and often without warning symptoms. The <b>intern</b> owns the first look: a monitor on the patient, an ECG in hand, and a call before anyone debates the number. The <b>resident</b> owns the sequence: protect the heart, push potassium into cells, then take it out of the body. The <b>fellow</b> owns the next episode: why it happened, what keeps it from happening again, and how to do that without taking away the medicines that protect the kidney and heart.</div>
{{plain:Think of a heart cell as a dam holding back a river. The water level on the far side, the resting membrane potential, is set mainly by how much potassium sits inside the cell compared with outside. The gate that opens to start each heartbeat needs a clear drop between the water and the top of the dam.}}
<p>The picture has a limit. A dam either holds or breaks, but a heart cell fails in graded steps. When plasma potassium rises, the gradient across the membrane narrows and the resting potential becomes less negative. At first the cell is easier to excite. Then sodium channels, which must reset at a negative voltage, start to stay inactivated, conduction slows, and the ECG changes from peaked T waves to a lengthened PR interval, a widening QRS, a sine wave, and finally ventricular fibrillation or asystole. When plasma potassium falls, the resting potential becomes more negative but repolarization slows, the QT and U waves lengthen, and ectopic beats and torsades become more likely, especially with digoxin or ischemia. The same number can be safe in one patient and lethal in another, depending on how fast it changed and what else the heart carries.</p>
<p>About 98% of the body&rsquo;s potassium is inside cells, held there by the sodium&ndash;potassium pump. Insulin and beta-2 adrenergic stimulation drive the pump and move potassium into cells within minutes. Over hours, the kidney excretes the daily intake in the distal nephron, where aldosterone and sodium delivery set the pace. In kidney failure, the gut takes over part of that excretion, and dialysis removes the rest. Each layer is a treatment target.</p>
{{cards:Key numbers|Severity (UK Kidney Association)::Mild 5.5&ndash;5.9; moderate 6.0&ndash;6.4; severe &ge;6.5 mmol/L|ECG sensitivity (Montague 2008)::In 90 patients with potassium &ge;6 mmol/L, the ECG was insensitive; no diagnostic threshold could be set|STOP angiotensin-converting enzyme inhibitor (ACEi), 411 patients with eGFR below 30::eGFR at 3 years 12.6 after stopping versus 13.3 after continuing RAS inhibitors (no significant difference)|DIAMOND, 878 patients with heart failure::Hyperkalemia events 77.7 versus 118.2 per 100 person-years with patiromer versus placebo|KDIGO 2020 potassium conference::Conference statements, not graded recommendations}}
<p>Most hyperkalemia on a medical service is mild, chronic and drug related, and the work is adjustment rather than rescue. A few patients arrive with a potassium and an ECG that can stop the heart within the hour, most often a dialysis patient who missed sessions. Your work is to recognize that patient at once, to treat in the right order, and then to prevent the next episode without abandoning the kidney-protective medicines that caused the first.</p>
""",
    "case": {"title": "Two sessions missed after the storm",
             "html": """
<p>Tuesday, 4 p.m., the emergency room of a regional hospital in Tacloban City, four days after a typhoon. Mr. Danilo Paca&ntilde;a, 58, a fisherman with diabetic kidney disease, dialyzes every Monday, Wednesday and Friday through a left arm fistula at a freestanding unit. The unit lost power and road access, and he missed Friday&rsquo;s and Monday&rsquo;s sessions. He takes losartan and makes almost no urine. With the town short of food, his family has been eating bananas and drinking coconut water from fallen trees.</p>
<p>He says his legs feel heavy and weak. His blood pressure is 168/96 mm Hg, his pulse 52 per minute, his oxygen saturation 94% on room air, and he has mild crackles at both bases. His potassium is 7.4 mmol/L, bicarbonate 15 mmol/L and glucose 186 mg/dL. The ECG shows tall, peaked T waves, a PR interval of 240 ms and a QRS of 130 ms.</p>
<p>The intern, Dr. Rhea Abellana, has just attached the leads. The internal medicine resident on duty, Dr. Miguel Dacanay, arrives. The nearest hospital hemodialysis unit is running on a generator and has a waiting list.</p>
""",
             "questions": ["Which findings are dangerous, and what is the very first treatment?",
                           "What is the full sequence for the next two hours, and what will you monitor?",
                           "How will the team prevent the next episode, including his losartan and the next typhoon?"]},
    "sections": [
        ("physiology", "Physiology", "Potassium physiology: shift, excretion and the heart", """
<p>Potassium handling has two clocks. The fast clock is <b>internal balance</b>: the shift of potassium between cells and plasma over minutes. The slow clock is <b>external balance</b>: excretion by the kidney and gut over hours to days. A meal containing potassium would raise the plasma level dangerously if insulin and catecholamines did not first move most of it into cells while the kidney slowly excretes it.</p>
<p>The kidney filters potassium and reabsorbs most of it before the distal nephron. What appears in the urine is mostly secreted in the connecting tubule and collecting duct. Secretion needs three things: sodium arriving to be reabsorbed through the epithelial sodium channel, which leaves the lumen negative; aldosterone, which increases sodium channels and the pump; and enough tubular flow to carry the secreted potassium away through the renal outer medullary potassium (ROMK) channel. Any drug that blocks one of these steps raises potassium.</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>What raises potassium</th><th>What lowers potassium</th></tr></thead>
<tbody>
<tr><td>Shift into cells</td><td>Insulin deficiency, beta blockade, acidosis from mineral acids, hypertonicity, cell breakdown (rhabdomyolysis, tumor lysis, hemolysis)</td><td>Insulin, beta-2 agonists, alkalosis, refeeding, rapid red cell production</td></tr>
<tr><td>Aldosterone effect</td><td>Angiotensin-converting enzyme (ACE) inhibitors, angiotensin receptor blockers (ARBs), mineralocorticoid receptor antagonists, heparin, calcineurin inhibitors, adrenal insufficiency</td><td>Primary aldosteronism, licorice, high-dose steroids</td></tr>
<tr><td>Distal sodium delivery and flow</td><td>Low effective volume, acute kidney injury (AKI), advanced chronic kidney disease (CKD), potassium-sparing diuretics, trimethoprim</td><td>Loop and thiazide diuretics, osmotic diuresis, vomiting with bicarbonaturia</td></tr>
<tr><td>Intake</td><td>Salt substitutes, bananas, coconut water and other high-potassium foods when excretion is limited; potassium supplements</td><td>Poor intake (rarely alone)</td></tr>
<tr><td>Extra-renal loss</td><td>Missed dialysis; constipation in kidney failure</td><td>Diarrhea, laxatives, gastrointestinal fistulas</td></tr>
</tbody></table></div>
<h3>Is the potassium real?</h3>
<p>Before you treat, ask whether the sample is telling the truth. Hemolysis during a difficult blood draw, a tight tourniquet with fist clenching, delayed processing, very high platelet or white cell counts, and drawing above an infusion can all raise measured potassium without raising the plasma level in the patient (pseudohyperkalemia). A high potassium in a patient with a normal ECG and no reason for it deserves an immediate repeat, ideally from a free-flowing vein, with a heparinized sample if the platelet or white count is very high. A high potassium with a reason, or with ECG change, is treated while you repeat it.</p>
{{key:Look at three things together: the number, the ECG and the reason. A dangerous potassium with a reason is treated at once; a surprising potassium with no reason and a normal ECG is repeated at once.}}
"""),
        ("hyperkalemia", "Hyperkalemia", "Hyperkalemia: stabilize, shift, remove", """
<p>The UK Kidney Association (UKKA) guideline grades hyperkalemia as mild (5.5 to 5.9 mmol/L), moderate (6.0 to 6.4 mmol/L) and severe (6.5 mmol/L or more).[[ntr07_2]] The Kidney Disease: Improving Global Outcomes (KDIGO) 2020 Controversies Conference addressed acute and chronic hyperkalemia in kidney disease; its conclusions are conference statements, not graded recommendations.[[ntr07_1]] Both describe the same physiological sequence.</p>
<p>The ECG helps when it is abnormal and misleads when it is normal. Montague and colleagues reviewed 90 patients admitted with potassium of 6 mmol/L or more and a concurrent ECG; the ECG was insensitive for hyperkalemia, changes became more likely as potassium rose, readers agreed only moderately, and no diagnostic threshold could be established.[[ntr07_3]] A normal ECG does not make a potassium of 7 mmol/L safe. Chronic dialysis patients often tolerate levels that would cause arrhythmias in someone whose potassium rose suddenly, but no one can predict which patient will arrest.</p>
{{fig:ntr07_a}}
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Mechanism</th><th>Onset and duration</th><th>What you must watch</th></tr></thead>
<tbody>
<tr><td>1. Stabilize: intravenous calcium</td><td>Restores the gap between resting and threshold potential; does not lower potassium</td><td>Minutes; effect wears off, so repeat ECG and treatment may be needed</td><td>Give for ECG changes or severe hyperkalemia per protocol; caution with digoxin</td></tr>
<tr><td>2. Shift: insulin with glucose</td><td>Drives the sodium&ndash;potassium pump; potassium moves into cells</td><td>Within the first hour; lasts a few hours</td><td>Glucose for several hours afterward; hypoglycemia is common when kidney function is low</td></tr>
<tr><td>2. Shift: nebulized beta-2 agonist</td><td>Drives the pump through beta-2 receptors</td><td>Within the first hour; additive to insulin</td><td>Tachycardia; some patients respond little</td></tr>
<tr><td>2. Shift: sodium bicarbonate</td><td>Small, slow effect on potassium</td><td>Unreliable</td><td>Reserve for metabolic acidosis; sodium and volume load</td></tr>
<tr><td>3. Remove: potassium binders</td><td>Exchange potassium in the gut</td><td>Hours</td><td>Constipation, sodium load, availability and cost</td></tr>
<tr><td>3. Remove: diuretics</td><td>Increase distal flow and secretion</td><td>Hours, if the kidney responds</td><td>Volume status; useless in anuria</td></tr>
<tr><td>3. Remove: hemodialysis</td><td>Diffusion into potassium-poor dialysate</td><td>Fastest removal; rebound after the session</td><td>Arrhythmia risk if potassium falls very fast; recheck after</td></tr>
</tbody></table></div>
<p>The shift agents buy time; they do not remove potassium. When they wear off, potassium returns to the plasma. Recheck potassium within the first hours, as your protocol sets, and again later for rebound, and recheck glucose repeatedly after insulin. The specific drugs, doses and concentrations come from your unit&rsquo;s protocol and the attending; this module gives none.</p>
<p>In a patient with kidney failure, dialysis is the removal step. A missed session is the commonest cause of life-threatening hyperkalemia in a dialysis patient. After Hurricane Katrina in the United States, missed sessions were associated with hospitalization among hemodialysis patients.[[ntr07_9]] Philippine typhoons, floods and power outages do the same. PhilHealth covers up to 156 hemodialysis sessions a year for patients registered in the PhilHealth Dialysis Database (PDD), at PHP 6,350 per session effective October 9, 2024; confirm the rates on the date of service.[[ntr07_12]][[ntr07_13]] Coverage does not help if the unit is flooded, so the plan for a missed session must exist before the storm.</p>
{{flow:Hyperkalemia: the first two hours|Monitor and ECG::Cardiac monitor, 12-lead ECG, intravenous access, repeat potassium if no reason and normal ECG. Check glucose.|Stabilize::Intravenous calcium per protocol for ECG changes or severe hyperkalemia. Repeat the ECG after.|Shift::Insulin with glucose, with or without a nebulized beta-2 agonist, per protocol. Glucose checks for several hours.|Remove::Arrange dialysis for a patient with kidney failure; binders and diuretics where the kidney or gut can do the work. Stop potassium sources, supplements and offending drugs for now.|Recheck::Potassium within the first hours per protocol and again later for rebound; ECG after each step; glucose repeatedly.|Hand off::Write the potassium times, treatments, ECG changes and the plan for removal in the note and the handoff.}}
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What you own in hyperkalemia</th></tr></thead>
<tbody>
<tr><td>Intern</td><td>Monitor, ECG and call within minutes; note dialysis schedule, last session, urine output and every medicine; draw the repeat sample correctly</td></tr>
<tr><td>Resident</td><td>Lead the sequence under supervision; set recheck times; escalate to dialysis early in kidney failure; watch for hypoglycemia</td></tr>
<tr><td>Fellow</td><td>Decide on urgent dialysis and the dialysate potassium with the attending; investigate the cause; plan prevention</td></tr>
</tbody></table></div>
{{call:Stop and call the attending nephrologist now, per unit protocol, but always ask the attending nephrologist for guidance, when:<ul><li>The ECG shows a widening QRS, bradycardia, a sine-wave pattern or any arrhythmia</li><li>Potassium is 6.5 mmol/L or more, or rising despite treatment</li><li>A dialysis patient has missed sessions and has a high potassium or fluid overload</li><li>Glucose falls after insulin, or the potassium rebounds after the shift agents wear off</li><li>Dialysis is not available within the time the patient needs it</li></ul>}}
{{fig:ntr07_b}}
{{key:Protect, shift, remove, recheck. Calcium protects the heart but lowers nothing; insulin and beta-agonists move potassium but remove nothing; only the kidney, the gut and dialysis take it out.}}
"""),
        ("hypokalemia-mg", "Hypokalemia and magnesium", "Hypokalemia and magnesium: the refill that leaks", """
<p>Hypokalemia comes from too little intake (rarely alone), a shift into cells, or losses through the gut or kidney. Weakness, ileus, rhabdomyolysis and arrhythmia follow as it deepens. The ECG shows flattened T waves, U waves and a longer QT interval; the risk is highest with digoxin, heart disease and other QT-prolonging drugs. Severe hypokalemia can paralyze the respiratory muscles.</p>
<p>Magnesium is the partner most often forgotten. Magnesium inside the cell normally blocks potassium leaving through ROMK channels in the distal nephron. Huang and Kuo reviewed evidence that magnesium deficiency removes that block and increases distal potassium secretion, so hypokalemia becomes refractory to potassium replacement. Magnesium deficiency alone does not always cause hypokalemia; increased distal sodium delivery or high aldosterone, as with diuretics or vomiting, is usually needed as well.[[ntr07_7]] Drugs commonly cause hypomagnesemia, including diuretics and proton pump inhibitors.[[ntr07_10]] Proton pump inhibitors are widely used and bought without prescription in the Philippines.</p>
<div class="table-wrap"><table>
<thead><tr><th>Cause group</th><th>Urine clue</th><th>Examples</th></tr></thead>
<tbody>
<tr><td>Shift into cells</td><td>Urine potassium low; total body potassium normal</td><td>Insulin, beta-2 agonists, thyrotoxic or familial periodic paralysis, refeeding</td></tr>
<tr><td>Gastrointestinal loss</td><td>Urine potassium low (unless vomiting with bicarbonaturia)</td><td>Diarrhea, laxatives</td></tr>
<tr><td>Kidney loss with high blood pressure</td><td>Urine potassium high</td><td>Primary aldosteronism, licorice, Cushing syndrome</td></tr>
<tr><td>Kidney loss with normal or low blood pressure</td><td>Urine potassium high</td><td>Diuretics, vomiting, magnesium deficiency, tubulopathies, some antibiotics and amphotericin</td></tr>
</tbody></table></div>
<p>The urine potassium-to-creatinine ratio on a spot sample separates kidney from extra-renal loss, and the site has calculators for it. The transtubular potassium gradient (TTKG) rests on assumptions about urea and osmole handling in the collecting duct that often fail, so read it with caution. The KDIGO 2020 conference proposed a diagnostic algorithm for hypokalemia that puts the clinical context first.[[ntr07_1]] The context usually answers the question faster than any ratio: a woman on a diuretic, a man with diarrhea, a young adult with sudden paralysis after a large carbohydrate meal.</p>
{{formula:<strong>Arithmetic illustration, not a target.</strong> Urine potassium-to-creatinine ratio = urine potassium (mmol/L) &divide; urine creatinine (mmol/L).<br>Urine potassium 30 mmol/L and urine creatinine 6 mmol/L: ratio 5 mmol/mmol, which points to kidney loss in a hypokalemic patient; a low ratio points to gut loss or a shift.}}
{{key:When hypokalemia will not correct, check and correct magnesium. Potassium poured into a leaking bucket keeps draining until the magnesium plugs the leak.}}
"""),
        ("prevention", "Prevention", "Preventing the next episode without losing kidney protection", """
<p>Many patients with hyperkalemia are taking an ACE inhibitor, an ARB or a mineralocorticoid receptor antagonist, because these drugs slow CKD and save lives in heart failure. Stopping them after one high potassium removes that protection permanently in many patients, because nobody restarts them. The KDIGO 2021 blood pressure guideline includes a practice point that hyperkalemia associated with renin&ndash;angiotensin system (RAS) inhibitors (RASi) can often be managed by measures to lower potassium rather than by decreasing the dose or stopping the drug.[[ntr07_8]]</p>
<p>The STOP ACEi (stopping ACE inhibitors or ARBs in advanced CKD) trial tested stopping in advanced CKD. It randomized 411 patients with an estimated glomerular filtration rate (eGFR) below 30 mL/min per 1.73 m&sup2; and progressive disease to stop or continue RAS inhibitors. At 3 years the eGFR was 12.6 with stopping and 13.3 with continuing, a difference of &minus;0.7 that was not significant. Kidney failure or the start of kidney replacement therapy (KRT) occurred in 62% versus 56% (hazard ratio 1.28, 95% confidence interval 0.99 to 1.65), and cardiovascular events and deaths were similar.[[ntr07_4]] Stopping did not help kidney function; eGFR is a surrogate, but the hard kidney outcome also did not favor stopping.</p>
<h3>Potassium binders</h3>
<p>The newer binders were tested mainly on potassium, a surrogate, and on the ability to keep RAAS inhibitors. In the HARMONIZE (sodium zirconium cyclosilicate in outpatients) trial, open-label sodium zirconium cyclosilicate lowered potassium from 5.6 to 4.5 mmol/L at 48 hours in 258 outpatients, with 84% normokalemic by 24 hours; in the randomized maintenance phase all three doses kept potassium lower than placebo for 28 days. Edema was more common at the highest dose (14% versus 2% with placebo), and hypokalemia occurred at the higher doses.[[ntr07_6]] In the DIAMOND (patiromer in heart failure) trial of 878 patients with heart failure and reduced ejection fraction who reached target RAAS inhibitor doses during a patiromer run-in, patiromer reduced hyperkalemia events (77.7 versus 118.2 per 100 person-years; hazard ratio 0.66) and the need to reduce mineralocorticoid receptor antagonist doses, with similar adverse events.[[ntr07_5]] Neither trial showed fewer deaths or kidney failure.</p>
<div class="table-wrap"><table>
<thead><tr><th>Binder type</th><th>What the evidence shows</th><th>Philippine reality</th></tr></thead>
<tbody>
<tr><td>Sodium zirconium cyclosilicate</td><td>Fast, sustained potassium lowering (HARMONIZE); sodium load and edema at higher doses</td><td>Out-of-pocket; may not be stocked in provincial hospitals</td></tr>
<tr><td>Patiromer</td><td>Fewer hyperkalemia events while keeping RAAS inhibitors in heart failure (DIAMOND)</td><td>Out-of-pocket; availability varies</td></tr>
<tr><td>Older resins (sodium or calcium polystyrene sulfonate)</td><td>Older and weaker evidence; gut adverse effects</td><td>Widely available and cheaper; often the only option</td></tr>
</tbody></table></div>
<p>The KDIGO 2020 conference noted growing evidence associating plant-based diets with better outcomes and urged a shift from blanket dietary potassium restriction toward healthy eating patterns, while noting that few data show diet changes restore an abnormal potassium to normal.[[ntr07_1]] For a dialysis patient, the advice is different: high-potassium foods such as bananas and coconut water can be dangerous when sessions are missed. Teach the family what to eat during a typhoon week, when dialysis may stop for days.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>Pseudohyperkalemia is common in infants and young children because heel-prick and squeezed capillary samples hemolyze easily; repeat a surprising result from a free-flowing sample. Newborns, especially preterm infants, can have high potassium in the first days of life, and treatments are dosed by weight from the pediatric formulary. A review of electrolyte emergencies in children describes the same stabilize, shift and remove sequence with pediatric dosing.[[ntr07_11]] See <a href="attending-pediatric-nephrologist-04-electrolyte-emergencies.html">Attending Pediatric Nephrologist, Module 04</a>.</div>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What you own in prevention</th></tr></thead>
<tbody>
<tr><td>Intern</td><td>List every potassium source and potassium-raising drug, including salt substitutes and herbal products; ask about missed sessions and food during disasters</td></tr>
<tr><td>Resident</td><td>Propose a plan to keep or restart RAAS inhibitors with monitoring; consider binders, diuretics and acidosis correction</td></tr>
<tr><td>Fellow</td><td>Choose an affordable binder strategy; write the dialysis patient&rsquo;s emergency plan (alternative unit, diet during disruption, when to come to the emergency room)</td></tr>
</tbody></table></div>
{{key:Treat the high potassium, not the drug that protects the kidney. Stop the RAAS inhibitor only when other measures fail, and if you stop it, write when it will be restarted.}}
"""),
    ],
    "debrief": ["""
<p><strong>The danger, and the first treatment.</strong> Mr. Paca&ntilde;a has severe hyperkalemia with ECG changes that signal impaired conduction: a long PR interval, a QRS of 130 ms and a slow pulse of 52. His weak, heavy legs fit hyperkalemic muscle weakness. Dr. Abellana has him on a monitor and calls immediately. The first treatment is intravenous calcium per protocol, to stabilize the membrane; it buys minutes and lowers no potassium. Dr. Dacanay repeats the ECG after it and watches for narrowing of the QRS.</p>
""", """
<p><strong>The sequence, and what to monitor.</strong> Next comes the shift: insulin with glucose and a nebulized beta-2 agonist, per protocol, with capillary glucose checks for several hours because insulin acts longer when kidney function is absent. His acidosis may justify bicarbonate on the attending&rsquo;s advice, mindful of his crackles and the sodium load. The removal step is dialysis: he is anuric, so binders alone are too slow. Dr. Dacanay calls the attending nephrologist, who arranges urgent dialysis at the hospital unit despite the waiting list. Potassium is rechecked within the first hours and again later, because the shift wears off; the ECG is repeated after each step.</p>
""", """
<p><strong>The next episode.</strong> The cause was two missed sessions, a high-potassium diet during the food shortage, and losartan. The fellow reviews him the next day. Losartan protects his heart, and the decision whether to continue it, perhaps with a binder the family can afford, belongs to the attending; it should not be stopped and forgotten. The family is taught which foods to avoid when a session is missed. The fellow writes an emergency plan: the nearest alternative dialysis unit, the phone numbers, a low-potassium food list for typhoon weeks, and the rule to come to the emergency room for weakness or palpitations after a missed session.</p>
"""],
    "skills": {"title": "Hyperkalemia response and prevention plan",
               "intro": "Complete with a preceptor on a real or simulated patient. Sign-off is local.",
               "items": [
                   ("Recognizes ECG features of dangerous hyperkalemia (peaked T waves, long PR, wide QRS, bradycardia, sine wave) on sample tracings", False),
                   ("States when to repeat a potassium for possible pseudohyperkalemia and how to draw the repeat correctly", False),
                   ("Runs the stabilize, shift, remove sequence in the correct order in simulation, naming the purpose and limit of each step without quoting doses", False),
                   ("Writes recheck times for potassium and glucose after shift therapy", False),
                   ("Explains the magnesium&ndash;potassium link and checks magnesium in refractory hypokalemia", False),
                   ("Writes an emergency plan for a dialysis patient covering a missed session during a typhoon", False),
               ],
               "placement": "Emergency room, medical ward or hemodialysis unit"},
    "quiz": [
        ("An intern receives a potassium of 7.1 mmol/L for a dialysis patient. Which ECG finding most demands an immediate call and treatment?",
         ["A sinus rhythm of 88 per minute",
          "A QRS duration of 140 ms with a slow pulse",
          "A single premature atrial beat",
          "A normal axis"], 1,
         "Widening QRS and bradycardia signal impaired conduction from sodium channel inactivation and can progress to a sine wave and arrest. A normal ECG would not make 7.1 mmol/L safe either; Montague found the ECG insensitive."),
        ("A resident has given intravenous calcium to a patient with hyperkalemia and ECG changes. The QRS has narrowed. What is the most important next step?",
         ["Shift potassium into cells with insulin and glucose (with or without a beta-2 agonist), then arrange removal, and recheck potassium and glucose",
          "Recheck the potassium tomorrow morning",
          "Nothing more; calcium has corrected the potassium",
          "Give a second dose of calcium every hour instead of other treatment"], 0,
         "Calcium protects the heart but does not lower potassium. Shift agents buy hours; removal by kidney, gut or dialysis is required, and potassium rebounds when shift agents wear off."),
        ("What did the STOP ACEi (angiotensin-converting enzyme inhibitor) trial show in patients with advanced, progressive CKD (eGFR below 30)?",
         ["Stopping RAS inhibitors raised eGFR by about 5 mL/min per 1.73 m&sup2;",
          "Continuing RAS inhibitors doubled the risk of kidney failure",
          "Stopping RAS inhibitors did not improve eGFR at 3 years (12.6 versus 13.3), and kidney failure or KRT was 62% versus 56%",
          "Stopping RAS inhibitors reduced deaths"], 2,
         "Stopping did not help the surrogate (eGFR) or the hard outcome. The KDIGO 2021 practice point favors lowering potassium over stopping RASi where possible."),
        ("A woman on furosemide and a proton pump inhibitor has a potassium of 2.7 mmol/L that has not risen despite two days of replacement. What should be checked and corrected?",
         ["Thyroid function",
          "Urine calcium",
          "Serum magnesium",
          "Serum phosphate"], 2,
         "Magnesium deficiency releases its block on distal ROMK channels and increases potassium secretion, especially with a diuretic raising distal sodium delivery. Both furosemide and proton pump inhibitors cause hypomagnesemia."),
        ("A 70-year-old man with essential thrombocythemia (platelets 1,200,000 per microliter) and normal kidney function has a serum potassium of 6.6 mmol/L. His ECG is normal and he takes no potassium-raising drugs. What is the best next step?",
         ["Start urgent dialysis",
          "Repeat the potassium from a free-flowing vein, using a heparinized plasma sample",
          "Give calcium and insulin immediately",
          "Start a potassium binder and recheck next week"], 1,
         "Very high platelet counts release potassium when blood clots in the tube, producing pseudohyperkalemia. With no reason for true hyperkalemia and a normal ECG, repeat it correctly at once."),
    ],
    "terms": [
        ("ACE", "Angiotensin-converting enzyme"),
        ("AKI", "Acute kidney injury"),
        ("ARB", "Angiotensin receptor blocker"),
        ("CKD", "Chronic kidney disease"),
        ("DIAMOND", "Trial of patiromer for hyperkalemia in heart failure with reduced ejection fraction"),
        ("ECG", "Electrocardiogram"),
        ("eGFR", "Estimated glomerular filtration rate"),
        ("HARMONIZE", "Trial of sodium zirconium cyclosilicate for hyperkalemia in outpatients"),
        ("KDIGO", "Kidney Disease: Improving Global Outcomes"),
        ("KRT", "Kidney replacement therapy"),
        ("PDD", "PhilHealth Dialysis Database"),
        ("RAAS", "Renin&ndash;angiotensin&ndash;aldosterone system"),
        ("RAS", "Renin&ndash;angiotensin system"),
        ("RASi", "Renin&ndash;angiotensin system inhibitors"),
        ("ROMK", "Renal outer medullary potassium (channel)"),
        ("STOP ACEi", "Trial of stopping ACE inhibitors or ARBs in advanced chronic kidney disease"),
        ("TTKG", "Transtubular potassium gradient"),
        ("UKKA", "UK Kidney Association"),
    ],
    "readings": [
        ("potassium-hyperkalemia-ckd.html", "Potassium and Hyperkalemia in CKD"),
        ("attending-nephrologist-06-electrolyte-emergencies.html", "Attending Nephrologist, Module 6: Electrolyte Emergencies"),
        ("physician-on-duty-18-potassium-sugar-and-the-brain.html", "Physician on Duty, Module 18: Potassium, Sugar and the Brain"),
        ("typhoon-disaster-preparedness-dialysis.html", "Typhoon and Disaster Preparedness for Dialysis Patients"),
    ],
    "calcs": ["calc-potassium-load.html", "calc-urine-k-creatinine-ratio.html", "calc-ttkg.html", "calc-magnesium-replacement.html",
              "calc-electrolyte-repletion.html", "calc-qtc.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
