# -*- coding: utf-8 -*-
"""Dialysis Nurse Assistant / Patient Care Assistant (PCA) track of the Renal Care Academy (Nephrology Nursing, By Role).

A supervised support role in adult maintenance hemodialysis. Course metadata, abbreviations, references and shared copy.
Module content lives in mNN.py. Rendered by generate_dialysis_nurse_assistant.py; never hand-edit the pages.
Built from Blueprint v2 (/Volumes/Storage/Renal Care Academy/Dialysis Nurse Assistant/BLUEPRINT-v2.md), which improves
the owner's v1.0 handoff package in the same folder.
"""

COURSE = {
    "title": "Dialysis Nurse Assistant / Patient Care Assistant (PCA)",
    "long_title": "Dialysis Nurse Assistant / Patient Care Assistant (PCA)",
    "hub_slug": "dialysis-nurse-assistant",
    "parent_slug": "nephrology-nursing",
    "entry_slug": "nephrology-nursing-09-hd-session-complication-response",
    "label": "Supervised support role &middot; not a registered-nurse specialty and not a technician equivalency",
    "review_date": "2026-11-25",
    "pass_correct": 20,
    "exam_items": 24,
    "module_draw": 5,
    "module_pass": 4,
    "store_key": "rcm-dna-progress-v1",
    "status": "Draft for clinical, nursing, infection prevention and regulatory review",
}

SCOPE_NOTE = (
    "This subtrack prepares <strong>supervised support workers</strong> in adult maintenance hemodialysis: the Dialysis Nurse "
    "Assistant, also called the Patient Care Assistant (PCA). You work on the delegation of a registered nurse (RN). The course "
    "does not authorize assessment or treatment decisions, needle or catheter work, connection or disconnection, medicines, "
    "machine settings, alarm resetting, dialyzer reprocessing or water-system work. Your employer&rsquo;s written job description, "
    "your signed-off competencies and the RN on duty decide what you may do. All people and cases are fictional."
)

# id, slug suffix, title, short title, week, hours (study, simulation, supervised workplace), competencies, practice note
MODULES = [
    ("01", "role-scope-teamwork", "Your Role, Delegation and Safe Teamwork", "Role and delegation", 1, (4, 2, 4), ["P1"], "Observation only in the workplace"),
    ("02", "kidney-care-foundations", "Kidney Failure and the Patient Journey", "Kidney care foundations", 1, (4, 2, 4), ["P2"], "Observation only in the workplace"),
    ("03", "dignity-communication", "Dignity, Consent, Privacy and Communication", "Dignity and communication", 2, (4, 2, 4), ["P3"], "Observation only in the workplace"),
    ("04", "infection-prevention", "Infection Prevention and Exposure Safety", "Infection prevention", 2, (4, 2, 4), ["P4"], "Observation only in the workplace"),
    ("05", "arrival-observations-weights", "Arrival, Observations and Weights", "Observations and weights", 3, (4, 2, 4), ["P5"], "Supervised practice after sign-off"),
    ("06", "station-supplies-preparation", "Station Readiness, Supplies and Preparation Assistance", "Station and supplies", 3, (4, 2, 4), ["P6"], "Supervised practice after sign-off"),
    ("07", "access-protection-monitoring", "Protect the Access and Observe During Treatment", "Access and observation", 4, (4, 2, 4), ["P7"], "Supervised practice after sign-off"),
    ("08", "deterioration-emergencies", "Deterioration, Emergencies and BLS Teamwork", "Emergencies", 4, (4, 2, 4), ["P8"], "Simulation; BLS course is additional"),
    ("09", "comfort-mobility-discharge", "Comfort, Safe Mobility and Departure", "Comfort and departure", 5, (4, 2, 4), ["P9"], "Supervised practice after sign-off"),
    ("10", "cleaning-waste-environment", "Cleaning, Waste and Equipment Boundaries", "Cleaning and waste", 5, (4, 2, 4), ["P10"], "Supervised practice after sign-off"),
    ("11", "records-specimens-benefits", "Accurate Records, Specimens, Supplies and Benefits", "Records and specimens", 6, (4, 2, 4), ["P11"], "Supervised practice after sign-off"),
    ("12", "capstone-quality-disasters", "Quality, Disasters and the Integrated Capstone", "Quality and capstone", 6, (4, 2, 4),
     ["P1", "P2", "P3", "P4", "P5", "P6", "P7", "P8", "P9", "P10", "P11", "P12"], "Capstone and workplace portfolio"),
]

