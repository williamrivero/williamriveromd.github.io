# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 35: Evidence appraisal, research, quality improvement and teaching.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. FIDELIO-DKD,
FIDELITY and CONFIDENCE numbers from the PubMed abstracts; absolute differences and NNTs are this module's arithmetic from
the published event proportions and are labeled as crude. KDIGO 2022 position on nonsteroidal MRAs stated without a grade
(grade not verified for this module). Teaching and QI sources from PubMed. No doses. Fictional case."""

MODULE = {
 'image_alt': 'Internal medicine residents and a nephrology fellow at a hospital journal club in Cebu City, one pointing at a projected bar chart of two trial arms while others take notes.',
 'objectives': [
  '<strong>Intern:</strong> Find the population, intervention, comparison and outcome of a trial report, and say in one sentence whether the outcome is one that patients feel or a surrogate.',
  '<strong>Resident:</strong> Appraise one randomized trial, compute the absolute risk reduction (ARR) and number needed to treat (NNT) from its event rates, and explain the result to a patient in plain numbers.',
  '<strong>Fellow:</strong> Design an ethical quality improvement (QI) or research project with a run chart or a protocol fit for ethics review, and teach a learner with structured feedback.',
 ],
 'big': """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; turning a paper into a decision, and a decision into a better unit</span>The intern reads the abstract and asks the plain questions: who was studied, what was compared, and what happened to them? The resident turns the published percentages into numbers a patient can use, and notices the traps. The fellow takes the next step: measures how the unit actually performs, tests one change at a time, knows when a project needs ethics review, and teaches all of this to the people behind them.</div>
{{plain:Think of a trial as a weather forecast for a crowd. It cannot tell you whether it will rain on one person&rsquo;s house, but it can tell you that out of 100 houses like hers, about 21 will get wet without an umbrella and about 18 with one.}}
<p>The picture has a limit. Weather does not change because you watch it; patients in trials are selected, monitored and treated more carefully than the patient in front of you, and the &ldquo;rain&rdquo; is often a composite of several different events, some of which patients feel and some of which are laboratory thresholds. A forecast also comes with a cost the trial never counts: in the Philippines, many kidney-protective medicines are paid for out of pocket, and the family decides whether three fewer events per 100 people over about 2.6 years is worth the monthly price. Appraisal is the skill of reading the forecast with all of that in mind.</p>
{{cards:Key numbers|FIDELIO-DKD (diabetic kidney disease) primary kidney outcome, median 2.6 years::17.8% with finerenone versus 21.1% with placebo; hazard ratio 0.82 (randomized controlled trial, 5,734 randomized)|Absolute risk reduction, FIDELIO-DKD primary outcome::3.3 percentage points; crude NNT about 30 over the trial (this module&rsquo;s arithmetic from the published proportions)|Hyperkalemia-related stopping of the trial drug, FIDELIO-DKD::2.3% versus 0.9%|FIDELITY pooled kidney outcome, median 3.0 years::5.5% versus 7.1%; hazard ratio 0.77 (prespecified pooled analysis, 13,026 patients)|PDSA reporting quality (systematic review of 73 articles)::Fewer than 20% fully documented a sequence of iterative cycles}}
<p>Most journal-club arguments are about relative effects quoted without baselines, composite outcomes read as if every part mattered equally, surrogate markers read as if they were outcomes, and subgroups read as if they were proof. A few are about the deeper question of whether the trial population looks like your patients at all. Your work is to convert every claim into absolute numbers for a defined group over a defined time, to name the traps aloud, and then to carry the same discipline into measuring and improving your own unit.</p>
""",
 'case': {'title': 'Journal club on a Tuesday',
  'html': """
