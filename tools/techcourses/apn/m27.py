# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 27: Life with a transplant: rejection, infection and adolescent adherence.
Written November 27, 2026 for the Renal Care Academy in the voice of the Physician on Duty modules, to the medical teaching
standard. Figures from the PubMed abstracts of Foster 2011 (USRDS age and graft failure), TAKE-IT 2018, Abu Bakar 2019, Eaton 2025
(TAKE-IT secondary analysis), the 2024 BK polyomavirus consensus and the AST 2019 EBV/PTLD guideline. PhilHealth post-transplant
package from PhilHealth's own documents. No doses. Every case is fictional."""

MODULE = {
    "image_alt": "A teenage girl and a pediatric nephrologist sit side by side looking at a phone with a medicine reminder app, while her mother waits outside the clinic door.",
    "objectives": [
        "Work up a rising creatinine in a child or adolescent with a kidney transplant, keeping rejection, infection, obstruction, drug toxicity and volume in the differential at once.",
        "Interpret tacrolimus levels and their variability as surrogates, and screen for BK polyomavirus and Epstein-Barr virus as current guidance describes.",
        "Treat adolescent nonadherence as a clinical problem with evidence-based support, and plan a closed-loop transition to adult care.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the graft&rsquo;s long-term physician</span>Most transplant programs hand a child back to the referring pediatric nephrologist within months of surgery. From then on you see the graft more often than the surgeon does: you read the creatinine trend, decide when a biopsy is needed, watch for viruses that live in an immunosuppressed child, and notice first when a teenager stops taking the tablets. You also prepare the young person, years ahead, for the day the adult nephrologist takes over.</div>
{{plain:Think of a transplanted kidney as a guest who is welcome only because the house guard has been told to look away. Tacrolimus and the other medicines are that instruction. Miss them, and the guard wakes up. Give too much, and the guard also stops watching for burglars, such as viruses.}}
<p>The picture has a limit. The immune system is not one guard but many cells with memory. A few weeks of missed doses can trigger an attack that leaves permanent scarring, and antibodies formed during that time may never go away. The medicines are also toxic in their own right: tacrolimus constricts the afferent arteriole and can raise the creatinine without any rejection at all. The balance is narrow, it moves with growth, puberty and behavior, and the creatinine alone cannot tell you which side you have fallen off.</p>
{{cards:Key numbers|Graft failure by current age, United States Renal Data System (USRDS) cohort::Highest crude rate at age 19 (6.6 per 100 person-years); hazard ratio 1.20 at ages 17&ndash;24 vs 25&ndash;29|Teen Adherence in Kidney Transplant Effectiveness of Intervention Trial (TAKE-IT), 169 randomized, ages 11&ndash;24::Odds ratio 1.66 for taking prescribed doses; 1.74 for taking them on time|Tacrolimus variability and late rejection (case-control)::Coefficient of variation 44% vs 24%|BK polyomavirus screening in children (2024 consensus)::Monthly to month 9, then every 3 months to 3 years after transplant|Epstein-Barr virus (EBV) and post-transplant lymphoproliferative disorder (PTLD), 2019 guideline::Reduction of immunosuppression is the best validated intervention}}
<p>Most rises in creatinine after the first months have a cause you can find: dehydration, a urinary tract problem, a drug level that is too high, a virus, or rejection. A few are the first sign that an adolescent has stopped taking medicines, and that cause is the one most often missed and most often punished instead of treated. Your work is to work up the graft systematically, to read drug levels as clues rather than verdicts, and to help a young person take ownership of a kidney that must last into adult life.</p>
""",
    "case": {"title": "Levels that swing",
             "html": """
<p>Kristine &ldquo;Tin&rdquo; Mercado is 16. She received a kidney from her father at 13 for renal dysplasia and has done well. She lives in Lipa, Batangas, and since starting Grade 11 she stays with her grandmother in the city during the week. Her last four tacrolimus trough levels, a month apart, read 9.8, 3.1, 11.2 and 2.6 ng/mL. Her creatinine has crept from 0.90 to 1.17 mg/dL, a rise of 30%, over three months. Blood pressure is 128/82 mm Hg; she has no fever and no urinary symptoms.</p>
<p>The pediatric resident suggests raising the tacrolimus dose because two levels were low. Tin&rsquo;s mother says, &ldquo;She is lazy with her medicines. Please scold her.&rdquo; Tin looks at the floor. When you see her alone, she says she sometimes forgets the evening dose when she is out with classmates, and that her grandmother does not know about her tablets.</p>
""",
             "questions": ["What could explain the rise in creatinine, and how do you work it up?",
                           "What do the swinging levels mean, and should the dose go up?",
                           "How do you help Tin take her medicines and prepare her for adult care?"]},
    "sections": [
        ("physiology", "Physiology", "Why grafts fail, and what the numbers measure", """
<p><strong>Rejection.</strong> T cells recognize donor antigens and infiltrate the tubules and interstitium (T-cell-mediated rejection). B cells and plasma cells can make donor-specific antibodies that injure the graft&rsquo;s capillaries (antibody-mediated rejection). Both are held off by continuous immunosuppression. When drug exposure falls, even intermittently, the immune system gets windows of opportunity, and memory makes the next attack easier.</p>
<p><strong>Calcineurin inhibitor exposure.</strong> Tacrolimus is absorbed variably, metabolized by enzymes in the gut and liver, and affected by food, other drugs, diarrhea and genetics. The trough level is a surrogate: it estimates exposure; it does not measure rejection or toxicity. High exposure constricts the afferent arteriole and can raise creatinine within days, which reverses when exposure falls; over years it may cause chronic injury. Low or erratic exposure invites rejection.</p>
<p><strong>Viruses.</strong> Immunosuppression lets latent viruses reactivate. BK polyomavirus lives in the urinary tract and can cause BK nephropathy, a tubulointerstitial injury that looks like rejection on a creatinine chart. Epstein-Barr virus (EBV) infects B cells; a child who was seronegative before transplant and acquires EBV, often from the donor, is at risk of post-transplant lymphoproliferative disorder (PTLD).</p>
<p><strong>The adolescent brain.</strong> The brain systems that weigh future consequences mature later than the systems that respond to peers and reward. That is not a moral failing; it is development. A 16-year-old who knows perfectly well what tacrolimus does can still miss the evening dose at a friend&rsquo;s house, because the future feels far away and the friends are right there.</p>
<div class="table-wrap"><table>
<thead><tr><th>Cause of a rising creatinine</th><th>Mechanism</th><th>Clues</th><th>First tests</th></tr></thead>
<tbody>
<tr><td>Volume depletion</td><td>Reduced graft perfusion</td><td>Vomiting, diarrhea, heat, poor intake</td><td>Examination, repeat creatinine after rehydration</td></tr>
<tr><td>Tacrolimus toxicity</td><td>Afferent vasoconstriction</td><td>High trough, tremor, new interacting drug</td><td>Trough level, medication review</td></tr>
<tr><td>Rejection</td><td>T-cell or antibody-mediated injury</td><td>Low or erratic levels, missed doses, new proteinuria</td><td>Donor-specific antibodies, urinalysis, protein-to-creatinine ratio, biopsy</td></tr>
<tr><td>BK nephropathy</td><td>Viral tubulointerstitial injury</td><td>Often silent; may coexist with high immunosuppression</td><td>Plasma BK viral load</td></tr>
<tr><td>Obstruction or reflux into the graft</td><td>Back-pressure; infection</td><td>Valve bladder, febrile urinary tract infection (UTI), poor catheterization</td><td>Graft ultrasound, bladder review</td></tr>
<tr><td>Recurrent disease</td><td>Original disease attacks the graft</td><td>Proteinuria in steroid-resistant nephrotic syndrome (SRNS); hemolysis in atypical hemolytic uremic syndrome (aHUS)</td><td>Urine protein, hemolysis markers</td></tr>
</tbody></table></div>
{{key:A creatinine rise in a graft has several causes at once more often than you expect. Test for all of them before you treat one.}}
{{fig:apn27_a}}
"""),
        ("evidence", "Evidence", "What the evidence shows", """
<p><strong>Adolescence is the dangerous age.</strong> Foster and colleagues analyzed 90,689 first kidney transplant recipients younger than 40 in the USRDS, 1988 to 2009; 18,310 were younger than 21 at transplant. Crude graft failure rates peaked at age 19, at 6.6 per 100 person-years. Compared with the same time after transplant at ages 25 to 29, death-censored graft failure was higher at 17 to 20 and 21 to 24 (hazard ratio 1.20 for each) and lowest at 5 to 12 (0.60 at 5 to 9, 0.56 at 10 to 12), whatever the age at transplant.[[apn27_2]] The design was observational; nonadherence is the most plausible but not the only explanation. The finding tells you when to intensify support: through the late teens and the move to adult care.</p>
<p><strong>Adherence can be improved.</strong> TAKE-IT randomized 169 recipients aged 11 to 24 at eight centers in Canada and the United States. After a 3-month run-in with electronic pill monitoring, the intervention group chose text, e-mail or visual reminders and met a coach every 3 months to review their adherence data and solve the barriers they chose; the control group met coaches without feedback. The intervention group had greater odds of taking prescribed doses (odds ratio 1.66, 95% confidence interval 1.15 to 2.39) and of taking them on time (1.74, 1.21 to 2.50). Electronic data were missing for some participants, and the trial was underpowered for rejection and graft loss.[[apn27_1]] It demonstrates better adherence, a behavior; it does not show that grafts lasted longer.</p>
<p><strong>Drug-level variability is a clue, not a verdict.</strong> In a case-control study of 25 children with biopsy-proven late acute cellular rejection and 25 matched stable controls, tacrolimus coefficient of variation over the previous year was 44% against 24%; a threshold of 26% on a related measure (mean absolute deviation) had 76% sensitivity and 76% specificity, and children with rejection spent more time with very low levels.[[apn27_5]] Yet in a secondary analysis of 103 TAKE-IT participants, high variability (standard deviation of 2 or more, or coefficient of variation of 30% or more) did not consistently match electronically monitored or self-reported adherence, and the authors warned that relying on variability may misidentify nonadherence.[[apn27_6]] Variability marks a graft at risk. It does not prove that the young person is skipping doses; diarrhea, interacting drugs, timing of the blood draw and food all move levels too.</p>
<p><strong>BK polyomavirus.</strong> The second international consensus guidelines (2024), graded with the Grading of Recommendations Assessment, Development and Evaluation (GRADE) system, recommend screening all kidney recipients monthly for plasma BK viral load until month 9, then every 3 months until 2 years after transplant, or 3 years for children. Where plasma testing is limited, urine cytology at similar times can exclude BK nephropathy, with plasma testing when decoy cells are seen. Immunosuppression should be reduced in predefined steps for persisting or high viral loads or biopsy-proven nephropathy; in children with persisting viremia, biopsy may be considered even without graft dysfunction. Current studies do not support leflunomide, cidofovir, quinolones or intravenous immunoglobulin.[[apn27_3]]</p>
<p><strong>EBV and PTLD.</strong> The American Society of Transplantation (AST) 2019 guideline names pre-transplant EBV seronegativity and primary EBV infection, often donor-transmitted, as important risk factors for early EBV-positive PTLD, a particular concern in children. Low-quality evidence supports preemptive strategies that measure the EBV viral load in blood and lower it; reduction of immunosuppression is the best validated intervention, and tissue biopsy with World Health Organization (WHO) pathology classification remains the diagnostic standard.[[apn27_4]]</p>
{{key:Adherence support has trial evidence; drug-level variability and viral loads are surrogates that tell you where to look. Use each for what it can show.}}
"""),
        ("workup", "Graft dysfunction", "Working up a rising creatinine", """
<p>A confirmed rise in creatinine of the size in Tin&rsquo;s case is a reason to act this week, not at the next routine visit. Confirm it first: same laboratory, a well-hydrated child, a trough drawn at the right time before the morning dose.</p>
{{flow:A rising creatinine in a pediatric graft|Confirm::Repeat creatinine with a correctly timed tacrolimus trough; ask about vomiting, diarrhea, new medicines, and when the last dose was really taken.|Look for the simple causes::Volume status, blood pressure, a febrile UTI, a full bladder or poor catheterization in a child with a valve bladder.|Image::Graft ultrasound for hydronephrosis, collections and flow.|Test the immune and viral causes::Urinalysis and protein-to-creatinine ratio, donor-specific antibodies, plasma BK viral load, EBV viral load where the program monitors it.|Decide on biopsy::If no reversible cause explains the rise, or levels have been low or erratic, discuss a graft biopsy with the transplant team. Treatment of rejection follows the biopsy.|Talk to the young person alone::Ask how doses are really taken, by whom, and when they are missed. Write what you learn.}}
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>What it suggests</th><th>What not to do</th></tr></thead>
<tbody>
<tr><td>High trough, tremor, creatinine up</td><td>Calcineurin inhibitor effect</td><td>Do not assume rejection and add immunosuppression</td></tr>
<tr><td>Low or swinging troughs, new donor-specific antibodies, proteinuria</td><td>Underexposure and rejection risk</td><td>Do not simply raise the dose before you know whether doses are being taken</td></tr>
<tr><td>Rising plasma BK viral load</td><td>BK viremia, possible nephropathy</td><td>Do not intensify immunosuppression for presumed rejection without considering a biopsy</td></tr>
<tr><td>Hydronephrosis of the graft with a high residual bladder volume</td><td>Bladder dysfunction or obstruction</td><td>Do not overlook the bladder in a child with congenital anomalies of the kidney and urinary tract (CAKUT)</td></tr>
</tbody></table></div>
<p><strong>Why not just raise the dose.</strong> If Tin misses evening doses on some days and takes all of them on others, a higher dose produces higher peaks on the good days, more toxicity, and no protection on the days she forgets. Raising the dose treats the number, not the cause. Changes to the regimen belong to you and the transplant team once you know what is happening, using the program&rsquo;s protocol and pharmacist.</p>
<div class="tc-scene"><span class="tc-lab">By Viber from a provincial hospital &middot; fictional</span><p>A pediatrician in Iloilo messages you about Gabriel, 9, transplanted two years ago, admitted with diarrhea. His creatinine has doubled and his tacrolimus trough is far above his usual range.</p><p>You explain that diarrhea can raise tacrolimus levels and cause vasoconstrictive injury on top of dehydration. You ask for rehydration per the ward&rsquo;s pediatric protocol, a repeat trough, and a call to you before the next dose so the dose can be held or adjusted by the transplant team.</p><p class="tc-scene-take"><b>What this shows.</b> A level is a clue to exposure. Read it with the story before deciding what it means.</p></div>
{{call:<ul><li>Creatinine up by a clinically significant amount on repeat, with no clear reversible cause</li><li>Fever, graft tenderness, or reduced urine output in a transplanted child</li><li>A trough far outside the program&rsquo;s range, or a new interacting drug started elsewhere</li><li>Rising BK or EBV viral loads on surveillance</li><li>Lymph node enlargement, unexplained fever or weight loss (consider PTLD)</li><li>A young person who says, or whose family says, that doses are being missed</li></ul>}}
{{key:Never raise the dose on a swinging level until you know how the doses are being taken. Ask the young person, alone, first.}}
"""),
        ("practice", "Adherence and transition", "Adherence as a clinical problem, and the handover to adult care", """
<p><strong>Name it without blame.</strong> Start from the TAKE-IT approach: the young person chooses the reminders, reviews the data with a coach, and picks the barrier to work on.[[apn27_1]] Scolding moves adherence underground; problem-solving brings it into the room. Ask open questions alone with the adolescent: When is the hardest time to take your medicine? Who knows you take it? What happens on weekends? Then let the young person choose one change.</p>
<div class="table-wrap"><table>
<thead><tr><th>Barrier the adolescent names</th><th>Mechanism</th><th>What can help</th></tr></thead>
<tbody>
<tr><td>&ldquo;I forget in the evening when I&rsquo;m out&rdquo;</td><td>Routine broken by social life</td><td>A phone alarm and a small pill case in the school bag; a dosing time the program agrees is workable</td></tr>
<tr><td>&ldquo;My friends don&rsquo;t know&rdquo;</td><td>Fear of stigma</td><td>Practice what to say; choose one trusted friend</td></tr>
<tr><td>&ldquo;I stay at Lola&rsquo;s during the week&rdquo;</td><td>Two households, no supervision at one</td><td>Bring the grandmother into the plan, with the young person&rsquo;s agreement</td></tr>
<tr><td>&ldquo;The tablets make me look fat&rdquo;</td><td>Side effects that matter to identity</td><td>Discuss with the transplant team and pharmacist; acknowledge the concern as real</td></tr>
<tr><td>&ldquo;We ran out&rdquo;</td><td>Cost, pharmacy supply, travel</td><td>Check coverage under the post-transplant Z benefit; involve the social worker</td></tr>
</tbody></table></div>
<p><strong>Coverage.</strong> PhilHealth&rsquo;s Z benefit for post-kidney transplantation services in children, PhilHealth Circular (PC) 2025-0011, covers post-transplant care for pediatric recipients and their living donors at contracted facilities, including items such as maintenance immunosuppression, prophylaxis, drug-level monitoring and laboratory tests as its annexes list.[[apn27_8]] Confirm with the facility&rsquo;s Z benefit coordinator on the date of service which medicines and tests are covered and how often. A benefit that covers a level a set number of times a year does not tell you how often to check one.</p>
<p><strong>Transition.</strong> The International Society of Nephrology (ISN) and International Pediatric Nephrology Association (IPNA) consensus describes transfer to adult care as the end of a transition process that involves both teams, individualized to the young person, focused on self-management skills and on the support around them.[[apn27_7]] In practice: start the conversation around age 12 to 14, see the adolescent alone for part of every visit, teach them to name their diagnosis, medicines and doses, to order refills and to call the unit themselves, and write a handover letter that names the adult nephrologist who has agreed to accept, the date of the first adult visit, and who confirms that it happened.</p>
<div class="tc-scene"><span class="tc-lab">At the joint clinic &middot; fictional</span><p>Mark, 18, is moving to adult care. You arrange one visit in which you and the adult transplant nephrologist see him together. He explains his own medicines and his last biopsy result; the adult nephrologist books his first visit and gives him a direct number.</p><p>Six weeks later you call the adult clinic to confirm he attended. He did not; the clinic had changed its schedule. You and the adult team rebook him the same day.</p><p class="tc-scene-take"><b>What this shows.</b> A transition letter is not a transfer. The loop closes only when someone confirms the first adult visit happened.</p></div>
{{key:Treat nonadherence like any other complication: name it without blame, find its mechanism, and choose the intervention with the young person.}}
{{fig:apn27_b}}
"""),
    ],
    "debrief": [
        "<p><strong>The differential.</strong> A 30% rise over three months is real and needs a work-up this week. Repeat the creatinine with a correctly timed trough. Check volume status and blood pressure, and ask about diarrhea and new medicines. Order a graft ultrasound, urinalysis and protein-to-creatinine ratio, donor-specific antibodies, and a plasma BK viral load. With erratic, often low exposure, rejection is the leading concern, and if no reversible cause is found, discuss a biopsy with the transplant team. Her diagnosis was renal dysplasia, so recurrence is unlikely, but a bladder problem should be asked about.</p>",
        "<p><strong>The levels and the dose.</strong> Levels that alternate between high and low, in a young person who says she misses evening doses, most likely reflect intermittent dosing rather than a dose that is too small. Raising the dose would produce toxic peaks on the days she takes it and no cover on the days she does not. Variability marks her graft as at risk, as in the case-control data, but the TAKE-IT secondary analysis shows it is not proof of nonadherence by itself, so check timing of blood draws, diarrhea and interacting drugs too. Keep the regimen unchanged until the work-up and the adherence picture are clear, and make any change with the transplant team and pharmacist.</p>",
        "<p><strong>Adherence and transition.</strong> Thank Tin for telling you. Do not scold her, and ask her mother to stop scolding too. Use the TAKE-IT approach: Tin chooses a reminder (a phone alarm and a pill case in her school bag), agrees to bring her grandmother into the plan, and reviews how it went at a short visit in a month. Arrange the psychologist or social worker if available. Check that her medicines and levels are covered under PhilHealth PC 2025-0011 at her transplant facility. Start transition now: see her alone at every visit, teach her to explain her own regimen and order refills, and plan a joint visit with an adult transplant nephrologist before she turns 18, with a confirmed first adult appointment.</p>",
    ],
    "skills": {"title": 'Life with a transplant: rejection, infection and adolescent adherence',
               "intro": "Complete with a preceptor, in simulation or at your own unit. Sign-off is local.",
               "items": [("Works up a rising creatinine in a graft using a structured differential", False),
                         ("Interprets a series of tacrolimus levels with the clinical story before any dose change", False),
                         ("Conducts an adherence conversation alone with an adolescent using a problem-solving approach", False),
                         ("Writes a transition handover letter with a named accepting physician and a confirmed first visit", False)],
               "placement": "Simulation or supervised practice"},
    "quiz": [
        ("A 16-year-old&rsquo;s tacrolimus troughs alternate between high and low, and her creatinine has risen 30%. She admits missing evening doses. What is the best next step?",
         ["Raise the tacrolimus dose because two levels were low",
          "Work up the creatinine rise and address adherence with her before changing the regimen",
          "Stop tacrolimus because of toxicity",
          "Wait for the next routine visit"],
         1,
         "Intermittent dosing causes swinging levels; a higher dose adds toxic peaks without covering missed doses. Work up rejection, BK, obstruction and toxicity, and solve the adherence problem."),
        ("What did the USRDS analysis by Foster and colleagues show?",
         ["Graft failure was highest in children aged 5 to 12",
          "Age had no association with graft failure",
          "Graft failure was lowest at ages 17 to 24",
          "Graft failure was highest at ages 17 to 24, regardless of age at transplant"],
         3,
         "Crude rates peaked at 19 (6.6 per 100 person-years); hazard ratio 1.20 at 17&ndash;24 vs 25&ndash;29. The design was observational."),
        ("What did the TAKE-IT trial demonstrate?",
         ["Better electronically measured adherence with a multicomponent intervention",
          "Fewer graft losses with reminders",
          "No effect on adherence",
          "That tacrolimus variability equals nonadherence"],
         0,
         "Odds ratio 1.66 for taking doses and 1.74 for timing. The trial was underpowered for rejection and graft loss."),
        ("According to the 2024 BK polyomavirus consensus, how long should children be screened with plasma BK viral load?",
         ["Only when creatinine rises",
          "Monthly for the first year only",
          "Monthly until month 9, then every 3 months until 3 years after transplant",
          "Once at 6 months"],
         2,
         "The schedule extends to 2 years in adults and 3 years in children. Urine cytology can be used where plasma testing is limited."),
        ("A transplanted 7-year-old who was EBV-seronegative before transplant has a rising EBV viral load. What does the AST guideline name as the best validated intervention?",
         ["Adding an antiviral as sole therapy",
          "Reduction of immunosuppression",
          "Increasing immunosuppression",
          "Repeating the test in a year"],
         1,
         "Reduction of immunosuppression is the best validated intervention; preemptive strategies rest on low-quality evidence, and tissue biopsy diagnoses PTLD."),
    ],
    "terms": [("aHUS", "Atypical hemolytic uremic syndrome"), ("AST", "American Society of Transplantation"),
              ("CAKUT", "Congenital anomalies of the kidney and urinary tract"), ("EBV", "Epstein-Barr virus"),
              ("GRADE", "Grading of Recommendations Assessment, Development and Evaluation"),
              ("IPNA", "International Pediatric Nephrology Association"), ("ISN", "International Society of Nephrology"),
              ("PC", "PhilHealth Circular"), ("PTLD", "Post-transplant lymphoproliferative disorder"),
              ("SRNS", "Steroid-resistant nephrotic syndrome"), ("TAKE-IT", "Teen Adherence in Kidney Transplant Effectiveness of Intervention Trial"),
              ("USRDS", "United States Renal Data System"), ("UTI", "Urinary tract infection"), ("WHO", "World Health Organization")],
    "readings": [('kidney-transplant.html', 'Beyond Dialysis: Understanding Kidney Transplant'),
                 ('transplant-allograft-failure.html', 'Kidney Transplant Failure — Understanding Rejection & What Comes Next'),
                 ('ckd-children-young-adults.html', 'CKD in Children & Young Adults')],
    "calcs": ["calc-tacrolimus-level-check.html", "calc-allograft-egfr-trend.html", "calc-ckid-u25-egfr.html",
              "calc-transplant-prom.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
