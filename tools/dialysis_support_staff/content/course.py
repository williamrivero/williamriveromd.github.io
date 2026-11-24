# -*- coding: utf-8 -*-
"""Dialysis Unit Support Staff subtrack of the Renal Care Academy (Nephrology Nursing).

Orderlies and environmental service (EVS) aides. Course metadata, abbreviations, references and shared copy.
Module content lives in mNN.py. Rendered by generate_dialysis_support_staff.py; never hand-edit the pages.
Improved from the owner's blueprint package (/Volumes/Storage/Renal Care Academy/Dialysis Unit Support Staff).
"""

COURSE = {
    "title": "Dialysis Unit Support Staff",
    "long_title": "Orderlies and Environmental Service Aides in the Dialysis Unit",
    "hub_slug": "dialysis-unit-support-staff",
    "parent_slug": "nephrology-nursing",
    "entry_slug": "nephrology-nursing-07-hd-vascular-access-infection-prevention",
    "label": "Nonclinical support pathway &middot; orderlies and environmental service aides",
    "review_date": "2026-11-24",
    "guided_hours": 30,
    "practice_hours": 28,
    "pass_correct": 12,
    "exam_items": 15,
    "status": "Draft for clinical, infection prevention and regulatory review",
}

SCOPE_NOTE = (
    "This subtrack prepares orderlies, environmental service (EVS) aides, utility workers and contracted cleaners for "
    "<strong>nonclinical</strong> support work in an adult hemodialysis unit. It does not authorize nursing care, "
    "machine operation, needle or catheter work, medicines, dialyzer reprocessing, water-treatment work or technical "
    "release of a station. Your employer&rsquo;s written task list, your supervisor and the nurse on duty decide what "
    "you may do. All people and cases are fictional."
)

# id, slug suffix, title, short title, day, hours (guided, practice), competencies, pathway note
MODULES = [
    ("01", "role-and-orientation", "Your Role in the Dialysis Unit", "Role and orientation", 1, (2, 1), ["S1"], "Both pathways"),
    ("02", "dignity-and-communication", "Dignity, Privacy and Clear Communication", "Dignity and communication", 1, (2, 1), ["S2"], "Both pathways"),
    ("03", "how-germs-travel", "How Germs and Blood Travel in a Dialysis Unit", "How germs travel", 2, (2, 1), ["S3"], "Both pathways"),
    ("04", "hand-hygiene-and-ppe", "Hand Hygiene and Protective Equipment", "Hand hygiene and PPE", 2, (2, 2), ["S3"], "Both pathways"),
    ("05", "aseptic-habits", "Aseptic Habits: Clean to Dirty, and Never Back", "Aseptic habits", 3, (2, 1), ["S3", "S4"], "Both pathways"),
    ("06", "products-and-zones", "Cleaning Products, Tools and Zones", "Products and zones", 3, (2, 2), ["S4"], "Both pathways"),
    ("07", "station-turnover", "Safe Turnover of a Dialysis Station", "Station turnover", 4, (2, 3), ["S1", "S4"], "Both; practice only if assigned"),
    ("08", "routine-terminal-cleaning-and-linen", "Routine and Terminal Cleaning, Restricted Areas and Linen", "Routine cleaning and linen", 4, (2, 2), ["S4", "S6"], "Both pathways"),
    ("09", "spills-sharps-and-exposures", "Blood Spills, Sharps and Exposure Response", "Spills, sharps and exposures", 5, (2, 2), ["S5"], "Both pathways"),
    ("10", "health-care-waste", "Health Care Waste: From Segregation to Storage", "Health care waste", 5, (2, 3), ["S6"], "Both pathways"),
    ("11", "patient-escort-and-transport", "Patient Escort and Transport", "Escort and transport", 6, (2, 2), ["S2", "S7"], "Orderly practice; EVS awareness"),
    ("12", "transfers-falls-and-your-back", "Transfers, Falls and Protecting Your Back", "Transfers and lifting", 6, (2, 2), ["S7", "S8"], "Orderly practice; EVS awareness"),
    ("13", "supplies-and-technical-boundaries", "Supplies, Equipment and Technical Boundaries", "Supplies and boundaries", 7, (2, 1), ["S1", "S8"], "Both pathways"),
    ("14", "emergencies-and-worker-safety", "Emergencies and Worker Safety", "Emergencies and safety", 7, (2, 2), ["S5", "S8"], "Both pathways"),
    ("15", "records-improvement-and-capstone", "Honest Records, Improvement and the Capstone", "Records and capstone", 8, (2, 3), ["S1", "S2", "S3", "S4", "S5", "S6", "S7", "S8"], "Both pathways"),
]

