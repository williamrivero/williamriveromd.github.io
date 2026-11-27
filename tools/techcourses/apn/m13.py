# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 13: Hemolytic uremic syndrome and thrombotic microangiopathy.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, for Philippine practice.
Numbers checked against the PubMed abstracts of Ardissino 2016, Wong 2000, Freedman 2016, Spinale 2013, Greenbaum 2016 and
Ariceta 2021; the 24&ndash;48 hour statement against the HUS International consensus (Loirat 2016) summary. No doses."""

MODULE = {'image_alt': 'A pediatric nephrologist and a mother sit beside a pale toddler in a ward crib while a nurse checks a small urine bag.',
 'objectives': ['Explain how endothelial injury produces the triad of microangiopathic hemolytic anemia, thrombocytopenia and acute kidney injury, and '
                'separate Shiga toxin, pneumococcal and complement-mediated causes at the bedside.',
                'Manage Shiga toxin&ndash;associated HUS with attention to volume, dialysis timing, the brain, and the drugs and transfusions that can harm.',
                'Recognize atypical HUS early, send the right samples before treatment, and plan complement blockade, meningococcal protection and access '
                'in a Philippine setting.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the child with blood, platelets and kidneys failing together</span>'
        'Hemolytic uremic syndrome (HUS) reaches you by phone from a provincial hospital, usually on day five or six of a diarrheal illness, '
        'when the child has stopped passing urine. You decide where the child is safest, what the referring team should stop and start, '
        'when dialysis begins, and whether this is the common infection-triggered disease or the rarer complement disease that needs a different '
        'drug. You also carry the family through a frightening week and the follow-up that lasts years.</div>\n'
        '{{plain:Think of the inner lining of the small kidney vessels as a nonstick coating on a pan. Scratch the coating and everything starts '
        'to stick: platelets clump on the bare spots, red cells are sliced as they squeeze past the clumps, and the narrowed pan heats unevenly.}}\n'
        '<p>The picture has a limit. A scratched pan stays scratched; the endothelium can heal, and most children with the infection-triggered form '
        'recover kidney function. And the scratch has different causes that need different treatments: a bacterial toxin that injures once, a '
        'bacterial enzyme that unmasks a hidden antigen, or an immune system that keeps attacking because its brakes are faulty. The pan does not tell '
        'you which; the history, the stool and the complement studies do.</p>\n'
        '{{cards:Key numbers|STEC infection to HUS (Wong 2000)::10 of 71 children (14%) with <em>E. coli</em> O157:H7 diarrhea developed '
        'HUS|Early volume expansion (Ardissino 2016, observational)::Dialysis 26.3% vs 57.9% in historical controls|Pneumococcal HUS (Spinale '
        '2013)::5&ndash;15% of all HUS cases|Eculizumab, pediatric atypical HUS (Greenbaum 2016)::Complete TMA response in 14 of 22 by week 26|'
        'Ravulizumab, pediatric atypical HUS (Ariceta 2021)::Complete TMA response in 77.8% of 18 by week 26}}\n'
        '<p>Most children with HUS have the Shiga toxin form, need supportive care done well, and recover. A few have pneumococcal disease, '
        'where plasma can do harm, and a few have atypical HUS, where days without complement blockade cost kidney and brain. Your work is to '
        'support the child through the first week, keep the wrong drugs and products away, and recognize the child who does not follow the usual '
        'course.</p>\n',
 'case': {'title': 'The toddler who stopped wetting his diaper',
          'html': '<p>It is 9 p.m. on a Tuesday in July. A pediatric resident at a district hospital in San Jose, Nueva Ecija, calls your mobile phone. '
                  'Gabriel Manalastas is 2 years and 3 months old and weighs 12 kg. Six days ago he had watery diarrhea that turned bloody on '
                  'the second day, with cramps but little fever. The family gave oral rehydration solution and a loperamide syrup bought at a '
                  'pharmacy. The barangay health worker referred him today because he is pale and puffy and his diaper has been dry for '
                  '18 hours.</p>\n'
                  '<p>His hemoglobin is 6.4 g/dL, platelets 34,000/&micro;L, creatinine 3.2 mg/dL, potassium 6.0 mmol/L and lactate '
                  'dehydrogenase (LDH) far above the laboratory range. The smear shows fragmented red cells. Blood pressure is 124/80; '
                  'he is drowsy but rousable. The admitting order sheet already lists intravenous ciprofloxacin, a platelet transfusion and '
                  'furosemide &ldquo;for oliguria.&rdquo; The consultant on duty has also asked whether fresh frozen plasma should be given '
                  '&ldquo;because this is HUS.&rdquo; The nearest pediatric unit that can dialyze a 12 kg child is three hours away in Manila. '
                  'His mother, Rowena, asks you directly whether he will need a machine.</p>\n',
          'questions': ['What is the most likely diagnosis, and what on the order sheet should change tonight?',
                        'Where should Gabriel be treated, and what decides when dialysis starts?',
                        'What would make you suspect atypical HUS instead, and what should be sent before any plasma or blood product?']},
 'sections': [('physiology',
               'Physiology',
               'How the endothelium fails',
               '<p>Thrombotic microangiopathy (TMA) is a lesion, not a diagnosis. Injured endothelial cells swell and detach, the subendothelial '
               'space widens, and platelet&ndash;fibrin thrombi form in arterioles and glomerular capillaries. Red cells are torn as they pass, '
               'which produces fragmented cells (schistocytes), a high LDH, a low haptoglobin and a negative direct antiglobulin test. Platelets '
               'are consumed. The glomerulus, with its fenestrated endothelium and high flow, is where the injury shows first, so acute kidney '
               'injury (AKI) completes the triad.</p>\n'
               '<p>Three upstream causes dominate in children, and each injures the endothelium by a different route.</p>\n'
               '<p><strong>Shiga toxin.</strong> Shiga toxin&ndash;producing <em>Escherichia coli</em> (STEC), classically O157:H7, colonizes the '
               'colon and releases toxin that crosses the inflamed gut wall. The toxin binds globotriaosylceramide (Gb3), a receptor that is '
               'dense on glomerular endothelium and podocytes, enters the cell, and stops protein synthesis. The injured cell turns '
               'prothrombotic. The diarrhea usually precedes HUS by several days, and the window between bloody diarrhea and HUS is when volume '
               'status and drug choices matter most. In a prospective cohort of 71 children under 10 with O157:H7 diarrhea, 10 (14%) developed '
               'HUS.[[apn13_2]]</p>\n'
               '<p><strong>Pneumococcal neuraminidase.</strong> <em>Streptococcus pneumoniae</em> produces neuraminidase, which strips sialic acid '
               'from cell surfaces and exposes the Thomsen&ndash;Friedenreich (T) antigen on red cells, platelets and endothelium. Preformed '
               'antibodies in plasma bind the exposed antigen. Pneumococcal HUS accounts for about 5&ndash;15% of all HUS, often after pneumonia '
               'with empyema or meningitis, and the review that reports this notes that fresh frozen plasma, which carries more of those '
               'antibodies, should be avoided.[[apn13_4]] The direct antiglobulin test is often positive here, unlike STEC-HUS.</p>\n'
               '<p><strong>Complement dysregulation.</strong> The alternative complement pathway idles continuously on every cell surface. Factor H, '
               'factor I and membrane cofactor protein (CD46) keep it from attacking host endothelium. A loss-of-function variant in a regulator, a '
               'gain-of-function variant in C3 or factor B, or an autoantibody against factor H removes the brake. A trigger such as an infection, '
               'including a diarrheal one, then sets off terminal complement (C5b-9) on the endothelium, and the attack continues after the trigger '
               'is gone. This is atypical HUS (aHUS), and it is the form where blocking C5 changes the course.[[apn13_8]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Cause</th><th>What injures the endothelium</th><th>What you see first</th>'
               '<th>Clue that points here</th></tr></thead><tbody>'
               '<tr><td>STEC-HUS</td><td>Shiga toxin binding Gb3, stopping protein synthesis</td><td>Bloody diarrhea, then pallor and falling urine '
               'output several days later</td><td>Bloody stool, age 1&ndash;5 years, clustered cases, a positive stool test for Shiga toxin or '
               'STEC</td></tr>'
               '<tr><td>Pneumococcal HUS</td><td>Neuraminidase exposing the T antigen; antibody binding</td><td>A child with pneumonia, empyema or '
               'meningitis who becomes anemic and oliguric</td><td>Invasive pneumococcal infection; a positive direct antiglobulin test</td></tr>'
               '<tr><td>Atypical HUS</td><td>Uncontrolled alternative-pathway complement on host endothelium</td><td>TMA with or without a mild '
               'trigger; may relapse; may be familial</td><td>No bloody diarrhea, a young infant, a previous episode, a family history, low C3, '
               'progression despite good supportive care</td></tr>'
               '<tr><td>Secondary TMA</td><td>Drug, malignant hypertension, transplant, lupus, cobalamin C disorder</td><td>Depends on the '
               'setting</td><td>A culprit drug, very high blood pressure, a systemic disease, an infant with metabolic features</td></tr>'
               '</tbody></table></div>\n'
               '<p>The brain shares the same vessel biology. Seizures, a falling level of consciousness, or focal signs in a child with HUS are TMA '
               'in the brain until proven otherwise, worsened by hypertension, hyponatremia and uremia. The gut can perforate or infarct; the '
               'pancreas can fail and produce diabetes; the heart can be injured. HUS is a systemic disease that the kidney reports first.</p>\n'
               '{{key:Name the lesion first (TMA), then name the cause. The cause, not the lesion, decides whether you support, avoid plasma, or block '
               'complement.}}\n'
               '<div class="tc-scene"><span class="tc-lab">On the ward, a second look at the smear &middot; fictional</span><p>A 4-year-old in '
               'Tarlac is admitted with pneumonia and a right-sided effusion. On day 3 she is pale and her urine is dark and scant. Her platelets '
               'are 41,000/&micro;L and the smear shows schistocytes. The resident starts setting up fresh frozen plasma &ldquo;for HUS.&rdquo;</p>'
               '<p>You ask him to hold it. The effusion is purulent, the blood culture grows <em>S. pneumoniae</em>, and her direct antiglobulin '
               'test is positive.</p><p class="tc-scene-take"><b>What this shows.</b> Pneumococcal HUS is the one form where plasma may add fuel. '
               'Washed red cells, if transfusion is needed, and treatment of the infection are the safer path.</p></div>\n'
               '\n{{fig:apn13_a}}\n'),
              ('stec',
               'STEC-HUS',
               'Shiga toxin HUS: support, fluids and what to avoid',
               '<p>No drug has been shown to stop STEC-HUS once it starts. Outcomes depend on supportive care: perfusion, fluid and electrolytes, '
               'blood pressure, nutrition, timely dialysis, and protection of the brain. Two decisions dominate the first days: how much fluid to '
               'give, and which drugs to keep away.</p>\n'
               '<p><strong>Fluid.</strong> Children with STEC infection are often hemoconcentrated when HUS begins, and hemoconcentration at onset is '
               'associated with more severe disease. Ardissino and colleagues at a single Italian center gave every child with STEC-HUS from 2012 to '
               '2014 an early intravenous volume expansion aimed at about 10% of working weight and compared them with 38 historical patients whose '
               'fluids had been restricted. The expanded group needed dialysis less often (26.3% vs 57.9%), had less central nervous system involvement '
               '(7.9% vs 23.7%, a difference that did not reach statistical significance, P = .06), fewer intensive care days, and fewer long-term '
               'kidney and extrarenal sequelae (13.2% vs 39.5%).[[apn13_1]] This is an observational study with historical controls, so changes in '
               'referral, recognition and other care over time may explain part of the difference. It suggests that restoring circulating volume '
               'helps; it does not show that a child who is already anuric and edematous should receive more fluid.</p>\n'
               '<p>The practical reading: in the prodrome and the first hours of HUS, a dry child with urine still coming needs volume restored, '
               'with close weights and balance. Once the child is anuric and overloaded, more fluid without a way to remove it causes pulmonary '
               'edema and hypertension, and that child needs dialysis, not a bolus.</p>\n'
               '<p><strong>Antibiotics.</strong> In the 2000 cohort, 5 of the 10 children who developed HUS had received antibiotics, and antibiotic '
               'treatment was associated with HUS after adjustment (relative risk 17.3, 95% confidence interval 2.2 to 137).[[apn13_2]] The wide '
               'interval reflects nine treated children. A 2016 meta-analysis of 17 reports and 1,896 patients found a pooled odds ratio of 1.33 '
               '(0.89 to 1.99) overall, but 2.24 (1.45 to 3.46) when restricted to studies at low risk of bias that used an acceptable HUS '
               'definition, and its authors concluded that antibiotics are not recommended in STEC infection.[[apn13_3]] The proposed mechanism is '
               'toxin release from injured bacteria and induction of the toxin-carrying phage. The evidence is observational, the antibiotic classes '
               'differ, and the question is not settled; in practice, a child with bloody diarrhea and suspected STEC should not receive '
               'antibiotics for the diarrhea unless another indication exists, such as sepsis.</p>\n'
               '<p><strong>Antimotility drugs.</strong> Loperamide and similar drugs slow toxin clearance from the gut and are widely avoided in '
               'bloody diarrhea in children. The evidence is weaker than for antibiotics, but the drug offers a child no benefit worth the '
               'risk.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Order</th><th>Physiologic reason for caution</th><th>What to do instead</th></tr>'
               '</thead><tbody>'
               '<tr><td>Antibiotic for bloody diarrhea</td><td>May increase toxin release; associated with HUS in cohort and meta-analysis '
               'data</td><td>Stop unless there is a separate indication; culture stool and blood</td></tr>'
               '<tr><td>Loperamide or another antimotility drug</td><td>Slows clearance of toxin from the colon</td><td>Stop; treat cramps and '
               'dehydration</td></tr>'
               '<tr><td>Platelet transfusion</td><td>Fresh platelets may feed microthrombi; the count is low from consumption, not failed '
               'production</td><td>Reserve for active bleeding or before a procedure such as catheter insertion, as the unit&rsquo;s protocol '
               'states</td></tr>'
               '<tr><td>Loop diuretic in an anuric child</td><td>Little urine to work on; ototoxic at high exposure; delays the dialysis decision</td>'
               '<td>Assess volume; a single trial in a child still passing urine may be reasonable; plan dialysis if anuric</td></tr>'
               '<tr><td>Nephrotoxins (aminoglycoside, NSAID, contrast)</td><td>Add tubular injury to a kidney with no reserve</td><td>Avoid; '
               'adjust every renally cleared drug</td></tr>'
               '<tr><td>Fresh frozen plasma &ldquo;for HUS&rdquo;</td><td>No benefit shown in STEC-HUS; harmful in pneumococcal HUS</td><td>Hold '
               'until the cause is clear; consider only if atypical HUS is likely and complement blockade is unavailable</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Transfusion of red cells.</strong> Hemolysis can drop hemoglobin quickly. Red cells are given for symptomatic anemia or a '
               'threshold set by the unit&rsquo;s protocol, slowly, with attention to volume and potassium in an anuric child.</p>\n'
               '<p><strong>Dialysis.</strong> The usual indications apply: refractory hyperkalemia, acidosis, fluid overload with respiratory '
               'compromise or hypertension, uremic encephalopathy, and the need to make room for blood products and nutrition. Peritoneal dialysis '
               '(PD) suits small children and avoids heparin and a large central catheter in a child with low platelets; hemodialysis or continuous '
               'kidney replacement therapy (CKRT) is used where PD is not possible, for example after colitis with bowel injury. Module 16 covers '
               'acute PD and CKRT.</p>\n'
               '{{key:In STEC-HUS, restore volume while the child can still make urine, keep antibiotics, antimotility drugs, platelets and plasma '
               'away unless a specific reason exists, and dialyze for the usual indications before overload sets in.}}\n'
               '<div class="tc-scene"><span class="tc-lab">Two days before HUS, in a rural health unit &middot; fictional</span><p>A 3-year-old '
               'boy in Bulacan has had bloody diarrhea for two days. His older sister had the same illness last week. The rural health physician '
               'messages you a photograph of the stool and asks which antibiotic to give.</p><p>You advise oral rehydration, no antibiotic and no '
               'loperamide, a stool sample to the provincial laboratory if available, and a complete blood count, creatinine and urine check in '
               '48 hours or sooner if he looks pale, sleepy or stops passing urine.</p><p class="tc-scene-take"><b>What this shows.</b> The window '
               'before HUS is where hydration and drug choices are made, usually by someone other than you.</p></div>\n'),
              ('atypical',
               'Atypical HUS',
               'Atypical HUS and complement blockade',
               '<p>Atypical HUS is rare, but it is the form where your speed matters most. Without complement blockade, many children progress to '
               'kidney failure or relapse, and relapses can recur after transplant. With blockade, most recover hematologically and many recover '
               'kidney function.</p>\n'
               '<p><strong>Suspecting it.</strong> Think of aHUS when a child has TMA without bloody diarrhea, is under 6 months old, has had an '
               'episode before, has a relative with HUS, has a low serum C3, or keeps hemolyzing and losing platelets after the first week of good '
               'supportive care. A diarrheal trigger does not exclude aHUS; complement variants can declare themselves after an infection, '
               'including STEC. In some populations, notably in South Asia, antibody against factor H is a common acquired cause; it matters because '
               'it is treated with immunosuppression as well as plasma or complement blockade.</p>\n'
               '<p><strong>Sampling before treatment.</strong> Plasma infusion, plasma exchange and complement blockade all change the results of '
               'complement studies. Before the first dose of any of them, draw and store serum and EDTA plasma for C3, C4, factor H, factor I, '
               'CD46 expression, anti-factor H antibodies and genetic testing, and send a von Willebrand factor&ndash;cleaving protease '
               '(ADAMTS13) activity to exclude thrombotic thrombocytopenic purpura. Your hospital may need to send these abroad; the sample can be '
               'stored and sent later, but it cannot be drawn later.</p>\n'
               '<p><strong>The evidence for blockade.</strong> Eculizumab, a monoclonal antibody against C5, was studied prospectively in children '
               'in an open-label, single-arm phase II trial: 22 patients aged 5 months to 17 years, 11 on dialysis at baseline. By week 26, 14 had a '
               'complete TMA response, 18 normalized platelets and LDH, and 9 of the 11 on dialysis came off it; no deaths or meningococcal '
               'infections occurred.[[apn13_6]] Ravulizumab, an engineered longer-acting C5 antibody, was studied in a single-arm phase III trial '
               'in 18 complement inhibitor&ndash;na&iuml;ve children, median age 5.2 years: 77.8% had a complete TMA response by week 26 and 94.4% '
               'by week 50, again with no meningococcal infections.[[apn13_7]] Neither trial had a control group, and both are small, so they '
               'demonstrate response but cannot estimate how much better blockade is than plasma therapy. The size of the response in a disease '
               'that otherwise often ends in dialysis is why it is accepted as first-line treatment.</p>\n'
               '<p><strong>The consensus.</strong> HUS International, an expert group, proposed complement blockade as first-line treatment for '
               'children with a clinical diagnosis of aHUS, ideally started within 24 to 48 hours of onset or admission, with plasma exchange, or '
               'plasma infusion if exchange is not possible, while blockade is unavailable.[[apn13_5]] This is expert consensus, not a graded '
               'recommendation. The KDIGO Controversies Conference on aHUS and C3 glomerulopathy reached broadly similar conclusions and set out '
               'the unanswered questions, especially how long to continue treatment.[[apn13_8]]</p>\n'
               '<p><strong>Meningococcal protection.</strong> Terminal complement is the body&rsquo;s main defense against <em>Neisseria '
               'meningitidis</em>. Every child who receives C5 blockade needs meningococcal vaccination and, because a vaccine response takes time '
               'and may be incomplete, antibiotic prophylaxis as the consensus and the product information describe.[[apn13_5]] Families need a '
               'written fever plan: fever in a child on C5 blockade is an emergency.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Step</th><th>Why it matters physiologically</th><th>Philippine reality</th></tr>'
               '</thead><tbody>'
               '<tr><td>Store complement and genetic samples first</td><td>Plasma and C5 blockade alter the results</td><td>Testing is often sent '
               'abroad; store serum and EDTA plasma frozen until a route is arranged</td></tr>'
               '<tr><td>Exclude TTP with ADAMTS13</td><td>Severe ADAMTS13 deficiency needs plasma exchange, not C5 blockade</td><td>The result may '
               'take days; send it, do not wait for it to start support</td></tr>'
               '<tr><td>Complement blockade if aHUS is likely</td><td>Stops C5b-9 formation on the endothelium</td><td>Availability and cost are the '
               'barriers; confirm supply with the hospital pharmacy and the family&rsquo;s funding before you promise it</td></tr>'
               '<tr><td>Plasma exchange or infusion as a bridge</td><td>Replaces missing regulators and removes antibody or mutant protein</td>'
               '<td>Plasma exchange in a small child needs a large catheter and an experienced team, often only in Manila or Cebu</td></tr>'
               '<tr><td>Meningococcal vaccine and prophylaxis</td><td>C5 blockade removes the main defense against <em>Neisseria</em></td><td>Check '
               'which meningococcal vaccines are available locally; document the plan and the fever instructions</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Cost and access.</strong> C5 inhibitors are among the most expensive drugs in medicine and are not stocked in most '
               'Philippine hospitals. The attending&rsquo;s job is to start the access process on day one: confirm whether the drug is obtainable, '
               'involve the hospital&rsquo;s social service and medical director, document the indication so that charitable and government '
               'assistance applications can move, and arrange plasma therapy in the meantime. Do not tell a family that a drug will arrive until '
               'someone has confirmed that it will.</p>\n'
               '{{key:If you suspect atypical HUS, draw and store the complement and genetic samples before any plasma or blockade, start access to '
               'complement blockade on day one, and bridge with plasma therapy while you wait.}}\n'
               '\n{{fig:apn13_b}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Confirm TMA and look for the cause in the first hour.</strong> Ask for a smear review, LDH, haptoglobin, reticulocytes, '
               'direct antiglobulin test, creatinine, electrolytes, urinalysis, blood pressure and a careful volume examination. Send stool for '
               'Shiga toxin or STEC where a laboratory can test it; send blood and other cultures if pneumococcal disease is possible; and store '
               'complement samples if the story is not typical.</p>\n'
               '<p><strong>Decide where the child is safest.</strong> A child with HUS who is anuric, hyperkalemic, hypertensive, overloaded or '
               'drowsy needs a bed where dialysis can start the same day and the brain can be watched. If transfer is three hours away, call the '
               'accepting pediatric nephrologist and intensivist yourself, agree on what happens before the ambulance leaves (potassium treatment, '
               'stopping harmful orders, blood pressure control, a working intravenous line), and send a written endorsement.</p>\n'
               '{{flow:First 24 hours in suspected HUS|Confirm TMA::Smear with schistocytes, high LDH, low platelets, AKI. Note the direct antiglobulin '
               'test.|Find the trigger::Bloody diarrhea and stool testing; pneumonia, empyema or meningitis; no trigger, a young infant or a prior '
               'episode.|Stop what harms::Antibiotics for the diarrhea alone, antimotility drugs, routine platelets, plasma in suspected pneumococcal '
               'disease, nephrotoxins.|Fix what kills::Potassium, acidosis, severe hypertension, fluid overload, seizures.|Choose the bed::Same-day '
               'dialysis and neurologic monitoring for an anuric, overloaded or drowsy child.|Store samples::Complement and genetic samples and '
               'ADAMTS13 before plasma or blockade if aHUS is possible.|Write the plan::Weights, balance, blood pressure targets as the unit sets them, '
               'daily labs, who calls whom.}}\n'
               '<p><strong>Run the week.</strong> Weigh daily, chart intake and output, and check hemoglobin, platelets, LDH, creatinine and '
               'electrolytes at least daily while hemolysis is active. Rising platelets and a falling LDH usually come before urine output returns. '
               'Treat hypertension, keep sodium within a safe range, and feed early; PD fluid and catabolism make protein and energy needs high. '
               'Look at the abdomen every day for perforation or pancreatitis, and check blood glucose.</p>\n'
               '<p><strong>Watch the brain.</strong> Seizures, a falling level of consciousness, or focal signs are an emergency. Treat seizures, '
               'correct sodium and blood pressure, and involve the intensivist. Whether complement blockade helps in severe neurologic STEC-HUS is '
               'debated and the evidence is limited to case series; if it is being considered, it is a decision for the attending with the family '
               'and the intensivist, with the uncertainty stated plainly.</p>\n'
               '<p><strong>When the course is not typical.</strong> Persistent hemolysis and low platelets after the first week, a C3 below range, '
               'no diarrhea, an infant under 6 months, or a relapse should make you revisit the diagnosis and move on complement samples and access.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>What you see on day 7 to 10</th><th>Likely meaning</th><th>What you do</th></tr></thead>'
               '<tbody>'
               '<tr><td>Platelets normal, LDH falling, urine returning</td><td>Endothelium healing; typical STEC course</td><td>Taper dialysis, '
               'plan follow-up</td></tr>'
               '<tr><td>Platelets low, LDH high, still anuric</td><td>Ongoing TMA; aHUS possible</td><td>Review complement results, discuss '
               'blockade or plasma, re-examine the history</td></tr>'
               '<tr><td>New seizure or coma</td><td>Cerebral TMA, hypertension, hyponatremia</td><td>Emergency care; intensive care bed; '
               'senior discussion of options</td></tr>'
               '<tr><td>Rising glucose, abdominal pain</td><td>Pancreatic or bowel involvement</td><td>Surgical review; insulin per protocol</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Follow for years.</strong> Children who recover from STEC-HUS can carry proteinuria, hypertension and a reduced GFR into '
               'adolescence; in the Italian cohort, 13.2% of the volume-expanded group and 39.5% of historical controls had kidney or extrarenal sequelae.[[apn13_1]] Plan blood pressure, urine protein and creatinine checks at discharge, '
               'then at intervals the unit sets, for several years, and longer if any abnormality persists. Tell the family in writing; they '
               'are the ones who will remember.</p>\n'
               '{{call:<ul><li>Anuria with potassium rising or ECG changes</li><li>Seizure, falling level of consciousness or focal signs</li>'
               '<li>Fluid overload with rising oxygen need</li><li>Severe hypertension</li><li>Abdominal distension, peritonism or rectal bleeding '
               'after the diarrhea had settled</li><li>Fever in any child receiving complement blockade</li></ul>}}\n'
               '{{key:Every child with HUS leaves with a written plan: the cause as best known, the dialysis days, the blood pressure, the urine '
               'protein, and who checks each one next.}}\n'
               '\n{{fig:apn13_c}}\n')],
 'debrief': ['<p><strong>Diagnosis and the order sheet.</strong> Bloody diarrhea six days ago in a toddler, then hemolysis with schistocytes, '
             'low platelets and anuric AKI, is STEC-HUS until proven otherwise. Ask the resident to stop the ciprofloxacin (no other indication '
             'has been found), hold the platelet transfusion (he is not bleeding and no procedure is under way), hold the fresh frozen plasma '
             '(no benefit in STEC-HUS, and the cause is not yet confirmed), and stop the loperamide the family was giving. Treat the potassium '
             'now as the unit&rsquo;s protocol directs, avoid nephrotoxins, and send stool for Shiga toxin testing if any laboratory can do it.</p>\n',
             '<p><strong>Where and when.</strong> He is anuric, hyperkalemic, hypertensive and drowsy, so he needs a pediatric unit that can '
             'dialyze a 12 kg child today and watch his brain. Call the accepting team in Manila yourself. Furosemide in an anuric child will not '
             'help and may delay the decision. Dialysis starts for refractory potassium, acidosis, overload or encephalopathy, and to make room for '
             'blood and nutrition; acute PD is a good choice in a toddler with low platelets. Tell Rowena honestly: yes, he probably needs '
             'dialysis for a while, most children with this illness recover kidney function, and the next days are about keeping him safe while '
             'the kidneys heal.</p>\n',
             '<p><strong>When to think atypical.</strong> No bloody diarrhea, age under 6 months, a previous episode, a relative with HUS, a low '
             'C3, or hemolysis and low platelets that persist after the first week would point to atypical HUS. If any of these appears, draw and '
             'store serum and EDTA plasma for complement studies, anti-factor H antibodies and genetics, and send ADAMTS13, before any plasma '
             'or complement blockade, then start the access process for C5 blockade and arrange plasma therapy as a bridge.</p>\n'],
 'skills': {'title': 'Hemolytic uremic syndrome and thrombotic microangiopathy',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Confirms TMA from smear, LDH, haptoglobin, platelets and creatinine, and names the likely cause', False),
                      ('Reviews an admission order sheet for HUS and removes harmful orders with a stated reason', False),
                      ('Lists the complement and genetic samples to store before plasma or blockade, and arranges their storage', False),
                      ('Writes a discharge and long-term follow-up plan for a child after STEC-HUS', False)],
            'placement': 'Supervised practice on the pediatric ward or PICU, or simulation'},
 'quiz': [('A 3-year-old has had bloody diarrhea for two days and is still passing urine. A sibling had the same illness. Which advice best '
           'fits the evidence?',
           ['Give an antibiotic now to prevent HUS',
            'Give oral or intravenous fluid to keep him well hydrated, avoid antibiotics and antimotility drugs, and recheck blood count and '
            'creatinine soon',
            'Restrict fluids to prevent edema',
            'Give loperamide to reduce stool losses'],
           1,
           'Volume restoration is associated with less dialysis in observational data, while antibiotics are associated with HUS in cohort and '
           'meta-analysis data. Antimotility drugs slow toxin clearance.'),
          ('In the Ardissino 2016 study of early volume expansion in STEC-HUS, what does the design allow you to conclude?',
           ['That fluid restriction is harmful in every child with HUS',
            'That early volume expansion was associated with less dialysis (26.3% vs 57.9%) compared with historical controls, without '
            'proving cause',
            'That volume expansion cures HUS',
            'That anuric, overloaded children should receive fluid boluses'],
           1,
           'It was a single-center comparison with historical controls. The association is strong, but other changes over time may contribute, '
           'and it says nothing in favor of fluid for an already overloaded, anuric child.'),
          ('A child with pneumococcal empyema develops TMA with a positive direct antiglobulin test. Which product should be avoided?',
           ['Fresh frozen plasma',
            'Antibiotics for the pneumonia',
            'Oxygen',
            'Peritoneal dialysis if indicated'],
           0,
           'Neuraminidase exposes the T antigen; plasma carries antibodies that bind it. The review cited in this module advises avoiding fresh '
           'frozen plasma.'),
          ('Before plasma therapy or complement blockade in suspected atypical HUS, what should be done?',
           ['Nothing; treatment should never be delayed for samples',
            'Wait for genetic results before starting any treatment',
            'Draw and store samples for complement studies, anti-factor H antibodies, genetics and ADAMTS13',
            'Give a platelet transfusion'],
           2,
           'Plasma and C5 blockade change complement results. Samples take minutes to draw and can be stored and sent later; treatment is not '
           'delayed waiting for results.'),
          ('What did the pediatric single-arm trial of eculizumab in atypical HUS report by week 26?',
           ['No effect on dialysis dependence',
            'Meningococcal infection in a third of patients',
            'A mortality reduction compared with plasma exchange',
            'Complete TMA response in 14 of 22 children, and 9 of 11 on dialysis came off it'],
           3,
           'Greenbaum 2016 had no control group, so it shows response rather than a comparison with plasma therapy. No meningococcal infections '
           'occurred in that trial.')],
 'terms': [('HUS', 'Hemolytic uremic syndrome'),
           ('aHUS', 'Atypical hemolytic uremic syndrome'),
           ('TMA', 'Thrombotic microangiopathy'),
           ('STEC', 'Shiga toxin&ndash;producing <em>Escherichia coli</em>'),
           ('Gb3', 'Globotriaosylceramide, the Shiga toxin receptor'),
           ('LDH', 'Lactate dehydrogenase'),
           ('AKI', 'Acute kidney injury'),
           ('PD', 'Peritoneal dialysis'),
           ('CKRT', 'Continuous kidney replacement therapy'),
           ('ADAMTS13', 'A disintegrin and metalloproteinase with thrombospondin motifs 13 (von Willebrand factor&ndash;cleaving protease)'),
           ('TTP', 'Thrombotic thrombocytopenic purpura'),
           ('CD46', 'Membrane cofactor protein'),
           ('C5b-9', 'Terminal complement complex (membrane attack complex)'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('NSAID', 'Nonsteroidal anti-inflammatory drug'),
           ('EDTA', 'Ethylenediaminetetraacetic acid (anticoagulant tube)'),
           ('ECG', 'Electrocardiogram'),
           ('GFR', 'Glomerular filtration rate'),
           ('PICU', 'Pediatric intensive care unit')],
 'readings': [('complement-mediated-kidney-disease.html', 'Complement-Mediated Kidney Disease: C3G, aHUS & MPGN'),
              ('complement-targeted-therapy-kidney-disease.html', 'Complement Inhibitors in Kidney Disease: Clinical Guide'),
              ('ckd-children-young-adults.html', 'CKD in Children & Young Adults')],
 'calcs': ['calc-pediatric-aki.html', 'calc-pediatric-uo.html', 'calc-fluid-overload.html', 'calc-reticulocyte-rpi.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
