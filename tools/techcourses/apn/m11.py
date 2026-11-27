# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 11: Hematuria and the nephritic child.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, for Philippine
practice. Post-streptococcal GN facts checked against PubMed abstracts (VanDeVoorde 2015; Rodriguez-Iturbe 2008; Carapetis 2005)
and the MSD Manual (C3 recovery); IgAN/IgAV statements and grades against the IPNA 2025 recommendations (full text,
PMC11666671) and the KDIGO 2025 IgAN/IgAV executive summary; C3 glomerulopathy and RPGN framed on KDIGO 2021. No doses."""

MODULE = {
    "image_alt": "A Filipino boy of about eight with puffy eyes sits on a hospital bed beside a clear urine bag holding cola-colored urine, while a pediatric nephrologist checks his blood pressure.",
    "objectives": [
        "Separate glomerular from non-glomerular hematuria at the bedside, and explain why a nephritic child is volume overloaded.",
        "Diagnose and manage post-streptococcal glomerulonephritis (PSGN), using complement and its recovery to decide who needs a biopsy.",
        "Manage IgA nephropathy and IgA vasculitis nephritis in children as the IPNA 2025 recommendations describe, and recognize rapidly progressive glomerulonephritis as an emergency.",
    ],
    "big": """<div class="tc-keyp"><span class="tc-lab">Your role &middot; the urine that changes color</span>Red or cola-colored urine brings families to the emergency room fast and frightens them. The child is usually admitted under a pediatrician, who calls you about the blood pressure, the creatinine or the complement result. Your duty is to decide whether the blood comes from the glomerulus, to stop orders that make a nephritic child worse, and to set the follow-up that tells a self-limited post-infectious nephritis from a disease that needs a biopsy.</div>
{{plain:Think of the glomerulus as a fine sieve inside a pipe. Blood that leaks from a cracked pipe further down comes out bright and in clots. Blood that has been squeezed through the sieve comes out battered, mixed with protein, and sometimes molded into the shape of the tubules it passed through.}}
<p>The picture has a limit. A sieve is passive, but an inflamed glomerulus is an active organ. Immune complexes, complement and leukocytes in the capillary tuft lower the filtration surface, so glomerular filtration rate (GFR) falls, and the kidney retains sodium and water directly. The nephritic child is therefore usually volume expanded, hypertensive and edematous, the opposite of the underfilled nephrotic child in Module 9, and fluids given for &ldquo;low urine output&rdquo; make him worse.</p>
{{cards:Key numbers|Latency after streptococcal infection::1&ndash;2 weeks after pharyngitis; 2&ndash;6 weeks after skin infection|Low C3 in PSGN::Found in more than 90% of cases|C3 recovery in postinfectious GN::Back to normal within 6&ndash;8 weeks in 80% of cases|Group A streptococcal pyoderma worldwide::More than 111 million prevalent cases (2005 estimate)|Kidney involvement in children with IgA vasculitis::20&ndash;54%|IgA nephropathy in children::Median age at presentation 10.9 years}}
<p>Most children with gross hematuria and nephritis after a skin or throat infection have PSGN and recover. A few have IgA nephropathy, C3 glomerulopathy, lupus, vasculitis or a crescentic process that will destroy the kidneys in weeks without treatment. Your work is to treat the fluid and pressure now, use complement and its recovery as a clock, and biopsy the child whose course does not fit.</p>
""",
    "case": {"title": "Three weeks after the sores",
             "html": """<p>It is 11 p.m. Jerome Pascual, 8 years old and 27 kg, was admitted this afternoon to a provincial hospital in San Fernando, Pampanga, with cola-colored urine, puffy eyes and a headache. Three weeks ago he had infected sores on his legs, which his grandmother treated with leaves from the yard. His younger sister has similar sores now.</p>
