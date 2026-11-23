# -*- coding: utf-8 -*-
"""Physician on Duty, Module 11: Safe to Start, Safe to Go Home.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty greeting a dialysis patient at the weighing scale and looking at how she walks and breathes before her session.",
    "objectives": [
        "Perform a focused three-minute assessment of a patient who is about to start hemodialysis.",
        "Choose among four decisions: start as ordered, start after a call for changes, delay, or transfer to the emergency room.",
        "Recognize the red flags that mean a patient should not be connected in an outpatient unit.",
        "Assess a patient who missed sessions and report the findings before connection.",
        "Confirm serology and isolation status before a patient is connected.",
        "Perform the post-dialysis check and decide whether a patient is safe to go home.",
    ],
    "big": """
{{plain:Think of an inter-island ferry. Before it leaves port, an officer checks the weather, the vessel, and the passengers. At the other end, nobody steps off until the ramp is secure. A dialysis session has the same two gates. You check the patient before the blood leaves the body, and again before the patient leaves the building.}}
<p>The picture has one limit. A ferry that stays in port is safe. A dialysis patient who is not dialyzed is not. The fluid, potassium, and acid that Module 2 described keep building while the patient waits. &ldquo;Do not start&rdquo; is therefore never a complete decision. It must come with a plan for where and when the patient will be dialyzed.</p>
{{cards:Key terms for this module|Pre-dialysis assessment::A short, structured look at the patient before connection.|Clearance note::Your written record of that assessment and of the decision made.|Red flag::A finding that suggests a condition the dialysis unit cannot diagnose or treat safely.|Serology status::Recorded test results for hepatitis B, hepatitis C, and human immunodeficiency virus (HIV), with their dates.|Isolation station::A room or area with a machine used only for patients with hepatitis B infection.|Orthostatic hypotension::A fall in blood pressure on standing, often with dizziness.|Hemostasis::Bleeding from the needle sites has stopped and stays stopped.}}
""",
    "case": {"title": "She walked in breathless.", "html": """
<p>Mrs. Lourdes Villanueva, 64, dialyzes every Tuesday and Friday through a left arm fistula. She has been away for two weeks at a family wake in her home province. She had one session at a center there last Tuesday and missed the Friday session because of the burial. Today is Tuesday. It has been seven days since her last dialysis.</p>
<p>She walks in holding her daughter&rsquo;s arm and stops twice to catch her breath. She speaks in short phrases. She is 5.2 kilograms above her dry weight. Her blood pressure is 190/104 mm Hg, her heart rate is 112 per minute, and her oxygen saturation is 89% on room air. She has no chest pain and no fever.</p>
<p>The charge nurse, Ms. Aquino, says quietly: &ldquo;Doctor, she dialyzed somewhere else last week. We have no record from that center.&rdquo;</p>
""", "questions": ["What do you need to find out in the next three minutes?",
                  "Which of the four decisions fits her: start as ordered, start after a call, delay, or transfer?",
                  "What must be settled about her session in another center before she is connected?"]},
    "sections": [
        ("frame", "Two gates", "Two gates and four possible answers", """
