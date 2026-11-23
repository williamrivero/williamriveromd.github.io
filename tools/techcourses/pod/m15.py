# -*- coding: utf-8 -*-
"""Physician on Duty, Module 15: Heart Emergencies in the Chair: Chest Pain, Arrhythmia, and Cardiac Arrest.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty reading a 12-lead electrocardiogram beside a patient in a dialysis chair while a nurse stands at the machine.",
    "objectives": [
        "Sort chest pain in a dialysis patient by cause, including the causes that come from the dialysis circuit.",
        "Read a 12-lead electrocardiogram for rhythm, ischemia, and potassium effects, and interpret troponin with caution.",
        "Explain why arrhythmia clusters around dialysis and the long gap, and manage new atrial fibrillation in the chair.",
        "Decide with the attending nephrologist whether to stop dialysis and return the blood, and arrange transfer.",
        "Lead life support beside a dialysis machine, including the chair, the machine, the blood, and the access.",
        "Name the reversible causes special to dialysis, assign team roles, and lead a debrief.",
    ],
    "big": """
{{plain:Think of the heart as a pump in a house with unreliable wiring. In a dialysis patient the pipes that feed the pump are narrowed. The voltage, which is potassium, drifts up for days and then drops within hours. The tank the pump must empty fills across the gap and is drained in one session. Most heart emergencies in the chair come from the supply, the electricity, or the load.}}
<p>The picture is useful, and it has limits. The three problems feed each other: a fall in blood pressure starves heart muscle of oxygen, and starved muscle is electrically unstable. Some chest pain in the chair does not come from the heart at all. Air, damaged red cells, and a dialyzer reaction come from the circuit, and they change what you do with the blood.</p>
{{cards:Key terms for this module|Acute coronary syndrome::Sudden loss of blood flow to heart muscle. It includes unstable angina and heart attack.|Troponin::A heart muscle protein measured in blood. It rises when heart muscle is injured.|Atrial fibrillation (AF)::A fast, irregular rhythm in which the upper chambers quiver and do not contract.|Ventricular fibrillation (VF)::A chaotic rhythm of the lower chambers that produces no pulse.|Shockable rhythm::Ventricular fibrillation or pulseless ventricular tachycardia (VT). A defibrillator shock can stop it.|Cardiopulmonary resuscitation (CPR)::Chest compressions and breaths given to a person in cardiac arrest.|Blood return::Flushing the blood in the circuit back to the patient with saline. Staff also call it rinse-back.|Defibrillation-proof::A rating given to equipment that can stay connected to a patient during a defibrillator shock.}}
""",
    "case": {"title": "Palpitations at the end of the long weekend", "html": """
<p>Mr. Ramon Villanueva, 64, has diabetes and has been on hemodialysis for three years. He dialyzes on Mondays and Thursdays through a left arm fistula. This Monday was a holiday. He spent the long weekend at a town fiesta in his home province and missed his session. He arrives on Tuesday, five days after his last dialysis, 4.8 kilograms above his dry weight. Nurse Liza Manalo draws his blood before dialysis as ordered and starts the session.</p>
<p>Forty minutes later he calls her. &ldquo;My heart is jumping, and my chest feels heavy.&rdquo; His pulse is fast and irregular at about 140 per minute. His blood pressure is 100/60 mm Hg. It was 160/90 at the start. He is sweating. Nurse Manalo looks at you and asks, &ldquo;Doctor, do we stop and return the blood?&rdquo;</p>
""", "questions": ["What do you do in the first two minutes?",
                  "Is this the coronary arteries, the potassium, or the dialysis itself, and which tests help you tell?",
                  "Do you stop dialysis, and do you return the blood?"]},
    "sections": [
        ("pain", "Chest pain", "Chest pain in the chair: eight causes", """