COMPETENCIES = [
    ("P1", "Work inside the role: name the supervising RN, accept only delegated tasks within sign-off, decline safely and close the loop.", "Repeat-back, safe refusal and handback in every station"),
    ("P2", "Explain dialysis in plain words and route treatment, diet, medicine and money questions to the right person.", "Plain-language explanation; missed-treatment relay"),
    ("P3", "Protect dignity and privacy, respect refusal, use interpreters and teach-back, and escalate safeguarding concerns.", "Confidentiality and refusal scenario"),
    ("P4", "Perform hand hygiene and glove changes at the right moments, keep clean and dirty apart, and start the exposure response at once.", "Hand hygiene and exposure station"),
    ("P5", "Identify with two identifiers, obtain trustworthy weights and assigned observations, and report the reading and the symptom.", "Weight, tare and observation station"),
    ("P6", "Prepare a station from the approved list, spot mismatched, damaged or expired supplies, and respect quarantine.", "Station readiness with a planted mismatch"),
    ("P7", "Keep the access visible and protected, notice bleeding and symptom change, and report without touching the circuit.", "Access concern simulation"),
    ("P8", "Recognize deterioration, activate the emergency response, and perform the role learned in a practical BLS course.", "Emergency activation drill; BLS card"),
    ("P9", "Give comfort and mobility help within the RN&rsquo;s plan, prevent falls, and never let an unwell patient leave unreviewed.", "Transfer and departure station"),
    ("P10", "Clean external surfaces with full wet contact time after clinical clearance, segregate waste, and report faults.", "Cleaning cycle and fault report"),
    ("P11", "Keep truthful records, carry sealed specimens with identity checks, and route benefits questions without promises.", "Factual entry and mismatch response"),
    ("P12", "Integrate the role across a shift, report near misses, and act within the plan during disasters and outages.", "Capstone; workplace portfolio"),
]

ABBR = {
    "PCA": ("Patient Care Assistant", "the title used for the Dialysis Nurse Assistant in this course; never &ldquo;Patient Care Technician&rdquo;"),
    "PCT": ("Patient Care Technician", "a United States dialysis role with its own certification; not the Philippine assistant role"),
    "RN": ("registered nurse", ""),
    "HD": ("hemodialysis", ""),
    "PD": ("peritoneal dialysis", ""),
    "CKD": ("chronic kidney disease", ""),
    "AV": ("arteriovenous", ""),
    "AVF": ("arteriovenous fistula", "an artery joined to a vein in the arm, used for dialysis needles"),
    "AVG": ("arteriovenous graft", "a tube joining an artery to a vein, used for dialysis needles"),
    "BLS": ("basic life support", ""),
    "ACLS": ("advanced cardiovascular life support", ""),
    "AED": ("automated external defibrillator", ""),
    "CPR": ("cardiopulmonary resuscitation", ""),
    "BP": ("blood pressure", ""),
    "PPE": ("personal protective equipment", ""),
    "IPC": ("infection prevention and control", ""),
    "SOP": ("standard operating procedure", ""),
    "IFU": ("instructions for use", "the manufacturer&rsquo;s instructions for a device or product"),
    "DOH": ("Department of Health", "Philippines"),
    "PSN": ("Philippine Society of Nephrology", ""),
    "PRC": ("Professional Regulation Commission", "Philippines"),
    "PhilHealth": ("Philippine Health Insurance Corporation", ""),
    "HFSRB": ("Health Facilities and Services Regulatory Bureau", "DOH licensing bureau"),
    "CDC": ("Centers for Disease Control and Prevention", "United States"),
    "WHO": ("World Health Organization", ""),
    "AHA": ("American Heart Association", ""),
    "KDOQI": ("Kidney Disease Outcomes Quality Initiative", ""),
    "DOPPS": ("Dialysis Outcomes and Practice Patterns Study", ""),
    "NIOSH": ("National Institute for Occupational Safety and Health", "United States"),
    "CMS": ("Centers for Medicare &amp; Medicaid Services", "United States"),
    "CFR": ("Code of Federal Regulations", "United States"),
    "NHS": ("National Health Service", "United Kingdom"),
    "TESDA": ("Technical Education and Skills Development Authority", "Philippines"),
    "CPD": ("continuing professional development", ""),
    "UF": ("ultrafiltration", "removal of water from the blood during dialysis"),
    "IDWG": ("interdialytic weight gain", "weight gained between the end of one session and the start of the next"),
    "SpO2": ("oxygen saturation by pulse oximetry", ""),
    "HBV": ("hepatitis B virus", ""),
    "HCV": ("hepatitis C virus", ""),
    "HIV": ("human immunodeficiency virus", ""),
    "PEP": ("post-exposure prophylaxis", "medicines given soon after an exposure to prevent infection"),
    "RO": ("reverse osmosis", "the main purification step of dialysis water"),
    "RA": ("Republic Act", ""),
    "AO": ("Administrative Order", ""),
    "OSH": ("occupational safety and health", ""),
    "SBAR": ("Situation, Background, Assessment, Recommendation", "a structured way to report"),
    "QI": ("quality improvement", ""),
    "PTSD": ("post-traumatic stress disorder", ""),
    "OR": ("odds ratio", ""),
    "HR": ("hazard ratio", ""),
    "RR": ("relative risk", ""),
    "CI": ("confidence interval", ""),
    "OSCE": ("objective structured clinical examination", ""),
    "ICU": ("intensive care unit", ""),
    "EMS": ("emergency medical services", ""),
    "PESO": ("Public Employment Service Office", "Philippines"),
    "HCA": ("healthcare assistant", ""),
}

