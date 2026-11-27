# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 14: The newborn kidney and neonatal AKI.
Written November 27, 2026 in the voice of the Physician on Duty modules, to the medical teaching standard, for Philippine practice.
Numbers checked against the PubMed abstracts of AWAKEN (Jetton 2017), Baby NINJA (Stoops 2019), Harer 2018, Nourse 2021 (ISPD
pediatric acute PD), CARPEDIEM (Ronco 2014) and Nidus (Coulthard 2014); neonatal staging against the Selewski 2015 review. No doses."""

MODULE = {'image_alt': 'A pediatric nephrologist and a neonatologist review a urine output chart beside an incubator holding a tiny preterm infant.',
 'objectives': ['Interpret serum creatinine and urine output in the first weeks of life, accounting for maternal creatinine, gestational age and '
                'immature tubular function, and stage neonatal AKI with the neonatal modified KDIGO criteria.',
                'Lead nephrotoxin stewardship in the neonatal intensive care unit, using the AWAKEN and Baby NINJA evidence with its limits.',
                'Choose kidney replacement for a newborn when it is needed, from acute peritoneal dialysis to small-infant machines, within what '
                'your hospital can safely deliver.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the consultant the neonatal intensive care unit (NICU) calls</span>In most Philippine hospitals the '
        'neonatologist owns the baby and you are the consultant who is asked, often late, whether a creatinine &ldquo;is normal for a preemie.&rdquo; '
        'Your duty is to read the number against the baby&rsquo;s age, to name acute kidney injury (AKI) when it is present, to change the '
        'drug chart with the neonatologist and pharmacist, and to plan dialysis honestly when it is needed and possible. You also own the '
        'follow-up of a kidney that started life short of nephrons.</div>\n'
        '{{plain:Think of a newborn&rsquo;s creatinine as the water level in a tank that was filled by the mother. At birth the level is the '
        'mother&rsquo;s; over the next days it should drain as the baby&rsquo;s own kidneys open the outlet. A level that stops falling, or rises, '
        'means the outlet is blocked.}}\n'
        '<p>The picture has a limit. The outlet does not open at a fixed speed. A baby born at 28 weeks drains far more slowly than a term '
        'baby, and in the first days the preterm creatinine can even rise a little as the immature tubule reabsorbs creatinine back into the '
        'blood. So you judge each value against the baby&rsquo;s own previous lowest value and gestational age, not against an adult range '
        'and not against a single number.</p>\n'
        '{{cards:Key numbers|Neonatal AKI, stage 1 (neonatal modified KDIGO)::Creatinine rise &ge;0.3 mg/dL within 48 h, or 1.5&ndash;1.9 times '
        'the lowest previous value within 7 days|Stage 3::&ge;3 times the lowest previous value, or creatinine &ge;2.5 mg/dL, or dialysis|AWAKEN '
        '(2,022 NICU infants)::AKI in 29.9%; adjusted odds of death 4.6|Baby NINJA (single-center quality project)::Nephrotoxin-associated AKI '
        '30.9% to 11.0%|CARPEDIEM machine::Circuit priming volume under 30 mL}}\n'
        '<p>Most neonatal AKI is nonoliguric, multifactorial and quiet, and it is found only by someone who looks at the creatinine trend and '
        'the drug chart together. A few babies need dialysis, usually peritoneal. Your work is to make the creatinine mean something, to remove '
        'the avoidable injuries, and to have a realistic plan for the baby who will not recover without help.</p>\n',
 'case': {'title': 'Day 9 in the NICU',
          'html': '<p>It is day 9 in the NICU of a tertiary government hospital in Davao City. Baby Boy Dela Cruz '
                  'was born at 28 weeks weighing 1,050 g after preterm labor. He is on noninvasive respiratory support and caffeine. A course of '
                  'ibuprofen for a patent ductus arteriosus ended on day 7. He has been on gentamicin for 8 days and vancomycin for 5 days for '
                  'suspected late-onset sepsis; the blood culture remains negative.</p>\n'
                  '<p>His creatinine was 1.1 mg/dL on day 1, fell to 0.8 mg/dL on day 4, and is 1.4 mg/dL today. His urine output over the '
                  'last 24 hours was 0.8 mL/kg per hour; it was above 2 mL/kg per hour last week. His weight is up 90 g in two days, and his '
                  'sodium is 129 mmol/L. The neonatologist calls you: &ldquo;Preemies always have high creatinine. Is this just the '
                  'mother&rsquo;s? And can we keep the gentamicin until tomorrow&rsquo;s level?&rdquo; His father, a seafarer, joins the '
                  'mother on a video call from abroad and asks whether his son&rsquo;s kidneys are failing.</p>\n',
          'questions': ['Is this AKI, and what stage?',
                        'What should change on the drug chart today, and how will you make that stick in this NICU?',
                        'If he needed kidney replacement, what could your hospital offer a 1 kg baby, and what would you tell the parents?']},
 'sections': [('physiology',
               'Physiology',
               'The newborn kidney',
               '<p>Nephrogenesis continues until about 34 to 36 weeks of gestation. A baby born at 28 weeks is born mid-construction: nephrons '
               'continue to form for a short time after birth, but the final number is often lower, and the deepest, oldest nephrons carry most of '
               'the early filtration. After birth, glomerular filtration rises as systemic pressure climbs, renal vascular resistance falls and '
               'renal blood flow increases. That rise is slower the more preterm the baby.[[apn14_1]]</p>\n'
               '<p>Creatinine crosses the placenta, so the creatinine at birth reflects the mother&rsquo;s. A term baby clears it over the first '
               'week or two. A very preterm baby clears it more slowly, and the immature tubule can reabsorb creatinine, so values in the first '
               'days may rise slightly before they fall. That is why the neonatal criteria use the baby&rsquo;s lowest previous value as the '
               'reference, and why a single creatinine in the first 48 hours tells you more about the mother than the baby.[[apn14_1]]</p>\n'
               '<p>The newborn tubule is also immature. Fractional excretion of sodium is high in preterm babies at baseline, so a high value does '
               'not prove tubular injury and a single fractional excretion of sodium (FENa) is hard to read. The concentrating ability is limited, '
               'so urine output may stay normal or high while filtration falls; nonoliguric AKI is common. Sodium handling is fragile in both '
               'directions.</p>\n'
               '<p>Neonatal AKI has typical causes: perinatal asphyxia and low perfusion, sepsis, cardiac surgery, necrotizing enterocolitis, and '
               'drugs. Indomethacin and ibuprofen constrict the afferent arteriole by blocking prostaglandins on which neonatal renal blood flow '
               'depends. Aminoglycosides accumulate in proximal tubular cells. Vancomycin adds tubular toxicity, especially with an aminoglycoside. '
               'Each exposure adds to the last.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Feature of the newborn kidney</th><th>Consequence</th><th>What you see at the '
               'bedside</th></tr></thead><tbody>'
               '<tr><td>Maternal creatinine at birth</td><td>Day 1 value reflects the mother</td><td>A &ldquo;high&rdquo; first creatinine that '
               'falls over days</td></tr>'
               '<tr><td>Slow GFR maturation in preterm babies</td><td>Creatinine falls slowly; drugs clear slowly</td><td>Higher values for longer; '
               'prolonged drug levels</td></tr>'
               '<tr><td>Tubular creatinine back-leak early on</td><td>Small early rises can be physiologic</td><td>A modest rise in the first '
               'days in a very preterm baby</td></tr>'
               '<tr><td>High baseline sodium excretion</td><td>FENa is hard to interpret; hyponatremia is common</td><td>Low sodium with normal '
               'urine output</td></tr>'
               '<tr><td>Prostaglandin-dependent renal blood flow</td><td>Nonsteroidal anti-inflammatory drugs (NSAIDs) lower GFR</td><td>Falling urine output after '
               'ibuprofen or indomethacin for a ductus</td></tr>'
               '<tr><td>Limited concentrating ability</td><td>Nonoliguric AKI</td><td>Rising creatinine with &ldquo;good&rdquo; urine output</td></tr>'
               '</tbody></table></div>\n'
               '{{key:Read every neonatal creatinine against the baby&rsquo;s own lowest previous value and gestational age. The trend is the '
               'test.}}\n'
               '<div class="tc-scene"><span class="tc-lab">On a teleconsult, the &ldquo;high&rdquo; first value &middot; fictional</span><p>A '
               'pediatrician in a provincial hospital in Samar messages you about a term baby, born yesterday, with a creatinine of 1.0 mg/dL. The '
               'baby is feeding, passing urine and well.</p><p>You ask for the mother&rsquo;s creatinine and a repeat on day 3. The mother&rsquo;s '
               'is 0.9 mg/dL; the baby&rsquo;s falls to 0.6 mg/dL by day 3.</p><p class="tc-scene-take"><b>What this shows.</b> A first-day value '
               'is the mother&rsquo;s report card. Judge the baby by the direction of travel.</p></div>\n'),
              ('staging',
               'Staging',
               'Staging neonatal AKI',
               '<p>The Kidney Disease: Improving Global Outcomes (KDIGO) 2012 AKI definition was built mainly for older patients.[[apn14_8]] The '
               'neonatal modified KDIGO criteria, set out by the group that formed the Neonatal Kidney Collaborative, keep the structure but change '
               'two things: the reference creatinine is the lowest previous value, and the absolute creatinine for stage 3 is 2.5 mg/dL instead of '
               '4.0 mg/dL, because a neonatal creatinine of 2.5 mg/dL already corresponds to a very low GFR.[[apn14_1]]</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Stage</th><th>Serum creatinine (neonatal modified KDIGO)</th><th>What it usually means '
               'clinically</th></tr></thead><tbody>'
               '<tr><td>0</td><td>No change, or a rise of less than 0.3 mg/dL</td><td>No AKI by creatinine; keep watching drug exposures</td></tr>'
               '<tr><td>1</td><td>Rise of &ge;0.3 mg/dL within 48 h, or 1.5&ndash;1.9 times the lowest previous value within 7 days</td><td>Early '
               'injury; often reversible if the cause is removed</td></tr>'
               '<tr><td>2</td><td>2.0&ndash;2.9 times the lowest previous value</td><td>Significant loss of function; drug dosing must change</td></tr>'
               '<tr><td>3</td><td>&ge;3 times the lowest previous value, or &ge;2.5 mg/dL, or receipt of dialysis</td><td>Severe AKI; fluid and '
               'electrolyte balance at risk; think about dialysis</td></tr>'
               '</tbody></table></div>\n'
               '<p>Urine output criteria in neonates are less settled. Published versions differ, and several set the oliguria threshold higher '
               'than in older children, because newborns normally pass more urine per kilogram. AWAKEN used urine output below 1 mL/kg per hour on '
               'postnatal days 2 to 7 as its urine criterion.[[apn14_2]] Use the version your NICU has adopted, and measure urine properly: '
               'weighed diapers, recorded at fixed times, are the usual method in a ward without catheters.</p>\n'
               '<p>Two traps. First, a baby whose creatinine has stopped falling may have AKI before it rises, because the expected fall did not '
               'happen. Second, fluid overload dilutes creatinine and can hide AKI; weight gain and hyponatremia, as in the case, are warnings.</p>\n'
               '{{flow:Reading a neonatal creatinine|Find the reference::The lowest creatinine recorded so far, not the day 1 value.|Compare::Rise of '
               '&ge;0.3 mg/dL in 48 h or &ge;1.5 times the reference in 7 days is stage 1 or more.|Check the expected course::A value that has '
               'stopped falling in a baby who should be clearing maternal creatinine deserves the same attention.|Add urine output and weight::Weighed '
               'diapers at fixed times; weight gain can dilute creatinine.|Look at the drug chart::Aminoglycoside, vancomycin, ibuprofen or '
               'indomethacin, contrast, other nephrotoxins.|Write the stage::Record the stage, the reference value and the date in the chart.}}\n'
               '{{key:Name the stage, write down the reference value, and say which drugs and exposures are contributing. A stage without a cause is '
               'only half a consultation.}}\n'
               '<div class="tc-scene"><span class="tc-lab">At the morning NICU round, a creatinine that stopped falling &middot; fictional</span>'
               '<p>A 31-week baby in Cagayan de Oro had creatinine values of 1.0, 0.9 and 0.9 mg/dL on days 2, 5 and 8. The resident reports that '
               'there is no AKI because the value never rose. The baby has had a week of amikacin and a course of indomethacin.</p><p>You point '
               'out that at 31 weeks the creatinine should still be falling, look at the diaper weights (lower than last week), and ask for a '
               'review of both drugs and a repeat in 48 hours.</p><p class="tc-scene-take"><b>What this shows.</b> In a newborn, a plateau can be '
               'the first sign of injury. The expected course is part of the reference.</p></div>\n'
               '\n{{fig:apn14_a}}\n'),
              ('evidence',
               'Evidence',
               'What the evidence shows',
               '<p><strong>How common, and how dangerous.</strong> The Assessment of Worldwide Acute Kidney Injury Epidemiology in Neonates '
               '(AWAKEN) study screened 4,273 babies admitted to 24 NICUs in Australia, Canada, India and the United States in early 2014 and '
               'included 2,022. AKI occurred in 605 (29.9%): 47.9% of babies born at 22 to under 29 weeks, 18.3% at 29 to under 36 weeks, and 36.7% '
               'at 36 weeks or more. Death occurred in 9.7% of babies with AKI and 1.4% without; after adjustment, the odds of death were 4.6 times '
               'higher (95% confidence interval 2.5 to 8.3), and hospital stay was 8.8 days longer.[[apn14_2]] AWAKEN was observational. It shows '
               'that AKI marks babies at high risk; it does not prove that preventing AKI would save those lives, because sicker babies have both.</p>\n'
               '<p><strong>Can nephrotoxic AKI be prevented?</strong> Baby NINJA (Nephrotoxic Injury Negated by Just-in-Time Action) was a '
               'single-center quality improvement project in a level IV NICU from 2015 to 2017. Babies with high-risk exposure, defined as three or '
               'more nephrotoxic drugs within 24 hours or four or more calendar days of an intravenous aminoglycoside, had daily creatinine until two '
               'days after the exposure or the AKI ended. Comparing the initiation and sustainability eras, high-risk exposures fell from 16.4 to 9.6 '
               'per 1,000 patient-days, the proportion of AKI attributable to nephrotoxins fell from 30.9% to 11.0%, and AKI intensity fell from '
               '9.1 to 2.9 days per 100 susceptible patient-days; the authors estimated 100 AKI episodes prevented in 18 months.[[apn14_3]] A '
               'before-and-after design at one well-resourced center is vulnerable to secular trends, and long-term kidney outcomes were not '
               'measured. The finding that matters for you is that a simple surveillance rule, run by pharmacists and nurses, changed exposure.</p>\n'
               '<p><strong>Caffeine.</strong> In a secondary analysis of AWAKEN including 675 babies born before 33 weeks, AKI in the first 7 days '
               'occurred in 11.2% of those who received caffeine and 31.6% of those who did not; the adjusted odds ratio was 0.20 (0.11 to '
               '0.34).[[apn14_4]] Caffeine is given for apnea, not for the kidney, and babies who receive it may differ from those who do not in '
               'ways the adjustment cannot capture. The study supports caffeine&rsquo;s safety for the kidney and suggests a protective effect, '
               'possibly through adenosine-receptor blockade and afferent vasodilation; it does not justify caffeine as a kidney drug.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Study</th><th>Design and size</th><th>Main finding</th><th>What it does not show</th>'
               '</tr></thead><tbody>'
               '<tr><td>AWAKEN</td><td>Observational, 24 NICUs, 2,022 babies</td><td>AKI 29.9%; adjusted odds ratio (OR) for death 4.6</td><td>That preventing '
               'AKI lowers mortality</td></tr>'
               '<tr><td>Baby NINJA</td><td>Single-center before-and-after quality project</td><td>Nephrotoxin-associated AKI 30.9% to 11.0%</td>'
               '<td>Long-term kidney outcomes; generalizability to low-resource NICUs</td></tr>'
               '<tr><td>Caffeine and AKI (AWAKEN secondary analysis)</td><td>Observational, 675 babies under 33 weeks</td><td>AKI 11.2% vs 31.6%; '
               'adjusted OR 0.20</td><td>That caffeine should be given to protect the kidney</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>After discharge.</strong> KDIGO 2012 advises evaluating patients about 3 months after AKI for recovery or new CKD '
               '(ungraded).[[apn14_8]] Babies born preterm, with or without AKI, start life with fewer nephrons, and the neonatal review calls '
               'for long-term follow-up of babies with AKI to find those who develop chronic kidney disease (CKD).[[apn14_1]]</p>\n'
               '{{key:AKI marks the NICU babies who die, and nephrotoxin exposure is the part of it you can change. Count exposures every day.}}\n'),
              ('practice',
               'Practice',
               'What the attending does',
               '<p><strong>Make stewardship a system.</strong> You cannot round in every NICU every day. A rule can. Agree with the neonatologist and '
               'pharmacist on a daily trigger list (three or more nephrotoxins in 24 hours, or a fourth day of an intravenous aminoglycoside, as Baby '
               'NINJA used), a daily creatinine for flagged babies, and a standing question for each flagged baby: is each drug still needed, is there '
               'a less nephrotoxic option, and is the dose and interval adjusted to the current kidney function? Doses and levels come from the '
               'NICU formulary and pharmacist, not from you by phone.</p>\n'
               '<p><strong>Treat the AKI you find.</strong> Restore perfusion, stop or substitute nephrotoxins, adjust every renally cleared drug, '
               'restrict fluid to insensible losses plus output when the baby is overloaded, correct sodium slowly, watch potassium and calcium, and '
               'image the kidneys and bladder with ultrasound to exclude obstruction and structural disease. Protect nutrition; a starved baby '
               'catabolizes and raises potassium and urea.</p>\n'
               '<p><strong>Fluid and sodium.</strong> A baby with AKI and rising weight needs total fluid matched to insensible losses plus urine '
               'output, recalculated at least daily, with the neonatologist owning the nutrition plan inside that limit. Hyponatremia in a gaining '
               'baby is usually dilutional and is treated by restricting free water, not by adding sodium; hyponatremia in a baby losing weight '
               'with high urine sodium is tubular loss and needs sodium. Weights twice a day where the scale allows are the best single guide. '
               'Potassium-free fluids, calcium checks and early recognition of hyperkalemia (a squeezed heel stick can give a falsely high value) '
               'complete the basics.</p>\n'
               '<p><strong>Know when dialysis is needed.</strong> Refractory hyperkalemia or acidosis, fluid overload that compromises breathing or '
               'blocks nutrition, and severe uremia are the usual reasons. For a newborn, peritoneal dialysis (PD) is the most widely available '
               'option. The International Society for Peritoneal Dialysis (ISPD) 2020 pediatric acute PD guideline rates PD as a suitable therapy '
               'for AKI in children (1C), prefers a surgically placed Tenckhoff catheter (1B) with a Seldinger kit as an acceptable alternative '
               '(1C), allows improvised catheters only when nothing else is available (practice point), and notes that automated PD machines do not '
               'suit neonates because the fill volumes are too small (1D). For manual PD in small children it describes a closed system with burettes '
               'to measure fill and drain (practice point), and in neonates and small infants shorter cycles to achieve ultrafiltration (practice '
               'point).[[apn14_5]] The fill, cycle and dextrose orders come from your unit&rsquo;s protocol and the dialysis team.</p>\n'
               '<p><strong>Machines built for babies.</strong> Conventional hemodialysis and continuous kidney replacement therapy (CKRT) circuits '
               'hold a large volume relative to a newborn&rsquo;s blood volume, so they usually need blood priming. Two machines were designed for '
               'small infants. The Cardio-Renal Pediatric Dialysis Emergency Machine (CARPEDIEM) has a priming volume under 30 mL and scales accurate '
               'to 1 g; its first patient was a 2.9 kg neonate with 65% fluid overload who survived.[[apn14_6]] The Newcastle infant dialysis and '
               'ultrafiltration system (Nidus) dialyzed 10 babies weighing 1.8 to 5.9 kg for 2,475 hours without blood priming, through a '
               'single-lumen line, with clearances of about 1.5 to 2.0 mL/min against 0.2 to 0.8 mL/min with PD.[[apn14_7]] Both reports are small '
               'and from expert centers; neither machine is generally available in the Philippines. Module 16 discusses them with CKRT.</p>\n'
               '<div class="table-wrap"><table><thead><tr><th>Option for a newborn</th><th>Strength</th><th>Limitation in a Philippine NICU</th>'
               '</tr></thead><tbody>'
               '<tr><td>Acute PD, manual, closed system with burettes</td><td>No blood circuit, no anticoagulation, gentle fluid removal</td><td>Needs a '
               'catheter and nurses trained in neonatal exchanges; leaks; abdominal surgery or necrotizing enterocolitis (NEC) may preclude it</td></tr>'
               '<tr><td>Acute PD with improvised catheter</td><td>Possible when nothing else exists</td><td>Higher leak and infection risk; a last '
               'resort per ISPD</td></tr>'
               '<tr><td>Conventional CKRT or hemodialysis</td><td>Precise clearance in larger infants</td><td>Blood priming, large catheter relative to '
               'vessel size, hypotension at connection</td></tr>'
               '<tr><td>Small-infant machines (CARPEDIEM, Nidus)</td><td>Small circuit, precise fluid control</td><td>Not widely available; '
               'experience limited to expert centers</td></tr>'
               '</tbody></table></div>\n'
               '<p><strong>Talk to the family honestly.</strong> Parents of a 1 kg baby need to hear what AKI means for their child now, what is '
               'being changed, what dialysis would involve and whether it is realistically available here, and that many babies with mild AKI '
               'recover. When dialysis is not feasible or not in the baby&rsquo;s interest, say so with the neonatologist, and document the '
               'conversation.</p>\n'
               '<p><strong>Plan follow-up.</strong> At NICU discharge, write the AKI stage, the peak and discharge creatinine, the drug exposures and '
               'the follow-up: blood pressure, urinalysis for protein and creatinine at about 3 months and then periodically as the unit sets, with '
               'the family and the pediatrician told why.</p>\n'
               '<div class="tc-scene"><span class="tc-lab">At the NICU pharmacy desk &middot; fictional</span><p>Pharmacist Anne Villanueva prints '
               'a list each morning of babies on three or more nephrotoxins or a fourth aminoglycoside day. On the first morning there are nine. You '
               'agree with the neonatologist to review each one at the 10 a.m. huddle.</p><p>By the end of the month the morning list has three '
               'names, and two babies have had gentamicin stopped on day 3 when cultures came back negative.</p><p class="tc-scene-take"><b>What '
               'this shows.</b> A list printed every morning protects more kidneys than an expert called once.</p></div>\n'
               '{{call:<ul><li>Potassium rising despite treatment, or electrocardiogram (ECG) changes</li><li>Fluid overload limiting ventilation or feeding</li><li>Stage 3 '
               'AKI with anuria</li><li>Creatinine rising in a baby still on an aminoglycoside or vancomycin</li><li>Hyponatremia with seizures</li>'
               '</ul>}}\n'
               '{{key:Every NICU baby with AKI leaves with a stage, a list of exposures, a blood pressure and urine plan, and a named person who '
               'checks the kidney at about 3 months.}}\n'
               '\n{{fig:apn14_b}}\n')],
 'debrief': ['<p><strong>Is it AKI?</strong> Yes. His lowest previous creatinine is 0.8 mg/dL on day 4. A value of 1.4 mg/dL is 1.75 times that '
             'reference within 7 days, which is stage 1 by the neonatal modified KDIGO criteria. It is not maternal creatinine: his own kidneys had '
             'already lowered it, and it has turned upward. The fall in urine output, the weight gain and the low sodium suggest fluid retention '
             'that may be diluting the creatinine, so the true injury may be larger than the stage suggests.</p>\n',
             '<p><strong>The drug chart.</strong> He has had gentamicin for 8 days, vancomycin for 5, and ibuprofen until two days ago, with a '
             'negative blood culture. Ask the neonatologist whether the antibiotics are still needed; if sepsis is not supported, stop them today '
             'rather than wait for a level. If they are needed, ask the pharmacist to adjust dose and interval to his current function and to '
             'follow levels. Check daily creatinine, weighed diapers and sodium; restrict fluids to output and insensible losses if overloaded; '
             'order a kidney and bladder ultrasound. To make it stick, propose a daily trigger list run by the pharmacist, as in Baby NINJA.</p>\n',
             '<p><strong>If he needed dialysis.</strong> For a 1 kg baby the realistic option is acute PD with a closed, burette-measured manual '
             'system, if the abdomen allows and the NICU nurses are trained; conventional circuits would need blood priming and a large catheter, '
             'and small-infant machines are not generally available here. Tell his parents, including his father on the call, that his kidneys '
             'are injured but working, that the drugs that may be harming them are being reviewed today, that most mild injury in babies '
             'improves, and that if dialysis became necessary you would explain exactly what it involves and whether it is right for him.</p>\n'],
 'skills': {'title': 'The newborn kidney and neonatal AKI',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Stages neonatal AKI from a creatinine series using the lowest previous value as reference', False),
                      ('Reviews a NICU drug chart with the pharmacist and documents each nephrotoxin decision', False),
                      ('Explains acute PD for a newborn to a nurse team, including closed burette systems and leak risk', False),
                      ('Writes a NICU discharge kidney follow-up plan with stage, exposures and a 3-month review', False)],
            'placement': 'Supervised NICU consultation or simulation'},
 'quiz': [('A 28-week baby&rsquo;s creatinine was 1.1 mg/dL on day 1, 0.8 mg/dL on day 4 and 1.3 mg/dL on day 8. What is the reference value '
           'for staging?',
           ['1.1 mg/dL, the birth value',
            '0.8 mg/dL, the lowest previous value',
            'The mother&rsquo;s creatinine',
            'An adult normal value'],
           1,
           'The neonatal modified KDIGO criteria use the lowest previous creatinine as the reference, because the birth value reflects the mother.'),
          ('What absolute creatinine defines stage 3 in the neonatal modified KDIGO criteria?',
           ['2.5 mg/dL', '4.0 mg/dL', '1.5 mg/dL', '6.0 mg/dL'],
           0,
           'A neonatal creatinine of 2.5 mg/dL already reflects a very low GFR, so the adult 4.0 mg/dL threshold was lowered.'),
          ('What did AWAKEN show?',
           ['That treating AKI lowers neonatal mortality',
            'That AKI is rare in preterm babies',
            'That AKI occurred in 29.9% of included NICU babies and was associated with higher adjusted odds of death',
            'That caffeine causes AKI'],
           2,
           'AWAKEN was observational: AKI was common and independently associated with death (adjusted OR 4.6), but it does not prove that '
           'prevention saves lives.'),
          ('Which trigger did Baby NINJA use to flag high-risk nephrotoxin exposure?',
           ['Any single antibiotic',
            'A creatinine above 1.5 mg/dL',
            'Urine output below 0.5 mL/kg per hour',
            'Three or more nephrotoxic drugs within 24 hours, or four or more days of an intravenous aminoglycoside'],
           3,
           'Flagged babies had daily creatinine; nephrotoxin-associated AKI fell from 30.9% to 11.0% in this single-center project.'),
          ('Why do automated PD machines not suit most neonates, according to the ISPD 2020 pediatric acute PD guideline?',
           ['They cannot use dextrose solutions',
            'The fill volumes newborns need are too small for currently available machines',
            'They require anticoagulation',
            'They cause hyperkalemia'],
           1,
           'The guideline rates automated PD as suitable for pediatric AKI except in neonates, for whom fill volumes are too small (1D).')],
 'terms': [('AKI', 'Acute kidney injury'),
           ('NICU', 'Neonatal intensive care unit'),
           ('KDIGO', 'Kidney Disease: Improving Global Outcomes'),
           ('AWAKEN', 'Assessment of Worldwide Acute Kidney Injury Epidemiology in Neonates'),
           ('NINJA', 'Nephrotoxic Injury Negated by Just-in-Time Action'),
           ('GFR', 'Glomerular filtration rate'),
           ('FENa', 'Fractional excretion of sodium'),
           ('CKD', 'Chronic kidney disease'),
           ('PD', 'Peritoneal dialysis'),
           ('ISPD', 'International Society for Peritoneal Dialysis'),
           ('CKRT', 'Continuous kidney replacement therapy'),
           ('CARPEDIEM', 'Cardio-Renal Pediatric Dialysis Emergency Machine'),
           ('Nidus', 'Newcastle infant dialysis and ultrafiltration system'),
           ('NEC', 'Necrotizing enterocolitis'),
           ('OR', 'Odds ratio'),
           ('ECG', 'Electrocardiogram')],
 'readings': [('neonatal-acute-kidney-injury-clinician.html', 'Neonatal Acute Kidney Injury — A Clinician Guide to Recognition, Staging, Prevention & Follow-up'),
              ('born-small-kidneys-for-life.html', 'Born Small, Kidneys for Life: Birth History and Kidney Health'),
              ('nsaid-kidney-injury.html', 'How NSAIDs injure the kidney, and safer pain relief')],
 'calcs': ['calc-neonatal-aki.html', 'calc-pediatric-uo.html', 'calc-urine-output-fluid-balance.html', 'calc-fena-feurea.html']}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
