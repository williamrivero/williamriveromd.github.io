# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 01: Role, Designation, and Sources of Authority. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer and a unit manager reviewing a binder labeled role file at a desk in a dialysis clinic office.",
    "objectives": [
        "Tell a licensing rule from a payer rule, a professional guideline, and a privacy law.",
        "Read any rule for its issuer, scope, and effective date before acting on it.",
        "Assemble the role file an inspector expects: designation, contract, training, manual, and deputy.",
        "Route coding, claims, privacy, and destruction decisions to their owners, each with a named alternate.",
    ],
    "big": """
{{plain:A dialysis unit answers to four referees at once. One decides whether the unit may operate, one decides whether it gets paid, one sets what good practice looks like, and one decides whether patient information was handled lawfully. Each writes its own rulebook and revises it on its own schedule.}}
<p>The picture has a limit. Referees in a game share one rulebook; these four do not. A records officer who confuses them will, sooner or later, apply last year&rsquo;s payer rule to this year&rsquo;s claim, or treat a professional recommendation as if it were law. The habit this module builds is simple: before acting on any instruction, find who issued it, whom it covers, and when it took effect.</p>
{{cards:Key terms for this module|Medical records officer (MRO)::Medical records officer, the person designated to keep the unit&rsquo;s records.|Designation::The written act that names a person to a role.|Issuance::A formally numbered order, circular, or advisory.|Standard operating procedure (SOP)::Standard operating procedure; the facility&rsquo;s local translation of the rules.|Personal information controller (PIC)::Personal information controller; the organization that decides how personal data are used and owns breach-notification decisions.|Data protection officer (DPO)::Data protection officer.}}
""",
    "case": {"title": "The binder before the inspection", "html": """
<p>Your 22-station freestanding unit expects a Department of Health (DOH) licensing visit in three weeks. The unit manager hands you a thin binder labeled &ldquo;MRO&rdquo; containing a two-year-old memo naming your predecessor and a printout of an old Philippine Health Insurance Corporation (PhilHealth) circular. She asks whether you are &ldquo;covered.&rdquo; A colleague at a 16-station unit across town says their center skipped designating anyone because &ldquo;the rule only applies above 20 stations.&rdquo;</p>
""", "questions": ["What belongs in your role file, and what is missing from this one?",
                  "Is your colleague right about the 20-station threshold?",
                  "Who signs off on a coding query, a claim, a privacy incident, and a destruction request in your unit?"]},
    "sections": [
        ("owns", "What the MRO owns", "Custody, not content", """
<p>The medical records officer (MRO) runs the custody workflow: capturing and retrieving records, monitoring completeness, validating coded fields within delegated authority, coordinating registry returns, and keeping the evidence an inspector will ask for. The MRO does <strong>not</strong> own clinical content. A physician or nurse who recorded a fact is its author, and only they, through the clinical correction workflow, may change it. The facility head authorizes claims submission, system access, releases, and destruction under approved rules.</p>
<p>The Philippine Society of Nephrology (PSN) hemodialysis guidelines describe the MRO&rsquo;s duties as coding, custody, registry coordination, completeness for the Department of Health (DOH), and implementation of the records manual, and recommend training in the International Classification of Diseases, 10th Revision (ICD-10), basic records management, and hospital health information management (HIM).[[psn2024]] That is strong professional guidance, not law.</p>
{{key:You keep the record. You never author the clinical facts inside it.}}
"""),
        ("rulebooks", "Four rulebooks", "Read every rule for issuer, scope, and date", """
{{fig:mro01_referees}}
<div class="table-wrap"><table>
<thead><tr><th>Referee</th><th>What it decides</th><th>Example issuance</th></tr></thead>
<tbody>
<tr><td>DOH (licensing)</td><td>Whether the unit may operate</td><td>Administrative Order 2012-0001 and the License to Operate (LTO) assessment tool[[doh2012]][[dch_doh_rao_tool]]</td></tr>
<tr><td>PhilHealth (payment)</td><td>Whether, and how much, the unit is paid</td><td>Circular 2024-0023 on the 156-session HD package[[dch_philhealth2024]]</td></tr>
<tr><td>PSN (professional)</td><td>What good practice looks like</td><td>March 2024 HD guidelines[[psn2024]]</td></tr>
<tr><td>NPC (privacy)</td><td>Whether personal data were handled lawfully</td><td>Data Privacy Act and NPC Circular 16-03[[dch_ra10173]][[dch_npc1603]]</td></tr>
</tbody></table></div>
<p>Before acting on any instruction, check three things. <strong>Issuer</strong>: who wrote it? <strong>Scope</strong>: does it cover a hospital-based unit, a freestanding unit, public entities only, or everyone? <strong>Effective date</strong>: which version governs this service date? PhilHealth changed the HD rate twice in 2024, so a session on September 30, 2024 and one on October 9, 2024 fall under different rates.[[mro_ph2025news]]</p>
<p>The facility&rsquo;s standard operating procedure (SOP) translates these sources into local steps with owners, forms, and logs. When an SOP and a newer issuance disagree, the issuance wins: log the gap and raise it for revision.</p>
"""),
        ("rolefile", "The role file", "What an inspector expects to see", """
<p>The posted DOH assessment tool for hemodialysis clinics lists a designated MRO, a notarized employment contract reflecting MRO duties, and a medical-records-management training certificate for facilities with more than 20 stations.[[dch_doh_rao_tool]] Read the threshold carefully: it applies to the training certificate, not to the designation itself. Confirm the current tool, and which training providers&rsquo; certificates are accepted, with your Center for Health Development licensing office.</p>
{{flow:A complete role file|Designation memo::Signed, current, naming you and your deputy.|Contract::Notarized, with MRO duties written in.|Training evidence::The records-management certificate where required, plus ICD-10 and HIM training per PSN.|Records manual::Approved, with its revision date.|Source register::Each rule with issuer, scope, effective date, owner, and next review.|Decision map::Who decides coding, claims, privacy, and destruction, each with an alternate.}}
"""),
        ("routing", "Who decides", "Log, preserve, and route", """
<p>Every records decision belongs to someone. Clinical diagnosis and authentication belong to the treating clinician, escalating to the Dialysis Clinical Head. Indexing and deficiency tracking belong to you. Code selection belongs to the authorized coder or claims lead, with the physician answering diagnostic questions. Claims submission belongs to authorized claims staff and the facility signatory. Whether a breach is notified to the National Privacy Commission (NPC) is decided by the personal information controller (PIC), advised by the data protection officer (DPO).[[dch_npc1603]] Destruction needs the facility head, counsel, and, for public entities, the National Archives process.[[mro_ra9470]]</p>
{{call:When a records problem could affect the next treatment, escalate to the clinical team before that session. When it could affect a person&rsquo;s privacy, escalate to the DPO within the hour of discovery. Everything else goes in the deficiency log with an owner and a due date. Local protocol sets the exact times; the attending nephrologist and the DPO are always the right people to ask when unsure.}}
"""),
    ],
    "debrief": ["""
<p><strong>The role file.</strong> Replace the predecessor&rsquo;s memo with a current designation naming you and a deputy; add your notarized contract with MRO duties, the records-management training certificate (required here because the unit exceeds 20 stations), ICD-10 and HIM training evidence, the approved manual with its revision date, and a current source register. Ask the licensing lead to confirm accepted certificates with the regional office and record the answer.</p>
<p><strong>The colleague.</strong> Wrong. The threshold concerns the training certificate; the designation applies regardless of size.</p>
<p><strong>The decision map.</strong> Name the owner and alternate for each: coding query (coder or claims lead, with the physician), claim (claims staff and signatory), privacy incident (DPO, with the PIC deciding on notification), destruction (facility head and counsel).</p>
"""],
    "skills": {"title": "Role file and decision map",
               "intro": "Assemble a role file and source register for a fictional unit with a preceptor.",
               "items": [
                   ("States the issuer, scope, and effective date for each rule in the register.", True),
                   ("Distinguishes the designation requirement from the training-certificate threshold.", True),
                   ("Produces a complete role file: designation, contract, training, manual, deputy.", False),
                   ("Names an owner and an alternate for coding, claims, privacy, and destruction decisions.", True),
                   ("Flags an SOP that conflicts with a newer issuance and routes it for revision.", False),
               ],
               "placement": "Find your own unit&rsquo;s role file and source register. List every rule that has no recorded effective date."},
    "terms": [("MRO", "Medical records officer."), ("Designation", "A written act naming a person to a role."),
              ("Issuance", "A formally numbered order, circular, or advisory."), ("SOP", "Standard operating procedure."),
              ("PIC", "Personal information controller."), ("DPO", "Data protection officer."),
              ("LTO", "License to Operate, issued by the DOH.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["01"])
