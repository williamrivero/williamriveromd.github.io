# -*- coding: utf-8 -*-
"""Physician on Duty, Module 06: Water and Dialysate: The Hidden Half of the Treatment.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician on duty and a water treatment technician in the water room of a Filipino dialysis unit, reading a logbook together beside the reverse osmosis unit.",
    "objectives": [
        "Explain, with arithmetic, why a dialysis patient meets hundreds of liters of water each week, and why contaminants that are harmless to drink can harm that patient.",
        "Describe the water treatment steps in outline, and match each major contaminant to its source and to the illness it causes.",
        "Explain how dialysis fluid is mixed from water and two concentrates, what conductivity measures, and what goes wrong when the mix is wrong.",
        "Recognize a cluster event and carry out the first steps in the order your unit&rsquo;s protocol sets.",
        "Read the water and dialysis fluid records a physician should understand, and name the standards they follow.",
    ],
    "big": """
{{plain:Think of the water you drink as a visitor who must pass three guarded gates before reaching the blood. The gut lining is the first gate. The liver is the second. The kidneys, which throw out whatever slips through, are the third. Dialysis fluid takes a back door. It skips all three gates and meets the blood across one thin membrane.}}
<p>The picture has a limit. The membrane is not a gate that lets nothing through. It is built to let small molecules cross in both directions, because that is how dialysis cleans the blood. Anything small enough in the fluid, such as fluoride, aluminum, or fragments of bacteria, can cross into the blood too. The patient has no working kidneys to clear it afterward.</p>
{{cards:Key terms for this module|Dialysis fluid (dialysate)::The fluid on the other side of the dialyzer membrane. The machine makes it from treated water and two concentrates.|Product water::Water after treatment, ready to make dialysis fluid.|Reverse osmosis (RO)::A very tight membrane filter that rejects most dissolved salts, metals, and microbes.|Chloramine::A disinfectant in many city water supplies. It breaks red blood cells.|Endotoxin::Part of the wall of certain bacteria that triggers fever and inflammation, even from dead bacteria.|Conductivity::How well the fluid carries an electric current. It rises with the amount of dissolved salt, mainly sodium.|Cluster event::Two or more patients with the same new symptom, linked by shift, room, water loop, machine group, or lot of supplies.}}
<p>Most shifts pass without any problem from the water or the dialysis fluid. A few bring one, and it looks like the nausea, headache, chills, or cramps you see every day. Your work is to notice when the same complaint appears in more than one chair, to stop the harm per protocol, and to ask the right questions of the right people.</p>
""",
    "case": {"title": "Everyone on the afternoon shift is nauseated", "html": """
<p>It is 2:50 p.m. on a hot Tuesday in a 14-station unit in Marilao, Bulacan. The afternoon shift started forty minutes ago. Nurse Carmela Reyes calls you to the floor.</p>
<p>Mang Teodoro Santiago, 61, is nauseated and has a headache. So is Aling Pacita Navarro, 55, two stations away. A third patient, Jun-jun Ramos, 38, says his legs are cramping and he feels &ldquo;hot inside.&rdquo; Their blood pressures are 150/90, 146/88, and 162/96 mm Hg. These are illustrative values, not targets. No patient on the morning shift complained.</p>
<p>Two facts come up as you talk. The technician replaced the bicarbonate concentrate supply at the start of the afternoon shift. The water system was serviced yesterday. Nurse Reyes has stopped fluid removal on the first patient and is checking the machines.</p>
""", "questions": ["What makes this a cluster rather than three unrelated complaints?",
                  "Which causes in the water, the concentrate, the machines, or the disposables fit these symptoms, and what would you ask to see?",
                  "What are your first steps in the next 10 minutes, and whom do you call?"]},
    "sections": [
        ("exposure", "How much water", "The hidden half: how much water meets the blood", """
