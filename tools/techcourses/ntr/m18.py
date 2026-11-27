# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 18: Immune kidney disease and systemic illness.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. KDIGO 2024 lupus
nephritis (hydroxychloroquine 1C, initial therapy options 1B, MPAA maintenance 1B, 36-month practice point, response
definitions) and KDIGO 2024 ANCA vasculitis (Recommendation 9.3.1.1, 1B; Practice Point 9.3.1.9 as corrected) checked against
kdigo.org; BLISS-LN, AURORA 1, RAVE, PEXIVAS, ADVOCATE, ISN/RPS 2018 revision and the IKMG MGRS consensus checked against
PubMed abstracts; WHO tuberculosis figure from the Global Tuberculosis Report 2025. No doses. Fictional case."""

MODULE = {
 'image_alt': 'A nephrology fellow explains a kidney biopsy plan to a young Filipina woman with lupus and her mother at the bedside, while a resident reviews a urine sediment report on a tablet.',
 'objectives': [
  '<strong>Intern:</strong> Recognize the rapidly progressive pattern (a creatinine rising over days, a nephritic urine, hemoptysis or a systemic rash) and report it to the resident at once, with the history of infections, medicines and tuberculosis contacts.',
  '<strong>Resident:</strong> Send the urgent serologies (antineutrophil cytoplasmic antibodies, anti-glomerular basement membrane antibodies, complement, antinuclear and anti-double-stranded DNA antibodies), start the pre-immunosuppression safety screen, and escalate the same day.',
  '<strong>Fellow:</strong> Manage lupus nephritis and ANCA-associated vasculitis by the Kidney Disease: Improving Global Outcomes (KDIGO) 2024 guidelines with their stated grades, recognize anti-GBM, paraprotein and infection-related kidney disease, and adapt treatment to Philippine tuberculosis risk and cost.'],
 'big': """<div class="tc-keyp"><span class="tc-lab">Your role &middot; the systemic illness that is quietly destroying the kidneys</span>The <strong>intern</strong> notices the rash, the joint pains, the cough with streaks of blood, the urine that has turned dark, and the creatinine that was higher today than yesterday. Report it the same day and take a careful history of infections, tuberculosis contacts and medicines. The <strong>resident</strong> sends the serologies that answer the urgent question first and starts the safety screen that every immunosuppressed patient needs. The <strong>fellow</strong> plans the biopsy, chooses the regimen from the KDIGO 2024 options with the attending, and makes sure the patient survives the treatment as well as the disease.</div>
{{plain:Think of the immune system as a fire brigade that has been sent to the wrong address. In lupus it arrives with buckets of immune complexes and floods the glomeruli. In ANCA vasculitis it sends neutrophils that burn the walls of small vessels. In anti-GBM disease it attacks the building&rsquo;s frame directly. Each brigade does its damage in days, and each needs to be called off with a different order.}}
<p>The picture has a limit. A fire brigade can be recalled with one message; an autoimmune response cannot. Immunosuppression stops new damage, but it cannot rebuild glomeruli that have already scarred, and it leaves the patient open to real infections, including tuberculosis and hepatitis B, which are common in the Philippines. The physiology that matters is the <strong>crescent</strong>. When the capillary wall ruptures, fibrin, macrophages and proliferating cells fill Bowman&rsquo;s space. A <em>cellular</em> crescent can still resolve with treatment. Within days to weeks it becomes <em>fibrocellular</em> and then <em>fibrous</em>, and the glomerulus behind it is lost for good. That is why rapidly progressive glomerulonephritis is a race against time.</p>
{{cards:Key numbers|Lupus nephritis, hydroxychloroquine (KDIGO 2024)::Recommended for all patients with SLE, including lupus nephritis, unless contraindicated (1C)|Lupus nephritis, total immunosuppression (KDIGO 2024)::Initial plus maintenance for proliferative disease at least 36 months (practice point)|ANCA vasculitis, initial treatment (KDIGO 2024)::Glucocorticoids with cyclophosphamide or rituximab (1B)|ANCA vasculitis, plasma exchange (KDIGO 2024 practice point)::Consider for creatinine above 3.4 mg/dL (300 &micro;mol/L), dialysis, rapidly rising creatinine, or alveolar hemorrhage with hypoxemia|PEXIVAS, 704 patients::Death or kidney failure 28.4% with plasma exchange versus 31.0% without (no significant difference)|Philippines, tuberculosis (WHO 2025)::6.8% of the world&rsquo;s incident cases in 2024, third highest of any country}}
<p>Most immune kidney diseases you meet will be lupus nephritis in a young woman and ANCA vasculitis in an older adult, with infection-related and paraprotein disease close behind. A few are anti-GBM disease, where hours count. Your work is to recognize the rapidly progressive pattern, send the right tests the same day, get tissue when it will change the plan, choose a regimen with a known grade behind it, and screen and protect the patient before the first immunosuppressive dose.</p>
""",
 'case': {'title': 'The student who stopped her tablets',
  'html': """<p>Monday, 4 p.m., the medical ward of a government hospital in Cebu City. Angelica Ramos, 19, a nursing student, was diagnosed with systemic lupus erythematosus (SLE) a year ago after a facial rash and painful joints. She stopped hydroxychloroquine six months ago because her family could not afford it after her father&rsquo;s overseas contract in Saudi Arabia ended. For two weeks her legs have been swelling and her urine looks foamy and darker.</p>
