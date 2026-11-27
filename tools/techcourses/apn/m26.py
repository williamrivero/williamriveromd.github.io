# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 26: Preparing a child for kidney transplantation.
Written November 27, 2026 for the Renal Care Academy in the voice of the Physician on Duty modules, to the medical teaching
standard. Guideline content from the KDIGO 2020 candidate and 2017 living-donor guideline abstracts, IPNA 2020 SRNS, the 2017 KDIGO
aHUS/C3G controversies report and the 2022 PUV meta-analysis (PubMed). Philippine law and PhilHealth items from the Supreme Court
e-library (RA 7170, DOH AO 2010-0018) and PhilHealth's own documents. No doses. Every case is fictional."""

MODULE = {
    "image_alt": "A teenage boy sits between his father and his aunt in a hospital clinic room while a pediatric nephrologist and a urologist review a bladder study on a screen.",
    "objectives": [
        "Explain why the lower urinary tract, recurrence risk and vaccination are settled before a child is listed or a donor is worked up.",
        "Guide a family through living-donor evaluation that is ethical and lawful in the Philippines, and recognize an offer that is not.",
        "Assemble a transplant readiness plan, including PhilHealth Z benefit requirements, without turning coverage into clinical timing.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the child&rsquo;s advocate before the operating room</span>The transplant surgeon operates and the transplant program decides on candidacy. The attending pediatric nephrologist prepares the child: makes the bladder safe with the urologist, completes vaccines while they can still work, finds out whether the original disease can come back, sits with the family while a relative offers a kidney, and keeps the process inside Philippine law. PhilHealth&rsquo;s kidney transplant Z benefit names a pediatric nephrologist certified by the Pediatric Nephrology Society of the Philippines (PNSP) among the pediatric team; that line on a form describes a real job.</div>
{{plain:Think of a transplant as moving a family into a new house. The house can be perfect, but if the plumbing below it backs up, the house floods within a year. Before the move, you check the pipes, fix the wiring, and make sure the old problem that ruined the last house is not waiting in the new one.}}
<p>The picture has a limit. A house is passive; a transplanted kidney is a living organ under constant immune attack, kept alive by medicines the child must take every day for the rest of life. A high-pressure bladder does not only flood the kidney; it carries infection up to it. And some diseases that destroyed the child&rsquo;s own kidneys are carried in the blood, not the kidney, so they move into the new house with the family. Preparation is mostly about those hidden risks.</p>
{{cards:Key numbers|Steroid-resistant nephrotic syndrome, monogenic cause (IPNA 2020)::10&ndash;30% of children|Posterior urethral valves, clean intermittent catheterization (meta-analysis, 49 studies)::Up to 32% (prenatal diagnosis) and 22% (postnatal)|Prenatal vs postnatal valve diagnosis, need for transplant::Odds ratio 1.64, 95% confidence interval (CI) 0.61 to 4.42 (no difference)|PhilHealth KT Z benefit, pediatric team::Includes a PNSP-certified pediatric nephrologist with valid accreditation|PhilHealth kidney transplant (KT) data registry (Advisory 2026-0026)::Registration mandatory to avail of the KT benefit}}
<p>Most children with kidney failure are better off with a transplant than with any form of dialysis, and many Filipino children receive a kidney from a parent or relative. A few are harmed because the transplant came before the bladder was safe, before vaccines were given, or before anyone asked whether the disease would recur. Your work is to find those risks early, fix what can be fixed, explain the rest honestly, and keep every donor offer voluntary, informed and unpaid.</p>
""",
    "case": {"title": "An aunt, a bladder, and an offer",
             "html": """
<p>Jerome Villanueva is 15 and weighs 44 kilograms. He was born with posterior urethral valves, ablated in infancy at a government hospital in Manila. He reached kidney failure last year and does home peritoneal dialysis in Malolos, Bulacan. He is supposed to catheterize his bladder four times a day but admits he does it &ldquo;when I remember.&rdquo; He has had two febrile urinary tract infections this year. His mother works as a caregiver in Hong Kong; his father drives a jeepney.</p>
<p>At clinic today his aunt, Tita Lorna, 38, his mother&rsquo;s younger sister, says she wants to give Jerome a kidney. His father asks whether the operation can be done before Christmas, five weeks away. Then he lowers his voice: a cousin knows &ldquo;someone who can find a donor if Lorna is not a match, for a fee.&rdquo; The urologist&rsquo;s report from last month describes a small, thick-walled bladder with high filling pressures.</p>
""",
             "questions": ["Is Jerome ready for a transplant, and what has to come first?",
                           "How do you handle Tita Lorna&rsquo;s offer and the cousin&rsquo;s suggestion?",
                           "What else must be done before Jerome is ready, including PhilHealth requirements?"]},
    "sections": [
        ("physiology", "Why prepare", "Why transplant, and why the bladder comes first", """
<p><strong>Why a transplant.</strong> Dialysis replaces a fraction of filtration and none of the kidney&rsquo;s endocrine and metabolic work. A functioning graft restores most of it continuously, which matters most in a body that is still growing, learning and going to school. That is why the conversation about transplant begins well before dialysis, not after it.</p>
<p><strong>Why the bladder.</strong> A kidney transplant drains into the child&rsquo;s own bladder. In congenital anomalies of the kidney and urinary tract (CAKUT), especially posterior urethral valves, the bladder may be small, stiff and high-pressure, may empty poorly, or may have been bypassed for years by polyuria and a diaper. High pressure is transmitted back up the ureter to the graft. Residual urine grows bacteria, and in an immunosuppressed child a febrile urinary tract infection can injure the graft and trigger rejection. A bladder that was tolerable for a polyuric native kidney can be dangerous for a new one.</p>
<p><strong>Why the old disease matters.</strong> Some causes of kidney failure live in the kidney itself: dysplasia, obstruction, a genetic podocyte defect. A new kidney does not carry them. Others live in the blood: a circulating factor in some steroid-resistant nephrotic syndrome (SRNS), uncontrolled complement activation in atypical hemolytic uremic syndrome (aHUS), oxalate from the liver in primary hyperoxaluria. These can attack the graft. Knowing which kind of disease the child has is part of the preparation, not an afterthought.</p>
<p><strong>Why vaccines now.</strong> After transplant, immunosuppression blunts the response to vaccines, and live vaccines are generally avoided. The months before transplant are the best window to complete the child&rsquo;s schedule.</p>
<div class="table-wrap"><table>
<thead><tr><th>Hidden risk</th><th>Mechanism</th><th>What it does to a graft</th><th>What you do before transplant</th></tr></thead>
<tbody>
<tr><td>High-pressure or poorly emptying bladder</td><td>Pressure transmitted to the ureter; stagnant urine grows bacteria</td><td>Hydronephrosis of the graft, febrile infections, rejection triggered by infection</td><td>Urodynamics with the urologist; a catheterization plan the child will follow; augmentation or a diversion if needed</td></tr>
<tr><td>Circulating factor (some SRNS)</td><td>An immune factor that injures podocytes</td><td>Recurrent proteinuria, sometimes soon after transplant</td><td>Genetic testing; a recurrence plan agreed with the transplant team</td></tr>
<tr><td>Complement dysregulation (aHUS)</td><td>Uncontrolled alternative complement activation on the endothelium</td><td>Thrombotic microangiopathy in the graft</td><td>Identify the genetic and acquired drivers; plan with the transplant team</td></tr>
<tr><td>Incomplete vaccination</td><td>Immunosuppression blunts responses; live vaccines avoided after transplant</td><td>Preventable infections</td><td>Complete the schedule and record titers where the program requires</td></tr>
<tr><td>Nonadherence</td><td>Missed doses lower drug exposure</td><td>Rejection and graft loss (Module 27)</td><td>Start adherence work before transplant, with the adolescent at the center</td></tr>
</tbody></table></div>
<div class="tc-scene"><span class="tc-lab">At the transplant conference, the forgotten bladder &middot; fictional</span><p>A 12-year-old with valves is presented for a living related transplant. Every box is ticked: cross-match, cardiac review, dental clearance. No one has seen a bladder study since he was 3.</p><p>You ask for urodynamics before the date is set. The study shows a bladder that fills to high pressure and empties poorly. The urologist plans a catheterization program first, and the transplant is moved by three months.</p><p class="tc-scene-take"><b>What this shows.</b> A complete checklist can still miss the organ the graft will drain into. The bladder belongs on the list in its own line.</p></div>
{{key:Settle the bladder, the vaccines and the recurrence risk before anyone sets a date. A graft lost to a preventable cause is a second kidney failure for the child and the donor.}}
{{fig:apn26_a}}
"""),
        ("evidence", "Evidence", "What the evidence and guidelines show", """
<p><strong>Candidate evaluation.</strong> The Kidney Disease: Improving Global Outcomes (KDIGO) 2020 guideline on the evaluation and management of candidates for kidney transplantation used the Grading of Recommendations Assessment, Development and Evaluation (GRADE) approach. It covers access to transplantation, adherence, the cause of kidney failure, infections, malignancy, cardiac, neurologic and other comorbidities, and psychosocial assessment, and asks the team to consider each risk separately and then make an overall judgment within the local context.[[apn26_1]] Its recommendations were written mostly for adults, with pediatric input. Read its graded statements in the guideline itself before quoting a grade to a family or committee.</p>
<p><strong>Living donors.</strong> The KDIGO 2017 guideline on the evaluation and care of living kidney donors concluded that a comprehensive assessment of the donor&rsquo;s whole risk profile should replace decisions based on single risk factors in isolation, and it built a framework for quantitative risk estimation and shared decision-making. Many of its recommendations are ungraded expert opinion, because prospective long-term donor outcome studies are lacking.[[apn26_2]] For Tita Lorna, this means her evaluation is about her own lifetime risk, explained to her by a team whose duty is to her, not to Jerome.</p>
<p><strong>Recurrence of nephrotic syndrome.</strong> The International Pediatric Nephrology Association (IPNA) 2020 recommendations report mutations in podocyte-associated genes in 10&ndash;30% of children with SRNS, with an undefined circulating factor of immune origin assumed in the rest, and list recurrence after transplantation among the serious complications of SRNS.[[apn26_3]] The practical consequence follows from the mechanism: a child whose disease is a structural defect of his own podocytes has a different recurrence outlook from a child with a circulating factor. That is one reason genetic testing belongs before transplant.</p>
<p><strong>aHUS.</strong> A 2015 KDIGO Controversies Conference on aHUS and C3 glomerulopathy reviewed the genetic and acquired drivers of complement disease and the treatment strategies, including anti-complement therapy, and set out a research agenda. Its report is a conference statement, not a graded guideline.[[apn26_4]] For the attending, the point is that a child with aHUS should not reach the transplant list without a known or actively sought complement abnormality and a plan made with the transplant team.</p>
<p><strong>The valve bladder.</strong> A systematic review and meta-analysis of 49 studies (3,820 patients) compared prenatally and postnatally diagnosed posterior urethral valves. Prenatal diagnosis did not change the pooled odds of chronic kidney disease (CKD) progression, kidney replacement therapy or transplant (for transplant, odds ratio 1.64, 95% confidence interval 0.61 to 4.42). Clean intermittent catheterization was needed by up to 32% of the prenatal group and 22% of the postnatal group. Most included studies carried a moderate or serious risk of bias.[[apn26_5]] The review does not test bladder management before transplant, but it shows how common a bladder that needs catheterization is in this population.</p>
{{key:Quote the guideline&rsquo;s grade only from the guideline. Much of transplant preparation rests on GRADE recommendations written for adults, ungraded expert opinion, and conference statements, and the family deserves to know which is which.}}
"""),
        ("philippines", "Law and coverage", "Philippine law, ethics and coverage", """
<p><strong>The law on donation.</strong> Republic Act (RA) 7170, the Organ Donation Act of 1991, governs donation after death.[[apn26_6]] Living donation is governed by Department of Health (DOH) policy. DOH Administrative Order (AO) 2010-0018 revised the national policy on living non-related donation. It commits the DOH to the Anti-Trafficking in Persons Act (RA 9208), the Declaration of Istanbul on Organ Trafficking and Transplant Tourism and the World Health Organization (WHO) guiding principles, does not permit non-directed living non-related donation, and provides for the Philippine Board for Organ Donation and Transplantation to oversee its implementation. The DOH and PhilHealth enforce it through licensing and accreditation.[[apn26_7]] The Declaration of Istanbul was updated in a 2018 edition.[[apn26_8]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>What the attending does</th></tr></thead>
<tbody>
<tr><td>A relative offers a kidney</td><td>Thank the relative, refer to the transplant program&rsquo;s donor team, and keep the donor&rsquo;s evaluation separate from the child&rsquo;s care</td></tr>
<tr><td>A relative seems pressured</td><td>Ask the donor team to see the relative alone; a donor can withdraw at any time without giving a reason to the family</td></tr>
<tr><td>Someone offers to &ldquo;find a donor for a fee&rdquo;</td><td>Say plainly that buying a kidney is not allowed, that you will not take part, and that it puts the child, the donor and the family at legal and medical risk; involve the transplant program&rsquo;s ethics process</td></tr>
<tr><td>A non-related person wants to donate</td><td>Refer to the transplant program, which follows the DOH policy and its own ethics committee; do not judge eligibility yourself</td></tr>
<tr><td>Deceased-donor listing</td><td>Ask the transplant program how its deceased-donor program works and what the family must do to be listed</td></tr>
</tbody></table></div>
<p><strong>Coverage.</strong> PhilHealth&rsquo;s Z benefit for kidney transplantation is governed by PhilHealth Circular (PC) 2024-0035. Its 2025 self-assessment tool for contracted facilities lists, for pediatric transplants, a kidney transplant surgeon certified by the Philippine Society for Transplant Surgeons, a pediatric infectious disease specialist certified by the Pediatric Infectious Disease Society of the Philippines, and a pediatric nephrologist certified by the PNSP, each with valid PhilHealth accreditation.[[apn26_9]] PhilHealth Advisory 2026-0026 made registration in the KT data registry mandatory for patients who avail of the benefit.[[apn26_10]] Post-transplant care in children has its own package (Module 27).</p>
<p>A benefit pays for a transplant at a contracted facility under stated conditions. It does not decide when a child is ready, and it does not replace the clinical steps in this module. Confirm the current rules, rates and forms with the facility&rsquo;s Z benefit coordinator on the date of service.</p>
<div class="tc-scene"><span class="tc-lab">By video call, the mother abroad &middot; fictional</span><p>Shaina, 11, is on peritoneal dialysis in Cabanatuan. Her mother, a nurse in Saudi Arabia, wants to donate and asks whether she can do the tests there and fly home only for the operation.</p><p>You connect her with the transplant program&rsquo;s donor coordinator, who explains which tests may be done abroad, which must be repeated at the program, and that the donor team will want to meet her in person, alone, before any decision. You write down for the family what the program said, so that no one hears a different version later.</p><p class="tc-scene-take"><b>What this shows.</b> Overseas Filipino worker families are common donors. The donor team, not the child&rsquo;s doctor, sets the donor&rsquo;s path, and the family needs it in writing.</p></div>
{{key:A donor gives freely, knows the risks, and can say no at any point. Anything else, including a fee dressed as help, is outside the law and outside your practice.}}
"""),
        ("practice", "Practice", "The readiness plan the attending writes", """
<p>Transplant programs have their own checklists. The attending&rsquo;s plan does something different: it makes sure the child arrives at the program&rsquo;s checklist with the pediatric problems already solved.</p>
<div class="table-wrap"><table>
<thead><tr><th>Domain</th><th>The attending&rsquo;s question</th><th>Who acts with you</th></tr></thead>
<tbody>
<tr><td>Cause of kidney failure</td><td>Do we know it? If SRNS, aHUS, C3 glomerulopathy or hyperoxaluria, has genetic or specific testing been done, and is there a recurrence plan?</td><td>Geneticist, transplant nephrologist</td></tr>
<tr><td>Lower urinary tract</td><td>Is the bladder safe at the volumes a graft will produce? Will the child really catheterize?</td><td>Pediatric urologist, nurse educator</td></tr>
<tr><td>Vaccines</td><td>Is the schedule complete, including the vaccines that cannot be given after transplant?</td><td>Pediatrician, infectious disease specialist</td></tr>
<tr><td>Growth, nutrition and bone</td><td>Is the child as well nourished and as strong as possible before surgery?</td><td>Dietitian (Modules 17 and 18)</td></tr>
<tr><td>Access and dialysis</td><td>Is the current dialysis adequate, and is the access plan protecting veins in case of graft failure?</td><td>Dialysis team (Modules 20 to 25)</td></tr>
<tr><td>Adherence and psychosocial</td><td>Who will give medicines at home? Does the adolescent understand and want this? What about school, money and travel to clinic?</td><td>Social worker, psychologist</td></tr>
<tr><td>Donor</td><td>Is a donor being evaluated by a separate team? Is a deceased-donor listing appropriate?</td><td>Transplant program, donor team</td></tr>
<tr><td>Coverage and paperwork</td><td>Is the facility contracted for the KT Z benefit? Is the child in the KT data registry?</td><td>Z benefit coordinator</td></tr>
</tbody></table></div>
<p><strong>Talking about timing.</strong> Families often hear &ldquo;transplant&rdquo; and start counting weeks. Give them a sequence instead of a date: the bladder plan, the vaccines, the donor&rsquo;s own evaluation, the program&rsquo;s review, then a date. Say which steps depend on the child, which on the donor, and which on the program, and tell them honestly when a step has stalled. A father who knows why the date moved is a father who keeps bringing his son to clinic. Write the sequence in the chart and give the family a copy in Filipino or English, whichever they read more easily.</p>
<div class="tc-scene"><span class="tc-lab">In clinic, the adolescent&rsquo;s own answer &middot; fictional</span><p>Bea, 16, has been on hemodialysis for two years. Her mother has finished donor evaluation and the program is ready. Bea is quiet through the whole consultation.</p><p>You ask her mother to step out for ten minutes. Bea tells you she is afraid of the medicines making her fat and that she has been skipping her phosphate binders for months. You do not postpone the transplant on that alone; you bring in the psychologist and the transplant pharmacist to start adherence work now, with Bea choosing the first goal.</p><p class="tc-scene-take"><b>What this shows.</b> The adolescent&rsquo;s assent is part of readiness. Time alone with the young person is how you learn what the plan has to solve.</p></div>
{{call:<ul><li>A febrile urinary tract infection in a child on the transplant pathway: review the bladder plan</li><li>Any suggestion of payment or pressure around a donor</li><li>A donor who wants to withdraw: protect the donor&rsquo;s privacy and reason</li><li>A new diagnosis of SRNS, aHUS or hyperoxaluria as the cause of kidney failure</li><li>A family told that a date depends on PhilHealth rather than on readiness</li></ul>}}
{{key:Write the readiness plan in domains, give each domain an owner, and bring the adolescent into the room for the parts that only the adolescent can answer.}}
{{fig:apn26_b}}
"""),
    ],
    "debrief": [
        "<p><strong>Not yet; the bladder first.</strong> Jerome is a reasonable transplant candidate, but not in five weeks. A small, thick-walled, high-pressure bladder that he catheterizes &ldquo;when I remember,&rdquo; with two febrile infections this year, would expose a new kidney to back-pressure and infection under immunosuppression. Ask the urologist for a plan now: a catheterization schedule Jerome can actually keep, with the nurse educator, and a decision on whether augmentation or another procedure is needed before transplant. Meanwhile, confirm the cause of kidney failure (valves, so recurrence is not the issue), complete his vaccines, and keep his peritoneal dialysis adequate. Tell his father honestly that a date set by Christmas would put the kidney at risk.</p>",
        "<p><strong>The aunt and the fee.</strong> Thank Tita Lorna and refer her to the transplant program&rsquo;s donor team, who will evaluate her own lifetime risk, separately from Jerome&rsquo;s care, and who will see her alone so that she can decline without explaining herself to the family. Under the KDIGO 2017 donor guideline, her whole risk profile is weighed, not a single test. To the father, say clearly and kindly that paying for a kidney is not permitted under DOH policy, which follows the Declaration of Istanbul and the anti-trafficking law, that you will not take part, and that it would endanger Jerome, the person paid, and the family. If he persists, involve the transplant program&rsquo;s ethics process. Ask also whether Jerome can be listed for a deceased-donor kidney.</p>",
        "<p><strong>The rest of the plan.</strong> Write Jerome&rsquo;s readiness plan by domain with an owner for each: urology and catheterization, vaccines, nutrition and bone, dialysis adequacy and an access plan in case of graft failure, adherence work with Jerome himself (time alone with him, his own goals), and psychosocial support for a family with a mother abroad. Check that the transplant facility is contracted for PhilHealth&rsquo;s KT Z benefit under PC 2024-0035, that its team includes a PNSP-certified pediatric nephrologist, and that Jerome is registered in the KT data registry, which PhilHealth Advisory 2026-0026 made mandatory. Make clear to the family that the benefit pays for the transplant; readiness decides the date.</p>",
    ],
    "skills": {"title": 'Preparing a child for kidney transplantation',
               "intro": "Complete with a preceptor, in simulation or at your own unit. Sign-off is local.",
               "items": [("Writes a domain-based transplant readiness plan with owners and dates", False),
                         ("Discusses a living-donor offer with a family, keeping the donor&rsquo;s evaluation separate", False),
                         ("Responds to a suggestion of a paid donor clearly and lawfully, in a simulated conversation", False),
                         ("Reviews a urodynamic report with a urologist and agrees a pre-transplant bladder plan", False)],
               "placement": "Simulation or supervised practice"},
    "quiz": [
        ("A 14-year-old with posterior urethral valves has a high-pressure bladder and recurrent febrile urinary tract infections (UTIs). A living donor is ready. What is the best next step?",
         ["Proceed with transplant; the bladder will adapt",
          "Settle a bladder management plan with the urologist before setting a date",
          "Defer transplant until age 18",
          "Remove both native kidneys first in every case"],
         1,
         "A high-pressure, poorly emptying bladder transmits pressure and infection to the graft. The bladder plan comes before the date."),
        ("What does DOH AO 2010-0018 say about non-directed living non-related donation?",
         ["It is permitted with payment through a registry",
          "It is permitted for children only",
          "It is not permitted",
          "It is permitted when PhilHealth approves"],
         2,
         "The order, aligned with the anti-trafficking law, the Declaration of Istanbul and WHO principles, does not permit non-directed living non-related donation."),
        ("Why does genetic testing matter before transplant in a child with steroid-resistant nephrotic syndrome?",
         ["It changes the immunosuppression dose",
          "It determines blood group compatibility",
          "It is required by PhilHealth",
          "A monogenic podocyte defect and a circulating factor carry different recurrence outlooks"],
         3,
         "IPNA reports a monogenic cause in 10&ndash;30% of SRNS. The donor kidney does not carry the child&rsquo;s podocyte defect, but a circulating factor can attack it."),
        ("How did the KDIGO 2017 living-donor guideline change donor evaluation?",
         ["It replaced single risk-factor cutoffs with a comprehensive assessment of the donor&rsquo;s whole risk profile",
          "It banned donation by relatives under 40",
          "It set fixed kidney function cutoffs for all countries",
          "It made all recommendations grade 1A"],
         0,
         "The guideline favors comprehensive, quantitative risk assessment and shared decision-making; many recommendations are ungraded expert opinion."),
        ("A family says the transplant date depends on when PhilHealth approves the Z benefit. What is the correct framing?",
         ["PhilHealth approval sets clinical readiness",
          "The benefit pays for the transplant under its conditions; clinical readiness decides the date",
          "Without PhilHealth, transplant is not allowed",
          "The benefit requires transplant within a fixed number of weeks"],
         1,
         "Coverage is not a clinical decision. Confirm benefit rules with the Z benefit coordinator on the date of service."),
    ],
    "terms": [("aHUS", "Atypical hemolytic uremic syndrome"), ("AO", "Administrative Order"),
              ("CAKUT", "Congenital anomalies of the kidney and urinary tract"), ("CI", "Confidence interval"),
              ("CKD", "Chronic kidney disease"), ("DOH", "Department of Health"),
              ("GRADE", "Grading of Recommendations Assessment, Development and Evaluation"),
              ("IPNA", "International Pediatric Nephrology Association"), ("KDIGO", "Kidney Disease: Improving Global Outcomes"),
              ("KT", "Kidney transplantation"), ("PC", "PhilHealth Circular"),
              ("PNSP", "Pediatric Nephrology Society of the Philippines"), ("RA", "Republic Act"),
              ("SRNS", "Steroid-resistant nephrotic syndrome"), ("UTI", "Urinary tract infection"), ("WHO", "World Health Organization")],
    "readings": [('kidney-transplant.html', 'Beyond Dialysis: Understanding Kidney Transplant'),
                 ('organ-donation-philippines.html', 'Organ & Kidney Donation in the Philippines: A Complete Patient & Family Guide'),
                 ('transplant-prehabilitation.html', 'Getting Fit for a Kidney Transplant: Prehabilitation, Nutrition and Recovery')],
    "calcs": ["calc-ckid-u25-egfr.html", "calc-pediatric-egfr.html", "calc-donor-esrd-risk.html",
              "calc-transplant-coordinator-toolkit.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
