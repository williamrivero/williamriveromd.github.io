# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 17: The difficult access and changing modality. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A complex access conference with a timeline of previous operations drawn on a whiteboard and a patient&rsquo;s old venograms on screen.",
    "objectives": [
        "Reconstruct a patient&rsquo;s access history into one chronology with the reason each route failed.",
        "Run a complex access conference that includes peritoneal dialysis, transplantation and supportive care.",
        "Explain why later accesses tend to do worse, and what that means for counseling.",
        "Recognize when a complex reconstruction belongs in another service.",
    ],
    "big": """
{{plain:Repeated access failure is like a car that keeps breaking down on the same road. You can keep towing it to the nearest garage, or you can stop, look at the whole history of repairs, and ask whether the road, the car, or the destination needs to change.}}
<p>The picture has a limit. A car can be replaced; vessels cannot. Each failed access uses up sites and often adds central stenosis, so the options narrow with every attempt. The patient also changes: tired of procedures, perhaps closer to a transplant, perhaps closer to the end of life. The next decision must account for both.</p>
{{cards:Key terms for this module|Complex access conference::A planned multidisciplinary review of a patient with limited remaining access options.|Access chronology::A dated list of every access, intervention, infection and reason for failure.|Modality::The type of kidney replacement: hemodialysis, peritoneal dialysis, transplant, or conservative care.|Exhausted access::No conventional upper-limb site remains.|Conservative kidney management::Active care focused on symptoms and quality of life without dialysis.}}
<p>Your work is to stop the cycle of the next nearest operation, assemble the history, and help the patient and team choose a path that fits what remains and what the patient wants.</p>
""",
    "case": {"title": "The ninth procedure", "html": """
<p>Mrs. Erlinda Gonzales, 52, has had both forearm fistulas and a left upper-arm graft fail over seven years, with eight angioplasties and two thrombectomies. She now dialyzes through a right femoral tunneled catheter after both internal jugular veins occluded. A referral from another hospital asks you to &ldquo;create a right upper-arm graft.&rdquo; No old imaging or operative notes are attached.</p>
<p>She says she is exhausted. She has never been offered peritoneal dialysis; her sister has asked about donating a kidney.</p>
""", "questions": [
        "What do you need before proposing any operation?",
        "Who should be at the table, and what options should be discussed?",
        "How do you decide whether a complex reconstruction should happen in your hospital?"]},
    "sections": [
        ("history", "Reconstructing the history", "Reconstructing the history", """
<p>Repeated failure is information. Each failure had a cause: a small vein that never matured, an outflow stenosis, infection, thrombosis from hypotension, a central occlusion from catheters. Assemble every operation, intervention, infection, catheter and image into a single chronology, with the reason each route failed. Request old venograms and operative notes. Without them, the next operation may repeat a known mistake, or be placed into an outflow already known to be blocked.</p>
{{fig:vs17_a}}
<p>Later accesses tend to do worse. In a Canadian cohort of 1,091 patients, second fistulas were used catheter-free less often than first fistulas, and people who needed a second fistula spent much less time catheter-free than those who needed only one (23% versus 49% of the time).[[vs_kamar2019]] This is observational and selection plays a part, but it supports honest counseling: each further attempt carries lower odds.</p>
{{flow:Access chronology|Every access::Date, configuration, operator.|Every intervention::Angioplasty, stent, thrombectomy, revision.|Every catheter and device::Site, duration, complications.|Every infection::Organism, treatment, outcome.|Why it failed::The best available explanation for each.|What remains::Sites, central patency, and their uncertainty.}}
"""),
        ("conference", "The conference", "The complex access conference", """
<p>The UK Kidney Association (UKKA) 2025 guideline suggests a shared decision in managing access complications, weighing severity, treatability, alternative access options and patient priorities (statement 4.1, grade 2C).[[vs_ukka]] KDOQI&rsquo;s Life-Plan asks the same at the level of the whole kidney replacement course.[[vs_kdoqi]] A complex access conference puts the surgeon, interventionist, nephrologist, dialysis nurse and, when relevant, transplant and palliative care teams together with the patient&rsquo;s history and preferences.</p>
{{fig:vs17_b}}
<p>Discuss all paths. Peritoneal dialysis may be feasible and spare the veins entirely. A living-donor transplant evaluation may be the best access plan of all. Lower-limb access, chest-wall grafts, or devices that bypass central obstruction may be possible in expert hands. For some patients, conservative kidney management fits their goals better than another operation. No modality switch should be presented as a punishment for difficult vessels.</p>
<div class="table-wrap"><table>
<thead><tr><th>Path</th><th>What it needs</th><th>What it costs</th></tr></thead>
<tbody>
<tr><td>Further upper-limb access</td><td>A patent outflow and a usable vein or graft route</td><td>Lower odds; more procedures</td></tr>
<tr><td>Lower-limb or complex reconstruction</td><td>Expertise and rescue capacity; adequate leg arteries</td><td>Infection and limb ischemia risk</td></tr>
<tr><td>Peritoneal dialysis</td><td>A suitable abdomen and support at home</td><td>Daily self-care; peritonitis risk</td></tr>
<tr><td>Transplant</td><td>Fitness, a donor, and evaluation</td><td>Surgery and lifelong immunosuppression</td></tr>
<tr><td>Long-term catheter or conservative care</td><td>Patient choice informed by prognosis</td><td>Infection risk; or no dialysis</td></tr>
</tbody></table></div>
"""),
        ("limits", "Knowing the limits", "When the operation belongs elsewhere", """
<p>A technically possible operation may still be the wrong one: for this patient, or in this hospital. Complex reconstructions need a surgeon with experience, imaging, intensive care, and the ability to manage complications such as infection, bleeding and limb ischemia. If your service cannot provide these, refer to one that can, with the chronology attached and a safe interim plan for dialysis. Explain travel, cost and maintenance demands honestly; in the Philippines these often decide what is feasible.</p>
{{scene:Teleconference, fictional|<p>A provincial hospital refers a patient with bilateral central occlusions. You run the conference by video with the referring nephrologist, review the venograms, and agree that a lower-limb graft is possible but should be done at a tertiary center with interventional backup. You call that center, send the chronology, and keep the femoral catheter plan in place meanwhile.</p><p class="tc-scene-take"><b>What this shows.</b> Referral with a prepared history and an interim plan is a contribution, not an abdication.</p>}}
{{call:Do not attempt a complex device or reconstruction beyond local competence and rescue capability. Refer with the chronology and an interim dialysis plan.}}
"""),
    ],
    "debrief": [
        "<p><strong>Before any operation.</strong> Reconstruct her chronology: every access, intervention and catheter, and why each failed. Obtain old venograms and operative notes, and image her central veins, since both jugulars are occluded and right arm outflow is unknown. A right upper-arm graft into a blocked outflow would fail.</p>",
        "<p><strong>At the table.</strong> Surgeon, interventionist, nephrologist, dialysis nurse, a peritoneal dialysis nurse and the transplant team, with Mrs. Gonzales and, if she wishes, her sister. Discuss peritoneal dialysis, which she has never been offered; her sister&rsquo;s kidney, which could be the best plan; and complex vascular options only if outflow allows.</p>",
        "<p><strong>Where to operate.</strong> If a complex reconstruction is chosen and your hospital lacks the expertise or rescue capacity, refer with the chronology and keep a safe catheter plan meanwhile. Record her preferences and her exhaustion as part of the decision.</p>",
    ],
    "skills": {"title": "Complex access conference",
               "intro": "Prepare and present a fictional or anonymized case.",
               "items": [("Creates a dated chronology with reasons for each failure", True),
                         ("Identifies remaining options and their uncertainty", False),
                         ("Includes peritoneal dialysis, transplant and supportive care in the discussion", False),
                         ("Invites and records the patient&rsquo;s preferences", False),
                         ("Refers beyond local competence with an interim plan", True)],
               "placement": "Multidisciplinary conference"},
    "quiz": [
        ("Repeated access failures should trigger what?",
         ["Reconstruction of prior history and multidisciplinary review of remaining paths", "Automatic repetition of the last operation",
          "Exclusion of patient preferences", "Immediate long-term catheter"],
         0, "Prior procedures and failures change the next choice."),
        ("When local expertise is insufficient for a complex reconstruction, what is appropriate?",
         ["An unsupervised first attempt", "Referral to a capable service with a safe interim plan", "No further discussion with the patient",
          "Waiting until the catheter fails"],
         1, "Capability and rescue capacity belong in the access strategy."),
        ("What did the Canadian cohort find about second fistulas?",
         ["They outperformed first fistulas", "They were used catheter-free less often than first fistulas", "They never failed",
          "They were identical to grafts"],
         1, "Second fistulas did worse on catheter-free use; outcomes were hard to predict."),
        ("Which option spares the veins entirely for a patient with exhausted upper-limb access?",
         ["A right upper-arm graft", "Peritoneal dialysis", "A subclavian catheter", "Repeated angioplasty"],
         1, "Peritoneal dialysis avoids vascular access if the abdomen and home support allow."),
        ("UKKA 2025 statement 4.1 suggests managing access complications how?",
         ["By the surgeon alone", "By shared decision weighing severity, treatability, alternatives and patient priorities",
          "Always by ligation", "Only by endovascular means"],
         1, "Grade 2C."),
    ],
    "terms": [("Femoral catheter", "A dialysis catheter placed in the groin vein when neck veins are unavailable."),
              ("Living-donor transplant", "A kidney from a living person, often a relative.")],
    "readings": [("peritoneal-dialysis-ckd.html", "Peritoneal dialysis as an option."),
                 ("kidney-transplant.html", "Kidney transplant, including living donation."),
                 ("hemodialysis-elderly.html", "Balancing dialysis burden and goals.")],
    "calcs": ["calc-catheter-exposure.html", "calc-access-intervention-burden.html", "calc-frailty-assessment.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
