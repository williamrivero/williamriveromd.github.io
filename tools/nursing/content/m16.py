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
<p>Many nurses picture palliative care as a door at the end of a corridor: first the patient receives &ldquo;active&rdquo; treatment, and only when that fails does comfort care begin. In kidney care this picture is wrong, and it costs patients months of avoidable suffering.</p>
<p>A better picture is two tracks that run side by side for the whole journey. One track is disease-directed treatment: slowing chronic kidney disease (CKD), then hemodialysis (HD), peritoneal dialysis (PD), or a transplant. The other track is <strong>supportive care</strong>: relieving symptoms, attending to mood, sleep, family strain, money, faith, and meaning, and planning ahead for the time when the person can no longer speak for themselves. The second track starts at diagnosis, not at the end.</p>
<p>Over time the balance between the tracks shifts. Early on, most effort goes to disease-directed treatment, with supportive care in the background. For a frail patient with a heavy burden of illness, the balance may tilt the other way, toward comfort and function. For some, the disease-directed track ends altogether: they choose conservative kidney management without dialysis (Module 5), or they decide to stop dialysis. Then supportive care becomes all of care, and in the last days it becomes <strong>end-of-life care</strong>.</p>
<p>Three terms are used loosely, so it helps to fix their meaning for this module:</p>
<ul>
<li><strong>Supportive care</strong> (kidney supportive care): attention to symptoms, psychological, social, and spiritual needs, advance care planning, and family support, alongside or instead of dialysis. Module 14 introduced it for patients living well on HD.</li>
<li><strong>Palliative care</strong>: the same approach delivered by, or with, a specialist team when needs are complex. It is not limited to the dying.</li>
<li><strong>End-of-life care</strong>: care in the last weeks and days of life, including care of the family after death.</li>
</ul>
<p>The dialysis nurse already works on both tracks, often without naming the second. Asking about itch while cannulating, noticing that a patient has stopped joking with the others, or learning which daughter makes the decisions are all supportive care. This module makes that work deliberate.</p>
"""},
        {"id": "physiology", "nav": "Symptom physiology", "tag": "Physiology in depth", "h2": "Why kidney failure causes so many symptoms, and what happens when dialysis stops",
         "html": """
