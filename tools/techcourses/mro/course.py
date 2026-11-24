# -*- coding: utf-8 -*-
"""Medical Records Officer and Custodian (MRO) track: course definition in the POD/DCH package schema.
Written for the Renal Care Academy from published sources (editorial package v2.0, November 24, 2026).
Every case, name, and identifier in the series is fictional."""

HUB = "medical-records-officer"
_HB = "Illustrated clinical vignette, warm natural light, Filipino staff and patients, modern hemodialysis unit, no text and no legible names or numbers in image. "

COURSE = {
    "title": "Medical Records Officer and Custodian",
    "short": "Records Officer",
    "hub_slug": HUB,
    "label": "Training track for the records officers of hemodialysis units",
    "tag": "Health Information",
    "icon": "🗂️",
    "no_branch": True,
    "audience": ("Designated medical records officers, custodians, and deputies in standalone and hospital-based hemodialysis units "
                 "&middot; hospital health information management staff assigned to dialysis &middot; unit managers who supervise records"),
    "audience_type": "Medical records officers of hemodialysis units",
    "level": "College reading level; no clinical license assumed",
    "review_date": "2026-11-24",
    "draw": 8,
    "mastery": "7 of 8",
    "keywords": ("dialysis medical records officer Philippines, hemodialysis records custodian training, PhilHealth hemodialysis 156 sessions Annex A, "
                 "PhilHealth Dialysis Database PDD, Philippine Renal Disease Registry, ICD-10 ICD-11 Philippines, Data Privacy Act health records, "
                 "NPC breach 72 hours, DOH records disposition schedule 2021-0226, dialysis downtime reconciliation"),
    "page_title": "Medical Records Officer and Custodian: A Training Track",
    "desc": ("A free training track for the records officers of hemodialysis units: authority and designation, the dialysis chart and its "
             "technical logs, patient identity, capture and corrections, ICD-10 and ICD-11 coding, PhilHealth claims evidence, registries, "
             "privacy and release, certificates, retention, digital custody, downtime, inspection metrics, and transfers."),
    "h1": "Medical Records <em>Officer</em>",
    "sub": ("A training track for the person who keeps the dialysis record. Learn to keep every fact attributed, attached to the right "
            "person, complete, findable, protected, and kept exactly as long as required, without ever changing what a clinician wrote."),
    "disclaimer": ("Educational material for records staff. Completing it is an Academy learning record only. It does not confer DOH-recognized "
                   "training credit, a facility designation, or system access, and it does not replace current regulations, your facility&rsquo;s "
                   "records manual, or advice from your data protection officer or counsel."),
    "scope_note": ("This module is study material for the records officers of hemodialysis units. It explains the reasoning behind common records "
                   "decisions; it is not a records manual and not legal advice. Regulations change: confirm every rule against the current text and "
                   "your facility&rsquo;s approved policy before you rely on it. Clinical content belongs to its clinical author; questions about a "
                   "patient&rsquo;s care go to the attending nephrologist. Every case, name, and identifier is fictional."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Records officers",
    "branch_blurb": ("For the person who keeps the dialysis record: identity, the chart and its technical logs, coding, PhilHealth evidence, "
                     "registries, privacy, certificates, retention, downtime, audits, and transfers."),
    "academy_meta": "14 modules &middot; a capstone &middot; a calculator toolkit",
    "hero_alt": "A medical records officer at a bright, orderly records workstation inside a hemodialysis unit, with labeled chart folders, a document scanner, and the dialysis floor visible through a glass partition.",
    "start_h2": "The keeper of the record",
    "start_html": """
<p>A patient on maintenance hemodialysis (HD) comes in about 156 times a year. Each visit leaves a trail: the order that authorized the treatment, the run sheet that proves it happened, the dialyzer and water logs that prove it was safe, the claim that pays for it, the registry row that counts it. Months or years later, someone will depend on each of those facts being exactly right &mdash; the next nurse, the payer, an inspector, a receiving unit, a court.</p>
<p>Think of the dialysis record as a <strong>chain of custody for clinical truth</strong>. Clinicians create the facts. The medical records officer (MRO) never creates or changes a clinical fact; the MRO makes sure each one is <strong>attributed</strong>, attached to the <strong>right person</strong>, <strong>complete</strong>, <strong>findable</strong>, <strong>protected</strong>, and <strong>kept exactly as long as required</strong>. When a link breaks, the failure usually shows up far downstream &mdash; a denied claim, a registry rejection, a wrong-patient lab result, a privacy complaint &mdash; so this track teaches you to trace failures back upstream instead of patching them where they appear.</p>
{{fig:mro00_chain}}
{{cards:What this track will help you do|Know whose rule it is::Read any rule for its issuer, scope, and effective date, and route each decision to its owner.|Keep identity clean::Match on two person-level identifiers, search before you create, and never merge on a hunch.|Prove care was authorized, delivered, and safe::Index orders, run sheets, and the technical logs that back them.|Support honest claims::Prove eligibility, delivery, and documentation separately, and catch duplicates.|Protect patients' information::Release only the minimum through a verified channel, and escalate a breach inside the hour.|Keep records as long as required, no longer::Apply the Department of Health (DOH) disposition schedule, honor holds, and document lawful destruction.|Survive the bad day::Reconcile downtime paper, pass an inspection, and close a transfer on receipt.}}
<p>The track is written in plain language at a college reading level, and no clinical license is assumed. Every module has a case, figures, a skills checklist for a preceptor, and a self-assessment drawn from a bank of fifteen questions. The target level is an <strong>independent records officer</strong>: someone who can run the dialysis records function for a week without supervision and who knows exactly which decisions belong to someone else.</p>
""",
    "exam_draw": 40,
    "is_not": ("It is a training track written independently from published laws, regulations, guidelines, and research. It is not a DOH-recognized "
               "training certificate, a facility designation, PhilHealth accreditation, or legal advice. It does not replace your facility&rsquo;s "
               "records manual, your data protection officer, or counsel, and clinical questions always go to the attending nephrologist."),
    "pathways_tag": "Four weeks",
    "pathways_h2": "Four weeks of study, in four parts",
    "pathways_nav": "Weeks",
    "pathways_html": """
<p>The fourteen modules follow the path a fact takes through a dialysis unit: who has authority over it, how it is captured and attached to the right person, how it is coded and paid and counted, how it is protected and released, how long it is kept, and how it survives a system failure, an inspection, or a transfer.</p>
{{cards:The four weeks|Week 1 &middot; The record and the person::Modules 1 to 4. Authority, the dialysis chart and its technical logs, identity and the patient index, capture and corrections.|Week 2 &middot; Codes, claims, and counts::Modules 5 to 7. ICD-10 and ICD-11 with compliant queries, PhilHealth evidence and the 156-session ledger, registries.|Week 3 &middot; Rights and lifecycle::Modules 8 to 10. Privacy and release, certificates and abstracts, retention and holds.|Week 4 &middot; Systems and handovers::Modules 11 to 14. Digital custody, downtime and recovery, inspection metrics, transfers and international practice.}}
""",
    "modules_h2": "Fourteen modules in four weeks",
    "modules_intro": ("Study the modules in order. Each one starts from why a records control exists, moves to what the rules and the evidence say, "
                      "and ends with what a records officer does on the next shift."),
    "syllabus_note": ("Each module takes about 80 minutes: 25 to read, 15 for the worked example, 30 for practice, and 10 for the self-assessment "
                      "(about 19 hours of study in all), plus 8 hours of supervised practice and 5 for review, the examination, and the capstone."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 8 questions drawn at random from a bank of 15; the mastery mark is 7 of 8 on two different sets. The end-of-track examination draws 40 questions from all fourteen banks. The capstone is a 90-minute simulated shift &mdash; an inspection, a transfer, and a downtime at once &mdash; scored on five dimensions with listed critical failures, such as wrong-patient filing, unauthorized release, bypassing a hold, or inventing clinical data.</p>
""",
    "sources_html": """
<p>The track is built from published sources. Philippine requirements follow the Department of Health (DOH) licensing order and assessment tool, the DOH records disposition schedule, PhilHealth circulars and advisories, the Philippine Society of Nephrology (PSN) hemodialysis guidelines, and the Data Privacy Act and National Privacy Commission (NPC) rules.[[doh2012]][[dch_doh_rao_tool]][[mro_doh2021rds]][[dch_philhealth2024]][[psn2024]][[dch_ra10173]][[dch_npc1603]] Statements about how records fail rest on peer-reviewed studies of patient matching, wrong-patient errors, downtime, copy-and-paste, and registry accuracy.[[mro_just2016]][[mro_adelman2019]][[mro_larsen2018]][[mro_tsou2017]][[mro_longenecker2000]]</p>
<p>Where the evidence is observational, the text says &ldquo;associated with.&rdquo; Rules from other countries appear only as comparisons, never as Philippine deadlines. Regulatory statements were checked against public sources on November 24, 2026. Two items could be confirmed only in part: the claims switch-over date in DOH Administrative Order 2025-0021 on ICD-11, and the annex of non-patient record classes in DOH Department Circular 2021-0226. Confirm both locally before you rely on them.[[mro_doh2025icd11]]</p>
""",
    "trainers_intro": ("A health information management head, a unit operations manager, or a dialysis clinical head can use these modules as the guided-study part of a records officer&rsquo;s orientation. "),
    "trainer_h2": "Using the track to prepare a records officer",
    "trainer_audience": "HIM heads, unit operations managers, clinical heads, data protection officers, and preceptors",
    "trainer_html": """
<p>The track supports orientation; it does not replace it. A practical plan is four weeks: about five hours of modules a week, each paired with a two-hour supervised session on the learner&rsquo;s own unit using fictional records, then the capstone. Claims staff, the head nurse, and the data protection officer (DPO) should join the sessions that touch their decisions.</p>
{{flow:Suggested sequence|Week 1::Modules 1 to 4. Build the role and source register, audit a chart, resolve an identity exception, disposition a scan.|Week 2::Modules 5 to 7. Write a non-leading query, reconcile a claims ledger with a duplicate, balance a registry batch.|Week 3::Modules 8 to 10. Role-play a release request and a misdirected email, draft a certificate with a source sheet, place a hold.|Week 4::Modules 11 to 14. Run an access review, reconcile downtime sheets, report a rate with its interval, close a transfer.|Capstone::A 90-minute simulated shift with an injected registry rejection, then 20 minutes of feedback.}}
<p><strong>Safety-gated assessment.</strong> For a formal sign-off, run a supervised sitting in which the learner must also answer every safety question correctly &mdash; wrong-patient filing, a disputed diagnosis code, a canceled session staged for a claim, release to an unverified requester, a hold on an eligible chart, and shared credentials &mdash; regardless of the total score. Keep signed assessments in the facility&rsquo;s staff training file, and use fictional identifiers in every exercise.</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments: 7 of 8 on two different sets for each module, with every missed question reviewed.</li>
<li>Every <span class="tc-crit">Critical</span> step on every checklist demonstrated independently to a preceptor in simulation.</li>
<li>Capstone 16 of 20 or higher, every dimension at least 2 of 4, and no critical failure: wrong-patient filing or disclosure, unauthorized release, bypassing a hold, inventing clinical data or certificate statements, submitting a known duplicate or an undelivered session, using shared credentials, or failing to escalate a suspected breach promptly.</li>
</ul>
<p>Completion is an Academy learning record. It is not DOH-recognized training credit, a facility designation, or system access.</p>
""",
    "related": [("calc-medical-records-officer-toolkit.html", "Seven calculators for the dialysis records office."),
                ("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
}

W1, W2, W3, W4 = ("Week 1 &middot; The record and the person", "Week 2 &middot; Codes, claims, and counts",
                  "Week 3 &middot; Rights and lifecycle", "Week 4 &middot; Systems and handovers")

_ROWS = [
    ("01", "role-and-authority", "Role, Designation, and Sources of Authority", W1,
     "The four rulebooks that govern a dialysis record, reading a rule for issuer, scope, and date, the role file, and who decides what.",
     "A records officer and a unit manager reviewing a binder labeled role file at a desk in a dialysis clinic office."),
    ("02", "dialysis-chart", "The Dialysis Chart and Its Technical Records", W1,
     "What the order, the run sheet, and the dialyzer, water, and machine logs each prove, and routing deficiencies to their owners.",
     "A records officer cross-checking a run sheet against a dialyzer reprocessing log beside a records cabinet."),
    ("03", "identity-and-intake", "Identity, Intake, and the Master Patient Index", W1,
     "Two person-level identifiers, search before create, how duplicates are really made, and resolving a suspected misfile safely.",
     "A records clerk at a dialysis intake desk checking an older patient's ID card while his daughter waits beside him."),
    ("04", "capture-and-corrections", "Capture, Indexing, Authentication, and Corrections", W1,
     "Six-field capture, scan quality checks, indexing versus clinical corrections, late entries, and copied text.",
     "A records officer feeding a treatment record into a document scanner and checking the page count on a monitor."),
    ("05", "coding-and-queries", "Coding: ICD-10 Today, ICD-11 Tomorrow, and Compliant Queries", W2,
     "Coding only from authenticated notes, tabular verification, diagnosis versus procedure fields, the ICD-11 transition, and non-leading queries.",
     "A records officer and a nephrologist reviewing a written documentation query together at a nurses' station."),
    ("06", "philhealth", "PhilHealth: Eligibility, the 156-Session Ledger, and the Claim Packet", W2,
     "The current HD package, the per-session Annex A, the session ledger, three separate proofs, and duplicates.",
     "A records officer and a claims clerk comparing signed session forms with a claims list at a small office desk."),
    ("07", "registries", "Registries and Data Quality", W2,
     "Two different registries, event definitions, the event ledger, balancing a batch, and why registries inherit the chart's gaps.",
     "A records officer reviewing a printed event ledger with a highlighter beside a computer in a quiet records room."),
    ("08", "privacy-and-release", "Privacy, Patient Rights, and Release of Information", W3,
     "Five checks before release, access and correction as rights, and the first hour after a misdirected record.",
     "A records officer at a release counter politely checking a woman's written authorization and ID card."),
    ("09", "certificates-and-abstracts", "Certificates, Clinical Abstracts, and Patient Requests", W3,
     "Preparing drafts from the authenticated chart, dialysis vintage and serology dates, physician authorship, and the request log.",
     "A records officer handing a draft clinical abstract with a source sheet to a nephrologist for review and signature."),
    ("10", "retention-and-holds", "Retention, Holds, and Lawful Disposition", W3,
     "The DOH disposition schedule, the right trigger date, holds that override schedules, and documented destruction.",
     "A records officer labeling archive boxes on metal shelving in a clean, well-lit records storage room."),
    ("11", "digital-custody", "Digital Custody, Access Control, and Audit Trails", W4,
     "One person, one account, access reviews and offboarding, reading the audit trail, backups, and national data standards.",
     "A records officer and an IT staff member reviewing a user access list on a monitor in a clinic office."),
    ("12", "downtime-and-recovery", "Downtime and Recovery", W4,
     "Downtime kits, numbered paper sheets, reconciling schedule, paper, and electronic records, and balancing the counts.",
     "A nurse and a records officer comparing a numbered paper downtime sheet with a laptop at a dialysis nurses' station."),
    ("13", "inspection-and-quality", "Inspection Readiness, Metrics, and Improvement", W4,
     "The evidence index, defining numerators and denominators before sampling, confidence intervals, and re-measurement.",
     "A records officer and a quality lead reviewing a run chart and an evidence binder in a small dialysis office."),
    ("14", "transfers-and-international", "Transfers, Transient Dialysis, and International Practice", W4,
     "The transfer packet, verifying the recipient, closing on receipt, downstream updates, and borrowing good process from abroad.",
     "A records officer on the phone with a hospital switchboard while checking a transfer packet manifest."),
]
MODULES = []
for _id, _slug, _title, _part, _sub, _brief in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part,
                    "card_img": f"{HUB}-{_id}-card.webp", "hero_brief": _HB + _brief})
