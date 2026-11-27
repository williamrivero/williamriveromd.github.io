# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 01: Role, Designation, and Sources of Authority. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer and a unit manager reviewing a binder labeled role file at a desk in a dialysis clinic office.",
    "objectives": [
        "Tell a licensing rule from a payer rule, a professional guideline, and a privacy law.",
        "Read any rule for its issuer, scope, and effective date before acting on it.",
        "Explain the line between keeping a record and authoring what is in it.",
        "Assemble the role file an inspector expects: designation, contract, training, manual, and deputy.",
        "Route coding, claims, privacy, and destruction decisions to their owners, each with a named alternate.",
    ],
    "big": """
{{plain:Picture a basketball game with four referees, each carrying a different rulebook. One decides whether your team may play at all. One decides whether your team gets paid. One judges whether you played well. One watches whether anyone was hurt. Each referee rewrites the rulebook on their own schedule and does not tell the others. A dialysis unit plays in front of all four, every day, and its records are the scoreboard all four read.}}
{{fig:mro00_chain}}
<p>The picture is useful, and it has one limit. In a real game the referees agree on what a foul is. These four do not. The Department of Health (DOH) asks whether the unit may operate. The Philippine Health Insurance Corporation (PhilHealth) asks whether a session should be paid. The Philippine Society of Nephrology (PSN) describes what good practice looks like. The National Privacy Commission (NPC) asks whether personal information was handled lawfully. The same chart page can satisfy one and fail another.</p>
<p>This module builds one habit that the rest of the course depends on. Before you act on any instruction, find out who issued it, whom it covers, and when it took effect. Most records mistakes in dialysis units are not careless. They come from careful people following the wrong version of the right rule.</p>
{{cards:Key terms for this module|Medical records officer (MRO)::The person designated in writing to keep the unit&rsquo;s records and run its records workflows.|Designation::The written act that names a person to a role. Being told verbally is not a designation.|Issuance::A formally numbered order, circular, or advisory from a government agency, such as a DOH administrative order or a PhilHealth circular.|Standard operating procedure (SOP)::The facility&rsquo;s own written steps that turn the rules into local work, with forms, owners, and logs.|Personal information controller (PIC)::The organization that decides how personal data are used. It owns breach-notification decisions.|Data protection officer (DPO)::The person the controller designates to oversee privacy compliance and advise on incidents.}}
""",
    "case": {"title": "The binder before the inspection", "html": """
<p>You started on Monday as the medical records officer of a 22-station freestanding hemodialysis (HD) unit in Bulacan. On Wednesday, Ms. Teresita Aquino, the unit manager, places a thin blue binder on your desk. The label says &ldquo;MRO.&rdquo; Inside are a two-year-old memo naming your predecessor, Mr. Ramil Dizon, and a printout of a PhilHealth circular from 2022 with coffee rings on it. The DOH licensing visit is in three weeks.</p>
<p>&ldquo;Are we covered?&rdquo; she asks.</p>
<p>That evening, a friend who keeps records at a 16-station unit in Valenzuela messages you: &ldquo;Relax. We never designated anyone. The rule only applies above 20 stations.&rdquo;</p>
""", "questions": ["What belongs in your role file, and what is missing from this one?",
                  "Is your friend right about the 20-station threshold?",
                  "Who signs off on a coding query, a claim, a privacy incident, and a destruction request in your unit, and who covers for each when they are away?"]},
    "sections": [
        ("owns", "What the MRO owns", "Custody, not content", """
<p>Start with the line that every other module depends on. The medical records officer (MRO) keeps the record. The MRO does not author what is in it.</p>
<p>Keeping the record is a large job. You capture and file documents, index them to the right patient and session, retrieve them when asked, track what is missing, validate coded fields within the authority delegated to you, coordinate registry returns, release copies through the approved process, and keep the evidence an inspector will ask to see. You also notice when something looks wrong and send it to the person who can fix it.</p>
<p>Authoring is different. A nurse who wrote a pre-dialysis weight is the author of that weight. A physician who wrote &ldquo;chronic kidney disease stage 5&rdquo; is the author of that diagnosis. Only they, through the clinical correction workflow, may change it, even when the right value seems obvious from another page. The facility head authorizes what leaves the building: claims, releases, system access, and destruction.</p>
<div class="table-wrap"><table>
<thead><tr><th>You own</th><th>You route to someone else</th></tr></thead>
<tbody>
<tr><td>Filing a run sheet to the right patient and session</td><td>What the run sheet says</td></tr>
<tr><td>Noticing that the final weight box is blank</td><td>Filling in the final weight</td></tr>
<tr><td>Checking that a code matches the signed diagnosis</td><td>Choosing a diagnosis the physician did not write</td></tr>
<tr><td>Preparing a draft certificate with its sources</td><td>Signing the certificate</td></tr>
<tr><td>Logging a possible privacy breach within the hour</td><td>Deciding whether the NPC must be notified</td></tr>
<tr><td>Listing charts that are eligible for disposal</td><td>Approving their destruction</td></tr>
</tbody></table></div>
<p>The PSN hemodialysis guidelines describe the records officer&rsquo;s duties as coding, custody, registry coordination, completeness for the DOH, and carrying out the records manual. They recommend training in the International Classification of Diseases, 10th Revision (ICD-10), basic records management, and hospital health information management (HIM).[[psn2024]] That is strong professional guidance. It is not law, and the next section explains why that difference matters.</p>
{{key:You keep the record. You never author the clinical facts inside it. When you catch yourself about to &ldquo;just fix&rdquo; a clinical value, stop and route it.}}
{{scene:The obvious weight|<p>Ms. Cristina Lim, two months into the job, notices that Tuesday&rsquo;s run sheet for Mr. Herminio Valdez has no post-dialysis weight. The machine log on the same clipboard shows 58.9 kg. It would take her five seconds to write it in.</p>
<p>She does not. She clips a note to the sheet for the nurse who ran the session, Mr. Jerome Tan, and enters it in the deficiency log. Mr. Tan checks his own notes, finds he weighed the patient after the machine log was printed, and writes 58.6 kg as a dated late entry.</p>
<p class="tc-scene-take">The obvious value was wrong by 300 grams. Only the author knew the right one.</p>}}
"""),
        ("rulebooks", "Four rulebooks", "Read every rule for issuer, scope, and date", """
{{fig:mro01_referees}}
<p>Each referee speaks through its own kind of document. Learn to recognize them on sight.</p>
<div class="table-wrap"><table>
<thead><tr><th>Referee</th><th>What it decides</th><th>How it speaks</th><th>Example</th></tr></thead>
<tbody>
<tr><td>DOH (licensing)</td><td>Whether the unit may operate</td><td>Administrative orders, department circulars, the License to Operate (LTO) assessment tool</td><td>Administrative Order 2012-0001 and the hemodialysis clinic assessment tool[[doh2012]][[dch_doh_rao_tool]]</td></tr>
<tr><td>PhilHealth (payment)</td><td>Whether, and how much, a session is paid</td><td>Circulars, advisories, and their annexes</td><td>Circular 2024-0023 on the 156-session hemodialysis package[[dch_philhealth2024]]</td></tr>
<tr><td>PSN (professional)</td><td>What good practice looks like</td><td>Clinical practice guidelines and position statements</td><td>March 2024 hemodialysis guidelines[[psn2024]]</td></tr>
<tr><td>NPC (privacy)</td><td>Whether personal data were handled lawfully</td><td>The Data Privacy Act, its implementing rules, circulars, and advisory opinions</td><td>Republic Act 10173 and NPC Circular 16-03 on breach management[[dch_ra10173]][[dch_npc1603]]</td></tr>
</tbody></table></div>
<p>A DOH requirement can cost the unit its license. A PhilHealth requirement can cost it a payment. A PSN recommendation shapes what an inspector or a court will consider reasonable, but it does not by itself close a unit. An NPC requirement can bring a complaint, an order, or a fine. Knowing which referee wrote a rule tells you how much is at stake and whom to ask when it is unclear.</p>
<h3>Three questions before you act</h3>
<p>Read every instruction for three things.</p>
<ul>
<li><strong>Issuer.</strong> Who wrote it? A memo from the head office, a PhilHealth advisory, and a post in a records officers&rsquo; group chat are not equal.</li>
<li><strong>Scope.</strong> Whom does it cover? Some rules apply to hospital-based units, some to freestanding units, some only to public entities, and some to everyone.</li>
<li><strong>Effective date.</strong> Which version governs the date in question? This is the one most often missed.</li>
</ul>
<p>Here is why the date matters. PhilHealth changed the hemodialysis rate twice in 2024. A session on September 30, 2024 and a session on October 9, 2024 fall under different rates, even if both claims are filed on the same afternoon.[[mro_ph2025news]] The governing version is the one in force on the <em>service date</em>, not the filing date. A records officer who keeps only the newest circular cannot answer a question about last year&rsquo;s claim.</p>
<h3>When the rules disagree</h3>
<p>The facility&rsquo;s standard operating procedure (SOP) translates the four rulebooks into local steps. SOPs age. When an SOP and a newer issuance disagree, the issuance wins. Do not quietly follow either one. Log the gap, tell your supervisor, and raise it for revision, so that everyone in the unit follows the same version.</p>
<p>Keep a <strong>source register</strong>: one row per rule, with its issuer, number, title, scope, effective date, the SOP that carries it out, its owner, and the date you will next check whether it has changed. It is a plain table, and it is the single most useful document you will build this year.</p>
{{key:Before you act on any rule, say its issuer, scope, and effective date out loud. If you cannot, you are not ready to act on it.}}
{{scene:Two rates, one afternoon|<p>In March 2025 a PhilHealth reviewer returns two claims from the same patient. One session was on September 30, 2024; the other on October 9, 2024. The clerk had billed both at the new rate because both were filed in October.</p>
<p>The records officer opens the source register, finds the rate change recorded with its effective date of October 9, 2024, and shows the clerk that the September session falls under the earlier rate. The corrected claim goes back the same week.</p>
<p class="tc-scene-take">The service date decides which rule applies. A register with effective dates turns a dispute into a lookup.</p>}}
"""),
        ("rolefile", "The role file", "What an inspector expects to see", """
<p>The DOH assessment tool for hemodialysis clinics, as posted, lists three items about the records officer: a designated MRO, a notarized employment contract that reflects MRO duties, and a medical-records-management training certificate for facilities with more than 20 stations.[[dch_doh_rao_tool]]</p>
<p>Read that last line slowly, because it is often misread. The 20-station threshold attaches to the <em>training certificate</em>. It does not attach to the designation. A 16-station unit still needs a designated records officer. It may not need the specific certificate. Assessment tools are revised, and regional offices differ on which training providers they accept, so confirm the current tool and the accepted providers with your Center for Health Development licensing office, and write down who told you and when.</p>
{{flow:A complete role file|Designation memo::Signed by the facility head, current, naming you and your deputy.|Contract::Notarized, with your records duties written into it.|Training evidence::The records-management certificate where required, plus ICD-10 and health information management training as PSN recommends.|Records manual::Approved, signed, with its revision date.|Source register::Each rule with issuer, scope, effective date, owner, and next review.|Decision map::Who decides coding, claims, privacy, and destruction, each with an alternate.}}
<p>Why a deputy? Because records work does not stop when you are on leave, sick, or at a seminar. If no one else is authorized to release a transfer packet, a patient may arrive at the receiving unit without orders. The deputy needs the same training, the same access, and a copy of the same decision map.</p>
<p>A role file is not a one-time project. Check it at least yearly and whenever you, your deputy, the facility head, or a governing issuance changes. An inspector who finds a memo naming someone who left two years ago will reasonably ask what else has not been updated.</p>
{{scene:The 16-station unit|<p>A 16-station unit in Pampanga prepares for its licensing visit. The owner has read online that records requirements &ldquo;start at 20 stations&rdquo; and has never designated anyone.</p>
<p>The new administrator reads the assessment tool line by line, sees that the 20-station threshold sits on the training certificate, and asks the facility head to sign a designation naming the senior clerk and a deputy the following Monday. She calls the regional office to ask whether the certificate applies to them, and files the answer with the name of the person she spoke to.</p>
<p class="tc-scene-take">A threshold attached to one item is easy to stretch over the whole list. Read which line it belongs to.</p>}}
"""),
        ("routing", "Who decides", "Log, preserve, and route", """
<p>Every records decision belongs to someone. Your job is to know who, and to route the question to them quickly, with the facts, without deciding it yourself.</p>
<div class="table-wrap"><table>
<thead><tr><th>Decision</th><th>Owner</th><th>What you do</th></tr></thead>
<tbody>
<tr><td>A clinical fact, diagnosis, or correction</td><td>The treating clinician; escalate to the Dialysis Clinical Head</td><td>Log the question, route it, check that it was answered</td></tr>
<tr><td>Indexing and deficiency tracking</td><td>You</td><td>Do it, and keep the trail</td></tr>
<tr><td>Code selection</td><td>The authorized coder or claims lead, with the physician answering diagnostic questions</td><td>Validate against the signed note; send queries</td></tr>
<tr><td>Claims submission</td><td>Authorized claims staff and the facility signatory</td><td>Make the packet complete and traceable</td></tr>
<tr><td>Whether a breach is notified to the NPC</td><td>The personal information controller (PIC), advised by the data protection officer (DPO)[[dch_npc1603]]</td><td>Report within the hour and preserve the evidence</td></tr>
<tr><td>Destruction of records</td><td>The facility head and counsel; for public entities, the National Archives process[[mro_ra9470]]</td><td>Prepare the list and the disposition record</td></tr>
</tbody></table></div>
<p>Each row needs a named person and a named alternate. &ldquo;The doctor&rdquo; is not a name. &ldquo;Dr. Mendoza, or Dr. Bautista when she is away&rdquo; is.</p>
<h3>How fast to escalate</h3>
<p>Not every gap is urgent, but some are urgent in a way that a records office does not usually see. Sort every problem you find by what it could affect.</p>
<div class="table-wrap"><table>
<thead><tr><th>If the problem could affect&hellip;</th><th>Escalate to</th><th>How soon</th></tr></thead>
<tbody>
<tr><td>The next treatment (an expired order, a document filed to the wrong patient, a dialyzer that cannot be traced)</td><td>The charge nurse and the clinical team</td><td>Before that session starts</td></tr>
<tr><td>A person&rsquo;s privacy (a misdirected email, a lost logbook, odd access in the audit trail)</td><td>The DPO</td><td>Within the hour of discovery</td></tr>
<tr><td>A payment (a missing form, a duplicate claim)</td><td>The claims lead</td><td>Before the batch is sent</td></tr>
<tr><td>Everything else</td><td>The owner, through the deficiency log</td><td>By the due date you set</td></tr>
</tbody></table></div>
{{call:When a records problem could affect the next treatment, escalate to the clinical team before that session. When it could affect a person&rsquo;s privacy, escalate to the DPO within the hour of discovery. Local protocol sets the exact times, but when you are unsure, ask the attending nephrologist about clinical risk and the DPO about privacy. Asking early is never the mistake.}}
{{scene:Friday at 4:45 p.m.|<p>At 4:45 p.m. on a Friday, the records officer finds three problems in one stack: a laboratory page in the wrong chart for a patient who dialyzes Saturday at 6 a.m., a claim missing its Annex A, and an email to the wrong address from Thursday.</p>
<p>She sorts them by what they could affect. The misfiled page goes to the charge nurse before she leaves, because Saturday&rsquo;s session is first. The email goes to the data protection officer the same hour. The claim waits for Monday, logged with an owner.</p>
<p class="tc-scene-take">Three problems, three clocks. The order comes from what each one could harm, not from which one is easiest.</p>}}
{{fig:mro01_fig_01_decision_owners_escalation_clock}}
"""),
        ("week", "Your first week", "A first-week plan", """
<p>A new records officer usually inherits a mix of good systems and loose ends. Use the first week to find out which is which before you change anything.</p>
<div class="table-wrap"><table>
<thead><tr><th>Day</th><th>What to do</th><th>What you will learn</th></tr></thead>
<tbody>
<tr><td>1</td><td>Read the records manual and the role file. Note every date.</td><td>How old the paperwork is</td></tr>
<tr><td>2</td><td>Walk one patient&rsquo;s session from schedule to run sheet to claim to registry.</td><td>Where documents actually travel</td></tr>
<tr><td>3</td><td>Start the source register with the four referees&rsquo; current issuances.</td><td>Which rules the unit is really following</td></tr>
<tr><td>4</td><td>Meet the charge nurse, claims lead, DPO, and IT contact. Agree how each wants to be reached.</td><td>Who to call, and how fast they answer</td></tr>
<tr><td>5</td><td>Draft the decision map and give it to the unit manager for sign-off.</td><td>Where ownership is unclear</td></tr>
</tbody></table></div>
<p>Do not reorganize the records room in week one. A records officer who moves everything before learning where staff expect to find it can cause a missed order on the first busy Monday.</p>
"""),
    ],
    "debrief": ["""
<p><strong>What belongs in the role file?</strong> A current designation memo naming you and a deputy, signed by the facility head. Your notarized contract with records duties written in. The records-management training certificate, which your unit needs because it has more than 20 stations, plus ICD-10 and health information management training evidence. The approved records manual with its revision date. A current source register and a signed decision map. Mr. Dizon&rsquo;s memo stays in the file as history; it no longer designates anyone. The 2022 circular is replaced by the current one, recorded with its effective date.</p>
<p><strong>Is your friend right?</strong> No. The 20-station threshold applies to the training certificate, not to the designation. Her unit still needs a designated records officer. Tell her kindly, and suggest she confirm the current assessment tool with her regional licensing office.</p>
<p><strong>Who signs off?</strong> A coding query goes to the authorized coder or claims lead, with the physician answering the diagnostic question. A claim goes to the claims staff and the facility signatory. A privacy incident goes to the DPO within the hour, and the controller decides on notification. A destruction request goes to the facility head and counsel. Each of the four needs a named alternate, written into the decision map.</p>
<p><strong>And Ms. Aquino&rsquo;s question?</strong> &ldquo;Not yet, but we will be in a week.&rdquo; Give her the list of what is missing, who owns each item, and the date each will be done.</p>
<p>The licensing visit is three weeks away, but the habit you build this week matters for longer. A records officer who can name the issuer, scope, and date of every rule they follow is the person the whole unit learns to trust.</p>
"""],
    "skills": {"title": "Role file and decision map",
               "intro": "Assemble a role file and source register for a fictional unit while your preceptor observes.",
               "items": [
                   ("States the issuer, scope, and effective date for each rule in the register.", True),
                   ("Explains which rules come from licensing, payment, professional guidance, and privacy law.", False),
                   ("Distinguishes the designation requirement from the training-certificate threshold.", True),
                   ("Produces a complete role file: designation, contract, training, manual, and deputy.", False),
                   ("Names an owner and an alternate for coding, claims, privacy, and destruction decisions.", True),
                   ("Sorts three sample problems by urgency: next treatment, privacy, payment, or routine.", True),
                   ("Flags an SOP that conflicts with a newer issuance and routes it for revision.", False),
               ],
               "placement": "Find your own unit&rsquo;s role file and source register. List every rule that has no recorded effective date, and every decision that has no named alternate."},
    "terms": [("MRO", "Medical records officer."), ("Designation", "A written act naming a person to a role."),
              ("Issuance", "A formally numbered order, circular, or advisory."), ("SOP", "Standard operating procedure."),
              ("PIC", "Personal information controller."), ("DPO", "Data protection officer."),
              ("LTO", "License to Operate, issued by the DOH."),
              ("Source register", "A table of every rule the unit follows, with issuer, scope, effective date, owner, and next review.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["01"])