<p>The kidneys do far more than make urine. They clear waste products and many medicines, keep sodium, potassium, water, and acid in balance, make the hormone that drives red-cell production, and activate vitamin D. When they fail, each lost function produces its own symptoms, and dialysis, done for about 12 hours a week, replaces only part of what healthy kidneys do around the clock. That is why symptom burden stays high even in well-dialyzed patients.</p>
<div class="table-wrap"><table><thead><tr><th>Symptom</th><th>Main mechanisms</th><th>What the nurse can look for</th></tr></thead><tbody>
<tr><td>Fatigue and weakness</td><td>Anemia lowers oxygen delivery to muscle and brain; retained uremic waste products and chronic inflammation may produce &ldquo;sickness behavior&rdquo;; muscle wasting; poor sleep; low mood; the fluid and blood-pressure shifts of each session</td><td>Hemoglobin trend, recovery time after dialysis, sleep, mood, falls in blood pressure during sessions</td></tr>
<tr><td>Itch (uremic pruritus)</td><td>Several mechanisms acting together: dry skin, high phosphate and calcium&ndash;phosphate imbalance, immune and inflammatory changes in the skin, and an imbalance in the body&rsquo;s own opioid-signaling system that may make the itch pathway overactive; histamine plays a smaller part than in allergic itch</td><td>Scratch marks, broken or thickened skin, disturbed sleep, phosphate results, missed or shortened sessions</td></tr>
<tr><td>Breathlessness</td><td>Fluid retained between sessions moves into the lungs; anemia means each breath delivers less oxygen; metabolic acidosis drives faster, deeper breathing; heart disease is common; anxiety amplifies the sensation</td><td>Weight gain since the last session, swelling, crackles, oxygen saturation, the position the patient prefers, panic</td></tr>
<tr><td>Pain</td><td>Bone and mineral disease; nerve damage from diabetes or uremia (burning, tingling feet); poor circulation and leg ulcers; joint and muscle pain; repeated cannulation; rarely, painful skin lesions from calcified small vessels</td><td>Site, character (aching, burning, shooting), timing, effect on sleep and walking, wounds</td></tr>
<tr><td>Nausea and poor appetite</td><td>Retained waste products stimulate the brain&rsquo;s vomiting center; slow stomach emptying in diabetes; constipation from fluid limits, iron, phosphate binders, and inactivity; medicines that accumulate</td><td>Pattern in relation to sessions and meals, bowel habit, weight and muscle loss, taste changes</td></tr>
<tr><td>Restlessness and confusion</td><td>Restless legs (often linked to iron deficiency); delirium from uremia, infection, low oxygen, low glucose, or medicines that the failed kidneys can no longer clear</td><td>Timing (evening leg discomfort versus fluctuating attention), new medicines, fever, glucose, bladder and bowels</td></tr>
<tr><td>Low mood and anxiety</td><td>Loss of role, income, and independence; inflammation and uremia may act on the brain; poor sleep; uncertainty about the future (Module 14)</td><td>Withdrawal from others, irritability, hopelessness, screening scores</td></tr>
</tbody></table></div>
<p><strong>The pharmacology trap.</strong> Many medicines, and the active breakdown products of some, are normally cleared by the kidneys. In kidney failure they can build up over days and cause drowsiness, confusion, twitching, slowed breathing, or falls. A symptom can therefore be caused or worsened by the very medicine given to relieve another. This is why every symptom medicine in kidney failure is chosen and dosed by the physician with kidney function in mind, and why the nurse watches for new side effects after any change.</p>
<p><strong>What happens in the body when dialysis stops.</strong> When regular dialysis ends, the functions it was replacing stop being replaced. How fast changes follow depends mostly on how much kidney function and urine output the person still has, on how much they eat and drink, and on their other illnesses. The changes that may occur are:</p>
<ul>
<li><strong>Waste products accumulate.</strong> As uremic toxins rise, most people become progressively more tired and sleepy, eat and drink less, and spend more of the day asleep. Many drift into a deep sleep before death. Some develop restlessness, confusion, or muscle twitching, which can be treated.</li>
<li><strong>Potassium rises.</strong> High potassium can disturb the heart rhythm, and in some patients death comes suddenly from this cause, often during sleep.</li>
<li><strong>Fluid accumulates.</strong> In someone who passes little urine, fluid taken in stays in the body and can cause swelling and breathlessness. Small sips for comfort and mouth care, rather than large drinks, help.</li>
<li><strong>Acid builds up.</strong> Acidosis can make breathing deeper and faster.</li>
</ul>
<p>Studies give a sense of time, not a prediction for any one person. In a small prospective study in two United States dialysis units, patients lived a mean of 9.6 days after dialysis was stopped.[[cohen1995]] In a larger study of 1,947 patients admitted to hospice after stopping dialysis, mean survival after hospice admission was 7.4 days, with a range from the same day to 40 days; swelling of the limbs, lower functional status, referral from a hospital, and male sex were associated with shorter survival.[[oconnor2013]] Families can be told, honestly and calmly, that the time is usually days to a few weeks, that it differs from person to person, that people who still pass urine may live longer, and that the symptoms which do occur can be relieved.</p>
"""},
        {"id": "evidence", "nav": "Evidence", "tag": "Evidence", "h2": "What is known about symptom burden, conservative care, and stopping dialysis",
         "html": """
