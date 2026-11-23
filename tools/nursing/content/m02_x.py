# -*- coding: utf-8 -*-
OBJECTIVES = [
    "Use the risk grid to explain how often a patient needs monitoring.",
    "Describe each element of the plan that slows progression and the nursing checks that go with it.",
    "Give safe temporary-illness (sick-day) and kidney-protection advice.",
]
EXTRA = [
    {"after": "physiology", "id": "causes", "nav": "Causes and risk grid", "tag": "Classification in practice", "h2": "Cause, risk, and how often to look",
     "html": """
<p><strong>Cause comes first.</strong> Diabetes and hypertension cause most chronic kidney disease (CKD) in the Philippines, as elsewhere. Chronic glomerulonephritis, obstruction and stones, and polycystic kidney disease follow. In some patients no cause is ever found. The cause changes management. Glomerular disease may need immunosuppression. Obstruction needs relief. Inherited disease matters for relatives. When a chart says only &ldquo;CKD,&rdquo; ask: due to what?</p>
<p><strong>The risk grid.</strong> The Kidney Disease: Improving Global Outcomes (KDIGO) guideline combines the two axes into a color-coded grid. Each cell carries a risk level and a suggested minimum number of kidney-function and albuminuria checks per year.[[ckd2024]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Filtration category</th><th>A1 (below 30 mg/g)</th><th>A2 (30 to 299 mg/g)</th><th>A3 (300 mg/g or higher)</th></tr></thead>
<tbody>
<tr><td>G1 (90 or higher)</td><td>Low risk; yearly if chronic kidney disease is present</td><td>Moderately increased; yearly</td><td>High; 3 times a year</td></tr>
<tr><td>G2 (60 to 89)</td><td>Low risk; yearly if chronic kidney disease is present</td><td>Moderately increased; yearly</td><td>High; 3 times a year</td></tr>
<tr><td>G3a (45 to 59)</td><td>Moderately increased; yearly</td><td>High; twice a year</td><td>Very high; 3 times a year</td></tr>
<tr><td>G3b (30 to 44)</td><td>High; twice a year</td><td>Very high; 3 times a year</td><td>Very high; 3 times a year</td></tr>
<tr><td>G4 (15 to 29)</td><td>Very high; 3 times a year</td><td>Very high; 3 times a year</td><td>Very high; 4 or more times a year</td></tr>
<tr><td>G5 (below 15)</td><td>Very high; 4 or more times a year</td><td>Very high; 4 or more times a year</td><td>Very high; 4 or more times a year</td></tr>
</tbody></table></div>
<p>The frequencies are minimums. Sicker or less stable patients are seen more often. For you, running a clinic list, the grid answers one practical question: whose follow-up is overdue?</p>
<p><strong>What counts as progression.</strong> Estimated glomerular filtration rate (eGFR) varies from test to test with hydration, diet, and laboratory method. Ungraded KDIGO 2024 practice points say that a change in eGFR of more than 20% between tests exceeds expected variability and warrants evaluation, and that a fall of more than 30% after starting a renin&ndash;angiotensin system inhibitor or a sodium-glucose cotransporter-2 (SGLT2) inhibitor does the same.[[ckd2024]] The earlier 2012 edition defined progression as a drop to a lower category together with a fall of 25% or more from baseline, and rapid progression as a sustained decline of more than 5 mL/min/1.73 m&sup2; per year. Many clinicians still use those terms.</p>
<p><strong>A single lower value during an illness is rechecked before anyone calls it progression.</strong></p>
"""},
    {"after": "evidence", "id": "slowing", "nav": "The treatment plan", "tag": "Clinical application", "h2": "The plan that slows progression, and the nursing checks for each part",
     "html": """
<p>Each part of the plan below has its own strength of evidence. The guideline&rsquo;s own words tell you which: &ldquo;we recommend&rdquo; is a level 1 recommendation, &ldquo;we suggest&rdquo; is level 2, and practice points are ungraded.</p>
<div class="table-wrap"><table>
<thead><tr><th>Element</th><th>What the guideline advises</th><th>Nursing checks and teaching</th></tr></thead>
<tbody>
<tr><td>Blood pressure</td><td>A suggested systolic target below 120 mmHg when tolerated, using standardized office measurement (level 2B); less strict targets for frail people or those with symptoms on standing[[bp2021]]</td><td>Measure correctly every visit; ask about dizziness and falls; teach home monitoring and bringing the record</td></tr>
<tr><td>Renin–angiotensin system inhibitor</td><td>Recommended for CKD with severely increased albuminuria, and for moderately or severely increased albuminuria when diabetes is present (level 1B), at the highest tolerated dose. Suggested for moderately increased albuminuria without diabetes (level 2C)[[ckd2024]]</td><td>Creatinine and potassium are checked within 2 to 4 weeks of starting or increasing. A creatinine rise of up to 30% is accepted and is not a reason to stop; a larger rise or high potassium is reported. Ask about cough and facial swelling. Not used in pregnancy</td></tr>
<tr><td>SGLT2 inhibitor</td><td>Recommended for adults with CKD and type 2 diabetes, heart failure, or an albumin-to-creatinine ratio of 200 mg/g or more (level 1A), started when eGFR is 20 or higher and usually continued until dialysis[[ckd2024]]</td><td>A small early dip in eGFR is expected. Teach genital hygiene (yeast infections are the commonest side effect), to follow the prescriber&rsquo;s written plan for pausing and restarting the medicine during illness with poor intake and before major surgery, and to report nausea, vomiting, or abdominal pain, which can signal ketoacidosis even with near-normal blood sugar</td></tr>
<tr><td>Other diabetes-specific agents</td><td>A nonsteroidal mineralocorticoid receptor antagonist (finerenone) and glucagon-like peptide-1 receptor agonists have trial evidence of kidney or cardiovascular benefit in type 2 diabetes with CKD[[ckd2024]]</td><td>Potassium monitoring with finerenone; nausea and injection technique with the injectable agents</td></tr>
<tr><td>Blood sugar</td><td>An individualized glycated hemoglobin target, generally from below 6.5% to below 8%, less strict where hypoglycemia risk is high[[kdigo2022dm]]</td><td>Hypoglycemia becomes more likely as kidney function falls, because insulin and some tablets last longer. Metformin is reduced when eGFR falls below 45 and stopped below 30</td></tr>
<tr><td>Lipids</td><td>A statin, or a statin with ezetimibe, for adults aged 50 and older with CKD not on dialysis (level 1A when eGFR is below 60)[[ckd2024]]</td><td>Adherence; muscle symptoms</td></tr>
<tr><td>Sodium</td><td>A suggested intake below 2 g of sodium (5 g of salt) a day (level 2C)[[ckd2024]]</td><td>Identify the patient&rsquo;s main sources: fish sauce, soy sauce, shrimp paste, bouillon cubes, instant noodles, dried and canned fish, processed meats. Suggest calamansi, vinegar, garlic, onion, and ginger for flavor. Warn against potassium-based salt substitutes</td></tr>
<tr><td>Protein</td><td>A suggested intake of 0.8 g/kg per day for adults with stages 3 to 5 not on dialysis (level 2C); avoid high intakes; lower intakes only under dietitian supervision[[ckd2024]]</td><td>Screen for weight loss before reinforcing restriction (Module 3)</td></tr>
<tr><td>Activity, weight, tobacco</td><td>At least 150 minutes a week of moderate activity as tolerated; stop smoking</td><td>Ask, advise, refer</td></tr>
</tbody></table></div>
<p>The 30% rule deserves a sentence, because you will field the worried phone calls. These medicines lower the pressure inside the glomerulus. Lower pressure means slightly less filtration today, seen as a small creatinine rise. The trials above show fewer patients reaching kidney failure over the following years. Stopping the medicine for a modest rise trades that long-term protection for a better-looking number.</p>
<p><strong>A small creatinine rise after one of these medicines is expected. Report it, and do not let it become a reason the medicine quietly stops.</strong></p>
"""},
    {"after": "bedside", "id": "protect", "nav": "Kidney protection", "tag": "Clinical application", "h2": "Protecting the kidneys that remain",
     "html": """
<p><strong>Temporary-illness advice.</strong> During vomiting, diarrhea, or fever with poor intake, the kidney leans on the very mechanisms that several common medicines block. Many clinics teach patients to pause a short list of medicines until they have been eating and drinking normally for 24 to 48 hours, then restart them. The usual list is renin–angiotensin system inhibitors, diuretics, SGLT2 inhibitors, metformin, and nonsteroidal anti-inflammatory drugs. The evidence for this advice is limited. Give it only with the prescriber&rsquo;s agreement and in writing, because the commoner harm is a medicine that is stopped and never restarted. At the next visit, ask: &ldquo;Did you restart everything?&rdquo;</p>
<p><strong>Hazards to flag.</strong></p>
<ul>
<li><strong>Contrast studies.</strong> The risk from intravenous contrast is lower than once thought, but it is not zero at low filtration rates. Make sure the requesting team knows the eGFR, that the patient is not dehydrated, and that pausing metformin has been considered.</li>
<li><strong>Bowel preparations and enemas containing phosphate.</strong> These can cause acute phosphate injury to the kidney and dangerous phosphate levels in advanced CKD.</li>
<li><strong>Antacids and laxatives containing magnesium or aluminum.</strong> Both accumulate.</li>
<li><strong>Herbal and &ldquo;kidney cleansing&rdquo; products.</strong> Contents are often unknown. Some contain agents toxic to the kidney or large amounts of potassium. Ask without judgment and record the product.</li>
<li><strong>Dose-dependent medicines.</strong> Many antibiotics, gabapentin and pregabalin, some blood thinners, and several diabetes medicines need dose changes as function falls. An up-to-date eGFR on the chart is a safety measure.</li>
</ul>
<p><strong>Vaccination.</strong> People with CKD respond less well to vaccines as function declines, so they are vaccinated early: influenza yearly, pneumococcal vaccine, and hepatitis B for those likely to need dialysis, with the antibody response checked afterward. The schedule follows national immunization guidance and the prescriber.</p>
<p><strong>Thinking ahead at stage 4.</strong> Once eGFR is below 30, three things begin together. Education about treatment options starts (Module 5). Arm veins are protected: no needles or cannulas in the forearm or upper arm of the non-dominant side (Module 7). Assessment for transplantation begins. These are nursing prompts as much as medical ones.</p>
<p><strong>Every pause needs a restart date. Every eGFR below 30 needs a protected arm.</strong></p>
"""},
]
QUIZ = [
    {"stem": "Three weeks after a renin–angiotensin system inhibitor is started, a patient&rsquo;s creatinine has risen from 1.5 to 1.8 mg/dL and potassium is 4.8 mmol/L. She feels well. What should you expect?",
     "options": [
         ("The medicine will be stopped permanently because it is damaging the kidney", False, "A rise of 20% is within the expected range. It reflects lower pressure in the glomerulus, not injury."),
         ("The dose will be doubled immediately", False, "Dose changes are made by the prescriber after reviewing the results. The rise itself does not call for an increase."),
         ("The medicine is usually continued, because a creatinine rise of up to 30% is acceptable, with repeat monitoring", True, "A KDIGO practice point advises continuing unless creatinine rises by more than 30% within 4 weeks. Report the results, and monitoring continues."),
         ("The result should be ignored and not reported", False, "Expected changes are still reported so the prescriber can confirm the plan."),
     ],
     "objective": "Describe each element of the plan that slows progression and the nursing checks that go with it.", "sources": ["ckd2024"], "flag": ""},
    {"stem": "A patient with stage 3b CKD taking an SGLT2 inhibitor, a diuretic, and a renin–angiotensin system inhibitor telephones with two days of vomiting and diarrhea and little oral intake. Which response is most appropriate?",
     "options": [
         ("Advise him to continue all medicines and drink more water", False, "Continuing these agents during volume depletion raises the risk of acute kidney injury and, with the SGLT2 inhibitor, ketoacidosis."),
         ("Advise him to stop all his medicines permanently", False, "The pause is temporary. Stopping for good removes proven protection."),
         ("Tell him to take an anti-inflammatory tablet for the abdominal discomfort", False, "This adds another kidney hazard."),
         ("Follow the clinic's temporary-illness plan: arrange same-day assessment, confirm with the prescriber which medicines to pause, and make sure they are restarted on recovery", True, "Volume loss with these medicines is a recognized setting for acute kidney injury. Pausing is directed by the prescriber, and restarting is the step most often missed."),
     ],
     "objective": "Give safe temporary-illness (sick-day) and kidney-protection advice.", "sources": ["ckd2024"], "flag": "Sick-day rules are consensus practice with limited evidence; use only as agreed locally."},
]
TERMS = [
    ("Sick-day rules", "Written advice to pause specified medicines temporarily during an illness that causes dehydration."),
    ("Glycated hemoglobin", "A blood test reflecting average blood sugar over about 3 months."),
]
FLAGS = ["Risk-grid monitoring frequencies and the 20% and 30% change thresholds are from KDIGO 2024; the 25% and 5 mL/min/1.73 m2 per year progression definitions are from the 2012 edition. Confirm against the sources before publication. Vaccination paragraph is uncited pending a Philippine immunization source. KDIGO grades added in this pass (BP target 2B, RASi 1B/2C, SGLT2i 1A, statin 1A, sodium 2C, protein 2C, risk equation 1A) were checked against the KDIGO 2024 summary of recommendations and the KDIGO 2021 BP guideline. The glycated hemoglobin range is from the KDIGO 2022 diabetes in CKD guideline (kdigo2022dm); confirm the wording against the full text."]
