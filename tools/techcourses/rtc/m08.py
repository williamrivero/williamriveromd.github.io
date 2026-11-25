# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 08: Legal Documents and Informed Consent. Written for this series from published sources."""

MODULE = {
    "image_alt": "A coordinator checking civil registry documents against a manifest checklist at a desk with a document scanner.",
    "objectives": [
        "Assemble a legal packet in which every document records where, by whom, and when it was verified.",
        "Verify identity and relationship documents through authorized channels, and route corrections through the legal route.",
        "Explain consent as a process that continues until surgery, obtained by the surgeon with independent witnessing.",
        "Support understanding with interpreters and teach-back, without the recipient acting as interpreter.",
        "Handle exceptional cases (foreign nationals, unusual relationships, capacity questions) by escalation, not improvisation.",
    ],
    "big": """
{{plain:A legal packet is like the chain of title for a piece of land. A buyer does not trust a land title because it looks official. They trace it: who issued it, which registry holds the original, and whether every transfer was recorded. A photocopy that cannot be traced back to the registry is just a nice-looking piece of paper.}}
{{fig:rtc08_packet}}
<p>The picture has a limit. Land does not have feelings, and a land title does not change its mind. A donor&rsquo;s consent is not a title you transfer once; it is a continuing agreement the donor may withdraw until the operation. So this module has two halves that work differently: documents, which must be authentic and traceable, and consent, which must be informed, voluntary, and alive until the last moment.</p>
<p>The DOH living-donor order requires documentation of identity and relationship, and sets out how donor consent is obtained: by the surgeon, with specified independent witnessing, with the right to withdraw preserved.[[rtc_doh2021]] Your job is to build a packet a reviewer can trust, and to set up consent conversations that a donor can actually understand.</p>
{{cards:Key terms for this module|Legal packet::The set of documents that prove identity, relationship, and consent for a living donation.|Manifest::A list of every document in the packet, with source, verifier, and date.|Authenticated copy::A copy certified through the issuing agency&rsquo;s or the hospital&rsquo;s authorized process.|Deed of donation::The signed instrument by which the donor records the gift, as the program&rsquo;s legal forms require.|Informed consent::Agreement after understanding the purpose, risks, alternatives, and the right to refuse.|Teach-back::The person explains in their own words what they understood.}}
""",
    "case": {"title": "The photocopy and the interpreter", "html": """
<p>Mrs. Leticia Dizon, 51, from Pampanga, is being evaluated as a donor for her younger brother, Mr. Arnel Cruz, 47. Their mother&rsquo;s maiden name differs between the two birth certificates in the packet; one is a clear photocopy, the other a certified copy from the Philippine Statistics Authority (PSA).</p>
<p>Mrs. Dizon reads little English and is most comfortable in Kapampangan. Mr. Cruz&rsquo;s wife offers to translate at the consent meeting: &ldquo;I speak Kapampangan, and it&rsquo;s family anyway.&rdquo;</p>
<p>A notarized affidavit of relationship spells Mrs. Dizon&rsquo;s middle name with one letter wrong. The consent meeting with the surgeon is on Friday.</p>
""", "questions": ["What do you do about the photocopy and the differing maiden names?",
                  "Who should interpret at the consent meeting, and how will understanding be checked?",
                  "How is the affidavit corrected?"]},
    "sections": [
        ("packet", "Build a traceable legal packet", "Every document, its source, its verifier, its date", """
<p>A reviewer &mdash; the ethics committee, PhilHealth, a regulator, a court &mdash; should be able to pick up the packet and see, for every document, what it proves and how you know it is authentic.</p>
<div class="table-wrap"><table>
<thead><tr><th>Document type</th><th>What it proves</th><th>How it is verified</th></tr></thead>
<tbody>
<tr><td>Government-issued identification</td><td>Identity and age</td><td>Original seen and compared with the person; copy marked as seen</td></tr>
<tr><td>Birth and marriage certificates</td><td>Relationship within the stated degree</td><td>PSA-certified copies, or through the program&rsquo;s authorized verification route</td></tr>
<tr><td>Affidavits</td><td>Facts the certificates cannot show, such as emotional ties</td><td>Properly executed and notarized; consistency checked against other documents</td></tr>
<tr><td>Deed of donation and program forms</td><td>The donor&rsquo;s recorded intention</td><td>Signed under the program&rsquo;s procedure</td></tr>
<tr><td>Consent record</td><td>Informed, voluntary agreement</td><td>Obtained by the surgeon with independent witnessing</td></tr>
</tbody></table></div>
<p>Keep a <strong>manifest</strong> on top: each document, what it proves, its source, who verified it, how, and when. When documents disagree &mdash; a different maiden name, a different birth date &mdash; do not choose the version that &ldquo;looks right.&rdquo; Record the discrepancy and route it for verification. A discrepancy may be a clerical error; it may also be the first sign of a false relationship (Module 6).</p>
<p>Corrections follow the legal route. A notarized affidavit with an error is corrected by a properly executed new or corrective document, not by correction fluid or a handwritten note above the line. Keep the original and the correction together, so the trail is visible.</p>
{{key:A document is trusted because it can be traced, not because it looks official. Record source, verifier, and date for every page.}}
"""),
        ("process", "Consent is a process", "Informed, voluntary, and alive until surgery", """
<p>Consent is not the signature. The signature records a conversation that should have covered the purpose of the operation, the risks with honest numbers (Module 7), the alternatives for the recipient, the costs, the follow-up, and the right to refuse or withdraw at any time before surgery. Under the DOH order, the surgeon obtains the donor&rsquo;s consent, with the independent witnessing the order specifies.[[rtc_doh2021]] The coordinator prepares and supports; the coordinator does not obtain surgical consent.</p>
<ul>
<li><strong>Prepare.</strong> Schedule enough time, in a private room, with the right interpreter.</li>
<li><strong>Support understanding.</strong> Give materials in the person&rsquo;s language beforehand; after the discussion, use teach-back: &ldquo;Can you tell me in your own words what the operation involves and what you can do if you change your mind?&rdquo;</li>
<li><strong>Keep it alive.</strong> Check again before surgery that the donor still wishes to proceed, and that nothing has changed.</li>
</ul>
{{scene:&ldquo;Do you understand?&rdquo;|<p>At a consent meeting, the donor nods when asked &ldquo;Do you understand?&rdquo; Coordinator Ms. Celia Ramos, there to support, asks instead: &ldquo;What will you do if you decide next week that you don&rsquo;t want to go ahead?&rdquo;</p>
<p>The donor says she thinks it is too late once she has signed. The surgeon explains again that she may withdraw until the operation, privately, through her advocate or the coordinator. Ms. Ramos records the teach-back in the donor&rsquo;s record.</p>
<p class="tc-scene-take">A nod is politeness. Teach-back is understanding.</p>}}
{{key:A signature records a conversation. Check understanding with teach-back and check the decision again before surgery.}}
"""),
        ("language", "Interpreters and capacity", "Understanding is the point", """
<p>An interpreter must be competent in both languages and independent of the outcome. The recipient, the recipient&rsquo;s spouse, and anyone who stands to gain from the donation have a conflict: they may soften the risks or add pressure without meaning to. Use a qualified hospital interpreter or an independent staff member fluent in the language, and record who interpreted.</p>
<p>Some donors raise questions of capacity: a learning disability, a mental illness, severe distress. Capacity is assessed by clinicians, not by coordinators. If you notice that a donor cannot repeat back the main points, or seems confused, record what you observed and route it to the donor&rsquo;s team and advocate before any consent meeting.</p>
<div class="table-wrap"><table>
<thead><tr><th>Situation</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>Donor prefers a regional language</td><td>Independent interpreter; materials in that language where available</td></tr>
<tr><td>Donor cannot read</td><td>Materials read aloud; extra time; teach-back</td></tr>
<tr><td>Donor seems unable to understand or recall</td><td>Record observations; route to clinicians and advocate</td></tr>
<tr><td>Family member offers to interpret</td><td>Thank them; arrange an independent interpreter</td></tr>
</tbody></table></div>
{{key:The interpreter must be competent and independent. Never let the recipient&rsquo;s side translate the donor&rsquo;s consent.}}
"""),
        ("exceptions", "Handle exceptional cases deliberately", "Escalate, do not improvise", """
<p>Some cases need more review than the standard pathway: a donor or recipient who is a foreign national, a relationship based on emotional ties rather than kinship, a donor who lives abroad, or a donor whose documents come from another country. The DOH order and your hospital&rsquo;s policy set additional requirements for some of these; the ethics committee often reviews them with extra care.[[rtc_doh2021]] Treat them as exceptional on purpose: list what is different, ask the program manager and legal office which additional steps apply, and record the answer in the register.</p>
<p>Privacy applies to every page. Identity and civil registry documents are personal information, and health information is sensitive personal information under the Data Privacy Act.[[rtc_ra10173]] Store the packet in the approved system, share it only with those who need it, and never send it through personal messaging apps.</p>
{{key:When a case is unusual, name what is unusual and ask who decides the extra steps. Improvising is how safeguards get skipped.}}
"""),
    ],
    "debrief": ["""
<p><strong>The photocopy and the names.</strong> Request a PSA-certified copy of the second birth certificate, or verify it through the program&rsquo;s authorized route. Record the maiden-name discrepancy in the manifest and route it for verification; it may be a clerical error, but it bears directly on the relationship the ethics committee must confirm. Do not choose a version.</p>
<p><strong>The interpreter.</strong> Thank Mrs. Cruz and decline: as the recipient&rsquo;s wife she has a conflict. Arrange a qualified, independent Kapampangan interpreter for Friday, send materials in advance, and plan teach-back after the surgeon&rsquo;s discussion. Record who interpreted.</p>
<p><strong>The affidavit.</strong> Route it for a properly executed corrective document through the notary and program&rsquo;s legal office. Keep both versions in the packet with the correction trail. If the correction cannot be completed by Friday, the consent discussion can still take place; the packet stays open in the register until the correction is in.</p>
"""],
    "skills": {"title": "Legal packet and consent preparation",
               "intro": "Assemble a mock legal packet and prepare a consent meeting while your preceptor observes.",
               "items": [
                   ("Builds a manifest that records source, verifier, method, and date for each document.", True),
                   ("Identifies and routes a discrepancy between documents without choosing a version.", True),
                   ("Explains why a notarized document is corrected through the legal route, not altered.", False),
                   ("Arranges an independent, qualified interpreter and declines a conflicted family interpreter.", True),
                   ("Supports a consent discussion and records teach-back, without obtaining consent.", True),
                   ("Lists the additional review steps for an exceptional case and records who decided them.", False),
               ],
               "placement": "Audit one completed legal packet (with fictional identifiers removed). Mark each document whose source or verifier is not recorded."},
    "terms": [("Legal packet", "Documents proving identity, relationship, and consent."), ("Manifest", "The packet&rsquo;s list of documents with source, verifier, and date."),
              ("Authenticated copy", "A copy certified through an authorized process."), ("Informed consent", "Agreement after understanding purpose, risks, alternatives, and the right to refuse."),
              ("PSA", "Philippine Statistics Authority.")],
    "readings": [("organ-donation-philippines.html", "How donation works in the Philippines, for the public.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["08"])
