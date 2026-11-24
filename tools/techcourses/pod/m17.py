# -*- coding: utf-8 -*-
"""Physician on Duty, Module 17: The Shivering Patient (fever and bloodstream infection).
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty preparing blood culture bottles beside a shivering dialysis patient with a neck catheter, while a nurse checks her temperature.",
    "objectives": [
        "Explain how bacteria reach the blood through a dialysis catheter, and why dialysis patients are at high risk.",
        "Separate catheter-related bloodstream infection, access-site infection, a pyrogenic reaction, and infection elsewhere by timing and pattern.",
        "Draw blood cultures correctly in a dialysis patient, before antibiotics and without using veins needed for future access.",
        "Recognize sepsis and septic shock in a dialysis patient using current definitions, and state their limits in this population.",
        "Start treatment per your unit&rsquo;s protocol with the attending nephrologist, and recognize complications that need escalation: endocarditis, spine infection, and persistent bacteremia.",
    ],
    "big": """
{{plain:Think of a dialysis catheter as an open door from the skin to the heart. The staff unlock it with care at every session. Each time it opens, a little of the outside world can slip in.}}
<p>The picture has a limit. A door lets things in only when it is open, and a catheter does not. Bacteria also creep along its outer surface from the skin, day and night. Once inside, they settle on the catheter wall in a protective layer. The patient&rsquo;s defenses are weaker than normal, so a few bacteria can become a bloodstream infection within hours.</p>
{{cards:Key terms for this module|Bacteremia::Bacteria in the blood, shown by a positive blood culture.|Catheter-related bloodstream infection::Bacteremia whose source is a central venous catheter.|Biofilm::A layer of bacteria and their products on a catheter surface. It shields bacteria from antibiotics and white cells.|Pyrogenic reaction::Chills and fever caused by bacterial fragments, such as endotoxin, entering the blood from contaminated water or fluid. Blood cultures are negative.|Sepsis::Life-threatening organ dysfunction caused by a dysregulated host response to infection.|Septic shock::Sepsis with circulatory and metabolic failure severe enough to need vasopressors and to raise the blood lactate.|Rigors::Violent shaking chills.}}
<p>Shivering in the chair has a short list of causes. In a patient with a catheter, the catheter is the first suspect. A few episodes are pyrogenic reactions from contaminated fluid, which may affect several patients at once. Some are infections elsewhere. Your work is to draw cultures correctly before antibiotics, recognize sepsis even when fever is absent, start treatment per your unit&rsquo;s protocol with the attending nephrologist, and notice when the problem is the unit rather than the patient.</p>
""",
    "case": {"title": "Chills thirty minutes after starting", "html": """
<p>It is Thursday, 2:30 p.m. Mrs. Rosario &ldquo;Charing&rdquo; Dela Cruz, 59, has diabetes and has been on dialysis for eight months. She dialyzes through a tunneled catheter in the right internal jugular vein while her new fistula matures.</p>
<p>Thirty minutes after connection she is shaking under two blankets. The nurse, Mr. Mark Villareal, calls you to her chair. Her temperature is 38.9 &deg;C. Her blood pressure is 98/56 mm Hg; it was 142/80 before the session. Her pulse is 118 per minute, her respiratory rate 24 per minute, and her oxygen saturation 95%. Fluid removal is running at the ordered rate.</p>
<p>The exit site is slightly red, with no pus. The tunnel is not tender. She tells you she felt &ldquo;feverish&rdquo; last night. No other patient on the floor has chills. All values are illustrative.</p>
""", "questions": ["Which of the four explanations is most likely, and what one check rules a unit-wide problem in or out?",
                  "Which cultures do you draw, from where, and before what?",
                  "Does she meet sepsis criteria, what happens in the first hour, and what happens to the session and the catheter?"]},
    "sections": [
        ("why", "Why it happens", "Why dialysis patients get bloodstream infections", """
