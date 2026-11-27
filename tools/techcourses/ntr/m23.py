# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 23: Hemodialysis prescription and adequacy.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, for Philippine practice.
Numbers checked against PubMed abstracts (HEMO, Saran 2006, Flythe 2011, Assimon 2016, CONVINCE, Obi 2016, Fernandez Lucas 2025,
TwoPlus protocol) and the KDOQI 2015 statement list with grades. PhilHealth: PC 2024-0023, PHP 6,350 per session from October 9, 2024.
No doses, no order sets. Every case is fictional."""

MODULE = {
 'image_alt': 'A nephrology fellow and an internal medicine resident review a hemodialysis flow sheet beside a patient in a dialysis chair, '
              'with the machine screen showing blood flow and ultrafiltration, in a Philippine dialysis unit.',
 'objectives': [
  '<strong>Intern:</strong> Name the parts of a hemodialysis order (time, frequency, blood flow, dialysate flow, dialyzer, dialysate and '
  'ultrafiltration goal) and report a patient who misses, shortens or cannot tolerate sessions.',
  '<strong>Resident:</strong> Read a dialysis order and interpret a urea reduction ratio (URR) or Kt/V, including the reasons a result may be '
  'falsely low or falsely reassuring, and calculate an ultrafiltration rate.',
  '<strong>Fellow:</strong> Write and adjust a prescription (time, flows, dialyzer, dialysate, ultrafiltration and hemodiafiltration), and use '
  'residual kidney function to decide on incremental or twice-weekly hemodialysis honestly within Philippine cost limits.',
 ],
 'big': """<div class="tc-keyp"><span class="tc-lab">Your role &middot; reader, checker, prescriber</span>The intern reads the order aloud at
handoff, knows what each line means, and reports the patient who missed a session or left early. The resident checks that the order
matches the patient in the chair: the access, the weight, the potassium, the last Kt/V. The fellow writes and changes the prescription
with the attending nephrologist, and explains the dose to the patient and the family in pesos and in hours, not only in numbers.</div>
{{plain:Picture a cloudy aquarium with a filter pump. How clean the water gets depends on three things: how fast the pump moves water
through the filter, how long it runs, and how big the tank is. Run a small pump for a short time in a big tank, and the water stays
cloudy. Hemodialysis works the same way. The dialyzer is the filter, the blood pump and dialysate set its speed, the session length is the
time, and the patient&rsquo;s body water is the tank.}}
<p>The picture has a limit. The body is not one tank. Urea sits in the blood, in the spaces between cells and inside cells, especially
muscle, and it moves between these spaces slowly. The blood is cleaned fast; the cells give up their urea late, so the level rebounds after
the session ends. Urea is also only a marker. It is small, it crosses the membrane easily, and it is not the toxin that makes patients
sick. Larger &ldquo;middle molecules&rdquo; such as beta-2 microglobulin move poorly by diffusion and better by convection. And the filter is
only half the job. The machine must also remove the water the patient drank since the last session, and water removal has its own speed
limit, set by how fast the tissues refill the blood vessels. A session can clean urea perfectly and still leave a patient breathless or
hypotensive.</p>
{{cards:Key numbers|KDOQI 2015 dose target (thrice weekly)::Single-pool Kt/V 1.4 per session, minimum delivered 1.2 (1B)|Schedules other
than thrice weekly (KDOQI 2015)::Standard Kt/V target 2.3 per week, minimum 2.1, counting ultrafiltration and residual function (not graded)|Session
length with residual function under 2 mL/min (KDOQI 2015)::A bare minimum of 3 hours, thrice weekly (1D)|HEMO trial, 1,846
patients::Higher dose (equilibrated Kt/V 1.53 vs 1.16) did not lower mortality (relative risk 0.96)|CONVINCE trial, 1,360
patients::Death 17.3% with high-dose hemodiafiltration vs 21.9% with high-flux hemodialysis, median 30 months|PhilHealth hemodialysis
benefit::Up to 156 sessions a year at PHP 6,350 per session for patients in the PhilHealth Dialysis Database (from October 9, 2024; confirm on
the date of service)}}
<p>Most patients on maintenance hemodialysis in a Philippine unit do well on an ordinary prescription that is actually delivered: full time,
the blood flow the access can give, a high-flux dialyzer and a fluid goal the patient can tolerate. A few are underdialyzed without anyone
noticing, because the Kt/V was drawn wrong, the sessions are short, the catheter recirculates, or the schedule is twice weekly in a patient
who no longer makes urine. Your work is to read the numbers for what they measure, find the gap between the prescribed and the delivered
dose, and write a prescription the patient can live with.</p>
""",
 'case': {'title': 'Twice a week since 2019',
  'html': """<p>It is Tuesday at 10 a.m. in a freestanding hemodialysis unit in San Fernando, Pampanga. Mr. Rogelio Pangilinan, 61, a retired
