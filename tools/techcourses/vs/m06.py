# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 6: Plan and create an autogenous fistula. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A surgeon explains a simple drawing of a forearm fistula to a patient before surgery, the planned needle zone shaded on the drawing.",
    "objectives": [
        "Explain how a fistula matures, from shear stress to outward remodeling, and why some fail.",
        "Interpret the evidence on maturation rates and on drugs given to prevent early failure, separating surrogate from functional outcomes.",
        "Rehearse the intraoperative decisions an assessor observes: confirming the plan, responding to unexpected anatomy, and knowing when to stop.",
        "Write an operative handoff the dialysis unit can act on.",
    ],
    "big": """
{{plain:A new fistula is like a footpath that becomes a road. At first it is narrow. Heavy traffic wears it wider and firmer until trucks can use it. If the traffic is too light, or there is a bottleneck where the path joins the main road, it never becomes a road.}}
<p>The picture has a limit. A path widens because it is worn down; a vein widens because it is alive. High flow raises shear stress on the endothelium, which releases nitric oxide and other signals that make the vein dilate outward and thicken its wall. At the same time, injury at the anastomosis and the swing segment can trigger the opposite response, neointimal hyperplasia, which narrows the lumen from inside. Maturation is a race between these two.</p>
{{cards:Key terms for this module|Maturation::Growth of the fistula until it can support dialysis with two needles.|Shear stress::The drag of flowing blood on the vessel lining; it signals the vein to remodel.|Neointimal hyperplasia::Growth of smooth-muscle-like cells inside the vessel wall that narrows the lumen.|Swing segment::The first few centimeters of vein beyond the anastomosis, where stenosis often forms.|Functional patency::An access that is open and actually used for dialysis.}}
<p>Most of the outcome is decided before and soon after the operation: the choice of vessels, careful handling, and early follow-up. Your work in this module is planning and judgment. This course does not teach anastomotic technique; that is learned under supervision.</p>
""",
    "case": {"title": "The vein that was not there", "html": """
<p>Mr. Eduardo Bautista, 52, consented to a left radiocephalic fistula at the wrist. The consent form and your notes include a contingency: &ldquo;If the wrist vessels are unsuitable, proceed to a left forearm fistula higher up, or abandon and plan an upper-arm fistula at a later date.&rdquo; He is under a brachial plexus block.</p>
<p>At the wrist, the cephalic vein is thrombosed and cord-like for 3 cm, probably from an old intravenous line. The second-year resident suggests, &ldquo;The brachial artery and basilic vein look good. Let us do a brachiobasilic transposition now, he is already asleep.&rdquo; Your fellow, Dr. Paulo Santos, is assisting. The consultant on call is in another theater.</p>
""", "questions": [
        "What may you do within this consent?",
        "What should happen with the resident&rsquo;s suggestion?",
        "What must your operative note and handoff contain?"]},
    "sections": [
        ("maturation", "How fistulas mature", "Why fistulas mature, and why they fail", """
<p>After the anastomosis opens, flow in the artery and vein can rise many times within days. The vein responds to high shear stress by dilating outward and by thickening its wall so it can tolerate needles. The feeding artery also enlarges. Failure follows three main routes: inflow that cannot deliver enough flow, often from small or calcified arteries; a stenosis at the anastomosis or swing segment from neointimal hyperplasia; or a vein that is too deep, or has large side branches stealing flow, so the cannulation segment never develops.</p>
{{fig:vs06_a}}
<p>The Hemodialysis Fistula Maturation (HFM) study followed 535 new fistulas prospectively. Median time from creation to maturation was 115 days. Among patients already on dialysis, 29% of fistulas had matured by three months, 67% by six months and 76% by 12 months. Over a third needed an intervention to help maturation or manage a complication before maturing, and almost half of those that matured (47.5%) needed further intervention afterward. Functional patency of matured fistulas was 87% at one year and 75% at two years.[[vs_huber2021]] A meta-analysis of 62 cohorts found a primary failure rate of 23% and one-year secondary patency of 71%.[[vs_aljaishi2014]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Failure route</th><th>Mechanism</th><th>What you may notice</th></tr></thead>
<tbody>
<tr><td>Inflow</td><td>Small or calcified artery; proximal stenosis</td><td>Weak pulse in the fistula, low flow on duplex</td></tr>
<tr><td>Juxta-anastomotic stenosis</td><td>Neointimal hyperplasia at the swing segment</td><td>Strong pulse at the anastomosis, weak beyond it</td></tr>
<tr><td>Deep or branched vein</td><td>Flow diverted to side branches; segment too deep</td><td>Good flow but nothing to needle</td></tr>
<tr><td>Outflow</td><td>Central or cephalic arch stenosis</td><td>Pulsatile, firm fistula; arm swelling</td></tr>
</tbody></table></div>
{{key:A fistula has three or four months to win the race between remodeling and hyperplasia. Plan follow-up to find the losers early.}}
"""),
        ("drugs", "Evidence on adjuncts", "Can a drug improve maturation? What the trials show", """
<p>Several randomized trials asked whether a drug could reduce early failure. In the Dialysis Access Consortium (DAC) trial, 877 patients received clopidogrel or placebo for six weeks after fistula creation. Early thrombosis fell from 19.5% to 12.2% (relative risk 0.63), an absolute reduction of about 7 percentage points. But failure to become suitable for dialysis was unchanged: 61.8% with clopidogrel and 59.5% with placebo.[[vs_dember2008]] The drug moved a surrogate, early clotting, without improving the outcome that matters, a usable fistula.</p>
{{fig:vs06_b}}
<p>The FAVOURED trial randomized 567 patients to fish oil or placebo, and a subset to aspirin. Fistula failure at 12 months was 47% in both fish oil and placebo groups; aspirin did not reduce it either (45% versus 43%).[[vs_irish2017]] No drug is proven to make fistulas mature. Choose antiplatelet therapy for the patient&rsquo;s cardiovascular indication, not to rescue a fistula.</p>
<p>Technique and setting matter more, though the evidence is mostly observational. The UK Kidney Association (UKKA) 2025 guideline recommends establishing and maintaining surgical expertise (statement 3.6, grade 1C) and regular monitoring of new fistulas using &ldquo;look, feel and listen,&rdquo; supported by ultrasound where necessary (3.7, grade 1C).[[vs_ukka]] Endovascular fistula creation (endoAVF) is an alternative in selected anatomy; the NEAT study, single-arm and without a surgical comparator, reported 12-month primary and cumulative patency of 69% and 84%.[[vs_lok2017]]</p>
{{key:Surrogate success, a fistula that stays open, is not the same as functional success, a fistula that is used. Report and judge both.}}
"""),
        ("operating", "In the operating room", "Judgment in the operating room, and the handoff", """
<p>During supervised practice, the assessor watches your judgment as much as your hands: confirming the patient, side and plan; protecting nerves and side branches; responding to unexpected findings; assessing the immediate result (thrill, pulse, distal perfusion); and recognizing when to ask for help. Consent defines what you may do. A contingency written in the consent can be followed; an operation outside it, on a patient who cannot now discuss it, generally cannot, unless an emergency leaves no alternative.</p>
<p>The handoff turns the operation into a dialysis plan. It must reach the nephrologist and the dialysis unit, not just the chart.</p>
{{flow:The operative handoff|What was done::Configuration, artery and vein used, anything abandoned and why.|What was found::Vessel quality, thrombosed segments, central concerns.|Immediate result::Thrill, pulse, hand perfusion and sensation at the end.|Restrictions::No blood pressure cuff, needles or tight clothing on that arm; what not to cannulate.|Follow-up owner::Who reviews the fistula, when, and how maturation will be assessed.|Warning signs and contact::Bleeding, cold or weak hand, loss of thrill, fever, with a number.}}
{{call:Stop and get help, or close and defer, when the safe alternative is outside your consent, competence or privileges. An unconsented operation on an anesthetized patient is not rescued by a good result.}}
"""),
    ],
    "debrief": [
        "<p><strong>Within the consent.</strong> The consent allows a forearm fistula higher up if the vessels there are suitable, or abandoning the operation. If a mid-forearm cephalic vein above the thrombosed segment is suitable and you are privileged to do it, that is within consent.</p>",
        "<p><strong>The resident&rsquo;s suggestion.</strong> A brachiobasilic transposition was not discussed with Mr. Bautista, carries different risks (a longer incision, nerve injury, more hand ischemia with brachial inflow) and uses an upper-arm site the plan was trying to save. It is not an emergency. Decline it, explain why to the team, and if the forearm option is unsuitable, close and plan a discussion with the patient.</p>",
        "<p><strong>Note and handoff.</strong> Record the thrombosed wrist segment, what was done or abandoned, the immediate result and hand examination, restrictions, the follow-up date and owner, and warning signs with a contact. Send it to the nephrologist and the dialysis unit. If nothing was created, update the Life-Plan and tell the patient yourself.</p>",
    ],
    "skills": {"title": "Fistula planning, judgment and handoff",
               "intro": "Assessed by a qualified surgeon at the learner&rsquo;s authorized supervision level.",
               "items": [("Presents the operative plan, contingency and what is protected for later", False),
                         ("Confirms patient, side, consent and contingency at the time-out", True),
                         ("Recognizes when an alternative exceeds consent, competence or privileges and stops or seeks help", True),
                         ("Assesses the immediate result including hand perfusion and sensation", True),
                         ("Delivers a written handoff to the dialysis team and confirms receipt", False)],
               "placement": "Operating room at the assigned supervision level"},
    "quiz": [
        ("A complete operative handoff should include what?",
         ["Only the operation&rsquo;s name", "Findings, immediate result, restrictions, follow-up owner and warning signs",
          "Only the incision length", "The anesthetic drugs used"],
         1, "The dialysis pathway needs actionable information after the operation."),
        ("Unexpected anatomy requires an alternative beyond the consent and the learner&rsquo;s competence. What is the best response?",
         ["Seek qualified help or defer, within the clinical circumstances", "Improvise independently",
          "Proceed and document afterward", "Ask the scrub nurse to decide"],
         0, "Consent, competence and privileges constrain a non-emergency change of plan."),
        ("In the Dialysis Access Consortium (DAC) clopidogrel trial, what happened to suitability of fistulas for dialysis?",
         ["It improved markedly", "It did not differ from placebo despite less early thrombosis",
          "It worsened significantly", "It was not measured"],
         1, "Thrombosis fell from 19.5% to 12.2%, but failure to attain suitability was 61.8% versus 59.5%."),
        ("What did the Hemodialysis Fistula Maturation (HFM) study report as the median time from creation to maturation?",
         ["About 2 weeks", "About 6 weeks", "About 115 days", "About 2 years"],
         2, "Median 115 days, with wide variation by whether the patient was already on dialysis."),
        ("Which mechanism narrows a new fistula from inside?",
         ["Outward remodeling", "Neointimal hyperplasia", "Shear-stress-induced dilation", "Arterial enlargement"],
         1, "Neointimal hyperplasia, often at the swing segment, competes with outward remodeling."),
    ],
    "terms": [("Brachiobasilic transposition", "A fistula from the brachial artery to the basilic vein, which is moved to a superficial course."),
              ("Juxta-anastomotic", "Next to the anastomosis.")],
    "readings": [("hemodialysis-access-lifeline.html", "Fistula creation and maturation, in plain words."),
                 ("dialysis-access-care.html", "Care of a new fistula.")],
    "calcs": ["calc-av-fistula-maturation.html", "calc-av-access-outcome-audit.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
