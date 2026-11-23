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
<p>Each kidney holds roughly one million nephrons, and each nephron is a filter followed by a long tubule with specialized segments. Knowing what each segment does explains three things a nurse meets daily: where each diuretic acts, why particular electrolyte problems travel together, and why different kidney diseases look different at the bedside.</p>
<div class="table-wrap"><table>
<thead><tr><th>Segment</th><th>Main work</th><th>Medicines that act here</th><th>What failure or blockade looks like</th></tr></thead>
<tbody>
<tr><td>Glomerulus</td><td>Filters plasma; holds back cells and protein</td><td>Renin–angiotensin system inhibitors and sodium-glucose cotransporter-2 (SGLT2) inhibitors lower the pressure inside it</td><td>Albumin or blood in the urine; falling filtration</td></tr>
<tr><td>Proximal tubule</td><td>Reclaims about two thirds of filtered sodium and water, nearly all glucose, amino acids, phosphate, and bicarbonate; secretes many drugs; activates vitamin D</td><td>SGLT2 inhibitors; acetazolamide</td><td>Glucose in the urine with normal blood sugar; low phosphate; acidosis with a normal anion gap</td></tr>
<tr><td>Loop of Henle</td><td>Reclaims about a quarter of filtered sodium; builds the salt gradient that lets the kidney concentrate urine</td><td>Loop diuretics such as furosemide</td><td>Large urine volumes; loss of potassium, magnesium, and calcium</td></tr>
<tr><td>Distal convoluted tubule</td><td>Fine-tunes sodium and calcium</td><td>Thiazide-type diuretics</td><td>Low sodium and potassium; calcium retained</td></tr>
<tr><td>Collecting duct</td><td>Final control of sodium and potassium under aldosterone, of water under antidiuretic hormone, and of acid</td><td>Spironolactone, amiloride; finerenone</td><td>High potassium and acidosis when aldosterone is blocked or absent; dilute urine when antidiuretic hormone does not act</td></tr>
</tbody></table></div>
<p>Two practical consequences follow. First, loop diuretics still work when filtration is low, which is why they are the usual diuretic in advanced kidney disease, although larger doses are needed because less drug reaches the tubule. Second, any medicine that blocks aldosterone or the renin–angiotensin system reduces potassium excretion in the collecting duct, so potassium is checked after these are started or increased.</p>
"""},
    {"after": "nephron", "id": "balance", "nav": "Water, salt, acid", "tag": "Physiology in depth", "h2": "Water, sodium, potassium, and acid: four balances",
     "html": """
<p><strong>Sodium sets volume; water sets concentration.</strong> These are separate systems, and confusing them is a common source of error. The body's sodium content determines how much fluid sits outside the cells, so too much sodium appears as edema, weight gain, and hypertension, not as a high sodium level. The serum sodium <em>concentration</em> reflects water balance: a low sodium level usually means too much water relative to salt, and a high level means too little water. A patient can therefore be swollen with fluid and have a low serum sodium at the same time, and the usual prescribed approach is to limit water, not to give salt; the cause is assessed by the physician.</p>
<p>Three hormone systems run these balances. The renin–angiotensin–aldosterone system responds to low kidney perfusion by constricting blood vessels and retaining sodium. Antidiuretic hormone responds to concentrated blood or low circulating volume by making the collecting duct reabsorb water. Natriuretic peptides, released when the heart is stretched, push the kidney to excrete sodium. In kidney failure the first is often overactive and the last cannot overcome the loss of nephrons, so sodium is retained.</p>
<p><strong>Potassium.</strong> Only about 2% of the body's potassium is outside cells, yet that small pool sets the electrical stability of the heart. Two processes control it. Shifts between cells and blood happen in minutes: insulin and beta-agonists drive potassium into cells, while acidosis, tissue breakdown, and lack of insulin let it leak out. Excretion happens over hours, mostly through the kidney and to a smaller extent the bowel. When kidneys fail, excretion is lost and the patient depends on shifts and on intake, which is why a missed dialysis session, a potassium-rich meal, constipation, or a transfusion of stored red cells can each tip the balance.</p>
<p><strong>Acid.</strong> Normal metabolism of dietary protein generates acid every day. The lungs remove carbon dioxide within minutes; only the kidneys remove the remaining acid and rebuild bicarbonate. When they cannot, serum bicarbonate falls. The body compensates by breathing more deeply and quickly to blow off carbon dioxide, so a patient with significant metabolic acidosis may have deep, sighing respirations without lung disease. On a blood gas the pattern is low pH, low bicarbonate, and low carbon dioxide. In nursing terms: unexplained deep or rapid breathing in a patient with kidney disease is a reason to check a bicarbonate, not only an oxygen saturation.</p>
"""},
    {"after": "evidence", "id": "tests", "nav": "Reading the tests", "tag": "Laboratory interpretation", "h2": "Reading kidney tests without being misled",
     "html": """
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
<p><strong>Urinalysis.</strong> A dipstick and microscopy cost little and say a great deal. Protein on a dipstick mainly reflects albumin but depends on how concentrated the urine is, so a dilute sample can miss significant albuminuria; this is why the ratio is preferred. Blood on the dipstick with red cells on microscopy points to the kidney or urinary tract; blood on the dipstick with <em>no</em> red cells suggests free hemoglobin or myoglobin, as in hemolysis or muscle breakdown. White cells and nitrite suggest infection. A specific gravity that stays near 1.010 whatever the patient drinks means the kidney has lost the ability to concentrate or dilute. Collect a clean midstream sample, send it promptly, and record whether the patient is menstruating or has a catheter, because both change the interpretation.</p>
"""},
    {"after": "bedside", "id": "history", "nav": "History and examination", "tag": "Clinical application", "h2": "The renal history and examination in more depth",
     "html": """
