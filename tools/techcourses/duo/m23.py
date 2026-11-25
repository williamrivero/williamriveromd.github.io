# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 23: Expansion, acquisition, succession, and responsible exit. Written for this course from published sources."""

MODULE = {
    "image_alt": "Three clinic buildings growing along a road toward a fork where a handshake takes place at a table.",
    "objectives": [
        "Expand only when the original unit is safe and the new one passes the same gates.",
        "Explain what studies observed after acquisitions and private equity ownership, and how strong the evidence is.",
        "Run due diligence that protects patients as well as value.",
        "Plan succession and a closure or sale in which every patient is placed.",
    ],
    "big": """
{{plain:Selling or closing a dialysis unit is not like selling a shop. A shop&rsquo;s customers can walk to the next one. A dialysis unit&rsquo;s patients need a chair every two days, a prescription, and records that follow them. The sale is finished only when every patient is safe somewhere.}}
<p>The picture has a limit. A sale can also be good for patients: a stronger owner can bring better systems and money for repairs. Whether it is good depends on what the buyer does next, and that is what due diligence is for.</p>
{{cards:Key terms for this module|Due diligence::The investigation of a business before buying or selling it.|Acquisition::One organization buying another.|Private equity::Investment funds that buy companies, usually to sell them later at a profit.|Succession::The plan for who leads or owns the unit next.|Responsible exit::Closing or selling with every patient placed and every record safe.}}
<p>Your work is to grow carefully, to ask a buyer the questions that protect patients, and to finish any exit with every patient accounted for.</p>
""",
    "case": {"title": "The offer", "html": """
<p>A regional chain offers to buy a family&rsquo;s two units in Pampanga for a price the family considers generous. The offer letter mentions &ldquo;standardizing staffing models&rdquo; and &ldquo;optimizing drug utilization.&rdquo; The founder, Dr. Ernesto Lacson, is 72 and has no successor in the family who wants to run the units.</p>
""", "questions": ["What do the phrases in the offer letter make you ask?", "What should due diligence cover besides price?", "What must be true before the sale closes?"]},
    "sections": [
        ("growth", "Expansion", "Expand from strength", """
<p>Expand only when the first unit is stable: safe staffing, closed safety actions, healthy cash, and leaders with time to spare. A second site needs its own license, clinical head coverage, staff, water, and the four investment gates from Module 6. Spreading thin leaders across more sites is a common way for a good unit to become a struggling one.</p>
{{key:Every new site passes the same gates as the first.}}
"""),
        ("acquisition", "Acquisitions", "What happens after an acquisition", """
{{fig:duo23a}}
<p>The largest study of dialysis acquisitions followed more than 1,200 independent United States facilities bought by large chains. Afterward, acquired facilities increased doses of highly reimbursed drugs, replaced nurses with less-trained technicians, put fewer patients on the transplant waiting list, and their patients fared worse.[[duo_eliason2020]] Earlier research found large for-profit chain affiliation associated with higher mortality.[[duo_zhang2011]] A systematic review of private equity ownership across health care found it most consistently associated with higher costs, mixed-to-harmful effects on quality, and in some settings lower nurse staffing.[[duo_borsa2023]]</p>
<p>All of this is observational and mostly from the United States, under payment rules unlike PhilHealth&rsquo;s. It does not prove that every acquisition harms patients. It does tell a seller which questions to ask: how will staffing, skill mix, drug use, transplant referral, and safety spending change after the sale?</p>
{{key:Ask the buyer how they will protect staffing, referral, and safety spending, and get the answers in writing.}}
"""),
        ("succession", "Succession", "Succession and due diligence", """
<p>Due diligence runs both ways. A buyer checks licenses, accreditation, claims history, liabilities, and equipment. A seller who cares about patients checks the buyer&rsquo;s staffing models, safety record, how it handles held machines and complaints, and its track record with patients after past purchases. Ask for commitments on staffing, clinical leadership, and referral, and for a transition period.</p>
<p>Succession is not only for sale. Every unit needs a written plan for who decides if the owner dies or becomes unable to act, with powers ready to use. A unit without one can freeze at the worst moment.</p>
{{key:Write the succession plan before you need it.}}
"""),
        ("closure", "Responsible exit", "Closing or selling without losing a patient", """
{{fig:duo23b}}
<p>A closure or a sale that changes services needs a plan with six parts: notify regulators and PhilHealth as required; find receiving units with confirmed slots; make an individual transfer plan for each patient, agreed with the attending nephrologist; transfer records securely; inform and pay staff correctly; and check that every patient is accounted for. Give patients enough notice to prepare, and do not close a unit before its patients have somewhere to go.</p>
{{stop:Do not close or hand over a unit until every patient has a confirmed place to dialyze.}}
{{key:The exit ends when the last patient is placed, not when the contract is signed.}}
"""),
    ],
    "debrief": ["""
<p><strong>The phrases.</strong> &ldquo;Standardizing staffing models&rdquo; and &ldquo;optimizing drug utilization&rdquo; describe exactly the changes the acquisition research observed. Ask what they mean in nurse posts, skill mix, and dosing policy.</p>
<p><strong>Due diligence.</strong> The buyer&rsquo;s staffing ratios, safety record, complaint handling, referral rates, and history with past acquisitions; written commitments on staffing, clinical leadership, and referral; and a transition period.</p>
<p><strong>Before closing.</strong> Regulators and PhilHealth notified, clinical leadership confirmed, every patient&rsquo;s care continuous, records safe, and staff paid correctly. Separately, Dr. Lacson should write a succession plan now, whatever happens to the sale.</p>
"""],
    "skills": {"title": "Due-diligence checklist and succession and closure plan",
               "intro": "Write a seller&rsquo;s due-diligence checklist and a closure continuity plan for a fictional unit.",
               "items": [("Applies the investment gates to a proposed new site.", False),
                         ("Describes the acquisition evidence as observational and names the questions it raises.", False),
                         ("Requires written buyer commitments on staffing, clinical leadership, and referral.", False),
                         ("Writes a succession plan with powers ready to use.", False),
                         ("Refuses to close or hand over a unit before every patient has a confirmed place.", True),
                         ("Transfers records securely and pays staff correctly at exit.", True)],
               "placement": "Find out who would decide for your unit tomorrow if you could not."},
    "quiz": [
        ("What did Eliason and colleagues observe after chain acquisitions?",
         ["More nurses and better outcomes", "More highly reimbursed drugs, fewer nurses, fewer waitlistings, worse outcomes", "No change", "Lower drug use and more transplants"],
         1, "Observational evidence from US Medicare data."),
        ("What did the systematic review of private equity in health care most consistently find?",
         ["Lower costs", "Higher costs to patients or payers", "Better quality everywhere", "No studies"],
         1, "Quality effects were mixed to harmful."),
        ("A buyer promises to &ldquo;standardize staffing models.&rdquo; What should a seller ask?",
         ["Nothing", "What it means for nurse posts and skill mix, in writing", "Only the price", "The color of uniforms"],
         1, "Staffing changes drove outcomes in the research."),
        ("When is a closure finished?",
         ["When the lease ends", "When every patient has a confirmed place and records are safe", "When the sign comes down", "When the owner is paid"],
         1, "Responsible exit is measured by patients placed."),
        ("Why write a succession plan before a sale?",
         ["It is decorative", "So the unit does not freeze if the owner cannot act", "PhilHealth requires it", "To raise prices"],
         1, "Units without succession plans can stall in a crisis."),
        ("Before opening a second site, the owner should:",
         ["Move the best staff from the first", "Confirm the first unit is stable and pass the four gates for the new one", "Skip licensing", "Use the first site&rsquo;s license"],
         1, "Expand from strength, through the same gates."),
    ],
    "terms": [("Transition period", "An agreed period after a sale during which the seller helps ensure continuity.")],
    "readings": [],
    "calcs": [],
}


def _balance(quiz):
    """Spread the keyed answers across A to D, deterministically (same as tools/techcourses/uom/quizutil.py)."""
    out = []
    for i, (stem, opts, ans, why) in enumerate(quiz):
        opts = list(opts)
        target = (i * 3 + 1) % 4
        if target != ans:
            opts[target], opts[ans] = opts[ans], opts[target]
        out.append((stem, opts, target, why))
    return out


MODULE["quiz"] = _balance(MODULE["quiz"])
