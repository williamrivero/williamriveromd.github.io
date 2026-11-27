# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 25: Emergencies during hemodialysis.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. Study numbers checked
against PubMed abstracts (Flythe 2015, Kuipers 2019, Burton 2009, MyTEMP 2022, Duffy 2000, Pun 2019, Lehrich 2007); the EBPG
intradialytic hypotension definition checked against studies quoting it. Goes deeper on reasoning than the Physician on Duty track,
which it links. No drug doses. Fictional case."""

MODULE = {
 'image_alt': 'A young physician on duty kneels beside a reclined dialysis chair, checking the pulse of an older woman while a nurse watches the machine and holds an electrocardiogram lead.',
 'objectives': [
  '<strong>Intern:</strong> Recognize a hemodialysis emergency at the chair (a falling pressure, chest pain, sudden breathlessness, air or dark blood in the lines, a reaction in the first minutes, bleeding, collapse) and call for help at once with the facts the attending will need.',
  '<strong>Resident:</strong> Run the first actions for intradialytic hypotension, cramps, chest pain, air embolism, hemolysis, dialyzer reaction, bleeding and cardiac arrest in the order your unit&rsquo;s protocol sets, and know when blood must not be returned.',
  '<strong>Fellow:</strong> Find the cause after the event, change the prescription or the system that allowed it, and teach the unit from it through a structured review.',
 ],
 'big': """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the dialysis chair at hour three</span>The <strong>intern</strong> rotating through a hospital dialysis unit is often the nearest doctor when a nurse calls: notice, go to the chair, and call the responsible physician with the pressure, the pulse, the time into the session and what has been done. The <strong>resident</strong>, on the ward or moonlighting as a physician on duty (POD) in a freestanding unit, runs the first actions and must know before the shift whether they are eligible to cover it. The Department of Health (DOH) licensing rules and the Philippine Society of Nephrology (PSN) 2024 hemodialysis guidelines describe the POD role, including the POD course and advanced cardiac life support.[[ntr25_14]][[ntr25_13]] The <strong>fellow</strong> reviews every serious event with the attending and changes something so it does not recur.</div>
{{plain:Picture a borrowed second circulation running beside the patient&rsquo;s own: half a liter or so of blood leaves through one needle, is pumped through plastic tubing and a filter, and comes back through another. For four hours, two circulations share one heart. Most of the time they cooperate. When something goes wrong, it goes wrong fast, because the circuit is connected straight to the great veins.}}
<p>The picture has a limit. A second circulation is not passive plumbing; it changes the patient while it runs. Water is pulled out of the blood faster than the tissues can refill it. Potassium falls quickly, which can disturb the rhythm of a damaged heart. Blood touches foreign surfaces that can activate complement and the contact system. And the circuit can deliver air, broken red cells or contaminated fluid straight into the patient. So every emergency at the chair has two possible sources: the patient, or the circuit. The first question at every alarm is which one.</p>
{{cards:Key numbers|EBPG 2007 definition of intradialytic hypotension::A fall in systolic pressure of 20 mm Hg or more, or in mean arterial pressure of 10 mm Hg or more, with symptoms and a need for intervention (opinion based)|How often (meta-analysis, 2019)::10.1% of sessions by the EBPG definition; 11.6% by a nadir systolic below 90 mm Hg|Nadir below 90 mm Hg (11,801 patients, observational)::The definition most strongly associated with death|Cardiac arrest in outpatient units (398 events)::66% nonshockable first rhythm; staff started CPR in 81.4%|Staff-initiated CPR::Associated with about threefold odds of discharge alive (observational)}}
<p>Most emergencies during dialysis are a falling pressure from fluid removal, and they recover within minutes. A few are heart attacks, arrhythmias, air, hemolysis, reactions or bleeding, and these kill within minutes to hours if the first move is wrong. Your work is to treat the common one promptly, recognize the dangerous one early, decide correctly whether the blood goes back, and make sure the next session is safer.</p>
""",
 'case': {'title': 'Saturday night, hour three',
          'html': """
