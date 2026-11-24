# -*- coding: utf-8 -*-
"""Physician on Duty, Module 18: The Confused or Seizing Patient: Potassium, Sugar, and the Brain.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty at a dialysis recliner reads a glucose meter strip while a nurse watches a monitor showing tall, peaked T waves. The patient in the chair is drowsy.",
    "objectives": [
        "Explain why potassium rises highest before the first session of the week, why the electrocardiogram is an insensitive guide, and how dialysis lowers it.",
        "Carry out the stabilize, shift, remove sequence for high potassium in the order your unit&rsquo;s protocol sets, and recognize the low blood sugar that insulin treatment can cause.",
        "Recognize low potassium, calcium, and magnesium after a session and explain how the dialysis fluid prescription contributes.",
        "Check a bedside glucose in every confused dialysis patient, explain why sugar falls during and after dialysis, and give the first treatment per your unit&rsquo;s protocol.",
        "Work through altered consciousness and seizure in the chair using a fixed list of dialysis-specific causes, including drug toxicity.",
        "Recognize the signs of stroke, record the last-known-well time, and arrange transfer without delay.",
    ],
    "big": """
{{plain:Picture a bathtub with the drain closed from Friday afternoon to Monday morning. The tap drips all weekend. On Monday the machine opens the drain for four hours. The water is highest right before the drain opens, and it drops fastest in the first hour.}}
<p>The picture has a limit. The bathtub is only the blood and the fluid around the cells, and it holds a small share of the body&rsquo;s potassium. Almost all of it sits inside the cells, as Module 2 explained. Cells can push potassium out or pull it in within minutes. So the blood level can swing fast even when the total in the body barely changes.</p>
{{cards:Key terms for this module|Hyperkalemia::A blood potassium above the laboratory&rsquo;s normal range. Its danger is to the heart rhythm.|Hypoglycemia::A blood sugar low enough to starve the brain. In dialysis patients it is often silent.|Serum-to-dialysate gradient::The difference between the potassium in the blood and the potassium in the dialysis fluid. It drives removal.|Potassium binder::A medicine that holds potassium in the gut so it leaves in the stool.|Altered consciousness::Any change from the patient&rsquo;s usual alertness, from new confusion to no response.|Last known well::The last time someone saw the patient at their usual neurologic state. The stroke clock starts here.|Status epilepticus::A seizure that does not stop, or repeated seizures without recovery in between.}}
<p>Most dialysis patients who stop answering have a cause you can reverse within minutes, often a low sugar. A few have a potassium that can stop the heart without symptoms, or a stroke that needs a hospital now. Your work is to run a fixed list in a fixed order, treat what the unit&rsquo;s protocol allows, and call the attending nephrologist and the stroke team early.</p>
""",
    "case": {"title": "He stopped answering", "html": """
<p>Mr. Rodolfo &ldquo;Rudy&rdquo; Villanueva, 66, is a retired jeepney driver. He has had type 2 diabetes for 18 years. He dialyzes on Monday, Wednesday, and Friday through a right arm fistula. Today is Monday, and he is in hour one of the first session after the weekend. He skipped breakfast because he felt nauseated. He took his usual morning insulin at home.</p>
<p>At 7:40 a.m. the nurse, Ms. Liza Domingo, calls you to his chair. He has stopped answering questions and he is sweating. His blood pressure is 156/90 mm Hg. His heart rate is 58 per minute and regular. His oxygen saturation is 97% on room air. No one has checked his capillary glucose yet. The predialysis potassium from the 6:30 a.m. sample has come back at 6.9 mmol/L. The monitor shows tall, narrow T waves. Ms. Domingo has confirmed that both needles are in place, the blood pump is running, and there are no machine alarms. These values are illustrative, not targets.</p>
""", "questions": ["What do you check in the first minute, and why that before anything else?",
                  "How do you rank the potassium against the confusion: is one causing the other, or are there two problems?",
                  "If insulin is used for the potassium, what must happen over the next several hours, and who sets it?"]},
    "sections": [
        ("kpeak", "Why potassium peaks", "Why potassium peaks on Monday morning", """
