# -*- coding: utf-8 -*-
"""Shared data for the Nephrology Nursing & Hemodialysis course.

Edited by hand; consumed by generate_nursing_course.py. American English only.
Nothing here is rendered until the generator runs.
"""

COURSE = {
    "title": "Nephrology Nursing & Hemodialysis",
    "hub_slug": "nephrology-nursing",
    "educator_slug": "nephrology-nursing-educator",
    "label": "Self-study for registered nurses",
    "review_date": "2026-11-23",
    "card_teaser": (
        "A study series for registered nurses, from kidney assessment and CKD to safe "
        "hemodialysis care. Each module includes a nursing case and a self-assessment "
        "with answer rationales."
    ),
    "card_cta": "View the syllabus and start learning.",
}

# id, slug suffix, title, short title, week, nephrology-path role, hemodialysis-path role
# role: "core" = emphasized on that path; "foundation" = shared foundation
MODULES = [
    ("01", "kidney-function-renal-assessment", "Kidney Function and Renal Assessment", "Renal assessment", "core", "core"),
    ("02", "ckd-identification-staging", "CKD Identification, Staging, and Progression", "CKD staging", "core", "foundation"),
    ("03", "ckd-complications-nutrition-medicines", "CKD Complications, Nutrition, and Medicines", "CKD complications", "core", "foundation"),
    ("04", "aki-acute-kidney-support", "AKI and Acute Kidney Support", "AKI", "core", "foundation"),
    ("05", "kidney-failure-treatment-choices", "Kidney Failure, Treatment Choices, and Conservative Care", "Treatment choices", "core", "foundation"),
    ("06", "hd-principles-prescription-adequacy", "HD Principles, Prescription, and Adequacy", "HD prescription", "foundation", "core"),
    ("07", "hd-vascular-access-infection-prevention", "HD Vascular Access and Infection Prevention", "Vascular access", "foundation", "core"),
    ("08", "hd-equipment-water-dialysate-safety", "HD Equipment, Water, and Dialysate Safety", "Water and dialysate", "foundation", "core"),
    ("09", "hd-session-complication-response", "The Complete HD Session and Complication Response", "HD session", "foundation", "core"),
    ("10", "pd-home-dialysis-nursing", "PD and Home Dialysis Nursing", "PD and home dialysis", "core", "foundation"),
    ("11", "transplantation-special-populations", "Transplantation and Special Populations", "Transplant", "core", "foundation"),
    ("12", "philippine-practice-quality-capstone", "Philippine Practice, Quality Improvement, and Capstone", "Practice and quality", "core", "core"),
    # core module added after the PSN Basic Course review; studied before the capstone on both paths
    ("14", "living-well-hemodialysis", "Living Well on Hemodialysis: Mind, Behavior, and Longevity", "Living well on HD", "core", "core"),
    # core modules added to complete the curriculum
    ("15", "glomerular-systemic-kidney-disease", "Glomerular and Systemic Kidney Diseases", "Glomerular and systemic disease", "core", "core"),
    ("16", "supportive-palliative-kidney-care", "Supportive, Palliative, and End-of-Life Kidney Care", "Palliative and end-of-life care", "core", "core"),
    ("17", "teaching-evidence-based-practice", "Patient Teaching, Health Literacy, and Evidence-Based Practice", "Teaching and evidence", "core", "core"),
    # advanced module, studied after the capstone on both paths
    ("13", "convective-therapies-crrt-hdf", "Convective Therapies: CRRT and Hemodiafiltration", "Continuous therapy and hemodiafiltration", "advanced", "advanced"),
]

# Suggested study order on each path (module ids)
PATH_ORDER = {
    "neph": ["01", "02", "15", "03", "04", "05", "06", "07", "08", "09", "10", "11", "14", "16", "17", "12", "13"],
    "hd": ["01", "06", "07", "08", "09", "14", "02", "03", "04", "05", "16", "10", "11", "15", "17", "12", "13"],
}