<p>Most patients who arrive for dialysis are well enough to start and, later, to go home. The assessment exists to find the few who are not. It works only when it is done for every patient, in the same order.</p>
<p>Philippine licensing rules expect a physician to be present while a dialysis clinic operates, and they assign nurses to assess patients before, during, and after treatment.[[doh2012]] Professional standards add that the physician on duty evaluates all patients during the tour of duty.[[psn2024]] Read the nurse&rsquo;s assessment before you begin yours.</p>
<p>At the first gate there are four possible answers, not two.</p>
{{cards:Four answers at the first gate|Start as ordered::The patient is in their own usual state. Nothing calls for a change to the prescription.|Start after a call::The patient can be dialyzed here, but something may need to change. The attending nephrologist decides what.|Delay::One question must be answered first, such as an electrocardiogram (ECG), a blood sugar, or a call back. The patient stays under observation.|Transfer::The patient needs diagnosis or treatment that the unit cannot give. Dialysis, if still needed, is arranged in the hospital.}}
{{fig:pod11_trafficlight}}
{{flow:Safe to start?|Look for red flags::Unstable vital signs, chest pain, a new neurologic deficit, active bleeding, or altered consciousness. If present, follow the emergency protocol, call, and prepare to transfer.|Compare with the patient&rsquo;s usual::Weight gain, blood pressure, heart rate, breathing, and temperature, against your unit&rsquo;s limits and this patient&rsquo;s pattern.|Ask about the gap::Missed sessions, dialysis elsewhere, illness, bleeding, falls, and new medicines.|Check the access::A thrill and healthy skin, or a clean catheter exit site.|Confirm the station::Serology status is known, current, and matches the machine.|Decide and write::One of the four answers, with the time.}}
<p>This four-answer structure is a teaching framework built for this series. It does not come from a guideline, and no trial has tested it. Your unit&rsquo;s protocol and the attending nephrologist set the limits between one answer and the next.</p>
{{key:A delay needs a clock. Decide what you are waiting for and for how long. A delay with no end point becomes a missed session.}}
"""),
        ("assess", "Three minutes", "The three-minute assessment", """
<p>A full history and examination takes too long when twelve patients arrive together. A fixed short sequence does not. It moves from what you can see across the room, to the numbers, to your hands.</p>
{{fig:pod11_sequence}}
{{flow:Three minutes, in order|Minute one, look and ask::Watch the patient walk from the scale. Note breathing, color, alertness, and speech. Ask, &ldquo;How have you been since your last session?&rdquo;|Minute two, read the numbers::Weight against the dry weight and the last post-dialysis weight. Blood pressure, heart rate, temperature, and oxygen saturation. Blood sugar in patients with diabetes, as protocol states.|Minute three, examine::Neck veins, lung bases, ankles or sacrum, and the access.|Then decide::Say the decision to the nurse and write the clearance note.}}
<h3>Read the numbers against the patient&rsquo;s own pattern</h3>
<p>Dialysis patients often live with values that would alarm you in anyone else. A single reading tells you little. A reading that departs from that patient&rsquo;s last several sessions tells you a great deal, so open the previous treatment records before you examine.</p>
<h3>What the chest and the ankles cannot tell you</h3>
<p>Listening for crackles and pressing on the ankles are quick, and you should do both. They are also weak tests. In a study of 79 hemodialysis patients with 1,106 paired examinations, crackles and leg edema agreed poorly with lung congestion seen on ultrasound, alone or combined.[[torino2016]] Those patients had heart disease, so the figures may not apply to every unit. The lesson still holds: a clear chest does not rule out fluid in the lungs. Breathlessness, sleeping upright, a large weight gain, and a low oxygen saturation count for more.</p>
<h3>The access</h3>
{{fig:look_listen_feel|Look, listen, and feel. A fistula or graft should have a continuous thrill and no redness, swelling, or discharge.}}
<p>For a fistula or graft, look at the skin and feel for the thrill, the buzzing vibration of blood flowing through the access. For a catheter, look at the exit site and ask about fever or chills. An access with no thrill, or one that looks infected, is not needled until the attending nephrologist has been told. The access plan is part of the prescription.</p>
"""),
        ("redflags", "Red flags", "Red flags that belong in the emergency room", """
