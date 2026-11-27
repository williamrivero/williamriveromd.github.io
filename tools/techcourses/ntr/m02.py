# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 02: Renal physiology for clinical decisions.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard.
KDIGO 2024 Chapter 1 recommendation grades (1B, 1C, 1D) checked against KDIGO's summary of recommendations; CKD-EPI 2021,
EKFC 2021, kinetic eGFR (Chen 2013), Cockcroft-Gault 1976 and CKiD U25 checked against PubMed. Case eGFR values computed
with the published equations. No doses. Fictional case."""

MODULE = {
    "image_alt": "A Filipino resident sketches a nephron on a whiteboard for two interns, with an arrow from the glomerulus to the collecting duct and a creatinine curve beside it.",
    "objectives": [
        "<strong>Intern:</strong> Explain at the bedside, in plain words, how the kidney filters blood, adjusts what it keeps along the tubule, and balances water separately from salt.",
        "<strong>Resident:</strong> Use filtration, tubular handling and water balance to read common laboratory patterns, including a creatinine that looks normal but is not, and a creatinine that rises without any change in filtration.",
        "<strong>Fellow:</strong> Connect clearance, tubular transport and renal hemodynamics to competing treatment choices, and choose the right estimate of glomerular filtration rate (GFR) for the decision at hand, stating its assumptions.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; reading the kidney&rsquo;s numbers</span>An <strong>intern</strong> owns the baseline: finding the old creatinine, the weight, the urine output and the medicine list, and noticing when a &ldquo;normal&rdquo; value has doubled. A <strong>resident</strong> owns the interpretation: which estimate applies, whether the patient is in steady state, and what the pattern means. A <strong>fellow</strong> owns the choice: when to measure cystatin C or a timed clearance, which estimate to use for a drug decision, and how a change in hemodynamics will move the number.</div>
{{plain:Think of a rice mill with a sieve and a sorting line. The sieve lets fine grains and husk dust through by the sackful. Workers along the line pick back the good grains and toss the stones. What leaves the mill at the end is a small sack of what the owner did not want to keep.}}
<p>The picture has a limit. A mill sorts at a fixed speed. The kidney&rsquo;s sieve, the glomerulus, filters about 125 mL of plasma a minute in a healthy young adult, which is roughly 180 liters a day, and the tubule then returns almost all of the water and salt. But the tubule does not work at a fixed rate. Hormones, blood pressure and the medicines you prescribe change what each segment keeps, minute by minute. And the number you use to judge the sieve, the serum creatinine, depends on how much creatinine the muscles make and how much the tubule secretes, not only on filtration.</p>
<p>That is the physiology behind most mistakes with kidney numbers. A small, frail patient makes little creatinine, so a filtration rate that is truly low can sit behind a creatinine inside the laboratory&rsquo;s normal range. A drug that blocks creatinine secretion can raise the creatinine with no change in filtration. And in acute kidney injury (AKI), the creatinine lags behind the filtration rate by a day or more.</p>
{{cards:Key numbers|Initial GFR assessment (KDIGO 2024)::Creatinine-based estimated GFR (eGFRcr) for adults at risk of CKD; use creatinine plus cystatin C if available (1B)|When eGFRcr is less accurate (KDIGO 2024)::Use eGFRcr-cys when GFR affects a clinical decision (1C)|Use an equation, not creatinine alone (KDIGO 2024)::Validated estimating equation recommended (1D)|CKD-EPI 2021 race-free equations::85% or more of estimates within 30% of measured GFR in validation|AKI stage 2 (KDIGO 2012)::Creatinine 2.0 to 2.9 times baseline (ungraded definition)}}
<p>Most of the time a stable creatinine and an estimating equation are good enough. A few patients break the equation&rsquo;s assumptions: the very thin, the very muscular, the acutely ill, the patient on a drug that blocks secretion. Your work is to know which patient is in front of you, to say aloud which assumption fails, and to choose a better measure when the decision depends on it.</p>
""",
    "case": {"title": "The normal creatinine", "html": """
<p>Thursday, 3 p.m., the medical ward of a provincial hospital in San Fernando, Pampanga. Mrs. Teresita Mallari, 78, is admitted for a fall at home. She is frail, weighs 38 kg, and has eaten little for a week. She takes a thiazide for blood pressure and, her daughter says, a &ldquo;pain reliever for her knees&rdquo; bought at the market.</p>
<p>Her serum creatinine today is 1.1 mg/dL. The laboratory&rsquo;s reference range is 0.6 to 1.2 mg/dL, and the result is not flagged. The intern, Dr. Paolo Lansang, finds a clinic slip on the daughter&rsquo;s phone: six months ago her creatinine was 0.5 mg/dL. Her urine output since admission is about 120 mL over eight hours. The admitting note reads &ldquo;renal function normal.&rdquo;</p>
""", "questions": [
        "Is her kidney function normal? What does the change from 0.5 to 1.1 mg/dL mean physiologically?",
        "What do the estimating equations say, and why may each be wrong for her today?",
        "What would you measure or do next, and what would change your plan?"]},
    "sections": [
        ("filtration", "GFR and creatinine", "Glomerular filtration and what creatinine really measures", """
<p>Filtration is pressure working against a barrier. The heart drives blood into the glomerular capillaries; the afferent arteriole sets how much pressure arrives and the efferent arteriole sets how much stays. The pressure pushes plasma water and small solutes across the capillary wall into Bowman&rsquo;s space, and the GFR is the total volume filtered per minute by all nephrons. Large proteins and cells stay behind.</p>
<p>The kidney defends its GFR. When pressure falls, the afferent arteriole relaxes and angiotensin II tightens the efferent arteriole, which keeps pressure in the capillary. This is why a patient who depends on angiotensin II, through volume depletion, heart failure or renal artery stenosis, can lose GFR quickly when started on an angiotensin-converting enzyme (ACE) inhibitor or angiotensin receptor blocker (ARB), and why a nonsteroidal anti-inflammatory drug (NSAID), which removes the prostaglandins that relax the afferent arteriole, does harm in the same patient. It is also why a modest early fall in eGFR with these drugs, or with a sodium-glucose cotransporter 2 (SGLT2) inhibitor, is expected: lowering glomerular pressure is part of how they protect the kidney over years.</p>
<h3>Creatinine is a waste product, not a ruler</h3>
<p>Creatinine comes from creatine in muscle, at a rate roughly proportional to muscle mass, with a smaller amount from cooked meat. It is filtered freely, and a part is also secreted by the proximal tubule. Its serum level therefore depends on four things: how much is made, how much is filtered, how much is secreted, and, in some laboratory methods, substances that interfere with the assay.[[ntr02_6]] Only one of the four is the GFR.</p>
<p>At steady state, creatinine production equals creatinine excretion. Production is roughly fixed for a given person, so if the GFR halves, the serum creatinine must double before excretion again matches production. The relationship is a hyperbola: serum creatinine is roughly proportional to 1 divided by GFR.</p>
{{fig:ntr02_b}}
<div class="table-wrap"><table>
<thead><tr><th>Where the creatinine comes from or goes</th><th>What changes it</th><th>What you see</th></tr></thead>
<tbody>
<tr><td>Production by muscle</td><td>Low muscle mass (frailty, old age, small body size, amputation, malnutrition, liver disease); high muscle mass; a large cooked-meat meal</td><td>A low-normal creatinine that hides a low GFR; a high creatinine in a muscular young man with normal GFR</td></tr>
<tr><td>Filtration</td><td>True change in GFR</td><td>The change you are trying to detect</td></tr>
<tr><td>Tubular secretion</td><td>Drugs that block secretion, such as trimethoprim and cimetidine; secretion rises as GFR falls</td><td>A creatinine rise without a fall in GFR; a creatinine clearance that overestimates GFR in CKD</td></tr>
<tr><td>Assay</td><td>Interference in some methods, for example from ketones or bilirubin</td><td>A value that does not fit the patient</td></tr>
</tbody></table></div>
<h3>The flat part and the steep part</h3>
<p>The hyperbola explains two bedside errors. On the flat part, at high GFR, a large fall in GFR moves the creatinine only a little: from 0.5 to 1.1 mg/dL in a small woman is a reading the laboratory may not flag, yet it may mean she has lost more than half her filtration. On the steep part, at low GFR, a small change in GFR moves the creatinine a lot, so a rise from 4.0 to 4.6 mg/dL may mean only a small further loss.</p>
<p>Many Filipino patients, especially older women, are small and carry little muscle. Their creatinine runs low when they are well. Judge every creatinine against that person&rsquo;s own baseline and body, not against the laboratory&rsquo;s range.</p>
{{key:Compare every creatinine with the patient&rsquo;s own baseline and muscle mass. A doubling inside the normal range is still a doubling.}}
"""),
        ("tubules", "Segment by segment", "The tubule segment by segment, with the drugs that act there", """
<p>The filtrate leaving Bowman&rsquo;s space is plasma without its proteins. The tubule decides, segment by segment, what to keep. Each segment has a main transporter, and most kidney drugs act by blocking one of them. Knowing the map lets you predict what a drug does to sodium, potassium, acid and water, and why two diuretics together do more than one.[[ntr02_8]]</p>
{{fig:ntr02_a}}
<div class="table-wrap"><table>
<thead><tr><th>Segment</th><th>Main job and transporter</th><th>Drugs acting there</th><th>What you may see</th></tr></thead>
<tbody>
<tr><td>Proximal tubule</td><td>Reclaims most filtered sodium, glucose, bicarbonate, phosphate and amino acids; sodium-glucose cotransport (SGLT2), sodium-hydrogen exchange; secretes creatinine and many drugs</td><td>SGLT2 inhibitors; carbonic anhydrase inhibitors (acetazolamide); trimethoprim and cimetidine block creatinine secretion</td><td>Glucosuria; an early modest eGFR dip with SGLT2 inhibitors; bicarbonate loss; a creatinine rise without GFR change</td></tr>
<tr><td>Thick ascending limb of the loop of Henle</td><td>Sodium-potassium-2-chloride cotransport (NKCC2); builds the concentrated medulla; reclaims calcium and magnesium</td><td>Loop diuretics (furosemide)</td><td>Large natriuresis; loss of potassium, calcium and magnesium; a dilute, less concentrated urine</td></tr>
<tr><td>Distal convoluted tubule</td><td>Sodium-chloride cotransport (NCC); fine-tunes calcium</td><td>Thiazides</td><td>Hyponatremia in older patients; hypokalemia; less calcium in urine</td></tr>
<tr><td>Collecting duct (principal cell)</td><td>Epithelial sodium channel (ENaC) under aldosterone, potassium secretion; water through aquaporin-2 under antidiuretic hormone (ADH)</td><td>Spironolactone, eplerenone, finerenone (mineralocorticoid receptor); amiloride and trimethoprim (ENaC); tolvaptan (vasopressin V2 receptor)</td><td>Hyperkalemia; free-water loss with tolvaptan</td></tr>
<tr><td>Collecting duct (intercalated cell)</td><td>Acid secretion and bicarbonate handling</td><td>&mdash;</td><td>Distal renal tubular acidosis when it fails</td></tr>
</tbody></table></div>
<h3>Why the segments talk to each other</h3>
<p>Block one segment and the next one works harder. A loop diuretic sends more sodium to the distal tubule, which grows and reclaims more over weeks; adding a thiazide blocks that adaptation. More sodium delivered to the collecting duct means more potassium secreted, which is why loop and thiazide diuretics cause hypokalemia, and why blocking aldosterone or ENaC raises potassium.[[ntr02_8]] The same logic explains why a patient on a thiazide who drinks tea and eats little salt becomes hyponatremic: the thiazide impairs dilution in the distal tubule, and the low solute intake leaves too little to excrete water with. Module 6 builds on this.</p>
<h3>Reading a pattern instead of a number</h3>
<p>The tubule writes its work into the blood and the urine. A low bicarbonate with a normal anion gap points to the proximal or distal tubule or to the gut. Glucose in the urine with a normal blood sugar points to the proximal tubule or an SGLT2 inhibitor. A high potassium in a patient with modest CKD on spironolactone and trimethoprim points to two blocks in the collecting duct, not to a sudden loss of GFR. Ask which segment could produce the pattern, then which drug or disease acts there.</p>
{{key:For every electrolyte surprise, ask which tubular segment could produce it and which drug on the list acts there.}}
"""),
        ("water", "Water versus salt", "Water balance is not salt balance", """
<p>The kidney runs two separate control systems, and confusing them causes many errors.</p>
<p><strong>Salt controls volume.</strong> Sodium is the main solute outside cells, so the total body sodium sets the size of the extracellular fluid. When the circulation senses low effective volume, through the baroreceptors and the afferent arteriole, renin, angiotensin II, aldosterone and sympathetic nerves make the tubule keep sodium. Edema means too much total sodium; dryness means too little. The urine sodium tells you what the kidney thinks of the volume, unless a diuretic is speaking for it.</p>
<p><strong>Water controls concentration.</strong> The plasma sodium concentration reflects the ratio of sodium to water, and it is set mostly by water balance. When plasma tonicity rises by a small amount, the hypothalamus releases ADH and makes you thirsty. ADH inserts aquaporin-2 channels in the collecting duct, and water flows back into the concentrated medulla built by the loop of Henle. When tonicity falls, ADH switches off and the kidney makes dilute urine.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>What answers it</th><th>Bedside clue</th></tr></thead>
<tbody>
<tr><td>Is total body salt high, low or normal?</td><td>Volume examination; urine sodium off diuretics</td><td>Edema, crackles and raised neck veins versus dry mucosa, postural drop</td></tr>
<tr><td>Is water out of proportion to salt?</td><td>Plasma sodium and osmolality</td><td>Confusion, seizure (hyponatremia); thirst, lethargy (hypernatremia)</td></tr>
<tr><td>Is ADH acting?</td><td>Urine osmolality</td><td>Concentrated urine with a low plasma sodium means ADH is on when it should be off</td></tr>
<tr><td>Can the kidney make dilute urine?</td><td>Solute intake, distal delivery, diuretics, GFR</td><td>Tea and toast, beer potomania, thiazides, advanced CKD</td></tr>
</tbody></table></div>
<p>The two systems collide in hypovolemia. When effective volume falls far enough, the body releases ADH even at a low tonicity, because keeping circulating volume matters more than keeping concentration. That is why a volume-depleted patient, or one with heart failure or cirrhosis, can be both edematous or dry <em>and</em> hyponatremic. A patient can have too much salt and still too much water for that salt.</p>
<p>Two practical rules follow. A low plasma sodium is a water problem until proven otherwise, and its treatment is about water. A swollen patient has a salt problem, and fluid restriction alone will not fix the edema. Module 5 covers volume assessment and Module 6 covers sodium disorders and the house limits for correcting them.</p>
{{key:Ask two separate questions every time: what is the total body salt (volume), and what is the water relative to that salt (sodium concentration)?}}
"""),
        ("clearance", "Estimates and assumptions", "Estimating equations and their assumptions", """
<p>Every estimating equation turns a blood marker into a GFR by assuming things about the patient. The equation is reliable only when those assumptions hold. Stating the assumption before quoting the number is the most useful habit in this module.</p>
<h3>The equations you will meet</h3>
<div class="table-wrap"><table>
<thead><tr><th>Measure</th><th>What it uses</th><th>Key assumption</th><th>Where it fails</th></tr></thead>
<tbody>
<tr><td>CKD Epidemiology Collaboration (CKD-EPI) 2021, creatinine (eGFRcr)</td><td>Creatinine, age, sex; no race term</td><td>Average muscle mass for age and sex; steady state</td><td>Frailty, very low or high muscle mass, AKI, drugs blocking secretion</td></tr>
<tr><td>CKD-EPI 2021, creatinine plus cystatin C (eGFRcr-cys)</td><td>Both markers</td><td>Errors in the two markers partly cancel</td><td>High-dose corticosteroids, thyroid disease and inflammation affect cystatin C; still assumes steady state</td></tr>
<tr><td>European Kidney Function Consortium (EKFC)</td><td>Creatinine, age, sex, scaled to a population&rsquo;s normal creatinine</td><td>A continuous equation from childhood to old age</td><td>Same steady-state and muscle assumptions</td></tr>
<tr><td>Cockcroft&ndash;Gault</td><td>Creatinine, age, weight, sex</td><td>Estimates creatinine clearance, not GFR; derived in 249 patients in 1976, for men with a correction for women</td><td>Obesity, edema, modern standardized creatinine</td></tr>
<tr><td>Kinetic eGFR</td><td>Two or more creatinines over time, an estimate of production and volume</td><td>Creatinine is changing</td><td>Fluid shifts, uncertain production; it is an estimate of an estimate</td></tr>
<tr><td>Measured creatinine clearance</td><td>Timed urine collection and a blood creatinine</td><td>Complete collection</td><td>Missed voids; overestimates GFR because of secretion</td></tr>
</tbody></table></div>
<p>The Kidney Disease: Improving Global Outcomes (KDIGO) 2024 CKD guideline recommends using a validated estimating equation rather than the serum marker alone (1D), creatinine-based eGFR for initial assessment in adults at risk of CKD, with the combination of creatinine and cystatin C to estimate the GFR category when cystatin C is available (1B), and eGFRcr-cys in clinical situations when eGFRcr is less accurate and GFR affects decisions (1C). Its practice points add that GFR should be measured where more accurate ascertainment will change treatment, that a timed urine collection for creatinine clearance can be considered when measured GFR is unavailable, and that race should not be used in computing eGFR.[[ntr02_1]]</p>
<h3>What the evidence shows</h3>
<p>Inker and colleagues developed the 2021 CKD-EPI equations without race in 8,254 participants (creatinine) and 5,352 participants (creatinine and cystatin C), and validated them in 4,050 participants with measured GFR. For all equations, 85% or more of estimates were within 30% of measured GFR, and the combined creatinine-cystatin C equations were more accurate than creatinine alone.[[ntr02_2]] Read that number the other way too: even in research cohorts, up to about one estimate in seven was more than 30% away from the measured value. The EKFC equation, built and validated in about 19,600 people with measured GFR from 13 studies, showed low bias across ages 2 to 90 years; no Black participants were included.[[ntr02_3]] Neither cohort was drawn from Filipino patients, and no Philippine validation study is cited here, so treat any equation as an approximation in a small, older Filipino patient.</p>
<p>Cockcroft and Gault derived their formula from 24-hour creatinine excretion in 249 patients, and it predicted measured creatinine clearance with a correlation of 0.83.[[ntr02_5]] Its weight term makes it sensitive to edema and obesity, and it was developed before creatinine assays were standardized. Many drug labels still state kidney dosing in Cockcroft&ndash;Gault creatinine clearance, which is why you will still use it; keep the label&rsquo;s measure when you follow the label.</p>
<h3>Steady state and the kinetic estimate</h3>
<p>All standard equations assume steady state. After a sudden loss of filtration, creatinine rises over days toward a new plateau; during that rise, an eGFR calculated from today&rsquo;s value overestimates the true GFR. When filtration recovers, creatinine falls slowly and the eGFR underestimates. Chen proposed a kinetic eGFR built from the change between consecutive creatinines, the volume of distribution and the production rate, to estimate GFR while creatinine is changing.[[ntr02_4]] It is a derived estimate from first principles, not a validated measurement, and fluid shifts in the critically ill can mislead it. Use it to sense direction and size, not to dose a narrow-margin drug.</p>
{{formula:<strong>Arithmetic illustration, not a target.</strong> Mrs. Mallari, 78, female, 38 kg.<br>CKD-EPI 2021 eGFRcr at creatinine 0.5 mg/dL = about 96; at 1.1 mg/dL = about 51 mL/min/1.73 m&sup2; (if she were in steady state).<br>Cockcroft&ndash;Gault creatinine clearance at 1.1 mg/dL = (140 &minus; 78) &times; 38 &divide; (72 &times; 1.1) &times; 0.85 = about 25 mL/min.<br>The two answers differ twofold because one ignores her weight and the other uses it; neither is valid while her creatinine is still rising.}}
<h3>Cystatin C in the Philippines</h3>
<p>Cystatin C is produced by all nucleated cells and depends much less on muscle, which is why it helps in the frail, the amputee and the malnourished. In many Philippine provinces it is unavailable or must be sent out, and the family usually pays. Order it when the answer will change a decision, such as whether to start, stop or dose a drug, whether a patient has CKD at all, or whether to list for a procedure, and say so in the request. When it is not available, a timed urine creatinine clearance is the practice-point fallback, with its own errors.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>Children are not small adults: GFR rises through infancy and reaches adult values, scaled to body surface area, by about two years, and muscle mass changes with growth and puberty. Use pediatric equations built on height, such as the Chronic Kidney Disease in Children (CKiD) under-25 (U25) equations, which use age- and sex-specific constants from childhood into young adulthood.[[ntr02_9]] A neonate&rsquo;s first creatinine reflects the mother&rsquo;s. See <a href="attending-pediatric-nephrologist-02-growing-kidney-assessment.html">Attending Pediatric Nephrologist, Module 2</a>.</div>
<p>Stevens and colleagues&rsquo; review remains a clear account of why measured and estimated GFR differ and when each is worth the trouble.[[ntr02_7]]</p>
{{key:Before you quote an eGFR, say which equation, whether the patient is in steady state, and whether muscle mass is average. If any answer is no and the decision matters, use cystatin C, a timed clearance or the trend.}}
"""),
    ],
    "debrief": ["""
<p><strong>Is it normal?</strong> No. Her creatinine has risen 2.2-fold from her baseline, inside the laboratory&rsquo;s range. In a 38-kg woman with little muscle, creatinine production is low, so her baseline of 0.5 mg/dL reflected good filtration, and the rise means she has lost more than half of it. If the rise happened within the last seven days, it meets KDIGO 2012 stage 2 AKI (2.0 to 2.9 times baseline);[[ntr02_10]] if over six months, it is a large fall that needs explaining. Her urine output of about 120 mL in eight hours, about 0.4 mL/kg per hour for a 38-kg woman, has stayed below 0.5 mL/kg per hour for more than six hours, which on its own meets the KDIGO urine output criterion for stage 1. The admitting note should be corrected.</p>
""", """
<p><strong>What the equations say.</strong> CKD-EPI 2021 gives about 51 mL/min/1.73 m&sup2; at 1.1 mg/dL, and Cockcroft&ndash;Gault about 25 mL/min. Both assume steady state, and her creatinine is probably still rising after poor intake, a thiazide and a market &ldquo;pain reliever&rdquo; that is likely an NSAID, so both overestimate her current GFR. CKD-EPI also assumes average muscle mass for her age and sex, which she does not have. Cockcroft&ndash;Gault uses her low weight, which is why it is lower, but it was built for a different era and population. The honest statement is that her GFR is markedly reduced and still uncertain.</p>
""", """
<p><strong>What next.</strong> Repeat the creatinine in 12 to 24 hours to see the direction, and use the change to judge severity (a kinetic estimate helps with the direction). Examine her volume, chart intake, output and weight daily, stop the NSAID and hold the thiazide with the attending&rsquo;s agreement, review every drug for kidney dosing at the lower estimate, and send a urinalysis. Cystatin C would help once she is stable if a decision about chronic kidney function or drug dosing depends on it and the family can manage the cost. A further rise, falling urine output, potassium above the hospital&rsquo;s threshold or a worsening acid-base picture changes the plan to an urgent call.</p>
"""],
    "skills": {"title": "Physiology at the bedside",
               "intro": "Complete with a preceptor during ward rounds or teaching. Sign-off is local.",
               "items": [
                   ("Draws a nephron and labels the transporter and drug class for each of four segments", False),
                   ("Explains the creatinine&ndash;GFR hyperbola using a real patient&rsquo;s baseline and current values", False),
                   ("Calculates CKD-EPI 2021 eGFR and Cockcroft&ndash;Gault clearance for a patient and states which assumption each violates", False),
                   ("Separates a salt (volume) problem from a water (concentration) problem in one patient with hyponatremia or edema", False),
                   ("States when to request cystatin C or a timed clearance, and how the result would change the decision", False),
               ],
               "placement": "Medical ward, renal service or teaching session"},
    "quiz": [
        ("A thin 80-year-old woman has a serum creatinine of 1.0 mg/dL, within the laboratory range. Why may her kidney function still be markedly reduced?",
         ["The laboratory range applies only to men",
          "Creatinine depends on muscle mass, so low production can keep the value low despite a low GFR",
          "Creatinine is not filtered in older adults",
          "Older adults secrete no creatinine"], 1,
         "Serum creatinine reflects production, filtration and secretion. With little muscle, production is low and a reduced GFR can hide inside the normal range. Older adults still filter and secrete creatinine."),
        ("A patient with stable CKD has a creatinine rise of 0.3 mg/dL one week after starting trimethoprim-sulfamethoxazole, with normal urine output and no other change. What is the most likely explanation?",
         ["Acute tubular necrosis",
          "Reduced creatinine secretion in the proximal tubule without a change in GFR",
          "Volume overload",
          "Increased creatinine production"], 1,
         "Trimethoprim blocks tubular creatinine secretion, so creatinine rises without a fall in filtration. Acute tubular necrosis remains possible and should be considered if urine output falls or the rise continues, but the isolated small rise with a known secretion blocker fits best."),
        ("A fellow must decide whether a frail amputee with an eGFRcr of 48 mL/min/1.73 m&sup2; can take a drug restricted below an eGFR of 45. What does KDIGO 2024 recommend in this situation?",
         ["Use creatinine alone",
          "Use eGFRcr-cys when eGFRcr is less accurate and GFR affects a clinical decision (1C), or measure GFR if that will change treatment",
          "Use the Cockcroft&ndash;Gault equation in every case",
          "Add a race coefficient"], 1,
         "Low muscle mass makes eGFRcr unreliable, and the decision hinges on the number. KDIGO 2024 recommends eGFRcr-cys here (1C), with measured GFR where accuracy will change treatment, and advises against race in eGFR."),
        ("A patient in septic shock has creatinines of 1.0 mg/dL yesterday and 1.9 mg/dL today, with urine output of 10 mL per hour. The CKD-EPI eGFR today reads 35. What is the best interpretation?",
         ["The true GFR is about 35",
          "The patient is in steady state, so the eGFR is accurate",
          "Creatinine is still rising, so the eGFR overestimates the current GFR, which may be much lower",
          "The eGFR underestimates the GFR"], 2,
         "Standard equations assume steady state. While creatinine is climbing toward a new plateau, the current value understates the loss, so the eGFR is too high. A kinetic estimate and the urine output give a truer sense of current filtration."),
        ("An older woman on a thiazide, eating mainly tea and bread, has a sodium of 118 mmol/L and no edema. Which statement best explains it?",
         ["She has too much total body sodium",
          "The thiazide impairs dilution in the distal tubule and low solute intake limits water excretion, so water is retained relative to sodium",
          "Her ADH is fully suppressed",
          "Her kidneys are retaining potassium"], 1,
         "Hyponatremia is mainly a water problem. Thiazides act in the distal convoluted tubule, where urine is diluted, and a low-solute diet leaves too little solute to carry water out. Edema would point to excess total sodium instead."),
    ],
    "terms": [
        ("ACE", "Angiotensin-converting enzyme"),
        ("ADH", "Antidiuretic hormone (vasopressin)"),
        ("AKI", "Acute kidney injury"),
        ("ARB", "Angiotensin receptor blocker"),
        ("CKD", "Chronic kidney disease"),
        ("CKD-EPI", "Chronic Kidney Disease Epidemiology Collaboration"),
        ("CKiD", "Chronic Kidney Disease in Children (study)"),
        ("EKFC", "European Kidney Function Consortium"),
        ("ENaC", "Epithelial sodium channel"),
        ("eGFR", "Estimated glomerular filtration rate"),
        ("eGFRcr", "Creatinine-based estimated glomerular filtration rate"),
        ("eGFRcr-cys", "Creatinine and cystatin C&ndash;based estimated glomerular filtration rate"),
        ("GFR", "Glomerular filtration rate"),
        ("KDIGO", "Kidney Disease: Improving Global Outcomes"),
        ("NCC", "Sodium-chloride cotransporter"),
        ("NKCC2", "Sodium-potassium-2-chloride cotransporter, isoform 2"),
        ("NSAID", "Nonsteroidal anti-inflammatory drug"),
        ("SGLT2", "Sodium-glucose cotransporter 2"),
        ("U25", "Under 25 years (CKiD equations)"),
    ],
    "readings": [
        ("kidney-physiology.html", "Kidney Physiology"),
        ("how-to-properly-assess-kidney-function.html", "How to Properly Assess Kidney Function"),
        ("physician-on-duty-02-water-salt-potassium-acid.html", "Physician on Duty, Module 2: Water, salt, potassium and acid"),
        ("attending-pediatric-nephrologist-02-growing-kidney-assessment.html", "Attending Pediatric Nephrologist, Module 2: Assessing the growing kidney"),
    ],
    "calcs": ["calc-egfr-ckd-epi.html", "calc-ekfc-egfr.html", "calc-egfr-cystatin.html", "calc-kegfr.html",
              "calc-cockcroft-gault.html", "calc-measured-crcl.html", "calc-ckid-u25-egfr.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
