# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 05: AKI and post-AKI care.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. Figures checked against the PubMed abstracts (BICARICU-2, SMART), the KDIGO 2012 AKI guideline, and the
2010 Philippine leptospirosis guideline (dialysis chapter and PhilHealth policy summary)."""

MODULE = {'image_alt': 'A farmer walks along a path between flooded rice paddies toward a barangay health station.',
 'objectives': ['Stage acute kidney injury (AKI) from creatinine and urine-output trends and identify reversible causes in parallel.',
                'Manage leptospirosis-associated AKI in the Philippine context.',
                'Write a post-AKI follow-up plan with named labs, timing and owner.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the '
        'Philippine Society of Nephrology (PSN) guidelines, you coordinate with the nurses and the physician on duty in emergencies (b8), '
        'endorse properly when your patient is admitted under another nephrologist (b12), and plan long-term care with the patient '
        '(b9).[[an01_1]]</div>\n'
        '{{plain:Think of acute kidney injury (AKI) as a fever of the kidney. A fever tells you something is wrong; it does not tell you '
        'what. You bring it down while you look for the cause.}}\n'
        '<p>The picture has a limit. A fever leaves no trace; AKI often does. An injured kidney can recover its creatinine and still '
        'carry a scar that raises the risk of chronic kidney disease (CKD) years later. So AKI has a third job: follow the kidney after '
        'it seems to have recovered.</p>\n'
        '{{cards:Key numbers|Stage 1 (KDIGO 2012)::Creatinine 1.5&ndash;1.9 times baseline or a rise of &ge;0.3 mg/dL; urine output '
        '(UO) &lt;0.5 mL/kg/h for 6&ndash;12 h|Stage 2::Creatinine 2.0&ndash;2.9 times baseline; UO &lt;0.5 mL/kg/h for &ge;12 h|Stage '
        '3::Creatinine &ge;3 times baseline, or &ge;4.0 mg/dL, or kidney replacement therapy (KRT) started; UO &lt;0.3 mL/kg/h for &ge;24 h '
        'or anuria &ge;12 h|BICARICU-2, 90-day mortality::62.1% with bicarbonate vs 61.7% without|Post-AKI review::Kidney function and '
        'urine albumin at about 3 months}}\n'
        '<p>Most AKI reaches you by phone or Viber from someone else&rsquo;s hospital. Your work is to stage it from the trend, start what '
        'cannot wait, decide where the patient is safest, and make sure someone owns the follow-up.</p>\n',
 'case': {'title': 'The flood patient sent for dialysis',
          'html': '<p>It is the third day after a typhoon. At 7 a.m. a doctor at a provincial hospital calls your mobile phone. He wants to '
                  'transfer Mr. Gatdula, 34, a construction worker who waded through floodwater five days ago. He has fever, calf pain, and '
                  'yellow eyes. His platelets are 48,000/&micro;L, creatinine 4.6 mg/dL, and potassium 3.2 mmol/L. After fluids his mean '
                  'arterial pressure is 70, but his urine output is only 0.3 mL/kg an hour.</p>\n'
                  '<p>The referring doctor says, &ldquo;His potassium is low, so he does not need dialysis yet. Can you just see him in your '
                  'clinic next week?&rdquo; Your head nurse messages that the unit is already full, because patients from a flooded satellite '
                  'unit have been added to every shift.</p>\n',
          'questions': ['What is your working diagnosis, and what should start now?',
                        'Does a low potassium mean dialysis can wait?',
                        'Where should he be treated, given that your unit is full?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>The kidneys receive about a fifth of the cardiac output, yet the medulla runs near hypoxia, because the thick ascending '
               'limb pumps sodium hard on a sparse blood supply. Low pressure, sepsis, nephrotoxins and venous congestion push it past its '
               'margin.</p>\n'
               '<p>Congestion is the cause most often treated with the wrong fluid. A high central venous pressure narrows the '
               'arterial-venous gradient that drives renal blood flow and raises pressure inside a capsule that cannot stretch. More fluid '
               'then lowers perfusion.</p>\n'
               '<p>Injured tubular cells can arrest in the G2/M phase of the cell cycle and secrete profibrotic signals, a proposed '
               'mechanism for the later CKD.</p>\n'
               '<p>Leptospirosis, endemic after Philippine floods, injures the proximal tubule and thick ascending limb, so the kidney wastes '
               'sodium and potassium. The result is often a non-oliguric AKI with a low potassium, which the 2010 Philippine guideline names '
               'as a recognized feature.[[an05_5]] Severe disease (Weil syndrome) adds jaundice, low platelets and pulmonary '
               'hemorrhage.</p>\n'
               '{{key:A low potassium in leptospirosis is the kidney&rsquo;s injury showing, not the kidney coping.}}\n'
               '<div class="tc-scene"><span class="tc-lab">By Viber, from a partner hospital &middot; fictional</span><p>Mrs. Uy has AKI '
               'after pneumonia. Over two days she has received 7 liters of fluid. Her urine output has not risen, her neck veins are '
               'full, and her oxygen requirement is climbing. The internist of record messages you: &ldquo;One more liter?&rdquo;</p><p>You '
               'call back: the high venous pressure and a swollen, encapsulated kidney mean more fluid is now making perfusion worse.</p><p class="tc-scene-take"><b>What '
               'this shows.</b> Euvolemia, not maximum fluid, is the target in AKI.</p></div>\n'
               '\n'
               '{{fig:an05_a}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Definition.</strong> The Kidney Disease: Improving Global Outcomes (KDIGO) 2012 guideline, still the current '
               'final version, stages AKI by creatinine and urine output.[[an05_1]] The KDIGO 2026 draft, still in public review, adds '
               'structural biomarkers and follow-up; until it is final, quote the 2012 grades.[[an05_2]]</p>\n'
               '<p><strong>Fluids.</strong> SMART randomized 15,802 adults in five intensive care units (ICUs) to balanced crystalloids or '
               'saline. Death, new KRT or persistent kidney dysfunction at 30 days occurred in 14.3% versus 15.4%, about 1 percentage point; '
               'no single component differed significantly.[[an05_6]] A modest, single-center result, but it favors balanced fluid.</p>\n'
               '<p><strong>Bicarbonate.</strong> BICARICU-2 randomized 640 patients in 43 French ICUs with pH &le;7.20 and moderate to severe '
               'AKI. Day-90 mortality was 62.1% with bicarbonate and 61.7% without. Less KRT (35% versus 50%) was one of 18 secondary '
               'outcomes, so it is hypothesis-generating.[[an05_4]]</p>\n'
               '<p><strong>Leptospirosis.</strong> The 2010 Philippine guideline, developed by the infectious disease, nephrology and chest '
               'societies, recommends antibiotics as soon as leptospirosis is suspected (Grade B): penicillin G first line in moderate to '
               'severe disease, ceftriaxone an alternative, doxycycline in mild disease. Any one of these indicates dialysis (Grade A): '
               'uremic symptoms, creatinine above 3 mg/dL, potassium above 5 mEq/L with oliguria, lung involvement, pH below 7.2, fluid '
               'overload, or oliguria despite resuscitation. Hemodialysis is preferred; peritoneal dialysis is acceptable when it is not '
               'available.[[an05_5]] These grades are the guideline&rsquo;s own scale, not KDIGO&rsquo;s, and the dialysis evidence is '
               'largely observational.[[an05_3]]</p>\n'
               '<p><strong>After discharge.</strong> KDIGO 2012 advises evaluating patients about 3 months after AKI for recovery, new CKD, '
               'or worsening of existing CKD (ungraded).[[an05_1]]</p>\n'
               '{{key:Quote the grade with its source. A Grade A in the Philippine leptospirosis guideline and a 1A in KDIGO come from '
               'different systems.}}\n' '\n{{fig:an05_fig_aki_evidence_fluids_bicarbonate_lepto}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Work in parallel.</strong> Check perfusion, obstruction and intrinsic disease together. Stop nephrotoxins, adjust '
               'doses, and aim for euvolemia.</p>\n'
               '<p><strong>Think leptospirosis early.</strong> After flood or animal exposure with fever, myalgia, conjunctival suffusion, '
               'jaundice or low platelets, ask for antibiotics now, without waiting for serology, and watch potassium and the lungs.</p>\n'
               '<p><strong>Decide where the patient is safest.</strong> A freestanding unit is not the place for jaundice, low platelets and '
               'a risk of lung bleeding. Find a hospital that can dialyze him today, speak to the accepting doctor, and send a written '
               'endorsement.</p>\n'
               '<p><strong>Own the follow-up.</strong> At discharge, the summary should name the AKI stage, the peak and discharge '
               'creatinine, the medicine changes, and who checks creatinine and urine albumin at about 3 months. That check usually happens '
               'in your private clinic at the patient&rsquo;s expense, so book it before he leaves and copy the plan to the referring '
               'doctor.</p>\n'
               '\n'
               '{{fig:an05_b}}\n'
               '<div class="tc-scene"><span class="tc-lab">In your clinic, a forgotten patient &middot; fictional</span><p>Three months '
               'after a dialysis-requiring AKI, Mr. Ferrer comes to your clinic only because his pharmacist told him to. His discharge summary '
               'lists no stage, no follow-up, and no medicine changes. His creatinine is 1.8 mg/dL, and his baseline was 1.0.</p><p>You '
               'record the AKI stage, check his urine albumin, review his medicines, and book him into your CKD follow-up.</p><p '
               'class="tc-scene-take"><b>What this shows.</b> AKI survivors carry a higher risk of later CKD. A named follow-up owner is part '
               'of the treatment.</p></div>\n'
               '{{key:Every AKI discharge needs a stage, a date, a test and a name. If no one else writes them, you do.}}\n'
               '{{call:<ul><li>Oliguria persisting after perfusion is restored</li><li>Leptospirosis with hemoptysis or falling oxygen '
               'saturation (pulmonary hemorrhage)</li><li>Potassium &ge;6.5 mmol/L or electrocardiogram (ECG) changes</li><li>Fluid overload '
               'with rising oxygen requirement</li></ul>}}\n')],
 'debrief': ['<p><strong>The diagnosis.</strong> This is severe leptospirosis, Weil syndrome, with stage 3 AKI. Ask the referring doctor '
             'to start intravenous penicillin G, or ceftriaxone, now, without waiting for serology.</p>\n'
             '<p><strong>Can dialysis wait?</strong> No. Leptospiral injury wastes potassium, so a low value is expected and does not mean '
             'the kidney is coping. His creatinine is above 3 mg/dL and he is oliguric after resuscitation; each is an indication for '
             'dialysis in the 2010 Philippine guideline. Replace potassium cautiously, avoid excess fluid, and watch his oxygen saturation: '
             'pulmonary hemorrhage is the complication that kills.</p>\n'
             '<p><strong>Where?</strong> He needs a hospital bed with monitoring and a temporary dialysis catheter, not a clinic chair next '
             'week and not a full freestanding unit. Confirm acceptance with a named doctor at a hospital that can dialyze him today, send a '
             'short endorsement, and offer him a three-month slot in your clinic.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Stages AKI from trends', False),
                      ('Works up perfusion, obstruction and intrinsic causes in parallel', False),
                      ('Identifies leptospirosis features and starts antibiotics', False),
                      ('Drafts a post-AKI plan with named labs and owner', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('What should determine the next step after initial stabilization?',
           ['Creatinine alone',
            'Serial perfusion, urine output, chemistry and complications',
            'Flood exposure alone',
            'The admitting diagnosis code'],
           1,
           'The trend in physiology and complications sets the urgency while the cause is worked up.'),
          ('What belongs in the post-AKI discharge plan?',
           ['Residual dysfunction, medication changes and named lab follow-up',
            'An AKI code alone',
            'A direction to repeat testing without an owner',
            'Permanent avoidance of all antihypertensives'],
           0,
           'The next clinician needs a defined action, a time frame and a name. KDIGO advises review at about 3 months.'),
          ('Which electrolyte pattern is characteristic of early leptospirosis-associated AKI?',
           ['Isolated hyperphosphatemia',
            'Hyperkalemia with hypercalcemia',
            'Hypernatremia with polyuria from diabetes insipidus only',
            'Non-oliguric AKI with hypokalemia from tubular potassium wasting'],
           3,
           'Leptospiral injury to the proximal tubule and thick ascending limb wastes sodium and potassium.'),
          ('What did BICARICU-2 show in severe metabolic acidemia with moderate to severe AKI?',
           ['Higher mortality with bicarbonate',
            'A 30% mortality reduction',
            'No difference in 90-day mortality; less frequent KRT in the bicarbonate group as a secondary finding',
            'Faster kidney recovery in all patients'],
           2,
           'The primary outcome was neutral (62.1% vs 61.7%). The KRT finding was one of 18 secondary outcomes.'),
          ('Why does venous congestion worsen AKI?',
           ['It increases glomerular filtration',
            'It lowers the transrenal perfusion gradient and raises pressure inside the encapsulated kidney',
            'It dilates the afferent arteriole',
            'It lowers renal interstitial pressure'],
           1,
           'Perfusion depends on arterial minus venous pressure; a tense, encapsulated kidney compounds the drop.')],
 'terms': [('AKI', 'Acute kidney injury'),
           ('CKD', 'Chronic kidney disease'),
           ('TAL', 'Thick ascending limb'),
           ('UO', 'Urine output'),
           ('UACR', 'Urine albumin-to-creatinine ratio'),
           ('ICU', 'Intensive care unit'),
           ('ECG', 'Electrocardiogram'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('KRT', 'Kidney replacement therapy')],
 'readings': [('aki-does-not-end-at-discharge.html', 'AKI Does Not End at Discharge: 90-Day Recovery Guide'),
              ('leptospirosis-nephropathy.html', 'Leptospirosis After Flood Exposure: Symptoms, Kidney Warning Signs & What To Do')],
 'calcs': ['calc-aki-staging.html', 'calc-fena-feurea.html', 'calc-leptospirosis-aki-risk.html', 'calc-post-aki-followup.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
