# -*- coding: utf-8 -*-
"""Physician on Duty, Module 26: The Person in the Chair: Mood, Burden, and Choices About Care.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A Filipino physician on duty sitting at eye level beside a middle-aged man in a dialysis chair in quiet afternoon light, listening without writing, while the man&rsquo;s tired wife stands behind the chair.",
    "objectives": [
        "Screen a patient in the chair for depression in two steps, two brief questions and then the Patient Health Questionnaire-9 (PHQ-9), and interpret the score in light of dialysis symptoms.",
        "Explore the reasons for a missed or shortened session with open questions before giving advice, and record the barriers.",
        "Recognize caregiver strain and money and transport barriers, and route each to its owner per your unit&rsquo;s protocol.",
        "Respond to a request to stop dialysis: check safety and decision-making capacity, separate a treatable cause from a settled choice, and escalate the same day.",
        "Prepare and support a goals-of-care conversation led by the attending nephrologist, using words that help and avoiding words that harm.",
        "Respond to a death in the unit: the first steps, support for the family, the record, and care of the team.",
    ],
    "big": """
{{plain:Think of a jeepney that runs the same route every day. The engine can be tuned perfectly, but the trip still fails if the driver is exhausted, the fare box is empty, or the family at home needs him elsewhere. Dialysis is the same. A perfect prescription helps only a person who can and wants to come back to the chair.}}
<p>The picture has a limit. A jeepney driver&rsquo;s tiredness is separate from the engine. In kidney failure the two are tangled. Uremic toxins, inflammation, anemia, and poor sleep are thought to act on the brain, so the body&rsquo;s illness may itself lower mood and drive. Low mood then makes it harder to keep the schedule, the diet, and the fluid limits, and the body suffers in turn.</p>
{{cards:Key terms for this module|Depression::Persistent low mood or loss of interest, with changes in sleep, appetite, energy, or thinking, for at least two weeks.|Patient Health Questionnaire-9 (PHQ-9)::Nine items on the past two weeks, each scored 0 to 3, total 0 to 27.|Item 9::The PHQ-9 question about thoughts of being better off dead or of self-harm. Any positive answer starts the safety pathway.|Decision-making capacity::The ability to understand, appreciate, reason about, and communicate a choice.|Withdrawal from dialysis::A decision to stop dialysis, made by the patient with the attending nephrologist and, usually, the family.|Goals of care::What matters most to the patient, and the plan that fits it.|Caregiver burden::The physical, emotional, social, and financial strain on the family member who looks after the patient.}}
<p>Most patients in the chair cope, often with great courage. Some carry depression that nobody has named. A few will say, quietly, that they want to stop. Your work is to notice, ask, keep the patient safe today, and bring in the right people: the attending nephrologist, the social worker, and the unit&rsquo;s mental health referral pathway.</p>
""",
    "case": {"title": "&ldquo;I am tired of this&rdquo;", "html": """
<p>Mang Romeo Dizon, 58, was a jeepney driver until four years ago. He now dialyzes three times a week through a left arm fistula. He arrives at 1:30 in the afternoon for his Wednesday session. He missed Monday.</p>
<p>Nurse Liza Manalo reports at the station. His pre-dialysis weight is 4.1 kilograms above his dry weight. His blood pressure is 168/94 mm Hg, pulse 92, and oxygen saturation 96% on room air. A point-of-care potassium is 6.1 mmol/L, and the rhythm strip she ran shows no changes from potassium. These are illustrative values, not targets. She called the attending nephrologist about the potassium, cannulated the fistula, and started the session on the standing order.</p>
<p>At hour one he tells her, &ldquo;I am tired of this. I want to stop dialysis. My wife has to stop selling at the market to bring me here.&rdquo; He adds that he has not slept well in weeks. Ms. Manalo asks you to come to the chair. His wife, Aling Nena, is sitting in the waiting area.</p>
""", "questions": ["Is Mang Romeo safe right now, and what single question must you ask before anything else?",
                  "What could be driving this request that might be treatable, and how will you find out?",
                  "Whom do you call, what do you say in SBAR form, and what exactly do you write in the chart?"]},
    "sections": [
        ("burden", "A week in the life", "A week in the life: what dialysis asks of a person", """
{{fig:hd_week}}
<p>Twelve hours of treatment is the visible part. Add the ride, the waiting, the tiredness after each session, the fluid and diet limits, the lost work, and the hours a spouse or child gives up. The real load is much larger than the prescription.</p>
{{fig:pod26_week}}
<h3>How mood falls: a causal chain</h3>
<p>Mood depends on the brain, the body, and the person&rsquo;s place in the world. Kidney failure presses on all three. Uremic toxins and chronic inflammation may blunt energy and interest; this is plausible but not proven in patients. Anemia and poor sleep add fatigue, and itch and cramps (Module 24) break sleep further.</p>
<p>The social chain is often heavier. A man who fed his family may now depend on his wife for the fare. Loss of role, income, and control are classic triggers of depression in chronic illness. On dialysis they arrive together.</p>
{{fig:pod26_mechanism}}
<p>Here is the trap. Depression and uremia share fatigue, poor appetite, poor sleep, and slow thinking. An underdialyzed patient can look depressed, and a depressed patient can look underdialyzed. Neither label should erase the other.</p>
<div class="table-wrap"><table>
<thead><tr><th>Symptom</th><th>Points toward depression</th><th>Points toward the body</th></tr></thead>
<tbody>
<tr><td>Fatigue</td><td>Present on good days too, with loss of interest</td><td>Worse after sessions, with anemia or missed sessions</td></tr>
<tr><td>Poor appetite</td><td>With low mood and no pleasure in food</td><td>With nausea, metallic taste, or a low delivered dose</td></tr>
<tr><td>Poor sleep</td><td>Early waking with worry or sadness</td><td>Itch, cramps, restless legs, or breathlessness lying flat</td></tr>
<tr><td>Hopelessness and guilt</td><td>Strongly suggests depression</td><td>Not explained by uremia</td></tr>
</tbody></table></div>
<h3>How common, and how serious</h3>
<p>Palmer and colleagues pooled 249 study populations with 55,982 participants. By clinical interview, depression affected 22.8% of patients on dialysis; by rating scales, 39.3%. The authors concluded that scales may overestimate depression in dialysis.[[palmer2013]] Both figures come from observational studies of varying quality.</p>
<p>Kurella and colleagues studied all patients who started dialysis in the United States from 1995 to 2000. The crude suicide rate was 24.2 per 100,000 patient-years, 1.84 times the general-population rate after standardization. Age 75 or older, male sex, alcohol or drug dependence, and a recent hospital stay for mental illness were independent predictors.[[kurella2005]] Suicide remained rare in absolute terms. These registry data are older and from one country; they cannot tell you who in your unit is at risk, which is why you ask every patient directly.</p>
{{key:Depression is common, under-named, and partly hidden behind uremic symptoms. Ask about mood the way you ask about breathlessness.}}
"""),
        ("screen", "Screening at the chair", "Screening for depression at the chair", """
