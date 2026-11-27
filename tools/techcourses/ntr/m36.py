# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 36: Integrated capstone, disaster readiness and transition.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. Katrina, Sandy,
Kopp 2007, KDIGO 2020 potassium conference, I-PASS and ten Cate against PubMed; UK Kidney Association severity bands and the
CDC emergency dialysis advice checked on the web. No doses, infusion rates or order sets. Fictional case."""

MODULE = {
 'image_alt': 'In a provincial hospital emergency room after a typhoon, a medical intern, a resident and a nephrology fellow gather at the bedside of a breathless man on hemodialysis while a nurse runs an ECG and rain still streaks the windows.',
 'objectives': [
  '<strong>Intern:</strong> Present an integrated case of a dialysis patient who missed sessions, name the immediate dangers in order, and hand off using a structured format.',
  '<strong>Resident:</strong> Manage an admission end to end, from stabilizing hyperkalemia and fluid overload to arranging dialysis, transfer if needed, and a safe discharge with a disaster plan.',
  '<strong>Fellow:</strong> Defend a longitudinal plan for the patient and the unit, including disaster readiness, and teach it to the team using an entrustment-based portfolio.',
 ],
 'big': """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the whole patient, in the worst week of the year</span>This module puts the track together. The intern is first to see the patient and must recognize, in minutes, that a man who missed two dialysis sessions is in danger from potassium, fluid and acid, and say so clearly. The resident turns that recognition into a sequence of actions and a plan that survives the night. The fellow asks the longer questions: why did he miss dialysis, what will happen in the next typhoon, and what should this unit and this patient change. All three hand off, document and teach.</div>
{{plain:Think of a patient on hemodialysis as a house with a blocked drain that is pumped out three times a week. Between pumpings, water and waste rise slowly. Miss one pumping and the level is high; miss two and it is over the doorstep.}}
<p>The picture has a limit. The things that rise are not one fluid. Potassium rises from food and from cells, and its danger is electrical: the resting membrane potential of heart muscle shifts, conduction slows, and the rhythm can fail without warning. Salt and water rise and fill the lungs. Acid accumulates and drives more potassium out of cells. A storm adds its own insults: no refrigerator, salted and canned food, no medicines, crowded evacuation centers, injury and infection. The danger does not rise in a straight line, and a patient can feel well until shortly before he arrests.</p>
{{cards:Key numbers|Hurricane Katrina, 386 New Orleans patients on HD::44% missed at least one session and almost 17% missed three or more (survey, Anderson 2009)|Missing three or more sessions and hospitalization::Adjusted odds ratio 2.16 compared with missing none (observational)|Hurricane Sandy, 13,264 patients::59% received early dialysis before landfall; emergency department visits 4.1% versus 2.6% and 1.7% in comparison groups (retrospective cohort)|Severe hyperkalemia (UK Kidney Association)::Potassium 6.5 mmol/L or higher|Medicines to keep for emergencies (CDC advice to patients)::At least a 3-day supply of each}}
<p>Most patients who miss dialysis in a disaster survive if they are found early, stabilized in the right order and dialyzed. A few die at home or in an evacuation center before anyone knows they missed a session. Your work is to treat the first group quickly and well, and to build the plans, with each patient and with the unit, that make the second group smaller in the next storm.</p>
""",
 'case': {'title': 'The morning after the typhoon',
  'html': """
