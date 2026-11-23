# -*- coding: utf-8 -*-
"""Physician on Duty, Module 16: When the Circuit Fails: Air, Hemolysis, Reactions, and Blood Loss.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician and a dialysis nurse at a hemodialysis machine, the nurse closing a clamp on the blood line while the physician watches the patient.",
    "objectives": [
        "Name the points where the blood circuit can fail and the machine guard that watches each one.",
        "Carry out the first two minutes for air embolism, hemolysis, a dialyzer reaction, and blood loss from a dislodged needle or separated line.",
        "State the events in which the blood in the circuit must not be returned to the patient, and give the reason for each.",
        "Respond to a clotting circuit, a blood leak alarm, and a dialysis fluid alarm within your unit&rsquo;s protocol.",
        "Recognize a cluster event and start the unit-wide response.",
        "Report a circuit emergency to the attending nephrologist and preserve what the investigation will need.",
    ],
    "big": """
{{plain:Think of the dialysis circuit as a loop road. Blood leaves the body, makes a short trip through the machine, and comes home. Air can get onto the road. The travelers can be injured on the way, which is hemolysis. The road itself can provoke them, which is a dialyzer reaction. The road can break open, or jam with clot. Each time, you ask one question first: is this blood safe to bring home?}}
<p>The picture has a limit. Blood is not a passive traveler. It reacts to the plastic, the membrane, the dialysis fluid, and the pump, and the patient reacts to what comes back. The circuit also holds only a small share of the patient&rsquo;s blood at any moment. Giving up that share costs far less than returning air, broken red cells, or an allergen. That trade is the center of this module.</p>
{{cards:Key terms for this module|Extracorporeal circuit::The blood lines and dialyzer outside the body, from the arterial needle to the venous needle.|Air embolism::Air that enters a vein or artery and blocks blood flow in the heart, lungs, or brain.|Hemolysis::Breaking of red blood cells, which releases hemoglobin and potassium into the plasma.|Dialyzer reaction::An allergic or inflammatory response to the dialyzer or to something used to make or sterilize it.|Venous needle dislodgement::The needle that returns blood to the patient comes out of the access while the pump is running.|Rinse-back::The usual end of treatment, when saline pushes the blood in the circuit back to the patient.|Cluster event::Two or more patients with the same new symptoms in the same shift, which points to a shared cause.}}
""",
    "case": {"title": "Three patients, one complaint.", "html": """
<p>It is 40 minutes into the second shift on a Wednesday. Mrs. Villanueva, 54, calls the nurse because her upper abdomen and back hurt and she feels sick. Her blood pressure, usually 140/80 mm Hg, is 186/104. While you examine her, Mr. Bautista, two chairs away, vomits. He also has abdominal pain. Then Ms. Ocampo, on the other side of the room, says her chest feels tight and her stomach aches.</p>
<p>The nurse, Ms. Reyes, points to Mrs. Villanueva&rsquo;s venous line. &ldquo;Doctor, look at the color.&rdquo; The blood is a bright, almost see-through red. A staff member at the next chair has already picked up a saline bag to end Mr. Bautista&rsquo;s treatment and return his blood. The technician mentions that the carbon tanks were changed the day before. Nine other patients are on machines.</p>
""", "questions": ["What do three patients with the same complaint in the same half hour tell you?",
                  "What do you do in the first two minutes, and is the blood returned?",
                  "Whom do you call, and what must be kept for the investigation?"]},
    "sections": [
        ("map", "The circuit map", "Where the circuit can fail, and the first question", """
