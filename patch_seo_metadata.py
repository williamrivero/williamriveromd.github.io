#!/usr/bin/env python3
"""
patch_seo_metadata.py
Adds/fixes SEO metadata (keywords, description, author, robots) for all 93 guide files.
"""

import re
import os

GUIDES_DIR = "/home/user/williamriveromd.github.io/guides"

# Per-guide metadata: (description 140-160 chars, keywords list)
# description: plain text, no HTML, ≤160 chars, patient-focused, Philippine context where relevant
# keywords: 15-25 items, lowercase, comma-separated

GUIDE_META = {
    "acute-kidney-injury-on-ckd.html": {
        "description": "Sudden worsening of kidney function in CKD patients: causes, warning signs, treatment, and how to protect remaining kidney function in the Philippines.",
        "keywords": "acute kidney injury, AKI on CKD, sudden kidney failure, kidney damage causes, AKI treatment Philippines, creatinine spike, oliguria, kidney injury prevention, KDIGO AKI, dehydration kidney, nephrotoxic drugs, kidney injury stages, bato acutely damaged, kidney failure warning signs, NKTI Philippines, acute renal failure, AKI management, kidney injury recovery, contrast nephropathy, sepsis kidney injury"
    },
    "advance-care-planning-dialysis.html": {
        "description": "Guide for dialysis patients on documenting your care wishes, living wills, and ensuring your values guide treatment decisions — Filipino context included.",
        "keywords": "advance care planning dialysis, living will Philippines, dialysis end of life, healthcare proxy, withdrawing dialysis, patient rights Philippines, conservative kidney management, palliative care CKD, dialysis withdrawal, DNAR Philippines, advance directive, end stage kidney disease planning, dialysis quality of life, dying with dignity Philippines, comfort care kidney failure, hospice Philippines, dialysis patient rights, surrogate decision maker, values history kidney, family meeting dialysis"
    },
    "alcohol-ckd.html": {
        "description": "How alcohol affects kidneys with CKD — safe limits, Filipino drink equivalents (SMB, Red Horse, lambanog), drug interactions, and dialysis risks explained.",
        "keywords": "alcohol kidney disease, alcohol CKD Philippines, drinking limits kidney failure, lambanog kidney, San Miguel Beer kidney, Red Horse beer kidney, Tanduay rum kidney, alcohol hemodialysis, standard drink calculator Philippines, alcohol drug interactions, KDIGO alcohol limits, drinking with dialysis, alcohol proteinuria, alcoholic kidney disease, bato at alak, kidney damage alcohol, drinking log kidney, alcohol creatinine, alcohol hypertension kidney, safe alcohol limits Philippines"
    },
    "alcohol-drinking-log.html": {
        "description": "Free 14-day printable alcohol tracking log for Filipino kidney, heart, and diabetes patients — fill by hand or on-screen and bring to your consultation.",
        "keywords": "alcohol drinking log, printable drinking tracker, 14 day alcohol log Philippines, kidney patient alcohol diary, diabetes drinking log, heart patient alcohol log, alcohol self-monitoring, standard drink log, kidney disease alcohol tracker, dialysis patient drinking record, alcohol consumption diary, CKD alcohol log, patient drinking record, alcohol log download Philippines, nephrology consultation log, drinking tracker printable, alcohol record kidney, Filipino patient tools"
    },
    "anemia-management.html": {
        "description": "Anemia in kidney disease explained: low hemoglobin causes, iron vs. EPO treatment, Filipino iron-rich foods, and targets to restore energy and protect your heart.",
        "keywords": "anemia kidney disease, anemia CKD Philippines, low hemoglobin kidney, EPO injection kidney, erythropoietin CKD, iron deficiency dialysis, iron infusion Philippines, TSAT ferritin kidney, anemia treatment CKD, pagod palagi kidney, mahina anemia, iron supplement kidney patient, darbepoetin Philippines, roxadustat kidney anemia, hemoglobin target dialysis, blood building foods Philippines, anemia fatigue kidney, kidney anemia treatment, IV iron hemodialysis, Filipino iron rich foods kidney"
    },
    "buko-juice-alkaline-water-ckd.html": {
        "description": "Is buko juice safe for kidney disease? Does alkaline water help kidneys? Evidence-based answers for Filipino CKD patients on these common questions.",
        "keywords": "buko juice kidney disease, coconut water kidney, alkaline water CKD Philippines, buko kidney patient, is coconut water safe kidney failure, alkaline water kidney stones, tubig na bato, potassium buko kidney, coconut juice dialysis, alkaline water Philippines kidney, buko juice potassium, kidney patient drink recommendations, CKD safe drinks Philippines, coconut water electrolytes kidney, tubig alkaline bato, buko juice safe dialysis, alkaline pH water kidneys, kidney friendly drinks Philippines, electrolyte drink CKD, buko water hyperkalemia"
    },
    "cardiac-rehab-ckd-post-mi.html": {
        "description": "Cardiac rehabilitation after heart attack for CKD and dialysis patients — safe exercise phases, medication guidance, diet, and monitoring in the Philippines.",
        "keywords": "cardiac rehab CKD Philippines, heart attack recovery kidney disease, post MI rehabilitation, exercise after heart attack kidney, cardiac rehabilitation dialysis patient, heart attack kidney failure, CKD cardiovascular recovery, phase 1 2 3 cardiac rehab, post MI medications kidney, heart kidney disease recovery, exercise CKD after heart attack, cardiac monitoring hemodialysis, smoking cessation CKD, statin kidney disease, aspirin kidney, beta blocker dialysis, cardiac rehab Philippines, Filipino heart attack recovery, post-MI exercise kidney patient, cardiorenal rehabilitation"
    },
    "caregiver-guide-ckd.html": {
        "description": "Practical guide for families caring for a CKD patient at home — managing medications, diet, fistula care, emotional support, and caregiver self-care in the Philippines.",
        "keywords": "caregiver CKD Philippines, family guide kidney disease, caring for kidney patient, home care dialysis patient, CKD caregiver burnout, fistula care at home, kidney patient diet caregiver, medication management CKD, caregiver mental health, kidney disease family support, dialysis caregiver guide, CKD home care Philippines, supporting kidney patient, caregiver tips kidney, looking after kidney patient, pamilya kidney disease, caregiver resources Philippines, kidney disease caregiver stress, home hemodialysis caregiver, palagi may sakit na bato"
    },
    "cholesterol-diet-guide.html": {
        "description": "Cholesterol and kidney disease: understanding LDL, HDL, triglycerides, and what Filipino foods to eat or avoid to protect your heart and kidneys.",
        "keywords": "cholesterol kidney disease Philippines, high cholesterol CKD, LDL HDL kidney patient, dyslipidemia diet Philippines, Filipino foods cholesterol, statin kidney disease, cholesterol diet kidney, kolesterol Filipino, triglycerides kidney disease, heart disease kidney cholesterol, cholesterol reduction diet Philippines, coconut oil cholesterol kidney, pork cholesterol kidney, Filipino cholesterol lowering foods, atorvastatin kidney, rosuvastatin CKD, cholesterol targets kidney patient, lipid diet guide Philippines, low cholesterol Filipino recipes, bato at kolesterol"
    },
    "ckd-alternative-holistic-medicine.html": {
        "description": "Which herbal and holistic treatments are safe for kidney disease, which are harmful, and how integrative medicine can work alongside nephrology care in the Philippines.",
        "keywords": "alternative medicine kidney disease Philippines, herbal remedy kidney, holistic kidney treatment, tawas kidney, herbal CKD Philippines, lagundi kidney, sambong kidney stone, traditional medicine kidney Philippines, integrative nephrology, acupuncture kidney disease, herbal medicine safety CKD, DOH herbal medicine Philippines, kidney disease natural treatment, alternative therapy dialysis, faith healing kidney, safe herbs kidney patient, harmful herbs kidneys, complementary medicine CKD, Filipino traditional medicine kidney, evidence-based herbal kidney"
    },
    "ckd-children-young-adults.html": {
        "description": "Kidney disease in children and teens: causes, school support, transition to adult nephrology, mental health, and Philippine resources for families.",
        "keywords": "pediatric CKD Philippines, kidney disease children, CKD teenagers Philippines, young adult kidney failure, NKTI pediatric nephrology, congenital kidney disease, CAKUT Philippines, kidney disease school children, transitional nephrology Philippines, nephrotic syndrome children, lupus nephritis children, adolescent kidney disease, kidney transplant children Philippines, chronic kidney disease child, pediatric dialysis Philippines, kidney disease diagnosis child, school and kidney disease, growth CKD child, pediatric nephrology Manila, children kidney failure treatment"
    },
    "ckd-dri-calculator.html": {
        "description": "Personalized daily nutrition targets for CKD patients — protein, potassium, phosphorus, sodium, fluid, and calories adjusted by your kidney stage.",
        "keywords": "CKD nutrition calculator Philippines, kidney diet daily targets, protein intake CKD, potassium limit kidney disease, phosphorus limit dialysis, sodium limit kidney patient, fluid restriction dialysis, calorie needs CKD, kidney diet calculator, DRI kidney disease, CKD dietary reference intake, daily nutrition kidney patient, kidney stage diet calculator, hemodialysis protein requirements, peritoneal dialysis nutrition, CKD G3 G4 G5 diet, kidney nutrient calculator, Filipino kidney diet calculator, phosphorus daily limit CKD, kidney diet personalized"
    },
    "ckd-financial-stress.html": {
        "description": "Managing the cost of kidney disease in the Philippines — PhilHealth benefits, PCSO, DSWD, Malasakit Center, NGOs, and strategies to reduce dialysis expenses.",
        "keywords": "kidney disease financial help Philippines, dialysis cost Philippines, PhilHealth kidney benefit, PCSO kidney disease, DSWD kidney patient, Malasakit Center dialysis, kidney disease financial assistance Philippines, dialysis subsidy Philippines, free dialysis Philippines, kidney foundation Philippines, CKD financial stress, dialysis cost reduction, DOH dialysis program, Kidney Foundation Philippines, NKF Philippines, dialysis scholarship, kidney patient financial aid, gastos dialysis Pilipinas, PhilHealth Z package kidney, affordable dialysis Philippines"
    },
    "ckd-friendly-recipes-regional.html": {
        "description": "Regional Filipino recipes adapted for kidney disease — Kapampangan, Ilocano, Ilonggo, Cebuano cuisines reimagined with kidney-safe ingredient swaps.",
        "keywords": "regional Filipino kidney recipes, Kapampangan recipes kidney disease, Ilocano diet kidney patient, Ilonggo kidney friendly food, Cebuano recipes kidney disease, Filipino cuisine kidney patient, kidney safe Filipino food, regional cuisine CKD Philippines, kidney diet Filipino regional, lowered potassium Filipino recipe, low sodium Filipino dish, kidney safe adobo, kidney recipe pinakbet, kidney recipe sinigang, regional food CKD, Filipino kidney diet regional, kare-kare kidney patient, low phosphorus Filipino food, kidney friendly Filipino cooking, dialysis recipe Filipino"
    },
    "ckd-friendly-recipes.html": {
        "description": "Practical kidney-safe Filipino recipes for pre-dialysis and dialysis patients using local ingredients — with clear potassium, phosphorus, and sodium information.",
        "keywords": "kidney friendly Filipino recipes, CKD diet recipes Philippines, dialysis patient meals, kidney safe Filipino food, low potassium Filipino recipe, low phosphorus recipe Philippines, kidney diet sinigang, kidney safe adobo, Filipino kidney meal plan, dialysis diet recipe Philippines, kidney patient cooking Philippines, low sodium Filipino recipe, pre-dialysis diet recipe, kidney food Philippines, bato friendly recipe, lutuin para kidney patient, low protein recipe Philippines, kidney rice dish Philippines, kidney safe ulam, Filipino kidney diet meals"
    },
    "ckd-label-scanner.html": {
        "description": "Upload a food nutrition label and instantly get CKD safety flags — phosphorus, potassium, sodium, and protein warnings for your kidney stage.",
        "keywords": "CKD food label scanner, kidney safe food checker Philippines, nutrition label kidney disease, phosphorus food label CKD, potassium food scanner, kidney food safety checker, food label analyzer CKD, packaged food kidney safe, dialysis food checker, kidney patient food app, food label scanner Philippines, CKD nutrition app, kidney safe packaged food, food label phosphorus checker, potassium food label scan, kidney diet food checker, supermarket kidney safe food, CKD food guide Philippines, food label reader kidney, nutrition facts kidney patient"
    },
    "ckd-mbd.html": {
        "description": "CKD-mineral bone disease: how kidney failure disrupts calcium, phosphorus, vitamin D, and PTH — causing bone loss and vessel hardening — with treatment options.",
        "keywords": "CKD mineral bone disease, CKD-MBD Philippines, kidney bone disease, phosphorus kidney disease, calcium kidney failure, PTH kidney disease, parathyroid kidney, vitamin D kidney, renal osteodystrophy, vascular calcification kidney, bone disease dialysis, CKD bone loss Philippines, secondary hyperparathyroidism, phosphate binder Philippines, calcitriol kidney, kidney bone pain, adynamic bone disease, dialysis bone disease, kidney mineral disorder, phosphorus control dialysis Philippines"
    },
    "ckd-mental-health-sleep.html": {
        "description": "How kidney disease affects mental health and sleep — depression, anxiety, cognitive changes, insomnia, restless legs, and evidence-based strategies to help.",
        "keywords": "kidney disease mental health Philippines, CKD depression, dialysis anxiety, kidney disease sleep problems, insomnia dialysis patient, restless leg syndrome kidney, CKD cognitive impairment, depression kidney failure, mental health dialysis Philippines, kidney disease brain fog, sleep disorder CKD, dialysis patient mental wellness, anxiety kidney disease, mental health support kidney Philippines, kidney patient psychology, depression treatment CKD, CKD sleep disturbance, dialysis insomnia, dialysis mental health, quality of life kidney disease"
    },
    "ckd-recipe-analyzer.html": {
        "description": "Paste any recipe and get a complete nutrition label with CKD safety flags — know if a dish is safe for your kidney stage before you cook it.",
        "keywords": "CKD recipe analyzer Philippines, kidney recipe nutrition calculator, recipe kidney safe checker, dialysis recipe analyzer, kidney diet recipe calculator, recipe phosphorus calculator, recipe potassium calculator, recipe sodium CKD, Filipino recipe kidney check, kidney safe recipe tool, recipe nutrition kidney disease, CKD food app Philippines, recipe analyzer dialysis patient, kidney diet recipe planner, Filipino recipe kidney analyzer, recipe ingredient kidney check, kidney friendly recipe app, nutrition recipe kidney calculator, recipe safety kidney, dialysis friendly recipe checker"
    },
    "ckd-statistics-philippines.html": {
        "description": "CKD statistics in the Philippines and Asia — why Filipinos are disproportionately affected, mortality data, dialysis access rates, and what the numbers mean for you.",
        "keywords": "CKD statistics Philippines, kidney disease Philippines data, kidney failure incidence Philippines, dialysis population Philippines, Filipino kidney disease burden, CKD epidemiology Philippines, ESRD Philippines statistics, kidney disease mortality Philippines, chronic kidney disease prevalence Philippines, NKF Philippines data, dialysis centers Philippines, kidney disease ASEAN, Filipino hypertension CKD, diabetes kidney disease Philippines, CKD awareness Philippines, PhilHealth dialysis statistics, kidney disease deaths Philippines, Philippine Society of Nephrology statistics, NKTI patient data, kidney disease public health Philippines"
    },
    "ckd-top5-mistakes.html": {
        "description": "The 5 most common mistakes kidney patients make — stopping medications, ignoring diet, missing labs, using herbal remedies, and skipping nephrologist visits.",
        "keywords": "kidney patient mistakes Philippines, CKD management errors, common dialysis mistakes, kidney disease misconceptions, stopping kidney medication, herbal remedy kidney danger, missing dialysis Philippines, kidney patient pitfalls, CKD self-management errors, kidney diet mistakes Philippines, skipping nephrologist Philippines, taking NSAIDs kidney disease, stopping antihypertensive kidney, common CKD errors, kidney patient education Philippines, medication compliance kidney, CKD progression mistakes, dialysis skip danger, kidney failure prevention mistakes, patient education nephrology"
    },
    "contrast-nephropathy.html": {
        "description": "Contrast-induced kidney injury from CT scans and angiograms — who is at risk, how to prevent it, and what to do if your kidneys worsen after a procedure.",
        "keywords": "contrast nephropathy Philippines, contrast-induced AKI, iodinated contrast kidney damage, CT scan kidney risk, angiogram kidney injury, contrast dye kidney disease, CKD contrast agent, pre-hydration contrast, N-acetylcysteine contrast kidney, contrast media kidney failure, kidney protection CT scan, iodine dye kidney, cardiology procedure kidney risk, kidney damage after angiogram, contrast CKD Philippines, preventing contrast nephropathy, creatinine after contrast, coronary angiogram kidney, cardiac catheterization kidney, kidney injury imaging"
    },
    "diabetes-kidneys.html": {
        "description": "How diabetes damages kidneys, blood sugar and protein targets to protect kidney function, Filipino diet tips, and medications like SGLT2 inhibitors that slow CKD.",
        "keywords": "diabetic kidney disease Philippines, diabetes and kidneys, diabetic nephropathy Philippines, blood sugar kidney, HbA1c kidney disease, proteinuria diabetes, SGLT2 inhibitor kidney, empagliflozin kidney, dapagliflozin diabetes kidney, diabetes CKD Philippines, kidney failure diabetes, Filipino diabetes kidney, ACE inhibitor diabetic kidney, ARB diabetes kidney, diabetes diet kidney Philippines, microalbuminuria diabetes, glucose control kidney, finerenone diabetic kidney, type 2 diabetes kidney disease, diabetic CKD treatment Philippines"
    },
    "dialysis-access-care.html": {
        "description": "Understanding dialysis access types — AV fistula, graft, catheter — and how to care for your access at home to prevent infection and clotting in the Philippines.",
        "keywords": "dialysis access care Philippines, AV fistula care, arteriovenous fistula, dialysis catheter care, fistula infection signs, fistula thrombosis, graft dialysis Philippines, dialysis access Philippines, fistula needle site care, permcath care, AV graft care, dialysis access complication, fistula bruit thrill, fistula check at home, dialysis line infection, dialysis access cleaning, buttonhole fistula, fistula maturation, hemodialysis access Philippines, vascular access care kidney"
    },
    "dialysis-adequacy.html": {
        "description": "What Kt/V and URR mean, why dialysis adequacy matters, your target numbers, and how to calculate if you are getting enough dialysis in the Philippines.",
        "keywords": "dialysis adequacy Philippines, Kt/V hemodialysis, URR dialysis, underdialysis symptoms, dialysis dose Philippines, adequate dialysis target, Kt/V calculation, URR calculation, dialysis adequacy test, hemodialysis Kt/V Philippines, peritoneal dialysis adequacy, weekly Kt/V peritoneal dialysis, inadequate dialysis signs, dialysis session length, dialysis blood flow rate, urea reduction ratio, dialysis efficiency Philippines, how to check dialysis adequacy, KDOQI dialysis adequacy, CAPD Kt/V Philippines"
    },
    "dialysis-coming-pre-eskd.html": {
        "description": "Pre-dialysis guide for Filipinos with eGFR 15-29 — choosing hemodialysis vs peritoneal dialysis, fistula timing, diet changes, PhilHealth Z-Benefit enrollment.",
        "keywords": "pre-dialysis Philippines, approaching dialysis, eGFR 15 29 kidney, when to start dialysis, pre-ESKD Philippines, choosing dialysis modality, hemodialysis vs peritoneal dialysis, fistula creation Philippines, AV fistula timing, peritoneal catheter Philippines, pre-dialysis diet, dialysis preparation Philippines, PhilHealth Z-benefit dialysis, conservative kidney management, dialysis decision Philippines, kidney failure approaching, ESKD preparation, pre-dialysis education, dialysis vs no dialysis Philippines, malapit na sa dialysis"
    },
    "dialysis-prescription.html": {
        "description": "Understanding your dialysis prescription — Kt/V targets, blood flow rate, dialysate composition, and how your nephrologist adjusts your hemodialysis or PD dose.",
        "keywords": "dialysis prescription Philippines, hemodialysis prescription, peritoneal dialysis prescription, Kt/V URR targets, blood flow rate dialysis, dialysate composition, dialysis session parameters, PD prescription CAPD CCPD, dialysis dose adjustment, heparin dialysis, dialysis machine settings, dialyzer selection, hemodialysis dose Philippines, peritoneal dialysis dose, dialysis adequacy KDOQI, UFR ultrafiltration rate, dialysis time per session, dialysis prescription explained, nephrologist dialysis order, dialysis parameters Philippines"
    },
    "dyslipidemia-2026.html": {
        "description": "2026 cholesterol guidelines for CKD and dialysis patients — LDL targets, statin safety in kidney disease, non-statin options, and cardiovascular risk reduction.",
        "keywords": "dyslipidemia CKD 2026, cholesterol guidelines kidney disease, LDL target CKD Philippines, statin kidney disease safe, atorvastatin CKD, rosuvastatin kidney, high cholesterol dialysis patient, ACC AHA 2026 kidney, cardiovascular risk CKD, triglycerides kidney disease, cholesterol control kidney, non-statin therapy CKD, ezetimibe kidney patient, fibrates kidney disease, PCSK9 inhibitor CKD, lipid management kidney Philippines, cholesterol kidney failure, statin dose adjustment CKD, dyslipidemia treatment kidney, heart disease prevention CKD Philippines"
    },
    "el-nino-heat-dialysis.html": {
        "description": "El Nino and extreme heat survival guide for Filipino dialysis patients — fluid management, brownout preparation, heat emergencies, and access care during hot season.",
        "keywords": "El Nino dialysis Philippines, extreme heat kidney disease, dialysis heat emergency, brownout dialysis Philippines, heat stroke kidney patient, fluid management hot weather dialysis, summer kidney disease Philippines, PAGASA heat dialysis, hot weather kidney failure, dehydration dialysis, dialysis missed session heat, water shortage kidney patient, dry weight heat dialysis, heat and fluid restriction, heat stroke prevention dialysis, power outage dialysis Philippines, dialysis schedule summer, extreme heat CKD Philippines, fluid overload heat, El Nino kidney care"
    },
    "exercise-guide-ckd.html": {
        "description": "Safe exercise program for CKD patients — walking, stretching, balance, aerobics, and strength training adapted for every kidney disease stage and dialysis patients.",
        "keywords": "exercise kidney disease Philippines, CKD exercise program, walking kidney patient, safe exercise dialysis, exercise hemodialysis patient, physical activity CKD, kidney disease fitness Philippines, exercise kidney failure, aerobic exercise CKD, strength training kidney disease, exercise guide kidney patient, kidney rehabilitation exercise, ehersisyo kidney patient, physical activity ESKD, exercise peritoneal dialysis, balance exercise kidney, stretching CKD, walking program dialysis, intradialytic exercise, CKD exercise safety Philippines"
    },
    "fluid-management-dialysis.html": {
        "description": "Fluid management for dialysis patients — understanding dry weight, interdialytic weight gain, fluid restriction, thirst management, and preventing fluid overload.",
        "keywords": "fluid management dialysis Philippines, fluid restriction hemodialysis, interdialytic weight gain, dry weight dialysis, fluid overload kidney, thirst management dialysis, water limit dialysis patient, fluid weight gain kidney, too much fluid dialysis, fluid control kidney disease, antok sa tubig dialysis, fluid restriction tips, heart failure fluid dialysis, pulmonary edema dialysis, hypertension fluid dialysis, fluid balance kidney, daily weight monitoring dialysis, fluid intake limit hemodialysis, fluid buildup kidney failure, water restriction kidney patient Philippines"
    },
    "food-kidney-toxins.html": {
        "description": "Foods that generate kidney toxins in CKD — high-protein meats, red meat, certain plants, and cooking methods that worsen kidney function in Filipino patients.",
        "keywords": "food kidney toxins Philippines, uremic toxins food, indoxyl sulfate food, p-cresol food CKD, red meat kidney disease, high protein kidney failure, kidney toxin foods Philippines, cooking methods kidney toxins, uremic precursors diet, gut microbiome kidney toxins, dietary kidney toxins, Filipino food kidney danger, star fruit kidney toxin, carambola kidney failure, food generate toxins kidney, protein restriction kidney, kidney toxin generating foods, Filipino kidney safe food choices, TMAO kidney disease, kidney diet toxin reduction"
    },
    "gdm-nutrition-nephrology.html": {
        "description": "Gestational diabetes and kidney health — nutrition guidance for pregnant Filipino women to protect kidneys and reduce future CKD risk after gestational diabetes.",
        "keywords": "gestational diabetes kidneys Philippines, GDM kidney risk, pregnancy diabetes kidney, gestational diabetes Filipino, GDM nutrition Philippines, gestational diabetes diet, pregnancy kidney disease, GDM CKD risk, pregnant diabetic kidney, postpartum kidney care GDM, gestational diabetes prevention kidney, pregnancy proteinuria, preeclampsia kidney Philippines, diabetes pregnancy Filipino diet, GDM management Philippines, kidney health pregnancy, post-GDM kidney monitoring, pregnancy nutrition kidney, gestational hypertension kidney, Filipino pregnancy diabetes kidney"
    },
    "glomerulonephritis.html": {
        "description": "Glomerulonephritis explained — types, diagnosis, symptoms like blood and protein in urine, and treatments to protect kidney function in Filipino patients.",
        "keywords": "glomerulonephritis Philippines, kidney inflammation, blood in urine kidney, protein urine kidney disease, nephritic syndrome Philippines, nephrotic syndrome Philippines, glomerulonephritis treatment, IgA nephropathy Philippines, lupus nephritis glomerulonephritis, kidney biopsy Philippines, MPGN Philippines, FSGS Philippines, membranous nephropathy Philippines, glomerulonephritis causes, glomerulonephritis symptoms, immunosuppressive therapy kidney, steroids glomerulonephritis, kidney inflammation treatment, hematuria kidney, glomerulonephritis Filipino patient"
    },
    "glp1-ozempic-ckd.html": {
        "description": "Ozempic (semaglutide) and GLP-1 drugs for kidney protection in type 2 diabetes and CKD — what the FLOW trial showed, who benefits, and access in the Philippines.",
        "keywords": "Ozempic kidney disease Philippines, semaglutide CKD, GLP-1 kidney protection, semaglutide diabetic kidney, FLOW trial CKD, Ozempic Philippines kidney, GLP-1 agonist CKD Philippines, semaglutide proteinuria, Ozempic type 2 diabetes kidney, weight loss kidney protection, GLP-1 kidney benefit, kidney protection diabetes drug, semaglutide dose kidney, Ozempic access Philippines, GLP-1 Philippines kidney, FDA approved kidney protection drug, Ozempic CKD trial, diabetes kidney drug Philippines, liraglutide kidney, tirzepatide kidney"
    },
    "gout-uric-acid.html": {
        "description": "Why uric acid builds up, how it damages joints and kidneys, gout flare prevention, low-purine Filipino foods, and allopurinol use in kidney disease patients.",
        "keywords": "gout Philippines, uric acid kidney disease, gout flares kidney, hyperuricemia CKD, allopurinol kidney, febuxostat kidney, gout Filipino diet, low purine foods Philippines, uric acid kidney stones, gout attack kidney, gout management Philippines, uric acid lowering therapy, gout and CKD, purine rich foods Philippines, gout prevention diet, uric acid joint pain, kidney stones uric acid, Filipino gout diet, gout causes Philippines, tae ng buto gout"
    },
    "heart-kidney-connection.html": {
        "description": "Why heart and kidney disease occur together — how each organ affects the other, cardiorenal syndrome, and strategies to protect both in Filipino patients.",
        "keywords": "heart kidney connection Philippines, cardiorenal syndrome, heart disease kidney failure, CKD heart failure, kidney heart link, heart failure kidney disease, cardiorenal syndrome Philippines, cardiac complications CKD, kidney disease cardiovascular risk, heart attack kidney failure, heart kidney CKD Philippines, heart failure dialysis, kidney protect heart, cardiorenal management Philippines, heart disease kidney protection, left ventricular hypertrophy kidney, cardiovascular CKD Philippines, heart kidney syndrome, kidney fluid heart, cardiorenal medicine Philippines"
    },
    "hematuria-blood-in-urine.html": {
        "description": "Blood in urine (hematuria) explained — causes from kidney stones to cancer, when it is an emergency, and what tests your doctor will order in the Philippines.",
        "keywords": "blood in urine Philippines, hematuria kidney disease, dugo sa ihi, red urine kidney, pink urine causes, gross hematuria Philippines, microscopic hematuria, blood urine causes, hematuria kidney stone, hematuria IgA nephropathy, blood urine bladder cancer, hematuria workup Philippines, hematuria UTI, blood urine infection, kidney cancer hematuria, urine blood kidney biopsy, glomerulonephritis hematuria, urology hematuria Philippines, hematuria evaluation, blood urine nephrologist Philippines"
    },
    "hemodialysis-complications.html": {
        "description": "Managing hemodialysis complications — low blood pressure, muscle cramps, arrhythmias, access infections, and headaches during and after dialysis sessions.",
        "keywords": "hemodialysis complications Philippines, dialysis low blood pressure, intradialytic hypotension, dialysis muscle cramps, pulikat dialysis, dialysis arrhythmia, dialysis access infection, dialysis headache, dialysis disequilibrium syndrome, hemodialysis side effects, dialysis complications treatment, IDH dialysis, fistula infection, dialysis fever, HD complications Philippines, dialysis hypotension management, muscle cramp dialysis treatment, chest pain dialysis, air embolism dialysis, dialysis complication prevention Philippines"
    },
    "hemodialysis-elderly.html": {
        "description": "Starting dialysis as an elderly patient — benefits, burdens, conservative management as an alternative, and family decision-making guidance for Filipino seniors.",
        "keywords": "dialysis elderly Philippines, hemodialysis senior patient, dialysis old age Philippines, kidney failure elderly Filipino, geriatric dialysis, conservative kidney management elderly, starting dialysis at 70 80, dialysis quality of life elderly, elderly kidney failure treatment, dialysis burden elderly, dialysis benefit senior citizen, kidney failure senior Philippines, geriatric nephrology Philippines, comfort care kidney failure elderly, dialysis decision elderly, aging kidney disease, kidney failure alternative elderly, matanda kidney failure, elderly ESKD Philippines, dialysis geriatric Philippines"
    },
    "hemodialysis-modalities.html": {
        "description": "Comparing hemodialysis types — conventional HD, hemodiafiltration, home HD, peritoneal dialysis, CRRT, SLED — and which is best for different patients in the Philippines.",
        "keywords": "hemodialysis modalities Philippines, hemodiafiltration Philippines, home hemodialysis Philippines, peritoneal dialysis Philippines, CRRT Philippines, SLED dialysis Philippines, dialysis types comparison, conventional hemodialysis, high-flux dialysis, online hemodiafiltration, dialysis modality choice, HDF Philippines, nocturnal hemodialysis, daily hemodialysis, CAPD CCPD Philippines, dialysis options Philippines, modality selection kidney failure, best dialysis type, kidney replacement therapy Philippines, dialysis technology Philippines"
    },
    "hemodialysis-transfer-guide.html": {
        "description": "How to safely transfer to a new hemodialysis center or nephrologist in the Philippines — PSN Endorsement Form, PhilHealth continuity, and avoiding missed sessions.",
        "keywords": "hemodialysis transfer Philippines, change dialysis center Philippines, transfer dialysis patient, PSN endorsement form, dialysis center change, new dialysis center Philippines, dialysis doctor transfer, PhilHealth dialysis transfer, dialysis continuity Philippines, transfer hemodialysis records, dialysis center referral Philippines, avoid missed dialysis transfer, dialysis transfer procedure, kidney doctor transfer Philippines, dialysis center move, transfer hemodialysis Philippines, PSN dialysis form, dialysis endorsement letter, nephrologist transfer Philippines, dialysis center switching Philippines"
    },
    "hemoperfusion-blood-purification.html": {
        "description": "Hemoperfusion for blood purification in kidney disease and poisoning — how it differs from dialysis, when it is used, and Philippine availability.",
        "keywords": "hemoperfusion Philippines, blood purification kidney disease, hemoperfusion vs dialysis, adsorption therapy kidney, cytokine removal hemodialysis, hemoperfusion poisoning treatment, HA330 hemoperfusion, protein-bound toxin removal, hemoperfusion Philippines availability, hemoperfusion CKD, blood purification CRRT, sepsis hemoperfusion, hemoperfusion liver failure, inflammatory mediator removal, uremic toxin adsorption, hemoperfusion renal failure, hemoperfusion indications, dialysis adsorption Philippines, hemoperfusion clinical use, blood purification therapy Philippines"
    },
    "herbal-nephropathy.html": {
        "description": "Herbal remedies that damage kidneys — aristolochic acid, tung shueh pills, Chinese herbs, Philippine plants — and how to protect your kidneys from herbal toxins.",
        "keywords": "herbal nephropathy Philippines, herbal kidney damage, aristolochic acid kidney, Chinese herbal kidney damage, herbal medicine kidney toxicity, tung shueh pills kidney, damong gamot bato, herbal kidney failure Philippines, toxic herbs kidneys, Filipino herbal kidney damage, kidney damage supplements, herbal AKI Philippines, plant nephrotoxicity, balut herbal kidney, traditional medicine kidney injury Philippines, DOH herbal warning kidney, herbal nephritis, Chinese herbs kidney, kidney safe herbal remedies, herbal supplement kidney risk Philippines"
    },
    "hypertensive-kidney-disease.html": {
        "description": "High blood pressure and kidney disease — how hypertension damages kidneys, blood pressure targets, medications, and lifestyle changes for Filipino CKD patients.",
        "keywords": "hypertensive kidney disease Philippines, high blood pressure kidney, hypertension CKD Philippines, kidney damage high blood pressure, blood pressure target kidney, ACE inhibitor kidney, ARB kidney disease, amlodipine kidney, antihypertensive CKD Philippines, hypertension nephropathy, blood pressure kidney Philippines, salt reduction kidney, mataas na presyon bato, kidney disease hypertension management, RAAS kidney, hypertension control CKD, nephrosclerosis Philippines, secondary hypertension kidney, blood pressure monitoring kidney, kidney failure hypertension Philippines"
    },
    "igan-guide.html": {
        "description": "IgA nephropathy patient guide — causes, symptoms, KDIGO 2025 treatment options including sparsentan and budesonide, monitoring, and support in the Philippines.",
        "keywords": "IgA nephropathy Philippines, IgAN patient guide, Berger disease Philippines, kidney disease hematuria protein, KDIGO 2025 IgAN treatment, sparsentan Philippines, budesonide IgAN, IgA nephropathy prognosis, IgAN immunosuppression, kidney biopsy IgAN Philippines, hematuria protein urine IgA, glomerulonephritis IgA Philippines, IgAN management Philippines, nephrologist IgAN Philippines, NKTI IgAN, IgA nephropathy Filipino patient, kidney inflammation IgA, IgA nephropathy steroid, IgAN risk factors, IgA nephropathy treatment 2025"
    },
    "innovative-technologies-ckd.html": {
        "description": "New technologies for kidney disease — wearable kidneys, biomarker tests, gene therapy, remote monitoring, and AI in nephrology care and the future of CKD treatment.",
        "keywords": "innovative kidney disease technology, wearable artificial kidney, kidney disease AI Philippines, biomarker kidney disease, gene therapy kidney, remote monitoring CKD, kidney technology Philippines, precision medicine kidney, artificial kidney wearable, stem cell kidney regeneration, kidney chip technology, AI nephrology Philippines, telemedicine kidney disease Philippines, CKD innovation, kidney replacement future, kidney organoid, novel kidney therapy Philippines, digital health kidney, kidney point of care test, ESKD technology future Philippines"
    },
    "ketogenic-chrononutrition-ckd.html": {
        "description": "Evidence-based review of ketogenic and low-carb diets in kidney disease, and how meal timing and circadian biology may benefit CKD patients — risks and benefits.",
        "keywords": "ketogenic diet kidney disease, keto diet CKD Philippines, low carb diet kidney, ketosis kidney patient, ketogenic diet renal, keto kidney stones, chrononutrition kidney disease, meal timing CKD, intermittent fasting kidney, time restricted eating CKD, circadian biology kidney, ketogenic diet risks kidney, very low carb CKD, keto and kidney, kidney diet low carbohydrate, ketogenic diet hemodialysis, keto diet proteinuria, low carb kidney Philippines, ketogenic diet kidney stone risk, keto CKD evidence"
    },
    "kidney-cancers.html": {
        "description": "Kidney cancer types, staging, and treatments — renal cell carcinoma, symptoms like blood in urine or back pain, surgery, immunotherapy, and outcomes in the Philippines.",
        "keywords": "kidney cancer Philippines, renal cell carcinoma Philippines, kidney tumor symptoms, blood in urine cancer, kidney cancer treatment Philippines, renal cell carcinoma treatment, nephrectomy Philippines, kidney cancer surgery, immunotherapy kidney cancer, sunitinib kidney cancer, kidney mass Philippines, kidney cancer staging, kidney cancer diagnosis, kidney cancer prognosis Philippines, renal cell carcinoma immunotherapy, back pain kidney cancer, kidney cancer nephrectomy, cancer sa bato, kidney cancer NKTI, transitional cell carcinoma kidney"
    },
    "kidney-physiology.html": {
        "description": "How your kidneys work — filtration, reabsorption, hormone production, blood pressure regulation, and electrolyte balance explained in plain language for patients.",
        "keywords": "how kidneys work Philippines, kidney physiology patient, kidney function explained, glomerular filtration, kidney tubule function, GFR kidney, erythropoietin kidney production, kidney blood pressure regulation, renin kidney, kidney electrolyte balance, kidney urine production, nephron function, kidney anatomy Philippines, kidney hormone production, kidney filtration explained, kidney acid base balance, creatinine clearance, kidney vitamin D, kidney phosphorus regulation, bato function Philippines"
    },
    "kidney-transplant.html": {
        "description": "Kidney transplant in the Philippines — who qualifies, living vs deceased donors, surgery, anti-rejection medications, long-term care, and Philippine transplant centers.",
        "keywords": "kidney transplant Philippines, bato transplant Philippines, transplant kidney, living donor kidney Philippines, deceased donor kidney, kidney transplant surgery Philippines, anti-rejection medication transplant, immunosuppression transplant, kidney transplant NKTI, transplant eligibility Philippines, kidney graft Philippines, tacrolimus kidney transplant, kidney transplant outcome Philippines, transplant waiting list Philippines, Philippine transplant law, kidney donor Philippines, kidney transplant cost Philippines, organ donation transplant Philippines, transplant kidney care, transplant rejection treatment"
    },
    "lab-interpreter-guide.html": {
        "description": "Enter your kidney lab values for instant color-coded interpretation — creatinine, eGFR, potassium, phosphorus — with KDIGO 2024 and ADA 2025 targets and PDF report.",
        "keywords": "kidney lab interpreter Philippines, lab results kidney disease, eGFR kidney Philippines, creatinine interpreter, kidney lab values Philippines, lab results CKD, understand lab results kidney, potassium lab kidney, phosphorus lab kidney, hemoglobin lab kidney, KDIGO 2024 lab targets, kidney lab PDF report, kidney function tests Philippines, lab result checker kidney, ADA 2025 lab targets, kidney lab normal values, GFR lab result Philippines, kidney lab interpretation, blood test kidney Philippines, interpret kidney labs Philippines"
    },
    "lab-interpreter.html": {
        "description": "Interactive laboratory interpreter for Filipino kidney patients — input your lab values and get instant plain-language interpretation of common kidney blood and urine tests.",
        "keywords": "lab interpreter kidney Philippines, kidney blood test interpreter, creatinine normal range Philippines, eGFR calculator Philippines, kidney lab results, BUN creatinine ratio, UPCR lab kidney, kidney function blood test Philippines, online lab interpreter kidney, kidney lab calculator, understanding kidney labs, creatinine eGFR Philippines, kidney test results Philippines, lab value kidney disease, nephrology lab guide Philippines, potassium normal range kidney, phosphorus lab CKD, hemoglobin kidney lab, albumin lab kidney, urine protein creatinine ratio"
    },
    "leptospirosis-nephropathy.html": {
        "description": "Leptospirosis and kidney failure in the Philippines — symptoms after flooding, when to go to the ER, treatment, and kidney recovery after leptospiral infection.",
        "keywords": "leptospirosis Philippines, leptospirosis kidney failure, leptospirosis after flood Philippines, leptospirosis symptoms kidney, leptospirosis ER Philippines, kidney failure after flood, leptospiral nephropathy, leptospirosis treatment Philippines, leptospirosis prevention, flood disease kidney Philippines, wading flood water kidney, leptospirosis dialysis Philippines, Weil disease Philippines, leptospirosis antibiotics Philippines, leptospirosis jaundice kidney, leptospirosis kidney recovery, kidney failure flooding Philippines, acute kidney injury leptospirosis, flood fever kidney Philippines, leptospirosis signs Philippines"
    },
    "living-with-dialysis.html": {
        "description": "Living well on hemodialysis — managing sessions, fistula care, diet and fluid limits, travel, relationships, work, and quality of life for Filipino dialysis patients.",
        "keywords": "living with dialysis Philippines, life on hemodialysis, dialysis quality of life Philippines, dialysis patient daily life, dialysis and work Philippines, dialysis and travel, dialysis diet daily, fistula care daily, hemodialysis schedule Philippines, dialysis patient lifestyle, dialysis and relationships, emotional life dialysis, dialysis patient community Philippines, hemodialysis 3 times week, dialysis patient tips Philippines, kidney failure lifestyle, dialysis sex life, dialysis patient activities, adapting to dialysis, dialysis patient support Philippines"
    },
    "lupus-nephritis.html": {
        "description": "Lupus nephritis guide — classes, diagnosis by kidney biopsy, treatment with mycophenolate and belimumab, monitoring, and protecting kidneys from SLE in the Philippines.",
        "keywords": "lupus nephritis Philippines, lupus kidney disease, SLE kidney Philippines, lupus nephritis treatment, mycophenolate mofetil lupus, belimumab lupus nephritis, voclosporin lupus Philippines, lupus kidney biopsy, lupus nephritis class III IV, lupus CKD Philippines, SLE nephritis treatment Philippines, lupus kidney monitoring, lupus nephritis prognosis, cyclophosphamide lupus, hydroxychloroquine lupus kidney, lupus kidney failure, Filipino lupus kidney, lupus nephritis diagnosis, ANA anti-dsDNA lupus kidney, lupus nephritis remission Philippines"
    },
    "managing-hypertension.html": {
        "description": "Managing high blood pressure — home monitoring, antihypertensive medications, lifestyle changes, salt reduction, and blood pressure targets for Filipino patients.",
        "keywords": "high blood pressure Philippines, hypertension management Filipino, mataas na presyon Philippines, blood pressure medication Philippines, antihypertensive drugs Philippines, blood pressure home monitoring, blood pressure target Philippines, salt reduction hypertension, lifestyle hypertension Philippines, amlodipine Philippines, losartan Philippines, hypertension diet Philippines, blood pressure control Philippines, hypertension Filipino diet, DASH diet Philippines, blood pressure monitor Philippines, hypertension treatment Philippines, blood pressure lifestyle, hypertension kidney Philippines, blood pressure tips Philippines"
    },
    "managing-kidney-stones.html": {
        "description": "Kidney stones — types, why they form, passing a stone safely, pain management, and diet and medication strategies to prevent recurrence in Filipino patients.",
        "keywords": "kidney stones Philippines, bato sa bato, kidney stone pain, urinary stone Philippines, kidney stone treatment, kidney stone prevention, calcium oxalate stone Philippines, uric acid stone Philippines, kidney stone Filipino diet, kidney stone hydration, kidney stone symptoms, passing kidney stone, kidney stone surgery Philippines, lithotripsy Philippines, kidney stone diet, urologist Philippines kidney stone, kidney stone type treatment, struvite kidney stone, cystine kidney stone, kidney stone recurrence prevention Philippines"
    },
    "meal-prep-fastfood-ckd.html": {
        "description": "Meal prep and fast food strategies for busy Filipino kidney patients — batch cooking, kidney-safe Jollibee and McDonald's orders, and traffic-light food guides.",
        "keywords": "meal prep kidney disease Philippines, CKD meal prep, kidney friendly fast food Philippines, Jollibee kidney patient, McDonald's kidney disease, kidney safe fast food Philippines, batch cooking kidney diet, kidney patient busy lifestyle, dialysis meal prep, fast food kidney safe order, kidney diet Philippines meal prep, CKD fast food guide, kidney patient food tips Philippines, Chowking kidney safe, quick kidney meals Philippines, kidney diet shortcut, Filipino fast food kidney, packed lunch kidney patient, renal diet meal planning Philippines, dialysis diet meal prep"
    },
    "metabolic-acidosis-ckd.html": {
        "description": "Metabolic acidosis in CKD — low bicarbonate causes, how it worsens kidney function and bones, and treatment with sodium bicarbonate tablets in Filipino patients.",
        "keywords": "metabolic acidosis CKD Philippines, low bicarbonate kidney, kidney acidosis treatment, sodium bicarbonate kidney, CKD acidosis Philippines, bicarbonate CKD, kidney acid base imbalance, low bicarb kidney, baking soda kidney disease, metabolic acidosis hemodialysis, bicarbonate target kidney disease, KDIGO bicarbonate kidney, acidosis CKD treatment Philippines, kidney metabolic acidosis symptoms, CKD G3 G4 acidosis, bicarbonate supplement kidney, acid imbalance kidney disease, kidney acidosis bone loss, metabolic acidosis muscle wasting, sodium bicarbonate CKD Philippines"
    },
    "microbiome-probiotics-health.html": {
        "description": "The gut microbiome and kidney health — how probiotics, prebiotics, and fiber reduce uremic toxins and support kidney and immune function in CKD patients.",
        "keywords": "gut microbiome kidney disease, probiotics CKD Philippines, gut health kidney, prebiotics kidney disease, fiber kidney CKD, gut bacteria uremic toxins, probiotics dialysis patient, synbiotics kidney, gut dysbiosis kidney disease, microbiome kidney Philippines, fermented food kidney, yogurt kidney patient, gut bacteria kidney health, uremic toxin gut, probiotic supplement kidney, gut kidney axis, microbiome CKD Philippines, Lactobacillus kidney, gut health dialysis, postbiotics kidney disease"
    },
    "muscle-building-supplements-ckd.html": {
        "description": "Muscle wasting in CKD — safe supplements, protein intake, exercise strategies, and what to avoid to preserve muscle mass in Filipino kidney disease patients.",
        "keywords": "muscle wasting CKD Philippines, sarcopenia kidney disease, protein kidney patient, creatine kidney disease, BCAA kidney CKD, muscle mass kidney failure, protein supplement dialysis Philippines, muscle building kidney safe, exercise CKD muscle, dialysis muscle loss, protein restriction kidney, muscle wasting dialysis, kidney patient protein intake, leucine kidney, whey protein kidney safe, CKD sarcopenia treatment, ketoacid supplement kidney, muscle preservation kidney disease Philippines, dialysis protein requirement, anabolic supplement kidney Philippines"
    },
    "new-therapeutic-agents-ckd.html": {
        "description": "New CKD drugs — SGLT2 inhibitors, finerenone, sparsentan, GLP-1 agonists, and emerging therapies that have transformed kidney disease treatment in the Philippines.",
        "keywords": "new kidney disease drugs Philippines, SGLT2 inhibitor kidney, empagliflozin kidney Philippines, dapagliflozin CKD, finerenone kidney, Kerendia Philippines, sparsentan kidney, GLP-1 kidney drug, new CKD treatment 2025, SGLT2 CKD Philippines, novel CKD therapy, kidney drug Philippines 2026, bardoxolone kidney, RNA therapy kidney, kidney drug pipeline Philippines, new nephrology drugs, empagliflozin EMPA-KIDNEY, dapagliflozin DAPA-CKD, CREDENCE trial kidney, CKD pharmacology Philippines"
    },
    "nsaid-kidney-injury.html": {
        "description": "NSAIDs and kidney injury — why ibuprofen, mefenamic acid (Ponstan), and diclofenac damage kidneys in CKD patients, and safer pain alternatives in the Philippines.",
        "keywords": "NSAIDs kidney damage Philippines, ibuprofen kidney disease, mefenamic acid kidney, Ponstan kidney damage, diclofenac kidney, naproxen kidney CKD, pain killer kidney damage Philippines, NSAID acute kidney injury, pain relief kidney safe, paracetamol vs NSAID kidney, over the counter pain killer kidney, NSAID kidney Philippines, ibuprofen CKD, kidney safe pain medication Philippines, Alaxan kidney damage, pain reliever kidney disease Philippines, kidney injury pain medication, NSAID alternatives kidney, safe analgesic kidney, anti-inflammatory kidney safe Philippines"
    },
    "nutrition-kidney-patients.html": {
        "description": "Filipino kidney diet guide — what to eat and avoid, low-potassium low-phosphorus foods, protein limits, meal plans, and label reading for CKD patients.",
        "keywords": "kidney diet Philippines, nutrition kidney disease, CKD diet Filipino, low potassium foods Philippines, low phosphorus diet kidney, kidney diet protein, Filipino kidney food list, kidney diet meal plan Philippines, kidney patient food guide, renal diet Philippines, dialysis diet Philippines, kidney safe foods, foods to avoid kidney disease, kidney diet vegetables Philippines, low sodium kidney diet, kidney diet fruits Philippines, phosphorus foods to avoid kidney, potassium foods kidney, kidney diet meat Philippines, Filipino renal diet guide"
    },
    "nutrition-labels-ckd.html": {
        "description": "How to read food labels for kidney disease — spotting hidden phosphorus, potassium, and sodium in Filipino supermarket products and understanding ingredient lists.",
        "keywords": "food labels kidney disease Philippines, nutrition facts CKD, reading food labels kidney, phosphorus food label, potassium food label kidney, sodium food label, hidden phosphorus additives, food label kidney safe, supermarket kidney Philippines, phosphate additives food label, potassium chloride food label, nutrition facts panel kidney, kidney safe processed food, food ingredient kidney, phosphorus additive label, low phosphorus packaged food, kidney patient shopping Philippines, food label reading guide, CKD supermarket guide, packaged food kidney patient Philippines"
    },
    "obesity-ckd.html": {
        "description": "Obesity and kidney disease in Filipinos — Asian BMI cutoffs, how excess weight damages kidneys, safe weight loss strategies, GLP-1 drugs, and dialysis considerations.",
        "keywords": "obesity kidney disease Philippines, overweight kidney damage, BMI kidney disease Filipino, Asian BMI cutoff kidney, weight loss CKD Philippines, obesity CKD Philippines, hyperfiltration obesity kidney, MASH kidney disease, weight loss kidney protection, GLP-1 weight loss kidney, bariatric surgery kidney, obesity dialysis paradox, obese kidney patient, weight kidney disease Philippines, Filipino obesity kidney, obesity proteinuria, overweight Filipino kidney, CKD weight management Philippines, dialysis obesity Philippines, obesity paradox dialysis"
    },
    "organ-donation-philippines.html": {
        "description": "Organ donation in the Philippines — how to register as a donor, kidney transplant waiting list, Philippine law, and why donation rates are critically low.",
        "keywords": "organ donation Philippines, kidney donation Philippines, how to register organ donor Philippines, Philippine organ donation law, kidney transplant waiting list Philippines, deceased donor Philippines, living organ donor Philippines, NKTI organ donation, OrganPH Philippines, organ donor card Philippines, organ donation awareness Philippines, kidney transplant donor Philippines, organ procurement Philippines, Philippine organ donation statistics, donate kidney Philippines, donor registration Philippines, posthumous kidney donation, organ donation Filipino culture, PDCT Philippines, kidney donation family Philippines"
    },
    "pain-management-ckd.html": {
        "description": "Managing pain safely with kidney disease — which painkillers to avoid, safe alternatives like paracetamol, gabapentin, and topical treatments for Filipino CKD patients.",
        "keywords": "pain management kidney disease Philippines, safe pain relief CKD, paracetamol kidney, gabapentin kidney pain, tramadol kidney disease, pain killers kidney failure Philippines, opioid kidney disease, painkiller CKD Philippines, kidney safe analgesic, NSAID avoid kidney, pain CKD treatment Philippines, nerve pain kidney disease, chronic pain dialysis, pain medication dialysis Philippines, topical pain relief kidney, pregabalin kidney pain, pain control kidney failure, safe pain medication CKD, neuropathic pain kidney, pain CKD Filipino patient"
    },
    "peritoneal-dialysis-ckd.html": {
        "description": "Peritoneal dialysis for kidney failure — how PD works, CAPD vs CCPD, advantages for Filipino patients, catheter care, and why more patients should consider home PD.",
        "keywords": "peritoneal dialysis Philippines, PD dialysis Philippines, CAPD Philippines, CCPD Philippines, home dialysis Philippines, peritoneal dialysis catheter, PD vs hemodialysis Philippines, peritoneal dialysis advantages, PD technique Philippines, dialysis at home Philippines, APD Philippines, peritoneal dialysis cost Philippines, PD fluid exchange, PD catheter care, peritoneal dialysis infection, PD Philippines training, peritoneal dialysis diet, PD solution Philippines, home kidney treatment Philippines, peritoneal dialysis Filipino patient"
    },
    "philhealth-z-packages.html": {
        "description": "PhilHealth Z-Benefit package guide for dialysis and kidney transplant — what is covered, how to enroll, session limits, copayments, and PC 2024-0023 updates.",
        "keywords": "PhilHealth Z package Philippines, PhilHealth dialysis benefit, PhilHealth kidney transplant coverage, PhilHealth Z benefit kidney, dialysis PhilHealth Philippines, PhilHealth hemodialysis coverage, PhilHealth peritoneal dialysis, PhilHealth kidney benefit 2024, PC 2024-0023 PhilHealth, PhilHealth Z-ESA, Z-MORPH PhilHealth, PhilHealth enrollment kidney, PhilHealth dialysis sessions covered, PhilHealth copayment dialysis, PhilHealth accredited dialysis center, kidney insurance Philippines, PhilHealth kidney failure, PhilHealth benefit package kidney, government kidney benefit Philippines, PhilHealth dialysis 2026"
    },
    "phosphorus-ckd.html": {
        "description": "Phosphorus in kidney disease — why it builds up, foods to avoid, phosphate binders explained, and how to protect bones and blood vessels in Filipino CKD patients.",
        "keywords": "phosphorus kidney disease Philippines, high phosphorus CKD, phosphate binder Philippines, phosphorus food kidney, calcium carbonate phosphate binder, sevelamer Philippines, lanthanum kidney, phosphorus control dialysis, phosphorus bone kidney, phosphorus vascular calcification, hyperphosphatemia kidney, phosphorus limit kidney, low phosphorus diet Philippines, phosphorus food list kidney, phosphorus kidney Philippines, phosphate binder meal timing, phosphorus dairy kidney, hidden phosphorus food, phosphorus soda kidney, phosphorus dialysis Philippines"
    },
    "polycystic-kidney-disease.html": {
        "description": "Polycystic kidney disease (PKD) explained — genetics, symptoms, how cysts grow, tolvaptan to slow progression, pain management, and living with PKD in the Philippines.",
        "keywords": "polycystic kidney disease Philippines, PKD Philippines, ADPKD Philippines, kidney cysts Philippines, polycystic kidney genetic, tolvaptan Philippines, ADPKD tolvaptan, kidney cyst treatment, PKD diagnosis, PKD progression, PKD pain management, ARPKD Philippines, PKD hereditary kidney disease, kidney cyst pain, PKD Filipino family, polycystic kidney symptoms, PKD kidney failure, PKD genetic testing Philippines, PKD blood pressure, PKD management Philippines"
    },
    "potassium-hyperkalemia-ckd.html": {
        "description": "Potassium and hyperkalemia in kidney disease — why potassium rises, dangerous levels, emergency treatment, low-potassium Filipino foods, and potassium binders.",
        "keywords": "hyperkalemia Philippines, high potassium kidney disease, potassium kidney danger, hyperkalemia treatment Philippines, potassium binder Philippines, patiromer Philippines, sodium zirconium cyclosilicate, potassium CKD, high potassium dialysis, low potassium foods Philippines, potassium kidney diet, dangerous potassium level, hyperkalemia ECG, banana kidney disease, potassium emergency kidney, kayexalate Philippines, potassium restriction CKD, hyperkalemia symptoms, potassium heart kidney, potassium level kidney patient Philippines"
    },
    "preventing-uti.html": {
        "description": "Preventing urinary tract infections — why UTIs recur, who is most at risk, practical hygiene steps, Filipino diet tips, and when to see a doctor in the Philippines.",
        "keywords": "UTI prevention Philippines, urinary tract infection kidney, UTI kidney patient, prevent UTI Philippines, UTI recurrence prevention, female UTI Philippines, UTI after sex, UTI hygiene Philippines, cranberry UTI Philippines, UTI symptoms Philippines, UTI antibiotics Philippines, UTI Filipino patient, UTI causes kidney damage, UTI bacteria Philippines, UTI urine test, UTI in diabetes Philippines, UTI prevention diet, UTI dehydration, catheter UTI prevention, UTI nephrology Philippines"
    },
    "prostate-enlargement.html": {
        "description": "Benign prostatic hyperplasia (BPH) — urinary symptoms, medications, lifestyle changes, and when surgery is needed to restore urinary flow in Filipino men.",
        "keywords": "prostate enlargement Philippines, BPH Philippines, enlarged prostate, prostate urinary problems, urinary retention Philippines, prostate medication Philippines, tamsulosin Philippines, finasteride prostate, BPH treatment Philippines, prostate Filipino men, urinary frequency prostate, urinary obstruction kidney, prostate and kidney disease, enlarged prostate treatment Philippines, prostate surgery Philippines, TURP Philippines, prostate ultrasound, prostate urology Philippines, obstructive uropathy Philippines, prostate urine flow Philippines"
    },
    "proteins-proteinuria.html": {
        "description": "Protein in urine (proteinuria) — what it means, how it is measured, why it damages kidneys, and proven strategies including ACE inhibitors and ARBs to reduce it.",
        "keywords": "proteinuria Philippines, protein in urine kidney, foamy urine kidney disease, bula sa ihi kidney, urine protein kidney, UPCR proteinuria Philippines, ACE inhibitor proteinuria, ARB reduce protein urine, proteinuria treatment Philippines, kidney protein leakage, protein urine test, microalbuminuria Philippines, nephrotic syndrome proteinuria, proteinuria causes, dipstick protein kidney, protein urine kidney damage, reduce proteinuria Philippines, kidney filter protein, diabetic proteinuria, hypertensive proteinuria Philippines"
    },
    "recurrent-uti-ckd.html": {
        "description": "Recurrent UTIs in CKD — why they are more dangerous for kidney patients, how infections drive kidney scarring, antibiotic management, and prevention strategies.",
        "keywords": "recurrent UTI kidney disease Philippines, UTI CKD Philippines, repeated UTI kidney, UTI kidney scarring, UTI kidney damage, recurrent UTI treatment CKD, UTI antibiotics kidney patient, pyelonephritis kidney, UTI CKD management, kidney infection recurrent, UTI prevention kidney, E. coli kidney infection, UTI sepsis kidney, urinary infection kidney disease, complicated UTI CKD, UTI kidney biopsy, UTI CKD prognosis, UTI prophylaxis kidney, urosepsis Philippines, recurrent kidney infection Philippines"
    },
    "slowing-ckd-progression.html": {
        "description": "How to slow kidney disease progression — blood pressure control, SGLT2 inhibitors, protein restriction, diabetes control, and lifestyle targets for every CKD stage.",
        "keywords": "slowing kidney disease Philippines, CKD progression prevention, kidney disease slow down, protect kidney function, CKD progression Philippines, SGLT2 inhibitor kidney protection, blood pressure kidney, protein restriction CKD, kidney disease management Philippines, kidney protection strategies, eGFR decline prevention, ACE ARB kidney, kidney disease lifestyle, diabetes kidney protection, smoking kidney disease, RAAS kidney, kidney progression Philippines, delay dialysis Philippines, kidney stage slowing, nephroprotective Philippines"
    },
    "sodium-salt-reduction-ckd.html": {
        "description": "Salt reduction guide for Filipino kidney patients — sodium targets, hidden salt in Filipino foods, practical swaps, soy sauce alternatives, and a daily intake calculator.",
        "keywords": "salt reduction kidney Philippines, low sodium kidney diet, sodium CKD Philippines, salt kidney disease, low sodium Filipino food, hidden salt Filipino food, patis sodium, toyo sodium kidney, bagoong kidney disease, reduce salt Philippines kidney, DASH diet kidney Philippines, salt substitute kidney, sodium target kidney, low sodium cooking Philippines, Filipino salt reduction, kidney salt limit, blood pressure salt kidney, Filipino food sodium content, salt reduction tips Philippines, sodium calculator kidney"
    },
    "stem-cells-ckd.html": {
        "description": "Stem cell therapy for kidney disease — what the science shows, why unproven Philippine stem cell clinics may be dangerous, and legitimate research on kidney regeneration.",
        "keywords": "stem cell kidney disease Philippines, stem cell therapy kidney, stem cell clinic Philippines, unproven stem cell treatment, kidney regeneration Philippines, stem cell CKD Philippines, stem cell dialysis treatment, kidney stem cell research, mesenchymal stem cell kidney, stem cell FDA Philippines, legitimate stem cell kidney, stem cell cure kidney Philippines, kidney repair stem cell, stem cell scam Philippines, regenerative medicine kidney, stem cell hemodialysis, kidney disease cure Philippines, stem cell trial kidney, exosome kidney therapy, stem cell CKD evidence"
    },
    "symptom-checker.html": {
        "description": "Interactive symptom checker for Filipino kidney, heart, and diabetes patients — tick your symptoms and get an instant triage recommendation: ER, urgent, or routine visit.",
        "keywords": "kidney symptom checker Philippines, CKD symptoms Philippines, kidney disease symptoms, dialysis symptom triage, kidney emergency symptoms, when to go ER kidney Philippines, kidney symptom guide, heart disease symptom checker, diabetes symptom checker, online symptom checker kidney Philippines, kidney disease warning signs, nephrology symptom triage, dialysis patient symptom, kidney patient ER guide, symptom checker Philippines, foamy urine symptom, swollen feet kidney, kidney symptom assessment, triage kidney symptoms, emergency kidney symptoms Philippines"
    },
    "transplant-allograft-failure.html": {
        "description": "When a transplanted kidney fails — causes of allograft failure, management, returning to dialysis, second transplant options, and emotional support in the Philippines.",
        "keywords": "transplant failure Philippines, kidney allograft failure, transplant rejection Philippines, chronic allograft nephropathy, failed kidney transplant, return to dialysis after transplant, second kidney transplant Philippines, transplant rejection treatment, tacrolimus rejection, antibody mediated rejection kidney, transplant failure causes, kidney graft loss Philippines, transplant kidney monitoring, rejection treatment Philippines, failed transplant CKD, re-listing transplant Philippines, calcineurin inhibitor kidney, transplant biopsy rejection, transplant nephropathy Philippines, kidney graft failure treatment"
    },
    "travel-dialysis-ckd.html": {
        "description": "Traveling with kidney disease or dialysis — booking dialysis centers abroad, medications for travel, diet on the road, and tips for Filipino CKD patients who want to travel.",
        "keywords": "travel dialysis Philippines, dialysis travel abroad, kidney disease travel tips, traveling kidney patient Philippines, dialysis vacation Philippines, book dialysis abroad, dialysis while traveling, dialysis center travel, travel medications kidney, kidney disease flight, dialysis travel insurance, OFW dialysis abroad, traveling with kidney failure, dialysis travel arrangements, kidney patient travel guide Philippines, dialysis passport Philippines, dialysis coordination travel, kidney diet travel, flying kidney patient, peritoneal dialysis travel"
    },
    "tuberculosis-kidney-disease.html": {
        "description": "Tuberculosis and kidney disease in the Philippines — how CKD increases TB risk, kidney TB symptoms, treatment challenges, rifampicin dose adjustments in kidney failure.",
        "keywords": "tuberculosis kidney Philippines, TB kidney disease, CKD tuberculosis Philippines, kidney TB Philippines, TB treatment kidney failure, rifampicin kidney, TB CKD drug adjustment, genitourinary TB Philippines, renal tuberculosis Philippines, TB dialysis Philippines, TB LTBI kidney, isoniazid kidney, TB risk CKD, TB CKD mortality, Philippine TB kidney burden, TB kidney biopsy, TB culture kidney, drug resistant TB kidney, TB prophylaxis kidney, BCG kidney disease Philippines"
    },
    "typhoon-disaster-preparedness-dialysis.html": {
        "description": "Typhoon preparedness for Filipino dialysis patients — emergency plans for missed sessions, medication supplies, evacuation, and safe fluid management during disasters.",
        "keywords": "typhoon dialysis Philippines, disaster preparedness kidney patient, dialysis emergency Philippines, missed dialysis typhoon, dialysis flood Philippines, dialysis patient typhoon plan, kidney disease emergency kit, dialysis during typhoon, emergency dialysis Philippines, typhoon kidney patient, missed dialysis session, dialysis center closed typhoon, fluid management disaster dialysis, dialysis medication supply typhoon, kidney patient evacuation, DOST PAGASA dialysis, dialysis crisis Philippines, kidney patient disaster plan, typhoon CKD patient, fluid overload missed dialysis"
    },
    "understanding-ckd.html": {
        "description": "Complete guide to chronic kidney disease — what CKD means, the 5 stages, causes, symptoms, lab targets, and what you can do today to protect your kidneys in the Philippines.",
        "keywords": "chronic kidney disease Philippines, CKD Philippines, sakit sa bato, kidney disease stages, CKD stage 3 4 5, eGFR kidney stages, kidney disease causes Philippines, CKD symptoms Philippines, swollen feet kidney, foamy urine, creatinine kidney disease, kidney disease diet Philippines, CKD management Philippines, kidney disease Filipino, CKD treatment Philippines, kidney failure prevention, nephrologist Philippines, NKTI Philippines, kidney disease hypertension diabetes Philippines, CKD patient guide Philippines"
    },
    "understanding-iron.html": {
        "description": "Iron and kidney disease — how the body uses iron for hemoglobin, three stages of iron deficiency, what blocks absorption, and why CKD patients need intravenous iron.",
        "keywords": "iron deficiency kidney disease Philippines, iron kidney anemia, serum ferritin kidney, TSAT iron kidney, oral iron supplement kidney, IV iron infusion Philippines, iron absorption kidney, iron deficiency anemia CKD, iron kidney dialysis, ferritin level kidney, iron status kidney patient, iron tablets kidney, iron kidney Philippines, iron supplement CKD, iron hemoglobin kidney, dietary iron kidney, iron blood test Philippines, iron deficiency stages, iron hepcidin kidney, iron replenishment kidney Philippines"
    },
    "understanding-lab-results.html": {
        "description": "Plain-language guide to kidney lab results — creatinine, BUN, eGFR, potassium, phosphorus, hemoglobin, albumin — what each means and when to be concerned in the Philippines.",
        "keywords": "understanding lab results kidney Philippines, kidney blood test results, creatinine normal range kidney, BUN blood urea nitrogen, eGFR kidney Philippines, potassium lab results kidney, phosphorus lab kidney, hemoglobin kidney patient, albumin lab kidney, kidney lab normal values, GFR kidney stage Philippines, kidney lab guide Filipino, urine protein test, UPCR kidney, 24-hour urine kidney, kidney blood test guide Philippines, bicarbonate lab kidney, calcium lab kidney, lab results kidney patient, kidney laboratory Philippines"
    },
    "uremic-pruritus-ckd.html": {
        "description": "Uremic itching in dialysis patients — causes, treatment options including difelikefalin, antihistamines, skin care, and improving sleep and quality of life in the Philippines.",
        "keywords": "uremic pruritus Philippines, dialysis itching, kidney disease itching, CKD itch Philippines, uremic itch treatment, difelikefalin Philippines, antihistamine kidney itch, kidney itch relief, dialysis patient itching, skin care kidney disease, hemodialysis pruritus, uremic pruritus treatment Philippines, chronic itch kidney failure, gabapentin kidney itch, pruritus dialysis Philippines, kidney itch causes, uremic toxin skin itch, nalbuphine kidney itch, phosphorus itching kidney, skin kidney disease Philippines"
    },
    "uremic-toxin-precursors.html": {
        "description": "Dietary uremic toxin precursors — tryptophan, tyrosine, choline, sulfur amino acids — how gut bacteria convert food into kidney-damaging toxins in CKD patients.",
        "keywords": "uremic toxin precursors Philippines, uremic toxins CKD, indoxyl sulfate diet, p-cresyl sulfate kidney, TMAO kidney disease, uremic toxin food sources, gut bacteria kidney toxins, dietary uremic precursors, tryptophan kidney toxin, choline kidney disease, kidney toxin diet, indole producing foods kidney, uremic metabolite food, gut dysbiosis kidney toxins, fiber uremic toxin, dietary intervention uremic toxins, uremic toxin reduction diet, gut microbiome kidney, low uremic toxin diet Philippines, kidney toxin precursor food"
    },
    "viral-infections-vaccinations-ckd.html": {
        "description": "Viral infections and vaccinations for CKD and dialysis patients — COVID-19, hepatitis B, influenza, pneumonia vaccines, and immune protection in the Philippines.",
        "keywords": "vaccination kidney disease Philippines, CKD vaccination Philippines, dialysis vaccination Philippines, hepatitis B vaccine kidney, COVID-19 vaccine kidney, influenza vaccine kidney, pneumococcal vaccine kidney, vaccine schedule CKD, kidney disease immunization Philippines, dialysis patient vaccine, CKD immune suppression, viral infection kidney, COVID kidney disease, hepatitis B dialysis Philippines, vaccination hemodialysis patient, kidney patient infection risk, flu shot kidney disease, kidney transplant vaccination, viral AKI kidney, immunization kidney failure Philippines"
    },
    "zero-balance-billing-philhealth.html": {
        "description": "PhilHealth Zero-Balance Billing explained for kidney patients — what it covers, which hospitals participate, and how to avoid out-of-pocket charges for dialysis in the Philippines.",
        "keywords": "zero balance billing PhilHealth Philippines, PhilHealth no balance billing, dialysis zero copay Philippines, PhilHealth kidney no copayment, zero balance billing dialysis, PhilHealth accredited hospital kidney, PhilHealth dialysis no out-of-pocket, balance billing PhilHealth, PhilHealth kidney benefit no charge, zero balance billing guide Philippines, PhilHealth hospital list kidney, ZBB PhilHealth dialysis, PhilHealth coverage kidney patient, government dialysis no cost Philippines, PhilHealth benefit full coverage kidney, no copay dialysis Philippines, PhilHealth Z benefit zero billing, patient rights PhilHealth, kidney patient PhilHealth rights, PhilHealth dialysis cost Philippines"
    },
}

