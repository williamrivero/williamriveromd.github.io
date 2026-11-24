# -*- coding: utf-8 -*-
"""Renal Dietitian: a study series for registered nutritionist-dietitians (RNDs) entering adult kidney care.
Blueprint: ~/Documents/Renal Dietitians/renal-dietitian-v2 (v2.0, November 23, 2026), expanded from the 13-module
v1 handoff to 16 modules. All content is written independently from primary sources; no course material from any
other training provider is used. Modules are authored natively in m01.py ... m16.py. Published
November 24, 2026 on Dr. Rivero's instruction; four figures held back after the image audit (see
docs/tech-courses/renal-dietitian-image-corrections.md)."""

_HB = ("Illustrated clinical vignette, warm natural light, Filipino staff and patients, Philippine clinic or dialysis unit, "
       "painterly editorial illustration (not flat vector), no text in image. ")

COURSE = {
    "title": "Renal Dietitian",
    "short": "Renal Dietitian",
    "hub_slug": "renal-dietitian",
    "label": "Study series for renal dietitians",
    "tag": "Ancillary Staff",
    "icon": "🥗",
    "no_branch": True,
    "audience": ("Registered nutritionist-dietitians entering adult kidney care &middot; renal RND preceptors, "
                 "nephrologists, and head nurses who orient them"),
    "audience_type": "Registered nutritionist-dietitians in kidney care",
    "level": "Licensed nutritionist-dietitians, written in plain language",
    "review_date": "2026-11-23",
    "draw": 8,
    "exam_draw": 40,
    "mastery": "7 of 8",
    "keywords": ("renal dietitian training Philippines, renal nutrition course, medical nutrition therapy chronic kidney disease, "
                 "dialysis diet, protein-energy wasting, potassium phosphorus sodium, peritoneal dialysis nutrition, "
                 "kidney transplant nutrition, Filipino renal diet"),
    "page_title": "Renal Dietitian: A Study Series in Kidney Nutrition",
    "desc": ("A free study series for registered nutritionist-dietitians entering adult kidney care in the Philippines: how the "
             "kidney handles nutrients, how to assess nutrition risk, how to write and adjust a nutrition prescription across "
             "chronic kidney disease, dialysis, hospital care, and transplant, and how to counsel with familiar Filipino foods. "
             "Plain language, many figures, a case, a skills checklist, and a self-assessment in every module."),
    "h1": "Renal <em>Dietitian</em>",
    "sub": ("Medical nutrition therapy across adult kidney care. Learn why each restriction exists, when it should be lifted, "
            "and how to turn a prescription into food a Filipino family will cook."),
    "disclaimer": ("Educational study material for registered nutritionist-dietitians. Does not replace the nephrologist&rsquo;s orders, "
                   "facility policy, the Nutrition Care Process documentation required by the Department of Health, or supervised practice."),
    "scope_note": ("This module is study material for dietitians in adult kidney care. It explains the reasoning behind common decisions; "
                   "it is not a protocol. In practice, follow your facility&rsquo;s policy and the responsible physician&rsquo;s orders. "
                   "Targets and cut-off values are set by your unit and the attending nephrologist. Every case is fictional."),
    "branch_img": "renal-dietitian-card.webp",
    "branch_role": "Dietitians",
    "branch_blurb": ("For registered nutritionist-dietitians: assessment, medical nutrition therapy, and counseling across chronic "
                     "kidney disease, dialysis, acute kidney injury, transplantation, and supportive care."),
    "academy_meta": "16 modules &middot; 240 practice questions &middot; four parts",
    "hero_alt": "A renal dietitian and a patient looking at a plate of rice, fish, and vegetables beside a hemodialysis chair.",
    "start_h2": "Food is a treatment, and you prescribe it",
    "start_html": """
<p>Two healthy kidneys clear the waste of whatever a person eats. When they fail, the diet has to do part of that work in advance: less sodium than the kidney can no longer excrete, enough protein to keep muscle but not so much that waste builds up, and the right amount of potassium and phosphorus for today&rsquo;s laboratory results, not last year&rsquo;s. The registered nutritionist-dietitian (RND) is the team member trained to make those trade-offs with the patient.</p>
<p>Old renal diets were long lists of forbidden foods. Patients ate less, lost muscle, and still had high potassium, because the cause was often a medicine, constipation, or a missed dialysis session and not the banana. Current guidelines ask for something harder and better: an individualized prescription, adjusted to the stage of disease and the treatment, built from food the patient already eats.[[kdoqi2020]][[kdigo_ckd2024]]</p>
{{cards:What this series will help you do|Understand the physiology::Explain how a failing kidney handles nitrogen, sodium, potassium, phosphorus, and acid, so every restriction has a reason.|Assess::Find protein-energy wasting early, using weight history, intake, examination, and function, not albumin alone.|Prescribe::Calculate energy and protein for each stage and treatment, and say which guideline you used and why.|Individualize::Restrict potassium, phosphorus, sodium, and fluid only when the patient in front of you needs it.|Counsel::Turn numbers into sinigang, tinola, rice, and fish, with teach-back.|Escalate::Recognize the findings that need a physician or nurse today, and hand off clearly.}}
<p>The series is written in plain language. Every new term is explained when it first appears, and every module has figures, a fictional case, real situations with problems and solutions, a skills checklist, and a self-assessment.</p>
""",
    "is_not": ("It is study material written independently from published guidelines, textbooks, and research. It is not a license, a specialty "
               "certificate, or continuing professional development (CPD) credit, and it does not replace the scope of practice set by Republic "
               "Act No. 10862 or the Nutrition Care Process documentation required of hospitals by the Department of Health.[[ra10862]][[doh_ncp2019]] "
               "Prescribing medicines, changing a dialysis prescription, and directing emergency treatment belong to the responsible physician. "
               "The series covers adults. Children and pregnant patients are taught as recognize-and-refer topics."),
    "pathways_tag": "Four parts",
    "pathways_h2": "Five weeks of study, in four parts",
    "pathways_nav": "Parts",
    "pathways_html": """
<p>The series has 16 modules. A new renal dietitian can finish them in about five weeks of part-time study, alongside supervised practice on the unit.</p>
{{cards:The four parts|Part 1. Foundations::Three modules: your role and the first consult, how the kidney handles nutrients, and nutrition assessment.|Part 2. The nutrition prescription in chronic kidney disease::Five modules: energy and protein, sodium and fluid, potassium and acid, phosphorus and bone, and diabetes with obesity.|Part 3. Dialysis, hospital, and transplant::Four modules: hemodialysis, peritoneal dialysis, acute kidney injury and nutrition support, and transplantation.|Part 4. Special situations and skills::Four modules: supportive care and special groups, vitamins and supplements, counseling and Filipino food skills, and quality with the capstone.}}
{{flow:Suggested five-week pace|Week 1::Modules 1 to 3. Observe a first visit for chronic kidney disease and write a simulated assessment.|Week 2::Modules 4 to 8. Practice label reading; rehearse a critical-result handoff and a hypoglycemia handoff.|Week 3::Modules 9 to 12. Observe a hemodialysis shift, a peritoneal dialysis clinic, and one inpatient round.|Week 4::Modules 13 to 15. Role-play a supportive care visit and a recipe-based teach-back.|Week 5::Module 16. Capstone case, four observed stations, and a feedback meeting.}}
""",
    "modules_h2": "Sixteen modules in four parts",
    "modules_intro": ("Study the modules in order. Each one starts from physiology, moves to what the evidence shows, and ends with what to do "
                      "at the bedside or the clinic desk."),
    "syllabus_note": ("Each module takes about 60 to 90 minutes to read and work through (about 20 hours in all). Skills checklists are completed "
                      "with a preceptor; allow at least 10 further hours of supervised practice."),
    "assessment_html": """
<p>The questions at the end of each module are for practice. Each visit draws eight from a bank of fifteen, and every question explains its best answer. The end-of-course examination draws 40 questions from all 240. The questions were written for this series.</p>
<p>Competence is shown with patients, not on a screen. Each module has a skills checklist for a preceptor to complete while watching you work, and the preceptor page has four observed stations and a capstone case with a scoring rubric. Answers stay on your device; nothing is sent or stored by the site.</p>
""",
    "sources_html": """
<p>The series is built from published sources. Nutrition recommendations follow the Kidney Disease Outcomes Quality Initiative (KDOQI) 2020 nutrition guideline and the Kidney Disease: Improving Global Outcomes (KDIGO) 2024 chronic kidney disease guideline, which differ on protein and are compared side by side in Module 4.[[kdoqi2020]][[kdigo_ckd2024]] Diabetes follows KDIGO 2022 and the American Diabetes Association Standards of Care 2026.[[kdigo_dm2022]][[ada2026]] Hospital nutrition follows the European Society for Clinical Nutrition and Metabolism (ESPEN).[[espen2024]] Peritoneal dialysis follows the International Society for Peritoneal Dialysis (ISPD).[[ispd2020]][[ispd_perit2022]] Food values come from the Philippine Food Composition Tables and the Food Exchange Lists of the Food and Nutrition Research Institute.[[philfct]][[fel2019]]</p>
<p>Each guideline&rsquo;s own grade is quoted as written (for example, KDOQI 1C or KDIGO 2C) and never converted to another system. Where a practice rests on observation or expert opinion, the text says so. Where good Philippine data are missing, international data are used and labeled.</p>
""",
    "trainers_intro": ("A senior renal RND, with the attending nephrologist and head nurse, can use these modules as the guided-study part of orientation. "),
    "trainer_h2": "Using the series to orient a new renal dietitian",
    "trainer_html": """
<p>Assign one renal RND as preceptor. Before the first session, identify the unit&rsquo;s critical-result contacts, the after-hours escalation route, the patient education languages, and which patient encounters the learner may observe or conduct under documented supervision. Use fictional cards for simulation.</p>
{{flow:Suggested orientation sequence|Before day 1::Modules 1 to 3; each self-assessment at 7 of 8.|Week 1::Unit tour, laboratory schedule, critical-result policy, documentation system. Station 1 (assessment and documentation).|Week 2::Supervised first visits for chronic kidney disease. Station 2 (prescription and counseling).|Week 3::Hemodialysis rounds and a peritoneal dialysis clinic. Station 3 (peritoneal dialysis calculation and urgent escalation).|Week 4::Inpatient round with the nutrition support team. Station 4 (acute kidney injury handoff).|Week 5::Capstone case, rubric, and feedback meeting.}}
<p><strong>Scoring the checklists.</strong> Mark each behavior as observed independently, observed with prompting, or pending. Record the date, the setting, the evidence, and the next practice step. Re-observe every prompted or pending <span class="tc-crit">Critical</span> behavior. Facility policy governs clinical privileges.</p>
<p><strong>Observed stations.</strong> Give the learner the case and tasks with the worked answer hidden. Allow 10 minutes per station and 5 minutes for feedback. Score each criterion 0 (missing or unsafe), 1 (incomplete or prompted), or 2 (complete and independent). A station passes at 5 of 6 with the critical criterion scored 2. Repeat an unsuccessful station with a parallel fictional case after coaching.</p>
<div class="table-wrap"><table>
<thead><tr><th>Station</th><th>Case from</th><th>Criteria (critical criterion marked)</th></tr></thead>
<tbody>
<tr><td>1. Assessment and documentation</td><td>Module 3, &ldquo;The denture&rdquo;</td><td>Selects comparable weights and computes 6.5% loss. Writes a PES statement with an actionable cause and two measurable follow-up items. <span class="tc-crit">Critical</span> Recognizes combined intake decline and weight loss and reports it the same day.</td></tr>
<tr><td>2. Stable CKD prescription and counseling</td><td>Module 4, &ldquo;Two guidelines, one patient&rdquo;</td><td>Calculates 48 g protein and 1,500 to 2,100 kcal at 60 kg. <span class="tc-crit">Critical</span> Checks metabolic stability before discussing restriction and explains why the KDOQI pathway differs. Agrees on one affordable change with teach-back.</td></tr>
<tr><td>3. Peritoneal dialysis calculation and urgent escalation</td><td>Module 10, &ldquo;Full by dinner&rdquo;</td><td>Calculates 272 kcal from dialysate and about 1,528 kcal from food, and 60 to 72 g protein. Lifts the outdated potassium restriction and reports the low result. <span class="tc-crit">Critical</span> When the examiner reveals cloudy fluid, stops and contacts the PD team at once with a documented handoff.</td></tr>
<tr><td>4. AKI and nutrition support handoff</td><td>Module 11, &ldquo;The old order&rdquo;</td><td>Chooses the 69 kg pre-illness weight and the continuous KRT range (about 104 to 117 g/day). <span class="tc-crit">Critical</span> Flags refeeding risk and the falling phosphate and asks for the protocol before feeds increase. Recommends cancelling the outpatient order and tracking delivered intake.</td></tr>
</tbody></table></div>
<p><strong>Capstone.</strong> Module 16, &ldquo;Ramon.&rdquo; Allow 25 minutes for the written plan and 5 minutes for the oral handoff. Introduce the critical potassium with weakness only after the learner has described routine follow-up. Five criteria, each scored 0 to 2: comparable weight loss (4.8%) and the 60 to 72 g/day range with the stability caveat; PES and a patient-chosen change; phosphorus handoff that protects protein; <span class="tc-crit">Critical</span> immediate urgent escalation with accepted handoff; quality measure (75%) with a balancing measure. Pass at 8 of 10 with the critical criterion scored 2. If not passed, give feedback on the missed behavior, assign the related module, and reassess with a new fictional case.</p>
<p><strong>Printable worksheets.</strong> Four one-page forms support the stations: a consult documentation sheet, a food calculation sheet, an observation record, and a handoff practice sheet. Sign-offs belong on paper or in the facility&rsquo;s own system; nothing is recorded on this site.</p>
<p><strong>Before publication.</strong> A renal RND checks the assessment, calculations, and food examples; a nephrologist checks staging, escalation language, and transitions; a PD nurse and pharmacist check peritonitis escalation, icodextrin, binder, and interaction teaching. Recheck sources at least yearly.</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments: 7 of 8 on two different sets for each module, with every missed question reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated to a preceptor without prompting.</li>
<li>Four observed stations passed, and the capstone case passed at 8 of 10.</li>
<li>One closed-loop escalation of a simulated critical result, with documented acceptance.</li>
<li>Sign-off recorded locally by the facility, on paper or in its own system.</li>
</ul>
<p>These are proposals for each unit to adapt. The series confers no license, specialty certification, or CPD credit.</p>
""",
}

