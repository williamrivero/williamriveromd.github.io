# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 27: Peritoneal dialysis principles and prescription.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, for Philippine practice.
Numbers checked against PubMed abstracts (Rippe 1993, Brimble 2006, Bargman 2001, ADEMEX, Lo 2003, Htay 2018 and 2020) and the
ISPD 2020 open-access text. ISPD 2020 statements are practice points, not graded. No doses, no solution regimens. Every case is fictional."""

MODULE = {
 'image_alt': 'A nephrology fellow and a peritoneal dialysis nurse hold up a drained overnight bag against the light with a patient at home, '
              'comparing its volume with the exchange record, in a Philippine house.',
 'objectives': [
  '<strong>Intern:</strong> Explain in plain words how a peritoneal dialysis (PD) exchange works, record fill and drain volumes, weight and urine '
  'output correctly, and report cloudy effluent, pain or a falling drain volume.',
  '<strong>Resident:</strong> Explain PD transport with the three-pore model, read an exchange record and a peritoneal equilibration test (PET), and '
  'separate membrane causes of poor ultrafiltration from mechanical and adherence causes.',
  '<strong>Fellow:</strong> Prescribe continuous ambulatory PD (CAPD) or automated PD (APD) to goals that the patient sets with the team, assess adequacy '
  'without chasing an arbitrary clearance number, protect residual kidney function, and run urgent-start PD safely.',
 ],
 'big': """<div class="tc-keyp"><span class="tc-lab">Your role &middot; the clinician who sees PD from the ward</span>Most PD patients are seen
by trainees only when they are admitted. The intern records every exchange and every drain volume and knows that a cloudy bag is an emergency.
The resident reads the exchange record and asks why the drain volumes changed before ordering anything. The fellow writes the prescription with
the PD nurse and the attending nephrologist, explains it in terms of the patient&rsquo;s day, and makes sure the solution supply reaches the house.</div>
{{plain:Think of the peritoneum as a large, living tea bag. Fresh fluid sits in the belly; waste molecules from the blood steep out into it, and
glucose in the fluid draws water across like sugar drawing juice from fruit. Drain the tea, add fresh water, and the steeping starts again.}}
<p>The picture has a limit. A tea bag is passive; the peritoneum is a living capillary bed. Glucose does not stay in the belly: it is absorbed
into the blood, so the osmotic pull fades through the dwell, and in some patients it fades within a few hours. Water and solutes cross by
different pathways, so water can move without sodium. And the membrane changes with time, inflammation and every episode of peritonitis. A PD
prescription is therefore a match between the patient&rsquo;s membrane, the residual kidney function that still works beside it, and the life
the patient wants to live.</p>
{{cards:Key numbers|ADEMEX trial, 965 patients::Higher peritoneal clearance did not improve survival (relative risk 1.00)|Hong Kong trial, 320 CAPD patients::No survival difference across total Kt/V targets of 1.5&ndash;1.7, 1.7&ndash;2.0 and above 2.0|CANUSA reanalysis, 601 patients::Each 250 mL more urine a day associated with 36% lower risk of death; peritoneal clearance not associated|PET and mortality (meta-analysis, 19 studies)::Risk ratio 1.15 for each 0.1 rise in 4-hour dialysate-to-plasma creatinine|ISPD 2020::No survival advantage in aiming routinely for weekly Kt/V above 1.7 (practice point)|Neutral-pH low-GDP solutions (Cochrane, high certainty)::About 114 mL/day more urine preserved}}
<p>Most PD patients do well on a prescription built around their own day, with enough drain volume to keep them euvolemic and enough residual
function to carry part of the load. A few run into trouble because the membrane transports fast, the urine output falls, the catheter drains
poorly or the exchanges are skipped. Your work is to read the drain volumes like a vital sign, find which of these is happening, and adjust the
prescription to the person rather than to a number.</p>
""",
 'case': {'title': 'The overnight bag that came back small',
  'html': """<p>It is Monday morning in the medical ward of a tertiary hospital in Zamboanga City. Mr. Nasser Abubakar, 47, a fish vendor with