<p>Blood pressure 150/100, heart rate 92, oxygen saturation 95% with fine crackles at both bases. He has gained 2 kg. Urinalysis: blood 3+, protein 2+, more than 50 red cells per high-power field with red cell casts. Creatinine 1.1 mg/dL, potassium 5.4 mmol/L. C3 is low, C4 is normal, and an antistreptolysin O titer is pending.</p>
<p>Because he had passed little urine, the admitting doctor ordered intravenous fluids at maintenance &ldquo;for oliguria,&rdquo; and the resident has written &ldquo;for methylprednisolone pulse? glomerulonephritis.&rdquo; His grandmother asks you whether the leaves caused this, and whether his sister will get it too.</p>""",
             "questions": ["Is the blood glomerular, and what is the most likely diagnosis?",
                           "What must change on his orders tonight, and what are the danger signs?",
                           "What follow-up confirms the diagnosis, and what would make you biopsy?"]},
    "sections": [
        ("physiology", "Physiology", "Where the blood comes from, and why the nephritic child is overloaded",
         """<p>Red cells reach the urine either through the glomerular capillary wall or by bleeding anywhere from the renal pelvis to the urethra. Cells that pass the glomerulus are deformed as they squeeze through the basement membrane and are then exposed to the shifting osmolality of the tubule, so they appear dysmorphic. Some show ring forms with blebs, called acanthocytes. Red cells that stick together with Tamm-Horsfall protein in the tubule form red cell casts, which can only arise in the nephron.</p>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>Glomerular hematuria</th><th>Non-glomerular hematuria</th></tr></thead>
<tbody>
<tr><td>Color</td><td>Cola, tea or smoky brown</td><td>Bright red or pink</td></tr>
<tr><td>Clots</td><td>Absent</td><td>May be present</td></tr>
<tr><td>Red cell shape</td><td>Dysmorphic; acanthocytes</td><td>Uniform (isomorphic)</td></tr>
<tr><td>Casts</td><td>Red cell casts</td><td>None</td></tr>
<tr><td>Protein</td><td>Often present beyond what the blood explains</td><td>Little</td></tr>
<tr><td>Associated findings</td><td>Edema, hypertension, rising creatinine</td><td>Pain, dysuria, trauma, stones, hypercalciuria</td></tr>
</tbody></table></div>
<p><strong>Why the child is overloaded.</strong> In acute glomerulonephritis, inflammation in the tuft reduces the filtering surface and the GFR falls. Tubular function is relatively preserved, so the kidney keeps reabsorbing sodium avidly from a smaller filtered load. Salt and water accumulate, the extracellular volume expands, and blood pressure rises. Renin is suppressed, unlike in the underfilled nephrotic child. The result is periorbital edema, hypertension, sometimes pulmonary edema, and oliguria that reflects the low GFR, not dehydration.</p>
<p>Hypertension in acute nephritis can cause headache, vomiting, visual change and seizures (hypertensive encephalopathy), and fluid overload can cause pulmonary edema. Those are the two complications that injure children in the first week.</p>
<div class="table-wrap"><table>
<thead><tr><th>What breaks</th><th>What follows</th><th>What you see</th></tr></thead>
<tbody>
<tr><td>Glomerular filtering surface</td><td>GFR falls; creatinine and potassium rise</td><td>Oliguria, rising creatinine, hyperkalemia</td></tr>
<tr><td>Sodium excretion</td><td>Primary salt and water retention</td><td>Edema, weight gain, crackles</td></tr>
<tr><td>Volume and pressure</td><td>Expanded extracellular volume, high blood pressure</td><td>Headache, vomiting, seizures, visual change</td></tr>
<tr><td>Capillary wall integrity</td><td>Red cells and protein leak</td><td>Cola urine, red cell casts, proteinuria</td></tr>
</tbody></table></div>
{{key:Oliguria in a nephritic child means a low GFR and an overloaded child. Do not treat it with fluid.}}
{{fig:apn11_a}}
"""),
        ("psgn", "Post-streptococcal GN", "Post-streptococcal glomerulonephritis and the complement clock",
         """<p><strong>Who gets it.</strong> PSGN remains the leading cause of glomerulonephritis in children worldwide, although its prevalence has fallen as pyoderma has become less common in wealthier countries.[[apn11_1]] In less developed settings its burden has been estimated at 9.5 to 28.5 new cases per 100,000 people per year.[[apn11_2]] Skin infection with group A streptococci is common in tropical, crowded settings: a 2005 global estimate counted more than 111 million prevalent cases of streptococcal pyoderma.[[apn11_3]] In a nephritic child, ask about scabies and impetigo in everyone at home, not only the patient.</p>
