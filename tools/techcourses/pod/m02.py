# -*- coding: utf-8 -*-
"""Physician on Duty, Module 02: Life Without Kidney Function I: Water, Salt, Potassium, and Acid.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician checking a dialysis patient's ankles for swelling before a session.",
    "objectives": [
        "Describe, with rough numbers, what healthy kidneys remove from the body each day.",
        "Explain what builds up between dialysis sessions and where in the body it goes.",
        "Predict what an intravenous fluid bolus does in a patient who makes no urine.",
        "Explain why potassium rises, what moves it into and out of cells, and why the electrocardiogram can be falsely reassuring.",
        "Explain why acid builds up and how dialysis corrects it.",
        "Explain why the longest gap between sessions is the most dangerous time of the week.",
    ],
    "big": """
{{plain:Picture a house where the tap runs a little all day and the drain is closed. Nothing flows out until someone opens the drain for four hours, two or three times a week. Between those times, everything that comes in stays in. A patient without kidney function lives in that house. Water, salt, potassium, and acid from every meal and every drink wait in the body for the next dialysis session.}}
{{fig:pod02_drain}}
<p>The picture is useful, and it has one limit. The body is not a single tank. Water, salt, and potassium sit in different compartments and move between them at different speeds. Most of this module is about those compartments, because they explain why treatment that is right for other patients can harm this one.</p>
{{cards:Key terms for this module|End-stage kidney disease (ESKD)::Kidney failure that needs dialysis or a transplant to sustain life.|Anuric::Making almost no urine, usually less than about 100 milliliters a day.|Residual kidney function::The urine and waste removal that failed kidneys still manage. Many patients keep some for months or years.|Interdialytic weight gain::Weight gained between two sessions. Nearly all of it is water.|Extracellular fluid::Water outside the cells: in the blood and between the cells.|Ultrafiltration::Removal of water from the blood by pressure across the dialyzer membrane.|Hyperkalemia::A blood potassium level above the normal range.|Metabolic acidosis::A fall in blood bicarbonate because acid has built up.}}
""",
    "case": {"title": "One liter, fast", "html": """
<p>Mr. Dela Cruz, 58, has had no urine output for two years. He comes to the emergency room on a Sunday night with vomiting and loose stools since the morning. His blood pressure is 88/50 mm Hg and his heart rate is 110 per minute. His last dialysis was on Friday and his next is on Monday.</p>
<p>The emergency room physician, who rarely sees dialysis patients, orders what works for gastroenteritis in anyone else: one liter of intravenous saline, given fast, then a second liter, and a maintenance drip overnight. By morning his blood pressure is 150/95, he cannot lie flat, and his oxygen saturation is 86%. He arrives at your unit by wheelchair for his Monday session.</p>
""", "questions": ["Was any intravenous fluid appropriate on Sunday night?",
                  "Where did the two liters and the overnight drip go?",
                  "What would you have ordered instead, and what would you watch?"]},
    "sections": [
        ("normal", "Healthy kidneys", "What healthy kidneys do every day", """
