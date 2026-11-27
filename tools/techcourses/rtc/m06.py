# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 06: Living Donor Intake and Protection. Written for this series from published sources."""

MODULE = {
    "image_alt": "A coordinator talking privately with an adult potential donor in a small quiet consultation room, door closed, both seated.",
    "objectives": [
        "Run a private first conversation with a potential living donor, without the recipient or family present.",
        "Apply the DOH living-donor safeguards at coordination level: age, relationship, advocate, psychosocial and social-work review, and ethics committee review.",
        "Recognize signs of pressure, inducement, or exploitation and route them to the safeguarding pathway.",
        "Make withdrawal safe, using neutral and truthful wording agreed with the donor.",
        "Explain why donor costs matter to voluntariness.",
    ],
    "big": """
{{plain:A living donor is like a volunteer firefighter. They choose to walk toward a risk to help someone else. A good fire chief never shames a volunteer who decides not to go in, never pays them under the table, and always makes sure someone is watching out for the volunteer&rsquo;s safety, not just the building&rsquo;s.}}
{{fig:rtc06_private}}
<p>The picture has a limit. A firefighter&rsquo;s choice is made in a moment, among colleagues. A donor&rsquo;s choice is made over weeks or months, inside a family, often with love, obligation, money, and history all pressing at once. That is why the DOH living-donor order surrounds the donor with protections that the recipient does not need: a designated donor advocate, psychiatric or clinical psychological evaluation, social-work assessment including evidence from a home visit, review by the Hospital Transplant Ethics Committee (HTEC), consent obtained by the surgeon with independent witnessing, and the right to withdraw.[[rtc_doh2021]]</p>
<p>The job of this module is to open the donor&rsquo;s pathway correctly. A donor is a person, not a resource. Your first conversation tells them whether this program is a place where they can ask hard questions and say no.</p>
{{cards:Key terms for this module|Potential donor::A person who has asked to be evaluated as a living donor.|Donor advocate::The person designated under the DOH order to protect the donor&rsquo;s interests, separate from the recipient&rsquo;s team.|Voluntariness::A choice made freely, without pressure, threat, or reward.|Inducement::An offer of money, goods, debt relief, a job, or any benefit in exchange for donation.|Withdrawal::The donor&rsquo;s decision to stop, at any point before surgery.|Restricted record::The part of the donor&rsquo;s record that holds private reasons and sensitive assessments, open only to those who need it.}}
""",
    "case": {"title": "The cousin and the debt", "html": """
<p>Mr. Rogelio Santos, 56, a factory supervisor in Valenzuela, needs a transplant. His cousin, Mr. Jun Pascual, 34, a delivery rider, calls the donor intake line and asks to be evaluated.</p>
<p>At the private intake, Mr. Pascual is friendly and keen. When you ask what made him decide, he says, &ldquo;Kuya Roger is family. And his boss said that after the operation, my loan with the company will be cleared. Win-win.&rdquo;</p>
<p>Two days later Mr. Santos&rsquo;s wife calls you. &ldquo;Please don&rsquo;t write the part about the loan. We&rsquo;re cousins. It&rsquo;s not a sale, it&rsquo;s family.&rdquo;</p>
""", "questions": ["Is this a concern? Which safeguard does it touch?",
                  "What do you document, where, and whom do you inform?",
                  "What do you say to Mrs. Santos, and what support continues for both men?"]},
    "sections": [
        ("person", "The donor is a person, not a resource", "The private first conversation", """
<p>The first contact sets the tone. Hold it in private, with the door closed, without the recipient or family present, and in the donor&rsquo;s preferred language. Explain, plainly:</p>
<ul>
<li>what the evaluation involves and how long it may take;</li>
<li>that the donor has their own team and their own record, separate from the recipient;</li>
<li>that surgery has short-term risks and a small long-term risk, which the donor&rsquo;s doctors will explain with numbers (Module 7);</li>
<li>that there may be practical costs and time off work, and what the program does about them;</li>
<li>that the donor may stop at any point, and the program will help them do so privately.</li>
</ul>
<p>Then listen. Neutral questions open doors: &ldquo;What makes you want to do this?&rdquo; &ldquo;What would happen if you decided not to?&rdquo; &ldquo;Has anyone offered you anything, or warned you about anything, if you donate or do not?&rdquo; Write down what the person says, factually, in their words where it matters.</p>
<p>The DOH order sets conditions you will check at coordination level and pass to the decision makers: in the inspected text, a living donor must be at least 21 years old and related to the recipient within the fourth degree of consanguinity or affinity, or have established emotional ties.[[rtc_doh2021]] You collect the evidence; the team, the advocate, and the ethics committee decide. Verify the current text, and do not import foreign age thresholds.</p>
{{key:The donor speaks for themself, in private, in their own language. The first conversation must make &ldquo;no&rdquo; feel safe.}}
"""),
        ("protect", "Arrange independent protections", "The donor&rsquo;s own safeguards", """
<p>Each protection answers a different question. Coordinate them as separate gates on the donor&rsquo;s pathway.</p>
<div class="table-wrap"><table>
<thead><tr><th>Protection (DOH AO 2021-0059)</th><th>Question it answers</th><th>What you coordinate</th></tr></thead>
<tbody>
<tr><td>Pre-transplant orientation</td><td>Does the donor understand what donation involves?</td><td>Scheduling, language, materials, attendance record</td></tr>
<tr><td>Designated donor advocate</td><td>Is someone looking after only the donor&rsquo;s interests?</td><td>Referral to the designated advocate; private meetings</td></tr>
<tr><td>Psychiatric or clinical psychological evaluation</td><td>Is the decision informed and free of undue pressure? Is the donor psychologically prepared?</td><td>Appointment, report received</td></tr>
<tr><td>Social-work assessment with home visit</td><td>What are the relationships, circumstances, and pressures at home?</td><td>Home visit scheduling, report received</td></tr>
<tr><td>HTEC review</td><td>Is this donation ethical and voluntary?</td><td>A complete submission (Module 9)</td></tr>
</tbody></table></div>
<p>A family relationship does not remove the need for any of these. Close relatives can feel the strongest pressure of all. And the recipient&rsquo;s coordinator should never quietly substitute for the designated advocate; the conflict of interest is built into the role.</p>
{{scene:The advocate who was also the coordinator|<p>At a small program, the donor advocate is on leave for a month, and the recipient&rsquo;s coordinator offers to &ldquo;cover the advocate meetings&rdquo; so the case does not slip.</p>
<p>The program manager declines and pauses the donor&rsquo;s advocate step until a designated alternate is available. The donor&rsquo;s other evaluations continue.</p>
<p class="tc-scene-take">A delay of two weeks was better than a safeguard run by someone working for the other side.</p>}}
{{key:Every safeguard answers its own question. A relationship, a signature, or a busy calendar does not stand in for any of them.}}
"""),
        ("pressure", "Recognize pressure and reward", "Red flags to route, not to investigate", """
<p>Most donors are motivated by love and a wish to help. A few are under pressure they cannot name, and a very few are being paid or exploited. Philippine law treats recruiting or obtaining a person by coercion, deceit, or intimidation for the removal or sale of organs as trafficking in persons.[[rtc_ra10364]] The WHO guiding principles and the Declaration of Istanbul both call for donation that is voluntary and financially neutral.[[rtc_who2010]][[rtc_istanbul2018]]</p>
<div class="table-wrap"><table>
<thead><tr><th>What you may hear or see</th><th>What it may mean</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>A promised job, debt relief, money, or goods after donation</td><td>Inducement</td><td>Record facts; pause progression; escalate to the advocate, HTEC, and safeguarding</td></tr>
<tr><td>The family answers every question for the donor</td><td>Possible pressure</td><td>Insist on private meetings; note it factually</td></tr>
<tr><td>A &ldquo;relative&rdquo; who knows little about the recipient&rsquo;s life</td><td>Possible false relationship</td><td>Verify documents through authorized channels (Module 8); escalate</td></tr>
<tr><td>Fear of consequences if they do not donate</td><td>Coercion</td><td>Reassure about privacy; escalate</td></tr>
<tr><td>A broker, agent, or third party arranging contact</td><td>Possible trafficking</td><td>Escalate at once through safeguarding and legal pathways</td></tr>
</tbody></table></div>
<p>Do not investigate alone, confront the family, or promise secrecy beyond what the law allows. Your role is to record what you observed, protect the donor&rsquo;s privacy, pause the elective progression, and route the concern to the people with the authority and training to assess it.</p>
{{key:A benefit tied to donation is a red flag even inside a loving family. Record, pause, and route; never investigate alone.}}
{{fig:tc06_fig_donor_red_flags_route}}
"""),
        ("withdraw", "Make withdrawal safe", "A truthful way to stop", """
<p>A donor who wants to stop often fears the family&rsquo;s reaction more than anything else. The program&rsquo;s job is to make stopping private and safe.</p>
<ul>
<li>Agree with the donor and the donor team on neutral, truthful wording for the recipient and family, such as &ldquo;The team is not able to proceed with this donor.&rdquo;</li>
<li>Never invent a medical problem. A false diagnosis is dishonest and can follow the donor into their own records and insurance.</li>
<li>Record the donor&rsquo;s reasons only in the restricted record.</li>
<li>Tell the recipient&rsquo;s team only that the donor pathway has closed, and support the recipient to look at other options.</li>
</ul>
<p>Costs belong in this section too, because unpaid costs can make a donor feel they cannot stop &mdash; or cannot afford to continue. A systematic review of 16 studies (6,158 donors) found that about 80% of donors had some financial loss, with total costs ranging from US$900 to US$19,900 and lost income the largest share; donors from lower-income households and those who traveled far had the greatest hardship.[[rtc_fu2021]] None of the studies were from Asia, so the size of the burden here is unknown, but the direction is likely similar. Modules 10 and 11 cover how to protect donors from costs.</p>
{{key:Withdrawal must be possible at every step, privately, with a truthful neutral message and no invented diagnosis.}}
"""),
    ],
    "debrief": ["""
<p><strong>Is it a concern?</strong> Yes. A promised debt cancellation from the recipient&rsquo;s employer is a benefit tied to donation: a potential inducement. It touches the voluntariness safeguard and may touch the anti-trafficking law. Being cousins does not neutralize it.</p>
<p><strong>Document and inform.</strong> Record Mr. Pascual&rsquo;s words factually in his restricted record, with the date and who was present. Pause the elective progression of his donor pathway. Inform his designated donor advocate and the HTEC through the program&rsquo;s safeguarding pathway, and the program manager. Do not confront the employer or investigate the loan yourself.</p>
<p><strong>Mrs. Santos.</strong> Be kind and clear: &ldquo;I understand this is family. I have to record what any potential donor tells us, and the ethics committee reviews it. That protects everyone.&rdquo; Do not share what Mr. Pascual said beyond what she already knows. Continue Mr. Santos&rsquo;s recipient workup unchanged, and keep supporting Mr. Pascual: he may still be evaluated if the concern is resolved, and he may stop at any time.</p>
"""],
    "skills": {"title": "Private donor intake",
               "intro": "Conduct a simulated private donor intake with a standardized donor while your preceptor observes.",
               "items": [
                   ("Holds the intake in private, in the donor&rsquo;s preferred language, without the recipient or family present.", True),
                   ("Explains the donor&rsquo;s separate team, record, risks, costs, and right to stop.", True),
                   ("Asks neutral questions about motivation, consequences, and offers.", False),
                   ("Collects age and relationship evidence for review without deciding eligibility.", False),
                   ("Arranges advocate, psychiatric or psychological, and social-work referrals.", False),
                   ("Documents a coercion or inducement concern factually in the restricted record and escalates.", True),
                   ("Agrees neutral, truthful withdrawal wording without inventing a diagnosis.", True),
               ],
               "placement": "Review your program&rsquo;s donor intake script and identify where the donor can say no privately at each step."},
    "terms": [("Potential donor", "A person who asked to be evaluated as a living donor."),
              ("Donor advocate", "Designated under the DOH order to protect the donor&rsquo;s interests."),
              ("Voluntariness", "A choice free of pressure, threat, or reward."), ("Inducement", "An offered benefit in exchange for donation."),
              ("Withdrawal", "The donor&rsquo;s decision to stop."), ("Restricted record", "Private donor information open only to those who need it.")],
    "readings": [("organ-donation-philippines.html", "Organ donation in the Philippines, for the public.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["06"])
