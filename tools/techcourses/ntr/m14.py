# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 14: Anemia in CKD.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard.
KDIGO 2026 anemia recommendations, practice points and grades checked against the published guideline
(Kidney Int 2026;109(1S):S1-S99) and its executive summary (Kidney Int 2026;109:44-56). TREAT, CHOIR, PIVOTAL
and ASCEND-ND numbers from the PubMed abstracts. PhilHealth package wording from the PhilHealth news release
and Advisory 2024-0036. No doses. Fictional case."""

MODULE = {
    "image_alt": "A nephrology fellow and an internal medicine resident review a complete blood count and iron studies with an older Filipino woman with chronic kidney disease in a Quezon City clinic.",
    "objectives": [
        "<strong>Intern:</strong> Recognize anemia in a patient with chronic kidney disease (CKD), take the bleeding, diet, medicine and transfusion history, and collect the first test set your resident orders without missing a sample.",
        "<strong>Resident:</strong> Work up anemia and iron status in CKD, look for every correctable cause before blaming the kidneys, and propose iron therapy using the thresholds of the Kidney Disease: Improving Global Outcomes (KDIGO) 2026 anemia guideline.",
        "<strong>Fellow:</strong> Apply the KDIGO 2026 guidance on iron, erythropoiesis-stimulating agents (ESAs), hypoxia-inducible factor prolyl hydroxylase inhibitors (HIF-PHIs) and transfusion with their stated grades, keep hemoglobin (Hgb) below the recommended ceiling, and manage hyporesponsiveness.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the tired patient with a low hemoglobin</span>The <strong>intern</strong> notices the pallor, asks about black stools, pain tablets and past transfusions, and gets the right tubes to the laboratory before any iron or blood is given. The <strong>resident</strong> builds the work-up, names the correctable causes, and proposes iron with the guideline threshold that justifies it. The <strong>fellow</strong> decides with the attending whether and when to add an ESA or a HIF-PHI, sets the hemoglobin ceiling, and keeps transfusion for the patient who truly needs it.</div>
{{plain:Picture a garment factory in Taytay. A foreman watches the orders and tells the sewers how many shirts to make. The sewers need cloth from a bodega. If the foreman stops calling for shirts, production falls. If the bodega is locked, the sewers stand idle even when the foreman shouts. In the body the kidney is the foreman, erythropoietin is the order slip, the bone marrow is the sewing floor, and iron is the cloth.}}
<p>The picture has a limit. A factory has one foreman and one bodega. In CKD both fail together, and for linked reasons. The kidney&rsquo;s oxygen sensor sits in fibroblast-like cells around the tubules. When they sense low oxygen, the hypoxia-inducible factor (HIF) pathway switches on the erythropoietin gene. In diseased kidneys these cells are scarred and the signal is too small for the degree of anemia. At the same time, inflammation and reduced kidney clearance raise hepcidin, the liver hormone that locks iron inside gut cells and macrophages. The marrow then has orders it cannot fill. Blood lost to dialysis circuits, phlebotomy and the gut drains the bodega further.[[ntr14_3]]</p>
{{cards:Key numbers|Anemia in adults (KDIGO 2026)::Hemoglobin (Hb) below 13.0 g/dL in men and below 12.0 g/dL in women|Start iron in hemodialysis (KDIGO 2026)::Ferritin &le;500 ng/mL and transferrin saturation (TSAT) &le;30% (2D)|Start iron, no dialysis or peritoneal dialysis (KDIGO 2026)::Ferritin below 100 ng/mL with TSAT below 40%, or ferritin 100 to 300 ng/mL with TSAT below 25% (2D)|Start an ESA on dialysis (KDIGO 2026)::Hb at or below 9.0 to 10.0 g/dL (2D)|Hb ceiling for adults on an ESA (KDIGO 2026)::Keep Hb below 11.5 g/dL (1D)|Withhold routine iron (KDIGO 2026)::Ferritin above 700 ng/mL or TSAT &ge;40% (practice point)}}
<p>Most anemia in CKD is a mix of too little erythropoietin and too little usable iron, and it responds to patient, stepwise correction of both. A few patients are anemic because they are bleeding, have a marrow or blood disease, or have a deficiency the kidneys did not cause. Your work is to find those first, give iron when the numbers and the patient call for it, use ESAs to avoid transfusion rather than to chase a normal hemoglobin, and remember that a hemoglobin value is a surrogate, not an outcome the patient feels.</p>
""",
    "case": {"title": "The ward consult on a Thursday", "html": """
<p>Thursday, 10 a.m., medical ward of a tertiary hospital in Quezon City. Mrs. Corazon Villanueva, 61, a retired market vendor from Novaliches, has type 2 diabetes and CKD G4 with an estimated glomerular filtration rate (eGFR) of 22 mL/min/1.73 m&sup2;. She was admitted last night for breathlessness on climbing the stairs to her apartment and swelling of both ankles. She takes losartan, insulin, and a ferrous sulfate tablet she buys from the botika &ldquo;when there is money.&rdquo; For her knees she takes mefenamic acid most days. For two weeks her stools have been darker than usual.</p>
<p>Her Hb is 8.1 g/dL, mean corpuscular volume (MCV) 78 fL, platelets normal, ferritin 90 ng/mL and TSAT 14%. No reticulocyte count was sent. Her son, an overseas Filipino worker (OFW) in Dubai, has asked about donating a kidney to her. The admitting resident, Dr. Paolo Mendoza, wants to transfuse two units tonight and &ldquo;start EPO so she can go home.&rdquo; Her daughter has already been told to find two blood donors for the blood bank.</p>
""", "questions": ["What must be done before anyone gives blood, iron or an ESA, and which correctable causes do you see?",
                  "Does she meet a KDIGO 2026 threshold for iron, and would you give it by mouth or intravenously?",
                  "Does she need a transfusion tonight, and when would an ESA or a HIF-PHI enter the plan?"]},
    "sections": [
        ("why", "Why CKD causes anemia", "Why the kidney makes people anemic: four linked failures", """
<p>A healthy adult replaces about one percent of red cell (RBC)s each day. The marrow keeps pace because the kidney adjusts the order and the gut and macrophages release enough iron. In CKD this loop breaks at four points, and each points to a different action at the bedside.[[ntr14_3]]</p>
<p>First, erythropoietin falls short. The level in a patient with CKD may be within the laboratory&rsquo;s normal range, yet far too low for the degree of anemia. That is a relative deficiency, and it is the reason a normal erythropoietin result does not exclude renal anemia. Second, iron is locked away. Hepcidin rises with inflammation and with falling kidney clearance. It blocks the iron exporter ferroportin, so gut absorption falls and iron stays trapped in macrophages. The patient may have stored iron and still be unable to use it, which we call functional iron deficiency. Third, iron is lost. Every hemodialysis session leaves blood in the dialyzer and lines, every admission brings phlebotomy, and uremic platelets and pain tablets make gut bleeding easier. Fourth, red cells live a shorter time in a uremic environment, and other contributors such as severe hyperparathyroidism and deficiency of vitamin B12 or folate add to the problem.[[ntr14_3]]</p>
{{fig:ntr14_a}}
<div class="table-wrap"><table>
<thead><tr><th>Failure</th><th>What drives it</th><th>What you see</th><th>What it changes for you</th></tr></thead>
<tbody>
<tr><td>Too little erythropoietin</td><td>Scarred peritubular oxygen-sensing cells</td><td>Normocytic anemia, low reticulocyte response, worse as eGFR falls</td><td>The reason ESAs and HIF-PHIs work</td></tr>
<tr><td>Iron locked away (functional deficiency)</td><td>Hepcidin from inflammation and low clearance</td><td>Ferritin normal or high, TSAT low</td><td>Oral iron is poorly absorbed; intravenous iron bypasses the gut</td></tr>
<tr><td>Iron lost (absolute deficiency)</td><td>Gut bleeding, dialysis circuit, phlebotomy, menstruation</td><td>Ferritin low, TSAT low, MCV falling</td><td>Look for the bleeding source before you replace</td></tr>
<tr><td>Shorter red cell survival and other causes</td><td>Uremia, hemolysis, hyperparathyroidism, deficiencies, marrow disease</td><td>Anemia out of proportion to the eGFR, abnormal smear or other cell lines</td><td>Expand the work-up; this is not &ldquo;just the kidneys&rdquo;</td></tr>
</tbody></table></div>
<p>The proportion matters. Anemia that is severe while the eGFR is still well preserved, anemia with a low platelet or white cell count, or a microcytic picture with a ferritin far below 100 ng/mL should each make you suspect a second process. The kidney explains the anemia only when the anemia fits the kidney.</p>
<p>In the Philippines, add what the region brings. Ask about hookworm and other intestinal parasites in a patient from a farming area, malaria in a patient from an endemic province such as Palawan, and thalassemia trait in a microcytic patient whose iron stores are normal or whose relatives have &ldquo;always been pale.&rdquo; Ask about herbal products and pain tablets bought without prescription; mefenamic acid and other nonsteroidal anti-inflammatory drugs (NSAIDs) cause gut bleeding as well as kidney injury.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>Children with CKD use age-specific Hb thresholds, and anemia matters for growth, school performance and heart size as well as energy. KDIGO 2026 groups children with adults who are not on dialysis when it advises choosing the Hb at which to start an ESA by symptoms, expected benefit and risk (2D), and it publishes a separate illustration for children.[[ntr14_8]][[ntr14_1]] Transfusion carries the same allosensitization cost for a child who will one day need a kidney. See <a href="attending-pediatric-nephrologist-18-ckd-complications.html">Attending Pediatric Nephrologist, Module 18</a>.</div>
{{key:Before you call it renal anemia, ask which of the four failures is present: too little erythropoietin, iron locked away, iron lost, or a second cause. Each one changes what you do next.}}
"""),
        ("workup", "Work-up", "The work-up: what to send, how often, and how to read it", """
<p>KDIGO 2026 asks you to test for anemia in CKD at referral, regularly during follow-up, and whenever symptoms suggest it. The first test set is a complete blood count (CBC), reticulocytes with the reticulocyte production index (RPI), ferritin and TSAT (practice point).[[ntr14_1]][[ntr14_2]] The minimum frequency rises as kidney function falls: at least yearly in CKD G3, twice a year in G4, and every three months in G5 and on dialysis (practice point).[[ntr14_1]]</p>
<p>The intern&rsquo;s job is concrete. Draw the iron studies before the first iron tablet or infusion in hospital, or the numbers will mislead everyone for weeks. Note the date of the last transfusion; transfused cells change the MCV, the reticulocyte count and the ferritin. Ask about black or bloody stools, heavy menses, nosebleeds, aspirin, NSAIDs and anticoagulants, and record them in the history, not just the order sheet.</p>
<h3>Reading ferritin and TSAT together</h3>
<p>Ferritin reflects stored iron, but it is also an acute-phase protein. Infection, inflammation, liver disease and malignancy push it up. TSAT reflects iron in transit to the marrow, and it falls quickly when supply cannot meet demand. Neither alone tells the whole story, which is why the guideline thresholds always pair them.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pattern</th><th>Likely meaning</th><th>Next step for the resident</th></tr></thead>
<tbody>
<tr><td>Ferritin low, TSAT low, MCV falling</td><td>Absolute iron deficiency</td><td>Look for blood loss; replace iron</td></tr>
<tr><td>Ferritin normal or high, TSAT low</td><td>Functional deficiency, inflammation, or both</td><td>Look for infection and inflammation; consider intravenous iron if thresholds are met</td></tr>
<tr><td>Ferritin and TSAT adequate, reticulocytes low</td><td>Erythropoietin deficiency is likely</td><td>Correct other causes, then consider an ESA</td></tr>
<tr><td>Reticulocytes high</td><td>Bleeding or hemolysis</td><td>Smear, lactate dehydrogenase, haptoglobin, bilirubin; look for the source</td></tr>
<tr><td>Macrocytosis, or other cell lines low</td><td>Deficiency, drug effect, liver disease, marrow disease</td><td>B12, folate, liver tests, smear; consider hematology</td></tr>
</tbody></table></div>
<p>When the first set does not explain the anemia, KDIGO lists an expanded panel: blood smear, haptoglobin, lactate dehydrogenase, C-reactive protein, vitamin B12, folate, liver tests, serum protein electrophoresis and free light chains, thyroid-stimulating hormone, parathyroid hormone and fecal occult blood (practice point).[[ntr14_1]] When iron deficiency has no clear explanation, the guideline asks you to consider evaluation for blood loss with referral to the right specialist (practice point).[[ntr14_1]] In practice, that means asking the gastroenterology service about endoscopy, especially in an older adult, in anyone with dark stools, and in anyone on an NSAID.</p>
{{formula:<strong>How the reticulocyte production index works (arithmetic, not a target).</strong> RPI = reticulocyte % &times; (patient hematocrit &divide; 45) &divide; maturation factor. The correction removes the false rise caused by fewer red cells, and the maturation factor accounts for reticulocytes released early in severe anemia. An RPI below 2 in an anemic patient means the marrow is not responding as it should.}}
<p>The Philippine reality is that a CBC is cheap and a full iron panel is not, and many families pay for laboratory tests out of pocket. If you must choose, the CBC with indices, a reticulocyte count, ferritin and TSAT answer most first questions. Write down why each extra test is needed; a family will often find the money for a test they understand.</p>
{{call:Stop and call the attending nephrologist when <ul><li>Hb has fallen 2 g/dL or more since the last result without an obvious explanation;</li><li>there is melena, hematemesis, fresh rectal bleeding or a falling blood pressure;</li><li>the platelet or white cell count is also low;</li><li>the patient has chest pain, breathlessness at rest or confusion with the anemia.</li></ul>Do this per unit protocol, but always ask the attending nephrologist for guidance.}}
{{key:Draw the iron studies before the first dose of iron or the first unit of blood. Numbers taken after either one mislead the next three doctors.}}
"""),
        ("iron", "Iron", "Iron: when the thresholds say yes, and by which route", """
<p>Iron comes first because an ESA cannot build red cells without it, and because correcting iron deficiency alone raises Hb in some patients. KDIGO 2026 lists iron deficiency among the correctable causes to address before starting an ESA or a HIF-PHI (practice point).[[ntr14_1]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Population</th><th>KDIGO 2026 statement</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>Hemodialysis</td><td>Start iron if ferritin &le;500 ng/mL and TSAT &le;30%</td><td>2D</td></tr>
<tr><td>Hemodialysis, route</td><td>Intravenous rather than oral iron when starting</td><td>2D</td></tr>
<tr><td>Hemodialysis, approach</td><td>Give intravenous iron proactively to keep iron status stable</td><td>Practice point</td></tr>
<tr><td>Not on dialysis, or on peritoneal dialysis</td><td>Start iron if ferritin below 100 ng/mL with TSAT below 40%, or ferritin 100 to 300 ng/mL with TSAT below 25%</td><td>2D</td></tr>
<tr><td>Not on hemodialysis, route</td><td>Oral or intravenous, chosen by preference, severity, efficacy, tolerability, availability and cost</td><td>2D</td></tr>
<tr><td>Everyone treated with iron</td><td>Reasonable to withhold routine iron if ferritin is above 700 ng/mL or TSAT is 40% or higher</td><td>Practice point</td></tr>
<tr><td>Profound iron deficiency without anemia</td><td>Ferritin below 30 ng/mL and TSAT below 20%: consider oral or intravenous iron</td><td>Practice point</td></tr>
</tbody></table></div>
<p>These statements come from the guideline and its executive summary.[[ntr14_1]][[ntr14_2]] Notice the grades. Every iron threshold is 2D: a weak suggestion on very low certainty evidence. The trials that informed them used these cut points as entry criteria; none tested the thresholds against each other for outcomes patients feel. Treat them as sensible boundaries, not as proof.</p>
<h3>Monitoring and safety</h3>
<p>Test Hb, ferritin and TSAT about every three months in patients not on dialysis or on peritoneal dialysis, and every one to three months on hemodialysis (practice points). Switch from oral to intravenous iron if oral iron fails after one to three months or is not tolerated, and consider pausing iron during a systemic infection (practice points). Give intravenous iron only where an acute reaction can be managed; routine test doses and premedication are usually not needed (practice points).[[ntr14_1]] The doses come from your unit formulary and the label, not from memory.</p>
<h3>The evidence behind proactive intravenous iron in hemodialysis</h3>
<p>PIVOTAL randomized 2,141 adults starting maintenance hemodialysis in the United Kingdom to a proactive high-dose intravenous iron sucrose strategy, held only when ferritin was above 700 &micro;g/L or TSAT was 40% or more, or to a reactive low-dose strategy triggered by ferritin below 200 &micro;g/L or TSAT below 20%. Over a median of 2.1 years, the composite of nonfatal myocardial infarction, nonfatal stroke, heart failure admission or death occurred in 29.3% of the proactive group and 32.3% of the reactive group (hazard ratio [HR] 0.85, 95% confidence interval 0.73 to 1.00). That is about 3 fewer events per 100 patients over two years, a number needed to treat (NNT) of roughly 33. The proactive group needed about a fifth less ESA, and infection rates did not differ.[[ntr14_6]] This was an open-label randomized controlled trial (RCT) with blinded end-point review, in incident hemodialysis patients. It does not tell you about patients not on dialysis, and its iron ceiling is where the KDIGO practice point to withhold iron comes from.</p>
<p>For patients not on dialysis, trials comparing intravenous with oral iron showed modest differences in Hb, which is a surrogate. KDIGO therefore leaves the route to shared choice (2D).[[ntr14_1]] In the Philippines that choice is shaped by money and travel. Oral iron is cheap and taken at home; it causes constipation and abdominal upset, and absorption is poor when hepcidin is high. Intravenous iron needs a facility visit and a trained nurse, but one or a few visits may replace months of tablets.</p>
<p>For patients on maintenance hemodialysis, PhilHealth describes its hemodialysis package of PHP 6,350 per session, effective October 9, 2024, as including drugs and medicines for anemia management, and its advisory lists erythropoietin preparations among the minimum standards of the package.[[ntr14_9]][[ntr14_10]] Confirm what your unit actually supplies on the date of service. A patient not yet on dialysis has no such package and usually pays for every vial and tablet.</p>
{{fig:ntr14_c}}
{{key:Pair ferritin with TSAT, name the KDIGO threshold you are using and its 2D grade, and choose the route by setting and patient: intravenous in hemodialysis, a shared choice everywhere else.}}
"""),
        ("esa-hif", "ESA and HIF-PHI", "ESAs and HIF-PHIs: treat to avoid harm, not to reach normal", """
<p>Once iron and other causes are corrected, the remaining anemia is mostly erythropoietin deficiency. ESAs replace the missing signal by injection. HIF-PHIs are tablets that block the enzymes that break down HIF, so the body&rsquo;s own erythropoietin rises and iron handling improves. Both raise Hb. The question that cost nephrology a decade of trials was how high to raise it.</p>
<h3>The trials that set the ceiling</h3>
<p>CHOIR (Correction of Hemoglobin and Outcomes in Renal Insufficiency) randomized 1,432 patients with CKD not on dialysis to epoetin alfa targeting Hb 13.5 g/dL or 11.3 g/dL. Over a median of 16 months, the composite of death, myocardial infarction, heart failure admission or stroke occurred in 125 patients (17.5%) in the high-target group and 97 (13.5%) in the low-target group (HR 1.34, 95% confidence interval 1.03 to 1.74). Quality of life improved equally in both groups.[[ntr14_5]] That is about 4 more events per 100 patients for aiming higher, with nothing gained in how patients felt. CHOIR was open label.</p>
<p>TREAT (Trial to Reduce Cardiovascular Events with Aranesp Therapy) randomized 4,038 patients with type 2 diabetes, CKD not on dialysis and anemia to darbepoetin alfa targeting Hb about 13 g/dL, or to placebo with rescue darbepoetin when Hb fell below 9.0 g/dL. Death or a cardiovascular event did not differ (632 versus 602 patients; HR 1.05). Stroke occurred in 101 patients (5.0%) on darbepoetin and 53 (2.6%) on placebo (HR 1.92). Transfusions were fewer with darbepoetin (297 versus 496 patients, about 15% versus 25%), and fatigue improved only modestly.[[ntr14_4]] Read the trade-off in absolute terms: for every 100 patients treated to the higher target, about 10 avoided a transfusion and about 2 more had a stroke.</p>
{{fig:ntr14_b}}
<h3>What KDIGO 2026 recommends</h3>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>KDIGO 2026 statement</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>Correct first</td><td>Address all correctable causes, including iron deficiency, before an ESA or HIF-PHI</td><td>Practice point</td></tr>
<tr><td>Which agent first</td><td>An ESA rather than a HIF-PHI as first-line treatment</td><td>2D</td></tr>
<tr><td>Start on dialysis</td><td>Start an ESA when Hb is at or below 9.0 to 10.0 g/dL</td><td>2D</td></tr>
<tr><td>Start without dialysis (including transplant recipients and children)</td><td>Choose the starting Hb by symptoms, expected benefit of a higher Hb, and the risks of transfusion and of ESA</td><td>2D</td></tr>
<tr><td>Ceiling in adults</td><td>Keep Hb below 11.5 g/dL while on an ESA</td><td>1D</td></tr>
<tr><td>HIF-PHI safety</td><td>Avoid HIF-PHIs in people at increased risk of adverse events; Hb thresholds for HIF-PHIs are unknown, so use the ESA thresholds</td><td>Practice points</td></tr>
<tr><td>Events on treatment</td><td>Suspend an ESA during acute stroke, access thrombosis or thromboembolism</td><td>Practice point</td></tr>
</tbody></table></div>
<p>These statements are from the guideline and its executive summary.[[ntr14_1]][[ntr14_2]] The ceiling is the guideline&rsquo;s one strong recommendation, yet its certainty is very low. That combination is deliberate: the panel judged that the harms seen in CHOIR and TREAT were serious enough to recommend against higher targets for almost everyone, even though no trial tested 11.5 g/dL itself.</p>
<h3>HIF-PHIs: an alternative, not a default</h3>
<p>ASCEND-ND randomized 3,872 patients with CKD not on dialysis to oral daprodustat or injected darbepoetin alfa. The rise in Hb was similar, and a first major adverse cardiovascular event (MACE) occurred in 19.5% versus 19.2% over a median of 1.9 years (HR 1.03, 95% confidence interval 0.89 to 1.19), which met the trial&rsquo;s noninferiority margin.[[ntr14_7]] Noninferiority with a margin of 1.25 is not proof of equal safety, and longer experience with these agents is still limited. KDIGO keeps ESAs first (2D) and asks you to avoid HIF-PHIs in people with active cancer, recent cardiovascular events or recent thrombosis (practice points).[[ntr14_1]] A tablet may still suit a patient who cannot reach a clinic for injections, after a frank discussion.</p>
<h3>When the Hb will not rise</h3>
<p>ESA hyporesponsiveness means Hb fails to rise, or needs escalating ESA, despite treatment. The guideline asks you first to identify and treat the cause (practice point).[[ntr14_1]] The usual list is iron deficiency, infection or inflammation, ongoing blood loss, hyperparathyroidism, inadequate dialysis, missed injections, and, rarely, antibody-mediated pure red cell aplasia (PRCA), which needs the ESA stopped and hematology involved (practice point).[[ntr14_1]] Do not answer hyporesponsiveness by doubling the dose; in the trials, patients who needed the most ESA did worst.</p>
<p>In the Philippines, the ESA for a patient not on dialysis is usually bought by the family, a few vials at a time. Ask how the vials are stored; most ESAs need refrigeration, and a brownout in a typhoon can spoil them. Ask whether doses were skipped because of money. Missed doses look like hyporesponsiveness in the chart.</p>
{{key:Use an ESA to spare the patient symptoms and transfusions, never to reach a normal Hb. In adults keep Hb below 11.5 g/dL (1D), and treat a poor response by finding its cause.}}
"""),
        ("transfuse", "Transfusion", "Transfusion stewardship: blood is a scarce drug with long effects", """
<p>A transfusion raises Hb within hours and can relieve angina or breathlessness the same night. It also carries volume, potassium, infection risk and, for a future transplant candidate, sensitization to human leukocyte antigens (HLA) that can make a matched kidney harder to find for years. KDIGO 2026 frames transfusion as part of a whole strategy decided with the patient (practice point).[[ntr14_1]]</p>
<div class="table-wrap"><table>
<thead><tr><th>KDIGO 2026 practice point</th><th>What it means on your ward</th></tr></thead>
<tbody>
<tr><td>Base transfusion on symptoms and signs of anemia, not an arbitrary Hb threshold</td><td>Ask what the patient feels and what the heart shows; do not write &ldquo;transfuse if Hb below 8&rdquo; by reflex</td></tr>
<tr><td>In transplant candidates, avoid transfusion when possible</td><td>Ask about transplant plans before every unit; a living donor offer changes the calculus</td></tr>
<tr><td>Transfuse when benefits outweigh risks in acute anemia</td><td>Hemorrhage, unstable coronary disease, urgent surgery</td></tr>
<tr><td>Transfusion may be preferred when an ESA or HIF-PHI is ineffective or harmful</td><td>Recent stroke, active cancer, thrombosis</td></tr>
<tr><td>Use strategies that reduce transfusion</td><td>Fewer and smaller blood draws, continue ESA and iron in hospital, follow Hb trends</td></tr>
</tbody></table></div>
<p>These practice points are from the guideline.[[ntr14_1]] There is no Hb threshold recommendation in the chapter: the panel did not find evidence to set one for people with CKD.</p>
<p>The trials remind you that preventing transfusion is a real benefit. In TREAT, about one in four patients on placebo was transfused, against about one in seven on darbepoetin.[[ntr14_4]] The same trial showed the price of chasing a high Hb. The fellow holds both facts and helps the patient choose.</p>
<h3>The Philippine blood bank and the family</h3>
<p>Many Philippine hospitals ask the family to bring replacement donors before or after a transfusion. A daughter who spends a day recruiting donors for a unit that was not needed has lost wages and goodwill, and the blood bank has lost a unit someone else needed. Before you send the family out, write down the reason for the transfusion. If the patient is stable, symptomatic only on exertion and has a correctable cause, treat the cause first and reassess in the morning.</p>
<p>Fewer blood draws matter more than most residents think. Combine tests, use pediatric tubes where your laboratory accepts them, and stop daily CBCs once the trend is clear.</p>
{{call:Stop and call the attending nephrologist when a patient with CKD is bleeding actively, has chest pain or breathlessness at rest with anemia, has a fall in Hb that changes your plan, or is a transplant candidate and a transfusion is being considered. Do this per unit protocol, but always ask the attending nephrologist for guidance.}}
{{key:Before every unit, write three things in the chart: the symptom or sign that justifies it, whether the patient is a transplant candidate, and what you are doing about the cause.}}
"""),
    ],
    "debrief": ["""
<p><strong>Before anything is given.</strong> Send a reticulocyte count and a blood smear now, before the first unit or the first iron dose, and add vitamin B12, folate and fecal occult blood. Ask the intern to document the dark stools, the daily mefenamic acid and any past transfusions. Stop the NSAID. Her picture is not simple renal anemia: microcytosis, a ferritin of 90 ng/mL and two weeks of dark stools on an NSAID point to gut blood loss on top of erythropoietin deficiency. Ask gastroenterology about endoscopy. Her ankle swelling and breathlessness also need a volume assessment, because a fluid-overloaded heart makes anemia feel worse.</p>
""", """
<p><strong>Iron.</strong> She is not on dialysis, so the KDIGO 2026 threshold is ferritin below 100 ng/mL with TSAT below 40%, or ferritin 100 to 300 ng/mL with TSAT below 25% (2D). With ferritin 90 ng/mL and TSAT 14% she meets it clearly. Her irregular oral iron failed, possibly because of cost, side effects and hepcidin, and she may be losing blood faster than tablets can replace it. Intravenous iron in hospital, given where a reaction can be managed and once infection is excluded, is a reasonable shared choice. Write the doses from the formulary. Recheck Hb, ferritin and TSAT in about three months.</p>
""", """
<p><strong>Transfusion and ESA.</strong> She is breathless on stairs, not at rest, has no chest pain, and her blood pressure is stable. Transfusion tonight is not clearly needed and carries a real cost: her son&rsquo;s offer of a kidney makes her a transplant candidate, and KDIGO advises avoiding transfusion in candidates when possible. Transfuse if she bleeds actively, becomes unstable or develops symptoms at rest. Tell her daughter to pause the donor search until the team decides. An ESA comes after iron and the bleeding source are dealt with. If Hb stays low and she has symptoms, an ESA is the first choice over a HIF-PHI (2D), with Hb kept below 11.5 g/dL (1D). Discuss cost honestly; outside the dialysis package her family will pay for each vial.</p>
"""],
    "skills": {"title": "Anemia work-up and iron decision in CKD",
               "intro": "Complete with a preceptor on two patients with CKD and anemia, on the ward or in clinic. Sign-off is local.",
               "items": [
                   ("Takes a focused anemia history: bleeding, NSAIDs and anticoagulants, diet, menses, past transfusions, and transplant plans.", False),
                   ("Orders or collects the KDIGO first test set (CBC, reticulocytes, ferritin, TSAT) before any iron or blood is given.", False),
                   ("Interprets ferritin and TSAT together and states whether the patient meets a KDIGO 2026 iron threshold, with its grade.", False),
                   ("Lists the correctable causes found and the plan for each before an ESA is discussed.", False),
                   ("States the Hb ceiling for an adult on an ESA, its grade, and the trials behind it, in plain words a patient can follow.", False),
                   ("Writes a transfusion justification that names the symptom, the transplant status and the plan for the cause.", False),
               ],
               "placement": "Medical ward, renal clinic or hemodialysis unit"},
    "quiz": [
        ("An intern is asked to send iron studies for a patient with CKD who is about to receive a first transfusion tonight. What should the intern do?",
         ["Draw the blood for ferritin and TSAT before the transfusion starts",
          "Send the iron studies tomorrow morning after the transfusion",
          "Skip the iron studies because the transfusion will correct the anemia",
          "Send only the ferritin, because TSAT adds nothing"], 0,
         "Transfused red cells change the indices, reticulocytes and ferritin, so samples drawn afterward mislead. Sending only ferritin fails because ferritin is an acute-phase protein and KDIGO thresholds always pair it with TSAT."),
        ("A man with CKD G3b not on dialysis has Hb 10.2 g/dL, ferritin 180 ng/mL and TSAT 19%. By KDIGO 2026, what is the iron decision?",
         ["No iron, because ferritin is above 100 ng/mL",
          "Iron is suggested, because ferritin is 100 to 300 ng/mL with TSAT below 25% (2D)",
          "Iron only if he starts hemodialysis",
          "Iron only after an ESA is started"], 1,
         "For people not on dialysis or on peritoneal dialysis, KDIGO 2026 suggests iron if ferritin is below 100 ng/mL with TSAT below 40%, or ferritin 100 to 300 ng/mL with TSAT below 25% (2D). The first option applies only the ferritin cut point and ignores the TSAT arm."),
        ("A fellow is asked why KDIGO 2026 recommends keeping Hb below 11.5 g/dL in adults on an ESA. Which answer is most accurate?",
         ["A trial showed that 11.5 g/dL gives the best survival",
          "Higher Hb targets improved quality of life but increased cost",
          "Trials of higher targets (CHOIR, TREAT) showed more cardiovascular events or stroke without a meaningful gain in how patients felt; the recommendation is strong (1D) despite very low certainty",
          "The ceiling applies only to patients with diabetes"], 2,
         "No trial tested 11.5 g/dL itself. CHOIR showed more composite events and TREAT nearly doubled stroke at higher targets, with little or no quality-of-life gain. The second option is wrong because quality of life did not meaningfully improve."),
        ("A 45-year-old woman on maintenance hemodialysis in Cebu has Hb 9.4 g/dL, ferritin 420 ng/mL and TSAT 24% with no infection. What does KDIGO 2026 suggest?",
         ["Start intravenous iron, because ferritin is &le;500 ng/mL and TSAT &le;30% (2D)",
          "No iron, because ferritin is above 300 ng/mL",
          "Oral iron first for three months",
          "Transfuse to Hb 11.5 g/dL"], 0,
         "In hemodialysis, KDIGO 2026 suggests starting iron if ferritin is &le;500 ng/mL and TSAT &le;30% (2D), intravenously rather than orally (2D). The 300 ng/mL cut point applies to patients not on dialysis or on peritoneal dialysis."),
        ("A man with CKD G4 on an ESA has had a falling Hb for three months despite rising doses. What should the resident do first?",
         ["Double the ESA dose",
          "Switch to a HIF-PHI immediately",
          "Look for the cause: iron status, infection or inflammation, blood loss, hyperparathyroidism and missed doses",
          "Stop all anemia treatment"], 2,
         "KDIGO 2026 asks you to identify and treat the causes of hyporesponsiveness first (practice point). Escalating the dose is the trap: in the trials, patients needing the most ESA did worst. A HIF-PHI trial is considered only after causes are addressed."),
    ],
    "terms": [
        ("ASCEND-ND", "Daprodustat versus darbepoetin alfa trial in CKD not on dialysis"),
        ("CBC", "Complete blood count"),
        ("CHOIR", "Correction of Hemoglobin and Outcomes in Renal Insufficiency (trial)"),
        ("CKD", "Chronic kidney disease"),
        ("eGFR", "Estimated glomerular filtration rate"),
        ("ESA", "Erythropoiesis-stimulating agent"),
        ("Hb", "Hemoglobin"),
        ("HIF", "Hypoxia-inducible factor"),
        ("HIF-PHI", "Hypoxia-inducible factor prolyl hydroxylase inhibitor"),
        ("HLA", "Human leukocyte antigen"),
        ("HR", "Hazard ratio"),
        ("KDIGO", "Kidney Disease: Improving Global Outcomes"),
        ("MACE", "Major adverse cardiovascular event"),
        ("MCV", "Mean corpuscular volume"),
        ("NNT", "Number needed to treat"),
        ("NSAID", "Nonsteroidal anti-inflammatory drug"),
        ("OFW", "Overseas Filipino worker"),
        ("PIVOTAL", "Proactive intravenous iron therapy trial in maintenance hemodialysis"),
        ("PRCA", "Pure red cell aplasia"),
        ("RCT", "Randomized controlled trial"),
        ("RPI", "Reticulocyte production index"),
        ("TREAT", "Trial to Reduce Cardiovascular Events with Aranesp Therapy"),
        ("TSAT", "Transferrin saturation"),
    ],
    "readings": [
        ("anemia-management.html", "Anemia Management in CKD"),
        ("epo-resistant-renal-anemia.html", "EPO-Resistant Renal Anemia"),
        ("attending-nephrologist-10-ckd-complications.html", "Attending Nephrologist, Module 10: CKD complications"),
        ("physician-on-duty-21-blood-and-bone.html", "Physician on Duty, Module 21: Blood and bone"),
    ],
    "calcs": ["calc-iron-status-tsat.html", "calc-reticulocyte-rpi.html", "calc-iron-deficit-ganzoni.html",
              "calc-esa-dose-adjustment.html", "calc-transfusion-hgb.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
