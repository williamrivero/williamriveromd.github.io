# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 12: Lupus nephritis and vasculitis in children.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, for Philippine
practice. KDIGO 2024 lupus nephritis recommendations (10.2.1.1, 1C; 10.2.3.1.1, 1B; Practice Point 10.3.3.1; the 36-month
practice point; the pediatric complete-response footnote) checked against the guideline text; KDIGO 2024 ANCA vasculitis
statements (rituximab preferred in children; Practice Point 9.3.1.9 as corrected) against KDIGO documents; SHARE 2017,
Livingston 2011, Hiraki 2012, BLISS-LN, AURORA 1, PEXIVAS and ARChiVe against PubMed abstracts. No doses."""

MODULE = {
    "image_alt": "A Filipino teenage girl with a faint butterfly rash across her cheeks talks with a pediatric nephrologist at her hospital bedside while her mother holds her hand.",
    "objectives": [
        "Explain why childhood-onset lupus is more often renal, and why the biopsy class, not the creatinine alone, decides lupus nephritis treatment.",
        "Choose induction and maintenance therapy for proliferative lupus nephritis with the family as KDIGO 2024 describes, weighing growth, bone and fertility.",
        "Recognize ANCA vasculitis and anti-GBM disease in a child as emergencies, start treatment without waiting for every result, and know when plasma exchange is considered.",
    ],
    "big": """<div class="tc-keyp"><span class="tc-lab">Your role &middot; the kidney in a systemic disease</span>Lupus and vasculitis in children are shared with pediatric rheumatology, often by phone, because few Philippine hospitals have both specialists on site. You own the kidney: the biopsy and its timing, the induction plan, the blood pressure, the proteinuria target and the dialysis decision. You also carry the conversation about what the drugs will cost a girl in growth, bone and fertility, in words a teenager and her mother can weigh.</div>
{{plain:Think of lupus as a fire alarm system that has started to ring at the building itself. The alarm is meant for intruders, but it now sends the fire brigade to every room, and the water does as much damage as any fire.}}
<p>The picture has a limit. In lupus the damage comes from immune complexes, antibodies bound to nuclear antigens, that lodge in glomeruli and activate complement and leukocytes. Where they deposit decides what you see: in the mesangium the injury is mild; beneath the endothelium it provokes proliferation, crescents and falling function; beneath the epithelium it causes membranous nephrotic syndrome. ANCA vasculitis is different again: few immune deposits, but activated neutrophils that necrose small vessels. A biopsy tells you which fire you are fighting.</p>
{{cards:Key numbers|Lupus nephritis in childhood-onset SLE (SHARE 2017)::50&ndash;60% of patients|KDIGO 2024, complete response in children::Proteinuria &lt;0.5 g/1.73 m&sup2; per day|KDIGO 2024, proliferative lupus nephritis::Initial plus maintenance immunosuppression for at least 36 months in total|BLISS-LN (adults), renal response at 104 weeks::43% with belimumab vs 32% with standard therapy alone|AURORA 1 (adults), complete renal response at 52 weeks::41% with voclosporin vs 23%|PEXIVAS (adults), death or kidney failure::28.4% with plasma exchange vs 31.0% without}}
<p>Most children with lupus nephritis can reach remission and keep their kidneys if the biopsy is done early and induction is followed by years of maintenance that they actually take. A few lose function within weeks from crescentic lupus, ANCA vasculitis or anti-glomerular basement membrane disease. Your work is to biopsy promptly, start treatment without dangerous delay, choose regimens that a growing child can survive well, and keep an adolescent engaged for the years the disease demands.</p>
""",
    "case": {"title": "The creatinine that doubled",
             "html": """<p>Angelica Reyes is 13 years old and weighs 44 kg. She reached menarche six months ago. She lives with her mother, a public school teacher, in Calamba, Laguna. For three weeks she has had fatigue, painful knees and wrists, mouth ulcers and a rash across her cheeks that worsens in the sun. For a week her urine has been frothy and her ankles swollen.</p>
