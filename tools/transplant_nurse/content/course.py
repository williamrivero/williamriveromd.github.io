# -*- coding: utf-8 -*-
"""Transplant Nurse subtrack of the Renal Care Academy (Nephrology Nursing).

Course metadata, abbreviations, references and shared copy. Module content lives in mNN.py.
Rendered by generate_transplant_nurse.py; never hand-edit the generated academy pages.
"""

COURSE = {
    "title": "Transplant Nurse",
    "long_title": "Kidney Transplant Nursing",
    "hub_slug": "transplant-nurse",
    "parent_slug": "nephrology-nursing",
    "entry_slug": "nephrology-nursing-11-transplantation-special-populations",
    "label": "Specialty subtrack for registered nurses",
    "review_date": "2026-11-24",
    "core_hours": 30,
    "supervised_hours": 40,
    "pass_correct": 10,
    "exam_items": 12,
}

SCOPE_NOTE = (
    "This subtrack prepares Philippine registered nurses for <strong>supervised</strong> kidney transplant ward and "
    "clinic work. It teaches assessment, communication and escalation within nursing scope. Candidacy, listing, organ "
    "allocation, compatibility decisions, dose changes and benefit approval belong to the authorized transplant team, "
    "the histocompatibility laboratory, the Philippine Health Insurance Corporation (PhilHealth) and the facility. All cases are synthetic."
)

# id, slug suffix, title, short title, week, hours, competencies
MODULES = [
    ("01", "role-and-referral", "The Transplant Pathway and the Nursing Role", "Role and referral", 1, 2, ["K1"]),
    ("02", "candidate-and-compatibility", "Recipient Evaluation, Compatibility, and Readiness", "Candidate and compatibility", 1, 2.5, ["K1"]),
    ("03", "living-donor", "Living Donor Evaluation and Advocacy", "Living donor", 2, 2, ["K2"]),
    ("04", "deceased-donor-and-offers", "Deceased Donation, Allocation, and Organ Offers", "Deceased donation and offers", 2, 2, ["K1", "K2"]),
    ("05", "perioperative-and-early-recovery", "Perioperative Care and Early Graft Surveillance", "Perioperative care", 3, 3, ["K3"]),
    ("06", "immunosuppression", "Immunosuppression and Medication Safety", "Immunosuppression", 3, 3, ["K4"]),
    ("07", "graft-dysfunction", "Graft Dysfunction, Rejection, and Biopsy Care", "Graft dysfunction", 4, 2.5, ["K3", "K5"]),
    ("08", "infection", "Infection Prevention and Urgent Triage", "Infection", 4, 2.5, ["K5"]),
    ("09", "longitudinal-care", "Discharge, Follow-up, and Life After Transplant", "Longitudinal care", 5, 2, ["K4", "K6"]),
    ("10", "philhealth-and-registries", "Philippine Benefits, Documentation, and Privacy", "PhilHealth and registries", 5, 2.5, ["K7"]),
    ("11", "quality-and-special-populations", "Quality, Equity, and Special Populations", "Quality and special populations", 6, 2, ["K6", "K8"]),
    ("12", "capstone", "Capstone and Transition to Practice", "Capstone", 6, 4, ["K1", "K2", "K3", "K4", "K5", "K6", "K7", "K8"]),
]

COMPETENCIES = [
    ("K1", "Explain role boundaries, coordinate referral, and track evaluation, waitlist readiness and compatibility changes.", "Referral SBAR, readiness tracker, offer call record"),
    ("K2", "Protect donor voluntariness, confidentiality and appropriate referral.", "Private donor interview and escalation note"),
    ("K3", "Assess early postoperative recovery and escalate deterioration.", "OR-to-ward handoff and deteriorating-patient simulation"),
    ("K4", "Reconcile immunosuppression and manage monitoring and supply gaps within nursing scope.", "Two-source medication reconciliation and teach-back"),
    ("K5", "Recognize graft dysfunction and infection, and close the loop on triage and test results.", "Fever triage note and trend-based SBAR"),
    ("K6", "Plan longitudinal follow-up, including transition, equity and self-management.", "One-page discharge plan and care adaptation"),
    ("K7", "Apply Philippine coverage workflows, documentation and privacy safeguards.", "Synthetic benefits-readiness worksheet"),
    ("K8", "Measure a safety process and integrate decisions across settings.", "Improvement charter and four-station objective structured clinical examination (OSCE)"),
]

