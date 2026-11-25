# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 10: Recognize a failing access. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A surgeon at a dialysis chair raises the patient&rsquo;s arm to watch whether a fistula collapses, while a nurse reads out the session pressures.",
    "objectives": [
        "Connect the clinical signs of access dysfunction to the location of a stenosis, using flow and pressure physiology.",
        "Distinguish clinical monitoring from instrument-based surveillance, and state what trials of preemptive treatment showed.",
        "Explain why an anatomic narrowing alone does not establish a treatment indication.",
        "Write a dysfunction referral that states what changed, its effect on dialysis, what was checked, the urgency and the question.",
    ],
    "big": """
{{plain:An access circuit is like a garden hose with a pump at one end. Pinch the hose near the tap and the water downstream dribbles and the hose goes soft. Pinch it near the nozzle and the hose swells and stiffens behind the pinch. Where the hose is pinched changes what you feel.}}
<p>The picture has a limit. A hose does not grow new tissue at the pinch. An access does: neointimal hyperplasia at a stenosis keeps progressing, so a lesion that causes nothing today may clot the access in three months, or may stay stable for years. Signs tell you where a lesion is and whether it is affecting dialysis. They do not tell you, on their own, whether treating it now prevents a clot.</p>
{{cards:Key terms for this module|Clinical monitoring::Examination and dialysis findings checked at every session.|Surveillance::Periodic measurement with instruments, such as access flow by ultrasound dilution or duplex.|Inflow stenosis::A narrowing between the artery and the needle zone.|Outflow stenosis::A narrowing between the needle zone and the heart.|Clinically significant lesion::A stenosis with both anatomic narrowing and a clinical consequence.}}
<p>Most access problems announce themselves at the chair if someone is looking. Your work is to read those signs, investigate the patient&rsquo;s problem rather than a number, and decide with the team whether a lesion needs treatment.</p>
""",
    "case": {"title": "The narrowing on the report", "html": """
<p>Mr. Felix Mendoza, 58, has had a left brachiocephalic fistula for three years. Dialysis is uneventful: blood flow 350 mL/min, no prolonged bleeding, Kt/V stable. A duplex done for &ldquo;routine surveillance&rdquo; at an outside clinic reports a 55% narrowing of the cephalic arch. His nephrologist forwards it: &ldquo;Please schedule preventive angioplasty.&rdquo;</p>
<p>At the same unit, Mrs. Rosario Bernardo, 66, with a left forearm fistula, has had needle-site bleeding lasting 25 minutes after each of her last four sessions, and her arm swells by evening. The nurse&rsquo;s note says only &ldquo;bad access.&rdquo;</p>
""", "questions": [
        "Should Mr. Mendoza have angioplasty?",
        "What do Mrs. Bernardo&rsquo;s signs suggest, and what should the referral say?",
        "How would you set up monitoring in this unit?"]},
    "sections": [
        ("physiology", "Reading the signs", "Where the stenosis is, from what you see", """
<p>Flow through an access depends on the pressure difference between artery and veins and on the resistance of the narrowest segment. An outflow stenosis traps arterial pressure upstream: the access becomes pulsatile and firm, venous pressures rise during dialysis, needle sites bleed longer, and the arm may swell. An inflow stenosis starves the access: it feels soft and flat, collapses when the arm is raised, and the blood pump draws more negative arterial pressure. Recirculation, when cleaned blood re-enters the arterial needle, lowers delivered dialysis and can appear as falling Kt/V.</p>
{{fig:vs10_a}}
<div class="table-wrap"><table>
<thead><tr><th>Sign</th><th>Likely location</th><th>Why</th></tr></thead>
<tbody>
<tr><td>Pulsatile, firm access; does not collapse on arm elevation</td><td>Outflow</td><td>Arterial pressure trapped upstream of the lesion</td></tr>
<tr><td>Prolonged needle-site bleeding</td><td>Outflow</td><td>High pressure inside the access at the puncture</td></tr>
<tr><td>Arm, breast or face swelling</td><td>Central outflow</td><td>Venous hypertension beyond the arm veins</td></tr>
<tr><td>Weak, flat access; collapses on elevation; poor flow</td><td>Inflow</td><td>Too little flow reaching the needle zone</td></tr>
<tr><td>Falling Kt/V with recirculation</td><td>Either</td><td>Delivered dialysis lower than prescribed</td></tr>
</tbody></table></div>
<p>Kt/V and access flow are surrogates. What matters is whether the patient gets reliable dialysis and keeps the access. But the surrogate that changes from the patient&rsquo;s own baseline is the most useful early warning.</p>
{{key:Compare the access with its own baseline. A change matters more than any single value.}}
"""),
        ("evidence", "Monitoring or surveillance", "Does finding stenosis early help? What the trials show", """
<p>If stenosis causes thrombosis, it seems obvious that finding and treating it early would save accesses. The trials are less clear. Ravani and colleagues pooled 14 randomized trials with 1,390 participants comparing preemptive correction of stenosis in functioning accesses with treatment only when dysfunction appeared. Preemptive correction did not significantly reduce access loss (risk ratio 0.81, 95% confidence interval 0.65 to 1.02). It did reduce thrombosis (risk ratio 0.79), with larger effects in fistulas than in grafts. The trials were small, and results for mortality, infection and hospitalization were imprecise.[[vs_ravani2016]]</p>
{{fig:vs10_b}}
<p>So a lesion found by surveillance in a well-functioning access is not, by itself, a reason to treat. KDOQI 2019 links intervention to stenosis that is both anatomically and clinically significant, and does not support routine instrument-based surveillance added to clinical monitoring.[[vs_kdoqi]] The UK Kidney Association (UKKA) 2025 guideline recommends intervention for radiologically significant stenosis with clinical features of access dysfunction (statement 4.2, grade 1B).[[vs_ukka]]</p>
{{flow:From signal to decision|Clinical signal::A change in examination, pressures, bleeding, flow or symptoms.|Competing causes::Needle position, hypotension, catheter use, prescription change.|Targeted imaging::Duplex or angiography to locate and grade the lesion.|Significance::Anatomic narrowing plus a clinical consequence.|Decision::Treat, watch with a defined trigger, or treat the competing cause.}}
{{call:Do not route emergencies into an imaging queue. Loss of thrill, a cold or weak hand, bleeding, or fever goes to the urgent pathway the same day.}}
"""),
        ("referral", "The referral", "A referral that can be acted on", """
<p>A useful referral answers five things: what changed and since when; how it affects dialysis or the patient; what has already been checked; how urgent it is; and what decision is being asked. &ldquo;Bad access&rdquo; answers none of them. &ldquo;Needle-site bleeding over 20 minutes after the last four sessions, venous pressure up from 140 to 210 mm Hg at the same blood flow, evening arm swelling; needle placement reviewed; no fever; please assess for outflow stenosis this week&rdquo; answers all of them.</p>
<p>Help the unit build this habit. Agree on what nurses record each session (access examination, arm elevation, pressures at a standard flow, bleeding time, cannulation problems), and on which changes trigger a call.</p>
{{scene:Unit quality meeting, fictional|<p>The head nurse shows you that half of last quarter&rsquo;s access referrals said only &ldquo;poor access.&rdquo; You agree on a one-line template: change, impact, checked, urgency, question. Next quarter, triage time falls and two outflow stenoses are treated before the accesses clot.</p><p class="tc-scene-take"><b>What this shows.</b> Better referrals are a system change, not a lecture to one nurse.</p>}}
{{key:Treat the patient&rsquo;s problem, not the scan&rsquo;s finding.}}
"""),
    ],
    "debrief": [
        "<p><strong>Mr. Mendoza.</strong> He has no clinical dysfunction: stable flow, no bleeding, stable Kt/V. A 55% cephalic arch narrowing found on surveillance is anatomically present but not clinically significant. The pooled trials did not show that preemptive correction saves accesses, and angioplasty has its own risks, including accelerating restenosis. Explain this to the nephrologist, agree on clinical triggers for re-referral, and document the decision.</p>",
        "<p><strong>Mrs. Bernardo.</strong> Prolonged bleeding and evening arm swelling point to outflow stenosis, possibly central. Ask the unit for venous pressures at a standard flow, whether the access collapses on arm elevation, and her catheter history. Arrange imaging this week and treat a lesion that explains her symptoms. Help the unit rewrite &ldquo;bad access&rdquo; into a referral with change, impact, checks, urgency and question.</p>",
        "<p><strong>Monitoring.</strong> Agree on a simple per-session record and a list of triggers for calling, and review referrals at the unit&rsquo;s quality meeting.</p>",
    ],
    "skills": {"title": "Linking clinical signs to a diagnostic question",
               "intro": "At the dialysis chair or with recorded session data, supervised.",
               "items": [("Obtains trends against the patient&rsquo;s own baseline", False),
                         ("Performs the arm-elevation and pulse examination and interprets it", False),
                         ("Considers competing causes before attributing a change to stenosis", False),
                         ("States a specific diagnostic question and urgency", True),
                         ("Does not recommend treatment of a scan finding without clinical relevance", True)],
               "placement": "Dialysis unit"},
    "quiz": [
        ("A stenosis is seen incidentally in an access with stable clinical function. What is the best interpretation?",
         ["Every narrowing requires intervention", "Assess clinical significance before deciding on treatment",
          "Imaging is never useful", "The access will clot within a week"],
         1, "An anatomic finding alone does not establish an indication."),
        ("Which is the most useful dysfunction referral?",
         ["Bad access", "Please scan sometime", "A change from baseline linked to dialysis impact, checks done, urgency and the question",
          "Access issue, kindly see"],
         2, "A defined clinical question helps select and prioritize investigation."),
        ("An access is pulsatile, does not collapse when the arm is raised, and needle sites bleed for a long time. Where is the stenosis most likely?",
         ["Inflow", "Outflow", "At the arterial needle only", "There is no stenosis"],
         1, "Outflow obstruction traps arterial pressure upstream."),
        ("In the meta-analysis of 14 trials, what did preemptive correction of stenosis do?",
         ["Clearly reduced access loss", "Reduced thrombosis but did not significantly reduce access loss",
          "Increased mortality", "Had no effect on anything"],
         1, "Access loss risk ratio 0.81 (confidence interval crossed 1); thrombosis risk ratio 0.79."),
        ("UKKA 2025 statement 4.2 recommends intervention for which lesions?",
         ["Any stenosis over 30%", "Radiologically significant stenosis with clinical features of dysfunction",
          "Only lesions found on surveillance", "Only central lesions"],
         1, "Grade 1B; both anatomic and clinical significance are required."),
    ],
    "terms": [("Recirculation", "Cleaned blood re-entering the arterial needle, lowering delivered dialysis."),
              ("Venous pressure", "Pressure measured by the machine in the return line; rises with outflow stenosis.")],
    "readings": [("dialysis-access-care.html", "What nurses and patients check at each session."),
                 ("avf-aneurysm-and-changes.html", "Changes in a fistula that matter.")],
    "calcs": ["calc-access-intervention-burden.html", "calc-access-flow-cardiac.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
