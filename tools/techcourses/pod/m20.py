# -*- coding: utf-8 -*-
"""Physician on Duty, Module 20: Prescribing Without Kidneys.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty and a nurse at a dialysis chair sorting the contents of a patient&rsquo;s medicine bag on a tray, while the patient&rsquo;s daughter stands beside her.",
    "objectives": [
        "Name the groups of medicines most dialysis patients take and the reason for each, and reconcile a medication list at the chair with the nurse and the patient.",
        "Apply five questions before any prescription: is it needed, is it cleared by the kidney, is it removed by dialysis, when is it given relative to the session, and does it interact or duplicate.",
        "Explain which drug properties make a drug removable by dialysis and why some doses are timed after the session.",
        "Recognize the drugs that build up and cause confusion, seizures, falls, low blood sugar, or bleeding, and suggest safer directions to the attending nephrologist.",
        "Look up a dose for kidney failure in your unit&rsquo;s named reference and confirm it with the attending nephrologist or pharmacist before it is given.",
        "Ask about over-the-counter, herbal, and imported products by generic ingredient, since brand names vary.",
    ],
    "big": """
{{plain:Picture a basin with a tap above and a drain below. Each dose of a medicine is water from the tap, and the kidneys are the drain. In kidney failure the drain is almost closed, so the same tap fills the basin higher with every dose. Dialysis opens a second drain, but only for a few hours, a few times a week.}}
<p>The picture has a limit. Many drugs leave through the liver, and for them the drain is still open. Some are changed by the liver into active breakdown products, called metabolites, that the kidneys must then remove. And the dialysis drain is selective. It takes small molecules floating free in the blood and leaves those bound to protein or hidden in the tissues.</p>
{{cards:Key terms for this module|Renal clearance::The part of a drug&rsquo;s removal that the kidneys perform. It falls toward zero in a patient without urine.|Active metabolite::A breakdown product of a drug that still acts on the body.|Half-life::The time for the blood level of a drug to fall by half. It lengthens when the route of removal is lost.|Accumulation::The rise in drug level when each dose arrives before the last one has cleared.|Protein binding::The share of a drug attached to blood proteins such as albumin. Bound drug cannot cross the dialyzer membrane.|Volume of distribution::How widely a drug spreads into the body&rsquo;s tissues. A large volume means little of it sits in the blood.}}
<p>Module 4 explained why kidney failure changes drug handling. This module puts that knowledge to work at the chair. Most medicines a dialysis patient takes are needed and safe at the doses the nephrologist has set. A few common prescriptions build up quietly and first show themselves as confusion, a fall, a seizure, low blood sugar, or bleeding. Your work is to know those few, to ask five questions before any new prescription, and to bring the list to the attending nephrologist before harm, not after it.</p>
""",
    "case": {"title": "Ten medicines, three doctors", "html": """
<p>Mrs. Erlinda &ldquo;Linda&rdquo; Pascual, 71, has dialyzed on Mondays, Wednesdays, and Fridays for two years through a right upper-arm fistula. She has diabetes and passes almost no urine. Today is Wednesday. At 2:30 p.m., in hour two, her daughter tells you that her mother has been &ldquo;sleepy and talking strangely&rdquo; since Monday.</p>
<p>Last week a clinic doctor gave her gabapentin for burning feet. On Saturday an urgent-care doctor started valacyclovir for shingles on her left chest. She also takes glibenclamide that a relative bought for her, amlodipine, calcium carbonate with meals, and a cough syrup from a drugstore. None of the doctors knew about the others&rsquo; prescriptions.</p>
<p>The nurse, Ms. Grace Alcantara, has checked the capillary glucose, laid out the medicine bag on a tray, and called you. Illustrative bedside values, not targets: blood pressure 132/74 mm Hg, heart rate 80 per minute, oxygen saturation 98%, capillary glucose 68 mg/dL, temperature 37.0 &deg;C. Mrs. Pascual knows her daughter but not the day of the week. Her hands twitch now and then.</p>
""", "questions": ["Which drugs on this list could explain her confusion, and in what order would you raise them?",
                  "What do you do now for the low glucose, under protocol, and what do you tell the attending nephrologist?",
                  "What reference do you use to check doses, and who decides whether to stop, change, or remove a drug with extra dialysis?"]},
    "sections": [
        ("pillbox", "The pill box", "What is in the pill box, and why", """