<p>Thursday, 5:50 a.m., the emergency room of a provincial hospital in Naga City, Camarines Sur. A strong typhoon crossed the province on Monday. Mr. Rodel Caballero, 54, a fish vendor with diabetes and hypertension, dialyzes every Monday, Wednesday and Friday at a freestanding unit in a nearby town through a left arm fistula. The unit was flooded and without power from Monday to Wednesday, so he missed both sessions. His family brought him by pedicab and then a borrowed truck through flooded roads.</p>
<p>He is sitting upright, breathless and anxious. Blood pressure 178/100 mm Hg, pulse 56 per minute and irregular, respiratory rate 30 per minute, oxygen saturation 87% on room air. He has crackles to both mid-lungs and pitting edema to the knees. The fistula has a good thrill. His potassium is 7.4 mmol/L, bicarbonate 13 mmol/L, glucose 268 mg/dL. The electrocardiogram (ECG) shows peaked T waves, absent P waves and a QRS of 0.14 seconds. During the storm he ate dried fish and canned sardines from the relief packs, and he has had no medicines since Sunday.</p>
<p>The hospital&rsquo;s hemodialysis (HD) unit is running on a generator; the head nurse says water treatment is working but only two machines can run. The medical intern, Dr. Ana Robles, sees him first. The resident on duty is Dr. Miguel Tan; the nephrology fellow, Dr. Grace Villanueva, is on her way.</p>
""",
  'questions': ['How should the intern present this patient and hand off, and what are the immediate dangers in order?',
                'How should the resident manage the admission from now to discharge, including what to do if dialysis is delayed?',
                'What longitudinal and disaster plan should the fellow defend for Mr. Caballero and for his unit?']},
 'sections': [
  ('disaster', 'Disaster readiness', 'Typhoons, floods and power: why dialysis patients are harmed', """
<p>The Philippines takes typhoons every year, and its dialysis patients depend on electricity, treated water, transport and a unit that stays open. The causal chain of harm is predictable. The storm closes the unit or the road. Sessions are missed. Potassium, fluid and acid accumulate faster because the emergency food is salty and potassium-rich and the medicines have run out. The patient presents late, often at a hospital that is itself on a generator. Each link is a place to intervene.</p>
<p><strong>What the evidence shows.</strong> Most of it comes from United States hurricanes, because they were studied. After Hurricane Katrina, 94 dialysis facilities in the Gulf Coast states closed for at least a week, and existing emergency plans did not provide continuity of care.[[ntr36_3]] Among 386 patients from nine New Orleans units interviewed afterward, 44% missed at least one session and almost 17% missed three or more. Missing three or more was more likely in patients who had been on dialysis less than 2 years, had missed sessions before the storm, lived alone, did not know their facility&rsquo;s emergency plan, did not evacuate before landfall, or were placed in a shelter, and it was associated with hospitalization (adjusted odds ratio 2.16, 95% confidence interval 1.05 to 4.43).[[ntr36_1]] After Hurricane Sandy, in 13,264 patients, 59% received early dialysis before landfall; afterward, emergency department visits were 4.1% versus 2.6% and 1.7% in the two comparison groups, hospitalization 4.5% versus 3.2% and 3.8%, and 30-day mortality 1.83% versus 1.47% and 1.60%.[[ntr36_2]] Both studies are observational, from another health system, and cannot prove that preparation prevents death; they do show who is at risk and that early dialysis before a storm is feasible on a large scale.</p>
<p><strong>What patients are told to do.</strong> The United States Centers for Disease Control and Prevention (CDC) advises dialysis patients to keep an emergency kit with contact numbers for their doctor, their regular unit and another unit nearby, a list of their medicines with at least a 3-day supply of each, to follow a 3-day emergency diet if they cannot get dialysis, and to tell the person in charge of a shelter about their medical needs.[[ntr36_4]] The emergency diet does not replace dialysis; it limits potassium, salt and fluid to buy time. Adapt it to Filipino relief food: dried fish, canned meat and instant noodles are salty, and bananas and coconut water are high in potassium.</p>
{{fig:ntr36_a}}
<div class="table-wrap"><table><thead><tr><th>Link in the chain</th><th>What breaks</th><th>What the patient and unit do before the season</th></tr></thead><tbody>
<tr><td>Unit closes</td><td>Flood, power, water treatment, staff cannot travel</td><td>Generator and fuel plan; a written agreement with an alternate unit; staff call tree</td></tr>
<tr><td>Patient cannot reach a unit</td><td>Roads flooded, no transport, evacuation</td><td>Dialyze early when a strong storm is forecast, per the attending&rsquo;s decision; know the alternate unit</td></tr>
<tr><td>Records lost</td><td>Papers wet; unit offline</td><td>Patient carries a waterproof card: diagnosis, prescription, access, serologies with dates, medicines, PDD status, contacts</td></tr>
<tr><td>Food and fluid</td><td>Relief food salty and high in potassium</td><td>Teach the emergency diet in Filipino terms; keep low-potassium, low-salt food and measured water</td></tr>
<tr><td>Medicines run out</td><td>Pharmacies closed</td><td>At least a 3-day supply; a printed list</td></tr>
<tr><td>Payment</td><td>Treated at an unfamiliar unit</td><td>An active PhilHealth Dialysis Database (PDD) registration; the benefit card and an identification card in the kit</td></tr>
<tr><td>Peritoneal dialysis (PD) at home</td><td>Power out, supplies cut off, home flooded</td><td>Manual exchange plan for patients on automated cycles, as their PD team teaches; spare supplies; a clean place to exchange</td></tr>
</tbody></table></div>
<p>PhilHealth&rsquo;s benefit follows the registered patient: patients with chronic kidney disease stage 5 registered in the PDD can avail of up to 156 sessions a year.[[ntr36_7]] Make sure the registration is active before typhoon season, because a patient who dialyzes at an unfamiliar unit should not have to argue about payment while his potassium climbs. Confirm current benefit rules on the date of service.</p>
<div class="tc-keyp"><span class="tc-lab">At your stage</span><strong>Intern:</strong> ask every dialysis patient you admit when the last session was and whether any were missed. <strong>Resident:</strong> include a disaster plan in every discharge of a dialysis patient during typhoon season. <strong>Fellow:</strong> help your unit write and test its alternate-unit agreement and patient call list before June.</div>
{{key:In a storm, the most dangerous dialysis patient is the one nobody knows has missed a session. Plan the call list, the alternate unit and the patient&rsquo;s kit before the season, not during it.}}
"""),
  ('capstone-case', 'The capstone case', 'The capstone case: potassium, fluid and acid in the right order', """