jeepney dispatcher with diabetes, has dialyzed twice a week, Tuesday and Friday, for four hours, through a left radiocephalic fistula since
2019. The family chose twice weekly because they paid for most sessions themselves. He now passes about a cup of urine a day.</p>
<p>His dry weight is recorded as 62 kg. He arrived today 3.8 kg above it, with a blood pressure of 172/96 mm Hg, crackles at both lung bases
and ankle edema. Pre-dialysis potassium last month was 5.9 mmol/L. He scratches his forearms and says Tuesdays are &ldquo;the hard
days.&rdquo; Last month&rsquo;s single-pool Kt/V, computed from the unit&rsquo;s pre- and post-dialysis urea, was 1.0. The flow sheet shows that
the blood pump ran at the prescribed speed but that two of the last eight sessions ended 30 minutes early because of cramps.</p>
<p>His daughter, an overseas Filipino worker home for two weeks, tells you he was registered in the PhilHealth Dialysis Database last month.
She asks the fellow and you, the resident on the renal rotation, whether he can now come three times a week, and whether that will help.</p>""",
  'questions': ['What does a Kt/V of 1.0 on a twice-weekly schedule mean for Mr. Pangilinan, and what could make it falsely low or falsely reassuring?',
                'What do his weight gains do to his ultrafiltration rate, and what would you change in the session?',
                'What will you propose to the attending nephrologist and the family about frequency now that the benefit covers up to 156 sessions?']},
 'sections': [
  ('kinetics', 'Kinetics', 'Kinetics: what K, t and V really measure', """
<p>Dialysis clears solutes by two mechanisms. In <strong>diffusion</strong>, a solute moves from high to low concentration across the
membrane, from blood into dialysate. Small molecules such as urea and potassium diffuse quickly; large ones barely move. In
<strong>convection</strong>, water is pushed across the membrane by pressure and carries dissolved solutes with it, small and middle-sized
alike. Conventional hemodialysis is mostly diffusion with a little convection from ultrafiltration. Hemodiafiltration adds large-volume
convection.</p>
<p>Kt/V describes the diffusive clearance of urea for one session. <strong>K</strong> is the dialyzer&rsquo;s urea clearance in milliliters per
minute. It rises with blood flow, with dialysate flow and with the size and permeability of the dialyzer, but each step gives less than the
one before, because the membrane can only move so much urea per minute. <strong>t</strong> is the time the blood actually passed through the
dialyzer. <strong>V</strong> is the volume in which urea is distributed, roughly total body water. Kt/V is therefore a ratio: how many times
the patient&rsquo;s body water was cleared of urea in one session.</p>
<p>In practice nobody measures K, t and V separately. The unit draws blood urea before and after the session and uses the fall. The urea
reduction ratio (URR) is the percentage fall. Single-pool Kt/V (spKt/V) corrects the fall for urea generated during the session and for the
water removed, because a patient who loses fluid shrinks V and would otherwise look better cleaned. Daugirdas&rsquo; second-generation
formula is the bedside standard.[[ntr23_3]]</p>
{{formula:<strong>Arithmetic illustration, not a target.</strong> spKt/V = &minus;ln(R &minus; 0.008 &times; t) + (4 &minus; 3.5 &times; R) &times; UF &divide; W, where
R = post-dialysis urea &divide; pre-dialysis urea, t = session length in hours, UF = fluid removed in liters, W = post-dialysis weight in kg.<br>
Pre-urea 30 mmol/L, post-urea 12 mmol/L (R = 0.40), 4 hours, 3 L removed, 62 kg: spKt/V is about 1.00 + 0.13 = 1.13.}}
<p>The single-pool model assumes one tank. The body is several. During the session, urea leaves the blood faster than it can leave the
cells, so the post-dialysis blood sample catches a falsely low level. Within the next 30 to 60 minutes urea flows back from cells into
blood and the level rebounds. Equilibrated Kt/V (eKt/V) corrects for this and is lower than spKt/V; the gap is largest in short, intense
sessions. This is the physiology behind the rule that time matters: a long, gentle session gives the cells time to empty.</p>
<div class="table-wrap"><table><thead><tr><th>What goes wrong</th><th>Mechanism</th><th>How the Kt/V misleads you</th><th>What you check</th></tr></thead><tbody>
<tr><td>Post-dialysis sample drawn after a delay</td><td>Rebound has begun</td><td>Falsely low</td><td>Timing of the draw per unit protocol</td></tr>
<tr><td>Post sample drawn from a line with dialysate or saline</td><td>Sample is diluted</td><td>Falsely high</td><td>Technique: slow the pump, sample from the arterial line</td></tr>
<tr><td>Access recirculation</td><td>Cleaned blood re-enters the arterial needle and is dialyzed again</td><td>Delivered clearance falls; may be read as a falsely high fall at the sampling site</td><td>Needle placement, access flow, stenosis on examination</td></tr>
<tr><td>Catheter that cannot give the prescribed blood flow</td><td>K falls</td><td>Truly low</td><td>Actual pump speed on the flow sheet, arterial pressure alarms</td></tr>
<tr><td>Sessions shortened for cramps, alarms or transport</td><td>t falls</td><td>Truly low, and missed on the day the sample was full length</td><td>Delivered minutes for every session of the month</td></tr>
<tr><td>Clotted or reused dialyzer with lost surface</td><td>K falls</td><td>Truly low</td><td>Dialyzer condition, reprocessing records</td></tr>
<tr><td>Muscle wasting</td><td>V falls, so the same Kt gives a higher Kt/V</td><td>Reassuring number in a malnourished patient</td><td>Weight trend, albumin, protein intake</td></tr>
</tbody></table></div>
<p><strong>What you do at your stage.</strong> The intern learns the parts of the order and notices the patient who leaves early. The resident
reads the month&rsquo;s flow sheets, not only the Kt/V, and compares delivered minutes and blood flow with the order. The fellow asks which of
K, t or V explains a low number before changing anything, because the fix for a failing access is not a bigger dialyzer.</p>
{{key:Before you act on a Kt/V, ask whether it was measured correctly and whether it reflects every session of the month. A good number from
one full session can hide four short ones.}}
{{fig:ntr23_a}}
"""),
  ('adequacy', 'Adequacy', 'Adequacy: what the trials and KDOQI say, and what Kt/V cannot tell you', """
