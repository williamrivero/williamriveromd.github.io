# -*- coding: utf-8 -*-
"""Physician on Duty, Module 13: When the Pressure Falls (intradialytic hypotension).
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty at the chair of a dialysis patient who has been laid back with the legs raised, while a nurse rechecks the blood pressure.",
    "objectives": [
        "Explain why blood pressure falls during dialysis, using plasma refilling, vessel tone, and the response of the heart.",
        "Describe how intradialytic hypotension is defined in the literature and why the definitions differ.",
        "Carry out the stepwise response to a falling pressure in the order your unit&rsquo;s protocol sets.",
        "Separate a volume-related drop from a dangerous cause by timing, accompanying symptoms, and response to first steps.",
        "State when dialysis is stopped and when blood must not be returned to the patient.",
        "List prevention measures to suggest to the attending nephrologist, with the strength of evidence for each.",
    ],
    "big": """
{{plain:Picture a small rooftop tank that supplies a house. A pump draws water out of the tank at a steady rate. A narrow pipe from a much larger cistern refills it, but slowly. If the pump is faster than the pipe, the tank level falls and the taps run weak. During dialysis the blood is the small tank, the tissues are the cistern, and the machine is the pump.}}
<p>The picture has a limit. A tank is passive, and the body is not. When blood volume falls, the vessels tighten and the heart works harder, and the pressure holds. Pressure falls when fluid removal outruns refilling <em>and</em> these active defenses fail.</p>
{{cards:Key terms for this module|Intradialytic hypotension (IDH)::A fall in blood pressure during a dialysis session. Published definitions differ.|Nadir pressure::The lowest systolic pressure recorded during a session.|Plasma refilling::Movement of fluid from the tissues back into the blood vessels as the machine removes water.|Vascular tone::The degree of tightening in the walls of small arteries and veins.|Autonomic neuropathy::Damage to the nerves that control heart rate and vessel tone. It is common in diabetes and in kidney failure.|Myocardial stunning::A temporary fall in the pumping of a segment of heart muscle after its blood supply has been reduced.|Ultrafiltration (UF)::Removal of water from the blood by pressure across the dialyzer membrane.}}
<p>Most episodes are volume related and recover within minutes. A few are the first sign of something dangerous. Your work is to treat the first kind promptly and to recognize the second kind early.</p>
""",
    "case": {"title": "Hour three", "html": """
<p>Mr. Ernesto Bautista, 64, has had diabetes for twenty years. He dialyzes on Mondays and Thursdays through a left arm fistula. Today is Monday. He arrived 4.4 kilograms above his dry weight of 58 kilograms, and the prescribed session is four hours. He took his amlodipine and carvedilol at six this morning. At hour two his wife brought him rice and fried fish, and he ate all of it.</p>
<p>At hour three, the nurse, Ms. Joy Mercado, calls you to his chair. He is yawning, his calves are cramping, and he says the room is going dim. His blood pressure is 82/48 mm Hg. It was 148/84 at the start. His heart rate is 62 per minute. Ms. Mercado has already laid the chair back and stopped fluid removal, as the unit&rsquo;s protocol allows.</p>
""", "questions": ["What do you do in the next two minutes, and in what order?",
                  "What tells you whether this is a volume-related drop or something more dangerous?",
                  "What will you suggest to the attending nephrologist to prevent the next episode?"]},
    "sections": [
        ("defenses", "Why pressure falls", "Why the pressure falls: three defenses", """
