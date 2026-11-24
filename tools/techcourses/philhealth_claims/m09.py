# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 09: Privacy, Accreditation, and Audit Readiness."""

MODULE = {
    "image_alt": "A light-gray steel filing cabinet with its top drawer open, showing neatly indexed folders, a brass padlock and key on top.",
    "objectives": [
        "Explain why dialysis claims data is sensitive personal information under the Data Privacy Act.",
        "Apply minimum necessary data, approved channels, and role-based access in daily claims work.",
        "Carry out the first hour after a misdirected message, and state who decides on notifying the National Privacy Commission.",
        "Verify facility and professional validity for each service date, with reminders before expiry.",
        "Keep an audit trail from service delivery through payment, and use only fictional data in training.",
    ],
    "big": """
{{plain:A dialysis claim folder is a diary someone else wrote about the patient. It records an incurable illness, blood test results for hepatitis and HIV, family relationships, and money. If it reaches the wrong person, the patient cannot take it back.}}
<p>The picture has a limit: a diary belongs to one person, but a claim file is shared by design with clinicians, coders, finance, and PhilHealth. Privacy is not about keeping the file from everyone; it is about sharing only what each person needs, through channels the facility approved, and leaving a record of who saw what.[[dch_ra10173]][[pc_npc_irr]]</p>
{{fig:pc_firsthour}}
{{cards:Key terms for this module|Sensitive personal information::Health, finances, and identifiers that the Data Privacy Act protects most strictly.|Minimum necessary::Only the data a task or question needs.|Personal information controller::The facility, which decides how personal data is used and answers for it.|DPO::Data Protection Officer, who leads the privacy program and incident response.|NPC::National Privacy Commission.|Audit trail::A record of who created, viewed, changed, or sent a record, and when.}}
""",
    "case": {"title": "Wrong address, and a borrowed number", "html": """
<p>At 3:40 PM, a clerk sends a claim attachment for a fictional patient to an email address that differs by one letter from the PRO contact. At the same time, the claims lead notices that the facility&rsquo;s PhilHealth accreditation certificate expires in three weeks, and a colleague suggests: &ldquo;If it lapses, we can file under our other branch&rsquo;s accreditation number until it is renewed.&rdquo; Another colleague offers to share a real patient&rsquo;s file in a personal chat group &ldquo;to make training faster.&rdquo;</p>
""", "questions": ["What do you do in the first hour after the misdirected email, and who decides on notification?",
                  "What is wrong with filing under the other branch&rsquo;s number?",
                  "How do you respond to the training suggestion?"]},
    "sections": [
        ("privacy", "Privacy every day", "Privacy in daily claims work", """
<p>Health information and identifying data require controlled processing under Republic Act 10173 and its implementing rules.[[dch_ra10173]][[pc_npc_irr]] In practice: use role-based access and approved channels; check recipients and attachments before sending; share the minimum necessary; secure paper and digital files; keep the audit history when correcting data; and follow the facility&rsquo;s retention and disposal policy.</p>
<ul>
<li>Use fictional records in training, screenshots, and demonstrations. Never a real PIN, name, or result.</li>
<li>Every extra identifier in an email widens the harm if it is misdirected, including emails to PhilHealth.</li>
<li>Personal chat accounts are not approved channels for patient data.</li>
</ul>
"""),
        ("incident", "The first hour", "When data goes to the wrong person", """
{{flow:The first hour|1. Stop::Do not send more.|2. Contain::If authorized, request recall or deletion using approved wording.|3. Preserve::Keep the evidence and the sent item.|4. Record::Write down the discovery time and what was sent.|5. Report::Tell the Data Protection Officer now.}}
<p>The personal information controller, through its incident process with the DPO, assesses whether mandatory notification applies. When it does, the National Privacy Commission and the affected people are generally notified within 72 hours under the applicable rule.[[dch_npc1603]] Claims staff record the facts and actions; they do not decide reportability on their own.</p>
{{call:Report a suspected privacy incident to the DPO immediately, even if you think it is minor. A delayed report can turn a containable incident into a reportable one.}}
"""),
        ("validity", "Valid on the service date", "Accreditation and licenses", """
<p>A session delivered on a day when the facility&rsquo;s license, its PhilHealth accreditation, or a professional&rsquo;s accreditation had lapsed may not be payable, however good the care. Track the Department of Health License to Operate, current PhilHealth accreditation, authorized professionals, provider data, and the performance commitment, and match each to the current checklist for your facility type.[[dch_philhealth2023acc]][[pc_accred_process]] PhilHealth also publishes quality standards for maintenance hemodialysis that it uses as its reference.[[dch_philhealth2024q]]</p>
{{fig:pc_valid}}
<p>A hospital unit and a freestanding center each validate their own category. Each site, on each date, files under its own identifiers. Borrowing another branch&rsquo;s accreditation number misrepresents the rendering facility and undermines every claim filed under it.</p>
"""),
        ("audit", "Audit readiness", "Keeping an audit trail", """
<p>An auditor will ask three questions about any claim: which record proves the session happened, which record proves it was filed, and who owns the next action. Keep evidence from service delivery through claim payment and record access, track corrective actions, and report requirements to the medical director and compliance lead.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>Evidence</th></tr></thead>
<tbody>
<tr><td>Did the session happen?</td><td>Attested treatment record and agreement form</td></tr>
<tr><td>Was it filed, once?</td><td>Acknowledgment or claim reference with time stamp</td></tr>
<tr><td>Was it paid correctly?</td><td>Remittance line matched to the ledger</td></tr>
<tr><td>Who changed what?</td><td>Audit trail of corrections, with original entries kept</td></tr>
</tbody></table></div>
"""),
    ],
    "debrief": ["""
<p><strong>The first hour.</strong> Stop, request recall if authorized, preserve the evidence, record the discovery time (3:40 PM) and what was sent, and tell the DPO now. The facility, through the DPO, decides whether the National Privacy Commission and the patient must be notified.</p>
<p><strong>The borrowed number.</strong> Escalate the expiry to the accreditation owner and claims lead today, record the renewal evidence, and hold claim release for any date on which participation is unresolved. Filing under another branch&rsquo;s accreditation misrepresents the rendering facility.</p>
<p><strong>The training file.</strong> Decline. Use only fictional training data, and approved channels for real work. If a real file has already been shared, report it to the DPO immediately.</p>
"""],
    "skills": {"title": "Privacy and validity drill",
               "intro": "Run a simulated wrong-recipient incident and check a fictional facility&rsquo;s credential calendar.",
               "items": [
                   ("Sends only minimum necessary data through an approved channel.", False),
                   ("Stops, contains if authorized, preserves evidence, records the discovery time, and reports to the DPO at once.", True),
                   ("Leaves the notification decision to the DPO and facility.", False),
                   ("Checks license and accreditation validity for each service date.", False),
                   ("Refuses to file under another facility&rsquo;s identifiers.", True),
                   ("Uses only fictional data in training and demonstrations.", True),
               ],
               "placement": "With your DPO, review where claims data is stored and sent at your unit and list any unapproved channel."},
    "quiz": [
        ("Who determines whether mandatory breach notification applies?",
         ["The clerk", "The personal information controller, through its incident process with the DPO", "The patient", "The vendor"], 1,
         "Claims staff report and record."),
        ("What is the risk of borrowing another branch&rsquo;s accreditation number?",
         ["None", "It misrepresents the rendering facility and undermines accreditation and claim evidence", "It speeds payment", "It is allowed for a month"], 1,
         "Each site, each date."),
        ("A training screenshot contains a real PIN. What do you do?",
         ["Use it", "Replace it with synthetic data and report it if it was already shared", "Blur half", "Ask the patient"], 1,
         "Training uses fictional data only."),
        ("Accreditation renewal is pending on a service date. What about release?",
         ["Release anyway", "Hold until participation for that date is confirmed", "Use another branch", "Delete the claim"], 1,
         "Validity on the service date matters."),
        ("Why is minimum necessary safer in emails to PhilHealth too?",
         ["It is shorter", "Every extra identifier widens the harm if the email is misdirected", "PhilHealth prefers it", "It is not safer"], 1,
         "Misdirection happens to everyone."),
        ("What is the first step after sending data to the wrong recipient?",
         ["Send an apology to everyone", "Stop sending more", "Delete your sent folder", "Wait until tomorrow"], 1,
         "Then contain, preserve, record, and report."),
        ("Within what period are the NPC and affected people generally notified when notification is required?",
         ["24 hours", "72 hours", "30 days", "No limit"], 1,
         "Under the applicable rule."),
        ("Which law protects patients&rsquo; personal data in the Philippines?",
         ["RA 11223", "RA 10173, the Data Privacy Act", "RA 7875", "RA 9165"], 1,
         "The Data Privacy Act of 2012."),
        ("Is a personal chat account an approved channel for patient data?",
         ["Yes", "No", "Only for photos", "Only on weekends"], 1,
         "Use the facility&rsquo;s approved channels."),
        ("Why are dialysis claims data especially sensitive?",
         ["They are not", "They include diagnoses, hepatitis and HIV results, relationships, and finances", "They are public", "They expire monthly"], 1,
         "Sensitive personal information."),
        ("When you correct a record, what do you keep?",
         ["Only the correction", "The original entry and the audit history of the change", "Nothing", "A verbal note"], 1,
         "Corrections never erase."),
        ("Which document proves a claim was filed once?",
         ["The schedule", "The acknowledgment or claim reference with time stamp", "The agreement form", "The PDD"], 1,
         "An auditor will ask."),
        ("Whose quality standards does PhilHealth use as its reference for maintenance hemodialysis?",
         ["A vendor&rsquo;s", "Its own Circular 2024-0029", "A hospital&rsquo;s", "None"], 1,
         "Quality standards on maintenance hemodialysis."),
        ("When should accreditation renewal reminders be set?",
         ["On the expiry date", "Well before expiry, for example at 90, 60, and 30 days", "After expiry", "Never"], 1,
         "A facility reminder practice."),
        ("Who leads the facility&rsquo;s privacy incident response?",
         ["The clerk", "The Data Protection Officer", "The vendor", "The PRO"], 1,
         "Report to the DPO at once."),
    ],
    "terms": [("Sensitive personal information", "Health, financial, and identifying data the Data Privacy Act protects most strictly."),
              ("Minimum necessary", "Only the data a task needs."),
              ("Personal information controller", "The facility that decides how personal data is used."),
              ("DPO", "Data Protection Officer."),
              ("NPC", "National Privacy Commission."),
              ("LTO", "License to Operate.")],
    "readings": [("hmo-ckd-coverage.html", "How HMO coverage fits with PhilHealth for kidney care.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