<p>Intact skin keeps bacteria out, and white cells kill the few that enter. A catheter patient has lost the first defense and has a weaker second.</p>
<p>Bacteria reach the blood by two routes. On the outside, skin bacteria creep along the catheter from the exit site, through the tunnel, toward the vein. On the inside, bacteria enter the lumen from the hub each time the catheter is opened, flushed, or connected. Module 10 covers exit-site and hub care.</p>
{{fig:pod17_catheter_to_blood}}
<p>On the catheter wall, bacteria build a biofilm that protects them from antibiotics and white cells. They shed from it into the blood, sometimes in a burst when the catheter is flushed. This is why a catheter infection can return after antibiotics, and why the catheter itself is often part of the treatment.[[idsa_crbsi2009]]</p>
<p>Module 4 explained that uremia impairs neutrophils and lymphocytes. Fever and the white cell count may therefore rise less than you expect. A modest temperature in a dialysis patient does not mean a modest infection.</p>
<p>United States surveillance gives the clearest numbers. In 2020, 4,840 dialysis facilities reported 14,822 bloodstream infections, and 34.2% were caused by <em>Staphylococcus aureus</em>. From 2017 to 2020, the rate of <em>S. aureus</em> bloodstream infection was 100 times higher in hemodialysis patients than in adults not on dialysis: 4,248 compared with 42 per 100,000 person-years. A central venous catheter was associated with an adjusted rate ratio of 6.2 compared with a fistula.[[rha2023]] These are observational data. Catheter patients are often sicker, and adjustment cannot remove all of that. The direction is consistent and fits the physiology.[[cdc_dialysis_bsi2024]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Link in the chain</th><th>What goes wrong</th><th>What you see at the chair</th></tr></thead>
<tbody>
<tr><td>Skin and exit site</td><td>A permanent break in the skin</td><td>Redness, crusting, or pus. Often nothing</td></tr>
<tr><td>Hub</td><td>Each connection can carry bacteria into the lumen</td><td>Rigors soon after the catheter is opened and flushed</td></tr>
<tr><td>Catheter wall</td><td>Biofilm shelters bacteria</td><td>Bacteremia that returns after treatment</td></tr>
<tr><td>Host defense</td><td>Uremia weakens white cells</td><td>Little or no fever, with a large change in pressure or mentation</td></tr>
</tbody></table></div>
{{key:A dialysis catheter turns a skin germ into a blood infection. Treat fever in a patient with a catheter as bacteremia until cultures say otherwise.}}
"""),
        ("sort", "Four explanations", "Shivering in the chair: four explanations", """
<p>Think of a smoke alarm in an apartment building: a fire in this apartment, on the whole floor, or smoke in the air supply. The picture has a limit: you treat the patient while you find the source.</p>
<p>Four explanations cover most shivering in the chair. The first is a catheter-related bloodstream infection. The second is infection of a fistula or graft, more often a graft (Module 9). The third is a pyrogenic reaction from contaminated water, dialysis fluid, or a solution. The fourth is infection elsewhere: lung, urine if the patient still passes urine, skin, a foot ulcer, the abdomen, the spine, or a heart valve.</p>
<h3>How a pyrogenic reaction behaves</h3>
<p>Endotoxin, from the wall of gram-negative bacteria, causes fever even when the bacteria are dead. It makes white cells release signals that raise the brain&rsquo;s temperature setting, so the patient shivers. Module 6 covers water treatment.</p>
<p>Outbreak reports show the pattern. In one center, contaminated heparinized saline caused 23 reactions in 16 patients. Chills (75%) and fever (90%) began a mean of 1.1 and 3.6 hours into dialysis, and all blood cultures were negative.[[kantor1983]] In another, endotoxin in tap water used for dialysis fluid caused 49 reactions in 23 of 70 patients.[[hindman1975]] In a third, water above the standard and inadequate machine disinfection caused both pyrogenic reactions and gram-negative bacteremia.[[jackson1994]] A prospective study in three centers counted 0.7 reactions per 1,000 treatments.[[gordon1992]] These older reports show the pattern, not current rates; Philippine rates are unknown. The third report is the warning: contaminated fluid can cause true bacteremia, so suspecting a pyrogenic reaction is never a reason to skip cultures.</p>
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>Bloodstream infection</th><th>Pyrogenic reaction</th></tr></thead>
<tbody>
<tr><td>Before the session</td><td>Often unwell the night before</td><td>Well on arrival</td></tr>
<tr><td>Timing</td><td>May start soon after the catheter is opened and flushed, or at any time</td><td>During the session, as exposure continues</td></tr>
<tr><td>Other patients</td><td>Usually one patient</td><td>Often several, on the same shift, water loop, or machine type</td></tr>
<tr><td>Access</td><td>Usually a catheter</td><td>Any access, including fistulas</td></tr>
<tr><td>Blood cultures</td><td>Positive</td><td>Negative, unless the fluid also carried live bacteria</td></tr>
<tr><td>Course</td><td>Persists or worsens without antibiotics</td><td>Often settles within hours once exposure stops</td></tr>
</tbody></table></div>
<p>These features come from the reports above and a standard dialysis text.[[daugirdas2015]] None is a validated test. Use the pattern to look in the right place, and draw cultures in every case.</p>
{{fig:pod17_fever_in_chair}}
{{formula:<strong>Decision walk-through, illustrative.</strong> Three patients on machines of the same model develop chills within the first hour. Blood cultures later return negative in two.<br>Step 1: say aloud that this is a possible cluster, and report to the Medical Director at once.<br>Step 2: hold the affected machines or water loop per the unit&rsquo;s protocol (Module 6).<br>Step 3: draw blood cultures from each patient before any antibiotic.<br>Step 4: record machine numbers, dialyzer lots, and solutions used.<br>Reading: the pattern fits a pyrogenic reaction from contaminated fluid, and the one positive culture fits the outbreak in which bad water caused both.[[jackson1994]][[kantor1983]] Negative cultures do not clear the unit. They point to endotoxin rather than live bacteria.}}
{{call:Stop and call when two or more patients develop chills or fever on the same shift. Call the attending nephrologist and the Medical Director at once, and follow the unit&rsquo;s cluster protocol (Modules 6 and 16).}}
{{key:Before you decide what is wrong with the patient, look around the floor. One patient is usually an infection. Several patients are the unit until proven otherwise.}}
"""),
        ("cultures", "Drawing cultures", "Drawing cultures the right way", """
<p>A fingerprint is useful only if it is lifted before anyone touches the scene. Blood cultures work the same way. The picture has a limit: a fingerprint does not fade, but the first antibiotic dose can kill bacteria in the blood and leave the bottles sterile. That is why cultures come first.</p>
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>Statement</th><th>Grade, in the source&rsquo;s terms</th></tr></thead>
<tbody>
<tr><td>Infectious Diseases Society of America (IDSA), 2009</td><td>Obtain blood cultures before antibiotics are started</td><td>A-I</td></tr>
<tr><td>IDSA, 2009</td><td>For suspected catheter infection, draw paired samples from the catheter and a peripheral vein</td><td>A-II</td></tr>
<tr><td>IDSA, 2009, hemodialysis patients</td><td>Peripheral samples should come from vessels not intended for future use as an access</td><td>A-III</td></tr>
<tr><td>IDSA, 2009, hemodialysis patients</td><td>Samples may be drawn during dialysis from the blood lines connected to the catheter</td><td>B-II</td></tr>
<tr><td>Kidney Disease Outcomes Quality Initiative (KDOQI), 2019</td><td>Obtain appropriate cultures before starting empiric antibiotics for suspected catheter infection (statement 25.1)</td><td>Expert opinion</td></tr>
<tr><td>Surviving Sepsis Campaign, 2026</td><td>For adults with possible, probable, or definite sepsis, collect blood cultures as soon as possible and ideally before the first antimicrobial dose</td><td>Strong recommendation, low certainty of evidence</td></tr>
</tbody></table></div>
<p>The IDSA grades are from 2009.[[idsa_crbsi2009]] The KDOQI algorithm draws one culture set from the catheter hub and one from the dialysis circuit, with peripheral veins optional, partly to protect veins for future fistulas.[[lok2020]] The 2026 sepsis guideline made blood cultures a strong recommendation of its own. Its words are &ldquo;as soon as possible and ideally before&rdquo; the first dose: a sequence to keep, not permission to delay the dose in a patient in shock.[[prescott2026]]</p>
<p>The paired-culture approach came from patients not on dialysis. Quittnat Pelletier and colleagues tested it in 178 suspected catheter infections in a Toronto dialysis unit. Cultures from the dialysis circuit were the most accurate, with a sensitivity of 93.5%, specificity of 100%, and accuracy of 95%. The guideline pair of a peripheral vein and the arterial hub was the least accurate. Only 100 of the 178 events had a peripheral culture at all, and the timing rule that compares how fast each bottle turns positive was met in fewer than one third.[[quittnatpelletier2016]] This single-center study&rsquo;s reference standard included the circuit cultures it tested. Still, it supports circuit and catheter cultures over arm veins.</p>
{{fig:pod17_paired_cultures}}
<p>Your role is to order and supervise the cultures per your unit&rsquo;s protocol. The port is disinfected and dried (Module 10), sets come from the sites the protocol names, and each bottle is filled to the laboratory&rsquo;s volume. Then the first dose is given and timed. Make sure nobody gives the antibiotic first because it was ready sooner.</p>
{{fig:pod17_culture_labels}}
{{key:Cultures first, then antibiotics, and never at the cost of a vein the patient will need for a fistula.}}
"""),
        ("sepsis", "Recognizing sepsis", "Recognizing sepsis in a dialysis patient", """
<p>Infection is the fire. Sepsis is the fire damaging the building&rsquo;s wiring, so that lights fail on floors the flames have not reached. The picture has a limit: in sepsis much of the damage comes from the body&rsquo;s own response, not from the bacteria.</p>
<p>Normally the response to bacteria stays local. In sepsis the white cells&rsquo; signals spread through the body. Vessels widen and leak, so the pressure falls. Tissues use oxygen poorly, so lactate rises, and organs fail in turn. That chain gives the warning signs: fast breathing, confusion, low pressure, and rising lactate.</p>
<p>The Third International Consensus Definitions (Sepsis-3), from 2016, define sepsis as life-threatening organ dysfunction caused by a dysregulated host response to infection. Organ dysfunction is a rise of 2 points or more in the Sequential Organ Failure Assessment (SOFA) score, associated with an in-hospital mortality above 10%. Septic shock is sepsis needing a vasopressor to keep the mean arterial pressure (MAP) at 65 mm Hg or more, with a lactate above 2 mmol/L despite adequate volume, associated with hospital mortality above 40%.[[singer2016]] These are consensus definitions, not graded recommendations.</p>
<p>The same group derived the quick SOFA (qSOFA): one point each for a respiratory rate of 22 per minute or more, altered mentation, and a systolic pressure of 100 mm Hg or less. In 66,522 encounters outside the intensive care unit, a score of 2 or more carried a 3- to 14-fold higher hospital mortality.[[seymour2016]] This retrospective study shows that qSOFA flags risk. It was not designed to rule sepsis out.</p>
<p>The current Surviving Sepsis Campaign guideline (2026) recommends the National Early Warning Score (NEWS or NEWS2), the Modified Early Warning Score (MEWS), or the systemic inflammatory response syndrome (SIRS) criteria over qSOFA as a single screening tool (strong recommendation, moderate certainty). It suggests measuring blood lactate in adults with possible, probable, or definite sepsis (conditional recommendation, low certainty).[[prescott2026]] The 2026 edition says &ldquo;conditional&rdquo; where the 2021 edition said &ldquo;weak&rdquo;.[[evans2021]]</p>
<p>None of these tools was derived in dialysis patients.</p>
<div class="table-wrap"><table>
<thead><tr><th>Red flag</th><th>Why it matters</th><th>Why it can mislead on dialysis</th></tr></thead>
<tbody>
<tr><td>Low blood pressure</td><td>Widespread vessel widening and leak</td><td>Fluid removal and morning blood pressure tablets also lower it. Stop fluid removal and recheck</td></tr>
<tr><td>Fast breathing</td><td>Acidosis and lung injury</td><td>Fluid overload and the acidosis of kidney failure also raise it</td></tr>
<tr><td>Altered mentation</td><td>Poor brain perfusion and inflammation</td><td>Uremia, low blood sugar, and sedating medicines also cause it. Compare with the usual state</td></tr>
<tr><td>Raised lactate</td><td>Tissues short of oxygen, or stress</td><td>Not every unit can measure it. Liver disease and some medicines raise it too</td></tr>
<tr><td>SOFA rise of 2 or more</td><td>Organ dysfunction</td><td>The kidney component is already at its maximum</td></tr>
</tbody></table></div>
{{formula:<strong>Worked example A, illustrative: qSOFA.</strong> Charing: respiratory rate 24 per minute (22 or more: 1 point). Mentation normal (0). Systolic pressure 98 mm Hg (100 or less: 1 point).<br>qSOFA = 1 + 0 + 1 = 2.[[seymour2016]]<br>What it tells you: higher risk; evaluate her now. What it does not: a score of 0 or 1 would not exclude sepsis, and qSOFA should not be the only screen.[[prescott2026]] The qSOFA and SOFA calculator linked below checks a score.}}
{{formula:<strong>Worked example B, illustrative: shock index and mean arterial pressure.</strong> Shock index = heart rate &divide; systolic pressure = 118 &divide; 98 = 1.20.<br>MAP = diastolic + (systolic &minus; diastolic) &divide; 3 = 56 + (98 &minus; 56) &divide; 3 = 56 + 14 = 70 mm Hg.<br>Both are standard bedside arithmetic.[[hall2021]] What they tell you: her heart is racing to hold a fallen pressure. What they do not: the shock index is not validated in dialysis patients, and part of the fall may be fluid removal. Stop it per protocol and recalculate.}}
{{formula:<strong>Worked example C, decision walk-through: SOFA on dialysis.</strong> SOFA scores breathing, clotting (platelets), liver (bilirubin), circulation (MAP and vasopressors), brain (Glasgow Coma Scale), and kidney.[[singer2016]]<br>On maintenance dialysis the kidney component already scores its maximum, so it cannot rise. A change of 2 or more must come from the other five.<br>Example: platelets fall from baseline into a higher band (+1), and a new vasopressor need raises the circulation score (+2 or more). Change from baseline = 3 or more.<br>Lesson: count the change from baseline in the non-kidney organs. This adaptation is a teaching aid, not a validated score.}}
<p>At the chair, stop fluid removal if the pressure is low (Module 13), assess mentation, breathing, and perfusion, ask for a lactate if available, and call.</p>
{{call:Stop and call the attending nephrologist at once when fever or rigors come with low pressure, altered mentation, fast breathing, or a raised lactate. Prepare for transfer while you call.}}
{{key:Sepsis is organ failure, not fever. In a dialysis patient, judge it by the change from the patient&rsquo;s own baseline.}}
"""),
        ("treat", "Starting treatment", "Starting treatment: antibiotics, the session, and the catheter", """
<p>A fire crew calls for backup, fights the fire, and finds the source, all at once. Here the call is to the attending nephrologist, the fight is the first antibiotic dose, and the source is usually the catheter. The picture has a limit: the antibiotic, the fluid, and the catheter plan are the nephrologist&rsquo;s decisions, made with you.</p>
<p>Each hour without an effective antibiotic lets bacteria multiply and organ injury run further. The 2026 guideline grades statements as strong (&ldquo;recommend&rdquo;) or conditional (&ldquo;suggest&rdquo;), with certainty from high to very low.</p>
<div class="table-wrap"><table>
<thead><tr><th>Surviving Sepsis Campaign statement</th><th>Strength and certainty, in the guideline&rsquo;s terms</th></tr></thead>
<tbody>
<tr><td>For possible, probable, or definite septic shock, and for probable or definite sepsis, give antimicrobials immediately, ideally within 1 hour of recognition (2026)</td><td>Strong, very low certainty</td></tr>
<tr><td>For possible sepsis without shock, rapid investigation, with antimicrobials within 3 hours if concern for infection persists (2026)</td><td>Conditional, very low certainty</td></tr>
<tr><td>At high risk of a specific multidrug-resistant bacterium, empiric therapy that covers it (2026). In a catheter infection the usual example is methicillin-resistant <em>S. aureus</em> (MRSA)</td><td>Conditional, very low certainty</td></tr>
<tr><td>Early source control, ideally within 6 hours, when a specific source needs it (2026)</td><td>Conditional, very low certainty</td></tr>
<tr><td>Prompt removal of intravascular access devices that are a possible source of sepsis, after other vascular access has been established (2021)</td><td>Best practice statement, 2021 edition</td></tr>
<tr><td>At least 30 mL/kg of intravenous crystalloid in the first 3 hours for sepsis-induced hypoperfusion or shock (2026)</td><td>Conditional, low certainty</td></tr>
<tr><td>Balanced crystalloids rather than 0.9% saline (2026)</td><td>Conditional, moderate certainty</td></tr>
<tr><td>Norepinephrine as the first-line vasopressor (2026)</td><td>Strong. High certainty against dopamine, low against epinephrine</td></tr>
<tr><td>An initial MAP target of 65 mm Hg in septic shock (2026). For adults aged 65 or older, an initial target of 60 to 65 mm Hg is suggested</td><td>Strong, moderate certainty. Age 65 or older: conditional, low certainty</td></tr>
</tbody></table></div>
<p>The 2026 statements are from the current guideline.[[prescott2026]] The device-removal statement is from the 2021 edition; the 2026 summary we checked did not list it, so it carries its year.[[evans2021]] Much of this rests on low or very low certainty.</p>
<h3>Fluids: a tension to name</h3>
<p>Module 2 explained that fluid given to an anuric patient stays in the body until dialysis removes it. The fluid suggestion is written for adults in general and does not address anuric dialysis patients. The volume for a septic dialysis patient is therefore the attending nephrologist&rsquo;s or the emergency physician&rsquo;s decision. Give what your unit&rsquo;s protocol allows while you call, and record every portion.</p>
<h3>The catheter</h3>
<div class="table-wrap"><table>
<thead><tr><th>IDSA 2009 statement for hemodialysis catheter infection</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>Empiric therapy should include vancomycin and coverage for gram-negative bacilli, based on the local susceptibility pattern</td><td>A-II</td></tr>
<tr><td>Switch to cefazolin for methicillin-susceptible <em>S. aureus</em></td><td>A-II</td></tr>
<tr><td>Remove the catheter for <em>S. aureus</em>, <em>Pseudomonas</em> species, or <em>Candida</em> species, with a temporary catheter at another site</td><td>A-II</td></tr>
<tr><td>If no other site is available, exchange the catheter over a guidewire</td><td>B-II</td></tr>
<tr><td>For other bacteria, treatment may begin without immediate removal, with an antibiotic lock as an adjunct. Remove the catheter if symptoms persist or metastatic infection appears</td><td>B-II</td></tr>
<tr><td>Treat for 4 to 6 weeks when bacteremia persists, or with endocarditis or infected clot in the vein</td><td>B-II</td></tr>
<tr><td>Obtain surveillance cultures 1 week after the course ends</td><td>B-III</td></tr>
</tbody></table></div>
<p>No newer IDSA guideline specific to hemodialysis was found.[[idsa_crbsi2009]] The 2019 KDOQI guideline frames catheter management as individualized: guidewire exchange, removal and reinsertion, salvage, or an antibiotic lock, chosen for the patient&rsquo;s health and access situation (statement 25.2, expert opinion).[[lok2020]] Doses belong to your unit&rsquo;s protocol and Module 20.</p>
<p>The attending nephrologist decides whether the session continues; the call card below covers stopping and returning the blood.</p>
{{key:Cultures, call, antibiotic, source: in that order, and within the hour if the patient looks septic.}}
"""),
        ("hidden", "Where it hides", "Where infection hides: valves and spine", """
<p>Bacteria in the blood are like seeds on the wind. The picture has a limit: they do not land at random. They stick where flow is turbulent, such as a damaged heart valve, or where bone has a rich blood supply, such as the spine.</p>
<p>A valve damaged by calcium, age, or earlier disease has a rough surface. Platelets and fibrin collect there, and bacteria stick to this mesh and grow into a vegetation. In the spine, bacteria lodge in small vessels beside a disc, then spread into the disc and the vertebrae. Pus can press toward the spinal cord. Both can follow a single bacteremia, and both are easy to miss.</p>
{{fig:pod17_where_hides}}
<p>An international registry included 6,691 patients with infective endocarditis, 553 (8.3%) of them on hemodialysis. In the dialysis patients, <em>S. aureus</em> caused 47.8% and enterococci 15.4%. Compared with other patients, in-hospital mortality was 30.4% versus 17%, six-month mortality 39.8% versus 20.7%, and relapse 9.4% versus 2.7%.[[pericas2021]] The registry was observational. In a matched study of 35 dialysis patients with endocarditis and 70 with bacteremia alone, earlier valve disease (odds ratio 29.7) and longer earlier catheter use (150 versus 28.5 days) were associated with endocarditis. Thirty-day mortality was 37.1% versus 17.1%.[[alchalabi2023]] The study was small, so the odds ratio is imprecise. In <em>S. aureus</em> bacteremia generally, a review of 9 studies with 4,050 patients found endocarditis in 14% to 28% with transesophageal echocardiography, compared with 2% to 15% with transthoracic.[[holland2014]]</p>
<p>A systematic review collected 212 dialysis patients with spine infection. <em>S. aureus</em> was the commonest cause. The time from back pain to diagnosis ranged from 3 days to 6 months, and about one quarter developed neurologic deficits.[[madhavan2019]] One center reported 8 spine or paraspinal infections among 162 patients when catheter bacteremia was treated with antibiotics alone, and none in 15 months after it adopted routine catheter exchange.[[philipneri2003]] That small uncontrolled series suggests, but does not prove, that leaving an infected catheter in place raises the risk.</p>
<div class="table-wrap"><table>
<thead><tr><th>Red flag</th><th>What it may mean</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>Fever or positive cultures that persist on treatment</td><td>An infected catheter left in place, a vegetation, or an abscess</td><td>Report the same day. Ask about the catheter plan</td></tr>
<tr><td>A new murmur, or new heart failure</td><td>Valve infection</td><td>Listen at every febrile session. Report at once</td></tr>
<tr><td>Painful spots on fingers or toes, a new stroke, or sudden limb pain</td><td>Fragments of a vegetation lodging downstream</td><td>Call at once. Prepare transfer</td></tr>
<tr><td>New back or neck pain with fever or recent bacteremia</td><td>Disc or vertebral infection</td><td>Examine the spine and legs. Report the earlier bacteremia</td></tr>
<tr><td>Leg weakness, numbness, or new bladder or bowel trouble</td><td>Pressure on the spinal cord</td><td>Emergency. Call and transfer at once</td></tr>
<tr><td>A second bacteremia with the same bacterium</td><td>Relapse from a hidden source</td><td>Report it as a relapse</td></tr>
</tbody></table></div>
{{call:Stop and call the attending nephrologist when a febrile or recently bacteremic patient has new back or neck pain, a new murmur, or any new weakness, numbness, or bladder change. A new neurologic deficit is an emergency; arrange transfer while you call.}}
{{key:Ask every febrile dialysis patient about back pain, and listen for a new murmur.}}
"""),
        ("prevent", "Prevention and call card", "Preventing the next one, and the call card", """
<p>Bloodstream infections are prevented by routines, not heroics. The picture has a limit: a routine protects only when everyone does it.</p>
<p>The Centers for Disease Control and Prevention (CDC) lists nine core interventions: surveillance and feedback, hand hygiene observations, catheter and access care observations, staff education and competency, patient education and engagement, catheter reduction, chlorhexidine skin antisepsis, catheter hub disinfection, and antimicrobial ointment at the exit site.[[cdc_core2013]][[cdc_dialysis_bsi2024]] In 17 United States facilities that adopted such a package, modeled bloodstream infection rates fell by 32% and access-related rates by 54%.[[patel2013]] There was no control group, so part of the fall may reflect other changes. The result supports the package but does not show which part mattered most.</p>
{{fig:pod17_core_interventions}}
<p>Modules 10 and 29 cover the details. Ask for the exit plan for every catheter. Report every bloodstream infection for surveillance. Clean your hands at every chair, because staff copy the doctor. Note in the record which arm is reserved for a fistula.</p>
{{formula:<strong>Worked example E, illustrative: a unit&rsquo;s bloodstream infection rate.</strong> Rate per 100 patient-months = events &divide; patient-months &times; 100, the unit used in the collaborative report.[[patel2013]]<br>A unit has 60 patients for 3 months: 60 &times; 3 = 180 patient-months, with 4 bloodstream infections.<br>Rate = 4 &divide; 180 &times; 100 = 2.2 per 100 patient-months.<br>It gives a number to track. With few events, one extra infection moves it a great deal, so compare quarters, not months. The access infection rate calculator linked below adds a confidence interval.}}
<p>Be exact about the blood. In an isolated infection the circuit is sound. When water, fluid, or a solution may be the cause, the circuit may carry the problem.</p>
{{flow:Call card: fever or rigors in the chair|Recognize::Shivering, rigors, a temperature at or above your unit&rsquo;s threshold, or new low pressure with warm or mottled skin. Fever may be absent.|First 2 minutes::Check airway, breathing, pressure, and mentation. Stop fluid removal if the pressure is low. Look around the floor for other patients with chills. Inspect the exit site and the access.|Stop dialysis?::If unstable, stop per your unit&rsquo;s protocol and prepare transfer. If stable, the attending nephrologist decides whether to continue, which allows circuit cultures and the first antibiotic dose, or to end early. If a cluster or contaminated fluid is suspected, follow the cluster pathway (Modules 6 and 16).|Return the blood?::Yes, per protocol, in an isolated infection with a sound circuit. Do NOT return the blood if hemolysis is possible, if there is air in the venous line, if a severe dialyzer reaction is suspected, or if the circuit has clotted. In a suspected cluster or contaminated fluid, clamp the lines and ask the attending nephrologist before any blood is returned.|Call::The attending nephrologist at once. The Medical Director for any cluster. The emergency room or transport for septic shock, altered mentation, or failing oxygenation. Use the SBAR format (situation, background, assessment, recommendation) from Module 1.|Write::Onset time and pattern. Vital signs over time. Other patients checked. Exit site and access findings. Culture sites and times. Antibiotic name and time, with the dose as ordered. Lactate if done. Who you called, when, and what was decided. Machine number and dialyzer lot if a cluster is suspected. Where the patient went.}}
"""),
    ],
    "debrief": ["""
<p><strong>Which explanation, and what one check?</strong> A catheter-related bloodstream infection is most likely. Charing has a tunneled catheter, a slightly red exit site, and rigors within half an hour of connection. She felt feverish the night before, so the illness began before today&rsquo;s fluid exposure. The one check is a look around the floor. Mr. Villareal confirms that no other patient has chills, so a pyrogenic cluster is unlikely. You still examine her chest and feet.</p>
<p><strong>Which cultures, from where, and before what?</strong> Two culture sets, one from the catheter hub and one from the dialysis circuit, as your unit&rsquo;s protocol specifies. No arm vein is used, because her arms are reserved for access. Both sets are drawn before the first antibiotic dose, filled to the laboratory&rsquo;s volume, and labeled with site and clock time.</p>
<p><strong>Sepsis, the first hour, the session, and the catheter.</strong> She has suspected infection with a qSOFA of 2, a systolic fall of 44 mm Hg from baseline, and a shock index of 1.20. She needs urgent evaluation as possible sepsis. You stop fluid removal, recheck the pressure, ask for a lactate per protocol, and call the attending nephrologist with an SBAR report. Within the hour, after the cultures, the first antibiotic dose is given as the nephrologist orders under the unit&rsquo;s protocol. Her pressure rises to 112/64 mm Hg once fluid removal stops. The nephrologist ends the session early. The blood is returned because the circuit is sound, and she goes to the emergency room for admission. If the cultures grow <em>S. aureus</em>, the guideline advises removing the catheter. That decision, and the plan for her maturing fistula, belong to the nephrologist.</p>
"""],
    "skills": {"title": "Blood cultures from the circuit and catheter, and the first-hour sepsis response",
               "intro": "Perform this response on a training arm and circuit, or with a simulated patient, while your preceptor observes and plays the nurse.",
               "items": [
                   ("Recognizes fever or rigors and checks at once whether other patients on the floor are affected.", True),
                   ("Stops fluid removal if the pressure is low, per the unit&rsquo;s protocol, and reassesses (Module 13).", False),
                   ("Performs hand hygiene and wears gloves and a mask per protocol.", False),
                   ("Disinfects the catheter hub or the blood line sampling port per protocol and lets it dry.", True),
                   ("Draws cultures from the circuit or catheter as the unit&rsquo;s protocol specifies, before any antibiotic.", True),
                   ("Does not use a vein the patient may need for a future access.", True),
                   ("Fills the bottles to the laboratory&rsquo;s required volume and labels each with site and time.", False),
                   ("Screens for sepsis using mentation, breathing, pressure, perfusion, and lactate per protocol, and examines the exit site, the tunnel, the heart for a murmur, and the back.", False),
                   ("Calls the attending nephrologist with an SBAR report and confirms the antibiotic order.", True),
                   ("Gives or confirms the first antibiotic dose as ordered, and records the time.", False),
                   ("States when the blood is returned and when it must not be.", True),
                   ("Decides with the attending nephrologist whether to continue, stop, or transfer, and documents culture times, antibiotic time, vital signs, and the plan.", False),
               ],
               "placement": "For one month, keep a log of every patient with fever or chills on your shifts: access type, onset time, culture sites and times, antibiotic time, and the final culture result. Review the log with your preceptor, and calculate the gap between recognition and the first antibiotic dose for each case."},
    "quiz": [
        ("Why can a catheter infection return after a full course of antibiotics?",
         ["Dialysis removes the antibiotic before it acts",
          "Uremia makes bacteria resistant",
          "Bacteria in a biofilm on the catheter wall are shielded from antibiotics and white cells",
          "Fever is blunted in kidney failure"], 2,
         "Biofilm shields bacteria, which then reseed the blood."),
        ("In United States surveillance, how did a central venous catheter compare with a fistula for <em>S. aureus</em> bloodstream infection?",
         ["It was associated with a rate about six times higher",
          "The rates were similar after adjustment",
          "It was associated with a lower rate",
          "It was associated with a rate about twice as high"], 0,
         "The adjusted rate ratio was 6.2, from observational data."),
        ("Three patients on machines of the same model begin shivering within the first hour of the morning shift. All were well on arrival. What is the first priority?",
         ["Treat each as a separate catheter infection",
          "Give antipyretics and continue all sessions",
          "Wait for culture results before acting",
          "Declare a possible cluster, follow the cluster protocol, and inform the Medical Director at once"], 3,
         "Several patients with one new symptom point to a shared source. Each patient is still assessed and cultured."),
        ("Why are blood cultures still drawn when a pyrogenic reaction is suspected?",
         ["Cultures are always positive in pyrogenic reactions",
          "Contaminated fluid can carry live bacteria and cause true bacteremia",
          "Cultures measure endotoxin",
          "The laboratory requires them for every patient"], 1,
         "In one outbreak, bad water and poor machine disinfection caused both pyrogenic reactions and gram-negative bacteremia."),
        ("A man with a tunneled catheter starts shaking minutes after his catheter is flushed and connected. He felt well on arrival. What does the timing suggest?",
         ["A reaction to the dialyzer membrane",
          "Low blood sugar",
          "Bacteria in the catheter lumen entering the blood, which cultures must confirm",
          "A pyrogenic reaction from the water"], 2,
         "The timing is a clinical clue, not a validated test."),
        ("In a dialysis patient with a catheter and suspected catheter infection, where should the culture sets usually come from?",
         ["Two arm veins",
          "The catheter hub and the dialysis circuit, per the unit&rsquo;s protocol",
          "The catheter tip only",
          "The fistula arm"], 1,
         "KDOQI draws from the hub and circuit, and circuit cultures were the most accurate in a diagnostic study."),
        ("What is the main reason to avoid arm-vein punctures for cultures in a dialysis patient?",
         ["Damaged veins may not be usable for a future fistula",
          "Arm-vein cultures are never positive",
          "Venipuncture causes bacteremia",
          "Arm veins carry dialysis fluid"], 0,
         "IDSA advises that peripheral samples in hemodialysis patients come from vessels not intended for future access (A-III)."),
        ("A woman on dialysis has a qSOFA score of 1. How should you interpret it?",
         ["Sepsis is excluded",
          "She needs no further assessment",
          "She meets the definition of septic shock",
          "It does not exclude sepsis; judge her by the change from her baseline"], 3,
         "qSOFA was derived to flag risk, not to rule sepsis out. The current guideline recommends against using it as the only screen."),
        ("Why can a SOFA score not rise in the kidney component for a patient on maintenance dialysis?",
         ["Dialysis normalizes creatinine",
          "The kidney component is excluded from SOFA",
          "The kidney component already scores its maximum",
          "Urine output is not measured"], 2,
         "A rise of 2 or more must come from breathing, clotting, liver, circulation, or the brain."),
        ("A febrile man with a catheter has a systolic pressure of 92 mm Hg, down from 150 at the start, while fluid removal continues. What do you do first?",
         ["Raise the fluid removal rate to finish on time",
          "Stop fluid removal per protocol, reassess, and call the attending nephrologist",
          "Give a large fluid bolus from memory",
          "Restart the session after a short pause"], 1,
         "Part of the fall may be fluid removal. Stop it, reassess, and call."),
        ("What does the 2026 Surviving Sepsis Campaign guideline say about the timing of antimicrobials in septic shock?",
         ["Within 6 hours, conditional recommendation",
          "After culture results return",
          "Within 3 hours, strong recommendation",
          "Immediately, ideally within 1 hour of recognition, strong recommendation with very low certainty"], 3,
         "The recommendation is strong despite very low certainty of evidence."),
        ("A patient&rsquo;s blood cultures grow <em>S. aureus</em> from a tunneled catheter. What does the IDSA guideline advise about the catheter?",
         ["Remove it and place a temporary catheter at another site",
          "Keep it and treat with antibiotics alone",
          "Keep it and add only an antibiotic lock",
          "Flush it with saline and continue"], 0,
         "Removal is advised for <em>S. aureus</em>, <em>Pseudomonas</em>, and <em>Candida</em> (A-II). A guidewire exchange is an option if no other site exists (B-II)."),
        ("A dialysis patient treated for <em>S. aureus</em> bacteremia a month ago has new back pain and a low fever. What is the best action?",
         ["Prescribe a pain reliever and review next week",
          "Reassure him that back pain is common on dialysis",
          "Examine the spine and legs, ask about weakness and bladder change, and call the attending nephrologist the same day",
          "Advise bed rest at home"], 2,
         "Spine infection is often diagnosed late, and about one quarter of reported patients developed deficits."),
        ("In the international registry, how did endocarditis outcomes in hemodialysis patients compare with other patients?",
         ["Mortality was similar",
          "In-hospital mortality was higher, 30.4% versus 17%",
          "Relapse was less common",
          "Cardiac surgery was performed more often"], 1,
         "Six-month mortality and relapse were also higher. The data are observational."),
        ("A patient&rsquo;s session ends early for an isolated catheter infection. The circuit is intact and unclotted. Another patient that shift had a suspected contaminated solution. What applies to each circuit?",
         ["Return neither",
          "Return both",
          "Return the contaminated circuit only",
          "Return the blood in the isolated infection per protocol; in the suspected contamination, clamp and ask the attending nephrologist first"], 3,
         "When the fluid or circuit may be the cause, the blood is not returned without the nephrologist&rsquo;s advice."),
    ],
    "terms": [("Bacteremia", "Bacteria in the blood, shown by a positive blood culture."),
              ("Catheter-related bloodstream infection", "Bacteremia whose source is a central venous catheter."),
              ("Biofilm", "A layer of bacteria and their products on a catheter surface that shields them from antibiotics and white cells."),
              ("Pyrogenic reaction", "Chills and fever from bacterial fragments such as endotoxin entering the blood. Blood cultures are negative."),
              ("Endotoxin", "A component of the outer wall of gram-negative bacteria that triggers fever even when the bacteria are dead."),
              ("Sepsis", "Life-threatening organ dysfunction caused by a dysregulated host response to infection."),
              ("Septic shock", "Sepsis needing a vasopressor to keep the mean arterial pressure at 65 mm Hg or more, with a lactate above 2 mmol/L despite adequate volume."),
              ("qSOFA", "Quick Sequential Organ Failure Assessment: one point each for fast breathing, altered mentation, and low systolic pressure."),
              ("Infective endocarditis", "Infection of a heart valve or the lining of the heart, usually with a vegetation."),
              ("Spondylodiscitis", "Infection of an intervertebral disc and the adjacent vertebrae.")],
    "readings": [("dialysis-access-infection.html", "How access and catheter infections present and how they are treated."),
                 ("dialysis-access-care.html", "Daily access care that prevents infection."),
                 ("hemodialysis-complications.html", "An overview of problems during dialysis, including fever and chills.")],
    "calcs": ["calc-qsofa-sofa.html", "calc-shock-index.html", "calc-access-infection-rate.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
