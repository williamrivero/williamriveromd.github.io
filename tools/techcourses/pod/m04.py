# -*- coding: utf-8 -*-
"""Physician on Duty, Module 04: Life Without Kidney Function III: Heart, Blood, Bone, and Defenses.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty and a nurse reviewing a laboratory printout beside an older Filipino man who is on a cardiac monitor in a dialysis chair. The troponin line on the printout is circled.",
    "objectives": [
        "Describe how kidney failure changes the heart and blood vessels, and explain why heart disease and sudden death dominate mortality on dialysis.",
        "Explain uremic bleeding, renal anemia, and the calcium, phosphate, and parathyroid axis in outline, and identify the findings that need the attending nephrologist.",
        "Explain why immunity is weaker and infection presents atypically, and recognize the risk of sepsis in a dialysis patient.",
        "Interpret troponin, natriuretic peptides, hemoglobin A1c, albumin-corrected calcium, and D-dimer with the cautions that kidney failure imposes.",
        "Explain why drug handling changes in kidney failure, and name where to look before you prescribe.",
    ],
    "big": """
{{plain:Picture an old house where the plumbing, the wiring, and the roof all aged together. A leak in one place loosens a wire somewhere else. Kidney failure does the same to the body. The heart, the blood, the bones, and the defenses against infection wear out together, and each strains the others.}}
<p>The picture has a limit. A house ages passively. In kidney failure, active processes drive the damage: retained salt, water, and phosphate, missing hormones, chronic inflammation, and the treatment itself. Several of them show up on the laboratory sheet you read every shift.</p>
{{fig:pod04_bodymap}}
{{cards:Key terms for this module|Left ventricular hypertrophy (LVH)::Thickening of the wall of the main pumping chamber of the heart.|High-sensitivity cardiac troponin::A test for very small amounts of a heart muscle protein. Troponin T (hs-cTnT) and troponin I (hs-cTnI) assays behave differently.|Natriuretic peptides::Hormones released by stretched heart muscle: B-type natriuretic peptide (BNP) and its fragment, NT-proBNP.|Erythropoietin::The kidney hormone that tells the marrow to make red cells.|Uremic platelet dysfunction::Platelets present in normal numbers that do not stick and clump normally.|CKD-mineral and bone disorder (CKD-MBD)::Linked changes in calcium, phosphate, hormones, bone, and vessels in chronic kidney disease (CKD).|Ionized calcium::The free, active part of blood calcium, measured directly.}}
<p>Most abnormal results on a dialysis patient&rsquo;s sheet are old news. A few are new and dangerous, and some hide behind values that are &ldquo;always high.&rdquo; Your work is to know why each system is different, to read each test against the patient&rsquo;s own baseline, and to report what is new to the attending nephrologist.</p>
""",
    "case": {"title": "The troponin is always high", "html": """
<p>Mang Ponciano Macaraeg, 67, is a retired jeepney driver from Angeles City. He has diabetes and has been on hemodialysis for four years. He arrives for his Monday 6:00 a.m. session, after the long weekend gap.</p>
<p>At 6:20 a.m. he tells the nurse, Ms. Liza Manalo, that he has felt a &ldquo;heaviness&rdquo; in his upper abdomen since last night. He is sweating slightly. On the monitor, his blood pressure is 104/62 mm Hg; his usual pre-dialysis pressure is about 150/80. His pulse is 98 and regular, and his oxygen saturation is 95% on room air. He is 3.4 kilograms above his target weight.</p>
<p>Ms. Manalo has drawn the pre-dialysis blood, including the high-sensitivity troponin that the unit&rsquo;s chest pain protocol asks for. She has not started the blood pump. His chart shows a troponin that has been &ldquo;high&rdquo; at every previous check. A senior staff member says, &ldquo;It is always high. Start him.&rdquo; All values in this case are illustrative, not targets.</p>
""", "questions": ["Why might this patient&rsquo;s troponin be elevated at baseline, and what would make today&rsquo;s value meaningful?",
                  "Which findings today are more important than the troponin number?",
                  "Should dialysis start, and what do you report to the attending nephrologist?"]},
    "sections": [
        ("heart", "The heart", "A thick, stiff heart and hard arteries", """
