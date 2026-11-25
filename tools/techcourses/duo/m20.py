# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 20: Privacy, cybersecurity, and information governance. Written for this course from published sources."""

MODULE = {
    "image_alt": "A padlock resting on a closed laptop beside a backup drive and a paper downtime binder at a nurse station.",
    "objectives": [
        "Apply the Data Privacy Act&rsquo;s rules on sensitive personal information to a dialysis unit.",
        "Explain how a ransomware attack spreads from data to care, and which preparations break each link.",
        "Run a downtime plan with tested offline backups and paper records.",
        "Approve an access matrix based on need to know, including vendors.",
    ],
    "big": """
{{plain:Patient records are like a house key. You give copies only to the people who need to enter, you know where every copy is, and you keep a spare in a safe place in case the lock is changed on you.}}
<p>The picture has a limit. A stolen key can be replaced with a new lock. A stolen medical record cannot be un-stolen, and a locked computer in the middle of a dialysis shift can stop treatment. Privacy and continuity are the same problem seen from two sides.</p>
{{cards:Key terms for this module|Sensitive personal information::Under the Data Privacy Act, information such as health records that needs extra protection.|Personal data breach::Loss, theft, or unauthorized access to personal data.|Ransomware::Malicious software that locks systems and demands payment.|Downtime::Time when computer systems cannot be used.|Need to know::Access only to the information a role requires.}}
<p>Your work is to limit who sees what, to prepare for the day the computers stop, and to make sure breaches are handled and reported correctly.</p>
""",
    "case": {"title": "The ransom note", "html": """
<p>At 7:20 on a Wednesday at a unit in Santa Rosa, Laguna, the scheduling computer shows a ransom note, and the electronic records will not open. Nineteen patients are on the floor; another 20 are due in the afternoon. The manager calls the owner, Mr. Nestor Aquino, who asks whether they should just pay.</p>
""", "questions": ["What happens on the floor in the next hour?", "Who must be told, and when?", "What should have been ready before today?"]},
    "sections": [
        ("privacy", "The law", "The Data Privacy Act in a dialysis unit", """
<p>Health records are sensitive personal information under Republic Act No. 10173, the Data Privacy Act of 2012. They may be processed only for a lawful purpose, and only as much as that purpose needs.[[dch_ra10173]] The National Privacy Commission (NPC) sets rules for managing and reporting personal data breaches.[[dch_npc1603]] Appoint a data protection officer and keep a register of what personal data the unit holds, where, and who can see it.</p>
<p>Owning the unit does not give an owner the right to read charts. Board reports need counts and rates, not names.</p>
{{key:Owners see aggregated reports. Clinicians see the charts they need.}}
"""),
        ("threats", "Ransomware", "When the computers stop", """
{{fig:duo20a}}
<p>Ransomware attacks on health care have grown. Among 374 attacks on United States health care delivery organizations from 2016 to 2021, the annual number more than doubled, and 44.4% disrupted care, often through system downtime and cancelled appointments.[[duo_neprash2022]] In the first week after an attack, outpatient visits at affected hospitals fell by 22% to 35%.[[duo_neprash2024]] When one system in San Diego was attacked, nearby emergency departments saw more patients and longer waits.[[dch_dameff2023]] These are United States data, but the software and the methods travel.</p>
<p>Each link in the chain has a defense: staff training and two-step login against phishing; offline backups, tested by restoring them, against encryption; a paper downtime kit against lost records; and transfer agreements against cancelled sessions.</p>
{{key:A backup you have never restored is not a backup.}}
"""),
        ("downtime", "Downtime", "The downtime plan", """
<p>Electronic record downtime is associated with patient safety events.[[mro_larsen2018]] A dialysis unit needs a paper kit that lets it treat safely without computers: each patient&rsquo;s current prescription, allergies, access, and serology status printed and updated at a set interval; blank treatment sheets; and a procedure for entering paper records once systems return. Practice it twice a year.</p>
{{key:Print what you need to dialyze safely, keep it current, and practice using it.}}
"""),
        ("vendors", "Access and vendors", "Who may see what", """
{{fig:duo20b}}
<p>An access matrix lists roles and the data each may see: board reports, patient charts, claims, and payroll. The owner sees board reports, not charts. Billing sees what claims require. Vendors who maintain systems see only what their work needs, under a written agreement that covers security and breach notification. Remove access the day someone leaves.</p>
{{stop:Do not share patient-identifiable data with anyone, including owners and vendors, beyond what their role requires.}}
{{key:Approve the access matrix once a year, and remove leavers the same day.}}
"""),
    ],
    "debrief": ["""
<p><strong>The floor.</strong> Switch to the paper downtime kit; nurses continue sessions with printed prescriptions. Disconnect affected computers from the network. The clinical head decides whether afternoon patients dialyze on paper or transfer.</p>
<p><strong>Who must be told.</strong> The data protection officer starts the breach procedure; notify the NPC and affected patients as the rules require; inform PhilHealth if claims systems are affected; and get IT and legal help. Do not decide on paying a ransom alone or in a hurry.</p>
<p><strong>What should have been ready.</strong> Tested offline backups, a current paper kit, two-step login, and transfer agreements.</p>
"""],
    "skills": {"title": "Access matrix, vendor privacy checklist, and downtime test",
               "intro": "Approve an access matrix, review one vendor agreement, and run a downtime drill.",
               "items": [("Applies the Data Privacy Act rules on sensitive personal information.", False),
                         ("Approves an access matrix with the owner seeing aggregated reports only.", True),
                         ("Confirms offline backups by restoring one.", False),
                         ("Keeps a current paper downtime kit and runs a drill.", False),
                         ("Follows the breach procedure and reporting rules.", True),
                         ("Requires security and breach terms in vendor agreements.", False)],
               "placement": "Ask when the unit last restored a backup, and how long it took."},
    "quiz": [
        ("Under the Data Privacy Act, health records are:",
         ["Public information", "Sensitive personal information", "Owned by the unit owner", "Free to share with vendors"],
         1, "They need extra protection and lawful, proportionate processing."),
        ("Among 374 ransomware attacks on US health care organizations, what share disrupted care?",
         ["About 4%", "About 44%", "About 90%", "None"],
         1, "44.4% disrupted care delivery."),
        ("What makes a backup trustworthy?",
         ["It is expensive", "It is offline and has been restored in a test", "It is on the same computer", "It is labeled"],
         1, "Only a tested restore proves a backup works."),
        ("What should the owner see from patient records?",
         ["Full charts", "Aggregated reports, not names", "Any chart on request", "Nothing at all"],
         1, "Board reports need counts and rates."),
        ("During downtime, how do nurses continue dialysis safely?",
         ["Guess the prescription", "Use the current paper downtime kit", "Stop all sessions", "Ask patients"],
         1, "A printed kit keeps care safe."),
        ("A vendor maintains the record system. What should the agreement include?",
         ["Unlimited access", "Security terms and breach notification, with access limited to the work", "No terms", "Access to payroll"],
         1, "Vendors get need-to-know access under written terms."),
    ],
    "terms": [("Data protection officer", "The person responsible for the unit&rsquo;s compliance with the Data Privacy Act.")],
    "readings": [],
    "calcs": [],
}


def _balance(quiz):
    """Spread the keyed answers across A to D, deterministically (same as tools/techcourses/uom/quizutil.py)."""
    out = []
    for i, (stem, opts, ans, why) in enumerate(quiz):
        opts = list(opts)
        target = (i * 3 + 1) % 4
        if target != ans:
            opts[target], opts[ans] = opts[ans], opts[target]
        out.append((stem, opts, target, why))
    return out


MODULE["quiz"] = _balance(MODULE["quiz"])
