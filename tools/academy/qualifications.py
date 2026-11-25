# -*- coding: utf-8 -*-
"""Philippine qualifications for each Renal Care Academy role (summary, not legal advice).

Sources (checked Nov 2026):
  DOH  = DOH Administrative Order No. 2012-0001, Sec. V.B.2.a (licensure of dialysis facilities)
  PSN  = Philippine Society of Nephrology, Guidelines for nephrologists in the operation of hemodialysis clinics, 3rd ed. (2024), Sec. III.A
  RND  = Republic Act No. 10862, Nutrition and Dietetics Law of 2016
Where DOH and PSN differ, both are shown; the stricter one is usually what an inspector or PSN chapter will ask for.
Used by apply_taxonomy.py (course-home boxes) and kept in step with the table on academy/index.html.
"""
NA = "No specific requirement in the DOH or PSN hemodialysis rules."
QUAL = {
 "nephrology-nursing": ("Hemodialysis Nurse", [
   "PRC-licensed nurse (R.A. 9173). <span class=q-src>DOH, PSN</span>",
   "Certificate of training in nursing care of renal dialysis patients; PSN cites a structured program of 3 months or more where needed. <span class=q-src>DOH, PSN</span>",
   "Current BLS (DOH); PSN asks for current BLS and ACLS from a DOH-accredited provider. At least one nurse per shift with updated ACLS. <span class=q-src>DOH, PSN</span>",
   "Ratio: no more than 1 nurse to 4 stations per shift; PSN allows 1:6 when a nursing assistant is present. <span class=q-src>DOH, PSN</span>"]),
 "peritoneal-dialysis-nurse": ("Peritoneal Dialysis Nurse", [
   "Licensed nurse with dialysis nursing training, as for a hemodialysis nurse. " + NA.replace("hemodialysis rules", "hemodialysis rules for a separate PD nurse role") + " Follow your PD program&rsquo;s credentialing."]),
 "transplant-nurse": ("Kidney Transplant Nurse", [
   "Licensed nurse (R.A. 9173). The Department of Health (DOH) and Philippine Society of Nephrology (PSN) dialysis rules do not cover transplant nursing; follow your transplant center&rsquo;s credentialing."]),
 "dialysis-head-nurse": ("Head Nurse", [
   "PRC-licensed nurse (R.A. 9173). <span class=q-src>PSN</span>",
   "Certificate from a structured renal dialysis nursing program of 3 months or more, where needed. <span class=q-src>PSN</span>",
   "Current BLS/ACLS from a DOH-accredited provider. <span class=q-src>PSN</span>",
   "At least 2 years&rsquo; experience as a dialysis nurse. <span class=q-src>PSN</span>",
   "DOH AO 2012-0001 does not define the head nurse role separately."]),
 "special-dialysis-nurse-roles": ("Special Dialysis Nurse Roles (portfolio nurse)", [
   "A hemodialysis nurse who meets the hemodialysis nurse requirements: PRC license (R.A. 9173), dialysis nursing training certificate, current BLS, ACLS where assigned. <span class=q-src>DOH, PSN</span>",
   "The DOH and PSN rules name facility duties (patient education, transplant linkage, registry and records, QAPI) but do not define any of the twelve portfolios as a separate post; the employer assigns the portfolio in writing.",
   "Portfolio work is added to safe licensed staffing: DOH sets no more than 1 nurse to 4 stations; PSN describes 1:4 patients, or 1:6 with a nursing assistant."]),
 "charge-nurse": ("Charge Nurse", [
   "Not defined in the DOH or PSN rules. In practice, a dialysis nurse who meets the hemodialysis nurse requirements, with current ACLS, designated by the head nurse for the shift."]),
 "dialysis-charge-nurse": ("Charge Nurse", [
   "Not defined separately in the DOH or PSN hemodialysis rules. In practice, a dialysis nurse who meets the hemodialysis nurse requirements: PRC license (R.A. 9173) and training in nursing care of renal dialysis patients. <span class=q-src>DOH, PSN</span>",
   "Current Basic Life Support (BLS); DOH requires at least one nurse trained in Advanced Cardiovascular Life Support (ACLS) per shift, and the charge nurse is often that nurse. <span class=q-src>DOH, PSN</span>",
   "Designated by the head nurse or employer for the shift; completing a study series is not an appointment."]),
 "dialysis-clinical-head": ("Dialysis Clinical Head", [
   "PRC-licensed physician; preferably a PSN board-certified nephrologist with a PSN Certificate of Attestation and PSN or chapter endorsement. <span class=q-src>DOH, PSN</span>",
   "If none is available, in order: board-eligible nephrologist; board-certified, then board-eligible internist or pediatrician with HDC experience (3 months under DOH, 6 months under PSN); general practitioner with 6 months&rsquo; experience. <span class=q-src>DOH, PSN</span>",
   "PSN limits: a non-board-certified nephrologist may serve up to 3 years; a non-nephrologist may head only one HDC, for one year. <span class=q-src>PSN</span>",
   "Visits at least once a week; heads no more than 3 HDCs (PSN allows up to 5 where nephrologists are scarce). <span class=q-src>DOH, PSN</span>",
   "PSN post-graduate course certificate for clinical heads, required from August 1, 2025, with an exemption for 10 years&rsquo; experience. <span class=q-src>PSN</span>"]),
 "attending-nephrologist": ("Attending Nephrologist", [
   "PRC-licensed, with nephrology training from a PSN-accredited or recognized institution. <span class=q-src>PSN</span>",
   "Practices in the area and is easily reached by the HDC; submits CV, updated PhilHealth accreditation, PRC license, and PSN or chapter endorsement. <span class=q-src>PSN</span>"]),
 "vascular-surgeon": ("Vascular Surgeon", [
   "PRC-licensed physician with surgical training; specialty credentials verified by the hospital that appoints the surgeon. No Department of Health (DOH) or Philippine Society of Nephrology (PSN) rule defines a separate vascular surgeon post for a dialysis unit. <span class=q-src>DOH, PSN</span>",
   "PSN 2024 &sect;1.2 b3 asks the attending nephrologist to coordinate access with a vascular surgeon or trained general surgeon; it does not credential the surgeon. <span class=q-src>PSN</span>",
   "Privileges for each open, catheter and endovascular procedure come from the operating hospital&rsquo;s credentialing committee; trainees work under documented supervision.",
   "PATACSI lists accredited TCVS training programs, including a post-residency vascular pathway; confirm board routes with the relevant board. Completing this track grants no privileges or certification."]),
 "physician-on-duty": ("Physician-on-Duty", [
   "PRC-licensed, in order of preference: nephrologist (board-certified, then board-eligible); internist or pediatrician with at least 3 months&rsquo; HDC experience; nephrology fellow or qualifying resident; general or family practitioner with at least 6 months&rsquo; experience. <span class=q-src>DOH, PSN</span>",
   "Current ACLS from a DOH-accredited provider, and a PSN-conducted or accredited post-graduate course for PODs. <span class=q-src>DOH, PSN</span>",
   "Present during all operating hours. Ratio no more than 1:15 stations (DOH); PSN allows up to 1:20 where PODs are scarce. <span class=q-src>DOH, PSN</span>"]),
 "dialyzer-reprocessing-technician": ("Dialyzer Reprocessing Technician", [
   "DOH lists daily reprocessor calibration, collection, reprocessing, acceptance testing, labeling, reuse records and storage among dialysis technician duties. <span class=q-src>DOH</span>",
   "High school graduate who has completed a structured technician training program of 3 months or longer. <span class=q-src>PSN</span>",
   "No separate PRC license. Release authority is granted by the facility after an observed practical assessment on its own reprocessor.",
   "Reuse must follow the unit&rsquo;s approved program; PhilHealth cites up to 5 total uses per dialyzer and TCV of at least 80%. <span class=q-src>PhilHealth</span>"]),
 "hemodialysis-technician": ("Dialysis Technician", [
   "At least a high school graduate, with structured dialysis technician training of 3 months or more where needed (renal function, machines, water treatment, infection control, emergency roles). <span class=q-src>PSN</span>",
   "Works under the supervision of the physician and nurse; assists in emergencies. DOH lists duties but no qualifications. <span class=q-src>DOH, PSN</span>"]),
 "water-treatment-technician": ("Water Treatment Technician", [
   NA + " Water duties (daily RO maintenance, monthly microbiology, chemical analysis every 6 months at DOH-accredited laboratories) fall to the dialysis technician. <span class=q-src>PSN</span>"]),
 "dialysis-biomedical-technician": ("Biomedical Equipment Technician", [
   NA + " Follow the manufacturer&rsquo;s service training and your unit&rsquo;s service agreement."]),
 "renal-dietitian": ("Renal Dietitian", [
   "Must be a registered and licensed Nutritionist-Dietitian (PRC and Board of Nutrition and Dietetics), which requires a BS in Nutrition and Dietetics and the licensure examination. <span class=q-src>RA 10862</span>",
   "The DOH and PSN dialysis rules do not list a dietitian position."]),
 "medical-records-officer": ("Medical Records Officer/Custodian", [
   "A designated staff member who keeps the records and serves as the Philippine Renal Disease Registry (PRDR) coordinator. <span class=q-src>DOH</span>",
   "Training in the International Classification of Diseases, 10th Revision (ICD-10), basic records management, and hospital health information management as required by DOH. <span class=q-src>PSN</span>"]),
 "dialysis-nurse-assistant": ("Dialysis Nurse Assistant / Patient Care Assistant (PCA)", [
   "PSN describes nursing assistants as BS Nursing graduates awaiting registration, BS Nursing undergraduates who completed at least second year, or BS Midwifery graduates, working under supervision. <span class=q-src>PSN</span>",
   "Not a registered nurse and not counted as one; a nursing degree without PRC registration does not authorize nursing practice. <span class=q-src>DOH, PSN</span>",
   "No national assistant license or TESDA equivalence; scope is the employer&rsquo;s written job description plus the tasks signed off under RN supervision.",
   "Ratio: DOH sets no more than 1 nurse to 4 stations; PSN discusses 1:6 patients when an assistant is present. Confirm with DOH licensing before relying on any exception. <span class=q-src>DOH, PSN</span>"]),
 "occupational-physical-therapist": ("Occupational and Physical Therapist", [
   "Physical therapists: PRC-registered under RA 5680; treatment requires a physician&rsquo;s prescription (Sec. 12). <span class=q-src>RA 5680</span>",
   "Occupational therapists: PRC-registered under RA 11241, a separate profession with its own scope; works on referral. <span class=q-src>RA 11241</span>",
   "The DOH and PSN dialysis rules list no renal OT or PT position, staffing ratio or renal therapist certificate; scope is the license, the referral and employer privileges. <span class=q-src>DOH, PSN</span>"]),
 "dialysis-unit-support-staff": ("Dialysis Unit Support Staff (orderly, environmental services aide)", [
   NA + " PSN groups housekeeping with the other nonmedical staff and expects written unit policies on infection control, waste, emergencies, and the environment. <span class=q-src>PSN</span>",
   "Your scope is your employer&rsquo;s written task list plus the tasks you have been trained and signed off on. <span class=q-src>DOH, PSN</span>"]),
 "dialysis-unit-manager": ("Unit Operations Manager/Unit Manager", [
   "At least 2 years of proven success in operations management, or as head of a unit or department with at least 5 employees. <span class=q-src>PSN</span>",
   "Bachelor&rsquo;s degree in operations management, business administration, or a medically related 4-year course; master&rsquo;s in hospital or business administration preferred. <span class=q-src>PSN</span>",
   "A separate manager is required for non-hospital HDCs with more than 15 stations; smaller units may combine the role. <span class=q-src>PSN</span>"]),
 "philhealth-claims": ("PhilHealth Liaison/Claims Officer", [
   "Listed among administrative staff (PhilHealth officer or clerk); no qualifications are specified. <span class=q-src>DOH, PSN</span>"]),
}
SOURCES = ("Sources: DOH Administrative Order No. 2012-0001, Sec. V.B.2.a; Philippine Society of Nephrology (2024), "
           "<em>Guidelines for nephrologists in the operation of hemodialysis clinics</em>, Sec. III.A; Republic Act No. 10862. "
           "A summary for orientation, not legal advice: check the current issuances, and your unit&rsquo;s license and PhilHealth accreditation.")
