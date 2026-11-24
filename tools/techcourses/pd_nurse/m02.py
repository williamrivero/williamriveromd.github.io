# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 02: Modality counseling, shared decisions and home readiness.
Rewritten in the Renal Care Academy POD voice, with illustrative scenarios. Every patient and nurse is fictional. Edit here."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Conduct a modality conversation that starts from the person&rsquo;s life goals, not from the machine.",
        "Explain the evidence comparing PD and in-center hemodialysis honestly, including what observational data can and cannot show.",
        "Assess physical, cognitive, sensory, emotional, social and environmental readiness for home PD.",
        "Separate remediable barriers from clinical suitability questions that belong to the nephrologist.",
        "Write a readiness plan with named owners, observable criteria and a reassessment date, including assisted PD where self-care is not feasible.",
    ],
    "big": """
<p>In the Philippines, most people with kidney failure start dialysis in a center, often after an urgent hospital admission. Many never hear peritoneal dialysis (PD) described properly. Local reports suggest that well over 90% of Filipinos on dialysis receive in-center hemodialysis. Registry-grade national figures should be confirmed with the Philippine Renal Disease Registry before you quote a number to a patient.</p>
<p>Your work in this module is to make the choice real. The person understands both paths. The team knows what matters to them. And the barriers that can be fixed get fixed before anyone mistakes them for unsuitability. Most people who are told &ldquo;PD is not for you&rdquo; were never shown that a lamp, a picture checklist or a different helper would have solved the problem.</p>
{{plain:Think of choosing a modality as fitting a treatment into a house that already has people, routines and limits. The question is not &ldquo;Is PD good?&rdquo; but &ldquo;Can this treatment live in this house, with this person, this year?&rdquo;}}
<p>The picture has a limit. A house is fixed; people change. Vision, strength, caregivers, jobs and homes change over months. The person you assess before dialysis, tired and slowed by uremia, may learn far better six weeks after starting. Readiness is a judgment at a point in time, so every readiness plan needs a reassessment date.</p>
{{cards:Key terms for this module|Shared decision-making::A conversation in which the person&rsquo;s goals and the team&rsquo;s evidence are weighed together.|Readiness::Safe performance of the needed tasks, observed under real conditions.|Remediable barrier::An obstacle that support, equipment or a different helper can remove.|Suitability::A clinical question about whether PD can work in this body, decided by the nephrologist.|Assisted PD::PD in which another person performs some or all of the tasks.}}
""",
    "case": {"title": "Mang Ernesto wants to stay home", "html": """
<p><strong>Mang Ernesto, 71</strong>, a retired jeepney driver from Malolos, has diabetic kidney disease and is approaching dialysis. He wants to keep tending his small <em>sari-sari</em> store, which he opens at six every morning.</p>
<p>His near vision is poor and he has a mild tremor in both hands. His wife died two years ago. His daughter <strong>Liza</strong> works days in Manila, leaves at 5:30 AM and returns at 8 PM. A grandson, 16, is home after school.</p>
<p>At his last clinic visit a resident wrote, &ldquo;Poor vision, tremor, lives alone by day. For hemodialysis.&rdquo; Nurse <strong>Joy</strong> has been asked to lead the readiness assessment before the plan is finalized.</p>
""", "questions": ["Which of his barriers can be fixed, and which belong to the nephrologist?",
                  "Who should be trained for each task?",
                  "What would you need to see before you sign readiness?"]},
    "sections": [
        ("what-the-evidence", "The evidence", "What the evidence actually says", """
<p>Patients ask two questions first: &ldquo;Will I live as long?&rdquo; and &ldquo;Is it safe at home?&rdquo; You owe them honest answers, which means saying what the evidence shows and what it does not.</p>
<h3>Survival</h3>
<p>Many registry comparisons show similar survival on PD and hemodialysis. PD sometimes looks better in the first one to two years, and hemodialysis sometimes looks better later. These are observational comparisons. People who choose PD differ from those who start hemodialysis urgently: they are often younger, planned earlier and less sick at the start. That selection explains much of the apparent difference. No large randomized trial has settled the question, and one is unlikely.</p>
<p>The honest summary is that, for people eligible for both, survival is broadly similar, and the decision rests on lifestyle, values, home and the person&rsquo;s own priorities.</p>
<h3>What PD offers</h3>
<p>Treatment at home. Fewer trips across the city in traffic. More control over the day. No needles. Steadier fluid and potassium shifts than intermittent in-center sessions. And, in observational studies, slower loss of residual urine. The 2024 International Society for Peritoneal Dialysis (ISPD) position paper on assisted PD states that PD should be offered to every eligible person considering maintenance dialysis, noting similar health outcomes and often lower cost than in-center hemodialysis.[[pd_oliver2024]] That is a position statement from an expert group, not a graded recommendation from a trial.</p>
<h3>What PD asks</h3>
<p>Daily treatment, every day of the year. A catheter in the abdomen. Storage for supplies. A clean space. The discipline of technique at every exchange. And a risk of peritonitis that training and technique reduce but never remove.</p>
<p>About half of people who start PD are no longer on it at two years, according to the 2026 ISPD position statement on loss from PD therapy. The common reasons are transfer to hemodialysis, death and transplantation.[[pd_quinn2026]] Transplantation is a good reason to leave PD. Much of the rest begins with readiness that was assumed rather than observed.</p>
<h3>Shared decision-making is the method, not a courtesy</h3>
<p>The 2020 ISPD practice recommendations on goal-directed prescribing put shared decision-making at the center of PD care. They are labeled practice points, not graded recommendations, because the underlying evidence is limited.[[pd_brown2020]]</p>
<div class="table-wrap"><table>
<thead><tr><th>If the patient says</th><th>What the evidence supports saying</th></tr></thead>
<tbody>
<tr><td>&ldquo;PD is for people who cannot afford hemodialysis.&rdquo;</td><td>PD is a full form of dialysis. For people eligible for both, survival is broadly similar.</td></tr>
<tr><td>&ldquo;PD is only for young people.&rdquo;</td><td>Older people do PD, including with help from family or a health worker.</td></tr>
<tr><td>&ldquo;At home I will surely get an infection.&rdquo;</td><td>Peritonitis is a real risk. Good training and technique lower it. Most episodes respond to prompt treatment, which is why we teach you to call early.</td></tr>
<tr><td>&ldquo;If I choose PD, I can never get a transplant.&rdquo;</td><td>PD does not close the door to transplantation. Evaluation can run alongside.</td></tr>
</tbody></table></div>
{{key:Say what the evidence shows and what it cannot show. &ldquo;Broadly similar&rdquo; is the honest answer on survival for people eligible for both.}}
"""),
        ("the-conversation", "The conversation", "The conversation", """
<p>Start with the person, not the modality. A brochure answers questions the patient has not asked. A good conversation finds out what the treatment must fit around.</p>
<ul>
<li>&ldquo;What does a good week look like for you right now?&rdquo;</li>
<li>&ldquo;What would you most want to keep doing?&rdquo; Work, church, caring for grandchildren, farming, travel to the province.</li>
<li>&ldquo;Who lives with you, and who helps when you are sick?&rdquo;</li>
<li>&ldquo;What have you heard about PD? About hemodialysis?&rdquo; Correct myths gently.</li>
<li>&ldquo;What worries you most?&rdquo;</li>
</ul>
<h3>Example: a conversation that changes the plan</h3>
<p>Mrs. Teresita, 52, sells vegetables at the Balintawak market from 3 AM to noon. The resident has listed her for hemodialysis on Mondays, Wednesdays and Fridays at 7 AM.</p>
<p>Nurse Kris asks what a good week looks like. Mrs. Teresita says the market <em>is</em> her week; if she loses three mornings, her stall goes to her cousin. Kris asks what she has heard about PD. &ldquo;That it is for rich people with big houses.&rdquo; Kris explains, plainly, that PD is done at home, that an automated form runs overnight, and that whether it suits her body is a question for the nephrologist. Mrs. Teresita asks to be considered.</p>
<p>Kris records her words: &ldquo;I need my mornings at the market.&rdquo; She routes the request to the nephrologist with the context. She did not promise PD. She made sure the choice was offered.</p>
<p>Record the person&rsquo;s own words. Revisit the conversation after hospital stays, after a caregiver change and whenever the person asks.</p>
<p>Cover transplant early. Being on PD does not close the door to transplantation, and the transplant evaluation can run in parallel.</p>
{{key:Write down what the person wants to protect, in their own words. It is the reason for every decision that follows.}}
"""),
        ("the-readiness-assessment", "Readiness", "The readiness assessment", """
<p>Readiness has six domains. For each one, ask what the person can actually do under realistic conditions, not what the chart says. A note that reads &ldquo;poor vision&rdquo; tells you nothing until you know whether the person can read a bag label under a lamp with a magnifier.</p>
{{fig:pd02_readiness}}
<div class="table-wrap"><table>
<thead><tr><th>Domain</th><th>What you assess</th><th>Common remediable barrier</th><th>Possible support</th></tr></thead>
<tbody>
<tr><td>Physical</td><td>Grip, fine finger movement, lifting a 2-liter bag, bending</td><td>Arthritis, tremor, weakness</td><td>Assistive devices, a cycler instead of manual exchanges, a caregiver for lifting</td></tr>
<tr><td>Sensory</td><td>Near vision for labels and clamps, hearing alarms</td><td>Poor near vision, glare</td><td>Task lighting, magnifier, high-contrast labels, alarm volume</td></tr>
<tr><td>Cognitive</td><td>Learning, memory for sequence, problem solving</td><td>Uremic slowing, low literacy</td><td>Staged training, picture checklists, teach-back, retesting once dialysis improves thinking</td></tr>
<tr><td>Emotional</td><td>Distress, depression, fear, motivation</td><td>Grief, fear of infection</td><td>Counseling, contact with an experienced PD patient, gradual exposure</td></tr>
<tr><td>Social</td><td>Caregiver availability, family dynamics, finances</td><td>Caregiver works days</td><td>Reassign tasks to an available person, APD at night, assisted PD</td></tr>
<tr><td>Environmental</td><td>Clean exchange area, water, hand hygiene, storage, pets, electricity, waste, transport</td><td>Small home, shared bathroom, power interruptions</td><td>A dedicated corner with a door, a clean table, scheduled deliveries, a backup plan for power</td></tr>
</tbody></table></div>
<h3>Testing, not asking</h3>
<p>Ask a patient &ldquo;Can you see the label?&rdquo; and most will say yes. Hand them three bags of different strengths and ask them to read the strength, volume and expiry aloud, and you will know. The same holds for every domain.</p>
<div class="table-wrap"><table>
<thead><tr><th>Instead of asking</th><th>Ask them to show you</th></tr></thead>
<tbody>
<tr><td>&ldquo;Can you open the clamps?&rdquo;</td><td>Open and close a training clamp three times</td></tr>
<tr><td>&ldquo;Can you lift the bag?&rdquo;</td><td>Lift a training bag from the floor to the table</td></tr>
<tr><td>&ldquo;Will you remember the steps?&rdquo;</td><td>Do the sequence once with a picture checklist and once without</td></tr>
<tr><td>&ldquo;Is there somewhere clean?&rdquo;</td><td>Walk through the home with you and point to it</td></tr>
</tbody></table></div>
<h3>The home visit is an assessment, not an inspection</h3>
<p>Many Filipino homes are small and shared. The question is not whether the house is impressive. It is whether one clean, closable, well-lit area can be set up. Can hands be washed and dried properly? Can pets be kept out during exchanges? The 2022 ISPD peritonitis recommendations added specific guidance on domestic pets.[[pd_li2022]] Where will 30 or more boxes a month be stored, away from heat and floodwater? Is the electricity reliable enough for a cycler?</p>
<h3>Example: a home in a flood-prone street</h3>
<p>Nurse Joy visits Mr. Rolando in Malabon. The ground floor floods ankle-deep two or three times each rainy season. The family had planned to stack supplies under the stairs.</p>
<p>Joy does not write &ldquo;unsuitable home.&rdquo; She writes the barrier and a fix. Supplies go on raised shelving on the second floor. The exchange corner moves to the upstairs bedroom, which has a door and a window. Two weeks of supplies stay in reserve before typhoon season, with the supplier&rsquo;s emergency number on the wall. At the follow-up visit, she checks that the boxes are off the floor and the corner is clean.</p>
<h3>Suitability is the nephrologist&rsquo;s call</h3>
<p>Prior major abdominal surgery, large hernias, severe lung disease, very large body size or a recent abdominal catastrophe may make PD difficult or unsafe. These are clinical questions. Your job is to document the facts accurately and route them, not to decide.</p>
<div class="table-wrap"><table>
<thead><tr><th>Usually a remediable barrier</th><th>Usually a suitability question</th></tr></thead>
<tbody>
<tr><td>Poor near vision that improves with a lamp and magnifier</td><td>Large ventral hernia</td></tr>
<tr><td>Tremor that makes clamps slow</td><td>Several major abdominal operations</td></tr>
<tr><td>Caregiver available only at night</td><td>Severe restrictive lung disease</td></tr>
<tr><td>No clean room yet</td><td>Recent abdominal catastrophe</td></tr>
</tbody></table></div>
{{key:Before anyone writes &ldquo;unsuitable,&rdquo; ask whether the barrier is one that support can remove.}}
"""),
        ("assisted-pd", "Assisted PD", "Assisted PD", """
<p>When the person cannot safely perform self-care PD and family support is missing or insufficient, assisted PD may be the path. The 2024 ISPD position paper defines assistance broadly: a family member, a paid caregiver, a home-care nurse or a community health worker, temporary or long term.[[pd_oliver2024]]</p>
<p>In observational comparisons, older and frailer people on assisted PD have had broadly similar peritonitis-free survival to self-care PD. These studies are small and their patients were selected, so they cannot show that assistance itself protects against peritonitis.[[pd_oliver2024]] Module 11 covers assisted PD in detail.</p>
<h3>Example: matching each task to a person</h3>
<p>Mrs. Lourdes, 78, has had a stroke that weakened her right hand. Her son works nights as a security guard and sleeps until noon. Her granddaughter, 22, works from home.</p>
<div class="table-wrap"><table>
<thead><tr><th>Task</th><th>Who</th><th>How it will be shown</th></tr></thead>
<tbody>
<tr><td>Cycler setup each evening</td><td>Granddaughter</td><td>Independent setup observed three times</td></tr>
<tr><td>Connection and disconnection</td><td>Granddaughter; son as backup on weekends</td><td>Both observed; backup trained before home start</td></tr>
<tr><td>Recognizing a cloudy bag and calling</td><td>Mrs. Lourdes, granddaughter, son</td><td>Each states what to do and whom to call</td></tr>
<tr><td>Exit-site care</td><td>Granddaughter</td><td>Observed, with correct description of warning signs</td></tr>
</tbody></table></div>
<p>Mrs. Lourdes keeps the tasks she can do safely. Recognizing a cloudy bag needs eyes, not two good hands.</p>
{{key:The test of readiness is safe performance, observed under the conditions where the treatment will actually happen.}}
"""),
    ],
    "debrief": ["""
<p><strong>What Joy finds.</strong> With a desk lamp and a 3&times; magnifier, Mang Ernesto reads the solution strength and expiry correctly. He opens a clamp slowly but safely. He forgets the sequence once without a checklist and never with a picture checklist. His home has a small back room with a door, but the family cat sleeps there.</p>
<p><strong>Which barriers can be fixed.</strong> Vision, sequence memory, the cat and storage are all remediable. Daytime support is a real gap, but there are options: APD with Liza setting up at night, or assisted CAPD. Whether his body suits PD, and which form, is for the nephrologist.</p>
<p><strong>What Joy plans.</strong></p>
<div class="table-wrap"><table>
<thead><tr><th>Barrier</th><th>Owner</th><th>Action</th><th>Observable criterion</th><th>Reassess</th></tr></thead>
<tbody>
<tr><td>Near vision</td><td>Joy, Mang Ernesto</td><td>Lamp and magnifier at the exchange table; high-contrast checklist</td><td>Reads strength, volume and expiry correctly 3 of 3 times</td><td>Training day 3</td></tr>
<tr><td>Daytime support</td><td>Team, Liza</td><td>Discuss APD with night setup by Liza, or assisted CAPD; nephrologist to advise</td><td>Liza completes cycler setup independently</td><td>Before home start</td></tr>
<tr><td>Cat in exchange room</td><td>Family</td><td>Move the cat&rsquo;s sleeping area; door closed during exchanges</td><td>Home visit confirms</td><td>Home visit</td></tr>
<tr><td>Storage</td><td>Joy, supplier</td><td>Raised shelving away from floor and heat</td><td>30 boxes stored off the floor</td><td>Home visit</td></tr>
</tbody></table></div>
<p><strong>What she needs before signing.</strong> Observed independent performance by whoever will do each task. Joy documents that the choice between self-care CAPD and APD with Liza&rsquo;s setup is pending nephrology review. The resident&rsquo;s note is not wrong about the facts. It was simply written before anyone asked which facts could change.</p>
"""],
    "skills": {"title": "Practice drill",
               "intro": "Complete both tasks with a peer while your preceptor observes.",
               "items": [("Role-play a modality conversation with a peer as a 45-year-old <em>tricycle</em> driver who fears losing income.", False),
                         ("Produce a readiness plan with at least two barriers, two named owners, observable criteria, a backup contact and a reassessment date.", False)]},
    "quiz": [
        ("What is the best opening for a modality conversation?",
         ["&ldquo;What does a good week look like for you, and what do you want to keep doing?&rdquo;", "&ldquo;PD is cheaper, so you should choose it.&rdquo;", "&ldquo;Hemodialysis is safer.&rdquo;", "&ldquo;Here is the PD machine manual.&rdquo;"], 0,
         "Goal-directed care starts from the person&rsquo;s priorities. The other openings are directive, unsupported as stated, or start from the equipment."),
        ("How should observational survival comparisons between PD and hemodialysis be described to a patient?",
         ["PD is proven to give longer life", "Hemodialysis is proven to give longer life", "For people eligible for both, survival is broadly similar; the choice rests largely on lifestyle and values", "No data exist"], 2,
         "The data are observational and shaped by who chooses each modality. Claims of proven superiority overstate them."),
        ("According to the 2026 ISPD position statement, about what proportion of people who start PD are no longer on it at two years?",
         ["About 5%", "About one in five", "Nearly all", "Nearly half"], 3,
         "Nearly half, mostly through transfer to hemodialysis, death or transplantation. Transplantation is a good outcome; much of the rest is the target of better readiness."),
        ("Which barrier is usually remediable rather than a suitability question for the nephrologist?",
         ["Large ventral hernia", "Poor near vision that is adequate with lighting and a magnifier", "Recent abdominal catastrophe", "Severe restrictive lung disease"], 1,
         "Vision aids can solve it, and you can verify that by watching. The others are clinical suitability questions."),
        ("What establishes readiness after a home barrier is addressed?",
         ["The patient&rsquo;s statement that it is fixed", "Observed safe performance under the revised conditions", "A signed consent form", "Completion of the scheduled number of training days"], 1,
         "Readiness is demonstrated, not declared. Statements, forms and calendars do not show performance."),
        ("A caregiver will perform the cycler setup. Who must demonstrate it?",
         ["The patient only", "Any family member", "The nurse", "The designated caregiver, with the patient&rsquo;s own role and a backup arrangement also assessed"], 3,
         "The person who does the task shows it. A backup is needed for illness, work or travel."),
        ("The 2020 ISPD goal-directed prescribing recommendations are best described as:",
         ["Practice points based on limited evidence", "Grade 1A recommendations", "Mandatory regulations", "Withdrawn"], 0,
         "They are labeled practice points. Never assign a grade the source did not give."),
        ("Why does a readiness plan need a reassessment date?",
         ["For billing", "Because PD solutions expire", "Because function, caregivers and homes change over time", "It does not need one"], 2,
         "Readiness is a judgment at one point in time. A patient slowed by uremia may learn much better after starting dialysis."),
        ("During a home visit, the family cat sleeps in the planned exchange room. What is the best action?",
         ["Ignore it; pets do not matter", "Declare the patient unsuitable for PD", "Plan to keep pets out of the exchange area and confirm at follow-up", "Ask the family to give the cat away"], 2,
         "The 2022 ISPD recommendations address pets as a modifiable risk. Unsuitability or giving the pet away is out of proportion."),
        ("Mrs. Teresita says, &ldquo;If I choose PD, I can never have a transplant.&rdquo; What is correct?",
         ["Transplant evaluation can proceed while she is on PD", "PD closes the door to transplant", "Only hemodialysis patients can be listed", "Transplant must wait five years after PD starts"], 0,
         "PD does not prevent transplantation, and evaluation can run alongside."),
        ("A patient has a tremor and struggles with clamps. What should you consider first?",
         ["Telling him PD is impossible", "Assistive devices, a cycler-based regimen or reassigning that task, then observing performance", "Skipping the clamp step", "Delaying dialysis"], 1,
         "Adapt, then verify by watching. Skipping a step is unsafe, and declaring PD impossible is premature."),
        ("What is the nurse&rsquo;s role when a patient has had several major abdominal operations?",
         ["Decide PD is contraindicated", "Ignore it", "Order imaging", "Document the history and route the suitability question to the nephrologist"], 3,
         "Suitability belongs to the nephrologist. Your part is an accurate history routed to the right person."),
        ("What does assisted PD mean in the 2024 ISPD position paper?",
         ["Only hospital-based PD", "PD done by the nephrologist", "PD without a catheter", "Help with PD tasks from family, paid caregivers or health workers, temporary or long term"], 3,
         "Assistance is defined broadly and can be short term, such as after a hospital stay, or long term."),
        ("Mr. Rolando&rsquo;s ground floor floods each rainy season. What is the best readiness action?",
         ["Write &ldquo;unsuitable home&rdquo;", "Move storage and the exchange corner upstairs, keep a reserve supply before typhoon season, and confirm at follow-up", "Tell him to buy a new house", "Store supplies under the stairs as planned"], 1,
         "Name the barrier, the fix and how you will verify it. A flood-prone ground floor is a storage and location problem, not a reason to deny PD."),
        ("Which documentation best reflects a remediable barrier?",
         ["&ldquo;Not suitable.&rdquo;", "&ldquo;Family will handle.&rdquo;", "Barrier, owner, action, observable criterion, reassessment date", "&ldquo;Discussed.&rdquo;"], 2,
         "It names who does what and how success will be checked. The others give the next nurse nothing to act on."),
    ],
    "terms": [("Peritoneal dialysis (PD)", "Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter."),
              ("APD", "Automated peritoneal dialysis: a cycler performs exchanges, usually overnight."),
              ("CAPD", "Continuous ambulatory peritoneal dialysis: manual exchanges through the day."),
              ("Cycler", "The machine that performs APD exchanges."),
              ("Peritonitis", "Infection or inflammation of the peritoneum, usually shown by cloudy effluent."),
              ("Shared decision-making", "Weighing the person&rsquo;s goals and the team&rsquo;s evidence together to reach a choice."),
              ("Remediable barrier", "An obstacle that support, equipment or a different helper can remove."),
              ("Teach-back", "Asking the learner to explain in their own words, to check understanding."),
              ("Assisted PD", "PD in which a family member, paid caregiver or health worker performs some tasks.")],
    "readings": [("peritoneal-dialysis-ckd.html", "Plain-language PD explanation to use in modality conversations."),
                 ("starting-dialysis-new-beginning.html", "Helping patients face the start of dialysis."),
                 ("incremental-dialysis.html", "Starting with the kidney function the patient still has.")],
    "calcs": ["calc-starting-dialysis-planner.html", "calc-dialysis-continuity-planner.html", "calc-frailty-assessment.html"],
}
