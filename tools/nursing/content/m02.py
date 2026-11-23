# -*- coding: utf-8 -*-
MODULE = {
    "sub": "How chronic kidney disease is confirmed, staged, and tracked, why chronicity takes three months to prove, and where nursing review of medicines changes the course of the disease.",
    "desc": "Module 2 of the Nephrology Nursing & Hemodialysis self-study series: confirming chronicity, cause-GFR-albuminuria staging, progression risk, referral clues, and medication reconciliation for registered nurses.",
    "keywords": "CKD staging nursing, G3a A2, eGFR chronicity, albuminuria categories, NSAID kidney, medication reconciliation CKD, KDIGO 2024",
    "objectives": [
        "State the definition of chronic kidney disease and explain why one abnormal result does not establish it.",
        "Stage a patient by cause, glomerular filtration rate category, and albuminuria category.",
        "Identify features that suggest faster progression or the need for nephrology referral.",
        "Carry out a kidney-focused medication reconciliation, including nonprescription pain relievers and herbal products.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "A slow leak, measured twice",
         "html": """
<p>Chronic kidney disease (CKD) behaves like a slow leak in a water tank. One reading of the level tells you where the water stands today; it cannot tell you whether the level is falling, steady, or recovering from a temporary dip. To call the problem chronic, you need a second reading separated in time. That is the whole logic of the three-month rule, and it protects patients from two opposite errors: labeling a temporary drop as lifelong disease, and dismissing a steady decline as a one-time abnormal result.</p>
"""},
        {"id": "physiology", "nav": "Definition and staging", "tag": "Physiology", "h2": "Definition, categories, and what they mean",
         "html": """
<p>The Kidney Disease: Improving Global Outcomes (KDIGO) 2024 guideline defines CKD as abnormalities of kidney structure or function, present for a minimum of 3 months, with implications for health.[[ckd2024]] The usual evidence is a glomerular filtration rate (GFR), reported by the laboratory as the estimated glomerular filtration rate (eGFR), below 60 mL/min/1.73 m&sup2;, or a marker of kidney damage such as albumin in the urine, abnormal urine sediment, or structural abnormality on imaging. A reduced eGFR that has been present for less than 3 months may be acute kidney injury (AKI) or acute kidney disease (AKD), which are managed differently (Module 4).</p>
<p>Once chronicity is established, CKD is classified by <strong>C</strong>ause, <strong>G</strong>FR category, and <strong>A</strong>lbuminuria category. Albuminuria is measured as the urine albumin-to-creatinine ratio (ACR).</p>
<div class="table-wrap"><table>
<thead><tr><th>GFR category</th><th>eGFR (mL/min/1.73 m&sup2;)</th><th>Albuminuria category</th><th>Urine ACR</th></tr></thead>
<tbody>
<tr><td>G1</td><td>90 or higher</td><td>A1</td><td>Below 30 mg/g (below 3 mg/mmol)</td></tr>
<tr><td>G2</td><td>60 to 89</td><td>A2</td><td>30 to 299 mg/g (3 to 29 mg/mmol)</td></tr>
<tr><td>G3a</td><td>45 to 59</td><td>A3</td><td>300 mg/g or higher (30 mg/mmol or higher)</td></tr>
<tr><td>G3b</td><td>30 to 44</td><td></td><td></td></tr>
<tr><td>G4</td><td>15 to 29</td><td></td><td></td></tr>
<tr><td>G5</td><td>Below 15</td><td></td><td></td></tr>
</tbody></table></div>
<p>The two axes exist because they measure different injuries. A falling eGFR reflects lost filtering units. Albuminuria reflects a leaking filtration barrier and raised pressure inside the remaining glomeruli, and it is both a marker and a contributor to further damage. This is why treatments that lower pressure inside the glomerulus slow progression.</p>
"""},
        {"id": "evidence", "nav": "Progression", "tag": "Evidence", "h2": "Who progresses, and what slows it",
         "html": """
<p>Risk rises with each step down in eGFR and each step up in albuminuria, and the combination predicts kidney failure, cardiovascular events, and death better than either alone.[[ckd2024]] KDIGO recommends using a validated risk equation, such as the Kidney Failure Risk Equation (KFRE), which combines age, sex, eGFR, and urine ACR, to estimate the absolute risk of kidney failure;[[tangri2011]] a 5-year risk of 3% to 5% is a suggested threshold for nephrology referral, and a 2-year risk above 10% for multidisciplinary care.[[ckd2024]] Referral is also indicated for a sustained fall in eGFR, heavy or rising albuminuria, persistent unexplained blood in the urine, hypertension that resists treatment, persistent potassium abnormalities, or hereditary kidney disease.</p>
<p>Randomized trials demonstrate that renin–angiotensin system blockade and sodium-glucose cotransporter-2 (SGLT2) inhibitors reduce the risk of kidney failure in people with albuminuric CKD, and KDIGO gives both strong recommendations in the indicated groups.[[ckd2024]] The size of the effect is worth knowing when a patient asks whether another tablet is worthwhile. In the DAPA-CKD trial, a composite of a sustained halving of eGFR, kidney failure, or death from kidney or cardiovascular causes occurred in 9.2% of participants given dapagliflozin and 14.5% given placebo over a median of 2.4 years, which is about one such event prevented for every 19 people treated.[[dapa2020]] The EMPA-KIDNEY trial extended the finding to a wider range of kidney function and albuminuria: progression of kidney disease or cardiovascular death occurred in 13.1% with empagliflozin and 16.9% with placebo over a median of 2.0 years.[[empa2023]] Blood pressure control, glucose control, and avoidance of further kidney injury complete the plan. Nurses rarely prescribe these agents, but they see whether the patient is taking them, whether they were stopped during an illness and never restarted, and whether a new medicine threatens the kidney.</p>
<p>The class most often implicated is the nonsteroidal anti-inflammatory drug (NSAID). These agents block the prostaglandins that keep blood flowing into the glomerulus when circulation is stressed, so in a person with CKD, dehydration, or concurrent use of a diuretic and a renin–angiotensin blocker, they can precipitate AKI. Many are sold without prescription under several brand names, and patients often do not think of them as medicines.</p>
"""},
        {"id": "bedside", "nav": "Nursing review", "tag": "Clinical application", "h2": "Staging and reconciling at the desk",
         "html": """
<p>At a clinic visit or on admission, the nursing contribution has four parts. First, look for the trend: list every available creatinine and eGFR with its date, and note whether two results at least 3 months apart are both abnormal. Second, check that a urine ACR exists and is recent. Third, record the cause if one is documented, since &ldquo;CKD&rdquo; without a cause is an incomplete diagnosis. Fourth, reconcile medicines.</p>
<p>For a kidney-focused reconciliation, ask about each of the following by name, dose, and frequency: prescription medicines; pain relievers bought over the counter; herbal products and supplements; and anything taken only occasionally. Ask what the patient takes for headache, joint pain, fever, or menstrual pain, because that question surfaces NSAIDs that a general &ldquo;any other medicines?&rdquo; misses. Flag NSAID exposure, duplicate brands of the same agent, and medicines whose dose depends on kidney function for prescriber or pharmacist review. Do not advise the patient to stop a prescribed medicine yourself; record, flag, and make sure the review happens.</p>
"""},
    ],
    "case": {
        "title": "One low result, then a pattern",
        "html": """
<p>Aling Rosario, 58, has had type 2 diabetes for 12 years. A pre-employment check shows an eGFR of 48 mL/min/1.73 m&sup2;. She feels well. At the clinic you find no earlier creatinine on file. She returns four months later: eGFR is 47 and urine ACR is 180 mg/g, the same ACR range as a test done by her company physician three months ago. When asked what she takes for knee pain, she produces two different boxes, both containing an NSAID, which she takes &ldquo;most days.&rdquo;</p>
""",
        "acte": {
            "Assess": "Dates and values of all kidney tests; blood pressure; current medicines by name, dose, and frequency, including both pain-reliever products.",
            "Communicate": "Report to the physician: eGFR 48 then 47 four months apart, ACR 180 mg/g persistent over 3 months (G3a/A2), near-daily use of two NSAID products.",
            "Teach": "What the two tests mean; that both boxes contain the same type of medicine; to ask before taking any pain reliever. Confirm understanding with teach-back.",
            "Escalate": "Reduced urine, vomiting or diarrhea with poor intake, or new swelling while on these medicines needs same-day review.",
        },
        "task": "Document the stage in the cause–GFR–albuminuria format and write the medication list entry for the two pain relievers exactly as you would chart it.",
    },
    "quiz": [
        {"stem": "A 58-year-old woman with diabetes has a single eGFR of 48 mL/min/1.73 m&sup2; and no previous results. A colleague writes &ldquo;CKD stage 3&rdquo; on the referral. What is the most accurate response?",
         "options": [
             ("Agree; an eGFR below 60 defines CKD stage 3", False, "The eGFR falls in the G3a range, but a single value does not show that the abnormality has lasted 3 months."),
             ("One result does not establish chronicity; look for prior results or repeat testing after at least 3 months", True, "CKD requires abnormalities present for a minimum of 3 months. Without earlier results, a reduced eGFR could be acute kidney injury or acute kidney disease."),
             ("Disagree; CKD cannot be diagnosed without a kidney biopsy", False, "Biopsy is needed only when the cause is unclear and the result would change management."),
             ("Disagree; CKD is diagnosed only when eGFR is below 30", False, "CKD includes all GFR categories when markers of damage or reduced eGFR persist for 3 months."),
         ],
         "objective": "State the definition of chronic kidney disease and explain why one abnormal result does not establish it.", "sources": ["ckd2024"], "flag": ""},
        {"stem": "Four months later her eGFR is 47 mL/min/1.73 m&sup2; and her urine ACR has been about 180 mg/g on two tests 3 months apart. How is her CKD categorized?",
         "options": [
             ("G2/A2", False, "G2 is an eGFR of 60 to 89."),
             ("G3b/A2", False, "G3b is an eGFR of 30 to 44."),
             ("G3a/A3", False, "A3 is an ACR of 300 mg/g or higher."),
             ("G3a/A2", True, "An eGFR of 45 to 59 is G3a, and an ACR of 30 to 299 mg/g is A2. Both abnormalities have persisted beyond 3 months, so chronicity is established."),
         ],
         "objective": "Stage a patient by cause, glomerular filtration rate category, and albuminuria category.", "sources": ["ckd2024"], "flag": ""},
        {"stem": "During medication reconciliation the patient says she takes &ldquo;something for my knees&rdquo; most days. What is the best nursing action?",
         "options": [
             ("Record &ldquo;occasional pain reliever&rdquo; and move on", False, "This loses the information the prescriber needs: which agent, how much, and how often."),
             ("Tell her that all pain relievers are safe if taken with food", False, "Food reduces stomach irritation; it does not protect the kidney from NSAID effects."),
             ("Identify each product by name, dose, and frequency, and flag any NSAID exposure for prescriber review", True, "Near-daily NSAID use in CKD can reduce kidney blood flow and precipitate acute kidney injury. Precise documentation and a flagged review are the nursing responsibilities."),
             ("Instruct her to stop all her medicines until she sees the nephrologist", False, "Stopping prescribed medicines without review can cause harm and is outside the nurse&rsquo;s role."),
         ],
         "objective": "Carry out a kidney-focused medication reconciliation, including nonprescription pain relievers and herbal products.", "sources": ["ckd2024"], "flag": "Who reviews flagged medicines (physician or pharmacist) follows local policy."},
    ],
    "reflect": "How does your unit record nonprescription and herbal products? Would a colleague reading your entry know the agent, dose, and frequency?",
    "practice": {
        "intro": "With your preceptor, review three outpatient or ward charts of patients with reduced eGFR.",
        "items": [
            "Lists dated creatinine and eGFR values and states whether chronicity is established.",
            "States the GFR and albuminuria categories, or identifies that an ACR is missing.",
            "Completes a medication reconciliation that names each pain reliever by agent, dose, and frequency.",
            "Flags findings to the prescriber using a structured handoff.",
        ],
    },
    "readings": [
        ("understanding-ckd.html", "The site&rsquo;s core explanation of CKD stages for patients and families."),
        ("slowing-ckd-progression.html", "The treatments that slow progression and why they work."),
        ("pain-management-ckd.html", "Safer approaches to pain in CKD, including NSAID risks."),
    ],
    "calcs": ["calc-egfr-ckd-epi.html", "calc-kfre.html", "calc-ckd-progression-slope.html"],
    "external": [
        ("KDIGO 2024 CKD evaluation and management guideline", "https://kdigo.org/guidelines/ckd-evaluation--and-management/"),
    ],
    "terms": [
        ("Chronicity", "Evidence that an abnormality has persisted for at least 3 months."),
        ("Medication reconciliation", "Building the most accurate list of everything a patient takes and comparing it with current orders."),
    ],
    "image": {
        "file": "renal-nursing-02-ckd-staging",
        "alt": "Nurse reviews kidney function and urine albumin trends with a patient.",
        "purpose": "Show trend review as a shared activity between nurse and patient.",
        "scene": "A Filipina nurse in her forties sits beside, not across from, a woman in her late fifties at an outpatient desk. The nurse points with a pen to a printed sheet of laboratory results lying between them; two small medicine boxes sit near the patient&rsquo;s hand.",
        "focal": "The shared sheet and the two faces turned toward it.",
        "setting": "Small Philippine outpatient clinic room, electric fan, wall calendar without readable text.",
        "details": "Printed results shown as soft, unreadable rows; plain unbranded medicine boxes.",
        "exclusions": "No readable values, names, brand names, or hospital logos; no computer screen content.",
        "archetype": "H (Clinical)", "reviewer": "Renal nurse educator",
    },
    "flags": ["KFRE referral thresholds are KDIGO 2024 practice points; local referral criteria may differ."],
    "crosswalk": {
        "ph": "PSN 2024 nurse training topics: renal physiology, laboratory interpretation",
        "anna": "Chronic kidney disease: identification, staging, slowing progression",
        "edtna": "Chronic kidney disease: assessment and prevention of progression",
        "nncc": "Concepts of kidney disease",
    },
}
