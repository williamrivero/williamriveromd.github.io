# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 11: Digital Custody: Access, Audit Trails, and Backups. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer and an IT staff member reviewing a user access list on a screen.",
    "objectives": [
        "Explain why every user needs an individual account and why shared logins defeat custody.",
        "Assign access by role and remove it promptly at departure.",
        "Run a monthly access review and document each finding and action.",
        "Recognize audit-trail signals worth escalating, and escalate without confronting the user.",
        "Explain why a backup must be test-restored with its audit metadata.",
    ],
    "big": """
{{plain:On paper, custody means a locked room, a key, and a sign-out sheet. Think of the electronic record as a building with a thousand doors. Each user carries a key card, and every door logs whose card opened it and when. The log is only useful if every card belongs to one person.}}
<p>The picture is useful, and it has one limit. In a real building, a stranger walking the halls is noticed. In an electronic record, someone who opens a chart they have no reason to see looks exactly like someone doing their job. The only witness is the log, and the log is only read if someone decides to read it.</p>
<p>The audit trail is the electronic equivalent of fingerprints on a folder: it shows who opened a record, when, and what they changed. It works only if every user has their own account, and only if someone looks.</p>
{{cards:Key terms for this module|Electronic medical record (EMR)::The digital record of patient care within one facility or unit.|Role-based access::Permissions assigned by job role, so each person sees what their work needs.|Audit trail::The system log of who viewed or changed a record, and when.|Access review::A regular check that every active account belongs to a current staff member with the right role.|Offboarding::Removing access when someone leaves or changes role.|Joint administrative order (JAO)::An order issued jointly by the Department of Health and the Philippine Health Insurance Corporation.}}
""",
    "case": {"title": "The monthly review", "html": """
<p>On the first Monday of the month, you sit down with Mr. Paolo Navarro from IT to review the ten active accounts in your unit&rsquo;s records system. Three things turn up.</p>
<ul>
<li>Nurse Angelica Robles resigned three weeks ago. Her account is still active, and it was last used four days ago.</li>
<li>An account named &ldquo;station2&rdquo; has no owner. Mr. Navarro explains that the nurses on the floor share it so they do not have to log in and out between patients.</li>
<li>Ms. Josephine Aguilar, a claims clerk, opened the full clinical notes of Mr. Ramon Aguilar, a patient who shares her surname, three times last week. She has no claims work pending on his account.</li>
</ul>
""", "questions": ["What happens to each account, and how soon?",
                  "Do you speak to Ms. Aguilar about what you found?",
                  "What do you document?"]},
    "sections": [
        ("access", "Access", "One person, one account, one reason to look", """
<p>Every user has an individual account. Shared logins destroy attribution, and they fall short of the security safeguards the National Privacy Commission (NPC) expects for personal data.[[mro_npc2023_06]] If ten nurses share &ldquo;station2,&rdquo; an entry made under it could have been made by any of them, and so, in practice, by none of them.</p>
<p>Access follows role. A technician does not need social-work notes. A claims clerk needs session and billing data, not full clinical narratives. A nurse needs the clinical record of the patients she treats. Staff open a record only when their work requires it. Curiosity, concern for a neighbor, and &ldquo;I was just checking how he is&rdquo; are not reasons.</p>
<div class="table-wrap"><table>
<thead><tr><th>Role</th><th>Usually needs</th><th>Usually does not need</th></tr></thead>
<tbody>
<tr><td>Dialysis nurse</td><td>Clinical record of patients on her shift</td><td>Billing details</td></tr>
<tr><td>Technician</td><td>Treatment parameters, machine and dialyzer records</td><td>Social-work and psychiatric notes</td></tr>
<tr><td>Claims clerk</td><td>Sessions, Annex A, billing, eligibility</td><td>Full clinical narratives</td></tr>
<tr><td>Records officer</td><td>Broad access for custody tasks, all of it logged</td><td>Authority to edit clinical content</td></tr>
</tbody></table></div>
<h3>The monthly access review</h3>
<p>Monthly, or as local policy says, the records officer reviews the user list with IT and the unit manager. Is everyone still employed? Is each role still accurate? Are any accounts dormant? Remove access <strong>promptly at departure</strong>, on the last working day, and document it. A nurse who moves to another unit in the same company changes role; her old access goes too.</p>
{{call:&ldquo;Just use my password while I&rsquo;m on leave&rdquo; is a security incident, not a favor. Decline politely and report it. The fix is a properly authorized temporary account, not a borrowed one.}}
"""),
        ("trail", "The audit trail", "Reading the audit trail", """
{{fig:mro11_audit}}
<p>Most audit-trail entries are ordinary work. A few patterns are worth a closer look.</p>
<ul>
<li>Access to a patient with no scheduled care, claim, or request that explains it.</li>
<li>A user opening relatives&rsquo;, neighbors&rsquo;, or coworkers&rsquo; records.</li>
<li>Bulk viewing or exporting of many records.</li>
<li>Access at odd hours unrelated to the user&rsquo;s shift.</li>
<li>Changes to signed entries, especially near an inspection or a complaint.</li>
<li>A departed user&rsquo;s account still in use.</li>
</ul>
<p>Each of these has innocent explanations. A nurse may have been asked by the physician to check a result. A claims clerk may share a surname with a patient by coincidence. That is exactly why you do not decide. Escalate to the data protection officer (DPO) and the unit manager, with the audit extract. Do not confront the user or investigate alone. A confrontation can warn someone who has done wrong, embarrass someone who has not, and spoil an investigation either way.</p>
<h3>Devices and backups</h3>
<p>Downloads to personal phones, laptops, or flash drives multiply the places a breach can happen. A photo of a run sheet sent through a messaging app to &ldquo;check something at home&rdquo; is a copy of health data on a device the unit does not control. Use facility-approved storage and transmission only.</p>
<p>IT owns backups, but records staff have a part to play. During a tested recovery, confirm that restored records <strong>and their audit metadata</strong> come back intact: the entries, their authors, their timestamps, and the trail of corrections. A backup that restores the text but loses who wrote it has lost the record&rsquo;s value as evidence. A backup that has never been restored is a hope, not a control.</p>
"""),
        ("national", "The national picture", "Why clean data matter beyond the unit", """
<p>Department of Health and Philippine Health Insurance Corporation (PhilHealth) Joint Administrative Order (JAO) 2021-0002 mandates national health data standards for interoperability, and data submitted to the national health data repository must conform to them.[[mro_jao2021]] PhilHealth is also moving providers toward certified electronic medical records (EMRs) and real-time submission. Its primary-care clinics under the Yaman ng Kalusugan Program (YAKAP) had to move to PhilHealth-certified EMR providers by July 1, 2026.[[mro_ph2025emr]]</p>
<p>That is not yet a dialysis rule, but it shows the direction. Clean identifiers, coded fields, and audit-ready records will increasingly be checked by machines, not only by inspectors. A unit whose records are tidy today will find that transition far easier.</p>
{{key:Attribution is the whole point of an audit trail. Shared accounts erase it, dormant accounts invite misuse, and an unread trail protects no one.}}
"""),
    ],
    "debrief": ["""
<p><strong>Nurse Robles&rsquo;s account.</strong> Disable it today and document it. Because it was used after she left, escalate that use to the DPO and the unit manager with the audit extract. Someone used her account four days ago, and the unit needs to know who.</p>
<p><strong>&ldquo;station2.&rdquo;</strong> Retire it and issue individual accounts. Work with IT and the charge nurse on a fast way for nurses to switch users between patients, because the shared account exists to solve a real problem, and the problem will return if nothing replaces it.</p>
<p><strong>Ms. Aguilar.</strong> No, you do not speak to her. The access may be innocent, or it may be a relative looking at a family member&rsquo;s record. Escalate the pattern to the DPO and the unit manager with the extract. They decide the next steps.</p>
<p><strong>What you document.</strong> The review date, who took part, each finding, the action taken, who approved it, and the date it was completed.</p>
<p>Each finding had a reasonable-sounding story behind it: a resignation not yet processed, a workaround for slow logins, a shared surname. Part of your role is to look past the story to the log, and to make each month&rsquo;s review shorter than the last.</p>
"""],
    "skills": {"title": "Access review and audit-trail escalation",
               "intro": "Run a mock access review on a fictional user list with your preceptor and IT.",
               "items": [
                   ("Matches every active account to a current staff member and role.", False),
                   ("Identifies dormant, departed, and shared accounts.", False),
                   ("Removes access on departure and documents it.", True),
                   ("Escalates unusual access to the DPO and manager with an audit extract, without confronting the user.", True),
                   ("Refuses shared credentials and proposes a proper alternative.", True),
                   ("States what a test restore must show beyond the record text.", False),
               ],
               "placement": "With IT, list every active account in your records system and match it to the staff roster."},
    "terms": [("EMR", "Electronic medical record."), ("Role-based access", "Permissions assigned by job role."),
              ("Audit trail", "The log of who viewed or changed a record."), ("Access review", "A regular check of active accounts against staff and roles."),
              ("Offboarding", "Removing access when someone leaves."),
              ("JAO", "Joint Administrative Order."), ("YAKAP", "Yaman ng Kalusugan Program, PhilHealth&rsquo;s primary-care benefit.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["11"])
