# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 04: Consent, prescribing and medication reconciliation.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. KDIGO 2024 statements checked against its summary of recommendations and practice points; metformin dosing
corrected to its source, the KDIGO 2022 diabetes-in-CKD guideline (Rec. 4.1.1, Practice Point 4.1.3, Figure 27); teach-back
evidence checked against the PubMed record (Ha Dinh 2016)."""

MODULE = {'image_alt': 'Top-down view of an older patient and a pharmacist going through a weekly pill organizer together.',
 'objectives': ['Use teach-back to confirm understanding and document an informed choice.',
                'Reconcile medicines across changes in kidney function and modality.',
                'Record hold and restart criteria with a named reviewer.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the '
        'Philippine Society of Nephrology (PSN) guidelines, you explain every option for end-stage kidney disease and document the '
        'informed consent, preferably witnessed by two people (b1). You keep the current medicines ready for the clinical abstract '
        '(b5).[[an04_3]]</div>\n'
        '{{plain:A drug dose is like a recipe written for one particular oven. Put the same dish in an oven that runs hotter or cooler '
        'and it burns or comes out raw. When the kidney changes, every recipe has to be reread.}}\n'
        '<p>The picture has a limit. An oven has one setting. A kidney keeps changing: filtration falls in acute kidney injury (AKI), '
        'recovers over weeks, or is partly replaced by dialysis, which clears some drugs and not others. Some drugs even change the '
        'oven, by altering pressure in the glomerulus. Medication errors cluster at these transitions.</p>\n'
        '{{cards:Key numbers|Creatinine after starting an angiotensin-converting enzyme (ACE) inhibitor or angiotensin receptor blocker '
        '(ARB)::Continue unless it rises &gt;30% within 4 weeks (KDIGO 2024, practice point)|Metformin (KDIGO 2022)::Halve the dose at '
        'estimated glomerular filtration rate (eGFR) 30&ndash;44; stop below 30}}\n'
        '<p>Your patients carry their medicines in a plastic bag and their history on discharge sheets from different hospitals. '
        'Your work in this module is to produce one list, with a reason, a restart trigger and an owner for every change.</p>\n',
 'case': {'title': 'Two lists in one plastic bag',
          'html': '<p>Mr. Navarro, 58, comes to your clinic at the dialysis center a week after a hospital stay for gastroenteritis that '
                  'pushed his kidney function down. He has diabetes and chronic kidney disease (CKD) G3a, and he is not on dialysis. He '
                  'hands you a plastic bag with every box of medicine he owns and two discharge sheets, one from the ward and one from the '
                  'emergency room.</p>\n'
                  '<p>One sheet says &ldquo;stop losartan, empagliflozin, and metformin.&rdquo; The other says &ldquo;continue all home '
                  'medicines.&rdquo; He has been taking only his amlodipine &ldquo;to be safe,&rdquo; and to save money while he was out of '
                  'work. His creatinine today is 1.4 mg/dL; his baseline before the illness was 1.3. He is eating and drinking normally. His '
                  'daughter, who manages his medicines, asks, &ldquo;Doc, which list is right?&rdquo;</p>\n',
          'questions': ['Which list is right?',
                        'How will you make sure the family does not end up with a third version?',
                        'What should happen the next time he has vomiting or diarrhea?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>Drug exposure equals dose divided by clearance. For drugs cleared by the kidney, or with active metabolites cleared by '
               'it (metformin, gabapentinoids, enoxaparin, many antibiotics, direct oral anticoagulants, and morphine through '
               'morphine-6-glucuronide), a falling glomerular filtration rate (GFR) raises exposure at the same dose.</p>\n'
               '<p>Dialysis then adds clearance in bursts. A small, water-soluble, unbound drug with a small volume of distribution, such '
               'as vancomycin, is removed substantially by a high-flux membrane. A highly protein-bound or lipid-soluble drug is barely '
               'touched.</p>\n'
               '<p>Some drugs change kidney hemodynamics directly. Angiotensin-converting '
               'enzyme (ACE) inhibitors and angiotensin receptor blockers (ARBs) dilate the efferent arteriole; sodium-glucose '
               'cotransporter 2 (SGLT2) inhibitors constrict the afferent arteriole through tubuloglomerular feedback. Both lower the '
               'pressure inside the glomerulus, so an early rise in creatinine is expected. Nonsteroidal anti-inflammatory drugs (NSAIDs) '
               'remove the prostaglandins that hold the afferent arteriole open when volume is low. That is why these drugs are held '
               'during vomiting or diarrhea.</p>\n'
               '{{key:For each drug at each transition, ask two questions: who clears it now, and does it change the pressure in the '
               'glomerulus?}}\n'
               '<div class="tc-scene"><span class="tc-lab">By phone &middot; fictional</span><p>Mr. Tolentino, on hemodialysis, was given '
               'vancomycin in hospital and told to &ldquo;have a dose after dialysis.&rdquo; On Wednesday the nurse calls to ask whether '
               'to give it. You ask what membrane he dialyzes on. It is high-flux.</p><p>Vancomycin is small, water-soluble, and mostly '
               'unbound, so a high-flux session removes a large share of it. You ask for a level and dose to it, instead of '
               'guessing.</p><p class="tc-scene-take"><b>What this shows.</b> Dialysis adds clearance that depends on the drug and the '
               'membrane.</p></div>\n'
               '\n'
               '{{fig:an04_a}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Dosing by kidney function.</strong> Kidney Disease: Improving Global Outcomes (KDIGO) 2024 gives only '
               'practice points here: consider GFR when dosing '
               'drugs cleared by the kidney, use a creatinine-based estimated GFR (eGFR) for most dosing, add cystatin C or measure GFR for drugs with a '
               'narrow therapeutic range, and review medicines at every transition of care.[[an04_1]]</p>\n'
               '<p><strong>The expected creatinine rise.</strong> KDIGO 2024 advises continuing an ACE inhibitor or ARB unless creatinine '
               'rises by more than 30% within 4 weeks of starting (practice point). For SGLT2 inhibitors it states that the reversible fall in eGFR at the start is generally not a reason '
               'to stop (practice point).[[an04_1]]</p>\n'
               '<p><strong>Holding and restarting.</strong> KDIGO 2024 suggests considering planned holds of metformin, ACE inhibitors, '
               'ARBs and SGLT2 inhibitors before elective surgery or while managing an adverse effect, warns that failing to restart them '
               'may cause harm, and asks for a clear restart plan (practice points).[[an04_1]]</p>\n'
               '<p><strong>Metformin.</strong> The KDIGO 2022 diabetes guideline recommends metformin for type 2 diabetes with CKD and '
               'eGFR &ge;30 (1B). It advises halving the dose at eGFR 30 to 44, considering a reduction for some patients at 45 to 59, and '
               'stopping it below 30.[[an04_4]]</p>\n'
               '<p><strong>Teach-back.</strong> In a systematic review of 12 studies in chronic disease, four showed better '
               'disease-specific knowledge; effects on readmission were positive but inconsistent.[[an04_5]] It is a low-cost habit, not '
               'a proven way to prevent hospitalization.</p>\n'
               '{{key:Most of what guides reconciliation is practice points and physiology, not trials. Say so, and keep the restart '
               'plan as firm as the stop.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Compare three lists.</strong> At every transition, set side by side what the patient actually takes, the last '
               'discharge list, and the current orders. Ask about over-the-counter and herbal remedies. For each discrepancy, decide continue, adjust, hold or stop. Write the reason, the restart '
               'trigger (for example, &ldquo;restart losartan when creatinine is within 20% of baseline and systolic pressure is above '
               '110&rdquo;), and the named reviewer with a date.</p>\n'
               '<p>Patients often stop a medicine because of cost and do not say so. Ask, and write the generic name where a '
               'registered generic exists.</p>\n'
               '<p><strong>Consent in plain language.</strong> Discuss benefits, burdens and alternatives, including doing nothing, in the '
               'family&rsquo;s language, document the choice as the PSN guideline asks,[[an04_3]] and close with teach-back.</p>\n'
               '<p>Give the family a copy and send one to the referring internist through an approved channel; the list is personal '
               'health information under the Data Privacy Act.[[an04_2]]</p>\n'
               '\n'
               '{{fig:an04_b}}\n'
               '<div class="tc-scene"><span class="tc-lab">In the clinic, teach-back &middot; fictional</span><p>You finish explaining Mr. '
               'Navarro&rsquo;s new list and ask his daughter, &ldquo;Tell me in your own words what he takes tomorrow.&rdquo; She lists '
               'the tablets correctly, then adds, &ldquo;And if he has diarrhea, he stops all of them.&rdquo;</p><p>You correct it: only '
               'losartan, empagliflozin, and metformin pause, and they restart once he is eating and drinking again. Amlodipine continues '
               'unless his pressure is low. She writes it on the list herself.</p><p class="tc-scene-take"><b>What this shows.</b> '
               'Teach-back finds the misunderstanding while you can still fix it.</p></div>\n'
               '{{key:One list, one reason per change, one restart trigger, one named reviewer. Anything less becomes a third version at '
               'home.}}\n'
               '{{call:<ul><li>Two conflicting discharge lists</li><li>&lsquo;Resume all when well&rsquo;</li><li>Renally cleared drug at '
               'full dose after AKI</li><li>Held cardioprotective therapy with no restart plan</li></ul>}}\n')],
 'debrief': ['<p><strong>Which list is right?</strong> Neither, as written. Start from what he actually takes: only amlodipine. His '
             'creatinine is within 10% of baseline and he is eating and drinking, so restart losartan and empagliflozin; the small '
             'creatinine rise they cause is expected. Restart metformin at the dose his eGFR allows.</p>\n'
             '<p><strong>One list.</strong> Write a single reconciled list with a decision and a reason for each drug. Arrange potassium '
             'and creatinine checks in one to two weeks, name who will message the family with the result, and send a copy to his '
             'internist. Then use teach-back.</p>\n'
             '<p><strong>Next time he is sick.</strong> Put the hold-and-restart plan in writing: when he cannot keep fluids down, he '
             'pauses losartan, empagliflozin, and metformin, and restarts them once he is eating and drinking again. Add: &ldquo;Message '
             'the clinic if you are not better in two days.&rdquo; A hold without a restart trigger becomes a permanent stop.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Uses teach-back', False),
                      ('Identifies a dose or timing concern by mechanism', False),
                      ('Assigns each pending medication decision an owner and a date', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('Which medication instruction supports safe follow-up?',
           ['Resume everything when well',
            'A defined review date, trigger and owner',
            'Hold indefinitely pending advice',
            'Ask the pharmacy to decide'],
           1,
           'KDIGO 2024 asks for a clear restart plan whenever medicines are stopped during an acute illness (practice point).'),
          ('How should the physician check consent comprehension?',
           ['Ask the patient to explain the options and agreed plan in their own words',
            'Ask only whether the information was clear',
            'Collect a signature before discussion',
            'Give a printed leaflet only'],
           0,
           'Teach-back reveals misunderstandings while there is time to address them.'),
          ('Two weeks after starting an SGLT2 inhibitor, creatinine rises 18% with stable potassium. Best action?',
           ['Switch to an NSAID',
            'Stop immediately',
            'Order a kidney biopsy',
            'Continue and recheck; this is the expected hemodynamic effect'],
           3,
           'Lower intraglomerular pressure produces an early, reversible eGFR dip. KDIGO 2024 states it is generally not a reason to '
           'stop (practice point).'),
          ('Which drug property most predicts substantial removal by high-flux hemodialysis (HD)?',
           ['Extensive tissue binding',
            'High lipid solubility',
            'Low protein binding with a small volume of distribution',
            'Very high molecular weight above 50 kDa'],
           2,
           'Unbound drug in plasma water crosses the membrane; drug held in tissue is not reached.'),
          ('Under the KDIGO 2022 diabetes guideline, metformin should be stopped when eGFR falls below:',
           ['60 mL/min/1.73 m²', '30 mL/min/1.73 m²', '45 mL/min/1.73 m²', '15 mL/min/1.73 m²'],
           1,
           'The guideline recommends metformin at eGFR 30 or more (1B), halves the dose at 30 to 44, and stops it below 30.')],
 'terms': [('AKI', 'Acute kidney injury'),
           ('CKD', 'Chronic kidney disease'),
           ('GFR', 'Glomerular filtration rate'),
           ('eGFR', 'Estimated glomerular filtration rate'),
           ('ACE', 'Angiotensin-converting enzyme'),
           ('ARB', 'Angiotensin receptor blocker'),
           ('SGLT2', 'Sodium-glucose cotransporter 2'),
           ('NSAID', 'Nonsteroidal anti-inflammatory drug'),
           ('HD', 'Hemodialysis'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes')],
 'readings': [('medication-operational-guide.html', "The CKD Prescriber's Playbook")],
 'calcs': ['calc-egfr-ckd-epi.html', 'calc-renal-med-safety.html', 'calc-metformin-ckd-safety.html', 'calc-sglt2i-eligibility.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