<p>A healthy kidney excretes almost all the potassium a person eats each day. In kidney failure that exit is nearly closed. The colon excretes a little more than usual, and any remaining urine carries some away. The rest accumulates until the next session.[[palmer2016]][[clase2020]]</p>
{{fig:pod02_potassium|Almost all potassium sits inside cells. A small shift across the cell wall makes a large change in the blood.}}
<p>The blood level also depends on where potassium sits. Acidosis, lack of insulin, nonselective beta-blockers, tissue breakdown, and hemolysis in the circuit (Module 16) each move potassium out of the cells.[[palmer2016]]</p>
<p>The gap from Friday to Monday is about three days; the other gaps are about two. So the week&rsquo;s highest potassium comes before the first session after the long gap.</p>
{{fig:pod18_weekly}}
<h3>What the evidence shows</h3>
<p>The Dialysis Outcomes and Practice Patterns Study (DOPPS) followed 55,183 patients in 20 countries. Higher serum potassium was associated with death and arrhythmia. Dialysis fluid potassium of 2 versus 3 mEq/L was not associated with either, and moved predialysis potassium very little, about 0.09 mEq/L for each 1 mEq/L of dialysis fluid potassium.[[karaboyas2017]] In a case-control study of cardiac arrest inside dialysis clinics, dialysis fluid potassium below 2 mEq/L was associated with arrest.[[pun2011]] Both are observational, and sicker patients may receive different prescriptions, so neither proves cause.</p>
<h3>The electrocardiogram is an insensitive guide</h3>
<p>A chart review of 90 hospitalized patients with a potassium of 6 mmol/L or more found the electrocardiogram (ECG) insensitive for high potassium. Changes became more likely as potassium rose, but no T-wave threshold could be set, and readers agreed only moderately.[[montague2008]]</p>
{{fig:pod15_ecg_strips|Peaked T waves and wide QRS complexes are warnings when present. Their absence does not clear a high potassium.}}
<p>Read the predialysis potassium as soon as the laboratory reports it. Send any high value to the attending nephrologist with a current ECG.</p>
{{key:A normal ECG does not make a high potassium safe. Treat the number and the patient, not the tracing alone.}}
"""),
        ("ktreat", "Stabilize, shift, remove", "High potassium: stabilize, shift, remove", """
<p>Three moves: protect the heart muscle, push potassium into the cells, and take it out of the body. Only the last lowers total body potassium.</p>
{{fig:pod18_ssr}}
<h3>How each move works</h3>
<p>A heart muscle cell fires when its resting voltage reaches a threshold. High outside potassium moves the resting voltage closer to that threshold. Sodium channels are inactivated, and conduction slows. Calcium raises the threshold and restores the gap, without lowering potassium.[[palmer2016]]</p>
<p>Insulin and beta-2 agonists such as salbutamol drive the sodium-potassium pump, and potassium moves into cells within minutes. The effect lasts hours, then potassium comes back out. Insulin is given with glucose to prevent a low sugar.[[palmer2016]] Dialysis removes potassium from the body. In a patient already connected, it is the definitive step.[[mahoney2005]] Shifting can blunt removal: in 7 hemodialysis patients, salbutamol before dialysis cut the potassium the session removed by about 40%.[[allon1995]] Whether to add a shifting drug once dialysis is running is for the order set and the attending nephrologist.</p>
<h3>What the evidence shows</h3>
<p>A Cochrane review of mostly small randomized trials found that inhaled or nebulized salbutamol and intravenous insulin with glucose each lowered potassium, and the combination more than either alone. Dialysis was effective, bicarbonate equivocal, and a resin not effective by four hours. No trial reported deaths or arrhythmias.[[mahoney2005]]</p>
<p>A 2025 systematic review linked to the International Liaison Committee on Resuscitation (ILCOR) included 101 studies. In adults, insulin with glucose, salbutamol, or both lowered potassium by 0.7 to 1.2 mmol/L on average, with very low to low certainty of evidence. Bicarbonate had no effect. The review found no evidence of a clinical benefit of calcium.[[jessen2025]] The Cochrane authors cited anecdotal and animal data for calcium when arrhythmias are present.[[mahoney2005]] Calcium rests on physiology and practice, not trials. A fall in potassium is a surrogate, and no trial shows that any of these treatments prevents death. The Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference report on potassium is a conference statement, not a graded recommendation.[[clase2020]]</p>
{{flow:High potassium in the chair: stabilize, shift, remove|Recognize::Read the potassium and look at the patient and the ECG. Weakness, a slow pulse, or a wide QRS raises the stakes.|Stabilize::If the ECG shows changes, give calcium as the unit&rsquo;s order set directs. Keep the patient on a cardiac monitor.|Shift::Give insulin with glucose, an inhaled beta-agonist, or both, as the order set directs.|Remove::Keep dialysis running. It is the treatment. Ask the attending nephrologist about extending the session or changing the dialysis fluid.|Watch the sugar::Arrange glucose checks for several hours after any insulin, at the times the protocol sets.|Call::Call the attending nephrologist with the value, the ECG, and what you have given.}}
<h3>The hidden harm: low sugar after insulin</h3>
<p>In 221 treated episodes in hospitalized hemodialysis patients, hypoglycemia below 60 mg/dL followed in 13%. It came at a median of 2 hours after the insulin and lasted a median of 2 hours. Patients without diabetes, and those with a lower starting glucose, were at higher risk.[[apel2014]] In a second hospital series of 219 patients, 8.7% became hypoglycemic and 2.3% severely so. Of those who did, 79% had acute kidney injury or were on hemodialysis.[[schafers2012]]</p>
<p>A healthy kidney clears a large share of the body&rsquo;s insulin. In kidney failure that clearance falls, and insulin lasts longer than the glucose given with it.[[abe2015]] One emergency department changed its protocol to favor a lower insulin amount in kidney disease. Hypoglycemia fell from 28% of 76 patients to 11% of 63 patients.[[mcnicholas2018]] That was a before-and-after study, so other changes may have contributed. All of these data come from hospitals, not outpatient dialysis units. The insulin amount, the glucose given with it, and the check schedule belong to the unit&rsquo;s order set, which the Medical Director sets.</p>
{{fig:pod18_gradient}}
{{formula:<strong>Worked example A. Illustrative arithmetic, not a prescription.</strong><br>Serum-to-dialysate potassium gradient = predialysis serum potassium &minus; dialysis fluid potassium.<br>Start of session: 6.9 mmol/L &minus; 2.0 mmol/L = 4.9 mmol/L.<br>Mid-session, serum potassium 4.0 mmol/L: 4.0 &minus; 2.0 = 2.0 mmol/L.<br>The gradient has fallen by more than half, so removal slows as the session goes on.[[karaboyas2017]]<br>What it tells you: removal is fastest early, and the blood falls faster than the cells release potassium, so the level rebounds afterward. What it does not tell you: the post-dialysis potassium, or which dialysis fluid to use, which is the attending nephrologist&rsquo;s order.}}
{{call:Stop and call the attending nephrologist at once for a high potassium with any ECG change, muscle weakness, a slow or irregular pulse, or any value above your unit&rsquo;s action threshold. Start the order set while you call.}}
"""),
        ("kprevent", "Preventing the next high", "Preventing the next high: diet, binders, and what the trials show", """
