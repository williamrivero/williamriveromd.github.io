# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 11: Stenosis and endovascular choices. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "An angiography suite with a fistulogram on the monitor showing a narrowing at the cephalic arch, an access team discussing it.",
    "objectives": [
        "Explain why balloon angioplasty restenoses, and how drug-coated balloons and stent grafts aim to delay it.",
        "Interpret the stent-graft and drug-coated balloon trials in absolute terms, with their endpoints and funding.",
        "Weigh surgical revision against endovascular treatment for a given lesion and patient.",
        "Protect future access when choosing where a device is placed.",
    ],
    "big": """
{{plain:Balloon angioplasty is like stretching a tight sleeve. It opens, but cloth that was stretched by force tends to shrink back. Lining the sleeve, or coating it with something that stops it shrinking, can make the stretch last longer.}}
<p>The picture has a limit. Cloth only recoils. A vein wall injured by a balloon also heals, and its healing is the same neointimal hyperplasia that caused the lesion. Restenosis is partly elastic recoil and partly a new round of scar. Paclitaxel on a balloon slows the cells that drive that scar; a covered stent graft holds the lumen open and walls off the healing tissue, at the cost of leaving metal and fabric in the vein.</p>
{{cards:Key terms for this module|Percutaneous transluminal angioplasty (PTA)::Dilating a stenosis with a balloon from inside the vessel.|Drug-coated balloon (DCB)::A balloon coated with an antiproliferative drug, usually paclitaxel.|Stent graft::A covered metal stent that lines the vessel.|Target-lesion primary patency::Freedom from repeat treatment of the treated lesion or circuit thrombosis.|Cephalic arch::The curve where the cephalic vein joins the axillary vein, a common stenosis site.}}
<p>Every treatment of a stenosis should answer one question: which lesion causes the patient&rsquo;s problem, and how will treating it restore use? Your work is to choose the option that does that with the least burden, and that leaves the next site intact.</p>
""",
    "case": {"title": "The convenient stent", "html": """
<p>Mrs. Norma Salazar, 61, has a left upper-arm graft with recurrent stenosis at the venous anastomosis, treated with angioplasty three times in nine months. Venous pressures are rising again and the last session ran at reduced flow. On today&rsquo;s fistulogram, the lesion sits 1 cm from the junction of the basilic and axillary veins.</p>
<p>The interventionist, Dr. Wilfredo Cruz, proposes a stent graft. The easiest landing zone would extend across the axillary junction into the axillary vein. Your access plan for Mrs. Salazar names a left axillary-based graft extension as her contingency if this graft fails.</p>
""", "questions": [
        "Is a stent graft reasonable for this lesion?",
        "What concerns you about the proposed landing zone?",
        "What will you agree with Dr. Cruz before the device is placed?"]},
    "sections": [
        ("mechanism", "Why lesions return", "Why stenoses come back after angioplasty", """
<p>A balloon opens a stenosis by stretching and tearing the vessel wall. That injury triggers platelet deposition, inflammation and smooth muscle proliferation. Within months the lumen narrows again. Fistula lesions often respond better than graft venous anastomotic lesions, where turbulence and compliance mismatch keep driving hyperplasia. Recurrent lesions despite repeated angioplasty are a sign that the cause is still active.</p>
{{fig:vs11_a}}
<p>The UK Kidney Association (UKKA) 2025 guideline suggests endovascular treatment as the first approach for non-complex access stenosis, using high-pressure balloons where needed (statement 4.3, grade 2C), and recommends covered stents for stenosis at the graft&ndash;vein anastomosis after adequate balloon dilation (4.4, grade 1C).[[vs_ukka]]</p>
"""),
        ("evidence", "Device evidence", "What the device trials show", """
<p>Haskal and colleagues randomized 190 patients with venous anastomotic stenosis in failing grafts to balloon angioplasty alone or angioplasty plus a covered stent graft. At six months, treatment-area patency was 51% with the stent graft and 23% with angioplasty; patency of the whole access circuit was 38% versus 20%; freedom from further intervention was 32% versus 16%.[[vs_haskal2010]] The benefit was real, but even with a stent graft, most circuits needed another procedure within six months. The trial addressed graft venous anastomoses, not fistula lesions.</p>
<p>In fistulas, Lookstein and colleagues randomized 330 patients after successful high-pressure angioplasty to a paclitaxel drug-coated balloon or a standard balloon. Six-month target-lesion primary patency was 82.2% versus 59.5%, an absolute difference of 22.8 percentage points, about one extra patent lesion for every four or five patients treated. Serious access-circuit adverse events at 30 days were similar (4.2% versus 4.4%).[[vs_lookstein2020]] The trial was funded by the manufacturer, its primary endpoint was a surrogate at six months, and it was not designed to detect differences in survival. In leg arteries, a meta-analysis of randomized trials found higher mortality at two years after paclitaxel devices (7.2% versus 3.8%), a signal that later analyses have debated.[[vs_katsanos2018]] A dialysis-access trial of this size cannot settle that question either way; discuss it with the patient.</p>
<div class="table-wrap"><table>
<thead><tr><th>Option</th><th>Best evidence</th><th>Effect</th><th>Caveat</th></tr></thead>
<tbody>
<tr><td>Plain PTA</td><td>Comparator arm in trials</td><td>Opens most lesions; frequent restenosis</td><td>Repeat treatments common</td></tr>
<tr><td>Stent graft, graft venous anastomosis</td><td>RCT, n=190</td><td>6-month treatment-area patency 51% vs 23%</td><td>Metal in the vein; landing zone matters</td></tr>
<tr><td>Drug-coated balloon, fistula lesions</td><td>RCT, n=330</td><td>6-month target-lesion patency 82.2% vs 59.5%</td><td>Industry funded; surrogate endpoint</td></tr>
<tr><td>Surgical revision</td><td>Mostly observational</td><td>Durable for some lesions</td><td>Uses vein; needs an operation</td></tr>
</tbody></table></div>
{{key:Technical success on the image is not the endpoint. A functioning dialysis pathway, with acceptable burden for the patient, is.}}
"""),
        ("future", "Protecting the future", "Choosing a device that protects the next site", """
<p>A stent graft that crosses a venous junction can cover the inflow of a vein needed for a future access, or jail a branch. A stent across the cephalic arch can make a later surgical revision harder. A device in a cannulation segment cannot be needled through safely. Before the device is placed, the access team should agree on where it may land, using the patient&rsquo;s Life-Plan.</p>
{{fig:vs11_b}}
<p>Surgery remains an option. A short lesion may be revised with a patch or a jump graft; a recurrent cephalic arch stenosis may be bypassed. Compare likely benefit, recurrence, procedural burden and the effect on later access. Preserve the images and write the rationale so the next operator understands the altered anatomy.</p>
{{scene:Access conference, fictional|<p>A fistula with recurrent cephalic arch stenosis has had five angioplasties in a year. The team discusses a stent graft versus a surgical cephalic vein transposition. The patient chooses surgery after hearing that it may last longer but needs an operation; the plan records why.</p><p class="tc-scene-take"><b>What this shows.</b> Recurrence is a reason to reconsider the strategy, not to repeat it.</p>}}
{{call:Stop and reconsider with the access team before placing a device that would cover a venous junction, a cannulation segment, or a vein named in the patient&rsquo;s contingency plan.}}
"""),
    ],
    "debrief": [
        "<p><strong>Is a stent graft reasonable?</strong> Yes. A recurrent graft venous anastomotic stenosis after repeated angioplasty is the lesion in which stent grafts were tested, and UKKA recommends covered stents there after adequate balloon dilation (grade 1C).</p>",
        "<p><strong>The landing zone.</strong> Extending across the basilic&ndash;axillary junction risks covering the axillary vein that is her contingency. A convenient deployment could consume her next access.</p>",
        "<p><strong>What to agree.</strong> Before deployment, agree with Dr. Cruz on a landing zone that ends before the axillary junction if technically safe, or on an alternative such as a surgical jump graft. Record what success means for her (reliable dialysis at the prescribed flow), when she will be reassessed, and save the images with a note of the device position for the next operator.</p>",
    ],
    "skills": {"title": "Intervention decision with future-site review",
               "intro": "Conference or supervised angiography list.",
               "items": [("Correlates the lesion with the clinical problem", False),
                         ("Compares endovascular and surgical options with their evidence", False),
                         ("Reviews the device&rsquo;s effect on cannulation segments and future sites", True),
                         ("States follow-up measures and what triggers reassessment", False),
                         ("Records the rationale and device position for the next operator", False)],
               "placement": "Access conference or angiography suite"},
    "quiz": [
        ("Before placing a device across a venous junction, what should be reviewed?",
         ["Its effect on cannulation and future access options", "Only the convenience of deployment",
          "Only the immediate image", "Only the device cost"],
         0, "A technically successful intervention can consume later options."),
        ("What is the most meaningful question after treatment?",
         ["Was the device expensive?", "Did the patient regain the intended access function with acceptable burden?",
          "Was the procedure note long?", "Was the residual stenosis under 10%?"],
         1, "Functional benefit and patient experience complement technical outcome."),
        ("In the Haskal trial for graft venous anastomotic stenosis, what was six-month treatment-area patency?",
         ["51% with stent graft versus 23% with angioplasty", "95% versus 90%", "No difference", "23% versus 51% favoring angioplasty"],
         0, "Circuit patency was 38% versus 20%; most circuits still needed more procedures."),
        ("Which is a limitation of the drug-coated balloon trial in fistulas?",
         ["It was not randomized", "It used a six-month surrogate endpoint and was industry funded",
          "It showed higher 30-day adverse events", "It enrolled only grafts"],
         1, "Target-lesion patency at six months is a surrogate; the sponsor was the manufacturer."),
        ("Why do stenoses recur after balloon angioplasty?",
         ["The balloon leaves debris", "Elastic recoil and a new round of neointimal hyperplasia from wall injury",
          "Patients stop antiplatelets", "Contrast damages the vein"],
         1, "Injury from dilation triggers the same healing response that caused the lesion."),
    ],
    "terms": [("Landing zone", "Where the ends of a stent or stent graft sit in the vessel."),
              ("Jump graft", "A short graft that bypasses a stenotic segment.")],
    "readings": [("hemodialysis-access-lifeline.html", "Keeping an access working over years."),
                 ("avf-aneurysm-and-changes.html", "Fistula changes and when they matter.")],
    "calcs": ["calc-access-intervention-burden.html", "calc-av-access-outcome-audit.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
