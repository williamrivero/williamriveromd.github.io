# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 20: Pediatric PD: access, membrane and prescription.
Written November 27, 2026 for the Renal Care Academy, in the voice of the Physician on Duty modules and to the medical teaching standard.
Numbers checked against Fischbach & Warady 2009 and Zurowska 2013 (PMC full text), the ISPD 2024 pediatric infection guideline (publisher
full text), IPPN and SCOPE registry abstracts, the Cochrane urgent-start review, and PhilHealth PC 2024-0036 (Tamang Sagot) and PA 2026-0013.
No fill volume, dwell or glucose choice in this file is an order; the unit's pediatric protocol sets the prescription."""

MODULE = {
 'image_alt': 'A Filipino mother holds her infant on a hospital bed while a pediatric dialysis nurse connects a small peritoneal dialysis catheter to a cycler line.',
 'objectives': [
    'Explain why peritoneal dialysis (PD) suits infants and small children, using the peritoneal membrane, the three-pore model and fill volume scaled to body surface area (BSA).',
    'Plan the PD catheter with the surgeon (type, exit site, omentum, break-in) and recognize the early mechanical problems that threaten it.',
    'Review a pediatric PD prescription each month against growth, blood pressure, fluid status and residual urine, treating Kt/V and creatinine clearance as surrogates.'],
 'big': '<div class="tc-keyp"><span class="tc-lab">Your role &middot; the PD prescriber of record</span>You decide with the family that a small child '
        'will start peritoneal dialysis (PD), you agree the catheter plan with the pediatric surgeon, and you write and sign the prescription. In a '
        'PhilHealth-contracted PD program you are also the attending pediatric nephrologist named on the pediatric checklist, so the prescription you '
        'write is the one the claim must match, never the reverse.</div>\n'
        '{{plain:Think of the peritoneum as a sponge-lined room. You pour a measured amount of clean water into the room, let it sit while the walls '
        'trade waste for water, then pour it out. A bigger room needs more water to wet all the walls; a small room floods if you pour too much.}}\n'
        '<p>The picture has a limit. The walls of this room are living tissue. Only part of the anatomic peritoneum touches the fluid at any moment, and how '
        'much it touches depends on posture and on how much fluid you put in. The membrane is a bed of capillaries with pores of three sizes, and glucose '
        'in the fluid leaks away into the blood, so the pull that draws water out fades with every hour of the dwell. A child&rsquo;s peritoneum is large '
        'relative to body weight but similar to an adult&rsquo;s relative to body surface area (BSA), which is why pediatric fill volumes are scaled to '
        'BSA and not simply to kilograms.[[apn20_1]]</p>\n'
        '{{cards:Key numbers|Fill volume scaling::Scale the exchange to BSA (mL/m&sup2;), raised by tolerance and intraperitoneal pressure (IPP) '
        '[Fischbach and Warady 2009]|Children older than 2 years::Fill raised stepwise toward an upper limit of about 1,200&ndash;1,400 mL/m&sup2; for a '
        'night exchange [same source]|Infants::Fill volumes of 600&ndash;900 mL/m&sup2;, IPP ideally below 10 cm H&#8322;O [European Pediatric Dialysis '
        'Working Group 2013]|Tolerated IPP::Normal 7&ndash;14 cm H&#8322;O; upper tolerated limit 18 cm H&#8322;O [Fischbach and Warady 2009]|PD catheter '
        'revisions, International Pediatric Peritoneal Dialysis Network (IPPN) registry::13% of 2,453 children; 60% for mechanical malfunction}}\n'
        '<p>These are ranges described by expert groups, not orders. Your unit&rsquo;s pediatric PD protocol and your own bedside assessment set the '
        'actual fill, dwell and solution for each child.</p>\n'
        '<p>Most small children start PD without trouble once the catheter has healed and the fill is matched to their size. A few leak, drain poorly or '
        'fail to grow on numbers that look adequate. Your work is to put the right catheter in the right place, scale the prescription to the child, and '
        'judge it every month by how the child grows and how the fluid balances, not by a Kt/V alone.</p>\n',
 'case': {'title': 'The leak on day two',
          'html': '<p>Althea Ramos is 10 months old and weighs 7 kg. She has renal dysplasia, and over the past month her urine output has fallen and her '
                  'potassium has risen. Two days ago a pediatric surgeon at a tertiary government hospital in Manila placed a PD catheter under general '
                  'anesthesia. Because her potassium was 6.4 mmol/L and she was gaining weight, the team started small-volume manual exchanges within '
                  '24 hours.</p>\n'
                  '<p>At 6 a.m. the night nurse calls you. The dressing is soaked with clear fluid that tests positive for glucose. The drain volumes are '
                  'smaller than the fills, and Althea cries during filling. The nurse asks, &ldquo;Doctor, can we give a bigger fill so we get more '
                  'out? The drains are so small.&rdquo; Her mother, Rowena, came from Tarlac with Althea&rsquo;s grandmother. She asks whether this means '
                  'the catheter has failed and whether her baby will need to go on the machine with blood.</p>\n',
          'questions': ['What is happening at the exit site, and what will you change now?',
                        'Why is a bigger fill the wrong answer this morning?',
                        'What will you tell Rowena, and what will you review before Althea goes home?']},
 'sections': [
  ('physiology', 'Physiology', 'Why PD fits a small child',
   '<p>Infants and small children have no good vein for long-term hemodialysis (HD), a circuit that holds a large share of their blood volume, and a '
   'blood pressure that falls easily when fluid is removed quickly. PD avoids all three. It uses the child&rsquo;s own peritoneum, needs no blood '
   'outside the body, runs at home, and removes fluid slowly over many hours. The European Pediatric Dialysis Working Group names PD the preferred '
   'kidney replacement therapy (KRT) in infants (graded 1B in its system based on the Kidney Disease Outcomes Quality Initiative [KDOQI]) and notes that it preserves the veins and the residual urine '
   'output.[[apn20_2]]</p>\n'
   '<p><strong>The membrane.</strong> Water and solutes cross the capillary wall through pores of three sizes. The three-pore model describes them: '
   'ultrasmall pores (aquaporins) that let water through without sodium, small pores that carry most diffusion of urea and creatinine, and a few '
   'large pores that let protein leak.[[apn20_1]] Two forces move solute and water. Diffusion follows the concentration gradient, so urea leaves the '
   'blood early in a dwell. Ultrafiltration follows the pressure gradient, which glucose creates and then loses as it is absorbed.</p>\n'
   '<p><strong>Contact area.</strong> Only 30&ndash;60% of the anatomic peritoneum touches the fluid at a time, as measured by computed tomography '
   '(CT) in humans. Recruitment of surface rises with fill volume, until the fill is close to 1,400 mL/m&sup2; in children 2 years and older, and is '
   'greater lying down.[[apn20_1]] A small fill wets a small part of the membrane.</p>\n'
   '<p><strong>The infant illusion.</strong> Small children were once thought to have a &ldquo;leaky&rdquo; membrane, because their test exchanges '
   'equilibrated fast and lost ultrafiltration early. Fischbach and Warady explain this as a geometry problem: a fill prescribed per kilogram is small '
   'relative to a large membrane, so solute equilibrates fast, glucose is absorbed fast and the osmotic pull disappears. Scaling the fill to BSA '
   'removes most of the apparent difference between infants, children and adults.[[apn20_1]]</p>\n'
   '<p><strong>Pressure.</strong> Fluid in the abdomen raises intraperitoneal pressure (IPP). Above a certain pressure the child feels pain and '
   'breathlessness, fluid is pushed into the abdominal wall and along the catheter tunnel, lymphatic absorption rises and net ultrafiltration falls. '
   'The same review lists pain, dyspnea, hydrothorax, hernia, reflux with poor appetite and loss of ultrafiltration as harms of an '
   'excessive fill.[[apn20_1]]</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Mechanism</th><th>What it means in a child</th><th>What you see</th></tr></thead><tbody>'
   '<tr><td>Membrane area similar to adults per m&sup2; of BSA</td><td>Fill per kilogram underfills the membrane</td><td>Fast equilibration, poor '
   'ultrafiltration, &ldquo;high transporter&rdquo; label on a test done with too small a fill</td></tr>'
   '<tr><td>Recruitment rises with fill and supine posture</td><td>Night exchanges lying down tolerate larger fills</td><td>Better clearance on '
   'night cycles than on the day dwell at the same volume</td></tr>'
   '<tr><td>Glucose absorbed during the dwell</td><td>The osmotic pull fades with time</td><td>Long day dwells drain less than they took in</td></tr>'
   '<tr><td>IPP rises with volume</td><td>Each child has a tolerance limit</td><td>Crying at fill, grunting, vomiting, leak, hernia</td></tr>'
   '<tr><td>Urea diffuses fast, phosphate slowly</td><td>Short dwells clear urea, long dwells clear phosphate</td><td>Good Kt/V with a high phosphate '
   'on fast cycling</td></tr></tbody></table></div>\n'
   '{{key:Scale the fill to the child&rsquo;s surface area and check it against the child&rsquo;s tolerance. Volume is the first lever, not the last.}}\n'
   '<div class="tc-scene"><span class="tc-lab">At a test exchange &middot; fictional</span><p>A 4-year-old boy, Kian, is labeled a high transporter '
   'after a peritoneal equilibration test (PET). You check the record: the test fill was the same per-kilogram fill used when he started PD at 13 '
   'months.</p><p>You ask the nurse to repeat the test with the fill the unit protocol sets for a PET, scaled to his BSA. His transport falls into the '
   'average range, and his day dwell is changed.</p><p class="tc-scene-take"><b>What this shows.</b> A PET is only as valid as its fill volume. '
   'Fischbach and Warady describe a test fill of about 1,000&ndash;1,100 mL/m&sup2; as the most valid in children beyond infancy.[[apn20_1]]</p></div>\n'
   '{{fig:apn20_a}}\n'),
  ('access', 'Access', 'The catheter: the child&rsquo;s lifeline for years',
   '<p>A PD catheter in a child may need to last until transplant, and a child who loses PD access early may lose PD altogether. In the IPPN registry, 452 access revisions occurred in 321 of 2,453 children (13%) over 3,134 patient-years, a '
   'rate of 0.14 per treatment year. Among new patients, 83% of revisions came in the first year. Mechanical malfunction caused 60% of revisions, '
   'peritonitis 16%, exit-site infection 12% and leakage 6%. Younger age, congenital anomalies of the kidney and urinary tract (CAKUT), ostomies, and a '
   'swan-neck tunnel with a curled intraperitoneal segment were associated with revision, and needing a revision was associated with more technique '
   'failure or death (hazard ratio 1.35).[[apn20_4]] This is registry evidence; the catheter-design finding is an association, and the children who '
   'received each design differed in other ways.</p>\n'
   '<p><strong>What the guidelines suggest.</strong> The 2024 international pediatric guideline on PD-associated infections suggests a double-cuff '
   'catheter with a downward or lateral exit site (2D, a weak suggestion on very low-quality evidence).[[apn20_3]] For infants, the European Pediatric '
   'Dialysis Working Group recommends surgical insertion with partial omentectomy, an exit site away from the diaper area and from any ostomy, '
   'immobilization of the catheter, and, where possible, a delay of 2&ndash;3 weeks before dialysis so the wound can heal (1C). It notes that '
   'omentectomy is recommended because blockage is common in infants, although its preventive value is unproven, that most centers use single-cuff '
   'catheters below 3 kg and double-cuff catheters at 3&ndash;10 kg, and that fibrin glue at the inner cuff has reduced leaks in one report.[[apn20_2]]</p>\n'
   '<p><strong>Your part in the operating plan.</strong> The surgeon places the catheter; you set the requirements. Mark the exit site with the '
   'family before surgery, with the child sitting and lying, away from the diaper line, a gastrostomy, a vesicostomy or a future stoma. Ask for '
   'contralateral hernia repair if a hernia is present. Agree who dresses the site and when, and who decides the first use.</p>\n'
   '<p><strong>Break-in and urgent start.</strong> Early use is a trade. In the Standardizing Care to Improve Outcomes in Pediatric End Stage Kidney '
   'Disease (SCOPE) collaborative, 98 of 1,106 catheters (8.4%) were followed by peritonitis within 60 days of insertion; early use of the catheter was '
   'associated with this early-onset peritonitis, and use before the first year of life, first catheters, exit-site sutures and early dressing changes '
   'were associated with early use.[[apn20_5]] A Cochrane review of 16 mostly adult studies found that starting PD within 2 weeks of insertion may '
   'increase dialysate leak (one randomized trial of 122 participants: 210 more leaks per 1,000, low certainty); effects on infection, technique and '
   'patient survival were uncertain.[[apn20_6]] Urgent-start PD still saves lives when no other KRT fits: in a 2023 outbreak of Shiga toxin&ndash;'
   'producing <em>E. coli</em> hemolytic uremic syndrome (HUS) in Canada, nine children were dialyzed by urgent-start PD on general wards, beginning '
   'with low fills that were increased as tolerated, and all recovered kidney function.[[apn20_10]] That is a nine-child case series, not a '
   'comparison.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Early problem</th><th>Likely mechanism</th><th>What you do first</th></tr></thead><tbody>'
   '<tr><td>Clear fluid at the exit site, glucose-positive</td><td>Pericatheter leak from early use or high IPP</td><td>Stop or reduce fills as the '
   'protocol allows, lie the child flat, consider a pause or temporary HD; never a bigger fill</td></tr>'
   '<tr><td>Inflow fast, outflow slow</td><td>Constipation, catheter tip displaced, omentum, fibrin</td><td>Treat constipation, abdominal X-ray for '
   'tip position, heparinized flush per protocol</td></tr>'
   '<tr><td>No inflow or outflow</td><td>Kink, clamp, clot</td><td>Check the line and clamps; surgical review if not resolved</td></tr>'
   '<tr><td>Scrotal or labial swelling</td><td>Patent processus vaginalis or hernia</td><td>Reduce fills, surgical review</td></tr>'
   '<tr><td>Bleeding or bloody effluent after insertion</td><td>Operative bleeding</td><td>Rapid in-and-out flushes per protocol; hemoglobin; '
   'surgeon</td></tr></tbody></table></div>\n'
   '{{key:The catheter is placed once and used for years. Choose the exit site with the family, protect the first weeks, and treat every leak as a '
   'pressure problem.}}\n'
   '{{fig:apn20_b}}\n'),
  ('prescription', 'Prescription', 'Building the prescription for a growing child',
   '<p>A PD prescription has five levers: fill volume, dwell time, number of exchanges, total time on dialysis, and the solution. Each moves '
   'something different. The prescription aims at two goals at once: enough ultrafiltration to keep the child euvolemic, and enough removal of '
   'solute, not urea alone, to allow growth and bone health.[[apn20_1]]</p>\n'
   '<p><strong>Continuous ambulatory PD (CAPD) or automated PD (APD).</strong> In CAPD the family does several manual exchanges by day and leaves a '
   'long night dwell. In APD a cycler does short exchanges at night, often with a day dwell. Most children worldwide receive APD, because a full '
   'abdomen is better tolerated lying down, short dwells limit reabsorption, and night treatment leaves the day free for school and the '
   'parents&rsquo; work.[[apn20_1]] Fischbach and Warady describe an initial APD dwell of about 1 hour as typical, to be revised for the child&rsquo;s '
   'growth, residual function and membrane.[[apn20_1]]</p>\n'
   '<p><strong>Infants.</strong> The infant recommendations describe lower fills (600&ndash;900 mL/m&sup2;), shorter dwells (30&ndash;40 minutes), more '
   'exchanges (12&ndash;16) and longer sessions (10&ndash;16 hours) than in older children, with the daytime fill about half the night fill, and '
   'recommend individualizing the prescription to urine output and nutrition (1B).[[apn20_2]] Very small fills bring their own problems: cycler alarms '
   'and a tubing recirculation volume that is large compared with the fill. Infants under about 2&ndash;3 kg with fills below 100 mL are usually '
   'dialyzed manually in hospital.[[apn20_2]]</p>\n'
   '<p><strong>Solutions and glucose.</strong> Use the lowest glucose that achieves the ultrafiltration the child needs, and prefer biocompatible '
   'solutions with neutral pH and low glucose degradation products where available; the infant recommendations grade this 1B, while noting that no '
   'infant trial compares solutions.[[apn20_2]] Icodextrin, a glucose polymer that keeps its osmotic pull for many hours, helps the long day dwell; '
   'it should be used with caution in infants because of reported hyponatremia and rebound hypoglycemia.[[apn20_2]] In the IPPN registry, icodextrin '
   'was used in 724 of 3,573 children (20.3%) on APD with a day dwell; children who started it within the first year had better blood pressure and '
   'slower loss of residual function than glucose-only matched children, and late starters had a higher risk of technique failure or death than early '
   'starters (hazard ratio 5.16).[[apn20_8]] This was a propensity-matched observational analysis and does not prove that early icodextrin causes the '
   'better outcomes.</p>\n'
   '<p><strong>Sodium.</strong> Frequent short exchanges remove water with little sodium, because aquaporins move water without salt early in the '
   'dwell. Infants with salt-losing dysplasia lose more sodium in urine. Many infants need sodium supplements, which may help growth, and serum sodium '
   'reflects sodium status poorly.[[apn20_2]] A low sodium, poor weight gain and a low blood pressure in an infant on PD point to salt depletion, not to '
   'a need for less dialysis.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Lever</th><th>What it mostly changes</th><th>What you watch</th></tr></thead><tbody>'
   '<tr><td>Fill volume (scaled to BSA)</td><td>Membrane recruitment, urea removal, ultrafiltration</td><td>Comfort, IPP, leaks, hernia, breathing, '
   'reflux</td></tr>'
   '<tr><td>Dwell time</td><td>Short: urea and water; long: creatinine and phosphate</td><td>Phosphate, net ultrafiltration of the day dwell</td></tr>'
   '<tr><td>Number of exchanges and hours</td><td>Total clearance</td><td>Sleep, family fatigue, cost of solution</td></tr>'
   '<tr><td>Glucose concentration</td><td>Ultrafiltration</td><td>Blood sugar, weight gain from absorbed glucose, membrane injury over time</td></tr>'
   '<tr><td>Icodextrin for the long dwell</td><td>Sustained ultrafiltration</td><td>Sodium and glucose in infants, rash, residual urine</td></tr>'
   '<tr><td>Sodium supplement</td><td>Extracellular volume and growth in salt-losing infants</td><td>Weight gain, blood pressure, edema</td></tr>'
   '</tbody></table></div>\n'
   '<div class="tc-scene"><span class="tc-lab">On a monthly review &middot; fictional</span><p>Ezekiel, 3 years old on nightly APD, has a weekly Kt/V '
   'that the nurse calls &ldquo;excellent&rdquo;, but his phosphate is high and his height is falling across centiles. His cycler runs many short '
   'exchanges and no day dwell.</p><p>You add a day dwell within the unit&rsquo;s protocol and ask the dietitian to review his phosphate intake. His '
   'phosphate settles over two months.</p><p class="tc-scene-take"><b>What this shows.</b> Short dwells clear urea well and phosphate poorly. The time '
   'needed for phosphate to equilibrate is three to four times that for urea.[[apn20_1]]</p></div>\n'
   '{{key:Each lever moves something different. Name the problem first (fluid, urea, phosphate, sodium, comfort) and then move the lever that fixes '
   'it.}}\n'),
  ('evidence', 'Evidence', 'What the evidence shows, and how firm it is',
   '<p>Pediatric PD rests on expert consensus, physiology and registries. There are almost no randomized trials, so most recommendations carry grade '
   '1C to 2D in the systems their authors use, or no grade at all. Read each one for what it is.</p>\n'
   '<p><strong>Fill volume and pressure.</strong> The scaling of fill to BSA, the 1,200&ndash;1,400 mL/m&sup2; upper range in children over 2, the '
   'suggested upper fill of 800 mL/m&sup2; (or 30&ndash;50 mL/kg) in infants under 2 with tolerance as the deciding factor, and the IPP values come '
   'from physiological studies and a narrative review, not from trials.[[apn20_1]] They are reasonable starting rules, and tolerance in the individual '
   'child overrides them.</p>\n'
   '<p><strong>Transport, dialysis dose and growth.</strong> In a prospective cohort of 51 children followed for 18 months, a faster creatinine '
   'equilibration on the first PET correlated with less gain in height standard deviation score (SDS) (r = &minus;0.31), and higher dialytic '
   'creatinine clearance was associated with better height gain.[[apn20_7]] The effects were modest (partial r&sup2; 0.07 and 0.11) and the design '
   'cannot show that changing the prescription changes growth. It is still one of the few studies to link PD mechanics to the outcome children and '
   'parents care about.</p>\n'
   '<p><strong>Adequacy numbers.</strong> Weekly Kt/V (urea clearance scaled to body water) and weekly creatinine clearance are surrogates. Infants on '
   'frequent short exchanges often show a high Kt/V with a low creatinine clearance; the infant recommendations accept this if the child is '
   'biochemically stable and growing, and name appropriate growth and development as the most important measure of adequacy (1C).[[apn20_2]] The 2020 '
   'International Society for Peritoneal Dialysis (ISPD) recommendations on prescribing high-quality goal-directed PD moved away from solute targets '
   'toward person-centered goals reached by shared decision-making, and labeled their statements practice points rather than graded recommendations, '
   'as a United States commentary by the Kidney Disease Outcomes Quality Initiative (KDOQI) explains.[[apn20_9]] This module therefore gives no pediatric Kt/V '
   'target. Follow your unit&rsquo;s protocol for measurement and thresholds, and read the number next to the growth chart.</p>\n'
   '<p><strong>Catheter outcomes.</strong> IPPN registry data show catheter survival in new patients of 84% at 12 months and 73% at 48 '
   'months.[[apn20_4]] SCOPE data link early use with early peritonitis.[[apn20_5]] Both are observational.</p>\n'
   '<p><strong>Coverage.</strong> Under PhilHealth Circular 2024-0036, the Z benefits package for PD covers CAPD for children and, for automated PD, '
   'a pilot in selected facilities. The package defines coverage in tiers of solution bags per day, plus catheter insertion and PD initiation, '
   'exit-site and peritonitis prevention care, outpatient treatment of PD peritonitis, and monthly monitoring.[[apn20_11]] The pediatric APD pilot was '
   'extended to July 31, 2026 by Advisory 2026-0013; its status after that date is unresolved, so confirm it with your PhilHealth liaison before '
   'promising a family APD coverage.[[apn20_12]] A coverage tier is not a prescription. Prescribe what the child needs, document it truthfully, and '
   'confirm the benefit on the date of service.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>Statement</th><th>Source and grade</th><th>What it does not show</th></tr></thead><tbody>'
   '<tr><td>PD is the preferred KRT in infants</td><td>Infant recommendations, 1B[[apn20_2]]</td><td>No randomized comparison with HD</td></tr>'
   '<tr><td>Double-cuff catheter, downward or lateral exit</td><td>2024 pediatric infection guideline, 2D[[apn20_3]]</td><td>Effect size in '
   'children</td></tr>'
   '<tr><td>Omentectomy, exit away from diaper, 2&ndash;3 week delay in infants</td><td>Infant recommendations, 1C[[apn20_2]]</td><td>Proven '
   'preventive value of omentectomy</td></tr>'
   '<tr><td>Growth is the main measure of adequacy in infants</td><td>Infant recommendations, 1C[[apn20_2]]</td><td>A target Kt/V that improves '
   'growth</td></tr>'
   '<tr><td>Person-centered, goal-directed PD prescription</td><td>ISPD 2020, practice points (ungraded)[[apn20_9]]</td><td>Trial evidence for any '
   'solute target</td></tr></tbody></table></div>\n'
   '{{key:In pediatric PD, most rules are expert consensus. Quote the grade with the source and let the child&rsquo;s growth decide.}}\n'),
  ('practice', 'Practice', 'What the attending reviews every month',
   '<p>The monthly review is where the prescription is tested. The infant recommendations describe visits every two weeks for young infants, '
   'extended to every 3&ndash;4 weeks in older infants who are growing well, with weight, length and head circumference plotted at each visit and '
   'daily home records of weight, blood pressure, urine output, ultrafiltration and feeds.[[apn20_2]] In a Philippine program the review often '
   'happens partly by phone or Viber with photographs of the home log; make sure the face-to-face visits still happen at the interval your unit '
   'sets.</p>\n'
   '<div class="table-wrap"><table><thead><tr><th>What you review</th><th>Why it matters</th><th>What makes you change something</th></tr></thead><tbody>'
   '<tr><td>Growth chart: weight, length or height, head circumference in infants</td><td>The outcome that matters most in a small child</td><td>Falling '
   'height SDS, weight gain that is fluid not tissue</td></tr>'
   '<tr><td>Blood pressure against percentiles, edema, home weights</td><td>Fluid status and cardiovascular risk</td><td>Rising pressure, edema, weight '
   'jumps between visits</td></tr>'
   '<tr><td>Residual urine volume</td><td>Clearance and fluid allowance; it helps feeding</td><td>Falling output: re-check fluid allowance and '
   'nephrotoxins</td></tr>'
   '<tr><td>Home log: fill, drain and net ultrafiltration by exchange; alarms</td><td>Mechanics and technique</td><td>Drains smaller than fills, '
   'frequent cycler alarms</td></tr>'
   '<tr><td>Sodium, potassium, bicarbonate, calcium, phosphate, parathyroid hormone (PTH), albumin, hemoglobin</td><td>Metabolic control for growth '
   'and bone</td><td>Low sodium in an infant, high phosphate on fast cycling, low potassium</td></tr>'
   '<tr><td>Kt/V and creatinine clearance, PET when indicated</td><td>Surrogates that explain a problem</td><td>A discrepancy that fits poor growth or '
   'poor phosphate control</td></tr>'
   '<tr><td>Exit site photograph and score</td><td>Infection prevention</td><td>Any score above zero (see Module 22)</td></tr>'
   '<tr><td>Feeding route and dietitian plan</td><td>Most infants need tube feeds to grow</td><td>Vomiting, reflux, poor intake</td></tr>'
   '<tr><td>The caregiver</td><td>The family is the dialysis unit at home</td><td>Exhaustion, missed exchanges, money for transport and solutions</td></tr>'
   '</tbody></table></div>\n'
   '{{flow:When a small child&rsquo;s PD is not working|Name the problem::Fluid overload, poor clearance, poor growth, leak, poor drain, or the family '
   'cannot cope.|Rule out mechanics first::Constipation, catheter position, kinks, leaks. A poor drain is not a membrane problem until proven '
   'otherwise.|Check the fill against BSA and tolerance::Too small a fill looks like a fast membrane; too large a fill leaks and is reabsorbed.|Match dwell '
   'to the solute::Short dwells for water and urea, a long dwell for phosphate and creatinine.|Look at sodium and residual urine::Salt-losing infants need '
   'sodium; a falling urine output changes the whole fluid plan.|Write the change and the date to re-check::One change at a time, with the measure that '
   'will show it worked.}}\n'
   '<div class="tc-scene"><span class="tc-lab">By Viber, Sunday night &middot; fictional</span><p>A father in Batangas sends a photograph of his '
   'son&rsquo;s cycler log: three &ldquo;low drain&rdquo; alarms and a net ultrafiltration that has dropped by half. The boy has not passed stool in '
   'three days.</p><p>You advise the unit&rsquo;s constipation plan for PD, ask the father to log the next two nights and send the drain volumes, and '
   'book an abdominal X-ray if drains do not recover.</p><p class="tc-scene-take"><b>What this shows.</b> Constipation is the commonest reversible '
   'cause of poor drainage. Treat it before anyone blames the membrane.</p></div>\n'
   '{{key:Review growth, fluid and the family before the numbers. A Kt/V explains a problem; it does not prove there is none.}}\n'
   '{{call:<ul><li>Fluid leaking at the exit site or swelling of the abdominal wall, scrotum or labia</li><li>Breathlessness or a pleural effusion on a '
   'child on PD (possible hydrothorax)</li><li>Cloudy effluent, abdominal pain or fever (see Module 22)</li><li>No outflow after constipation is '
   'treated</li><li>An infant with falling sodium, poor feeding or weight loss</li></ul>}}\n'
   '{{fig:apn20_c}}\n'),
 ],
 'debrief': [
    '<p><strong>The exit site.</strong> Glucose-positive clear fluid at the exit site is dialysate: a pericatheter leak in a catheter used within a day '
    'of insertion, in a 7 kg infant whose abdominal wall has not healed. Leaks are a known cost of early use, and the infant recommendations favor '
    'waiting 2&ndash;3 weeks where possible. Stop or reduce the fills as your protocol allows, keep her flat and dressed with a sterile dressing, and '
    'decide with the surgeon whether to rest the catheter. If her potassium or fluid status cannot wait, temporary HD or a short pause with medical '
    'management of potassium may be safer than pushing fluid through a leaking tunnel. Document the leak; a leak raises the risk of tunnel infection '
    'and peritonitis.</p>\n',
    '<p><strong>Why not a bigger fill.</strong> Small drains in this setting do not mean too little dialysis. Fluid is escaping through the tunnel and '
    'the abdominal wall, and she cries at filling because the pressure is already above her tolerance. A larger fill raises IPP further, widens the '
    'leak, can cause a hernia and is partly absorbed by lymphatics, so the net drain may fall. In infants the expert range is 600&ndash;900 mL/m&sup2; '
    'with IPP ideally below 10 cm H&#8322;O, and the fill is raised slowly once the catheter has healed and only as the child tolerates it.</p>\n',
    '<p><strong>Rowena.</strong> Tell her plainly: the catheter has not failed. A leak in the first days is common in babies, it usually seals if the '
    'catheter rests, and PD remains the best dialysis for a baby Althea&rsquo;s size. If a few HD sessions are needed while the wound heals, say so and '
    'explain why. Before discharge, review a home plan you can check every month: her growth chart, home weights and blood pressure, urine output, '
    'drain log, sodium and feeding plan, the exit site, and how Rowena and the grandmother will share the night work. Confirm the PhilHealth PD '
    'package enrollment with the program coordinator, and do not let the coverage tier decide her prescription.</p>\n'],
 'skills': {'title': 'Pediatric PD: access, membrane and prescription',
            'intro': 'Complete with a preceptor, in simulation or at your own unit. Sign-off is local.',
            'items': [('Calculates BSA and states the fill-volume range the unit protocol uses for a given child', False),
                      ('Marks a PD catheter exit site with the surgeon and family, away from diaper and ostomy sites', False),
                      ('Distinguishes leak, constipation, malposition and membrane causes of poor drainage at the bedside', False),
                      ('Leads a monthly PD review that starts with growth, blood pressure and fluid status', False)],
            'placement': 'Pediatric PD unit or supervised clinic'},
 'quiz': [
    ('Why are pediatric PD fill volumes scaled to body surface area rather than body weight?',
     ['Because weight-based fills are always too large in infants',
      'Because the peritoneal surface area relates to BSA, so per-kilogram fills underfill the membrane in small children',
      'Because PhilHealth coverage is calculated per m&sup2;',
      'Because BSA predicts residual urine output'],
     1,
     'Fills prescribed per kilogram are small relative to the membrane in young children, giving fast equilibration and early loss of ultrafiltration. '
     'Scaling to BSA removes most of the apparent age difference.'),
    ('A 10-month-old on PD started the day after catheter insertion has glucose-positive fluid at the exit site. What is the best first step?',
     ['Increase the fill to improve drainage',
      'Start intraperitoneal antibiotics',
      'Reduce or stop fills as the protocol allows, keep the child flat, and review with the surgeon',
      'Change to a higher glucose solution'],
     2,
     'This is a pericatheter leak. Lowering intraperitoneal pressure and resting the catheter give it the best chance to seal.'),
    ('A 3-year-old on rapid nightly cycling has a high Kt/V, a high phosphate and falling height centiles. What is the most likely explanation?',
     ['Short dwells clear urea well but phosphate poorly',
      'The membrane is failing',
      'The child is receiving too much dialysis',
      'The Kt/V was measured incorrectly'],
     0,
     'Phosphate needs three to four times longer than urea to equilibrate. A long dwell and a dietitian review address the problem the Kt/V hides.'),
    ('Which statement about evidence for pediatric PD catheters is correct?',
     ['Randomized trials prove omentectomy prevents blockage in infants',
      'Exit-site orientation has no recorded association with outcome',
      'Catheter revisions are rare after the first year and are mostly due to infection',
      'In the IPPN registry, 60% of revisions were for mechanical malfunction, and a double-cuff catheter with a downward or lateral exit is a 2D suggestion'],
     3,
     'Pediatric catheter guidance is weak (2D) and largely registry-based; omentectomy is recommended for infants without proven preventive value.'),
    ('A family asks whether the PhilHealth PD package decides how many exchanges their child will do. What is the correct answer?',
     ['Yes, the coverage tier sets the number of bags',
      'No; the attending prescribes what the child needs, documents it truthfully, and confirms coverage on the date of service',
      'Yes, but only for APD',
      'No, because PhilHealth does not cover children on PD'],
     1,
     'Coverage is not a prescription. The pediatric APD pilot status after July 31, 2026 is unresolved and must be confirmed with the PhilHealth liaison.'),
 ],
 'terms': [('APD', 'Automated peritoneal dialysis'),
           ('BSA', 'Body surface area'),
           ('CAKUT', 'Congenital anomalies of the kidney and urinary tract'),
           ('CAPD', 'Continuous ambulatory peritoneal dialysis'),
           ('CT', 'Computed tomography'),
           ('HD', 'Hemodialysis'),
           ('HUS', 'Hemolytic uremic syndrome'),
           ('IPP', 'Intraperitoneal pressure'),
           ('IPPN', 'International Pediatric Peritoneal Dialysis Network'),
           ('ISPD', 'International Society for Peritoneal Dialysis'),
           ('KDOQI', 'Kidney Disease Outcomes Quality Initiative'),
           ('KRT', 'Kidney replacement therapy'),
           ('PD', 'Peritoneal dialysis'),
           ('PET', 'Peritoneal equilibration test'),
           ('PTH', 'Parathyroid hormone'),
           ('SCOPE', 'Standardizing Care to Improve Outcomes in Pediatric End Stage Kidney Disease (collaborative)'),
           ('SDS', 'Standard deviation score')],
 'readings': [('peritoneal-dialysis-ckd.html', 'Peritoneal Dialysis: Your Complete Guide'),
              ('adding-peritoneal-dialysis-program.html', 'Roadmap to Adding a Peritoneal Dialysis Program — A Staged Implementation Guide'),
              ('dialysis-adequacy.html', 'Dialysis Adequacy — Is Your Dialysis Really Working?')],
 'calcs': ['calc-bsa.html', 'calc-pd-adequacy.html', 'calc-pd-glucose-absorption.html', 'calc-pediatric-growth-percentiles.html'],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