<p>Her blood pressure is 158/96 mm Hg. Creatinine is 1.8 mg/dL; it was 0.7 mg/dL three months ago at the rheumatology clinic. Urine shows 3+ protein, dysmorphic red cells and a few red cell casts; the UPCR is 3.2 g/g. Hemoglobin is 9.0 g/dL, platelets 110,000/&micro;L, C3 and C4 are low, and anti-double-stranded DNA is strongly positive. Her grandfather, who lives with the family, finished tuberculosis treatment last year. The intern has written &ldquo;lupus flare, for steroids&rdquo; and asks whether to give the first dose tonight.</p>
""",
  'questions': ['Is this rapidly progressive, and what must happen today?',
                'What will the biopsy add, and how will you choose the initial treatment?',
                'What must be done before and during immunosuppression for this Filipino patient?']},
 'sections': [
  ('rpgn', 'RPGN', 'Rapidly progressive glomerulonephritis: the race against crescents',
   """<p>Rapidly progressive glomerulonephritis (RPGN) is a clinical description, not a diagnosis: a nephritic urine with kidney function falling over days to weeks. Its pathologic correlate is crescentic glomerulonephritis. The causal chain is the same whatever the trigger. Immune injury ruptures the capillary wall; plasma proteins and fibrin leak into Bowman&rsquo;s space; macrophages and parietal epithelial cells proliferate into a crescent; the crescent compresses the tuft; filtration stops; the crescent scars. The clinical clock is the crescent&rsquo;s clock.</p>
<p>Immunofluorescence sorts RPGN into three mechanisms, and the serologies predict which one you will see.</p>
<div class="table-wrap"><table><thead><tr><th>Mechanism</th><th>Immunofluorescence</th><th>Serology</th><th>Common causes</th></tr></thead><tbody>
<tr><td>Anti-GBM antibody</td><td>Linear IgG along the basement membrane</td><td>Anti-GBM antibody positive</td><td>Anti-GBM disease, with or without lung hemorrhage</td></tr>
<tr><td>Immune complex</td><td>Granular deposits</td><td>Low complement, ANA, anti-dsDNA, ASO, cryoglobulins depending on cause</td><td>Lupus nephritis, IgA nephropathy or vasculitis, post-infectious GN</td></tr>
<tr><td>Pauci-immune</td><td>Little or no immunoglobulin</td><td>ANCA (MPO or PR3) positive in most</td><td>Microscopic polyangiitis, granulomatosis with polyangiitis</td></tr>
</tbody></table></div>
<p>The intern&rsquo;s trigger for escalation is simple: a nephritic urine plus a creatinine that is higher than the last known value, or higher today than yesterday. Add any of hemoptysis, a purpuric rash, sinusitis with crusting or bleeding, mononeuritis, or a new pulmonary infiltrate, and the patient may have a pulmonary-renal syndrome. The resident sends antineutrophil cytoplasmic antibodies (ANCA), anti-glomerular basement membrane (anti-GBM) antibodies, complement C3 and C4, antinuclear antibody (ANA) and anti-double-stranded DNA (anti-dsDNA) the same day, and calls the fellow. The fellow arranges a biopsy as soon as it is safe and, with the attending, decides whether treatment must begin before the result.</p>
<p>KDIGO 2024 states that in a patient with a presentation compatible with small-vessel vasculitis and a positive MPO- or PR3-ANCA, immunosuppressive treatment should not be delayed while waiting for a biopsy, especially in a patient who is deteriorating rapidly.[[ntr18_2]] The same logic applies to anti-GBM disease.[[ntr18_4]]</p>
{{fig:ntr18_a}}
{{call:Stop and call the attending nephrologist now, per unit protocol, but always ask the attending nephrologist for guidance, when you see:<ul><li>A nephritic urine with a creatinine rising over days</li><li>Hemoptysis, a falling hemoglobin with new lung infiltrates, or oxygen requirement in a patient with hematuria</li><li>Oliguria, or potassium, acidosis or fluid overload approaching dialysis indications</li><li>A positive ANCA or anti-GBM result on a send-out test</li><li>Fever, a new cough or breathlessness in a patient already on immunosuppression</li></ul>}}
{{key:A nephritic urine with a creatinine rising over days is RPGN until proven otherwise. Send ANCA, anti-GBM and complement today, and let the attending decide whether treatment starts before the biopsy.}}
"""),
  ('lupus', 'Lupus nephritis', 'Lupus nephritis: class, activity, and the KDIGO 2024 options',
   """<p>In SLE, nuclear antigens released from dying cells form immune complexes with autoantibodies such as anti-dsDNA. The complexes deposit in the mesangium, beneath the endothelium or beneath the podocyte, or form there. Where they sit decides the class. Mesangial deposits cause mild disease. Subendothelial deposits face the blood, attract inflammatory cells and complement, and cause proliferative disease (class III if under half of glomeruli, class IV if half or more). Subepithelial deposits are hidden from the circulation by the basement membrane and injure the podocyte, causing membranous disease (class V) with nephrotic proteinuria.</p>
