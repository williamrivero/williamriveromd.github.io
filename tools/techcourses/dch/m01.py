# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 01: Before You Sign: Authority and Appointment. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician reading an appointment letter across a desk from a clinic owner, a floor plan and a list of sites between them.",
    "objectives": [
        "Describe what a clinical head owns, and what belongs to the owner, the attending nephrologist, the head nurse, and the technical leads.",
        "Explain why the reach of one physician across several sites is a patient-safety question, not only a contract question.",
        "Build an authority matrix that names, for each decision, the owner, the alternate, and the escalation route.",
        "Trace each qualification and coverage requirement to the rule that sets it, and record which ones are still unconfirmed.",
        "Settle three questions with the owner before you sign: who stops an unsafe operation, who pays to fix it, and who restarts it.",
        "Decline or defer an appointment whose scope you cannot oversee, and say why in writing.",
    ],
    "big": """
{{plain:An appointment letter is like the keys to a car you have not driven. Before you take it on the highway, you check the brakes, ask who else has a key, and find out who pays when it breaks down.}}
<p>The picture has a limit. A car has one driver. A dialysis unit has many: the owner who funds it, the nephrologists who prescribe, the nurses who treat, and the technicians who release the water and the machines. Your job is not to drive every one of them. It is to make sure the system they work in is safe, and to stop it when it is not.</p>
{{cards:Key terms for this module|Clinical head::The physician appointed to oversee the clinical system of a dialysis unit: policies, competency arrangements, the quality program, and the decision to hold or restart a service. The Philippine Society of Nephrology (PSN) describes a Dialysis Clinical Head for freestanding units and a Dialysis Unit Head in hospitals.|Owner or governing body::The person or board that funds the unit, assigns authority in writing, and receives risks the unit cannot manage on its own.|Attending nephrologist::The physician responsible for each patient&rsquo;s prescription and care plan.|Authority matrix::A table listing each recurring decision, who makes it, who covers when that person is away, and where it escalates.|LTO::License to Operate, the Department of Health (DOH) authority for a non-hospital dialysis clinic to operate.|RLED::Regulatory, Licensing and Enforcement Division of the DOH Center for Health Development in your region.|Alternate::The named person who holds a decision when its owner is unreachable.}}
{{flow:Three habits this module teaches|Map before you sign::Every site, every decision, every alternate.|Ask in writing::Unclear rules go to the regulator, and the answer goes in the file.|Hold what you cannot oversee::An appointment can wait. A patient harmed by a gap cannot.}}
""",
    "case": {"title": "Four sites by Monday", "html": """
<p>Bayani Dialysis, a growing freestanding group, offers Dr. Ramon Castillo the clinical head appointment for all its sites, starting Monday. The owner, Mr. Arnel Uy, hands over a two-page letter. It names &ldquo;the company&rsquo;s dialysis units&rdquo; without listing them. Over coffee, Mr. Uy explains there are four: two in Quezon City, one in Bulacan, and one opening in Pampanga next month. The Pampanga site is two hours away in traffic.</p>
<p>&ldquo;The last clinical head visited the far sites once a month and answered calls the rest of the time,&rdquo; Mr. Uy says. He shows a printed licensing assessment tool, marked Revision 03, April 2015, that he says allows up to three clinics per head. &ldquo;We are a bit over, but the fourth is not open yet. Can you sign today?&rdquo;</p>
""", "questions": ["Would you sign today? What would you need to see first?",
                  "Which questions belong to the DOH, which to PSN, and which only to Mr. Uy?",
                  "Who covers the existing units while you check?"]},
    "sections": [
        ("why", "Why it matters", "Why the appointment is a safety question", """
<p>Patients on maintenance hemodialysis live close to the edge. Without kidney function, potassium and water accumulate between sessions, and the risk of death is highest after the longest gap of the week. In a United States cohort, all-cause mortality was 22.1 per 100 person-years on the day after the two-day weekend gap, compared with 18.0 on other days, and admissions for heart failure nearly doubled.[[dch_foley2011]] A unit that cannot deliver a scheduled session, or cannot act when a session goes wrong, removes the margin these patients depend on.</p>
<p>That is why the appointment matters. If you sign for four sites you cannot reach, or for authority you do not have, the gap does not disappear. It moves to the night a nurse calls about a water alarm and nobody with authority answers.</p>
{{fig:dch01_sites}}
<p>The workload is growing. Press reports citing the Philippine Renal Disease Registry put 64,845 Filipinos on dialysis in 2024, up 22% from 53,296 in 2023. These figures come from news reports, not the registry itself. More units, more sites per group, and more payer review all land on the physician who signs as clinical head.</p>
{{key:You are signing for a system. Ask to see the system before you sign.}}
"""),
        ("lanes", "Who owns what", "Who owns each decision", """
<p>Most failures of governance are failures of ownership. A decision that belongs to two people belongs to no one. Before you sign, draw the lanes.</p>
{{fig:dch01_lanes}}
<div class="table-wrap"><table>
<thead><tr><th>Lane</th><th>Owns</th><th>Your part as clinical head</th></tr></thead>
<tbody>
<tr><td>Owner or governing body</td><td>Funding, contracts, assigning authority in writing, accepting risks the unit cannot manage</td><td>Bring risks with their consequences and a request; record the owner&rsquo;s decision</td></tr>
<tr><td>Clinical head</td><td>Clinical policies, competency arrangements, the quality program, holding or restricting unsafe operation, signing clinical restart</td><td>Yours</td></tr>
<tr><td>Attending nephrologist</td><td>Each patient&rsquo;s prescription, care plan, and whether that patient can safely wait</td><td>Make sure the system lets them order, monitor, and be reached safely</td></tr>
<tr><td>Physician on duty</td><td>In-shift assessment, emergency response, closed-loop handover</td><td>Approve the protocols they work under and the coverage schedule</td></tr>
<tr><td>Head nurse</td><td>Nursing assignments, bedside competencies, shift readiness, nursing documentation</td><td>Support the head nurse&rsquo;s holds; review the competency program</td></tr>
<tr><td>Technical leads</td><td>Water testing, machine maintenance, technical release</td><td>Never sign a technical release; always require one before clinical restart</td></tr>
<tr><td>Operations and claims</td><td>Staffing logistics, procurement, claims submission and reconciliation</td><td>Set the clinical standards those processes must meet</td></tr>
</tbody></table></div>
<p>If the title &ldquo;head of facility&rdquo; legally belongs to someone else, such as a hospital director, record that separately. Your appointment should say which decisions you hold and which you only advise on.</p>
"""),
        ("rules", "The rules", "Which rule answers which question", """
<p>Several authorities speak to the clinical head&rsquo;s role, and each answers a different question. Keep a separate evidence item for each, because one document cannot satisfy another&rsquo;s requirement.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Source</th><th>What to keep in the file</th></tr></thead>
<tbody>
<tr><td>May this facility operate, and what must its head do?</td><td>DOH licensing order for dialysis facilities[[doh2012]] and the current regional assessment tool</td><td>LTO and its scope, signed appointment and job description, credentials, visit logs</td></tr>
<tr><td>Has the licensing rule changed?</td><td>DOH Department Circular 2026-0112, interim guidelines on licensing hemodialysis clinics[[dch_doh2026]]</td><td>The full circular and annexes, and the regional office&rsquo;s written reading of how it applies to you</td></tr>
<tr><td>What does the profession expect of a clinical head?</td><td>PSN hemodialysis guidelines[[psn2024]] and its attestation checklist[[dch_psn_attest2020]]</td><td>Licensure, nephrology certification, contract with decision rights, evidence of oversight, training, and surveillance</td></tr>
<tr><td>Will the facility be paid?</td><td>PhilHealth accreditation and performance commitment[[dch_philhealth2023acc]][[dch_philhealth_pa2025]]</td><td>Provider data record, signed commitment, validity dates, authorized signatories</td></tr>
</tbody></table></div>
<p>The printed tool Mr. Uy shows is a real historical document. A regional office posted a 2015 assessment tool, Revision 03, that lists credential evidence for nephrologist and non-nephrologist heads, documented weekly visits, and up to three clinics per head.[[dch_doh_rao_tool]] It is not proof of today&rsquo;s rule. A newer interim circular on licensing hemodialysis clinics appears on a regional issuance index in 2026; this course confirmed its title, not its text.[[dch_doh2026]] Where an old form and the PSN guideline disagree, neither one settles it. Ask the RLED and PSN in writing, and keep both answers.</p>
{{call:Stop and ask the RLED in writing when eligibility, the number of sites, the visit cadence, or a non-nephrologist pathway is unclear. Ask PSN about its current attestation process. Do not sign for a site until the answer for that site is in your file.}}
<p>Other systems handle the same problem in instructive ways. United States rules require the medical director of a dialysis facility to be board-certified with approved nephrology training and at least 12 months of dialysis experience, and assign the director quality assessment, staff education, and policy oversight.[[dch_cfr494]] Singapore requires a named clinical governance officer with specialist registration in renal medicine for each licensed outpatient dialysis service.[[dch_hcsa]] The common thread is a named person, a defined scope, and written accountability to the governing body.</p>
"""),
        ("file", "The appointment file", "What goes in the appointment file", """
{{fig:dch01_file}}
<p>Build the file before you start, not after the first inspection. It answers one question: what can I decide, where, and with what support?</p>
{{flow:The appointment file|1. Credentials::Professional license, specialty certification, life support certificates, and their expiry dates.|2. Contract and scope::Term, the sites and stations covered, and anything excluded.|3. Presence and coverage::Visit cadence per site, how you are reached, and response times you can actually meet.|4. Delegated authority::The decisions you hold alone, the ones you share, and the ones you advise on.|5. Alternates::A named physician who holds your decisions at each site when you are away.|6. Escalation::Who in the governing body receives a risk you cannot manage, and how fast.|7. Resources::What the owner commits to fund when a control fails.}}
<p>At the first meeting with the owner, rehearse three scenarios aloud: an unsafe roster, an unresolved water result, and a refusal to fund a repair. For each, record who stops the affected activity, who tells the patients, who verifies the fix, and who authorizes restart. If the owner will not agree that you can hold an unsafe operation, you do not yet have the authority the role requires.</p>
{{formula:<strong>Reach check, illustration only.</strong> Four sites, one physician, a weekly visit of three hours each, plus travel of 0.5, 0.5, 1.5, and 2 hours each way: 12 hours on site plus 9 hours of travel, about 21 hours a week before any call or emergency. Ask whether that leaves time for your own patients, and who covers when you are at the far site.}}
"""),
        ("decline", "Saying not yet", "When to defer or decline", """
<p>Declining an appointment is not a failure of service. It protects the patients who would be relying on oversight that does not exist. You can defer a site rather than refuse the whole appointment.</p>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>A reasonable response</th></tr></thead>
<tbody>
<tr><td>Scope unnamed</td><td>Sign only for a listed schedule of sites and stations</td></tr>
<tr><td>Site count or cadence unconfirmed</td><td>Sign for the confirmed sites; defer the rest until the RLED answers</td></tr>
<tr><td>No authority to hold unsafe operation</td><td>Do not sign until it is written in</td></tr>
<tr><td>No alternate for a site</td><td>Defer that site until one is named and has accepted</td></tr>
<tr><td>A site opening before its approvals</td><td>Decline to be named as its head until licensing is complete</td></tr>
</tbody></table></div>
{{key:An appointment can wait a week. A gap in oversight waits for the worst night of the year.}}
"""),
    ],
    "debrief": ["""
<p><strong>Would you sign today?</strong> Not for all four sites. Ask for a written schedule naming each site, its stations, its LTO, and its current head. Ask to see the assessment tool the regional office uses now, and the text of any new interim circular. Offer to sign for the two Quezon City sites if the scope, coverage, and authority are clear, and defer Bulacan and Pampanga until the RLED answers.</p>
<p><strong>Which questions belong to whom?</strong> Eligibility, permitted number of sites, and visit cadence are licensing questions for the RLED. Certification and attestation are questions for PSN. Funding, contracts, and the authority to hold an unsafe operation are questions for Mr. Uy, and his answers go into the contract. The 2015 tool is historical evidence; it does not answer any of them by itself.</p>
<p><strong>Who covers while you check?</strong> The current arrangements stay in place, with a named physician for each existing site, until the transfer of responsibility is signed. Record the date you asked each question and the person you asked.</p>
"""],
    "skills": {"title": "Authority matrix and pre-appointment meeting",
               "intro": "Build an authority matrix for a real or simulated unit, then hold a five-minute pre-appointment meeting with a preceptor playing the owner.",
               "items": [
                   ("Lists every site, its stations, license status, and current head.", False),
                   ("Traces each qualification and coverage requirement to its source and version.", True),
                   ("Marks each unconfirmed requirement and names who will be asked, and by when.", False),
                   ("Names an alternate physician for every site.", True),
                   ("Writes who stops, who tells patients, who verifies, and who restarts for an unsafe roster.", False),
                   ("Writes the same for an unresolved water result and a refused repair.", False),
                   ("Secures written authority to hold or restrict an unsafe operation.", True),
                   ("Declines or defers any site whose eligibility or coverage is unsupported.", True),
                   ("Keeps the appointment, the professional credentials, and the accreditation records as separate evidence items.", False),
                   ("Records the meeting outcome with dates and owners.", False),
               ],
               "placement": "Draw the authority matrix for your own unit. Show it to your head nurse and your owner, and ask each to mark one decision they believe belongs in a different lane. Resolve each disagreement in writing."},
    "quiz": [
        ("What does the clinical head own?",
         ["Every patient&rsquo;s prescription", "The clinical system: policies, competency arrangements, the quality program, and holding or restarting unsafe operation", "Technical release of water and machines", "Claims submission"], 1,
         "Prescriptions belong to the attending nephrologist and technical release to the technical leads."),
        ("Why does the long weekend gap matter when you judge coverage?",
         ["It is when billing closes", "Mortality and heart failure admissions are highest the day after it", "Staff are always absent then", "Water tests are not done on weekends"], 1,
         "In a large cohort, deaths and cardiovascular admissions peaked on the day after the two-day gap."),
        ("A 2015 regional assessment tool lists up to three clinics per head. What is it?",
         ["The current binding rule", "Historical evidence that needs confirmation with the regional office", "A PSN guideline", "A PhilHealth requirement"], 1,
         "Ask the RLED for the tool and rules in force now."),
        ("An old DOH form and the PSN guideline disagree on a qualification pathway. What resolves it?",
         ["Whichever is newer", "The owner&rsquo;s preference", "Written clarification from the RLED and from PSN, both filed", "A colleague&rsquo;s opinion"], 2,
         "Each authority answers its own question; get both answers in writing."),
        ("Who owns the decision that a particular patient can safely wait for a later session?",
         ["The owner", "The head nurse", "The attending nephrologist or physician on duty", "The operations manager"], 2,
         "It is a medical judgment about that patient."),
        ("Who signs the technical release of a water system after a repair?",
         ["The clinical head", "The designated technical lead", "The owner", "Any nurse"], 1,
         "The clinical head signs clinical authorization after the technical release exists."),
        ("The letter names &ldquo;the company&rsquo;s dialysis units.&rdquo; What should you ask for?",
         ["A higher fee", "A schedule listing each site, its stations, and its license", "Nothing; it is standard", "A shorter contract"], 1,
         "You cannot oversee a site you have not been told about."),
        ("Which of these must be written into the appointment before you sign?",
         ["Your parking space", "Authority to hold or restrict an unsafe operation", "The color of the uniforms", "The vendor list"], 1,
         "Without it, you carry accountability without control."),
        ("A site has no named alternate physician. What is a reasonable response?",
         ["Sign and find one later", "Defer that site until an alternate has accepted", "Ask a nurse to cover", "Cover by phone only"], 1,
         "Alternates are part of the coverage you are signing for."),
        ("United States rules assign the dialysis medical director which responsibilities?",
         ["Billing only", "Quality assessment, staff education, and policy oversight", "Building maintenance", "Patient transport"], 1,
         "The comparator shows the same pattern: named person, defined scope, accountability to governance."),
        ("What is the purpose of rehearsing three scenarios with the owner?",
         ["To impress the owner", "To agree in advance who stops, who tells patients, who verifies, and who restarts", "To set fees", "To choose vendors"], 1,
         "The middle of a crisis is too late to negotiate authority."),
        ("A site is due to open before its licensing approvals are complete. What should you do?",
         ["Accept and help it open on time", "Decline to be named as its head until licensing is complete", "Open it as a pilot", "Leave it to the owner"], 1,
         "Your name on an unlicensed site is an endorsement you cannot support."),
        ("What is an authority matrix?",
         ["An organizational chart of salaries", "A table of each decision, its owner, its alternate, and its escalation route", "A list of patients", "A staffing roster"], 1,
         "It turns &ldquo;who decides?&rdquo; into a lookup."),
        ("The same document is offered as proof for the DOH, PSN, and PhilHealth. What is the problem?",
         ["Nothing", "Each authority asks a different question and needs its own evidence", "It is too long", "It must be notarized"], 1,
         "Keep separate evidence for each authority."),
        ("In a hospital-based unit, what should the clinical head align with?",
         ["Only the owner", "Medical staff bylaws and the hospital incident command structure", "The vendor&rsquo;s manual", "Nothing beyond the unit"], 1,
         "Hospital governance shapes who holds which decision."),
    ],
    "terms": [("Clinical head", "The physician appointed to oversee the clinical system of a dialysis unit."),
              ("Governing body", "The owner or board that funds the unit, assigns authority, and accepts risks beyond the unit."),
              ("Authority matrix", "A table of each decision, its owner, its alternate, and where it escalates."),
              ("Alternate", "The named person who holds a decision when its owner is unreachable."),
              ("LTO", "License to Operate."),
              ("RLED", "Regulatory, Licensing and Enforcement Division of a DOH regional office."),
              ("Scope", "The list of sites, stations, and services an appointment covers."),
              ("Clinical restart", "The documented decision that patients may be treated again after a hold.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
