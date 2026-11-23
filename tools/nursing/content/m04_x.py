# -*- coding: utf-8 -*-
OBJECTIVES = [
    "Stage acute kidney injury and identify patients at risk before injury occurs.",
    "List the indications for urgent kidney support.",
    "Describe the nursing care of a patient receiving acute hemodialysis or continuous therapy.",
    "Plan follow-up after an episode of acute kidney injury.",
]
EXTRA = [
    {"after": "physiology", "id": "staging", "nav": "Staging and risk", "tag": "Classification in practice", "h2": "Staging, and who is at risk",
     "html": """
<div class="table-wrap"><table>
<thead><tr><th>Stage</th><th>Serum creatinine</th><th>Urine output</th></tr></thead>
<tbody>
<tr><td>1</td><td>1.5 to 1.9 times baseline, or a rise of 0.3 mg/dL or more</td><td>Below 0.5 mL/kg per hour for 6 to 12 hours</td></tr>
<tr><td>2</td><td>2.0 to 2.9 times baseline</td><td>Below 0.5 mL/kg per hour for 12 hours or more</td></tr>
<tr><td>3</td><td>3.0 times baseline or more, or 4.0 mg/dL or higher, or start of kidney replacement</td><td>Below 0.3 mL/kg per hour for 24 hours or more, or no urine for 12 hours</td></tr>
</tbody></table></div>
<p>The patient is placed in the highest stage reached by either criterion.[[aki2012]] Each higher stage is associated with higher mortality and a greater chance of lasting kidney damage. That is why even stage 1 is reported.</p>
<p><strong>Calculating urine output.</strong> The threshold is set by the patient&rsquo;s own weight. For a 60 kg adult, 0.5 mL/kg per hour is 30 mL per hour, or 180 mL over 6 hours. Total the output over the period, then divide by the hours and by the weight. A single low hour after a catheter change is not AKI. Six low hours in a row are.</p>
<p><strong>Who is at risk.</strong> AKI is far easier to prevent than to treat. Risk comes from two sides: what the patient brings, and what happens to the patient.</p>
<div class="table-wrap"><table>
<thead><tr><th>Susceptibility (the patient)</th><th>Exposure (the event)</th></tr></thead>
<tbody>
<tr><td>Chronic kidney disease (CKD)</td><td>Sepsis</td></tr>
<tr><td>Age over 65</td><td>Major surgery, especially cardiac and vascular</td></tr>
<tr><td>Diabetes, heart failure, liver disease</td><td>Volume loss: vomiting, diarrhea, bleeding, burns</td></tr>
<tr><td>Dehydration or poor oral intake</td><td>Low blood pressure or shock</td></tr>
<tr><td>Medicines that impair kidney defenses</td><td>Kidney-toxic medicines and contrast media</td></tr>
<tr><td>Previous AKI</td><td>Urinary obstruction; muscle breakdown; envenomation</td></tr>
</tbody></table></div>
<p>When a patient with several susceptibilities meets an exposure, your bundle is simple. Measure urine output and weight daily. Keep an accurate fluid balance. Make sure kidney function is checked. Question every kidney-toxic medicine. Report early.[[aki2012]]</p>
<p><strong>Susceptibility plus exposure is the signal to start counting.</strong></p>
"""},
    {"after": "evidence", "id": "management", "nav": "Supportive care", "tag": "Evidence", "h2": "Supportive care: what helps and what does not",
     "html": """
<p><strong>Fluids.</strong> In a patient short of volume, fluid restores filtration pressure. In one who is not, the failing kidney cannot excrete it, and it collects in the lungs and tissues. Fluid overload in AKI is associated with higher mortality in observational studies, though sicker patients also receive more fluid. Fluids are prescribed against an assessed need and reassessed, not continued by default. The KDIGO 2012 guideline suggests isotonic crystalloids rather than colloids (albumin or starches) for initial volume expansion when there is no hemorrhagic shock (grade 2B).[[aki2012]] Your part is the reassessment: weight, cumulative balance, breathing, and edema, reported before the next bag is hung.</p>
<p><strong>Diuretics and dopamine.</strong> The guideline recommends against diuretics to prevent AKI (grade 1B), suggests against them to treat AKI except for fluid overload (grade 2C), and recommends against low-dose dopamine (grade 1A).[[aki2012]] A good urine output after furosemide shows that some tubules still respond, not that the kidney has recovered.</p>
<p><strong>Finding the cause</strong> uses a small set of tests. On urine microscopy, granular &ldquo;muddy brown&rdquo; casts suggest tubular injury, and red-cell casts suggest glomerular inflammation. A kidney ultrasound excludes obstruction. A bedside bladder scan takes a minute and can end the search.</p>
<p><strong>When kidney support is started urgently.</strong> The accepted indications are complications that threaten life and have not responded to medical treatment:</p>
<ul>
<li>Potassium that remains dangerously high, or that comes with electrocardiogram (ECG) changes</li>
<li>Fluid overload with pulmonary edema that does not respond to diuretics</li>
<li>Severe metabolic acidosis</li>
<li>Uremic complications: pericarditis, encephalopathy, or bleeding</li>
<li>Certain poisonings and drug overdoses that dialysis can remove</li>
</ul>
<p>Without these, starting early does not help. The STARRT-AKI trial randomized 3,019 critically ill adults with severe AKI to start kidney support within 12 hours or to wait for a conventional indication. At 90 days, 43.9% of the early group and 43.7% of the standard group had died. Among survivors, 10.4% against 6.0% still depended on dialysis, and adverse events were more common with the early start (23.0% against 16.5%).[[starrt2020]] The decision rests on the trajectory and the whole clinical picture.[[ostermann2020]]</p>
<p><strong>The emergency treatment of hyperkalemia,</strong> for orientation. Doses and sequence are prescribed. The table explains what each step does and what you watch for.[[clase2020]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>Effect</th><th>What you monitor</th></tr></thead>
<tbody>
<tr><td>Intravenous calcium</td><td>Stabilizes heart muscle within minutes; lasts 30 to 60 minutes; does not lower potassium</td><td>Continuous ECG; a secure, patent vein, since calcium damages tissue if it leaks; a repeat ECG after the dose</td></tr>
<tr><td>Insulin with glucose</td><td>Moves potassium into cells within 15 to 30 minutes; lasts a few hours</td><td>Blood glucose before, then hourly for several hours; hypoglycemia is common and can be delayed</td></tr>
<tr><td>Inhaled beta-agonist</td><td>Moves potassium into cells; adds to insulin</td><td>Heart rate and tremor</td></tr>
<tr><td>Sodium bicarbonate</td><td>Useful mainly when acidosis is present</td><td>Sodium and fluid load</td></tr>
<tr><td>Removal: diuretic if urine is being made, potassium binder, dialysis</td><td>The only steps that take potassium out of the body</td><td>Repeat potassium as ordered; prepare for dialysis</td></tr>
</tbody></table></div>
<p>The first three steps wear off, and potassium rebounds unless removal follows.</p>
<p><strong>A repeat potassium after the first treatments is part of the plan, not an optional extra.</strong></p>
"""},
    {"after": "bedside", "id": "acute-krt", "nav": "Caring during kidney support", "tag": "Clinical application", "h2": "Nursing care during acute hemodialysis and continuous therapy",
     "html": """
<p>Advanced Module 13 covers continuous therapy in depth: modes, dose, citrate and heparin anticoagulation, hourly fluid accounting, circuit troubleshooting, and complications.</p>
<p><strong>Access.</strong> Acute treatment uses a temporary, non-tunneled dialysis catheter. The KDIGO 2012 guideline lists an order of preference for the vein, as an ungraded statement: the right internal jugular first, then a femoral vein, then the left internal jugular, and the subclavian last.[[aki2012]] The subclavian is avoided because narrowing there can ruin future fistula options in that arm. The catheter is used for dialysis only, handled with full aseptic technique (Module 7), and checked each shift for redness, discharge, bleeding, and position. A femoral catheter limits hip flexion. When the patient sits up, a kink shows as a pressure alarm.</p>
<p><strong>Continuous renal replacement therapy (CRRT) at the bedside.</strong></p>
<div class="table-wrap"><table>
<thead><tr><th>What to watch</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Hourly fluid balance against the prescribed net removal</td><td>Small hourly errors add up over 24 hours into liters</td></tr>
<tr><td>Circuit pressures and their trend</td><td>A rising pressure across the filter warns of clotting hours before the circuit stops; a sudden access-pressure alarm suggests a kinked or malpositioned catheter</td></tr>
<tr><td>Anticoagulation</td><td>With heparin, bleeding and clotting tests as ordered. With regional citrate, the patient&rsquo;s ionized calcium is watched closely, because citrate binds calcium; tingling, spasm, a low blood pressure, or a prolonged QT interval is reported at once</td></tr>
<tr><td>Temperature</td><td>Blood cools in the circuit; continuous therapy can cause hypothermia and can also hide a fever</td></tr>
<tr><td>Electrolytes</td><td>Continuous clearance removes potassium, phosphate, and magnesium; low levels are common after the first day and need replacement by order</td></tr>
<tr><td>Medicines and nutrition</td><td>Many antibiotics are removed and need dose review by the prescriber; amino acids and water-soluble vitamins are lost</td></tr>
<tr><td>Downtime</td><td>Time off the circuit for scans, clotting, or bag changes reduces the delivered dose; record it</td></tr>
</tbody></table></div>
<p><strong>Acute intermittent hemodialysis</strong> in an unstable patient uses the measures for preventing low blood pressure described in Module 9, with closer checks: slower blood flow at the start, cooler dialysate, a modest fluid goal, and blood pressure every 15 minutes or as ordered. A first treatment in a patient with very high urea is deliberately short and gentle, to avoid dialysis disequilibrium (Module 9).</p>
<p><strong>On continuous therapy, the hourly balance is the treatment. Record it as carefully as a medicine.</strong></p>
"""},
    {"after": "acute-krt", "id": "recovery", "nav": "Recovery and follow-up", "tag": "Clinical application", "h2": "Recovery, discharge, and the Philippine picture",
     "html": """
<p><strong>The recovery phase.</strong> As the tubules heal, filtration returns before the tubules can concentrate urine again. Output may rise to several liters a day. The risks then reverse. Dehydration, low potassium, and low sodium replace overload and high potassium. Daily weights and electrolyte checks continue, and fluid replacement is adjusted to output by order.</p>
<p><strong>After discharge.</strong> A person who has had AKI is at higher risk of CKD, of another episode, and of cardiovascular events. The KDIGO 2012 guideline advises, as an ungraded statement, that patients be evaluated 3 months after AKI to see whether it has resolved, become CKD, or worsened existing CKD.[[aki2012]] Check that the discharge plan contains four things:</p>
<ul>
<li>The diagnosis &ldquo;acute kidney injury,&rdquo; written in words the patient has been told</li>
<li>A date for a repeat creatinine and urine albumin test</li>
<li>A reconciled medication list that states which medicines were stopped, and whether and when each is to be restarted</li>
<li>Advice to tell any future prescriber about the AKI, and to seek care early during a dehydrating illness</li>
</ul>
<p><strong>Infectious causes seen in the Philippines.</strong> Leptospirosis follows exposure to floodwater or soil contaminated by animal urine. It typically presents with fever, muscle pain, especially in the calves, red eyes, and jaundice. Its kidney injury often comes with a normal or high urine output and a <em>low</em> potassium, and severe cases can bleed into the lungs. Severe dengue injures the kidney through shock, muscle breakdown, and bleeding. In both, early recognition, careful fluid balance, and early referral to a center with kidney support matter. Ask every patient with fever and a rising creatinine about wading, rodents, farming, and recent typhoons.</p>
<p><strong>A normal creatinine at discharge is not the end of the story. Make sure the 3-month check is booked.</strong></p>
"""},
]
QUIZ = [
    {"stem": "A patient with AKI is given insulin with glucose for a potassium of 6.6 mmol/L at 2:00 p.m. Which nursing action matters most over the next few hours?",
     "options": [
         ("Check blood glucose regularly, because hypoglycemia is common and may be delayed", True, "Insulin keeps acting after the glucose is used, particularly when the kidneys are not clearing insulin. Glucose is checked for several hours, and potassium is rechecked as ordered."),
         ("Stop cardiac monitoring once the infusion is complete", False, "The effect is temporary, and potassium can rebound."),
         ("Encourage oral potassium-rich fluids to prevent overcorrection", False, "This would worsen hyperkalemia."),
         ("Assume the potassium problem is solved", False, "Insulin shifts potassium into cells for a few hours. It does not remove it from the body."),
     ],
     "objective": "Monitor a patient at risk and recognize the findings that require urgent escalation.", "sources": ["clase2020"], "flag": "Monitoring interval and duration follow the hospital protocol."},
    {"stem": "Which finding in a patient with stage 3 AKI is an indication for urgent kidney support?",
     "options": [
         ("A creatinine that has risen but with normal potassium, clear lungs, and adequate urine output", False, "A creatinine value alone is not an indication. The decision rests on complications and trajectory."),
         ("Blood urea nitrogen that has doubled, with no symptoms", False, "Urea alone, without uremic complications, does not call for urgent treatment."),
         ("Pulmonary edema with low oxygen saturation that has not improved after intravenous diuretic", True, "Fluid overload that does not respond to diuretics is a classic urgent indication, together with refractory hyperkalemia, severe acidosis, and uremic complications."),
         ("A request from the family to start dialysis early", False, "In STARRT-AKI, an early start without an indication did not lower 90-day mortality and left more survivors dependent on dialysis. The family&rsquo;s concerns are addressed through discussion."),
     ],
     "objective": "List the indications for urgent kidney support.", "sources": ["aki2012", "starrt2020", "ostermann2020"], "flag": ""},
]
TERMS = [
    ("Ionized calcium", "The active, unbound fraction of blood calcium."),
    ("Regional citrate anticoagulation", "Citrate infused into the circuit to prevent clotting by binding calcium, with calcium replaced to the patient."),
    ("Polyuric phase", "A period of high urine output during recovery from tubular injury."),
]
FLAGS = [
    "Hyperkalemia table gives effects and timings for orientation; no doses are stated. Nephrologist review required.",
    "Catheter site preference is from KDIGO 2012 (ungraded); local practice may differ.",
    "KDIGO 2012 grades quoted (crystalloids 2B, diuretics 1B and 2C, low-dose dopamine 1A, CRRT for unstable patients 2B; catheter site, 3-month evaluation, and complementary use ungraded) were checked against the KDIGO AKI guideline summary.",
    "Leptospirosis and dengue paragraph is general clinical knowledge without a cited source; add a Philippine guideline reference or have it confirmed by the reviewer.",
    "Statement that fluid overload in AKI is associated with higher mortality is observational and uncited; reviewer may wish to add a source.",
]
