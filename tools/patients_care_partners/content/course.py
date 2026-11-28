# -*- coding: utf-8 -*-
"""Renal Patients and Care Partners: course-level copy for generate_patients_care_partners.py.
Built from the v1.0 handoff and Blueprint v2.0 (November 28, 2026). Module text lives in curriculum.json (canonical).
Every case and name is fictional. Status: draft pending Dr. Rivero's clinical sign-off."""

HUB = "patients-care-partners"
REVIEW_DATE = "2026-11-28"
REVIEW_HUMAN = "November 28, 2026"
STORE_KEY = "rcm-course-patients-care-partners-progress"
STATUS = "Draft for clinical review: not yet signed off by the clinical editor"

TITLE = "Renal Patients and Care Partners"
SHORT = "Patients &amp; Care Partners"
GROUP = "Patients &amp; Care Partners"

PATH_ORDER = ["core", "ckd", "hd", "pd", "home-hd", "transplant", "supportive", "partner", "family"]
PATH_LABEL = {
    "core": "Shared foundations", "ckd": "Kidney disease before dialysis", "hd": "In-center hemodialysis",
    "pd": "Peritoneal dialysis at home", "home-hd": "Exploring home hemodialysis", "transplant": "Kidney transplant",
    "supportive": "Conservative kidney care", "partner": "Care partners", "family": "Families and transitions",
}
PATH_BLURB = {
    "core": "Twelve modules everyone takes: your team, your results, choices, medicines, food, fluid, infection, emergencies, wellbeing, costs, disasters and speaking up.",
    "ckd": "Protect the kidneys you have, plan ahead, and understand the heart, kidney and sugar connection.",
    "hd": "Treatment days, protecting your access, using reviews, and why potassium, phosphorus and fluid rules exist.",
    "pd": "Get ready for supervised training, spot infection early, and run a safe home routine.",
    "home-hd": "Orientation only: the hemodialysis modules plus home organization. Device training happens with an authorized program.",
    "transplant": "Evaluation, a safe routine with anti-rejection medicines, and coverage across policy dates.",
    "supportive": "Active care focused on comfort and what matters most, and conversations about future care.",
    "partner": "Support without taking over, organize the practical load, and look after yourself.",
    "family": "Children and teenagers, growing independence, and coming home safely after a hospital stay.",
}
PATH_ICON = {"core": "🧭", "ckd": "🍃", "hd": "💧", "pd": "🌊", "home-hd": "🏠", "transplant": "🌱", "supportive": "☀️", "partner": "🤝", "family": "👪"}
OG_KEY = {"core": "track", "ckd": "ckd", "hd": "hd", "pd": "pd", "home-hd": "homehd", "transplant": "tx", "supportive": "support", "partner": "partner", "family": "family"}

SCOPE_NOTE = ("This course helps you understand your care and prepare questions. It does not give individual fluid limits, food "
              "limits, blood pressure targets, medicine doses or machine settings: those come from your own care team. Practical "
              "home dialysis training happens with your treatment service. No website, quiz or chat is watched in real time; in an "
              "emergency, get help now. Every person in the stories is fictional.")

DISCLAIMER = ("Patient and care-partner education from the Renal Care Academy. It supports, and never replaces, the advice of your "
              "own kidney team, your unit&rsquo;s written instructions, and supervised treatment training. Completing it is a "
              "self-reported learning record, not a qualification of any kind.")

IS_NOT = ("This course is education, not treatment. It does not diagnose, choose a treatment, or set any personal number. "
          "Finishing it gives no job qualification, nursing or technician credential, PSN recognition, PhilHealth accreditation, "
          "DOH licensure or CPD credit, and it never authorizes anyone to perform dialysis or any procedure. Practical home "
          "dialysis training and readiness are decided by your treatment service. Translations are not yet available.")

