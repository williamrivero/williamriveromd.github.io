# -*- coding: utf-8 -*-
# Module 14 expansion, part 1: mental health in depth (adaptation, screening, cognition and sleep, caregivers, crisis).
# Part 2 (disruptive behavior, de-escalation, exercise, frailty, adherence, symptoms, life goals) lives in m14_x2.py
# and attaches after "crisis".
OBJECTIVES = [
    "Support a patient's adaptation to hemodialysis by recognizing losses and role changes, and by drawing on family, faith, and peer support in the Filipino context.",
    "Use validated screening questionnaires as unit policy directs, and act on a positive screen through the referral pathways available in the Philippines.",
    "Recognize cognitive impairment, delirium, poor sleep, and restless legs in the unit, and adapt teaching to a patient with memory problems.",
    "Support family caregivers with attention to consent and confidentiality, and respond to suicide risk or self-neglect by asking directly, staying with the patient, and escalating per facility policy.",
]
EXTRA = [
    {"after": "bedside", "id": "adaptation", "nav": "Adaptation", "tag": "Psychological adaptation", "h2": "Adjusting to life on dialysis: losses, tasks, and sources of strength",
     "html": """
<p>Adaptation does not follow a timetable, but the early months are usually the hardest. Many patients start dialysis in an emergency, with a temporary catheter, after a hospital stay, and with little time to prepare. They meet the unit as strangers who are unwell, frightened, and often in debt. A patient who seems &ldquo;difficult&rdquo; in the first weeks is often a patient who is grieving.</p>
<p><strong>What patients lose, and what it can look like.</strong></p>
<div class="table-wrap"><table><thead><tr><th>Loss or change</th><th>How it may show in the unit</th><th>What helps</th></tr></thead><tbody>
<tr><td>Work and income; the role of provider</td><td>Shame, anger, insisting on leaving early to work, refusing extra tests because of cost</td><td>Referral to the social worker; schedule changes where possible; acknowledging the loss aloud</td></tr>
<tr><td>Role in the family (parent, spouse, eldest child)</td><td>Feeling like a burden; withdrawal; irritability at home reported by family</td><td>Finding tasks the patient can still own; involving the family, with consent</td></tr>
<tr><td>Control over time, food, and fluid</td><td>Breaking the fluid limit, arguing about the schedule, &ldquo;forgetting&rdquo; medicines</td><td>Giving real choices within safe limits; teaching the patient to track their own numbers</td></tr>
<tr><td>Body image (fistula, catheter, skin color, weight change)</td><td>Hiding the arm, refusing a fistula, avoiding social events</td><td>Private, matter-of-fact discussion; meeting a peer who has lived with an access for years</td></tr>
<tr><td>Freedom to travel and plan</td><td>Missing family events in the province or abroad</td><td>Explaining that holiday dialysis can be arranged with notice</td></tr>
<tr><td>Sexual life and intimacy</td><td>Rarely raised by the patient; may surface as tension between spouses</td><td>Asking permission to discuss it; referral to the physician, since causes include medicines and hormones</td></tr>
<tr><td>Expected future</td><td>Hopelessness; waiting for a transplant that may not come</td><td>Honest information; setting near-term goals the patient chooses</td></tr>
</tbody></table></div>
<p><strong>Tasks of adjustment.</strong> Over time, most patients work through a similar set of tasks: understanding what dialysis does and does not do; learning the routine of fluid, food, medicines, and access care; managing symptoms; finding a new role at home and, where possible, at work; deciding about transplant or other options with the team (Module 5); and making some peace with uncertainty. The nurse can help with each, mostly by explaining, by giving the patient a part in their own care, and by noticing when a task has stalled.</p>
<p><strong>The Filipino context.</strong> Family is usually the center of care and of decision-making. Many families pool income, and relatives working overseas often help pay for treatment. Some patients hide how badly they feel so as not to add to their family&rsquo;s worries, or feel deep shame at being dependent; others defer every decision to an adult child. Kidney failure and dialysis still carry stigma in some communities, where dialysis may be seen as the beginning of the end. None of these patterns applies to every Filipino patient, so ask rather than assume: &ldquo;Who helps you make decisions about your health?&rdquo; and &ldquo;Who knows how you are really feeling?&rdquo;</p>
<p><strong>Faith and meaning.</strong> For many patients, faith is a main source of strength: prayer before treatment, a rosary on the chair, a pastor&rsquo;s visit. Respect it, and offer the chaplain or the patient&rsquo;s own faith leader when the patient wishes. Faith can also become a reason not to speak of despair (&ldquo;God will take care of it&rdquo;) or a source of guilt (&ldquo;This is a punishment&rdquo;). The nurse does not argue theology; the nurse listens, and still asks about mood and safety.</p>
<p><strong>Peer support.</strong> Fellow patients are often the most believable teachers. A newly started patient may accept advice from someone who has dialyzed for ten years that they would not accept from staff. With consent on both sides, units can pair new patients with an experienced &ldquo;buddy,&rdquo; hold informal group sessions, or link patients with kidney patient support groups where they exist. Peers do not replace professional care for depression, and a buddy should know whom to tell if they are worried about someone.</p>
"""},
    {"after": "adaptation", "id": "screening", "nav": "Screening", "tag": "Screening and referral", "h2": "Screening for depression, anxiety, and related problems, and what happens next",
     "html": """
<p>Screening means using a validated questionnaire to find patients who need further assessment. It does not diagnose, and it does not replace asking and listening. Its value is consistency: problems that might be missed because a patient seems cheerful, quiet, or &ldquo;always like that&rdquo; are picked up the same way for everyone.</p>
<div class="table-wrap"><table><thead><tr><th>What is screened</th><th>Examples of validated tools</th><th>Notes for the dialysis unit</th></tr></thead><tbody>
<tr><td>Depression</td><td>Patient Health Questionnaire (nine-item) and its two-item short form; Beck Depression Inventory (second edition); Hospital Anxiety and Depression Scale</td><td>Physical symptoms of kidney failure overlap with depression items, so scores are interpreted by a clinician.[[palmer2013]] The ninth item of the nine-item questionnaire asks about thoughts of death or self-harm.</td></tr>
<tr><td>Anxiety</td><td>Generalized Anxiety Disorder scale (seven-item); Hospital Anxiety and Depression Scale</td><td>Anxiety often accompanies depression and may focus on needles, alarms, cost, or death.</td></tr>
<tr><td>Cognition</td><td>Mini-Cog; Montreal Cognitive Assessment</td><td>Done by trained staff, at a consistent time in the dialysis cycle (see the next section).</td></tr>
<tr><td>Delirium</td><td>Confusion Assessment Method</td><td>Used by staff trained in it; a new change in alertness is reported whether or not a tool is used.</td></tr>
<tr><td>Sleep</td><td>Pittsburgh Sleep Quality Index</td><td>Ask also about snoring with breathing pauses and about restless legs.</td></tr>
<tr><td>Caregiver strain</td><td>Zarit Burden Interview</td><td>Given to the caregiver, privately, with their agreement.</td></tr>
</tbody></table></div>
<p><strong>Who screens, and how often.</strong> Unit policy decides which tool is used, in which language version, who gives it (a trained nurse, social worker, or psychologist), and how often. A common pattern is to screen soon after a patient starts dialysis, then at regular intervals, and again whenever something changes: a hospital stay, a bereavement, missed sessions, a new behavior. Use only versions that have been translated and validated for the language the patient reads, and do not translate questions on the spot unless the policy allows it.</p>
<p><strong>How to give it.</strong> Explain why you are asking (&ldquo;We ask all our patients these questions, because feeling down is common on dialysis and can be treated&rdquo;), obtain the patient&rsquo;s agreement, give privacy, and read the questions aloud for a patient who cannot read them. Do not screen a patient who is hypotensive, hypoglycemic, or confused.</p>
<p><strong>What a positive screen triggers.</strong></p>
<ul>
<li><strong>A score above the unit&rsquo;s threshold:</strong> tell the patient the result in plain words, record it, and report it to the nephrologist the same day for clinical assessment and a decision on referral.</li>
<li><strong>Any positive answer about thoughts of death or self-harm, whatever the total score:</strong> follow the crisis steps below at once.</li>
<li><strong>A negative screen in a patient you are still worried about:</strong> report your concern anyway. A questionnaire does not overrule a nurse&rsquo;s observation.</li>
</ul>
<p><strong>Referral pathways in the Philippines.</strong> Services vary widely by region. Common routes include the nephrologist&rsquo;s own assessment and treatment; the hospital&rsquo;s psychiatry or psychology service; an outpatient psychiatrist or psychologist, in person or by teleconsultation; the local health center, where mental health services are increasingly offered at the primary-care level; and the National Center for Mental Health and regional mental health facilities for more complex needs. The social worker helps with cost, which is often the deciding barrier, and with checking current Philippine Health Insurance Corporation (PhilHealth) and local government assistance. Each unit should keep an up-to-date list of its referral contacts, and the nurse should know where it is.</p>
"""},
    {"after": "screening", "id": "cognition-sleep", "nav": "Memory and sleep", "tag": "Cognition and sleep", "h2": "Memory, delirium, sleep, and restless legs in the unit",
     "html": """
<p><strong>Recognizing cognitive impairment.</strong> Cognitive impairment is common in HD patients and is often not recorded.[[murray2006]] Clues in the unit include repeated questions about things explained before, confusion about the schedule, medicine errors, a companion who answers every question, unexplained missed sessions, difficulty learning a new routine, and a family that reports getting lost or forgetting meals. Report these for assessment; the nurse does not label a patient as having dementia.</p>
<p><strong>Timing matters.</strong> In a small study of older HD patients, thinking was worst during the session and best shortly before it or on the day after.[[murray2007]] Cognitive screening, important teaching, and consent conversations are therefore best done before connection or on a non-dialysis day, not late in the session or just after it. Repeat tests should use the same instrument and similar timing so that a change is real and not an artifact; the course&rsquo;s cognitive screening and score-comparison tools are built around these rules.</p>
<p><strong>Delirium on the unit.</strong> Delirium may begin during or after a session, especially in older patients, after a hospital stay, with infection, or after a new medicine. Watch for a patient who is suddenly drowsy, agitated, pulling at lines, or unable to keep attention on a simple conversation. Keep the patient safe at the chair, check BP, glucose, and oxygen, and report immediately. A patient with delirium is not sent home alone.</p>
<p><strong>Teaching a patient with memory problems.</strong></p>
<ul>
<li>One main message per session, in short sentences, in the patient&rsquo;s own language.</li>
<li>Pictures, large print, and written reminders the patient keeps; a medicine box or blister pack prepared with the pharmacist.</li>
<li>Teach-back: ask the patient to explain in their own words or show you, and repeat until it is right.[[talevski2020]]</li>
<li>Involve the caregiver, with consent, and give the same message to both.</li>
<li>Build routines: same day, same chair, same sequence where possible.</li>
<li>Check understanding again at the next session rather than assuming it lasted.</li>
</ul>
<p><strong>Sleep.</strong> Poor sleep is one of the most common complaints on dialysis, and it feeds low mood, poor memory, and irritability. Ask about it directly. Practical advice the nurse can give:</p>
<ul>
<li>Keep a regular time for waking, even after a bad night.</li>
<li>Limit long naps; a short rest is fine, but sleeping through every session may make nights worse.</li>
<li>Get daylight and some activity during the day.</li>
<li>Avoid coffee, strong tea, cola, and energy drinks in the afternoon and evening, and avoid alcohol and smoking near bedtime.</li>
<li>Keep the bedroom dark, quiet, and cool, and keep the phone away from the bed.</li>
</ul>
<p>Some sleep problems need the physician, not advice. Report waking breathless or needing extra pillows (possible fluid overload), loud snoring with pauses in breathing or severe daytime sleepiness (possible sleep apnea), itch or cramps that keep the patient awake, and use of over-the-counter sleeping pills, many of which contain sedating antihistamines that can accumulate in kidney failure and may worsen restless legs.</p>
<p><strong>Restless legs.</strong> Patients describe an urge to move the legs, often with crawling or aching sensations, that comes on at rest, is worse in the evening and at night, and is relieved by moving. It is common in dialysis patients, can make sitting through a session difficult, and is a frequent cause of poor sleep. Iron deficiency is one recognized contributor, and some medicines, including sedating antihistamines, some antidepressants, and some antinausea medicines, can make it worse. The nurse&rsquo;s part is to recognize the description, report it so the physician can review iron status and medicines, and suggest simple measures while the patient waits: stretching or walking when possible, massage, and warmth. Restless legs that drive a patient to cut sessions short is a reason to report promptly.</p>
"""},
    {"after": "cognition-sleep", "id": "caregivers", "nav": "Caregivers", "tag": "Family and caregivers", "h2": "Supporting caregivers: strain, family meetings, respite, and consent",
     "html": """
<p>Behind most patients on HD is at least one caregiver: a spouse, an adult child, a sibling, sometimes a teenager. Caregivers bring the patient three times a week, wait for hours, manage medicines, cook to a renal diet, pay bills, and watch for danger at night, often while working or raising children. Module 10 describes caregiver burnout in home dialysis; the same strain builds more quietly around in-center HD.</p>
<p><strong>Signs of caregiver strain.</strong> Exhaustion, irritability with the patient or staff, missed work, their own health problems neglected, tearfulness in the waiting area, saying &ldquo;I cannot do this anymore,&rdquo; and, in severe cases, neglect or harsh treatment of the patient. Ask the caregiver directly and separately: &ldquo;How are <em>you</em> managing?&rdquo; A caregiver strain questionnaire can be used if the unit offers one. Refer a struggling caregiver to the social worker, and encourage them to see their own physician.</p>
<p><strong>Respite and sharing the load.</strong> Practical help is often more valuable than advice. Help the family list the tasks (transport, waiting, medicines, meals, money, night-time help) and see which can be shared among relatives, neighbors, the parish or community, or paid help. A rotation, so that no single person attends every session, is a simple form of respite. Relatives abroad can contribute by video call, and by covering specific costs, which can relieve the one who is present.</p>
<p><strong>Family meetings.</strong> When decisions are large or the family is in conflict, a planned meeting works better than corridor conversations.</p>
<ol>
<li><strong>Prepare:</strong> agree the purpose with the nephrologist; ask the patient who should attend and what may be discussed; book a private room; include the social worker.</li>
<li><strong>Open:</strong> introductions; the patient&rsquo;s permission restated; what the meeting is for.</li>
<li><strong>Listen first:</strong> ask what the patient and family understand and what worries them most.</li>
<li><strong>Inform:</strong> the physician gives medical information in plain language; the nurse adds the practical picture.</li>
<li><strong>Plan:</strong> agree who does what, by when, and how the team can be reached.</li>
<li><strong>Close and record:</strong> summarize, check understanding, and document who attended, what was agreed, and what remains open.</li>
</ol>
<p><strong>Consent and confidentiality.</strong> An adult patient who can make decisions controls what is shared with family, even close family, and personal health information is protected under Philippine data privacy law.[[ra10173]] Ask the patient early and record the answer: who may receive information, and how much. Do not discuss a patient&rsquo;s mood or diagnosis with relatives in the waiting area or by text without that consent. When a patient cannot make decisions, for example during delirium or with advanced dementia, follow facility policy on who may act for them. The exception for immediate danger to life is defined by facility policy and is covered in the next section. Advance care planning (Module 5) helps a family know the patient&rsquo;s wishes before a crisis forces the question.</p>
"""},
    {"after": "caregivers", "id": "crisis", "nav": "Crisis response", "tag": "Crisis response", "h2": "Suicide risk and self-neglect: ask, stay, escalate",
     "html": """
<p>Suicide among people on dialysis is uncommon, but in a large national study from the United States it occurred more often than in the general population. Older age, male sex, alcohol or drug dependence, and a recent hospital admission for mental illness were among the factors associated with it.[[kurella2005]] Because the dialysis nurse sees patients so often, the nurse may be the first to hear that someone is in danger.</p>
<p><strong>Warning signs.</strong> Talking about being a burden or about wanting to die; hopelessness (&ldquo;There is no point&rdquo;); saying goodbye or giving away possessions; sudden calm after a period of deep low mood; withdrawal from family and fellow patients; increased drinking; and a positive answer to the self-harm item of a screening questionnaire.</p>
<p><strong>Self-neglect.</strong> Some patients put themselves at risk without saying so: repeatedly missing sessions, drinking far beyond the fluid limit, eating high-potassium foods on purpose, or stopping medicines. These may come from cost, misunderstanding, or exhaustion, but they can also be a sign of depression or a wish to die. They are different from an informed decision to stop dialysis, made with the physician and family after a proper conversation (Modules 5 and 12). Both deserve the same first step: ask the patient what is happening and tell the nephrologist.</p>
<p><strong>Ask directly.</strong> If you are worried, ask in private and in plain words: &ldquo;Sometimes when people feel this way, they think about ending their life. Are you having thoughts like that?&rdquo; Asking directly does not put the idea into a person&rsquo;s mind; it tells them it is safe to talk. If the answer is yes, ask whether the thoughts are present now, whether there is a plan, and whether anything has happened already, then listen. Use a calm voice, and do not argue, lecture, or make promises you cannot keep, including a promise of secrecy.</p>
<p><strong>Stay with the patient.</strong> A patient who describes current thoughts of ending their life is not left alone. On the unit, ask a colleague to call the physician while you stay. Keep the patient within sight, follow facility policy for keeping the area safe, and do not let the patient leave alone. If the patient is still on the machine, continue the treatment safely unless the physician directs otherwise.</p>
<p><strong>Escalate immediately, per facility policy.</strong> Inform the nephrologist or physician on duty at once, and follow the facility&rsquo;s crisis pathway, which may include urgent psychiatric assessment or transfer to an emergency department. This is a situation in which information is shared with the family or others who can keep the patient safe, even without consent, within the limits facility policy defines. The National Center for Mental Health operates a crisis hotline, reached by the toll-free number 1553, which patients and families can use outside the unit; check the current number and hours before giving it, and use it alongside, never instead of, the facility&rsquo;s pathway.</p>
<p><strong>Document.</strong> Record the patient&rsquo;s exact words, the questions you asked and the answers, the time, whom you informed and when, what was decided, who stayed with the patient, and with whom the patient left the unit. Plan follow-up at the next session.</p>
<p><strong>Afterward.</strong> A patient who has spoken about suicide needs continued, ordinary kindness at every session, not avoidance. Staff who have been through such an event, or the death of a patient by suicide, need a debriefing and support; seek it through the head nurse or medical director.</p>
"""},
]
QUIZ = [
    {"stem": "Three months after starting HD, a 38-year-old father of three who used to drive a delivery truck is angry with staff, argues about his fluid limit, and says, &ldquo;I am no longer the man of this house.&rdquo; What is the most helpful nursing approach?",
     "options": [
         ("Remind him firmly that other patients follow the rules without complaining", False, "Comparison and firmness without understanding usually deepen anger and shame."),
         ("Acknowledge the loss of his work and role, give him real choices within safe limits, and offer the social worker and, with his consent, a peer who has adapted", True, "His anger is linked to lost work and lost role. Acknowledging the loss, giving back some control, and practical and peer support address the cause."),
         ("Document him as a behavior problem and ask the nephrologist to discharge him from the unit", False, "Early anger is common in adaptation. Discharge is never a floor-level decision, and this is not a safety emergency."),
         ("Avoid talking with him about it, because men in the Philippines do not discuss feelings", False, "Assumptions about culture can prevent the conversation the patient needs. Ask rather than assume."),
     ],
     "objective": "Support a patient's adaptation to hemodialysis by recognizing losses and role changes, and by drawing on family, faith, and peer support in the Filipino context.",
     "sources": ["anna7"], "flag": ""},
    {"stem": "A patient&rsquo;s depression screening score is above the unit&rsquo;s threshold. She answers &ldquo;not at all&rdquo; to the question about thoughts of death or self-harm. What should the nurse do next?",
     "options": [
         ("Tell her she has depression and suggest she ask her pharmacist for an antidepressant", False, "A screen is not a diagnosis, and the nurse does not recommend psychiatric medicines."),
         ("Repeat the questionnaire next month to see whether the score improves", False, "Waiting delays assessment; a positive screen is reported now."),
         ("Explain the result in plain words, record it, and report it to the nephrologist the same day for assessment and a referral decision", True, "This is the expected response to a positive screen without self-harm thoughts. The physician assesses and decides on referral and treatment with the patient."),
         ("Activate the crisis pathway and arrange emergency transfer", False, "The crisis pathway is for thoughts of self-harm or suicide or other immediate danger; this patient denied them."),
     ],
     "objective": "Use validated screening questionnaires as unit policy directs, and act on a positive screen through the referral pathways available in the Philippines.",
     "sources": ["palmer2013"], "flag": "Threshold scores and reporting timelines follow unit policy."},
    {"stem": "You need to teach a 70-year-old patient with mild memory problems how to recognize signs of a clotted fistula. When is the best time, and what is the best approach?",
     "options": [
         ("Late in the session, when the patient is resting and has time to listen; give all the access teaching at once", False, "Thinking is worst during treatment, and too many messages at once overwhelm a patient with memory problems."),
         ("Before connection or on a non-dialysis day, with one main message, a written reminder, and teach-back, with the caregiver present if the patient agrees", True, "Cognition tends to be best before treatment or on the next day. One message, a written aid, teach-back, and caregiver involvement suit memory problems."),
         ("Right after disconnection, so the instruction is fresh when the patient goes home", False, "Just after the session is often a time of fatigue and slower thinking."),
         ("Teach only the caregiver, since the patient will not remember", False, "The patient is taught too, as far as they are able, and the caregiver is involved with consent."),
     ],
     "objective": "Recognize cognitive impairment, delirium, poor sleep, and restless legs in the unit, and adapt teaching to a patient with memory problems.",
     "sources": ["murray2007", "talevski2020"], "flag": ""},
    {"stem": "The wife of a patient on HD is tearful in the waiting area. She says she has not slept properly in weeks, has missed work to bring him to every session, and asks you how her husband&rsquo;s depression screen came out. What is the best response?",
     "options": [
         ("Tell her the result, because she is his wife and his main caregiver", False, "Information about his mood is shared with family only with his consent."),
         ("Ask how she is managing, refer her to the social worker for support and respite planning, and explain that you will ask her husband whether his results can be shared with her", True, "This attends to her strain and respects his confidentiality, while opening the way to involve her with consent."),
         ("Tell her the information is confidential and end the conversation", False, "Confidentiality is respected, but her own distress also needs a response."),
         ("Suggest she ask her husband to take a tricycle alone so she can rest", False, "Practical changes are planned with the patient and family, not suggested on the spot without assessing his safety to travel alone."),
     ],
     "objective": "Support family caregivers with attention to consent and confidentiality, and respond to suicide risk or self-neglect by asking directly, staying with the patient, and escalating per facility policy.",
     "sources": ["ra10173"], "flag": ""},
    {"stem": "During treatment, a patient tells you that he has been thinking about ending his life and that he does not want to go on. What should you do first?",
     "options": [
         ("Change the subject to something hopeful to lift his mood", False, "Changing the subject tells him the topic is not safe to discuss."),
         ("Promise to keep it secret so that he will keep talking to you", False, "A promise of secrecy cannot be kept when his life may be in danger."),
         ("Finish the rounds of your other patients and come back to him when you have time to talk", False, "A patient with current thoughts of ending his life is not left alone."),
         ("Stay with him, ask calmly about the thoughts and whether there is a plan, have a colleague call the physician, and follow the facility&rsquo;s crisis pathway", True, "Asking directly is safe, staying keeps him safe, and immediate escalation through the facility pathway brings the help he needs."),
     ],
     "objective": "Support family caregivers with attention to consent and confidentiality, and respond to suicide risk or self-neglect by asking directly, staying with the patient, and escalating per facility policy.",
     "sources": ["kurella2005"], "flag": "Crisis steps follow the facility's crisis pathway."},
]
TERMS = [
    ("Peer support", "Help and encouragement given by a fellow patient who has lived with the same treatment."),
    ("Positive screen", "A questionnaire result above the threshold set by policy, meaning the person needs clinical assessment; not a diagnosis."),
    ("Teach-back", "Asking a patient to explain or show in their own words what they have been taught, to confirm understanding."),
    ("Restless legs", "An urge to move the legs, often with unpleasant sensations, that comes on at rest, is worse in the evening, and is relieved by movement."),
    ("Sleep apnea", "Repeated pauses in breathing during sleep, often with loud snoring and daytime sleepiness."),
    ("Caregiver strain", "The physical, emotional, and financial burden carried by a person who cares for someone with a chronic illness."),
    ("Respite", "Planned relief for a caregiver, by sharing or handing over caregiving tasks for a time."),
    ("Family meeting", "A planned meeting of the patient, family, and care team to share information and agree on a plan."),
    ("Self-neglect", "Repeated behavior that puts a person's own health at risk, such as missing treatments or ignoring limits."),
    ("Crisis pathway", "The facility's written steps for responding immediately to a patient at risk of harming themselves."),
]
FLAGS = [
    "Adaptation section: losses, tasks, and the Filipino family, faith, and stigma descriptions are drawn from general psychosocial nephrology practice and local experience, not from a cited Philippine study; a reviewer familiar with Filipino patients should confirm the tone and avoid stereotyping.",
    "Screening table: instruments are named without cut-off scores. Which tools, language versions (validated Filipino or regional-language versions), intervals, thresholds, and who administers them must be set by unit policy. The Confusion Assessment Method, Montreal Cognitive Assessment, and Patient Health Questionnaire have licensing or training requirements that the unit should confirm.",
    "Referral pathways in the Philippines are described generally; the statement that mental health services are increasingly offered at the primary-care level reflects the direction of the Philippine Mental Health Act of 2018 (Republic Act No. 11036) and was not cited; confirm current local availability and PhilHealth coverage.",
    "Crisis line: the National Center for Mental Health crisis hotline toll-free number 1553 was verified only in a news report dated November 6, 2025 (Letran 'The Lance'); verify against the center's official channels and recheck before each course intake. The lesson tells nurses to confirm the number and hours before giving it.",
    "Crisis section: wording follows general safe-messaging practice (no methods, direct asking, staying, escalation). The statement that asking directly does not plant the idea is widely accepted in suicide-prevention guidance but is not cited here. Suicide risk factors are cited only from the United States study (Kurella 2005); Philippine data were not used.",
    "Cognition timing cites a small cohort (Murray 2007, 28 subjects); stated as one study's finding.",
    "Restless legs and sleep content (iron deficiency as a contributor, medicines that worsen it, over-the-counter sleep aids containing sedating antihistamines) is general clinical knowledge without a cited source; consider adding a restless-legs or sleep review reference.",
    "Confidentiality exception for imminent danger is stated in general terms; confirm with the facility's legal and data privacy officer how the Data Privacy Act and the Mental Health Act apply.",
]
NEW_REFS = {
    "palmer2013": "23486521",
    "farrokhi2014": "24183836",
    "lopes2002": "12081579",
    "weisbord2014": "25081360",
    "alsalmi2018": "30146421",
    "cukor2014": "24115478",
    "friedli2017": "28126706",
    "cast2017": "29101402",
    "ascend2019": "30802897",
    "murray2006": "16864811",
    "murray2007": "17660028",
    "kurella2005": "15659561",
}
