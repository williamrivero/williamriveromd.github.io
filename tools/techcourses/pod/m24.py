# -*- coding: utf-8 -*-
"""Physician on Duty, Module 24: Symptoms in the Chair and at Home (cramps, itch, sleep, pain, and fatigue).
Written for this series from published sources."""

MODULE = {
    "image_alt": "A middle-aged Filipino man in a dialysis chair scratches his forearm and rubs his calf. The physician on duty sits at his eye level holding a symptom card, while a nurse gently stretches his leg.",
    "objectives": [
        "Explain the causes of muscle cramps during dialysis and carry out the bedside response and prevention steps per your unit&rsquo;s protocol.",
        "Triage nausea, vomiting, headache, itching, back pain, and chest tightness during a session, and name the features that signal a serious cause.",
        "Assess chronic kidney disease&ndash;associated pruritus, restless legs syndrome, insomnia, chronic pain, and post-dialysis fatigue, and state what is known about their causes.",
        "Describe the treatments that are supported in dialysis patients and the strength of evidence for each, including difelikefalin, gabapentinoids, intravenous iron for restless legs, exercise, and pain coping skills training.",
        "Measure symptom burden with a simple validated score and track it over time.",
        "Reduce early sign-offs by treating the symptom rather than ending the session, and know when to call the attending nephrologist.",
    ],
    "big": """
{{plain:Picture a backpack that gets heavier one small stone at a time. No single stone is heavy. A patient carrying itch, poor sleep, aching legs, and a long tiredness after each session is carrying all the stones at once, and each one makes the others harder to bear.}}
<p>The picture has a limit. Stones sit side by side; symptoms feed one another through shared causes. Uremic retention solutes (wastes that dialysis removes only partly), inflammation, anemia, and the stress of each session act on several symptoms together, and low mood amplifies all of them.</p>
{{cards:Key terms for this module|Symptom burden::How many symptoms a patient carries, how severe, and how much they interfere with life.|Chronic kidney disease&ndash;associated pruritus (CKD-aP)::Itch caused by kidney failure, also called uremic pruritus.|Restless legs syndrome (RLS)::An urge to move the legs at rest, worse in the evening, eased by movement.|Gabapentinoids::Gabapentin and pregabalin, nerve-calming drugs cleared by the kidneys.|Kappa-opioid agonist::A drug that stimulates kappa-opioid receptors, which damp itch. Difelikefalin is one.|Recovery time::The hours a patient needs after a session to feel normal.|Early sign-off::Ending a session early at the patient&rsquo;s request.}}
<p>Most of these symptoms do not threaten life, which is why they are overlooked. A few &ldquo;small&rdquo; complaints are the first sign of something serious. Your work is to ask, to measure, to offer what is safe, and to recognize the complaint that is not small.</p>
""",
    "case": {"title": "He signs off early every Friday", "html": """
<p>Mr. Eduardo Manalastas, 55, is a jeepney operator who has been on hemodialysis for three years. He dialyzes on Mondays, Wednesdays, and Fridays, four hours each session. On Fridays he often asks to come off 45 to 60 minutes early (illustrative values).</p>
<p>Today is Friday. At hour three he again asks to stop. His calves cramp. His skin itches &ldquo;so much I cannot sleep.&rdquo; In the evening his legs &ldquo;will not stay still.&rdquo; He sleeps about four hours a night. He says it takes him &ldquo;until Saturday night&rdquo; to feel normal after dialysis.</p>
<p>His blood pressure is 128/76 mm Hg and his pulse is 84 per minute and regular. He is 0.8 kg above his target weight. His transferrin saturation, a measure of the iron available for making red cells, was low last month (all values illustrative). The nurse, Ms. Carmela Dizon, has already stretched his calf, and the cramp has eased.</p>
""", "questions": ["Is it safe to continue, and what will you do in the next 15 minutes instead of ending the session?",
                  "Which of his symptoms have a treatable cause, and what is the first step for each?",
                  "What will you measure today, and what will you tell the attending nephrologist?"]},
    "sections": [
        ("burden", "Symptom burden", "The miserable but stable patient", """
<p>Most dialysis patients carry several symptoms at once. Murtagh and colleagues pooled 59 studies of dialysis patients in a systematic review. The weighted average prevalence was 71% for fatigue, 55% for itch, 53% for constipation, 47% for pain, 44% for sleep disturbance, 30% for restless legs, and 27% for depression.[[murtagh2007]] Ranges were wide because definitions differed.</p>
<h3>Why symptoms cluster</h3>
<p>A healthy kidney clears waste continuously; dialysis clears it in bursts, and some molecules poorly. Retained solutes and inflammation are thought to act on nerves, skin, muscle, and brain. Sleep loss sits in the middle of this web: itch, restless legs, and pain break sleep, and broken sleep worsens pain, mood, and energy. One treatable symptom therefore often drives two or three others.</p>
<h3>Symptoms go unreported</h3>
<p>Patients often do not mention symptoms, and staff often do not ask. In the Dialysis Outcomes and Practice Patterns Study (DOPPS), a large international cohort, 17% of patients who were nearly always bothered by itch had not told the dialysis staff. Of 268 medical directors, 69% underestimated how common itch was in their own unit.[[rayner2017]]</p>
<p>A 2022 Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference concluded that care systems should provide individualized symptom assessment and management, led by nephrology teams, while acknowledging that evidence for many treatments is limited.[[mehrotra2023]] These are conference conclusions, not graded recommendations.</p>
<div class="table-wrap"><table>
<thead><tr><th>Symptom</th><th>Question to ask on your round</th><th>Where this module covers it</th></tr></thead>
<tbody>
<tr><td>Cramps</td><td>Do your muscles cramp during or after dialysis? When in the session?</td><td>Muscle cramps</td></tr>
<tr><td>Itch</td><td>How bad was your worst itch this week, from 0 to 10? Does it wake you?</td><td>Itch</td></tr>
<tr><td>Restless legs</td><td>Do your legs feel an urge to move when you sit or lie still, especially in the evening?</td><td>Restless legs and poor sleep</td></tr>
<tr><td>Sleep</td><td>How many hours do you sleep? Do you snore or fall asleep during the day?</td><td>Restless legs and poor sleep</td></tr>
<tr><td>Pain</td><td>Where does it hurt, how strong is it from 0 to 10, and what does it stop you doing?</td><td>Chronic pain</td></tr>
<tr><td>Tiredness</td><td>How long does it take you to recover from a dialysis session?</td><td>Fatigue and recovery</td></tr>
<tr><td>Mood</td><td>Have you felt down or lost interest in things lately?</td><td>Module 26</td></tr>
</tbody></table></div>
{{key:If you do not ask, the patient will not tell you. Ask one question each round: what bothers you most this week?}}
"""),
        ("inchair", "During the session", "Symptoms during the session: common cause, first step, when to worry", """
<p>Think of a traffic light for each symptom. Green is a common cause the protocol handles. Amber means look for the cause. Red means stop and call. The vital signs decide the color more often than the symptom does (Module 11).</p>
<p>The usual causes come from the session itself. Fluid removal lowers plasma volume and pressure (Module 13). Rapid removal of urea can shift water into the brain and cause headache, nausea, and sometimes confusion, a picture called dialysis disequilibrium. Some patients react to the dialyzer or tubing in the first minutes (Module 16).[[daugirdas2015]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Symptom</th><th>Common cause</th><th>First step, per your unit&rsquo;s protocol</th><th>When to worry</th></tr></thead>
<tbody>
<tr><td>Cramps</td><td>Fluid removal faster than refilling. Low pressure. Large weight gain</td><td>Check the pressure. Stretch the muscle. Fluid steps as the protocol allows</td><td>Low pressure. Cramps every session. Cramps early in the session</td></tr>
<tr><td>Nausea and vomiting</td><td>Falling pressure. Disequilibrium early in dialysis life. Eating during the session</td><td>Check the pressure. Treat a low pressure first. Turn the patient to the side if vomiting</td><td>Confusion, severe headache, chest pain, abdominal pain, or a low pressure that does not recover</td></tr>
<tr><td>Headache</td><td>High or low pressure. Caffeine withdrawal. Disequilibrium</td><td>Check the pressure and the blood sugar per protocol</td><td>Sudden, severe, or &ldquo;worst ever&rdquo; headache. Vomiting. A new neurologic sign. Very high pressure</td></tr>
<tr><td>Itch</td><td>Chronic kidney disease&ndash;associated pruritus, often worse in the chair</td><td>Skin care. Record a 0-to-10 score</td><td>Itch with flushing, wheeze, or swelling in the first minutes of a session</td></tr>
<tr><td>Back pain</td><td>Posture in the chair. Musculoskeletal pain</td><td>Reposition. Check the pressure</td><td>Onset in the first minutes with chest tightness, or with translucent red blood in the line</td></tr>
<tr><td>Chest tightness</td><td>Many causes, some dangerous</td><td>Vital signs and an electrocardiogram (ECG) per protocol</td><td>Always. Follow Module 15 for chest pain and Module 16 for early reactions</td></tr>
</tbody></table></div>
<p>This table rests on physiology and clinical experience, not trials. For disequilibrium (Module 12), a systematic review of 49 small reports covering 321 patients of all ages listed nausea (25.2%), headache (24.8%), vomiting (23.9%), and cramps (18.1%) as the commonest symptoms.[[raina2022]] Use it for the symptom list only.</p>
{{fig:idh|Low blood pressure during dialysis at a glance. Cramps, nausea, and yawning are often its first signs.}}
<h3>Nausea and vomiting</h3>
{{flow:Nausea and vomiting during dialysis|Protect the airway::Turn the head and body to the side if vomiting. Do not sit up a patient whose pressure may be low.|Check vital signs::A low pressure, the commonest cause, is treated first (Module 13).|Ask what came with it::Headache, confusion, chest pain, abdominal pain, or fever point beyond the session.|Look at the context::Time into the session, fluid removed, a recent meal, and whether the patient is new to dialysis.|Treat per protocol::Once a dangerous cause is unlikely.|Call::For vomiting with confusion, severe headache, chest or abdominal pain, or a pressure that does not recover.}}
<h3>Headache</h3>
<p>Most headaches during dialysis recur in the same mild pattern. Common contributors are a change in pressure, caffeine withdrawal, and, in new patients, disequilibrium.[[daugirdas2015]] A headache new in character is different.</p>
{{flow:Headache during dialysis|Check the pressure::Very high and low pressures both cause headache. Treat per protocol.|Ask about the pattern::The usual headache, or new, sudden, or the worst ever?|Check the brain::Alertness, speech, pupils, and limb strength.|Check the blood sugar::Per protocol, in a patient with diabetes.|Treat the usual headache::As the protocol allows.|Call at once for red flags::Sudden severe headache, vomiting with confusion, or a new neurologic sign. Start the emergency protocol while you call, and report the heparin given (Modules 18 and 19).}}
{{call:Stop and call the attending nephrologist when any &ldquo;minor&rdquo; symptom comes with abnormal vital signs, when a headache is sudden or severe, when vomiting comes with confusion, when there is chest pain or pressure, or when a symptom begins within minutes of starting with a new dialyzer. Follow the unit&rsquo;s protocol while you call.}}
{{key:Check the vital signs before you treat the symptom. Then treat the cause, not only the symptom.}}
"""),
        ("cramps", "Muscle cramps", "Muscle cramps", """
<p>Picture a muscle whose blood supply and salt balance changed faster than it could adapt. A cramp is a sustained, painful, involuntary contraction, usually of the calves, feet, or thighs, late in the session.</p>
<h3>What breaks</h3>
<p>The machine removes water only from the blood, and refilling from the tissues has a speed limit (Module 13). When removal outruns refilling, plasma volume falls. The body tightens the limb vessels to protect the vital organs, and the muscles receive less blood. Plasma sodium and osmolality also shift during the session. Reduced muscle perfusion and these shifts around nerve endings are thought to trigger the cramp.[[daugirdas2015]] The exact mechanism is not settled.</p>
<p>This chain explains the pattern: cramps cluster late in the session, after large weight gains, in patients whose target weight (dry weight, Module 8) is set too low, and with a falling pressure.</p>
{{fig:cramps|A cramp in the chair. The nurse stretches the muscle while you check the pressure.}}
<h3>At the chair</h3>
<p>The nurse stretches the muscle, and a low pressure gets the Module 13 response. Your task is to read the cause.</p>
{{fig:pod24_cramp_stretch}}
<div class="table-wrap"><table>
<thead><tr><th>Question you ask</th><th>What it tells you</th><th>Whom it concerns</th></tr></thead>
<tbody>
<tr><td>What is the pressure and pulse now?</td><td>A cramp with a low pressure is a hypotension episode</td><td>You, now (Module 13)</td></tr>
<tr><td>How much weight was gained since the last session?</td><td>A large gain means a fast fluid removal rate</td><td>The patient and the dietitian</td></tr>
<tr><td>Is it near target weight, and every session?</td><td>The target may be too low. A pattern is a prescription problem</td><td>The attending nephrologist</td></tr>
<tr><td>Is it early in the session?</td><td>An early cramp with little fluid removed suggests another cause</td><td>You, and the nephrologist</td></tr>
</tbody></table></div>
<h3>What the evidence says about preventing cramps</h3>
<p>No drug is established. A 2024 systematic review found 13 studies of nine drugs. Vitamins C and E were the most studied and showed positive results, but only the L-carnitine and creatine trials were at low risk of bias.[[mantilla2024]] A meta-analysis found fewer cramps with L-carnitine in five small trials with 147 participants (pooled odds ratio 0.22), but a trial sequential analysis, a test of whether enough data have accumulated, judged the evidence insufficient.[[chewcharat2022]] In a review of aerobic exercise, a single trial reported less cramping.[[hargrove2021]]</p>
<p>All of this is low-certainty evidence. The surest prevention follows the physiology: a smaller weight gain, a slower fluid removal rate, and a correct target weight. These belong to the prescription, so you report the pattern and the nephrologist decides.</p>
{{key:A cramp is a message about fluid removal. Treat the cramp, then read the message.}}
"""),
        ("itch", "Itch", "Itch (chronic kidney disease&ndash;associated pruritus)", """
<p>Picture an alarm wired to the wrong switch. The skin is not damaged, but the nerve sends the itch signal anyway. Scratching relieves it briefly, damages the skin, and damaged skin itches more.</p>
<h3>What is thought to happen</h3>
<p>The mechanism is not fully known. Proposed contributors are immune dysregulation, dry skin, retained uremic solutes, and an imbalance in the body&rsquo;s own opioid system: mu-opioid signaling tends to promote itch, while kappa-opioid signaling is thought to damp it. This is the rationale for kappa-opioid drugs.[[fishbane2020]] These are hypotheses that guide treatment, not proven causes.</p>
{{fig:pod24_why_itch}}
<p>Two common beliefs need correction. In DOPPS, medical directors ranked control of a high phosphate and a low Kt/V (a surrogate measure of dialysis dose) as the most important interventions for itch. Neither was associated with itch in the patient data.[[rayner2017]] Both matter for other reasons, but not as itch treatments. Antihistamines were the commonest first-line treatment, yet they lack good trial evidence for this itch.[[rayner2017]][[hercz2020]]</p>
<h3>What the evidence shows</h3>
<p>A Cochrane review included 92 randomized trials with 4,466 participants. Gabapentin and pregabalin reduced itch by about 4.95 cm on a 10-cm visual analog scale versus placebo (5 studies, 297 participants). Kappa-opioid agonists, including nalfurafine, reduced it by about 1.05 cm (6 studies, 661 participants). The review rated both findings high-certainty evidence. Ondansetron had little or no effect. Many trials were small, and harms were poorly reported.[[hercz2020]] An earlier review of 44 trials agreed.[[simonsen2017]]</p>
<p>Difelikefalin is a kappa-opioid agonist that acts mainly outside the brain, given intravenously three times a week after dialysis. The KALM-1 phase 3 trial randomized 378 patients with moderate to severe itch to difelikefalin or placebo for 12 weeks. A fall of at least 3 points on the Worst Itch Numerical Rating Scale (WI-NRS, 0 to 10) occurred in 51.9% of the difelikefalin group and 30.9% of the placebo group. Diarrhea, dizziness, and vomiting were more common with the drug.[[fishbane2020]] A pooled analysis of KALM-1 and its companion trial KALM-2 (851 patients) found 51.1% versus 35.2%.[[topf2022]] The manufacturer funded both trials.</p>
{{formula:<strong>Illustrative trial arithmetic.</strong> Absolute risk reduction (ARR) = response with drug &minus; response with placebo. Number needed to treat (NNT) = 100 &divide; ARR in percentage points, rounded up.<br>KALM-1: 51.9% &minus; 30.9% = 21.0 percentage points. NNT = 100 &divide; 21.0 = 4.8, so about 5 patients treated for 12 weeks for one more responder.[[fishbane2020]]<br>Pooled KALM-1 and KALM-2: 51.1% &minus; 35.2% = 15.9 points. NNT = 100 &divide; 15.9 = 6.3, so about 7.[[topf2022]]<br><strong>What it tells you:</strong> the drug helps a meaningful minority beyond placebo. <strong>What it does not:</strong> which patient will respond. The 31% placebo response shows how much itch improves with attention and time alone.}}
<p>The trade: gabapentinoids show larger effects in small trials but accumulate in kidney failure and cause drowsiness and falls (Module 20); difelikefalin has a modest effect in larger trials, and its availability in the Philippines was not verified for this module.</p>
{{flow:Itch treatment ladder (the nephrologist prescribes)|Measure::Worst itch over the past week, 0 to 10. Record it.|Look at the skin::Dryness, scratch marks, nodules, infection, or a rash suggesting another cause.|Skin care for everyone::Moisturizer, short nails, lukewarm baths, and loose cotton clothing.|Review the basics with the nephrologist::Dialysis adequacy, phosphate, and other causes such as liver disease or a drug reaction.|Drug treatment by the nephrologist::Gabapentinoids and kappa-opioid agonists have the strongest evidence. Choice, dose, and monitoring belong to the nephrologist.|Track::Repeat the score monthly and report the change.}}
{{key:Itch in dialysis is common, under-reported, and treatable. Measure it like a vital sign.}}
"""),
        ("restless", "Restless legs and sleep", "Restless legs and poor sleep", """
<p>Picture legs that want to move at the very moment the patient must sit still for four hours. Restless legs syndrome (RLS) is an urge to move the legs, usually with unpleasant feelings, that starts or worsens at rest, eases with movement, and is worse in the evening. Diagnosis rests on these features and on excluding mimics such as cramps and neuropathy (the International Restless Legs Syndrome Study Group criteria).[[sloand2004]]</p>
<h3>How common it is</h3>
<p>A 2024 meta-analysis of 57 studies with 12,573 maintenance hemodialysis patients estimated a pooled prevalence of 24.0%.[[liu2024]] A systematic review of RLS in chronic kidney disease found most dialysis studies reporting 15% to 30%, two to three times the rate in the general population.[[safarpour2023]]</p>
<h3>Why iron matters</h3>
<p>Movement control depends on dopamine signaling in the brain, and the brain needs iron to handle dopamine. Low brain iron is thought to disturb this pathway. Dialysis patients lose iron through blood left in the circuit, blood tests, and bleeding, so iron deficiency is common (Module 21) and is a treatable contributor worth excluding first.</p>
{{fig:pod24_rls_iron}}
<p>The trial evidence is thin. In a double-blind trial, 25 dialysis patients with RLS received one infusion of intravenous iron dextran or saline. RLS scores improved with iron at 1 and 2 weeks; by 4 weeks the difference was no longer significant.[[sloand2004]] A systematic review lists dopamine-acting drugs, gabapentinoids, vitamins C and E, intravenous iron, and exercise as studied treatments, with limited data.[[safarpour2023]] Two exercise trials reported fewer RLS symptoms, with moderate to high risk of bias.[[hargrove2021]] Drug choice belongs to the nephrologist.</p>
<p>Check the iron indices with the site&rsquo;s transferrin saturation calculator; iron treatment follows the anemia plan (Module 21).</p>
<h3>Poor sleep</h3>
<p>Insomnia in dialysis rarely has one cause. Look for the drivers before anyone reaches for a sleeping tablet.</p>
{{cards:Sleep: causes to look for|Itch::Scratching at night breaks sleep. Treating itch often restores it.|Pain::Ask whether pain wakes the patient.|Restless legs::The urge to move peaks at bedtime.|Sleep apnea::Loud snoring, pauses in breathing, and daytime sleepiness. Fluid overload can worsen it.|Mood::Low mood and worry disturb sleep. Module 26 covers screening.|Napping in the chair::A long sleep during dialysis steals from the night.|Shift time::An early-morning shift means waking before dawn three times a week.}}
<p>Proven treatments are scarce. In a randomized trial at 26 dialysis units in the United States, 126 patients with chronic insomnia received cognitive behavioral therapy for insomnia (CBT-I), trazodone, or placebo for 6 weeks. Neither beat placebo on the Insomnia Severity Index at 7 or 25 weeks. Serious adverse events, particularly cardiovascular events, were more frequent with trazodone.[[mehrotra2024]] The trial was modest and most participants had mild or moderate insomnia, so it does not close the question. It does argue against reflex sedatives.</p>
<p>The site&rsquo;s Pittsburgh Sleep Quality Index calculator describes sleep quality. Report snoring with daytime sleepiness as possible sleep apnea.</p>
{{key:Before any pill for restless legs, ask about iron. Before any pill for sleep, ask why the patient cannot sleep.}}
"""),
        ("pain", "Chronic pain", "Chronic pain", """
<p>Picture the usual pain ladder, from simple analgesics to strong opioids. In kidney failure the rungs are shorter and more slippery: several drugs, or their breakdown products, are cleared by the kidneys and build up, so a usual dose can cause confusion, sedation, or a fall.</p>
<h3>Where the pain comes from</h3>
<p>Sources include joints and muscles, diabetic nerve damage, the access, bone disease, and, rarely, calciphylaxis, a painful calcification of small skin vessels with dark, tender lesions (Module 21). The cause comes before the drug.</p>
<h3>What the evidence shows</h3>
<p>A review from the Hemodialysis Opioid Prescription Effort (HOPE) Consortium reports that half of hemodialysis patients have chronic moderate to severe pain. Opioids are prescribed more often than in the general population, and their use is associated with more illness and death, partly because sicker patients receive more opioids. Evidence that opioids work for chronic pain in dialysis patients is lacking.[[tobin2022]]</p>
<p>Morphine and codeine are not recommended because their metabolites accumulate and cause neurotoxicity. Buprenorphine is discussed as a safer option.[[coluzzi2020]][[tobin2022]] These are narrative reviews based on pharmacology, not trials. Tramadol and nonsteroidal anti-inflammatory drugs (NSAIDs) carry their own risks (Module 20).</p>
<p>A nondrug treatment now has trial support. The HOPE Consortium trial randomized 643 hemodialysis patients with chronic pain to pain coping skills training (12 weekly coach-led sessions by video or telephone, then 12 weeks of daily automated calls) or usual care. At 12 weeks, pain interference on the Brief Pain Inventory (0 to 10) fell 0.49 points more with training. A clinically meaningful improvement, a fall of more than 1 point, occurred in 50.9% versus 36.6%. The effect persisted at 24 weeks and had diminished by 36 weeks.[[dember2025]]</p>
{{formula:<strong>Illustrative trial arithmetic: averages and responder rates.</strong> ARR = 50.9% &minus; 36.6% = 14.3 percentage points. NNT = 100 &divide; 14.3 = 7.0, so about 7 patients trained for one more meaningful improvement at 12 weeks.[[dember2025]]<br>Mean between-group difference = 0.49 points on a 0-to-10 scale.<br><strong>What it tells you:</strong> a small average change can hide a useful benefit in a subset of patients. <strong>What it does not:</strong> which patients will respond, or whether the benefit lasts beyond six months.}}
{{flow:Chronic pain approach|Assess::Where, how strong from 0 to 10, and what it stops the patient doing.|Find the cause::Joints, nerves, the access, bone, skin lesions, or a new fracture or infection.|Nondrug measures::Positioning, heat or cold, activity, and coping skills support where available.|Review every analgesic::Prescription, over-the-counter, and herbal products.|Flag drugs that accumulate::Morphine, codeine, tramadol, gabapentinoids, and NSAIDs (Module 20).|Report::The score, the suspected cause, and the drug list. The nephrologist chooses any drug and dose.}}
<p>Do not start or escalate an opioid in the chair. Drowsiness, confusion, or limb jerking (myoclonus) on an opioid or a gabapentinoid is toxicity until proven otherwise.</p>
{{call:Stop and call the attending nephrologist for new severe pain, painful dark or ulcerated skin lesions that may be calciphylaxis, pain with fever, or drowsiness, confusion, or myoclonus in a patient taking an opioid or a gabapentinoid. Follow the unit&rsquo;s protocol for the first minutes while you call.}}
{{key:In kidney failure, ask what is causing the pain and what the patient is already taking before anyone adds a drug.}}
"""),
        ("fatigue", "Fatigue and recovery", "Fatigue and the long recovery after dialysis", """
<p>Picture a phone that takes all night to recharge after each use. The picture has a limit: fatigue has several sources that add together. Anemia reduces oxygen delivery. Inflammation acts on the brain to produce tiredness and withdrawal. Muscle loss reduces reserve (Module 23). Low mood and broken sleep add their share. The session adds fluid removal, falls in pressure, and solute shifts.</p>
<h3>Recovery time as a measure</h3>
<p>Rayner and colleagues asked 6,040 DOPPS patients one question: &ldquo;How long does it take you to recover from a dialysis session?&rdquo; 32% answered under 2 hours, 41% 2 to 6 hours, 17% 7 to 12 hours, and 10% more than 12 hours. Longer recovery was associated with greater fluid removal during the session and a lower sodium concentration in the dialysis fluid. Compared with 2 to 6 hours, recovery longer than 12 hours was associated with a higher risk of first hospital admission (adjusted hazard ratio 1.22) and death (1.47).[[rayner2014]]</p>
{{fig:pod24_recovery_time}}
<p>This prospective cohort shows an association, and the answers are subjective. Sicker patients may both recover slowly and die sooner, and no trial has shown that shortening recovery time improves survival. The question is still worth asking because it is quick and points to contributors you can report.</p>
<p>An international Standardized Outcomes in Nephrology&ndash;Hemodialysis (SONG-HD) consensus workshop prioritized fatigue as a core outcome for trials, measured by its impact on life participation.[[ju2018]] Aerobic exercise improved fatigue in one trial.[[hargrove2021]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Contributor</th><th>What you check</th><th>Who acts on it</th></tr></thead>
<tbody>
<tr><td>Anemia</td><td>The latest hemoglobin, a surrogate marker, and the iron indices</td><td>The nephrologist, per the anemia plan (Module 21)</td></tr>
<tr><td>Large fluid removal</td><td>Weight gains and the fluid removal rate</td><td>The patient, the dietitian, and the nephrologist</td></tr>
<tr><td>Falls in pressure</td><td>Episodes of low pressure in recent sessions</td><td>The nephrologist (Module 13)</td></tr>
<tr><td>Poor sleep</td><td>Hours slept, itch, restless legs, and snoring</td><td>This module, then the nephrologist</td></tr>
<tr><td>Low mood</td><td>Loss of interest and low mood</td><td>Module 26</td></tr>
<tr><td>Inactivity and muscle loss</td><td>Walking distance and daily activity</td><td>Module 23</td></tr>
</tbody></table></div>
<p>Report a long recovery, and especially one that is getting longer. A change in a stable patient can be the first sign of a new problem, such as a falling hemoglobin or an infection.</p>
{{key:Ask how long it takes to recover. The answer is quick to get and tells you a great deal.}}
"""),
        ("measure", "Measuring and sign-offs", "Measuring symptoms and reducing early sign-offs", """
<p>What gets measured gets treated. &ldquo;A bit itchy&rdquo; is easy to dismiss; a monthly number shows whether a treatment worked.</p>
<h3>Simple validated scores</h3>
<p>The Dialysis Symptom Index asks about 30 symptoms and how much each bothers the patient. Its developers reported moderate test-retest agreement (overall kappa 0.48).[[weisbord2004]] The modified Edmonton Symptom Assessment System (ESAS) is shorter: the patient rates a short list of common symptoms from 0 to 10. In 261 hemodialysis patients followed for 6 months, the change in ESAS score accounted for 46% of the change in mental and 34% of the change in physical health-related quality of life.[[davison2006]]</p>
<p>The site&rsquo;s patient-reported outcome calculator scores the Dialysis Symptom Index, the Kidney Disease Quality of Life (KDQOL-36) symptom subscale, and the Integrated Palliative care Outcome Scale&ndash;Renal (IPOS-Renal).</p>
{{cards:Symptom score at the chair|Pick one tool::Use the score your unit has chosen. Do not mix tools from month to month.|Ask the patient to rate::Each symptom from 0 (none) to 10 (worst possible). Help with reading if needed, without suggesting answers.|Record the top symptom::Write the worst-rated symptom and its score in the note.|Compare::Look at last month&rsquo;s scores. Report the change.|Act on high scores::A high or rising score goes to the attending nephrologist.}}
{{formula:<strong>Illustrative symptom tracking.</strong> Change = later score &minus; earlier score.<br>Month 1: itch 8, sleep 7. Month 3, after the nephrologist&rsquo;s treatment: itch 3, sleep 5.<br>Itch: 3 &minus; 8 = &minus;5. Sleep: 5 &minus; 7 = &minus;2.<br><strong>What it tells you:</strong> itch improved a great deal and sleep improved less, so sleep may have another driver (restless legs, pain, apnea, or mood).[[davison2006]] <strong>What it does not:</strong> why the scores changed. Single scores vary from day to day, so report the trend, not one value.}}
<h3>Early sign-offs</h3>
<p>A request to come off early has a reason: a cramp, itch, back pain, boredom, transport, a family duty, or worry. Most can be solved without ending the treatment.</p>
{{flow:When a patient asks to sign off early|Check vital signs::A request to stop can be the first sign of a low pressure.|Ask why::Use an open question and listen.|Treat the cause per protocol::Stretch a cramp, reposition for back pain, give skin care for itch.|Solve the practical problem::Ask the charge nurse or social worker about transport and shift times.|If the patient still leaves::Respect the decision. Explain what shortened time means and record the minutes lost and the reason.|Inform the nephrologist::Report every shortened session, and a pattern above all.}}
{{formula:<strong>Illustrative arithmetic: treatment time lost.</strong> Weekly prescribed time = minutes per session &times; sessions per week.<br>240 minutes &times; 3 = 720 minutes per week.<br>Signing off 50 minutes early once a week: 50 &divide; 720 &times; 100 = 6.9% of weekly time lost.<br>Over 4 weeks: 50 &times; 4 = 200 minutes, about 3.3 hours, close to one full 4-hour session.<br><strong>What it tells you:</strong> small, repeated losses add up. <strong>What it does not:</strong> the effect on the delivered dialysis dose. Module 7 covers dose, and Module 26 covers missed and shortened sessions.}}
<p>The patient may stop; your role is to inform the decision and address the cause. The session length belongs to the nephrologist, who needs to know when it is not delivered.</p>
{{call:Stop and call the attending nephrologist when a patient who asks to stop has abnormal vital signs, new chest pain, confusion, or another red flag. Follow the unit&rsquo;s protocol for the first minutes while you call.}}
{{key:When a patient asks to sign off early, find the reason first. A treated cause often keeps the patient in the chair.}}
"""),
    ],
    "debrief": ["""
<p><strong>Is it safe to continue, and what will you do instead of ending the session?</strong> Yes, on present findings. His pressure and pulse are normal, he is alert, and he has no chest pain or headache, so the cramp is not a hypotension episode. With 0.8 kg left to remove, most of the fluid is already off. You ask what makes him want to stop: the cramp, the itch, and Friday traffic. Ms. Dizon watches the pressure, applies moisturizer to his dry forearms, and repositions him. He agrees to try to finish, knowing he may still choose to stop. If he does, you record the minutes lost and the reason and inform the attending nephrologist.</p>
<p><strong>Which symptoms have a treatable cause?</strong> The cramps come late, near his target weight, every Friday. Friday follows a short gap, so a large weight gain is a less likely cause; check it anyway. The target weight may now be too low, so the first step is to report the pattern for a review. The itch is chronic kidney disease&ndash;associated pruritus until shown otherwise: score it, examine the skin, start skin care, and report, because effective treatments exist. His evening leg symptoms fit restless legs syndrome, and his transferrin saturation was low, so confirm the iron indices and let the nephrologist decide on iron. His short sleep likely follows the itch and restless legs, so no sedative is started. His long recovery may reflect all of these.</p>
<p><strong>What will you measure and report?</strong> A worst-itch score, the four RLS features, hours of sleep and snoring, his recovery time, and the unit&rsquo;s symptom score. Your report to the attending nephrologist: recurrent Friday cramps near target weight, high itch with dry skin, probable restless legs with a low transferrin saturation, four hours of sleep, recovery into the next evening, and shortened Friday sessions with the minutes lost. You ask for a review of the target weight and the itch and iron plans. Each decision is the nephrologist&rsquo;s.</p>
"""],
    "skills": {"title": "Cramp relief and symptom review at the chair",
               "intro": "Perform this review on a simulated patient or a colleague in a dialysis chair while your preceptor observes and plays the nurse and the patient.",
               "items": [
                   ("Checks blood pressure and pulse before addressing any symptom.", True),
                   ("Recognizes a symptom with abnormal vital signs as not minor and escalates per the unit&rsquo;s protocol.", True),
                   ("Supports the nurse&rsquo;s stretch technique and positioning for a cramp, keeping the access arm still.", False),
                   ("Reviews weight gain, target weight, and fluid removal rate as causes of cramps, and states whom to tell about a pattern.", False),
                   ("Asks for red flags with a headache or vomiting: sudden onset, worst ever, confusion, or a new neurologic sign.", True),
                   ("Asks the four restless legs questions and checks the date of the last iron studies.", False),
                   ("Scores itch on a 0-to-10 scale and inspects the skin for dryness, scratches, and infection.", False),
                   ("Asks the recovery-time question and records the answer.", False),
                   ("Completes the unit&rsquo;s symptom score and records the top symptom in the note.", False),
                   ("Reviews the analgesic and sedative list, including over-the-counter and herbal products, and flags drugs that accumulate.", True),
                   ("Offers a treatable-cause alternative to an early sign-off, documents any shortened time, and informs the nephrologist.", True),
                   ("Reports to the attending nephrologist in Situation, Background, Assessment, Recommendation (SBAR) format without changing the prescription.", True),
               ],
               "placement": "For two weeks, ask each patient on your shift the recovery-time question and the open question about what bothers them most. Score itch in every patient who mentions it. Review the list with your preceptor and choose two patients whose symptoms you will report to the attending nephrologist."},
    "quiz": [
        ("In the systematic review by Murtagh and colleagues, which symptom had the highest weighted prevalence among dialysis patients?",
         ["Restless legs", "Fatigue", "Depression", "Pain"], 1,
         "Fatigue was reported by about 71% of patients, ahead of itch at 55% and pain at 47%."),
        ("What did DOPPS show about itch and the medical directors of dialysis units?",
         ["Most directors overestimated itch in their units",
          "High phosphate was the strongest predictor of itch",
          "Most directors underestimated how common itch was in their units",
          "Antihistamines relieved itch in most patients"], 2,
         "69% of directors underestimated prevalence, and 17% of very itchy patients had not told staff."),
        ("A man asks to stop at hour three because of calf cramps. His pressure is 82/50 mm Hg; it was 146/84 at the start. What is the best first interpretation?",
         ["A minor muscle cramp that needs only stretching",
          "Restless legs syndrome",
          "A cramp from low calcium",
          "A hypotension episode that needs the Module 13 response"], 3,
         "A cramp with a low pressure is not minor. Fluid removal has outrun refilling."),
        ("A woman has calf cramps near the end of almost every session, and she reaches her target weight each time. What should you do?",
         ["Report the pattern to the attending nephrologist so the target weight and fluid plan can be reviewed",
          "Lower her target weight to remove more fluid",
          "Start a vitamin supplement to prevent cramps",
          "Shorten every session by 30 minutes"], 0,
         "A recurring pattern near target weight suggests the target may be too low. The prescription belongs to the nephrologist."),
        ("How strong is the evidence for drugs to prevent dialysis cramps?",
         ["Strong: L-carnitine is proven by large trials",
          "Low certainty: trials are small and heterogeneous, and no drug is established",
          "Moderate: vitamin E is recommended by KDIGO",
          "None: no trials have been done"], 1,
         "Vitamins and L-carnitine show signals in small trials only."),
        ("Forty minutes into a session, a man reports a sudden, severe headache, unlike any before. He vomits once and is slow to answer. What do you do?",
         ["Give a pain tablet per protocol and recheck in 30 minutes",
          "Advise him to drink coffee",
          "Treat it as dialysis disequilibrium and continue",
          "Call for help and the attending nephrologist now, check vital signs and neurologic status, and start the emergency protocol"], 3,
         "A sudden, worst-ever headache with vomiting and slowed responses is a neurologic emergency until proven otherwise."),
        ("In the Cochrane review of itch treatments, which drug class had high-certainty evidence and the largest reduction in itch?",
         ["Gabapentinoids", "Antihistamines", "Ondansetron", "Kappa-opioid agonists"], 0,
         "Gabapentinoids reduced itch by about 4.95 cm on a 10-cm scale. Kappa-opioid agonists helped less."),
        ("In KALM-1, 51.9% of patients on difelikefalin and 30.9% on placebo had at least a 3-point fall in worst itch. About how many patients need treatment for one more responder?",
         ["About 2", "About 21", "About 5", "About 52"], 2,
         "The absolute difference is 21 percentage points. 100 divided by 21 is about 4.8, rounded up to 5."),
        ("A man started gabapentin for itch two weeks ago. Today he is drowsy with jerking limbs. What is the likely explanation?",
         ["Restless legs syndrome",
          "Gabapentin accumulation in kidney failure",
          "Dialysis disequilibrium",
          "Normal fatigue after dialysis"], 1,
         "Gabapentin is cleared by the kidneys. Drowsiness and myoclonus suggest toxicity. Call the nephrologist."),
        ("A woman says her legs feel crawly and must move when she sits still in the evening, and moving eases it. What should you check first?",
         ["Her phosphate level",
          "Her dialysis fluid temperature",
          "Her Kt/V",
          "Her iron studies"], 3,
         "These are features of restless legs syndrome. Iron deficiency is a treatable contributor."),
        ("What did the randomized trial of insomnia treatments in hemodialysis patients find?",
         ["Neither CBT-I nor trazodone beat placebo, and serious cardiovascular events were more frequent with trazodone",
          "Trazodone cured insomnia in most patients",
          "CBT-I was better than trazodone and placebo",
          "Both treatments worked but CBT-I worked faster"], 0,
         "The trial was modest, but it argues against reflex sedatives."),
        ("A patient on hemodialysis has chronic knee pain and asks for &ldquo;something stronger.&rdquo; Which response fits this module?",
         ["Start codeine in the chair",
          "Ask about the cause, the score, and all current analgesics, then report to the nephrologist",
          "Start morphine at a low dose",
          "Tell him pain is expected on dialysis"], 1,
         "Morphine and codeine metabolites accumulate in kidney failure. The nephrologist chooses any drug."),
        ("In the HOPE trial, pain interference fell 0.49 points more with coping skills training; meaningful improvement occurred in 50.9% versus 36.6%. What is the best reading?",
         ["The training had no effect",
          "Every patient improved by about half a point",
          "A modest average effect hid a useful benefit in a subset, with about 7 trained per extra responder",
          "The effect grew larger by 36 weeks"], 2,
         "Averages and responder rates tell different stories. The effect diminished by 36 weeks."),
        ("In DOPPS, what was a recovery time longer than 12 hours associated with, compared with 2 to 6 hours?",
         ["Lower mortality",
          "Better quality of life",
          "Higher hospitalization and mortality, in observational data",
          "A proven benefit from shorter sessions"], 2,
         "The adjusted hazard ratio for death was 1.47. The study was observational and cannot show cause."),
        ("A patient has signed off 50 minutes early every Friday for a month on a 240-minute, three-times-weekly prescription. What is the best action?",
         ["Ignore it, since it is only one session a week",
          "Lengthen his other sessions on your own",
          "Refuse to let him leave",
          "Find the cause, offer a fix, record the time lost, and inform the nephrologist"], 3,
         "He has lost 200 minutes over four weeks, close to one full session. The prescription belongs to the nephrologist."),
    ],
    "terms": [("Chronic kidney disease&ndash;associated pruritus", "Itch caused by kidney failure, also called uremic pruritus."),
              ("Difelikefalin", "An intravenous kappa-opioid agonist that acts mainly outside the brain, given after dialysis for itch."),
              ("Gabapentinoids", "Gabapentin and pregabalin. Nerve-calming drugs cleared by the kidneys."),
              ("Restless legs syndrome", "An urge to move the legs at rest, worse in the evening and eased by movement."),
              ("Dialysis disequilibrium", "Brain swelling from rapid removal of urea, causing headache, nausea, and sometimes confusion or seizures."),
              ("Recovery time", "The hours a patient needs after a session to feel back to normal."),
              ("Calciphylaxis", "Calcification of small skin vessels causing painful dark skin lesions."),
              ("Number needed to treat", "The number of patients who must be treated for one more to benefit, compared with the control."),
              ("Edmonton Symptom Assessment System", "A short 0-to-10 symptom rating scale, modified for hemodialysis patients."),
              ("Early sign-off", "Ending a session before the prescribed time at the patient&rsquo;s request.")],
    "readings": [("uremic-pruritus-ckd.html", "Causes and treatment of itch in kidney failure, for patients and staff."),
                 ("post-dialysis-fatigue.html", "Why patients feel drained after dialysis and what can help."),
                 ("pain-management-ckd.html", "Safer pain management in chronic kidney disease, including drugs to avoid.")],
    "calcs": ["calc-dialysis-prom.html", "calc-iron-status-tsat.html", "calc-psqi.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