<p>Life-threatening events in hemodialysis (HD) are rare. A review credits machine safety features, water testing, written protocols, and staff training, and attributes most emergencies that do occur to human error.[[saha2017]]</p>
{{fig:blood_circuit|The blood circuit. Blood is pulled from the access by the pump, pushed through the dialyzer, and returned through the venous chamber, the air detector, and the venous clamp.}}
<p>Each part of the circuit has a guard. Pressure monitors on the arterial and venous sides sense kinks and clots. The air detector and venous clamp sit below the venous chamber. The blood leak detector watches the used dialysis fluid for blood. Conductivity and temperature monitors check the dialysis fluid before it reaches the dialyzer.[[daugirdas2015]]</p>
<p>When something fails, you make three decisions in this order. Stop the blood pump or not. Return the blood or not. Then call. Rinse-back is a habit, so the second decision is the easiest to get wrong.</p>
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>Return the blood?</th><th>Reason</th><th>Basis</th></tr></thead>
<tbody>
<tr><td>Air in the venous line, or suspected air embolism</td><td><strong>No</strong></td><td>Rinse-back would push more air into the patient</td><td>Published review[[greenberg2021]]</td></tr>
<tr><td>Suspected hemolysis</td><td><strong>No</strong></td><td>The circuit blood carries free potassium from broken cells</td><td>Published review[[greenberg2021]]</td></tr>
<tr><td>Severe early dialyzer reaction (type A)</td><td><strong>No</strong></td><td>The circuit blood carries the trigger</td><td>Published review[[greenberg2021]]</td></tr>
<tr><td>Mild later dialyzer reaction (type B)</td><td>Treatment may continue</td><td>Symptoms are usually mild and settle</td><td>Published review[[greenberg2021]]</td></tr>
<tr><td>Venous needle dislodgement or line separation</td><td>Per unit protocol. Never through a line end that has been open</td><td>An open end is contaminated and may have drawn in air</td><td>Unit protocol and custom</td></tr>
<tr><td>Clotted dialyzer or venous chamber</td><td><strong>No</strong>, not through the clotted part</td><td>Clot must never be pushed toward the patient</td><td>Standard practice[[daugirdas2015]]</td></tr>
<tr><td>Confirmed blood leak</td><td>Per unit protocol and the nephrologist</td><td>Blood has met non-sterile dialysis fluid. Practice differs with the size of the leak</td><td>Unit protocol and custom</td></tr>
<tr><td>Dialysis fluid error or cluster event</td><td><strong>No</strong> if hemolysis is possible. Otherwise ask first</td><td>Wrong or contaminated fluid can break red cells</td><td>Published review[[greenberg2021]]</td></tr>
</tbody></table></div>
{{key:Three firm rules. Blood is not returned when there is air in the line, when hemolysis is suspected, and in a severe dialyzer reaction. When you are unsure which event you are facing, stop the pump, clamp the lines, and do not return the blood until you have spoken to the nephrologist.}}
"""),
        ("air", "Air embolism", "Air embolism: air on the wrong side of the detector", """
<p>The part of the circuit between the access and the blood pump is under negative pressure, because the pump is pulling. Any opening there sucks air in instead of leaking blood out. A loose needle connection, a crack in the tubing, an uncapped or unclamped dialysis catheter, an empty saline bag left open, or a badly primed dialyzer can each admit air.[[greenberg2021]] The air detector catches large volumes. Very small bubbles can pass it.[[greenberg2021]]</p>
<p>What happens next depends on posture. In a seated patient, air can rise through the internal jugular vein into the veins of the brain. In a patient lying down, it travels to the right heart and the lung vessels, where a large volume can cause low oxygen, low blood pressure, and cardiac arrest.[[greenberg2021]] One review cites 100 to 300 mL as a volume likely to be lethal in an adult.[[greenberg2021]]</p>
{{fig:pod16_air}}
<p>Suspect air embolism when a patient suddenly coughs, becomes breathless or confused, collapses, or seizes, and there is air or foam in the venous line.</p>
{{flow:First response to suspected air embolism|Stop and clamp::Have the blood pump stopped and the venous line clamped. The blood is not returned.|Position::Lay the patient flat on the left side. This tends to hold air in the right heart, away from the outflow to the lungs.|Oxygen::Give supplemental oxygen as your unit&rsquo;s protocol directs.|Support::Call for the emergency cart. Begin resuscitation per protocol if the patient arrests.|Call::Call the attending nephrologist and arrange hospital transfer.}}
<p>Sources differ on the head-down tilt. Older teaching adds it to the left-side position. A 2021 review advises the left lateral position for venous air and cautions that a head-down position may worsen brain swelling when air has reached the brain.[[greenberg2021]] No trial has compared positions. Follow your unit&rsquo;s protocol.</p>
{{call:Stop and call for any air or foam below the venous chamber, and for any sudden cough, breathlessness, or change in consciousness on dialysis. The blood is not returned. Never override the air detector to finish a treatment.}}
"""),
        ("hemolysis", "Hemolysis", "Hemolysis: blood damaged on the trip", """
