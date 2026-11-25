# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 02: The renal consultation and the minimum dataset.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. KDIGO 2024 statements checked against the KDIGO 2024 summary of recommendations and practice points;
urinalysis and AKD figures against the PubMed records (Tsai 2005; ADQI 16, 2017)."""

MODULE = {'image_alt': 'A microscope with a urine sediment slide, a specimen cup and a centrifuge tube on a lab bench.',
 'objectives': ['Build a problem representation from creatinine trajectory, urine output and examination.',
                'Choose targeted urine, serologic and imaging studies by syndrome.',
                'Write a consult note that states urgency, the working diagnosis, alternatives and the owner of pending results.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the '
        'Philippine Society of Nephrology (PSN) guidelines, you perform a complete clinical assessment before hemodialysis is started '
        '(b2).[[an01_1]]</div>\n'
        '{{plain:Creatinine is like yesterday&rsquo;s bank balance. It tells you how much money is left, but it posts late, and it '
        'cannot tell you who has been spending or why.}}\n'
        '<p>The picture has a limit. A statement eventually catches up; creatinine catches up only when kidney function stops changing. '
        'And the urine shows what no balance can: where the injury lives.</p>\n'
        '{{cards:Key numbers|Acute kidney injury (AKI), KDIGO 2012::Creatinine rise &ge;0.3 mg/dL in 48 hours, or &ge;1.5 times baseline '
        'within 7 days, or urine output &lt;0.5 mL/kg/h for 6 hours|Acute kidney disease (AKD)::Kidney dysfunction lasting 7 to 90 days '
        '(ADQI consensus)|Fractional excretion of sodium (FENa)::&lt;1% off diuretics suggests avid sodium retention|Nephrotic-range '
        'proteinuria::&gt;3.5 g per day}}\n'
        '<p>Most referrals reach you as a text or a Viber message with one number in it. Your work in this module is to rebuild the '
        'timeline, read the urine yourself, and write a note that tells the next doctor what is happening, how urgent it is, and who owns '
        'each pending result.</p>\n',
 'case': {'title': 'The referral that arrived by text',
          'html': '<p>On Tuesday afternoon you are in your clinic when Nurse Cabral, head nurse at the dialysis center where several of '
                  'your patients dialyze, calls. A general practitioner has sent Mr. Reyes, 59, to the unit with a text: &ldquo;Pls accept '
                  'for HD, creatinine 2.5, edematous.&rdquo; You ask her to send him and his wife to your clinic instead.</p>\n'
                  '<p>His creatinine was 1.1 mg/dL ten days ago, on a result he keeps in his wallet. He has new ankle swelling, '
                  'cola-colored urine, and back pain for which he has been taking ibuprofen bought over the counter. His blood pressure '
                  'is 158/96 mm Hg. A urine sample taken in the clinic shows red cells, and when you look under the microscope yourself '
                  'you find dysmorphic red cells and one red-cell cast. While he is with you, Nurse Cabral texts: &ldquo;Doctor, should '
                  'we keep the 4 p.m. chair for him?&rdquo;</p>\n',
          'questions': ['Does he need dialysis today?',
                        'What does the urine tell you that the creatinine does not?',
                        'What will you write in your consult note, and who owns each pending result?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>Muscle makes creatinine at a roughly steady rate. When glomerular filtration rate (GFR) falls suddenly, production '
               'continues while removal drops, and the serum level climbs over 24 to 72 hours toward a new plateau. An early value '
               'underestimates the injury; during recovery the lag runs the other way.</p>\n'
               '<p>Location is read from the urine. Each finding traces back to a structure that failed:</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>Finding in the urine</th><th>What it means happened</th><th>Where the lesion sits</th></tr></thead>\n'
               '<tbody>\n'
               '<tr><td>Dysmorphic red cells, red-cell casts</td><td>Blood crossed a damaged glomerular capillary wall and set in the '
               'tubule</td><td>Glomerulus</td></tr>\n'
               '<tr><td>Muddy-brown granular casts, tubular epithelial cells</td><td>Injured tubular cells sloughed into the '
               'lumen</td><td>Tubule</td></tr>\n'
               '<tr><td>White-cell casts</td><td>Inflammatory cells collected in the tubule</td><td>Interstitium or kidney '
               'infection</td></tr>\n'
               '<tr><td>Bland sediment, high specific gravity, FENa &lt;1%</td><td>Tubules working hard to conserve salt</td><td>Usually '
               'reduced effective perfusion</td></tr>\n'
               '</tbody></table></div>\n'
               '<p>A low FENa is not specific: contrast injury, early obstruction and some glomerular diseases also hold sodium. Cystatin C '
               'depends less on muscle mass, so it estimates better after an amputation or in a frail older patient.</p>\n'
               '{{key:Creatinine tells you how much filtration is lost. The timeline, the kidney size and the sediment tell you why.}}\n'
               '<div class="tc-scene"><span class="tc-lab">In your clinic &middot; fictional</span><p>Two referrals arrive on the same '
               'afternoon, both &ldquo;creatinine 4.0.&rdquo; Mrs. Lim, 70, has small, bright kidneys on ultrasound and a creatinine of '
               '3.6 a year ago. Mr. Javier, 31, has normal-sized kidneys, a creatinine of 1.0 two months ago, and red-cell casts in his '
               'urine.</p><p>The same number describes two different diseases. For Mrs. Lim it is the next step on a long slope; for Mr. '
               'Javier it is an emergency that a biopsy may still reverse.</p><p class="tc-scene-take"><b>What this shows.</b> Ask for the '
               'old results first. In Philippine practice they are often in the patient&rsquo;s envelope or phone, not in any '
               'chart.</p></div>\n'
               '\n'
               '{{fig:an02_a}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Definitions.</strong> The AKI criteria come from the Kidney Disease: Improving Global '
               'Outcomes (KDIGO) 2012 guideline.[[an02_2]] The Acute Disease Quality '
               'Initiative (ADQI) consensus named the interval between AKI (7 days or less) and chronic kidney disease (CKD, more than 90 '
               'days) acute kidney disease, so that patients who have not recovered are not lost between the two labels.[[an02_7]] KDIGO has '
               'released a 2026 guideline for AKI and AKD as a public-review draft.[[an02_3]] Treat any draft statement as provisional until '
               'the final edition is published.</p>\n'
               '<p><strong>Estimating GFR.</strong> KDIGO 2024 advises using serum creatinine and an estimating equation for the initial '
               'assessment (practice point), using a validated equation (1D) without race in the computation (practice point), and the '
               'same equation within a region.[[an02_1]] The CKD Epidemiology Collaboration (CKD-EPI) 2021 creatinine equation is the '
               'race-free equation most laboratories now report.[[an02_4]] KDIGO 2024 recommends the combined creatinine and cystatin C '
               'estimate when the creatinine estimate is less accurate and GFR affects a decision (1C).[[an02_1]]</p>\n'
               '<p><strong>Reading the urine yourself.</strong> In a small single-center study of 26 patients with acute kidney failure, a '
               'nephrologist who examined the sediment personally identified the cause in 24 cases (92%). Diagnoses made from the '
               'hospital laboratory&rsquo;s urinalysis reports were correct in only 19% to 23%.[[an02_6]] It was small and from one center, so it suggests, '
               'rather than proves, that your own microscope changes the diagnosis.</p>\n'
               '<p>The KDIGO 2021 glomerular disease guideline defines the nephrotic range as proteinuria above 3.5 g per day.[[an02_5]]</p>\n'
               '{{key:Name the source behind each threshold. A definition, a graded recommendation, a practice point and a draft are four '
               'different levels of certainty.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p>Every consult note should answer five questions:</p>\n'
               '<ol><li>What was the baseline creatinine, and from what date?</li><li>Is this AKI, AKD or CKD?</li><li>Where is the lesion: '
               'prerenal, intrinsic (glomerular, tubular, interstitial, vascular) or postrenal?</li><li>How urgent is it, and which '
               'life-threatening complications are present now?</li><li>Who owns each pending result, and by when?</li></ol>\n'
               '<p>Examine the sediment yourself when intrinsic disease is possible; keep a centrifuge and a microscope in your clinic if '
               'you can. Quantify protein with a urine albumin-to-creatinine ratio (UACR) or protein-to-creatinine ratio (UPCR) rather than '
               'a 24-hour collection the patient may not manage. Order a kidney ultrasound early: size, echogenicity and hydronephrosis '
               'change the differential within minutes. Most patients pay for each test, so order first the tests that '
               'change the next decision.</p>\n'
               '\n'
               '{{fig:an02_b}}\n'
               '<div class="tc-scene"><span class="tc-lab">In the consult room &middot; fictional</span><p>You write Mr. Javier&rsquo;s '
               'note in five lines. Baseline: 1.0 mg/dL two months ago. Category: AKI. Lesion: glomerular, active sediment. Urgency: '
               'biopsy this week, admit if breathless or creatinine rises again. Owners: you follow the serologies by Friday; the general '
               'practitioner rechecks creatinine in 48 hours and sends you the result on Viber.</p><p>The next physician who opens his '
               'chart understands the plan in thirty seconds.</p><p class="tc-scene-take"><b>What this shows.</b> A consult note that '
               'answers the five questions is a handoff, not a diary.</p></div>\n'
               '{{key:A text that says &ldquo;for HD&rdquo; is a request, not a diagnosis. Your note turns it into one.}}\n'
               '{{call:<ul><li>Red-cell casts or dysmorphic red cells with rising creatinine</li><li>Hemoptysis, rash or purpura with '
               'AKI</li><li>Anuria (consider obstruction or a vascular event)</li><li>Bilateral small echogenic kidneys reframing '
               '&lsquo;AKI&rsquo; as advanced CKD</li></ul>}}\n')],
 'debrief': ['<p><strong>Does he need dialysis today?</strong> Not on what you have so far. A creatinine of 2.5 mg/dL is not an '
             'indication. Look for the things that would make it one: potassium, bicarbonate, breathlessness, and urine output. If none is '
             'present, the free chair is not the right next step. The right next step is a diagnosis.</p>\n'
             '<p><strong>What does the urine say?</strong> Ibuprofen can injure the kidney through blood flow or through interstitial '
             'nephritis, but it does not make red-cell casts. Dysmorphic red cells and a cast mean blood crossed an inflamed glomerulus, '
             'and a creatinine that more than doubled in ten days makes this a rapidly progressive glomerulonephritis until proven '
             'otherwise. Stop the ibuprofen. Send antineutrophil cytoplasmic antibodies, anti-glomerular basement membrane antibodies, C3 '
             'and C4, and hepatitis B, hepatitis C, and HIV serologies. Quantify protein with a protein-to-creatinine ratio and order a '
             'kidney ultrasound.</p>\n'
             '<p><strong>The note.</strong> Answer the five questions: baseline and its date, AKI rather than CKD, a glomerular lesion, '
             'the urgency (biopsy within days, and admission if he becomes breathless or the creatinine keeps climbing), and who follows '
             'each result by when. Tell Nurse Cabral why you are not booking the chair, and that you are not turning him away.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Reconstructs the baseline with dates', False),
                      ('Personally interprets the urine sediment', False),
                      ('Classifies AKI, AKD or CKD and localizes the lesion', False),
                      ('Writes urgency, plan and result ownership', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('Which finding most strengthens a glomerular explanation?',
           ['NSAID exposure alone', 'Dysmorphic erythrocytes and red-cell casts', 'An isolated creatinine result', 'A FENa of 2%'],
           1,
           'Sediment morphology places the injury at the glomerular capillary wall in a way creatinine cannot.'),
          ('Which data clarify whether a creatinine change is acute?',
           ['A dated baseline and a serial trajectory',
            'The oldest available blood pressure only',
            'An isolated assessment of edema',
            'A single cystatin C value'],
           0,
           'Change over time classifies acuity and gauges progression. Ask for the results the patient keeps at home.'),
          ('Why does a single creatinine underestimate injury early in AKI?',
           ['Muscle mass increases during illness',
            'Creatinine is secreted only during sleep',
            'The laboratory assay saturates',
            'Creatinine takes 24–72 hours to reach a new steady state after GFR falls'],
           3,
           'Production continues while filtration falls, so the serum level rises gradually toward the new equilibrium.'),
          ('In which patient is cystatin C most useful for estimating GFR?',
           ['A patient with normal creatinine and no symptoms',
            'A well-nourished adult of average build with stable creatinine',
            'A bilateral above-knee amputee with low muscle mass',
            'Any patient on dialysis'],
           2,
           'Cystatin C depends less on muscle mass, so it corrects the overestimate of GFR from creatinine when muscle is low. KDIGO '
           '2024 recommends the combined estimate when the creatinine estimate is less accurate and GFR affects a decision (1C).'),
          ('Muddy-brown granular casts most strongly suggest:',
           ['Minimal change disease', 'Acute tubular injury', 'Prerenal azotemia with intact tubules', 'Postrenal obstruction'],
           1,
           'Sloughed tubular epithelial cells form granular casts; prerenal states typically show a bland sediment.')],
 'terms': [('FENa', 'Fractional excretion of sodium'),
           ('AKI', 'Acute kidney injury'),
           ('AKD', 'Acute kidney disease'),
           ('ADQI', 'Acute Disease Quality Initiative'),
           ('CKD', 'Chronic kidney disease'),
           ('CKD-EPI', 'Chronic Kidney Disease Epidemiology Collaboration'),
           ('GFR', 'Glomerular filtration rate'),
           ('UACR', 'Urine albumin-to-creatinine ratio'),
           ('UPCR', 'Urine protein-to-creatinine ratio'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('NSAID', 'Nonsteroidal anti-inflammatory drug')],
 'readings': [('hematuria-blood-in-urine.html', 'Red Alert: Blood in Your Urine'),
              ('unlocking-urine-electrolytes-clinician.html', 'Unlocking Urine Electrolytes: A Practical Clinician Guide')],
 'calcs': ['calc-egfr-ckd-epi.html',
           'calc-egfr-cystatin.html',
           'calc-fena-feurea.html',
           'calc-aki-staging.html',
           'calc-urine-protein-excretion.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