# token: (expansion, optional note). Merged into the nursing ABBR dict, which the glossary and auto-expansion read.
ABBR = {
    "ABMR": ("antibody-mediated rejection", ""),
    "TCMR": ("T-cell-mediated rejection", ""),
    "DSA": ("donor-specific antibody", "an antibody in the recipient that targets the donor's HLA"),
    "dnDSA": ("de novo donor-specific antibody", "one that first appears after transplant"),
    "HLA": ("human leukocyte antigen", "tissue markers the immune system uses to tell self from non-self"),
    "cPRA": ("calculated panel-reactive antibody", "the percentage of donors a candidate's antibodies would react against"),
    "ABO": ("blood group", "the A, B, AB and O blood group system"),
    "DGF": ("delayed graft function", "need for dialysis in the first week after transplant"),
    "CNI": ("calcineurin inhibitor", "tacrolimus or cyclosporine"),
    "MPA": ("mycophenolic acid", "the active form of mycophenolate"),
    "MMF": ("mycophenolate mofetil", ""),
    "CMV": ("cytomegalovirus", ""),
    "BKPyV": ("BK polyomavirus", ""),
    "PJP": ("Pneumocystis jirovecii pneumonia", ""),
    "TMP-SMX": ("trimethoprim-sulfamethoxazole", "cotrimoxazole"),
    "PTDM": ("post-transplantation diabetes mellitus", ""),
    "dd-cfDNA": ("donor-derived cell-free DNA", "a blood test of graft injury"),
    "IPV": ("intrapatient variability", "how much one person's drug levels swing on an unchanged dose"),
    "C/D": ("concentration-to-dose ratio", ""),
    "KT": ("kidney transplant", ""),
    "KDIGO": ("Kidney Disease: Improving Global Outcomes", ""),
    "SBAR": ("Situation, Background, Assessment, Recommendation", ""),
    "OSCE": ("objective structured clinical examination", ""),
    "OR": ("operating room", ""),
    "PACU": ("post-anesthesia care unit", ""),
    "NKTI": ("National Kidney and Transplant Institute", ""),
    "DOH": ("Department of Health", ""),
    "PRC": ("Professional Regulation Commission", ""),
    "NPC": ("National Privacy Commission", ""),
    "OPTN": ("Organ Procurement and Transplantation Network", "the United States allocation system"),
    "HOPE": ("Human Organ Preservation Effort", "the Philippine deceased donation program"),
    "TTE": ("transthoracic echocardiogram", ""),
    "ESKD": ("end-stage kidney disease", ""),
    "eGFR": ("estimated glomerular filtration rate", ""),
    "GFR": ("glomerular filtration rate", ""),
    "CKD": ("chronic kidney disease", ""),
    "AKI": ("acute kidney injury", ""),
    "UTI": ("urinary tract infection", ""),
    "CVP": ("central venous pressure", ""),
    "MAP": ("mean arterial pressure", ""),
    "OTC": ("over-the-counter", ""),
    "IVIG": ("intravenous immunoglobulin", ""),
    "PCR": ("polymerase chain reaction", ""),
    "QI": ("quality improvement", ""),
    "PDSA": ("Plan-Do-Study-Act", ""),
    "RN": ("registered nurse", ""),
    "TB": ("tuberculosis", ""),
    "PTLD": ("post-transplant lymphoproliferative disorder", ""),
    "NNT": ("number needed to treat", ""),
    "RCT": ("randomized controlled trial", ""),
    "ICU": ("intensive care unit", ""),
    "HFSRB": ("Health Facilities and Services Regulatory Bureau", ""),
    "CPD": ("continuing professional development", ""),
    "SGLT2": ("sodium-glucose cotransporter 2", ""),
    "CYP3A": ("cytochrome P450 3A", "the liver and gut enzyme family that breaks down tacrolimus"),
    "PhilHealth": ("Philippine Health Insurance Corporation", ""),
    "NSAID": ("nonsteroidal anti-inflammatory drug", ""),
    "HbA1c": ("glycated hemoglobin", ""),
    "PROM": ("patient-reported outcome measure", ""),
    "QAPI": ("quality assessment and performance improvement", ""),
    "CQI": ("continuous quality improvement", ""),
    "HCV": ("hepatitis C virus", ""),
    "ATG": ("anti-thymocyte globulin", ""),
}

