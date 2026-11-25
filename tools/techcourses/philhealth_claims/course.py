# -*- coding: utf-8 -*-
"""PhilHealth Liaison, Claims Officer and Clerk track: course definition in the POD/DCH package schema.
Built from Dr. Rivero's handoff (Philhealth Claims/philhealth-academy-claude-handoff, files 01-07; 04 is the v1.1
upgrade layer, signed November 24, 2026). Every case, name, identifier, and record in the series is fictional.
Policy figures were checked against PhilHealth's own circulars and advisories on November 24, 2026."""

HUB = "philhealth-claims"
_HB = "Illustrated vignette, bright natural light, Filipino staff and families, dialysis unit, no text in image. "

COURSE = {
    "title": "PhilHealth Liaison, Claims Officer and Clerk",
    "short": "PhilHealth Claims",
    "hub_slug": HUB,
    "label": "Training track for the staff who keep dialysis claims honest, complete, and on time",
    "tag": "Administrative Staff",
    "icon": "🧾",
    "no_branch": True,
    "audience": ("PhilHealth liaisons, claims officers, and claims clerks in freestanding dialysis centers and hospital dialysis units "
                 "&middot; billing and finance staff &middot; head nurses and unit managers who supervise the claims desk"),
    "audience_type": "Dialysis claims staff",
    "level": "Office staff with no clinical background; every clinical idea is explained in plain language",
    "review_date": "2026-11-26",
    "draw": 8,
    "mastery": "7 of 8",
    "keywords": ("PhilHealth claims training, dialysis claims clerk, PhilHealth liaison, claims officer Philippines, PhilHealth hemodialysis "
                 "156 sessions, PhilHealth Dialysis Database PDD, eClaims 3.0, eSOA XML, PhilHealth returned claim, PhilHealth denied claim, "
                 "hemodialysis benefits agreement form, CF5 shadow billing, PhilHealth DRG, ICD-10 N18.5, Data Privacy Act dialysis, "
                 "HMO claims dialysis, HMO letter of authorization LOA, HMO accreditation dialysis center, HMO collections aging, "
                 "HMO disallowance appeal, Insurance Commission HMO complaint"),
    "page_title": "PhilHealth Liaison, Claims Officer and Clerk: A Training Track",
    "desc": ("A free training track for the staff who prepare, file, and follow up PhilHealth claims in dialysis units: roles and "
             "authority, eligibility and the dialysis database, the hemodialysis benefit and patient charges, session evidence and "
             "codes, the claim packet and eSOA, eClaims 3.0 and deadlines, returns and denials, reconciliation, privacy, renal "
             "pathways, and HMO claims: accreditation, letters of authorization, coordination with PhilHealth, disallowances, and "
             "collections. Plain language, illustrated figures, cases, calculators, and a capstone."),
    "h1": "PhilHealth <em>Claims</em> for Dialysis Units",
    "sub": ("A training track for PhilHealth liaisons, claims officers, and clerks. Learn why every claim follows the care, how to build "
            "one that will be paid, and what to do when it is not, for PhilHealth and for every HMO your unit is accredited with."),
    "disclaimer": ("Educational material for dialysis claims staff. Completing it is an Academy learning record only. It is not a PhilHealth "
                   "certification, it does not grant system access or signing authority, and it does not replace current PhilHealth "
                   "issuances, written guidance from your PhilHealth Regional Office, or your facility&rsquo;s approved procedures."),
    "scope_note": ("This module is study material for dialysis claims staff. PhilHealth rules change by circular and advisory: confirm every "
                   "rate, date, and form against the current issuance and your PhilHealth Regional Office before you rely on it. Clinical "
                   "decisions belong to the treating team. Every case, name, and identifier here is fictional; never use real patient data "
                   "in training."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Claims staff",
    "branch_blurb": ("For PhilHealth liaisons, claims officers, and clerks: eligibility and the dialysis database, the hemodialysis benefit, "
                     "session evidence and codes, eClaims, returns and denials, reconciliation, privacy, the shift to DRG, and HMO claims and collections."),
    "academy_meta": "13 modules &middot; a capstone practicum &middot; 7 calculators",
    "hero_alt": "A young claims clerk shows a printed session log to an older woman at the front desk, with the dialysis treatment floor visible behind them.",
    "hero_file": f"{HUB}-vignette-hero",
    "start_h2": "The claim follows the care",
    "start_html": """
<p>A patient with kidney failure on hemodialysis (HD) depends on a machine for the work the kidneys no longer do. Three times a week, for about four hours, blood is cleaned of wastes, potassium, acid, and the fluid the patient drank since the last session. Between sessions, all of it builds up again. Nothing clears it until the next treatment.</p>
<p>PhilHealth pays for that treatment through a fixed package for each session. The people who make that payment happen are rarely clinicians: the clerk who checks identity and the dialysis database, the claims officer who builds and files the claim, and the liaison who explains the benefit to the family and talks to PhilHealth when something goes wrong. Their work keeps the unit open and the patient&rsquo;s bill fair. It also carries one rule that this whole track is built on: <strong>a claim problem is never a reason to delay a treatment.</strong></p>
{{fig:pc_why}}
{{cards:What this track will help you do|Know who decides::Route every question to its owner and leave a traceable handoff.|Get eligibility right::Verify identity, eligibility, and dialysis-database registration as separate checks.|Keep the bill fair::Explain the benefit in plain words and catch a covered item charged to a patient.|Build a claim that will be paid::Count sessions from the nurse&rsquo;s record, assemble a traceable packet, and file it once.|Handle what comes back::Tell a return from a denial, keep the clock, and match every peso of the remittance.|Protect patients and the unit::Handle dialysis data safely and route each kidney problem to the right benefit.|Collect from every HMO::Keep a payer profile for each HMO, bill each peso once, appeal disallowances, and age every receivable.}}
{{fig:pc_lifecycle}}
<p>Each module starts from why a rule exists, works through a fictional case, and ends with a skills checklist and a self-assessment. Seven calculators handle the arithmetic: filing deadlines, the 156-session ledger, remittance and professional-fee splits, claims performance rates, bill checking, the PhilHealth&ndash;HMO&ndash;patient split, and HMO aging.</p>
""",
    "exam_draw": 40,
    "is_not": ("It is a training track written independently from PhilHealth circulars and advisories, Philippine law, and published research. "
               "It is not a PhilHealth course, certification, or accreditation requirement. It does not replace current issuances, written "
               "guidance from your PhilHealth Regional Office, your facility&rsquo;s approved procedures, or the treating team, who always "
               "decide clinical questions."),
    "pathways_tag": "Five weeks",
    "pathways_h2": "Five weeks of study, in six parts",
    "pathways_nav": "Parts",
    "pathways_html": """
<p>The first ten modules follow a PhilHealth claim from the patient&rsquo;s first visit to the closed file. Part 6 adds the HMOs: the same discipline applied to private payers, each with its own contract. A suggested pace is five weeks of lessons and practice (about 17 hours), with the 90-minute capstone after Module 11 and three supervised observations at work.</p>
{{cards:The five parts|Part 1 &middot; Foundations::Modules 1 to 3. Roles and policy, intake and eligibility, the benefit and patient charges.|Part 2 &middot; Building the claim::Modules 4 to 6. Session evidence, the claim packet and codes, eClaims and deadlines.|Part 3 &middot; After filing::Modules 7 and 8. Returns and denials, payments and reconciliation.|Part 4 &middot; Protection and routing::Modules 9 and 10. Privacy and audit, renal pathways and the handoff.|Part 5 &middot; Capstone::Module 11. A near-cap transfer with a mixed queue, plus copyable job aids.|Part 6 &middot; HMO claims and collections::Modules 12 to 14. Accreditation and payer profiles, letters of authorization and claim batches, payments, disallowances, and collections.}}
{{cards:Three roles, one track|Clerk or encoder::Verifies identity, assembles evidence, encodes from source, and routes discrepancies. Lead role in Modules 2, 4, and 5.|Claims officer or reviewer::Checks readiness, files with authorization, manages returns and denials, and reconciles payments. Lead role in Modules 5 to 8, 13, and 14.|Liaison::Explains benefits, coordinates the dialysis database and transfers, and keeps written contact with PhilHealth. Lead role in Modules 1, 3, 10, and 12.}}
""",
    "modules_h2": "Thirteen modules and a capstone",
    "modules_intro": ("Study the modules in order. Each one starts from why a rule exists, moves to what the current issuance says, and ends "
                      "with what you do at the desk on Monday morning."),
    "syllabus_note": ("Each module takes about 65 to 100 minutes to read and work through (about 17 hours in all), plus the 90-minute "
                      "capstone. Skills checklists are completed with a supervisor using fictional records."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 8 questions drawn at random from a bank of 15; the mastery mark is 7 of 8 on two different sets. The end-of-track examination draws 40 questions from all fourteen banks. The capstone (Module 11) is scored out of 100: a pass is 80 or more <strong>and</strong> zero critical errors, judged before the score. Employer sign-off requires three observed tasks at work: a correct intake, a full submission simulation, and an exception handoff.</p>
""",
    "sources_html": """
<p>The track is built from PhilHealth&rsquo;s own circulars and advisories on the hemodialysis benefit, eligibility, the electronic statement of account, eClaims 3.0, filing periods, accreditation, Z benefits, and the transition to diagnosis-related groups, together with the Data Privacy Act and its implementing rules.[[pc_pc2024_0023]][[pc_pc2023_0009]][[pc_pc2025_0007]][[pc_pa2026_0022]][[pc_pa2026_0027]][[pc_pc2026_0012]][[dch_ra10173]] The HMO modules rest on the executive order that placed HMOs under the Insurance Commission and on the Commission&rsquo;s circular letters on unsound business acts, complaints, and liquidity.[[pc_eo192_2015]][[pc_ic_cl2024_01]][[pc_ic_cl2018_14]][[pc_ic_cl2024_18]] Clinical statements on why every session matters rest on published cohort studies, worded at the strength of the evidence.[[dch_foley2011]][[pc_obialo2012]][[pc_fotheringham2020]]</p>
<p>Policy figures were checked against PhilHealth&rsquo;s published documents on November 24, 2026, and signed off by Dr. William Gregory M. Rivero the same day. The HMO modules (12 to 14) were added and their sources checked on November 26, 2026. Rules change by circular and advisory; every rate and date in this track is shown as text so it can be updated, and the course says where a local decision must be confirmed in writing with your PhilHealth Regional Office.</p>
""",
    "trainers_intro": ("A claims lead, a unit manager, or a facility head can use these modules as the guided-study part of a claims "
                       "staff member&rsquo;s orientation. "),
    "trainer_h2": "Using the track to prepare claims staff",
    "trainer_html": """
<p>The track supports orientation; it does not replace supervised practice with your facility&rsquo;s own systems. A practical plan is two or three modules a week over five weeks, each followed by a short desk exercise with fictional records, then the capstone and three supervised observations.</p>
{{flow:Suggested sequence|Week 1::Modules 1 to 3. Ungraded diagnostic first: a name mismatch, a schedule entry with no treatment note, and a portal timeout. Use the answers to assign extra practice.|Week 2::Modules 4 to 6. Build a session ledger, a packet manifest, and a deadline calendar from fictional records.|Week 3::Modules 7 and 8. Work a returned claim, a denial, and a short remittance.|Week 4::Modules 9 and 10, then the capstone (Form A; Form B for reassessment).|Week 5::Modules 12 to 14 for staff who handle HMO claims. Build a payer profile, split three sessions, and age a fictional receivables list.|After the course::Three observed tasks at work, recorded with date, observer, evidence reference, outcome, and any limits on delegated duties.}}
<p>Before staff use the course for live work, a claims lead should complete the facility adoption record in the capstone job aids with the facility head: contacts, intake and forms, the confirmed filing trigger, exception channels, systems, and audit rules. Review it whenever a new issuance changes the workflow, and at least every quarter.</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments: 7 of 8 on two different sets for each module, with every missed question reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated to a supervisor with fictional records.</li>
<li>Capstone 80 of 100 or higher with zero critical errors, plus three supervised observations at work.</li>
</ul>
<p>Completion is an Academy learning record. It is not a PhilHealth certification, system access, or signing authority; your employer decides delegation in writing.</p>
""",
    "related": [("calc-philhealth-claims-toolkit.html", "Five calculators for claims staff: filing deadlines, the 156-session ledger, remittance, performance rates, and bill checking."),
                ("zero-balance-billing-philhealth.html", "How zero balance billing works for PhilHealth members."),
                ("philhealth-acr-to-drg.html", "How PhilHealth is moving from case rates to diagnosis-related groups.")],
}

P1, P2, P3, P4, P5, P6 = ("Part 1 &middot; Foundations", "Part 2 &middot; Building the claim", "Part 3 &middot; After filing",
                          "Part 4 &middot; Protection and routing", "Part 5 &middot; Capstone", "Part 6 &middot; HMO claims and collections")

_ROWS = [
    ("01", "roles-and-policy", "Roles, Authority, and Policy", P1,
     "Who owns each decision, which issuance governs, how to resolve a conflict between sources, and the traceable hold note.",
     "Three pairs of hands passing a claim folder along a desk like a relay baton."),
    ("02", "eligibility-and-pdd", "Intake, Eligibility, and the Dialysis Database", P1,
     "Identity, eligibility, and PhilHealth Dialysis Database registration as separate checks, transfers, and the red flags that come before paperwork.",
     "A liaison welcoming an elderly man in a wheelchair and his adult son at an intake corner."),
    ("03", "hd-benefits", "The Hemodialysis Benefit, Patient Charges, and the Agreement Form", P1,
     "156 sessions at the package rate, what every session must include, why those items are covered, the agreement form, and fair billing.",
     "A man and his niece reading a one-page form together before his dialysis session."),
    ("04", "session-evidence", "Session Evidence, Utilization, and the Yearly Count", P2,
     "Proving a session happened, the one-row-per-encounter ledger, emergency sessions, shortened sessions, and the year boundary.",
     "A clipboard with a signed treatment sheet beside sealed red and blue bloodlines."),
    ("05", "forms-and-esoa", "The Claim Packet, Codes, and Diagnosis-Related Groups", P2,
     "The manifest, per-session agreement forms, the electronic statement of account, diagnosis and procedure codes, and what case rates and diagnosis-related groups mean for you.",
     "An open tabbed claim folder surrounded by its source documents."),
    ("06", "eclaims", "eClaims 3.0, Filing Deadlines, and Acknowledgments", P2,
     "Single transmission, the official receipt, filing clocks and internal targets, extensions, and what to do when the portal times out.",
     "A receipt slip emerging from a small printer, a laptop and a calendar behind it."),
    ("07", "returns-and-denials", "Returned Claims, Denials, and Escalation", P3,
     "Validation errors, returns, and denials as different events with different clocks, the case chronology, and a useful message to PhilHealth.",
     "Two claims staff pinning a letter to a chronology board."),
    ("08", "reconciliation", "Payments, Reconciliation, and Professional Fees", P3,
     "The three-way match, the facility and professional-fee split, the release clock, and performance rates with fixed definitions.",
     "A finance officer at a desk looking through glass onto the dialysis treatment floor."),
    ("09", "privacy-and-audit", "Privacy, Accreditation, and Audit Readiness", P4,
     "Why dialysis data is sensitive, the first hour after a wrong-recipient email, validity on the service date, and the audit trail.",
     "A steel filing cabinet with indexed folders and a padlock on top."),
    ("10", "renal-pathways", "Renal Pathways and the Patient Handoff", P4,
     "Maintenance hemodialysis, emergency sessions, acute kidney injury, peritoneal dialysis, and transplant, and a handoff that closes the loop.",
     "A young woman walking with a nurse in a corridor that branches three ways."),
    ("11", "practicum", "Capstone Practicum and Job Aids", P5,
     "A 90-minute near-cap transfer with a mixed queue, the scoring sheet and critical errors, a reassessment form, and copyable job aids.",
     "A claims officer working through an orderly arc of documents while a supervisor observes."),
    ("12", "hmo-accreditation", "HMOs, Accreditation, and the Payer Profile", P6,
     "Who regulates HMOs, the accreditation agreement clause by clause, why many plans limit dialysis, and the payment order: PhilHealth first, then the HMO, then the patient.",
     "A claims officer pinning four color-coded payer cards to a corkboard beside a signed contract."),
    ("13", "hmo-loa-and-claims", "HMO Verification, Letters of Authorization, and the Claim Batch", P6,
     "Three verification checks, reading and renewing the letter of authorization, splitting a session among three payers, and a batch filed once with proof of receipt.",
     "A clerk reading an approval code on a laptop while a patient waits with her health card and ID."),
    ("14", "hmo-collections", "HMO Payments, Disallowances, and Collections", P6,
     "Posting payments with tax withheld, sorting and appealing disallowances, aging by payer, the collection ladder, Insurance Commission complaints, and payer risk.",
     "A claims officer and a finance officer reviewing an aging report with one payer bar much longer than the rest."),
]
MODULES = []
for _id, _slug, _title, _part, _sub, _brief in _ROWS:
    row = {"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part, "hero_brief": _HB + _brief,
           "card_img": f"{HUB}-{_id}-card.webp"}
    if _id == "11":
        row["hero_file"] = f"{HUB}-practicum-vignette-hero"
    MODULES.append(row)
