#!/usr/bin/env python3
"""
Expand data-text search terms for every guide tile in guides/index.html.
Run from the repo root: python3 expand_search_terms.py
"""

import re
from pathlib import Path

INDEX = Path("guides/index.html")

# Map each guide filename → full expanded data-text string.
# Terms are space-separated; no quotes inside the value (attribute uses double-quotes).
EXPANDED = {
    "hematuria-blood-in-urine.html": (
        "blood urine hematuria igA nephropathy bladder stones cystoscopy "
        "red urine gross microscopic RBC dipstick urinalysis bladder cancer "
        "renal cell cancer infection glomerulonephritis kidney biopsy painless hematuria"
    ),
    "lab-interpreter-guide.html": (
        "lab results interpreter kidney CBC metabolic lipids diabetes eGFR PDF "
        "blood test creatinine BUN potassium sodium albumin complete blood count "
        "cholesterol triglycerides glucose HbA1c A1C what does my test mean"
    ),
    "symptom-checker.html": (
        "symptom checker triage ER same-day kidney heart diabetes "
        "swelling edema breathless shortness of breath chest pain fever nausea "
        "vomiting fatigue weakness dizziness urgent emergency when to go hospital"
    ),
    "obesity-ckd.html": (
        "obesity overweight CKD BMI Asian GLP-1 bariatric MASH protein calorie "
        "weight loss semaglutide tirzepatide Mounjaro Wegovy Zepbound fat sarcopenic "
        "NAFLD fatty liver diet exercise waist circumference Filipino"
    ),
    "metabolic-acidosis-ckd.html": (
        "metabolic acidosis CKD bicarbonate KDIGO sodium bicarb "
        "low CO2 acid base breathing fatigue bone disease alkali supplement "
        "baking soda sodium bicarbonate Shohl solution citrate correction"
    ),
    "kidney-physiology.html": (
        "kidney physiology normal function filtration endocrine "
        "how kidneys work glomerulus tubule nephron erythropoietin renin "
        "vitamin D fluid balance waste removal urine anatomy renal function"
    ),
    "hypertensive-kidney-disease.html": (
        "hypertension kidney disease nephrosclerosis BP targets RAAS silent scarring "
        "high blood pressure renal artery ARB ACE inhibitor amlodipine 130/80 "
        "microalbuminuria hypertensive nephropathy target organ damage"
    ),
    "understanding-ckd.html": (
        "CKD chronic kidney disease stages understanding classification progression "
        "what is CKD GFR G1 G2 G3 G4 G5 A1 A2 A3 uremia end stage "
        "kidney failure renal disease eGFR creatinine diagnosis staging"
    ),
    "ckd-statistics-philippines.html": (
        "CKD statistics Philippines epidemiology NKTI dialysis 2024 "
        "prevalence incidence Filipino patients burden registry PhilHealth "
        "cost mortality kidney disease data national statistics"
    ),
    "ckd-top5-mistakes.html": (
        "CKD mistakes patients NSAIDs protein medication follow-up "
        "common errors avoid dehydration analgesics pain relievers herbal supplements "
        "salt restriction fluid restriction missed appointments self-medication"
    ),
    "slowing-ckd-progression.html": (
        "slowing CKD progression SGLT2 RAAS medications targets lifestyle glomerulus "
        "delay protect kidney empagliflozin dapagliflozin Jardiance Farxiga "
        "blood pressure control smoking cessation exercise proteinuria reduction"
    ),
    "proteins-proteinuria.html": (
        "proteinuria protein urine UACR RAAS SGLT2 sodium reduction "
        "albumin creatinine ratio ACR dipstick foam urine kidney damage marker "
        "protein leakage nephrotic reduce spilling protein microalbuminuria"
    ),
    "glomerulonephritis.html": (
        "glomerulonephritis IgA nephropathy lupus FSGS ANCA vasculitis biopsy nephrotic "
        "GN nephrotic syndrome edema swelling membranous minimal change "
        "anti-GBM crescentic immunosuppression steroid focal segmental"
    ),
    "igan-guide.html": (
        "IgA nephropathy KDIGO 2025 sparsentan budesonide SAR Philippines "
        "IgAN Berger disease hematuria proteinuria targeted release budesonide "
        "hydroxychloroquine SGLT2 RAS support treatment Nefecon"
    ),
    "ckd-children-young-adults.html": (
        "CKD children pediatric eGFR Schwartz transitional nephrology Alport NKTI "
        "kids congenital CAKUT reflux nephropathy growth stunting "
        "nephrotic syndrome young adult transition bedwetting recurrent infection"
    ),
    "living-with-dialysis.html": (
        "hemodialysis dialysis ESKD KDIGO 2024 fluid access complications "
        "life on dialysis HD machine AVF schedule 3x week diet restrictions "
        "quality of life sleep fatigue thirst fluid limit what to expect"
    ),
    "kidney-transplant.html": (
        "kidney transplant ESKD triple immunosuppression rejection Philippines surgery "
        "transplantation graft living donor deceased donor waiting list "
        "tacrolimus cyclosporine mycophenolate calcineurin inhibitor NKTI"
    ),
    "transplant-allograft-failure.html": (
        "transplant failure rejection allograft Banff 2022 re-transplant desensitization "
        "acute chronic rejection DSA donor specific antibody biopsy "
        "plasma cell rich AMR T cell mediated antibody mediated rejection"
    ),
    "dialysis-access-care.html": (
        "dialysis access fistula graft catheter PD Tenckhoff care complications "
        "AVF AV fistula arteriovenous graft tunneled catheter buttonhole cannulation "
        "infection thrombosis maturation steal syndrome needle technique"
    ),
    "anemia-management.html": (
        "anemia kidney EPO iron ESA hemoglobin dialysis ferritin TSAT "
        "erythropoietin darbepoetin mircera low hemoglobin fatigue blood transfusion "
        "iron deficiency IV iron Venofer Ferinject darbepoetin alfa HIF-PHI"
    ),
    "ckd-mbd.html": (
        "CKD-MBD mineral metabolism bone calcium phosphorus PTH vitamin D calcification "
        "renal osteodystrophy hyperphosphatemia hypocalcemia secondary hyperparathyroidism "
        "vascular calcification cinacalcet sevelamer phosphate binder calcium carbonate"
    ),
    "managing-kidney-stones.html": (
        "kidney stones urolithiasis tamsulosin MET stone types metabolic causes "
        "calcium oxalate uric acid struvite cystine renal colic flank pain "
        "KUB ultrasound ESWL PCNL ureteroscopy hydration potassium citrate"
    ),
    "kidney-cancers.html": (
        "kidney cancer RCC urothelial carcinoma Wilms tumor staging oncology "
        "renal cell carcinoma clear cell papillary chromophobe nephrectomy "
        "immunotherapy sunitinib pembrolizumab incidental mass CT scan"
    ),
    "fluid-management-dialysis.html": (
        "fluid management weight gain interdialytic sodium Filipino food dry weight UF rate "
        "fluid restriction overload shortness of breath IDH ultrafiltration "
        "edema swelling salt water limit thirst interdialytic weight gain"
    ),
    "potassium-hyperkalemia-ckd.html": (
        "potassium hyperkalemia CKD EKG Filipino food Kayexalate patiromer emergency dialysis "
        "high potassium heart arrhythmia peaked T waves banana saging kamote "
        "sodium zirconium SZC Veltassa Lokelma calcium gluconate cardiac"
    ),
    "uremic-pruritus-ckd.html": (
        "uremic pruritus itch dialysis gabapentin difelikefalin moisturizer quality of life "
        "kidney itch scratch skin dry CKD dialysis antihistamine ondansetron "
        "naltrexone emollient cream corticosteroid itching dialysis patients"
    ),
    "hemodialysis-elderly.html": (
        "dialysis elderly frailty CKM incremental hemodialysis conservative shared decision "
        "older patients senior geriatric conservative kidney management palliative "
        "withdrawal stopping dialysis quality of life functional status CKM"
    ),
    "peritoneal-dialysis-ckd.html": (
        "peritoneal dialysis CAPD APD PhilHealth 2025 catheter PD ESKD "
        "home dialysis exchanges dextrose peritonitis cloudy bag continuous ambulatory "
        "automated cycler catheter placement PD vs HD comparison"
    ),
    "caregiver-guide-ckd.html": (
        "caregiver CKD family burnout neglect diet NKTI spouse "
        "family member support carer mental health companion hospital visits "
        "palliative medication management emotional burden caregiver fatigue"
    ),
    "diabetes-kidneys.html": (
        "diabetes kidney hyperfiltration DKD SGLT2 glycation targets "
        "diabetic kidney disease diabetic nephropathy sugar insulin type 2 "
        "HbA1c blood glucose GLP-1 ACE ARB progression microalbuminuria"
    ),
    "gdm-nutrition-nephrology.html": (
        "GDM gestational diabetes nutrition nephrology ADA 2025 microalbuminuria postpartum "
        "pregnancy diabetes preeclampsia protein in urine gestational hypertension "
        "breastfeeding postpartum kidney monitoring diet maternal CKD"
    ),
    "managing-hypertension.html": (
        "hypertension blood pressure heart kidney brain medication RAAS lifestyle "
        "high blood pressure 140/90 antihypertensive amlodipine losartan valsartan "
        "enalapril lisinopril stroke heart attack target BP home monitoring"
    ),
    "cholesterol-diet-guide.html": (
        "cholesterol diet lipids liver Filipino food biochemistry "
        "LDL HDL triglycerides statins heart disease atherosclerosis ASCVD "
        "low fat omega-3 plant sterols Filipino meals hyperlipidemia"
    ),
    "dyslipidemia-2026.html": (
        "dyslipidemia 2026 guidelines LDL statin ezetimibe PCSK9 inclisiran CKD ACC AHA PREVENT "
        "high cholesterol rosuvastatin atorvastatin evolocumab alirocumab "
        "lipid lowering cardiovascular risk CKD Rosuvastatin Crestor Lipitor"
    ),
    "heart-kidney-connection.html": (
        "heart kidney cardiorenal syndrome SGLT2 heart failure "
        "cardiorenal type 1 2 3 4 5 heart failure EF preserved reduced "
        "fluid overload diuretic furosemide Lasix natriuretic peptide BNP"
    ),
    "gout-uric-acid.html": (
        "gout uric acid crystals Filipino febuxostat allopurinol CKD joints kidney "
        "tophus tophi acute flare joint pain colchicine NSAIDs steroid "
        "urate lowering xanthine oxidase inhibitor purine diet bigsang paa"
    ),
    "preventing-uti.html": (
        "UTI urinary tract infection recurrent antibiotic hydration CKD diabetes "
        "urinary burning dysuria frequency urgency E. coli fosfomycin "
        "trimethoprim nitrofurantoin cranberry D-mannose hygiene prevention"
    ),
    "recurrent-uti-ckd.html": (
        "recurrent UTI CKD progression AMR resistance nitrofurantoin D-mannose microbiome "
        "complicated pyelonephritis upper tract catheter CAUTI antibiotic resistance "
        "biofilm prophylaxis postcoital urosepsis relapse recurrence"
    ),
    "prostate-enlargement.html": (
        "BPH prostate enlargement IPSS LUTS obstruction kidney medications "
        "benign prostatic hyperplasia urinary retention weak stream nocturia "
        "tamsulosin finasteride dutasteride alpha blocker 5-ARI TURP prostatism"
    ),
    "understanding-lab-results.html": (
        "lab results understanding blood urine tests decoder "
        "what does blood test mean creatinine BUN eGFR electrolytes sodium potassium "
        "CBC hemoglobin WBC platelets urinalysis UA protein dipstick"
    ),
    "pain-management-ckd.html": (
        "pain management CKD NSAIDs mefenamic acid ibuprofen opioids neuropathy Philippine brands "
        "paracetamol acetaminophen Biogesic Panadol Cataflam Voltaren tramadol "
        "neuropathic gabapentin pregabalin safe analgesic kidney patients"
    ),
    "nutrition-kidney-patients.html": (
        "nutrition kidney patients CKD diet protein potassium phosphorus sodium Filipino "
        "renal diet food restriction what to eat kidney-friendly meal plan "
        "low potassium low phosphorus low sodium low protein nutritionist dietitian"
    ),
    "ckd-dri-calculator.html": (
        "CKD dietary reference intake DRI calculator protein potassium phosphorus sodium KDIGO KDOQI "
        "how much protein sodium potassium phosphorus to eat kidney nutritional "
        "needs daily intake calculator renal dietitian calculator"
    ),
    "ckd-recipe-analyzer.html": (
        "CKD recipe analyzer nutrition facts AI sodium potassium phosphorus Filipino food safety "
        "food analysis check my meal recipe nutrition CKD safe AI Filipino "
        "ingredients nutrient content cooking kidney disease"
    ),
    "sodium-salt-reduction-ckd.html": (
        "sodium salt reduction CKD patis bagoong Maggi noodles Filipino diet hypertension "
        "low salt diet fluid retention blood pressure Filipino seasoning "
        "soy sauce toyo cooking tricks less salt flavor substitute"
    ),
    "ckd-label-scanner.html": (
        "CKD nutrition label scanner OCR packaged food sodium potassium phosphorus "
        "read food label packaged grocery phosphate additives sodium content "
        "scan barcode ingredients list processed food Philippines"
    ),
    "ckd-friendly-recipes.html": (
        "CKD friendly recipes tinola sinigang inihaw tilapia Filipino cooking pre-dialysis HD "
        "low potassium meals leaching vegetables kidney-friendly Filipino recipe "
        "ideas healthy cooking dialysis patient traditional Filipino"
    ),
    "understanding-iron.html": (
        "iron anemia nutrition red cells ferritin TSAT CKD IV iron absorption deficiency "
        "iron deficiency low ferritin transferrin saturation oral IV Venofer "
        "Ferinject Injectafer food source absorption red meat leafy vegetables"
    ),
    "nutrition-labels-ckd.html": (
        "reading nutrition labels CKD supermarket phosphate additives potassium chloride grocery "
        "food packaging hidden phosphorus potassium hidden salt additives "
        "E-numbers preservatives buying guide Philippines supermarket grocery"
    ),
    "meal-prep-fastfood-ckd.html": (
        "meal prep fast food CKD Jollibee McDonald's KFC Chowking Mang Inasal leaching weekly plan "
        "eating out restaurant Philippines kidney diet ordering tips "
        "low potassium low sodium choices Chickenjoy Burger McDo"
    ),
    "ckd-friendly-recipes-regional.html": (
        "CKD regional Philippine recipes Kapampangan Ilocano Ilonggo Cebuano kare-kare pinakbet adobo "
        "regional Filipino food kidney-friendly Visayas Mindanao Ilocos Tagalog "
        "traditional recipes modified kidney disease Bisaya Bisayas"
    ),
    "ketogenic-chrononutrition-ckd.html": (
        "ketogenic chrononutrition CKD diet VLPD ketoanalogues circadian biology meal timing "
        "keto low carb time-restricted eating intermittent fasting very low protein "
        "supplemented ketoanalogues ketoacid analogues Ketosteril"
    ),
    "phosphorus-ckd.html": (
        "phosphorus CKD silent threat food labels phosphate binders Filipino diet "
        "high phosphorus hyperphosphatemia sevelamer calcium carbonate Phoslo Renvela "
        "bone disease vascular calcification dialysis phosphate binders food"
    ),
    "food-kidney-toxins.html": (
        "food kidney toxins phosphorus potassium sodium purines oxalate AGEs Filipino "
        "foods to avoid kidney damage processed advanced glycation end products "
        "starfruit carambola harmful foods purine-rich high oxalate"
    ),
    "uremic-toxin-precursors.html": (
        "uremic toxin precursors indoxyl sulfate p-cresyl TMAO gut bacteria probiotics prebiotics "
        "gut-kidney axis dysbiosis fermented foods yogurt fiber bowel health "
        "uremic toxin reduction gut permeability leaky gut CKD microbiome"
    ),
    "exercise-guide-ckd.html": (
        "exercise CKD physical activity warm-up aerobic resistance rehabilitation fall prevention "
        "walking jogging swimming cycling yoga sarcopenia muscle weakness "
        "deconditioning exercise prescription intradialytic exercise dialysis"
    ),
    "ckd-mental-health-sleep.html": (
        "CKD mental health sleep depression anxiety brain fog RLS restless legs apnea "
        "psychological quality of life fatigue cognitive impairment uremic "
        "encephalopathy insomnia CPAP mood disorder kidney psychiatry"
    ),
    "muscle-building-supplements-ckd.html": (
        "muscle building supplements CKD sarcopenia PEW L-carnitine omega-3 HMB creatine exercise gym "
        "protein wasting muscle loss protein energy wasting resistance training "
        "protein intake safe supplements creatine kidney fish oil"
    ),
    "travel-dialysis-ckd.html": (
        "travel dialysis CKD abroad medications fluid checklist PD "
        "holiday vacation guest dialysis ESKD travel tips medication list "
        "insurance letter doctor certificate abroad temporary center"
    ),
    "contrast-nephropathy.html": (
        "contrast nephropathy CIN AKI CT angiogram prevention protocol CKD "
        "iodinated contrast dye scan CT MRI gadolinium NSF hydration prevention "
        "acetylcysteine metformin hold pre-hydration saline kidney protection"
    ),
    "herbal-nephropathy.html": (
        "herbal nephropathy star fruit aristolochic acid tawatawa Vitamin C Philippines traditional "
        "herbal medicine kidney damage karela ampalaya sambong Banaba salabat "
        "ginger herbal supplements renal toxicity alternative medicine herba"
    ),
    "nsaid-kidney-injury.html": (
        "NSAIDs kidney injury ibuprofen mefenamic Ponstan diclofenac triple whammy CKD pain "
        "anti-inflammatory pain reliever prostaglandin AKI renal failure analgesic "
        "avoid RAAS diuretic combination Advil Motrin Cataflam Voltaren"
    ),
    "ckd-alternative-holistic-medicine.html": (
        "alternative medicine herbal sambong integrative safety myths Philippines CKD "
        "traditional Chinese medicine acupuncture supplements quack unproven therapy "
        "kidney tonic false claims integrative medicine evidence-based"
    ),
    "practical-outpatient-algorithms.html": (
        "outpatient algorithms edema hyperkalemia hyponatremia resistant hypertension AKI CKD referral "
        "anemia proteinuria metabolic acidosis GP internist clinical decision "
        "flowchart work-up diagnosis pathway FeNa eGFR iron dose anion gap "
        "hyponatremia correction primary care nephrology step-by-step"
    ),
    "new-therapeutic-agents-ckd.html": (
        "SGLT2 finerenone GLP-1 sparsentan HIF-PHI new drugs CKD 2025 Philippines "
        "emerging treatments breakthrough clinical trial novel JAK inhibitor "
        "complement daprodustat roxadustat avacopan belimumab voclosporin"
    ),
    "glp1-ozempic-ckd.html": (
        "GLP-1 semaglutide Ozempic CKD FLOW trial FDA 2025 diabetes muscle Philippines cost "
        "Rybelsus Wegovy weight loss injection tirzepatide Mounjaro Zepbound "
        "kidney protection obesity Philippines price liraglutide Victoza"
    ),
    "innovative-technologies-ckd.html": (
        "innovative technologies kidney biomarkers wearable AI remote monitoring gene therapy Philippines "
        "artificial intelligence telemedicine digital health app smartwatch "
        "biomarker precision medicine CRISPR kidney chip organoid"
    ),
    "hemodialysis-modalities.html": (
        "hemodialysis modalities HDF home HD CRRT SLED PD clearance molecules comparison "
        "online hemodiafiltration home hemodialysis high-flux nocturnal short daily "
        "SLED CRRT clearance middle molecules high-efficiency"
    ),
    "stem-cells-ckd.html": (
        "stem cells CKD MSC myth commercial clinics reality evidence Philippines "
        "stem cell therapy regenerative medicine clinical trial unproven Philippines "
        "cost risk evidence-based mesenchymal stem cell"
    ),
    "dialysis-adequacy.html": (
        "dialysis adequacy Kt/V URR KDIGO 2024 spKtV Daugirdas hemodialysis PD calculator "
        "adequate dialysis urea reduction ratio target underdialysis blood flow "
        "time per session PD adequacy clearance adequacy testing"
    ),
    "dialysis-prescription.html": (
        "dialysis prescription Kt/V UFR HD PD adequacy KDOQI adjustment special populations "
        "dialysis order blood flow dialysate flow time per session membrane flux "
        "ultrafiltration rate incremental dialysis individualized"
    ),
    "lupus-nephritis.html": (
        "lupus nephritis SLE ISN RPS biopsy MMF cyclophosphamide belimumab voclosporin Philippines "
        "systemic lupus class III IV V ANA anti-dsDNA complement C3 C4 "
        "flare remission immunosuppression steroid taper mycophenolate"
    ),
    "polycystic-kidney-disease.html": (
        "polycystic kidney disease PKD ADPKD tolvaptan genetics total kidney volume intracranial aneurysm "
        "autosomal dominant cysts liver cysts pain hematuria hereditary family "
        "history Jinarc mutation PKD1 PKD2 enlarged kidneys"
    ),
    "microbiome-probiotics-health.html": (
        "microbiome probiotics prebiotics synbiotics gut kidney Renadyl psyllium CKD "
        "gut bacteria fermented food yogurt kefir fiber bowel health "
        "uremic toxin reduction gut permeability leaky gut dysbiosis"
    ),
    "dialysis-coming-pre-eskd.html": (
        "pre-dialysis preparing ESKD eGFR 15-29 AVF modality PhilHealth decision tools transplant "
        "approaching dialysis kidney failure starting dialysis access creation "
        "fistula graft PD catheter early referral modality choice"
    ),
    "advance-care-planning-dialysis.html": (
        "advance care planning ACP dialysis goals of care withdrawal Filipino family Philippines "
        "end of life palliative withdrawal stopping dialysis conservative management "
        "living will DNAR Do Not Resuscitate family meeting hospice"
    ),
    "el-nino-heat-dialysis.html": (
        "El Nino heat dialysis brownout HD PD Philippines protocol hyperkalemia cool dialysate "
        "summer heat stroke dehydration hot weather fluid intake power outage "
        "dialysis emergency heat stress Philippines climate change"
    ),
    "typhoon-disaster-preparedness-dialysis.html": (
        "typhoon disaster preparedness dialysis PAGASA go-bag HD PD evacuation NDRRMC Philippines "
        "bagyo flood storm surge emergency dialysis kit medications supply "
        "stockpile communication hospital disaster preparedness kidney"
    ),
    "hemodialysis-complications.html": (
        "hemodialysis complications IDH hypotension cramps arrhythmia infection disequilibrium access "
        "intradialytic hypotension muscle cramps disequilibrium fever chills rigors "
        "air embolism clotting hemolysis sudden drop blood pressure"
    ),
    "hemodialysis-transfer-guide.html": (
        "transfer dialysis center change nephrologist PSN HPEF endorsement form patient rights PhilHealth "
        "switching dialysis center transfer letter records endorsement BHERT "
        "patient rights PhilHealth coverage new center"
    ),
    "cardiac-rehab-ckd-post-mi.html": (
        "cardiac rehabilitation CKD post-MI acute MI cardiorenal exercise ECG Mediterranean renal diet "
        "heart attack rehabilitation cardiac exercise ECG monitoring "
        "secondary prevention beta-blocker aspirin statin angina ischemic"
    ),
    "acute-kidney-injury-on-ckd.html": (
        "AKI-on-CKD acute kidney injury KDIGO staging triple whammy contrast rhabdomyolysis sick day rules "
        "sudden kidney worsening creatinine rise dehydration sepsis "
        "NSAID diuretic ACE ARB hold medications sick day decompensation"
    ),
    "hemoperfusion-blood-purification.html": (
        "hemoperfusion critical care HA130 HA330 HPHD sepsis Philippines DSWD Helande "
        "blood purification hemoadsorption ICU cytokine storm severe sepsis "
        "charcoal resin Philippines cost critical illness organ support"
    ),
    "leptospirosis-nephropathy.html": (
        "leptospirosis flood fever AKI Weil's disease typhoon wading doxycycline Manila Bicol "
        "leptospira flood water wading AKI jaundice pulmonary hemorrhage "
        "penicillin amoxicillin prophylaxis Philippines monsoon season"
    ),
    "organ-donation-philippines.html": (
        "organ donation Philippines transplant donor registry PODRRS PCP 2025 myths "
        "deceased donor living donor brain death donor card NKTI registry "
        "waiting list organ procurement transplant law Philippines consent"
    ),
    "philhealth-z-packages.html": (
        "PhilHealth Z package peritoneal dialysis kidney transplant benefits Z benefit PD KT "
        "Z benefit coverage indigent NHCP NKTI hospital package "
        "reimbursement PhilHealth benefits dialysis cost financial aid"
    ),
    "ckd-financial-stress.html": (
        "CKD financial stress cost PhilHealth PCSO DSWD Malasakit PWD Senior dialysis Philippines "
        "financial aid assistance charity fund indigent patient senior citizen "
        "PWD discount Malasakit Center PhilHealth social worker"
    ),
    "viral-infections-vaccinations-ckd.html": (
        "vaccinations CKD HBV influenza COVID VZV transplant dialysis uremic immunoparalysis eGFR "
        "hepatitis B vaccine flu shot COVID-19 pneumococcal varicella zoster "
        "shingles vaccine schedule immune compromised kidney failure"
    ),
    "tuberculosis-kidney-disease.html": (
        "tuberculosis TB kidney disease CKD dialysis transplant rifampicin tacrolimus renal dose "
        "TB CKD drug dosing renal adjustment HRZE DOTS program Philippines "
        "immunosuppression drug interaction anti-TB latent TB"
    ),
    "buko-juice-alkaline-water-ckd.html": (
        "buko juice coconut alkaline water CKD myths hyperkalemia dialysis Philippines Filipino "
        "coconut water buko safe drink kidney disease ionized water pH myths "
        "Filipino remedies herbal drink kidney patient safe or not"
    ),
    "alcohol-ckd.html": (
        "alcohol CKD lambanog SMB beer dialysis drug interactions harm reduction Filipino "
        "drinking alcohol safe kidney Red Horse gin Tanduay Ginebra San Miguel "
        "kidney effect Filipino tuba basi beer wine spirits"
    ),
    "zero-balance-billing-philhealth.html": (
        "zero balance billing ZBB PhilHealth UHC patient rights R.A. 11223 hospital myths gaps "
        "no out-of-pocket PhilHealth coverage hospital billing rights balance "
        "billing ban UHC universal health care gaps exceptions"
    ),
}


def expand_data_text(html: str) -> tuple[str, int]:
    count = 0
    for filename, new_text in EXPANDED.items():
        # Collapse whitespace in new_text
        new_text_clean = " ".join(new_text.split())
        pattern = rf'(<a\s[^>]*href="{re.escape(filename)}"[^>]*data-text=")[^"]*(")'
        replacement = rf'\g<1>{new_text_clean}\g<2>'
        new_html, n = re.subn(pattern, replacement, html)
        if n:
            html = new_html
            count += n
        else:
            print(f"  WARNING: no match found for {filename}")
    return html, count


def main():
    html = INDEX.read_text(encoding="utf-8")
    print(f"Expanding search terms in {INDEX} …")
    new_html, total = expand_data_text(html)
    if total == 0:
        print("No changes made.")
        return
    INDEX.write_text(new_html, encoding="utf-8")
    print(f"Done — updated {total} guide tile(s).")


if __name__ == "__main__":
    main()