<p>Tuesday, 12:15 p.m., the conference room of a tertiary hospital in Cebu City. Dr. Mia Fernandez, a second-year internal medicine resident, presents FIDELIO-DKD. Her first slide says, in large letters, &ldquo;Finerenone reduces kidney disease progression by 18%.&rdquo; Dr. Carlo Aquino, a first-year nephrology fellow, says the drug is too expensive for their clinic patients and that &ldquo;sodium-glucose cotransporter 2 (SGLT2) inhibitors already do the job.&rdquo; Another resident shows a newer trial in which a combination lowered albuminuria by about a third more than either drug alone and says, &ldquo;So the combination must prevent dialysis.&rdquo;</p>
<p>The patient they have in mind is Mr. Teodoro Lim, 62, a retired jeepney operator from Mandaue with type 2 diabetes, an estimated glomerular filtration rate (eGFR) of 48 mL/min/1.73 m&sup2;, a urine albumin-to-creatinine ratio of 640 mg/g, and a potassium of 4.7 mmol/L, already on the maximum tolerated dose of an angiotensin receptor blocker and on an SGLT2 inhibitor (SGLT2i) his daughter in Singapore pays for. The attending asks the fellow to propose a unit project afterward, because two patients started on a mineralocorticoid receptor antagonist last year had no potassium checked for three months.</p>
""",
  'questions': ['What are the absolute risk reduction and number needed to treat for FIDELIO-DKD&rsquo;s primary outcome, and how would you explain them to Mr. Lim?',
                'Which interpretation traps appear in this discussion, and how would you correct each one?',
                'What project should the fellow propose for potassium monitoring, and does it need ethics review?']},
 'sections': [
  ('appraisal', 'Appraising a trial', 'From the abstract to absolute numbers', """
