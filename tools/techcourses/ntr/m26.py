# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 26: Infection prevention, water safety and shared exposures.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. KDIGO 2022 hepatitis C
statements and grades checked against the guideline PDF; CDC collaborative numbers, Caruaru and chloramine outbreak details checked
against PubMed abstracts; water limits from a peer-reviewed review table and the US federal rule text. No drug doses. Fictional case."""

MODULE = {
 'image_alt': 'A physician, a dialysis nurse and a water treatment technician stand at the water treatment room of a dialysis unit, the technician holding a chlorine test strip against a color chart.',
 'objectives': [
  '<strong>Intern:</strong> Follow hand hygiene at every patient contact in the dialysis unit, apply the unit&rsquo;s isolation rules for hepatitis B, and know why hepatitis C and HIV are managed with standard precautions.',
  '<strong>Resident:</strong> Recognize a catheter-related bloodstream infection and a cluster of febrile reactions, and tell an infection in one patient from a shared exposure affecting several.',
  '<strong>Fellow:</strong> Lead the response to an infection outbreak or a water event: stop exposure, find the source with the technician and the infection control team, report, and change the system.',
 ],
 'big': """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the shared room and the shared water</span>The <strong>intern</strong> owns the most effective prevention in the unit: clean hands before and after every contact with a patient, a machine or a line. The <strong>resident</strong> on the dialysis rotation, or moonlighting as physician on duty, recognizes fever in the chair, cultures before antibiotics, and notices when one febrile patient becomes three. The <strong>fellow</strong>, with the attending nephrologist, the medical director and the water technician, leads the response when the cause is shared: a lapse in infection control, a contaminated supply or the water itself.</div>
{{plain:Picture a jeepney terminal at rush hour: dozens of people in one room, touching the same rails, sitting where someone else sat an hour ago, all drinking from the same water dispenser. If one passenger carries a virus, or the dispenser is contaminated, everyone downstream is exposed. A dialysis unit is that terminal, three shifts a day, six days a week.}}
<p>The picture has a limit. Terminal passengers touch rails and drink a glass of water. Dialysis patients have needles or catheters in their great vessels, their blood leaves the body and returns, and each session exposes their blood across a membrane to well over a hundred liters of dialysate made from treated water. Their immunity is blunted by uremia. A tiny lapse (an unwashed glove, a shared multidose vial, a carbon tank past its limit) reaches the bloodstream directly. That is why hepatitis B and C have spread in dialysis units, why catheter infections remain a major cause of admission, and why contaminated water has killed dozens of patients in a single unit.</p>
{{cards:Key numbers|HCV screening of in-center HD patients (KDIGO 2022, 1B)::Every 6 months by immunoassay or nucleic acid test|Dedicated machines for HCV (KDIGO 2022, 1D)::Recommended against; isolation of HCV patients suggested against (2C)|AAMI chemical limits for dialysis water::Chloramines 0.10 mg/L; free chlorine 0.50 mg/L|ISO and AAMI microbial limits for water::Under 100 CFU/mL (action at 50); endotoxin under 0.25 EU/mL (action at 0.125)|CDC bloodstream infection collaborative (17 units)::Modeled access-related infections fell 54% after the core interventions (no control arm)}}
<p>Most fevers in a dialysis chair are one patient&rsquo;s infection, most often from a catheter. A few are a shared event: a cluster from a lapse in technique, a contaminated supply, or water that has broken through its treatment. Your work is to protect every patient with the basics every time, to treat the individual infection correctly, and to recognize early when the cause is shared, because then the next shift is already exposed.</p>
""",
 'case': {'title': 'Three patients with chills',
          'html': """
