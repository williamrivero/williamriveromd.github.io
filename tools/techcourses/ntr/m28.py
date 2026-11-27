# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 28: PD peritonitis, catheter and mechanical complications.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, for Philippine practice.
ISPD 2022 peritonitis and ISPD 2023 catheter-related infection statements and grades checked against the guideline texts; PDOPPS and the
urgent-start Cochrane review against PubMed abstracts. No antibiotic doses or regimens. Every case is fictional."""

MODULE = {
 'image_alt': 'A resident holds a cloudy peritoneal dialysis effluent bag against a printed page of text in the emergency room while a fellow '
              'examines the catheter exit site of a patient lying on a stretcher, in a Philippine provincial hospital.',
 'objectives': [
  '<strong>Intern:</strong> Recognize a cloudy bag, abdominal pain or a red, crusted exit site in a peritoneal dialysis (PD) patient as urgent, keep the '
  'bag, and report at once.',
  '<strong>Resident:</strong> Diagnose peritonitis with the International Society for Peritoneal Dialysis (ISPD) 2022 criteria, send effluent correctly '
  'before the first antibiotic, start the unit protocol with the fellow, and recognize exit-site and tunnel infection.',
  '<strong>Fellow:</strong> Follow the response day by day, decide on catheter removal in refractory, relapsing, fungal and catheter-related infection, '
  'manage leaks, hernias and drainage failure, and lead prevention and the unit&rsquo;s infection audit.',
 ],
 'big': """<div class="tc-keyp"><span class="tc-lab">Your role &middot; the first doctor who sees the bag</span>A PD patient with a cloudy bag
usually reaches an emergency room or a ward before the PD unit. The intern recognizes it, keeps the bag and calls. The resident sends the
effluent properly, starts the protocol within the hour with the fellow, and does not let the patient wait for a consult the next morning. The
fellow follows the effluent count every day, decides when the catheter must come out, and asks how the infection got in.</div>
{{plain:Think of the PD catheter as a door into a clean room. The room is the peritoneal cavity, which is sterile and has almost no guards of its
own once fluid fills it. Germs come in through the door when hands touch the connection, along the outside of the door frame when the exit site
is infected, or through the wall from a sick bowel next door.}}
<p>The picture has a limit. The peritoneum is not an empty room: it is lined by living cells and blood vessels that respond to infection by
pouring white cells and protein into the fluid, which is why the bag turns cloudy. That same inflammation makes the membrane leakier, so glucose
is absorbed faster, ultrafiltration falls and the patient may gain fluid during the infection. And repeated or prolonged infection scars the
membrane. Peritonitis is therefore an emergency for the patient and also for the membrane: each episode treated late or incompletely can end PD.</p>
{{cards:Key numbers|Diagnosis (ISPD 2022)::At least two of: pain and/or cloudy effluent; effluent white cells above 100/&micro;L after a dwell of at least 2 hours, with more than 50% neutrophils; positive culture (1C)|Unit peritonitis rate (ISPD 2022)::No more than 0.40 episodes per year at risk. Peritonitis-free: more than 80% of patients per year (2C)|Culture-negative episodes (ISPD 2022)::Less than 15% of all episodes (1C)|Refractory peritonitis::Effluent not clear after 5 days of appropriate antibiotics: remove the catheter (1D)|Exit-site infection rate (ISPD 2023)::No more than 0.40 episodes per year at risk (2C)|PDOPPS, 7,051 patients in 7 countries::Crude rate 0.28 episodes per patient-year; Thailand 0.40, with more gram-negative and culture-negative episodes}}
<p>Most peritonitis episodes are caused by skin bacteria introduced during an exchange and settle with prompt intraperitoneal antibiotics. A few
come from the bowel, a fungus or an infected tunnel, and these fail unless the source is found and the catheter removed in time. Your work is to
start treatment within the hour, follow the effluent count every day, and know the day on which waiting becomes harm.</p>
""",
 'case': {'title': 'The cloudy bag from Ubay',
  'html': """<p>It is 7 a.m. at a provincial hospital in Tagbilaran City, Bohol. Mr. Dionisio Loquias, 58, a fisherman from Ubay, has done CAPD for