<p>Module 2 explained plasma refilling. The machine removes water only from the blood, and the tissues must refill the vessels. The fluid goal for one session is often about as large as the whole plasma volume.[[reeves2018]] A healthy circulation tolerates this because three defenses act together.[[daugirdas2001]]</p>
{{fig:pod13_defenses}}
<p>First, fluid moves from the tissues into the vessels and replaces part of what the machine removes. Second, the vessels tighten. Third, the heart beats faster and more forcefully.</p>
<p>Veins matter more than most physicians expect, because they hold most of the blood volume. When they tighten, they return blood to the heart. When they relax, blood pools in them and the heart has less to pump.[[daugirdas2001]]</p>
{{fig:two_compartment|Refilling moves fluid from the tissue space into the vessels. It has a speed limit, and the limit differs between patients.}}
<p>A dialysis patient often brings a weakened version of each defense to the chair.</p>
<div class="table-wrap"><table>
<thead><tr><th>Defense</th><th>What weakens it</th><th>What you may notice</th></tr></thead>
<tbody>
<tr><td>Refilling</td><td>A fast fluid removal rate after a large weight gain. A dry weight set too low</td><td>A drop late in the session, with cramps</td></tr>
<tr><td>Vessel tone</td><td>Autonomic neuropathy. Blood pressure medicines taken before the session. A meal during dialysis, which opens the vessels of the gut. A rise in body temperature during the session, which opens the vessels of the skin</td><td>A drop soon after eating. A warm, flushed patient</td></tr>
<tr><td>Heart response</td><td>A thick, stiff left ventricle that needs full filling. A weak ventricle. Coronary artery disease. Valve disease. Medicines that slow the heart</td><td>A pulse that does not rise as the pressure falls</td></tr>
</tbody></table></div>
<p>In some patients the nerve signals that tighten the vessels switch off abruptly when the heart is poorly filled. The pressure and the heart rate then fall together. This reflex withdrawal of sympathetic tone is one proposed explanation for a sudden drop with a slow pulse.[[daugirdas2001]] The practical point is that a normal or slow pulse does not make a low pressure safe.</p>
{{key:At every episode, ask which defense failed: refilling, the vessels, or the heart. The answer points to the cause and to the prevention.}}
"""),
        ("definitions", "Definitions", "How the literature defines it, and how often it happens", """