<p>Tuesday, 2:30 p.m., a freestanding hemodialysis unit in Lipa City, Batangas. The municipal water supply was cut for a day after a pipe repair, and the unit received water by tanker truck yesterday and this morning. The technician changed nothing in the treatment system.</p>
<p>The physician on duty, Dr. Andrea Cruz, a second-year internal medicine resident, is called to chair 4: Mr. Danilo Ramos, 59, dialyzing through a fistula, has rigors 50 minutes into his session, temperature 38.7 &deg;C, blood pressure 128/76 mm Hg. Ten minutes later the nurse calls her to chair 7: Mrs. Teresita Laurel, 66, dialyzing through a tunneled catheter, also shivering, 38.9 &deg;C, pressure 96/58 mm Hg, with redness at the catheter exit site. By 3:15 p.m., a third patient, on a fistula, at chair 2, has chills and a headache.</p>
<p>Ms. Arlene Medina, the charge nurse, says all three started within the first hour of their sessions. The technician tells Dr. Cruz that this morning&rsquo;s chlorine test after the first carbon tank was &ldquo;a bit higher than usual&rdquo; but that the second tank reading was fine. The attending nephrologist is at a conference in Manila.</p>
""",
          'questions': ['What do you do at each chair right now?',
                        'Is this three separate infections or one shared exposure, and how do you tell?',
                        'What should the unit do today and this week?']},
 'sections': [
  ('bloodborne', 'Bloodborne viruses', 'Hepatitis B, hepatitis C and HIV: why the rules differ', """
<p>Bloodborne viruses spread in dialysis units through blood: on hands and gloves, on shared surfaces and equipment, through shared medication vials and supply carts. Each virus has its own survival and dose, and that explains why the rules differ.</p>
<div class="table-wrap"><table>
<thead><tr><th>Virus</th><th>Why it matters in dialysis</th><th>What the unit does</th></tr></thead>
<tbody>
<tr><td>Hepatitis B</td><td>Very high concentration in blood and survives on surfaces, so tiny contaminations transmit</td><td>Test all patients; vaccinate susceptible patients and check their antibody response; test susceptible patients regularly; dialyze patients who carry hepatitis B surface antigen (HBsAg) in a separate room with dedicated machines, equipment and supplies, with staff who do not care for susceptible patients on the same shift[[ntr26_1]]</td></tr>
<tr><td>Hepatitis C</td><td>Transmission follows lapses in standard precautions and injection safety</td><td>Standard precautions, audits, screening every 6 months, tracking every result; no dedicated machines or isolation required by KDIGO[[ntr26_2]][[ntr26_3]]</td></tr>
<tr><td>HIV</td><td>Low transmission risk with standard precautions</td><td>Standard precautions; no isolation or dedicated machine[[ntr26_1]]</td></tr>
</tbody></table></div>
<p>The hepatitis B measures come from the Centers for Disease Control and Prevention (CDC) recommendations for chronic hemodialysis units, which also define immunity after vaccination as an antibody to surface antigen (anti-HBs) level of at least 10 mIU/mL and advise revaccination of nonresponders.[[ntr26_1]] Patients with kidney failure respond less well to the vaccine than healthy adults, which is why the post-vaccination check matters.</p>
<h3>Hepatitis C: the guideline and local practice</h3>
<p>The Kidney Disease: Improving Global Outcomes (KDIGO) 2022 hepatitis C guideline recommends that hemodialysis facilities adhere to standard infection control procedures (1A) with regular observational audits (1C); recommends not using dedicated dialysis machines for patients with hepatitis C virus (HCV) infection (1D); suggests not isolating them (2C); suggests their dialyzers can be reused if standard procedures are followed (2D); recommends that centers examine and track all HCV test results (1B); and recommends screening in-center hemodialysis patients every 6 months (1B). When a new infection is likely acquired in the unit, it recommends aggressive measures to improve hand hygiene, injection safety and environmental cleaning (1A).[[ntr26_2]] A review of HCV transmission in dialysis settings emphasizes regular audits and staff training, and a protocol for investigating suspected unit-acquired cases.[[ntr26_3]]</p>
<p>Many Philippine units still assign dedicated machines or areas to HCV-positive patients. KDIGO&rsquo;s reasoning is that transmission tracks breaks in technique, not shared machines, and that a dedicated machine can create a false sense of safety while hands and vials keep spreading the virus. Its recommendation against dedicated machines is graded 1D, low certainty. Follow your unit&rsquo;s licensing requirements and written policy under the Department of Health (DOH) rules,[[ntr26_13]] and never let a dedicated machine stand in for hand hygiene.</p>
{{flow:Hand hygiene at the chair|Before touching the patient or the machine::Alcohol rub or wash; new gloves.|Before any aseptic task::Before needling, catheter connection, medication preparation.|After body fluid risk::After needle removal, catheter disconnection, handling blood lines or waste.|After touching the patient::Remove gloves and clean hands before moving to the next chair.|After touching the surroundings::The machine, the chair, the table count as the patient&rsquo;s zone.}}
<p>The CDC lists hand hygiene observations every month, with feedback to staff, among its core interventions for dialysis bloodstream infection prevention.[[ntr26_5]] For the intern, this is the lesson that matters most: the habit of clean hands at every chair is the main barrier between one infected patient and the rest of the room.</p>
<div class="tc-keyp"><span class="tc-lab">In children</span>Children in a mixed or adult unit need the same standard precautions and the same hepatitis B vaccination and testing, with schedules and doses from the pediatric team, and a family that understands catheter care at home. Water quality matters even more where small bodies receive large volumes of dialysate. See <a href="attending-pediatric-nephrologist-25-hd-emergencies-water.html">Attending Pediatric Nephrologist, Module 25</a>.</div>
{{key:Hepatitis B gets a separate room, machine and staff; hepatitis C and HIV get flawless standard precautions. Every patient gets clean hands at every contact.}}
"""),
  ('bsi', 'Bloodstream infection', 'Bloodstream infection: the catheter, the fistula and the culture', """