COMPETENCIES = [
    ("S1", "Explain the support role, name the supervisors, and decline clinical or technical work that is not on the written task list.", "Task-list teach-back; scope decisions in every station"),
    ("S2", "Protect dignity and privacy and report an observation clearly with Stop, Tell, Stay.", "Observed handoff; transport station"),
    ("S3", "Perform hand hygiene at the right moments, choose and remove protective equipment safely, and keep clean and dirty apart.", "Hand hygiene and doffing station with fluorescent feedback"),
    ("S4", "Read a product label and task card, achieve wet contact time, and complete environmental cleaning without claiming technical readiness.", "Station turnover with fluorescent-marker audit"),
    ("S5", "Make a spill or sharps hazard safe, and start the exposure response without delay.", "Spill and exposure simulation"),
    ("S6", "Segregate, contain, move and store waste and linen within the facility plan.", "Waste and linen station"),
    ("S7", "Support patient escort and transfers only within the nurse&rsquo;s plan, using equipment instead of solo lifting.", "Transport and transfer station (orderly pathway)"),
    ("S8", "Respond to emergencies, protect your own health, and keep truthful records that drive improvement.", "Emergency drill; accurate log; capstone"),
]

ABBR = {
    "EVS": ("environmental service", "the housekeeping and cleaning service of a health facility"),
    "IPC": ("infection prevention and control", ""),
    "SDS": ("safety data sheet", "the manufacturer&rsquo;s sheet on a chemical&rsquo;s hazards, first aid and spill response"),
    "PEP": ("post-exposure prophylaxis", "medicines given soon after an exposure to prevent infection"),
    "SOP": ("standard operating procedure", ""),
    "HCWM": ("health care waste management", ""),
    "DOLE": ("Department of Labor and Employment", "Philippines"),
    "DENR": ("Department of Environment and Natural Resources", "Philippines"),
    "NIOSH": ("National Institute for Occupational Safety and Health", "United States"),
    "OSHA": ("Occupational Safety and Health Administration", "United States"),
    "WHO": ("World Health Organization", ""),
    "NPC": ("National Privacy Commission", "Philippines"),
    "MRSA": ("methicillin-resistant Staphylococcus aureus", ""),
    "VRE": ("vancomycin-resistant enterococci", ""),
    "QI": ("quality improvement", ""),
    "RA": ("Republic Act", ""),
    "AED": ("automated external defibrillator", ""),
    "BP": ("blood pressure", ""),
    "OSH": ("occupational safety and health", ""),
    "RACE": ("Rescue, Alarm, Contain, Extinguish", "a common fire-response sequence"),
    "PASS": ("Pull, Aim, Squeeze, Sweep", "a common fire-extinguisher sequence"),
    "FIFO": ("first in, first out", "use the oldest stock first"),
    "OSCE": ("objective structured clinical examination", ""),
}

# PubMed-verified references: key -> PMID (metadata in data/dialysis-unit-support-staff/refs_pubmed_raw.json)
PUBMED_REFS = {
    "pittet2006": "17008173", "bond1981": "6111645", "thompson2009": "19124818", "mitchell2015": "26365827",
    "cook2006": "17699348", "waters2007": "17667392", "donskey2013": "23465603", "girou2008": "18662134",
    "rao2013": "23785746", "ray2017": "28462761", "carling2006": "16392086", "rutala2019": "31146858",
    "bouya2020": "32346521", "mitchell2019": "30858014", "schillie2013": "24352112", "tomas2015": "26457544",
    "kuhar2013": "23917901", "waters1993": "8339717", "pittet2000": "11073019", "fuller2011": "22080658",
    "schillie2018": "29939980", "lee2019": "30474130", "engst2005": "15764316", "west2019": "30201413",
    "doerrbecker2011": "22013220", "dumas2021": "33284160", "dumas2020": "31692020",
}