two years. He traveled two hours by motorcycle and bus with his wife, carrying this morning&rsquo;s drained bag, which is cloudy enough that newsprint
behind it cannot be read. Abdominal pain began yesterday afternoon. His temperature is 38.2&deg;C, blood pressure 108/68 mm Hg, and his abdomen is
diffusely tender with rebound.</p>
<p>His wife says they do the exchanges in the bedroom, where the cat sleeps, and wash hands with water from a covered drum because the piped water
is unreliable. A week ago the exit site was red with a yellow crust; they cleaned it but did not call. Today there is redness 1.5 cm around the exit
and a little pus on pressure, and the tunnel is not tender. He has had no diarrhea; his last bowel movement was two days ago.</p>
<p>The effluent count from the bag he brought is 1,850 white cells/&micro;L with 88% neutrophils. The Gram stain shows gram-positive cocci in
clusters. The fellow is on the way from the PD unit and asks you, the resident, to act.</p>""",
  'questions': ['Does Mr. Loquias have peritonitis by ISPD criteria, and what must happen before and within the first hour?',
                'What is the likely source, and how does the exit site change the plan and the risk of losing the catheter?',
                'How will you follow his response, when would the catheter come out, and what will you change at home?']},
 'sections': [
  ('peritonitis', 'Diagnosis', 'Peritonitis: diagnosis and the first hour', """