P1 = "Part 1 &middot; Foundations"
P2 = "Part 2 &middot; The nutrition prescription in chronic kidney disease"
P3 = "Part 3 &middot; Dialysis, hospital, and transplant"
P4 = "Part 4 &middot; Special situations and skills"

# id, slug, title, part, study minutes, competencies, sub (card text), hero brief
_ROWS = [
    ("01", "role-and-first-consult", "The Renal Dietitian&rsquo;s Role and the First Consult", P1, 60, "C1 C7",
     "Staging chronic kidney disease, triaging a referral, working within the RND scope, and escalating a critical result with a closed-loop handoff.",
     "A dietitian at a clinic desk on the telephone, a laboratory report in hand, a patient seated beside her."),
    ("02", "how-the-kidney-handles-nutrients", "How the Kidney Handles Nutrients", P1, 75, "C1 C4",
     "Nitrogen, sodium and water, potassium, phosphorus, acid, and vitamin D: what a healthy kidney does with each, and what fails first.",
     "A dietitian sketching a simple kidney and a plate of food on a whiteboard for two colleagues."),
    ("03", "assessment-and-nutrition-care-process", "Nutrition Assessment, Diagnosis, and Monitoring", P1, 90, "C2 C7",
     "Comparable weights, intake, nutrition-focused examination, handgrip strength, protein-energy wasting, and a problem&ndash;etiology&ndash;signs statement.",
     "A dietitian measuring a seated patient&rsquo;s mid-arm with a tape, a handgrip dynamometer on the table."),
    ("04", "energy-protein-eating-patterns", "Energy, Protein, and Eating Patterns in Stable Chronic Kidney Disease", P2, 90, "C2 C3",
     "The KDIGO and KDOQI protein recommendations side by side, energy, plant-dominant patterns, ketoanalogues, and who should not be restricted.",
     "A dietitian and an older man comparing two plates: one with a large fried pork portion, one with fish, tofu, vegetables, and rice."),
    ("05", "sodium-fluid-volume", "Sodium, Fluid, and Volume", P2, 75, "C3 C4 C6",
     "Why sodium drives thirst and blood pressure, counting sodium in patis, toyo, bagoong, and noodles, weight gain between dialysis sessions, and salt substitutes.",
     "A patient and dietitian reading the label on an instant noodle packet beside bottles of fish sauce and soy sauce."),
    ("06", "potassium-acid-base-fiber", "Potassium, Acid&ndash;Base Balance, and Fiber", P2, 75, "C4 C7",
     "Causes of high potassium other than food, when to restrict and when to liberalize, fruits and vegetables for acidosis, constipation, and low potassium.",
     "A market stall with bananas, leafy greens, and root crops; a dietitian talking with a vendor and a patient."),
    ("07", "phosphorus-calcium-bone", "Phosphorus, Calcium, Vitamin D, and Bone", P2, 75, "C4 C7",
     "Organic, plant, and additive phosphorus, binder timing, calcium load, what the HiLo trial did and did not show, and protecting protein intake.",
     "A dietitian pointing to the ingredient list on a processed meat package while a patient holds a pill organizer."),
    ("08", "diabetes-obesity-cardiometabolic", "Diabetes, Obesity, and Cardiometabolic Risk", P2, 75, "C3 C4 C6 C7",
     "Glucose data in advanced kidney disease, hypoglycemia, carbohydrate planning, newer medicines that change appetite and fluid needs, and weight loss that keeps muscle.",
     "A woman checking her glucose with a meter at a workplace canteen table, a packed lunch in front of her."),
    ("09", "hemodialysis", "Medical Nutrition Therapy in Maintenance Hemodialysis", P3, 90, "C2 C4 C5",
     "Why protein needs rise on dialysis, the dialysis-day gap, eating during treatment, oral supplements, intradialytic parenteral nutrition, and incremental and twice-weekly schedules.",
     "A patient in a hemodialysis chair eating a small packed meal while a dietitian reviews a chart with the nurse."),
    ("10", "peritoneal-dialysis", "Medical Nutrition Therapy in Peritoneal Dialysis", P3, 75, "C4 C5 C7",
     "Glucose absorbed from dialysate, protein losses, early satiety, low potassium and peritonitis, icodextrin and glucose meters, and when to call the peritoneal dialysis nurse.",
     "A patient at home performing a peritoneal dialysis exchange beside a small dining table with a light meal."),
    ("11", "acute-kidney-injury-nutrition-support", "Acute Kidney Injury and Inpatient Nutrition Support", P3, 90, "C2 C5 C7",
     "Protein by illness severity and kidney replacement modality, the weight to calculate from, enteral and parenteral feeding, refeeding syndrome, and energy hidden in fluids.",
     "An intensive care bedside with a feeding pump and a continuous kidney replacement machine; a dietitian speaking with the team."),
    ("12", "kidney-transplantation", "Nutrition Before and After Kidney Transplantation", P3, 75, "C4 C5 C6",
     "Prehabilitation, the first weeks, lifting old dialysis restrictions, post-transplant diabetes, food safety, and foods and herbs that change tacrolimus levels.",
     "A family kitchen where a transplant recipient and spouse cook fish thoroughly, a pomelo set aside on the counter."),
    ("13", "supportive-care-and-special-populations", "Supportive Care, Frailty, and Special Populations", P4, 75, "C2 C5 C6 C7",
     "Conservative kidney management, eating for comfort and function, frailty and sarcopenia, kidney stones, polycystic kidney disease, and when to refer children and pregnant patients.",
     "An older man eating a small meal at a family table with grandchildren, a dietitian visiting the home."),
    ("14", "vitamins-minerals-supplements-food-safety", "Vitamins, Minerals, Supplements, and Foods That Harm", P4, 75, "C4 C6 C7",
     "Water-soluble vitamin losses, vitamins A and C, iron and zinc, herbal products, star fruit (balimbing) and kamias, and how to review a supplement bag.",
     "A table covered with supplement bottles, herbal tea packets, and star fruit, a dietitian reading one label with a magnifier."),
    ("15", "counseling-and-filipino-food-skills", "Counseling and Filipino Food Skills", P4, 90, "C3 C6 C7",
     "Elicit&ndash;offer&ndash;check, teach-back, health literacy, household measures, recipe arithmetic, food exchange lists, eating on a budget, and fiestas.",
     "A dietitian and a mother measuring fish sauce with a spoon over a pot of tinola in a home kitchen."),
    ("16", "transitions-quality-capstone", "Transitions of Care, Quality Improvement, and Capstone", P4, 90, "C1 C2 C3 C4 C5 C6 C7 C8",
     "Handoffs across settings, defining and charting a nutrition quality measure, a balancing measure, and one integrated case with a critical result.",
     "A dietitian presenting a simple run chart on a wall board to a nurse and a nephrologist in a unit meeting room."),
]

COMPETENCIES = {
    "C1": "Classify kidney disease and triage a renal nutrition referral.",
    "C2": "Assess intake, clinical trends, nutrition risk, and function, then document a defensible nutrition diagnosis.",
    "C3": "Calculate a modality-appropriate energy, protein, and sodium plan and translate it into affordable meals.",
    "C4": "Interpret electrolyte, glycemic, and volume trends and coordinate a safe response.",
    "C5": "Adapt medical nutrition therapy across kidney replacement, hospital, transplant, and supportive care settings.",
    "C6": "Use shared decision-making and teach-back to agree on feasible food changes.",
    "C7": "Document monitoring and perform closed-loop interprofessional handoffs and escalation.",
    "C8": "Define and interpret a renal nutrition quality measure.",
}

MODULES = []
for _id, _slug, _title, _part, _min, _comp, _sub, _brief in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part, "minutes": _min,
                    "competencies": _comp.split(), "card_img": f"renal-dietitian-{_id}-card.webp",
                    "hero_brief": _HB + _brief})
