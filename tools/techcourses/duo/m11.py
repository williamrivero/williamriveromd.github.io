# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 11: Water, equipment, and utilities assurance. Written for this course from published sources."""

MODULE = {
    "image_alt": "A reverse osmosis water treatment system with blue pressure vessels and carbon tanks in a bright plant room.",
    "objectives": [
        "Explain why dialysis water must be far purer than drinking water.",
        "Describe the hold-and-release rule and the owner&rsquo;s role in it.",
        "Budget for the whole life cycle of machines and the water system.",
        "Secure power and water backups that keep treatment safe through an outage.",
    ],
    "big": """
{{plain:Drinking water passes through the gut, which acts like a careful customs officer: it lets in what the body needs and stops much of the rest. Dialysis water skips customs. In each session, a large volume of dialysate made from treated water meets the blood across a thin membrane, and small contaminants cross straight into the bloodstream.}}
<p>The picture has a limit. The membrane blocks large particles and most bacteria, but not small chemicals like chlorine-derived chloramines, aluminum, or fragments of bacteria. That is why dialysis water has its own standard and its own testing, and why a single missed test can harm every patient on a shift.</p>
{{cards:Key terms for this module|Reverse osmosis (RO)::The main purification step: water is pushed through a fine membrane that holds back most contaminants.|Carbon tanks::Tanks that remove chlorine and chloramine before the RO.|Endotoxin::Fragments of bacteria that can cause fever and inflammation.|Hold::A stop on use until the qualified person releases the system.|Asset life cycle::The stages of equipment from specification to retirement.}}
<p>Water and machines are where an owner&rsquo;s budget meets a patient&rsquo;s blood most directly. Your work is to fund them fully and to stay out of their release.</p>
""",
    "case": {"title": "Chlorine at 5:15", "html": """
<p>At 5:15 a.m. at a unit in Davao City, the morning chlorine test after the carbon tanks shows a result above the unit&rsquo;s limit. The water technician, Mr. Jomar Alcantara, holds the loop. Twenty-two patients are due from 6:00. The same week, a quote arrived for a new reverse osmosis membrane and an extra carbon tank: 420,000 pesos. The owner, Mrs. Cecilia Uy, had planned to defer it to next year.</p>
""", "questions": ["What happens to the morning shift?", "Why does a chlorine result matter so much?", "What should the board do about the quote?"]},
    "sections": [
        ("water", "Why water kills", "Why dialysis water must be so pure", """
{{fig:duo11a}}
<p>The worst dialysis disasters have been water disasters. In Caruaru, Brazil, in 1996, water contaminated with toxins from algae was used for dialysis, and dozens of patients died of liver failure.[[dch_jochimsen1998]] Elsewhere in Brazil, chlorine and chloramine left in dialysis water caused outbreaks of hemolysis, the destruction of red blood cells.[[dch_calderaro2001]] In both, the cause was a failure of treatment and testing that a working system and an honest log would have caught.</p>
<p>Modern standards, including the ISO standard for dialysis fluids, set limits for chemicals, bacteria, and endotoxin, and the DOH water order sets Philippine testing requirements.[[dch_iso2024]][[dch_doh2013]] The technical lead knows the numbers. The owner needs to know three things: the tests happen on schedule, the results are signed and filed, and a failed or missing result stops treatment.</p>
{{key:A missing test is a failed test. Treat it the same way.}}
"""),
        ("hold", "Hold and release", "The hold-and-release rule", """
<p>When a water result fails or is missing, the technical lead holds the system. It is released only when the problem is found, fixed, retested, and documented. The owner does not release water and does not ask for it to be released early. The owner makes the hold affordable: funds the repair, a carbon change, or a membrane today, and supports the clinical head in rescheduling or transferring patients safely.</p>
{{stop:No one may treat patients on water that has failed or missed a test, whatever the schedule.}}
{{key:The technical lead releases water. The owner releases the money to fix it.}}
"""),
        ("assets", "Asset life cycle", "Every machine has a life", """
{{fig:duo11b}}
<p>Machines and water systems move through a predictable life: specification, purchase, commissioning, preventive maintenance, repair and recall, and retirement. An asset register lists each one with its age, its maintenance history, and its planned replacement year. Preventive maintenance is not optional; it is how faults are found before they reach a patient.</p>
<p>Use the project calculator to compare replacing on schedule with running to failure. The comparison usually favors planning, but even when it does not, some replacements are required for safety, and the calculator only tells you how to fund them.</p>
{{key:Budget every year for maintenance and replacement. A machine that fails during a session is the most expensive machine you own.}}
"""),
        ("utilities", "Power and water", "Power and water backups", """
<p>A power cut in the middle of a session stops the blood pump and the water system together. Every unit needs a generator sized for the machines and the water system, with fuel for a defined period and a tested transfer switch, plus an uninterruptible supply for critical equipment. Water supply needs a plan too: storage, a second source where possible, and a rule for when sessions must stop.</p>
<p>Test the backups under load on a schedule, and record the test. A generator that has never run under load is a hope, not a backup.</p>
{{key:Test the generator under load and record it. Untested backups fail when you need them.}}
"""),
    ],
    "debrief": ["""
<p><strong>The morning shift.</strong> The loop stays held. The technical lead changes or regenerates the carbon, retests, and releases only on a passing result. The clinical head decides which patients wait and which go to a partner unit.</p>
<p><strong>Why chlorine matters.</strong> Chlorine and chloramine that pass into dialysate can destroy red blood cells; outbreaks of hemolysis have followed exactly this failure.</p>
<p><strong>The quote.</strong> Approve it now. Deferring water treatment to protect this year&rsquo;s budget moves the risk onto patients. Add the RO and carbon to the replacement reserve so the next one is planned.</p>
"""],
    "skills": {"title": "Water and asset assurance dashboard",
               "intro": "Build a one-page dashboard of water tests, holds, maintenance, and replacement dates.",
               "items": [("Explains why dialysis water differs from drinking water.", False),
                         ("Shows each required test, its schedule, and whether results are signed.", False),
                         ("States that water and machines are released only by the technical lead.", True),
                         ("Funds a held system&rsquo;s repair without delay.", True),
                         ("Keeps an asset register with replacement years and a reserve.", False),
                         ("Records generator tests under load.", False)],
               "placement": "Read last month&rsquo;s water log with the technical lead and count any missing results."},
    "quiz": [
        ("Why must dialysis water be purer than drinking water?",
         ["It is heated", "A large volume meets the blood across a thin membrane, so small contaminants enter the bloodstream", "It is used for cleaning", "PhilHealth requires it"],
         1, "Dialysis skips the gut&rsquo;s protection."),
        ("What did chlorine and chloramine in dialysis water cause in Brazilian outbreaks?",
         ["Hair loss", "Hemolysis, the destruction of red blood cells", "Kidney stones", "Sunburn"],
         1, "Residual chlorine and chloramine caused hemolysis outbreaks."),
        ("The morning chlorine result is missing. What is correct?",
         ["Treat as usual", "Treat it as a failed test and hold", "Use yesterday&rsquo;s result", "Ask the owner"],
         1, "A missing test is a failed test."),
        ("Who releases a held water system?",
         ["The owner", "The technical lead, after a passing retest", "The billing officer", "The supplier"],
         1, "Release is a protected technical decision."),
        ("Why keep an asset register with replacement years?",
         ["For decoration", "So replacement is planned and funded instead of happening as a crisis", "PhilHealth audits it monthly", "To lower rent"],
         1, "Planned replacement prevents failures during sessions."),
        ("What makes a generator a real backup?",
         ["Its brand", "Regular tests under load, recorded", "A new coat of paint", "A large fuel tank alone"],
         1, "Untested backups fail when needed."),
    ],
    "terms": [("Chloramine", "A disinfectant in some city water that can destroy red blood cells if it reaches the blood."),
              ("Transfer switch", "The device that moves the electrical load from the mains to the generator.")],
    "readings": [("dialysis-water-treatment-systems.html", "How a dialysis water system works.")],
    "calcs": ["calc-dialysis-owner-toolkit.html#c7", "calc-dialysis-clinical-head-toolkit.html#c8"],
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