# ── Abbreviations: used to build each page's glossary automatically ──────────
# key = token as written in the text; value = (expansion, glossary note or "")
ABBR = {
    "ACLS": ("Advanced Cardiovascular Life Support", ""),
    "ACR": ("albumin-to-creatinine ratio", "Urine albumin divided by urine creatinine in a spot sample."),
    "AHA": ("American Heart Association", ""),
    "AKD": ("acute kidney disease", "Kidney damage or reduced function lasting up to 3 months."),
    "AKI": ("acute kidney injury", ""),
    "ANNA": ("American Nephrology Nurses Association", ""),
    "AO": ("Administrative Order", "A regulatory issuance of the Department of Health."),
    "APD": ("automated peritoneal dialysis", "Exchanges performed by a cycler machine, usually overnight."),
    "AVF": ("arteriovenous fistula", "A surgical connection of an artery to a vein, used for needle access."),
    "AVG": ("arteriovenous graft", "A synthetic tube joining an artery and a vein."),
    "BLS": ("Basic Life Support", ""),
    "BSI": ("bloodstream infection", ""),
    "BUN": ("blood urea nitrogen", ""),
    "CAPD": ("continuous ambulatory peritoneal dialysis", "Manual exchanges several times a day."),
    "CBC": ("complete blood count", ""),
    "CDC": ("Centers for Disease Control and Prevention", "United States public health agency."),
    "CDN": ("Certified Dialysis Nurse", "A credential of the Nephrology Nursing Certification Commission."),
    "CFU": ("colony-forming unit", "The count of viable bacteria in a water sample."),
    "CKD": ("chronic kidney disease", ""),
    "CKD-MBD": ("chronic kidney disease–mineral and bone disorder", ""),
    "CKM": ("conservative kidney management", "Planned, comprehensive kidney-failure care without dialysis."),
    "CPD": ("Continuing Professional Development", ""),
    "CPR": ("cardiopulmonary resuscitation", ""),
    "CQI": ("continuous quality improvement", ""),
    "CRRT": ("continuous renal replacement therapy", ""),
    "CVVH": ("continuous venovenous hemofiltration", "Continuous therapy that clears solutes by convection, with replacement fluid."),
    "CVVHD": ("continuous venovenous hemodialysis", "Continuous therapy that clears solutes by diffusion into dialysate."),
    "CVVHDF": ("continuous venovenous hemodiafiltration", "Continuous therapy that combines diffusion and convection."),
    "IV": ("intravenous", ""),
    "SCUF": ("slow continuous ultrafiltration", "Continuous fluid removal without replacement fluid or dialysate."),
    "SLED": ("sustained low-efficiency dialysis", "A prolonged intermittent therapy run over many hours with a standard machine."),
    "HDF": ("hemodiafiltration", "Hemodialysis combined with large-volume convection and online replacement fluid."),
    "CVC": ("central venous catheter", ""),
    "DGF": ("delayed graft function", "Need for dialysis within the first week after a kidney transplant."),
    "DOH": ("Department of Health", "Philippines."),
    "ECG": ("electrocardiogram", ""),
    "EDTNA/ERCA": ("European Dialysis and Transplant Nurses Association/European Renal Care Association", ""),
    "eGFR": ("estimated glomerular filtration rate", ""),
    "ESA": ("erythropoiesis-stimulating agent", "For example epoetin or darbepoetin."),
    "EU": ("endotoxin unit", "The measure of bacterial endotoxin in a water sample."),
    "GFR": ("glomerular filtration rate", ""),
    "HBV": ("hepatitis B virus", ""),
    "HBsAg": ("hepatitis B surface antigen", ""),
    "HCV": ("hepatitis C virus", ""),
    "HD": ("hemodialysis", ""),
    "HIV": ("human immunodeficiency virus", ""),
    "ICU": ("intensive care unit", ""),
    "IDH": ("intradialytic hypotension", ""),
    "IDWG": ("interdialytic weight gain", "Fluid weight gained between two dialysis sessions."),
    "ISO": ("International Organization for Standardization", ""),
    "ISPD": ("International Society for Peritoneal Dialysis", ""),
    "KDIGO": ("Kidney Disease: Improving Global Outcomes", "The international nephrology guideline body."),
    "KDOQI": ("Kidney Disease Outcomes Quality Initiative", "Guideline program of the United States National Kidney Foundation."),
    "KFRE": ("Kidney Failure Risk Equation", ""),
    "KRT": ("kidney replacement therapy", "Dialysis or transplantation."),
    "NNCC": ("Nephrology Nursing Certification Commission", ""),
    "NSAID": ("nonsteroidal anti-inflammatory drug", ""),
    "PD": ("peritoneal dialysis", ""),
    "PDSA": ("Plan–Do–Study–Act", "A small, fast test-of-change cycle."),
    "PhilHealth": ("Philippine Health Insurance Corporation", ""),
    "PIRRT": ("prolonged intermittent renal replacement therapy", ""),
    "PPE": ("personal protective equipment", ""),
    "PRC": ("Professional Regulation Commission", "Philippines."),
    "PSN": ("Philippine Society of Nephrology", ""),
    "PTH": ("parathyroid hormone", ""),
    "RO": ("reverse osmosis", "The core water-purification stage of a dialysis water system."),
    "SBAR": ("Situation, Background, Assessment, Recommendation", "A structured handoff format."),
    "SGLT2": ("sodium-glucose cotransporter-2", ""),
    "TSAT": ("transferrin saturation", "An index of iron available for red-cell production."),
    "UF": ("ultrafiltration", "Removal of plasma water across the dialyzer membrane by a pressure gradient."),
    "UFR": ("ultrafiltration rate", ""),
    "URR": ("urea reduction ratio", ""),
    "VND": ("venous needle dislodgement", ""),
}