# PubMed-verified references: key -> PMID (metadata in data/dialysis-nurse-assistant/refs_pubmed_raw.json,
# data/nursing-course/refs_pubmed_raw.json or data/dialysis-unit-support-staff/refs_pubmed_raw.json)
PUBMED_REFS = {
    "aiken2017": "28626086", "saran2003": "12787417", "alsalmi2018": "30146421", "foley2011": "21992122",
    "kalantar2009": "19171851", "kallioinen2017": "27977471", "sjoding2020": "33326721", "freeman2011": "21431947",
    "pittet2000": "11073019", "fuller2011": "22080658", "bond1981": "6111645", "rao2013": "23785746",
    "thompson2009": "19124818", "girou2008": "18662134", "patel2013": "23676763", "bouya2020": "32346521",
    "schillie2013": "24352112", "vanwaeleghem2008": "19090893", "lok2020": "32778223", "karliner2007": "17362215",
    "jagodage2024": "37010245", "talevski2020": "32287296", "pun2019": "30733235", "aha2025bls": "41122888",
    "aha2025special": "41122889", "cook2006": "17699348", "waters2007": "17667392", "rutala2019": "31146858",
    "carling2006": "16392086", "kaufman2019": "30549289", "sever2023": "37479903", "hyre2007": "17900458",
}

JOURNALS = {
    "BMJ Qual Saf": "BMJ Quality &amp; Safety",
    "Kidney international": "Kidney International",
    "American journal of kidney diseases : the official journal of the National Kidney Foundation": "American Journal of Kidney Diseases",
    "Am J Kidney Dis": "American Journal of Kidney Diseases",
    "N Engl J Med": "The New England Journal of Medicine",
    "Circulation": "Circulation",
    "J Hypertens": "Journal of Hypertension",
    "Clin Auton Res": "Clinical Autonomic Research",
    "Lancet": "The Lancet",
    "Infect Control Hosp Epidemiol": "Infection Control and Hospital Epidemiology",
    "Nephrol Nurs J": "Nephrology Nursing Journal",
    "Ann Intern Med": "Annals of Internal Medicine",
    "Clin Infect Dis": "Clinical Infectious Diseases",
    "Ann Glob Health": "Annals of Global Health",
    "MMWR Recomm Rep": "MMWR Recommendations and Reports",
    "Journal of renal care": "Journal of Renal Care",
    "J Ren Care": "Journal of Renal Care",
    "Health Serv Res": "Health Services Research",
    "PloS one": "PLOS ONE",
    "J Am Soc Nephrol": "Journal of the American Society of Nephrology",
    "Clin J Am Soc Nephrol": "Clinical Journal of the American Society of Nephrology",
    "Am J Nurs": "American Journal of Nursing",
    "Am J Infect Control": "American Journal of Infection Control",
    "Transfusion": "Transfusion",
    "Nature reviews. Nephrology": "Nature Reviews Nephrology",
}

