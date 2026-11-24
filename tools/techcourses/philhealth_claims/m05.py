# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 05: The Claim Packet, eSOA, Codes, and the Shift to DRG (includes section 05B of the v1.1 blueprint)."""

MODULE = {
    "image_alt": "An open tabbed claim folder at the center of a desk, surrounded by five source documents joined to it by fine threads.",
    "objectives": [
        "Build an indexed packet manifest with each item&rsquo;s applicability, source, owner, version, and status.",
        "Check that sessions, dates, signatures, and identifiers agree across Claim Form 2 (CF2), CF4, the agreement forms, and the bill.",
        "Explain why the statement of account must be XML and what happens to a PDF.",
        "Tell an International Classification of Diseases, 10th Revision (ICD-10) diagnosis code from a Relative Value Scale (RVS) procedure code, and avoid the US-code trap.",
        "Explain in plain words how case rates differ from diagnosis-related groups, and what the CF5 rule changes today.",
    ],
    "big": """
{{plain:A claim packet is a folder in which every page points back to where it came from. A reviewer should be able to pick any field, the patient&rsquo;s name, a session date, a total, and follow a thread to the one record it was copied from.}}
<p>The picture has a limit: threads can be copied, but they cannot be invented. If a source is missing, the right response is to hold the packet and recover the source, not to fill the field. That is why a missing per-session agreement form stops a whole claim, and why a code chosen to fit a package, instead of the documentation, is a misrepresentation.</p>
{{fig:pc_trace}}
{{cards:Key terms for this module|Manifest::The packet&rsquo;s table of contents: each item, whether it applies, its source, owner, version, and status.|CF2::Claim Form 2, with provider and service information, the codes, and hemodialysis consumption in Part III.|CF4::Claim Form 4, the clinical information form, where required.|eSOA::Electronic statement of account, the bill sent as XML data.|ICD-10::The diagnosis code set PhilHealth uses, with Philippine modifications.|RVS::Relative Value Scale, PhilHealth&rsquo;s procedure codes.}}
""",
    "case": {"title": "Two sessions, one agreement, and a PDF", "html": """
<p>The claim for Mr. Ramil Aquino (fictional, SIM-05) groups two completed sessions. The manifest shows one signed agreement form; the second is unsigned. The CF4 end date is one day later than the last session on CF2. The billing system produced only a PDF statement.</p>
<p>A new clerk has also typed &ldquo;N18.6 &mdash; end stage renal disease&rdquo; into the draft CF2, copied from a free coding website, because it &ldquo;sounded more correct&rdquo; for a patient on dialysis.</p>
""", "questions": ["What three corrections does this packet need, and who owns each?",
                  "Can the second agreement form be signed today with the session date?",
                  "What is wrong with N18.6, and what does the clerk need to learn?"]},
    "sections": [
        ("manifest", "The manifest", "Building the packet", """
<p>List every item with its applicability, source, owner, version, and status. Check current official forms and your approved submission requirements. CF1 or the Claim Signature Form (CSF) and the PBEF support membership, eligibility, and attestations as your workflow prescribes. CF2 captures provider and service information, including hemodialysis consumption in Part III. CF4 records clinical information where required.[[pc_pc2019_0002]]</p>
<p>For repetitive procedures, the general CF4 guidance allows one CF4 for a grouped filing, with dates consistent across CF4 and CF2; confirm the current package rules and exclusions first. Grouping never removes the per-session agreement form: Circular 2024-0023 calls for one for each treatment session.[[pc_pc2024_0023]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Item</th><th>Applies?</th><th>Source</th><th>Owner</th><th>Version or date</th><th>Status</th></tr></thead>
<tbody>
<tr><td>CF1 or CSF</td><td>Yes</td><td>Intake record</td><td>Clerk</td><td>Current form</td><td>Complete</td></tr>
<tr><td>CF2 (Part III consumption)</td><td>Yes</td><td>Session ledger</td><td>Claims officer</td><td>Current form</td><td>Check dates</td></tr>
<tr><td>CF4</td><td>As required</td><td>Clinical record</td><td>Clinician or coder</td><td>Current form</td><td>Date conflict</td></tr>
<tr><td>Agreement form, session 1</td><td>Yes</td><td>Signed at session</td><td>Liaison or nurse</td><td>Annex A</td><td>Signed</td></tr>
<tr><td>Agreement form, session 2</td><td>Yes</td><td>Signed at session</td><td>Liaison or nurse</td><td>Annex A</td><td>Unsigned: hold</td></tr>
<tr><td>eSOA</td><td>Yes</td><td>Billing system</td><td>Billing</td><td>XML</td><td>PDF only: hold</td></tr>
</tbody></table></div>
"""),
        ("esoa", "The eSOA", "Why the bill must be XML", """
<p>Structured data lets PhilHealth check claims automatically, field by field. The electronic statement of account has been required for case-rate claims with admission dates from May 31, 2025, and under eClaims 3.0 it must be XML.[[pc_pc2023_0026]][[pc_pa2025_0040]] PhilHealth Advisory 2026-0022 states that a PDF statement of account is no longer accepted and the claim is returned to the facility for completion.[[pc_pa2026_0022]]</p>
<p>The package rate and the statement total measure different things: the rate is what PhilHealth pays per session; the statement itemizes what the session cost. Confirm that the patient, dates, totals, deductions, and approved charges in the XML match the authoritative billing record, and review any line-level difference with billing. A PDF may still help local review; it is not the submission.</p>
{{key:Never backdate. A record signed today carries today&rsquo;s date, and the correction trail shows when and by whom it was completed.}}
"""),
        ("codes", "Two code books", "Diagnosis codes and procedure codes", """
<p>PhilHealth identifies medical conditions with the International Classification of Diseases, 10th Revision (ICD-10), and procedures with the Relative Value Scale (RVS).[[pc_pc35_2013]] On a maintenance hemodialysis claim, the diagnosis is ICD-10 N18.5 (chronic kidney disease, stage 5) and the procedure is RVS 90935 (hemodialysis). They sit in different fields and are never interchangeable.</p>
<p><strong>The US-code trap.</strong> Many free coding websites use the United States version, ICD-10-CM, in which stage 5 disease that needs chronic dialysis is moved out of N18.5 into N18.6, &ldquo;end stage renal disease.&rdquo; PhilHealth&rsquo;s code set works the other way. PhilHealth deleted the old N18.0 &ldquo;end stage renal disease&rdquo; in the Philippine modifications, and end-stage kidney disease, including on dialysis, is coded N18.5.[[pc_pc30_2015]] PhilHealth applies the updated ICD-10 list to claims, and claims with outdated codes are returned to the facility.[[pc_pc2017_0019]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Code</th><th>Meaning</th><th>Where you see it</th></tr></thead>
<tbody>
<tr><td>N18.5</td><td>Chronic kidney disease, stage 5, including end-stage kidney disease on dialysis</td><td>Every maintenance and emergency stage 5 hemodialysis claim</td></tr>
<tr><td>90935 (RVS)</td><td>Hemodialysis procedure</td><td>The procedure field of the hemodialysis claim</td></tr>
<tr><td>N17.x</td><td>Acute kidney failure (subtypes .0, .1, .2, .8, .9)</td><td>Hospital acute kidney injury claims (Module 10)</td></tr>
<tr><td>Z49.x</td><td>Care involving dialysis</td><td>Encounter coding in some hospital records; confirm local use</td></tr>
<tr><td>Z99.2</td><td>Dependence on renal dialysis</td><td>A status code on admissions of dialysis patients</td></tr>
<tr><td>Z94.0</td><td>Kidney transplant status</td><td>Transplant recipients (Module 10)</td></tr>
<tr><td>E11.2 / I12 family</td><td>Diabetes with kidney complications; hypertensive kidney disease</td><td>Common causes listed beside N18.5, sequenced by the coder</td></tr>
</tbody></table></div>
{{call:Take codes only from the governing circular, your facility&rsquo;s approved code list, or the coder. Never copy a code from a US website or a vendor&rsquo;s free-text search, and never choose a code to fit a package.}}
"""),
        ("drg", "Case rates and DRG", "From case rates to diagnosis-related groups", """
<p>Under All Case Rates, PhilHealth pays a fixed amount for each specific illness or procedure, covering facility and professional fees.[[pc_pc31_2013]] Two patients with the same case-rate code receive the same payment, even if one was far sicker. That is simple and predictable, but it can underpay complex cases and overpay simple ones.</p>
<p>PhilHealth is moving its <em>inpatient</em> payment from case rates to Philippine diagnosis-related groups (DRG). A DRG system sorts hospital cases into groups by the principal diagnosis, the other diagnoses, the procedures, and factors such as age, sex, and length of stay. A program called a grouper assigns each case to a group, and each group carries a relative weight. In DRG systems generally, payment is a base rate multiplied by the group&rsquo;s weight, and complications or other diagnoses can move a case into a heavier group. PhilHealth adopted its grouping algorithm from the Thai DRG.[[pc_pc2026_0012]][[pc_drg_manual]]</p>
{{fig:pc_drg}}
<div class="table-wrap"><table>
<thead><tr><th>Setting</th><th>What changes now</th><th>What stays the same</th></tr></thead>
<tbody>
<tr><td>Freestanding hemodialysis center</td><td>Nothing in outpatient filing. The liaison should know that a patient&rsquo;s hospital confinement claim now needs a CF5, filed by the hospital.</td><td>Per-session package, CF2 with N18.5 and 90935, eSOA XML, per-session agreement form</td></tr>
<tr><td>Hospital unit, outpatient sessions</td><td>Same as freestanding</td><td>Same as freestanding</td></tr>
<tr><td>Hospital, inpatient cases</td><td>CF5 attached for every discharge from August 1, 2026; complete secondary diagnoses matter more</td><td>An emergency stage 5 session still counts toward the 156 and is coded per the circular</td></tr>
</tbody></table></div>
<p>Where it stands on November 24, 2026: hospitals are still paid by case rates, while their codes run through the grouper in parallel (shadow billing).[[pc_pc2026_0012]] For infirmaries and Level 1 to 3 hospitals, CF5 is a mandatory attachment for every patient discharged from August 1, 2026, and claims without a valid CF5 are not accepted.[[pc_pa2026_0036]] CF5 and the eSOA together supply the clinical and cost data used to build the group weights.[[pc_pa2026_0010]] The outpatient hemodialysis package is still paid per session; treat any change to it as unannounced until PhilHealth issues a circular.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Three corrections.</strong> The clinician or coder verifies the CF4 end date against the source record and corrects it if needed. The authorized owner resolves the unsigned agreement form for session 2. Billing produces and validates the eSOA as XML from the approved system. Then compare the corrected packet with the session ledger before release.</p>
<p><strong>No backdating.</strong> If the agreement was not signed at the session, it is completed now with today&rsquo;s date and a note explaining the late completion, following your SOP. A form signed today and dated last week misrepresents the record.</p>
<p><strong>N18.6.</strong> It belongs to the US ICD-10-CM. In PhilHealth&rsquo;s code set, end-stage kidney disease on dialysis is N18.5. Hold the draft, route the code to the coder, log the error for training, and take the website off the desk&rsquo;s reference list.</p>
"""],
    "skills": {"title": "Packet manifest and code check",
               "intro": "Build the manifest for a fictional two-session claim with three planted defects, including one US code.",
               "items": [
                   ("Lists each item with applicability, source, owner, version, and status.", False),
                   ("Requires one agreement form per session, even in a grouped claim.", True),
                   ("Compares sessions, dates, signatures, and identifiers across CF2, CF4, agreements, and the bill.", False),
                   ("Rejects a PDF as the eSOA and requests XML from the approved system.", False),
                   ("Distinguishes the ICD-10 diagnosis code from the RVS procedure code.", False),
                   ("Identifies N18.6 as a US code and routes the correction to the coder.", True),
                   ("Explains case rates, DRG, and the CF5 rule in two plain sentences each.", False),
               ],
               "placement": "Audit three released packets at your unit for traceability and report any field you could not trace."},
    "quiz": [
        ("Does grouping two sessions remove the second agreement form?",
         ["Yes", "No; each treatment session has its own agreement form", "Only for HDF", "Only if CF4 is attached"], 1,
         "The circular requires one per session."),
        ("Can a PDF serve as the eSOA under eClaims 3.0?",
         ["Yes", "No; submit XML from the approved system. A PDF may support local review", "Only for small claims", "Only in December"], 1,
         "PhilHealth returns claims with a PDF statement."),
        ("Who corrects a CF4 date conflict?",
         ["The clerk", "The clinical author or coder, from the source record", "PhilHealth", "The patient"], 1,
         "Claims staff route it."),
        ("An agreement form for session 2 is unsigned. Can someone sign it today with last week&rsquo;s date?",
         ["Yes", "No; complete it with today&rsquo;s date through the authorized owner and SOP", "Only the clerk", "Only if PhilHealth asks"], 1,
         "No backdating."),
        ("Is 90935 a diagnosis code?",
         ["Yes", "No; it is an RVS procedure code. The diagnosis on a stage 5 HD claim is N18.5", "It is both", "It is a PIN"], 1,
         "Two code books, two fields."),
        ("Where is end-stage kidney disease on dialysis coded in PhilHealth&rsquo;s code set?",
         ["N18.6", "N18.5", "N18.0", "N17.9"], 1,
         "PhilHealth deleted N18.0; N18.6 is a US code."),
        ("A clerk copies N18.6 from a free website. What do you do?",
         ["Keep it", "Hold the draft, route the code to the coder, and log the error", "Change it to N18.0", "Submit and see"], 1,
         "Take codes only from approved sources."),
        ("Under case rates, do two patients with the same code but different severity get different payments?",
         ["Yes", "No; the rate is fixed per case-rate code", "Only if one is older", "Only for dialysis"], 1,
         "That is the main limit of case rates."),
        ("Under DRG, which part of the coding can move a case into a heavier group?",
         ["The patient&rsquo;s PIN", "Complications and other diagnoses recorded as secondary diagnoses", "The filing date", "The hospital&rsquo;s name"], 1,
         "The full record decides the group."),
        ("During shadow billing, what decides what the hospital is paid?",
         ["DRG weights", "Case rates; DRG grouping runs in parallel for testing", "The patient", "The vendor"], 1,
         "Grouping is tested, not yet paid."),
        ("Does the August 1, 2026 CF5 rule change how a freestanding center files outpatient HD?",
         ["Yes", "No; CF5 applies to inpatient discharges", "Only for transfers", "Only for HDF"], 1,
         "The outpatient package is unchanged."),
        ("What does the eSOA prove that the package rate does not?",
         ["The patient&rsquo;s eligibility", "The itemized financial record of that claim", "The diagnosis", "The PDD status"], 1,
         "Rate and statement measure different things."),
        ("Name one field to compare across CF2, CF4, the agreement forms, and the eSOA.",
         ["The weather", "Service dates", "The clerk&rsquo;s name", "The vendor"], 1,
         "Also identity and session count."),
        ("A hospital asks your center to add a secondary diagnosis to its inpatient claim. What do you do?",
         ["Add it", "Decline; each facility&rsquo;s coder codes its own claim from its own documentation", "Add it if the patient agrees", "Ask PhilHealth to add it"], 1,
         "Share only verified facts, through the liaison."),
        ("Which program assigns a hospital case to a DRG?",
         ["The eSOA", "The grouper", "The PDD", "The agreement form"], 1,
         "PhilHealth adopted the Thai grouping algorithm."),
    ],
    "terms": [("Manifest", "The packet&rsquo;s table of contents with source, owner, version, and status."),
              ("CF2", "Claim Form 2."),
              ("CF4", "Claim Form 4."),
              ("CF5", "Claim Form 5, for inpatient DRG shadow billing."),
              ("eSOA", "Electronic statement of account, sent as XML."),
              ("ICD-10", "The diagnosis code set PhilHealth uses."),
              ("RVS", "Relative Value Scale, the procedure codes."),
              ("DRG", "Diagnosis-related group."),
              ("Grouper", "The program that assigns a hospital case to a DRG."),
              ("Shadow billing", "Filing under case rates while DRG grouping is tested in parallel.")],
    "readings": [("philhealth-acr-to-drg.html", "How PhilHealth is moving from case rates to diagnosis-related groups.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
