# -*- coding: utf-8 -*-
"""Peritoneal Dialysis Nurse, Module 09: Teach, validate and retrain.
Rewritten in the Renal Care Academy POD voice, with illustrative scenarios. Every patient and nurse is fictional. Edit here."""

MODULE = {
    "image_alt": "",
    "objectives": [
        "Apply adult-learning principles, health-literacy practice and teach-back to peritoneal dialysis (PD) training.",
        "Describe what the 2025 International Society for Peritoneal Dialysis (ISPD) position paper on teaching PD recommends and how strong that evidence is.",
        "Build an individualized training plan that names who performs each task.",
        "Judge readiness by independent return demonstration of critical steps and correct responses to common problems.",
        "Identify retraining triggers and schedule reassessment.",
    ],
    "big": """
<p>A PD nurse trainer is the single most important safety device in a home program. The patient will perform hundreds of exchanges alone. The technique they leave training with is the technique they will use at 3 AM when they are tired, in a hurry or unwell.</p>
<p>Your work is not to deliver information. It is to produce safe, durable performance, to verify it by watching, and to come back when it drifts. A patient who can recite the steps but cannot do them without a reminder is not ready, however many sessions they attended.</p>
{{plain:Think of learning to drive. Reading the manual does not make a driver. Practice with a coach does, and the license is given after an examiner watches you drive without help.}}
<p>The picture has a limit. A driving license lasts years. PD technique drifts within months, especially after illness, a new caregiver or a new device. Readiness is renewed, not awarded once.</p>
{{cards:Key terms for this module|Teach-back::Asking the learner to explain in their own words, to check understanding.|Return demonstration::The learner performs the skill while the trainer watches.|Critical step::A step whose failure could directly harm the patient, such as protecting the connector.|Retraining trigger::An event that calls for reassessing technique.|Health literacy::A person&rsquo;s ability to find, understand and use health information.}}
""",
    "case": {"title": "Two reminders", "html": """
<p><strong>Liza</strong>, 35, is learning cycler setup so she can run her father Mang Ernesto&rsquo;s APD each night (see Module 2). She works days in Manila, so Nurse <strong>Joy</strong> trains her in the evenings, after Liza&rsquo;s two-hour commute.</p>
<p>On the third evening, Liza completes the whole setup correctly. Twice, though, Joy has to remind her not to rest the connector on the table. Liza is tired and apologetic. &ldquo;I know it, ma&rsquo;am. I just forgot.&rdquo; Mang Ernesto&rsquo;s home start is scheduled for Saturday.</p>
""", "questions": ["Is Liza ready to do this alone at home?",
                  "What do you do right now, and when do you check again?",
                  "What teach-back question would you ask?"]},
    "sections": [
        ("what-the-evidence", "The evidence", "What the evidence shows", """
<h3>The 2025 ISPD position paper on teaching PD</h3>
<p>The paper builds on two earlier ISPD publications, including the 2016 syllabus for teaching PD to patients and caregivers. It acknowledges a lack of high-certainty evidence in teaching PD. It offers practice points across five areas: the PD nurse trainer&rsquo;s education, knowledge, skills and attributes; preparation for training; methods of training and educational interventions; follow-up after training; and measures of outcomes.[[pd_chow2025]][[pd_figueiredo2016]] Treat its advice as carefully assembled expert consensus, not as trial-proven.</p>
<h3>Training duration</h3>
<p>In the Peritoneal Dialysis Outcomes and Practice Patterns Study (PDOPPS), with 7,051 adults in 209 facilities across seven countries, facilities whose PD training lasted 6 or more days had lower peritonitis risk than those with shorter training (rate ratio 0.81, 95% confidence interval 0.68 to 0.96).[[pd_perl2020]] This is observational and measured at the facility level. Longer training may mark better-resourced programs rather than cause fewer infections. It is still a useful benchmark when a unit is under pressure to shorten training to free a slot.</p>
<h3>Training and reassessment</h3>
<p>The 2022 ISPD peritonitis recommendations revised their guidance on PD training and reassessment.[[pd_li2022]] In the United States, federal conditions for dialysis facilities require home-training programs to cover technique, emergency procedures and retraining, delivered by a qualified registered nurse.[[pd_cfr494100]] These rules do not bind Philippine units, but they offer a documented comparison when your unit writes its own policy.</p>
{{key:Teaching PD rests mostly on expert consensus and observational data. Use it, and say so honestly.}}
"""),
        ("principles-that-work", "Principles", "Principles that work", """
{{fig:pd09_cycle}}
<div class="table-wrap"><table>
<thead><tr><th>Principle</th><th>In practice</th></tr></thead>
<tbody>
<tr><td>Adults learn for a purpose</td><td>Link each skill to what the person wants: &ldquo;This is how you keep the catheter that lets you keep working.&rdquo;</td></tr>
<tr><td>Small chunks</td><td>One goal per session; build the sequence over days</td></tr>
<tr><td>Demonstrate on the real system</td><td>Use the device they will use at home, or an equivalent training model</td></tr>
<tr><td>Practice with coaching, then without</td><td>Prompts fade as competence grows</td></tr>
<tr><td>Teach-back</td><td>&ldquo;Tell me in your own words what you would do if the bag is cloudy.&rdquo; Not &ldquo;Do you understand?&rdquo;</td></tr>
<tr><td>Return demonstration</td><td>Full exchange or cycler setup with no prompts, observed</td></tr>
<tr><td>Health literacy</td><td>Plain words, pictures, simple numbers; Tagalog or the local language; interpreters when needed</td></tr>
<tr><td>Accessibility</td><td>Large print, high contrast, audio, tactile cues for low vision; adapted grips for weak hands</td></tr>
<tr><td>Emotional safety</td><td>Mistakes in training are expected and welcome; hiding errors at home is the real danger</td></tr>
</tbody></table></div>
<h3>Example: the learner who nods</h3>
<p>Mang Fred, 67, finished grade 4 and reads slowly. He nods at every explanation and says &ldquo;opo&rdquo; to every question. On day two, Nurse Joy stops asking &ldquo;Do you understand?&rdquo; and starts asking him to show her. He cannot find the strength printed on the bag. She switches to a picture checklist with large color photos of each step and a color sticker on each strength, matched to his prescription card. By day four he completes the sequence alone, pointing at each photo as he goes.</p>
<p>Nothing about Mang Fred was unteachable. The first method simply depended on reading, and he was too polite to say so.</p>
<h3>Example: the right language</h3>
<p>Lola Basing speaks Ilocano and only a little Tagalog. Her grandson translates during training but works abroad from next month. Joy arranges for the unit&rsquo;s Ilocano-speaking midwife to join two sessions, records the cloudy-bag instruction in Ilocano on the family&rsquo;s phone, and writes the PD hotline number in large print beside the exchange table.</p>
{{key:Ask the learner to show you, not to tell you they understand. Politeness hides confusion.}}
"""),
        ("build-the-plan", "Build the plan", "Build the plan", """
<ol>
<li><strong>Who does each task?</strong> Patient, caregiver, both, or an assistant. Train the person who will actually do it.</li>
<li><strong>Assess the learner.</strong> Language, reading, vision, hearing, dexterity, memory, prior experience, confidence, schedule, stress.</li>
<li><strong>Set session goals.</strong> One main goal per session.</li>
<li><strong>Teach the problems, not only the routine.</strong> Cloudy effluent, contamination, poor drain, leak, fever, missed therapy, power failure, supply delay.</li>
<li><strong>Plan the home start.</strong> The first home exchange observed, or followed by an early call; a home visit when feasible.</li>
</ol>
<h3>Example: a six-session plan for CAPD</h3>
<div class="table-wrap"><table>
<thead><tr><th>Session</th><th>Main goal</th><th>Problem taught that day</th></tr></thead>
<tbody>
<tr><td>1</td><td>Hand hygiene and setting up the clean area</td><td>What to do if interrupted</td></tr>
<tr><td>2</td><td>Checking the order and supplies; rejecting a defective bag</td><td>A leaking or expired bag</td></tr>
<tr><td>3</td><td>Connection, drain, flush and fill with prompts</td><td>Dry contamination</td></tr>
<tr><td>4</td><td>Full exchange with fading prompts; recording volumes</td><td>Wet contamination and the call</td></tr>
<tr><td>5</td><td>Full exchange without prompts; exit-site care</td><td>Cloudy effluent; poor drain</td></tr>
<tr><td>6</td><td>Independent exchange, observed; teach-back on all problems</td><td>Missed exchange; power or water outage; supply delay</td></tr>
</tbody></table></div>
<p>The sessions are a plan, not a deadline. If a learner meets session 6 goals on day 5, good. If they need eight sessions, they need eight. The PDOPPS observation about training of 6 days or more is a benchmark for the program, not a quota for each learner.</p>
"""),
        ("judge-readiness", "Judge readiness", "Judge readiness", """
<p>Check that the learner can, without prompting:</p>
<ul>
<li>Verify the order and supplies, and reject a defective bag.</li>
<li>Perform hand hygiene and prepare the area.</li>
<li>Protect critical connections throughout.</li>
<li>Complete the exchange or cycler setup and disconnection.</li>
<li>Inspect the effluent and record volumes and observations.</li>
<li>State the action for cloudy fluid, contamination, poor drain and missed therapy, including whom to call.</li>
</ul>
<p><strong>Require independently safe execution of every critical step before home readiness sign-off, under program policy.</strong> Record what was performed, cues needed, gaps, supports and the reassessment date.</p>
<h3>Example: two notes for the same session</h3>
<div class="table-wrap"><table>
<thead><tr><th>Weak note</th><th>Useful note</th></tr></thead>
<tbody>
<tr><td>&ldquo;Trained. Ready for home.&rdquo;</td><td>&ldquo;Caregiver (daughter) completed cycler setup and connection unprompted, all critical steps safe. Teach-back correct for cloudy bag, wet contamination and power failure. Adaptations: desk lamp, picture checklist. Patient states hotline number. Reassess at first home visit, day 3.&rdquo;</td></tr>
</tbody></table></div>
<h3>When pressure meets readiness</h3>
<p>Sometimes the home start date is fixed, a supplier delivery is booked or a hospital bed is needed. None of these changes what safe looks like. If a critical step still needs prompting, the honest options are another session, a supervised first week at home with daily calls, or temporary assistance. Signing off early moves the risk from your schedule to the patient&rsquo;s abdomen.</p>
{{key:Sign off what you saw done safely without help. Not what you hope will happen at home.}}
"""),
        ("retraining-triggers", "Retraining", "Retraining triggers", """
<p>Reassess technique, and retrain as needed, when any of these occur:</p>
<ul>
<li>Peritonitis or exit-site infection</li>
<li>A contamination event</li>
<li>Technique drift observed at a visit</li>
<li>A change of device or system</li>
<li>A change of caregiver or assistant</li>
<li>Hospitalization or major illness</li>
<li>A major change in vision, cognition, dexterity or home situation</li>
<li>Return after a long break from PD</li>
<li>The program&rsquo;s scheduled interval, even without problems</li>
</ul>
<h3>Example: the caregiver who left</h3>
<p>Mrs. Corazon&rsquo;s daughter, who did her cycler setup every night, has accepted work as a caregiver in Hong Kong. Her son will take over. Mrs. Corazon assumes he can learn by watching his sister for a week.</p>
<p>The son is a new learner with his own needs. Nurse Joy assesses him, trains him for his role, watches him set up the cycler without help, and documents his readiness before his sister leaves. She also asks who covers when he works late. A change of caregiver is a retraining trigger, and a departure date gives you a deadline to plan around.</p>
<h3>Example: drift after a good year</h3>
<p>At a routine home visit, Mr. Arturo, a year into CAPD with no peritonitis, skips the mask the program requires and rests the cap on the table during the fill. He has not had a problem, so the shortcuts felt safe. Joy watches a full exchange, names the two drifts without scolding, retrains the steps and books a recheck. Drift is normal. Catching it is the job.</p>
{{key:A good year is not proof of good technique. Watch a full exchange at scheduled visits.}}
{{fig:pd09_fig_09_retraining_triggers_nine}}
"""),
    ],
    "debrief": ["""
<p><strong>Is Liza ready?</strong> Not yet. She completed the setup, but a critical step, protecting the connector, needed two prompts. Independence means every critical step done safely without help.</p>
<p><strong>What Joy does now.</strong> She names the steps Liza did well, then demonstrates the connector step once more, slowly, explaining why: the connector&rsquo;s tip must never touch anything, because whatever touches it can reach her father&rsquo;s abdomen. She has Liza practice that step alone three times. She schedules another unprompted full setup two evenings later. She does not sign Liza off as independent that night, and she tells the nephrologist and the supplier that the home start may move.</p>
<p><strong>The next session.</strong> Liza completes the setup unprompted. Joy asks: &ldquo;What would you do if the morning drain bag is cloudy?&rdquo; Liza answers: &ldquo;Keep the bag, call the PD unit right away, and bring Papa in.&rdquo; Joy asks a second question: &ldquo;And if your sleeve touches the connector?&rdquo; &ldquo;Stop, clamp, call.&rdquo;</p>
<p><strong>The record.</strong> Joy documents independent performance, both teach-backs, the adaptations (lamp, picture checklist) and a reassessment at the first home visit. The home start goes ahead on Monday instead of Saturday. Two days cost nothing; a contaminated connection could have cost the catheter.</p>
"""],
    "skills": {"title": "Teaching a learner with limited vision (OSCE station 5)",
               "intro": "Teach a simulated patient with limited reading fluency using demonstration and a picture checklist. Ask them to explain what they would do if effluent becomes cloudy. Faculty scores against OSCE station 5.",
               "items": [("Assesses barriers and preferences.", False),
                         ("Demonstrates and adapts instruction.", False),
                         ("Observes an independent return demonstration.", False),
                         ("Withholds readiness sign-off after unsafe performance.", True),
                         ("Specifies coaching, support and a reassessment date.", False)]},
    "quiz": [
        ("What evidence best supports independent competence?",
         ["Correct return demonstration without prompts, including critical steps and responses to common problems", "The learner says they understand", "Attendance at all sessions", "A signed form"], 0,
         "Readiness is shown, not stated. Attendance and signatures do not show performance."),
        ("Which question is a true teach-back?",
         ["&ldquo;Do you understand?&rdquo;", "&ldquo;Any questions?&rdquo;", "&ldquo;Tell me in your own words what you would do if the bag is cloudy.&rdquo;", "&ldquo;Okay?&rdquo;"], 2,
         "Teach-back asks the learner to explain in their own words. Yes-or-no questions invite a polite yes."),
        ("How does the 2025 ISPD teaching position paper characterize its evidence?",
         ["High-certainty randomized evidence", "Regulations", "Withdrawn", "Practice points, acknowledging a lack of high-certainty evidence"], 3,
         "It is expert consensus. Use it, and describe it honestly."),
        ("In PDOPPS, facility training of 6 or more days was:",
         ["Proven by trial to prevent peritonitis", "Associated with lower facility peritonitis risk (rate ratio 0.81)", "Associated with higher risk", "Not studied"], 1,
         "Observational and facility-level. It may reflect better-resourced programs."),
        ("A caregiver completes a setup correctly only after reminders about the connector. Best action?",
         ["Sign off as independent", "Reinforce, demonstrate the critical step, and schedule another unprompted check before assigning the task at home", "Stop training", "Let the patient do it instead without assessment"], 1,
         "A critical step that needs prompting is not yet independent."),
        ("Mrs. Corazon&rsquo;s son will replace his sister as her caregiver. What is needed?",
         ["Nothing; he watched his sister", "The patient retrains alone", "A new prescription", "Assess his needs, train him for his role, observe his performance and document readiness before his sister leaves"], 3,
         "A change of caregiver is a retraining trigger. Watching is not the same as doing."),
        ("Which is a retraining trigger?",
         ["Peritonitis", "A birthday", "A sunny day", "A new television"], 0,
         "Peritonitis, exit-site infection, contamination, drift, a device or caregiver change and hospitalization all trigger reassessment."),
        ("Which training method best fits adult learners?",
         ["One long lecture", "Reading the manual alone", "Short, purpose-linked sessions with demonstration and practice", "Video only, no practice"], 2,
         "Adults learn best in short sessions tied to what they want, with practice and coaching."),
        ("Why should training cover problems, not only routine steps?",
         ["To fill time", "Because problems never happen", "Because safe home care depends on recognizing and responding to cloudy fluid, contamination and poor drain", "For billing"], 2,
         "The routine keeps the patient well on good days. Problem responses keep them safe on bad days."),
        ("Mang Fred nods at every explanation but cannot find the strength on the bag. A suitable adaptation is:",
         ["A picture checklist and color-coded strength stickers, verified by watching him", "Smaller labels", "Skipping label checks", "Asking &ldquo;Do you understand?&rdquo; more often"], 0,
         "Adapt the method to the learner, then confirm by observation."),
        ("Why make mistakes in training feel safe?",
         ["To shorten training", "So learners hide errors less at home", "Because mistakes do not matter", "It is not important"], 1,
         "A learner afraid of blame hides contamination. Hidden contamination becomes peritonitis."),
        ("Who should be trained for a task?",
         ["Whoever is available that day", "Only the patient", "Only the nurse", "The person who will actually perform it at home"], 3,
         "Train the person who does the task, and plan a backup."),
        ("Which element belongs in readiness documentation?",
         ["Only &ldquo;trained&rdquo;", "The patient&rsquo;s income", "Nothing", "Performed steps, cues needed, gaps, supports and the reassessment date"], 3,
         "The next nurse needs to know what was seen, what helped and when to check again."),
        ("Mr. Arturo has had a year without peritonitis but now rests the cap on the table during fills. What is appropriate?",
         ["Ignore it; his record is good", "Name the drift without scolding, retrain the step and book a recheck", "Report him for noncompliance", "Change his catheter"], 1,
         "Drift is normal after months of success. Catching and correcting it is part of the job."),
        ("What does health literacy practice require?",
         ["Medical jargon", "Long written handouts only", "Plain language, pictures, simple numbers, the person&rsquo;s own language and checking understanding", "Speaking faster"], 2,
         "Meet the learner where they are, and check by watching."),
    ],
    "terms": [("Peritoneal dialysis (PD)", "Dialysis that uses the lining of the abdomen as the filter, with fluid run in and out through a catheter."),
              ("APD", "Automated peritoneal dialysis: a cycler performs exchanges, usually overnight."),
              ("CAPD", "Continuous ambulatory peritoneal dialysis: manual exchanges through the day."),
              ("Exit-site infection", "Purulent discharge at the exit site, with or without redness (ISPD 2023)."),
              ("Cycler", "The machine that performs APD exchanges."),
              ("Peritonitis", "Infection or inflammation of the peritoneum, usually shown by cloudy effluent."),
              ("Effluent", "Fluid drained from the abdomen after a dwell."),
              ("Teach-back", "Asking the learner to explain in their own words, to check understanding."),
              ("Return demonstration", "The learner performs the skill while the trainer observes."),
              ("Critical step", "A step whose failure could directly harm the patient."),
              ("Health literacy", "A person&rsquo;s ability to find, understand and use health information.")],
    "readings": [("peritoneal-dialysis-ckd.html", "The patient guide to peritoneal dialysis your learners will reinforce.")],
    "calcs": [],
}