TITLE_OVERRIDES = {
    "28626086": "Nursing skill mix in European hospitals: Cross-sectional study of the association with mortality, patient ratings, and quality of care",
    "12787417": "Nonadherence in hemodialysis: Associations with mortality, hospitalization, and practice patterns in the DOPPS",
    "30146421": "Missed hemodialysis treatments: International variation, predictors, and outcomes in the Dialysis Outcomes and Practice Patterns Study (DOPPS)",
    "33326721": "Racial bias in pulse oximetry measurement",
    "27977471": "Sources of inaccuracy in the measurement of adult patients&rsquo; resting blood pressure in clinical settings: A systematic review",
    "21431947": "Consensus statement on the definition of orthostatic hypotension, neurally mediated syncope and the postural tachycardia syndrome",
    "11073019": "Effectiveness of a hospital-wide programme to improve compliance with hand hygiene",
    "22080658": "&ldquo;The dirty hand in the latex glove&rdquo;: A study of hand hygiene compliance when gloves are worn",
    "23785746": "Outbreak of hepatitis C virus infections at an outpatient hemodialysis facility: The importance of infection control competencies",
    "19124818": "Nonhospital health care-associated hepatitis B and C virus transmission: United States, 1998-2008",
    "23676763": "Bloodstream infection rates in outpatient hemodialysis facilities participating in a collaborative prevention effort: A quality improvement report",
    "32346521": "Global prevalence and device related causes of needle stick injuries among health care workers: A systematic review and meta-analysis",
    "24352112": "CDC guidance for evaluating health-care personnel for hepatitis B virus protection and for administering postexposure management",
    "19090893": "Venous needle dislodgement: How to minimise the risks",
    "32778223": "KDOQI clinical practice guideline for vascular access: 2019 update",
    "17362215": "Do professional interpreters improve clinical care for patients with limited English proficiency? A systematic review of the literature",
    "37010245": "Effectiveness of teach-back for chronic kidney disease patient education: A systematic review",
    "32287296": "Teach-back: A systematic review of implementation and impacts",
    "30733235": "Outcomes for hemodialysis patients given cardiopulmonary resuscitation for cardiac arrest at outpatient dialysis clinics",
    "41122888": "Part 7: Adult basic life support: 2025 American Heart Association guidelines for cardiopulmonary resuscitation and emergency cardiovascular care",
    "41122889": "Part 10: Adult and pediatric special circumstances of resuscitation: 2025 American Heart Association guidelines for cardiopulmonary resuscitation and emergency cardiovascular care",
    "17699348": "Falls and fall-related injuries in older dialysis patients",
    "31146858": "Best practices for disinfection of noncritical environmental surfaces and equipment in health care facilities: A bundle approach",
    "16392086": "Improved cleaning of patient rooms using a new targeting method",
    "30549289": "Electronic patient identification for sample labeling reduces wrong blood in tube errors",
    "37479903": "Disasters and kidney care: Pitfalls and solutions",
    "17900458": "Prevalence and predictors of posttraumatic stress disorder among hemodialysis patients following Hurricane Katrina",
    "18662134": "Determinant roles of environmental contamination and noncompliance with standard precautions in the risk of hepatitis C virus transmission in a hemodialysis unit",
    "19171851": "Fluid retention is associated with cardiovascular mortality in patients undergoing long-term hemodialysis",
    "21992122": "Long interdialytic interval and mortality among patients receiving hemodialysis",
}

RETRIEVED = "November 25, 2026"


def _link(url):
    return f'<a href="{url}">{url}</a>'


