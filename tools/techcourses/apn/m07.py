# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 07: Urinary tract infection, reflux and bladder-bowel dysfunction.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, for Philippine
practice. RIVUR, PREDICT, the RIVUR/CUTIE cohort, SCOUT and the oral-versus-intravenous trial checked against PubMed abstracts;
AAP 2011 diagnostic and imaging statements against the guideline abstract; reflux grading against the International Reflux Study
paper. No doses: the unit's pediatric formulary sets every antibiotic order."""

MODULE = {
    "image_alt": "A Filipino mother holds her infant son on a provincial hospital pediatric ward while a pediatric nephrologist explains a drawing of the bladder and kidneys.",
    "objectives": [
        "Diagnose febrile urinary tract infection (UTI) in an infant from a properly collected specimen, and choose imaging the way the American Academy of Pediatrics (AAP) guideline describes.",
        "Weigh antibiotic prophylaxis for vesicoureteral reflux (VUR) with a family, using the absolute numbers from RIVUR and PREDICT and what those trials do not show.",
        "Recognize and treat bladder and bowel dysfunction (BBD) as a driver of recurrent UTI in the toilet-trained child.",
    ],
    "big": """<div class="tc-keyp"><span class="tc-lab">Your role &middot; the kidney behind the fever</span>The pediatrician on the ward treats the infection. You are asked about the kidneys: was it really a UTI, does this child need imaging, prophylaxis or a urologist, and who checks the kidneys next year. Your answer often arrives by Viber to a provincial hospital, and it shapes years of antibiotics, radiation and worry for a family.</div>
{{plain:Think of the urinary tract as a one-way street with a strong current. Urine flows down from the kidneys and out of the bladder several times a day, and the flow sweeps bacteria out before they can settle. Infection needs a stalled current or a road that runs the wrong way.}}
<p>The picture has a limit. The current is only one defense. The bladder lining sheds bacteria, urine itself is hostile to many organisms, and the ureter enters the bladder through a tunnel in the wall that closes like a flap valve when the bladder squeezes. Reflux is a short tunnel that leaks. Stasis is a bladder that never empties or a rectum full of stool pressing on it. Fever means the bacteria have reached the kidney, and the kidney&rsquo;s own inflammatory response, not the bacteria alone, can leave a scar.</p>
{{cards:Key numbers|AAP 2011 diagnosis::Pyuria and at least 50,000 colonies per mL of a single uropathogen in an appropriately collected specimen|RIVUR, recurrent UTI over 2 years::39 of 302 on prophylaxis vs 72 of 305 on placebo|RIVUR, renal scarring::11.9% vs 10.2% (no significant difference)|RIVUR, resistant <em>E. coli</em> at first recurrence::63% vs 19% resistant to trimethoprim-sulfamethoxazole|PREDICT, first UTI in infants with grade III&ndash;V reflux::21.2% vs 35.6%; number needed to treat 7 over 2 years|Bladder and bowel dysfunction plus any reflux::56% had a recurrent febrile or symptomatic UTI over 2 years}}
<p>Most febrile UTIs in infants are single events in kidneys that heal. A few mark a child with high-grade reflux, an obstructed or dysplastic kidney, or a bladder that does not empty, whose kidneys will scar with each new infection. Your work is to confirm the diagnosis honestly, image the children who need it, choose prophylaxis or surgery with the family from real numbers, and treat the bladder and bowel that the urine culture never shows.</p>
""",
    "case": {"title": "The second fever",
             "html": """<p>It is 9 p.m. on a Tuesday. Gabriel Dizon, 7 months old and 7.8 kg, is on the pediatric ward of a provincial hospital in Tarlac City with a temperature of 39.4&deg;C, poor feeding and irritability. A catheter urine sample shows many white cells and is nitrite positive. Blood and urine cultures are pending, and the resident has started intravenous antibiotics from the ward&rsquo;s formulary. Creatinine is 0.3 mg/dL.</p>
<p>At 4 months he had a fever, a bag urine culture grew <em>E. coli</em>, and he was treated with oral antibiotics at home. A renal and bladder ultrasound afterward showed a dilated left collecting system. A voiding cystourethrogram (VCUG) at 5 months showed grade IV reflux on the left. No one started prophylaxis, and no one booked a follow-up.</p>
<p>The resident sends you a photo of the VCUG report on Viber with the note: &ldquo;For reimplantation? Parents want surgery now.&rdquo; Gabriel&rsquo;s father, a seafarer, calls in from abroad on video. His sister-in-law is a nurse who has read that surgery cures reflux. &ldquo;Doc, we do not want him on antibiotics for years. Just fix it.&rdquo;</p>""",
             "questions": ["Was the first episode really a UTI, and what makes this one certain?",
                           "Prophylaxis, surgery or watchful waiting: what do you offer for an infant with grade IV reflux and two febrile UTIs?",
                           "What do you tell the family about scarring, and what will actually protect his kidneys?"]},
    "sections": [
        ("physiology", "Physiology", "How the defenses fail",
         """<p>Most UTIs start in the bowel. Fecal <em>E. coli</em> colonize the perineum and climb the urethra. In the bladder, bacteria with adhesive fimbriae attach to the lining. Frequent, complete voiding washes most of them out before they multiply.</p>
<p>The ureter runs obliquely through the bladder wall before it opens. As the bladder fills and contracts, the wall compresses that tunnel and seals it. A tunnel that is too short, or a ureteric opening placed too far laterally, lets urine run back up the ureter during voiding. That is primary vesicoureteral reflux (VUR). The tunnel often lengthens as the child grows, which is why low grades of reflux tend to resolve.</p>
<p>Reflux alone does not injure the kidney. Infected reflux does. Bacteria carried into the renal pelvis reach the papillae, and compound papillae at the poles of the kidney let urine into the collecting ducts more easily. Neutrophils and cytokines that clear the infection also damage tubules and interstitium. Where inflammation is intense, fibrosis follows, and the scar is visible later on a dimercaptosuccinic acid (DMSA) scan as a cold area.</p>
<p>Not every scar comes from infection. Some boys with high-grade reflux are born with small, dysplastic kidneys, and the defect was present before any UTI. That distinction matters when a family asks whether the antibiotics they missed caused the damage.</p>
<div class="table-wrap"><table>
<thead><tr><th>Defense</th><th>What weakens it</th><th>What you may see</th></tr></thead>
<tbody>
<tr><td>Washout by voiding</td><td>Infrequent voiding, holding, incomplete emptying, a neurogenic bladder</td><td>Large post-void residual, daytime wetting, holding maneuvers</td></tr>
<tr><td>Flap-valve ureter</td><td>Short submucosal tunnel (primary reflux); high bladder pressure (secondary reflux, as with valves)</td><td>Dilated ureter and pelvis on ultrasound; reflux on VCUG</td></tr>
<tr><td>Free outflow</td><td>Posterior urethral valves, ureteropelvic or ureterovesical junction obstruction</td><td>Hydronephrosis, thick-walled bladder, poor stream in a boy</td></tr>
<tr><td>A rectum that empties</td><td>Constipation, which compresses the bladder and holds a fecal reservoir near the urethra</td><td>Hard stools, soiling, a palpable fecal mass, recurrent cystitis in a girl</td></tr>
<tr><td>A kidney that limits inflammation</td><td>Young age, delay in treatment, high-grade reflux, prior scars</td><td>New DMSA defects after febrile UTI</td></tr>
</tbody></table></div>
<p>Bladder and bowel dysfunction (BBD) is the name for the last two rows together in a toilet-trained child. The child postpones voiding, squats on a heel or crosses the legs to hold, empties partly, and is often constipated. The bladder works against a closed sphincter at high pressure, and residual urine incubates bacteria. In this setting reflux can be secondary, and it may improve when the voiding pattern improves.</p>
{{key:Ask which defense failed. A short tunnel, an obstructed outlet and a bladder that never empties each call for different treatment.}}
{{fig:apn07_a}}
"""),
        ("diagnosis", "Diagnosis", "Getting the diagnosis and the imaging right",
         """<p>A UTI diagnosis commits an infant to imaging, possible prophylaxis and years of follow-up. It has to be real. The AAP 2011 guideline for febrile infants and children aged 2 to 24 months requires both pyuria and at least 50,000 colonies per mL of a single uropathogen in an appropriately collected specimen.[[apn07_1]] The AAP reaffirmed the guideline in 2016.[[apn07_2]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Specimen</th><th>When it is used</th><th>How far to trust a positive culture</th></tr></thead>
<tbody>
<tr><td>Urethral catheter</td><td>Standard for the febrile infant who is not toilet trained</td><td>High, when collected cleanly</td></tr>
<tr><td>Suprapubic aspiration (SPA)</td><td>Infant with a full bladder, often ultrasound guided</td><td>Highest; any growth is significant</td></tr>
<tr><td>Clean-catch midstream</td><td>Toilet-trained child</td><td>Reasonable, if collected with cleaning and supervision</td></tr>
<tr><td>Bag</td><td>Convenient, so it is common on busy wards</td><td>Low. Skin and stool contaminate it. A negative bag urinalysis helps; a positive bag culture does not establish UTI</td></tr>
</tbody></table></div>
<p>Gabriel&rsquo;s first episode was diagnosed from a bag culture. It may well have been a UTI, given the later reflux, but no one can say. The second episode, from a catheter specimen with pyuria and a positive nitrite in a febrile infant, is the one to count, once the culture confirms a single uropathogen.</p>
<div class="tc-scene"><span class="tc-lab">On a Viber thread from a district hospital &middot; fictional</span><p>A resident messages you about a 10-month-old girl with fever and a bag urine culture growing three organisms. She asks whether to book a VCUG.</p><p>You ask for a catheter specimen before the next dose of antibiotic, if the child is not yet treated, and you point out that three organisms in a bag specimen are almost always skin and stool.</p><p class="tc-scene-take"><b>What this shows.</b> A contaminated specimen can start a cascade of radiation and prophylaxis for a child who never had a UTI.</p></div>
<p><strong>Imaging.</strong> The AAP advises renal and bladder ultrasound after a first febrile UTI to look for anatomic abnormalities. It does not advise a routine VCUG after a first febrile UTI. A VCUG is indicated when the ultrasound shows hydronephrosis, scarring or other findings that suggest high-grade reflux or obstruction, in other atypical or complex circumstances, and after a recurrent febrile UTI.[[apn07_1]] Gabriel met two of those criteria: a dilated collecting system and a recurrence.</p>
<p><strong>Grading.</strong> The International Reflux Study grades reflux on the VCUG from I to V by how far contrast fills and dilates the ureter, pelvis and calyces, and it set a standardized voiding cystography technique so that grades are comparable between centers.[[apn07_6]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Grade</th><th>What the VCUG shows</th><th>What it usually means</th></tr></thead>
<tbody>
<tr><td>I</td><td>Contrast into the ureter only</td><td>Low risk; often resolves</td></tr>
<tr><td>II</td><td>Ureter, pelvis and calyces filled, no dilatation</td><td>Low risk; often resolves</td></tr>
<tr><td>III</td><td>Mild to moderate dilatation, minimal blunting of calyces</td><td>Intermediate</td></tr>
<tr><td>IV</td><td>Moderate dilatation and tortuosity of the ureter, blunted calyces</td><td>High grade; scarring and dysplasia more likely</td></tr>
<tr><td>V</td><td>Gross dilatation and tortuosity, loss of papillary impressions</td><td>High grade; often congenital renal damage</td></tr>
</tbody></table></div>
<p><strong>Route and length of treatment.</strong> A multicenter randomized trial in 306 febrile children aged 1 to 24 months compared oral cefixime with initial intravenous cefotaxime followed by oral therapy. Urine was sterile within 24 hours in all children, time to defervescence was similar, and renal scarring at 6 months was 9.8% with oral therapy and 7.2% with initial intravenous therapy, a difference the authors did not find significant.[[apn07_5]] That trial predates current resistance patterns, so oral treatment works only when the organism is susceptible to the oral drug. On length, the AAP describes 7 to 14 days of treatment.[[apn07_1]] The SCOUT noninferiority trial randomized 664 children aged 2 months to 10 years who had improved after 5 days of antibiotics to 5 more days or placebo. Treatment failure was 0.6% with the standard course and 4.2% with the short course, an absolute difference of 3.6%. Most participants were girls (96%), so the result says little about febrile infant boys like Gabriel.[[apn07_8]] The drug, the route and the dose come from your unit&rsquo;s pediatric formulary and the culture result.</p>
{{key:Count only properly collected specimens. One honest UTI is worth more than three bag cultures.}}
"""),
        ("evidence", "Evidence", "Prophylaxis: what RIVUR and PREDICT show",
         """<p>Continuous low-dose antibiotic prophylaxis keeps the bladder urine sterile while the reflux has a chance to resolve. The question is whether that protects kidneys, and at what cost.</p>
<p><strong>RIVUR.</strong> The Randomized Intervention for Children with Vesicoureteral Reflux trial enrolled 607 children aged 2 to 71 months with grade I to IV reflux diagnosed after a first or second febrile or symptomatic UTI, and randomized them to trimethoprim-sulfamethoxazole (TMP-SMX) or placebo for 2 years. Recurrent UTI occurred in 39 of 302 children on prophylaxis and 72 of 305 on placebo (relative risk 0.55; hazard ratio 0.50). The benefit was larger when the index infection was febrile (hazard ratio 0.41) and in children with baseline BBD (hazard ratio 0.21). Renal scarring did not differ: 11.9% with prophylaxis and 10.2% with placebo. Among 87 children whose first recurrence grew <em>E. coli</em>, 63% of isolates were TMP-SMX resistant on prophylaxis and 19% on placebo.[[apn07_3]]</p>
<p>In absolute terms, about 13 of every 100 children on prophylaxis and about 24 of every 100 on placebo had a recurrence over 2 years. Roughly nine children were treated for 2 years to prevent one recurrence, and the scar rate did not move. RIVUR excluded grade V reflux and enrolled few infants with grade IV, so it cannot answer Gabriel&rsquo;s question directly.</p>
<p><strong>PREDICT.</strong> This open-label trial in 39 European centers randomized 292 infants aged 1 to 5 months with grade III, IV or V reflux and no previous UTI to prophylaxis or no treatment for 24 months; 80.5% had grade IV or V. A first UTI occurred in 21.2% with prophylaxis and 35.6% without (hazard ratio 0.55), and the number needed to treat for 2 years to prevent one UTI was 7. Among untreated infants, 64.4% had no UTI at all. New kidney scars and estimated glomerular filtration rate at 24 months did not differ substantially, and <em>Pseudomonas</em>, other non-<em>E. coli</em> organisms and resistance were more common in the prophylaxis group.[[apn07_4]] PREDICT enrolled infants before any UTI, mostly boys, so Gabriel, with two febrile UTIs already, sits at higher risk than its average participant.</p>
<div class="table-wrap"><table>
<thead><tr><th>Trial</th><th>Who</th><th>What prophylaxis did</th><th>What the trial does not show</th></tr></thead>
<tbody>
<tr><td>RIVUR, 2014</td><td>607 children, 2&ndash;71 months, grade I&ndash;IV, after 1&ndash;2 UTIs</td><td>Halved recurrences (39/302 vs 72/305)</td><td>Any reduction in scarring (11.9% vs 10.2%); any effect in grade V</td></tr>
<tr><td>PREDICT, 2023</td><td>292 infants, 1&ndash;5 months, grade III&ndash;V, no prior UTI</td><td>First UTI 21.2% vs 35.6%; NNT 7 over 2 years</td><td>A difference in new scars or eGFR at 24 months; effect after prior UTIs</td></tr>
<tr><td>RIVUR/CUTIE cohort, 2015</td><td>305 placebo children with reflux, 195 without</td><td>Not a prophylaxis comparison</td><td>Causation: it identifies risk factors (BBD, baseline scars) only</td></tr>
</tbody></table></div>
<p><strong>Risk factors.</strong> A 2-year cohort that combined the RIVUR placebo arm with 195 children without reflux from the Careful Urinary Tract Infection Evaluation (CUTIE) study found that recurrence was more common with reflux (25.4% vs 17.3%), with baseline BBD (adjusted hazard ratio 2.07) and with a baseline scar on DMSA (adjusted hazard ratio 2.88). Children with BBD and any grade of reflux had the highest risk, 56%.[[apn07_7]]</p>
<p><strong>What neither trial tested.</strong> Neither trial compared prophylaxis with surgery, and neither was large or long enough to show an effect on hypertension, chronic kidney disease (CKD) or kidney failure. Scarring on DMSA is a surrogate. The outcomes families care about lie decades away and have not been measured in these trials. Surgical correction, endoscopic or open, is a decision you make with pediatric urology, usually for breakthrough febrile infections on prophylaxis, high-grade reflux with new scarring, or a family that cannot sustain daily antibiotics.</p>
{{key:Prophylaxis prevents some infections. It has not been shown to prevent scars. Say both halves to every family.}}
{{fig:apn07_b}}
"""),
        ("practice", "Practice", "Bladder, bowel and the attending&rsquo;s plan",
         """<p><strong>Treat the infection with the culture in hand.</strong> Febrile infants who look septic, who cannot keep oral medicine down, or who are very young start intravenously, as your unit&rsquo;s protocol describes. Switch to an oral drug the organism is susceptible to once the child is improving. Know your hospital&rsquo;s antibiogram. A drug chosen because it is on the stock list and not because the organism is susceptible is a common reason for slow defervescence.</p>
<p><strong>Image on purpose.</strong> Renal and bladder ultrasound after a first febrile UTI. VCUG when the ultrasound is abnormal, the course is atypical, or the fever recurs. A DMSA scan, when your center offers one, is most useful several months after the infection to document scars, not during it. Each test exposes the child to sedation, radiation or a catheter, so every order should change a decision.</p>
<p><strong>Decide with the family.</strong> Lay out three paths for a child like Gabriel: prophylaxis with an agreed review date, surgical referral, or careful observation with a fast route to a urine culture at every fever. Give the numbers. Explain that prophylaxis cuts infections, that it has not been shown to prevent scars, and that resistant organisms follow. Agree who checks adherence, who sends the culture at the next fever, and who decides when to stop.</p>
<p><strong>Look for BBD in every toilet-trained child.</strong> Ask about voiding frequency, urgency, daytime wetting, holding postures and stool form. A child who passes urine twice a day at school and once at home, and stools every four days, is not ready for a reflux operation.</p>
<div class="table-wrap"><table>
<thead><tr><th>BBD clue</th><th>What it reflects</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>Voids fewer than four times a day</td><td>Postponement; a bladder that is never emptied fully</td><td>Timed voiding every 2 to 3 hours, including at school</td></tr>
<tr><td>Squatting, leg crossing, urgency</td><td>Overactive detrusor fought by the sphincter</td><td>Voiding diary; refer for urotherapy if it persists</td></tr>
<tr><td>Hard or infrequent stools, soiling</td><td>Constipation compressing the bladder</td><td>Treat constipation first and fully, then reassess the UTIs</td></tr>
<tr><td>Recurrent cystitis in a school-age girl with normal ultrasound</td><td>BBD more often than an anatomic problem</td><td>Treat BBD before ordering a VCUG</td></tr>
</tbody></table></div>
<p>School adds its own pressure. Ask whether the child avoids the school toilet because it lacks water, privacy or soap, and whether she drinks little so that she will not need to go. If she does, and write a note to the school asking that the child be allowed to drink and void freely.</p>
<div class="tc-scene"><span class="tc-lab">In your clinic, the fourth infection &middot; fictional</span><p>Bea, 6, has had four episodes of cystitis this year. Her ultrasound is normal. Her mother asks for a VCUG. You learn that Bea passes urine twice a day, holds until she squats, and has hard stools every few days.</p><p>You start a constipation regimen and timed voiding, give a voiding diary and ask the school to let her use the clinic toilet. Over six months she has one infection.</p><p class="tc-scene-take"><b>What this shows.</b> In a school-age girl, the bladder and bowel are usually the problem, and they are treated without radiation.</p></div>
{{flow:After a febrile UTI|Confirm::Catheter or SPA specimen in the infant; pyuria plus a single uropathogen at the AAP threshold.|Treat::By the culture and the unit&rsquo;s pediatric formulary; switch to oral when improving.|Ultrasound::Renal and bladder ultrasound after the first febrile UTI.|VCUG if indicated::Abnormal ultrasound, atypical course, or recurrence.|Decide with the family::Prophylaxis, surgical referral or observation, with RIVUR and PREDICT numbers and an agreed review date.|Treat the bladder and bowel::In every toilet-trained child with recurrence.|Follow the kidneys::Blood pressure, urinalysis and growth at intervals; creatinine when scars or reduced kidney size are present.}}
{{call:<ul><li>Febrile infant who is septic, lethargic or not feeding</li><li>No clinical improvement after about 48 hours of appropriate therapy (think obstruction, abscess or a resistant organism)</li><li>A rising creatinine, a solitary kidney or bilateral hydronephrosis</li><li>A boy with poor stream, a palpable bladder or a thick-walled bladder on ultrasound (think posterior urethral valves, Module 6)</li></ul>}}
{{key:Every child with scarred kidneys needs a named person who checks blood pressure and urine for years. If no one else owns it, you do.}}
"""),
    ],
    "debrief": [
        "<p><strong>Was it really a UTI?</strong> The first episode is uncertain, because a bag culture cannot establish the diagnosis. The second meets the AAP definition if the catheter culture grows at least 50,000 colonies per mL of a single uropathogen with the pyuria already seen. Count this one, and make sure the culture is followed up and the organism&rsquo;s susceptibilities guide the oral switch.</p>",
        "<p><strong>Prophylaxis, surgery or observation?</strong> Gabriel has grade IV reflux, a dilated system and now two febrile infections. Prophylaxis is reasonable while he is seen by pediatric urology: in PREDICT it lowered first infections in infants with grade III to V reflux (21.2% vs 35.6%, NNT 7 over 2 years), at the price of more resistant and non-<em>E. coli</em> organisms. Surgery is a fair option to discuss with the urologist, especially if he has a breakthrough febrile UTI or a new scar. It is not an emergency tonight, and no trial shows that operating now protects his kidneys better than prophylaxis with close follow-up.</p>",
        "<p><strong>What protects his kidneys?</strong> Tell the family the truth in both halves: prophylaxis prevents some infections, but neither RIVUR nor PREDICT showed fewer scars. What protects the kidney is a prompt, properly collected urine culture at every fever and early treatment, plus a plan for the reflux. Some of his kidney&rsquo;s changes may have been present from birth. Book a DMSA scan when he is well if your center offers it, agree on who sends the next culture, and record blood pressure and growth at every visit.</p>",
    ],
    "skills": {"title": 'Urinary tract infection, reflux and bladder-bowel dysfunction',
               "intro": "Complete with a preceptor, in simulation or at your own unit. Sign-off is local.",
               "items": [("Applies the AAP diagnostic definition and rejects bag cultures as proof of UTI", False),
                         ("Orders ultrasound, VCUG and DMSA only when the result will change a decision", False),
                         ("Counsels a family on prophylaxis using RIVUR and PREDICT absolute numbers and limits", False),
                         ("Takes a bladder and bowel history and starts a BBD plan", False)],
               "placement": "Pediatric ward, nephrology clinic or simulation"},
    "quiz": [
        ("A 10-month-old with fever has a bag urine culture growing <em>E. coli</em> and <em>Enterococcus</em>. What is the best next step?",
         ["Book a VCUG", "Obtain a catheter or SPA specimen with urinalysis before deciding it is a UTI", "Start long-term prophylaxis", "Refer for reimplantation"],
         1, "A bag culture, especially with mixed growth, does not establish UTI. The AAP definition requires pyuria and at least 50,000 colonies per mL of a single uropathogen in an appropriately collected specimen."),
        ("What did RIVUR show about renal scarring?",
         ["Prophylaxis halved scarring", "Prophylaxis eliminated scarring in grade IV reflux", "Scarring did not differ significantly: 11.9% with prophylaxis vs 10.2% with placebo", "Scarring was not measured"],
         2, "Prophylaxis halved recurrences (39/302 vs 72/305) but did not change scarring, and resistance to TMP-SMX rose (63% vs 19%)."),
        ("In PREDICT, what was the number needed to treat for 2 years to prevent one first UTI in infants with grade III to V reflux?",
         ["2", "7", "20", "Prophylaxis had no effect"],
         1, "First UTI 21.2% vs 35.6%; NNT 7 (95% CI 4 to 29). New scars and eGFR did not differ substantially, and resistant and non-<em>E. coli</em> organisms were more common with prophylaxis."),
        ("After a first febrile UTI in an 8-month-old, which imaging does the AAP 2011 guideline advise routinely?",
         ["VCUG and DMSA for all", "Renal and bladder ultrasound; VCUG only if it is abnormal, the course is atypical, or the UTI recurs", "No imaging", "Computed tomography"],
         1, "VCUG is not recommended routinely after the first febrile UTI. Ultrasound findings, an atypical course or recurrence trigger it."),
        ("A 6-year-old girl has a fourth cystitis, a normal ultrasound, voids twice a day and has hard stools. What comes first?",
         ["VCUG", "Treat constipation and start timed voiding", "Endoscopic injection", "Lifelong prophylaxis"],
         1, "Bladder and bowel dysfunction drives recurrence. In the RIVUR/CUTIE cohort, BBD carried an adjusted hazard ratio of 2.07 for recurrence."),
    ],
    "terms": [("UTI", "Urinary tract infection"), ("VUR", "Vesicoureteral reflux"), ("BBD", "Bladder and bowel dysfunction"),
              ("AAP", "American Academy of Pediatrics"), ("VCUG", "Voiding cystourethrogram"), ("DMSA", "Dimercaptosuccinic acid (renal scan)"),
              ("SPA", "Suprapubic aspiration"), ("RIVUR", "Randomized Intervention for Children with Vesicoureteral Reflux"),
              ("PREDICT", "Trial of continuous antibiotic prophylaxis in infants with grade III to V reflux (trial acronym)"), ("CUTIE", "Careful Urinary Tract Infection Evaluation"),
              ("SCOUT", "Short Course Therapy for Urinary Tract Infections"), ("TMP-SMX", "Trimethoprim-sulfamethoxazole"),
              ("NNT", "Number needed to treat"), ("CI", "Confidence interval"), ("eGFR", "Estimated glomerular filtration rate"), ("CKD", "Chronic kidney disease")],
    "readings": [('preventing-uti.html', 'Why UTIs Keep Coming Back — And How to Finally Stop Them'),
                 ('recurrent-uti-ckd.html', 'Recurrent UTI as a CKD Peril'),
                 ('ckd-children-young-adults.html', 'CKD in Children & Young Adults')],
    "calcs": ["calc-pediatric-egfr.html", "calc-schwartz-egfr.html", "calc-pediatric-bp.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