<p>She is admitted to the pediatric ward of a tertiary government hospital. Blood pressure 140/90. Creatinine 1.3 mg/dL; it was 0.6 mg/dL at a clinic visit one week ago. Urine protein-to-creatinine ratio 3.2 mg/mg, with red cell casts. Hemoglobin 9.2 g/dL, platelets 98,000/&micro;L. C3 and C4 are both low; antinuclear antibody is positive at 1:1280 and anti-double-stranded DNA antibody is high.</p>
<p>The kidney biopsy has been scheduled for ten days from now, because the procedure list is full. The pediatric rheumatologist is available by phone and suggests starting treatment. Angelica&rsquo;s mother has read that cyclophosphamide causes infertility and asks you, in front of her daughter, whether that is true and whether there is another way.</p>""",
             "questions": ["Why biopsy, and should treatment wait ten days for it?",
                           "Which induction options fit a 13-year-old girl, and how do growth, bone and fertility change the choice?",
                           "If the biopsy had shown pauci-immune necrotizing crescents with a positive MPO-ANCA, what would change?"]},
    "sections": [
        ("physiology", "Physiology", "How lupus and vasculitis injure the kidney, and why children fare worse",
         """<p><strong>Lupus nephritis (LN).</strong> Antibodies against nuclear antigens such as double-stranded DNA form immune complexes in the circulation or bind antigens planted in the glomerulus. Complement is consumed, which is why C3 and C4 fall, and the complexes recruit neutrophils and macrophages. The site of deposition sets the injury, and the International Society of Nephrology/Renal Pathology Society (ISN/RPS) classification groups biopsies into classes that guide treatment, as the SHARE pediatric recommendations and the KDIGO guideline use.[[apn12_2]][[apn12_5]]</p>
<div class="table-wrap"><table>
<thead><tr><th>ISN/RPS class</th><th>Where the injury is</th><th>What you usually see</th><th>Treatment intensity</th></tr></thead>
<tbody>
<tr><td>I and II</td><td>Mesangium</td><td>Mild hematuria or proteinuria; normal function</td><td>Guided by extrarenal disease; low intensity</td></tr>
<tr><td>III (focal) and IV (diffuse)</td><td>Subendothelial deposits, proliferation, crescents</td><td>Active sediment, hypertension, rising creatinine, often nephrotic proteinuria</td><td>Full induction then maintenance</td></tr>
<tr><td>V</td><td>Subepithelial deposits (membranous)</td><td>Nephrotic syndrome, bland sediment, thrombosis risk</td><td>Intermediate; combined with III/IV if present</td></tr>
<tr><td>VI</td><td>Global sclerosis</td><td>Chronic kidney disease</td><td>Prepare for kidney replacement; treat extrarenal lupus</td></tr>
</tbody></table></div>
<p><strong>Why childhood-onset lupus is more renal.</strong> A meta-analysis of 16 studies comparing 905 children with 5,993 adults with systemic lupus erythematosus (SLE) found that renal involvement, proteinuria and urinary cellular casts, along with malar rash, seizures, cytopenias, fever and lymphadenopathy, were more common in childhood-onset disease, with odds ratios from 1.3 to 3.7 across these features. Study quality was modest, averaging 16 of 32 on the STROBE checklist.[[apn12_3]] The SHARE recommendations state that LN occurs in 50% to 60% of patients with childhood-onset SLE (cSLE).[[apn12_2]] In a United States Medicaid claims cohort of 2,959 children with SLE, 37% had codes indicating LN, a lower estimate that reflects a billing-based definition.[[apn12_4]]</p>
<p><strong>ANCA vasculitis.</strong> Antineutrophil cytoplasmic antibodies (ANCA) against myeloperoxidase (MPO) or proteinase 3 (PR3) activate primed neutrophils, which damage small-vessel walls. The kidney shows focal necrotizing, crescentic glomerulonephritis with few immune deposits (&ldquo;pauci-immune&rdquo;). In the international ARChiVe registry, 231 children were classified as microscopic polyangiitis (MPA, 48) or granulomatosis with polyangiitis (GPA, 183). Children with MPA were younger (median 11 versus 14 years), renal involvement was common in both (75% and 83%) and tended to be more severe in MPA, and 64% of the children were female.[[apn12_10]]</p>
<p><strong>Anti-GBM disease.</strong> Antibodies against type IV collagen in the glomerular and alveolar basement membranes cause rapidly progressive crescentic nephritis, sometimes with pulmonary hemorrhage. It is rare in children, and it destroys kidneys in days.</p>
{{key:The biopsy class decides lupus nephritis treatment. The creatinine tells you how urgent it is.}}
{{fig:apn12_a}}
"""),
        ("lupus", "Lupus nephritis", "Treating lupus nephritis: induction, maintenance and what it costs a child",
         """<p><strong>For everyone.</strong> KDIGO 2024 recommends hydroxychloroquine or an equivalent antimalarial for all patients with SLE, including those with LN, unless contraindicated (Recommendation 10.2.1.1, graded 1C).[[apn12_5]] Blood pressure control, renin-angiotensin blockade for proteinuria and attention to infection and bone apply throughout.</p>