<p>An outpatient dialysis unit cannot image a brain, monitor a heart overnight, transfuse rapidly, or support a failing circulation. Connection also adds stress. Blood moves outside the body, fluid is removed, and heparin, a blood thinner, is usually given.[[daugirdas2015]] An unstable patient tolerates this poorly, and heparin can worsen bleeding.</p>
<p>A red flag does not cancel dialysis. It means the outpatient chair is the wrong place to begin. The nephrologist can arrange dialysis in the hospital once the emergency has been assessed.</p>
<div class="table-wrap"><table>
<thead><tr><th>Red flag</th><th>What it may be</th><th>Why not the outpatient chair</th></tr></thead>
<tbody>
<tr><td>Chest pain, or new ECG changes</td><td>Heart attack or a dangerous rhythm</td><td>Needs cardiac monitoring and tests</td></tr>
<tr><td>New weakness, facial droop, slurred speech, or sudden severe headache</td><td>Stroke, including bleeding in the brain</td><td>Needs urgent imaging. Heparin could worsen a bleed</td></tr>
<tr><td>New confusion or drowsiness</td><td>Low blood sugar, infection, stroke, severe uremia (buildup of wastes the kidneys normally clear)</td><td>Check blood sugar per protocol. The cause must be found</td></tr>
<tr><td>Low blood pressure with a fast pulse, cold skin, or fainting</td><td>Sepsis, bleeding, or a heart problem</td><td>Fluid removal would lower the pressure further</td></tr>
<tr><td>Severe breathlessness that does not ease with oxygen and sitting up</td><td>Pulmonary edema, pneumonia, heart attack</td><td>May need airway support. Urgent dialysis is arranged with the nephrologist</td></tr>
<tr><td>Black or bloody stools, vomiting blood, or a bleeding access</td><td>Active bleeding</td><td>Heparin and needling add risk. May need transfusion</td></tr>
<tr><td>Fall with a head injury since the last session</td><td>Bleeding inside the skull</td><td>Symptoms can be delayed. Heparin adds risk</td></tr>
</tbody></table></div>
{{call:Stop and call the attending nephrologist before connection for unstable vital signs, chest pain, a new neurologic deficit, or active bleeding. Begin your unit&rsquo;s emergency protocol while someone else dials. Do not start dialysis while you wait.}}
<h3>Fever in a patient with a catheter</h3>
<p>A dialysis catheter runs from the skin into a large central vein. Bacteria on the skin or in the catheter hub can enter the blood each time it is opened. Fever or chills in a patient with a catheter is therefore treated as a bloodstream infection until shown otherwise.</p>
<p>The reverse does not hold. A prospective study at one large center in the United States followed 305 episodes of suspected infection in catheter-dependent patients. Infection was confirmed in 88%, and catheter-related bloodstream infection made up 69% of confirmed infections. Fever was a presenting symptom in fewer than half of those bloodstream infections.[[alsolaiman2011]] This was a single center, and local patterns may differ. A catheter patient who feels cold or weak without fever still deserves suspicion.</p>
{{call:Call the attending nephrologist for any catheter patient with fever, chills, or a new feeling of being unwell. Follow your unit&rsquo;s protocol for blood cultures. Whether to dialyze, which antibiotic to give, and whether the catheter stays are the nephrologist&rsquo;s decisions.}}
"""),
        ("interval", "Since the last session", "Questions about the days since the last session", """
<p>The patient has lived several days without you. On a twice-weekly schedule the gaps are three and four days long. Most of what makes a session unsafe happened during those days, and patients often do not mention it unless asked.</p>
<div class="table-wrap"><table>
<thead><tr><th>Ask about</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Missed or shortened sessions</td><td>A longer gap means more fluid, potassium, and acid</td></tr>
<tr><td>Dialysis anywhere else</td><td>Serology status and the treatment record need review</td></tr>
<tr><td>Breathlessness, or trouble lying flat</td><td>Early signs of fluid in the lungs</td></tr>
<tr><td>Chest pain, palpitations, or fainting</td><td>Possible heart disease or a rhythm problem</td></tr>
<tr><td>Fever or chills, at home or after the last session</td><td>Access infection can show hours after a session</td></tr>
<tr><td>Bleeding, black stools, falls, or a blow to the head</td><td>Heparin is usually given during dialysis</td></tr>
<tr><td>Vomiting, loose stools, or poor appetite</td><td>The patient may be below dry weight</td></tr>
<tr><td>Admission, procedure, or new medicine</td><td>Bleeding risk, blood pressure, and potassium may have changed</td></tr>
<tr><td>Time needed to feel normal after the last session</td><td>A long recovery suggests the session was hard on the patient</td></tr>
</tbody></table></div>
<p>In an international study of 6,040 patients, one in ten reported needing more than 12 hours to recover from a session. They had a higher risk of hospital admission and death than patients who recovered in 2 to 6 hours.[[rayner2014]] The answer is subjective, and the study cannot show that long recovery causes harm. It is still worth passing to the nephrologist.</p>
{{key:Ask the same questions of every patient at every session. The patient who &ldquo;never has problems&rdquo; is the one whose new problem gets missed.}}
"""),
        ("missed", "Missed sessions", "The patient who missed sessions", """
