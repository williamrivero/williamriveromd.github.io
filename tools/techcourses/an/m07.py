# -*- coding: utf-8 -*-
"""Attending Nephrologist, Module 07: Acute kidney replacement therapy in the ICU.
Rewritten November 26, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, and framed for
Philippine practice. Figures checked against the PubMed abstracts (STARRT-AKI, AKIKI 2) and the KDIGO 2012 AKI guideline."""

MODULE = {'image_alt': 'An intensivist and a nephrologist confer at the foot of an ICU bed.',
 'objectives': ['Start acute kidney replacement therapy (KRT) for indications and trajectory, not for a creatinine number.',
                'Match modality to hemodynamics, brain risk, local capability and transfer feasibility.',
                'Write a plan that includes daily recovery review and stopping criteria.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your duty &middot; Section 1.2, 2024 hemodialysis guidelines</span>Under the '
        'Philippine Society of Nephrology (PSN) guidelines, you coordinate during emergencies (b8), and you endorse by letter or call when '
        'your patient is under another nephrologist&rsquo;s care in hospital (b12).[[an01_1]]</div>\n'
        '{{plain:Dialysis in the intensive care unit (ICU) is life support for a failing organ, like a ventilator for the lungs. You put '
        'a patient on a ventilator when the lungs can no longer keep oxygen and carbon dioxide survivable, not because one blood gas looked '
        'bad.}}\n'
        '<p>The picture has a limit. A ventilator rests the lungs; dialysis does not rest the kidney and may slow its recovery. So the '
        'moment to start is a trade, not a threshold.</p>\n'
        '{{cards:Key numbers|STARRT-AKI, 90-day mortality::43.9% accelerated vs 43.7% standard|Standard-arm patients never '
        'dialyzed::About 38%|Dialysis dependence at 90 days, survivors::10.4% accelerated vs 6.0% standard (relative risk 1.74)|AKIKI 2, '
        'waiting longer::No gain in dialysis-free days; 60-day death hazard ratio 1.65 (secondary analysis)|Urine output suggesting '
        'recovery::&gt;400&ndash;500 mL/day without diuretics (common practice; not trial-defined)}}\n'
        '<p>In Philippine practice you are usually the consultant, reached by phone at night by the intensivist or internist of record. '
        'Your work is to say whether there is an indication today, which modality this hospital can deliver safely, and what would change '
        'your answer.</p>\n',
 'case': {'title': 'The ICU wants your machine',
          'html': '<p>A hospital 20 minutes from your unit calls you at 9 p.m. Mrs. Bautista, 66, has septic shock from a gallbladder '
                  'infection. She is on norepinephrine and high-flow oxygen. Her fluid balance is now 9 liters positive, and her oxygen '
                  'requirement keeps rising despite high-dose furosemide. The hospital has no continuous kidney replacement therapy '
                  '(CRRT); the nearest center that does is 90 minutes away by ambulance.</p>\n'
                  '<p>The intensivist asks whether your unit&rsquo;s nurses can bring a hemodialysis machine to the ICU and &ldquo;pull off '
                  'the fluid.&rdquo; Your biomedical technician says one portable machine and a reverse-osmosis unit are free tonight. Your '
                  'head nurse warns that her two nurses on call have never done a session in an ICU.</p>\n',
          'questions': ['Is there an indication, or is this a number?',
                        'Should she be moved for continuous therapy, or treated where she is?',
                        'What must be agreed before your nurses connect her?']},
 'sections': [('physiology',
               'Physiology',
               'How it works',
               '<p>The classic indications describe a loss of balance the body cannot buy back: potassium beyond cellular buffering, '
               'acidemia that depresses the heart and blunts vasopressors, fluid that floods the lungs, uremic pericarditis or '
               'encephalopathy, a dialyzable poison. Timing is a trade: starting earlier removes these threats sooner but exposes patients '
               'who would have recovered to catheter infection, hypotension, drug and nutrient loss, and possibly slower recovery.</p>\n'
               '<p>Modality is a second trade. Intermittent hemodialysis (HD) works fast, which can drop blood pressure and, by lowering '
               'plasma osmolality quickly, drive water into an injured brain. Continuous therapy trades efficiency for steadiness.</p>\n'
               '<div class="table-wrap"><table>\n'
               '<thead><tr><th>What the kidney has lost</th><th>What you see</th><th>Whether dialysis replaces it</th></tr></thead>\n'
               '<tbody>\n'
               '<tr><td>Potassium excretion</td><td>Potassium rising despite shifting drugs; electrocardiogram (ECG) changes</td><td>Yes, quickly</td></tr>\n'
               '<tr><td>Acid excretion</td><td>pH falling despite treating the cause</td><td>Yes</td></tr>\n'
               '<tr><td>Salt and water excretion</td><td>Positive balance with worsening oxygenation; no diuretic response</td><td>Yes, by '
               'ultrafiltration</td></tr>\n'
               '<tr><td>Clearance alone, with none of the above</td><td>A high creatinine, a stable patient</td><td>Usually no reason yet to '
               'start</td></tr>\n'
               '</tbody></table></div>\n'
               '{{key:Ask what the kidney can no longer do. If the answer is &ldquo;nothing the body cannot survive today,&rdquo; write '
               'the triggers and wait.}}\n'
               '<div class="tc-scene"><span class="tc-lab">On the ICU round &middot; fictional</span><p>The intensivist points at Mr. '
               'Ramos&rsquo;s creatinine: 5.2 mg/dL. &ldquo;Should we start?&rdquo; You look at the rest: potassium 4.6, bicarbonate 20, '
               'oxygen improving, urine output 700 mL yesterday and rising.</p><p>No balance has been lost that the body cannot buy back. You '
               'write: &ldquo;No indication today. Start if potassium exceeds 6.0 despite treatment, pH falls below 7.15, or oxygen '
               'requirement rises with a positive fluid balance. Review tomorrow.&rdquo;</p><p class="tc-scene-take"><b>What this '
               'shows.</b> A written trigger lets the team act without waiting for you.</p></div>\n'
               '\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Timing.</strong> STARRT-AKI randomized critically ill adults with severe acute kidney injury (AKI) to an '
               'accelerated start within 12 hours or a standard strategy that waited for conventional indications or AKI lasting more than '
               '72 hours. Among 2,927 patients, 90-day mortality was 43.9% versus 43.7%. About 38% of the standard arm never needed '
               'dialysis. Among survivors, dialysis dependence was 10.4% versus 6.0% (relative risk 1.74), and adverse events 23.0% versus '
               '16.5%.[[an07_3]] Early starts did not improve survival and may slow recovery.</p>\n'
               '<p><strong>How long to wait.</strong> AKIKI 2 randomized 278 patients who already had 72 hours of oliguria or a blood urea '
               'nitrogen above 112 mg/dL. Waiting further, until a mandatory indication or a urea nitrogen of 140 mg/dL, gave no more '
               'dialysis-free days (median 10 versus 12). In a multivariable analysis, the more-delayed strategy was associated with higher '
               '60-day mortality (hazard ratio 1.65).[[an07_6]] Small trial, secondary finding, but waiting needs a ceiling.</p>\n'
               '<p><strong>Modality.</strong> The Kidney Disease: Improving Global Outcomes (KDIGO) 2012 guideline treats continuous and '
               'intermittent therapy as complementary (ungraded). It suggests CRRT for hemodynamically unstable patients (2B) and for acute '
               'brain injury or raised intracranial pressure (2B).[[an07_1]] Randomized trials have not shown a mortality difference '
               'between the two. The KDIGO 2026 draft, still in public review, revisits these questions; until it is final, quote the 2012 '
               'grades.[[an07_2]] The International Society for Peritoneal '
               'Dialysis (ISPD) supports acute peritoneal dialysis (PD) where extracorporeal therapy is not available.[[an07_4]]</p>\n'
               '\n'
               '{{fig:an07_a}}\n'
               '{{key:Early starts did not save lives, and very late starts may cost them. Decide each day, against named triggers.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Review daily, even by phone.</strong> Look for an absolute indication, or a trajectory toward one: potassium '
               'rising despite treatment, or fluid balance climbing while oxygenation worsens. Ask about goals of care. If you wait, write why and '
               'the triggers that end the wait, so the night resident can act without you.</p>\n'
               '<p><strong>Choose the modality the hospital can actually deliver.</strong> Many Philippine hospitals have no CRRT, and some '
               'ICUs depend on a dialysis unit&rsquo;s nurses and a portable machine. Weigh hemodynamics, brain risk, nursing skill, water '
               'safety, and the danger of transfer; an unstable patient may be safer with slow therapy where she is.</p>\n'
               '<p><strong>Divide the work in writing,</strong> including the hourly fluid-removal goal, the pressure at which '
               'ultrafiltration stops, and how the team reaches you.</p>\n'
               '<p><strong>Look for recovery every day.</strong> Rising urine output, a creatinine that no longer climbs between sessions, and '
               'a timed urine creatinine clearance when available.</p>\n'
               '\n'
               '{{fig:an07_b}}\n'
               '<div class="tc-scene"><span class="tc-lab">By phone, the head injury &middot; fictional</span><p>A hospital calls about a '
               'man with a subdural hematoma and AKI. They have booked a standard four-hour hemodialysis session.</p><p>You explain that a '
               'fast session lowers plasma urea quickly, and water can then move into the injured brain. You ask for continuous therapy if '
               'it is available, or a short, gentle session with low blood flow, and you write the reason in the order.</p><p '
               'class="tc-scene-take"><b>What this shows.</b> Choosing the modality is part of the prescription, and the brain is one of the '
               'reasons.</p></div>\n'
               '{{key:Every acute dialysis order needs four lines: the indication, the modality and why, who owns each task, and what would '
               'make you stop or transfer.}}\n'
               '{{call:<ul><li>Potassium rising despite shifting therapy</li><li>Fluid overload with escalating ventilator or oxygen '
               'requirements</li><li>Uremic pericarditis or encephalopathy</li><li>Dialyzable toxin meeting Extracorporeal Treatments in '
               'Poisoning (EXTRIP) criteria</li></ul>}}\n')],
 'debrief': ['<p><strong>The indication.</strong> Fluid overload that threatens her lungs and does not respond to diuretics is a true '
             'indication. This is not a creatinine decision.</p>\n'
             '<p><strong>Move her or treat her there?</strong> Weigh how unstable she is to move against how gently your team can dialyze '
             'where she is. If your unit can run slow, prolonged therapy (sustained low-efficiency dialysis or slow isolated '
             'ultrafiltration), she may be safer staying; if her vasopressor dose climbs or ultrafiltration fails, transfer her. Write that '
             'trigger down.</p>\n'
             '<p><strong>Before connecting.</strong> Agree in writing on who is responsible for what: the intensivist runs the '
             'resuscitation, you write the prescription, and your nurses run the machine with an ICU nurse at the bedside. Set an hourly '
             'fluid-removal goal, a pressure floor, and the signed water and machine checks. If your nurses are not trained for this, say '
             'so. A safe plan may be one experienced nurse with your '
             'senior technician, or no session tonight and a transfer instead. Document the indication, the modality and why you chose it, '
             'and the goals of care discussed with her family, including relatives abroad who may call in.</p>\n'],
 'skills': {'title': 'Skills checklist',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Justifies the indication by physiology', False),
                      ('Chooses a modality using hemodynamics and capability', False),
                      ('Confirms access site and location', False),
                      ('Sets daily recovery and reassessment criteria', False)],
            'placement': 'Simulation or supervised practice'},
 'quiz': [('What most strengthens the acute KRT indication?',
           ['A creatinine threshold in isolation',
            'Worsening refractory organ-threatening fluid overload',
            'The referral hospital owning CRRT machines',
            'A urea above an arbitrary cutoff with no symptoms'],
           1,
           'Indications depend on the complication and its response to treatment.'),
          ('What belongs in the acute KRT order review?',
           ['An indication, a feasible modality, reassessment and stopping criteria',
            'A modality selected only by habit',
            'An indefinite order with no reassessment date',
            'A dialysate potassium of zero for all patients'],
           0,
           'The prescription must address the indication and change with illness and recovery.'),
          ('What did STARRT-AKI show?',
           ['That CRRT is superior to intermittent HD',
            'A 25% mortality reduction with early dialysis',
            'Harm only in surgical patients',
            'No 90-day mortality benefit from accelerated initiation, with more dialysis dependence among survivors'],
           3,
           'Mortality was 43.9% versus 43.7%; dialysis dependence among survivors was 10.4% versus 6.0%.'),
          ('Which patient most clearly favors CRRT over intermittent HD?',
           ['A patient who will be discharged tomorrow',
            'A stable ward patient with isolated hyperkalemia',
            'Traumatic brain injury with raised intracranial pressure',
            'A patient with a mature fistula and normal blood pressure'],
           2,
           'Gradual solute removal avoids rapid osmotic shifts that can worsen cerebral edema; KDIGO 2012 suggests CRRT here (2B).'),
          ('Which sign during KRT most suggests renal recovery?',
           ['A stable predialysis urea',
            'Rising spontaneous urine output with falling interdialytic creatinine',
            'Improving hemoglobin',
            'Fewer circuit alarms'],
           1,
           'Returning native filtration shows up as urine and as creatinine that no longer climbs between sessions.')],
 'terms': [('KRT', 'Kidney replacement therapy'),
           ('AKI', 'Acute kidney injury'),
           ('STARRT-AKI', 'Standard versus Accelerated Initiation of Renal Replacement Therapy in Acute Kidney Injury trial'),
           ('AKIKI 2', 'Artificial Kidney Initiation in Kidney Injury 2 trial'),
           ('ICU', 'Intensive care unit'),
           ('ICP', 'Intracranial pressure'),
           ('CRRT', 'Continuous kidney replacement therapy'),
           ('HD', 'Hemodialysis'),
           ('PD', 'Peritoneal dialysis'),
           ('ECG', 'Electrocardiogram'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('ISPD', 'International Society for Peritoneal Dialysis'),
           ('EXTRIP', 'Extracorporeal Treatments in Poisoning workgroup')],
 'readings': [('aki-icu-dialysis-decisions.html', 'Dialysis Decisions in the ICU: AKI, Prognosis & Time-Limited Trials')],
 'calcs': ['calc-fluid-overload.html', 'calc-vasopressor-inotrope.html', 'calc-starting-dialysis-planner.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("an_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