<p><strong>How it presents.</strong> A latent period separates infection from nephritis: 1 to 2 weeks after pharyngitis and 2 to 6 weeks after skin infection. Nephritis that begins during an infection suggests another cause, such as IgA nephropathy. C3 is low in more than 90% of cases, often before the antistreptolysin O (ASO) titer rises. Hypertension, edema, gross hematuria and impaired kidney function are worst in the first 7 to 10 days, which is the period that needs the most vigilance.[[apn11_1]]</p>
<p><strong>Treatment is supportive.</strong> A review of PSGN in children reports that loop or thiazide diuretics are the most effective treatment for its hypertension and edema, with the added benefit of lowering potassium, and that angiotensin-converting enzyme (ACE) inhibitors or angiotensin receptor blockers carry a risk of hyperkalemia and of temporarily slowing recovery of kidney function.[[apn11_1]] Restrict salt and fluid while the child is overloaded, treat any persisting streptococcal infection, and check the household. A review of PSGN advises antibiotic prophylaxis in epidemic conditions and for household contacts in communities where the disease is common.[[apn11_2]] Glucocorticoids have no role in typical PSGN. Dialysis is occasionally needed.[[apn11_4]]</p>
<p><strong>The complement clock.</strong> C3 and total hemolytic complement fall during active postinfectious nephritis and return to normal within 6 to 8 weeks in 80% of cases.[[apn11_4]] Most children&rsquo;s gross hematuria and hypertension resolve within weeks, and the long-term prognosis is good, although persistent microscopic hematuria and proteinuria may be found in fewer than 10%.[[apn11_1]] A C3 that stays low beyond that window, heavy or rising proteinuria, or a falling GFR suggests a different disease, most importantly C3 glomerulopathy, a disorder of the alternative complement pathway that can look identical at onset. The Kidney Disease: Improving Global Outcomes (KDIGO) 2021 glomerular disease guideline covers its evaluation and treatment.[[apn11_5]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Complement pattern</th><th>Diseases to consider in a child</th></tr></thead>
<tbody>
<tr><td>Low C3, normal C4</td><td>PSGN and other postinfectious GN; C3 glomerulopathy</td></tr>
<tr><td>Low C3 and low C4</td><td>Lupus nephritis (Module 12); immune-complex membranoproliferative GN; shunt nephritis; endocarditis</td></tr>
<tr><td>Normal complement</td><td>IgA nephropathy, IgA vasculitis nephritis, ANCA vasculitis, anti-GBM disease, Alport syndrome (Module 8)</td></tr>
</tbody></table></div>
<div class="tc-scene"><span class="tc-lab">In your clinic, week twelve &middot; fictional</span><p>Kyla, 9, had nephritis after impetigo. Her edema and hypertension resolved, but at 12 weeks her C3 is still low and her urine protein-to-creatinine ratio is rising.</p><p>You explain to her mother that this no longer fits PSGN, and you arrange a biopsy, which shows C3 glomerulopathy. You refer to a center that can test the complement pathway and discuss treatment.</p><p class="tc-scene-take"><b>What this shows.</b> The complement level at follow-up is part of the diagnosis. A PSGN that does not recover is not PSGN.</p></div>
{{key:In a child with low C3 nephritis, check C3 again at about 8 weeks. Recovery confirms PSGN; persistence calls for a biopsy.}}
"""),
        ("iga", "IgA disease", "IgA nephropathy and IgA vasculitis nephritis in children",
         """<p><strong>IgA nephropathy (IgAN).</strong> Children with IgAN usually present with gross hematuria during a febrile upper respiratory infection, called synpharyngitic hematuria, unlike the latent period of PSGN. The median age at presentation in children is 10.9 years. Compared with adults, pediatric biopsies tend to show more intense inflammation and less chronic damage. The International Pediatric Nephrology Association (IPNA) 2025 recommendations note that management is supported by little high-quality evidence in children.[[apn11_7]]</p>
<p>For children with persistent proteinuria, defined as a urine protein-to-creatinine ratio (UPCR) of at least 0.2 mg/mg (20 mg/mmol), the IPNA recommends optimizing supportive care: dietary counseling to keep salt intake below 3 to 5 g a day (level X, strong recommendation) and renin-angiotensin system blockade with an ACE inhibitor or angiotensin receptor blocker at the maximally tolerated dose, aiming for UPCR below 0.2 mg/mg (grade C, moderate recommendation). In children with chronic kidney disease (CKD) stage 2 or higher, it recommends a 24-hour mean arterial pressure at or below the 50th percentile by ambulatory monitoring when UPCR exceeds 0.5 mg/mg, and at or below the 75th percentile without proteinuria (grade B, moderate recommendation). It recommends lifelong yearly blood pressure and urinalysis for anyone with pediatric IgAN (grade X, strong recommendation).[[apn11_7]] The pediatric evidence for blockade is a randomized trial in 66 children and young adults aged 9 to 35 with proteinuria of 1 to 3.5 g/day/1.73 m&sup2;: creatinine clearance fell by more than 30% in 14.7% on placebo and 3.1% on benazepril over about 35 months.[[apn11_7]] The adult KDIGO 2025 IgAN guideline now sets stricter proteinuria targets for adults, below 0.5 g a day and ideally below 0.3 g a day, but its authors note that little has changed for children because major pediatric trials are lacking.[[apn11_6]]</p>
<p><strong>IgA vasculitis nephritis (IgAVN).</strong> IgA vasculitis, formerly Henoch-Sch&ouml;nlein purpura, is the most common small-vessel vasculitis of childhood, with palpable purpura on the legs and buttocks, abdominal pain and arthritis. Kidney involvement is reported in 20% to 54% of affected children, usually as urinary abnormalities with normal blood pressure and kidney function, and nephritis may recover without treatment. The IPNA recommends urinalysis with a first-morning UPCR at onset and at least monthly for at least 6 months. It recommends kidney biopsy in children with IgA vasculitis and nephrotic-range proteinuria (UPCR above 2 mg/mg) (grade X, strong recommendation) or an estimated GFR below 90 mL/min/1.73 m&sup2; whatever the proteinuria (grade X, moderate recommendation), and suggests biopsy for moderate proteinuria (UPCR 1 to 2 mg/mg) lasting 2 to 4 weeks (grade D, weak recommendation).[[apn11_7]]</p>
<div class="table-wrap"><table>
<thead><tr><th></th><th>PSGN</th><th>IgA nephropathy</th><th>IgA vasculitis nephritis</th></tr></thead>
<tbody>
<tr><td>Timing of hematuria</td><td>1&ndash;6 weeks after throat or skin infection</td><td>During a respiratory infection</td><td>Days to weeks after the rash</td></tr>
<tr><td>C3</td><td>Low, recovers</td><td>Normal</td><td>Normal</td></tr>
<tr><td>Extrarenal signs</td><td>Healing sores, edema, hypertension</td><td>Usually none</td><td>Purpura, abdominal pain, arthritis</td></tr>
<tr><td>Course</td><td>Usually self-limited</td><td>Recurrent gross hematuria; risk tied to proteinuria and blood pressure</td><td>Often mild; risk tied to proteinuria and GFR</td></tr>
<tr><td>Biopsy</td><td>Only if atypical or not recovering</td><td>To diagnose when proteinuria persists</td><td>Nephrotic-range proteinuria, reduced eGFR, or persisting moderate proteinuria</td></tr>
</tbody></table></div>
{{key:Proteinuria and blood pressure, not the hematuria, carry the long-term risk in IgA disease. Measure them for life.}}
{{fig:apn11_b}}
"""),
        ("practice", "Practice", "The emergency, the follow-up and the attending&rsquo;s plan",
         """<p><strong>Rapidly progressive glomerulonephritis (RPGN).</strong> The IPNA defines RPGN as kidney function below half of normal, or a rapid loss of function, with crescents and necrosis on biopsy.[[apn11_7]] In a child it may be crescentic IgAN or IgAVN, lupus, ANCA vasculitis, anti-glomerular basement membrane (anti-GBM) disease, or severe postinfectious GN. Creatinine that doubles over days, oliguria that does not respond, or pulmonary hemorrhage is an emergency: urgent biopsy where possible, serology (ANCA, anti-GBM, antinuclear antibody, complement), and treatment in a center with pediatric nephrology, dialysis and intensive care, as the KDIGO glomerular guidelines describe.[[apn11_5]] Module 12 continues with lupus and vasculitis.</p>
<p><strong>Isolated microscopic hematuria.</strong> A well child with microscopic hematuria on a school urinalysis, normal blood pressure, no proteinuria and normal creatinine needs a repeat test, a family history and patience, not a biopsy. Ask about kidney failure, dialysis or deafness in relatives (Alport syndrome, Module 8), check urine calcium, and follow blood pressure and urine protein yearly.</p>
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>What it suggests</th><th>Next step</th></tr></thead>
<tbody>
<tr><td>Cola urine, edema, hypertension, low C3 after impetigo</td><td>PSGN</td><td>Fluid and salt restriction, diuretic for overload, C3 at about 8 weeks</td></tr>
<tr><td>Gross hematuria during a fever, normal C3</td><td>IgA nephropathy</td><td>UPCR; biopsy if proteinuria persists</td></tr>
<tr><td>Purpura, abdominal pain, then hematuria</td><td>IgA vasculitis nephritis</td><td>Monthly urinalysis for 6 months; biopsy by IPNA criteria</td></tr>
<tr><td>Low C3 and C4, rash, arthritis, cytopenias</td><td>Lupus nephritis</td><td>Antinuclear and anti-dsDNA antibodies; biopsy (Module 12)</td></tr>
<tr><td>Creatinine doubling in days, hemoptysis</td><td>RPGN: ANCA, anti-GBM, crescentic disease</td><td>Emergency serology, biopsy, transfer</td></tr>
<tr><td>Isolated microscopic hematuria, family history of deafness or dialysis</td><td>Alport syndrome</td><td>Urine albumin, hearing test, genetic testing</td></tr>
</tbody></table></div>
<div class="tc-scene"><span class="tc-lab">By phone from the ward, the fluid order &middot; fictional</span><p>A resident tells you that a nephritic 10-year-old has passed only 100 mL of urine since admission and that the intravenous fluid has been increased to &ldquo;flush the kidneys.&rdquo; The child now has crackles and a blood pressure of 160/110.</p><p>You ask her to stop the infusion, sit him up, give oxygen, give a loop diuretic as the unit protocol directs, start antihypertensive treatment, and call the intensive care team if he does not improve within the hour.</p><p class="tc-scene-take"><b>What this shows.</b> The oliguria of nephritis is the kidney&rsquo;s low GFR. Fluid adds to an already expanded volume.</p></div>
{{flow:The nephritic child, first 24 hours|Confirm glomerular origin::Cola urine, dysmorphic red cells or casts, proteinuria.|Assess the danger::Blood pressure, headache or seizures, crackles and oxygen saturation, weight, potassium, creatinine.|Stop harm::No maintenance fluid for oliguria; restrict salt and fluid.|Treat overload and pressure::Loop diuretic and antihypertensive per unit protocol; avoid RAAS blockade while potassium and creatinine are rising.|Send the clock::C3, C4, ASO or anti-deoxyribonuclease B (anti-DNase B); antinuclear antibody if any systemic feature.|Treat the source::Streptococcal skin or throat infection; examine the household.|Plan follow-up::C3 at about 8 weeks; urine and blood pressure until normal; biopsy if the course does not fit.}}
{{call:<ul><li>Headache with vomiting, visual change or seizure (hypertensive encephalopathy)</li><li>Crackles, falling oxygen saturation or breathlessness (pulmonary edema)</li><li>Potassium &ge;6.0 mmol/L or electrocardiogram changes</li><li>Creatinine rising daily, anuria, or hemoptysis (think RPGN)</li></ul>}}
{{key:Biopsy the nephritic child whose course does not fit: C3 still low after about 8 weeks, nephrotic-range or rising proteinuria, or a falling GFR.}}
"""),
    ],
    "debrief": [
        "<p><strong>Glomerular blood and the diagnosis.</strong> Cola urine with red cell casts and proteinuria is glomerular. Nephritis three weeks after skin sores, with hypertension, edema, a rising creatinine, a low C3 and a normal C4, is PSGN until the course says otherwise. The latency fits skin infection (2 to 6 weeks), and the ASO or anti-DNase B titer will support it. IgA nephropathy would have started during an infection, and lupus would usually lower C4 as well.</p>",
        "<p><strong>Tonight&rsquo;s orders.</strong> Stop the maintenance fluid: his oliguria is a low GFR in an overloaded child, and he already has crackles. Restrict salt and fluid, give a loop diuretic as the unit protocol directs, treat the blood pressure, and recheck potassium; the grandmother&rsquo;s leaves did not cause this. Cancel the methylprednisolone: glucocorticoids have no role in typical PSGN. The danger signs for the nurses are headache with vomiting, visual change or seizure, breathlessness or falling saturation, very low urine output with rising potassium, and a blood pressure that does not come down. Examine his sister, treat her sores and those of other household members, and consider antibiotic prophylaxis for close contacts as the PSGN literature advises in high-prevalence settings.</p>",
        "<p><strong>Follow-up and biopsy.</strong> Check his C3 again at about 8 weeks; in 80% of postinfectious nephritis it is normal by 6 to 8 weeks. Follow blood pressure and urine until the hematuria and proteinuria resolve; microscopic hematuria can linger for months. Biopsy him if C3 stays low beyond that window, if proteinuria reaches the nephrotic range or keeps rising, if his creatinine climbs instead of falling, or if systemic features appear. Those would point to C3 glomerulopathy, lupus or a crescentic disease.</p>",
    ],
    "skills": {"title": 'Hematuria and the nephritic child',
               "intro": "Complete with a preceptor, in simulation or at your own unit. Sign-off is local.",
               "items": [("Examines a urine sediment for dysmorphic red cells and casts, or interprets the laboratory report", False),
                         ("Manages fluid overload and hypertension in acute nephritis without giving fluid for oliguria", False),
                         ("Uses complement patterns and C3 recovery to decide on biopsy", False),
                         ("Applies IPNA 2025 biopsy and follow-up criteria in IgA vasculitis", False)],
               "placement": "Pediatric ward or nephrology clinic"},
    "quiz": [
        ("Which finding most reliably places hematuria in the glomerulus?",
         ["Bright red urine with clots", "Red cell casts", "Dysuria", "Flank pain radiating to the groin"],
         1, "Red cell casts form only in the tubule from red cells that crossed the glomerulus. Clots and bright red urine suggest a lower-tract source."),
        ("An oliguric 8-year-old with PSGN has edema, crackles and a blood pressure of 150/100. What is the right fluid order?",
         ["Maintenance intravenous fluid to restore urine output", "A fluid bolus", "Salt and fluid restriction with a loop diuretic per protocol", "Albumin infusion"],
         2, "Nephritic oliguria reflects a low GFR with primary salt retention; the child is volume expanded. Diuretics are the most effective treatment for PSGN hypertension and edema."),
        ("Three months after presumed PSGN, a child&rsquo;s C3 remains low and proteinuria is rising. What is the next step?",
         ["Reassure; C3 takes a year to recover", "Kidney biopsy, with C3 glomerulopathy high on the list", "Start long-term penicillin", "Repeat C3 in one year"],
         1, "C3 returns to normal within 6 to 8 weeks in 80% of postinfectious GN. Persistence with rising proteinuria does not fit PSGN."),
        ("According to the IPNA 2025 recommendations, which child with IgA vasculitis should have a kidney biopsy?",
         ["Any child with purpura", "A child with microscopic hematuria only", "A child with nephrotic-range proteinuria or eGFR below 90 mL/min/1.73 m&sup2;", "Every child at 6 months"],
         2, "Nephrotic-range proteinuria (grade X, strong) and reduced eGFR (grade X, moderate) are indications; moderate proteinuria for 2 to 4 weeks is a weaker indication (grade D)."),
        ("A child develops gross hematuria on the second day of a febrile sore throat; C3 is normal. What is most likely?",
         ["PSGN", "IgA nephropathy", "Lupus nephritis", "Nephrogenic diabetes insipidus"],
         1, "Synpharyngitic hematuria with normal complement points to IgA nephropathy; PSGN follows infection after a latent period with low C3."),
    ],
    "terms": [("GFR", "Glomerular filtration rate"), ("eGFR", "Estimated glomerular filtration rate"), ("PSGN", "Post-streptococcal glomerulonephritis"),
              ("GN", "Glomerulonephritis"), ("IgAN", "Immunoglobulin A nephropathy"), ("IgAV", "Immunoglobulin A vasculitis"),
              ("IgAVN", "Immunoglobulin A vasculitis nephritis"), ("IPNA", "International Pediatric Nephrology Association"),
              ("KDIGO", "Kidney Disease: Improving Global Outcomes"), ("UPCR", "Urine protein-to-creatinine ratio"),
              ("ACE", "Angiotensin-converting enzyme"), ("RAAS", "Renin-angiotensin-aldosterone system"), ("CKD", "Chronic kidney disease"),
              ("RPGN", "Rapidly progressive glomerulonephritis"), ("ANCA", "Antineutrophil cytoplasmic antibody"),
              ("anti-GBM", "Anti-glomerular basement membrane"), ("ASO", "Antistreptolysin O"), ("anti-dsDNA", "Anti-double-stranded DNA antibody"), ("anti-DNase B", "Anti-deoxyribonuclease B antibody")],
    "readings": [('hematuria-blood-in-urine.html', 'Red Alert: Blood in Your Urine — When to Worry, When to Wait'),
                 ('nephritic-syndromes.html', 'Nephritic Syndrome: Recognize It, Act Fast, Find the Cause'),
                 ('igan-guide.html', 'IgA Nephropathy — The Kidney Disease You Didn&rsquo;t Know You Had')],
    "calcs": ["calc-nephritic-toolkit.html", "calc-pediatric-bp.html", "calc-pediatric-egfr.html", "calc-urine-protein-excretion.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