<div class="table-wrap"><table><thead><tr><th>ISN/RPS class</th><th>Where deposits sit</th><th>What you see</th><th>What it means for treatment</th></tr></thead><tbody>
<tr><td>I and II</td><td>Mesangium</td><td>Mild hematuria or protein, normal GFR</td><td>Usually no kidney-specific immunosuppression; treat the SLE</td></tr>
<tr><td>III and IV</td><td>Subendothelial, with proliferation</td><td>Nephritic urine, rising creatinine, often low complement and high anti-dsDNA</td><td>Initial and maintenance immunosuppression by KDIGO 2024</td></tr>
<tr><td>V</td><td>Subepithelial</td><td>Nephrotic syndrome, bland or mild sediment</td><td>Supportive care; immunosuppression for nephrotic-range or persistent proteinuria, per KDIGO figure</td></tr>
<tr><td>VI</td><td>Global sclerosis in 90% or more of glomeruli</td><td>Advanced CKD</td><td>Prepare for kidney replacement; immunosuppression only for extrarenal SLE</td></tr>
</tbody></table></div>
<p>The 2018 revision of the International Society of Nephrology/Renal Pathology Society (ISN/RPS) classification clarified definitions of crescents and endocapillary hypercellularity, eliminated the class IV-S and IV-G subdivisions, and replaced the &ldquo;active&rdquo; and &ldquo;chronic&rdquo; labels with modified National Institutes of Health (NIH) activity and chronicity indices to be reported for all classes.[[ntr18_5]] Read both indices. A high activity index with a low chronicity index is the patient most likely to recover with treatment.</p>
<p><strong>When to biopsy.</strong> KDIGO 2024 suggests 0.5 g/day of proteinuria as a threshold for further investigation, with a kidney biopsy considered when it is reached, and notes that proteinuria can look modest in severe active nephritis.[[ntr18_1]]</p>
<p><strong>What KDIGO 2024 recommends.</strong> Hydroxychloroquine for every patient with SLE, including lupus nephritis, unless contraindicated (1C). For active class III or IV disease, glucocorticoids plus one of: a mycophenolic acid analog (MPAA); low-dose intravenous cyclophosphamide; belimumab with either MPAA or low-dose cyclophosphamide; or MPAA with a calcineurin inhibitor in patients without significantly impaired kidney function (all 1B). After initial therapy, MPAA for maintenance (1B), with total immunosuppression for proliferative disease of at least 36 months (practice point).[[ntr18_1]] A complete response is proteinuria below 0.5 g/g with stable kidney function; a partial response is a fall of at least 50% to below 3 g/g; responses are judged over 6 to 12 months, and complete response may take longer.[[ntr18_1]]</p>
<p><strong>The trials behind the add-on options.</strong> BLISS-LN randomized 448 adults with biopsy-proven active lupus nephritis on standard therapy to belimumab or placebo for 104 weeks. A primary efficacy renal response occurred in 43% versus 32%, and a complete renal response in 30% versus 20%; the risk of a renal-related event or death was lower (hazard ratio 0.51).[[ntr18_6]] About 11 more patients per 100 reached the primary response, roughly one for every 9 treated. AURORA 1 randomized 357 patients with class III, IV or V disease on mycophenolate and low-dose steroids to voclosporin or placebo; complete renal response at 52 weeks occurred in 41% versus 23%, with serious adverse events in 21% of each group.[[ntr18_7]] Renal response is a composite of proteinuria and eGFR, a surrogate for long-term kidney survival; both trials were too short to count kidney failure as the main outcome.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>Childhood-onset lupus is more often severe and more often involves the kidneys than adult-onset disease, and growth, puberty, school and long-term glucocorticoid exposure change every treatment choice. Cyclophosphamide exposure and fertility weigh heavily in adolescents, and adherence often falters during transition. See <a href="attending-pediatric-nephrologist-12-lupus-vasculitis.html">Attending Pediatric Nephrologist, Module 12</a>.</div>
{{fig:ntr18_b}}
{{key:In lupus nephritis, treat the class and the activity, not the serology alone. Hydroxychloroquine for everyone; for class III or IV, glucocorticoids plus a KDIGO 1B partner chosen with the patient&rsquo;s fertility, cost and adherence in mind.}}
"""),
  ('anca-gbm', 'ANCA and anti-GBM', 'ANCA vasculitis and anti-GBM disease',
   """<p><strong>ANCA vasculitis.</strong> ANCA bind myeloperoxidase (MPO) or proteinase 3 (PR3) on primed neutrophils. Activated neutrophils stick to small-vessel walls, degranulate and release extracellular traps, causing necrotizing inflammation with few immune deposits, hence &ldquo;pauci-immune.&rdquo; The alternative complement pathway amplifies the injury through C5a, which recruits and primes more neutrophils. That last step is the target of avacopan, a C5a receptor inhibitor.</p>
