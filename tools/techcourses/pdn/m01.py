# -*- coding: utf-8 -*-
"""Pediatric Dialysis Nurse, Module 1: Role, scope and the child's journey. POD voice. Every patient and nurse is fictional."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Distinguish the four separate authorizations behind pediatric dialysis work: license, modality training, facility authorization by age and size band, and clinical privileges.",
        "Describe the pediatric kidney team and who decides what, so that every question reaches its owner.",
        "Map a child&rsquo;s kidney journey from diagnosis to transition and name the nurse&rsquo;s job at each stage.",
        "Write a learning agreement that sets supervision, scope and escalation before your first clinical shift.",
    ],
    "big": """
<p>Most of what you know from adult dialysis still applies to children. The membrane, the machine and the physiology of diffusion are the same. What changes is the size of the margins, the people in the room, and the length of the road ahead. A child may be on dialysis for months before a transplant, then need care for sixty more years.</p>
<p>Your work in this track is to keep a child safe on dialysis today while protecting what the child still has to do: grow, learn, play and, usually, receive a kidney. This first module sets the ground rules: who authorizes you, who decides what, and how you start without guessing.</p>
{{plain:Think of an adult dialysis nurse as a pilot who flies a large passenger plane. A pediatric dialysis nurse flies a small plane in the same sky. The instruments look familiar, but every gust moves the small plane more, and there is less fuel to spare.}}
<p>The picture has a limit. A small plane carries no one else; a child never travels alone. Parents, grandparents and siblings come with every child, and they will do much of the care at home. The pediatric dialysis nurse is also a teacher, and the child is also a learner who will one day take over.</p>
{{fig:pdn00_margins}}
{{cards:Key terms for this module|Authorization::Permission from a body with the power to grant it: the PRC, the facility, the medical staff.|Age and size band::The range of ages or weights a nurse is signed off to treat, for example &ldquo;over 20 kilograms&rdquo;.|Scope of practice::What a registered nurse may do under the law and the facility&rsquo;s policy.|Learning agreement::A written plan naming your preceptor, supervision level, tasks and review date.|Escalation::Passing a problem to the person who can decide, quickly and clearly.}}
""",
    "case": {"title": "The adult nurse who was asked to cover", "html": """
<p><strong>Nurse Joanna Reyes, 31</strong>, has dialyzed adults for six years in a hospital unit in Quezon City. On a Saturday the pediatric dialysis nurse is sick, and the charge nurse asks Joanna to &ldquo;just watch&rdquo; <strong>Migo Santos, 8</strong>, who is due for hemodialysis through a tunneled catheter at 7 a.m. Migo weighs 22 kilograms. His mother has brought his school workbook.</p>
<p>Joanna has never set up the pediatric blood lines. The order sheet lists a blood flow and a fluid-removal goal in units she rarely uses. The pediatric nephrologist is reachable by phone.</p>
""", "questions": ["What is Joanna authorized to do this morning, and what is she not?",
                  "Who decides whether Migo is dialyzed today, and by whom?",
                  "What should Joanna say to the charge nurse, and when?"]},
    "sections": [
        ("separate-authorizations", "Authorizations", "Four separate authorizations", """
