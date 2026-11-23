# -*- coding: utf-8 -*-
"""Module 1 expansion. EXTRA sections are inserted after the section id given in `after`."""
OBJECTIVES = [
    "Relate each nephron segment to the laboratory and clinical findings that appear when it fails.",
    "Interpret a urinalysis and a urine albumin-to-creatinine ratio, including common false results.",
    "Recognize the breathing pattern and laboratory picture of metabolic acidosis.",
]
EXTRA = [
    {"after": "physiology", "id": "nephron", "nav": "Nephron map", "tag": "Physiology in depth", "h2": "The nephron, segment by segment",
     "html": """
<p>Each kidney holds roughly one million nephrons. Each nephron is a filter followed by a long tubule, and each part of the tubule has its own job. Learn the jobs and three daily puzzles become simple: where each diuretic acts, why some electrolyte problems travel together, and why different kidney diseases look different at the bedside.</p>
<div class="table-wrap"><table>
<thead><tr><th>Segment</th><th>Main work</th><th>Medicines that act here</th><th>What failure or blockade looks like</th></tr></thead>
<tbody>
<tr><td>Glomerulus</td><td>Filters plasma; holds back cells and protein</td><td>Renin–angiotensin system inhibitors and sodium-glucose cotransporter-2 (SGLT2) inhibitors lower the pressure inside it</td><td>Albumin or blood in the urine; falling filtration</td></tr>
<tr><td>Proximal tubule</td><td>Reclaims about two thirds of filtered sodium and water, nearly all glucose, amino acids, phosphate, and bicarbonate; secretes many drugs; activates vitamin D</td><td>SGLT2 inhibitors; acetazolamide</td><td>Glucose in the urine with normal blood sugar; low phosphate; acidosis with a normal anion gap</td></tr>
<tr><td>Loop of Henle</td><td>Reclaims about a quarter of filtered sodium; builds the salt gradient that lets the kidney concentrate urine</td><td>Loop diuretics such as furosemide</td><td>Large urine volumes; loss of potassium, magnesium, and calcium</td></tr>
<tr><td>Distal convoluted tubule</td><td>Fine-tunes sodium and calcium</td><td>Thiazide-type diuretics</td><td>Low sodium and potassium; calcium retained</td></tr>
<tr><td>Collecting duct</td><td>Final control of sodium and potassium under aldosterone, of water under antidiuretic hormone, and of acid</td><td>Spironolactone, amiloride; finerenone</td><td>High potassium and acidosis when aldosterone is blocked or absent; dilute urine when antidiuretic hormone does not act</td></tr>
</tbody></table></div>
<p>Two practical points follow. First, loop diuretics still work when filtration is low. That is why they are the usual diuretic in advanced kidney disease. Larger doses are needed, because less drug reaches the tubule. Second, any medicine that blocks aldosterone or the renin–angiotensin system reduces potassium excretion in the collecting duct. Expect potassium to be checked after these medicines are started or increased.</p>
<p><strong>When a new medicine is started, ask where in the nephron it acts. That tells you which result to watch.</strong></p>
"""},
    {"after": "nephron", "id": "balance", "nav": "Water, salt, acid", "tag": "Physiology in depth", "h2": "Water, sodium, potassium, and acid: four balances",
     "html": """
<p><strong>Sodium sets volume; water sets concentration.</strong> These are separate systems, and mixing them up is a common source of error. The body&rsquo;s sodium content decides how much fluid sits outside the cells. Too much sodium therefore shows up as edema, weight gain, and hypertension, not as a high sodium level. The serum sodium <em>concentration</em> reflects water balance. A low level usually means too much water relative to salt. A high level means too little water. A patient can be swollen with fluid and have a low serum sodium at the same time. The usual prescribed approach is then to limit water, not to give salt. The physician assesses the cause.</p>
<p>Three hormone systems run these balances. The renin–angiotensin–aldosterone system responds to low kidney perfusion: it tightens blood vessels and keeps sodium. Antidiuretic hormone responds to concentrated blood or low circulating volume: it makes the collecting duct take back water. Natriuretic peptides, released when the heart is stretched, push the kidney to excrete sodium. In kidney failure the first system is often overactive, and the last cannot make up for the lost nephrons. Sodium is kept.</p>
<p><strong>Potassium.</strong> Only about 2% of the body&rsquo;s potassium is outside the cells. That small pool sets the electrical stability of the heart. Two processes control it. Shifts between cells and blood happen in minutes: insulin and beta-agonists drive potassium into cells, while acidosis, tissue breakdown, and lack of insulin let it leak out. Excretion takes hours, mostly through the kidney and to a smaller extent the bowel. When the kidneys fail, excretion is lost. The patient then depends on shifts and on intake. That is why a missed dialysis session, a potassium-rich meal, constipation, or a transfusion of stored red cells can each tip the balance.</p>
<p><strong>Acid.</strong> Normal metabolism of dietary protein makes acid every day. The lungs remove carbon dioxide within minutes. Only the kidneys remove the rest of the acid and rebuild bicarbonate. When they cannot, serum bicarbonate falls. The body answers by breathing more deeply and quickly to blow off carbon dioxide. A patient with significant metabolic acidosis may therefore have deep, sighing respirations with healthy lungs. On a blood gas the pattern is low pH, low bicarbonate, and low carbon dioxide.</p>
<p><strong>Unexplained deep or rapid breathing in a patient with kidney disease is a reason to check a bicarbonate, not only an oxygen saturation.</strong></p>
"""},
    {"after": "evidence", "id": "tests", "nav": "Reading the tests", "tag": "Laboratory interpretation", "h2": "Reading kidney tests without being misled",
     "html": """
<p>Every kidney test can mislead you in a predictable way. Know the trap before you report the number.</p>
<div class="table-wrap"><table>
<thead><tr><th>Test</th><th>What it tells you</th><th>What misleads</th></tr></thead>
<tbody>
<tr><td>Serum creatinine</td><td>Waste from muscle, cleared by filtration; rises as filtration falls</td><td>Low in small, frail, or malnourished people, so a "normal" value may hide reduced function; raised by large muscle mass, a cooked-meat meal, creatine supplements, and some medicines (trimethoprim, cimetidine) that block its secretion without harming the kidney</td></tr>
<tr><td>Estimated glomerular filtration rate</td><td>Creatinine adjusted for age and sex; the basis for staging and drug dosing</td><td>Valid only when creatinine is stable; unreliable in acute kidney injury, amputees, pregnancy, and extremes of body size. Cystatin C can be added when a more accurate estimate would change a decision[[ckd2024]]</td></tr>
<tr><td>Blood urea nitrogen</td><td>Waste from protein breakdown</td><td>Raised by dehydration, bleeding into the gut, steroids, and high protein intake; lowered by liver disease and malnutrition</td></tr>
<tr><td>Urine albumin-to-creatinine ratio</td><td>Albumin leak corrected for urine concentration; a first-morning sample is preferred</td><td>Temporarily raised by fever, urinary tract infection, heavy exercise in the previous day, menstruation, and uncontrolled blood sugar or heart failure. An abnormal result is repeated before it is acted on[[ckd2024]]</td></tr>
<tr><td>Potassium</td><td>Excretion and shifts</td><td>Falsely high when the sample is hemolyzed, drawn with a tight tourniquet and fist clenching, delayed in transport, or taken from an arm with an infusion containing potassium</td></tr>
<tr><td>Bicarbonate (total carbon dioxide)</td><td>Acid–base reserve</td><td>Falls if the tube is underfilled or left open</td></tr>
</tbody></table></div>
<p><strong>Urinalysis.</strong> A dipstick and microscopy cost little and say a great deal. Protein on a dipstick mainly reflects albumin, but it depends on how concentrated the urine is. A dilute sample can miss significant albuminuria, which is why the ratio is preferred. Blood on the dipstick with red cells on microscopy points to the kidney or urinary tract. Blood on the dipstick with <em>no</em> red cells suggests free hemoglobin or myoglobin, as in hemolysis or muscle breakdown. White cells and nitrite suggest infection. A specific gravity that stays near 1.010 whatever the patient drinks means the kidney can no longer concentrate or dilute.</p>
<p>Collect a clean midstream sample and send it promptly. Record whether the patient is menstruating or has a catheter, because both change the interpretation.</p>
<p><strong>A suspicious result is still reported. Report it with the sampling details, and let the repeat test settle it.</strong></p>
"""},
    {"after": "bedside", "id": "history", "nav": "History and examination", "tag": "Clinical application", "h2": "The renal history and examination in more depth",
     "html": """
<p>Kidney disease is quiet until late. Much of the history is a search for clues the patient has not connected.</p>
<div class="table-wrap"><table>
<thead><tr><th>Ask about</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Diabetes, hypertension, gout, kidney stones, recurrent urinary infections, autoimmune disease, hepatitis B or C</td><td>The common causes and associations of kidney disease</td></tr>
<tr><td>Family members with kidney failure, dialysis, or polycystic kidneys</td><td>Hereditary disease; also possible living donors later</td></tr>
<tr><td>Urine: volume, getting up at night, foaming, blood, poor stream, pain</td><td>Night-time urination is an early sign of lost concentrating ability; foam suggests protein; a poor stream suggests obstruction</td></tr>
<tr><td>Swelling of the face on waking or the legs by evening; shoes or rings tighter; weight change</td><td>Sodium and water retention</td></tr>
<tr><td>Appetite, nausea, metallic taste, itch, cramps, restless legs, poor sleep, difficulty concentrating</td><td>Uremic symptoms, usually appearing when filtration is severely reduced</td></tr>
<tr><td>Breathlessness on exertion or lying flat; chest pain</td><td>Fluid overload, anemia, heart disease, or pericarditis</td></tr>
<tr><td>All medicines, including pain relievers, herbal products, and supplements; recent contrast studies</td><td>Avoidable kidney injury</td></tr>
<tr><td>Occupation, wading in floodwater, recent fever</td><td>Heat stress and, in the Philippines, leptospirosis</td></tr>
</tbody></table></div>
<p><strong>Examining volume status.</strong> No single sign is reliable, so you combine them. Signs of excess: weight above baseline, raised blood pressure, visible neck veins with the patient sitting at 45 degrees, pitting edema, crackles at the lung bases, and breathlessness lying flat. Test for pitting by pressing over the shin for several seconds, or over the sacrum in a patient in bed. Signs of depletion: weight below baseline, a fall in systolic pressure of 20 mmHg or more or dizziness on standing, a fast pulse, dry mouth and axillae, and less urine. Edema with a <em>low</em> blood pressure should make you think of low albumin, heart failure, or sepsis. Report it. Do not treat it by assumption.</p>
<p><strong>Standing blood pressure.</strong> Measure after 5 minutes lying or sitting, then again after 1 and 3 minutes of standing.[[bp2021]] Record both readings, the pulse, and any symptoms. For people on dialysis, pressures before and after treatment, sitting and standing, are part of every session under the unit protocol (Module 9).</p>
<p><strong>The uremic patient.</strong> Late signs include a sallow or darkened skin with scratch marks, a urine-like odor on the breath, twitching or a flapping tremor of the outstretched hands, drowsiness, and a rubbing sound over the heart from pericarditis. Each calls for urgent medical review. These are among the reasons kidney replacement therapy is started.</p>
<p><strong>No single sign settles volume status. Put the weight, the pressure, the breathing, and the edema together before you name a judgment.</strong></p>
"""},
]
QUIZ = [
    {"stem": "A patient with stage 5 chronic kidney disease is breathing deeply at 28 breaths per minute. Oxygen saturation is 98% on room air and the lungs are clear. Which result best explains the breathing pattern?",
     "options": [
         ("Serum bicarbonate of 12 mmol/L", True, "Deep, rapid breathing with clear lungs and normal saturation is the lungs compensating for metabolic acidosis. A low bicarbonate confirms it and needs prompt medical review."),
         ("Hemoglobin of 105 g/L", False, "Mild anemia causes breathlessness on exertion, not deep sighing respirations at rest."),
         ("Serum sodium of 132 mmol/L", False, "A mildly low sodium does not drive breathing."),
         ("Serum calcium of 2.0 mmol/L", False, "Low calcium may cause tingling or cramps, not this breathing pattern."),
     ],
     "objective": "Recognize the breathing pattern and laboratory picture of metabolic acidosis.", "sources": ["ckd2024"], "flag": ""},
    {"stem": "A 30-year-old man has a urine albumin-to-creatinine ratio of 85 mg/g on a sample collected the morning after a half-marathon. His estimated glomerular filtration rate is normal. What is the most appropriate next step?",
     "options": [
         ("Record chronic kidney disease category A2", False, "A single raised result after heavy exercise does not establish persistent albuminuria."),
         ("Repeat the test on a first-morning sample when he has not exercised heavily and is free of fever or infection", True, "Exercise, fever, and infection raise urine albumin for a short time. The result must persist on repeat testing over at least 3 months before it is used to classify disease."),
         ("Request a 24-hour urine collection for creatinine clearance", False, "This does not answer whether the albuminuria is transient, and it is inconvenient and error-prone."),
         ("Tell him the result is normal for athletes and needs no follow-up", False, "The result may be transient, but it should be confirmed, not dismissed."),
     ],
     "objective": "Interpret a urinalysis and a urine albumin-to-creatinine ratio, including common false results.", "sources": ["ckd2024"], "flag": ""},
]
TERMS = [
    ("Nephron", "The working unit of the kidney: a glomerulus and its tubule."),
    ("Anion gap", "A calculation from routine electrolytes that helps sort the causes of metabolic acidosis."),
    ("Pitting edema", "Swelling that keeps a dent after firm finger pressure."),
]
FLAGS = ["Nephron-segment table lists drug classes for orientation; it is not prescribing guidance."]