<p>Bacteria reach the peritoneal cavity by four routes. <strong>Touch contamination</strong> during an exchange brings skin bacteria such as
coagulase-negative staphylococci. <strong>Catheter-related</strong> infection spreads from an infected exit site or tunnel along the catheter,
classically <em>Staphylococcus aureus</em> or <em>Pseudomonas</em>. <strong>Enteric</strong> infection crosses the bowel wall in constipation,
diverticular disease, colitis or perforation, bringing gram-negative bacteria and anaerobes. Less often, bacteria arrive through the blood or the
genital tract. The route predicts the microbe, the response and whether the catheter will survive.</p>
<p>The ISPD 2022 recommendations diagnose peritonitis when at least two of the following are present: clinical features consistent with
peritonitis, meaning abdominal pain and/or cloudy effluent; an effluent white cell count above 100/&micro;L (0.1 &times; 10&#8313;/L) after a dwell of at
least 2 hours, with more than 50% polymorphonuclear neutrophils; and a positive effluent culture (1C).[[ntr28_1]] They recommend that a PD patient
presenting with cloudy effluent be presumed to have peritonitis and treated as such until the diagnosis is confirmed or excluded (1C).[[ntr28_1]]
The dwell time matters: in a patient on automated PD with short night dwells, the count may be lower, and a neutrophil proportion above 50% is strong
evidence of peritonitis even when the count is under 100.</p>
<div class="table-wrap"><table><thead><tr><th>Cloudy effluent that is not bacterial peritonitis</th><th>Clue</th></tr></thead><tbody>
<tr><td>Specimen from a dry or nearly dry abdomen</td><td>High count from a small volume; repeat after a proper dwell</td></tr>
<tr><td>Eosinophilic peritonitis</td><td>Early after catheter insertion; eosinophils on the differential</td></tr>
<tr><td>Chylous effluent</td><td>Milky, high triglycerides, low white cells; some calcium channel blockers cause cloudy effluent without infection</td></tr>
<tr><td>Hemoperitoneum</td><td>Pink or red effluent; menstruation, ovulation, procedures</td></tr>
<tr><td>Malignancy</td><td>Atypical cells; persistent cloudiness without response</td></tr>
</tbody></table></div>
<p><strong>Culture well.</strong> ISPD recommends blood culture bottles as the preferred technique for culturing PD effluent (1C), and that a unit&rsquo;s
culture-negative episodes stay below 15% of all episodes (1C).[[ntr28_1]] A high culture-negative rate usually means poor technique or antibiotics
given before sampling, and it leaves the team treating blind. In the Peritoneal Dialysis Outcomes and Practice Patterns Study (PDOPPS) of 7,051
patients in seven countries, Thailand, the participating country closest to Philippine conditions, had a peritonitis rate of 0.40 episodes per
patient-year with more gram-negative and culture-negative episodes than the other countries.[[ntr28_4]]</p>
<p><strong>Treat at once.</strong> ISPD recommends empirical antibiotic regimens that are center-specific (doses and any adjustment by creatinine clearance (CrCl) or residual function come from the unit protocol) and cover both gram-positive and gram-negative
bacteria (1C), with gram-positive bacteria covered by a first-generation cephalosporin or vancomycin (1B), and the intraperitoneal route preferred
when compatibility and stability allow (1B). It also recommends co-prescribing antifungal prophylaxis whenever a PD patient receives an antibiotic
course (1B).[[ntr28_1]] The drugs, doses, dwell instructions and mixing come from your unit&rsquo;s protocol and the attending; do not write them from
memory.</p>
{{flow:The first hour with a cloudy bag|Keep the bag::Do not discard the drained bag; it is the best specimen.|Examine::Temperature, blood pressure, abdomen, exit site and tunnel; ask about pain, diarrhea, constipation, contamination and recent procedures.|Send before antibiotics::Effluent cell count and differential, Gram stain, culture in blood culture bottles per protocol; blood cultures if septic.|Start the protocol::Empirical intraperitoneal antibiotics covering gram-positive and gram-negative bacteria, and antifungal prophylaxis, per the unit protocol, after calling the fellow.|Look for a surgical abdomen::Severe or localized pain, multiple enteric bacteria or anaerobes, free air, hypotension: call surgery.|Record the baseline::Effluent count, weight, drain volumes, glucose and potassium.}}
<p><strong>What you do at your stage.</strong> The intern keeps the bag and calls. The resident sends effluent before the first antibiotic and starts
the protocol within the hour with the fellow, without waiting for the culture. The fellow chooses the empirical regimen from the unit&rsquo;s own
microbiology and adjusts when the culture returns.</p>
{{key:Cloudy effluent is peritonitis until proven otherwise. Keep the bag, culture it in blood culture bottles, and start the protocol within the
hour.}}
{{fig:ntr28_a}}
"""),
  ('refractory', 'Response and removal', 'Following the response: refractory, relapsing and fungal peritonitis', """
<p>Most episodes improve within 48 to 72 hours: the pain settles, the bag clears and the effluent count falls. The count is the best daily
measure. A count that does not fall by day 3 or 5 means the antibiotic is wrong, the source is still there, or the bacteria live on the catheter
in a biofilm that antibiotics cannot reach. That last possibility is why the catheter itself sometimes has to go.</p>
<p>ISPD 2022 recommends removing the PD catheter in refractory peritonitis, defined as failure of the effluent to clear after 5 days of appropriate
antibiotics (1D). It now also suggests that observation for antibiotic effect longer than 5 days is appropriate when the effluent white cell count is
falling toward normal, rather than mandatory removal on day 5 (2C).[[ntr28_1]] The timing still matters. Peritonitis that drags on injures the membrane
and raises the risk of death; a catheter removed on time can often be replaced later and PD resumed.</p>
<div class="table-wrap"><table><thead><tr><th>Term (ISPD 2022)</th><th>Definition</th><th>What it suggests</th></tr></thead><tbody>
<tr><td>Refractory</td><td>Effluent not clear after 5 days of appropriate antibiotics</td><td>Biofilm, wrong drug, surgical source; catheter removal (1D)</td></tr>
<tr><td>Relapsing</td><td>A new episode within 4 weeks of finishing therapy, with the same bacterium or culture-negative</td><td>Biofilm on the catheter; consider timely removal (1C)</td></tr>
<tr><td>Recurrent</td><td>A new episode within 4 weeks of finishing therapy, with a different bacterium</td><td>Ongoing technique or source problem; consider timely removal (1C)</td></tr>
<tr><td>Repeat</td><td>A new episode more than 4 weeks after finishing therapy, with the same bacterium</td><td>Biofilm or reservoir; consider timely removal (1C)</td></tr>
<tr><td>Fungal</td><td>Fungi identified in the effluent</td><td>Immediate catheter removal (1C)</td></tr>
</tbody></table></div>
<p>For fungal peritonitis ISPD recommends immediate catheter removal (1C), with antifungal treatment continued for at least 2 weeks after removal (2C).
For relapsing, recurrent or repeat episodes it recommends that timely removal be considered (1C), and suggests that simultaneous removal and reinsertion
be considered once the effluent culture has become negative (2C).[[ntr28_1]] The guideline sets treatment durations by microbe; for example it suggests
about 2 weeks for coagulase-negative staphylococci and streptococci and 3 weeks for <em>Staphylococcus aureus</em> (2C), and for <em>Pseudomonas</em>
3 weeks with two antibiotics of different mechanisms (2C).[[ntr28_1]] Drug choice and dose stay with the protocol and the attending.</p>
<p><strong>Enteric clues.</strong> Several enteric bacteria in one culture, especially with anaerobes, suggest a hole in the bowel rather than a
contaminated exchange, and need a surgeon&rsquo;s opinion. ISPD 2022 also suggests that avoiding or limiting histamine-2 receptor antagonists may help
prevent enteric peritonitis (2C), and that avoiding and treating hypokalemia may reduce peritonitis risk (2C).[[ntr28_1]]</p>
<p><strong>The membrane during peritonitis.</strong> Inflammation makes the membrane transport faster, so glucose is absorbed early and ultrafiltration
falls. Patients gain fluid during an episode, and their usual prescription may stop working for a while. Watch weight and drain volumes, and adjust
with the PD nurse.</p>
<p><strong>What you do at your stage.</strong> The resident charts the effluent count every day on a single line so the trend is obvious. The fellow
names the day by which the effluent must be clear, discusses removal early with the attending and the surgeon in a non-responder, and arranges
temporary hemodialysis access before it is needed.</p>
{{key:Follow the effluent count every day and name the decision day in advance. A catheter removed on time can often be replaced; a membrane lost
to a long infection cannot.}}
<div class="tc-keyp"><span class="tc-lab">In children</span>Children have a separate ISPD guideline for PD-associated infections (2024 update), which scales
treatment to body size and addresses infants, whose catheters and exit sites behave differently.[[ntr28_7]] A child with a cloudy bag needs the pediatric
nephrologist the same hour. Read <a href="attending-pediatric-nephrologist-22-pd-peritonitis.html">Attending Pediatric Nephrologist, Module 22</a>.</div>
"""),
  ('exit-site', 'Exit site and tunnel', 'Exit-site and tunnel infection', """
<p>The exit site is a permanent wound where the catheter leaves the skin. Below it, a superficial cuff in the tunnel and a deep cuff near the
peritoneum are meant to be sealed in by scar tissue. Bacteria colonizing the exit can track inward along the catheter, past the superficial cuff
to the tunnel, and finally into the peritoneum. That is why an exit-site infection is not a skin problem: it is the first step toward catheter-related
peritonitis and catheter loss.</p>
<p>The ISPD 2023 catheter-related infection recommendations define exit-site infection as purulent discharge, with or without erythema of the skin
at the catheter-epidermal interface, and tunnel infection as clinical inflammation such as erythema, swelling, tenderness or induration along the
tunnel (both not graded). They set a unit exit-site infection rate of no more than 0.40 episodes per year at risk (2C).[[ntr28_2]] Redness alone,
without pus, may be irritation or early infection; the exit site is watched and swabbed if discharge appears. Ultrasound can help show tunnel
involvement.[[ntr28_2]]</p>
<div class="table-wrap"><table><thead><tr><th>Finding</th><th>Likely meaning</th><th>Recommendation (ISPD 2023)</th></tr></thead><tbody>
<tr><td>Pus at the exit, with or without redness</td><td>Exit-site infection</td><td>Culture; empiric oral antibiotics with <em>S. aureus</em> coverage (1C)</td></tr>
<tr><td><em>Pseudomonas</em> grown from the exit</td><td>Hard to eradicate; biofilm</td><td>At least 3 weeks of effective antibiotics (1C)</td></tr>
<tr><td>Tenderness, swelling or induration along the tunnel</td><td>Tunnel infection</td><td>Ultrasound may help; often ends in catheter intervention</td></tr>
<tr><td>Exit or tunnel infection followed by peritonitis with the same bacterium</td><td>Catheter-related peritonitis</td><td>Catheter removal (2C)</td></tr>
<tr><td>Catheter needs replacing for infection</td><td>Source control</td><td>Simultaneous removal and reinsertion with a new exit site under antibiotic cover may be considered (2C)</td></tr>
</tbody></table></div>
<p>Prevention is graded more strongly than treatment. ISPD 2023 recommends prophylactic antibiotics immediately before catheter insertion to prevent
peritonitis (1A), daily topical antibiotic cream or ointment at the exit site (1C, downgraded from the 2017 grade of 1A), and nasal antibiotic
prophylaxis for patients identified as nasal <em>S. aureus</em> carriers (1C).[[ntr28_2]] In PDOPPS, facilities that gave antibiotics at catheter
insertion had a lower peritonitis rate (rate ratio 0.83), an observational association that fits the recommendation.[[ntr28_4]]</p>
<p><strong>What you do at your stage.</strong> The intern looks at the exit site of every PD patient admitted for any reason, and describes it in
words. The resident swabs discharge before antibiotics and feels the tunnel. The fellow treats exit-site infection as a threat to the catheter,
follows it to cure, and decides with the surgeon on catheter intervention when the tunnel is involved.</p>
{{key:Pus at the exit site is an infection on its way to the peritoneum. Culture it, treat it, follow it to cure, and look at the tunnel.}}
{{fig:ntr28_b}}
"""),
  ('mechanical', 'Mechanical problems', 'Leaks, hernias and drainage failure', """
<p>Every exchange raises the pressure inside the abdomen. Fluid looks for the weakest point: a fresh catheter incision, an old hernia, a patent
processus vaginalis, or a defect in the diaphragm. The catheter itself depends on its tip sitting deep in the pelvis and on side holes not blocked by
bowel, omentum or fibrin. Mechanical problems therefore cluster in the first weeks after insertion and in patients with high fill volumes, but they
can appear at any time.</p>
<div class="table-wrap"><table><thead><tr><th>Problem</th><th>Mechanism</th><th>What you see</th><th>What usually helps</th></tr></thead><tbody>
<tr><td>Outflow failure</td><td>Constipation pushing bowel on the catheter, tip migration, omental wrap, fibrin</td><td>Inflow fine, outflow slow or positional; drain smaller than fill</td><td>Treat constipation first; radiograph for tip position; fibrin per protocol; repositioning by surgeon or radiologist</td></tr>
<tr><td>Pericatheter leak</td><td>Fluid tracks along an unhealed tunnel</td><td>Wet dressing, fluid at the exit, positive glucose on the fluid</td><td>Lower volumes, supine dwells or a pause in PD per protocol; risk of infection</td></tr>
<tr><td>Abdominal wall or genital leak</td><td>Fluid escapes into the wall or along a patent processus vaginalis</td><td>Swelling of the abdominal wall, scrotum or labia; falling drain volume</td><td>Imaging to find the path; surgical repair if persistent</td></tr>
<tr><td>Hernia</td><td>Raised pressure on a weak point</td><td>Bulge at the umbilicus, groin or incision</td><td>Surgical repair; watch for incarceration</td></tr>
<tr><td>Pleuroperitoneal leak (hydrothorax)</td><td>Defect in the diaphragm, usually right-sided</td><td>Breathlessness, right pleural effusion high in glucose</td><td>Stop PD and arrange hemodialysis while the attending and surgeon decide</td></tr>
<tr><td>Inflow or outflow pain</td><td>Catheter tip against the pelvis, jet effect, acidic solution</td><td>Pain at the start or end of an exchange</td><td>Check tip position; discuss solution and flow with the PD nurse</td></tr>
</tbody></table></div>
<p>The ISPD 2019 recommendations on creating and maintaining PD access describe these complications and their management, from correct catheter
placement and exit-site location to repositioning and repair, and emphasize that bowel function and catheter position are the first things to check
when drainage fails.[[ntr28_3]] Urgent-start PD trades early use for more leaks: in a Cochrane review, urgent start may increase dialysate leaks (risk
ratio 3.90; about 210 more per 1,000 patients), with low-certainty evidence.[[ntr28_5]]</p>
{{call:Stop and call the attending nephrologist, per unit protocol, but always ask the attending nephrologist for guidance, when:<ul><li>A PD
patient has cloudy effluent, abdominal pain or fever: start the first-hour steps while you call.</li><li>The patient is hypotensive, septic or has
a rigid abdomen, or the culture grows several enteric bacteria or fungi.</li><li>The effluent is not clearing by day 3 to 5 of treatment.</li><li>There
is pus with tunnel tenderness, or an exit-site infection is followed by peritonitis.</li><li>A PD patient becomes breathless with a new effusion, or
the scrotum, labia or abdominal wall swells.</li><li>The catheter will not drain and fluid cannot be removed.</li></ul>}}
<p><strong>What you do at your stage.</strong> The intern reports a wet dressing, a new bulge or a swollen scrotum. The resident works out whether a
drainage problem is inflow or outflow, positional or constant, and treats constipation before calling it a catheter failure. The fellow decides with
the surgeon on imaging, repositioning or repair, and arranges temporary hemodialysis when PD must pause.</p>
{{key:When drainage fails, check the bowel, the tip and the path of the fluid before you blame the catheter. When the chest fills with
dialysate, stop PD.}}
"""),
  ('prevention', 'Prevention', 'Prevention at home and in the unit', """
<p>Peritonitis is a quality measure for the whole PD program, not only for one patient. The ISPD 2022 recommendations set a target overall rate of
no more than 0.40 episodes per year at risk and suggest that units track the percentage of patients free of peritonitis, aiming for more than 80%
per year (2C).[[ntr28_1]] In PDOPPS, facility rates varied widely within each country, and 10% of facilities exceeded 0.50 episodes per patient-year.
Facilities with training of 6 days or more had a lower peritonitis rate than those with shorter training (rate ratio 0.81), an observational finding.[[ntr28_4]]</p>
<div class="table-wrap"><table><thead><tr><th>Risk at home</th><th>Why it matters</th><th>ISPD 2022 position</th></tr></thead><tbody>
<tr><td>Technique drifts over time</td><td>Touch contamination at connection</td><td>Regular reassessment and retraining of exchange technique (1C)</td></tr>
<tr><td>Cats, dogs and birds in the exchange room</td><td>Animals carry bacteria; some have caused peritonitis by chewing tubing</td><td>Extra precautions if pets are kept (1C); no pets in the exchange room (2A)</td></tr>
<tr><td>Wet contamination (open system or broken connection)</td><td>Bacteria enter with the fluid</td><td>Seek advice from the team at once (not graded); prophylactic antibiotics after wet contamination (2D)</td></tr>
<tr><td>Hypokalemia</td><td>Associated with bowel dysmotility and enteric peritonitis</td><td>Avoid and treat hypokalemia (2C)</td></tr>
<tr><td>Histamine-2 receptor antagonists</td><td>Reduced gastric acid barrier to bowel bacteria</td><td>Avoid or limit their use (2C)</td></tr>
</tbody></table></div>
<p><strong>Philippine practice.</strong> Many homes store water in drums or pails, share one bedroom among several family members, keep cats and
chickens, and lose power and piped water during typhoons. A home visit by the PD nurse shows the team what training in a hospital room cannot: where
the exchange happens, how hands are washed and dried, and where the bags are stored. PhilHealth&rsquo;s Z Benefits package for PD (Circular 2024-0036)
supports PD at accredited providers; confirm on the date of service what it covers for training, home visits and complications such as peritonitis
admissions, rather than quoting amounts.[[ntr28_6]] Distance is a risk of its own: a patient two hours from the hospital needs a written plan for what
to do with a cloudy bag, including whom to call and which bag to bring.</p>
<p><strong>What you do at your stage.</strong> The resident asks every PD patient with peritonitis how the exchange is done at home, step by step,
and reports what may have gone wrong without blame. The fellow presents each episode at the unit&rsquo;s infection review: the microbe, the likely route,
the outcome and the change made, and tracks the unit&rsquo;s rate and culture-negative proportion against the ISPD targets.</p>
{{key:Every peritonitis episode is a question about the route in. Find it, fix it at home, and count it in the unit&rsquo;s rate.}}
"""),
 ],
 'debrief': [
  """<p><strong>Diagnosis and the first hour.</strong> Mr. Loquias meets all three ISPD criteria: pain with a cloudy bag, an effluent count of 1,850/&micro;L
with 88% neutrophils, and a Gram stain that will very likely become a positive culture. Keep the bag, send cell count, Gram stain and culture in blood
culture bottles, and take blood cultures because he is febrile and his pressure is soft. Then start the unit&rsquo;s empirical intraperitoneal regimen
covering gram-positive and gram-negative bacteria, with antifungal prophylaxis, within the hour and with the fellow on the phone. Rebound tenderness
calls for a careful look for a surgical abdomen, though the Gram stain points to skin bacteria.</p>""",
  """<p><strong>The source.</strong> Gram-positive cocci in clusters with an exit site that has been red, crusted and now discharges pus point to
<em>Staphylococcus aureus</em> spreading from the exit site, a catheter-related peritonitis. Culture the exit-site pus. If the exit site and the
effluent grow the same bacterium, ISPD suggests catheter removal (2C), and an exit-site infection with tunnel involvement makes cure without removal
unlikely. Plan for temporary hemodialysis access now, so that removal, if needed, does not happen in a crisis.</p>""",
  """<p><strong>Follow-up and home.</strong> Chart the effluent count daily and set day 5 as the decision day with the attending: if it is not
clearing, the catheter comes out (1D), unless it is clearly falling toward normal (2C). Treat for the duration the protocol sets for the final
microbe. At home, the PD nurse should visit: keep the cat out of the exchange room (2A), review hand washing with stored water, retrain technique
(1C), and teach daily exit-site care with the topical agent the unit uses. Write a cloudy-bag plan for the trip from Ubay, and check his potassium and
bowels.</p>""",
 ],
 'skills': {'title': 'PD peritonitis, catheter and mechanical complications',
            'intro': 'Complete with a preceptor in a PD unit, emergency room or ward. Sign-off is local.',
            'items': [('Applies the ISPD 2022 diagnostic criteria to a cloudy bag and sends effluent correctly before antibiotics', False),
                      ('Starts the unit&rsquo;s peritonitis protocol with the fellow within the hour, including antifungal prophylaxis', False),
                      ('Examines and describes a PD exit site and tunnel and recognizes exit-site and tunnel infection', False),
                      ('Charts the daily effluent count and states the decision day for catheter removal', False),
                      ('Separates inflow, outflow, positional and leak problems in a catheter that drains poorly', False),
                      ('Takes a step-by-step history of the home exchange and identifies a likely route of infection', False)],
            'placement': 'Supervised PD unit, emergency room or ward rotation'},
 'quiz': [
  ('An intern sees a PD patient in the emergency room whose drained bag is cloudy. The patient has mild abdominal discomfort. What should the intern do first?',
   ['Discard the bag and ask the patient to do a fresh exchange tomorrow',
    'Keep the bag and report to the resident at once, because cloudy effluent is presumed peritonitis',
    'Give oral antibiotics and send the patient home',
    'Wait for the PD unit to open'],
   1,
   'ISPD 2022 recommends presuming peritonitis with cloudy effluent (1C). The drained bag is the best specimen; discarding it or waiting delays diagnosis '
   'and treatment.'),
  ('A resident evaluates a CAPD patient with abdominal pain. The effluent after a 4-hour dwell has 650 white cells/&micro;L with 80% neutrophils; the culture is pending. Which statement is correct?',
   ['Peritonitis cannot be diagnosed until the culture is positive',
    'Two ISPD criteria are met (pain and a count above 100/&micro;L with more than 50% neutrophils), so this is peritonitis and treatment should start now',
    'The count must exceed 1,000/&micro;L',
    'The neutrophil proportion is irrelevant'],
   1,
   'ISPD 2022 requires at least two of three criteria (1C). Pain plus the cell criterion is enough; waiting for culture delays treatment.'),
  ('A fellow follows a patient on day 5 of appropriate antibiotics. The effluent count was 2,400, 2,100, 1,900, 1,950 and 1,800/&micro;L on days 1 to 5, and the bag is still cloudy. What does ISPD 2022 recommend?',
   ['Continue for another 2 weeks and reassess',
    'Remove the catheter, because this is refractory peritonitis without a clear fall toward normal (1D)',
    'Add a third antibiotic and keep the catheter indefinitely',
    'Switch to automated PD'],
   1,
   'Refractory peritonitis is failure to clear after 5 days of appropriate antibiotics, and removal is recommended (1D). Longer observation is suggested only '
   'when the count is falling toward normal (2C), which this nearly flat curve is not.'),
  ('A CAPD patient&rsquo;s effluent culture grows <em>Candida</em>. What is the recommended action?',
   ['Intraperitoneal antifungal through the catheter for 2 weeks, keeping the catheter',
    'Immediate catheter removal, with antifungal treatment continued for at least 2 weeks after removal',
    'Repeat the culture in a week',
    'Topical antifungal at the exit site'],
   1,
   'ISPD 2022 recommends immediate removal in fungal peritonitis (1C) and antifungal treatment for at least 2 weeks after removal (2C). Fungi persist on the '
   'catheter; keeping it risks death and loss of the membrane.'),
  ('A patient on PD for one month develops right-sided breathlessness. A chest radiograph shows a large right pleural effusion, and the fluid glucose is very high. What is the most likely problem and first step?',
   ['Heart failure; increase the glucose strength of the bags',
    'Pleuroperitoneal leak; stop PD, arrange hemodialysis and call the attending and surgeon',
    'Pneumonia; continue PD and start antibiotics',
    'Peritonitis; send effluent culture only'],
   1,
   'A right effusion with high glucose in a PD patient suggests dialysate crossing a diaphragmatic defect. Continuing PD, or raising the glucose and fill, worsens '
   'it; PD is paused while the team decides on repair.'),
 ],
 'terms': [('PD', 'Peritoneal dialysis'), ('CAPD', 'Continuous ambulatory peritoneal dialysis'),
           ('ISPD', 'International Society for Peritoneal Dialysis'),
           ('PDOPPS', 'Peritoneal Dialysis Outcomes and Practice Patterns Study'), ('S. aureus', 'Staphylococcus aureus')],
 'readings': [('attending-nephrologist-18-pd-peritonitis.html', 'Attending Nephrologist, Module 18: PD peritonitis'),
              ('peritoneal-dialysis-nurse-07-infection-and-peritonitis.html', 'Peritoneal Dialysis Nurse, Module 7: Infection and peritonitis'),
              ('peritoneal-dialysis-nurse-08-mechanical-and-urgent-problems.html', 'Peritoneal Dialysis Nurse, Module 8: Mechanical and urgent problems'),
              ('peritoneal-dialysis-nurse-03-access-and-exit-site-care.html', 'Peritoneal Dialysis Nurse, Module 3: Access and exit-site care')],
 'calcs': ['calc-pd-adequacy.html', 'calc-pd-glucose-absorption.html', 'calc-sirs-sepsis.html', 'calc-renal-abx-dosing.html'],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