<p>Mr. Caballero has three problems, and they are ranked by how fast they kill. Potassium threatens the heart in minutes; his ECG already shows it. Fluid in the lungs threatens oxygenation in minutes to hours. Acidosis worsens both and will not correct without dialysis. All three have one definitive treatment, dialysis, and the first hour is about keeping him alive until he gets it.</p>
<p><strong>Potassium.</strong> The UK Kidney Association classifies potassium of 6.5 mmol/L or higher as severe hyperkalemia.[[ntr36_5]] The Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference on potassium reviewed acute management in kidney disease; its conclusions are conference statements, not graded recommendations.[[ntr36_6]] The physiology gives the order. First, protect the heart: intravenous calcium raises the threshold potential and stabilizes the membrane within minutes, without lowering potassium. Second, shift potassium into cells: insulin with glucose and inhaled beta-agonists drive it in through the sodium-potassium pump, temporarily. Third, remove it: in a patient on dialysis, that means dialysis, because his kidneys cannot excrete it and other routes are slow. Doses, the glucose plan and repeat checks come from the hospital protocol and the attending. Module 7 covers the detail.</p>
{{flow:Stabilize, shift, remove: the first hour for a dialysis patient who missed sessions|Recognize::Peaked T waves, absent P waves, wide QRS, a slow or irregular pulse. Put him on a cardiac monitor and get help.|Protect the heart::Intravenous calcium per protocol when the ECG shows hyperkalemic changes; repeat the ECG.|Shift::Insulin with glucose and an inhaled beta-agonist per protocol; check glucose often, because he is diabetic and may become hypoglycemic later.|Breathe::Sit him up, give oxygen, prepare for noninvasive support per protocol; diuretics are unlikely to work in a patient with little urine.|Remove::Call the nephrologist and the HD unit at once; dialysis is the definitive treatment for potassium, fluid and acid.|Watch for rebound::Potassium shifts back out of cells within hours; recheck after treatment and after dialysis.}}
<p><strong>Fluid.</strong> He gained fluid over two missed sessions, and his lungs show it. Ultrafiltration on dialysis is the treatment. Until then, position, oxygen and blood pressure control per protocol support him; giving intravenous fluid with his potassium medicines must be kept to the minimum the protocol requires.</p>
<p><strong>When dialysis is delayed.</strong> The generator can fail; two machines may be busy; the unit may lack water. Then the bridge measures are repeated per protocol, potassium and ECG are watched closely, and the attending decides early whether to transfer to a center that can dialyze. A potassium binder by mouth acts too slowly to be the main treatment in this setting. The decision to transfer a patient this sick, through flooded roads, is the attending&rsquo;s, with the family.</p>
<div class="table-wrap"><table><thead><tr><th>Danger</th><th>Mechanism</th><th>What you see</th><th>What buys time</th><th>What fixes it</th></tr></thead><tbody>
<tr><td>Hyperkalemia</td><td>Resting membrane potential rises; conduction slows</td><td>Peaked T, lost P, wide QRS, bradycardia, arrest</td><td>Calcium; insulin with glucose; beta-agonist</td><td>Dialysis</td></tr>
<tr><td>Pulmonary edema</td><td>Salt and water retained over two missed sessions</td><td>Orthopnea, crackles, low saturation, hypertension</td><td>Sitting up, oxygen, ventilatory support per protocol</td><td>Ultrafiltration</td></tr>
<tr><td>Metabolic acidosis</td><td>Acid not removed; worsens potassium shift</td><td>Low bicarbonate, fast breathing</td><td>Treat the cause; protocol-directed measures</td><td>Dialysis</td></tr>
<tr><td>Hidden extras</td><td>Infection from floodwater, injury, missed medicines, hyperglycemia</td><td>Fever, wounds, high glucose</td><td>Look for them on arrival</td><td>Specific treatment</td></tr>
</tbody></table></div>
{{call:Stop and call the attending nephrologist now, per unit protocol, but always ask the attending nephrologist for guidance, when:<ul><li>potassium is 6.5 mmol/L or higher, or the ECG shows hyperkalemic changes at any potassium;</li><li>oxygen saturation is falling despite oxygen and positioning;</li><li>dialysis cannot start soon because of machines, water, power or staff;</li><li>the potassium rebounds after the first treatment or after dialysis;</li><li>a transfer through disaster conditions is being considered.</li></ul>}}
{{fig:ntr36_b}}
<div class="tc-keyp"><span class="tc-lab">In children</span>Children on dialysis have smaller fluid and potassium reserves, so a missed session or a typhoon week can cause dangerous hyperkalemia and fluid overload faster, and treatment is planned by weight. Many children in the Philippines are on home peritoneal dialysis, where floods and power cuts interrupt automated cycling and supplies, and a manual exchange plan matters. Electrolyte emergencies in children are covered in <a href="attending-pediatric-nephrologist-04-electrolyte-emergencies.html">Attending Pediatric Nephrologist, Module 4</a>.</div>
{{key:Rank the dangers by how fast they kill: protect the heart, shift the potassium, support breathing, and get dialysis. Everything else waits.}}
"""),
  ('portfolio', 'Your portfolio', 'Handoffs, documentation and an entrustment portfolio', """
