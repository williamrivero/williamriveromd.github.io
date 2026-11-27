# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 03: Fluids, sodium and acid-base in children.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard. AAP 2018 key
action statement and grade, PIMS results, and Moritz-Ayus reviews checked against PubMed abstracts; correction limits
against the 2014 European hyponatraemia guideline text as quoted by issuer-derived protocols; dengue phases against the WHO
2009 guideline. No doses or fluid orders. Fictional case."""

MODULE = {'image_alt': 'A pediatric nephrologist and a resident check an infusion pump and a fluid bag beside a toddler&rsquo;s crib in a provincial hospital ward.',
 'objectives': ['Explain why hypotonic maintenance fluids cause hospital-acquired hyponatremia, and apply the American Academy of Pediatrics (AAP) 2018 recommendation for isotonic maintenance fluids within its stated scope.',
                'Recognize hyponatremic encephalopathy and hypernatremia in infants and correct sodium at a speed the brain can tolerate, using the unit&rsquo;s protocol for the actual order.',
                'Manage fluids through the phases of dengue and classify metabolic acidosis with anion-gap logic.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the fluid consultant for the pediatric ward</span>Residents write '
        'most of the fluid orders in a Philippine pediatric ward, often at night and often from a template. You are called when the sodium '
        'has already moved or the child has already swollen. Your duty is to fix the template as well as the child.</div>\n'
        '{{plain:Think of the body&rsquo;s sodium and water as salt dissolved in a pot of soup. The cook can make it too salty by adding salt or '
        'by boiling off water, and too bland by adding water or by scooping out salt. Taste alone does not tell you which happened.}}\n'
        '<p>The picture has a limit. A pot has no thirst and no kidney. A child does: antidiuretic hormone (ADH, arginine vasopressin) '
        'decides how much water the kidney keeps, and in a sick child it is often switched on by things that have nothing to do with sodium '
        '&mdash; vomiting, pain, fear, low volume, lung or brain disease, surgery. When ADH is on, the kidney keeps free water, and any '
        'free water you infuse stays in the pot. And the brain is not soup. Its cells swell when sodium falls fast and shrink when it rises '
        'fast, inside a skull that cannot stretch.</p>\n'
        '{{cards:Key numbers|AAP 2018 maintenance fluids::Isotonic solutions for ages 28 days to 18 years (evidence quality A; strong '
        'recommendation)|PIMS trial, hyponatremia::4% with sodium 140 mmol/L versus 11% with 77 mmol/L|Hyponatremia defined (European '
        'guideline)::Serum sodium below 135 mmol/L; acute if documented to exist less than 48 hours|Correction limit, chronic hyponatremia '
        '(European guideline)::No more than 10 mmol/L in the first 24 hours and 8 mmol/L in each 24 hours thereafter|Dengue critical '
        'phase::Around defervescence, usually days 3&ndash;7, lasting about 24&ndash;48 hours}}\n'
        '<p>Most children on intravenous fluids do well on any reasonable order. A few, with ADH switched on, drown their brain cells in '
        'free water from a fluid that looked harmless on the chart. Your work is to choose maintenance fluid that does not cause hyponatremia, '
        'to treat brain swelling fast and chronic hyponatremia slowly, and to watch the volume as closely as the sodium.</p>\n',
 'case': {'title': 'The seizure at 3 a.m.',
          'html': '<p>It is 3:20 a.m. at a district hospital in Cabanatuan, Nueva Ecija. The pediatric resident calls you. Andrea Dela Cruz, '
                  '18 months old and 10 kg, was admitted 18 hours ago with gastroenteritis and moderate dehydration. Her admission sodium was '
                  '134 mmol/L. After a saline bolus she was started on 5% dextrose with 0.3% sodium chloride at the full Holliday&ndash;Segar '
                  'rate, plus replacement for ongoing losses. She kept vomiting. At 3 a.m. she had a generalized seizure lasting four minutes, '
                  'stopped by the resident with a benzodiazepine. She is now drowsy, with a heart rate of 150 and a capillary refill under 2 '
                  'seconds.</p>\n'
                  '<p>A point-of-care sodium is 121 mmol/L. The resident plans to &ldquo;restrict fluids to two-thirds and recheck in the '
                  'morning.&rdquo; The ward has no premixed hypertonic saline; the pharmacy can prepare it from stock if someone writes the '
                  'order. The nearest pediatric intensive care unit is two hours away in Manila. Her grandmother asks whether the dextrose '
                  'drip caused the seizure.</p>\n',
          'questions': ['Why did Andrea&rsquo;s sodium fall, and why is fluid restriction alone the wrong answer tonight?',
                        'What happens in the next hour, and how fast should sodium rise after that?',
                        'What maintenance fluid should she have from now on, and what do you change on the ward?']},
 'sections': [('physiology',
               'Physiology',
               'Water follows ADH, and the brain follows water',
               '<p>Maintenance fluid replaces what a child loses through skin, breath, urine and stool. Holliday and Segar linked that water need to '
               'the calories a child spends, scaled by weight.[[apn03_2]] Their 1957 estimate is still the basis of most ward calculators. It '
               'tells you how much water a healthy child needs. It says nothing about how much a sick child, with ADH switched on, can '
               'excrete.</p>\n'
               '<p>That is the trap. Gastroenteritis, pneumonia, meningitis, surgery, pain and nausea all release ADH regardless of the serum '
               'sodium. With ADH on, the kidney returns free water to the blood. A hypotonic infusion supplies that free water; the sodium falls. '
               'Moritz and Ayus reviewed reports of death and permanent neurological injury from hospital-acquired hyponatremia in children and '
               'adults and found that virtually all of it followed hypotonic fluids, while prospective studies showed that 0.9% sodium chloride '
               'prevents it.[[apn03_4]] Their reviews are observational and expert in nature, but the mechanism is established physiology and the '
               'trial evidence below agrees.</p>\n'
               '<p>Children are especially vulnerable. The brain occupies a large share of the skull, so there is little room for swelling. '
               'Hypoxia and central nervous system disease lower the sodium at which encephalopathy appears.[[apn03_5]] Symptoms can begin with '
               'headache, vomiting and lethargy, which are easy to blame on the illness itself.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Stimulus</th><th>Why ADH rises</th><th>What you see on the ward</th></tr></thead><tbody>'
               '<tr><td>Volume depletion (gastroenteritis, dengue leak)</td><td>Baroreceptors override osmotic control</td><td>Concentrated urine '
               'despite falling sodium</td></tr>'
               '<tr><td>Nausea, vomiting, pain</td><td>Non-osmotic release</td><td>Sodium falls after admission, not before</td></tr>'
               '<tr><td>Pneumonia, bronchiolitis, meningitis</td><td>Lung and brain disease</td><td>Low sodium with normal or high volume</td></tr>'
               '<tr><td>Surgery, opioids</td><td>Stress response and drugs</td><td>Post-operative fall in sodium on hypotonic fluid</td></tr>'
               '</tbody></table></div>\n'
               '<p>Water moves across cell membranes in seconds; brain cells defend their volume over hours to days by exporting solutes. That '
               'adaptation decides treatment. In acute hyponatremia (documented for less than 48 hours, as the European guideline defines it),'
               '[[apn03_7]] the brain has not adapted, swelling is the danger, and a prompt rise in sodium is protective. In chronic hyponatremia, '
               'the brain has adapted, and a fast rise shrinks cells that have lost their solutes, the setting for osmotic demyelination.</p>\n'
               '{{key:A fluid that is safe for a healthy child can be dangerous for a sick one. In hospital, assume ADH is on until the urine '
               'proves otherwise.}}\n'
               '\n{{fig:apn03_a}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>Isotonic maintenance fluid.</strong> The American Academy of Pediatrics (AAP) 2018 guideline recommends that patients '
               'aged 28 days to 18 years who need maintenance intravenous fluids receive isotonic solutions with appropriate potassium chloride '
               'and dextrose, because they significantly decrease the risk of hyponatremia (evidence quality A; recommendation strength strong).'
               '[[apn03_1]] Note the scope. The guideline excludes neonates younger than 28 days or in the neonatal intensive care unit, and '
               'children with neurosurgical disorders, cardiac disease, hepatic disease, cancer, renal dysfunction, diabetes insipidus, voluminous '
               'watery diarrhea or severe burns.[[apn03_1]] Many of your patients sit in those exclusions, where the fluid must be built from the '
               'child&rsquo;s actual losses and kidney function.</p>\n'
               '<p><strong>PIMS.</strong> The PIMS randomized controlled trial (RCT) randomized 690 children in a Melbourne children&rsquo;s hospital to maintenance fluid with '
               'sodium 140 mmol/L or 77 mmol/L in a double-blind design; primary outcome data were available for 641. Hyponatremia occurred in '
               '12 of 319 children (4%) on sodium 140 and 35 of 322 (11%) on sodium 77 (odds ratio 0.31), an absolute difference of about 7 '
               'percentage points, or roughly one case prevented for every 14 children treated. No clinically apparent cerebral edema occurred in '
               'either group. One child on sodium 140 had seizures, compared with seven on sodium 77.[[apn03_3]] Hyponatremia is a laboratory '
               'outcome; the seizure difference was small in numbers and not the primary outcome, but it points the same way.</p>\n'
               '<p><strong>Treating encephalopathy.</strong> Moritz and Ayus argue that hyponatremic encephalopathy is a medical emergency to be '
               'treated with hypertonic saline, never with fluid restriction alone, and propose intermittent bolus therapy to reverse symptoms '
               'quickly while avoiding overcorrection.[[apn03_5]][[apn03_6]] The European guideline, written for adults and widely borrowed by '
               'pediatric protocols, aims for a rise of about 5 mmol/L in the first hour for severe symptoms and then limits the increase to 10 '
               'mmol/L in the first 24 hours and 8 mmol/L in every 24 hours thereafter.[[apn03_7]] These are expert-consensus limits, not '
               'trial-derived targets, and the volume and concentration of the actual order come from your unit&rsquo;s pediatric protocol.</p>\n'
               '<p><strong>Hypernatremia.</strong> Hospital-acquired hypernatremia occurs when a child with ongoing free-water losses cannot '
               'drink. Outside hospital, the breastfed infant whose mother&rsquo;s milk supply is failing is a high-risk group for neurological '
               'damage, which lactation support and close weight monitoring largely prevent.[[apn03_6]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Claim</th><th>Evidence</th><th>What it does not show</th></tr></thead><tbody>'
               '<tr><td>Isotonic maintenance fluid prevents hyponatremia</td><td>AAP 2018 (quality A, strong); PIMS RCT (4% vs 11%)</td>'
               '<td>Benefit in excluded groups (renal dysfunction, neonates, cardiac disease)</td></tr>'
               '<tr><td>Hypertonic saline reverses encephalopathy</td><td>Physiology, case series, expert review</td><td>A randomized comparison '
               'of regimens in children</td></tr>'
               '<tr><td>Correction limits prevent demyelination</td><td>Consensus guideline</td><td>An exact safe rate for every child</td></tr>'
               '</tbody></table></div>\n'
               '{{key:Isotonic is the default for maintenance in hospital. Hypertonic saline treats brain swelling. Restriction alone treats '
               'neither.}}\n'),
              ('dengue',
               'Dengue and acid-base',
               'Dengue on the Philippine ward, and acid-base by anion gap',
               '<p><strong>Dengue.</strong> The World Health Organization (WHO) 2009 guideline describes three phases: febrile, critical and '
               'recovery. The critical phase begins around defervescence, usually on days 3 to 7, when capillary permeability rises and plasma '
               'leaks; it lasts about 24 to 48 hours. In the recovery phase the leaked fluid returns to the circulation.[[apn03_8]] Children who '
               'were given generous fluid to cover the leak can then become overloaded, with pleural effusions, ascites and respiratory '
               'distress, at the moment the team relaxes. The nephrologist is often called at exactly this point, for a child who is '
               '&ldquo;not peeing&rdquo; after days of fluid.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Phase</th><th>What the vessels are doing</th><th>What you see</th><th>Fluid '
               'question</th></tr></thead><tbody>'
               '<tr><td>Febrile</td><td>Intact; fever and poor intake</td><td>Dehydration, high temperature</td><td>Oral or modest '
               'intravenous replacement</td></tr>'
               '<tr><td>Critical</td><td>Leaking plasma</td><td>Rising hematocrit, narrowing pulse pressure, effusions</td><td>Enough to keep '
               'perfusion, no more; reassess often</td></tr>'
               '<tr><td>Recovery</td><td>Leak closes; fluid returns</td><td>Falling hematocrit, rising blood pressure, diuresis or overload</td>'
               '<td>Reduce or stop; watch for overload and hyponatremia</td></tr>'
               '</tbody></table></div>\n'
               '<p>Module 15 covers dengue acute kidney injury. Here the point is that the fluid plan must change with the phase, and the sodium '
               'and the weight should be measured often enough to see the turn.</p>\n'
               '<p><strong>Metabolic acidosis.</strong> Start with the anion gap: sodium minus chloride and bicarbonate. A raised gap means an '
               'unmeasured acid has been added: lactate from poor perfusion, ketones in diabetic ketoacidosis or starvation, retained acids in '
               'kidney failure, or a toxin. A normal gap means bicarbonate has been lost (diarrhea, proximal tubular loss) or not regenerated '
               '(distal renal tubular acidosis), or chloride has been added, as with large volumes of 0.9% saline. Correct the gap for a low '
               'albumin, which is common in sick children and hides a raised gap. In a normal-gap acidosis, the urine anion gap helps separate '
               'gut losses, where the kidney excretes ammonium and the urine gap is negative, from distal tubular failure, where it cannot.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Pattern</th><th>Mechanism</th><th>Common pediatric causes</th></tr></thead><tbody>'
               '<tr><td>Raised anion gap</td><td>Acid added</td><td>Shock (lactate), diabetic ketoacidosis, starvation ketosis, kidney failure, '
               'salicylate or other toxins</td></tr>'
               '<tr><td>Normal gap, negative urine gap</td><td>Bicarbonate lost in stool; kidney responding</td><td>Gastroenteritis, ileostomy</td></tr>'
               '<tr><td>Normal gap, positive urine gap</td><td>Kidney cannot excrete acid</td><td>Distal renal tubular acidosis (Module 8)</td></tr>'
               '<tr><td>Normal gap after resuscitation</td><td>Chloride load</td><td>Large volumes of 0.9% saline</td></tr>'
               '</tbody></table></div>\n'
               '{{key:In dengue, watch the phase, not only the platelets. In acidosis, compute the gap before you treat the number.}}\n'
               '\n{{fig:apn03_b}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Fix the order and the template.</strong> For maintenance fluid in a ward child outside the AAP exclusions, choose an '
               'isotonic solution with dextrose and potassium as the unit protocol sets. For a child in an excluded group, such as one with '
               'kidney failure or polyuric tubular disease, write the fluid from the child&rsquo;s measured losses and urine. Then ask the ward to '
               'change the template that produced the hypotonic order.</p>\n'
               '<p><strong>Measure.</strong> Weigh the child daily, or twice daily in an infant. Check sodium before starting maintenance fluid '
               'and again within the first day, sooner if the child is vomiting, has lung or brain disease, or is post-operative. A urine sodium '
               'and osmolality, sent before treatment, help tell you whether ADH is on.</p>\n'
               '<p><strong>Treat symptoms, then slow down.</strong> A seizing or obtunded child with acute hyponatremia needs hypertonic saline '
               'now, as the unit protocol and a pediatric formulary set, with sodium checked frequently. Once symptoms resolve, stop the '
               'hypertonic infusion and keep the subsequent rise within the limits above, more cautiously in a child whose hyponatremia was '
               'chronic or unknown in duration. Watch for a sudden water diuresis as ADH switches off, which can overcorrect the sodium quickly.</p>\n'
               '<p><strong>Hypernatremia.</strong> Replace the free-water deficit over a period long enough for brain cells that have gained '
               'solutes to lose them, as the unit protocol sets, and rule out diabetes insipidus in a child with dilute urine despite a high '
               'sodium.</p>\n'
               '{{flow:A falling sodium in a ward child|Is the child symptomatic::Headache, vomiting, lethargy, seizure, low consciousness. If '
               'yes, treat as an emergency now.|Acute or chronic::Documented for less than 48 hours, or after hospital fluids, is acute; unknown '
               'duration is treated as chronic for the speed of correction.|What fluid is running::Stop any hypotonic infusion; change to '
               'isotonic.|What is ADH doing::Urine osmolality and sodium, sent before treatment if possible.|Set the limits::Write the target '
               'rise for the first hour and the ceiling for 24 hours, and how often sodium is checked.|Watch the turn::Urine output and sodium '
               'every few hours; act early on a water diuresis.}}\n'
               '{{call:<ul><li>Any seizure, reduced consciousness or vomiting with headache in a child whose sodium is falling</li><li>Sodium '
               'rising faster than the written ceiling</li><li>A sudden large urine output after hyponatremia</li><li>Dengue in the recovery '
               'phase with effusions, rising blood pressure or oxygen need</li></ul>}}\n'
               '<div class="tc-scene"><span class="tc-lab">After surgery &middot; fictional</span><p>Jun-jun, 7, had an appendectomy yesterday '
               'and is on a hypotonic template. His sodium has gone from 138 to 129 mmol/L, and he complains of a headache. The surgeon writes '
               '&ldquo;observe.&rdquo;</p><p>You change the fluid to an isotonic solution, ask for a sodium every four to six hours, and '
               'explain to the surgical resident why pain and opioids switch on ADH.</p><p class="tc-scene-take"><b>What this shows.</b> '
               'Headache with a falling sodium after surgery is encephalopathy until proven otherwise.</p></div>\n'
               '{{key:Write the sodium plan as three numbers: the target for the first hour, the ceiling for 24 hours, and how often you '
               'check.}}\n')],
 'debrief': ['<p><strong>Why it fell.</strong> Gastroenteritis, vomiting and volume depletion switched on ADH. Andrea then received free '
             'water in a hypotonic maintenance fluid plus replacement, and her kidneys kept it. Her sodium fell 13 mmol/L in under a day: acute '
             'hyponatremia with encephalopathy. Fluid restriction lowers future free-water intake but does nothing to shrink a swollen brain '
             'tonight. Moritz and Ayus are explicit that hyponatremic encephalopathy should never be managed with fluid restriction alone.</p>\n',
             '<p><strong>The next hour and after.</strong> Stop the hypotonic fluid. Ask the resident to give hypertonic saline now, prepared '
             'by the pharmacy from stock according to the hospital&rsquo;s pediatric protocol and formulary, aiming for a rise of about 5 mmol/L '
             'and resolution of symptoms, with sodium rechecked frequently and a blood glucose checked. Because her hyponatremia is acute, the '
             'brain has not adapted, and the risk of osmotic demyelination is lower than in a chronic case; still, write the ceiling of 10 '
             'mmol/L for the first 24 hours and watch for a water diuresis as her volume is restored. Discuss transfer with the PICU two hours '
             'away if she does not wake fully or seizes again.</p>\n',
             '<p><strong>From now on.</strong> Once she is stable, maintenance fluid should be isotonic with dextrose and potassium, as the AAP '
             'recommends for her age group, with ongoing losses replaced measure for measure and daily weights. Tell her grandmother, plainly, '
             'that the type of drip contributed and that it has been changed. Then ask the ward to replace the hypotonic template so the next '
             'child does not need a 3 a.m. call.</p>\n'],
 'skills': {'title': 'Fluids, sodium and acid-base in children',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Identifies ADH-stimulating conditions and selects isotonic maintenance fluid within the AAP 2018 scope', False),
                      ('Leads the first hour of hyponatremic encephalopathy using the unit protocol, with written correction limits', False),
                      ('Adjusts fluid through the febrile, critical and recovery phases of dengue', False),
                      ('Classifies metabolic acidosis using the albumin-corrected anion gap and the urine anion gap', False)],
            'placement': 'Pediatric ward, emergency department or simulation'},
 'quiz': [('Why do hypotonic maintenance fluids cause hyponatremia in hospitalized children?',
           ['They contain too much potassium',
            'Illness switches on ADH, so the kidney retains the free water infused',
            'They cause sodium loss in the stool',
            'They increase aldosterone'],
           1,
           'Non-osmotic ADH release from vomiting, pain, volume depletion and lung or brain disease means infused free water is kept.'),
          ('Which statement matches the AAP 2018 maintenance fluid guideline?',
           ['Hypotonic fluids are preferred for children under 5',
            'It applies to all neonates in intensive care',
            'It applies equally to children with renal dysfunction',
            'Isotonic solutions are recommended for ages 28 days to 18 years, with evidence quality A and a strong recommendation'],
           3,
           'The guideline excludes neonates under 28 days, renal dysfunction and other groups, where fluids must be individualized.'),
          ('What did the PIMS trial show?',
           ['Hyponatremia in 4% with sodium 140 mmol/L versus 11% with sodium 77 mmol/L',
            'More cerebral edema with isotonic fluid',
            'No difference in hyponatremia',
            'Higher mortality with isotonic fluid'],
           0,
           'PIMS, a double-blind RCT, found 12 of 319 versus 35 of 322 children developed hyponatremia; no cerebral edema occurred in either group.'),
          ('A child is seizing with acute hyponatremia. What is the correct immediate principle?',
           ['Fluid restriction alone',
            'Rapid oral salt tablets',
            'Hypertonic saline per the unit protocol to raise sodium promptly, with frequent checks',
            'Wait for a repeat sample in the morning'],
           2,
           'Hyponatremic encephalopathy is an emergency; hypertonic saline reverses brain swelling. Restriction alone does not.'),
          ('In which dengue phase is fluid overload most likely to appear?',
           ['The incubation period',
            'The recovery phase, when leaked fluid returns to the circulation',
            'The first day of fever',
            'Before any fever'],
           1,
           'WHO describes reabsorption of leaked fluid in recovery; children given generous fluid during the leak can become overloaded.')],
 'terms': [('AAP', 'American Academy of Pediatrics'),
           ('ADH', 'Antidiuretic hormone (arginine vasopressin)'),
           ('PICU', 'Pediatric intensive care unit'),
           ('PIMS', 'Trial name: Melbourne randomized trial of 140 versus 77 mmol/L sodium maintenance fluid'),
           ('RCT', 'Randomized controlled trial'),
           ('WHO', 'World Health Organization')],
 'readings': [('dysnatremia.html', 'Dysnatremia: When Blood Sodium Is Too Low or Too High'),
              ('dengue-aki-kidney.html', 'Dengue & Your Kidneys — When Fever Becomes a Kidney Emergency'),
              ('metabolic-acidosis-ckd.html', 'Metabolic Acidosis in CKD — The Silent Bicarbonate Drop Linked to Faster Kidney Loss')],
 'calcs': ['calc-holliday-segar.html', 'calc-maintenance-fluids.html', 'calc-pediatric-dehydration.html', 'calc-sodium-correction-rate.html', 'calc-anion-gap-acid-base.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
