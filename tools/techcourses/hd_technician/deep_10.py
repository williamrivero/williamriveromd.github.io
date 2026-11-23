# -*- coding: utf-8 -*-
"""Hemodialysis Technician track, Module 10 (Complications and Emergency Response): added lessons.
Merged into the Markdown-sourced module by generate_tech_courses.py."""

ADD = {
"extra": [
(1, "eventguide", "Event-by-event guide", "Fifteen events: what you see, what you do, what the nurse needs", """
{{plain:Your first actions are the same for almost every event: stay with the patient, call the nurse, note the time, and get ready to fetch. What changes is how fast you call and what you bring. The nurse and the nephrologist decide the cause and the treatment.}}
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>What you see or the patient says</th><th>What you do first, within scope</th><th>What the nurse will likely need from you</th></tr></thead>
<tbody>
<tr><td>Low blood pressure</td><td>Yawning, sweating, nausea, dizziness, &ldquo;I feel hot,&rdquo; pale face, going quiet</td><td>Call the nurse now. Stay. Recline the chair as trained or directed</td><td>A blood pressure reading and the earlier readings; fluid removed so far; saline ready at the station</td></tr>
<tr><td>Muscle cramps</td><td>Sudden hard pain in the calf, foot, or hand</td><td>Call the nurse. Stay. Support the limb as the patient prefers</td><td>Blood pressure; fluid removal goal and amount removed; time left</td></tr>
<tr><td>Nausea and vomiting</td><td>Retching; often comes with low blood pressure</td><td>Call the nurse. Give a basin. Turn the head to the side if the patient is drowsy</td><td>Blood pressure; suction within reach if drowsy</td></tr>
<tr><td>Headache</td><td>New or worsening headache</td><td>Tell the nurse. Ask when it started</td><td>Blood pressure; time of onset</td></tr>
<tr><td>Chest pain</td><td>Pain, pressure, or tightness; short of breath; sweating</td><td>Call for help immediately. Stay. Keep the patient still</td><td>Emergency cart and oxygen brought to the chair; blood pressure and pulse; time of onset</td></tr>
<tr><td>Itching</td><td>Scratching. Alone it is common. With rash, wheeze, or swelling, see dialyzer reaction</td><td>Tell the nurse. Look for rash or trouble breathing</td><td>When it started; whether anything was new this session</td></tr>
<tr><td>Fever and chills</td><td>Shaking, feeling cold, hot skin</td><td>Call the nurse. Ask whether other patients feel the same</td><td>Temperature; time since treatment started; access type; the number of patients affected</td></tr>
<tr><td>Dialyzer reaction</td><td>In the first minutes: itching, hives, cough, wheeze, chest or back pain, burning at the access</td><td>Call for help immediately. Stay</td><td>Emergency cart and oxygen; minutes since the start; dialyzer type and whether new or reprocessed; keep the dialyzer and its package</td></tr>
<tr><td>Clotting of the circuit</td><td>Very dark blood, dark streaks in the dialyzer, clots in a chamber, rising pressures</td><td>Call the nurse. Do not reset alarms to keep the pump going</td><td>Pressure trend; saline; a new circuit ready if asked</td></tr>
<tr><td>Bleeding</td><td>Blood at a needle site, connection, or catheter; nosebleed; blood in vomit</td><td>Call the nurse; shout if it is heavy. Uncover the access. Gloves on</td><td>Gauze and clamps; blood pressure; an estimate of the amount</td></tr>
<tr><td>Needle dislodgement</td><td>Needle out or partly out; blood on the sheet or floor; sometimes a venous pressure alarm, sometimes none</td><td>Shout for help. Follow the unit&rsquo;s emergency procedure within your training</td><td>Gauze, clamps, the cart; time found; estimate of blood lost</td></tr>
<tr><td>Seizure</td><td>Stiffening, jerking, not responding</td><td>Call for help. Protect the head and the access arm from injury. Put nothing in the mouth. Note the start time</td><td>How long it lasted; oxygen and suction; the glucose meter if the unit uses one</td></tr>
<tr><td>Cardiac arrest</td><td>Not responding and not breathing normally</td><td>Shout for help and start the code response. Begin compressions if you hold current basic life support certification</td><td>Cart and defibrillator; a recorder; someone to meet the ambulance</td></tr>
<tr><td>Suspected air embolism</td><td>Air or foam seen in the venous line with sudden cough, chest pain, breathlessness, or collapse</td><td>Call for help immediately. Position the patient on the left side with the head down, as trained and as the nurse directs</td><td>Oxygen and the cart; what you saw in the line and where</td></tr>
<tr><td>Suspected hemolysis</td><td>Blood in the venous line looks clear cherry red; chest, back, or abdominal pain; breathlessness</td><td>Call for help immediately. Check whether other patients have symptoms</td><td>Dialysate temperature and conductivity readings; today&rsquo;s chlorine result; the circuit and concentrate containers kept, not discarded</td></tr>
</tbody></table></div>
{{key:In a dialyzer reaction, clotting, or suspected hemolysis, the used dialyzer, lines, and containers are evidence. Nothing goes in the bin until the nurse says so.}}
{{stop:Two or more patients with the same symptom at the same time points to something shared: water, dialysate, or supplies. Say &ldquo;more than one patient&rdquo; in your first sentence to the charge nurse.}}
"""),
(2, "cartcheck", "Cart and oxygen", "The emergency cart and oxygen: the daily check", """
<p>An emergency cart is checked so that nobody has to search during an emergency. Medications on the cart are checked by the nurse or pharmacist. The equipment check is often assigned to a technician. Use your unit&rsquo;s own checklist; the table shows what such a list usually covers.[[psn2024]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>What you confirm</th><th>If it fails</th></tr></thead>
<tbody>
<tr><td>Cart location and seal</td><td>In its marked place, path clear, seal or lock intact, seal number matches the log</td><td>Tell the charge nurse; a broken seal means a full recheck</td></tr>
<tr><td>Defibrillator</td><td>Plugged in and charging, ready indicator or self-test passed, pads sealed and in date, spare pads present</td><td>Report at once; the unit arranges a replacement</td></tr>
<tr><td>Oxygen cylinder</td><td>Gauge reads above the minimum your unit sets, regulator and key attached, cylinder secured upright</td><td>Request a full cylinder now, not at the end of the shift</td></tr>
<tr><td>Oxygen delivery</td><td>Tubing, masks, and nasal cannulas present and sealed</td><td>Restock from stores</td></tr>
<tr><td>Bag-valve mask</td><td>Present with mask sizes, bag reinflates when squeezed</td><td>Replace</td></tr>
<tr><td>Suction</td><td>Turns on, pulls at the tip when blocked with a gloved thumb, catheter and tubing attached</td><td>Report to biomedical staff</td></tr>
<tr><td>Supplies</td><td>Gloves, backboard, saline, and the items on the unit&rsquo;s list, with nothing past its expiry date</td><td>Restock and record</td></tr>
<tr><td>Signature</td><td>Date, time, and your name on the check sheet</td><td>An unsigned check counts as not done</td></tr>
</tbody></table></div>
{{key:Know three places before every shift: the cart, the oxygen, and the emergency packs at the stations. If any has moved, find out where before the first patient arrives.}}
"""),
(2, "codejobs", "Your role in a code", "A code at the chair: five jobs a technician may be given", """
<p>A code is the unit&rsquo;s response to a patient who has stopped breathing or has no pulse. The nurse or physician leads. Each helper has one job and stays in it until the leader changes it.</p>
{{cards:Jobs a technician may be assigned|Caller::Activates the unit&rsquo;s emergency call and telephones the ambulance or hospital team if the leader says so. States the unit, the station, and &ldquo;adult cardiac arrest.&rdquo;|Cart bringer::Brings the cart, defibrillator, and oxygen to the chair and moves furniture out of the way.|Compressor::Gives chest compressions only if trained and currently certified in basic life support. Swaps with another person about every 2 minutes when the leader calls it.|Runner::Fetches what is asked for, meets the ambulance crew at the door, and guides them in.|Recorder::Writes each event with its clock time, using one clock for the whole event.}}
{{fig:code_first5|The first five minutes of a cardiac arrest in the unit. Find the jobs a technician may be given.}}
<p>The patient&rsquo;s blood circuit is handled by a nurse. If you are at the machine, do not press anything unless the leader tells you to.</p>
<div class="table-wrap"><table>
<thead><tr><th>Time</th><th>Recorder&rsquo;s entry (example)</th></tr></thead>
<tbody>
<tr><td>09:42</td><td>Station 6. Patient found not responding, not breathing. Help called by technician</td></tr>
<tr><td>09:42</td><td>Compressions started by Nurse A</td></tr>
<tr><td>09:43</td><td>Cart and defibrillator at chair. Ambulance called by technician B</td></tr>
<tr><td>09:44</td><td>Pads on. Shock advised. Shock 1 given</td></tr>
<tr><td>09:46</td><td>Compressor changed to technician C. Rhythm check: no shock advised</td></tr>
<tr><td>09:47</td><td>Blood returned and lines disconnected by Nurse D</td></tr>
<tr><td>09:48</td><td>Medication given by Nurse D on physician&rsquo;s order (name and dose as called out)</td></tr>
<tr><td>09:52</td><td>Pulse felt by leader. Patient breathing</td></tr>
<tr><td>09:58</td><td>Ambulance crew at chair. Handover by leader</td></tr>
</tbody></table></div>
{{key:The recorder writes what is said aloud, with the time, and asks &ldquo;What was that dose?&rdquo; if it was not heard. The recorder does not tidy, guess, or fill in later from memory.}}
"""),
(4, "packs", "Emergency disconnect", "Emergency disconnection and evacuation", """
<p>In a fire or a collapsing building there may be no time to return each patient&rsquo;s blood in the usual way. Units plan for this with an emergency disconnection pack at every station and a procedure often called clamp and disconnect. The blood left in the circuit is lost, which is accepted to get the patient out quickly.</p>
{{cards:The principle|Decision::The charge nurse or incident leader orders emergency disconnection. Nobody starts it alone unless unit policy says so.|Clamp::Both blood lines and both access lines are clamped, so that neither the patient nor the circuit can bleed.|Separate::The lines are disconnected, or cut between clamps, as the unit&rsquo;s policy states.|Needles stay in::Fistula needles are left in place, taped and capped, and removed later in a safe area.|Go::The patient leaves the machine behind.}}
<p>Who performs each step is written in unit policy. In most units a nurse does it, and patients who are able are taught to do it for themselves. A technician does it only if the policy assigns it and a drill has confirmed the skill.</p>
<div class="table-wrap"><table>
<thead><tr><th>Your part</th><th>Detail</th></tr></thead>
<tbody>
<tr><td>Before any emergency</td><td>Check at setup that the pack is at the station, sealed, and complete</td></tr>
<tr><td>When the order is given</td><td>Hand the pack to the nurse; move chairs, stools, and bins out of the exit path</td></tr>
<tr><td>Moving patients</td><td>Follow the order the leader calls. Commonly, patients who can walk go first, then wheelchairs, then those who must be carried</td></tr>
<tr><td>At the assembly point</td><td>Help with the head count against the day&rsquo;s patient list; stay with patients; watch needle sites for bleeding</td></tr>
<tr><td>Never</td><td>Go back inside for equipment, records, or belongings</td></tr>
</tbody></table></div>
"""),
(4, "firstfive", "First five minutes", "Utility failures and disasters: the first five minutes", """
<p>In every disaster one person leads, usually the charge nurse. Your first report is short: what happened, where, and how many patients are connected.</p>
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>First five minutes, technician</th><th>Do not</th></tr></thead>
<tbody>
<tr><td>Power failure</td><td>Stay at your stations and look at each patient. Tell the nurse which machines are on battery and which are dark. Bring flashlights and the hand cranks for the blood pumps. Note the time. Start no new treatments</td><td>Assume the generator will start, or switch machines off and on</td></tr>
<tr><td>Water failure</td><td>Count the machines alarming and tell the charge nurse and the water technician. Read the water room gauges and alarms if this is assigned to you. Hold all new starts. Note the time</td><td>Reset machines repeatedly, or bypass a water alarm</td></tr>
<tr><td>Fire or smoke</td><td>Rescue anyone in immediate danger. Raise the alarm. Close doors to contain it. Use an extinguisher only if trained, the fire is small, and your exit is behind you. Prepare for emergency disconnection</td><td>Use the elevator, or open a hot door</td></tr>
<tr><td>Earthquake</td><td>During shaking: drop, cover, and hold on; tell patients to stay in their chairs and protect their heads. After shaking: look at every patient, access, and line; report injuries, leaks, and fallen equipment; expect aftershocks</td><td>Run for the exit during shaking, or try to disconnect anyone while the floor is moving</td></tr>
<tr><td>Typhoon or flood</td><td>Follow the unit&rsquo;s plan, which may shorten or reschedule sessions. Move supplies and records off the floor. Report any water entering the unit or the water room. If water reaches electrical equipment, keep away and tell the leader</td><td>Touch plugged-in equipment while standing in water, or promise patients a new schedule yourself</td></tr>
</tbody></table></div>
{{flow:After any event|Write your own account::The same day, in your own words: times, what you saw, what you were told, and what you did.|Separate fact from opinion::&ldquo;Machine 4 screen dark at 14:06&rdquo; is a fact. &ldquo;The battery was faulty&rdquo; is an opinion.|Hand over evidence::Tagged equipment, kept circuits, and log sheets go to the person the leader names.|Attend the debrief::A short meeting soon after. What went well, what was slow, what was missing.|Leave with one action::Each fix has a named owner and a date.}}
{{key:A debrief looks for weak points in the system, such as an empty oxygen cylinder or an unclear role. It is not a search for someone to blame, and it works only if people say what really happened.}}
"""),
],
"quiz_extra": [
("A patient has a seizure in the dialysis chair. Which first action is within the technician&rsquo;s scope?",
 ["Place a padded object between the teeth", "Stop the blood pump and return the blood", "Call for help, protect the head and access arm from injury, and note the start time", "Hold the limbs down firmly until the jerking stops"], 2,
 "The technician calls, protects from injury, and times the event; nothing goes in the mouth and the circuit is the nurse&rsquo;s."),
("After a suspected dialyzer reaction, what should happen to the used dialyzer and its package?",
 ["Keep them for the nurse, because they are evidence", "Discard them at once as infectious waste", "Send the dialyzer for reprocessing as usual", "Rinse the dialyzer and store it at the station"], 0,
 "The team may need the dialyzer type, lot, and circuit to find the cause."),
("During the daily cart check the oxygen gauge reads below the minimum your unit sets. What do you do?",
 ["Sign the sheet and mention it at the next handoff", "Record it, tell the charge nurse, and request a full cylinder now", "Leave it, since oxygen is rarely needed", "Borrow the regulator from another cylinder at the end of the shift"], 1,
 "A cart item that fails its check is corrected immediately, not later."),
("You are assigned as recorder during a code. Which practice is correct?",
 ["Write a summary from memory after the event", "Write only the medications", "Use whichever clock is nearest for each entry", "Write each event with its time as it is called out, using one clock throughout"], 3,
 "A code record is a time log made as events happen, on a single clock."),
("In an emergency clamp-and-disconnect, what happens to fistula needles?",
 ["They are pulled out at the chair before leaving", "They are left in place, secured, and removed later in a safe area", "The technician removes them at the exit door", "They are flushed with saline first"], 1,
 "Removing needles takes time and needs pressure on each site; in an evacuation they stay in until the patient is safe."),
("The power fails and machines switch to battery. Which technician action is correct in the first five minutes?",
 ["Switch each machine off and on to reset it", "Start waiting patients quickly before the battery runs out", "Leave the floor to check the generator", "Stay with your patients, report which machines are on battery or dark, and bring flashlights and hand cranks"], 3,
 "The technician observes, reports, and brings equipment; the nurse decides what happens to each treatment."),
("Which entry in your written account after an event is a fact, not an opinion?",
 ["The battery was probably old", "Machine 4 screen went dark at 14:06", "The night shift must have skipped the check", "The patient was overreacting"], 1,
 "Accounts record what was seen and when; causes are worked out in the review."),
],
"skills_extra": [
("Completes the unit&rsquo;s emergency cart and oxygen check on the real cart, identifies one planted fault, and reports and records it.", True),
("Acts as recorder in a simulated code and produces a time log with every called event, from one clock, with no entries added from memory.", False),
("Locates the emergency disconnection pack at an assigned station, names its contents, and states who orders and who performs emergency disconnection under unit policy.", True),
],
}
