# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 04: Urinalysis, microscopy and renal imaging.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard.
Perazella 2008, Cavanaugh 2019, Koehler 1991, Sumida 2020, Davenport 2020, McDonald 2014, Mehran 2004, O'Neill 2014 and
Bosch 2009 checked against PubMed; KDIGO 2024 albuminuria practice points checked against KDIGO's summary of
recommendations. No doses. Fictional case."""

MODULE = {
    "image_alt": "A nephrology fellow and an intern look through a light microscope at a urine sediment slide in a small hospital laboratory, beside a centrifuge and a cup of tea-colored urine.",
    "objectives": [
        "<strong>Intern:</strong> Collect, label and report a urinalysis correctly, and recognize the dipstick and point-of-care findings, such as blood without red cell (RBC)s or tea-colored urine, that need review the same day.",
        "<strong>Resident:</strong> Interpret urine sediment, quantified protein or albumin and a kidney ultrasound together, with specimen quality and clinical context, and name the kidney syndrome they point to.",
        "<strong>Fellow:</strong> Perform and teach urine microscopy, and integrate sediment, protein quantification and imaging into a decision about biopsy, referral or contrast use.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; reading the urine and the scan</span>An <strong>intern</strong> owns the specimen: a fresh, correctly collected, correctly labeled sample, a dipstick read on time, and a same-day report of anything that does not fit. A <strong>resident</strong> owns the pattern: what the dipstick, the sediment, the protein number and the ultrasound say together. A <strong>fellow</strong> owns the microscope and the decision: spinning and reading the sediment personally, and deciding whether the pattern calls for a biopsy, a referral or a change in imaging plans.</div>
{{plain:Think of the urine as a letter the kidney sends every hour. The dipstick reads the envelope: it tells you something is inside. The microscope opens the letter and reads the handwriting: casts and cells say which part of the kidney wrote it. The ultrasound is a photograph of the post office: its size and shape say whether the problem is new or old.}}
<p>The picture has a limit. A letter says the same thing to every reader. Urine changes within an hour of collection: cells lyse, casts dissolve in alkaline or dilute urine, and bacteria multiply. The dipstick reacts to chemicals, not to cells, so it can call &ldquo;blood&rdquo; when there are no red cells at all, and it reads mainly albumin, so it can miss other proteins. An automated urinalysis counts particles but often cannot tell a granular cast from debris. And an ultrasound shows structure, not function. Each tool answers a narrower question than it seems to, and they become powerful only when read together, in context.</p>
<p>That is why urine microscopy by the physician still matters. Automated analyzers and central laboratories have made it rare for nephrologists to look at sediment themselves, yet it remains one of the most informative tests for acute kidney disease, often identifying the compartment of injury.[[ntr04_4]]</p>
{{cards:Key numbers|Albuminuria categories (KDIGO 2024)::A1 &lt;30 mg/g; A2 30 to 300 mg/g; A3 &gt;300 mg/g urine albumin-to-creatinine ratio (ACR)|Dipstick trace or more for ACR &gt;30 mg/g (Sumida 2020, 919,383 adults)::Sensitivity 62%, specificity 88%|Acanthocytes &ge;5% of urine red cells (K&ouml;hler 1991)::Sensitivity 52%, specificity 98% for glomerular disease|No casts or tubular cells, low prior suspicion of acute tubular necrosis (Perazella 2008)::Negative predictive value 91% for prerenal AKI|Contrast and kidney function (ACR&ndash;NKF 2020)::Prophylaxis indicated for acute kidney injury (AKI) or estimated glomerular filtration rate (eGFR) &lt;30 mL/min/1.73 m&sup2; not on dialysis (consensus statement)}}
<p>Most urinalyses are normal or show a minor, explainable finding. A few carry the first sign of glomerulonephritis, rhabdomyolysis, leptospirosis or obstruction, often before the creatinine moves. Your work is to collect the specimen properly, to look past the dipstick to the sediment and a quantified number, and to read the ultrasound as part of the same story.</p>
""",
    "case": {"title": "Tea-colored urine after the flood", "html": """
<p>Friday, 10 a.m., the emergency room of a public hospital in Marikina, eight days after a typhoon flooded the city. Mr. Jerome Villanueva, 34, a delivery rider, waded through floodwater for two days to reach his customers and help neighbors. For four days he has had fever, severe calf pain and headache. This morning his urine looked &ldquo;like tea,&rdquo; and his wife noticed his eyes were yellow.</p>
<p>He is alert, blood pressure 108/66 mm Hg, pulse 112, temperature 38.6 &deg;C. His sclerae are icteric and both calves are tender. A catheter sample shows dark brown urine. The dipstick reads blood 3+, protein 1+, bilirubin 2+, leukocyte esterase negative. The automated urinalysis reports 0 to 2 red cells per high-power field. His creatinine is 2.8 mg/dL; he has never had a test before. The emergency resident has requested &ldquo;renal ultrasound and urinalysis&rdquo; and asks the renal fellow, Dr. Ana Dimaculangan, whether the urine &ldquo;shows anything more.&rdquo;</p>
""", "questions": [
        "What explains blood 3+ on the dipstick with almost no red cells, and what makes the urine tea-colored?",
        "What would you look for under the microscope, and what would each finding mean?",
        "What do you expect on ultrasound, and how do the urine and imaging change the plan?"]},
    "sections": [
        ("dipstick", "Dipstick and its traps", "The dipstick and its traps", """
<p>The dipstick is a row of chemical pads. Each pad changes color when a particular chemical reaction happens, and the color is read against a chart at a set time. It is cheap, fast and useful, provided you remember what each pad actually detects.</p>
<h3>Collect the specimen well</h3>
<p>A good result starts before the dipstick. Use a fresh midstream sample, or a catheter sample in a patient who cannot void cleanly, and examine it within an hour if possible. For albuminuria, the Kidney Disease: Improving Global Outcomes (KDIGO) 2024 guideline prefers a first-void morning midstream sample in adults and children, and advises confirming a positive reagent strip for albumin or protein by quantitative laboratory measurement.[[ntr04_1]] A sample taken after heavy exercise, during fever or menstruation, or from a urine bag left for hours can mislead.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pad</th><th>What it actually detects</th><th>False positive or misleading</th><th>False negative or missed</th></tr></thead>
<tbody>
<tr><td>Blood</td><td>Peroxidase activity of the heme group</td><td>Hemoglobin from hemolysis and myoglobin from muscle injury, with no red cells; menstrual blood</td><td>High doses of vitamin C (ascorbic acid)</td></tr>
<tr><td>Protein</td><td>Mainly albumin</td><td>Very concentrated or alkaline urine</td><td>Immunoglobulin light chains and other non-albumin proteins; dilute urine</td></tr>
<tr><td>Specific gravity</td><td>Urine concentration</td><td>Contrast media, glucose</td><td>&mdash;</td></tr>
<tr><td>Leukocyte esterase and nitrite</td><td>White cells; bacteria that convert nitrate to nitrite</td><td>Contamination</td><td>Bacteria that do not make nitrite; urine not held in the bladder long enough</td></tr>
<tr><td>Bilirubin and urobilinogen</td><td>Conjugated bilirubin; its gut-derived product</td><td>Some drugs color the urine</td><td>Old specimens exposed to light</td></tr>
<tr><td>Glucose</td><td>Glucose above the tubule&rsquo;s reabsorptive capacity</td><td>&mdash;</td><td>&mdash; (note sodium-glucose cotransporter 2 (SGLT2) inhibitors cause glucosuria at normal blood sugar)</td></tr>
</tbody></table></div>
<h3>Blood without red cells</h3>
<p>The single most useful dipstick trap to know is a strongly positive blood pad with few or no red cells under the microscope. The pad detects heme, and heme is found in hemoglobin and myoglobin as well as in intact red cells. Free pigment in the urine therefore points to hemolysis or to rhabdomyolysis. Myoglobin released from injured muscle is filtered and can cause acute kidney injury (AKI) through tubular obstruction, direct toxicity and vasoconstriction, especially with volume depletion and acidic urine.[[ntr04_10]] A dark urine with heme-positive dipstick and few red cells should prompt a creatine kinase and a look at the serum for hemolysis.</p>
<h3>Tea-colored or dark urine</h3>
<p>Dark urine has several causes, and the dipstick helps to separate them: bilirubin (bilirubin pad positive, often with jaundice), myoglobin or hemoglobin (blood pad positive, few red cells), many red cells (blood pad positive with red cells on microscopy), and concentrated urine or some foods and drugs. More than one can be present at once.</p>
<p><strong>For the intern:</strong> label the sample with the time of collection, send it fresh, and report the same day any heme-positive dipstick with few red cells, any tea-colored urine, and any protein 2+ or more in a patient without a known reason.</p>
{{key:The dipstick reads chemistry, not cells. A strong blood pad with few red cells means pigment, hemoglobin or myoglobin, until proven otherwise.}}
"""),
        ("sediment", "Microscopy", "Urine microscopy: casts, cells and crystals", """
<p>A cast is a cylinder of protein molded inside a tubule. It forms where flow is slow and urine is concentrated and acidic, from a protein secreted by the tubule, and it traps whatever is in that tubule at the time. A cast is therefore a sample of the kidney itself: red cells in a cast must have come from the nephron, not from the bladder or the urethra.</p>
{{fig:ntr04_a}}
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>Where it comes from</th><th>What it points to</th></tr></thead>
<tbody>
<tr><td>Hyaline casts</td><td>Protein alone</td><td>Concentrated urine, often normal</td></tr>
<tr><td>Muddy brown granular casts and renal tubular epithelial cells</td><td>Sloughed, degenerating tubular cells</td><td>Acute tubular injury (acute tubular necrosis, ATN)</td></tr>
<tr><td>Red cell casts; dysmorphic red cells and acanthocytes</td><td>Red cells passing through a damaged glomerular wall</td><td>Glomerulonephritis</td></tr>
<tr><td>White cells and white cell casts</td><td>Inflammation in the interstitium or infection</td><td>Interstitial nephritis, pyelonephritis</td></tr>
<tr><td>Fatty casts, oval fat bodies (Maltese crosses under polarized light)</td><td>Lipid lost with heavy proteinuria</td><td>Nephrotic syndrome</td></tr>
<tr><td>Pigmented granular casts</td><td>Heme pigment in tubular casts</td><td>Rhabdomyolysis or hemolysis with tubular injury</td></tr>
<tr><td>Crystals</td><td>Supersaturated solutes or drugs</td><td>Context dependent: uric acid in tumor lysis, calcium oxalate in some poisonings, drug crystals</td></tr>
</tbody></table></div>
<h3>What the evidence shows</h3>
<p>Perazella and colleagues examined fresh sediment from 267 consecutive hospitalized patients with AKI and built a score from granular casts and renal tubular epithelial cells. In patients first thought to have ATN, any casts or tubular cells (a score of 2 or more) had a very high positive predictive value for a final diagnosis of ATN. In patients first thought to have prerenal AKI, the absence of casts and tubular cells had a sensitivity of 0.73, a specificity of 0.75, and a negative predictive value of 91% for prerenal AKI.[[ntr04_3]] This was a single-center diagnostic study, and the performance depends on who reads the slide, but it shows that the sediment shifts probability in a useful direction.</p>
<p>For glomerular bleeding, K&ouml;hler and colleagues studied phase-contrast microscopy in 351 patients with hematuria and 33 healthy controls. Most kinds of &ldquo;dysmorphic&rdquo; red cells occurred in both glomerular and non-glomerular disease. One form, the acanthocyte, a ring-shaped red cell with blebs, was specific: acanthocytes making up 5% or more of urine red cells had a sensitivity of 52% and a specificity of 98% for biopsy-proven glomerulonephritis.[[ntr04_5]] Read that pair of numbers carefully: finding acanthocytes strongly supports a glomerular source, but missing them does not exclude one.</p>
<h3>How to do it, and teach it</h3>
<p>Spin about 10 mL of fresh urine in a centrifuge, pour off the supernatant, resuspend the pellet in the last few drops, and examine a drop under low then high power, with the condenser lowered to improve contrast. Scan the edges of the coverslip, where casts collect. Many Philippine hospital laboratories report only automated counts; a centrifuge, slides and an ordinary light microscope in the renal office or ward are enough to teach sediment reading. A phone camera held to the eyepiece lets the fellow show the attending what was seen, as long as no patient identifier is in the image.</p>
{{flow:Reading a sediment|Before you spin::Fresh sample, under an hour old if possible; note pH and specific gravity from the dipstick.|Low power::Scan for casts along the edges of the coverslip; count per low-power field.|High power::Identify cells: red cells (shape, acanthocytes), white cells, tubular epithelial cells.|Casts::Name each type: hyaline, granular (muddy brown), red cell, white cell, fatty, pigmented.|Crystals::Note type and quantity; ask about drugs, toxins and tumor treatment.|Put it together::Name the compartment the sediment points to, and how strongly.}}
{{key:Look at the sediment yourself in every unexplained AKI and every patient with blood or protein. Casts tell you which part of the kidney is speaking.}}
"""),
        ("protein", "Quantifying protein", "Quantifying protein and albumin", """
<p>Albumin is a large, negatively charged protein that the healthy glomerular barrier holds back. Small amounts that do leak through are mostly reabsorbed by the proximal tubule. Albuminuria therefore usually means the glomerular barrier is damaged, and its amount carries strong prognostic information for kidney failure and cardiovascular disease. Other proteins, such as immunoglobulin light chains or low-molecular-weight tubular proteins, appear when production overwhelms the tubule or when the tubule fails to reabsorb them.</p>
<h3>Choose the right test</h3>
<div class="table-wrap"><table>
<thead><tr><th>Test</th><th>What it measures</th><th>Use</th><th>Limit</th></tr></thead>
<tbody>
<tr><td>Dipstick protein</td><td>Mainly albumin, semi-quantitative</td><td>Screening where nothing else is available</td><td>Misses moderate albuminuria and light chains; affected by concentration</td></tr>
<tr><td>Urine albumin-to-creatinine ratio (ACR)</td><td>Albumin corrected for urine concentration</td><td>First choice for detecting and staging chronic kidney disease (CKD)</td><td>Varies day to day; raised by exercise, fever, infection, menstruation</td></tr>
<tr><td>Urine protein-to-creatinine ratio (PCR)</td><td>All proteins</td><td>Heavy proteinuria, glomerular disease monitoring, suspected non-albumin proteins</td><td>Less standardized; the relation to ACR is inconsistent at low levels</td></tr>
<tr><td>24-hour urine protein</td><td>Total daily excretion</td><td>When a ratio may mislead (very high or very low muscle mass)</td><td>Incomplete collections are common</td></tr>
</tbody></table></div>
<p>KDIGO 2024 classifies albuminuria by urine ACR into A1 (below 30 mg/g, or 3 mg/mmol), A2 (30 to 300 mg/g) and A3 (above 300 mg/g), and lists urine ACR as the first-choice test, followed by reagent strips for albumin or ACR with automated reading. It asks that positive strips be confirmed by quantitative measurement and that chronicity not be assumed from a single result.[[ntr04_1]]</p>
<h3>When only PCR or a dipstick is available</h3>
<p>Many Philippine clinics have a dipstick and sometimes a PCR, but not an ACR. Sumida and colleagues pooled same-day measurements from 919,383 adults in 33 cohorts to build conversion equations. Above a PCR of about 50 mg/g, the predicted ACR classified screening and A2 and A3 categories with moderate sensitivity and good specificity. A dipstick reading of trace or more had a sensitivity of only 62% and a specificity of 88% for an ACR above 30 mg/g; a reading of 2+ had a sensitivity of 78% and a specificity of 98% for an ACR of 300 mg/g or more.[[ntr04_2]] The practical message: a negative dipstick misses roughly four in ten people with moderately increased albuminuria, so it is a weak screening test in people with diabetes or hypertension. When the dipstick is positive, or when risk is high, get a quantitative measure if the family can afford it.</p>
<p>Albuminuria is also a surrogate in trials. A fall in albuminuria with treatment is associated with slower loss of kidney function, but it is not the outcome the patient feels; kidney failure, death and cardiovascular events are.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>KDIGO 2024 asks for a first morning urine sample for initial testing of albuminuria and proteinuria in children, because upright posture during the day can raise protein in healthy adolescents (orthostatic proteinuria).[[ntr04_1]] Collecting urine for a suspected urinary infection in a child who is not toilet trained needs a catheter or suprapubic sample, or a clean catch; a bag sample is useful only if negative. See <a href="attending-pediatric-nephrologist-07-uti-reflux-bladder.html">Attending Pediatric Nephrologist, Module 7</a>.</div>
{{key:Quantify. Confirm a positive dipstick with an ACR, or a PCR if that is all you have, and do not label albuminuria or CKD from a single sample.}}
"""),
        ("imaging", "Ultrasound, CT, contrast", "Ultrasound, computed tomography and contrast risk", """
<p>Ultrasound is the first imaging test in almost every kidney problem. It is safe, cheap, portable, uses no contrast, and can be done at the bedside by a trained nephrologist. It answers three questions quickly: are there two kidneys, are they obstructed, and do they look acutely or chronically diseased. It also guides procedures such as catheter insertion and kidney biopsy, and its interpretation always depends on the clinical picture.[[ntr04_9]]</p>
{{fig:ntr04_b}}
<div class="table-wrap"><table>
<thead><tr><th>Ultrasound finding</th><th>What it suggests</th><th>Next question</th></tr></thead>
<tbody>
<tr><td>Small kidneys with thin, bright cortex</td><td>Long-standing chronic kidney disease</td><td>Is there an acute change on top? Is a biopsy still useful?</td></tr>
<tr><td>Normal or large kidneys with reduced function</td><td>Acute disease, or chronic diseases that keep kidneys large (diabetes, infiltrative disease, polycystic kidneys)</td><td>Urine sediment and protein; serologies as indicated</td></tr>
<tr><td>Dilated collecting systems (hydronephrosis)</td><td>Obstruction</td><td>Bladder distended? Unilateral or bilateral? Urgent drainage?</td></tr>
<tr><td>Asymmetric kidney sizes</td><td>Renovascular disease, reflux scarring, congenital difference</td><td>Blood pressure history, vascular imaging if it will change care</td></tr>
<tr><td>Cysts or masses</td><td>Simple cysts, polycystic disease, tumor</td><td>Characterize with further imaging as indicated</td></tr>
</tbody></table></div>
<p>Two cautions. Obstruction can exist without visible dilation early on or in a very dry patient, and dilation can persist after an obstruction is relieved. And brightness of the cortex is graded against the liver or spleen, which themselves can be abnormal.</p>
<h3>Computed tomography and iodinated contrast</h3>
<p>Non-contrast computed tomography (CT) is the test of choice for stones. Contrast CT answers many other questions, and the fear of contrast-induced AKI has long made clinicians withhold it. The evidence has shifted. McDonald and colleagues compared 12,508 propensity-matched patients who had contrast-enhanced or unenhanced CT. AKI became more common as baseline eGFR fell, but its incidence did not differ between contrast and non-contrast groups in any eGFR stratum, including eGFR below 30 mL/min/1.73 m&sup2;.[[ntr04_7]] This was a retrospective observational study, and propensity matching cannot remove all bias, because clinicians may have avoided contrast in the sickest patients.</p>
<p>The American College of Radiology and the National Kidney Foundation (ACR&ndash;NKF) consensus statement concluded that the risk of AKI from intravenous iodinated contrast has been overstated, mainly because older studies lacked control groups to separate contrast-induced AKI from AKI that merely coincided with contrast. It states that prophylaxis with intravenous normal saline is indicated for patients with AKI or an eGFR below 30 mL/min/1.73 m&sup2; who are not on maintenance dialysis, and may be considered at 30 to 44 in individual high-risk cases.[[ntr04_6]] This is a consensus statement, not a graded guideline recommendation, and it concerns intravenous contrast for CT.</p>
<p>Intra-arterial contrast for coronary procedures is a different setting. Mehran and colleagues built a risk score from 8,357 patients undergoing percutaneous coronary intervention, using hypotension, intra-aortic balloon pump, heart failure, CKD, diabetes, age over 75, anemia and contrast volume. Contrast nephropathy, defined there as a creatinine rise of 25% or 0.5 mg/dL at 48 hours, occurred in 13.1% overall, ranging from 7.5% at the lowest scores to 57.3% at the highest; the score&rsquo;s discrimination in validation was modest (c statistic 0.67).[[ntr04_8]] Use it to discuss risk with the cardiology team, not to forbid a needed procedure.</p>
<p>In the Philippines, CT is often far from the patient and paid out of pocket, and bedside ultrasound is increasingly available. Do not let contrast fear delay a diagnosis that will change treatment, such as an abscess, a dissection or a pulmonary embolism. Do check volume, stop avoidable nephrotoxins, and follow the hospital&rsquo;s contrast protocol.</p>
{{call:Stop and call the attending nephrologist, per unit protocol, but always ask the attending nephrologist for guidance, when:<ul><li>the urine shows red cell casts or many acanthocytes with a rising creatinine (possible rapidly progressive glomerulonephritis);</li><li>there is bilateral hydronephrosis or obstruction of a single functioning kidney;</li><li>pigment-positive urine comes with a rising creatinine, high potassium or falling urine output;</li><li>a patient with AKI or an eGFR below 30 needs urgent contrast and the team asks how to proceed.</li></ul>}}
{{key:Get an ultrasound in every unexplained kidney problem. Do not withhold contrast that will change management; weigh it against the patient&rsquo;s risk and follow the hospital protocol.}}
"""),
    ],
    "debrief": ["""
<p><strong>Blood without red cells, and the tea color.</strong> The blood pad detects heme. With 0 to 2 red cells per high-power field, the heme is free pigment: myoglobin from muscle injury, hemoglobin from hemolysis, or both. His floodwater exposure, fever, calf pain and jaundice fit severe leptospirosis, for which Philippine clinical practice guidelines set out diagnosis and management;[[ntr04_11]] muscle injury with pigment release is one way it can injure the kidney. The tea color has two sources here: pigment and conjugated bilirubin, which the bilirubin pad and his jaundice confirm. Dr. Dimaculangan asks for creatine kinase, a blood film and lactate dehydrogenase for hemolysis, liver tests and potassium.</p>
""", """
<p><strong>Under the microscope.</strong> She spins a fresh sample herself. Pigmented, muddy brown granular casts and tubular epithelial cells would confirm tubular injury from pigment, sepsis or both. White cells or white cell casts would raise interstitial nephritis, which leptospirosis can also cause. Red cell casts or acanthocytes would point to a glomerular process and change the urgency. She finds pigmented granular casts and tubular cells, no red cell casts and no acanthocytes. The pattern is acute tubular injury with pigment, and the automated &ldquo;0 to 2 red cells&rdquo; report is consistent with it.</p>
""", """
<p><strong>Ultrasound and the plan.</strong> She expects normal-sized or slightly large, swollen kidneys without hydronephrosis, which would support acute disease rather than old CKD. That is what the scan shows. Urine and imaging together say: AKI from pigment and tubular injury in suspected severe leptospirosis, not obstruction and not glomerulonephritis. The plan shifts to the AKI and leptospirosis pathway: close monitoring of urine output, potassium and creatinine, treatment per the hospital&rsquo;s leptospirosis protocol, avoidance of nephrotoxins, and early discussion with the attending nephrologist about kidney replacement therapy, which many references call renal replacement therapy (RRT), if potassium, acid or urine output worsen. Modules 9 and 10 continue this patient&rsquo;s story.</p>
"""],
    "skills": {"title": "Urinalysis, microscopy and imaging",
               "intro": "Complete with a preceptor on the renal service. Sign-off is local.",
               "items": [
                   ("Collects and labels a midstream or catheter urine sample correctly and reads a dipstick at the right times", False),
                   ("Explains a heme-positive dipstick with few red cells and orders the right follow-up tests", False),
                   ("Centrifuges urine, prepares a slide and identifies casts and cells under the microscope", False),
                   ("Classifies albuminuria by ACR category and explains the limits of dipstick and PCR conversion", False),
                   ("Interprets a kidney ultrasound report for size, echogenicity and hydronephrosis in clinical context", False),
                   ("States the ACR&ndash;NKF position on intravenous contrast in AKI or eGFR below 30 and applies the hospital protocol", False),
               ],
               "placement": "Renal service, ward laboratory or teaching session"},
    "quiz": [
        ("An intern reports a dipstick with blood 3+ and a microscopy count of 0 to 2 red cells per high-power field in a man with severe muscle pain. What should the intern report as the most likely meaning?",
         ["Laboratory error; repeat in a week",
          "Free heme pigment, such as myoglobin or hemoglobin, needing same-day review and a creatine kinase",
          "Glomerulonephritis",
          "Urinary infection"], 1,
         "The blood pad detects heme peroxidase activity, so myoglobin or hemoglobin turns it positive without red cells. Muscle pain makes rhabdomyolysis likely, and pigment can cause AKI, so it needs same-day review."),
        ("A resident sees a patient with a rising creatinine whose sediment shows red cell casts and many acanthocytes. Which syndrome does this point to?",
         ["Acute tubular necrosis",
          "Interstitial nephritis",
          "Glomerulonephritis",
          "Prerenal azotemia"], 2,
         "Red cell casts form inside the nephron and acanthocytes are highly specific for glomerular bleeding (specificity 98% at &ge;5%). Muddy brown casts would point to ATN and white cell casts to interstitial nephritis."),
        ("A fellow is asked whether a patient with an eGFR of 25 mL/min/1.73 m&sup2;, not on dialysis, can have an intravenous contrast CT for a suspected abscess. Which response best reflects the ACR&ndash;NKF consensus statement?",
         ["Contrast is absolutely contraindicated below an eGFR of 30",
          "Proceed if the scan will change management, with intravenous normal saline prophylaxis as indicated for eGFR below 30 and attention to volume and nephrotoxins",
          "Give contrast only after starting dialysis",
          "Use oral contrast only"], 1,
         "The consensus judged the risk overstated and indicated saline prophylaxis for AKI or eGFR below 30 in patients not on dialysis. Withholding a diagnostic scan that will change treatment can do more harm; it is a consensus statement, not a graded recommendation."),
        ("A 55-year-old woman with diabetes has a negative urine dipstick for protein at a rural clinic. Why is this not enough to exclude albuminuria?",
         ["Dipsticks detect only light chains",
          "In a pooled analysis, a dipstick reading of trace or more had only 62% sensitivity for an ACR above 30 mg/g, so many people with moderately increased albuminuria test negative",
          "Diabetes prevents albumin from reaching the urine",
          "Dipstick protein is accurate only in children"], 1,
         "Sumida and colleagues found dipstick sensitivity of 62% for ACR above 30 mg/g. A quantitative ACR, or PCR converted with caution, is needed in people at high risk."),
        ("A 70-year-old man has a creatinine of 5.2 mg/dL with no prior results. Ultrasound shows both kidneys small with thin, echogenic cortex and no hydronephrosis. What does this suggest?",
         ["Acute obstruction needing urgent drainage",
          "Long-standing chronic kidney disease, though an acute change on top must still be considered",
          "Acute glomerulonephritis",
          "Normal kidneys for age"], 1,
         "Small kidneys with a thin bright cortex point to chronic disease and supply evidence of chronicity, but an acute insult can still sit on top. No hydronephrosis makes obstruction unlikely."),
    ],
    "terms": [
        ("ACR", "Albumin-to-creatinine ratio (urine)"),
        ("ACR&ndash;NKF", "American College of Radiology and National Kidney Foundation"),
        ("AKI", "Acute kidney injury"),
        ("ATN", "Acute tubular necrosis"),
        ("CKD", "Chronic kidney disease"),
        ("CT", "Computed tomography"),
        ("eGFR", "Estimated glomerular filtration rate"),
        ("KDIGO", "Kidney Disease: Improving Global Outcomes"),
        ("PCR", "Protein-to-creatinine ratio (urine)"),
        ("SGLT2", "Sodium-glucose cotransporter 2"),
    ],
    "readings": [
        ("hematuria-blood-in-urine.html", "Hematuria: Blood in the Urine"),
        ("proteins-proteinuria.html", "Proteins and Proteinuria"),
        ("contrast-nephropathy.html", "Contrast Nephropathy"),
        ("leptospirosis-nephropathy.html", "Leptospirosis and the Kidney"),
    ],
    "calcs": ["calc-proteinuria-uacr.html", "calc-urine-protein-excretion.html", "calc-uacr-trend.html",
              "calc-ci-aki-mehran.html", "calc-mcmahon-rhabdo.html", "calc-leptospirosis-aki-risk.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