<p>Picture an old, hardened garden hose on a pump. The pump pushes harder, and its walls thicken and stiffen. The picture has a limit. A pump needs no blood supply, and the heart does; thick muscle needs more oxygen, and its small vessels deliver less.</p>
<h3>What normally happens and what breaks</h3>
<p>A healthy aorta stretches with each beat, and its recoil feeds the coronary arteries while the heart relaxes. In CKD the arteries stiffen and calcify, so systolic pressure rises and coronary filling falls.</p>
<p>Kidney failure then adds several loads at once. Retained salt and water stretch the heart. Anemia and the flow through a fistula or graft raise the output it must deliver. Retained phosphate drives calcium into artery walls and valves. Inflammation and uremic toxins injure the vessel lining and the muscle. These act on top of diabetes, high blood pressure, smoking, and age.[[jankowski2021]]</p>
<p>The result is a recognizable heart. The left ventricle thickens and relaxes poorly, so it needs a full chamber to pump well (diastolic dysfunction). Scar builds between the muscle fibers (fibrosis), and the valves calcify. Fibrosis and stretch disturb the electrical system, which sets the stage for arrhythmia and sudden death.[[jankowski2021]]</p>
{{fig:pod04_uremicheart}}
<div class="table-wrap"><table>
<thead><tr><th>What kidney failure adds</th><th>What it does to the heart</th><th>What you may see in the chair</th></tr></thead>
<tbody>
<tr><td>Salt and water between sessions</td><td>Stretches the chambers</td><td>High pre-dialysis pressure, breathlessness</td></tr>
<tr><td>Stiff, calcified arteries</td><td>Raises systolic load, lowers coronary filling</td><td>Wide pulse pressure. Ischemia when the pressure falls</td></tr>
<tr><td>Anemia and access flow</td><td>Raises the output the heart must deliver</td><td>Fast pulse, flow murmur</td></tr>
<tr><td>Thick, stiff ventricle</td><td>Needs a full chamber to fill</td><td>A sharp fall in pressure with fast fluid removal (Module 13)</td></tr>
<tr><td>Fibrosis and electrolyte swings</td><td>Unstable electrical system</td><td>Arrhythmia around the long gap (Module 15)</td></tr>
</tbody></table></div>
<h3>The evidence: how large the risk is</h3>
<p>Go and colleagues followed 1,120,295 adults not on dialysis. Risk rose as the estimated glomerular filtration rate (eGFR) fell. Below 15 mL per minute per 1.73 m&sup2;, the adjusted hazard ratio was 5.9 for death and 3.4 for cardiovascular events, compared with 60 or more.[[go2004]] The study was observational, so illnesses that travel with kidney disease may explain part of the excess. Dialysis patients sit beyond its lowest group. About half of all deaths in kidney failure are attributed to cardiovascular disease.[[kato2008]]</p>
{{fig:ckd_cascade|When nephrons are lost, several kidney jobs fail together. The heart, the blood, and the bones carry the consequences at the same time.}}
<h3>Why statins teach a lesson about this heart</h3>
<p>Statins lower low-density lipoprotein (LDL) cholesterol and reduce events in the general population. Three randomized trials tested them in kidney failure.</p>
<div class="table-wrap"><table>
<thead><tr><th>Trial</th><th>Who was studied</th><th>Main outcome</th></tr></thead>
<tbody>
<tr><td>4D (atorvastatin)</td><td>1,255 people with type 2 diabetes on hemodialysis</td><td>LDL fell 42%. Relative risk 0.92 (95% confidence interval 0.77 to 1.10), not significant[[wanner2005]]</td></tr>
<tr><td>AURORA (rosuvastatin)</td><td>2,776 people on hemodialysis</td><td>LDL fell 43%. 9.2 vs. 9.5 events per 100 patient-years, hazard ratio 0.96 (0.84 to 1.11), not significant[[fellstrom2009]]</td></tr>
<tr><td>SHARP (simvastatin plus ezetimibe)</td><td>9,270 people with CKD, 3,023 of them on dialysis</td><td>Major atherosclerotic events 11.3% vs. 13.4% over a median 4.9 years, rate ratio 0.83 (0.74 to 0.94)[[baigent2011]]</td></tr>
</tbody></table></div>
<p>In SHARP, the absolute difference of 2.1 percentage points means treating about 48 people for five years to prevent one event, and the result is for a population mostly not on dialysis.[[baigent2011]] The KDIGO (Kidney Disease: Improving Global Outcomes) lipid guideline suggests not starting a statin or statin and ezetimibe in adults on dialysis (2A), and suggests continuing them in adults already taking them when dialysis begins (2C).[[kdigo_lipid2014]]</p>
<p>LDL cholesterol is a surrogate outcome. The drugs moved it by more than 40%, yet events did not fall in the hemodialysis trials. A likely explanation is that much of this heart disease is thick muscle, scar, stiff vessels, and unstable rhythm, which cholesterol lowering does not reach.</p>
<h3>What you do on your shift</h3>
<p>Expect ischemia to present as breathlessness, abdominal discomfort, sweating, or a falling pressure, and arrhythmia around the long gap (Module 15). Do not start or stop a cardiovascular drug at the chair; report.</p>
{{key:This heart is thick, stiff, and easily stunned. Fast fluid shifts and sudden potassium shifts are its enemies.}}
"""),
        ("cardiactests", "Troponin and peptides", "Troponin and natriuretic peptides: reading the trend, not the number", """
