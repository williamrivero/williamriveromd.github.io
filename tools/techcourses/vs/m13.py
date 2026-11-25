# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 13: Hand ischemia and neurologic injury. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A surgeon compares the warmth and color of a patient&rsquo;s two hands, one pale and cool, while checking finger sensation.",
    "objectives": [
        "Explain access-related hand ischemia as loss of distal perfusion pressure, not simply reversed flow.",
        "Recognize and grade a threatened hand, and separate it from acute nerve injury and from other causes of hand pain.",
        "Use the digital&ndash;brachial index and access flow as supporting tests, knowing their limits.",
        "Escalate a threatened hand urgently, without waiting to name the operation.",
    ],
    "big": """
{{plain:An access is a low-resistance shortcut. Imagine a city water main with a new, wide drain opened near the end. Water rushes to the drain, and the houses beyond it get only a trickle, especially the ones uphill.}}
<p>The picture has a limit. The houses do not care which way the water flows in the street; they care about pressure at their taps. In the hand it is the same. Reversed flow in the artery beyond the access, &ldquo;steal,&rdquo; is common and often harmless. Ischemia happens when perfusion pressure in the hand falls below what the tissues need, usually because the arteries upstream could not enlarge enough, or are diseased, and the access draws off the pressure.[[vs_scheltinga2012]]</p>
{{cards:Key terms for this module|Hemodialysis access-induced distal ischemia (HAIDI)::Hand ischemia caused by an access, also called steal syndrome.|Digital&ndash;brachial index (DBI)::Finger pressure divided by arm pressure.|Ischemic monomelic neuropathy::Acute nerve injury from ischemia right after access creation, with pain and weakness but often a warm hand.|Banding::Narrowing the access just beyond the anastomosis to reduce flow.|Distal revascularization and interval ligation (DRIL)::A bypass that supplies the hand while the artery beyond the access is tied.}}
<p>Most cool hands after access creation are mild and improve. A few are threatened. A thrill tells you nothing about which kind you are seeing. Your work is to examine the hand, grade the threat, and escalate a severe one at once.</p>
""",
    "case": {"title": "&ldquo;It&rsquo;s still buzzing, doctor&rdquo;", "html": """
<p>Mrs. Imelda Navarro, 71, has diabetes and coronary artery disease. Yesterday afternoon you created a left brachiocephalic fistula. At 9:30 p.m., the ward nurse calls: Mrs. Navarro has severe burning pain in her left hand and cannot grip her cup. &ldquo;But the fistula is still buzzing strongly, doctor. Should I just give tramadol?&rdquo;</p>
<p>The nurse adds that the hand is warm, the radial pulse is weak, and the fingertips feel numb. Mrs. Navarro is distressed.</p>
""", "questions": [
        "What do you tell the nurse?",
        "What are you worried about, and how would you grade it?",
        "What are the options a qualified surgeon may consider, and how fast?"]},
    "sections": [
        ("mechanism", "Mechanism", "Why the hand loses pressure", """
<p>An arteriovenous access offers blood a path of very low resistance. Flow in the inflow artery rises sharply. In a healthy arterial tree, the arteries enlarge over weeks and hand pressure is maintained. In patients with diabetes, calcified arteries or proximal stenosis, the arteries cannot enlarge enough; pressure falls progressively toward the fingers, and turbulence at the anastomosis drops it further. Reversed flow in the artery beyond the access may follow, but it reflects the pressure gradient and collaterals; it is not itself the cause of ischemia.[[vs_scheltinga2012]]</p>
{{fig:vs13_a}}
<p>Timing points to cause. In a systematic review of 464 treated patients, ischemia within 24 hours of routine access surgery was strongly associated with grafts (88%), while chronic ischemia, after a month, followed autogenous access based on the brachial artery in 91%.[[vs_scheltinga2009]] Severe pain and weakness within hours of creation, in a warm hand with intact or weak pulses, suggests ischemic monomelic neuropathy, an acute nerve injury that needs immediate surgical assessment.</p>
<p>The UK Kidney Association (UKKA) 2025 guideline cites a cohort of 602 patients in which symptomatic steal developed in 7%, more often in women, people with diabetes and people with coronary disease; routine anatomic measurements predicted it poorly.[[vs_ukka]]</p>
"""),
        ("grading", "Grading", "Grading the threat", """
<p>UKKA grades steal clinically and links each grade to action.[[vs_ukka]] It suggests that all clinicians caring for hemodialysis patients be aware of steal syndrome, its risk factors and indications for urgent treatment (statement 4.8, grade 2C), and that mild steal be managed conservatively (4.9, grade 2C).</p>
{{fig:vs13_b}}
<div class="table-wrap"><table>
<thead><tr><th>Grade</th><th>Clinical features</th><th>Implication</th></tr></thead>
<tbody>
<tr><td>1, mild</td><td>Pale or cool extremity, no pain</td><td>No treatment needed; document and review</td></tr>
<tr><td>2, moderate</td><td>Pain on exercise or during dialysis</td><td>Treatment often needed; may be planned</td></tr>
<tr><td>3, severe</td><td>Pain at rest, ulcer or necrosis</td><td>Prompt treatment</td></tr>
<tr><td>Any grade plus new motor or sensory deficit</td><td>Possible acute nerve ischemia</td><td>Immediate surgical assessment</td></tr>
</tbody></table></div>
<p>Supporting tests help when the picture is unclear. The digital&ndash;brachial index compares finger pressure with arm pressure; low values are common after access creation and do not by themselves mean ischemia, so interpret them with symptoms. In a small series, banding in patients with hand ischemia raised the DBI from 0.52 to 0.65 while symptoms improved.[[vs_vanhoek2009]] Duplex can find an arterial stenosis or a high-flow access. Consider other causes of hand pain: carpal tunnel syndrome, arthritis, neuropathy.</p>
{{call:New weakness, new numbness, rest pain, or tissue loss in the access hand needs immediate surgical assessment, whatever the thrill. Do not treat it with analgesia and wait.}}
"""),
        ("treatment", "Treatment options", "What a qualified surgeon may consider", """
<p>There are no randomized trials to guide treatment; choices follow the mechanism.[[vs_ukka]] An inflow arterial stenosis may be treated with angioplasty, leaving the access alone. A high-flow access may be banded to reduce flow. Procedures such as distal revascularization and interval ligation (DRIL), proximalization of arterial inflow (PAI) and revision using distal inflow (RUDI) aim to restore hand perfusion while keeping the access. In the most severe cases, and in acute nerve ischemia, ligation restores perfusion most quickly and reliably. Preserving the access is valuable, but it does not outrank a functioning hand.</p>
<p>The learner&rsquo;s job is not to choose among these operations. It is to recognize the threat, grade it, and get the patient to a surgeon who can, quickly, with the history and examination ready.</p>
{{scene:Clinic review, fictional|<p>Three months after a brachiocephalic fistula, a patient reports hand pain only during dialysis and cool fingers. Grade 2. Duplex shows access flow of 2.3 L/min. After discussion, the team plans banding, and the patient continues dialyzing meanwhile with the hand reviewed every session.</p><p class="tc-scene-take"><b>What this shows.</b> Moderate ischemia with high flow points to flow reduction, planned rather than rushed.</p>}}
{{key:A thrill reassures you about the access, never about the hand.}}
"""),
    ],
    "debrief": [
        "<p><strong>What to tell the nurse.</strong> Do not give analgesia and wait. Severe pain with new weakness and numbness hours after a brachial-based fistula is a surgical emergency. Ask her to record the hand findings and to call the surgeon on call, or tell her you are coming now.</p>",
        "<p><strong>Your worry and grade.</strong> Rest pain with new motor and sensory deficit means at least grade 3, and a warm hand with early onset raises the possibility of ischemic monomelic neuropathy. Her diabetes and coronary disease are known risk factors.</p>",
        "<p><strong>Options and speed.</strong> A qualified surgeon assesses her tonight. In acute nerve ischemia, prompt restoration of hand perfusion, often by ligating the fistula, is usually favored over attempts to preserve it. Explain this to Mrs. Navarro and her family, update her Life-Plan, and tell her nephrologist that the fistula may be lost.</p>",
    ],
    "skills": {"title": "Urgent limb assessment",
               "intro": "Emergency station simulation or supervised ward review.",
               "items": [("Establishes onset relative to surgery or dialysis", False),
                         ("Assesses color, temperature, capillary refill, sensation and power in each hand", True),
                         ("Grades severity and identifies new neurologic deficit", True),
                         ("Escalates to a qualified surgeon with a named destination and time", True),
                         ("Documents findings and informs the nephrologist", False)],
               "placement": "Emergency station or ward"},
    "quiz": [
        ("New severe hand pain and weakness follow access creation, but a thrill is present. What is the best action?",
         ["Reassure because the access is patent", "Arrange urgent neurovascular and surgical assessment",
          "Wait for routine maturation review", "Give analgesia and recheck in the morning"],
         1, "Access flow does not show adequate hand perfusion or exclude nerve injury."),
        ("Which finding most clearly raises the urgency of assessment?",
         ["A stable healed scar", "A long-standing unchanged preference", "A new motor deficit", "A loud bruit"],
         2, "New functional loss can mean a time-critical limb or nerve problem."),
        ("What best explains access-related hand ischemia?",
         ["Reversed flow alone", "Loss of perfusion pressure in the hand when arteries cannot adapt", "Venous hypertension", "Infection"],
         1, "Steal is common and often harmless; low distal pressure causes symptoms."),
        ("Ischemia within 24 hours of routine access surgery is most strongly associated with what?",
         ["Radiocephalic fistulas", "Grafts", "Catheters", "Lower-limb access"],
         1, "In the systematic review, 88% of acute cases followed non-autogenous access."),
        ("How does UKKA 2025 suggest mild steal be managed?",
         ["Immediate ligation", "Conservatively", "DRIL in all cases", "Antibiotics"],
         1, "Statement 4.9, grade 2C."),
    ],
    "terms": [("Steal", "Reversed flow in the artery beyond an access; often harmless on its own."),
              ("Ligation", "Tying off the access, which sacrifices it to restore hand perfusion.")],
    "readings": [("dialysis-access-care.html", "Warning signs patients are taught to report."),
                 ("avf-aneurysm-and-changes.html", "Changes in the access arm over time.")],
    "calcs": ["calc-hand-ischemia-dbi.html", "calc-access-flow-cardiac.html", "calc-abi.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