# PubMed-verified references: key -> PMID (metadata in data/transplant-nurse/refs_pubmed_raw.json,
# with the three keys shared with the nursing course read from data/nursing-course/refs_pubmed_raw.json)
PUBMED_REFS = {
    "txcand2020": "32301874", "txrecip2009": "19845597", "mannon2018": "30007955",
    "wolfe1999": "10580071", "tonelli2011": "21883901", "lentine2017": "28742762", "muzaale2014": "24519297",
    "mjoen2014": "24284516", "garg2015": "25397608", "istanbul2018": "30681986", "greer2020": "32761206",
    "moers2009": "19118301", "collins2023": "37343576", "wilson2013": "23771708", "ekberg2007": "18094377",
    "vincenti2016": "26816011", "shuker2015": "25687818", "tholking2014": "25340655", "dew2007": "17460556",
    "schinstock2019": "30597643", "naesens2024": "38032300", "bloom2017": "28280140", "ho2022": "35019898",
    "lim2021": "32040251", "kotton2025": "40200403", "limaye2023": "37279999", "kotton2024": "38605438",
    "fishman2019": "31077616", "danziger2019": "31002409", "subramanian2019": "30817030", "engels2011": "22045767",
    "sharif2024": "38171510", "shah2019": "30674290", "foster2011": "21883752", "mcadams2015": "25359393",
    "jagodage2024": "37010245",
}

JOURNALS = {
    "N Engl J Med": "New England Journal of Medicine", "JAMA": "JAMA", "Transplantation": "Transplantation",
    "Am J Transplant": "American Journal of Transplantation", "Lancet": "Lancet",
    "Transplant Rev (Orlando)": "Transplantation Reviews", "PLoS One": "PLoS ONE",
    "J Am Soc Nephrol": "Journal of the American Society of Nephrology", "Clin Transplant": "Clinical Transplantation",
    "Pediatr Transplant": "Pediatric Transplantation", "BMC Nephrol": "BMC Nephrology",
    "Nephrol Dial Transplant": "Nephrology Dialysis Transplantation", "Kidney Int": "Kidney International",
    "Cochrane Database Syst Rev": "Cochrane Database of Systematic Reviews", "Intern Med J": "Internal Medicine Journal",
    "J Ren Care": "Journal of Renal Care", "Transpl Int": "Transplant International",
    "Clin J Am Soc Nephrol": "Clinical Journal of the American Society of Nephrology",
    "Kidney Int Suppl (2011)": "Kidney International Supplements",
    "Am J Kidney Dis": "American Journal of Kidney Diseases",
}

