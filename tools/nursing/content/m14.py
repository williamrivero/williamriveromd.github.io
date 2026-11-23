# -*- coding: utf-8 -*-
# Module 14 (core, studied before the capstone): living well on hemodialysis.
# Base sections: model, physiology (brain, mood, sleep, and behavior), evidence, bedside (the nurse's role).
# m14_x.py (part 1) adds the mental-health sections after "bedside": adaptation, screening, cognition-sleep, caregivers, crisis;
# m14_x2.py (part 2) adds disruptive behavior, de-escalation, exercise, frailty, adherence, symptoms, and life goals after "crisis".
MODULE = {
    "sub": "Why mood, memory, sleep, and behavior change on hemodialysis, what the evidence shows about depression and its treatment, and what the nurse at the chair can notice, ask, screen, report, and do to help patients and families live well, and live longer.",
    "desc": "Core Module 14 of the Nephrology Nursing & Hemodialysis self-study series: psychological adaptation to hemodialysis, the biology of mood, cognition, and sleep in kidney failure, depression and anxiety screening and referral, delirium, caregivers, and the nurse's response to suicide risk.",
    "keywords": "depression hemodialysis nursing, anxiety dialysis patient, psychological adaptation hemodialysis, delirium dialysis unit, cognitive impairment hemodialysis, restless legs dialysis, caregiver burden kidney failure, suicide risk dialysis nurse",
    "objectives": [
        "Describe adaptation to hemodialysis as an ongoing process, and name the losses and tasks it involves for patients and families.",
        "Explain the biological links between kidney failure, the dialysis session, and changes in mood, thinking, sleep, and behavior, and distinguish delirium from depression and dementia.",
        "Summarize, with calibrated language, what is known about depression in hemodialysis: how common it is, what it is associated with, and what treatment trials have and have not shown.",
        "Apply the nurse's role in mental health at the chair: notice, ask, listen, screen per unit policy, document, refer, involve the family with consent, and look after yourself.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Mental model", "h2": "A life rearranged three times a week",
         "html": """
<p>Picture a week before dialysis: work, meals, family, church, a drink with friends, a trip to the province. Now take out three half-days, each about four hours on the machine plus travel and waiting, and fix them in the same places every week, for years. Add a fluid limit, a food list, a box of medicines, needles in the arm, and a body that feels different after each treatment. That is hemodialysis (HD) as the patient lives it. It is not one event. It is a life rearranged around a schedule.</p>
<p>Adaptation is how a person rebuilds a life that works inside that new shape. It is a process, not a stage passed once. Most patients move back and forth between shock, grief, anger, bargaining, resignation, and a working acceptance. They move again when something changes: a failed access, a hospital stay, a lost job, a death in the family, a transplant that does not come. A patient who seemed settled for two years can be in crisis this month.</p>
<p>The picture has two limits. First, a low mood on dialysis is not always &ldquo;understandable sadness.&rdquo; Kidney failure and its treatment change the brain&rsquo;s chemistry, blood supply, and sleep. Some of what looks like attitude is biology, and some of what looks like biology is depression that can be treated. Second, the picture shows one person, and the family adapts too. In the Philippines, chronic kidney disease (CKD) that needs dialysis is usually a family event. Costs, transport, and caregiving are shared across a household, and sometimes across countries.</p>
<p>You see each patient for about twelve hours a week, more than any other professional does. That makes you the person most likely to notice a change, and the person a patient is most likely to tell. Most changes in mood and behavior on the unit are understandable responses to a hard life. A few are the first sign of delirium, of a treatable depression, or of danger to the patient&rsquo;s life. Your work is to notice, to ask, and to make sure the right person hears what you found. Part 2 of the module covers difficult behavior in the unit, physical function, and living longer.</p>
"""},
        {"id": "physiology", "nav": "Brain and body", "tag": "Physiology in depth", "h2": "How kidney failure and dialysis affect mood, thinking, sleep, and behavior",
         "html": """
<p>Mood, memory, attention, and sleep all depend on a brain that receives steady blood flow, enough oxygen and glucose, a stable chemical environment, and restful sleep. Kidney failure and the dialysis session disturb each of these. The mechanisms below are reasonably well supported. In any one patient several act together, and the weight of each is often unknown.</p>
<div class="table-wrap"><table><thead><tr><th>Mechanism</th><th>What happens</th><th>What the nurse may see</th></tr></thead><tbody>
<tr><td>Retained solutes</td><td>Many substances normally cleared by the kidney accumulate; some are thought to affect nerve cells and the blood vessels of the brain. Dialysis removes small molecules well but others less completely.</td><td>Slowed thinking, poor concentration, low energy, irritability; worse when sessions are missed or shortened</td></tr>
<tr><td>Chronic inflammation</td><td>Inflammatory signals are raised in kidney failure. In other illnesses the same signals produce &ldquo;sickness behavior&rdquo;: fatigue, withdrawal, poor appetite, and low mood.</td><td>Symptoms that overlap with depression, especially tiredness and loss of interest</td></tr>
<tr><td>Anemia</td><td>Less oxygen is carried to the brain and muscles.</td><td>Fatigue, breathlessness, poor concentration, low tolerance for activity</td></tr>
<tr><td>Blood pressure and fluid shifts during treatment</td><td>Rapid fluid removal can lower blood pressure (BP) and blood flow to the brain in some patients. Imaging studies suggest that repeated falls may be associated with changes in the brain&rsquo;s white matter over time; cause and effect are not proven.</td><td>Yawning, dizziness, confusion, or a &ldquo;washed-out&rdquo; feeling late in the session and after it (Module 9)</td></tr>
<tr><td>Osmotic shifts</td><td>Urea falls faster in blood than in brain cells; water moves into the brain. Severe in disequilibrium (Module 9); milder forms may contribute to headache and fatigue after treatment.</td><td>Headache, nausea, restlessness, tiredness after treatment</td></tr>
<tr><td>Disturbed sleep</td><td>Daytime naps on the machine, itch, cramps, restless legs, breathing pauses during sleep, worry, and noise disrupt night sleep.</td><td>Daytime sleepiness, irritability, poor memory, low mood</td></tr>
<tr><td>Medicines</td><td>Drugs cleared by the kidney accumulate. Examples include some pain medicines, some nerve-pain medicines, sedating antihistamines, and some antinausea medicines.</td><td>Drowsiness, confusion, falls, hallucinations, often after a new medicine or a dose increase</td></tr>
<tr><td>Glucose and electrolytes</td><td>Insulin and some diabetes medicines are cleared more slowly, and appetite is often poor, so low blood sugar is common in diabetic patients. Low sodium and high calcium can also affect the brain.</td><td>Sweating, anger, confusion, odd behavior, or drowsiness that can look like a psychiatric problem</td></tr>
</tbody></table></div>
<p><strong>Why this matters at the chair.</strong> Many of these causes can be reversed, fully or in part. A patient who is suddenly angry may be hypoglycemic. A patient who is newly forgetful may be accumulating a medicine. A patient who is exhausted and withdrawn may be anemic, underdialyzed, not sleeping, depressed, or all of these. So your first step is always physical. Check BP and blood glucose, look at the medicine list and recent laboratory results, and ask about sleep, before you conclude that a change is &ldquo;just psychological.&rdquo;</p>
<p><strong>Delirium, depression, and dementia.</strong> These three cause most changes in thinking and mood on the unit. They can occur together, and each makes the others harder to recognize.</p>
<div class="table-wrap"><table><thead><tr><th></th><th>Delirium</th><th>Depression</th><th>Dementia (major cognitive impairment)</th></tr></thead><tbody>
<tr><td>Onset</td><td>Sudden, over hours to days</td><td>Over weeks</td><td>Gradual, over months to years</td></tr>
<tr><td>Course</td><td>Fluctuates through the day; often worse at night</td><td>Persistent low mood or loss of interest most days</td><td>Slowly progressive</td></tr>
<tr><td>Attention and alertness</td><td>Disturbed: drowsy or agitated, cannot follow a conversation</td><td>Usually normal, though concentration is poor</td><td>Normal until late stages</td></tr>
<tr><td>Typical causes in dialysis patients</td><td>Infection, low BP, low blood sugar, low oxygen, medicines, stroke, missed treatments</td><td>Losses, illness burden, biology of kidney failure, past history</td><td>Vascular disease, stroke, Alzheimer disease, and other causes</td></tr>
<tr><td>Nursing response</td><td><strong>A medical emergency until explained:</strong> check BP, glucose, oxygen, and temperature; report immediately</td><td>Ask, screen per policy, report, and refer</td><td>Adapt teaching and safety; involve the family; report for assessment</td></tr>
</tbody></table></div>
<p><strong>A <em>new</em> change in alertness or attention is delirium, and therefore a physical problem, until a physician has assessed it.</strong></p>
"""},
        {"id": "evidence", "nav": "Evidence", "tag": "Evidence", "h2": "What is known about depression, anxiety, and their treatment",
         "html": """
<p><strong>How common it is.</strong> A systematic review pooled observational studies of adults on dialysis. Depression confirmed by clinical interview affected about one in four. Self-report rating scales flagged depressive symptoms in more, about four in ten. The authors suggest that rating scales may overestimate depression in dialysis patients, partly because fatigue, poor sleep, and poor appetite are symptoms of both kidney failure and depression.[[palmer2013]] Anxiety is also common, often alongside depression, but it has been studied less. Cognitive impairment is common too, and often unrecognized. In one study of HD patients aged 55 and over, only about one in eight had normal cognition on formal testing, and very few had impairment recorded in their charts.[[murray2006]]</p>
<p><strong>What depression is associated with.</strong> Across many observational studies, depressive symptoms in dialysis patients are associated with higher mortality.[[farrokhi2014]] In a large international cohort, both physician-diagnosed depression and two simple self-report questions about feeling down were associated with more deaths and more hospital admissions.[[lopes2002]] In a cohort followed with monthly questionnaires, depressive symptoms were associated with missed and shortened treatments, emergency visits, hospital admissions, and death.[[weisbord2014]] In another international study, patients with more depressive symptoms missed more treatments, and missed treatments were in turn associated with higher mortality.[[alsalmi2018]]</p>
<p>These are associations. They do not show that depression causes these outcomes, or that treating it would prevent them. Sicker patients may simply be both more depressed and more likely to die. What they do show is that a patient with low mood is a patient at higher risk. That is reason enough to notice and act.</p>
<p><strong>What treatment trials show.</strong> The trials are few and small, and they do not all point the same way. Each measured depression scores on a questionnaire, which is a symptom measure. None was designed to show an effect on hospital admissions or survival.</p>
<div class="table-wrap"><table><thead><tr><th>Trial</th><th>Who</th><th>Comparison</th><th>Main finding</th></tr></thead><tbody>
<tr><td>Chairside cognitive behavioral therapy[[cukor2014]]</td><td>Patients on HD with depressive symptoms; 59 completed</td><td>Cognitive behavioral therapy delivered during treatment for 3 months versus a waiting list</td><td>Larger fall in depression scores, better quality of life, and lower fluid gains between sessions with therapy</td></tr>
<tr><td>Sertraline versus placebo feasibility trial (United Kingdom)[[friedli2017]]</td><td>Patients on HD with major depression; 30 randomized</td><td>Sertraline versus placebo for 6 months</td><td>Depression scores improved in both groups with no difference between them; more dropouts from side effects with sertraline. Too small to be conclusive.</td></tr>
<tr><td>CAST[[cast2017]]</td><td>Patients with CKD stages 3 to 5 <em>not</em> on dialysis, with major depression; 201 randomized</td><td>Sertraline versus placebo for 12 weeks</td><td>No difference in depressive symptoms; more nausea, vomiting, and diarrhea with sertraline</td></tr>
<tr><td>ASCEND[[ascend2019]]</td><td>Patients on HD with depressive symptoms; 120 in the treatment phase</td><td>Cognitive behavioral therapy delivered in the dialysis facility versus sertraline for 12 weeks</td><td>Depression scores modestly lower with sertraline than with therapy; more adverse events with sertraline. There was no untreated comparison group.</td></tr>
</tbody></table></div>
<p>ASCEND also tested whether a structured &ldquo;engagement interview&rdquo; would make patients more willing to start treatment. About two-thirds started treatment whether or not they had the interview.[[ascend2019]] In plain terms: talking therapy and medicine both have some evidence in dialysis patients. Neither is a sure cure. The side effects of medicine are real. The choice between them belongs to the patient, with the physician or mental health professional. Your contribution is to make sure the question is asked and the referral is made.</p>
<p><strong>Screening tools.</strong> Several validated questionnaires are used in dialysis units, including the Patient Health Questionnaire (nine-item), the Beck Depression Inventory (second edition), and, for anxiety, the Generalized Anxiety Disorder scale (seven-item). The screening section below describes how to use them. A score is a screen, not a diagnosis. Thresholds and how often to screen come from unit policy and the instrument&rsquo;s validated version.</p>
<p><strong>What remains uncertain.</strong> Which patients benefit most from which treatment. Whether treatment changes hospital admissions or survival. How well screening tools perform in Filipino languages and settings. How best to deliver talking therapy where mental health professionals are scarce.</p>
<p><strong>Low mood marks a patient at higher risk, whatever its cause. Notice it, ask about it, and pass it on the same day.</strong></p>
"""},
        {"id": "bedside", "nav": "At the chair", "tag": "Clinical application", "h2": "The nurse&rsquo;s role: notice, ask, listen, screen, report, refer",
         "html": """
<p>You do not diagnose depression or prescribe psychiatric medicines. Your role is narrower, and it comes up far more often: to notice, to ask, to screen when policy says so, to record, to report, and to make sure a referral actually happens.</p>
<p><strong>Notice.</strong> Changes worth noticing: a patient who stops talking with neighbors in the next chair, arrives late or leaves early, misses sessions, stops keeping the fluid limit after months of control, neglects grooming, eats less, sleeps through every session, or becomes irritable with staff. Listen for phrases such as &ldquo;Pagod na ako&rdquo; (&ldquo;I am tired&rdquo;) or &ldquo;Wala na akong silbi&rdquo; (&ldquo;I am useless now&rdquo;). Any one of these may have a physical cause. Several together are a reason to ask.</p>
<p><strong>Ask, in private, and listen.</strong> Choose a quiet moment, ideally early in the session when the patient is most alert, and lower your voice. The dialysis floor is not private. Open questions work better than closed ones:</p>
<ul>
<li>&ldquo;How have you been coping with dialysis lately?&rdquo;</li>
<li>&ldquo;You seem quieter than usual. What has been happening at home?&rdquo;</li>
<li>&ldquo;How are you sleeping? How is your appetite?&rdquo;</li>
<li>&ldquo;Many patients feel discouraged at times. Has that happened to you?&rdquo;</li>
</ul>
<p>Then listen without hurrying to reassure. &ldquo;Be strong&rdquo; or &ldquo;Just pray&rdquo; can close a conversation the patient needed to have. Reflect what you heard (&ldquo;It sounds like losing your job has been the hardest part&rdquo;), and ask what would help.</p>
<p><strong>Screen per unit policy.</strong> If your unit uses a screening questionnaire, give it as the policy describes, in a language the patient reads well, with privacy, and record the score. Do not screen a patient who is drowsy, confused, or hypotensive until that is addressed.</p>
<p><strong>Document and report.</strong> Record what the patient said in their own words, what you observed, any score, and whom you told. Report a positive screen or a concerning change to the nephrologist the same day, using SBAR (Situation, Background, Assessment, Recommendation). Any mention of death, self-harm, or not wanting to live is handled at once, as the crisis section below describes.</p>
<p><strong>Refer, and follow up.</strong> Depending on what your unit has, referral may go to the nephrologist for medical review, a psychiatrist or psychologist, the social worker for money, transport, or work problems, a dietitian, a chaplain or the patient&rsquo;s own faith leader, or a peer-support group. A referral that is never completed helps no one. At the next session, ask whether the appointment happened.</p>
<p><strong>Involve the family, with consent.</strong> Families often notice change first, and they carry much of the load. Ask the patient whether, and how much, you may share with them. Respect a refusal, except in immediate danger as facility policy defines it (Module 12 covers confidentiality).</p>
<p><strong>Look after yourself.</strong> Caring for people with a chronic, sometimes fatal illness, for years, is demanding. Grief when a long-term patient dies, frustration with patients who do not follow advice, and exhaustion are common. They are not signs of weakness. Talk with colleagues, use debriefing after difficult events, take your leave, and seek help through the facility or your own physician if your mood or sleep suffers. A nurse who is depleted notices less.</p>
<p><strong>Notice, ask, record, report, and check at the next session that the referral happened. A question asked and then dropped is not care.</strong></p>
"""},
    ],
    "case": {
        "title": "Shortened sessions and short temper",
        "html": """
<p>Mr. Ramon Bautista, 47, drove a tricycle in Bulacan until eight months ago, when he started HD. He has diabetes and takes insulin. For the past four weeks he has asked to come off 45 minutes early at most sessions, and he missed one session entirely. His fluid gains between sessions have risen. Last Thursday he snapped at Ms. Carmela Ocampo, the nurse who asked about his weight. Today he refused to let the technician take his BP.</p>
<p>You are his nurse today. He tells you he sleeps about three hours a night because his legs &ldquo;cannot keep still.&rdquo; He now spends the day at home while his wife works. Near the end of the session, while you are adjusting his lines, he says quietly: &ldquo;Sometimes I think my family would be better off without me.&rdquo;</p>
""",
        "acte": {
            "Assess": "Stay with him and give him your full attention. Check BP and blood glucose now, because low blood sugar and low BP can both cause irritability. Ask directly and calmly whether he has had thoughts of ending his life. Asking does not plant the idea; it tells him it is safe to talk. Ask about sleep, the restless legs, appetite, what has changed at home, and why he leaves early (symptoms late in the session, cost, transport, or wanting the treatment over). Review his medicines and recent laboratory results, including hemoglobin and iron studies.",
            "Communicate": "Do not leave him alone if he describes thoughts of ending his life; follow the facility's crisis pathway and call the nephrologist immediately. Otherwise report to the nephrologist the same day using SBAR: shortened and missed sessions, rising fluid gains, irritability, severe sleep loss with restless legs, his statement about his family, and your assessment. With his consent, involve the social worker and, if he agrees, his wife.",
            "Teach": "Tell him that what he is feeling is common in people on dialysis, that it has causes that can be looked into, and that help exists. Explain that restless legs and poor sleep can often be improved and should be reviewed by the doctor. Explain plainly, without blame, what shortened sessions do to his body and how he can tell the team when the end of a session becomes hard to tolerate.",
            "Escalate": "Escalate immediately per facility policy if he describes thoughts of ending his life, a plan, or access to means, if he cannot agree to stay safe, or if he becomes confused or drowsy. Escalate to the nephrologist if he misses another session or leaves against advice, so the reasons can be addressed with the team rather than on the unit floor.",
        },
        "task": "Write the session note: his words quoted exactly, BP and glucose, what you asked and his answers, the screening score if the unit policy called for one, whom you informed and when, the crisis pathway steps taken if any, consent given or refused for family involvement, the referrals requested, and the plan for follow-up at the next session.",
    },
    "quiz": [
        {"stem": "A 72-year-old man on HD, normally talkative, is drowsy and confused this morning. His daughter says he was &ldquo;not himself&rdquo; last night and was fine the day before. He started a new medicine for nerve pain three days ago. What is the most appropriate interpretation and nursing action?",
         "options": [
             ("Probable depression; give the unit&rsquo;s mood questionnaire and refer to psychiatry", False, "Depression develops over weeks and does not disturb alertness. A drowsy or confused patient is not screened for mood until the confusion is explained."),
             ("Probable delirium; check BP, blood glucose, oxygen, and temperature, and report immediately", True, "A sudden change in alertness and attention over hours to days is delirium until proven otherwise. A new medicine cleared by the kidney is a likely cause, but infection, low BP, and low blood sugar must be checked."),
             ("Probable dementia; teach the daughter about memory aids", False, "Dementia progresses over months to years. A change since yesterday is not dementia, although the two can coexist."),
             ("Probable tiredness from yesterday&rsquo;s session; let him sleep during treatment", False, "Letting a newly confused patient sleep can miss low blood sugar, infection, stroke, or drug accumulation."),
         ],
         "objective": "Explain the biological links between kidney failure, the dialysis session, and changes in mood, thinking, sleep, and behavior, and distinguish delirium from depression and dementia.",
         "sources": ["anna7"], "flag": "Medicine review and dose changes are the physician&rsquo;s and pharmacist&rsquo;s decision."},
        {"stem": "A patient scores in the depression range on a self-report questionnaire. Her main complaints are fatigue, poor sleep, and poor appetite; her hemoglobin has fallen and she missed two sessions last month. Why should the result be interpreted with care?",
         "options": [
             ("Self-report questionnaires are not valid in dialysis patients and should not be used", False, "Validated questionnaires are useful screens in dialysis units; they are not diagnoses."),
             ("Fatigue, poor sleep, and poor appetite can come from kidney failure, anemia, and underdialysis as well as depression, so scales may overestimate depression", True, "Interview-based depression is less common in dialysis patients than scale-based depressive symptoms, partly because physical symptoms overlap. A positive screen is reported for clinical assessment, and the physical causes are reviewed too."),
             ("A positive score means she has major depression and needs an antidepressant", False, "A screen is not a diagnosis, and the nurse does not start psychiatric medicines."),
             ("The score is likely falsely high only because she missed sessions, so it can be ignored", False, "A positive screen is never ignored; missed sessions may themselves be associated with depression."),
         ],
         "objective": "Summarize, with calibrated language, what is known about depression in hemodialysis: how common it is, what it is associated with, and what treatment trials have and have not shown.",
         "sources": ["palmer2013"], "flag": ""},
        {"stem": "A colleague says, &ldquo;Studies show depression kills dialysis patients, so treating it will make them live longer.&rdquo; Which response best reflects the evidence?",
         "options": [
             ("Correct: trials show antidepressants reduce mortality in dialysis patients", False, "No trial in this module showed a survival benefit from treating depression."),
             ("Incorrect: depression has no relationship with outcomes on dialysis", False, "Depressive symptoms are consistently associated with higher mortality and hospital admission in observational studies."),
             ("Partly correct: depressive symptoms are associated with higher mortality and more hospital admissions, but it is not proven that treating depression improves survival", True, "Observational associations do not prove cause, and treatment trials have measured depression scores, not survival. Low mood still marks a patient at higher risk who deserves attention."),
             ("Partly correct: only physician-diagnosed depression matters; patient self-reports do not", False, "In a large international study, two simple self-report questions were associated with mortality and hospital admission, just as physician diagnosis was."),
         ],
         "objective": "Summarize, with calibrated language, what is known about depression in hemodialysis: how common it is, what it is associated with, and what treatment trials have and have not shown.",
         "sources": ["farrokhi2014", "lopes2002"], "flag": ""},
        {"stem": "Which statement accurately describes the ASCEND trial in patients on HD with depressive symptoms?",
         "options": [
             ("Cognitive behavioral therapy was clearly better than sertraline and had fewer side effects", False, "Depression scores at 12 weeks were modestly lower with sertraline, although adverse events were more frequent with sertraline."),
             ("Sertraline produced modestly lower depression scores than cognitive behavioral therapy at 12 weeks, with more adverse events; there was no untreated comparison", True, "That is the trial&rsquo;s main result and its key limitation. Both treatments are options, and the choice is made by the patient with the prescriber."),
             ("Sertraline was no better than placebo", False, "That describes the smaller United Kingdom feasibility trial and the CAST trial in CKD not on dialysis, not ASCEND, which had no placebo group."),
             ("An engagement interview doubled the number of patients who started treatment", False, "About two-thirds started treatment with or without the interview."),
         ],
         "objective": "Summarize, with calibrated language, what is known about depression in hemodialysis: how common it is, what it is associated with, and what treatment trials have and have not shown.",
         "sources": ["ascend2019"], "flag": ""},
        {"stem": "After telling you he has felt hopeless for weeks, a patient asks you not to tell his wife or the doctor. He denies any thoughts of death or self-harm. What is the best response?",
         "options": [
             ("Promise to keep it between the two of you, so that he keeps trusting you", False, "Information needed for his care is shared with the treating team. Promising secrecy you cannot keep damages trust later."),
             ("Tell his wife at once, because families have a right to know", False, "An adult patient decides what is shared with family, except in immediate danger as defined by facility policy."),
             ("Explain that you will share it with the treating team so he can get help, respect his wish about his wife for now, and ask whether he would let her be involved later", True, "The treating team is part of his care; family involvement needs his consent. If he later describes thoughts of death or self-harm, the facility&rsquo;s crisis pathway applies."),
             ("Record nothing, because he denied thoughts of self-harm", False, "Weeks of hopelessness are documented and reported even without thoughts of self-harm."),
         ],
         "objective": "Apply the nurse's role in mental health at the chair: notice, ask, listen, screen per unit policy, document, refer, involve the family with consent, and look after yourself.",
         "sources": ["ra10173"], "flag": "Limits of confidentiality in imminent danger follow facility policy and Philippine law."},
    ],
    "reflect": "Think of a patient in your unit whose mood or behavior changed. What did the team first assume the cause was, how long did it take for someone to ask the patient directly, and what was found when they did?",
    "practice": {
        "intro": "With a preceptor, over several sessions, observe and then practice the nurse's part in mental health care at the chair.",
        "items": [
            "Asks a patient open questions about mood, coping, sleep, and appetite in private during a routine session, and documents the answers in the patient's words.",
            "Gives the unit's mood or anxiety screening questionnaire as policy directs, records the score, and reports a positive screen to the nephrologist the same day using SBAR.",
            "Responds to a new change in alertness or behavior by checking BP and blood glucose first, then reporting.",
            "Reviews a patient's medicine list with the pharmacist or physician for medicines that can cause drowsiness or confusion in kidney failure, and records the outcome.",
            "Teaches one sleep or memory-support strategy using teach-back, with a family member present if the patient consents.",
            "Locates the facility's crisis pathway and referral contacts, and walks the preceptor through what to do if a patient describes thoughts of ending their life.",
        ],
    },
    "readings": [
        ["ckd-mental-health-sleep.html", "Depression, anxiety, cognitive change, insomnia, and restless legs in kidney disease, for patients and clinicians."],
        ["kidney-brain-axis-cognitive-dysfunction-ckd.html", "Why thinking and memory change in kidney failure, when confusion is an emergency, and which causes are reversible."],
        ["post-dialysis-fatigue.html", "The mechanisms behind exhaustion after treatment and what helps."],
        ["caregiver-guide-ckd.html", "Practical support for Filipino family caregivers, including caregiver strain."],
        ["advance-care-planning-dialysis.html", "Documenting values and care wishes, in the Filipino context."],
        ["symptom-checker.html", "A patient-facing tool for deciding when symptoms need urgent care."],
    ],
    "calcs": ["calc-cognitive-screen-ckd.html", "calc-cognitive-score-trend.html", "calc-frailty-assessment.html", "calc-exercise-hr-zones.html"],
    "external": [],
    "terms": [
        ("Adaptation", "The ongoing process by which a person and family rebuild a workable life around a chronic illness and its treatment."),
        ("Delirium", "A sudden, fluctuating disturbance of attention and alertness caused by a physical problem; a medical emergency until explained."),
        ("Depression (major depressive disorder)", "Persistent low mood or loss of interest, with other symptoms, most days for at least two weeks; diagnosed by a clinician, not by a screening score."),
        ("Dementia (major cognitive impairment)", "A gradual decline in memory and thinking that interferes with daily life."),
        ("Screening questionnaire", "A validated set of questions that identifies people who need further assessment; a positive result is not a diagnosis."),
        ("Cognitive behavioral therapy", "A structured talking therapy that helps a person recognize and change unhelpful patterns of thought and behavior."),
        ("Association", "A statistical link between two things that does not by itself show that one causes the other."),
    ],
    "image": {"file": "renal-nursing-14-living-well",
              "alt": "A dialysis nurse sits at eye level beside a middle-aged Filipino patient during treatment, listening attentively while a family member sits nearby.",
              "purpose": "Show mental health care in the dialysis unit as attentive, private, unhurried conversation at the chair.",
              "scene": "", "focal": "", "setting": "", "details": "", "exclusions": "", "archetype": "", "reviewer": ""},
    "flags": [
        "Module-wide: content on depression, anxiety, cognition, and suicide risk needs review by a psychiatrist or clinical psychologist with dialysis experience, and by the unit's medical director, before release.",
        "Physiology table: mechanisms are described from general nephrology and neuropsychiatry knowledge without a single cited source; the white-matter association with falls in blood pressure during treatment is stated as an imaging association, not as proven cause. Consider adding a review reference.",
        "Evidence table: trial results were taken from the PubMed abstracts (Cukor 2014, Friedli 2017, Hedayati 2017 [CAST], Mehrotra 2019 [ASCEND]). ASCEND was published in Annals of Internal Medicine, not JAMA. CAST enrolled patients with CKD not on dialysis.",
        "Anxiety prevalence is stated qualitatively only; no verified source was used for a number.",
        "Screening instruments are named without cut-off scores; thresholds, intervals, and validated Filipino-language versions must come from the unit policy and the instrument's licensed or validated version.",
        "Case: suicide-risk wording follows general safe-messaging practice; confirm against the facility's crisis pathway.",
    ],
    "crosswalk": {
        "ph": "Psychological adaptation, mental health, and long-term wellbeing of HD patients in Philippine units; PSN 2024 standards for patient education and support; RA 10173 (confidentiality)",
        "anna": "Psychosocial aspects of kidney disease; care of the patient with cognitive impairment; patient and family education",
        "edtna": "Psychosocial care and quality of life; patient and family support",
        "nncc": "Psychosocial care of the patient with kidney disease; hemodialysis",
    },
}