<p>Module 2 explained why the longest gap of the week is the most dangerous time. A missed session makes that gap longer. On a twice-weekly schedule, one missed session leaves the patient a full week without dialysis.</p>
<h3>What the evidence shows</h3>
<p>Three large observational studies point the same way. In an international cohort, patients who skipped one or more sessions a month had a 30% higher risk of death.[[saran2003]] Among 4,493 patients in countries where missed treatments were common, one or more missed treatments in four months was associated with a higher risk of death (hazard ratio 1.68), sudden death, and hospital admission.[[alsalmi2018]] In records of 182,536 patients in the United States, the odds of admission in the two days after a missed treatment were about four times those after an attended one.[[chan2014]]</p>
<p>These studies have limits. Patients who miss sessions differ in many ways from those who do not. Most were prescribed three sessions a week, so the figures cannot be applied directly to twice-weekly patients in the Philippines. The physiology gives no reason to expect a smaller risk when the usual gap is already longer.</p>
<p>The same studies linked missed sessions to longer travel, symptoms of depression, transport problems, and bad weather.[[alsalmi2018]][[chan2014]] A patient who feels blamed will hide the next missed session. Ask why with interest, and pass the reason to the team.</p>
<h3>What is different today</h3>
{{cards:Three dangers after a missed session|Fluid::More weight gain, and a higher chance of fluid in the lungs.|Potassium::More time to build up. A normal ECG does not exclude a high level.|Acid and uremia::Nausea, drowsiness, or deep rapid breathing.}}
<p>Faced with a large weight gain, it is natural to want all of it removed today. Module 2 showed that fast fluid removal is associated with harm.[[flythe2011]] After several missed sessions the blood urea may be very high. Standard texts advise a gentler session when urea is very high, to lower the risk of dialysis disequilibrium, a brain swelling syndrome.[[daugirdas2015]] That advice comes mainly from patients new to dialysis. How to divide the work across sessions is a prescription decision.</p>
{{flow:Missed-dialysis pathway|Count the days::Days since the last full session, and sessions missed or shortened.|Look for the three dangers::Breathing and oxygen saturation, weakness or palpitations, drowsiness or vomiting.|Test as protocol allows::An ECG and a pre-dialysis blood sample.|Call before connection::Report the days missed, the weight gain, the vital signs, and any results.|Carry out the orders::Fluid goal, time, dialysis fluid, and any extra session are the nephrologist&rsquo;s to set.|Ask why::Share the reason with the nurse and the social worker.|Fix the next date::Confirm the next session before the patient leaves.}}
{{call:Call the attending nephrologist before connecting any patient who missed a session. Treat it as an emergency under your unit&rsquo;s protocol if the patient is breathless at rest, weak, drowsy, or has an abnormal ECG.}}
"""),
        ("isolation", "Serology and isolation", "Serology and isolation status", """
