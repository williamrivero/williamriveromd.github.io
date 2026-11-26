# -*- coding: utf-8 -*-
MODULE = {
    "sub": "What the evaluation is looking for and why, how blood groups, HLA antibodies and crossmatches decide which kidney a body will accept, why a single transfusion can change a candidate's chances, and how to run a readiness tracker that keeps a candidate truly ready.",
    "desc": "Transplant Nurse Module 2: recipient evaluation domains (cardiac, cancer, infection, frailty, psychosocial), ABO and HLA compatibility, cPRA, donor-specific antibodies and crossmatch, sensitizing events, vaccines before transplant, and readiness tracking for Philippine registered nurses.",
    "keywords": "kidney transplant evaluation nursing, HLA antibodies cPRA explained, crossmatch nurse, sensitization transfusion transplant, frailty transplant candidate, waiting list readiness",
    "image_alt": "A transplant coordinator nurse reviewing a color-coded readiness checklist on a tablet with an older Filipino candidate and his daughter.",
    "objectives": [
        "Explain the purpose of each evaluation domain in terms of what could make surgery or immunosuppression unsafe.",
        "Explain ABO compatibility, HLA typing, cPRA, donor-specific antibodies and the crossmatch in plain language.",
        "Recognize sensitizing events and report them so that antibody testing stays current.",
        "Maintain a readiness tracker with dated results, dispositions and named owners.",
        "Respond to missed tests and loss of contact as barriers to solve rather than as nonadherence to punish.",
    ],
    "sections": [
        {"id": "model", "nav": "Mental model", "tag": "Intuition", "h2": "Two questions every evaluation asks",
         "html": """
<p>Every test in a transplant evaluation answers one of two questions. <em>Will this person survive the operation and the first year of immunosuppression?</em> And <em>will this person's immune system accept this particular kidney?</em> The first question is answered by the medical work-up: heart, cancer, infection, frailty, mind and means. The second is answered by the immunology laboratory: blood group, tissue type and antibodies.</p>
<p>Think of the immune system as a security guard holding a list of faces it has been taught to attack. Most people's list is short. Every pregnancy, every blood transfusion and every previous transplant shows the guard new faces, and the list grows. A candidate whose list matches most of the population is "highly sensitized" and will wait far longer for a kidney that matches none of the faces. The picture has a limit. A guard forgets faces; the immune system mostly does not. The list is written in antibodies made by plasma cells and kept by memory B cells, so it can be read with a blood test, it can grow silently after a single transfusion, and an antibody that has fallen below the test's detection level can return within days when the same tissue type is met again. That memory is why every sensitizing event must be reported, even an old one.</p>
"""},
        {"id": "workup", "nav": "Evaluation", "tag": "Physiology", "h2": "What the medical evaluation is looking for",
         "html": """
<p>The KDIGO candidate guideline organizes evaluation around risks that surgery or lifelong immunosuppression would make dangerous.[[txcand2020]] Learn the reason behind each item. It lets you explain the test to the patient, and it lets you spot what is overdue.</p>
<p>The guideline grades its statements, and the grade tells you how firm each one is. Screening every candidate for HIV, hepatitis C and hepatitis B is a strong recommendation on high-certainty evidence (1A). Routine cancer screening as for the general population is strong but rests on very low-certainty evidence (1D). Cardiac evaluation by history, examination and electrocardiogram is ungraded, while noninvasive coronary testing for asymptomatic high-risk candidates is a weak suggestion (2C). A psychosocial assessment for every candidate is also a weak suggestion (2D). Age alone should not exclude anyone (1A).[[txcand2020]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Domain</th><th>The physiologic worry</th><th>Nursing focus</th></tr></thead>
<tbody>
<tr><td>Cardiovascular</td><td>Coronary disease is common and often silent in kidney failure; surgery and fluid shifts unmask it.</td><td>Track stress test or echocardiogram dates; report new chest pain or dyspnea.</td></tr>
<tr><td>Cancer</td><td>Immunosuppression weakens immune surveillance, so an untreated cancer can grow faster.</td><td>Age- and sex-appropriate screening dates; report new weight loss or bleeding.</td></tr>
<tr><td>Infection</td><td>Latent infections (hepatitis B and C, HIV, tuberculosis, Strongyloides in endemic areas) can reactivate under immunosuppression.</td><td>Serology dates; latent tuberculosis results and treatment start; dental clearance.</td></tr>
<tr><td>Vascular and surgical</td><td>The kidney is joined to the iliac vessels and bladder; heavy calcification or bladder problems complicate surgery.</td><td>Imaging dates; prior abdominal surgery; urologic history.</td></tr>
<tr><td>Frailty and function</td><td>Low physiologic reserve predicts complications and death.</td><td>Mobility, falls, weight; refer for prehabilitation.</td></tr>
<tr><td>Psychosocial and means</td><td>Lifelong medicines, labs and visits require support, understanding and money.</td><td>Social work review; coverage; who will help after discharge.</td></tr>
</tbody></table></div>
<p><strong>Tuberculosis deserves particular attention in the Philippines.</strong> The burden of latent infection is high, and reactivation under immunosuppression can be severe and atypical. Guidance from the American Society of Transplantation recommends screening every candidate for latent tuberculosis and treating latent infection, ideally starting before transplant.[[subramanian2019]] KDIGO recommends latent tuberculosis screening at evaluation (1C), but it wrote that recommendation for low-prevalence areas; in a high-burden country, your program's own tuberculosis policy governs.[[txcand2020]] Track the result, the decision and the start date.</p>
<div class="tc-scene"><span class="tc-lab">In the transplant clinic &middot; fictional</span><p>Mr. Garcia, 49, is almost through his evaluation. His interferon-gamma release assay came back positive two months ago. The tracker says "for ID referral." Nobody has booked it.</p><p>You call infectious disease, book the visit, and write the owner and date into the tracker. Six weeks later he starts treatment for latent tuberculosis. The committee lists him the following month instead of deferring him.</p><p class="tc-scene-take"><b>What this shows.</b> A positive screen is not the end of the task. The result needs a decision, a start date and an owner.</p></div>

<p><strong>Frailty predicts outcomes independently of age.</strong> In a prospective cohort of 537 recipients, five-year survival was 91.5 percent in nonfrail, 86.0 percent in intermediately frail and 77.5 percent in frail recipients, and frailty was independently associated with about twice the risk of death (hazard ratio 2.17, with a wide confidence interval from 1.01 to 4.65, from a single center).[[mcadams2015]] This is observational evidence, so it identifies risk rather than proving that improving frailty improves survival. It is still a reason to measure frailty and to refer for prehabilitation while the candidate waits.</p>
<div class="tc-scene"><span class="tc-lab">In the transplant clinic &middot; fictional</span><p>Lola Pacing, 68, needs a hand to rise from the chair and walks slowly to the scale. Her daughter says, "She just needs the kidney, then she'll be strong again."</p><p>You record her chair-rise and walking speed, tell the nephrologist, and send a prehabilitation referral while she waits. You explain to the daughter that getting stronger now is part of getting ready, not a reason for delay.</p><p class="tc-scene-take"><b>What this shows.</b> Frailty is measured, reported and worked on during the wait. It is not a judgment made at the bedside.</p></div>

<p><strong>Vaccinate before, not after.</strong> Vaccines work better before immunosuppression, and live vaccines are generally avoided after transplant. KDIGO recommends starting inactivated vaccine series before transplant, on an accelerated schedule if needed, and completing any live attenuated vaccine series before transplant (both 1B); if a live vaccine is given, transplant should wait 4 weeks (1B).[[txcand2020]] Transplant infectious-disease guidance agrees that both kinds can be given before transplant.[[danziger2019]] A candidate on the active list should have an up-to-date vaccine record.</p>
"""},
        {"id": "contra", "nav": "Not now or not ever", "tag": "Decision points", "h2": "Not now, or not ever: what stops or delays a transplant",
         "html": """
<p>Patients and families hear evaluation results as a verdict: accepted or rejected. The reality has more shades. Most problems found during evaluation lead to a <em>deferral</em> (fix this, then we will look again), not a final decline. Knowing the difference lets you explain the result honestly and help the patient work on what can change.</p>
<p>The logic is the same as in the evaluation table above. A finding stops or delays transplant when surgery or immunosuppression would make it dangerous, or when the transplant would probably not help the person live longer or better.[[txcand2020]] The program decides. You help the patient understand which kind of finding he has.</p>
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>Why it matters physiologically</th><th>Usual direction</th><th>What the nurse can help with</th></tr></thead>
<tbody>
<tr><td>Active infection</td><td>Immunosuppression would let it spread</td><td>Defer until treated</td><td>Track treatment start and end; report fevers</td></tr>
<tr><td>Cancer, recent or active</td><td>Immune surveillance is weakened after transplant</td><td>Defer for a waiting period set by cancer type, or decline if active</td><td>Keep oncology records and dates in the file</td></tr>
<tr><td>Severe heart disease</td><td>Surgery and fluid shifts may cause infarction or heart failure</td><td>Defer for treatment, or decline if uncorrectable</td><td>Track cardiology referrals and procedures</td></tr>
<tr><td>Smoking</td><td>Damages vessels and wound healing; raises cancer and heart risk</td><td>Programs ask for cessation</td><td>Offer support; record a quit date</td></tr>
<tr><td>Excess weight</td><td>Wound complications, technical difficulty, metabolic risk</td><td>Program policy varies; often a weight goal</td><td>Refer to the dietitian and prehabilitation; record weights</td></tr>
<tr><td>Poor dental health</td><td>Mouth infections can seed the blood under immunosuppression</td><td>Defer until cleared</td><td>Book dental review early; it is often the last item done</td></tr>
<tr><td>Ongoing substance use, or repeated nonadherence</td><td>Lifelong medicines and follow-up are not yet safe</td><td>Defer with a plan and support</td><td>Explore barriers; connect to support; document progress</td></tr>
<tr><td>Very limited life expectancy from another illness</td><td>Risks of surgery may outweigh years gained</td><td>Decline, with a plan for other kidney failure care</td><td>Make sure dialysis or conservative care planning continues</td></tr>
</tbody></table></div>
<p>Several of these findings carry KDIGO grades. Active cancer excludes a candidate (1B), but a history of cancer, even metastatic, does not exclude one automatically (1D). Obesity alone should not exclude a candidate (2B), and weight-loss support should be offered (2D). Candidates should stop tobacco at least 1 month before listing (1B). An unstable psychiatric disorder or ongoing substance use disorder is a reason not to transplant now (1C), while a past history of nonadherence is not a permanent bar (1D).[[txcand2020]]</p>
<p><strong>Say "not yet" when it is not yet.</strong> A patient told he has been "rejected" for transplant may stop trying. A patient told "the team wants your dental treatment done and your weight down by eight kilos, then they will review you again" has a task and a reason to do it. Use the program's exact wording, and ask the coordinator if you are unsure which it is.</p>
<div class="tc-scene"><span class="tc-lab">In the transplant clinic &middot; fictional</span><p>Mr. Esguerra, 55, leaves the committee feedback visit and tells you in the corridor, "They rejected me. It's my weight." He is angry and close to tears.</p><p>You check the letter with him. It says "deferred," with a weight goal and a review in six months. You read it aloud slowly, show him the words "review in six months," and book him with the dietitian and the prehabilitation program before he leaves.</p><p class="tc-scene-take"><b>What this shows.</b> "Deferred" and "declined" are different futures. Make sure the patient knows which one he has.</p></div>
"""},
        {"id": "immunology", "nav": "Compatibility", "tag": "Physiology", "h2": "Blood groups, HLA, antibodies and the crossmatch",
         "html": """
<p><strong>ABO blood group.</strong> The same A and B sugar antigens that decide transfusion compatibility also coat the inner lining of the kidney's blood vessels. A recipient's natural anti-A or anti-B antibodies would attack an incompatible kidney within minutes, so ABO compatibility follows transfusion rules. Some centers perform ABO-incompatible transplants after removing antibodies, a specialized protocol.</p>
<p><strong>HLA typing.</strong> Human leukocyte antigens (HLA) are the proteins every cell uses to display fragments of itself to T lymphocytes. They are inherited, highly variable, and are the main targets of rejection. Typing tells the laboratory which HLA a candidate and a donor carry.</p>
<p><strong>Antibodies and cPRA.</strong> Sensitizing events (pregnancy, transfusion, a prior transplant) can create antibodies against HLA the candidate does not have. The laboratory lists antigens against which the candidate has clinically significant antibodies. The calculated panel-reactive antibody (cPRA) translates that list into a percentage: the share of donors in a reference population who carry at least one of those antigens. A cPRA of 95 percent means roughly 95 of every 100 donors would be unsuitable on antibody grounds.</p>
<p>KDIGO recommends that antibody testing use solid-phase assays (1B). It asks, as ungraded statements, that testing be done at evaluation, at regular intervals while waiting and after every sensitizing event, and that every sensitizing event be communicated to the laboratory.[[txcand2020]] cPRA is a measure of access, not an outcome. It predicts how long a candidate may wait and how hard a match will be; it does not by itself tell you how the kidney will do after transplant.</p>
<p><strong>Donor-specific antibody (DSA).</strong> cPRA describes breadth of sensitization against a population. A DSA is an antibody directed against an HLA carried by <em>a particular donor</em>. A candidate with a cPRA of 20 percent can still have a strong DSA against her husband's kidney; a candidate with 90 percent may have none against a specific offer.</p>
<p><strong>Crossmatch.</strong> The crossmatch tests the recipient's serum against the donor's cells (or, virtually, the antibody list against the donor's typing). A strongly positive crossmatch from preformed DSA can cause hyperacute or early antibody-mediated rejection, which is why the test must use the candidate's <em>current</em> serum.</p>
<div class="tc-keyp"><span class="tc-lab">Remember</span>cPRA tells you how hard it will be to find a kidney. DSA and crossmatch tell you whether <em>this</em> kidney is safe. The laboratory and transplant team interpret both; the nurse makes sure the sample is the right patient, the right date, and that new sensitizing events are reported.</div>
<div class="tc-scene"><span class="tc-lab">By phone &middot; fictional</span><p>Joy hangs up and turns to you. "Mrs. Cruz's cPRA is 98 percent. She asked if that means she'll never get a kidney."</p><p>Carla answers for both of you: "It means very few donors are safe for her, so her wait is longer. It does not mean none are. The lab checks every offer against her antibody list. What she can do is keep her samples current and tell us right away about any transfusion."</p><p class="tc-scene-take"><b>What this shows.</b> Patients hear numbers as verdicts. Translate them into what they mean for the wait, and what the patient can do.</p></div>
"""},
        {"id": "sensitizing", "nav": "Sensitizing events", "tag": "Practice", "h2": "One transfusion can change everything",
         "html": """
<p>A wait-listed candidate who receives a blood transfusion during an unrelated admission may develop new HLA antibodies within weeks. If the laboratory's stored serum predates the transfusion, a future crossmatch could miss a dangerous antibody. Programs therefore ask to be notified of transfusions, pregnancies, miscarriages and infections, and they keep serum samples current on a regular schedule. KDIGO asks that all sensitizing events, including platelet transfusions and pregnancies, be communicated to the laboratory (an ungraded statement). It has no separate graded recommendation to avoid transfusion; that part is clinical judgment by the treating team.[[txcand2020]]</p>
<ul>
<li>Ask every listed candidate at every contact: any admission, transfusion, pregnancy or surgery since we last spoke?</li>
<li>Record the date, the facility and the number of units if known, and request the records.</li>
<li>Notify the coordinator and, per local procedure, the histocompatibility laboratory, and document who will arrange the repeat sample.</li>
<li>Avoid unnecessary transfusion in candidates where you have influence: flag the patient's status to the treating team, who weigh anemia treatment options.</li>
</ul>
<div class="tc-stop"><span class="tc-lab">Stop and report</span>Any discrepancy in a sample label, a result that seems to belong to another patient, or a crossmatch request with a mismatched identifier must stop the workflow until it is verified through the laboratory's procedure.</div>
<div class="tc-scene"><span class="tc-lab">On the ward &middot; fictional</span><p>A listed candidate is admitted to the medical ward with a hemoglobin of 7.2 g/dL after a gastrointestinal bleed. The resident writes an order for two units of packed red cells.</p><p>You notice the "transplant candidate" flag and tell the resident before the blood is hung. The resident still transfuses, because the patient is dizzy and bleeding. You record the date and number of units, and you email the coordinator and the laboratory that evening so a fresh serum sample is drawn.</p><p class="tc-scene-take"><b>What this shows.</b> Sometimes a transfusion is necessary. What makes it safe for the future is that the program knows about it.</p></div>
"""},
        {"id": "tracker", "nav": "Readiness tracker", "tag": "Workflow", "h2": "Keeping a candidate truly ready",
         "html": """
<p>A candidate is "ready" only if every required item is current on the day a kidney becomes available. Results expire: a cardiac test from three years ago, an outdated serum sample, a lapsed cancer screen. A good tracker lists, for each item, the date done, the result disposition (reviewed and acceptable, needs action, pending), the expiry or repeat date, and the owner of the next step.</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Date</th><th>Disposition</th><th>Repeat due</th><th>Owner</th></tr></thead>
<tbody>
<tr><td>Serum sample for antibody screening</td><td>12 Jan</td><td>Reviewed</td><td>Per laboratory schedule, or after any sensitizing event</td><td>Coordinator</td></tr>
<tr><td>Cardiac assessment</td><td>3 Feb</td><td>Cardiology cleared</td><td>Per program policy</td><td>Nephrologist</td></tr>
<tr><td>Latent tuberculosis test</td><td>20 Feb</td><td>Positive, treatment started 1 Mar</td><td>Completion date</td><td>Infectious disease</td></tr>
<tr><td>Cervical cancer screen</td><td>pending</td><td>Overdue</td><td>Book this month</td><td>Clinic RN</td></tr>
</tbody></table></div>
<p><strong>Missed tests are a signal.</strong> A candidate who misses two appointments may have run out of money for transport, lost a job, become ill, or misunderstood. Contact them through the approved route, ask what happened, document the barrier, and offer a path back: bundled visits, local testing, social work, or a benefits review. Labeling a candidate "nonadherent" without exploring the reason closes the door on people who most need help.</p>
<div class="tc-scene"><span class="tc-lab">By phone &middot; fictional</span><p>Mang Berto has missed two cardiology appointments. The tracker shows him in red. On the phone, he admits he lost his job as a security guard and cannot pay the tricycle and bus fare to the center.</p><p>You document the barrier and refer him to the social worker, who finds a hospital charity fund to help with his fares. You also ask the coordinator whether his echocardiogram can be done at the provincial hospital and sent. He is back on track within a month.</p><p class="tc-scene-take"><b>What this shows.</b> "Missed appointment" is a finding to investigate, not a verdict on the patient.</p></div>

<p><strong>Report changes that affect safety.</strong> New infection, hospitalization, a new cancer concern, major weight change, or loss of contact for weeks may require the team to place a candidate on hold. You report; the program decides the status and communicates it.</p>
"""},
        {"id": "waiting", "nav": "Staying ready", "tag": "Practice", "h2": "While the candidate waits: staying well and staying ready",
         "html": """
<p>A candidate may wait months for a living-donor work-up to finish, or years for a deceased-donor kidney. The waiting time is not empty. What happens during it decides whether the candidate is still fit, still sensitized at the same level, and still reachable when the call comes.</p>
<p><strong>Why some candidates wait longer.</strong> Two things lengthen the wait, and both come from the immunology above. First, blood group. A group O candidate can receive only a group O kidney, while group O kidneys can be given to recipients of other groups. Group O candidates therefore compete for a narrower supply. Second, sensitization. A candidate with a high cPRA is compatible with only a small share of donors, so suitable offers are rare. Neither is the patient's fault, and both are worth explaining so that a long wait is not taken as neglect. KDIGO suggests telling candidates plainly how their blood group and sensitization affect their access to a kidney (2C), and recommends that highly sensitized candidates be offered access to a larger donor pool where one exists (1C).[[txcand2020]]</p>
<p><strong>When the willing donor is incompatible.</strong> A relative may volunteer and then turn out to be ABO-incompatible, or to have a positive crossmatch. Some programs offer desensitization or ABO-incompatible protocols. Others use paired exchange, in which two incompatible pairs swap donors so that each recipient gets a compatible kidney. Availability depends entirely on the program. Your part is to make sure the patient hears the options from the team, not to promise any of them.</p>
<h3>Keeping the candidate well</h3>
<div class="tc-cards">
<div class="tc-card"><b>Anemia without transfusion</b>Anemia is treated, where possible, with iron and erythropoiesis-stimulating agents rather than blood, because every transfusion can raise antibodies. Flag listed status on every admission.</div>
<div class="tc-card"><b>Dialysis and nutrition</b>Missed sessions, fluid overload and falling albumin all erode fitness. Report a candidate whose dialysis attendance or weight is slipping.</div>
<div class="tc-card"><b>Strength</b>Frailty can worsen while waiting. Walking programs and prehabilitation keep muscle and confidence up.</div>
<div class="tc-card"><b>Mood</b>Long waits wear people down. Ask how the patient is coping, and refer to social work or mental health support when hope is fading.</div>
<div class="tc-card"><b>Screening dates</b>Cancer screens, cardiac tests and serology expire. The tracker shows what is due next.</div>
<div class="tc-card"><b>Contact details</b>A new phone number, a move to another province or a long trip abroad must reach the program the same week.</div>
</div>
<p><strong>The readiness call.</strong> Many programs contact listed candidates on a schedule to update their status. Use the same short script every time, so nothing is skipped: any admission, transfusion, pregnancy, surgery or infection; any new diagnosis or medicine; any change in phone, address or companion; any planned travel; how dialysis is going; how the patient is feeling about the wait. Record the answers with the date, and act on any yes.</p>
<div class="tc-scene"><span class="tc-lab">By phone &middot; fictional</span><p>On his quarterly call, Mr. Ramos, listed for 18 months, says everything is fine. When you reach the question about travel, he mentions that he is leaving next week to work on a construction site in Saudi Arabia for a year, "to save for the transplant."</p><p>You do not tell him what to decide. You explain that if a kidney is offered while he is abroad, he will not be able to come in time, and that the program needs to know so it can discuss his listing status with him. You notify Joy that afternoon, and she arranges a call with Dr. Santos before he leaves.</p><p class="tc-scene-take"><b>What this shows.</b> A candidate's plans are part of his readiness. The scripted question about travel caught a change that would have made him unreachable.</p></div>
"""},
        {"id": "evidence", "nav": "Evidence", "tag": "Certainty", "h2": "What is established, and what is not",
         "html": """
<ul>
<li><strong>Established physiology:</strong> preformed antibodies against ABO or donor HLA can cause immediate or early antibody-mediated graft injury; this is why compatibility testing exists.</li>
<li><strong>Guideline-based:</strong> structured evaluation across cardiac, cancer, infection, frailty and psychosocial domains follows the KDIGO candidate guideline, whose grades range from 1A (viral screening, no exclusion for age alone) to ungraded (basic cardiac evaluation, antibody testing schedule).[[txcand2020]] Pre-transplant latent tuberculosis screening and vaccination are recommended by transplant infectious-disease guidance.[[subramanian2019]][[danziger2019]]</li>
<li><strong>Association, not proven causation:</strong> frailty predicts mortality after transplant.[[mcadams2015]] Whether prehabilitation reverses that risk is still being studied.</li>
</ul>
"""},
    ],
    "case": {
        "title": "The transfusion nobody mentioned",
        "html": """
<p><strong>Thursday, 2:15 p.m., quarterly readiness call.</strong> Aling Merly, 58, has been on the deceased-donor waiting list for two years. Her cPRA was 35 percent at listing. You go down the call script with her: any admission, transfusion, pregnancy or surgery since we last spoke?</p>
<p>"Nothing much," she says. Then, almost in passing: "Ah, last month I was confined in the provincial hospital for heavy bleeding, the monthly kind. They gave me two bags of blood. I'm fine now."</p>
<p>You check her file. The program's last serum sample is from four months ago. Her tracker also shows the mammogram she was due for in March is still open. She laughs that she missed it because her son's motorcycle broke down.</p>
""",
        "acte": {
            "Assess": "Date and place of admission, number of units, current symptoms, ongoing bleeding, hemoglobin if known, and whether the bleeding cause has been evaluated (also a cancer-screening issue).",
            "Communicate": "Notify the coordinator and, per procedure, the histocompatibility laboratory that a sensitizing event occurred after the last stored sample. Request the provincial records. Document who will arrange the repeat sample and by when.",
            "Teach": "Explain why a transfusion can create new antibodies and why the laboratory needs a fresh sample to keep her safe when a kidney is offered. Ask her to report any future admission or transfusion promptly.",
            "Escalate": "The new uterine bleeding and the missed mammogram are both cancer-screening concerns; route them to the nephrologist for work-up and possible temporary hold. Offer social work help with transport.",
        },
        "task": "Write the contact note: event, dates, notifications made, owner of the repeat sample, owner of the gynecologic and breast follow-up, and who will tell her about any change in list status.",
        "outcome": """
<p>The nurse in the story asked three follow-up questions before ending the call: the date, the hospital and the number of units. Then she emailed the coordinator and the histocompatibility laboratory that afternoon, flagged that the stored serum predated the transfusion, and requested the provincial records. The coordinator took ownership of the repeat sample and booked it for the following week.</p>
<p>She also recognized that new heavy uterine bleeding in a 58-year-old is not "just bleeding". She routed it, with the overdue mammogram, to the nephrologist, who arranged a gynecologic evaluation and placed Aling Merly on temporary hold while it was done. Social work arranged a ride for the visit.</p>
<p>Six weeks later the evaluation was reassuring, the new sample showed one new antibody, and she was reactivated with an updated antibody list. If an offer had come in the meantime, the laboratory would have been working from the old list.</p>
""",
    },
    "second_round": ("One laboratory result in her file has a different middle name, and her cervical screening is also overdue.", "A tracker with the suspect result flagged as invalid until verified, the verification route, and separate owners for each follow-up item."),
    "evidence_out": "Readiness tracker with dated results, dispositions and named owners.",
    "critical": "Independently clearing compatibility or changing listing status.",
    "reflect": "Which items on your unit's candidate checklist expire, and does anyone track their expiry dates?",
    "practice": {
        "intro": "Use synthetic or de-identified examples only.",
        "items": [
            "Build a readiness tracker for a synthetic candidate with at least eight dated items and owners.",
            "Explain cPRA, DSA and crossmatch to a peer in plain language without using the acronyms.",
            "Walk through your laboratory's sample-labeling and verification procedure with the histocompatibility staff.",
            "Practice a scripted check-in call that asks about admissions, transfusions and pregnancies.",
            "Review one candidate's vaccine record against the program's pre-transplant schedule.",
        ],
    },
    "readings": [
        ("highly-sensitized-kidney-transplant-candidates-clinician.html", "Deeper dive on sensitization and access for highly sensitized candidates."),
        ("transplant-prehabilitation.html", "Prehabilitation for frail candidates."),
        ("viral-infections-vaccinations-ckd.html", "Vaccines and viral screening in kidney disease."),
    ],
    "calcs": ["calc-frailty-assessment.html", "calc-epts.html"],
    "terms": [
        ("Sensitization", "Development of antibodies against foreign HLA after pregnancy, transfusion or a previous transplant."),
        ("Crossmatch", "A test of the recipient's serum against a specific donor's cells or HLA type to detect donor-specific antibodies."),
        ("Hyperacute rejection", "Immediate graft destruction caused by preformed antibodies against donor antigens."),
        ("Prehabilitation", "Structured exercise and nutrition before surgery to build physiologic reserve."),
    ],
    "quiz": [
        {"stem": "Which statement best distinguishes cPRA from a donor-specific antibody (DSA)?",
         "options": [("cPRA estimates the share of donors a candidate is sensitized against; DSA is an antibody against a particular donor's HLA.", True, "cPRA describes breadth; DSA and crossmatch address a specific donor."),
                     ("They are two names for the same test.", False, "They answer different questions."),
                     ("cPRA identifies the antibody that will reject a particular kidney.", False, "Only donor-specific testing does that."),
                     ("DSA measures blood group compatibility.", False, "ABO is a separate system.")],
         "sources": ["txcand2020"]},
        {"stem": "A listed candidate received two units of blood at another hospital last month. What is the priority nursing action?",
         "options": [("Report the sensitizing event to the coordinator and laboratory pathway and document who will arrange a repeat serum sample.", True, "New antibodies may form; the stored sample may no longer be current."),
                     ("No action; transfusions do not affect transplant.", False, "Transfusion is a recognized sensitizing event."),
                     ("Remove her from the list yourself.", False, "Listing status is a program decision."),
                     ("Advise her to refuse all future transfusions.", False, "Transfusion decisions belong to the treating team weighing her safety.")],
         "sources": ["txcand2020"]},
        {"stem": "Why must the crossmatch use the candidate's current serum?",
         "options": [("Antibodies can appear after recent sensitizing events, and an old sample could miss them.", True, "Current serum reflects current antibodies."),
                     ("Old serum samples spoil within a day.", False, "Serum is stored frozen for antibody testing."),
                     ("PhilHealth requires it.", False, "The reason is immunologic safety."),
                     ("It makes the test cheaper.", False, "Not the reason.")],
         "sources": ["txcand2020"]},
        {"stem": "Why does a candidate's cancer screening matter before transplant?",
         "options": [("Immunosuppression weakens immune surveillance and may allow an undetected cancer to progress.", True, "This is the physiologic rationale for cancer screening."),
                     ("Cancer screening is needed only for living donors.", False, "Recipients need it too."),
                     ("It is an administrative formality.", False, "It addresses real risk."),
                     ("Cancer cells reject the kidney.", False, "Not the mechanism.")],
         "sources": ["txcand2020", "engels2011"]},
        {"stem": "What do transplant infectious-disease guidelines recommend about latent tuberculosis in candidates?",
         "options": [("Screen all candidates and treat latent infection, ideally starting before transplant.", True, "Reactivation under immunosuppression can be severe."),
                     ("Screen only candidates with cough.", False, "Latent infection is asymptomatic by definition."),
                     ("Defer all screening until after transplant.", False, "Pre-transplant screening allows treatment before immunosuppression."),
                     ("Tuberculosis is not relevant in transplant.", False, "It is a major concern, especially in high-burden countries.")],
         "sources": ["subramanian2019"]},
        {"stem": "In a prospective cohort, how was frailty at transplant related to survival?",
         "options": [("Frail recipients had lower five-year survival and about twice the adjusted risk of death.", True, "Five-year survival was 77.5 percent in frail versus 91.5 percent in nonfrail recipients."),
                     ("Frailty had no relationship with survival.", False, "The association was independent of age."),
                     ("Frailty only mattered in recipients older than 80.", False, "It was associated with risk regardless of age."),
                     ("Frail recipients lived longer.", False, "The opposite was found.")],
         "sources": ["mcadams2015"]},
        {"stem": "What timing is recommended for vaccines before transplant when possible?",
         "options": [("Start inactivated series and complete any live vaccine series before transplant; wait 4 weeks after a live vaccine.", True, "KDIGO recommends both (1B): vaccines work better before immunosuppression, and live vaccines are generally avoided afterward."),
                     ("All vaccines should wait until one year after transplant.", False, "Pre-transplant vaccination is preferred."),
                     ("Live vaccines are preferred immediately after transplant.", False, "Live vaccines are generally avoided after transplant."),
                     ("Vaccines are not needed for transplant candidates.", False, "Up-to-date vaccination is part of readiness.")],
         "sources": ["txcand2020", "danziger2019"]},
        {"stem": "A candidate has missed two scheduled tests. What is the most appropriate first action?",
         "options": [("Contact her through the approved route, explore barriers, document, and coordinate completion.", True, "Missed tests often signal solvable barriers."),
                     ("Document her as nonadherent and notify the committee to decline her.", False, "Premature and outside nursing scope."),
                     ("Wait for her next quarterly call.", False, "Delays readiness and leaves the barrier unsolved."),
                     ("Cancel her remaining tests.", False, "Unhelpful and unauthorized.")],
         "sources": []},
        {"stem": "A laboratory result in a candidate's file shows a different middle name. What should happen?",
         "options": [("Flag it as unverified, exclude it from decisions, and verify identity through the laboratory's procedure.", True, "Identity discrepancies stop the workflow until resolved."),
                     ("Correct the name by hand.", False, "Altering a result record is unsafe and improper."),
                     ("Use it anyway; middle names are often wrong.", False, "A wrong-patient result could cause serious harm."),
                     ("Delete it from the chart.", False, "Records are corrected through procedure, not deleted.")],
         "sources": []},
        {"stem": "Why are ABO-incompatible kidneys normally avoided?",
         "options": [("Natural anti-A or anti-B antibodies can attack antigens on the graft's blood vessels.", True, "A and B antigens are expressed on vascular endothelium."),
                     ("Blood type determines kidney size.", False, "Not related."),
                     ("ABO incompatibility only matters for transfusions.", False, "It matters for kidneys too."),
                     ("They are never possible under any protocol.", False, "Specialized antibody-removal protocols exist at some centers.")],
         "sources": []},
        {"stem": "Which event is NOT typically a sensitizing event for HLA antibodies?",
         "options": [("A routine eye examination.", True, "No exposure to foreign HLA occurs."),
                     ("Pregnancy.", False, "Exposure to paternal HLA can sensitize."),
                     ("Blood transfusion.", False, "Transfusion is a classic sensitizing event."),
                     ("A previous transplant.", False, "Prior grafts commonly sensitize.")],
         "sources": []},
        {"stem": "Which best describes a readiness tracker entry?",
         "options": [("Item, date done, disposition, repeat or expiry date, and owner of the next step.", True, "These fields keep a candidate ready on the day of an offer."),
                     ("Item name only.", False, "Without dates and owners, readiness cannot be judged."),
                     ("Free-text comments about the family.", False, "Not a tracker."),
                     ("The results of a single day's labs.", False, "Readiness spans many dated items.")],
         "sources": []},
        {"stem": "A wait-listed candidate is hospitalized with pneumonia. Who decides whether her list status changes?",
         "options": [("The transplant program, after the nurse reports the admission.", True, "The nurse reports; the program decides and communicates status."),
                     ("The ward nurse caring for her.", False, "Not within nursing authority."),
                     ("The patient herself.", False, "She participates, but listing status is a program decision."),
                     ("PhilHealth.", False, "Coverage does not determine clinical status.")],
         "sources": ["txcand2020"]},
        {"stem": "What does a cPRA of 95 percent mean in practice?",
         "options": [("Roughly 95 of 100 donors would be unsuitable on antibody grounds, so waiting is likely to be longer.", True, "High cPRA narrows the pool of compatible donors."),
                     ("The transplant will be 95 percent successful.", False, "cPRA is not a success rate."),
                     ("The candidate has a 95 percent match with her sibling.", False, "Not what cPRA measures."),
                     ("The candidate has no antibodies.", False, "High cPRA means broad sensitization.")],
         "sources": ["txcand2020"]},
        {"stem": "Why is psychosocial and financial review part of evaluation?",
         "options": [("Lifelong medicines, monitoring and visits require support, understanding and resources.", True, "Barriers identified early can be addressed before transplant."),
                     ("To exclude poor patients.", False, "The purpose is to identify and solve barriers, not exclude."),
                     ("To decide who will donate.", False, "Donor decisions are separate and voluntary."),
                     ("It is optional for recipients.", False, "It is a standard evaluation domain.")],
         "sources": ["txcand2020"]},
    ],
    "exam": [
        {"stem": "A listed candidate with an old serum sample on file reports a recent transfusion elsewhere. What is the correct sequence?",
         "options": [("Capture the date and records, notify the team and laboratory pathway, confirm the repeat-sampling owner, and document who will communicate any status change.", True, "Covers reporting, ownership and communication."),
                     ("Reassure her and record it at the next annual review.", False, "Delays an immunologic safety step."),
                     ("Order a crossmatch yourself.", False, "Outside nursing scope."),
                     ("Tell her she has been removed from the list.", False, "Status decisions and communication belong to the program.")],
         "sources": ["txcand2020"]},
        {"stem": "Does a high cPRA identify the antibody that would reject a particular donor's kidney?",
         "options": [("No. Donor-specific antibody testing and the crossmatch address a particular donor.", True, "cPRA summarizes breadth of sensitization."),
                     ("Yes. cPRA is donor-specific.", False, "It is population-based."),
                     ("Yes, if it is above 50 percent.", False, "No cutoff makes it donor-specific."),
                     ("Only for living donors.", False, "It is never donor-specific.")],
         "sources": ["txcand2020"]},
        {"stem": "A candidate missed two evaluation tests. What is the best first action?",
         "options": [("Contact through the approved route, assess barriers, document, and coordinate completion.", True, "Barrier-focused follow-up."),
                     ("Report nonadherence to the committee.", False, "Premature without exploring barriers."),
                     ("Discharge her from the program.", False, "Outside scope."),
                     ("Wait for her to reschedule.", False, "Passive; risks losing her.")],
         "sources": []},
    ],
}
