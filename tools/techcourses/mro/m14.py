# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 14: Transfers, Transient Dialysis, and International Practice. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer checking a transfer packet against its manifest before sealing it.",
    "objectives": [
        "Assemble a transfer packet against a manifest, with the clinical scope set by the clinical team.",
        "Verify the receiving facility and its channel through a trusted directory, not the request itself.",
        "Escalate a missing clinical item before dispatch and track it to delivery.",
        "Close a transfer on acknowledgment and update the chart, registry, claims ledger, and retention trigger.",
        "Use international practice as a source of ideas without mistaking it for Philippine law.",
    ],
    "big": """
{{plain:A transfer is a relay race. Your runner has carried the baton for years. Now another team&rsquo;s runner is waiting, and the baton must pass from hand to hand without touching the ground. Most dropped batons are dropped in the handoff, not on the track.}}
<p>The picture is useful, and it has one limit. In a relay, the next runner sees the baton coming. A receiving dialysis unit sees only what you send. If a page is missing, nothing tells them it should have been there. They will dialyze the patient, often within a day or two, on the strength of the packet, and fill any gap with assumptions.</p>
<p>For a patient with chronic kidney disease (CKD) who depends on dialysis, a missing dry weight or an outdated hepatitis result is not an administrative gap at that point. It is a clinical risk: a fluid target guessed, or a patient placed on the wrong machine. This module is about making the handoff complete, verified, and confirmed.</p>
{{cards:Key terms for this module|Manifest::The itemized list of what a packet contains.|Acknowledgment of receipt::The recipient&rsquo;s confirmation that the packet arrived, complete.|Transient dialysis::Treatment at another unit while the patient is traveling.|Transfer-out::The event that ends a patient&rsquo;s care at your unit and begins it elsewhere.|Local standard::A practice the facility adopts by its own policy, clearly labeled as not a legal requirement.}}
""",
    "case": {"title": "Before tomorrow&rsquo;s session", "html": """
<p>Mr. Eduardo Reyes, 70, is moving to live with his daughter in Laguna. A hospital-based unit there has accepted him and plans to dialyze him tomorrow morning. At 3:30 p.m. an email arrives asking for his current signed hemodialysis (HD) orders, his last treatment record, and his medication list &ldquo;before tomorrow&rsquo;s session.&rdquo;</p>
<p>The email comes from an address you do not recognize: a free webmail account with the hospital&rsquo;s name in it. Dr. Mendoza has already authorized the transfer packet. When you pull the chart, you see that his last run sheet, from this morning, still has no final weight.</p>
""", "questions": ["How do you confirm where to send the packet?",
                  "What do you do about the missing final weight?",
                  "When is the transfer closed, and what else must you update?"]},
    "sections": [
        ("packet", "The packet", "Build it, verify it, send it", """
<p>The clinical team decides what is clinically required and signs the treatment summary. A typical packet holds:</p>
<ul>
<li>the current signed standing orders;</li>
<li>the last several run sheets;</li>
<li>the dry weight and recent weight trend;</li>
<li>vascular access details, including the access type, site, and any recent problems;</li>
<li>the current medication list and allergies;</li>
<li>the latest hepatitis serologies, each with its collection date;</li>
<li>recent laboratory results;</li>
<li>isolation status.</li>
</ul>
<p>The records officer checks the packet against its manifest: identity on every page, legibility, completeness, the approved scope, and the documented basis for disclosure (Module 8). Write the manifest before you assemble the packet, not after. A manifest written from what is in the envelope cannot show what is missing from it.</p>
<h3>Verify the destination</h3>
<p>Confirm the receiving facility and its secure channel through a trusted directory or the facility&rsquo;s switchboard, not the contact details in the request. A request that arrives from an unfamiliar address may be genuine; busy units do use personal accounts. It may also be mistyped, or not genuine at all. In either case, a hepatitis result sent to the wrong address is a breach (Module 8). Send only through the approved channel.</p>
{{fig:mro14_transfer}}
{{scene:The packet that went to the wrong Laguna|<p>A transfer request names &ldquo;Laguna Medical Center.&rdquo; The clerk searches online and finds two hospitals with similar names in two different towns.</p>
<p>The records officer calls the patient&rsquo;s daughter, confirms the town, finds the hospital&rsquo;s switchboard in the unit directory, and confirms the receiving nurse and secure email. The packet goes to the right hospital the first time.</p>
<p class="tc-scene-take">A name is not an address. Verify the receiver before you send.</p>}}
"""),
        ("close", "Closing", "Close on receipt, then update four places", """
<p>Record what was sent, when, by whom, and through which channel. Obtain the receiver&rsquo;s acknowledgment. List any item still to follow, with its owner and a due time. An urgent gap, one the receiving team needs for the first session, goes to your clinical team immediately, before dispatch.</p>
{{flow:Downstream updates|Chart::Transfer-out event, date, and destination.|Registry::Transfer-out per the receiver&rsquo;s definitions (Module 7).|Claims ledger::Stop local claims after the last local session; the patient&rsquo;s annual 156-session count travels with the patient, not the unit.|Retention::The last local treatment becomes the retention trigger (Module 10).}}
<p>The ledger point is worth telling the receiving unit. If Mr. Reyes has used 140 of his 156 Philippine Health Insurance Corporation (PhilHealth) sessions this year, the new unit needs to know that coverage runs out in about five weeks, not next November.</p>
<p>For transient dialysis, the same logic applies over a shorter horizon. The receiving unit&rsquo;s checklist usually sets the scope, and the physician-signed certification follows Module 9. When the patient returns, ask for the treatment records from the transient unit and file them, because those sessions are part of the patient&rsquo;s history and may count toward the annual cap.</p>
{{key:Dispatch is not delivery. A transfer closes on confirmed receipt.}}
{{scene:Received, but not the hepatitis result|<p>The receiving unit acknowledges a transfer packet for Mr. Alfredo Tolentino. Checking the acknowledgment against the manifest, the records officer sees that they list every item except the hepatitis serology.</p>
<p>She calls. The page had printed blank on their side. She resends it, gets a second acknowledgment naming it, and closes the transfer. Their first session for him was the next morning.</p>
<p class="tc-scene-take">An acknowledgment is only as good as its match to the manifest.</p>}}
{{fig:mro14_fig_14_transfer_close_four_updates}}
"""),
        ("abroad", "Abroad", "What other countries do, and how to use it", """
<p>Other countries have thought hard about records custody, and their practices are worth knowing. They are also easy to misuse.</p>
<div class="table-wrap"><table>
<thead><tr><th>Jurisdiction</th><th>Practice worth knowing</th></tr></thead>
<tbody>
<tr><td>United States</td><td>The federal dialysis rule requires one record available to the whole team, including advance-directive status; retention six years from discharge; requested records sent to a receiving facility within one working day of transfer.[[dch_cfr494]]</td></tr>
<tr><td>England</td><td>The National Health Service (NHS) records code calls for a named records lead and executive accountability.[[mro_nhs_code]]</td></tr>
<tr><td>Australia</td><td>A New South Wales (NSW) Health directive covers capture, amendment, access, and incident escalation.[[mro_nsw2025]]</td></tr>
<tr><td>Canada</td><td>The national organ replacement register uses secure batch submission with validation and acknowledgment.[[mro_cihi_corr]]</td></tr>
<tr><td>Singapore</td><td>The renal registry operates under national registry legislation with defined events.[[mro_nrdo]]</td></tr>
</tbody></table></div>
<p>A Philippine unit may adopt a process control from abroad, such as a one-working-day internal target for sending transfer records, through its own approved policy, labeled clearly as a local standard. It never becomes a legal deadline by being copied. And no foreign rule can shorten a Philippine one: the United States six-year retention rule does not let a Philippine unit discard an outpatient chart before the Department of Health&rsquo;s seven years.</p>
{{scene:&ldquo;By law, within one day&rdquo;|<p>A receiving unit&rsquo;s nurse insists that records &ldquo;must by law&rdquo; arrive within one working day, citing a document she read online.</p>
<p>The records officer recognizes the United States federal dialysis rule. She sends the packet that afternoon anyway, because the patient dialyzes tomorrow, and mentions politely that the one-day target is good practice her unit follows as a local standard, not a Philippine legal deadline.</p>
<p class="tc-scene-take">A good idea from abroad is worth adopting. It is still not Philippine law.</p>}}
"""),
    ],
    "debrief": ["""
<p><strong>Where to send.</strong> Call the Laguna hospital through its switchboard number from your directory, ask for the dialysis unit, and confirm who is receiving Mr. Reyes and the unit&rsquo;s secure email or portal. Send there, not to the webmail address. If the webmail address turns out to be the right person, the unit can tell you so; you have lost ten minutes, not a hepatitis result.</p>
<p><strong>The final weight.</strong> Alert the charge nurse and the nurse who ran this morning&rsquo;s session now. The receiving unit will plan tomorrow&rsquo;s fluid removal partly from it. Send the authorized items today, and log &ldquo;final weight to follow,&rdquo; with the assigned nurse as owner and a due time this evening. Do not estimate it or copy it from the machine screen yourself.</p>
<p><strong>Closing.</strong> When the receiver acknowledges the packet, and the follow-up item has been sent and acknowledged too. Then update the chart, the registry, the claims ledger, and the retention trigger, and tell the receiving unit how many PhilHealth sessions Mr. Reyes has used this year.</p>
<p>Mr. Reyes will meet a new nurse tomorrow who has never seen him. Part of your role is to make sure everything she needs to know about him is already on her desk.</p>
"""],
    "skills": {"title": "Transfer packet and closure",
               "intro": "Assemble, verify, and close a fictional transfer while your preceptor observes.",
               "items": [
                   ("Writes the manifest before assembling the packet.", False),
                   ("Checks identity, legibility, scope, and authority against the manifest.", False),
                   ("Verifies the recipient and channel through a trusted directory.", True),
                   ("Escalates an urgent missing item to the clinical team before dispatch.", True),
                   ("Closes on acknowledgment and tracks pending items with an owner and due time.", False),
                   ("Updates the chart, registry, claims ledger, and retention trigger.", False),
                   ("Distinguishes a foreign rule or local standard from a Philippine legal requirement.", False),
               ],
               "placement": "Review your unit&rsquo;s last three transfers and check that each has a manifest and an acknowledgment."},
    "terms": [("Manifest", "The itemized list of a packet&rsquo;s contents."), ("Acknowledgment of receipt", "The recipient&rsquo;s confirmation."),
              ("Transient dialysis", "Treatment at another unit while traveling."), ("Transfer-out", "The event ending care at the unit."),
              ("Local standard", "A practice adopted by facility policy, not a legal requirement."),
              ("NHS", "National Health Service (England)."), ("NSW", "New South Wales, Australia.")],
    "readings": [("travel-dialysis-ckd.html", "Planning dialysis while traveling.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["14"])
