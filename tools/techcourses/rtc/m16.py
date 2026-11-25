# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 16: Symptoms, Graft Dysfunction, and Urgent Escalation. Written for this series from published sources."""

MODULE = {
    "image_alt": "A coordinator answering a phone call at a transplant clinic desk while writing on a structured urgent-call log.",
    "objectives": [
        "Explain, in plain words, why delay matters after transplant: rejection, infection, and missed medicines.",
        "Recognize the symptoms and situations that need same-day or emergency clinical review, for recipients and donors.",
        "Route an urgent call within scope, using the program&rsquo;s protocol, and never give clinical advice outside it.",
        "Close the loop: confirm receipt, action, and the patient&rsquo;s understanding, then document.",
    ],
    "big": """
{{plain:After a transplant, the new kidney is like a newly planted tree in dry season. Most days it grows quietly. But when something threatens it &mdash; a pest, a missed watering, a storm &mdash; the signs are small at first, and by the time the leaves wilt, the damage is harder to undo. The gardener who acts on small signs saves the most trees.}}
{{fig:rtc16_routing}}
<p>The picture has a limit. A tree does not fight back against itself. A transplanted kidney faces three kinds of threat at once: the recipient&rsquo;s immune system (rejection), infections made more likely by the medicines that prevent rejection, and gaps in those medicines. All three can start quietly. Fever, less urine, swelling, pain over the kidney, vomiting that stops tablets from staying down, diarrhea that changes drug levels, or a rising creatinine on a routine test can each be the first sign.</p>
<p>KDIGO&rsquo;s recipient guideline frames post-transplant care around early detection: frequent monitoring of kidney function early on, and prompt evaluation of a rise.[[rtc_kdigo2009]] Your job is to make sure the right clinician hears about a warning sign quickly, and that the loop closes. Clinical coordinators may take a structured history under protocol; support staff route at once. Nobody in this role diagnoses or advises outside protocol.</p>
{{cards:Key terms for this module|Rejection::The immune system attacking the transplanted kidney; often silent at first and treatable when found early.|Graft dysfunction::The kidney working less well, from any cause.|Creatinine::A blood test the team uses to follow kidney function.|Urgent-call protocol::The program&rsquo;s written list of symptoms and where each is routed: emergency now, transplant team today, or routine.|Closed loop::Receipt, action, and the patient&rsquo;s understanding confirmed and documented.}}
""",
    "case": {"title": "Three calls before noon", "html": """
<p>It is Tuesday morning at the transplant clinic.</p>
<p>9:05 a.m. Mrs. Corazon Lopez, 50, two weeks after transplant, calls: since last night she has had a fever of 38.4 &deg;C and is passing less urine than usual.</p>
<p>9:40 a.m. Mr. Rodel Aquino, 35, eight months after transplant, texts: he has been vomiting since early morning and could not keep his tablets down. He asks whether he should &ldquo;just take them tomorrow.&rdquo;</p>
<p>11:15 a.m. Mr. Ben Garcia, Mrs. Lopez&rsquo;s brother and her donor, one week after nephrectomy, calls separately: his abdominal pain has been getting worse for two days and he feels feverish.</p>
""", "questions": ["Where does each call go, and how fast?",
                  "What do you say to Mr. Aquino about tomorrow&rsquo;s tablets?",
                  "Whose team handles Mr. Garcia, and what must you avoid?"]},
    "sections": [
        ("why", "Know why delay matters", "Three threats that start quietly", """
<div class="table-wrap"><table>
<thead><tr><th>Threat</th><th>What happens</th><th>What you may hear</th></tr></thead>
<tbody>
<tr><td>Rejection</td><td>The immune system attacks the kidney; often found first as a rise in creatinine</td><td>Usually nothing; sometimes less urine, swelling, tenderness over the kidney, fever</td></tr>
<tr><td>Infection</td><td>Immunosuppression lowers defenses; infections can progress fast</td><td>Fever, chills, cough, painful urination, diarrhea</td></tr>
<tr><td>Missed or low medicines</td><td>Vomiting, diarrhea, running out, or skipping lowers drug levels, which can trigger rejection</td><td>&ldquo;I couldn&rsquo;t keep my tablets down,&rdquo; &ldquo;I ran out,&rdquo; &ldquo;I stopped one&rdquo;</td></tr>
<tr><td>Surgical problems</td><td>Leaks, bleeding, blocked flow, especially early</td><td>Pain, swelling at the wound, much less urine</td></tr>
</tbody></table></div>
<p>Nonadherence is associated with a large share of graft losses (Module 15),[[rtc_butler2004]] and rejection treated early generally has a better chance of recovery than rejection found late. That is the whole case for urgency: the earlier the team knows, the more options it has.</p>
{{key:After transplant, a small sign can be the first sign. Route it the same day; let the team decide what it means.}}
"""),
        ("contact", "Use a disciplined contact", "Protocol, not advice", """
<p>Every program needs a written urgent-call protocol that lists symptoms and their routes, and every coordinator keeps it by the phone. A simple structure:</p>
<div class="table-wrap"><table>
<thead><tr><th>Route</th><th>Examples (the program&rsquo;s protocol is the authority)</th></tr></thead>
<tbody>
<tr><td>Emergency now</td><td>Difficulty breathing, chest pain, confusion, fainting, severe bleeding, no urine</td></tr>
<tr><td>Transplant clinician today</td><td>Fever, less urine, new pain or swelling over the kidney, vomiting or diarrhea that stops medicines, a missed immunosuppressant, a rising creatinine reported by a laboratory</td></tr>
<tr><td>Routine</td><td>Questions about appointments, paperwork, or stable symptoms the protocol lists as routine</td></tr>
</tbody></table></div>
<p>Take down the caller&rsquo;s name, two identifiers, the symptom in their words, when it started, and a callback number. Clinical coordinators assigned to do so may ask the protocol&rsquo;s structured questions. Support staff route at once to the on-call clinician and do not ask clinical questions beyond the protocol&rsquo;s first screen.</p>
<p>Never tell a caller to take, skip, delay, or double a medicine, or to &ldquo;wait and see,&rdquo; unless that exact advice is in the protocol you are authorized to use. &ldquo;Just take them tomorrow&rdquo; can be the wrong answer, and only a clinician can give the right one.</p>
{{key:Route by protocol, take a callback number, and never give medicine advice outside protocol.}}
"""),
        ("donor", "Donors call too", "The donor has their own team", """
<p>Donors can develop complications after nephrectomy: wound infection, bleeding, bowel problems, or chest infection, mostly in the first weeks.[[rtc_lentine2016]] A donor&rsquo;s urgent call goes to the donor&rsquo;s surgical or donor team, not to the recipient&rsquo;s team, and the donor&rsquo;s information stays in the donor&rsquo;s record. If donor and recipient call about the same day&rsquo;s worries, treat them as two calls, two logs, two routes.</p>
{{scene:Two calls from one house|<p>A recipient and her donor husband call within ten minutes of each other, both feverish. Coordinator Mr. Jun Santos opens two urgent-call log entries, routes the recipient to the transplant clinician and the donor to the donor surgical team, and calls each back separately with their own plan.</p>
<p>The recipient is admitted for review; the donor is seen the same afternoon in the surgical clinic.</p>
<p class="tc-scene-take">Living in one house did not make them one patient.</p>}}
{{key:Donor calls go to the donor&rsquo;s team. Two people, two logs, two routes.}}
"""),
        ("close", "Close the loop", "From call to confirmed plan", """
<p>An urgent call is closed only when four things have happened and been written down:</p>
{{flow:A closed urgent call|Received::The clinician confirms they have the message, with the time.|Acted::The clinician gives a plan: come in now, go to emergency, a test, a medicine instruction.|Understood::The patient repeats the plan back to you or the clinician.|Documented::The log shows times, who decided, the plan, and the follow-up check.}}
<p>A text, a voicemail, or a message in a group chat is dispatch, not closure. If the clinician does not respond within the protocol&rsquo;s time, escalate to the backup on the list. Check later that the patient actually arrived or did what was planned.</p>
<p>Trends matter too. The site&rsquo;s <a href="calc-allograft-egfr-trend.html">allograft eGFR trend tool</a> is a clinician tool for following kidney function over time; coordinators make sure routine results reach the team and that an abnormal result triggers a call, not a filing.</p>
{{key:Received, acted, understood, documented. Anything less is an open urgent call.}}
"""),
    ],
    "debrief": ["""
<p><strong>Mrs. Lopez (9:05).</strong> Fever and less urine two weeks after transplant: transplant clinician today, now, under protocol. Take her details and a callback number, route at once, and confirm the plan with her. If she has any emergency sign, emergency route.</p>
<p><strong>Mr. Aquino (9:40).</strong> Vomiting with missed immunosuppressants: transplant clinician the same day. Tell him you are getting a doctor&rsquo;s instruction now, and do not tell him to take them tomorrow, double up, or skip. Close the loop when he has the clinician&rsquo;s instruction and repeats it back.</p>
<p><strong>Mr. Garcia (11:15).</strong> Worsening abdominal pain and fever one week after nephrectomy: the donor surgical team, urgently, under protocol. Open a separate log in his record. Do not route him through his sister&rsquo;s team and do not share his call with her.</p>
"""],
    "skills": {"title": "Urgent-call routing",
               "intro": "Take three simulated urgent calls, including one from a donor, while your preceptor observes.",
               "items": [
                   ("Records name, two identifiers, symptom in the caller&rsquo;s words, onset, and callback number.", False),
                   ("Routes each call by the protocol to emergency, same-day clinician, or routine.", True),
                   ("Gives no medicine advice outside the protocol, including to a caller who asks to delay doses.", True),
                   ("Routes a donor&rsquo;s call to the donor&rsquo;s team in a separate log.", True),
                   ("Closes each loop: received, acted, understood, documented.", True),
                   ("Escalates to the backup when a clinician does not respond in time.", False),
               ],
               "placement": "Review your program&rsquo;s urgent-call protocol. Audit five recent urgent calls for each of the four closure steps."},
    "terms": [("Rejection", "Immune attack on the transplanted kidney."), ("Graft dysfunction", "The kidney working less well."),
              ("Creatinine", "A blood test for kidney function."), ("Urgent-call protocol", "The written routing list for symptoms."),
              ("Closed loop", "Received, acted, understood, documented.")],
    "readings": [("transplant-allograft-failure.html", "When a transplanted kidney is failing: what patients and clinicians face."),
                 ("viral-infections-vaccinations-ckd.html", "Infections and vaccinations in kidney disease.")],
    "calcs": ["calc-allograft-egfr-trend.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["16"])