<p><strong>The 2015 international conference on supportive care.</strong> In 2015 Kidney Disease: Improving Global Outcomes (KDIGO) published the executive summary of a Controversies Conference on Supportive Care in CKD. An international group of experts in nephrology, palliative care, research methods, economics, and education concluded that people with advanced CKD, including those on dialysis, carry a high burden of physical and psychological symptoms, that prognostic and assessment tools are limited, and that the quality of conservative and palliative care is often poor. The conference set out a roadmap for clinical work and research, and it applied supportive care to patients on dialysis as well as to those managed without it.[[ckm2015]] Module 5 used the same conference for its definition of comprehensive conservative care.</p>
<p><strong>How common symptoms are.</strong> A systematic review of 59 studies in patients on dialysis found these weighted mean prevalences: fatigue 71%, itch 55%, constipation 53%, poor appetite 49%, pain 47%, sleep disturbance 44%, anxiety 38%, breathlessness 35%, nausea 33%, restless legs 30%, and depression 27%; estimates varied widely between studies because definitions and time frames differed.[[murtagh2007sx]] In 507 Canadian dialysis patients, the mean number of symptoms reported on a modified Edmonton symptom checklist was 7.5, and symptom distress was strongly associated with poorer physical and mental quality of life.[[davison2006]] A small pilot study found that patients with advanced kidney failure reported a symptom burden and quality of life similar to those of patients with terminal cancer.[[saini2006]]</p>
<p><strong>Symptoms are missed.</strong> In the international Dialysis Outcomes and Practice Patterns Study, 69% of medical directors underestimated how common itch was in their own unit, and among patients who were nearly always or always bothered by itching, 17% had not told staff about it and 18% were using no treatment.[[rayner2017]] Patients often assume symptoms are an unavoidable part of dialysis. Unless someone asks, they stay silent.</p>
<p><strong>Tools that make asking routine.</strong> Two short questionnaires designed for kidney patients are widely used:</p>
<ul>
<li>The <strong>Edmonton Symptom Assessment System&ndash;revised: Renal</strong> asks the patient to rate the severity of common symptoms, including itch, on a 0 to 10 scale. An earlier modified version was shown to be reliable and valid in dialysis patients,[[davison2006]] and the renal version was used in a trial of routine symptom measurement and reporting in hemodialysis units in Alberta, Canada.[[wen2022]]</li>
<li>The renal version of the <strong>Integrated Palliative care Outcome Scale</strong> asks about kidney-related symptoms and also about worry, family anxiety, feeling at peace, information, and practical problems. It has a patient version and a staff version. In 81 patients and 53 nurses in Australia, both versions showed good test&ndash;retest reliability, internal consistency, and agreement with comparable measures.[[raj2018]]</li>
</ul>
<p>Neither tool diagnoses anything. Each turns a vague &ldquo;How are you?&rdquo; into specific, comparable answers that can be tracked over time and acted on. Which tool, which language version, and how often it is used are decided by unit policy.</p>
<p><strong>Conservative care compared with dialysis.</strong> There are no randomized trials. In a retrospective study of patients over 75 years old with stage 5 CKD attending planned pre-dialysis clinics, those who chose dialysis lived longer on average than those managed conservatively, but this survival advantage was lost in patients with high comorbidity, especially ischemic heart disease.[[murtagh2007surv]] A systematic review found broadly similar 1-year survival in older patients treated with dialysis or supportive care, but warned that data on supportive care were scarce and open to bias, so the relative benefit could not be estimated with confidence.[[foote2016]] The honest message for patients is that, for frail older people with several serious illnesses, dialysis may add little time and much burden, while for others it adds years; the decision rests on the person&rsquo;s goals as much as on numbers.</p>
<p><strong>Stopping dialysis.</strong> In a United States study from the early 1990s, about 10% of deaths among patients on long-term dialysis were preceded by a decision to stop.[[cohen1995]] In a prospective study of 131 patients in United States and Canadian clinics who died after stopping dialysis, pain and agitation were the most common symptoms in the last day of life; terminal care was generally judged satisfactory, and most deaths were considered good.[[cohen2000]] A peaceful death after stopping dialysis is possible, and it depends on planned symptom control.</p>
<p><strong>What patients say they want.</strong> In a survey of 584 Canadian patients with stage 4 or 5 CKD, patients said they relied on the kidney team for symptom management, advance care planning, and psychological and spiritual support; 61% regretted their decision to start dialysis; more wanted to die at home (36%) or in a hospice (29%) than in hospital (27%); and fewer than 10% had discussed end-of-life care with their nephrologist in the previous year.[[davison2010]] Findings from one Canadian program may not transfer directly to Filipino patients, but the gap between what patients need and what they are offered is a reason to ask.</p>
<p><strong>What remains uncertain.</strong> Philippine data on symptom burden, conservative care, and stopping dialysis are scarce, so this module uses figures from United States and other international studies, labeled by source, as working estimates. Which patients gain most from dialysis rather than conservative care, how best to predict prognosis, and which symptom treatments work best in kidney failure are all still being studied. Where evidence is incomplete, the physician&rsquo;s judgment, the patient&rsquo;s goals, and the unit&rsquo;s policy guide care.</p>
"""},
        {"id": "bedside", "nav": "Nursing role", "tag": "Clinical application", "h2": "The nurse&rsquo;s role: ask, assess, comfort, document, report, refer",
         "html": """
