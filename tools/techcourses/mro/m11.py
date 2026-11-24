# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 11: Digital Custody, Access Control, and Audit Trails. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer and an IT staff member reviewing a user access list on a monitor in a clinic office.",
    "objectives": [
        "Apply individual, role-based access to the electronic record.",
        "Run a periodic access review and an offboarding check.",
        "Read an audit trail for unusual access and escalate it without confronting anyone.",
        "Explain why national data standards and certified electronic records make clean identifiers matter beyond the unit.",
    ],
    "big": """
{{plain:On paper, custody means a locked room and a sign-out sheet. In an electronic record, custody means who can see what, and proof of who did.}}
<p>The audit trail is the electronic equivalent of fingerprints on a folder: it shows who opened a record, when, and what they changed. It works only if every user has their own account.</p>
{{cards:Key terms for this module|Electronic medical record (EMR)::Electronic medical record.|Role-based access::Permissions assigned by job role.|Audit trail::The system log of who viewed or changed a record.|Offboarding::Removing access when someone leaves.|Joint administrative order (JAO)::Joint Administrative Order.}}
""",
    "case": {"title": "The monthly review", "html": """
<p>Your monthly access review of a ten-user list turns up three things: a nurse who resigned three weeks ago still has an active account; a shared login named &ldquo;station2&rdquo; is used by whoever is on the floor; and a claims clerk viewed the full clinical notes of a fictional patient who is her relative.</p>
""", "questions": ["What happens to each account, and how soon?",
                  "Do you speak to the claims clerk?",
                  "What do you document?"]},
    "sections": [
        ("access", "Access", "One person, one account, one reason to look", """
<p>Every user has an individual account; shared logins destroy attribution and fall short of the security safeguards the National Privacy Commission (NPC) expects.[[mro_npc2023_06]] Access follows role: a technician does not need social-work notes, and a claims clerk needs session and billing data, not full clinical narratives. Staff open a record only when their work requires it; curiosity is not a reason.</p>
<p>Monthly, or as local policy says, the records officer reviews the user list with IT and the unit manager: everyone still employed, role still accurate, no dormant accounts. Remove access <strong>promptly at departure</strong>, on the last working day, and document it.</p>
{{call:&ldquo;Just use my password while I&rsquo;m on leave&rdquo; is a security incident, not a favor. Decline and report it.}}
"""),
        ("trail", "The audit trail", "Reading the audit trail", """
{{fig:mro11_audit}}
<p>Signals worth escalating: access to a patient with no scheduled care; a user opening relatives&rsquo; or coworkers&rsquo; records; bulk viewing or exporting; access at odd hours unrelated to the shift; changes to signed entries. Escalate to the data protection officer and the unit manager with the audit extract. Do not confront the user or investigate alone.</p>
<p>Downloads to personal phones, laptops, or flash drives multiply the places a breach can happen; use facility-approved storage and transmission only. IT owns backups, but records staff should confirm during a tested recovery that restored records <strong>and their audit metadata</strong> come back intact. A backup that has never been restored is a hope, not a control.</p>
"""),
        ("national", "The national picture", "Why clean data matter beyond the unit", """
<p>DOH&ndash;PhilHealth Joint Administrative Order (JAO) 2021-0002 mandates national health data standards for interoperability, and data submitted to the national health data repository must conform to them.[[mro_jao2021]] PhilHealth is also moving providers toward certified electronic medical records (EMRs) and real-time submission: its primary-care YAKAP clinics had to move to PhilHealth-certified EMR providers by July 1, 2026.[[mro_ph2025emr]] That is not yet a dialysis rule, but it shows the direction. Clean identifiers, coded fields, and audit-ready records will increasingly be checked by machines, not only by inspectors.</p>
{{key:Attribution is the whole point of an audit trail. Shared accounts erase it.}}
"""),
    ],
    "debrief": ["""
<p><strong>Accounts.</strong> Disable the resigned nurse&rsquo;s account today and document it. Retire &ldquo;station2&rdquo; and issue individual accounts.</p>
<p><strong>The clerk.</strong> No. Escalate the event to the DPO and the unit manager with the audit-trail extract; they decide the next steps.</p>
<p><strong>Documentation.</strong> The review date, each finding, the action, who approved it, and the date it was completed.</p>
"""],
    "skills": {"title": "Access review and audit-trail escalation",
               "intro": "Run a mock access review on a fictional user list with a preceptor and IT.",
               "items": [
                   ("Identifies dormant, departed, and shared accounts.", False),
                   ("Removes access on departure and documents it.", True),
                   ("Escalates unusual access to the DPO and manager without confronting the user.", True),
                   ("Refuses shared credentials.", True),
               ],
               "placement": "With IT, list every active account in your records system and match it to the staff roster."},
    "terms": [("EMR", "Electronic medical record."), ("Role-based access", "Permissions assigned by job role."),
              ("Audit trail", "The log of who viewed or changed a record."), ("Offboarding", "Removing access when someone leaves."),
              ("JAO", "Joint Administrative Order."), ("YAKAP", "Yaman ng Kalusugan Program, PhilHealth&rsquo;s primary-care benefit.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["11"])