<p>A capstone is not only a case well managed; it is evidence that you can be trusted with it. The idea of entrustable professional activities, introduced by ten Cate, is that training should certify units of professional work, such as managing a patient with hyperkalemia or handing off an unstable patient, that a supervisor can entrust to a trainee once competence has been shown, rather than abstract lists of competencies.[[ntr36_9]] The level of entrustment rises in steps: observe, act with direct supervision, act with supervision available, act independently within the institution&rsquo;s rules.</p>
<p>Handoff is the activity that ties every stage together. In the multicenter study of a structured resident handoff program, medical errors fell from 24.5 to 18.8 per 100 admissions and preventable adverse events from 4.7 to 3.3 per 100 admissions after implementation, without longer handoffs.[[ntr36_8]] It was a before-and-after design, so the improvement is associated with the program rather than proven to be caused by it. A common structure is I-PASS: illness severity, patient summary, action list, situation awareness and contingency planning, and synthesis by the receiver.</p>
<div class="table-wrap"><table><thead><tr><th>I-PASS element</th><th>Mr. Caballero at 7 a.m.</th></tr></thead><tbody>
<tr><td>Illness severity</td><td>Unstable: watch closely</td></tr>
<tr><td>Patient summary</td><td>54-year-old on HD three times a week, missed two sessions after the typhoon; potassium 7.4 with ECG changes, pulmonary edema, acidosis</td></tr>
<tr><td>Action list</td><td>Calcium and shift measures given per protocol at stated times; HD booked on machine 2 at 7:30; recheck potassium and glucose after; restart medicines</td></tr>
<tr><td>Situation awareness and contingency</td><td>If the ECG worsens, repeat calcium per protocol and call the fellow; if the generator fails, call the attending about transfer</td></tr>
<tr><td>Synthesis by receiver</td><td>The receiver repeats the plan and the triggers</td></tr>
</tbody></table></div>
<p><strong>What goes in your portfolio from this module.</strong> A written integrated case with your own reasoning; an observed handoff assessed by a supervisor; a discharge plan that includes a disaster plan; for fellows, a unit-level improvement (for example, the alternate-unit agreement) with a measure; and one teaching session, with feedback. The Academy&rsquo;s Personal Study Record and preceptor sign-off hold the record; your training program decides what counts.</p>
<div class="tc-keyp"><span class="tc-lab">At your stage</span><strong>Intern:</strong> present with the structure above and ask your resident to rate one handoff. <strong>Resident:</strong> collect observed assessments for the acute activities in this track. <strong>Fellow:</strong> assess residents and interns against the same activities, and record your own entrustment for dialysis, transplant and critical care work.</div>
{{key:Entrustment is earned one observed activity at a time. Hand off with a structure, and ask someone to watch you do it.}}
"""),
  ('next-step', 'The next step', 'From this admission to the next stage of training', """
