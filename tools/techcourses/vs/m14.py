# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 14: Aneurysm and life threatening bleeding. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A close view of a gloved hand pressing two fingers on a fistula needle site while a nurse calls for help in the background.",
    "objectives": [
        "Explain why access bleeding can be fatal within minutes, and why most deaths happen away from the unit.",
        "Read the skin over an aneurysm for signs of impending rupture.",
        "Respond to major access hemorrhage: focused pressure, help, resuscitation, transfer.",
        "Teach patients and staff what to do, and plan definitive care and the next dialysis route.",
    ],
    "big": """
{{plain:A fistula is a high-pressure pipe running just under the skin. Where the skin over it becomes thin and shiny, it is like a garden hose worn down to the last layer of rubber: it can hold for months, or burst tonight.}}
<p>The picture has a limit. A hose is the same pressure along its length. An access runs at near-arterial flow but venous wall strength, and its pressure rises further when outflow is narrowed. Repeated needling in one area weakens the wall and the skin over it. When it ruptures, blood loss can be fast enough to kill before help arrives, which is why recognition and teaching matter more than any repair technique.</p>
{{cards:Key terms for this module|True aneurysm::Dilation of the whole access wall.|Pseudoaneurysm::A contained leak through the wall, usually at a needle site, held only by surrounding tissue.|Skin threat::Thin, shiny, ulcerated or scabbed skin over an aneurysm.|Focused pressure::Firm pressure with one or two fingers directly on the bleeding point.|Sentinel bleed::A small bleed that can precede a major one.}}
<p>Your work is to spot threatened skin before it bleeds, to make sure nobody needles it, and to rehearse the first two minutes of a major bleed so that everyone does them without thinking.</p>
""",
    "case": {"title": "The shiny bulge", "html": """
<p>Mr. Benigno Tolentino, 59, has a left upper-arm fistula created eight years ago. Most of his cannulations have used the same 4 cm segment. It has become a 3 cm bulge with shiny, thin skin and a dark scab at its top. Last night the scab bled onto his pillow; his wife pressed a towel on it for twenty minutes until it stopped.</p>
<p>This morning at the unit, the nurse sends you a photograph and asks: &ldquo;He says the usual needle site is the easiest. Can we cannulate there today? The bleeding has stopped.&rdquo; His venous pressures have been rising for two months.</p>
""", "questions": [
        "Can the usual site be used today?",
        "What does this bulge tell you, and what needs to happen next?",
        "What do Mr. Tolentino and his wife need to know before they go home?"]},
    "sections": [
        ("why", "Why it kills", "Why access bleeding can be fatal", """
<p>Access hemorrhage is rare but catastrophic. Reviewing 14 years of reported deaths in Australia and New Zealand, Jose and colleagues estimated fewer than one fatal access bleed per 1,000 patient-years; a unit may see one only once a decade. Their review of each unit&rsquo;s root-cause analyses concluded that these deaths are potentially preventable with the right policies.[[vs_jose2017]] In a forensic series of 100 deaths from access-site hemorrhage, 81% of the bleeds occurred at home and 44% of patients died there.[[vs_gill2012]] These are descriptive series, not trials, but they show where prevention must reach: the patient&rsquo;s home.</p>
{{fig:vs14_a}}
<p>The mechanism explains the speed. Access flow is often over a liter a minute, the wall is thin, and the bleeding point sits just under the skin. An outflow stenosis raises the pressure further. Skin that is thin, shiny, ulcerated or scabbed, or a recent small bleed, means the barrier has almost gone.</p>
<div class="table-wrap"><table>
<thead><tr><th>Finding</th><th>What it means</th><th>Action</th></tr></thead>
<tbody>
<tr><td>Stable aneurysm, healthy thick skin</td><td>Low immediate risk</td><td>Rotate sites; regular review</td></tr>
<tr><td>Rapid enlargement, rising venous pressure</td><td>Possible outflow stenosis</td><td>Image and treat the outflow</td></tr>
<tr><td>Thin, shiny or discolored skin</td><td>Skin threat</td><td>Do not cannulate; urgent surgical review</td></tr>
<tr><td>Ulcer, scab, or recent bleeding</td><td>Impending rupture</td><td>Do not cannulate; same-day surgical assessment</td></tr>
</tbody></table></div>
{{key:Never needle threatened skin. A small bleed from it is a warning, not a resolved problem.}}
"""),
        ("response", "The first two minutes", "Responding to a major bleed", """
<p>In major access hemorrhage, the first minutes decide the outcome. Call for help and activate the emergency response. Apply firm, focused pressure with one or two fingers directly on the bleeding point, not a large dressing that spreads the pressure. Lay the patient down and start the institution&rsquo;s resuscitation and transfer pathway. If a tourniquet is part of your local protocol, follow it; otherwise maintain direct pressure until a surgeon controls the bleeding. Do not send the patient for imaging while bleeding continues, and do not attempt an unsupervised repair because an algorithm describes one.</p>
{{flow:Major access hemorrhage|Call::Emergency help; say &ldquo;major bleeding from a dialysis access.&rdquo;|Press::Firm focused pressure on the bleeding point with one or two fingers.|Position and resuscitate::Lie flat; airway, breathing, circulation; intravenous access and blood per protocol.|Transfer::To a surgeon who can control and repair it, with pressure maintained.|Plan dialysis::The access may be lost; arrange a temporary route.}}
<p>After control, the specialist assessment considers the whole circuit: an outflow stenosis that raised the pressure, infection in the aneurysm, the options for repair or reconstruction, and the next dialysis route. The UK Kidney Association (UKKA) 2025 guideline recommends regular assessment of aneurysms with intervention guided by symptoms, access function and the risk of spontaneous bleeding (statement 4.6, grade 1C), and suggests surgical repair as the main approach, combined with inflow reduction or treatment of downstream stenosis where appropriate (4.7, grade 2D).[[vs_ukka]]</p>
{{call:Active bleeding from an access is an emergency. Call for help and press on the point. Imaging, photographs and paperwork come later.}}
"""),
        ("teaching", "Teaching and prevention", "Teaching patients and staff", """
<p>Because most fatal bleeds happen at home, every patient and household member should know what to do: press firmly with two fingers on the spot, keep pressing, call for emergency help, and do not remove the pressure to look. Teach it at the first-use visit and repeat it when an aneurysm appears. A unit can rehearse the response the way it rehearses a cardiac arrest.</p>
{{fig:vs14_b}}
<p>Prevention is mostly about cannulation and outflow: rotating needle sites, avoiding area puncture, and treating outflow stenosis that raises pressure. A photograph cannot establish that skin is safe. Know who provides definitive care out of hours, and write it in the coverage arrangement.</p>
{{scene:Unit drill, fictional|<p>The head nurse runs a bleeding drill with a simulator arm. A new nurse reaches for a thick gauze pad; the trainer stops her and shows two-finger focused pressure. The next drill takes 40 seconds from alarm to pressure and help called.</p><p class="tc-scene-take"><b>What this shows.</b> The right response has to be automatic. Drills make it so.</p>}}
"""),
    ],
    "debrief": [
        "<p><strong>The usual site.</strong> No. Shiny thin skin, a scab, and a bleed last night are signs of impending rupture. Needling there could start a bleed he might not survive. Tell the nurse not to cannulate that segment or anywhere on the threatened skin.</p>",
        "<p><strong>What next.</strong> Arrange same-day surgical assessment. The rising venous pressures suggest an outflow stenosis that has been raising the pressure in the aneurysm; it needs imaging and treatment along with the aneurysm. Agree with the nephrologist on a safe dialysis plan meanwhile: another usable segment far from the threatened skin if one exists, or a temporary catheter.</p>",
        "<p><strong>Before going home.</strong> Teach Mr. Tolentino and his wife two-finger pressure on the bleeding point and to call for emergency help without lifting the pressure. Give them the unit&rsquo;s and the surgeon&rsquo;s numbers and the name of the nearest hospital that can treat a bleed.</p>",
    ],
    "skills": {"title": "Skin threat recognition and hemorrhage response",
               "intro": "Simulator station and supervised clinic.",
               "items": [("Identifies skin warning signs over an aneurysm", True),
                         ("Instructs that threatened skin is never cannulated", True),
                         ("Rehearses focused pressure and emergency activation on a simulator", True),
                         ("Communicates transfer to a surgeon who can control bleeding", False),
                         ("Documents an alternative dialysis plan and teaches the patient home response", False)],
               "placement": "Simulation and access clinic"},
    "quiz": [
        ("An aneurysmal area has ulcerated skin and recent bleeding. What is the best response?",
         ["Avoid that area and arrange urgent assessment with a dialysis contingency", "Cannulate through the scab",
          "Reassure because the bleeding stopped", "Apply a tight bandage and continue"],
         0, "Skin threat and recent bleeding mean impending rupture."),
        ("Major access bleeding begins in a simulation. What is the first response?",
         ["Photograph it before helping", "Call for help and apply focused direct pressure while starting the resuscitation pathway",
          "Send for imaging", "Remove the dressing to look"],
         1, "Hemorrhage control and emergency response come before anything else."),
        ("Where did most fatal access hemorrhages occur in the forensic series of 100 deaths?",
         ["In the dialysis unit", "At home", "In the operating room", "In the emergency department"],
         1, "81% of the hemorrhages occurred at home, so home teaching is essential."),
        ("Which technique best controls bleeding from an access needle site?",
         ["A large bulky dressing", "Firm focused pressure with one or two fingers on the bleeding point",
          "Elevating the arm only", "Ice packs"],
         1, "Focused pressure concentrates force on the defect."),
        ("Rapid aneurysm growth with rising venous pressures suggests what?",
         ["Inflow stenosis", "Outflow stenosis raising pressure in the access", "Infection only", "A normal aging fistula"],
         1, "Downstream narrowing raises intra-access pressure; treat it with the aneurysm."),
    ],
    "terms": [("Pseudoaneurysm", "A contained leak through the access wall held by surrounding tissue."),
              ("Root-cause analysis", "A structured review of how a serious event happened, to prevent it.")],
    "readings": [("avf-aneurysm-and-changes.html", "Fistula aneurysms and the warning signs patients should know."),
                 ("dialysis-access-care.html", "How patients are taught to stop a bleed.")],
    "calcs": ["calc-shock-index.html", "calc-access-flow-cardiac.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
