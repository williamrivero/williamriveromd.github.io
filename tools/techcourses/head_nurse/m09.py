# -*- coding: utf-8 -*-
"""Dialysis Head Nurse, Module 09: Partnering With Patients. Written for this series from published sources."""

MODULE = {
    "image_alt": "A head nurse sitting at eye level with a patient in a dialysis chair, listening, the patient's daughter beside them.",
    "objectives": [
        "Explain why skipping or shortening sessions harms patients, using the physiology from Modules 2 and 3.",
        "Summarize what predicts missed sessions, and why much of it lies in systems.",
        "Find the real reason a patient shortens or skips treatment, and bring in the person who can help.",
        "Teach with teach-back, and say how strong the evidence for it is.",
        "Ask two routine questions each month and use the answers.",
        "Track every referral until an outcome is recorded.",
    ],
    "big": """
{{plain:When a patient shortens or skips a session, the chart often says &ldquo;non-adherent.&rdquo; Replace that word with a question: what is competing with dialysis today?}}
<p>Dialysis takes about 600 hours a year in the chair, plus travel and recovery. It competes with a job, a child, a ride, the cost of the ride, pain, fear, and exhaustion. A patient who leaves early is usually making a rational trade with information you do not have yet.</p>
<p>The picture has a limit. Some patients do decide, with full information, to shorten or stop dialysis. That is their right. Your work is to make sure the decision is informed, assessed, and documented, not assumed.</p>
{{fig:hn09_compete}}
{{cards:Key terms for this module|Teach-back::Asking the patient to explain or show what was taught, so that gaps become visible.|Health literacy::The ability to find, understand, and use health information.|Recovery time::How long a patient takes to feel normal after a session.|Referral::A request for another service, such as transplant assessment, the dietitian, or social work.|Shared decision::A decision made with the patient, using their goals and the evidence.|Conservative care::Kidney care without dialysis, focused on symptoms and quality of life.}}
""",
    "case": {"title": "The last affordable ride", "html": """
<p>Mr. Danilo Ramos, 49, works as a security guard and dialyzes on the afternoon shift. In three weeks he has signed off early three times, each time about 45 minutes before the end. The nurses have recorded &ldquo;refused full treatment.&rdquo; His weight gain is 3.8 kilograms on a dry weight of 68 kilograms.</p>
<p>When you sit down with him, he says: &ldquo;The last jeepney that goes past my barangay leaves at 5:30. If I miss it, the tricycle costs me 250 pesos. I can&rsquo;t pay that three times a week.&rdquo;</p>
""", "questions": ["What is the actual problem, and who can help solve it?",
                  "What will you show Mr. Ramos, and how?",
                  "What do you change in the chart, and how do you know the plan worked?"]},
    "sections": [
        ("why", "Why it matters", "Why skipping and shortening matter", """
<p>Modules 2 and 3 explained the physiology. Skipping lengthens the gap, so potassium and fluid climb. Shortening removes diffusion time and forces the same fluid off faster.</p>
<p>What the patient feels is the result: breathlessness before sessions, cramps and a washed-out afternoon after them. Many patients do not connect the washed-out feeling with the speed of fluid removal. Making that link in plain words is often the most persuasive thing you can teach, because it trades something they feel for something they can change.</p>
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>Data</th><th>Strength</th></tr></thead>
<tbody>
<tr><td>Missed sessions</td><td>Associated with 68% higher mortality. Four-month risk of missing ranged from under 1% to 24% between countries. Longer travel time and depressive symptoms predicted it[[hn_alsalmi2018]]</td><td>Cohort</td></tr>
<tr><td>Skipping</td><td>Associated with 30% higher mortality and more hospital admission[[hn_saran2003]]</td><td>Cohort</td></tr>
<tr><td>Storms</td><td>Tropical storm exposure was associated with 55% higher risk of a missed session over the following week[[hn_remigio2023]]</td><td>Cohort</td></tr>
<tr><td>Health literacy</td><td>In 480 new patients, 32% had limited health literacy, which was associated with higher mortality (hazard ratio 1.54)[[hn_cavanaugh2010]]</td><td>Cohort</td></tr>
</tbody></table></div>
<p>A fiftyfold difference between countries cannot be explained by patient character. It points to transport, scheduling, cost, and support, which is where you can act. You cannot tell by looking which patients have limited health literacy, so teach everyone as if they might.</p>
{{scene:The washed-out afternoon|<p>Mrs. Linda Soriano, 57, tells her nurse that she &ldquo;loses the whole afternoon&rdquo; after dialysis. She lies down when she gets home and cannot cook dinner. She thinks this is just how dialysis is.</p>
<p>Her weight gains are often 4 kilograms on a dry weight of 55, so her machine removes about 18 mL/kg/h over four hours. The nurse explains in plain words: &ldquo;When the machine has to take off a lot of water in a short time, your blood pressure drops and your body has to work hard to catch up. That is part of why you feel washed out. If you come in carrying less water, the machine can go gentler.&rdquo; The nurse brings in the dietitian to talk about salt and thirst. Six weeks later, Mrs. Soriano&rsquo;s gains average 2.8 kilograms, and she says she can cook dinner on dialysis days again. She did not change her habits because she was told to. She changed them because she could feel the difference.</p>}}
"""),
        ("ask", "Ask first", "Ask before you teach", """
<p>&ldquo;What makes it hard to stay the full time?&rdquo; Then be quiet. Typical answers, and who can act:</p>
<div class="table-wrap"><table>
<thead><tr><th>Barrier</th><th>Who to bring in</th><th>Possible moves</th></tr></thead>
<tbody>
<tr><td>Last affordable ride leaves early</td><td>Scheduling, social worker, family</td><td>An earlier shift, shared transport, local government or charity transport help</td></tr>
<tr><td>Work hours</td><td>Scheduling, a letter to the employer</td><td>A different shift or days</td></tr>
<tr><td>Cramps or feeling ill in the last hour</td><td>Attending nephrologist</td><td>Review dry weight, fluid removal rate, and time. This is a prescription problem, not an adherence problem</td></tr>
<tr><td>Cost</td><td>Billing, social worker, PhilHealth desk</td><td>Confirm dialysis database registration and remaining sessions (Module 10), medical assistance programs</td></tr>
<tr><td>Low mood, hopelessness</td><td>Attending nephrologist, mental health referral</td><td>Screen, refer, follow up</td></tr>
<tr><td>Needle pain or fear</td><td>Senior cannulator, nephrologist</td><td>A consistent cannulator, numbing cream if ordered</td></tr>
</tbody></table></div>
{{scene:Better off without me|<p>Mr. Arturo Valdez, 58, has missed two Fridays this month. When the nurse asks what makes it hard to come, he says quietly, &ldquo;My children are paying for all of this. They would be better off without the expense.&rdquo;</p>
<p>That sentence is not a scheduling problem. It may be hopelessness, and it is one of the triggers in this module for calling the attending nephrologist the same day. The nurse thanks him for saying it, stays with him, and tells you. You call the nephrologist, who speaks with Mr. Valdez before he leaves, arranges a referral for support, and asks the social worker to look at coverage. You document what he said, in his words, and who was told. Asking &ldquo;What makes it hard?&rdquo; is how this came out. A note that said &ldquo;missed sessions, counseled&rdquo; would have missed it.</p>}}
{{call:Stop and call the attending nephrologist when a patient has shortened or missed two or more sessions in a month, when a patient expresses hopelessness or a wish to stop dialysis, or when cramps or low pressure are driving early sign-off. Follow your unit&rsquo;s protocol while you call.}}
"""),
        ("teach", "Teach-back", "Teaching that you can check", """
{{fig:hn09_teachback}}
{{flow:Teach-back in three steps|Explain::One thing, in plain words. &ldquo;If potassium gets too high, the heart can stop without warning.&rdquo;|Ask back::Check yourself, not the patient. &ldquo;I want to be sure I explained that well. If you miss Friday, what would you watch for, and what would you do?&rdquo;|Fix and ask again::Correct the gap and ask once more. Record the topic and what the patient said.}}
<p>&ldquo;Do you understand?&rdquo; almost always gets a yes. It measures politeness, not understanding.</p>
<p>The evidence for teach-back is modest. A systematic review in kidney disease found six studies with 520 participants and some evidence of better self-management, self-efficacy, and knowledge, but limited evidence for quality of life, and the studies were too different to combine.[[hn_jagodage2024]] A broader review in chronic disease found similar results.[[hn_hadinh2016]] The method costs nothing and has no known harm, which is why it is recommended despite the limited evidence.</p>
<p>Use the patient&rsquo;s language. Offer the site&rsquo;s Tagalog, Cebuano, or Kapampangan materials where reviewed translations exist. Bring in the family member who cooks and the one who drives.</p>
{{scene:The answer that needed fixing|<p>The nurse explains to Mr. Gregorio Lopez that if he misses a session, potassium builds up and can make the heart beat dangerously. Then she asks, &ldquo;I want to be sure I explained that well. If you miss Friday, what would you do?&rdquo;</p>
<p>Mr. Lopez says, &ldquo;I&rsquo;d drink more water to flush it out.&rdquo; That is the opposite of safe, and &ldquo;Do you understand?&rdquo; would never have revealed it. The nurse corrects it gently: &ldquo;Without kidneys, water doesn&rsquo;t flush potassium out. It just adds to the fluid. If you miss a session, call us to come in as early as possible, avoid fruits like banana, and go to the emergency room if you feel weak or your heart is racing.&rdquo; Then she asks again, and he says it back correctly. She records the topic and his answer.</p>}}
"""),
        ("monthly", "Two questions", "Two questions every month", """
<p>&ldquo;How long does it take you to recover after a session?&rdquo; One patient in ten takes more than twelve hours, and longer recovery was associated with hospital admission and death.[[hn_rayner2014]] &ldquo;What symptom bothers you most?&rdquo; Routine electronic symptom checks with feedback to clinicians are feasible in dialysis units and take under seven minutes.[[hn_agarwal2023]] Whether they improve outcomes is still being tested.</p>
<p>Record both answers and bring them to the monthly review with the nephrologist and dietitian.</p>
{{scene:Sixteen hours|<p>At the monthly review, Mr. Simeon Bautista answers the first question: &ldquo;It takes me until the next morning to feel normal. Maybe sixteen hours.&rdquo; He has never mentioned it, because no one asked.</p>
<p>His records show weight gains of 3.5 to 4 kilograms and frequent cramping in the last hour. The nurse brings both to the nephrologist with his recovery time. The nephrologist adds thirty minutes to his sessions and asks the dietitian to see him. Two months later, he says he feels normal by evening. The question took ten seconds. Without it, his long recovery would have stayed invisible, because nothing in the machine records it.</p>}}
"""),
        ("referral", "Referrals", "Options, and closing referrals", """
<p>Every patient should have a documented conversation about transplant and peritoneal dialysis, and where appropriate about conservative care. Staffing touches this too: in young patients, the most stretched nursing quartile was associated with 14% lower incidence of transplant.[[hn_bicki2024]] Referral work is among the tasks left undone.</p>
{{fig:hn09_referral}}
<p>Track each referral to an outcome: referred, seen, decision, next step. A referral with no recorded outcome is still open.</p>
<p><strong>When a patient wants to leave early.</strong> Signing off early is the patient&rsquo;s right. Leaving without being assessed is the unit&rsquo;s failure. Assess symptoms, explain the specific risk in plain words, confirm the next session, inform the physician, and document the conversation. In a conflict, lower your voice, acknowledge the concern, state the safety boundary, offer the options that exist, and call for support if there is any threat.</p>
{{scene:Leaving at three hours, done properly|<p>At three hours, Mrs. Teresa Garcia asks to stop because her grandson&rsquo;s school program starts at 5:00. The nurse does not argue and does not simply disconnect.</p>
<p>She checks Mrs. Garcia&rsquo;s pressure and symptoms, and explains: &ldquo;You still have about 800 mL of fluid that we planned to remove. Leaving now means you start the weekend carrying it, which can make you short of breath by Sunday.&rdquo; She tells the physician, confirms Monday&rsquo;s session, and agrees with Mrs. Garcia that she will come early on Monday. She writes down what was said, the actual minutes and fluid removed, and the reason. Mrs. Garcia leaves for the program. The record shows an informed choice, not a refusal.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>The actual problem.</strong> Transport and cost, recorded as refusal. Ask Mr. Ramos&rsquo;s permission to work on it with him. Scheduling may have a morning or midday slot that fits his work. The social worker may know of transport help from the barangay, the city, or a charity. The nephrologist needs to know about three shortened sessions now, because the plan may need to change while the transport problem is solved.</p>
<p><strong>What you show him.</strong> His fluid removal rate at the full time and at the time he actually stays. With 3.8 liters on 68 kilograms over four hours, the rate is about 14 mL/kg/h. Over three hours and fifteen minutes, it is about 17. Ask whether he feels washed out after sessions, and link the feeling to the number. Then use teach-back on the agreed plan.</p>
<p><strong>The chart and the check.</strong> Change &ldquo;refused&rdquo; to what happened: &ldquo;Signed off 45 minutes early because of transport. Transport and schedule options under review with social work.&rdquo; Name who will check that the next session ran to time, and close the issue only when it has.</p>
"""],
    "skills": {"title": "Patient conversation and handoff",
               "intro": "Role-play the conversation with a facilitator playing the patient, then hand off to scheduling and social work.",
               "items": [
                   ("Asks permission and sits at eye level.", False),
                   ("Asks an open question about what makes it hard to stay, and listens.", True),
                   ("Names the barrier in the patient&rsquo;s own words.", True),
                   ("Avoids the words non-adherent and refused unless accurate.", False),
                   ("Identifies who can help with the barrier.", True),
                   ("Informs the nephrologist of repeated shortened sessions.", True),
                   ("Uses teach-back on the plan and repairs any gap.", True),
                   ("Asks the recovery-time question and records the answer.", False),
                   ("Records an owner and a follow-up date.", True),
               ],
               "placement": "For one month, review every session signed off early or missed on your shifts. For each, record the reason the patient gave and the action taken. Discuss the pattern with your facilitator."},
    "quiz": [
        ("What question should replace the word non-adherent?",
         ["Why won&rsquo;t you cooperate?", "What is competing with dialysis today?", "Do you understand the risks?", "Who told you to leave?"], 1,
         "Most early sign-offs are trades with information the team does not yet have."),
        ("What did DOPPS find about missed sessions?",
         ["No effect on survival", "An association with 68% higher mortality", "Fewer admissions", "Lower potassium"], 1,
         "Longer travel time and depressive symptoms predicted missing."),
        ("Why does a fiftyfold difference between countries matter?",
         ["It shows some nationalities are less disciplined", "It points to systems such as transport, scheduling, and cost", "It proves the data are wrong", "It means missing is harmless"], 1,
         "Patient character cannot explain that range."),
        ("A patient cramps every session in the last hour and leaves early. What kind of problem is this?",
         ["An adherence problem", "A prescription problem to raise with the nephrologist", "A behavior problem", "A billing problem"], 1,
         "Review dry weight, rate, and time."),
        ("How is teach-back different from asking &ldquo;Do you understand?&rdquo;",
         ["It is faster", "The patient explains or shows the plan, so gaps become visible", "It is required by PhilHealth", "It replaces written material"], 1,
         "A yes to &ldquo;Do you understand?&rdquo; measures politeness."),
        ("How strong is the evidence for teach-back in kidney disease?",
         ["Strong, from large trials", "Modest, from six small and varied studies", "None", "It has been shown to harm"], 1,
         "It is used because it is free, harmless, and shows what was not understood."),
        ("What fraction of new hemodialysis patients had limited health literacy in the Cavanaugh study?",
         ["About 5%", "About a third", "About two thirds", "All of them"], 1,
         "32%, and it was associated with higher mortality."),
        ("Tropical storm exposure was associated with what change in missed sessions?",
         ["No change", "About 55% higher risk over the following week", "Fewer missed sessions", "Higher risk only on the same day"], 1,
         "Plan for this every rainy season."),
        ("Which routine question has outcome data behind it?",
         ["Do you like your nurse?", "How long does it take you to recover after a session?", "Did you eat today?", "Do you have questions?"], 1,
         "Longer recovery was associated with admission and death."),
        ("Who individualizes nutrition advice?",
         ["The head nurse", "The renal dietitian and clinical team, with nurses reinforcing it", "The family", "The patient alone"], 1,
         "Nurses reinforce the agreed plan."),
        ("When is a referral closed?",
         ["When it is sent", "When an outcome is recorded", "After one month", "When the patient agrees"], 1,
         "A referral without a recorded outcome is still open."),
        ("A patient wants to sign off early. What must happen?",
         ["Nothing, it is their right", "Assess symptoms, explain the specific risk, confirm the next session, inform the physician, and document", "Refuse to disconnect", "Call security"], 1,
         "Signing off is the patient&rsquo;s right. Leaving unassessed is the unit&rsquo;s failure."),
        ("A patient says he feels there is no point continuing dialysis. What do you do?",
         ["Change the subject", "Listen, and inform the attending nephrologist promptly", "Tell him to be strong", "Note it at the end of the month"], 1,
         "Hopelessness and a wish to stop need the nephrologist&rsquo;s attention."),
        ("How should a chart entry read when a patient left early because of transport?",
         ["Refused full treatment", "Signed off early because of transport, options under review, with an owner", "Non-compliant", "Left against advice"], 1,
         "Accurate words lead to the right fix."),
        ("Which staffing finding relates to referrals?",
         ["More nurses lowered Kt/V", "The most stretched nursing quartile was associated with lower incidence of transplant", "Staffing had no association with anything", "Fewer nurses improved attendance"], 1,
         "Referral work is among the tasks left undone."),
    ],
    "terms": [("Teach-back", "Asking the patient to explain or show what was taught."),
              ("Health literacy", "The ability to find, understand, and use health information."),
              ("Recovery time", "How long a patient takes to feel normal after a session."),
              ("Referral", "A request for another service, tracked until an outcome is recorded."),
              ("Shared decision", "A decision made with the patient, using their goals and the evidence."),
              ("Conservative care", "Kidney care without dialysis, focused on symptoms and quality of life."),
              ("Peritoneal dialysis", "Dialysis using the lining of the abdomen, usually done at home."),
              ("Barangay", "The smallest administrative unit in the Philippines, often a source of local transport help.")],
    "readings": [("starting-dialysis-new-beginning.html", "Living well on dialysis."),
                 ("fluid-management-dialysis.html", "Salt and fluid advice in plain language."),
                 ("hemodialysis-modalities.html", "Treatment options to discuss with patients.")],
    "calcs": ["calc-dialysis-head-nurse-toolkit.html#c2", "calc-dialysis-head-nurse-toolkit.html#c12"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("hn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