<p>Module 5 followed the blood through the circuit. This module follows the water and the concentrates that become dialysis fluid. You do not run the water system, but when it fails, you may be the first doctor to see the result.</p>
<h3>Three gates, and the one that remains</h3>
<p>In a healthy person, the gut absorbs only part of most metals in drinking water, the liver clears much of what is absorbed, and the kidneys excrete the rest. Each gate lowers the dose that reaches the tissues.</p>
<p>In a dialysis patient, the dialysis fluid bypasses the gut and the liver entirely. Only the membrane separates it from the blood. Small ions such as fluoride move across by diffusion toward the side with less of them. Aluminum crosses too, and once in the blood it binds to plasma proteins, so the free level stays low and more keeps moving in. The kidneys that would have excreted them are gone. What crosses tends to stay and build up.[[daugirdas2015]]</p>
{{fig:pod06_tap_to_dialyzer}}
<p>Bacteria are too large to cross an intact membrane, but small pieces of endotoxin can. High-flux membranes also let some fluid move from the dialysis fluid into the blood, a process called backfiltration.[[daugirdas2015]] Purity matters even when the bacteria stay on the fluid side.</p>
<h3>The volume is the second reason</h3>
<p>The gate is thinner, and the volume is far larger. The arithmetic below shows the scale.</p>
{{formula:<strong>Worked scenario 1. Weekly water exposure (illustrative arithmetic, not a prescription).</strong><br>Formula: dialysis fluid used per session (liters) = dialysis fluid flow (mL per minute) &times; session time (minutes) &divide; 1,000.<br>Illustrative values: 500 mL per minute &times; 240 minutes = 120,000 mL = <strong>120 L per session</strong>.<br>Three sessions a week: 120 L &times; 3 = <strong>360 L per week</strong>.<br>Comparison: a person who drinks 2 L a day drinks 2 &times; 7 = 14 L a week. 360 &divide; 14 &asymp; <strong>26 times</strong> more water meets the blood by dialysis fluid than a person drinks, and the drinking water passes the gut and the liver first.<br>What the number tells you: a concentration trivial in drinking water can deliver a meaningful dose across the membrane. What it does not tell you: how much of any one substance crosses, which depends on its size, its binding, and the gradient.}}
<p>Flow and session length belong to the prescription (Module 7).</p>
<h3>What the record of harm shows</h3>
<p>A review from the Centers for Disease Control and Prevention (CDC) counted at least 592 cases and 16 deaths in the United States since the 1960s from chemical, bacterial, and endotoxin contamination, in outbreaks that still recur.[[coulliette2013]] These are reported outbreaks only, so the true number is likely higher.</p>
{{key:The membrane is the only gate. Whatever is in the water is one membrane away from the blood.}}
"""),
        ("treatment", "The treatment train", "From tap to dialyzer: the water treatment train", """
<p>Picture a line of guards at a series of gates, each catching a different kind of intruder, so that one tired guard does not let everything through. The picture has a limit: a guard who has caught too many intruders stops catching any, without warning. Carbon beds and softeners become exhausted in exactly this way, which is why they are tested and not trusted.</p>
<p>The technician track teaches how to run each step. You need to know what each one removes, so that a symptom in a patient points you to a step in the water room.[[coulliette2013]][[daugirdas2015]]</p>
{{fig:wts_train|The water treatment train, from feed water to the distribution loop. Each step removes a different kind of contaminant.}}
{{cards:The steps and what each removes|Sediment filters::Sand, rust, and particles.|Softener::Calcium and magnesium, which would scale the reverse osmosis membrane.|Carbon beds::Chlorine and chloramine. This step protects red blood cells.|Reverse osmosis (RO)::The main barrier against dissolved salts, metals such as aluminum and fluoride, bacteria, and endotoxin.|Distribution loop::Pipes that carry product water to every station and back, kept moving so bacteria cannot settle.|Point-of-use ultrafilters::In some units, a final filter at each station against bacteria and endotoxin.}}
<h3>Why the carbon step gets daily attention</h3>
<p>Reverse osmosis has one important gap. Chloramine passes through it and through deionization, so it must be removed earlier, by activated carbon. A review of chloramine removal advised two carbon beds in series, so that breakthrough after the first bed is detected before the second one fails. It also advised testing more than once daily, because the chloramine level in city water can change without notice.[[ward1996]]</p>
{{fig:pod06_two_carbon_beds}}
<p>This is why a total chlorine test is done before each shift. Section 6 shows where it is recorded.</p>
<h3>The standards behind the system</h3>
<p>The International Organization for Standardization (ISO) publishes the ISO 23500 series on fluids for dialysis. Part 1, in its second edition of 2024, sets the general requirements and replaced the 2019 edition.[[iso23500_1_2024]] Part 3 sets the minimum chemical and microbiological quality of water used to make dialysis fluid and concentrates, and gives guidance on monitoring.[[iso23500_3_2024]] Part 5 sets the minimum chemical and microbiological quality of the dialysis fluid itself.[[iso23500_5_2024]] These are standards, not graded clinical recommendations. ISO has marked Parts 3 and 5 for revision, so check which edition your unit&rsquo;s policy cites. Earlier European guidance on dialysis fluid purity preceded them.[[ebpg_purity2002]]</p>
{{fig:wts_tiers|Three tiers of purity: water for dialysis, standard dialysis fluid, and ultrapure dialysis fluid. Each tier has its own limits in the standards.}}
<p>This module does not print chemical or microbial limits. The limits that apply are those in your unit&rsquo;s water-quality policy, taken from the edition the unit and its regulator have adopted. Ask to see it in your first week.</p>
<p>Source water changes the design. City water usually carries chlorine or chloramine. Deep-well water may carry more iron and hardness, and no disinfectant. The site&rsquo;s self-assessment, carbon tank contact-time, and capacity calculators show the checks a technician works through.</p>
<h3>What the physician on duty does</h3>
<p>Before your first shift ends, know where the water room is, who the responsible technician is and how to reach them, and where today&rsquo;s chlorine check is written. You will rarely need them, and then within minutes.</p>
{{key:Each step catches one kind of contaminant. When a patient shows the calling card of that contaminant, ask about that step.}}
"""),
        ("contaminants", "Contaminants", "What goes wrong: contaminants and the illnesses they cause", """