<p>In the 1990s, observational data showed that patients with higher urea clearance lived longer, and the natural next question was whether
pushing the dose higher would save more lives. The Hemodialysis (HEMO) Study answered it. It randomized 1,846 patients on thrice-weekly
dialysis, in a two-by-two factorial design, to a standard or a high dose and to a low-flux or a high-flux dialyzer. The standard-dose group
achieved a URR of 66.3%, spKt/V 1.32 and eKt/V 1.16; the high-dose group 75.2%, 1.71 and 1.53. Death from any cause did not differ: relative
risk 0.96 (95% confidence interval 0.84 to 1.10) for high versus standard dose, and 0.92 (0.81 to 1.05) for high versus low flux.[[ntr23_2]]</p>
<p>HEMO did not show that dose does not matter. It showed that, above the standard dose it delivered, more urea clearance in the same thrice-weekly
schedule did not lower mortality. Below that level, the observational association between low dose and death still stands, and no trial would
now randomize patients to underdialysis.</p>
<p>The Kidney Disease Outcomes Quality Initiative (KDOQI) 2015 guideline translated this into its central dose statement: a target spKt/V of
1.4 per session for patients treated thrice weekly, with a minimum delivered spKt/V of 1.2 (1B).[[ntr23_1]] The target sits above the minimum on
purpose. Delivered dose varies from session to session, so aiming at 1.4 keeps most sessions above 1.2. For schedules other than thrice
weekly, KDOQI suggests a target standard Kt/V of 2.3 volumes per week, with a minimum delivered dose of 2.1, calculated in a way that counts
ultrafiltration and residual kidney function (not graded). Standard Kt/V is a weekly measure that lets schedules of different frequency be
compared; it is not the sum of the session Kt/V values.[[ntr23_1]] KDOQI also recommends a bare minimum of 3 hours per session for patients
with low residual kidney function (less than 2 mL/min) on thrice-weekly dialysis (1D).[[ntr23_1]]</p>
<p><strong>Time is more than a term in the equation.</strong> In the Dialysis Outcomes and Practice Patterns Study (DOPPS), about 22,000 patients
in seven countries, sessions longer than 240 minutes were associated with lower mortality (relative risk 0.81), and every 30 minutes longer
with a 7% lower risk, after adjustment for Kt/V and body size.[[ntr23_4]] This is observational: patients who tolerate longer sessions may be
healthier. But the physiology supports it. Longer sessions remove water more slowly, clear more phosphate and middle molecules, and let
urea leave the cells.</p>
<p><strong>Kt/V is a surrogate.</strong> It measures urea removal, which patients do not feel. What patients feel is breathlessness from fluid,
cramps and post-dialysis fatigue from fast removal, itch, poor appetite and the hours lost every week. Adequate dialysis is the dose that
achieves the urea target <em>and</em> controls volume, blood pressure, potassium, acid and phosphate, <em>and</em> lets the patient eat and live.
The normalized protein catabolic rate (nPCR), derived from the same urea data, estimates protein intake; a falling nPCR in a patient with a
&ldquo;good&rdquo; Kt/V is a warning that V, not K, has changed.</p>
<div class="table-wrap"><table><thead><tr><th>Domain of adequacy</th><th>What you measure</th><th>What it tells you</th></tr></thead><tbody>
<tr><td>Small solute removal</td><td>spKt/V, URR, standard Kt/V for other schedules</td><td>Whether the delivered dose meets the minimum; a surrogate</td></tr>
<tr><td>Volume and blood pressure</td><td>Interdialytic weight gain, pre- and post-dialysis pressure, edema, lungs</td><td>Whether time and frequency are enough to remove fluid safely</td></tr>
<tr><td>Potassium and acid</td><td>Pre-dialysis potassium and bicarbonate</td><td>Long gaps (the weekend, a twice-weekly gap) show here first</td></tr>
<tr><td>Phosphate and middle molecules</td><td>Phosphate, itch, symptoms</td><td>Time-dependent removal that Kt/V does not capture</td></tr>
<tr><td>Nutrition</td><td>nPCR, albumin, weight trend</td><td>Whether a rising Kt/V reflects a shrinking patient</td></tr>
<tr><td>How the patient feels</td><td>Symptoms, recovery time after a session, work and family life</td><td>The outcome that matters most to the patient</td></tr>
</tbody></table></div>
<p><strong>What you do at your stage.</strong> The resident reports a Kt/V below 1.2 on thrice-weekly dialysis and the domain that is failing.
The fellow decides with the attending whether the answer is more time, more blood flow, a better access, more sessions, or a different
modality, and checks whether the patient&rsquo;s symptoms agree with the numbers.</p>
{{key:A Kt/V at target is the floor, not the definition of adequate dialysis. Ask what the patient feels, what the fluid is doing and what the
potassium does after the long gap.}}
{{fig:ntr23_b}}
"""),
  ('prescription', 'Prescription', 'The prescription, line by line', """
