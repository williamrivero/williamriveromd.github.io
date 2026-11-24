# -*- coding: utf-8 -*-
"""Physician on Duty, Module 27: Other Roads: Transplant, Peritoneal Dialysis, and Conservative Care.
Written for this series from published sources."""

MODULE = {
    "image_alt": "A young Filipina teacher in a dialysis chair at dawn, her younger brother seated beside her, while the physician on duty listens. A bag of blood for transfusion hangs on a pole, not yet connected.",
    "objectives": [
        "Explain in plain words the three long-term paths after kidney failure and what each asks of the patient.",
        "Identify a patient who has not been referred for transplant evaluation and flag the gap to the attending nephrologist, citing the Kidney Disease: Improving Global Outcomes (KDIGO) 2020 candidate guideline.",
        "List what keeps a patient ready for transplant, and recognize the events that must reach the transplant team.",
        "Describe how peritoneal dialysis works and recognize the patient who arrives with possible peritonitis, exit-site infection, or fluid overload.",
        "Describe conservative kidney management and the evidence that compares it with dialysis in older patients, including its limits.",
        "Receive a patient who returns to hemodialysis after a failed transplant or failed peritoneal dialysis safely, per your unit&rsquo;s protocol.",
    ],
    "big": """
{{plain:Picture a fork in a road. Everyone with kidney failure arrives at the same fork. One road leads to a new kidney. One leads to a machine or a bag of fluid that does part of the kidney&rsquo;s work. One leads to care that keeps the person comfortable without dialysis. Nobody should be walked down one road without being shown the others.}}
<p>The picture has a limit. Roads on a map are fixed, and these are not. A patient can move from one to another: from peritoneal dialysis to hemodialysis, from hemodialysis to a transplant, from a failed transplant back to dialysis. Some roads close with time. Antibodies, frailty, and infection can shut the transplant road unless someone keeps it open.</p>
{{cards:Key terms for this module|Kidney transplant::Surgery that places a donor kidney in the lower abdomen. The new kidney filters continuously and makes hormones.|Peritoneal dialysis (PD)::Dialysis inside the body. Fluid placed in the abdomen draws waste and water across the lining of the abdomen.|Conservative kidney management (CKM)::Planned, active kidney care without dialysis, focused on symptoms, quality of life, and the person&rsquo;s goals.|Sensitization::The formation of antibodies against human leukocyte antigens (HLA) after exposure to another person&rsquo;s tissue, such as blood, a pregnancy, or an earlier transplant.|Immunosuppressive medicines::Medicines that keep the immune system from rejecting a transplanted kidney.|Peritonitis::Infection and inflammation of the lining of the abdomen. In PD it is a serious complication.}}
<p>Most patients in your chairs will stay on hemodialysis. Some could be living with a transplant, or dialyzing at home, and nobody told them. A few have chosen a path without dialysis. Your work is to notice the missed conversation, to protect the patient&rsquo;s chance of a transplant during your shift, and to recognize the PD or transplant patient who comes to your unit unwell. The long-term decision belongs to the patient and the attending nephrologist.</p>
""",
    "case": {"title": "Nobody ever told me I could be listed", "html": """
<p>Ms. Cristina Bautista is 34 and teaches grade four in a public school. She has had immunoglobulin A (IgA) nephropathy, in which antibody deposits damage the kidney filters, since college. She has dialyzed three times a week for three years through a left arm fistula. Today she is in station 6 for the 6 AM shift.</p>
<p>The nurse, Mr. Jomar Reyes, reports her numbers: a pre-dialysis blood pressure of 142/86 mm Hg, a weight gain of 2.4 kg since the last session, and a hemoglobin of 7.8 g/dL from last week. These are illustrative values, not targets. The ward requested packed red cells to be given during today&rsquo;s session for &ldquo;low hemoglobin.&rdquo; She is not bleeding, and she is not breathless.</p>
<p>While Mr. Reyes prepares the transfusion form, Ms. Bautista turns to you. &ldquo;My younger brother says he will give me a kidney,&rdquo; she says. &ldquo;Nobody ever told me I could be listed. Is it too late?&rdquo; Her chart shows no documented discussion of transplant.</p>
""", "questions": ["What should happen to the transfusion plan before it starts, and why does it matter for her future transplant?",
                  "Should she hear about transplant, and what does the KDIGO 2020 guideline say about informing and referring her?",
                  "What exactly do you tell her today, whom do you call, and what do you write?"]},
    "sections": [
        ("roads", "Three roads", "Three roads from the same starting point", """
{{fig:pod27_roads}}
<h3>What each road replaces</h3>
<p>A working transplant replaces almost everything a kidney does. It filters all day and all night. It makes erythropoietin, the hormone that drives red cell production, and activates vitamin D. It excretes acid and potassium in step with what the patient eats. The cost is surgery, a lifelong course of immunosuppressive medicines, and the infections and cancers those medicines make more likely.</p>
<p>Dialysis replaces only part of the kidney&rsquo;s clearing work: it removes waste, water, and potassium and corrects acid, but it makes no hormones. Hemodialysis does this fast and intermittently: about twelve hours a week instead of 168. PD works every day, more gently, but clears small solutes less efficiently per hour than a hemodialysis session. Because neither makes hormones, your patients need erythropoiesis-stimulating agents and active vitamin D.</p>
<p>Conservative kidney management replaces nothing. It relies on the patient&rsquo;s residual kidney function (Module 3), on diet and medicines, and on symptom care.</p>
{{fig:modalities|The dialysis road has its own branches: in-center hemodialysis, home hemodialysis, and peritoneal dialysis.}}
<div class="table-wrap"><table>
<thead><tr><th>Road</th><th>What it replaces</th><th>Where it happens</th><th>Who does the work</th><th>Main risks</th></tr></thead>
<tbody>
<tr><td>Kidney transplant</td><td>Filtration, hormones, acid and potassium handling, continuously</td><td>Transplant center, then home</td><td>The patient, with lifelong medicines and clinic visits</td><td>Surgery, rejection, infection, cancer, medicine side effects</td></tr>
<tr><td>In-center hemodialysis</td><td>Part of filtration, about twelve hours a week</td><td>The dialysis unit</td><td>The unit staff</td><td>Access problems, falling pressure, swings in fluid and potassium, bloodstream infection</td></tr>
<tr><td>Home hemodialysis</td><td>Part of filtration, often on more days</td><td>Home</td><td>The patient and a trained helper</td><td>The same as in-center, managed at home</td></tr>
<tr><td>Peritoneal dialysis</td><td>Part of filtration, every day</td><td>Home</td><td>The patient or a caregiver</td><td>Peritonitis, exit-site infection, catheter problems, fluid overload</td></tr>
<tr><td>Conservative kidney management</td><td>None. Uses remaining kidney function</td><td>Clinic and home</td><td>The patient, family, and the kidney team</td><td>Symptoms of advancing kidney failure, shorter survival in some groups</td></tr>
</tbody></table></div>
<h3>What the evidence shows about transplant</h3>
<p>No randomized trial has compared transplant with dialysis. Healthier patients are chosen for transplant, so a simple observational comparison flatters it.</p>
<p>Tonelli and colleagues reviewed 110 cohort studies with 1,922,300 participants. Most studies found that transplant was associated with lower mortality and fewer cardiovascular events than dialysis, and quality of life was substantially better. The studies were too different to pool into one number.[[tonelli2011]]</p>
<p>Wolfe and colleagues reduced the selection problem. In the United States registry, they compared transplant recipients only with patients also accepted onto the waiting list, and so also judged fit. In the first two weeks after surgery, the risk of death was 2.8 times higher with transplant. By 18 months, it was much lower (relative risk 0.32). Over the long term, mortality was 48% to 82% lower than on the waiting list, depending on the subgroup.[[wolfe1999]]</p>
{{fig:tx_overview|A kidney transplant in one picture: donor types, the operation, and life afterward.}}
<p>Even this comparison cannot remove all selection, and the data come from another country and era. The direction of the finding has held across many cohorts.</p>
{{key:Transplant is the road with the best average outcomes for those who qualify. It is still surgery, with early risk and lifelong medicines. The comparison is never &ldquo;transplant versus nothing.&rdquo;}}
"""),
        ("refer", "Who should hear", "Who should hear about transplant, and when", """
<p>A patient cannot choose a road nobody has described. Sometimes the barrier is not a medical contraindication but a conversation that never happened.</p>
<p>The KDIGO 2020 guideline on transplant candidates sets out who should hear about transplant and when to refer.[[kdigo_txcand2020]] KDIGO grades a recommendation 1 (&ldquo;we recommend&rdquo;) or 2 (&ldquo;we suggest&rdquo;), and the quality of evidence A (high) to D (very low). Statements marked &ldquo;Not Graded&rdquo; are expert guidance without a formal grade.</p>
<div class="table-wrap"><table>
<thead><tr><th>KDIGO 2020 statement</th><th>Grade</th><th>What it means on your shift</th></tr></thead>
<tbody>
<tr><td>Patients with chronic kidney disease (CKD) stages G4 to G5 who are expected to reach kidney failure should be informed of, educated about, and considered for transplant, regardless of socioeconomic status, sex, gender identity, or race (1.1)</td><td>1D</td><td>Every patient in your unit falls under this statement unless a reason has been documented</td></tr>
<tr><td>Refer potential candidates for evaluation at least 6 to 12 months before dialysis is expected to start (1.1.1)</td><td>Not Graded</td><td>Applies to clinic patients. In your unit, the window has usually passed</td></tr>
<tr><td>Refer candidates already on dialysis when medically stable and kidney failure is judged irreversible (1.1.2)</td><td>Not Graded</td><td>A patient on dialysis for months or years is not &ldquo;too late&rdquo;</td></tr>
<tr><td>Pre-emptive transplant from a living donor is the preferred treatment for eligible patients (1.4)</td><td>1A</td><td>A family member&rsquo;s offer is worth reporting the same day</td></tr>
<tr><td>Do not exclude patients because of age alone (2.1.1). Consider age with other illness, including frailty (2.1)</td><td>1A for 2.1.1. Not Graded for 2.1</td><td>&ldquo;Too old&rdquo; is not a reason by itself</td></tr>
<tr><td>Assess adherence and its barriers before transplant (5.1). Refer patients with barriers for education and support (5.2)</td><td>Not Graded</td><td>Missed sessions call for help, not automatic exclusion</td></tr>
</tbody></table></div>
<p>Note the grades. The 1A statements concern living-donor transplant and age. Informing everyone is a strong recommendation on very low quality evidence (1D). There are no trials behind it; it rests on a principle: a patient who is not told cannot choose.[[kdigo_txcand2020]]</p>
<p>The kidney failure risk equation calculator on this site helps clinics time referral under 1.1.1 for patients not yet on dialysis.</p>
<h3>The Philippine frame</h3>
<p>In the Philippines, the Department of Health (DOH) requires every transplant center to have a Hospital Transplant Ethics Committee. It reviews each donor and recipient pair to make sure the donation is voluntary and free of payment. A descriptive survey found that most approved pairs involved living unrelated donors, and that committee structure varied.[[abacan2021]] A sibling&rsquo;s offer enters this process at the transplant center.</p>
<p>Referral centers, steps, and costs are set locally. Ask your medical director, and do not quote costs or waiting times from memory. Scores a patient may read about online, such as the estimated post-transplant survival (EPTS) score, are United States allocation tools that may not apply here.</p>
{{flow:From &ldquo;Can I be listed?&rdquo; to a documented flag|The patient asks, or you see that the patient may be eligible::Listen. Do not promise or rule out anything.|Check the chart::Look for a documented transplant discussion, a referral, a waiting-list status, or a documented reason not to refer.|If nothing is documented::Tell the attending nephrologist the same day. Name the KDIGO statement: every patient expected to reach kidney failure should be informed and considered (1D).|The nephrologist decides::The nephrologist discusses transplant with the patient and refers to a transplant center if appropriate.|Record the flag::Write the patient&rsquo;s question, the time you informed the nephrologist, and the plan.}}
{{key:If the chart does not show that transplant was discussed, tell the attending nephrologist. Silence is a barrier you can remove.}}
"""),
        ("ready", "Staying ready", "Staying transplant-ready in the dialysis unit", """
<p>A patient on the waiting list is like a car kept tuned and fueled for a trip that could start any night, when the call for a deceased-donor kidney comes.</p>
<p>The picture has a limit. A car is either ready or not. Readiness for transplant erodes quietly, through events that seem minor on the day: a transfusion, an infection, a changed phone number.</p>
<h3>Why a transfusion matters: sensitization</h3>
<p>Every person&rsquo;s cells carry surface proteins called human leukocyte antigens (HLA). The immune system uses them to tell self from non-self. Blood, a pregnancy, or a transplant exposes it to another person&rsquo;s HLA, and it may make antibodies against them.</p>
<p>Those antibodies persist. If a donor kidney carries the same antigens, the antibodies can attack it, sometimes within hours. The laboratory therefore screens candidates for HLA antibodies and tests each donor against the recipient&rsquo;s blood. The more antibodies, the fewer donors will match, and the longer the wait.</p>
{{fig:pod27_sensitization}}
<p>KDIGO asks that all sensitizing events, including blood product transfusion (platelets too), pregnancy, and miscarriage, be communicated to the HLA laboratory that serves the transplant program (19.1, Not Graded). It asks that the program test for HLA antibodies at evaluation, at regular intervals while the patient waits, and after a sensitizing event (19.2, Not Graded).[[kdigo_txcand2020]] Both rest on physiology and how matching works, not on trials.</p>
<p>The decision to transfuse belongs to the attending nephrologist (Module 21). Unless the patient is bleeding or unstable, there is usually time to call first.</p>
<h3>Infection screening and vaccines</h3>
<p>Immunosuppressive medicines after transplant can let a hidden infection flare. KDIGO therefore recommends screening every candidate for human immunodeficiency virus (HIV), hepatitis C, and hepatitis B, the last with hepatitis B surface antigen (HBsAg), antibody to the surface antigen (anti-HBs), and antibody to the core antigen (anti-HBc). Each of these is graded 1A. Where tuberculosis (TB) is more common, it suggests screening for latent TB as local guidelines direct (2C). It recommends that vaccine series be started before transplant, on an accelerated schedule if needed (1B), and suggests a dental evaluation (2C).[[kdigo_txcand2020]] Your unit already tests for these viruses on a schedule (Module 29). A new positive result in a waitlisted patient must reach the transplant team.</p>
{{cards:Transplant-readiness check at the chair|Serology::Hepatitis B, hepatitis C, and HIV results current per your unit&rsquo;s schedule, with dates.|Vaccines::Hepatitis B and other vaccines recorded per your unit&rsquo;s protocol.|Transfusions::Any blood product since the last report, with date and place.|Infections and teeth::Recent infections, open wounds, dental pain, or a dental review not yet done.|Adherence::Missed or shortened sessions, and the reasons behind them.|Contact::The transplant center&rsquo;s number in the chart and the patient&rsquo;s current phone number.}}
{{formula:<strong>Worked example: a readiness review (decision walk-through, illustrative).</strong><br>Mr. Rodel Santos, 52, has been on the waiting list for two years.<br>1. Hepatitis B and C results current per unit schedule: yes.<br>2. HIV result on file: yes.<br>3. Transfusions in the past year: one, last month, at another hospital, not reported. <strong>Flag 1.</strong> Basis: KDIGO 19.1, communicate all sensitizing events (Not Graded).<br>4. Dental review: not done. <strong>Flag 2.</strong> Basis: KDIGO 10.4.1, dental evaluation per local guidelines (2C).<br>5. Phone number in the chart: outdated. <strong>Flag 3.</strong> Basis: a transplant offer needs a reachable patient.<br>Output: three flags reported to the attending nephrologist, each with its owner, written in the chart.<br><em>What it does not tell you:</em> whether he is still a good candidate. That is the transplant team&rsquo;s judgment.}}
{{call:Stop and call the attending nephrologist when a waitlisted patient is about to receive, or has received, a blood transfusion; when a waitlisted patient has a new positive hepatitis B, hepatitis C, or HIV result; or when a transplant offer call comes while the patient is in the chair. For an offer, follow the transplant center&rsquo;s instructions and your unit&rsquo;s protocol for ending the session.}}
{{key:Readiness is lost one unreported event at a time. Report every transfusion, infection, and new result in a waitlisted patient.}}
"""),
        ("pd", "Peritoneal dialysis", "Peritoneal dialysis: the body&rsquo;s own filter at home", """
<p>Think of the lining of the abdomen as a very large tea bag. Fluid runs in through a soft catheter, sits for hours (the dwell) while waste and water move into it, and is drained and replaced. Each cycle is an exchange.</p>
{{fig:pd_exchange|One exchange: fill, dwell, drain.}}
<p>The picture has a limit. A tea bag is passive. The peritoneum, the lining of the abdomen, is living tissue full of capillaries, and it changes with time and infection.</p>
<h3>How it works</h3>
<p>Two forces do the work.[[daugirdas2015]] In diffusion, urea, creatinine, and potassium move from capillary blood into the fluid, down their concentration gradients. In ultrafiltration, water is drawn into the abdomen by the osmotic pull of glucose, which PD fluid contains at a concentration far above that of blood.</p>
<p>The glucose gradient fades during a long dwell, because the peritoneum absorbs glucose. Fluid can then flow back into the body. Icodextrin, a large sugar molecule absorbed slowly, keeps drawing water during long dwells. The absorbed glucose also adds calories and raises blood sugar, which matters in diabetes (Module 22).</p>
<p>Residual kidney function remains valuable on any form of dialysis. In incident hemodialysis patients, a faster loss of residual function was associated with higher mortality in a graded way. That study was observational and did not show that preserving residual function prolongs life.[[obi2016]]</p>
<h3>Prescribing and measuring PD</h3>
<p>The International Society for Peritoneal Dialysis (ISPD) recommends a PD prescription that is person-centered and goal-directed, built through shared decision-making, rather than one driven only by numbers for small-solute clearance.[[ispd_prescribing2020]] Weekly urea clearance, written as Kt/V, is a surrogate: a lab-based measure of dialysis dose, not an outcome the patient feels. The PD adequacy calculator on this site shows the arithmetic, for orientation only. The prescription belongs to the nephrologist.</p>
<p>PD suits a motivated patient with a clean space at home, clean water, and the dexterity to do exchanges, or a helper who can. Past abdominal surgery or hernias may make it harder. The decision is made with the nephrologist and the PD team.</p>
<h3>The complications you may meet</h3>
<p>Peritonitis is infection of the peritoneum. Bacteria enter by touch contamination, along the catheter tunnel, or from the bowel. The inflamed peritoneum pours white cells into the drained fluid, the effluent, which turns cloudy. The patient feels abdominal pain and may have fever. Repeated or severe episodes can scar the membrane and end PD.</p>
{{fig:pod27_effluent}}
<p>The ISPD 2022 peritonitis update sets targets for a PD program: an overall peritonitis rate of no more than 0.40 episodes per patient-year at risk, and more than 80% of patients free of peritonitis each year.[[ispd_peritonitis2022]] The ISPD 2023 update on catheter infections sets a target exit-site infection rate of no more than 0.40 episodes per patient-year. It also downgraded its recommendation for topical antibiotic at the exit site.[[ispd_catheter2023]] These are program targets for the PD team, not bedside thresholds.</p>
{{formula:<strong>Worked example: a peritonitis rate (illustrative program data, not a Philippine benchmark).</strong><br>Formula (ISPD 2022): peritonitis rate = number of episodes &divide; patient-years at risk.[[ispd_peritonitis2022]]<br>A home PD program follows 20 patients for a total of 180 patient-months. There were 5 episodes.<br>Patient-years at risk = 180 &divide; 12 = 15.<br>Rate = 5 &divide; 15 = 0.33 episodes per patient-year. This meets the target of 0.40 or fewer.<br>Patients free of peritonitis: 16 of 20 = 80%. This sits at the edge of the &ldquo;more than 80%&rdquo; target, and does not exceed it.<br><em>What it does not tell you:</em> with so few patients, one more episode changes the rate a great deal. Report the count and the time at risk with the rate, and follow ISPD definitions of an episode.}}
<div class="table-wrap"><table>
<thead><tr><th>What breaks</th><th>What you see when a PD patient comes to your unit</th><th>What you do, while you call</th></tr></thead>
<tbody>
<tr><td>Infection of the peritoneum</td><td>Cloudy effluent. Abdominal pain or tenderness. Fever, nausea, or diarrhea</td><td>Keep the drained bag. Check vital signs. Follow your unit&rsquo;s protocol for samples. Call the attending nephrologist and the PD team</td></tr>
<tr><td>Infection at the catheter exit site or along the tunnel</td><td>Redness, crusting, or pus where the catheter leaves the skin. A red, tender line over the tunnel</td><td>Look, do not squeeze. Cover the site as your protocol directs. Call</td></tr>
<tr><td>Fluid overload</td><td>Weight up, swelling, breathlessness, high blood pressure. Drained volumes smaller than filled</td><td>Assess breathing and oxygen saturation. Call. Module 14 covers the breathless patient</td></tr>
<tr><td>Catheter problem</td><td>Fluid will not drain, or drains slowly. Constipation often contributes</td><td>Do not flush or manipulate the catheter. Call the PD team</td></tr>
</tbody></table></div>
{{call:Stop and call the attending nephrologist when a PD patient has cloudy effluent, abdominal pain, or fever, or when the catheter exit site has pus or the tunnel is red and tender. Follow your unit&rsquo;s protocol and keep the bag. Do not start antibiotics or flush the catheter on your own.}}
{{key:In a PD patient, look at the drained fluid. If you cannot read print through the bag, think of peritonitis and call.}}
"""),
        ("ckm", "Conservative care", "Conservative kidney management: a plan, not an absence of care", """
<p>The third road has its own map, with stops for symptoms, food, anemia, fluid, advance care planning, and family support. Module 26 introduced it as a choice. Here you see it as a plan.</p>
{{fig:pod27_ckm}}
<p>The picture has a limit. A map suggests a fixed route. In practice the plan changes as kidney function falls and symptoms appear, and a patient can revisit the choice.</p>
<h3>What the plan does</h3>
<p>Without dialysis, waste, acid, potassium, and fluid build slowly as the remaining kidney function declines. The plan slows the build-up through diet, medicines, and diuretics, treats the symptoms that follow (Module 24), and prepares the patient and family through advance care planning.</p>
<p>A KDIGO conference on supportive care framed conservative care as part of core kidney care. That is a conference statement, not a graded recommendation.[[davison2015]]</p>
<h3>What the evidence shows, and how weak it is</h3>
<p>No randomized trial has compared conservative kidney management (CKM) with dialysis in older people. In the cohorts, patients chose their path, and those who chose CKM differed from those who chose dialysis, often by age. Survival comparisons are confounded from the start.</p>
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>Design and size</th><th>Finding</th><th>Main limitation</th></tr></thead>
<tbody>
<tr><td>Cochrane review, 2025[[yang_cochrane2025]]</td><td>24 non-randomized studies, 26,127 people aged 65 or older. No randomized trials found</td><td>Death: 813 per 1,000 with CKM and 630 per 1,000 with dialysis (relative risk 1.28). Effects on quality of life uncertain</td><td>Very low certainty. Large imbalances in prognostic factors between groups</td></tr>
<tr><td>Dutch single-center cohort, 2016[[verberne2016]]</td><td>107 patients chose conservative care, 204 chose dialysis, all aged 70 or older</td><td>Median survival 1.5 years with conservative care and 3.1 years with dialysis. In those aged 80 or older, 1.4 and 2.1 years, a difference that was not statistically significant (P=0.08)</td><td>Retrospective, one center. The conservative group was older (mean 83 versus 76 years), although comorbidity scores did not differ</td></tr>
<tr><td>Systematic review of caregivers, 2022[[walavalkar2022]]</td><td>Mixed-methods review of six studies</td><td>Caregiver burden and quality of life similar to those of caregivers of dialysis patients</td><td>Few, small studies</td></tr>
</tbody></table></div>
<p>The excess of 183 deaths per 1,000 is associated with CKM, but the Cochrane authors rated it very low certainty because of prognostic imbalances the analyses could not remove. They concluded that CKM had uncertain effects on death and quality of life.[[yang_cochrane2025]] The Dutch cohort suggests the survival gap narrows in the oldest patients and in those with heavy comorbidity.[[verberne2016]] Neither can predict what a given patient would gain from the other choice.</p>
<p>The frailty assessment calculator on this site gives context for this conversation, not a verdict. Module 25 covers frailty.</p>
{{formula:<strong>Worked example: conservative care or a missed referral? (decision walk-through, illustrative).</strong><br>Patient A: Mrs. Remedios Villanueva, 84. Estimated glomerular filtration rate (eGFR) 8 mL/min/1.73 m&sup2;. Her daughter asks you at the unit why her mother is not on dialysis.<br>Chart: documented conservative plan, advance care plan, and symptom review. <strong>Result: not a missed referral.</strong> Route the question to the attending nephrologist, and see Module 26 for the conversation.<br>Patient B: Mr. Arnel Cruz, 45, on hemodialysis for two years. Chart: no transplant discussion and no documented contraindication. <strong>Result: flag</strong> to the attending nephrologist under KDIGO 1.1 (1D).<br><em>What it does not tell you:</em> whether either choice is right for the person. It tells you only whether the conversation is documented.}}
{{key:Conservative kidney management is a planned path with its own goals. The evidence that compares it with dialysis is observational and of very low certainty.}}
"""),
        ("returning", "Coming back", "When a transplant or PD patient comes to the hemodialysis unit", """
<p>The roads cross. Three kinds of patient arrive from another road: one whose transplant has failed, one whose transplant needs dialysis support for a while, and one who has left PD after peritonitis, catheter failure, or loss of membrane function.</p>
{{fig:pod27_failedgraft}}
<h3>What changes for you</h3>
<p>Stopping immunosuppressive medicines can lead to rejection of a graft that still works. Continuing them raises the risk of infection. After a graft fails, the balance depends on remaining graft function, plans for another transplant, and infection risk. That decision belongs to the nephrologist and the transplant team. Never hold, start, or change these medicines yourself.</p>
<p>Immunosuppression also blunts fever and inflammation. A transplant recipient can have a serious infection with few signs. A failed graft can still inflame, with pain over the graft, fever, or blood in the urine. A graft that still makes urine is residual kidney function, and Module 3 explained why it is worth protecting.</p>
<p>The patient often arrives with a new catheter that needs a plan for a permanent access (Module 10), and needs current hepatitis B, hepatitis C, and HIV results before the first session (Modules 11 and 29).</p>
{{cards:First session for a returning transplant or PD patient|Serology::Latest hepatitis B, hepatitis C, and HIV results, with dates, before the session per your unit&rsquo;s protocol.|Medicines::A full list, with immunosuppressive medicines marked. No changes without the nephrologist and the transplant team.|Contacts::The transplant team&rsquo;s or PD team&rsquo;s name and number in the chart.|Access::The type of access, its date of insertion, and the plan for a permanent access.|Urine::Urine output now, so that a change can be noticed.|Recent events::Transfusions, infections, and hospital stays, with dates.}}
{{call:Stop and call the attending nephrologist when a transplant recipient has fever, pain or tenderness over the graft, or falling urine output, and whenever anyone asks about holding or changing immunosuppressive medicines. Ask that the transplant team be informed.}}
{{key:In a transplant recipient, the medicine list belongs to the transplant team. Your job is to notice and report, not to adjust.}}
"""),
        ("talk", "Talking at the chair", "Talking about the roads at the chair", """
<p>Patients ask the physician on duty what they did not ask in clinic: &ldquo;Can I have a transplant?&rdquo; &ldquo;Can I do dialysis at home?&rdquo; Each question is a chance to keep a road open. Answer honestly, do not promise, and pass it to the person who decides.</p>
<div class="table-wrap"><table>
<thead><tr><th>Words that help</th><th>Words that harm</th><th>Why</th></tr></thead>
<tbody>
<tr><td>&ldquo;That is a good question for Dr. Garcia. I will write it down and ask her today.&rdquo;</td><td>&ldquo;You are too old for that.&rdquo;</td><td>Age alone is not a reason to exclude a patient (KDIGO 2.1.1, 1A)[[kdigo_txcand2020]]</td></tr>
<tr><td>&ldquo;Many patients on dialysis can be considered for transplant. Your nephrologist can check whether you are one of them.&rdquo;</td><td>&ldquo;You will get a kidney soon.&rdquo;</td><td>A promise you cannot keep damages trust</td></tr>
<tr><td>&ldquo;Your mother and her doctor chose a plan without dialysis. I will ask the doctor to talk with you about it.&rdquo;</td><td>&ldquo;Someone should have started her on dialysis.&rdquo;</td><td>A documented conservative plan is a choice, not a mistake</td></tr>
</tbody></table></div>
<p>The written question becomes the referral flag. The module readings are patient guides you can share with families.</p>
{{cards:What to write after the conversation|The question::In the patient&rsquo;s words.|The finding::Whether the chart shows a transplant discussion, a referral, a conservative plan, or none of these.|The flag::To whom you reported, and when.|The owner::Who will speak with the patient next.}}
{{key:Answer the question honestly, promise nothing, and make sure the nephrologist hears it the same day.}}
"""),
    ],
    "debrief": ["""
<p><strong>What should happen to the transfusion plan?</strong> Ms. Bautista is stable, with no bleeding, breathlessness, or chest pain, so nothing requires the blood in the next few minutes. You ask Mr. Reyes to hold it, as your unit&rsquo;s protocol allows, and call the attending nephrologist before it starts. A transfusion could expose her to foreign human leukocyte antigens. Antibodies would shrink her pool of compatible donors, possibly including her brother. The nephrologist may still decide she needs blood, but now decides knowing a transplant is possible. If blood is given, it is recorded so the transplant team can be told (KDIGO 19.1, Not Graded).</p>
<p><strong>Is she a candidate to hear about transplant?</strong> Yes. KDIGO recommends that every patient expected to reach kidney failure be informed of, educated about, and considered for transplant (1.1, 1D). Patients already on dialysis should be referred when medically stable and kidney failure is irreversible (1.1.2, Not Graded). Three years on dialysis is not too late. She is young and has a willing living donor. KDIGO names pre-emptive living-donor transplant the preferred treatment for eligible patients (1.4, 1A); she is past the pre-emptive window, but her brother&rsquo;s offer is worth reporting today. Eligibility is for the nephrologist and the transplant center to judge, and her brother&rsquo;s offer would pass through the center&rsquo;s Hospital Transplant Ethics Committee.</p>
<p><strong>What do you tell her, whom do you call, and what do you write?</strong> You tell her the truth without promising: &ldquo;It is a very good question, and it is not too late to ask it. I will tell Dr. Garcia today so that she can talk with you about transplant and your brother&rsquo;s offer.&rdquo; You call the attending nephrologist about both the held transfusion and the absent transplant discussion. You write the time, her question in her own words, the transfusion decision, the flag, and who will follow up.</p>
"""],
    "skills": {"title": "Transplant-readiness review at the chair",
               "intro": "Perform this review with a patient, or a colleague playing a patient, while your preceptor observes. Use a real or mock chart.",
               "items": [
                   ("Confirms the patient&rsquo;s identity and explains the purpose of the review.", False),
                   ("Checks the chart for a documented transplant discussion, a referral, a waiting-list status, or a documented reason not to refer.", False),
                   ("Flags an absent transplant discussion to the attending nephrologist when the patient has no documented contraindication.", True),
                   ("Reviews hepatitis B, hepatitis C, and HIV results and their dates against the unit&rsquo;s schedule.", False),
                   ("Identifies any blood transfusion since the last report to the transplant team and makes sure it is reported per unit protocol.", True),
                   ("Checks the vaccine record, including hepatitis B, per unit protocol.", False),
                   ("Asks about infections, dental problems, and new medicines since the last review.", False),
                   ("Asks about missed or shortened sessions and their reasons without judgment.", False),
                   ("Confirms the transplant center&rsquo;s contact number and the patient&rsquo;s current phone number.", False),
                   ("Recognizes a documented conservative care plan and does not label it a missed referral.", True),
                   ("States that immunosuppressive medicines are never changed without the nephrologist and the transplant team.", True),
                   ("Documents each flag and its owner in the chart.", False),
               ],
               "placement": "Over two weeks, review the charts of every patient on your shifts for a documented transplant discussion. List the patients with no discussion and no documented reason, and review the list with your preceptor before passing it to the attending nephrologists."},
    "quiz": [
        ("Which function does a working kidney transplant provide that neither hemodialysis nor peritoneal dialysis provides?",
         ["Removal of urea",
          "Removal of water",
          "Production of erythropoietin and activation of vitamin D",
          "Removal of potassium"], 2,
         "Both forms of dialysis replace part of filtration only. A transplant also restores hormone production."),
        ("Why did Wolfe and colleagues compare transplant recipients with patients on the waiting list rather than with all dialysis patients?",
         ["Waitlisted patients were also judged fit, which reduces the effect of selecting healthier patients",
          "Waitlisted patients were randomized",
          "All dialysis patients had the same risk",
          "Waitlisted patients received more dialysis"], 0,
         "Comparing like with like reduces, but does not remove, selection bias."),
        ("In the waitlist comparison, how did the risk of death after transplant change over time?",
         ["It was lower from the first day",
          "It was higher in the first two weeks, then much lower by 18 months",
          "It was equal at all times",
          "It was higher at every time point"], 1,
         "Surgery carries early risk. The relative risk at 18 months was 0.32, and long-term mortality was 48% to 82% lower."),
        ("A 38-year-old man has been on hemodialysis for four years. His chart shows no transplant discussion and no documented contraindication. What should you do?",
         ["Nothing. After four years it is too late",
          "Refer him to a transplant center yourself",
          "Tell him he will be listed soon",
          "Flag the absent discussion to the attending nephrologist and document it"], 3,
         "KDIGO asks that patients be informed and considered (1D). The referral is the nephrologist&rsquo;s."),
        ("What is the grade of the KDIGO 2020 recommendation not to exclude patients from transplant because of age alone?",
         ["1A",
          "1D",
          "2C",
          "Not Graded"], 0,
         "Statement 2.1.1 is graded 1A."),
        ("A waitlisted woman is stable, with a hemoglobin lower than last month. A transfusion has been ordered for today&rsquo;s session. What is the best first step?",
         ["Give the transfusion, because the order is written",
          "Cancel the transfusion permanently",
          "Hold it as your unit&rsquo;s protocol allows and call the attending nephrologist, noting that she is waitlisted",
          "Give half of the blood and observe"], 2,
         "A transfusion may sensitize her. When she is stable, there is time to call."),
        ("How does a blood transfusion reduce a patient&rsquo;s chance of finding a compatible donor?",
         ["It suppresses erythropoietin production",
          "It exposes the immune system to foreign HLA, and the antibodies formed can rule out donors",
          "It raises the blood potassium",
          "It changes the patient&rsquo;s blood group"], 1,
         "Antibodies against HLA persist and can attack a donor kidney that carries the same antigens."),
        ("What drives water removal in peritoneal dialysis?",
         ["Pressure from a pump",
          "Diffusion of urea",
          "Gravity during the drain",
          "The osmotic gradient created by glucose or icodextrin in the fluid"], 3,
         "Glucose draws water osmotically. The gradient fades as glucose is absorbed."),
        ("A woman on peritoneal dialysis arrives for backup hemodialysis. She has abdominal pain and her drained bag is cloudy. What do you do?",
         ["Keep the bag, check vital signs, follow the unit protocol, and call the attending nephrologist",
          "Start an antibiotic you know works for peritonitis",
          "Flush the catheter to clear it",
          "Discard the bag and start hemodialysis"], 0,
         "Cloudy effluent with pain suggests peritonitis. Treatment is directed by the nephrologist and the PD team."),
        ("A PD program records 4 episodes of peritonitis over 120 patient-months. What is its peritonitis rate?",
         ["0.03 episodes per patient-year",
          "0.40 episodes per patient-year",
          "0.33 episodes per patient-year",
          "3.0 episodes per patient-year"], 1,
         "Patient-years at risk are 120 &divide; 12 = 10. The rate is 4 &divide; 10 = 0.40, at the ISPD target of no more than 0.40."),
        ("What did the 2025 Cochrane review conclude about conservative kidney management compared with dialysis in older people?",
         ["Conservative care was proven to shorten life",
          "Dialysis was proven to improve quality of life",
          "Effects on death and quality of life were uncertain, with very low certainty evidence from non-randomized studies",
          "The two were proven equal"], 2,
         "No randomized trials exist, and prognostic imbalances made the certainty very low."),
        ("In the Dutch cohort of patients aged 70 or older, what was found in those aged 80 or older?",
         ["Conservative care had longer survival",
          "Survival was identical to the day",
          "Dialysis tripled survival",
          "The survival difference was smaller and not statistically significant"], 3,
         "Median survival was 1.4 versus 2.1 years (P=0.08) in a retrospective single-center study."),
        ("An 85-year-old man in the unit for his wife&rsquo;s appointment has an eGFR of 7 mL/min/1.73 m&sup2;. His chart shows a documented conservative plan and an advance care plan. His son says nobody offered dialysis. What is the best response?",
         ["Recognize a planned path, avoid suggesting an error, and ask the attending nephrologist to speak with the family",
          "Arrange urgent dialysis",
          "Flag a missed referral",
          "Tell the son the plan was a mistake"], 0,
         "A documented conservative plan is a choice. The family&rsquo;s question goes to the nephrologist."),
        ("A man with a failed transplant is now on hemodialysis. A nurse asks whether to stop his tacrolimus because the graft no longer works. What do you say?",
         ["Stop it, since the graft has failed",
          "Do not change it. Ask the attending nephrologist and the transplant team",
          "Halve the dose",
          "Switch to another immunosuppressant"], 1,
         "Stopping risks rejection of the old graft, and continuing raises infection risk. The transplant team decides."),
        ("A transplant recipient dialyzing temporarily has a temperature of 38.2 &deg;C, tenderness over the graft, and less urine than yesterday. Which statement is correct?",
         ["Fever in a transplant recipient is usually minor",
          "Give paracetamol and continue the session without calling",
          "Call the attending nephrologist at once and ask that the transplant team be informed",
          "Increase his immunosuppressive medicines"], 2,
         "Graft tenderness and falling urine raise concern for infection or rejection."),
    ],
    "terms": [("Kidney transplant", "Surgery that places a donor kidney in the lower abdomen, restoring filtration and hormone production."),
              ("Waiting list", "The list of evaluated and accepted patients waiting for a kidney from a deceased donor."),
              ("Pre-emptive transplant", "A transplant performed before dialysis starts."),
              ("Human leukocyte antigens (HLA)", "Proteins on cell surfaces that the immune system uses to tell self from non-self."),
              ("Sensitization", "Formation of antibodies against HLA after a transfusion, pregnancy, or earlier transplant."),
              ("Peritoneal dialysis (PD)", "Dialysis that uses the lining of the abdomen as the filter, with fluid placed through a catheter."),
              ("Effluent", "The fluid drained from the abdomen after a PD dwell."),
              ("Peritonitis", "Infection and inflammation of the peritoneum. In PD it usually shows as cloudy effluent and abdominal pain."),
              ("Conservative kidney management (CKM)", "Planned, active kidney care without dialysis, focused on symptoms, quality of life, and the person&rsquo;s goals."),
              ("Immunosuppressive medicines", "Medicines that prevent rejection of a transplanted kidney. They raise the risk of infection.")],
    "readings": [("kidney-transplant.html", "What a transplant involves, from evaluation to life afterward, for patients and families."),
                 ("peritoneal-dialysis-ckd.html", "How peritoneal dialysis works at home and who it suits."),
                 ("transplant-allograft-failure.html", "What happens when a transplanted kidney fails, and the return to dialysis.")],
    "calcs": ["calc-kfre.html", "calc-pd-adequacy.html", "calc-frailty-assessment.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pod_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