MANUAL_REFS = {
    "doh2012": ("Department of Health (DOH). (2012). <em>Administrative Order No. 2012-0001: New rules and regulations governing the "
                "licensure and regulation of dialysis facilities in the Philippines</em>. " + _link("https://hfsrb.doh.gov.ph/wp-content/uploads/2021/05/AO-2012-0001.pdf")),
    "psn2024": ("Philippine Society of Nephrology (PSN). (2024). <em>Guidelines for nephrologists in the operation of hemodialysis "
                "clinics in the Philippines</em> (3rd ed.). " + _link("https://psn.org.ph/wp-content/uploads/2024/03/HD-Guidelines-for-Nephrologists-Final-Revision-3.14.24.pdf")),
    "phic2024_23": ("Philippine Health Insurance Corporation (PHIC). (2024). <em>PhilHealth Circular No. 2024-0023: Institutionalization of "
                    "156 hemodialysis sessions and coverage expansion (Revision 2)</em>. " + _link("https://www.philhealth.gov.ph/circulars/2024/PC2024-0023.pdf")),
    "phic2024_29": ("Philippine Health Insurance Corporation (PHIC). (2024). <em>PhilHealth Circular No. 2024-0029: Quality standards on "
                    "maintenance hemodialysis procedure as reference of the Corporation</em>. " + _link("https://www.philhealth.gov.ph/circulars/2024/PC2024-0029.pdf")),
    "doh2013_03": ("Department of Health (DOH). (2013). <em>Administrative Order No. 2013-0003: Implementing guidelines on the analysis, "
                   "monitoring and maintenance of water for dialysis</em>. " + _link("https://hfsrb.doh.gov.ph/wp-content/uploads/2021/05/02052013-2013-0003.pdf")),
    "cfr494": ("Office of the Federal Register (OFR). (2025). <em>42 CFR &sect; 494.140: Personnel qualifications</em> (Code of Federal Regulations, "
               "annual edition). " + _link("https://www.govinfo.gov/content/pkg/CFR-2025-title42-vol5/xhtml/CFR-2025-title42-vol5-part494-subpartD.html")),
    "cdc_core": ("Centers for Disease Control and Prevention (CDC). (2026). <em>Core interventions for dialysis bloodstream infection "
                 f"prevention</em>. Retrieved {RETRIEVED}, from " + _link("https://www.cdc.gov/dialysis-safety/hcp/clinical-safety/")),
    "cdc_station": ("Centers for Disease Control and Prevention (CDC). (2026). <em>Routine disinfection of the dialysis station: Checklist</em>. "
                    f"Retrieved {RETRIEVED}, from " + _link("https://www.cdc.gov/dialysis-safety/media/pdfs/env-checklist-508.pdf")),
    "cdc2001": ("Centers for Disease Control and Prevention (CDC). (2001). Recommendations for preventing transmission of "
                "infections among chronic hemodialysis patients. <em>MMWR Recommendations and Reports</em>, <em>50</em>(RR-5), 1&ndash;43. "
                + _link("https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5005a1.htm")),
    "who2009": ("World Health Organization (WHO). (2009). <em>WHO guidelines on hand hygiene in health care</em>. "
                + _link("https://www.who.int/publications/i/item/9789241597906")),
    "ra10173": ("National Privacy Commission (NPC). (2012). <em>Republic Act No. 10173: Data Privacy Act of 2012</em>. "
                + _link("https://privacy.gov.ph/data-privacy-act/")),
    "ra11058": ("Republic of the Philippines (RP). (2018). <em>Republic Act No. 11058: An act strengthening compliance with occupational "
                "safety and health standards</em>. " + _link("https://lawphil.net/statutes/repacts/ra2018/ra_11058_2018.html")),
    "doh_hcwm": ("Department of Health (DOH), Health Facility Development Bureau. (2020). <em>Health care waste management manual</em> "
                 "(4th ed.). " + _link("https://www.washinhcf.org/wp-content/uploads/2021/07/DOH-Health-Care-Waste-Management-Manual_4th-Edition_FINAL.pdf")),
}

HUB_REFS = ["doh2012", "psn2024", "phic2024_23", "phic2024_29", "doh2013_03", "cfr494", "cdc_core", "aiken2017",
            "saran2003", "foley2011", "kalantar2009", "pun2019", "cook2006", "aha2025bls"]