<p>When a patient on the machine reports chest pain, your first task is to sort. Two things matter: whether this is dangerous now, and whether the circuit is involved.</p>
{{fig:pod15_pain_map}}
<div class="table-wrap"><table>
<thead><tr><th>Cause</th><th>Why it happens in dialysis patients</th><th>Clues at the chair</th></tr></thead>
<tbody>
<tr><td>Coronary artery disease</td><td>Very common. Dialysis stresses narrowed arteries</td><td>Heaviness, breathlessness, sweating, a pressure drop. Pain may be absent</td></tr>
<tr><td>Pericarditis</td><td>Inflammation of the sac around the heart, linked to under-dialysis</td><td>Sharp pain, worse lying flat, eased by sitting forward. Missed sessions</td></tr>
<tr><td>Aortic dissection</td><td>Long-standing high blood pressure</td><td>Sudden tearing pain that goes to the back. Unequal pulses</td></tr>
<tr><td>Pulmonary embolism</td><td>Clot from a leg vein or a catheter</td><td>Sudden breathlessness, low oxygen saturation, fast heart rate</td></tr>
<tr><td>Air embolism</td><td>Air enters the venous line or an open catheter</td><td>Sudden cough, breathlessness, or collapse. Air or foam in the venous line</td></tr>
<tr><td>Hemolysis</td><td>Red cells are damaged by faulty dialysis fluid or a kinked line</td><td>Chest and back pain. Blood in the lines looks translucent, like red wine. Several patients may be affected</td></tr>
<tr><td>Dialyzer reaction</td><td>An allergic-type reaction to the dialyzer or a substance in the circuit</td><td>Starts in the first minutes. Itching, wheeze, swelling, flushing, low blood pressure</td></tr>
<tr><td>Chest wall or stomach</td><td>Muscle strain, reflux</td><td>Diagnosed only after the others are excluded</td></tr>
</tbody></table></div>
<p>The first four causes apply to any patient with acute chest pain.[[gulati2021]] The next three come from the circuit.[[daugirdas2015]]</p>
<h3>Why coronary disease is common, and often quiet</h3>
<p>Kidney disease speeds up disease of the heart and its arteries.[[defilippi2017]] A thickened left ventricle and narrowed coronary arteries are very frequent in these patients.[[turakhia2018]] Thick muscle needs more oxygen, and anemia delivers less. Fluid removal can also lower the pressure that fills the coronary arteries.</p>
<p>The warning signs are often missing. In a United States registry study of 3,049 dialysis patients admitted with a heart attack, 44.4% had chest pain on arrival, compared with 68.3% of patients not on dialysis. Only 19.1% had ST elevation, compared with 35.9%. Nearly half, 44.8%, were first given a diagnosis other than acute coronary syndrome.[[herzog2007]] The data are retrospective and date from 1998 to 2000.</p>
{{key:In a dialysis patient, breathlessness, sweating, sudden weakness, or an unexplained fall in blood pressure can be the only sign of a heart attack. Treat these as possible chest pain.}}
"""),
        ("ecg", "ECG and troponin", "Two tests and their limits: the ECG and troponin", """
