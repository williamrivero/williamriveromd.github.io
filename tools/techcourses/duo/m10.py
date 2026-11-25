# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 10: Workforce investment and employment oversight. Written for this course from published sources."""

MODULE = {
    "image_alt": "Three dialysis staff of different ages in a loose huddle at shift change beside a whiteboard roster.",
    "objectives": [
        "Explain the chain from staffing to care processes to patient outcomes, and how strong the evidence is.",
        "Describe why skill mix matters, not only head count.",
        "Calculate full-time equivalents (FTE) with a relief factor and staff cost per session.",
        "Oversee the employer&rsquo;s duties: lawful pay, remittances, safe hours, and burnout.",
    ],
    "big": """
{{plain:Staff are the unit&rsquo;s immune system. You do not notice them when they are strong; you notice everything when they are weak. A unit with too few nurses does not fail at once. It fails one skipped check at a time.}}
<p>The picture has a limit. An immune system grows by itself. A competent dialysis workforce has to be hired, trained, signed off, kept, and paid on time, and every one of those steps is an owner decision.</p>
{{cards:Key terms for this module|Staffing ratio::Patients or stations per nurse or technician on a shift.|Skill mix::The share of registered nurses (RNs), patient care technicians (PCTs), and others on a shift.|Full-time equivalent (FTE)::One person working full contracted hours.|Relief factor::Extra staffing that covers leave, training, and sickness.|Care left undone::Necessary tasks that staff do not have time to complete.}}
<p>Staffing is the largest cost an owner controls and the one most closely tied to what happens to patients. This module shows you why, and how to plan it.</p>
""",
    "case": {"title": "Two nurses", "html": """
<p>A board in Iloilo City reviews a budget that is 180,000 pesos a month short. The finance officer proposes removing two nurse posts and covering with patient care technicians and overtime. The head nurse, Ms. Jocelyn Tumbaga, says the remaining nurses would each cover four stations on every shift with no relief, and that two of them have already asked about jobs abroad.</p>
""", "questions": ["What does the evidence associate with heavier staffing loads?", "How many FTE does the unit actually need?", "What other options should the board consider?"]},
    "sections": [
        ("why-staff", "Staffing and outcomes", "From staffing to outcomes", """
{{fig:duo10a}}
<p>Follow the chain. Staffing level and skill mix decide how much time each patient gets. Time decides whether assessments are done, alarms answered, teaching given, and access checked. Those processes decide outcomes.</p>
<p>The studies agree in direction. In United States units, a higher patient load per registered nurse was associated with more nurse-reported adverse events and more care left undone.[[dch_thomashawkins2008]] Facilities with a heavier patient care technician load were associated with higher mortality and hospitalization.[[uom_plantinga2024]] Among adolescents and young adults, higher patient-to-staff ratios were associated with lower access to the transplant waiting list.[[dch_bicki2024]] And when large chains acquired independent facilities, nurses were replaced by less-trained technicians as outcomes worsened.[[duo_eliason2020]]</p>
<p>All of this evidence is observational and from another country. Sicker patients may cluster in busier units, and that could explain part of the link. But the direction is consistent across studies, it fits how care is delivered, and no study shows that cutting staff is safe.</p>
{{key:Staffing is a safety control that happens to cost money, not a cost that happens to affect safety.}}
"""),
        ("skill-mix", "Skill mix", "Head count is not enough", """
<p>Two units with the same number of staff can be very different. A registered nurse assesses, decides, gives medicines, and recognizes deterioration; a technician supports under supervision. Replacing nurses with technicians lowers cost and narrows what the shift can safely do. The DOH order sets the nurse-to-station limit and requires an ACLS-trained nurse on every shift; a technician does not count toward either.[[doh2012]]</p>
<p>Burnout is part of skill mix too. A meta-analysis linked nurse burnout with lower patient safety and lower patient satisfaction.[[uom_li2024]] Tired, overloaded staff leave, and every resignation costs a hiring cycle and months of training.</p>
{{key:Protect the nurse posts the license requires, and treat burnout as a safety risk.}}
"""),
        ("fte", "FTE", "Full-time equivalents and relief", """
{{fig:duo10b}}
<p>One post on every shift needs more than one person. <strong>Worked example (fictional).</strong> Three nurse posts per shift, eighteen shifts a week, six hours each, with 48 contracted hours a week: 3 &times; 18 &times; 6 &divide; 48 = 6.75 FTE. Add a 15% relief factor for leave, training, and sickness: 6.75 &times; 1.15 = 7.76, so hire eight. At 38,000 pesos a month all-in per FTE, that is about 295,000 pesos a month, or about 490 pesos per session at 600 sessions.</p>
<p>The calculator gives you the number. Your licensing rule and your clinical head tell you whether it is enough for your patients&rsquo; needs.</p>
{{key:Budget for relief. A roster that works only when nobody is sick does not work.}}
"""),
        ("employer", "The employer", "The employer&rsquo;s duties", """
<p>An owner is also an employer. Pay must meet the current wage order for your region; overtime, night differential, and holiday pay follow the Labor Code; and contributions to the Social Security System (SSS), PhilHealth, and Pag-IBIG must be remitted on time.[[uom_laborcode]][[uom_sss2025]][[uom_ph_pa2025]] These rates change. Have your accountant and labor adviser keep a dated calendar of every obligation, and review it at each board meeting.</p>
<p>Late pay and missing remittances are not only legal problems. They tell staff that the unit cannot be trusted, and trusted staff are the ones who stay.</p>
{{stop:Never delay payroll or statutory remittances to fund an owner distribution or a growth project.}}
{{key:Pay people correctly and on time. It is the cheapest retention policy there is.}}
"""),
    ],
    "debrief": ["""
<p><strong>The evidence.</strong> Heavier staffing loads are associated with more adverse events, care left undone, higher mortality and hospitalization, and lower transplant access. The data are observational, but none suggests the cut is safe.</p>
<p><strong>The FTE.</strong> Run the calculator with the unit&rsquo;s actual posts, shifts, and relief. If it shows the current roster has no relief, the gap is already a risk.</p>
<p><strong>Other options.</strong> Look at supply costs, collections, idle capacity, or a temporary loan. If none closes the gap, reduce the number of patients accepted rather than the nurses who treat them, and plan transfers through the clinical head.</p>
"""],
    "skills": {"title": "Workforce assurance plan and employment calendar",
               "intro": "Build a workforce plan with FTE, relief, skill mix, and a dated calendar of employer obligations.",
               "items": [("Explains the staffing-to-outcome chain and calls the evidence observational.", False),
                         ("Calculates FTE with relief on the calculator.", False),
                         ("Keeps nurse posts at or above the DOH limit and the ACLS requirement on every shift.", True),
                         ("Refuses to balance a budget by cutting below safe staffing; shows the trade-off instead.", True),
                         ("Keeps a dated calendar of wage, overtime, and remittance obligations from current sources.", False),
                         ("Tracks turnover and burnout signals for the board.", False)],
               "placement": "With the head nurse, compare last month&rsquo;s actual roster with the FTE calculation."},
    "quiz": [
        ("What did Thomas-Hawkins and colleagues associate with a higher patient load per registered nurse?",
         ["Fewer adverse events", "More nurse-reported adverse events and care left undone", "Lower costs with no effect", "Shorter sessions"],
         1, "The study was observational, from United States units."),
        ("Three posts, eighteen shifts, six hours, 48 contracted hours. What is the base FTE?",
         ["4.5", "6.75", "9.0", "18"],
         1, "3 &times; 18 &times; 6 &divide; 48 = 6.75."),
        ("Why add a relief factor?",
         ["To pay bonuses", "To cover leave, training, and sickness", "To meet PhilHealth rules", "To shorten shifts"],
         1, "Without relief, the roster fails whenever someone is absent."),
        ("Can a patient care technician count toward the DOH nurse-to-station limit?",
         ["Yes", "No", "Only at night", "Only on weekends"],
         1, "The limit is for nurses, and an ACLS-trained nurse is required on every shift."),
        ("The budget is short. Which response is safest?",
         ["Cut nurse posts below the limit", "Reduce patients accepted and look for other savings, keeping safe staffing", "Delay payroll", "Skip remittances for a month"],
         1, "Safe staffing is a protected constraint; volume and other costs can flex."),
        ("What did the meta-analysis of nurse burnout find?",
         ["No link with safety", "Burnout was associated with lower patient safety and satisfaction", "Burnout improved efficiency", "Burnout affected only pay"],
         1, "Burnout is a patient safety issue as well as a staffing one."),
    ],
    "terms": [("Wage order", "A regional order setting the minimum wage."),
              ("Statutory remittance", "A contribution the employer must pay to SSS, PhilHealth, or Pag-IBIG.")],
    "readings": [],
    "calcs": ["calc-dialysis-owner-toolkit.html#c4"],
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