<p>Think of the contaminants as a rogues&rsquo; gallery. Each one leaves a calling card that you can recognize at the chair. The picture has a limit. Calling cards overlap, and the same card can come from a cause outside the water. Use the gallery to choose your first question, not to make a diagnosis.</p>
<p>The evidence here comes from outbreak investigations. They are observational, from other countries and decades, and rarely give a precise dose. The mechanisms they point to are established.</p>
<h3>Chloramine: the red cell breaker</h3>
<p>Chloramine is an oxidant. In the blood it damages hemoglobin and the red cell membrane, and the damaged cells break, which is hemolysis.[[daugirdas2015]] In one outbreak, the carbon filter in a recently modified water system failed. Forty-one patients needed transfusion for hemolytic anemia. The unit&rsquo;s death rate rose in the following months, although no death could be attributed to the exposure.[[tipple1991]] Copper released from pipes by acidic water can break red cells too. Nitrates in well water can turn hemoglobin into methemoglobin, a form that cannot carry oxygen.[[coulliette2013]][[greenberg2021]]</p>
<h3>Aluminum: the brain</h3>
<p>At autopsy, dialysis patients who had died of an unexplained neurologic syndrome had brain gray-matter aluminum of 25 parts per million. Dialysis patients who died of other causes had 6.5, and controls 2.2.[[alfrey1976]] These patients had also taken aluminum-containing phosphate binders, so the study does not say how much came from the water. This small tissue comparison suggested, without proving, that the syndrome was aluminum intoxication. A later outbreak supports the link. In Cura&ccedil;ao, distilled seawater ran through a new pipe lined with cement mortar, and aluminum leached into the dialysis water. Of 27 patients with similar exposure, 10 died of acute aluminum encephalopathy. Those who died were older, lighter, and had lower serum albumin.[[berend2001]] </p>
<h3>Fluoride: the itch and the heart</h3>
<p>A temporary deionization system in one room of a university unit took up fluoride and then released it in a burst. Over five shifts, 12 of 15 patients in that room became acutely ill, with severe itching, many nonspecific symptoms, or fatal ventricular fibrillation in 3. None of 17 patients in the adjacent room became ill.[[arnow1994]] </p>
<h3>Cyanobacterial toxins: the liver</h3>
<p>At a center in Caruaru, Brazil, in 1996, water from a reservoir reached the unit without treatment, filtering, or chlorination. Toxins made by cyanobacteria, called microcystins, were found in the water and in patients&rsquo; blood and liver. Of 130 patients, 116 had visual disturbance, nausea, and vomiting; 101 met the case definition of acute liver failure, and 50 died.[[jochimsen1998]] </p>
<h3>Bacteria and endotoxin: fever and slow inflammation</h3>
<p>Bacteria grow in water loops, in stagnant branches, and in bicarbonate concentrate. Their fragments cause a pyrogenic reaction: chills, fever, and sometimes low blood pressure, often within the first hour of the session.[[daugirdas2015]][[greenberg2021]] Module 17 covers fever and bloodstream infection. Low-grade contamination may add to chronic inflammation without ever causing fever.</p>
<p>The standard endotoxin test, the Limulus amebocyte lysate (LAL) test, detects intact endotoxin. In 269 samples tested with a cell assay that also responds to smaller bacterial fragments, 10.3% of samples meeting the European definition of pure fluid, and 9.1% of those meeting the ultrapure definition, still provoked an inflammatory response.[[glorieux2009]] This laboratory study shows that the standard test misses some inflammatory material. It does not show that this material harms patients.</p>
<div class="table-wrap"><table>
<thead><tr><th>Contaminant</th><th>Where it comes from</th><th>What the patient shows</th><th>First question to the technician</th></tr></thead>
<tbody>
<tr><td>Chloramine</td><td>City water, exhausted or bypassed carbon</td><td>Hemolysis: new anemia, back or chest pain, pink or red plasma</td><td>What was today&rsquo;s total chlorine result, and when was it taken?</td></tr>
<tr><td>Copper, nitrates</td><td>Copper pipes or fittings, source water</td><td>Hemolysis, nausea; with nitrates, bluish skin from methemoglobin</td><td>Has any pipe, fitting, or source changed?</td></tr>
<tr><td>Aluminum</td><td>Source water, pipes, failed reverse osmosis</td><td>Confusion, speech change, jerks, seizures</td><td>How is the reverse osmosis rejection trending?</td></tr>
<tr><td>Fluoride</td><td>Source water, exhausted deionization</td><td>Severe itching, nausea, arrhythmia</td><td>Was a deionizer or temporary system used?</td></tr>
<tr><td>Bacteria, endotoxin</td><td>Loop, dead legs, bicarbonate concentrate</td><td>Chills and fever early in the session</td><td>When was the last disinfection and culture?</td></tr>
<tr><td>Cyanobacterial toxins</td><td>Untreated surface water</td><td>Vomiting, visual change, liver failure</td><td>Is the source water treated before it reaches us?</td></tr>
</tbody></table></div>
<h3>A cluster is not always the water</h3>
<p>In May 1998, 30 patients in three states of the United States developed hemolysis during dialysis. Twenty had high blood pressure and 18 had abdominal pain. Ten needed intensive care, and two died. The only common factor was one lot of blood tubing with a narrowed opening that damaged red cells as they were pumped through it.[[duffy2000]] The water was sound. A cluster investigation checks the lot numbers of the disposables as well as the water (Module 16).</p>
{{key:Match the calling card to the suspect: hemolysis to chloramine or the tubing, confusion to aluminum, itching and arrhythmia to fluoride, early chills to bacteria, liver failure to toxins.}}
"""),
        ("dialysate", "Mixing dialysate", "Mixing dialysis fluid: water, two concentrates, and conductivity", """
