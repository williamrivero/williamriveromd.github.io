# -*- coding: utf-8 -*-
"""Renal Social Worker, Module 05: A Comprehensive Psychosocial Assessment. Written for this series from published sources."""

MODULE = {
    "image_alt": "A social worker taking notes during a private interview with a middle-aged man in a hospital social service office.",
    "objectives": [
        "Conduct a psychosocial assessment that covers every domain and records strengths beside barriers.",
        "Separate facts, their sources, your interpretations, and what is still unknown.",
        "Write a formulation that explains why the situation is as it is, using predisposing, precipitating, perpetuating, and protective factors.",
        "Replace labels such as &ldquo;noncompliant&rdquo; with factual descriptions of behavior and its causes.",
        "Decide when an assessment must stop for an immediate safety or clinical concern.",
    ],
    "big": """
{{plain:An assessment is like a fisherman reading the sea before he goes out. He looks at the wind, the clouds, the tide, his boat, and his crew, and only then decides where to go. A form filled in from top to bottom is a weather report nobody read. The point of looking is to decide something.}}
{{fig:sw05_domains}}
<p>The picture has a limit. The sea does not change because the fisherman watched it. People do. A good assessment is itself an intervention: being listened to carefully, perhaps for the first time since diagnosis, changes what a person is willing to tell you and to try. And unlike the weather, a person has a view on what you conclude. The formulation should be something they recognize as true about their own life.</p>
<p>Your job in this module is to gather the right information from the right sources, notice the strengths that will carry the plan, and turn it all into a short explanation of why things are as they are. That explanation, the formulation, is what makes your plan more than a list of referrals. International guidance points the same way: a United Kingdom consensus recommends a holistic wellbeing assessment for everyone approaching dialysis or transplant listing, with referral onward for identified needs,[[sw_coyne2023]] and the KDIGO transplant candidate guideline treats psychosocial assessment as part of candidacy.[[sw_chadban2020]]</p>
{{cards:Key terms for this module|Psychosocial assessment::A structured conversation, with other sources, about the person&rsquo;s goals, coping, relationships, resources, and risks.|Domain::One area of life the assessment covers, such as money, family, or safety.|Collateral source::Information from someone other than the person, gathered with permission.|Formulation::A short explanation of why the situation is as it is, which guides the plan.|Strengths::Abilities, relationships, beliefs, and resources the person can use.|Descriptive language::Words that say what happened (&ldquo;missed 4 of 13 sessions in October&rdquo;) instead of labels (&ldquo;noncompliant&rdquo;).}}
""",
    "case": {"title": "&ldquo;Noncompliant&rdquo; on the referral slip", "html": """
<p>Monday, 8:30 a.m. A referral slip from the dialysis unit reads: &ldquo;Mr. Danilo Ramos, 39, HD 1 year. NONCOMPLIANT. Missed 4 sessions this month, IDWG 4&ndash;5 kg. For counseling.&rdquo;</p>
<p>You meet Mr. Ramos at 11:00 a.m. after his session. He is a construction worker paid by the day. He lives in Valenzuela with his wife, who works at a garment factory, and two children aged 9 and 6. He says little at first. When you ask what a normal week looks like, he says the foreman gives work only to men who show up every day, and that he has two jobs a week that pay more than a dialysis day costs him. He smiles when he talks about his son&rsquo;s basketball.</p>
<p>At the end, he mentions that he has not slept well for weeks and that &ldquo;minsan naiisip ko, mas mabuti pang wala na ako&rdquo; (sometimes I think it would be better if I were gone).</p>
""", "questions": ["What do you do first, before finishing the assessment?",
                  "Once he is safe, what facts, sources, and unknowns would you record?",
                  "Write a short formulation that would replace &ldquo;noncompliant.&rdquo;"]},
    "sections": [
        ("domains", "Domains and sources", "Cover everything, record the source", """
<p>A renal psychosocial assessment covers more ground than most medical social work because kidney failure reaches into every part of daily life. Cover each domain at least briefly; go deeper where the person&rsquo;s goals or risks are.</p>
<div class="table-wrap"><table>
<thead><tr><th>Domain</th><th>Ask about</th><th>Strengths to look for</th></tr></thead>
<tbody>
<tr><td>Goals and values</td><td>What matters most; hopes for the next year</td><td>A clear purpose (children, work, faith)</td></tr>
<tr><td>Understanding of illness</td><td>What they know about kidney failure and treatment; teach-back</td><td>Past success managing another illness</td></tr>
<tr><td>Mood, coping, and safety</td><td>Sleep, interest, worry; past coping; thoughts of self-harm</td><td>Faith, humor, friends, past resilience</td></tr>
<tr><td>Family and caregivers</td><td>Household, who helps with what, who depends on them</td><td>A reliable helper; backup</td></tr>
<tr><td>Money and benefits</td><td>Income, debts, PhilHealth status, assistance already used</td><td>Savings, employer support, family abroad</td></tr>
<tr><td>Transport and housing</td><td>How they get to the unit, time, cost; water, space, safety at home</td><td>A neighbor with a vehicle; a stable home</td></tr>
<tr><td>Work, school, roles</td><td>Job type, schedule, employer attitude; changes in roles</td><td>Skills, flexible work</td></tr>
<tr><td>Substances, legal, other</td><td>Alcohol, smoking, other substances; legal problems; other illnesses</td><td>Past success stopping a habit</td></tr>
</tbody></table></div>
<p>Use several sources, with permission: the person, the family, the nurses who see them three times a week, the chart, and the claims officer. Record where each fact came from. &ldquo;Wife reports he drinks every weekend&rdquo; is different from &ldquo;He drinks every weekend.&rdquo;</p>
<p>The DOH issued demographic and assessment tools for medical social workers in 2024; only the overview was reviewed for this course, so check your facility&rsquo;s required forms before you replace anything.[[sw_dm2024]] The toolkit worksheet T01 in the handoff package is a teaching form, not an official DOH tool.</p>
{{key:Cover every domain. Write down the source of every fact.}}
"""),
        ("strengths", "Strengths before deficits", "What will carry the plan", """
<p>A referral usually arrives full of problems. If the assessment only adds more problems, the plan will have nothing to stand on. Every barrier you record should sit beside a strength you can use.</p>
<p>This is not optimism for its own sake. Plans that use what a person already does well are more likely to be carried out. A man who never misses his son&rsquo;s basketball games is a man who can keep a schedule when it matters to him. A grandmother who has run a <em>sari-sari</em> store for 20 years can manage a medicine budget.</p>
{{fig:sw05_formulation}}
<div class="table-wrap"><table>
<thead><tr><th>Barrier recorded</th><th>Strength beside it</th><th>How the plan uses it</th></tr></thead>
<tbody>
<tr><td>Misses sessions for day work</td><td>Reliable worker, valued by his foreman</td><td>Explore a schedule change with the unit; a letter to the foreman</td></tr>
<tr><td>Cannot read the medicine labels</td><td>Daughter in high school is good with phones</td><td>Picture schedule; daughter sets phone reminders</td></tr>
<tr><td>Wife exhausted</td><td>Sister-in-law offers help on weekends</td><td>A written backup plan (Module 13)</td></tr>
<tr><td>Fear of transplant surgery</td><td>Strong faith; trusts the parish priest</td><td>Invite questions; with permission, include the priest in a family talk</td></tr>
</tbody></table></div>
{{key:Every barrier gets a strength beside it. The plan stands on the strengths.}}
"""),
        ("formulation", "The formulation", "Explaining why", """
<p>A formulation turns a pile of facts into an explanation. A simple frame is the four Ps: what made the person vulnerable (predisposing), what triggered the current problem (precipitating), what keeps it going (perpetuating), and what protects them (protective). Write it in two to five sentences that the person would recognize.</p>
<div class="table-wrap"><table>
<thead><tr><th>Part</th><th>Question</th><th>Example (Mr. Ramos)</th></tr></thead>
<tbody>
<tr><td>Predisposing</td><td>What made this person vulnerable?</td><td>Daily-wage work with no sick pay; household depends on his income</td></tr>
<tr><td>Precipitating</td><td>What started the current problem?</td><td>The foreman began giving work only to men present every day</td></tr>
<tr><td>Perpetuating</td><td>What keeps it going?</td><td>Each missed session saves a day&rsquo;s wage; poor sleep and hopelessness</td></tr>
<tr><td>Protective</td><td>What helps?</td><td>Devoted to his children; wife employed; values being a provider</td></tr>
</tbody></table></div>
<p>The formulation is a hypothesis, not a verdict. Say it to the person: &ldquo;It sounds like you are missing dialysis to keep your job, because your family needs the money, and the worry is keeping you awake. Is that right?&rdquo; If they correct you, the correction is the most valuable data you collected.</p>
{{formula:<strong>Worked example, illustrative.</strong> Formulation: Mr. Ramos, 39, is missing about one session a week because his daily-wage income would otherwise fall below what the family needs; his foreman now favors men present every day. The missed sessions and the worry about money are feeding poor sleep and hopelessness, and he has had a passing thought that his family would be better off without him. His love for his children and his wife&rsquo;s steady job are strengths the plan can build on.}}
{{key:A formulation explains why in a few sentences and is checked with the person.}}
"""),
        ("writing", "Writing it, and when to stop", "Facts, sources, unknowns, safety", """
<p>Write the assessment so a colleague who has never met the person could act on it. Use descriptive language, not labels. &ldquo;Noncompliant&rdquo; tells the reader nothing about what to do, and it tells the person they are the problem. &ldquo;Missed 4 of 13 sessions in October; reports he works on those days to keep his job&rdquo; tells everyone what to do next.</p>
<div class="table-wrap"><table>
<thead><tr><th>Label</th><th>Description to write instead</th></tr></thead>
<tbody>
<tr><td>Noncompliant</td><td>&ldquo;Missed 4 of 13 sessions in October; reports work conflicts.&rdquo;</td></tr>
<tr><td>Difficult family</td><td>&ldquo;Daughter raised her voice twice about waiting times; asked for a written schedule.&rdquo;</td></tr>
<tr><td>In denial</td><td>&ldquo;States he expects his kidneys to recover; has not yet heard from the nephrologist that they will not.&rdquo;</td></tr>
<tr><td>Poor support</td><td>&ldquo;Lives alone; neighbor helps with transport on Mondays only.&rdquo;</td></tr>
</tbody></table></div>
<p>Some things stop the assessment. A statement about not wanting to live, a disclosure of violence, chest pain, or confusion comes before every other domain. You can finish the assessment another day; you cannot take back a missed warning. Module 11 covers the safety pathway in full.</p>
{{call:If a person says anything suggesting thoughts of death or self-harm, stop the assessment, ask directly, stay with them, and follow your unit&rsquo;s safety pathway before you do anything else.}}
{{scene:The unknowns line|<p>Social worker Mr. Ben Aquino ends every assessment with a line titled &ldquo;Unknown.&rdquo; For one patient it reads: &ldquo;Whether the brother abroad still sends money; whether the patient knows his transplant work-up has stalled.&rdquo;</p>
<p>At the next visit, the line tells him exactly what to ask.</p>
<p class="tc-scene-take">Writing down what you do not know is what keeps an assessment honest and current.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>First, safety.</strong> &ldquo;Sometimes I think it would be better if I were gone&rdquo; stops the assessment. Ask directly and calmly: &ldquo;When you say that, do you have thoughts of ending your life?&rdquo; Asking does not put the idea in his head (Module 11). Stay with him, follow your unit&rsquo;s safety pathway, and tell the attending nephrologist today. If he denies any plan or intent, you still arrange follow-up and a mental health referral, and you record exactly what he said.</p>
<p><strong>Facts, sources, unknowns.</strong> Facts: missed 4 sessions this month (unit records); daily-wage construction work, foreman favors daily attendance (patient); wife employed at a garment factory (patient); weeks of poor sleep and a passive death thought (patient). Unknowns: household income and debts; whether a different dialysis shift is possible; whether his wife knows how he feels; whether anything has been prescribed for sleep.</p>
<p><strong>Formulation.</strong> Something close to the worked example above: missing sessions to protect the family&rsquo;s income after a change in how his foreman assigns work; the money worry and missed sessions are feeding poor sleep and hopelessness; his children and his wife&rsquo;s job are protective. That replaces &ldquo;noncompliant&rdquo; with a reason, and a reason points to a plan: a shift change, an employer letter, a cost review, a mental health referral, and a talk with his wife if he agrees.</p>
"""],
    "skills": {"title": "An assessment and a formulation",
               "intro": "With a simulated patient, complete a psychosocial assessment and present a formulation while your supervisor observes.",
               "items": [
                   ("Covers all eight domains at least briefly and goes deeper where the goals or risks are.", False),
                   ("Records the source of each fact and separates facts from interpretation.", False),
                   ("Records at least one strength beside each major barrier.", False),
                   ("Writes a formulation of two to five sentences using the four Ps and checks it with the person.", False),
                   ("Replaces labels with descriptive language in the written note.", True),
                   ("Stops the assessment and follows the safety pathway on any statement suggesting self-harm.", True),
                   ("Ends with a list of unknowns and the plan to resolve them.", False),
               ],
               "placement": "Complete one supervised psychosocial assessment of a patient new to dialysis, with consent, in your facility&rsquo;s approved record. Discuss the formulation with your supervisor."},
    "terms": [("Psychosocial assessment", "A structured conversation about goals, coping, relationships, resources, and risks."),
              ("Collateral source", "Information from someone other than the person, gathered with permission."),
              ("Formulation", "A short explanation of why the situation is as it is."),
              ("Four Ps", "Predisposing, precipitating, perpetuating, and protective factors."),
              ("Descriptive language", "Words that describe behavior and its context instead of labeling the person."),
              ("Strengths", "Abilities, relationships, beliefs, and resources the person can use.")],
    "readings": [("ckd-mental-health-sleep.html", "The patient guide to mood and sleep in kidney disease.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("sw_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["05"])
