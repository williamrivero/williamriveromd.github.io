# -*- coding: utf-8 -*-
# Module 15 (core, both paths): glomerular and systemic kidney diseases.
# Base sections: model, physiology (filtration barrier and the two injury patterns), evidence (KDIGO guidance), bedside (nursing monitoring).
# m15_x.py adds disease and treatment sections after "bedside": nephrotic, nephritic, lupus-vasculitis, diabetic-pkd, biopsy, immunosuppression.
MODULE = {
    "sub": "How the glomerulus can leak protein or bleed and inflame, why each pattern brings its own complications, and the nursing that keeps these patients safe: daily weights, blood pressure, urine testing, watching for clots and infection, kidney biopsy care, and the safe use of steroids and immunosuppressive medicines.",
    "desc": "Core Module 15 of the Nephrology Nursing & Hemodialysis self-study series: nephrotic and nephritic syndromes, lupus nephritis, antineutrophil cytoplasmic antibody vasculitis, diabetic and polycystic kidney disease, kidney biopsy nursing, and monitoring during immunosuppressive treatment.",
    "keywords": "glomerulonephritis nursing, nephrotic syndrome nursing care, nephritic syndrome, lupus nephritis nurse, antineutrophil cytoplasmic antibody vasculitis nursing, kidney biopsy nursing care, immunosuppression monitoring nurse, polycystic kidney disease family screening, KDIGO glomerular diseases guideline",
    "objectives": [
        "Explain how the glomerular filtration barrier normally holds back protein and blood cells, and how injury produces either a nephrotic or a nephritic pattern.",
        "Link the complications of nephrotic syndrome (edema, thrombosis, infection, high blood lipids) and of nephritis (high blood pressure, hematuria, falling filtration) to their mechanisms.",
        "Summarize what current Kidney Disease: Improving Global Outcomes (KDIGO) guidance says about diagnosing and treating glomerular disease, lupus nephritis, and antineutrophil cytoplasmic antibody vasculitis, using calibrated language.",
        "Carry out the nursing monitoring of a patient with glomerular disease: daily weight, edema, blood pressure, urine testing and collection, signs of thrombosis and infection, and safe handling of immunosuppressive treatment.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Mental model", "h2": "A living filter that can leak or bleed",
         "html": """
<p>Module 1 described the glomerulus as a filter that throws almost nothing away. Every day it lets through a huge volume of water and small solutes. Blood cells and almost all protein stay in the blood. This module asks what happens when that filter is damaged.</p>
<p>Picture a fishing net that a crew mends every night. The crew keeps the mesh tight. If the crew falls sick, the holes widen and small fish slip through. If someone slashes the net, it tears. The glomerulus is the net, and its cells are the crew.</p>
<p>The picture has a limit. A net is passive, and a glomerulus is not. It is built of living cells that the immune system can attack, that can heal, and that can scar. The same immune defense that protects the body can be what injures the filter.</p>
<p>A living filter fails in two main ways.</p>
<ul>
<li><strong>It can leak.</strong> The fine slits that hold back protein open up. Albumin pours into the urine, while the filter itself looks quiet: little inflammation, few red cells, and often a normal filtration rate at first. The patient swells, the urine foams, and the blood thickens with fats and clotting proteins. This is the <strong>nephrotic</strong> pattern.</li>
<li><strong>It can bleed and inflame.</strong> Immune attack damages the capillary walls. White cells move in, red cells escape into the urine, and the swollen glomeruli filter less. Blood pressure rises, urine output may fall, and kidney function can drop within days. This is the <strong>nephritic</strong> pattern.</li>
</ul>
<div class="table-wrap"><table><thead><tr><th></th><th>Nephrotic pattern: the filter leaks</th><th>Nephritic pattern: the filter bleeds and inflames</th></tr></thead><tbody>
<tr><td>Main urine finding</td><td>Heavy protein, foamy urine; few red cells</td><td>Blood (cola- or tea-colored, or seen only on testing), red-cell casts; less protein</td></tr>
<tr><td>Blood findings</td><td>Low albumin, high cholesterol</td><td>Rising creatinine; complement or antibody tests may be abnormal</td></tr>
<tr><td>Swelling</td><td>Often marked: legs, eyelids, abdomen, genitals</td><td>Usually milder, from salt and water retention</td></tr>
<tr><td>Blood pressure</td><td>Normal or raised</td><td>Usually raised, sometimes suddenly</td></tr>
<tr><td>Kidney function</td><td>Often normal at first</td><td>Often falling, sometimes over days</td></tr>
<tr><td>Main dangers</td><td>Clots, infection, fluid overload, long-term heart risk from lipids</td><td>Acute kidney injury, very high blood pressure, fluid in the lungs</td></tr>
</tbody></table></div>
<p>Two more corrections. Real patients often show a <strong>mixture</strong>: lupus can leak and bleed at the same time. And many diseases that end in kidney failure, such as diabetes, injure the glomerulus slowly through pressure and metabolic stress, not immune attack. They produce protein leak and scarring over years. The two patterns are a starting point for thinking, not a diagnosis. The diagnosis usually needs blood tests and often a kidney biopsy.</p>
<p>Most of these patients are investigated and treated over weeks to years, with long stretches of routine checks. A few become dangerously ill within hours, from a clot, an infection, or a filter that is failing fast. Your work is to keep the routine checks exact, so that the dangerous change stands out when it comes.</p>
<p><strong>Where this module fits.</strong> Module 1 taught urinalysis, creatinine, and the urine albumin-to-creatinine ratio. Module 2 taught why albuminuria predicts progression and how blood pressure control and kidney-protective medicines slow chronic kidney disease (CKD). Module 4 taught acute kidney injury (AKI), including red-cell casts as a sign of glomerular inflammation. This module does not repeat them. It explains <em>why</em> the glomerulus leaks or bleeds, which diseases cause each pattern, and what you watch for while these patients are investigated and treated.</p>
<p><strong>Ask of every patient with glomerular disease: is the filter leaking, bleeding, or both? The answer tells you which complications to look for first.</strong></p>
"""},
        {"id": "physiology", "nav": "Barrier and injury", "tag": "Physiology in depth", "h2": "The filtration barrier, immune injury, and why the complications follow",
         "html": """
<p><strong>Three layers, one barrier.</strong> Blood in a glomerular capillary is separated from the urinary space by three layers. They work together.</p>
<div class="table-wrap"><table><thead><tr><th>Layer</th><th>Structure</th><th>What it holds back</th><th>What injures it</th></tr></thead><tbody>
<tr><td>Capillary lining (endothelium)</td><td>Thin cells full of open windows, coated with a negatively charged sugar layer</td><td>Blood cells; some protein through charge</td><td>Immune complexes, inflammation, very high pressure, blood-vessel diseases</td></tr>
<tr><td>Glomerular basement membrane</td><td>A dense mesh of structural proteins shared by the two cell layers</td><td>Larger proteins by size and charge</td><td>Antibodies against the membrane itself; immune deposits; thickening in diabetes</td></tr>
<tr><td>Podocytes</td><td>Octopus-like cells whose interlocking &ldquo;foot processes&rdquo; wrap the capillary; the narrow slits between the feet are bridged by a protein zipper, the slit diaphragm</td><td>Albumin and other mid-sized proteins: the final and most selective barrier</td><td>Circulating factors, antibodies, viruses, toxins, genetic defects, overwork in a shrinking kidney</td></tr>
</tbody></table></div>
<p>Podocytes are the key to the nephrotic pattern. In adults they can barely divide to replace themselves. When they are injured, the foot processes flatten and the slit diaphragm breaks down, so albumin escapes. If enough podocytes are lost, the bare membrane sticks to the surrounding capsule and the glomerulus scars. That is how a disease that begins as a pure leak can end as loss of kidney function.</p>
<p><strong>How the immune system injures a glomerulus.</strong> Most glomerular diseases are named for what the biopsy shows. The mechanisms fall into a few groups.</p>
<ul>
<li><strong>Immune complexes</strong> are clumps of antibody stuck to antigen. They are trapped in the capillary walls or formed there. They switch on complement, a cascade of blood proteins that attracts white cells and punches holes in cells. Lupus nephritis, the kidney disease after a streptococcal infection, and immunoglobulin A nephropathy work this way. Complement levels in the blood may fall because complement is being used up.</li>
<li><strong>Antibodies against the basement membrane itself</strong> attack the filter directly. They can attack the lung too, which shares the same protein. This disease is rare but one of the most urgent in nephrology.</li>
<li><strong>Antineutrophil cytoplasmic antibodies</strong> activate white cells called neutrophils, which then damage the small blood vessels they pass through. The biopsy shows few immune deposits, but the capillaries break and bleed.</li>
<li><strong>Podocyte-targeted injury</strong> comes from antibodies against podocyte proteins (as in membranous nephropathy) or from circulating factors not yet fully identified (as in minimal change disease). It produces leak with little inflammation.</li>
</ul>
<p><strong>Why the nephrotic complications follow.</strong> Each one traces back to protein leaving the body, and to the body&rsquo;s attempt to compensate.</p>
<div class="table-wrap"><table><thead><tr><th>Complication</th><th>What breaks</th><th>What you may notice</th></tr></thead><tbody>
<tr><td>Edema</td><td>Two forces act together. The kidney holds on to sodium in its collecting ducts, so salt and water are retained even when the circulation is full. Low albumin weakens the pull that keeps water inside the vessels, so the retained fluid seeps into the tissues. In some patients, especially children with very low albumin, the circulation is actually underfilled</td><td>Rising weight, pitting edema of the legs and back, swollen eyelids in the morning, abdominal swelling, scrotal or labial swelling, breathlessness if fluid collects around the lungs</td></tr>
<tr><td>Thrombosis</td><td>Small anticoagulant proteins such as antithrombin are lost in the urine. The liver, working hard to replace albumin, also makes more large clotting proteins. Platelets become stickier. Diuretics concentrate the blood, illness reduces mobility, and glucocorticoids add risk</td><td>One-sided leg swelling and pain, sudden breathlessness or chest pain, flank pain with blood in the urine (a clot in the kidney vein), unusual headache or weakness</td></tr>
<tr><td>Infection</td><td>Antibodies (immunoglobulins) and complement factors leak into the urine. Edema fluid is a good culture medium, and stretched skin breaks easily. Immunosuppressive treatment adds to the risk</td><td>Cellulitis of swollen legs, abdominal pain and fever from peritonitis in a patient with ascites, pneumonia. Glucocorticoids may blunt the fever</td></tr>
<tr><td>High blood lipids</td><td>The liver makes more lipoproteins as it responds to the low albumin, and the body clears them more slowly</td><td>High cholesterol and triglycerides on blood tests; fatty casts or &ldquo;oval fat bodies&rdquo; on microscopy</td></tr>
<tr><td>Loss of other carried substances</td><td>Proteins that carry thyroid hormone, vitamin D, and iron are lost with albumin. Drugs normally bound to albumin circulate more freely</td><td>Abnormal thyroid or vitamin D results that the physician must interpret; altered drug effects</td></tr>
</tbody></table></div>
<p><strong>Why the nephritic findings follow.</strong> Inflammation narrows and blocks the capillaries. Less blood is filtered, and the glomerular filtration rate (GFR) falls. The kidney keeps salt and water, so blood pressure rises and the patient swells, sometimes with fluid in the lungs. Damaged capillary walls let red cells squeeze through. As the cells pass along the tubules, they are bent out of shape and packed with tubular protein into red-cell casts. The cast is the urine finding that places the bleeding inside the glomerulus.</p>
<p>When inflammation is severe, cells and fibrin fill the space around the glomerulus in a half-moon shape, a <strong>crescent</strong>. Many crescents mean rapidly progressive glomerulonephritis. In that disease, kidney function can be lost within weeks unless treatment starts promptly.</p>
<p><strong>What you take from this.</strong> Weight, blood pressure, and urine output tell you about salt and water. The dipstick and the albumin or protein ratio tell you about the leak. Creatinine and urine output tell you about filtration. One-sided swelling, breathlessness, or flank pain may be a clot. Fever or new pain may be infection.</p>
<p><strong>Every routine observation in this module has a mechanism behind it. Know the mechanism, and you will know which change is dangerous.</strong></p>
"""},
        {"id": "evidence", "nav": "Guidelines", "tag": "Evidence", "h2": "What the KDIGO guidelines say, and how strong the evidence is",
         "html": """
<p>The international reference for these diseases is the Kidney Disease: Improving Global Outcomes (KDIGO) 2021 guideline for the management of glomerular diseases.[[gn2021]] KDIGO has since updated single chapters as new drugs arrived: lupus nephritis in 2024,[[ln2024]] antineutrophil cytoplasmic antibody vasculitis in 2024,[[aav2024]] and immunoglobulin A nephropathy in 2025.[[igan2025]] A separate 2025 KDIGO guideline covers autosomal dominant polycystic kidney disease.[[adpkd2025]] The disease sections later in this module summarize each one. The points below apply across glomerular disease.</p>
<p><strong>How to read a KDIGO statement.</strong> KDIGO issues two kinds of statement. A <em>recommendation</em> carries a strength (1, &ldquo;we recommend,&rdquo; or 2, &ldquo;we suggest&rdquo;) and a certainty of evidence from A (high) to D (very low). A <em>practice point</em> is ungraded expert advice. Much of the everyday supportive care below rests on practice points. This module states a grade only where we checked it in the full guideline text.</p>
<p><strong>Diagnosis.</strong> The 2021 guideline calls the kidney biopsy the &ldquo;gold standard&rdquo; for diagnosing glomerular disease, in a practice point.[[gn2021]] It also allows exceptions. In membranous nephropathy, a positive blood test for the antibody against a podocyte protein, the phospholipase A2 receptor, in a typical clinical picture, can make a biopsy unnecessary (also a practice point).[[gn2021]] The guideline describes nephrotic syndrome as edema with low serum albumin and nephrotic-range proteinuria, above 3.5 g per day.[[gn2021]] Glomerular disease can be triggered by infection. The guideline therefore advises testing for hepatitis B in proteinuric glomerular disease, and screening for tuberculosis, hepatitis B, and hepatitis C in clinically appropriate patients.[[gn2021]]</p>
<p><strong>Supportive care for every patient.</strong></p>
<ul>
<li><strong>Edema:</strong> the guideline describes diuretics, with loop diuretics as first choice, plus moderate dietary sodium restriction as the mainstays of treatment.[[gn2021]]</li>
<li><strong>Proteinuria and blood pressure:</strong> a renin&ndash;angiotensin system inhibitor at the highest tolerated dose is advised for persistent proteinuria in several glomerular diseases, together with the blood pressure and kidney-protection measures of Module 2.[[gn2021]][[ckd2024]]</li>
<li><strong>Thrombosis:</strong> full anticoagulation is indicated when a clot occurs with nephrotic syndrome (a practice point). Preventive anticoagulation is decided patient by patient. The physician weighs how low the serum albumin has fallen, the main marker of clot risk, especially in membranous nephropathy, against the risk of bleeding. The guideline notes that aspirin is not enough to prevent venous clots and that glucocorticoids increase clot risk.[[gn2021]]</li>
<li><strong>Infection:</strong> pneumococcal vaccination is advised for patients with glomerular disease and nephrotic syndrome. Preventive trimethoprim&ndash;sulfamethoxazole should be considered for patients on high-dose glucocorticoids. Both are practice points.[[gn2021]]</li>
<li><strong>Pregnancy:</strong> nephrology and obstetrics plan the care of a pregnant patient together. Pregnancy is best avoided while lupus nephritis is active or while a patient takes a medicine that can harm the fetus.[[gn2021]][[ln2024]]</li>
</ul>
<p><strong>Disease-specific treatment, in outline.</strong></p>
<div class="table-wrap"><table><thead><tr><th>Disease</th><th>What current KDIGO guidance says (in outline)</th></tr></thead><tbody>
<tr><td>Minimal change disease in adults</td><td>High-dose oral glucocorticoids are recommended as initial treatment (2021, grade 1C: strong, low certainty). They are given for a limited period and tapered after remission. Other agents are considered when glucocorticoids are unsuitable[[gn2021]]</td></tr>
<tr><td>Membranous nephropathy</td><td>Not every patient needs immunosuppression. For patients with at least one risk factor for progression, the 2021 guideline recommends rituximab, or cyclophosphamide with glucocorticoids, or a calcineurin inhibitor-based regimen, chosen by the estimated risk (grade 1B: strong, moderate certainty). Antibody levels can be followed to judge response[[gn2021]]</td></tr>
<tr><td>Immunoglobulin A nephropathy</td><td>A stricter proteinuria goal than before. Treatment aims both to reduce production of the harmful antibody and immune complexes and to manage the consequences of nephron loss with kidney-protective medicines[[igan2025]]</td></tr>
<tr><td>Lupus nephritis</td><td>Hydroxychloroquine for all patients without a contraindication (grade 1C). For active proliferative disease, glucocorticoids plus one of several immunosuppressive combinations (grade 1B)[[ln2024]]</td></tr>
<tr><td>Antineutrophil cytoplasmic antibody vasculitis</td><td>Glucocorticoids with rituximab or cyclophosphamide to start (grade 1B), a move toward lower glucocorticoid doses, and maintenance treatment afterward (grade 1C)[[aav2024]]</td></tr>
</tbody></table></div>
<p><strong>How strong is the evidence?</strong> Each glomerular disease is uncommon, so trials are smaller than in diabetes or heart disease. Notice that the grades above are B or C, not A. Many trials measured remission of proteinuria or a change in estimated glomerular filtration rate (eGFR). Those are surrogate outcomes: laboratory markers that stand in for kidney failure or death. So &ldquo;reduces proteinuria&rdquo; is a firmer statement than &ldquo;prevents kidney failure&rdquo; for many of these treatments.</p>
<p>Advice also changes quickly. Three chapters were rewritten within four years of the 2021 guideline. You do not choose these treatments. Knowing why they were chosen, and how uncertain the choice can be, helps you explain to a patient why her plan differs from a relative&rsquo;s or changes over time.</p>
<p><strong>The Philippine context.</strong> Chronic glomerulonephritis is one of the leading causes of CKD in the Philippines after diabetes and hypertension (Module 2). Biopsy services, specialized antibody tests, and newer biological drugs are concentrated in larger centers. Many medicines are paid for out of pocket. Delayed diagnosis and treatment interrupted by cost are real risks. You often see them first, and you can bring them to the physician and the social worker.</p>
<p><strong>When you hear a guideline quoted, ask two things: is it a graded recommendation or a practice point, and did the trials measure a laboratory value or an outcome the patient feels?</strong></p>
"""},
        {"id": "bedside", "nav": "Nursing monitoring", "tag": "Clinical application", "h2": "The nurse at the bedside: weight, pressure, urine, clots, infection, and medicines",
         "html": """
<p>The patient may be a child with a first nephrotic relapse, a young woman starting treatment for lupus nephritis, or an older man admitted with a rising creatinine and blood in the urine. Your core checks are the same. They track the three things the glomerulus controls (salt and water, protein, filtration) and the two dangers of the disease and its treatment (clots and infection).</p>
<div class="table-wrap"><table><thead><tr><th>Check</th><th>How to do it well</th><th>What to report</th></tr></thead><tbody>
<tr><td>Daily weight</td><td>Same scale, same time (morning, after voiding, before breakfast), same clothing. Record it on a trend chart, not only in the notes</td><td>A gain or loss beyond the limit in the order; weight falling quickly on diuretics with dizziness</td></tr>
<tr><td>Edema</td><td>Check ankles, shins, sacrum (in bedbound patients), eyelids, abdomen, and genitals. Grade pitting the same way each time. Inspect stretched skin for breaks and redness</td><td>Rising edema; new breathlessness; skin breakdown, weeping, or redness that may be cellulitis</td></tr>
<tr><td>Blood pressure</td><td>Correct cuff size for a swollen arm, patient seated and rested, standing pressure if dizzy (technique as in Module 2)</td><td>Values above or below the ordered target; headache, visual change, or confusion with high pressure</td></tr>
<tr><td>Intake and output</td><td>Measure all urine when ordered. Record fluids by mouth and intravenous (IV) infusions</td><td>Urine output falling below the ordered threshold; positive balance with rising weight</td></tr>
<tr><td>Urine dipstick</td><td>Fresh sample, strip read at the stated time, results recorded as printed on the bottle. Note menstruation or a catheter (Module 1)</td><td>New or rising protein; new blood; protein returning in a patient in remission, which may mean relapse</td></tr>
<tr><td>Spot ratio and timed collection</td><td>First-morning sample for a spot protein- or albumin-to-creatinine ratio when ordered. For a 24-hour collection, follow the steps below</td><td>A collection that was incomplete or interrupted, so it is not misread</td></tr>
<tr><td>Thrombosis signs</td><td>Compare calves and thighs. Ask about chest pain, breathlessness, flank pain, headache</td><td>Any of these at once; they are urgent</td></tr>
<tr><td>Infection signs</td><td>Temperature, and also new pain, cough, urinary symptoms, skin changes, abdominal tenderness. Glucocorticoids blunt fever</td><td>Any sign of infection in a patient on immunosuppression, even with a normal temperature</td></tr>
<tr><td>Medicine safety</td><td>Glucose, blood pressure, blood counts, and kidney function as ordered. Check that ordered preventive medicines (stomach protection, Pneumocystis prophylaxis) are given</td><td>Results outside the protocol range; missed doses; side effects (see the immunosuppression section)</td></tr>
</tbody></table></div>
<p><strong>The 24-hour urine collection, done right.</strong> Most wrong results come from missed urine, not from the laboratory.</p>
<ol>
<li>At the start time (for example 7 a.m.), the patient empties the bladder into the toilet, and that urine is <em>discarded</em>. Write the start time on the container.</li>
<li>Every void for the next 24 hours goes into the container, including urine passed when opening the bowels. Keep the container cool if the laboratory requires it.</li>
<li>At exactly the same time the next day, the patient voids one last time, and that urine is <em>added</em>. Write the end time.</li>
<li>If any urine is lost, restart the collection or record the loss. Never send an incomplete collection without saying so.</li>
</ol>
<p>A creatinine measured in the same collection lets the laboratory judge whether it was complete. Many units now use a spot first-morning ratio, which avoids these errors. Follow the order.</p>
<p><strong>Diuretics and edema.</strong> Patients with heavy proteinuria may need larger diuretic doses. One proposed reason is that the drug binds to protein in the tubular fluid and works less well. Removing fluid too quickly from a circulation that is already underfilled can cause dizziness, a fall in blood pressure, and AKI. Watch for dizziness on standing, cramps, a sharp rise in creatinine, and low potassium or sodium, and report them. The dose and the pace of fluid removal belong to the prescriber.</p>
<p><strong>Teaching the patient and family.</strong> Use the living-filter picture: &ldquo;Your kidney&rsquo;s filter is leaking protein, so water is collecting in your legs.&rdquo; Teach a low-salt diet with Filipino examples (Module 2). Teach daily home weights, with a written action plan from the physician. Teach that foamy urine is worth reporting, and how to recognize clots and infection. Patients on long courses of glucocorticoids and other immunosuppressive medicines also need the teaching in the immunosuppression section.</p>
<p><strong>When to escalate at once.</strong> Use SBAR (Situation, Background, Assessment, Recommendation) and call the physician immediately for: chest pain or sudden breathlessness; one-sided leg swelling; flank pain with blood in the urine; blood pressure above the ordered limit with headache, confusion, or visual change; urine output falling sharply; coughing up blood, which in a patient with nephritis can mean bleeding in the lungs; fever or rigors in a patient on immunosuppression; and any sign of bleeding after a kidney biopsy.</p>
<p><strong>A weight taken the same way every morning is a measurement. A weight taken any old way is a guess. Make the routine exact, and the dangerous change will stand out.</strong></p>
"""},
    ],
    "case": {
        "title": "A swollen calf on day six",
        "html": """
<p>Mr. Rodolfo Dizon, 52, is on the medical ward with nephrotic syndrome. A kidney biopsy two days ago showed membranous nephropathy. His serum albumin is very low, and his 24-hour urine protein is well into the nephrotic range. He receives a loop diuretic and an angiotensin receptor blocker, and the team is discussing rituximab. No anticoagulant has been ordered yet because of the recent biopsy. His weight has fallen 3 kg in four days.</p>
<p>It is 7 a.m. on day six of his admission. On your morning round he says his left calf has ached since last night. The left calf is visibly larger than the right, and tender. He also felt &ldquo;a little short of breath&rdquo; walking to the toilet. His pulse is 108, blood pressure 104/66, respiratory rate 22, and oxygen saturation 93% on room air, down from 97% yesterday. His urine is clear yellow. The night nurse, Ms. Liza Ocampo, is still at the station and tells you he slept poorly.</p>
""",
        "acte": {
            "Assess": "One-sided calf swelling and tenderness in a nephrotic patient suggests deep vein thrombosis. New breathlessness with a fast pulse, fast breathing, and a lower oxygen saturation raises concern that a clot has reached the lungs. Measure both calves, repeat full vital signs, and ask about chest pain and coughing up blood. Check the biopsy site and the urine for bleeding, because any anticoagulant decision will depend on it. Note the rapid weight loss on diuretics, which concentrates the blood.",
            "Communicate": "Call the physician now using SBAR: membranous nephropathy with very low albumin, two days after kidney biopsy, new left calf swelling and tenderness, breathlessness, pulse 108, respiratory rate 22, oxygen saturation 93%, blood pressure 104/66. Request urgent review, imaging, and orders on oxygen, anticoagulation, and the diuretic. State the biopsy date so the bleeding risk is weighed.",
            "Teach": "Explain to Mr. Dizon, calmly, that the leaking filter also lets out proteins that normally stop blood from clotting, and that this is why his leg is being checked urgently. Ask him to stay in bed until he is reviewed, not to massage the leg, and to report chest pain, worsening breathlessness, or coughing blood at once.",
            "Escalate": "Activate the rapid response or emergency team per hospital protocol if oxygen saturation keeps falling, blood pressure drops, chest pain develops, or he becomes confused. Give oxygen per protocol. Once an anticoagulant is ordered, watch the biopsy site and urine closely for bleeding.",
        },
        "task": "Write the morning note: the symptoms and when they started, calf measurements, vital signs compared with yesterday, biopsy-site and urine findings, whom you called and when, the orders received (imaging, oxygen, anticoagulation, diuretic changes), and Mr. Dizon&rsquo;s response.",
    },
    "quiz": [
        {"stem": "A 6-year-old boy has swollen eyelids every morning and swollen legs by evening. His urine is foamy, the dipstick shows heavy protein and no blood, his blood pressure is normal, and his serum albumin is very low. Which part of the glomerular filter is most likely failing?",
         "options": [
             ("The podocytes and the slit diaphragm between their foot processes", True, "Heavy protein loss without blood or inflammation is the nephrotic pattern. The podocyte slit is the final, most selective barrier to albumin. In children this is most often minimal change disease."),
             ("The capillary lining, broken by inflammation that lets red cells escape", False, "Inflamed, breaking capillaries produce the nephritic pattern: blood in the urine, high blood pressure, and falling filtration. This child has none of these."),
             ("The tubules, which have stopped reabsorbing the albumin they normally return", False, "Healthy glomeruli let through very little albumin. Nephrotic-range loss comes from a leaking filter, not from failed tubular reabsorption."),
             ("The bladder lining, which is leaking protein into stored urine", False, "The bladder does not add protein to urine in this way. Edema with low albumin points to the glomerulus."),
         ],
         "objective": "Explain how the glomerular filtration barrier normally holds back protein and blood cells, and how injury produces either a nephrotic or a nephritic pattern.",
         "sources": ["gn2021"], "flag": ""},
        {"stem": "Why does a patient with nephrotic syndrome have a higher risk of deep vein thrombosis?",
         "options": [
             ("Low albumin makes the blood thinner, which slows it in the leg veins", False, "Low albumin does not cause clots by thinning the blood. The problem is the balance of clotting and anticoagulant proteins."),
             ("Small natural anticoagulants such as antithrombin are lost in the urine while the liver makes more clotting proteins", True, "The leaking filter loses small anticoagulant proteins, and the liver overproduces larger clotting factors. Platelets become stickier, and diuretics, immobility, and glucocorticoids add to the risk."),
             ("High blood pressure damages the vein walls in the legs", False, "Nephrotic syndrome does not cause clots through high blood pressure. Many nephrotic patients have normal pressure."),
             ("Edema fluid squeezes the veins shut, so clots form from the pressure alone", False, "Swelling and immobility contribute. The main reason is the change in clotting proteins caused by urinary protein loss."),
         ],
         "objective": "Link the complications of nephrotic syndrome (edema, thrombosis, infection, high blood lipids) and of nephritis (high blood pressure, hematuria, falling filtration) to their mechanisms.",
         "sources": ["gn2021"], "flag": ""},
        {"stem": "A 19-year-old develops tea-colored urine, swollen eyelids, a blood pressure well above his usual, and a falling urine output three weeks after infected sores on his legs. Which explanation best links these findings?",
         "options": [
             ("Heavy protein loss has lowered his albumin, so fluid has shifted into the tissues", False, "This describes the nephrotic pattern. His dark urine, high blood pressure, and low urine output point to inflamed glomeruli."),
             ("Inflamed glomeruli filter less, so salt and water are retained, and damaged capillaries let red cells into the urine", True, "This is the nephritic pattern, typical of the kidney disease that can follow a streptococcal skin infection. Reduced filtration causes salt and water retention and high blood pressure, and bleeding capillaries color the urine."),
             ("Dehydration from the infection has concentrated the urine and lowered the urine output", False, "Dehydration does not explain high blood pressure and edema. These show salt and water retention."),
             ("Muscle breakdown has released myoglobin, which colors the urine", False, "Myoglobin gives a positive blood test with no red cells. His eyelid swelling and high pressure fit glomerular inflammation."),
         ],
         "objective": "Link the complications of nephrotic syndrome (edema, thrombosis, infection, high blood lipids) and of nephritis (high blood pressure, hematuria, falling filtration) to their mechanisms.",
         "sources": ["gn2021"], "flag": ""},
        {"stem": "A colleague says that every patient with nephrotic syndrome should be given aspirin to prevent clots. Which response best reflects the KDIGO 2021 glomerular diseases guideline?",
         "options": [
             ("Agree; aspirin is the recommended first-line prevention for all nephrotic patients", False, "The guideline states that aspirin is not sufficient to prevent venous clots in this setting."),
             ("Disagree; anticoagulants are never used in nephrotic syndrome because of bleeding risk", False, "Full anticoagulation is indicated when a clot occurs, and preventive anticoagulation is considered for selected patients."),
             ("Disagree; preventive anticoagulation is decided patient by patient by weighing how low the albumin is against bleeding risk, and aspirin is not enough for venous clots", True, "The guideline links clot risk mainly to the degree of low albumin, especially in membranous nephropathy, and asks the physician to balance it against bleeding risk. This is ungraded practice-point advice."),
             ("Agree, but only once the patient has completed a course of glucocorticoids", False, "Glucocorticoids increase clot risk. The guideline does not tie anticoagulation decisions to finishing them."),
         ],
         "objective": "Summarize what current Kidney Disease: Improving Global Outcomes (KDIGO) guidance says about diagnosing and treating glomerular disease, lupus nephritis, and antineutrophil cytoplasmic antibody vasculitis, using calibrated language.",
         "sources": ["gn2021"], "flag": "Anticoagulation decisions are made by the physician; the nurse reports clot and bleeding signs."},
        {"stem": "You are teaching a patient to collect a 24-hour urine sample for protein, starting at 7 a.m. Which instruction is correct?",
         "options": [
             ("Collect the 7 a.m. urine as the first sample, and stop collecting after the last void before 7 a.m. the next day", False, "The 7 a.m. urine was made before the collection started. Including it and omitting the final void gives the wrong 24-hour period."),
             ("Empty the bladder into the toilet at 7 a.m., collect every void after that, and add a final void at 7 a.m. the next day", True, "Discarding the first void and adding the last one captures exactly 24 hours of urine production."),
             ("Collect only the urine passed during the day, since night urine is too dilute", False, "All urine over the 24 hours is needed. Leaving out night urine makes the result falsely low."),
             ("If a void is missed, add extra water to the container to make up the volume", False, "Water adds no protein and hides the error. Report a missed void, and restart the collection or record the loss."),
         ],
         "objective": "Carry out the nursing monitoring of a patient with glomerular disease: daily weight, edema, blood pressure, urine testing and collection, signs of thrombosis and infection, and safe handling of immunosuppressive treatment.",
         "sources": ["anna7"], "flag": "Container handling and storage follow the laboratory's instructions."},
    ],
    "reflect": "Think of the last patient with heavy proteinuria or lupus you cared for. Were the daily weights done the same way every morning? Did anyone compare the two calves or ask about breathlessness? What would you change on your ward so that clots and infections are caught earlier?",
    "practice": {
        "intro": "With a preceptor on a medical or nephrology ward or in a kidney clinic, care for or review at least two patients with glomerular disease, one of them on immunosuppressive treatment.",
        "items": [
            "Explains the patient&rsquo;s findings using the leak-or-bleed model and names the likely complications to watch for.",
            "Performs and charts a standardized daily weight and edema assessment, and reports a change outside the ordered limits.",
            "Measures blood pressure with the right cuff and technique and reports values outside the ordered target.",
            "Performs and records a urine dipstick and teaches a correct 24-hour urine collection or first-morning sample.",
            "Assesses for thrombosis and infection signs every shift and escalates using SBAR.",
            "Checks glucose, blood counts, and ordered preventive medicines for a patient on immunosuppression, and teaches the patient what to report.",
        ],
    },
    "readings": [
        ["glomerulonephritis.html", "Glomerulonephritis explained: the main types, tests, and treatments."],
        ["nephrotic-syndrome.html", "Nephrotic syndrome: why protein leaks, and how swelling, clots, and infection are managed."],
        ["lupus-nephritis.html", "Lupus nephritis: classes, treatment, and long-term follow-up."],
        ["igan-guide.html", "Immunoglobulin A nephropathy, the most common glomerulonephritis worldwide."],
        ["anti-gbm-disease.html", "Disease caused by antibodies against the glomerular basement membrane: an emergency."],
        ["polycystic-kidney-disease.html", "Polycystic kidney disease: inheritance, complications, and family screening."],
        ["diabetes-kidney-disease-not-always-diabetic.html", "When kidney disease in a person with diabetes may have another cause."],
        ["proteins-proteinuria.html", "Protein in the urine: what the tests measure and what they mean."],
        ["hematuria-blood-in-urine.html", "Blood in the urine: where it comes from and how it is investigated."],
        ["viral-infections-vaccinations-ckd.html", "Infections and vaccination in kidney disease."],
    ],
    "calcs": ["calc-proteinuria-uacr.html", "calc-urine-protein-excretion.html", "calc-igan-prediction.html", "calc-anca-renal-risk.html", "calc-nephritic-toolkit.html", "calc-corticosteroid-conversion.html"],
    "external": [
        ["KDIGO glomerular diseases guideline page (2021 guideline and chapter updates)", "https://kdigo.org/guidelines/gd/"],
        ["KDIGO lupus nephritis guideline page (2024 update)", "https://kdigo.org/guidelines/lupus-nephritis/"],
        ["KDIGO antineutrophil cytoplasmic antibody vasculitis guideline page (2024 update)", "https://kdigo.org/guidelines/antineutrophilic-cytoplasmic-antibody-anca-associated-vasculitis-aav/"],
    ],
    "terms": [
        ("Glomerular basement membrane", "The dense protein mesh between the capillary lining and the podocytes in the glomerular filter."),
        ("Podocyte", "A specialized cell whose interlocking foot processes form the final barrier that keeps albumin in the blood."),
        ("Slit diaphragm", "The protein bridge between neighboring podocyte foot processes; its breakdown lets albumin leak."),
        ("Nephrotic syndrome", "Heavy proteinuria (above 3.5 g per day in adults) with low serum albumin and edema, usually with high blood lipids."),
        ("Nephritic syndrome", "Glomerular inflammation causing blood in the urine, red-cell casts, high blood pressure, edema, and falling kidney function."),
        ("Red-cell cast", "A cylinder of red cells formed in a tubule; it shows that the bleeding comes from the glomerulus."),
        ("Crescent", "A half-moon of cells and fibrin around an inflamed glomerulus, the hallmark of rapidly progressive glomerulonephritis."),
        ("Complement", "A cascade of blood proteins that the immune system uses to attract white cells and damage targets; low levels can signal immune-complex disease."),
        ("Immune complex", "Antibody bound to its antigen; when trapped in the glomerulus, it triggers inflammation."),
        ("Practice point", "Ungraded expert advice in a KDIGO guideline; it carries no strength or certainty grade."),
    ],
    "image": {"file": "renal-nursing-15-glomerular",
              "alt": "A ward nurse weighs a patient with swollen legs on a bedside scale at the start of the morning, with a urine dipstick and a chart on the trolley beside her.",
              "purpose": "Show the routine bedside checks that track a leaking or inflamed glomerulus: daily weight, edema, urine testing, and careful charting.",
              "scene": "", "focal": "", "setting": "", "details": "", "exclusions": "", "archetype": "", "reviewer": ""},
    "flags": [
        "Core module: glomerular disease content needs review by a nephrologist with a glomerular disease practice; lupus and vasculitis content also by a rheumatologist where the hospital shares care.",
        "Grades stated in this module were verified in the full guideline texts during the November 2026 rewrite. KDIGO 2021 glomerular diseases: Rec 5.3.1 minimal change disease 1C; Rec 3.3.1 membranous nephropathy 1B (rituximab, or cyclophosphamide with alternate-month glucocorticoids for 6 months, or calcineurin inhibitor-based therapy for at least 6 months, by risk estimate); practice points 1.1.1 (biopsy), 3.1.1 (anti-PLA2R), 1.7.1 and 3.4.5 (anticoagulation), 1.8.1, 1.8.2, 1.8.4 (vaccination, screening, prophylaxis). KDIGO 2024 lupus nephritis: Rec 10.2.1.1 hydroxychloroquine 1C; Rec 10.2.3.1.1 initial Class III/IV therapy 1B. KDIGO 2024 antineutrophil cytoplasmic antibody vasculitis: Rec 9.3.1.1 initial therapy 1B; Rec 9.3.2.1 maintenance 1C. Immunoglobulin A nephropathy (2025) and polycystic kidney disease (2025) statements come from executive summaries and carry no grade in the text.",
        "Membranous nephropathy treatment corrected in the rewrite: the earlier text named rituximab alone; Rec 3.3.1 lists three options.",
        "Nephrotic syndrome threshold (above 3.5 g per day) is quoted from the 2021 guideline; the serum albumin cutoff for the definition and the albumin thresholds for preventive anticoagulation (which depend on the laboratory assay) are deliberately not stated.",
        "Statement that chronic glomerulonephritis is a leading cause of CKD in the Philippines after diabetes and hypertension repeats Module 2 and is not separately cited; confirm with Philippine registry data if a number is wanted.",
        "Diuretic resistance explanation (diuretic bound to protein in tubular fluid) is mechanistic and stated as 'one proposed reason'; not cited.",
        "Weight-change and urine-output thresholds for reporting are left to the order; none are quantified.",
        "Case vital signs are illustrative; the decision on anticoagulation soon after biopsy belongs to the physician.",
    ],
    "crosswalk": {
        "ph": "Kidney diseases that lead to CKD and their care in Philippine hospitals and dialysis units: glomerular disease, lupus, diabetes, and inherited cystic disease; ward monitoring and medicine safety per hospital protocol",
        "anna": "Glomerular and systemic diseases affecting the kidney; nursing care during immunosuppressive treatment and kidney biopsy",
        "edtna": "Causes of kidney disease, including glomerulonephritis, systemic disease, and inherited disease; nursing assessment and patient education",
        "nncc": "Disease processes leading to kidney failure; pharmacology of immunosuppressive agents; patient education",
    },
}
