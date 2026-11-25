# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 24: Integrated owner capstone and the first 90 days. Written for this course."""

MODULE = {
    "image_alt": "A governance meeting around a long table, one person presenting a printed board pack while others take notes.",
    "objectives": [
        "Assemble the module outputs into one board pack that leads to decisions.",
        "Make and record governance decisions under time pressure without crossing a protected line.",
        "Write a first-ninety-days plan for a new or returning owner.",
        "Defend the plan before a panel that includes a clinical reviewer.",
    ],
    "big": """
{{plain:The capstone is a flight simulator. Everything you learned is tested at once, with the weather changing, so that the first real storm is not the first time you have flown through one.}}
<p>The picture has a limit. A simulator cannot make you feel what a family feels after a death, or what a nurse feels when an owner shouts. The panel will ask about those moments too, because good governance is judgment under pressure, not only arithmetic.</p>
{{cards:What the capstone includes|Board pack::One document assembled from all 24 module outputs.|Seventy-two hours of injects::A water failure, a claims shortfall, a typhoon warning, a complaint, and a buyer&rsquo;s call, released in sequence.|Decision log::Every decision, who made it, on what evidence, and what it protected.|First 90 days::A written plan for the owner&rsquo;s next three months.|Panel defense::A 45-minute defense before a panel with a clinical reviewer.}}
<p>The capstone takes about six hours. It is the main evidence that you can apply the course, and an unsafe decision cannot be offset by a high quiz score.</p>
""",
    "case": {"title": "Seventy-two hours", "html": """
<p>You are the new chair of a 16-station unit in Dagupan, Pangasinan. On Monday morning you receive the board pack. At 9:00 the technical lead holds the water loop after a failed endotoxin result. At 11:00 the finance officer reports that 22% of last month&rsquo;s sessions are unpaid and payroll is due Friday. On Tuesday a typhoon signal is raised for Thursday. On Wednesday a family complains that their father was told he might be &ldquo;moved&rdquo; if they kept calling, and a chain calls to ask whether the unit is for sale.</p>
""", "questions": ["What do you decide in the first hour, and who decides the rest?", "What goes in the decision log?", "What will your first ninety days look like?"]},
    "sections": [
        ("board-pack", "The board pack", "Assembling the board pack", """
{{fig:duo24a}}
<p>Put the module outputs into seven tabs: governance and authority (charter, appointments, conflicts), compliance (register and change control), capacity and staffing (safe capacity, FTE, dependencies), water, equipment, and infection, claims and money (reconciliation, unit economics, cash forecast, capital), quality and patient voice (dashboard, complaints, experience), and continuity and risk (dependency map, privacy, insurance, succession). The cover sheet lists the decisions the board must make this month, with the evidence for each.</p>
{{key:The cover sheet is the decisions, not the summary.}}
"""),
        ("decisions", "Deciding under pressure", "Deciding under pressure", """
<p>When several crises arrive at once, sort them with the course&rsquo;s rules. Protected decisions stay with the qualified people: the water stays held until the technical lead releases it, and the clinical head decides which patients transfer. Owner decisions are made quickly: fund the water repair, fund the outbreak or storm preparations, chase the claims and protect payroll, hold distributions. Rights are protected: the family&rsquo;s complaint is acknowledged and the threat withdrawn. Strategy waits: the buyer is told the board will respond after the week is over.</p>
<p>Record every decision in the log: what, who, when, on what evidence, and what it protected.</p>
{{stop:In the capstone, any decision that overrides a clinical or technical hold, delays payroll for distributions, threatens a patient for complaining, or reopens without the restart gate is a critical failure.}}
{{key:Protected decisions stay protected, owner decisions are made fast, rights are respected, and strategy waits.}}
"""),
        ("ninety", "The first 90 days", "The first ninety days", """
{{fig:duo24b}}
<p>A new owner&rsquo;s first ninety days have three phases. In days 1 to 30, listen and secure: walk the floor on every shift, meet each leader, respect every hold, check cash and payroll, and read the register, the dashboard, and the last year&rsquo;s complaints. In days 31 to 60, fix the top risks with funded corrective actions that have owners and dates. In days 61 to 90, build the system: the charter, the dashboard with an actions column, and a continuity drill.</p>
{{key:Listen and secure, then fix, then build.}}
"""),
        ("defense", "The defense", "Defending the plan", """
<p>Present the board pack and the decision log to a panel that includes a clinical reviewer, a governance or finance reviewer, and ideally a patient representative. Expect questions on every protected line. The panel scores the portfolio and the defense and records any critical failure.</p>
<p>Use the owner toolkit to show your numbers live: break-even, capacity, staffing, cash runway, loan coverage, and the patient&rsquo;s share.</p>
{{key:Show your reasoning and your numbers, and name what each decision protected.}}
"""),
    ],
    "debrief": ["""
<p><strong>The first hour.</strong> Confirm the water hold and fund the repair; ask the clinical head to decide transfers. Ask the finance officer for the claims exceptions list and a payroll plan. Those two decisions are yours; the water and the transfers are not.</p>
<p><strong>The rest of the week.</strong> Approve storm preparations and early sessions with the clinical head; acknowledge the complaint and withdraw the threat in writing; tell the chain you will reply after the week.</p>
<p><strong>The first ninety days.</strong> Listen and secure, fix the top risks, build the system, as in the figure.</p>
"""],
    "skills": {"title": "Board pack, decision log, and first-ninety-days plan",
               "intro": "Complete the 72-hour inject exercise, assemble the board pack, and defend it before the panel.",
               "items": [("Assembles all 24 module outputs into seven tabs with a decisions cover sheet.", False),
                         ("Keeps every water and machine hold with the technical lead.", True),
                         ("Protects payroll and remittances and holds distributions during the cash shortfall.", True),
                         ("Withdraws the threat to the complaining family in writing.", True),
                         ("Reopens after the storm only through the restart gate.", True),
                         ("Records every decision with its evidence and what it protected.", False),
                         ("Writes a first-ninety-days plan in three phases.", False),
                         ("Shows the key numbers on the owner toolkit during the defense.", False)],
               "placement": "Run the exercise with your own leaders playing their roles, and ask the clinical reviewer to score it."},
    "quiz": [
        ("The water loop is held and payroll is due Friday. Which decision is the owner&rsquo;s?",
         ["Releasing the water", "Funding the water repair and protecting payroll", "Choosing which patients transfer", "Changing prescriptions"],
         1, "The owner funds and protects; the qualified people decide the rest."),
        ("What belongs on the board pack&rsquo;s cover sheet?",
         ["A summary of everything", "The decisions the board must make, with evidence", "Photos", "The owner&rsquo;s biography"],
         1, "Board packs exist to produce decisions."),
        ("Which is a capstone critical failure?",
         ["Asking for more data", "Overriding a technical hold", "Holding a distribution", "Writing a decision log"],
         1, "Crossing a protected line fails the capstone."),
        ("What are the three phases of the first ninety days?",
         ["Hire, fire, rehire", "Listen and secure, fix the top risks, build the system", "Market, expand, sell", "Plan, wait, decide"],
         1, "Secure the basics before building."),
        ("A chain calls about buying the unit during a crisis week. What is a sensible response?",
         ["Sell immediately", "Tell them the board will respond after the week", "Ignore all future calls", "Ask staff to vote"],
         1, "Strategy waits while safety and people come first."),
        ("Who should sit on the capstone panel?",
         ["Only the owner&rsquo;s family", "A clinical reviewer, a governance or finance reviewer, and ideally a patient representative", "The supplier", "Nobody"],
         1, "Applied judgment is tested by people who understand the protected lines."),
    ],
    "terms": [("Decision log", "A record of each decision, who made it, on what evidence, and what it protected."),
              ("Inject", "A new event released during an exercise to test decisions.")],
    "readings": [],
    "calcs": ["calc-dialysis-owner-toolkit.html"],
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
