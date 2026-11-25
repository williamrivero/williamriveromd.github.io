# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 4: Mapping and choosing an access. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A sonographer scans the inner arm of a seated patient while a surgeon marks the course of a vein on the skin.",
    "objectives": [
        "Read a vessel-mapping report against the planned inflow, outflow, course, depth and cannulation segment.",
        "Explain why diameter is a surrogate for what you need, and what imaging cannot tell you.",
        "State what the randomized evidence on routine preoperative ultrasound does and does not show.",
        "Justify a chosen access and a backup, including why alternatives were rejected.",
    ],
    "big": """
{{plain:A vessel map is like a survey before building a road. It tells you the width of the ground, how deep it lies, and whether it runs straight. But a road is built for traffic, and an access is built for needles: a survey that ignores where the cars will drive answers the wrong question.}}
<p>The picture has a limit. Ground does not change with use; a vein does. A vein of adequate diameter may still fail because its wall is stiff, the artery feeding it is calcified, or the outflow is narrow. The map shows what the vessels are today, not how they will respond to arterial flow. Diameter is a surrogate for that response, and an imperfect one.</p>
{{cards:Key terms for this module|Vessel mapping::Duplex ultrasound of arteries and veins before surgery, usually with a tourniquet for veins.|Minimum luminal diameter::The narrowest inner width of a vessel segment.|Cannulation segment::A straight, superficial stretch long enough for two needles.|Distal first::Using the most peripheral feasible site first, to keep proximal sites for later.|Surrogate::A measurement that stands in for the outcome you care about, here a usable access.}}
<p>The map makes most decisions clearer and a few more confusing. Your work is to read it for construction and for cannulation, and to settle uncertainty before booking theater.</p>
""",
    "case": {"title": "Two maps, two answers", "html": """
<p>Ms. Rosalinda Garcia, 49, has CKD from lupus nephritis and an eGFR of 14. Her right hand is dominant. A map from a private clinic reports a left forearm cephalic vein of 2.4 mm and a radial artery of 1.9 mm. A second map, done at your hospital three weeks later, reports the same vein at 1.8 mm without a tourniquet and the upper-arm cephalic vein at 4.2 mm, running 9 mm below the skin for most of its length.</p>
<p>She works as a seamstress and asks that you avoid her right arm. Dialysis is expected within four months.</p>
""", "questions": [
        "How do you reconcile the two maps?",
        "What does each report not tell you?",
        "Which access would you propose, what is your backup, and why?"]},
    "sections": [
        ("reading", "Reading the map", "What a useful map answers", """
<p>A fistula works only if four things are true: the artery can deliver enough flow, the vein can dilate and thicken in response, the outflow can drain it, and nurses can reach it with needles. The map speaks to some of these directly and to others only by proxy. Read it with your planned operation drawn on it: inflow artery, anastomosis site, the vein&rsquo;s course and depth, the cannulation segment, and the central outflow.</p>
{{fig:vs04_a}}
<p>Measurements depend on method. A vein measured with a tourniquet in a warm room is larger than the same vein measured cold without one. Before comparing two reports, check how each was done. Ask what the map cannot establish: wall quality, response to flow, and central veins behind the clavicle.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question</th><th>What the map shows</th><th>What it cannot show</th></tr></thead>
<tbody>
<tr><td>Inflow</td><td>Arterial diameter, calcification, flow pattern</td><td>How much the artery will dilate</td></tr>
<tr><td>Vein</td><td>Diameter, continuity, depth, branches</td><td>Wall compliance and remodeling capacity</td></tr>
<tr><td>Outflow</td><td>Arm veins to the axilla</td><td>Central veins behind the clavicle</td></tr>
<tr><td>Cannulation</td><td>Depth and straight-segment length</td><td>The skill of the cannulator</td></tr>
</tbody></table></div>
{{key:Never declare an access usable from diameter alone. Ask whether it can be built, whether it will grow, and whether a nurse can needle it.}}
"""),
        ("evidence", "Evidence", "What the evidence on mapping and thresholds shows", """
<p>Ferring and colleagues randomized 218 patients to clinical examination alone or clinical examination plus routine ultrasound before fistula creation. Immediate failure fell from 11% to 4%. Primary fistula survival at one year was not statistically different (65% versus 56%), but assisted primary survival was better with ultrasound (80% versus 65%). About 12 patients needed scanning to prevent one fistula failure.[[vs_ferring2010]] This was a single-center trial; patency is a surrogate for usable dialysis access, but the authors also reported use for dialysis.</p>
{{fig:vs04_b}}
<p>The UK Kidney Association (UKKA) 2025 guideline suggests that the decision on whether and where to form access is best informed by combined clinical and ultrasound assessment (statement 2.4, grade 2C), and recommends counseling patients to expect poorer outcomes when one or both vessels are under 2.0 mm (3.3, grade 1C).[[vs_ukka]] Note what that statement does and does not say: 2.0 mm is a counseling threshold, not a prohibition.</p>
<p>UKKA also recommends favoring distal locations first where anatomy and preference allow (3.2, grade 1B), to keep proximal sites for later.[[vs_ukka]] Distal fistulas fail primarily more often, so the choice is a trade between preserving the future and succeeding now; for a patient with little time before dialysis, the balance shifts upward.</p>
{{call:Guidelines differ in how much routine mapping they recommend and in their thresholds. Your service should adopt one written policy, record it, and not mix thresholds from different documents case by case.}}
"""),
        ("choosing", "Choosing", "From map to decision", """
<p>Integrate the anatomy with the time before dialysis, prior failures, the patient&rsquo;s dominant hand and work, local expertise, and what each choice leaves for later. A deep vein can be superficialized or transposed, but that adds an operation and delays use. A borderline forearm vein may mature with time the patient does not have.</p>
{{flow:Choosing an access|Draw the plan on the map::Inflow, anastomosis, course, depth, cannulation segment, outflow.|Name the uncertainty::What the map cannot tell you and whether it matters.|Weigh time and future::Time to dialysis against preserving proximal sites.|Choose and justify::Selected access, backup, and why alternatives were rejected.|Tell the patient::Expected maturation, extra procedures, and failure risk.}}
{{scene:Weekly access conference, fictional|<p>A trainee proposes a radiocephalic fistula because the vein measures 2.1 mm. You ask the sonographer how it was measured: cold room, no tourniquet. A repeat scan with a tourniquet shows 2.9 mm and a continuous straight segment. The plan stands, now on evidence rather than a number.</p><p class="tc-scene-take"><b>What this shows.</b> A measurement is only as good as its method. Ask before you act on it.</p>}}
{{key:Write down why you rejected the alternatives. The next surgeon, possibly you, will need to know.}}
"""),
    ],
    "debrief": [
        "<p><strong>Reconciling the maps.</strong> Check the method of each: the 2.4 mm figure may have been measured with a tourniquet, the 1.8 mm without. Review the images with the sonographer, repeat the forearm study under standardized conditions if needed, and examine her yourself. Do not pick the larger number.</p>",
        "<p><strong>What the reports do not tell you.</strong> Neither shows her central veins, and neither predicts how a 1.9 mm radial artery will dilate. The upper-arm vein is large but 9 mm deep for most of its course: hard to cannulate unless it is superficialized or transposed.</p>",
        "<p><strong>A reasonable proposal.</strong> With dialysis about four months away, a small forearm vein and a small artery, UKKA would have you counsel her to expect a poorer chance of success if either vessel is under 2.0 mm. A left upper-arm fistula with a planned superficialization (or a two-stage transposition) is a defensible first choice; the backup is a left upper-arm graft if the vein fails. Her right arm is protected for the future. Record why the forearm was rejected, and that she agreed after hearing the expected timeline and the chance of a second operation.</p>",
    ],
    "skills": {"title": "Interpreting a map and justifying a choice",
               "intro": "Use anonymized or fictional mapping reports in a supervised conference.",
               "items": [("Annotates inflow, anastomosis, vein course and depth, and outflow on the map", False),
                         ("Checks how each measurement was obtained before comparing reports", False),
                         ("Identifies what the imaging cannot establish", False),
                         ("Marks a feasible cannulation segment, or states that none exists", True),
                         ("Defends the selected route and a backup, with reasons for rejecting alternatives", True),
                         ("Does not declare usability from diameter alone", True)],
               "placement": "Access conference"},
    "quiz": [
        ("What makes a mapping report useful for access selection?",
         ["One diameter without context", "Anatomy interpreted against the planned construction and cannulation segment",
          "An unqualified declaration of suitability", "A report signed by two sonographers"],
         1, "The report must answer the clinical question, including whether the access can be needled."),
        ("Two mapping reports disagree about a vein&rsquo;s diameter. What is the best next action?",
         ["Use the larger measurement", "Operate and decide intraoperatively",
          "Review images, methods and examination with the mapping team", "Choose a graft to avoid the question"],
         2, "Method (tourniquet, temperature) changes diameter; resolve consequential uncertainty first."),
        ("In the Ferring randomized trial, routine preoperative ultrasound most clearly reduced what?",
         ["Mortality", "Immediate fistula failure (4% versus 11%)", "The need for any dialysis catheter", "Infection"],
         1, "Immediate failure fell; assisted primary survival at one year also improved, while primary survival did not differ significantly."),
        ("UKKA 2025 statement 3.3 recommends what when a vessel is under 2.0 mm?",
         ["Never create a fistula", "Counsel the patient to expect a poorer outcome", "Always place a graft", "Repeat the scan monthly"],
         1, "It is a counseling threshold (grade 1C), not an absolute contraindication."),
        ("Why does UKKA recommend favoring distal sites first?",
         ["Distal fistulas never fail", "To keep proximal sites available for later access",
          "Distal fistulas have higher flow", "Distal sites avoid the need for consent"],
         1, "Statement 3.2 (grade 1B) preserves future options, accepting a higher primary failure rate distally."),
    ],
    "terms": [("Superficialization", "An operation that brings a deep vein closer to the skin so it can be needled."),
              ("Transposition", "Moving a vein to a new, more superficial and accessible course.")],
    "readings": [("hemodialysis-access-lifeline.html", "How access is planned and why vessels matter."),
                 ("dialysis-access-care.html", "Access care after creation.")],
    "calcs": ["calc-av-fistula-maturation.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