<p><strong>Proliferative disease (class III or IV, with or without V).</strong> KDIGO 2024 recommends glucocorticoids plus any one of four options, each graded 1B: a mycophenolic acid analog (MPAA, such as mycophenolate mofetil); low-dose intravenous cyclophosphamide; belimumab with either an MPAA or low-dose intravenous cyclophosphamide; or an MPAA with a calcineurin inhibitor (CNI) when estimated glomerular filtration rate (eGFR) is at least 45 mL/min/1.73 m&sup2; (Recommendation 10.2.3.1.1).[[apn12_5]] A practice point advises treating pediatric patients with regimens similar to those used in adults (Practice Point 10.3.3.1), and the guideline notes that in children the cumulative glucocorticoid dose affects peak bone mass and growth. For children younger than 18, it defines complete response as proteinuria below 0.5 g/1.73 m&sup2; per day. It advises that initial plus maintenance immunosuppression for proliferative LN last at least 36 months in total.[[apn12_5]]</p>
<p>The European SHARE initiative, written for children, recommends mycophenolate mofetil (MMF) or intravenous cyclophosphamide with glucocorticoids for class III/IV induction, MMF or azathioprine for at least 3 years of maintenance, complete renal response as the treatment goal, and MMF with low-dose prednisone for pure class V.[[apn12_2]]</p>
<p><strong>The newer add-on drugs were tested in adults.</strong> BLISS-LN randomized 448 adults with active biopsy-proven LN to intravenous belimumab or placebo on top of standard therapy. At 104 weeks the primary efficacy renal response was 43% versus 32%, complete renal response 30% versus 20%, and the risk of a renal-related event or death was lower with belimumab (hazard ratio 0.51).[[apn12_6]] AURORA 1 randomized 357 adults with class III, IV or V LN to voclosporin or placebo with MMF and rapidly tapered low-dose steroids; complete renal response at 52 weeks was 41% versus 23%, with similar serious adverse events.[[apn12_7]] Both trials used proteinuria-based composite responses, which are surrogates, and neither enrolled children. Using them in adolescents is extrapolation, and cost and availability limit access in the Philippines.</p>
<div class="table-wrap"><table>
<thead><tr><th>Induction option (KDIGO 2024, 1B)</th><th>Evidence base</th><th>What weighs more in a child</th></tr></thead>
<tbody>
<tr><td>Glucocorticoids + MPAA</td><td>Adult trials; SHARE pediatric recommendation</td><td>Twice-daily adherence; gastrointestinal effects; teratogenic, so contraception counseling in adolescents</td></tr>
<tr><td>Glucocorticoids + low-dose IV cyclophosphamide</td><td>Adult trials; SHARE pediatric recommendation</td><td>Gonadal toxicity related to cumulative dose; supervised infusions help adherence</td></tr>
<tr><td>Belimumab + MPAA or low-dose IV cyclophosphamide</td><td>BLISS-LN, adults only</td><td>Cost and access; extrapolated to adolescents</td></tr>
<tr><td>MPAA + CNI (eGFR &ge;45)</td><td>AURORA 1 and other adult trials</td><td>Nephrotoxicity, hypertension, drug levels</td></tr>
</tbody></table></div>
<p>Glucocorticoid exposure deserves its own line in every plan. A teenager still growing, building peak bone mass and forming a body image will feel the steroids long after the nephritis is quiet. Use the lowest exposure the regimen allows, plot height and weight, and check bone health and blood pressure.</p>
{{key:Choose induction by class, then by what the child can tolerate and sustain: adherence, growth, bone and fertility weigh more at 13 than at 43.}}
"""),
        ("vasculitis", "Vasculitis", "ANCA vasculitis and anti-GBM disease in children",
         """<p><strong>Do not wait for the biopsy.</strong> KDIGO 2024 states that when the clinical presentation is compatible with small-vessel vasculitis and MPO- or PR3-ANCA is positive, waiting for a kidney biopsy should not delay immunosuppression, especially in patients who are deteriorating rapidly; the biopsy follows as soon as feasible.[[apn12_8]]</p>