<p>A hemodialysis order is a set of choices, each of which changes K, t, V or the water removed. Reading it well means knowing what each line
does physiologically and what limits it in the chair. Doses of heparin and other drugs come from the unit&rsquo;s protocol and the attending;
this section is about what each line is for.</p>
<div class="table-wrap"><table><thead><tr><th>Line of the order</th><th>What it does physiologically</th><th>What limits it</th><th>What you check</th></tr></thead><tbody>
<tr><td>Frequency and time</td><td>Sets t, the length of the interdialytic gap, and the hours over which water is removed</td><td>Cost, transport, chair availability, the patient&rsquo;s life</td><td>Delivered minutes per session; missed sessions</td></tr>
<tr><td>Blood flow</td><td>Raises K, with diminishing returns</td><td>The access: fistula or graft flow, catheter function, needle size</td><td>Actual pump speed and arterial pressure on the flow sheet</td></tr>
<tr><td>Dialysate flow</td><td>Keeps the concentration gradient high along the fibers</td><td>Machine and water capacity; small gains above usual flows</td><td>The machine setting matches the order</td></tr>
<tr><td>Dialyzer</td><td>Surface area and permeability set the maximum K; high-flux membranes remove more middle molecules</td><td>Formulary, cost, reuse policy</td><td>Dialyzer type; reprocessing records if reused</td></tr>
<tr><td>Dialysate sodium</td><td>Sets the sodium the patient leaves with; higher sodium increases thirst and the next weight gain</td><td>Intradialytic hypotension and cramps</td><td>Thirst, weight gain, blood pressure trend</td></tr>
<tr><td>Dialysate potassium</td><td>Sets the gradient for potassium removal; low potassium baths remove faster</td><td>Arrhythmia risk with fast falls, especially on digoxin</td><td>Pre-dialysis potassium, electrocardiogram when indicated</td></tr>
<tr><td>Dialysate calcium and bicarbonate</td><td>Calcium balance and acid correction during the session</td><td>Hypotension, alkalosis, vascular calcification concerns</td><td>Pre-dialysis bicarbonate and calcium, parathyroid hormone (PTH)</td></tr>
<tr><td>Dialysate temperature</td><td>Cooler dialysate tightens vessels</td><td>Patient comfort</td><td>Intradialytic hypotension pattern</td></tr>
<tr><td>Ultrafiltration goal</td><td>Water removed: the weight gain plus intake during the session, toward the dry weight</td><td>Plasma refilling rate</td><td>Ultrafiltration rate in mL/kg/h (next lesson)</td></tr>
<tr><td>Anticoagulation</td><td>Keeps the circuit open so the dose is delivered</td><td>Bleeding risk</td><td>Clotting of the dialyzer; bleeding at needle sites</td></tr>
</tbody></table></div>
<p>KDOQI 2015 recommends biocompatible high-flux or low-flux membranes for intermittent hemodialysis (1B), and both reducing dietary sodium and
adequate sodium and water removal during dialysis (1B).[[ntr23_1]] The Philippine Society of Nephrology (PSN) 2024 hemodialysis guidelines are
the local reference for unit standards; read them alongside your unit&rsquo;s protocol.[[ntr23_12]]</p>
{{flow:When the delivered dose is low|Check the measurement::Timing and technique of the post-dialysis sample. Repeat if doubtful.|Check t::Delivered minutes for every session; why sessions ended early (cramps, alarms, transport, the patient&rsquo;s choice).|Check K::Actual blood flow, arterial and venous pressures, dialyzer clotting, recirculation, needle position.|Check the access::Examine the fistula or catheter; a failing access is the commonest hidden cause.|Check V::Weight trend and nutrition; a shrinking patient can hide a falling Kt.|Then change one thing::More time or frequency first when t or volume is the problem; access work when K is the problem; dialyzer or flow changes only after these.}}
<div class="tc-keyp"><span class="tc-lab">In children</span>Children on hemodialysis need the dose and the fluid removal scaled to a small body: blood
volume limits the circuit, the access limits blood flow, and growth, school and nutrition are outcomes in their own right. Many pediatric units
dialyze more often or longer than adult units, and hemodiafiltration has been studied in children. Read <a
href="attending-pediatric-nephrologist-23-hd-prescription.html">Attending Pediatric Nephrologist, Module 23</a> before covering a child.</div>
<p><strong>What you do at your stage.</strong> The intern reads each line of the order back to the nurse at handoff. The resident checks that
the dialysate potassium matches today&rsquo;s potassium and that the blood flow ordered is one the access can give. The fellow writes the order,
documents the reason for each non-routine choice and reviews it monthly with the attending.</p>
{{key:Every line of a dialysis order changes clearance, the gap or the water removed. If you cannot say which, you are not yet ready to change
it.}}
"""),
  ('uf-dry-weight', 'UF and dry weight', 'Ultrafiltration rate, dry weight and the speed limit on water', """
