# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 09: Steroid-sensitive nephrotic syndrome.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, for Philippine
practice. Definitions and grades checked against the IPNA 2022 SSNS recommendations (full text, PMC9589698) and the KDIGO 2025
guideline and executive summary (Recommendations 1.3.1.1, 1B; 1.3.2.1, 1C); PREDNOS, PREDNOS 2, Hengel 2024 and Kapur 2009
against PubMed abstracts. Note for sign-off: IPNA 2022 defines frequent relapses as >=2 in the first 6 months or >=3 in any
12 months; the KDIGO 2021 definition used >=4. KDIGO 2025 aligned its definitions with IPNA. No doses."""

MODULE = {
    "image_alt": "A puffy-eyed Filipino preschool boy rests on his mother's lap on a district hospital ward while a pediatric nephrologist presses gently on his fingertip to check capillary refill.",
    "objectives": [
        "Explain nephrotic edema from podocyte injury to sodium retention, and tell the underfilled child from the overfilled child at the bedside.",
        "Treat the first episode of idiopathic nephrotic syndrome as KDIGO 2025 recommends, and classify the response and course with the IPNA 2022 definitions.",
        "Prevent the complications that kill (hypovolemia with acute kidney injury, infection and thrombosis) and teach the family home monitoring.",
    ],
    "big": """<div class="tc-keyp"><span class="tc-lab">Your role &middot; the first episode sets the course</span>Most first episodes of nephrotic syndrome are treated by pediatricians in district and provincial hospitals, often before you hear of the child. You are called when the swelling is dramatic, when the child looks unwell, or when someone wants to give a diuretic. Your advice in that call, and the plan you write for the first 8 to 12 weeks, decides whether the family learns to catch relapses at home or arrives at an emergency room with a shocked, clotted or infected child.</div>
{{plain:Think of the glomerular filter as a coffee filter. A good filter lets water through and holds back the grounds. In nephrotic syndrome the filter has torn, and the protein that should stay in the blood pours into the urine.}}
<p>The picture has a limit. A torn coffee filter is a passive hole. The glomerular barrier is living tissue, and in childhood idiopathic nephrotic syndrome (INS) the main defect sits in the podocyte, the cell whose interdigitating foot processes and slit diaphragm form the final barrier. Under light microscopy the glomeruli usually look normal. Under the electron microscope the foot processes are flattened. The injury is functional and often reversible, which is why most children respond completely to glucocorticoids, and why the disease can return.</p>
{{cards:Key numbers|Incidence (IPNA 2022)::1.15 to 16.9 per 100,000 children per year worldwide|Complete remission with glucocorticoids::About 85% within 4&ndash;6 weeks (IPNA 2022)|At least one relapse::About 70&ndash;80%|Frequent relapses or steroid dependence::About 50%|Antinephrin antibodies (Hengel 2024)::52% of children with INS; 90% of untreated children with active disease|PREDNOS, 16 vs 8 weeks::No difference in time to first relapse (hazard ratio 0.87)}}
<p>Most children with a first episode go into remission and do well. A few are harmed in the first days, by a diuretic given to a child who is already volume depleted, by pneumococcal peritonitis, or by a clot. Your work is to treat the first episode by the guideline, recognize the underfilled child before the furosemide is pushed, prevent infection and thrombosis, and teach the family to read a dipstick.</p>
""",
    "case": {"title": "Furosemide ordered",
             "html": """<p>It is 4 p.m. on a Saturday. A pediatric resident at a district hospital in Bayombong, Nueva Vizcaya, five hours by road from your center, calls about Elijah Ramos, 4 years old. His usual weight is 15 kg; today he weighs 17.4 kg. Over five days his eyes, legs and scrotum have swollen, and his abdomen is tense. Since morning he complains of tummy pain, and he has passed urine twice.</p>