<p>Making dialysis fluid is like making juice from concentrate: the machine adds exact amounts of two concentrates to treated water, minute by minute. Conductivity is the machine&rsquo;s taste test for total dissolved salt. The picture has a limit. A taste test says the juice is too strong or too weak, not which ingredient is wrong, and it cannot taste a contaminant that carries no charge.</p>
{{fig:pod06_proportioning}}
<h3>The two concentrates</h3>
<p>The acid concentrate carries sodium chloride, potassium, calcium, magnesium, a small amount of acid, and in many formulas glucose. The bicarbonate concentrate carries sodium bicarbonate. The two are kept apart until the last moment, because calcium and magnesium would otherwise combine with bicarbonate and fall out of solution as scale.[[daugirdas2015]] The machine draws each through its own pump in a fixed ratio and mixes them with product water. This is called proportioning.</p>
{{fig:pod06_concentrates}}
<p>Bicarbonate concentrate supports bacterial growth. A jug left open or mixed long before use can carry bacteria and endotoxin into every session it feeds.[[daugirdas2015]] Your unit&rsquo;s protocol states how long a mixed bicarbonate container may be used.</p>
<h3>What conductivity measures, and what it misses</h3>
<p>Conductivity rises with the concentration of charged particles. Sodium and its partner anions supply most of it, so conductivity is a close stand-in for the sodium in the fluid.[[daugirdas2015]] If a pump fails, a line kinks, a jug runs empty, or the wrong jug is connected, conductivity moves. Out of range, the machine alarms and sends the fluid to drain, the bypass Module 5 described. A temperature sensor works the same way.</p>
<p>Two gaps remain. Conductivity cannot tell sodium from potassium, so a wrong acid concentrate with similar total salt may pass. It also misses bacteria, endotoxin, and uncharged toxins, which depend on the water system and testing.[[greenberg2021]]</p>
<h3>What the blood does when the fluid is wrong</h3>
<p>Plasma equilibrates with dialysis fluid within minutes, so a wrong fluid changes the patient quickly. The chain below is established physiology. Alarm thresholds belong to the machine manual and the unit&rsquo;s protocol.</p>
<div class="table-wrap"><table>
<thead><tr><th>Error</th><th>What happens in the body</th><th>What you may see</th></tr></thead>
<tbody>
<tr><td>Sodium too low (fluid too dilute)</td><td>Plasma sodium falls. Water moves into red cells and brain cells, which swell. Red cells burst</td><td>Hemolysis with chest or back pain, headache, confusion, seizures</td></tr>
<tr><td>Sodium too high (fluid too concentrated)</td><td>Plasma sodium and osmolality rise. Water leaves cells, including brain cells</td><td>Intense thirst, headache, nausea, rising blood pressure, confusion</td></tr>
<tr><td>Fluid too hot</td><td>Heat damages the red cell membrane</td><td>Hemolysis, often in the first part of the session</td></tr>
<tr><td>Fluid too cold</td><td>The body loses heat to the circuit</td><td>Shivering and a cold sensation, without fever</td></tr>
<tr><td>Contaminated bicarbonate</td><td>Bacterial fragments cross the membrane and trigger cytokines</td><td>Chills, fever, and low blood pressure early in the session</td></tr>
</tbody></table></div>
<p>The table follows standard sources.[[daugirdas2015]][[greenberg2021]] When several patients on one concentrate batch show the same picture, suspect the batch.</p>
<h3>Purity and long-term inflammation: what the trials show</h3>
<p>Composition is part of the prescription (Module 7). Purity is a separate question. Ultrapure dialysis fluid is made to stricter bacterial and endotoxin limits, often with an ultrafilter at the station.</p>
<p>Susantitaphong and colleagues pooled 23 study arms with 2,221 patients, most of them not randomized. Ultrapure fluid lowered C-reactive protein (CRP) by 3.2 mg/L, raised serum albumin by 0.11 g/dL and hemoglobin by 0.40 g/dL, and lowered the weekly erythropoietin dose by 273 units. The results held when the analysis was limited to controlled trials. The authors called these surrogate markers and asked for a trial with hard outcomes.[[susantitaphong2013]]</p>
<p>Asci and colleagues then randomized 704 patients in a two-by-two factorial trial of high-flux versus low-flux membranes and ultrapure versus standard fluid. The trial found no difference with ultrapure fluid in fatal and nonfatal cardiovascular events (hazard ratio 0.90, 95% confidence interval 0.61 to 1.32). A lower risk after more than 3 years on dialysis came from a post hoc analysis, which can only generate a hypothesis.[[asci2013]]</p>
<p>Surrogates improve; in the one trial, hard outcomes did not. Whether to use ultrapure fluid is a decision for the unit and its Medical Director.</p>
<h3>What the physician on duty does</h3>
<p>A conductivity or temperature alarm with the patient connected is a stop-and-check event (Module 5). Sudden headache, chest tightness, cramps, or hemolysis early in the session prompts a check of the concentrate and the machine, not only the patient. Ask which jug is connected, when it was changed, and what the machine&rsquo;s conductivity reads.</p>
{{call:Stop and call when a conductivity or temperature alarm will not clear with the patient connected, or when any patient shows signs of hemolysis. Follow your unit&rsquo;s protocol on whether the blood is returned, as Module 16 teaches; suspected hemolysis means it is not. Call the attending nephrologist at once.}}
"""),
        ("cluster", "Clusters", "When several patients are sick from the same cause", """
