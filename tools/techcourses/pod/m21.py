# -*- coding: utf-8 -*-
"""Physician on Duty, Module 21: Blood and Bone: Anemia and Mineral Disorders.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty at the nurses&rsquo; station reviewing a monthly laboratory sheet with a dialysis nurse, while a patient rests in a dialysis chair in the background.",
    "objectives": [
        "Explain renal anemia as the sum of low erythropoietin, iron deficiency, iron blocked by inflammation, blood loss, and shortened red cell survival.",
        "Read hemoglobin, ferritin, and transferrin saturation together and tell absolute from functional iron deficiency.",
        "Describe what iron, erythropoiesis-stimulating agents, and the newer oral agents do, what the major trials showed, and why higher hemoglobin targets caused harm.",
        "Recognize a poor response to an erythropoiesis-stimulating agent, list its causes, and know when a transfusion question goes to the attending nephrologist, including why transfusion matters for a future transplant.",
        "Explain the calcium, phosphate, and parathyroid hormone axis, how phosphate is controlled, and read a mineral panel against the 2017 Kidney Disease: Improving Global Outcomes (KDIGO) suggestions.",
        "Recognize severe hyperparathyroidism, abnormal calcium, and calciphylaxis, and know which findings go to the attending nephrologist and how fast.",
    ],
    "big": """
{{plain:Picture a factory that makes red cells. It needs two things: an order form that tells it how many to make, and raw material to build them with. The bone marrow is the factory, erythropoietin is the order form, and iron is the raw material. In kidney failure the order forms stop coming, and the raw material is locked in the warehouse.}}
<p>The picture has a limit. The marrow keeps working at a low rate even with little erythropoietin, and the lock on the warehouse is a hormone, hepcidin, that rises and falls with inflammation. The monthly hemoglobin is the net of production, iron supply, red cell survival, and blood loss. Module 4 drew the outline of these systems and of the calcium, phosphate, and vitamin D triangle; this module goes one level deeper.</p>
{{cards:Key terms for this module|Erythropoietin (EPO)::The kidney hormone that tells the bone marrow to make red cells.|Erythropoiesis-stimulating agent (ESA)::An injected medicine that acts like erythropoietin, such as epoetin or darbepoetin.|HIF-PHI::Hypoxia-inducible factor prolyl hydroxylase inhibitor. An oral medicine that makes the body produce its own erythropoietin by mimicking low oxygen.|Ferritin::A protein that stores iron. Its blood level reflects iron stores, but it also rises with inflammation.|Transferrin saturation (TSAT)::The share of the iron-carrying protein, transferrin, that is loaded with iron. It reflects iron available to the marrow.|Hepcidin::A liver hormone that blocks iron release from the gut and from storage cells. Inflammation raises it.|Parathyroid hormone (PTH)::The hormone of the parathyroid glands. It raises blood calcium by drawing on bone and kidney.|Calciphylaxis::Calcification and clotting of small skin vessels that causes very painful skin death.}}
<p>Most results on the monthly sheet are slow problems for the attending nephrologist&rsquo;s review. A few need a call today: a sudden hemoglobin fall, symptomatic anemia, a dangerous calcium, possible calciphylaxis, or a fracture. Your work is to read the results as a set, find the urgent few, and report the rest without changing any order.</p>
""",
    "case": {"title": "Hemoglobin falling despite the injections", "html": """
<p>Mr. Arnel Santiago, 54, is a former tricycle driver. He has dialyzed on Tuesdays, Thursdays, and Saturdays for three years. For now he dialyzes through a right internal jugular tunneled catheter while a new fistula matures. He receives an erythropoiesis-stimulating agent (ESA) with each session on the attending nephrologist&rsquo;s order, and the dose was raised last month.</p>
<p>It is Saturday, 9:00 a.m., hour one of his session. The monthly laboratory sheet arrives. The values below are illustrative, not targets:</p>
<div class="table-wrap"><table>
<thead><tr><th>Test</th><th>This month</th><th>Last month</th></tr></thead>
<tbody>
<tr><td>Hemoglobin</td><td>7.9 g/dL</td><td>9.4 g/dL</td></tr>
<tr><td>Ferritin</td><td>820 &micro;g/L</td><td>760 &micro;g/L</td></tr>
<tr><td>Transferrin saturation</td><td>14%</td><td>19%</td></tr>
<tr><td>C-reactive protein</td><td>Elevated</td><td>Mildly elevated</td></tr>
<tr><td>Albumin-corrected calcium</td><td>8.4 mg/dL</td><td>8.6 mg/dL</td></tr>
<tr><td>Phosphate</td><td>7.2 mg/dL</td><td>6.8 mg/dL</td></tr>
<tr><td>Intact PTH (assay upper limit 65 pg/mL)</td><td>1,150 pg/mL</td><td>Not tested</td></tr>
</tbody></table></div>
<p>When you greet him, he mentions two black stools this week. He feels breathless walking to the toilet. His blood pressure is 118/70 mm Hg and his heart rate is 104 per minute. The nurse, Ms. Rowena Lim, has already rechecked his vital signs. She tells you that his catheter exit site looks red.</p>
""", "questions": ["Which finding makes this a same-day call rather than a monthly-review item?",
                  "What do the ferritin and transferrin saturation together say about his iron, and which two causes of poor ESA response stand out?",
                  "What will you report about the phosphate and PTH, and what will you not act on today?"]},
    "sections": [
        ("redcell", "Why hemoglobin falls", "From kidney to red cell: why the hemoglobin falls", """
