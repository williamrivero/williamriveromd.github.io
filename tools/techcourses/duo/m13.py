# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 13: Procurement, supply chains, and conflicts. Written for this course from published sources."""

MODULE = {
    "image_alt": "Sealed dialyzer boxes on a tidy stockroom shelf, one pulled forward with a lot-number barcode, beside a handheld scanner.",
    "objectives": [
        "Qualify a substitute product through registration, technical, clinical, training, and traceability gates.",
        "Manage related-party suppliers through declaration, recusal, and equal criteria.",
        "Calculate stock runway and reorder points, and act early when a shortage becomes a clinical decision.",
        "Trace a recalled lot to every affected patient within an hour.",
    ],
    "big": """
{{plain:Buying for a dialysis unit is like buying parts for an airplane, not for a car. A cheaper part that fits is not good enough; it must be certified for that aircraft, the mechanics must know it, and you must be able to find every plane it went into if it fails.}}
<p>The picture has a limit. An airline can ground a plane. A unit cannot ground a patient, who needs the next session in two days. That is why supply planning in dialysis looks ahead in weeks, and why a shortage becomes a clinical decision early.</p>
{{cards:Key terms for this module|Qualification::The checks a new product passes before use on patients.|Related party::A supplier connected to an owner, leader, or their family.|Runway::Days of stock left before the next verified delivery.|Reorder point::The stock level that triggers an order: daily use &times; lead time + safety stock.|Lot traceability::Recording which lot of a product was used for which patient.}}
<p>Your work is to buy honestly, plan ahead, and be able to find every patient who received a faulty product.</p>
""",
    "case": {"title": "The cheaper dialyzer", "html": """
<p>Collections at a unit in Tarlac City are six weeks behind. The stockroom says the current dialyzer runs out in three days, and the usual supplier can deliver in five. Mr. Jerome Uy, a supplier and the owner&rsquo;s nephew, offers a different brand that is 120 pesos cheaper per unit and can arrive tomorrow. The technical lead has never seen it.</p>
""", "questions": ["What is the gap, in days and treatments?", "What must be true before the new dialyzer is used?", "How is the family tie handled?"]},
    "sections": [
        ("qualify", "Qualifying a product", "A cheaper substitute must pass five gates", """
{{fig:duo13a}}
<p>A dialyzer, bloodline, or concentrate touches a patient&rsquo;s blood. Before any new product is used, it passes five gates: registration with the Food and Drug Administration (FDA) of the Philippines for this use; technical compatibility with your machines, confirmed by the technical lead; clinical review of its specifications against your patients&rsquo; prescriptions by the clinical head; staff training; and lot traceability in your records.</p>
<p>Price is a reason to start qualifying a product, not a reason to skip a gate. A product that arrives tomorrow cannot be qualified by tomorrow without cutting corners.</p>
{{stop:No unqualified product is used on a patient, however short the stock or cheap the offer.}}
{{key:Five gates, every time, for every new product that touches blood.}}
"""),
        ("related", "Related parties", "When the supplier is family", """
<p>Incentives around supplies and drugs can shape practice. In United States data, for-profit facilities gave more of a highly reimbursed drug than nonprofit facilities, an association that shows how purchasing and payment can drive clinical patterns.[[duo_thamer2007]] A related-party supplier adds a personal incentive to a financial one.</p>
<p>Handle it as Module 5 described: the related person declares the tie in writing, steps out of the decision, and the product and price are evaluated by others on the same criteria as any supplier. The board minutes record how the decision was made.</p>
{{key:Family suppliers are allowed. Hidden family suppliers are not.}}
"""),
        ("stock", "Stock runway", "Runway and reorder points", """
<p>Know how many days each critical item will last. Reorder point = average daily use &times; lead time + safety stock. When a supplier warns of a delay, recalculate with the longer lead time the same day.</p>
<p><strong>Worked example (fictional).</strong> The unit uses 20 dialyzers a day. Stock lasts three days; the verified delivery arrives on day five. The gap is two days, about 40 treatments. Paying more for verified stock from the usual supplier, or borrowing from a partner unit, is almost always cheaper than transferring 40 treatments, and it carries no clinical risk from an unqualified product.</p>
<p>If a gap cannot be closed, it becomes a clinical decision: the attending nephrologists decide which patients can safely have a shorter or delayed session and which cannot. The owner&rsquo;s job is to see it coming early enough that this rarely happens.</p>
{{key:Recalculate the reorder point the day a supplier warns of delay.}}
"""),
        ("recall", "Recall", "One-hour recall", """
{{fig:duo13b}}
<p>When a product is recalled, the unit must find every patient who received the affected lot. That is only possible if the lot number was recorded at each session. Test it: once a quarter, pick a lot at random and time how long it takes to list the patients. The aim is under an hour.</p>
{{key:If you cannot find the patients, you cannot protect them. Test your recall trace every quarter.}}
"""),
    ],
    "debrief": ["""
<p><strong>The gap.</strong> Two days, about 40 treatments at 20 a day.</p>
<p><strong>Before use.</strong> The new dialyzer would need FDA registration for this use, technical compatibility, clinical review, staff training, and traceability. That cannot be done safely by tomorrow. Close the gap with verified stock: pay for partial early delivery, borrow from a partner unit, and ask the nephrologists to prioritize only if a gap remains.</p>
<p><strong>The family tie.</strong> The owner declares it, steps out, and the product is evaluated later on equal criteria. It may become a good second supplier, after qualification.</p>
"""],
    "skills": {"title": "Supplier scorecard, conflict declaration, and recall trace",
               "intro": "Build a supplier scorecard, complete a conflict declaration, and run a timed recall trace.",
               "items": [("Lists the five qualification gates and who owns each.", False),
                         ("Prevents use of any unqualified product that touches blood.", True),
                         ("Requires written declaration and recusal for related-party suppliers.", True),
                         ("Calculates runway and the reorder point at the usual and delayed lead time.", False),
                         ("Compares the full cost of options, including transfers and clinical risk.", False),
                         ("Completes a recall trace for one lot and records the time taken.", False)],
               "placement": "Pick one lot number from last month and time how long the unit takes to list every patient who received it."},
    "quiz": [
        ("Stock lasts three days and the verified delivery arrives on day five. What is the gap?",
         ["One day", "Two days", "Three days", "Five days"],
         1, "Five minus three."),
        ("Which is NOT one of the five qualification gates?",
         ["FDA registration for this use", "Technical compatibility", "The lowest price", "Lot traceability"],
         2, "Price is a reason to start qualifying, not a gate."),
        ("The owner&rsquo;s nephew offers a cheaper product. What happens first?",
         ["Accept to help the family", "The owner declares the tie and steps out of the decision", "Reject it automatically", "Use it on half the patients"],
         1, "Declare, recuse, and evaluate on equal criteria."),
        ("What is the reorder point formula?",
         ["Price &times; quantity", "Daily use &times; lead time + safety stock", "Stock &divide; patients", "Lead time &divide; price"],
         1, "Recalculate it when lead time changes."),
        ("Why record the lot number at every session?",
         ["For billing", "So every patient who received a recalled lot can be found quickly", "To lower prices", "PhilHealth requires barcodes"],
         1, "Traceability is a safety system."),
        ("A supply gap cannot be closed. Who decides which patients may have a delayed session?",
         ["The owner", "The attending nephrologists", "The supplier", "The billing officer"],
         1, "Prioritizing treatment is a clinical decision."),
    ],
    "terms": [("Safety stock", "Extra stock kept to cover unexpected use or delay.")],
    "readings": [],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html#c2", "calc-dialysis-clinical-head-toolkit.html#c7"],
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
