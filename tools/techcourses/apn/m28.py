# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist, Module 28: Medicines, safeguarding, documentation and leading the service.
Written November 27, 2026 for the Renal Care Academy in the voice of the Physician on Duty modules, to the medical teaching
standard. Medication-error figures from the PubMed abstract of Kaushal 2001; consent from the AAP 2016 technical report; Philippine
law from the texts of RA 7610, the DOJ 1993 reporting rules, DOH AO 2013-0011 and RA 10173; ISPD 2022 targets from the PubMed
abstract. No doses. Every case is fictional."""

MODULE = {
    "image_alt": "A pediatric nephrologist kneels to speak with a thin eleven-year-old girl in a clinic while a social worker sits nearby with a notebook and a peritoneal dialysis logbook lies open on the desk.",
    "objectives": [
        "Prescribe safely for a child whose kidneys, liver and body size are changing, and design the safeguards that prevent tenfold and formulation errors.",
        "Recognize and act on a safeguarding concern as Philippine law requires, while keeping the child&rsquo;s kidney care going.",
        "Document truthfully for PhilHealth, hand adolescents over to adult care with a closed loop, and lead a quality-improvement project with a run chart.",
    ],
    "big": """
<div class="tc-keyp"><span class="tc-lab">Your role &middot; the physician whose name is on every page</span>The attending pediatric nephrologist signs the prescriptions, the PhilHealth checklists, the transfer letters and, when it comes to that, the child protection report. Each signature is a statement of fact. In a service with few pediatric nephrologists, you are also the person who teaches the residents, sets the unit&rsquo;s standards and watches its numbers. This module gathers the duties that sit behind every other module: medicines, protection, records, transition and improvement.</div>
{{plain:Think of a child&rsquo;s care as a relay race. Every handoff, from doctor to pharmacist, from parent to school, from pediatric to adult clinic, is where the baton is dropped. The fastest runners lose if the handoffs fail.}}
<p>The picture has a limit. In a relay, a dropped baton is obvious to everyone. In medicine, the dropped baton is often invisible: a decimal point in a liquid dose, bruises no one asks about, a checklist signed for services not given, a teenager who never reached the adult clinic. Nobody sees the drop until harm appears, sometimes months later. The attending&rsquo;s job is to build handoffs that make the drop visible early.</p>
{{cards:Key numbers|Medication errors, pediatric inpatients (Kaushal 2001)::616 errors in 10,778 orders (5.7%)|Where potential adverse drug events began::79% at the ordering stage; 34% involved incorrect dosing|Mandatory child-abuse reporting (DOJ rules, 1993)::Within 48 hours, by the head of the hospital and the attending physician and nurse|Age of majority in the Philippines::18 years|ISPD 2022 peritonitis targets (a unit quality measure)::No more than 0.40 episodes per year at risk; more than 80% of patients peritonitis-free per year}}
<p>Most of the harm in this module is not dramatic. It comes from systems: a prescribing habit that allows a tenfold error, a clinic that never asks why a child stopped coming, a form filled in to satisfy a claim. A few situations are urgent: a child who appears to have been hurt, a child who is not being given dialysis at home. Your work is to make safe prescribing the default, to recognize and report abuse and neglect without abandoning the child&rsquo;s care, to sign only what is true, and to measure the service so that it improves.</p>
""",
    "case": {"title": "Missed visits, weight loss and bruises",
             "html": """