TITLE_OVERRIDES = {
    "37010245": "Effectiveness of teach-back for chronic kidney disease patient education: A systematic review",
    "37279999": "Letermovir vs valganciclovir for prophylaxis of cytomegalovirus in high-risk kidney transplant recipients: A randomized clinical trial",
    "32761206": "Determination of brain death/death by neurologic criteria: The World Brain Death Project",
    "28742762": "KDIGO clinical practice guideline on the evaluation and care of living kidney donors",
    "32301874": "KDIGO clinical practice guideline on the evaluation and management of candidates for kidney transplantation",
    "19845597": "KDIGO clinical practice guideline for the care of kidney transplant recipients",
    "30007955": "Delayed graft function: The AKI of kidney transplantation",
    "40200403": "The fourth international consensus guidelines on the management of cytomegalovirus in solid organ transplantation",
    "38605438": "The second international consensus guidelines on the management of BK polyomavirus in kidney transplantation",
    "37343576": "Balanced crystalloid solution versus saline in deceased donor kidney transplantation (BEST-Fluids): A pragmatic, double-blind, randomised, controlled trial",
    "25687818": "Intra-patient variability in tacrolimus exposure: Causes, consequences for clinical management",
    "38032300": "The Banff 2022 Kidney Meeting Report: Reappraisal of microvascular inflammation and the role of biopsy-based transcript diagnostics",
    "28280140": "Cell-free DNA and active rejection in kidney allografts",
    "30674290": "Pregnancy outcomes in women with kidney transplant: Metaanalysis and systematic review",
    "26816011": "Belatacept and long-term outcomes in kidney transplantation",
    "30681986": "The Declaration of Istanbul on Organ Trafficking and Transplant Tourism (2018 edition) introduction",
    "31002409": "Vaccination of solid organ transplant candidates and recipients: Guidelines from the American Society of Transplantation Infectious Diseases Community of Practice",
    "35019898": "Complications of percutaneous kidney allograft biopsy: Systematic review and meta-analysis",
    "32040251": "Desmopressin acetate to prevent bleeding in percutaneous kidney biopsy: A systematic review",
    "30817030": "Mycobacterium tuberculosis infections in solid organ transplantation: Guidelines from the Infectious Diseases Community of Practice of the American Society of Transplantation",
    "30597643": "Factors at de novo donor-specific antibody initial detection associated with allograft loss: A multicenter study",
}

RETRIEVED = "November 24, 2026"


def _link(url):
    return f'<a href="{url}">{url}</a>'