AUTHOR = 'W. G. M. Rivero, MD, FPCP, DPSN'

def strip_html(text):
    """Remove HTML tags from text."""
    return re.sub(r'<[^>]+>', '', text).strip()

def fix_description(desc):
    """Strip HTML from description and truncate to 160 chars."""
    clean = strip_html(desc)
    # Remove ellipsis patterns from truncated descriptions
    clean = re.sub(r'\s*[—–-]?\s*\.\.\.$', '', clean).strip()
    clean = re.sub(r'\s*…$', '', clean).strip()
    if len(clean) > 160:
        clean = clean[:157] + '...'
    return clean

def process_file(filepath, meta):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()

    filename = os.path.basename(filepath)
    description = meta["description"]
    keywords = meta["keywords"]

    # Find existing description tag (various forms)
    # Pattern: <meta name="description" ...> or <meta content="..." name="description"/>
    desc_pattern = re.compile(
        r'<meta\s+(?:name=["\']description["\']\s+content=["\']([^"\']*)["\']|content=["\']([^"\']*)["\'])\s*name=["\']description["\']\s*/?>',
        re.IGNORECASE | re.DOTALL
    )
    # Also a simpler pattern for both orderings
    desc_pattern2 = re.compile(
        r'<meta\s[^>]*name=["\']description["\'][^>]*/?>',
        re.IGNORECASE | re.DOTALL
    )

    has_keywords = bool(re.search(r'<meta\s[^>]*name=["\']keywords["\'][^>]*/?>',
                                   content, re.IGNORECASE))
    has_author = bool(re.search(r'<meta\s[^>]*name=["\']author["\'][^>]*/?>',
                                 content, re.IGNORECASE))
    has_robots = bool(re.search(r'<meta\s[^>]*name=["\']robots["\'][^>]*/?>',
                                 content, re.IGNORECASE))

    # Find existing description match
    existing_desc_match = desc_pattern2.search(content)

    # Build the new description meta tag
    new_desc_tag = f'<meta name="description" content="{description}">'

    # Build extra tags to insert after description
    extra_tags = []
    if not has_keywords:
        extra_tags.append(f'<meta name="keywords" content="{keywords}">')
    if not has_author:
        extra_tags.append(f'<meta name="author" content="{AUTHOR}">')
    if not has_robots:
        extra_tags.append(f'<meta name="robots" content="index, follow">')

    # Fix OG description - find og:description and update if needed
    og_desc_pattern = re.compile(
        r'(<meta\s+property=["\']og:description["\']\s+content=["\'])([^"\']*)(["\']\s*/?>)',
        re.IGNORECASE
    )
    # Twitter description
    tw_desc_pattern = re.compile(
        r'(<meta\s+name=["\']twitter:description["\']\s+content=["\'])([^"\']*)(["\']\s*/?>)',
        re.IGNORECASE
    )

    if existing_desc_match:
        # Replace existing description tag, then insert extra tags after it
        old_desc_tag = existing_desc_match.group(0)
        new_block = new_desc_tag
        if extra_tags:
            new_block += '\n' + '\n'.join(extra_tags)
        content = content.replace(old_desc_tag, new_block, 1)
    else:
        # Insert before <link rel="canonical"> or before </head>
        canonical_match = re.search(r'<link rel=["\']canonical["\'][^>]*/?>',
                                     content, re.IGNORECASE)
        if canonical_match:
            new_block = new_desc_tag + '\n' + '\n'.join(extra_tags) + '\n' if extra_tags else new_desc_tag + '\n'
            content = content[:canonical_match.start()] + new_block + content[canonical_match.start():]
        else:
            # insert before </head>
            head_end = content.find('</head>')
            if head_end >= 0:
                new_block = (new_desc_tag + '\n' + '\n'.join(extra_tags) + '\n') if extra_tags else new_desc_tag + '\n'
                content = content[:head_end] + new_block + content[head_end:]

    # If keywords already existed but we need to update description only, add the new ones
    if has_keywords:
        # Still need to add author and robots if missing
        # Find any existing meta tag to insert after
        last_meta = None
        for m in re.finditer(r'<meta[^>]*/?>',content, re.IGNORECASE):
            last_meta = m
        # Actually, let's insert extra tags (author/robots) right after desc
        desc_match_new = desc_pattern2.search(content)
        if desc_match_new and (not has_author or not has_robots):
            remaining_extras = []
            if not has_author:
                remaining_extras.append(f'<meta name="author" content="{AUTHOR}">')
            if not has_robots:
                remaining_extras.append(f'<meta name="robots" content="index, follow">')
            if remaining_extras:
                insert_pos = desc_match_new.end()
                content = content[:insert_pos] + '\n' + '\n'.join(remaining_extras) + content[insert_pos:]

    # Update OG description
    def repl_og(m):
        return m.group(1) + description + m.group(3)
    content = og_desc_pattern.sub(repl_og, content)

    # Update Twitter description
    def repl_tw(m):
        return m.group(1) + description + m.group(3)
    content = tw_desc_pattern.sub(repl_tw, content)

    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)

    return True

def main():
    updated = 0
    skipped = []

    for filename, meta in GUIDE_META.items():
        filepath = os.path.join(GUIDES_DIR, filename)
        if not os.path.exists(filepath):
            print(f"MISSING: {filename}")
            skipped.append(filename)
            continue
        try:
            result = process_file(filepath, meta)
            if result:
                print(f"OK: {filename}")
                updated += 1
        except Exception as e:
            print(f"ERROR: {filename}: {e}")
            skipped.append(filename)

    print(f"\nDone: {updated} files updated, {len(skipped)} skipped.")
    if skipped:
        print("Skipped:", skipped)

if __name__ == "__main__":
    main()