<p>Every therapeutic claim reduces to one question: in people like these, over this much time, how many fewer had the bad outcome, and at what cost in harm? Relative effects such as hazard ratios are the natural output of the statistics, but they hide the baseline. An 18% relative reduction means one thing when the baseline risk is 40% and another when it is 4%. Laupacis and colleagues proposed the number needed to treat as the reciprocal of the absolute risk reduction, precisely so that clinicians could see the size of an effect in people rather than in ratios.[[ntr35_4]]</p>
{{formula:<strong>Arithmetic from the FIDELIO-DKD abstract, not a target.</strong> ARR = control event rate &minus; treatment event rate = 21.1% &minus; 17.8% = 3.3 percentage points.<br>NNT = 1 &divide; ARR = 1 &divide; 0.033 &asymp; 30 people treated for the median 2.6 years to prevent one primary outcome event.<br>Number needed to harm for stopping the drug because of hyperkalemia = 1 &divide; (0.023 &minus; 0.009) &asymp; 71.}}
<p><strong>The trial.</strong> The Finerenone in Reducing Kidney Failure and Disease Progression in Diabetic Kidney Disease (FIDELIO-DKD) trial randomized 5,734 patients with type 2 diabetes and chronic kidney disease (CKD), that is, diabetic kidney disease (DKD),, all on renin-angiotensin system blockade adjusted to the maximum labeled dose that did not cause unacceptable side effects, to finerenone or placebo. Eligible patients had a urine albumin-to-creatinine ratio of 30 to under 300 mg/g with an eGFR of 25 to under 60 and diabetic retinopathy, or a ratio of 300 to 5,000 mg/g with an eGFR of 25 to under 75. Over a median 2.6 years, the primary composite of kidney failure, a sustained fall in eGFR of at least 40%, or renal death occurred in 504 of 2,833 patients (17.8%) on finerenone and 600 of 2,841 (21.1%) on placebo, hazard ratio 0.82 (95% confidence interval 0.73 to 0.93). The key cardiovascular secondary outcome occurred in 13.0% versus 14.8%. Overall adverse events were similar; stopping the trial drug because of hyperkalemia was more frequent with finerenone (2.3% versus 0.9%).[[ntr35_1]]</p>
<p><strong>The pooled view.</strong> FIDELITY combined FIDELIO-DKD with its companion trial, Finerenone in Reducing Cardiovascular Mortality and Morbidity in Diabetic Kidney Disease (FIGARO-DKD), in a prespecified analysis of 13,026 patients followed for a median 3.0 years. The cardiovascular composite occurred in 12.7% versus 14.4% (hazard ratio 0.86), and a kidney composite that used a stricter threshold, a sustained eGFR fall of at least 57%, occurred in 5.5% versus 7.1% (hazard ratio 0.77). Hyperkalemia leading to permanent discontinuation occurred in 1.7% versus 0.6%.[[ntr35_2]] The crude absolute differences are 1.7 and 1.6 percentage points, about 59 and 63 people treated for three years per event prevented; a pooled analysis of two trials is still randomized evidence, but its kidney outcome definition differs from FIDELIO-DKD&rsquo;s, so the numbers are not interchangeable.</p>
<p><strong>The guideline.</strong> The Kidney Disease: Improving Global Outcomes (KDIGO) 2022 diabetes guideline places a nonsteroidal mineralocorticoid receptor antagonist with proven kidney or cardiovascular benefit in adults with type 2 diabetes, an eGFR of at least 25 mL/min/1.73 m&sup2;, a normal serum potassium and albuminuria despite the maximum tolerated dose of a renin-angiotensin system inhibitor.[[ntr35_3]] Read the guideline itself for the strength and grade attached; this module does not restate a grade it has not checked. KDIGO has also begun a focused update of this chapter, so check for the newest text.</p>
<div class="table-wrap"><table><thead><tr><th>Question</th><th>Where to find it</th><th>FIDELIO-DKD answer</th></tr></thead><tbody>
<tr><td>Who was studied?</td><td>Methods: eligibility</td><td>Type 2 diabetes, albuminuric CKD, on maximum tolerated renin-angiotensin blockade</td></tr>
<tr><td>What was compared?</td><td>Methods: intervention</td><td>Finerenone versus placebo, on top of usual care</td></tr>
<tr><td>What happened, absolutely?</td><td>Results: event counts</td><td>17.8% versus 21.1% over a median 2.6 years</td></tr>
<tr><td>Is the outcome felt by patients?</td><td>Outcome definitions</td><td>A composite: kidney failure and renal death are felt; a 40% eGFR fall is a laboratory threshold</td></tr>
<tr><td>What harms?</td><td>Safety table</td><td>More hyperkalemia leading to stopping the drug</td></tr>
<tr><td>Does it fit my patient?</td><td>Baseline table</td><td>Check eGFR, albuminuria, potassium and background therapy, including how many were on an SGLT2 inhibitor</td></tr>
</tbody></table></div>
<div class="tc-keyp"><span class="tc-lab">Philippine practice</span>A drug the family buys every month competes with food, fares and other medicines. Give the family absolute numbers over a stated time, the harm and its monitoring, and the cost, then let them weigh it. An NNT of about 30 over 2.6 years is a real benefit; it is also an honest statement that most people treated would not have had the event either way.</div>
{{key:Never present a relative effect alone. Say how many people in 100, over how many years, avoided the outcome, and how many had the harm.}}
{{fig:ntr35_a}}
"""),
  ('stats-traps', 'Statistical traps', 'Traps: relative effects, composites, surrogates and subgroups', """
