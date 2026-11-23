# -*- coding: utf-8 -*-
"""Dialysis Clinical Head, Module 11: Money, Procurement, and Conflicts of Interest. Written for this series from published sources."""

MODULE = {
    "image_alt": "A physician reviewing a supply forecast with an operations manager in a dialysis stockroom, boxes of dialyzers on the shelves.",
    "objectives": [
        "Read the finances that affect safety: volume, collections, fixed and variable costs, and commitments.",
        "Calculate the runway of a critical supply and decide early when a shortage becomes a clinical decision.",
        "Compare the full cost of options, including cancellations, transfers, and harm, not only purchase price.",
        "Qualify a substitute product through its regulatory, technical, clinical, training, and traceability gates.",
        "Disclose and recuse when you, or the people deciding, have a tie to a vendor.",
        "Stabilize coverage first, then mediate, when two clinicians dispute patients or services.",
    ],
    "big": """
{{plain:A shortage is a runway. You know how many days of stock you have, and you know when the next verified delivery lands. The distance between them is the time you have to choose.}}
{{fig:dch11_runway}}
<p>The picture has a limit. A runway has a fixed length, but stock does not: a change in demand, a damaged box, or a recall can shorten it overnight. Check the runway every day once it is short, and decide early, while you still have options.</p>
{{cards:Key terms for this module|Fixed cost::A cost that does not change with the number of sessions, such as rent or salaries.|Variable cost::A cost that rises with each session, such as dialyzers and lines.|Collections::Cash actually received, which may lag behind claims submitted.|Qualification::The checks a new product passes before it is used on patients.|Conflict of interest::A financial or personal tie that could influence, or appear to influence, a decision.|Recusal::Stepping back from a decision in which you have a conflict.}}
""",
    "case": {"title": "Three days of stock", "html": """
<p>PhilHealth collections at your Bulacan unit are six weeks behind. The stockroom forecasts that the unit&rsquo;s current dialyzer model will run out in three days. The usual supplier can deliver in five days, at 120 pesos more per unit than last quarter, enough for 80 treatments.</p>
<p>Mr. Jerome Uy, a supplier and the owner&rsquo;s nephew, offers delivery tomorrow of a dialyzer model the unit has never used, at the old price. &ldquo;It is the same thing,&rdquo; he says. &ldquo;Just a different brand.&rdquo;</p>
""", "questions": ["What evidence would make the substitute usable, and who signs each part?",
                  "What do you do if that evidence arrives after the current stock runs out?",
                  "How do you handle the family tie?"]},
    "sections": [
        ("money", "Reading the money", "The finances that touch safety", """
<p>You do not run the books, but you need to read them well enough to see when money is about to become a safety problem. Ask finance for treatment volume, collections timing, operating expenses, upcoming contractual commitments, and the cost of downtime. Separate a fall in demand from a delay in collections; they need different responses.</p>
<p>Some costs are the price of operating at all. A second carbon tank, a validated relief nurse, or a water culture are not savings opportunities. When the owner proposes a cut, ask which control it removes and show the consequence in plain terms.</p>
{{call:Stop and escalate in writing any proposed cost cut that removes a safety control. State the control, the risk it covers, and the alternative savings you would accept.}}
"""),
        ("cost", "Comparing options", "The full cost of a shortage", """
<p>Compare options on their full cost. The incremental cost of the verified product is the price difference times the units needed. The cost of not having it includes canceled or transferred sessions, transport, staff time, and the clinical risk of a longer gap between treatments.</p>
<div class="table-wrap"><table>
<thead><tr><th>Option</th><th>Direct cost</th><th>Hidden cost</th></tr></thead>
<tbody>
<tr><td>Pay more for the verified product</td><td>120 pesos &times; 80 = 9,600 pesos</td><td>Two days of gap if the delivery lands on day 5 and stock ends on day 3</td></tr>
<tr><td>Transfer sessions during the gap</td><td>Partner unit fees, transport</td><td>Patient travel, missed sessions, disruption</td></tr>
<tr><td>Use the unfamiliar substitute</td><td>Lower price</td><td>Qualification time, training, unknown performance, recall traceability</td></tr>
<tr><td>Ask for partial early delivery or borrow from a partner unit</td><td>Negotiation, freight</td><td>Depends on partner&rsquo;s stock</td></tr>
</tbody></table></div>
{{formula:<strong>Runway.</strong> Stock lasts 3 days; verified delivery lands on day 5. Gap = 2 days. With 30 treatments a day, about 60 treatments fall in the gap. Calculator 7 compares the incremental cost with the cost of canceling or transferring them.}}
<p>Use ranges when assumptions are uncertain. A brief that says &ldquo;between 40 and 60 sessions, depending on whether the courier delivers on day 4 or day 5&rdquo; is more honest, and more useful, than a single number.</p>
"""),
        ("qualify", "Qualifying a substitute", "Paying for it does not make it safe", """
{{fig:dch11_qualify}}
{{flow:Gates for a substitute|1. Regulatory::Registered for sale in the Philippines for this use.|2. Technical::Compatible with your machines, lines, and reprocessing method if you reuse.|3. Clinical::Membrane, surface area, and clearance reviewed against your patients&rsquo; prescriptions by a physician.|4. Training::Staff shown any differences in priming, handling, or alarms.|5. Traceability::Lot numbers recorded so a recall can find every patient.}}
<p>Each gate has its own owner: compliance, the technical lead, the clinical head or a designated nephrologist, the head nurse, and the stockroom. An owner who approves payment has not approved suitability.</p>
"""),
        ("coi", "Conflicts", "Disclose, then step back", """
{{fig:dch11_coi}}
<p>A family tie to a vendor is not a scandal. Hiding it is. Before any evaluation, the person with the tie discloses it in writing and steps back from the decision, following your facility&rsquo;s purchasing and recusal process. Compliance should review inducements, bundled charges, and anything that looks like a payment for referrals.</p>
<p>The same discipline applies to clinicians. When two nephrologists dispute referrals, coverage, or use of a service, first make sure no patient is left without a physician. Then document the competing interests, ask a neutral medical staff leader or governance designee to mediate under your bylaws, and recuse anyone with a material conflict. Agree who tells patients, who resolves open orders, and who fixes any process defect the dispute exposed. Credentialing or conduct issues go through the authorized medical staff pathway.</p>
{{key:Patients should never feel a dispute between the people responsible for them.}}
"""),
    ],
    "debrief": ["""
<p><strong>What would make the substitute usable?</strong> Evidence that it passes each gate: registration for this use, technical compatibility confirmed by the technical lead, clinical review of its specifications against your patients&rsquo; prescriptions, staff training, and lot traceability. That cannot happen by tomorrow without cutting corners.</p>
<p><strong>If the evidence arrives late.</strong> Restrict operations to verified supply. Ask the attending nephrologists to prioritize the roughly 60 treatments that fall in the two-day gap, try for partial early delivery or a loan from a partner unit, and transfer sessions where needed with confirmed acceptance. Present the owner with the incremental 9,600 pesos against the cost of transfers and the clinical risk of gaps. On these numbers, paying for verified stock is likely the cheaper option.</p>
<p><strong>The family tie.</strong> The owner discloses the relationship in writing and steps back from the decision. The substitute is evaluated through the usual gates by people without the tie, and compliance reviews the offer. If it qualifies later, it can be considered on its merits for the next order.</p>
"""],
    "skills": {"title": "Resource decision and conflict of interest",
               "intro": "Prepare and present a supply decision to a mock board, including a disclosed conflict.",
               "items": [
                   ("Calculates the runway and the number of treatments in the gap.", False),
                   ("Compares full costs, including cancellations, transfers, and clinical risk.", False),
                   ("Uses ranges where assumptions are uncertain.", False),
                   ("Prevents use of an unqualified supply.", True),
                   ("Names the owner of each qualification gate.", False),
                   ("Requires written disclosure and recusal before vendor evaluation.", True),
                   ("Escalates a cost cut that removes a safety control, in writing.", True),
                   ("Gives a time-bound fallback plan with physician prioritization.", True),
               ],
               "placement": "List your unit&rsquo;s ten critical supplies with their lead times, approved substitutes, and qualification owners. Fill any gap before the next shortage."},
    "quiz": [
        ("Stock lasts 3 days and the verified delivery lands on day 5. What is the gap?",
         ["1 day", "2 days", "3 days", "5 days"], 1,
         "5 minus 3."),
        ("The verified product costs 120 pesos more per unit for 80 units. What is the incremental cost?",
         ["960 pesos", "9,600 pesos", "96,000 pesos", "12,000 pesos"], 1,
         "120 times 80."),
        ("What belongs in a full cost comparison?",
         ["Purchase price only", "Purchase, qualification, downtime, transfers, patient access, and consequences of delay", "The vendor&rsquo;s discount", "The owner&rsquo;s preference"], 1,
         "Hidden costs often dominate."),
        ("Can an owner authorize a product&rsquo;s clinical suitability by approving payment?",
         ["Yes", "No; clinical and technical suitability need their own reviews", "Yes in emergencies", "Only for dialyzers"], 1,
         "Each gate has its own owner."),
        ("Which is a qualification gate for a substitute dialyzer?",
         ["Color of the box", "Technical compatibility with your machines and reprocessing", "Vendor&rsquo;s reputation", "Price"], 1,
         "Also registration, clinical review, training, traceability."),
        ("A vendor is the owner&rsquo;s nephew. What should happen?",
         ["Exclude the vendor forever", "Written disclosure, recusal of the conflicted person, and evaluation by others through the usual gates", "Proceed quickly", "Hide the tie"], 1,
         "Disclose, then step back."),
        ("The owner proposes removing the second carbon tank to save money. What do you do?",
         ["Agree", "Escalate in writing that it removes a safety control, with the risk and alternatives", "Ignore it", "Ask the vendor"], 1,
         "Some costs are the price of operating at all."),
        ("If a qualified product is unavailable in time, what is the fallback?",
         ["Use the unqualified one", "Restrict to verified capacity, prioritize clinically, and arrange confirmed transfers", "Cancel everyone", "Reuse beyond limits"], 1,
         "Time-bound and physician-led."),
        ("Why use ranges in a budget brief?",
         ["To look uncertain", "To show honestly how results depend on uncertain assumptions", "Because boards prefer them", "They are required"], 1,
         "Ranges are more useful than false precision."),
        ("What is the first step when two nephrologists dispute coverage?",
         ["Choose a winner", "Make sure every patient has a covering physician", "Report both", "Wait"], 1,
         "Stabilize coverage, then mediate."),
        ("Who should mediate the dispute?",
         ["The owner", "A neutral medical staff leader or governance designee under the bylaws", "A patient", "The vendor"], 1,
         "Recuse anyone with a material conflict."),
        ("Collections are late but demand is stable. Why separate the two?",
         ["They need different responses", "They are the same", "To blame PhilHealth", "To delay payments"], 0,
         "Cash timing and demand are different problems."),
        ("What should compliance review in a vendor offer?",
         ["Font size", "Inducements, bundled charges, and payments that could look like referral incentives", "The delivery truck", "Nothing"], 1,
         "Look for incentives that distort care."),
        ("Why record lot numbers for dialyzers?",
         ["For inventory only", "So a recall can find every patient exposed", "For PhilHealth", "For marketing"], 1,
         "Traceability is a safety gate."),
        ("What is a variable cost?",
         ["Rent", "A cost that rises with each session, such as dialyzers", "Salaries", "Insurance"], 1,
         "Fixed costs do not change with volume."),
    ],
    "terms": [("Fixed cost", "A cost that does not change with the number of sessions."),
              ("Variable cost", "A cost that rises with each session."),
              ("Collections", "Cash actually received."),
              ("Runway", "Days of stock left before the next verified delivery."),
              ("Qualification", "The checks a new product passes before use."),
              ("Conflict of interest", "A tie that could influence, or appear to influence, a decision."),
              ("Recusal", "Stepping back from a decision because of a conflict.")],
    "readings": [("dialyzer-reprocessing-reuse.html", "How dialyzer reprocessing affects supply, cost, and safety.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html"],
}


import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("dch_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