<p>A healthy kidney senses oxygen. When the oxygen delivered to its tissue falls, a transcription factor called hypoxia-inducible factor (HIF) stays active and switches on the erythropoietin gene. Erythropoietin travels to the marrow, red cell production rises, oxygen delivery recovers, and the signal switches off.[[hall2021]][[kdigo_anemia2026gl]]</p>
{{fig:pod21_kidney_to_red_cell}}
<p>In kidney failure the loop breaks in several places at once. The KDIGO (Kidney Disease: Improving Global Outcomes) 2026 anemia guideline lists the common causes: relatively low erythropoietin, shortened red cell survival, iron and other nutrient deficiencies, blood loss during hemodialysis, uremic toxins that blunt the marrow&rsquo;s response, and inflammation.[[kdigo_anemia2026gl]]</p>
<div class="table-wrap"><table>
<thead><tr><th>What breaks</th><th>How it lowers hemoglobin</th><th>What you may see on the sheet or at the chair</th></tr></thead>
<tbody>
<tr><td>Erythropoietin production</td><td>Scarred kidneys release too little hormone for the degree of anemia</td><td>A slow, steady anemia with low reticulocytes</td></tr>
<tr><td>Iron supply</td><td>Iron is lost with blood, and absorption from the gut is blocked</td><td>Low transferrin saturation, low or falling ferritin</td></tr>
<tr><td>Iron release (hepcidin)</td><td>Inflammation raises hepcidin, which traps iron inside storage cells</td><td>High ferritin with low transferrin saturation, high C-reactive protein</td></tr>
<tr><td>Blood loss</td><td>Blood left in the dialyzer and lines, frequent blood tests, needle bleeding, and gut bleeding</td><td>A fall larger or faster than usual, black stools, clotted circuits</td></tr>
<tr><td>Red cell survival</td><td>Uremia shortens the life of each red cell</td><td>A higher ESA need than expected</td></tr>
</tbody></table></div>
<p>Hepcidin destroys ferroportin, the only known channel that lets iron out of gut and storage cells, so inflammation leaves iron stranded. Blood loss, from tests, the circuit, accidents, and the gut, is the main cause of true iron deficiency in hemodialysis.[[kdigo_anemia2026gl]] Modules 16 and 19 cover clotted circuits and bleeding.</p>
<p>KDIGO 2026 asks for a complete blood count, reticulocytes, ferritin, and transferrin saturation, at least every three months on dialysis. This is a practice point: clinical advice not graded by a systematic review.[[kdigo_anemia2026gl]][[kdigo_anemia2026]] Hemoglobin itself is a surrogate. What patients feel is breathlessness, fatigue, chest pain, and the need for transfusion.</p>
{{key:Read the hemoglobin trend over months, not one value. A slow drift is a monthly-review problem. A sudden fall is a bleeding problem until proven otherwise.}}
"""),
        ("iron", "Iron stores and transit", "Iron stores, iron in transit, iron locked away", """
<p>Think of ferritin as the stock in a warehouse and transferrin saturation (TSAT) as the iron on the delivery trucks. A full warehouse with empty trucks means the doors are locked. In a dialysis patient, the lock is usually inflammation working through hepcidin.</p>
{{fig:pod21_iron_warehouse}}
<p>The picture has a limit. Ferritin also rises with infection and inflammation, so a high ferritin does not prove iron is plentiful. Never read it alone.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pattern</th><th>Ferritin</th><th>TSAT</th><th>Usual meaning</th></tr></thead>
<tbody>
<tr><td>Absolute iron deficiency</td><td>Low</td><td>Low</td><td>Stores are empty. Look for blood loss</td></tr>
<tr><td>Functional iron deficiency</td><td>Normal or high</td><td>Low</td><td>Iron is stored but locked away. Look for inflammation or infection</td></tr>
<tr><td>Iron replete</td><td>Adequate</td><td>Adequate</td><td>Iron is not the limiting factor</td></tr>
<tr><td>Iron overload risk</td><td>High</td><td>High</td><td>More iron is unlikely to help. The guideline advises withholding routine iron</td></tr>
</tbody></table></div>
<h3>What the trial showed</h3>
<p>The PIVOTAL trial randomized 2,141 hemodialysis patients to proactive high-dose intravenous iron, withheld if ferritin exceeded 700 &micro;g/L or TSAT reached 40%, or to reactive low-dose iron, given when ferritin fell below 200 &micro;g/L or TSAT below 20%. Over a median of 2.1 years, nonfatal myocardial infarction, nonfatal stroke, heart failure hospitalization, or death occurred in 29.3% vs. 32.3% (hazard ratio 0.85, 95% confidence interval 0.73 to 1.00). Infection rates were the same, and ESA doses were lower.[[macdougall2019]] The absolute difference of 3.0 percentage points means roughly one event avoided per 33 patients over two years, derived from the reported rates. The trial was open label, and the upper confidence limit touched 1.00. It shows a proactive regimen was not harmful and probably better. It does not show that higher iron indices help every patient.</p>
<h3>What the guideline says</h3>
<div class="table-wrap"><table>
<thead><tr><th>KDIGO 2026 statement (hemodialysis)</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>Start iron if ferritin is 500 &micro;g/L or less and TSAT is 30% or less</td><td>2D (suggestion, very low certainty)</td></tr>
<tr><td>Use intravenous rather than oral iron when starting iron</td><td>2D</td></tr>
<tr><td>Give intravenous iron proactively to keep iron status stable</td><td>Practice point (ungraded)</td></tr>
<tr><td>Withhold routine iron if ferritin is above 700 &micro;g/L or TSAT is 40% or more</td><td>Practice point</td></tr>
<tr><td>Consider pausing iron during a systemic infection</td><td>Practice point</td></tr>
</tbody></table></div>
<p>These grades come from the full guideline.[[kdigo_anemia2026gl]] Every graded iron statement is a suggestion on very low certainty evidence, so the thresholds are starting points for a unit protocol, not proven targets.</p>
{{formula:<strong>Worked example A: transferrin saturation (illustrative).</strong><br>TSAT (%) = serum iron &divide; total iron-binding capacity (TIBC) &times; 100.<br>Serum iron 35 &micro;g/dL, TIBC 250 &micro;g/dL: 35 &divide; 250 &times; 100 = 14%.<br>With ferritin 820 &micro;g/L, this is the pattern of functional iron deficiency. With a low ferritin, the same TSAT would point to absolute deficiency.[[kdigo_anemia2026gl]]<br>What it tells you: whether iron is reaching the marrow. What it does not tell you: the cause of the block, or whether more iron would help. The site&rsquo;s transferrin saturation calculator does this arithmetic.}}
<p>Iron orders belong to the attending nephrologist and your unit&rsquo;s anemia protocol. You read the pattern and report changes.</p>
{{key:Ferritin tells you what is stored. TSAT tells you what is moving. Read them together.}}
"""),
        ("agents", "ESAs and HIF-PHIs", "Stimulating agents, the newer oral agents, and why &ldquo;normal&rdquo; was harmful", """