<p>Your Philippine nursing license is the first authorization, and it covers the care of children and families.[[pd_ra9173]] It does not, by itself, make you competent or authorized to dialyze a child. Three more layers sit on top of it.</p>
{{fig:pdn01_a}}
<div class="table-wrap"><table>
<thead><tr><th>Layer</th><th>Question it answers</th><th>Who grants it</th><th>What to keep</th></tr></thead>
<tbody>
<tr><td>License</td><td>May this person practice nursing?</td><td>Professional Regulation Commission (PRC)</td><td>Current license</td></tr>
<tr><td>Modality training</td><td>Has this nurse been trained in the modality?</td><td>A recognized program; for hemodialysis, structured renal training as PSN guidance describes[[psn2024]]</td><td>Certificates with dates and hours</td></tr>
<tr><td>Facility authorization</td><td>May this nurse perform this task, on this device, for children of this age and size?</td><td>The facility, after observed practice</td><td>Signed competency record with age and size band and review date</td></tr>
<tr><td>Clinical privileges</td><td>May this nurse work in this unit and setting?</td><td>The hospital&rsquo;s nursing service and medical staff rules</td><td>Privilege record</td></tr>
</tbody></table></div>
<p>The review behind this track found no separate Philippine license, fixed training duration or nurse-to-patient ratio specific to pediatric dialysis.[[doh2012]][[pd_ph_sat]] That does not make pediatric work unregulated. It means the facility&rsquo;s own authorization carries more weight, and a nurse authorized for adults is not automatically authorized for children.</p>
{{key:A license lets you practice. A facility authorization by modality, device and age band lets you dialyze this child. You need both.}}
"""),
        ("the-team", "The team", "The pediatric kidney team, and who decides what", """
<p>Children on dialysis are cared for by a team larger than most adult units. The team exists because a child&rsquo;s problems cross organ systems and life domains: growth, bone, blood pressure, school, family income, mood.</p>
<div class="table-wrap"><table>
<thead><tr><th>Team member</th><th>Owns</th><th>The nurse brings them</th></tr></thead>
<tbody>
<tr><td>Pediatric nephrologist</td><td>Diagnosis, prescription, target weight, medicines, modality decision</td><td>Measured findings, trends, the family&rsquo;s questions</td></tr>
<tr><td>Pediatric dialysis nurse</td><td>Safe delivery, monitoring, teaching, escalation, records</td><td>Coordination of everyone else</td></tr>
<tr><td>Renal dietitian</td><td>Feeding plan, energy and protein targets, potassium and phosphate advice</td><td>Weights, heights, intake records, feeding problems</td></tr>
<tr><td>Pharmacist</td><td>Dose checks, compounding, drug removal by dialysis</td><td>Weight changes, missed doses, administration problems</td></tr>
<tr><td>Social worker and psychologist</td><td>Family resources, coping, school liaison, safeguarding</td><td>Concerns noticed at the chair</td></tr>
<tr><td>Surgeon and interventional team</td><td>Catheters, fistulas, PD access</td><td>Access findings and dysfunction</td></tr>
<tr><td>Child life staff or teacher, where available</td><td>Play, preparation for procedures, schooling during treatment</td><td>The child&rsquo;s fears and interests</td></tr>
</tbody></table></div>
<p>When you do not know who owns a question, ask it of the nephrologist first. A question routed to the wrong person costs time; a question never asked can cost the child.</p>
{{key:You coordinate many decisions and own a few. Name the owner of each before you act.}}
"""),
        ("the-childs-journey", "The journey", "The child&rsquo;s kidney journey", """
<p>A child&rsquo;s kidney story usually runs through five stages: chronic kidney disease (CKD) care, preparation for kidney replacement, dialysis, transplant, and transition to adult care. Some children receive a kidney before ever needing dialysis; some return to dialysis when a transplant fails. The nurse appears at every stage.</p>
{{fig:pdn01_b}}
<p>Outcomes on pediatric dialysis are better than many families fear, and they depend heavily on resources. In the International Pediatric Peritoneal Dialysis Network (IPPN) registry of 2,956 children, the probability of death after three years on maintenance PD was 5% overall, from 2% in North America to 9% in Eastern Europe, and country income explained about half of the difference between regions.[[pdn_ploos2021]] A European registry found the same pattern: public health spending explained most of the variation in mortality between countries.[[pdn_chesnaye2017]] Both are observational. They tell you that systems matter, and that the nurse&rsquo;s reliability is part of the system.</p>
{{scene:Saturday, 6:40 a.m.|<p>Back to Joanna. She reads Migo&rsquo;s chart and finds the written plan: pediatric lines, a specific dialyzer, a blood flow in mL per minute and a goal in mL. She has never primed those lines.</p><p>She tells the charge nurse before Migo is connected: &ldquo;I am authorized for adults only. I can weigh him, take his vital signs and keep him company, but I should not set up or run his treatment. Can we call the pediatric nephrologist now?&rdquo;</p><p class="tc-scene-take">Saying it before the connection, in one clear sentence, is the safe moment. After the pump starts, the same sentence is much harder to say.</p>}}
{{key:Dialysis is one stage of a long road. Every decision today should leave the child&rsquo;s options open for tomorrow.}}
"""),
        ("starting-safely", "Starting safely", "Starting safely: the learning agreement", """
