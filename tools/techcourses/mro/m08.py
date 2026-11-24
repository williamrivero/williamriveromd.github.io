# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 08: Privacy, Patient Rights, and Release of Information. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer at a release counter politely checking a woman's written authorization and ID card.",
    "objectives": [
        "Explain why health information is sensitive personal information under Philippine law.",
        "Process a release request through identity, authority, purpose, scope, and channel, then log it.",
        "Recognize requests that must go to the data protection officer or counsel.",
        "Handle access and correction requests as rights, and route corrections to their authors.",
        "Escalate a possible breach within the hour, preserve its evidence, and explain the 72-hour notification clock.",
    ],
    "big": """
{{plain:A dialysis chart is like a house key. In the right hands it opens the door to good care. In the wrong hands it opens the same door to someone who should never be inside. A copy of a key is just as dangerous as the original, and you cannot take it back once it is cut.}}
<p>The picture is useful, and it has one limit. A lost key can be replaced by changing the lock. A released chart cannot be recalled. It holds a person&rsquo;s diagnoses, their hepatitis and HIV status, their finances, their family contacts, and sometimes their address. In the wrong hands it can cost a patient a job, a relationship, an insurance policy, or their safety.</p>
<p>The law treats it accordingly. Under the Data Privacy Act, health information is sensitive personal information, and processing it needs a lawful basis, proportionality, and safeguards.[[dch_ra10173]] Breaches are not hypothetical in Philippine health care: in September 2023 the Philippine Health Insurance Corporation (PhilHealth) itself suffered a ransomware attack that forced manual operations and prompted an investigation by the National Privacy Commission (NPC).[[mro_ph2023medusa]]</p>
{{cards:Key terms for this module|Sensitive personal information::Under the Data Privacy Act, a category that includes health information and needs extra protection.|Data subject::The person the information is about.|Minimum necessary::Releasing only what the stated purpose requires.|Data protection officer (DPO)::The person designated to oversee privacy compliance and advise on incidents.|Personal information controller (PIC)::The organization that decides how personal data are used, and decides on breach notification.|Data Breach Notification Management System (DBNMS)::The NPC&rsquo;s online system for filing breach notifications.}}
""",
    "case": {"title": "The sister and the wrong email", "html": """
<p>It is a Tuesday afternoon. At 1:50 p.m. the phone rings. A woman says she is the sister of Mr. Romeo Garcia, 49, who dialyzes on your Tuesday-Thursday-Saturday shift. &ldquo;He asked me to handle his insurance. Please send his complete chart to my Gmail. I need it today.&rdquo; She sounds upset and in a hurry. Nothing in Mr. Garcia&rsquo;s chart names her or authorizes anyone to receive his records.</p>
<p>At 2:10 p.m., while you are still writing down the call, your colleague Ms. Kristine Bautista comes to your desk, pale. At 2:00 p.m. she emailed a laboratory page for Mrs. Erlinda Torres, with her name, patient number, and hepatitis results, to an outside address. She meant to send it to the hospital&rsquo;s laboratory; she picked a similar-looking address from the autocomplete list.</p>
""", "questions": ["What do you tell the caller, and what do you log?",
                  "What do you do about the misdirected email, and by when?",
                  "Who decides whether the NPC must be notified, and by when would notification be due?"]},
    "sections": [
        ("five", "Five checks", "Five checks before any release", """
{{fig:mro08_checks}}
<p>Every release of a record, whether a single laboratory page or a full chart, passes through the same five checks, in the same order.</p>
{{flow:Before you release anything|Identity::Is the requester who they claim to be? Verify with approved identifiers, in person or through an independently trusted channel.|Authority::On what basis may they receive it? The patient, a representative with written authority, a receiving facility for continuity of care, PhilHealth for a claim, a court order, or the Department of Health (DOH) for inspection.|Purpose::Why do they need it?|Scope::The minimum necessary for that purpose.|Channel::A verified, approved route: pickup with ID, the facility&rsquo;s secure email or portal, or a sealed courier. Never a personal email address or an unapproved messaging app.}}
<p>The checks work together. A request can pass identity and fail authority: the caller really is the patient&rsquo;s sister, but the patient never authorized her. A request can pass authority and fail scope: the employer is entitled to know the patient&rsquo;s dialysis schedule, not their hepatitis status. A request can pass everything and fail the channel: the right document to the right person, sent to a personal email that three other family members can open.</p>
<div class="table-wrap"><table>
<thead><tr><th>Requester</th><th>Usual authority</th><th>Usual scope</th></tr></thead>
<tbody>
<tr><td>The patient, in person with ID</td><td>Their own right of access</td><td>What they ask for</td></tr>
<tr><td>A relative or friend</td><td>Only with the patient&rsquo;s written authorization or documented legal authority</td><td>What the authorization covers</td></tr>
<tr><td>A receiving dialysis unit</td><td>Continuity of care, on the physician&rsquo;s authorization</td><td>What the receiving team needs to treat (Module 14)</td></tr>
<tr><td>PhilHealth</td><td>Claims processing and audit, under its rules</td><td>The claim packet and what an audit requests</td></tr>
<tr><td>An employer or school</td><td>Only with the patient&rsquo;s authorization</td><td>Schedule and functional statements only (Module 9)</td></tr>
</tbody></table></div>
<p>Then log every release: what was sent, to whom, by whom, when, under what authority, and through which channel. The release log is how you will answer the patient who later asks, &ldquo;Who has seen my records?&rdquo;</p>
<h3>Requests that are not yours to decide</h3>
<p>Some requests go straight to the data protection officer (DPO) or counsel. You log them and route them; you do not answer them.</p>
<ul>
<li>Subpoenas and court orders</li>
<li>Requests from the police, the media, or a lawyer for another party</li>
<li>Relatives without documented authority, especially in a family dispute</li>
<li>Requests about a patient who has died</li>
<li>Anything unfamiliar, or anything that makes you uneasy</li>
</ul>
<p>Urgency is not authority. A caller who is upset, in a hurry, or claims to be a doctor still passes the same five checks. Pressure to skip them is itself a reason to slow down.</p>
"""),
        ("rights", "Patient rights", "Access and correction are rights", """
<p>Patients may ask for copies of their own records, and they may ask that errors be corrected. These are rights, not favors, and they should be handled promptly and without making the patient explain why they want to see their own chart.</p>
<p>These requests also catch real mistakes. In a survey of 22,889 patients who read their visit notes, 21.1% reported a perceived mistake, and 42.3% of those judged it serious.[[mro_bell2020]] The survey measured what patients <em>perceived</em>; not every reported mistake was confirmed. But it shows that patients who read their records are an error-detection system the unit gets for free.</p>
{{flow:A correction request|Log it::Date, patient, what they say is wrong.|Verify identity::The same two identifiers as any release.|Route to the author::Through the clinical correction workflow (Module 4).|Track it::The author agrees and corrects, or disagrees and documents why.|Tell the patient::The outcome, in writing.|Keep the request::With the record, so a reader sees that the entry was disputed.}}
<p>Never delete or overwrite a disputed entry yourself, even when the patient is plainly right about a simple fact such as a misspelled name. A spelling correction to an identifier goes through the identity workflow (Module 3). A clinical correction goes to its author.</p>
"""),
        ("breach", "A possible breach", "The first hour", """
{{fig:mro08_hour}}
<p>A misdirected email. A lost logbook. An unlocked records room overnight. A run sheet left at the pharmacy counter. Unexplained access in the audit trail. Any of these may be a breach. You do not need to decide whether it is. You need to report it.</p>
<p>Report internally <strong>at once</strong>, within the hour of discovery, to the DPO. Write down the facts: what happened, who was involved, when it happened, when and how it was discovered. Protect logs and devices, so the evidence of what happened is not lost. Support containment, such as asking the wrong recipient, through the DPO&rsquo;s approved wording, to delete the message and confirm in writing.</p>
<p>Do not investigate alone. Do not contact affected patients yourself. Do not reassure anyone that &ldquo;it is probably fine.&rdquo; Those steps belong to the people who decide on notification.</p>
<h3>Who decides, and how fast</h3>
<p>The personal information controller (PIC), through its breach response team and advised by the DPO, decides whether notification is required. Under NPC Circular 16-03, notification to the Commission and to affected data subjects is due within 72 hours of knowledge of, or reasonable belief in, a breach that requires notification. It is based on the information available, even if the full extent is not yet known.[[dch_npc1603]][[mro_npc_irr]] Notifications are filed through the NPC&rsquo;s Data Breach Notification Management System (DBNMS), and filing a request there does not pause the clock.[[mro_npc2026dbnms]]</p>
<p>Seventy-two hours sounds like a long time. It is not, once you subtract a weekend, the time to find out what was in the email, the time to reach the facility head, and the time to draft a notice. Every hour lost at the front line is taken from the people who must decide.</p>
{{call:Do not wait for proof of harm. The 72-hour clock runs from the organization&rsquo;s knowledge, so an hour lost at the front line is an hour taken from the controller. When unsure whether something is a breach, report it and let the DPO decide.}}
<p>The toolkit&rsquo;s 72-hour clock calculator shows the deadline from the moment of awareness.</p>
"""),
        ("culture", "A reporting culture", "Making it safe to report", """
<p>Ms. Bautista walked to your desk ten minutes after she made her mistake. That is the best possible outcome of a bad moment, and it happened because she was not afraid to tell you.</p>
<p>Units where staff are punished for reporting their own errors do not have fewer errors. They have fewer reports, and the breaches surface weeks later, when the 72 hours are long gone. Thank the person who reports. Let the DPO and the unit manager handle any follow-up about how it happened. Your role is to make sure the clock starts on time.</p>
<div class="table-wrap"><table>
<thead><tr><th>Usual reaction</th><th>Better reaction</th></tr></thead>
<tbody>
<tr><td>&ldquo;How could you?&rdquo;</td><td>&ldquo;Thank you for telling me right away. Let&rsquo;s write down what happened.&rdquo;</td></tr>
<tr><td>&ldquo;Let&rsquo;s keep this between us.&rdquo;</td><td>&ldquo;I need to report this to the DPO now. You did the right thing.&rdquo;</td></tr>
<tr><td>&ldquo;Email them and ask them to delete it.&rdquo;</td><td>&ldquo;The DPO will tell us exactly what to send.&rdquo;</td></tr>
</tbody></table></div>
"""),
    ],
    "debrief": ["""
<p><strong>The caller.</strong> Explain politely that the unit must verify identity and authority before releasing any records, and that records are released only through approved channels, never to a personal email address. Ask her to bring Mr. Garcia&rsquo;s signed written authorization and her own ID, or to come with him on Thursday. Offer to let Mr. Garcia know she called. Log the request, including that nothing was released. She may be exactly who she says she is. The checks protect him either way.</p>
<p><strong>The email.</strong> Escalate to the DPO immediately, by 2:15 p.m. Record the facts with Ms. Bautista: sent at 2:00 p.m., reported at 2:10 p.m., what the page contained, the exact recipient address. Preserve the sent item; do not delete it. Follow the DPO&rsquo;s instructions on asking the recipient to delete and confirm. Thank Ms. Bautista.</p>
<p><strong>Who decides, and by when?</strong> The personal information controller, through its breach response team, advised by the DPO. If notification is required, the 72-hour window from the organization&rsquo;s knowledge, which began when the report reached your desk, ends at about 2:10 p.m. on Friday. Hepatitis results with a name and patient number are sensitive personal information, so this needs a decision quickly.</p>
<p>Two requests reached your desk in twenty minutes: one to release something you should not, one about something released by mistake. Part of your role is to slow down the first and speed up the second.</p>
"""],
    "skills": {"title": "Release decision and breach escalation",
               "intro": "Role-play a release request and a misdirected disclosure with your preceptor and a role player.",
               "items": [
                   ("Verifies identity and authority before any disclosure.", True),
                   ("Declines an urgent request politely without releasing anything, and offers a lawful route.", True),
                   ("Releases only the minimum necessary through an approved channel and logs it.", False),
                   ("Routes subpoenas, police, media, and unfamiliar requests to the DPO or counsel.", False),
                   ("Routes a patient&rsquo;s correction request to the author and tells the patient the outcome.", False),
                   ("Escalates a possible breach to the DPO within the hour and preserves evidence.", True),
                   ("Computes the 72-hour notification deadline from the moment of awareness.", False),
                   ("Does not contact affected patients or investigate alone.", False),
               ],
               "placement": "Find your unit&rsquo;s release log and DPO contact. Check that both are current, and that the release log has an entry for every release in the last month."},
    "terms": [("Sensitive personal information", "Under the Data Privacy Act, includes health information."),
              ("Data subject", "The person the information is about."), ("Minimum necessary", "Only what the purpose requires."),
              ("DPO", "Data protection officer."), ("PIC", "Personal information controller."),
              ("NPC", "National Privacy Commission."), ("DBNMS", "Data Breach Notification Management System.")],
    "readings": [("personal-medical-journal-health-history.html", "Helping patients keep their own health history.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["08"])
