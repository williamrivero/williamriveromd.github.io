# -*- coding: utf-8 -*-
OBJECTIVES = [
    "Trace the blood circuit from access to access and interpret arterial, venous, and transmembrane pressure alarms.",
    "Explain what each dialysate component and each anticoagulation strategy does, and the direction of risk when it is wrong.",
    "Describe correct pre- and post-dialysis urea sampling and the practical ways to raise a low delivered dose.",
    "Assess target weight as a clinical judgment that changes over time, and teach salt and fluid control.",
]
EXTRA = [
    {"after": "physiology", "id": "circuit", "nav": "Blood circuit", "tag": "Physiology in depth", "h2": "The blood circuit, step by step, and what each pressure means",
     "html": """
<p>Picture the circuit as a loop of tubing with one pump in it. Everything before the pump is being pulled, so the pressure there is below zero. Everything after the pump is being pushed, so the pressure there is above zero. Almost every pressure alarm can be reasoned out from that single picture: find which side of the pump the sensor is on, then ask what would make pulling or pushing harder or easier.</p>
<ol>
<li><strong>Arterial needle or catheter limb.</strong> Blood leaves the patient here. &ldquo;Arterial&rdquo; names the direction (away from the patient), not the vessel.</li>
<li><strong>Arterial (pre-pump) pressure monitor.</strong> This sensor sits between the access and the pump. It reads negative because the pump is drawing blood through a narrow needle. The harder it is for the access to supply the blood the pump demands, the more negative the reading becomes.</li>
<li><strong>Blood pump.</strong> A roller pump squeezes the tubing segment forward. The flow shown on the screen is calculated from pump speed; when the arterial pressure is very negative, the tubing does not refill completely and the true flow is lower than the displayed flow.</li>
<li><strong>Dialyzer.</strong> Blood passes through the hollow fibers while dialysate passes around them. Anticoagulant, when ordered, is usually infused before the dialyzer.</li>
<li><strong>Venous drip chamber, air detector, and venous clamp.</strong> The chamber traps air and clots. A detector below it stops the pump and closes the clamp if air or foam is sensed, so that air cannot reach the patient. The detector is never bypassed or disabled during treatment.</li>
<li><strong>Venous pressure monitor and venous needle or catheter limb.</strong> Measured at the drip chamber, this is the pressure needed to push blood back through the return needle into the access. It is positive, and most of it is produced by the resistance of the needle itself.</li>
</ol>
<p>Transmembrane pressure is not measured at one point. The machine calculates it as the difference between the pressure on the blood side and the pressure on the dialysate side of the membrane, which is the force that drives ultrafiltration.</p>
<div class="table-wrap"><table>
<thead><tr><th>Alarm</th><th>What it means</th><th>Likely causes</th><th>First nursing checks</th></tr></thead>
<tbody>
<tr><td>Arterial pressure more negative than the limit</td><td>The pump is asking for more blood than the access is delivering</td><td>Needle tip against the vessel wall or poorly placed; bent arm; kinked or clamped arterial line; clot in the needle or catheter limb; low blood pressure or volume depletion; pump speed too high for the needle size; narrowing on the inflow side of the access</td><td>Look at the patient first: blood pressure and symptoms. Then follow the line from the access to the pump for kinks and clamps, check arm position and the needle site, and reduce pump speed as the unit procedure allows</td></tr>
<tr><td>High venous pressure</td><td>Something is resisting the return of blood</td><td>Kinked or clamped venous line; patient lying on the line or bending the arm; clot in the venous chamber or needle; needle against the wall or infiltrated into tissue (swelling, pain); narrowing on the outflow side of the access, especially if readings rise from session to session</td><td>Check the line and arm position, then the needle site for swelling or pain. Inspect the venous chamber for clots. Stop the pump and call for help if infiltration is suspected</td></tr>
<tr><td>Low venous pressure</td><td>Less resistance or less flow than before</td><td>Line separation or needle dislodgement; blood pump stopped or slowed; fall in blood flow from an arterial problem; clotting in the dialyzer upstream of the sensor</td><td>Look at the access and every connection before touching the machine. Blood on the floor, the sheet, or the chair is checked for immediately</td></tr>
<tr><td>High transmembrane pressure</td><td>The machine needs more force to remove the set amount of fluid</td><td>Fluid goal or time entered incorrectly; hourly rate too high for the dialyzer; fibers clotting, which shrinks the working membrane; kinked dialysate line</td><td>Recheck the fluid goal and time against the order, inspect the dialyzer for dark streaks, confirm that anticoagulation was given as ordered, and report</td></tr>
</tbody></table></div>
<p>Two rules protect patients. First, an alarm is silenced only after its cause has been looked for; resetting repeatedly or widening the limits removes the warning without removing the problem. Second, the venous pressure alarm cannot be relied on to detect venous needle dislodgement (VND). Because the needle itself produces most of the venous pressure, the reading may fall only slightly when the needle slips out of the vein, and the pump can continue to run while blood is lost.[[vnd2008]] This is why the access and connections stay visible for the whole treatment (Module 7).</p>
"""},
    {"after": "circuit", "id": "dialyzer", "nav": "The dialyzer", "tag": "Physiology in depth", "h2": "Inside the dialyzer",
     "html": """
<p>A dialyzer is a plastic casing packed with thousands of hollow fibers, each roughly the width of a human hair. Blood runs through the inside of the fibers; dialysate bathes the outside. The fiber wall is the membrane. Blood enters and leaves through the <strong>end caps</strong>, one at each end of the casing. Dialysate enters and leaves through the two <strong>side ports</strong>. Tracing these four connections by hand is part of every setup, because a dialyzer connected the wrong way loses much of its efficiency.</p>
<p><strong>Countercurrent flow.</strong> Blood and dialysate travel in opposite directions. If they ran the same way, the two fluids would approach the same urea concentration partway down the fibers and the rest of the membrane would do little. Running them in opposite directions means that blood nearing the exit, already low in urea, meets the freshest dialysate, so a concentration difference exists along the whole length. Connecting the dialysate lines so that flow runs in the same direction as the blood measurably lowers clearance without triggering any alarm.</p>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>What it means</th><th>Why the nurse cares</th></tr></thead>
<tbody>
<tr><td>Surface area</td><td>Total membrane area of all fibers</td><td>A larger area gives more clearance at a given flow; the model and size are part of the order</td></tr>
<tr><td>Low-flux membrane</td><td>Small pores; low water permeability</td><td>Removes small solutes well and larger molecules poorly; needs a higher transmembrane pressure for the same fluid removal</td></tr>
<tr><td>High-flux membrane</td><td>Larger pores; high water permeability</td><td>Also removes some larger &ldquo;middle&rdquo; molecules; requires a machine with accurate volumetric fluid control and dialysate of good microbiological quality (Module 8)</td></tr>
<tr><td>Priming volume</td><td>Blood held in the fibers and headers</td><td>Matters most in small adults and children</td></tr>
</tbody></table></div>
<p><strong>Hemodiafiltration</strong> adds deliberate convection. The machine removes a large extra volume of plasma water across a high-flux membrane, dragging larger solutes with it, and replaces that volume with sterile fluid prepared online from the dialysate. It demands a high blood flow, a well-functioning access, and very pure water. Whether it improves survival compared with high-flux hemodialysis (HD) has been studied in randomized trials with differing results, and it is not widely available in the Philippines; the nurse&rsquo;s task where it is used is to follow the machine-specific procedure exactly. Advanced Module 13 covers hemodiafiltration in depth: convection volume, water and fluid quality, the trial evidence, and session care.</p>
<p><strong>Where dialyzers are reprocessed,</strong> each is labeled for one patient only, tested before reuse as the unit procedure specifies, and discarded when it fails the test or reaches the reuse limit. Clotted or lost fibers reduce the working surface area, which is one reason a patient&rsquo;s delivered dose can fall while the prescription stays the same.</p>
"""},
    {"after": "dialyzer", "id": "dialysate", "nav": "Dialysate in depth", "tag": "Physiology in depth", "h2": "Dialysate: what each component does and what goes wrong",
     "html": """
<p>Dialysate is best thought of as a prescribed drug delivered by the liter. The membrane lets each small solute move toward whichever side has less of it, so the level set in the dialysate decides where the patient&rsquo;s blood level ends up. The physician&rsquo;s order and the unit&rsquo;s list of stocked concentrates govern what is used. A wrong concentrate container on the machine is a medication error and is handled and reported as one.</p>
<div class="table-wrap"><table>
<thead><tr><th>Component</th><th>What it does</th><th>If too low</th><th>If too high</th></tr></thead>
<tbody>
<tr><td>Sodium</td><td>Sets the main osmotic balance between blood and dialysate</td><td>Water shifts into cells: cramps, headache, nausea, low blood pressure</td><td>Sodium is loaded into the patient: thirst, larger weight gain before the next session, higher blood pressure</td></tr>
<tr><td>Potassium</td><td>Controls how fast and how far blood potassium falls</td><td>Rapid or excessive fall in blood potassium; observational studies associate very low dialysate potassium with arrhythmia and sudden death, particularly in patients whose pre-dialysis potassium is not high</td><td>Too little removal; pre-dialysis hyperkalemia persists</td></tr>
<tr><td>Calcium</td><td>Determines whether calcium is gained or lost in the session; affects heart contraction and vessel tone</td><td>Low blood pressure, cramps, tingling, rhythm disturbance; stimulates parathyroid hormone over time</td><td>Calcium loading, with concern about deposition in blood vessels</td></tr>
<tr><td>Bicarbonate</td><td>Replaces buffer used up by acid produced between sessions</td><td>Acidosis is not corrected: muscle and bone loss over time</td><td>Alkalosis after dialysis: cramps, tingling, lower ionized calcium and potassium, rhythm disturbance</td></tr>
<tr><td>Magnesium</td><td>Supports nerve, muscle, and heart rhythm stability</td><td>Cramps, arrhythmia</td><td>Weakness, low blood pressure; uncommon with standard concentrates</td></tr>
<tr><td>Glucose</td><td>Prevents loss of glucose into the dialysate</td><td>Hypoglycemia during treatment, especially in patients using insulin or eating poorly</td><td>Higher blood glucose during treatment</td></tr>
<tr><td>Temperature</td><td>Affects vessel tone and the patient&rsquo;s heat balance</td><td>Shivering and discomfort</td><td>Skin vessels dilate and blood pressure falls; seriously overheated dialysate damages red cells, which is why the machine has a temperature alarm</td></tr>
</tbody></table></div>
<p><strong>Sodium.</strong> A dialysate sodium set above the patient&rsquo;s own level can make a session smoother, but the sodium gained drives thirst afterward, and the patient returns heavier. A Kidney Disease: Improving Global Outcomes conference on blood pressure and volume advised against routine sodium loading, including sodium profiles that deliver a net gain.[[flythe2020]]</p>
<p><strong>Potassium.</strong> The dangerous moments are at both ends: the patient who arrives with a high potassium after a long interval, and the patient whose potassium is driven down quickly by a low-potassium bath. The nurse checks that the potassium concentrate hung matches the current order, not last month&rsquo;s, and tells the physician when a recent pre-dialysis result is low or the patient has had vomiting, diarrhea, or poor intake, because the ordered bath may no longer fit.</p>
<p><strong>Calcium.</strong> The international mineral and bone guideline suggests a dialysate calcium between 1.25 and 1.50 mmol/L, a weak recommendation based on limited evidence, to balance the two directions of risk.[[mbd2017]]</p>
<p><strong>Temperature.</strong> Dialysis tends to raise core temperature, and the body responds by opening skin vessels, which works against blood pressure. Modestly cooler dialysate limits this response, and the same conference considered it a reasonable, low-cost option for patients prone to low blood pressure during treatment, while noting that its effect on long-term outcomes was not established.[[flythe2020]] Temperature is changed only by order or unit protocol, and a patient who feels cold is given a blanket with the access left uncovered.</p>
<p><strong>Before starting,</strong> confirm that the acid and bicarbonate concentrates match the order and each other, that the machine has passed its conductivity and temperature self-checks, and that no alarm has been overridden. Conductivity is the machine&rsquo;s running estimate of total dissolved salts, chiefly sodium; a conductivity alarm means the mixture is wrong, and dialysate is automatically diverted away from the dialyzer until it is corrected.</p>
"""},
    {"after": "dialysate", "id": "anticoag", "nav": "Anticoagulation", "tag": "Clinical application", "h2": "Anticoagulation: keeping the circuit open without making the patient bleed",
     "html": """
<p>Blood that touches plastic tubing, a membrane, and air in the drip chambers begins to clot. A clotted circuit shortens the session, lowers clearance, and can cost the patient the blood in the lines, which matters in someone who is already anemic. Anticoagulation is prescribed to prevent this, and the dose is a compromise that the physician resets as the patient&rsquo;s circumstances change.</p>
<div class="table-wrap"><table>
<thead><tr><th>Approach</th><th>How it is given</th><th>Points for the nurse</th></tr></thead>
<tbody>
<tr><td>Unfractionated heparin</td><td>A loading dose at the start, then a continuous infusion or repeated doses</td><td>Short-acting. For fistulas and grafts the maintenance dose is usually stopped before the end of the session, at the time stated in the order, so that needle sites seal. Dose is individualized; never copied from another patient</td></tr>
<tr><td>Low-molecular-weight heparin</td><td>Usually a single dose into the circuit at the start</td><td>Simple to give, but it is cleared by the kidneys and its effect lasts longer; it cannot be &ldquo;stopped early&rdquo; and is only partly reversible. Prolonged bleeding after needle removal is reported</td></tr>
<tr><td>Heparin-free treatment</td><td>No anticoagulant; the circuit is flushed with saline at intervals if the unit protocol includes this</td><td>Used when bleeding risk is high. Watch the circuit closely; keep blood flow as ordered; avoid stopping the pump unnecessarily. Every flush is fluid given and is added to the removal goal</td></tr>
</tbody></table></div>
<p><strong>Assess before every dose.</strong> The order was written for the patient as they were when the physician last saw them. Before giving any anticoagulant, ask and look for what has changed:</p>
<ul>
<li>Active bleeding: gums, nose, black or bloody stools, vomiting blood, heavy menstrual bleeding, new large bruises.</li>
<li>A fall or head injury since the last session, even if the patient feels well.</li>
<li>Surgery, dental extraction, biopsy, or access procedure recently done or planned for today or tomorrow.</li>
<li>New medicines that affect clotting, such as warfarin, antiplatelet agents, or a nonsteroidal anti-inflammatory drug (NSAID).</li>
<li>Very high blood pressure, new severe headache, or visual change.</li>
<li>Prolonged bleeding from needle sites after the previous session.</li>
</ul>
<p>Any of these is a reason to hold the anticoagulant and call the physician before starting, not after. The nurse does not reduce or omit a dose silently; the change is ordered and documented.</p>
<p><strong>Recognizing a clotting circuit.</strong> Signs appear in a typical order: the blood in the lines looks darker; dark streaks appear along the dialyzer fibers after a saline flush; clots or foam collect in the drip chambers; then pressures change, with a rising transmembrane pressure and, if the venous chamber or needle is clotting, a rising venous pressure. Acting on the early signs, by reporting and following the unit protocol, may save the circuit. Once clotting is advanced, the blood is not returned, because clots could be pushed into the patient; the estimated blood loss is documented and reported.</p>
<p><strong>Heparin-induced thrombocytopenia.</strong> In a small number of patients, heparin triggers antibodies that activate platelets. The platelet count falls, typically some days after heparin exposure begins, and the danger is clotting, not bleeding. A falling platelet count, unexplained clotting of the circuit or the access, or skin changes at injection sites are reported promptly. If the diagnosis is suspected, all heparin is stopped by order, and that includes heparin used to lock catheters and to flush lines.</p>
"""},
    {"after": "evidence", "id": "measuring", "nav": "Measuring adequacy", "tag": "Evidence", "h2": "Measuring adequacy properly, and what to do when it is low",
     "html": """
<p>An adequacy result is only as good as the two blood samples behind it. Both come from the same session, and each has its own typical error.</p>
<p><strong>The pre-dialysis sample</strong> must be undiluted blood taken before treatment begins. From a fistula or graft it is drawn from the arterial needle before any saline or heparin has passed through it. From a catheter, the locking solution and an additional discard volume are withdrawn first, as the unit procedure specifies. A sample diluted with saline gives a falsely low starting urea, which makes the dose look smaller than it was.</p>
<p><strong>The post-dialysis sample</strong> is harder, because three things distort urea at the end of a session. Blood that has just been cleaned may recirculate through the access and be sampled again. Dialysis continues for as long as dialysate is flowing, so the timing drifts. Once treatment stops, urea moves back from the tissues into the blood (rebound). The accepted methods deal with the first two by sampling at the end of the prescribed time, with ultrafiltration (UF) stopped, after either slowing the blood pump for a short interval or stopping dialysate flow for a short interval, and then drawing from the arterial sampling port. The exact steps and timings are those of the unit&rsquo;s written method, and every nurse in the unit uses the same one so that results can be compared month to month. The most damaging error is drawing the sample after the saline rinse-back has begun: diluted blood gives a falsely low urea and a falsely reassuring result.</p>
<p><strong>Urea reduction ratio.</strong> The calculation is (pre-dialysis urea − post-dialysis urea) ÷ pre-dialysis urea × 100. <em>Example for teaching only:</em> pre-dialysis blood urea nitrogen (BUN) 70 mg/dL and post-dialysis 21 mg/dL gives (70 − 21) ÷ 70 × 100 = 70%. The same arithmetic works in mmol/L.</p>
<p><strong>What Kt/V adds.</strong> The ratio ignores two things: urea carried out with the fluid removed, and urea the body makes during the session. The widely used second-generation formula corrects for both using the session length, the UF volume, and the post-dialysis weight.[[daugirdas1993]] In practice, two patients with the same ratio have different Kt/V values if one had much more fluid removed. Accurate treatment time and accurate pre- and post-dialysis weights on the record are therefore part of the laboratory result.</p>
<p><strong>Residual kidney function.</strong> Urine still made by the patient&rsquo;s own kidneys clears urea and, more importantly, fluid and larger solutes around the clock. The Kidney Disease Outcomes Quality Initiative (KDOQI) guideline allows the dialysis dose to be adjusted for substantial residual function provided it is measured periodically, because it declines over time.[[hd2015]] Ask about urine volume regularly, carry out timed urine collections when ordered, and help protect what remains by flagging NSAID use and repeated low blood pressure during treatment.</p>
<p><strong>How often.</strong> Guideline-based programs measure delivered dose about monthly, and again after a change in prescription or access. Where patients pay for their own tests, the interval may be longer; the unit policy states the minimum.</p>
<div class="table-wrap"><table>
<thead><tr><th>Way to raise delivered dose</th><th>Why it works</th><th>Limits and nursing points</th></tr></thead>
<tbody>
<tr><td>Deliver the full prescribed time; extend time</td><td>Time multiplies clearance directly and also helps fluid and phosphate removal</td><td>The most reliable measure. Record minutes lost to late starts, alarms, and early sign-off</td></tr>
<tr><td>Higher blood flow</td><td>More blood presented to the membrane each minute</td><td>Only if the access delivers it without a very negative arterial pressure; gains flatten at higher flows</td></tr>
<tr><td>Higher dialysate flow</td><td>Keeps the concentration difference steep</td><td>Modest gain; uses more water and concentrate</td></tr>
<tr><td>Larger or more efficient dialyzer</td><td>More membrane area</td><td>By order; check reprocessed dialyzers are still within the unit&rsquo;s test limits</td></tr>
<tr><td>Needle size and placement</td><td>A larger-bore needle supports the ordered flow at safer pressures; needles well apart and correctly oriented limit recirculation</td><td>Needle size is matched to blood flow by the unit chart; check lines are not reversed</td></tr>
<tr><td>Access function</td><td>A narrowed access cannot supply the flow and recirculates</td><td>Report rising venous pressures, falling achievable flow, or prolonged bleeding for access review (Module 7)</td></tr>
<tr><td>Prevent clotting</td><td>Clotted fibers are lost membrane</td><td>Review anticoagulation with the physician if dialyzers are streaked</td></tr>
</tbody></table></div>
<p><strong>What urea adequacy does not capture.</strong> A passing Kt/V says nothing about phosphate, which leaves the tissues slowly and depends mainly on hours of treatment; about fluid status and blood pressure; about larger retained molecules; or about how the patient feels. Appetite, itch, sleep, and the time it takes to recover after a session are asked about directly, and a long recovery time is worth reporting even when the numbers look acceptable.</p>
"""},
    {"after": "bedside", "id": "dryweight", "nav": "Target weight", "tag": "Clinical application", "h2": "Target weight: a clinical judgment that keeps moving",
     "html": """
<p>Target weight is not measured; it is estimated, tested, and revised. It is the lowest post-dialysis weight the patient tolerates without symptoms of too little fluid and without signs of too much. The physician sets it, but the nurse who sees the patient three times a week supplies most of the evidence.</p>
<div class="table-wrap"><table>
<thead><tr><th>Suggests the target is too high (fluid left behind)</th><th>Suggests the target is too low (too much removed)</th></tr></thead>
<tbody>
<tr><td>Blood pressure high before and after dialysis</td><td>Low blood pressure late in the session or on standing afterward</td></tr>
<tr><td>Ankle, sacral, or facial edema; raised neck veins</td><td>Cramps, especially in the last hour</td></tr>
<tr><td>Breathlessness lying flat or at night; crackles at the lung bases</td><td>Dizziness, yawning, nausea, ringing in the ears</td></tr>
<tr><td>Target reached easily with no symptoms and blood pressure still high</td><td>Marked fatigue and a long recovery after treatment; hoarse voice, thirst</td></tr>
</tbody></table></div>
<p>No single sign is reliable. Edema can be absent with several liters of excess fluid, and low blood pressure during dialysis can occur in a patient who is still overloaded, because the problem is the speed of removal and not the total.</p>
<p><strong>Why it changes.</strong> The scale cannot tell fluid from flesh. After an infection, a hospital stay, or weeks of poor appetite, the patient loses muscle and fat. If the target is left unchanged, fluid quietly fills the gap: the patient &ldquo;reaches target&rdquo; while becoming hypertensive and breathless. The opposite happens when appetite returns and the patient gains real weight: the old target now demands removal of fluid that is not excess, and cramps and low blood pressure appear. Report a change in appetite, a recent illness, looser or tighter clothing, and any new pattern of symptoms, with a clear statement that the target weight may need review.</p>
<p><strong>Probing.</strong> When the target is thought to be too high, the physician lowers it in small steps over several sessions while the team watches blood pressure and symptoms. Large single reductions cause the complications that make patients distrust fluid removal. The nurse&rsquo;s documentation of how each step was tolerated is what allows the next step.</p>
<p><strong>Weight gain between sessions</strong> is judged against body size. Three kilograms is 6% of body weight for a 50 kg patient and under 4% for an 80 kg patient, and the hourly rate per kilogram needed to remove it differs in the same proportion. Because the gain is almost entirely driven by salt intake and the thirst that follows, teaching concentrates on sodium, not on willpower about water: fish sauce, soy sauce, shrimp paste, bouillon cubes, instant noodles, dried and salted fish, canned and processed meats, and salty snack foods. Salt substitutes are avoided because most contain potassium. A patient who suddenly gains very little may simply be eating poorly, which is a nutritional warning and not a success.</p>
<p><strong>Weighing accurately.</strong> Use the same scale before and after, with similar clothing, shoes off, and pockets empty; account for wheelchairs, prostheses, and heavy casts the same way each time. An error of half a kilogram on the scale is half a liter in the fluid goal.</p>
<p><strong>Adjunct tools.</strong> Lung ultrasound, which counts artifacts produced by fluid in the lungs, and bioimpedance, which estimates body water from electrical resistance, can support the clinical assessment where available. The same international conference regarded them as promising aids whose effect on patient outcomes still needed confirmation, not as replacements for examination.[[flythe2020]]</p>
<p><strong>When sessions will be missed.</strong> Typhoons, floods, and transport failures interrupt dialysis in the Philippines every year. Patients are taught in advance, following the unit&rsquo;s emergency plan, to tighten salt, fluid, and potassium intake when a session is likely to be delayed, and to contact the unit early instead of waiting until they are breathless.</p>
"""},
]
QUIZ = [
    {"stem": "Ninety minutes into treatment, a patient with a forearm fistula turns onto his side to sleep, and the high venous pressure alarm sounds. The blood pump has stopped. He is comfortable, and his blood pressure is unchanged. What should the nurse do first?",
     "options": [
         ("Press reset and raise the upper venous pressure limit so that he can sleep", False, "Widening a limit removes the warning without finding the cause, and a persisting obstruction can clot the circuit or mask an infiltration."),
         ("Give a saline bolus through the circuit", False, "Saline does not relieve an obstruction to blood return and adds fluid that must then be removed."),
         ("Remove the venous needle and recannulate at a new site", False, "This may eventually be needed, but only after simple external causes and the needle site have been checked."),
         ("Check the venous line for a kink or compression under his arm or body, then inspect the needle site for swelling or pain", True, "A sudden high venous pressure after a position change is most often a kinked or compressed line or a bent arm. The site is then examined for infiltration before the pump is restarted."),
     ],
     "objective": "Trace the blood circuit from access to access and interpret arterial, venous, and transmembrane pressure alarms.", "sources": ["anna7"], "flag": "Alarm limits and restart steps follow the machine manual and unit procedure."},
    {"stem": "A new nurse draws the post-dialysis urea sample from the arterial port two minutes after the saline rinse-back has started. The pre-dialysis sample was drawn correctly. How will this affect the reported adequacy?",
     "options": [
         ("The post-dialysis urea will be falsely low, so the urea reduction ratio and Kt/V will look better than the dose actually delivered", True, "Saline dilutes the sample. A falsely low post-dialysis urea overstates the fall in urea and can hide under-dialysis."),
         ("The post-dialysis urea will be falsely high, so adequacy will look worse than it was", False, "Dilution lowers the measured urea; it does not raise it."),
         ("There will be no effect, because urea is unaffected by saline", False, "Saline contains no urea, so mixing it with blood lowers the measured concentration."),
         ("Only the pre-dialysis value is used in the calculation, so the error does not matter", False, "Both values are required; the result depends on the ratio between them."),
     ],
     "objective": "Describe correct pre- and post-dialysis urea sampling and the practical ways to raise a low delivered dose.", "sources": ["hd2015", "daugirdas1993"], "flag": "The unit's written sampling method governs the exact steps and timings."},
]
TERMS = [
    ("Transmembrane pressure", "The pressure difference between the blood side and the dialysate side of the membrane; the force that drives ultrafiltration."),
    ("Countercurrent flow", "Blood and dialysate running in opposite directions through the dialyzer so that a concentration difference is kept along its whole length."),
    ("High-flux membrane", "A membrane with larger pores and high water permeability that also removes some larger molecules."),
    ("Hemodiafiltration", "Hemodialysis combined with large-volume convection, with the removed fluid replaced by sterile solution."),
    ("Conductivity", "The machine's electrical measure of total dissolved salts in the dialysate, used to confirm correct mixing."),
    ("Rebound", "The rise in blood urea after dialysis stops as urea moves back from the tissues into the bloodstream."),
    ("Residual kidney function", "The clearance and urine volume still provided by the patient's own kidneys."),
]
FLAGS = [
    "Pressure alarm limits, permitted pump-speed changes, and restart steps are machine- and policy-specific; the alarm table gives reasoning, not settings.",
    "Heparin and low-molecular-weight heparin doses, stop times, and saline flush volume and interval for heparin-free treatment are by order and unit protocol; none are quantified.",
    "Post-dialysis sampling: slow-flow and stop-dialysate-flow methods are described in principle only; confirm the unit's written method and timings.",
    "Monthly adequacy measurement reflects KDOQI practice; confirm the interval required by unit policy and local payer rules.",
    "Statement that very low dialysate potassium is associated with arrhythmia and sudden death is from observational literature and is not tied to a listed reference; reviewer to confirm wording or add a source.",
    "Hemodiafiltration paragraph states that randomized trials have had differing results without citing them (no reference added); reviewer may wish to add a verified source.",
    "Dialysate calcium range of 1.25 to 1.50 mmol/L is the KDIGO 2017 suggestion; confirm against the unit's stocked concentrates.",
    "Advance instructions for missed sessions (typhoon, flood) must come from the unit's own emergency plan and the nephrologist.",
]