<p>A smoke alarm going off in one room may mean burnt toast. Alarms going off in three rooms at once point to the building. The picture has a limit. Three patients can fall ill on one afternoon for three reasons. A cluster is a hypothesis to test quickly, not a conclusion.</p>
<h3>What counts as a cluster</h3>
<p>A cluster is two or more patients with the same new symptom, linked by something they share. The link may be the shift, the room, the water loop, a group of machines, a batch of concentrate, or a lot of disposables. The symptom need not be dramatic. Nausea, itching, or chills in more than one chair within an hour is enough to ask.</p>
<p>Module 16 gives the circuit side of the cluster-event card. This section adds the water and the fluid, and the reasoning that finds the cause.</p>
<h3>Comparison finds the cause</h3>
<p>Every outbreak in Section 3 was solved by comparison. In the fluoride outbreak, illness was confined to one room served by one deionization unit: 12 of 15 patients in that room and none of 17 next door.[[arnow1994]] In Caruaru, all 17 patients on the Tuesday, Thursday, and Saturday night schedule became ill.[[jochimsen1998]] In the tubing outbreak, the link was one manufacturing lot.[[duffy2000]] The comparison, not the count, points to the cause.</p>
{{formula:<strong>Worked scenario 2. Attack rate: who is sick and who is not.</strong><br>Formula: attack rate = patients who became ill &divide; patients who were exposed.<br>Published example: fluoride outbreak. Room A: 12 &divide; 15 = <strong>80%</strong>. Adjacent room: 0 &divide; 17 = <strong>0%</strong>. The difference pointed to the one thing room A had and the other room did not: its own deionizer.<br>Illustrative unit example: afternoon shift 5 &divide; 12 = <strong>42%</strong>. Morning shift 0 &divide; 14 = <strong>0%</strong>. The difference points to something that changed between shifts, such as a concentrate batch, a group of machines, a lot of disposables, or a water event.<br>What the number tells you: where to look first. What it does not tell you: the cause. With small numbers, chance differences are easy, so testing must confirm the comparison.}}
<p>Split the patients by every exposure you can name, and hand that table to the Medical Director. The published figures above are from the fluoride report.[[arnow1994]]</p>
{{fig:wts_golden|When a water problem is suspected, the rule is the same: stop, hold treatments per protocol, check, and escalate.}}
<h3>The first steps</h3>
<p>The first steps follow your unit&rsquo;s cluster protocol. The sequence below shows what such a protocol usually contains.</p>
{{flow:First steps in a suspected water or fluid cluster|Say it aloud::Tell the charge nurse that this may be a cluster event. Name the shared symptom and the patients.|Treat each patient::Assess each at the chair and stop fluid removal or the blood pump per protocol. Suspected hemolysis means the blood is not returned (Module 16).|Hold new starts::Per protocol, on the affected loop, machines, or concentrate batch.|Call the technician::Ask for a total chlorine test now, the conductivity of affected machines, and today&rsquo;s log entries.|Keep samples::Patient blood per protocol, dialysis fluid, product water, concentrate containers, and dialyzers and tubing with lot numbers.|Record::Times, stations, machines, batch, lots, symptoms, and who was told.|Call::The attending nephrologist for each patient and the Medical Director at once. Reporting outside the unit follows unit policy.}}
<p>Two errors are common: treating each patient alone while the shared cause reaches new patients, and discarding the jug, the dialyzers, and with them the cause.</p>
{{call:Stop and call the Medical Director at once when two or more patients have the same new symptom on the same shift, room, loop, machine group, or lot. Call each patient&rsquo;s attending nephrologist. Start the unit&rsquo;s cluster protocol while you call.}}
{{key:One sick patient is a patient problem. Two with the same new symptom is a unit problem until proven otherwise.}}
"""),
        ("records", "The water log", "Reading the water log and asking the right questions", """