<p>Picture a sponge in the gut that soaks up potassium and leaves in the stool. The picture has a limit: binders exchange potassium for sodium or calcium, and they act over days, not minutes.[[natale2020]]</p>
<h3>What the trials measured</h3>
<p>The question is whether a binder prevents what a high potassium predicts: arrhythmia and sudden death. A lower potassium is only a surrogate for those events.</p>
<div class="table-wrap"><table>
<thead><tr><th>Study</th><th>Design and size</th><th>Surrogate result (potassium)</th><th>Patient outcome result</th></tr></thead>
<tbody>
<tr><td>DIALIZE, sodium zirconium cyclosilicate</td><td>Randomized, double-blind, 196 hemodialysis patients, 4-week evaluation</td><td>41.2% versus 1.0% kept predialysis potassium 4.0 to 5.0 mmol/L after the long gap[[fishbane2019]]</td><td>Not designed to test outcomes</td></tr>
<tr><td>DIALIZE-Outcomes, sodium zirconium cyclosilicate</td><td>Randomized, 2,690 hemodialysis patients, stopped early</td><td>Normal potassium at 12 months in 74.0% versus 47.0%[[fishbane2025]]</td><td>Sudden cardiac death, stroke, or arrhythmia events in 8.8% versus 8.9% (hazard ratio 0.98, 95% confidence interval 0.76 to 1.26)[[fishbane2025]]</td></tr>
<tr><td>Patiromer trial</td><td>Open-label, randomized, 33 hemodialysis patients, 4 weeks</td><td>13 versus 41 episodes of potassium 5.5 mEq/L or more in week 4[[middleton2024]]</td><td>No difference in arrhythmias on 7-day monitors, in a trial too small to show one[[middleton2024]]</td></tr>
<tr><td>Cochrane review</td><td>15 randomized trials, 1,849 participants, 3 trials in hemodialysis</td><td>Potassium lower by 0.62 mEq/L, low certainty[[natale2020]]</td><td>Newer binders may make little or no difference to death (risk ratio 0.69, 95% confidence interval 0.11 to 4.32), low certainty[[natale2020]]</td></tr>
</tbody></table></div>
<p>DIALIZE-Outcomes stopped with about a third of the planned events, because events were fewer than expected and many patients stopped the study drug. Low potassium occurred in 3.0% on the binder and 1.4% on placebo.[[fishbane2025]] The early stop means it cannot exclude a modest benefit. It does show that better potassium control did not bring fewer arrhythmia events over the time studied.</p>
{{key:Binders lower the number. They have not yet been shown to prevent the events the number predicts.}}
<h3>Diet</h3>
<p>The KDIGO conference moved away from blanket dietary potassium restriction toward healthy eating patterns, including plant-based foods. It noted that few data show diet changes alone return a high serum potassium to normal.[[clase2020]] Module 23 covers food in detail. Hidden sources still matter, such as salt substitutes made with potassium chloride.</p>
<h3>What you do</h3>
<p>Report a pattern of predialysis highs with the dates and ECGs. Ask about missed or shortened sessions, new medicines, constipation, and diet. Binders, dialysis fluid potassium, and diet referral are decisions for the attending nephrologist and the dietitian. The dietary potassium calculator on the site helps when you review a food record together.</p>
"""),
        ("aftersession", "Low after the session", "Low after the session: potassium, calcium, and magnesium", """