JOURNALS = {
    "Lancet Infect Dis": "The Lancet Infectious Diseases", "Lancet": "The Lancet",
    "Ann Intern Med": "Annals of Internal Medicine", "J Hosp Infect": "Journal of Hospital Infection",
    "Clin J Am Soc Nephrol": "Clinical Journal of the American Society of Nephrology", "Am J Nurs": "American Journal of Nursing",
    "Am J Infect Control": "American Journal of Infection Control", "Clin Infect Dis": "Clinical Infectious Diseases",
    "Nephrol Nurs J": "Nephrology Nursing Journal", "Infect Control Hosp Epidemiol": "Infection Control and Hospital Epidemiology",
    "Ann Glob Health": "Annals of Global Health", "MMWR Recomm Rep": "MMWR Recommendations and Reports",
    "JAMA Intern Med": "JAMA Internal Medicine", "Ergonomics": "Ergonomics", "Am J Ind Med": "American Journal of Industrial Medicine",
    "J Infect Dis": "The Journal of Infectious Diseases", "Curr Opin Allergy Clin Immunol": "Current Opinion in Allergy and Clinical Immunology",
}

TITLE_OVERRIDES = {
    "19124818": "Nonhospital health care-associated hepatitis B and C virus transmission: United States, 1998-2008",
    "26365827": "Risk of organism acquisition from prior room occupants: A systematic review and meta-analysis",
    "28462761": "A multicenter randomized trial to determine the effect of an environmental disinfection intervention on the incidence of healthcare-associated Clostridium difficile infection",
    "30858014": "An environmental cleaning bundle and health-care-associated infections in hospitals (REACH): A multicentre, randomised trial",
    "31146858": "Best practices for disinfection of noncritical environmental surfaces and equipment in health care facilities: A bundle approach",
    "32346521": "Global prevalence and device related causes of needle stick injuries among health care workers: A systematic review and meta-analysis",
    "23785746": "Outbreak of hepatitis C virus infections at an outpatient hemodialysis facility: The importance of infection control competencies",
    "18662134": "Determinant roles of environmental contamination and noncompliance with standard precautions in the risk of hepatitis C virus transmission in a hemodialysis unit",
    "24352112": "CDC guidance for evaluating health-care personnel for hepatitis B virus protection and for administering postexposure management",
    "17699348": "Falls and fall-related injuries in older dialysis patients",
    "16392086": "Improved cleaning of patient rooms using a new targeting method",
    "22080658": "&ldquo;The dirty hand in the latex glove&rdquo;: A study of hand hygiene compliance when gloves are worn",
    "31692020": "Occupational exposure to disinfectants and asthma incidence in U.S. nurses: A prospective cohort study",
    "29939980": "Prevention of hepatitis B virus infection in the United States: Recommendations of the Advisory Committee on Immunization Practices",
    "30474130": "Impact of California's safe patient handling legislation on musculoskeletal injury prevention among nurses",
}

RETRIEVED = "November 24, 2026"


def _link(url):
    return f'<a href="{url}">{url}</a>'