<p>The case does not end when the potassium is normal. Mr. Caballero will go home to the same province, the same unit and the next typhoon season. The fellow&rsquo;s longitudinal plan covers his kidneys, his heart, his risk and his life. For people with chronic kidney disease who are not yet on dialysis, the KDIGO 2024 chronic kidney disease (CKD) guideline recommends estimating the absolute risk of kidney failure with an externally validated risk equation, which shapes the timing of modality and access planning (Module 11).[[ntr36_10]] For Mr. Caballero, already on HD, the plan is different: adequacy, fluid targets, potassium education in the language and foods of his home, medicines he can afford, vaccination, his fistula, transplant referral if he is a candidate (Module 29), and a disaster plan written down with his family.</p>
<div class="table-wrap"><table><thead><tr><th>Part of the plan</th><th>What the fellow defends</th><th>Linked module</th></tr></thead><tbody>
<tr><td>Why he missed dialysis</td><td>The unit closed; he had no alternate unit and did not know the unit&rsquo;s emergency plan</td><td>This module</td></tr>
<tr><td>Potassium and diet</td><td>Teach which relief foods are dangerous; a low-potassium emergency list</td><td>Modules 7 and 15</td></tr>
<tr><td>Fluid and blood pressure</td><td>Review target weight after the admission; restart medicines</td><td>Modules 5, 12 and 23</td></tr>
<tr><td>Medicines</td><td>A 3-day emergency supply and a printed list</td><td>Module 16</td></tr>
<tr><td>Benefit continuity</td><td>PDD registration active; sessions counted</td><td>Module 34</td></tr>
<tr><td>Long-term options</td><td>Transplant evaluation if appropriate; PD if home conditions suit</td><td>Modules 27 and 29</td></tr>
<tr><td>Goals of care</td><td>What matters to him and his family if the next storm is worse</td><td>Module 32</td></tr>
</tbody></table></div>
<p><strong>Your own next step.</strong> Each stage in the Philippine ladder carries different authority. The intern moves toward the licensure examination; the resident toward specialty boards and, for some, fellowship; the fellow toward the Philippine Society of Nephrology (PSN) board and independent practice. Module 1 and Module 33 explain what each stage allows, including the rules for working as a dialysis physician on duty. What carries across every stage is the same set of habits this track has taught: look at the patient and the urine yourself, rank dangers by speed, say the absolute numbers, write the truth, hand off with a structure, and call the attending when the situation exceeds your authority or your experience.</p>
<p>Look after yourself as well. Disaster weeks are long, and trainees often work through their own family&rsquo;s losses. Fatigue causes errors, and asking for relief is part of patient safety, not a failure.</p>
<div class="tc-keyp"><span class="tc-lab">At your stage</span><strong>Intern:</strong> write down three habits from this track you will keep as a resident. <strong>Resident:</strong> choose the activities you want entrusted next and ask to be observed. <strong>Fellow:</strong> teach this capstone case to the next group of interns.</div>
{{key:A good admission ends with a plan for the next storm. A good training year ends with habits you will keep without being asked.}}
"""),
 ],
 'debrief': [
  '<p><strong>The intern&rsquo;s presentation.</strong> Ana starts with severity, not history: &ldquo;Unstable. 54-year-old on HD three times a week, missed Monday and Wednesday because of the typhoon, now with potassium 7.4, ECG with peaked T waves, absent P waves and a wide QRS, pulmonary edema with saturation 87%, and bicarbonate 13.&rdquo; She names the dangers in order of speed: the heart, the lungs, the acid. She calls the resident at once, asks for a monitor and an ECG repeat, and hands off with I-PASS, including what has been given and what should trigger a call. To rehearse the response with your nurses, technicians and head nurse, run the Academy&rsquo;s <a href="/academy/same-event-every-role.html">Same event, every role</a> drill.</p>',
  '<p><strong>The resident&rsquo;s admission.</strong> Miguel follows the sequence: monitor, calcium per protocol for the ECG changes, shift measures with glucose checks, upright position and oxygen, and an immediate call to the fellow and the HD unit for emergency dialysis with ultrafiltration. He looks for floodwater infection, wounds and missed medicines. He rechecks potassium and glucose after treatment and after dialysis, watching for rebound. If the generator or the machines fail, he repeats the bridge measures per protocol and asks the attending early about transfer. Before discharge he restarts medicines, reviews the target weight, confirms the next session at a unit that is open, and writes a disaster plan with the family.</p>',
  '<p><strong>The fellow&rsquo;s longitudinal plan.</strong> Grace defends a plan that addresses why he missed dialysis: an alternate unit named in writing, early dialysis when a strong storm is forecast as the attending decides, a waterproof card with his prescription, access, serologies and PDD status, a 3-day medicine supply, and an emergency diet taught with Filipino relief foods in mind. For his unit, she proposes a tested call list and alternate-unit agreement before the next season, measured by the share of patients reached within 24 hours of a storm. She also raises transplant referral and goals of care, and teaches the case to the interns, using the observed handoff for their portfolios.</p>',
 ],
 'skills': {'title': 'Integrated capstone, disaster readiness and transition',
  'intro': 'Complete with a preceptor, in simulation or on a real admission. Sign-off is local.',
  'items': [('Presents an integrated case of a dialysis patient who missed sessions, ranking dangers by speed', False),
            ('Leads the stabilize-shift-remove sequence in simulation, naming the protocol source for each step', False),
            ('Gives an observed I-PASS handoff of an unstable patient', False),
            ('Writes a discharge plan that includes a disaster plan and an emergency diet adapted to Filipino foods', False),
            ('Reviews or drafts a unit alternate-unit agreement and patient call list', False),
            ('Teaches the capstone case to junior learners and records feedback', False)],
  'placement': 'Emergency room, ward, dialysis unit or simulation'},
 'quiz': [
  ('An intern sees a man on hemodialysis who missed two sessions during a typhoon. His ECG shows peaked T waves and a wide QRS. What should the intern say first when calling the resident?',
   ['His full past medical history',
    'That he is unstable, with potassium and ECG changes, fluid overload and missed sessions, and needs help now',
    'That his family wants to know when he can go home',
    'That his fistula has a good thrill'],
   1,
   'Structured handoffs start with illness severity and the immediate dangers. A complete history (the tempting distractor) delays the action that the ECG demands.'),
  ('A resident manages a patient with potassium 7.4 mmol/L and hyperkalemic ECG changes who is on maintenance hemodialysis. What is the correct order of priorities?',
   ['Oral potassium binder first, then dialysis next week',
    'Protect the heart with intravenous calcium per protocol, shift potassium into cells per protocol, then remove it with dialysis',
    'Dialysis only; no other measures are needed',
    'Diuretics to remove potassium in the urine'],
   1,
   'Calcium stabilizes the membrane, insulin with glucose and beta-agonists shift potassium temporarily, and dialysis removes it. Diuretics (a tempting distractor) are unlikely to work in a patient with little urine, and binders act too slowly in this setting.'),
  ('A fellow is asked to defend a disaster plan for her dialysis unit. Which finding from Hurricane Katrina most directly supports teaching patients the unit&rsquo;s emergency plan?',
   ['Facilities in other states stayed open',
    'Patients unaware of their facility&rsquo;s emergency plan were more likely to miss three or more sessions, and missing three or more was associated with hospitalization',
    'Mortality was unchanged',
    'All patients evacuated before landfall'],
   1,
   'In the Katrina survey, unawareness of the facility plan was among the factors linked to missing three or more sessions (adjusted odds ratio for hospitalization 2.16). It is observational, but it points to a modifiable risk.'),
  ('At a provincial hospital the generator fails one hour after a patient with severe hyperkalemia received calcium and shift measures, and dialysis cannot start. What is the most appropriate step?',
   ['Wait for power to return without further action',
    'Discharge the patient on an oral binder',
    'Monitor closely, repeat bridge measures per protocol as potassium and ECG require, and call the attending nephrologist early about transfer to a center that can dialyze',
    'Give large volumes of intravenous fluid'],
   2,
   'Shift measures are temporary and potassium rebounds, so a patient without dialysis needs close monitoring, repeated bridge measures and an early transfer decision by the attending. An oral binder (a tempting distractor) acts too slowly to replace dialysis.'),
  ('Before typhoon season, which item belongs in a patient&rsquo;s emergency kit, according to CDC advice for dialysis patients?',
   ['A one-month supply of bananas and coconut water',
    'Contact numbers for the regular and an alternate unit, a list of medicines with at least a 3-day supply, and a 3-day emergency diet plan',
    'Only the PhilHealth card',
    'A home dialysis machine'],
   1,
   'The CDC advises a kit with contacts, a medicine list and at least a 3-day supply, and an emergency diet if dialysis is missed. Bananas and coconut water (the tempting distractor) are high in potassium.'),
 ],
 'terms': [('CDC', 'Centers for Disease Control and Prevention'),
           ('CKD', 'Chronic kidney disease'),
           ('ECG', 'Electrocardiogram'),
           ('HD', 'Hemodialysis'),
           ('I-PASS', 'Illness severity, patient summary, action list, situation awareness and contingency planning, synthesis by receiver'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('PD', 'Peritoneal dialysis'),
           ('PDD', 'PhilHealth Dialysis Database'),
           ('PhilHealth', 'Philippine Health Insurance Corporation'),
           ('PSN', 'Philippine Society of Nephrology'),
           ('QRS', 'The ventricular depolarization complex on the ECG')],
 'readings': [('attending-nephrologist-22-disasters-continuity.html', 'Attending Nephrologist, Module 22: Disasters and Continuity'),
              ('typhoon-disaster-preparedness-dialysis.html', 'Typhoon and Disaster Preparedness for Dialysis'),
              ('attending-nephrologist-24-capstone.html', 'Attending Nephrologist, Module 24: Capstone')],
 'calcs': ['calc-dialysis-continuity-planner.html', 'calc-potassium-load.html', 'calc-qtc.html', 'calc-idwg-fluid.html', 'calc-fluid-overload.html'],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