<p>To understand what is missing, start with what is normal. Two healthy kidneys filter about 180 liters of fluid from the blood every day, roughly 125 milliliters a minute. They take back about 99% of it and send out 1 to 2 liters as urine.[[hall2021]] That urine carries exactly what the body does not need that day.</p>
{{fig:nephron|The nephron is the kidney&rsquo;s working unit. Each kidney has about a million. It filters at the top, then takes back what the body needs and adds what must leave.}}
<div class="table-wrap"><table>
<thead><tr><th>What comes in each day</th><th>What healthy kidneys do</th><th>With no kidney function</th></tr></thead>
<tbody>
<tr><td>Water from drinks and food</td><td>Pass more or less urine to keep body water steady</td><td>Stays. Only sweat, breath, and stool remove water, about half a liter to a liter a day</td></tr>
<tr><td>Salt (sodium chloride)</td><td>Excrete the day&rsquo;s intake</td><td>Stays, and holds water with it</td></tr>
<tr><td>Potassium from food</td><td>Excrete about 90% of the day&rsquo;s intake; the gut removes the rest</td><td>Stays. The gut removes somewhat more than before, but not enough</td></tr>
<tr><td>Acid from the breakdown of protein</td><td>Excrete the acid and rebuild bicarbonate</td><td>Stays, and uses up bicarbonate</td></tr>
<tr><td>Urea and other wastes</td><td>Filter and excrete</td><td>Stay</td></tr>
</tbody></table></div>
<p>The kidneys do this work continuously, 168 hours a week. Standard hemodialysis (HD) does it for about 12 hours a week, or 8 hours on a twice-weekly schedule.[[daugirdas2015]] The body spends the rest of the week storing what it cannot remove.</p>
<p>The gut and the skin help a little. In kidney failure the large bowel secretes more potassium than usual, which is one reason constipation can raise the blood potassium in a dialysis patient.[[palmer2016]] These routes cannot replace the kidneys.</p>
{{key:Ask every patient: &ldquo;How much urine do you still pass in a day?&rdquo; A patient who passes a liter a day and one who passes none are different patients, and the answer changes how much fluid and potassium each can handle.}}
<p>Some patients keep useful urine output for months or years after starting dialysis. In a study of 6,538 patients who started hemodialysis, those who lost this residual kidney function faster during the first year were more likely to die in the years that followed.[[obi2016]] This was an observational study, so it shows an association and does not prove that preserving urine output prolongs life. It is still a good reason to protect what function remains. Module 3 covers how.</p>
"""),
        ("water", "Water and salt", "Water and salt: the closed drain", """
<p>Salt and water travel together. When a patient eats salt, the sodium level in the blood rises slightly, the patient becomes thirsty, and drinks until the sodium is back to normal. The body then holds that salt and water together as extra fluid. Normal body fluid contains about 9 grams of salt per liter, so 9 grams of salt, less than two teaspoons, is held with about one liter of water.[[hall2021]]</p>
{{fig:pod02_salt}}
<p>This is why advice to &ldquo;drink less&rdquo; fails when it is given alone. A patient who eats salty food will be thirsty and will drink. Cutting salt reduces thirst, and less thirst means less weight gain.[[kdigo_bpvol2020]]</p>
<p>Where does the fluid go? It stays outside the cells, in the extracellular fluid. About a quarter of that is in the blood vessels and the rest lies between the cells of the tissues.</p>
{{fig:two_compartment|Fluid gained between sessions collects outside the cells: partly in the blood vessels, mostly in the tissues.}}
{{flow:What extra salt and water do|Vessels fill::Blood volume rises and blood pressure climbs.|Heart stretches::The heart works against more volume and more pressure.|Tissues swell::Fluid collects in the legs, the back, and around the eyes.|Lungs flood::Fluid enters the air spaces and the patient becomes breathless.}}
<p>Edema in the legs appears only after several liters have collected, so a patient can be badly overloaded with normal-looking ankles. Breathlessness on lying flat, a raised blood pressure, and the weight gain itself are earlier signs.</p>
<p>Large weight gains matter beyond the day they occur. In a study of more than 34,000 patients on hemodialysis in the United States, those who gained 4 kilograms or more between sessions had a higher risk of cardiovascular death than those who gained 1.5 to 2 kilograms, after adjustment for other factors (hazard ratio 1.25).[[kalantar2009]] The study was observational. Sicker patients may gain more, so it does not prove that weight gain alone caused the deaths.</p>
<h3>Why the fluid cannot simply be pulled off fast</h3>
<p>Dialysis removes water from the blood, and the blood holds only about 3 liters of plasma. To remove 3 or 4 liters in one session, the tissues must refill the blood vessels as fast as the machine empties them. This is called plasma refilling. When the machine removes fluid faster than the tissues can give it back, blood volume drops and so does blood pressure.[[daugirdas2015]]</p>
{{formula:<strong>Fluid removal rate</strong> = fluid to remove (mL) &divide; treatment time (hours) &divide; body weight (kg)<br>Illustration: 3,000 mL over 4 hours in a 60-kg patient = 12.5 mL per kg per hour. The same 3,000 mL over 3 hours = 16.7 mL per kg per hour.}}
<p>Faster removal is associated with harm. In an analysis of 1,846 patients from the Hemodialysis (HEMO) Study, removal rates above 13 mL per kg per hour were associated with a higher risk of death than rates up to 10 mL per kg per hour (adjusted hazard ratio 1.59).[[flythe2011]] This was also an observational analysis. No randomized trial has tested a specific limit, and KDIGO conference participants described fluid management as a balance between leaving fluid behind and removing it too fast.[[kdigo_bpvol2020]] Your unit&rsquo;s protocol sets the limit you work with.</p>
{{call:Call the attending nephrologist when the fluid goal cannot be reached at a safe rate in the time booked. The choices, such as a longer session, an extra session, or a smaller goal today, belong to the prescription.}}
"""),
        ("bolus", "Intravenous fluid", "What an intravenous fluid bolus does here", """