<p>Picture a smoke detector in a house where someone always cooks. It reads a little smoke every day, so one reading tells you little. A reading that climbs over an hour tells you a fire has started. The picture has a limit. In kidney failure the everyday &ldquo;smoke&rdquo; is itself a warning: a chronically raised troponin marks a damaged heart and a higher risk of death.</p>
<h3>Why troponin is raised at baseline</h3>
<p>Injured heart muscle cells release troponin. In a dialysis patient, the thick ventricle, scarred muscle, diseased small vessels, and repeated stress of fluid removal cause a slow, steady leak. Reduced clearance may contribute for some assays, but the elevation mainly reflects underlying heart disease.[[defilippi2017]]</p>
<p>The assay matters. In 103 stable, symptom-free hemodialysis patients, hs-cTnT was above the general-population 99th percentile in 99%, and a troponin I assay in 13%. The median hs-cTnT was unchanged over two weeks (69 vs. 69 ng/L) and fell slightly after a session (69 to 61 ng/L).[[pianta2012]] With a high-sensitivity troponin I assay, 93% of 215 hemodialysis patients were below the 99th percentile, yet higher values still predicted death.[[artunc2019]] Know which assay your laboratory uses.</p>
{{fig:pod04_troponintrend}}
<h3>What the diagnosis of infarction requires</h3>
<p>The Fourth Universal Definition of Myocardial Infarction requires a rise or fall of troponin, with at least one value above the 99th percentile, plus clinical evidence of ischemia, such as symptoms or new electrocardiogram (ECG) changes. A high but stable troponin is chronic myocardial injury.[[thygesen2018]] This is a consensus definition, not a graded recommendation, and it applies to dialysis patients too.</p>
<h3>The evidence on serial testing</h3>
<p>In two cohorts with suspected infarction (1,494 and 7,059 patients), the specificity of a single hs-cTnT with an eGFR below 60 fell to 0.26, compared with 0.73 without CKD. A second measurement at three hours restored performance.[[kraus2018]] In 501 emergency patients with CKD, a baseline hs-cTnT of 52 ng/L or more had a positive predictive value for infarction of only 36%. A rise of more than 20 ng/L over two hours had a positive predictive value of 86%.[[knott2024]] These were CKD cohorts, not dialysis-only cohorts, and the thresholds belong to one assay.</p>
<p>Among 46,927 patients with suspected acute coronary syndrome, hs-cTnI was above the 99th percentile in 46% of those with kidney impairment. With a type 1 infarction, they were less often revascularized (26% vs. 53%). Among patients with a troponin above the 99th percentile, infarction or cardiovascular death at one year was twice as frequent with kidney impairment (24% vs. 12%).[[gallacher2022]] The analysis is observational and shows a gap, not its cause.</p>
<h3>Natriuretic peptides</h3>
<p>BNP and NT-proBNP are excreted by the kidney and almost always raised in kidney failure. They relate to heart structure and mortality, but cut-offs for heart failure or overload are inconsistent.[[yang2020]] A value well above the patient&rsquo;s own usual level, with a picture that fits, is worth reporting.</p>
{{flow:Reading a troponin in a dialysis patient|Start with the patient::Symptoms, pressure against the usual value, pulse, and breathing.|Get an ECG now::Compare it with the last tracing. A new change outranks any troponin value.|Find the baseline::The last stable troponin, the assay, and its timing relative to dialysis.|Repeat per protocol::At the interval your unit&rsquo;s chest pain protocol sets.|Read the change::A rise or fall with ischemia suggests acute infarction. A stable high value suggests chronic injury.|Call::Report the picture, the ECG, and both values. Module 15 has the full pathway.}}
{{formula:<strong>Worked scenario 1. Troponin change (illustrative values only).</strong><br>Last stable pre-dialysis hs-cTnT: 70 ng/L. Today at 0 hours: 88 ng/L. At 2 hours: 116 ng/L.<br>Change from today&rsquo;s first value = 116 &minus; 88 = <strong>28 ng/L</strong> over 2 hours. Change from baseline = 116 &minus; 70 = 46 ng/L.<br><strong>What it tells you:</strong> the level is rising, the pattern the Universal Definition requires.[[thygesen2018]] In one CKD cohort, a 2-hour rise above 20 ng/L had a positive predictive value of 86%.[[knott2024]]<br><strong>What it does not tell you:</strong> it does not diagnose infarction without clinical evidence of ischemia, and the threshold was not derived in dialysis patients or for every assay. Your laboratory and protocol govern.}}
<h3>What you do on your shift</h3>
<p>Never dismiss chest pain or an anginal equivalent because &ldquo;the troponin is always high,&rdquo; and never diagnose infarction from one value. Draw cardiac markers per protocol, before the session when possible, because dialysis lowers some values.</p>
{{call:Stop and call the attending nephrologist at once for chest pain or an anginal equivalent (breathlessness, epigastric heaviness, sweating, unexplained low pressure) with a new ECG change, a rising troponin, or an unstable patient. Start your unit&rsquo;s chest pain protocol while you call. Call also for a new murmur or a pericardial rub.}}
{{key:Read a troponin as a trend against the patient&rsquo;s own baseline, beside the ECG and the symptoms. One number never rules infarction in or out.}}
"""),
        ("blood", "Blood", "Blood: anemia and the platelet that cannot stick", """
