# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 21: Disasters, emergency coverage, and continuity. Written for this course from published sources."""

MODULE = {
    "image_alt": "A dialysis clinic on a flooded street after a typhoon, a small rescue boat bringing patients to a raised entrance while a generator runs.",
    "objectives": [
        "Explain why disasters endanger dialysis patients more than most people.",
        "Map the unit&rsquo;s dependencies and the backup for each.",
        "Secure transfer agreements and patient contact plans before the season starts.",
        "Reopen only through a restart gate.",
    ],
    "big": """
{{plain:For most people a typhoon is three bad days. For a dialysis patient it can be a missed session on Monday, another on Wednesday, and a dangerous potassium level by Thursday. The storm does not have to touch the patient to harm them; it only has to close the unit.}}
<p>The picture has a limit. A storm warning gives days of notice. Patients still cannot dialyze in advance for a week. What preparation can do is move sessions earlier before landfall, keep the unit running or a partner unit ready, and know where every patient is.</p>
{{cards:Key terms for this module|Continuity plan::The unit&rsquo;s plan to keep treating patients, or to move them safely, during a disruption.|Dependency map::A picture of what the unit needs to operate and the backup for each.|Transfer agreement::A written arrangement with a partner unit to accept patients.|Restart gate::The checks that must pass before reopening after a disaster.}}
<p>Your work is to fund and test the plan before the season, and to reopen only when it is safe.</p>
""",
    "case": {"title": "Signal number 3", "html": """
<p>On a Sunday evening, PAGASA raises Tropical Cyclone Wind Signal No. 3 over the province around a unit in Legazpi, Albay, with landfall expected on Monday afternoon. Forty-two patients are scheduled for Monday and Tuesday. The unit&rsquo;s generator was last tested in March, and the patient contact list was last updated in June.</p>
""", "questions": ["What can be done before landfall?", "What does the unit need to stay open, and what if it cannot?", "When will it reopen?"]},
    "sections": [
        ("why", "Why disasters kill", "Why disasters endanger dialysis patients", """
<p>After Hurricane Sandy in 2012, United States dialysis patients in the affected areas had more emergency visits and hospital admissions in the following weeks than in comparable periods.[[uom_kelman2015]] Patients who dialyzed early, before the storm, were less likely to need emergency care and hospitalization afterward.[[dch_lurie2015]] Both studies were observational, but they point to the same practical rule: move sessions earlier before the storm. Asia-Pacific nephrologists have described the same problems after earthquakes, floods, and typhoons in our region.[[uom_gray2015]]</p>
<p>Philippine law requires disaster risk reduction and management (DRRM) planning, and local plans assume that facilities know their own vulnerabilities.[[dch_ra10121]]</p>
{{key:Dialyze early before landfall, then know where every patient is.}}
"""),
        ("dependencies", "Dependencies", "The dependency map", """
{{fig:duo21a}}
<p>List what a session needs and the backup for each: power (generator with fuel for a stated number of days, tested under load), water (supply plan and storage), staff (a call tree and, if needed, a place to stay), supplies (extra stock before the season), patients (current contact list and transport), and records (the paper kit from Module 20). Assign an owner to each line and test it before the season.</p>
{{key:Every dependency has a backup and a person who has tested it.}}
"""),
        ("transfer", "Transfer agreements", "Transfers and the patient list", """
<p>Sign transfer agreements with at least one partner unit outside your likely flood or storm zone, with contacts and the paperwork each patient needs: prescription, serology, and access. Keep each patient&rsquo;s emergency information current and give patients an emergency card and a three-day emergency diet plan prepared by the dietitian and clinicians. During and after a storm, account for every patient by name.</p>
<p>Use the continuity planner to estimate how many sessions you can deliver at reduced capacity and how many must move.</p>
{{key:Before the season: current contacts, signed partners, and a card in every patient&rsquo;s hand.}}
"""),
        ("restart", "Restart", "Reopen through a gate", """
{{fig:duo21b}}
<p>Reopening after a disaster follows the same logic as opening day. The building is safe, power is stable, the water is tested and released by the technical lead, the machines are checked, and enough staff are present. Until then, keep transfers going. When the unit reopens, the attending nephrologists triage patients by clinical urgency, assessing potassium, fluid, breathing, and symptoms, rather than following a simple order of missed sessions.</p>
{{stop:Do not reopen on untested water or unchecked machines, however long the patients have waited.}}
{{key:Reopen through the gate, not around it.}}
"""),
    ],
    "debrief": ["""
<p><strong>Before landfall.</strong> Ask the nephrologists to move Monday and Tuesday sessions earlier, to Sunday night and Monday morning where possible. Test the generator now, top up fuel, update contacts, and confirm the partner unit.</p>
<p><strong>To stay open.</strong> Power, water, staff, and supplies. If any fails, transfer patients by name.</p>
<p><strong>Reopening.</strong> When the restart gate passes, not before; the order of patients set by physician-led triage of clinical urgency.</p>
"""],
    "skills": {"title": "Continuity dependency map, transfer record, and restart gate",
               "intro": "Build a dependency map, a transfer agreement checklist, and a restart gate for your unit.",
               "items": [("Explains why disasters endanger dialysis patients, with the observational evidence.", False),
                         ("Maps every dependency with a tested backup and an owner.", False),
                         ("Keeps current patient contacts and emergency cards.", False),
                         ("Holds signed transfer agreements outside the likely hazard zone.", False),
                         ("Reopens only after water is released by the technical lead and machines are checked.", True),
                         ("Accounts for every patient by name during and after a disaster.", True)],
               "placement": "Call five patients from the contact list and check that the numbers still work."},
    "quiz": [
        ("What did Lurie and colleagues find about dialysis before Hurricane Sandy?",
         ["It made no difference", "Early dialysis before the storm was associated with fewer emergency visits and admissions", "It increased deaths", "It was impossible"],
         1, "Observational evidence supports dialyzing early before landfall."),
        ("Which is a dependency that needs a tested backup?",
         ["Power", "Wall paint", "Waiting-room magazines", "Uniform color"],
         0, "Power stops the blood pump and the water system."),
        ("Where should a partner unit for transfers ideally be?",
         ["Next door, in the same flood zone", "Outside the likely flood or storm zone", "Abroad", "Anywhere"],
         1, "A partner in the same hazard zone fails at the same time."),
        ("After a typhoon, when can the unit reopen?",
         ["When the owner decides", "When the building, power, water release, machines, and staff checks pass", "Immediately", "After one week regardless"],
         1, "The restart gate mirrors opening day."),
        ("Who decides the order in which patients are dialyzed after reopening?",
         ["The owner", "The attending nephrologists", "The patients", "The supplier"],
         1, "Priority is a clinical triage decision based on urgency, not a simple missed-session order."),
        ("When should the generator be tested?",
         ["Only after it fails", "On a schedule under load, and before the storm season", "Never", "Once at purchase"],
         1, "Untested backups fail when needed."),
    ],
    "terms": [("PAGASA", "The Philippine Atmospheric, Geophysical and Astronomical Services Administration, which issues storm warnings.")],
    "readings": [("typhoon-disaster-preparedness-dialysis.html", "Typhoon preparedness for dialysis patients.")],
    "calcs": ["calc-dialysis-continuity-planner.html"],
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