<p>Joy Pascual is 11 and does continuous ambulatory peritoneal dialysis (CAPD) at home in San Jose City, Nueva Ecija. She has missed three monthly visits. Today she arrives with her 19-year-old stepbrother, who says he does her exchanges because their mother works in Manila and their father is away driving trucks. Joy has lost 2.1 kilograms in two months. Her peritoneal dialysis (PD) logbook has blank days. On her upper arms and back you see bruises of different colors. Her stepbrother says she falls a lot. Joy says nothing and will not look up.</p>
<p>Her liquid blood pressure medicine was compounded by a new pharmacy last month; the label gives a different concentration from the old bottle, and her stepbrother has been measuring the same number of milliliters. The clinic&rsquo;s PhilHealth coordinator reminds you that the monthly essential-services checklist for Joy&rsquo;s PD Z benefit is due today and needs your signature.</p>
""",
             "questions": ["What could explain Joy&rsquo;s presentation, and what do you do today?",
                           "What does Philippine law require of you, and how do you protect Joy while keeping her dialysis going?",
                           "What can you sign, and what system changes follow?"]},
    "sections": [
        ("physiology", "Pediatric pharmacology", "A changing body, a changing drug", """
<p>A child is not a small adult, and a 2-year-old is not a small 12-year-old. Absorption, distribution, metabolism and excretion all change with age. Glomerular filtration matures over the first two years; hepatic enzymes mature on their own timetables; body water and fat change the volume a drug distributes into.[[apn28_1]] Kidney disease adds a second layer: reduced clearance in chronic kidney disease (CKD), removal by PD, hemodialysis (HD) or continuous kidney replacement therapy (CKRT), and protein loss in nephrotic syndrome that changes free drug levels.</p>
<p>Dosing by weight or body surface area (BSA) follows from that physiology: both are attempts to scale a dose to a body that is growing. Each has limits. Weight-based dosing can overshoot in an obese adolescent, BSA requires height, which is often not measured on the ward, and neither accounts for a kidney that clears less. Every pediatric dose must be capped at the adult dose and checked against the child&rsquo;s kidney function and dialysis modality by the prescriber and a pharmacist. The doses themselves come from the hospital&rsquo;s pediatric formulary and current references, not from this module.</p>
<div class="table-wrap"><table>
<thead><tr><th>Error type</th><th>Why it happens in children</th><th>What it looks like</th><th>The safeguard</th></tr></thead>
<tbody>
<tr><td>Tenfold error</td><td>Doses calculated per kilogram; decimal points; trailing zeros</td><td>&ldquo;1.0 mL&rdquo; read as &ldquo;10 mL&rdquo;; a dose ten times too large or small</td><td>No trailing zeros, always a leading zero; dose written in milligrams and milliliters; independent pharmacist check</td></tr>
<tr><td>Formulation change</td><td>Liquids compounded locally at different concentrations</td><td>Same milliliters, different milligrams</td><td>Prescribe in milligrams; ask the family to bring every bottle; one pharmacy where possible</td></tr>
<tr><td>Weight not updated</td><td>Children grow, or lose weight when unwell</td><td>Underdosing as a child grows; overdosing after weight loss</td><td>Date the weight used on every prescription</td></tr>
<tr><td>Kidney function ignored</td><td>Creatinine read as normal for an adult</td><td>Accumulation of renally cleared drugs</td><td>Pediatric estimated glomerular filtration rate (eGFR) on the chart; dialysis modality on every order</td></tr>
<tr><td>Dialysis clearance ignored</td><td>Drug removed by PD, HD or CKRT</td><td>Subtherapeutic antibiotic levels</td><td>Pharmacist review with the dialysis prescription</td></tr>
</tbody></table></div>
<p><strong>Medicines across settings.</strong> A child with kidney disease is prescribed for in many places: your clinic, a provincial emergency room, a barangay health center, an adult HD unit, a pharmacy that compounds a liquid. Each prescriber sees a part. Reconcile the full list at every transition: admission, discharge, start of dialysis, transplant, and transfer to adult care. Ask the family to bring every bottle and box, not a list, because the bottle shows the concentration and the list does not.</p>
<div class="tc-scene"><span class="tc-lab">On the ward, the bottle in the bag &middot; fictional</span><p>Daniel, 4, on PD, is admitted with drowsiness and a low blood pressure. His mother shows you two bottles of the same antihypertensive from two pharmacies; one is five times as concentrated as the other, and she has been using the same syringe mark for both.</p><p>You hold the medicine, monitor him until he recovers, rewrite the prescription in milligrams with a single pharmacy named, and ask the pharmacist to mark the syringe and teach the mother with the bottle in her hand.</p><p class="tc-scene-take"><b>What this shows.</b> A prescription in milliliters is only safe while the concentration never changes, and in compounded liquids it often does.</p></div>
{{key:Write every pediatric dose in milligrams, with the weight and date used, the kidney function and the dialysis modality, and let a second person check it.}}
{{fig:apn28_a}}
"""),
        ("evidence", "Evidence", "What the evidence shows about errors, consent and improvement", """