<p><strong>What KDIGO 2024 recommends.</strong> Glucocorticoids in combination with cyclophosphamide or rituximab as initial treatment of new-onset ANCA-associated vasculitis (1B). Avacopan may be used as an alternative to glucocorticoids. Rituximab is preferred in children and adolescents, premenopausal women and men concerned about fertility, and relapsing disease; relapses should be re-induced, preferably with rituximab. Plasma exchange should be considered for patients with a serum creatinine above 3.4 mg/dL (300 &micro;mol/L), those requiring dialysis or with rapidly rising creatinine, and those with diffuse alveolar hemorrhage who have hypoxemia (Practice Point 9.3.1.9 as corrected).[[ntr18_2]][[ntr18_3]]</p>
<div class="table-wrap"><table><thead><tr><th>Trial</th><th>Design and size</th><th>Result</th><th>What it changed</th></tr></thead><tbody>
<tr><td>RAVE (2010)</td><td>Double-blind, 197 ANCA-positive patients, rituximab versus cyclophosphamide</td><td>Remission without prednisone at 6 months 64% versus 53% (noninferior); in relapsing disease 67% versus 42%[[ntr18_8]]</td><td>Rituximab as an induction option, preferred in relapse</td></tr>
<tr><td>PEXIVAS (2020)</td><td>2-by-2 factorial, 704 patients with eGFR below 50 or alveolar hemorrhage</td><td>Death or kidney failure 28.4% with plasma exchange versus 31.0% without (HR 0.86, not significant); reduced-dose glucocorticoids noninferior (27.9% versus 25.5%), with fewer serious infections at 1 year (IRR 0.69)[[ntr18_9]]</td><td>Plasma exchange no longer routine; lower glucocorticoid exposure</td></tr>
<tr><td>ADVOCATE (2021)</td><td>331 patients, avacopan versus prednisone taper, all on cyclophosphamide or rituximab</td><td>Remission at week 26 72.3% versus 70.1% (noninferior); sustained remission at week 52 65.7% versus 54.9% (superior)[[ntr18_10]]</td><td>Avacopan as an alternative to glucocorticoids</td></tr>
</tbody></table></div>
<p>Read PEXIVAS carefully. The primary outcome showed no significant benefit from plasma exchange, which is why KDIGO moved it from routine to a considered option in the sickest patients. The confidence interval was wide, so a modest benefit in a subgroup was not excluded. Plasma exchange machines and fresh frozen plasma or albumin are scarce outside large Philippine centers. If the attending considers it, plan transfer early, not after the patient is on dialysis.</p>
<p><strong>Anti-GBM disease.</strong> Antibodies against the noncollagenous domain of type IV collagen bind the glomerular and alveolar basement membranes directly. Immunofluorescence shows linear IgG. The disease moves fast, and kidney outcome depends heavily on the creatinine and the need for dialysis at presentation. KDIGO 2021 advises initiating cyclophosphamide, glucocorticoids and plasma exchange in all patients with anti-GBM glomerulonephritis except those who are dialysis-dependent at presentation, have 100% crescents or extensive global sclerosis on an adequate biopsy, and have no pulmonary hemorrhage.[[ntr18_4]] It also advises starting treatment without delay if anti-GBM disease is suspected, while results are pending.[[ntr18_4]] Some patients are positive for both ANCA and anti-GBM; KDIGO lists them among those for whom plasma exchange should be considered.[[ntr18_2]]</p>
{{key:In ANCA vasculitis, the 1B choice is glucocorticoids with rituximab or cyclophosphamide; plasma exchange is for the sickest, and less glucocorticoid is safer. In anti-GBM disease, treat on suspicion, and do it today.}}
"""),
  ('paraprotein', 'Paraprotein', 'Paraprotein kidney disease and MGRS',
   """<p>A plasma cell or B-cell clone can injure the kidney without ever becoming a malignancy that needs treatment on hematologic grounds. The monoclonal immunoglobulin or its free light chain is the toxin. The chain of events depends on where the protein goes. Free light chains filtered in large amounts overwhelm the proximal tubule, then precipitate with Tamm&ndash;Horsfall protein in the distal tubule as casts that obstruct it: cast nephropathy, usually with myeloma. Light chains that misfold into fibrils deposit as amyloid in the glomeruli and cause nephrotic syndrome. Other forms deposit as granular material (monoclonal immunoglobulin deposition disease), or activate complement (C3 glomerulopathy with a monoclonal protein), or damage endothelium (thrombotic microangiopathy).</p>