hypertensive kidney disease, started CAPD six weeks ago with four daytime and overnight exchanges, using the lowest-strength glucose bags. The PD
catheter was placed by a surgeon eight weeks ago and the training went well.</p>
<p>He is admitted for leg edema, breathlessness when lying flat and a blood pressure of 168/100 mm Hg. He is 3 kg above his weight at the end of
training. His exchange record shows that his daytime exchanges each drain about 150 to 200 mL more than he fills, but his 10-hour overnight bag
drains about 300 mL <em>less</em> than he filled. His urine output has fallen from about 800 mL a day at the start of PD to about 400 mL. He has
been constipated for a week. The effluent is clear. A PET done in week four shows a 4-hour dialysate-to-plasma creatinine ratio of 0.85, which the
unit&rsquo;s reference classifies as high transport.</p>
<p>His wife says the solution delivery from Manila was delayed by a storm two weeks ago, and for three days he did only three exchanges to save
bags. The fellow asks you, the resident, to work out what is happening before the attending&rsquo;s round.</p>""",
  'questions': ['Why does his overnight bag come back smaller than it went in, while his daytime bags drain more?',
                'What else must you exclude before blaming the membrane, and what does the PET add?',
                'What would you propose to change, and how will you protect his residual kidney function within his supply and benefit limits?']},
 'sections': [
  ('membrane', 'The membrane', 'The membrane: three pores, two forces and a fading gradient', """
<p>The peritoneum lines the abdominal wall and the organs, and its capillaries are the real dialysis membrane. Between the blood in those capillaries
and the fluid in the cavity lie the capillary wall, the interstitium and the mesothelium. The capillary wall decides almost everything, and the
three-pore model describes it.[[ntr27_1]]</p>
<div class="table-wrap"><table><thead><tr><th>Pathway</th><th>Size and share</th><th>What crosses</th><th>What it means at the bedside</th></tr></thead><tbody>
<tr><td>Small pores</td><td>Radius about 40&ndash;55 &Aring;; about 99% of the pore area and about 90% of the ultrafiltration coefficient</td><td>Water with small solutes: urea, creatinine, potassium, glucose, sodium</td><td>Most clearance and most fluid removal</td></tr>
<tr><td>Large pores</td><td>Radius about 250 &Aring;; about 0.01% of pores</td><td>Proteins, including albumin</td><td>Protein loss into the effluent; increases with inflammation</td></tr>
<tr><td>Ultrasmall (water-only) pores</td><td>About 2% of the ultrafiltration coefficient</td><td>Water only, driven by the glucose gradient</td><td>Water without sodium early in a dwell (sodium sieving)</td></tr>
</tbody></table></div>
<p>The water-only pathway was later attributed to aquaporin-1 channels in the capillary endothelium. Because water crosses there without sodium,
the dialysate sodium falls in the first hour of a hypertonic dwell, then rises as sodium diffuses back. This &ldquo;sodium sieving&rdquo;
explains why short, frequent dwells, as in some APD prescriptions, can remove water but relatively little sodium, and why blood pressure can stay
high on a prescription that looks wet enough.</p>
<p><strong>Two forces.</strong> Solutes move by <em>diffusion</em> down their concentration gradient, fast at the start of a dwell and slower as the
dialysate approaches the plasma concentration. Water moves by <em>osmosis</em>: glucose in the dialysate draws water across the small pores and the
aquaporins. But glucose is a small molecule, so it diffuses <em>out</em> of the dialysate into the blood through the same small pores. As it is
absorbed, the osmotic gradient fades. Meanwhile lymphatics and the tissues reabsorb fluid from the cavity at a roughly steady rate. Net
ultrafiltration rises early, peaks, and then falls; in a long dwell it can become negative, so the drain volume is smaller than the fill.</p>
<p>The speed at which this happens depends on the <strong>transport status</strong>. In a high transporter, a large effective capillary surface
lets creatinine equilibrate quickly, which is good for clearance, but glucose is absorbed just as quickly, so the osmotic gradient is lost early
and long dwells drain poorly. In a low transporter the opposite holds: water is removed well over long dwells, but small-solute clearance is
slower. Icodextrin, a glucose polymer too large for the small pores, draws water by colloid osmosis and is absorbed slowly through lymphatics, so
it keeps working through a long dwell.</p>
{{formula:<strong>Arithmetic illustration, not a target.</strong> Net ultrafiltration of one exchange = drain volume &minus; fill volume.<br>
Day exchange: fill 2,000 mL, drain 2,180 mL = +180 mL. Overnight 10-hour dwell: fill 2,000 mL, drain 1,700 mL = &minus;300 mL.<br>
Daily net peritoneal ultrafiltration = sum of all exchanges (for example, 3 &times; 180 &minus; 300 = +240 mL), plus urine output for total fluid removal.}}
<p><strong>What you do at your stage.</strong> The intern records fill and drain volumes for every exchange, not only &ldquo;drained
well.&rdquo; The resident computes net ultrafiltration per exchange and sees which dwell is failing. The fellow links the failing dwell to
transport status and chooses whether to shorten it, change the solution or move it to a machine.</p>
{{key:Read drain volumes exchange by exchange. A long dwell that drains less than it was filled is the membrane telling you how fast it
absorbs glucose.}}
{{fig:ntr27_a}}
"""),
  ('prescription', 'Prescription', 'Writing a prescription around a person', """