<p>In most patients, intravenous fluid is forgiving. If you give a little too much, the kidneys pass it within hours. In a patient who makes no urine, every milliliter stays until the next dialysis session. The fluid first expands the blood volume, then spreads into the tissues, and when the tissues are full it enters the lungs.</p>
<div class="table-wrap"><table>
<thead><tr><th>Common order</th><th>In a patient with working kidneys</th><th>In a patient who makes no urine</th></tr></thead>
<tbody>
<tr><td>One liter of saline, given fast</td><td>Raises blood volume; excess is passed as urine</td><td>All of it stays. Useful only if the patient is truly volume depleted, and then in small measured amounts</td></tr>
<tr><td>Maintenance drip</td><td>Replaces what the kidneys pass</td><td>There is nothing to replace. A drip left running overnight can cause pulmonary edema</td></tr>
<tr><td>&ldquo;Keep vein open&rdquo; line</td><td>Harmless</td><td>Adds up over hours. Use a capped cannula instead</td></tr>
<tr><td>Medicines diluted in large bags</td><td>Harmless</td><td>Ask the pharmacist for the smallest safe volume</td></tr>
<tr><td>Fluids that contain potassium</td><td>The kidneys excrete the potassium</td><td>The potassium stays as well</td></tr>
<tr><td>Blood transfusion</td><td>Volume is tolerated</td><td>Best given during dialysis, so the volume and potassium can be removed</td></tr>
</tbody></table></div>
<p>This does not mean that a dialysis patient never needs fluid. A patient with vomiting, diarrhea, bleeding, or sepsis can be truly short of volume, and a patient whose blood pressure falls during dialysis may need fluid returned. The difference is in how you give it.</p>
{{flow:Giving fluid to a patient who makes no urine|Confirm the need::Is the patient below dry weight, with a history of losses? Or is the low pressure from the heart, infection, or bleeding?|Give a small, measured amount::Use the volume in your unit&rsquo;s protocol, not a general ward bolus.|Reassess::Blood pressure, heart rate, breathing, and oxygen saturation after each amount.|Stop when the pressure recovers::Do not continue to a fixed total.|Record the volume::The dialysis team needs to know how much to remove.|Tell the nephrologist::The next session may need to change.}}
{{key:Before you sign any fluid order for a dialysis patient, ask: &ldquo;Where will this fluid be tomorrow?&rdquo; If the answer is &ldquo;still inside the patient,&rdquo; give less, give it slower, and look again.}}
"""),
        ("potassium", "Potassium", "Potassium: a small pool with large effects", """