<p>Picture a factory that has lost its foreman (the marrow without erythropoietin), and a road crew whose glue no longer sets (the platelets). The picture has a limit. The marrow is not broken and the platelets are not absent. Both work in a body whose signals and chemistry have changed.</p>
<h3>Renal anemia</h3>
<p>In health, the kidney senses falling oxygen delivery and releases erythropoietin, which tells the marrow to make red cells. Iron from stores builds their hemoglobin. In kidney failure, several links fail together. The kidney makes too little erythropoietin. Iron is lost in the circuit, at the needle sites, and in blood tests. Inflammation raises hepcidin, a liver hormone that locks iron in storage cells so it cannot reach the marrow. Red cells also survive a shorter time.</p>
{{fig:pod04_epoiron}}
<p>The KDIGO 2026 anemia guideline states that anemia should be evaluated with a complete blood count, reticulocytes, ferritin, and transferrin saturation (TSAT). It notes that alloimmunization after red cell transfusion may reduce future suitability for a kidney transplant.[[kdigo_anemia2026]] Module 21 covers treatment with iron and erythropoiesis-stimulating agents (ESAs).</p>
<h3>Uremic bleeding</h3>
<p>When a vessel is cut, platelets stick to the wall through a bridging protein, von Willebrand factor, then release their contents and clump. In uremia, retained toxins impair adhesion and aggregation, the interaction with von Willebrand factor is altered, and excess nitric oxide blunts platelet activation. Anemia adds to it: red cells normally push platelets toward the vessel wall, so fewer red cells means fewer platelets at the injury.[[hedges2007]]</p>
{{fig:pod04_platelet}}
<p>The platelet count is usually normal. A review lists dialysis itself, erythropoietin, cryoprecipitate, desmopressin, and conjugated estrogens as options, with different onsets and durations, supported mostly by small trials.[[hedges2007]] The choice and every dose belong to the attending nephrologist and the protocol.</p>
<div class="table-wrap"><table>
<thead><tr><th>Mechanism</th><th>What it causes</th><th>What you may see</th></tr></thead>
<tbody>
<tr><td>Too little erythropoietin</td><td>Too few red cells made</td><td>Slowly falling hemoglobin, fatigue</td></tr>
<tr><td>Iron loss and the hepcidin lock</td><td>Red cells cannot be built</td><td>Low TSAT. Ferritin low with iron loss, normal or high with the hepcidin lock</td></tr>
<tr><td>Uremic platelet dysfunction</td><td>Weak plugs at cut vessels</td><td>Oozing needle sites, easy bruising</td></tr>
<tr><td>Heparin during the session</td><td>Added anticoagulation</td><td>Prolonged bleeding after needle removal (Module 19)</td></tr>
</tbody></table></div>
<h3>What you do on your shift</h3>
<p>An unexplained drop in hemoglobin is a search for bleeding: needle sites, stools, vomit, menstrual loss, and the circuit records. Before transfusing a patient who may be considered for a transplant, ask the attending nephrologist first, unless bleeding threatens life; then follow the protocol.</p>
{{call:Stop and call the attending nephrologist for an unexplained fall in hemoglobin, black stools or vomiting of blood, or bleeding that does not stop after the usual measures in your unit&rsquo;s protocol.}}
{{key:A falling hemoglobin means &ldquo;find the blood loss&rdquo; before it means &ldquo;give more erythropoietin.&rdquo;}}
"""),
        ("bone", "Bone and minerals", "Bone and minerals: calcium, phosphate, and the parathyroid", """
<p>Picture a seesaw with calcium on one end and phosphate on the other, and a supervisor who pushes down whenever it tilts. The supervisor is parathyroid hormone (PTH). In kidney failure the seesaw tilts more each year, and the supervisor works harder each year. The picture has a limit. The real system has at least five players, and bone and blood vessels are part of the board.</p>
<h3>What normally happens and what breaks</h3>
<p>Healthy kidneys excrete dietary phosphate and make calcitriol, the active vitamin D that helps the gut absorb calcium. As kidney function falls, phosphate is retained, and bone releases fibroblast growth factor 23 (FGF23) to push it out. FGF23 also suppresses calcitriol, so less calcium is absorbed. Low calcium, high phosphate, and low calcitriol all drive the parathyroid glands to grow and release more PTH, which pulls calcium and phosphate out of bone. Over years, bone weakens and calcium phosphate settles in arteries and valves.</p>
<p>KDIGO defines the whole picture as CKD-MBD: abnormal laboratory values, abnormal bone, and vascular or soft-tissue calcification together.[[kdigo_mbd2017]] The calcified arteries of the first section are partly a mineral problem. Module 21 teaches management.</p>
{{fig:pod04_mineral}}
<h3>The test-reading rule: corrected calcium</h3>
<p>About half of blood calcium is bound, mostly to albumin. The other half is free, or ionized, and only this fraction is active.[[hall2021]] When albumin is low, total calcium falls while ionized calcium may be normal. Payne and colleagues derived a correction in 1973 from 200 specimens sent for liver tests: adjusted calcium = calcium &minus; albumin + 4.0 (mg/dL and g/dL).[[payne1973]] Many references use a version with a factor of 0.8.</p>
<p>The formula was not derived in dialysis patients. In 50 stable hemodialysis patients, no correction formula improved agreement with measured ionized calcium beyond the uncorrected total, and the Payne formula did worse. Although 92% took calcium supplements, 22% had a low ionized calcium.[[clase2000]] pH matters too: acidosis raises the ionized fraction and alkalosis lowers it.</p>
{{formula:<strong>Worked scenario 3. Corrected calcium, and why not to trust it (illustrative values only).</strong><br>Payne formula: adjusted calcium = measured calcium &minus; albumin + 4.0.[[payne1973]]<br>Calcium 8.4 mg/dL, albumin 3.0 g/dL: 8.4 &minus; 3.0 + 4.0 = <strong>9.4 mg/dL</strong>.<br><strong>What it tells you:</strong> the formula moves a low-looking value into the normal range.<br><strong>What it does not tell you:</strong> on hemodialysis, correction did not bring the value closer to ionized calcium.[[clase2000]] When it matters (symptoms, a QT change, before any calcium is given), ask for an ionized calcium per protocol. The site&rsquo;s corrected calcium calculator carries the same caution.}}
<h3>What you do on your shift</h3>
<p>Read calcium with the albumin and the acid-base state in mind, and do not act on a corrected value alone. A high phosphate unchanged for months belongs to the monthly review. A new, very high or very low calcium is a call. So is calciphylaxis: calcification and clotting of small skin vessels that causes very painful, firm, dark skin patches, often on the thighs or abdomen. It is rare and often fatal, so early recognition matters.[[daugirdas2015]]</p>
{{call:Stop and call the attending nephrologist for a very high or very low calcium, tingling or muscle spasm, a new QT prolongation, or a painful skin lesion that suggests calciphylaxis.}}
{{key:Trust a measured ionized calcium over any corrected calcium. A formula is not a measurement.}}
"""),
        ("defenses", "Defenses", "Defenses: weaker immunity and silent infection", """