# Course home: a fictional day in the unit (scenes drawn from the modules)
DAY_HTML = """
<p>Here is what the job looks like before you start the modules. The day is fictional, and so is everyone in it. Every moment in it happens in Philippine dialysis units every week. You will meet the same team in every module: <strong>Nurse Jessa Manalo</strong>, the RN in charge of Bay A; <strong>Kuya Paolo Reyes</strong>, a Dialysis Nurse Assistant with three years in the unit; and <strong>Bea Santos</strong>, a new assistant and a BS Nursing graduate waiting for her board results. The unit is the San Isidro Dialysis Center, eighteen stations, three shifts a day.</p>
<div class="tc-sits">
<div class="tc-sit"><h3>6:05 a.m. &middot; arrival</h3><dl>
<dt>What happens</dt><dd>Mang Rolando, 68, is wheeled in by his son. The wheelchair scale reads 78.6 kg. No one knows this wheelchair&rsquo;s weight.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Do not guess the tare. Weigh the empty chair, or move him to the standing scale if the RN&rsquo;s plan allows. Record both numbers and the units. Module 5.</dd></dl></div>
<div class="tc-sit"><h3>6:20 a.m. &middot; intake</h3><dl>
<dt>What happens</dt><dd>His net weight is 63.4 kg. His last weight after dialysis was 58.0 kg. He is breathing fast and cannot finish a sentence.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Call the RN now, before you finish the form. Report the breathlessness first and the weight second. Module 5 and the toolkit.</dd></dl></div>
<div class="tc-sit"><h3>8:40 a.m. &middot; hour two</h3><dl>
<dt>What happens</dt><dd>Nanay Lorna has pulled her blanket over her fistula arm because she is cold. She is drowsy.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Offer a second blanket for her body and keep the access arm uncovered and in view. Tell the RN she is drowsy. Module 7.</dd></dl></div>
<div class="tc-sit"><h3>10:10 a.m. &middot; shift change</h3><dl>
<dt>What happens</dt><dd>A colleague asks you to &ldquo;just silence&rdquo; a beeping machine at Station 4 while the RN is busy.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Do not touch it. Look at the patient, read the message on the screen, and tell the RN or the backup now. Modules 1 and 7.</dd></dl></div>
<div class="tc-sit"><h3>11:00 a.m. &middot; departure</h3><dl>
<dt>What happens</dt><dd>Mang Rolando stands up quickly to catch his tricycle and grabs the armrest. He says the room is spinning.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Help him sit back down. Stay with him. Call the RN. The tricycle waits; he does not leave until the RN has seen him. Module 9 and the toolkit.</dd></dl></div>
<div class="tc-sit"><h3>4:30 p.m. &middot; the chart</h3><dl>
<dt>What happens</dt><dd>A post-dialysis blood pressure is missing from a chart. Someone says, &ldquo;Just write 130 over 80 so the claim goes through.&rdquo;</dd>
<dt class="tc-sit-do">What you do</dt><dd>Refuse, kindly and clearly. Tell the RN. A missing value is corrected through the approved process, never invented. Module 11.</dd></dl></div>
</div>
<p>None of these moments asks you to make a treatment decision. Every one asks you to notice, to measure honestly, to keep the patient safe for the next minute, and to tell the RN in time. That is the job this subtrack trains.</p>
"""

ROLE_TABLE = """
<div class="table-wrap"><table>
<caption>The role in one table. Columns 1 and 2 apply only after sign-off and on the RN&rsquo;s delegation.</caption>
<thead><tr><th scope="col">Observe and do</th><th scope="col">Report at once</th><th scope="col">Never, under this course</th></tr></thead>
<tbody>
<tr><td>Greet, identify with two identifiers, explain the task</td><td>Chest pain, breathlessness, fainting, collapse, seizure, new confusion</td><td>Assess, triage or decide treatment</td></tr>
<tr><td>Weigh with the tare recorded; take assigned blood pressure, pulse, temperature, respirations and oxygen saturation</td><td>Bleeding, a wet blanket near the access, a needle or line that looks out of place</td><td>Set dry weight, fluid removal or treatment time</td></tr>
<tr><td>Prepare unopened supplies against the list; restock</td><td>Fever or shivering, especially in a patient with a catheter</td><td>Cannulate, touch catheter hubs or connections, connect, disconnect, return blood</td></tr>
<tr><td>Help with comfort, toileting, positioning and transfers within the RN&rsquo;s plan</td><td>A reading far from the patient&rsquo;s usual, or one you could not take reliably</td><td>Give, prepare or hand over any medicine; give blood products</td></tr>
<tr><td>Clean external surfaces after clinical clearance, within the product label</td><td>A machine alarm, a leak, a smell, a damaged cable, an out-of-service tag</td><td>Silence or reset alarms; change settings; prime without a separate sign-off</td></tr>
<tr><td>Carry sealed, labeled specimens and documents</td><td>A specimen or document that does not match</td><td>Draw blood, or relabel from memory</td></tr>
<tr><td>Write what you measured, when, and whom you told</td><td>A missed treatment, a fall, a threat to safety, a request outside your role</td><td>Enter or copy a number you did not obtain</td></tr>
</tbody></table></div>
"""
