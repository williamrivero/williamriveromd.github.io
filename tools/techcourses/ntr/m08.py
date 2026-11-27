# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 08: Acid-base interpretation.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. Winters
formula (Albert 1967), albumin correction (Figge 1998), urine anion gap (Batlle 1988), anion gap limits (Kraut and
Madias 2007), EXTRIP methanol indications (2015), 2024 DKA consensus criteria, BICAR-ICU and PECARN FLUID checked
against PubMed abstracts or published summaries. Lambanog outbreak figure from a news report quoting DOH. No doses.
Fictional case."""

MODULE = {
    "image_alt": "In a Laguna emergency room, a Filipino resident and intern compare blood gas printouts for three men from the same drinking session while a nephrology fellow speaks on the phone beside a hemodialysis machine being prepared.",
    "objectives": [
        "<strong>Intern:</strong> Read the pH, the partial pressure of carbon dioxide (PaCO&#8322;) and the bicarbonate on a blood gas, name the primary disorder, and report a pH below 7.2 or a rising anion gap at once.",
        "<strong>Resident:</strong> Check compensation, calculate the albumin-corrected anion gap, the osmolal gap and, where useful, the urine anion gap, and use them to find the cause.",
        "<strong>Fellow:</strong> Teach the bicarbonate-centered and Stewart approaches, untangle mixed disorders, and manage toxic alcohol poisoning, diabetic ketoacidosis (DKA) and severe acidemia, including the decision to dialyze.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; three numbers and a story</span>A blood gas is three numbers that only make sense with a story. The <b>intern</b> owns the first read: acidemia or alkalemia, metabolic or respiratory, and a call when the pH is dangerous. The <b>resident</b> owns the arithmetic: compensation, the gaps, and a differential that fits them. The <b>fellow</b> owns the hard cases: the mixed disorder hiding behind a near-normal pH, the poisoning that needs dialysis tonight, and the teaching that makes the next intern faster.</div>
{{plain:Think of bicarbonate as the money in a household&rsquo;s emergency fund. Every day, acids from food and metabolism withdraw from it. The lungs act like a fast teller who can rebalance the account within minutes by blowing off carbon dioxide. The kidneys are the slow but steady earner who rebuilds the fund over days.}}
<p>The picture has a limit. A bank account holds a fixed sum, but the bicarbonate buffer is an open system. Carbon dioxide and bicarbonate are linked through carbonic acid, and the pH depends on their ratio, not on either alone, as the Henderson&ndash;Hasselbalch equation states. Because the lungs can change carbon dioxide in minutes, the system buffers far more acid than its concentration suggests. The kidneys do more than save: they reclaim all the filtered bicarbonate in the proximal tubule, and they generate new bicarbonate in the distal nephron by excreting acid as ammonium and as titratable acid such as phosphate. When kidney function falls, ammonium excretion falls first, and a chronic metabolic acidosis appears.[[ntr08_1]]</p>
<p>The Stewart approach describes the same chemistry differently. It treats the pH as set by three independent variables: the strong ion difference (mainly sodium minus chloride), the total weak acids (mainly albumin and phosphate) and the PaCO&#8322;. A chloride load from saline lowers the strong ion difference and causes acidosis; a low albumin removes weak acid and pushes toward alkalosis. The two approaches give the same diagnosis when used carefully; the Stewart frame is most useful when albumin and chloride are both abnormal, as in the intensive care unit (ICU).</p>
{{cards:Key numbers|Expected PaCO&#8322; in metabolic acidosis (Albert, Dell and Winters 1967)::1.5 &times; bicarbonate + 8 (&plusmn;2) mm Hg|Albumin correction (Figge 1998)::Each 1 g/dL fall in albumin lowers the anion gap by about 2.5 mmol/L|Methanol, EXTRIP 2015::Extracorporeal treatment for severe poisoning, including coma, seizures, new vision deficits, pH &le;7.15, persistent acidosis or anion gap above 24 mmol/L (consensus)|DKA, 2024 consensus::Glucose &ge;200 mg/dL or known diabetes; beta-hydroxybutyrate &ge;3.0 mmol/L or urine ketones &ge;2+; pH below 7.3 and/or bicarbonate below 18 mmol/L|BICAR-ICU, 389 patients::Primary outcome 71% control versus 66% bicarbonate (not significant)}}
<p>Most blood gases on a medical service tell a simple story: sepsis with lactate, vomiting with alkalosis, chronic kidney disease (CKD) with a low bicarbonate. A few hide two or three disorders at once, and a few are poisonings in which the hours before dialysis decide whether the patient sees again. Your work is to read every gas in the same order, to let the gaps point to the cause, and to recognize the patients who need the attending and a dialysis machine tonight.</p>
""",
    "case": {"title": "The drinking session in Rizal, Laguna",
             "html": """
<p>Sunday, 9 p.m., the emergency room of a provincial hospital in Laguna. Three men arrive together from a birthday celebration the night before in the town of Rizal, where they shared bottles of lambanog bought from a neighborhood store. All three have headache, abdominal pain and vomiting. Two say their vision is blurred, &ldquo;like looking through fog.&rdquo;</p>
<p>The sickest is Mr. Romeo Dimaculangan, 44, breathing deep and fast at 32 per minute. His arterial gas shows pH 7.08, PaCO&#8322; 18 mm Hg and bicarbonate 5 mmol/L. His sodium is 138 mmol/L, chloride 100 mmol/L, potassium 5.0 mmol/L, glucose 110 mg/dL, blood urea nitrogen 14 mg/dL, creatinine 1.4 mg/dL and albumin 4.0 g/dL. Measured serum osmolality is 330 mOsm/kg. Blood ethanol is not detected. The second man, Mr. Jun Robles, has a bicarbonate of 14 mmol/L and blurred vision. The third, Mr. Nestor Cuevas, kept drinking beer this morning; he is drowsy, smells of alcohol, and his bicarbonate is 21 mmol/L.</p>
<p>The intern, Dr. Paulo Garcia, hands the gases to the internal medicine resident, Dr. Lianne Sarmiento. The nephrology fellow, Dr. Mark Bautista, is called.</p>
""",
             "questions": ["What is Mr. Dimaculangan&rsquo;s primary disorder, and is his breathing compensating as expected?",
                           "What do the anion gap and the osmolal gap tell you, and why is Mr. Cuevas less acidotic?",
                           "What does the fellow arrange tonight, and how should three patients share one dialysis machine?"]},
    "sections": [
        ("buffers", "Buffers", "Buffers, lungs and kidneys: the physiology behind the numbers", """
<p>Each day, metabolism produces carbon dioxide in large amounts and a much smaller load of nonvolatile acid from protein and other sources. The carbon dioxide leaves through the lungs. The nonvolatile acid is first buffered, mostly by bicarbonate, and then excreted by the kidneys, which regenerate the bicarbonate used. Three lines of defense act on three time scales.</p>
<div class="table-wrap"><table>
<thead><tr><th>Defense</th><th>Speed</th><th>How it works</th><th>What failure looks like</th></tr></thead>
<tbody>
<tr><td>Chemical buffers (bicarbonate, proteins, phosphate, bone)</td><td>Seconds</td><td>Bind hydrogen ions</td><td>A falling bicarbonate as the buffer is used up</td></tr>
<tr><td>Lungs</td><td>Minutes to hours</td><td>Change ventilation to change PaCO&#8322;</td><td>Respiratory acidosis when the patient tires or is sedated; Kussmaul breathing in metabolic acidosis</td></tr>
<tr><td>Kidneys</td><td>Hours to days</td><td>Reclaim filtered bicarbonate; make new bicarbonate by excreting ammonium and titratable acid</td><td>Chronic metabolic acidosis in CKD and renal tubular acidosis</td></tr>
</tbody></table></div>
<p>Compensation always moves the second variable in the same direction as the first. In metabolic acidosis the bicarbonate falls, so ventilation increases and the PaCO&#8322; falls too. Compensation reduces the change in pH but rarely returns it fully to normal. A normal pH with an abnormal bicarbonate and PaCO&#8322; should make you suspect two opposing disorders, not perfect compensation.[[ntr08_1]]</p>
<p>A venous blood gas gives a pH and bicarbonate close enough to arterial values for most metabolic questions, but not an oxygen value and not a reliable PaCO&#8322; in shock. Many Philippine emergency rooms have a blood gas machine; many provincial hospitals send the sample to a laboratory with a delay. When the gas is delayed, the electrolyte panel already gives you the bicarbonate and the anion gap.</p>
{{key:Compensation moves in the same direction and never quite reaches normal. A normal pH with abnormal parts means two disorders until proven otherwise.}}
"""),
        ("stepwise", "Step by step", "A stepwise reading you can do at 3 a.m.", """
<p>Read every gas in the same order. The order protects you from anchoring on the first abnormal number.</p>
{{flow:Reading a blood gas|1. The pH::Below 7.35 is acidemia; above 7.45 is alkalemia. A pH below 7.2 needs a call now.|2. The primary process::In acidemia, a low bicarbonate means metabolic acidosis and a high PaCO&#8322; means respiratory acidosis. In alkalemia, a high bicarbonate means metabolic alkalosis and a low PaCO&#8322; means respiratory alkalosis.|3. Compensation::For metabolic acidosis, compare the PaCO&#8322; with 1.5 &times; bicarbonate + 8 (&plusmn;2). Higher than expected means a respiratory acidosis as well; lower means a respiratory alkalosis as well. Use the site&rsquo;s calculators for the other disorders.|4. The anion gap::Sodium minus (chloride plus bicarbonate), corrected for albumin. Always calculate it, even when the pH looks normal.|5. If the gap is high::Compare the rise in the gap with the fall in bicarbonate, and calculate the osmolal gap if a toxic alcohol is possible.|6. If the gap is normal::Think of bicarbonate loss from the gut or kidney, or chloride gain; the urine anion gap helps separate them.|7. The story::Does the diagnosis fit the history, the medicines and the examination? If not, read again.}}
<p>The compensation formula for metabolic acidosis comes from Albert, Dell and Winters, who derived it in 1967 from patients with metabolic acidosis: expected PaCO&#8322; = 1.5 &times; bicarbonate + 8, &plusmn;2 mm Hg.[[ntr08_4]] It applies to a steady state; for an hour or two after a sudden acid load, ventilation may not have caught up.</p>
{{formula:<strong>Arithmetic illustration, not a target.</strong> Bicarbonate 12 mmol/L: expected PaCO&#8322; = 1.5 &times; 12 + 8 = 26 mm Hg (range 24 to 28).<br>Measured PaCO&#8322; 34 mm Hg: higher than expected, so a respiratory acidosis is present as well, for example a tiring patient or sedation.<br>Measured PaCO&#8322; 18 mm Hg: lower than expected, so a respiratory alkalosis is present as well, for example sepsis or salicylate poisoning.}}
<div class="table-wrap"><table>
<thead><tr><th>Primary disorder</th><th>Common causes on a Philippine medical service</th><th>A clue at the bedside</th></tr></thead>
<tbody>
<tr><td>Metabolic acidosis</td><td>Sepsis, diarrhea, DKA, acute kidney injury (AKI) and CKD, toxic alcohols, leptospirosis with AKI</td><td>Deep, fast breathing</td></tr>
<tr><td>Metabolic alkalosis</td><td>Vomiting, nasogastric suction, diuretics, low potassium</td><td>Low chloride, low potassium, a history of vomiting or diuretics</td></tr>
<tr><td>Respiratory acidosis</td><td>Chronic obstructive lung disease, sedation, neuromuscular weakness, a tiring patient</td><td>Drowsiness, shallow breathing</td></tr>
<tr><td>Respiratory alkalosis</td><td>Sepsis, liver disease, pregnancy, anxiety, early salicylate poisoning</td><td>Fast breathing with a high pH</td></tr>
</tbody></table></div>
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>What you own in reading a gas</th></tr></thead>
<tbody>
<tr><td>Intern</td><td>Steps 1 and 2 on every gas; report a pH below 7.2, a bicarbonate below 10 mmol/L or a rising anion gap at once</td></tr>
<tr><td>Resident</td><td>Steps 3 to 7; write the full interpretation in the note with the gaps and the differential</td></tr>
<tr><td>Fellow</td><td>Mixed and triple disorders; teach both approaches; decide with the attending when acidemia needs dialysis</td></tr>
</tbody></table></div>
{{key:Read every gas in the same seven steps. Calculate the anion gap every time, because a normal pH can hide a high-gap acidosis and an alkalosis together.}}
"""),
        ("gaps", "The gaps", "The gaps: anion, osmolal and urine", """
<h3>The anion gap</h3>
<p>Blood is electrically neutral. The anion gap, sodium minus the sum of chloride and bicarbonate, reflects anions that are not measured, chiefly albumin. When an acid such as lactic acid, ketoacid or formic acid accumulates, its hydrogen ion consumes bicarbonate and its anion stays behind, so the gap rises. When bicarbonate is lost from the gut or kidney, chloride replaces it and the gap stays normal.</p>
<p>The normal range varies widely between laboratories and methods, so know your own laboratory&rsquo;s range.[[ntr08_2]] Albumin carries most of the normal gap. Figge and colleagues studied 152 critically ill patients and found that each 1 g/L fall in albumin lowered the observed gap by 0.25 mmol/L, which is 2.5 mmol/L for each 1 g/dL.[[ntr08_3]] In a patient with an albumin of 2.0 g/dL, a &ldquo;normal&rdquo; gap of 12 mmol/L may hide an acidosis.</p>
{{formula:<strong>Arithmetic illustration, not a target.</strong> Anion gap = sodium &minus; (chloride + bicarbonate).<br>Albumin-corrected gap = measured gap + 2.5 &times; (normal albumin &minus; measured albumin, in g/dL).<br>Sodium 136, chloride 104, bicarbonate 18, albumin 2.0 g/dL (normal taken as 4.0): measured gap 14; corrected gap 14 + 2.5 &times; 2 = 19 mmol/L.}}
<p>The delta ratio compares the rise in the gap with the fall in bicarbonate, to look for a second metabolic disorder: a fall in bicarbonate much larger than the rise in the gap suggests an added normal-gap acidosis; a much smaller fall suggests an added metabolic alkalosis. Kraut and Madias caution that the ratio varies considerably within high-gap acidosis, so it should not be used alone to diagnose a mixed disorder.[[ntr08_2]] Use it as a prompt to look harder, not as a verdict.</p>
<h3>The osmolal gap</h3>
<p>Methanol, ethylene glycol and other alcohols are small, osmotically active molecules that are not counted in the calculated osmolality. The osmolal gap, measured minus calculated osmolality, rises when they are present, before they are metabolized. As the parent alcohol is converted to toxic acids, the osmolal gap falls and the anion gap rises. A patient seen late may have a normal osmolal gap and a very high anion gap; a patient seen early may have the reverse.[[ntr08_6]] A normal osmolal gap therefore does not exclude a toxic alcohol, and ethanol raises the osmolal gap by itself and must be accounted for.</p>
{{formula:<strong>Arithmetic illustration, not a target.</strong> Calculated osmolality = 2 &times; sodium + glucose (mg/dL) &divide; 18 + blood urea nitrogen (mg/dL) &divide; 2.8.<br>Sodium 138, glucose 110, urea nitrogen 14: 276 + 6.1 + 5.0 &asymp; 287 mOsm/kg. Measured 330: osmolal gap &asymp; 43 mOsm/kg.}}
<h3>The urine anion gap</h3>
<p>In a normal-gap acidosis, the question is whether the kidney is responding by excreting acid. The kidney excretes acid mostly as ammonium, which the laboratory does not measure, but ammonium travels with chloride. Batlle and colleagues measured urine sodium plus potassium minus chloride in 46 patients. In normal subjects given an acid load, the gap was negative (about &minus;27 mmol/L), and in patients with diarrhea it was also negative (about &minus;20 mmol/L) despite a urine pH above 5.3. In patients with impaired distal acidification, renal tubular acidosis or selective aldosterone deficiency, it was positive.[[ntr08_5]] A negative urine anion gap suggests gut loss of bicarbonate with an intact kidney response; a positive one suggests the kidney is failing to excrete acid. It is a rough index of ammonium and misleads when other unmeasured anions, such as ketones, are in the urine.</p>
<div class="table-wrap"><table>
<thead><tr><th>Gap</th><th>What it detects</th><th>Main trap</th></tr></thead>
<tbody>
<tr><td>Serum anion gap</td><td>Unmeasured acid anions</td><td>Low albumin hides it; laboratory ranges differ</td></tr>
<tr><td>Delta ratio</td><td>A second metabolic disorder</td><td>Wide natural variation; never use alone</td></tr>
<tr><td>Osmolal gap</td><td>Unmeasured osmoles such as toxic alcohols</td><td>Normal late in poisoning; raised by ethanol</td></tr>
<tr><td>Urine anion gap</td><td>Urine ammonium in normal-gap acidosis</td><td>Misleads with ketonuria and other urine anions</td></tr>
</tbody></table></div>
{{fig:ntr08_b}}
{{key:Correct the anion gap for albumin, read the osmolal gap with the clock in mind, and remember that every gap is a clue, not a diagnosis.}}
"""),
        ("special", "Special problems", "DKA, toxic alcohols, lactic acidosis, renal tubular acidosis and alkalosis", """
<h3>Toxic alcohols, and the Philippine outbreaks</h3>
<p>Methanol itself is relatively harmless. Alcohol dehydrogenase converts it to formaldehyde and then formic acid, which poisons mitochondria in the retina and the basal ganglia. That is why vision fails and why the patient may look well for many hours before the acidosis appears. Ethanol and fomepizole compete for or block alcohol dehydrogenase and stop the conversion; dialysis removes both methanol and formate.[[ntr08_6]]</p>
<p>Philippine outbreaks of methanol poisoning have been linked to lambanog, a distilled coconut liquor, when illegally or poorly distilled batches contain methanol. In December 2019, the Department of Health (DOH) office for Calabarzon confirmed 23 deaths in an outbreak that began in Rizal, Laguna, and spread to Quezon province.[[ntr08_10]] Outbreaks bring many patients at once to hospitals with one or two dialysis machines.</p>
<p>The Extracorporeal Treatments in Poisoning (EXTRIP) workgroup recommends extracorporeal treatment for severe methanol poisoning, including any of coma, seizures, new vision deficits, a blood pH of 7.15 or less, persistent metabolic acidosis despite supportive measures and antidotes, or an anion gap above 24 mmol/L, as well as for high methanol concentrations, or impaired kidney function. In the absence of a methanol level, the osmolal gap may be informative. Intermittent hemodialysis is the modality of choice, and continuous modalities are acceptable alternatives. The workgroup noted that the relative importance of each indication for triage in an epidemic, when need exceeds resources, is unknown, and that decisions about cost and availability must be made locally.[[ntr08_7]] Few Philippine hospitals can measure methanol, and fomepizole is not stocked everywhere; ask early what your hospital has.</p>
{{call:Stop and call the attending nephrologist now, per unit protocol, but always ask the attending nephrologist for guidance, when:<ul><li>The pH is below 7.2, or the bicarbonate is below 10 mmol/L</li><li>A high anion gap acidosis comes with visual symptoms, an osmolal gap, or a history of homemade or unlabeled liquor</li><li>Several patients arrive from the same drinking session or the same source</li><li>A patient with DKA is drowsy, or a patient taking a sodium&ndash;glucose cotransporter 2 (SGLT2) inhibitor has ketoacidosis with a near-normal glucose</li><li>Acidemia is worsening despite treatment, or the patient is tiring</li></ul>}}
<h3>Diabetic ketoacidosis, including with SGLT2 inhibitors</h3>
<p>The 2024 consensus report defines DKA by three criteria: a glucose of 200 mg/dL or more or a known history of diabetes; ketosis, with beta-hydroxybutyrate of 3.0 mmol/L or more or urine ketones of 2+ or more; and metabolic acidosis, with a pH below 7.3 and/or a bicarbonate below 18 mmol/L.[[ntr08_8]] The anion gap is no longer a diagnostic criterion, and the lower glucose threshold and the &ldquo;known diabetes&rdquo; clause capture euglycemic DKA. SGLT2 inhibitors lower glucose by glycosuria, so a patient can be ketoacidotic with a glucose that looks reassuring. These drugs are increasingly used in the Philippines for diabetes, heart failure and CKD, often bought out of pocket. Ask about them in every patient with an unexplained high-gap acidosis, especially after surgery, fasting or acute illness.</p>
<h3>Lactic acidosis and bicarbonate</h3>
<p>Lactic acidosis from shock (type A) is treated by restoring perfusion; lactic acidosis without shock (type B) has causes such as metformin accumulation in AKI, liver failure, thiamine deficiency and malignancy. Bicarbonate therapy was tested in the BICAR-ICU (sodium bicarbonate for severe metabolic acidemia in the ICU) trial, which randomized 389 ICU patients with severe metabolic acidemia (pH 7.20 or less, PaCO&#8322; 45 mm Hg or less, bicarbonate 20 mmol/L or less). The primary outcome, death by day 28 or organ failure at day 7, occurred in 71% of controls and 66% with bicarbonate (absolute difference &minus;5.5 percentage points, not significant). In a prespecified stratum with moderate to severe AKI, 28-day survival was 37% without and 54% with bicarbonate.[[ntr08_9]] A subgroup finding is a hypothesis, not proof. Metabolic alkalosis, hypernatremia and hypocalcemia were more frequent with bicarbonate.</p>
<h3>Renal tubular acidosis and metabolic alkalosis</h3>
<div class="table-wrap"><table>
<thead><tr><th>Disorder</th><th>Mechanism</th><th>Clues</th></tr></thead>
<tbody>
<tr><td>Distal (type 1) renal tubular acidosis</td><td>Collecting duct cannot secrete acid</td><td>Normal-gap acidosis, low potassium, positive urine anion gap, urine pH that cannot fall, stones and nephrocalcinosis; autoimmune disease</td></tr>
<tr><td>Proximal (type 2) renal tubular acidosis</td><td>Proximal tubule cannot reclaim bicarbonate</td><td>Normal-gap acidosis, often with glycosuria at normal glucose, phosphate and urate wasting (Fanconi syndrome); some drugs and myeloma</td></tr>
<tr><td>Type 4 (hyperkalemic) renal tubular acidosis</td><td>Low aldosterone effect</td><td>Normal-gap acidosis with high potassium; diabetes, renin&ndash;angiotensin&ndash;aldosterone system (RAAS) inhibitors, trimethoprim</td></tr>
<tr><td>Chloride-responsive metabolic alkalosis</td><td>Chloride and volume loss maintain bicarbonate reabsorption</td><td>Vomiting, nasogastric suction, past diuretics; low urine chloride</td></tr>
<tr><td>Chloride-resistant metabolic alkalosis</td><td>Mineralocorticoid excess or ongoing diuretic</td><td>High blood pressure or current diuretic; high urine chloride</td></tr>
</tbody></table></div>
{{fig:ntr08_a}}
<div class="tc-keyp"><span class="tc-lab">In children</span>Children with DKA are at risk of cerebral injury during treatment. The Pediatric Emergency Care Applied Research Network (PECARN) FLUID trial randomized 1,389 DKA episodes in 1,255 children to faster or slower fluid and to 0.9% or 0.45% sodium chloride; mental status declined in 3.5% of episodes and clinically apparent brain injury occurred in 0.9%, with no significant differences between groups.[[ntr08_11]] Normal blood gas values and compensation differ in neonates, and inherited metabolic disorders and renal tubular acidosis present early in life. See <a href="attending-pediatric-nephrologist-03-fluids-sodium-acid-base.html">Attending Pediatric Nephrologist, Module 03</a>.</div>
{{key:In a high-gap acidosis, ask four questions: ketones, lactate, kidney failure, toxin. If the story includes unlabeled liquor or blurred vision, call the attending and prepare for dialysis before the methanol level returns.}}
"""),
    ],
    "debrief": ["""
<p><strong>The primary disorder and its compensation.</strong> The pH of 7.08 is severe acidemia, and the bicarbonate of 5 mmol/L makes it a metabolic acidosis. Expected PaCO&#8322; is 1.5 &times; 5 + 8 = 15.5, range 13.5 to 17.5 mm Hg. His measured 18 mm Hg sits just above that range: his breathing is not quite keeping up, which may mean he is beginning to tire. Dr. Garcia should report the pH below 7.2 at once, and the team should watch his breathing closely, because if ventilation fails, the pH will fall sharply.</p>
""", """
<p><strong>The gaps, and the third man.</strong> His anion gap is 138 &minus; (100 + 5) = 33 mmol/L with a normal albumin, a high-gap acidosis. The rise in the gap (about 21 above a typical 12) roughly matches the fall in bicarbonate (about 19), so there is no strong sign of a second metabolic disorder, keeping in mind that the ratio varies. His calculated osmolality is about 287 and his measured 330, an osmolal gap of about 43, with no ethanol to explain it. A high anion gap, a high osmolal gap, blurred vision and lambanog point to methanol poisoning. Mr. Cuevas is less acidotic because he kept drinking ethanol, which competes for alcohol dehydrogenase and slows the conversion of methanol to formic acid; he is not safe, and he needs the same assessment and an antidote once the ethanol wanes.</p>
""", """
<p><strong>Tonight&rsquo;s plan and the one machine.</strong> Dr. Bautista calls the attending nephrologist. An alcohol dehydrogenase blocker is started for all three, using what the hospital stocks, per protocol. Mr. Dimaculangan meets several EXTRIP indications: vision changes, a pH of 7.08 and an anion gap above 24 mmol/L; Mr. Robles has vision changes. The attending decides the order of dialysis, the fellow prepares the circuit without systemic anticoagulation if possible, and the team contacts the nearest center with a second machine for transfer. EXTRIP notes that triage in an epidemic has no evidence base, so the decision is clinical and documented. The resident notifies the DOH regional office, because other drinkers from the same store may be at home with early symptoms.</p>
"""],
    "skills": {"title": "Blood gas interpretation and toxic alcohol response",
               "intro": "Complete with a preceptor using real or teaching blood gases. Sign-off is local.",
               "items": [
                   ("Reads ten blood gases in the seven-step order and names the primary disorder correctly in each", False),
                   ("Calculates expected PaCO&#8322; with the Winters formula and identifies a concurrent respiratory disorder", False),
                   ("Calculates the albumin-corrected anion gap and the osmolal gap, and explains the time course of each in methanol poisoning", False),
                   ("Uses the urine anion gap to separate gut from kidney causes of a normal-gap acidosis, naming its limits", False),
                   ("States the EXTRIP indications for dialysis in methanol poisoning and what the hospital stocks as an antidote", False),
               ],
               "placement": "Emergency room, medical ward, ICU or hemodialysis unit"},
    "quiz": [
        ("A blood gas shows pH 7.24, PaCO&#8322; 28 mm Hg and bicarbonate 12 mmol/L. What is the primary disorder?",
         ["Respiratory alkalosis",
          "Respiratory acidosis",
          "Metabolic alkalosis",
          "Metabolic acidosis"], 3,
         "The pH is low (acidemia) and the bicarbonate is low, so the primary process is metabolic acidosis. The low PaCO&#8322; is compensation, moving in the same direction."),
        ("A patient has sodium 135, chloride 100, bicarbonate 20 mmol/L and albumin 1.8 g/dL. Using the Figge correction and a normal albumin of 4.0 g/dL, what is the corrected anion gap?",
         ["About 20.5 mmol/L, a high gap that the low albumin was hiding",
          "15 mmol/L, normal",
          "About 9.5 mmol/L, low",
          "It cannot be calculated without a lactate"], 0,
         "Measured gap = 135 &minus; (100 + 20) = 15 mmol/L. Correction = 2.5 &times; (4.0 &minus; 1.8) = 5.5. Corrected gap = about 20.5 mmol/L. Reading the measured 15 as normal would miss an unmeasured acid; subtracting the correction instead of adding it gives the wrong answer of 9.5."),
        ("A fellow is teaching about the delta ratio in high anion gap acidosis. Which statement is most accurate?",
         ["A ratio of exactly 1 is required to diagnose a pure high-gap acidosis",
          "The ratio varies considerably within high-gap acidosis, so it prompts a search for a second disorder but should not be used alone",
          "The ratio replaces the need to calculate compensation",
          "The ratio is only valid in respiratory disorders"], 1,
         "Kraut and Madias showed wide variation in the rise of the gap relative to the fall in bicarbonate. Use the ratio with the history, other electrolytes and compensation."),
        ("A man who drank homemade liquor yesterday has blurred vision, pH 7.12, anion gap 30 mmol/L and an osmolal gap of 8 mOsm/kg. A colleague says the normal osmolal gap excludes methanol. What is the best response?",
         ["Agree; a normal osmolal gap excludes toxic alcohols",
          "Wait for a methanol level before any treatment",
          "Disagree; late in poisoning, methanol has been converted to formic acid, so the osmolal gap falls while the anion gap rises; he meets EXTRIP criteria and needs the attending and dialysis",
          "Treat with bicarbonate alone and observe"], 2,
         "The osmolal gap reflects the parent alcohol; the anion gap reflects its toxic acids. Vision deficits, pH 7.15 or less and an anion gap above 24 mmol/L are EXTRIP indications for extracorporeal treatment."),
        ("A 52-year-old woman with type 2 diabetes on an SGLT2 inhibitor is admitted two days after surgery with vomiting. Her glucose is 190 mg/dL, pH 7.21, bicarbonate 13 mmol/L and beta-hydroxybutyrate 4.5 mmol/L. What is the diagnosis by the 2024 consensus criteria?",
         ["DKA; known diabetes satisfies the glucose criterion, with ketosis and acidosis",
          "Not DKA, because the glucose is below 250 mg/dL",
          "Lactic acidosis",
          "Starvation ketosis without clinical significance"], 0,
         "The 2024 criteria accept a known history of diabetes in place of glucose of 200 mg/dL or more, which captures euglycemic DKA, a recognized risk with SGLT2 inhibitors after surgery or fasting."),
    ],
    "terms": [
        ("AKI", "Acute kidney injury"),
        ("BICAR-ICU", "Sodium bicarbonate therapy for patients with severe metabolic acidaemia in the intensive care unit (trial)"),
        ("CKD", "Chronic kidney disease"),
        ("DKA", "Diabetic ketoacidosis"),
        ("DOH", "Department of Health"),
        ("EXTRIP", "Extracorporeal Treatments in Poisoning (workgroup)"),
        ("ICU", "Intensive care unit"),
        ("PaCO&#8322;", "Partial pressure of carbon dioxide in arterial blood"),
        ("PECARN", "Pediatric Emergency Care Applied Research Network"),
        ("RAAS", "Renin&ndash;angiotensin&ndash;aldosterone system"),
        ("SGLT2", "Sodium&ndash;glucose cotransporter 2"),
    ],
    "readings": [
        ("metabolic-acidosis-ckd.html", "Metabolic Acidosis in CKD"),
        ("unlocking-urine-electrolytes-clinician.html", "Unlocking Urine Electrolytes (Clinician)"),
        ("physician-on-duty-02-water-salt-potassium-acid.html", "Physician on Duty, Module 2: Water, Salt, Potassium and Acid"),
        ("attending-nephrologist-06-electrolyte-emergencies.html", "Attending Nephrologist, Module 6: Electrolyte Emergencies"),
    ],
    "calcs": ["calc-abg-analyzer.html", "calc-anion-gap-acid-base.html", "calc-winters-formula.html", "calc-osmolal-gap.html",
              "calc-urine-anion-gap.html", "calc-stewart-sig.html", "calc-bicarb-deficit.html", "calc-dka-management.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
