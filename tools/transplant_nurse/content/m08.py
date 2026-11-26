# -*- coding: utf-8 -*-
MODULE = {
    "sub": "Why the infections that threaten a recipient change month by month, how CMV and BK polyomavirus are prevented and watched for under the newest international consensus, what tropical infections add in the Philippines, and how to triage a fever phone call so that an unstable patient is never left waiting for clinic.",
    "desc": "Transplant Nurse Module 8: infection risk timeline after kidney transplant, CMV prevention (prophylaxis, preemptive monitoring, letermovir), BK polyomavirus surveillance (2024 consensus), Pneumocystis prophylaxis, vaccines, tuberculosis, dengue, leptospirosis and Strongyloides in the Philippines, and fever triage for Philippine registered nurses.",
    "keywords": "kidney transplant infection nursing, CMV prophylaxis letermovir valganciclovir, BK virus screening transplant, fever after kidney transplant triage, PJP prophylaxis cotrimoxazole, vaccines after transplant",
    "image_alt": "A nurse on the phone at a transplant clinic desk, holding a structured fever triage form, with a timeline poster of post-transplant infection risk on the wall behind her.",
    "objectives": [
        "Describe how infection risk changes over the first year and why rejection treatment raises it again.",
        "Explain CMV risk by donor and recipient serostatus, and the difference between prophylaxis and preemptive monitoring.",
        "Describe the BK polyomavirus screening schedule and why an asymptomatic result matters.",
        "Teach prevention: prophylaxis adherence, vaccines, food and water safety, and tropical exposures.",
        "Triage a fever or illness call, route unstable patients to emergency care, and close the loop on results.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "A calendar of risk",
         "html": """
<p>Picture the first year after transplant as a calendar with three seasons. In the first month, the threats are the ones any surgical patient faces: the wound, the bladder catheter, intravenous lines, hospital-acquired pneumonia, and occasionally an infection carried in the donor organ. From roughly the second to the sixth month, when immunosuppression is at its peak and prophylaxis is ending, opportunistic infections appear: cytomegalovirus (CMV), BK polyomavirus (BKPyV), Pneumocystis, fungi, and reactivated tuberculosis. After that, most recipients face ordinary community infections, but each one can be more severe, and the calendar resets whenever immunosuppression is intensified to treat rejection.</p>
<p>The picture has a limit. A calendar runs on dates; infection risk runs on the net state of immunosuppression, the total dose and duration of the drugs plus anything else that weakens defenses, such as a CMV infection or low lymphocytes. The dates are only a proxy for it. A recipient with a heavily treated rejection at month 10 may be back in the high-risk season. And immunosuppression blunts the body's alarm system: fever may be low or absent, white cell counts may not rise, and a serious infection can look like mild fatigue.</p>
<div class="tc-plain"><span class="tc-lab">In plain words</span>Do not wait for a high fever. In a recipient, "I feel unusually weak and I am passing less urine" can be the whole story of a serious infection.</div>
"""},
        {"id": "signs", "nav": "Quiet signs", "tag": "Physiology", "h2": "Why infection looks different after transplant",
         "html": """
<p>Fever, redness, swelling and pain are not the infection itself. They are the body's inflammatory response to it. Immunosuppressive drugs are designed to quiet that response. So the drugs that protect the graft also hide the warning signs of infection, and a recipient can be seriously ill with surprisingly little to show for it.</p>
<p><strong>The net state of immunosuppression.</strong> Infection risk depends on the sum of everything that weakens defenses at a given time: the drug doses, recent rejection treatment, low white cell or lymphocyte counts, diabetes, poor nutrition, an indwelling catheter or stent, an open wound, and viral infections such as cytomegalovirus that themselves suppress immunity. Two recipients on the same tablets can carry very different risk. Ask about all of it, not only the medicine list.</p>
<div class="table-wrap"><table>
<thead><tr><th>Usual sign</th><th>How it can change after transplant</th><th>What to look for instead</th></tr></thead>
<tbody>
<tr><td>Fever</td><td>Steroids lower it; a recipient may have a serious infection at 37.6 °C</td><td>Chills, sweats, feeling "not right," a new fast heart rate</td></tr>
<tr><td>Raised white cell count</td><td>Mycophenolate and other drugs may keep it normal or low</td><td>Trends, other laboratory clues, the whole clinical picture</td></tr>
<tr><td>Localized pain and redness</td><td>Less inflammation means less pain, even with pyelonephritis or a wound infection</td><td>Mild graft tenderness, wound drainage, a subtle change in the skin</td></tr>
<tr><td>Cough and sputum in pneumonia</td><td>Some infections, such as Pneumocystis, cause little sputum</td><td>Breathlessness on walking, a falling oxygen saturation</td></tr>
<tr><td>Confusion</td><td>May be the first or only sign in an older recipient</td><td>Any change in behavior reported by the family</td></tr>
</tbody></table></div>
<p><strong>The adrenal question.</strong> A recipient taking prednisone every day has an adrenal gland that has learned to rest. In a severe infection the body cannot make the extra cortisol it needs, and the blood pressure may fall more than expected. Whether to give additional steroid is a decision for the team. Your part is to tell every new team caring for the patient that he takes long-term steroids, and never to let a steroid dose be omitted because the patient is "nil by mouth."</p>
<div class="tc-keyp"><span class="tc-lab">Remember</span>In a transplant recipient, mild signs do not mean mild illness. Take vague symptoms seriously, and judge by the whole picture, including trends, not by the thermometer alone.</div>
<div class="tc-scene"><span class="tc-lab">In the transplant clinic &middot; fictional</span><p>Mr. Lim, 58, nine weeks after transplant, comes for a routine visit. He has "just a little cough" and his temperature is 37.4 °C. But walking from the elevator to the clinic left him breathless, and his oxygen saturation at rest is 93 percent, falling to 88 percent after a short walk in the corridor.</p><p>You recognize that breathlessness on exertion with a low-grade temperature, in the first months, is a pattern that needs prompt assessment. You report it to Dr. Santos at once rather than adding it to the end-of-clinic list. Mr. Lim is admitted that afternoon for investigation.</p><p class="tc-scene-take"><b>What this shows.</b> A walking oxygen saturation found what the thermometer missed. Look for function, not only fever.</p></div>
"""},
        {"id": "cmv", "nav": "CMV", "tag": "Evidence", "h2": "Cytomegalovirus: risk, prevention and monitoring",
         "html": """
<p>CMV is a herpesvirus most adults carry silently. After transplant it can reactivate in a seropositive recipient (R+) or be transmitted from a seropositive donor (D+). Without prevention, it causes fever, low white cells, hepatitis, colitis, pneumonitis, and it is linked to rejection and poorer graft survival. Risk depends on serostatus and on the intensity of immunosuppression: donor-positive, recipient-negative (D+/R−) recipients are at highest risk; R+ recipients are intermediate; D−/R− recipients are at low risk.</p>
<p>The Fourth International Consensus Guidelines on CMV in solid-organ transplantation (2025) support two prevention strategies.[[kotton2025]]</p>
<div class="tc-cards">
<div class="tc-card"><b>Universal prophylaxis</b>An antiviral is given to all at-risk recipients for a defined period after transplant (months), usually valganciclovir. Simple to run; misses late-onset disease after it stops.</div>
<div class="tc-card"><b>Preemptive monitoring</b>Blood CMV DNA is measured on a schedule (often weekly) and treatment starts when the viral load crosses a center threshold. Avoids drug toxicity in many patients; demands reliable, timely testing and follow-up.</div>
</div>
<p><strong>Letermovir.</strong> In a randomized trial of 601 high-risk (D+/R−) kidney recipients, letermovir prophylaxis was noninferior to valganciclovir for preventing CMV disease through week 52 (10.4 versus 11.8 percent), with far fewer cases of low white cell counts through week 28 (26 versus 64 percent), an important advantage because valganciclovir and mycophenolate both suppress the bone marrow.[[limaye2023]] CMV disease was the trial's patient-relevant end point; the lower rate of detectable CMV DNA in the blood with letermovir is a surrogate. Access and cost determine its use locally.</p>
<p><strong>The nurse's part.</strong> Know which strategy your center uses for each patient, the stop date of any prophylaxis, and the monitoring schedule. Make sure prophylaxis doses are adjusted to kidney function as ordered, that each viral load result has an owner, and that patients know the symptoms to report, particularly after prophylaxis ends.</p>
<div class="tc-scene"><span class="tc-lab">In the transplant clinic &middot; fictional</span><p>Mrs. Aquino received a kidney from a CMV-positive donor; she was CMV-negative. She finished six months of valganciclovir three weeks ago. Today she says she has felt "tired and feverish in the afternoons" for a week, and her white cell count is lower than at her last visit.</p><p>You recognize the pattern: a high-risk recipient, soon after prophylaxis stopped, with fever and falling white cells. You ask the team whether a CMV viral load should be drawn today rather than at her next visit, and you make sure the result has an owner before she leaves.</p><p class="tc-scene-take"><b>What this shows.</b> Late-onset CMV appears after prophylaxis ends. Knowing the stop date tells you when to be most alert.</p></div>
"""},
        {"id": "bk", "nav": "BK polyomavirus", "tag": "Evidence", "h2": "BK polyomavirus: the silent graft infection",
         "html": """
<p>Most people acquire BKPyV in childhood; it lies dormant in the urinary tract. Under immunosuppression, particularly with tacrolimus, higher steroid exposure and after rejection treatment, it can replicate in the graft's tubular cells, causing BKPyV nephropathy and graft loss. It produces no symptoms until creatinine rises, which is why it must be screened for.</p>
<p>The Second International Consensus Guidelines (2024), graded with the GRADE method, recommend screening all kidney recipients for BKPyV DNA in plasma monthly until month 9, then every 3 months until 2 years after transplant (3 years in children). Where plasma testing is not available, urine cytology for "decoy cells" at similar intervals can help exclude nephropathy, with plasma testing when decoy cells appear. For DNA loads persisting above 1,000 copies/mL, or exceeding 10,000 copies/mL, or biopsy-proven nephropathy, immunosuppression should be reduced in predefined steps. The consensus does not support leflunomide, cidofovir, quinolones or IVIG for treatment.[[kotton2024]] The viral load is a surrogate; what screening protects is the graft. The consensus judges routine screening cost-effective and beneficial for clinical outcomes and quality of life.[[kotton2024]]</p>
<div class="tc-keyp"><span class="tc-lab">Remember</span>An asymptomatic BK result is not a "routine" result. It can mean the graft is already being injured. Make sure it is reviewed by the team within the center's interval, that the patient is told the plan, and that the next test is booked.</div>
<div class="tc-scene"><span class="tc-lab">At the results desk &middot; fictional</span><p>On Friday afternoon you find a plasma BK result in the inbox: 18,000 copies/mL, collected eight days ago. The patient, Mr. Fernandez, has a normal creatinine and "feels fine." The result has not been opened by anyone.</p><p>You flag it to the transplant nephrologist that afternoon instead of leaving it for Monday rounds. The team plans a stepwise reduction of immunosuppression. You call Mr. Fernandez, explain the plan, have him repeat the new dose instructions, and book his repeat test.</p><p class="tc-scene-take"><b>What this shows.</b> BK nephropathy is silent until creatinine rises. An unopened result is the most common way it is missed.</p></div>
"""},
        {"id": "prevention", "nav": "Prevention", "tag": "Practice", "h2": "Prophylaxis, vaccines, food and the tropics",
         "html": """
<p><strong>Pneumocystis.</strong> Pneumocystis jirovecii pneumonia (PJP) should not occur while a patient takes trimethoprim-sulfamethoxazole (TMP-SMX) prophylaxis. American Society of Transplantation guidance recommends prophylaxis for at least 6 to 12 months after transplant, preferably with TMP-SMX, and notes higher risk with low lymphocyte counts, CMV infection, low antibody levels (hypogammaglobulinemia), treated rejection, corticosteroids and age over 65.[[fishman2019]] TMP-SMX can raise potassium and creatinine slightly; report these as ordered rather than stopping the drug.</p>
<p><strong>Vaccines.</strong> Live vaccines are generally avoided after transplant. Inactivated vaccines, including annual influenza, can be given after transplant once the team judges immunosuppression has stabilized, typically a few months after surgery. Household contacts should also be vaccinated.[[danziger2019]] Coordinate every vaccine with the transplant team.</p>
<p><strong>Food and water.</strong> Teach safe water (boiled or treated), thorough cooking of meat, eggs and seafood, washing produce, and avoiding raw <em>kinilaw</em>, unpasteurized dairy and street food of uncertain hygiene, especially in the early months.</p>
<p><strong>Infections that matter more in the Philippines</strong></p>
<ul>
<li><strong>Tuberculosis.</strong> Recipients have a much higher risk than the general population, and disease is often extrapulmonary or atypical. Treatment with rifampicin requires major immunosuppression adjustment (Module 6).[[subramanian2019]]</li>
<li><strong>Dengue.</strong> Fever in the rainy season may be dengue; watch platelet counts, fluid balance and warning signs, and do not give NSAIDs.</li>
<li><strong>Leptospirosis.</strong> Wading in floodwater carries risk of leptospirosis and acute kidney injury; ask about exposure after typhoons and floods.</li>
<li><strong>Strongyloides.</strong> A gut parasite that can cause overwhelming hyperinfection when corticosteroids are given; candidates from endemic areas are screened or treated before transplant.</li>
</ul>
<div class="tc-scene"><span class="tc-lab">By phone, after a typhoon &middot; fictional</span><p>Three days after floodwater rose through his barangay in Malabon, Mr. Ramos calls. He waded through knee-deep water to rescue his neighbor's children. Now he has fever, severe calf pain and red eyes, and he is passing less urine.</p><p>You recognize a possible leptospirosis exposure in an immunosuppressed recipient with falling urine. You do not suggest waiting to see. You direct him to the emergency department now, call ahead to the transplant team, and record his exposure history so the emergency staff hear it from the start.</p><p class="tc-scene-take"><b>What this shows.</b> Local exposures change the differential. Ask about floodwater, mosquitoes and sick contacts on every fever call.</p></div>
"""},
        {"id": "urinary", "nav": "Urinary infection", "tag": "Practice", "h2": "The commonest infection: urine, stents and the graft",
         "html": """
<p>Urinary tract infection is the most frequent bacterial infection after kidney transplant. The reasons are anatomical as much as immunological. The new ureter joins the bladder over a temporary stent; the urinary catheter stays in for days; the stent remains for weeks; and immunosuppression weakens the bladder's own defenses. A Cochrane review found that stented patients had more urinary infections unless prophylactic cotrimoxazole was given.[[wilson2013]]</p>
<p><strong>When infection reaches the graft.</strong> An infection that climbs to the transplanted kidney (graft pyelonephritis) inflames it and can cause acute kidney injury. Because the graft sits just under the skin of the lower abdomen, tenderness over it is a useful sign, but immunosuppression may make it mild. Fever, chills, graft tenderness and a creatinine rise together suggest graft pyelonephritis, and the patient usually needs same-day assessment and intravenous treatment as ordered.</p>
<p><strong>Getting the specimen right.</strong> A contaminated sample leads to the wrong antibiotic, or to treatment the patient did not need.</p>
<ul>
<li>Collect a clean midstream sample, or a sample from the catheter's sampling port, never from the drainage bag.</li>
<li>Send it before the first antibiotic dose whenever the order allows, because treatment can sterilize the culture.</li>
<li>Label the date, time and collection method, and note whether a stent is still in place.</li>
<li>Track the result until a clinician has reviewed the culture and its sensitivities.</li>
</ul>
<p><strong>Antibiotics and the immunosuppressants.</strong> Some antibiotics change tacrolimus levels; clarithromycin and erythromycin can raise them sharply (Module 6). Trimethoprim, in cotrimoxazole, blocks the tubule's secretion of creatinine and of potassium, so creatinine and potassium may rise without any true loss of filtration, although true kidney injury must still be excluded. When a new antibiotic is started, check it against the patient's medicine list and report possible interactions to the prescriber and pharmacist.</p>
<div class="tc-scene"><span class="tc-lab">By phone &middot; fictional</span><p>Six weeks after transplant, Mrs. Cortez calls. She has burning on passing urine and has felt feverish since last night. She still has her stent; the removal is booked for next week. A local clinic has offered to start "clarithromycin for the infection."</p><p>You ask about chills, graft tenderness and urine output, and arrange same-day assessment at the transplant clinic, according to your protocol. You explain that clarithromycin can push her tacrolimus level dangerously high and that the transplant team will choose an antibiotic that suits her medicines. You tell Dr. Santos and note that the stent is still in place.</p><p class="tc-scene-take"><b>What this shows.</b> A urinary infection in a recipient is not routine. The stent, the graft and the drug interactions all change the plan.</p></div>
"""},
        {"id": "triage", "nav": "Fever calls", "tag": "Practice", "h2": "The fever or illness call",
         "html": """
<p>Use a structured approach so that nothing important is missed and the disposition is clear.</p>
<ol class="tc-flow">
<li><b>Where and how to reach</b>Confirm identity, current location and a callback number before anything else, in case the call drops.</li>
<li><b>Context</b>Months since transplant, recent rejection treatment, current immunosuppression and prophylaxis, recent procedures or stent.</li>
<li><b>Acuity</b>Breathing difficulty, confusion, fainting, chest pain, very low urine output, rigors, inability to keep medicines down, severe abdominal pain; temperature and blood pressure if a device is available.</li>
<li><b>Focus and exposures</b>Cough, urinary symptoms, diarrhea, rash, wounds; sick contacts, floodwater, mosquito exposure, travel.</li>
<li><b>Disposition</b>Emergency care now; same-day assessment; or advice and a defined callback, according to protocol and the transplant physician's direction.</li>
<li><b>Close the loop</b>Notify the transplant team, document advice and read-back, and track any tests ordered until they are reviewed.</li>
</ol>
<div class="tc-stop"><span class="tc-lab">Stop and call</span>A recipient with signs of systemic illness, instability, or inability to take immunosuppressants is routed to emergency care immediately, with the transplant program notified. Never defer such a patient to a routine clinic callback.</div>
<div class="tc-scene"><span class="tc-lab">By phone, 10:40 p.m. &middot; fictional</span><p>A woman calls about her husband, who had a transplant five months ago. He has fever and "is talking strangely." Then the line drops.</p><p>Because you asked for her location and a callback number in the first 20 seconds, you can call back. You reach her on the second try and direct her to the nearest emergency department immediately. You notify the transplant team and the receiving hospital, and you document the advice and her read-back.</p><p class="tc-scene-take"><b>What this shows.</b> Location and callback number come first. In an emergency call, they are the only details you cannot get later.</p></div>

<p>Vomiting and diarrhea deserve special mention: they cause dehydration and AKI, may prevent absorption of immunosuppressants, and diarrhea can paradoxically <em>raise</em> tacrolimus levels. These patients often need same-day assessment.</p>
"""},
        {"id": "elsewhere", "nav": "Admitted elsewhere", "tag": "Practice", "h2": "When a recipient is admitted to another ward or hospital",
         "html": """
<p>Many recipients are admitted with an infection to a general medical ward, or to a hospital nearer home that rarely cares for transplant patients. The infection may be treated well while the transplant is put at risk. A few predictable errors account for most of the harm.</p>
<div class="table-wrap"><table>
<thead><tr><th>Common error</th><th>Why it is dangerous</th><th>What the nurse does</th></tr></thead>
<tbody>
<tr><td>Immunosuppressants stopped or delayed because the patient is "nil by mouth" or not on the formulary</td><td>Missed doses invite rejection; omitted steroids risk adrenal crisis</td><td>Ask the team for an explicit plan for each drug; never omit silently; get the program's advice</td></tr>
<tr><td>A new drug that interacts with tacrolimus</td><td>Levels rise or fall sharply within days</td><td>Check every new drug against the list; ask the pharmacist; request a level when advised</td></tr>
<tr><td>NSAIDs for pain or fever</td><td>Reduce blood flow to the graft</td><td>Flag the transplant status; ask for an alternative</td></tr>
<tr><td>Contrast or other kidney-toxic tests without preparation</td><td>Adds kidney injury on top of illness</td><td>Make sure the team knows the patient has a single kidney with treated function</td></tr>
<tr><td>The transplant program not told</td><td>Decisions are made without the people who know the patient</td><td>Notify the program on admission and on major changes; give the ward the program's contact number</td></tr>
</tbody></table></div>
<p>Changes to immunosuppression during an infection, such as reducing or holding mycophenolate, are sometimes appropriate. They are decisions for the transplant team, made with the treating team, not by the ward on its own and not by the nurse.</p>
<p><strong>Isolation and hand hygiene.</strong> Recipients do not usually need special isolation for their own protection, but they need strict hand hygiene from everyone who touches them, and they should not share a room with a patient who has a transmissible infection, such as influenza or chickenpox, when this can be avoided. Follow your hospital's infection prevention policy.</p>
<div class="tc-scene"><span class="tc-lab">At a provincial hospital &middot; fictional</span><p>Mang Danilo, two years after transplant, is admitted to a provincial hospital with pneumonia. On the second day his daughter calls the transplant clinic: the ward has not given his tacrolimus or prednisone since admission because "the pharmacy does not stock them" and he is too breathless to swallow.</p><p>You take the ward's direct number and call the nurse in charge. You give her the program's contact for the admitting physician, explain that the steroid in particular must not be stopped abruptly, and tell Dr. Santos, who speaks with the admitting physician within the hour. They agree a plan for each drug, and the family brings his own supply in the meantime.</p><p class="tc-scene-take"><b>What this shows.</b> An infection treated well can still cost a graft if the immunosuppressants stop. Connect the treating team to the transplant program early.</p></div>
"""},
    ],
    "case": {
        "title": "Chills, weakness and less urine",
        "html": """
<p><strong>Saturday, 4:00 p.m., transplant hotline.</strong> Mrs. Garcia, 57, calls. She is five months after a deceased-donor transplant and stopped valganciclovir prophylaxis three weeks ago, as planned.</p>
<p>She has had chills since morning and feels "too weak to stand for long." She has passed "only a little urine" today. Her husband measured a temperature of 37.9 °C. She vomited her morning medicines, including tacrolimus, about an hour after taking them.</p>
<p>She lives 40 minutes from the nearest hospital. Her husband can drive. Halfway through the call she says she feels dizzy and needs to sit down.</p>
""",
        "acte": {
            "Assess": "Location and callback number first. Then breathing, confusion, dizziness or fainting, blood pressure if a home device is available, urine output, vomiting and which doses were lost, diarrhea, cough, urinary symptoms, and exposures.",
            "Communicate": "Notify the on-call transplant physician immediately. Document the advice, the read-back, and the receiving emergency department, and inform it that a transplant recipient is coming if your process allows.",
            "Teach": "Explain why she needs assessment today, what to bring (medicine list, transplant card, all her medicines), and that she should not drive herself if dizzy.",
            "Escalate": "Possible sepsis or CMV disease with reduced urine output and lost immunosuppressant doses: route to emergency care now. Arrange follow-up by the transplant team of ordered tests (blood cultures, CMV DNA, creatinine, tacrolimus level).",
        },
        "task": "Write the triage and routing record: time, location and callback, findings, disposition, physician notified, read-back, and the owner of pending results.",
        "outcome": """
<p>The nurse in the story had already taken her address and her husband's number in the first minute. When Mrs. Garcia said she felt dizzy, the nurse did not continue the full questionnaire. She told her to lie down, asked her husband to take her to the emergency department now, and had him repeat the name of the hospital.</p>
<p>She called the on-call transplant physician, then the emergency department, so they knew a recipient with fever, low urine output and lost immunosuppressant doses was on the way. She documented the time of each call and the read-back.</p>
<p>In the emergency department, Mrs. Garcia's blood pressure was low and her creatinine had doubled. She was admitted for intravenous fluids, cultures and a cytomegalovirus test. The test came back positive on Monday, which is where the second round begins.</p>
""",
    },
    "second_round": ("On Monday, a CMV DNA result requires callback, but the daytime desk is closed for a holiday.", "A triage and routing record showing the backup reviewer, acknowledgment, and patient communication."),
    "evidence_out": "Fever triage and abnormal-result follow-through.",
    "critical": "Deferring an unstable patient to a routine clinic callback.",
    "reflect": "If a recipient called your unit at 4 p.m. on a Saturday, who would answer, and how would they reach the transplant physician?",
    "practice": {
        "intro": "In clinic and on the hotline, supervised.",
        "items": [
            "Map each of your current recipients to a CMV strategy, prophylaxis stop date and BK screening schedule.",
            "Complete a simulated fever triage call using the structured form.",
            "Teach food and water safety and tropical exposure precautions using teach-back.",
            "Review a recipient's vaccine plan with the transplant team.",
            "Track a viral load result from collection to documented review and patient communication.",
        ],
    },
    "readings": [
        ("viral-infections-vaccinations-ckd.html", "Viral infections and vaccines in kidney disease."),
        ("dengue-aki-kidney.html", "Dengue and the kidney."),
        ("tropical-infection-aki.html", "Tropical infections that injure the kidney, including leptospirosis."),
    ],
    "calcs": ["calc-dengue-aki-risk.html", "calc-leptospirosis-aki-risk.html"],
    "terms": [
        ("Serostatus", "Whether a person has antibodies showing past infection with a virus such as CMV."),
        ("Universal prophylaxis", "Giving preventive antimicrobial medicine to all at-risk patients for a set period."),
        ("Preemptive monitoring", "Testing on a schedule for early viral replication and treating only when it appears."),
        ("DNAemia", "Viral DNA detectable in the blood."),
        ("Decoy cells", "Virus-infected urinary tract cells seen on urine cytology, suggesting BK polyomavirus replication."),
        ("Strongyloides hyperinfection", "Overwhelming spread of the Strongyloides parasite, usually triggered by corticosteroids."),
    ],
    "quiz": [
        {"stem": "Which CMV serostatus combination carries the highest risk after transplant?",
         "options": [("Donor positive, recipient negative (D+/R−).", True, "The recipient has no prior immunity to the transmitted virus."),
                     ("Donor negative, recipient negative.", False, "Lowest risk."),
                     ("Donor negative, recipient positive.", False, "Intermediate risk."),
                     ("Serostatus does not matter.", False, "It is central to risk stratification.")],
         "sources": ["kotton2025"]},
        {"stem": "What distinguishes CMV prophylaxis from a preemptive strategy?",
         "options": [("Prophylaxis gives antiviral medicine for a defined period; preemptive care monitors viral DNA and treats when replication appears.", True, "Both are accepted strategies."),
                     ("They are the same.", False, "Different approaches."),
                     ("Preemptive means treating everyone before surgery.", False, "Not the definition."),
                     ("Prophylaxis is only used after CMV disease.", False, "That is treatment.")],
         "sources": ["kotton2025"]},
        {"stem": "In the randomized trial in high-risk kidney recipients, how did letermovir compare with valganciclovir?",
         "options": [("Noninferior for preventing CMV disease, with fewer low white cell counts.", True, "CMV disease 10.4 versus 11.8 percent through week 52."),
                     ("Clearly inferior.", False, "It met noninferiority."),
                     ("It increased CMV disease threefold.", False, "Not observed."),
                     ("It caused more bone marrow suppression.", False, "Less marrow suppression.")],
         "sources": ["limaye2023"]},
        {"stem": "What BK polyomavirus screening schedule does the 2024 consensus recommend?",
         "options": [("Plasma BK DNA monthly until month 9, then every 3 months until 2 years.", True, "Three years in children."),
                     ("Only when creatinine rises.", False, "Screening detects infection before graft injury."),
                     ("Once at one year.", False, "Too infrequent."),
                     ("Weekly for life.", False, "Not recommended.")],
         "sources": ["kotton2024"]},
        {"stem": "Why is an asymptomatic BK DNAemia result important?",
         "options": [("It can signal risk to the graft and requires timely review and follow-up under the center protocol.", True, "BK nephropathy is silent until injury is advanced."),
                     ("It is harmless if the patient feels well.", False, "Silence is the danger."),
                     ("It means the patient has rejection.", False, "A different process, though related to immunosuppression."),
                     ("It requires leflunomide.", False, "The consensus does not support leflunomide.")],
         "sources": ["kotton2024"]},
        {"stem": "What is the main management step for persistent significant BK DNAemia according to the consensus?",
         "options": [("Stepwise reduction of immunosuppression as directed by the team.", True, "Reducing antiproliferatives, CNI or both."),
                     ("Ciprofloxacin.", False, "Quinolones are not supported."),
                     ("IVIG for all.", False, "Not supported."),
                     ("Increasing tacrolimus.", False, "Would worsen replication.")],
         "sources": ["kotton2024"]},
        {"stem": "When does PJP prophylaxis guidance recommend coverage after transplant?",
         "options": [("For at least 6 to 12 months, preferably with TMP-SMX.", True, "Guidance from the American Society of Transplantation."),
                     ("Only during the hospital stay.", False, "Too short."),
                     ("Only if the patient develops cough.", False, "It is preventive."),
                     ("Never; PJP is rare.", False, "PJP is a recognized risk.")],
         "sources": ["fishman2019"]},
        {"stem": "Which vaccine type is generally avoided after kidney transplant?",
         "options": [("Live vaccines.", True, "Risk of vaccine-strain infection under immunosuppression."),
                     ("Inactivated influenza vaccine.", False, "Recommended annually."),
                     ("Inactivated pneumococcal vaccine.", False, "Recommended."),
                     ("Hepatitis B vaccine.", False, "Inactivated; may be given.")],
         "sources": ["danziger2019"]},
        {"stem": "A recipient calls with chills, weakness and reduced urine, and vomited her medicines. What is the right disposition?",
         "options": [("Emergency assessment now, with the transplant team notified and the advice documented.", True, "Possible sepsis with lost immunosuppression."),
                     ("Advise rest and a clinic visit next week.", False, "Unsafe delay."),
                     ("Tell her to double tomorrow's doses.", False, "Unauthorized and unsafe."),
                     ("Advise paracetamol and call if worse.", False, "Inadequate for systemic illness.")],
         "sources": []},
        {"stem": "What is the first thing to establish in a fever triage call?",
         "options": [("Identity, location and a callback number.", True, "So help can be directed if the call drops."),
                     ("The patient's favorite hospital.", False, "Not first."),
                     ("Her PhilHealth status.", False, "Not first."),
                     ("Her diet history.", False, "Not first.")],
         "sources": []},
        {"stem": "Why can serious infection look mild in a transplant recipient?",
         "options": [("Immunosuppression blunts fever and inflammatory responses.", True, "Signs may be subtle."),
                     ("Recipients do not get serious infections.", False, "They are at higher risk."),
                     ("Tacrolimus cures infections.", False, "False."),
                     ("Infections only cause high fever.", False, "Fever may be absent.")],
         "sources": ["fishman2019"]},
        {"stem": "A recipient wades through floodwater after a typhoon and develops fever and calf pain. Which infection should be considered?",
         "options": [("Leptospirosis.", True, "Floodwater exposure is the classic risk."),
                     ("CMV only.", False, "Exposure history points to leptospirosis."),
                     ("Influenza only.", False, "Less consistent with exposure."),
                     ("BK polyomavirus.", False, "Not acquired from floodwater.")],
         "sources": []},
        {"stem": "Why are candidates from endemic areas screened or treated for Strongyloides?",
         "options": [("Corticosteroids can trigger life-threatening hyperinfection.", True, "Pre-transplant treatment prevents this."),
                     ("Strongyloides causes rejection directly.", False, "Not the main concern."),
                     ("It is required by PhilHealth.", False, "Not the reason."),
                     ("It is not relevant in the Philippines.", False, "The Philippines is endemic.")],
         "sources": []},
        {"stem": "Why does rejection treatment change infection risk?",
         "options": [("Intensified immunosuppression raises the risk of opportunistic infections again.", True, "The risk calendar resets."),
                     ("It lowers infection risk.", False, "It raises it."),
                     ("It has no effect.", False, "It has a major effect."),
                     ("It only affects bacterial infections.", False, "Viral and fungal risk also rise.")],
         "sources": ["kotton2025", "kotton2024"]},
        {"stem": "What completes the loop on a CMV viral load result?",
         "options": [("Review by the authorized clinician, documented action, and communication with the patient.", True, "Closed-loop result management."),
                     ("The result appearing in the system.", False, "Availability is not review."),
                     ("Printing the result.", False, "Not review."),
                     ("Telling the patient to check online.", False, "Not closed loop.")],
         "sources": []},
    ],
    "exam": [
        {"stem": "A recipient reports chills, weakness and reduced urine. What is the correct sequence?",
         "options": [("Establish location and callback, assess acuity, route to emergency care if unstable, notify the transplant team, and document the disposition.", True, "Structured triage."),
                     ("Schedule a routine clinic visit.", False, "Unsafe for possible sepsis."),
                     ("Advise more fluids and rest only.", False, "Inadequate."),
                     ("Tell her to stop her immunosuppressants.", False, "Unauthorized.")],
         "sources": []},
        {"stem": "What makes an asymptomatic BK result important?",
         "options": [("It can signal risk to the graft and needs timely interpretation and follow-up under protocol.", True, "Silent graft injury."),
                     ("Nothing; it can wait a year.", False, "Too long."),
                     ("It proves rejection.", False, "Different process."),
                     ("It requires antibiotics.", False, "Not supported.")],
         "sources": ["kotton2024"]},
        {"stem": "What distinguishes CMV prophylaxis from preemptive care?",
         "options": [("Prophylaxis gives preventive medicine for a defined risk period; preemptive care monitors replication and treats per protocol.", True, "Two accepted strategies."),
                     ("Prophylaxis is given only after disease.", False, "That is treatment."),
                     ("Preemptive care uses vaccines.", False, "No CMV vaccine is in routine use."),
                     ("They are identical.", False, "Different.")],
         "sources": ["kotton2025"]},
    ],
}
