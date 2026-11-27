# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 2: Why children's kidneys fail, and how a modality is chosen. POD voice. Fictional cases."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Explain how the causes of kidney failure in children differ by age and region, and why that matters at the chair.",
        "Describe how chronic kidney disease (CKD) acts on a growing body: water and salt handling, growth, bone, blood and blood pressure.",
        "Estimate kidney function in a child with the bedside CKiD equation and explain its limits.",
        "Support a fair modality conversation about peritoneal dialysis (PD), hemodialysis and preemptive transplant.",
    ],
    "big": """
<p>Adults usually reach kidney failure through diabetes or high blood pressure, after decades. Children usually reach it through kidneys that formed differently, inherited disease, or glomerular disease. Many of these children still pass large volumes of urine. That single fact changes how you think about fluid, salt and growth at every session.</p>
<p>Your work in this module is to understand why this child&rsquo;s kidneys failed, because the cause predicts the urine output, the salt losses, the bone problems and the questions the family will ask.</p>
{{plain:Picture two leaky buckets. The adult bucket has lost its holes; it fills between sessions and must be emptied. Many children with kidneys that formed abnormally have a bucket full of holes: they pour out dilute urine and salt, and run dry if fluid or salt is restricted the adult way.}}
<p>The picture has a limit. A child who passes a lot of urine can still retain potassium, phosphate, acid and waste, because the failing kidney cannot concentrate them. Volume and clearance are different jobs. A child may lose too much water and salt while keeping too much potassium.</p>
{{cards:Key terms for this module|CAKUT::Congenital anomalies of the kidney and urinary tract: kidneys or drainage that formed abnormally.|Polyuria::Passing large volumes of dilute urine.|Glomerulopathy::Disease of the glomerulus, the kidney&rsquo;s filter.|Preemptive transplant::A kidney transplant before dialysis starts.|Residual kidney function::The work the child&rsquo;s own kidneys still do.}}
""",
    "case": {"title": "The toddler who drinks all day", "html": """
<p><strong>Gab Villanueva, 3</strong>, was born with posterior urethral valves and has CKD stage 5. He weighs 12 kilograms. His mother, <strong>Liza</strong>, says he drinks constantly, soaks a diaper every hour, and cries for water at night. A relative told her to stop giving water &ldquo;because his kidneys are weak&rdquo;.</p>
<p>The pediatric nephrologist is discussing starting dialysis. Liza asks the nurse, <strong>Ana</strong>, whether PD or hemodialysis is &ldquo;better&rdquo;, and whether Gab can have her kidney instead.</p>
""", "questions": ["Why might restricting Gab&rsquo;s water be dangerous?",
                  "What makes PD, hemodialysis or transplant more or less suitable for him?",
                  "What is Ana&rsquo;s role in Liza&rsquo;s questions, and what is not?"]},
    "sections": [
        ("causes-by-age", "Causes", "Causes change with age and region", """
<p>A registry analysis of 23,620 children starting maintenance kidney replacement therapy in 80 countries found that the causes differ by age and by region.[[pdn_borzych2026]] In younger children, CAKUT and hereditary kidney diseases predominate. Adolescents more often have immune-mediated glomerular disease. In Southeast Asia, immune-mediated glomerulopathy was the most common cause overall, and in 14% of children worldwide the cause was unknown.</p>
{{fig:pdn02_a}}
<div class="table-wrap"><table>
<thead><tr><th>Group of causes</th><th>Typical age</th><th>What you may notice at the chair</th></tr></thead>
<tbody>
<tr><td>CAKUT (dysplasia, valves, reflux)</td><td>Infancy and early childhood</td><td>High urine output, salt loss, urinary infections, bladder care needs</td></tr>
<tr><td>Hereditary disease (for example cystinosis, nephronophthisis)</td><td>Childhood</td><td>Polyuria, growth failure, extra medicines; siblings may be affected</td></tr>
<tr><td>Immune-mediated glomerulopathy (for example nephrotic syndrome, lupus)</td><td>Later childhood and adolescence</td><td>Low urine output, edema, high blood pressure, immunosuppression history</td></tr>
</tbody></table></div>
<p>Philippine pediatric data are scarce. One tertiary government hospital described 86 children with leptospirosis and acute kidney injury; 62% were oliguric, and PD was started in 36% of the oliguric children.[[pdn_anacleto2014]] Acute causes like this matter for Module 16; chronic causes shape everything else.</p>
{{key:Ask what caused this child&rsquo;s kidney failure. The answer predicts urine output, salt losses and what the family fears.}}
"""),
        ("ckd-in-a-growing-body", "CKD and growth", "CKD in a growing body", """
<p>In an adult, CKD damages an organ. In a child, it also interferes with growth. The failing kidney does several jobs at once, and each failure has a bedside sign.</p>
<div class="table-wrap"><table>
<thead><tr><th>Normal job</th><th>What breaks in CKD</th><th>What you may see</th></tr></thead>
<tbody>
<tr><td>Balance water and salt</td><td>Concentrating ability fails (polyuric causes) or excretion fails (oliguric causes)</td><td>Dehydration or edema; thirst; blood pressure changes</td></tr>
<tr><td>Remove acid</td><td>Acid accumulates; bone buffers it</td><td>Poor appetite, poor growth, fast breathing when severe</td></tr>
<tr><td>Make active vitamin D and handle phosphate</td><td>Phosphate rises, calcium and parathyroid hormone are disturbed</td><td>Bone pain, bowed legs, slow growth</td></tr>
<tr><td>Make erythropoietin</td><td>Anemia</td><td>Pallor, tiredness, poor school stamina</td></tr>
<tr><td>Clear waste</td><td>Uremia</td><td>Nausea, poor feeding, poor concentration</td></tr>
</tbody></table></div>
<h3>Estimating kidney function in a child</h3>
<p>Adult equations do not work for children. The bedside CKiD equation, derived in 349 children aged 1 to 16 years with CKD, estimates glomerular filtration rate (GFR) as 0.413 &times; height in centimeters &divide; serum creatinine in mg/dL.[[pdn_schwartz2009]] It needs an accurate height, which is one more reason to measure height carefully. It is an estimate with error; trends matter more than one value.</p>
<p><strong>Worked example.</strong> A 120 cm child with creatinine 2.0 mg/dL: 0.413 &times; 120 &divide; 2.0 = about 25 mL/min/1.73 m&sup2;. The Kidney Disease: Improving Global Outcomes (KDIGO) 2024 guideline stages CKD by GFR and albuminuria in children as well as adults.[[kdigo_ckd2024]]</p>
{{key:A child with kidney failure may pass plenty of urine and still need dialysis. Volume is not clearance.}}
"""),
        ("choosing-a-modality", "Modality", "Choosing a modality with the family", """
<p>There is no single best modality for every child. PD is often chosen for infants and young children because it avoids needles and repeated blood loss, can be done at home overnight, and preserves the veins a child may need later. Hemodialysis is often chosen when PD is not possible (abdominal surgery, no caregiver able to do PD, membrane failure) or for older children and adolescents. Preemptive transplant, when a suitable donor is available and the child is ready, avoids dialysis altogether.[[pdn_fischbach2005]]</p>
{{fig:pdn02_b}}
<div class="table-wrap"><table>
<thead><tr><th>Factor</th><th>Leans toward PD</th><th>Leans toward hemodialysis</th></tr></thead>
<tbody>
<tr><td>Age and size</td><td>Infants and small children</td><td>Older children and adolescents, if access is feasible</td></tr>
<tr><td>Home and caregivers</td><td>A trained, available caregiver; space and clean water</td><td>No caregiver able to do PD reliably</td></tr>
<tr><td>Distance</td><td>Far from a pediatric hemodialysis unit</td><td>Lives near the unit</td></tr>
<tr><td>Abdomen</td><td>Intact peritoneum</td><td>Previous major surgery, ostomies, hernias</td></tr>
<tr><td>School and activity</td><td>Daytime free with overnight cycling</td><td>Can attend sessions without losing school</td></tr>
</tbody></table></div>
<p>In the Philippines, PhilHealth piloted a pediatric automated PD benefit at the National Kidney and Transplant Institute (NKTI), the University of the Philippines&ndash;Philippine General Hospital (UP-PGH) and the Philippine Children&rsquo;s Medical Center (PCMC), extended to July 31, 2026.[[pc_pa2025_0074]][[pd_ph_pa2026]] Its status after that date was not verified for this track. Never promise a family a benefit you have not confirmed.</p>
{{scene:Clinic room, Tuesday|<p>Liza asks Ana which is better. Ana answers: &ldquo;Both can keep Gab well. The doctor will help you choose. Can I tell you what each one asks of your family, so you can bring your questions?&rdquo; She describes nightly cycling at home and three trips a week to the unit, and she notes that Liza could be evaluated as a donor.</p><p class="tc-scene-take">The nurse explains what each option asks of the family; the nephrologist and family make the choice.</p>}}
{{key:The best modality is the one this family can do safely, that keeps the child growing, and that keeps options open.}}
"""),
    ],
    "debrief": ["""
<p><strong>Why restricting water is dangerous.</strong> Gab&rsquo;s kidneys formed abnormally. Like many children with CAKUT, he passes large volumes of dilute urine and loses salt. Withholding water could dehydrate him quickly. Ana tells Liza not to restrict fluids and asks the nephrologist to address the relative&rsquo;s advice directly.</p>
<p><strong>Modality fit.</strong> At 12 kilograms, Gab is a typical PD candidate: no needles, care at home, veins preserved. His valves history means the team will check his bladder and abdomen. Hemodialysis would need a central line and a small-volume circuit. Liza&rsquo;s offer to donate is a reason to start the transplant evaluation early.</p>
<p><strong>Ana&rsquo;s role.</strong> She explains what each option demands, answers practical questions, and passes the clinical choice and the donor question to the nephrologist and transplant team. She does not choose for the family.</p>
"""],
    "skills": {"title": "Cause, function and modality", "intro": "Use fictional charts.",
               "items": [("Identifies the cause of kidney failure and states its expected urine output pattern", False),
                         ("Calculates bedside CKiD eGFR with units and an independent check", True),
                         ("Explains in plain words what PD and hemodialysis each ask of a family", False),
                         ("Refers the modality decision and donor questions to the nephrologist and transplant team", True)]},
    "quiz": [
        ('Which causes predominate in younger children starting kidney replacement therapy?',
         ['Diabetes and hypertension', 'Lupus only', 'CAKUT and hereditary disease', 'Drug toxicity'], 2,
         'The global registry analysis found CAKUT and hereditary disease predominate in young children.'),
        ('In Southeast Asia, which cause was most common in the 2026 registry analysis?',
         ['CAKUT', 'Diabetes', 'Unknown in every case', 'Immune-mediated glomerulopathy'], 3,
         'Immune-mediated glomerular disease was most common in Southeast Asia.'),
        ('A 3-year-old with dysplastic kidneys soaks diapers hourly. Why is water restriction risky?',
         ['He may be polyuric and salt-losing and become dehydrated', 'It is never risky', 'It causes edema', 'It raises potassium only'], 0,
         'Volume and clearance are different jobs.'),
        ('A polyuric child can still need dialysis because:',
         ['Urine volume equals clearance', 'The kidney cannot concentrate potassium, phosphate, acid and waste', 'Polyuria cures CKD', 'Dialysis increases urine'], 1,
         'Dilute urine carries little waste.'),
        ('The bedside CKiD equation uses:',
         ['Age and weight', 'Cystatin only', 'Height and serum creatinine', 'Urine volume'], 2,
         'eGFR = 0.413 &times; height (cm) &divide; creatinine (mg/dL).'),
        ('Height 120 cm, creatinine 2.0 mg/dL. Bedside CKiD eGFR is about:',
         ['12', '50', '100', '25'], 3,
         '0.413 &times; 120 &divide; 2.0 &asymp; 24.8 mL/min/1.73 m&sup2;.'),
        ('Why does CKD cause poor growth?',
         ['Acidosis, bone-mineral disturbance, anemia, uremia and poor intake act together', 'Only because of diet', 'It does not', 'Because of dialysis alone'], 0,
         'Several failing kidney jobs converge on growth.'),
        ('Why is PD often chosen for infants?',
         ['It needs no caregiver', 'It avoids needles and blood loss, works at home and preserves veins', 'It removes more potassium', 'Hemodialysis is illegal in infants'], 1,
         'These are the usual reasons; the choice is individual.'),
        ('Which factor leans toward hemodialysis?',
         ['An intact abdomen', 'A trained caregiver at home', 'Previous major abdominal surgery or ostomies', 'Living far from the unit'], 2,
         'PD needs a usable peritoneum.'),
        ('What is a preemptive transplant?',
         ['A transplant after five years of dialysis', 'A temporary kidney', 'A living donor only', 'A transplant before dialysis starts'], 3,
         'It avoids dialysis when a donor and the child are ready.'),
        ('The pediatric automated PD benefit pilot was extended to:',
         ['July 31, 2026', 'December 31, 2025', 'Indefinitely', 'It never existed'], 0,
         'Status after July 31, 2026 was not verified; confirm before advising a family.'),
        ('A mother asks which modality is better. The nurse should:',
         ['Choose for her', 'Explain what each option asks of the family and pass the choice to the nephrologist and family', 'Say hemodialysis always', 'Avoid answering'], 1,
         'The nurse informs; the family and nephrologist decide.'),
        ('In the Philippine pediatric leptospirosis series, PD was started in about what share of oliguric children?',
         ['5%', '75%', '36%', '100%'], 2,
         '19 of 53 oliguric children (36%).'),
        ('Why must height be measured accurately?',
         ['For school records', 'It sets the dialyzer', 'It does not matter', 'Pediatric eGFR and growth assessment depend on it'], 3,
         'Bedside CKiD uses height directly.'),
        ('In what share of children worldwide was the cause of kidney failure unknown?',
         ['14%', '1%', '40%', '70%'], 0,
         '14% overall, highest in Northeast Asia.'),
    ],
    "terms": [("CAKUT", "Congenital anomalies of the kidney and urinary tract."),
              ("Posterior urethral valves", "A birth defect of the male urethra that blocks urine flow and can damage the kidneys."),
              ("Polyuria", "Passing large volumes of dilute urine."),
              ("Bedside CKiD equation", "A pediatric eGFR estimate from height and serum creatinine."),
              ("Preemptive transplant", "Kidney transplant before dialysis starts."),
              ("Residual kidney function", "The work the child&rsquo;s own kidneys still do.")],
    "readings": [("ckd-children-young-adults.html", "Kidney disease in children and young adults."),
                 ("nephrotic-syndrome.html", "Nephrotic syndrome, a leading glomerular cause in older children."),
                 ("peritoneal-dialysis-ckd.html", "Peritoneal dialysis explained for families.")],
    "calcs": ["calc-pediatric-egfr.html", "calc-ckid-u25-egfr.html", "calc-pediatric-ckd-krt-risk.html"],
}