MANUAL_REFS = {
    "cdc2001": ("Centers for Disease Control and Prevention (CDC). (2001). Recommendations for preventing transmission of "
                "infections among chronic hemodialysis patients. <em>MMWR Recommendations and Reports</em>, <em>50</em>(RR-5), 1&ndash;43. "
                + _link("https://www.cdc.gov/mmwr/preview/mmwrhtml/rr5005a1.htm")),
    "who2009": ("World Health Organization (WHO). (2009). <em>WHO guidelines on hand hygiene in health care</em>. "
                + _link("https://www.who.int/publications/i/item/9789241597906")),
    "who2014": ("World Health Organization (WHO). (2014). <em>Safe management of wastes from health-care activities</em> (2nd ed.). "
                + _link("https://www.who.int/publications/i/item/9789241548564")),
    "doh_hcwm": ("Department of Health (DOH), Health Facility Development Bureau. (2020). <em>Health care waste management manual</em> "
                 "(4th ed.). " + _link("https://www.washinhcf.org/wp-content/uploads/2021/07/DOH-Health-Care-Waste-Management-Manual_4th-Edition_FINAL.pdf")),
    "cdc_station": ("Centers for Disease Control and Prevention (CDC). (2026). <em>Routine disinfection of the dialysis station: Checklist</em>. "
                    f"Retrieved {RETRIEVED}, from " + _link("https://www.cdc.gov/dialysis-safety/media/pdfs/env-checklist-508.pdf")),
    "cdc_envnotes": ("Centers for Disease Control and Prevention (CDC). (2026). <em>Environmental surface disinfection in dialysis "
                     f"facilities: Notes for clinical managers</em>. Retrieved {RETRIEVED}, from " + _link("https://www.cdc.gov/dialysis-safety/media/pdfs/env-notes-508.pdf")),
    "cdc_dart": ("Centers for Disease Control and Prevention (CDC). (2026). <em>Dialysis assessment and reporting tool (DART): Routine "
                 "environmental cleaning and disinfection</em>. " + _link("https://www.cdc.gov/dialysis-safety/media/pdfs/DART-EnvCleaningModule-form-508.pdf")),
    "cdc_b2": ("Centers for Disease Control and Prevention (CDC). (2026). <em>Appendix B2: Cleaning procedure summaries for specialized "
               f"patient areas</em>. Retrieved {RETRIEVED}, from " + _link("https://www.cdc.gov/healthcare-associated-infections/hcp/cleaning-global/appendix-b2.html")),
    "cdc_wallbox": ("Centers for Disease Control and Prevention (CDC). (2026). <em>Considerations for dialysis wall boxes and drains</em>. "
                    f"Retrieved {RETRIEVED}, from " + _link("https://www.cdc.gov/dialysis-safety/hcp/infection-control/wall-boxes-drains.html")),
    "osha1030": ("Occupational Safety and Health Administration (OSHA). (2026). <em>Bloodborne pathogens (29 CFR 1910.1030)</em>. "
                 f"Retrieved {RETRIEVED}, from " + _link("https://www.osha.gov/laws-regs/regulations/standardnumber/1910/1910.1030")),
    "psn2024": ("Philippine Society of Nephrology (PSN). (2024). <em>Guidelines for nephrologists in the operation of hemodialysis "
                "clinics in the Philippines</em> (3rd ed.). " + _link("https://psn.org.ph/wp-content/uploads/2024/03/HD-Guidelines-for-Nephrologists-Final-Revision-3.14.24.pdf")),
    "doh2012": ("Department of Health (DOH). (2012). <em>Administrative Order No. 2012-0001: New rules and regulations governing the "
                "licensure and regulation of dialysis facilities in the Philippines</em>. " + _link("https://hfsrb.doh.gov.ph/wp-content/uploads/2021/05/AO-2012-0001.pdf")),
    "phic2024_29": ("Philippine Health Insurance Corporation (PHIC). (2024). <em>PhilHealth Circular No. 2024-0029: Quality standards on "
                    "maintenance hemodialysis procedure as reference of the Corporation</em>. " + _link("https://www.philhealth.gov.ph/circulars/2024/PC2024-0029.pdf")),
    "ra10173": ("National Privacy Commission (NPC). (2012). <em>Republic Act No. 10173: Data Privacy Act of 2012</em>. "
                + _link("https://privacy.gov.ph/data-privacy-act/")),
    "npc2024": ("National Privacy Commission (NPC). (2024). <em>Reminder on sharing photos and videos containing personal data</em>. "
                + _link("https://privacy.gov.ph/reminder-on-sharing-photos-and-videos-containing-personal-data/")),
    "ra11058": ("Republic of the Philippines (RP). (2018). <em>Republic Act No. 11058: An act strengthening compliance with occupational "
                "safety and health standards</em>. " + _link("https://elibrary.judiciary.gov.ph/assets/dtSearch/dtSearch_system_files/dtisapi6.dll?DocId=20136&amp;Index=%2A2ceb34621b4a207c3a52af138f1e7bbf&amp;cmd=getdoc")),
    "ra9003": ("Republic of the Philippines (RP). (2001). <em>Republic Act No. 9003: Ecological Solid Waste Management Act of 2000</em>. "
               + _link("https://lawphil.net/statutes/repacts/ra2001/ra_9003_2001.html")),
    "ra6969": ("Republic of the Philippines (RP). (1990). <em>Republic Act No. 6969: Toxic Substances and Hazardous and Nuclear Wastes "
               "Control Act of 1990</em>. " + _link("https://lawphil.net/statutes/repacts/ra1990/ra_6969_1990.html")),
    "dao2005": ("Department of Environment and Natural Resources (DENR), &amp; Department of Health (DOH). (2005). <em>Joint DENR-DOH "
                "Administrative Order No. 02, Series of 2005: Policies and guidelines on effective and proper handling, collection, "
                "transport, treatment, storage and disposal of health care wastes</em>. " + _link("https://apidb.denr.gov.ph/infores/uploads/policy/2005/dao/JointDAO-2005-002.pdf")),
    "niosh1994": ("Waters, T. R., Putz-Anderson, V., &amp; Garg, A. (1994). <em>Applications manual for the revised NIOSH lifting equation</em> "
                  "(DHHS [NIOSH] Publication No. 94-110). National Institute for Occupational Safety and Health. "
                  + _link("https://www.cdc.gov/niosh/docs/94-110/")),
    "nkti2025": ("National Kidney and Transplant Institute (NKTI). (2025). <em>Minimum qualification requirements for outsourced "
                 "employees (IB No. 25-059)</em>. " + _link("https://nkti.gov.ph/wp-content/uploads/2025/01/IBNO25-059.pdf")),
}

