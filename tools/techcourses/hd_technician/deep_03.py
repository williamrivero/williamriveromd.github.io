# -*- coding: utf-8 -*-
"""Hemodialysis Technician track, Module 03: added lessons (options side by side, diet and fluid basics,
replies to common patient questions, missed and shortened treatments, distress and respectful communication)."""

ADD = {
"extra": [
(1, "sidebyside", "Options side by side", "Five options side by side: place, schedule, and daily work", """
{{plain:Patients ask practical questions: where, how often, how long, and who does the work. This table answers those in general terms. It does not say which option is best, because there is no single best option. The nephrologist and the patient decide which ones are possible and which one fits.}}
<div class="table-wrap"><table>
<thead><tr><th>Option</th><th>Where, and who does the work</th><th>Usual schedule</th><th>What the patient must do</th><th>Access or surgery</th><th>Often discussed when</th></tr></thead>
<tbody>
<tr><td>In-center hemodialysis</td><td>At the unit. Staff run the treatment</td><td>Commonly three sessions a week of about four hours each, as prescribed</td><td>Attend every session for the full time. Protect the access. Follow the diet, fluid, and medicine plan</td><td>A fistula, graft, or catheter</td><td>The patient wants or needs staff to perform treatment, or home is not suitable</td></tr>
<tr><td>Home hemodialysis</td><td>At home. The patient, often with a trained partner</td><td>Set by the home program; often shorter, more frequent sessions</td><td>Complete several weeks of training. Set up the machine, insert the needles, record each treatment, order supplies, and call the program when something goes wrong</td><td>The same access; the home needs space, water, and power</td><td>The patient wants a flexible schedule, can be trained, and a program is available</td></tr>
<tr><td>Peritoneal dialysis</td><td>At home or at work. The patient, by hand or with a machine called a cycler</td><td>Every day. By hand: commonly about four exchanges a day, each taking roughly 30 to 40 minutes. By cycler: overnight, commonly eight to ten hours</td><td>Complete training. Use strict clean technique at every connection. Care for the catheter exit site daily. Store boxes of solution</td><td>A soft catheter placed in the abdomen</td><td>The patient wants treatment without needles and has a clean space at home</td></tr>
<tr><td>Kidney transplant</td><td>Surgery in a transplant hospital, then clinic follow-up</td><td>No dialysis sessions while the kidney works. Frequent clinic visits at first, then regular visits for life</td><td>Take anti-rejection medicines every day, on time, for as long as the kidney works. Attend visits and blood tests. Report fever or illness early</td><td>Major surgery and a kidney from a living or deceased donor</td><td>The transplant team finds the patient fit for surgery and a donor kidney is available</td></tr>
<tr><td>Conservative care</td><td>Clinic and home. The care team, patient, and family</td><td>Regular visits. No dialysis</td><td>Take medicines, follow the diet, report symptoms, and plan ahead with the family</td><td>None</td><td>The patient chooses not to have dialysis, or dialysis is unlikely to help the person live longer or better</td></tr>
</tbody></table></div>
<p>Choices are not permanent. A patient may move from peritoneal dialysis to hemodialysis, from dialysis to a transplant, or back to dialysis if a transplant stops working.</p>
{{key:A safe sentence for any question about which option to choose: &ldquo;Each one has trade-offs. The doctor can go through which are possible for you. I will tell the nurse you want to talk about it.&rdquo;}}
"""),
(3, "dietfluid", "Diet and fluid basics", "Diet and fluid: what the dietitian and nurse teach, and how you support it", """
<p>The nephrologist and dietitian set each patient&rsquo;s diet and fluid plan, and the nurse reinforces it. You will hear about it at the chair every day. Your part is to understand the reasons, notice problems, and pass them on. You do not set or change the plan.</p>
<div class="table-wrap"><table>
<thead><tr><th>What is limited</th><th>Why</th><th>Foods and drinks the dietitian commonly discusses</th><th>How the technician supports</th></tr></thead>
<tbody>
<tr><td>Sodium (salt)</td><td>Salt causes thirst and holds water in the body, so weight gain and blood pressure rise</td><td>Fish sauce, soy sauce, shrimp paste, dried salted fish, instant noodles, canned and processed meats, seasoning cubes, salty snacks</td><td>Listen for thirst and salty food habits. Report large weight gains with the numbers</td></tr>
<tr><td>Potassium</td><td>A high level can disturb the heart rhythm without warning</td><td>Bananas, coconut water, oranges and fruit juices, dried fruit, tomatoes and tomato sauce, potatoes and other root crops. Salt substitutes, many of which are made from potassium</td><td>Tell the nurse if a patient mentions large amounts of these or a new salt substitute</td></tr>
<tr><td>Phosphate</td><td>A high level over time weakens bones, hardens blood vessels, and causes itching</td><td>Dark cola drinks, processed foods with phosphate additives, milk and cheese, organ meats, nuts, beans. Phosphate binder tablets are taken with meals</td><td>Tell the nurse if a patient says the binders are skipped or taken apart from meals</td></tr>
<tr><td>Fluid</td><td>With little or no urine, what is drunk stays in the body until the next treatment</td><td>Anything liquid at room temperature: water, coffee, soft drinks, soup broth, rice porridge, ice, gelatin, ice cream</td><td>Weigh accurately. Help the patient keep a fluid record if the nurse asks</td></tr>
</tbody></table></div>
<p>Protein is different. Patients on dialysis usually need enough protein, and the dietitian sets the amount. Never advise a patient to avoid protein foods.</p>
{{stop:Star fruit (balimbing) is harmful to people with kidney failure and can cause hiccups, confusion, and seizures. If a patient says he or she has eaten it or drunk its juice, tell the nurse immediately, even if the patient feels well.}}
<p><strong>Tracking fluid.</strong> The fluid allowance is the total volume the nephrologist permits in a day. Volumes below are approximate; containers differ, so the patient should measure his or her own cup and bowl once with a measuring cup.</p>
<div class="table-wrap"><table>
<thead><tr><th>Common serving</th><th>Approximate volume</th></tr></thead>
<tbody>
<tr><td>Regular glass of water</td><td>240 mL</td></tr>
<tr><td>Cup of coffee or tea</td><td>180 mL</td></tr>
<tr><td>Bowl of soup broth</td><td>200 mL</td></tr>
<tr><td>Bowl of rice porridge</td><td>250 mL, counted as fluid as the dietitian teaches</td></tr>
<tr><td>Canned soft drink</td><td>330 mL (read the label)</td></tr>
<tr><td>One ice cube</td><td>20 to 30 mL</td></tr>
<tr><td>Water to swallow medicines</td><td>30 to 60 mL each time</td></tr>
<tr><td>One tablespoon</td><td>15 mL</td></tr>
</tbody></table></div>
{{formula:<strong>Fluid left for the day</strong> = allowance &minus; total taken so far.<br>Example, with a fictional allowance of 1,000 mL: coffee 180 + water with medicines 60 + soup 200 + glass of water 240 + four ice cubes at 25 each, 100 + evening tea 180 = 960 mL. 1,000 &minus; 960 = 40 mL left.}}
{{cards:Thirst tips the nurse and dietitian commonly teach|Less salt::The most effective step, because salt drives thirst.|A small cup::The same number of drinks, less volume.|Ice::Lasts longer than water, but it is counted.|Rinse, do not swallow::Mouth rinses and tooth brushing ease a dry mouth.|Spread it out::Divide the allowance across the day.|Blood sugar::For patients with diabetes, high sugar causes thirst; they should discuss it with the doctor.}}
"""),
(3, "replies", "What to say", "Common patient questions: a helpful reply and where to refer", """
{{cards:Four habits for every question|Listen to the end::Do not answer the first half of a question.|Say what you can do::Even when the answer belongs to someone else.|Never guess::A confident wrong answer travels fast in a waiting room.|Close the loop::Tell the patient whom you told.}}
<div class="table-wrap"><table>
<thead><tr><th>The patient says</th><th>A helpful reply within your scope</th><th>Refer to</th></tr></thead>
<tbody>
<tr><td>&ldquo;Can I skip Saturday? We have a family event.&rdquo;</td><td>&ldquo;I cannot decide that, but please do not simply stay away. Let me call the nurse now to look at another slot.&rdquo;</td><td>Nurse or scheduler</td></tr>
<tr><td>&ldquo;Take off an extra kilo today. I drank a lot.&rdquo;</td><td>&ldquo;The nurse and doctor set how much comes off. I will tell the nurse what you told me.&rdquo;</td><td>Nurse</td></tr>
<tr><td>&ldquo;Is my potassium all right?&rdquo;</td><td>&ldquo;The nurse or doctor will explain your results. I will let them know you asked.&rdquo;</td><td>Nurse or nephrologist</td></tr>
<tr><td>&ldquo;My neighbor says this herbal tea cleans the kidneys.&rdquo;</td><td>&ldquo;Some herbs and supplements can harm people on dialysis. Please do not start it until the doctor has checked. Could you bring the label?&rdquo;</td><td>Nurse or nephrologist</td></tr>
<tr><td>&ldquo;Will my kidneys recover? Is this forever?&rdquo;</td><td>&ldquo;That is an important question, and the doctor knows your case. I will make sure the nurse knows you want to talk about it.&rdquo;</td><td>Nephrologist</td></tr>
<tr><td>&ldquo;I cannot afford the medicines and the fare.&rdquo;</td><td>&ldquo;Thank you for telling me. May I tell the nurse, so the right person can go through what help is available?&rdquo;</td><td>Nurse, social worker, or the unit&rsquo;s billing staff</td></tr>
<tr><td>&ldquo;The needles hurt more with that nurse.&rdquo;</td><td>&ldquo;I am sorry it hurt. I will pass that on to the charge nurse.&rdquo; Do not take sides or criticize a colleague</td><td>Charge nurse</td></tr>
<tr><td>&ldquo;What is wrong with the man in the next chair?&rdquo;</td><td>&ldquo;I cannot talk about other patients, just as I would not talk about you.&rdquo;</td><td>No referral needed</td></tr>
</tbody></table></div>
"""),
(3, "missedtime", "Missed, short sessions", "Missed and shortened treatments: why they matter and how to report them", """
{{fig:hd_week|Dialysis fills only a small part of the week. Every hour lost is a share of the only cleaning time the patient has.}}
{{cards:What a missed or shortened session leaves behind|Fluid::More weight to remove next time, or breathlessness before then.|Potassium::Rises silently between treatments.|Wastes::Nausea, poor appetite, itching, tiredness.|A pattern::Patients who often miss or shorten sessions are admitted to hospital more often and die sooner than those who do not.}}
{{formula:<strong>Share of a session delivered</strong> = minutes delivered &divide; minutes prescribed &times; 100.<br>Example: 240 minutes prescribed, treatment ended 30 minutes early, so 210 delivered. 210 &divide; 240 &times; 100 = 87.5 percent.}}
{{formula:<strong>Time lost over a year</strong> = minutes lost per session &times; sessions per week &times; 52.<br>Example: 30 minutes &times; 3 sessions &times; 52 weeks = 4,680 minutes = 78 hours. 78 &divide; 4 hours = about 19 and a half full sessions lost in a year.}}
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>What the technician does</th></tr></thead>
<tbody>
<tr><td>A patient asks to come off early</td><td>Tell the nurse at once. Do not stop the pump, change the time, or argue. The nurse talks with the patient and completes any form the unit uses</td></tr>
<tr><td>A patient arrives late</td><td>Tell the nurse the arrival time. The nurse decides whether the full time can still be given</td></tr>
<tr><td>A patient has not arrived</td><td>Tell the nurse by the time your unit sets, so that someone telephones the patient</td></tr>
<tr><td>Treatment is interrupted by alarms, clotting, or a toilet break</td><td>Record when the blood pump stopped and restarted. Minutes with the pump stopped are not treatment</td></tr>
<tr><td>A patient returns after a missed session</td><td>Say so to the nurse before setup. Watch for breathlessness, weakness, and a large weight gain</td></tr>
</tbody></table></div>
{{flow:Recording a shortened treatment|Times::Prescribed duration, actual start, actual end.|Delivered::The treatment time shown on the machine.|Reason::In the patient&rsquo;s own words, in quotation marks.|Notified::The nurse&rsquo;s name and the time.|Pattern::Mention at handoff if this is the second time or more.}}
{{stop:A patient who missed a session and now has breathlessness, chest pain, marked weakness, or an irregular pulse is an emergency. Call the nurse immediately.}}
"""),
(4, "distress", "Distress and respect", "Recognizing distress and speaking respectfully with patients and families", """
<p>Kidney failure brings loss: of work, income, food, travel, and time. You see patients more often than almost anyone else on the team, so you are often the first to notice a change.</p>
<div class="table-wrap"><table>
<thead><tr><th>What you may notice</th><th>What to do</th></tr></thead>
<tbody>
<tr><td>A talkative patient becomes silent, or a calm one becomes irritable</td><td>Ask one open question: &ldquo;You seem quieter today. How are things?&rdquo; Tell the nurse what you saw</td></tr>
<tr><td>Missed sessions, large weight gains, or poor grooming that are new for this patient</td><td>Report the change and when it began</td></tr>
<tr><td>Tearfulness, or talk of being a burden to the family</td><td>Listen. Do not hurry to cheer the patient up. Tell the nurse the same session</td></tr>
<tr><td>&ldquo;I want to stop dialysis.&rdquo;</td><td>Do not argue or agree. &ldquo;I hear you. This matters, and I would like the nurse and doctor to talk with you about it.&rdquo; Tell the nurse now</td></tr>
<tr><td>Talk of wanting to die or of self-harm</td><td>Stay with the patient. Call the nurse to the chair immediately. Never promise to keep it secret</td></tr>
<tr><td>Fear or silence when a particular companion is present, or unexplained injuries</td><td>Tell the nurse privately</td></tr>
</tbody></table></div>
{{cards:Speaking with respect|Name::Use the name and form of address the patient prefers.|Level::Sit or bend to eye level. Do not talk over a patient to a coworker.|Plain words::No jargon, no scolding, no blame about weight or diet.|Privacy::Lower your voice. Ask before discussing anything in front of a companion.|Honesty::&ldquo;I do not know, but I will find out who does&rdquo; is a good answer.|Language::Use the language the patient is comfortable in, or ask the nurse for an interpreter.}}
<p><strong>Families and companions.</strong> The patient decides who hears what. Ask the patient first, each time. Thank companions for their help, show them where to wait, and send their questions about care to the nurse. An angry relative is usually a frightened one: listen, do not argue, and bring the nurse.</p>
{{key:You are not expected to solve a patient&rsquo;s distress. You are expected to notice it, respond kindly, and make sure the nurse knows the same day.}}
"""),
],
"quiz_extra": [
("A session is prescribed for 240 minutes. The patient ends 30 minutes early. What share of the session was delivered?",
 ["75 percent", "80 percent", "87.5 percent", "92.5 percent"], 2,
 "210 divided by 240, times 100, equals 87.5 percent."),
("A patient with a 1,000 mL allowance has had one coffee (180 mL), one bowl of soup broth (200 mL), and two glasses of water (240 mL each). How much is left for the day?",
 ["140 mL", "380 mL", "420 mL", "None; the allowance is exceeded by 140 mL"], 0,
 "180 + 200 + 480 = 860 mL, and 1,000 minus 860 leaves 140 mL."),
("A patient mentions switching to a salt substitute to cut down on salt. Why should the nurse be told?",
 ["Salt substitutes increase thirst", "Salt substitutes contain phosphate", "Salt substitutes stain the dialyzer", "Many salt substitutes are made from potassium"], 3,
 "Potassium-based salt substitutes can raise blood potassium in a person with kidney failure."),
("A patient says, &ldquo;Take off an extra kilo today, I drank a lot.&rdquo; Which reply is within the technician&rsquo;s scope?",
 ["&ldquo;All right, I will raise the goal.&rdquo;", "&ldquo;The nurse and doctor set how much comes off. I will tell the nurse what you told me.&rdquo;", "&ldquo;You should not have drunk so much.&rdquo;", "&ldquo;That is not possible on this machine.&rdquo;"], 1,
 "Fluid removal is a clinical decision; the technician passes on the information."),
("A patient says he ate star fruit yesterday and now has hiccups that will not stop. What should you do?",
 ["Offer him water", "Record it at the end of the shift", "Tell the nurse immediately", "Advise him to eat less of it next time"], 2,
 "Star fruit is harmful in kidney failure, and persistent hiccups can be an early sign."),
("A patient quietly says, &ldquo;Sometimes I think everyone would be better off if I were gone.&rdquo; What is the correct response?",
 ["Change the subject to something cheerful", "Promise to keep it between the two of you", "Tell the patient&rsquo;s companion in the waiting area", "Stay with the patient and call the nurse to the chair immediately"], 3,
 "Talk of wanting to die is reported at once and is never kept secret."),
],
"skills_extra": [
("Totals a mock one-day fluid record in milliliters and compares it with the stated allowance, without advising a change to the plan.", False),
("Records a simulated shortened treatment with prescribed time, actual start and end times, the patient&rsquo;s stated reason, and the nurse notified.", True),
("Responds to a scripted out-of-scope question by saying what the technician can do and naming whom the question goes to.", True),
],
}