<p>A PD prescription has a small number of levers. Each one acts on the physiology of the last lesson. The solution strengths, volumes and number
of exchanges for a given patient come from the unit&rsquo;s protocol, the PD nurse and the attending nephrologist; this lesson is about what each
lever does.</p>
<div class="table-wrap"><table><thead><tr><th>Lever</th><th>Physiology</th><th>Gain</th><th>Cost</th></tr></thead><tbody>
<tr><td>Fill volume</td><td>More fluid keeps the concentration gradient longer and wets more membrane</td><td>Clearance</td><td>Abdominal pressure: discomfort, breathlessness, leaks, hernias</td></tr>
<tr><td>Number of exchanges</td><td>More fresh gradients per day</td><td>Clearance and ultrafiltration</td><td>Time, bags, cost, burden; more connections</td></tr>
<tr><td>Dwell length</td><td>Short dwells catch the early peak of ultrafiltration; long dwells allow equilibration</td><td>Matched to transport status</td><td>Short dwells remove less sodium (sieving)</td></tr>
<tr><td>Glucose strength</td><td>Steeper osmotic gradient</td><td>Ultrafiltration</td><td>Glucose absorption: weight gain, hyperglycemia, lipids, membrane injury over time</td></tr>
<tr><td>Icodextrin for the long dwell</td><td>Colloid osmosis, slow absorption</td><td>Sustained ultrafiltration in long dwells</td><td>Cost and availability; interference with some glucose meters</td></tr>
<tr><td>Neutral-pH, low glucose-degradation-product solutions</td><td>Less toxic to the membrane</td><td>Preservation of residual function and urine volume</td><td>Cost and availability</td></tr>
<tr><td>CAPD versus APD</td><td>Manual daytime exchanges versus a cycler at night with short dwells</td><td>APD frees the day, suits high transporters</td><td>Machine, electricity, cost; short dwells and sodium sieving</td></tr>
</tbody></table></div>
<p><strong>The evidence on solutions.</strong> A Cochrane review of 42 randomized trials found, with high certainty, that neutral-pH, low
glucose-degradation-product (GDP) solutions improved preservation of residual kidney function (about 0.54 mL/min/1.73 m&sup2; higher glomerular
filtration rate) and residual urine volume (about 114 mL/day more). With moderate certainty, icodextrin reduced episodes of uncontrolled fluid
overload (risk ratio 0.30) and increased peritoneal ultrafiltration (about 449 mL/day more). Effects on peritonitis, technique survival and patient
survival remain uncertain.[[ntr27_8]] These outcomes are partly surrogates: residual function and urine volume matter because they are associated
with survival, as the next lesson shows.</p>
<p><strong>Goal-directed prescribing.</strong> The International Society for Peritoneal Dialysis (ISPD) 2020 recommendations changed the question
from &ldquo;what Kt/V does this patient need?&rdquo; to &ldquo;what goals does this person have, and what prescription meets them with the least
burden?&rdquo; Care goals are set by shared decision-making with the person doing PD, and the prescription should aim for clinical euvolemia, with
blood pressure as a key objective measure of prescription quality.[[ntr27_2]] Statements supported by low-certainty evidence are labeled practice
points rather than graded numerically, as the KDOQI commentary on the recommendations notes.[[ntr27_3]] ISPD also describes incremental PD,
prescribing less than full-dose PD while residual function contributes, and states that it achieves outcomes at least as good as full-dose PD
(practice point).[[ntr27_2]]</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>Children have a larger peritoneal surface relative to body weight, so fill volumes are scaled
to body surface area, not taken from adult habits, and intra-abdominal pressure limits how far they can rise. APD at night is common so the child can attend
school, and growth and nutrition are outcomes in their own right. Read <a href="attending-pediatric-nephrologist-20-pd-access-prescription.html">Attending
Pediatric Nephrologist, Module 20</a> before adjusting a child&rsquo;s prescription.</div>
<p><strong>Philippine practice.</strong> PhilHealth&rsquo;s Z Benefits package for PD (Circular 2024-0036) supports PD for eligible adult and pediatric
patients at accredited providers; confirm the current coverage, the eligibility checklist and what it includes on the date of service rather than
quoting amounts from memory.[[ntr27_10]] Solution bags come by courier, often from Luzon, so typhoons, ferry cancellations and storage space at home
shape the prescription as much as the membrane does. A prescription a family cannot keep supplied is not a prescription.</p>
<p><strong>What you do at your stage.</strong> The resident reads the prescription back as a day: when each exchange happens, what strength,
how long it dwells. The fellow writes it with the patient&rsquo;s work and sleep in mind, uses the lowest glucose exposure that meets the fluid
goal, and plans for the week the delivery does not come.</p>
{{key:Every PD lever trades clearance or water against burden, glucose and cost. Choose the trade with the patient, and write it as a day
they can live.}}
"""),
  ('adequacy-pet', 'Adequacy and PET', 'Adequacy, residual function and the PET', """