<p>Picture guards who are tired and jumpy: slow to meet a real intruder, yet always on edge. The picture has a limit. Guards change shifts; this immune system stays this way for years, and the gate, the skin over the access, opens three times a week.</p>
<h3>What normally happens and what breaks</h3>
<p>In health, neutrophils and monocytes kill bacteria, and lymphocytes make antibodies and remember infections. Fever and a rising white cell count are the visible signs. Uremia disturbs both arms. Kato and colleagues describe immunodepression, with weaker killing by white cells and poor lymphocyte responses that blunt vaccines. They also describe immunoactivation, a persistent low-grade inflammation that may feed vascular disease.[[kato2008]] Diabetes, malnutrition, age, catheters, and needles add to the risk.</p>
{{fig:pod04_immune}}
<h3>The evidence</h3>
<p>About 20% of deaths in kidney failure are attributed to infection.[[kato2008]] Using United States registry data from the mid-1990s, Sarnak and Jaber found the annual death rate from sepsis about 100 to 300 times higher in dialysis patients than in the general population. The gap narrowed but persisted after stratifying by age, and sepsis mortality was still about 50 times higher when every cause listed on the death record was counted.[[sarnak2000]] The data are old and current Philippine figures are unknown, but the direction is not in doubt.</p>
<div class="table-wrap"><table>
<thead><tr><th>What uremia changes</th><th>Why it matters</th><th>What you may see</th></tr></thead>
<tbody>
<tr><td>Weaker killing by white cells</td><td>Bacteria spread before the body responds</td><td>Infection advanced when first noticed</td></tr>
<tr><td>Blunted fever</td><td>The usual alarm is quiet</td><td>Low-grade, normal, or low temperature with sepsis</td></tr>
<tr><td>Poor antibody response</td><td>Vaccines protect less</td><td>Antibody levels that need checking (Module 29)</td></tr>
<tr><td>Skin breached every session</td><td>A direct route into the blood</td><td>Exit-site redness or pus. Rigors soon after connection</td></tr>
</tbody></table></div>
<h3>What you do on your shift</h3>
<p>Fever may be absent. A low temperature, new confusion, or an unexplained fall in pressure can be the first sign of sepsis. Rigors soon after a catheter is connected suggest a catheter bloodstream infection. Look at the access first, then the chest, urine, feet, and any wound. Module 17 has the fever pathway.</p>
{{call:Stop and call the attending nephrologist for fever or rigors in a patient with a catheter, unexplained low blood pressure, or a low temperature or new confusion with any sign of infection. Follow your unit&rsquo;s fever protocol while you call.}}
{{key:Sepsis can arrive without fever. Look at the access first, and treat unexplained low pressure or new confusion as possible infection.}}
"""),
        ("labs", "Tests that mislead", "Tests that read differently", """