<p>Kidney disease is quiet until late, so much of the history is a search for clues the patient has not connected.</p>
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
<p><strong>Examining volume status.</strong> No single sign is reliable, so findings are combined. Signs of excess: weight above baseline, raised blood pressure, visible neck veins when sitting at 45 degrees, pitting edema (press over the shin or, in a bedbound patient, the sacrum for several seconds), crackles at the lung bases, and breathlessness lying flat. Signs of depletion: weight below baseline, a fall in systolic pressure of 20 mmHg or more or dizziness on standing, a fast pulse, dry mouth and axillae, and reduced urine. Edema with a <em>low</em> blood pressure should prompt thought about low albumin, heart failure, or sepsis and is reported, not treated by assumption.</p>
<p><strong>Standing blood pressure.</strong> Measure after 5 minutes lying or sitting, then again after 1 and 3 minutes of standing.[[bp2021]] Record both, with the pulse, and note symptoms. In people on dialysis, a pressure taken before and after treatment, sitting and standing, is part of every session under the unit protocol (Module 9).</p>
<p><strong>The uremic patient.</strong> Late signs include a sallow or darkened skin tone with scratch marks, a urine-like odor on the breath, twitching or a flapping tremor of the outstretched hands, drowsiness, and a rubbing sound over the heart from pericarditis. These are indications for urgent medical review, because they are among the reasons kidney replacement is started.</p>
"""},
]
QUIZ = [
    {"stem": "A patient with stage 5 chronic kidney disease is breathing deeply at 28 breaths per minute. Oxygen saturation is 98% on room air and the lungs are clear. Which result best explains the breathing pattern?",
     "options": [
         ("Serum bicarbonate of 12 mmol/L", True, "Deep, rapid breathing with clear lungs and normal saturation is the respiratory compensation for metabolic acidosis. A low bicarbonate confirms it and needs prompt medical review."),
         ("Hemoglobin of 105 g/L", False, "Mild anemia causes breathlessness on exertion, not deep sighing respirations at rest."),
         ("Serum sodium of 132 mmol/L", False, "A mildly low sodium does not drive respiration."),
         ("Serum calcium of 2.0 mmol/L", False, "Low calcium may cause tingling or cramps, not this breathing pattern."),
     ],
     "objective": "Recognize the breathing pattern and laboratory picture of metabolic acidosis.", "sources": ["ckd2024"], "flag": ""},
    {"stem": "A 30-year-old man has a urine albumin-to-creatinine ratio of 85 mg/g on a sample collected the morning after a half-marathon. His estimated glomerular filtration rate is normal. What is the most appropriate next step?",
     "options": [
         ("Record chronic kidney disease category A2", False, "A single raised result after heavy exercise does not establish persistent albuminuria."),
         ("Repeat the test on a first-morning sample when he has not exercised heavily and is free of fever or infection", True, "Exercise, fever, and infection raise urine albumin temporarily. Persistence on repeat testing over at least 3 months is required before the result is used to classify disease."),
         ("Request a 24-hour urine collection for creatinine clearance", False, "This does not address whether the albuminuria is transient and is inconvenient and error-prone."),
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