<p>Heart rate 138, blood pressure 88/60, capillary refill 4 seconds, cold hands and feet. Dipstick protein 4+, no blood. Serum albumin 1.4 g/dL, hematocrit 46%, creatinine 0.6 mg/dL. A spot urine sodium is below 10 mmol/L; the resident calculates a fractional excretion of sodium of 0.1%.</p>
<p>The consultant on call has ordered intravenous furosemide &ldquo;for the edema,&rdquo; and the nurse is drawing it up. The hospital has no concentrated albumin in stock this weekend. Elijah&rsquo;s mother, who sells vegetables at the market, asks when the swelling will go down so that he can go home, and whether he can still have his school vaccinations.</p>""",
             "questions": ["Is Elijah underfilled or overfilled, and what do you tell the resident about the furosemide?",
                           "What initial treatment do you advise, and how will you know he has responded?",
                           "What must the family learn before discharge to keep him safe and catch relapses early?"]},
    "sections": [
        ("physiology", "Physiology", "From podocyte to edema",
         """<p>The glomerular barrier has three layers: fenestrated endothelium, the glomerular basement membrane and the podocyte. Podocyte foot processes from neighboring cells interlock, and the slit diaphragm between them, built around the protein nephrin, holds back albumin. When nephrin signaling or the podocyte&rsquo;s actin skeleton is disturbed, the foot processes retract and flatten, and albumin leaks.</p>
