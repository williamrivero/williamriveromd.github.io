# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 2: The lifetime access plan. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A surgeon, a nephrologist and an older Filipino patient with her daughter sit around a clinic table looking at a simple drawing of an arm.",
    "objectives": [
        "Explain why the access decision belongs inside the patient&rsquo;s whole kidney replacement plan, using the Kidney Disease Outcomes Quality Initiative (KDOQI) end-stage kidney disease (ESKD) Life-Plan.",
        "Compare a fistula, a graft and a catheter for one patient in terms of time to use, procedures, infection and survival, with the strength of each comparison.",
        "Interpret the observational access-mortality data without overstating causation.",
        "Document a present access, a contingency and a successor, chosen with the patient and confirmed by teach-back.",
    ],
    "big": """
{{plain:A good access plan is like planning a long road trip with a spare tire, a second route, and a sense of where you will stop for the night. The first car you take matters, but what ruins trips is having no plan for the flat tire and no idea which roads are still open.}}
<p>The picture has a limit. A road does not change because you drove on it. Veins do. Every catheter, every failed fistula and every venipuncture changes which routes remain. The first access decision spends some of the patient&rsquo;s vascular future, so it has to be made with the whole journey in view.</p>
{{cards:Key terms for this module|ESKD Life-Plan::The Kidney Disease Outcomes Quality Initiative (KDOQI) framework that links access choices to the patient&rsquo;s expected course of kidney replacement therapy.|Present access::The access that will carry dialysis now or next.|Contingency::What happens if the present access fails or does not mature.|Succession::Which site or modality comes after the present access is exhausted.|Teach-back::The patient explains the plan in their own words, so you can see what they understood.}}
<p>For most patients with a long expected course of hemodialysis and usable vessels, a fistula is the right first choice. For some, it is not. Your work is to find out which patient is in front of you, and to write down what happens after the first plan, not only the first plan.</p>
""",
    "case": {"title": "The referral says &ldquo;fistula, please&rdquo;", "html": """
<p>Mrs. Corazon Villanueva, 82, has chronic kidney disease (CKD) with an estimated glomerular filtration rate (eGFR) of 11 mL/min/1.73 m&sup2;. She has heart failure, walks with a cane, and was admitted twice this year. She lives in Bulacan with her daughter, Ms. Annabelle Villanueva, who works weekdays in Manila. Her nephrologist&rsquo;s referral says only: &ldquo;For AV fistula creation.&rdquo;</p>
<p>In your clinic, Mrs. Villanueva says she is tired of hospitals. Her daughter asks how many operations a fistula needs and whether her mother will have to come back many times. Her forearm cephalic vein looks small; the upper-arm vein looks better.</p>
""", "questions": [
        "What do you need to learn from Mrs. Villanueva and her nephrologist before choosing any access?",
        "How would you explain the realistic path of a fistula, a graft, and a catheter for her?",
        "What should the written plan contain beyond the name of an operation?"]},
    "sections": [
        ("lifeplan", "The Life-Plan", "From &ldquo;fistula first&rdquo; to the right access at the right time", """
<p>For two decades the slogan was &ldquo;fistula first, catheter last.&rdquo; It rested on a real observation: patients dialyzing through catheters died more often and had more infections. The KDOQI 2019 update kept the preference for autogenous access where it suits the patient, but replaced the slogan with the end-stage kidney disease (ESKD) Life-Plan: the right access, in the right patient, at the right time, for the right reasons, with a contingency and a successor planned in advance.[[vs_kdoqi]]</p>
{{fig:vs02_a}}
<p>The UK Kidney Association (UKKA) 2025 guideline says the same in graded form. It recommends treating access choice as a patient decision supported by the multidisciplinary team (statement 1.2, grade 1C), and advising fistula formation for patients with suitable anatomy and a likelihood of prolonged hemodialysis (1.3, grade 1B).[[vs_ukka]] Timing matters too. A recent review suggests referral for access when the eGFR falls progressively to 15 to 20 mL/min, or when peritoneal dialysis, a transplant or the current access is failing.[[vs_lok2024]] UKKA suggests referral when hemodialysis is likely within 12 months (2.1, grade 2C).[[vs_ukka]]</p>
{{flow:Three questions the plan must answer|What works now?::The access that will carry dialysis at the expected start, given anatomy and time.|What if it fails?::The contingency: revision, a graft, a different site, or a bridge, decided before failure.|What comes after?::The successor site or modality, and what must be protected to keep it.}}
{{key:Write the second and third plans before you need them. A contingency invented during a crisis usually costs a catheter and a vein.}}
"""),
        ("evidence", "What the evidence shows", "What the access-type evidence can and cannot tell you", """
<p>Ravani and colleagues pooled 62 cohort studies including 586,337 people. Compared with patients using fistulas, those using catheters had a higher risk of death (risk ratio 1.53), of fatal infection (2.12) and of cardiovascular events (1.38). Grafts sat between the two for death and infection.[[vs_ravani2013]] These are associations. Patients who dialyze through catheters are often sicker, started dialysis unplanned, or have exhausted other sites. Part of the difference is the access; part is the patient. No randomized trial has assigned access type, so the size of the true causal effect is unknown.</p>
{{fig:vs02_b}}
<p>A fistula also has a cost the slogan hid: it often fails to mature. In a meta-analysis of 62 cohorts, 23% of fistulas failed primarily, and one-year primary patency including those failures was 60%.[[vs_aljaishi2014]] For a patient with limited life expectancy, months of catheter dependence while waiting for a fistula that may never be used can outweigh the long-term advantage.</p>
<p>Drew and colleagues modeled this trade-off. For most patient profiles an attempt at a fistula was best for survival and cost, especially in younger men without diabetes. The advantage shrank considerably in older patients, and women with diabetes and older men with diabetes had similar outcomes regardless of access type.[[vs_drew2015]] A decision model is only as good as its inputs, so treat it as a way of thinking, not a rule.</p>
<div class="table-wrap"><table>
<thead><tr><th>Access</th><th>What it offers</th><th>What it costs</th><th>Strength of comparison</th></tr></thead>
<tbody>
<tr><td>Fistula</td><td>Lowest infection and intervention rates once it works</td><td>Months to mature; about one in four fail primarily</td><td>Observational for survival; consistent for infection</td></tr>
<tr><td>Graft</td><td>Usable within weeks; fewer anatomic requirements</td><td>More stenosis, thrombosis and procedures over time</td><td>Observational</td></tr>
<tr><td>Catheter</td><td>Immediate use; no needles</td><td>Highest infection risk; central vein injury that can close future sites</td><td>Observational for survival; strong for infection</td></tr>
</tbody></table></div>
{{key:The observational data justify preferring a working fistula. They do not justify promising any patient that a fistula will work, or that it will help them live longer.}}
"""),
        ("deciding", "Deciding together", "Making the decision with the patient", """
<p>Shared decision-making is not a consent form. It is a conversation that puts the realistic paths side by side and asks which one fits this person&rsquo;s life. Ask what the patient wants to protect: independence, fewer hospital visits, staying at work, avoiding needles, staying well enough for a transplant. Ask about home dialysis and transplantation; a patient planned for peritoneal dialysis may need only a contingency for hemodialysis.</p>
<p>Explain likely extra procedures, travel and costs, and uncertainty. Then check understanding with teach-back: &ldquo;So I know I explained it well, can you tell me what happens if the fistula does not grow?&rdquo; A plan the patient can explain is one the patient can follow.</p>
{{scene:Access clinic, fictional|<p>A 45-year-old jeepney driver with polycystic kidney disease and an eGFR of 18 wants to keep working. His forearm vessels are good. You plan a left radiocephalic fistula now, name a left upper-arm fistula as the contingency, and protect the right arm for the future. You also note that his brother has offered a kidney.</p><p class="tc-scene-take"><b>What this shows.</b> The same plan format serves a patient heading for transplant: the access protects him while he waits, and the plan says so.</p>}}
{{call:Revisit the plan, with the patient and the nephrologist, whenever health, prognosis, or preferences change. An access plan written for last year&rsquo;s patient can be wrong for this year&rsquo;s.}}
"""),
    ],
    "debrief": [
        "<p><strong>What to learn first.</strong> Ask Mrs. Villanueva what matters most to her and what she fears. Ask her nephrologist about her expected trajectory: how soon dialysis is likely, whether conservative kidney management has been discussed, and whether home therapy is possible. Age alone does not settle anything, but her frailty, heart failure and wish to avoid hospitals do change the balance.</p>",
        "<p><strong>Explaining the paths.</strong> A fistula may take three to six months to become usable and may need extra procedures; about one in four never work. A graft can usually be used within weeks but tends to need procedures to keep it open. A catheter works at once but carries the highest infection risk. For her, a forearm fistula with a small vein might not mature in time; an upper-arm fistula or a graft may be more realistic. If she is unlikely to start dialysis soon, or chooses conservative care, the right answer may be no operation yet.</p>",
        "<p><strong>The written plan.</strong> Record her goals, the options discussed, the chosen access and why, the contingency if it fails, which arm and veins to protect, who reviews her and when, and that she and her daughter could explain the plan back. Send a copy to the nephrologist and the dialysis unit.</p>",
    ],
    "skills": {"title": "Building an access Life-Plan",
               "intro": "Use a fictional patient or, with consent and supervision, a real clinic consultation.",
               "items": [("Elicits the patient&rsquo;s goals and what they want to protect", False),
                         ("Confirms the expected kidney replacement trajectory with the nephrologist", False),
                         ("Compares feasible options with realistic time to use and failure rates", True),
                         ("Names a contingency and a successor, and the vessels to protect", True),
                         ("Confirms understanding by teach-back", False),
                         ("Avoids promising that any access type is universally superior", True)],
               "placement": "Access clinic or simulation"},
    "quiz": [
        ("What belongs in an individualized access plan?",
         ["Only the next operation", "The present access, a contingency, future options and the patient&rsquo;s goals",
          "A fixed access type for every patient", "The surgeon&rsquo;s preferred configuration"],
         1, "The KDOQI Life-Plan links the current decision to the patient&rsquo;s whole treatment course."),
        ("A patient worries about repeated travel to the hospital. What is the best response?",
         ["Treat travel as unrelated to the access decision", "Include travel burden when comparing feasible pathways",
          "Decline all surgery", "Promise that a fistula will need no further visits"],
         1, "A workable shared decision weighs burdens without letting one concern replace the full assessment."),
        ("A meta-analysis of cohort studies found higher mortality with catheters than with fistulas. What is the most accurate interpretation?",
         ["Catheters cause a 53% increase in death", "The association is real but partly reflects sicker patients; the causal effect is unknown",
          "Access type has no relationship to outcomes", "Randomized trials have confirmed the effect"],
         1, "The data are observational; confounding by illness and unplanned starts is likely."),
        ("What share of new fistulas failed primarily in the Al-Jaishi meta-analysis?",
         ["About 5%", "About 23%", "About 50%", "About 75%"],
         1, "Primary failure was 23% (95% confidence interval 18% to 28%)."),
        ("UK Kidney Association (UKKA) 2025 statement 1.2 recommends treating access choice as what?",
         ["A surgical decision", "A patient decision supported by the multidisciplinary team",
          "A payer decision", "A decision made after dialysis starts"],
         1, "Statement 1.2 (grade 1C) frames access choice as the patient&rsquo;s decision, with team support and time to consider."),
    ],
    "terms": [("Life-Plan", "KDOQI&rsquo;s framework for planning access around a patient&rsquo;s whole course of kidney replacement therapy."),
              ("Primary failure", "A fistula that never becomes usable or fails before it is used.")],
    "readings": [("hemodialysis-access-lifeline.html", "Planning access as a lifeline that lasts."),
                 ("when-should-dialysis-start.html", "Timing the start of dialysis, which sets the access timeline."),
                 ("hemodialysis-elderly.html", "Hemodialysis decisions in older adults.")],
    "calcs": ["calc-kfre.html", "calc-egfr-ckd-epi.html", "calc-frailty-assessment.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