<p>For years PD adequacy meant a weekly Kt/V target. Two randomized trials changed that. ADEMEX randomized 965 patients in Mexico to continue four
2-liter exchanges a day or to a modified prescription aiming for a peritoneal creatinine clearance of 60 L/week/1.73 m&sup2;. Peritoneal
clearances separated and stayed apart, but survival did not: relative risk of death 1.00 (95% confidence interval 0.80 to 1.24), with 2-year
survival 68.3% in the control group and 69.3% in the intervention group.[[ntr27_4]] In Hong Kong, 320 new CAPD patients were randomized to total
Kt/V targets of 1.5 to 1.7, 1.7 to 2.0, or above 2.0. Two-year survival was 87.3%, 86.1% and 81.5%, without a significant difference. The lowest
group had more patients withdrawn by their physicians and more needed erythropoietin, so the authors recommended a minimum total Kt/V above
1.7.[[ntr27_5]]</p>
<p>Residual kidney function, by contrast, tracks survival closely. A reanalysis of the CANUSA cohort (601 patients) found that each 5 L/week/1.73
m&sup2; of residual glomerular filtration was associated with a 12% lower risk of death, while peritoneal creatinine clearance showed no
association (relative risk 1.00); and each 250 mL of daily urine was associated with a 36% lower risk (relative risk 0.64).[[ntr27_6]] This is
observational. Patients with more urine may be healthier in other ways. But it fits the physiology: native kidneys remove water, sodium, middle
molecules and phosphate continuously, and produce hormones, which a peritoneal bag does not.</p>
<p>ISPD 2020 draws the conclusion. There is no specific clearance target that guarantees sufficient dialysis for an individual; increasing
small-solute clearance above a weekly Kt/V of 1.7 may improve uremic symptoms if present; there appears to be no survival advantage in aiming
routinely above 1.7; and no prescription change is needed for the sole purpose of reaching an arbitrary clearance target. Residual function and
urine volume should be known for everyone on PD, and management should focus on preserving them as long as possible (practice points).[[ntr27_2]]
Kt/V remains a surrogate worth measuring, as a check, not a goal.</p>
<p><strong>The PET.</strong> The peritoneal equilibration test is a standardized 4-hour dwell. The ratio of creatinine in the dialysate to that in
plasma at 4 hours (D/P creatinine) classifies the membrane as high, high-average, low-average or low transport; the drain volume and the fall in
dialysate glucose describe ultrafiltration capacity. In a meta-analysis of 19 observational studies, each 0.1 increase in D/P creatinine was
associated with a 15% higher risk of death (relative risk 1.15, 95% confidence interval 1.07 to 1.23), equal to 21.9%, 45.7% and 77.3% higher risk in
low-average, high-average and high transporters compared with low transporters. Studies with more patients on cycler PD showed a smaller excess
risk.[[ntr27_7]] The likely mechanism is fluid: high transporters lose the osmotic gradient early, gain fluid on long dwells and absorb more glucose.
The finding is an association, but it tells you what to do with a high transporter: protect the long dwell.</p>
<div class="table-wrap"><table><thead><tr><th>Transport status</th><th>Clearance</th><th>Ultrafiltration on long dwells</th><th>Prescription direction to discuss</th></tr></thead><tbody>
<tr><td>High</td><td>Fast</td><td>Poor; often negative</td><td>Shorter dwells (APD), icodextrin for the long dwell</td></tr>
<tr><td>High-average or low-average</td><td>Moderate</td><td>Moderate</td><td>Standard CAPD or APD to goals</td></tr>
<tr><td>Low</td><td>Slow</td><td>Good</td><td>Longer dwells, larger fills; watch clearance as residual function falls</td></tr>
</tbody></table></div>
<p>The ISPD 2020 recommendations add, for low- and lower-middle-income settings, that the PET and weekly Kt/V should be encouraged if their cost
does not compromise the person&rsquo;s ability to continue PD.[[ntr27_2]] In a Philippine province that may mean a simplified PET done when the
problem appears, rather than a routine one.</p>
<p><strong>What you do at your stage.</strong> The intern records urine output every day on a PD patient, because it is part of the
dialysis. The resident avoids nephrotoxins, contrast without good reason and hypotension in a PD patient who still makes urine. The fellow orders a
PET when ultrafiltration changes, interprets it with the exchange record, and treats a falling urine output as a reason to review the prescription.</p>
{{key:In PD, protect the urine first and read the PET second. Kt/V is a check, not the goal, and a high transporter needs its long dwell
rescued.}}
{{fig:ntr27_b}}
"""),
  ('urgent-start', 'Urgent-start PD', 'Urgent-start PD and the first weeks', """