<p>Potassium is the body&rsquo;s main mineral inside cells. About 98% of it is inside cells, mostly in muscle. Only about 2% is in the fluid outside cells, and that small amount is what a blood test measures.[[palmer2016]] The steep difference between the inside and the outside sets the electrical charge across every nerve and heart muscle cell.</p>
{{fig:pod02_potassium}}
<p>Two consequences follow. First, a small shift of potassium out of cells produces a large rise in the blood. Second, the blood level can change within minutes, long before the total amount in the body has changed.</p>
<p>A healthy person handles a meal rich in potassium in two steps. Within minutes, insulin released by the meal pushes potassium into cells, which blunts the rise in the blood. Over the next hours, the kidneys excrete the load.[[palmer2016]] A patient without kidney function still has the first step and has lost the second. The potassium waits inside cells until dialysis.</p>
<div class="table-wrap"><table>
<thead><tr><th>Moves potassium into cells (lowers blood level)</th><th>Moves potassium out of cells (raises blood level)</th></tr></thead>
<tbody>
<tr><td>Insulin</td><td>Lack of insulin, as in fasting or uncontrolled diabetes</td></tr>
<tr><td>Adrenaline-like stimulation (beta-2 receptors), including salbutamol</td><td>Beta-blocking medicines (a modest effect)</td></tr>
<tr><td>A rise in blood bicarbonate</td><td>Acid build-up from kidney failure</td></tr>
<tr><td>&mdash;</td><td>Very high blood sugar, which draws water and potassium out of cells</td></tr>
<tr><td>&mdash;</td><td>Tissue breakdown: crush injury, bleeding into the gut, hemolysis</td></tr>
</tbody></table></div>
<p>These shifts explain several things you will see. A dialysis patient who fasts for a long time can become hyperkalemic without eating any potassium, because insulin is low.[[palmer2016]] The standard emergency treatments for a high potassium, insulin with glucose and inhaled salbutamol, work by moving potassium into cells. They buy time. They do not remove potassium from the body. In a patient without kidney function, only dialysis does that in a useful amount.[[daugirdas2015]]</p>
<h3>Why the electrocardiogram cannot reassure you</h3>
<p>A high potassium slows electrical conduction in the heart and can cause a fatal rhythm. The electrocardiogram (ECG) may show tall, peaked T waves, a wide QRS complex, or a slow rhythm. It may also show nothing. In a review of 90 hospital patients with a potassium of 6.0 mmol/L or more, the investigators found the ECG insensitive for diagnosing hyperkalemia. Changes became more likely as the potassium rose, but no T-wave measurement reliably separated dangerous levels from safe ones, and they advised against using the ECG to guide treatment in stable patients.[[montague2008]]</p>
{{key:A normal ECG does not rule out a dangerous potassium level. An abnormal ECG in a patient who may be hyperkalemic is an emergency.}}
<p>After dialysis the opposite can happen. Dialysis lowers the blood potassium quickly, and potassium then moves back out of cells over the next few hours, so the level rises again. A blood sample taken right after dialysis reads lower than the level the patient will have that evening.[[daugirdas2015]]</p>
{{call:Call the attending nephrologist at once for a patient with a high potassium result, an ECG change, or muscle weakness, and follow your unit&rsquo;s hyperkalemia protocol while you call. The potassium level of the dialysis fluid is part of the prescription.}}
"""),
        ("acid", "Acid", "Acid: the daily load and the buffer", """
<p>Breaking down the protein in food produces acid, roughly one millimole of acid for each kilogram of body weight every day. Healthy kidneys excrete this acid and rebuild the bicarbonate that was used to neutralize it.[[kraut2016]]</p>
<p>Without kidney function, the acid stays. Bicarbonate in the blood neutralizes it and is used up, so the blood bicarbonate falls between sessions. When bicarbonate runs low, bone gives up some of its mineral to help neutralize the acid, and muscle protein is broken down faster.[[kraut2016]] Over years this contributes to weak bone and loss of muscle.</p>
{{flow:Acid across the week|Protein is eaten::The body makes acid every day.|Bicarbonate neutralizes it::Blood bicarbonate falls a little each day.|Bone and muscle help::They give up mineral and protein when bicarbonate is low.|Dialysis reloads the buffer::The dialysis fluid contains bicarbonate, which crosses into the blood.|After dialysis::Bicarbonate is at its highest, then falls again.}}
<p>Dialysis does not remove acid directly. It gives bicarbonate. The dialysis fluid has a higher bicarbonate level than the patient&rsquo;s blood, so bicarbonate moves into the patient during the session.[[daugirdas2015]] The blood bicarbonate is therefore lowest just before a session and highest just after.</p>
<p>Acid and potassium are linked. The kind of acid that builds up in kidney failure pushes potassium out of cells, so a patient who is more acidotic tends to have a higher blood potassium.[[palmer2016]] A low bicarbonate before dialysis is expected. A very low bicarbonate, or a patient who is breathing deeply and fast, is not, and suggests another cause such as infection, diabetic ketoacidosis, or a missed session.</p>
"""),
        ("gap", "The long gap", "The week on dialysis and the long gap", """