<p>Picture a weekly pill box filled from prescriptions in three doctors&rsquo; handwriting. Each compartment has a reason, and most stand in for a job the kidneys used to do.</p>
{{fig:pod20_pillbox}}
<p>Healthy kidneys remove phosphate, activate vitamin D, balance salt and water, and make the hormone that drives red cell production. When they fail, each lost job leaves a gap, and a medicine fills it. Other medicines treat the diseases that travel with kidney failure, such as diabetes and heart disease.</p>
<div class="table-wrap"><table>
<thead><tr><th>Group</th><th>The kidney job or problem it answers</th><th>Module</th></tr></thead>
<tbody>
<tr><td>Phosphate binders</td><td>Phosphate is no longer excreted</td><td>21</td></tr>
<tr><td>Active vitamin D and calcimimetics</td><td>Vitamin D is no longer activated, and the parathyroid glands overwork</td><td>21</td></tr>
<tr><td>Blood pressure medicines</td><td>Salt and water are retained</td><td>14</td></tr>
<tr><td>Iron and erythropoiesis-stimulating agents (ESA)</td><td>Too little erythropoietin, and iron losses</td><td>21</td></tr>
<tr><td>Diabetes medicines</td><td>The commonest cause of kidney failure</td><td>22</td></tr>
<tr><td>Statins and antiplatelet medicines</td><td>Heart and vessel disease</td><td>4, 15</td></tr>
</tbody></table></div>
<p>Chiu and colleagues counted the daily pills of 233 patients in three United States dialysis units. The median was 19 pills a day, and a quarter of patients took more than 25. Phosphate binders made up about half, and 62% of patients did not take their binders as prescribed. A higher pill burden was associated with lower physical quality of life.[[chiu2009]] The study was cross-sectional, so it cannot show that the pills caused the poorer quality of life.</p>
{{formula:<strong>Worked example C: a pill count at the chair (illustrative).</strong><br>Calcium carbonate, 3 tablets with each of 3 meals = 9. Amlodipine = 1. Glibenclamide = 2. Gabapentin = 3. Valacyclovir = 3. Other tablets = 4.<br>Total = 9 + 1 + 2 + 3 + 3 + 4 = 22 tablets a day, against a published median of 19.[[chiu2009]]<br>What it tells you: the burden is high, and two drugs are new this week. What it does not tell you: which drugs are safe or which can stop. That is a conversation with the attending nephrologist.}}
<p>The Kidney Disease: Improving Global Outcomes (KDIGO) 2024 guideline on chronic kidney disease (CKD) advises a thorough medication review periodically and at transitions of care, to check adherence, continued need, and interactions, noting that people with CKD often see several specialists. KDIGO issues this as an ungraded practice point.[[kdigo_ckd2024]] A hospital discharge, a visit to another doctor, and a trip to a drugstore are all transitions.</p>
{{flow:Reconcile at the chair|Gather every source::The patient&rsquo;s bag, the chart list, the latest discharge summary, and outside prescriptions.|Write each drug by generic name::Strength, frequency, prescriber, and start date.|Ask what is not in the bag::Drugstore products, herbal remedies, and medicines bought by relatives.|Mark duplicates and new drugs::Two drugs of one class, and anything started or changed in the past week.|Report::Give the list to the attending nephrologist. Do not stop or start drugs outside protocol.}}
{{key:The list in the chart is a guess until you have seen what is in the patient&rsquo;s bag.}}
"""),
        ("fivequestions", "Five questions", "Five questions before you write", """
<p>Treat every new prescription for a dialysis patient as a gate with five bars. The drug passes only when each bar has an answer. Most of the harm in this module would not pass it.</p>
{{flow:Five questions before any prescription|1. Is it needed?::Name the problem. Ask whether a non-drug step or a drug already on the list would do.|2. Is it cleared by the kidney?::Check the drug and its active metabolites. If either leaves through the kidneys, it builds up without a dose change.|3. Is it removed by dialysis?::Check the reference. The next section explains what decides removal.|4. When is it given?::Doses of removed drugs are usually given after the session, as the order and the reference state.|5. Does it interact or duplicate?::A second sedative, a second drug that lowers glucose, a second blood thinner, or one drug under two brand names.}}
<h3>Why the usual kidney numbers do not apply</h3>
<p>KDIGO advises that clinicians consider glomerular filtration rate (GFR) when dosing drugs cleared by the kidneys, and monitor drug levels when indicated for drugs with a narrow therapeutic window. Both are ungraded practice points.[[kdigo_ckd2024]] What follows for a dialysis patient is practical inference, not a guideline statement. Equations that estimate GFR from creatinine assume a steady level. In dialysis, creatinine rises between sessions and falls during them, so an estimated GFR (eGFR) or a Cockcroft-Gault clearance reflects the dialysis schedule, not the kidneys. Use the reference&rsquo;s line for hemodialysis. A patient with good residual urine output, as Module 3 described, has some kidney clearance left, and that judgment belongs to the attending nephrologist.</p>
<div class="table-wrap"><table>
<thead><tr><th>Where to look up a dose</th><th>What it gives you</th><th>Its limit</th></tr></thead>
<tbody>
<tr><td>Your unit&rsquo;s adopted dosing reference</td><td>A hemodialysis line, often with timing</td><td>References differ for some drugs, because the data are small studies. Use one, and name it in the record</td></tr>
<tr><td>The product label</td><td>Kidney dosing, if it was studied</td><td>Many labels say only &ldquo;not studied in dialysis&rdquo;</td></tr>
<tr><td>The pharmacist</td><td>A check of dose, interactions, and duplicates</td><td>Needs the full reconciled list</td></tr>
<tr><td>The attending nephrologist</td><td>The decision for this patient</td><td>Needs a clear report from you</td></tr>
</tbody></table></div>
<p>The site&rsquo;s Renal Medication Safety calculator screens a list for kidney cautions. Use it to prepare your call, not to choose a dose. KDIGO also encourages working with pharmacists on complex regimens, as a practice point.[[kdigo_ckd2024]]</p>
<p>Some physicians raise a dose because &ldquo;dialysis will remove it.&rdquo; This is often wrong. Many drugs are barely removed, and those that are removed still accumulate across the long gaps between sessions.</p>
{{call:Stop and call the attending nephrologist before any new antibiotic, anticoagulant, antiseizure drug, opioid, or sedative is given to a dialysis patient. Bring the reconciled list and the line from your unit&rsquo;s reference.}}
{{key:Five questions, every time: needed, kidney-cleared, removed by dialysis, timing, and interactions.}}
"""),
        ("dialyzable", "What dialysis removes", "What the dialyzer takes out", """