<p>Many Philippine patients need dialysis within days of meeting a nephrologist. The default has been a temporary hemodialysis catheter, with its
infection and central vein risks (Module 24). Urgent-start PD offers another path: a PD catheter placed and used within two weeks, usually with
small supine volumes at first so that intra-abdominal pressure stays low while the tissues heal around the cuffs.</p>
<p><strong>The evidence.</strong> A Cochrane review identified 16 studies with 2,953 participants: one randomized trial (122 participants) and 15
non-randomized studies. With low-certainty evidence, urgent-start PD may increase dialysate leaks compared with conventional start (risk ratio 3.90,
95% confidence interval 1.56 to 9.78), about 210 more leaks per 1,000 patients. For catheter blockage, malposition, exit-site infection,
peritonitis, technique survival and death, the evidence was very low certainty and the effects uncertain.[[ntr27_9]] The honest summary: leaks are
more likely, other harms are uncertain, and no trial has compared urgent-start PD with the realistic alternative for most of these patients, an
emergency hemodialysis catheter.</p>
<div class="table-wrap"><table><thead><tr><th>Phase</th><th>Physiology</th><th>What the team watches</th></tr></thead><tbody>
<tr><td>First days after insertion</td><td>Tissue around the cuffs and the peritoneal incision is not healed</td><td>Leak at the exit site or wound, scrotal or labial swelling, drain failure</td></tr>
<tr><td>Small supine fills</td><td>Lower intra-abdominal pressure when lying down</td><td>Fluid and potassium control with less clearance than full PD</td></tr>
<tr><td>Gradual increase in fill</td><td>Healing allows higher pressure</td><td>Hernias, breathlessness, comfort</td></tr>
<tr><td>Training at home</td><td>The patient takes over the connections</td><td>Technique, hygiene, early peritonitis (Module 28)</td></tr>
</tbody></table></div>
<p>Mechanical problems are common in the first weeks and often mimic membrane failure. Constipation pushes bowel against the catheter tip and slows
drainage, so a full colon is the first thing to treat when the drain volume falls. A catheter tip that has migrated out of the pelvis drains poorly in
some positions. Fibrin can block the side holes. A leak into the abdominal wall makes the drain smaller without the membrane changing at all.</p>
{{flow:When drain volume falls|Is the effluent clear?::Cloudy effluent is peritonitis until proven otherwise (Module 28).|Is it the catheter?::Slow inflow or outflow, drainage that changes with position, constipation, fibrin in the bag; an abdominal radiograph shows the tip.|Is it a leak?::Wet dressing, swelling of the abdominal wall, scrotum or labia, or a hernia.|Is it adherence or supply?::Missed or shortened exchanges, saved bags, wrong strength used.|Is it the membrane?::Long dwells drain less than filled; PET shows high transport or reduced ultrafiltration capacity.|Is it the kidneys?::Urine output falling; review nephrotoxins and blood pressure.}}
{{call:Stop and call the attending nephrologist, per unit protocol, but always ask the attending nephrologist for guidance, when:<ul><li>The
effluent is cloudy or the patient has abdominal pain or fever.</li><li>The patient is breathless, hypoxic or hypertensive from fluid overload that
the current prescription cannot remove.</li><li>The catheter does not drain, or there is a leak at the exit site, wound, scrotum or labia.</li><li>Potassium
is high or low enough to threaten the heart.</li><li>Solution supply has failed and the patient cannot do the prescribed exchanges.</li></ul>}}
<p><strong>What you do at your stage.</strong> The intern reports a wet dressing, a swollen scrotum or a bag that drains slowly. The resident
works through the drain-volume sequence above before calling the membrane failed. The fellow decides with the attending and the surgeon whether
urgent-start PD fits the patient, writes the low-volume start, and arranges early training and a home visit.</p>
{{key:When a new PD catheter drains less, think bowel, tip, leak and missed bags before membrane. Most early problems are mechanical.}}
"""),
 ],
 'debrief': [
  """<p><strong>Why the overnight bag shrinks.</strong> Mr. Abubakar is a high transporter: his membrane absorbs glucose fast, so the osmotic