<p>A central venous catheter is a plastic bridge from the skin and the hub to the right atrium. Bacteria travel along the outside from the exit site, or along the inside from the hub each time it is opened, and settle in a biofilm that shields them from antibiotics and from the patient&rsquo;s defenses. A fistula is the patient&rsquo;s own vessel, punctured fresh each session, and carries far less risk. Reducing catheter use through timely permanent access is part of the end-stage kidney disease life-plan in the Kidney Disease Outcomes Quality Initiative (KDOQI) 2019 vascular access guideline.[[ntr26_7]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Clue</th><th>What it suggests</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>Fever or rigors in a catheter patient, especially soon after connection</td><td>Catheter-related bloodstream infection until proven otherwise</td><td>Blood cultures before antibiotics, per protocol; inspect the exit site and tunnel; call</td></tr>
<tr><td>Redness, pus or tenderness at the exit site or along the tunnel</td><td>Exit-site or tunnel infection</td><td>Culture any discharge; the attending decides on catheter management</td></tr>
<tr><td>Fever with low pressure, confusion or rising lactate</td><td>Sepsis</td><td>Sepsis protocol; end the session with the attending; transfer if needed</td></tr>
<tr><td>Fever in a fistula patient with a hot, swollen access</td><td>Access infection</td><td>Do not cannulate the infected area; cultures; call</td></tr>
<tr><td>Fever and chills in several patients on the same shift</td><td>A shared source: water, dialysate, a supply, a lapse</td><td>See the cluster lesson below; tell the charge nurse and technician now</td></tr>
</tbody></table></div>
<p>The Infectious Diseases Society of America (IDSA) 2009 guideline on intravascular catheter infection describes how to diagnose catheter-related bloodstream infection with paired cultures and how management depends on the bacterium or fungus and whether the catheter is kept, exchanged or removed, including hemodialysis-specific approaches when peripheral veins must be saved for future access.[[ntr26_6]] Antibiotic choice and doses come from your unit&rsquo;s protocol, the culture and the attending.</p>
<h3>Prevention works when it is a system</h3>
<p>In a CDC collaborative, 17 outpatient units reported infections to the National Healthcare Safety Network and implemented a package: chlorhexidine for catheter exit-site care, staff training and competency checks on catheter care and aseptic technique, hand hygiene and vascular access care audits, and feedback of infection and adherence rates to staff. Pooled bloodstream infection rates went from 1.09 to 0.89 per 100 patient-months, and access-related infections from 0.73 to 0.42; modeled rates fell 32% and 54%. There was no control arm, and the participating units were volunteers.[[ntr26_4]] CDC now publishes the package as its core interventions.[[ntr26_5]] The design means these numbers show what is possible, not a guaranteed effect, but no unit has an excuse not to try.</p>
<p><strong>Philippine reality.</strong> Many patients start dialysis on a catheter because they reached kidney failure without a fistula, and many stay on one because access surgery costs money, the surgeon is far away, or the fistula failed. Every catheter month is risk. The resident&rsquo;s contribution is to ask at each review, &ldquo;why is this patient still on a catheter, and who is fixing that?&rdquo;</p>
{{key:Culture before antibiotics, inspect the exit site, and ask every catheter patient&rsquo;s team when the catheter will come out.}}
"""),
  ('water', 'Water safety', 'Water: the largest exposure in the room', """
<p>Tap water is safe to drink because the gut is a selective barrier and we drink a liter or two a day. Dialysate is separated from blood only by a thin membrane, and each session exposes the patient to well over a hundred liters. Small molecules, including chloramine, aluminum and copper, cross into the blood, and fragments of bacteria (endotoxin) can cross or trigger inflammation. So dialysis water is treated in stages: sediment filters and softener, activated carbon to remove chlorine and chloramine, reverse osmosis to remove most dissolved substances, and a distribution loop kept free of biofilm.[[ntr26_8]]</p>
{{fig:ntr26_a}}
<div class="table-wrap"><table>
<thead><tr><th>Contaminant</th><th>Limit used in standards</th><th>What happens if it breaks through</th></tr></thead>
<tbody>
<tr><td>Chloramines</td><td>0.10 mg/L (Association for the Advancement of Medical Instrumentation, AAMI)[[ntr26_8]]</td><td>Oxidative damage to red cells: hemolysis, methemoglobinemia, falling hemoglobin</td></tr>
<tr><td>Free chlorine</td><td>0.50 mg/L (AAMI)[[ntr26_8]]</td><td>Same oxidative injury</td></tr>
<tr><td>Bacteria in water</td><td>Under 100 colony-forming units (CFU)/mL, action level 50 CFU/mL (International Organization for Standardization [ISO] and AAMI)[[ntr26_8]]</td><td>Biofilm, endotoxin release, pyrogenic reactions</td></tr>
<tr><td>Endotoxin in water</td><td>Under 0.25 endotoxin units (EU)/mL, action level 0.125 EU/mL (ISO and AAMI)[[ntr26_8]]</td><td>Fever, chills, hypotension during dialysis; chronic inflammation</td></tr>
<tr><td>Aluminum and other metals</td><td>Low limits set by the same standards[[ntr26_8]]</td><td>Bone disease, anemia, encephalopathy with chronic exposure</td></tr>
</tbody></table></div>
<p>Carbon tanks are the defense against chlorine and chloramine, and they exhaust silently. The United States rule requires two carbon tanks in series; if the reading after the first tank is above 0.5 mg/L free chlorine or 0.1 mg/L chloramines, or at or above 0.1 mg/L total chlorine, the second tank must be tested, and the rule sets what happens when the second tank also fails.[[ntr26_9]] Philippine dialysis facilities follow the DOH water guidelines issued under the licensing rules, which set the analysis, monitoring and maintenance of dialysis water.[[ntr26_10]] Know your own unit&rsquo;s written test schedule and action levels; the technician holds the log, but the physician is responsible for acting on it.</p>
<h3>What happens when water fails</h3>
<p>In 1996, after a drought, all 126 patients in a hemodialysis unit in Caruaru, Brazil, developed acute neurotoxicity and toxic hepatitis after the unit used water from a lake with a massive growth of cyanobacteria; 60 died. Microcystins, the algal toxins, were found in patients&rsquo; serum, dialysis filters and water-treatment columns.[[ntr26_12]] In a Brazilian unit in 2004, dialysate chloramine levels rose from below 0.1 to 0.27 in three months and an outbreak of anemia followed; hemoglobin recovered within a month of replacing the activated charcoal column, without changing erythropoietin doses.[[ntr26_11]] The first was a catastrophe from source water; the second a slow, silent exhaustion of carbon. Both are possible in the Philippines: units that draw from wells, that receive water by tanker after a pipe break or a typhoon, or that delay a carbon change.</p>
<p><strong>Philippine reality.</strong> Tanker water, interrupted municipal supply, brownouts that stop the treatment system, floods that reach the water room, and well water with variable quality all stress the treatment train. A change in source water is a reason to test more often, not less. The site&rsquo;s carbon tank empty-bed contact time calculator helps the technician and the medical director check whether the carbon stage is sized for the flow.</p>
{{key:A change in the water (a tanker, a well, a pipe repair, a flood) is a reason to test chlorine before every shift and to suspect the water first when several patients react.}}
"""),
  ('cluster', 'Clusters and outbreaks', 'From one patient to a cluster: leading the response', """
<p>A cluster is more cases than expected, close together in time or place. In a dialysis unit, two or three patients with fever, chills, hemolysis or a new hepatitis result in a short period is a cluster until shown otherwise. The pattern of cases points to the source.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pattern</th><th>Likely shared source</th><th>First checks</th></tr></thead>
<tbody>
<tr><td>Fever and chills early in the session, in patients with fistulas and catheters alike, on the same shift</td><td>Water or dialysate: endotoxin or bacteria (a pyrogenic reaction), or chemical contamination</td><td>Stop new sessions on the affected loop; water and dialysate cultures and endotoxin; chlorine; review the treatment log</td></tr>
<tr><td>Hemolysis or falling hemoglobin across many patients</td><td>Chloramine or other oxidant breakthrough; a faulty supply lot</td><td>Total chlorine before and after each carbon tank; keep tubing and packaging</td></tr>
<tr><td>Bloodstream infections with the same bacterium, mostly catheter patients</td><td>A lapse in catheter care, a contaminated antiseptic or priming solution</td><td>Audit technique; cultures of products; review who connected the catheters</td></tr>
<tr><td>A new hepatitis C or B result in a previously negative patient</td><td>Unit-acquired transmission</td><td>Review all results, station and staff assignments, vial use; enhanced audits; report</td></tr>
</tbody></table></div>
<p>A pyrogenic reaction from endotoxin typically begins during the session, often within the first hour, and settles after the session stops, with negative blood cultures. A true bloodstream infection tends to persist and produces positive cultures. At the chair you often cannot tell them apart, so culture every febrile patient before antibiotics and treat the sick ones; the pattern across patients, and the cultures, answer the question later.</p>
{{flow:Responding to a suspected cluster or water event|Protect patients now::Treat each patient; culture before antibiotics; stop sessions on the suspected supply or loop; do not start new patients until the source is checked.|Tell the right people::Charge nurse, water technician, medical director and attending nephrologist, at once. Notify infection control.|Keep the evidence::Save dialyzers, tubing, packaging and lot numbers; draw water and dialysate samples from the points the technician names before any change is made.|Check the water::Total chlorine before and after each carbon tank; reverse osmosis alarms and readings; any change in source water; disinfection dates.|Line list::Every affected patient: chair, machine, shift, access type, onset time, symptoms, temperature, cultures.|Report and fix::Report per DOH and facility rules; correct the source; restart only when the medical director signs off; review with the team.}}
<p>The same-event drill on this site follows one water event through every role in the unit, from technician to head nurse to physician on duty; work through it with your unit before you need it.</p>
{{call:Stop and call the attending nephrologist and the medical director at once, per unit protocol, but always ask the attending nephrologist for guidance:<ul><li>Two or more patients with fever, chills, hemolysis or hypotension on the same shift</li><li>A chlorine or chloramine reading at or above the unit&rsquo;s action level after any carbon tank</li><li>Any change in source water (tanker, well, repair, flood) with patient symptoms</li><li>A febrile catheter patient with low blood pressure or confusion</li><li>A new hepatitis B or C result in a previously negative patient</li></ul>}}
{{fig:ntr26_b}}
{{key:When more than one patient becomes unwell, stop thinking about each patient alone: protect the next shift, keep the evidence, and test the water.}}
"""),
 ],
 'debrief': [
  """<p><strong>At each chair now.</strong> Dr. Cruz examines each patient, takes temperature, pressure and pulse, and has blood cultures drawn before any antibiotic, per protocol. Mrs. Laurel, with a red catheter exit site and a falling pressure, gets the hypotension and sepsis steps, cultures from the catheter and a swab of the exit site, and a call to the attending about ending her session and starting antibiotics. The two fistula patients are stable; she watches them closely and, with the charge nurse, stops starting new patients on the same water until the source is checked. To rehearse it as a team, run the Academy&rsquo;s <a href="/academy/same-event-every-role.html?event=water">Same event, every role</a> drill.</p>""",
  """<p><strong>Three infections or one exposure?</strong> Three patients on one shift, two with fistulas, all starting within the first hour, the day after the unit switched to tanker water, with a higher-than-usual chlorine reading after the first carbon tank: this is a shared exposure until proven otherwise. Endotoxin or bacteria from the new water (a pyrogenic reaction) best fit the fistula patients; Mrs. Laurel may have that, a catheter infection, or both. Cultures of blood, water and dialysate, endotoxin tests and the chlorine readings before and after each tank will separate them.</p>""",
  """<p><strong>Today and this week.</strong> Today: tell the charge nurse, technician, medical director and attending at once; keep dialyzers, tubing and lot numbers; sample water and dialysate before any change; test total chlorine before and after each carbon tank before every shift; make a line list of all patients treated today; and report per DOH rules. This week: with the medical director, review the tanker source and the carbon stage, disinfect the loop if cultures or endotoxin are high, audit hand hygiene and catheter care, and, for Mrs. Laurel, push her fistula referral forward so the catheter can come out.</p>""",
 ],
 'skills': {'title': 'Infection prevention and water safety in the dialysis unit',
            'intro': 'Complete in your dialysis unit with the charge nurse, the water technician and your preceptor. Sign-off is local.',
            'items': [
             ('Performs hand hygiene at all five moments during a dialysis shift, observed by the charge nurse', False),
             ('States the unit&rsquo;s hepatitis B isolation rules and the KDIGO position on hepatitis C machines, with grades', False),
             ('Assesses a febrile catheter patient: exit site, tunnel, cultures before antibiotics, sepsis screen, call', False),
             ('Reads the water treatment log with the technician, including total chlorine after each carbon tank and the action levels', False),
             ('Builds a line list for a simulated cluster and names the samples to take before any change', False),
             ('Walks through the same-event drill for a water event with the unit team', False)],
            'placement': 'Hemodialysis unit, including the water treatment room'},
 'quiz': [
  ('An intern finishes disconnecting a patient&rsquo;s catheter and is asked to help at the next chair. What is the correct sequence?',
   ['Keep the same gloves to save time and go to the next chair',
    'Remove gloves, clean hands, and put on new gloves before touching the next patient or machine',
    'Wipe the gloves with alcohol and proceed',
    'Clean hands only if the gloves are visibly soiled'],
   1,
   'Gloves carry blood and bacteria between stations. Hand hygiene after removing gloves and before the next patient is the main barrier to bloodborne virus and bacterial transmission; CDC lists monthly hand hygiene audits among its core interventions.'),
  ('A catheter patient develops rigors 30 minutes into dialysis; his pressure is stable. Two other patients on fistulas are well. What should the resident do?',
   ['Give an antibiotic now and skip cultures to save time',
    'Draw blood cultures before antibiotics per protocol, inspect the exit site and tunnel, and call the attending',
    'Assume a pyrogenic reaction and continue without action',
    'Remove the catheter immediately in the unit'],
   1,
   'A single febrile catheter patient most likely has a catheter-related bloodstream infection. Cultures before antibiotics guide treatment; catheter management is the attending&rsquo;s decision per the IDSA approach. A pyrogenic reaction becomes likely when several patients react together.'),
  ('According to KDIGO 2022, how should a unit manage patients with hepatitis C infection?',
   ['Dedicated machines and an isolation room are recommended (1A)',
    'Standard infection control with audits; dedicated machines recommended against (1D) and isolation suggested against (2C)',
    'Dialyzers of HCV patients must never be reused',
    'Screen once at entry only'],
   1,
   'KDIGO 2022 recommends standard procedures (1A) and audits (1C), recommends against dedicated machines (1D), suggests against isolation (2C), allows dialyzer reuse with standard precautions (2D) and recommends screening every 6 months (1B). Hepatitis B, unlike C, still calls for separation.'),
  ('A unit using tanker water after a pipe repair finds a total chlorine of 0.2 mg/L after the first carbon tank. The second tank reads 0.05 mg/L. What is the most appropriate response?',
   ['No action, since the water reaching patients is below 0.1 mg/L',
    'Treat it as a carbon breakthrough warning: test the second tank before every shift, tell the medical director, and plan carbon replacement, because the first tank has exhausted',
    'Add more chlorine to the tanker water',
    'Stop testing until the municipal supply returns'],
   1,
   'The first tank is no longer removing chlorine, so only one barrier remains. The US rule requires testing the second tank whenever the first reads at or above 0.1 mg/L total chlorine. In the 2004 chloramine outbreak, anemia resolved after the charcoal column was replaced.'),
  ('Within one shift, three patients, two with fistulas and one with a catheter, develop chills and fever within the first hour of dialysis. What is the most likely explanation and first priority?',
   ['Three coincidental catheter infections; start antibiotics and continue the shift',
    'A shared exposure, most likely water or dialysate: treat and culture each patient, stop new sessions on that supply, keep the evidence, test the water and alert the medical director',
    'A viral illness in the community; send them home',
    'Dialyzer reactions; switch membranes for the next session only'],
   1,
   'Early fever in several patients, including those without catheters, points to a shared source such as endotoxin in the water or dialysate. The next shift is already exposed, so the response starts with stopping exposure and testing.'),
 ],
 'terms': [
  ('AAMI', 'Association for the Advancement of Medical Instrumentation'),
  ('anti-HBs', 'Antibody to hepatitis B surface antigen'),
  ('CDC', 'Centers for Disease Control and Prevention (United States)'),
  ('CFU', 'Colony-forming unit'),
  ('DOH', 'Department of Health (Philippines)'),
  ('EU', 'Endotoxin unit'),
  ('HBsAg', 'Hepatitis B surface antigen'),
  ('HCV', 'Hepatitis C virus'),
  ('HD', 'Hemodialysis'),
  ('HIV', 'Human immunodeficiency virus'),
  ('IDSA', 'Infectious Diseases Society of America'),
  ('ISO', 'International Organization for Standardization'),
  ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
  ('KDOQI', 'Kidney Disease Outcomes Quality Initiative'),
  ('Pyrogenic reaction', 'Fever and chills during dialysis caused by bacterial fragments (endotoxin) in water or dialysate, with negative blood cultures'),
 ],
 'readings': [('physician-on-duty-17-fever-and-bloodstream-infection.html', 'Physician on Duty, Module 17: Fever and Bloodstream Infection'),
              ('physician-on-duty-29-a-clean-unit.html', 'Physician on Duty, Module 29: A Clean Unit'),
              ('dialysis-water-treatment-systems.html', 'Dialysis Water Treatment Systems')],
 'calcs': ['calc-access-infection-rate.html', 'calc-carbon-tank-ebct.html'],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