<p>Saturday, 10:40 p.m., a freestanding hemodialysis unit in San Fernando, Pampanga. Dr. Carlo Mendoza, a third-year internal medicine resident, is moonlighting as the only physician on duty for the night shift. He confirmed his POD course and advanced cardiac life support certificate with the unit last month.</p>
<p>Mrs. Lourdes Navarro, 68, has diabetes and had a coronary stent placed three years ago. She dialyzes on Wednesdays and Saturdays through a left arm fistula. She arrived 4.1 kg above her dry weight of 55 kg, and the session is set for four hours. Her blood pressure was 152/86 mm Hg at the start. At hour three, the nurse, Ms. Weng Dizon, calls him: Mrs. Navarro says her chest feels heavy and she is sweating. Her pressure is 78/44 mm Hg and her pulse 118 per minute and irregular. Ms. Dizon has already reclined the chair and stopped fluid removal under the unit protocol.</p>
<p>The attending nephrologist is at home in Angeles City. The nearest hospital with a cardiac catheterization laboratory is 25 minutes away.</p>
""",
          'questions': ['What do you do in the first two minutes, and in what order?',
                        'Is this a simple drop from fluid removal or something more dangerous, and what decides whether the blood goes back?',
                        'After she is safe, what should change in her prescription and in the unit?']},
 'sections': [
  ('hypotension', 'Hypotension and cramps', 'Intradialytic hypotension: the common emergency', """
<p>The machine removes water only from the blood. The tissues must refill the vessels, the vessels must tighten, and the heart must keep up. Pressure falls when removal outruns refilling and these active defenses fail. Diabetes and autonomic neuropathy blunt the vessels and the heart rate; a thick, stiff ventricle needs full filling; blood pressure tablets taken that morning, a meal during dialysis and a rising body temperature all relax the vessels. The Physician on Duty track explains these defenses in detail; here, carry the causal chain: large weight gain, then fast removal, then refilling outrun, then a weak defense, then the drop.</p>
<p>No single definition is accepted. The European Best Practice Guideline (EBPG) on hemodynamic instability defined intradialytic hypotension as a fall in systolic pressure of 20 mm Hg or more, or in mean arterial pressure of 10 mm Hg or more, with symptoms and a need for intervention, and graded that definition as opinion.[[ntr25_1]] In 1,409 patients from the Hemodialysis (HEMO) Study and 10,392 from a large dialysis organization, a nadir systolic pressure below 90 mm Hg was the definition most strongly associated with death; in patients starting at 160 mm Hg or more, a nadir below 100 mm Hg was. Definitions built on symptoms or interventions were not associated with death.[[ntr25_2]] A meta-analysis found that 10.1% of sessions met the EBPG definition and 11.6% the nadir-below-90 definition, lower than many reviews claim; diabetes, higher weight gain between sessions, female sex and lower body weight were the main risk factors.[[ntr25_3]] All of this is observational: it tells you who is at risk and which numbers track death, not that preventing a low nadir saves lives.</p>
{{flow:Falling pressure at the chair|Go and look::Check that the patient responds, breathes and has a pulse. Ask for help early.|Lay back and stop removal::Recline flat with legs raised as far as breathing allows. Stop ultrafiltration. Keep the blood pump running unless you suspect air, hemolysis, a reaction or blood loss from the circuit.|Recheck and count::Repeat the pressure every few minutes. Count the pulse yourself and note the rhythm.|Look for a cause::Chest pain, breathlessness, fever, bleeding at the needles or lines, the time into the session, the fluid removed, the morning medicines, the last meal, and blood sugar in diabetes, per protocol.|Fluid if no recovery::Use the fluid and amount in the unit protocol, in measured portions, reassessing after each.|Call::The attending nephrologist, with what you found and did. Agree on the rest of the session.}}
{{fig:ntr25_a}}
<p>Do not restart fluid removal at the old rate once the pressure recovers; the remaining goal, time and dry weight belong to the prescription. Cramps often come with a volume-related drop: the same first steps help, along with stretching the muscle.</p>
<h3>Why it matters beyond the moment</h3>
<p>In 30 patients who already had dialysis-induced myocardial ischemia, serial echocardiography over a year showed that resting left ventricular ejection fraction fell from about 61.5% to 52.9%, with some segments developing fixed dysfunction, and dialysis-induced hypotension became more frequent.[[ntr25_5]] It was a small observational study; it suggests that repeated drops injure the heart, not that preventing them prolongs life.</p>
<h3>Prevention, and a trial that tempers enthusiasm</h3>
<p>The Kidney Disease: Improving Global Outcomes (KDIGO) controversies conference on blood pressure and volume in dialysis concluded that managing pressure and volume means weighing comorbidity, the hemodynamic pattern of each session, clinical judgment and patient preference within local resources.[[ntr25_4]] Cooling the dialysate was one popular strategy. The MyTEMP trial cluster-randomized 84 Ontario centers treating 15,413 patients to personalized cooler dialysate or a standard 36.5 &deg;C. Over four years, cardiovascular death or admission occurred in 21.4% vs 22.4% (adjusted hazard ratio 1.00), and the mean intradialytic fall in systolic pressure was 26.6 vs 27.1 mm Hg.[[ntr25_6]] Cooling as a center-wide policy did not help. It did not test cooling for the individual patient who drops every session, and the temperature remains a prescription choice for the attending.</p>
{{formula:<strong>Arithmetic illustration, not a target.</strong> Ultrafiltration rate (UFR) = fluid to remove (mL) &divide; session time (h) &divide; weight (kg).<br>4,100 mL over 4 hours in a 55-kg patient = about 18.6 mL/kg/h. Over 5 hours = about 14.9 mL/kg/h.}}
{{key:At every drop, ask which defense failed (refilling, vessel tone or the heart) and report the weight gain, the ultrafiltration rate, the time of onset, the last meal and the morning medicines.}}
"""),
  ('cardiac', 'Chest pain and rhythm', 'Chest pain, breathlessness and rhythm problems in the chair', """