HUB_REFS = ["cdc2001", "psn2024", "doh2012", "phic2024_29", "doh_hcwm", "who2009", "who2014", "ra11058", "ra10173",
            "pittet2006", "thompson2009", "girou2008", "mitchell2019", "cook2006", "waters2007", "kuhar2013", "nkti2025"]

# Hub: a fictional day in the unit (scenes drawn from the modules)
DAY_HTML = """
<p>Before the modules, here is what the job looks like. The day below is fictional, and so is everyone in it, but every moment happens in Philippine dialysis units every week. Each moment points to the module that prepares you for it. You will meet the same small team throughout: <strong>Ate Lorna</strong>, the EVS supervisor who has cleaned dialysis units for twenty years; <strong>Kuya Ramon</strong>, the senior orderly; and <strong>Nurse Jessa</strong>, the charge nurse of the San Isidro Dialysis Unit, an 18-station unit in a provincial hospital that runs three shifts a day.</p>
<div class="tc-sits">
<div class="tc-sit"><h3>5:40 a.m. &middot; before the first shift</h3><dl>
<dt>What happens</dt><dd>A new aide fills a spray bottle from a big jug of concentrate &ldquo;by feel,&rdquo; the way he did at his last job in a mall.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Read the label&rsquo;s dilution, measure with the marked jug, label the bottle with the product and date, and check its wet contact time. Module 6.</dd></dl></div>
<div class="tc-sit"><h3>10:05 a.m. &middot; shift change</h3><dl>
<dt>What happens</dt><dd>The next patient is waiting. The patient at Station 7 is still connected, with ten minutes left. Someone asks you to &ldquo;start wiping the chair so we save time.&rdquo;</dd>
<dt class="tc-sit-do">What you do</dt><dd>Wait for clinical clearance and for the patient to leave. Then clean, keep the surfaces wet for the full contact time, and hand over the station as &ldquo;environmental work complete.&rdquo; Module 7.</dd></dl></div>
<div class="tc-sit"><h3>11:30 a.m. &middot; waste room</h3><dl>
<dt>What happens</dt><dd>A yellow bag is heavy and lumpy at the bottom. Something pokes against the plastic.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Do not press, squeeze or reach in. Hold the bag by the neck away from your body, set it in a rigid bin, and report a sharp in the wrong container. Modules 9 and 10.</dd></dl></div>
<div class="tc-sit"><h3>2:50 p.m. &middot; after the session</h3><dl>
<dt>What happens</dt><dd>Mang Celso, 74, has just finished dialysis. Three liters of fluid were removed. He stands up quickly to go home and sways.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Help him sit, keep him safe, call the nurse, and stay. Move him only by wheelchair and only when the nurse says he is ready. Modules 11 and 12.</dd></dl></div>
<div class="tc-sit"><h3>4:15 p.m. &middot; isolation station</h3><dl>
<dt>What happens</dt><dd>You are cleaning the hepatitis B isolation station. The clean-supply cart from the main floor is parked just inside the door.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Use only the isolation station&rsquo;s dedicated tools, and tell the nurse the cart must leave without anything being taken from it. Module 5.</dd></dl></div>
<div class="tc-sit"><h3>7:45 p.m. &middot; end of day</h3><dl>
<dt>What happens</dt><dd>You missed the wall-mounted handrub dispenser at Station 3 during terminal cleaning. Nobody would ever know.</dd>
<dt class="tc-sit-do">What you do</dt><dd>Go back, clean it, and record the correction truthfully. Honest records are what make the next audit useful. Module 15.</dd></dl></div>
</div>
<p>None of these moments asks you to make a clinical decision. Every one depends on you noticing, doing your own task exactly, and telling the right person in time. That is what this subtrack trains.</p>
"""