<p>Put the three together and a pattern appears. Weight, potassium, acid, and urea climb between sessions and fall during each one. The peaks are highest after the longest gap.</p>
{{fig:pod02_sawtooth}}
{{fig:hd_week|A week on a three-times-a-week schedule. The two-day gap ends with the highest fluid and waste levels of the week.}}
<p>On a three-times-a-week schedule the longest gap is two days. In a study of 32,065 patients in the United States on this schedule, the death rate on the day after the two-day gap was 22.1 per 100 person-years, compared with 18.0 on other days. Hospital admissions for heart failure, heart attack, stroke, and rhythm problems were also more frequent on that day.[[foley2011]] The study was observational, but the pattern fits the physiology: the first session after the long gap meets the highest fluid, potassium, and acid load of the week.</p>
<p>Many patients in the Philippines dialyze twice a week. Their gaps are three and four days long. The study above did not include twice-weekly patients, so its numbers cannot be applied to them directly. The same physiology applies, though, and it is reasonable to expect the longest gap to be the riskiest time for them as well.</p>
{{cards:What this means on the floor|Know the schedule::For each patient, know which session follows the long gap.|Look harder that day::Expect the largest weight gain, the highest potassium, and the lowest bicarbonate.|Ask about the gap::Salt, fluid, fruit, missed medicines, and any illness since the last session.|Missed sessions multiply the risk::A patient who skipped the last session has an even longer gap. See them first.}}
"""),
        ("rules", "The rules that change", "General medicine rules that change in this patient", """
