# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 11: PD peritonitis and exit-site infection, the first hour. POD voice. Fictional cases."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Apply the 2024 ISPD pediatric criteria for an empiric diagnosis of peritonitis, including the dwell-time rule for children on APD.",
        "Run the first hour after a cloudy bag: sepsis screen, specimen, escalation and antibiotics as ordered without delay.",
        "Recognize exit-site and tunnel infection and their treatment durations, and what the nurse monitors.",
        "Calculate a program peritonitis rate and compare it with the ISPD 2024 pediatric benchmarks.",
    ],
    "big": """
<p>Peritonitis is infection of the peritoneum, usually from organisms that entered through a connection, the exit site and tunnel, or the bowel. It is the main reason children leave PD. It is also one of the most treatable emergencies in dialysis, if it is recognized and treated quickly.</p>
<p>Your work in this module is to recognize peritonitis early, get a good specimen, start the ordered antibiotics without delay, and keep the family calm and informed.</p>
{{plain:Think of the effluent bag as a window into the abdomen. Clear fluid is a clean window. Cloudy fluid is the window fogging up: white blood cells have rushed into the abdomen because something is wrong.}}
<p>The picture has a limit. A clean window does not prove a clean room. A child on cycler therapy with short night dwells and a dry day may have so little dwell time that white cells have not accumulated. That is why the guideline asks for an adequate dwell before sampling, and why pain or fever with clear fluid still needs a call.</p>
{{cards:Key terms for this module|Peritonitis::Infection or inflammation of the peritoneum.|Effluent cell count::White blood cells per mm&sup3; in the drained fluid, with the share that are neutrophils.|Intraperitoneal (IP) antibiotic::An antibiotic added to the dialysate.|Refractory peritonitis::Peritonitis that has not cleared after 5 days of appropriate antibiotics.|Culture-negative peritonitis::Peritonitis in which no organism grows.}}
""",
    "case": {"title": "Cloudy on a school morning", "html": """
<p>At 6:30 a.m., <strong>Mrs. Joy Castillo</strong> calls the PD hotline: the first drain of her son <strong>Paolo, 8</strong>, 24 kilograms, looks cloudy, and he says his tummy hurts. He is on APD with a dry day. He feels warm. They live 40 minutes from the hospital by tricycle and jeepney. <strong>Nurse Rina</strong> answers.</p>
""", "questions": ["What does Rina ask first, and why?",
                  "What should happen to the bag, and when should a sample be taken?",
                  "How fast should antibiotics start, and who orders them?"]},
    "sections": [
        ("recognizing-peritonitis", "Recognition", "Recognizing peritonitis in a child", """
<p>The 2024 ISPD pediatric guideline makes an empiric diagnosis when at least two of the following are present: effluent white cell count above 100/mm&sup3;, at least 50% neutrophils (polymorphonuclear cells), clinical signs such as abdominal pain or fever, and growth on culture (statement 8.2, not graded).[[pdn_warady2024]]</p>
{{fig:pdn11_a}}
<p>For a child on APD without a daytime dwell, the guideline&rsquo;s rationale says the fill volume should be instilled for at least 2 hours before the sample is taken, so that cells have time to collect. Obtaining the sample correctly and using proper culture technique are described as crucial for diagnosis and for choosing antibiotics (8.3).[[pdn_warady2024]]</p>
<p>Young children may not say &ldquo;my tummy hurts&rdquo;. Look for irritability, refusing to be held, vomiting, poor feeding, a tense abdomen, or a child who will not walk. Fever may be absent.</p>
{{key:Cloudy fluid, pain or fever: any one is a call. Two of the four criteria make the empiric diagnosis.}}
"""),
        ("the-first-hour", "First hour", "The first hour", """
<p>Antibiotics should start as soon as possible after the right specimens are obtained (9.1, not graded); the rationale notes that adult data link delays with more catheter removal, PD discontinuation and death.[[pdn_warady2024]]</p>
{{fig:pdn11_b}}
<div class="table-wrap"><table>
<thead><tr><th>Minute</th><th>Action</th></tr></thead>
<tbody>
<tr><td>0&ndash;5</td><td>Sepsis screen by phone: is the child drowsy, floppy, breathing fast, cold, mottled, vomiting repeatedly, or not passing urine? If yes, emergency transport now.</td></tr>
<tr><td>5&ndash;10</td><td>Keep the cloudy bag, closed, cool, upright; bring it. Note the time it was drained.</td></tr>
<tr><td>10&ndash;15</td><td>Call the PD nephrologist with SBAR (situation, background, assessment, recommendation); agree on where the child is seen.</td></tr>
<tr><td>On arrival</td><td>Sample per protocol (after an adequate dwell if the abdomen was dry); cell count, differential, Gram stain and culture; blood cultures if septic</td></tr>
<tr><td>Then</td><td>Ordered antibiotics started without waiting for culture results</td></tr>
</tbody></table></div>
<p>The guideline suggests empiric therapy with either intraperitoneal cefepime alone, or gram-positive coverage plus gram-negative coverage with ceftazidime preferred or an aminoglycoside if ceftazidime is unavailable (9.3, 2D). Children with features of sepsis should receive intravenous antibiotics. The intraperitoneal route is preferred when drug compatibility and stability allow (10.3, not graded). It also suggests nystatin or fluconazole prophylaxis while a child on PD receives antibiotics (7.1, 2D).[[pdn_warady2024]] The nephrologist chooses agents and doses; you prepare and give them exactly as ordered and record the time of the first dose.</p>
{{key:Screen for sepsis, keep the bag, sample correctly, then antibiotics without delay. Time the first dose and write it down.}}
"""),
        ("exit-site-and-tunnel", "Exit site and tunnel", "Exit-site and tunnel infection", """
<p>Purulent discharge at the catheter&ndash;skin junction defines an exit-site infection; a positive culture is not required (19.4, 2C). A tunnel infection shows redness, swelling and tenderness along the subcutaneous catheter path, and ultrasound may help (19.5, 2C). An infection within 30 days of insertion is called insertion-related.[[pdn_warady2024]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Infection</th><th>Suggested treatment duration</th><th>Grade</th></tr></thead>
<tbody>
<tr><td>Exit-site infection</td><td>7 to 14 days by response and microbiology</td><td>2D</td></tr>
<tr><td><em>Pseudomonas</em> exit-site infection</td><td>At least 3 weeks</td><td>2C</td></tr>
<tr><td>Tunnel infection</td><td>At least 3 weeks</td><td>2C</td></tr>
</tbody></table></div>
<p>Exit-site and tunnel infections can seed peritonitis. Monitor the exit-site score at every visit, teach the family to report discharge, and remind the team at the end of the planned course if the site has not settled. Fungal peritonitis is the clearest catheter-removal indication: the guideline suggests immediate removal when fungal elements are seen in the effluent (14.1, 2D).[[pdn_warady2024]]</p>
{{key:Purulent discharge is infection. Tunnel signs and Pseudomonas mean longer treatment and closer watching.}}
"""),
        ("benchmarks-and-prevention", "Benchmarks", "Program benchmarks and prevention", """
<p>The guideline sets program benchmarks (22.6, not graded): an overall peritonitis rate of no more than 0.4 episodes per year at risk, culture-negative peritonitis under 15% of episodes, and peritonitis within 30 days of catheter insertion after fewer than 5% of insertions. It also asks for an apparent cause analysis after every episode (22.5).[[pdn_warady2024]] For context, the SCOPE collaborative reported 0.40 in children under 2 years, and IPPN an annualized 0.32 in older children, as cited in the guideline.</p>
{{formula:Peritonitis rate (episodes per patient-year) = episodes &divide; (patient-months at risk &divide; 12)<br>Example: 3 episodes over 96 patient-months &rarr; 3 &divide; 8 = 0.375 per patient-year}}
<p>A high culture-negative share usually points to sampling and laboratory technique, not to an unusual disease. Prevention rests on what earlier modules taught: training and retraining (Module 18), exit-site care (Module 8), clean exchanges and honest reporting of contamination (Module 9), and audited bundles (Module 5).[[pdn_neu2016]]</p>
{{key:Count every episode, divide by time at risk, and investigate each one. The benchmark is 0.4 or fewer per patient-year.}}
"""),
    ],
    "debrief": ["""
<p><strong>First question.</strong> Rina screens for sepsis: drowsiness, fast breathing, cold or mottled skin, repeated vomiting, poor urine. Any of these means emergency transport now.</p>
<p><strong>The bag and the sample.</strong> Keep the bag closed and upright, note its drain time, and bring it. Because Paolo has a dry day, the team instills a fill and waits at least 2 hours, or samples the night effluent per protocol, so the count is valid.</p>
<p><strong>Antibiotics.</strong> As soon as the specimens are taken, per the nephrologist&rsquo;s order, intraperitoneally unless he is septic. Rina documents call time, arrival, sample time and first-dose time, and the team later completes an apparent cause analysis.</p>
"""],
    "skills": {"title": "The cloudy-bag response", "intro": "Simulate the telephone call and the arrival.",
               "items": [("Screens for sepsis by telephone and routes emergency care when present", True),
                         ("Instructs the family to keep and bring the bag and records its drain time", False),
                         ("Arranges sampling after an adequate dwell for a child with a dry day", True),
                         ("Gives SBAR to the nephrologist with read-back of orders", False),
                         ("Records the time of specimen collection and first antibiotic dose", True)]},
    "quiz": [
        ('ISPD 2024 pediatric empiric diagnosis needs at least how many of the four criteria?',
         ['One', 'Three', 'All four', 'Two'], 3,
         'Statement 8.2, not graded.'),
        ('The effluent white cell threshold in the criteria is:',
         ['Above 100/mm&sup3;', 'Above 10/mm&sup3;', 'Above 1,000/mm&sup3;', 'Any number'], 0,
         'With at least 50% neutrophils as a separate criterion.'),
        ('A child on APD with a dry day needs, before sampling:',
         ['Nothing', 'A fill instilled for at least 2 hours', 'Antibiotics first', 'Imaging'], 1,
         'So that cells accumulate.'),
        ('Antibiotics should start:',
         ['After culture results', 'Next day', 'As soon as possible after appropriate specimens', 'Only if fever'], 2,
         'Statement 9.1, not graded.'),
        ('Which is a suggested empiric regimen (9.3, 2D)?',
         ['Oral amoxicillin', 'No antibiotics', 'Antifungal only', 'IP cefepime monotherapy'], 3,
         'Or gram-positive plus gram-negative coverage.'),
        ('A child with peritonitis and features of sepsis should receive:',
         ['Intravenous antibiotics', 'IP antibiotics only', 'Oral antibiotics', 'Nothing until cultures'], 0,
         'Per the 2024 guideline.'),
        ('While on antibiotics, ISPD 2024 suggests:',
         ['Nothing extra', 'Nystatin or fluconazole prophylaxis (7.1, 2D)', 'Steroids', 'Stopping PD'], 1,
         'Antifungal cover for the antibiotic course.'),
        ('Which alone defines an exit-site infection?',
         ['Redness', 'Itch', 'Purulent discharge', 'Crust'], 2,
         '19.4, 2C.'),
        ('Suggested duration for a tunnel infection:',
         ['3 days', '7 days', 'No treatment', 'At least 3 weeks'], 3,
         '20.6, 2C.'),
        ('Fungal elements in the effluent:',
         ['Immediate catheter removal suggested (14.1, 2D)', 'Watch and wait', 'Oral antifungal only', 'Ignore'], 0,
         'The clearest removal indication.'),
        ('ISPD 2024 pediatric benchmark for overall peritonitis:',
         ['1.0', 'No more than 0.4 episodes per year at risk', '0.1', 'None'], 1,
         '22.6, not graded.'),
        ('Culture-negative peritonitis should be under:',
         ['5%', '40%', '15%', '60%'], 2,
         'A higher share points to sampling or lab technique.'),
        ('3 episodes over 96 patient-months equals:',
         ['0.031', '3.0', '32', '0.375 per patient-year'], 3,
         '96 &divide; 12 = 8 years; 3 &divide; 8.'),
        ('A toddler with peritonitis may show:',
         ['Irritability, vomiting, poor feeding, a tense abdomen', 'Only cloudy fluid', 'Nothing', 'Better appetite'], 0,
         'Young children may not report pain.'),
        ('After every peritonitis episode, ISPD 2024 asks for:',
         ['Nothing', 'An apparent cause analysis', 'A new catheter', 'A modality change'], 1,
         '22.5, not graded.'),
    ],
    "terms": [("Peritonitis", "Infection or inflammation of the peritoneum."),
              ("Effluent cell count", "White cells per mm&sup3; in drained fluid, with the neutrophil share."),
              ("Intraperitoneal antibiotic", "An antibiotic added to the dialysate."),
              ("Refractory peritonitis", "Persistently cloudy fluid or count above 100/mm&sup3; after 5 days of appropriate antibiotics."),
              ("Tunnel infection", "Redness, swelling and tenderness along the catheter&rsquo;s path under the skin."),
              ("Apparent cause analysis", "A structured review of how an infection probably happened.")],
    "readings": [("peritoneal-dialysis-ckd.html", "Peritoneal dialysis for families."),
                 ("antibiotic-stewardship-dialysis.html", "Antibiotic stewardship in dialysis.")],
    "calcs": ["calc-pediatric-dialysis-nurse-toolkit.html", "calc-access-infection-rate.html"],
}
