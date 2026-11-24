# -*- coding: utf-8 -*-
"""PhilHealth Claims, Module 10: Renal Pathways and the Patient Handoff."""

MODULE = {
    "image_alt": "A young woman walks with a male nurse in a bright hospital corridor that branches into three hallways marked with wordless pictograms.",
    "objectives": [
        "Explain in plain words why acute kidney injury and chronic kidney disease stage 5 lead to different benefits.",
        "Route a case by the clinician-documented diagnosis and modality: maintenance hemodialysis, emergency hemodialysis, acute kidney injury, peritoneal dialysis, or transplant.",
        "Describe the Z benefits for peritoneal dialysis and transplantation at the level a liaison needs, with their contracting requirements.",
        "Close the loop on a referral with an owner, an acknowledgment, and a callback time.",
        "Distinguish verified coverage from a pending determination when talking to a family.",
    ],
    "big": """
{{plain:The same two kidneys can fail in two very different ways. Acute kidney injury is a sudden injury, like a sprained ankle: dialysis is a crutch while the kidney may heal. Chronic kidney disease stage 5 is a lasting loss, like a lost limb: dialysis or a transplant replaces what will not come back.}}
<p>The picture has a limit: some patients with acute injury do not recover and move on to chronic disease, and only the nephrologist can say which is happening. That is why the documented diagnosis, not the machine or the room, decides which benefit a session belongs to, and why claims staff never route a case by convenience.</p>
{{fig:pc_pathways}}
{{cards:Key terms for this module|Acute kidney injury (AKI)::A sudden, possibly reversible fall in kidney function.|Maintenance hemodialysis::Regular sessions, usually three a week, for chronic kidney disease stage 5.|Peritoneal dialysis (PD)::Dialysis using the lining of the abdomen, done at home.|Z benefits::PhilHealth packages for high-cost conditions, delivered by contracted facilities.|Contracted provider::A facility under contract with PhilHealth for a specific Z benefit.|Callback::An agreed time when a named person will contact the patient with the next step.}}
""",
    "case": {"title": "Three requests at one desk", "html": """
<p>In one afternoon the liaison, Ms. Carla Mendoza, receives three requests. A hospital asks how to file for a patient discharged after temporary dialysis for acute kidney injury. Ms. Grace Lim (fictional, SIM-10), 28, on maintenance hemodialysis, asks to be evaluated for a kidney transplant and says a friend told her &ldquo;PhilHealth pays for everything at any hospital.&rdquo; And a stage 5 patient of the unit received emergency hemodialysis during a three-day confinement for pneumonia.</p>
""", "questions": ["Who owns each request, and which pathway does each follow?",
                  "What do you tell Ms. Lim about the transplant benefit, and what is the next step?",
                  "What does your unit record about the emergency session?"]},
    "sections": [
        ("routes", "Five routes", "Route by the documented diagnosis", """
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>Documentation that triggers it</th><th>Route and owner</th></tr></thead>
<tbody>
<tr><td>Chronic kidney disease stage 5 on maintenance hemodialysis</td><td>Clinician-documented stage 5, PDD registration</td><td>Hemodialysis package (Modules 2 to 8)</td></tr>
<tr><td>Emergency hemodialysis in stage 5 disease</td><td>Documented emergency session</td><td>Hemodialysis package, filed by the rendering facility; counts toward the 156 (Module 4)</td></tr>
<tr><td>Dialysis for acute kidney injury</td><td>Clinician-documented acute injury</td><td>Hospital coding and claims review, under the applicable case rate</td></tr>
<tr><td>Peritoneal dialysis</td><td>Stage 5, PDD registration, contracted provider</td><td>Z benefit for peritoneal dialysis</td></tr>
<tr><td>Kidney transplant and aftercare</td><td>Transplant evaluation by a contracted center</td><td>Z benefit for kidney transplantation and post-transplant services</td></tr>
</tbody></table></div>
<p>A facility accredited for hemodialysis may need a separate contract to deliver a Z benefit. Verify contracting, any pre-authorization, forms, and deadlines with the receiving service before the patient is told anything definite.</p>
"""),
        ("zbenefits", "Z benefits", "Peritoneal dialysis and transplant benefits", """
<p>PhilHealth&rsquo;s Z benefit for peritoneal dialysis, effective January 1, 2025, covers continuous ambulatory peritoneal dialysis for adults and both continuous ambulatory and automated peritoneal dialysis for children, with automated dialysis in children first piloted at named sites. Patients must be registered in the PDD.[[pc_pc2024_0036]][[pc_pa2025_0074]] PhilHealth announced annual coverage of up to about 1.2 million pesos for pediatric automated peritoneal dialysis, with adult coverage depending on the daily solution prescription.[[pc_news2025_pd]]</p>
<p>The kidney transplant Z benefit was raised under PhilHealth Circular 2024-0035, and post-transplant services were added under Circular 2025-0011.[[pc_pc2024_0035]][[pc_pc2025_0011]] Amounts differ by donor type and induction medicine; quote them only from the current circular, through the contracted center.</p>
{{key:A liaison explains which door a patient should knock on and helps them get there. The contracted service decides eligibility and amounts.}}
"""),
        ("handoff", "The handoff", "A handoff that closes the loop", """
<p>Use the patient&rsquo;s preferred language and agree an owner and a callback time. Separate what is verified (&ldquo;your eligibility is confirmed&rdquo;) from what is pending (&ldquo;the transplant center will tell us whether you qualify&rdquo;). If the patient has an urgent clinical concern, hand over directly to nursing or the treating team. Route possible financial help to the facility&rsquo;s social service.</p>
<div class="table-wrap"><table>
<thead><tr><th>Handoff field</th><th>Example (fictional)</th></tr></thead>
<tbody>
<tr><td>Verified status</td><td>Eligible; PDD registered; 98 sessions used this year</td></tr>
<tr><td>Last treatment</td><td>Wednesday, completed</td></tr>
<tr><td>Open questions</td><td>Transplant evaluation pathway and pre-authorization</td></tr>
<tr><td>Authorized receiver</td><td>Transplant coordinator, contracted center</td></tr>
<tr><td>Next action and callback</td><td>Referral acknowledged by Friday; callback to patient before 3 PM Friday</td></tr>
</tbody></table></div>
<p>A callback line in Filipino: &ldquo;Tatawagan ko po kayo bukas bago mag-alas tres para sabihin ang susunod na hakbang.&rdquo; (&ldquo;I will call you tomorrow before three o&rsquo;clock to tell you the next step.&rdquo;)</p>
"""),
    ],
    "debrief": ["""
<p><strong>Owners and routes.</strong> The acute kidney injury discharge goes to the hospital&rsquo;s own coding and claims review under the applicable case rate, not the maintenance hemodialysis package. Ms. Lim&rsquo;s request goes to her nephrologist and the contracted transplant center&rsquo;s coordinator. The emergency session during the pneumonia stay is a hemodialysis-package session filed by the hospital.</p>
<p><strong>What to tell Ms. Lim.</strong> That PhilHealth has a Z benefit for kidney transplantation, delivered only through contracted centers, and that the center will assess whether she qualifies and explain the coverage. Record her request, contact the nephrologist and coordinator, confirm the referral is received, and agree a callback time.</p>
<p><strong>The emergency session.</strong> Record it in the ledger as consumed (#n of 156), keep the hospital&rsquo;s claim reference, and do not bill that date. The hospital codes and files its confinement claim, with a CF5 attached if the discharge is on or after August 1, 2026 (Module 5).</p>
"""],
    "skills": {"title": "Routing and closed-loop handoff",
               "intro": "Route five fictional requests and complete one handoff, including the callback, with a supervisor playing the patient.",
               "items": [
                   ("Routes each case by the clinician-documented diagnosis and modality.", True),
                   ("Verifies contracting and pre-authorization before giving definite answers about a Z benefit.", False),
                   ("Separates verified coverage from pending determinations in plain language.", False),
                   ("Hands over urgent clinical concerns directly to nursing.", True),
                   ("Closes the loop with an owner, an acknowledgment, and a callback time.", False),
               ],
               "placement": "Follow one transfer or referral at your unit from request to acknowledgment."},
    "quiz": [
        ("Can the maintenance stage 5 allowance be assumed for temporary dialysis for acute kidney injury?",
         ["Yes", "No; route it to hospital claims review under the applicable pathway", "Only for one week", "Only if the patient agrees"], 1,
         "The diagnosis decides the route."),
        ("What belongs in a transfer handoff?",
         ["Only the patient&rsquo;s name", "Verified status, last treatment, utilization, open questions, authorized receiver, and next action", "The patient&rsquo;s full chart", "A photo"], 1,
         "Close the loop."),
        ("Does peritoneal dialysis under the Z benefit require PDD registration?",
         ["No", "Yes", "Only for children", "Only for automated PD"], 1,
         "Circular 2024-0036."),
        ("A hemodialysis-accredited center wants to bill a transplant work-up under the Z benefit. Allowed?",
         ["Always", "Only if it is a contracted Z provider for that package", "Never for anyone", "Only on weekends"], 1,
         "Contracting is separate from HD accreditation."),
        ("A patient on AKI dialysis is discharged still needing dialysis. Who decides the pathway?",
         ["The clerk", "The nephrologist documents the diagnosis; hospital coding routes the claim", "PhilHealth&rsquo;s hotline", "The family"], 1,
         "Some patients progress to chronic disease."),
        ("Why do AKI and stage 5 chronic kidney disease (CKD) lead to different benefits?",
         ["Different machines", "AKI is sudden and may recover; stage 5 is a lasting loss", "Different rooms", "They do not"], 1,
         "Crutch versus replacement."),
        ("A patient says PhilHealth pays for a transplant at any hospital. What is accurate?",
         ["Yes, any hospital", "The Z benefit is delivered through contracted centers, which assess eligibility", "Transplants are not covered", "Only private hospitals"], 1,
         "Verify with the receiving service."),
        ("Who quotes the amount of a Z benefit to the patient?",
         ["The clerk from memory", "The contracted service, from the current circular", "A friend", "The vendor"], 1,
         "Amounts change by circular."),
        ("A patient asks to switch to peritoneal dialysis next month. First step?",
         ["Cancel HD", "Record the request, contact the clinical team and a contracted PD coordinator, and agree a callback", "Tell them it is impossible", "Send them to PhilHealth"], 1,
         "Close the loop."),
        ("What does &ldquo;closing the loop&rdquo; on a referral need?",
         ["A phone call only", "An owner, an acknowledgment of receipt, and a callback time", "A signature from PhilHealth", "Nothing"], 1,
         "A referral sent is not a referral received."),
        ("An emergency HD session during a confinement: what does your unit record?",
         ["Nothing", "The session as consumed, with the hospital&rsquo;s claim reference, and no billing for that date", "A new claim", "A denial"], 1,
         "The hospital files it."),
        ("A patient raises an urgent symptom during a coverage conversation. What do you do?",
         ["Finish the explanation", "Hand over directly to nursing or the treating team", "Schedule a call", "Write it down for later"], 1,
         "Clinical first, always."),
        ("Which phrase separates verified from pending?",
         ["&ldquo;You are covered for everything.&rdquo;", "&ldquo;Your eligibility is confirmed; the center will tell us whether you qualify for the transplant benefit.&rdquo;", "&ldquo;Ask PhilHealth.&rdquo;", "&ldquo;Don&rsquo;t worry.&rdquo;"], 1,
         "Never promise what is not yet determined."),
        ("Where does possible financial help go?",
         ["Nowhere", "The facility&rsquo;s social service pathway", "PhilHealth directly", "The nurse"], 1,
         "Route it; do not improvise."),
        ("Which document decides which benefit a session belongs to?",
         ["The room number", "The clinician-documented diagnosis and modality", "The schedule", "The bill"], 1,
         "Never route by convenience."),
    ],
    "terms": [("Acute kidney injury", "A sudden, possibly reversible fall in kidney function (AKI)."),
              ("Maintenance hemodialysis", "Regular sessions for chronic kidney disease stage 5."),
              ("Peritoneal dialysis", "Dialysis using the lining of the abdomen (PD)."),
              ("Z benefits", "PhilHealth packages for high-cost conditions, delivered by contracted facilities."),
              ("Contracted provider", "A facility under contract with PhilHealth for a specific Z benefit."),
              ("Callback", "An agreed time when a named person will contact the patient.")],
    "readings": [("philhealth-z-packages.html", "PhilHealth&rsquo;s Z benefit packages for kidney patients."),
                 ("peritoneal-dialysis-ckd.html", "Peritoneal dialysis explained for patients and families."),
                 ("kidney-transplant.html", "Kidney transplantation: who qualifies and what to expect.")],
    "calcs": ["calc-philhealth-claims-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("pc_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