# ── References not taken from PubMed (hand-built APA 7) ───────────────────────
MANUAL_REFS = {
    "doh2012": (
        'Department of Health (DOH). (2012). <em>Administrative Order No. 2012-0001: New rules and regulations '
        'governing the licensure and regulation of dialysis facilities in the Philippines</em>. Republic of the Philippines. '
        '<a href="https://hfsrb.doh.gov.ph/wp-content/uploads/2021/05/AO-2012-0001.pdf">https://hfsrb.doh.gov.ph/wp-content/uploads/2021/05/AO-2012-0001.pdf</a>'
    ),
    "doh2013": (
        'Department of Health (DOH). (2013). <em>Administrative Order No. 2013-0003: Implementing guidelines in the analysis, '
        'monitoring and maintenance of water used in dialysis facilities</em>. Republic of the Philippines. '
        '<a href="https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/69036">https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/69036</a>'
    ),
    "psn2024": (
        'Philippine Society of Nephrology (PSN) Committee on Hemodialysis. (2024). <em>Guidelines for nephrologist in the operation '
        'of hemodialysis clinics in the Philippines</em> (3rd ed.). Philippine Society of Nephrology. '
        '<a href="https://psn.org.ph/wp-content/uploads/2024/03/HD-Guidelines-for-Nephrologists-Final-Revision-3.14.24.pdf">https://psn.org.ph/wp-content/uploads/2024/03/HD-Guidelines-for-Nephrologists-Final-Revision-3.14.24.pdf</a>'
    ),
    "ra9173": (
        'Republic of the Philippines (RP). (2002). <em>Republic Act No. 9173: Philippine Nursing Act of 2002</em>. '
        '<a href="https://ldr.senate.gov.ph/sites/default/files/2025-03/RA9173.pdf">https://ldr.senate.gov.ph/sites/default/files/2025-03/RA9173.pdf</a>'
    ),
    "ra10173": (
        'National Privacy Commission (NPC). (2012). <em>Republic Act No. 10173: Data Privacy Act of 2012</em>. '
        '<a href="https://privacy.gov.ph/data-privacy-act/">https://privacy.gov.ph/data-privacy-act/</a>'
    ),
    "iso23500_5": (
        'International Organization for Standardization (ISO). (2024). <em>Preparation and quality management of fluids for '
        'haemodialysis and related therapies — Part 5: Quality of dialysis fluid for haemodialysis and related therapies</em> (ISO 23500-5:2024). '
        '<a href="https://www.iso.org/standard/84372.html">https://www.iso.org/standard/84372.html</a>'
    ),
    "iso23500_3": (
        'International Organization for Standardization (ISO). (2024). <em>Preparation and quality management of fluids for '
        'haemodialysis and related therapies — Part 3: Water for haemodialysis and related therapies</em> (ISO 23500-3:2024). '
        '<a href="https://www.iso.org/standard/84370.html">https://www.iso.org/standard/84370.html</a>'
    ),
    "anna7": (
        'Counts, C. S. (Ed.). (2020). <em>Core curriculum for nephrology nursing</em> (7th ed.). American Nephrology Nurses Association. '
        '<a href="https://old.annanurse.org/core-curriculum-nephrology-nursing">https://old.annanurse.org/core-curriculum-nephrology-nursing</a>'
    ),
    "aki2012": (
        'Kidney Disease: Improving Global Outcomes (KDIGO) Acute Kidney Injury Work Group. (2012). KDIGO clinical practice guideline '
        'for acute kidney injury. <em>Kidney International Supplements</em>, <em>2</em>(1), 1–138. '
        '<a href="https://doi.org/10.1038/kisup.2012.1">https://doi.org/10.1038/kisup.2012.1</a>'
    ),
    "mbd2017": (
        'Kidney Disease: Improving Global Outcomes (KDIGO) CKD-MBD Update Work Group. (2017). KDIGO 2017 clinical practice guideline '
        'update for the diagnosis, evaluation, prevention, and treatment of chronic kidney disease–mineral and bone disorder (CKD-MBD). '
        '<em>Kidney International Supplements</em>, <em>7</em>(1), 1–59. '
        '<a href="https://doi.org/10.1016/j.kisu.2017.04.001">https://doi.org/10.1016/j.kisu.2017.04.001</a>'
    ),
    "anemia2026": (
        'Kidney Disease: Improving Global Outcomes (KDIGO) Anemia Work Group. (2026). KDIGO 2026 clinical practice guideline for the '
        'management of anemia in chronic kidney disease (CKD). <em>Kidney International</em>, <em>109</em>(1S), S1–S99. '
        '<a href="https://doi.org/10.1016/j.kint.2025.06.006">https://doi.org/10.1016/j.kint.2025.06.006</a>'
    ),
    "cdc2001": (
        'Centers for Disease Control and Prevention (CDC). (2001). Recommendations for preventing transmission of infections among '
        'chronic hemodialysis patients. <em>MMWR Recommendations and Reports</em>, <em>50</em>(RR-5), 1–43. '
        '<a href="https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5005a1.htm">https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5005a1.htm</a>'
    ),
}