<p>Sometimes the drain works too well. A low-potassium dialysis fluid pulls the blood level down fast during the session. The cells have not yet given back their stores, so the blood level is lowest at the end. Over the next hours potassium moves out of the cells again, and the level rebounds.[[daugirdas2015]][[karaboyas2017]]</p>
<h3>Why a fast fall matters to the heart</h3>
<p>The heart responds to the ratio of potassium inside and outside the cell. A fast fall outside lengthens repolarization, seen as a long QT interval. Low calcium and low magnesium lengthen it too, and digoxin or QT-prolonging medicines add risk. The DOPPS authors noted that the blood-to-dialysis fluid gradient drives fast electrolyte shifts, which may contribute to arrhythmias.[[karaboyas2017]]</p>
{{cards:Three lows after a session|Low potassium::Weakness, palpitations, extra beats, or a long QT after a session with a low-potassium dialysis fluid, poor intake, vomiting, or diarrhea.|Low calcium::Tingling around the mouth or in the fingers, muscle twitching, cramps, a long QT. Read it against the albumin, and ask for an ionized calcium if the picture does not fit.|Low magnesium::Tremor, weakness, extra beats, a long QT. It often travels with low potassium and makes it harder to correct.}}
<h3>What the evidence shows</h3>
<p>A case-control study compared 502 patients who had a cardiac arrest inside dialysis clinics with 1,632 matched controls, drawn from 43,200 patients. Those who arrested were more often exposed to dialysis fluid potassium below 2 mEq/L, and to low-calcium dialysis fluid. Their predialysis potassium did not explain the difference.[[pun2011]] In DOPPS, outcomes did not differ between 2 and 3 mEq/L baths.[[karaboyas2017]] The two do not conflict: one studied baths below 2 mEq/L, the other two common baths. Both are observational. The best dialysis fluid potassium for a given patient is unknown, and none of the sources in this module sets one number for everyone. The attending nephrologist chooses it.</p>
<h3>What you do</h3>
<p>For palpitations, weakness, or tingling around the mouth after a session, obtain an ECG and ask for electrolytes per your unit&rsquo;s protocol. Measure the QT interval and correct it for heart rate; the corrected QT calculator on the site does the arithmetic. Read a low calcium against the albumin, and check for digoxin and QT-prolonging medicines. Give replacement only as the unit&rsquo;s protocol allows, and report to the attending nephrologist, who owns the dialysis fluid prescription.</p>
{{key:A rhythm problem after a session is a dialysis fluid question until proven otherwise. Send the ECG, the electrolytes, and the bath to the attending nephrologist.}}
"""),
        ("sugar", "Sugar falls in the chair", "Sugar falls in the chair", """
<p>Glucose crosses the dialyzer membrane the way urea does. If the dialysis fluid holds less glucose than the blood, glucose leaves with every pass, and the organs that would top it up are slow.</p>
{{fig:pod18_sugar}}
<h3>Why the sugar falls</h3>
<p>Glucose diffuses into a dialysis fluid that holds little or none, and some moves into red cells. A healthy kidney makes a share of the body&rsquo;s new glucose between meals; a failed kidney makes little. The failed kidney also clears insulin slowly, so insulin and sulfonylureas act longer than expected. Many patients eat little before a morning session. Hours after the session, a rebound high sugar may follow.[[abe2015]]</p>
<p>Autonomic neuropathy blunts the warning signs of a low sugar, and beta-blockers blunt the fast pulse and tremor, though sweating often remains. The first sign may be confusion, drowsiness, odd behavior, or a seizure.</p>
<h3>What the evidence shows</h3>
<p>A Japanese study used continuous glucose monitors in 98 hemodialysis patients with type 2 diabetes whose dialysis fluid contained 100 to 150 mg/dL of glucose. Sensor glucose still fell steadily during dialysis, and in half of them dropped below the dialysis fluid glucose. Twenty-one patients (21%) had hemodialysis-related hypoglycemia below 70 mg/dL, during the session or before the next meal. Every one of these episodes was asymptomatic.[[hayashi2021]] A small study of 20 patients compared dialysis fluids with and without glucose. Hypoglycemia during the session occurred only with glucose-free or glucose-poor fluid, and it was linked to a lower predialysis glucose.[[burmeister2015]] Both are observational. They suggest that glucose in the dialysis fluid lowers the risk without removing it, and that a low starting sugar is a warning.</p>
<p>Ask whether your unit&rsquo;s dialysis fluid contains glucose (Module 7).</p>
<h3>What you do</h3>
<p>Check a capillary glucose in every confused, sweaty, unusually drowsy, or seizing dialysis patient. Only airway, breathing, and circulation come before it. Treat a low value as your unit&rsquo;s protocol directs, by mouth if the patient can swallow safely, and recheck at the protocol&rsquo;s interval. Then find out what insulin or sulfonylurea was taken, when, and what the patient ate, and report it to the attending nephrologist. Long-term diabetes regimens belong to Module 22.</p>
{{formula:<strong>Worked example B. Illustrative decision walk-through, not a protocol.</strong><br>A patient without diabetes has a starting glucose of 95 mg/dL. At 8:00 a.m. she receives insulin with glucose under the unit&rsquo;s hyperkalemia order set.<br>Published median time to hypoglycemia after insulin = 2 hours; median duration = 2 hours.[[apel2014]]<br>Median onset: 8:00 + 2 hours = 10:00 a.m. Median end of the low: 10:00 + 2 hours = 12:00 noon.<br>A watch that ends at 9:00 a.m. misses most of the risk. In this illustration the checks run from 8:00 a.m. to at least noon, longer if values are falling.<br>What it tells you: the window is hours long, and this patient&rsquo;s profile carries higher risk. What it does not tell you: the schedule or the glucose to give. Those are in the unit&rsquo;s protocol.}}
{{key:Check the sugar first. It takes one minute, and it is the cause you can reverse fastest.}}
"""),
        ("brain", "Confusion and seizure", "Confusion and seizure in the chair: a fixed list", """
