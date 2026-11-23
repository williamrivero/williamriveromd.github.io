# -*- coding: utf-8 -*-
# Module 17 (core, studied before the capstone on both paths): patient teaching, health literacy, and evidence-based practice.
# Base sections: model, physiology (the science of learning and memory), evidence, bedside (teaching at the chair).
# m17_x.py adds "literacy", "teaching-plan", "motivation", "reading-evidence", and "ebp" after "bedside".
MODULE = {
    "sub": "How people learn when they are ill, tired, and anxious; how to teach so that the lesson survives the trip home; how to spot and respect limited health literacy; and how a nurse reads a study and turns a unit question into evidence-based practice.",
    "desc": "Core Module 17 of the Nephrology Nursing & Hemodialysis self-study series: the science of learning and memory, health literacy in chronic kidney disease, teach-back and teaching at the dialysis chair, motivational interviewing basics, reading a study, and the steps of evidence-based practice.",
    "keywords": "patient teaching dialysis nurse, health literacy chronic kidney disease, teach-back method, motivational interviewing nursing, evidence-based practice nursing PICO, absolute and relative risk, KDIGO grading, patient education hemodialysis Philippines",
    "objectives": [
        "Explain how working memory, attention, anxiety, sleep, and kidney disease shape what a patient can learn, and adapt teaching to those limits.",
        "Summarize the evidence on limited health literacy in chronic kidney disease, on teach-back, and on education before kidney failure, using calibrated language.",
        "Use teach-back, chunking, and spaced repetition to confirm and reinforce understanding without testing or shaming the patient.",
        "Plan, deliver, and document a short teaching episode during a hemodialysis session, involving the family members the patient chooses.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Mental model", "h2": "A narrow doorway into a large room",
         "html": """
<p>Every module so far has ended with something to teach: how much to drink between sessions, which foods carry potassium, how to press a needle site that rebleeds at home, when cloudy fluid on peritoneal dialysis (PD) means a call to the unit. Teaching is woven through nephrology nursing. This module steps back and asks two questions that sit underneath all of it: how does a person actually learn, and how does a nurse know which advice deserves to be taught at all?</p>
<p><strong>The doorway and the room.</strong> Picture memory as a large room reached through a narrow doorway. The room, long-term memory, is enormous; a person can store a lifetime of recipes, routes, and names there. The doorway, working memory, lets only a few items through at once. Whatever the nurse says crowds at the doorway. If too much arrives together, most of it never gets in. Fear, pain, a pounding headache, or a sleepless night narrow the doorway further. Teaching well is mostly the craft of passing a few things through the doorway at a time, making sure they were actually stored, and then bringing them out again often enough that they stay easy to find.</p>
<p><strong>Where the analogy needs correcting.</strong> The doorway is not a fixed size. Things the patient already knows pass through as single bundles: a cook who already measures rice by the cup can take &ldquo;one cup of rice&rdquo; through the doorway as one item, while &ldquo;150 grams of cooked carbohydrate&rdquo; arrives as several unfamiliar pieces. Connecting new advice to what the patient already knows is what widens the doorway.</p>
<p><strong>The second half of the job.</strong> A nurse teaches what the team believes is true and useful. That belief should rest on evidence, not on habit (&ldquo;we have always told patients this&rdquo;). The later sections give the nurse the tools to read a study, to tell an association from a proven effect, to read a guideline&rsquo;s grade, and to turn a question raised at the chair into a small, ethical project. Throughout, the module refers to chronic kidney disease (CKD) and hemodialysis (HD) as well as PD.</p>
<p><strong>What this module does not repeat.</strong> Shared decision-making about treatment choices is in Module 5; screening for depression, delirium, and cognitive problems is in Module 14; quality audits, improvement cycles, and the capstone are in Module 12. Here the focus is the teaching itself and the evidence behind it.</p>
"""},
        {"id": "physiology", "nav": "How people learn", "tag": "Physiology in depth", "h2": "The science of learning and memory in a person with kidney disease",
         "html": """
<p><strong>Three stages.</strong> Learning has three steps, and each can fail. <em>Encoding</em> is taking information in through attention and working memory. <em>Storage</em>, or consolidation, is turning it into a durable long-term memory, a process that continues for hours to days afterward. <em>Retrieval</em> is bringing it back out when it is needed, for example in the kitchen on a Sunday when the patient is deciding whether to have a second bowl of soup.</p>
<p><strong>Working memory is small.</strong> Experimental work suggests that adults can hold only about four meaningful units, or chunks, in mind at once when they cannot rehearse them or link them to what they already know.[[cowan2001]] A chunk can be a single number or a whole familiar idea. That is why a list of ten instructions given at the end of a session overwhelms almost anyone, and why grouping advice into two or three familiar bundles works better. A widely cited review of patients&rsquo; memory for medical information concluded that much of what patients are told is forgotten quickly, that the more is said the less is remembered, and that part of what is remembered is remembered wrongly.[[kessels2003]]</p>
<p><strong>Retrieval strengthens memory.</strong> Being asked to recall something is not only a test; it changes the memory. In a classic experiment, students who practiced recalling a passage remembered much more of it a week later than students who simply reread it, even though the rereaders felt more confident.[[roediger2006]] This is the physiology behind teach-back: when the patient explains the plan in their own words, they are not merely showing that they understood; they are practicing retrieval, and the memory becomes stronger.</p>
<p><strong>Spacing beats cramming.</strong> A meta-analysis of hundreds of experiments found that learning spread over several sessions is retained better than the same amount of learning massed into one, and that the best gap between sessions grows with how long the memory must last.[[cepeda2006]] A dialysis unit is unusually well placed to use this: the nurse sees the patient three times a week and can return to one key point at the next session and the one after.</p>
<p><strong>Sleep consolidates.</strong> Sleep helps turn newly learned material into stable memory.[[diekelmann2010]] Many people on dialysis sleep poorly (Module 14), so a lesson given after a sleepless night may need more repetition.</p>
<p><strong>Anxiety captures attention.</strong> Anxiety draws attention toward threat and away from the task at hand, so a frightened person processes new information less efficiently.[[eysenck2007]] A patient in the first weeks of dialysis, or one who has just been told that an access is failing, may hear little beyond the frightening word. Reassurance, and a plan for when the information will be repeated, come before detail.</p>
<p><strong>Kidney disease affects the brain.</strong> In a study of 374 people aged 55 and older on HD in the United States, about seven in eight of those tested had at least mild cognitive impairment and more than a third had severe impairment, yet only 2.9% had a documented history of a cognitive problem.[[murray2006]] Possible contributors include stroke and small-vessel brain disease, diabetes, retained uremic solutes, anemia, and swings in blood pressure during treatment. Memory and attention may also vary across the dialysis cycle, for example being worse when the patient is fluid-overloaded or hypotensive. The nurse cannot assume that a nod means the information went in, and cannot assume that an adult who fails to remember is careless.</p>
<p><strong>The senses are the entry points.</strong> Age-related hearing loss, the noise of machines and alarms, diabetic eye disease, cataracts, and forgotten reading glasses all block information before it reaches working memory at all. A patient who cannot hear the consonants in a noisy unit may agree to everything and remember nothing.</p>
<div class="table-wrap"><table><thead><tr><th>Factor</th><th>What it does to learning</th><th>What the nurse does</th></tr></thead><tbody>
<tr><td>Small working memory</td><td>Long lists overflow; most items are lost</td><td>Two or three points per session; group advice into familiar bundles</td></tr>
<tr><td>Fast forgetting</td><td>Correct understanding at the chair fades by the next day</td><td>Repeat the key point at the next sessions; give a simple reminder to take home</td></tr>
<tr><td>Retrieval strengthens memory</td><td>Recalling the plan makes it stick better than rereading it</td><td>Teach-back every time; ask again at the next session</td></tr>
<tr><td>Anxiety, pain, cramps, nausea</td><td>Attention is pulled toward the threat or the symptom</td><td>Treat or wait for the symptom to settle; reassure first; teach later</td></tr>
<tr><td>Sleep loss</td><td>Less consolidation of new learning</td><td>Expect to repeat; keep the lesson short</td></tr>
<tr><td>Cognitive impairment, uremia</td><td>Slower processing, poorer recall, difficulty with multi-step tasks</td><td>Simplify; use routines and visual cues; involve the family; report new or worsening confusion</td></tr>
<tr><td>Hearing or vision loss</td><td>Information never reaches working memory</td><td>Face the patient, reduce background noise where possible, check glasses and hearing aids, use large print and pictures</td></tr>
</tbody></table></div>
"""},
        {"id": "evidence", "nav": "Evidence", "tag": "Evidence", "h2": "What is known about health literacy, teach-back, and education before kidney failure",
         "html": """
<p><strong>What health literacy means.</strong> Health literacy is more than the ability to read. A widely used definition, built from a systematic review of earlier definitions, describes it as the knowledge, motivation, and skills to find, understand, appraise, and apply health information in order to make everyday decisions about health care, disease prevention, and health promotion.[[sorensen2012]] A university graduate can have limited health literacy about dialysis; a patient with little schooling can manage PD exchanges flawlessly. It is a fit between a person and the demands placed on them, not a fixed trait.</p>
<p><strong>How common is limited health literacy in CKD?</strong> A systematic review pooled 20 studies of 12,324 patients and estimated that about one in four people with CKD has limited health literacy: 25% of those not on dialysis, 27% of those on dialysis, and 14% of transplant recipients.[[taylor2017]] Nineteen of the 20 studies came from the United States, the studies differed widely, and their quality was low to moderate. Limited health literacy was consistently linked with lower socioeconomic status. No pooled estimate for Philippine kidney patients has been published, so this course adopts the largely United States figure as its working estimate: plan for about one patient in four to have limited health literacy, and teach every patient as if it might apply.</p>
<p><strong>Is it linked with outcomes?</strong> In a cohort of 480 people starting HD in the United States, 32% had limited health literacy, and limited health literacy was associated with a higher risk of death (hazard ratio 1.54; 95% confidence interval 1.01 to 2.36) after adjustment for age, sex, race, and diabetes.[[cavanaugh2010]] A later systematic review found limited health literacy independently associated with hospital admissions, emergency visits, missed dialysis sessions, cardiovascular events, and, in cohort studies, death; but most of the 29 included studies were of poor quality, and the authors concluded that robust evidence of a causal effect is lacking.[[taylor2018]] In plain terms: limited health literacy travels with worse outcomes, but it also travels with poverty, other illness, and poorer access to care, and it is not yet proven that improving health literacy alone would change survival.</p>
<p><strong>Teach-back.</strong> In a systematic review of 20 studies across many settings, teach-back was associated with better outcomes in 19, ranging from knowledge and recall to hospital readmissions and quality of life; the studies were varied and of mixed quality.[[talevski2020]] Module 5 introduced teach-back for treatment choices; the physiology in this module explains why it works.</p>
<p><strong>Education before kidney failure.</strong> In a randomized trial of 70 patients with advanced CKD, adding a two-part educational program (booklets and a short video, then a small-group interactive session) to usual predialysis care increased the proportion who intended to start with a self-care form of dialysis, such as PD or self-care HD, from 50% to 82.1%.[[manns2005]] The outcome was an intention, not the treatment actually received. A systematic review of education and PD combined that single trial with observational studies in which predialysis education was associated with about twice the odds of choosing PD and more than three times the odds of starting on it; because most studies were observational, education cannot be said to cause the choice.[[devoe2016]] The direction of the evidence is consistent: patients who are taught about all options, early and well, more often choose options other than in-center HD. Whether a given patient should choose them is a separate, values-based decision (Module 5).</p>
<p><strong>Motivational interviewing.</strong> A meta-analysis of 72 randomized trials found that motivational interviewing outperformed traditional advice-giving in roughly three out of four studies across a range of conditions, with effects also seen in brief encounters of about 15 minutes and more reliably when there was more than one encounter.[[rubak2005]] The basics are taught in a later section of this module.</p>
<p><strong>What remains uncertain.</strong> Which teaching methods work best for people on dialysis in Philippine settings, in Filipino and the regional languages, has hardly been studied. Most of the evidence above comes from high-income, English-speaking countries. That gap is exactly the kind of question a unit can begin to answer for itself, using the evidence-based practice steps at the end of this module.</p>
"""},
        {"id": "bedside", "nav": "At the chair", "tag": "Clinical application", "h2": "Teaching in the dialysis chair",
         "html": """
<p>The dialysis unit offers something most of health care does not: about four hours, three times a week, with the same patient. Used well, that time is the best classroom in nephrology. Used badly, it becomes a stream of reminders that the patient has learned to tune out.</p>
<p><strong>Choose the moment.</strong> Teaching usually goes best after the patient is connected, settled, and stable, and before fatigue, cramps, or low blood pressure set in near the end of treatment, when attention may already be on going home. Do not teach during an alarm, a hypotensive episode, or cannulation pain. If the patient is drowsy, confused, or distressed, postpone, document why, and plan the next opportunity.</p>
<p><strong>Ask before telling.</strong> Start with what the patient already knows and wants: &ldquo;What have you been told about your weight gain between sessions?&rdquo; or &ldquo;What would you like to understand better about your blood results?&rdquo; This shows where the gaps are, and it connects new information to existing knowledge, which is what widens the doorway.</p>
<p><strong>Use the patient&rsquo;s own data.</strong> &ldquo;You came in 3.5 kilos above your target weight today&rdquo; is more memorable than a general talk about fluid. A result the patient can see on the flow sheet, a potassium value compared with last month, or the ankles that swelled after a heavy weekend make the lesson personal.</p>
<p><strong>One goal, two or three points.</strong> Pick the single most important thing for this patient now, and limit the explanation to two or three points. A patient with a dangerous potassium needs the potassium lesson today; the phosphate binder lesson can wait until Thursday.</p>
<p><strong>Show, then let them show.</strong> For any skill, from pressing a bleeding needle site to measuring a fluid allowance with the patient&rsquo;s own cup, demonstrate it and then watch the patient or family member do it.</p>
<p><strong>Close the loop with teach-back.</strong> Put the burden on yourself: &ldquo;I want to be sure I explained that clearly. When you are at home on Sunday and feel thirsty, what will you do?&rdquo; If the answer has a gap, re-explain in a different way, not louder and not in the same words, and ask again. Teach-back checks the teacher; it is never an examination of the patient.</p>
<p><strong>Include the family the patient chooses.</strong> In many Filipino households the person who shops, cooks, measures water, or gives medicines is not the patient. Ask the patient who should hear the information, and teach that person too, with the patient&rsquo;s agreement.</p>
<p><strong>Mind privacy and dignity.</strong> Dialysis chairs are close together. Lower your voice, draw a curtain where available, and avoid discussing weight gain, missed sessions, or test results where other patients can hear. A patient who feels embarrassed in front of others is unlikely to ask questions.</p>
<p><strong>Repeat across sessions.</strong> Return to the same point at the next session and the one after, asking the patient to explain it again. This uses spacing and retrieval together, and it shows whether the change is happening at home.</p>
<p><strong>Document the learning, not just the teaching.</strong> &ldquo;Health teaching given&rdquo; tells the next nurse nothing. Record what was taught, to whom, the method and language, the teach-back result in the patient&rsquo;s own words where possible, any barrier noticed (hearing, vision, language, distress), and the plan for the next session. Report to the physician or dietitian when a learning barrier changes what the patient can safely do, for example a patient on PD who can no longer perform an exchange correctly.</p>
<p><strong>Stay within scope.</strong> Nurses teach the plan that has been ordered and agreed; they do not change it. When a patient asks whether to stop a medicine, take a new supplement, or change a dose, the nurse explains what is known, gives no new instruction, and refers the question to the physician.</p>
"""},
    ],
    "case": {
        "title": "&ldquo;Opo, naiintindihan ko&rdquo;",
        "html": """
<p>Mang Ernesto, 66, a retired tricycle driver from a town near Angeles City, started HD six weeks ago. His first language is Kapampangan; he understands some Filipino and little English. He comes to sessions alone because his wife, who cooks for the family, sells snacks near the market in the mornings. His weight gain between sessions has been 3.5 to 4.5 kilos, and today he arrives breathless with swollen ankles. When a nurse gave him a printed fluid and diet leaflet in English last week, he folded it into his pocket and said, &ldquo;Opo, naiintindihan ko&rdquo; (&ldquo;Yes, I understand&rdquo;). Today you notice that he squints at the weight scale display and asks another patient to read it for him. His blood pressure is high before treatment, and he says he slept badly because he could not lie flat.</p>
""",
        "acte": {
            "Assess": "Assess his breathing, oxygen saturation, lung sounds, edema, and blood pressure, and report the fluid overload to the physician before teaching anything; safety comes first. Once he is stable on treatment, assess learning barriers without shaming him: his vision (squinting, reading glasses), his language, who prepares his food and drinks, and what he already understands about fluid. Ask him to tell you, in his own words, what he remembers being told.",
            "Communicate": "Report today's weight gain, breathlessness, and blood pressure to the physician using the unit's structured handoff. Tell the team that the English leaflet did not work, that he may have a vision problem, and that his wife does the cooking. Ask for a Kapampangan-speaking colleague to help, and ask whether the dietitian can see him together with his wife.",
            "Teach": "Choose one goal: limiting fluid between sessions. Teach in Kapampangan or Filipino with a bilingual colleague, using his own cup and a bottle marked with his daily allowance as ordered. Keep to two or three points, then ask him to show you how he will measure his drinks tomorrow. With his agreement, arrange to teach his wife, who cooks the soups.",
            "Escalate": "Escalate at once if he becomes more breathless, cannot lie flat, or has chest pain. If a vision or hearing problem is confirmed, request assessment through the physician. If repeated teaching does not change his weight gain, raise it at the care conference instead of repeating the same leaflet.",
        },
        "task": "Write today's teaching note in five or six sentences: what you assessed about his learning needs, the single goal you chose, the method and language used, who was present, his teach-back or return demonstration in his own words, and the plan for the next two sessions.",
    },
    "quiz": [
        {"stem": "At the end of a busy session, a nurse gives a patient who started HD two weeks ago a list of eight instructions about fluid, potassium, phosphate binders, and access care. Two days later he remembers almost none of them. What best explains this?",
         "options": [
             ("The patient was not motivated and needs to be reminded more firmly", False, "Forgetting most of a long list is normal human memory, not a sign of poor motivation; firmer reminders do not fix overload."),
             ("Working memory holds only a few items at once, and much of what is heard is forgotten quickly, especially when tired or anxious", True, "Working memory holds about four chunks, patients forget much of what they are told, and fatigue and anxiety at the end of a session reduce encoding further."),
             ("The information should have been given in English, the language of the medical record", False, "Teaching should use the patient's preferred language; English is not more memorable for a patient whose first language is different."),
             ("Patients on dialysis cannot learn new information and should rely on family members", False, "Cognitive impairment is common, but many patients learn well when teaching is adapted; the family is involved as the patient chooses, not instead of the patient."),
         ],
         "objective": "Explain how working memory, attention, anxiety, sleep, and kidney disease shape what a patient can learn, and adapt teaching to those limits.",
         "sources": ["cowan2001", "kessels2003"], "flag": ""},
        {"stem": "A colleague says: \"A study proved that low health literacy kills dialysis patients, so if we raise their literacy, they will live longer.\" Which response best reflects the evidence?",
         "options": [
             ("That is correct; the association was adjusted for other factors, so it proves cause", False, "Adjusting for a few factors does not rule out other confounders such as poverty and other illnesses; cohort studies show association, not proof of cause."),
             ("The studies show no link between health literacy and outcomes", False, "Limited health literacy has been associated with higher mortality, hospital admissions, and missed sessions."),
             ("Limited health literacy is associated with higher mortality, but it is not proven that improving it alone would change survival", True, "Cohort data show an association, and a systematic review concluded that robust evidence of a causal effect is lacking."),
             ("Health literacy matters only for patients who cannot read", False, "Health literacy includes understanding, appraising, and applying information, and it can be limited in people who read well."),
         ],
         "objective": "Summarize the evidence on limited health literacy in chronic kidney disease, on teach-back, and on education before kidney failure, using calibrated language.",
         "sources": ["cavanaugh2010", "taylor2018"], "flag": ""},
        {"stem": "After explaining how to press a needle site that rebleeds at home, which teach-back prompt is most appropriate?",
         "options": [
             ("\"Do you understand what I told you?\"", False, "A yes-or-no question invites a polite yes and checks nothing."),
             ("\"Let me test you to see whether you were listening.\"", False, "Teach-back checks the teacher's explanation; framing it as a test can shame the patient."),
             ("\"I want to make sure I explained it well. If the site bleeds tonight at home, show me what you will do.\"", True, "The prompt takes responsibility for the explanation and asks the patient to show the skill, which also practices retrieval."),
             ("\"Any questions? No? Good, then we are done.\"", False, "Asking only for questions does not reveal misunderstandings, and many patients will not ask."),
         ],
         "objective": "Use teach-back, chunking, and spaced repetition to confirm and reinforce understanding without testing or shaming the patient.",
         "sources": ["talevski2020", "roediger2006"], "flag": ""},
        {"stem": "A nurse wants a new patient to remember the warning signs of high potassium. Which plan makes best use of how memory works?",
         "options": [
             ("Explain everything in one long session in the first week, then leave a leaflet", False, "Teaching massed into one session is retained less well than the same teaching spaced over several sessions."),
             ("Teach two or three signs today with teach-back, then ask the patient to recall them at the next two sessions", True, "Chunking respects working memory, teach-back and repeated recall strengthen retrieval, and spacing across sessions improves retention."),
             ("Ask the patient to reread the leaflet several times before the next session", False, "Rereading builds confidence more than lasting memory; practicing recall is more effective."),
             ("Teach only the family, because the patient is too anxious", False, "Anxiety is a reason to reassure first and teach in small steps, not to exclude the patient."),
         ],
         "objective": "Use teach-back, chunking, and spaced repetition to confirm and reinforce understanding without testing or shaming the patient.",
         "sources": ["cepeda2006", "roediger2006"], "flag": ""},
        {"stem": "Which note best documents a teaching episode during an HD session?",
         "options": [
             ("\"Health teaching given. Patient verbalized understanding.\"", False, "This does not say what was taught, to whom, by what method, or what the patient actually said."),
             ("\"Taught patient and daughter (with patient's agreement), in Filipino, to measure daily fluid with his own marked bottle. Patient filled the bottle correctly and said: 'This is all I drink until tomorrow.' Poor vision limits reading; will review at the next two sessions.\"", True, "It records the content, the people taught, the language and method, the return demonstration and teach-back in the patient's words, a barrier, and the follow-up plan."),
             ("\"Patient noncompliant with fluid restriction again. Advised to follow instructions.\"", False, "Labeling the patient blames instead of describing, and the note records no teaching method or learning."),
             ("\"Gave the standard diet leaflet. Patient to read at home.\"", False, "A leaflet handed over is not learning confirmed; there is no evidence that the patient can read or use it."),
         ],
         "objective": "Plan, deliver, and document a short teaching episode during a hemodialysis session, involving the family members the patient chooses.",
         "sources": ["anna7"], "flag": "Documentation format follows the unit's record system."},
    ],
    "reflect": "Think of the last time a patient said &ldquo;yes, I understand&rdquo; to something you taught. What did you do to find out whether that was true, and what would you do differently now?",
    "practice": {
        "intro": "With a preceptor, plan and deliver short teaching episodes during HD sessions over two weeks, and review your documentation together.",
        "items": [
            "Assesses readiness and learning barriers (distress, symptoms, vision, hearing, language, cognition) before teaching, and postpones when the patient cannot learn safely.",
            "Chooses one goal per episode, based on the patient&rsquo;s own data and current risk.",
            "Uses the patient&rsquo;s preferred language, with a bilingual colleague when needed, and includes family members the patient chooses.",
            "Demonstrates a skill and observes a return demonstration.",
            "Uses teach-back with a prompt that places the responsibility on the nurse, and re-explains differently when there is a gap.",
            "Revisits the same point at later sessions and documents what was taught, to whom, how, the teach-back result, barriers, and the plan.",
        ],
    },
    "readings": [
        ["understanding-lab-results.html", "A plain-language patient guide to kidney blood tests, useful for practicing how to explain results."],
        ["lab-to-action-card.html", "A one-page, color-coded card linking a lab result to what the patient does next."],
        ["first-nephrology-visit-guide.html", "What patients are advised to bring and ask at a first nephrology visit."],
        ["dialysis-coming-pre-eskd.html", "Patient guide to preparing for dialysis, including the choice between HD and PD."],
        ["caregiver-guide-ckd.html", "A guide for the family members who often carry out the teaching at home."],
        ["medicines-and-your-kidneys.html", "Patient guide to medicines and the kidneys, useful for practicing plain-language explanations."],
        ["natural-supplements-kidney.html", "An evidence-graded patient guide to popular supplements: an example of applying evidence to patients&rsquo; questions."],
    ],
    "calcs": [],
    "external": [
        ["KDIGO 2024 guideline for the evaluation and management of CKD, including how its recommendations are graded", "https://kdigo.org/guidelines/ckd-evaluation--and-management/"],
        ["PubMed, the free search engine for biomedical literature", "https://pubmed.ncbi.nlm.nih.gov/"],
    ],
    "terms": [
        ("Working memory", "The small mental workspace that holds a few items at once while a person takes in new information."),
        ("Chunk", "A meaningful unit held in working memory; a familiar idea counts as one chunk."),
        ("Retrieval practice", "Recalling information from memory, which strengthens the memory more than rereading it."),
        ("Spaced repetition", "Returning to the same material over several sessions separated by time, which improves long-term retention."),
        ("Health literacy", "The knowledge, motivation, and skills to find, understand, appraise, and apply health information."),
        ("Teach-back", "Asking the patient to explain or show, in their own words, what they will do, to check the teacher&rsquo;s explanation."),
        ("Return demonstration", "The patient or family member performs a skill after watching the nurse demonstrate it."),
    ],
    "image": {"file": "renal-nursing-17-teaching",
              "alt": "A dialysis nurse sits beside a patient in a treatment chair, showing him a marked water bottle while his wife watches and listens.",
              "purpose": "Show teaching at the dialysis chair as an unhurried, respectful conversation that includes the family and uses a real object.",
              "scene": "", "focal": "", "setting": "", "details": "", "exclusions": "", "archetype": "", "reviewer": ""},
    "flags": [
        "No Philippine prevalence estimate of limited health literacy among kidney patients was found; by the course owner's decision, the pooled (mostly United States) estimate is adopted and labeled as such. Replace it if a verified local study is published.",
        "Kessels 2003 has no PubMed abstract and PMC returned no full text; its conclusions are stated qualitatively (much is forgotten quickly, more information means less recall, part of what is recalled is wrong) with no percentage. Confirm against the full text.",
        "Murray 2006: 'about seven in eight' is 13.9% + 36.1% + 37.3% = 87.3% with at least mild impairment among the 338 who completed testing; 'more than a third' severe is 37.3%. United States HD patients aged 55 and older.",
        "Statements that memory and attention may vary across the dialysis cycle, and that teaching usually goes best early in the session, are reasoned from physiology, not from a cited trial.",
        "Case set near Angeles City with a Kapampangan-speaking patient; change if a reviewer prefers another region. Fluid allowance is 'as ordered'; no volume is given.",
    ],
    "crosswalk": {
        "ph": "Philippine dialysis nurse training: health teaching of patients and families, and nursing research and evidence-based practice within the nurse's legal scope",
        "anna": "Patient and family education; health literacy; evidence-based practice and research in nephrology nursing",
        "edtna": "Patient education and empowerment in kidney care; research and evidence-based practice",
        "nncc": "Patient education and self-management; professional practice including evidence-based practice",
    },
}
