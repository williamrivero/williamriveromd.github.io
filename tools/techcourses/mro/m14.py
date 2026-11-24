# -*- coding: utf-8 -*-
"""Medical Records Officer, Module 14: Transfers, Transient Dialysis, and International Practice. Written for this series from published sources."""

MODULE = {
    "image_alt": "A records officer on the phone with a hospital switchboard while checking a transfer packet manifest.",
    "objectives": [
        "Assemble an authorized transfer or transient-dialysis packet against a manifest.",
        "Verify the recipient and the channel independently.",
        "Close a transfer on confirmed receipt, with pending items tracked.",
        "Update the chart, registries, claims ledger, and retention trigger after a transfer.",
        "Borrow good process from other countries without importing their legal deadlines.",
    ],
    "big": """
{{plain:A transfer is the moment the chain of custody must cross from one organization to another without dropping anything.}}
<p>The receiving hemodialysis (HD) unit will dialyze the patient, who lives with chronic kidney disease (CKD),, often within a day or two, on the strength of what you send. A missing dry weight or an outdated hepatitis result is not an administrative gap at that point; it is a clinical risk.</p>
{{cards:Key terms for this module|Manifest::The itemized list of what a packet contains.|Acknowledgment of receipt::The recipient&rsquo;s confirmation that the packet arrived.|Transient dialysis::Treatment at another unit while traveling.|National Health Service (NHS)::National Health Service of England.|New South Wales (NSW)::New South Wales, Australia.}}
""",
    "case": {"title": "Before tomorrow&rsquo;s session", "html": """
<p>A hospital accepting fictional patient SIM-041 asks for current signed HD orders, the last treatment record, and the medication list before tomorrow&rsquo;s session. The email comes from an address you do not recognize. The physician has authorized the packet. The last run sheet still lacks the final weight.</p>
""", "questions": ["How do you confirm where to send the packet?",
                  "What do you do about the missing final weight?",
                  "When is the transfer closed, and what else must you update?"]},
    "sections": [
        ("packet", "The packet", "Build it, verify it, send it", """
<p>The clinical team decides what is clinically required and signs the treatment summary: typically the current signed standing orders, the last several run sheets, dry weight, vascular access details, the current medication list, allergies, the latest serologies with dates, recent laboratory results, and isolation status. The records officer checks identity on every page, legibility, completeness against the manifest, the approved scope, and the documented basis for disclosure.</p>
<p>Confirm the receiving facility and its secure channel through a trusted directory or switchboard, not the contact details in the request, and send only through the approved channel.</p>
{{fig:mro14_transfer}}
"""),
        ("close", "Closing", "Close on receipt, then update four places", """
<p>Record what was sent, when, by whom, and through which channel; obtain the receiver&rsquo;s acknowledgment; and list any item still to follow with its owner and due time. An urgent gap goes to the clinical team immediately.</p>
{{flow:Downstream updates|Chart::Transfer-out event, date, and destination.|Registry::Transfer-out per the receiver&rsquo;s definitions (Module 7).|PhilHealth ledger::Stop local claims after the last local session; the patient&rsquo;s annual 156-session count travels with the patient, not the unit.|Retention::The last local treatment becomes the retention trigger (Module 10).}}
<p>For transient dialysis, the same logic applies over a shorter horizon; the receiving unit&rsquo;s checklist usually sets the scope, and the physician-signed certification follows Module 9.</p>
{{key:Dispatch is not delivery. A transfer closes on confirmed receipt.}}
"""),
        ("abroad", "Abroad", "What other countries do, and how to use it", """
<div class="table-wrap"><table>
<thead><tr><th>Jurisdiction</th><th>Practice worth knowing</th></tr></thead>
<tbody>
<tr><td>United States</td><td>The federal dialysis rule requires one record available to the whole team, including advance-directive status; retention six years from discharge; requested records sent to a receiving facility within one working day of transfer.[[dch_cfr494]]</td></tr>
<tr><td>England</td><td>The National Health Service (NHS) records code calls for a named records lead and executive accountability.[[mro_nhs_code]]</td></tr>
<tr><td>Australia</td><td>A New South Wales (NSW) Health directive covers capture, amendment, access, and incident escalation.[[mro_nsw2025]]</td></tr>
<tr><td>Canada</td><td>The national organ replacement register uses secure batch submission with validation and acknowledgment.[[mro_cihi_corr]]</td></tr>
<tr><td>Singapore</td><td>The renal registry operates under national registry legislation with defined events.[[mro_nrdo]]</td></tr>
</tbody></table></div>
<p>A Philippine unit may adopt a process control, such as a one-working-day internal target for sending transfer records, through its own approved policy, labeled clearly as a local standard. It never becomes a legal deadline by being copied.</p>
"""),
    ],
    "debrief": ["""
<p><strong>Where to send.</strong> Call the hospital through its switchboard number from your directory, confirm the receiving unit and its secure email, and use that, not the unfamiliar address.</p>
<p><strong>The final weight.</strong> Alert the clinical team now. Send the authorized items, and log &ldquo;final weight to follow,&rdquo; with the assigned nurse as owner and a due time today.</p>
<p><strong>Closing.</strong> When the receiver acknowledges the packet and the follow-up item has been sent and acknowledged. Then update the chart, the registry, the claims ledger, and the retention trigger.</p>
"""],
    "skills": {"title": "Transfer packet and closure",
               "intro": "Assemble, verify, and close a fictional transfer with a preceptor.",
               "items": [
                   ("Checks identity, legibility, scope, and authority against a manifest.", False),
                   ("Verifies the recipient and channel through a trusted directory.", True),
                   ("Escalates an urgent missing item to the clinical team before dispatch.", True),
                   ("Closes on acknowledgment and tracks pending items with an owner and due time.", False),
                   ("Updates the chart, registry, claims ledger, and retention trigger.", False),
               ],
               "placement": "Review your unit&rsquo;s last three transfers and check that each has a manifest and an acknowledgment."},
    "terms": [("Manifest", "The itemized list of a packet&rsquo;s contents."), ("Acknowledgment of receipt", "The recipient&rsquo;s confirmation."),
              ("Transient dialysis", "Treatment at another unit while traveling."), ("NHS", "National Health Service (England)."),
              ("NSW", "New South Wales, Australia.")],
    "readings": [("travel-dialysis-ckd.html", "Planning dialysis while traveling.")],
    "calcs": ["calc-medical-records-officer-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
def _ld(n):
    s = _u.spec_from_file_location("mro_" + n, _P(__file__).resolve().parent / (n + ".py")); m = _u.module_from_spec(s); s.loader.exec_module(m); return m
MODULE["quiz"] = _ld("quizutil").balance(_ld("quizbank").QUIZ["14"])