<p>Misreading a trial rarely comes from bad arithmetic. It comes from four habits of mind, each with a mechanism you can name. The Grading of Recommendations Assessment, Development and Evaluation (GRADE) approach was built partly to make these judgments explicit: it rates the certainty of evidence for each outcome that matters to patients, and it separates that certainty from the strength of a recommendation.[[ntr35_5]]</p>
<div class="table-wrap"><table><thead><tr><th>Trap</th><th>How it misleads</th><th>What you say at journal club</th></tr></thead><tbody>
<tr><td>Relative effect without a baseline</td><td>&ldquo;18% reduction&rdquo; sounds the same for a high-risk and a low-risk patient</td><td>&ldquo;From 21.1% to 17.8% over 2.6 years: 3.3 fewer per 100.&rdquo;</td></tr>
<tr><td>Composite outcome read as one thing</td><td>A benefit driven by the softest component is credited to the hardest</td><td>&ldquo;Which components drove the result? Is the eGFR threshold a surrogate?&rdquo;</td></tr>
<tr><td>Surrogate read as an outcome</td><td>A laboratory marker improves; patients may not</td><td>&ldquo;Albuminuria fell. Did kidney failure, death or hospitalization fall?&rdquo;</td></tr>
<tr><td>Subgroup read as proof</td><td>With enough subgroups, some differ by chance</td><td>&ldquo;Was it prespecified, with a stated direction, one of few, and is there a test for interaction?&rdquo;</td></tr>
<tr><td>Population that does not match</td><td>Trial patients are selected and monitored closely</td><td>&ldquo;Would our patient have been eligible? Would we monitor potassium as closely?&rdquo;</td></tr>
<tr><td>Statistical versus clinical significance</td><td>A small p value can attach to a small effect</td><td>&ldquo;What is the confidence interval in absolute terms?&rdquo;</td></tr>
</tbody></table></div>
<p><strong>Surrogates.</strong> The CONFIDENCE trial randomized adults with type 2 diabetes, CKD and albuminuria to finerenone, empagliflozin or both. At 180 days, the reduction in urine albumin-to-creatinine ratio with the combination was 29% greater than with finerenone alone and 32% greater than with empagliflozin alone; symptomatic hypotension, acute kidney injury and hyperkalemia leading to stopping were uncommon.[[ntr35_8]] It was a phase 2 trial with albuminuria as its primary outcome. Albuminuria is a surrogate: it is associated with kidney failure, and lowering it is biologically plausible as a route to benefit, but CONFIDENCE did not measure kidney failure, dialysis or death. &ldquo;So the combination must prevent dialysis&rdquo; is a hypothesis, not a finding.</p>
<p><strong>Subgroups.</strong> Sun and colleagues set out criteria for judging whether a subgroup effect is believable: among them, whether the subgroup was specified before the analysis with a predicted direction, whether it is one of a small number tested, whether the test for interaction is significant, whether the effect is consistent across related outcomes and studies, and whether there is a compelling biological rationale.[[ntr35_6]] Most subgroup claims in a slide deck meet few of these.</p>
<p><strong>Reporting.</strong> The CONSORT 2025 statement is a 30-item checklist and a flow diagram for reporting randomized trials, with a new section on open science.[[ntr35_7]] Use it as a reading checklist: if the flow of participants, the prespecified primary outcome or the harms are hard to find, the report is hiding something or the trial was weak.</p>
<div class="tc-keyp"><span class="tc-lab">At your stage</span><strong>Intern:</strong> label every outcome you present as felt by patients or surrogate. <strong>Resident:</strong> put the absolute numbers on your first slide, not your last. <strong>Fellow:</strong> ask the subgroup and composite questions aloud, kindly, so that residents learn to ask them.</div>
{{key:Before you believe a result, name the outcome, the baseline, the time and the comparison. If any of the four is missing, you do not yet know the effect.}}
"""),
  ('qi', 'Quality improvement', 'Quality improvement: PDSA cycles and run charts', """