ABBR = {
    "CKD": ("chronic kidney disease", ""), "eGFR": ("estimated glomerular filtration rate", ""),
    "uACR": ("urine albumin-to-creatinine ratio", ""), "HD": ("hemodialysis", ""), "PD": ("peritoneal dialysis", ""),
    "NSAID": ("non-steroidal anti-inflammatory drug", ""), "CAPD": ("continuous ambulatory peritoneal dialysis", ""),
    "APD": ("automated peritoneal dialysis", ""), "CKM": ("conservative kidney management", ""),
    "AKI": ("acute kidney injury", ""), "ARB": ("angiotensin receptor blocker", ""), "ACE": ("angiotensin-converting enzyme", ""),
    "SGLT2": ("sodium-glucose cotransporter 2", ""), "GLP-1": ("glucagon-like peptide-1", ""),
    "URR": ("urea reduction ratio", ""), "KDIGO": ("Kidney Disease: Improving Global Outcomes", ""),
    "KDOQI": ("Kidney Disease Outcomes Quality Initiative", ""), "DOPPS": ("Dialysis Outcomes and Practice Patterns Study", ""),
    "ISPD": ("International Society for Peritoneal Dialysis", ""), "CDC": ("Centers for Disease Control and Prevention", ""),
    "WHO": ("World Health Organization", ""), "DOH": ("Department of Health", ""), "PSN": ("Philippine Society of Nephrology", ""),
    "NICE": ("National Institute for Health and Care Excellence", ""), "ESKD": ("end-stage kidney disease", ""),
    "CPD": ("continuing professional development", ""), "NIDDK": ("National Institute of Diabetes and Digestive and Kidney Diseases", ""),
}

READINGS = {
    "C01": [("personal-medical-journal-health-history.html", "Keep your own health journal for visits and emergencies.")],
    "C02": [("kidney-functions.html", "What healthy kidneys do, in more depth."), ("how-to-properly-assess-kidney-function.html", "How kidney function is measured.")],
    "C03": [("hemodialysis-modalities.html", "The kinds of hemodialysis."), ("peritoneal-dialysis-ckd.html", "Peritoneal dialysis explained.")],
    "C04": [("medicines-and-your-kidneys.html", "How kidney disease changes medicines."), ("nsaid-kidney-injury.html", "Pain relievers and kidney injury.")],
    "C05": [("sodium-salt-reduction-ckd.html", "Practical salt reduction."), ("plant-forward-renal-diet.html", "Building plant-forward kidney meals.")],
    "C06": [("fluid-management-dialysis.html", "Fluid on dialysis, explained."), ("dry-weight-determination.html", "How target (dry) weight is set.")],
    "C07": [("dialysis-access-care.html", "Everyday access care."), ("dialysis-access-infection.html", "Access infections and warning signs.")],
    "C08": [("hemodialysis-complications.html", "Problems that can happen during hemodialysis."), ("potassium-hyperkalemia-ckd.html", "High potassium and the heart.")],
    "C09": [("exercise-guide-ckd.html", "Starting exercise safely."), ("anemia-management.html", "Anemia, a common cause of tiredness.")],
    "C10": [("philhealth-z-packages.html", "PhilHealth hemodialysis, PD and transplant benefits."), ("zero-balance-billing-philhealth.html", "Zero balance billing, explained.")],
    "C11": [("typhoon-disaster-preparedness-dialysis.html", "Typhoon and disaster preparedness on dialysis."), ("hemodialysis-transfer-guide.html", "Transferring or traveling for dialysis.")],
    "C12": [("personal-medical-journal-health-history.html", "A journal makes every visit more useful.")],
    "K01": [("medicines-and-your-kidneys.html", "Medicines and sick days."), ("filipino-diabetic-diet.html", "Filipino meals for diabetes.")],
    "K02": [("starting-dialysis-new-beginning.html", "Why starting dialysis can be a new beginning."), ("hemodialysis-access-lifeline.html", "Planning an access that lasts.")],
    "K03": [("cholesterol-diet-guide.html", "Heart-healthy eating with kidney disease."), ("how-to-properly-assess-kidney-function.html", "Reading kidney function results.")],
    "H01": [("hemodialysis-complications.html", "Cramps, dizziness and other session problems."), ("dry-weight-determination.html", "Target weight, explained.")],
    "H02": [("hemodialysis-access-lifeline.html", "Making an access last a lifetime."), ("dialysis-access-care.html", "Daily access care.")],
    "H03": [("hemodialysis-modalities.html", "Options for hemodialysis schedules."), ("anemia-management.html", "Anemia and your review.")],
    "H04": [("potassium-hyperkalemia-ckd.html", "Potassium, in depth."), ("phosphorus-ckd.html", "Phosphorus and binders.")],
    "P01": [("peritoneal-dialysis-ckd.html", "Peritoneal dialysis, in depth.")],
    "P02": [("peritoneal-dialysis-ckd.html", "PD complications and prevention."), ("dialysis-access-infection.html", "Exit-site and catheter infections.")],
    "P03": [("peritoneal-dialysis-ckd.html", "Living with PD at home."), ("home-hemodialysis-philippines.html", "Home hemodialysis in the Philippines.")],
    "T01": [("kidney-transplant.html", "Kidney transplant, in depth."), ("transplant-prehabilitation.html", "Getting fit for a transplant.")],
    "T02": [("kidney-transplant.html", "Life after transplant."), ("transplant-allograft-failure.html", "When a transplant starts to fail.")],
    "T03": [("philhealth-z-packages.html", "PhilHealth transplant benefits.")],
    "S01": [("advance-care-planning-dialysis.html", "Advance care planning."), ("hemodialysis-elderly.html", "Dialysis decisions in older adults.")],
    "S02": [("advance-care-planning-dialysis.html", "Talking about future care.")],
    "A01": [("caregiver-guide-ckd.html", "A guide for caregivers.")],
    "A02": [("caregiver-guide-ckd.html", "Organizing care at home."), ("personal-medical-journal-health-history.html", "Keeping records together.")],
    "A03": [("caregiver-guide-ckd.html", "Looking after the caregiver.")],
    "F01": [("caregiver-guide-ckd.html", "Supporting a family member.")],
    "F02": [("medicines-and-your-kidneys.html", "Medicine changes after a hospital stay."), ("personal-medical-journal-health-history.html", "Bringing records to every visit.")],
}

