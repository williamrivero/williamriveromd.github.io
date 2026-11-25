# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 3: Philippine licensing and the compliance register. Written for this course from published sources."""

MODULE = {
    "image_alt": "Official folders, a tabbed binder, a rubber stamp, and a desk calendar with three dates circled.",
    "objectives": [
        "Distinguish the Department of Health (DOH) license, PhilHealth accreditation, Philippine Society of Nephrology (PSN) attestation, and local permits, and what each one covers.",
        "Build a compliance register in which every line has a requirement, evidence, a named owner, and an expiry alert.",
        "Use change control when a rule, a station count, or an appointee changes.",
        "Prepare for inspection by testing the register before an inspector does.",
    ],
    "big": """
{{plain:Running a licensed unit is like keeping a car legal on the road. The registration, the insurance, the emissions test, and the driver&rsquo;s license are separate papers from separate offices, with separate expiry dates. A valid registration does not cover an expired license.}}
<p>The picture has a limit. A car can be parked while its papers are renewed. A dialysis unit cannot pause, because its patients cannot. That is why compliance in a dialysis unit is a system with alerts and owners, not a drawer of certificates.</p>
{{cards:Key terms for this module|License to operate::The Department of Health (DOH) authority for the facility to provide hemodialysis at a stated address and scope.|Accreditation::PhilHealth recognition that lets the facility file claims for its members.|Attestation::The Philippine Society of Nephrology (PSN) process that reviews a unit against its guidelines.|Compliance register::One list of every requirement, its evidence, its owner, and its expiry.|Change control::A rule that a change in stations, appointees, or regulations triggers a review before it takes effect.}}
<p>Your work here is to see the layers clearly, to know which ones carry the force of law, and to make sure that nothing expires because nobody was assigned to watch it.</p>
""",
    "case": {"title": "Expansion week", "html": """
<p>Ms. Lorna Villanueva owns a 10-station unit in San Fernando, Pampanga. Her contractor finishes four new stations on November 3. The unit&rsquo;s PhilHealth accreditation renewal is due the same month, and the clinical head&rsquo;s contract ends December 31.</p>
<p>The manager suggests opening the new stations right away, &ldquo;because the machines are already here and patients are waiting,&rdquo; and filing the paperwork afterward.</p>
""", "questions": ["What does the license currently allow?", "Which three items in the register are about to collide?",
                  "What is the safe order of steps?"]},
    "sections": [
        ("layers", "Four layers", "Four layers, four sets of rules", """
{{fig:duo03a}}
<p><strong>The DOH license</strong> is the legal authority to operate. Administrative Order 2012-0001 sets the licensing framework for dialysis facilities, including a permit to construct, personnel, equipment, records, and safety conditions; it limits each nurse to four hemodialysis stations and requires at least one nurse trained in Advanced Cardiovascular Life Support (ACLS) on each shift.[[doh2012]] Dialysis water is governed by a separate order, AO 2013-0003.[[dch_doh2013]] A 2026 Department Circular, No. 2026-0112, issued interim guidelines on licensing hemodialysis clinics; its title is confirmed but its full text was not reviewed for this course, so check it with your Center for Health Development (CHD) before relying on any older form.[[dch_doh2026]]</p>
<p><strong>PhilHealth accreditation</strong> lets the facility claim the hemodialysis package for members.[[dch_philhealth2023acc]] It has its own renewal cycle and filing deadlines.[[dch_philhealth_pa2025]] <strong>PSN attestation</strong> is a professional-society review against its guidelines, not a law.[[dch_psn_attest2020]][[psn2024]] <strong>Local permits</strong> come from your city or municipality: business, building, fire, sanitation, and waste.</p>
<p>Where a society guideline and a binding rule differ, follow the binding rule. The PSN guideline allows one nurse to six patients under conditions with an assistant; the DOH order sets one nurse to four stations. A society provision does not relax a licensing condition. Plan to the DOH limit and ask your CHD in writing if you think a different rule applies.</p>
{{key:The license is law, accreditation is a payer contract, attestation is professional review, and permits are local law. Each expires on its own date.}}
"""),
        ("register", "The register", "A compliance register that proves itself", """
{{fig:duo03b}}
<p>A register is one table. Each line names a requirement, the evidence that it is met, the person responsible, the expiry or next check date, and an alert set well before that date. Keep the evidence one click away, not &ldquo;in the admin office.&rdquo;</p>
<div class="table-wrap"><table>
<thead><tr><th>Requirement</th><th>Evidence</th><th>Owner</th><th>Expiry or next check</th><th>Alert</th></tr></thead>
<tbody>
<tr><td>DOH license to operate</td><td>Current license; approved station count</td><td>Manager</td><td>Annual renewal</td><td>90 days before</td></tr>
<tr><td>PhilHealth accreditation</td><td>Accreditation certificate; filing receipt</td><td>Manager</td><td>Per PhilHealth cycle</td><td>90 days before</td></tr>
<tr><td>Clinical head appointment</td><td>Signed contract; scope; sites</td><td>Owner</td><td>Contract end</td><td>120 days before</td></tr>
<tr><td>Water testing</td><td>Signed results by sampling point</td><td>Technical lead</td><td>Per schedule</td><td>Missed result = same-day alert</td></tr>
<tr><td>Fire safety inspection</td><td>Certificate; drill record</td><td>Manager</td><td>Annual</td><td>60 days before</td></tr>
</tbody></table></div>
<p>The lead times in the table are this course&rsquo;s suggestions. Set yours by how long each renewal really takes in your region.</p>
{{key:Every line needs evidence, an owner, and an alert. A requirement with no owner is a requirement nobody is meeting.}}
"""),
        ("change", "Change control", "Change control: when something moves", """
<p>Most compliance failures start with a good change made in the wrong order: new stations opened before the license covers them, a new clinical head who starts before the appointment is filed, or a supplier change that slips past the technical lead. Change control is a simple habit. Before a change takes effect, ask which register lines it touches and update them first.</p>
<p>Three changes always trigger a review: a change in station count or address, a change in any appointee named on the license or accreditation, and a new or amended regulation or circular. The last one needs someone to watch issuances. Assign it, and have that person bring a one-line summary of anything new to each board meeting.</p>
{{stop:Do not treat patients on stations the license does not cover, even if the machines are installed and patients are waiting.}}
{{key:Update the register before the change, not after.}}
"""),
        ("inspection", "Inspection", "Inspect yourself first", """
<p>An inspector usually follows one patient and one machine through the unit and asks to see the evidence at each step. You can do the same. Once a quarter, pick a patient record and a machine at random and trace them: the patient&rsquo;s consent and serology results, the session records, the nurse&rsquo;s competency, the machine&rsquo;s maintenance log, and the water results for that day.</p>
<p>Write down every gap. A gap you find is a corrective action. A gap an inspector finds is a finding. The work is the same; the consequences are not.</p>
{{key:Run your own tracer every quarter. The best inspection result is one you already knew.}}
"""),
    ],
    "debrief": ["""
<p><strong>What the license allows.</strong> Ten stations at the licensed address. The four new stations cannot be used until the DOH approves the change, whatever the machines and the waiting list say.</p>
<p><strong>The collision.</strong> The station change, the PhilHealth renewal, and the clinical head&rsquo;s contract all fall within two months. Each one affects the others: the accreditation is tied to the licensed facility and its appointees.</p>
<p><strong>The safe order.</strong> File the license amendment with your CHD, renew the clinical head&rsquo;s appointment in writing, file the PhilHealth renewal on time, and only then staff and open the new stations, after the technical lead releases their machines and water.</p>
"""],
    "skills": {"title": "Compliance register with change control",
               "intro": "Build a compliance register for a real or fictional unit with at least twelve lines and test it with one tracer.",
               "items": [("Separates the license, accreditation, attestation, and local permits.", False),
                         ("Gives every line evidence, a named owner, an expiry, and an alert.", False),
                         ("Plans staffing to the DOH station limit and does not use a society provision to relax it.", True),
                         ("Refuses to treat patients on stations the license does not cover.", True),
                         ("Defines the three changes that trigger review.", False),
                         ("Runs one tracer and records each gap as a corrective action.", False)],
               "placement": "Ask your manager for the current license, accreditation, and three permits, and time how long it takes to produce them."},
    "quiz": [
        ("Which document gives a facility the legal authority to provide hemodialysis?",
         ["PSN attestation", "The DOH license to operate", "PhilHealth accreditation", "A business permit alone"],
         1, "The DOH license is the legal authority. Accreditation is a payer relationship; attestation is professional review."),
        ("The PSN guideline and the DOH order give different nurse limits. What should the owner plan to?",
         ["The less strict one", "The binding DOH limit, with written clarification from the CHD if needed", "Whatever the manager prefers", "An average of the two"],
         1, "Society guidance does not relax a binding licensing condition."),
        ("Four stations are installed but not yet on the license. Patients are waiting. What is correct?",
         ["Open them now and file later", "Wait until the license covers them and the technical lead releases them", "Use them only on weekends", "Use them for PhilHealth members only"],
         1, "Treating on unlicensed stations exceeds the approved scope, however urgent the waiting list."),
        ("What must every line in a compliance register have?",
         ["A color code", "Evidence, a named owner, an expiry or next check, and an alert", "The owner&rsquo;s signature", "A peso value"],
         1, "Without an owner and an alert, a requirement quietly expires."),
        ("Which change should always trigger a review of the register before it takes effect?",
         ["New office furniture", "A change in station count or address", "A new uniform color", "A change in the menu for staff"],
         1, "Station count, address, named appointees, and new regulations all touch licensing and accreditation."),
        ("What does a quarterly self-tracer do?",
         ["Replaces the DOH inspection", "Finds gaps before an inspector does, so they become corrective actions", "Proves the unit is perfect", "Is required by PhilHealth"],
         1, "A tracer follows one patient and one machine through the evidence. Gaps found early are cheaper to fix."),
    ],
    "terms": [("Tracer", "An audit that follows one patient or one machine through every record that should exist."),
              ("Corrective action", "A planned fix with an owner, a due date, and proof that it worked.")],
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