<p>Research asks whether something works in general. Quality improvement asks whether your unit reliably does what is already known to work, and whether a change helps here. The causal model is different. The evidence for checking potassium after starting a mineralocorticoid receptor antagonist is not in question; what is in question is why two of your patients went three months without a test. The answer lies in the process: who orders the test, who reminds, who reads the result, and what happens when the patient cannot afford the fare to the laboratory.</p>
<p><strong>The plan-do-study-act (PDSA) cycle</strong> tests one change on a small scale, predicts what will happen, measures, learns and then adapts, adopts or abandons it before the next cycle. A systematic review of 73 articles reporting PDSA in health care found that many applications did not follow the method&rsquo;s main features: fewer than 20% (14 of 73) fully documented a sequence of iterative cycles, and only 15% (7 of 47) used quantitative data at monthly or more frequent intervals to guide the cycles.[[ntr35_9]] The lesson is to keep cycles small, predictions explicit and data frequent.</p>
<p><strong>The run chart</strong> plots a measure over time, in order, with a median line. It lets a team see whether changes are followed by real improvement or by ordinary variation, with little mathematics, and it is the foundation for more formal control charts.[[ntr35_10]] An average before and after hides exactly what a run chart shows: when the change happened and whether it held.</p>
{{fig:ntr35_b}}
{{flow:A small QI project for potassium monitoring|Aim::By the end of three months, 90% of clinic patients started on a mineralocorticoid receptor antagonist have a potassium result within the interval the attending and the unit protocol set.|Measure::Each week, count patients started and those with a timely result. Plot the percentage on a run chart.|Change idea 1::A pre-printed laboratory request and return date given with every new prescription.|Predict::Write down what you expect: for example, timely tests rise from half to most.|Study::After two to four weeks, look at the run chart and ask the patients who missed why.|Act::Keep, adapt or drop the change. If fares are the barrier, test a second idea, such as a nearby partner laboratory or a home extraction service.}}
<div class="table-wrap"><table><thead><tr><th>QI element</th><th>Good practice</th><th>Common error</th></tr></thead><tbody>
<tr><td>Aim</td><td>Specific, measurable, time-bound</td><td>&ldquo;Improve monitoring&rdquo;</td></tr>
<tr><td>Measure</td><td>One outcome measure, one process measure, one balancing measure</td><td>Only an end-of-year average</td></tr>
<tr><td>Change</td><td>Small, tested on a few patients first</td><td>A unit-wide policy on day one</td></tr>
<tr><td>Data</td><td>Weekly or monthly points on a run chart</td><td>Before-and-after comparison only</td></tr>
<tr><td>Learning</td><td>Each cycle recorded with prediction and result</td><td>Cycles remembered but not written</td></tr>
</tbody></table></div>
<div class="tc-keyp"><span class="tc-lab">At your stage</span><strong>Intern:</strong> collect data honestly and record misses without blame. <strong>Resident:</strong> run one PDSA cycle with your team during the rotation. <strong>Fellow:</strong> lead a project through several cycles, present the run chart at the unit&rsquo;s continuous quality improvement (CQI) meeting, and hand it on when you rotate.</div>
{{key:Measure often, change one thing at a time, and let the run chart, not the average, tell you whether it worked.}}
"""),
  ('research-ethics', 'Research ethics', 'When a project becomes research: ethics review in the Philippines', """
