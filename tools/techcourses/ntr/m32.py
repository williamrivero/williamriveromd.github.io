# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern, Module 32: Supportive kidney care, ethics and serious illness.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard.
Moss 2008, Kurella Tamura 2009, Verberne 2016, O'Connor 2013, Davison 2015 and 2024, REMAP (Childers 2017) and Scherer
and Holley 2016 checked against PubMed. Conference statements are described as such, without grades. PhilHealth
hemodialysis benefit as in Blueprint 3.2 (confirm on date of service). No doses. Fictional case."""

MODULE = {
    "image_alt": "A Filipino nephrology resident kneels beside the bed of an elderly woman in a provincial hospital ward, holding her hand, while her son stands nearby and her daughter joins by video call on a phone held up by a granddaughter.",
    "objectives": [
        "<strong>Intern:</strong> Notice suffering and family distress in a patient with advanced kidney disease, ask about symptoms and worries in plain words, and report what you hear to your resident.",
        "<strong>Resident:</strong> Hold a goals-of-care conversation with a patient and family using a structured framework, and document the patient&rsquo;s values, decisions and who should decide if the patient cannot.",
        "<strong>Fellow:</strong> Offer conservative kidney management (CKM) and time-limited dialysis trials as real options, estimate prognosis honestly with its uncertainty, and lead care when dialysis is withheld or withdrawn.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the doctor who asks what matters</span>An <strong>intern</strong> spends the most time at the bedside and is often the first to hear &ldquo;pagod na ako&rdquo; or to see a family arguing in the corridor; noticing and reporting is real care. A <strong>resident</strong> leads the goals-of-care conversation on most wards. A <strong>fellow</strong> brings the prognosis, the evidence on dialysis in frail older adults, and the options of conservative kidney management and time-limited trials, and stays with the patient whatever is chosen.</div>
{{plain:Think of three roads to the same town. One is a highway with tolls and long queues; one is a bridge that only some people may cross; one is a quieter provincial road with fewer stops. All three reach the town. The question is not which road is &ldquo;correct&rdquo; but which journey this traveler wants.}}
<p>The picture has a limit. The three roads (dialysis, transplantation and conservative kidney management) do not always reach the same town at the same time. For a young person, dialysis or a transplant usually adds years. For a very old, frail person with heart failure, dialysis may add little time and may take away independence, while conservative care keeps them at home with symptoms treated. And no one knows the exact length of any road. Prognosis in kidney failure is a range, shaped by age, frailty, comorbidity and function, and it must be offered with honesty about its uncertainty.</p>
<p>The physiology explains why. Dialysis removes solutes and water but does not reverse vascular disease, heart failure, frailty or dementia. Starting it adds a catheter or fistula, three sessions a week, transport, hypotension and post-dialysis fatigue. In a body with little reserve, those burdens can outweigh the clearance gained.</p>
{{cards:Key numbers|The surprise question (Moss 2008, 147 patients on hemodialysis, prospective)::1-year mortality 29.4% when the answer was &ldquo;no, I would not be surprised&rdquo; versus 10.6% when &ldquo;yes&rdquo; (odds ratio 3.5)|Starting dialysis in nursing home residents (Kurella Tamura 2009, 3,702 US residents)::At 12 months, 58% had died and only 13% had kept their pre-dialysis function|Conservative care versus dialysis at 80 or older (Verberne 2016, Dutch single center)::Median survival 2.1 versus 1.4 years from the time of choice, not statistically different|After dialysis is stopped (O&rsquo;Connor 2013, 1,947 hospice patients)::Mean survival 7.4 days after hospice enrollment (range 0 to 40)|PhilHealth hemodialysis benefit::Up to 156 sessions a year at PHP 6,350 per session for patients in the PhilHealth Dialysis Database (confirm on the date of service)}}
<p>Most patients with advanced kidney disease want honest information and a voice in the plan. A few will choose not to start dialysis, or to stop it, and a few families will disagree. Your work is to notice suffering, to give a prognosis people can use, to offer every real option including conservative care, and to keep caring for the patient whatever path is chosen.</p>
""",
    "case": {"title": "The lola who wants to go home", "html": """
<p>Saturday, 10 a.m., a medicine ward of a provincial hospital in Bacolod. Mrs. Remedios Santos, 84, a retired market vendor, has diabetic kidney disease with an estimated glomerular filtration rate (eGFR) of 8 mL/min per 1.73 m&sup2;, heart failure with an ejection fraction of 30%, and a stroke two years ago. She needs help to bathe and dress and walks with a cane only inside the house. She was admitted with breathlessness, leg edema and a potassium of 6.1 mmol/L, which improved with treatment. She has lost 6 kg in six months.</p>
<p>Her son Nonoy, who lives with her and takes her to every appointment, says, &ldquo;Ayaw na niya ng ospital, Doc.&rdquo; Her daughter Carmela, a nurse in Toronto, says by video call, &ldquo;Do everything. Start dialysis. We will pay.&rdquo; When the resident, Dr. Jerome Villanueva, asks Mrs. Santos herself, she says she misses her garden and her chickens and that she is tired, then adds, &ldquo;Bahala na ang mga anak ko.&rdquo;</p>
""", "questions": ["What is her likely prognosis, and what does the evidence say dialysis would offer her?",
                  "How should the team hold the conversation, and who decides?",
                  "What would conservative kidney management or a time-limited trial of dialysis look like for her?"]},
    "sections": [
        ("prognosis", "Prognosis", "Prognosis: estimating it, and saying it", """
<p>Prognosis matters because it changes what people choose. A patient told only &ldquo;your kidneys have failed, you need dialysis&rdquo; has not been given a choice. A patient told &ldquo;dialysis may give you some more months, mostly spent in hospital and in the unit; without it, we can keep you comfortable at home, and the time may be similar&rdquo; has.</p>
<p><strong>What predicts a short and difficult road.</strong> Advanced age, frailty, dependence in daily activities, heart failure, dementia, weight loss and malnutrition, and a hospital stay that ends in a dialysis start all predict poorer survival and loss of function. Each piece is common; together they define the patient for whom dialysis may add more burden than time.</p>
<div class="table-wrap"><table><thead><tr><th>Tool</th><th>What it captures</th><th>How to use it</th></tr></thead><tbody>
<tr><td>Surprise question: &ldquo;Would I be surprised if this patient died in the next year?&rdquo;</td><td>The clinician&rsquo;s integrated judgment</td><td>A &ldquo;no&rdquo; is a prompt to start a goals-of-care conversation, not a prediction to announce</td></tr>
<tr><td>Comorbidity index (for example, Charlson)</td><td>Burden of other disease</td><td>Higher scores lower expected survival on any treatment</td></tr>
<tr><td>Frailty and function</td><td>Reserve to withstand dialysis</td><td>Ask what the patient can do now; dependence predicts further loss</td></tr>
<tr><td>Trajectory</td><td>Whether the patient is stable or declining</td><td>Recent hospital stays, weight loss and falls signal a downhill course</td></tr>
</tbody></table></div>
<p><strong>The evidence.</strong> In a prospective study of 147 patients in three hemodialysis units, nephrologists answered the surprise question for each patient. Those in the &ldquo;no&rdquo; group were older, sicker and less functional; their 1-year mortality was 29.4% against 10.6% (odds ratio 3.5).[[ntr32_1]] Note what this shows: seven of ten patients in the &ldquo;no&rdquo; group were still alive at a year. The question identifies risk; it does not tell anyone when they will die.</p>
<p>Kurella Tamura and colleagues linked United States dialysis and nursing home registries for 3,702 nursing home residents who started dialysis. A dependence score rose from 12 to 16 points around the start of dialysis; at 3 months function was maintained in 39%, and at 12 months 58% had died and function was maintained in only 13%.[[ntr32_2]] The study was observational and had no comparison group managed without dialysis, so it cannot say that dialysis caused the decline. It does describe what usually follows for people like Mrs. Santos who start dialysis.</p>
<p>Verberne and colleagues compared 107 patients aged 70 or older who chose conservative management with 204 who chose dialysis at one Dutch hospital. Overall, median survival from the time of choice was 3.1 years with dialysis versus 1.5 years with conservative management. At age 80 or older, the difference shrank and was not statistically significant (2.1 versus 1.4 years), and it was substantially reduced in patients with high comorbidity.[[ntr32_3]] This was a small, single-center, observational study; patients who chose conservative care were older, and choice was not randomized. It is the kind of evidence you have, and you should say so.</p>
<p><strong>Saying it.</strong> Give prognosis as ranges and scenarios: the best case, the most likely case and the worst case, with dialysis and without. Use the patient&rsquo;s words: &ldquo;If we start dialysis, the most likely course is more time in hospital and in the unit, and you may not get back to your garden.&rdquo; Check what was heard.</p>
{{fig:ntr32_a}}
{{key:Give prognosis as honest ranges and scenarios, with and without dialysis, and never present dialysis as the only option.}}
"""),
        ("conversation", "The conversation", "The goals-of-care conversation, in a Filipino family", """
<p>A goals-of-care conversation is a structured talk in which the clinician learns what matters most to the patient and recommends care that fits. It is a skill, not a talent. The REMAP framework, developed for oncology and now widely taught, has five steps: Reframe, Expect emotion, Map out goals, Align with goals, and Propose a plan.[[ntr32_7]] It travels well to nephrology.</p>
<div class="table-wrap"><table><thead><tr><th>Step</th><th>What you do</th><th>What it can sound like on a Philippine ward</th></tr></thead><tbody>
<tr><td>Reframe</td><td>Give a headline that the situation has changed</td><td>&ldquo;Lola, your kidneys have become very weak, and your heart is weak too. We are at a point where we need to talk about what kind of care is best for you.&rdquo;</td></tr>
<tr><td>Expect emotion</td><td>Pause; name and respond to feelings before facts</td><td>&ldquo;This is hard to hear.&rdquo; Silence. Let the family cry or argue a little.</td></tr>
<tr><td>Map goals</td><td>Ask open questions about values, fears, hopes</td><td>&ldquo;What matters most to you now? What are you most afraid of? What would a good day look like?&rdquo;</td></tr>
<tr><td>Align</td><td>Reflect back what you heard</td><td>&ldquo;I hear that being at home with your garden and your son matters most, and that you are tired of hospitals.&rdquo;</td></tr>
<tr><td>Propose</td><td>With permission, recommend a plan that fits</td><td>&ldquo;Based on what you told us, I would recommend care at home that treats your breathlessness and keeps you comfortable, without dialysis. We would still see you and adjust your medicines.&rdquo;</td></tr>
</tbody></table></div>
<p><strong>Who decides.</strong> A patient with capacity decides for herself. Many Filipino elders prefer to decide with their children, or to let them decide. That is a legitimate choice, but it must be <em>her</em> choice. Ask directly: &ldquo;Lola, do you want to decide this yourself, or do you want Nonoy and Carmela to decide with you?&rdquo; If she says &ldquo;bahala na ang mga anak ko,&rdquo; explore it gently; it may mean trust, or it may mean she does not want to burden them with her real wish. Ask what she would want them to choose.</p>
<p><strong>The distant child.</strong> Children working abroad often carry guilt and want &ldquo;everything done.&rdquo; Bring them into the meeting by video, give them the same prognosis and the same options, and acknowledge their love. Do not let the conversation turn into a contest between the child at home and the child abroad; return it to the patient&rsquo;s own words.</p>
<p><strong>Faith and money.</strong> Ask about faith and whether a priest, pastor, imam or other religious leader should be present. Ask about costs openly, because they shape choices quietly. PhilHealth covers up to 156 hemodialysis sessions a year at PHP 6,350 per session for patients registered in the PhilHealth Dialysis Database (confirm on the date of service), but transport, medicines and lost work remain.[[ntr32_10]][[ntr32_11]] A choice of conservative care must never be made for a poor patient because of cost alone, and dialysis must never be pressed on a frail patient because it is covered.</p>
<p><strong>Documentation and law.</strong> Write the patient&rsquo;s values in her words, the options discussed, the decision, who was present, and whom she wants to decide if she cannot. The Philippines has no standalone palliative care law; palliative care provisions sit in broader statutes, including the Universal Health Care Act of 2019.[[ntr32_9]] Follow your hospital&rsquo;s policy on advance directives and do-not-resuscitate orders, and ask its legal or ethics office when unsure.</p>
{{fig:ntr32_b}}
{{key:Ask the patient how she wants decisions made, map what matters to her, and recommend a plan that fits it; the family helps, but the patient&rsquo;s values lead.}}
"""),
        ("ckm", "Conservative care", "Conservative kidney management and time-limited trials", """
<p><strong>What it is.</strong> An International Society of Nephrology consensus, developed with a Filipino nephrologist among its authors, defines conservative kidney management as planned, holistic, patient-centered care for people with kidney failure who choose not to receive dialysis or a transplant, and kidney supportive care as care that addresses symptoms, psychological, social and spiritual needs across every treatment path, including dialysis and transplantation. It stresses that both are active treatments, not the absence of treatment, and gives considerations for low-resource settings where dialysis access is limited.[[ntr32_6]] The earlier Kidney Disease: Improving Global Outcomes (KDIGO) Controversies Conference on supportive care set out a roadmap for prognosis, shared decision-making, symptom management and end-of-life care in chronic kidney disease (CKD).[[ntr32_5]] Both are conference and consensus statements, not graded recommendations.</p>
<div class="table-wrap"><table><thead><tr><th>Component</th><th>What it involves</th><th>Who leads</th></tr></thead><tbody>
<tr><td>Symptom management</td><td>Breathlessness, edema, itch, fatigue, nausea, poor appetite, pain, sleep, low mood</td><td>Nephrology with palliative care</td></tr>
<tr><td>Kidney and fluid care</td><td>Medicines that slow decline when they still help; diuretics; diet adjusted to comfort; potassium managed without rigid restriction late in illness</td><td>Fellow and attending</td></tr>
<tr><td>Advance care planning</td><td>Preferred place of care and death, resuscitation preferences, surrogate decision-maker</td><td>Resident and fellow</td></tr>
<tr><td>Family and spiritual support</td><td>Caregiver strain, finances, faith</td><td>Social worker, chaplain, nurse</td></tr>
<tr><td>End-of-life care</td><td>Recognizing the last weeks; comfort at home or in hospital</td><td>Whole team</td></tr>
</tbody></table></div>
<p><strong>What it is not.</strong> It is not abandonment. A patient on CKM still has clinic visits, blood tests when they change care, medicines adjusted to kidney function, and a phone number to call. Doses of symptom medicines must account for the low GFR; the attending and the formulary set them.</p>
<p><strong>The time-limited trial.</strong> When the outcome is uncertain, or when a family cannot accept CKM yet, a time-limited trial of dialysis can help. Scherer and Holley describe its elements for critically ill patients with acute kidney injury (AKI), and the same logic applies to frail patients with kidney failure: an honest assessment of prognosis, elicitation of the patient&rsquo;s values, a defined duration, agreed markers of success and failure, clear documentation and, often, palliative care involvement. A well-run trial can prevent conflict among clinicians and support the patient, family and staff.[[ntr32_8]]</p>
{{flow:Setting up a time-limited trial of dialysis|Agree the goal::&ldquo;We will try dialysis to see whether Lola can breathe more easily and go home, able to sit in her garden.&rdquo;|Set the time::A defined period agreed with the family, for example a set number of weeks, written in the chart.|Name success::Specific markers the family understands, such as going home, eating, recognizing family, tolerating sessions.|Name failure::Repeated hospital stays, distress during sessions, loss of consciousness, no return home.|Review on the date::Meet again on the agreed date with the same family members.|Decide::Continue if the goals are being met; if not, stop dialysis and continue comfort-focused care.}}
<div class="tc-keyp"><span class="tc-lab">In children</span>Decisions about dialysis for infants and children with severe comorbidities are made with parents, and older children and adolescents should have a voice matched to their maturity. Conservative and palliative pathways exist for neonates with very poor prognosis, and pediatric palliative care teams support families through them. See <a href="attending-pediatric-nephrologist-19-choosing-krt.html">Attending Pediatric Nephrologist, Module 19</a>.</div>
<p><strong>Philippine practice.</strong> Specialist palliative care teams are concentrated in large hospitals, and home hospice services are limited outside cities. A nephrology team often provides primary palliative care itself, with the barangay health worker, the family and the parish. Teach the family how to recognize breathlessness, how to give the medicines prescribed for it, and whom to call at night.</p>
{{key:Offer conservative kidney management as active treatment, and when the future is uncertain, propose a time-limited dialysis trial with written goals and a review date.}}
"""),
        ("withdrawal-endoflife", "Withdrawal and end of life", "Stopping dialysis and caring for the dying", """
<p>Stopping dialysis is ethically accepted when a patient with capacity, or a surrogate acting on the patient&rsquo;s known wishes, decides that its burdens outweigh its benefits. It is not suicide and not euthanasia; it is the withdrawal of a treatment that no longer serves the patient&rsquo;s goals. Death follows from the underlying kidney failure.</p>
<p><strong>What happens next.</strong> In a study of 1,947 patients admitted to ten United States hospices after stopping dialysis, mean survival was 7.4 days, with a range from 0 to 40 days. Shorter survival was associated with male sex, referral from a hospital, lower functional status and peripheral edema.[[ntr32_4]] Families need this range: &ldquo;usually about a week, sometimes a few days, occasionally several weeks.&rdquo; Patients with some residual kidney function may live longer.</p>
<p><strong>The mechanism of the last days.</strong> Without dialysis, potassium, acid and uremic toxins accumulate and fluid builds up. Most patients become drowsy and then unconscious; some develop breathlessness from fluid, agitation, twitching or itch. Each symptom has a cause the team can treat for comfort, not to prolong life.</p>
<div class="table-wrap"><table><thead><tr><th>Symptom</th><th>Likely cause</th><th>Comfort approach (medicines and doses per palliative team and formulary)</th></tr></thead><tbody>
<tr><td>Breathlessness</td><td>Fluid in the lungs, acidosis, anxiety</td><td>Sit up, fan, oxygen if it helps, medicines for breathlessness chosen for low kidney function</td></tr>
<tr><td>Agitation, confusion</td><td>Uremia, retention, pain</td><td>Check bladder and pain first; calm environment; family presence</td></tr>
<tr><td>Twitching (myoclonus)</td><td>Uremia; accumulating drugs and metabolites</td><td>Review and stop drugs that accumulate; treat per palliative team</td></tr>
<tr><td>Pain</td><td>Underlying disease, immobility</td><td>Analgesics chosen with kidney failure in mind, because some opioid metabolites accumulate</td></tr>
<tr><td>Secretions, mouth dryness</td><td>Weakness, mouth breathing</td><td>Positioning, mouth care</td></tr>
</tbody></table></div>
<p><strong>Stop what no longer helps.</strong> Daily blood tests, blood pressure targets, phosphate binders, erythropoiesis-stimulating agents and many other medicines add burden without benefit at this stage. The decision is the attending&rsquo;s, with the family, and it should be written.</p>
<p><strong>Dying at home.</strong> Many Filipino families want their lola to die at home, surrounded by relatives and neighbors, with prayers and the rites of their faith. Plan for it: transport, equipment, medicines in hand, a family member taught to give them, a contact number, and clear instructions about who will certify death and how. A resident who arranges a good home death has done important work.</p>
{{call:Stop and call the attending nephrologist, per unit protocol, but always ask the attending nephrologist for guidance, when:<ul><li>A patient asks to stop dialysis or not to start it, or a family asks you to stop or withhold it</li><li>You doubt the patient&rsquo;s capacity to decide, or the patient and family disagree</li><li>Symptoms such as breathlessness, pain or agitation are not controlled</li><li>A resuscitation decision is unclear or undocumented at night</li><li>A family member abroad asks you to override the decision made by the patient and the family at the bedside</li></ul>}}
{{key:When dialysis stops, care does not. Tell the family what to expect in days, treat every symptom for comfort, and help them be present at the end.}}
"""),
    ],
    "debrief": [
        "<p><strong>Prognosis and what dialysis offers.</strong> Mrs. Santos is 84, dependent in daily activities, with heart failure, a past stroke and weight loss. Most clinicians would not be surprised if she died within a year, the &ldquo;no&rdquo; answer that Moss associated with 29.4% one-year mortality in dialysis patients. Kurella Tamura&rsquo;s data on nursing home residents suggest that after starting dialysis, most similar patients lose function and many die within a year. Verberne&rsquo;s observational data show no significant survival advantage for dialysis over conservative management at age 80 or older, especially with heavy comorbidity. Dialysis might add some time, likely spent in hospital and in the unit, and is unlikely to return her to her garden. Say this honestly, as ranges.</p>",
        "<p><strong>The conversation and who decides.</strong> Arrange a family meeting with Mrs. Santos, Nonoy and Carmela by video, using REMAP: reframe, expect emotion, map her goals, align, and propose. She has capacity, so she decides; ask whether she wants to decide herself or with her children, and what she would want them to choose. Her own words, home, garden, tired of hospitals, point toward comfort-focused care. Acknowledge Carmela&rsquo;s love and guilt, and give her the same information. Document values, options, decision and surrogate.</p>",
        "<p><strong>CKM or a trial.</strong> Conservative kidney management would mean going home with diuretics, potassium control, symptom medicines dosed for low kidney function, regular contact with the team, an advance care plan, and support for Nonoy as caregiver. If the family cannot yet accept that, a time-limited trial of dialysis could be offered: a defined period, written goals such as going home and tolerating sessions, failure markers such as repeated admissions or distress, and a review meeting on a set date with the same family members. Either path continues with the nephrology team.</p>",
    ],
    "skills": {"title": "Supportive kidney care and serious illness",
               "intro": "Complete with a preceptor, in simulation or at your own unit. Sign-off is local.",
               "items": [("Screens a patient with advanced CKD for symptoms and family distress and reports them", False),
                         ("Uses the surprise question and functional status to identify patients who need a goals-of-care conversation", False),
                         ("Leads a simulated family meeting using REMAP, including a relative joining by video", False),
                         ("Explains conservative kidney management and a time-limited trial with written goals and a review date", False),
                         ("Documents values, decision, surrogate and resuscitation preference clearly", False)],
               "placement": "Medicine ward, nephrology clinic, dialysis unit or simulation"},
    "quiz": [
        ("During rounds, an 80-year-old man on hemodialysis tells the intern quietly, &ldquo;Pagod na ako, ayoko na.&rdquo; What should the intern do?",
         ["Reassure him that dialysis will make him feel better soon",
          "Ask him gently what he means, listen, and report his words to the resident the same day",
          "Tell him that stopping dialysis is not allowed",
          "Ignore it because older patients often say this"],
         1,
         "Noticing and exploring suffering, then reporting it, is the intern&rsquo;s role. Stopping dialysis is ethically permitted for a patient with capacity, so telling him it is not allowed is wrong, and dismissing it misses a goals-of-care need."),
        ("In the REMAP framework for goals-of-care conversations, what does the &ldquo;Map&rdquo; step involve?",
         ["Describing all available dialysis machines",
          "Asking open questions about what matters most to the patient, their fears and hopes",
          "Drawing the family tree",
          "Explaining the laboratory results in detail"],
         1,
         "Map out patient goals: open questions about values guide the recommendation. Reframe gives the headline; Align reflects values back; Propose offers a plan."),
        ("What did Verberne and colleagues (2016) find in patients aged 80 or older choosing conservative management versus dialysis?",
         ["Dialysis doubled survival in all patients over 80",
          "No statistically significant survival difference (median 2.1 versus 1.4 years), in a small observational single-center study",
          "Conservative management was associated with longer survival in all age groups",
          "A randomized trial showing dialysis harms survival"],
         1,
         "The survival advantage of dialysis seen in the whole cohort was no longer significant at 80 or older. The study was observational and not randomized, so it informs counseling but does not prove equivalence."),
        ("A family asks how long their father will live after he stops hemodialysis. Which answer best reflects the evidence?",
         ["Several months, as long as he eats well",
          "Usually about a week, though it can be a few days or several weeks",
          "Exactly 48 hours",
          "It is impossible to say anything at all"],
         1,
         "In 1,947 hospice patients who stopped dialysis, mean survival was 7.4 days (range 0 to 40). Giving a range helps families prepare; refusing to estimate leaves them unprepared."),
        ("A frail 86-year-old woman&rsquo;s son wants dialysis started, while she says she wants to stay home. She has capacity and says, &ldquo;Bahala na ang anak ko.&rdquo; What is the best next step?",
         ["Start dialysis because the son is the decision-maker",
          "Explore with her what she means and what she would want her son to choose, then propose care that fits her values",
          "Refuse dialysis because she is over 85",
          "Discharge her without a plan"],
         1,
         "A capable patient may choose to share decisions, but it must be her choice; exploring her words protects her real wishes. Age alone does not decide, and the son is not the decision-maker while she has capacity."),
    ],
    "terms": [("AKI", "Acute kidney injury"), ("CKD", "Chronic kidney disease"), ("CKM", "Conservative kidney management"),
              ("eGFR", "Estimated glomerular filtration rate"), ("GFR", "Glomerular filtration rate"),
              ("KDIGO", "Kidney Disease: Improving Global Outcomes"), ("PHP", "Philippine peso"),
              ("REMAP", "Reframe, Expect emotion, Map out goals, Align with goals, Propose a plan")],
    "readings": [("attending-nephrologist-20-conservative-care.html", "Attending Nephrologist, Module 20: Conservative care"),
                 ("advance-care-planning-dialysis.html", "Advance Care Planning and Dialysis"),
                 ("nephrology-nursing-16-supportive-palliative-kidney-care.html", "Nephrology Nursing, Module 16: Supportive and palliative kidney care"),
                 ("social-worker-16-supportive-care-grief-and-bereavement.html", "Social Worker, Module 16: Supportive care, grief and bereavement")],
    "calcs": ["calc-charlson-comorbidity.html", "calc-frailty-assessment.html", "calc-dialysis-prom.html", "calc-kfre.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("ntr_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