<p>The water log is the daily vital-sign sheet for the unit&rsquo;s largest patient. The picture has a limit. A water log describes samples taken at certain points and times, so a clean log can miss a problem that started an hour after the last test.</p>
<h3>What the log contains</h3>
<p>The ISO standards set the quality requirements and give guidance on monitoring. Each unit writes them into its own policy.[[iso23500_3_2024]][[iso23500_5_2024]] The CDC review covers the monitoring methods.[[coulliette2013]]</p>
<p>Expect pre-shift total chlorine results, daily reverse osmosis readings such as product water conductivity and salt rejection, bacterial culture and endotoxin results from set sample points, periodic chemical analyses, disinfection dates, and the corrective action taken whenever a result reached a set level.</p>
{{fig:pod06_water_report}}
<p>Two terms matter on a microbiology report. A maximum level is the limit at which the system should be taken out of use until it is corrected and re-tested. An action level is set below it, as an early warning. Reaching it calls for corrective steps such as disinfection and a re-test.[[coulliette2013]] The same review advises testing total chlorine before each patient shift, after the first carbon tank.[[coulliette2013]] The numbers come from your unit&rsquo;s policy.</p>
<h3>Reading a log line by line</h3>
{{formula:<strong>Worked scenario 3. A model water log (illustrative entries; the unit&rsquo;s ISO-based levels apply).</strong><br>Line 1. Today, 5:40 a.m.: total chlorine after the first carbon bed recorded as within the unit&rsquo;s limit, initialed. <em>Reading:</em> the test was done and passed. No question needed.<br>Line 2. Last month: bacterial culture from the loop return marked &ldquo;action level reached&rdquo;; loop disinfected two days later; re-sample within limit. <em>Reading:</em> the system worked as designed. Confirm that the re-test result is on file.<br>Line 3. Reverse osmosis salt rejection: 98%, 97%, 96%, 95% over two weeks. <em>Reading:</em> a falling trend. Ask the technician today what is planned, and tell the Medical Director.<br>Line 4. Yesterday: &ldquo;system serviced&rdquo; with no detail of what was changed and no post-service chlorine test. <em>Reading:</em> a documentation gap. Ask what was serviced and whether a test was done before patients started.<br>What the walk-through tells you: which entries need a question and to whom. What it does not tell you: whether the water is safe now. Only a current test answers that.}}
<p>You are not auditing the technician. You are confirming that today&rsquo;s protective checks were done, and noticing trends the Medical Director should know.</p>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>Question to the technician</th><th>Who else needs to know</th></tr></thead>
<tbody>
<tr><td>Start of every shift</td><td>Was the chlorine test done, and did it pass?</td><td>No one, if it passed</td></tr>
<tr><td>Chlorine test failed</td><td>What does our policy say happens to treatments now?</td><td>Charge nurse, attending nephrologist, Medical Director</td></tr>
<tr><td>A culture or endotoxin result reached the action level</td><td>Has the corrective action been done and the re-test sent?</td><td>Medical Director</td></tr>
<tr><td>A falling reverse osmosis trend</td><td>What is planned, and by when?</td><td>Medical Director</td></tr>
<tr><td>Two or more patients with the same new symptom</td><td>Chlorine now, conductivity of affected machines, today&rsquo;s log</td><td>Medical Director and attending nephrologists, at once</td></tr>
</tbody></table></div>
<h3>What the physician on duty does</h3>
<p>At the start of each shift, confirm that the chlorine test was done and passed. If a result is out of range, follow the unit&rsquo;s water policy on holding treatments, backup carbon, and who decides. Write any water-related concern in your shift note, with the time and the name of the person you told. Module 30 covers failure of the water supply itself.</p>
{{key:Read the log at the start of every shift. A passed chlorine test is the one entry that must be there before the first patient starts.}}
"""),
    ],
    "debrief": ["""