<p>An ESA is the order form itself, given by injection. A HIF-PHI, taken by mouth, tricks the body&rsquo;s oxygen sensor so the kidney and liver make more of their own erythropoietin.</p>
<p>The picture has a limit. HIF switches on many genes besides erythropoietin, and both classes carry concerns about clots and cancer.[[kdigo_anemia2026gl]] So the trials counted strokes and heart events, not only hemoglobin. Three trials that aimed for a normal hemoglobin found harm or a trend toward it; the table sets them beside the iron and HIF-PHI trials.</p>
<div class="table-wrap"><table>
<thead><tr><th>Trial</th><th>Population</th><th>Comparison</th><th>Result</th></tr></thead>
<tbody>
<tr><td>Normal Hematocrit Trial[[besarab1998]]</td><td>1,233 on hemodialysis with heart disease</td><td>Hematocrit 42% vs. 30%</td><td>183 deaths and 19 myocardial infarctions vs. 150 and 14 (risk ratio 1.3, 0.9 to 1.9). Halted</td></tr>
<tr><td>CHOIR[[singh2006]]</td><td>1,432 not on dialysis</td><td>Hemoglobin 13.5 vs. 11.3 g/dL</td><td>125 vs. 97 events (hazard ratio 1.34, 1.03 to 1.74)</td></tr>
<tr><td>TREAT[[pfeffer2009]]</td><td>4,038 with diabetes, not on dialysis</td><td>Darbepoetin vs. placebo</td><td>No fall in death or cardiovascular events. Stroke 101 vs. 53 (hazard ratio 1.92, 1.38 to 2.68)</td></tr>
<tr><td>PIVOTAL[[macdougall2019]]</td><td>2,141 on hemodialysis</td><td>Proactive vs. reactive intravenous iron</td><td>29.3% vs. 32.3% (hazard ratio 0.85, 0.73 to 1.00)</td></tr>
<tr><td>ASCEND-D[[singh2021]]</td><td>2,964 on dialysis</td><td>Daprodustat vs. ESA</td><td>Major cardiovascular events 25.2% vs. 26.7% (hazard ratio 0.93, 0.81 to 1.07)</td></tr>
<tr><td>INNO2VATE[[eckardt2021]]</td><td>3,923 on dialysis</td><td>Vadadustat vs. darbepoetin</td><td>Major cardiovascular events 18.2% vs. 19.3% (hazard ratio 0.96, 0.83 to 1.11)</td></tr>
</tbody></table></div>
<p>The Normal Hematocrit Trial was halted before reaching its stopping boundary.[[besarab1998]] CHOIR and TREAT enrolled patients not on dialysis and are quoted for the lesson about targets only. In TREAT, stroke occurred in about 5.0% vs. 2.6%, an absolute excess of about 2.4 percentage points, derived from the reported counts.[[pfeffer2009]] The mechanism is not settled; higher ESA doses and higher blood pressure are plausible contributors. The outcome is settled: aiming for normal did not improve how patients felt or how long they lived, and it increased strokes.</p>
<p>The HIF-PHIs daprodustat and vadadustat were noninferior to ESAs for hemoglobin and for major adverse cardiovascular events in dialysis patients.[[singh2021]][[eckardt2021]] Roxadustat was noninferior to epoetin for hemoglobin in 305 Chinese dialysis patients over 26 weeks.[[chen2019]] Noninferior means &ldquo;not unacceptably worse,&rdquo; not &ldquo;better.&rdquo; KDIGO rated the certainty of evidence comparing the classes in dialysis as very low, and the long-term risks of HIF-PHIs outside trials are unknown.[[kdigo_anemia2026gl]]</p>
<h3>What the guideline says</h3>
<div class="table-wrap"><table>
<thead><tr><th>KDIGO 2026 statement</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>In adults on an ESA, target hemoglobin below 11.5 g/dL</td><td>1D (recommendation, very low certainty)</td></tr>
<tr><td>On dialysis, consider starting an ESA when hemoglobin is 9.0 to 10.0 g/dL or lower</td><td>2D</td></tr>
<tr><td>Once correctable causes are addressed, use an ESA rather than a HIF-PHI first</td><td>2D</td></tr>
<tr><td>Do not combine an ESA with a HIF-PHI</td><td>Practice point</td></tr>
<tr><td>Do not use a HIF-PHI with active cancer, a recent cardiovascular event, or recent vascular thrombosis</td><td>Practice point</td></tr>
<tr><td>It is reasonable to suspend the ESA during hospitalization for acute stroke, access thrombosis, or other clots</td><td>Practice point</td></tr>
</tbody></table></div>
<p>A HIF-PHI may be chosen for a preference for an oral agent, ESA intolerance, or no refrigeration.[[kdigo_anemia2026gl]] The 11.5 g/dL ceiling is the one strong recommendation, yet its certainty is very low: strength and certainty are separate judgments.</p>
<p>Your unit&rsquo;s protocol sets the working range and dose steps. Report values outside the range. Never change an ESA or HIF-PHI dose yourself; hold one only if the protocol directs it, for example after a stroke or access clot, and call the attending nephrologist the same day.</p>
{{key:Higher hemoglobin was not better. The trials that aimed for normal found more strokes and clots.}}
"""),
        ("response", "Poor response", "When the injections stop working", """