<p>No single definition of intradialytic hypotension (IDH) is accepted. Studies use a fall from the starting pressure, a lowest (nadir) pressure, symptoms, or the need for an intervention. The European Best Practice Guideline (EBPG) group stated that it could not give an evidence-based definition.[[ebpg2007]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>Definition used</th><th>Comment</th></tr></thead>
<tbody>
<tr><td>EBPG, 2007</td><td>A fall in systolic pressure of 20 mm Hg or more, or in mean arterial pressure of 10 mm Hg or more, with symptoms and a need for nursing intervention[[ebpg2007]]</td><td>Opinion based</td></tr>
<tr><td>Nadir-based definition</td><td>A lowest systolic pressure below 90 mm Hg during the session[[flythe2015]]</td><td>Simple to measure</td></tr>
<tr><td>Kidney Disease: Improving Global Outcomes (KDIGO) conference, 2020</td><td>Any symptomatic fall in systolic pressure, or a nadir below 90 mm Hg, should prompt a review of pressure and volume management[[kdigo_bpvol2020]]</td><td>A conference statement, not a graded recommendation</td></tr>
</tbody></table></div>
<p>Flythe and colleagues compared common definitions in 1,409 patients from the Hemodialysis (HEMO) Study and 10,392 patients from a large dialysis provider. A nadir systolic pressure below 90 mm Hg was the definition most strongly associated with death. In patients who started the session at 160 mm Hg or higher, a nadir below 100 mm Hg carried the strongest association. Definitions built on symptoms or interventions were not associated with death.[[flythe2015]] The analysis was observational and does not show that preventing a low nadir prolongs life.</p>
{{fig:idh|Intradialytic hypotension at a glance: who is at risk, what the patient feels, and the first response.}}
<p>Frequency depends on the definition as well. In a Dutch study of 3,818 sessions, the pressure fell by the EBPG amount in 77.7% of sessions, symptoms occurred in 21.4%, and nurses intervened in 8.5%. The full EBPG definition was met in 6.7%.[[kuipers2016]] A later meta-analysis estimated that about 10% to 12% of sessions are affected.[[kuipers2019]] The KDIGO conference report quotes a range up to half of sessions.[[kdigo_bpvol2020]]</p>
<p>Yawning, nausea, cramps, and dimming vision are the usual early signs, but a patient can reach a low nadir without complaining. The trigger for action in your unit is the one written in your unit&rsquo;s protocol. Learn it before your first shift.</p>
"""),
        ("harm", "Why it matters", "Why a low pressure matters beyond the moment", """
<p>The heart is the best studied. Burton and colleagues performed echocardiography during dialysis in 70 patients. In 64% of them, segments of the left ventricle contracted less well during the session, a finding called myocardial stunning. Age, the volume of fluid removed, intradialytic hypotension, and the troponin level were each associated with it. Patients with stunning had a higher death rate over 12 months.[[burton2009]] In a follow-up of 30 patients with stunning, the resting ejection fraction fell from about 62% to 53% over one year.[[burton2009b]]</p>
{{fig:pod13_stunning}}
<p>These were small observational studies from one center. They do not prove that preventing stunning improves survival.</p>
<p>Larger cohorts point the same way. In records from 39,497 patients in the United States, intradialytic hypotension was associated with death (adjusted hazard ratio 1.07) and with myocardial infarction (1.20).[[stefansson2014]] Sicker patients drop their pressure more easily, so part of this association may reflect the patients and not the episodes.</p>
{{cards:What a low pressure can cost|Heart::Stunning during the session, and a falling ejection fraction over time.|Access::An association with clotting of the fistula or graft.|Dialysis dose::Interrupted sessions deliver less treatment.|Fluid balance::Fluid given back and a missed goal leave the patient overloaded.}}
<p>The KDIGO conference report summarizes the associations with access clotting, a lower dialysis dose, and death.[[kdigo_bpvol2020]]</p>
"""),
        ("response", "The response", "The stepwise response at the chair", """
<p>The first steps restore blood to the heart and stop the loss. Guidelines and textbooks agree on them, although the evidence behind each is modest.[[ebpg2007]][[daugirdas2015]] Nurses usually begin them under the unit&rsquo;s protocol before you arrive. You confirm them, examine the patient, and decide whether this is a simple drop.</p>
{{flow:Hypotension response ladder|Go to the chair::Look at the patient. Check that the patient responds, breathes comfortably, and has a pulse. Ask for help early.|Lay the patient back::Recline the chair flat and raise the legs, as far as the patient&rsquo;s breathing allows. Turn the patient to the side if vomiting.|Stop fluid removal::Ask the nurse to stop ultrafiltration. The blood pump keeps running unless you suspect air, hemolysis, a severe dialyzer reaction, or blood loss from a dislodged needle or open line.|Recheck the pressure::Repeat it now and every few minutes. Count the pulse yourself and note the rhythm.|Give oxygen::As your unit&rsquo;s protocol directs.|Look for a cause::Chest pain, breathlessness, fever, bleeding, the needle sites, the lines, the time into the session, and the fluid removed so far. Ask for a blood sugar check in a patient with diabetes, per protocol.|Give fluid if there is no recovery::Use the fluid and the amount in your unit&rsquo;s protocol, in measured portions, and reassess after each.|Call the attending nephrologist::Report what you found and what was done. Agree on the plan for the rest of the session.}}
{{fig:pod13_position}}
<h3>What the evidence says about each step</h3>
<p>The head-down, legs-up position is recommended on opinion only, with a note that its effect may be limited. It is used because it is quick and carries little risk in a patient who is breathing comfortably. A breathless patient may not tolerate lying flat.[[daugirdas2015]] In the EBPG, stopping ultrafiltration rests on low-level evidence. Isotonic saline is advised for patients who do not respond to those two steps, and hypertonic saline showed no advantage over it. The guideline also advises each center to write a stepwise protocol.[[ebpg2007]]</p>
<h3>Fluid is a treatment with a cost</h3>
<p>Module 2 explained that fluid given to a patient without urine output stays in the body. Give what the protocol allows, stop when the pressure recovers, and record the total. A patient who needs repeated portions does not have a simple drop.</p>
{{fig:cramps|Cramps often accompany a volume-related drop. Stretching the calf helps while the pressure recovers.}}
<h3>After the pressure recovers</h3>
<p>Do not restart fluid removal at the old rate by reflex. The remaining goal, the remaining time, and the dry weight belong to the prescription. Ask the attending nephrologist whether to continue at a lower goal, without fluid removal, or to end the session.</p>
{{call:Stop and call the attending nephrologist at once when the pressure does not recover after the first steps of the protocol, when it falls again after recovering, or when the patient needs more than one portion of fluid. Continue the protocol while you call.}}
"""),
        ("sinister", "Simple or sinister", "Simple drop or dangerous cause", """
<p>Fluid removal explains most episodes. A minority have another cause, and some of those causes kill within minutes to hours. You separate them by timing, by what accompanies the drop, and by the response to first steps.</p>
{{fig:pod13_redflags}}
<div class="table-wrap"><table>
<thead><tr><th>Cause</th><th>Clues at the chair</th><th>First move, while you call</th></tr></thead>
<tbody>
<tr><td>Myocardial infarction or ischemia</td><td>Chest pain or pressure, breathlessness, sweating. Pain may be absent in diabetes</td><td>Electrocardiogram (ECG). Follow the unit&rsquo;s chest pain protocol</td></tr>
<tr><td>Arrhythmia</td><td>A very fast, very slow, or irregular pulse. Palpitations. Fainting</td><td>ECG and cardiac monitor</td></tr>
<tr><td>Bleeding</td><td>A dislodged needle or open line. Blood under the blanket. Black stools. New abdominal or back pain</td><td>Uncover and inspect the access and lines. Stop the blood pump if a needle is out or a line is open. Apply pressure to a bleeding site</td></tr>
<tr><td>Sepsis</td><td>Fever or chills, often with a catheter. Warm skin. Confusion</td><td>Temperature. Follow the unit&rsquo;s fever protocol</td></tr>
<tr><td>Cardiac tamponade</td><td>Low pressure early in several sessions with little fluid removed. Distended neck veins. Faint heart sounds</td><td>Stop fluid removal. Urgent transfer for echocardiography</td></tr>
<tr><td>Air in the circuit</td><td>Sudden cough, chest tightness, or collapse. Air or foam in the venous line. An air detector alarm</td><td>Stop the blood pump and clamp the venous line. Do not return the blood</td></tr>
<tr><td>Hemolysis</td><td>Chest, back, or abdominal pain. Dark or translucent red blood in the venous line. More than one patient affected</td><td>Stop the blood pump and clamp the lines. Do not return the blood</td></tr>
<tr><td>Dialyzer reaction</td><td>Onset in the first minutes. Itching, flushing, wheeze, swelling of the face, back pain</td><td>Stop the blood pump and clamp the lines. Do not return the blood. Follow the unit&rsquo;s reaction protocol</td></tr>
</tbody></table></div>
<p>The clues and first moves in this table follow a standard dialysis text.[[daugirdas2015]] Other modules cover each of these causes in full.</p>
{{flow:Simple or sinister|When did it start::A drop in the first half hour, before much fluid is removed, is unlikely to be from fluid removal alone.|What came with it::Chest pain, breathlessness, altered consciousness, fever, bleeding, wheeze, or pain in the back or abdomen each point away from a simple drop.|What do the pulse and rhythm show::A very fast, very slow, or irregular pulse needs an ECG.|What do the access and the lines show::Check the needle sites, every connection, and the color of the blood in the venous line.|Did it recover::A simple drop improves within minutes of lying back and stopping fluid removal. Failure to recover is a warning sign in itself.|Does the story fit::A large fluid goal, a recent meal, or morning blood pressure tablets support a simple drop.}}
<p>The timing rule comes from physiology and experience, not from a diagnostic study. Use it to raise suspicion and never to dismiss a worrying patient.</p>
{{call:Stop and call the attending nephrologist immediately, and call for help in the unit, when a low pressure comes with chest pain, breathlessness, altered consciousness, fever, bleeding, or an abnormal pulse. Start the unit&rsquo;s emergency protocol while you call. Do not wait to see whether the pressure recovers.}}
{{key:If more than one patient drops at the same time, suspect the dialysis fluid or the water. Tell the charge nurse and the technician, and call the attending nephrologist and the medical director.}}
"""),
        ("prevention", "Prevention", "Prevention: what to suggest to the nephrologist", """
<p>One episode needs treatment. A pattern needs a change in the plan, and the plan belongs to the attending nephrologist. You notice the pattern and suggest options. The KDIGO conference advised that measures that do not use medicines come first: reassess the target weight, reduce the fluid removal rate, and look after the heart.[[kdigo_bpvol2020]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Option to raise</th><th>Why it could help</th><th>Evidence and limits</th></tr></thead>
<tbody>
<tr><td>Reassess the dry weight</td><td>A target set too low dries the patient below their true weight</td><td>Clinical examination is the basis. Guideline opinion[[ebpg2007]]</td></tr>
<tr><td>Less salt and smaller weight gains</td><td>A smaller gain means a slower fluid removal rate</td><td>Higher weight gain is associated with more episodes in cohort data[[stefansson2014]]</td></tr>
<tr><td>Longer or more frequent sessions</td><td>The same fluid is removed over more hours</td><td>Advised by the EBPG on moderate to low evidence[[ebpg2007]]</td></tr>
<tr><td>Cooler dialysis fluid</td><td>Limits the rise in body temperature, so skin vessels stay tight</td><td>Small trials show fewer episodes.[[mustafa2016]] The EBPG advised it for patients with frequent episodes.[[ebpg2007]] A later large trial of center-wide cooling showed no fewer cardiovascular events and no smaller fall in pressure[[mytemp2022]]</td></tr>
<tr><td>No meal during or shortly before dialysis</td><td>A meal opens the vessels of the gut</td><td>Sources disagree. See below</td></tr>
<tr><td>Review the timing of blood pressure medicines</td><td>A dose taken shortly before the session peaks during fluid removal</td><td>The EBPG advises caution and advises against routine withholding.[[ebpg2007]] KDIGO calls the effect of withholding unknown[[kdigo_bpvol2020]]</td></tr>
<tr><td>Cardiac evaluation</td><td>A new drop in a previously stable patient may be a heart problem</td><td>Guideline opinion[[ebpg2007]]</td></tr>
<tr><td>Changes to the dialysis fluid, or a medicine such as midodrine</td><td>These act on refilling and vessel tone</td><td>Each has a trade-off. Midodrine evidence comes from small, short studies[[kdigo_bpvol2020]]</td></tr>
</tbody></table></div>
<h3>Cool dialysis fluid: what the trials do and do not show</h3>
<p>Dialysis tends to raise body temperature, and the skin vessels open to lose heat. Slightly cooler dialysis fluid counters this. A meta-analysis of 26 randomized trials with 484 patients found that cooler fluid reduced the rate of intradialytic hypotension by about 70% and raised mean arterial pressure during the session. The trials were small, some lacked blinding, and none reported long-term outcomes.[[mustafa2016]]</p>
<p>The MyTEMP trial then tested cooling as a policy. It randomized 84 centers in Ontario, Canada, treating 15,413 patients, to dialysis fluid set slightly below each patient&rsquo;s body temperature or to a standard temperature. Over four years, cardiovascular death or admission occurred in 21.4% of patients in the cooler group and 22.4% in the standard group, with an adjusted hazard ratio of 1.00. The mean fall in systolic pressure during sessions did not differ.[[mytemp2022]]</p>
<p>The two results answer different questions. MyTEMP shows that cooling the fluid for every patient in a center does not reduce cardiovascular events. It did not test cooling for the individual patient with frequent episodes, and the mean temperatures achieved in its two groups were close. The temperature setting is part of the prescription.</p>
<h3>Food during dialysis: two sources that disagree</h3>
<p>The EBPG advises that patients with frequent episodes avoid eating during or shortly before dialysis, weighed against nutrition in a malnourished patient.[[ebpg2007]] A later nutrition consensus statement concluded that meals during dialysis should be considered for patients without contraindications, and it names a fall in pressure after eating as a risk.[[kistler2018]] For a patient who drops after a meal, a reasonable suggestion is to move the meal, not to stop the patient from eating.</p>
{{formula:<strong>Arithmetic illustration, not a target.</strong> Fluid removal rate = fluid to remove (mL) &divide; time (hours) &divide; weight (kg).<br>4,400 mL over 4 hours in a 58-kg patient = about 19 mL per kg per hour. The same 4,400 mL over 5 hours = about 15 mL per kg per hour.}}
{{key:When you report an episode, include the weight gain, the fluid removal rate, the time of onset, the last meal, the morning medicines, and the number of recent episodes.}}
"""),
        ("callcard", "Record and call card", "After the episode: record, hand off, and the call card", """
<p>An episode is finished when the patient has left safely, the record shows what happened, and the attending nephrologist knows.</p>
{{cards:Before the patient leaves|Standing pressure::Check the pressure seated and then standing, per protocol. A patient who is dizzy on standing is not ready to go.|Access::Confirm that the needle sites have stopped bleeding, and check the thrill.|Advice::Explain what happened. Ask the patient to report chest pain, breathlessness, or fainting at home.}}
<p>Be exact about the blood. Returning the blood in the circuit gives the patient back volume. It is right when a session ends for a cause in the patient. It is wrong when the blood or the circuit may be the cause.</p>
{{flow:Call card: a falling pressure during dialysis|Recognize::Yawning, nausea, cramps, dim vision, a quiet patient, or a low reading on the monitor. Recheck the pressure and count the pulse yourself.|First 2 minutes::Lay the patient back with the legs raised, as far as breathing allows. Stop fluid removal. Give oxygen per protocol. Check chest pain, breathing, consciousness, temperature, needle sites, and lines.|Stop dialysis?::Not for a simple drop that recovers. Stop the blood pump at once if you suspect air, hemolysis, a severe dialyzer reaction, or blood loss from a dislodged needle or open line. End the session, on the nephrologist&rsquo;s advice, if the pressure does not recover or a dangerous cause is likely.|Return the blood?::Yes, when the session ends for a cause in the patient and the circuit is sound. Do NOT return the blood if it may be hemolyzed, if there is air in the venous line, if a severe dialyzer reaction is suspected, or if the circuit has clotted. Clamp the lines and keep the circuit for inspection.|Call::The attending nephrologist, at once, for no recovery after first steps, a second drop, or any red flag. Use the SBAR format from Module 1. Follow the unit&rsquo;s escalation list if there is no answer.|Write::Time, pressures, pulse, symptoms, fluid removed, steps and response, fluid given, advice received, and the patient&rsquo;s condition on leaving.}}
"""),
    ],
    "debrief": ["""
<p><strong>What do you do in the next two minutes?</strong> Ms. Mercado has already performed the first two steps. You confirm them, then look at Mr. Bautista. He answers you and is breathing comfortably. You recheck the pressure and count his pulse, which is regular. You ask about chest pain and breathlessness, and he has neither. You uncover his arm and check both needle sites and the lines. You ask for oxygen and a blood sugar check under the protocol. If his pressure has not improved on the next reading, the protocol&rsquo;s fluid step follows. You call the attending nephrologist in either case.</p>
<p><strong>Simple or sinister?</strong> Several features fit a volume-related drop. It came in hour three. His fluid removal rate works out to about 19 mL per kg per hour, which is fast. He ate a full meal an hour earlier and took two blood pressure medicines that morning. He has cramps. The pulse of 62 is the feature to respect. Carvedilol and autonomic neuropathy can both hold the pulse down. A slow rate also means that his heart cannot compensate, and it does not exclude a rhythm problem. Diabetes can hide the pain of a heart attack. If he does not recover within minutes, an ECG and an urgent call come before any further fluid removal.</p>
<p><strong>What will you suggest?</strong> His pressure returns to 118/70 within five minutes, and the nephrologist advises a smaller fluid goal today. You then offer options for the next session. His weight gain over the four-day gap is large, so salt and fluid intake need review with the dietitian. A longer session, or a third weekly session, would lower the rate. His meal could move to before or after dialysis. The timing of his morning medicines and his dry weight could be reviewed. Each of these is the nephrologist&rsquo;s decision.</p>
"""],
    "skills": {"title": "Hypotension response on a simulated patient",
               "intro": "Perform this response on a simulated patient or a colleague in a dialysis chair while your preceptor observes and plays the nurse.",
               "items": [
                   ("Goes to the chair at once and checks that the patient responds, is breathing, and has a pulse.", True),
                   ("Asks for help and states the problem aloud to the nurse.", False),
                   ("Reclines the chair flat with the legs raised, as far as the patient&rsquo;s breathing allows, and turns the patient to the side if vomiting.", True),
                   ("Confirms with the nurse that fluid removal has been stopped.", True),
                   ("Rechecks the blood pressure, counts the pulse by hand, and comments on rate and rhythm.", True),
                   ("Asks for oxygen as the unit&rsquo;s protocol directs.", False),
                   ("Asks about chest pain, breathlessness, and other symptoms, and checks the level of consciousness.", True),
                   ("Uncovers and inspects the access, the needle sites, the connections, and the color of the blood in the venous line.", True),
                   ("Notes the time into the session, the fluid removed so far, the weight gain, the last meal, and the medicines taken today.", False),
                   ("States whether the findings fit a simple drop or suggest a dangerous cause, with reasons.", True),
                   ("States the next step in the unit&rsquo;s protocol if the pressure has not recovered, without quoting an amount from memory.", False),
                   ("Calls the attending nephrologist with an SBAR report and repeats back the advice.", True),
                   ("States when blood must not be returned to the patient.", True),
                   ("Documents the episode, including the response to each step.", False),
               ],
               "placement": "For two weeks, keep a log of every episode of low pressure on your shifts: time into the session, fluid removal rate, last meal, medicines, and response. Review the log with your preceptor and identify one patient whose pattern you will report to the attending nephrologist."},
    "quiz": [
        ("Why do most patients tolerate the removal of several liters in one session?",
         ["The machine removes fluid directly from the tissues",
          "The blood holds far more water than the fluid goal",
          "Refilling, vessel tightening, and the heart&rsquo;s response act together",
          "The dialysis fluid replaces the water removed"], 2,
         "The machine removes water only from the blood. The three defenses hold the pressure while it does."),
        ("Why does tightening of the veins help to maintain pressure during fluid removal?",
         ["Veins hold most of the blood volume, so tightening returns blood to the heart",
          "Veins set the resistance against which the heart pumps",
          "Veins absorb water from the dialysis fluid",
          "Veins slow the heart rate"], 0,
         "When veins tighten, the heart stays filled. When they relax, blood pools and output falls."),
        ("A woman with long-standing diabetes has a pressure of 80/46 mm Hg in hour three. Her pulse is 64 per minute and regular. What does the pulse tell you?",
         ["The reading must be an error",
          "She is not short of volume",
          "The episode is mild",
          "Her heart rate response is blunted, so the pulse does not make the pressure safe"], 3,
         "Autonomic neuropathy and reflex loss of sympathetic tone can both keep the pulse from rising."),
        ("In the analysis by Flythe and colleagues, which definition was most strongly associated with death?",
         ["Any fall in pressure with cramps",
          "A lowest systolic pressure below 90 mm Hg",
          "Any episode that needed saline",
          "A fall of 20 mm Hg with nausea"], 1,
         "Nadir-based definitions tracked mortality. Definitions built on symptoms or interventions did not."),
        ("Published estimates of how often intradialytic hypotension occurs vary widely. What is the main reason?",
         ["Patients differ between countries",
          "Machines differ between units",
          "Studies use different definitions",
          "Most studies are too small"], 2,
         "A fall in pressure alone is very common. A fall with symptoms and an intervention is much less common."),
        ("A patient&rsquo;s pressure has fallen in hour three and the nurse has not yet acted. The patient responds and is breathing. What comes first?",
         ["Order an ECG and wait for it",
          "End the session and return the blood",
          "Telephone the nephrologist before touching the patient",
          "Lay the patient back with the legs raised and stop fluid removal"], 3,
         "These two steps take seconds. Assessment and the call follow immediately."),
        ("How strong is the evidence for the head-down, legs-up position?",
         ["Expert opinion, with a note that its effect may be limited",
          "Large randomized trials show that it raises pressure",
          "Trials show that it is harmful",
          "It has been shown to prevent myocardial stunning"], 0,
         "The European guideline grades it as opinion. It is used because it is quick, carries little risk in a patient who is breathing comfortably, and fits the physiology."),
        ("A patient recovers after first steps. The nurse asks whether to restart fluid removal at the original rate. What is the best answer?",
         ["Yes, because the goal is part of the prescription",
          "Ask the attending nephrologist how to manage the remaining goal",
          "Yes, but raise the blood pump speed",
          "No, lower the dry weight instead"], 1,
         "The remaining goal, the time, and the dry weight belong to the prescription."),
        ("Ten minutes into a session, a man becomes itchy and flushed, begins to wheeze, and his pressure falls. What happens to the blood in the circuit?",
         ["Return it quickly to restore volume",
          "Return it slowly with extra saline",
          "Do not return it. Stop the blood pump and clamp the lines",
          "Continue dialysis and observe"], 2,
         "Onset in the first minutes with itching and wheeze suggests a dialyzer reaction. That blood is not returned."),
        ("A woman with a dialysis catheter has a pressure of 86/50 mm Hg forty minutes into her session. She is shivering and feels warm. What is the best interpretation?",
         ["A simple volume-related drop",
          "A drop caused by her last meal",
          "An expected effect of cool dialysis fluid",
          "Possible sepsis. Call the nephrologist and start the fever protocol"], 3,
         "An early drop with chills and a catheter does not fit fluid removal."),
        ("Which finding makes a simple volume-related drop less likely?",
         ["Onset in the last hour",
          "A patient who arrived at or below the dry weight",
          "Calf cramps",
          "Recovery within minutes of stopping fluid removal"], 1,
         "A patient who is not overloaded has little fluid to lose. Look for another cause, or a dry weight set too low."),
        ("What did the MyTEMP trial show?",
         ["Cooler dialysis fluid as a center-wide policy did not reduce cardiovascular death or admission",
          "Cooler dialysis fluid halved cardiovascular deaths",
          "Cooler dialysis fluid increased deaths",
          "Cooler dialysis fluid has no effect in any patient"], 0,
         "The hazard ratio was 1.00. The trial tested a policy, not cooling for individual patients with frequent episodes."),
        ("What did the echocardiography studies by Burton and colleagues show?",
         ["Preventing hypotension prolongs life",
          "Stunning occurs only with chest pain",
          "Dialysis has no effect on the heart",
          "Heart muscle function often falls during dialysis, and this is associated with later harm"], 3,
         "Stunning occurred in 64% of 70 patients and was associated with higher mortality. The studies were small and observational."),
        ("A man has had low pressure in four of his last six sessions, each time after a full meal in hour two. What should the physician on duty do?",
         ["Tell him never to eat on dialysis days",
          "Lower his fluid goal for all future sessions",
          "Report the pattern to the attending nephrologist and suggest moving the meal",
          "Advise him to skip his morning medicines"], 2,
         "Moving the meal addresses the trigger and protects nutrition. The plan belongs to the nephrologist."),
        ("During an episode, the blood in the venous line looks dark and translucent and the patient has back pain. A second patient nearby is also unwell. What do you do?",
         ["Return the blood to both patients",
          "Stop the blood pump, clamp the lines, do not return the blood, and call for help",
          "Give fluid and continue dialysis",
          "Lower the blood pump speed and observe"], 1,
         "These findings suggest hemolysis, possibly from the dialysis fluid. Hemolyzed blood is not returned."),
    ],
    "terms": [("Intradialytic hypotension", "A fall in blood pressure during a dialysis session. Published definitions differ."),
              ("Nadir systolic pressure", "The lowest systolic pressure recorded during a session."),
              ("Plasma refilling", "Movement of fluid from the tissues back into the blood vessels during dialysis."),
              ("Vascular tone", "The degree of tightening in the walls of small arteries and veins."),
              ("Autonomic neuropathy", "Damage to the nerves that control heart rate and vessel tone."),
              ("Myocardial stunning", "A temporary fall in the pumping of a segment of heart muscle after its blood supply has been reduced."),
              ("Head-down position", "Lying flat with the legs raised above the heart. It is a modified form of the Trendelenburg position, in which the whole body is tilted head down."),
              ("Cluster-randomized trial", "A trial that assigns whole centers, not individual patients, to each treatment."),
              ("Cardiac tamponade", "Fluid around the heart that prevents it from filling."),
              ("Hemolysis", "Breakdown of red blood cells, which releases their contents into the blood.")],
    "readings": [("hemodialysis-complications.html", "An overview of problems during dialysis, including low pressure and cramps."),
                 ("dry-weight-determination.html", "How dry weight is judged and when it should be reassessed."),
                 ("fluid-management-dialysis.html", "Salt and fluid advice that reduces weight gain between sessions.")],
    "calcs": ["calc-ufr-ceiling.html", "calc-idwg-fluid.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
