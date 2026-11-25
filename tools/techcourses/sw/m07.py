# -*- coding: utf-8 -*-
"""Renal Social Worker, Module 07: PhilHealth Navigation and Financial Protection. Written for this series from published sources."""

MODULE = {
    "image_alt": "A social worker explaining a printed benefit summary to a patient and her daughter at a hospital help desk.",
    "objectives": [
        "Read a PhilHealth rule by its circular number, version, effective date, and the date of the person&rsquo;s case before explaining it.",
        "Explain the hemodialysis benefit (up to 156 sessions a year; no copayment for package-covered services) without promising that all care is free.",
        "Describe the peritoneal dialysis and kidney transplant Z Benefits at the level the reviewed sources support, and say what you could not verify.",
        "Plan ahead for the month the hemodialysis sessions run out, using the session balance tool.",
        "Keep navigation separate from claims decisions: explain, prepare, and route; never adjudicate or guarantee.",
    ],
    "big": """
{{plain:A PhilHealth benefit is like a bus pass. It takes you a long way, but only on certain routes, only until a certain date, and only for a certain number of rides. People get stranded not because the pass is worthless, but because nobody told them which rides it covers, or that the rides run out in October.}}
{{fig:sw07_philhealth}}
<p>The picture has a limit. A bus pass rarely changes its rules mid-year. PhilHealth circulars are revised, replaced, and sometimes published weeks before they take effect, with transition rules for cases that started under the old version. The same question (&ldquo;Is my transplant covered?&rdquo;) can have different answers depending on the date of the case. So the habit is not to remember the benefit; it is to look it up by number and date each time, and to say which version you are using.</p>
<p>Your job is navigation and financial protection: help the person understand what is covered, prepare what they need, plan for what is not covered, and route claims questions to the people who decide them. You do not decide eligibility or pay claims, and you never promise an amount.</p>
{{cards:Key terms for this module|PhilHealth circular (PC)::A numbered PhilHealth issuance that sets or changes a benefit, such as PC 2024-0023.|Benefit package::The defined set of services and the amount PhilHealth pays for them.|Copayment::A charge the patient pays beyond what PhilHealth covers, allowed only where the rule allows it.|Z Benefits::PhilHealth packages for selected high-cost conditions, delivered through contracted facilities.|Contracted provider::A facility under contract with PhilHealth to deliver a Z Benefits package.|Tamang Sagot::PhilHealth&rsquo;s official question-and-answer companion to a circular.}}
""",
    "case": {"title": "&ldquo;The 156 sessions are used up in October&rdquo;", "html": """
<p>Friday, 1:30 p.m. Mrs. Lucila Bernardo, 66, has been on hemodialysis three times a week since January. Her daughter, Ms. Joy Bernardo, comes to your desk with a printout from a social media post that says &ldquo;PhilHealth now covers dialysis 100% free, all year, no limits.&rdquo;</p>
<p>The unit&rsquo;s billing clerk has just told her that her mother&rsquo;s PhilHealth sessions will run out before the end of the year and that she will then be charged per session. Ms. Bernardo is angry and frightened. &ldquo;Which one is true? Are you telling me my mother will stop dialysis in November?&rdquo;</p>
<p>Mrs. Bernardo also asks whether she should switch to peritoneal dialysis at home because &ldquo;that one is free forever,&rdquo; and whether the new transplant rule she heard about this week means she can get a transplant now.</p>
""", "questions": ["How do you explain the hemodialysis benefit accurately, and what do you check first?",
                  "When will her sessions run out, and what will you plan before then?",
                  "How do you answer her questions about peritoneal dialysis and the new transplant circular?"]},
    "sections": [
        ("reading", "Read the rule by number and date", "Four checks before you explain", """
<p>Before you explain any benefit, do four checks. Which circular governs this benefit now? Which version is it, and when did it take effect? What date does this person&rsquo;s case start: the first session, the admission, the operation? Do any transition rules apply to cases that started under an older version?</p>
{{fig:sw07b_four_checks}}
<div class="table-wrap"><table>
<thead><tr><th>Check</th><th>Where to look</th><th>Why it matters</th></tr></thead>
<tbody>
<tr><td>Current circular and version</td><td>PhilHealth&rsquo;s circular index for the current and previous year</td><td>Older circulars may be amended or replaced</td></tr>
<tr><td>Effective date</td><td>The effectivity clause, usually near the end</td><td>Publication is not the same as effectivity</td></tr>
<tr><td>Case date</td><td>The record: first session, admission, operation</td><td>Decides which version applies</td></tr>
<tr><td>Transition rules</td><td>The transitory clause</td><td>Cases begun under an older rule may continue under it</td></tr>
<tr><td>Official explanation</td><td>Tamang Sagot or the official news explainer</td><td>Plain-language answers from PhilHealth itself</td></tr>
</tbody></table></div>
<p>Social media posts, other patients&rsquo; stories, and old printouts are where the confusion starts. Respect the question behind them, then show the person the official source.</p>
{{key:Name the circular, its version, and its effective date every time you explain a benefit. Check the case date against it.}}
"""),
        ("hd", "The hemodialysis benefit", "156 sessions, and what &ldquo;no copayment&rdquo; means", """
<p>Under PhilHealth Circular 2024-0023, as explained in PhilHealth&rsquo;s official Tamang Sagot, the hemodialysis benefit covers up to 156 sessions a year at PHP 6,350 per session, with no copayment for package-covered services in both public and private facilities.[[sw_phic2024hd]][[sw_phic2024ts]] The official explanation also describes a capped professional-fee copayment of up to PHP 450 for specified additional services, documented in the package agreement.[[sw_phic2024ts]] That is not a routine surcharge on every session. The circular PDF itself is a scanned document; check the exact tables visually before you quote operational details.</p>
<p>So the social media post is wrong in one way, and the clerk may be right in another. &ldquo;No copayment for package services&rdquo; is true. &ldquo;Free, all year, no limits&rdquo; is not: the benefit is limited to 156 sessions a year, and services outside the package may cost money. A person on three sessions a week uses 156 sessions in exactly 52 weeks, so a full year is covered only if no extra sessions are needed. Extra sessions after an admission, or a fourth weekly session, use the balance faster.</p>
<p>PhilHealth also sets quality standards for maintenance hemodialysis that facilities follow;[[sw_phic2024q]] these are not social work rules, but they explain some of the documents the unit asks patients for.</p>
{{formula:<strong>Worked example, illustrative.</strong> Sessions left = annual sessions &minus; sessions used. Weeks left = sessions left &divide; sessions per week.<br>Annual sessions: 156. Used by September 30: 120 (extra sessions after a September admission). Schedule: 3 a week.<br>Sessions left = 156 &minus; 120 = 36. Weeks left = 36 &divide; 3 = 12. Twelve weeks after September 30 is about December 23.<br>What the number tells you: the family has about 12 weeks to plan the last week of the year. What it does not tell you: how the current rule counts the year, or what the unit will charge after; confirm both with the claims officer.}}
<p>The toolkit&rsquo;s <a href="calc-social-worker-toolkit.html#tool-3">session balance tool</a> does this arithmetic for any schedule and date.</p>
{{key:&ldquo;No copayment for package services&rdquo; is true; &ldquo;free with no limit&rdquo; is not. Plan for the session limit months ahead.}}
"""),
        ("pd_kt", "Peritoneal dialysis and transplant", "Say what is verified, and what is not", """
<p>For peritoneal dialysis, PhilHealth Circular 2024-0036 sets Z Benefits packages. PhilHealth&rsquo;s official explainer describes separate adult and pediatric packages, delivery through contracted providers, registration in the PhilHealth dialysis database, and limits on charges for essential services.[[sw_phic2024pd]][[sw_phic2025pdnews]] The full circular could not be retrieved for this course, so no package amount or eligibility rule is quoted here. Check the current circular and its annexes, and ask the contracted provider, before you discuss amounts.</p>
<p>For kidney transplantation, PhilHealth Circular 2026-0019 (Revision 1) amends the earlier transplant Z Benefits circular, PC 2024-0035. It was published on November 21, 2026, and its effectivity clause says it takes effect 15 days after publication; it also has transition provisions for cases under the older circular.[[sw_phic2026kt]] On the date this course was written it was published but not yet effective. Do not tell a family that a new rule &ldquo;already applies&rdquo; to them; ask the contracted transplant facility which version governs their case date.</p>
<div class="table-wrap"><table>
<thead><tr><th>Question you hear</th><th>Honest answer</th></tr></thead>
<tbody>
<tr><td>&ldquo;Is peritoneal dialysis free forever?&rdquo;</td><td>&ldquo;There is a PhilHealth package for it through contracted providers. I will check the current rules and what a provider near you charges.&rdquo;</td></tr>
<tr><td>&ldquo;Does the new transplant rule mean I can get a transplant now?&rdquo;</td><td>&ldquo;The rule changes how a transplant is paid for. Whether a transplant is right and possible for you is a medical decision, and the payment rules depend on dates. Let us ask the transplant team.&rdquo;</td></tr>
<tr><td>&ldquo;How much will PhilHealth pay?&rdquo;</td><td>&ldquo;Let me show you the circular and the facility&rsquo;s written estimate. I cannot promise an amount.&rdquo;</td></tr>
</tbody></table></div>
<p>A choice of dialysis type should never be made because of a rumor about cost. It is a clinical and personal decision (Module 14). Your part is to make sure the cost picture is accurate.</p>
{{key:When you could not verify a rule, say so. Point to the circular and the contracted provider, and never quote an amount you have not seen.}}
"""),
        ("protect", "Financial protection without promises", "Navigate, prepare, route", """
<p>Financial protection is the purpose behind the paperwork. Out-of-pocket costs drive people to skip and stop kidney treatment: a review of 14 studies from high-income and low- and middle-income countries found that cost consistently worsened adherence to dialysis and medicines, with poorer households worst affected.[[sw_dodd2018]] A Philippine cost-of-illness study estimated that, beyond medical costs, patients on maintenance dialysis carried PHP 37,920 to 246,480 a year in non-medical and indirect costs such as transport and lost income, against PHP 3,160 for transplant recipients; the estimates came mostly from urban and semi-urban facilities.[[sw_villanueva2025]]</p>
{{flow:Navigation without adjudication|Explain::The current rule, by number and date, in plain words, with what it does not cover.|Prepare::The documents and steps the person needs, using the facility&rsquo;s current checklist.|Plan::The month the benefit runs out; the costs outside the package; the assistance to apply for (Module 8).|Route::Claims questions to the claims officer; eligibility decisions to PhilHealth.|Record::What you explained, which version, and the date, so the next worker does not contradict you.}}
<p>Never promise approval, an amount, or a date. A promise that fails costs the person money they did not set aside and trust they will not give you again. You can promise something else: that you will check, explain honestly, and stay with them through the answer.</p>
{{key:Explain, prepare, plan, route, and record. Never promise an approval or an amount.}}
{{scene:The version note|<p>Social worker Ms. Carmela Torres writes one line in every benefit note: &ldquo;Explained per PC 2024-0023 and its Tamang Sagot, checked November 25, 2026.&rdquo;</p>
<p>When a later circular changes a detail, her colleagues can see exactly which advice was given under which rule, and correct it without blaming anyone.</p>
<p class="tc-scene-take">Dating your explanation is what makes it correctable.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>Explaining the benefit.</strong> First check the current circular and its official explanation. Then: &ldquo;The post is partly right. PhilHealth covers up to 156 hemodialysis sessions a year, and for the services in the package there is no copayment. But there is a limit of 156, and some services outside the package can cost money. Let me show you the official explanation.&rdquo;[[sw_phic2024ts]] Do not contradict the clerk in front of the family; check with the claims officer and give one consistent answer.</p>
<p><strong>When the sessions run out.</strong> Count with the session balance tool: sessions used so far, schedule, today&rsquo;s date. If they run out in the last weeks of the year, plan now: assistance applications (Module 8), the unit&rsquo;s charges after the limit, and a review of any extra sessions she needed. She must not stop dialysis because of money; that is a clinical danger, and the nephrologist and claims officer must be part of the plan.</p>
<p><strong>Peritoneal dialysis and the new transplant circular.</strong> Peritoneal dialysis has its own Z Benefits through contracted providers; whether it suits her is a clinical and household decision, not a cost rumor (Module 14). The transplant circular published November 21, 2026 was not yet in effect on the research date, and it changes payment, not medical eligibility. Offer a referral to the transplant team if she wants to explore transplant.</p>
"""],
    "skills": {"title": "Explaining a benefit by version and date",
               "intro": "Explain a PhilHealth benefit to a simulated family and plan for the session limit while your supervisor observes.",
               "items": [
                   ("Names the governing circular, version, effective date, and the case date before explaining.", True),
                   ("Explains the 156-session limit and &ldquo;no copayment for package services&rdquo; accurately, without saying all care is free.", False),
                   ("Calculates the session balance and run-out date with the toolkit and starts planning weeks ahead.", False),
                   ("States what could not be verified (for example, peritoneal dialysis amounts) and where to confirm it.", False),
                   ("Declines to promise an approval, amount, or date.", True),
                   ("Routes a claims question to the claims officer and records which version was explained.", False),
               ],
               "placement": "Sit with the unit&rsquo;s claims officer for two hours. List the five benefit questions patients ask most, and the source that answers each."},
    "terms": [("PhilHealth circular", "A numbered PhilHealth issuance that sets or changes a benefit."),
              ("Benefit package", "The defined services and the amount PhilHealth pays for them."),
              ("Copayment", "A charge beyond PhilHealth&rsquo;s payment, allowed only where the rule allows it."),
              ("Z Benefits", "PhilHealth packages for selected high-cost conditions, through contracted facilities."),
              ("Effective date", "The date a rule starts to apply, which can be after publication."),
              ("Transition provision", "A rule for cases begun under an older version.")],
    "readings": [("philhealth-z-packages.html", "The patient guide to PhilHealth hemodialysis, peritoneal dialysis, and transplant benefits."),
                 ("zero-balance-billing-philhealth.html", "The patient guide to zero balance billing.")],
    "calcs": ["calc-social-worker-toolkit.html#tool-3", "calc-social-worker-toolkit.html#tool-1"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("sw_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["07"])