<p>New pediatric dialysis nurses fail most often not from lack of knowledge but from unclear limits. A learning agreement fixes the limits in writing before the first shift.</p>
<ul>
<li><strong>Preceptor:</strong> a named senior pediatric dialysis nurse, and who covers when they are away.</li>
<li><strong>Supervision level by task:</strong> observe, assist, perform with direct supervision, perform with the preceptor nearby.</li>
<li><strong>Age and size band:</strong> start with older, larger, stable children; small infants come later and need separate sign-off.</li>
<li><strong>Escalation:</strong> whom to call, for what, at what hour, with phone numbers that work.</li>
<li><strong>Readiness:</strong> pediatric resuscitation preparation as your employer requires, and orientation to the emergency cart.</li>
<li><strong>Review date:</strong> when the agreement is reassessed.</li>
</ul>
<p>Keep your agreement and competency records in the facility&rsquo;s system. The Academy is self-study; it never records competence.</p>
{{key:Write the limits down before the first shift. A limit you never stated is a limit nobody will protect.}}
"""),
    ],
    "debrief": ["""
<p><strong>What Joanna may do.</strong> She is licensed, and she is authorized for adult hemodialysis. She is not authorized to set up or run pediatric treatment on that equipment. She may weigh Migo, take age-appropriate vital signs, comfort him and his mother, and help a qualified nurse.</p>
<p><strong>Who decides.</strong> The pediatric nephrologist decides whether Migo is dialyzed today, how, and by whom; the charge nurse and the facility decide staffing. Options include a qualified nurse from another area, a short delay with close monitoring, or transfer, depending on Migo&rsquo;s potassium, fluid status and symptoms.</p>
<p><strong>What Joanna says, and when.</strong> She speaks before connection, states her authorization in one sentence, offers what she can safely do, and asks for the nephrologist to be called. She documents the conversation and the decision. Afterward she asks to start a pediatric learning agreement.</p>
"""],
    "skills": {"title": "Starting safely in pediatric dialysis", "intro": "Complete these with your preceptor in your first week.",
               "items": [("States own authorization by modality, device and age band in one sentence", True),
                         ("Names the owner of five common decisions (target weight, antibiotic choice, fill volume, feeding plan, school letter)", False),
                         ("Locates the pediatric emergency cart and checks its log with the preceptor", True),
                         ("Lists escalation contacts with working numbers for day, night and weekend", True),
                         ("Drafts a learning agreement with supervision levels and a review date", False)],
               "placement": "Shadow a pediatric dialysis shift from setup to the last disconnection. Note every moment a decision passed from one person to another."},
    "quiz": [
        ('What does a Philippine nursing license, by itself, authorize?',
         ['Dialysis of any patient', 'The practice of nursing, including care of children and families', 'Prescribing dialysis', 'Teaching caregivers to change doses'], 1,
         'The license is the first layer. Modality training, facility authorization and privileges sit on top of it.'),
        ('A nurse is authorized for adult hemodialysis. May she run a child&rsquo;s treatment on pediatric lines?',
         ['Yes, the machine is the same', 'Yes, if the child is over 10 years', 'Only with facility authorization for that device and age band', 'Yes, if a parent agrees'], 2,
         'Authorization is by modality, device and age or size band.'),
        ('The review behind this track found which pediatric-specific Philippine requirement?',
         ['A separate pediatric dialysis nurse license', 'A fixed pediatric nurse-to-patient ratio', 'A six-month fellowship', 'None specific; facility authorization carries the weight'], 3,
         'No separate pediatric license or ratio was found. Facility authorization therefore matters more.'),
        ('Who owns the target weight for a child on hemodialysis?',
         ['The pediatric nephrologist', 'The nurse', 'The renal dietitian', 'The parent'], 0,
         'The nurse measures and reports; the nephrologist sets the target.'),
        ('Who writes the feeding plan for a child on PD?',
         ['The nurse', 'The renal dietitian', 'The pharmacist', 'The school nurse'], 1,
         'The nurse measures, reinforces and reports intake and growth.'),
        ('In the IPPN registry, what was the overall probability of death after three years on maintenance PD?',
         ['About 1%', 'About 25%', 'About 5%', 'About 50%'], 2,
         '5% overall, from 2% in North America to 9% in Eastern Europe.'),
        ('What explained about half of the regional difference in IPPN mortality?',
         ['Catheter brand', 'Nurse age', 'Season', 'Country income'], 3,
         'Income category explained 50.1% of the variance. The finding is observational.'),
        ('Why does this track call the pediatric nurse a teacher as well as a clinician?',
         ['Caregivers do much of the care at home and the child will take over later', 'Children must pass exams', 'Teaching replaces treatment', 'Hospitals require lectures'], 0,
         'Family members and, later, the young person carry the care day to day.'),
        ('When is the safest moment to say &ldquo;I am not authorized for this&rdquo;?',
         ['After the pump starts', 'Before connection, in one clear sentence', 'At the end of the shift', 'Only if something goes wrong'], 1,
         'Speaking before connection protects the child and is easier than stopping later.'),
        ('Which item belongs in a learning agreement?',
         ['Your salary', 'The child&rsquo;s diagnosis', 'Supervision level by task and a review date', 'Your exam scores'], 2,
         'It fixes limits and supervision in writing.'),
        ('A new pediatric dialysis nurse should usually start with which children?',
         ['The smallest infants', 'Children in the PICU', 'Any child on the list', 'Older, larger, stable children'], 3,
         'Small infants need separate sign-off because margins are smallest.'),
        ('Where are a nurse&rsquo;s competency records kept?',
         ['In the facility&rsquo;s approved system', 'On the Academy site', 'In the patient&rsquo;s chart', 'On the nurse&rsquo;s phone'], 0,
         'The Academy is self-study and never records competence.'),
        ('A question arises and you do not know who owns it. What is the default?',
         ['Decide yourself', 'Ask the nephrologist first', 'Wait for the next shift', 'Ask the parent'], 1,
         'A misrouted question costs time; an unasked one can harm.'),
        ('What do the European registry and IPPN findings imply for nurses?',
         ['Nothing; they are about money', 'Children always do badly', 'Systems matter, and reliable nursing is part of the system', 'Only machines matter'], 2,
         'Both are observational, but they point to resources and reliability.'),
        ('Which stage usually follows dialysis for a child?',
         ['Retirement', 'Discharge from all care', 'Conservative care only', 'Transplant, then transition to adult care'], 3,
         'Most children are prepared for transplant; transition follows in adolescence.'),
    ],
    "terms": [("Authorization", "Permission from a body that has the power to grant it."),
              ("Age and size band", "The range of ages or weights a nurse is signed off to treat."),
              ("Learning agreement", "A written plan of preceptor, supervision level, tasks and review date."),
              ("Clinical privileges", "Permission from the hospital to work in a unit or setting."),
              ("Preceptor", "An experienced nurse who supervises and assesses a learner."),
              ("Transition", "The planned move of a young person from pediatric to adult care.")],
    "readings": [("ckd-children-young-adults.html", "Kidney disease in children and young adults: the patient-facing view."),
                 ("born-small-kidneys-for-life.html", "Why birth weight and prematurity shape lifelong kidney risk.")],
    "calcs": ["calc-pediatric-dialysis-nurse-toolkit.html"],
}
