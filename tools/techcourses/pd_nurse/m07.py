# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 07: Peritonitis: recognition, sampling, escalation and prevention.
Rewritten in the Renal Care Academy POD voice, with illustrative scenarios. Every patient and nurse is fictional. Edit here."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Explain how peritonitis develops through the intraluminal, periluminal, transmural (enteric) and hematogenous routes, and what each implies for prevention.",
        "Apply the 2022 International Society for Peritoneal Dialysis (ISPD) diagnostic criteria to understand the team&rsquo;s assessment, including the short-dwell caveat in automated peritoneal dialysis (APD).",
        "Activate the PD pathway on suspicion, screen for instability, and coordinate effluent sampling so that culture-negative results stay rare.",
        "Use the 2022 ISPD outcome definitions (refractory, relapsing, recurrent, repeat, catheter-related, enteric, pre-PD) in follow-up documentation.",
        "Lead post-episode prevention: technique review, retraining and modifiable risk factors.",
    ],
    "big": """
<p>Peritonitis is the complication that most often ends peritoneal dialysis (PD). It drives hospitalization, catheter removal, transfer to hemodialysis and, in severe or fungal cases, death. In the Peritoneal Dialysis Outcomes and Practice Patterns Study (PDOPPS), an international cohort of 7,051 adults, the crude rate was 0.28 episodes per patient-year, and one facility in ten exceeded 0.50.[[pd_perl2020]]</p>
<p>Most episodes respond to prompt antibiotics. The difference between a cured episode and a lost catheter is often measured in hours: how fast the patient calls, how fast the sample is taken, how fast treatment starts. Your work is to make those hours short, and then to find out why the episode happened so the next one does not.</p>
{{plain:Think of the peritoneal cavity as a sealed, warm room stocked with sugar. Bacteria that get in have food and time.}}
<p>The picture has a limit. The peritoneum is not passive. It has resident macrophages and recruits neutrophils within hours. That is why effluent turns cloudy: cloudiness is the body&rsquo;s defense made visible, white cells by the billions. It is the alarm, not the damage itself. The damage comes when the defense is overwhelmed, the organism is hard to kill, or treatment starts late.</p>
{{cards:Key terms for this module|Cloudy effluent::Drained fluid you cannot read print through; possible peritonitis until proven otherwise.|Cell count and differential::The number of white cells in the effluent and the share that are neutrophils.|Culture-negative::An episode in which no organism grows; often a sign of sampling problems.|Enteric peritonitis::Peritonitis arising from the bowel.|SBAR::Situation, Background, Assessment, Recommendation: a structured handoff.}}
""",
    "case": {"title": "Coconut milk at 6:40 AM", "html": """
<p><strong>Lola Aida, 74</strong>, on APD, assisted by her granddaughter <strong>Mika</strong>, lives in Tarlac City. Nurse <strong>Ramon</strong> is on call for the PD unit.</p>
<p><strong>6:40 AM.</strong> Mika calls. The drain bag &ldquo;looks like <em>gata</em>&rdquo;, coconut milk. Lola Aida has chills and mild abdominal discomfort. No vomiting. She is alert and talking. Mika asks whether she should just throw the bag away and connect the day bag as usual.</p>
""", "questions": ["Is this peritonitis until proven otherwise?",
                  "What do you screen for in the first five minutes?",
                  "What must be in your handoff before you hang up?"]},
    "sections": [
        ("the-physiology", "The physiology", "The physiology: how bacteria get in", """
<p>Every episode has a route. Knowing the route tells you where prevention failed, and often which organisms to expect.</p>
<div class="table-wrap"><table>
<thead><tr><th>Route</th><th>How</th><th>Typical organisms</th><th>Prevention focus</th></tr></thead>
<tbody>
<tr><td>Intraluminal (touch)</td><td>Contamination at connection</td><td>Skin flora, coagulase-negative staphylococci</td><td>Technique, flush before fill, contamination response (Module 4)</td></tr>
<tr><td>Periluminal</td><td>Along the outside of the catheter from an infected exit site or tunnel</td><td><em>S. aureus</em>, <em>P. aeruginosa</em></td><td>Exit-site care (Module 3)</td></tr>
<tr><td>Transmural (enteric)</td><td>Across the bowel wall in constipation, diverticulitis or colitis</td><td>Gram-negative rods, mixed bowel flora, anaerobes</td><td>Bowel care, correcting low potassium, antibiotic prophylaxis before invasive procedures</td></tr>
<tr><td>Hematogenous or ascending</td><td>Bloodstream or gynecologic</td><td>Streptococci, others</td><td>Procedure prophylaxis</td></tr>
</tbody></table></div>
{{fig:pd07_routes}}
<h3>Why the abdomen hurts, and why it sometimes does not</h3>
<p>Inflammation of the peritoneum lining the abdominal wall stimulates pain fibers. Pain can be absent early, especially in APD, where short dwells dilute the signal, and in older or diabetic patients. That is why cloudy effluent without pain still counts.</p>
<h3>Why ultrafiltration falls</h3>
<p>Inflammation widens the blood vessels under the membrane and makes them leakier. Glucose is absorbed faster, the osmotic gradient fades faster, and ultrafiltration (UF) falls. Patients may become fluid overloaded during an episode. Protein loss into the effluent rises, which is one reason appetite and nutrition need attention afterward.</p>
<h3>Example: three episodes, three routes</h3>
<div class="table-wrap"><table>
<thead><tr><th>Patient</th><th>What happened before</th><th>Organism</th><th>Most likely route</th></tr></thead>
<tbody>
<tr><td>Mr. Lito</td><td>Rushed exchange before a 6 AM jeepney trip; admits he may have touched the connector</td><td>Coagulase-negative staphylococcus</td><td>Intraluminal</td></tr>
<tr><td>Mrs. Perla</td><td>Exit-site infection treated last month, same organism</td><td><em>S. aureus</em></td><td>Periluminal; catheter-related</td></tr>
<tr><td>Mang Isko</td><td>Five days without a bowel movement; low potassium on last labs</td><td>Mixed gram-negative organisms</td><td>Transmural (enteric)</td></tr>
</tbody></table></div>
{{key:Every episode has a route. Name it, because prevention depends on it.}}
"""),
        ("diagnosis-ispd-2022", "Diagnosis", "Diagnosis (ISPD 2022)", """
<p>The 2022 ISPD recommendations diagnose peritonitis when at least two of the following are present (GRADE 1C):[[pd_li2022]]</p>
<ol>
<li>Clinical features consistent with peritonitis: abdominal pain and/or cloudy dialysis effluent.</li>
<li>Dialysis effluent white cell count above 100/&micro;L (above 0.1 &times; 10&#8313;/L) after a dwell of at least 2 hours, with more than 50% polymorphonuclear leukocytes.</li>
<li>Positive dialysis effluent culture.</li>
</ol>
<h3>Short APD dwells</h3>
<p>Because cycler dwells are short, the absolute white cell count may be lower than 100/&micro;L even during real peritonitis. The proportion of polymorphonuclear cells above 50% remains meaningful.[[pd_li2022]] That is why you always record the dwell duration with the sample. A count of 80/&micro;L with 85% neutrophils after a 90-minute cycler dwell means something very different from the same count after an 8-hour dwell.</p>
<h3>Not all cloudy effluent is infection</h3>
<p>Other causes include chemical irritation, eosinophilic effluent (often early after insertion), chylous effluent (milky, lipid-rich), hemoperitoneum (blood-tinged, for example during menstruation), malignancy, and reactions to some solutions or medicines. The team sorts these out.</p>
<h3>Example: cloudy, but not what it seems</h3>
<p>Ms. Andrea, 31, calls because her morning bag is pink and hazy. It is the second day of her period, she has no pain and no fever, and this happened last month too. It may well be menstrual blood. But that is the team&rsquo;s conclusion to reach, not hers or yours. You arrange same-day assessment so the effluent can be examined. If it is blood alone, she has learned how to report it. If it is not, she was treated early.</p>
{{key:Treat every cloudy bag as possible peritonitis until the team says otherwise.}}
{{fig:pd07_fig_07_peritonitis_diagnosis_two_of_three}}
"""),
        ("what-you-do", "The first hour", "What you do: the first hour", """
{{fig:pd07_hour}}
<p>On the call or at the bedside, work through these steps in order.</p>
<ol>
<li><strong>Recognize and activate.</strong> Cloudy effluent, with or without pain, means immediate PD team contact.</li>
<li><strong>Screen for instability.</strong> Fever with rigors, low blood pressure, confusion, severe pain, vomiting that prevents eating and drinking, rapid breathing. Use emergency services or the emergency department per the local pathway.</li>
<li><strong>Gather the facts.</strong> Onset; last exchange and dwell length; recent contamination or breach; exit-site changes; constipation or diarrhea; recent procedures (colonoscopy, dental, gynecologic); recent antibiotics; allergies; prior episodes and organisms.</li>
<li><strong>Preserve the effluent.</strong> Instruct the patient to keep the cloudy bag, closed and labeled, and bring it, or follow the program&rsquo;s instructions for the first bag. If the patient arrives with a dry abdomen, for example on APD with no day dwell, the unit protocol may call for a fill and a short dwell before sampling.</li>
<li><strong>Coordinate sampling.</strong> Cell count and differential, Gram stain and culture, per protocol. Inoculating effluent into blood-culture bottles is the preferred culture technique in ISPD guidance; follow your laboratory&rsquo;s exact volumes and transport times. Label with dwell duration and collection time.[[pd_li2022]]</li>
<li><strong>Do not delay treatment.</strong> Empirical antibiotics, usually intraperitoneal, covering both gram-positive and gram-negative organisms, should start as soon as possible after specimens are taken. Collection before antibiotics is preferred when feasible, but it must not delay urgent care. Antibiotic choice and dose are the prescriber&rsquo;s; administration follows the written order or standing protocol.[[pd_li2022]]</li>
<li><strong>Close the loop.</strong> SBAR to the accepting clinician, read-back, time stamp, disposition (admit, treat at home with a return visit, or emergency) and who will follow the culture.</li>
</ol>
<h3>Example: the patient who is three hours away</h3>
<p>Mr. Edgar lives in a mountain barangay in Benguet, three hours by jeepney from the PD unit. He calls at 5 PM with a cloudy bag and mild pain. The last trip down the mountain has left.</p>
<p>Nurse Liza screens him: no fever, no vomiting, alert, able to drink. She calls the nephrologist with SBAR. The program has a written plan for remote patients. Under it, he goes to the nearest district hospital that evening, where a sample can be taken and the first ordered dose given under the nephrologist&rsquo;s instructions, and he travels to the PD unit in the morning. Liza tells him to keep the bag cold and closed, and to go straight to emergency if he becomes faint, confused or cannot keep fluids down. She documents the times, the plan and who will call the district hospital.</p>
<p>The plan existed before the call. That is the point: for patients far from the unit, the first hour is designed in advance, not improvised.</p>
{{call:Contact the PD team immediately for any cloudy effluent. Use emergency services for confusion, fainting, low blood pressure, rigors or uncontrolled vomiting. Never let sampling delay treatment for an unstable patient.}}
"""),
        ("program-quality-markers", "Quality markers", "Program quality markers (ISPD 2022)", """
<div class="table-wrap"><table>
<thead><tr><th>Marker</th><th>2022 target</th></tr></thead>
<tbody>
<tr><td>Overall peritonitis rate</td><td>No more than 0.40 episodes per year at risk</td></tr>
<tr><td>Patients free of peritonitis per year</td><td>More than 80%</td></tr>
<tr><td>Culture-negative episodes</td><td>Less than 15% of all episodes (GRADE 1C)</td></tr>
</tbody></table></div>
<p>These targets come from the 2022 ISPD recommendations.[[pd_li2022]] A culture-negative rate above 15% usually points to sampling or laboratory problems, or to antibiotics given before sampling. Nurses control much of that.</p>
<p>PDOPPS country rates ranged from 0.26 episodes per patient-year in the United States to 0.40 in Thailand. Thailand had more gram-negative and culture-negative episodes.[[pd_perl2020]] Compare Philippine program data with these figures carefully, because definitions and case-finding differ.</p>
<h3>Example: a culture-negative problem</h3>
<p>A unit reviews its year. Of 18 peritonitis episodes, 5 grew nothing: 28%. The head nurse traces each one. Three samples sat at room temperature over a weekend before reaching the laboratory. One was taken after the first antibiotic dose. One was sent in a plain sterile cup instead of blood-culture bottles. None of these is a microbiology mystery. The fix is a weekend transport arrangement, a sampling checklist taped to the PD room door, and bottles kept in stock.</p>
{{key:A high culture-negative rate is usually a process problem. Fix the sampling before you blame the bacteria.}}
"""),
        ("follow-through-and", "Follow-through", "Follow-through and outcome definitions", """
<p>The 2022 update revised and clarified these definitions. Use them in documentation so episodes are counted consistently.[[pd_li2022]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Term</th><th>Meaning</th></tr></thead>
<tbody>
<tr><td>Refractory</td><td>Failure of the effluent to clear after 5 days of appropriate antibiotics. The 2022 update allows expectant management beyond day 5 if the effluent white cell count is falling toward normal, rather than mandatory catheter removal.</td></tr>
<tr><td>Relapsing</td><td>An episode within 4 weeks of completing therapy for a prior episode, with the same organism or one sterile episode</td></tr>
<tr><td>Recurrent</td><td>An episode within 4 weeks of completing therapy, with a different organism</td></tr>
<tr><td>Repeat</td><td>An episode more than 4 weeks after completing therapy, with the same organism</td></tr>
<tr><td>Catheter-related</td><td>Peritonitis with an exit-site or tunnel infection with the same organism (or one site sterile)</td></tr>
<tr><td>Enteric</td><td>Peritonitis arising from an intestinal source (inflammation, perforation or ischemia)</td></tr>
<tr><td>Pre-PD</td><td>Peritonitis after catheter insertion but before PD training or treatment begins</td></tr>
<tr><td>Medical cure</td><td>Resolution without complications such as relapse, catheter removal, hemodialysis transfer or death</td></tr>
</tbody></table></div>
<h3>Example: classify the second episode</h3>
<div class="table-wrap"><table>
<thead><tr><th>First episode</th><th>Second episode</th><th>Term</th></tr></thead>
<tbody>
<tr><td><em>S. aureus</em>, treatment finished March 1</td><td><em>S. aureus</em>, March 20</td><td>Relapsing</td></tr>
<tr><td><em>S. aureus</em>, treatment finished March 1</td><td><em>E. coli</em>, March 20</td><td>Recurrent</td></tr>
<tr><td><em>S. aureus</em>, treatment finished March 1</td><td><em>S. aureus</em>, May 15</td><td>Repeat</td></tr>
</tbody></table></div>
<h3>Nursing follow-through</h3>
<p>Repeat cell counts as ordered. Track the culture and sensitivities. Confirm the antibiotic course is completed. Watch UF and weight during the episode, because UF often falls. Watch for hearing changes if aminoglycosides are used; the 2022 update added a recommendation on adjunctive oral N-acetylcysteine to reduce aminoglycoside ototoxicity, a prescriber decision. Confirm antifungal prophylaxis whenever antibiotics are given, if the program uses it.[[pd_li2022]]</p>
<p>Ask the patient directly about ringing in the ears, muffled hearing or unsteadiness, because many will not mention them unprompted.</p>
{{fig:pd07_fig_07_relapsing_recurrent_repeat_timeline}}
"""),
        ("prevention-after-every", "Prevention", "Prevention after every episode", """
<p>Every episode is a signal. Review it as a team, without blame, within days of the episode.</p>
<ul>
<li><strong>Root cause.</strong> Which route? Touch, exit site, bowel, procedure?</li>
<li><strong>Technique.</strong> Observe a full exchange. The 2022 ISPD update revised its recommendations on training and reassessment; retraining after peritonitis is standard practice.[[pd_li2022]]</li>
<li><strong>Modifiable risk factors named in 2022:</strong> domestic pets in the exchange area, low potassium, and histamine-2 receptor antagonist use.[[pd_li2022]] Report these to the prescriber; do not change medicines yourself.</li>
<li><strong>Procedures.</strong> Antibiotic prophylaxis before invasive procedures such as colonoscopy or gynecologic procedures, and emptying the abdomen beforehand, per the revised recommendations and the prescriber&rsquo;s order.[[pd_li2022]]</li>
</ul>
<h3>Example: a review that found three things</h3>
<p>After Mang Isko&rsquo;s enteric episode, Nurse Ramon visits and watches a full exchange. Technique is fine. But Mang Isko has been taking an over-the-counter acid reducer from the sari-sari store for heartburn, his last potassium was low, and he goes days without a bowel movement because he avoids vegetables &ldquo;for the kidneys.&rdquo; Ramon reports the acid reducer and the potassium to the nephrologist, asks the dietitian to review fiber within his potassium limits, and teaches him to call when he has gone three days without a bowel movement. None of these would have surfaced from the culture result alone.</p>
{{key:Every cloudy bag gets a call. Every episode gets a review.}}
"""),
    ],
    "debrief": ["""
<p><strong>Is it peritonitis until proven otherwise?</strong> Yes. Cloudy effluent with chills and discomfort meets the clinical feature criterion. Ramon tells Mika not to throw the bag away and not to connect the day bag until the team says so.</p>
<p><strong>6:45 AM, the five-minute screen.</strong> Ramon checks for instability: temperature 38.2 &deg;C on their thermometer, no confusion, no dizziness on standing, pulse 96 by Mika&rsquo;s count. Last night&rsquo;s cycler dwell was about 1 hour 30 minutes. No known contamination. Exit site dry. Last bowel movement three days ago. No recent procedures. No known allergies.</p>
<p><strong>6:52 AM, the handoff.</strong> Ramon activates the PD pathway and calls the nephrologist on duty. Situation: cloudy effluent, chills, fever 38.2 &deg;C, stable by home assessment. Background: 74, APD, assisted by her granddaughter, no prior peritonitis. Assessment: suspected peritonitis; short APD dwell, to be recorded for the cell count; possible constipation. Recommendation: same-morning assessment at the PD unit for sampling and empirical treatment; emergency department if she becomes unstable before arrival.</p>
<p><strong>6:58 AM.</strong> The nephrologist accepts. Ramon reads back the plan. He tells Mika to clamp and bring the drain bag, or a sample per protocol, to bring Lola&rsquo;s medicines, and to call 911 or go to the nearest emergency department if Lola becomes confused, faint or breathless on the way.</p>
<p><strong>8:10 AM.</strong> At the unit, samples are sent, labeled with dwell duration and collection time. Empirical intraperitoneal antibiotics start per order at 8:25. Ramon documents the times from call to sample to first dose, the accepting clinician and who will review the culture at 48 hours. He schedules a technique review with Mika after the episode, and a bowel plan.</p>
"""],
    "skills": {"title": "Cloudy bag with pain (OSCE station 3)",
               "intro": "Run a timed mock call. Deliver SBAR, document read-back, disposition and time stamps. Faculty scores against OSCE station 3 in the faculty assessment.",
               "items": [("Recognizes urgency and activates the PD pathway.", True),
                         ("Checks for systemic instability and routes emergency care as indicated.", True),
                         ("Preserves the specimen and coordinates timely sampling under protocol.", False),
                         ("Relays SBAR and obtains read-back.", False),
                         ("Time-stamps contact and disposition.", False)]},
    "quiz": [
        ("A patient feels well but reports cloudy effluent. What is the response?",
         ["Activate urgent PD assessment, screen for instability and arrange sampling", "Wait to see if it clears", "Drink more water", "Skip the next exchange"], 0,
         "Cloudy effluent without pain still counts, especially in APD and in older or diabetic patients."),
        ("How many of the three ISPD 2022 criteria are needed to diagnose peritonitis?",
         ["One", "All three", "At least two", "None; diagnosis is clinical only"], 2,
         "At least two of three: clinical features, the cell count criterion and a positive culture."),
        ("Which effluent result meets the cell-count criterion after a dwell of at least 2 hours?",
         ["White cells above 10/&micro;L with any differential", "Red cells above 100/&micro;L", "Lymphocytes above 50%", "White cells above 100/&micro;L with more than 50% polymorphonuclear cells"], 3,
         "That is the 2022 criterion. Red cells and lymphocytes do not meet it."),
        ("Why record dwell duration with the sample?",
         ["For billing", "Short APD dwells may give a lower absolute count; the differential remains meaningful", "It determines the antibiotic", "It is not needed"], 1,
         "The same count means different things after a 90-minute and an 8-hour dwell."),
        ("What is the ISPD 2022 target for culture-negative peritonitis?",
         ["Less than 50%", "Less than 15% of episodes", "Less than 1%", "No target"], 1,
         "Less than 15% (GRADE 1C). Higher rates usually point to sampling problems."),
        ("Sampling before antibiotics is preferred. What if the patient is septic and sampling is delayed?",
         ["Delay treatment until sampling", "Skip sampling entirely", "Send the patient home", "Do not delay urgent care; coordinate sampling as quickly as possible"], 3,
         "Treatment must not wait for an unstable patient."),
        ("Mang Isko had five days without a bowel movement and grows mixed gram-negative organisms. Which route fits?",
         ["Transmural from the bowel", "Intraluminal touch", "Periluminal from the exit site", "Hematogenous from the skin"], 0,
         "Constipation and mixed bowel organisms suggest enteric peritonitis."),
        ("<em>S. aureus</em> peritonitis 19 days after finishing treatment for <em>S. aureus</em> peritonitis is:",
         ["Recurrent", "Repeat", "Relapsing", "Refractory"], 2,
         "Same organism, within 4 weeks of completing therapy."),
        ("<em>E. coli</em> peritonitis 19 days after finishing treatment for <em>S. aureus</em> peritonitis is:",
         ["Relapsing", "Repeat", "Recurrent", "Pre-PD"], 2,
         "Different organism, within 4 weeks."),
        ("What did the 2022 update change about refractory peritonitis?",
         ["Expectant management beyond day 5 may be considered if the effluent white cell count is falling toward normal", "Catheter removal is now required on day 2", "Refractory peritonitis no longer exists", "Antibiotics are no longer used"], 0,
         "A falling count beyond day 5 allows watchful management rather than mandatory removal."),
        ("Which is a modifiable peritonitis risk factor named in the 2022 ISPD update?",
         ["Blood type", "Low potassium", "Height", "Eye color"], 1,
         "Along with pets in the exchange area and histamine-2 receptor antagonist use."),
        ("A unit finds 5 of 18 episodes culture-negative; three samples sat over a weekend. What is the best interpretation?",
         ["The organisms are unusual", "A sampling and transport process problem", "The laboratory is always wrong", "Nothing can be done"], 1,
         "28% is above the target. Transport delays, late sampling and wrong containers are fixable process problems."),
        ("Why does UF often fall during peritonitis?",
         ["Antibiotics block water", "The catheter is removed", "Patients drink less", "Inflammation increases membrane permeability and glucose absorption, so the osmotic gradient fades"], 3,
         "An inflamed membrane absorbs glucose faster. Watch weight and UF during the episode."),
        ("Ms. Andrea&rsquo;s bag is pink and hazy on day 2 of her period, with no pain or fever. What should happen?",
         ["Ignore it because it is menstrual", "Report it; the team decides whether it is blood alone or infection", "Give antibiotics yourself", "Flush until clear"], 1,
         "Treat it as possible peritonitis until the team decides."),
        ("Which element makes a peritonitis handoff closed-loop?",
         ["Sending an email", "Telling the patient to wait", "Accepting clinician named, read-back, time stamp, disposition and a named person to follow the culture", "Writing &ldquo;endorsed&rdquo;"], 2,
         "Closing the loop means someone has accepted the plan, and someone will follow the result."),
    ],
    "terms": [("Peritoneal dialysis (PD)", "Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter."),
              ("APD", "Automated peritoneal dialysis: a cycler performs exchanges, usually overnight."),
              ("Dwell", "The time dialysis solution stays in the abdomen between fill and drain."),
              ("Ultrafiltration (UF)", "Fluid removed by dialysis; net UF is drained volume minus instilled volume."),
              ("Exit site", "The point where the PD catheter leaves the skin."),
              ("Tunnel", "The path of the catheter under the skin between the cuffs."),
              ("Tunnel infection", "Inflammation along the catheter tunnel, with or without a fluid collection on ultrasound."),
              ("Flush before fill", "Sending a little fresh solution straight to the drain bag before filling, to wash out bacteria introduced at connection."),
              ("Cycler", "The machine that performs APD exchanges."),
              ("Peritonitis", "Infection or inflammation of the peritoneum, usually shown by cloudy effluent."),
              ("Effluent", "Fluid drained from the abdomen after a dwell."),
              ("Culture-negative peritonitis", "An episode in which no organism grows from the effluent."),
              ("Enteric peritonitis", "Peritonitis arising from the bowel."),
              ("Ototoxicity", "Damage to hearing or balance caused by a medicine."),
              ("SBAR", "Situation, Background, Assessment, Recommendation: a structured handoff.")],
    "readings": [("antibiotic-stewardship-dialysis.html", "Antibiotic stewardship in dialysis units."),
                 ("dialysis-access-infection.html", "Dialysis access infections.")],
    "calcs": ["calc-qapi-run-chart-spc.html"],
}