<p>Red cells are flexible but fragile. They break when they are squeezed through a narrow point at high speed, heated, swollen by dilute fluid, or attacked by an oxidizing chemical. The broken cells release hemoglobin, which turns the plasma pink, and potassium. Module 2 explained why a potassium load is dangerous here.</p>
{{cards:What breaks red cells in a dialysis circuit|Mechanical::A kinked or defective blood line, a needle too small for the blood flow, or a very negative arterial pressure.|Chemical::Chloramine, copper, or nitrates in the water, or disinfectant left in the machine.|Thermal::Dialysis fluid that is too hot.|Osmotic::Dialysis fluid that is too dilute, so water enters the cells until they burst.}}
<p>These causes are drawn from a published review.[[greenberg2021]] In May 1998, 30 patients in three states of the United States developed hemolysis during dialysis. Twenty had high blood pressure, 18 had abdominal pain, 10 needed intensive care, and two died. Investigators traced the outbreak to one lot of blood tubing with a narrowed opening.[[duffy2000]] In 1987, a carbon filter failed in a center whose city water contained chloramine, and 41 patients needed transfusion for hemolytic anemia.[[tipple1991]]</p>
{{fig:pod16_cherry}}
<p>The patient may report nausea, vomiting, abdominal, back, or chest pain, breathlessness, or chills. Blood pressure often rises. The blood in the line looks brighter and more translucent than usual, a color described as cherry red.[[greenberg2021]]</p>
{{flow:First response to suspected hemolysis|Stop and clamp::Have dialysis stopped at once and the lines clamped. The blood is not returned.|Assess::Check airway, breathing, circulation, and the heart rhythm on a monitor.|Test::Send urgent potassium and hemoglobin, and tests for hemolysis, as your protocol lists.|Look for the cause::Trace the lines for a kink. Ask for the dialysis fluid temperature and conductivity readings.|Look around::Ask whether any other patient has similar symptoms.|Call::Call the attending nephrologist and arrange urgent hospital evaluation. The patient may need dialysis again on a new circuit for hyperkalemia.}}
<p>The rule on blood return is explicit. The circuit blood should not be returned, because the potassium released from broken cells can cause severe hyperkalemia.[[greenberg2021]] Severe hemolysis can also cause dangerous heart rhythms, pancreatitis, and death, so the review advises urgent emergency department evaluation, with repeat potassium and hemoglobin tests.[[greenberg2021]]</p>
{{call:Stop and call for cherry-red or translucent blood in the line, pink plasma in a sample, or abdominal, back, or chest pain with a rising blood pressure on dialysis. The blood is not returned. Keep the lines and dialyzer.}}
"""),
        ("reactions", "Dialyzer reactions", "Dialyzer reactions: when the membrane is the trigger", """