MANUAL_REFS = {
    "ra9173": ("Republic of the Philippines (RP). (2002). <em>Republic Act No. 9173: Philippine Nursing Act of 2002</em>. "
               + _link("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/2/1459")),
    "ra7170": ("Republic of the Philippines (RP). (1991). <em>Republic Act No. 7170: Organ Donation Act of 1991</em>. "
               + _link("https://lawphil.net/statutes/repacts/ra1992/ra_7170_1992.html")),
    "ra7885": ("Republic of the Philippines (RP). (1995). <em>Republic Act No. 7885: An act amending Republic Act No. 7170</em>. "
               + _link("https://lawphil.net/statutes/repacts/ra1995/ra_7885_1995.html")),
    "ra10173": ("National Privacy Commission (NPC). (2012). <em>Republic Act No. 10173: Data Privacy Act of 2012</em>. "
                + _link("https://lawphil.net/statutes/repacts/ra2012/ra_10173_2012.html")),
    "doh2010_18": ("Department of Health (DOH). (2010). <em>Administrative Order No. 2010-0018: Amendment to Administrative "
                   "Order No. 2008-0004-A on living non-related organ donation and transplantation</em>. "
                   + _link("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/52059")),
    "doh2010_19": ("Department of Health (DOH). (2010). <em>Administrative Order No. 2010-0019: Policies and guidelines on "
                   "deceased donor organ sharing, procurement and allocation</em>. "
                   + _link("https://elibrary.judiciary.gov.ph/thebookshelf/showdocs/10/52063")),
    "doh2021_19": ("Department of Health (DOH). (2021). <em>Administrative Order No. 2021-0019: Revised rules and regulations "
                   "on the licensure of hospitals</em>. "
                   + _link("https://law.upd.edu.ph/wp-content/uploads/2021/05/DOH-Administrative-Order-No-2021-0019.pdf")),
    "phic2024_35": ("Philippine Health Insurance Corporation (PHIC). (2024). <em>PhilHealth Circular No. 2024-0035: "
                    "Z Benefits package for kidney transplantation</em>. "
                    + _link("https://www.philhealth.gov.ph/circulars/2024/PC2024-0035.pdf")),
    "phic2025_11": ("Philippine Health Insurance Corporation (PHIC). (2025). <em>PhilHealth Circular No. 2025-0011: "
                    "Z Benefits package for post-kidney transplantation services in children</em>. "
                    + _link("https://www.philhealth.gov.ph/circulars/2025/PC2025-0011.pdf")),
    "phic2025_12": ("Philippine Health Insurance Corporation (PHIC). (2025). <em>PhilHealth Circular No. 2025-0012: "
                    "Z Benefits package for post-kidney transplantation services in adults</em>. "
                    + _link("https://www.philhealth.gov.ph/circulars/2025/PC2025-0012.pdf")),
    "phic2026_26": ("Philippine Health Insurance Corporation (PHIC). (2026). <em>PhilHealth Advisory No. 2026-0026: "
                    "Implementation of the kidney transplantation (KT) data registry system</em>. "
                    + _link("https://www.philhealth.gov.ph/advisories/2026/PA2026-0026.pdf")),
    "phic_providers": ("Philippine Health Insurance Corporation (PHIC). (2026). <em>Contracted health facilities</em>. "
                       f"Retrieved {RETRIEVED}, from "
                       + _link("https://www.philhealth.gov.ph/partners/providers/facilities/contracted/")),
    "psn_cpg": ("Philippine Society of Nephrology (PSN). (2020). <em>Clinical practice guidelines and protocols</em>. "
                f"Retrieved {RETRIEVED}, from " + _link("https://psn.org.ph/education/clinical-practice-guideline-and-protocols/")),
    "nkti_pia": ("Philippine Information Agency (PIA). (2025). <em>NKTI expands training to enhance transplant services across "
                 "PH</em>. " + _link("https://pia.gov.ph/news/nkti-expands-training-to-enhance-transplant-services-across-ph/")),
    "mmc2025": ("Makati Medical Center (MMC). (2025). <em>Transplant coordinator</em> [Job posting]. "
                + _link("https://www.makatimed.net.ph/career/transplant-coordinator/")),
    "optn": ("Health Resources and Services Administration (HRSA). (2026). <em>OPTN policies</em>. "
             f"Retrieved {RETRIEVED}, from " + _link("https://www.hrsa.gov/optn/policies-bylaws/policies")),
    "abtc": ("American Board for Transplant Certification (ABTC). (2026). <em>Frequently asked questions</em>. "
             f"Retrieved {RETRIEVED}, from " + _link("https://abtc.net/about/frequently-asked-questions")),
    "mn_bon": ("Minnesota Board of Nursing (MBN). (2026). <em>RN licensure by examination: Internationally educated nurses</em>. "
               f"Retrieved {RETRIEVED}, from "
               + _link("https://mn.gov/boards/nursing/licensure/apply-for-a-license/rn-lic-exam-foreign-prog.jsp")),
    "mayo_pre": ("Mayo Clinic (MAYO). (2026). <em>RN transplant care coordinator, pre kidney/pancreas, outpatient</em> [Job posting]. "
                 + _link("https://jobs.mayoclinic.org/job/rochester/rn-transplant-care-coordinator-pre-kidney-pancreas-outpatient/33647/102051636336")),
    "nmc": ("Nursing and Midwifery Council (NMC). (2026). <em>Joining the register: Trained outside the UK</em>. "
            f"Retrieved {RETRIEVED}, from "
            + _link("https://www.nmc.org.uk/registration/joining-the-register/register-nurse-midwife/trained-outside-uk/how-to-guide/")),
    "cno": ("College of Nurses of Ontario (CNO). (2026). <em>Registration requirements</em>. "
            f"Retrieved {RETRIEVED}, from " + _link("https://www.cno.org/become-a-nurse/registration-requirements?l=en-ca")),
    "uhn": ("University Health Network (UHN). (2026). <em>Kidney transplant program: Our team</em>. "
            f"Retrieved {RETRIEVED}, from " + _link("https://www.uhn.ca/Transplant/Kidney_Transplant_Program/Pages/our_team.aspx")),
    "swslhd": ("South Western Sydney Local Health District (SWSLHD). (2026). <em>Liverpool Hospital renal nursing specialty services</em>. "
               f"Retrieved {RETRIEVED}, from " + _link("https://www.swslhd.health.nsw.gov.au/liverpool/Renal/serv_nurs.html")),
}