<p>The heart in the dialysis chair works under three stresses at once. Coronary flow depends on diastolic pressure, so a falling pressure starves a heart with narrowed arteries. Anemia lowers oxygen delivery. Potassium and other electrolytes shift within hours, which can provoke arrhythmias in a scarred or hypertrophied ventricle. Add fluid overload before the session, and the patient may arrive already in pulmonary edema.</p>
<div class="table-wrap"><table>
<thead><tr><th>Problem</th><th>Mechanism</th><th>Clues at the chair</th><th>First move while you call</th></tr></thead>
<tbody>
<tr><td>Myocardial ischemia or infarction</td><td>Low diastolic pressure, anemia and coronary disease cut oxygen supply</td><td>Chest heaviness, sweating, breathlessness; may be painless in diabetes</td><td>Stop fluid removal, oxygen per protocol, 12-lead electrocardiogram (ECG), unit chest pain protocol</td></tr>
<tr><td>Arrhythmia</td><td>Rapid electrolyte shifts on a diseased myocardium</td><td>Fast, slow or irregular pulse, palpitations, fainting</td><td>ECG and monitor; prepare the defibrillator; check potassium if available</td></tr>
<tr><td>Pulmonary edema</td><td>Overload before or after the session; ischemia</td><td>Breathlessness, crackles, cannot lie flat</td><td>Sit up; continue or increase fluid removal only on the attending&rsquo;s advice</td></tr>
<tr><td>Pericarditis or tamponade</td><td>Uremic or dialysis-associated inflammation</td><td>Rub, repeated early drops with little fluid removed, distended neck veins</td><td>Stop fluid removal; urgent transfer for echocardiography</td></tr>
</tbody></table></div>
<p>A new drop in a stable patient, or a drop with chest pain, breathlessness, an irregular pulse or altered consciousness, is not a simple drop. Do not wait to see whether lying back fixes it. Get the ECG while the nurse continues the hypotension steps, and call. Whether to end the session and return the blood is decided with the attending; for a cause in the patient with a sound circuit, returning the blood gives back volume and is usually right.</p>
{{call:Stop and call the attending nephrologist immediately, and call for help in the unit, per unit protocol, but always ask the attending nephrologist for guidance:<ul><li>A low pressure with chest pain, breathlessness, altered consciousness, fever or bleeding</li><li>A pulse that is very fast, very slow or newly irregular</li><li>No recovery after the first steps, a second drop, or need for more than one portion of fluid</li><li>Air or foam in the venous line, translucent cherry-red blood, or more than one patient unwell</li><li>Any collapse: start the code first, then call</li></ul>}}
{{key:A drop with chest pain or an irregular pulse is a cardiac event until the ECG says otherwise; get the tracing before more fluid comes off.}}
"""),
  ('circuit', 'Circuit emergencies', 'When the circuit is the cause: air, clotting, blood leak, hemolysis, bleeding', """