# ── PubMed-verified references: key -> PMID (metadata in refs_pubmed_raw.json) ─
PUBMED_REFS = {
    "mytemp2022": "36343653", "caruaru1998": "9516222",
    "ckd2024": "38490803", "nutr2020": "32829751", "hd2015": "26498416", "va2019": "32778223",
    "ispd2022": "35264029", "ispd2023": "37232412", "txcand2020": "32301874", "txrecip2009": "19845597",
    "ckm2015": "25923985", "flythe2011": "20927040", "flythe2020": "32278617", "clase2020": "31706619",
    "inker2021": "34554658", "ostermann2020": "32709292", "bp2021": "33637192", "figueiredo2016": "26917664",
    "hcv2022": "36410841", "kanbay2020": "33391741", "chan2019": "30987837", "brown2020": "32063219",
    "patel2013": "23676763", "mannon2018": "30007955", "shroff2019": "30859187", "wiles2019": "31672135",
    "talevski2020": "32287296", "muller2018": "30139905", "daugirdas1993": "8305648", "sever2023": "37479903",
    "vnd2008": "19090893", "aha2025als": "41122884", "aha2025special": "41122889",
    "dapa2020": "32970396", "empa2023": "36331190", "tangri2011": "21482743",
    "starrt2020": "32668114", "ideal2010": "20581422",
}