<p>Screening works like two fishing nets. The first is wide and quick: the first two PHQ-9 items. Over the last two weeks, how often have you been bothered by little interest or pleasure in doing things? How often have you felt down, depressed, or hopeless? The second, finer net is the full PHQ-9 for anyone the first net catches.</p>
{{flow:The two-step screen at the chair|Set the scene::Sit at eye level. Lower your voice. Ask the nurse to draw the curtain if your unit has one. Use Filipino or English, as the patient prefers.|Ask the two questions::Low mood and loss of interest over the past two weeks. If both answers are &ldquo;not at all,&rdquo; record a negative screen and the date.|Complete the PHQ-9::If either answer is positive, complete all nine items with the patient, or review the form the patient filled in.|Ask item 9 in person::Ask about thoughts of being better off dead or of hurting oneself, in plain words, whatever the total score.|Branch on item 9::Any positive answer starts the safety pathway now. A negative answer with a high total goes to the attending nephrologist with a referral request.|Record::Score, date, item 9 answer, the patient&rsquo;s own words, and who was told.}}
<h3>How well the PHQ-9 works in dialysis</h3>
<p>The PHQ-9 was first validated in 6,000 primary care and obstetric patients: a score of 10 or more had sensitivity and specificity of 88% for major depression, and scores of 5, 10, 15, and 20 marked mild, moderate, moderately severe, and severe depression.[[kroenke2001]]</p>
<p>Watnick and colleagues tested it in 62 patients on dialysis against a structured psychiatric interview. At 10 or more, sensitivity was 92%, specificity 92%, positive predictive value 71%, and negative predictive value 98%.[[watnick2005]] The study was small and single-center. A negative screen is reassuring. A positive screen means &ldquo;look closer&rdquo;: about three in ten positives did not have depression on interview.</p>
<div class="table-wrap"><table>
<thead><tr><th>PHQ-9 total</th><th>Severity band</th><th>Dialysis caveat</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>0 to 4</td><td>Minimal</td><td>None</td><td>Record. Rescreen at the interval your unit sets</td></tr>
<tr><td>5 to 9</td><td>Mild</td><td>Sleep, energy, and appetite items may come from uremia</td><td>Record. Tell the attending nephrologist at the next review</td></tr>
<tr><td>10 to 14</td><td>Moderate</td><td>Look at items 1, 2, 6, and 9, which uremia does not explain</td><td>Report to the attending nephrologist and request a referral per protocol</td></tr>
<tr><td>15 to 27</td><td>Moderately severe to severe</td><td>Do not explain the score away</td><td>Report the same day</td></tr>
<tr><td>Item 9 above 0, any total</td><td>Safety concern</td><td>None. Uremia never explains this item</td><td>Start the safety pathway now</td></tr>
</tbody></table></div>
<p>The bands come from primary care.[[kroenke2001]] The dialysis caveat is reasoning from shared symptoms, not a tested correction. The <a href="calc-phq9.html">PHQ-9 calculator</a> adds the items, and the <a href="calc-dialysis-prom.html">patient-reported outcome tool</a> tracks scores over time.</p>
{{formula:<strong>Worked example, illustrative.</strong> PHQ-9 total = sum of nine items, each scored 0 to 3.[[kroenke2001]]<br>Item scores: interest 2, low mood 2, sleep 3, energy 3, appetite 2, feeling a failure 2, concentration 1, slowness 1, item 9 0.<br>Total = 2 + 2 + 3 + 3 + 2 + 2 + 1 + 1 + 0 = 16.<br>This is above the dialysis-validated cutoff of 10.[[watnick2005]] Sleep, energy, and appetite (7 of the 16 points) overlap uremic symptoms. Interest, low mood, and feeling a failure (6 points) do not.<br>What the number tells you: depression is likely enough to report and refer. What it does not tell you: the diagnosis, the cause, or the treatment. Item 9 is 0, so no safety pathway, but the score goes to the attending nephrologist today with a referral request.}}
<p>The Medical Director sets the screening interval, the form, and who scores it. No trial has tested whether routine screening in dialysis improves outcomes, but it is the only way to find depression that patients do not mention.</p>
{{call:Stop and call when a patient answers item 9 above zero, states a plan to harm himself, or wants to leave mid-session to harm himself. Stay with the patient or keep a staff member beside him, and speak calmly and without judgment. Keep the access and lines in view. Follow your unit&rsquo;s safety protocol: call the attending nephrologist and the patient&rsquo;s emergency contact, and activate the unit&rsquo;s mental health referral pathway or the crisis line your Medical Director lists. Do not send the patient home alone.}}
"""),
        ("treat", "What helps", "What helps: the evidence on treating depression in dialysis", """