<p>For decades the cause of childhood INS was described as an unidentified circulating factor. In 2024 Hengel and colleagues reported autoantibodies against nephrin in 94 of 182 children with INS (52%), and in 90% of children with active disease who were not receiving immunosuppression. Antibody levels tracked disease activity, and immunizing mice with nephrin produced a nephrotic syndrome with IgG at the slit diaphragm.[[apn09_6]] This makes an autoimmune podocytopathy the leading explanation for many children, and it fits the response to glucocorticoids and B-cell therapy. It is a cross-sectional and experimental finding; antinephrin testing is not yet a routine clinical test, and it does not change first-line treatment.</p>
<p><strong>Why albumin falls.</strong> The liver increases albumin synthesis, but not enough to match urinary loss and tubular catabolism of filtered protein. Lipids rise as the liver makes more lipoproteins and their clearance falls.</p>
<p><strong>Why edema forms: two mechanisms, both real.</strong> In the underfill explanation, low plasma oncotic pressure lets fluid leave the capillaries, circulating volume falls, and renin, aldosterone and antidiuretic hormone rise, so the kidney holds salt and water that leak out again. In the overfill explanation, the nephrotic kidney retains sodium primarily, whatever the volume, partly because proteases filtered in the urine, such as plasmin, activate the epithelial sodium channel (ENaC) in the collecting duct. A review in <em>Kidney International</em> proposed that this protease-driven sodium retention is present regardless of volume status, and that other mechanisms add to it.[[apn09_7]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>Underfilled child (volume contracted)</th><th>Overfilled child (volume expanded)</th></tr></thead>
<tbody>
<tr><td>Heart rate and blood pressure</td><td>Tachycardia; low or falling pressure</td><td>Normal heart rate; normal or high pressure</td></tr>
<tr><td>Peripheries</td><td>Cold hands, prolonged capillary refill</td><td>Warm</td></tr>
<tr><td>Abdomen</td><td>Pain, sometimes severe (gut ischemia or peritonitis must be excluded)</td><td>Distension without pain</td></tr>
<tr><td>Urine</td><td>Oliguria; very low urine sodium</td><td>Urine sodium less suppressed</td></tr>
<tr><td>Blood</td><td>High hematocrit; rising urea and creatinine</td><td>Hematocrit not concentrated</td></tr>
<tr><td>What a diuretic does</td><td>Deepens hypovolemia; risks shock, AKI and thrombosis</td><td>Removes salt and water</td></tr>
</tbody></table></div>
<p>A small prospective study of 30 children with severe nephrotic edema used fractional excretion of sodium (FENa) to separate the two. A FENa below 0.2% identified volume contraction, and those children had higher urea, renin, aldosterone and antidiuretic hormone. Children with a higher FENa were treated with diuretics alone, safely, with similar weight loss and hospital stay.[[apn09_8]] The study was small and single-center, so FENa supports the bedside assessment rather than replacing it.</p>
{{key:Before any diuretic, look at the hands, the heart rate and the abdomen. A cold, tachycardic child with abdominal pain is underfilled until proven otherwise.}}
{{fig:apn09_a}}
"""),
        ("complications", "Complications", "The complications that kill",
         """<p>Before glucocorticoids, nephrotic syndrome in childhood carried a mortality of about 40% from acute kidney injury (AKI), infection and thrombosis, according to the IPNA 2022 recommendations.[[apn09_1]] Those three still cause most serious harm, and the first days of an episode are the riskiest.</p>
<p><strong>Hypovolemia and AKI.</strong> The IPNA recommends withholding diuretics in a child with signs of hypovolemia, because of the risks of thrombosis, hypovolemic shock and AKI, and stopping angiotensin-converting enzyme (ACE) inhibitors and angiotensin receptor blockers (grade X, strong recommendation). It recommends concentrated albumin for children with signs of hypovolemia, which it lists as oliguria, AKI, prolonged capillary refill, tachycardia and abdominal discomfort, with a loop diuretic considered during or after the infusion only once volume is restored and urine output remains insufficient (grade C, moderate recommendation).[[apn09_1]] The product, volume and rate come from your unit&rsquo;s pediatric formulary and protocol, and the child is watched closely for fluid overload during the infusion. In an overfilled, hypertensive child, the IPNA suggests diuretics with fluid and salt restriction (grade C, weak recommendation).[[apn09_1]]</p>
<p><strong>Infection.</strong> Children lose immunoglobulin and complement factors in the urine, have tense ascites, and take immunosuppressive drugs. Spontaneous bacterial peritonitis, classically pneumococcal, cellulitis, sepsis and pneumonia follow. Fever with abdominal pain in a nephrotic child is peritonitis until proven otherwise. In the Philippines, also think of dengue in season, and screen for tuberculosis before a long course of glucocorticoids; the IPNA work-up lists tuberculosis and HIV for endemic regions.[[apn09_1]]</p>
<p><strong>Thrombosis.</strong> Loss of antithrombin in the urine, high hepatic production of clotting factors, high hematocrit, immobility and central lines combine. Renal vein, cerebral venous sinus and pulmonary thromboses occur. The IPNA does not recommend routine prophylactic anticoagulation or antiplatelet therapy in the acute stage (grade C, weak recommendation), suggests considering it during relapses when risk is increased (grade C, weak recommendation), and recommends teaching families the risk factors and symptoms.[[apn09_1]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Complication</th><th>Mechanism</th><th>What you see first</th><th>What the attending does</th></tr></thead>
<tbody>
<tr><td>Hypovolemia, AKI</td><td>Low oncotic pressure, leak; diuretics; diarrhea</td><td>Cold peripheries, tachycardia, abdominal pain, oliguria, rising hematocrit</td><td>Stop diuretics and RAAS blockers; albumin per protocol; watch urine output</td></tr>
<tr><td>Peritonitis, sepsis</td><td>Urinary loss of immunoglobulin and complement; ascites; immunosuppression</td><td>Fever, abdominal pain, tenderness</td><td>Cultures, antibiotics per unit protocol, surgical review if needed</td></tr>
<tr><td>Thrombosis</td><td>Antithrombin loss, more clotting factors, hemoconcentration</td><td>Headache, seizure, flank pain, hematuria, breathlessness, a swollen limb</td><td>Urgent imaging; anticoagulation with pediatric hematology</td></tr>
<tr><td>Steroid toxicity</td><td>Cumulative exposure</td><td>Weight gain, behavior change, hypertension, slowed growth</td><td>Count exposure; plan steroid-sparing therapy if relapses mount (Module 10)</td></tr>
</tbody></table></div>
<div class="tc-scene"><span class="tc-lab">On the ward at night, the headache &middot; fictional</span><p>A 7-year-old girl in her second week of a first episode complains of headache and vomits twice. Her edema is improving. The night resident gives an antiemetic.</p><p>You ask for her hematocrit, an urgent neurologic examination and venous imaging of the brain. She has a cerebral venous sinus thrombosis and starts anticoagulation with the hematologist.</p><p class="tc-scene-take"><b>What this shows.</b> New headache in a nephrotic child is a clot until imaging says otherwise.</p></div>
{{key:Fever with abdominal pain is peritonitis, and new headache is a clot, until proven otherwise.}}
{{fig:apn09_b}}
"""),
        ("evidence", "Evidence", "Treating the first episode, and naming the response",
         """<p><strong>Confirm before treating.</strong> The IPNA recommends confirming nephrotic-range proteinuria at least once by quantification, ideally a first-morning urine protein-to-creatinine ratio (UPCR), before treating a first episode.[[apn09_1]] It does not recommend routine kidney biopsy or genetic testing in children older than 1 year with typical features (grade B, moderate recommendation). It recommends biopsy for atypical features: macroscopic hematuria, low C3, AKI not explained by hypovolemia, sustained hypertension, arthritis or rash (grade A, strong recommendation), and suggests genetic testing or biopsy in infantile onset, 3 to 12 months of age.[[apn09_1]]</p>
<p><strong>The definitions.</strong> KDIGO 2025 aligned its definitions of remission, relapse, steroid sensitivity and resistance with those of the IPNA, and introduced a confirmation period between 4 and 6 weeks.[[apn09_2]][[apn09_3]] Use one vocabulary with families and in referral notes.</p>
<div class="table-wrap"><table>
<thead><tr><th>Term</th><th>IPNA 2022 definition</th></tr></thead>
<tbody>
<tr><td>Nephrotic-range proteinuria</td><td>UPCR &ge;200 mg/mmol (2 mg/mg) in a spot urine, or &ge;1000 mg/m&sup2; per day in a 24-hour urine, corresponding to 3+ or 4+ on dipstick</td></tr>
<tr><td>Nephrotic syndrome</td><td>Nephrotic-range proteinuria and either serum albumin &lt;30 g/L or edema when albumin is not available</td></tr>
<tr><td>Complete remission</td><td>UPCR &le;20 mg/mmol (0.2 mg/mg), or negative or trace dipstick, on three or more consecutive days</td></tr>
<tr><td>Partial remission</td><td>UPCR above 20 but below 200 mg/mmol, and serum albumin &ge;30 g/L</td></tr>
<tr><td>Steroid-sensitive (SSNS)</td><td>Complete remission within 4 weeks of glucocorticoid at standard dose</td></tr>
<tr><td>Steroid-resistant (SRNS)</td><td>No complete remission within 4 weeks; partial responders enter a confirmation period from week 4 to week 6</td></tr>
<tr><td>Late responder</td><td>Complete remission during the confirmation period; managed as SSNS</td></tr>
<tr><td>Relapse</td><td>Dipstick &ge;3+ or UPCR &ge;200 mg/mmol on 3 consecutive days in a child who had been in complete remission</td></tr>
<tr><td>Frequently relapsing (FRNS)</td><td>&ge;2 relapses in the first 6 months after remission of the first episode, or &ge;3 relapses in any 12 months</td></tr>
<tr><td>Steroid-dependent (SDNS)</td><td>2 consecutive relapses during glucocorticoid therapy or within 14 days of stopping it</td></tr>
</tbody></table></div>
<p>These definitions come from the IPNA 2022 table.[[apn09_1]] The IPNA notes that its definition of frequent relapses differs from earlier ones, including KDIGO&rsquo;s, which counted four relapses in 12 months; KDIGO 2025 now defines infrequent relapses as fewer than two in the first 6 months or fewer than three in any subsequent 12 months.[[apn09_2]] The Academy&rsquo;s nephrotic course classifier, linked below, applies these definitions to the dates you enter and returns the category and the next question to ask; it gives no doses.</p>
<p><strong>How long to treat.</strong> KDIGO 2025 recommends oral glucocorticoids for 8 weeks or 12 weeks, each as a daily phase followed by an alternate-day phase (Recommendation 1.3.1.1, graded 1B), unchanged from 2021.[[apn09_2]] PREDNOS randomized 237 children in the United Kingdom with a first episode to a standard 8-week course or an extended 16-week course. Time to first relapse did not differ (hazard ratio 0.87, 95% CI 0.65 to 1.17), and neither did frequent relapses (50% vs 53%), steroid dependence (44% vs 42%) or the need for other immunosuppression (56% vs 54%).[[apn09_5]] Longer courses add steroid exposure without fewer relapses. The dose is weight- or surface-area-based, and the unit&rsquo;s pediatric formulary sets it.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>What the evidence shows</th><th>What it does not show</th></tr></thead>
<tbody>
<tr><td>8 vs 16 weeks (PREDNOS)</td><td>No difference in relapse, FRNS or SDNS</td><td>Results in very young children or in populations outside the United Kingdom with certainty; the trial suggested younger children merit further study</td></tr>
<tr><td>Daily glucocorticoid at URTI (PREDNOS 2)</td><td>No reduction in infection-related relapse</td><td>A benefit in South Asian children (a post hoc signal only)</td></tr>
<tr><td>Antinephrin antibodies (Hengel 2024)</td><td>Common in active childhood INS; track activity</td><td>That testing improves outcomes or should change first-line therapy</td></tr>
</tbody></table></div>
{{key:Confirm the proteinuria, treat for 8 or 12 weeks as KDIGO 2025 recommends, and name the response with the IPNA definitions.}}
{{fig:apn09_c}}
"""),
        ("practice", "Practice", "Home monitoring, vaccines and the long run",
         """<p><strong>Teach the dipstick.</strong> The IPNA recommends teaching families to monitor urine protein at home, so that response and relapse are detected early (grade X, moderate recommendation). Where dipsticks are not available, it suggests the heat coagulation or sulfosalicylic acid test as alternatives (grade C, weak recommendation).[[apn09_1]] Give the family a diary card, show them how to read a first-morning sample, and tell them exactly when to call: three consecutive days at 3+ or more, or edema with any proteinuria.</p>
<p><strong>Infections and relapses.</strong> Many relapses follow upper respiratory tract infections (URTIs). PREDNOS 2 randomized children with relapsing SSNS to 6 days of daily low-dose prednisolone or placebo at the start of each URTI; 365 were enrolled and 271 formed the modified intention-to-treat population. Infection-related relapse occurred in 42.7% with prednisolone and 44.3% with placebo, an adjusted risk difference of &minus;0.02 (95% CI &minus;0.14 to 0.10).[[apn09_4]] KDIGO 2025 now recommends against routinely giving daily glucocorticoids during infections in children with frequent relapses or steroid dependence (Recommendation 1.3.2.1, graded 1C), with a practice point that allows a short low-dose course in selected children.[[apn09_3]]</p>
<p><strong>Vaccines.</strong> Inactivated vaccines follow the national schedule, with particular attention to pneumococcal, meningococcal and <em>H. influenzae</em> type b (Hib) vaccines and annual influenza vaccine; the IPNA reports that the risk of vaccine-induced relapse is low. Live vaccines are avoided during high-dose immunosuppression and in the first 6 months after rituximab (grade X, strong recommendation), and the household should be vaccinated against influenza and with live vaccines when the child cannot be (grade A, strong recommendation).[[apn09_1]] Elijah&rsquo;s mother&rsquo;s question deserves a precise answer from you, written in his discharge plan.</p>
<p><strong>Watch the cost of steroids.</strong> IPNA describes steroid toxicity as new or worsening obesity, sustained hypertension, hyperglycemia, behavioral or psychiatric disorders, sleep disruption, impaired growth and Cushingoid features.[[apn09_1]] Measure height, weight and blood pressure at every visit and plot them. A child with mounting toxicity is a child for Module 10.</p>
<div class="table-wrap"><table>
<thead><tr><th>Before discharge, the family can&hellip;</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Read a first-morning dipstick and fill in the diary</td><td>Relapses caught at home are treated before edema and complications</td></tr>
<tr><td>Name the warning signs: fever with abdominal pain, cold hands with fast breathing or poor urine, severe headache, a swollen limb</td><td>Peritonitis, hypovolemia and thrombosis kill within hours</td></tr>
<tr><td>Give the glucocorticoid in the morning, as written, and never stop it suddenly</td><td>Adherence and adrenal safety</td></tr>
<tr><td>State which vaccines are allowed now and which must wait</td><td>Avoids both missed protection and unsafe live vaccines</td></tr>
<tr><td>Reach your clinic or the covering pediatrician by phone</td><td>A five-hour drive needs a plan before it is needed</td></tr>
</tbody></table></div>
{{flow:First episode, district hospital|Assess volume::Heart rate, blood pressure, capillary refill, abdomen, urine output, hematocrit; FENa if available.|Protect::No diuretic in the underfilled child; albumin per protocol; treat infection; mobilize.|Confirm::Quantify proteinuria (first-morning UPCR) and check albumin, creatinine, C3 if any atypical feature.|Treat::Glucocorticoid for 8 or 12 weeks as KDIGO 2025 recommends; dose from the unit formulary.|Name the response::Complete remission by 4 weeks, late response by 6 weeks, or SRNS (Module 10).|Teach::Dipstick diary, warning signs, vaccines, a phone number.|Follow::Growth, blood pressure and steroid toxicity at every visit; classify the course with the IPNA definitions.}}
{{call:<ul><li>Tachycardia, cold peripheries or hypotension in an edematous child</li><li>Fever with abdominal pain or tenderness</li><li>New headache, seizure, flank pain or a swollen limb</li><li>Rising creatinine, macroscopic hematuria, low C3 or sustained hypertension (atypical features: think biopsy)</li><li>No complete remission by 4 weeks of standard glucocorticoid</li></ul>}}
{{key:Discharge is safe when the family can read a dipstick, name the warning signs and reach you by phone.}}
"""),
    ],
    "debrief": [
        "<p><strong>Underfilled or overfilled?</strong> Elijah is underfilled: tachycardia, cold peripheries, a capillary refill of 4 seconds, abdominal pain, oliguria, a hematocrit of 46%, a creatinine high for his age and a FENa of 0.1%. Ask the nurse to hold the furosemide now. A diuretic would deepen his hypovolemia and raise the risk of shock, AKI and thrombosis; the IPNA recommends withholding it (grade X, strong). Ask the resident to examine the abdomen for peritonitis and send blood cultures if he has fever or tenderness. He needs concentrated albumin per protocol, given with close monitoring; since the hospital has none, arrange transfer or emergency supply today, with a written endorsement and a direct call to the accepting doctor.</p>",
        "<p><strong>Initial treatment and response.</strong> Confirm nephrotic-range proteinuria with a first-morning UPCR, check C3 because he has AKI, and screen for tuberculosis exposure. With typical features at age 4, he needs no biopsy now. Start oral glucocorticoids for an 8- or 12-week course as KDIGO 2025 recommends (1B), with the dose from the unit&rsquo;s pediatric formulary. Complete remission is a negative or trace dipstick, or UPCR &le;0.2 mg/mg, on three consecutive days; if it comes within 4 weeks, he has SSNS. If he is only in partial remission at 4 weeks, the confirmation period runs to 6 weeks; no remission by then is SRNS and a Module 10 problem.</p>",
        "<p><strong>Before discharge.</strong> His mother learns to read a first-morning dipstick and keep a diary, to call for three consecutive days at 3+ or more, and to bring him in at once for fever with abdominal pain, cold hands with poor urine, severe headache or a swollen limb. Write which vaccines he may have now (inactivated vaccines on schedule, influenza yearly) and which must wait (live vaccines while on high-dose glucocorticoids), and ask that the household be vaccinated. Give her your clinic number and the name of the covering pediatrician in Bayombong.</p>",
    ],
    "skills": {"title": 'Steroid-sensitive nephrotic syndrome',
               "intro": "Complete with a preceptor, in simulation or at your own unit. Sign-off is local.",
               "items": [("Assesses intravascular volume in an edematous nephrotic child and decides on diuretic versus albumin", False),
                         ("Applies the IPNA 2022 definitions of remission, relapse, FRNS, SDNS and SRNS to a real course", False),
                         ("Identifies atypical features that call for biopsy or genetic testing", False),
                         ("Teaches a family dipstick monitoring, warning signs and vaccine rules", False)],
               "placement": "Pediatric ward, nephrology clinic or simulation"},
    "quiz": [
        ("A nephrotic 4-year-old has tachycardia, capillary refill of 4 seconds, abdominal pain and a FENa of 0.1%. Furosemide is ordered. What do you advise?",
         ["Give furosemide and repeat in 6 hours", "Hold the diuretic; give albumin per protocol with monitoring and exclude peritonitis", "Restrict fluids and give spironolactone", "Start anticoagulation"],
         1, "These are signs of hypovolemia. The IPNA recommends withholding diuretics in hypovolemia (grade X, strong) and using albumin; FENa below 0.2% suggested volume contraction in a small prospective study."),
        ("By the IPNA 2022 definitions, which course is frequently relapsing?",
         ["One relapse in the first 6 months", "Two relapses in the first 6 months after remission of the first episode", "Relapse only during infections", "Two relapses during steroid therapy"],
         1, "FRNS is &ge;2 relapses in the first 6 months after remission, or &ge;3 in any 12 months. Two consecutive relapses on therapy or within 14 days of stopping define steroid dependence."),
        ("What did PREDNOS show?",
         ["16 weeks halved relapses", "16 weeks did not lengthen time to first relapse compared with 8 weeks (hazard ratio 0.87)", "8 weeks caused more steroid dependence", "Daily steroids at each cold prevented relapse"],
         1, "FRNS (50% vs 53%), SDNS (44% vs 42%) and need for other immunosuppression did not differ. KDIGO 2025 recommends 8 or 12 weeks (1B)."),
        ("Which feature in a child with a first episode of nephrotic syndrome calls for kidney biopsy according to the IPNA?",
         ["Age 4 years", "Edema of the scrotum", "Macroscopic hematuria or a low C3", "Serum albumin of 1.5 g/dL"],
         2, "Atypical features (macroscopic hematuria, low C3, AKI not from hypovolemia, sustained hypertension, arthritis or rash) call for biopsy (grade A, strong). Typical disease over age 1 does not."),
        ("A nephrotic child on high-dose glucocorticoids is due for school vaccinations. What is correct?",
         ["Postpone all vaccines until steroids stop", "Give inactivated vaccines on schedule; avoid live vaccines during high-dose immunosuppression; vaccinate the household", "Give all live vaccines now", "Vaccines cause most relapses, so avoid them for life"],
         1, "The IPNA reports a low risk of vaccine-induced relapse, recommends avoiding live vaccines during high-dose immunosuppression (grade X), and recommends vaccinating the household (grade A)."),
    ],
    "terms": [("INS", "Idiopathic nephrotic syndrome"), ("SSNS", "Steroid-sensitive nephrotic syndrome"), ("SRNS", "Steroid-resistant nephrotic syndrome"),
              ("FRNS", "Frequently relapsing nephrotic syndrome"), ("SDNS", "Steroid-dependent nephrotic syndrome"),
              ("IPNA", "International Pediatric Nephrology Association"), ("KDIGO", "Kidney Disease: Improving Global Outcomes"),
              ("UPCR", "Urine protein-to-creatinine ratio"), ("FENa", "Fractional excretion of sodium"), ("ENaC", "Epithelial sodium channel"),
              ("AKI", "Acute kidney injury"), ("ACE", "Angiotensin-converting enzyme"), ("RAAS", "Renin-angiotensin-aldosterone system"),
              ("URTI", "Upper respiratory tract infection"), ("PREDNOS", "Prednisolone in Nephrotic Syndrome trials"),
              ("HIV", "Human immunodeficiency virus"), ("CI", "Confidence interval"), ("IgG", "Immunoglobulin G"), ("Hib", "<em>H. influenzae</em> type b vaccine")],
    "readings": [('nephrotic-syndrome.html', 'Nephrotic Syndrome: When the Kidney Filter Leaks Protein'),
                 ('ckd-children-young-adults.html', 'CKD in Children & Young Adults')],
    "calcs": ["calc-pediatric-nephrotic-course.html", "calc-corticosteroid-conversion.html", "calc-fena-feurea.html", "calc-urine-protein-excretion.html", "calc-pediatric-uo.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
