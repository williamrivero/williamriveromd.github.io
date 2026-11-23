# -*- coding: utf-8 -*-
# Module 16 expansion: symptom care, advance care planning, requests to stop dialysis, the last days, and grief.
# Sections follow the base "bedside" section in this order: symptoms-pc, acp, withdrawal, last-days, grief.
OBJECTIVES = [
    "Assess pain, itch, breathlessness, nausea, fatigue, restlessness, and low mood, provide nursing comfort measures, and report for treatment with attention to medicine safety in kidney failure.",
    "Support advance care planning by eliciting goals, identifying the surrogate decision-maker, and documenting wishes per facility policy, within the Filipino family and faith context.",
    "Respond to a request to stop dialysis by screening for depression and reversible causes, involving the team, respecting a decision made with capacity, and continuing care after dialysis stops.",
    "Recognize the dying phase, provide comfort care to the patient and family in hospital or at home, and support bereaved families and grieving staff.",
]
EXTRA = [
    {"after": "bedside", "id": "symptoms-pc", "nav": "Symptom care", "tag": "Symptom care",
     "h2": "Symptom by symptom: assess, comfort, report, refer",
     "html": """
<p>Module 14 taught you to ask about symptoms routinely in patients living well on HD. This section goes further, for patients whose symptoms are heavy or whose goals have shifted toward comfort. The pattern is the same for every symptom: assess it, relieve what nursing can relieve, report it with enough detail for the physician to act, and refer. Medicines appear here by class only, so you know what to watch for. The physician chooses the medicine, dose, and timing. You give it as ordered and watch the response.</p>
<p><strong>A rule for every symptom medicine in kidney failure.</strong> The failed kidneys no longer clear many drugs and their breakdown products. Side effects can therefore appear days after a medicine is started or increased. After any new symptom medicine, watch for increasing drowsiness, new confusion, muscle twitching or jerks, slowed or shallow breathing, unsteadiness, and falls. If they appear, hold the next dose as the order or protocol allows, and notify the physician.[[davison2019]]</p>
<p><strong>Pain.</strong> Ask about pain at every contact and rate it from 0 to 10. A patient with confusion or dementia may not be able to rate it. Watch instead for grimacing, guarding, moaning, restlessness, and resistance to being turned, and use the behavioral pain tool your unit approves. Describe the character, because it points to the cause: aching bone pain, burning or tingling nerve pain, cramping, the sharp pain of a wound. Comfort measures include positioning and pressure relief, warmth or cool packs as the care plan allows, gentle movement, and pacing activity. Know the medicine cautions:</p>
<ul>
<li>Acetaminophen (paracetamol) is often the physician&rsquo;s first choice for mild pain.</li>
<li>Anti-inflammatory pain relievers (the nonsteroidal group, including many over-the-counter tablets and some widely used gels) can damage remaining kidney function, raise potassium, and increase bleeding from the stomach. Teach patients not to buy them on their own.</li>
<li>Some opioid medicines, or their active breakdown products, accumulate in kidney failure. The physician chooses opioids and doses suited to kidney failure. Watch for drowsiness, confusion, twitching, and slow breathing. Expect constipation, which needs a bowel plan from the start.</li>
<li>Medicines for nerve pain also accumulate and can cause drowsiness, dizziness, and falls.</li>
</ul>
<p>Pain in kidney failure is both under-treated and treated with unsuitable medicines. Good pain control depends on careful choice, not on avoiding pain relievers altogether.[[davison2019]]</p>
<p><strong>Itch.</strong> Ask directly, because many patients never mention it.[[rayner2017]] Rate it from 0 to 10, ask how often it wakes the patient, and inspect the skin for scratch marks, broken skin, and infection. Comfort measures: an unperfumed moisturizer at least daily and after bathing; lukewarm, not hot, water; short nails; loose cotton clothing; a cool room; and distraction during sessions. Report a high or rising score together with the phosphate results and any missed or shortened sessions. The physician may review dialysis adequacy and phosphate control, or prescribe medicines. Sedating antihistamines, which are commonly used, can cause drowsiness and falls in older patients. Some itch medicines accumulate in kidney failure.</p>
<p><strong>Breathlessness.</strong> First decide whether it is an emergency. Sudden or severe breathlessness, falling oxygen saturation, chest pain, frothy sputum, or confusion needs the physician at once, because fluid in the lungs may need urgent removal. For chronic breathlessness, sit the patient upright and supported, with legs down if swollen. Direct a hand-held or electric fan toward the face, which many patients find relieving. Open a window. Teach slow, pursed-lip breathing. Stay calm and present, because fear makes breathlessness worse. Check weight gain and swelling, and report them for review of the target weight and fluid removal. Give oxygen only as ordered, usually when saturation is low. In palliative care the physician may prescribe low doses of medicines that ease the sensation of breathlessness. Watch for drowsiness and slowed breathing.</p>
<p><strong>Nausea and poor appetite.</strong> Ask when nausea comes: before meals, during or after sessions, or in the morning. Check bowel habit, and review recent medicine changes. Offer small, frequent portions of foods the patient enjoys. Serve them cool if smells trigger nausea. Give mouth care before meals. Treat constipation as ordered. When the goal is comfort, ask the physician and dietitian whether diet restrictions can be relaxed. Forcing a dying person to follow a strict renal diet adds burden without benefit. Some anti-nausea medicines accumulate and can cause abnormal movements, restlessness, or drowsiness. Report these if they appear.</p>
<p><strong>Fatigue.</strong> Ask how long the patient takes to recover after a session (Module 14) and what they can no longer do. Look for causes that can be treated: anemia, low blood pressure during sessions, poor sleep, low mood, infection, a sedating medicine. Help the patient spend energy on what matters most, such as a grandchild&rsquo;s birthday or Sunday Mass, with rest before and after.</p>
<p><strong>Restlessness.</strong> Two different problems hide under this word. <em>Restless legs</em> is an uncomfortable urge to move the legs, worse in the evening and at rest, relieved by moving. Report it, because iron deficiency and some medicines contribute and it can be treated. <em>Agitation or delirium</em> is a change in attention and awareness that comes and goes over hours, often with confusion, pulling at lines, or seeing things. Check for causes the team can reverse: pain, a full bladder, constipation, low oxygen, low or high glucose, fever, and medicines that have accumulated. Keep the patient safe and a family member close. Use a calm voice, and orient gently. Avoid restraints except as facility policy strictly allows. Report new delirium promptly. Sedating medicines are ordered by the physician and need close observation in kidney failure.</p>
<p><strong>Low mood.</strong> Screen with the unit&rsquo;s tool and follow the steps in Module 14. Fatigue, poor appetite, and poor sleep overlap between kidney failure and depression, so hopelessness, loss of interest, and guilt are often more telling. Some antidepressants need dose adjustment in kidney failure, and their benefit in dialysis patients is uncertain. Psychological support, social help, and spiritual care matter as much as medicine. A patient with low mood who says they want to stop dialysis needs both a mood assessment and a hearing. The stopping-dialysis section explains how.</p>
<p><strong>Report and refer.</strong> Report each symptom with its score, trend, effect on daily life, likely contributors, and what you have tried. For example: &ldquo;Breathlessness 7 of 10 lying flat, sleeps sitting in a chair, gained 3 kg since Monday, saturation 93% on room air; fan and positioning helped a little; requesting review of target weight and of her itch, which is 8 of 10.&rdquo; Reassess after any change, and report again if relief is not achieved. Refer to the palliative care team, where one exists, when symptoms persist despite usual measures or when several problems pile up at once.</p>
<p><strong>After any new symptom medicine, the next few days are when accumulation shows. Look for drowsiness, twitching, and slow breathing before you look for relief.</strong></p>
"""},
    {"after": "symptoms-pc", "id": "acp", "nav": "Advance care planning", "tag": "Advance care planning",
     "h2": "Advance care planning: goals, a trusted voice, and a written record",
     "html": """
<p>Module 5 introduced advance care planning as a routine part of kidney care and gave opening questions. This section describes the whole process and your part in it.</p>
<p><strong>What it is.</strong> Advance care planning is a series of conversations, not a single form. Over months or years, the patient comes to understand the illness, thinks about what matters most, chooses who should speak for them if they cannot, and, if they wish, records preferences for future care. The plan is revisited when health changes: after a hospital admission, a new diagnosis, a fall, or a loss of independence.</p>
<p><strong>Why it matters.</strong> Most patients on dialysis will at some point be too ill to decide for themselves, often suddenly. Without a plan, families must guess under pressure, and treatment defaults to whatever is technically possible.</p>
<p>The best trial evidence comes from the United States. In a randomized trial of 210 patient&ndash;surrogate pairs from 20 dialysis centers in one region, a structured two-session advance care planning intervention for patients and their chosen surrogates improved agreement between patient and surrogate on goals of care. It also improved the surrogate&rsquo;s confidence in decision-making. It did not change the patients&rsquo; own decisional conflict. Among the 45 patients who died, surrogates in the intervention group reported less anxiety, depression, and post-traumatic distress afterward.[[song2015]] That bereavement finding rests on a small subgroup, and the trial measured agreement and distress, not survival. The program was designed to be delivered by trained nurses.[[song2018]] Patients in a Canadian survey said they relied on their kidney team for this planning, yet fewer than 10% had discussed end-of-life care with their nephrologist in the previous year.[[davison2010]]</p>
<p><strong>The steps, and who does them.</strong></p>
<div class="table-wrap"><table><thead><tr><th>Step</th><th>What happens</th><th>Your part</th></tr></thead><tbody>
<tr><td>Open the topic</td><td>Planning is presented as something every patient is offered</td><td>&ldquo;We ask everyone on dialysis to think about this, while they are well.&rdquo; Notice moments when the patient raises it.</td></tr>
<tr><td>Understanding</td><td>What the patient knows, and wants to know, about the illness</td><td>Ask, listen, and report gaps to the physician. Do not give a prognosis yourself.</td></tr>
<tr><td>Goals and values</td><td>What matters most; what would be unacceptable; what the patient fears</td><td>&ldquo;If your health got worse, what would be most important to you?&rdquo; Record the patient&rsquo;s own words.</td></tr>
<tr><td>Surrogate decision-maker</td><td>Who should speak for the patient if they cannot</td><td>Ask, record the name and contact details, and confirm that person knows and has heard the patient&rsquo;s wishes.</td></tr>
<tr><td>Specific treatments</td><td>Cardiopulmonary resuscitation, intensive care, breathing machines, tube feeding, continuing or stopping dialysis</td><td>Led by the physician. You attend, support, and document. Resuscitation status becomes an order only when the physician writes it.</td></tr>
<tr><td>Record and share</td><td>The plan is written and placed where it will be found</td><td>Document per facility policy. Make sure the plan travels with the patient to the hospital and the emergency room.</td></tr>
<tr><td>Review</td><td>Plans change as health and wishes change</td><td>Flag the plan for review after admissions or major changes.</td></tr>
</tbody></table></div>
<p><strong>The Filipino family and faith context.</strong> In many Filipino families, the family decides together rather than the patient alone. The person who decides may be an eldest child, a spouse, a sibling who pays the bills, or a relative who is a nurse or doctor, sometimes working abroad. Some families avoid talking about death for fear that speaking of it invites it, or protect an elder from bad news. Some patients defer completely to their children or to God&rsquo;s will. None of this makes planning impossible. Practical approaches:</p>
<ul>
<li>Ask the patient, privately and early, how they want decisions made: &ldquo;Some people want to hear everything and decide themselves. Others prefer their family to decide with the doctor. What would you prefer?&rdquo; Respect the answer and record it.</li>
<li>Ask whom the patient wants present. Arrange family meetings when key members can attend, including relatives abroad by video call when the patient agrees. An adult patient with capacity controls what is shared, under data privacy law.[[ra10173]]</li>
<li>Use the patient&rsquo;s language, and gentle, indirect openings when direct ones feel too harsh: &ldquo;Have you thought about what you would want if you became very sick?&rdquo;</li>
<li>Invite faith into the conversation instead of leaving it outside. For many patients, prayer, the sacraments, or the guidance of a priest, pastor, minister, or imam is part of how they decide. Ask, &ldquo;Is your faith important to you in this?&rdquo; and offer to contact their faith leader. Trust in God and acceptance of medical limits can sit together.</li>
<li>Watch for conflict between family members, or between what the family wants and what the patient has said. Report it. The physician, social worker, or ethics committee can help resolve it.</li>
</ul>
<p><strong>The legal and policy setting in the Philippines.</strong> At the time of writing, we could not verify any Philippine law that specifically governs advance directives for end-of-life care or the appointment of a health care proxy. Bills on health care proxies and advance care planning have been filed in Congress but were not found to have been enacted. Until that changes, facility policy sets how a written directive or a named representative is recorded and honored, guided by the hospital&rsquo;s ethics committee and legal counsel. Follow your facility&rsquo;s forms and procedures. Never promise a patient or family that a document will be legally binding.</p>
<p><strong>When the patient cannot decide.</strong> If a patient has lost capacity, the surrogate is asked to decide as the patient would have wanted, using what is known of their wishes and values. Where those are unknown, the surrogate decides in the patient&rsquo;s best interests. Facility policy sets who may act as surrogate, and in what order relatives are approached when no one was named. A plan made earlier is the surrogate&rsquo;s best guide, and a comfort afterward.</p>
<p><strong>The most useful thing you can record is a name and a sentence: who will speak for this patient, and what the patient said matters most.</strong></p>
"""},
    {"after": "acp", "id": "withdrawal", "nav": "Requests to stop dialysis", "tag": "Stopping dialysis",
     "h2": "When a patient asks to stop dialysis",
     "html": """
<p>Sooner or later, a patient will tell you at the chair that they want to stop. Module 5 described stopping dialysis as a recognized choice made with the physician and family. Module 12 placed it in the ethics of refusal. This section is about what you do between the moment the words are spoken and the moment a decision is made, and after.</p>
<p><strong>A request is the start of a conversation, not a decision.</strong> &ldquo;I want to stop&rdquo; can mean many things. &ldquo;I am exhausted today.&rdquo; &ldquo;My itch is unbearable.&rdquo; &ldquo;I cannot afford the fare.&rdquo; &ldquo;I do not want to be a burden to my children.&rdquo; &ldquo;I am depressed.&rdquo; Or &ldquo;I have thought about this for months, and I am ready.&rdquo; Each needs a different response. Begin by listening: &ldquo;That sounds important. Can you tell me more about what is making you feel this way?&rdquo; Do not argue, reassure too quickly, or change the subject.</p>
<p><strong>Screen for depression and for risk of suicide.</strong> A request to stop dialysis is not the same as suicidal intent. Many patients who decide to stop are not depressed and have weighed the burdens of treatment clearly. But depression is common in dialysis patients, it can drive the request, and it can be treated. Screen mood with the unit&rsquo;s tool. If anything the patient says suggests thoughts of ending their life in other ways, ask directly and follow the crisis section of Module 14, &ldquo;Suicide risk and self-neglect: ask, stay, escalate.&rdquo; A patient who describes current thoughts of ending their life is not left alone. Missing sessions, or drinking far beyond the fluid limit without discussion, may be self-neglect rather than a decision. Module 14 covers that too.</p>
<p><strong>Look for causes that can be reversed.</strong></p>
<div class="table-wrap"><table><thead><tr><th>Possible driver</th><th>What may help</th></tr></thead><tbody>
<tr><td>Uncontrolled symptoms: itch, pain, cramps, breathlessness, long recovery after sessions, low blood pressure during sessions</td><td>Symptom review and treatment; changes to the dialysis prescription by the nephrologist</td></tr>
<tr><td>Depression, anxiety, grief, or loneliness</td><td>Mood assessment, treatment, counseling, peer and faith support</td></tr>
<tr><td>Cost, transport, or lost income</td><td>Social worker; benefits and charitable assistance; shift changes</td></tr>
<tr><td>Feeling like a burden; family conflict</td><td>Family meeting; caregiver support (Module 14)</td></tr>
<tr><td>Access problems or painful cannulation</td><td>Access review; cannulation by an experienced nurse; local anesthetic per order</td></tr>
<tr><td>Confusion or delirium affecting judgment</td><td>Medical review for reversible causes before any decision is taken</td></tr>
</tbody></table></div>
<p><strong>Inform the nephrologist and bring the team together.</strong> Report the request the same day, with the patient&rsquo;s exact words and your findings. The physician assesses decision-making capacity: whether the patient understands the information, appreciates that it applies to them, can weigh it, and can communicate a choice. A family meeting follows, led by the physician, with you, the social worker, and, if the patient wishes, a chaplain or faith leader. The options are laid out honestly: continuing unchanged; changing the dialysis plan to reduce its burden; a time-limited trial with a review date (Module 5); stopping with full supportive care; and what each would likely mean.</p>
<p><strong>Respect a decision made with capacity.</strong> An adult who has capacity may decide to stop dialysis even when the team or family disagrees. Your duty is to make sure the decision is informed, voluntary, and documented, and then to support it. If the patient lacks capacity, the surrogate decides as described in the advance care planning section. Where the family and the patient disagree, or the team is uncertain, the hospital ethics committee can help. Record the conversations, who was present, the decisions, the physician&rsquo;s orders, and the patient&rsquo;s own words.</p>
<p><strong>Stopping dialysis does not mean stopping care.</strong> Before the last session, make sure that:</p>
<ul>
<li>A symptom plan is ordered for breathlessness, restlessness, itch, pain, nausea, and noisy breathing, with medicines suited to kidney failure available wherever the patient will be.</li>
<li>The place of care is agreed: home, hospital, or hospice where one exists, with referral to palliative or home care services.</li>
<li>The family knows what to expect, how to give comfort, and whom to call, day and night.</li>
<li>Diet and fluid restrictions are relaxed as the physician advises, so the patient can enjoy small amounts of favorite food and drink.</li>
<li>The physician has reviewed medicines that no longer help, for example phosphate binders or some long-term preventive drugs.</li>
<li>The patient knows they may change their mind, and how to reach the unit if they do.</li>
<li>The unit stays in touch: a call, a visit where policy allows, and a goodbye from the staff who have known the patient for years.</li>
</ul>
<p>Stopping is an emotional moment for staff too. If you disagree with a decision, say so to the team, not to the patient, and ask for support if you need it. The grief section of this module covers moral distress.</p>
<p><strong>When a patient says &ldquo;I want to stop,&rdquo; your first job is to find out what they mean. Listen, screen, look for what can be fixed, and tell the nephrologist the same day.</strong></p>
"""},
    {"after": "withdrawal", "id": "last-days", "nav": "The last days", "tag": "End-of-life care",
     "h2": "The last days of life: recognizing dying and caring for comfort",
     "html": """
<p>A patient may die after stopping dialysis, during conservative care, or from another illness while still on dialysis. In each case the last days follow a pattern you can learn to recognize. Recognizing it matters, because it changes the goal of every action: from correcting numbers to keeping the person comfortable and the family close.</p>
<p><strong>Signs that a person may be entering the last days.</strong> No single sign is certain, and the team decides together. These often appear in combination:</p>
<ul>
<li>Spending most of the day asleep, and becoming harder to wake</li>
<li>Taking little or no food or fluid, and difficulty swallowing tablets</li>
<li>Changes in breathing: irregular breaths, pauses, or rapid shallow breathing</li>
<li>Noisy, rattling breathing from secretions the person can no longer clear</li>
<li>Cool, pale, or mottled hands, feet, and knees</li>
<li>Confusion or restlessness, or a quiet withdrawal from surroundings</li>
<li>Passing little or no urine</li>
</ul>
<p>When the team agrees that the patient is dying, the physician reviews every order with the family. Which medicines to stop. Which comfort medicines to give, and by which route if swallowing fails. Whether blood tests and frequent vital signs are still useful. The resuscitation decision. You carry out the plan and make sure it is written where every shift will see it.</p>
<p><strong>Comfort care, in hospital or at home.</strong></p>
<div class="table-wrap"><table><thead><tr><th>Need</th><th>Nursing care</th></tr></thead><tbody>
<tr><td>Mouth</td><td>A dry mouth is common and uncomfortable. Moisten the mouth and lips often with a damp swab, a few drops of water, or ice chips if the patient can manage them. Apply lip balm, and clean gently. Teach the family to do this; it gives them a way to help.</td></tr>
<tr><td>Position and skin</td><td>Turn and reposition gently for comfort, support with pillows, and keep skin clean and dry. As death nears, comfort comes before a strict turning schedule.</td></tr>
<tr><td>Secretions</td><td>Position the patient on the side with the head slightly raised. Explain to the family that the rattling sound comes from saliva the patient can no longer swallow, and that it is not thought to distress the patient. Deep suctioning is usually avoided, because it can cause discomfort. Give medicines to reduce secretions only as ordered.</td></tr>
<tr><td>Breathlessness, pain, and restlessness</td><td>Give comfort medicines as ordered. Assess regularly for grimacing, moaning, or agitation. Check for a full bladder or constipation as causes of restlessness. Report symptoms that are not controlled.</td></tr>
<tr><td>Eating and drinking</td><td>Offer small amounts the patient wants. Never force food or fluid. Explain that loss of appetite is part of dying, not starvation.</td></tr>
<tr><td>Environment</td><td>Quiet, soft lighting, privacy where possible, and familiar things: a rosary, photographs, music, the voices of family.</td></tr>
</tbody></table></div>
<p><strong>At home.</strong> Many Filipino patients wish to die at home among family. Make that possible where you can. Confirm the referral to a home care or palliative service where one exists. Make sure comfort medicines and written instructions go home with the family. Teach mouth care, positioning, and what the changes in breathing mean, and give a number to call. Tell the family what to do when death occurs at home, as the facility advises, including how a physician will confirm and certify the death.</p>
<p><strong>Family presence.</strong> Let family stay as facility policy allows, and stretch the rules gently where safety permits. Encourage them to talk to and touch the patient; hearing may continue even when the person cannot respond. Prepare them for what they will see. Help relatives abroad say goodbye by phone or video call. Make sure family members also eat, rest, and take turns.</p>
<p><strong>Spiritual care.</strong> Ask the patient or family which rites or prayers they want, and arrange them early, while the patient can still take part. For many Catholic families this includes the Anointing of the Sick and prayers at the bedside. Other Christian, Muslim, and indigenous families have their own practices; some, for example, wish the body to be prepared and buried quickly. Do not assume. Ask, &ldquo;Are there prayers or customs that are important to your family at this time?&rdquo; and make room for them.</p>
<p><strong>After death.</strong> Follow facility policy for each step:</p>
<ol>
<li>Death is confirmed and the time recorded by the physician, or as policy defines. The physician completes the death certificate.</li>
<li>Give the family time with the person before any care is done, and offer to call their faith leader.</li>
<li>Care for the body with respect: close the eyes, straighten the limbs, clean and dress as the family wishes and culture allows, and invite the family to take part if they want to.</li>
<li>Remove lines and devices as policy directs. A tunneled dialysis catheter or an implanted device may need a specific procedure, or may have to be left in place for the funeral parlor. Standard infection-control precautions continue after death.</li>
<li>Label and release the body, and hand belongings to the family, as policy requires.</li>
<li>Document the time of death, who confirmed it, who was present, notifications made, care given, and items released.</li>
<li>Tell the dialysis unit and the other teams who knew the patient, so no reminder calls or appointments go to a grieving family.</li>
</ol>
<p><strong>Once the team agrees a patient is dying, every order should answer one question: does this make the person more comfortable, or the family closer?</strong></p>
"""},
    {"after": "last-days", "id": "grief", "nav": "Grief and self-care", "tag": "Bereavement and staff care",
     "h2": "Grief: the family afterward, and the staff who knew the patient for years",
     "html": """
<p><strong>The family&rsquo;s grief.</strong> Families of dialysis patients often grieve twice: first over years of decline, sacrifice, and caregiving, and then at the death. Grief may bring relief as well as sorrow, and relief can bring guilt. Both are normal and deserve to be named gently. Some families also carry debt from years of treatment. A bereaved relative may need more help if there is intense guilt that does not ease, inability to function months later, heavy drinking, or talk of not wanting to live. These warrant referral to a doctor or counselor.</p>
<p>What a unit can do, within its policy: send a card or make a call after the death; tell the family how to collect belongings and documents; give information about bereavement support through the hospital, parish, or community; and, where policy and the family welcome it, let staff attend the wake or a memorial Mass. Advance care planning done well before death may also help those left behind. In the randomized trial described earlier, surrogates of patients who died reported less anxiety and depression when they had taken part in planning.[[song2015]]</p>
<p><strong>Staff grief.</strong> You may see a patient three times a week for ten years. You know the names of the grandchildren and the favorite jokes. When that patient dies, the loss is real, and it can repeat many times a year. Unrecognized, repeated grief can turn into exhaustion, detachment, or a sense that the work is pointless. Ways to acknowledge it:</p>
<ul>
<li>Tell the whole team, not only the shift on duty, when a patient dies.</li>
<li>Pause for a moment of silence or a short prayer at the start of a shift, as the team prefers.</li>
<li>Hold a periodic remembrance gathering for patients who have died.</li>
<li>Let staff who were close to the patient attend the wake or funeral when the roster and policy allow.</li>
</ul>
<p><strong>Moral distress.</strong> Moral distress is the strain of believing you know the right thing to do but being unable to do it, or of taking part in care you believe is wrong. In kidney care it can arise when dialysis continues for a dying patient because the family cannot let go; when a patient stops dialysis and you disagree; when symptoms are left uncontrolled; or when cost decides treatment. Name it. Raise it with the head nurse or physician, bring it to a team meeting, and use the ethics committee when values conflict. Silence makes it worse.</p>
<p><strong>Debriefing.</strong> After a difficult death, a sudden death in the unit, a death after stopping dialysis, or a suicide (Module 14), a short, structured debriefing helps the team learn and recover. Keep it blame-free and confidential: what happened, what went well, what was hard, what we would change, and who needs more support. Debriefing is not an incident review, although an incident report may also be needed.</p>
<p><strong>Self-care is part of professional practice.</strong> Sleep, food, exercise, time with family, faith, and humor are not luxuries. Know your own signs of strain, such as dreading work, irritability, numbness, or poor sleep, and speak to someone you trust. Use the staff support or employee assistance your facility offers, and seek professional help if grief or distress persists. Nurses who look after themselves can stay present for patients over the long years that dialysis care demands.</p>
<p><strong>Grief that is named and shared becomes bearable. Grief that is carried alone, shift after shift, becomes burnout. Tell the team when a patient dies.</strong></p>
"""},
]
QUIZ = [
    {"stem": "Three days after the physician started a new opioid for leg pain, a patient on HD is unusually sleepy during the session, has small jerking movements of his hands, and is breathing slowly. What should you do?",
     "options": [
         ("Reassure the family that he is finally sleeping well because his pain is controlled", False, "Increasing drowsiness, twitching, and slow breathing after a new opioid suggest accumulation in kidney failure, not good pain control."),
         ("Assess his breathing, oxygen saturation, and level of consciousness, hold the next dose as the order or protocol allows, and notify the physician now", True, "Some opioids and their breakdown products accumulate in kidney failure. You assess, hold per order or protocol, and report so the physician can review the medicine."),
         ("Give an extra dose before he wakes up so the pain does not return", False, "Giving more could deepen sedation and slow his breathing further."),
         ("Stop the dialysis session so that the medicine is not removed", False, "The concern is accumulation, not removal, and stopping treatment is not a nursing decision for this problem."),
     ],
     "objective": "Assess pain, itch, breathlessness, nausea, fatigue, restlessness, and low mood, provide nursing comfort measures, and report for treatment with attention to medicine safety in kidney failure.",
     "sources": ["davison2019"], "flag": "Holding doses follows the order or unit protocol."},
    {"stem": "A patient with long-standing breathlessness who has chosen conservative kidney management is short of breath sitting at home. Her saturation is unchanged from her usual, and she has no chest pain. Which comfort measure is most appropriate to teach her daughter?",
     "options": [
         ("Lay her flat so that she can rest", False, "Lying flat usually worsens breathlessness. Upright, supported positioning helps."),
         ("Sit her upright, supported with pillows, direct a fan toward her face, and stay calm with her", True, "Upright positioning, airflow from a fan across the face, and a calm presence are simple measures many patients find relieving, alongside treatments the physician orders."),
         ("Give her oxygen from a neighbor&rsquo;s tank whenever she is breathless", False, "Oxygen is given only as ordered. It helps mainly when saturation is low."),
         ("Encourage large drinks of water to loosen her chest", False, "In kidney failure extra fluid may accumulate and worsen breathlessness."),
     ],
     "objective": "Assess pain, itch, breathlessness, nausea, fatigue, restlessness, and low mood, provide nursing comfort measures, and report for treatment with attention to medicine safety in kidney failure.",
     "sources": ["ckm2015"], "flag": "Escalate sudden or severe breathlessness, falling saturation, or chest pain as an emergency."},
    {"stem": "A 70-year-old widow on HD tells you she wants her eldest son to make medical decisions for her if she becomes too ill, but she has never told him. What is the most useful next step?",
     "options": [
         ("Tell her that only a lawyer can arrange that", False, "Naming a surrogate begins with a conversation. Documentation follows facility policy, and a lawyer is not required to start."),
         ("Record her choice and his contact details per facility policy, report it to the physician, and encourage her to talk with her son, offering a family meeting", True, "Naming the surrogate, making sure that person knows the patient&rsquo;s wishes, and documenting per policy are core steps of advance care planning."),
         ("Telephone her son yourself today and tell him what she said", False, "The patient controls what is shared. Ask her consent and let her lead the conversation, with support."),
         ("Wait until she is admitted to hospital to discuss it", False, "Planning works best while the patient is well enough to think and talk."),
     ],
     "objective": "Support advance care planning by eliciting goals, identifying the surrogate decision-maker, and documenting wishes per facility policy, within the Filipino family and faith context.",
     "sources": ["song2015", "ra10173"], "flag": "Documentation and legal weight of advance directives follow facility policy; no Philippine statute was verified."},
    {"stem": "A patient who has been on HD for six years says, &ldquo;I want to stop dialysis. I am tired of being a burden to my children.&rdquo; Which response comes first?",
     "options": [
         ("Tell her that stopping dialysis is the same as suicide and she must not think that way", False, "A request to stop is not the same as suicidal intent, and lecturing closes the conversation. It does need screening and a hearing."),
         ("Arrange for this to be her last session, as she has the right to refuse", False, "A request is the start of a conversation. Reversible causes and capacity are assessed, and the team is involved, before any decision."),
         ("Listen and explore what lies behind the request, screen her mood and ask about thoughts of self-harm per Module 14, and report to the nephrologist today", True, "Listening, screening for depression and suicide risk, looking for reversible causes such as feeling a burden, and informing the physician are the first steps."),
         ("Ask her children to persuade her to continue", False, "Pressuring her is not appropriate. Family involvement happens in a meeting she agrees to."),
     ],
     "objective": "Respond to a request to stop dialysis by screening for depression and reversible causes, involving the team, respecting a decision made with capacity, and continuing care after dialysis stops.",
     "sources": ["anna7"], "flag": "Capacity is assessed by the physician; crisis steps follow Module 14 and facility policy."},
    {"stem": "A dying patient in the ward has noisy, rattling breathing. His wife is frightened and asks you to suction him. He is unresponsive and appears settled. What is the best action?",
     "options": [
         ("Perform deep suctioning every hour until the sound stops", False, "Deep suctioning is usually avoided at this stage, because it can cause discomfort and the secretions reform."),
         ("Reposition him on his side with the head slightly raised, explain the cause of the sound, give any secretion medicine ordered, and stay with her", True, "Positioning, explanation, ordered medicine, and presence address both the patient&rsquo;s comfort and the family&rsquo;s fear."),
         ("Start intravenous fluids so that the secretions become thinner", False, "Extra fluid in a dying patient with kidney failure can worsen secretions and swelling. Fluids follow the physician&rsquo;s plan."),
         ("Ask her to leave the room so the sound does not upset her", False, "Family presence is supported. Explanation helps more than separation."),
     ],
     "objective": "Recognize the dying phase, provide comfort care to the patient and family in hospital or at home, and support bereaved families and grieving staff.",
     "sources": ["cohen2000"], "flag": "Suctioning and secretion medicines follow the physician&rsquo;s order and facility policy."},
]
TERMS = [
    ("Advance care planning", "A series of conversations in which a person considers their goals and values, names who should speak for them, and records preferences for future care."),
    ("Surrogate decision-maker", "The person who makes health decisions for a patient who has lost capacity, guided by the patient&rsquo;s known wishes."),
    ("Decision-making capacity", "The ability to understand information, appreciate how it applies to oneself, weigh it, and communicate a choice; assessed by the physician."),
    ("Moral distress", "The strain of believing one knows the right action but being unable to take it, or of taking part in care one believes is wrong."),
    ("Debriefing", "A short, structured, blame-free team discussion after a difficult event, to learn and to support one another."),
    ("Delirium", "An acute, fluctuating disturbance of attention and awareness, often with confusion or agitation, usually with a medical cause."),
    ("Restless legs", "An uncomfortable urge to move the legs, worse in the evening and at rest, relieved by movement."),
]
FLAGS = [
    "Philippine legal status of advance directives: no statute specifically governing end-of-life advance directives or health care proxies was verified (web search November 2026; a Senate committee sponsored a Healthcare Proxy Act in March 2026, with no evidence found of enactment). The text describes it as facility policy and should be rechecked by legal counsel at each review.",
    "Medicines are named by class only, with no doses. Statements on opioid and nerve-pain medicine accumulation, anti-inflammatory pain relievers, sedating antihistamines, and anti-nausea medicines are general pharmacology supported by one review (Davison 2019); confirm with the nephrology pharmacist.",
    "Signs of the dying phase, mouth care, secretion management, and avoidance of deep suctioning reflect general palliative nursing practice and are not cited to a kidney-specific source; review by a palliative care specialist is requested.",
    "After-death care steps (confirmation, certification, removal of devices, release of the body) follow facility policy; handling of tunneled catheters after death was deliberately left to policy.",
    "Religious and cultural practices are described as examples only (Anointing of the Sick; some families wishing rapid burial), with an instruction to ask; confirm wording with the hospital chaplaincy.",
    "Bereavement practices (cards, calls, attendance at wakes) are framed as options within unit policy.",
    "The nurse-delivered nature of the advance care planning program is taken from the protocol paper of its later pragmatic trial (Song 2018), which states the earlier trials used trained research nurses.",
    "Song 2015: the rewrite adds that the bereavement finding rests on a small subgroup (45 deaths) and that the trial measured agreement and distress, not survival; no new numbers were added.",
    "fetch_refs.py may not glob m16_x.py; the NEW_REFS PMIDs must be added to refs_pubmed_raw.json, and journal names added to JOURNALS where missing, before the check passes without reference errors.",
]
NEW_REFS = {
    "murtagh2007sx": "17200048",
    "murtagh2007surv": "17412702",
    "saini2006": "17060257",
    "davison2006": "16672923",
    "wen2022": "34278540",
    "raj2018": "29729346",
    "rayner2017": "28923831",
    "oconnor2013": "24202133",
    "cohen1995": "7802519",
    "cohen2000": "10873883",
    "davison2010": "20089488",
    "foote2016": "26265214",
    "song2015": "26141307",
    "song2018": "28993286",
    "davison2019": "30833302",
}