<p>Picture a map drawn for another country. The roads look familiar, but the distances are wrong. Most reference ranges were drawn from people with working kidneys. The picture has a limit. A wrong map is useless; a test in a dialysis patient is still useful once you know which way it is distorted.</p>
<p>Two rules apply to almost every test. Note when the sample was drawn: before or after dialysis, after the long or short gap. Compare it with the patient&rsquo;s own recent values.</p>
<div class="table-wrap"><table>
<thead><tr><th>Test</th><th>How kidney failure distorts it</th><th>How to read it</th></tr></thead>
<tbody>
<tr><td>Creatinine and eGFR</td><td>eGFR equations assume steady state and working kidneys. On dialysis, creatinine reflects muscle mass and session timing</td><td>Do not use an eGFR on dialysis. A falling creatinine over months may mean lost muscle (Module 23)</td></tr>
<tr><td>Hemoglobin A1c (HbA1c)</td><td>Shorter red cell survival and ESAs lower it for the same glucose[[peacock2008]]</td><td>Compare with glucose readings. KDIGO notes low reliability on dialysis[[kdigo_dm2022]]</td></tr>
<tr><td>High-sensitivity troponin</td><td>Raised at baseline with some assays; slightly lower after a session[[pianta2012]]</td><td>Read the change and the ECG</td></tr>
<tr><td>BNP and NT-proBNP</td><td>Almost always raised; cut-offs inconsistent[[yang2020]]</td><td>Compare with the patient&rsquo;s usual level</td></tr>
<tr><td>Total and corrected calcium</td><td>Correction does not track ionized calcium[[clase2000]]</td><td>Ask for ionized calcium when it matters</td></tr>
<tr><td>D-dimer</td><td>Stays sensitive, but nearly everyone with an eGFR below 60 has a raised value. Few study patients had severe kidney failure[[lindner2014]]</td><td>A normal value still argues against a clot, though dialysis patients were not studied separately. A raised one means little</td></tr>
<tr><td>Potassium</td><td>Highest before the first session of the week; falls during the session</td><td>Always note the timing (Modules 2 and 18)</td></tr>
<tr><td>Blood urea nitrogen (BUN)</td><td>Falls with dialysis and with poor protein intake</td><td>A low pre-dialysis BUN can mean poor eating (Module 7)</td></tr>
</tbody></table></div>
<h3>Hemoglobin A1c: the evidence</h3>
<p>In 307 people with diabetes, 258 on hemodialysis, HbA1c tended to be lower on dialysis despite higher glucose, and it was lower in patients on higher erythropoietin doses. Glycated albumin reflected glycemia better.[[peacock2008]] The study was cross-sectional and did not test outcomes.</p>
<p>The KDIGO 2022 diabetes guideline still recommends HbA1c to monitor glycemic control in diabetes and CKD (1C). Its ungraded Practice Point 2.1.2 adds that HbA1c accuracy declines in CKD G4 to G5, particularly on dialysis, where reliability is low. Practice Point 2.1.3 offers a glucose management indicator from continuous glucose monitoring when HbA1c and measured glucose disagree.[[kdigo_dm2022]] HbA1c remains the standard test, read with its bias in mind.</p>
{{formula:<strong>Worked scenario 2. HbA1c and estimated average glucose (illustrative values only).</strong><br>A1c-Derived Average Glucose (ADAG) formula: estimated average glucose (mg/dL) = 28.7 &times; HbA1c (%) &minus; 46.7.[[nathan2008]]<br>HbA1c 6.2%: 28.7 &times; 6.2 &minus; 46.7 = 177.9 &minus; 46.7 = <strong>131 mg/dL</strong>. The home glucose log averages about 190 mg/dL.<br><strong>What it tells you:</strong> HbA1c suggests far better control than the log, the direction of error expected on hemodialysis.[[peacock2008]]<br><strong>What it does not tell you:</strong> the formula came from 507 people with and without diabetes, not from dialysis patients, so it cannot be corrected for this patient. Report the mismatch; do not change glucose treatment at the chair (Module 22). The site&rsquo;s HbA1c calculator shows the same conversion.}}
<h3>Worked scenario 4: a monthly sheet with the nurse</h3>
<p>Ms. Manalo hands you the monthly results of a patient who is well today. You sort them.</p>
<div class="table-wrap"><table>
<thead><tr><th>Result (illustrative)</th><th>Group</th><th>Action</th></tr></thead>
<tbody>
<tr><td>Phosphate high, unchanged for three months</td><td>Expected for this patient</td><td>Document as stable</td></tr>
<tr><td>Troponin &ldquo;high&rdquo; from last week&rsquo;s chest pain check, at the usual level, no symptoms</td><td>Expected for this patient</td><td>Record the assay and value as a baseline</td></tr>
<tr><td>Hemoglobin 9.1 g/dL, last month 10.4 g/dL</td><td>New; report today</td><td>Look for bleeding. Tell the attending nephrologist</td></tr>
<tr><td>Albumin 3.3 g/dL</td><td>Note it</td><td>Read the calcium with it in mind</td></tr>
<tr><td>Potassium 5.9 mmol/L before the session</td><td>Act per protocol now</td><td>Follow the potassium protocol and call if it directs (Module 18)</td></tr>
</tbody></table></div>
{{formula:<strong>Arithmetic for the sheet (illustrative).</strong> Change in hemoglobin = 10.4 &minus; 9.1 = <strong>1.3 g/dL</strong> in one month, more than a tenth of the previous value.<br><strong>What it tells you:</strong> with no known change in treatment, this is new and is reported today.<br><strong>What it does not tell you:</strong> the cause. Bleeding comes first; a missed ESA dose, iron deficiency, infection, and hemolysis follow.}}
{{key:Read every result against this patient&rsquo;s own baseline and against the clock of the dialysis week.}}
"""),
        ("drugs", "Drugs", "Drugs: what the missing kidney and the dialyzer change", """