<p>The dialyzer puts a large foreign surface in contact with blood. Most patients tolerate it. A few react, either to the membrane or to a chemical used to sterilize it. Daugirdas and Ing divided these reactions into two types in 1988, and the division is still used.[[daugirdas1988]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>Type A (anaphylactic)</th><th>Type B (nonspecific)</th></tr></thead>
<tbody>
<tr><td>Timing</td><td>Early, usually within the first 20 to 30 minutes, often in the first minutes</td><td>Later in the treatment</td></tr>
<tr><td>Symptoms</td><td>Itching, hives, throat swelling, wheeze, breathlessness, chest pain, vomiting, low oxygen, low blood pressure, cardiac arrest</td><td>Chest pain and back pain, sometimes nausea and vomiting</td></tr>
<tr><td>Mechanism</td><td>Allergy to a sterilant such as ethylene oxide, or a bradykinin surge when certain membranes are used in a patient taking an angiotensin-converting enzyme (ACE) inhibitor</td><td>Activation of the complement system by the membrane</td></tr>
<tr><td>Severity</td><td>Can be fatal</td><td>Usually mild</td></tr>
<tr><td>Return the blood?</td><td><strong>No</strong></td><td>Treatment can continue if symptoms are mild</td></tr>
</tbody></table></div>
<p>The details in the table follow a 2021 review, which also notes that both types are now rarely seen.[[greenberg2021]] ACE inhibitors slow the breakdown of bradykinin, a substance that widens blood vessels, and one membrane material (AN69) increases its production.[[greenberg2021]]</p>
{{flow:First response to an early, severe (type A) reaction|Stop and clamp::Have dialysis stopped and the lines clamped. The blood is not returned.|Treat as anaphylaxis::Follow your unit&rsquo;s anaphylaxis protocol. Protect the airway and give oxygen.|Call::Call for help and call the attending nephrologist.|Keep::Keep the dialyzer and its packaging. Record the model and lot number.|Next session::The nephrologist chooses a different dialyzer and reviews the medicines.}}
<p>Type B is diagnosed only after excluding cardiac, embolic, and hemolytic causes of chest pain. Check vital signs, oxygen saturation, an electrocardiogram (ECG), and the color of the blood in the line, then call the nephrologist. Continuing the treatment, or changing the dialyzer, is the nephrologist&rsquo;s decision. Medicines given during treatment can also cause allergic reactions, and the first response is the same.[[saha2017]]</p>
{{call:Stop and call for itching, hives, wheeze, hoarseness, throat tightness, or a fall in blood pressure in the first minutes of a treatment. The blood is not returned in a severe reaction. Do not wait to see whether it passes.}}
"""),
        ("bloodloss", "Blood loss", "Blood loss: a dislodged needle or a separated line", """
<p>The pump does not know where the blood is going. If the venous needle slips out of the access, or a connection on the return side comes apart, the pump keeps delivering blood at the set flow, onto the bed or the floor. One review gives the loss as 300 to 450 mL per minute until the pump stops, and notes that severe bleeding and death can occur within minutes.[[greenberg2021]]</p>
<p>The venous pressure alarm often fails to catch this. The pressure the machine reads on the venous side is mostly a sum of two things: the resistance of the return tubing and needle, and the pressure inside the access. In a fistula the access pressure is usually the smaller part.[[frinak2023]] When the needle comes out, only that part is lost. The alarm sounds only if the fall is larger than the gap between the reading and the lower alarm limit.[[greenberg2021]] In a study of 99 patients, 29% of fistulas, against 94% of grafts, had an access pressure high enough for the alarm to be expected to detect a dislodgement.[[ribitsch2014]] In an engineering feasibility study, which used mostly laboratory data, the standard venous pressure alarm detected half of the dislodgements.[[holmer2020]] These figures are not clinical event rates, but the direction is clear: a silent machine does not mean the needle is in.</p>
{{fig:pod16_hidden}}
<p>Risk is higher in patients who are restless or confused, in those with difficult access or an allergy to tape, and whenever the access is covered.[[greenberg2021]] European renal nurses published 12 practice recommendations, based on expert consensus, not trials.[[vanwaeleghem2008]] Prevention is plain work: secure taping, needle sites and connections left uncovered, alarm limits left as set, and closer watch on high-risk patients.</p>
{{flow:First response to a dislodged needle or separated line|Stop and clamp::Have the blood pump stopped and the open line clamped on both sides of the break.|Press::Apply firm pressure to the needle site with gloved hands and gauze.|Assess the patient::Lay the patient flat. Check consciousness, pulse, and blood pressure. Give oxygen.|Estimate the loss::Look under the blanket, on the chair, and on the floor.|Treat::Follow your unit&rsquo;s protocol for blood loss and call for the emergency cart if the patient is unstable.|Call::Call the attending nephrologist. Fluids, transfusion, and transfer are decided together.}}
<p>The blood on the floor is lost. The published reviews used here give no rule about the blood still in the circuit after a dislodgement, so your unit&rsquo;s protocol decides. One principle holds everywhere: a needle that has come out is never reinserted, and a line end that has been open is contaminated and is never reconnected to the patient.</p>
{{call:Stop and call for any blood on the bed, chair, or floor, for a wet dressing over the access, or for a patient who becomes pale, sweaty, or drowsy with no explanation. Lift the blanket before you do anything else.}}
"""),
        ("clots", "Clotting and blood leak", "A clotting circuit and a blood leak alarm", """
<p>Blood clots when it touches plastic. Heparin or another blood thinner, ordered by the nephrologist, holds this back for the length of a treatment. Clotting becomes more likely when blood flow is low or keeps stopping for alarms, or when the blood thinner was reduced or omitted for a good reason such as recent bleeding.[[daugirdas2015]]</p>
{{fig:pod16_clot}}
<p>The signs are very dark blood in the circuit, dark streaks in the dialyzer fibers, clot in the venous chamber, and changing circuit pressures.[[daugirdas2015]]</p>
<p>The nurses usually see these signs first and act under protocol. If the circuit can still be rinsed back safely, the blood is returned early and the circuit replaced. If the dialyzer or venous chamber is clotted, the blood in that part is not returned, because clot must never be pushed toward the patient.[[daugirdas2015]] Record and report the blood lost in the circuit. Whether to restart, and with what blood thinner, is a prescription decision.</p>
<h3>Blood leak alarm</h3>
<p>A blood leak alarm means the detector has sensed blood in the used dialysis fluid. If true, the membrane has torn. Blood is escaping into the fluid, and non-sterile fluid may be reaching the blood. False alarms occur, so staff confirm the leak by testing the used fluid for blood, as the unit protocol describes.[[daugirdas2015]]</p>
<p>When a leak is confirmed, the treatment on that dialyzer stops. Practice on returning the blood differs between units and depends on the size of the leak. This rests on custom, not trial evidence. Follow your protocol, tell the nephrologist, and watch the patient afterward for fever or chills.</p>
{{call:Stop and call when a circuit clots, when a blood leak is confirmed, and whenever blood was not returned. Report the estimated blood loss. Do not order a restart or a change in blood thinner on your own.}}
"""),
        ("cluster", "Fluid errors and clusters", "Dialysis fluid errors, cluster events, and the Call card", """
<p>Every problem so far affects one patient. A fault in the water or the dialysis fluid can affect every patient in the room at once. The machine mixes treated water with concentrates and checks the result by its conductivity, which reflects the salt content, and by its temperature. If either is out of range, the machine diverts the fluid away from the dialyzer. This is called bypass.[[daugirdas2015]]</p>
<p>The guard fails when a monitor is faulty or overridden, or when the contaminant is something the machine does not measure. Fluid that is too dilute or too hot breaks red cells.[[greenberg2021]] Chloramine, which many city water suppliers add as a disinfectant, is not removed by reverse osmosis. Dialysis units rely on carbon filters to remove it, and outbreaks of hemolysis have followed when the carbon was exhausted.[[ward1996]] Bacteria and endotoxin in the fluid cause fever, chills, and low blood pressure.[[greenberg2021]]</p>
{{fig:wts_train|The water treatment steps. The carbon tanks remove chloramine. A failure here reaches every machine on the loop.}}
{{call:Stop and call when a conductivity or temperature alarm does not clear, or when anyone tries to override it. No patient is dialyzed against fluid the machine has rejected.}}
<h3>Recognizing a cluster event</h3>
<p>One patient with nausea is a patient problem. Two or more patients with the same new symptoms in the same shift are a unit problem until proved otherwise.</p>
{{flow:Cluster event response|Say it aloud::Tell the charge nurse that this is a possible cluster event.|Stop::Have treatments stopped per the cluster protocol, starting with patients who have symptoms. Hold all new starts.|Do not return blood::If hemolysis is possible, the blood is not returned for any affected patient.|Check water and fluid::The technician tests for chlorine and chloramine and checks conductivity, temperature, and the water system log.|Assess every patient::Vital signs, blood color in each line, and urgent potassium and hemoglobin for those with symptoms.|Call the Medical Director::Also call each attending nephrologist. The Medical Director decides when the unit may restart.|Preserve::Keep the lines, dialyzers, packaging with lot numbers, and samples of water and dialysis fluid.}}
<p>Afterward the unit carries out a root cause analysis, a structured review of how the failure passed each guard.[[saha2017]] Your notes are its raw material.</p>
<h3>Dialysis disequilibrium, briefly</h3>
<p>One event looks like a circuit failure and is not. Dialysis disequilibrium syndrome is headache, nausea, confusion, or seizures during or shortly after a session. The leading explanation is that urea falls faster in the blood than in the brain, so water moves into brain cells. It is most likely in a first treatment with a very high urea.[[greenberg2021]] If you suspect it, have the treatment stopped and call the nephrologist. The circuit is sound, so the usual blood return applies unless the nephrologist says otherwise.</p>
{{flow:Call card: when the circuit fails|Recognize::Sudden cough or breathlessness. Abdominal, back, or chest pain. Itching or wheeze in the first minutes. Blood outside the circuit. Cherry-red, very dark, or foamy blood in the line. Several patients with one complaint.|First 2 minutes::Have the blood pump stopped and the lines clamped. Check airway, breathing, and circulation. Give oxygen. Lift the blanket and look at the access and the lines.|Stop dialysis?::Yes for air, hemolysis, a severe reaction, blood loss, a clotted circuit, a confirmed blood leak, rejected dialysis fluid, and a cluster. A mild later reaction may continue if the nephrologist agrees.|Return the blood?::NOT returned when there is air in the line, when hemolysis is suspected, and in a severe dialyzer reaction. NOT returned through a clotted dialyzer or chamber or through a line end that has been open. If unsure, do not return it until you have spoken to the nephrologist.|Call::The attending nephrologist for every event. The Medical Director as well for a cluster or a suspected water or dialysis fluid fault. The emergency team if the patient is unstable.|Write::Time, symptoms, vital signs, whether blood was returned and why, estimated blood loss, machine and lot numbers, and whom you called.}}
"""),
    ],
    "debrief": ["""
<p><strong>What do three patients with the same complaint tell you?</strong> They tell you the cause is shared. Abdominal pain, vomiting, chest tightness, and a sharp rise in blood pressure in three patients within one half hour do not fit three separate illnesses. The bright, translucent blood in Mrs. Villanueva&rsquo;s line points to hemolysis. The carbon tanks were changed the day before, so chloramine in the dialysis fluid is a leading possibility. A faulty lot of tubing or a dialysis fluid error would look the same. You do not need to know which it is to act.</p>
<p><strong>What do you do in the first two minutes, and is the blood returned?</strong> You stop the staff member holding the saline bag. In suspected hemolysis the blood is not returned, because the circuit blood carries potassium released from broken cells. You tell the charge nurse that this is a possible cluster event. The three patients with symptoms are stopped and clamped first, the other nine under the cluster protocol, and no one new is connected. Each affected patient gets a heart monitor, oxygen as protocol directs, and urgent potassium and hemoglobin tests. The technician tests the water and checks the dialysis fluid readings while you examine patients.</p>
<p><strong>Whom do you call, and what is kept?</strong> You call the Medical Director, because the event may involve the water system and affects the whole unit, and each patient&rsquo;s attending nephrologist. The three patients with symptoms are likely to need hospital care and repeat potassium tests. The unit keeps the lines, dialyzers, packaging with lot numbers, the water system log, and samples of water and dialysis fluid. It does not restart until the Medical Director says it may.</p>
<p>The nurse who said &ldquo;look at the color&rdquo; made the diagnosis.</p>
"""],
    "skills": {"title": "Emergency disconnect and manual blood return on a training circuit",
               "intro": "Perform both drills on a primed training circuit that is not connected to a patient, with a dialysis nurse or technician as preceptor. The aim is to know the steps well enough to direct and assist, not to replace the nursing staff.",
               "items": [
                   ("States aloud the reason for the disconnect and whether the blood will be returned.", True),
                   ("Stops the blood pump, or confirms that it has stopped.", True),
                   ("Closes the clamps on both needle lines and both blood lines before any connection is opened.", True),
                   ("Puts on gloves, mask, and eye protection before handling the connections.", False),
                   ("Disconnects the blood lines from the needle lines and caps or covers the open ends without touching them.", False),
                   ("Explains how the needles or catheter are secured or flushed after an emergency disconnect, per unit protocol.", False),
                   ("Names the three events in which blood is not returned: air in the line, suspected hemolysis, and a severe dialyzer reaction.", True),
                   ("For manual return, identifies a situation in which it is allowed, such as a power failure with a sound circuit.", True),
                   ("Locates the hand crank and fits it to the blood pump.", False),
                   ("Opens the venous line from the machine&rsquo;s clamp as the manufacturer describes and states that the air detector no longer protects the patient.", True),
                   ("Turns the crank in the marked direction at a slow, steady rate while watching the venous chamber and line for air.", True),
                   ("Stops and clamps the venous line when saline reaches the patient end or as soon as any air is seen.", True),
                   ("Labels and sets aside the lines, dialyzer, and packaging when the event needs investigation.", False),
                   ("Gives a structured report to the preceptor, acting as the attending nephrologist, that includes whether blood was returned.", False),
               ],
               "placement": "During one supervised shift, find the clamps, the hand crank, the emergency cart, and the written protocols for air embolism, hemolysis, anaphylaxis, blood loss, and cluster events. Note any protocol you could not find and tell the charge nurse."},
    "quiz": [
        ("Why is the circuit blood not returned when hemolysis is suspected?",
         ["It has become infected", "It has lost its oxygen",
          "It contains potassium released from broken red cells", "The saline may be contaminated"], 2,
         "Returning it can cause severe hyperkalemia in a patient who cannot excrete potassium."),
        ("Twelve minutes into a first treatment with a new dialyzer, a patient has itching, a hoarse voice, wheeze, and a falling blood pressure. What happens to the blood in the circuit?",
         ["It is not returned. Dialysis stops and the lines are clamped", "It is returned quickly to avoid blood loss",
          "It is returned after an antihistamine", "It is returned at half the pump speed"], 0,
         "This is a severe early (type A) reaction. The circuit blood carries the trigger."),
        ("Why may the venous pressure alarm stay silent when the venous needle comes out?",
         ["The alarm is off during treatment", "The reading falls only by the pressure inside the access, which is often low in a fistula",
          "The arterial pressure rises to compensate", "The air detector takes over"], 1,
         "Tubing and needle resistance remain, so the pressure can stay within the alarm limits."),
        ("Mr. Aquino, 78, has dementia and keeps pulling at his blanket. The machine is quiet. He is now pale and drowsy. What do you do first?",
         ["Order a blood sugar test", "Ask for a lower fluid removal rate",
          "Check the alarm history", "Lift the blanket and look at the access and lines"], 3,
         "A covered access in a restless patient is the usual setting for a dislodged venous needle. A silent machine does not exclude it."),
        ("A patient coughs and becomes breathless, and there is foam below the venous chamber. The pump is stopped and the line clamped. Which position do published reviews advise for venous air embolism?",
         ["Sitting upright", "Lying on the right side", "Lying on the left side", "Prone"], 2,
         "The left lateral position tends to hold air in the right heart. Sitting upright lets air rise toward the brain."),
        ("Why does an opening in the circuit before the blood pump draw air in?",
         ["That segment is under negative pressure because the pump is pulling", "The blood there is warmer",
          "Heparin thins the blood there", "The air detector creates suction"], 0,
         "Pressure there is below atmospheric, so an opening admits air instead of leaking blood."),
        ("Which pair describes a type B dialyzer reaction?",
         ["First minutes; throat swelling and hives", "After treatment ends; fever and chills",
          "First treatment only; seizures", "Later in treatment; chest and back pain, usually mild"], 3,
         "Type B reactions come later and are usually mild. Dangerous causes of chest pain are excluded first."),
        ("Three patients in one shift develop abdominal pain and high blood pressure within 30 minutes. What is the best next step?",
         ["Treat each patient&rsquo;s pain and continue", "Declare a possible cluster event, stop treatments per protocol, and have the water and dialysis fluid checked",
          "Wait for a fourth patient", "Return every patient&rsquo;s blood and send them home"], 1,
         "The same new symptoms in several patients point to a shared cause. Blood is not returned if hemolysis is possible."),
        ("The venous chamber holds a large clot and the dialyzer shows dark streaks. A staff member suggests pushing saline hard to return the blood. What do you advise?",
         ["Agree, to avoid blood loss", "Agree, after extra heparin",
          "Do not return blood through the clotted parts, record the loss, and call the nephrologist", "Return it through the arterial needle"], 2,
         "Clot must never be pushed toward the patient."),
        ("Which part of the water system removes chloramine?",
         ["The carbon tanks", "The reverse osmosis membrane", "The water softener", "The sediment filter"], 0,
         "Chloramine passes through reverse osmosis. Exhausted carbon has led to outbreaks of hemolysis."),
        ("A conductivity alarm returns after each reset and the fluid is in bypass. A staff member proposes overriding it to finish the last hour. What is correct?",
         ["Override it, because the patient needs the time", "Override it and check potassium afterward",
          "Lower the blood flow and override", "Do not override. Call the technician and the nephrologist"], 3,
         "Fluid that is too dilute can break red cells. The bypass is protecting the patient."),
        ("What did investigators find in the 1998 multistate outbreak of hemolysis?",
         ["Bacteria in the water loop", "A lot of blood tubing with a narrowed opening",
          "A heparin overdose", "A reused dialyzer"], 1,
         "The one common factor across three states was a single lot of tubing."),
        ("Ms. Lim has her first dialysis with a very high urea. Near the end she has a headache and becomes confused. The lines and blood look normal. Which statement fits best?",
         ["This is a type A reaction", "This is air embolism",
          "Dialysis disequilibrium is possible. The treatment stops and the nephrologist is called", "It is expected and needs no action"], 2,
         "New neurologic symptoms in a first treatment with a high urea suggest disequilibrium, which is not a circuit fault."),
        ("What does a confirmed blood leak alarm mean?",
         ["The dialyzer membrane has torn", "A needle has come out",
          "The venous chamber is clotted", "The pump segment has split"], 0,
         "The detector sits in the used dialysis fluid. Blood return then follows unit protocol and the nephrologist."),
        ("You cannot tell whether sudden chest pain is hemolysis, a reaction, or cardiac. The pump is stopped and the lines clamped. What is the safest position on blood return?",
         ["Return it at once to preserve hemoglobin", "Do not return it until you have spoken to the nephrologist",
          "Return half of it", "Let the patient decide"], 1,
         "Giving up the circuit blood costs less than returning air, broken cells, or an allergen."),
    ],
    "terms": [("Extracorporeal circuit", "The blood lines and dialyzer outside the body."),
              ("Air embolism", "Air that enters the bloodstream and blocks flow in the heart, lungs, or brain."),
              ("Hemolysis", "Breaking of red blood cells, with release of hemoglobin and potassium."),
              ("Type A dialyzer reaction", "An early, anaphylactic reaction to the dialyzer or its sterilant."),
              ("Type B dialyzer reaction", "A later, usually mild reaction with chest and back pain."),
              ("Venous needle dislodgement", "The return needle comes out of the access while the pump is running."),
              ("Rinse-back", "Returning the blood in the circuit to the patient with saline at the end of treatment."),
              ("Bypass", "The machine diverts dialysis fluid away from the dialyzer because it is out of range."),
              ("Chloramine", "A water disinfectant that damages red cells if it is not removed by carbon."),
              ("Cluster event", "Two or more patients with the same new symptoms in one shift, suggesting a shared cause.")],
    "readings": [("hemodialysis-complications.html", "A wider survey of problems during dialysis, including those outside the circuit."),
                 ("dialysis-water-treatment-systems.html", "How the water system removes chloramine and other contaminants."),
                 ("code-blue-acls-dialysis-unit.html", "What to do when a circuit emergency becomes a cardiac arrest.")],
    "calcs": [],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