<p>Think of a checklist taped to the machine, run in the same order every time, fastest reversible causes first.</p>
<p>The brain needs steady glucose, oxygen, blood pressure, and a stable chemical bath. Dialysis disturbs all of these at once: it removes fluid, shifts electrolytes and water, and is often given with heparin. The patient also carries drugs that the kidney would have cleared.[[greenberg2021]][[saha2017]]</p>
{{flow:Altered consciousness in the chair: the order of checks|Airway and breathing::Look, listen, and check the oxygen saturation. Give oxygen per protocol. Confirm that the access and needles are secure.|Glucose::Capillary glucose now. Treat a low value per protocol.|Pressure::A low pressure starves the brain. Module 13 covers the response.|Oxygen::Hypoxia from fluid overload or a dialyzer reaction. Look at the breathing pattern.|Electrolytes and the ECG::Potassium, calcium, magnesium, and sodium. A rhythm strip.|Drugs::Review what was given today and what accumulates in kidney failure.|Stroke signs::Face, arm, speech, gaze. Record the last-known-well time.|Infection::Temperature, the catheter site, and the chest. Module 17 covers fever.}}
<h3>Causes special to dialysis</h3>
<div class="table-wrap"><table>
<thead><tr><th>Cause</th><th>Clue at the chair</th><th>First check</th><th>Who to call</th></tr></thead>
<tbody>
<tr><td>Low sugar</td><td>Sweating, drowsiness, odd behavior; insulin or a sulfonylurea taken, little eaten</td><td>Capillary glucose</td><td>Attending nephrologist after treatment per protocol</td></tr>
<tr><td>Potassium, calcium, magnesium, or sodium</td><td>Weakness, tingling, twitching, an abnormal ECG</td><td>ECG and electrolytes</td><td>Attending nephrologist</td></tr>
<tr><td>Low pressure</td><td>Yawning, dim vision, a late-session drop</td><td>Blood pressure (Module 13)</td><td>Attending nephrologist if no recovery</td></tr>
<tr><td>Hypoxia</td><td>Breathlessness, crackles, a falling saturation</td><td>Oxygen saturation</td><td>Attending nephrologist; emergency team if severe</td></tr>
<tr><td>Disequilibrium</td><td>A new patient with a very high urea in the first sessions; headache, nausea, restlessness</td><td>Session number and urea (Module 12)</td><td>Attending nephrologist</td></tr>
<tr><td>Drug toxicity</td><td>Confusion, myoclonus, or drowsiness after a new or increased medicine</td><td>Medicine list (Module 20)</td><td>Attending nephrologist</td></tr>
<tr><td>Infection and sepsis</td><td>Fever, chills, a catheter, low pressure</td><td>Temperature and the catheter site (Module 17)</td><td>Attending nephrologist</td></tr>
<tr><td>Stroke or bleeding in the head</td><td>Facial droop, one-sided weakness, slurred speech, sudden severe headache</td><td>Face-arm-speech check, last-known-well time</td><td>Attending nephrologist and emergency transfer</td></tr>
<tr><td>Air embolism</td><td>Sudden cough, chest tightness, collapse, air in the venous line</td><td>The venous line and the air detector (Module 16)</td><td>Call for help now; attending nephrologist</td></tr>
<tr><td>Uremia</td><td>Missed sessions, drowsiness, twitching</td><td>Attendance record and urea</td><td>Attending nephrologist</td></tr>
</tbody></table></div>
<h3>Drugs that build up</h3>
<p>Several medicines cleared by the kidney accumulate in kidney failure, and their toxicity looks like a brain problem: gabapentin and pregabalin (drowsiness, confusion), cefepime (confusion, myoclonus, nonconvulsive seizures), acyclovir and valacyclovir (confusion, hallucinations), baclofen (drowsiness, coma), and some opioids. Module 20 covers dosing. At the chair, look for a new medicine, a recent increase, or a prescription from a doctor who did not know the patient is on dialysis.</p>
<h3>Seizures</h3>
<p>A seizure in kidney failure often has a metabolic cause: low sugar, low sodium, low calcium, uremia, or drug toxicity. A review put the incidence of uremic seizures in kidney failure at about 10%. They are often nonconvulsive and can mimic the drowsy confusion of uremia. Antiseizure drugs behave differently in kidney failure, and dialysis removes some of them.[[titoff2019]] A patient who stays confused after a seizure needs a neurologic assessment, not only time.</p>
{{flow:Seizure at the machine|Protect::Keep the patient in the chair, turned to the side. Hold the access arm so the needles stay in.|Stop the blood pump::Per protocol, stop the pump. Decide with the nurse whether the blood can be returned safely or the lines should be clamped.|Airway and oxygen::Clear the airway and give oxygen per protocol.|Glucose::Check a capillary glucose and treat a low value per protocol.|Call::Call for help in the unit and call the attending nephrologist. Time the seizure.|Antiseizure drug::Give only the drug the unit&rsquo;s protocol names, by the person it authorizes. Doses differ in kidney failure.|Transfer::A seizure that does not stop, or repeated seizures without recovery, is status epilepticus. Arrange emergency transfer.}}
{{call:Stop and call the attending nephrologist for every seizure, and for any new confusion that does not clear once the glucose and the pressure are corrected. Call for emergency transfer for status epilepticus.}}
"""),
        ("stroke", "Stroke and the call card", "Stroke: the clock starts at last-known-well", """