<p>Picture a garden sieve. Small loose stones fall through. Large stones stay on top. Stones stuck to a big rock stay with the rock, and stones buried in the garden beds never reach the sieve.</p>
<p>The picture has a limit. Removal also depends on blood and dialysis fluid flow, the membrane&rsquo;s pores, and the session length, as Module 5 explained. Here the question is narrower: which features of a drug decide whether it crosses.</p>
{{fig:pod20_dialyzable}}
<p>A drug crosses the membrane only as a free molecule in plasma water. That one fact explains the properties a standard dialysis text lists.[[daugirdas2015]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Property</th><th>Favors removal</th><th>Limits removal</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Molecular size</td><td>Small</td><td>Large</td><td>Large molecules diffuse slowly and may not fit the pores</td></tr>
<tr><td>Protein binding</td><td>Little</td><td>Strong</td><td>The protein cannot cross, so drug riding on it stays</td></tr>
<tr><td>Volume of distribution</td><td>Mostly in the blood</td><td>Spread into tissues and fat</td><td>The dialyzer sees only the blood</td></tr>
<tr><td>Water solubility</td><td>Water-soluble</td><td>Fat-soluble</td><td>Fat-soluble drugs sit in tissues and bind proteins</td></tr>
</tbody></table></div>
<p>Two drugs show the extremes. Gabapentin is small, barely protein-bound, and leaves the body almost entirely in the urine. Dialysis removes it well, yet it still builds up, because in an anuric patient dialysis is its only way out. Apixaban, an anticoagulant, is largely protein-bound. In a pharmacokinetic study of seven hemodialysis patients, a session removed only 4% of it.[[mavrakanas2017]] Seven patients is a small sample, but the finding fits the drug&rsquo;s properties.</p>
<h3>Why some doses are given after the session</h3>
<p>A dose of a removed drug given before dialysis is partly lost in the dialysis fluid. Given after the session, the full dose stays until the next one. After a session, drug held in the tissues can also move back into the blood, so the level rises again. This rebound is one reason a level drawn at the end of a session can mislead.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pattern in the order</th><th>Why it exists</th><th>How you confirm it</th></tr></thead>
<tbody>
<tr><td>&ldquo;Give after dialysis&rdquo;</td><td>The session removes the drug</td><td>The hemodialysis line in your reference</td></tr>
<tr><td>A supplemental dose after the session</td><td>Removal is large enough to underdose the patient</td><td>The reference, the pharmacist, the attending</td></tr>
<tr><td>A level before the next dose</td><td>A narrow range between effect and harm, as with vancomycin</td><td>The order and the pharmacist</td></tr>
<tr><td>No timing instruction</td><td>The drug is barely removed, or no one has checked</td><td>Ask. Assume neither way</td></tr>
</tbody></table></div>
<h3>How much of a dose remains</h3>
<p>When the kidneys are the main route out, losing them lengthens the half-life, and much more of yesterday&rsquo;s dose is still present today. The arithmetic below uses first-order elimination, the pattern most drugs follow at usual doses (Module 4).</p>
{{formula:<strong>Worked example A: fraction of a dose remaining (illustrative values, not drug data).</strong><br>Formula (first-order elimination): fraction remaining after time t = (1/2)<sup>t &divide; half-life</sup><br>Suppose a half-life of 6 hours with normal kidneys and 30 hours in kidney failure.<br>After 24 hours, normal kidneys: (1/2)<sup>24 &divide; 6</sup> = (1/2)<sup>4</sup> = 1/16, about 6% left.<br>After 24 hours, kidney failure: (1/2)<sup>24 &divide; 30</sup> = (1/2)<sup>0.8</sup> = about 0.57, or 57% left.<br>A second daily dose lands on more than half of the first. A steady level takes about four to five half-lives: about one day with normal kidneys, five to six days in kidney failure.<br>What this tells you: why toxicity appears days after a drug is started. What it does not tell you: a dose.}}
{{key:Do not assume a drug is removed by dialysis. Check the reference, and give removed drugs after the session as ordered.}}
"""),
        ("accumulate", "Drugs that build up", "The drugs that build up and hurt the brain", """
<p>Picture a bucket under a dripping tap with its drain blocked. Nothing happens for a while. Then, days later, it overflows. In a dialysis patient the first overflow is usually in the brain: drowsiness, confusion, jerking of the limbs, or a fall.</p>
<p>The picture has a limit. The brain is not a passive floor. Kidney failure is thought to make it more sensitive, through retained uremic toxins and changes in the barrier between blood and brain. A level a healthy person tolerates may tip a dialysis patient over.</p>
{{fig:pod20_accumulation}}
<p>Worked example A showed why the level climbs for days before it settles. That timing is your best clue at the chair. New confusion a few days after a new prescription points to the drug until shown otherwise.</p>
{{fig:pod20_timeline}}
<h3>Gabapentin and pregabalin</h3>
<p>These drugs treat nerve pain, itch, and restless legs, and the kidneys clear them. Ishida and colleagues studied 140,899 United States hemodialysis patients in the national registry. In 2011, 19% received gabapentin and 4% pregabalin. The highest gabapentin dose category was associated with 50%, 55%, and 38% higher hazards of altered mental status, falls, and fracture. Even the lowest doses were associated with 31% to 41% higher hazards of altered mental status. Pregabalin was associated with up to 51% and 68% higher hazards of altered mental status and falls.[[ishida2018]] The study was observational. Patients given these drugs may differ in ways the data cannot capture.</p>
<p>Among 74,084 older adults in Ontario with CKD not on dialysis, starting at a higher dose was associated with more hospital visits for encephalopathy, falls, fracture, or slowed breathing within 30 days: 1.9% versus 1.5%. The absolute difference was 0.40%, about one extra event for every 250 patients.[[muanda2022]] Dialysis patients, whose clearance is lower still, were excluded.</p>
<h3>Opioids</h3>
<p>From 2006 to 2010, more than 60% of United States dialysis patients filled at least one opioid prescription each year, and about 20% had a chronic supply. In 153,758 patients, opioid prescription was associated with death, stopping dialysis, and hospitalization, and higher doses with more deaths.[[kimmel2017]] The authors state that causation cannot be inferred, because an opioid may mark a sicker patient. Some opioids, such as morphine, also have active metabolites that the kidneys clear.</p>
<h3>Cefepime</h3>
<p>Cefepime, a broad-spectrum antibiotic, crosses into the brain and at high levels blocks the calming signal of gamma-aminobutyric acid (GABA). In a systematic review of 135 published cases, 80% of patients had kidney dysfunction. Forty-eight percent had been overdosed for their kidney function, yet 26% developed toxicity despite appropriate dosing. Of those who had an electroencephalogram (EEG), 25% showed nonconvulsive status epilepticus, a seizure state without visible jerking.[[payne2017]] A second review of 119 cases found a median onset of four days and improvement in 97.5% after dose reduction or stopping the drug.[[maan2022]] A meta-analysis of 23 studies found an odds ratio of 10.06 for neurotoxicity with an eGFR below 30 mL/min/1.73 m&sup2;.[[hardi2025]] These are case collections and observational data. They describe the pattern well but cannot give a true rate.</p>
<h3>Acyclovir and valacyclovir</h3>
<p>Valacyclovir becomes acyclovir in the body, and the kidneys excrete it. In 119 published cases of neurotoxicity, 83.3% had kidney impairment and 57.1% had kidney failure. In 59.7% the dose exceeded the kidney-adjusted recommendation. Symptoms began a mean of 3.1 days after starting. Stopping the drug was the main treatment, and some patients needed extra dialysis.[[brandariz2021]]</p>
{{formula:<strong>Worked example B: the five questions for valacyclovir (decision walk-through).</strong><br>1. Needed? Shingles in an older adult: an antiviral is reasonable.<br>2. Kidney-cleared? Yes, as acyclovir.<br>3. Removed by dialysis? Partly. The reference gives a hemodialysis line.<br>4. Timing? After the session on dialysis days, as the reference states.<br>5. Interactions? Gabapentin adds a second drug that can cloud the brain.<br>Outcome: you read the hemodialysis line in your unit&rsquo;s reference, you do not write the prescription, and you call the attending nephrologist, noting that most published neurotoxicity followed doses above the kidney-adjusted recommendation.[[brandariz2021]]<br>What this does not tell you: the dose.}}
<h3>Baclofen</h3>
<p>Baclofen, a muscle relaxant, leaves through the kidneys. Wolf and colleagues described a hemodialysis patient whose baclofen toxicity reversed with urgent hemodialysis, and they recommend avoiding the drug in severe kidney dysfunction and on dialysis.[[wolf2018]] This is the authors&rsquo; recommendation from a case report and review, not a graded guideline.</p>
<div class="table-wrap"><table>
<thead><tr><th>Think twice</th><th>Harm in dialysis patients</th><th>Evidence</th><th>Direction to discuss</th></tr></thead>
<tbody>
<tr><td>Gabapentin, pregabalin</td><td>Confusion, falls, fracture</td><td>Registry cohort, associations[[ishida2018]]</td><td>Is it needed; a kidney-adjusted dose</td></tr>
<tr><td>Opioids</td><td>Sedation, falls</td><td>Registry cohort, associations[[kimmel2017]]</td><td>Non-drug steps and paracetamol first</td></tr>
<tr><td>Cefepime</td><td>Confusion, myoclonus, nonconvulsive seizures</td><td>Reviews of cases[[payne2017]][[maan2022]]</td><td>Adjusted dosing, close watch, or another antibiotic</td></tr>
<tr><td>Acyclovir, valacyclovir</td><td>Confusion, hallucinations</td><td>Review of cases[[brandariz2021]]</td><td>The hemodialysis line, after the session</td></tr>
<tr><td>Baclofen</td><td>Drowsiness, coma</td><td>Case report with review[[wolf2018]]</td><td>Another approach to spasm</td></tr>
</tbody></table></div>
<p>Module 18 covers the confused patient. This table supplies the drug suspects.</p>
{{call:Stop and call the attending nephrologist when you suspect drug toxicity: new confusion, jerking of the limbs, a seizure, low blood sugar, unexpected sleepiness, or bleeding. Some toxicities are treated with extra dialysis, which only the attending nephrologist orders. Follow your unit&rsquo;s protocol for the first minutes while you call.}}
{{key:When a dialysis patient becomes confused, ask what was started or changed this week.}}
"""),
        ("diabetesdoac", "Diabetes drugs and anticoagulants", "Metformin, sulfonylureas, and anticoagulants", """
<p>Some drugs are safe at one level of kidney function and unsafe when the kidneys are gone. The drug has not changed. Its route out has closed. Three groups matter most because they arrive on lists written by doctors who may not know the patient dialyzes.</p>
<h3>Metformin</h3>
<p>Metformin leaves the body unchanged in the urine, and at high levels it pushes the body toward lactic acid production. Without kidneys it accumulates. KDIGO 2022 recommends metformin for type 2 diabetes with CKD and an eGFR of 30 mL/min/1.73 m&sup2; or more, graded 1B.[[kdigo_dm2022]] The consensus of the American Diabetes Association (ADA) and KDIGO states that &ldquo;metformin is contraindicated with eGFR &lt;30 mL/min/1.73 m<sup>2</sup> and with dialysis treatment.&rdquo;[[deboer2022]] The site&rsquo;s Metformin Safety in CKD calculator shows the cutoff.</p>
<h3>Sulfonylureas and insulin</h3>
<p>Healthy kidneys break down part of the body&rsquo;s insulin and make some glucose. When they fail, insulin lasts longer and glucose reserves are smaller. Glibenclamide, a long-acting sulfonylurea, drives insulin release, and its active metabolites are cleared partly by the kidneys. Low glucose can then last for hours and return after treatment. The ADA-KDIGO consensus names advanced CKD as a risk factor for hypoglycemia and advises careful use of insulin and sulfonylureas.[[deboer2022]] The American Geriatrics Society (AGS) Beers Criteria advise avoiding sulfonylureas as first- or second-line therapy in adults 65 and older unless there are substantial barriers to safer agents, and prefer short-acting agents over long-acting ones such as glibenclamide, a strong recommendation with high-quality evidence for hypoglycemia.[[beers2023]] Module 22 covers diabetes regimens, and Module 18 covers low glucose in the chair.</p>
<h3>Anticoagulants</h3>
<p>The direct oral anticoagulants (DOAC) differ in how much they depend on the kidneys. Apixaban depends on them least, yet it accumulates in hemodialysis. In the study by Mavrakanas and colleagues, apixaban 2.5 mg twice daily gave exposure similar to the standard dose with normal kidneys, while 5 mg twice daily raised trough levels above the 90th percentile for that dose.[[mavrakanas2017]] These doses are study findings, not instructions. The study measured drug levels, a surrogate, in seven patients (five on the higher dose), not strokes or bleeding. The right dose in hemodialysis is still debated; Module 19 covers anticoagulants and bleeding. The site&rsquo;s DOAC Renal Dosing calculator shows labeled kidney dosing to prepare your call.</p>
<div class="table-wrap"><table>
<thead><tr><th>Found on the list</th><th>Why the risk changes</th><th>What the source says</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>Metformin</td><td>Excreted unchanged; accumulates</td><td>Contraindicated with dialysis, consensus statement[[deboer2022]]</td><td>Flag it the same day</td></tr>
<tr><td>Glibenclamide</td><td>Longer action, active metabolites, smaller glucose reserve</td><td>Avoid in older adults, strong[[beers2023]]</td><td>Check glucose, treat by protocol, flag it</td></tr>
<tr><td>Apixaban or another DOAC</td><td>Reduced clearance; little removed by dialysis</td><td>Higher dose supratherapeutic in a small study[[mavrakanas2017]]</td><td>Report dose, prescriber, and any bleeding</td></tr>
</tbody></table></div>
{{call:Stop and call the attending nephrologist the same day when metformin, a long-acting sulfonylurea, or an outside anticoagulant appears on a dialysis patient&rsquo;s list. Call at once if there is low glucose or bleeding, after starting treatment under your unit&rsquo;s protocol.}}
{{key:A drug that was right before dialysis can be wrong after it. Read every outside prescription as if it were new.}}
"""),
        ("antibiotics", "Antibiotics and pain", "Antibiotics and pain relief: the common requests", """
<p>You will hear two requests most often: &ldquo;he needs an antibiotic&rdquo; and &ldquo;she needs something for the pain.&rdquo; Both are reasonable, and both carry the drugs most often linked to harm.</p>
<h3>Antibiotics: the pattern, not the dose</h3>
<p>The pattern follows from Module 4. The first dose fills the volume of distribution, which kidney failure does not shrink, so it is usually full. Later doses replace what is cleared, and with the kidneys gone less is cleared, so they shrink or spread out.</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>What it means</th><th>Who sets it</th></tr></thead>
<tbody>
<tr><td>Loading dose</td><td>Usually a full first dose</td><td>The reference and the attending nephrologist</td></tr>
<tr><td>Maintenance</td><td>Smaller, less often, or after each session</td><td>The reference and the attending nephrologist</td></tr>
<tr><td>Timing</td><td>After the session for drugs dialysis removes</td><td>The order</td></tr>
<tr><td>Levels</td><td>Vancomycin and aminoglycosides are dosed by measured levels</td><td>The attending nephrologist and the pharmacist</td></tr>
</tbody></table></div>
<p>Cultures come before the first dose when the protocol allows. Module 17 covers fever and bloodstream infection, and the reading on antibiotic stewardship explains why the narrowest suitable drug is preferred.</p>
<h3>Pain relief</h3>
<p>Nonsteroidal anti-inflammatory drugs (NSAIDs) such as ibuprofen reduce blood flow to the remaining kidney tissue, raise potassium, retain salt and water, and add to bleeding risk. The Beers Criteria advise avoiding chronic use of most oral NSAIDs in older adults, and avoiding ketorolac and indomethacin, both strong recommendations on moderate-quality evidence.[[beers2023]] Paracetamol is the usual first drug because the liver, not the kidney, clears it. Opioid choice and dose belong to the attending nephrologist, weighed against the harms in the registry data.[[kimmel2017]]</p>
<p>The Beers Criteria also list drugs to avoid or reduce by kidney function: gabapentin and pregabalin for dose reduction below a creatinine clearance of 60 mL/min, and baclofen for avoidance below an eGFR of 60 or on chronic dialysis, each strong on moderate-quality evidence; tramadol for reduction or avoidance below a creatinine clearance of 30 mL/min, weak on low-quality evidence.[[beers2023]] These cutoffs describe the criteria, not a dose, and a creatinine clearance means nothing in an anuric patient. The criteria were built for older adults in the United States and support, not replace, judgment. Tramadol with a gabapentinoid stacks two sedating, kidney-dependent drugs, a combination the Beers Criteria say to avoid (strong, moderate-quality evidence).[[beers2023]]</p>
{{flow:Pain relief for a dialysis patient|Ask and examine::A new pain may be a fracture after a fall, an infected access, or the heart.|Non-drug measures::Position, warmth, gentle movement, and treating the cause.|Paracetamol::The usual first drug, as your unit&rsquo;s protocol allows.|Avoid repeated NSAIDs::Especially with residual urine, high potassium, or bleeding risk.|Anything stronger::Opioids, gabapentinoids, and muscle relaxants are chosen and dosed by the attending nephrologist.|Write it down::The indication, the reference used, and the advice received.}}
{{key:Write no new antibiotic or opioid without the attending nephrologist&rsquo;s instruction, and record the indication and the reference you used.}}
"""),
        ("otc", "Over the counter", "Over-the-counter, herbal, and imported products", """
<p>Every home has a medicine cabinet you never see: the drugstore cough syrup, a neighbor&rsquo;s antacid, a cousin&rsquo;s herbal tea, capsules a relative sent from abroad. None appear in the chart unless someone asks.</p>
<p>KDIGO advises reviewing and limiting over-the-counter medicines and dietary or herbal remedies that may harm people with CKD, an ungraded practice point.[[kdigo_ckd2024]] The reason is physiology. Potassium, magnesium, aluminum, and phosphate are normally excreted by the kidneys. Without them, a product harmless to a neighbor can build up in a dialysis patient.</p>
<p>Brand names change between drugstores and countries. Ask the family to bring the box, and read the generic ingredients.</p>
<div class="table-wrap"><table>
<thead><tr><th>Product</th><th>Ingredient to look for</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Pain relievers</td><td>Ibuprofen, mefenamic acid, naproxen, alone or with paracetamol</td><td>Loss of residual function, high potassium, bleeding</td></tr>
<tr><td>Cough and cold mixtures</td><td>Chlorphenamine and other sedating antihistamines; phenylephrine</td><td>Drowsiness and confusion; higher blood pressure</td></tr>
<tr><td>Salt substitutes</td><td>Potassium chloride</td><td>A dangerous rise in potassium (Module 18)</td></tr>
<tr><td>Antacids</td><td>Magnesium and aluminum salts</td><td>Both accumulate without kidney excretion</td></tr>
<tr><td>Laxatives and enemas</td><td>Phosphate and magnesium salts</td><td>A load the patient cannot excrete</td></tr>
<tr><td>Herbal products, imported &ldquo;kidney cleansers&rdquo;</td><td>Often unknown</td><td>Uncertain content and strength; possible interactions</td></tr>
</tbody></table></div>
<p>Ask without judgment. Many patients buy these products because a pain or cough went unaddressed, or because the drugstore is cheaper. A patient who feels scolded stops telling you. Record each product by ingredient, and report anything on the table to the attending nephrologist.</p>
{{key:Ask about the cabinet you cannot see at every reconciliation, and record what you find by ingredient.}}
"""),
    ],
    "debrief": ["""
<p><strong>Which drugs could explain her confusion, and in what order?</strong> Start with what you can measure and reverse in minutes. Her glucose is low, and glibenclamide bought without a prescription is the likely cause. Low glucose alone may not explain two days of confusion, so go on. Valacyclovir is next. It started on Saturday and the confusion on Monday, matching the onset of a few days in published cases, most of which involved kidney failure and unadjusted doses.[[brandariz2021]] The twitching fits too. Gabapentin is third: started last week, cleared by the kidneys, and associated with altered mental status even at low doses in registry data.[[ishida2018]] The two drugs add to each other. The cough syrup is fourth until you read its label. Drugs are not the only explanation. Shingles can spread to the brain, and Module 18 lists potassium, stroke, and infection. Raise the drugs alongside those causes.</p>
<p><strong>What do you do for the low glucose, and what do you tell the attending?</strong> Ask Ms. Alcantara to treat it now by the route and amount in your unit&rsquo;s hypoglycemia protocol and to recheck it as directed. A long-acting sulfonylurea can lower glucose again for hours, so ask for repeated checks through the session and before she leaves. Then call the attending nephrologist with a structured report: situation, background, assessment, and recommendation (SBAR), as Module 1 taught. Give the timeline, the glucose and its response, the reconciled list with start dates and prescribers, the twitching, and your concern about valacyclovir and gabapentin. Ask whether the session continues as planned, whether to hold the new drugs, and whether she needs transfer.</p>
<p><strong>What reference, and who decides?</strong> You read the hemodialysis lines in the one reference your unit has adopted and name it in the record, and you may ask the pharmacist to check the list. The attending nephrologist decides whether to stop or change any drug. Extra dialysis to clear a drug is ordered only by the attending nephrologist. You document the list, the glucose readings and treatment, the call, and the advice, and you make sure the family can tell the outside doctors that she is on dialysis.</p>
"""],
    "skills": {"title": "Medication reconciliation and toxicity screen at the chair",
               "intro": "Reconcile the medicines of a real or simulated dialysis patient from a medicine bag while your preceptor observes. Then present a toxicity screen for a newly confused patient.",
               "items": [
                   ("Collects every source: the patient&rsquo;s bag, the chart list, the latest discharge summary, and outside prescriptions.", True),
                   ("Records each drug by generic name, strength, frequency, prescriber, and start date.", False),
                   ("Asks about over-the-counter, herbal, and imported products and reads their ingredients.", False),
                   ("Identifies duplicates, such as two drugs of one class from two prescribers.", False),
                   ("Marks drugs that are kidney-cleared or have active metabolites, using the unit&rsquo;s named reference.", True),
                   ("Flags high-risk drugs: gabapentinoids, opioids, cefepime, acyclovir or valacyclovir, baclofen, sulfonylureas, metformin, and anticoagulants.", True),
                   ("For a confused patient, lists drugs started or changed in the past seven days and asks for a glucose check.", True),
                   ("Notes the timing relative to dialysis for each drug the session removes.", False),
                   ("States why an eGFR or creatinine clearance does not apply to an anuric dialysis patient.", False),
                   ("Reports to the attending nephrologist with an SBAR summary and does not stop or start drugs outside protocol.", True),
                   ("Explains to the patient and family, in plain words, which medicines are under review and why.", False),
                   ("Documents the reconciled list, the reference used, and the call.", False),
               ],
               "placement": "Over two weeks, reconcile the medicines of five patients on your shifts from their bags, not the chart alone. For each, count the daily pills, list any high-risk drug, and note any over-the-counter product. Review the five lists with your preceptor and the attending nephrologist."},
    "quiz": [
        ("Why does a kidney-cleared drug build up in a hemodialysis patient even though dialysis removes it?",
         ["Dialysis converts it into a more toxic form",
          "Dialysis raises its protein binding",
          "Between sessions there is no kidney clearance, so each dose adds to what remains",
          "The liver stops working when the kidneys fail"], 2,
         "Dialysis runs a few hours a few times a week. Between sessions an anuric patient has no route out."),
        ("Which drug properties predict good removal by hemodialysis?",
         ["Small, little protein binding, mostly in the blood",
          "Large, strongly protein-bound, fat-soluble",
          "Small, strongly protein-bound, spread into tissues",
          "Large, water-soluble, spread into tissues"], 0,
         "Only free molecules in plasma water cross the membrane."),
        ("A nurse asks you to double a new antibiotic dose &ldquo;because dialysis will wash it out.&rdquo; What is the best response?",
         ["Agree, since all antibiotics are removed",
          "Give the usual dose before the session",
          "Give half the usual dose to be safe",
          "Check the hemodialysis line in the unit&rsquo;s reference and call the attending nephrologist first"], 3,
         "Many drugs are barely removed, and removed drugs still accumulate between sessions."),
        ("Why does an eGFR from serum creatinine mislead when dosing for an anuric dialysis patient?",
         ["The liver removes creatinine in dialysis patients",
          "Creatinine is not at steady state and reflects the dialysis schedule",
          "The equations fail only in women",
          "Creatinine is not measured in dialysis units"], 1,
         "The equations assume a steady creatinine. In dialysis it rises between sessions and falls during them."),
        ("Mrs. Reyes, 76, on hemodialysis, became drowsy and confused three days after starting a new medicine. Which is the most likely culprit?",
         ["Amlodipine, taken for four years",
          "Calcium carbonate, taken for two years",
          "Valacyclovir, started three days ago for shingles",
          "Atorvastatin, taken for five years"], 2,
         "Confusion a few days after a kidney-cleared drug is started is the classic pattern. Published cases had a mean onset of 3.1 days."),
        ("A hemodialysis patient on cefepime for four days now has jerking arms and is hard to rouse. What is the key consideration?",
         ["Fatigue from pneumonia",
          "Cefepime neurotoxicity, including possible nonconvulsive seizures; call the attending nephrologist now",
          "Cefepime is not kidney-cleared, so it cannot be the cause",
          "Raise the cefepime dose"], 1,
         "In one review, a quarter of those with an EEG had nonconvulsive status epilepticus."),
        ("What did Ishida and colleagues find about gabapentin in hemodialysis patients?",
         ["It reduced falls compared with pregabalin",
          "Only doses above the labeled maximum were linked to harm",
          "A randomized trial proved it causes fractures",
          "Even low doses were associated with a higher hazard of altered mental status"], 3,
         "Low doses carried 31% to 41% higher hazards. The study was observational, so it shows association, not proof of cause."),
        ("In older adults with CKD, 1.9% on a higher versus 1.5% on a lower starting gabapentinoid dose had a serious event within 30 days. What is the best reading?",
         ["A small absolute difference, about one extra event per 250 patients, in people not on dialysis",
          "A 27% absolute increase in events",
          "Proof that higher doses cause encephalopathy in dialysis patients",
          "No meaningful difference"], 0,
         "The risk ratio was 1.27, but the absolute difference was 0.40%. Dialysis patients were excluded."),
        ("Mr. Dizon, 63, on hemodialysis, has metformin on a list from a new clinic doctor. What do you do?",
         ["Continue it, since KDIGO recommends metformin",
          "Halve the dose",
          "Flag it to the attending nephrologist; the ADA-KDIGO consensus calls it contraindicated with dialysis",
          "Tell him to stop all diabetes medicines"], 2,
         "The KDIGO 1B recommendation applies to an eGFR of 30 or more."),
        ("A woman on hemodialysis takes glibenclamide bought by a relative. Her glucose is low in hour two and recovers with treatment by protocol. What is the main concern?",
         ["She is now safe",
          "Her glucose may fall again for hours; arrange repeated checks and call the attending",
          "Dialysis removes glibenclamide completely",
          "She should take another tablet to balance the treatment"], 1,
         "A long-acting sulfonylurea with active metabolites can cause recurrent low glucose."),
        ("In the apixaban study by Mavrakanas and colleagues, how much of the drug did a hemodialysis session remove?",
         ["About half",
          "About a quarter",
          "Almost all",
          "About 4%"], 3,
         "Apixaban is largely protein-bound. The study had seven patients and measured drug levels, a surrogate."),
        ("Why is an antibiotic loading dose usually not reduced in a dialysis patient?",
         ["It fills the volume of distribution, which kidney failure does not shrink",
          "Dialysis patients have worse infections",
          "It is given after the session and removed",
          "Loading doses do not reach the blood"], 0,
         "Clearance falls in kidney failure, so maintenance changes. The volume the first dose fills does not."),
        ("A dialysis patient with good residual urine asks for ibuprofen for knee pain. What is the best first step?",
         ["Prescribe ibuprofen for two weeks",
          "Prescribe tramadol with gabapentin",
          "Examine the knee, use non-drug measures and paracetamol per protocol, and avoid repeated NSAIDs",
          "Give ketorolac by injection"], 2,
         "NSAIDs threaten residual function and raise potassium. Ketorolac is on the Beers list to avoid."),
        ("Which over-the-counter product most often raises potassium dangerously?",
         ["Paracetamol",
          "A potassium chloride salt substitute",
          "Calcium carbonate",
          "Saline nasal spray"], 1,
         "Salt substitutes replace sodium with potassium, which the patient cannot excrete."),
        ("Mr. Santos, 68, on hemodialysis, takes an unlabeled herbal capsule from abroad. How do you handle it?",
         ["Ignore it, since herbs are natural",
          "Warn him he will be discharged from the unit",
          "Suggest a different herbal product",
          "Ask without judgment, identify the ingredients if possible, record it, and report it to the attending nephrologist"], 3,
         "KDIGO advises reviewing and limiting such remedies. Scolding drives them out of sight."),
    ],
    "terms": [("Renal clearance", "The part of a drug&rsquo;s removal performed by the kidneys."),
              ("Active metabolite", "A breakdown product of a drug that still acts on the body."),
              ("Half-life", "The time for the blood level of a drug to fall by half."),
              ("Accumulation", "The rise in drug level when each dose arrives before the last has cleared."),
              ("Dialyzability", "How much of a drug the dialyzer removes during a session."),
              ("Protein binding", "The share of a drug attached to blood proteins. Bound drug cannot cross the dialyzer membrane."),
              ("Volume of distribution", "How widely a drug spreads into the body&rsquo;s tissues."),
              ("Loading dose", "A first dose that fills the volume of distribution so the drug acts quickly."),
              ("Medication reconciliation", "Comparing every source of information about a patient&rsquo;s medicines to produce one accurate list."),
              ("Nonconvulsive status epilepticus", "Prolonged seizure activity in the brain without visible jerking, seen on an electroencephalogram.")],
    "readings": [("medicines-and-your-kidneys.html", "A plain-language guide to how kidney failure changes medicines, useful when you explain a change to a patient."),
                 ("medication-operational-guide.html", "How medicines are handled and recorded in the unit."),
                 ("antibiotic-stewardship-dialysis.html", "Why the narrowest suitable antibiotic is chosen, and how antibiotics are dosed around dialysis.")],
    "calcs": ["calc-renal-med-safety.html", "calc-doac-renal-dosing.html", "calc-metformin-ckd-safety.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
