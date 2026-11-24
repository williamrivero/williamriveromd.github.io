# -*- coding: utf-8 -*-
"""Special Dialysis Nurse Roles subtrack of the Renal Care Academy (Nephrology Nursing, By Role).

Course metadata, abbreviations, references and shared copy. Module content lives in mNN.py.
Rendered by generate_special_dialysis_nurse_roles.py; never hand-edit the generated academy pages.
Blueprint: /Volumes/Storage/Renal Care Academy/Special Dialysis Nurse Roles/v2/SDNR-BLUEPRINT-v2.md
"""

COURSE = {
    "title": "Special Dialysis Nurse Roles",
    "long_title": "Special Dialysis Nurse Roles",
    "hub_slug": "special-dialysis-nurse-roles",
    "parent_slug": "nephrology-nursing",
    "entry_slug": "nephrology-nursing-12-philippine-practice-quality-capstone",
    "label": "Role subtrack for registered nurses",
    "review_date": "2026-11-24",
    "core_hours": 60,
    "supervised_hours": 51,
    "pass_correct": 12,
    "exam_items": 14,
}

SCOPE_NOTE = (
    "This subtrack prepares Philippine registered nurses who are <strong>assigned</strong> a special portfolio in a "
    "hemodialysis unit: vascular access, infection prevention, education, quality, safety, coordination, anemia, transplant "
    "liaison, records, water and equipment liaison, or adequacy and outcomes. It teaches assessment, coordination, teaching "
    "and escalation within nursing scope. Prescriptions, dose changes, access procedures, transplant listing, water-system "
    "repair and technical release belong to the physician, the authorized team and the technical staff. All cases are synthetic."
)