<p>Module 25 and the Physician-on-Duty modules teach what happens in the chair when the pressure falls. This lesson is about the prescription
that prevents it. The machine removes water only from the blood. The tissues refill the blood vessels from the interstitium, but refilling
has a speed limit that differs between patients and is lower in heart failure, low albumin and autonomic neuropathy. When removal outruns
refilling, blood volume falls, and the heart, the gut and probably the brain receive less blood, often before the blood pressure falls.</p>
<p>The ultrafiltration (UF) rate expresses this speed per kilogram: milliliters removed per hour per kilogram of body weight. It turns a
weight gain into a physiological load.</p>
{{formula:<strong>Arithmetic illustration, not a target.</strong> UF rate = fluid to remove (mL) &divide; session time (hours) &divide; weight (kg).<br>
3,800 mL over 4 hours in a 62-kg patient = about 15.3 mL/kg/h. The same 3,800 mL over 4.5 hours = about 13.6 mL/kg/h. A 2,500 mL gain over 4 hours = about 10.1 mL/kg/h.}}
<p><strong>The evidence.</strong> All of it is observational. In a secondary analysis of the HEMO Study (1,846 patients), UF rates above 13
mL/h/kg, compared with up to 10 mL/h/kg, were associated with higher all-cause and cardiovascular mortality (adjusted hazard ratios 1.59 and
1.71); risk appeared to rise above about 10 mL/h/kg.[[ntr23_5]] In 118,394 patients of a large United States dialysis organization, UF rates above
13 mL/h/kg were associated with higher mortality (adjusted hazard ratio 1.31, 95% confidence interval 1.28 to 1.34), and the association held
across body sizes.[[ntr23_6]] In DOPPS, UF rates above 10 mL/h/kg were associated with more intradialytic hypotension and higher mortality.[[ntr23_4]]
None of these studies shows that lowering the rate saves lives; patients with high gains may differ in diet, adherence and heart function.
But the direction is consistent and the physiology is plausible, so most units treat roughly 10 to 13 mL/kg/h as a rate to stay under.</p>
<p>KDOQI 2015 asks you to prescribe a UF rate for each session that balances euvolemia, blood pressure and clearance while limiting
hemodynamic instability (not graded), and to consider additional sessions or longer sessions for patients with large weight gains, high UF rates,
poorly controlled blood pressure, difficulty reaching dry weight or poor metabolic control (not graded).[[ntr23_1]]</p>
<p><strong>Dry weight</strong> is a clinical judgment: the lowest weight a patient tolerates after dialysis without symptoms or hypotension, with
blood pressure controlled and without edema. It drifts. Patients gain flesh after a good fiesta month and lose it during an infection, so a
dry weight that is never challenged becomes wrong in either direction. The Physician-on-Duty module on dry weight teaches the bedside probe.</p>
<div class="table-wrap"><table><thead><tr><th>Problem</th><th>Physiology</th><th>What you may see</th><th>Prescription levers to discuss</th></tr></thead><tbody>
<tr><td>Large weight gains</td><td>Salt drives thirst; water follows</td><td>UF rate above 13 mL/kg/h, cramps, hypotension late in session</td><td>Diet counseling on salt, dialysate sodium, longer or extra sessions</td></tr>
<tr><td>Long interdialytic gap</td><td>Fluid and potassium accumulate over 3 to 4 days</td><td>The &ldquo;hard day&rdquo; after the long gap</td><td>Thrice weekly where possible; never two long gaps in a row</td></tr>
<tr><td>Dry weight set too low</td><td>Removal beyond refill capacity</td><td>Cramps, hypotension, fatigue after every session</td><td>Raise the target weight; reassess</td></tr>
<tr><td>Dry weight set too high</td><td>Chronic volume excess</td><td>Hypertension, edema, breathlessness, left ventricular hypertrophy</td><td>Probe the dry weight gradually with longer time</td></tr>
<tr><td>Residual urine output</td><td>The kidneys remove part of the daily intake</td><td>Smaller gains</td><td>Protect it: avoid hypotension and nephrotoxins</td></tr>
</tbody></table></div>
{{call:Stop and call the attending nephrologist, per unit protocol, but always ask the attending nephrologist for guidance, when:<ul><li>The
fluid needed to reach dry weight cannot be removed at a UF rate the patient tolerates, and the patient is breathless or hypoxic before the
session.</li><li>Pre-dialysis potassium is high after a missed or shortened session, especially with electrocardiogram changes.</li><li>Sessions
are repeatedly shortened by cramps or hypotension, so the delivered dose is unknown.</li><li>A family asks to reduce frequency for cost in a
patient with little urine output.</li></ul>}}
<p><strong>What you do at your stage.</strong> The intern records the weight before and after, and reports cramps and early terminations. The
resident calculates the UF rate for every session in the month and flags rates above about 13 mL/kg/h. The fellow chooses among salt counseling,
dialysate sodium, longer time, extra sessions and a dry weight review, and writes the reason in the chart.</p>
{{key:Convert every weight gain into a UF rate. When the rate is too fast, the answer is more time or more sessions, not a lower blood
pressure tolerance.}}
"""),
  ('hdf-incremental', 'HDF and incremental HD', 'Hemodiafiltration, incremental dialysis and the twice-weekly reality', """