# Full journal names (APA wants the full title, not the PubMed abbreviation)
JOURNALS = {
    'Journal of clinical apheresis': 'Journal of Clinical Apheresis',
    'Psychological bulletin': 'Psychological Bulletin',
    'Family medicine': 'Family Medicine',
    'Archives of internal medicine': 'Archives of Internal Medicine',
    'The Behavioral and brain sciences': 'Behavioral and Brain Sciences',
    'Nature reviews. Neuroscience': 'Nature Reviews Neuroscience',
    'Emotion (Washington, D.C.)': 'Emotion',
    'Nephrology (Carlton, Vic.)': 'Nephrology',
    'Journal of the Royal Society of Medicine': 'Journal of the Royal Society of Medicine',
    'Advances in chronic kidney disease': 'Advances in Chronic Kidney Disease',
    'Journal of pain and symptom management': 'Journal of Pain and Symptom Management',
    'ACP journal club': 'ACP Journal Club',
    'Psychological science': 'Psychological Science',
    'The British journal of general practice : the journal of the Royal College of General Practitioners': 'British Journal of General Practice',
    'BMJ (Clinical research ed.)': 'BMJ',
    'Palliative medicine': 'Palliative Medicine',
    'Contemporary clinical trials': 'Contemporary Clinical Trials',
    'BMC public health': 'BMC Public Health',
    'Quality of life research : an international journal of quality of life aspects of treatment, care and rehabilitation': 'Quality of Life Research',
    'Clinical journal of the American Society of Nephrology : CJASN': 'Clinical Journal of the American Society of Nephrology',
    'Annals of internal medicine': 'Annals of Internal Medicine',
    'Neurology': 'Neurology',
    'The Cochrane database of systematic reviews': 'Cochrane Database of Systematic Reviews',
    'NEJM evidence': 'NEJM Evidence',
    'Renal failure': 'Renal Failure',
    "Lancet (London, England)": "The Lancet",
    "Kidney international": "Kidney International",
    "American journal of kidney diseases : the official journal of the National Kidney Foundation": "American Journal of Kidney Diseases",
    "Peritoneal dialysis international : journal of the International Society for Peritoneal Dialysis": "Peritoneal Dialysis International",
    "Transplantation": "Transplantation",
    "The New England journal of medicine": "The New England Journal of Medicine",
    "Clinical kidney journal": "Clinical Kidney Journal",
    "Nephron": "Nephron",
    "Nephrology, dialysis, transplantation : official publication of the European Dialysis and Transplant Association - European Renal Association": "Nephrology Dialysis Transplantation",
    "BMC nephrology": "BMC Nephrology",
    "PloS one": "PLOS ONE",
    "BMJ open": "BMJ Open",
    "Journal of the American Society of Nephrology : JASN": "Journal of the American Society of Nephrology",
    "Nature reviews. Nephrology": "Nature Reviews Nephrology",
    "Journal of renal care": "Journal of Renal Care",
    "Circulation": "Circulation",
    "JAMA": "JAMA",
    "American journal of transplantation : official journal of the American Society of Transplantation and the American Society of Transplant Surgeons": "American Journal of Transplantation",
}