<p>Supportive care is not a separate job for a separate team. In most Philippine dialysis units it will be done by the people already at the chair, or it will not be done at all. The nurse&rsquo;s part has six steps.</p>
<ol>
<li><strong>Ask routinely.</strong> Use the unit&rsquo;s symptom questionnaire at the set interval, and at every session ask one open question: &ldquo;Anything new or bothering you since last time?&rdquo; Ask specifically about itch, pain, sleep, breathlessness, appetite, and mood, because patients rarely volunteer them.</li>
<li><strong>Assess.</strong> For each symptom, record severity on a 0 to 10 scale, pattern, triggers, effect on sleep and daily life, and what the patient has already tried. Look for the mechanisms in the physiology table: weight gain, low blood pressure during sessions, a high phosphate, a new medicine.</li>
<li><strong>Comfort.</strong> Carry out the non-drug measures that are within nursing practice: positioning, skin care, a fan for breathlessness, mouth care, warmth, a quiet word, and time. These are described symptom by symptom in the next section.</li>
<li><strong>Document.</strong> Record the patient&rsquo;s own words, the scores, what you did, and the response. A symptom that is not written down is not handed over.</li>
<li><strong>Report.</strong> Tell the physician, with the severity, the trend, and the effect on the patient&rsquo;s life, using SBAR (Situation, Background, Assessment, Recommendation). Nurses do not prescribe, start, stop, or change symptom medicines; they give them as ordered, watch for benefit and side effects, hold and notify per order or protocol, and report again if relief is not achieved.</li>
<li><strong>Refer.</strong> With the physician&rsquo;s agreement and the patient&rsquo;s consent, involve the social worker for cost and transport, the dietitian for appetite and weight loss, a psychologist or psychiatrist for mood, a chaplain or the patient&rsquo;s own faith leader for spiritual distress, and a palliative care team where one is available.</li>
</ol>
<p><strong>Signs that a fuller conversation is needed.</strong> Repeated hospital admissions, steady loss of weight or function, a patient who is spending more time in bed, a new serious illness such as cancer or a major amputation, symptoms that are not controlled, or a patient or family member who says, in any words, that dialysis no longer seems worth it. The nurse does not lead the prognosis discussion, but can notice these signs, report them, and ask the physician whether it is time to talk about goals.</p>
<p><strong>Stay within your role, and stay present.</strong> Questions such as &ldquo;How long do I have?&rdquo; or &ldquo;Should I stop?&rdquo; are answered by the physician with the patient and family. The nurse can still respond: &ldquo;That is an important question. Can you tell me what is making you think about it? I will make sure the doctor hears it, and I would like to be there when you talk.&rdquo; Not changing the subject is itself care.</p>
"""},
    ],
    "case": {
        "title": "&ldquo;Ayoko na&rdquo; at the chair",
        "html": """