<p><strong>Errors are common.</strong> Kaushal and colleagues studied 1,120 pediatric inpatients at two academic hospitals over six weeks in 1999. Of 10,778 medication orders, 616 contained an error (5.7%); there were 115 potential adverse drug events (1.1%) and 26 actual adverse drug events (0.24%). Most potential adverse events began at the ordering stage (79%) and involved incorrect dosing (34%), anti-infective drugs (28%) and intravenous medicines (54%). The potential adverse event rate was about three times that of an earlier adult study and was highest in neonates in intensive care. Physician reviewers judged that computerized order entry could have prevented 93% and ward-based clinical pharmacists 94% of potential adverse events.[[apn28_2]] The study is old, American and observational, and the prevention figures are reviewers&rsquo; judgments, not measured effects. Its lesson still applies wherever doses are calculated by hand at night.</p>
<p><strong>Consent and assent.</strong> The American Academy of Pediatrics (AAP) describes informed consent in pediatrics as an active process of parental permission and the child&rsquo;s assent, with the child&rsquo;s and adolescent&rsquo;s opinion included more fully as they mature, and with particular attention to adolescent consent, assent and refusal.[[apn28_3]] It is a policy framework, not a trial-tested intervention, and it is written for American law. In the Philippines the age of majority is 18, so a parent or guardian gives consent for a minor; the child&rsquo;s assent is still sought and recorded.</p>
<p><strong>Improvement.</strong> Perla, Provost and Murray describe the run chart: data plotted in time order with a median line, read with probability-based rules that distinguish a real change from random variation. They argue that this is more useful to improvement teams than aggregate summary statistics that ignore time order.[[apn28_9]] For a pediatric PD service, an obvious measure is the peritonitis rate, for which the International Society for Peritoneal Dialysis (ISPD) 2022 recommends no more than 0.40 episodes per year at risk and more than 80% of patients peritonitis-free per year.[[apn28_10]]</p>
<p><strong>Transition.</strong> The International Society of Nephrology (ISN) and International Pediatric Nephrology Association (IPNA) consensus describes transfer as the end of an individualized transition process involving both pediatric and adult teams, focused on self-management skills and support structures.[[apn28_8]] It is a consensus statement and gives a framework rather than tested outcomes.</p>
{{key:Medication errors begin mostly where doses are written. Put the second check at the point of ordering, not at the bedside.}}
"""),
        ("safeguarding", "Safeguarding", "Protecting the child: what the law requires and what the attending does", """
