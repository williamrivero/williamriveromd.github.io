# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 16: Vascular access and access infection.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. LOCK IT-100 checked against the PubMed abstract; catheter-removal indications against the IDSA 2009
guideline; tunneled catheter path matches the locked anatomy (right internal jugular, chest exit, cuff in tunnel, tip in the
right atrium)."""

MODULE = {'image_alt': 'A three-dimensional forearm showing an arteriovenous fistula joining the radial artery to an enlarged vein.',
 'objectives': ['Create a patient-specific access life-plan.',
                'Recognize and escalate access emergencies and catheter-related bloodstream infection.',
                'Lead catheter-reduction and infection-surveillance practice.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the Philippine '
        'Society of Nephrology (PSN) guidelines, you coordinate with a vascular surgeon or a trained general surgeon on access provision '
        'and care (b3), and you coordinate in emergencies (b8).[[an16_3]]</div>\n'
        '{{plain:A catheter is a temporary bridge. It gets people across today, but the longer the town relies on it, the more likely it '
        'is to fail on a busy day.}}\n'
        '<p>The picture has a limit. A bridge wears evenly, and a catheter does not. Within days its surface grows a biofilm, and every '
        'catheter-day adds risk. The fistula takes months to build, so the bridge needs a date for the real one.</p>\n'
        '{{cards:Key numbers|LOCK IT-100, taurolidine&ndash;heparin lock::Catheter-related bloodstream infection (CRBSI) 2% vs 8% of '
        'patients; 0.13 vs 0.46 per 1,000 catheter-days|Surveillance metric::Bloodstream infections per 1,000 catheter-days, not raw '
        'counts}}\n'
        '<p>Many Filipino patients start on a catheter and stay on it while surgery waits for money or a surgeon. Your work is to give '
        'each an access plan with a surgeon and a date, and to act fast when a catheter becomes a source of sepsis.</p>\n',
 'case': {'title': 'Rigors at 30 minutes',
          'html': '<p>Mr. Domingo, 49, has dialyzed through a tunneled right internal jugular catheter for seven months. His fistula '
                  'surgery was postponed twice, once for cost and once for the surgeon&rsquo;s schedule. Thirty minutes into his Friday '
                  'session he starts shaking uncontrollably. His temperature is 39.2 &deg;C and his blood pressure falls to 82/50 mm '
                  'Hg.</p>\n'
                  '<p>Dr. Salonga, the physician on duty, calls you. &ldquo;Doc, he had the same thing last month. Blood culture grew '
                  '<em>Staphylococcus aureus</em>, and they gave him antibiotics through the catheter. Should I give paracetamol and '
                  'finish the session?&rdquo; Your head nurse adds that this is the unit&rsquo;s third catheter bloodstream infection this '
                  'quarter.</p>\n',
          'questions': ['What should Dr. Salonga do now?',
                        'Should the catheter stay?',
                        'What does the third infection this quarter tell you, and what will you do about it?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p><strong>The fistula.</strong> Joining an artery to a vein raises flow in the vein. The shear stress dilates it and '
               'thickens its wall until it can take needles. Neointimal hyperplasia at the swing segment or the outflow narrows it, and '
               'that shows as high venous pressure, prolonged bleeding or poor flow.</p>\n'
               '<p><strong>The tunneled catheter.</strong> It enters the right internal jugular vein low in the neck, curves over the '
               'clavicle under the skin, and exits on the upper chest below the clavicle. A Dacron cuff sits inside the tunnel near the '
               'exit and seals it. The tip lies in the right atrium. Bacteria reach the blood by two routes: along the outside from the '
               'exit site and tunnel, or down the inside from a hub that was handled.</p>\n'
               '<p><strong>The biofilm.</strong> Bacteria in the biofilm are shielded from antibiotics and white cells, so the same '
               'organism returning after treatment points to the catheter.</p>\n'
               '{{key:A clean exit site does not mean a clean catheter. The same organism twice means the catheter is the source.}}\n'
               '<div class="tc-scene"><span class="tc-lab">At the access review &middot; fictional</span><p>Mr. Domingo&rsquo;s blood '
               'cultures grow <em>Staphylococcus aureus</em> again, four weeks after the last course. The exit site looks clean.</p><p>You '
               'explain to the fellow that the bacteria live in the biofilm, out of reach of the antibiotics.</p><p '
               'class="tc-scene-take"><b>What this shows.</b> Treat the source, not only the culture.</p></div>\n'
               '\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Access planning.</strong> The Kidney Disease Outcomes Quality Initiative (KDOQI) 2019 guideline moved from '
               '&ldquo;fistula first&rdquo; to an individualized end-stage kidney disease (ESKD) Life-Plan: the right access for the right '
               'patient at the right time. It names the right internal jugular vein as the preferred site for a tunneled '
               'catheter.[[an16_1]] Most access evidence is observational.</p>\n'
               '<p><strong>Lock solutions.</strong> LOCK IT-100 randomized 795 patients dialyzing through catheters at 70 US sites to a '
               'taurolidine&ndash;heparin lock or heparin alone, double-blind. Bloodstream infection occurred in 9 of 397 patients (2%) '
               'versus 32 of 398 (8%): 0.13 versus 0.46 per 1,000 catheter-days (hazard ratio 0.29). Safety was similar. The trial stopped '
               'early for benefit, which can overstate an effect.[[an16_5]] Check local registration and cost before relying on it.</p>\n'
               '<p><strong>Treatment and removal.</strong> The Infectious Diseases Society of America (IDSA) 2009 guideline advises '
               'removing the catheter for infection with <em>S. aureus</em>, <em>Pseudomonas</em> or <em>Candida</em>, and for complicated '
               'infection such as tunnel infection or septic shock.[[an16_6]]</p>\n'
               '<p><strong>Prevention.</strong> The Centers for Disease Control and Prevention (CDC) Core Interventions combine '
               'surveillance with feedback, hand hygiene and catheter-care audits, chlorhexidine skin antisepsis, hub disinfection, staff '
               'training and catheter reduction. They are associated with lower bloodstream infection rates in collaborative projects; the '
               'evidence is observational.[[an16_4]]</p>\n'
               '{{key:Fewer catheter-days is the strongest prevention. Lock solutions and audits reduce the risk of the days that '
               'remain.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Write an access life-plan for each patient:</strong> current access, next access, the arm to protect (no '
               'venipuncture or peripherally inserted central catheter), the surgeon and the date. When surgery is postponed for cost, '
               'record the reason and ask what support is available.</p>\n'
               '<p><strong>Fever or rigors in a catheter patient.</strong> Stop the session if unstable. Take cultures from the catheter '
               'and a second site, start vancomycin with gram-negative cover from the local antibiogram, and decide on the '
               'catheter.[[an16_6]]</p>\n'
               '<p><strong>Surveillance.</strong> Dialysis facilities are licensed by the Department of Health (DOH) under Administrative '
               'Order 2012-0001,[[an16_2]] and the unit&rsquo;s infection program belongs to the clinical head and the infection-control '
               'nurse. Your part is to report your patients&rsquo; events and to ask for a rate per 1,000 catheter-days, not a count.</p>\n'
               '\n'
               '{{fig:an16_a}}\n'
               '<div class="tc-scene"><span class="tc-lab">At the monthly infection review &middot; fictional</span><p>Eleven of your '
               'patients at the unit are on catheters. Five have no date for fistula surgery. Two have had their surgery postponed '
               'twice.</p><p>You write an access life-plan for each: current access, next access, the arm to protect, the surgeon and the '
               'date. You ask the head nurse to bring the list to every monthly visit until the column of dates is full.</p><p '
               'class="tc-scene-take"><b>What this shows.</b> A catheter without a removal date tends to become permanent.</p></div>\n'
               '{{key:Every catheter needs a surgeon&rsquo;s name and a date beside it.}}\n'
               '{{call:<ul><li>Rigors or hypotension during hemodialysis with a catheter</li><li>Pulsatile bleeding or a ruptured '
               'aneurysm</li><li>Cold, painful hand after access creation (steal)</li><li>Swelling of the whole arm (central vein '
               'stenosis)</li></ul>}}\n')],
 'debrief': ['<p><strong>Now.</strong> Tell Dr. Salonga to stop the session. This is septic shock, not a fever for paracetamol. He '
             'activates the sepsis pathway and resuscitates, takes blood cultures from the catheter and a second site, and gives empiric '
             'vancomycin plus gram-negative cover from the local antibiogram. Transfer for monitored care, and confirm who receives '
             'him.</p>\n'
             '<p><strong>The catheter.</strong> It has to come out. Septic shock and a second <em>S. aureus</em> infection are both '
             'reasons for removal. The bacteria live in the biofilm, out of reach of the antibiotics. Arrange temporary access for further '
             'dialysis, and call the access surgeon yourself for a firm fistula date. Seven months on a catheter was a plan that '
             'drifted.</p>\n'
             '<p><strong>The third infection.</strong> The unit&rsquo;s surveillance belongs to the clinical head and the '
             'infection-control nurse, and the three patients may have three different attending nephrologists. Report this event, ask for '
             'a rate per 1,000 catheter-days compared with last quarter, and support an audit of catheter care on every shift. Then check '
             'your own panel: every catheter needs a life-plan with a surgeon and a date.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Examines or describes access findings', False),
                      ('Documents urgency and the infection plan', False),
                      ('Assigns a definitive access review', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('Which action matters most in an unstable patient with suspected access sepsis?',
           ['Schedule a future access clinic',
            'Emergency stabilization and coordinated infection management',
            'Wait for final culture before escalation',
            'Continue the session to finish fluid removal'],
           1,
           'Instability requires immediate intervention and source assessment.'),
          ('What makes a vascular access life-plan individualized?',
           ['It accounts for treatment trajectory, anatomy and patient goals',
            'It mandates the same option for every patient',
            'It begins after every vascular option is exhausted',
            'It is written only by the surgeon'],
           0,
           'Selection should anticipate current and future access needs.'),
          ('What did LOCK IT-100 show?',
           ['Lower mortality as the primary outcome',
            'No difference from heparin',
            'Higher thrombosis with taurolidine',
            'A 71% lower risk of catheter-related bloodstream infection with taurolidine-heparin lock'],
           3,
           'The primary endpoint was time to adjudicated catheter-related bloodstream infection.'),
          ('Which organism usually requires catheter removal in catheter-related bloodstream infection?',
           ['Any organism after one dose of antibiotics',
            'Coagulase-negative Staphylococcus with prompt response',
            'Staphylococcus aureus',
            'Contaminant Bacillus species'],
           2,
           'S. aureus, Pseudomonas and Candida infections are poorly cleared from biofilm.'),
          ('Why compare infection rates per 1,000 catheter-days rather than raw counts?',
           ['Raw counts are always lower',
            'The denominator adjusts for how many patients had catheters and for how long',
            'It is a Philippine Health Insurance Corporation (PhilHealth) form requirement',
            'It removes the need for cultures'],
           1,
           'Exposure-based rates allow fair comparison over time.')],
 'terms': [('ESKD', 'End-stage kidney disease'),
           ('IV', 'Intravenous'),
           ('KDOQI', 'Kidney Disease Outcomes Quality Initiative'),
           ('HD', 'Hemodialysis'),
           ('CRBSI', 'Catheter-related bloodstream infection'),
           ('IDSA', 'Infectious Diseases Society of America'),
           ('CDC', 'Centers for Disease Control and Prevention'),
           ('DOH', 'Department of Health'),
           ('PSN', 'Philippine Society of Nephrology')],
 'readings': [('hemodialysis-access-lifeline.html',
               'Transforming the Achilles Heel of Hemodialysis Access into a "Lifeline That Lasts for a Lifetime"'),
              ('dialysis-access-infection.html', 'When the Access Gets Infected')],
 'calcs': ['calc-access-infection-rate.html',
           'calc-catheter-exposure.html',
           'calc-access-flow-cardiac.html',
           'calc-access-intervention-burden.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
