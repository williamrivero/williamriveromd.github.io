# -*- coding: utf-8 -*-
# Module 14 expansion, part 2: behavior in the unit and living well over the long term.
# Sections follow the mental-health half (m14_x.py), starting after "crisis".
OBJECTIVES = [
    "Identify the medical causes of agitation and disruptive behavior in the hemodialysis (HD) unit before attributing behavior to personality, and de-escalate a tense situation step by step within unit policy.",
    "Describe how documentation, team review, behavior agreements, and debriefing protect patients and staff, and state the ethical limits on refusing or discharging a patient from a dialysis unit.",
    "Explain why muscle and physical function decline on HD, summarize the evidence for intradialytic and home exercise, and apply a safety screen before exercise during treatment.",
    "Recognize frailty, post-dialysis orthostatic hypotension, and fall risk, and teach fall prevention and home safety, referring for therapy when needed.",
    "Address skipped and shortened sessions, high interdialytic weight gain, and symptom burden through nonjudgmental problem-solving, routine symptom review, and goals that matter to the patient.",
]
EXTRA = [
    {"after": "crisis", "id": "behavior", "nav": "Disruptive behavior", "tag": "Behavior in the unit",
     "h2": "What drives disruptive behavior in the dialysis unit",
     "html": """
<p>A hemodialysis (HD) unit concentrates the conditions that make people lose their temper: a serious chronic illness, needles, long waits, a fixed schedule that controls the patient&rsquo;s week, money worries, and a room shared with strangers for twelve hours or more every week. Most patients cope remarkably well. When one does not, and shouts, threatens, pulls at lines, refuses to leave, or abuses staff or other patients, the nurse needs a way of thinking that keeps everyone safe and finds the cause. Module 12 set out the ethical principles; this section and the next two turn them into practice.</p>
<p><strong>Medical causes come first.</strong> The brain is an organ that fails like any other, and in a person with chronic kidney disease (CKD) on dialysis it is exposed to shifts in glucose, oxygen, sodium, urea, and blood pressure within a single session. Behavior that looks like anger or bad manners is often the first sign of one of these:</p>
<div class="table-wrap"><table>
<thead><tr><th>Medical cause</th><th>Why it changes behavior</th><th>What the nurse checks</th></tr></thead>
<tbody>
<tr><td>Low blood sugar</td><td>The brain depends on glucose; a falling level causes irritability, confusion, and sweating, especially in a patient with diabetes who took insulin or a sulfonylurea and did not eat</td><td>Capillary glucose at once; treat per protocol</td></tr>
<tr><td>Low oxygen or low blood pressure</td><td>Reduced brain perfusion or oxygen causes restlessness and confusion before collapse</td><td>Blood pressure, pulse, oxygen saturation, breathing; stop or reduce fluid removal as Module 9 describes</td></tr>
<tr><td>Delirium</td><td>An acute, fluctuating disturbance of attention, often from infection, new medicines, or recent hospitalization; older patients and those with cognitive impairment are most at risk</td><td>Sudden change from the patient&rsquo;s usual self, inattention, fluctuating alertness; temperature; new medicines</td></tr>
<tr><td>Dialysis disequilibrium</td><td>Rapid urea removal in a new or under-dialyzed patient shifts water into brain cells</td><td>Headache, nausea, restlessness in an early or long-missed patient (Module 9)</td></tr>
<tr><td>Uremia</td><td>Accumulated toxins after missed sessions dull and irritate the brain</td><td>Recent missed or shortened sessions; drowsiness, twitching, poor concentration</td></tr>
<tr><td>Pain</td><td>Unrelieved pain from cannulation, ulcers, cramps, or bone disease lowers anyone&rsquo;s tolerance</td><td>Ask directly and look; cramps and access pain are common and treatable</td></tr>
<tr><td>Alcohol, drugs, or withdrawal</td><td>Intoxication disinhibits; withdrawal causes tremor, agitation, and sometimes seizures</td><td>Smell of alcohol, slurred speech, history from the companion; report to the physician</td></tr>
<tr><td>Medicine effects</td><td>Some sedatives, pain medicines, and other drugs accumulate when the kidneys fail and cause confusion</td><td>Recent new or changed medicines; report for physician review</td></tr>
</tbody></table></div>
<p>The rule is simple: <strong>check the body before judging the person.</strong> A capillary glucose, a blood pressure, and an oxygen saturation take less than two minutes and can prevent a seizure, a fall, or a cardiac arrest. Treating hypoglycemic confusion as rudeness is not only unkind; it is dangerous.</p>
<p><strong>Then the human causes.</strong> When the body has been checked, most remaining anger has an understandable source:</p>
<ul>
<li><strong>Fear.</strong> Of needles, of the machine, of dying, of the next hospital admission. Fear often comes out as anger because anger feels less helpless.</li>
<li><strong>Loss of control.</strong> Dialysis decides when the patient eats, drinks, works, and travels. Arguing over a chair, a time slot, or the order of cannulation is sometimes the one place a patient can still exert control.</li>
<li><strong>Waiting.</strong> Late starts after a long commute, an unexplained delay, or watching another patient go first are common triggers. Delays that are explained are tolerated far better than delays that are not.</li>
<li><strong>Cost and family stress.</strong> Out-of-pocket costs for sessions, medicines, laboratory tests, and transport, lost income, and tension at home arrive in the chair with the patient.</li>
<li><strong>Perceived disrespect.</strong> Being talked about instead of to, being called by bed number, or feeling blamed for weight gain can turn a tired patient into an angry one.</li>
</ul>
<p><strong>Personality and psychiatric illness.</strong> A smaller group of patients have long-standing personality traits, untreated depression or anxiety (the mental-health sections of this module), psychosis, or cognitive impairment that make conflict more likely. These patients still deserve dialysis and dignity. Recognizing a pattern helps the team plan, but a psychiatric label never replaces a check for a medical cause on the day: a patient with a known personality disorder can also become hypoglycemic.</p>
<p><strong>Why the order matters.</strong> If the team decides too early that &ldquo;he is just difficult&rdquo;, every later outburst is read the same way, and the hypoglycemia, the infection, or the falling blood pressure is missed. Ruling out a medical cause is the first step every time, even with a patient whose behavior is familiar.</p>
"""},
    {"after": "behavior", "id": "deescalation", "nav": "De-escalation", "tag": "Behavior in the unit",
     "h2": "De-escalation, step by step",
     "html": """
<p>De-escalation is a set of communication and positioning skills that lowers the emotional temperature of a situation so that the person can think again. It is learned and practiced like cannulation; it is not a personality trait. The steps below are general. Your unit&rsquo;s policy names who is called, how security is summoned, and when treatment may be stopped.</p>
<ol>
<li><strong>Safety and space.</strong> Keep a clear path to the exit for yourself and the patient. Stand at an angle, not face to face, at more than arm&rsquo;s length. Move other patients or visitors away if needed. Do not approach alone if the person is threatening; call a colleague first. Remove or move away from objects that could be thrown, including sharps trays.</li>
<li><strong>Check the body.</strong> If it can be done safely, check glucose, blood pressure, and oxygen saturation. Ask quietly, &ldquo;Are you in pain? Do you feel faint?&rdquo;</li>
<li><strong>One speaker.</strong> Agree quickly which staff member will talk. Several people speaking at once raises the volume and the threat.</li>
<li><strong>Calm voice and body.</strong> Speak slowly, in a low and steady tone, using short sentences and the patient&rsquo;s name. Keep your hands visible and relaxed. Sit down if it is safe and the patient is seated.</li>
<li><strong>Listen and validate.</strong> Let the person say what is wrong without interruption. Name the feeling and the reason: &ldquo;You have been waiting an hour after a long trip, and nobody told you why. I would be frustrated too.&rdquo; Validating a feeling is not agreeing with the behavior.</li>
<li><strong>Offer real choices.</strong> Small, honest choices return some control: &ldquo;Would you like to sit by the window while we prepare your machine, or talk with the charge nurse first?&rdquo; Never offer a choice you cannot honor.</li>
<li><strong>Set clear, respectful limits.</strong> State the limit and the reason without threats: &ldquo;I want to help you, and I cannot do that while you are shouting at the other patients. Can we talk over here?&rdquo; Limits are about behavior, not about the person.</li>
<li><strong>Know when to stop.</strong> If the patient is connected and becomes violent, pulls at needles or lines, or the danger to the patient or others is greater than the danger of ending the session, call for help and the physician. Ending treatment early follows the unit&rsquo;s rinse-back and needle-removal procedure, with the reason, time, and amount of treatment delivered documented. If anyone is in immediate danger, staff step back and summon security according to policy. Any restraint, sedation, or transfer for psychiatric assessment is decided by the physician and governed by facility policy; it is never a nurse&rsquo;s improvised response.</li>
</ol>
<p><strong>What not to do.</strong> Do not argue, debate who is right, or try to win. Do not use sarcasm, threats, or ultimatums (&ldquo;Calm down or we will send you home&rdquo;). Do not touch an agitated person without warning, crowd them, or block their exit. Do not laugh, roll your eyes, or discuss the patient with colleagues within earshot. Do not promise what the unit cannot deliver. And do not handle an escalating person alone.</p>
<div class="table-wrap"><table>
<thead><tr><th>Behavior</th><th>What it may signal</th><th>Nursing response</th></tr></thead>
<tbody>
<tr><td>Anxious, restless, repeatedly asking questions</td><td>Fear, uncertainty, early physical illness</td><td>Check vital signs and glucose; explain what is happening and how long it will take; offer a companion or a simple task</td></tr>
<tr><td>Raised voice, complaints, refusing to cooperate</td><td>Frustration with waiting, pain, or loss of control</td><td>One calm speaker; listen and validate; explain the delay; offer choices; involve the charge nurse</td></tr>
<tr><td>Shouting, swearing, verbal abuse of staff or other patients</td><td>Anger beyond self-control; possible intoxication or delirium</td><td>Create space; set a clear limit; move other patients; second staff member present; inform the charge nurse and physician; document</td></tr>
<tr><td>Threats of harm, throwing objects, pulling at lines</td><td>High risk of injury</td><td>Step back; call for help and security per policy; physician decides on stopping treatment; protect other patients; no one acts alone</td></tr>
<tr><td>Physical assault</td><td>Immediate danger</td><td>Withdraw to safety; summon security and emergency help per policy; care for anyone injured; report through the incident system</td></tr>
</tbody></table></div>
<p>Afterward, return to the patient when calm. Many patients are embarrassed and want to repair the relationship; a brief, nonjudgmental conversation about what happened and what would help next time is often the start of a care plan.</p>
"""},
    {"after": "deescalation", "id": "agreements", "nav": "Agreements and limits", "tag": "Behavior in the unit",
     "h2": "Documentation, behavior agreements, and the limits of a unit",
     "html": """
<p><strong>Document facts, not labels.</strong> After any incident, record what was seen and heard, as close to the time as possible: the time, what the patient said in their own words, what the patient did, the vital signs and glucose, who was present, what staff did, and the outcome, including how much treatment was delivered. &ldquo;Patient shouted &lsquo;I will hit you&rsquo; and raised his fist at 10:15&rdquo; is useful; &ldquo;patient aggressive and manipulative&rdquo; is not. Labels follow a patient for years, are read by other teams, and can bias future care. File an incident report as policy requires, and hand over to the next shift using Situation, Background, Assessment, Recommendation (SBAR).</p>
<p><strong>Team review.</strong> A single incident in a patient who is frightened or ill is usually managed with the patient on the day. A pattern, or any threat or assault, is reviewed by the team: the head nurse, the attending nephrologist or medical director, and, where the facility has them, the social worker, psychologist or psychiatrist, and dietitian. The review asks what triggers the behavior, whether a medical or psychiatric cause has been missed, what the unit itself contributes (waiting, communication, scheduling), and what a fair plan looks like.</p>
<p><strong>Behavior or care agreements.</strong> A written agreement, prepared by the team and discussed with the patient, and with the family where the patient agrees, sets out expectations on both sides. A useful agreement:</p>
<ul>
<li>names the specific behaviors that are not acceptable (threats, verbal abuse, damaging equipment) in plain language;</li>
<li>states what the unit will do in return, such as explaining delays, a consistent nurse where possible, a fixed chair, a regular time to discuss concerns, or referral for counseling;</li>
<li>explains what will happen if the agreement is broken, step by step, without threats;</li>
<li>is signed or acknowledged, filed in the record, and reviewed on a set date.</li>
</ul>
<p>An agreement is a tool for helping the patient keep their place on the unit, not a step toward removing them. It works best when the patient helped write it.</p>
<p><strong>Involving family and social work.</strong> Families often know the triggers and what calms the patient. A social worker can address the cost, transport, housing, or family conflict that lies behind many outbursts and can link the patient to local government, charity, or other financial assistance. Family members can also be the source of conflict; the same rules about respectful behavior apply to companions, and they too can be asked to wait outside when necessary.</p>
<p><strong>The ethics of refusing or discharging a patient.</strong> Dialysis is life-sustaining, so removing a patient from a unit can be fatal. For that reason, in keeping with the principles in Module 12:</p>
<ul>
<li>No patient is discharged from the unit by an individual nurse, on the floor, or in the heat of the moment.</li>
<li>Involuntary discharge is a last resort, considered only after medical and psychiatric causes have been addressed, reasonable accommodations and a behavior agreement have been tried, and the pattern is documented. It is a decision of the medical director and facility management under written policy, with the patient informed and given a chance to respond.</li>
<li>Where it occurs, the patient is given reasonable notice and real help to transfer to another unit, a clinical abstract and records go with them, and the patient is told where to go for emergency dialysis in the meantime. Immediate danger to staff or patients may justify faster action, but the duty to ensure that the patient knows how to obtain life-sustaining treatment remains.</li>
<li>Facility policy, professional ethical codes, and, where needed, legal counsel govern each case. The nurse&rsquo;s role is to document accurately, raise concerns early, and advocate both for safety and for the patient&rsquo;s access to care.</li>
</ul>
<p><strong>Protecting staff and other patients.</strong> Other patients have a right to a calm, safe place to receive treatment, and staff have a right to a workplace free from violence (Module 12). Practical protections include scheduling a patient with a history of aggression when more staff are present, seating them near the station with a clear exit, assigning experienced staff, and never assigning a nurse to a patient who has assaulted them without the nurse&rsquo;s agreement.</p>
<p><strong>Debrief after an incident.</strong> A short, structured conversation soon after the event, led by the charge nurse or head nurse, asks four questions: What happened? What went well? What could we do differently? What support does anyone need? A debrief is not a search for blame. Staff who were threatened or hurt are checked on, offered time away from the bedside if needed, and directed to occupational health or counseling where the facility provides it. Lessons go into the unit&rsquo;s quality program, for example, a change in how delays are announced.</p>
"""},
]
EXTRA += [
    {"after": "agreements", "id": "exercise", "nav": "Exercise", "tag": "Longevity",
     "h2": "Muscle, movement, and exercise on dialysis",
     "html": """
<p><strong>Why muscle matters.</strong> Muscle is the body&rsquo;s protein reserve and its engine for walking, rising from a chair, and recovering from illness. On dialysis, several forces push it toward loss at once. Metabolic acidosis and inflammation switch on protein breakdown in muscle. Amino acids are lost into the dialysate at every session. Appetite is often poor, and protein intake may fall below what the body needs (Module 3). Insulin resistance, low vitamin D, anemia, and hyperparathyroidism weaken muscle further. On top of this sits inactivity: three sessions of about four hours each week spent sitting, the travel to and from the unit, and the fatigue that follows many sessions together take a large share of a patient&rsquo;s waking time and energy. Muscle that is not used is broken down. The result is a cycle in which weakness leads to less activity, which leads to more weakness, and finally to frailty, falls, and loss of independence.</p>
<p><strong>What the evidence shows.</strong> A Cochrane systematic review of 45 randomized trials with 1,863 adults with CKD, including people on dialysis, found that regular exercise improved aerobic capacity, walking capacity, resting blood pressure and heart rate, some nutritional measures, and health-related quality of life; about half of the included studies were at high risk of bias, and evidence on other outcomes was insufficient.[[heiwe2011]] Two larger trials since then are directly relevant to nurses:</p>
<ul>
<li><strong>Exercise during treatment.</strong> In a cluster-randomized trial in Germany, 1,211 patients were randomized by dialysis unit to 12 months of combined endurance and resistance training during HD sessions or to usual care. In the 917 patients analyzed, the number of times a patient could rise from a chair in 60 seconds improved in the exercise group and declined with usual care (difference 3.85 repetitions), and walking distance and the physical summary score of quality of life also favored exercise. Adverse events during sessions were similar in both groups, and mortality did not differ.[[diatt2023]]</li>
<li><strong>Exercise at home.</strong> In an Italian multicenter trial, 296 patients on dialysis were randomized to normal activity or a simple, personalized, low-intensity walking program at home on non-dialysis days, managed by dialysis staff. After six months, six-minute walking distance and sit-to-stand time improved in the walking group but not in the control group, along with scores for cognitive function and quality of social interaction.[[excite2017]]</li>
</ul>
<p>These trials show that exercise improves physical function, which patients value. They have not shown that exercise lowers mortality. A unit can therefore promote exercise honestly as a way to stay stronger, walk farther, and stay independent, without promising longer life.</p>
<p><strong>The safety screen before intradialytic exercise.</strong> Exercise during treatment is done only in a program approved by the unit, for patients cleared by the physician, following the program&rsquo;s protocol. Programs commonly schedule exercise in the first half of the session, before fluid removal has lowered blood volume much; the exact timing, type, and intensity are set by the program. Before each session, the nurse checks for reasons not to exercise that day, and stops exercise if they appear:</p>
<div class="table-wrap"><table>
<thead><tr><th>Do not start, or stop and report</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Chest pain, new or worse breathlessness, palpitations, or an irregular pulse</td><td>Possible cardiac ischemia, heart failure, or arrhythmia</td></tr>
<tr><td>Blood pressure outside the limits set by the program, or symptomatic low blood pressure</td><td>Exercise can lower or raise pressure further</td></tr>
<tr><td>Fever, acute illness, or a recent hospital admission not yet reviewed</td><td>Increased demand on a stressed body; needs physician review first</td></tr>
<tr><td>Large interdialytic weight gain with breathlessness or edema</td><td>Fluid overload; the heart is already working harder</td></tr>
<tr><td>Dizziness, cramps, nausea, or unusual fatigue during the session</td><td>Early signs of falling blood volume</td></tr>
<tr><td>Abnormal pre-dialysis potassium or glucose reported, a new foot wound, or acute joint pain</td><td>Rhythm risk, hypoglycemia, or injury</td></tr>
<tr><td>Any concern about the access, needles, or lines</td><td>Movement can dislodge needles; the access limb is kept still and visible</td></tr>
</tbody></table></div>
<p><strong>The nurse&rsquo;s role.</strong> Nurses do not prescribe exercise, but they make it possible. They identify patients who are losing strength, ask about activity at every review, encourage the patient to discuss exercise with the physician, apply the unit program&rsquo;s screen and protocol, keep the access visible throughout, and record what was done and how it was tolerated. Simple messages help: walk a little more each week on non-dialysis days, stand up from a chair several times without using the hands, take stairs where safe, and spend less of the day sitting. Pairing exercise with the dietitian&rsquo;s advice on protein intake (Module 3) matters, because muscle cannot be rebuilt without adequate protein.</p>
"""},
    {"after": "exercise", "id": "frailty-falls", "nav": "Frailty and falls", "tag": "Longevity",
     "h2": "Frailty, orthostatic hypotension, and falls",
     "html": """
<p><strong>Frailty</strong> is a state of reduced physical reserve in which a minor stress, such as an infection, a missed session, or a new medicine, causes a disproportionate decline. It is common on dialysis and not limited to the very old. Typical features are unintentional weight loss, exhaustion, weakness (poor grip or difficulty rising from a chair), slow walking, and low physical activity. A systematic review and meta-analysis of 36 studies with 56,867 patients on maintenance HD found that frailty was associated with higher mortality, more hospitalization and emergency visits, more vascular access events, and more depression, falls, and fractures.[[cheng2024]] These are associations from observational studies; frailty identifies a patient at risk, and what can be changed is the care plan.</p>
<p><strong>Recognizing frailty at the chairside.</strong> Nurses see patients more often than anyone else on the team, so they notice change first: a patient who now needs help onto the scale, walks more slowly from the waiting area, holds furniture, has lost weight, or says they no longer go out. Many units use a simple screening tool, such as a clinical frailty scale or a timed walking or sit-to-stand test, at set intervals. Report a decline rather than waiting for the next scheduled review.</p>
<p><strong>Why patients fall after dialysis.</strong> Fluid removal lowers blood volume, and the compensating tightening of blood vessels may be blunted by diabetes, age, or blood pressure medicines. When the patient stands, blood pools in the legs, and blood pressure can fall sharply: orthostatic (postural) hypotension. Add muscle weakness, poor vision, nerve damage in the feet, sedating medicines, low blood sugar after a long session without food, and a slippery floor, and the post-dialysis hour becomes the most dangerous time of the week for a fall. Module 9 covers the end-of-session check; the points that matter for falls are:</p>
<ul>
<li>Sit the patient up for a minute or two, then stand with support, and ask about dizziness before walking.</li>
<li>Check standing blood pressure for patients who are dizzy or known to drop their pressure, and report a significant fall; they do not leave until it is safe.</li>
<li>Repeated post-dialysis dizziness may mean the target weight or fluid removal rate needs review (Module 6). Report the pattern.</li>
<li>Patients who use a cane or walker bring it into the unit, and staff or a companion walk with patients at risk.</li>
</ul>
<p><strong>Teaching fall prevention and home safety.</strong> Use teach-back: ask the patient to explain in their own words what they will do, and correct any gaps.[[talevski2020]]</p>
<ul>
<li><strong>Rise slowly.</strong> Sit on the edge of the bed or chair before standing, especially after dialysis and at night. Sit down at once if dizzy.</li>
<li><strong>Light and floors.</strong> A light on the way to the toilet at night; no loose mats, cords, or clutter on the floor; wipe up spills, especially in the bathroom.</li>
<li><strong>Bathroom.</strong> A non-slip mat, a grab bar or sturdy handhold, and a plastic chair for bathing if balance is poor.</li>
<li><strong>Footwear.</strong> Closed, well-fitting, non-slip footwear instead of loose slippers; daily foot checks for those with diabetes.</li>
<li><strong>Medicines and eyes.</strong> Bring all medicines for review, including those bought without a prescription; report new sleeping pills or pain medicines; keep eyeglasses up to date.</li>
<li><strong>Stay strong.</strong> Regular walking and simple strength exercises, as cleared by the physician.</li>
<li><strong>After a fall.</strong> Report any fall to the unit. After a head injury, seek medical advice immediately, and tell the unit before the next session, because anticoagulation during dialysis may need to be held (Module 9).</li>
</ul>
<p><strong>When to refer.</strong> Report to the physician for possible referral to rehabilitation, physical therapy, or occupational therapy when a patient has fallen, is afraid of falling, has a new decline in walking or transfers, needs help with daily activities, or scores as frail on the unit&rsquo;s tool. A home safety assessment, mobility aids, and a family member trained to help can keep a patient living independently far longer.</p>
"""},
]
EXTRA += [
    {"after": "frailty-falls", "id": "adherence", "nav": "Missed and shortened sessions", "tag": "Longevity",
     "h2": "Skipped sessions, shortened sessions, and weight gain between sessions",
     "html": """
<p><strong>Why it matters.</strong> Every hour of dialysis removes potassium, fluid, acid, and toxins that the failed kidneys cannot. A skipped session leaves the patient with roughly two to three days of accumulation before the next one, the longest and most dangerous gap of the week. A shortened session delivers less of everything that the prescription was calculated to deliver (Module 6). In a large international observational study of hemodialysis practice, skipping one or more sessions a month was associated with higher mortality and more hospitalization, and interdialytic weight gain above 5.7% of body weight was associated with higher mortality.[[saran2003]] In a United States cohort of more than 34,000 patients, larger average weight gains between sessions were associated with higher all-cause and cardiovascular mortality after adjustment for nutritional status; a gain of 4 kg or more was associated with a higher risk of cardiovascular death than a gain of 1.5 to 2 kg.[[kalantar2009]] These are associations, not proof that each extra kilogram causes harm, but the physiology is consistent: a large gain forces either a fast fluid removal rate, with low blood pressure and cardiac stress, or incomplete removal, with chronic fluid overload.</p>
<p>The same study also showed something nurses should keep in mind: before adjustment, patients with larger gains tended to be better nourished, with higher protein intake and serum albumin.[[kalantar2009]] Some weight gain between sessions reflects eating well. The aim is to limit salt and excess fluid, not to frighten patients into eating less.</p>
<p><strong>The reasons behind the numbers.</strong> Patients rarely miss dialysis because they do not understand that it keeps them alive. Common reasons include:</p>
<ul>
<li><strong>Cost:</strong> sessions, medicines, laboratory tests, and transport that the patient cannot pay for this week, especially when insurance-covered sessions for the year run out.</li>
<li><strong>Transport:</strong> long commutes, unreliable rides, flooding, typhoons, and fares that cost as much as a meal.</li>
<li><strong>Symptoms:</strong> cramps, headaches, low blood pressure, or exhaustion after dialysis that make the patient dread the next session or ask to come off early.</li>
<li><strong>Depression and hopelessness:</strong> &ldquo;What is the point?&rdquo; may be the first sign of depression (the mental-health sections of this module), or of a wish to discuss stopping dialysis, which deserves a real conversation, not a lecture.</li>
<li><strong>Work, school, and family:</strong> a job that will not release the patient, children to collect, or a caregiver who is also working.</li>
<li><strong>Thirst and salt:</strong> a salty diet and high blood sugar both drive thirst; fluid limits fail when the cause of the thirst is not addressed.</li>
</ul>
<p><strong>Nonjudgmental problem-solving.</strong> Start with curiosity: &ldquo;I noticed you came off 40 minutes early the last three times. What has been happening?&rdquo; Then work on the actual reason with the patient: a different shift that fits work, a talk with the physician about cramps or post-dialysis fatigue, referral to the social worker for transport or financial help, review of salty foods with the dietitian, or screening for depression. Avoid scolding, public weighing commentary, and threats; shame drives patients away from the unit, the opposite of what is needed. Praise small improvements.</p>
<p><strong>Documenting delivered versus prescribed time.</strong> Record the prescribed treatment time and the time actually delivered for every session, with the reason for any difference: late arrival, patient request, alarms, access problems, clotting, or symptoms. If the patient asks to stop early, explain in plain words what will be lost, inform the physician as policy requires, and document the conversation and the patient&rsquo;s decision. A pattern of missed or shortened sessions is reported to the physician, because it may explain low adequacy, high potassium, or fluid overload, and because it may be the first sign that the patient is struggling.</p>
"""},
    {"after": "adherence", "id": "symptoms", "nav": "Symptom burden", "tag": "Longevity",
     "h2": "Symptom burden: asking routinely and reporting for treatment",
     "html": """
<p>Many patients on dialysis live with several symptoms at once. Because they are common, staff and patients alike may come to see them as normal and stop mentioning them. Yet symptoms are what patients feel every day, and many can be improved. The nurse&rsquo;s task is to ask about them systematically and to report them so that the physician can look for causes and treat them.</p>
<ul>
<li><strong>Fatigue and recovery time.</strong> Ask, &ldquo;How long does it take you to recover from a dialysis session?&rdquo; In a large international cohort, about one patient in ten reported more than 12 hours, and a recovery time longer than 12 hours was associated with poorer quality of life and higher risks of hospitalization and death.[[rayner2014]] Long recovery may relate to the amount of fluid removed, low blood pressure during the session, anemia, depression, poor sleep, or other illness, and is reported even when laboratory results look acceptable.</li>
<li><strong>Itching.</strong> Ask about it directly; patients often scratch silently or lose sleep over it. It may relate to dry skin, high phosphate, inadequate dialysis, or other causes, and effective treatments exist.</li>
<li><strong>Pain.</strong> From cannulation, bone and joint disease, neuropathy, ulcers, or other illness. Ask about it, rate it, and report it; pain medicines need physician review because many accumulate in kidney failure.</li>
<li><strong>Cramps.</strong> Usually late in the session and linked to fluid removal (Module 9). A pattern suggests the target weight or fluid removal rate needs review.</li>
<li><strong>Restless legs.</strong> An unpleasant urge to move the legs, worse in the evening and at rest, including during dialysis, that disturbs sleep. Iron deficiency and some medicines can contribute; it is treatable and worth reporting.</li>
<li><strong>Sleep, appetite, nausea, and mood.</strong> Each affects the others; the mental-health and sleep sections of this module give screening approaches.</li>
<li><strong>Sexual concerns.</strong> Reduced desire, erectile difficulty, menstrual changes, and fertility questions are common and rarely raised by patients. Ask respectfully and privately, with permission: &ldquo;Some people on dialysis notice changes in their sexual health. Is that something you would like to talk about?&rdquo; Accept a &ldquo;no&rdquo;, keep the answer confidential, and refer to the physician when the patient wishes.</li>
</ul>
<p><strong>Routine review and patient-reported outcomes.</strong> A symptom review works best when it is regular and structured rather than left to chance. Many units use a short symptom checklist or questionnaire completed by the patient, often with a severity rating, at set intervals, for example monthly or at each care plan review, plus a brief question at each session: &ldquo;Anything new or troubling since last time?&rdquo; Questionnaires that patients complete themselves, called patient-reported outcome measures, capture what the patient experiences rather than what staff assume. Their value depends on what happens next: every score that is high or rising is reviewed, reported, and followed up, and the patient is told what was done. A questionnaire that is filed and never acted on teaches patients not to bother answering.</p>
<p><strong>Reporting for treatment.</strong> Report symptoms with their pattern, severity, effect on daily life, and any likely trigger you have noticed, for example: &ldquo;Itch is now 8 out of 10, keeps her awake most nights, and has been getting worse for a month; last phosphate was high.&rdquo; The physician decides on investigation and treatment; nurses do not prescribe. The nurse carries out the non-drug measures in the care plan, checks whether the treatment helped at the next review, and reports again if it did not.</p>
"""},
    {"after": "symptoms", "id": "goals", "nav": "Living well", "tag": "Longevity",
     "h2": "Living well: goals, outcomes that matter, and the long relationship",
     "html": """
<p>Survival matters, but patients on dialysis also want to keep working, finish school, care for their families, worship, travel home for a fiesta or a funeral, and feel like themselves. Longevity in the full sense means more good years, not only more years.</p>
<p><strong>What patients say matters most.</strong> The Standardized Outcomes in Nephrology&ndash;Hemodialysis (SONG-HD) initiative asked patients, caregivers, and health professionals from many countries which outcomes should be measured in every trial of HD. In its international Delphi survey of more than 1,000 participants, patients and caregivers gave higher priority than health professionals to lifestyle outcomes such as the ability to travel, time free of dialysis, and feeling &ldquo;washed out&rdquo; after dialysis, while both groups prioritized vascular access problems, dialysis adequacy, fatigue, cardiovascular disease, and mortality.[[songhd2017]] The initiative then developed a core measure for fatigue, centered on how it limits patients&rsquo; ability to do their usual activities.[[songfatigue2018]] The message for the unit is that fatigue and a working access are not side issues; they are among the outcomes patients and clinicians rank highest.</p>
<p><strong>Work and school.</strong> Many patients can keep working or studying with planning. Shift scheduling around work hours, a medical certificate or letter for the employer or school when the patient asks, advice on avoiding heavy lifting with the access arm, and attention to post-dialysis fatigue all help. Losing a job also loses income and identity, so it is worth preventing.</p>
<p><strong>Travel dialysis.</strong> Patients can travel if sessions are arranged ahead at a unit at the destination. The usual requirements are booking well in advance, a recent clinical abstract and dialysis prescription from the home unit, recent hepatitis and other required test results, and a list of current medicines. Teach the patient to plan fluid and diet during travel, to carry medicines in hand luggage, and to know what to do if a session is missed.</p>
<p><strong>Faith and family life.</strong> For many Filipino patients, faith and family give dialysis its meaning. Respect religious practices that affect scheduling, diet, or fasting, and discuss them with the physician rather than forbidding them. Involve family as the patient wishes, and remember that family members, too, carry the burden of caregiving and cost.</p>
<p><strong>Kidney supportive care alongside dialysis.</strong> Supportive care is not only for people who choose not to have dialysis. It means attention to symptoms, psychological and spiritual needs, advance care planning, and support for the family, delivered together with dialysis for as long as dialysis serves the patient&rsquo;s goals.[[ckm2015]] Signs that the patient may benefit from a fuller conversation include repeated hospital admissions, steady functional decline, increasing frailty, heavy symptom burden, or a patient who says dialysis no longer feels worth it. The nurse can open the topic gently, report it, and support the physician-led discussion of goals, which may lead to changes in the dialysis plan or to conservative care (Module 5).</p>
<p><strong>The nurse&rsquo;s longitudinal relationship.</strong> Few health workers see a patient as often or for as long as the dialysis nurse: three times a week, for years. That relationship is a clinical tool. It lets the nurse notice small changes, earns the trust that allows hard questions about mood, money, or sexual health, and gives patients a steady person to turn to. Use it to ask regularly, &ldquo;What matters most to you right now, and what is getting in the way?&rdquo;, to record the answer in the care plan, and to bring it to team reviews. Care that is built around the patient&rsquo;s goals is the purpose of everything else in this module.</p>
"""},
]
QUIZ = [
    {"stem": "Ninety minutes into his session, a patient with diabetes who is usually calm begins shouting at the nurse, says she is &ldquo;useless&rdquo;, and tries to get out of the chair. He is sweaty and his speech is slurred. Which action comes first?",
     "options": [
         ("Tell him firmly that abusive language is not allowed and that he will be reported to the head nurse", False, "Setting limits has a place, but this sudden change with sweating and slurred speech suggests a medical cause, which is checked first."),
         ("Keep a safe distance, call a colleague, and check his capillary glucose, blood pressure, and oxygen saturation", True, "A sudden change in a usually calm patient, with sweating and slurred speech, suggests hypoglycemia, low blood pressure, or another medical cause. Checking the body comes before judging the behavior, with safety maintained."),
         ("Stop the treatment and remove the needles at once so that he can leave", False, "Ending treatment does not treat the likely cause, and removing needles from an agitated, possibly hypoglycemic patient is unsafe. The cause is found and treated first; stopping follows the physician and unit procedure."),
         ("Ask his companion whether he has been drinking alcohol, and document intoxication", False, "Alcohol is possible, but slurred speech and sweating in a patient with diabetes require an immediate glucose check. Labeling the cause without checking can miss a dangerous low blood sugar."),
     ],
     "objective": "Identify the medical causes of agitation and disruptive behavior in the hemodialysis (HD) unit before attributing behavior to personality, and de-escalate a tense situation step by step within unit policy.", "sources": ["anna7"], "flag": ""},
    {"stem": "A patient has verbally abused two nurses this month, and today shouted threats at another patient. A colleague says, &ldquo;We should tell him not to come back. Nobody can work with him.&rdquo; What is the most appropriate course?",
     "options": [
         ("Tell the patient at the end of today&rsquo;s session that he is discharged from the unit", False, "A nurse on the floor does not discharge a patient from life-sustaining treatment. Involuntary discharge is a last resort under written policy, decided by the medical director and management after other steps."),
         ("Document each incident factually, report it, and ask for a team review that looks for medical and social causes and prepares a behavior agreement", True, "Factual documentation, incident reporting, a team review including medical and psychiatric causes, and a behavior agreement discussed with the patient are the fair and safe steps. Other patients and staff are protected meanwhile."),
         ("Ignore the threats, since patients on dialysis are under stress and staff should expect this", False, "Stress explains but does not excuse threats. Staff and other patients are entitled to safety, and threats are reported and addressed."),
         ("Shorten his sessions so that he spends less time on the unit", False, "Shortening treatment harms the patient and is a prescription change only the physician can order; it is not a behavior management tool."),
     ],
     "objective": "Describe how documentation, team review, behavior agreements, and debriefing protect patients and staff, and state the ethical limits on refusing or discharging a patient from a dialysis unit.", "sources": ["anna7"], "flag": "Involuntary discharge procedures follow facility policy and legal advice; only general principles are taught."},
    {"stem": "A patient enrolled in the unit&rsquo;s approved intradialytic cycling program arrives with a weight gain larger than usual and says he became breathless climbing the stairs this morning. His blood pressure is within the program&rsquo;s limits. What should the nurse do about exercise today?",
     "options": [
         ("Proceed with cycling, because exercise during treatment improves physical function", False, "Exercise does improve function over months, but new breathlessness with a large weight gain suggests fluid overload or a cardiac problem, which is a reason not to exercise until reviewed."),
         ("Proceed but at double the usual time, to help remove the extra fluid", False, "Exercise is not a way of removing fluid, and doing more when the heart is stressed adds risk."),
         ("Hold exercise today, assess and report the breathlessness and weight gain to the physician, and document the reason", True, "New breathlessness and a large weight gain are on the safety screen as reasons not to start. The finding is reported for physician review, and the reason exercise was held is documented."),
         ("Remove him from the exercise program permanently, since he has not followed his fluid limits", False, "One day&rsquo;s contraindication is not a reason to remove a patient from a program, and blaming him does not address the cause."),
     ],
     "objective": "Explain why muscle and physical function decline on HD, summarize the evidence for intradialytic and home exercise, and apply a safety screen before exercise during treatment.", "sources": ["diatt2023", "heiwe2011"], "flag": "Exercise safety-screen criteria and timing are program-specific; none are quantified."},
    {"stem": "A 74-year-old woman has felt dizzy on standing after her last three sessions and fell at home last week without injury. She walks more slowly than a month ago. Which plan best fits?",
     "options": [
         ("Reassure her that dizziness after dialysis is normal and that she should rest when she gets home", False, "Repeated post-dialysis dizziness and a fall are warning signs, not normal. They need review and teaching."),
         ("Advise her to drink extra fluid after each session so that her blood pressure does not fall", False, "Extra fluid raises the next weight gain. A repeated drop in pressure is reported so that target weight and fluid removal can be reviewed."),
         ("Check standing blood pressure before she leaves, report the pattern and the fall, teach rising slowly and home safety using teach-back, and ask the physician about referral for therapy", True, "The pattern suggests orthostatic hypotension, possibly from the target weight or fluid removal rate, plus increasing frailty. Checking, reporting, teaching with teach-back, and seeking referral address both."),
         ("Ask the physician to lower her target weight so that she is less fluid-overloaded", False, "Dizziness after dialysis suggests too much or too fast fluid removal, not too little; and target weight is the physician&rsquo;s decision after review."),
     ],
     "objective": "Recognize frailty, post-dialysis orthostatic hypotension, and fall risk, and teach fall prevention and home safety, referring for therapy when needed.", "sources": ["cheng2024", "talevski2020"], "flag": ""},
    {"stem": "A 45-year-old jeepney driver has asked to come off 45 minutes early at four of his last six sessions and his weight gains have increased. Which response is most appropriate?",
     "options": [
         ("Warn him in front of the other patients that he will die if he keeps shortening treatment", False, "Public warnings shame patients and drive them away. The conversation is private and starts with understanding his reasons."),
         ("Ask privately what has been making him leave early, document delivered versus prescribed time with reasons, and report the pattern to the physician", True, "Skipped and shortened sessions are associated with hospitalization and death. Exploring the reason (work, income, cramps, fatigue, mood) without judgment, accurate documentation, and physician review allow a practical solution such as a different shift or treatment of symptoms."),
         ("Record the sessions as completed, since he agreed to come off early", False, "The record must show the time actually delivered and the reason. Recording prescribed time as delivered is inaccurate and hides under-dialysis."),
         ("Tell him the unit will no longer let him leave early under any circumstances", False, "An adult with capacity may decline the remainder of a session. The task is to explain the consequences, find the reason, and inform the physician."),
     ],
     "objective": "Address skipped and shortened sessions, high interdialytic weight gain, and symptom burden through nonjudgmental problem-solving, routine symptom review, and goals that matter to the patient.", "sources": ["saran2003", "kalantar2009"], "flag": ""},
]
TERMS = [
    ("De-escalation", "Communication and positioning skills that lower tension so that an upset person can think and cooperate again."),
    ("Delirium", "An acute, fluctuating disturbance of attention and awareness, usually caused by a medical problem such as infection, medicines, or metabolic change."),
    ("Behavior agreement", "A written plan agreed between the team and a patient that names unacceptable behaviors, what the unit will do in return, and what follows if it is broken."),
    ("Debrief", "A short, structured, blame-free team conversation after an incident about what happened, what went well, and what to change."),
    ("Intradialytic exercise", "Exercise, such as cycling or resistance training, performed in the dialysis chair during treatment under a unit program."),
    ("Frailty", "Reduced physical reserve in which a minor stress causes a disproportionate decline; marked by weight loss, exhaustion, weakness, slowness, and low activity."),
    ("Orthostatic hypotension", "A fall in blood pressure on standing that causes dizziness or fainting; common after fluid removal."),
    ("Recovery time", "The time a patient reports needing to recover after a dialysis session; long recovery is associated with poorer outcomes."),
    ("Patient-reported outcome measure", "A questionnaire completed by the patient about symptoms, function, or well-being."),
    ("Kidney supportive care", "Attention to symptoms, psychological and spiritual needs, advance care planning, and family support, alongside or instead of dialysis."),
]
FLAGS = [
    "SONG-HD: the text states only what the Delphi survey (songhd2017) and the fatigue workshop (songfatigue2018) abstracts report; the final core outcome set was not restated because its source was not verified.",
    "Intradialytic exercise timing (first half of the session) and the safety-screen items are general practice; limits and timing are program-specific and not quantified.",
    "Involuntary discharge from a dialysis unit is described in general ethical terms only; no Philippine statute, DOH rule, or PSN document on discharge was verified, so none is cited.",
    "Restraint, sedation, and psychiatric transfer are referred to physician orders and facility policy only; no instructions are given.",
    "Insurance coverage limits on sessions are mentioned generically ('insurance-covered sessions for the year run out'); no benefit numbers are stated.",
    "Travel dialysis requirements (clinical abstract, prescription, hepatitis results, medicine list) are typical; exact requirements vary by receiving unit.",
    "DiaTT hospital days (median 2 vs 5) were not taught because they were a secondary, descriptive result.",
    "Journal names not yet in common.JOURNALS: 'The Cochrane database of systematic reviews' (heiwe2011), 'NEJM evidence' (diatt2023), 'Renal failure' (cheng2024). Title-case PubMed titles needing TITLE_OVERRIDES: 28238554, 29551585, 27909047, 38320198.",
    "fetch_refs.py may not glob m14_x2.py; the NEW_REFS PMIDs must be added to refs_pubmed_raw.json before the check passes without reference errors.",
]
NEW_REFS = {
    "heiwe2011": "21975737",
    "diatt2023": "38320198",
    "excite2017": "27909047",
    "cheng2024": "39099468",
    "saran2003": "12787417",
    "kalantar2009": "19171851",
    "rayner2014": "24529994",
    "songhd2017": "28238554",
    "songfatigue2018": "29551585",
}