<p><strong>Hemodiafiltration (HDF)</strong> adds convection to diffusion. A large volume of plasma water is filtered across a high-flux
membrane during the session and replaced with ultrapure fluid made online by the machine. Middle molecules, which diffuse poorly, are carried
across with the water.</p>
<p><strong>The evidence.</strong> The CONVINCE trial randomized 1,360 patients in Europe who had been on high-flux hemodialysis for at least 3
months and were judged able to achieve a convection volume of at least 23 liters per session. Over a median of 30 months, death from any cause
occurred in 118 of 683 patients (17.3%) on high-dose HDF and 148 of 677 (21.9%) on high-flux hemodialysis: hazard ratio 0.77 (95% confidence
interval 0.65 to 0.93).[[ntr23_7]] From these counts, the absolute difference is about 4.6 percentage points over about two and a half years,
or roughly one death prevented for every 22 patients treated. The trial was open-label and enrolled selected patients, most with fistulas
able to deliver high blood flows; the result applies to patients who can reach that convection volume, in units that can make ultrapure
fluid. It does not tell you what HDF does at lower convection volumes or with poor water quality.</p>
<p><strong>Incremental hemodialysis</strong> starts dialysis at less than full dose, usually twice weekly, while residual kidney function still
removes part of the load, and increases the dose as that function falls. KDOQI 2015 states that the dose may be reduced in patients with
significant residual kidney function, provided it is measured periodically to avoid inadequate dialysis (not graded).[[ntr23_1]] Residual function
matters beyond urea: it removes water, potassium, phosphate and middle molecules continuously, every day.</p>
<p>In a United States cohort of 23,645 incident patients, 351 on twice-weekly incremental dialysis, compared with matched thrice-weekly patients,
kept 16% more residual urea clearance and 15% more urine volume. Mortality was not higher in those with residual urea clearance above 3.0
mL/min/1.73 m&sup2; (hazard ratio 0.99), but was higher in those at or below 3.0 (hazard ratio 1.61, 95% confidence interval 1.07 to 2.44).[[ntr23_8]]
This is observational and selected. A Spanish randomized trial of 150 incident patients with residual urea clearance of at least 2.5 mL/min
compared twice-weekly with thrice-weekly HDF and found no difference in the decline of residual function, hospitalizations or mortality over 12
months, with 69.1 versus 122.6 sessions a year; 15 patients moved to thrice weekly after an average of 193 days.[[ntr23_9]] Larger pragmatic trials,
including TwoPlus in the United States, are testing twice-weekly starts with diuretics and other supports in patients with residual function.[[ntr23_10]]</p>
<p><strong>The Philippine reality.</strong> Many Philippine patients have dialyzed twice weekly not because of residual function but because of
cost. That is a different situation. Incremental dialysis is a plan: it requires measured residual function, a timed urine collection or a
reliable urine volume, and a promise to increase the dose when function falls. Twice-weekly dialysis in a patient who passes almost no urine is
not incremental; it is underdialysis by arithmetic, because the KDOQI standard Kt/V minimum of 2.1 per week is hard to reach with two sessions
of ordinary length and no kidney contribution, and the long gaps bring larger weight gains and higher potassium.</p>
<p>PhilHealth Circular 2024-0023 covers up to 156 hemodialysis sessions a year, three a week for 52 weeks, for members and dependents with stage 5
chronic kidney disease registered in the PhilHealth Dialysis Database, at PHP 6,350 per session from October 9, 2024. PhilHealth states that the
package includes items such as anticoagulation, medicines for anemia, laboratory tests, the dialyzer and solutions; confirm the coverage and any
co-payment on the date of service.[[ntr23_11]] For many families the barrier to thrice-weekly dialysis is now transport, lost work and caregiving
rather than the session fee. The benefit makes the physiologic prescription possible; it does not decide it.</p>
<div class="table-wrap"><table><thead><tr><th>Patient</th><th>Residual function</th><th>Reasonable discussion</th></tr></thead><tbody>
<tr><td>New to dialysis, good urine output</td><td>Measured and substantial</td><td>Incremental twice weekly with monitoring, increase when it falls</td></tr>
<tr><td>Twice weekly for years, little urine</td><td>Minimal</td><td>Move to thrice weekly; use the benefit; address transport</td></tr>
<tr><td>Thrice weekly, large gains, high UF rates</td><td>Minimal</td><td>Longer sessions, salt counseling, or extra sessions if possible</td></tr>
<tr><td>Good candidate for HDF, unit can make ultrapure fluid</td><td>Any</td><td>Discuss HDF with its evidence and its limits</td></tr>
</tbody></table></div>
<p><strong>What you do at your stage.</strong> The resident asks every twice-weekly patient how much urine they pass and records it. The fellow
measures residual function before calling a schedule incremental, explains the difference to the family, and helps them use the benefit for the
schedule the physiology needs.</p>
{{key:Twice weekly is a prescription only when residual function is measured and followed. Without urine, it is a cost decision that the
benefit may now let you correct.}}
"""),
 ],
 'debrief': [
  """<p><strong>What the Kt/V means.</strong> A single-pool Kt/V of 1.0 is below the KDOQI minimum of 1.2 even for thrice-weekly dialysis, and on