TOOLKIT = "calc-patient-care-partner-toolkit.html"
CALC_ANCHOR = {"CALC-RESULTS-TREND": "tool-1", "CALC-SODIUM-LABEL": "tool-2", "CALC-FLUID-LOG": "tool-3", "CALC-IDWG": "tool-4",
               "CALC-HD-SESSIONS": "tool-5", "CALC-TX-DOSE-CLOCK": "tool-6", "CALC-MED-SCHEDULER": None}
MED_SCHEDULER = "../drugs/med-scheduler.html"

STATIONS = [
    ("Emergency", "Severe breathlessness at home", "Identifies urgent help, states location and kidney treatment, avoids online delay", "Waits for a website or chat reply"),
    ("Medicines", "Hospital list conflicts with the old list", "Spots the difference, names the clinician or pharmacist to ask, avoids choosing a dose", "Chooses a dose without clarification"),
    ("Benefits", "An advertisement promises maximum transplant coverage", "Asks for eligibility and contracting review, the effective date and an itemized estimate", "Treats an advertised maximum as guaranteed cash"),
    ("Access", "The usual fistula vibration disappears", "Contacts the dialysis unit promptly and does not manipulate the access", "Waits until next week or tries to clear it"),
    ("Peritoneal dialysis (PD learners only)", "Cloudy drainage with mild symptoms", "Calls the PD team immediately and follows the taught urgent plan", "Waits for severe pain or adds antibiotics"),
    ("Partnership", "A care partner disagrees with a capable patient", "Asks the patient's preferences and offers respectful support", "Overrides the patient because of course completion"),
    ("Continuity", "A flooded road prevents travel to the unit", "Contacts the unit or backup promptly and uses the written plan", "Quietly skips treatment without telling anyone"),
]
