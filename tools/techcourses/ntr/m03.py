# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 03: The renal consultation and diagnostic synthesis.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard.
Goldman 1983, Bowen 2006, Graber 2005, Siew 2012, Starmer 2014, Debelle 2008 and Hoste 2015 checked against PubMed;
KDIGO 2012 AKI definitions and KDIGO 2024 chronicity practice points checked against the guideline texts. No doses.
Fictional case."""

MODULE = {
    "image_alt": "A nephrology fellow and an internal medicine resident review a creatinine timeline drawn on paper at a ward station at night, while a patient&rsquo;s wife shows them old laboratory slips on her phone.",
    "objectives": [
        "<strong>Intern:</strong> Present a focused renal history, examination and timeline of creatinine, urine output and exposures, including herbal and over-the-counter products, in under three minutes.",
        "<strong>Resident:</strong> Write a one-sentence problem representation and a prioritized differential with an investigation plan in which each test would change the next decision.",
        "<strong>Fellow:</strong> Deliver a consultation that answers the referring team&rsquo;s question, states urgency and uncertainty, gives contingency plans and names who follows up, by direct conversation as well as in the note.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; turning a referral into a plan</span>An <strong>intern</strong> owns the data: the old creatinines, the urine output, every medicine and remedy, the examination, laid out on a timeline. A <strong>resident</strong> owns the synthesis: what the problem is, what it could be, and which test will decide between the possibilities. A <strong>fellow</strong> owns the answer to the referring team: what to do now, what to watch, when to call, and who comes back tomorrow.</div>
{{plain:Think of a barangay health worker called to a house because &ldquo;Lola is not well.&rdquo; Before she does anything, she asks who called and why, checks whether Lola is breathing and talking, asks when this started and what changed, and looks at the medicine bag on the table. Only then does she decide whether to give advice, return tomorrow, or send for the ambulance.}}
<p>The picture has a limit. The health worker sees one person in one room. A renal consultation pulls data from several places and times: another hospital&rsquo;s laboratory, a clinic slip on a daughter&rsquo;s phone, a nurse&rsquo;s urine chart, a pharmacy record, a market remedy. Kidney problems are told in time. A creatinine of 3.4 mg/dL means something different if it was 1.0 mg/dL yesterday, 3.2 mg/dL a year ago, or never measured. The consultant&rsquo;s first job is to rebuild that time course, because the time course is most of the diagnosis.</p>
<p>Diagnostic error in medicine is common and has a recognizable shape. In a review of 100 diagnostic errors involving internists, cognitive factors contributed in 74% and system factors in 65%, and the single most common cognitive cause was premature closure: stopping at the first explanation without considering the rest.[[ntr03_3]] A structured consultation is a defense against both.</p>
{{cards:Key numbers|AKI (KDIGO 2012)::Creatinine rise &ge;0.3 mg/dL within 48 hours, or &ge;1.5 times baseline within 7 days, or urine output &lt;0.5 mL/kg/h for 6 hours (ungraded definition)|Chronic kidney disease (KDIGO 2024)::Abnormal kidney structure or function for at least 3 months; do not assume chronicity from a single abnormal value (practice points)|Best baseline creatinine (Siew 2012)::Mean outpatient value 7 to 365 days before admission agreed best with nephrologists (intraclass correlation 0.91)|Diagnostic error (Graber 2005, 100 cases)::Cognitive factors in 74%; premature closure the most common}}
<p>Most renal referrals are for a rising creatinine in a patient who is otherwise stable. A few hide an emergency: potassium high enough to stop the heart, fluid in the lungs, a uremic patient who is drowsy, an obstructed kidney. Your work is to find the emergency first, then to build the timeline, name the problem in one sentence, and leave the referring team with a plan they can act on at 3 a.m. without you.</p>
""",
    "case": {"title": "Creatinine high, pls see", "html": """
<p>Tuesday, 2:05 a.m., a tertiary hospital in Manila. The medicine resident on call, Dr. Kevin Ocampo, receives a referral through the hospital&rsquo;s messaging system: &ldquo;Bed 22, 59M, CAP, crea 3.4, pls see. Thanks Doc.&rdquo; Nothing else.</p>
<p>At the bedside he finds Mr. Danilo Ramos, a jeepney operator with type 2 diabetes, admitted 30 hours ago for community-acquired pneumonia (CAP). He is awake, breathing 22 times a minute, blood pressure 104/62 mm Hg, pulse 108. The chart has no earlier creatinine. The nurse has not recorded urine output since admission; the urinal holds about 150 mL. His wife, Mrs. Elena Ramos, says he took &ldquo;two or three&rdquo; pain tablets a day for fever for five days before admission, and that he has taken herbal capsules &ldquo;for the kidneys&rdquo; bought online since last year. He had a contrast computed tomography (CT) scan of the chest at a clinic in Caloocan four days ago. Tonight&rsquo;s potassium is 5.9 mmol/L. Her phone has a photo of a laboratory slip from a company physical in March: creatinine 1.1 mg/dL.</p>
""", "questions": [
        "What is the real question, and how urgent is it tonight?",
        "What is the timeline, and what is your one-sentence problem representation and differential?",
        "What do you write, whom do you call, and who follows up?"]},
    "sections": [
        ("question", "Question and stability", "Establish the question and the patient&rsquo;s stability", """
<p>Every consultation answers a question, and the first error is to answer the wrong one. Goldman and colleagues set out ten principles for effective consultation in 1983: determine the question being asked, establish the urgency, gather primary data yourself, communicate briefly, make specific recommendations, provide contingency plans, understand your own role, teach, talk directly to the requesting physician, and follow up.[[ntr03_1]] These are expert opinion, not trial results, but four decades of consultation practice still rest on them.</p>
<p>&ldquo;Creatinine high, pls see&rdquo; is not a question. Behind it may be &ldquo;is this dangerous tonight?&rdquo;, &ldquo;can we give contrast?&rdquo;, &ldquo;how do we dose the antibiotic?&rdquo;, or &ldquo;does he need dialysis?&rdquo; Call the referring physician, or ask the first person you meet on the ward, and get the real question before you write anything.</p>
<h3>Stability first</h3>
<p>Before history, before timeline, decide whether anything will kill the patient in the next hours. The kidney fails in four ways that can: potassium, fluid, acid and uremic toxins.</p>
<div class="table-wrap"><table>
<thead><tr><th>Threat</th><th>What you check in the first minutes</th><th>What makes it urgent</th></tr></thead>
<tbody>
<tr><td>Potassium</td><td>Latest value and time, an electrocardiogram (ECG), drugs that raise it</td><td>A high value with ECG changes, or a rising value with poor urine output</td></tr>
<tr><td>Fluid</td><td>Breathing rate, oxygen saturation, crackles, neck veins, recent balance</td><td>Pulmonary edema not responding to diuretics, rising oxygen need</td></tr>
<tr><td>Acid</td><td>Bicarbonate or blood gas, breathing pattern</td><td>Severe acidemia, Kussmaul breathing, a toxic ingestion</td></tr>
<tr><td>Uremia</td><td>Consciousness, asterixis, pericardial rub, bleeding</td><td>Encephalopathy, pericarditis, uremic bleeding</td></tr>
<tr><td>Obstruction</td><td>Bladder size, catheter, history of prostate disease or pelvic tumor</td><td>A palpable bladder or anuria: obstruction is quick to fix and easy to miss</td></tr>
<tr><td>Circulation</td><td>Blood pressure, pulse, perfusion, lactate if sepsis</td><td>Shock: the kidney will not recover until perfusion does</td></tr>
</tbody></table></div>
<p>For Mr. Ramos, the potassium of 5.9 mmol/L needs an ECG now and a repeat value, the tachycardia and soft pressure need attention to his sepsis and volume, and the urinal needs emptying and a bladder scan or catheter question answered. None of this waits for the timeline.</p>
{{call:Stop and call the attending nephrologist, per unit protocol, but always ask the attending nephrologist for guidance, when you find:<ul><li>a high potassium with ECG changes, or one that keeps rising;</li><li>pulmonary edema or rising oxygen need in a patient with poor urine output;</li><li>severe acidemia, a suspected toxic ingestion, or uremic encephalopathy or pericarditis;</li><li>anuria, or a patient for whom the referring team is asking about urgent dialysis.</li></ul>Start the hospital&rsquo;s emergency protocols while you call.}}
{{key:Find the real question and rule out the four killers (potassium, fluid, acid, uremia) and obstruction before you take the history.}}
"""),
        ("timeline", "The timeline", "Build the creatinine, urine and exposure timeline", """
<p>Kidney diseases are distinguished mostly by their tempo. The same creatinine can belong to AKI over hours, acute kidney disease over weeks, or chronic kidney disease (CKD) over years, and the plan differs in each. A timeline lays the evidence side by side so the tempo shows itself.</p>
{{fig:ntr03_a}}
<h3>Find the baseline</h3>
<p>The baseline creatinine defines AKI. Kidney Disease: Improving Global Outcomes (KDIGO) 2012 defines AKI as a rise of at least 0.3 mg/dL within 48 hours, a rise to at least 1.5 times baseline known or presumed to have occurred within the prior 7 days, or urine output below 0.5 mL/kg per hour for 6 hours; these definitions are not graded.[[ntr03_6]] Pick the wrong baseline and you miss AKI or invent it. Siew and colleagues compared common ways of choosing a baseline with a reference adjudicated by nephrologists in 379 hospitalized patients. The mean of outpatient creatinines measured 7 to 365 days before admission agreed best (intraclass correlation 0.91), better than the most recent or the lowest value; adding older values or values from the week before admission did not help.[[ntr03_5]] This was a single-center study, but it supports a practical rule: use the average of the last year&rsquo;s stable outpatient values when you have them.</p>
<p>In the Philippines the baseline is often outside the chart: a company physical, a clinic slip, a photo on a relative&rsquo;s phone, a laboratory in another city. Ask for it every time. When there is none, say so, and do not assume CKD from a single high value. KDIGO 2024 states that chronicity needs at least three months of evidence and should not be assumed from one abnormal estimated glomerular filtration rate (eGFR) or albuminuria result; small kidneys on ultrasound, a past result or a long history can supply that proof.[[ntr03_7]]</p>
<h3>Lay out the three lines</h3>
<div class="table-wrap"><table>
<thead><tr><th>Line</th><th>What to collect</th><th>Common gap</th></tr></thead>
<tbody>
<tr><td>Creatinine and other laboratory values</td><td>Every creatinine with its date and place; potassium, bicarbonate, urinalysis, hemoglobin</td><td>Results from another facility not in the chart</td></tr>
<tr><td>Urine output and weight</td><td>Hourly or shift totals, catheter status, daily weight, fluid in and out</td><td>Output &ldquo;not recorded&rdquo; on the first night</td></tr>
<tr><td>Exposures and events</td><td>Hypotension, sepsis, surgery, contrast, every drug started or stopped, over-the-counter painkillers, herbal and &ldquo;kidney cleanse&rdquo; products, vomiting, diarrhea, poor intake</td><td>Products the family does not think of as medicines</td></tr>
</tbody></table></div>
<h3>Ask about every product</h3>
<p>Ask the question in a way that gets an answer: &ldquo;What tablets, capsules, teas or powders has he taken, even ones from the market, online or a friend?&rdquo; Bring the bags if possible. Nonsteroidal anti-inflammatory drugs (NSAIDs) sold without prescription for fever and pain are common. Herbal products sold for the kidneys can harm them: aristolochic acid nephropathy, a progressive interstitial fibrosis often followed by urothelial cancer, was first described after slimming pills containing a Chinese herb and has been reported worldwide, with Asian traditional medicine a recognized risk because of substitution of herbs.[[ntr03_8]] Most remedies you meet will be unknown mixtures; record the name, the seller and a photo of the label, and include them in the differential.</p>
<p>Fill in what you can, then mark the gaps. A timeline with honest gaps (&ldquo;no creatinine between March and admission&rdquo;) is more useful than one that pretends.</p>
{{key:Put every creatinine, every urine output and every exposure on one dated line. The tempo tells you whether this is acute, subacute or chronic.}}
"""),
        ("problem", "Problem representation", "Problem representation and the prioritized differential", """
<p>A problem representation is a one-sentence summary that names the time course, the key features and the syndrome in abstract terms. Bowen described it as the step that turns a list of findings into something you can match against illness scripts, the patterns of disease that experienced clinicians carry in memory.[[ntr03_2]] It is the hinge of diagnostic reasoning: a vague representation leads to a vague differential, and a sharp one narrows the search.</p>
{{fig:ntr03_b}}
<div class="table-wrap"><table>
<thead><tr><th>Weak version</th><th>Problem representation</th><th>What it changes</th></tr></thead>
<tbody>
<tr><td>&ldquo;59M, CAP, crea 3.4.&rdquo;</td><td>&ldquo;A 59-year-old man with diabetes and sepsis from pneumonia has AKI over days, from a baseline of 1.1 mg/dL to 3.4 mg/dL, with low urine output and potassium 5.9 mmol/L, after NSAIDs, a contrast scan and an unidentified herbal product.&rdquo;</td><td>Names the tempo (days), the syndrome (oliguric AKI with hyperkalemia), the context (sepsis, diabetes) and the exposures</td></tr>
<tr><td>&ldquo;Renal failure, for hemodialysis (HD)?&rdquo;</td><td>&ldquo;A woman with long-standing hypertension has creatinine 6.0 mg/dL with small echogenic kidneys and no acute symptoms.&rdquo;</td><td>Points toward advanced CKD and planning, not an emergency</td></tr>
</tbody></table></div>
<h3>From representation to differential</h3>
<p>Sort the causes by where the problem sits, then rank them by probability and by danger. The classic split into perfusion (prerenal), intrinsic kidney disease and obstruction still works, as long as you remember that sepsis can act through all three and that more than one cause is common.</p>
<div class="table-wrap"><table>
<thead><tr><th>Compartment</th><th>Causes that fit Mr. Ramos</th><th>The test that would change the next decision</th></tr></thead>
<tbody>
<tr><td>Perfusion</td><td>Sepsis with low effective volume, NSAIDs blocking afferent vasodilation</td><td>Response of urine output and creatinine to restoring perfusion; urine sodium if no diuretic</td></tr>
<tr><td>Tubule</td><td>Acute tubular injury from sepsis, NSAIDs or contrast; pigment if rhabdomyolysis</td><td>Urine sediment for muddy brown casts and tubular cells (Module 4); creatine kinase if muscle pain</td></tr>
<tr><td>Interstitium</td><td>Drug-induced interstitial nephritis from NSAIDs, antibiotics or herbal products</td><td>Sediment for white cells and white cell casts; history of rash or fever</td></tr>
<tr><td>Glomerulus or vessels</td><td>Rapidly progressive glomerulonephritis is less likely but dangerous</td><td>Blood and protein on urinalysis, dysmorphic red cells</td></tr>
<tr><td>Obstruction</td><td>Prostate enlargement, clot</td><td>Bladder scan or catheter; kidney ultrasound</td></tr>
</tbody></table></div>
<p>Rank each test by whether it changes the next decision. A urinalysis, a sediment, a bladder scan and a kidney ultrasound change decisions tonight or tomorrow. A long panel of serologies sent at 2 a.m. for every patient rarely does, costs the family money, and delays the tests that matter.</p>
<h3>Guard against premature closure</h3>
<p>In Graber&rsquo;s series, premature closure was the most common cognitive error, and faulty knowledge was uncommon.[[ntr03_3]] The fix is a habit, not more reading: once you have a leading diagnosis, ask &ldquo;what else could this be, and what finding would prove me wrong?&rdquo; For Mr. Ramos, &ldquo;septic AKI&rdquo; is likely, but the herbal product, the NSAIDs and a possible obstruction each need a deliberate check.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>The renal consult in a child starts from height, weight and age-specific norms, not adult numbers: creatinine is lower, eGFR uses height-based equations, and urine output is judged per kilogram. Dehydration from gastroenteritis, congenital anomalies of the kidney and urinary tract, and post-infectious glomerulonephritis dominate the differential, and the parents are both the historians and the decision-makers. See <a href="attending-pediatric-nephrologist-01-taking-responsibility.html">Attending Pediatric Nephrologist, Module 1</a>.</div>
{{key:Say the problem in one sentence with tempo, syndrome and context, then rank causes by probability and danger, and order only tests that will change the next decision.}}
"""),
        ("consult-note", "Note, call, handoff", "The note, the call and the handoff", """
<p>A consultation that is correct but not received is a failure. The plan must reach the person who will act on it, in a form they can act on, with clear signals for when to call back.</p>
<h3>The note</h3>
<p>Lead with the answer. The referring team should find the recommendations in the first lines, not after a page of history. Then give the reasoning briefly, the uncertainties, and the contingency plan: what to do if the potassium rises, if the urine output stays low, if the patient becomes breathless.</p>
<div class="table-wrap"><table>
<thead><tr><th>Part of the note</th><th>What it contains</th><th>Example line for Mr. Ramos</th></tr></thead>
<tbody>
<tr><td>Question and answer</td><td>The question asked and your short answer</td><td>&ldquo;Asked: cause and management of raised creatinine. Answer: oliguric AKI stage 2 to 3 on a baseline of 1.1 mg/dL, likely septic and drug-related; not dialysis tonight if potassium responds.&rdquo;</td></tr>
<tr><td>Problem representation</td><td>One sentence</td><td>As in the previous section</td></tr>
<tr><td>Recommendations</td><td>Numbered, specific, few</td><td>&ldquo;1. ECG now and repeat potassium; treat per hospital hyperkalemia protocol. 2. Stop NSAIDs and the herbal product. 3. Hourly urine output; bladder scan. 4. Urinalysis and sediment; kidney ultrasound in the morning. 5. Review all drugs for kidney dosing with pharmacy.&rdquo;</td></tr>
<tr><td>Contingencies</td><td>If-then triggers with a number to call</td><td>&ldquo;Call the renal fellow if potassium is not falling on repeat, if ECG changes appear, if urine output stays below the agreed threshold for six hours, or if oxygen need rises.&rdquo;</td></tr>
<tr><td>Owner and follow-up</td><td>Who sees the patient next and when</td><td>&ldquo;Renal fellow will review at 8 a.m. rounds; attending informed at 2:40 a.m.&rdquo;</td></tr>
</tbody></table></div>
<h3>The call</h3>
<p>Talk to the requesting physician directly when anything is time-sensitive, which Goldman counted among the ten principles.[[ntr03_1]] A note in a chart that nobody reads until morning rounds does not protect a patient with a potassium of 5.9 mmol/L. Use SBAR (situation, background, assessment, recommendation), read back the critical numbers, and write that the call happened.</p>
<h3>The handoff</h3>
<p>At the end of your duty, hand the patient over in a structure that the next person expects. I-PASS (illness severity, patient summary, action list, situation awareness and contingency planning, synthesis by receiver) was introduced with training and faculty observation in nine hospitals, and medical errors fell from 24.5 to 18.8 per 100 admissions and preventable adverse events from 4.7 to 3.3 per 100 admissions; handoffs took no longer.[[ntr03_4]] The study compared periods before and after the program, so it shows association, not proof. The &ldquo;synthesis by receiver&rdquo; step, in which the next doctor repeats the plan back, catches misunderstandings before they reach the patient.</p>
<h3>Why the follow-up matters</h3>
<p>AKI is not a one-night problem. In the multinational AKI-EPI study of 1,802 intensive care unit (ICU) patients in 97 centers, 57.3% had AKI in the first ICU week, and at hospital discharge 47.7% of those with AKI had an eGFR below 60 mL/min/1.73 m&sup2;, compared with 14.8% of those without.[[ntr03_9]] The study was cross-sectional and observational, so it does not show that AKI caused the lower eGFR, but it shows why someone must own the follow-up after discharge. Name that person and that date in the note. Use a tool such as the CKD progression slope calculator later, when you have serial values over months, to judge the long-term trajectory; the slope of eGFR is a surrogate, not an outcome the patient feels.</p>
<p>In the Philippines the follow-up plan must fit the family&rsquo;s reality: where they live, whether the patient can come back to this hospital, whether laboratory tests can be done near home, and who will pay. A plan to &ldquo;repeat creatinine in one week at the renal clinic&rdquo; fails if the family lives in Bulacan and the clinic is in Manila. Write the nearest workable option.</p>
{{key:Lead with the answer, give specific recommendations and if-then triggers, talk to the team directly when it is urgent, and name the person and date for follow-up.}}
"""),
    ],
    "debrief": ["""
<p><strong>The real question and its urgency.</strong> Dr. Ocampo calls the referring intern and learns the team wants to know whether Mr. Ramos needs dialysis and how to dose his antibiotic. Before answering, he checks stability: the ECG shows peaked T waves, so the hospital&rsquo;s hyperkalemia protocol starts now with the resident on the medical team; he is tachycardic with a soft pressure, so his sepsis and volume need reassessment; his bladder is not distended on scan. He calls the renal fellow because of the ECG changes. The urgent question tonight is the potassium and perfusion, not dialysis.</p>
""", """
<p><strong>Timeline and representation.</strong> March: creatinine 1.1 mg/dL. Five days of over-the-counter NSAIDs before admission, herbal capsules for a year, contrast CT four days ago, 30 hours of sepsis from pneumonia with a soft pressure, creatinine 3.4 mg/dL now (about 3.1 times baseline, KDIGO stage 3 by creatinine if the rise is within 7 days, which the recent normal-range history and acute illness suggest), and little urine. The representation: &ldquo;A 59-year-old man with diabetes and pneumonia-related sepsis has oliguric AKI over days with hyperkalemia, after NSAIDs, contrast and an unidentified herbal product.&rdquo; Differential: septic and NSAID-related perfusion injury and acute tubular injury first; drug-induced interstitial nephritis second; obstruction excluded by scan; glomerulonephritis unlikely but checked by urinalysis.</p>
""", """
<p><strong>Note, call and owner.</strong> The note leads with the answer: oliguric AKI stage 3 by creatinine, no dialysis tonight if the potassium responds, with numbered recommendations (potassium protocol and repeat, stop NSAIDs and the herbal capsules, hourly urine output, urinalysis and sediment, morning ultrasound, kidney dosing of the antibiotic with pharmacy) and if-then triggers. He calls the medical resident to read back the plan and the triggers, the fellow informs the attending nephrologist, and the note names the renal fellow at 8 a.m. rounds as the owner. At discharge, the plan will include a creatinine check near the family&rsquo;s home in Caloocan and a renal clinic visit.</p>
"""],
    "skills": {"title": "Renal consultation",
               "intro": "Complete with a preceptor on the renal consult service. Sign-off is local.",
               "items": [
                   ("Clarifies the referring team&rsquo;s question directly before writing", False),
                   ("Checks potassium, fluid, acid, uremia, obstruction and circulation in the first minutes", False),
                   ("Builds a dated timeline of creatinine, urine output and exposures, including herbal and over-the-counter products", False),
                   ("States a one-sentence problem representation with tempo, syndrome and context", False),
                   ("Writes a consult note that leads with the answer, numbered recommendations, contingencies and a named owner", False),
                   ("Calls the requesting physician for a time-sensitive plan and hands over using I-PASS with read-back", False),
               ],
               "placement": "Renal consult service, medical wards or emergency department"},
    "quiz": [
        ("An intern presents a patient referred for a raised creatinine. Which element of the presentation most helps the team decide whether this is acute kidney injury?",
         ["The full list of past surgeries",
          "A dated baseline creatinine and the urine output since admission",
          "The patient&rsquo;s occupation",
          "The latest hemoglobin"], 1,
         "KDIGO 2012 defines AKI by change from baseline creatinine or by low urine output over time. Without a baseline and output, the team cannot tell AKI from CKD. Other history matters, but not for this decision."),
        ("A resident writes: &ldquo;Female, 70, crea 2.8, for evaluation.&rdquo; Which rewrite is the best problem representation?",
         ["&ldquo;Elderly female with renal failure, rule out everything.&rdquo;",
          "&ldquo;A 70-year-old woman with heart failure has AKI over three days, from 1.2 to 2.8 mg/dL, after a new diuretic and an ACE inhibitor, with low blood pressure and no urinary abnormalities.&rdquo;",
          "&ldquo;Creatinine 2.8 mg/dL, potassium 4.9 mmol/L, sodium 136 mmol/L.&rdquo;",
          "&ldquo;Renal consult requested by the cardiology service.&rdquo;"], 1,
         "A problem representation names tempo, key features, syndrome and context in one sentence. The second option does so and points to a hemodynamic cause; the others are vague, a list of values, or administrative."),
        ("A fellow finishes a consult on a patient with potassium of 6.3 mmol/L at 11 p.m. What best ensures the plan is carried out?",
         ["Write a detailed note and leave it for morning rounds",
          "Write a note that leads with the recommendations and if-then triggers, call the requesting physician to read back the plan, and name who follows up",
          "Send a chat message to the ward",
          "Tell the patient to inform the nurse"], 1,
         "Goldman&rsquo;s principles include specific recommendations, contingency plans and direct communication. A note alone may not be read in time for a dangerous potassium, and a chat message without acknowledgment does not confirm receipt."),
        ("A 45-year-old man has creatinine 4.1 mg/dL at his first visit, with no previous results. Ultrasound shows kidneys of normal size. What is the best statement in the consult note?",
         ["CKD stage 4, chronic",
          "Kidney function is reduced, but chronicity is not established; repeat and trend the creatinine, examine the urine, and look for acute causes",
          "AKI stage 3, confirmed",
          "No conclusion can be drawn, so no tests are needed"], 1,
         "KDIGO 2024 advises not to assume chronicity from a single abnormal value. With no baseline and normal-sized kidneys, the tempo is unknown, so trend the value and look for acute causes before labeling."),
        ("While reviewing an AKI patient, a resident fixes on contrast nephropathy after a CT two days ago. Which step best protects against premature closure?",
         ["Ordering every serology available",
          "Asking what else could cause the picture and what finding would prove the leading diagnosis wrong, then checking the urine sediment, drugs and bladder",
          "Waiting for the creatinine to normalize",
          "Accepting the first diagnosis because contrast is a known cause"], 1,
         "Graber found premature closure the most common cognitive cause of diagnostic error. Deliberately naming alternatives and the finding that would disprove the leading diagnosis is the practical defense; blanket testing adds cost without focus."),
    ],
    "terms": [
        ("ACE", "Angiotensin-converting enzyme"),
        ("AKI", "Acute kidney injury"),
        ("AKI-EPI", "Acute Kidney Injury&ndash;Epidemiologic Prospective Investigation (study)"),
        ("CAP", "Community-acquired pneumonia"),
        ("CKD", "Chronic kidney disease"),
        ("CT", "Computed tomography"),
        ("ECG", "Electrocardiogram"),
        ("eGFR", "Estimated glomerular filtration rate"),
        ("HD", "Hemodialysis"),
        ("ICU", "Intensive care unit"),
        ("I-PASS", "Illness severity, Patient summary, Action list, Situation awareness and contingency planning, Synthesis by receiver"),
        ("KDIGO", "Kidney Disease: Improving Global Outcomes"),
        ("NSAID", "Nonsteroidal anti-inflammatory drug"),
        ("SBAR", "Situation, background, assessment, recommendation"),
    ],
    "readings": [
        ("attending-nephrologist-02-consultation-dataset.html", "Attending Nephrologist, Module 2: The consultation dataset"),
        ("attending-nephrologist-03-communication-and-coverage.html", "Attending Nephrologist, Module 3: Communication and coverage"),
        ("herbal-nephropathy.html", "Herbal Nephropathy"),
        ("first-nephrology-visit-guide.html", "Your First Nephrology Visit"),
    ],
    "calcs": ["calc-which-kidney-test.html", "calc-ckd-progression-slope.html", "calc-icd10-search.html",
              "calc-aki-staging.html", "calc-fena-feurea.html", "calc-kegfr.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
