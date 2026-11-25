# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 16: High flow and central venous obstruction. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A multidisciplinary meeting where a surgeon, a cardiologist and a nephrologist review an echocardiogram and an access flow study side by side.",
    "objectives": [
        "Explain how an access adds to cardiac work, and when access flow may contribute to heart failure.",
        "Formulate a differential for breathlessness or arm swelling in a patient with an access before choosing an intervention.",
        "Interpret the evidence on access flow thresholds and central venous stenosis management, with its limits.",
        "Weigh how reducing flow, restoring outflow or abandoning access would affect symptoms, dialysis and future options.",
    ],
    "big": """
{{plain:An access is a hole in the circulation&rsquo;s plumbing that lets blood skip the tissues and go straight back to the heart. The heart must pump that extra blood on every beat, like a household pump running with a tap left open.}}
<p>The picture has a limit. A pump either copes or fails. The heart adapts: it increases output, and the chambers can enlarge. Most patients tolerate an access well, and breathlessness in a dialysis patient has many causes, fluid above all. An access contributes to heart failure only in some patients, usually with high flow, and proving that it does requires evidence, not assumption.</p>
{{cards:Key terms for this module|Access flow (Qa)::The blood flow through the fistula or graft, usually in liters per minute.|Cardiac output::The blood the heart pumps per minute.|High-output heart failure::Heart failure with high cardiac output, driven by a large shunt or other cause.|Central venous stenosis::Narrowing of large chest veins, often after catheters.|Banding::Narrowing an access to reduce its flow.}}
<p>Your work is to state the mechanism you suspect, gather the evidence that would support or refute it, and avoid both automatic ligation and automatic dismissal of the access.</p>
""",
    "case": {"title": "Breathless despite dry weight", "html": """
<p>Mr. Lorenzo Pineda, 55, has a left brachiocephalic fistula created four years ago. Over six months he has become breathless climbing one flight of stairs, despite his nephrologist lowering his target weight twice. He has no chest pain. His echocardiogram shows a dilated left ventricle with normal ejection fraction and moderate pulmonary hypertension. A duplex reports access flow of 2.8 L/min. His left arm is not swollen.</p>
<p>His nephrologist writes: &ldquo;Fistula too big? Please ligate.&rdquo; Mr. Pineda is on the transplant waiting list and would like to keep the fistula.</p>
""", "questions": [
        "What mechanisms could explain his breathlessness?",
        "What evidence would support an access contribution?",
        "What options exist short of ligation, and what would each cost him?"]},
    "sections": [
        ("physiology", "Physiology", "How an access loads the heart", """
<p>Blood flowing through an access bypasses the arteriolar resistance of the arm, so systemic vascular resistance falls and venous return rises. The heart responds by increasing stroke volume and rate; over time, the left ventricle and atria can enlarge. The UK Kidney Association (UKKA) 2025 guideline notes that an access usually increases cardiac output by at least 15%, most markedly with larger, usually upper-arm, fistulas, but that most of these changes cause no symptoms.[[vs_ukka]]</p>
{{fig:vs16_a}}
<p>Basile and colleagues measured access flow and cardiac output in 96 patients. Upper-arm fistulas had higher flow (mean 1.58 L/min versus 0.95 for forearm fistulas) and were associated with high-output heart failure. Access flow of 2.0 L/min or more predicted high-output failure with a sensitivity of 89% and specificity of 100% in that cohort.[[vs_basile2008]] It was a small single-center study with ten cases of heart failure, so treat 2.0 L/min as a prompt to investigate, not a diagnosis.</p>
<div class="table-wrap"><table>
<thead><tr><th>Possible cause of breathlessness</th><th>Supporting clues</th></tr></thead>
<tbody>
<tr><td>Volume overload</td><td>Weight above target, edema, improves with fluid removal</td></tr>
<tr><td>Access-related high output</td><td>High access flow, high cardiac output, dilated chambers, symptoms improve with brief access compression</td></tr>
<tr><td>Ischemic or valvular heart disease</td><td>Angina, wall-motion abnormality, valve lesion</td></tr>
<tr><td>Anemia</td><td>Low hemoglobin</td></tr>
<tr><td>Lung disease, pulmonary hypertension from other causes</td><td>History, imaging, lung function</td></tr>
</tbody></table></div>
{{key:State the mechanism before you choose the operation. Then name the finding that would prove you wrong.}}
"""),
        ("central", "Central veins", "Central venous stenosis: anatomy versus illness", """
<p>Central venous stenosis usually follows catheters or device leads (Modules 3 and 8). In an access arm it causes swelling of the arm, breast or face, venous collaterals, prolonged bleeding and high venous pressures. It may also be found on imaging in a patient with no symptoms. UKKA suggests a multidisciplinary approach that considers symptoms, access function, preference and the kidney replacement journey (statement 7.2, grade 2C), and that asymptomatic central venous stenosis be managed conservatively (7.3, grade 2C).[[vs_ukka]] Treating a lesion that is not causing a problem can injure the vein and accelerate restenosis.</p>
<p>When stenosis is symptomatic, options include angioplasty with or without a stent, reducing access flow to lower the venous load, surgical bypass, devices that bypass central obstruction (for example a graft connected to a catheter ending in the right atrium), or moving the access. Each has a cost to the future.</p>
{{call:Asymptomatic central venous findings and clinically important obstruction are different judgments. Treat the patient, not the image.}}
"""),
        ("options", "Options", "Weighing interventions with the team", """
<p>Before any irreversible step, define what result would support the working diagnosis. For high-output failure: does brief manual compression of the access slow the heart rate and lower cardiac output? Do symptoms improve after flow reduction? A multidisciplinary discussion with cardiology and nephrology avoids one specialty&rsquo;s fix becoming another&rsquo;s problem.</p>
{{fig:vs16_b}}
<p>Flow reduction (banding) aims to keep a usable access at lower flow. In a small series, banding in nine patients with cardiac overload lowered access flow from about 3.2 to 1.2 L/min, and accesses stayed functional over a mean of 30 months.[[vs_vanhoek2009]] It is a case series without controls. Ligation removes the load completely but sacrifices the access and may require a catheter, a cost that matters more for a patient awaiting transplant.</p>
{{scene:Multidisciplinary meeting, fictional|<p>A patient with a 3.1 L/min upper-arm fistula and breathlessness undergoes echocardiography during brief access compression: the heart rate falls by 12 beats per minute and cardiac output drops substantially. The team agrees on banding with a target flow, and to re-measure symptoms and output at three months.</p><p class="tc-scene-take"><b>What this shows.</b> A test that predicts the effect of the operation turns a guess into a plan.</p>}}
"""),
    ],
    "debrief": [
        "<p><strong>Mechanisms.</strong> Volume overload despite target-weight changes, access-related high output (flow 2.8 L/min, dilated left ventricle with preserved ejection fraction), pulmonary hypertension from other causes, coronary or valve disease, and anemia. They can coexist.</p>",
        "<p><strong>Supporting evidence.</strong> A measured cardiac output and the ratio of access flow to cardiac output; the response of heart rate and output to brief access compression; exclusion of anemia and ischemia; and a review of volume status by bioimpedance or clinical trend. Access flow over 2.0 L/min prompts this work-up but does not settle it.</p>",
        "<p><strong>Options.</strong> If the work-up supports an access contribution, banding to reduce flow could relieve symptoms while keeping a usable fistula until transplant. Ligation would remove the load but leave him needing other access. Present both to Mr. Pineda with the team&rsquo;s view, and agree on measures of success at follow-up.</p>",
    ],
    "skills": {"title": "Multidisciplinary problem formulation",
               "intro": "Case conference with cardiology and nephrology input.",
               "items": [("Builds a differential for breathlessness or swelling", False),
                         ("States the evidence needed to support an access contribution", True),
                         ("Compares the consequences of flow reduction, outflow treatment and ligation", False),
                         ("Avoids irreversible access loss without adequate assessment, outside emergencies", True),
                         ("Names review and follow-up owners and the measures of success", False)],
               "placement": "Multidisciplinary conference"},
    "quiz": [
        ("Recurrent breathlessness in a patient with an upper-arm access should lead to what?",
         ["Automatic ligation", "A coordinated differential assessment of volume, cardiac and access factors",
          "Automatic exclusion of an access contribution", "Doubling the dialysis time only"],
         1, "A plausible relationship needs evaluation before an irreversible decision."),
        ("How should an asymptomatic central venous stenosis on imaging be interpreted?",
         ["As an automatic indication for intervention", "As proof the patient cannot dialyze", "In its clinical and access context; usually managed conservatively",
          "As a reason to ligate the access"],
         2, "UKKA 7.3 (grade 2C) suggests conservative management when asymptomatic."),
        ("In Basile&rsquo;s study, access flow of what level predicted high-output heart failure most accurately?",
         ["0.5 L/min or more", "1.0 L/min or more", "2.0 L/min or more", "5.0 L/min or more"],
         2, "Sensitivity 89%, specificity 100% in a small single-center cohort; a prompt, not a diagnosis."),
        ("Why does an access increase cardiac work?",
         ["It raises systemic vascular resistance", "It lowers resistance and increases venous return, so the heart pumps more",
          "It reduces blood volume", "It slows the heart"],
         1, "The shunt bypasses arteriolar resistance; output rises to maintain pressure."),
        ("Which test helps predict whether flow reduction will help a patient with suspected high-output failure?",
         ["Serum albumin", "Response of heart rate and cardiac output to brief access compression", "Chest radiograph alone", "Urine output"],
         1, "A change on compression supports an access contribution."),
    ],
    "terms": [("Cardiopulmonary recirculation", "The share of cardiac output that passes through the access."),
              ("Bioimpedance", "A bedside measure of body water used to judge fluid status.")],
    "readings": [("heart-failure-ckd.html", "Heart failure in kidney disease."),
                 ("heart-kidney-connection.html", "How the heart and kidney influence each other."),
                 ("cardiovascular-death-dialysis.html", "Why cardiovascular disease dominates dialysis outcomes.")],
    "calcs": ["calc-access-flow-cardiac.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
