# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 22: PD peritonitis and exit-site and tunnel infection.
Written November 27, 2026 for the Renal Care Academy, in the voice of the Physician on Duty modules and to the medical teaching standard.
Definitions, grades and benchmarks checked against the ISPD 2024 pediatric infection guideline (publisher full text), the ISPD 2022 peritonitis
and 2023 catheter-related infection abstracts, and SCOPE and IPPN registry abstracts. No antibiotic dose appears in this file; doses come
from the ISPD pediatric tables and the unit's pediatric formulary."""

MODULE = {
 'image_alt': 'A Filipino mother holds a peritoneal dialysis drain bag up to a lamp at night to look at the effluent while talking on her phone, her young daughter resting on the bed behind her.',
 'objectives': [
    'Diagnose peritoneal dialysis (PD) peritonitis in a child using the 2024 international pediatric criteria, and start empirical intraperitoneal antibiotics without delay.',
    'Classify refractory, relapsing, recurrent and repeat peritonitis and fungal peritonitis, and decide when the catheter must come out.',
    'Score and treat exit-site and tunnel infection, calculate the unit&rsquo;s peritonitis rate, and lead retraining and quality improvement after every episode.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the night call and the unit&rsquo;s rate</span>Peritonitis usually reaches you '
        'by phone, at night, from a mother far from the peritoneal dialysis (PD) center. You decide within minutes whether the child is treated now and where, you make sure '
        'cultures are taken and antibiotics start, and you own the follow-up: the culture result, the response at day 3 to 5, the catheter decision, '
        'and the retraining. Each month you also own the program&rsquo;s infection rate.</div>\n'
        '{{plain:Peritonitis in a child on PD is like a house fire that starts in the kitchen. The smoke (cloudy fluid) shows early, and a fire caught in '
        'the first minutes is put out with a kitchen extinguisher. Wait until morning and you may lose the house.}}\n'
        '<p>The picture has a limit. A fire has one source. Peritonitis has several routes in, and the route tells you what to fix afterward: a hand '
        'that touched a connection, an infected exit site, a gut that leaked bacteria, or blood that carried them. And unlike a house, the peritoneum '
        'that survives a bad infection may not work as well again; repeated episodes thicken the membrane and shorten PD life. The infant '
        'recommendations put it plainly: the aim is to preserve the peritoneal membrane, not the catheter.[[apn22_11]]</p>\n'
        '{{cards:Key numbers|Diagnosis (2024 pediatric guideline)::Two of three: clinical features; effluent white cells over 100/mm&sup3; with at '
        'least 50% neutrophils after a dwell of at least 2 hours; positive culture|Overall peritonitis rate::No more than 0.40 episodes per patient-year '
        '(International Society for Peritoneal Dialysis [ISPD] 2022; pediatric benchmark 0.4)|Peritonitis-free patients::More than 80% per year (ISPD 2022)|Culture-negative episodes::Less than 15% '
        '(pediatric benchmark)|Standardizing Care to Improve Outcomes in Pediatric End Stage Kidney Disease (SCOPE) collaborative::0.46 episodes per patient-year overall; 0.62 in children 2 years or younger}}\n'
        '<p>Most episodes in children respond to prompt empirical antibiotics given into the peritoneum. A few are refractory, fungal or relapsing and '
        'cost the child the catheter or the membrane. Your work is to treat cloudy effluent as peritonitis until proven otherwise, start treatment the '
        'same night, follow the response by day, and use every episode to fix the step that failed.</p>\n',
 'case': {'title': 'Cloudy at 10 p.m.',
          'html': '<p>Kyla Mendoza is 5 years old and weighs 17 kg. She has been on home continuous ambulatory PD (CAPD) for 11 months. At 10 p.m. her '
                  'mother, Jenny, calls your mobile phone from Baliuag, Bulacan. The bag from the evening exchange is cloudy; she cannot read the '
                  'newspaper through it. Kyla has had a tummy ache since the afternoon and a temperature of 38.2 &deg;C. She is drinking and talking. '
                  'Yesterday the cap of the transfer set fell on the floor and Jenny put it back on &ldquo;quickly.&rdquo;</p>\n'
                  '<p>The pediatric PD center is 90 minutes away by car, and the family has no car tonight. A district hospital is 15 minutes away; it '
                  'has a pediatric resident on duty but no pediatric nephrologist and has never treated PD peritonitis. Jenny asks whether she can '
                  'give paracetamol and bring Kyla to the center in the morning.</p>\n',
          'questions': ['Is this peritonitis, and what must happen tonight?',
                        'Where should Kyla be treated, and what will you tell the district hospital?',
                        'What happens after the episode, for Kyla and for the program?']},
 'sections': [
  ('physiology', 'Physiology', 'How organisms reach the peritoneum',
   '<p>The peritoneum has good defenses: resident macrophages, mesothelial cells and a fluid that dilutes and clears bacteria. PD weakens them. '
   'Every exchange dilutes the immune cells and opsonins, glucose solutions impair cell function, and the catheter is a foreign body crossing the '
   'skin. Organisms arrive by four routes, and each route has a typical organism and a typical fix.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Route</th><th>How it happens in a child</th><th>Typical organisms</th><th>What it tells you to '
   'fix</th></tr></thead><tbody>'
   '<tr><td>Touch contamination (intraluminal)</td><td>A hand, a dropped cap or a broken bag at connection</td><td>Skin flora: coagulase-negative '
   'staphylococci, <em>Staphylococcus aureus</em></td><td>Technique: retraining, observed exchange</td></tr>'
   '<tr><td>Exit site and tunnel (periluminal)</td><td>Bacteria track along the catheter from an infected exit site</td><td><em>S. aureus</em>, '
   '<em>Pseudomonas</em></td><td>Exit-site care, catheter orientation, treatment of exit-site infection</td></tr>'
   '<tr><td>Transmural from the bowel</td><td>Constipation, diarrhea, colitis, a nearby gastrostomy or ostomy</td><td>Gram-negative rods, anaerobes, '
   'several organisms together</td><td>Bowel care; look for surgical pathology if polymicrobial</td></tr>'
   '<tr><td>Hematogenous or ascending</td><td>Bacteremia; rarely via the genital tract</td><td>Streptococci, others</td><td>Source elsewhere</td></tr>'
   '</tbody></table></div>\n'
   '<p><strong>Children differ.</strong> Infants have the highest rates. In SCOPE, 156 infants with a PD catheter placed before their first birthday '
   'had an in-hospital peritonitis rate of 1.73 and an overall rate of 0.76 episodes per patient-year; nephrectomy at or before catheter placement and '
   'a gastrostomy placed after the catheter were associated with nearly sixfold and nearly threefold higher risk, and infants with peritonitis had '
   'lower survival (86.3% versus 95.6%).[[apn22_6]] Gram-negative &ldquo;diaper peritonitis&rdquo; is more frequent in infants, and fungal '
   'infection is more common in children with a gastrostomy.[[apn22_11]] Touch contamination is common: 846 of 2,685 children (32%) in SCOPE reported '
   'at least one, more often in younger children.[[apn22_7]]</p>\n'
   '<p><strong>What children grow and how episodes end.</strong> In 391 episodes among 734 children in SCOPE, gram-positive organisms caused 37.8%, '
   'culture-negative episodes made up 24.7%, gram-negative organisms 19.5%, polymicrobial infections 10.3% and fungi alone 7.7%. Treatment with '
   'antibiotics alone resolved 76.6% of episodes; 12.2% ended in permanent catheter removal and 6% in removal with return to PD.[[apn22_4]] Organisms '
   'and susceptibilities vary by region: in an international registry, gram-negative episodes and <em>Pseudomonas</em> were more frequent in some '
   'regions than others, and susceptibility to first-generation cephalosporins and aminoglycosides varied significantly.[[apn22_10]] Your own '
   'program&rsquo;s culture log is therefore part of the empirical choice.</p>\n'
   '<p>Very young children on PD may have low immunoglobulin levels from protein loss in the effluent. The infant recommendations note that the link '
   'with severe infection is not straightforward, that antibody responses to vaccines are usually normal, and that there is no evidence for routine '
   'prophylactic immunoglobulin.[[apn22_11]] Keep the child&rsquo;s vaccinations up to date; they protect against the bacteremias that can seed the '
   'peritoneum.</p>\n'
   '{{key:Every episode has a route. Name it, because the route tells you what to change after the antibiotics are finished.}}\n'
   '<div class="tc-scene"><span class="tc-lab">After the second episode &middot; fictional</span><p>An 18-month-old boy on PD has his second '
   '<em>Klebsiella</em> peritonitis in four months. Both times his mother reported loose stools for two days before the effluent turned cloudy, and '
   'his catheter exit sits close to the edge of his diaper.</p><p>You treat the episode, ask the surgeon whether the exit can be relocated at the next '
   'procedure, and teach the family a diaper routine that keeps the exit site above and away from soiling.</p><p class="tc-scene-take"><b>What this '
   'shows.</b> Repeat gram-negative episodes in an infant point to the bowel and the diaper, not only to hand hygiene.</p></div>\n'
   '{{fig:apn22_a}}\n'),
  ('diagnosis', 'Diagnosis', 'Cloudy effluent is peritonitis until proven otherwise',
   '<p><strong>The criteria.</strong> The 2024 international pediatric guideline diagnoses peritonitis when two of three criteria are present: '
   'clinical features (abdominal pain, cloudy effluent, fever); an effluent white blood cell count over 100/mm&sup3; with at least 50% '
   'polymorphonuclear cells after a dwell of at least 2 hours; and a positive effluent culture (an ungraded statement).[[apn22_1]] In a child on '
   'automated PD (APD) without a day dwell, the guideline notes that 50% or more neutrophils suggests peritonitis even when the total count is below '
   '100/mm&sup3;, because the short dwells leave less time for cells to accumulate.[[apn22_1]] The adult ISPD 2022 guideline uses the same '
   'structure.[[apn22_2]]</p>\n'
   '<p><strong>The specimen.</strong> Take the effluent for cell count, Gram stain and culture before the first antibiotic dose, using the culture '
   'method your laboratory has validated. Culture technique matters. In SCOPE, 165 of 620 episodes (27%) were culture-negative; centers varied '
   'widely in their culture techniques, and no single practice separated low-rate from high-rate centers.[[apn22_8]] Worldwide, the culture-negative '
   'proportion ranged from 11% in North America to 67% in Mexico in an international pediatric registry of 501 episodes.[[apn22_10]] The pediatric '
   'guideline sets a benchmark of less than 15% culture-negative episodes; a higher rate is a reason to review sampling and culture '
   'methods.[[apn22_1]]</p>\n'
   '<p><strong>Do not wait for the count.</strong> If the effluent is cloudy and the child has pain or fever, start treatment once the specimen is '
   'taken. The pediatric guideline says empirical antibiotics should begin as soon as possible after appropriate microbiological specimens are '
   'obtained (ungraded).[[apn22_1]]</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Cloudy effluent: cause</th><th>Clue</th><th>What it means</th></tr></thead><tbody>'
   '<tr><td>Infectious peritonitis</td><td>Pain, fever, neutrophils over 50%</td><td>Treat now</td></tr>'
   '<tr><td>Culture-negative peritonitis</td><td>Neutrophils high, culture negative, recent antibiotics</td><td>Treat; review culture '
   'technique</td></tr>'
   '<tr><td>Fibrin or blood</td><td>Strands, pink fluid, no neutrophilia</td><td>Not infection; check for trauma or menstruation in adolescents</td></tr>'
   '<tr><td>Chylous effluent</td><td>Milky, high triglyceride, few cells</td><td>Lymphatic leak, not infection</td></tr>'
   '<tr><td>Eosinophilic effluent</td><td>Eosinophils predominate, early after catheter placement</td><td>Usually benign; still exclude '
   'infection</td></tr></tbody></table></div>\n'
   '{{flow:The 10 p.m. phone call|Is the effluent cloudy, or is there pain or fever?::Any one: treat as possible peritonitis tonight.|Is the child '
   'unwell?::Lethargy, poor perfusion, persistent vomiting, severe pain: emergency room now, intravenous antibiotics for sepsis.|Where can a sample '
   'be taken and antibiotics given within hours?::The PD center if reachable; otherwise the nearest hospital, with you on the phone.|Tell the family '
   'what to bring::The cloudy bag, the home log, transfer set supplies, and the PD booklet.|Speak to the receiving doctor::Specimen first, then '
   'intraperitoneal antibiotics from the ISPD pediatric tables and the formulary; agree who calls you with the count.|Write it down::Time of call, '
   'advice, where the child went, who is following up.}}\n'
   '<p><strong>When the PD center is far.</strong> Most Philippine families on PD live hours from a pediatric PD center, and the hospital nearest '
   'to them may never have treated PD peritonitis. Prepare for this before the first episode. Give each family a sealed &ldquo;peritonitis '
   'packet&rdquo;: a one-page letter to any receiving doctor describing the child, the catheter, the diagnostic criteria, the need for an effluent '
   'specimen before antibiotics, the empirical options in your program&rsquo;s protocol, and your phone number; a copy of the ISPD pediatric '
   'antibiotic table your unit uses; and spare transfer-set supplies. Agree in advance with one hospital near each cluster of families that it will '
   'take the effluent sample and start therapy while you guide by phone.</p>\n'
   '{{key:Cloudy effluent, pain or fever in a child on PD is peritonitis until proven otherwise. Take the specimen and start antibiotics the same '
   'night.}}\n'
   '{{fig:apn22_b}}\n'),
  ('treatment', 'Treatment', 'Empirical treatment, response and the catheter decision',
   '<p><strong>Empirical therapy.</strong> The 2024 pediatric guideline suggests either intraperitoneal cefepime alone, or gram-positive coverage with '
   'a first-generation cephalosporin or vancomycin combined with gram-negative coverage, with ceftazidime preferred and an aminoglycoside where '
   'ceftazidime is unavailable (2D). Children with features of sepsis should receive intravenous antibiotics. Center-specific susceptibility patterns '
   'and the child&rsquo;s history should guide the choice (ungraded).[[apn22_1]] The intraperitoneal route reaches high local concentrations; give '
   'it as the ISPD pediatric tables and your formulary direct, with intermittent or continuous dosing and dwell adjustments for APD as your protocol '
   'sets. Add antifungal prophylaxis with nystatin or fluconazole during the antibiotic course; the guideline suggests this (2D) and favors stopping it '
   'when antibiotics stop.[[apn22_1]]</p>\n'
   '<p><strong>When the culture returns.</strong> Narrow the therapy. In 379 gram-negative episodes in 308 children from 45 centers in the International Pediatric Peritoneal Dialysis Network (IPPN) '
   'registry, 74% responded well to empirical therapy and 82% achieved full functional recovery. Severe abdominal pain at onset and at 60&ndash;72 '
   'hours, <em>Pseudomonas</em>, and in vitro resistance to the empirical antibiotics were associated with failure to recover; monotherapy as '
   'definitive treatment was associated with lower risk, and dual therapy showed no benefit for <em>Pseudomonas</em> after adjustment. Cefazolin '
   'monotherapy for susceptible <em>Enterobacterales</em> gave similar full recovery to ceftazidime or cefepime (91% versus 93%).[[apn22_9]] This is '
   'registry evidence, but it supports de-escalation to the narrowest effective drug.</p>\n'
   '<p><strong>Following the response.</strong> Most children improve within 48&ndash;72 hours: less pain, clearer effluent, a falling cell count. '
   'Repeat the effluent count at day 3 to 5. Persistent severe pain at 60&ndash;72 hours predicted poor recovery in the gram-negative '
   'cohort.[[apn22_9]]</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Category (2024 pediatric guideline)</th><th>Definition</th><th>What it means for the '
   'catheter</th></tr></thead><tbody>'
   '<tr><td>Refractory</td><td>Persistently cloudy effluent or effluent white cells over 100/mm&sup3; after 5 days of appropriate therapy</td><td>Removal '
   'of the catheter suggested (2D)</td></tr>'
   '<tr><td>Relapsing</td><td>Within 4 weeks of finishing therapy, same organism (or one culture-negative episode)</td><td>Removal once controlled '
   'if a tunnel infection persists or after a second relapse (2C)</td></tr>'
   '<tr><td>Recurrent</td><td>Within 4 weeks of finishing therapy, different organism</td><td>Look for a new route; consider the bowel</td></tr>'
   '<tr><td>Repeat</td><td>More than 4 weeks after finishing therapy, same organism</td><td>Look for a reservoir: biofilm, exit site, carrier '
   'state</td></tr>'
   '<tr><td>Fungal</td><td>Fungal elements in effluent</td><td>Immediate catheter removal; antifungal therapy for at least 2 weeks after removal '
   '(both 2D)</td></tr>'
   '<tr><td>Exit-site or tunnel infection with peritonitis, same organism</td><td>Infection along the catheter feeding the peritoneum</td><td>Removal '
   'suggested (2D)</td></tr></tbody></table></div>\n'
   '<p>These definitions come from the pediatric guideline&rsquo;s tables, and the removal statements are weak suggestions on low or very low-quality '
   'evidence.[[apn22_1]] Removal is still the right call when the membrane is at stake. A child who loses the catheter can often return to PD after '
   'a period on hemodialysis (HD); a child who loses the membrane cannot.</p>\n'
   '<p><strong>Special situations.</strong> Polymicrobial growth, especially with anaerobes, raises the possibility of a bowel perforation or an '
   'intra-abdominal source, and needs an early surgical opinion. A culture-negative episode that improves can be completed as the protocol directs; '
   'one that does not improve needs a repeat specimen with attention to culture technique and a search for unusual organisms with the infectious '
   'diseases team. Peritonitis in a child with a recent gastrostomy, colitis or an invasive procedure should prompt a question about the route '
   'before the next procedure is planned.</p>\n'
   '<div class="tc-scene"><span class="tc-lab">Day 4, on the ward &middot; fictional</span><p>A 10-year-old boy treated for <em>Pseudomonas</em> '
   'peritonitis still has severe abdominal pain on day 3, and his effluent count has fallen only from 2,400 to 1,600/mm&sup3;. His exit site is '
   'red with a crust, and the tunnel is tender.</p><p>You discuss catheter removal with the surgeon the same day rather than waiting until day 5, '
   'because the exit site and tunnel are infected with the likely same organism and severe pain at 60&ndash;72 hours predicted poor recovery in the '
   'IPPN cohort.</p><p class="tc-scene-take"><b>What this shows.</b> The day 3 review is a decision point, not a formality.</p></div>\n'
   '<p><strong>After removal.</strong> When the catheter is removed for peritonitis, the child needs a temporary hemodialysis access and a plan. '
   'Many children can return to PD with a new catheter after the infection has cleared, if the membrane recovers; simultaneous removal and '
   'replacement is considered in selected relapsing or exit-site situations once the effluent has cleared, as the pediatric guideline '
   'describes.[[apn22_1]] Fungal peritonitis and repeated severe episodes are the situations most likely to end PD. Discuss the likely course with '
   'the family before surgery, not after.</p>\n'
   '{{key:Reassess at day 3 to 5. Refractory or fungal peritonitis means the catheter comes out, because the goal is to save the membrane, not the '
   'tube.}}\n'),
  ('exitsite', 'Exit site', 'Exit-site and tunnel infection',
   '<p>The exit site is where the catheter crosses skin, and the route by which <em>S. aureus</em> and <em>Pseudomonas</em> travel down the tunnel '
   'to the peritoneum. The 2024 pediatric guideline defines a definite exit-site infection by purulent discharge at the catheter&ndash;skin junction, '
   'with or without a positive culture (2C), and a tunnel infection by inflammation along the subcutaneous segment, with or without fluid on '
   'ultrasound (2C).[[apn22_1]]</p>\n'
   '<p><strong>The score.</strong> The guideline suggests a pediatric exit-site score (2D) that rates five signs from 0 to 2: swelling, crust, redness, '
   'pain on pressure and secretion. A total of 4 or more is treated as infection. The authors note that the score is not validated and its '
   'reproducibility is limited, so it supports clinical judgment rather than replacing it.[[apn22_1]] In SCOPE, an exit-site score above 0 at the '
   'previous month&rsquo;s visit, or no documented review of site care, was associated with more exit-site infection.[[apn22_5]]</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Sign (scored 0 to 2)</th><th>What you look for</th></tr></thead><tbody>'
   '<tr><td>Swelling</td><td>Induration around the exit, along the first part of the tunnel</td></tr>'
   '<tr><td>Crust</td><td>Dried exudate at the exit</td></tr>'
   '<tr><td>Redness</td><td>Erythema and its width around the catheter</td></tr>'
   '<tr><td>Pain on pressure</td><td>Tenderness over the exit or tunnel</td></tr>'
   '<tr><td>Secretion</td><td>Serous or purulent discharge</td></tr></tbody></table></div>\n'
   '<p><strong>How often and how bad.</strong> SCOPE recorded 207 exit-site infections in 124 children, 0.25 per dialysis year, with a median time to '
   'infection of 392 days; 69% involved the exit only, 23% the tunnel only and 8% both. Peritonitis followed in 6%, 24% needed hospitalization and '
   '9% needed catheter removal, usually for tunnel infection.[[apn22_5]] The ISPD 2023 recommendations set an overall exit-site infection target of '
   'no more than 0.40 episodes per year at risk.[[apn22_3]]</p>\n'
   '<p><strong>Treatment.</strong> Empirical oral therapy should cover methicillin-susceptible <em>S. aureus</em>, for example a first-generation '
   'cephalosporin or an antistaphylococcal penicillin (ungraded), continued for 7&ndash;14 days according to response and culture (2D), and for at '
   'least 3 weeks for <em>Pseudomonas</em>, with catheter removal if remission is incomplete (2C).[[apn22_1]] Take a swab before starting. A tunnel '
   'infection that does not settle, or one linked to peritonitis, usually means a new catheter.</p>\n'
   '<p><strong>Prevention.</strong> Exit-site care is taught at training and reviewed at every visit: hand hygiene, a clean dressing as your '
   'protocol directs, and an immobilized catheter so that it does not pull on the exit. The ISPD 2023 update downgraded its recommendation on routine '
   'topical antibiotic cream or ointment at the exit site and clarified its suggestion on covering the exit with a dressing.[[apn22_3]] Follow your '
   'program&rsquo;s protocol on topical agents, and remember that SCOPE linked documented review of site care with fewer infections.[[apn22_5]]</p>\n'
   '<div class="tc-scene"><span class="tc-lab">At the clinic &middot; fictional</span><p>A 12-year-old girl&rsquo;s exit site has a small crust and '
   'slight redness for the second month in a row. Her mother says it &ldquo;always looks like that.&rdquo; The score is 2.</p><p>You review the '
   'dressing technique, check how the catheter is anchored, swab the site, and book a review in two weeks instead of a month. The swab grows '
   '<em>S. aureus</em>; her mother is retrained in exit-site care and the redness settles.</p><p class="tc-scene-take"><b>What this shows.</b> A score '
   'above zero is not an infection yet, but it is a reason to look closer and sooner.</p></div>\n'
   '{{key:Score the exit site at every visit and photograph it. A score above zero is a reason to look closer, and a score of 4 is an '
   'infection.}}\n'
   '{{fig:apn22_c}}\n'),
  ('quality', 'Unit quality', 'Driving the unit&rsquo;s peritonitis rate down',
   '<p><strong>The benchmarks.</strong> The ISPD 2022 guideline sets an overall peritonitis rate of no more than 0.40 episodes per year at risk and '
   'more than 80% of patients peritonitis-free per year.[[apn22_2]] The 2024 pediatric guideline sets ungraded benchmarks of no more than 0.4 '
   'episodes per year, less than 15% culture-negative episodes, and peritonitis within 30 days in fewer than 5% of catheter insertions.[[apn22_1]]</p>\n'
   '<p><strong>Calculating the rate.</strong> Count every episode in the period and divide by the total patient-years at risk (the sum of days each '
   'child was on PD, divided by 365). A program with 14 children on PD for a whole year (14 patient-years) and 6 episodes has a rate of 0.43 per '
   'patient-year. Plot it monthly as a rolling 12-month rate on a run chart; small programs swing widely, so look at the trend, not one month.</p>\n'
   '<p><strong>What lowers it.</strong> SCOPE, a North American quality-improvement collaborative, found an aggregate rate of 0.46 episodes per '
   'patient-year in 734 children; compliance with a standardized follow-up care bundle was associated with fewer episodes (rate ratio 0.49), while an '
   'upward-facing exit site (rate ratio 4.2) and touch contamination (rate ratio 2.22) were associated with more.[[apn22_4]] After touch '
   'contamination, prophylactic antibiotics were associated with less peritonitis (23% versus 38%) in the 2026 SCOPE analysis.[[apn22_7]] The '
   'pediatric guideline considers a single dose of intraperitoneal cefazolin reasonable after wet contamination for most children (the related '
   'statement is 2D).[[apn22_1]] In the IPPN training survey, training under 20 hours was associated with higher peritonitis rates.[[apn22_12]] All of '
   'these are observational associations; the bundle effect is the strongest signal because it was tested inside a structured program.</p>\n'
   '<p><strong>After every episode.</strong> The ISPD 2022 update revised its recommendations on PD training and reassessment.[[apn22_2]] In practice, '
   'every episode should trigger a root-cause review with the family: watch an exchange, inspect the home corner, check the exit site and the bowel '
   'history, and retrain the step that failed. Record the route you think was responsible.</p>\n'
   '{{cards:Root-cause questions after an episode|The connection::Who did the exchange, where, with what light, and was anything dropped or '
   'touched?|The exit site::What was the last score, and was there an exit-site infection with the same organism?|The bowel::Constipation, diarrhea, '
   'a gastrostomy or a recent procedure?|The supplies::A broken bag, a new brand of transfer set, wet storage?|The caregiver::Who is tired, who is '
   'new, and when were they last retrained?|The response::How fast did the family call, and how long until antibiotics started?}}\n'
   '<p>The last question matters in the Philippines more than almost anywhere. Record the hours from cloudy bag to first antibiotic dose for every '
   'episode. If the delay is long, the fix is not only technique; it is the peritonitis packet, the agreement with a nearer hospital, and the '
   'family&rsquo;s confidence that a night call is welcome.</p>\n'
   '<p><strong>Coverage.</strong> The PhilHealth pediatric PD Z package includes outpatient treatment of PD-related peritonitis and exit-site and '
   'peritonitis prevention care.[[apn22_13]] Confirm what applies on the date of service; coverage never decides which antibiotic or route the child '
   'receives.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Measure</th><th>Benchmark</th><th>If you miss it</th></tr></thead><tbody>'
   '<tr><td>Overall peritonitis rate</td><td>No more than 0.40 per patient-year</td><td>Review routes by episode; audit technique and the follow-up '
   'bundle</td></tr>'
   '<tr><td>Peritonitis-free patients</td><td>More than 80% per year</td><td>Find the children with repeated episodes; look for a reservoir</td></tr>'
   '<tr><td>Culture-negative episodes</td><td>Less than 15%</td><td>Review sampling, transport and culture method with the laboratory</td></tr>'
   '<tr><td>Peritonitis within 30 days of insertion</td><td>Fewer than 5% of insertions</td><td>Review insertion technique, early use, exit-site '
   'dressing</td></tr>'
   '<tr><td>Exit-site infection rate</td><td>No more than 0.40 per year at risk</td><td>Review site care, orientation, scoring at every '
   'visit</td></tr></tbody></table></div>\n'
   '<div class="tc-scene"><span class="tc-lab">At the quarterly program meeting &middot; fictional</span><p>The PD nurse presents a rate of 0.71 '
   'episodes per patient-year for the past 12 months. Seven of 10 episodes were in children cared for by grandparents, and four followed a dropped cap '
   'or a touched connection that was never reported.</p><p>You agree on three actions: a touch-contamination hotline with a same-day plan, retraining of '
   'every grandparent caregiver, and an observed exchange at each quarterly review. The rate is plotted monthly.</p><p class="tc-scene-take"><b>What '
   'this shows.</b> A rate is a set of stories. Read the episodes, and the fix is usually visible.</p></div>\n'
   '{{key:Calculate the rate monthly, read every episode for its route, and retrain the step that failed. The rate falls when the program '
   'learns.}}\n'
   '{{call:<ul><li>Cloudy effluent with lethargy, poor perfusion or persistent vomiting (sepsis)</li><li>Fungal elements on the Gram stain or '
   'culture</li><li>Effluent still cloudy or cell count above 100/mm&sup3; after 5 days of therapy</li><li>Polymicrobial or anaerobic growth (possible '
   'bowel perforation)</li><li>Peritonitis with a tunnel infection or with the same organism as an exit-site infection</li></ul>}}\n'),
 ],
 'debrief': [
    '<p><strong>Tonight.</strong> Cloudy effluent with abdominal pain and fever meets at least two of the three criteria before any count is back. '
    'This is peritonitis until proven otherwise, and a dropped cap yesterday suggests touch contamination as the route. Paracetamol and a morning visit '
    'are not safe: delay gives bacteria hours to multiply and the membrane hours of inflammation. Tell Jenny that Kyla needs a sample taken and '
    'antibiotics started tonight, ask her to bring the cloudy bag, the home log and her PD supplies, and stay on the phone until there is a plan.</p>\n',
    '<p><strong>Where.</strong> Kyla is alert and drinking, so she does not need a resuscitation bay, but she does need treatment within hours. The '
    'district hospital 15 minutes away is the right place tonight if you support it. Call the resident yourself: take effluent for cell count, Gram '
    'stain and culture before antibiotics; give empirical intraperitoneal antibiotics as the 2024 pediatric guideline suggests, with doses from the '
    'ISPD pediatric tables you send and the hospital formulary; add antifungal prophylaxis; give intravenous antibiotics if she shows signs of sepsis; '
    'and call you with the count and the Gram stain. Arrange transfer to the PD center the next morning for follow-up, or sooner if she worsens.</p>\n',
    '<p><strong>Afterward.</strong> Narrow the antibiotics when the culture returns, repeat the count at day 3 to 5, and remove the catheter if the '
    'peritonitis is refractory or fungal. Then retrain: observe Jenny&rsquo;s full exchange, teach what to do when a cap falls (report it the same day '
    'so the team can decide on prophylaxis), and check the exit site and bowel history. For the program, record the episode, its route and its outcome, '
    'update the rolling 12-month rate, and look for a pattern across families.</p>\n'],
 'skills': {'title': 'PD peritonitis and exit-site and tunnel infection',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Applies the 2024 pediatric criteria to a cloudy effluent case and orders specimens before antibiotics', False),
                      ('Gives a remote hospital a complete telephone plan for empirical intraperitoneal therapy using the unit formulary', False),
                      ('Scores an exit site and decides between observation, oral therapy and catheter review', False),
                      ('Calculates a program peritonitis rate per patient-year and presents it on a run chart', False)],
            'placement': 'Pediatric PD unit, telephone simulation or program quality meeting'},
 'quiz': [
    ('Which combination meets the 2024 pediatric criteria for PD peritonitis?',
     ['Fever alone',
      'Cloudy effluent with abdominal pain, plus effluent white cells over 100/mm&sup3; with at least 50% neutrophils after a 2-hour dwell',
      'A positive blood culture alone',
      'Exit-site redness with a score of 2'],
     1,
     'Two of three criteria are needed: clinical features, the effluent cell count and differential after an adequate dwell, and a positive culture.'),
    ('A child on CAPD has cloudy effluent at night. When should empirical antibiotics start?',
     ['After the culture result',
      'The next morning at the PD center',
      'As soon as effluent specimens are taken',
      'Only if the cell count exceeds 500/mm&sup3;'],
     2,
     'The pediatric guideline states antibiotics should begin as soon as possible after appropriate microbiological specimens are obtained.'),
    ('Fungal elements are seen in the effluent of a child on PD. What does the 2024 pediatric guideline suggest?',
     ['Immediate catheter removal and antifungal therapy for at least 2 weeks after removal',
      'Intraperitoneal antifungal therapy with the catheter left in place',
      'Repeat the culture in one week',
      'Add vancomycin'],
     0,
     'Fungal peritonitis threatens the membrane; removal is suggested at once (2D).'),
    ('A program has 6 peritonitis episodes in 14 patient-years. Which statement is correct?',
     ['The rate is 2.3 per patient-year',
      'The rate cannot be calculated without culture results',
      'The rate meets the 0.40 benchmark',
      'The rate is about 0.43 per patient-year, above the 0.40 benchmark'],
     3,
     'Episodes divided by patient-years at risk: 6 / 14 = 0.43.'),
    ('In the SCOPE collaborative, which factor was associated with a lower peritonitis rate?',
     ['An upward-facing exit site',
      'Compliance with a standardized follow-up care bundle',
      'Touch contamination',
      'Age 2 years or younger'],
     1,
     'Bundle compliance had a rate ratio of 0.49; upward exit sites and touch contamination were associated with more peritonitis. The data are observational.'),
 ],
 'terms': [('APD', 'Automated peritoneal dialysis'),
           ('CAPD', 'Continuous ambulatory peritoneal dialysis'),
           ('HD', 'Hemodialysis'),
           ('IPPN', 'International Pediatric Peritoneal Dialysis Network'),
           ('ISPD', 'International Society for Peritoneal Dialysis'),
           ('PD', 'Peritoneal dialysis'),
           ('SCOPE', 'Standardizing Care to Improve Outcomes in Pediatric End Stage Kidney Disease (collaborative)')],
 'readings': [('dialysis-access-infection.html', 'When the Access Gets Infected'),
              ('antibiotic-stewardship-dialysis.html', 'Antibiotic Stewardship in Hemodialysis: Using Antibiotics Wisely'),
              ('peritoneal-dialysis-ckd.html', 'Peritoneal Dialysis: Your Complete Guide')],
 'calcs': ['calc-dialysis-qapi-scorecard.html', 'calc-bsa.html', 'calc-pd-adequacy.html'],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