<p>The line between QI and research matters because research asks people to accept risks or burdens for knowledge that may benefit others, and that requires independent review. A unit project that changes how reminders are given, uses data the unit already collects, and is meant only to improve local care usually sits on the QI side. A project that randomizes patients, adds tests or contacts beyond usual care, collects data for a general conclusion, or is planned for publication often crosses into research. When in doubt, the decision belongs to a research ethics committee, not to the investigator.</p>
<p>In the Philippines, the Philippine Health Research Ethics Board (PHREB) promulgated the National Ethical Guidelines for Research Involving Human Participants in 2022.[[ntr35_11]] Internationally, the World Medical Association&rsquo;s Declaration of Helsinki, revised in 2024 with the title &ldquo;Ethical Principles for Medical Research Involving Human Participants,&rdquo; requires that a research protocol be submitted to a research ethics committee for consideration, comment, guidance and approval before the study begins.[[ntr35_12]] Data handling falls under the Data Privacy Act (Module 33).</p>
<div class="table-wrap"><table><thead><tr><th>Feature of the project</th><th>Leans toward QI</th><th>Leans toward research</th></tr></thead><tbody>
<tr><td>Purpose</td><td>Improve care in this unit</td><td>Produce generalizable knowledge</td></tr>
<tr><td>Intervention</td><td>Implementing known good practice</td><td>Testing an unproven intervention</td></tr>
<tr><td>Allocation</td><td>Everyone gets the change</td><td>Random or deliberate allocation</td></tr>
<tr><td>Burden on patients</td><td>None beyond usual care</td><td>Extra tests, visits, questionnaires or risks</td></tr>
<tr><td>Data</td><td>Routine data, kept within the unit</td><td>New data, shared or published</td></tr>
<tr><td>What to do</td><td>Follow the hospital&rsquo;s QI process; ask the research ethics committee if unsure</td><td>Write a protocol and get research ethics committee approval before starting</td></tr>
</tbody></table></div>
<p>Two Philippine pressures deserve care. Families often defer to the physician and may agree to anything asked of them in a hospital; consent must be informed, voluntary and free of any suggestion that care depends on it. And patients who pay out of pocket for medicines may join a trial to get free drugs; that is a legitimate benefit, but it raises the duty to explain what happens when the trial ends.</p>
<div class="tc-keyp"><span class="tc-lab">At your stage</span><strong>Intern:</strong> never collect data for a project without knowing whether it has approval. <strong>Resident:</strong> ask the research ethics committee before you start a case series or audit you plan to publish. <strong>Fellow:</strong> write the protocol, including how data are protected, and submit it before the first patient.</div>
{{key:If you plan to publish, randomize, or add any burden for patients, it is research until a research ethics committee says otherwise. Ask before you start.}}
"""),
  ('teaching', 'Teaching', 'Teaching on the run: the one-minute preceptor and feedback', """