<p>The International Kidney and Monoclonal Gammopathy Research Group defines monoclonal gammopathy of renal significance (MGRS) as a clonal disorder that produces a nephrotoxic monoclonal immunoglobulin but does not meet hematologic criteria for treatment of a specific malignancy. It recommends a kidney biopsy with immunofluorescence when MGRS is suspected; serum and urine protein electrophoresis with immunofixation and serum free light chains to identify the protein; and bone marrow examination to find the clone.[[ntr18_11]]</p>
<div class="table-wrap"><table><thead><tr><th>Lesion</th><th>What you see</th><th>Clue on the biopsy</th></tr></thead><tbody>
<tr><td>Cast nephropathy</td><td>AKI, often with anemia, hypercalcemia, bone pain; dipstick protein low but total urine protein high</td><td>Fractured, light-chain-restricted casts in distal tubules</td></tr>
<tr><td>AL amyloidosis</td><td>Nephrotic syndrome, large kidneys, low blood pressure, heart or nerve involvement</td><td>Congo red positive, apple-green birefringence, light chain restriction</td></tr>
<tr><td>MIDD and other MGRS lesions</td><td>Proteinuria, CKD, sometimes hematuria</td><td>Monotypic deposits on immunofluorescence</td></tr>
</tbody></table></div>
<p>The intern&rsquo;s clue is the mismatch: a dipstick that shows little protein while a quantified urine protein is high, because the dipstick detects albumin and misses light chains. The resident&rsquo;s clue is an older adult with unexplained AKI, anemia and a high calcium, or a nephrotic patient with heart failure and low blood pressure. Send the protein studies early; a serum protein electrophoresis alone can miss a small free light chain clone. The fellow coordinates with hematology, because treatment is directed at the clone.</p>
{{key:Unexplained kidney disease in an older adult, a dipstick that does not match the urine protein, or nephrotic syndrome with a stiff heart: send serum free light chains and immunofixation, and think of the clone.}}
"""),
  ('infection', 'Infection', 'Infection-related kidney disease, and infection caused by treatment',
   """<p>Infection reaches the glomerulus in two ways. Some infections drive immune-complex disease: the classic is post-streptococcal glomerulonephritis in children, but in adults, especially older adults with diabetes, staphylococcal infection can cause an IgA-dominant glomerulonephritis while the infection is still active. Chronic infections cause chronic glomerular disease: hepatitis B with membranous nephropathy, hepatitis C with cryoglobulinemic membranoproliferative disease, HIV with collapsing FSGS (HIV-associated nephropathy), and long-standing infections such as tuberculosis with AA amyloidosis or interstitial nephritis. KDIGO 2021 covers infection-related glomerular disease and stresses treating the infection as the main therapy.[[ntr18_4]]</p>