<p><strong>Why chronic kidney disease raises the risk.</strong> A child on home dialysis depends on adults for treatment every day. Exhausted caregivers, poverty, absent parents working abroad or far away, and a child who cannot easily tell anyone all raise the risk of neglect and abuse. Missed visits, unexplained weight loss, a logbook with blank days and injuries that do not fit the story are signals. They are not proof; each has innocent explanations, and in CKD, bruising can come from platelet dysfunction or anticoagulation. Your job is to notice, examine, document, and involve the people trained to assess.</p>
<p><strong>The law.</strong> Republic Act (RA) 7610, the Special Protection of Children Against Child Abuse, Exploitation and Discrimination Act, defines children as persons below 18, or older but unable to protect themselves because of a disability, and declares that the State shall intervene on behalf of a child when the parent or guardian fails or is unable to protect the child.[[apn28_4]] The Department of Justice (DOJ) rules on reporting and investigation (1993) require the head of any public or private hospital, clinic or similar institution, and the attending physician and nurse, to report the examination or treatment of a child who appears to have suffered abuse to the Department of Social Welfare and Development (DSWD) or the equivalent local agency within 48 hours of knowledge, orally or in writing. Failure to report is punishable by a fine; a person who reports in good faith is free from civil or administrative liability.[[apn28_5]]</p>
<p><strong>The hospital resource.</strong> Department of Health (DOH) Administrative Order (AO) 2013-0011 set the revised policy for women and children protection units (WCPUs) in all government hospitals, to standardize their services.[[apn28_6]] Where your hospital has a WCPU, it is the team to call; where it does not, the hospital social worker and the local social welfare office are.</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>What the attending does</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Notice</td><td>Ask about missed visits and weight loss without accusation; see the child alone if age and situation allow</td><td>Children rarely disclose in front of a possible abuser</td></tr>
<tr><td>Examine and document</td><td>Record injuries objectively: site, size, color, pattern; the explanation given, in the words used; photographs per hospital policy</td><td>Facts, not conclusions, protect the child and the record</td></tr>
<tr><td>Exclude medical causes</td><td>Platelet count, coagulation, anticoagulant exposure</td><td>Bruising in CKD can be medical</td></tr>
<tr><td>Make the child safe today</td><td>If you believe the child is unsafe going home, admit for medical reasons and involve the WCPU or social worker</td><td>Dialysis cannot stop while the situation is assessed</td></tr>
<tr><td>Report</td><td>Report through the hospital&rsquo;s process to DSWD or the local social welfare office within 48 hours</td><td>A legal duty for the head of the institution, the attending physician and nurse</td></tr>
<tr><td>Keep caring</td><td>Plan who will do dialysis, and where, during the assessment</td><td>Protection that interrupts dialysis harms the child</td></tr>
</tbody></table></div>
<p><strong>Confidentiality.</strong> Health information is sensitive personal information under the Data Privacy Act of 2012 (RA 10173).[[apn28_7]] Share what the child&rsquo;s safety and care require, with the people who need it, and record why. Adolescents deserve confidential time with you; tell them at the start that you will keep what they say private unless someone is at risk of serious harm, and keep that promise both ways.</p>
{{call:<ul><li>Injuries with no plausible explanation, or an explanation that changes</li><li>A child who discloses abuse</li><li>A child on home dialysis whose treatments are not being done</li><li>Weight loss, missed visits and a caregiver who cannot be reached</li><li>An adolescent who discloses self-harm or thoughts of suicide</li></ul>}}
{{key:You do not have to be certain to report; you have to have reason to be concerned. Report within 48 hours, keep the child safe, and keep the dialysis going.}}
"""),
        ("practice", "Records and improvement", "Truthful records, the handover letter, and a quality project", """