<p>In dialysis, blood leaves the body through tubing handled by staff who move between patients. Small amounts reach gloves, clamps, and machine surfaces, and can carry viruses to the next patient without a visible spill.</p>
<p>Hepatitis B is the main concern because the virus is hardy. The United States Centers for Disease Control and Prevention (CDC) note that it stays viable on surfaces for at least seven days and has been found on clamps, scissors, and machine control knobs in dialysis centers.[[cdc2001]]</p>
{{fig:pod11_isolation}}
<h3>What the guidelines say</h3>
<p>The CDC recommendations state that hepatitis B status should be known before a patient is admitted to a unit, and before a transfer. Patients positive for hepatitis B surface antigen (HBsAg) are dialyzed in a separate room on a dedicated machine. Staff who care for them do not care for susceptible patients at the same time.[[cdc2001]] Philippine licensing rules require a clinic to assign at least one machine to patients with hepatitis B.[[doh2012]]</p>
<p>For hepatitis C, guidance and common practice differ. The CDC document does not recommend isolation or dedicated machines, and relies on strict infection control for every patient. It also does not recommend routine HIV testing for infection control.[[cdc2001]] The Kidney Disease: Improving Global Outcomes (KDIGO) guideline strongly recommends hepatitis C testing at the start of in-center dialysis and on transfer.[[gordon2019]] Some units assign separate machines for hepatitis C by local policy. Follow your unit&rsquo;s policy, which may be stricter than these documents.</p>
<p>These recommendations rest largely on outbreak investigations and expert consensus, and the CDC document dates from 2001. Module 29 covers infection control in depth.</p>
<h3>Your check before connection</h3>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>Confirm</th><th>If it is not clear</th></tr></thead>
<tbody>
<tr><td>Regular patient</td><td>Results are on file and current under unit policy. The station matches</td><td>Tell the charge nurse</td></tr>
<tr><td>New patient or transfer</td><td>Dated results from the referring unit are in the chart</td><td>Do not assume a negative result. Call the nephrologist and follow unit policy</td></tr>
<tr><td>Returning after dialysis elsewhere</td><td>Where, how many sessions, and whether a record came back</td><td>Unit policy decides the station and retesting</td></tr>
<tr><td>Sent from a ward or emergency room</td><td>Status is written in the referral</td><td>Treat as unknown under unit policy</td></tr>
</tbody></table></div>
<p>The charge nurse assigns stations and usually knows each patient&rsquo;s status. Your task is to confirm that the question was asked and answered before connection. Discuss results quietly, as Module 1 advised.</p>
{{key:Unknown is not the same as negative. A patient with no result on file is managed under your unit&rsquo;s policy for unknown status until the result arrives.}}
"""),
        ("discharge", "Going home", "Safe to go home: the post-dialysis check", """
<p>The end of a session is not the end of the risk. The patient may have lost several liters in a few hours. Module 2 explained plasma refilling. Refilling continues after the machine stops, so blood volume is still low when the patient stands.</p>
<p>Standing adds a second stress. Blood pools in the legs, and the body normally responds by tightening vessels and raising the heart rate. Many dialysis patients respond weakly because of diabetic nerve damage, blood pressure medicines, or age.[[daugirdas2015]] The result is orthostatic hypotension, often in the hallway or on the ride home.</p>
{{fig:pod11_standing}}
<p>The evidence is limited but points one way. In 1,244 patients at 28 Japanese dialysis centers, a larger fall in systolic pressure on standing soon after dialysis was associated with a higher risk of death over two years. The routine readings taken before and after the session were not.[[shoji2004]] The study was observational and does not show that preventing the fall saves lives. It suggests that the standing reading carries information the routine readings lack.</p>
{{flow:Safe to go home?|Review the session::Time completed, fluid removed against the goal, and any event.|Ask about symptoms::Dizziness, chest pain, breathlessness, cramps, headache, or chills.|Measure seated, then standing::Blood pressure and heart rate, as your unit&rsquo;s protocol describes. Stay beside the patient.|Check the access::Needle sites are dry and the thrill is present. A catheter is capped, clamped, and dressed.|Weigh::Compare the post-dialysis weight with the dry weight.|Watch the walk::The patient walks steadily and speaks normally.|Confirm the plan::Who takes the patient home, the next session date, and reasons to return early.}}
<h3>The access before the patient leaves</h3>
<p>Bleeding from a needle site normally stops within minutes of steady pressure that is not hard enough to stop the thrill. The vascular access guideline of the Kidney Disease Outcomes Quality Initiative (KDOQI) lists bleeding from the needle sites that lasts longer than usual for that patient, at three sessions in a row, among the clinical signs that an access may be narrowing.[[lok2020]] One long bleed can also reflect heparin or poor pressing technique. A pattern over several sessions should reach the nephrologist.</p>
<div class="table-wrap"><table>
<thead><tr><th>Finding after dialysis</th><th>What it may mean</th><th>What to do</th></tr></thead>
<tbody>
<tr><td>Pressure falls on standing, with dizziness</td><td>Too much fluid removed, dry weight too low, medicine effect</td><td>Lay the patient down. Follow the hypotension protocol and call</td></tr>
<tr><td>Weight well above target</td><td>Goal not reached, or session cut short</td><td>Reweigh. Check breathing. Report, since an extra session may be considered</td></tr>
<tr><td>Weight below target</td><td>More fluid removed than planned, or true weight loss</td><td>Check standing pressure. Report for dry weight review</td></tr>
<tr><td>Needle site still bleeding</td><td>Heparin effect, technique, or high pressure in the access</td><td>Reapply pressure per protocol. Keep the patient until dry. Call if the bleeding does not stop or returns</td></tr>
<tr><td>No thrill after the needles are out</td><td>The access may be clotting</td><td>Call the nephrologist now</td></tr>
<tr><td>Chills or fever</td><td>Bloodstream infection, above all with a catheter</td><td>Cultures per protocol and call</td></tr>
<tr><td>Chest pain, confusion, or a new neurologic sign</td><td>Heart attack, stroke, or low blood sugar</td><td>Emergency protocol, call, and prepare to transfer</td></tr>
</tbody></table></div>
{{call:Do not send home a patient who is dizzy on standing, still bleeding, feverish, confused, or in pain. Keep the patient in the unit, follow your protocol, and call the attending nephrologist. The decision to transfer is made together.}}
"""),
    ],
    "debrief": ["""