<div class="table-wrap"><table><thead><tr><th>Infection</th><th>Kidney lesion</th><th>Main treatment principle</th></tr></thead><tbody>
<tr><td>Streptococcal throat or skin</td><td>Post-infectious GN, low C3 recovering over weeks</td><td>Supportive; treat volume and blood pressure</td></tr>
<tr><td>Staphylococcal (endocarditis, diabetic foot, abscess)</td><td>Infection-associated GN, sometimes IgA-dominant</td><td>Eradicate the infection; immunosuppression may harm</td></tr>
<tr><td>Hepatitis B</td><td>Membranous nephropathy, MPGN</td><td>Antiviral therapy; avoid immunosuppression without antiviral cover</td></tr>
<tr><td>Hepatitis C</td><td>Cryoglobulinemic MPGN</td><td>Direct-acting antivirals; immunosuppression for severe disease with specialist input</td></tr>
<tr><td>HIV</td><td>HIV-associated nephropathy, immune-complex disease</td><td>Antiretroviral therapy</td></tr>
<tr><td>Tuberculosis</td><td>Interstitial nephritis, AA amyloidosis, sterile pyuria</td><td>Antituberculous therapy</td></tr>
</tbody></table></div>
<p>The other side of infection is what immunosuppression does. In the Philippines, tuberculosis is not a remote risk. The World Health Organization estimates that the Philippines accounted for 6.8% of the world&rsquo;s incident tuberculosis cases in 2024, the third highest share of any country.[[ntr18_12]] A patient started on high-dose glucocorticoids and cyclophosphamide or rituximab without a tuberculosis screen may reactivate latent infection within weeks. Hepatitis B reactivation after rituximab can cause fulminant hepatitis; KDIGO 2021 advises screening for hepatitis B before rituximab and other immunosuppression.[[ntr18_4]] PEXIVAS showed that a lower glucocorticoid exposure reduced serious infections at one year without worsening the kidney outcome.[[ntr18_9]]</p>
<div class="table-wrap"><table><thead><tr><th>Before the first dose</th><th>Why</th></tr></thead><tbody>
<tr><td>Tuberculosis history, contacts, chest radiograph; interferon-gamma release assay or tuberculin test where available</td><td>Latent tuberculosis reactivates under immunosuppression</td></tr>
<tr><td>Hepatitis B surface antigen and core antibody; hepatitis C; HIV</td><td>Reactivation, and drug interactions with antivirals</td></tr>
<tr><td>Strongyloides serology or empiric treatment where endemic, per protocol</td><td>Hyperinfection under glucocorticoids</td></tr>
<tr><td>Pregnancy test and contraception plan; fertility counseling before cyclophosphamide</td><td>Teratogenicity and gonadal toxicity</td></tr>
<tr><td>Vaccination review, pneumocystis prophylaxis per protocol, bone protection</td><td>Opportunistic infection and steroid harm</td></tr>
</tbody></table></div>
<p><strong>Philippine practice.</strong> Belimumab, voclosporin, avacopan and rituximab are expensive and mostly paid out of pocket; PhilHealth benefits for these drugs are limited, and Malasakit Centers, charity services and pharmaceutical access programs may help. A KDIGO 1B regimen that the family can sustain, such as glucocorticoids with low-dose intravenous cyclophosphamide or MPAA, is better than a newer one abandoned after two doses. Hydroxychloroquine is cheap relative to the harm of stopping it; Angelica&rsquo;s story is common. Write the cost conversation in the chart.</p>
{{key:Before the first immunosuppressive dose, screen for tuberculosis and hepatitis B, plan contraception, and choose a regimen the family can afford to finish.}}
""")],
 'debrief': [
  """<p><strong>Rapidly progressive, and today.</strong> Yes. Angelica&rsquo;s creatinine has risen from 0.7 to 1.8 mg/dL in three months with a nephritic urine, low complement and high anti-dsDNA: active lupus nephritis, probably proliferative. Today the resident sends ANCA and anti-GBM to exclude an overlap, starts the safety screen (chest radiograph, tuberculosis history and test, hepatitis B surface antigen and core antibody, hepatitis C, HIV, pregnancy test), controls blood pressure, and calls the fellow and attending. The attending, not the intern&rsquo;s note, decides whether glucocorticoids start tonight or after the biopsy, weighing the speed of decline against her grandfather&rsquo;s recent tuberculosis.</p>""",
  """<p><strong>The biopsy and the choice.</strong> Her proteinuria is well above the 0.5 g/day threshold KDIGO 2024 suggests for investigation. The biopsy will give the ISN/RPS class and the NIH activity and chronicity indices, which tell you how much can still be saved. If it shows class III or IV, KDIGO 2024 recommends glucocorticoids plus one of MPAA, low-dose intravenous cyclophosphamide, belimumab with either, or MPAA with a calcineurin inhibitor (1B), and hydroxychloroquine restarted (1C). Choose with her: low-dose intravenous cyclophosphamide is usually the cheaper course but needs fertility counseling; MPAA needs daily adherence and contraception; add-on biologics improved renal response in trials but cost more than the family can manage.</p>""",
  """<p><strong>Before and during.</strong> Complete the tuberculosis and hepatitis B screens before the first dose, or, if the attending judges treatment cannot wait, start it with a documented plan for prophylaxis or close monitoring. Plan contraception, because MPAA and cyclophosphamide harm a pregnancy. Use the lowest glucocorticoid exposure the evidence supports. Restart hydroxychloroquine and ask the social worker about Malasakit or charity support so that she can afford it. Set a response target: a fall in proteinuria of at least 50% toward below 0.5 g/g with stable creatinine over 6 to 12 months, and a plan to continue immunosuppression for at least 36 months.</p>"""],
 'skills': {'title': 'Immune kidney disease',
  'intro': 'Complete with a preceptor on the ward, in clinic, or at a renal pathology conference. Sign-off is local.',
  'items': [('Recognizes the rapidly progressive pattern and escalates the same day with a structured handoff', False),
            ('Orders ANCA, anti-GBM, complement, ANA and anti-dsDNA in the right sequence and documents send-out dates', False),
            ('Completes and documents a pre-immunosuppression safety screen: tuberculosis, hepatitis B and C, HIV, pregnancy, vaccination', False),
            ('Reads a lupus nephritis biopsy report, stating ISN/RPS class and NIH activity and chronicity indices', False),
            ('States the KDIGO 2024 initial treatment options for class III/IV lupus nephritis and ANCA vasculitis with their grades', False),
            ('Writes a cost-aware treatment plan with the patient and family and records the conversation', False)],
  'placement': 'Nephrology ward, lupus or vasculitis clinic, renal pathology conference'},
 'quiz': [
  ('An intern sees a 62-year-old with hemoptysis, red cell casts and a creatinine of 3.1 mg/dL that was 1.2 mg/dL two weeks ago. What should the intern do first?',
   ['Report it to the resident at once as a possible pulmonary-renal syndrome', 'Request a repeat urinalysis tomorrow', 'Start oral antibiotics for pneumonia and review in the morning', 'Order a kidney ultrasound and wait for the result'],
   0,
   'Hemoptysis with a nephritic urine and a creatinine more than doubling in two weeks is a pulmonary-renal syndrome until proven otherwise; hours matter in anti-GBM and ANCA disease. An ultrasound helps later but does not answer the urgent question.'),
  ('A resident suspects RPGN. Which set of tests should be sent today?',
   ['Anti-PLA2R and lipid profile', 'Uric acid and HbA1c', 'ANCA, anti-GBM antibody, C3, C4, ANA and anti-dsDNA', 'Urine culture only'],
   2,
   'These tests sort RPGN into anti-GBM, immune-complex and pauci-immune mechanisms, each with time-critical treatment. Anti-PLA2R is for membranous nephropathy, a nephrotic disease.'),
  ('What does KDIGO 2024 recommend as initial treatment of new-onset ANCA-associated vasculitis?',
   ['Plasma exchange for all patients', 'Glucocorticoids in combination with cyclophosphamide or rituximab (1B)', 'Rituximab alone without glucocorticoids or avacopan', 'Hydroxychloroquine'],
   1,
   'Recommendation 9.3.1.1 is graded 1B. Plasma exchange is a considered option in the sickest patients after PEXIVAS showed no significant benefit on death or kidney failure; avacopan may replace glucocorticoids.'),
  ('A 21-year-old with class IV lupus nephritis asks why she must keep taking hydroxychloroquine. Which answer reflects KDIGO 2024?',
   ['It is recommended for all patients with SLE, including lupus nephritis, unless contraindicated (1C)', 'It is only for skin disease', 'It replaces immunosuppression in class IV', 'It is optional once proteinuria falls'],
   0,
   'KDIGO 2024 recommends hydroxychloroquine for everyone with SLE unless contraindicated (1C). It does not replace class III/IV immunosuppression.'),
  ('A 45-year-old from Tondo is about to start high-dose glucocorticoids and rituximab for ANCA vasculitis. His brother has active tuberculosis. What is the most important step before the first dose?',
   ['Double the glucocorticoid dose', 'Screen for latent and active tuberculosis and for hepatitis B, and plan prophylaxis or treatment with the attending', 'Skip screening because the disease is urgent', 'Give plasma exchange first'],
   1,
   'The Philippines has one of the highest tuberculosis burdens worldwide, and rituximab can reactivate hepatitis B. If treatment cannot wait, the screen still starts the same day with a documented plan. Plasma exchange does not address infection risk.')],
 'terms': [('AL', 'Amyloid light-chain (amyloidosis)'),
           ('ANA', 'Antinuclear antibody'),
           ('ANCA', 'Antineutrophil cytoplasmic antibody'),
           ('anti-dsDNA', 'Anti-double-stranded DNA antibody'),
           ('anti-GBM', 'Anti-glomerular basement membrane'),
           ('ASO', 'Antistreptolysin O'),
           ('CKD', 'Chronic kidney disease'),
           ('eGFR', 'Estimated glomerular filtration rate'),
           ('FSGS', 'Focal segmental glomerulosclerosis'),
           ('GBM', 'Glomerular basement membrane'),
           ('GFR', 'Glomerular filtration rate'),
           ('GN', 'Glomerulonephritis'),
           ('HbA1c', 'Glycated hemoglobin'),
           ('HIV', 'Human immunodeficiency virus'),
           ('HR', 'Hazard ratio'),
           ('IRR', 'Incidence rate ratio'),
           ('ISN/RPS', 'International Society of Nephrology/Renal Pathology Society'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('MGRS', 'Monoclonal gammopathy of renal significance'),
           ('MIDD', 'Monoclonal immunoglobulin deposition disease'),
           ('MPAA', 'Mycophenolic acid analog'),
           ('MPGN', 'Membranoproliferative glomerulonephritis'),
           ('MPO', 'Myeloperoxidase'),
           ('NIH', 'National Institutes of Health'),
           ('PEXIVAS', 'Plasma Exchange and Glucocorticoids in Severe ANCA-Associated Vasculitis (trial)'),
           ('PLA2R', 'M-type phospholipase A2 receptor'),
           ('PR3', 'Proteinase 3'),
           ('RAVE', 'Rituximab in ANCA-Associated Vasculitis (trial)'),
           ('RPGN', 'Rapidly progressive glomerulonephritis'),
           ('SLE', 'Systemic lupus erythematosus'),
           ('UPCR', 'Urine protein-to-creatinine ratio'),
           ('WHO', 'World Health Organization')],
 'readings': [('lupus-nephritis.html', 'Lupus Nephritis'),
              ('attending-nephrologist-11-glomerular-disease-biopsy.html', 'Attending Nephrologist, Module 11: Glomerular disease and the biopsy'),
              ('attending-pediatric-nephrologist-12-lupus-vasculitis.html', 'Attending Pediatric Nephrologist, Module 12: Lupus and vasculitis'),
              ('viral-infections-vaccinations-ckd.html', 'Viral Infections and Vaccinations in CKD')],
 'calcs': ['calc-sledai.html', 'calc-anca-renal-risk.html', 'calc-anti-gbm-renal-risk.html', 'calc-nephritic-toolkit.html', 'calc-urine-protein-excretion.html']}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