HUB_REFS = ["txcand2020", "lentine2017", "txrecip2009", "kotton2025", "kotton2024", "ra9173", "ra7170", "doh2010_18",
            "doh2010_19", "phic2024_35", "phic2025_11", "phic2025_12", "phic2026_26", "ra10173", "nkti_pia", "mmc2025",
            "abtc", "optn", "mn_bon", "mayo_pre", "nmc", "cno", "uhn", "swslhd"]

# Hub: a fictional week on the transplant service (scenarios drawn from the modules)
WEEK_HTML = """
<p>Before the modules, here is what the job looks like. The week below is fictional, and so are all the people in it, but every moment comes from situations transplant nurses meet regularly. Each day points to the module that prepares you for it. Nurse Carla, Joy the recipient coordinator, and Dr. Santos the transplant nephrologist appear throughout the subtrack.</p>
<div class="tc-sits">
<div class="tc-sit"><h3>Monday &middot; kidney clinic</h3><dl>
<dt>What happens</dt><dd>A truck driver with diabetic kidney disease has an estimated glomerular filtration rate (eGFR) that has fallen to 19. Nobody has mentioned transplant to him. He works on another island and can only take calls after 7 p.m.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Raise transplant with him and his wife, send a complete referral that includes his evening-only contact window, and confirm that Joy has received it. Module 1.</dd></dl></div>
<div class="tc-sit"><h3>Tuesday &middot; by phone</h3><dl>
<dt>What happens</dt><dd>On a routine call, a woman on the waiting list mentions that she was given two bags of blood at a provincial hospital last month.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Recognize a sensitizing event, notify the coordinator and the laboratory so a fresh sample is drawn, and name an owner for each follow-up. Module 2.</dd></dl></div>
<div class="tc-sit"><h3>Wednesday &middot; donor intake</h3><dl>
<dt>What happens</dt><dd>Alone with you, a potential living donor goes quiet when you ask what would happen if she said no. Then she says she cannot refuse her sister.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Tell her she may stop at any point, keep her words in the restricted donor record, and route them to the donor team the same day. Module 3.</dd></dl></div>
<div class="tc-sit"><h3>Thursday, 2 a.m. &middot; transplant ward</h3><dl>
<dt>What happens</dt><dd>Six hours after surgery, a recipient's urine output falls, his pulse climbs, and the drain fills with dark red blood.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Read the three trends together, hold off on extra fluid, activate the emergency response, and stay at the bedside. Module 5.</dd></dl></div>
<div class="tc-sit"><h3>Friday &middot; transplant clinic</h3><dl>
<dt>What happens</dt><dd>A tacrolimus level is far above the patient's usual. She took her morning dose before the blood draw, and she has a new prescription for clarithromycin from a provincial clinic.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Flag the level as not a trough, report the interaction before she starts the antibiotic, and teach the trough routine with teach-back. Module 6.</dd></dl></div>
<div class="tc-sit"><h3>Saturday, 4 p.m. &middot; hotline</h3><dl>
<dt>What happens</dt><dd>Five months after transplant, a recipient who stopped her antiviral prophylaxis three weeks ago calls with chills and weakness. She is passing little urine and vomited her morning medicines.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Get her location and callback number first, route her to emergency care now, and notify the on-call transplant physician. Module 8.</dd></dl></div>
</div>
<p>None of these moments asks the nurse to make the medical decision. Every one of them depends on the nurse noticing, asking the right question, and handing over clearly to the person who decides. That is what this subtrack trains.</p>
"""