# id, slug suffix, title, short title, week, hours, competencies, SDNR code, (study, workshop, supervised)
MODULES = [
    ("01", "foundations-and-role-charter", "Foundations: Portfolios, Authority and the Role Charter", "Foundations", 1, 4, ["S1", "S4"], "SDNR-00", (2, 1, 1)),
    ("02", "vascular-access", "Vascular Access Nurse and Coordinator", "Vascular access", 1, 10, ["S2", "S4"], "SDNR-01", (3, 2, 5)),
    ("03", "infection-prevention", "Infection Prevention and Control Nurse", "Infection prevention", 2, 9, ["S2", "S6"], "SDNR-02", (3, 2, 4)),
    ("04", "educator-and-preceptor", "Nurse Educator and Clinical Preceptor", "Educator and preceptor", 2, 8, ["S3"], "SDNR-03", (2, 2, 4)),
    ("05", "patient-education", "Patient Education and Self-Management Nurse", "Patient education", 3, 7, ["S3"], "SDNR-04", (2, 2, 3)),
    ("06", "quality-improvement-audit", "Quality Improvement and Clinical Audit Nurse", "Quality and audit", 3, 8, ["S5"], "SDNR-05", (3, 2, 3)),
    ("07", "safety-and-emergency-preparedness", "Patient Safety and Emergency Preparedness Nurse", "Safety and emergencies", 4, 8, ["S6"], "SDNR-06", (2, 2, 4)),
    ("08", "care-coordination-transitions", "Case Management and Care Coordination Nurse", "Care coordination", 4, 8, ["S4"], "SDNR-07", (2, 2, 4)),
    ("09", "anemia-and-medication-safety", "Anemia Management and Medication Safety Nurse", "Anemia and medicines", 5, 9, ["S2", "S4"], "SDNR-08", (3, 2, 4)),
    ("10", "transplant-and-options-liaison", "Transplant Referral and Treatment Options Liaison", "Transplant liaison", 5, 7, ["S3", "S4"], "SDNR-09", (2, 2, 3)),
    ("11", "records-registry-philhealth", "Documentation, Registry and PhilHealth Liaison Nurse", "Records and PhilHealth", 6, 7, ["S7"], "SDNR-10", (2, 2, 3)),
    ("12", "water-dialysate-equipment-liaison", "Water, Dialysate and Equipment Safety Liaison Nurse", "Water and equipment", 6, 9, ["S2", "S6"], "SDNR-11", (3, 2, 4)),
    ("13", "adequacy-volume-outcomes", "Dialysis Adequacy, Volume and Outcomes Nurse", "Adequacy and volume", 7, 9, ["S2", "S5"], "SDNR-12", (3, 2, 4)),
    ("14", "capstone", "Integrated Portfolio Practicum and Capstone", "Capstone", 7, 8, ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"], "SDNR-13", (1, 2, 5)),
]

COMPETENCIES = [
    ("S1", "Read a requirement at its true level of authority and write a role charter with escalation, backup and limits.", "Signed role charter and source-authority worksheet"),
    ("S2", "Turn a bedside finding (access, infection, anemia trend, water or equipment status, adequacy data) into the right urgency and the right person.", "Focused assessment and SBAR in simulation; observed escalation"),
    ("S3", "Teach a patient or a colleague and check the result by observation or teach-back, not by attendance.", "Teach-back record, microteaching, direct-observation form"),
    ("S4", "Close a loop: referral sent, received, acted on, returned and documented, with one named owner per action.", "Referral tracker and transition reconciliation record"),
    ("S5", "Define a measure with an honest numerator, denominator and exclusions, show it over time, and run a small test of change.", "Measure specification, run chart and PDSA log"),
    ("S6", "Recognize a system hazard (transmission, emergency, water or equipment) and stop harm before investigating.", "IPC observation set, drill debrief, stop-use and release record"),
    ("S7", "Keep clinical, registry and claims records truthful, amend without concealment, and protect privacy.", "Documentation audit and amendment exercise"),
    ("S8", "Integrate safety, scope and coordination in a multi-problem shift and present portfolio evidence.", "Four-station capstone OSCE and portfolio presentation"),
]

ABBR = {
    "SDNR": ("Special Dialysis Nurse Roles", "the code used for this subtrack's modules"),
    "AVF": ("arteriovenous fistula", ""),
    "AVG": ("arteriovenous graft", ""),
    "CVC": ("central venous catheter", ""),
    "IPC": ("infection prevention and control", ""),
    "BSI": ("bloodstream infection", ""),
    "DART": ("Dialysis Audit and Reporting Tools", "the CDC observation checklists for dialysis units"),
    "CDC": ("Centers for Disease Control and Prevention", ""),
    "HBV": ("hepatitis B virus", ""),
    "HCV": ("hepatitis C virus", ""),
    "HIV": ("human immunodeficiency virus", ""),
    "PPE": ("personal protective equipment", ""),
    "ESA": ("erythropoiesis-stimulating agent", ""),
    "EPO": ("erythropoietin", ""),
    "HIF-PHI": ("hypoxia-inducible factor prolyl hydroxylase inhibitor", ""),
    "TSAT": ("transferrin saturation", ""),
    "Hb": ("hemoglobin", ""),
    "URR": ("urea reduction ratio", ""),
    "UFR": ("ultrafiltration rate", ""),
    "IDWG": ("interdialytic weight gain", ""),
    "BUN": ("blood urea nitrogen", ""),
    "KRT": ("kidney replacement therapy", ""),
    "QAPI": ("quality assessment and performance improvement", ""),
    "CQI": ("continuous quality improvement", ""),
    "QI": ("quality improvement", ""),
    "PDSA": ("Plan-Do-Study-Act", ""),
    "SBAR": ("Situation, Background, Assessment, Recommendation", ""),
    "OSCE": ("objective structured clinical examination", ""),
    "PRDR": ("Philippine Renal Disease Registry", ""),
    "PRC": ("Professional Regulation Commission", ""),
    "DOH": ("Department of Health", ""),
    "PSN": ("Philippine Society of Nephrology", ""),
    "PhilHealth": ("Philippine Health Insurance Corporation", ""),
    "KDIGO": ("Kidney Disease: Improving Global Outcomes", ""),
    "KDOQI": ("Kidney Disease Outcomes Quality Initiative", ""),
    "DOPPS": ("Dialysis Outcomes and Practice Patterns Study", ""),
    "HEMO": ("Hemodialysis Study", "a United States randomized trial of dialysis dose and membrane flux"),
    "RO": ("reverse osmosis", ""),
    "BLS": ("basic life support", ""),
    "ACLS": ("advanced cardiovascular life support", ""),
    "CPD": ("continuing professional development", ""),
    "CKD": ("chronic kidney disease", ""),
    "ESKD": ("end-stage kidney disease", ""),
    "eGFR": ("estimated glomerular filtration rate", ""),
    "KFRE": ("Kidney Failure Risk Equation", ""),
    "HD": ("hemodialysis", ""),
    "PD": ("peritoneal dialysis", ""),
    "ICU": ("intensive care unit", ""),
    "RN": ("registered nurse", ""),
    "AO": ("Administrative Order", ""),
    "RA": ("Republic Act", ""),
    "NPC": ("National Privacy Commission", ""),
    "HFSRB": ("Health Facilities and Services Regulatory Bureau", ""),
    "CHD": ("Center for Health Development", "the DOH regional office"),
    "RCT": ("randomized controlled trial", ""),
    "CI": ("confidence interval", ""),
    "HR": ("hazard ratio", ""),
    "RR": ("relative risk", ""),
    "NNT": ("number needed to treat", ""),
    "CKD-MBD": ("chronic kidney disease–mineral and bone disorder", ""),
    "NSAID": ("nonsteroidal anti-inflammatory drug", ""),
    "VND": ("venous needle dislodgement", ""),
    "AHRQ": ("Agency for Healthcare Research and Quality", ""),
    "CMS": ("Centers for Medicare &amp; Medicaid Services", ""),
    "WHO": ("World Health Organization", ""),
    "ISO": ("International Organization for Standardization", ""),
    "NHS": ("National Health Service", "the United Kingdom's public health system"),
    "IV": ("intravenous", ""),
    "MRSA": ("methicillin-resistant <em>Staphylococcus aureus</em>", ""),
    "ECG": ("electrocardiogram", ""),
    "BP": ("blood pressure", ""),
    "UPS": ("uninterruptible power supply", ""),
    "HLA": ("human leukocyte antigen", ""),
    "CBC": ("complete blood count", ""),
    "AKI": ("acute kidney injury", ""),
    "TB": ("tuberculosis", ""),
}

# PubMed-verified references: key -> PMID. Metadata is read from data/{nursing-course,transplant-nurse,
# dialysis-unit-support-staff,special-dialysis-nurse-roles}/refs_pubmed_raw.json.
PUBMED_REFS = {
    # reused, verified in earlier Academy builds
    "va2019": "32778223", "patel2013": "23676763", "talevski2020": "32287296", "jagodage2024": "37010245",
    "taylor2017": "28487346", "cavanaugh2010": "20671215", "sever2023": "37479903", "vnd2008": "19090893",
    "txcand2020": "32301874", "wolfe1999": "10580071", "istanbul2018": "30681986",
    "caruaru1998": "9516222", "daugirdas1993": "8305648", "flythe2011": "20927040",
    "thompson2009": "19124818", "pittet2000": "11073019", "hcv2022": "36410841",
    "bond1981": "6111645", "muir2014": "24370768", "wong2014": "25110302",
    # new for this subtrack (verified 24 November 2026)
    "ravani2013": "23431075", "ravani2016": "26776537", "cook2011": "21900138", "perla2011": "21228075",
    "taylor2014": "24025320", "pivotal2019": "30365356", "treat2009": "19880844", "owen1993": "8366899",
    "hemo2002": "12490682", "saran2006": "16609686",
}

JOURNALS = {
    "J Am Soc Nephrol": "Journal of the American Society of Nephrology", "Am J Kidney Dis": "American Journal of Kidney Diseases",
    "JAMA": "JAMA", "BMJ Qual Saf": "BMJ Quality &amp; Safety", "N Engl J Med": "New England Journal of Medicine",
    "Kidney Int": "Kidney International", "J Ren Care": "Journal of Renal Care", "Transplantation": "Transplantation",
    "Ann Intern Med": "Annals of Internal Medicine", "Lancet": "The Lancet",
}

TITLE_OVERRIDES = {
    "26776537": "Preemptive correction of arteriovenous access stenosis: A systematic review and meta-analysis of randomized controlled trials",
    "23431075": "Associations between hemodialysis access type and clinical outcomes: A systematic review",
    "21900138": "Technology-enhanced simulation for health professions education: A systematic review and meta-analysis",
    "21228075": "The run chart: A simple analytical tool for learning from variation in healthcare processes",
    "16609686": "Longer treatment time and slower ultrafiltration in hemodialysis: Associations with reduced mortality in the DOPPS",
    "37010245": "Effectiveness of teach-back for chronic kidney disease patient education: A systematic review",
    "41485807": "Executive summary of the KDIGO 2026 clinical practice guideline for the management of anemia in chronic kidney disease (CKD)",
    "30681986": "The Declaration of Istanbul on Organ Trafficking and Transplant Tourism (2018 edition) introduction",
    "32301874": "KDIGO clinical practice guideline on the evaluation and management of candidates for kidney transplantation",
    "28487346": "A systematic review of the prevalence and associations of limited health literacy in CKD",
    "20671215": "Low health literacy associates with increased mortality in ESRD",
    "32287296": "Teach-back: A systematic review of implementation and impacts",
    "37479903": "Disasters and kidney care: Pitfalls and solutions",
    "19090893": "Venous needle dislodgement: How to minimise the risks",
    "19124818": "Nonhospital health care-associated hepatitis B and C virus transmission: United States, 1998-2008",
    "8305648": "Second generation logarithmic estimates of single-pool variable volume Kt/V: An analysis of error",
    "23676763": "Bloodstream infection rates in outpatient hemodialysis facilities participating in a collaborative prevention effort: A quality improvement report",
    "32778223": "KDOQI clinical practice guideline for vascular access: 2019 update",
    "26498416": "KDOQI clinical practice guideline for hemodialysis adequacy: 2015 update",
}

RETRIEVED = "November 24, 2026"


def _link(url):
    return f'<a href="{url}">{url}</a>'


MANUAL_REFS = {
    "hd2015": ("National Kidney Foundation (NKF). (2015). KDOQI clinical practice guideline for hemodialysis adequacy: 2015 update. "
               "<em>American Journal of Kidney Diseases</em>, <em>66</em>(5), 884–930. " + _link("https://doi.org/10.1053/j.ajkd.2015.07.015")),
    "phic2024_29": ("Philippine Health Insurance Corporation (PHIC). (2024). <em>PhilHealth Circular No. 2024-0029: Quality standards "
                    "on maintenance hemodialysis</em>. " + _link("https://www.philhealth.gov.ph/circulars/2024/PC2024-0029.pdf")),
    "phic2024_23": ("Philippine Health Insurance Corporation (PHIC). (2024). <em>PhilHealth Circular No. 2024-0023: Hemodialysis "
                    "benefits (Revision 2)</em>. " + _link("https://www.philhealth.gov.ph/circulars/2024/PC2024-0023.pdf")),
    "phic2026_idx": ("Philippine Health Insurance Corporation (PHIC). (2026). <em>PhilHealth circulars 2026</em> [Index, including "
                     f"Circular No. 2026-0019 on kidney transplantation benefits]. Retrieved {RETRIEVED}, from "
                     + _link("https://www.philhealth.gov.ph/circulars/2026/archives.php")),
    "ra7170": ("Republic of the Philippines (RP). (1991). <em>Republic Act No. 7170: Organ Donation Act of 1991</em>. "
               + _link("https://lawphil.net/statutes/repacts/ra1992/ra_7170_1992.html")),
    "cdc_core": ("Centers for Disease Control and Prevention (CDC). (2024). <em>Core interventions for dialysis bloodstream infection "
                 f"prevention</em>. Retrieved {RETRIEVED}, from " + _link("https://www.cdc.gov/dialysis-safety/hcp/clinical-safety/")),
    "cdc_dart": ("Centers for Disease Control and Prevention (CDC). (2026). <em>Dialysis Audit and Reporting Tools (DART) toolkit</em>. "
                 f"Retrieved {RETRIEVED}, from " + _link("https://www.cdc.gov/dialysis-safety/php/dart-toolkit/index.html")),
    "cdc_water": ("Centers for Disease Control and Prevention (CDC). (2024). <em>Considerations for water use in dialysis</em>. "
                  f"Retrieved {RETRIEVED}, from " + _link("https://www.cdc.gov/dialysis-safety/hcp/recommendations-resources/water-use-in-dialysis.html")),
    "cdc_steward": ("Centers for Disease Control and Prevention (CDC). (2023). <em>Core elements of antibiotic stewardship for "
                    "outpatient hemodialysis facilities</em>. "
                    + _link("https://www.cdc.gov/antibiotic-use/media/pdfs/Core-Elements-Outpatient-Hemodialysis-508.pdf")),
    "ahrq_tool5": ("Agency for Healthcare Research and Quality (AHRQ). (2024). <em>Health literacy universal precautions toolkit</em> "
                   f"(3rd ed.), Tool 5: Use the teach-back method. Retrieved {RETRIEVED}, from "
                   + _link("https://www.ahrq.gov/health-literacy/improve/precautions/tool5.html")),
    "cms_appz": ("Centers for Medicare &amp; Medicaid Services (CMS). (2019). <em>State operations manual, Appendix Z: Emergency "
                 "preparedness for all provider and certified supplier types</em>. "
                 + _link("https://www.cms.gov/regulations-and-guidance/guidance/manuals/downloads/som107ap_z_emergprep.pdf")),
    "cms_meas26": ("Centers for Medicare &amp; Medicaid Services (CMS). (2026). <em>ESRD measures manual for the 2026 performance "
                   "period</em> (Version 11.1). " + _link("https://www.cms.gov/files/document/esrd-measures-manual-v11-1.pdf")),
    "who_ipc": ("World Health Organization (WHO). (2020). <em>Core competencies for infection prevention and control professionals</em>. "
                + _link("https://www.who.int/publications/i/item/9789240011656")),
    "who_tx": ("World Health Organization (WHO). (2010). <em>WHO guiding principles on human cell, tissue and organ transplantation</em>. "
               + _link("https://www.who.int/publications/i/item/WHO-HTP-EHT-CPR-2010.01")),
    "ukka_va": ("UK Kidney Association (UKKA). (2023). <em>Vascular access for haemodialysis</em> [Clinical practice guideline]. "
                + _link("https://www.ukkidney.org/sites/default/files/FINAL%20FORMATTED%20Vascular%20access%20for%20haemodialysis%20April%202023.pdf")),
    "nhs_edu": ("NHS England (NHSE). (2026). <em>Nursing and midwifery educator framework</em>. "
                + _link("https://www.england.nhs.uk/long-read/nursing-and-midwifery-educator-framework/")),
    "bcr_urea": ("BC Renal (BCR). (2015). <em>Urea testing pre and post hemodialysis</em>. "
                 + _link("https://www.bcrenal.ca/resource-gallery/Documents/Urea%20Testing%20Pre%20and%20Post%20Hemodialysis.pdf")),
    "bcr_team": ("BC Renal (BCR). (2019). <em>The hemodialysis interdisciplinary team: Hemodialysis workforce strategy</em>. "
                 + _link("https://www.bcrenal.ca/resource-gallery/Documents/The_Hemodialysis_Interdisciplinary_Team-Hemodialysis_Workforce_Strategy.pdf")),
    "anna_spec": ("American Nephrology Nurses Association (ANNA). (2026). <em>The nephrology nursing specialty</em>. "
                  f"Retrieved {RETRIEVED}, from " + _link("https://www.annanurse.org/nephrology-nursing/")),
    "nhsbt_coord": ("NHS Blood and Transplant (NHSBT). (2026). <em>Role of the transplant recipient coordinator</em>. "
                    f"Retrieved {RETRIEVED}, from "
                    + _link("https://www.odt.nhs.uk/odt-structures-and-standards/organ-donation-retrieval-and-transplantation-teams/role-of-transplant-recipient-co-ordinator/")),
    "epo_label": ("National Library of Medicine (NLM). (2026). <em>DailyMed: Epoetin alfa prescribing information</em>. "
                  f"Retrieved {RETRIEVED}, from " + _link("https://dailymed.nlm.nih.gov/dailymed/search.cfm?labeltype=all&amp;query=epoetin+alfa")),
}

# Shared references reused from the parent nursing course (tools/nursing/content/common.py MANUAL_REFS):
SHARED_MANUAL = ["doh2012", "doh2013", "psn2024", "ra9173", "ra10173", "iso23500_3", "iso23500_5", "anemia2026", "cdc2001", "anna7"]

HUB_REFS = ["doh2012", "psn2024", "ra9173", "ra10173", "phic2024_29", "phic2024_23", "phic2026_idx", "cdc_core", "who_ipc",
            "va2019", "anemia2026", "hd2015", "txcand2020", "anna_spec", "bcr_team", "nhs_edu", "nhsbt_coord"]

WEEK_HTML = """
<p>Before the modules, here is what portfolio work looks like. The week below is fictional, and so are all the people in it, but every moment comes from situations dialysis units meet regularly. Each day points to the module that prepares you for it. Nurse Aileen, the unit's access coordinator, Nurse Benjo, who holds the infection prevention portfolio, and Dr. Reyes, the attending nephrologist, appear throughout the subtrack.</p>
<div class="tc-sits">
<div class="tc-sit"><h3>Monday, 6:40 a.m. &middot; station 4</h3><dl>
<dt>What happens</dt><dd>Mang Tonyo's fistula has no thrill this morning. He says his left hand has felt cold and painful since last night. His surgical follow-up is three weeks away.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Do not cannulate. Check the hand against the other side, notify the nephrologist now, and get the vascular surgeon's same-day decision recorded with a named owner. Module 2.</dd></dl></div>
<div class="tc-sit"><h3>Tuesday, 11 a.m. &middot; second shift</h3><dl>
<dt>What happens</dt><dd>Two patients with catheters develop rigors within an hour. A shared supply tray has been moving between their stations.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Help the charge nurse with immediate care, take the tray out of use, start a line list, and keep the supplies for review. Module 3.</dd></dl></div>
<div class="tc-sit"><h3>Wednesday &middot; quality meeting</h3><dl>
<dt>What happens</dt><dd>A slide says referral completion is 100 percent. You know 20 referrals were due, 12 forms were sent, and only 8 plans have come back.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Show the true closure rate, 8 of 20, and propose one small test of change with a run chart. Module 6.</dd></dl></div>
<div class="tc-sit"><h3>Thursday, 2 p.m. &middot; power interruption</h3><dl>
<dt>What happens</dt><dd>The lights flicker and machines switch to battery. One patient's venous needle is hidden under a blanket. Someone suggests silencing the alarms.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Uncover every needle site, keep alarms active, and follow the unit's power-failure procedure under the charge nurse's direction. Module 7.</dd></dl></div>
<div class="tc-sit"><h3>Friday &middot; anemia review</h3><dl>
<dt>What happens</dt><dd>A patient's hemoglobin has fallen from 10.2 to 8.1 g/dL in two weeks. He mentions black stools. The spreadsheet suggests raising his erythropoiesis-stimulating agent dose.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Treat it as possible bleeding, not a dose step. Check vital signs, report to the physician today, and hold the spreadsheet suggestion until the prescriber reviews. Module 9.</dd></dl></div>
<div class="tc-sit"><h3>Saturday &middot; machine release</h3><dl>
<dt>What happens</dt><dd>After overnight disinfection, a machine's release sheet is unsigned and the residual disinfectant test is missing. The next patient is waiting.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Keep the machine out of use, call the technician on duty for release, and move the patient to a released machine. Module 12.</dd></dl></div>
</div>
<p>None of these moments asks the nurse to make the medical or engineering decision. Every one depends on a nurse who notices, checks what the evidence actually shows, and hands over clearly to the person who decides. That is what a special role adds to a unit, and what this subtrack trains.</p>
"""

CROSSWALK_HTML = """
<div class="table-wrap"><table>
<thead><tr><th>Source</th><th>What it says (in its own terms)</th><th>What it means for a portfolio nurse</th></tr></thead>
<tbody>
<tr><td>DOH Administrative Order 2012-0001</td><td>Dialysis nurses are PRC-licensed, with a renal dialysis training certificate and BLS; at least one ACLS-trained nurse per shift. Nurse-to-patient <strong>stations</strong>: no more than 1:4. Patient education, transplant linkage, registry participation and a records function are facility duties.</td><td>A portfolio is extra work on top of safe licensed staffing. Many of the twelve portfolios support duties the facility already owes; none is defined as a separate post.</td></tr>
<tr><td>PSN Hemodialysis Guidelines, 2024</td><td>Describes structured renal-nursing preparation of three months or more, BLS and ACLS, and a nurse-to-<strong>patient</strong> ratio of 1:4, with 1:6 where a trained assistant supports the nurse. Discusses records, registry work and QAPI.</td><td>Society guidance, shown beside the DOH wording. It does not by itself change the DOH station-based provision. Never read either as permission to change a roster.</td></tr>
<tr><td>RA 9173, Philippine Nursing Act</td><td>The nursing process, health teaching, collaboration and carrying out prescribed therapies are within nursing practice.</td><td>Assess, coordinate, teach, check orders and escalate. Do not prescribe or change doses.</td></tr>
<tr><td>PhilHealth Circulars 2024-0029 and 2024-0023</td><td>Payer quality standards and hemodialysis benefits, with prescription and treatment-documentation provisions.</td><td>Truthful delivered-treatment records. A benefit rule is not a clinical order or a nursing qualification.</td></tr>
<tr><td>RA 10173, Data Privacy Act</td><td>Health information is sensitive personal information.</td><td>Role-based access, minimum necessary data, secure release. Academy cases stay fictional.</td></tr>
</tbody></table></div>
"""

# Role chooser on the hub: (who, module ids). Advisory only; every page stays open.
PATHWAYS = [
    ("Newly assigned vascular access nurse", ["01", "02", "06", "14"]),
    ("Infection prevention champion", ["01", "03", "06", "14"]),
    ("Unit educator or preceptor", ["01", "04", "05", "06", "14"]),
    ("Patient education nurse", ["01", "05", "08"]),
    ("Quality improvement or audit nurse", ["01", "06", "14"]),
    ("Safety and emergency preparedness nurse", ["01", "07", "06", "14"]),
    ("Care coordinator or case manager", ["01", "08", "05", "06"]),
    ("Anemia and medication safety nurse", ["01", "09", "06", "14"]),
    ("Transplant and treatment-options liaison", ["01", "05", "08", "10"]),
    ("Records, registry or PhilHealth liaison nurse", ["01", "11", "06"]),
    ("Water, dialysate and equipment liaison nurse", ["01", "12", "03", "14"]),
    ("Adequacy, volume and outcomes nurse", ["01", "13", "06", "14"]),
    ("Professional development: the whole subtrack", ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12", "13", "14"]),
]