# Sentence-case titles for sources PubMed stores in title case (APA 7)
TITLE_OVERRIDES = {
    "7802519": "Dialysis discontinuation: A \u201cgood\u201d death?",
    "25863828": 'Long-term effects of frequent nocturnal hemodialysis on mortality: The Frequent Hemodialysis Network (FHN) Nocturnal Trial',
    "27125246": 'Patient education and peritoneal dialysis modality selection: A systematic review and meta-analysis',
    "28487346": 'A systematic review of the prevalence and associations of limited health literacy in CKD',
    "28923831": 'International comparisons of prevalence, awareness, and treatment of pruritus in people on hemodialysis',
    "29729346": 'Validation of the IPOS-Renal symptom survey in advanced kidney disease: A cross-sectional study',
    "30833302": 'Clinical pharmacology considerations in pain management in patients with advanced kidney failure',
    "34556256": 'KDIGO 2021 clinical practice guideline for the management of glomerular diseases',
    "36272764": 'KDIGO 2022 clinical practice guideline for diabetes management in chronic kidney disease',
    "37017433": 'Guidelines on the use of therapeutic apheresis in clinical practice: Evidence-based approach from the Writing Committee of the American Society for Apheresis: The ninth special issue',
    "38182286": 'KDIGO 2024 clinical practice guideline for the management of lupus nephritis',
    "38388102": 'KDIGO 2024 clinical practice guideline for the management of antineutrophil cytoplasmic antibody (ANCA)-associated vasculitis',
    "40975525": 'Executive summary of the KDIGO 2025 clinical practice guideline for the management of immunoglobulin A nephropathy (IgAN) and immunoglobulin A vasculitis (IgAV)',
    "27909047": 'Exercise in patients on dialysis: A multicenter, randomized clinical trial',
    "28126706": 'Sertraline versus placebo in patients with major depressive disorder undergoing hemodialysis: A randomized, controlled feasibility trial',
    "28238554": 'Developing a set of core outcomes for trials in hemodialysis: An international Delphi survey',
    "29101402": 'Effect of sertraline on depressive symptoms in patients with chronic kidney disease without dialysis dependence: The CAST randomized clinical trial',
    "29551585": 'Establishing a core outcome measure for fatigue in patients on hemodialysis: A Standardized Outcomes in Nephrology-Hemodialysis (SONG-HD) consensus workshop report',
    "30146421": 'Missed hemodialysis treatments: International variation, predictors, and outcomes in the Dialysis Outcomes and Practice Patterns Study (DOPPS)',
    "30802897": 'Comparative efficacy of therapies for treatment of depression for patients undergoing maintenance hemodialysis: A randomized clinical trial',
    "31585683": 'Practical guide to vaccination in all stages of CKD, including patients treated by dialysis or kidney transplantation',
    "38320198": 'Exercise during hemodialysis in patients with chronic kidney failure',
    "33095849": "Effect of regional citrate anticoagulation vs systemic heparin anticoagulation during continuous kidney replacement therapy on dialysis filter life span and mortality among critically ill patients with acute kidney injury: A randomized clinical trial",
    "38490803": "KDIGO 2024 clinical practice guideline for the evaluation and management of chronic kidney disease",
    "32829751": "KDOQI clinical practice guideline for nutrition in CKD: 2020 update",
    "26498416": "KDOQI clinical practice guideline for hemodialysis adequacy: 2015 update",
    "32778223": "KDOQI clinical practice guideline for vascular access: 2019 update",
    "37232412": "ISPD catheter-related infection recommendations: 2023 update",
    "32301874": "KDIGO clinical practice guideline on the evaluation and management of candidates for kidney transplantation",
    "19845597": "KDIGO clinical practice guideline for the care of kidney transplant recipients",
    "33637192": "KDIGO 2021 clinical practice guideline for the management of blood pressure in chronic kidney disease",
    "36410841": "KDIGO 2022 clinical practice guideline for the prevention, diagnosis, evaluation, and treatment of hepatitis C in chronic kidney disease",
    "26917664": "A syllabus for teaching peritoneal dialysis to patients and caregivers",
    "30007955": "Delayed graft function: The AKI of kidney transplantation",
    "32287296": "Teach-back: A systematic review of implementation and impacts",
    "32970396": "Dapagliflozin in patients with chronic kidney disease",
    "32668114": "Timing of initiation of renal-replacement therapy in acute kidney injury",
    "20581422": "A randomized, controlled trial of early versus late initiation of dialysis",
    "36331190": "Empagliflozin in patients with chronic kidney disease",
    "41122884": "Part 9: Adult advanced life support: 2025 American Heart Association guidelines for cardiopulmonary resuscitation and emergency cardiovascular care",
    "41122889": "Part 10: Adult and pediatric special circumstances of resuscitation: 2025 American Heart Association guidelines for cardiopulmonary resuscitation and emergency cardiovascular care",
}
# Group authors that PubMed lists by collective name only
GROUP_AUTHORS = {
    "34556256": 'Kidney Disease: Improving Global Outcomes (KDIGO) Glomerular Diseases Work Group',
    "38182286": 'Kidney Disease: Improving Global Outcomes (KDIGO) Lupus Nephritis Work Group',
    "38388102": 'Kidney Disease: Improving Global Outcomes (KDIGO) ANCA Vasculitis Work Group',
    "36272764": 'Kidney Disease: Improving Global Outcomes (KDIGO) Diabetes Work Group',
    "19846848": "RENAL Replacement Therapy Study Investigators",
    "36343653": "MyTEMP Writing Committee",
    "26498416": "National Kidney Foundation (NKF)",
}