<p>Picture a stopwatch that started when the nurse last saw the patient normal, not when you reached the chair. Every stroke treatment depends on that time.</p>
<h3>Why stroke is common in the chair</h3>
<p>Dialysis patients often carry high blood pressure, diabetes, atrial fibrillation, and hardened arteries at once. Dialysis adds its own risks: pressure falls during the session, and heparin raises the risk of bleeding. In a population-based United States cohort, incident dialysis patients had hospitalized stroke rates 4.4 to 9.7 times those of the general population, depending on sex and race group.[[seliger2003]] A Japanese single-center series of 151 strokes in hemodialysis patients over 22 years found that 34% of brain infarctions began during dialysis or within 30 minutes after it. Only 19% of brain hemorrhages did.[[toyoda2005]] Both are observational.</p>
{{fig:pod18_clock}}
<h3>What the evidence says about treatment</h3>
<p>Clot-dissolving treatment (thrombolysis) and clot removal (thrombectomy) work only within time windows. Trial data in dialysis patients are scarce. In a large United States registry of 44,410 patients given thrombolysis, chronic kidney disease was not associated with more symptomatic brain hemorrhage after adjustment, although in-hospital death was higher.[[ovbiagele2014]] In a national database, 1,072 dialysis-dependent patients given thrombolysis had brain hemorrhage rates similar to other patients (5.2% versus 6.1%). Their in-hospital death rate was higher, 22% versus 11%, with an adjusted odds ratio of 1.92.[[tariq2013]] These are observational data. Dialysis patients are sicker, and the excess deaths may reflect that rather than the treatment.</p>
<p>The 2026 American Heart Association/American Stroke Association (AHA/ASA) guideline for acute ischemic stroke replaced the 2018 guideline and its 2019 update. It revised thrombolytic choice and eligibility and thrombectomy eligibility.[[prabhakaran2026]] The stroke team at the receiving hospital decides eligibility, not the dialysis chair. Your job is to get the patient there fast with the facts the team needs.</p>
<h3>What you do</h3>
<p>Look for a facial droop, a drifting arm, slurred speech, a gaze to one side, or a sudden severe headache. Check the glucose, because a low sugar can mimic stroke. Record the last-known-well time and the heparin given this session. Stop dialysis per protocol, and return the blood if the circuit is sound. Arrange urgent transfer to a stroke-capable hospital and call the attending nephrologist. The stroke scale calculator on the site helps you describe the deficit. Module 19 covers heparin and bleeding.</p>
{{formula:<strong>Worked example C. Illustrative times on a transfer note, not an eligibility decision.</strong><br>Heparin bolus given: 7:30 a.m.<br>Last seen at her usual state by the nurse: 9:10 a.m.<br>Deficit noticed: 9:45 a.m.<br>Departure by ambulance: 10:05 a.m.<br>Elapsed from last known well to departure = 10:05 &minus; 9:10 = 55 minutes. Elapsed from heparin to departure = 10:05 &minus; 7:30 = 2 hours 35 minutes.<br>What it tells you: the clock is counted from 9:10, not from 9:45, and the stroke team needs the heparin time. What it does not tell you: whether she can receive thrombolysis. That is the stroke team&rsquo;s decision.}}
{{call:Stop and call the attending nephrologist, and arrange emergency transfer, for any new focal weakness, facial droop, slurred speech, or sudden severe headache. Do not wait for the session to finish.}}
{{key:Write down two times at once: when the patient was last normal, and when heparin was last given.}}
{{flow:Call card: the confused, seizing, or weak patient|Recognize::New confusion, drowsiness, sweating, twitching or seizure, slurred speech, one-sided weakness, or palpitations with weakness.|First 2 minutes::Airway and oxygen per protocol. Capillary glucose. Blood pressure. ECG and the latest potassium. Face-arm-speech check. Note the last-known-well time.|Stop dialysis?::Stop the blood pump per protocol for a seizure, a suspected stroke, or an unstable rhythm. For a high potassium without instability, dialysis is the treatment: do NOT stop it without the attending nephrologist.|Return the blood?::Yes, when the circuit is intact and the patient can receive it safely per protocol. Do NOT return the blood if air in the line or hemolysis is suspected (Module 16); clamp the lines and keep the circuit.|Call::The attending nephrologist at once. Emergency transfer to a stroke-capable hospital for stroke signs, status epilepticus, or a dangerous arrhythmia. The code team for arrest (Module 15).|Write::The times of symptom onset, last known well, heparin, and insulin. Glucose and potassium values. ECG findings. Treatments given under protocol. Who was called and when. Where the patient went.}}
"""),
    ],
    "debrief": ["""