gradient of a low-strength bag fades within a few hours. Daytime dwells are short enough to drain more than they were filled. During a 10-hour
overnight dwell, after the gradient is gone, lymphatic and tissue reabsorption continue, and the bag drains about 300 mL less than the fill. His net
peritoneal ultrafiltration for the day is small, his urine has halved, and the three days of saved bags added fluid on top.</p>""",
  """<p><strong>What to exclude first.</strong> Clear effluent makes peritonitis unlikely, but check for pain and fever. Treat his constipation,
because a full colon slows drainage. Check that the drain volume does not change with position and that an abdominal radiograph shows the tip in the
pelvis; look for a leak into the abdominal wall or a hernia. Confirm with his wife that exchanges are now complete and the right strengths are used.
Only then read the PET: a D/P creatinine of 0.85, classified by the unit as high transport, together with the negative long dwell, points to the
membrane as the main cause.</p>""",
  """<p><strong>What to change.</strong> Propose to the attending nephrologist and PD nurse a prescription that rescues the long dwell: icodextrin
for the overnight dwell if it can be supplied, or shorter night dwells on a cycler, with the glucose exposure kept as low as the fluid goal allows. Set
the goals with him: no orthopnea, blood pressure controlled, weight back to his post-training level. Protect his 400 mL of urine by avoiding
hypotension and nephrotoxins; neutral-pH, low-GDP solutions are associated with better preservation where available. Check what the PD Z benefit
covers for icodextrin or a cycler, and plan a two-week buffer of bags before the typhoon season.</p>""",
 ],
 'skills': {'title': 'Peritoneal dialysis principles and prescription',
            'intro': 'Complete with a preceptor in a PD unit, on the ward or by case review. Sign-off is local.',
            'items': [('Explains a PD exchange and the three-pore model in plain words to a patient or family', False),
                      ('Calculates net ultrafiltration per exchange and per day from an exchange record', False),
                      ('Interprets a PET result with the exchange record and states the transport category', False),
                      ('Works through the falling-drain-volume sequence: effluent, catheter, leak, adherence, membrane, kidneys', False),
                      ('Records residual urine output and lists measures that protect it', False),
                      ('Writes a draft prescription as a daily schedule with the PD nurse, for attending review', False)],
            'placement': 'Supervised PD unit or ward rotation'},
 'quiz': [
  ('An intern records exchanges for a CAPD patient. Which record is most useful to the team?',
   ['&ldquo;Drained well&rdquo; for each exchange',
    'Fill and drain volumes for every exchange, the dwell length, effluent appearance, weight and urine output',
    'Only the daily weight',
    'The number of bags used'],
   1,
   'Net ultrafiltration is drain minus fill for each exchange, and urine output is part of total fluid removal. &ldquo;Drained well&rdquo; hides a long dwell '
   'that drains less than it was filled.'),
  ('A resident sees that a patient&rsquo;s overnight 10-hour dwell drains 300 mL less than it was filled, while day dwells drain more. Which explanation fits the three-pore model best?',
   ['The large pores have closed',
    'Glucose is absorbed through the small pores, the osmotic gradient fades, and reabsorption continues through the long dwell',
    'Sodium sieving has made the effluent hypertonic',
    'The patient has peritonitis'],
   1,
   'Glucose crosses the small pores into the blood; once the gradient is gone, lymphatic and tissue reabsorption make net ultrafiltration negative. This is '
   'fastest in high transporters. Sieving lowers dialysate sodium early in a dwell; it does not make a long dwell negative.'),
  ('A fellow reviews a stable CAPD patient who feels well, is euvolemic, passes 900 mL of urine a day and has a total weekly Kt/V of 1.8. What does ISPD 2020 suggest?',
   ['Increase the prescription to reach a Kt/V above 2.0',
    'No change is needed solely to reach an arbitrary clearance target; keep protecting residual function',
    'Switch to hemodialysis',
    'Stop measuring urine output'],
   1,
   'ISPD 2020 practice points state there is no survival advantage in aiming routinely above 1.7 and no change is needed only to reach a clearance target. ADEMEX '
   'and the Hong Kong trial found no survival benefit from higher peritoneal clearance.'),
  ('A new urgent-start PD patient&rsquo;s drain volumes fall on day 5. The effluent is clear, he has not passed stool for four days, and drainage improves when he lies on his left side. What is the most likely cause?',
   ['High transport membrane', 'Mechanical drainage problem from constipation and catheter position',
    'Ultrafiltration failure from peritoneal sclerosis', 'Loss of residual kidney function'],
   1,
   'Positional drainage and constipation point to a mechanical cause. A membrane problem does not change with position and would not appear this early; the '
   'drain-volume sequence checks bowel, tip and leak first.'),
  ('A resident presents the Cochrane review of urgent-start PD. Which statement is accurate?',
   ['Urgent-start PD clearly lowers mortality compared with conventional start',
    'Urgent-start PD may increase dialysate leaks (about 210 more per 1,000), with low-certainty evidence; other harms are uncertain',
    'Urgent-start PD doubles peritonitis risk with high certainty',
    'The review included 16 randomized trials'],
   1,
   'The review included one randomized trial and 15 non-randomized studies. Only the leak signal reached low certainty; peritonitis, technique survival and death '
   'were very low certainty.'),
 ],
 'terms': [('PD', 'Peritoneal dialysis'), ('CAPD', 'Continuous ambulatory peritoneal dialysis'), ('APD', 'Automated peritoneal dialysis'),
           ('PET', 'Peritoneal equilibration test'), ('D/P', 'Dialysate-to-plasma ratio'), ('GDP', 'Glucose degradation products'),
           ('ISPD', 'International Society for Peritoneal Dialysis'), ('KDOQI', 'Kidney Disease Outcomes Quality Initiative'),
           ('ADEMEX', 'Adequacy of Peritoneal Dialysis in Mexico trial'), ('CANUSA', 'Canada&ndash;USA peritoneal dialysis study'),
           ('Kt/V', 'Urea clearance times time divided by urea distribution volume')],
 'readings': [('attending-nephrologist-17-pd-prescription.html', 'Attending Nephrologist, Module 17: PD prescription'),
              ('peritoneal-dialysis-nurse-04-capd.html', 'Peritoneal Dialysis Nurse, Module 4: CAPD'),
              ('peritoneal-dialysis-nurse-05-apd.html', 'Peritoneal Dialysis Nurse, Module 5: APD'),
              ('peritoneal-dialysis-ckd.html', 'Peritoneal Dialysis: Your Complete Guide')],
 'calcs': ['calc-pd-adequacy.html', 'calc-pd-glucose-absorption.html', 'calc-urine-output-fluid-balance.html', 'calc-kfre.html'],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