<p>The circuit has guards: pressure monitors on both lines, an air detector just before the blood returns, a blood-leak detector in the dialysate path. Most circuit emergencies happen when a guard is bypassed, silenced or fooled, or when something fails upstream of it. The reviews of dialysis emergencies note that most are attributable to human error, and that root cause analysis after the event is how units prevent recurrence.[[ntr25_7]][[ntr25_8]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>What happened</th><th>Clues</th><th>First move</th><th>Return the blood?</th></tr></thead>
<tbody>
<tr><td>Air embolism</td><td>Air enters through a loose connection, an empty infusion bag, a catheter left open, or past a disabled detector</td><td>Air or foam in the venous line, air alarm, sudden cough, chest tightness, breathlessness, collapse</td><td>Clamp the venous line and stop the blood pump; position the patient per protocol, commonly lying on the left side, head down; high-flow oxygen; call</td><td>No</td></tr>
<tr><td>Hemolysis</td><td>Kinked or narrowed blood lines, overheated or wrongly mixed dialysate, contaminated water</td><td>Translucent, port-wine or cherry-red venous blood; chest, back or abdominal pain; more than one patient affected</td><td>Stop the blood pump, clamp the lines; check every patient on the same water or lot; potassium and hemoglobin</td><td>No</td></tr>
<tr><td>Circuit clotting</td><td>Low flow, no anticoagulation, high hematocrit, access problems</td><td>Rising pressures, dark streaks in the dialyzer, clots in the drip chamber</td><td>Per protocol, often a saline flush; replace the circuit if clotted</td><td>Not from a clotted circuit</td></tr>
<tr><td>Blood leak</td><td>A dialyzer fiber ruptures</td><td>Blood-leak alarm, pink dialysate</td><td>Stop and replace the dialyzer per protocol</td><td>Per unit protocol and the attending</td></tr>
<tr><td>Needle dislodgement or line separation</td><td>A venous needle slips out or a connection opens; the pump keeps running</td><td>Blood under the blanket, a pool on the floor, falling pressure; the venous pressure alarm may not trigger</td><td>Stop the blood pump, clamp, apply pressure to the site; assess blood loss</td><td>Only once the circuit is intact and sterile, per protocol</td></tr>
</tbody></table></div>
<p>The guidance in this table follows standard reviews of hemodialysis emergencies.[[ntr25_7]][[ntr25_8]] Keep needle sites and lines visible: a blanket over the arm is how a dislodged venous needle bleeds unnoticed, because the venous pressure alarm may not fall enough to trigger.</p>
{{fig:ntr25_b}}
<h3>When hemolysis hits more than one chair</h3>
<p>In May 1998, patients in units in three American states developed hemolysis after dialysis. Thirty case-patients were identified; 60% had abdominal pain, 36% were admitted to intensive care, and two died. The only factor common to all three outbreaks was one lot of disposable blood tubing, in which a narrowed aperture raised the pressure on red cells as they were pumped toward the dialyzer; the manufacturer recalled it.[[ntr25_9]] The lesson for a POD: when two patients become unwell in the same shift, suspect the shared supply (the water, the dialysate or a lot of disposables), keep the circuits and packaging, and tell the charge nurse, the technician and the attending at once. Module 26 covers the water side.</p>
{{key:Air, hemolysis, a severe reaction or a clotted circuit: clamp, stop the pump, and do not return the blood. A cause in the patient with a sound circuit: the blood usually goes back.}}
"""),
  ('reactions', 'Reactions', 'Reactions to the dialyzer, medicines and fluid', """
<p>Blood meeting a membrane can activate complement and the contact system. Contact activation releases bradykinin, which an angiotensin-converting enzyme (ACE) inhibitor prevents from being broken down, so some membranes and ACE inhibitors together can produce sudden flushing, swelling and hypotension. A review of hypersensitivity in hemodialysis found that medicines (iron, erythropoiesis-stimulating agents and heparin) are the most common identifiable cause, that most reactions are pseudoallergic rather than immunoglobulin E mediated, and that once a cause is established, an alternative drug preparation or membrane usually prevents recurrence.[[ntr25_10]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Pattern</th><th>Timing</th><th>Features</th><th>First move</th></tr></thead>
<tbody>
<tr><td>Severe (anaphylactic or anaphylactoid) reaction</td><td>Usually within the first minutes of the session or of a drug</td><td>Flushing, itching, urticaria, wheeze, facial or throat swelling, hypotension, back or chest pain</td><td>Stop the blood pump, clamp, do not return the blood; anaphylaxis protocol; call</td></tr>
<tr><td>Milder reaction</td><td>Often later in the session</td><td>Chest or back pain, nausea, without collapse</td><td>Slow or pause per protocol; assess; often the session continues with the attending&rsquo;s advice</td></tr>
<tr><td>Fever and chills</td><td>During the session</td><td>Rigors, high temperature; with a catheter, suspect bloodstream infection; in several patients, suspect the water or dialysate</td><td>Cultures per protocol; Module 26 for clusters</td></tr>
</tbody></table></div>
<p>After any reaction, record the dialyzer type and lot, the reprocessing status if dialyzers are reused, the medicines given in the first hour, the patient&rsquo;s ACE inhibitor use, and the time of onset. Those details let the attending choose a different membrane or preparation for the next session.[[ntr25_10]]</p>
{{key:A reaction in the first minutes of a session means stop, clamp, do not return the blood, treat as anaphylaxis, and record the dialyzer, the lot and every drug given.}}
"""),
  ('arrest', 'Code in the chair', 'Cardiac arrest in the dialysis chair', """
<p>Sudden cardiac arrest is a leading cause of death on hemodialysis, and many arrests happen in the unit. A registry study of 398 cardiac arrests in outpatient dialysis clinics in the southeastern United States found that 66% had a nonshockable first rhythm. Dialysis staff started cardiopulmonary resuscitation (CPR) before emergency services arrived in 81.4% of events and applied a defibrillator in 52.3%. Staff-initiated CPR was associated with about threefold higher odds of discharge alive with good neurologic status.[[ntr25_11]] An earlier cohort of 43,200 patients with 729 in-unit arrests found that the presence of an automated external defibrillator (AED) alone was not associated with survival (30-day survival 19% vs 15% with and without one); having the device is not the same as using it well.[[ntr25_12]] Both studies were observational and from the United States, but the message travels: what the staff do in the first minutes matters most.</p>
{{flow:Code in the chair|Call the code::Shout for help, note the time, bring the crash cart and defibrillator.|Start CPR::Lower the chair flat. Start compressions. Follow advanced cardiac life support.|Deal with the circuit::Stop ultrafiltration. Return the blood if the circuit is sound and your protocol says so, or clamp and disconnect; do not let the circuit delay compressions.|Think of the dialysis causes::Hyperkalemia or hypokalemia, air embolism, hemorrhage from the access, hypoxia, a reaction, tamponade.|Call::Emergency services for transfer and the attending nephrologist, as soon as hands allow.|After::Document times, rhythms, drugs and shocks; tell the family with the attending; hold a debriefing with the team.}}
<p><strong>Philippine reality.</strong> Many freestanding units have one POD, two or three nurses and a technician on a night shift, and the nearest hospital may be far. Confirm before your first shift that the defibrillator works and the crash cart is complete, that you know the unit&rsquo;s emergency transfer arrangements, and that your own advanced life support training is current. The PSN 2024 guidelines describe the POD course and life support requirement, and DOH licensing rules govern who may cover a unit.[[ntr25_13]][[ntr25_14]] If you are not eligible, do not take the shift.</p>
<h3>After the event: the fellow&rsquo;s work</h3>
<p>One emergency needs treatment; the pattern behind it needs a change. With the attending, the fellow asks what happened, why, and what the unit will change: the dry weight and ultrafiltration rate for a patient who drops every session, a membrane or drug for a patient who reacted, a check on the defibrillator, a lot recall, a rule that needle sites stay uncovered. Reviews of dialysis emergencies recommend root cause analysis for exactly this purpose.[[ntr25_7]] The site&rsquo;s session review calculator helps structure the facts.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>A child&rsquo;s blood volume is small, so the circuit holds a larger share of it, and a fall in pressure or a loss of blood from the circuit becomes dangerous sooner. Pediatric units plan circuit size, priming and ultrafiltration per kilogram, and young children may not report symptoms. See <a href="attending-pediatric-nephrologist-25-hd-emergencies-water.html">Attending Pediatric Nephrologist, Module 25</a>.</div>
{{key:In a code in the chair, compressions come first and the circuit second. Afterward, every serious event gets a review that changes a prescription or a system.}}
"""),
 ],
 'debrief': [
  """<p><strong>The first two minutes.</strong> Ms. Dizon has already reclined the chair and stopped fluid removal. Dr. Mendoza goes to the chair, confirms Mrs. Navarro responds and is breathing, counts her pulse (fast and irregular), asks for oxygen per protocol and a 12-lead ECG now, and for the monitor and defibrillator to be brought to the chair. He uncovers her arm to check both needle sites and the lines, and looks at the color of the venous blood. He asks for a blood sugar check under the protocol. Because chest heaviness and an irregular pulse came with the drop, he does not wait for the pressure to recover before calling the attending.</p>""",
  """<p><strong>Simple or dangerous, and the blood.</strong> Some features fit a volume drop: hour three, a large weight gain, an ultrafiltration rate near 19 mL/kg/h. But chest heaviness with sweating, a known coronary stent, diabetes and a new irregular tachycardia point to ischemia or a dialysis-provoked arrhythmia, both made worse by the low pressure. The circuit looks normal: no air, no translucent blood, no alarm, no bleeding. So the cause is in the patient and the circuit is sound. With the attending, he ends the session, returns the blood to give back volume, continues the chest pain protocol, and arranges transfer to the hospital with a catheterization laboratory, with the ECG and session record.</p>""",
  """<p><strong>What changes.</strong> At the review on Monday, the fellow and the attending note her large weight gain over a four-day gap and a fast ultrafiltration rate in a patient with coronary disease. Options for the attending: dietitian review of salt and fluid, a longer or extra session to lower the rate, reassessment of her dry weight, review of her morning blood pressure medicines and meal timing, and cardiology follow-up. For the unit: confirm the defibrillator check log, and add &ldquo;12-lead ECG within minutes for any chest pain&rdquo; to the night-shift card.</p>""",
 ],
 'skills': {'title': 'Emergencies during hemodialysis',
            'intro': 'Practice on a simulated patient in a dialysis chair with your preceptor playing the nurse. Sign-off is local.',
            'items': [
             ('Runs the falling-pressure sequence in protocol order and states when the blood pump must stop', False),
             ('Separates a volume-related drop from a cardiac cause using timing, symptoms, pulse and response, and obtains an ECG', False),
             ('Demonstrates the first moves for air in the venous line and for suspected hemolysis, and states that the blood is not returned', False),
             ('Recognizes a severe dialyzer or drug reaction in the first minutes and records the dialyzer, lot and drugs given', False),
             ('Leads a simulated code in the chair: CPR first, then the circuit, then the dialysis-specific causes', False),
             ('Verifies own POD eligibility, the defibrillator, the crash cart and the transfer arrangements before a shift', False)],
            'placement': 'Hospital or freestanding hemodialysis unit, or simulation laboratory'},
 'quiz': [
  ('An intern on a dialysis rotation is called because a patient at hour two says her vision is dimming and she is yawning. Her pressure is 84/50 mm Hg. What should the intern do first?',
   ['Leave a note for the physician to review at the end of the session',
    'Go to the chair, confirm the nurse has laid the patient back and stopped fluid removal, recheck the pressure and pulse, and call the responsible physician',
    'Increase the blood pump speed',
    'Give a large fluid bolus immediately without assessing her'],
   1,
   'Yawning and dimming vision are early signs of a falling pressure. The first steps are quick and low risk, and the physician needs the pressure, pulse, time and actions. Fluid comes per protocol after the first steps fail, in measured portions.'),
  ('Ten minutes into a session, a man becomes flushed and itchy, then wheezes, and his pressure falls. What happens to the blood in the circuit?',
   ['Return it quickly to restore his volume',
    'Stop the blood pump, clamp the lines and do not return the blood; start the anaphylaxis protocol',
    'Continue dialysis and observe for 15 minutes',
    'Lower the blood flow and continue'],
   1,
   'A reaction in the first minutes with itching and wheeze suggests a severe dialyzer or drug reaction. The blood that has been in contact with the trigger is not returned. Returning it is right only for a cause in the patient with a sound circuit.'),
  ('A fellow reviews a patient with frequent intradialytic hypotension. What did the MyTEMP trial show about cooler dialysate?',
   ['Cooler dialysate halved cardiovascular deaths',
    'Personalized cooler dialysate as a center-wide policy did not reduce cardiovascular death or admission (21.4% vs 22.4%, hazard ratio 1.00)',
    'Cooler dialysate increased deaths',
    'Cooler dialysate eliminated intradialytic hypotension'],
   1,
   'MyTEMP tested a policy across 84 centers and found no benefit; the mean intradialytic fall in systolic pressure was also similar. It did not test cooling for an individual patient with frequent episodes, so the temperature stays a prescription decision.'),
  ('During a night shift, two patients on adjacent machines develop back pain, and the blood in one venous line looks translucent and cherry red. What is the best interpretation and action?',
   ['Two coincidental muscle strains; give analgesia',
    'Possible hemolysis from a shared cause such as the water, dialysate or a tubing lot: stop the pumps, clamp, do not return the blood, check other patients and call the attending and technician',
    'Dialyzer reactions; return the blood slowly',
    'Hypotension; give fluid and continue'],
   1,
   'Translucent cherry-red blood with pain suggests hemolysis, and two patients at once point to a shared supply. In the 1998 multistate outbreak, faulty tubing from one lot caused hemolysis in 30 patients, and two died.'),
  ('A patient collapses in the dialysis chair and has no pulse. What is the correct order of priorities?',
   ['Disconnect and return the blood fully before starting CPR',
    'Call the attending nephrologist first, then start CPR',
    'Call the code and start CPR at once; then stop ultrafiltration and handle the circuit per protocol; then consider dialysis-specific causes',
    'Wait for emergency services to arrive with a defibrillator'],
   2,
   'Compressions come first. In registry data, staff-initiated CPR was associated with about threefold higher odds of discharge alive; the circuit is managed without delaying compressions, and hyperkalemia, hypokalemia, air and hemorrhage are considered next.'),
 ],
 'terms': [
  ('ACE', 'Angiotensin-converting enzyme'),
  ('AED', 'Automated external defibrillator'),
  ('CPR', 'Cardiopulmonary resuscitation'),
  ('DOH', 'Department of Health (Philippines)'),
  ('EBPG', 'European Best Practice Guideline'),
  ('ECG', 'Electrocardiogram'),
  ('HEMO', 'Hemodialysis Study'),
  ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
  ('MyTEMP', 'Trial of personalized cooler dialysate in Ontario hemodialysis centers'),
  ('POD', 'Physician on duty'),
  ('PSN', 'Philippine Society of Nephrology'),
  ('Intradialytic hypotension', 'A fall in blood pressure during a dialysis session; published definitions differ'),
  ('Nadir', 'The lowest systolic pressure recorded during a session'),
 ],
 'readings': [('physician-on-duty-13-when-the-pressure-falls.html', 'Physician on Duty, Module 13: When the Pressure Falls'),
              ('physician-on-duty-15-heart-emergencies-in-the-chair.html', 'Physician on Duty, Module 15: Heart Emergencies in the Chair'),
              ('physician-on-duty-16-when-the-circuit-fails.html', 'Physician on Duty, Module 16: When the Circuit Fails'),
              ('hemodialysis-complications.html', 'Hemodialysis Complications')],
 'calcs': ['calc-hd-session-review.html', 'calc-ultrafiltration-rate.html', 'calc-shock-index.html'],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
