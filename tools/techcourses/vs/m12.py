# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 12: Thrombosis and urgent dialysis. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "In an emergency bay, a patient sits upright with oxygen while a surgeon feels a silent arm graft and a nephrologist reviews a potassium result.",
    "objectives": [
        "Treat a thrombosed access as two problems at once: dialysis safety and access salvage.",
        "Explain why access clots form, and why salvage that ignores the cause fails again.",
        "Compare surgical and endovascular thrombectomy using the randomized evidence and its gaps.",
        "Record times, owners and the contingency so the patient is never left between teams.",
    ],
    "big": """
{{plain:When the only bridge into a town collapses, two jobs start at once. Someone must get food and medicine into the town today, by boat if needed. Someone else must rebuild the bridge. If everyone works on the bridge, the town starves while they work.}}
<p>The picture has a limit. A bridge collapses from its own weakness. An access usually clots because something downstream narrowed it, or because flow fell: hypotension after a long session, compression while sleeping, or dehydration. Rebuilding without fixing that cause is rebuilding the same weak bridge.</p>
{{cards:Key terms for this module|Access thrombosis::Clotting of a fistula or graft so that flow stops.|Thrombectomy::Removing clot, surgically or with endovascular devices.|Culprit lesion::The stenosis or other cause that led to the clot.|Bridge access::A temporary catheter used while the access is salvaged or replaced.|Salvage window::The time within which clot removal is more likely to succeed.}}
<p>Your work is to make sure the patient&rsquo;s immediate danger, usually potassium and fluid after a missed session, is managed now, while you plan the rescue and treat the cause.</p>
""",
    "case": {"title": "The declot list is tomorrow", "html": """
<p>Mr. Alfredo Ramos, 68, has a left upper-arm graft. He missed his Saturday session because the graft was silent when he woke. It is now Monday, 10:30 a.m. He arrives at your hospital&rsquo;s emergency department breathless, sitting upright, with ankle edema. His potassium is 7.1 mmol/L and the electrocardiogram shows wide QRS complexes. The emergency physician calls you: &ldquo;Graft is clotted. Your declot list is tomorrow morning. Can we admit him and wait?&rdquo;</p>
""", "questions": [
        "What must happen in the next hour, and who owns it?",
        "How do you plan the salvage?",
        "What do you need to find and fix at the time of salvage?"]},
    "sections": [
        ("two", "Two problems", "Two problems, two owners, one timeline", """
<p>The danger of access thrombosis is rarely the clot. It is the dialysis the patient has missed. Potassium rises between sessions because, in kidney failure from chronic kidney disease (CKD), nothing excretes it; fluid accumulates. A patient who missed a session over a weekend can reach a lethal potassium and pulmonary edema. These need emergency medical treatment and, often, dialysis through a temporary catheter, today. That decision belongs to the emergency team and the nephrologist.</p>
{{fig:vs12_a}}
<p>Salvage belongs to you or the interventionist, and it can run in parallel. Ask when the last successful session was, how long the access has been silent, whether the patient is stable enough for a procedure, and what rescue services exist today. Agree with the nephrologist whether a catheter is placed first, and where, so it does not harm the arm you are trying to save.</p>
{{flow:Parallel pathway for a clotted access|Assess the patient::Potassium, electrocardiogram, oxygen, blood pressure, volume.|Treat the threat::Emergency potassium treatment and dialysis as the nephrologist directs.|Plan the bridge::Temporary catheter site chosen to protect the access arm.|Plan salvage::Surgical or endovascular, today or at a set time, with a named operator.|Find the cause::Image the whole circuit and treat the culprit lesion.|Close the loop::Next dialysis session booked and confirmed with the unit.}}
{{call:A patient with a clotted access who is breathless, has a dangerous potassium or electrocardiographic changes, or has missed dialysis needs emergency assessment now. Salvage scheduling never replaces that.}}
"""),
        ("why", "Why clots form", "Why accesses clot, and why the cause matters", """
<p>Most graft thromboses follow a venous anastomotic or outflow stenosis that has gradually lowered flow until it falls below the threshold at which blood stays liquid. Fistulas clot from juxta-anastomotic or outflow stenosis, from low pressure (intradialytic hypotension, dehydration), from compression, or from a hypercoagulable state. Removing the clot restores flow but leaves the stenosis; the access clots again unless the culprit is treated.</p>
{{fig:vs12_b}}
<p>The UK Kidney Association (UKKA) 2025 guideline recommends either an endovascular or surgical approach to salvage based on local expertise, with surgical approaches followed by treatment of the underlying culprit stenosis (statement 4.5, grade 1C).[[vs_ukka]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Clue</th><th>Likely cause</th><th>Implication at salvage</th></tr></thead>
<tbody>
<tr><td>Rising venous pressures and prolonged bleeding before the clot</td><td>Outflow stenosis</td><td>Image and treat the outflow</td></tr>
<tr><td>Weak, flat access in the weeks before</td><td>Inflow or juxta-anastomotic stenosis</td><td>Image the arterial side</td></tr>
<tr><td>Clot after a hypotensive session or diarrhea</td><td>Low flow from low pressure</td><td>Review dry weight and drugs with the nephrologist</td></tr>
<tr><td>Repeated clots without a lesion</td><td>Hypercoagulability or compression</td><td>Consider testing and patient education</td></tr>
</tbody></table></div>
"""),
        ("choice", "Choosing the rescue", "Surgical or endovascular: what the evidence shows", """
<p>Kuhan and colleagues found six randomized trials, all in thrombosed grafts, with 573 grafts. Technical success, need for a temporary line and 30-day primary patency were similar between surgery and endovascular therapy; one-year primary patency did not differ significantly, and a single study suggested better assisted patency with surgery. There were no randomized trials for native fistulas.[[vs_kuhan2013]] Choice therefore rests on local expertise, the anatomy, the age of the clot and what remains for the future.</p>
<p>A restored image is not the end. Confirm that the access supports dialysis at the next session, and decide what happens if rescue fails: who places a catheter, where, and when the next access discussion happens. Record the times: when the access was found silent, when the patient was assessed, when salvage was done. Delays between teams are where these patients come to harm.</p>
{{scene:Weekend on-call, fictional|<p>A fistula patient calls the unit on Sunday: no thrill since morning, no breathlessness, potassium last Friday normal. The nephrologist arranges a potassium check and a Monday dialysis plan; you book an early Monday fistulogram and possible thrombectomy, and the unit reads the plan back.</p><p class="tc-scene-take"><b>What this shows.</b> A stable patient can wait hours for salvage when dialysis safety has an owner and a time.</p>}}
{{key:Remove the clot, then find and fix the reason it formed. Otherwise you will meet it again.}}
"""),
    ],
    "debrief": [
        "<p><strong>The next hour.</strong> This is a medical emergency. The emergency team treats the potassium now (cardiac membrane stabilization and measures that shift potassium into cells, per protocol) and the nephrologist arranges urgent dialysis, which needs a temporary catheter. You advise on catheter site: a right internal jugular line protects the left arm. Waiting for tomorrow&rsquo;s list would be unsafe.</p>",
        "<p><strong>Salvage.</strong> Once he is stabilized and dialyzed, plan thrombectomy, endovascular or surgical according to local expertise, today if possible or at a fixed time tomorrow, with a named operator. The graft has been silent since Saturday; the longer the delay, the harder salvage may be.</p>",
        "<p><strong>The cause.</strong> Image the whole circuit at salvage. A graft clot is usually a venous anastomotic or outflow stenosis; treat it, which in a graft may mean a stent graft (Module 11). Check whether low blood pressure or dehydration contributed. Book his next session through the graft only after flow is confirmed, and set the catheter&rsquo;s removal date.</p>",
    ],
    "skills": {"title": "Parallel salvage and dialysis plan",
               "intro": "Emergency station simulation or supervised emergency case.",
               "items": [("Asks first about the last session, potassium, electrocardiogram and breathing", True),
                         ("Contacts the nephrologist and emergency team for dialysis safety in parallel", True),
                         ("Advises a bridge catheter site that protects the access arm", False),
                         ("Agrees salvage approach, operator and time", False),
                         ("Plans imaging and treatment of the culprit lesion", False),
                         ("Confirms the next dialysis session with the unit", False)],
               "placement": "Emergency station or on-call"},
    "quiz": [
        ("A patient with a thrombosed graft is breathless after a missed session. What is the priority?",
         ["Wait for tomorrow&rsquo;s declot list", "Finish elective consent first",
          "Urgent medical and dialysis assessment alongside salvage planning", "Discharge with anticoagulation"],
         2, "The immediate threat and access rescue need parallel coordination."),
        ("A salvage plan should also address what?",
         ["The underlying cause, the next dialysis session and a failure contingency", "Only clot removal",
          "Only the next imaging appointment", "Only the cost"],
         0, "Restoring flow without fixing the cause or planning dialysis leaves the problem unresolved."),
        ("What is the commonest cause of graft thrombosis?",
         ["Arterial embolism", "Venous anastomotic or outflow stenosis", "Infection", "High potassium"],
         1, "Hyperplasia at the venous end gradually lowers flow until the graft clots."),
        ("The meta-analysis of randomized trials comparing surgical and endovascular thrombectomy found what?",
         ["Surgery clearly superior in fistulas", "Similar 30-day outcomes in grafts; no randomized trials in fistulas",
          "Endovascular therapy doubled mortality", "Both had identical five-year outcomes"],
         1, "Six trials, 573 grafts; fistula evidence was absent."),
        ("Where should a bridge catheter go for a patient trying to save a left-arm graft?",
         ["Left subclavian", "Right internal jugular, if available", "Left internal jugular always", "Any site, it does not matter"],
         1, "Choose a site that protects the access arm&rsquo;s central outflow."),
    ],
    "terms": [("Membrane stabilization", "Treatment that protects the heart from high potassium while the level is lowered."),
              ("Culprit lesion", "The narrowing that caused an access to clot.")],
    "readings": [("potassium-hyperkalemia-ckd.html", "Why potassium becomes dangerous after a missed session."),
                 ("dialysis-access-care.html", "What patients should do if the thrill is gone.")],
    "calcs": ["calc-potassium-load.html", "calc-catheter-exposure.html", "calc-access-intervention-burden.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
