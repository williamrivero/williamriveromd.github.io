# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 06: Sodium disorders and water balance.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. House
standard for chronic hyponatremia: no more than 10 mmol/L in the first 24 hours and 8 mmol/L in each 24 hours after
(European guideline 2014, 1D, checked against the full text). SALSA, Ayus 2025, George 2018, Sood 2013, Hillier 1999 and
Chauhan 2019 checked against PubMed abstracts. No doses or infusion rates. Fictional case."""

MODULE = {
    "image_alt": "A Filipino resident and a nephrology fellow review a sodium trajectory chart beside an elderly woman resting after a seizure in an emergency room in Cebu, while her daughter holds her hand.",
    "objectives": [
        "<strong>Intern:</strong> Recognize hyponatremia with moderately severe or severe symptoms, such as vomiting, confusion, somnolence or seizure, and report it to your resident at once with the sodium, glucose and medicine list.",
        "<strong>Resident:</strong> Classify a sodium disorder by tonicity, volume and urine studies, and propose a monitored plan that stays within the house correction limit of 10 mmol/L in the first 24 hours and 8 mmol/L in each 24 hours after.",
        "<strong>Fellow:</strong> Anticipate and manage overcorrection, treat the syndrome of inappropriate antidiuresis (SIAD), low-solute hyponatremia (beer potomania, &ldquo;tea and toast&rdquo;) and hypernatremia, and explain where the guidelines and the newer evidence disagree.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the number that moves too fast</span>A sodium disorder is a water disorder, and its danger lies in speed: a sodium that fell fast swells the brain, and a sodium corrected fast after it fell slowly can destroy it. The <b>intern</b> owns recognition and the first call. The <b>resident</b> owns the classification and a plan with a written ceiling. The <b>fellow</b> owns the trajectory: predicting the water diuresis before it comes, and stopping the rise before it crosses the limit.</div>
{{plain:Think of brain cells as soft water balloons packed inside a hard clay pot, the skull. If the water outside the balloons becomes more dilute, water moves in and the balloons swell against the pot. Given a day or two, the balloons let some of their contents leak out, shrink back, and fit the pot again.}}
<p>The picture has a limit. Brain cells do not leak only salt. Over about 48 hours they export potassium, chloride and organic osmolytes such as glutamate, myo-inositol and taurine, and they return to near-normal volume despite a low plasma sodium. That adaptation protects the patient with chronic hyponatremia, and it is also the trap. Reloading those osmolytes takes days. If the plasma sodium is raised faster than the cells can recover their solutes, water leaves the adapted cells, they shrink, and the myelin of the pons and other regions can break down days later: osmotic demyelination. The European guideline uses 48 hours to separate acute from chronic hyponatremia, and treats hyponatremia of unknown duration as chronic.[[ntr06_1]]</p>
<p>The plasma sodium measures the ratio of sodium to water, not the amount of either. Most hyponatremia comes from water retained under the action of antidiuretic hormone (ADH, vasopressin), not from salt lost. Most hypernatremia comes from water lost or never drunk. Every classification and every treatment follows from asking why the kidney is or is not excreting water.</p>
{{cards:Key numbers|Chronic hyponatremia, house standard (European guideline 2014)::No more than 10 mmol/L in the first 24 h and 8 mmol/L in every 24 h after, until 130 mmol/L (1D)|Severe symptoms, first hour (European guideline 2014)::Prompt hypertonic saline (1D), aiming for a 5 mmol/L rise (2D)|Overcorrection (European guideline 2014)::Prompt intervention to re-lower the sodium if a limit is exceeded (1D)|SALSA, 178 patients::Overcorrection 17.2% with rapid intermittent boluses versus 24.2% with slow continuous infusion (not significant); re-lowering treatment 41.4% versus 57.1%|Glucose correction (Hillier 1999)::Sodium falls about 2.4 mmol/L for every 100 mg/dL rise in glucose}}
<p>Most hyponatremia on a medical ward is mild and chronic, and the work is finding the cause. A few patients arrive seizing, and a few are harmed by the treatment itself. Your work is to treat severe symptoms promptly, to raise the sodium only as far as the brain can follow, and to watch the urine for the water diuresis that signals overcorrection is coming.</p>
""",
    "case": {"title": "The seizure at 10:50 p.m.",
             "html": """
<p>Tuesday night, the emergency room of a tertiary hospital in Cebu City. Lola Teresita Yba&ntilde;ez, 70, from Talisay City, weighs 45 kg. Three months ago a clinic started her on a fixed combination of losartan and hydrochlorothiazide for blood pressure and told her to avoid salt. Since then she has eaten mostly rice porridge, crackers and tea. During the hot weeks of the dry season she drank &ldquo;many glasses of water&rdquo; to stay cool. For two days she has had nausea, then vomiting, then confusion.</p>
<p>Ten minutes after arrival she has a generalized seizure that stops after treatment by the emergency team. Her laboratory results return: sodium 112 mmol/L, potassium 2.9 mmol/L, glucose 108 mg/dL, creatinine 0.8 mg/dL, serum osmolality 238 mOsm/kg, urine osmolality 360 mOsm/kg and urine sodium 46 mmol/L. She is drowsy but rousable, with a blood pressure of 112/70 mm Hg and dry mucous membranes.</p>
<p>The intern, Dr. Jessa Lim, calls the internal medicine resident, Dr. Carlo Mendoza. The nephrology fellow on call, Dr. Ana Villanueva, is in the hospital.</p>
""",
             "questions": ["What must happen in the first hour, and what is the target?",
                           "How do you classify her hyponatremia, and what caused it?",
                           "What will make her sodium rise too fast over the next 48 hours, and how will the team prevent it?"]},
    "sections": [
        ("water-physiology", "Water physiology", "How the kidney handles water", """
<p>Plasma tonicity is held in a narrow range by two controls: thirst, which brings water in, and ADH, which lets the collecting duct keep it. A rise in tonicity of a few percent triggers both. ADH inserts aquaporin-2 water channels into the collecting duct, and water moves from the dilute urine into the concentrated medulla. Without ADH the duct stays watertight and the urine is dilute.</p>
<p>ADH has a second trigger that overrides the first. A large fall in effective arterial volume, from vomiting, bleeding, heart failure or cirrhosis, releases ADH even when the plasma is already dilute. The body chooses to defend volume over tonicity. Nausea, pain, stress and many medicines also release ADH. This is why so many hospital patients become hyponatremic when given hypotonic fluid.</p>
<p>The kidney&rsquo;s ability to excrete water also depends on solute. Urine cannot be diluted below a floor of roughly 50 to 100 mOsm/kg, so the daily solute load sets the most water a person can excrete. Someone eating normally excretes several hundred milliosmoles a day and can clear many liters of water. Someone living on tea, crackers or beer may excrete only a fraction of that, and a few liters of water is then more than the kidney can remove. This is low-solute hyponatremia, often called beer potomania or &ldquo;tea and toast&rdquo; hyponatremia.</p>
{{formula:<strong>Arithmetic illustrations, not targets.</strong><br>Effective osmolality (tonicity) = 2 &times; sodium (mmol/L) + glucose (mg/dL) &divide; 18.<br>Maximum daily water excretion &asymp; daily solute excretion (mOsm) &divide; minimum urine osmolality (mOsm/kg). With 300 mOsm a day and a floor of 60 mOsm/kg: about 5 liters. With 120 mOsm a day: about 2 liters.<br>A urine sodium plus potassium higher than the serum sodium means the kidney is excreting no electrolyte-free water; fluid restriction alone will not raise the sodium.}}
<div class="table-wrap"><table>
<thead><tr><th>Step in water handling</th><th>What breaks it</th><th>What you see</th></tr></thead>
<tbody>
<tr><td>Thirst</td><td>Old age, stroke, dementia, sedation, no access to water</td><td>Hypernatremia in a bedridden or confused patient</td></tr>
<tr><td>ADH release</td><td>Low effective arterial volume, nausea, pain, lung or brain disease, drugs, tumors</td><td>Concentrated urine despite dilute plasma</td></tr>
<tr><td>Diluting segment (thick ascending limb, distal tubule)</td><td>Thiazides block the distal tubule&rsquo;s sodium chloride transport and impair dilution</td><td>Hyponatremia weeks after a thiazide is started, especially in thin older women</td></tr>
<tr><td>Collecting duct response</td><td>Lithium, hypercalcemia, hypokalemia, genetic causes</td><td>Dilute urine despite high plasma tonicity (nephrogenic diabetes insipidus)</td></tr>
<tr><td>Solute supply</td><td>Low-protein, low-salt diets; beer</td><td>Dilute urine with hyponatremia; a large water diuresis once solute is given</td></tr>
</tbody></table></div>
{{key:Ask why the kidney is or is not excreting water. The urine osmolality answers whether ADH is acting; the urine sodium and the volume examination answer why.}}
"""),
        ("classify", "Classify", "Classifying hyponatremia: tonicity, then urine, then volume", """
<p>Classification protects you from treating the wrong disorder. The European guideline sets three biochemical grades: mild, 130 to 135 mmol/L; moderate, 125 to 129 mmol/L; and profound, below 125 mmol/L. It grades symptoms separately as moderately severe (for example nausea without vomiting, confusion, headache) or severe (for example vomiting, cardiorespiratory distress, deep somnolence, seizures, coma). Symptoms, not the number, decide how urgently you act.[[ntr06_1]]</p>
{{fig:ntr06_a}}
<p><b>First, exclude non-hypotonic hyponatremia.</b> Glucose in the plasma draws water out of cells and dilutes the sodium; the true tonicity may be normal or high. Hillier and colleagues raised glucose in six healthy volunteers and found an average fall of 2.4 mmol/L of sodium for every 100 mg/dL rise in glucose, larger than the traditional 1.6, and larger still above 400 mg/dL.[[ntr06_9]] Mannitol and radiocontrast do the same. Severe hyperlipidemia or paraproteinemia can produce a falsely low sodium with older laboratory methods (pseudohyponatremia), which a direct ion-selective electrode avoids. Measure serum osmolality when in doubt.</p>
<p><b>Second, read the urine osmolality.</b> A urine osmolality of 100 mOsm/kg or less means ADH is suppressed and points to excess water intake or low solute. Above that, ADH is acting.[[ntr06_1]]</p>
<p><b>Third, read the urine sodium with the volume examination.</b> A urine sodium of 30 mmol/L or less suggests low effective arterial volume, from true volume loss or from heart failure or cirrhosis. Above 30 mmol/L, consider diuretics, kidney disease, SIAD, adrenal insufficiency and vomiting with bicarbonaturia.[[ntr06_1]] Diuretics confound every urine test; a thiazide makes a dry patient look like SIAD.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pattern</th><th>Urine osmolality</th><th>Urine sodium</th><th>Usual causes</th></tr></thead>
<tbody>
<tr><td>Water excess or low solute</td><td>&le;100 mOsm/kg</td><td>Usually low</td><td>Primary polydipsia, beer potomania, tea and toast</td></tr>
<tr><td>Low effective volume</td><td>&gt;100 mOsm/kg</td><td>&le;30 mmol/L</td><td>Vomiting or diarrhea (before bicarbonaturia), heart failure, cirrhosis, nephrotic syndrome</td></tr>
<tr><td>Kidney salt loss or inappropriate ADH</td><td>&gt;100 mOsm/kg</td><td>&gt;30 mmol/L</td><td>Thiazides, SIAD, adrenal insufficiency, hypothyroidism (rare), kidney disease, cerebral salt wasting (rare)</td></tr>
</tbody></table></div>
<p>The syndrome of inappropriate antidiuresis (SIAD) is a diagnosis of exclusion: hypotonic hyponatremia, urine osmolality above 100 mOsm/kg, clinical euvolemia, urine sodium above 30 mmol/L on a normal salt and water intake, and no diuretic, adrenal or thyroid explanation. For SIAD with moderate or profound hyponatremia, the European guideline suggests fluid restriction as first-line treatment (2D) and, as second-line options, increased solute intake with urea or low-dose loop diuretics with oral sodium chloride (2D). It recommends against vasopressin receptor antagonists in moderate and profound hyponatremia (1C).[[ntr06_1]] The United States expert panel is more accepting of vaptans in selected patients.[[ntr06_2]] The difference reflects how each panel weighed the risk of overly rapid correction and liver injury against the benefit in sodium, a surrogate. For hypovolemic hyponatremia, the European guideline recommends restoring extracellular volume with 0.9% saline or a balanced crystalloid (1B).[[ntr06_1]]</p>
<p><b>Philippine practice.</b> Thiazides and thiazide-like diuretics are common in fixed-dose combinations, cheap and often started at primary care, and older thin women eating little salt or protein are at particular risk. During the hot months many older Filipinos drink large amounts of water while eating little. Ask the family exactly what the patient ate and drank this week; it often explains the sodium better than any test.</p>
{{key:Before you treat a low sodium, check glucose and tonicity, read the urine osmolality and sodium, and look at the medicine list for a thiazide. The cause decides the treatment and the speed.}}
"""),
        ("severe", "Severe symptoms", "Severe symptoms: treat the brain, then set the ceiling", """
<p>A seizing patient with hyponatremia has cerebral edema now. A small rise in sodium, a few millimoles per liter, shrinks the brain enough to stop seizures and reduce intracranial pressure. The European guideline recommends prompt intravenous hypertonic saline for severe symptoms (1D), with a check of the sodium after each bolus, aiming for a 5 mmol/L rise (2D).[[ntr06_1]] The volumes and concentrations belong to the guideline and your unit&rsquo;s protocol; this module gives none. Both the European guideline and the United States panel support this bolus approach.[[ntr06_5]]</p>
<p>The bolus approach was tested against slow continuous infusion. The SALSA (saline bolus versus slow infusion) trial, a randomized comparison of the two methods, enrolled 178 adults with symptomatic hyponatremia (glucose-corrected sodium 125 mmol/L or less, mean 118 mmol/L) in three Korean hospitals. Overcorrection, defined in that trial as a rise of more than 12 mmol/L in 24 hours or 18 mmol/L in 48 hours, occurred in 17.2% with rapid intermittent boluses and 24.2% with slow continuous infusion, a difference that was not significant. Fewer patients in the bolus group needed treatment to re-lower the sodium (41.4% versus 57.1%; number needed to treat about 6), and more reached the target within 1 hour in the intention-to-treat analysis (32.2% versus 17.6%).[[ntr06_3]] Note that SALSA&rsquo;s overcorrection threshold is looser than the house standard, so even its &ldquo;safe&rdquo; patients could have exceeded 10 mmol/L in a day.</p>
<p>Once the symptoms improve or the sodium has risen by about 5 mmol/L, the emergency is over and the problem becomes chronic hyponatremia again. Stop the hypertonic saline, treat the cause, and set the ceiling.</p>
{{flow:Severe symptomatic hyponatremia: the first hours|Recognize::Vomiting, deep somnolence, seizures, coma or cardiorespiratory distress with a low sodium. Check glucose to exclude a hyperglycemic cause.|Call::The resident calls the attending at once, per unit protocol, but always asks the attending nephrologist for guidance. Move the patient to a monitored bed.|Treat::Hypertonic saline bolus per the guideline and unit protocol, with a sodium check after each bolus, aiming for a rise of about 5 mmol/L or symptom improvement.|Stop the emergency phase::When symptoms improve or the 5 mmol/L rise is reached. Do not chase a normal sodium.|Write the ceiling::&ldquo;Sodium rise no more than 10 mmol/L in the first 24 hours and 8 mmol/L in each 24 hours after.&rdquo; Write the baseline value and the clock time.|Watch the urine::Hourly urine output; frequent sodium checks as the unit protocol sets. A sudden large volume of dilute urine means the sodium is about to rise fast.}}
{{fig:ntr06_b}}
<h3>The house standard and the newer evidence</h3>
<p>For chronic hyponatremia, this course uses the European guideline&rsquo;s limits as its house standard: no more than 10 mmol/L in the first 24 hours and no more than 8 mmol/L in each 24 hours after, until the sodium reaches 130 mmol/L (1D).[[ntr06_1]] The United States panel sets goals of 4 to 8 mmol/L a day, 4 to 6 in patients at high risk of osmotic demyelination, with limits of 10 to 12 mmol/L a day, or 8 in high-risk patients.[[ntr06_2]] High-risk features include a sodium of 105 mmol/L or less, alcohol use disorder, malnutrition, hypokalemia and advanced liver disease.[[ntr06_2]]</p>
<p>A 2025 meta-analysis challenges how slow is too slow. Ayus and colleagues pooled 16 cohort studies with 11,811 hospitalized adults with severe hyponatremia. Rapid correction (8 to 10 mmol/L or more in 24 hours) was associated with 32 fewer in-hospital deaths per 1,000 patients than slow correction (odds ratio 0.67; moderate-certainty evidence) and with no statistically significant increase in osmotic demyelination.[[ntr06_4]] The studies were observational. Patients whose sodium rises slowly are often sicker, with heart failure, cirrhosis or cancer, and that confounding can produce the association without any causal effect of speed. The analysis shows that very slow correction is not proven safe; it does not show that crossing the house limit is safe. Keep the ceiling, and do not let fear of the ceiling stop you treating the patient.</p>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What you own in severe hyponatremia</th></tr></thead>
<tbody>
<tr><td>Intern</td><td>Recognize severe symptoms, call at once, check glucose, list every medicine including herbal and over-the-counter products, start hourly urine output</td></tr>
<tr><td>Resident</td><td>Start the emergency phase under supervision, stop it at the target, write the ceiling and the monitoring plan, correct hypokalemia knowing it raises sodium</td></tr>
<tr><td>Fellow</td><td>Predict the water diuresis, plan prevention, and decide with the attending on re-lowering if a limit is crossed</td></tr>
</tbody></table></div>
{{call:Stop and call the attending nephrologist when, per unit protocol, but always ask the attending nephrologist for guidance:<ul><li>A low sodium comes with vomiting, deep somnolence, seizure, coma or breathing difficulty</li><li>The sodium has risen by 8 mmol/L or more at any point within the first 24 hours, or is rising faster than the plan</li><li>Urine output suddenly rises with dilute urine in a patient being treated for hyponatremia</li><li>New swallowing difficulty, weakness or altered behavior appears days after correction</li></ul>}}
{{key:In severe symptoms, raise the sodium a little, quickly, then stop. In everything that follows, the ceiling is 10 mmol/L in the first 24 hours and 8 mmol/L in each 24 hours after.}}
"""),
        ("overcorrection", "Overcorrection", "Preventing and rescuing overcorrection", """
<p>Overcorrection is usually caused by the patient, not the drip. When the stimulus for ADH disappears, the kidney suddenly excretes large volumes of dilute urine, and the sodium climbs by several millimoles per liter in a few hours. The common triggers are predictable:</p>
<div class="table-wrap"><table>
<thead><tr><th>Trigger</th><th>Why ADH falls or water excretion rises</th><th>What you see</th></tr></thead>
<tbody>
<tr><td>Volume restored after vomiting or diarrhea</td><td>The volume stimulus for ADH disappears</td><td>Urine output rises hours after saline</td></tr>
<tr><td>Thiazide stopped</td><td>Diluting capacity returns</td><td>Rising dilute urine over the first day</td></tr>
<tr><td>Solute given to a low-solute patient</td><td>Food or saline supplies the solute the kidney needed to excrete water</td><td>Water diuresis after the first meals</td></tr>
<tr><td>Nausea, pain or drug effect resolved</td><td>Non-osmotic ADH release stops</td><td>Dilute urine after symptoms settle</td></tr>
<tr><td>Potassium repleted</td><td>Potassium entering cells pulls sodium out of them, and potassium given raises plasma sodium</td><td>A rise larger than the saline explains</td></tr>
</tbody></table></div>
<p>George and colleagues reviewed 1,490 patients admitted with sodium below 120 mmol/L in seven hospitals. Rapid correction, a rise of more than 8 mmol/L at 24 hours, occurred in 41%. Younger age, female sex, schizophrenia, a lower presenting sodium and a urine sodium below 30 mmol/L were associated with greater risk. Eight patients (0.5%) developed osmotic demyelination; five had beer potomania, five had hypokalemia, and seven had a rise of more than 8 mmol/L in a 24-hour period beforehand. Five of the eight recovered neurologically.[[ntr06_6]] The study was retrospective and found demyelination only in those who had imaging, so the true rate may be higher.</p>
<h3>Three strategies</h3>
<p><b>Reactive:</b> watch the urine and the sodium, and act when a water diuresis begins. <b>Proactive:</b> in a patient at high risk, give desmopressin from the start to hold ADH activity constant, so the sodium rises only with the hypertonic saline given. Sood and colleagues reported this in 25 patients with sodium below 120 mmol/L; mean rises were 5.8 mmol/L in the first 24 hours and 4.5 mmol/L in the second, with no correction beyond 12 mmol/L in 24 hours.[[ntr06_7]] This was a quality improvement report without controls; it shows feasibility, not superiority. <b>Rescue:</b> when a limit has been crossed, the European guideline recommends prompt intervention to re-lower the sodium (1D): stop the active treatment, and consult an expert about electrolyte-free water and desmopressin with strict monitoring (1D).[[ntr06_1]] Re-lowering is an attending decision.</p>
<p>The house standard applies to the whole 24-hour window, measured from the first sodium. A rise of 7 mmol/L in the first six hours leaves only 3 mmol/L for the next 18. Write the cumulative rise and the clock time beside every result.</p>
{{key:Watch the urine more closely than the drip. A sudden flow of dilute urine means the sodium will soon cross the ceiling unless someone acts.}}
"""),
        ("hypernatremia", "Hypernatremia", "Hypernatremia: the patient who could not reach the water", """
<p>Hypernatremia means water deficit relative to sodium. Because thirst is powerful, it develops almost only in people who cannot drink when thirsty: infants, older adults with dementia or stroke, sedated and ventilated patients, and anyone whose water depends on someone else. The causal chain is water lost (fever, fast breathing, sweating, diarrhea, an osmotic diuresis from glucose or urea, diabetes insipidus) and not replaced, or, less often, sodium gained (hypertonic fluids, bicarbonate, salt ingestion).</p>
<p>Brain cells shrink at first and then gain osmolytes over a day or two, so chronic hypernatremia carries the opposite risk to chronic hyponatremia: correcting too fast could, in theory, swell the brain. Seay and colleagues note that goals for the correction rate of hypernatremia are less well established than for hyponatremia.[[ntr06_8]] Some studies suggest a fall of no more than 0.5 mmol/L per hour. Chauhan and colleagues examined 449 critically ill adults with sodium above 155 mmol/L and found no association between faster correction and death (adjusted odds ratio 1.3 in each group, not significant), and no case of cerebral edema attributable to rapid correction on chart review.[[ntr06_10]] It was a single-database observational study. Correct steadily, monitor, and do not leave a hypernatremic patient untreated out of fear of speed.</p>
{{formula:<strong>Arithmetic illustration, not a target.</strong> Free water deficit &asymp; total body water &times; (serum sodium &divide; 140 &minus; 1).<br>An 82-year-old man weighing 50 kg (total body water about 50% of weight, 25 L) with a sodium of 162 mmol/L: 25 &times; (162 &divide; 140 &minus; 1) &asymp; 3.9 L, before ongoing losses.}}
<div class="table-wrap"><table>
<thead><tr><th>Cause</th><th>Urine clue</th><th>First thought for the plan</th></tr></thead>
<tbody>
<tr><td>No access to water, extra-renal losses</td><td>Small volume, concentrated urine</td><td>Replace water enterally if the gut works; count ongoing losses</td></tr>
<tr><td>Osmotic diuresis (glucose, urea after recovery from acute kidney injury (AKI), mannitol)</td><td>Large volume, urine osmolality near or above plasma</td><td>Treat the solute source; replace losses</td></tr>
<tr><td>Diabetes insipidus</td><td>Large volume of dilute urine despite high sodium</td><td>Distinguish central from nephrogenic with the attending</td></tr>
<tr><td>Sodium gain</td><td>High urine sodium</td><td>Stop the source; the kidney excretes sodium if it works</td></tr>
</tbody></table></div>
<p><b>Philippine practice.</b> Many bedridden older patients in the Philippines are cared for at home by family members or hired caregivers, and many are fed by nasogastric tube with commercial formulas or blended food. Free water flushes are easy to forget, and hot months increase losses. When you admit an older patient with hypernatremia, ask who gives the water and how much, and teach that person before discharge. The tonicity calculators on this site help with the arithmetic; the plan belongs to the team.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>Children become hyponatremic easily in hospital because illness, pain and nausea release ADH; the American Academy of Pediatrics (AAP) recommends isotonic maintenance fluids with appropriate potassium chloride and dextrose for patients 28 days to 18 years old (evidence quality A; strong recommendation).[[ntr06_11]] Infants with gastroenteritis and children with diabetic ketoacidosis are at risk of hypernatremia and of cerebral edema during treatment, and sodium targets are set by the pediatric team. See <a href="attending-pediatric-nephrologist-03-fluids-sodium-acid-base.html">Attending Pediatric Nephrologist, Module 03</a>.</div>
{{key:Hypernatremia is usually a problem of access to water. Find out who gives this patient water, replace the deficit steadily with monitoring, and fix the access before discharge.}}
"""),
    ],
    "debrief": ["""
<p><strong>The first hour, and the target.</strong> A seizure with a sodium of 112 mmol/L is hyponatremia with severe symptoms. Dr. Lim calls immediately, rechecks glucose (108 mg/dL, so the hyponatremia is truly hypotonic), lists the losartan&ndash;hydrochlorothiazide, and starts hourly urine output. Dr. Mendoza calls the attending, moves Lola Teresita to a monitored bed, and starts the hypertonic saline bolus approach under the guideline and unit protocol (1D), checking the sodium after each bolus. The target for this phase is a rise of about 5 mmol/L (2D) or an end to the symptoms, not a normal sodium. At 11:50 p.m. her sodium is 117 mmol/L and she is more awake; the boluses stop.</p>
""", """
<p><strong>Classification and cause.</strong> Her serum osmolality is low, so the hyponatremia is hypotonic. Her urine osmolality of 360 mOsm/kg shows ADH is acting. Her urine sodium of 46 mmol/L would suggest SIAD, but she is on a thiazide and has been vomiting, which confound it, and her dry mucous membranes suggest volume depletion. The likely mechanism is several at once: a thiazide impairing dilution, vomiting and low volume driving ADH, a low-solute diet limiting water excretion, and a high water intake in the heat. Hypokalemia, from the thiazide and vomiting, adds to the risk.</p>
""", """
<p><strong>The next 48 hours.</strong> Dr. Villanueva counts the triggers for a water diuresis: the thiazide is stopped, her volume will be restored, potassium repletion will raise her sodium, and her first full meals will supply solute. She is also at high risk of osmotic demyelination: profound hyponatremia, hypokalemia and poor nutrition. The ceiling is written from the first sodium at 10:40 p.m.: no more than 122 mmol/L by 10:40 p.m. tomorrow, and the attending asks for a lower goal within it, as the United States panel suggests for high-risk patients. At 6 a.m. her urine output reaches 350 mL an hour, dilute, and her sodium is 120 mmol/L. The fellow calls the attending, who decides, as the guideline advises with expert input, to hold the water diuresis with desmopressin under close monitoring. The family is taught that the &ldquo;low salt&rdquo; advice was not meant to mean tea and crackers, and her blood pressure medicine is changed.</p>
"""],
    "skills": {"title": "Hyponatremia: classification and a correction plan with a ceiling",
               "intro": "Complete with a preceptor, on a real or simulated patient. Sign-off is local.",
               "items": [
                   ("Grades severity by sodium and by symptoms using the European guideline categories, and states which findings need an immediate call", False),
                   ("Excludes non-hypotonic hyponatremia with glucose correction and serum osmolality", False),
                   ("Classifies the disorder using urine osmolality, urine sodium, volume examination and the medicine list", False),
                   ("Writes the house ceiling (10 mmol/L in 24 hours, 8 mmol/L in each 24 hours after) with the baseline value and clock time", False),
                   ("Lists the triggers of a water diuresis in this patient and the monitoring that will detect it", False),
                   ("Calculates a free water deficit for a hypernatremic patient and names the person responsible for water at home", False),
               ],
               "placement": "Emergency room, medical ward or intensive care unit"},
    "quiz": [
        ("A 74-year-old man with a sodium of 118 mmol/L has been vomiting repeatedly and is now hard to rouse. What should the intern do first?",
         ["Recheck the sodium in the morning blood draw",
          "Restrict his fluids and observe overnight",
          "Report it to the resident at once as hyponatremia with severe symptoms, with the glucose and medicine list",
          "Give oral salt tablets"], 2,
         "Vomiting and deep somnolence are severe symptoms in the European guideline. Severe symptoms decide urgency, not the number. Fluid restriction is a treatment for SIAD without severe symptoms."),
        ("A euvolemic woman not on diuretics has a sodium of 124 mmol/L, serum osmolality 258 mOsm/kg, urine osmolality 480 mOsm/kg and urine sodium 62 mmol/L, with normal thyroid and adrenal tests. What is the best classification and first-line treatment per the European guideline?",
         ["SIAD; fluid restriction as first-line treatment (2D)",
          "Hypovolemic hyponatremia; isotonic saline (1B)",
          "Primary polydipsia; no treatment",
          "Pseudohyponatremia; repeat with a direct electrode"], 0,
         "Low tonicity, urine osmolality above 100 mOsm/kg, urine sodium above 30 mmol/L, euvolemia and no diuretic, adrenal or thyroid cause fit SIAD. Saline can worsen SIAD because the kidney excretes the sodium and keeps the water."),
        ("A patient with chronic hyponatremia started at 110 mmol/L. Twelve hours later the sodium is 119 mmol/L and the urine output is 300 mL an hour, dilute. What does the house standard require?",
         ["Continue; the 24-hour limit is 12 mmol/L",
          "Stop active sodium-raising treatment and call the attending now to prevent or reverse overcorrection, because the 10 mmol/L limit for 24 hours is about to be crossed",
          "Give a loop diuretic to remove the extra water",
          "Restrict fluids to slow the rise"], 1,
         "Nine of the 10 mmol/L allowed in the first 24 hours are used in 12 hours, and a water diuresis has begun. The European guideline recommends prompt intervention to re-lower if a limit is exceeded (1D); acting now may avoid it."),
        ("A man with poorly controlled diabetes has a measured sodium of 126 mmol/L and a glucose of 900 mg/dL. Using the Hillier correction, what is his glucose-corrected sodium, and what does it mean?",
         ["About 113 mmol/L; severe hypotonic hyponatremia",
          "About 126 mmol/L; no correction is needed",
          "About 139 mmol/L; normal tonicity",
          "About 145 mmol/L; his tonicity is high and he has a water deficit that will appear as glucose falls"], 3,
         "Corrected sodium = 126 + 2.4 &times; (900 &minus; 100) &divide; 100 = about 145 mmol/L. His effective osmolality is high; the sodium will rise as insulin lowers the glucose, revealing the water deficit."),
        ("A 2025 meta-analysis of 16 cohort studies associated rapid correction of severe hyponatremia with lower in-hospital mortality. How should a fellow explain this on rounds?",
         ["The data are observational and confounded by illness severity; they show very slow correction is not proven safe, but they do not show that crossing the house limit is safe",
          "The house limit should be abandoned",
          "The study proves that rapid correction prevents death",
          "The study found that osmotic demyelination was common with rapid correction"], 0,
         "Patients whose sodium rises slowly are often sicker. Observational associations cannot establish that speed itself saves lives. The analysis found no statistically significant increase in osmotic demyelination, which is not the same as proving safety."),
    ],
    "terms": [
        ("AAP", "American Academy of Pediatrics"),
        ("ADH", "Antidiuretic hormone (vasopressin)"),
        ("AKI", "Acute kidney injury"),
        ("SALSA", "Trial acronym: a randomized comparison of rapid intermittent bolus with slow continuous infusion of hypertonic saline in symptomatic hyponatremia"),
        ("SIAD", "Syndrome of inappropriate antidiuresis"),
    ],
    "readings": [
        ("dysnatremia.html", "Dysnatremia: Low and High Sodium"),
        ("unlocking-urine-electrolytes-clinician.html", "Unlocking Urine Electrolytes (Clinician)"),
        ("attending-nephrologist-06-electrolyte-emergencies.html", "Attending Nephrologist, Module 6: Electrolyte Emergencies"),
        ("el-nino-heat-dialysis.html", "El Ni&ntilde;o, Heat and Kidney Patients"),
    ],
    "calcs": ["calc-dysnatremia-toolkit.html", "calc-sodium-correction-rate.html", "calc-sodium-trajectory-tracker.html",
              "calc-sodium-glucose-correction.html", "calc-free-water-deficit.html", "calc-efw-clearance.html", "calc-osmolal-gap.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
