# -*- coding: utf-8 -*-
"""Physician on Duty, Module 30: When the Power or Water Fails (power, water, and building emergencies; continuity of dialysis).
Written for this series from published sources."""

MODULE = {
    "image_alt": "Dusk in a dialysis unit during a typhoon. Rain streaks the window, emergency lights are on, one machine screen is dark, and a nurse and a physician stand beside a reclined patient.",
    "objectives": [
        "Explain why a dialysis patient tolerates a missed session poorly and why sessions are moved earlier before a storm, with the strength of the evidence.",
        "Lead the first ten minutes of a power failure: confirm that every patient is safe, oversee emergency take-off with manual blood return when it is safe, and call per protocol.",
        "Recognize a possible water or dialysis fluid contamination event, have the affected treatments stopped, keep the circuits, and escalate at once.",
        "Respond to an earthquake, fire, flood, or evacuation order using the unit&rsquo;s plan: emergency disconnection, the grab bag, the routes, and patient tracking.",
        "Apply the unit&rsquo;s priority list when capacity is cut, and give patients the emergency diet and medicine advice the unit has approved.",
        "Describe how a unit keeps its patients dialyzed when it cannot open: partner units, a patient registry, a communication tree, and an after-event review.",
    ],
    "big": """
{{plain:Picture a jeepney route that needs fuel, a road, a driver, and a working engine all at once. Lose one and the trip stops. A hemodialysis patient depends on four things in the same way: electricity, treated water, transport, and trained staff. A typhoon can take away all four in one night.}}
<p>The picture has a limit. A stalled jeepney waits safely at the roadside. A patient&rsquo;s body does not wait. Without dialysis, water, potassium, and acid keep building up. And when the power fails mid-session, part of the patient&rsquo;s blood is outside the body, in tubing that has stopped moving.</p>
{{cards:Key terms for this module|Emergency take-off::Ending all treatments quickly because the unit can no longer run them.|Manual blood return::Returning the circuit&rsquo;s blood by turning the blood pump by hand.|Clamp and cut::Disconnecting without returning the blood.|Standby generator::A fuel generator that takes over when the main power fails.|Water event::Illness caused by a fault in the water or dialysis fluid.|Early dialysis::A session moved ahead of schedule before an expected disruption.|Priority list::The unit&rsquo;s written order for who dialyzes first when sessions are short.|Grab bag::A packed bag by the exit with the patient list, contacts, kits, and dialysis summaries.}}
<p>Most power cuts end when the generator starts, and the shift goes on. A few become real emergencies: the generator fails, the water room floods, the building shakes, or several patients fall ill at once. Your work is to keep every patient safe in the first ten minutes, follow the unit&rsquo;s plan without improvising, and call early.</p>
""",
    "case": {"title": "Signal No. 4, and tomorrow is a full day", "html": """
<p>It is a Wednesday in September, 4:10 p.m., the second shift at a 15-station free-standing unit in Marikina. The Philippine Atmospheric, Geophysical and Astronomical Services Administration (PAGASA) has raised Tropical Cyclone Wind Signal No. 4 for the area, with landfall expected overnight. Twelve patients are on the machines.</p>
<p>The nurse, Ms. Maricel Dizon, calls you. The main power has failed, the generator has not started, and the machines are alarming on battery. Mr. Rodrigo Santos, 58, dialyzes through a right internal jugular catheter and is at hour three. His last pressure was 104/62 mm Hg. Mrs. Lourdes Reyes, 71, has a left arm fistula. She missed Monday&rsquo;s session because of flooding, and her potassium before dialysis today was 6.8 mmol/L. She is 40 minutes into treatment. These values are illustrative.</p>
<p>The technician, Mr. Jun Aquino, is checking the generator. The charge nurse has assigned one nurse to each row and opened the emergency take-off kits. Tomorrow&rsquo;s schedule has 30 patients, and the water room is in the basement.</p>
""", "questions": ["What do you check and decide in the next ten minutes, and in what order?",
                  "Which patients&rsquo; blood should be returned by hand, and when would you clamp and disconnect without returning it?",
                  "What do you ask the attending nephrologist about tomorrow&rsquo;s 30 patients, and who should be dialyzed first if the unit can open only partly?"]},
    "sections": [
        ("why", "Why they cannot wait", "Why a dialysis patient cannot wait out a storm", """
<p>Module 2 explained the closed drain. A failed kidney no longer removes the water, salt, potassium, and acid that enter the body each day. Dialysis opens the drain for a few hours, then closes it until the next session.</p>
{{fig:pod02_drain|With the drain closed, everything that comes in stays until the next session. A storm keeps the drain closed for longer.}}
<p>Each skipped session adds two or three more days of intake to a body that cannot clear it. The danger does not rise in a straight line. Potassium can reach a level that disturbs the heart rhythm before the patient feels short of breath. A patient who looks well can still be in danger.</p>
<p>The long gap is already the riskiest part of the week. In a large cohort, death and cardiovascular admission were more frequent on the day after the long weekend gap than on other days.[[foley2011]] A disaster stretches a two-day gap into four or five.</p>
<h3>What the disaster studies show</h3>
<p>After Hurricane Katrina in 2005, investigators interviewed 386 patients from nine New Orleans units. Overall, 44% missed at least one session and almost 17% missed three or more. Missing three or more, compared with none, was associated with hospitalization: adjusted odds ratio (OR) 2.16, 95% confidence interval (CI) 1.05 to 4.43. Patients unaware of their unit&rsquo;s emergency plan were more likely to miss three or more.[[anderson2009]] Outside disasters, the Dialysis Outcomes and Practice Patterns Study (DOPPS) found that skipping one or more sessions a month was associated with higher mortality (relative risk 1.30).[[saran2003]] Both studies are observational. Patients who miss sessions differ in many ways from those who do not.</p>
<p>Before Hurricane Sandy in 2012, many units dialyzed patients ahead of schedule. A retrospective study of Medicare claims included 13,836 patients; 60% received early dialysis. After adjustment, early dialysis was associated with lower odds of an emergency department visit (OR 0.80), hospitalization (OR 0.79), and death within 30 days (OR 0.72, 95% CI 0.52 to 0.997).[[lurie2015]] The data could not show who was offered early dialysis and declined, so healthier patients may have been the ones who came. The finding supports the practice; it does not prove that early dialysis prevents death.</p>
<h3>What you do when a storm is coming</h3>
<p>When PAGASA raises a wind signal for your area, ask the charge nurse and the attending nephrologist whether the unit&rsquo;s plan moves sessions earlier, and help identify the patients most at risk. Any change to a schedule, session length, or fluid goal is the nephrologist&rsquo;s decision. The site&rsquo;s interdialytic weight gain calculator shows how a delayed session raises the fluid to be removed next time.</p>
{{key:A dialysis patient has no spare days. Every storm plan starts with one question: when is each patient&rsquo;s next session, and can it come earlier?}}
"""),
        ("power", "Power failure", "Power failure: the first ten minutes", """
<p>Think of the dialysis machine as four devices in one box: a pump, a heater, a mixer, and a set of alarms. When the power fails, all four stop together. The blood in the lines does not know that.</p>
<h3>What stops, and what follows</h3>
<p>When the blood pump stops, the blood in the circuit (Module 5) stands still. Standing blood in contact with the tubing and dialyzer begins to clot, so the chance of returning it falls by the minute. The dialysis fluid stops and cools, and fluid removal stops.</p>
<p>The alarms matter most. The venous air detector and venous line clamp keep air out of the vein. Without power, or once a backup battery runs down, they may not work. Battery time varies by model; ask your technician, and do not assume a figure.</p>
<p>Philippine licensing rules require a standby generator appropriate to the facility&rsquo;s size and a plan for emergencies.[[doh2012]] The Philippine Society of Nephrology (PSN) standard for hemodialysis clinics repeats both.[[psn2024]] A generator still takes time to start and can fail. A Signal No. 4 warning expects a near total loss of power and telecommunications.[[pagasa_tcws]]</p>
<p>Manual blood return is a standard textbook procedure for power failure.[[daugirdas2015]] No trial has compared responses; the order below is established practice, not tested evidence.</p>
{{flow:Power failure: the first ten minutes|Patients first::Walk the floor. Check every patient&rsquo;s airway, consciousness, and access before you look at a machine. Uncover each access and look for bleeding.|Ask for the power status::Ask the technician whether the generator has started, whether it is stable, and how long its fuel will last.|Decide with the charge nurse::Continue on generator power only if the technician confirms it is stable. Wait only as long as your unit&rsquo;s protocol allows. Otherwise begin emergency take-off.|One staff member per patient::Each patient whose blood is being returned has one staff member at the chair, watching the venous line.|Watch the patients::Recheck pressures and ask about cramps, dizziness, and chest pain during the return. Respond per protocol.|Count and record::Account for every patient: time off, method, and blood returned or not returned.|Call::The attending nephrologist and the Medical Director, using the SBAR (Situation, Background, Assessment, Recommendation) format from Module 1.}}
{{formula:<strong>Worked example, illustrative.</strong> Generator runtime (hours) = usable fuel (liters) &divide; fuel use at the expected load (liters per hour). This is arithmetic; the fuel use comes from the generator&rsquo;s data plate and the technician&rsquo;s log.<br>Usable diesel = 120 liters. Fuel use at the unit&rsquo;s usual load = 8 liters per hour.<br>Runtime = 120 &divide; 8 = 15 hours.<br><strong>What it tells you:</strong> roughly how long the fuel supports treatment. <strong>What it does not tell you:</strong> whether the generator will keep running. Fuel use rises with load and poor maintenance, and a refill truck may not arrive during a storm.}}
<p>Ask for this number at the start of every storm shift.</p>
{{call:Stop and call the attending nephrologist and the Medical Director when power cannot be restored within the time your unit&rsquo;s protocol allows, when any patient is unstable, or when blood cannot be returned safely. Follow your unit&rsquo;s protocol while you call.}}
"""),
        ("takeoff", "Emergency take-off", "Emergency take-off: returning the blood by hand", """
<p>Picture a shop owner closing in a hurry before a storm: the cash is still counted and the doors locked in the same order. Speed comes from a fixed order, not from skipping steps.</p>
<p>In a normal take-off, the machine pumps the blood back while the air detector watches the venous line. Without power, a nurse turns the blood pump with a hand crank, and the detector and clamp may not act.[[daugirdas2015]] The operator&rsquo;s eyes now do the detector&rsquo;s job. On some models the battery still runs the blood pump and air detector for a short time; if your unit&rsquo;s protocol uses that window for the return, it is one more reason not to wait.</p>
{{fig:pod30_manual_return}}
<p>Air in the venous line can travel to the heart, lungs, or brain. Blood whose red cells have broken down (hemolysis) carries potassium and free hemoglobin that can harm the heart.[[greenberg2021]] Module 16 covers both, and its rule applies unchanged: do not return blood that may contain air or may be hemolyzed.</p>
<h3>Return the blood, or clamp and cut</h3>
<p>Returning the blood gives back the red cells and volume in the circuit. That is right when the session ends for a cause outside the patient and the circuit is sound. It is wrong when the blood or circuit may be the danger, or when there is no time. Clamp and cut uses a kit to close and separate the lines in seconds, for example after earthquake damage or during a fire. Whichever method is used, a central venous catheter&rsquo;s own clamps are closed before its lines are separated, because an open catheter hub can draw air into a central vein.[[greenberg2021]] The unit decides in advance which method fits which situation, and how fistula needles are secured or removed.</p>
{{fig:pod30_return_or_clamp}}
<h3>What you do during take-off</h3>
<p>The nurses perform the return. You lead and watch the patients.</p>
<ol>
<li>Assign one staff member to each patient being returned, and name who watches the venous line.</li>
<li>Examine the unstable patients first: low pressure, chest pain, or confusion.</li>
<li>Decide with the charge nurse which patients are clamped without return: a clotted circuit, visible air, or possible hemolysis.</li>
<li>Watch for low pressure, cramps, and dizziness as blood goes back. Respond per your unit&rsquo;s protocol.</li>
<li>When every patient is off, confirm that each access has stopped bleeding.</li>
<li>Record each patient&rsquo;s time off, method, volume returned or not returned and why, and condition.</li>
</ol>
<p>Tell the attending nephrologist who was cut short and by how much; their next session may need to come sooner.</p>
{{key:Without power, the operator&rsquo;s eyes replace the air detector. One staff member stays with each patient whose blood is being returned, watching the venous line until the clamp is closed.}}
"""),
        ("water", "Water failure", "When the water fails or turns toxic", """
<p>The water room is the unit&rsquo;s second kidney. Each session, the patient&rsquo;s blood meets a very large volume of dialysis fluid, separated from it only by a thin membrane.</p>
{{formula:<strong>Illustrative arithmetic.</strong> Dialysis fluid per session = dialysis fluid flow (mL per minute) &times; session time (minutes).<br>500 mL per minute &times; 240 minutes = 120,000 mL = 120 liters.<br><strong>What it tells you:</strong> the scale of exposure. A person drinks a few liters a day; a dialysis patient meets about a hundred liters in four hours. <strong>What it does not tell you:</strong> this patient&rsquo;s prescription, which sets the real flow and time.}}
<p>A substance in drinking water must cross the gut, and healthy kidneys clear what gets through. In dialysis, small dissolved substances cross the membrane straight into the blood, and the kidney that would clear them has failed.</p>
{{fig:pod30_water_to_blood}}
<p>Module 6 described the treatment train. Here the point is what happens when a stage fails. Chloramine, a disinfectant in city water, is not removed by reverse osmosis; the carbon beds must remove it. When the carbon is exhausted, chloramine reaches the dialysis fluid and damages red cells, causing hemolysis and anemia.[[ward1996]][[tipple1991]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Event</th><th>What failed</th><th>What patients showed</th><th>What it teaches</th></tr></thead>
<tbody>
<tr><td>Chloramine, one Brazilian unit, 2004</td><td>An exhausted activated carbon column</td><td>Hematocrit and hemoglobin fell across the unit, and recovered within a month after the column was changed, with no change in erythropoietin[[deoliveira2009]]</td><td>Anemia in many patients at once may be a water problem</td></tr>
<tr><td>Fluoride, one United States unit</td><td>A temporary deionization system released the fluoride it had held</td><td>12 of 15 patients in one room fell ill with severe itching and nonspecific symptoms; 3 died of ventricular fibrillation. None of 17 in the next room fell ill[[arnow1994]]</td><td>Illness confined to one room or loop points to that water</td></tr>
<tr><td>Microcystins, Caruaru, Brazil, 1996</td><td>Untreated reservoir water carrying toxins from blue-green algae (cyanobacteria)</td><td>116 of 130 patients had visual disturbance, nausea, and vomiting; 101 met the definition of acute liver failure, and 50 died[[jochimsen1998]]</td><td>Source water and its treatment matter as much as the machines</td></tr>
</tbody></table></div>
<p>Outbreak reports cannot show how often such events happen, only how they first appear.</p>
<h3>Recognize a water event</h3>
<p>Think of the water when more than one patient in a room or shift has similar symptoms: chest or back pain with wine-colored blood in the venous line, anemia across the unit, itching, nausea, headache, visual disturbance, or a cluster of fevers or chills. A water alarm, a failed test, or a lost supply is a water event by definition.</p>
<h3>What the rules require</h3>
<p>Department of Health (DOH) Administrative Order 2013-0003 requires microbiological tests monthly at three points (raw water, product water, and the point of use) and chemical tests at the point of use before opening and every six months. When a test fails, the facility temporarily stops operations until a repeat test complies, disinfects the product water loop, and notifies its patients.[[doh_ao2013_0003]] The current international standard for dialysis water is ISO 23500-3:2024, from the International Organization for Standardization (ISO).[[iso23500_3_2024]]</p>
<p>The regulatory limit for the bacterial count in dialysis water is the one in the DOH order: less than 200 colony-forming units (CFU) per milliliter.[[doh_ao2013_0003]] Accredited water testing laboratories report against this DOH value, and it is the limit that licensing inspectors apply. The PSN standard gives a stricter target of less than 100 CFU/mL.[[psn2024]] Some units adopt the stricter target in their water policy, approved by the Medical Director. A result that meets it also meets the DOH limit; a result above the DOH limit is a failed test.</p>
<p>A dry tank, a cut supply, or a flooded water room stops product water, and treatments stop. The site&rsquo;s water system capacity calculator compares peak demand with what the system makes. Whether water is fit for dialysis is decided by the technician and the Medical Director, not the physician on duty.</p>
{{formula:<strong>Worked example, illustrative.</strong> At 9:20 a.m., two patients in Room B report chest tightness and back pain. One patient&rsquo;s plasma looks pink.<br>Proportion affected = patients with symptoms &divide; patients in the room = 2 &divide; 6 = 33%, on one water loop.<br><strong>What it tells you:</strong> the arithmetic is trivial; the pattern is the alarm. <strong>What it does not tell you:</strong> the cause. A kinked line or one faulty machine can also cause hemolysis.}}
{{flow:Two patients, same symptoms: the water event pathway|Stop the affected treatments::Ask the nurses to stop the blood pump and clamp the lines per protocol.|Do not return the blood::If hemolysis is possible, the blood stays in the circuit (Module 16).|Keep the evidence::Keep the circuits, dialyzers, and dialysis fluid samples. Ask the technician to hold the water room as it is.|Examine everyone on the loop::Not only the two who complained. Ask about pain, itching, nausea, and vision.|Send the sick::Patients with chest pain, signs of hemolysis, or an abnormal rhythm go to the emergency room per protocol, with an electrocardiogram (ECG).|Call at once::The attending nephrologist and the Medical Director. The unit then follows the steps of the DOH water order.}}
{{call:Stop and call the attending nephrologist and the Medical Director at once when two or more patients become ill with similar symptoms in the same shift, when a water alarm or a failed water result is reported, or when the water supply stops. Follow your unit&rsquo;s protocol while you call.}}
{{key:One sick patient is a patient problem. Two sick patients with the same symptoms in the same shift is a water problem until proven otherwise.}}
"""),
        ("building", "Quake, fire, flood", "Earthquake, fire, flood, and evacuation", """
<p>A ship&rsquo;s crew drills the lifeboats on calm days, because in a real sinking people do what they have practiced.</p>
<h3>Typhoon and flood</h3>
<p>Typhoons give warning. PAGASA uses five wind signal levels. At Signal No. 4, winds of 118 to 184 km/h are expected within 12 hours, with a near total loss of power and telecommunications and a likely fall in potable water. At Signal No. 5, electricity, potable water, and telecommunications may be unavailable for prolonged periods.[[pagasa_tcws]]</p>
{{fig:pod30_typhoon_signals}}
<p>A flood that reaches a basement water room or generator ends treatment even when the floor above is dry.</p>
<h3>Earthquake</h3>
<p>Shaking can pull needles out and topple machines. When it stops, check every patient&rsquo;s access for bleeding and every patient&rsquo;s condition first, then the building. Crush injury with acute kidney injury (AKI) belongs to the attending nephrologist and the hospital, though your unit may be asked for emergency sessions. After the 2023 Kahramanmara&#351; earthquake in T&uuml;rkiye, high potassium (hyperkalemia) was the most frequent first reason for dialysis in crush-related AKI at one center, in 61 of 82 patients (74.4%), and outages of power and water hindered treatment (a single-center retrospective study).[[kaya2024]] The International Society of Nephrology (ISN) recommendations for crush victims rest on retrospective analyses, case reports, and expert opinion, and carry no grades by design.[[sever2012]]</p>
<h3>Fire and evacuation</h3>
<p>Follow the unit&rsquo;s evacuation plan and routes. Patients who cannot walk are moved first, by staff assigned in advance. Module 15 covers resuscitation; here the task is to move people.</p>
{{fig:pod30_evacuation_routes}}
<p>The grab bag leaves with the staff; without each patient&rsquo;s dialysis summary, a receiving unit must guess the prescription.</p>
{{fig:pod30_grab_bag}}
<p>Stress raises blood pressure. In 205 hemodialysis patients in Fukushima City, mean pressure before dialysis rose from 148.6/77.5 mm Hg at baseline to 153.1/80.1 mm Hg one week after the 2011 Great East Japan Earthquake.[[tani2014]] This retrospective, single-region study is a reason to recheck pressures after a disaster, not a treatment target.</p>
<h3>What you do</h3>
<ol>
<li>Before your first shift, learn the exits, the assembly point, the take-off kits, the flashlights, and the patient tracking sheet.</li>
<li>During the event, report to the incident lead named in the unit&rsquo;s plan.</li>
<li>Account for every patient and staff member at the assembly point, and record where each patient went.</li>
</ol>
{{key:In an evacuation, count before you treat. Every patient and every staff member is accounted for, and the grab bag leaves the building with you.}}
"""),
        ("priority", "When capacity is cut", "When capacity is cut: who dialyzes first, and what to eat until then", """
<p>A lifeboat with fewer seats than passengers needs rules for who boards first, written on calm days. The patients who become dangerously ill first are those whose closed drain fills fastest or who have the least room.</p>
<div class="table-wrap"><table>
<thead><tr><th colspan="3">Who dialyzes first: set by the unit and the attending nephrologist</th></tr>
<tr><th>Factor a priority list usually weighs</th><th>Why it matters</th><th>What you can find out</th></tr></thead>
<tbody>
<tr><td>Days since the last session</td><td>Water, potassium, and acid build up with time</td><td>Date and time of the last completed session</td></tr>
<tr><td>Residual urine output</td><td>Urine still removes some water and potassium</td><td>The patient or the record</td></tr>
<tr><td>Potassium</td><td>A high level can disturb the rhythm before symptoms</td><td>The last result and its date</td></tr>
<tr><td>Breathlessness or swelling</td><td>Fluid already in the lungs</td><td>A phone call or an examination</td></tr>
<tr><td>Access</td><td>A failing catheter or clotted fistula delays treatment further</td><td>The last session&rsquo;s notes</td></tr>
</tbody></table></div>
<p>A review by Sever and colleagues names fair distribution of limited resources and limiting harm as the core ethical concerns.[[sever2023]] Shortened or less frequent sessions are consensus practice; no trial has tested them or any priority order.</p>
{{formula:<strong>Worked example, illustrative.</strong> Today is Wednesday. Three patients cannot be reached for tomorrow.<br>Patient A: last session Saturday, no urine, last potassium 6.2 mmol/L. Days since the last session = 4.<br>Patient B: last session Monday, weight gain 2.1 kg, passes urine daily. Days = 2.<br>Patient C: last session Monday, catheter with poor flow. Days = 2.<br>A has the longest gap and no residual function, so A is offered the earliest slot; C&rsquo;s catheter is reported to the nephrologist. The real order is set by the unit&rsquo;s priority list and the attending nephrologist.<br><strong>What it tells you:</strong> a starting point. <strong>What it does not tell you:</strong> who is sickest. Sorting is not triage.}}
<p>The site&rsquo;s dialysis continuity planner compares sessions due with staffed chairs, water, power, kits, and partner slots. It shows the gap; it does not decide who goes first.</p>
<h3>What to eat until the next session</h3>
<p>The Kidney Community Emergency Response (KCER) Coalition publishes a three-day emergency kidney diet. It favors low-sodium canned fish, poultry, and vegetables, plain crackers, and bottled water, and lists potatoes and tomatoes as foods not to eat.[[kcer_diet]] The Centers for Disease Control and Prevention (CDC) advises patients to keep numbers for their own unit and another nearby, at least a three-day supply of each medicine, and to follow the emergency diet.[[cdc_emergency2024]]</p>
<div class="table-wrap"><table>
<thead><tr><th colspan="2">Emergency diet card: principles from the KCER sheet; limits set by the unit dietitian</th></tr>
<tr><th>Principle</th><th>For this patient (unit to complete)</th></tr></thead>
<tbody>
<tr><td>Less salt: low-sodium or no-salt-added canned food</td><td>Sodium advice: ______</td></tr>
<tr><td>Avoid high-potassium foods such as potatoes and tomatoes</td><td>Potassium advice: ______</td></tr>
<tr><td>Drink less: fluid builds up without dialysis</td><td>Daily fluid limit: ______</td></tr>
<tr><td>A three-day supply of each medicine and a written list</td><td>Medicines to continue: ______</td></tr>
<tr><td>Numbers for the unit and a partner unit</td><td>Partner unit: ______</td></tr>
</tbody></table></div>
<p>The KCER sheet gives no daily limits; those come from the unit dietitian and the nephrologist. Module 23 adapts the choices to Filipino meals. In a survey of 357 patients after Hurricane Sandy, 26.3% missed dialysis and only 44.3% carried a detailed medication list. Dialysis-specific preparedness was associated with fewer missed sessions (incidence rate ratio 0.91, 95% CI 0.87 to 0.98).[[murakami2015]] Prepared patients may differ in other ways.</p>
<p>Apply the unit&rsquo;s priority list with the attending nephrologist. Never improvise a session length or fluid goal, and write down why each patient was placed where.</p>
{{call:Stop and call the attending nephrologist before any change from the prescribed schedule, session length, or fluid goal, and for any patient who has missed a session and has breathlessness, weakness, palpitations, or a high potassium result. Follow your unit&rsquo;s protocol while you call.}}
"""),
        ("continuity", "Continuity and call card", "Keeping patients dialyzed when the unit cannot open, and the call card", """
<p>Think of a relay team: if one runner falls, the baton must already be within reach of the next. When a unit cannot open, its patients must already be known to another unit.</p>
<p>After Hurricane Katrina, 94 Gulf Coast dialysis facilities closed for at least one week, and existing plans were inadequate to keep patients in care.[[kopp2007]] After Hurricane Sandy, patients in the affected area had higher rates of emergency department visits (4.1% against 2.6% and 1.7% in two comparison groups), hospitalization (4.5% against 3.2% and 3.8%), and death within 30 days (1.83% against 1.47% and 1.60%; the mortality difference was significant against only the first group).[[kelman2015]] These are retrospective comparisons. An Asia-Pacific review adds displacement and post-traumatic stress,[[gray2015]] and renal organizations now coordinate international relief.[[lameire2020]] No Philippine study of dialysis outcomes after a typhoon or flood was found.</p>
<p>The DOH licensing order and the PSN standard expect a written contingency and disaster plan.[[doh2012]][[psn2024]] Know where it is kept. A working plan includes a communication tree, partner-unit agreements, a current patient registry with phone numbers and addresses, and a review after every event.[[sever2023]]</p>
{{flow:Communication tree|Physician on duty::Reports the event and the patients&rsquo; status to the charge nurse at once.|Charge nurse::Confirms the facts and starts the unit&rsquo;s call list.|Attending nephrologist::Decides each patient&rsquo;s plan: shortened session, early session, or transfer.|Medical Director::Decides whether the unit stays open and activates partner-unit agreements.|Partner units::Receive patients with their dialysis summary and medicine list.|Patients::Are reached by phone and text with where and when to go.}}
<p>Record who was treated, cut short, sent elsewhere, or not reached, and hand that list over before you leave. Afterward, take part in the review.</p>
<h3>What is uncertain</h3>
<ul>
<li>Early dialysis rests on retrospective claims data from one hurricane; the association may partly reflect who chose to come early.[[lurie2015]]</li>
<li>Shortened sessions, emergency diets, and priority orders are consensus practice, untested by trials.</li>
<li>The DOH limit (less than 200 CFU/mL) is the regulatory reference for dialysis water and the one testing laboratories report against; whether a unit also holds itself to the stricter PSN target (less than 100 CFU/mL) is set in its water policy.</li>
<li>Machine battery time varies by model; only your technician can tell you.</li>
</ul>
{{flow:Call card: power, water, or building emergency|Recognize::Power: machines on battery or dark, alarms, lights out. Water: two or more patients with the same symptoms, unexplained hemolysis, a water alarm, or a failed result. Building: shaking, smoke, rising water, or an evacuation order.|First 2 minutes::Look at every patient: airway, consciousness, access, and bleeding. Ask for the generator and water status. Assign one staff member to each patient. In a suspected water event, have the affected treatments stopped.|Stop dialysis?::Power: continue on generator only if the technician confirms stable power; otherwise end treatments by the unit&rsquo;s emergency take-off method. Water: stop the affected treatments. Building: disconnect as the evacuation plan directs.|Return the blood?::Yes, by hand, with one person watching the venous line, when the circuit is sound and time allows. Do NOT return the blood if hemolysis is possible, if there is air in the venous line, if the circuit has clotted, or if the building must be left at once. Clamp the lines, close any catheter&rsquo;s own clamps before separating, and keep the circuits.|Call::The attending nephrologist and the Medical Director at once, then the unit&rsquo;s communication tree. Use SBAR (Module 1).|Write::Time of the event, each patient&rsquo;s status, method of disconnection, volume returned or not returned and why, circuits kept, calls made and advice received, where each patient went, and who will contact the patients due tomorrow.}}
{{key:The plan is written before the storm. Your job on the day is to follow it, count every patient, and call early.}}
"""),
    ],
    "debrief": ["""
<p><strong>What do you check and decide in the next ten minutes?</strong> Patients before machines. With a flashlight, you check all twelve for airway, consciousness, access, and bleeding, starting with Mr. Santos, who has the lowest pressure and a catheter. You ask Mr. Aquino when the generator can start. He cannot promise a time, and standing blood will clot. With the charge nurse, you begin emergency take-off rather than wait past what the protocol allows, and you call the attending nephrologist and the Medical Director by SBAR while the nurses work.</p>
<p><strong>Whose blood goes back?</strong> Every patient whose circuit is sound and free of air, including Mr. Santos and Mrs. Reyes, has the blood returned by hand, with one nurse per chair watching the venous line. You would clamp without return for a clotted circuit, air in a line, possible hemolysis, or flood water forcing immediate evacuation.</p>
<p><strong>What do you ask about tomorrow?</strong> Mrs. Reyes is the most urgent patient in the building: she missed Monday, her potassium was 6.8 mmol/L, and she received only 40 minutes. You obtain an ECG and a repeat potassium per protocol, and ask the nephrologist for a plan for her tonight, such as transfer to a running hospital or partner unit. Then you ask whether the unit can open with a basement water room under Signal No. 4, and which partner units can help. If it opens partly, the priority list and the nephrologist set the order; the longest gap, no urine, high potassium, breathlessness, a catheter problem, and today&rsquo;s shortened sessions usually come first. You give the charge nurse a written list of the twelve patients and the dialysis each received.</p>
"""],
    "skills": {"title": "Timed emergency take-off and tabletop disaster drill",
               "intro": "Run this as a drill on a quiet day. Your preceptor calls out events (&ldquo;power failure,&rdquo; &ldquo;two patients ill,&rdquo; &ldquo;evacuate&rdquo;) and plays the charge nurse, while colleagues play the patients.",
               "items": [
                   ("States the location of the exits, the assembly point, the emergency take-off kits, the flashlights, and the patient tracking sheet.", True),
                   ("On &ldquo;power failure,&rdquo; checks every patient&rsquo;s airway, consciousness, and access before looking at the machines.", True),
                   ("Asks the technician for the generator status and expected runtime.", False),
                   ("Assigns one staff member to each patient whose blood is being returned, and names who watches the venous line.", True),
                   ("States the conditions for not returning blood: air in the line, possible hemolysis, a clotted circuit, or immediate evacuation.", True),
                   ("Monitors the patient during manual return, including pressure and symptoms, and responds per protocol.", False),
                   ("On &ldquo;two patients ill with the same symptoms,&rdquo; has the affected treatments stopped per protocol, keeps the circuits and samples, and calls the nephrologist and the Medical Director.", True),
                   ("Accounts for every patient and staff member at the end of the drill.", False),
                   ("Applies the unit&rsquo;s priority list for the next day&rsquo;s sessions with the attending nephrologist, without changing any prescription.", True),
                   ("Gives a patient the unit&rsquo;s approved emergency diet and medicine advice in plain words.", False),
                   ("Writes the event note: times, patients, methods, volumes returned, and calls made.", False),
               ],
               "placement": "Before the next typhoon season, find your unit&rsquo;s disaster plan, the take-off kits, the grab bag, and the partner-unit list. Walk the evacuation route once. Ask the technician for each machine model&rsquo;s battery time and whether it has a hand crank, and review what you found with your preceptor."},
    "quiz": [
        ("Why does a missed session carry more danger than its length suggests?",
         ["The dialyzer clots more easily next time",
          "Fluid is the only substance that builds up",
          "Potassium can reach a dangerous level before the patient feels breathless",
          "Missed sessions lower the blood pressure"], 2,
         "Potassium can disturb the rhythm while the patient still looks well."),
        ("What did the Hurricane Sandy study of early dialysis show?",
         ["An association with lower odds of admission and death, in retrospective claims data",
          "Proof from a randomized trial that it prevents death",
          "No difference in any outcome",
          "More emergency department visits"], 0,
         "The study could not tell who was offered early dialysis and declined, so healthier patients may have come early."),
        ("The power fails at 2:15 p.m. with ten patients on the machines. What do you do first?",
         ["Call the electric company",
          "Restart each machine",
          "Ask the technician about generator fuel",
          "Check every patient&rsquo;s airway, consciousness, and access"], 3,
         "Patients come before machines. Generator status is the second question."),
        ("Why does the blood become harder to return the longer the power is off?",
         ["The dialysis fluid overheats",
          "Standing blood in the tubing and dialyzer begins to clot",
          "The patient&rsquo;s pressure rises",
          "The air detector releases air"], 1,
         "Moving blood resists clotting. A clotted circuit is not returned."),
        ("During manual blood return without power, what replaces the venous air detector?",
         ["A second arterial clamp",
          "A faster crank speed",
          "A staff member watching the venous drip chamber and line until the clamp is closed",
          "The battery alarm"], 2,
         "Without power the detector and clamp may not act. The operator&rsquo;s eyes do their job."),
        ("Mrs. Cruz&rsquo;s session is being ended by hand after a power failure. The nurse sees foam in the venous line. What is right?",
         ["Return the blood slowly",
          "Return it with extra saline",
          "Wait for the generator, then return it",
          "Clamp the lines and do not return the blood"], 3,
         "Air in the venous line means no return. Clamp and keep the circuit."),
        ("Smoke enters the treatment area and the incident lead orders immediate evacuation. How are patients disconnected?",
         ["By the unit&rsquo;s clamp-and-cut method, without returning the blood",
          "By manual return for every patient first",
          "By stopping the pump and leaving the lines connected",
          "By whatever method each nurse prefers"], 0,
         "When the building must be left at once, there is no time to return the blood."),
        ("Two patients in one room report back pain and chest tightness at 9:20 a.m.; one patient&rsquo;s plasma looks pink. Both share a water loop. What do you do?",
         ["Give pain relief and continue",
          "Stop the affected treatments, do not return the blood, keep the circuits, and call the nephrologist and the Medical Director",
          "Return the blood quickly and send both home",
          "Change both dialyzers and restart"], 1,
         "This is a water event until proven otherwise. Possible hemolysis means no return."),
        ("Why can a substance harmless in drinking water poison a dialysis patient?",
         ["Dialysis patients drink more water",
          "Reverse osmosis adds it to the water",
          "The machine&rsquo;s heater concentrates it",
          "It crosses the dialyzer membrane straight into the blood, and the failed kidney cannot clear it"], 3,
         "The patient meets a very large volume of fluid each session, separated from the blood by a thin membrane."),
        ("Over two weeks, hemoglobin falls in many patients in one unit, with no change in medicines. What should you consider?",
         ["Poor diet in everyone",
          "Coincidence",
          "Chloramine reaching the dialysis fluid from exhausted carbon",
          "A laboratory reference range error"], 2,
         "Anemia across a unit is a pattern. A chloramine outbreak showed exactly this."),
        ("A monthly water test fails. Under Department of Health Administrative Order 2013-0003, what must the facility do?",
         ["Temporarily stop operations until a repeat test complies, disinfect the product water loop, and notify patients",
          "Continue and repeat the test next month",
          "Lower the dialysis fluid flow",
          "Treat only patients who pass urine"], 0,
         "The order requires a temporary stop, disinfection, and notification of patients."),
        ("A water laboratory report shows a bacterial count of 150 CFU/mL in product water. How does it read?",
         ["It fails the DOH limit",
          "It meets the DOH regulatory limit of less than 200 CFU/mL, but not the stricter PSN target if the unit&rsquo;s water policy has adopted it",
          "It meets every standard, so no one needs to know",
          "The physician on duty decides whether it passes"], 1,
         "The DOH order sets the regulatory limit at less than 200 CFU/mL, and testing laboratories report against it. The PSN standard gives a stricter target of less than 100 CFU/mL, which a unit may adopt in its water policy; the physician on duty does not choose."),
        ("Only half the chairs can run tomorrow. Mr. Lim has no urine, last dialyzed four days ago, and had a high potassium. Mrs. Uy dialyzed two days ago and passes urine. What is best?",
         ["Give both half a session",
          "Lengthen tomorrow&rsquo;s sessions yourself",
          "Report both to the nephrologist; under a priority list Mr. Lim usually comes first",
          "Let the patients decide"], 2,
         "The longest gap, no residual function, and high potassium usually come first. The list and the nephrologist set the order."),
        ("A patient kept away by a flood asks what to eat until the unit reopens. What do you give?",
         ["Advice to fast",
          "Your own estimate of a daily fluid allowance",
          "Advice to eat tomatoes and potatoes",
          "The unit&rsquo;s approved emergency diet and medicine advice, and a call to the nephrologist if breathless or weak"], 3,
         "Numeric limits come from the unit dietitian and the nephrologist."),
        ("Why does a unit review its response after a typhoon closure?",
         ["Dialysis cannot resume without it",
          "Reviewing each response is how the next one goes better",
          "It replaces the written plan",
          "It assigns blame"], 1,
         "Disaster reviews name the after-event review as a core step that feeds back into the plan."),
    ],
    "terms": [("Emergency take-off", "Ending all treatments quickly and safely because the unit can no longer run them."),
              ("Manual blood return", "Returning the blood in the circuit by turning the blood pump by hand when the machine has no power."),
              ("Clamp and cut", "Closing and separating the lines without returning the blood, for immediate evacuation or unsafe blood."),
              ("Standby generator", "A fuel-powered generator that supplies the unit when the main power fails."),
              ("Water event", "Illness in patients caused by a fault in the water or dialysis fluid."),
              ("Chloramine", "A disinfectant in city water that passes reverse osmosis and damages red cells unless the carbon beds remove it."),
              ("Early dialysis", "A session given ahead of the usual schedule because a disruption is expected."),
              ("Priority list", "The unit&rsquo;s written order for who is dialyzed first when sessions are fewer than patients."),
              ("Grab bag", "A packed bag by the exit holding the patient list, contacts, clamps, kits, and each patient&rsquo;s dialysis summary."),
              ("After-event review", "A structured discussion after an emergency of what worked, what failed, and what the plan must change.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "How patients and units prepare for typhoons, floods, and power cuts."),
                 ("dialysis-water-treatment-systems.html", "How the water room works and what each stage removes."),
                 ("el-nino-heat-dialysis.html", "Water shortage and heat, and what they mean for dialysis patients.")],
    "calcs": ["calc-dialysis-continuity-planner.html", "calc-idwg-fluid.html", "calc-wts-capacity.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