<p>Picture two doors: talking therapy and medicine. Both are open. Neither is a sure cure, and the evidence behind each is thinner than in people without kidney failure.</p>
<p>Two features of dialysis explain why. Some antidepressants or their breakdown products accumulate when the kidneys fail, and most are poorly removed by dialysis, so levels and side effects can differ (Module 20). And because of the somatic overlap above, a trial that measures symptom scores partly measures uremia.</p>
{{cards:What each study tested and found|Antidepressant versus placebo, Cochrane review::Four small randomized trials, 170 participants, 8 to 12 weeks. No quality-of-life benefit shown; more nausea with the drug (risk ratio 2.67). One trial of 43 patients found lower depression scores. Certainty very low or ungradeable.[[palmer_cochrane2016]]|Sertraline versus placebo, feasibility trial::30 randomized, 6 months. Eight of 15 on sertraline and 13 of 15 on placebo completed. Both groups improved, with no difference. Too small to conclude.[[friedli2017]]|Sertraline versus chairside talking therapy, ASCEND::120 patients, 41 United States units, 12 weeks, open label. Clinician-rated scores 1.84 points lower with sertraline, with more adverse events. No placebo arm.[[mehrotra2019]]|Chairside talking therapy versus wait-list::Randomized crossover, 65 enrolled. Among those depressed at baseline, 89% were no longer depressed after therapy, against 38% on the wait-list. Quality of life and weight gain between sessions improved.[[cukor2014]]|Stepped collaborative care by telehealth, T&#256;Ccare::160 patients; talking therapy, medicine, or both. Fatigue and pain improved modestly, lasting to 6 months; the depression score fell slightly.[[jhamb2023]]}}
<h3>Reading these results</h3>
<p>Cognitive behavioral therapy (CBT) is a structured talking therapy that helps a person notice and change unhelpful thoughts and habits. The evidence suggests benefit at the chair, but the main trial enrolled 65 patients at two centers.[[cukor2014]] Whether antidepressants beat placebo in dialysis is uncertain; the placebo-controlled trials are few and tiny.[[palmer_cochrane2016]][[friedli2017]] ASCEND shows sertraline did modestly better than chairside CBT, and cannot say whether either beats no treatment.[[mehrotra2019]]</p>
<p>All of these outcomes are rating-scale scores, surrogates for how a person feels and functions. None of these trials was designed to show an effect on survival, hospital stays, or suicide. In ASCEND, a structured engagement interview did not raise treatment uptake (66% against 64%).[[mehrotra2019]] Patients decide for their own reasons. Your role is to make the offer, record the answer, and keep the door open.</p>
<div class="table-wrap"><table>
<thead><tr><th>Task</th><th>Who owns it</th></tr></thead>
<tbody>
<tr><td>Screening, scoring, and recording</td><td>The physician on duty or the staff member your protocol names</td></tr>
<tr><td>Asking the patient&rsquo;s preference: talking, medicine, both, or neither for now</td><td>The physician on duty, recorded in the patient&rsquo;s words</td></tr>
<tr><td>Referral to psychiatry, psychology, or counseling</td><td>Per your unit&rsquo;s referral pathway, with the attending nephrologist</td></tr>
<tr><td>Choosing and dosing any antidepressant</td><td>The attending nephrologist, with the psychiatrist where available</td></tr>
</tbody></table></div>
<p>Do not start an antidepressant on the floor, and do not stop one the patient already takes. Sudden stopping of some antidepressants causes withdrawal symptoms. Report the screen, the preference, and any side effects the patient describes.</p>
{{key:Treatment helps some patients, but the evidence is thin. Your job is to find, record, and refer, not to prescribe.}}
"""),
        ("missed", "Missed sessions", "Missed and shortened sessions: ask before you lecture", """
<p>An empty chair is a symptom, not a character flaw. Module 11 decides whether it is safe to dialyze after a missed session. This section asks why it was missed.</p>
<p>The physiology is unforgiving. Every missed session stretches the gap between treatments (Module 2), and potassium, fluid, and acid keep building. The risk is highest in the days right after a missed treatment.</p>
<h3>What the cohorts show</h3>
<p>In the Dialysis Outcomes and Practice Patterns Study (DOPPS), skipping one or more sessions a month was associated with higher mortality (relative risk 1.30) and hospital admission (relative risk 1.13). Shortening meant ending a session more than 10 minutes early. A higher share of highly trained staff hours was associated with lower odds of skipping (odds ratio 0.84 per 10%).[[saran2003]]</p>
<p>A later DOPPS analysis of 8,501 patients in 20 countries found a four-month missed-treatment risk from under 1% in Italy and Japan to 24% in the United States. Younger age, less time on dialysis, longer travel, and more depressive symptoms predicted missing. Missed treatments were associated with higher all-cause mortality (hazard ratio 1.68).[[alsalmi2018]]</p>
<p>In 182,536 United States patients, the average missed rate was 7.1 sessions per patient-year. In the two days after a miss, the odds of hospital admission were about four times higher (odds ratio 3.98). Transport, weather, holidays, psychiatric illness, pain, and stomach upset were linked to missed days.[[chan2014]]</p>
<p>All three are observational. Patients who skip differ in many ways, so part of the association with death may reflect those differences. Most data come from high-income countries; no Philippine data were found. The wide variation between countries suggests that missed sessions can be changed.</p>
{{fig:pod26_emptychair}}
{{flow:Missed sessions: ask before you lecture|Open question::&ldquo;I noticed you were not here on Monday. What happened?&rdquo; Then wait. Silence gives the patient room.|Sort the barrier::Transport or fare money. Symptoms during the session such as cramps or a falling pressure. Low mood. Family duties. Work. Doubt about whether dialysis is needed.|Match an owner::Social worker for money and transport. Head nurse for schedule and chair time. Attending nephrologist for symptoms, fluid goals, and mood.|Record::The barrier in the patient&rsquo;s words, the owner, and the date of follow-up.|Follow up::Ask at the next session whether anything changed.}}
{{formula:<strong>Delivered-time check, illustrative.</strong> Percent delivered = delivered minutes &divide; prescribed minutes &times; 100.<br>Prescribed: 240 minutes &times; 13 sessions = 3,120 minutes.<br>Delivered: 2 sessions missed (0 minutes), 4 sessions ended at 200 minutes, 7 sessions ran 240 minutes.<br>Delivered = (7 &times; 240) + (4 &times; 200) = 1,680 + 800 = 2,480 minutes.<br>Percent delivered = 2,480 &divide; 3,120 &times; 100 = 79.5%.<br>Shortened sessions by the DOPPS definition, more than 10 minutes short: 4.[[saran2003]]<br>What the number tells you: about one fifth of the prescribed time was not delivered this month. What it does not tell you: why. Record the reason for each missed or shortened session, including sessions ended early for medical reasons.}}
<p>Write the numbers, not a label. &ldquo;Missed 2 of 13 sessions; 4 ended 40 minutes early because of cramps&rdquo; helps the next reader. &ldquo;Noncompliant&rdquo; helps nobody and follows the patient for years. The <a href="calc-hd-session-review.html">session review tool</a> shows delivered time and events when a patient signs off early.</p>
<h3>A barrier sort in practice</h3>
<p>A man has missed two Mondays. Your open question finds two reasons: no fare money after the weekend, and painful cramps in his last hour. The fare goes to the social worker. The cramps and the fluid goal go to the attending nephrologist, because they belong to the prescription (Module 24). The Monday schedule goes to the head nurse. You record each owner and the follow-up date.</p>
{{key:Ask why before you warn. A barrier you name can be fixed; a lecture changes nothing.}}
"""),
        ("caregiver", "Caregivers and money", "The person beside the chair: caregivers and money", """
<p>The caregiver is often the second patient in the room. In many Filipino families one person, usually a spouse or daughter, brings the patient three times a week, cooks the low-salt food, buys the medicines, and finds the fare, often after giving up work.</p>
{{fig:pod26_caregiver}}
<p>Each session takes most of a day for two people. Lost income meets new costs: transport, medicines, and laboratory tests. Money worry and fatigue wear down the caregiver&rsquo;s health and patience. A worn-out caregiver may stop bringing the patient, and the patient may come to feel like a burden. When a patient says he is a burden, take it as a reason to screen, including item 9.</p>
<p>Walavalkar and colleagues reviewed six studies of caregivers of patients on conservative kidney care, without dialysis. These caregivers carried significant burden, with effects on quality of life similar to those of dialysis caregivers, and fear of the patient dying ran through their accounts.[[walavalkar2022]] The review was small and could not pool its data.</p>
<p>Can the burden be eased? Gillespie and colleagues found 13 intervention studies, mostly education and skills training. Twelve reported less burden, and a meta-analysis of five education programs showed a reduction, with high heterogeneity and low certainty.[[gillespie2026]] Teaching caregivers suggests benefit; which program works best is unknown.</p>
{{cards:One question, three owners|Ask the caregiver::&ldquo;How are you managing with all of this?&rdquo; Ask it away from the patient if the caregiver seems to hold back.|Money and transport::The social worker, or the staff member your unit names, for financial counseling and available assistance.|Schedule::The head nurse, for a shift or chair time that fits work or market hours.|Exhaustion, low mood, or conflict::The attending nephrologist and the unit&rsquo;s referral pathway. A caregiver can be screened and referred too.}}
<p>Do not quote coverage rules or amounts from memory; they change, and a wrong promise damages trust. The guide on <a href="ckd-financial-stress.html">financial stress in kidney disease</a> is a starting point, and the social worker holds the current details.</p>
{{key:Notice the caregiver, ask one question, and route the answer. A supported caregiver keeps the patient in the chair.}}
"""),
        ("stop", "&ldquo;I want to stop&rdquo;", "&ldquo;I want to stop dialysis&rdquo;", """
<p>A request to stop dialysis is the start of a conversation, not the end of one. It may be a settled choice after years of thought, or the voice of untreated depression, uncontrolled itch, or an empty fare purse. On the day you hear it, you cannot know which, and you do not need to. You need to keep the patient safe, listen well, and bring in the attending nephrologist the same day.</p>
<h3>Why this is a valid choice, and why it needs care</h3>
<p>The Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference on supportive care placed symptom control, advance care planning, conservative care, and end-of-life care inside good kidney care, including for people on dialysis.[[davison2015]] This is a conference statement, not a graded recommendation.</p>
<p>Stopping dialysis leads to death, usually soon. In 1,947 patients admitted to 10 United States hospices after stopping dialysis, mean survival was 7.4 days (range 0 to 40). Male sex, hospital referral, lower function, and edema were associated with shorter survival.[[oconnor2013]] These figures describe a hospice group in one country, not the future of the patient in front of you.</p>
<h3>Four questions, in order</h3>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>What you check</th><th>What you do with the answer</th></tr></thead>
<tbody>
<tr><td>Is the patient safe right now?</td><td>Item 9 of the PHQ-9. Any plan or wish to harm himself. Wanting to leave the unit to do so</td><td>Any yes starts the safety pathway. The request to stop is recorded and is not acted on today</td></tr>
<tr><td>Can the patient decide?</td><td>Understands the facts. Appreciates that they apply to him. Reasons about the options. States a steady choice</td><td>Record what you found. A formal capacity assessment belongs to the attending nephrologist or psychiatrist</td></tr>
<tr><td>Is there a treatable driver?</td><td>Depression. Uncontrolled itch, pain, cramps, or poor sleep (Module 24). Money, transport, or family conflict. Confusion from illness</td><td>Name each driver and its owner. A fixed barrier can change the decision</td></tr>
<tr><td>Who decides?</td><td>The patient, with the attending nephrologist and, if the patient wishes, the family</td><td>Not you, today, at the chair</td></tr>
</tbody></table></div>
<p>Capacity is specific to one decision at one time. A patient with mild memory problems may still decide about dialysis; one who is newly confused, intoxicated, or very ill may not, even if he spoke clearly last week (Module 25).</p>
{{fig:pod26_stopflow}}
<h3>Today&rsquo;s session</h3>
<p>Ask whether the patient will finish today&rsquo;s session while the conversation continues. Many will, once they feel heard. A patient with capacity who declines cannot be dialyzed against his will. Explain the risks in plain words, ask the nurse to end the session per protocol, and call the attending nephrologist before he leaves (Module 11 covers the gap). If he seems confused or unwell, call at once and do not let him leave alone.</p>
<p>Write the patient&rsquo;s exact words in quotation marks: &ldquo;I am tired of this; I want to stop&rdquo; says more than &ldquo;patient requests withdrawal.&rdquo; Withdrawal orders, do-not-resuscitate orders, and consent forms are covered in Module 31.</p>
{{call:Stop and call the attending nephrologist the same day for any request to stop dialysis, for any refusal of today&rsquo;s session by a patient who seems confused, intoxicated, or medically unstable, and for any family request to stop that the patient has not voiced himself. If the patient also has thoughts of self-harm, start the safety pathway first and call while a staff member stays with him.}}
<h3>When the request comes from the family</h3>
<p>Sometimes a relative says, &ldquo;Doc, let us stop. He is suffering.&rdquo; Thank the relative and listen. Then ask to hear from the patient, alone if possible. The patient&rsquo;s voice leads while he can decide. Record both voices and call the attending nephrologist.</p>
{{flow:Call card: a patient at risk of self-harm during dialysis|Recognize::Item 9 above zero, talk of being better off dead, a stated plan, sudden calm after deep distress, or a patient trying to leave mid-session to harm himself.|First 2 minutes::Stay with the patient or assign a staff member to stay. Speak calmly and listen. Keep the access and lines in view. Call for help in the unit per protocol.|Stop dialysis?::Continue if the patient is calm and consents. End the session per protocol if the patient insists on stopping or cannot be kept safe in the chair.|Return the blood?::Yes, through the usual return, when the session ends and the circuit is closed and intact. Do NOT return blood from a circuit that has been opened, disconnected, or contaminated, or that has clotted. If a needle is pulled or a line is opened, stop the blood pump, clamp, and press on the site.|Call::The attending nephrologist, the patient&rsquo;s emergency contact, and the unit&rsquo;s mental health referral pathway, emergency room, or crisis line, as your protocol lists. Use the SBAR format from Module 1.|Write::Time, the patient&rsquo;s words in quotation marks, the item 9 answer, who stayed with the patient, whom you called and when, the advice received, and where and with whom the patient went.}}
"""),
        ("goals", "Goals and a death", "Goals-of-care conversations and a death in the unit", """
<p>Think of a map with three roads. The attending nephrologist walks them with the patient and family. You often stand at the crossroads first, because the patient speaks to whoever is at the chair.</p>
{{cards:Three roads|Continue as is::The patient values the time dialysis gives and accepts its load. Goals are reviewed at intervals.|Change the plan::Symptom relief, fewer restrictions, or a different schedule, decided by the attending nephrologist (Module 27).|Stop with comfort care::The patient, with the attending nephrologist and family, chooses to stop; symptom care and family support follow.}}
<h3>What the evidence says about planning ahead</h3>
<p>Advance care planning is a series of conversations about what matters to the patient and who will speak for him if he cannot. The SPIRIT trial randomized 42 United States dialysis clinics, with 426 patient and surrogate pairs; trained nurses and social workers led structured planning talks. At two weeks, pairs agreed more often on end-of-life goals (odds ratio 1.61), and patients had less decisional conflict. Surrogate confidence did not differ. Among 77 bereaved surrogates, anxiety was lower, but depression and posttraumatic distress were similar.[[song2024]]</p>
<p>The trial supports planning talks led by trained unit staff. Its main outcomes were preparation scores at two weeks, not survival or place of death. Filipino families often decide together, so applying it here needs local judgment.</p>
{{cards:Words that help and words that harm|&ldquo;What matters most to you now?&rdquo;::Opens the conversation and puts the patient&rsquo;s values first.|&ldquo;Tell me more about being tired of this.&rdquo;::Invites the reason behind the request.|&ldquo;Whatever you decide, we will keep caring for you.&rdquo;::Removes the fear of abandonment.|&ldquo;I will ask Dr. ... to sit down with you and your family.&rdquo;::Names the next step and the person.|Avoid &ldquo;There is nothing more we can do&rdquo;::There is always care to give, even when dialysis stops.|Avoid &ldquo;You will die if you stop, so you cannot stop&rdquo;::True in part, but it ends the conversation and overrides the patient.|Avoid &ldquo;Noncompliant&rdquo; and &ldquo;refuser&rdquo;::Labels that close minds and follow the patient in the chart.}}
<p>The guides on <a href="advance-care-planning-dialysis.html">advance care planning on dialysis</a> and <a href="ckd-mental-health-sleep.html">mental health and sleep</a> are written for families. The <a href="calc-frailty-assessment.html">frailty assessment</a> gives context before a goals-of-care talk (Module 25).</p>
{{key:You open the door to goals-of-care talk and document what was said; the attending nephrologist leads the decision.}}
<h3>A death in the unit</h3>
<p>Some deaths in the unit are expected; others follow an arrest the team could not reverse. The resuscitation itself belongs to the unit&rsquo;s protocol and other modules. This part covers what follows.</p>
{{flow:After a death in the unit: the first 30 minutes|Confirm and record::Pronounce death per your unit&rsquo;s protocol and hospital rules. Record the time.|Protect privacy::Draw the curtain or screen the chair. Move nearby patients if possible, or explain quietly what has happened, without names.|Call::The attending nephrologist and the Medical Director, per protocol. The head nurse arranges care of the body.|Inform the family::In a private place, sitting down, in plain words. Say &ldquo;died,&rdquo; not &ldquo;passed&rdquo; or &ldquo;lost.&rdquo; Then stay and listen.|Write the death note::Time, events, the response, who was present, who was told, and when.|Care for the team::A short huddle before the next patient: what happened, how people are, and what needs follow-up.}}
<p>Other patients have watched someone like them die. A brief, honest word at the chair helps more than silence. Staff grieve too, and a short debrief is part of safe practice.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Is Mang Romeo safe right now, and what must you ask first?</strong> You go to the chair, sit at eye level, and ask Ms. Manalo to draw the curtain. His pressure and potassium are already with the attending nephrologist, and his monitor shows a steady rhythm. The question that comes before everything else is about self-harm. You ask it plainly: &ldquo;Sometimes when people feel this tired, they think they would be better off dead, or think of hurting themselves. Has that happened to you?&rdquo; He says no, and that he wants to stop because he is a burden, not because he wants to die. You thank him and say he can tell any of the staff if such thoughts come. He understands where he is, what dialysis does, and what stopping means, and he agrees to finish today&rsquo;s session.</p>
<p><strong>What could be treatable?</strong> He describes weeks of waking early with worry. With his consent you complete the PHQ-9: 16, item 9 at 0, the pattern of the worked example. Interest, low mood, and feeling a failure, which uremia does not explain, give 6 points. He may have depression. His wife&rsquo;s lost market income and the fare are a practical barrier and likely explain the missed Monday. His poor sleep may also have a physical cause, such as itch or breathlessness lying flat. You ask Aling Nena, separately, how she is managing. She cries and says she is exhausted.</p>
<p><strong>Whom do you call, what do you say, and what do you write?</strong> You call the attending nephrologist during the session. Situation: &ldquo;Mang Romeo Dizon, 58, said at hour one that he wants to stop dialysis.&rdquo; Background: &ldquo;He missed Monday; you know about today&rsquo;s potassium of 6.1. Weeks of poor sleep. His wife stopped work to bring him.&rdquo; Assessment: &ldquo;No thoughts of self-harm. PHQ-9 16, item 9 zero. He understands his situation and agreed to finish today. Possible depression, a money and transport barrier, and caregiver strain.&rdquo; Recommendation: &ldquo;I suggest a review with you and the family this week, a mental health referral through our pathway, and a social worker referral today.&rdquo; You repeat back the advice. In the chart you write the time, his words in quotation marks, the item 9 answer, the PHQ-9 score, his consent to continue, the barriers and owners, the call and advice, and the follow-up date. You do not write &ldquo;noncompliant.&rdquo;</p>
"""],
    "skills": {"title": "Mood screen and response to a request to stop dialysis",
               "intro": "Perform this at a practice station with a standardized patient in a dialysis chair while your preceptor observes. The patient will raise low mood and a wish to stop dialysis.",
               "items": [
                   ("Introduces self, sits at eye level, and arranges privacy at the chair.", False),
                   ("Asks the two screening questions in Filipino or English, as the patient prefers.", False),
                   ("Administers or reviews the PHQ-9 and computes the total correctly.", False),
                   ("Asks item 9 directly and starts the safety pathway for any positive answer.", True),
                   ("Identifies which positive items may reflect uremic symptoms, without dismissing them.", False),
                   ("Asks open questions about missed or shortened sessions before giving advice.", False),
                   ("Names at least one barrier and its owner: social worker, head nurse, or attending nephrologist.", False),
                   ("On a request to stop dialysis, checks immediate safety and does not leave a patient with self-harm risk alone.", True),
                   ("Assesses decision-making capacity in outline: understands, appreciates, reasons, and states a choice.", False),
                   ("Calls the attending nephrologist the same day with an SBAR report and records the patient&rsquo;s words verbatim.", True),
                   ("Uses at least two phrases that help and avoids &ldquo;there is nothing more we can do.&rdquo;", False),
                   ("Documents the score, the date, the actions, the calls, and the follow-up plan.", False),
               ],
               "placement": "Over two weeks, with your preceptor, review the mood screens recorded in your unit. Pick one patient with a positive screen and one patient who has missed two or more sessions. For each, check that a barrier, an owner, and a follow-up date are recorded, and report any gap to the attending nephrologist."},
    "quiz": [
        ("Why can a depression symptom score overestimate depression in a patient on dialysis?",
         ["Patients on dialysis tend to exaggerate their answers",
          "Fatigue, poor sleep, and poor appetite can come from uremia as well as from depression",
          "The PHQ-9 was never tested in dialysis",
          "Dialysis removes the chemicals that cause low mood"], 1,
         "Scales count somatic items that kidney failure can cause; interview-based prevalence was lower in the Palmer meta-analysis."),
        ("A man on dialysis scores 4 on the PHQ-9, but answers 1 on item 9. What do you do?",
         ["Record a minimal score and rescreen at the usual interval",
          "Tell him the score is normal for dialysis",
          "Start the safety pathway now, whatever the total",
          "Repeat the questionnaire next week"], 2,
         "Any positive answer to item 9 starts the safety pathway. The total does not override it."),
        ("In the Watnick validation study in dialysis, what did a PHQ-9 score of 10 or more show?",
         ["Sensitivity and specificity of about 92%, in a small single-center sample",
          "Perfect accuracy in a large multicenter trial",
          "Poor accuracy, so the test should not be used",
          "A reduction in deaths from screening"], 0,
         "The study had 62 patients. It shows good accuracy against interview, not that screening improves outcomes."),
        ("A woman&rsquo;s PHQ-9 total is 12. Her highest items are sleep, energy, and appetite; interest, mood, and item 9 are 0. What is the best interpretation?",
         ["She has severe depression and needs medicine today",
          "Depression is excluded",
          "The score is invalid and should be discarded",
          "Uremic symptoms may be driving the score; report it and look for physical causes as well"], 3,
         "The somatic items overlap uremia. Report it, look for causes such as itch, anemia, or underdialysis, and let the attending nephrologist decide on referral."),
        ("What does the Cochrane review of antidepressants versus placebo in dialysis show?",
         ["Clear benefit on quality of life",
          "Very low certainty evidence, no quality-of-life benefit shown, and more nausea",
          "Antidepressants reduce suicide",
          "Antidepressants are harmful and should be avoided"], 1,
         "Four small trials with 170 participants could not show benefit with confidence. Nausea was more common."),
        ("The ASCEND trial found modestly lower depression scores with sertraline than with chairside CBT. What can you conclude?",
         ["Sertraline beats placebo in dialysis",
          "CBT is useless in dialysis",
          "Sertraline did better than CBT on a rating scale, but neither was compared with no treatment",
          "All patients on dialysis should take sertraline"], 2,
         "ASCEND compared two active treatments. It had no placebo or no-treatment arm, and its outcome was a surrogate score."),
        ("A patient with a positive screen asks you to start him on an antidepressant today. What is the best response?",
         ["Report the screen and his preference to the attending nephrologist, who chooses and doses any medicine",
          "Start a low dose of any antidepressant",
          "Tell him medicines do not work in dialysis",
          "Tell him to buy one at the pharmacy"], 0,
         "Drug choice and dosing in kidney failure belong to the attending nephrologist. Your job is to record and refer."),
        ("A man has missed three Mondays. The head nurse wants you to warn him that he will die. What is the better first step?",
         ["Write &ldquo;noncompliant&rdquo; in the chart",
          "Ask an open question about what happened and sort the barrier",
          "Tell him he will lose his chair",
          "Lower his fluid goal"], 1,
         "A named barrier can be fixed. A warning without understanding rarely changes behavior."),
        ("In the DOPPS data, which factor was associated with fewer skipped sessions?",
         ["Larger units",
          "A higher share of highly trained staff hours",
          "Shorter sessions",
          "Younger patients"], 1,
         "Each 10% more highly trained staff hours was associated with lower odds of skipping. Larger facility size showed only a borderline association with more skipping."),
        ("A patient was prescribed 13 sessions of 240 minutes. He missed 1 and the other 12 ran full time. What percent was delivered?",
         ["100%", "88.0%", "92.3%", "95.0%"], 2,
         "Delivered 12 &times; 240 = 2,880 minutes. Prescribed 3,120. 2,880 &divide; 3,120 = 92.3%."),
        ("A daughter who brings her mother to every session looks exhausted and has stopped working. What do you do?",
         ["Ask how she is managing, and route money, schedule, and her own strain to their owners",
          "Tell her to find another relative",
          "Nothing, because she is not the patient",
          "Promise her financial help from the government"], 0,
         "Caregiver strain threatens the patient&rsquo;s care. Route each part to its owner and never promise coverage from memory."),
        ("A calm, oriented woman says she wants to stop dialysis. She has no thoughts of self-harm. What is your role today?",
         ["Arrange the withdrawal orders",
          "Tell her she cannot stop",
          "Ask her to sign a consent form",
          "Listen, check capacity in outline, look for treatable drivers, and call the attending nephrologist the same day"], 3,
         "The decision belongs to the patient with the attending nephrologist and family. Documents are covered in Module 31."),
        ("A man asks to stop dialysis and also says his family would be better off if he were dead. What comes first?",
         ["Discuss hospice options",
          "Start the safety pathway: stay with him, call the attending nephrologist and his emergency contact",
          "Let him go home to think it over",
          "Record the request and wait for the next session"], 1,
         "Self-harm risk comes before the withdrawal question. He is not left alone or sent home alone."),
        ("A son asks you to stop his father&rsquo;s dialysis. The father, who is alert, has said nothing about stopping. What do you do?",
         ["Stop the session as the family wishes",
          "Ignore the son",
          "Listen to the son, then ask to hear from the father, record both, and call the attending nephrologist",
          "Tell the son he has no say"], 2,
         "While the patient can decide, his voice leads. A family request he has not voiced is a stop-and-call trigger."),
        ("What did the SPIRIT trial of advance care planning in dialysis clinics show?",
         ["It improved survival",
          "It reduced dialysis withdrawal",
          "It had no effect on any outcome",
          "Better agreement between patients and surrogates on end-of-life goals, and less decisional conflict"], 3,
         "Its outcomes were preparation measures at two weeks. Surrogate confidence did not differ, and bereavement results were mixed."),
    ],
    "terms": [("Depression", "A persistent low mood or loss of interest with changes in sleep, appetite, energy, or thinking that lasts at least two weeks."),
              ("PHQ-9", "The Patient Health Questionnaire-9, a nine-item depression symptom score from 0 to 27."),
              ("Item 9", "The PHQ-9 question about thoughts of being better off dead or of self-harm. Any positive answer starts the safety pathway."),
              ("Cognitive behavioral therapy (CBT)", "A structured talking therapy that helps a person notice and change unhelpful thoughts and habits."),
              ("Decision-making capacity", "The ability to understand, appreciate, reason about, and communicate a choice about a specific decision."),
              ("Withdrawal from dialysis", "A decision to stop dialysis, made by the patient with the attending nephrologist and, usually, the family."),
              ("Advance care planning", "A series of conversations about what matters to a patient and who will decide if the patient cannot."),
              ("Surrogate", "The person the patient chooses to speak for him if he cannot speak for himself."),
              ("Caregiver burden", "The physical, emotional, social, and financial strain on a family member who looks after the patient."),
              ("Supportive care", "Care that focuses on symptoms, quality of life, and planning, given alongside or instead of dialysis.")],
    "readings": [("ckd-mental-health-sleep.html", "Mood, anxiety, and sleep in kidney disease, written for patients and families."),
                 ("advance-care-planning-dialysis.html", "How patients and families can plan ahead and choose who speaks for them."),
                 ("caregiver-guide-ckd.html", "Practical support for the family member who carries the daily load.")],
    "calcs": ["calc-phq9.html", "calc-dialysis-prom.html", "calc-hd-session-review.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
