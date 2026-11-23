# -*- coding: utf-8 -*-
"""Hemodialysis Technician track, Module 01: added lessons (patient journey, shift timeline, name alerts,
SBAR worked examples, documentation rules and conduct)."""

ADD = {
"extra": [
(1, "journey", "Patient journey", "One patient, one treatment: who does what at each step", """
{{plain:Think of renewing a document at a government office. You move from window to window in a fixed order: the form, the photo, the payment, the release. Each window trusts that the one before it did its job. A patient moves through the dialysis unit the same way, from the door to the chair and back to the door, and at each step the technician and the nurse have different jobs.}}
<p>The picture has a limit. At an office, a skipped window costs you time, and a clerk sends you back to it. In the unit, nobody sends the patient back. A weight that was never checked becomes the basis of the fluid goal. An identity that was never confirmed becomes another patient&rsquo;s prescription. Your work is to know the order, to do your own steps the same way every time, and to notice when a step before yours looks skipped.</p>
{{flow:The patient&rsquo;s path through the unit|Arrival::You greet the patient and observe how he or she looks.|Weight::You measure and record the pre-treatment weight.|Identity at the station::You check two identifiers against the treatment record.|Pre-treatment checks::You measure vital signs; the nurse assesses the patient and the access.|Connection::The nurse connects the patient and starts treatment.|Treatment::You record readings at set intervals and report changes.|End of treatment::The nurse returns the blood and disconnects.|Post-treatment checks::You measure vital signs and the post-treatment weight.|Departure::The nurse decides that the patient is fit to leave.|Turnover::You strip, clean, and disinfect the station.}}
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Technician</th><th>Nurse</th><th>Tell the nurse at once if</th></tr></thead>
<tbody>
<tr><td>Arrival</td><td>Greets the patient. Notices how the patient looks, walks, speaks, and breathes</td><td>Is told about anything unusual</td><td>The patient looks unwell, is breathless or confused, or is bleeding</td></tr>
<tr><td>Weight</td><td>Checks that the scale reads zero. Weighs the patient the same way every time. Records the weight</td><td>Reviews the weight and sets the fluid removal goal within the prescription</td><td>The weight is far from the patient&rsquo;s usual, or the patient cannot stand safely</td></tr>
<tr><td>Identity at the station</td><td>Checks two identifiers against the treatment record. Checks that the dialyzer and concentrates match the prescription sheet</td><td>Verifies the prescription and the machine settings</td><td>Anything does not match</td></tr>
<tr><td>Pre-treatment checks</td><td>Measures and records blood pressure, pulse, and temperature as assigned</td><td>Assesses the patient and the access. Decides whether treatment starts</td><td>A reading is outside the limits your unit sets, or the patient reports a new symptom</td></tr>
<tr><td>Connection</td><td>Has the primed circuit and supplies ready. Stays nearby</td><td>Inserts the needles or opens the catheter, connects, and starts treatment</td><td>You see air, a leak, or a loose connection</td></tr>
<tr><td>Treatment</td><td>Records readings at the interval the unit sets. Keeps the access in view. Answers alarms by looking and calling</td><td>Assesses, gives medication, and adjusts treatment</td><td>Any symptom, any alarm you cannot explain, any blood outside the circuit</td></tr>
<tr><td>End of treatment</td><td>Brings the supplies for returning blood and for dressings</td><td>Returns the blood, removes the needles or closes the catheter</td><td>Bleeding continues or the patient feels faint</td></tr>
<tr><td>Post-treatment checks</td><td>Measures post-treatment weight and vital signs as assigned</td><td>Decides whether the patient is fit to go home</td><td>Dizziness on standing, bleeding through the dressing, or a weight far from the target</td></tr>
<tr><td>Turnover</td><td>Removes and discards the circuit, cleans and disinfects (Modules 5 and 6)</td><td>Releases the station for the next patient</td><td>A step could not be completed</td></tr>
</tbody></table></div>
<p>Notice the last column. At every step there is a point where you stop and tell the nurse. You do not need to know the cause to make that call. You need to see the change, say it clearly, and say it at once.</p>
{{key:Your unit&rsquo;s written job description and your competency sign-off set the exact split of tasks. This table does not, and neither does a coworker&rsquo;s idea of what is usual.[[doh2012]]}}
"""),
(1, "shiftclock", "Shift timeline", "The technician&rsquo;s day: opening, turnover, and closing", """
<p>A unit usually runs two or three patient shifts in a day. Your duties gather at three points: before the first patient arrives, between shifts, and after the last patient leaves. Each point ends with a handoff to someone who was not there. Read the last column of the table as a test: when you finish, could the next person see exactly what you see?</p>
<div class="table-wrap"><table>
<thead><tr><th>When</th><th>Typical duties</th><th>Finished when</th></tr></thead>
<tbody>
<tr><td>Opening, before the first patient</td><td>Read the logbook and receive the handoff. Confirm that the water system has been checked and released by the person assigned (Module 7). Switch on the machines and let each one complete its self-test. Check the concentrates. Stock each station. Check the scale. Set up and prime according to the schedule sheet</td><td>Every station is marked ready or on hold, and the nurse knows which</td></tr>
<tr><td>During each shift</td><td>Record readings on time. Answer alarms by looking and calling. Restock. Prepare supplies for the next shift away from occupied stations</td><td>The records are current at every interval</td></tr>
<tr><td>Turnover, between shifts</td><td>Wait until the patient has left the station. Remove and discard the used circuit. Wipe every surface and keep it wet for the contact time. Run the machine program your unit requires. Only then bring supplies for the next patient[[cdc_dialysis]]</td><td>The station is clean, dry, and set up for the right patient</td></tr>
<tr><td>Closing, after the last patient</td><td>Run the end-of-day disinfection on every machine. Handle leftover concentrate as the procedure states. Remove waste and used linen. Count and restock. Complete the machine and cleaning logs. Report every fault in writing</td><td>The next opening team can read exactly what is ready and what is on hold</td></tr>
</tbody></table></div>
<p>The order inside turnover is the point of turnover. Clean supplies set down on a surface that has not yet been disinfected are no longer clean, and they travel with the next patient. That is why the station is cleaned first and supplied second, never the other way around.</p>
{{stop:Turnover is the most hurried part of the day, and it is where shortcuts cause harm. Never bring the next patient&rsquo;s supplies to a station that has not been cleaned. Never seat a patient at a machine whose disinfection or self-test did not finish. If the time is too short to do turnover properly, tell the nurse. Do not shorten the cleaning.}}
"""),
(2, "namealert", "ID and name alerts", "Patient identification: when to check, and name alerts", """
<p>You already know the rule of two identifiers. This section adds three things: when you repeat the check, what does not count as an identifier, and what the unit does when two patients are easy to confuse.</p>
<p>The check is repeated because every task you do for a patient carries that patient&rsquo;s name forward. A weight, a dialyzer, a result, or a schedule attached to the wrong person does its harm quietly, often long after you have moved on.</p>
<div class="table-wrap"><table>
<thead><tr><th>Check identity before you</th><th>Because a mix-up would</th></tr></thead>
<tbody>
<tr><td>Record a weight or vital sign</td><td>Put one patient&rsquo;s numbers in another patient&rsquo;s record, and the fluid goal is built on them</td></tr>
<tr><td>Set up a dialyzer, concentrate, or machine for a named patient</td><td>Deliver another patient&rsquo;s prescription</td></tr>
<tr><td>Bring a reprocessed dialyzer to the station</td><td>Expose the patient to another person&rsquo;s blood (Module 11)</td></tr>
<tr><td>Hand over any paper, result, or schedule</td><td>Give private information to the wrong person</td></tr>
</tbody></table></div>
{{cards:These are not identifiers|The chair or station number::Patients change seats, and you will not always know when.|A familiar face::Memory fails on a busy morning, even with patients you have known for years.|A yes to your question::A patient who is deaf, drowsy, or simply polite may agree to any name.|A relative&rsquo;s word alone::Use it only as your unit&rsquo;s alternate process allows.}}
<p>Ask an open question, so that the patient supplies the answer: &ldquo;Please tell me your full name and date of birth.&rdquo; Do not ask, &ldquo;Are you Mr. Cruz?&rdquo; A closed question can be answered with a yes, and a yes proves nothing.</p>
<p><strong>Name alerts.</strong> A name alert is a visible warning that two patients could be mistaken for each other. Many surnames are shared by a large number of families, so every unit meets this often. You will see it most on the busiest mornings, when two charts with the same surname sit side by side at the nurses&rsquo; station.</p>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>Example (fictional)</th><th>What the unit does</th></tr></thead>
<tbody>
<tr><td>Same surname</td><td>Jose Santos and Josefina Santos</td><td rowspan="4">Marks both records, and both dialyzers where reuse is practiced, with a name-alert label. Seats the two patients apart or on different shifts where possible. Uses the full name with middle name and the date of birth every time. States the alert aloud at every handoff</td></tr>
<tr><td>Same full name</td><td>Two patients named Maria Reyes</td></tr>
<tr><td>Names that sound alike</td><td>Bautista and Batista</td></tr>
<tr><td>Relatives, or a senior and a junior</td><td>Ramon Garcia Sr. and Ramon Garcia Jr.</td></tr>
</tbody></table></div>
{{key:When you notice a possible mix-up that nobody has labeled yet, you have found a name alert. Tell the nurse the same day so that both records are marked.}}
"""),
(3, "sbarmore", "SBAR in practice", "Reporting to the nurse: two worked SBAR examples", """
<p>SBAR stands for Situation, Background, Assessment, Recommendation. It gives a spoken report a fixed shape, so the listener finds the problem in the first sentence and the request in the last. For a technician, two parts need care. The assessment is what you observed and measured, never a diagnosis. The recommendation is a clear request, not a hint.</p>
{{cards:Have these ready before you speak|Who and where::The full name and the station number.|Numbers with times::The exact reading and when you took it.|What you have done::Including what you have not touched.|What you need::Come now, come when free, or tell me what to do.}}
<div class="table-wrap"><table>
<thead><tr><th></th><th>Example 1: a patient change</th><th>Example 2: an equipment fault</th></tr></thead>
<tbody>
<tr><td>Situation</td><td>&ldquo;Mrs. Dela Paz at Station 4 says she feels dizzy.&rdquo;</td><td>&ldquo;Machine 7 has failed its self-test twice.&rdquo;</td></tr>
<tr><td>Background</td><td>&ldquo;She is two hours into treatment. Her blood pressure was 150/90 at the start.&rdquo;</td><td>&ldquo;No patient is connected. Mr. Aquino is scheduled on it at 11:00.&rdquo;</td></tr>
<tr><td>Assessment</td><td>&ldquo;At 09:10 it is 96/58 and her pulse is 104. She is pale and yawning. I have not changed anything on the machine.&rdquo;</td><td>&ldquo;The screen reads &lsquo;conductivity test failed&rsquo; both times. The concentrates are correct and in date. I have labeled it &lsquo;Do not use.&rsquo;&rdquo;</td></tr>
<tr><td>Recommendation</td><td>&ldquo;Please come and see her now.&rdquo;</td><td>&ldquo;Which machine should I set up for Mr. Aquino, and shall I call the biomedical technician?&rdquo;</td></tr>
</tbody></table></div>
<p>Notice what each report contains: a name and a place, the numbers with their times, what was done and not done, and a request the nurse can answer with one word or one action. Now compare the weak versions below.</p>
<div class="table-wrap"><table>
<thead><tr><th>Weak report</th><th>Why it fails</th><th>Stronger report</th></tr></thead>
<tbody>
<tr><td>&ldquo;Station 4 is not okay.&rdquo;</td><td>No name, no numbers, no request</td><td>Example 1 above</td></tr>
<tr><td>&ldquo;Her pressure dropped because too much fluid is coming off.&rdquo;</td><td>It states a cause the technician cannot know</td><td>&ldquo;Her pressure was 150/90 and is now 96/58.&rdquo;</td></tr>
<tr><td>&ldquo;Machine 7 is acting up again.&rdquo;</td><td>The exact message is missing</td><td>Read the words on the screen aloud</td></tr>
</tbody></table></div>
<p><strong>Check-back.</strong> A spoken instruction can be heard two ways. Repeat what you were told and wait for a yes: &ldquo;You want me to set up Machine 9 for Mr. Aquino and leave Machine 7 labeled. Correct?&rdquo; Then record the time and the name of the person you told.</p>
"""),
(3, "charting", "Documentation rules", "Documentation rules, with good and poor entries", """
{{plain:Think of the logbook a tricycle driver keeps for the owner of the vehicle: the date, the trips, the fuel, the money handed over. The owner was not on the road, so the logbook is the only way to know what happened. The treatment record works the same way for the next shift, the nephrologist, and an inspector. Write what you saw, measured, and did, with the time and your name.}}
<p>The picture has a limit. A driver&rsquo;s logbook is read by one person and settles a day&rsquo;s accounts. A treatment record is read by many people, for years, and decisions about a patient&rsquo;s care are built on it. It is also a legal document. Each rule below protects one of those uses.</p>
<div class="table-wrap"><table>
<thead><tr><th>Rule</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Write legibly in permanent ink, or under your own login</td><td>An entry nobody can read, or nobody can trace to you, protects no one</td></tr>
<tr><td>Record the real time of each observation</td><td>Trends depend on times</td></tr>
<tr><td>Sign every entry with your name and designation</td><td>Each entry needs an owner</td></tr>
<tr><td>Record what you measured, with units</td><td>&ldquo;Normal&rdquo; and &ldquo;okay&rdquo; are opinions, not measurements</td></tr>
<tr><td>Correct an error with a single line, then your initials, the date, and the time</td><td>The original must stay readable. No correction fluid, no erasing, no writing over</td></tr>
<tr><td>Mark a forgotten entry &ldquo;late entry&rdquo; with the time you are writing and the time of the observation</td><td>Backdating is falsification</td></tr>
<tr><td>Never chart ahead, and never chart for someone else</td><td>You can sign only for what you did and saw</td></tr>
<tr><td>Leave no blank lines or spaces</td><td>Anyone can fill in a blank later</td></tr>
<tr><td>Use only the abbreviations your unit approves</td><td>Private shorthand gets misread</td></tr>
</tbody></table></div>
<p>Each good entry below answers the same questions: when, what exactly, and who was told. Each poor entry leaves the reader to guess.</p>
<div class="table-wrap"><table>
<thead><tr><th>Poor entry</th><th>Good entry</th></tr></thead>
<tbody>
<tr><td>&ldquo;BP ok.&rdquo;</td><td>&ldquo;08:30 BP 138/84, pulse 76, right arm, seated. J. Ramos, HD Tech.&rdquo;</td></tr>
<tr><td>&ldquo;Patient complaining again.&rdquo;</td><td>&ldquo;09:10 Patient states, &lsquo;I feel dizzy.&rsquo; BP 96/58. Nurse L. Cruz informed at 09:11.&rdquo;</td></tr>
<tr><td>&ldquo;Machine problem, fixed.&rdquo;</td><td>&ldquo;06:20 Machine 7 failed conductivity self-test twice. Labeled Do not use. Charge nurse informed 06:22.&rdquo;</td></tr>
<tr><td>A 09:30 reading written at 10:15 as if on time</td><td>&ldquo;10:15 Late entry for 09:30: BP 122/76, pulse 80.&rdquo;</td></tr>
</tbody></table></div>
{{cards:Confidentiality and conduct|Need to know::Open and discuss a record only for the patient you are assigned.|No photos::Never photograph patients, records, screens, or schedules on a personal phone.|No social media::Not even without a name. A chair, a tattoo, or a date can identify someone.|Low voice::Speak about a patient at the chair, not across the room, and never in the elevator or the canteen.|Callers and visitors::Give no schedule or health details. Refer the request to the nurse.|Gifts and money::Follow unit policy. Never accept payment for a favor or a preferred slot.|Respect::Ask before you touch, explain what you are doing, and keep the patient covered.}}
{{stop:If anyone asks you to change, backdate, or sign an entry for something you did not do or see, do not do it. Tell the charge nurse or your supervisor.}}
"""),
],
"quiz_extra": [
("Which wording is the correct way to ask a patient to confirm identity?",
 ["&ldquo;Are you Mr. Cruz?&rdquo;", "&ldquo;You are in Chair 5 as usual, right?&rdquo;", "&ldquo;Please tell me your full name and date of birth.&rdquo;", "&ldquo;Your birthday is in May, correct?&rdquo;"], 2,
 "An open question makes the patient supply the identifiers; a yes can be given to any name."),
("Jose Santos and Josefina Santos are scheduled on the same shift. What should happen?",
 ["Both records carry a name-alert label and the alert is stated at handoff", "The two are seated side by side so staff can compare them", "Staff use first names only for the shift", "Nothing, because the first names differ"], 0,
 "Similar names are marked, kept apart where possible, and announced at every handoff."),
("At 10:15 you realize you did not write down the 09:30 reading you took. What is correct?",
 ["Write it in the 09:30 space as if it had been written on time", "Leave it out to keep the record tidy", "Ask a coworker to write it for you", "Write it now, marked as a late entry, with the current time and the time of the observation"], 3,
 "A late entry is honest; backdating is falsification."),
("When may cleaning and disinfection of a station begin?",
 ["As soon as the blood has been returned", "After the patient has left the station", "While the needle sites are being held", "When the next patient arrives"], 1,
 "The station is cleaned only once the patient has left it, and the next patient&rsquo;s supplies come after cleaning."),
("Which statement is a suitable Assessment in a technician&rsquo;s SBAR report?",
 ["&ldquo;She is having a reaction to the dialyzer.&rdquo;", "&ldquo;Too much fluid is being removed.&rdquo;", "&ldquo;Her blood pressure was 150/90 and is now 96/58, and she says she is dizzy.&rdquo;", "&ldquo;She needs saline.&rdquo;"], 2,
 "The technician reports observations and numbers, not a cause or a treatment."),
("After treatment, who decides that the patient is fit to go home?",
 ["The nurse", "The technician who took the last blood pressure", "The patient&rsquo;s companion", "The receptionist"], 0,
 "The technician measures and reports; the nurse assesses and decides."),
],
"skills_extra": [
("Identifies a name-alert pair on a mock schedule and states the steps the unit takes for both patients.", True),
("Gives an SBAR report on a simulated equipment fault with the exact screen message, times, action taken, and a clear request, then confirms the instruction with check-back.", False),
("Corrects a mock charting error with a single line, initials, date, and time, leaving the original readable.", True),
],
}
