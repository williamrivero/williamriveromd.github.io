# -*- coding: utf-8 -*-
# Module 16 (core): supportive, palliative, and end-of-life kidney care.
# Base sections: model (supportive care alongside every treatment), physiology (symptom mechanisms; what happens
# when dialysis stops), evidence (KDIGO 2015 conference, symptom tools, conservative care, stopping dialysis), bedside.
# m16_x.py adds "symptoms-pc", "acp", "withdrawal", "last-days", and "grief" after "bedside".
# Cross-references: Module 5 (treatment choices, conservative kidney management, advance care planning introduced),
# Module 11 (older adults), Module 14 (mental health, crisis section, symptom burden, living well).
MODULE = {
    "sub": "Supportive care runs alongside every kidney treatment, not only at the end of life: why symptoms are so common in kidney failure, how to assess and relieve them, how to plan ahead with patients and families, what happens when dialysis stops, and how nurses care for the dying, the bereaved, and themselves.",
    "desc": "Module 16 of the Nephrology Nursing & Hemodialysis self-study series: kidney supportive and palliative care for registered nurses, covering symptom mechanisms and assessment, comfort measures, advance care planning in the Filipino family and faith context, requests to stop dialysis, care in the last days of life, and bereavement and staff grief.",
    "keywords": "kidney supportive care nursing, renal palliative care nurse, dialysis withdrawal nursing, stopping dialysis end of life, IPOS-Renal, ESAS-r Renal symptom assessment, uremic pruritus nursing, advance care planning dialysis Philippines, conservative kidney management, end-of-life care hemodialysis, bereavement dialysis nurses",
    "objectives": [
        "Explain why supportive care runs alongside every kidney treatment, and how it differs from care in the last days of life.",
        "Relate the common symptoms of kidney failure to their mechanisms, and describe what happens in the body when dialysis stops.",
        "Name validated symptom-assessment tools and summarize, in calibrated language, what studies show about conservative care and stopping dialysis.",
        "Carry out the nurse&rsquo;s role in supportive care: ask routinely, assess, comfort, document, report, and refer.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Mental model", "h2": "Two tracks that run side by side",
         "html": """
<p>Many nurses picture palliative care as a door at the end of a corridor. First the patient receives &ldquo;active&rdquo; treatment. Only when that fails does comfort care begin. In kidney care this picture is wrong, and it costs patients months of suffering that could have been eased.</p>
<p>A better picture is two railway tracks that run side by side for the whole journey. One track is disease-directed treatment: slowing chronic kidney disease (CKD), then hemodialysis (HD), peritoneal dialysis (PD), or a transplant. The other is <strong>supportive care</strong>: relieving symptoms; attending to mood, sleep, family strain, money, faith, and meaning; and planning ahead for the time when the person can no longer speak for themselves. The second track starts at diagnosis, not at the end.</p>
<p>The picture has a limit. Real tracks never touch, and these do all the time. The same session that removes fluid can relieve breathlessness. A change to the dialysis prescription can ease cramps and itch. The two tracks are not two teams. They are two questions the same team asks at every visit: what is the disease doing, and how is this person living with it?</p>
<p>Over time the balance shifts. Early on, most effort goes to disease-directed treatment, with supportive care in the background. For a frail patient with a heavy burden of illness, the balance may tilt toward comfort and function. For some, the disease-directed track ends. They choose conservative kidney management without dialysis (Module 5), or they decide to stop dialysis. Then supportive care becomes all of care, and in the last days it becomes <strong>end-of-life care</strong>.</p>
<p>Three terms are used loosely. Fix their meaning for this module:</p>
<ul>
<li><strong>Supportive care</strong> (kidney supportive care): attention to symptoms; psychological, social, and spiritual needs; advance care planning; and family support, alongside or instead of dialysis. Module 14 introduced it for patients living well on HD.</li>
<li><strong>Palliative care</strong>: the same approach delivered by, or with, a specialist team when needs are complex. It is not limited to the dying.</li>
<li><strong>End-of-life care</strong>: care in the last weeks and days of life, including care of the family after death.</li>
</ul>
<p>Most of your patients will live for years on dialysis, and most of their symptoms can be eased. A few will reach a point where dialysis no longer serves them. Your work is to ask about suffering early and routinely, so that relief comes in time, and so that no one reaches the end without having been asked what matters to them.</p>
<p>You already work on both tracks, often without naming the second. Asking about itch while you cannulate, noticing that a patient has stopped joking with the others, learning which daughter makes the decisions: all of this is supportive care. This module makes that work deliberate.</p>
<p><strong>At every session, ask two questions: what is the disease doing, and how is this person living with it?</strong></p>
"""},
        {"id": "physiology", "nav": "Symptom physiology", "tag": "Physiology in depth", "h2": "Why kidney failure causes so many symptoms, and what happens when dialysis stops",
         "html": """
<p>The kidneys do far more than make urine. They clear waste products and many medicines. They keep sodium, potassium, water, and acid in balance. They make the hormone that drives red-cell production, and they activate vitamin D. When they fail, each lost function produces its own symptoms. Dialysis, done for about 12 hours a week, replaces only part of what healthy kidneys do around the clock. That is why the symptom burden stays high even in well-dialyzed patients.</p>
<div class="table-wrap"><table><thead><tr><th>Symptom</th><th>Main mechanisms</th><th>What you may notice</th></tr></thead><tbody>
<tr><td>Fatigue and weakness</td><td>Anemia lowers oxygen delivery to muscle and brain. Retained uremic waste products and chronic inflammation may produce &ldquo;sickness behavior.&rdquo; Muscle wasting, poor sleep, low mood, and the fluid and blood-pressure shifts of each session add to it</td><td>Hemoglobin trend, recovery time after dialysis, sleep, mood, falls in blood pressure during sessions</td></tr>
<tr><td>Itch (uremic pruritus)</td><td>Several mechanisms act together: dry skin, high phosphate and calcium&ndash;phosphate imbalance, immune and inflammatory changes in the skin, and an imbalance in the body&rsquo;s own opioid-signaling system that may make the itch pathway overactive. Histamine plays a smaller part than in allergic itch</td><td>Scratch marks, broken or thickened skin, disturbed sleep, phosphate results, missed or shortened sessions</td></tr>
<tr><td>Breathlessness</td><td>Fluid retained between sessions moves into the lungs. Anemia means each breath delivers less oxygen. Metabolic acidosis drives faster, deeper breathing. Heart disease is common. Anxiety amplifies the sensation</td><td>Weight gain since the last session, swelling, crackles, oxygen saturation, the position the patient prefers, panic</td></tr>
<tr><td>Pain</td><td>Bone and mineral disease; nerve damage from diabetes or uremia (burning, tingling feet); poor circulation and leg ulcers; joint and muscle pain; repeated cannulation; rarely, painful skin lesions from calcified small vessels</td><td>Site, character (aching, burning, shooting), timing, effect on sleep and walking, wounds</td></tr>
<tr><td>Nausea and poor appetite</td><td>Retained waste products stimulate the brain&rsquo;s vomiting center. Slow stomach emptying in diabetes. Constipation from fluid limits, iron, phosphate binders, and inactivity. Medicines that accumulate</td><td>Pattern in relation to sessions and meals, bowel habit, weight and muscle loss, taste changes</td></tr>
<tr><td>Restlessness and confusion</td><td>Restless legs, often linked to iron deficiency. Delirium from uremia, infection, low oxygen, low glucose, or medicines the failed kidneys can no longer clear</td><td>Timing (evening leg discomfort versus fluctuating attention), new medicines, fever, glucose, bladder and bowels</td></tr>
<tr><td>Low mood and anxiety</td><td>Loss of role, income, and independence. Inflammation and uremia may act on the brain. Poor sleep. Uncertainty about the future (Module 14)</td><td>Withdrawal from others, irritability, hopelessness, screening scores</td></tr>
</tbody></table></div>
<p><strong>The pharmacology trap.</strong> Many medicines, and the active breakdown products of some, are normally cleared by the kidneys. In kidney failure they build up over days. They can cause drowsiness, confusion, twitching, slowed breathing, or falls. So a symptom can be caused or worsened by the very medicine given to relieve another. That is why the physician chooses and doses every symptom medicine with kidney function in mind, and why you watch for new side effects after any change.</p>
<p><strong>What happens in the body when dialysis stops.</strong> When regular dialysis ends, the functions it was replacing stop being replaced. How fast changes follow depends mostly on three things: how much kidney function and urine output the person still has, how much they eat and drink, and their other illnesses. The changes that may occur:</p>
<ul>
<li><strong>Waste products accumulate.</strong> As uremic toxins rise, most people become steadily more tired and sleepy, eat and drink less, and spend more of the day asleep. Many drift into a deep sleep before death. Some develop restlessness, confusion, or muscle twitching, which can be treated.</li>
<li><strong>Potassium rises.</strong> High potassium can disturb the heart rhythm. In some patients death comes suddenly from this cause, often during sleep.</li>
<li><strong>Fluid accumulates.</strong> In someone who passes little urine, fluid taken in stays in the body. It can cause swelling and breathlessness. Small sips for comfort and mouth care help more than large drinks.</li>
<li><strong>Acid builds up.</strong> Acidosis can make breathing deeper and faster.</li>
</ul>
<p>Studies give a sense of time, not a prediction for any one person. In a small prospective study in two United States dialysis units, patients lived a mean of 9.6 days after dialysis was stopped.[[cohen1995]] In a larger study of 1,947 patients admitted to hospice after stopping dialysis, mean survival after hospice admission was 7.4 days, ranging from the same day to 40 days. Swelling of the limbs, lower functional status, referral from a hospital, and male sex were associated with shorter survival.[[oconnor2013]] Both studies were observational and from the United States. They describe what happened to those patients, not what will happen to the one in front of you.</p>
<p>What families can be told, honestly and calmly: the time is usually days to a few weeks; it differs from person to person; people who still pass urine may live longer; and the symptoms that do occur can be relieved.</p>
<p><strong>Before you accept a symptom as &ldquo;just the kidneys,&rdquo; ask whether a medicine the kidneys can no longer clear is part of the cause.</strong></p>
"""},
        {"id": "evidence", "nav": "Evidence", "tag": "Evidence", "h2": "What is known about symptom burden, conservative care, and stopping dialysis",
         "html": """
<p><strong>The 2015 international conference on supportive care.</strong> In 2015 Kidney Disease: Improving Global Outcomes (KDIGO) published the executive summary of a Controversies Conference on Supportive Care in CKD. An international group of experts in nephrology, palliative care, research methods, economics, and education reached three conclusions. People with advanced CKD, including those on dialysis, carry a high burden of physical and psychological symptoms. Prognostic and assessment tools are limited. The quality of conservative and palliative care is often poor. The conference set out a roadmap for clinical work and research, and it applied supportive care to patients on dialysis as well as to those managed without it.[[ckm2015]] This is a conference statement, not a graded recommendation. Module 5 used the same conference for its definition of comprehensive conservative care.</p>
<p><strong>How common symptoms are.</strong> A systematic review of 59 studies in patients on dialysis found these weighted mean prevalences: fatigue 71%, itch 55%, constipation 53%, poor appetite 49%, pain 47%, sleep disturbance 44%, anxiety 38%, breathlessness 35%, nausea 33%, restless legs 30%, and depression 27%. Estimates varied widely between studies, because definitions and time frames differed.[[murtagh2007sx]] In 507 Canadian dialysis patients, the mean number of symptoms reported on a modified Edmonton symptom checklist was 7.5. Symptom distress was strongly associated with poorer physical and mental quality of life.[[davison2006]] A small pilot study found that patients with advanced kidney failure reported a symptom burden and quality of life similar to those of patients with terminal cancer.[[saini2006]] It was small, and it shows a comparison, not a cause.</p>
<p><strong>Symptoms are missed.</strong> In the international Dialysis Outcomes and Practice Patterns Study, 69% of medical directors underestimated how common itch was in their own unit. Among patients who were nearly always or always bothered by itching, 17% had not told staff, and 18% were using no treatment.[[rayner2017]] Patients often assume symptoms are an unavoidable part of dialysis. Unless someone asks, they stay silent.</p>
<p><strong>Tools that make asking routine.</strong> Two short questionnaires designed for kidney patients are widely used.</p>
<ul>
<li>The <strong>Edmonton Symptom Assessment System&ndash;revised: Renal</strong> asks the patient to rate the severity of common symptoms, including itch, on a 0 to 10 scale. An earlier modified version was shown to be reliable and valid in dialysis patients.[[davison2006]] The renal version was used in a trial of routine symptom measurement and reporting in hemodialysis units in Alberta, Canada.[[wen2022]]</li>
<li>The renal version of the <strong>Integrated Palliative care Outcome Scale</strong> asks about kidney-related symptoms and also about worry, family anxiety, feeling at peace, information, and practical problems. It has a patient version and a staff version. In 81 patients and 53 nurses in Australia, both versions showed good test&ndash;retest reliability, internal consistency, and agreement with comparable measures.[[raj2018]]</li>
</ul>
<p>Neither tool diagnoses anything. Each turns a vague &ldquo;How are you?&rdquo; into specific answers that can be compared over time and acted on. Unit policy decides which tool, which language version, and how often.</p>
<p><strong>Conservative care compared with dialysis.</strong> There are no randomized trials. In a retrospective study of patients over 75 years old with stage 5 CKD attending planned pre-dialysis clinics, those who chose dialysis lived longer on average than those managed conservatively. The survival advantage was lost in patients with high comorbidity, especially ischemic heart disease.[[murtagh2007surv]] Patients who choose dialysis may differ in many ways from those who do not, so this design cannot separate the effect of dialysis from the effect of who chose it. A systematic review found broadly similar 1-year survival in older patients treated with dialysis or supportive care. It warned that data on supportive care were scarce and open to bias, so the relative benefit could not be estimated with confidence.[[foote2016]]</p>
<p>The honest message for patients: for frail older people with several serious illnesses, dialysis may add little time and much burden; for others it adds years. The decision rests on the person&rsquo;s goals as much as on numbers.</p>
<p><strong>Stopping dialysis.</strong> In a United States study from the early 1990s, about 10% of deaths among patients on long-term dialysis were preceded by a decision to stop.[[cohen1995]] In a prospective study of 131 patients in United States and Canadian clinics who died after stopping dialysis, pain and agitation were the most common symptoms in the last day of life. Terminal care was generally judged satisfactory, and most deaths were considered good.[[cohen2000]] A peaceful death after stopping dialysis is possible. It depends on planned symptom control.</p>
<p><strong>What patients say they want.</strong> In a survey of 584 Canadian patients with stage 4 or 5 CKD, patients said they relied on the kidney team for symptom management, advance care planning, and psychological and spiritual support. Sixty-one percent regretted their decision to start dialysis. More wanted to die at home (36%) or in a hospice (29%) than in hospital (27%). Fewer than 10% had discussed end-of-life care with their nephrologist in the previous year.[[davison2010]] Findings from one Canadian program may not transfer directly to Filipino patients. The gap between what patients need and what they are offered is still a reason to ask.</p>
<p><strong>What remains uncertain.</strong> Philippine data on symptom burden, conservative care, and stopping dialysis are scarce. This module uses figures from United States and other international studies, labeled by source, as working estimates. Which patients gain most from dialysis rather than conservative care, how best to predict prognosis, and which symptom treatments work best in kidney failure are all still being studied. Where evidence is incomplete, the physician&rsquo;s judgment, the patient&rsquo;s goals, and unit policy guide care.</p>
<p><strong>Most of this evidence is observational. It tells you that suffering is common and often missed. It does not tell you which patient should choose which path. That answer comes from the patient.</strong></p>
"""},
        {"id": "bedside", "nav": "Nursing role", "tag": "Clinical application", "h2": "The nurse&rsquo;s role: ask, assess, comfort, document, report, refer",
         "html": """
<p>Supportive care is not a separate job for a separate team. In most Philippine dialysis units it is done by the people already at the chair, or it is not done at all. Your part has six steps.</p>
<ol>
<li><strong>Ask routinely.</strong> Use the unit&rsquo;s symptom questionnaire at the set interval. At every session ask one open question: &ldquo;Anything new or bothering you since last time?&rdquo; Ask specifically about itch, pain, sleep, breathlessness, appetite, and mood. Patients rarely volunteer them.</li>
<li><strong>Assess.</strong> For each symptom, record severity on a 0 to 10 scale, pattern, triggers, effect on sleep and daily life, and what the patient has already tried. Look for the mechanisms in the physiology table: weight gain, low blood pressure during sessions, a high phosphate, a new medicine.</li>
<li><strong>Comfort.</strong> Carry out the non-drug measures within nursing practice: positioning, skin care, a fan for breathlessness, mouth care, warmth, a quiet word, and time. The next section describes them symptom by symptom.</li>
<li><strong>Document.</strong> Record the patient&rsquo;s own words, the scores, what you did, and the response. A symptom that is not written down is not handed over.</li>
<li><strong>Report.</strong> Tell the physician the severity, the trend, and the effect on the patient&rsquo;s life, using SBAR (Situation, Background, Assessment, Recommendation). You do not prescribe, start, stop, or change symptom medicines. You give them as ordered, watch for benefit and side effects, hold and notify per order or protocol, and report again if relief is not achieved.</li>
<li><strong>Refer.</strong> With the physician&rsquo;s agreement and the patient&rsquo;s consent, involve the social worker for cost and transport, the dietitian for appetite and weight loss, a psychologist or psychiatrist for mood, a chaplain or the patient&rsquo;s own faith leader for spiritual distress, and a palliative care team where one exists.</li>
</ol>
<p><strong>Signs that a fuller conversation is needed.</strong> Repeated hospital admissions. Steady loss of weight or function. More time spent in bed. A new serious illness such as cancer or a major amputation. Symptoms that are not controlled. A patient or relative who says, in any words, that dialysis no longer seems worth it. You do not lead the prognosis discussion. You can notice these signs, report them, and ask the physician whether it is time to talk about goals.</p>
<p><strong>Stay within your role, and stay present.</strong> Questions such as &ldquo;How long do I have?&rdquo; or &ldquo;Should I stop?&rdquo; are answered by the physician with the patient and family. You can still respond: &ldquo;That is an important question. Can you tell me what is making you think about it? I will make sure the doctor hears it, and I would like to be there when you talk.&rdquo; Not changing the subject is itself care.</p>
<p><strong>A symptom you did not ask about is a symptom nobody will treat. Ask, write it down, and pass it on.</strong></p>
"""},
    ],
    "case": {
        "title": "&ldquo;Ayoko na&rdquo; at the chair",
        "html": """
<p>Lola Remedios Santiago, 79, has been on HD three times a week for three years for diabetic kidney disease. She also has heart failure and had two hospital admissions in the last four months for fluid overload. Her daughter works abroad as a nurse. Her son Arnel brings her to every session and pays for her medicines.</p>
<p>It is the start of her Monday session. She has gained 3.1 kg since Friday and is sitting bolt upright. Her forearms are covered in scratch marks. You are the nurse at her chair, with the charge nurse, Ms. Weng Cabrera, two chairs away. While you tape her needles she says quietly, &ldquo;Ayoko na, anak. I don&rsquo;t want this anymore. I can&rsquo;t sleep, I itch all night, and I can&rsquo;t breathe lying down.&rdquo; Her son, overhearing, says, &ldquo;Don&rsquo;t listen to her, Nurse. She is just tired.&rdquo;</p>
""",
        "acte": {
            "Assess": "Check breathing, oxygen saturation, blood pressure, lung sounds, and swelling now. Fluid overload is a treatable cause of both breathlessness and distress. Rate her itch, breathlessness, and sleep with the unit&rsquo;s symptom tool, and check her phosphate trend and medicine list. In private, ask what she means by &ldquo;ayoko na&rdquo;: tired of the symptoms, of dialysis, of being a burden, or of living. Screen her mood with the unit&rsquo;s tool and, as Module 14 teaches, ask directly whether she has thoughts of ending her life.",
            "Communicate": "Report to the nephrologist today using SBAR: the weight gain and breathlessness lying flat, uncontrolled itch and insomnia, her statement and what she said when you explored it, and the screening results. Ask for review of her fluid removal and target weight, her itch and sleep, and whether a family meeting about goals of care can be arranged, including her daughter by video call if Lola Remedios agrees.",
            "Teach": "Tell her that her words have been heard and will be passed to the doctor, and that relief of itch and breathlessness is possible whether or not she continues dialysis. Show her and her son skin care for itch. Acknowledge her son&rsquo;s worry gently, and explain that listening to what she is saying is how the team can help her feel better.",
            "Escalate": "Act immediately if her breathing worsens, her oxygen saturation falls, or chest pain develops. If she describes current thoughts of ending her life, stay with her and follow the crisis pathway in Module 14. A considered request to stop dialysis is not settled at the chair. It goes to the nephrologist and the team, as the stopping-dialysis section explains.",
        },
        "task": "Write the session note: her exact words, your respiratory assessment and vital signs, the symptom scores, the mood screening result and her answer to the direct question about self-harm, whom you informed and when, what was decided, and the plan for a family meeting.",
    },
    "quiz": [
        {"stem": "A nurse new to the dialysis unit says, &ldquo;Palliative care is for patients who have stopped dialysis. Our patients are still on treatment.&rdquo; Which reply best reflects kidney supportive care?",
         "options": [
             ("That is right: comfort care begins only when disease-directed treatment ends", False, "This is the &ldquo;door at the end of the corridor&rdquo; model. Waiting until treatment ends leaves years of symptoms unaddressed."),
             ("Supportive care runs alongside dialysis from the start, addressing symptoms, mood, planning, and family needs, and the balance shifts as needs change", True, "Supportive care is a second track that runs alongside disease-directed treatment for the whole journey. The KDIGO conference applied it to patients on dialysis as well as to those managed without it."),
             ("Supportive care is a specialist service, so dialysis nurses do not need to be involved", False, "Most supportive care in dialysis units is delivered by the staff already at the chair. Specialist palliative teams are for complex needs."),
             ("Supportive care means starting comfort medicines in every patient on dialysis", False, "Supportive care is an approach of asking, assessing, and relieving. The physician prescribes medicines only when they are needed."),
         ],
         "objective": "Explain why supportive care runs alongside every kidney treatment, and how it differs from care in the last days of life.",
         "sources": ["ckm2015"], "flag": ""},
        {"stem": "A patient on HD says the itch is worst at night and keeps him awake. His forearms show scratch marks and dry, scaly skin. Which explanation of his itch is most accurate?",
         "options": [
             ("It is an allergy to the dialyzer, so antihistamines alone will cure it", False, "Histamine plays only a small part in itch from kidney failure. A dialyzer reaction occurs early in the session and looks different."),
             ("It comes from several mechanisms together, including dry skin, mineral imbalance, and changes in immune and nerve signaling", True, "Itch in kidney failure is multifactorial. Dry skin, high phosphate, inflammation, and an imbalance in opioid signaling may all contribute, so several measures are combined."),
             ("It is psychological, and reassurance is the main treatment", False, "Itch in kidney failure has physical mechanisms. It is a recognized symptom that deserves assessment and treatment."),
             ("It shows that his access is infected", False, "Generalized itch with dry skin does not point to access infection. Local redness, warmth, pus, or fever would."),
         ],
         "objective": "Relate the common symptoms of kidney failure to their mechanisms, and describe what happens in the body when dialysis stops.",
         "sources": ["rayner2017"], "flag": ""},
        {"stem": "The daughter of a patient who has decided with his physician to stop dialysis asks, &ldquo;What will happen to him now?&rdquo; Which answer is accurate and calm?",
         "options": [
             ("He will die within 24 hours, in pain", False, "This is inaccurate and frightening. The time is usually days to a few weeks, and the symptoms that occur can be relieved."),
             ("Nothing will change, because his body has adapted to kidney failure", False, "When dialysis stops, waste products, potassium, fluid, and acid accumulate. Families need honest preparation."),
             ("He will most likely become more tired and sleepy over days to a few weeks; the time varies, and the team will treat any breathlessness, restlessness, or itch", True, "Rising waste products usually bring increasing drowsiness. Observational studies report a mean survival of about one to two weeks, with wide variation. Planned symptom control makes a peaceful death more likely."),
             ("Only the doctor can talk about that, so I cannot say anything", False, "The physician leads the prognosis discussion. You can still give general, honest information about what to expect and make sure the family&rsquo;s questions reach the physician."),
         ],
         "objective": "Relate the common symptoms of kidney failure to their mechanisms, and describe what happens in the body when dialysis stops.",
         "sources": ["cohen1995", "oconnor2013", "cohen2000"], "flag": "The physician leads prognosis discussions; the nurse reinforces general information."},
        {"stem": "Your unit wants a short, validated questionnaire that asks kidney patients about symptoms and also about worry, family anxiety, and feeling at peace, with a staff version. Which tool fits best?",
         "options": [
             ("The renal version of the Integrated Palliative care Outcome Scale", True, "It covers kidney symptoms plus emotional and practical concerns, has patient and staff versions, and was found reliable and valid in patients with advanced kidney disease and their nurses."),
             ("The urea reduction ratio", False, "This measures dialysis dose, a surrogate number, not symptoms or concerns."),
             ("A pain scale alone", False, "A pain scale captures one symptom. It misses itch, breathlessness, mood, and practical concerns."),
             ("The Kidney Failure Risk Equation", False, "This predicts progression to kidney failure. It does not assess symptoms."),
         ],
         "objective": "Name validated symptom-assessment tools and summarize, in calibrated language, what studies show about conservative care and stopping dialysis.",
         "sources": ["raj2018"], "flag": "Choice of tool and language version follows unit policy."},
        {"stem": "During a routine symptom review, a patient rates her pain as 7 out of 10, says it keeps her from walking to church, and asks you to give her the ibuprofen her neighbor uses. What should you do?",
         "options": [
             ("Give one dose now and report it afterward", False, "Nurses do not give medicines without an order. Anti-inflammatory pain relievers can harm remaining kidney function, raise potassium, and increase bleeding risk."),
             ("Tell her pain is expected on dialysis and that she should rest more", False, "Pain is common but not something to accept. It should be assessed and reported for treatment."),
             ("Assess the pain&rsquo;s site, character, and effect on her life, explain why that medicine is unsafe in kidney failure, use comfort measures, and report to the physician", True, "Assess, comfort, document, report. The physician chooses pain medicines suited to kidney failure, and you explain the risk of self-medication."),
             ("Refer her to the pharmacist and take no further action", False, "The pharmacist can help, but you still assess, document, and report the pain to the physician."),
         ],
         "objective": "Carry out the nurse&rsquo;s role in supportive care: ask routinely, assess, comfort, document, report, and refer.",
         "sources": ["davison2019"], "flag": ""},
    ],
    "reflect": "Think of a patient in your unit who died in the last year. Looking back, when did their supportive-care needs begin? Who first noticed them? Was there ever a conversation about what mattered most to them before the last admission?",
    "practice": {
        "intro": "With a preceptor experienced in kidney supportive or palliative care, practice the assessment and communication skills of this module with patients who agree to take part.",
        "items": [
            "Administers the unit&rsquo;s symptom questionnaire to a patient, scores it, and reports the highest scores to the physician using SBAR.",
            "Assesses one symptom in depth (severity, pattern, triggers, effect on daily life) and carries out the non-drug comfort measures in the care plan.",
            "Checks a patient&rsquo;s symptom medicines for drowsiness, confusion, twitching, or slowed breathing, and reports concerns.",
            "Observes a family meeting or goals-of-care discussion led by the physician, and documents the decisions and the named surrogate decision-maker per facility policy.",
            "Explains to a family, in calm and plain words, what supportive care offers alongside dialysis.",
            "Takes part in a debriefing after a patient&rsquo;s death in the unit.",
        ],
    },
    "readings": [
        ["advance-care-planning-dialysis.html", "Advance care planning for people on dialysis: starting the conversation and recording wishes."],
        ["symptom-checker.html", "A patient-facing symptom checker that can open a symptom conversation."],
        ["uremic-pruritus-ckd.html", "Itch in kidney disease: mechanisms, skin care, and treatment options."],
        ["pain-management-ckd.html", "Pain in kidney disease and why medicine choice matters."],
        ["caregiver-guide-ckd.html", "Practical and emotional support for family caregivers."],
        ["ckd-mental-health-sleep.html", "Mood, anxiety, and sleep in kidney disease."],
        ["hemodialysis-elderly.html", "Dialysis in older adults, frailty, and treatment decisions."],
        ["post-dialysis-fatigue.html", "Fatigue after dialysis sessions and what can help."],
    ],
    "calcs": [],
    "external": [["KDIGO Controversies Conference on Supportive Care in CKD: executive summary (Kidney International, 2015)", "https://doi.org/10.1038/ki.2015.110"]],
    "terms": [
        ("Kidney supportive care", "Care of symptoms, psychological, social, and spiritual needs, advance care planning, and family support, alongside or instead of dialysis."),
        ("Palliative care", "An approach that relieves suffering and supports quality of life in serious illness; not limited to the last days of life."),
        ("End-of-life care", "Care in the last weeks and days of life, including care of the family after death."),
        ("Symptom burden", "The total number, severity, and distress of the symptoms a person lives with."),
        ("Uremic pruritus", "Itch caused by kidney failure, from several mechanisms acting together."),
        ("Patient-reported outcome measure", "A questionnaire completed by the patient that records what the patient experiences, such as symptom severity."),
        ("Stopping dialysis", "A planned decision by a patient, or a surrogate on the patient&rsquo;s behalf, with the physician, to end regular dialysis and focus on comfort."),
    ],
    "image": {"file": "renal-nursing-16-palliative",
              "alt": "A dialysis nurse sits at eye level beside an older Filipino patient in a reclining chair, holding her hand while a family member listens.",
              "purpose": "Show supportive care as unhurried, present, family-centered nursing at the dialysis chair, not only at the deathbed.",
              "scene": "", "focal": "", "setting": "", "details": "", "exclusions": "", "archetype": "", "reviewer": ""},
    "flags": [
        "Core module on supportive, palliative, and end-of-life kidney care: needs review by a nephrologist with palliative care experience and, where available, a palliative care specialist and a hospital chaplain or pastoral care lead.",
        "Survival after stopping dialysis is stated only from two United States studies (mean 9.6 days in 18 patients, 1995; mean 7.4 days after hospice admission in 1,947 patients, 2013); no Philippine data were found.",
        "The figure that about 10% of deaths of dialysis patients were preceded by stopping dialysis is from a 1995 United States study and may not apply in the Philippines today; it is attributed to its source and era in the text.",
        "Mechanisms of uremic pruritus (opioid-signaling imbalance, immune changes) and of symptoms after stopping dialysis are general physiology described with 'may'; confirm wording with the nephrology reviewer.",
        "Tool names: the text uses the full names 'Edmonton Symptom Assessment System&ndash;revised: Renal' and 'renal version of the Integrated Palliative care Outcome Scale'; the short forms ESAS-r: Renal and IPOS-Renal appear only in keywords. The validation paper calls the renal tool the 'Integrated Palliative Outcome Score'; the developers' usual name is 'Integrated Palliative care Outcome Scale'. Confirm preferred naming.",
        "The 2015 KDIGO conference is labeled in the text as a conference statement, not a graded recommendation.",
        "Case: weight gain of 3.1 kg is illustrative; no fluid-removal targets are stated. Patient surname, son's and charge nurse's names added in the rewrite.",
    ],
    "crosswalk": {
        "ph": "Philippine dialysis nurse training topics: patient and family support, ethics, and care of the dying; hospital palliative care and end-of-life policies",
        "anna": "Supportive and palliative kidney care; symptom management; ethics and advance care planning",
        "edtna": "Psychosocial and supportive care; conservative management; care at the end of life",
        "nncc": "Professional practice: ethics and end-of-life care; patient and family education and support",
    },
}