<p>Lola Remedios, 79, has been on HD three times a week for three years for diabetic kidney disease. She also has heart failure and had two hospital admissions in the last four months for fluid overload. Her daughter works abroad as a nurse; her son, who brings her to every session, pays for her medicines. Today she has gained 3.1 kg since the last session and is sitting bolt upright. Her forearms are covered in scratch marks. While you are taping her needles she says quietly, &ldquo;Ayoko na, anak. I don&rsquo;t want this anymore. I can&rsquo;t sleep, I itch all night, and I can&rsquo;t breathe lying down.&rdquo; Her son, overhearing, says, &ldquo;Don&rsquo;t listen to her, Nurse. She is just tired.&rdquo;</p>
""",
        "acte": {
            "Assess": "Check breathing, oxygen saturation, blood pressure, lung sounds, and swelling now; fluid overload is a treatable cause of both breathlessness and distress. Rate her itch, breathlessness, and sleep with the unit&rsquo;s symptom tool, and check her phosphate trend and medicine list. In private, ask what she means by &ldquo;ayoko na&rdquo;: tired of the symptoms, of dialysis, of being a burden, or of living. Screen her mood with the unit&rsquo;s tool and, as Module 14 teaches, ask directly whether she has thoughts of ending her life.",
            "Communicate": "Report to the nephrologist today using SBAR: weight gain and breathlessness lying flat, uncontrolled itch and insomnia, her statement and what she said when you explored it, and the screening results. Ask for review of her fluid removal and target weight, her itch and sleep, and whether a family meeting about goals of care can be arranged, including her daughter by video call if Lola Remedios agrees.",
            "Teach": "Tell her that her words have been heard and will be passed to the doctor, and that relief of itch and breathlessness is possible whether or not she continues dialysis. Show her and her son skin care for itch. Acknowledge her son&rsquo;s worry gently, and explain that listening to what she is saying is how the team can help her feel better.",
            "Escalate": "Act immediately if her breathing worsens, oxygen saturation falls, or chest pain develops. If she describes current thoughts of ending her life, stay with her and follow the crisis pathway in Module 14. A considered request to stop dialysis is not settled at the chair; it goes to the nephrologist and the team, as the stopping-dialysis section explains.",
        },
        "task": "Write the session note: her exact words, your respiratory assessment and vital signs, the symptom scores, the mood screening result and her answer to the direct question about self-harm, whom you informed and when, what was decided, and the plan for a family meeting.",
    },
    "quiz": [
        {"stem": "A nurse new to the dialysis unit says, &ldquo;Palliative care is for patients who have stopped dialysis. Our patients are still on treatment.&rdquo; Which reply best reflects kidney supportive care?",
         "options": [
             ("That is right: comfort care begins only when disease-directed treatment ends", False, "This is the &ldquo;door at the end of the corridor&rdquo; model. Waiting until treatment ends leaves years of symptoms unaddressed."),
             ("Supportive care runs alongside dialysis from the start, addressing symptoms, mood, planning, and family needs, and the balance shifts as needs change", True, "Supportive care is a second track that runs alongside disease-directed treatment for the whole journey; the KDIGO conference applied it to patients on dialysis as well as those managed without it."),
             ("Supportive care is a specialist service, so dialysis nurses do not need to be involved", False, "Most supportive care in dialysis units is delivered by the staff already at the chair; specialist palliative teams are for complex needs."),
             ("Supportive care means starting comfort medicines in every patient on dialysis", False, "Supportive care is an approach of asking, assessing, and relieving; medicines are prescribed by the physician only when needed."),
         ],
         "objective": "Explain why supportive care runs alongside every kidney treatment, and how it differs from care in the last days of life.",
         "sources": ["ckm2015"], "flag": ""},
        {"stem": "A patient on HD says the itch is worst at night and keeps him awake. His forearms show scratch marks and dry, scaly skin. Which explanation of his itch is most accurate?",
         "options": [
             ("It is an allergy to the dialyzer, so antihistamines alone will cure it", False, "Histamine plays only a small part in itch from kidney failure; a dialyzer reaction occurs early in the session and looks different."),
             ("It comes from several mechanisms together, including dry skin, mineral imbalance, and changes in immune and nerve signaling", True, "Itch in kidney failure is multifactorial. Dry skin, high phosphate, inflammation, and an imbalance in opioid signaling may all contribute, so several measures are combined."),
             ("It is psychological, and reassurance is the main treatment", False, "Itch in kidney failure has physical mechanisms and is a recognized symptom that deserves assessment and treatment."),
             ("It shows that his access is infected", False, "Generalized itch with dry skin does not point to access infection; local redness, warmth, pus, or fever would."),
         ],
         "objective": "Relate the common symptoms of kidney failure to their mechanisms, and describe what happens in the body when dialysis stops.",
         "sources": ["rayner2017"], "flag": ""},
        {"stem": "The daughter of a patient who has decided with his physician to stop dialysis asks, &ldquo;What will happen to him now?&rdquo; Which answer is accurate and calm?",
         "options": [
             ("He will die within 24 hours, in pain", False, "This is inaccurate and frightening. The time is usually days to a few weeks, and symptoms that occur can be relieved."),
             ("Nothing will change, because his body has adapted to kidney failure", False, "When dialysis stops, waste products, potassium, fluid, and acid accumulate; families need honest preparation."),
             ("He will most likely become more tired and sleepy over days to a few weeks; the time varies, and the team will treat any breathlessness, restlessness, or itch", True, "Rising waste products usually bring increasing drowsiness. Studies report a mean survival of about one to two weeks, with wide variation; planned symptom control makes a peaceful death more likely."),
             ("Only the doctor can talk about that, so I cannot say anything", False, "The physician leads the prognosis discussion, but the nurse can give general, honest information about what to expect and make sure the family&rsquo;s questions reach the physician."),
         ],
         "objective": "Relate the common symptoms of kidney failure to their mechanisms, and describe what happens in the body when dialysis stops.",
         "sources": ["cohen1995", "oconnor2013", "cohen2000"], "flag": "The physician leads prognosis discussions; the nurse reinforces general information."},
        {"stem": "Your unit wants a short, validated questionnaire that asks kidney patients about symptoms and also about worry, family anxiety, and feeling at peace, with a staff version. Which tool fits best?",
         "options": [
             ("The renal version of the Integrated Palliative care Outcome Scale", True, "It covers kidney symptoms plus emotional and practical concerns, has patient and staff versions, and was found reliable and valid in patients with advanced kidney disease and their nurses."),
             ("The urea reduction ratio", False, "This measures dialysis dose, not symptoms or concerns."),
             ("A pain scale alone", False, "A pain scale captures one symptom; it misses itch, breathlessness, mood, and practical concerns."),
             ("The Kidney Failure Risk Equation", False, "This predicts progression to kidney failure; it does not assess symptoms."),
         ],
         "objective": "Name validated symptom-assessment tools and summarize, in calibrated language, what studies show about conservative care and stopping dialysis.",
         "sources": ["raj2018"], "flag": "Choice of tool and language version follows unit policy."},
        {"stem": "During a routine symptom review, a patient rates her pain as 7 out of 10, says it keeps her from walking to church, and asks you to give her the ibuprofen her neighbor uses. What should you do?",
         "options": [
             ("Give one dose now and report it afterward", False, "Nurses do not give medicines without an order, and anti-inflammatory pain relievers can harm remaining kidney function, raise potassium, and increase bleeding risk."),
             ("Tell her pain is expected on dialysis and that she should rest more", False, "Pain is common but not something to accept; it should be assessed and reported for treatment."),
             ("Assess the pain&rsquo;s site, character, and effect on her life, explain why that medicine is unsafe in kidney failure, use comfort measures, and report to the physician", True, "Assess, comfort, document, report: the physician chooses pain medicines suited to kidney failure, and the nurse explains the risk of self-medication."),
             ("Refer her to the pharmacist and take no further action", False, "The pharmacist can help, but the nurse still assesses, documents, and reports the pain to the physician."),
         ],
         "objective": "Carry out the nurse&rsquo;s role in supportive care: ask routinely, assess, comfort, document, report, and refer.",
         "sources": ["davison2019"], "flag": ""},
    ],
    "reflect": "Think of a patient in your unit who died in the last year. Looking back, when did their supportive-care needs begin, who first noticed them, and was there ever a conversation about what mattered most to them before the last admission?",
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
        "Case: weight gain of 3.1 kg is illustrative; no fluid-removal targets are stated.",
    ],
    "crosswalk": {
        "ph": "Philippine dialysis nurse training topics: patient and family support, ethics, and care of the dying; hospital palliative care and end-of-life policies",
        "anna": "Supportive and palliative kidney care; symptom management; ethics and advance care planning",
        "edtna": "Psychosocial and supportive care; conservative management; care at the end of life",
        "nncc": "Professional practice: ethics and end-of-life care; patient and family education and support",
    },
}