SCOPE_NOTE = (
    "This module is self-study for registered nurses. It explains the reasoning behind safe practice; it does not "
    "replace the physician&rsquo;s orders, your unit&rsquo;s approved procedures, or the manufacturer&rsquo;s instructions "
    "for the equipment you use. Every case is fictional. A quiz score records self-assessment only; practice "
    "competencies are observed and signed off by a clinical preceptor or training provider."
)


# ── Competency framework (rendered on each module, the hub progression map, and the educator checklist) ──
# Each module's competencies live in content/mNN_c.py as COMPETENCIES = [{"thread", "statement", "level", "evidence"}]
# and MILESTONE = "one sentence". Levels follow Miller's pyramid; self-study alone never exceeds "knows".
COMPETENCY_LEVELS = {
    "K": ("Knows", "Explains the reasoning and applies it to cases. Verified by the self-assessment and the nursing case."),
    "S": ("Shows how", "Demonstrates the skill in simulation, a skills station, or teach-back. Verified by an educator."),
    "D": ("Does, supervised", "Performs the task with real patients under direct supervision. Verified by preceptor observation."),
    "I": ("Does, independent", "Performs the task without direct supervision after preceptor sign-off under the unit&rsquo;s policy."),
}
COMPETENCY_THREADS = {
    "assessment":    "Clinical assessment and fluid status",
    "results":       "Interpreting results and trends",
    "medicines":     "Medicines and their safety",
    "teaching":      "Patient and family teaching, nutrition, and shared decisions",
    "therapy":       "Delivering kidney replacement therapy",
    "access":        "Vascular and peritoneal access",
    "infection":     "Infection prevention and control",
    "water":         "Water, dialysate, and equipment safety",
    "emergency":     "Recognizing deterioration and emergency response",
    "communication": "Communication, handoff, and documentation",
    "professional":  "Professional, ethical, and legal practice",
    "quality":       "Quality, safety culture, and improvement",
}
COMPETENCY_EVIDENCE = ["Self-assessment", "Nursing case", "Skills station", "Simulation", "Teach-back", "Observed practice", "Record review"]