twice-weekly dialysis with almost no urine the weekly standard Kt/V will be well under the 2.1 minimum. Before acting, check the measurement:
the post-dialysis sample timing, whether it came from a full-length session, the blood flow the fistula actually delivered and any sign of
recirculation or stenosis. Two of eight sessions ended early, so the real monthly dose is lower than the number suggests. His itch, high
potassium and hard Tuesdays agree that he is underdialyzed.</p>""",
  """<p><strong>The weight gains.</strong> A 3.8 kg gain removed over 4 hours in a 62-kg man is a UF rate of about 15 mL/kg/h, above the 13 mL/kg/h
associated with higher mortality in observational studies, and it explains the cramps that shorten his sessions. Tuesday follows the
three-day gap. Lengthening the session lowers the rate; a third session shortens the gap and lowers both the gain and the potassium. Salt
counseling with his family, a review of dialysate sodium and a careful look at his dry weight, since he has crackles and edema, all belong in
the plan.</p>""",
  """<p><strong>The frequency conversation.</strong> Propose to the attending nephrologist that he move to thrice-weekly sessions of full length,
now that he is registered in the PhilHealth Dialysis Database and the benefit covers up to 156 sessions a year; confirm the coverage and any
co-payment with the unit. Explain to his daughter that his kidneys no longer help, so two sessions cannot do the work of three, and that the
change should ease his breathing, itch and Tuesdays. Ask about transport and who will bring him, because that is now the likely barrier.
Recheck the Kt/V, potassium and weight gains after a month.</p>""",
 ],
 'skills': {'title': 'Hemodialysis prescription and adequacy',
            'intro': 'Complete with a preceptor in a dialysis unit or on case records. Sign-off is local.',
            'items': [('Reads a hemodialysis order aloud and explains what each line does physiologically', False),
                      ('Calculates spKt/V from pre- and post-dialysis urea, time, fluid removed and weight, and checks the sampling technique', False),
                      ('Reviews a month of flow sheets for delivered minutes, blood flow and early terminations', False),
                      ('Calculates the ultrafiltration rate for each session and flags rates above about 13 mL/kg/h', False),
                      ('Records residual urine output or a timed urine collection before a schedule is called incremental', False),
                      ('Explains a change in frequency to a patient and family, including the PhilHealth benefit and transport', False)],
            'placement': 'Supervised dialysis unit rotation'},
 'quiz': [
  ('An intern is asked which part of a hemodialysis order sets how long the interdialytic gap is. Which is it?',
   ['The dialysate potassium', 'The frequency and session schedule', 'The dialyzer surface area', 'The blood flow rate'],
   1,
   'Frequency and the days chosen set the gap, which drives weight gain and pre-dialysis potassium. Blood flow and dialyzer size change clearance '
   'per minute, not the gap.'),
  ('A patient on thrice-weekly dialysis has a spKt/V of 1.15. The post-dialysis sample was drawn 40 minutes after the session ended. What is the best interpretation?',
   ['The dose is adequate because the KDOQI minimum is 1.0',
    'The result may be falsely low because urea rebound had begun; repeat with correct timing before changing the prescription',
    'The result is falsely high because rebound raises the post-dialysis urea',
    'The dialyzer must be changed at once'],
   1,
   'Urea rebounds from cells into blood within 30 to 60 minutes, so a late sample overestimates post-dialysis urea and underestimates Kt/V. The KDOQI '
   'minimum delivered spKt/V for thrice-weekly dialysis is 1.2 (1B), not 1.0.'),
  ('A fellow considers starting a new patient on twice-weekly incremental hemodialysis. Which finding most supports this plan?',
   ['A spKt/V of 1.4 on the first session',
    'Measured residual urea clearance above 3 mL/min/1.73 m&sup2; with good urine output, and a plan to remeasure it',
    'The family prefers fewer trips',
    'A high interdialytic weight gain'],
   1,
   'Incremental dialysis depends on residual function. In the Obi cohort, twice-weekly schedules were not associated with higher mortality when residual '
   'urea clearance exceeded 3.0, but were when it was 3.0 or less (hazard ratio 1.61). Preference alone does not make a schedule incremental.'),
  ('A 70-kg patient arrives 4.2 kg above dry weight for a 4-hour session. What is the ultrafiltration rate, and what does observational evidence suggest?',
   ['About 7.5 mL/kg/h; no concern',
    'About 15 mL/kg/h; rates above 13 mL/kg/h are associated with higher mortality, so discuss longer or extra sessions',
    'About 60 mL/kg/h; stop dialysis',
    'About 15 mL/kg/h; randomized trials show that lowering it prolongs life'],
   1,
   '4,200 mL &divide; 4 h &divide; 70 kg is 15 mL/kg/h. HEMO secondary analysis and a cohort of 118,394 patients associated rates above 13 mL/kg/h with higher '
   'mortality. No randomized trial has shown that lowering the rate saves lives, so the last option overstates the evidence.'),
  ('A resident presents CONVINCE at journal club. Which statement is accurate?',
   ['HDF lowered mortality in every patient on dialysis regardless of convection volume',
    'Death occurred in 17.3% with high-dose HDF and 21.9% with high-flux hemodialysis over a median 30 months, in selected patients able to reach at least 23 L of convection per session',
    'The trial was double-blind and enrolled incident patients with catheters',
    'HDF showed no difference in mortality'],
   1,
   'CONVINCE enrolled 1,360 prevalent patients judged able to reach a convection volume of at least 23 L; hazard ratio 0.77. It was open-label, so the '
   'result applies to similar patients in units that can make ultrapure fluid.'),
 ],
 'terms': [('HD', 'Hemodialysis'), ('HDF', 'Hemodiafiltration'), ('URR', 'Urea reduction ratio'),
           ('Kt/V', 'Dialyzer urea clearance (K) times time (t) divided by urea distribution volume (V)'),
           ('spKt/V', 'Single-pool Kt/V'), ('eKt/V', 'Equilibrated Kt/V'), ('stdKt/V', 'Standard (weekly) Kt/V'),
           ('UF', 'Ultrafiltration'), ('KDOQI', 'Kidney Disease Outcomes Quality Initiative'), ('HEMO', 'Hemodialysis Study'),
           ('DOPPS', 'Dialysis Outcomes and Practice Patterns Study'), ('CONVINCE', 'Comparison of high-dose hemodiafiltration with high-flux hemodialysis trial'),
           ('nPCR', 'Normalized protein catabolic rate'), ('PTH', 'Parathyroid hormone'), ('PSN', 'Philippine Society of Nephrology'),
           ('PHP', 'Philippine peso')],
 'readings': [('attending-nephrologist-14-hd-prescription-adequacy.html', 'Attending Nephrologist, Module 14: Hemodialysis prescription and adequacy'),
              ('physician-on-duty-07-dialysis-order-and-dose.html', 'Physician on Duty, Module 7: The dialysis order and dose'),
              ('physician-on-duty-08-dry-weight.html', 'Physician on Duty, Module 8: Dry weight'),
              ('incremental-dialysis.html', 'Incremental dialysis')],
 'calcs': ['calc-dialysis-adequacy-ktv.html', 'calc-dialysis-kinetics.html', 'calc-dialysis-prescription.html', 'calc-hd-adequacy-npcr.html',
           'calc-ultrafiltration-rate.html', 'calc-ufr-ceiling.html', 'calc-dry-weight-estimator.html', 'calc-idwg-fluid.html'],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
