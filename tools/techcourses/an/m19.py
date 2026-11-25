# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 19: Transplant referral and shared follow-up.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. Registry figures checked against the PubMed abstract (Wolfe 1999); KDIGO 2020 referral statements and
the KDIGO 2024 practice point checked against the guideline texts."""

MODULE = {'image_alt': 'A transplanted kidney in the lower right abdomen, connected to the iliac vessels and the bladder.',
 'objectives': ['Refer suitable patients early with a complete, actionable dataset.',
                'Explain living- and deceased-donor pathways and independent donor assessment.',
                'Triage graft dysfunction and coordinate immunosuppression changes with the transplant team.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the '
        'Philippine Society of Nephrology (PSN) guidelines, long-term medical planning with the patient (b9) includes a timely transplant '
        'referral.[[an01_1]]</div>\n'
        '{{plain:Think of a transplant referral as getting in line at a government office with a long queue and a long checklist. The '
        'earlier you take a number, and the more complete the papers you bring, the sooner you reach the window.}}\n'
        '<p>The picture has a limit. A queue moves in order; a transplant program does not. The program decides, with its own team and its '
        'own work-up, whether and when a patient is ready, and a living donor goes through a separate evaluation of their own. What the '
        'picture gets right is time: the commonest reason a suitable patient is never transplanted is that the referral came late or came '
        'incomplete.</p>\n'
        '{{cards:Key numbers|Referral timing (KDIGO 2020)::At least 6&ndash;12 months before expected dialysis; consider everyone with '
        'estimated glomerular filtration rate (eGFR) &lt;30 expected to reach kidney failure|Kidney Failure Risk Equation (KFRE) 2-year risk '
        '&gt;40%::Can be used to time education on kidney replacement options (KDIGO 2024, practice point)|Registry comparison (Wolfe '
        '1999)::Long-term mortality 48%&ndash;82% lower after transplant than on the waiting list (observational)}}\n'
        '<p>In the Philippines the transplant itself happens at a transplant center, with its own nephrologists, surgeons, and coordinators. '
        'You refer, you help prepare the patient and the family, and after the transplant you often share follow-up with the center from '
        'your clinic or dialysis unit. Your work in this module is to refer early with papers the center can act on, and to recognize the '
        'graft emergencies you must hand back to the center the same day.</p>\n',
 'case': {'title': 'The clarithromycin from the corner clinic',
          'html': '<p>Mrs. Ramos, 46, dialyzed at your unit for three years before a living-donor transplant five months ago at a '
                  'transplant center in Manila. She still visits your clinic for blood pressure and shared follow-up with the center.</p>\n'
                  '<p>Today she comes in with a fever of 38.3 &deg;C. Her creatinine, 1.2 mg/dL last month, is now 1.9. Her urine output has '
                  'dropped a little. Ten days ago a clinic near her home started clarithromycin for bronchitis. She takes tacrolimus, '
                  'mycophenolate, and prednisone. Your clinic nurse asks whether to schedule her for a session &ldquo;since her kidney is '
                  'going down.&rdquo;</p>\n',
          'questions': ['What could be causing the creatinine rise?',
                        'Which of these causes did a single prescription create?',
                        'What do you do today, and what must you not do on your own?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>A working transplant restores what dialysis only imitates: continuous filtration, steady salt and water balance, and the '
               'hormones a kidney makes, erythropoietin and calcitriol. That is the physiologic reason transplant recipients usually feel and '
               'function better than they did on dialysis.</p>\n'
               '<p>The graft is foreign tissue. Recipient T cells recognize the donor&rsquo;s human leukocyte antigens (HLA) and attack the '
               'tubules and vessels. Donor-specific antibodies injure the graft&rsquo;s capillaries. Immunosuppression keeps both in '
               'check.</p>\n'
               '<p>Calcineurin inhibitors such as tacrolimus block T-cell activation, but they also constrict the afferent arteriole, so high '
               'levels lower filtration and, over time, scar the graft. The liver and gut clear tacrolimus through the enzyme cytochrome P450 '
               '3A4 (CYP3A4). Drugs that inhibit this enzyme raise tacrolimus levels; drugs that induce it lower them.</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>What the other prescriber gives</th><th>Effect on CYP3A4</th><th>Tacrolimus level</th><th>What you may see</th></tr></thead>\n'
               '<tbody>\n'
               '<tr><td>Clarithromycin, erythromycin, azole antifungals, diltiazem, verapamil; grapefruit or pomelo</td><td>Inhibits</td>'
               '<td>Rises</td><td>Rising creatinine, tremor, high potassium</td></tr>\n'
               '<tr><td>Rifampicin, phenytoin, carbamazepine</td><td>Induces</td><td>Falls</td><td>Rising creatinine from rejection, weeks '
               'later</td></tr>\n'
               '</tbody></table></div>\n'
               '{{key:Every new prescription for a transplant recipient is a tacrolimus decision. Ask what was started, by whom, and when.}}\n'
               '<div class="tc-scene"><span class="tc-lab">In the clinic, the pomelo question &middot; fictional</span><p>Mrs. Ramos asks '
               'whether she can eat pomelo. Her neighbor said it is &ldquo;good for the kidneys.&rdquo;</p><p>You explain that pomelo, like '
               'grapefruit, can block the enzyme that breaks down tacrolimus. Her levels could rise and injure the new kidney. She asks you '
               'to write it on her medicine card.</p><p class="tc-scene-take"><b>What this shows.</b> Transplant medicines interact with '
               'food as well as drugs. Ask about both.</p></div>\n'
               '\n'
               '{{fig:an19_a}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Why refer.</strong> No randomized trial compares transplantation with staying on dialysis, so the evidence is '
               'observational. The clearest design compares transplant recipients with patients on the same waiting list, who have already '
               'passed the same selection. In a United States Renal Data System cohort of 228,552 dialysis patients, 46,164 waitlisted and '
               '23,275 transplanted, the risk of death was higher in the first two weeks after surgery but fell below the waiting-list risk '
               'by 18 months (relative risk 0.32). Long-term mortality was 48% to 82% lower after transplant (3.8 versus 6.3 deaths per 100 '
               'patient-years).[[an19_5]] Waitlisting itself selects healthier patients, so these figures describe suitable candidates, not '
               'everyone on dialysis.</p>\n'
               '<p><strong>When to refer.</strong> The Kidney Disease: Improving Global Outcomes (KDIGO) 2020 guideline on transplant '
               'candidates says patients with CKD G4&ndash;G5 (glomerular filtration rate below 30) who are expected to reach kidney failure '
               'should be informed about, educated about, and considered for transplantation. It advises referral at least 6 to 12 months '
               'before dialysis is expected to start, and names pre-emptive transplantation from a living donor as the preferred treatment for '
               'eligible patients.[[an19_1]] Separately, KDIGO 2024 lets a 2-year KFRE above 40% time education about kidney replacement '
               'options, which includes transplant; that is a practice point, not a graded recommendation.[[an09_1]]</p>\n'
               '<p><strong>Coverage.</strong> In the Philippines, kidney transplantation and post-transplant care are covered by '
               'Philippine Health Insurance Corporation (PhilHealth) Z Benefits packages through accredited centers.[[an19_2]][[an19_3]] The '
               'packages are revised from time to time; check the current circulars before you counsel a family about cost.[[an19_4]] For many '
               'families, the donor work-up, travel to the center, and the first year of medicines still cost more than the package '
               'covers.</p>\n'
               '{{key:Transplantation is associated with much longer survival in suitable patients. A late referral costs the patient the '
               'chance of a pre-emptive transplant.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Refer early, and send papers the center can act on.</strong> Raise transplant once eGFR is below 30 and falling, '
               'and refer at least 6 to 12 months before you expect dialysis. Write a referral letter with the cause of kidney disease (with '
               'biopsy, if any), the eGFR trajectory, comorbidities, cancer screening, infection serologies, sensitizing events (transfusions, '
               'pregnancies, prior grafts), and the barriers you can help address. Many of your hemodialysis patients were never referred; '
               'review your panel at least once a year.</p>\n'
               '<p><strong>Prepare the family.</strong> In Philippine practice the family usually discusses donation together, often with '
               'relatives abroad. Explain that a potential living donor is evaluated separately by the transplant center, with an advocate of '
               'their own, and that the donor&rsquo;s choice must be free. Point the family to the PhilHealth package and the center&rsquo;s '
               'social worker early, before cost becomes the reason to stop.[[an19_2]]</p>\n'
               '<p><strong>Share follow-up, and know where your role ends.</strong> After transplant, you may see the patient between center '
               'visits. Review adherence, drug interactions, infection, blood pressure, and the creatinine trend. For fever, a rising '
               'creatinine, or falling urine output, call the transplant team the same day. Do not change immunosuppression on your own; agree '
               'with the center who adjusts doses and who follows the levels. Tell the referring internist and every other prescriber to '
               'check interactions before starting anything new.</p>\n'
               '\n'
               '{{fig:an19_b}}\n'
               '<div class="tc-scene"><span class="tc-lab">Your panel, a census check &middot; fictional</span><p>You review your 40 '
               'hemodialysis patients for transplant referral. Eleven are under 60 and have no clear contraindication. Only three have ever '
               'been referred.</p><p>You write eight referral letters that month, each with the cause of kidney disease, serologies, '
               'transfusion history, and the barriers you can help with.</p><p class="tc-scene-take"><b>What this shows.</b> The commonest '
               'reason a suitable patient is not transplanted is that nobody referred them.</p></div>\n'
               '{{key:You refer, prepare, and watch. The transplant center decides candidacy and changes immunosuppression.}}\n'
               '{{call:<ul><li>Creatinine rise &gt;20&ndash;25% from the graft&rsquo;s baseline (a common clinical trigger; follow your '
               'center&rsquo;s threshold)</li><li>Fever in the first year after transplant</li><li>New interacting drug started by another '
               'prescriber</li><li>Missed immunosuppressant doses</li></ul>}}\n')],
 'debrief': ['<p><strong>Possible causes.</strong> Several may be present at once: tacrolimus toxicity, infection (urinary sepsis, '
             'cytomegalovirus [CMV], or BK virus), acute rejection, or obstruction. A 58% rise in creatinine with a fever five months after '
             'transplant needs all of them considered.</p>\n'
             '<p><strong>The prescription.</strong> Tacrolimus is broken down by CYP3A4. Clarithromycin blocks that enzyme, so tacrolimus '
             'levels can climb. High tacrolimus constricts the afferent arteriole and injures the graft. The interaction is well established '
             'and predictable, which is why it is preventable.</p>\n'
             '<p><strong>Today.</strong> Check whether she is stable. Send a tacrolimus trough level, blood and urine cultures, CMV and BK '
             'polymerase chain reaction (PCR) tests where available, a urinalysis, and a graft ultrasound. Replace clarithromycin with an '
             'antibiotic that does not interact. Call the transplant team today and agree with them who adjusts immunosuppression and who '
             'follows the levels. Do not change her tacrolimus, mycophenolate, or prednisone on your own. Dialysis is not the question today; '
             'finding the cause is.</p>\n'
             '<p><strong>Afterwards.</strong> Give her a wallet card that lists her immunosuppressants and says &ldquo;check interactions '
             'before prescribing,&rdquo; and ask her to show it at every clinic and pharmacy she visits. Write a short note to the clinic near '
             'her home.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Writes a transplant referral with a complete dataset', False),
                      ('Identifies urgent graft red flags', False),
                      ('Confirms transplant-service acceptance and the monitoring plan', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('What should guide immunosuppression changes in a febrile recipient with rising creatinine?',
           ['An automatic stop of all agents',
            'Urgent transplant-team coordination with evaluation of competing causes',
            'A routine review several weeks later',
            'Doubling the tacrolimus dose'],
           1,
           'Several high-risk causes can coexist, and changes made without the transplant team may worsen outcomes.'),
          ('Which information improves a transplant referral?',
           ['Cause and trajectory, comorbidity, sensitizing events and barriers the team can address',
            'A referral urgency label alone',
            'A guarantee of transplant acceptance',
            'Only the latest creatinine'],
           0,
           'The center can prioritize and coordinate a complete evaluation.'),
          ('Clarithromycin raises tacrolimus levels by:',
           ['Enhancing renal excretion',
            'Increasing tacrolimus absorption via P-glycoprotein induction',
            'Displacing it from albumin only',
            'Inhibiting CYP3A4 metabolism'],
           3,
           'CYP3A4 inhibition reduces clearance, raising levels and the risk of nephrotoxicity.'),
          ('When does KDIGO 2020 advise referral for transplant evaluation?',
           ['When eGFR falls below 5',
            'Only after 1 year of dialysis',
            'At least 6–12 months before anticipated dialysis, considering everyone with eGFR &lt;30 expected to reach kidney failure',
            'At chronic kidney disease (CKD) diagnosis regardless of trajectory'],
           2,
           'Early referral makes pre-emptive transplantation possible.'),
          ('Why is a living donor evaluated by an independent team?',
           ['To speed the recipient&rsquo;s surgery',
            'To protect donor safety and ensure the decision is voluntary',
            'Because the recipient&rsquo;s nephrologist cannot read donor labs',
            'To avoid PhilHealth paperwork'],
           1,
           'Separating donor advocacy from recipient care avoids conflicts of interest.')],
 'terms': [('CYP3A4', 'Cytochrome P450 3A4'),
           ('eGFR', 'Estimated glomerular filtration rate'),
           ('BP', 'Blood pressure'),
           ('HLA', 'Human leukocyte antigen'),
           ('KFRE', 'Kidney Failure Risk Equation'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('CMV', 'Cytomegalovirus'),
           ('PCR', 'Polymerase chain reaction'),
           ('PSN', 'Philippine Society of Nephrology'),
           ('PhilHealth', 'Philippine Health Insurance Corporation')],
 'readings': [('kidney-transplant.html', 'Beyond Dialysis: Understanding Kidney Transplant')],
 'calcs': ['calc-tacrolimus-dosing.html',
           'calc-allograft-egfr-trend.html',
           'calc-epts.html',
           'calc-kdpi-kdri.html',
           'calc-dgf-risk.html',
           'calc-donor-esrd-risk.html',
           'calc-drug-interaction-checker.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