<p>Sometimes the order form arrives and the hemoglobin still does not rise. The factory may be out of material, on strike, or losing product out the back door. This is ESA hyporesponsiveness: hemoglobin below target despite a significant dose increase, or persistently high doses to hold it.[[kdigo_anemia2026gl]]</p>
<p>Poor response is associated with more cardiovascular events and death. The link is observational, and poor response may mark illness rather than cause harm. The commonest causes are inflammation and iron deficiency; no cause is found in about 30%, and it is often transient.[[kdigo_anemia2026gl]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Cause</th><th>Clue</th><th>Test or check, per protocol</th></tr></thead>
<tbody>
<tr><td>Iron deficiency</td><td>Low TSAT, low or falling ferritin</td><td>Iron indices. Look for blood loss</td></tr>
<tr><td>Inflammation or infection</td><td>High ferritin with low TSAT. Fever. A red catheter exit site</td><td>C-reactive protein, temperature, exit site and tunnel inspection (Module 10)</td></tr>
<tr><td>Blood loss</td><td>Black stools, vomiting blood, heavy menses, repeated circuit clotting</td><td>Stool test for blood, circuit clotting log (Module 16)</td></tr>
<tr><td>Inadequate dialysis</td><td>Missed or shortened sessions, poor access flow, a falling dose measure</td><td>Adequacy results (Module 7)</td></tr>
<tr><td>Severe hyperparathyroidism</td><td>Very high PTH, bone pain</td><td>PTH and alkaline phosphatase</td></tr>
<tr><td>B12 or folate deficiency, hemolysis, marrow disease</td><td>Large red cells, poor diet, low haptoglobin, falling white cells or platelets</td><td>Vitamin B12, folate, lactate dehydrogenase, smear</td></tr>
</tbody></table></div>
<p>The guideline&rsquo;s list also names hypothyroidism, malnutrition, and pure red cell aplasia, a rare antibody reaction to the ESA. Causes should be treated before an ESA dose is pushed higher. A HIF-PHI trial may be considered for persistent hyporesponsiveness, a practice point on evidence the work group calls weak.[[kdigo_anemia2026gl]][[kdigo_anemia2026]]</p>
{{flow:Low hemoglobin work-up ladder|Bleeding first::Stools, vomiting blood, needle sites, circuit clotting, pulse, pressure.|Iron::Ferritin and TSAT together.|Inflammation::Temperature, C-reactive protein, catheter exit site.|Adequacy and PTH::Missed sessions, adequacy result, PTH.|Report::List findings for the attending nephrologist. Change no order.}}
<p>The site&rsquo;s ESA resistance index calculator tracks the dose needed per unit of hemoglobin over months.</p>
{{formula:<strong>Worked example C: sudden drop or slow drift (illustrative decision walk-through).</strong><br>Change in hemoglobin = this month &minus; last month.<br>Patient 1: 7.9 &minus; 9.4 = &minus;1.5 g/dL in one month, with two black stools and a heart rate of 104 per minute. Sort as possible bleeding, not ESA failure. Stop and call. Hold heparin per your unit&rsquo;s protocol (Module 19). Transfuse only per protocol or on the attending nephrologist&rsquo;s instruction.<br>Patient 2: 10.1 &minus; 10.4 = &minus;0.3 g/dL, with a red catheter exit site and a TSAT of 16%. Sort as poor response for the monthly review, and report the exit site today.<br>What the number tells you: how fast the hemoglobin moved. What it does not tell you: why. The fall, the symptoms, and the pulse together set the urgency.[[kdigo_anemia2026gl]]}}
{{call:Stop and call the attending nephrologist the same hour for a sudden fall in hemoglobin, for anemia with black stools, vomiting blood, or other signs of bleeding, and for anemia with symptoms: chest pain, breathlessness at rest, fainting, or a fast pulse that does not settle. Follow your unit&rsquo;s protocol for the first steps while you call.}}
{{key:Before you blame the injection, look for the four common culprits: bleeding, iron, inflammation, and underdialysis.}}
"""),
        ("transfusion", "Transfusion", "Transfusion: when, and what it costs a future transplant", """
<p>A transfusion borrows another person&rsquo;s red cells and leaves a memory in the immune system. Donor blood carries human leukocyte antigens (HLA), the tissue-type markers a transplant team matches. The recipient may make antibodies against them. This is called sensitization, or allosensitization.</p>
<p>The picture has a limit. Not every transfusion sensitizes, and the risk has probably fallen with changes in transfusion practice. Removing white cells from blood products does not remove it. Sensitization has been linked with longer waits for a transplant and more graft rejection.[[kdigo_anemia2026gl]]</p>
<p>In a Taiwanese cross-sectional study of 289 patients with kidney failure and 888 healthy controls, HLA antibodies were present in 23.2% vs. 12.8%. Kidney failure itself was not an independent risk factor; pregnancy and recent transfusion were. A transfusion within the past year carried the highest odds (odds ratio 10.06).[[hung2014]] The study was observational and from one hospital. The guideline also cites a systematic review of 180 studies in which risk rose with the number of units given.[[kdigo_anemia2026gl]]</p>
<div class="table-wrap"><table>
<thead><tr><th>KDIGO 2026 practice point (ungraded)</th><th>What it means on your shift</th></tr></thead>
<tbody>
<tr><td>Base transfusion on symptoms and signs, not an arbitrary hemoglobin threshold</td><td>A low number alone is not an emergency</td></tr>
<tr><td>Consider transfusion when rapid correction is needed, such as acute hemorrhage or unstable coronary disease</td><td>Bleeding or ischemia changes the balance at once</td></tr>
<tr><td>In transplant candidates, avoid transfusion when possible</td><td>Ask about transplant plans first</td></tr>
<tr><td>Transfusion may outweigh its harms when ESAs or HIF-PHIs fail or may harm, such as after a stroke or with cancer</td><td>The attending nephrologist decides</td></tr>
</tbody></table></div>
<p>These practice points are from the full guideline and are ungraded expert advice.[[kdigo_anemia2026gl]]</p>
{{flow:Transfusion decision|Unstable?::Chest pain, breathlessness at rest, fainting, low pressure, or active bleeding. Follow your unit&rsquo;s protocol and call the attending nephrologist now.|Bleeding?::Black stools, vomiting blood, or a fast fall. Treat as bleeding (Module 19) while you call.|Stable?::A low number without symptoms is a question, not an order.|Transplant planned?::Check the chart and tell the attending nephrologist, so the plan weighs sensitization (Module 27).|Write::Hemoglobin, symptoms, vital signs, transplant status, and the advice received.}}
<p>When blood is ordered, the units and timing follow your unit&rsquo;s protocol. A patient who passes little urine keeps the extra fluid (Module 14).</p>
{{key:Transfuse for the patient in front of you, not for the number. Ask about transplant plans before any transfusion that can wait.}}
"""),
        ("phosphate", "Phosphate", "Phosphate in, phosphate out", """
<p>Phosphate pours in with every meal, seven days a week. Three dialysis sessions bail out only part of it. Binders catch some at meals. The gap stays in the body.</p>
{{fig:pod21_phosphate_in_out}}
<p>The picture has a limit. Most body phosphate sits inside cells and bone, with only a small share in the blood.[[hall2021]] During a session blood phosphate falls quickly, then removal slows because phosphate leaves the cells slowly. Longer or more frequent sessions therefore remove more.[[daugirdas2015]]</p>
<p>As kidney function falls, bone cells release fibroblast growth factor 23 (FGF23) and the parathyroid glands release more PTH. Both push the remaining nephrons to excrete phosphate, and FGF23 suppresses activation of vitamin D. For a time phosphate stays normal. When too few nephrons remain, compensation fails: phosphate rises, and high FGF23, high PTH, and low active vitamin D remain.[[ketteler2017]][[kdigo_mbd2017]] This cluster of laboratory, bone, and vessel changes is chronic kidney disease&ndash;mineral and bone disorder (CKD-MBD).</p>
<p>Phosphate targets have rested on observational studies, in which high phosphate is associated with worse outcomes.[[kdigo_mbd2017]][[edmonston2025]] Diet, nutrition, and dialysis dose affect both phosphate and survival, so these associations can be confounded. No trial has shown that lowering phosphate prevents those outcomes.</p>
<h3>What the guideline says</h3>
<div class="table-wrap"><table>
<thead><tr><th>KDIGO 2017 CKD-MBD statement</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>Base treatment on serial phosphate, calcium, and PTH considered together</td><td>Not graded</td></tr>
<tr><td>Lower elevated phosphate toward the normal range</td><td>2C</td></tr>
<tr><td>Base phosphate-lowering treatment on progressively or persistently high phosphate</td><td>Not graded</td></tr>
<tr><td>In adults, restrict the dose of calcium-based binders</td><td>2B</td></tr>
<tr><td>Avoid long-term aluminum-containing binders</td><td>1C</td></tr>
<tr><td>Limit dietary phosphate</td><td>2D</td></tr>
<tr><td>On dialysis, increase dialytic phosphate removal for persistent high phosphate</td><td>2C</td></tr>
</tbody></table></div>
<p>Grades are from the guideline&rsquo;s summary of recommendations.[[kdigo_mbd2017]] &ldquo;Toward the normal range&rdquo; is deliberately not a fixed target, and the update moved away from acting on a single result.[[ketteler2017]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Binder type</th><th>How taken</th><th>Main issue</th><th>Evidence note</th></tr></thead>
<tbody>
<tr><td>Calcium-based (carbonate, acetate)</td><td>With meals</td><td>Adds calcium. Can raise blood calcium and feed calcification</td><td>KDIGO suggests restricting the dose (2B)[[kdigo_mbd2017]]</td></tr>
<tr><td>Sevelamer</td><td>With meals</td><td>Large tablets, pill burden, bloating, constipation</td><td>Calcium-free</td></tr>
<tr><td>Lanthanum</td><td>Chewed with meals</td><td>Nausea. Tablets must be chewed</td><td>Calcium-free</td></tr>
<tr><td>Iron-based (sucroferric oxyhydroxide, ferric citrate)</td><td>With meals</td><td>Dark stools, diarrhea</td><td>Calcium-free. Dark stools can be mistaken for bleeding</td></tr>
<tr><td>Aluminum-based</td><td>Rarely used</td><td>Aluminum builds up in bone and brain</td><td>Avoid long-term use (1C)[[kdigo_mbd2017]]</td></tr>
</tbody></table></div>
<p>Module 20 covers binder pill burden, and Module 23 covers phosphate in Filipino foods.</p>
<p>A meta-analysis of 11 randomized trials with 4,622 patients found 22% lower all-cause mortality with non-calcium than with calcium-based binders (risk ratio 0.78, 0.61 to 0.98).[[jamal2013]] Many trials were small and open label, and the upper limit sits near 1. The finding supports limiting calcium-based binders; it does not prove that any one binder saves lives.</p>
<p>The HiLo trial compared a higher phosphate target (6.5 mg/dL or above) with a lower one (below 5.5 mg/dL) in hemodialysis. It planned 4,400 patients, enrolled 793, and stopped early for poor enrollment and too little separation between groups (win ratio 0.97, 0.55 to 1.71). The authors concluded that no inference about targets was possible.[[edmonston2025]] Phosphate is a surrogate; the outcomes that matter are death, fractures, cardiovascular events, and how patients feel.</p>
<p>The site&rsquo;s CKD-MBD calculator sets calcium, phosphate, and PTH side by side. Binder and diet changes belong to the attending nephrologist and the dietitian.</p>
{{key:No trial has yet shown that a particular phosphate target saves lives. The guidance is to lower high phosphate toward normal, with low certainty.}}
"""),
        ("parathyroid", "Parathyroid and calcium", "The overworked parathyroid gland", """
<p>Picture a thermostat that keeps turning up the heat because the room never feels warm. The parathyroid glands are the thermostat; blood calcium and active vitamin D are the room temperature. In kidney failure active vitamin D stays low and phosphate stays high, so the glands keep releasing PTH.</p>
<p>The picture has a limit. A thermostat does not grow, but parathyroid glands do. Under constant stimulation they enlarge and respond less to the signals that should switch them off, so severe disease can resist medicines.[[kdigo_mbd2017]]</p>
{{fig:pod21_overworked_parathyroid}}
<p>PTH pulls calcium and phosphate out of bone, so over years the skeleton thins and fractures become more likely. Calcium and phosphate from bone, food, binders, and dialysis fluid can settle in artery walls and valves. The patient can have weak bones and calcified arteries at once.[[ketteler2017]] Pushing PTH too low also harms: bone turnover nearly stops, a state called adynamic bone disease, which is linked with vascular calcification and calciphylaxis.[[chewcharat2025]]</p>
{{fig:pod21_bone_and_vessel}}
<p>At the chair, watch for bone pain and fractures, itch (Module 24), confusion from high calcium (Module 18), and tingling or cramps from low calcium, often on a calcimimetic.</p>
<h3>What the guideline says</h3>
<div class="table-wrap"><table>
<thead><tr><th>KDIGO 2017 statement (dialysis patients)</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>Keep intact PTH at about 2 to 9 times the upper normal limit for the assay</td><td>2C</td></tr>
<tr><td>Let marked changes in PTH within that range prompt a change in therapy</td><td>2C</td></tr>
<tr><td>When PTH lowering is needed, use calcimimetics, calcitriol, or vitamin D analogs, alone or combined</td><td>2B</td></tr>
<tr><td>In adults, avoid hypercalcemia</td><td>2C</td></tr>
<tr><td>Use dialysis fluid calcium of 1.25 to 1.50 mmol/L (2.5 to 3.0 mEq/L)</td><td>2C</td></tr>
<tr><td>For severe hyperparathyroidism that fails medical treatment, consider parathyroidectomy</td><td>2B</td></tr>
</tbody></table></div>
<p>Grades are from the guideline summary; every statement is a suggestion.[[kdigo_mbd2017]] Module 7 showed the dialysis fluid calcium on the order.</p>
{{formula:<strong>Worked example B: PTH as a multiple of the assay&rsquo;s upper limit (illustrative).</strong><br>Multiple = intact PTH &divide; the assay&rsquo;s upper normal limit (same units).<br>1,150 pg/mL &divide; 65 pg/mL = about 17.7 times the upper limit, against a KDIGO 2017 suggestion of about 2 to 9 times (2C).[[kdigo_mbd2017]]<br>What it tells you: where the result sits against a weak suggestion. What it does not tell you: what to prescribe, or how the bone looks. Always use the limit printed on that report; raw PTH values differ between assays.}}
<p>EVOLVE randomized 3,883 hemodialysis patients with moderate to severe secondary hyperparathyroidism to cinacalcet, a calcimimetic, or placebo. Death or a major cardiovascular event occurred in 48.2% vs. 49.2% (hazard ratio 0.93, 0.85 to 1.02), not a significant reduction in the unadjusted primary analysis. Low calcium and gastrointestinal effects were more frequent.[[chertow2012]] In 683 patients, intravenous etelcalcetide lowered PTH by more than 30% in more patients than cinacalcet (68.2% vs. 57.7%), with more low calcium (68.9% vs. 59.8%).[[block2017]] PTH is a surrogate; that trial did not test death, fractures, or heart events.</p>
<p>Report the PTH trend and multiple. Read calcium against treatment: low on a calcimimetic, high on calcitriol, a vitamin D analog, or calcium binders. Use albumin-corrected calcium where ionized calcium is not reported. Medicine changes belong to the attending nephrologist.</p>
{{call:Stop and call the attending nephrologist the same day for a calcium outside your unit&rsquo;s alert range, for new confusion or drowsiness with high calcium, for tingling, spasm, or seizure with low calcium, especially on a calcimimetic, and for a suspected fracture. Follow your unit&rsquo;s protocol for an electrocardiogram (ECG) and first steps while you call.}}
{{key:Divide every PTH by its assay&rsquo;s upper limit, and read every calcium against the medicines that move it.}}
"""),
        ("calciphylaxis", "Calciphylaxis", "Calciphylaxis: the wound that must not be missed", """
<p>In calciphylaxis, the small vessels that feed the skin and the fat beneath it slowly turn to stone, then clot. The skin above them loses its blood supply and dies.</p>
<p>The picture has a limit. Calcium alone does not explain it. Inflammation, low levels of the body&rsquo;s natural calcification inhibitors, and clotting all take part, and the cause is still poorly understood.[[chewcharat2025]] That is one reason no treatment is proven.</p>
{{fig:pod21_calciphylaxis}}
<h3>What it looks like</h3>
<p>The lesions are excruciatingly painful. Early ones are violaceous, plaque-like nodules, firm areas under the skin, or a net-like purple mottling called livedo reticularis. As vessels clot, they become necrotic ulcers with black crusts called eschars. They favor fatty areas: the abdomen, buttocks, and thighs. Pulses are usually present and lesions often bilateral, unlike blocked large arteries.[[chewcharat2025]] An early lesion may be only a tender, firm area, so a complaint of pain deserves a look under the clothing.</p>
<div class="table-wrap"><table>
<thead><tr><th>Risk factor named in a recent review</th><th>Why it matters on your shift</th></tr></thead>
<tbody>
<tr><td>Female sex, obesity, diabetes</td><td>Raise your suspicion</td></tr>
<tr><td>Warfarin, calcium, vitamin D analogs, iron</td><td>Note them for the attending nephrologist</td></tr>
<tr><td>High calcium, phosphate, or PTH, or over-suppressed PTH</td><td>Read the mineral panel</td></tr>
<tr><td>Inflammatory disease, recurrent skin trauma, a tendency to clot</td><td>Ask about skin injections and clots</td></tr>
</tbody></table></div>
<p>These risk factors, from a 2025 expert review, raise suspicion; they do not prove cause. The review reports a mortality of about 37% at six months. Treatment is multidisciplinary and largely unproven: control of the mineral panel, stopping warfarin where possible, stopping calcium and vitamin D supplements, adequate dialysis, wound and pain care, and an off-label trial of sodium thiosulfate, which meta-analyses of observational studies have not shown to improve survival or healing.[[chewcharat2025]]</p>
<p>Your part: look at the skin, describe and measure the lesion, photograph it with consent under your unit&rsquo;s privacy rules, and report it the same day.</p>
{{call:Stop and call the attending nephrologist the same day for any painful skin lesion with purple mottling, a firm purple plaque, or a black crusted ulcer in a dialysis patient. Report the medicines and the latest calcium, phosphate, and PTH. Do not start or stop any medicine on your own.}}
{{flow:What to flag, to whom, how fast|Same hour::Sudden hemoglobin fall, anemia with bleeding signs or symptoms, symptomatic abnormal calcium. Call the attending nephrologist and follow protocol.|Same day::Suspected calciphylaxis or fracture, calcium outside the alert range, a red exit site with falling hemoglobin.|Monthly review::Slow hemoglobin drift, iron patterns, rising ESA needs, phosphate and PTH trends. List them in your note.|Write::Values, trend, findings, whom you called and when, and the advice.}}
{{key:Believe the pain. A painful purple patch on the thigh of a dialysis patient is calciphylaxis until the attending nephrologist says otherwise.}}
"""),
    ],
    "debrief": ["""
<p><strong>Which finding makes this a same-day call?</strong> A fall from 9.4 to 7.9 g/dL in one month is faster than poor ESA response usually produces. With two black stools, breathlessness on minimal effort, and a pulse of 104 per minute before much fluid has been removed, this is possible gastrointestinal bleeding until proven otherwise. You ask about vomiting blood, check the access and circuit, and ask Ms. Lim to follow the heparin protocol. You call the attending nephrologist within the hour using SBAR (situation, background, assessment, recommendation) from Module 1. Transfusion or admission is the attending nephrologist&rsquo;s decision. Iron can darken stools, but that possibility does not delay the call.</p>
<p><strong>What do ferritin and TSAT say?</strong> Ferritin 820 &micro;g/L with TSAT 14% is functional iron deficiency: iron stored but locked away. The high C-reactive protein and red exit site point to catheter-related inflammation as the lock. The two causes of poor response that stand out are catheter inflammation or infection, and blood loss. Neither is fixed by a higher ESA dose. You report the exit site for assessment per protocol (Module 10). Iron decisions wait for the attending nephrologist.</p>
<p><strong>What will you report, and what will you not act on?</strong> The PTH is about 17.7 times the assay&rsquo;s upper limit, above the 2-to-9-times range KDIGO 2017 suggests (2C). Phosphate is high and rising. Corrected calcium does not explain symptoms. You list these for the monthly review with his binder and vitamin D medicines, and note that severe hyperparathyroidism can blunt ESA response. You change no binder, vitamin D analog, calcimimetic, dialysis fluid calcium, or ESA.</p>
"""],
    "skills": {"title": "Monthly anemia and mineral review with the nurse",
               "intro": "Perform this review with a nurse on a real or simulated monthly laboratory sheet while your preceptor observes.",
               "items": [
                   ("Lays out the last three to six months of hemoglobin, ferritin, TSAT, calcium, phosphate, and PTH side by side.", False),
                   ("Identifies any fall in hemoglobin large or fast enough to suggest bleeding, and asks about black stools, vomiting blood, and circuit clotting.", True),
                   ("Asks about symptoms of anemia: breathlessness at rest, chest pain, fainting, and checks pulse and blood pressure.", True),
                   ("Reads ferritin and TSAT together and names the pattern: absolute deficiency, functional deficiency, or replete.", False),
                   ("Checks for causes of poor ESA response: catheter infection, inflammation, missed or short sessions, and PTH.", False),
                   ("States the unit&rsquo;s hemoglobin range and the guideline ceiling, without changing any dose.", False),
                   ("Computes PTH as a multiple of the assay&rsquo;s upper limit and states where it sits against the KDIGO 2017 suggestion.", False),
                   ("Reads calcium against the patient&rsquo;s calcimimetic, vitamin D, and binder therapy.", False),
                   ("Asks about transplant plans before any non-urgent transfusion is discussed.", False),
                   ("Inspects the skin of the legs, thighs, and abdomen of a patient who reports a new painful lesion, and describes it.", True),
                   ("Reports same-day findings to the attending nephrologist with an SBAR report and repeats back the advice.", True),
                   ("Lists monthly-review findings in a summary note and documents the review.", False),
               ],
               "placement": "For one month, review the monthly laboratory sheet with the nurse for every patient on your shift. For each patient, write the hemoglobin trend, the iron pattern, and the PTH multiple. Discuss with your preceptor which findings you would have called the same day, and why."},
    "quiz": [
        ("Why does inflammation cause anemia in a dialysis patient even when iron stores are full?",
         ["It destroys erythropoietin", "It raises hepcidin, which traps iron in storage cells", "It lowers ferritin", "It lengthens red cell survival"], 1,
         "Hepcidin closes the iron exit channel, so stored iron cannot reach the marrow."),
        ("A patient has ferritin 900 &micro;g/L, TSAT 12%, and a high C-reactive protein. Which pattern is this?",
         ["Iron overload", "Absolute iron deficiency", "Functional iron deficiency", "Iron replete"], 2,
         "Iron is stored but not moving. Inflammation is the usual lock."),
        ("A patient has ferritin 60 &micro;g/L and TSAT 11%. What should you look for first?",
         ["A source of blood loss", "Iron overload", "Vitamin D deficiency", "A high PTH"], 0,
         "Empty stores in a dialysis patient usually mean blood loss."),
        ("What did PIVOTAL show for proactive high-dose intravenous iron compared with reactive low-dose iron?",
         ["More infections", "No change in ESA dose", "Higher mortality", "Fewer cardiovascular events and deaths, with lower ESA doses"], 3,
         "29.3% vs. 32.3% (hazard ratio 0.85), with equal infection rates."),
        ("What grade does KDIGO 2026 give to intravenous rather than oral iron in hemodialysis?",
         ["1A", "2D", "Practice point", "1B"], 1,
         "A suggestion on very low certainty evidence."),
        ("Which statement about hemoglobin targets do the trials support?",
         ["Aiming for normal increased strokes or cardiovascular events without better quality of life", "Aiming for normal reduced deaths", "Higher targets were harmless", "Targets made no difference"], 0,
         "Normal Hematocrit, CHOIR, and TREAT all pointed to harm. KDIGO 2026 sets a ceiling below 11.5 g/dL (1D)."),
        ("What did ASCEND-D and INNO2VATE show about HIF-PHIs in dialysis?",
         ["Superior survival", "Doubled stroke", "Noninferior to ESAs for major cardiovascular events", "No rise in hemoglobin"], 2,
         "Noninferior is not better. KDIGO 2026 still suggests an ESA first (2D)."),
        ("Mr. Reyes&rsquo;s hemoglobin fell from 10.2 to 8.4 g/dL in a month. He reports black stools, and his pulse is 108 at the start of the session. What do you do?",
         ["Suggest a higher ESA dose at the monthly review", "Start oral iron", "Record it for the monthly review", "Treat it as possible bleeding and call the attending nephrologist now"], 3,
         "A fast fall with black stools and a fast pulse is bleeding until proven otherwise."),
        ("Mrs. Dizon&rsquo;s hemoglobin has drifted down over three months despite rising ESA doses. Her catheter exit site is red and C-reactive protein is high. What is most likely?",
         ["Catheter inflammation blocking the ESA response", "Too much iron", "Too little binder", "Normal aging"], 0,
         "Inflammation is a leading cause of poor response. Report the exit site today."),
        ("Mr. Cruz, on the transplant waiting list, has a hemoglobin of 7.8 g/dL, no symptoms, normal vital signs, and no bleeding. The nurse asks about transfusion. What is best?",
         ["Transfuse for the number", "Call the attending nephrologist first, noting his transplant plans and lack of symptoms", "Give an extra ESA dose", "Start a HIF-PHI"], 1,
         "Transfuse for symptoms, and avoid transfusion when possible in transplant candidates."),
        ("An intact PTH is 520 pg/mL; the assay&rsquo;s upper limit is 65 pg/mL. Where does it sit against KDIGO 2017?",
         ["Below the range", "At 8 times, within about 2 to 9 times", "At 17 times, above the range", "Cannot be judged"], 1,
         "520 &divide; 65 = 8 (2C suggestion)."),
        ("What did EVOLVE show?",
         ["Cinacalcet halved cardiovascular events", "Cinacalcet increased deaths", "Cinacalcet had no side effects", "No significant reduction in death or major cardiovascular events in the primary analysis"], 3,
         "48.2% vs. 49.2% (hazard ratio 0.93, 0.85 to 1.02)."),
        ("What did the HiLo phosphate target trial conclude?",
         ["A lower target saved lives", "A higher target was safer", "No inference was possible", "Phosphate does not matter"], 2,
         "It stopped early with poor enrollment and separation."),
        ("Mrs. Bautista takes cinacalcet and reports tingling around her mouth and finger cramps. What do you do?",
         ["Suspect low calcium: follow protocol, check calcium and an ECG, and call", "Give a binder", "Order iron studies", "Photograph her hands"], 0,
         "Calcimimetics lower calcium. Symptoms make it a same-day call."),
        ("Mrs. Santos, 61, has diabetes and obesity, takes warfarin, and reports a very painful, firm purple patch on her thigh. What is best?",
         ["Call it a warfarin bruise", "Record it for the monthly review", "Inspect, describe, and photograph it with consent, and call the attending nephrologist the same day", "Stop her warfarin"], 2,
         "This suggests calciphylaxis. Medicine changes belong to the attending nephrologist."),
    ],
    "terms": [("Erythropoietin", "The kidney hormone that tells the bone marrow to make red cells."),
              ("Erythropoiesis-stimulating agent (ESA)", "An injected medicine that acts like erythropoietin."),
              ("HIF-PHI", "An oral medicine that mimics low oxygen so the body makes more of its own erythropoietin."),
              ("Hepcidin", "A liver hormone that blocks iron release. Inflammation raises it."),
              ("Functional iron deficiency", "Iron stored in the body but unavailable to the marrow, shown by a normal or high ferritin with a low TSAT."),
              ("ESA hyporesponsiveness", "A hemoglobin that does not reach the target despite a significant increase in ESA dose, or that needs persistently high doses."),
              ("Allosensitization", "Antibodies against another person&rsquo;s tissue markers, which can follow transfusion or pregnancy and make transplant matching harder."),
              ("Secondary hyperparathyroidism", "Overactivity of the parathyroid glands driven by kidney failure."),
              ("Calcimimetic", "A medicine that makes the parathyroid gland sense more calcium than is present, so it releases less PTH."),
              ("Calciphylaxis", "Calcification and clotting of small skin vessels that causes very painful skin death.")],
    "readings": [("anemia-management.html", "How anemia in kidney disease is evaluated and treated, with iron and stimulating agents."),
                 ("epo-resistant-renal-anemia.html", "Causes and work-up of a poor response to erythropoiesis-stimulating agents."),
                 ("ckd-mbd.html", "Calcium, phosphate, parathyroid hormone, and vitamin D in kidney disease.")],
    "calcs": ["calc-iron-status-tsat.html", "calc-eri.html", "calc-ckd-mbd.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
