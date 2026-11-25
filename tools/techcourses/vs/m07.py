# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 7: Grafts and alternative configurations. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A surgeon shows a patient a looped forearm graft drawn on a tablet, with the two needle zones marked on either limb of the loop.",
    "objectives": [
        "Explain why grafts are usable sooner but narrow more often, starting from the graft&ndash;vein anastomosis.",
        "Identify when a graft is a reasoned first choice rather than a fallback.",
        "Interpret the dipyridamole-aspirin trial in absolute terms.",
        "Set first-use conditions from the specific device, the healing tissue and the patient, not from a single fixed date.",
    ],
    "big": """
{{plain:A graft is a ready-made pipe laid between an artery and a vein. Unlike a fistula, it does not need to grow before you can use it. But where the pipe joins the living vein, the vein keeps trying to repair the joint, and the repair narrows it.}}
<p>The picture has a limit. A pipe joint leaks or holds. A graft&ndash;vein anastomosis is a zone of turbulent flow, mismatched stiffness and repeated injury. Smooth-muscle-like cells grow into the vein wall there (neointimal hyperplasia), narrowing the outflow until the graft clots. This is why grafts need more procedures than fistulas over time, even though they rarely fail to mature.</p>
{{cards:Key terms for this module|Arteriovenous graft (AVG)::A synthetic or biologic conduit joining an artery to a vein, needled directly.|Expanded polytetrafluoroethylene (ePTFE)::The most common synthetic graft material.|Early-cannulation graft::A graft engineered to be needled within days of placement.|Venous anastomosis::Where the graft joins the vein; the commonest site of graft stenosis.|Primary unassisted patency::Time the access stays open without any procedure to keep it so.}}
<p>A graft is a reasoned choice when anatomy, timing or the patient&rsquo;s plan favor it. Your work is to choose it for those reasons, to explain its maintenance burden honestly, and to give the dialysis unit device-specific first-use instructions.</p>
""",
    "case": {"title": "Three weeks to dialysis", "html": """
<p>Mrs. Leonora Castillo, 63, has had two failed left forearm fistulas and a failed right forearm fistula. She dialyzes through a right internal jugular tunneled catheter that has already been exchanged once for dysfunction. Her nephrologist writes: &ldquo;She wants off the catheter. Another fistula?&rdquo; Mapping shows a 2.6 mm left upper-arm cephalic vein with a 4 cm sclerotic segment and a 3.8 mm left basilic vein, deep. Her brachial artery is good.</p>
<p>She tells you she cannot face another three-month wait with the catheter, and she runs a sari-sari store that keeps her busy.</p>
""", "questions": [
        "How would you compare a fourth fistula with a graft for her?",
        "What would you tell the dialysis unit about when and how the graft can be used?",
        "What would you document so that the next operator understands the plan?"]},
    "sections": [
        ("why", "Graft physiology", "Why grafts behave the way they do", """
<p>A graft avoids the maturation race. It is open, superficial and long from the day it is placed, so a nurse can needle it as soon as the tissue around it has healed enough to seal the needle holes. The trade-off is at the venous end. Compliance mismatch between a stiff graft and a soft vein, turbulence and vibration, and injury during anastomosis all drive neointimal hyperplasia in the outflow vein. Over months this stenosis lowers flow until the graft clots. Infection risk is also higher than with a fistula, because synthetic material cannot clear bacteria as living tissue does.</p>
{{fig:vs07_a}}
<div class="table-wrap"><table>
<thead><tr><th>Feature</th><th>Fistula</th><th>Graft</th></tr></thead>
<tbody>
<tr><td>Time to use</td><td>Usually three to six months</td><td>Usually two to four weeks; early-cannulation grafts within days</td></tr>
<tr><td>Primary failure</td><td>Common (about one in four)</td><td>Uncommon</td></tr>
<tr><td>Procedures to maintain</td><td>Fewer once mature</td><td>More, mainly for venous anastomotic stenosis</td></tr>
<tr><td>Infection</td><td>Lowest</td><td>Higher; infected grafts often need removal</td></tr>
<tr><td>Hand ischemia</td><td>Usually later, with brachial inflow</td><td>More often early</td></tr>
</tbody></table></div>
<p>Timing figures are from a recent review and the UK Kidney Association (UKKA) 2025 guideline.[[vs_lok2024]][[vs_ukka]] Hand ischemia that appears within a day of routine access surgery is strongly associated with non-autogenous access.[[vs_scheltinga2009]]</p>
{{key:A graft trades a maturation problem for a maintenance problem. Make sure the patient knows which one they are choosing.}}
"""),
        ("when", "When to choose", "When a graft is the right first choice", """
<p>UKKA recommends favoring a fistula over a graft in adults except where early cannulation is necessary or anatomy at conventional sites is unfavorable, when a graft may be considered (statement 3.4, grade 1C).[[vs_ukka]] KDOQI 2019 reached a similar position through the Life-Plan: the right access for the right patient at the right time.[[vs_kdoqi]] For Mrs. Castillo, three failed fistulas, a catheter she wants removed, and borderline remaining veins all point toward a graft as a reasoned first choice, not a defeat.</p>
{{fig:vs07_b}}
<p>Second fistulas tend to do worse than first ones. In a Canadian cohort of 1,091 people, second fistulas were used catheter-free at least once less often than first fistulas (38% versus 46%), and outcomes were hard to predict from clinical features.[[vs_kamar2019]] This observational finding does not forbid a second fistula; it argues for honesty about the odds.</p>
<p>Can a drug keep a graft open? The Dialysis Access Consortium trial randomized 649 patients with new grafts to extended-release dipyridamole plus low-dose aspirin or placebo. At one year, primary unassisted patency was 28% versus 23%, an absolute difference of 5 percentage points (hazard ratio 0.82), with no difference in graft failure, death or bleeding.[[vs_dixon2009]] The effect was real but modest, and three in four grafts still needed a procedure or clotted within a year in both groups.</p>
{{call:Do not repeat a fistula plan with poor odds only to improve a unit&rsquo;s fistula percentage. Choose the access that fits the patient, and record why.}}
"""),
        ("firstuse", "First use", "First-use conditions and configurations", """
<p>Different materials and designs have different healing and first-use characteristics. Standard ePTFE grafts are usually needled after two to four weeks, when the tunnel has incorporated and swelling has settled; early-cannulation grafts are designed for use within 24 to 72 hours.[[vs_lok2024]] The exact instructions belong to the specific product and your unit&rsquo;s experience. Write them in the handoff: the earliest permitted date, the cannulation zones (arterial and venous limbs, and the direction of flow), what to avoid near the anastomoses, and what to do if the first cannulation fails.</p>
<p>Lower-limb grafts, chest-wall configurations and other complex routes belong in a service with the expertise and rescue capacity to manage their complications. A hard-to-place graft is not a reason to step automatically down a list of operations; it is a reason for a complex access conference (Module 17).</p>
{{scene:Dialysis unit phone call, fictional|<p>Ten days after placing a forearm loop graft, a nurse calls: &ldquo;It has a strong thrill. Can we start using it today to take out the catheter?&rdquo; You check your handoff: standard ePTFE, permitted from day 21, swelling still present at day 10. You explain why, confirm the date, and ask her to call if the thrill changes.</p><p class="tc-scene-take"><b>What this shows.</b> A thrill shows flow, not healed tissue. First use follows the device and the wound.</p>}}
{{key:There is no single safe cannulation date for all grafts. Write the date and the conditions for the one you placed.}}
"""),
    ],
    "debrief": [
        "<p><strong>Comparing options.</strong> A fourth fistula on a 2.6 mm vein with a sclerotic segment would likely need months and possibly further procedures, with a real chance of never being used, while she stays on a catheter that has already malfunctioned. A left upper-arm graft can usually be used within weeks, at the price of more maintenance procedures. Present both, with her wish to be catheter-free and her work in view, and let her choose.</p>",
        "<p><strong>Use instructions.</strong> Name the product, the earliest permitted cannulation date, the arterial and venous limbs and flow direction, zones to avoid near the anastomoses, and what to do if cannulation fails. Ask the unit to keep the catheter until the graft is used successfully for several sessions, then plan removal.</p>",
        "<p><strong>Documentation.</strong> Record the failed sites and why, the configuration and inflow and outflow vessels, what remains for the future (her right upper arm, the left basilic vein), and the contingency if the graft fails.</p>",
    ],
    "skills": {"title": "Graft selection and first-use plan",
               "intro": "Case discussion or supervised clinic.",
               "items": [("Justifies a graft in terms of anatomy, timing and the patient&rsquo;s goals", False),
                         ("Explains the expected maintenance burden in plain words", False),
                         ("Identifies the specific product&rsquo;s first-use instructions", True),
                         ("Marks cannulation zones and flow direction in the handoff", False),
                         ("Documents first-use conditions, failed-cannulation plan and backup", True)],
               "placement": "Access clinic or conference"},
    "quiz": [
        ("Why might a graft be considered for a patient?",
         ["To improve a universal fistula metric", "Its timing and anatomy may fit the individual patient&rsquo;s plan",
          "It eliminates follow-up", "It never becomes infected"],
         1, "Selection rests on the patient&rsquo;s feasible pathway and the trade-offs."),
        ("When may a graft first be cannulated?",
         ["On one fixed date for all products", "Whenever a thrill is present",
          "After individualized readiness assessment consistent with the specific device and the written plan", "Only after six months"],
         2, "Device design and tissue healing determine first use."),
        ("Where do most graft stenoses form?",
         ["At the arterial anastomosis", "At the graft&ndash;vein anastomosis and outflow vein", "In the middle of the graft", "In the radial artery"],
         1, "Compliance mismatch and turbulence drive neointimal hyperplasia at the venous end."),
        ("In the Dialysis Access Consortium (DAC) graft trial, dipyridamole plus aspirin changed one-year primary unassisted patency by how much?",
         ["From 23% to 28%, an absolute 5 percentage points", "From 20% to 80%", "No change at all", "From 50% to 25%"],
         0, "A modest effect (hazard ratio 0.82); most grafts still lost primary patency within a year."),
        ("According to UKKA 2025 statement 3.4, when may a graft be considered over a fistula in adults?",
         ["Never", "When early cannulation is necessary or anatomy at conventional sites is unfavorable",
          "Whenever the surgeon prefers", "Only in patients over 80"],
         1, "Statement 3.4 is graded 1C."),
    ],
    "terms": [("Compliance mismatch", "The difference in stiffness between a graft and the vein it joins, a driver of stenosis."),
              ("Incorporation", "Healing of tissue around a graft so that needle holes seal.")],
    "readings": [("hemodialysis-access-lifeline.html", "Grafts and fistulas compared for patients."),
                 ("dialysis-access-care.html", "Care of a new graft.")],
    "calcs": ["calc-access-intervention-burden.html", "calc-catheter-exposure.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
