# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 18: Kidney care beyond the access. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "At a fistula review, a surgeon kneels to examine a dialysis patient&rsquo;s foot with a small toe wound, the access arm resting on the table.",
    "objectives": [
        "Recognize vascular problems in access patients that need a different pathway: limb ischemia, renal artery and transplant vascular questions.",
        "Plan imaging and procedures that protect residual kidney function and fluid balance.",
        "Explain the training and privileging boundaries between access surgery, general vascular surgery and transplant surgery.",
        "Stabilize, route and hand off a non-access problem with confirmed receipt.",
    ],
    "big": """
{{plain:An access appointment is like a car brought in for a tire. A good mechanic still notices smoke from the engine, and does not send the car home because the job sheet says &ldquo;tire.&rdquo;}}
<p>The picture has a limit. A mechanic can usually fix the engine too. Access experience does not make a surgeon competent in every vascular or transplant operation, and dialysis patients carry the heaviest burden of arterial disease, calcification and wound failure of any group. Noticing the engine is the obligation; fixing it may belong to someone else.</p>
{{cards:Key terms for this module|Chronic limb-threatening ischemia::Rest pain, ulcers or gangrene from arterial disease.|Ankle&ndash;brachial index::Ankle pressure divided by arm pressure; falsely high when arteries are calcified.|Residual kidney function::The kidney function a dialysis patient, or a patient with late chronic kidney disease (CKD), still has.|Scope of practice::The procedures a clinician is trained and privileged to perform.|Warm handoff::A direct conversation with the receiving clinician, not just a referral form.}}
<p>Your work is to identify the principal problem, judge its urgency, protect kidney function in the investigations you order, and route it to a qualified service.</p>
""",
    "case": {"title": "The toe at the fistula visit", "html": """
<p>Mr. Crisanto Valdez, 67, comes for a routine six-month fistula review. The fistula is working well. As he leaves he mentions that his right foot has hurt at night for three weeks; he sleeps with his leg hanging off the bed. A small black wound on his second toe has not healed. He has diabetes and has been on hemodialysis for two years; he still passes about 600 mL of urine a day.</p>
<p>The clinic is running late. The resident suggests, &ldquo;Let us note it and tell him to see his doctor.&rdquo;</p>
""", "questions": [
        "How urgent is this, and what is the likely problem?",
        "What would you consider before ordering contrast imaging?",
        "Who should take this on, and how do you hand it over?"]},
    "sections": [
        ("interfaces", "Other vascular problems", "Recognizing problems that are not the access", """
<p>Patients with kidney failure have accelerated, often heavily calcified, arterial disease. Rest pain relieved by hanging the leg down, a non-healing toe wound, or gangrene suggest chronic limb-threatening ischemia, a threat to the leg that needs prompt vascular assessment. Calcified arteries make the ankle&ndash;brachial index unreliable (often falsely normal or high), so toe pressures or imaging may be needed.</p>
{{fig:vs18_a}}
<p>Other interfaces include renal artery disease in a patient with resistant hypertension or flash pulmonary edema, vascular questions in a transplant recipient (such as a transplant renal artery stenosis), and aortic disease found incidentally. Each has its own pathway and specialists. Clarify whether the problem in front of you is the access, systemic vascular disease, or another service&rsquo;s domain.</p>
<div class="table-wrap"><table>
<thead><tr><th>Presentation</th><th>Possible problem</th><th>Pathway</th></tr></thead>
<tbody>
<tr><td>Rest pain, toe wound, gangrene</td><td>Chronic limb-threatening ischemia</td><td>Urgent vascular service</td></tr>
<tr><td>Sudden cold, painful, pale limb</td><td>Acute limb ischemia</td><td>Emergency vascular surgery</td></tr>
<tr><td>New hypertension or graft dysfunction after transplant</td><td>Transplant vascular problem</td><td>Transplant team</td></tr>
<tr><td>Resistant hypertension, flash pulmonary edema</td><td>Renal artery stenosis</td><td>Nephrologist with vascular input</td></tr>
</tbody></table></div>
{{call:Rest pain, tissue loss or a sudden cold limb in a dialysis patient is not a routine note. Assess it and route it to the right urgent service the same day.}}
"""),
        ("kidney", "Protecting the kidney", "Investigations that protect residual function", """
<p>Residual kidney function matters even on dialysis: it helps control fluid, potassium and phosphate, and its preservation is associated with better outcomes. A patient still passing 600 mL a day has something to protect. Iodinated contrast, hypotension, and nephrotoxic drugs can all reduce it; contrast-associated acute kidney injury (AKI) is the usual worry. Plan the minimum useful investigation with the renal and imaging teams: duplex first where it answers the question, the lowest effective contrast volume where angiography is needed, timing relative to dialysis, and attention to fluid balance and allergies.</p>
{{fig:vs18_b}}
<p>The same thinking applies to patients with chronic kidney disease (CKD) not yet on dialysis who need access mapping or angiography: the investigation that answers today&rsquo;s question should not hasten tomorrow&rsquo;s dialysis.</p>
{{key:Ask what result you need and how it will change management before ordering a test that can harm the kidneys.}}
"""),
        ("scope", "Scope", "Training, scope and the safest contribution", """
<p>Access surgery is a distinct skill set. Board certification in vascular surgery follows defined training and examination pathways; in the United States these are set by the Accreditation Council for Graduate Medical Education (ACGME) and the American Board of Surgery (ABS).[[vs_acgme]][[vs_abs]] In the Philippines, the Philippine Association of Thoracic and Cardiovascular Surgery, Inc. (PATACSI) lists accredited thoracic and cardiovascular surgery (TCVS) training programs, including a post-residency vascular pathway; that directory helps verify training but does not by itself define every eligibility rule.[[vs_patacsi]] Completing this Academy track adds no transplant, aortic or peripheral arterial privileges.</p>
<p>The safest contribution to a problem outside your scope is an accurate assessment, timely referral, and a warm handoff: a direct call, the key findings, the urgency, and confirmation that the receiving service has accepted the patient.</p>
{{scene:Clinic corridor, fictional|<p>During an access review, a transplant recipient mentions that her graft function has fallen and her blood pressure has risen. You do not order renal artery imaging yourself. You call her transplant nephrologist, who arranges a duplex the same week, and you write the call in her notes.</p><p class="tc-scene-take"><b>What this shows.</b> Recognizing a problem and handing it to the right team is part of good access care.</p>}}
"""),
    ],
    "debrief": [
        "<p><strong>Urgency.</strong> Three weeks of rest pain relieved by dependency and a black, non-healing toe wound in a patient with diabetes on dialysis suggest chronic limb-threatening ischemia. This needs urgent vascular assessment, not a note to see his doctor.</p>",
        "<p><strong>Before contrast.</strong> He still passes 600 mL a day. Discuss with his nephrologist and the vascular team: start with clinical examination and duplex or toe pressures (his ankle&ndash;brachial index may be falsely reassuring from calcification), and if angiography is needed, minimize contrast and coordinate timing and fluid balance.</p>",
        "<p><strong>Handoff.</strong> If you are privileged and equipped for peripheral arterial work, take it on; if not, call the vascular service directly today, give the findings and urgency, and confirm acceptance. Tell his nephrologist and document the handoff.</p>",
    ],
    "skills": {"title": "Scope decision and urgent routing",
               "intro": "Case discussion or supervised clinic.",
               "items": [("Identifies the principal problem beyond the access", True),
                         ("States urgency correctly", True),
                         ("Explains investigation trade-offs for residual kidney function", False),
                         ("Refers to a qualified service with a warm handoff and confirms receipt", True)],
               "placement": "Access clinic"},
    "quiz": [
        ("A fistula-review patient reports new rest pain and a toe wound. What is the best response?",
         ["Ignore it as unrelated", "Wait until the next access visit", "Assess and route the limb threat to an appropriate urgent service",
          "Prescribe analgesics only"],
         2, "Appointment labels cannot replace assessment of a serious vascular problem."),
        ("What does completing this track establish about transplant surgery?",
         ["No additional transplant operative authorization", "Automatic transplant privileges", "Eligibility to bypass specialty requirements",
          "Board certification"],
         0, "Distinct procedures need their own training and hospital privileges."),
        ("Why may the ankle&ndash;brachial index mislead in dialysis patients?",
         ["It is always low", "Calcified arteries resist compression, giving falsely normal or high values", "It measures veins", "It requires contrast"],
         1, "Medial calcification is common in kidney failure; toe pressures or imaging help."),
        ("A dialysis patient still passes 600 mL of urine daily and needs angiography. What is the best approach?",
         ["Use as much contrast as needed; he is on dialysis anyway", "Plan the minimum useful investigation with the renal team to protect residual function",
          "Avoid all imaging", "Stop dialysis before the study"],
         1, "Residual function is worth protecting; minimize nephrotoxic exposure."),
        ("What does the Philippine Association of Thoracic and Cardiovascular Surgery (PATACSI) directory of accredited programs establish?",
         ["Every board eligibility rule", "Which programs are accredited for TCVS training, which helps verify training evidence",
          "Hospital privileges", "PhilHealth accreditation"],
         1, "It is a verification tool, not a complete eligibility standard."),
    ],
    "terms": [("Medial calcification", "Calcium deposits in the artery wall, common in kidney failure."),
              ("Toe pressure", "Blood pressure measured at the toe, more reliable than ankle pressure when arteries are calcified.")],
    "readings": [("contrast-nephropathy.html", "Contrast and the kidney."),
                 ("cardiovascular-death-dialysis.html", "Vascular disease in dialysis patients."),
                 ("kidney-transplant.html", "The transplant pathway.")],
    "calcs": ["calc-abi.html", "calc-egfr-ckd-epi.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