<p><strong>What makes this a cluster?</strong> Three patients developed new symptoms within forty minutes of starting, on the same shift, in the same room. Their complaints overlap, and their pressures are higher than expected early in a session. The morning shift was well. Something changed between shifts, and two changes are known: a new bicarbonate concentrate supply and yesterday&rsquo;s water service. Together they share an exposure, which makes this a unit problem until proven otherwise.</p>
<p><strong>Which causes fit, and what would you ask to see?</strong> The picture fits fluid that is too concentrated: headache, nausea, thirst or a feeling of heat, cramps, and rising pressure. A proportioning fault or a wrong concentrate could produce it, and the concentrate change makes this the leading suspect. Early hemolysis also fits, so chloramine after yesterday&rsquo;s service, overheated fluid, and a faulty tubing lot stay on the list. Contaminated bicarbonate would more often bring chills and fever, which no one has yet. You ask to see the concentrate containers on each affected machine with their batch numbers, the machines&rsquo; conductivity and temperature readings, an immediate total chlorine test, the record of yesterday&rsquo;s service, and the dialyzer and tubing lots. You look at the blood in each venous line and ask for sodium, potassium, and hemoglobin per protocol.</p>
<p><strong>Your first steps in the next 10 minutes, and whom you call.</strong> You tell the charge nurse aloud that this is a possible cluster. Each patient is assessed, and fluid removal is stopped per protocol. Because the concentrate is the leading suspect, treatment on the affected machines is paused per protocol until the conductivity and the containers are checked. If any line shows translucent, dark blood or a patient has chest or back pain, the blood pump is stopped, the lines are clamped, and the blood is not returned, as Module 16 teaches. Per protocol, no new patient is started on the machines or concentrate batch in question. You check the other eleven patients, because the attack rate matters. The containers, fluid samples, and disposables are kept. You call the Medical Director at once and each patient&rsquo;s attending nephrologist. You record times, stations, machines, batch, lots, and whom you told.</p>
"""],
    "skills": {"title": "Reading the daily water log with the technician",
               "intro": "Perform this at the start of a supervised shift, in the water room, with the technician and your preceptor present.",
               "items": [
                   ("Locates the water room, the water log, and the technician on duty at the start of the shift.", False),
                   ("Confirms that today&rsquo;s pre-shift total chlorine (or chloramine) test was done, recorded, and within the unit&rsquo;s limit.", True),
                   ("Identifies the sample point for each recorded result.", False),
                   ("Reads the most recent microbiology and endotoxin results and states whether an action or maximum level was reached.", False),
                   ("If a level was reached, confirms that the corrective action and the re-test are recorded.", False),
                   ("Notes recent maintenance, disinfection, or concentrate changes that could explain new symptoms on the shift.", False),
                   ("Reads the reverse osmosis performance trend and states whether it is stable or falling.", False),
                   ("States the unit&rsquo;s rule for what happens to treatments when a chlorine test fails.", True),
                   ("Names the escalation path: technician, charge nurse, attending nephrologist, Medical Director.", True),
                   ("States the first steps of the unit&rsquo;s cluster protocol, including which samples and supplies are kept.", True),
                   ("Records in the shift note any water-related concern, the time, and the person to whom it was reported.", False),
               ],
               "placement": "Once a week for four weeks, read the water log with the technician at the start of your shift. Each time, write down one entry you would question and the answer you received. Review the four entries with your preceptor or the Medical Director."},
    "quiz": [
        ("Why can a contaminant that is harmless in drinking water harm a dialysis patient?",
         ["Dialysis patients drink more water than other people",
          "Dialysis fluid bypasses the gut and liver, the volume is large, and the kidneys cannot excrete what crosses",
          "The dialyzer membrane concentrates contaminants",
          "Contaminants become more toxic when heated"], 1,
         "Three gates are lost, and the exposure runs to hundreds of liters a week."),
        ("A dialysis fluid flow of 500 mL per minute runs for 240 minutes, three times a week. About how much fluid meets the blood each week?",
         ["36 L", "120 L", "360 L", "1,440 L"], 2,
         "500 &times; 240 &divide; 1,000 = 120 L per session, and 120 &times; 3 = 360 L per week."),
        ("Which step of water treatment removes chloramine?",
         ["Reverse osmosis", "The softener", "The sediment filter", "Activated carbon"], 3,
         "Chloramine passes through reverse osmosis and deionization. Carbon removes it, which is why the chlorine test is taken after the first carbon bed."),
        ("Why are two carbon beds placed in series?",
         ["So that breakthrough after the first bed is detected before the second fails",
          "To double the speed of water flow",
          "So that one bed removes chlorine and the other removes bacteria",
          "To remove fluoride"], 0,
         "A test between the beds catches exhaustion of the first while the second still protects."),
        ("Over two afternoon shifts, four patients in one room develop new anemia, and two have back pain during dialysis. The technician changed a carbon tank last week. Which contaminant is the leading suspect?",
         ["Aluminum", "Chloramine", "Fluoride", "Endotoxin"], 1,
         "Hemolysis after a carbon change points to chloramine. A faulty tubing lot is the main mimic."),
        ("Several patients develop severe itching and nausea during dialysis, and one has ventricular fibrillation. All were treated in one room that uses a temporary deionizer. What is the likely cause?",
         ["Cyanobacterial toxins", "Copper", "Fluoride released from the deionizer", "Aluminum from cement-lined pipes"], 2,
         "This matches the published outbreak in which a temporary deionizer released fluoride: 12 of 15 patients in one room became ill."),
        ("What did the Caruaru outbreak in Brazil show?",
         ["Untreated surface water carried cyanobacterial toxins that caused liver failure and death",
          "Ultrapure dialysis fluid prevents liver disease",
          "Chloramine causes liver failure",
          "Endotoxin tests detect all toxins"], 0,
         "Of 130 patients, 101 met the case definition of acute liver failure and 50 died. The water had not been treated."),
        ("What does the Limulus amebocyte lysate (LAL) test miss, according to Glorieux and colleagues?",
         ["All endotoxin",
          "Live bacteria",
          "Chlorine",
          "Some smaller bacterial fragments that still provoke inflammation in a cell assay"], 3,
         "About 1 in 10 pure or ultrapure samples still provoked a cytokine response. The clinical meaning is unknown."),
        ("What does conductivity in dialysis fluid mainly reflect?",
         ["Bacterial contamination", "Total dissolved salt, mostly sodium", "Temperature", "Glucose concentration"], 1,
         "Conductivity rises with charged particles. It cannot detect bacteria, endotoxin, or uncharged toxins."),
        ("Twenty minutes into the session, a patient complains of intense thirst, headache, and nausea, and the blood pressure has risen. The bicarbonate jug was changed before the start. What should you suspect first?",
         ["A pyrogenic reaction",
          "Dialysis fluid that is too cold",
          "Dialysis fluid that is too concentrated, from a proportioning or concentrate error",
          "A volume-related drop"], 2,
         "High sodium pulls water out of cells and raises thirst and pressure. Check the concentrate, the conductivity, and the machine."),
        ("What did the factorial randomized trial by Asci and colleagues show about ultrapure dialysis fluid?",
         ["It halved cardiovascular events",
          "It increased mortality",
          "It improved survival in all subgroups",
          "It did not reduce cardiovascular events; a benefit after more than 3 years on dialysis was post hoc"], 3,
         "The hazard ratio was 0.90 with a confidence interval from 0.61 to 1.32. The subgroup finding needs confirmation."),
        ("The meta-analysis by Susantitaphong and colleagues found that ultrapure fluid raised hemoglobin and albumin and lowered C-reactive protein. How should you describe these findings?",
         ["Proof that ultrapure fluid prolongs life",
          "Changes in surrogate markers, mostly from nonrandomized studies, without proof of benefit on hard outcomes",
          "Evidence of harm",
          "Changes too small to measure"], 1,
         "These are surrogates. The authors called for a large trial with hard outcomes."),
        ("At 3 p.m., two patients in different rooms on the same water loop develop chills and fever within an hour of starting. Neither has a catheter. What is the best next step?",
         ["Treat each as a separate infection and continue",
          "Raise the dialysis fluid temperature",
          "Restart both sessions after giving fluids",
          "Declare a possible cluster, follow the protocol, and call the Medical Director and the attending nephrologists"], 3,
         "The same new symptom on one loop is a unit problem until proven otherwise. Early chills suggest endotoxin."),
        ("In a cluster, 6 of 10 patients on machines that received a new concentrate batch are ill, and 0 of 9 on the old batch are. What does this comparison tell you?",
         ["The new batch is the leading suspect, to be confirmed by testing",
          "The water is the cause",
          "The batch is proven to be the cause",
          "Nothing, because the numbers are small"], 0,
         "An attack rate of 60% against 0% points to the batch. It guides testing; it does not prove the cause."),
        ("At the start of your shift, the log shows no total chlorine result for today, and the first patients are about to start. What do you do?",
         ["Start the patients, because yesterday&rsquo;s test passed",
          "Ask the technician to test now and follow the unit&rsquo;s policy before patients start, and inform the charge nurse",
          "Change the patients&rsquo; dialysis fluid prescription",
          "Wait until the end of the shift to mention it"], 1,
         "The pre-shift chlorine test protects red cells. The policy states what happens when it is missing."),
    ],
    "terms": [("Dialysis fluid (dialysate)", "The fluid on the other side of the dialyzer membrane, made from treated water and two concentrates."),
              ("Product water", "Water after treatment, ready to make dialysis fluid and concentrates."),
              ("Reverse osmosis", "A tight membrane process that rejects most dissolved salts, metals, and microbes. The main barrier in water treatment."),
              ("Chloramine", "A disinfectant added to city water. It passes reverse osmosis, is removed by carbon, and breaks red cells."),
              ("Endotoxin", "A part of the outer wall of certain bacteria that triggers fever and inflammation, even when the bacteria are dead."),
              ("Conductivity", "How well the fluid carries an electric current. It reflects total dissolved salt, mostly sodium."),
              ("Proportioning", "The machine&rsquo;s mixing of treated water with acid and bicarbonate concentrates in a fixed ratio."),
              ("Ultrapure dialysis fluid", "Dialysis fluid made to stricter bacterial and endotoxin limits than standard fluid."),
              ("Action level", "A test result below the maximum level that calls for corrective action and a re-test."),
              ("Attack rate", "The number of people who became ill divided by the number who were exposed.")],
    "readings": [("dialysis-water-treatment-systems.html", "How each part of the water treatment system works, and how source water changes the design."),
                 ("dialysis-prescription.html", "How dialysis fluid composition, flow, and time fit into the prescription.")],
    "calcs": ["calc-wts-self-assessment.html", "calc-carbon-tank-ebct.html", "calc-wts-capacity.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