<p>Much of what you learned for other patients assumes that the kidneys will correct small errors. Here they cannot. This table collects the main differences from this module. Later modules add more for medicines, tests, and the heart.</p>
<div class="table-wrap"><table>
<thead><tr><th>Usual rule</th><th>In a patient without kidney function</th><th>Why</th></tr></thead>
<tbody>
<tr><td>&ldquo;Give a fluid bolus for low blood pressure&rdquo;</td><td>Find the cause first; give small measured amounts per protocol</td><td>No urine to remove the excess</td></tr>
<tr><td>&ldquo;Drink plenty of fluids&rdquo;</td><td>Follow the fluid allowance set by the nephrologist</td><td>Intake stays until dialysis</td></tr>
<tr><td>&ldquo;Start a maintenance drip&rdquo;</td><td>Use a capped cannula</td><td>There are no urinary losses to replace</td></tr>
<tr><td>&ldquo;Replace potassium when it is low-normal&rdquo;</td><td>Do not give potassium without the nephrologist</td><td>A small dose can cause a large rise</td></tr>
<tr><td>&ldquo;A banana and coconut water for cramps or diarrhea&rdquo;</td><td>Avoid; both are high in potassium</td><td>The load cannot be excreted</td></tr>
<tr><td>&ldquo;Fast before the procedure&rdquo;</td><td>Keep fasting short and check blood sugar and potassium</td><td>Low insulin lets potassium leave cells</td></tr>
<tr><td>&ldquo;A normal ECG rules out danger&rdquo;</td><td>It does not rule out a high potassium</td><td>The ECG is an insensitive test</td></tr>
<tr><td>&ldquo;A low bicarbonate needs urgent work-up&rdquo;</td><td>A mildly low level before dialysis is expected</td><td>Acid builds up between sessions</td></tr>
<tr><td>&ldquo;A creatinine this high means acute kidney injury&rdquo;</td><td>A high creatinine and urea are this patient&rsquo;s baseline</td><td>Compare with the patient&rsquo;s own previous results</td></tr>
</tbody></table></div>
{{key:For any laboratory result in a dialysis patient, ask two questions before you react. When was the sample taken in relation to dialysis? What is this patient&rsquo;s own usual value?}}
<p>What counts as an acceptable potassium, bicarbonate, or weight gain before dialysis is set by your unit&rsquo;s protocol and the attending nephrologist. Learn those values for your unit before your first shift.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Was any fluid appropriate?</strong> Probably yes, a little. Mr. Dela Cruz had a day of vomiting and diarrhea, a low blood pressure, and a fast heart rate two days after his last session. He may truly have been short of volume. The mistake was not the decision to give fluid. It was the amount, the speed, and the maintenance drip.</p>
<p><strong>Where did it go?</strong> He makes no urine, so all of it stayed. The saline first refilled his blood vessels, which is why his pressure recovered and then overshot. It then spread into his tissues. When they could hold no more, fluid entered his lungs. The overnight drip replaced urinary losses that he does not have.</p>
<p><strong>What would have been better?</strong> A small measured amount of fluid, with his blood pressure, breathing, and oxygen saturation checked after each amount, stopping as soon as the pressure recovered. No maintenance drip. A check of his potassium and blood sugar, since diarrhea, vomiting, and poor intake can move both. A search for other causes of low pressure, including infection and a heart problem. And a telephone call to his nephrologist or the dialysis unit on Sunday night, so that Monday&rsquo;s session could be planned.</p>
<p><strong>And now?</strong> He is in pulmonary edema at your door. Sit him upright, give oxygen, examine him, and call the attending nephrologist for urgent dialysis orders. Record how much fluid he received overnight, because that volume is part of what must be removed.</p>
<p>The emergency room physician did what is right for most patients. Part of your role is to be the person other doctors can call about a dialysis patient before the second liter is hung.</p>
"""],
    "skills": {"title": "Bedside volume assessment",
               "intro": "Perform this assessment on three patients before their sessions while your preceptor observes.",
               "items": [
                   ("Asks how much urine the patient still passes in a day.", True),
                   ("Confirms today&rsquo;s weight, the dry weight, and the weight after the last session, and calculates the gain.", True),
                   ("Asks about breathlessness, breathlessness on lying flat, and how many pillows the patient sleeps on.", False),
                   ("Asks about salt and fluid intake, vomiting, diarrhea, fever, and poor appetite since the last session.", False),
                   ("Measures blood pressure and heart rate, seated, and compares them with the patient&rsquo;s usual values.", True),
                   ("Measures oxygen saturation on room air.", True),
                   ("Looks at the neck veins with the patient at 45 degrees.", False),
                   ("Listens to the lung bases for crackles.", True),
                   ("Checks for edema at the ankles and, in a patient who has been in bed, over the sacrum.", False),
                   ("States a conclusion: overloaded, near dry weight, or below dry weight, with the findings that support it.", True),
                   ("Calculates the fluid removal rate in mL per kg per hour for the planned session and compares it with the unit&rsquo;s limit.", True),
                   ("States what would be reported to the attending nephrologist.", False),
               ],
               "placement": "For one week, note which session follows the long gap for each patient you see, and compare their weight gain and pre-dialysis potassium on that day with their other sessions."},
    "quiz": [
        ("About how much fluid do two healthy kidneys filter each day?",
         ["About 2 liters", "About 20 liters", "About 180 liters", "About 1,800 liters"], 2,
         "The kidneys filter about 180 liters a day and take back about 99%, leaving 1 to 2 liters of urine."),
        ("A patient who makes no urine is given one liter of intravenous saline. Where is that liter six hours later?",
         ["Passed as urine", "Still in the body, in the blood vessels and tissues", "Removed by the liver", "Lost through the skin"], 1,
         "Without urine output, the fluid stays until dialysis removes it."),
        ("Why does telling a patient to &ldquo;drink less&rdquo; often fail when it is the only advice?",
         ["Patients forget", "Salt intake drives thirst, so a patient who eats salty food will drink",
          "Water is not absorbed in kidney failure", "Thirst is not affected by diet"], 1,
         "Salt raises the blood sodium slightly and causes thirst. Cutting salt reduces thirst and weight gain."),
        ("Fluid gained between sessions collects mainly in which compartment?",
         ["Inside the cells", "Outside the cells, in the blood vessels and tissues", "Inside the bones", "Inside the gut"], 1,
         "Salt and water expand the extracellular fluid."),
        ("Why does blood pressure fall when fluid is removed too fast during dialysis?",
         ["The machine cools the blood", "The tissues cannot refill the blood vessels as fast as the machine empties them",
          "Potassium is removed too fast", "The heart stops responding to insulin"], 1,
         "Dialysis takes water from the plasma. If plasma refilling from the tissues cannot keep up, blood volume and pressure fall."),
        ("A 50-kg patient needs 3,000 mL removed in 4 hours. What is the fluid removal rate?",
         ["7.5 mL per kg per hour", "10 mL per kg per hour", "15 mL per kg per hour", "60 mL per kg per hour"], 2,
         "3,000 &divide; 4 &divide; 50 = 15 mL per kg per hour."),
        ("In the analysis of the HEMO Study, fluid removal rates above 13 mL per kg per hour were:",
         ["Proven in a randomized trial to cause death", "Associated with a higher risk of death in an observational analysis",
          "Associated with a lower risk of death", "Not studied"], 1,
         "The association was observational (adjusted hazard ratio 1.59 compared with rates up to 10). No randomized trial has tested a specific limit."),
        ("About what share of the body&rsquo;s potassium is inside cells?",
         ["2%", "25%", "50%", "98%"], 3,
         "About 98% is inside cells. The blood test measures only the small amount outside."),
        ("How do insulin with glucose and inhaled salbutamol lower the blood potassium?",
         ["They remove potassium in the urine", "They move potassium into cells", "They bind potassium in the gut", "They block potassium absorption"], 1,
         "They shift potassium into cells and buy time. In a patient without kidney function, dialysis is what removes it."),
        ("A dialysis patient with possible hyperkalemia has a normal ECG. What does this mean?",
         ["The potassium must be normal", "A dangerous potassium level is not ruled out",
          "Dialysis can be postponed safely", "The blood sample was wrong"], 1,
         "The ECG is an insensitive test. In a review of 90 patients with a potassium of 6.0 mmol/L or more, no ECG measurement reliably identified hyperkalemia."),
        ("A dialysis patient fasts for a long time before a procedure. Which change is most likely?",
         ["Potassium falls because nothing is eaten", "Potassium rises because low insulin lets potassium leave cells",
          "Sodium rises sharply", "Bicarbonate rises"], 1,
         "With little insulin, potassium moves out of cells, and without kidneys it cannot be excreted."),
        ("How does hemodialysis correct metabolic acidosis?",
         ["It filters acid out directly", "Bicarbonate in the dialysis fluid moves into the patient&rsquo;s blood",
          "It raises the breathing rate", "It removes protein"], 1,
         "The dialysis fluid has a higher bicarbonate level than the blood, so bicarbonate crosses into the patient."),
        ("When is the blood bicarbonate of a dialysis patient usually lowest?",
         ["Just after a session", "Just before a session, especially after the long gap", "Midway through a session", "It does not vary"], 1,
         "Acid builds up between sessions and uses up bicarbonate."),
        ("In the study of 32,065 patients dialyzing three times a week, what was found on the day after the two-day gap?",
         ["Fewer deaths than on other days", "A higher death rate and more cardiovascular admissions than on other days",
          "No difference", "Fewer admissions for heart failure"], 1,
         "The death rate was 22.1 compared with 18.0 per 100 person-years on other days."),
        ("A blood sample taken immediately after dialysis shows a low-normal potassium. What should you expect a few hours later?",
         ["A further fall", "A rise, as potassium moves back out of cells", "No change", "A fall in sodium"], 1,
         "Potassium rebounds after dialysis. The immediate post-dialysis level underestimates the level later that day."),
    ],
    "terms": [("Anuric", "Making almost no urine."),
              ("Residual kidney function", "The urine and waste removal that failed kidneys still manage."),
              ("Interdialytic weight gain", "Weight gained between two dialysis sessions, nearly all of it water."),
              ("Extracellular fluid", "Body water outside the cells, in the blood and the tissues."),
              ("Plasma refilling", "Movement of fluid from the tissues back into the blood vessels during dialysis."),
              ("Ultrafiltration", "Removal of water from the blood by pressure across the dialyzer membrane."),
              ("Hyperkalemia", "A blood potassium level above the normal range."),
              ("Metabolic acidosis", "A fall in blood bicarbonate because acid has built up."),
              ("Long interdialytic gap", "The longest interval between sessions in the patient&rsquo;s weekly schedule."),
              ("Hazard ratio", "A comparison of how often an event happens in two groups over time. A ratio above 1 means more events in the first group.")],
    "readings": [("fluid-management-dialysis.html", "Practical fluid advice for patients between sessions."),
                 ("dry-weight-determination.html", "How dry weight is judged and adjusted."),
                 ("kidney-functions.html", "What the kidneys do, in more detail.")],
    "calcs": ["calc-ufr-ceiling.html", "calc-idwg-fluid.html"],
}

# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
