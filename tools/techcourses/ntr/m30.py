# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 30: Transplant follow-up and allograft dysfunction.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard.
KDIGO 2009 recipient statements and grades (R5.1 1B with 2C sub-points; R6.1 1C; R7.1 1C; R13.1.1 2C/2D; R13.2.1 1B/1C;
R14.3.1 2D; R14.3.2 1C; R16.1.2 2C; R18.4 2D; R11.1 not graded) checked against the NKF summary of the guideline.
ELITE-Symphony, Borra 2010 and the 2024 BK consensus checked against PubMed abstracts. No doses. Fictional case."""

MODULE = {
    "image_alt": "A Filipino nephrology resident examines the right lower abdomen of a woman with a kidney transplant on a medicine ward, while her husband holds a plastic bag of medicine boxes and a phone showing a laboratory result.",
    "objectives": [
        "<strong>Intern:</strong> Recognize the kidney transplant recipient on your ward, list every medicine they take including generics and recent additions, and report fever, diarrhea, missed doses or a rising creatinine to the transplant team at once.",
        "<strong>Resident:</strong> Work through a rising creatinine or a fever in a recipient by time since transplant, check drug levels and interactions, and call the transplant team before changing any immunosuppressant or starting an interacting drug.",
        "<strong>Fellow:</strong> Manage immunosuppression monitoring, cytomegalovirus (CMV), BK polyomavirus and tuberculosis risk, and allograft dysfunction with the Kidney Disease: Improving Global Outcomes (KDIGO) 2009 guideline and current consensus statements, including when to biopsy.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the doctor who sees the recipient first</span>Transplant recipients rarely present to the transplant center first. They present to a provincial emergency room, a medicine ward or a dialysis unit where a resident is on call. An <strong>intern</strong> owns the complete medicine list and the first report. A <strong>resident</strong> owns the first work-up and the call to the transplant team, and must not stop, start or substitute an immunosuppressant on their own. A <strong>fellow</strong> owns the reasoning about drug levels, infection and rejection, and the decision with the transplant nephrologist about biopsy.</div>
{{plain:Think of immunosuppression as a leash on a guard dog. The dog is the immune system. Too loose, and it attacks the new kidney. Too tight, and it cannot chase away burglars: infections and cancers walk in.}}
<p>The picture has a limit. A leash has one length, set once. The right degree of immunosuppression changes with time after transplant, highest in the first months and lower later. And the length of the leash is not under the doctor&rsquo;s control alone. Tacrolimus, the backbone drug, has a narrow gap between too little and too much, and its blood level moves with diarrhea, with antibiotics and antifungals bought at a corner pharmacy, with a switch to a cheaper brand, and with every missed dose. The same prescription can be too loose one week and too tight the next.</p>
<p>That is why a rising creatinine in a recipient is never just &ldquo;acute kidney injury (AKI)&rdquo; and a fever is never just &ldquo;viral.&rdquo; Each points to one of a short list of causes whose treatments pull the leash in opposite directions. Treating rejection when the problem is drug toxicity, or reducing immunosuppression when the problem is rejection, can cost the graft.</p>
{{cards:Key numbers|Low-dose tacrolimus regimen (ELITE-Symphony, 1,645 recipients, RCT)::Biopsy-proven acute rejection at 12 months 12.3% versus 25.8% with standard-dose cyclosporine and 37.2% with low-dose sirolimus|Calcineurin inhibitor levels (KDIGO 2009, R5.1)::Measure them (1B), including whenever a medicine or the patient&rsquo;s condition changes and whenever kidney function declines (2C)|Biopsy (KDIGO 2009, R7.1)::Biopsy for declining function of unclear cause (1C)|CMV prophylaxis (KDIGO 2009, R13.2.1)::At least 3 months after transplant unless donor and recipient are both CMV-seronegative (1B)|BK screening (2024 consensus)::Plasma BK DNA monthly to month 9, then every 3 months to 2 years (3 years in children)}}
<p>Most recipients you meet are doing well and need only their usual medicines, correctly continued. A few have a graft in danger from rejection, toxicity, infection or obstruction. Your work is to keep every immunosuppressant going at the right level, to sort the cause by time since transplant and by the drug list, and to bring in the transplant team early.</p>
""",
    "case": {"title": "Fever after the switch", "html": """
<p>Monday, 9 p.m., the emergency room of a provincial hospital in Lipa, Batangas. Mrs. Liza Dimaculangan, 46, received a living-donor kidney from her sister at a Metro Manila transplant center 14 months ago. Her creatinine has been stable at 1.2 mg/dL. Her maintenance regimen is tacrolimus, mycophenolate and prednisone.</p>
<p>Five weeks ago, to save money, she changed to a cheaper tacrolimus brand from a pharmacy near her home. No trough level has been checked since. Four days ago a clinic gave her clarithromycin for a cough. For three days she has had a temperature up to 38.4 &deg;C and loose stools six times a day. Tonight her creatinine is 1.9 mg/dL and potassium 5.6 mmol/L. Her graft is not tender. Her husband, Ramon, says the transplant clinic is &ldquo;too far, three hours by bus,&rdquo; and asks if she can just be admitted here.</p>
""", "questions": ["What could explain her rising creatinine, and which causes pull treatment in opposite directions?",
                  "What do you check tonight, and whom do you call?",
                  "What will you advise about her medicines, the clarithromycin and the brand switch?"]},
    "sections": [
        ("immunosuppression", "Immunosuppression", "Immunosuppression: how the drugs work and how their levels move", """
<p>A T cell needs three signals to attack a graft. Signal 1 is recognition of donor human leukocyte antigens (HLA) through the T-cell receptor. Signal 2 is costimulation. Signal 3 is interleukin-2, which drives the cell to divide. Each drug class blocks a step in that chain.</p>
<div class="table-wrap"><table><thead><tr><th>Drug class</th><th>What it blocks</th><th>Toxicity you will see</th><th>What moves its level</th></tr></thead><tbody>
<tr><td>Calcineurin inhibitors (tacrolimus, cyclosporine)</td><td>Calcineurin, so interleukin-2 is not transcribed (signal 1 to 3)</td><td>Afferent arteriolar vasoconstriction and a rising creatinine; tremor; hyperkalemia; hypomagnesemia; new diabetes; chronic graft scarring</td><td>Cytochrome P450 3A4 and P-glycoprotein inhibitors and inducers, diarrhea, brand switches, missed doses</td></tr>
<tr><td>Antiproliferatives (mycophenolate, azathioprine)</td><td>Purine synthesis in dividing lymphocytes</td><td>Leukopenia, diarrhea, anemia; mycophenolate harms a fetus</td><td>Adherence, interactions with some binders</td></tr>
<tr><td>Corticosteroids</td><td>Cytokine gene transcription broadly</td><td>Diabetes, bone loss, infection, weight gain</td><td>Usually fixed</td></tr>
<tr><td>Mammalian target of rapamycin (mTOR) inhibitors (sirolimus, everolimus)</td><td>Signal 3 downstream</td><td>Poor wound healing, proteinuria, mouth ulcers, high lipids</td><td>Same enzymes as tacrolimus</td></tr>
<tr><td>Induction antibodies (T-cell depleting or interleukin-2 receptor blocking)</td><td>T cells around the time of surgery</td><td>Later infection risk, especially CMV after T-cell depletion</td><td>Given once, early</td></tr>
</tbody></table></div>
<p><strong>The evidence for the modern backbone.</strong> The ELITE-Symphony trial randomized 1,645 recipients to standard-dose cyclosporine, or induction with low-dose cyclosporine, low-dose tacrolimus or low-dose sirolimus, all with mycophenolate and steroids. At 12 months the low-dose tacrolimus group had the highest calculated GFR (65.4 mL per minute versus 56.7 to 59.4), the lowest rate of biopsy-proven acute rejection (12.3%, against 25.8% with standard cyclosporine, 24.0% with low-dose cyclosporine and 37.2% with sirolimus) and the highest graft survival (94.2% against 89.3% to 93.1%).[[ntr30_2]] The primary end point, calculated GFR, is a surrogate; rejection and graft loss are outcomes patients feel. The trial ran for one year and does not settle long-term choices.</p>
<p><strong>Why levels matter.</strong> Tacrolimus has a narrow therapeutic range and highly variable absorption and metabolism. KDIGO 2009 recommends measuring calcineurin inhibitor blood levels (1B), suggesting checks every other day early after transplant until the target is reached, whenever there is a change in medication or patient status that may affect levels, and whenever kidney function declines in a way that may mean toxicity or rejection (each 2C).[[ntr30_1]] Variability matters too. In a retrospective cohort of 297 recipients, high within-patient variability in tacrolimus clearance between 6 and 12 months was associated with graft loss, chronic allograft nephropathy or doubling of creatinine, even though mean levels were similar in those who failed and those who did not.[[ntr30_3]] The study was observational; variability may mark nonadherence as much as pharmacology.</p>
<p><strong>The interaction card.</strong> Most dangerous interactions run through the same liver and gut enzyme.</p>
<div class="table-wrap"><table><thead><tr><th>Raises tacrolimus (risk: toxicity, rising creatinine, hyperkalemia)</th><th>Lowers tacrolimus (risk: rejection)</th></tr></thead><tbody>
<tr><td>Clarithromycin and erythromycin; azole antifungals; diltiazem and verapamil; grapefruit; diarrhea (less gut metabolism)</td><td>Rifampin and other rifamycins; phenytoin and carbamazepine; St John&rsquo;s wort; missed doses; vomiting</td></tr>
</tbody></table></div>
<p>KDIGO 2009 recommends monitoring calcineurin inhibitor and mTOR inhibitor levels in patients receiving rifampin (1C), because the fall in levels can be steep.[[ntr30_1]] For herbal products, assume an interaction until proven otherwise.</p>
<p><strong>Generic switches.</strong> In the Philippines, recipients often change tacrolimus brands for cost or because a pharmacy runs out. Bioequivalence standards allow some difference in exposure between products, and a patient whose level sat at the target on one brand may land above or below it on another. A switch is exactly the &ldquo;change in medication&rdquo; that KDIGO says should trigger a level.[[ntr30_1]] Teach recipients to tell the transplant clinic before any change and to keep one brand when they can; when they cannot, arrange a trough level soon after the change.</p>
{{fig:ntr30_b}}
{{key:Every new medicine, every brand change and every bout of diarrhea in a recipient is a reason to ask what just happened to the tacrolimus level.}}
"""),
        ("dysfunction", "Rising creatinine", "A rising creatinine: sort the cause by time since transplant", """
<p>A creatinine rise in a recipient has the causes of AKI in anyone, plus four special ones: rejection, calcineurin inhibitor toxicity, BK polyomavirus nephropathy and recurrent disease. The time since transplant tells you which are likely.</p>
<div class="table-wrap"><table><thead><tr><th>Time since transplant</th><th>Most likely causes</th><th>Clues</th></tr></thead><tbody>
<tr><td>First week</td><td>Delayed graft function from ischemic injury; renal artery or vein thrombosis; urine leak; obstruction; hyperacute or early antibody-mediated rejection</td><td>Sudden anuria, graft pain, falling urine output after a good start, fluid around the graft on ultrasound</td></tr>
<tr><td>1 to 6 months</td><td>Acute T-cell-mediated or antibody-mediated rejection; calcineurin inhibitor toxicity; BK nephropathy; obstruction or lymphocele; pyelonephritis; volume depletion; CMV</td><td>Drug level, BK deoxyribonucleic acid (DNA) in plasma, urine culture, Doppler ultrasound</td></tr>
<tr><td>After 6 months</td><td>Antibody-mediated rejection from donor-specific antibodies, often after missed doses or under-immunosuppression; drug toxicity; recurrent glomerular disease; transplant renal artery stenosis; chronic injury</td><td>Adherence history, proteinuria, donor-specific antibody testing, new hypertension</td></tr>
</tbody></table></div>
<p><strong>The work-up in order.</strong> First, confirm the rise with a repeat value and look at the trend; the site&rsquo;s allograft eGFR trend calculator helps you see slope rather than noise. Second, look for the easy, reversible causes: dehydration from diarrhea, a new drug, urinary retention or infection. Third, check the trough level. Fourth, get a graft ultrasound with Doppler to exclude obstruction, collections and vascular problems. Fifth, check urine protein, plasma BK DNA and, through the transplant team, donor-specific antibodies.</p>
<p><strong>When to biopsy.</strong> KDIGO 2009 recommends a kidney allograft biopsy for all patients with declining kidney function of unclear cause, to detect potentially reversible causes (1C), and a biopsy before treating acute rejection unless the biopsy would substantially delay treatment (1C).[[ntr30_1]] The reason is mechanistic: rejection, toxicity and BK nephropathy can all look the same in the blood, but they need opposite moves on the leash. Treating presumed rejection with more immunosuppression in a patient with BK nephropathy feeds the virus.</p>
<p><strong>Philippine practice.</strong> Graft biopsy, C4d staining, BK testing and donor-specific antibody testing are available at transplant centers but not in most provincial hospitals. That makes the phone call to the transplant team, and often transfer, part of the work-up. A trough level can usually be sent out; ask the laboratory for its turnaround before you rely on it tonight.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>Adolescents carry the highest risk of late rejection from missed doses, and the move from pediatric to adult care is a dangerous moment for the graft. Growth, school and puberty change drug handling and adherence. BK screening runs to 3 years after transplant in children, and the 2024 consensus allows biopsy for persistent BK DNA even without graft dysfunction. See <a href="attending-pediatric-nephrologist-27-transplant-follow-up.html">Attending Pediatric Nephrologist, Module 27</a>.</div>
{{fig:ntr30_a}}
{{call:Stop and call the transplant team or the attending nephrologist, per unit protocol, but always ask the attending nephrologist for guidance, when:<ul><li>Any unexplained rise in creatinine, or falling urine output, in a recipient</li><li>Graft pain or tenderness, or fever with a tender graft</li><li>Vomiting or diarrhea that stops the patient from taking or absorbing immunosuppressants</li><li>A new medicine that interacts with tacrolimus has been started or is being considered</li><li>Missed immunosuppressant doses, or a brand switch without a level</li><li>Potassium high enough to need urgent treatment</li></ul>}}
{{key:Treat a recipient&rsquo;s creatinine rise as rejection, toxicity, infection or obstruction until proven otherwise, and do not adjust immunosuppression before the transplant team and, usually, a biopsy have spoken.}}
"""),
        ("infection", "Infection", "Infection: CMV, BK and tuberculosis in a Philippine recipient", """
<p>Infection after transplant follows a timetable set by the intensity of immunosuppression. In the first month, surgical-site, line and urinary infections dominate, as after any operation. From about one to six months, when immunosuppression is most intense, opportunistic infections appear: CMV, BK, <em>Pneumocystis</em>, and reactivation of latent tuberculosis. After six months, most infections are community-acquired, but a recipient who has been treated for rejection is back in the high-risk window.</p>
<p><strong>CMV.</strong> The highest risk is a seronegative recipient of a seropositive donor&rsquo;s kidney, who meets the virus for the first time while immunosuppressed.[[ntr30_4]] CMV causes fever, leukopenia, diarrhea and hepatitis, and it is also associated with rejection and graft loss. KDIGO 2009 recommends that recipients receive antiviral chemoprophylaxis for at least 3 months after transplantation (1B) and for 6 weeks after treatment with a T-cell-depleting antibody (1C), except when donor and recipient are both CMV-seronegative.[[ntr30_1]] The third international consensus (2018) describes prophylaxis and pre-emptive monitoring strategies by risk group.[[ntr30_4]] Drug choice and duration come from the transplant center.</p>
<p><strong>BK polyomavirus.</strong> Most adults carry BK virus silently in the urinary tract. Under immunosuppression it replicates in tubular cells, spills into the blood (BK DNAemia) and can scar the graft (BK nephropathy), with a rising creatinine that mimics rejection. The 2024 international consensus lists risk factors including older recipient age, male sex, tacrolimus, acute rejection and higher steroid exposure. It recommends screening all recipients for plasma BK DNA monthly until month 9 and then every 3 months until 2 years (3 years in children); in resource-limited settings, urine cytology at the same time points can exclude nephropathy, with plasma testing when decoy cells appear. For BK DNA persisting above 1,000 copies/mL, exceeding 10,000 copies/mL, or biopsy-proven nephropathy, it advises stepwise reduction of immunosuppression; it found no support for leflunomide, cidofovir, quinolones or intravenous immunoglobulin.[[ntr30_5]]</p>
<p>The older KDIGO 2009 guideline suggested screening by nucleic acid testing (2C), monthly for the first 3 to 6 months and then every 3 months to the end of the first year (2D).[[ntr30_1]] The two documents disagree on the schedule because the consensus is 15 years newer, used later evidence and the Grading of Recommendations Assessment, Development and Evaluation (GRADE) method, and found screening cost-effective. Follow your transplant center&rsquo;s protocol; most now follow the newer schedule where testing is affordable.</p>
<p><strong>Tuberculosis.</strong> The Philippines carried about 6.8% of the world&rsquo;s tuberculosis cases in 2024 on World Health Organization estimates.[[ntr30_6]] A recipient with latent infection may reactivate under immunosuppression, often with atypical or extrapulmonary disease. KDIGO 2009 suggests that prophylaxis and treatment regimens be the same as those used in the local general population (2D), and recommends monitoring calcineurin and mTOR inhibitor levels in patients receiving rifampin (1C).[[ntr30_1]] Rifampin is a powerful enzyme inducer: started without warning, it can drop tacrolimus levels enough to cause rejection within weeks. The infectious diseases team chooses the regimen; you make sure the transplant team knows before the first dose.</p>
<div class="table-wrap"><table><thead><tr><th>Fever in a recipient: question</th><th>Why you ask it</th></tr></thead><tbody>
<tr><td>How long since transplant, and any recent rejection treatment?</td><td>Sets the infection timetable</td></tr>
<tr><td>CMV status of donor and recipient; prophylaxis stopped when?</td><td>CMV often appears soon after prophylaxis ends</td></tr>
<tr><td>Graft tender? Urine findings?</td><td>Graft pyelonephritis or rejection</td></tr>
<tr><td>Cough, night sweats, weight loss, contact history?</td><td>Tuberculosis</td></tr>
<tr><td>Floodwater, mosquito exposure, local outbreaks?</td><td>Leptospirosis and dengue happen to recipients too, and can hit a single kidney hard</td></tr>
<tr><td>New antibiotics or antifungals already given?</td><td>Interaction with tacrolimus</td></tr>
</tbody></table></div>
<p>Live vaccines, such as varicella, measles-mumps-rubella, yellow fever and oral typhoid, are avoided after transplant; inactivated vaccines are given.[[ntr30_1]] Vaccination is best brought up to date before transplant, while the immune system can still respond.</p>
{{key:In a febrile recipient, think timetable, think CMV, BK and tuberculosis, and think about what any antimicrobial will do to the tacrolimus level before it is given.}}
"""),
        ("long-term", "Long-term care", "Long-term care: keeping the graft, and the patient, alive", """
<p>The survival benefit of transplantation lasts only while the graft works. In the long-term data from the United States, recipients had an annual death rate of 3.8 per 100 patient-years against 6.3 among those still waiting.[[ntr30_8]] When a graft fails, the patient returns to dialysis with a sensitized immune system and often a harder path to a second transplant. Long-term care protects that gain.</p>
<div class="table-wrap"><table><thead><tr><th>Long-term threat</th><th>Mechanism</th><th>What KDIGO 2009 suggests or recommends</th></tr></thead><tbody>
<tr><td>Nonadherence</td><td>Missed doses allow donor-specific antibodies and late rejection</td><td>Nonadherence is associated with a high risk of acute rejection and graft loss (not graded); consider education and support for recipients and families</td></tr>
<tr><td>Cardiovascular disease</td><td>Chronic kidney disease (CKD), diabetes, calcineurin inhibitors and steroids raise risk</td><td>Blood pressure goal below 130/80 mm Hg in adults (2C); manage lipids and glucose</td></tr>
<tr><td>Skin and other cancers</td><td>Immune surveillance is reduced</td><td>Annual skin and lip examination by a qualified health professional (2D); age-appropriate cancer screening</td></tr>
<tr><td>New diabetes after transplant</td><td>Tacrolimus and steroids impair insulin secretion and action</td><td>Screen glucose regularly</td></tr>
<tr><td>Pregnancy</td><td>Mycophenolate harms the fetus; graft and pregnancy affect each other</td><td>Plan pregnancy with the transplant team; review drugs before conception</td></tr>
</tbody></table></div>
<p>The rows above are from the 2009 guideline.[[ntr30_1]] It is now old, written before several newer drugs and before current BK and CMV evidence. Where a newer consensus or a later KDIGO guideline covers a topic, the transplant center will follow the newer document; tell the learner, and the patient, which one you are quoting.</p>
<p><strong>Philippine practice.</strong> Immunosuppressants are a lifelong cost, largely out of pocket. PhilHealth has a post-kidney transplant services benefit; the transplant center&rsquo;s PhilHealth office confirms what it covers.[[ntr30_7]] The kidney transplantation Z benefit (PhilHealth Circular 2026-0019, Revision 1) covers immunosuppressants only in the induction phase, until 1 week after discharge, and states that patients remain eligible for hemodialysis or peritoneal dialysis benefits if the graft fails from rejection, infection, acute kidney injury or other complications; confirm the effective date and current rules with the PhilHealth liaison on the date of service.[[ntr30_9]] Supply gaps happen: a pharmacy runs out of a brand, a typhoon closes the road to the city. Teach recipients to keep a buffer of at least two weeks of every immunosuppressant, to carry a written medicine list with brand names, and to call the transplant clinic before running out, not after. Recipients in the provinces should know which nearby hospital can draw a trough level and where to send it.</p>
<p><strong>What each of you does on a ward.</strong> The intern writes down every medicine by name and brand, including what was bought last week, and confirms the next dose time; immunosuppressants are not &ldquo;held&rdquo; because the patient is on nothing by mouth (NPO) without an explicit decision. The resident calls the transplant team on admission, not on discharge. The fellow reviews the trough, the interaction list and the infection timetable, and agrees with the transplant nephrologist on whether biopsy or transfer is needed.</p>
{{key:Keep every immunosuppressant going, at the right level, on the right brand, through every admission, and call the transplant team on day one.}}
"""),
    ],
    "debrief": [
        "<p><strong>The causes.</strong> Several are likely at once. Clarithromycin and diarrhea both raise tacrolimus levels, so calcineurin inhibitor toxicity, with hyperkalemia, is likely; diarrhea also causes volume depletion. The brand switch five weeks ago without a level could have pushed her level either way: too low invites acute rejection, too high adds toxicity. Fever and diarrhea at 14 months could be CMV, another infection or a drug effect, and BK nephropathy remains possible. Toxicity and volume depletion call for less drug and more fluid; rejection calls for more immunosuppression; BK nephropathy calls for less. That is why nobody guesses.</p>",
        "<p><strong>Tonight.</strong> Assess volume and treat potassium per protocol. Send a tacrolimus trough (timed before the next dose), a complete blood count, electrolytes and magnesium, urinalysis and urine culture, blood cultures, and stool studies. Arrange a graft ultrasound with Doppler. Ask the transplant center about CMV and BK testing and whether samples can be sent from Lipa. Call the transplant team tonight with the drug list, the switch, the clarithromycin and the numbers; agree whether she stays here or transfers. Biopsy, if needed, will be at the transplant center (KDIGO 2009 R7.1, 1C).</p>",
        "<p><strong>The medicines.</strong> Do not stop her immunosuppressants on your own. Raise the clarithromycin with the transplant team: it should usually be replaced by an antibiotic that does not raise tacrolimus, if one is still needed. Any change in her tacrolimus dose waits for the level and the team&rsquo;s decision. Explain to Mrs. Dimaculangan and Ramon that brand changes are allowed only with a level check soon after, ideally on one consistent brand, and that every new medicine, including from local clinics, must be cleared with the transplant team first. Refer them to the center&rsquo;s PhilHealth office about the post-transplant benefit, since cost drove the switch.</p>",
    ],
    "skills": {"title": "Transplant follow-up and allograft dysfunction",
               "intro": "Complete with a preceptor, in simulation or at your own unit. Sign-off is local.",
               "items": [("Takes a complete transplant medicine history, including brand, recent switches and all new drugs", False),
                         ("Lists the causes of a rising creatinine by time since transplant and orders the first-line work-up", False),
                         ("Identifies drugs that raise or lower tacrolimus levels on a real medicine list", False),
                         ("Applies the CMV and BK screening and prophylaxis statements with their sources and grades", False),
                         ("Presents a recipient to the transplant team by phone with drug level, interactions and timeline", False)],
               "placement": "Medicine ward, transplant clinic or simulation"},
    "quiz": [
        ("A transplant recipient is admitted to your ward for pneumonia. Which item is most important for the intern to record and report at once?",
         ["The date of the next routine transplant clinic visit",
          "Every medicine with brand names, including any recent switches and antibiotics already given",
          "The donor&rsquo;s blood group",
          "Whether the patient prefers oral or intravenous fluids"],
         1,
         "A complete medicine list, including brand switches and new antimicrobials, is what lets the team foresee tacrolimus toxicity or rejection. Clinic dates and donor details can wait."),
        ("A recipient 3 months after transplant has a creatinine rise from 1.1 to 1.6 mg/dL. The resident is unsure whether it is rejection or toxicity. What does KDIGO 2009 recommend?",
         ["Increase tacrolimus empirically and recheck in a week",
          "Stop tacrolimus until creatinine returns to baseline",
          "A kidney allograft biopsy for declining function of unclear cause, arranged with the transplant team",
          "Start antibiotics for presumed graft pyelonephritis"],
         2,
         "KDIGO 2009 R7.1 recommends biopsy for declining function of unclear cause (1C), because rejection, toxicity and BK nephropathy need opposite treatments. Empiric changes in tacrolimus in either direction can harm the graft."),
        ("Which BK polyomavirus screening schedule does the 2024 international consensus recommend for adult kidney recipients?",
         ["Urine culture monthly for 6 months",
          "Plasma BK DNA monthly until month 9, then every 3 months until 2 years",
          "Plasma BK DNA only when creatinine rises",
          "Annual kidney biopsy for 5 years"],
         1,
         "The 2024 consensus recommends monthly plasma BK DNA to month 9, then every 3 months to 2 years (3 years in children). The older KDIGO 2009 schedule ended at 1 year; screening only on a creatinine rise misses the window for early intervention."),
        ("A recipient 8 months after transplant is started on rifampin-based treatment for tuberculosis at a health center. Two weeks later her creatinine rises. What is the most likely mechanism?",
         ["Rifampin is directly nephrotoxic in all patients",
          "Rifampin induced tacrolimus metabolism, lowering levels and allowing rejection",
          "Tuberculosis has spread to the graft in every case",
          "Rifampin raised the tacrolimus level"],
         1,
         "Rifampin is a strong enzyme inducer that lowers calcineurin inhibitor levels; KDIGO 2009 recommends monitoring levels with rifampin (1C). The fall in levels can allow acute rejection within weeks."),
        ("A recipient with stable function switched to a cheaper tacrolimus brand last month. What is the best advice?",
         ["No action is needed because generics are identical",
          "Check a trough level soon after the switch and tell the transplant clinic before any future brand change",
          "Double the dose to be safe",
          "Switch back to the original brand without informing the clinic"],
         1,
         "A brand change is a change in medication that may alter levels, which KDIGO 2009 says should trigger level monitoring (2C). Doubling the dose or switching silently risks toxicity or rejection."),
    ],
    "terms": [("AKI", "Acute kidney injury"), ("BK", "BK polyomavirus"), ("CKD", "Chronic kidney disease"),
              ("CMV", "Cytomegalovirus"), ("DNA", "Deoxyribonucleic acid"), ("eGFR", "Estimated glomerular filtration rate"),
              ("GFR", "Glomerular filtration rate"), ("GRADE", "Grading of Recommendations Assessment, Development and Evaluation"),
              ("HLA", "Human leukocyte antigen"), ("KDIGO", "Kidney Disease: Improving Global Outcomes"),
              ("mTOR", "Mammalian target of rapamycin"), ("NPO", "Nothing by mouth (nil per os)"), ("PD", "Peritoneal dialysis"),
              ("RCT", "Randomized controlled trial")],
    "readings": [("transplant-nurse-07-graft-dysfunction.html", "Transplant Nurse, Module 7: Graft dysfunction"),
                 ("transplant-nurse-08-infection.html", "Transplant Nurse, Module 8: Infection"),
                 ("transplant-allograft-failure.html", "Transplant Allograft Failure"),
                 ("physician-on-duty-27-transplant-pd-conservative-care.html", "Physician on Duty, Module 27: Transplant, PD and conservative care")],
    "calcs": ["calc-tacrolimus-level-check.html", "calc-tacrolimus-dosing.html", "calc-allograft-egfr-trend.html", "calc-transplant-prom.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
