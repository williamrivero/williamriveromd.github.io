# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 15: CKD mineral and bone disorder and nutrition.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard.
KDIGO 2017 CKD-MBD statements and grades checked against the guideline summary (PMC6340919); KDOQI 2020 protein
statements and grades against the published commentary table; KDIGO 2024 Recommendation 3.3.1.1 (2C) and practice
points against the KDIGO summary. CRIC FGF23 data, EVOLVE, the Jamal meta-analysis, the Sullivan additive trial and
the Garneata ketoanalogue trial from the PubMed abstracts. No doses. Fictional case."""

MODULE = {
    "image_alt": "A nephrology fellow points to the ingredient list on a can of luncheon meat while a hemodialysis patient and his wife look on at a dialysis unit in Caloocan.",
    "objectives": [
        "<strong>Intern:</strong> Record calcium, phosphate, parathyroid hormone (PTH) and alkaline phosphatase results with dates, units and assay, correct calcium for albumin, and take a diet and supplement history that includes processed foods and soft drinks.",
        "<strong>Resident:</strong> Interpret calcium, phosphate, PTH and alkaline phosphatase as trends using the Kidney Disease: Improving Global Outcomes (KDIGO) 2017 chronic kidney disease&ndash;mineral and bone disorder (CKD-MBD) guideline, and name the modifiable driver behind each abnormal trend.",
        "<strong>Fellow:</strong> Plan phosphate binders, vitamin D, calcimimetics, parathyroidectomy referral and dietary protein with the KDIGO 2017, Kidney Disease Outcomes Quality Initiative (KDOQI) 2020 nutrition and KDIGO 2024 statements and their grades, and explain where the guidelines disagree.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the monthly laboratory sheet and the plate</span>The <strong>intern</strong> lines up the results by date, corrects calcium for albumin, and asks what the patient actually ate this week, from the canned goods to the soft drinks. The <strong>resident</strong> reads the trend rather than the single value and names what is driving it: food, missed binders, short dialysis, low vitamin D, or rising PTH. The <strong>fellow</strong> chooses with the attending among binders, vitamin D, calcimimetics and surgery, sets a protein target the patient can live with, and knows which statement in which guideline backs each choice.</div>
{{plain:Picture a sari-sari store with one narrow back door. Deliveries of phosphate arrive every day from the patient&rsquo;s meals. The kidney is the back door, the only way out. When the door narrows, the owner hires a guard to push more stock out of each opening and cancels part of tomorrow&rsquo;s delivery. If that is not enough, the owner calls the landlord, who starts breaking the walls to make room.}}
<p>The picture has a limit. The store has one guard and one landlord; the body has several hormones that talk to each other, and the walls they break are bone and blood vessels. As nephrons are lost, bone cells release fibroblast growth factor 23 (FGF23). With its kidney co-receptor Klotho, FGF23 makes each remaining nephron excrete more phosphate and suppresses the activation of vitamin D to calcitriol. Less calcitriol means less calcium absorbed from the gut and less restraint on the parathyroid glands, so PTH rises. For years these hormones keep serum phosphate and calcium normal. The price is paid quietly: FGF23 and PTH climb, Klotho falls, bone turnover changes, and calcium and phosphate settle in arteries and heart valves.[[ntr15_3]]</p>
{{cards:Key numbers|Start monitoring calcium, phosphate, PTH and alkaline phosphatase (KDIGO 2017)::From CKD G3a in adults (1C)|PTH on dialysis (KDIGO 2017)::About 2 to 9 times the upper normal limit of the assay (2C)|Calcium-based binders in adults (KDIGO 2017)::Restrict the dose (2B)|Dialysate calcium (KDIGO 2017)::1.25 to 1.50 mmol/L (2C)|Protein in CKD G3&ndash;G5 (KDIGO 2024)::0.8 g/kg body weight per day (2C); avoid more than 1.3 g/kg per day (practice point)|Protein in stable CKD 3&ndash;5 without diabetes (KDOQI 2020)::0.55 to 0.60 g/kg per day under close supervision (1A for kidney failure or death)}}
<p>Most mineral problems in CKD build slowly over months and are found on a routine laboratory sheet. A few announce themselves: symptomatic hypocalcemia, severe hypercalcemia, or painful skin ulcers of calciphylaxis. Your work is to read the trend early, fix the driver you can see before adding a medicine, avoid loading the patient with calcium, and give diet advice that fits a Filipino kitchen and a Filipino budget.</p>
""",
    "case": {"title": "The itch that keeps him awake", "html": """
<p>Saturday, 7 a.m., a freestanding hemodialysis unit in Caloocan. Mr. Rodel Santiago, 49, a security guard, has been on hemodialysis for four years. He dialyzes twice a week because the tricycle fare for a third trip is more than his family can spare. He tells you the itch on his back and legs keeps him awake, and his knees and heels ache when he stands at his post.</p>
<p>The intern, Dr. Bea Tolentino, has lined up his results. Over nine months, phosphate rose from 5.8 to 7.1 mg/dL, total calcium from 9.0 to 9.6 mg/dL with a normal albumin, intact PTH from 380 to 920 pg/mL (laboratory upper normal limit 65 pg/mL), and alkaline phosphatase from 110 to 240 U/L. He was prescribed calcium carbonate tablets with meals and takes them &ldquo;when I remember, usually at night.&rdquo; His usual meals on duty are instant noodles, hotdogs or canned luncheon meat with rice, and a cola. He asks whether he should stop eating meat altogether.</p>
""", "questions": ["What do the nine-month trends tell you, and what is driving them?",
                  "What would you change first in his binders, diet and dialysis before adding a new medicine?",
                  "If PTH keeps rising, which PTH-lowering options would you discuss with the attending, and when is parathyroidectomy on the table?"]},
    "sections": [
        ("axis", "The mineral axis", "The mineral axis: FGF23, Klotho, calcitriol and PTH", """
<p>In a steady state, a healthy kidney excretes as much phosphate as the gut absorbs, and it fine-tunes how much leaves in the urine. The tuning is hormonal. FGF23 and PTH both tell the proximal tubule to excrete phosphate. Calcitriol, the active form of vitamin D made in the kidney, raises gut absorption of calcium and phosphate and holds PTH down.</p>
<p>In CKD the sequence runs in a predictable order. FGF23 rises first. In 3,879 adults with CKD stages 2 to 4 in the Chronic Renal Insufficiency Cohort (CRIC), median FGF23 was markedly higher than in healthy populations and rose as estimated glomerular filtration rate (eGFR) fell, while mean phosphate and median PTH were still in the normal range. High FGF23 was more common than secondary hyperparathyroidism or hyperphosphatemia at every level of eGFR, and its rise began at a higher eGFR than the rise in PTH.[[ntr15_3]] This was an observational cross-sectional analysis; it shows the order of change, not that lowering FGF23 helps.</p>
<p>The chain that follows is the one to carry in your head: fewer nephrons, then higher FGF23, then less calcitriol, then less gut calcium and less restraint on the parathyroid glands, then rising PTH, then, late, rising phosphate. High PTH pulls calcium and phosphate out of bone. When the parathyroid glands are pushed long enough, they enlarge and become less responsive, and PTH stays high even when calcium is normal.</p>
{{fig:ntr15_a}}
<div class="table-wrap"><table>
<thead><tr><th>Step in the chain</th><th>What happens</th><th>What you see on the sheet or at the bedside</th></tr></thead>
<tbody>
<tr><td>FGF23 rises, Klotho falls</td><td>More phosphate excreted per nephron; calcitriol suppressed</td><td>Usually nothing; FGF23 is not a routine test</td></tr>
<tr><td>Calcitriol falls</td><td>Less calcium absorbed; parathyroid glands released from restraint</td><td>Calcium low-normal; 25-hydroxyvitamin D often low as well</td></tr>
<tr><td>PTH rises</td><td>Bone resorption increases; high-turnover bone disease</td><td>Rising PTH and alkaline phosphatase; bone pain, fractures</td></tr>
<tr><td>Phosphate rises (late)</td><td>Excretion capacity overwhelmed; calcium-phosphate deposits</td><td>Hyperphosphatemia, itch, vascular and valve calcification</td></tr>
<tr><td>PTH oversuppressed</td><td>Low-turnover (adynamic) bone; calcium has nowhere to go</td><td>Low PTH, hypercalcemia with calcium loads, fractures</td></tr>
</tbody></table></div>
<p>Two wrong turns are possible, and both cause harm. Too much PTH breaks bone down. Too little, often from heavy calcium loads and vitamin D, leaves bone inactive, so a calcium load goes into vessels instead of skeleton. That is why the guideline speaks of trends and ranges, not of driving PTH as low as possible.[[ntr15_1]]</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>A child&rsquo;s skeleton is still growing, so CKD-MBD shows as growth failure, bone deformity and rickets as well as laboratory changes. KDIGO 2017 starts monitoring in children from CKD G2 (2D) and asks that calcium be kept in the age-appropriate normal range (2C).[[ntr15_1]] Children need more phosphate and calcium for growth than adults, so restriction must be planned with a pediatric renal dietitian.[[ntr15_10]] See <a href="attending-pediatric-nephrologist-18-ckd-complications.html">Attending Pediatric Nephrologist, Module 18</a>.</div>
{{key:Read CKD-MBD as a chain: FGF23 first, then calcitriol, then PTH, then phosphate. A normal phosphate in CKD G3 does not mean the axis is normal.}}
"""),
        ("labs-trends", "Labs and trends", "The laboratory sheet: what to measure, how often, and how to read it", """
<p>KDIGO 2017 recommends monitoring serum calcium, phosphate, PTH and alkaline phosphatase activity in adults beginning at CKD G3a (1C).[[ntr15_1]] The frequency rises as kidney function falls and when results are abnormal or treatment changes. The guideline&rsquo;s first treatment statement sets the habit for everything that follows: base decisions on serial measurements of phosphate, calcium and PTH considered together, not on one value (not graded).[[ntr15_1]]</p>
<div class="table-wrap"><table>
<thead><tr><th>KDIGO 2017 statement</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>Monitor calcium, phosphate, PTH and alkaline phosphatase from CKD G3a in adults</td><td>1C</td></tr>
<tr><td>Consider measuring 25-hydroxyvitamin D and correct deficiency as for the general population</td><td>2C</td></tr>
<tr><td>Consider bone mineral density testing to assess fracture risk when results will change treatment</td><td>2B</td></tr>
<tr><td>A bone biopsy is reasonable if knowing the type of bone disease will change treatment</td><td>Not graded</td></tr>
<tr><td>Base treatment on serial phosphate, calcium and PTH considered together</td><td>Not graded</td></tr>
</tbody></table></div>
<p>The table follows the guideline summary.[[ntr15_1]] A bone biopsy is rarely available in the Philippines, which makes the trend in PTH and alkaline phosphatase your main window on bone turnover.</p>
<h3>The intern&rsquo;s part: getting the numbers right</h3>
<p>Correct total calcium for a low albumin before anyone acts on it, and say that you did. Write the PTH assay&rsquo;s upper normal limit beside every PTH value, because PTH assays differ and the KDIGO dialysis range is expressed as a multiple of that limit. Note when the sample was taken in relation to dialysis; phosphate drawn right after a session is not comparable with a pre-dialysis value.</p>
{{formula:<strong>Albumin-corrected calcium (arithmetic illustration, not a target).</strong> Corrected calcium (mg/dL) = measured calcium + 0.8 &times; (4.0 &minus; albumin in g/dL).<br>Measured calcium 8.2 mg/dL with albumin 2.5 g/dL: 8.2 + 0.8 &times; 1.5 = 9.4 mg/dL. Where your laboratory offers ionized calcium, it is more reliable in very sick or very low-albumin patients.}}
<h3>The resident&rsquo;s part: reading patterns</h3>
<div class="table-wrap"><table>
<thead><tr><th>Trend over months</th><th>Most likely driver</th><th>First question to ask</th></tr></thead>
<tbody>
<tr><td>Phosphate rising, PTH rising</td><td>Phosphate load exceeds removal; binder not taken with meals</td><td>What did you eat, and when do you take the tablets?</td></tr>
<tr><td>PTH rising, phosphate and calcium normal (CKD G3&ndash;G4)</td><td>Calcitriol deficiency, low 25-hydroxyvitamin D, phosphate load</td><td>Is vitamin D low? Has protein or processed food intake risen?</td></tr>
<tr><td>Calcium rising</td><td>Calcium binder, vitamin D analog, high dialysate calcium, immobility</td><td>What calcium-containing tablets and supplements is the patient taking?</td></tr>
<tr><td>PTH very low with high calcium</td><td>Oversuppression, adynamic bone</td><td>Can calcium and vitamin D loads be reduced?</td></tr>
<tr><td>Alkaline phosphatase rising with PTH</td><td>High bone turnover</td><td>Is PTH-lowering therapy needed?</td></tr>
</tbody></table></div>
<p>In the Philippines a PTH costs far more than an alkaline phosphatase, and many patients pay out of pocket between dialysis packages. A rising alkaline phosphatase with normal liver tests is a cheap clue that bone turnover is climbing and that a PTH is worth paying for.</p>
{{call:Stop and call the attending nephrologist when <ul><li>a patient has tingling, muscle spasm, tetany or seizures with a low calcium;</li><li>corrected calcium is high with confusion, vomiting or new arrhythmia;</li><li>a dialysis patient has new painful, purplish skin lesions or ulcers on the thighs or abdomen, which may be calciphylaxis;</li><li>calcium falls sharply after parathyroid surgery.</li></ul>Do this per unit protocol, but always ask the attending nephrologist for guidance.}}
{{key:Never treat a single phosphate or PTH value. Line up at least three results with dates, correct the calcium, write the assay&rsquo;s upper limit beside the PTH, and then ask what changed.}}
"""),
        ("treatment", "Treatment", "Treatment: lower phosphate, spare calcium, and keep PTH in range", """
<p>Treatment follows the chain. Reduce the phosphate load, avoid adding calcium, correct vitamin D deficiency, and keep PTH from climbing out of range. Phosphate, calcium and PTH are surrogate markers. No trial has shown that hitting a phosphate value prolongs life, and the guideline grades reflect that.</p>
<div class="table-wrap"><table>
<thead><tr><th>KDIGO 2017 treatment statement</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>Lower elevated phosphate toward the normal range</td><td>2C</td></tr>
<tr><td>Avoid hypercalcemia in adults</td><td>2C</td></tr>
<tr><td>Use dialysate calcium of 1.25 to 1.50 mmol/L</td><td>2C</td></tr>
<tr><td>Start phosphate-lowering treatment for persistently or progressively high phosphate, not pre-emptively</td><td>Not graded</td></tr>
<tr><td>Restrict the dose of calcium-based phosphate binders in adults</td><td>2B</td></tr>
<tr><td>Avoid long-term aluminum-containing binders and aluminum contamination of dialysate</td><td>1C</td></tr>
<tr><td>Limit dietary phosphate, alone or with other treatments</td><td>2D</td></tr>
<tr><td>Increase dialytic phosphate removal for persistent hyperphosphatemia</td><td>2C</td></tr>
<tr><td>Not on dialysis: when PTH is rising or persistently high, evaluate phosphate, calcium, phosphate intake and vitamin D deficiency</td><td>2C</td></tr>
<tr><td>Not on dialysis: do not routinely use calcitriol or vitamin D analogs in CKD G3a&ndash;G5</td><td>2C</td></tr>
<tr><td>Reserve calcitriol or analogs for CKD G4&ndash;G5 with severe and progressive hyperparathyroidism</td><td>Not graded</td></tr>
<tr><td>Dialysis: keep intact PTH at about 2 to 9 times the assay&rsquo;s upper normal limit</td><td>2C</td></tr>
<tr><td>Dialysis, PTH-lowering therapy: calcimimetics, calcitriol or vitamin D analogs, or a combination</td><td>2B</td></tr>
<tr><td>Severe hyperparathyroidism not responding to medical therapy: consider parathyroidectomy</td><td>2B</td></tr>
</tbody></table></div>
<p>Every statement and grade in this table is from the KDIGO 2017 summary.[[ntr15_1]] Notice that most are weak suggestions on low-quality evidence, and several are ungraded. The strongest statements are about what to avoid: aluminum and excess calcium.</p>
<h3>Why spare calcium</h3>
<p>A calcium binder lowers phosphate, but part of the calcium is absorbed. A patient with adynamic bone cannot store it, so it may go to vessel walls. Jamal and colleagues pooled 11 randomized trials with 4,622 patients and found that those assigned to non-calcium-based binders had 22% lower all-cause mortality than those on calcium-based binders (risk ratio 0.78, 95% confidence interval 0.61 to 0.98).[[ntr15_5]] The trials were mostly small, open label and heterogeneous, and the meta-analysis does not give a reliable absolute difference for an individual patient. KDIGO turned this into a suggestion to restrict calcium binder doses (2B), not a ban.[[ntr15_1]]</p>
<h3>Calcimimetics: a strong surrogate effect, a neutral outcome trial</h3>
<p>Calcimimetics make the parathyroid calcium-sensing receptor more sensitive, so PTH falls. EVOLVE randomized 3,883 hemodialysis patients with moderate to severe secondary hyperparathyroidism to cinacalcet or placebo on top of usual care. In the unadjusted intention-to-treat analysis, the composite of death, myocardial infarction, admission for unstable angina, heart failure or a peripheral vascular event occurred in 48.2% on cinacalcet and 49.2% on placebo (HR 0.93, 95% confidence interval 0.85 to 1.02). Hypocalcemia and gastrointestinal effects were more frequent with cinacalcet.[[ntr15_4]] The drug lowered PTH reliably; it did not significantly reduce hard events in the main analysis. That is the lesson of every CKD-MBD trial so far: a better surrogate does not guarantee a better patient outcome.</p>
<h3>The Philippine reality</h3>
<p>Calcium carbonate is cheap and widely sold. Non-calcium binders, calcimimetics and active vitamin D analogs cost far more, and most families pay out of pocket for take-home medicines even when the dialysis session itself is covered. Parathyroidectomy needs an experienced surgeon and a hospital that can manage the severe hypocalcemia that can follow. A plan that the family cannot afford is not a plan. Ask what the patient can buy every month, then choose the option with the best evidence inside that budget, and document the conversation.</p>
<p>Dialysis time matters too. Phosphate removal depends on time on dialysis more than on almost anything else in the prescription. A patient who dialyzes twice a week because of transport costs will struggle to control phosphate with tablets alone. KDIGO suggests increasing dialytic removal for persistent hyperphosphatemia (2C).[[ntr15_1]] PhilHealth covers up to 156 sessions a year for patients registered in the PhilHealth Dialysis Database (PDD), enough for three sessions a week, but the fare and the lost wages are not covered.[[ntr15_2]] Help the family look for transport support from the local government or the Malasakit Center before accepting twice-weekly dialysis as fixed.</p>
{{flow:Monthly CKD-MBD review|Line up the trend::Phosphate, corrected calcium, PTH with its assay limit, alkaline phosphatase, over at least three results.|Check intake::Processed foods, soft drinks, protein sources, and calcium or vitamin D supplements bought without prescription.|Check the binder::Is it taken with meals, not at bedtime? Is it affordable every month?|Check dialysis::Sessions per week, hours per session, missed sessions.|Check vitamin D::25-hydroxyvitamin D if not recently measured.|Then consider medicines::Binder type, calcitriol or analogs, calcimimetics, within the KDIGO statements and the family&rsquo;s budget.|Refer::Severe, rising PTH despite medical therapy: discuss parathyroidectomy with the attending nephrologist.}}
{{key:Fix the driver before adding a drug: a binder taken with meals, fewer additive-laden foods, enough dialysis time and corrected vitamin D come before a calcimimetic.}}
"""),
        ("nutrition", "Nutrition", "Nutrition: phosphate sources, protein targets and the Filipino plate", """
<p>Not all phosphate is equal. Phosphate in plant foods such as beans and grains is partly bound in phytate, which humans digest poorly, so less of it is absorbed. Phosphate in meat and dairy is absorbed more readily. Inorganic phosphate added to processed foods as a preservative, leavening or flavor enhancer is absorbed most completely. KDIGO 2017 suggests limiting dietary phosphate (2D) and adds, without a grade, that the source of phosphate should be considered.[[ntr15_1]]</p>
<p>Teaching patients about additives works, modestly. In a cluster randomized trial at 14 hemodialysis facilities, 279 patients with high phosphate were assigned to education on avoiding foods with phosphorus additives or to usual care. After three months the fall in serum phosphate was 0.6 mg/dL larger with education (95% confidence interval 0.1 to 1.0 mg/dL).[[ntr15_6]] Serum phosphate is a surrogate, and the trial was short, but the intervention cost almost nothing.</p>
{{fig:ntr15_b}}
<div class="table-wrap"><table>
<thead><tr><th>Common Filipino food</th><th>Why it matters for phosphate</th><th>A swap to suggest</th></tr></thead>
<tbody>
<tr><td>Hotdogs, longganisa, tocino, luncheon meat, corned beef</td><td>Processed meats often carry phosphate additives</td><td>Fresh fish, chicken or pork cooked at home, in the portion the dietitian sets</td></tr>
<tr><td>Instant noodles and flavor packets</td><td>Additives and very high sodium</td><td>Rice or fresh noodles with vegetables; half the seasoning</td></tr>
<tr><td>Cola soft drinks</td><td>Phosphoric acid</td><td>Water, within the fluid allowance</td></tr>
<tr><td>Processed cheese, powdered milk drinks</td><td>Dairy phosphate plus additives</td><td>Smaller portions, as the dietitian advises</td></tr>
<tr><td>Bread and baked goods with leavening</td><td>Phosphate-containing leavening agents</td><td>Read the label; choose products without &ldquo;phosph&rdquo; in the ingredient list</td></tr>
</tbody></table></div>
<p>Teach one reading skill: look for the letters &ldquo;phos&rdquo; in the ingredient list, as in sodium phosphate, sodium tripolyphosphate or phosphoric acid. Many local labels list ingredients in English even when the rest of the pack is in Filipino.</p>
<h3>Protein: two guidelines, one direction, different depths</h3>
<p>Protein drives phosphate intake, acid load and, through glomerular hyperfiltration, perhaps kidney decline. Protein is also what keeps muscles and immunity intact, and protein-energy wasting is common in advanced CKD. The guidelines agree on avoiding high intake and disagree on how low to go.</p>
<div class="table-wrap"><table>
<thead><tr><th>Population</th><th>Statement</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>Adults with CKD G3&ndash;G5 (KDIGO 2024)</td><td>Maintain protein intake of 0.8 g/kg body weight per day</td><td>2C</td></tr>
<tr><td>Adults with CKD at risk of progression (KDIGO 2024)</td><td>Avoid high protein intake above 1.3 g/kg per day</td><td>Practice point</td></tr>
<tr><td>Older adults with frailty or sarcopenia (KDIGO 2024)</td><td>Consider higher protein and calorie targets</td><td>Practice point</td></tr>
<tr><td>Metabolically stable CKD 3&ndash;5 without diabetes (KDOQI 2020)</td><td>0.55 to 0.60 g/kg per day, or 0.28 to 0.43 g/kg per day with ketoanalogues, under close clinical supervision</td><td>1A to reduce kidney failure or death; 2C for quality of life</td></tr>
<tr><td>Metabolically stable CKD 3&ndash;5 with diabetes (KDOQI 2020)</td><td>0.6 to 0.8 g/kg per day</td><td>Opinion</td></tr>
<tr><td>Metabolically stable patients on dialysis (KDOQI 2020)</td><td>1.0 to 1.2 g/kg per day</td><td>1C for hemodialysis without diabetes; opinion otherwise</td></tr>
</tbody></table></div>
<p>The KDIGO statements come from the 2024 CKD guideline and the KDOQI statements from the 2020 nutrition guideline.[[ntr15_7]][[ntr15_8]] Why the difference? KDOQI attaches its low targets to a condition: a metabolically stable patient under close supervision, ideally by a renal dietitian. KDIGO writes for a global audience in which many patients have no dietitian, and it sets a target close to the general population&rsquo;s recommended intake while warning against excess. The two are compatible if you read them as steps. Move a patient eating 1.5 g/kg toward 0.8 first. Go lower only for a stable, well-nourished patient who wants to, with dietitian support and monitoring of weight, albumin and muscle.</p>
<h3>Ketoanalogues: what one trial showed</h3>
<p>Garneata and colleagues randomized nondiabetic adults with stable eGFR below 30 mL/min/1.73 m&sup2;, proteinuria below 1 g/g and good nutrition, after a run-in on a low-protein diet, to a vegetarian very low-protein diet with ketoanalogues or to continued conventional low-protein diet for 15 months. The adjusted NNT to avoid the composite of starting kidney replacement therapy or a fall in eGFR of more than 50% was 4.4 in the intention-to-treat analysis. Nutritional measures did not worsen. Only 14% of screened patients were randomized.[[ntr15_9]] The result is promising for a highly selected, motivated group in one country; it is not evidence for an unselected clinic population.</p>
<p>In the Philippines, rice supplies a large share of protein in many diets, and fish, chicken and pork are bought daily in small amounts. Ketoanalogues are an out-of-pocket cost. Renal dietitians are few outside large cities. Use the Renal Dietitian track and the site&rsquo;s nutrition calculators, and plan with the family who buys and cooks the food. Answer the patient who asks whether to stop meat altogether with a clear no: on dialysis he needs more protein, not less.</p>
{{key:Protein advice depends on the stage. Not on dialysis: steer away from high intake, toward 0.8 g/kg, and lower only with supervision. On dialysis: 1.0 to 1.2 g/kg, with phosphate managed by food choice, binders and dialysis time, not by starving the patient.}}
"""),
    ],
    "debrief": ["""
<p><strong>Reading the trend.</strong> Over nine months his phosphate, PTH and alkaline phosphatase have all risen together, and PTH is now about 14 times the assay&rsquo;s upper limit, well above the KDIGO dialysis range of about 2 to 9 times (2C). Calcium is high-normal. This is progressive secondary hyperparathyroidism with high bone turnover, which fits his bone pain, and the phosphate load fits his itch. The drivers are visible: binder taken at night instead of with meals, processed meats, instant noodles and cola every shift, and only two dialysis sessions a week.</p>
""", """
<p><strong>What to change first.</strong> Move the calcium carbonate to mealtimes, where it binds food phosphate, and ask whether the family can afford it every month. With the dietitian, swap the hotdogs, luncheon meat and noodles for fresh fish or chicken, and replace the cola with water within his fluid allowance; show him how to look for &ldquo;phos&rdquo; on labels. Tell him clearly not to stop eating protein; on dialysis he needs about 1.0 to 1.2 g/kg per day. Work with the social worker on transport help so he can return to three sessions a week, which PhilHealth covers if he is registered in the PDD. Check 25-hydroxyvitamin D. Because his calcium is already high-normal, avoid adding more calcium load.</p>
""", """
<p><strong>If PTH keeps rising.</strong> KDIGO suggests calcimimetics, calcitriol or vitamin D analogs, or a combination, for dialysis patients who need PTH-lowering therapy (2B). With his calcium at 9.6 mg/dL, a calcimimetic or a lower-calcium strategy is preferable to piling on calcitriol, and a non-calcium binder would help if he can afford it. Explain honestly that EVOLVE showed reliable PTH lowering without a significant fall in cardiovascular events in its main analysis. If PTH stays severely high despite medical therapy, KDIGO suggests considering parathyroidectomy (2B); discuss referral with the attending nephrologist and plan for postoperative calcium monitoring.</p>
"""],
    "skills": {"title": "CKD-MBD laboratory review and diet counseling",
               "intro": "Complete with a preceptor on two patients with CKD G4&ndash;G5 or on dialysis. Sign-off is local.",
               "items": [
                   ("Lines up at least three dated results of phosphate, corrected calcium, PTH (with assay upper limit) and alkaline phosphatase.", False),
                   ("Names the most likely driver of each abnormal trend and the question that tests it.", False),
                   ("States the KDIGO 2017 PTH range on dialysis and the statement on calcium-based binders, with grades.", False),
                   ("Takes a diet history that identifies processed foods, soft drinks and supplements, and teaches the patient to find &ldquo;phos&rdquo; on a label.", False),
                   ("Sets a protein target appropriate to the stage, naming the KDIGO 2024 or KDOQI 2020 source and grade.", False),
               ],
               "placement": "Hemodialysis unit, CKD clinic or renal ward"},
    "quiz": [
        ("A patient&rsquo;s measured calcium is 8.0 mg/dL and albumin is 2.0 g/dL. What should the intern report?",
         ["Calcium 8.0 mg/dL, low",
          "Corrected calcium about 9.6 mg/dL, within the usual range",
          "Corrected calcium about 6.4 mg/dL, severely low",
          "Calcium cannot be interpreted without a PTH"], 1,
         "Corrected calcium = 8.0 + 0.8 &times; (4.0 &minus; 2.0) = 9.6 mg/dL. Reporting 8.0 as low ignores the albumin effect and could lead to unneeded calcium. Subtracting instead of adding gives the wrong 6.4."),
        ("A man with CKD G4 has normal phosphate and calcium, but PTH has risen on three consecutive results. What does KDIGO 2017 suggest first?",
         ["Start calcitriol routinely",
          "Evaluate modifiable factors: phosphate, calcium, phosphate intake and vitamin D deficiency (2C)",
          "Refer for parathyroidectomy",
          "Ignore PTH until he starts dialysis"], 1,
         "For CKD G3a&ndash;G5 not on dialysis, KDIGO suggests evaluating modifiable factors when PTH is rising or persistently high (2C), and suggests not using calcitriol or analogs routinely (2C)."),
        ("A fellow is asked why KDOQI 2020 and KDIGO 2024 give different protein targets for CKD not on dialysis. Which answer is best?",
         ["KDIGO recommends a high-protein diet",
          "KDOQI suggests 0.55 to 0.60 g/kg per day for stable patients without diabetes under close supervision (1A for kidney failure or death), while KDIGO suggests 0.8 g/kg per day (2C) for a global audience and warns against above 1.3 g/kg",
          "The guidelines agree exactly",
          "KDOQI applies only to dialysis patients"], 1,
         "Both avoid high intake. KDOQI goes lower but ties its target to supervision and metabolic stability; KDIGO sets a target near the general recommended intake. The first option misstates KDIGO, which warns against high intake."),
        ("A hemodialysis patient in Batangas has phosphate 7.4 mg/dL, calcium 10.1 mg/dL and PTH within the KDIGO range. He takes calcium carbonate with meals. What is the most appropriate step?",
         ["Add calcitriol",
          "Increase calcium carbonate",
          "Review diet and dialysis time and discuss a non-calcium binder, since KDIGO suggests avoiding hypercalcemia (2C) and restricting calcium-based binders (2B)",
          "Stop all binders"], 2,
         "Adding calcium or calcitriol would worsen hypercalcemia. Stopping binders would leave phosphate higher. Lowering the phosphate load without adding calcium is the guideline direction."),
        ("A 62-year-old woman on dialysis has new, very painful purplish skin lesions on her thighs. What should the resident do?",
         ["Apply a topical steroid and review in a month",
          "Treat as cellulitis only",
          "Call the attending nephrologist now because this may be calciphylaxis",
          "Wait for the next monthly laboratory results"], 2,
         "Painful violaceous lesions or ulcers in a dialysis patient raise concern for calciphylaxis, which carries high mortality and needs urgent attending input. Treating it as simple cellulitis risks missing it."),
    ],
    "terms": [
        ("CKD", "Chronic kidney disease"),
        ("CKD-MBD", "Chronic kidney disease&ndash;mineral and bone disorder"),
        ("CRIC", "Chronic Renal Insufficiency Cohort"),
        ("eGFR", "Estimated glomerular filtration rate"),
        ("EVOLVE", "Evaluation of Cinacalcet Hydrochloride Therapy to Lower Cardiovascular Events (trial)"),
        ("FGF23", "Fibroblast growth factor 23"),
        ("HR", "Hazard ratio"),
        ("KDIGO", "Kidney Disease: Improving Global Outcomes"),
        ("KDOQI", "Kidney Disease Outcomes Quality Initiative"),
        ("NNT", "Number needed to treat"),
        ("PDD", "PhilHealth Dialysis Database"),
        ("PTH", "Parathyroid hormone"),
    ],
    "readings": [
        ("phosphorus-ckd.html", "Phosphorus and CKD"),
        ("nutrition-labels-ckd.html", "Reading Nutrition Labels with CKD"),
        ("renal-dietitian-07-phosphorus-calcium-bone.html", "Renal Dietitian, Module 7: Phosphorus, calcium and bone"),
        ("renal-dietitian-04-energy-protein-eating-patterns.html", "Renal Dietitian, Module 4: Energy, protein and eating patterns"),
    ],
    "calcs": ["calc-ckd-mbd.html", "calc-corrected-calcium.html", "calc-phosphorus-load.html", "calc-ckd-nutrition-rx.html",
              "calc-ketoanalogue-dose.html", "calc-nutrition-screening.html", "calc-vitamin-d-dose.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