<p>Most clinical teaching in a Philippine hospital happens in the corridor, between admissions, with a fellow teaching a resident and a resident teaching an intern. The mechanism of good teaching under these conditions is to make the learner&rsquo;s reasoning visible, correct it precisely and give one rule they can carry.</p>
<p>Neher and colleagues described five microskills for this setting: get a commitment, probe for supporting evidence, teach a general rule, reinforce what was done right, and correct mistakes.[[ntr35_13]] The model was described from experience and was well received by teachers; it is a practical framework rather than a trial-tested intervention. Ramani and Krackov&rsquo;s review of the feedback literature offers twelve tips for clinical teachers, among them establishing a respectful learning climate, basing feedback on direct observation, making it timely and regular, using specific, neutral language about performance rather than the person, and ending with an action plan.[[ntr35_14]]</p>
<div class="table-wrap"><table><thead><tr><th>Microskill</th><th>What you say</th><th>In the journal club case</th></tr></thead><tbody>
<tr><td>Get a commitment</td><td>&ldquo;What do you think we should do for Mr. Lim?&rdquo;</td><td>Mia commits: add finerenone</td></tr>
<tr><td>Probe for evidence</td><td>&ldquo;What makes you say that?&rdquo;</td><td>She cites the 18% reduction</td></tr>
<tr><td>Teach a general rule</td><td>&ldquo;Always translate a relative effect into absolute numbers.&rdquo;</td><td>21.1% to 17.8%, NNT about 30 over 2.6 years</td></tr>
<tr><td>Reinforce what was right</td><td>&ldquo;You chose a trial that matches his eGFR and albuminuria.&rdquo;</td><td>Specific praise</td></tr>
<tr><td>Correct mistakes</td><td>&ldquo;The headline slide left out the baseline and the harm.&rdquo;</td><td>Add hyperkalemia and cost</td></tr>
</tbody></table></div>
<p>Feedback works best when it is about something you saw, given soon, in private when it is corrective, and paired with one thing to do next time. &ldquo;Good job&rdquo; teaches nothing; &ldquo;Your first slide gave the relative reduction without the event rates; next time put both on the same line&rdquo; teaches a habit.</p>
<div class="tc-keyp"><span class="tc-lab">At your stage</span><strong>Intern:</strong> ask for feedback on one specific task each week. <strong>Resident:</strong> use the five microskills once a day with your intern. <strong>Fellow:</strong> observe a resident directly at least once a week, give feedback that names the behavior, and agree on one action.</div>
{{key:Teach by getting a commitment and correcting the reasoning, not by lecturing the answer. Feedback names a behavior you saw and one thing to do next.}}
"""),
 ],
 'debrief': [
  '<p><strong>Absolute numbers for Mr. Lim.</strong> The ARR for FIDELIO-DKD&rsquo;s primary outcome is 21.1% minus 17.8%, 3.3 percentage points over a median 2.6 years, and the crude NNT is about 30. For Mr. Lim and his daughter: &ldquo;In the trial, out of 100 people like you, about 21 on placebo and about 18 on finerenone had kidney failure, a large fall in kidney function, or died from kidney causes over about two and a half years. About 2 in 100 had to stop the drug because of high potassium, compared with about 1 in 100 on placebo. The drug is paid out of pocket.&rdquo; Then check whether he resembles the trial population, including the SGLT2 inhibitor he already takes, and let the family weigh it with the attending.</p>',
  '<p><strong>The traps.</strong> &ldquo;Reduces progression by 18%&rdquo; is a relative effect without a baseline; replace it with event rates and time. The primary outcome is a composite that includes a laboratory threshold, so say which parts are felt by patients. The combination trial measured albuminuria, a surrogate, over 180 days, so &ldquo;prevents dialysis&rdquo; is a hypothesis. &ldquo;SGLT2 inhibitors already do the job&rdquo; is a claim about background therapy: check the baseline table for how many FIDELIO-DKD participants were on one, and do not rescue the argument with a post hoc subgroup unless it meets credibility criteria. Cost is a legitimate part of the decision, not a reason to skip the numbers.</p>',
  '<p><strong>The fellow&rsquo;s project.</strong> The missed potassium checks are a process failure, so a QI project fits: an aim such as 90% of new starts with a timely potassium within three months, a weekly run chart, and small PDSA cycles starting with a pre-printed request and return date, then a nearby laboratory if fares are the barrier. It implements known good practice, uses routine data and adds no burden, so it leans toward QI under the hospital&rsquo;s process. If the team later wants to publish it or compare strategies by allocation, they write a protocol and ask the research ethics committee first.</p>',
 ],
 'skills': {'title': 'Evidence, quality improvement and teaching',
  'intro': 'Complete with a preceptor or program director, at journal club, a CQI meeting or on the ward. Sign-off is local.',
  'items': [('Presents one randomized trial with population, comparison, outcome, absolute risk reduction, NNT and harms on the first slide', False),
            ('Labels each outcome in a trial as felt by patients or surrogate and explains why', False),
            ('Applies subgroup credibility criteria to one published subgroup claim', False),
            ('Designs a PDSA cycle with an aim, measures and a run chart, and presents it at a CQI meeting', False),
            ('Decides with the research ethics committee whether a project is QI or research', False),
            ('Teaches a learner with the five microskills and gives specific feedback with an action plan, observed by a preceptor', False)],
  'placement': 'Journal club, CQI meeting, ward rounds or teaching session'},
 'quiz': [
  ('An intern summarizes a trial: &ldquo;The drug reduced albuminuria by 30%.&rdquo; Which description of this outcome is correct?',
   ['A patient-felt outcome equivalent to preventing dialysis',
    'A surrogate marker associated with kidney outcomes, which by itself does not show fewer kidney failures or deaths',
    'A safety outcome',
    'A composite of hard outcomes'],
   1,
   'Albuminuria is a laboratory surrogate. Treating it as equivalent to preventing dialysis (the tempting distractor) is the error CONFIDENCE illustrates: it measured albuminuria at 180 days, not kidney failure.'),
  ('In FIDELIO-DKD, a trial in diabetic kidney disease (DKD), the primary outcome occurred in 17.8% with finerenone and 21.1% with placebo over a median 2.6 years. What are the absolute risk reduction and crude number needed to treat?',
   ['18% and about 6',
    '3.3 percentage points and about 30',
    '0.82 and about 1',
    '33 percentage points and about 3'],
   1,
   'ARR = 21.1% minus 17.8% = 3.3 percentage points; NNT = 1 divided by 0.033, about 30 over the trial period. The 18% figure (the tempting distractor) is the relative reduction implied by the hazard ratio, not the absolute one.'),
  ('A fellow wants to compare two reminder methods for potassium checks by randomly assigning clinic patients to each, and to publish the results. What is required?',
   ['Nothing, because reminders are low risk',
    'Approval from the hospital pharmacy',
    'A protocol submitted to a research ethics committee and approved before the first patient is enrolled',
    'Verbal agreement from the attending only'],
   2,
   'Random allocation and intent to publish make this research; the Declaration of Helsinki requires research ethics committee review before the study begins, and PHREB&rsquo;s 2022 guidelines govern Philippine practice. Low risk (the tempting distractor) affects the type of review, not whether review is needed.'),
  ('A resident&rsquo;s slide says a drug &ldquo;worked especially well in women&rdquo; based on one of 24 subgroups in the forest plot, not prespecified, with no interaction test reported. How should the fellow respond?',
   ['Accept it, because the confidence interval in women excludes 1',
    'Treat it as hypothesis-generating: it fails several credibility criteria, including prespecification, few subgroups tested and a test for interaction',
    'Recommend the drug only for women',
    'Conclude the drug does not work in men'],
   1,
   'Subgroup credibility criteria ask about prespecification with a stated direction, the number of subgroups and the interaction test. A confidence interval within one subgroup (the tempting distractor) does not show that the effect differs between subgroups.'),
  ('A dialysis unit tested a new catheter-care checklist and reports only that infections were 1.1 per 100 patient-months the year before and 0.9 the year after. What is the best next step to judge whether the change helped?',
   ['Conclude it worked because the rate fell',
    'Plot monthly rates on a run chart with the change date marked, and look for a sustained shift rather than a before-and-after average',
    'Stop collecting data because the result is positive',
    'Change three more processes at once'],
   1,
   'Run charts show timing and persistence that a before-and-after average hides. Concluding success from two averages (the tempting distractor) cannot separate improvement from ordinary variation or other changes.'),
 ],
 'terms': [('ARR', 'Absolute risk reduction'),
           ('CKD', 'Chronic kidney disease'),
           ('CONFIDENCE', 'Name of a 2025 randomized trial of finerenone, empagliflozin or both in CKD and type 2 diabetes'),
           ('CONSORT', 'Consolidated Standards of Reporting Trials'),
           ('CQI', 'Continuous quality improvement'),
           ('eGFR', 'Estimated glomerular filtration rate'),
           ('FIDELIO-DKD', 'Finerenone in Reducing Kidney Failure and Disease Progression in Diabetic Kidney Disease (trial)'),
           ('FIGARO-DKD', 'Finerenone in Reducing Cardiovascular Mortality and Morbidity in Diabetic Kidney Disease (trial)'),
           ('GRADE', 'Grading of Recommendations Assessment, Development and Evaluation'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('NNT', 'Number needed to treat'),
           ('PDSA', 'Plan-do-study-act'),
           ('PHREB', 'Philippine Health Research Ethics Board'),
           ('QI', 'Quality improvement'),
           ('SGLT2', 'Sodium-glucose cotransporter 2')],
 'readings': [('attending-nephrologist-23-supervision-qi.html', 'Attending Nephrologist, Module 23: Supervision and Quality Improvement'),
              ('dialysis-qapi-vs-cqi.html', 'Dialysis QAPI versus CQI'),
              ('ai-in-nephrology-practice.html', 'AI in Nephrology Practice')],
 'calcs': ['calc-qapi-run-chart-spc.html', 'calc-qapi-cqi-toolkit.html', 'calc-qapi-meeting-wizard.html', 'calc-kfre.html', 'calc-dkd-risk.html'],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