<p><strong>PhilHealth documentation.</strong> The pediatric essential-services checklist for the PD Z benefit under PhilHealth Circular (PC) 2024-0036 carries the name of the attending pediatric nephrologist.[[apn28_11]] Your signature says the listed services were delivered. If they were not, the record must say so. A checklist completed to keep a claim flowing, for a child whose exchanges were not done, is false, and it also hides the clinical problem from everyone who reads the chart later. Coverage rules change; confirm them with the coordinator on the date of service.</p>
<p><strong>The transition letter.</strong> A good handover letter names the diagnosis and its history, every medicine with its dose and formulation, the dialysis or transplant details, the access plan, the outstanding problems, what the young person knows and can do for themselves, the adult physician who has agreed to accept, the date of the first adult visit, and who will confirm attendance. The letter is not the transfer; the confirmed first visit is.</p>
<p><strong>A quality project.</strong> Choose one measure that matters to children and that your unit can count each month. The pediatric peritonitis rate is a good first project: its definition is published by ISPD, its target is explicit, and its causes are mostly in training and technique.[[apn28_10]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Step</th><th>For a pediatric PD peritonitis project</th></tr></thead>
<tbody>
<tr><td>Aim</td><td>Reach and hold a rate within the ISPD target, with more than 80% of children peritonitis-free per year</td></tr>
<tr><td>Measure</td><td>Episodes and patient-months at risk, every month; the organism and the likely route for each episode</td></tr>
<tr><td>Display</td><td>A run chart with a median line, updated monthly and posted where the nurses see it</td></tr>
<tr><td>Change</td><td>Retraining after every episode; a home-visit checklist; a caregiver-fatigue check at each review</td></tr>
<tr><td>Study</td><td>Read the run chart with its rules for shifts and trends, not month-to-month impressions</td></tr>
</tbody></table></div>
<p><strong>Teaching the people who carry your plan.</strong> In a scarce specialty, most of your patients&rsquo; care at night is given by people you trained or failed to train: pediatric residents, the physician on duty (POD) in an adult unit, ward nurses, the PD nurse. Teach the few rules that prevent the most harm, in short sessions where they work: how to write a pediatric dose, when to stop dialysis and call, which veins to protect, what makes a child protection report necessary. Ask them afterward to talk you through a case; their explanation tells you what they will actually do at 2 a.m.</p>
<div class="tc-scene"><span class="tc-lab">At the monthly meeting &middot; fictional</span><p>The PD nurse in your unit has plotted twelve months of pediatric peritonitis episodes. Three of the last four episodes were in children whose exchanges are done by an older sibling, not a parent.</p><p>You and the nurse add a training session for every secondary caregiver and a question about who actually does the exchanges to each monthly visit. You keep plotting.</p><p class="tc-scene-take"><b>What this shows.</b> A run chart that records why, not only how many, points to the change worth making.</p></div>
{{key:Sign only what is true, close every handover with a confirmed visit, and measure one thing that matters every month.}}
{{fig:apn28_b}}
"""),
    ],
    "debrief": [
        "<p><strong>The explanations, and today.</strong> Several explanations may be true at once: dialysis not being done (blank logbook days, a 19-year-old carrying an adult&rsquo;s task alone), poor intake or inadequate dialysis causing weight loss, a tenfold or formulation error from the new liquid concentration, and possible physical abuse or neglect. Bruising can also come from uremic platelet dysfunction, so check a platelet count and coagulation. Today: see Joy alone if she is willing; examine and document the bruises objectively; reconcile the medicine bottle, prescribe in milligrams and ask the pharmacist to confirm the dose; assess her fluid and nutritional state and her dialysis adequacy. If you are not confident she is safe at home, admit her for medical reasons, which her weight loss and incomplete dialysis justify.</p>",
        "<p><strong>The law and her dialysis.</strong> Under RA 7610 and the DOJ reporting rules, the head of the hospital and the attending physician and nurse must report a child who appears to have suffered abuse to DSWD or the local social welfare office within 48 hours; certainty is not required, and good-faith reporting is protected. Involve the hospital&rsquo;s women and children protection unit or social worker today. Keep the report factual. Meanwhile, plan who performs her exchanges during the assessment: in hospital, by the PD nurses, until a safe caregiver is trained. Call her mother. Share only what her care and safety require, and record why, consistent with the Data Privacy Act.</p>",
        "<p><strong>What to sign, and what changes.</strong> Do not sign the PD essential-services checklist as if services were delivered when the logbook shows they were not; record what was actually given and explain the gap to the coordinator. Then fix the systems: prescribe liquids in milligrams with the weight and date, ask families to bring every bottle, and have a pharmacist check each change in formulation. Add a question about who actually performs exchanges and a caregiver-fatigue check to every PD review, train secondary caregivers, and track missed visits and peritonitis on a monthly run chart so that the next Joy is noticed after one missed visit, not three.</p>",
    ],
    "skills": {"title": 'Medicines, safeguarding, documentation and leading the service',
               "intro": "Complete with a preceptor, in simulation or at your own unit. Sign-off is local.",
               "items": [("Reviews a set of pediatric prescriptions and finds the tenfold, formulation and kidney-function errors", False),
                         ("Documents a safeguarding concern objectively and completes the report pathway with the social worker or WCPU", False),
                         ("Completes a PhilHealth checklist truthfully for a child whose services were incomplete", False),
                         ("Builds a monthly run chart of a unit measure and reads it with its rules", False)],
               "placement": "Simulation or supervised practice"},
    "quiz": [
        ("A family has been giving the same number of milliliters of a liquid medicine after a pharmacy changed its concentration. Which safeguard best prevents this error?",
         ["Prescribing by milliliters only",
          "Prescribing in milligrams with the concentration checked by a pharmacist at each formulation change",
          "Doubling the volume when unsure",
          "Asking the family to estimate the dose"],
         1,
         "Same volume at a different concentration delivers a different dose. Milligrams, the weight used, and an independent pharmacist check close the gap."),
        ("Under the 1993 DOJ rules implementing RA 7610, what must the attending physician do when examining a child who appears to have been abused?",
         ["Wait until the abuse is proven",
          "Inform only the parents",
          "Report to DSWD or the local social welfare office within 48 hours",
          "Report only if the child asks"],
         2,
         "The head of the institution and the attending physician and nurse must report within 48 hours; good-faith reporting is protected from civil or administrative liability."),
        ("In the Kaushal study of pediatric inpatients, where did most potential adverse drug events begin?",
         ["At the ordering stage",
          "At dispensing",
          "At administration",
          "At monitoring"],
         0,
         "79% began at ordering, and 34% involved incorrect dosing; reviewers judged order entry systems and ward pharmacists could prevent most."),
        ("A child&rsquo;s PD logbook shows exchanges were not done on several days. The monthly PhilHealth essential-services checklist is due. What should the attending do?",
         ["Sign it so the claim is not delayed",
          "Ask the coordinator to sign instead",
          "Leave it unsigned with no explanation",
          "Record what was actually delivered and address the clinical gap"],
         3,
         "A signature is a statement of fact. A false checklist misleads the payer and hides the child&rsquo;s clinical problem."),
        ("Why is a run chart preferred to a yearly average for a unit&rsquo;s peritonitis rate?",
         ["It removes the need for a target",
          "It shows data in time order so real change can be distinguished from random variation",
          "It is required by PhilHealth",
          "It always shows improvement"],
         1,
         "Perla and colleagues describe run charts, read with probability-based rules, as more useful than summaries that ignore time order."),
    ],
    "terms": [("AAP", "American Academy of Pediatrics"), ("AO", "Administrative Order"), ("BSA", "Body surface area"),
              ("CAPD", "Continuous ambulatory peritoneal dialysis"), ("CKD", "Chronic kidney disease"),
              ("CKRT", "Continuous kidney replacement therapy"), ("DOH", "Department of Health"), ("DOJ", "Department of Justice"),
              ("DSWD", "Department of Social Welfare and Development"), ("eGFR", "Estimated glomerular filtration rate"),
              ("HD", "Hemodialysis"), ("IPNA", "International Pediatric Nephrology Association"),
              ("ISN", "International Society of Nephrology"), ("ISPD", "International Society for Peritoneal Dialysis"),
              ("PC", "PhilHealth Circular"), ("PD", "Peritoneal dialysis"), ("POD", "Physician on duty"),
              ("RA", "Republic Act"), ("WCPU", "Women and children protection unit")],
    "readings": [('medicines-and-your-kidneys.html', 'Multiple Medicines and Your Kidneys'),
                 ('dialysis-qapi-vs-cqi.html', 'Dialysis Center QAPI vs. CQI: A Quality Management Field Manual'),
                 ('philhealth-z-packages.html', 'PhilHealth Benefits: HD, PD & Kidney Transplant')],
    "calcs": ["calc-renal-med-safety.html", "calc-pediatric-egfr.html", "calc-bsa.html",
              "calc-qapi-run-chart-spc.html", "calc-philhealth-claims-toolkit.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("apn_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