<p>Picture a building with several exits. In kidney failure, one of the widest, the kidney, is closed. A revolving door appears, the dialyzer, but it turns only during the session and lets through only small, free molecules. The picture has a limit. Closing the kidney exit also slows some of the other exits.</p>
<h3>What normally happens and what breaks</h3>
<p>When the kidney route closes, a drug that depends on it accumulates with repeated doses, and so do active or toxic products of some liver-handled drugs. A KDIGO conference report adds that kidney disease also reduces non-renal clearance, through liver enzymes and drug transporters.[[matzke2011]] Uremia and low albumin change protein binding, so the free, active fraction can rise while the total level looks normal.</p>
{{fig:pod04_drugjourney}}
<p>A drug crosses the dialyzer membrane only when it is free in the plasma and small enough for the membrane&rsquo;s pores. A drug spread widely in the tissues has little in the blood to remove. High-flux membranes and longer sessions remove more.[[matzke2011]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Drug property</th><th>Removal by dialysis</th><th>Practical question</th></tr></thead>
<tbody>
<tr><td>Small, free in plasma</td><td>Removed more readily</td><td>Should the dose follow the session?</td></tr>
<tr><td>Highly protein bound</td><td>Little removed</td><td>Is the free level higher than the total suggests?</td></tr>
<tr><td>Large volume of distribution</td><td>Little removed</td><td>Will toxicity persist after dialysis?</td></tr>
<tr><td>Cleared mainly by the kidney</td><td>Accumulates between sessions</td><td>Does the dose or interval need to change?</td></tr>
</tbody></table></div>
<h3>What the guidelines say</h3>
<p>The KDIGO 2024 CKD guideline gives ungraded practice points. People with CKD may be more susceptible to nephrotoxic medicines, so weigh benefit against harm (4.1.1). Review and limit over-the-counter medicines and herbal remedies that may be harmful (4.1.3). Consider GFR when dosing drugs cleared by the kidneys (4.2.1). Tell patients the benefits and risks of their medicines so they can report adverse events, and work with pharmacists and tools that support safe prescribing (4.3.1.1 and 4.3.1.2).[[kdigo_ckd2024]]</p>
{{cards:Before you prescribe at the chair|Check the reference::Use a renal dosing reference and the unit&rsquo;s formulary, with the dialysis entry, not an eGFR band. The site&rsquo;s renal medication safety tool is a starting point.|Ask about timing::Ask whether the dose should follow the session.|Count what is already there::Over-the-counter painkillers, herbal remedies, and medicines from other doctors add to the load.|Ask the nephrologist::Chronic medicines belong to the attending nephrologist. Module 20 teaches prescribing.}}
{{key:Every new drug gets three questions: is it cleared by the kidney, is it removed by the dialyzer, and when should it be given relative to the session.}}
"""),
    ],
    "debrief": ["""
<p><strong>Why might his troponin be high at baseline, and what would make today&rsquo;s value meaningful?</strong> Four years of dialysis and diabetes have almost certainly left Mang Ponciano with a thick, scarred ventricle and diseased small vessels, which leak troponin steadily. With an hs-cTnT assay, nearly every stable hemodialysis patient is above the 99th percentile.[[pianta2012]] Today&rsquo;s value becomes meaningful when it is compared with his last stable value, same assay and same point in the dialysis week, and when a repeat shows whether it is rising. A rise with ischemia meets the definition of acute infarction.[[thygesen2018]]</p>
<p><strong>Which findings matter more?</strong> Epigastric heaviness with sweating in a man with diabetes is an anginal equivalent until proven otherwise. His pressure is more than 40 mm Hg below his usual value while he carries 3.4 kilograms of extra fluid: a low pressure in an overloaded patient points to a failing pump, and bleeding and sepsis must also be considered. A pulse of 98 fits any of these. The ECG, compared with his last tracing, comes before any troponin result.</p>
<p><strong>Should dialysis start?</strong> Not on &ldquo;it is always high.&rdquo; Fluid removal could lower his pressure further and deepen the ischemia. You ask for an ECG now, follow the chest pain protocol, and call the attending nephrologist before the blood pump starts. Using the situation, background, assessment, recommendation (SBAR) format from Module 1, you report the symptom and its onset, his pressure against his usual value, pulse, saturation, weight gain, the ECG, his baseline and today&rsquo;s troponin with the assay, and when the repeat is due. His ECG shows new ST depression in the lateral leads, and the nephrologist arranges transfer to the emergency department (Module 15).</p>
"""],
    "skills": {"title": "Reading a routine laboratory sheet with the nurse",
               "intro": "Read a real or simulated monthly laboratory sheet with a dialysis nurse while your preceptor observes. Talk through each step aloud.",
               "items": [
                   ("Confirms the patient&rsquo;s identity and the date and time of each sample.", True),
                   ("Notes whether each sample was drawn before or after dialysis, and after the long or the short gap.", True),
                   ("Compares each value with the patient&rsquo;s own last three values, not only with the laboratory range.", False),
                   ("Identifies results that need action now under the unit&rsquo;s protocol, such as potassium, and acts or calls.", True),
                   ("Identifies new changes to report today, such as a fall in hemoglobin or a new high calcium.", False),
                   ("Identifies expected chronic abnormalities and documents them as stable.", False),
                   ("For troponin or a natriuretic peptide, records the assay and the patient&rsquo;s baseline if known.", False),
                   ("For HbA1c, states the caution on dialysis and compares it with glucose readings.", False),
                   ("For calcium, reads it with the albumin and the acid-base state, and requests an ionized calcium per protocol when it matters.", False),
                   ("States which drugs on the patient&rsquo;s list are cleared by the kidney, without changing any of them.", False),
                   ("Writes a brief summary in the record and tells the attending nephrologist what is new.", True),
               ],
               "placement": "For two weeks, read the monthly laboratory sheets of five patients with the charge nurse. For each, write one line on what is expected for that patient, what is new, and what needed action. Review the lines with your preceptor and the attending nephrologist."},
    "quiz": [
        ("Why does the left ventricle thicken in kidney failure?",
         ["Dialysis fluid irritates the heart muscle",
          "Stiff arteries, retained fluid, anemia, and access flow raise its workload",
          "Low cholesterol weakens the heart wall",
          "Retained urea makes the muscle swell"], 1,
         "Each load raises wall stress, and the ventricle thickens in response."),
        ("4D and AURORA lowered LDL cholesterol by more than 40% in hemodialysis patients. What happened to the main cardiovascular outcome?",
         ["It fell by about 40%",
          "It rose significantly",
          "It did not fall significantly",
          "It fell only without diabetes"], 2,
         "The surrogate moved, but events did not. This heart disease is not only atherosclerosis."),
        ("A man who has taken a statin for years starts hemodialysis. What does the KDIGO lipid guideline suggest?",
         ["Continue the statin (2C)",
          "Stop the statin at the first session",
          "Double the statin dose",
          "Switch to ezetimibe alone"], 0,
         "KDIGO suggests not starting statins on dialysis (2A) but continuing them (2C). The nephrologist decides."),
        ("In stable hemodialysis patients tested with an hs-cTnT assay, how many were above the general-population 99th percentile?",
         ["About 13%",
          "About 50%",
          "About 7%",
          "About 99%"], 3,
         "Nearly all were, so one value means little. A troponin I assay was raised in 13%."),
        ("A woman on dialysis has epigastric discomfort. Her troponin is 85 ng/L; her last stable value, same assay, was 80. A repeat two hours later is 84 and her ECG is unchanged. What does this suggest?",
         ["Chronic injury without a rise; keep assessing and report",
          "Acute myocardial infarction",
          "Laboratory error",
          "Troponin is useless on dialysis"], 0,
         "Acute infarction needs a rise or fall with ischemia. Her symptom still needs a report."),
        ("Why are cardiac markers drawn before the session when possible?",
         ["Heparin destroys troponin",
          "Dialysis lowers some values, so a post-dialysis sample is not comparable",
          "The machine adds troponin to the blood",
          "Troponin can only be drawn from a fistula"], 1,
         "In one study, hs-cTnT fell from 69 to 61 ng/L after a session."),
        ("Why are BNP and NT-proBNP hard to interpret on dialysis?",
         ["Heparin destroys them",
          "They are never raised on dialysis",
          "They measure kidney function",
          "They are nearly always raised, and cut-offs are inconsistent"], 3,
         "Compare with the patient&rsquo;s usual level and the clinical picture."),
        ("A man&rsquo;s hemoglobin fell from 10.8 to 9.2 g/dL in a month. He feels well. What comes first?",
         ["A search for blood loss",
          "A request to double his erythropoietin",
          "A transfusion",
          "Nothing, because anemia is expected"], 0,
         "Anemia is expected; a new fall is not. Look for bleeding and report."),
        ("Why do dialysis patients bleed easily with a normal platelet count?",
         ["The dialyzer destroys platelets",
          "Uremia impairs platelet adhesion and aggregation, and anemia keeps platelets from the vessel wall",
          "Erythropoietin thins the blood",
          "Phosphate binds clotting factors"], 1,
         "The defect is in function, not number. Heparin adds to it."),
        ("A patient&rsquo;s calcium is 8.0 mg/dL with an albumin of 2.8 g/dL, so the corrected calcium is 9.2. She has tingling around her mouth. What should you do?",
         ["Reassure her; the corrected value is normal",
          "Give calcium without testing",
          "Request an ionized calcium per protocol, check the ECG, and call",
          "Repeat the albumin only"], 2,
         "Correction does not track ionized calcium on dialysis, and she has symptoms."),
        ("A woman with a tunneled catheter is quiet and slightly confused. Her temperature is 36.2 &deg;C and her pressure is lower than usual. What is the best interpretation?",
         ["Normal variation; start the session",
          "Low potassium",
          "Possible sepsis despite a normal temperature",
          "Too much dialysis last session"], 2,
         "Uremia blunts fever. Examine the catheter site and call."),
        ("A man with diabetes on dialysis has an HbA1c of 6.0%, but his home glucose is mostly above 200 mg/dL. What best explains this?",
         ["His meter is faulty",
          "Dialysis removes HbA1c",
          "He is hiding high readings",
          "Shorter red cell survival and ESA treatment lower HbA1c"], 3,
         "HbA1c underestimates glycemia on hemodialysis. Report it; do not change treatment at the chair."),
        ("A dialysis patient has a raised D-dimer. What does it tell you?",
         ["Pulmonary embolism is confirmed",
          "Little, because nearly everyone with reduced kidney function has a raised value",
          "The patient has sepsis",
          "Anticoagulation should start now"], 1,
         "D-dimer keeps its sensitivity but loses specificity. A normal value still helps."),
        ("Which drug is least likely to be removed by dialysis?",
         ["A small molecule free in the plasma",
          "A small, water-soluble drug cleared by the kidney",
          "A drug with a small volume of distribution",
          "A highly protein-bound drug with a large volume of distribution"], 3,
         "Only free drug in the plasma reaches the membrane."),
        ("A nurse asks you to prescribe an antibiotic for a dialysis patient&rsquo;s skin infection. What comes first?",
         ["Use the usual adult dose",
          "Check a renal dosing reference using the dialysis entry, ask about timing, and inform the nephrologist",
          "Halve the dose",
          "Wait for the eGFR"], 1,
         "Dosing depends on renal clearance and dialytic removal. eGFR is not valid on dialysis."),
    ],
    "terms": [("Left ventricular hypertrophy", "Thickening of the wall of the main pumping chamber of the heart."),
              ("Chronic myocardial injury", "A troponin above the 99th percentile that is stable over time, without the rise or fall of acute injury."),
              ("Surrogate outcome", "A laboratory or physiologic measure, such as LDL cholesterol, used in place of an outcome patients feel."),
              ("Hepcidin", "A liver hormone that locks iron inside storage cells. Inflammation raises it."),
              ("Uremic platelet dysfunction", "Platelets that are normal in number but stick and clump poorly in uremia."),
              ("CKD-mineral and bone disorder", "The linked abnormalities of calcium, phosphate, hormones, bone, and vascular calcification in chronic kidney disease."),
              ("Ionized calcium", "The free, active fraction of blood calcium, measured directly."),
              ("Calciphylaxis", "Calcification and clotting of small skin vessels that causes very painful skin lesions, mainly in dialysis patients."),
              ("Glycated albumin", "A marker of average glucose over the previous few weeks that does not depend on red cell survival."),
              ("Volume of distribution", "How widely a drug spreads through the body&rsquo;s tissues compared with the blood.")],
    "readings": [("heart-kidney-connection.html", "How kidney disease and heart disease drive each other."),
                 ("understanding-lab-results.html", "A plain-language guide to the laboratory values on a dialysis sheet."),
                 ("cardiovascular-death-dialysis.html", "Why heart disease and sudden death dominate mortality on dialysis.")],
    "calcs": ["calc-corrected-calcium.html", "calc-eag-hba1c.html", "calc-renal-med-safety.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