<p><strong>Induction.</strong> KDIGO 2024 recommends glucocorticoids with rituximab or cyclophosphamide for initial treatment, and lists children and adolescents, and patients concerned about their fertility, among those in whom rituximab is preferred.[[apn12_8]] Its corrected Practice Point 9.3.1.9 advises considering plasma exchange for patients with a serum creatinine above 3.4 mg/dL (300 &micro;mol/L), those requiring dialysis or with a rapidly rising creatinine, and those with diffuse alveolar hemorrhage and hypoxemia.[[apn12_9]] The evidence for plasma exchange comes from PEXIVAS, which randomized 704 adults with severe ANCA vasculitis (eGFR below 50 or diffuse pulmonary hemorrhage). Death or end-stage kidney disease (ESKD) occurred in 28.4% with plasma exchange and 31.0% without (hazard ratio 0.86, not significant). A reduced-dose glucocorticoid regimen was noninferior to standard dosing (27.9% vs 25.5%) and caused fewer serious infections in the first year (incidence rate ratio 0.69).[[apn12_1]] PEXIVAS enrolled adults; in children, these findings support lower glucocorticoid exposure by extrapolation.</p>
<p><strong>Anti-GBM disease</strong> is treated urgently with plasma exchange, cyclophosphamide and glucocorticoids, as the KDIGO 2021 glomerular disease guideline describes; outcomes depend on how early treatment begins.[[apn12_11]] In a child with nephritis and hemoptysis, send ANCA and anti-GBM antibodies together and transfer early to a center that can dialyze and perform plasma exchange.</p>
<div class="table-wrap"><table>
<thead><tr><th>Presentation</th><th>Serology</th><th>First actions</th></tr></thead>
<tbody>
<tr><td>Nephritis with rash, arthritis, cytopenias</td><td>ANA, anti-dsDNA positive; low C3 and C4</td><td>Biopsy promptly; start glucocorticoids if crescentic or rapidly progressive; hydroxychloroquine</td></tr>
<tr><td>Rapidly progressive GN, sinus or lung disease</td><td>MPO- or PR3-ANCA positive; normal complement</td><td>Start glucocorticoids with rituximab or cyclophosphamide; biopsy when feasible; consider plasma exchange by PP 9.3.1.9</td></tr>
<tr><td>Rapidly progressive GN with pulmonary hemorrhage</td><td>Anti-GBM positive (sometimes with ANCA)</td><td>Plasma exchange, cyclophosphamide and glucocorticoids without delay; transfer</td></tr>
</tbody></table></div>
<div class="tc-scene"><span class="tc-lab">On the ward, the cough with blood &middot; fictional</span><p>A 14-year-old boy from Batangas with cola urine coughs bright blood overnight; his oxygen saturation drops to 89%, and his creatinine has risen from 1.0 to 2.8 mg/dL in four days. ANCA and anti-GBM results will take three days from a send-out laboratory.</p><p>You start pulse glucocorticoids as the unit protocol directs, call the pediatric intensive care unit, and arrange transfer to a center that can do plasma exchange and dialysis today. You do not wait for the serology.</p><p class="tc-scene-take"><b>What this shows.</b> In pulmonary-renal syndrome, delay costs lungs and kidneys. Treatment begins on the clinical picture.</p></div>
{{key:A positive ANCA in a compatible illness is enough to start treatment. The biopsy confirms; it does not license delay.}}
{{fig:apn12_b}}
"""),
        ("practice", "Practice", "The attending&rsquo;s plan: biopsy, protection and the long road",
         """<p><strong>Biopsy early and safely.</strong> Correct the platelet count and blood pressure as far as the protocol requires, and push for the earliest safe slot. Ten days is too long for a girl whose creatinine doubled in a week. If the biopsy must wait, discuss with the rheumatologist starting glucocorticoids now, accepting that the biopsy should follow within days so that the class can still guide the choice of the second agent.</p>