<p><strong>What do you check in the first minute?</strong> After a glance at the airway and breathing, you ask for a capillary glucose. He took insulin, skipped breakfast, and is losing glucose into the dialysis fluid. Low sugar is the likeliest cause of his confusion and the fastest to reverse. The reading is 46 mg/dL (illustrative). Ms. Domingo treats it under the unit&rsquo;s protocol. Within minutes he wakes and asks for his wife. His face-arm-speech check is normal, and you record when he was last seen well.</p>
<p><strong>How do you rank the potassium against the confusion?</strong> There are two problems. High potassium causes weakness and rhythm problems, rarely confusion. The low sugar explains the confusion, and its quick reversal confirms it. The potassium of 6.9 mmol/L with peaked T waves and a pulse of 58 is the more dangerous problem, because it can stop the heart without warning. You keep him on the monitor and start the hyperkalemia order set. Dialysis is the treatment, so it keeps running. You call the attending nephrologist with both problems, the ECG, and the fact that he was hypoglycemic minutes ago, which weighs on whether insulin is added while dialysis is removing potassium.</p>
<p><strong>If insulin is used, what must happen next?</strong> Glucose checks continue for several hours, because published hypoglycemia after insulin began at a median of 2 hours and lasted a median of 2 hours.[[apel2014]] Mr. Villanueva is at higher risk: he has already been low, has not eaten, and his own insulin is still acting. The amounts and the check schedule come from the unit&rsquo;s order set, which the Medical Director sets. You make sure he eats, the checks continue past the end of dialysis, and he goes home only when the attending nephrologist agrees.</p>
"""],
    "skills": {"title": "Bedside glucose and focused neurologic screen in a confused dialysis patient",
               "intro": "Perform this assessment on a simulated patient or a colleague in a dialysis chair while your preceptor observes and plays the nurse.",
               "items": [
                   ("Confirms the airway and breathing, and that the access and needles are secure.", True),
                   ("Obtains a capillary glucose within the first minute and states the unit&rsquo;s action level from the protocol.", True),
                   ("Checks the blood pressure and oxygen saturation and relates them to the low-pressure response in Module 13.", False),
                   ("Reviews the latest potassium and asks for an ECG; names the ECG features of high potassium and states that a normal ECG does not exclude it.", True),
                   ("Records the level of consciousness with the Glasgow Coma Scale and checks the pupils.", False),
                   ("Performs a face-arm-speech screen and records the last-known-well time.", True),
                   ("Records the time and amount of the last heparin, and any insulin or sulfonylurea taken today.", False),
                   ("Reviews the medicine list for gabapentin, pregabalin, cefepime, acyclovir or valacyclovir, baclofen, and opioids.", False),
                   ("Decides with the nurse, per protocol, whether to stop the blood pump and whether returning the blood is safe.", False),
                   ("States when the blood must not be returned.", True),
                   ("Calls the attending nephrologist with an SBAR summary (situation, background, assessment, recommendation) and arranges transfer when indicated.", True),
                   ("Documents events, times, values, and actions in the session record.", False),
               ],
               "placement": "For two weeks, look at the predialysis potassium and the morning glucose history of every patient with diabetes on your first session after the long gap. Note any value that would have triggered the order set, and review the list with your preceptor and the attending nephrologist."},
    "quiz": [
        ("Why is the predialysis potassium usually highest on the first session of the week?",
         ["The dialysis fluid potassium is higher on Mondays",
          "Patients eat more potassium on weekends than on weekdays",
          "The long gap gives about three days of intake with almost no kidney excretion",
          "Weekend acidosis drives potassium into the cells"], 2,
         "Intake continues while the exit is nearly closed."),
        ("A patient&rsquo;s predialysis potassium is 7.0 mmol/L and the ECG looks normal. What is the best interpretation?",
         ["The heart may still be at risk, because the ECG is insensitive for high potassium",
          "The sample is probably hemolyzed and can be ignored",
          "The normal ECG shows the potassium is safe today",
          "Only patients with diabetes show ECG changes"], 0,
         "The ECG is insensitive for high potassium."),
        ("What does intravenous calcium do in high potassium?",
         ["It binds potassium in the blood",
          "It moves potassium into cells",
          "It removes potassium through the gut",
          "It raises the firing threshold of heart muscle without lowering potassium"], 3,
         "Calcium protects the membrane; potassium does not change."),
        ("A man on dialysis has a potassium of 6.8 mmol/L in hour one, with peaked T waves. He is otherwise stable. The nurse asks whether to stop dialysis while the order set is started. What is the best answer?",
         ["Stop dialysis so the medicines can work",
          "Keep dialysis running, because it removes potassium, and call the attending nephrologist",
          "Stop dialysis and transfer him to the emergency room",
          "Lower the blood pump speed until the ECG improves"], 1,
         "Dialysis is the step that removes potassium from the body."),
        ("What did the 2025 systematic review of acute hyperkalemia treatment find?",
         ["Calcium lowered potassium more than insulin",
          "Bicarbonate was the most effective single treatment",
          "Insulin with glucose, salbutamol, or both lowered potassium on average, with very low to low certainty",
          "All treatments reduced deaths from arrhythmia"], 2,
         "Average falls were 0.7 to 1.2 mmol/L. No clinical benefit was shown for calcium or bicarbonate."),
        ("A woman without diabetes receives insulin with glucose for high potassium at 9:00 a.m. Her starting glucose was 92 mg/dL. When is she most likely to become hypoglycemic, based on published data?",
         ["Within 10 minutes",
          "Around 2 hours later, and the low may last about 2 hours",
          "Only after 12 hours",
          "Never, because glucose was given with the insulin"], 1,
         "Median onset was 2 hours, median duration 2 hours. Patients without diabetes were at higher risk."),
        ("What did DIALIZE-Outcomes show about sodium zirconium cyclosilicate in hemodialysis patients?",
         ["It improved potassium control but did not reduce arrhythmia-related events",
          "It reduced sudden cardiac death by half",
          "It caused more arrhythmias than placebo",
          "It had no effect on serum potassium"], 0,
         "Normokalemia 74.0% versus 47.0%; events 8.8% versus 8.9%."),
        ("Which statement about potassium binders in dialysis is best supported?",
         ["They prevent sudden death",
          "They replace the need for dialysis",
          "They work within minutes in an emergency",
          "They lower a surrogate value; benefit on patient outcomes is not shown"], 3,
         "No trial has shown fewer deaths or arrhythmias."),
        ("Two hours after a session with a low-potassium dialysis fluid, a patient on digoxin reports palpitations. What is the best first step?",
         ["Reassure him; this is normal after dialysis",
          "Obtain an ECG and electrolytes, and call the attending nephrologist",
          "Give an extra dose of digoxin",
          "Change the dialysis fluid for the next session yourself"], 1,
         "Low potassium with digoxin raises arrhythmia risk."),
        ("Why does blood sugar tend to fall during dialysis?",
         ["Dialysis raises insulin production",
          "The dialyzer adds insulin to the blood",
          "Glucose leaves into the dialysis fluid, insulin is cleared slowly, and the failed kidney makes little new glucose",
          "Glucose is converted into urea in the dialyzer"], 2,
         "Several links act together."),
        ("A woman with type 2 diabetes becomes quiet and drowsy in hour three. Her pressure is normal. What do you check first?",
         ["Capillary glucose",
          "Serum magnesium",
          "A head scan",
          "Her hemoglobin"], 0,
         "It takes one minute, and lows in the chair are often silent."),
        ("A man on dialysis started a new medicine for shingles from another doctor three days ago. Today he is confused and hallucinating in the chair. Glucose, pressure, and oxygen are normal. What is the most likely cause?",
         ["Dialysis disequilibrium",
          "Air embolism",
          "Low potassium",
          "Accumulation of acyclovir or valacyclovir"], 3,
         "These drugs accumulate in kidney failure and cause confusion and hallucinations."),
        ("A patient has a generalized seizure during dialysis. Which sequence fits this module?",
         ["Give the antiseizure drug from memory, then check glucose",
          "Remove the needles at once and send him to the emergency room",
          "Protect the patient and the access, stop the blood pump per protocol, airway and oxygen, glucose, and call",
          "Wait for the seizure to stop before doing anything"], 2,
         "Protect first. The antiseizure drug comes from the unit&rsquo;s protocol."),
        ("At 9:45 a.m. a nurse notices a new facial droop. She last saw the patient normal at 9:10 a.m. Heparin was given at 7:30 a.m. From what time does the stroke clock run?",
         ["7:30 a.m.",
          "9:10 a.m.",
          "9:45 a.m.",
          "The time the patient arrives at the hospital"], 1,
         "The clock starts at last known well."),
        ("What do the registry data on thrombolysis in dialysis patients show?",
         ["Similar brain hemorrhage rates, but higher in-hospital death, in observational data",
          "Thrombolysis is contraindicated in all dialysis patients",
          "Dialysis patients have half the brain hemorrhage rate of others",
          "Randomized trials prove the benefit is the same as in other patients"], 0,
         "Hemorrhage 5.2% versus 6.1%; death 22% versus 11%. The stroke team decides eligibility."),
    ],
    "terms": [("Hyperkalemia", "A blood potassium above the laboratory&rsquo;s normal range. Its main danger is to the heart rhythm."),
              ("Serum-to-dialysate potassium gradient", "The difference between blood potassium and dialysis fluid potassium. It drives removal and narrows as the session goes on."),
              ("Potassium rebound", "The rise in blood potassium in the hours after a session, as potassium moves out of the cells again."),
              ("Potassium binder", "A medicine that holds potassium in the gut so it leaves in the stool. It acts over days."),
              ("Surrogate outcome", "A laboratory value or measurement used in place of an outcome patients feel, such as death or arrhythmia."),
              ("Hemodialysis-related hypoglycemia", "A low blood sugar during a session or before the next meal, often without symptoms."),
              ("Nonconvulsive seizure", "Seizure activity in the brain without obvious jerking. It can look like drowsiness or confusion."),
              ("Status epilepticus", "A seizure that does not stop, or repeated seizures without recovery in between."),
              ("Last known well", "The last time someone saw the patient at their usual neurologic state. Stroke treatment windows count from it."),
              ("Thrombolysis", "Treatment that dissolves a clot blocking a brain artery. The stroke team decides eligibility.")],
    "readings": [("potassium-hyperkalemia-ckd.html", "How potassium builds up in kidney disease, and the foods and medicines that raise it."),
                 ("sugar-control-kidney-disease.html", "Why blood sugar behaves differently in kidney failure, and how low sugars happen."),
                 ("epilepsy-seizures-ckd.html", "Seizures in kidney disease, and how antiseizure medicines change when the kidneys fail.")],
    "calcs": ["calc-potassium-load.html", "calc-qtc.html", "calc-nihss.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