<p>The 12-lead electrocardiogram (ECG) is your fastest test. The American chest pain guideline states that, in any setting, an ECG should be acquired and reviewed within 10 minutes of arrival for acute chest pain, and repeated if symptoms continue. Where an ECG cannot be obtained, it advises referral to an emergency department.[[gulati2021]] The 10-minute figure is the guideline&rsquo;s standard, reported here for reference. It is not a target set by this series. Record the ECG as early as your unit&rsquo;s protocol allows.</p>
<p>Always compare with an old tracing. A thick left ventricle already produces large voltages and ST changes at rest, so a change from the previous ECG matters most.</p>
{{fig:pod15_ecg_strips}}
{{cards:A first read in five steps|Rate::Very fast or very slow.|Regularity::An irregular rhythm with no clear P waves suggests atrial fibrillation.|QRS width::A wide QRS means a ventricular rhythm, a conduction block, or a high potassium.|ST segments::New elevation or depression compared with the old ECG.|T waves and QT::Tall, peaked T waves suggest high potassium. A long QT suggests low potassium, low calcium, or a medicine.}}
<p>Before dialysis, a high potassium can produce peaked T waves, a wide QRS, and a slow rhythm. Late in a session and afterward, a low potassium can lengthen the QT interval and favor ventricular rhythms. As Module 2 explained, the ECG is an insensitive test for high potassium, so a normal tracing does not exclude it.[[montague2008]]</p>
<h3>Troponin in kidney failure</h3>
<p>In most patients a raised troponin points to an acute event. In dialysis patients it may not. With high-sensitivity tests, most patients with kidney failure have a troponin above the usual upper limit even when they are well.[[thygesen2018]] These chronic elevations are thought to reflect underlying heart disease more than slow clearance by the kidneys, and they predict a worse outlook.[[defilippi2017]]</p>
<p>A single raised value therefore cannot diagnose a heart attack. The pattern over time can. The Fourth Universal Definition of Myocardial Infarction requires a rise or fall in troponin together with evidence of ischemia, such as symptoms or new ECG changes. It found no data to support different troponin limits in kidney disease.[[thygesen2018]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Troponin finding</th><th>What it most likely means</th></tr></thead>
<tbody>
<tr><td>Raised and unchanged on repeat testing</td><td>Chronic heart muscle injury. It does not exclude coronary disease</td></tr>
<tr><td>Rising or falling on repeat testing, with symptoms or ECG change</td><td>Acute heart attack is likely</td></tr>
<tr><td>Not raised on a single early sample</td><td>Too early to exclude a heart attack</td></tr>
</tbody></table></div>
<p>Repeat testing over hours belongs in a hospital, not in an outpatient unit.</p>
"""),
        ("pathway", "Stop or continue", "The chest pain pathway: stop dialysis, return blood, transfer", """
<p>Look at the patient and the circuit before you decide anything about the blood.</p>
{{flow:Chest pain in the chair|Go to the patient::Check alertness, breathing, and color. Ask for blood pressure, pulse, and oxygen saturation. Attach the monitor.|Look at the circuit::Air in the venous line, blood of an unusual color, clotting, or onset in the first minutes of the session.|Take the protocol&rsquo;s first steps::These usually include stopping fluid removal and giving oxygen when saturation is low.|Record a 12-lead ECG::Compare it with the last one on file.|Call the attending nephrologist::Use SBAR from Module 1. Call during these steps, not after.|Decide about dialysis and the blood::Use the table below with the nephrologist.|Arrange transfer::For an ECG change, ongoing pain, or instability.}}
<h3>Whether to stop, and whether to return the blood</h3>
<p>Returning the blood gives the patient back their red cells, and it is the default when a session stops early. In four situations the blood in the circuit may be the cause of the harm, and returning it can make the patient worse. A review of hemodialysis emergencies advises stopping without returning the blood for air embolism, hemolysis, and a severe dialyzer reaction.[[greenberg2021]] Withholding clotted blood is standard dialysis practice.[[daugirdas2015]]</p>
<div class="table-wrap"><table>
<thead><tr><th>What you find</th><th>Dialysis</th><th>Blood in the circuit</th></tr></thead>
<tbody>
<tr><td>Pain has settled, ECG unchanged, patient stable</td><td>May continue under close observation if the nephrologist agrees</td><td>&mdash;</td></tr>
<tr><td>ECG change, ongoing pain, low blood pressure, or an unstable rhythm</td><td>Stop per protocol</td><td>Return it, unless one of the rows below applies</td></tr>
<tr><td>Air or foam in the venous line, or suspected air embolism</td><td>Stop the pump and clamp the venous line at once</td><td><strong>Do not return</strong></td></tr>
<tr><td>Suspected hemolysis</td><td>Stop and clamp. Check other patients</td><td><strong>Do not return</strong></td></tr>
<tr><td>Severe reaction in the first minutes: wheeze, swelling, collapse</td><td>Stop and clamp</td><td><strong>Do not return</strong></td></tr>
<tr><td>Clotted circuit</td><td>Stop</td><td><strong>Do not return</strong> clotted blood</td></tr>
</tbody></table></div>
<p>The circuit holds a small part of the patient&rsquo;s blood. Losing it is far safer than returning air, damaged cells, or the trigger of a reaction. Stopping a session also has a cost, because the potassium and fluid remain. The decision to end the session, and the plan to complete dialysis later, belong to the attending nephrologist.</p>
<h3>Arranging transfer</h3>
<p>For suspected acute coronary syndrome outside a hospital, the guideline recommends transfer to an emergency department by emergency medical services.[[gulati2021]]</p>
{{cards:Transfer checklist|Where::The emergency room in your unit&rsquo;s transfer plan. Telephone the receiving physician yourself.|How::By ambulance, with a monitor and an escort per protocol.|What goes with the patient::Every ECG with its time, today&rsquo;s dialysis record, the medicine list, and the time and type of blood thinner given during dialysis.|The access::State which arm holds the fistula or graft.}}
{{call:Stop and call the attending nephrologist for every patient with chest pain plus an ECG change, a fall in blood pressure, a new abnormal rhythm, breathlessness, or fainting. Call while you take the first steps in your unit&rsquo;s protocol.}}
"""),
        ("rhythm", "Arrhythmia", "Why rhythms fail around dialysis, and new atrial fibrillation", """
<p>A steady rhythm needs stable salts across the cell wall and healthy muscle. In dialysis patients the salts swing with the dialysis cycle, and the muscle is thick and scarred.</p>
{{fig:pod15_week_risk}}
<div class="table-wrap"><table>
<thead><tr><th>Stress on the rhythm</th><th>When it peaks</th><th>What it does</th></tr></thead>
<tbody>
<tr><td>High potassium and acid</td><td>End of the long gap, before the session</td><td>Slows conduction. Slow rhythms, wide QRS, arrest</td></tr>
<tr><td>Rapid fall in potassium</td><td>During the session and the hours after</td><td>Lengthens the QT interval. Ventricular rhythms</td></tr>
<tr><td>Fluid overload</td><td>End of the long gap</td><td>Stretches the heart chambers. Atrial fibrillation</td></tr>
<tr><td>Large or rapid fluid removal</td><td>Second half of the session</td><td>Low blood pressure and less blood flow to heart muscle</td></tr>
</tbody></table></div>
<p>The evidence is observational. Sudden cardiac death accounts for about 25% to 29% of all deaths in patients on hemodialysis.[[turakhia2018]] In a United States study of 32,065 patients, deaths and cardiac admissions were more frequent on the day after the two-day gap.[[foley2011]] A review of 400 arrests in dialysis units found more arrests on Mondays. Patients who arrested were about twice as likely to have been dialyzed against a very low potassium dialysis fluid.[[karnik2001]]</p>
<p>A later case-control study of 502 arrests linked sudden arrest to dialysis fluid potassium below 2 mmol/L, to larger fluid removal volumes, and to low-calcium dialysis fluid.[[pun2011]] These designs cannot prove cause. They do show why the dialysis fluid and the fluid target are the nephrologist&rsquo;s decisions.</p>
<p>In 66 patients fitted with implanted rhythm recorders for six months, significant arrhythmias were most frequent during the first session of the week. They also rose in the last 12 hours before each session, most of all after the long gap. Most events were slow rhythms, not ventricular tachycardia.[[roychaudhury2018]] The study was small. Patients in these studies dialyzed three times a week, so the risk for twice-weekly patients, whose gaps are longer, has not been measured directly.</p>
<h3>New atrial fibrillation in the chair</h3>
<p>Estimates of the prevalence of atrial fibrillation (AF) in dialysis patients range from 15% to 40%.[[turakhia2018]] Dialysis can set it off. In 40 dialysis patients with implanted defibrillators, AF began more often on dialysis days, and especially during the session.[[buiten2014]]</p>
{{flow:New atrial fibrillation in the chair|Confirm::Feel the pulse and record a 12-lead ECG. An irregular rhythm with no P waves is AF.|Judge stability::Low blood pressure, chest pain, breathlessness, or confusion means the patient is unstable.|If unstable::Call for the emergency cart. Follow the tachycardia algorithm of advanced cardiac life support (ACLS) and your unit&rsquo;s protocol, and have someone call the attending nephrologist now.|Look for the trigger::Today&rsquo;s potassium, the fluid removed so far, fever, missed medicines, and chest pain.|Take first steps per protocol::These usually include stopping fluid removal while you assess.|Call the attending nephrologist::Ask whether to continue or stop the session, and who will decide on rate control and blood thinners.}}
<p>Dialysis patients were mostly excluded from trials of AF treatment, so the best long-term approach is uncertain.[[turakhia2018]] Do not start these medicines on your own.</p>
{{call:Stop and call for any new rhythm with low blood pressure, chest pain, breathlessness, or reduced alertness, and for any wide-QRS or very slow rhythm even when the patient feels well. Bring the defibrillator to the chair before you telephone.}}
"""),
        ("arrest", "Cardiac arrest", "Cardiac arrest in the dialysis chair", """
<p>A code beside a dialysis machine is ordinary resuscitation with three extra jobs: the chair, the machine with its blood, and the access. Everything else is the basic life support (BLS) and ACLS you already know.</p>
<p>Two large United States series found 7 and 4.5 arrests per 100,000 sessions.[[karnik2001]][[pun2011]] Reports of the first rhythm disagree. In 102 arrests attended by paramedics in dialysis centers, ventricular fibrillation or tachycardia was the first rhythm in 72.[[davis2008]] In a later registry of 398 arrests in dialysis clinics, 66% had a first rhythm that was not shockable.[[pun2019]] Attach the defibrillator early in every arrest and let the rhythm decide.</p>
<p>In the same registry, dialysis staff began cardiopulmonary resuscitation (CPR) in 81.4% of arrests, and staff-started CPR was associated with about three times the odds of leaving the hospital alive.[[pun2019]] The study was observational. It still argues against waiting for outside help.</p>
<h3>What current guidance says</h3>
<p>The European Resuscitation Council (ERC) 2025 guidelines include a section on cardiac arrest in hemodialysis patients.[[erc2025_special]] It keeps the standard algorithm and adds five points.</p>
{{cards:ERC 2025: cardiac arrest in hemodialysis patients|Operator::Assign a trained dialysis nurse or technician to operate the dialysis machine.|Stop and return::Stop dialysis and return the patient&rsquo;s blood volume with a fluid bolus.|Disconnect::Disconnect from the dialysis machine unless it is defibrillation-proof, and beware of wet surfaces.|Access::Leave the dialysis access open and use it for drug administration.|Afterward::Dialysis may be required in the early period after resuscitation.}}
<p>The ERC text also advises teams to avoid delays in defibrillation. It advises considering high potassium when arrest occurs before or early in a session, and low potassium when it occurs in the middle or late part of a session or soon after. The five points are not labeled with evidence grades. They do not say what to do when a shock is ready before the blood has been returned.[[erc2025_special]]</p>
<p>The American Heart Association (AHA) 2025 guidelines contain no section on the hemodialysis unit. Their general recommendations apply.[[aha2025_bls]][[aha2025_special]]</p>
<p>The steps below put those points in a working order for this series. The order is the series&rsquo; own, based on the rule that nothing delays compressions or a shock. Your unit&rsquo;s protocol governs.</p>
{{flow:Cardiac arrest in the dialysis chair|Confirm and call::Unresponsive and not breathing normally. Call the code and send for the defibrillator.|Flatten and compress::Recline the chair fully and start chest compressions at once. Compressions do not wait for the machine.|Attach the defibrillator as soon as it arrives::Dry the chest and apply the pads while compressions continue. Read the rhythm.|Assign the machine at the same time::One dialysis nurse stops dialysis and starts blood return while compressions continue, unless a do-not-return condition applies. This work never interrupts compressions.|Shock without delay::For a shockable rhythm, the nurse clamps and disconnects the lines first, unless the machine is defibrillation-proof. If blood return is not finished, it is abandoned. Everyone stands clear of the patient, the chair, and wet surfaces.|Use the access::Keep the needles or catheter in place and open for drugs.|Run the ACLS algorithm::Cycles, rhythm checks, and drugs per the algorithm and your unit&rsquo;s protocol.|Think of dialysis causes::Potassium first, then bleeding, air, hemolysis, and reaction.|Call out::The ambulance or hospital code team, and the attending nephrologist.}}
{{fig:bls|The adult basic life support sequence.}}
<h3>From chair to flat</h3>
<p>Compressions on a half-reclined patient in a padded chair are likely to be less effective. The AHA advises CPR on a firm surface with the person on their back when this is feasible and does not delay compressions. It also advises resuscitation where the person is found, as long as high-quality CPR can be given safely.[[aha2025_bls]] Neither guideline addresses dialysis chairs.</p>
{{fig:pod15_chair_flat}}
<p>Recline the chair fully flat and begin. Then make the surface firm as your unit&rsquo;s protocol describes, with a rigid board or a controlled move to the floor. A move can dislodge the needles, so one person guards the access arm.</p>
"""),
        ("machine", "Machine and access", "The machine, the blood, and the access during a code", """
<p>Each question below has a short answer in the guidance and a detail your unit&rsquo;s protocol must settle in advance.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>What the guidance says</th><th>What to settle in your unit</th></tr></thead>
<tbody>
<tr><td>Who handles the machine?</td><td>A trained dialysis nurse or technician, not the team leader[[erc2025_special]]</td><td>Name this role at the start of every shift</td></tr>
<tr><td>Is the blood returned?</td><td>Yes. Stop dialysis and return the blood volume with a fluid bolus[[erc2025_special]]</td><td>The saline volume, the do-not-return conditions, and a written rule that a ready shock is never held for blood return</td></tr>
<tr><td>Is the patient disconnected?</td><td>Yes, unless the machine is defibrillation-proof[[erc2025_special]]</td><td>Whether your machines carry this rating. Ask the technician</td></tr>
<tr><td>Where do drugs go?</td><td>Through the dialysis access, which is left open[[erc2025_special]]</td><td>Which port or needle is used, who gives the drugs, and how the line is flushed</td></tr>
</tbody></table></div>
<p><strong>The order.</strong> Compressions start first and do not stop for the machine. The defibrillator pads go on as soon as the defibrillator arrives. The machine nurse stops dialysis and returns the blood at the same time as these steps, not before them.</p>
<p><strong>The shock.</strong> Blood return never delays compressions or defibrillation. If a shockable rhythm appears before the blood is back, the nurse clamps the lines and disconnects at once, and the blood left in the circuit is given up. A machine rated defibrillation-proof may stay connected. Spilled dialysis fluid and saline conduct electricity, so dry the chest and keep staff clear of wet areas. Confirm this sequence in your unit&rsquo;s written protocol before your first shift.</p>
<p><strong>The blood: an addition to the ERC wording.</strong> The ERC guidance says to return the blood and lists no exceptions.[[erc2025_special]] This series adds four do-not-return conditions during an arrest: air in the line, suspected hemolysis, a severe dialyzer reaction, and a clotted circuit. The addition comes from the dialysis emergency literature, not from a resuscitation guideline. A review of hemodialysis emergencies advises stopping dialysis without returning the blood for air embolism, hemolysis, and a severe dialyzer reaction.[[greenberg2021]] Withholding clotted blood is standard dialysis practice.[[daugirdas2015]] Neither source studied cardiac arrest, so this is a reasoned extension for your medical director to confirm. In those cases the nurse clamps the lines and disconnects without returning the blood.</p>
<p><strong>The access.</strong> The needles or catheter already in place are faster than any new cannula. Disconnecting from the machine does not mean removing them. A needle dislodged during compressions bleeds quickly under the blanket, so one person watches the access arm throughout.</p>
{{key:Disconnect the machine, keep the access. The needles or catheter stay in place until the code is over.}}
<p><strong>After the pulse returns.</strong> The patient needs a hospital. Dialysis may be needed early, guided by fluid status and blood tests.[[erc2025_special]] The attending nephrologist arranges this with the receiving team.</p>
"""),
        ("causes", "Reversible causes", "Reversible causes special to dialysis", """
<p>All the reversible causes taught in ACLS apply to a dialysis patient.[[erc2025_special]] Start with the timing of the arrest within the session.</p>
<div class="table-wrap"><table>
<thead><tr><th>Cause</th><th>When to suspect it</th><th>First response, per unit protocol</th></tr></thead>
<tbody>
<tr><td>High potassium</td><td>Before or early in the session, after a long gap. Slow, wide rhythm</td><td>Hyperkalemia arrest protocol. Urgent potassium from the pre-dialysis sample</td></tr>
<tr><td>Rapid potassium fall</td><td>Late in the session or soon after. Very low potassium dialysis fluid</td><td>ACLS algorithm. Report the dialysis fluid used</td></tr>
<tr><td>Low blood volume</td><td>Late in the session with a large fluid target, or any bleeding</td><td>Stop fluid removal. Return blood. Fluid per protocol</td></tr>
<tr><td>Bleeding</td><td>Blood on the floor or under the blanket. Dislodged needle or open catheter</td><td>Direct pressure. Clamp. Fluid per protocol</td></tr>
<tr><td>Fluid overload with low oxygen</td><td>Before the session, large weight gain, frothy sputum</td><td>Airway and oxygen. Early dialysis after the pulse returns</td></tr>
<tr><td>Air embolism</td><td>Sudden collapse with air in the venous line or an open catheter</td><td>Clamp. Do not return blood. High-concentration oxygen. Position per protocol</td></tr>
<tr><td>Hemolysis</td><td>Translucent, wine-red blood in the lines. Other patients unwell</td><td>Clamp. Do not return blood. Stop all affected machines</td></tr>
<tr><td>Dialyzer reaction</td><td>First minutes of the session. Wheeze, swelling</td><td>Clamp. Do not return blood. Anaphylaxis protocol</td></tr>
<tr><td>Cardiac tamponade</td><td>Under-dialyzed patient with recent pericarditis. Distended neck veins</td><td>ACLS algorithm. Urgent hospital transfer</td></tr>
</tbody></table></div>
<h3>Hyperkalemia during arrest: where the guidelines differ</h3>
<p>The ERC recommends intravenous calcium and sodium bicarbonate for hyperkalemic arrest, and notes that dialysis is the definitive treatment but is rarely used during an arrest.[[erc2025_special]] The AHA states that the effectiveness of intravenous calcium, sodium bicarbonate, and insulin with glucose in arrest from suspected hyperkalemia is not well established. It advises against inhaled beta-agonists during arrest.[[aha2025_special]]</p>
<p>Both positions rest on limited evidence. The ERC itself states that the evidence for or against intravenous calcium in this setting is insufficient.[[erc2025_special]] This series gives no drugs or doses. Follow your ACLS training and your unit&rsquo;s protocol, approved by the medical director, and do not let any drug delay compressions or a shock.</p>
<p>Positioning for air embolism also varies. The AHA considers a flat position on the back or the recovery position reasonable.[[aha2025_special]] Dialysis texts and reviews teach the left side for air in the veins, some with the head down.[[daugirdas2015]][[greenberg2021]] Follow your unit&rsquo;s protocol while the patient has a pulse. A patient in cardiac arrest lies flat on the back for compressions.</p>
"""),
        ("team", "Team and debrief", "Team roles, the first five minutes, and the debrief", """
<p>You are the team leader. Stand at the foot of the chair, keep your hands free, and give short orders by name. Ask each person to repeat the order back.</p>
{{fig:code_roles|Positions around the chair. Add one nurse at the machine.}}
<div class="table-wrap"><table>
<thead><tr><th>Role</th><th>First five minutes</th></tr></thead>
<tbody>
<tr><td>Team leader (physician on duty)</td><td>Confirms arrest, assigns roles, reads the rhythm, directs the algorithm, seeks the cause</td></tr>
<tr><td>Compressor</td><td>Starts compressions at once and rotates with a second person</td></tr>
<tr><td>Airway</td><td>Opens the airway, gives breaths with a bag and mask, connects oxygen</td></tr>
<tr><td>Defibrillator</td><td>Brings the cart, dries the chest, applies pads, charges and shocks on the leader&rsquo;s order</td></tr>
<tr><td>Machine nurse</td><td>Stops dialysis, returns or withholds the blood as ordered, disconnects, then guards the access</td></tr>
<tr><td>Drugs</td><td>Prepares and gives drugs through the access, flushes, calls out each one</td></tr>
<tr><td>Recorder</td><td>Notes the time of collapse, each shock, drug, and rhythm check</td></tr>
<tr><td>Caller</td><td>Telephones the ambulance or hospital code team, the nephrologist, then the family</td></tr>
<tr><td>Floor nurse</td><td>Stays with the other patients, draws screens, and keeps watching their machines</td></tr>
</tbody></table></div>
{{fig:code_first5|The first five minutes. Assign roles in the first minute.}}
<p>Small units have fewer people than roles, so combine roles in advance. For hospitals, the AHA considers designated code teams with clearly defined roles and adequate training reasonable.[[aha2025_systems]]</p>
{{fig:code_readiness|Check readiness at the start of each shift.}}
<h3>The debrief</h3>
<p>Every code ends with a short team conversation. The AHA states that performance-focused debriefing of rescuers after cardiac arrest can be effective for improving resuscitation, and that using both an immediate and a delayed debrief is reasonable.[[aha2025_systems]] Keep the immediate one brief and without blame: what went well, what was hard, and what to change. Check on the staff and on the patients who watched.</p>
{{call:Call a code and start compressions for any patient who is unresponsive and not breathing normally. Have a team member call the attending nephrologist and the ambulance while you lead.}}
{{flow:Call card: heart emergencies in the chair|Recognize::Chest pain, or breathlessness, sweating, or a pressure drop without pain. A new abnormal pulse. Unresponsive and not breathing normally means cardiac arrest.|First 2 minutes::With a pulse: monitor, vital signs, circuit check, unit protocol, 12-lead ECG. Without a pulse: call the code, flatten the chair, compress, attach the defibrillator.|Stop dialysis?::Stop per protocol for cardiac arrest, ECG change, ongoing pain, low blood pressure, or an unstable rhythm. Otherwise the nephrologist decides.|Return the blood?::Yes when stopping, including cardiac arrest. Compressions and a shock always come first. If a shock is ready, clamp and disconnect without finishing blood return. Do NOT return blood when there is air in the venous line, suspected hemolysis, a severe dialyzer reaction, or a clotted circuit. Clamp and disconnect. Keep the access in place.|Call::The attending nephrologist during the first steps. The ambulance or hospital code team for arrest and for transfer.|Write::Time of onset, vital signs, each ECG, what was stopped, whether blood was returned and why, drugs and shocks, who was called and when, and the patient&rsquo;s condition on leaving.}}
"""),
    ],
    "debrief": ["""
<p><strong>What do you do in the first two minutes?</strong> Go to Mr. Villanueva and look at him. He is awake, so this is not an arrest, but a fast irregular pulse with a fall in pressure, chest heaviness, and sweating makes him unstable. Ask for the monitor and the emergency cart. Check the circuit for air and for blood of an unusual color. Take the first steps in your unit&rsquo;s protocol, record a 12-lead ECG, and have someone telephone the attending nephrologist now.</p>
<p><strong>Is it the coronary arteries, the potassium, or the dialysis?</strong> Probably more than one. The ECG is likely to show atrial fibrillation. Read it for ST change and potassium effects as well. Five days of fluid stretched his heart, and five days of potassium are now falling quickly. Either can set off AF, and fast AF can cause ischemia. The pre-dialysis potassium that Nurse Manalo drew is the most useful result available, so ask for it urgently. One troponin will not settle the question. He needs serial testing in a hospital.</p>
<p><strong>Do you stop dialysis, and do you return the blood?</strong> He has a new rhythm, a pressure drop, and chest heaviness, so the pathway points to stopping per protocol. Confirm this with the attending nephrologist, who is already being called, because stopping leaves his fluid and potassium in place. No do-not-return condition is present, so the blood is returned and the access is kept in place. The nephrologist decides where and when his dialysis is completed, usually in a hospital with monitoring. Arrange an ambulance transfer with his ECGs and the dialysis record.</p>
<p>The answer to Nurse Manalo&rsquo;s question came from three observations: the patient, the circuit, and the ECG.</p>
"""],
    "skills": {
        "title": "12-lead ECG at the chairside, and mock code as team leader",
        "intro": "Part A: acquire and read a 12-lead ECG on a patient during dialysis while your preceptor observes. Part B: lead one mock cardiac arrest at a dialysis station using the unit&rsquo;s own chair, machine, and emergency cart.",
        "items": [
            ("Part A. Explains the test to the patient, exposes the chest with privacy, and keeps the access arm still and visible.", False),
            ("Places the six chest leads and four limb leads correctly, moving a limb lead up the arm when the access is in the way.", True),
            ("Records a tracing free of artifact and labels it with the patient&rsquo;s name, the date, the time, and the symptoms.", True),
            ("Reads aloud in order: rate, regularity, QRS width, ST segments, T waves, and QT interval.", True),
            ("Compares the tracing with the most recent ECG on file and states what has changed.", True),
            ("States whether the findings need a call to the attending nephrologist and gives the report in SBAR form.", False),
            ("Part B. Confirms unresponsiveness and abnormal breathing, calls the code, and sends for the cart and defibrillator.", True),
            ("Orders the chair reclined flat and compressions started, and makes the surface firm as the unit&rsquo;s protocol describes.", True),
            ("Assigns roles by name, including one nurse to the dialysis machine and one person to guard the access.", True),
            ("Looks at the circuit and states whether the blood is to be returned or withheld, and why, without pausing compressions.", True),
            ("Before a shock, confirms the patient is disconnected or the machine is defibrillation-proof, does not wait for blood return, and checks that everyone is clear.", True),
            ("Directs that the dialysis access stays in place and is used for drugs per unit protocol.", False),
            ("Asks aloud for reversible causes special to dialysis, starting with the timing in the session and the potassium.", False),
            ("Leads a brief, blame-free debrief and names one change for the unit.", False),
        ],
        "placement": "During your supervised shifts, find the defibrillator, check that it was tested today, flatten one dialysis chair yourself, and ask the technician whether your unit&rsquo;s machines are rated defibrillation-proof. Read your unit&rsquo;s chest pain, hyperkalemia, and code protocols and note where each is kept.",
    },
    "quiz": [
        ("Ten minutes into a session with a new dialyzer type, a patient develops itching, wheeze, and a falling blood pressure. What is done with the blood in the circuit?",
         ["Return it quickly to support the pressure", "Return half and reassess", "Clamp the lines and do not return it", "Continue at a slower pump speed"], 2,
         "A severe early reaction may be caused by the dialyzer. Returning the blood delivers more of the trigger."),
        ("Why is a single raised troponin a poor guide to heart attack in a dialysis patient?",
         ["The dialyzer removes troponin", "Most dialysis patients have a chronically raised value, so the change over time matters", "The test fails in diabetes", "Troponin rises only after a day"], 1,
         "Chronic elevation is common. A rise or fall with evidence of ischemia defines an acute heart attack."),
        ("A 70-year-old woman with diabetes becomes breathless and sweaty in the third hour. Her blood pressure has fallen. She has no chest pain. After the first protocol steps, what comes next?",
         ["A 12-lead ECG and a call to the attending nephrologist", "Reassurance, because she has no pain", "Reassessment when the session ends", "A troponin, then a call when it is reported"], 0,
         "Fewer than half of dialysis patients with a heart attack had chest pain in a large registry. Treat these signs as possible ischemia."),
        ("According to the ERC 2025 guidance, who operates the dialysis machine during a cardiac arrest?",
         ["The team leader", "Whoever is nearest", "No one", "A trained dialysis nurse or technician assigned to it"], 3,
         "Assigning the machine to trained staff leaves the leader free to direct the code."),
        ("A patient collapses during dialysis, and the nurse sees foam in the venous line. What is correct for the circuit?",
         ["Return the blood with a fluid bolus", "Stop the pump, clamp the venous line, and do not return the blood", "Raise the pump speed to clear the air", "Disconnect the arterial line only"], 1,
         "Air in the venous line is a do-not-return condition. Returning the blood would push more air into the patient."),
        ("What does the ERC 2025 guidance say about the dialysis access during a cardiac arrest?",
         ["Remove the needles to prevent bleeding", "Never use it for drugs", "Leave it open and use it for drugs", "Use it only after the pulse returns"], 2,
         "The access is already in the circulation and is faster than a new cannula."),
        ("When must a patient be disconnected from the dialysis machine before a shock?",
         ["Never", "Only with a catheter", "Only in a non-shockable rhythm", "Whenever the machine is not rated defibrillation-proof"], 3,
         "The ERC advises disconnection unless the machine is defibrillation-proof. Know your machines&rsquo; rating before a code."),
        ("A man who missed a session arrests in the waiting area before dialysis. The monitor shows a slow, wide rhythm. Which reversible cause leads your list?",
         ["High potassium", "Rapid fall in potassium", "Air embolism", "Dialyzer reaction"], 0,
         "Arrest before a session after a long gap points to hyperkalemia. The other three need a running circuit."),
        ("Why do arrhythmias cluster around the first session after the long gap?",
         ["Patients are more anxious", "Potassium and fluid peak, then fall fastest in that session", "Machines are less reliable after a rest day", "Blood thinners wear off"], 1,
         "Both the peak and the rapid correction stress the rhythm."),
        ("Studies disagree on whether the first rhythm in dialysis unit arrests is usually shockable. What follows in practice?",
         ["Defibrillators are not useful in dialysis units", "Shock every patient without a rhythm check", "Delay the defibrillator until drugs are given", "Attach the defibrillator early in every arrest and let the rhythm decide"], 3,
         "Either type of rhythm may be present, so early rhythm analysis is needed alongside immediate compressions."),
        ("A patient develops new atrial fibrillation in the second hour. He is stable and feels well. A colleague suggests starting a blood thinner today. What is the best response?",
         ["Start it at once", "Record an ECG, look for triggers, and call the attending nephrologist", "Ignore the rhythm", "Stop dialysis and send him home"], 1,
         "Evidence for long-term AF treatment in dialysis patients is limited. The decision belongs to the nephrologist and cardiologist."),
        ("How do the ERC and AHA 2025 guidelines compare on intravenous calcium for cardiac arrest from high potassium?",
         ["Both strongly recommend it", "Both advise against it", "The ERC recommends it, and the AHA says its effectiveness is not well established", "Neither mentions it"], 2,
         "The guidelines differ, and both rest on limited evidence. Your unit&rsquo;s protocol decides."),
        ("A patient arrests in a half-reclined dialysis chair. What is the first step for positioning?",
         ["Recline the chair flat and start compressions", "Carry the patient to another room", "Compress with the patient sitting up", "Wait for a stretcher"], 0,
         "Compressions start where the patient is, on the back, on as firm a surface as can be achieved without delay."),
        ("A session is stopped for chest pain with new ST depression. The patient is stable. How does he travel to the emergency room?",
         ["By private car with a relative", "By taxi with a nurse", "On foot if the hospital is near", "By ambulance with monitoring and an escort"], 3,
         "For suspected acute coronary syndrome, the chest pain guideline recommends transfer by emergency medical services."),
        ("Which statement about the debrief after a code is most accurate?",
         ["It is needed only when the patient dies", "Its purpose is to find who made mistakes", "An immediate debrief and a later review are both reasonable, and the focus is performance", "It waits for the monthly meeting"], 2,
         "The AHA supports performance-focused debriefing, both immediate and delayed."),
    ],
    "terms": [
        ("Acute coronary syndrome", "Sudden loss of blood flow to heart muscle, including unstable angina and heart attack."),
        ("Troponin", "A heart muscle protein measured in blood. In dialysis patients a change over time matters more than one value."),
        ("Atrial fibrillation", "A fast, irregular rhythm in which the upper chambers of the heart quiver and do not contract."),
        ("Shockable rhythm", "Ventricular fibrillation or pulseless ventricular tachycardia, which a defibrillator shock can stop."),
        ("Blood return (rinse-back)", "Flushing the blood in the dialysis circuit back to the patient with saline."),
        ("Do-not-return conditions", "Air in the venous line, suspected hemolysis, a severe dialyzer reaction, and a clotted circuit."),
        ("Defibrillation-proof", "A rating for equipment that can remain connected to a patient during a defibrillator shock."),
        ("Reversible cause", "A condition that produced a cardiac arrest and can be corrected during resuscitation."),
        ("Hemolysis", "Breakdown of red blood cells, in dialysis usually from faulty dialysis fluid or a damaged blood line."),
        ("Debrief", "A short, structured team conversation after an event to learn what to keep and what to change."),
    ],
    "readings": [
        ("code-blue-acls-dialysis-unit.html", "A fuller walk-through of running a code in a dialysis unit."),
        ("hemodialysis-complications.html", "Air embolism, hemolysis, dialyzer reactions, and other complications named in this module."),
    ],
    "calcs": [],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
