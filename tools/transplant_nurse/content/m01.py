# -*- coding: utf-8 -*-
MODULE = {
    "sub": "Why a kidney transplant is usually the best treatment for kidney failure, why the clock for referral starts long before dialysis, who decides what on a transplant team, and how a nurse sends a referral that actually moves.",
    "desc": "Transplant Nurse Module 1: the kidney transplant pathway, survival evidence, KDIGO referral timing, team roles and nursing scope under RA 9173, and a closed-loop SBAR referral for Philippine registered nurses.",
    "keywords": "kidney transplant nursing, transplant referral timing, preemptive kidney transplant, transplant coordinator role Philippines, SBAR referral, RA 9173 nursing scope",
    "image_alt": "A Filipino nurse sitting with a patient and his wife at a clinic table, pointing to a simple drawing of the kidney transplant journey from clinic to surgery to follow-up.",
    "objectives": [
        "Explain, in physiologic terms, why transplant usually outperforms dialysis and why the first weeks carry extra risk.",
        "State when a potentially suitable patient should be referred and why waiting for dialysis to start loses options.",
        "Describe what each member of the transplant team decides and where the nurse's authority begins and ends.",
        "Compose a complete SBAR referral and close the loop with a named owner and a follow-up date.",
        "Identify the practical barriers (distance, work, cost, family expectations) that most often stall a referral.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "A relay race, not a referral slip",
         "html": """
<p>Think of the transplant pathway as a relay race with many runners: the clinic nurse, the referring physician, the transplant coordinator, the surgeon, the laboratory, the donor team, the benefits office, and the patient and family. A baton dropped between any two runners costs months. Nobody loses the race by running slowly. They lose it in the handoffs, when each runner assumes the next one already has the baton.</p>
<p>The picture has a limit. In a real relay every runner can see the baton. In transplant care the baton is often invisible: a referral letter sitting unread, a laboratory result filed without review, a patient who stopped answering because the bus fare to the center is half a week's income. Your job on this pathway is to keep the baton visible. You do that by writing referrals that carry everything the next person needs, by confirming that someone actually received them, and by writing down who owns the next step and when you will check.</p>
<div class="tc-plain"><span class="tc-lab">In plain words</span>The nurse rarely decides who gets a kidney. The nurse very often decides whether the patient's file keeps moving.</div>
<p>Throughout this subtrack you will work alongside the same small team. Nurse Carla is your preceptor, a transplant nurse with many years on the ward and in the clinic. Joy is the recipient coordinator. Dr. Santos is the transplant nephrologist. The patients change from module to module. All of them, staff and patients, are fictional, and their stories are built from situations transplant nurses meet every week.</p>
"""},
        {"id": "why", "nav": "Why transplant", "tag": "Physiology and evidence", "h2": "Why transplant, and why the clock starts early",
         "html": """
<p><strong>What dialysis replaces, and what it does not.</strong> A healthy kidney never stops working. It filters about 180 liters of plasma a day. It adjusts sodium, potassium, acid and water minute by minute. It makes erythropoietin and active vitamin D. It clears middle-sized uremic molecules that dialysis membranes remove poorly.</p>
<p>Thrice-weekly hemodialysis squeezes a week of that work into about 12 hours. Between sessions, water, potassium and acid build up. During sessions they are pulled off quickly. The heart and vessels take the swings, which is why left ventricular hypertrophy, vascular calcification and sudden cardiac death are the main causes of death on dialysis. A working transplant restores continuous filtration and the kidney's hormones, so many of those stresses simply stop.</p>
<p><strong>The survival curve has a dip before it rises.</strong> In a national cohort of more than 228,000 people on dialysis in the United States, those who received a first deceased-donor transplant had a higher risk of death in the first two weeks than comparable patients still waiting on the list (relative risk about 2.8), the cost of major surgery and induction immunosuppression. The curves crossed within months, and long-term mortality among recipients was 48 to 82 percent lower than among wait-listed patients who stayed on dialysis.[[wolfe1999]] A later systematic review of observational studies found the same direction for mortality, cardiovascular events and quality of life across most subgroups.[[tonelli2011]] These are observational data, so selection still matters; but because the comparison group was already judged fit enough to be listed, much of the healthy-candidate bias is removed.</p>
<div class="tc-keyp"><span class="tc-lab">Remember</span>The first weeks after transplant are the riskiest weeks; the years after are the reward. That early dip is why careful evaluation, prepared families and alert postoperative nursing matter so much.</div>
<p><strong>Why referral is a CKD-clinic task, not a dialysis-unit task.</strong> The Kidney Disease: Improving Global Outcomes (KDIGO) candidate guideline recommends that patients with advanced CKD who are expected to reach kidney failure be informed about transplant and referred for evaluation at least 6 to 12 months before dialysis is anticipated, so that a preemptive transplant (one done before dialysis starts) remains possible. Patients already on dialysis should be referred once they are medically stable, and access to evaluation should not depend on socioeconomic status, sex or ethnicity.[[txcand2020]] Evaluation takes months: cardiac testing, cancer screening, dental and infection clearance, donor work-up, and paperwork. A referral made on the day dialysis starts guarantees the patient a period of dialysis that might have been avoided.</p>
<p>In practice, start thinking about referral when the estimated glomerular filtration rate (eGFR) is falling through the low 20s, or when a validated risk tool predicts a meaningful chance of kidney failure within a year or two. Age alone, diabetes alone, or being on dialysis for a long time do not exclude a patient; the team weighs the whole person.</p>
<div class="tc-scene"><span class="tc-lab">In the CKD clinic &middot; fictional</span><p>Nurse Carla, your preceptor, is reviewing the morning list with you. Mrs. Abad, 61, has an eGFR of 22, down from 31 a year ago. Her chart says "transplant: not discussed." You assume it is too early, since she is nowhere near dialysis.</p><p>Carla shakes her head. "Evaluation here takes six months on a good day. Count backward from when she will need dialysis, not forward from today." She asks you to raise transplant at this visit and to flag the chart for the nephrologist.</p><p class="tc-scene-take"><b>What this shows.</b> The referral clock runs backward from the expected start of dialysis. The nurse who notices the trend is often the one who starts it.</p></div>
"""},
        {"id": "pathway", "nav": "The pathway", "tag": "Workflow", "h2": "The journey in six stations",
         "html": """
<ol class="tc-flow">
<li><b>Kidney failure planning</b>Transplant is discussed alongside dialysis and comprehensive conservative care, using what matters to the patient.</li>
<li><b>Referral</b>A complete referral reaches a named person at the transplant program, who acknowledges receipt.</li>
<li><b>Evaluation</b>Medical, surgical, psychosocial, infection, cancer and financial review; potential living donors are evaluated by a separate team.</li>
<li><b>Readiness</b>Either a living donor is approved, or the candidate is activated on the deceased-donor waiting list and kept ready.</li>
<li><b>Transplant admission</b>Surgery, early graft surveillance, induction immunosuppression, discharge teaching.</li>
<li><b>Lifelong follow-up</b>Drug levels, rejection and infection surveillance, cardiovascular and cancer prevention, and eventually planning if the graft fails.</li>
</ol>
<p>Each station has its own owner, and the nurse touches all six. At station 1 you raise the topic. At station 2 you assemble and send. At station 3 you track dates and dispositions. At station 4 you keep contact details, transfusion history and illness reports current. At station 5 you assess and escalate. At station 6 you reconcile medicines, time samples, teach and triage. The modules that follow take each station in turn.</p>
<div class="tc-scene"><span class="tc-lab">On the ward &middot; fictional</span><p>Mr. Lacson was listed for a deceased-donor kidney last year. Tonight the coordinator, Joy, calls the ward: an offer has come in, but his phone number on file has been disconnected for three months. His daughter's number is not in the chart. By the time the family is reached through the barangay, the offer has gone to the next candidate.</p><p>Nobody in this story made a clinical error. Station 4 failed because nobody owned "keep the contact details current."</p><p class="tc-scene-take"><b>What this shows.</b> Each station needs a named owner. Readiness is a nursing task as much as a medical one.</p></div>
"""},
        {"id": "roles", "nav": "Who decides", "tag": "Scope", "h2": "Who does what on a transplant team",
         "html": """
<p>Transplant programs are built to separate decisions that could conflict. The person caring for the recipient does not also advocate for the donor. The person who wants a kidney for a patient does not also allocate kidneys. Knowing these boundaries protects patients, donors and you.</p>
<div class="table-wrap"><table>
<thead><tr><th>Role</th><th>Decides or does</th><th>The nurse's part</th></tr></thead>
<tbody>
<tr><td>Transplant nephrologist and surgeon</td><td>Candidacy, surgical plan, immunosuppression, treatment of rejection</td><td>Report findings, carry out orders, escalate change</td></tr>
<tr><td>Multidisciplinary selection committee</td><td>Accepts, defers or declines a candidate; approves a living donor</td><td>Supply accurate, dated information; never pre-announce a decision</td></tr>
<tr><td>Recipient coordinator (often an RN)</td><td>Tracks evaluation, readiness, listing communication, follow-up</td><td>Keep the tracker current; name an owner for every open item</td></tr>
<tr><td>Living donor team and independent advocate</td><td>Protects the donor's interests and voluntary decision</td><td>Give the donor a private route; never relay a donor's private reasons</td></tr>
<tr><td>Histocompatibility laboratory</td><td>HLA typing, antibody screening, crossmatch interpretation</td><td>Verify sample identity and date; report transfusions and pregnancies</td></tr>
<tr><td>Allocation authority (deceased donation)</td><td>Who is offered a deceased-donor kidney</td><td>Respond to offers through verified channels only</td></tr>
<tr><td>Pharmacist, social worker, dietitian, benefits staff</td><td>Drug supply and interactions, social barriers, nutrition, coverage</td><td>Route needs early; document the referral and its outcome</td></tr>
</tbody></table></div>
<p>Under the Philippine Nursing Act (RA 9173), the registered nurse assesses, plans and gives nursing care, teaches, and collaborates with physicians and other professionals, within law, physician orders and institutional privileges.[[ra9173]] That is a broad and important scope, and it is enough to make the transplant pathway work. It does not include clearing compatibility, telling a candidate they are accepted, or changing an immunosuppressant dose. Those statements, made kindly but without authority, are the most common way a well-meaning nurse causes harm.</p>
<div class="tc-stop"><span class="tc-lab">Stop and report</span>If a patient or relative asks you to confirm acceptance, a match, or a surgery date that has not been communicated by the program, say what you know, say who will confirm it, and document the question.</div>
<div class="tc-scene"><span class="tc-lab">At the bedside &middot; fictional</span><p>Aling Nena's son corners you in the hallway after his mother's evaluation visit. "Nurse, the doctor looked happy. Is she accepted? Can we tell the relatives in Pampanga?"</p><p>You want to reassure him. Instead you say: "I don't have the committee's decision yet. Joy, the coordinator, will call you once it is final, usually within two weeks. I'll write down that you asked, so she knows to call you." Then you document the question and send Joy a message.</p><p class="tc-scene-take"><b>What this shows.</b> Kindness and scope are compatible. Say what you know, say who will confirm the rest, and leave a written trail.</p></div>
"""},
        {"id": "referral", "nav": "The referral", "tag": "Practice", "h2": "A referral that moves",
         "html": """
<p>A referral is a clinical handoff to someone who has never met the patient. It should let the coordinator decide what to schedule first without calling you back. Use the Situation, Background, Assessment, Recommendation (SBAR) structure, and attach what the program asks for.</p>
<div class="tc-cards">
<div class="tc-card"><b>Situation</b>Who the patient is, why you are referring now, and the trajectory: eGFR trend, or dialysis start date and modality.</div>
<div class="tc-card"><b>Background</b>Cause of kidney disease, prior transplants, transfusions and pregnancies, major comorbidities, current medicines, allergies, vascular or peritoneal access.</div>
<div class="tc-card"><b>Assessment</b>Function and frailty, adherence history, support at home, potential donors who have <em>volunteered</em>, and barriers: distance, work, cost, language.</div>
<div class="tc-card"><b>Recommendation</b>What you are asking for (evaluation appointment), contact preferences and the best time to call, and when you will follow up.</div>
</div>
<p><strong>Close the loop.</strong> A referral that has been faxed, emailed or handed over is not yet received. Confirm receipt with a named person, record the date, and write the next expected action and its owner in the chart: for example, "Received by the recipient coordinator on 3 March; first evaluation visit to be scheduled by the program within two weeks; clinic RN to call the patient on 17 March to confirm." Then do the call.</p>
<div class="tc-scene"><span class="tc-lab">In the CKD clinic &middot; fictional</span><p>Two referrals leave the clinic on the same day. The first is a one-line note: "For transplant evaluation, please." The second gives the eGFR trend, the cause of kidney disease, two pregnancies and one transfusion, the patient's evening-only phone window, and a request for a first visit.</p><p>Three weeks later, the first patient has not been called; the coordinator needed the transfusion history and could not reach anyone. The second patient already has her cardiac tests scheduled.</p><p class="tc-scene-take"><b>What this shows.</b> A referral is judged by whether the next person can act on it without calling you back.</p></div>

<p><strong>Ask what matters.</strong> Shared decision-making means the patient hears the options, the honest tradeoffs, and is asked about work, travel, caregiving and fears. A jeepney driver who cannot lose four days a week to dialysis may weigh transplant very differently from a retired teacher with a supportive family nearby. Record those priorities; they guide the evaluation team.</p>
<p><strong>Never recruit donors.</strong> You may explain that living and deceased donation both exist and that a living donor must volunteer freely and is evaluated separately. You must not ask a specific relative to donate, or suggest that a family "should" provide a kidney. Pressure, even gentle, undermines the voluntariness that Module 3 protects.</p>
"""},
        {"id": "ph", "nav": "Philippine context", "tag": "Local practice", "h2": "The Philippine setting",
         "html": """
<p>Kidney transplant in the Philippines is concentrated in a limited number of licensed transplant facilities, led by the National Kidney and Transplant Institute (NKTI), which also trains coordinators for other centers.[[nkti_pia]] Living donation is the most common source of kidneys, and living non-related donation is governed by its own Department of Health (DOH) rules and ethics review (Module 3). Deceased donation is governed by the Organ Donation Act and DOH allocation rules (Module 4).[[ra7170]] Since January 2025, PhilHealth's Z Benefits for kidney transplantation have been substantially expanded, and post-transplant packages for adults and children were added in 2025 (Module 10).[[phic2024_35]][[phic2025_12]]</p>
<p>Geography shapes everything. A patient in Samar or Sulu may need a ferry, a bus and a night's lodging to reach an evaluation visit. A referral that ignores this will stall. Plan with the patient: which visits can be bundled, which tests can be done locally and sent, who can accompany, and how the program can reach them if mobile signal is poor.</p>
<p>Common misconceptions you will hear: that only a sibling can donate; that older patients are never accepted; that diabetes rules a person out; that transplant is only for the wealthy. Each is false or outdated. Correct them gently, and let the program make the individual decision.</p>
<div class="tc-scene"><span class="tc-lab">By phone &middot; fictional</span><p>Ka Lito lives in Northern Samar. His first evaluation visit requires a ferry, two buses and a night in Manila. He has missed it twice. On your third call you ask what would make it possible. He says his cousin drives to Manila every second Monday.</p><p>You and Joy rebook the visit for that Monday, bundle the dental and chest X-ray clearances into the same trip, and arrange for his local laboratory to send the blood tests ahead.</p><p class="tc-scene-take"><b>What this shows.</b> Geography is a clinical barrier. Plan around it with the patient instead of documenting "no-show."</p></div>
"""},
        {"id": "evidence", "nav": "Evidence", "tag": "Certainty", "h2": "What is established, and what is not",
         "html": """
<ul>
<li><strong>Established:</strong> for most suitable candidates, transplant is associated with longer survival and better quality of life than remaining on dialysis, after an early period of higher risk.[[wolfe1999]][[tonelli2011]] This rests on large, consistent observational data; a randomized trial would be neither ethical nor feasible.</li>
<li><strong>Guideline position:</strong> early referral (6 to 12 months before anticipated dialysis) to allow preemptive transplant is a KDIGO recommendation.[[txcand2020]]</li>
<li><strong>Evidence-supported inference:</strong> that nurse-led tracking and closed-loop referral shorten time to evaluation is plausible and supported by quality-improvement experience, but trial evidence specific to the Philippines is lacking. Measure it locally (Module 11).</li>
</ul>
"""},
    ],
    "case": {
        "title": "The driver who works on another island",
        "html": """
<p><strong>Tuesday, 10:20 a.m., CKD clinic.</strong> Mang Rodel, 46, drives a delivery truck between Cebu and Bohol. He has diabetic kidney disease. His eGFR has fallen from 28 to 19 mL/min/1.73 m² over 14 months, and his albuminuria is heavy. He has no dialysis access yet.</p>
<p>His wife answers most of your questions. When you raise transplant, he shakes his head. "My doctor mentioned it. But my brother is the only one who could give me a kidney, and he has his own family. Besides, I can't miss work to go to Manila." He looks at the clock; his truck leaves for the port at noon.</p>
<p>He has a basic phone and is reachable only after 7 p.m., when he is off the road. The chart shows no referral, no access plan, and the note "transplant: patient not interested."</p>
""",
        "acte": {
            "Assess": "Kidney trajectory and timing (he is within the referral window now), comorbidities, his understanding of options, what matters to him (income, family), support, and practical barriers: travel, work hours, cost, phone access.",
            "Communicate": "Send an SBAR referral to the transplant program with trajectory, comorbidities, medicines and his evening-only contact window. Confirm receipt with a named coordinator. Inform the nephrologist that referral is done and access planning should proceed in parallel.",
            "Teach": "In two minutes: transplant usually means longer life and freedom from dialysis; evaluation takes months, so starting now protects options; living donors must volunteer freely and are evaluated separately; deceased donation also exists. Correct the idea that only his brother can help, without asking anyone to donate.",
            "Escalate": "Refer to social work and the benefits office for travel, lodging and coverage questions. If he cannot reach the program, escalate to the coordinator lead rather than letting the referral lapse.",
        },
        "task": "Write the SBAR referral, the closed-loop entry (who received it, when, next action and owner, your follow-up date), and one sentence recording what matters to him.",
        "outcome": """
<p>Your colleague in the story, Nurse Liza, did three things before noon. She told Mang Rodel, in two minutes, that evaluation takes months, that starting now keeps a transplant before dialysis possible, and that a living donor must volunteer freely and is not the only route, because deceased donation exists too. She did not ask about his brother again.</p>
<p>She wrote the SBAR referral with his eGFR trend, his medicines and his evening-only contact window, sent it to the program, and called Joy to confirm receipt. Joy agreed to call him after 7 p.m. on Thursday. Liza wrote that plan in the chart, with her own follow-up call set for the next Monday, and told the nephrologist that access planning should start in parallel.</p>
<p>On Monday, Liza learned that Joy's Thursday call had not gone through; his phone was off at sea. Because the follow-up was written down, Liza noticed, and they agreed on a text-first approach that Mang Rodel had consented to. His first evaluation visit was booked for a Saturday.</p>
""",
    },
    "second_round": ("He cannot leave work during office hours, and the program's coordinator works 8 a.m. to 5 p.m.", "A revised referral with one feasible contact route (for example, a scheduled evening call or a text-first agreement documented with consent) and a named follow-up owner."),
    "evidence_out": "Complete SBAR referral and documented closed-loop handoff.",
    "critical": "Promising acceptance, or pressuring a family member to donate.",
    "reflect": "Think of a patient you have cared for who started dialysis without ever being referred for transplant evaluation. At which station did the baton drop, and who could have picked it up?",
    "practice": {
        "intro": "Use synthetic or de-identified examples only.",
        "items": [
            "Observe a transplant referral being prepared; identify which SBAR elements were missing.",
            "Draft an SBAR referral for a synthetic CKD stage 4 patient and have your preceptor critique it.",
            "Confirm receipt of a referral by phone and document the closed loop with owner and date.",
            "Practice a two-minute explanation of transplant, dialysis and conservative care with a peer acting as the patient.",
            "List your facility's contact routes and backup contacts for the transplant program.",
        ],
    },
    "readings": [
        ("kidney-transplant.html", "Patient-level overview of transplant you can share."),
        ("organ-donation-philippines.html", "How living and deceased donation work in the Philippines."),
        ("transplant-prehabilitation.html", "What candidates can do while waiting to be fitter for surgery."),
    ],
    "calcs": ["calc-kfre.html", "calc-epts.html"],
    "terms": [
        ("Preemptive transplant", "A kidney transplant performed before the patient has started maintenance dialysis."),
        ("Closed loop", "A handoff confirmed as received, with the next action, its owner and a follow-up date recorded."),
        ("Candidacy", "The transplant team's judgment that a person can safely undergo transplant and benefit from it."),
    ],
    "quiz": [
        {"stem": "A 52-year-old with diabetic CKD has an eGFR falling from 24 to 18 mL/min/1.73 m² over a year and no living donor identified. When should transplant referral happen?",
         "options": [("Now, during advanced CKD planning, so evaluation can finish before dialysis is needed.", True, "KDIGO recommends referral at least 6 to 12 months before anticipated dialysis to allow preemptive transplant."),
                     ("After dialysis starts, because the program needs a dialysis history.", False, "Dialysis is not a prerequisite; waiting forfeits the chance of a preemptive transplant."),
                     ("Only after a living donor has been identified.", False, "Deceased donation is also possible, and donor discussions happen in parallel, not as a gate."),
                     ("When eGFR falls below 10 mL/min/1.73 m².", False, "By then evaluation can rarely be completed before dialysis is required.")],
         "sources": ["txcand2020"]},
        {"stem": "Who decides that a patient is an acceptable transplant candidate?",
         "options": [("The authorized transplant team or selection committee.", True, "Candidacy is a team decision; the nurse supplies accurate information and facilitates access."),
                     ("The referring clinic nurse, once the checklist is complete.", False, "A complete checklist supports the decision but does not make it."),
                     ("The PhilHealth benefits office.", False, "Coverage eligibility is separate from clinical candidacy."),
                     ("The patient's family, through consensus.", False, "The family's views matter, but candidacy is a clinical judgment.")],
         "sources": ["txcand2020"]},
        {"stem": "In the large dialysis cohort comparing transplant recipients with wait-listed patients, what happened to the risk of death in the first two weeks after transplant?",
         "options": [("It was higher than for comparable wait-listed patients, before becoming much lower later.", True, "Early risk was about 2.8 times higher; long-term mortality was 48 to 82 percent lower among recipients."),
                     ("It was already lower than on dialysis from day one.", False, "Surgery and induction create an early period of increased risk."),
                     ("It was identical throughout follow-up.", False, "The curves crossed; long-term survival favored transplant."),
                     ("It stayed higher for the whole study period.", False, "Long-term risk was substantially lower in recipients.")],
         "sources": ["wolfe1999"]},
        {"stem": "Which statement about the evidence that transplant prolongs survival is most accurate?",
         "options": [("It comes from large observational studies that compare recipients with patients already judged fit for the waiting list.", True, "Comparing with wait-listed patients reduces, but cannot remove, selection bias; randomization would be unethical."),
                     ("It comes from a randomized trial of transplant versus dialysis.", False, "No such trial exists or could ethically be done."),
                     ("It is purely mechanistic and has never been studied in patients.", False, "Large patient cohorts consistently show the association."),
                     ("It applies only to recipients younger than 40.", False, "Benefit was seen across most subgroups, although it was larger in some.")],
         "sources": ["wolfe1999", "tonelli2011"]},
        {"stem": "A referral was emailed to the transplant program last week. What makes the handoff complete?",
         "options": [("Confirmed receipt by a named person, with the next action, its owner and a follow-up date documented.", True, "A closed loop requires acknowledgment and a recorded owner and date."),
                     ("The email shows it was sent successfully.", False, "Sent is not received; many referrals stall unread."),
                     ("The patient was told to wait for a call.", False, "This places the whole burden on the patient and has no owner."),
                     ("A copy was filed in the chart.", False, "Filing documents the attempt, not the handoff.")],
         "sources": []},
        {"stem": "A relative asks whether her husband has been accepted for transplant. The committee has not met. Best response?",
         "options": [("Explain that the committee has not yet reviewed him, name who will communicate the decision, and document the question.", True, "Honest, within scope, and routed to the authorized communicator."),
                     ("Reassure her that he will almost certainly be accepted.", False, "Promising acceptance is a critical error and may cause harm if he is deferred."),
                     ("Tell her you cannot discuss anything.", False, "You can share what is known and who will confirm; refusing all information erodes trust."),
                     ("Look up the committee members' opinions and share them.", False, "Pre-announcing informal opinions is outside scope and inappropriate.")],
         "sources": ["ra9173"]},
        {"stem": "During referral teaching, the patient says his sister should give him a kidney because she is single. What should the nurse do?",
         "options": [("Explain that donation must be voluntary and is discussed privately with a separate donor team; do not ask or pressure the sister.", True, "Voluntariness is protected from the first conversation."),
                     ("Ask the sister directly whether she is willing.", False, "Recruiting a specific donor creates pressure."),
                     ("Agree that single relatives are the best donors.", False, "Marital status does not make someone an appropriate donor."),
                     ("Tell him transplant is impossible without her.", False, "False; deceased donation and other donors may be possible.")],
         "sources": ["lentine2017"]},
        {"stem": "Which element is most important to include in the Background section of a transplant referral?",
         "options": [("Prior transfusions, pregnancies and transplants.", True, "These sensitizing events shape antibody testing and matching."),
                     ("The patient's favorite foods.", False, "Not relevant to the referral background."),
                     ("Your opinion of whether the family is wealthy.", False, "Inappropriate and not a clinical datum; financial barriers are described factually in Assessment."),
                     ("A guess about which donor will be chosen.", False, "Speculation about donors does not belong in a referral.")],
         "sources": ["txcand2020"]},
        {"stem": "Under RA 9173, which action falls within the registered nurse's scope on a transplant pathway?",
         "options": [("Assessing the patient, teaching, and coordinating referral in collaboration with physicians.", True, "Assessment, teaching and collaboration are core nursing functions under the Act."),
                     ("Clearing a crossmatch as compatible.", False, "Compatibility interpretation belongs to the laboratory and transplant team."),
                     ("Activating a patient on the waiting list on your own authority.", False, "Listing is a program decision."),
                     ("Changing an immunosuppressant dose from a level result.", False, "Dose changes require an authorized prescriber.")],
         "sources": ["ra9173"]},
        {"stem": "A patient misses his first evaluation visit. What is the best first step?",
         "options": [("Contact him through his agreed route, ask what happened, and help remove the barrier.", True, "Missed visits often reflect transport, work or cost barriers that can be solved."),
                     ("Mark him nonadherent and close the referral.", False, "This punishes a barrier rather than addressing it."),
                     ("Wait for him to call back.", False, "Passive waiting lets the baton drop."),
                     ("Ask the program to remove him from consideration.", False, "Premature and outside nursing scope.")],
         "sources": []},
        {"stem": "Why does evaluation for transplant typically take months?",
         "options": [("It includes cardiac, cancer, infection, dental, psychosocial and donor work-up, each with scheduling and results.", True, "The breadth of work-up is why referral must be early."),
                     ("PhilHealth requires a waiting period.", False, "Not the reason evaluation is long."),
                     ("Patients must be on dialysis for six months first.", False, "No such requirement exists."),
                     ("Kidneys can only be transplanted at certain times of year.", False, "False.")],
         "sources": ["txcand2020"]},
        {"stem": "Which statement about age and transplant candidacy is correct?",
         "options": [("Age alone does not exclude a candidate; the team weighs overall health and frailty.", True, "KDIGO advises against exclusion on age alone."),
                     ("Patients older than 60 are never accepted.", False, "Many older adults are successfully transplanted."),
                     ("Only patients younger than 40 benefit.", False, "Benefit extends across age groups."),
                     ("Age determines eligibility more than any other factor.", False, "Overall physiologic reserve matters more than chronologic age.")],
         "sources": ["txcand2020"]},
        {"stem": "When the patient's only phone is shared and he can be reached only after 7 p.m., what belongs in the referral?",
         "options": [("His contact preferences and window, documented with his consent, so the program can plan calls.", True, "Contact feasibility determines whether the program can reach him."),
                     ("Nothing; the program will figure it out.", False, "Missed calls are a common reason referrals stall."),
                     ("Instructions that he must buy a new phone.", False, "Unrealistic and unkind."),
                     ("A note that he is difficult to reach and should be deprioritized.", False, "Prejudicial and not a clinical recommendation.")],
         "sources": []},
        {"stem": "What is the main purpose of shared decision-making when introducing transplant?",
         "options": [("To present options and tradeoffs and learn what matters to the patient, so the plan fits his life.", True, "Shared decision-making aligns care with the patient's priorities."),
                     ("To persuade every patient to choose transplant.", False, "Some patients reasonably choose dialysis or conservative care."),
                     ("To obtain consent for surgery.", False, "Surgical consent comes much later, from the surgical team."),
                     ("To decide which relative will donate.", False, "Donor decisions are voluntary and handled separately.")],
         "sources": ["txcand2020"]},
        {"stem": "Why are recipient care and donor advocacy separated on a transplant team?",
         "options": [("To prevent a conflict of interest between wanting a kidney for the recipient and protecting the donor.", True, "Separation protects the donor's free and informed choice."),
                     ("Because donors and recipients speak different languages.", False, "Not the reason."),
                     ("To reduce paperwork.", False, "It usually adds work; its purpose is protection."),
                     ("Because recipients do not need nurses.", False, "False.")],
         "sources": ["lentine2017"]},
    ],
    "exam": [
        {"stem": "A patient with CKD stage 4 and a steadily falling eGFR asks whether he must start dialysis before being referred for transplant. Best answer?",
         "options": [("No. Referral now allows evaluation to finish and keeps a preemptive transplant possible.", True, "Early referral is the guideline standard."),
                     ("Yes. Programs only evaluate patients on dialysis.", False, "False; preemptive evaluation is preferred."),
                     ("Yes, for at least one year.", False, "No minimum dialysis period is required."),
                     ("Only if a sibling agrees to donate.", False, "Donor availability is not a referral prerequisite.")],
         "sources": ["txcand2020"]},
        {"stem": "Which entry best documents a closed-loop transplant referral?",
         "options": [("Received by named coordinator on a date; program to schedule evaluation; RN to call patient on a stated date.", True, "Receipt, next action, owner and date are all present."),
                     ("Referral sent.", False, "No receipt, owner or date."),
                     ("Patient informed to wait.", False, "No owner or follow-up."),
                     ("Referral discussed with family.", False, "Does not show the program received it.")],
         "sources": []},
        {"stem": "A family member asks the nurse to confirm the patient is 'a match' with his brother. No crossmatch result has been communicated. Best action?",
         "options": [("Explain that compatibility is determined by the laboratory and team, say who will communicate it, and document the request.", True, "Within scope and routed to the authorized source."),
                     ("Say they are probably a match because they are brothers.", False, "Speculation about compatibility is outside scope."),
                     ("Read the raw laboratory printout to the family.", False, "Interpreting compatibility is not a nursing role."),
                     ("Refuse to speak with the family.", False, "Families deserve honest information about the process.")],
         "sources": ["ra9173"]},
    ],
}