<p><strong>Protect before you suppress.</strong> Screen for tuberculosis and hepatitis B before intensive immunosuppression, update inactivated vaccines where time allows, and plan infection prophylaxis as your unit protocol and the regimen require. Start hydroxychloroquine and arrange baseline and periodic eye examinations.</p>
<p><strong>Talk about fertility honestly.</strong> Cyclophosphamide&rsquo;s gonadal toxicity rises with cumulative dose and age; low-dose regimens are designed to limit cumulative exposure, and KDIGO 2024 lists MMF-based options as equal alternatives for lupus nephritis. For an adolescent girl, discuss contraception as well, because MMF is teratogenic and pregnancy during active nephritis is dangerous. Speak to Angelica directly; at 13 she can understand and should assent.</p>
<div class="table-wrap"><table>
<thead><tr><th>Long-term threat</th><th>Why it happens</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>Flare</td><td>Poor adherence, early withdrawal, disease biology</td><td>At least 36 months of total immunosuppression for proliferative LN; regular urine protein and complement</td></tr>
<tr><td>Growth and bone loss</td><td>Glucocorticoids, inflammation, CKD</td><td>Lowest steroid exposure; growth chart; bone health plan</td></tr>
<tr><td>Infection</td><td>Immunosuppression, hypogammaglobulinemia after rituximab</td><td>Screening, vaccines, prophylaxis per protocol, a low threshold to admit with fever</td></tr>
<tr><td>Cardiovascular risk</td><td>Hypertension, dyslipidemia, proteinuria, steroids</td><td>Blood pressure targets, renin-angiotensin blockade, lipids</td></tr>
<tr><td>Disengagement in adolescence</td><td>Long treatment, side effects on appearance, transition</td><td>Shared goals, private time with the adolescent, a planned handover to adult care</td></tr>
</tbody></table></div>
<p><strong>Measure disease activity the same way each time.</strong> A systemic activity score such as the SLE Disease Activity Index (SLEDAI), linked below, helps you and the rheumatologist speak the same language, while proteinuria, sediment, creatinine and complement track the kidney.</p>
{{flow:Suspected lupus nephritis in a child|Confirm SLE::ANA, anti-dsDNA, complement, blood counts; joint review with rheumatology.|Grade the kidney::Creatinine trend, UPCR, sediment, blood pressure.|Biopsy promptly::Correct platelets and pressure; do not let the list delay a rapidly rising creatinine.|Protect::Tuberculosis and hepatitis B screening, vaccines, hydroxychloroquine, eye examination.|Induce by class::KDIGO 2024 options with the family; counsel on fertility and contraception; doses from the formulary.|Maintain::At least 36 months of total therapy; complete response in children is proteinuria below 0.5 g/1.73 m&sup2;/day.|Keep her engaged::Adherence, school, body image, transition plan.}}
{{call:<ul><li>Creatinine rising over days, or oliguria</li><li>Hemoptysis, falling oxygen saturation or diffuse alveolar hemorrhage</li><li>Seizure, severe headache or hypertensive urgency</li><li>Fever on intensive immunosuppression</li><li>Platelets falling with hemolysis (consider thrombotic microangiopathy, Module 13)</li></ul>}}
{{key:Lupus nephritis in a child is a three-year commitment at least. Plan the maintenance, the monitoring and the adolescent&rsquo;s place in decisions from the first week.}}
"""),
    ],
    "debrief": [
        "<p><strong>Biopsy, and whether to wait.</strong> The biopsy class decides the regimen: proliferative class III or IV needs full induction, class V alone is managed differently, and class VI changes the goal. But her creatinine has doubled in a week, and ten days is too long. Push for an earlier slot once platelets and blood pressure are acceptable, and agree with the rheumatologist whether to start glucocorticoids now, with the biopsy following within days. Start hydroxychloroquine, which KDIGO 2024 recommends for everyone with SLE (1C), and screen for tuberculosis and hepatitis B.</p>",
        "<p><strong>Induction for a 13-year-old.</strong> If the biopsy shows class III or IV, KDIGO 2024 offers glucocorticoids plus an MPAA, low-dose intravenous cyclophosphamide, belimumab with either, or an MPAA with a CNI (each 1B), and advises treating children with regimens similar to adults. Answer the mother directly: cyclophosphamide&rsquo;s effect on fertility rises with cumulative dose, low-dose regimens are designed to limit exposure, and MMF-based induction avoids the drug altogether; SHARE accepts either MMF or intravenous cyclophosphamide for children. Because she is growing, keep glucocorticoid exposure as low as the regimen allows and monitor growth and bone. Discuss contraception, since MMF is teratogenic. Plan at least 36 months of total therapy and aim for proteinuria below 0.5 g/1.73 m&sup2; per day.</p>",
        "<p><strong>If it were ANCA vasculitis.</strong> Pauci-immune necrotizing crescents with MPO-ANCA would make this ANCA-associated GN. Treatment would start on the clinical picture and serology without waiting for the biopsy. KDIGO 2024 lists children and adolescents and patients concerned about fertility among those in whom rituximab is preferred with glucocorticoids, and a reduced-dose glucocorticoid regimen, supported by PEXIVAS in adults, would limit steroid harm. Plasma exchange would be considered if her creatinine exceeded 3.4 mg/dL, if she needed dialysis or her creatinine rose rapidly, or if she developed alveolar hemorrhage with hypoxemia. Hydroxychloroquine would not be part of the plan.</p>",
    ],
    "skills": {"title": 'Lupus nephritis and vasculitis in children',
               "intro": "Complete with a preceptor, in simulation or at your own unit. Sign-off is local.",
               "items": [("Interprets an ISN/RPS lupus nephritis biopsy report and links the class to treatment intensity", False),
                         ("Presents KDIGO 2024 induction options to an adolescent and her family, including fertility and contraception", False),
                         ("Recognizes pulmonary-renal syndrome and starts treatment and transfer without waiting for serology", False),
                         ("Writes a maintenance and monitoring plan covering at least 36 months, growth, bone, eyes and infection", False)],
               "placement": "Pediatric ward, nephrology or joint rheumatology clinic"},
    "quiz": [
        ("What does KDIGO 2024 recommend for all patients with SLE, including those with lupus nephritis?",
         ["Rituximab", "Hydroxychloroquine or an equivalent antimalarial unless contraindicated (1C)", "Plasma exchange", "Long-term high-dose glucocorticoids"],
         1, "Recommendation 10.2.1.1 is graded 1C. It applies whatever the biopsy class."),
        ("How does KDIGO 2024 define complete response of lupus nephritis in children younger than 18?",
         ["Proteinuria below 0.5 g/1.73 m&sup2; per day", "Normal C3 alone", "Negative ANA", "Creatinine below 1.0 mg/dL"],
         0, "The guideline uses a body-surface-area-indexed proteinuria threshold for children."),
        ("Which statement about BLISS-LN and AURORA 1 is correct?",
         ["Both were pediatric trials with kidney failure as the primary outcome", "Both enrolled adults and used proteinuria-based renal response composites; use in adolescents is extrapolation", "Both showed no benefit", "Both compared plasma exchange with no exchange"],
         1, "BLISS-LN: renal response 43% vs 32% at 104 weeks; AURORA 1: complete renal response 41% vs 23% at 52 weeks; both in adults."),
        ("A 14-year-old with cola urine, hemoptysis and rapidly rising creatinine has serology pending for three days. What is the right approach?",
         ["Wait for serology and biopsy before any treatment", "Start glucocorticoids, involve intensive care and transfer to a center with plasma exchange and dialysis now", "Give antibiotics only", "Start hydroxychloroquine and review in a week"],
         1, "KDIGO 2024 advises that biopsy should not delay treatment in a compatible presentation, particularly with rapid deterioration; pulmonary-renal syndrome is an emergency."),
        ("What did PEXIVAS show in adults with severe ANCA vasculitis?",
         ["Plasma exchange halved death or kidney failure", "No significant reduction in death or ESKD with plasma exchange (28.4% vs 31.0%); reduced-dose glucocorticoids were noninferior with fewer serious infections", "Higher mortality with reduced-dose glucocorticoids", "Rituximab was inferior to cyclophosphamide"],
         1, "Hazard ratio 0.86 for plasma exchange; reduced-dose glucocorticoids 27.9% vs 25.5%, with an infection incidence rate ratio of 0.69."),
    ],
    "terms": [("SLE", "Systemic lupus erythematosus"), ("cSLE", "Childhood-onset systemic lupus erythematosus"), ("LN", "Lupus nephritis"),
              ("ISN/RPS", "International Society of Nephrology/Renal Pathology Society"), ("KDIGO", "Kidney Disease: Improving Global Outcomes"),
              ("SHARE", "Single Hub and Access point for Pediatric Rheumatology in Europe (initiative name)"),
              ("STROBE", "Strengthening the Reporting of Observational Studies in Epidemiology"),
              ("MPAA", "Mycophenolic acid analog"), ("MMF", "Mycophenolate mofetil"), ("CNI", "Calcineurin inhibitor"),
              ("eGFR", "Estimated glomerular filtration rate"), ("ANCA", "Antineutrophil cytoplasmic antibody"), ("MPO", "Myeloperoxidase"),
              ("PR3", "Proteinase 3"), ("MPA", "Microscopic polyangiitis"), ("GPA", "Granulomatosis with polyangiitis"),
              ("anti-GBM", "Anti-glomerular basement membrane"), ("ESKD", "End-stage kidney disease"), ("GN", "Glomerulonephritis"),
              ("ANA", "Antinuclear antibody"), ("anti-dsDNA", "Anti-double-stranded DNA antibody"), ("UPCR", "Urine protein-to-creatinine ratio"),
              ("SLEDAI", "Systemic Lupus Erythematosus Disease Activity Index"), ("PP", "Practice point"), ("CKD", "Chronic kidney disease"),
              ("BLISS-LN", "Belimumab in lupus nephritis trial (trial name)"), ("AURORA 1", "Phase 3 trial of voclosporin in lupus nephritis (trial name)"),
              ("PEXIVAS", "Plasma exchange and glucocorticoids in severe ANCA vasculitis trial (trial name)"),
              ("ARChiVe", "A Registry for Childhood Vasculitis: e-entry"), ("IV", "Intravenous")],
    "readings": [('lupus-nephritis.html', 'Lupus Nephritis — When Your Immune System Attacks Your Kidneys'),
                 ('glomerulonephritis.html', 'Glomerulonephritis: When Kidney Filters Become Inflamed'),
                 ('nephritic-syndromes.html', 'Nephritic Syndrome: Recognize It, Act Fast, Find the Cause')],
    "calcs": ["calc-sledai.html", "calc-anca-renal-risk.html", "calc-anti-gbm-renal-risk.html", "calc-pediatric-egfr.html", "calc-urine-protein-excretion.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
