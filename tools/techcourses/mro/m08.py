# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 08: Privacy, Patient Rights, and Release of Information. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer at a release counter politely checking a woman's written authorization and ID card.",
    "objectives": [
        "Explain why health information is sensitive personal information under Philippine law.",
        "Process a release request through identity, authority, purpose, scope, and channel, then log it.",
        "Handle access and correction requests as rights.",
        "Escalate a possible breach within the hour and preserve its evidence.",
    ],
    "big": """
{{plain:A dialysis chart holds a person&rsquo;s diagnoses, infections, finances, and family contacts. Released to the wrong person, it can cost a patient a job, a relationship, or their safety.}}
<p>The law treats it accordingly. Under the Data Privacy Act, health information is sensitive personal information, and processing it needs a lawful basis, proportionality, and safeguards.[[dch_ra10173]] Breaches are not hypothetical in Philippine health care: in September 2023 PhilHealth itself suffered a ransomware attack that forced manual operations and prompted an investigation by the National Privacy Commission (NPC).[[mro_ph2023medusa]]</p>
{{cards:Key terms for this module|Sensitive personal information::Under the Data Privacy Act, includes health information.|Data subject::The person the information is about.|Minimum necessary::Releasing only what the purpose requires.|Data protection officer (DPO)::Data protection officer.|Personal information controller (PIC)::Personal information controller.|Data Breach Notification Management System (DBNMS)::The NPC&rsquo;s Data Breach Notification Management System.}}
""",
    "case": {"title": "The sister and the wrong email", "html": """
<p>At 1:50 p.m. a caller says she is the sister of fictional patient SIM-041 and asks for the complete chart sent to her personal email. No authority is on file. At 2:10 p.m. a colleague tells you she emailed a laboratory page with a patient identifier and results to a similarly named outside address at 2:00 p.m.</p>
""", "questions": ["What do you tell the caller, and what do you log?",
                  "What do you do about the misdirected email, and by when?",
                  "Who decides whether the NPC must be notified?"]},
    "sections": [
        ("five", "Five checks", "Five checks before any release", """
{{fig:mro08_checks}}
{{flow:Before you release anything|Identity::Is the requester who they claim to be? Verify with approved identifiers, in person or through an independently trusted channel.|Authority::On what basis may they receive it? The patient, a representative with written authority, a receiving facility for continuity of care, PhilHealth for a claim, a court order, or the DOH for inspection.|Purpose::Why do they need it?|Scope::The minimum necessary for that purpose.|Channel::A verified, approved route: pickup with ID, the facility&rsquo;s secure email or portal, or a sealed courier. Never a personal email address or an unapproved messaging app.}}
<p>Then log it: what was sent, to whom, by whom, when, under what authority, and through which channel. Subpoenas, court orders, media or police requests, relatives without documented authority, and anything unfamiliar go to the data protection officer (DPO) or counsel; you log and route.</p>
"""),
        ("rights", "Patient rights", "Access and correction are rights", """
<p>Patients may ask for copies of their own records and ask that errors be corrected. These requests also catch real mistakes: in a survey of 22,889 patients who read their visit notes, 21.1% reported a perceived mistake, and 42.3% of those judged it serious.[[mro_bell2020]] Log the request, verify identity, route a correction request to the clinical author through the correction workflow, and tell the patient the outcome. Never delete or overwrite the disputed entry yourself.</p>
"""),
        ("breach", "A possible breach", "The first hour", """
{{fig:mro08_hour}}
<p>A misdirected email, a lost logbook, an unlocked records room, unexplained access in the audit trail: report it internally <strong>at once</strong>, within the hour of discovery, to the DPO. Write down the facts (what, who, when, how discovered), protect logs and devices, and support containment, such as asking the wrong recipient to delete and confirm in writing. Do not investigate alone, and do not contact affected patients yourself.</p>
<p>The personal information controller (PIC), through its breach response team and advised by the DPO, decides whether notification is required. Under NPC Circular 16-03, notification to the Commission and to affected data subjects is due within 72 hours of knowledge of, or reasonable belief in, a breach that requires notification, based on the information available even if the full extent is not yet known.[[dch_npc1603]][[mro_npc_irr]] Notifications are filed through the NPC&rsquo;s Data Breach Notification Management System (DBNMS), and filing a request there does not pause the clock.[[mro_npc2026dbnms]]</p>
{{call:Do not wait for proof of harm. The 72-hour clock runs from the organization&rsquo;s knowledge, so an hour lost at the front line is an hour taken from the controller.}}
"""),
    ],
    "debrief": ["""
<p><strong>The caller.</strong> Explain politely that the unit must verify identity and authority first and that records are released only through approved channels. Ask for the patient&rsquo;s written authorization or documented legal authority. Log the request. Release nothing yet.</p>
<p><strong>The email.</strong> Escalate to the DPO immediately, by 2:15 p.m. Record the facts: sent 2:00, reported 2:10, the content, the recipient. Preserve the sent item. If notification is required, the controller&rsquo;s 72-hour window from the organization&rsquo;s knowledge ends about 2:15 p.m. three days later.</p>
<p><strong>Who decides.</strong> The personal information controller, through its breach response team, advised by the DPO.</p>
"""],
    "skills": {"title": "Release decision and breach escalation",
               "intro": "Role-play a release request and a misdirected disclosure with a preceptor and a role player.",
               "items": [
                   ("Verifies identity and authority before any disclosure.", True),
                   ("Releases only the minimum necessary through an approved channel and logs it.", False),
                   ("Routes subpoenas and unfamiliar requests to the DPO or counsel.", False),
                   ("Escalates a possible breach to the DPO within the hour and preserves evidence.", True),
                   ("Does not contact affected patients or investigate alone.", False),
               ],
               "placement": "Find your unit&rsquo;s release log and DPO contact. Check that both are current."},
    "terms": [("Sensitive personal information", "Under the Data Privacy Act, includes health information."),
              ("Data subject", "The person the information is about."), ("Minimum necessary", "Only what the purpose requires."),
              ("DPO", "Data protection officer."), ("PIC", "Personal information controller."),
              ("NPC", "National Privacy Commission."), ("DBNMS", "Data Breach Notification Management System.")],
    "readings": [("personal-medical-journal-health-history.html", "Helping patients keep their own health history.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["08"])