<p><strong>What to find out in three minutes.</strong> Mrs. Villanueva told you a great deal by walking in. She stops to breathe and speaks in phrases, and her numbers agree. Sit her upright and give oxygen as your protocol allows while you continue. Ask about chest pain, palpitations, and fever, and examine her. Seven days without dialysis also gives potassium and acid time to build, so obtain an ECG and a blood sample if your protocol provides for them. A heart attack or pneumonia can look like fluid overload at the door.</p>
<p><strong>Which of the four decisions.</strong> She cannot start as ordered, and she cannot be sent home, because dialysis is the treatment for her fluid and potassium. The choice lies between starting here after a call and transferring. If she settles with oxygen, has no chest pain, and her ECG shows no new change, the nephrologist may ask you to start promptly with orders for today. If she stays breathless at rest, or has chest pain or an abnormal ECG, she needs the emergency room, and the nephrologist arranges dialysis there. Either way, the call comes before the needles. The fluid goal and time for a 5.2-kilogram gain are the nephrologist&rsquo;s to set.</p>
<p><strong>The session in another center.</strong> Ms. Aquino raised the right point. A patient who dialyzed elsewhere returns with two unknowns: what was done there, and whether her serology status is still what your records say. Ask the daughter for any record from that center, tell the nephrologist, and follow your unit&rsquo;s policy on the station and on retesting. Units differ on this, and the practice rests on infection control principles, not trial evidence. It should not hold up emergency care.</p>
<p><strong>At the end of the day.</strong> If she is dialyzed in your unit, she should leave breathing more easily, steady on standing, with dry needle sites, a thrill, and her next session fixed. Ask what would have made Friday possible. A burial in the province is a reason, not a fault.</p>
"""],
    "skills": {"title": "Pre-dialysis clearance note and post-dialysis discharge check",
               "intro": "Complete both parts on three patients in one shift while your preceptor observes. Write each note in the patient&rsquo;s record.",
               "items": [
                   ("Reads the nurse&rsquo;s pre-dialysis assessment and the last three treatment records before seeing the patient.", False),
                   ("Watches the patient walk and speak, and asks about the days since the last session, including missed sessions and dialysis elsewhere.", True),
                   ("Compares weight, blood pressure, heart rate, temperature, and oxygen saturation with the patient&rsquo;s own usual values.", True),
                   ("Examines neck veins, lung bases, and ankles or sacrum.", False),
                   ("Examines the access: thrill and skin for a fistula or graft, exit site for a catheter.", True),
                   ("Confirms that serology results are on file and current, and that the assigned station matches.", True),
                   ("States one of four decisions aloud to the nurse: start as ordered, start after a call, delay, or transfer.", True),
                   ("Writes a clearance note with the findings, the decision, the time, and any call made with the orders received.", True),
                   ("After dialysis, reviews time completed, fluid removed against the goal, and events during the session.", False),
                   ("Asks about dizziness, chest pain, breathlessness, cramps, and chills before the patient stands.", False),
                   ("Measures blood pressure and heart rate seated and then standing, staying beside the patient.", True),
                   ("Confirms that needle sites are dry and the thrill is present, or that the catheter is capped and dressed.", True),
                   ("Compares the post-dialysis weight with the dry weight and reports a clear mismatch.", False),
                   ("Confirms who is taking the patient home, the next session date, and the reasons to return early, and writes the discharge note.", False),
               ],
               "placement": "During your first week, keep a list of every patient you did not start as ordered. For each one, note which of the four decisions you made, what the attending nephrologist advised, and what you would do the same way next time."},
    "quiz": [
        ("Why is &ldquo;do not start&rdquo; never a complete decision for a dialysis patient?",
         ["The unit loses the treatment slot",
          "The nurse must agree first",
          "Fluid, potassium, and acid keep building, so a plan for where and when to dialyze is still needed",
          "Every patient must be dialyzed in the outpatient unit"], 2,
         "Not dialyzing carries its own risk."),
        ("Mr. Ramos has a catheter. His blood pressure is far below that of his last six sessions, and he has felt cold and weak since yesterday. He has no fever. What fits best?",
         ["Start as ordered",
          "Delay, examine him, follow protocol, and call the attending nephrologist before connection",
          "Send him home to rest",
          "Start and remove less fluid on your own decision"], 1,
         "Fever is often absent in catheter bloodstream infection."),
        ("What is the purpose of the first minute of the three-minute sequence?",
         ["To observe how the patient walks, breathes, and speaks, and to ask how they have been",
          "To write the clearance note",
          "To check the machine settings",
          "To measure the standing blood pressure"], 0,
         "Walking, breathing, alertness, and speech give the fastest information."),
        ("A patient is 4 kilograms above dry weight and sleeps sitting up. Her chest is clear and her ankles are not swollen. What does the evidence suggest?",
         ["She is not overloaded",
          "Crackles and edema reflect lung congestion reliably",
          "Lung ultrasound is required before every session",
          "A normal examination does not exclude overload"], 3,
         "In 1,106 paired examinations, crackles and edema agreed poorly with lung congestion on ultrasound."),
        ("Mrs. Bautista arrives for dialysis. Her speech has been slurred since breakfast and her right hand is clumsy. Vital signs are at her usual values. What is the best decision?",
         ["Start as ordered",
          "Start without heparin on your own decision",
          "Do not connect, follow the emergency protocol, call the attending nephrologist, and prepare to transfer",
          "Delay for two hours and reassess"], 2,
         "A new neurologic deficit needs urgent imaging, and heparin could worsen a brain bleed."),
        ("Why is the outpatient dialysis chair the wrong place to begin for a patient with active bleeding?",
         ["Dialysis raises the platelet count",
          "The machine cannot run when hemoglobin is low",
          "Bleeding always stops during dialysis",
          "Heparin can worsen bleeding, and the unit cannot transfuse rapidly or treat the source"], 3,
         "The circuit usually needs a blood thinner."),
        ("In the study of suspected infection in catheter-dependent patients, what was found about fever?",
         ["It was present in nearly every bloodstream infection",
          "It was a presenting symptom in fewer than half of catheter-related bloodstream infections",
          "It was never present",
          "It was more common with fistulas"], 1,
         "Fever was a presenting symptom in 47%, so its absence does not exclude infection."),
        ("Which question bears most directly on the safety of heparin today?",
         ["Any bleeding, black stools, falls, or a blow to the head",
          "Any salty food",
          "Any dialysis elsewhere",
          "Time to recover after the last session"], 0,
         "Heparin can worsen any bleeding, including a slow bleed inside the skull after a fall. Report these answers before connection. The nephrologist decides the heparin plan."),
        ("What do the large studies of missed dialysis sessions show?",
         ["Randomized trials prove that one missed session causes death",
          "Missed sessions have no association with outcomes",
          "Missed sessions are associated with more deaths and admissions, with possible confounding",
          "The risk applies only to twice-weekly patients"], 2,
         "The studies were observational, and most patients were on three sessions a week."),
        ("Mr. Santiago missed his last session and arrives 6 kilograms above dry weight, comfortable at rest. The nurse suggests removing all of it today. What is the best response?",
         ["Agree, because the full gain must come off in one session",
          "Refuse dialysis until he promises not to miss again",
          "Halve the goal on your own decision and start",
          "Assess him, test as protocol allows, and call the attending nephrologist, who sets the fluid goal and time"], 3,
         "Fast fluid removal is associated with harm. Dividing the work across sessions is a prescription decision."),
        ("A patient admits he skipped a session because he had no fare. Which response serves him best?",
         ["Warn him that he may lose his slot",
          "Thank him, explain the risk, and share the reason with the team so help can be arranged",
          "Record &ldquo;non-compliant&rdquo; and move on",
          "Tell him to borrow money next time"], 1,
         "Patients who feel blamed hide missed sessions."),
        ("Under the CDC recommendations, how is a patient positive for hepatitis B surface antigen dialyzed?",
         ["At any station, with gloves changed between patients",
          "Only in an intensive care unit",
          "In a separate room on a dedicated machine, by staff not caring for susceptible patients at the same time",
          "At a general station on the last shift"], 2,
         "Hepatitis B survives on surfaces for at least seven days."),
        ("A patient transfers to your unit this morning with no hepatitis B result in the chart. He says, &ldquo;I am negative.&rdquo; What should you do?",
         ["Treat the status as unknown, tell the charge nurse, call the attending nephrologist, and follow unit policy",
          "Accept his word and use a general station",
          "Assign the isolation machine permanently",
          "Cancel dialysis until next week"], 0,
         "Unknown is not the same as negative."),
        ("After dialysis, Mrs. Cruz has her usual seated blood pressure. On standing she is dizzy and her pressure falls. What is the best next step?",
         ["Discharge her, since the seated pressure is normal",
          "Ask her relative to hold her arm",
          "Lower her dry weight yourself",
          "Lay her down, follow the hypotension protocol, call the attending nephrologist, and keep her until stable"], 3,
         "The fall on standing shows she cannot yet compensate for the fluid removed, so she is not safe to walk. Dry weight review belongs to the nephrologist."),
        ("A patient&rsquo;s needle sites have bled longer than usual at three sessions in a row. Why should the nephrologist be told?",
         ["It proves the heparin order is wrong",
          "A pattern of prolonged bleeding is one clinical sign that the access may be narrowing",
          "It means the fistula is infected",
          "It is expected in every fistula"], 1,
         "The KDOQI guideline lists it among the clinical signs of a failing access. Other causes exist."),
    ],
    "terms": [("Pre-dialysis assessment", "A short, structured look at the patient before connection."),
              ("Clearance note", "The written record of the pre-dialysis assessment and the decision made."),
              ("Red flag", "A finding that suggests a condition the dialysis unit cannot diagnose or treat safely."),
              ("Missed session", "A scheduled dialysis treatment that did not take place."),
              ("Serology status", "Recorded results for hepatitis B, hepatitis C, and HIV, with their dates."),
              ("HBsAg", "Hepatitis B surface antigen. A positive result usually means current hepatitis B infection."),
              ("Isolation station", "A room or area with a machine used only for patients with hepatitis B infection."),
              ("Orthostatic hypotension", "A fall in blood pressure on standing, often with dizziness."),
              ("Hemostasis", "Bleeding from the needle sites has stopped and stays stopped."),
              ("Dialysis disequilibrium", "Headache, nausea, or confusion from brain swelling when a very high urea is lowered quickly.")],
    "readings": [("hemodialysis-complications.html", "What can go wrong during and after a session, in more detail."),
                 ("dialysis-access-care.html", "How to examine and protect a fistula, graft, or catheter."),
                 ("dry-weight-determination.html", "How the dry weight is judged, for when the post-dialysis weight does not fit.")],
    "calcs": ["calc-ufr-ceiling.html", "calc-idwg-fluid.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
