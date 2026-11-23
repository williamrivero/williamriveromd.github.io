# -*- coding: utf-8 -*-
OBJECTIVES = [
    "Explain when kidney replacement is started and why the decision is not made on a laboratory value alone.",
    "Compare the pathways across the domains that matter to patients.",
    "Outline the preparation timeline for each pathway.",
    "Describe symptom care within conservative kidney management and care at the end of life.",
]
EXTRA = [
    {"after": "physiology", "id": "compare", "nav": "Pathways compared", "tag": "Comparison", "h2": "The pathways compared, in the terms patients ask about",
     "html": """
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>In-center hemodialysis</th><th>Peritoneal dialysis</th><th>Transplant</th><th>Conservative management</th></tr></thead>
<tbody>
<tr><td>Where and how often?</td><td>At a unit, usually 3 times a week, about 4 hours each</td><td>At home, every day; 3 to 5 manual exchanges or overnight by machine</td><td>One operation; clinic visits, frequent at first</td><td>Clinic or home visits as needed</td></tr>
<tr><td>What has to be done first?</td><td>Fistula or graft surgery months ahead, or a catheter</td><td>Catheter placed in the abdomen, ideally 2 weeks or more before use; 1 to 2 weeks of training</td><td>Evaluation of recipient and donor; may take months</td><td>A plan for symptoms, emergencies, and who to call</td></tr>
<tr><td>Who does the work?</td><td>Nurses and technicians</td><td>The patient or a caregiver</td><td>The patient, taking medicines daily for life</td><td>The patient and family, with the care team</td></tr>
<tr><td>Diet and fluid</td><td>Strictest limits on fluid, potassium, and phosphate</td><td>Usually more liberal</td><td>Close to normal, with food-safety rules</td><td>Adjusted for comfort and symptoms</td></tr>
<tr><td>Main risks</td><td>Low blood pressure and cramps during treatment; access infection or clotting; fatigue after sessions</td><td>Peritonitis; exit-site infection; weight gain from glucose in the fluid</td><td>Rejection; infection; side effects of medicines; surgical risks</td><td>Symptoms of uremia and fluid overload as kidney function falls</td></tr>
<tr><td>Travel and work</td><td>Tied to the unit schedule; sessions can be arranged elsewhere with planning</td><td>Flexible; supplies travel with the patient</td><td>Most freedom once stable</td><td>No treatment schedule</td></tr>
<tr><td>Who may not be suitable?</td><td>People with no usable blood vessels or who cannot tolerate fluid shifts</td><td>People with extensive abdominal scarring, no safe space, or no one able to perform exchanges</td><td>People with active infection or cancer, or severe heart or lung disease</td><td>It is an option for anyone; most often chosen by older people with several serious illnesses</td></tr>
</tbody></table></div>
<p>The diet row follows from the schedule. Daily peritoneal dialysis removes fluid and potassium a little at a time, every day. In-center hemodialysis removes them in a few sessions a week, so everything the patient takes in between sessions accumulates until the next one.</p>
<p>The pathways are neither exclusive nor permanent. Many people move between them over a lifetime: peritoneal dialysis (PD) first, then hemodialysis (HD); dialysis while waiting for a transplant; back to dialysis if a transplant fails; or a trial of dialysis followed by a decision to stop. Saying so relieves some of the fear of choosing wrongly.</p>
<p><strong>No choice is final. Tell the patient so, early.</strong></p>
"""},
    {"after": "evidence", "id": "timing", "nav": "When to start", "tag": "Evidence", "h2": "When treatment starts, and how far ahead to prepare",
     "html": """
<p><strong>Starting is a clinical decision, not a number.</strong> The IDEAL trial randomized 828 adults with advanced chronic kidney disease in Australia and New Zealand. One group was to start dialysis at an estimated filtration rate of 10 to 14 mL/min, the other at 5 to 7. Over a median of 3.6 years, 37.6% of the early group and 36.6% of the late group died (hazard ratio 1.04). Three in four of those assigned to wait started before reaching the lower level, because symptoms appeared.[[ideal2010]]</p>
<p>The KDIGO 2024 guideline on chronic kidney disease therefore advises starting dialysis on a combined assessment of symptoms, signs, quality of life, and preferences. Its triggers include persistent nausea and weight loss, fluid overload or blood pressure that cannot be controlled, itching, cognitive slowing, and inflammation of the lining of the heart. These often appear when the estimated filtration rate is between 5 and 10 mL/min/1.73 m&sup2;. These are practice points, which KDIGO does not grade.[[ckd2024]][[chan2019]]</p>
<p>Patients are often told a number at which &ldquo;dialysis will be needed,&rdquo; and they wait for it in dread. A more accurate message is that the team is watching how they feel and function as well as the tests, and that preparation happens early so the start can be planned.</p>
<div class="table-wrap"><table>
<thead><tr><th>Preparation</th><th>Lead time</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Education about all pathways</td><td>From stage 4</td><td>Decisions made in an emergency are rarely the patient's own</td></tr>
<tr><td>Transplant referral</td><td>6 to 12 months before dialysis is expected[[txcand2020]]</td><td>Allows a transplant before dialysis, and time to assess a living donor</td></tr>
<tr><td>Vein preservation</td><td>From stage 3 or 4, for life</td><td>Every needle in an arm vein costs a future access site</td></tr>
<tr><td>Fistula creation</td><td>Several months before expected start</td><td>A fistula needs weeks to months to mature and sometimes a second procedure</td></tr>
<tr><td>PD catheter</td><td>At least 2 weeks before use where possible</td><td>Healing reduces leaks; urgent starts are possible with modified technique</td></tr>
<tr><td>Hepatitis B vaccination</td><td>As early as possible</td><td>Response is better before kidney failure is advanced</td></tr>
<tr><td>Social work and benefits assessment</td><td>Before the start</td><td>Transport and cost determine whether treatment continues</td></tr>
</tbody></table></div>
<p>An unplanned start, through a temporary catheter after an emergency admission, is common. It is associated with more infections, longer hospital stays, and worse early survival than a planned start, although patients who start unplanned are often sicker to begin with. Each line in the table is a way of preventing one.</p>
<p><strong>Prepare early so that the start can wait for the patient, not for an emergency.</strong></p>
"""},
    {"after": "bedside", "id": "sdm", "nav": "The conversation", "tag": "Clinical application", "h2": "Structuring the conversation",
     "html": """
<p>Shared decision-making can be organized in three steps. Each has its own task for you.</p>
<ol>
<li><strong>Introduce the choice.</strong> Make clear that there is a decision to make, that there is more than one reasonable option, and that the patient's own priorities will guide it. Many patients do not realize they have a say.</li>
<li><strong>Describe the options.</strong> Use the same headings for each, as in the table above. Check understanding as you go with teach-back. Use pictures, a visit to the unit, or a conversation with a patient already on that treatment where these can be arranged.</li>
<li><strong>Help the patient weigh them.</strong> Ask what a good day looks like, what they most want to keep doing, and what they most want to avoid. Reflect back what you hear: &ldquo;It sounds as though staying at home matters more to you than avoiding daily tasks.&rdquo; Then give time. A decision does not have to be made in one visit.</li>
</ol>
<p><strong>In Filipino families,</strong> decisions are often made together, and adult children may ask that bad news be kept from a parent out of love. The respectful approach is to ask the patient directly, early and privately, how much they want to know and who they want involved. Some will say, &ldquo;Tell my daughter and she will decide.&rdquo; That is a choice the patient is entitled to make, and you document it. A patient who wants to know is told, even when the family is reluctant, with the physician leading the discussion.</p>
<p><strong>Common fears worth naming.</strong> &ldquo;Dialysis is a death sentence.&rdquo; &ldquo;I will be a burden.&rdquo; &ldquo;The needles.&rdquo; &ldquo;We cannot afford it.&rdquo; &ldquo;If I choose no dialysis, the doctors will abandon me.&rdquo; Each has a factual answer and an emotional one. Patients rarely raise them unless asked.</p>
<p><strong>Financial and practical support in the Philippines.</strong> Sources of help typically include the national health insurance benefit packages, government medical-assistance programs reached through hospital social service and assistance desks, local government and charity support, and registration as a person with disability, which brings discounts. Programs and amounts change. Your role is a prompt referral to the social worker with the patient's documents ready, not a quotation of figures.</p>
<p><strong>Ask the patient first, privately, how much they want to know and who should decide with them.</strong></p>
"""},
    {"after": "sdm", "id": "ckm-care", "nav": "Conservative and end-of-life care", "tag": "Clinical application", "h2": "Conservative management and care at the end of life",
     "html": """
<p>Conservative kidney management (CKM) is active care. Kidney-protective treatment, anemia treatment, and blood pressure and fluid control continue for as long as they help the person feel well. What changes is the aim: comfort and function, not laboratory targets.[[ckm2015]] The KDIGO 2024 guideline lists support for comprehensive conservative management, for people who choose not to start kidney replacement, as an ungraded practice point.[[ckd2024]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Symptom</th><th>Contributors to look for</th><th>Nursing measures; prescribed options exist for each</th></tr></thead>
<tbody>
<tr><td>Itch</td><td>Dry skin, high phosphate</td><td>Regular unperfumed moisturizer, cool bathing, short nails, loose cotton clothing</td></tr>
<tr><td>Nausea and poor appetite</td><td>Uremia, constipation, medicines</td><td>Small frequent meals of preferred foods; mouth care; treat constipation; relax dietary restrictions</td></tr>
<tr><td>Breathlessness</td><td>Fluid overload, anemia, acidosis, anxiety</td><td>Upright positioning, a fan directed at the face, salt and fluid adjustment; report for diuretic review</td></tr>
<tr><td>Fatigue and poor sleep</td><td>Anemia, low mood, restless legs, itch</td><td>Activity pacing; sleep routine; screen mood</td></tr>
<tr><td>Pain</td><td>Bone and joint disease, neuropathy</td><td>Assess with a scale at every contact; avoid anti-inflammatory drugs; opioids suited to kidney failure are chosen by the physician</td></tr>
<tr><td>Swelling</td><td>Sodium and water retention</td><td>Leg elevation, skin care, salt review</td></tr>
<tr><td>Confusion or drowsiness</td><td>Uremia, medicines accumulating, infection</td><td>Safety; medicine review; tell the family what to expect</td></tr>
</tbody></table></div>
<p><strong>Advance care planning</strong> records what the person would and would not want if they became too ill to speak, and who should speak for them. Useful openings are: &ldquo;What do you understand about where your illness is heading?&rdquo; &ldquo;What worries you most?&rdquo; &ldquo;If your health got worse, what would matter most to you?&rdquo; Document the patient's words, tell the physician, and make sure the family knows where the record is.</p>
<p><strong>Stopping dialysis.</strong> Some people decide that the burdens of dialysis have come to outweigh its benefits. This is a recognized and lawful choice made with the physician, the patient, and the family. It is different from suicide or abandonment. After dialysis stops, death usually follows within days to a few weeks, depending on remaining kidney function. It is most often peaceful, with increasing drowsiness. Families need to hear this in advance, along with what will be done for breathlessness, restlessness, itch, and secretions, and whom to call at night. Palliative or hospice services are involved wherever they are available.</p>
<p><strong>A time-limited trial</strong> is a middle path when the outlook is uncertain. Dialysis is started for an agreed period, with agreed signs of benefit, and reviewed on a set date. It lets a hesitant patient try treatment without feeling the decision is irreversible.[[ckm2015]]</p>
<p><strong>Choosing no dialysis is not choosing no care. Assess every symptom at every contact.</strong></p>
"""},
]
QUIZ = [
    {"stem": "A patient with stage 5 chronic kidney disease has an estimated filtration rate of 11 mL/min/1.73 m&sup2;. She is eating well, her weight is stable, and she has no swelling or itch. Her son asks why dialysis has not been started. What is the most accurate explanation?",
     "options": [
         ("Dialysis must start once the filtration rate falls below 15", False, "No trial supports starting at a fixed number."),
         ("Dialysis is started when symptoms or complications of kidney failure appear; starting earlier on the number alone has not been shown to improve survival", True, "In the IDEAL trial, a planned early start did not improve survival over a later start. Guidelines advise starting on symptoms and signs, with preparation done in advance."),
         ("The unit has no available slot", False, "Scheduling is not the clinical basis for the decision."),
         ("She should wait until she has an emergency", False, "The aim is a planned start before an emergency, with access and education ready."),
     ],
     "objective": "Explain when kidney replacement is started and why the decision is not made on a laboratory value alone.", "sources": ["ideal2010", "ckd2024", "chan2019"], "flag": ""},
    {"stem": "A patient with stage 4 chronic kidney disease who may choose hemodialysis is admitted for pneumonia. The intern is about to place an intravenous cannula in the left forearm; the patient is right-handed. What should the nurse do?",
     "options": [
         ("Assist; forearm veins are the easiest to cannulate", False, "Needles and cannulas scar the veins needed for a future fistula."),
         ("Suggest a vein on the back of the hand, preferably on the dominant side, and explain the need to preserve the forearm and upper-arm veins", True, "Vein preservation begins well before dialysis. The non-dominant arm is usually the first choice for a fistula, so its forearm and upper-arm veins are protected."),
         ("Refuse all intravenous access", False, "Access is needed for treatment. The task is to choose the site wisely."),
         ("Request a peripherally inserted central catheter instead", False, "These catheters damage the central veins and are avoided in people who may need a fistula."),
     ],
     "objective": "Outline the preparation timeline for each pathway.", "sources": ["va2019"], "flag": ""},
]
TERMS = [
    ("Time-limited trial", "Treatment started for an agreed period with agreed goals, then reviewed."),
    ("Unplanned start", "Beginning dialysis as an emergency without prior education or permanent access."),
    ("Hospice", "Care focused on comfort for a person approaching the end of life."),
]
FLAGS = [
    "Statement on survival after stopping dialysis is given as a range without a citation; confirm wording with the palliative care reviewer.",
    "Philippine support sources are named by type only; verify current programs with the social worker.",
    "Family-communication paragraph reflects common practice; align with hospital policy on disclosure.",
    "IDEAL figures (828 adults, deaths 37.6% vs 36.6%, hazard ratio 1.04, 75.9% of the late group starting early for symptoms) were checked against the PubMed abstract; filtration rates in IDEAL were estimated with the Cockcroft-Gault equation.",
    "KDIGO 2024 dialysis-start triggers and support for conservative management are practice points (5.4.1, 5.4.2, 5.5.2), checked against the KDIGO summary of recommendations.",
    "Statement that unplanned starts are associated with more infections, longer stays, and worse early survival has no cited source; reviewer may wish to add one.",
]
