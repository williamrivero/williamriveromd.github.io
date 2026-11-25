# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 14: Final Readiness and Perioperative Handoff. Written for this series from published sources."""

MODULE = {
    "image_alt": "A preoperative huddle with surgeon, anesthesiologist, nurse, and coordinator reviewing a readiness board before surgery.",
    "objectives": [
        "Reconcile all four gates for both people into a single readiness view before surgery.",
        "Track holds explicitly, each with an owner, a condition, and the evidence that releases it.",
        "Run or support a readiness huddle that ends in a recorded go, hold, or stop decision by the authorized lead.",
        "Give separate, structured handoffs for the recipient and the donor.",
    ],
    "big": """
{{plain:Readiness for surgery is like the last check before a rocket launch. Each station &mdash; fuel, weather, guidance, crew &mdash; reports &ldquo;go&rdquo; or &ldquo;no go&rdquo; in turn. The launch director does not count votes. One &ldquo;no go&rdquo; holds the launch until that station is fixed.}}
{{fig:rtc14_convergence}}
<p>The picture has a limit. A rocket has one crew. A living-donor transplant has two people on two operating tables, each with their own four stations: medical, legal, ethical, and insurance. That makes eight gates, owned by different people, closing on different days. Readiness is the moment they all converge, and it is also the moment pressure peaks: the operating room is booked, families are waiting, and everyone wants the last item to be a formality.</p>
<p>Recall why this matters. Surgery carries a real early risk for the recipient &mdash; in a large registry study, death risk in the first two weeks after transplant was 2.8 times that of wait-listed patients before falling far below it[[rtc_wolfe1999]] &mdash; and the donor accepts surgical risk with no medical benefit (Module 7). The readiness check is where those risks are accepted deliberately, on current evidence, or not at all.</p>
{{cards:Key terms for this module|Readiness::All gates closed, for both people, by the people who own them, on current evidence.|Hold::A stated condition that must be met before surgery, with an owner and release evidence.|Huddle::A short structured meeting that ends in a go, hold, or stop decision.|Authorized lead::The person the program designates to make the final go or stop decision.|Handoff::The structured transfer of responsibility from one team to another, with read-back.}}
""",
    "case": {"title": "The Monday morning list", "html": """
<p>Mr. Francisco Manalo, 55, is scheduled for a living-donor transplant on Monday at 7:30 a.m. from his son, Mr. Paolo Manalo, 28. It is Friday afternoon.</p>
<p>Your readiness board shows: recipient medical cleared; donor medical cleared; legal packet complete; HTEC approved with one condition, &ldquo;independent interpreter at consent&rdquo; &mdash; done, documented; donor consent signed Wednesday; PhilHealth pre-authorization valid until next March.</p>
<p>One hold remains: &ldquo;Final crossmatch within 7 days of surgery.&rdquo; The last crossmatch was done 9 days before Monday. The laboratory&rsquo;s weekend courier leaves at 5 p.m. today. Also, the son mentioned on Wednesday that he &ldquo;felt a bit feverish&rdquo; and has not been asked about it since.</p>
""", "questions": ["Which gates are closed, and which are open?",
                  "What do you do before 5 p.m.?",
                  "What will the Monday huddle need to see?"]},
    "sections": [
        ("converge", "Readiness is a convergence", "Eight gates, one view", """
<p>Build one readiness view with two columns, one per person, and four rows. Each cell shows the status, the owner, and the evidence.</p>
<div class="table-wrap"><table>
<thead><tr><th>Gate</th><th>Recipient: closed by</th><th>Donor: closed by</th></tr></thead>
<tbody>
<tr><td>Medical</td><td>Transplant team decision on current results; final compatibility results reviewed</td><td>Donor clinicians&rsquo; decision on current results; fit for surgery today</td></tr>
<tr><td>Legal</td><td>Identity confirmed; recipient consent</td><td>Legal packet complete; donor consent by the surgeon with independent witnessing</td></tr>
<tr><td>Ethical</td><td>Not usually a separate gate, unless the team raised one</td><td>HTEC decision with every condition closed; donor confirms continuing wish</td></tr>
<tr><td>Insurance</td><td>Pre-authorization valid on the surgery date; KT registry entry confirmed</td><td>Coverage within the package confirmed; no donation-related charges</td></tr>
</tbody></table></div>
<p>The <a href="calc-transplant-coordinator-toolkit.html#tool-1">four-gate readiness board</a> in the toolkit turns these statuses into a single view that stays &ldquo;not ready&rdquo; until every cell is closed. The tool is a display; the people who own each gate close it.</p>
{{key:Readiness is eight gates closed by their owners on current evidence. One open gate means not ready.}}
"""),
        ("holds", "Track holds explicitly", "Every hold has a release", """
<p>A hold is a condition someone with authority set: &ldquo;repeat crossmatch within 7 days,&rdquo; &ldquo;potassium below a level the team sets on the morning of surgery,&rdquo; &ldquo;dental clearance before listing.&rdquo; Treat each as a register row with four fields: the condition, the owner, the deadline, and the evidence that releases it.</p>
<p>Only the person who set a hold, or their delegate, releases it. A coordinator never releases a hold because the result &ldquo;was fine last time&rdquo; or because the date is close. If a hold cannot be met in time, the decision to postpone, proceed with a different plan, or stop belongs to the team; your job is to make the gap visible early, with an SBAR, while there is still time to fix it.</p>
<p>Watch for new information that should become a hold. A donor who mentions a fever, a recipient who missed two dialysis sessions, a new medicine, a family conflict that surfaces late &mdash; record it and route it to the gate owner the same day.</p>
{{scene:The crossmatch and the courier|<p>On Thursday afternoon coordinator Ms. Belen Cruz sees that a pre-surgery crossmatch will be 8 days old on the surgery date against a 7-day hold. The laboratory&rsquo;s last courier leaves in three hours.</p>
<p>She calls the transplant nephrologist, who orders a repeat; Ms. Cruz arranges collection at the patient&rsquo;s dialysis session that evening and a special courier. The result is reviewed Saturday morning.</p>
<p class="tc-scene-take">The hold was met because the gap was seen while there was still a courier to catch.</p>}}
{{key:Every hold has an owner and a release. Only the owner releases it; you make the gap visible in time.}}
"""),
        ("huddle", "The readiness huddle", "Go, hold, or stop, on the record", """
<p>A huddle the day before or the morning of surgery brings the gate owners together: transplant surgeon, anesthesia, transplant nephrologist, nursing, and the coordinator, with the donor&rsquo;s team for the donor. Keep it short and structured.</p>
{{flow:A readiness huddle|Identity::Both people, two identifiers each.|Gates::Each of the eight gates read aloud with its status and evidence.|Holds::Each hold with its release evidence, or stated as open.|New information::Anything since the last review, for each person.|Decision::Go, hold, or stop, stated by the authorized lead and recorded with the time.}}
<p>The coordinator presents the board; the authorized lead decides. If anyone in the huddle says they are not satisfied, the lead hears them before deciding. Record the decision, who made it, and any conditions.</p>
{{key:The huddle ends with one recorded decision by the authorized lead. Silence is not agreement.}}
"""),
        ("handoff", "Handoff each person separately", "Two teams, two handoffs", """
<p>On the day of surgery, the donor and recipient often go to different theaters and different wards, under different teams. Hand each one over separately, to their own receiving team, with read-back.</p>
<ul>
<li>Identity and the procedure.</li>
<li>Gates and their evidence, with any conditions still to be met.</li>
<li>Allergies, medicines, and anything the team flagged.</li>
<li>Contact preferences: who may receive updates for this person, and who may not.</li>
<li>For the donor: the donor&rsquo;s own follow-up contact and the plan beyond discharge.</li>
</ul>
<p>Never combine the two into one family update. The family waiting room is not a handoff channel, and each person&rsquo;s updates go only to the people they named.</p>
{{key:Two people, two handoffs, two update lists. Read back each one.}}
"""),
    ],
    "debrief": ["""
<p><strong>Closed and open.</strong> Recipient medical, donor medical (as of the last review), legal, ethics (condition closed), consent, and insurance are closed with evidence. Open: the crossmatch hold, which the 9-day-old result does not meet. New information not yet routed: the son&rsquo;s possible fever, which belongs to the donor&rsquo;s medical gate.</p>
<p><strong>Before 5 p.m.</strong> SBAR to the transplant nephrologist about the crossmatch hold, and arrange collection and the courier if a repeat is ordered. Call Mr. Paolo Manalo privately about the fever and route what he says to his donor clinicians today; they decide whether his medical gate stays closed. Update the board.</p>
<p><strong>Monday&rsquo;s huddle.</strong> Both identities, all eight gates with evidence, the crossmatch result and who reviewed it, the donor&rsquo;s fever review, any new information since Friday, and a go, hold, or stop decision by the authorized lead, recorded with the time. Then two separate handoffs.</p>
"""],
    "skills": {"title": "Readiness board and huddle",
               "intro": "Build a readiness board for a fictional pair, run a simulated huddle, and give two handoffs while your preceptor observes.",
               "items": [
                   ("Builds an eight-gate readiness view with owner and evidence for each gate.", True),
                   ("Identifies a hold that a stale result does not meet and routes it by SBAR in time.", True),
                   ("Routes new information (for example, a donor&rsquo;s fever) to the right gate owner the same day.", True),
                   ("Presents the board at a huddle without making the go or stop decision.", True),
                   ("Gives separate structured handoffs for donor and recipient with read-back.", False),
               ],
               "placement": "Attend one pre-surgery huddle. Record whether every gate was stated with its evidence and who made the final decision."},
    "terms": [("Readiness", "All gates closed by their owners on current evidence."), ("Hold", "A condition that must be met before surgery."),
              ("Huddle", "A short structured meeting ending in a recorded decision."), ("Authorized lead", "The person designated to make the go or stop decision."),
              ("Handoff", "A structured transfer of responsibility with read-back.")],
    "readings": [("kidney-transplant.html", "What patients are told about the day of surgery.")],
    "calcs": ["calc-transplant-coordinator-toolkit.html#tool-1"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["14"])
