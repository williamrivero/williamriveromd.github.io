# -*- coding: utf-8 -*-
"""Renal Transplant Coordinator, Module 05: Compatibility and Safe Specimen Coordination. Written for this series from published sources."""

MODULE = {
    "image_alt": "A coordinator checking labels on sealed blood specimen tubes against a request form before handing a transport box to a courier.",
    "objectives": [
        "Explain blood group, tissue type, antibodies, and crossmatch in plain words, and why each matters.",
        "Recognize sensitizing events and make sure they reach the transplant team and the HLA laboratory.",
        "Protect the specimen chain from labeling to laboratory receipt.",
        "Relay a critical compatibility result with read-back, without interpreting it.",
    ],
    "big": """
{{plain:Think of the immune system as a security guard with a very good memory for faces. Every cell in your body carries a kind of ID badge. The guard ignores your own badges and attacks strangers. A transplanted kidney arrives wearing someone else&rsquo;s badges, so the team needs to know two things: how different the new badges are, and whether the guard has already met, and learned to hate, badges like them.}}
<p>The picture has a limit. Real immune memory is not a single guard but many cells, and the &ldquo;badges&rdquo; come in several kinds. Two matter most for a coordinator to understand. The first is the <strong>ABO blood group</strong>, the same system used for blood transfusion: people make antibodies against blood groups they do not have, so a group O recipient cannot receive a standard kidney from a group A donor. The second is the <strong>human leukocyte antigen (HLA)</strong> system, the tissue type. A recipient can carry antibodies against HLA from earlier exposure to someone else&rsquo;s tissue. If those antibodies match the donor&rsquo;s HLA &mdash; a <strong>donor-specific antibody (DSA)</strong> &mdash; the kidney can be attacked, sometimes within hours.</p>
<p>Your job is not to interpret any of this. Your job is to keep the samples trustworthy, keep the laboratory informed about anything that can change a person&rsquo;s antibodies, and get critical results to the right clinician fast.</p>
{{cards:Key terms for this module|ABO blood group::Groups O, A, B, and AB. Standard transplants follow blood-transfusion compatibility.|HLA (tissue type)::Markers on cells that the immune system uses to recognize self.|HLA antibodies::Antibodies a person has made against other people&rsquo;s HLA.|Calculated panel reactive antibody (cPRA)::An estimate of the share of donors a person would likely react against.|Crossmatch::A laboratory test that mixes recipient serum with donor cells or HLA to look for a reaction.|Sensitizing event::An exposure that can create new HLA antibodies: blood transfusion, pregnancy, or a previous transplant.}}
""",
    "case": {"title": "The transfusion nobody mentioned", "html": """
<p>Mr. Allan Ramos, 44, is on the waiting list and has a living donor, his wife, Mrs. Cora Ramos, under evaluation. His last HLA antibody screen, three months ago, showed few antibodies.</p>
<p>On a Saturday he is admitted to a district hospital in Laguna for bleeding from a dialysis access and receives two units of packed red cells. He goes home Monday. Nobody tells the transplant center.</p>
<p>On Wednesday you are preparing the final crossmatch samples for both. At the bedside, the recipient&rsquo;s tube is labeled with his name only; the request form has his name and hospital number. The courier to the HLA laboratory is waiting at the door.</p>
""", "questions": ["Why does the transfusion matter, and who must know?",
                  "What do you do with the half-labeled tube?",
                  "If the laboratory later phones a positive crossmatch, what is your role?"]},
    "sections": [
        ("matching", "Why matching is more than a blood group", "Two systems in plain words", """
<p>A coordinator does not need immunology to coordinate well, but needs enough to know why the steps exist.</p>
<div class="table-wrap"><table>
<thead><tr><th>Test</th><th>The question it answers</th><th>What changes it</th></tr></thead>
<tbody>
<tr><td>ABO blood group</td><td>Are recipient and donor blood groups compatible?</td><td>Nothing; it is fixed (except in rare situations the team handles)</td></tr>
<tr><td>HLA typing</td><td>What tissue type do recipient and donor have?</td><td>Nothing; it is fixed</td></tr>
<tr><td>HLA antibody screen (and cPRA)</td><td>Which HLA does the recipient have antibodies against?</td><td>Sensitizing events: transfusion, pregnancy, previous transplant</td></tr>
<tr><td>Crossmatch</td><td>Does this recipient react to this donor now?</td><td>Any change in antibodies since the last sample</td></tr>
</tbody></table></div>
<p>The last two rows explain the coordinator&rsquo;s duty. Antibodies change; blood group and tissue type do not. KDIGO advises HLA antibody testing at evaluation and at regular intervals before transplant, and that all sensitizing events, and clinical events that can affect antibody levels, be communicated to the HLA laboratory.[[rtc_kdigo2020]] A transfusion in another hospital that nobody reports can make a three-month-old antibody result describe a different person.</p>
<p>A high cPRA means a person reacts to many potential donors and may wait longer; a separate site guide explains how programs approach highly sensitized candidates. ABO-incompatible or HLA-incompatible transplant programs exist in some centers, but whether and how to use them is a clinical decision.</p>
{{key:Blood group and tissue type stay the same; antibodies change. Every transfusion, pregnancy, or previous transplant must reach the team and the HLA laboratory.}}
"""),
        ("events", "Catch sensitizing events", "Ask, every time", """
<p>Sensitizing events happen outside the transplant center: a transfusion during an emergency, a pregnancy, a miscarriage, a surgery elsewhere. People rarely think to mention them. Build the question into every contact.</p>
<ul>
<li>At every monthly or waiting-list contact: &ldquo;Since we last spoke, have you been admitted anywhere, had a blood transfusion, been pregnant, or had any surgery?&rdquo;</li>
<li>Ask the person&rsquo;s dialysis unit to tell you of any transfusion, and give them a direct number.</li>
<li>Record the date and place of the event, and request the transfusion record if possible.</li>
<li>Tell the transplant physician and the HLA laboratory the same day, through the program&rsquo;s channel.</li>
</ul>
{{scene:The miscarriage|<p>At a waiting-list call, a candidate mentions she had a miscarriage two months ago and was treated in a provincial hospital. She did not think it mattered.</p>
<p>Coordinator Ms. Ana Lim thanks her, records the date in the candidate&rsquo;s file, and notifies the transplant physician and the HLA laboratory that afternoon. The laboratory asks for a new sample at her next dialysis session.</p>
<p class="tc-scene-take">Pregnancy, including one that ends early, can create HLA antibodies. The person did not know; the question found it.</p>}}
{{key:Ask about admissions, transfusions, pregnancies, and surgeries at every contact, and report the same day.}}
"""),
        ("chain", "Protect the specimen chain", "A sample is only as good as its weakest link", """
{{fig:rtc05_specimen}}
<p>A compatibility result is only as trustworthy as the sample behind it. A mislabeled or delayed tube can produce a result that belongs to someone else, or a result that no longer describes the person.</p>
<div class="table-wrap"><table>
<thead><tr><th>Link</th><th>What can go wrong</th><th>Control</th></tr></thead>
<tbody>
<tr><td>Request</td><td>Wrong test, wrong donor paired</td><td>Check the request against the team&rsquo;s order and the pairing</td></tr>
<tr><td>Collection and labeling</td><td>Wrong patient, incomplete label</td><td>Two identifiers on the tube, labeled at the bedside, at the time of collection</td></tr>
<tr><td>Packaging</td><td>Wrong temperature, leaking tube</td><td>Follow the laboratory&rsquo;s transport instructions and container</td></tr>
<tr><td>Transport</td><td>Delay, loss</td><td>A courier log with times and signatures</td></tr>
<tr><td>Receipt</td><td>Sample unaccounted for</td><td>The laboratory confirms receipt; you record it</td></tr>
</tbody></table></div>
<p>An incompletely labeled sample is never repaired after collection. Writing the second identifier on the tube later, or asking the courier to do it, breaks the link between the tube and the person. Re-collect and relabel at the bedside, and let the courier wait or reschedule.</p>
{{key:Label at the bedside with two identifiers. A tube labeled later is a tube of unknown origin.}}
"""),
        ("relay", "Communicate within scope", "Relay critical results, do not interpret them", """
<p>Compatibility results can change the plan in an hour. When the laboratory calls with a critical result &mdash; a positive crossmatch, a new donor-specific antibody, a blood-group discrepancy &mdash; three things matter: speed, accuracy, and the right recipient of the message.</p>
<ol>
<li>Write the result down as stated, with the caller&rsquo;s name and time.</li>
<li>Read it back to the caller and confirm.</li>
<li>Call the transplant physician on duty at once; read it again.</li>
<li>Record who received it and when. Close the loop when the physician confirms the next step.</li>
</ol>
<p>Do not tell the recipient or donor what the result means. A positive crossmatch has several possible explanations and responses, all of them clinical. If a family asks, say truthfully that a result has come in and the doctor will speak with them.</p>
{{key:Write it, read it back, route it, record it. The meaning of the result belongs to the team.}}
"""),
    ],
    "debrief": ["""
<p><strong>The transfusion.</strong> Two units of red cells can create new HLA antibodies, so Mr. Ramos&rsquo;s three-month-old antibody screen may no longer describe him, and his wife&rsquo;s crossmatch could change. Tell the transplant physician and the HLA laboratory today, with the date, place, and units, and request the transfusion record from the Laguna hospital. Ask his dialysis unit to report future transfusions directly.</p>
<p><strong>The tube.</strong> Do not send it and do not add the hospital number yourself. Re-collect and label at the bedside with two identifiers; let the courier wait or reschedule. Record the re-collection.</p>
<p><strong>A positive crossmatch.</strong> Write it down, read it back, call the transplant physician at once, and record the handoff. Do not interpret it for the couple. The team will decide what it means and what to do next.</p>
"""],
    "skills": {"title": "Specimen chain and critical result relay",
               "intro": "Prepare, label, package, and dispatch a mock compatibility specimen, and relay a mock critical result, while your preceptor observes.",
               "items": [
                   ("Explains ABO, HLA, antibodies, cPRA, and crossmatch in plain words.", False),
                   ("Asks a candidate about admissions, transfusions, pregnancies, and surgeries since last contact.", True),
                   ("Reports a sensitizing event to the transplant physician and the HLA laboratory the same day.", True),
                   ("Refuses to dispatch an incompletely labeled tube and arranges re-collection.", True),
                   ("Completes a courier log and confirms laboratory receipt.", False),
                   ("Relays a critical result with read-back and records the handoff, without interpreting it.", True),
               ],
               "placement": "Follow one real compatibility sample from request to laboratory receipt and map every handoff."},
    "terms": [("ABO", "The blood-group system used for transfusion and standard transplant compatibility."),
              ("HLA", "Human leukocyte antigen, the tissue type."), ("DSA", "Donor-specific antibody."),
              ("cPRA", "Calculated panel reactive antibody."), ("Crossmatch", "A test for reaction between recipient serum and donor cells or HLA."),
              ("Sensitizing event", "Transfusion, pregnancy, or a previous transplant.")],
    "readings": [("highly-sensitized-kidney-transplant-candidates-clinician.html", "How programs approach candidates with many antibodies.")],
    "calcs": [],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("rtc_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["05"])
