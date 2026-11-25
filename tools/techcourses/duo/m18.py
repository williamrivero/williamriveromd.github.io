# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 18: Quality dashboards and board assurance. Written for this course from published sources."""

MODULE = {
    "image_alt": "A tablet on a boardroom table showing a run chart whose line shifts upward, beside three indicator cards.",
    "objectives": [
        "Choose indicators with clear definitions and denominators.",
        "Read a run chart and tell a signal from noise.",
        "Explain what the evidence says about ownership, ratings, and outcomes, and how strong it is.",
        "Build a dashboard in which every indicator leads to an owned action.",
    ],
    "big": """
{{plain:A quality dashboard is the instrument panel of a plane. A pilot does not stare at every dial at once; a few dials, read correctly and often, tell the pilot whether the plane is safe. A dial with no units is useless, and a dial nobody reads is decoration.}}
<p>The picture has a limit. Plane instruments measure physics. Quality indicators measure people and processes, and they can be gamed. A dashboard that rewards low numbers will get low numbers, sometimes by not counting. That is why every indicator needs a definition, a denominator, and a check that the data are complete.</p>
{{cards:Key terms for this module|Indicator::A measure tracked over time, such as infections per 1,000 catheter-days.|Denominator::What the count is divided by; without it, a count means little.|Run chart::A line chart of an indicator over time with its median.|Signal::A change in a run chart unlikely to be chance.|Quality assessment and performance improvement (QAPI)::The unit&rsquo;s regular cycle of measuring and improving quality.}}
<p>Your work is to ask for few indicators, read them correctly, and insist that each one leads to a decision.</p>
""",
    "case": {"title": "A green dashboard and three deaths", "html": """
<p>The board of a unit in Cagayan de Oro receives a dashboard of 22 green indicators. In the same quarter, three patients died within a month of hospital admission for fluid overload. None of the 22 indicators tracked missed sessions, hospital admissions, or the long-gap day. The clinical head, Dr. Esperanza Lagman, asks for a different dashboard.</p>
""", "questions": ["What was wrong with the dashboard?", "Which indicators would you add?", "How will the board know the changes worked?"]},
    "sections": [
        ("indicators", "Indicators", "Few indicators, clearly defined", """
<p>Choose a small set that covers safety, access, and outcomes: bloodstream infections per 1,000 catheter-days, the share of patients on catheters, missed sessions per 100 scheduled, hospital admissions per patient-year, deaths, water test completeness, staff competency current, complaints by cause, and referrals for transplant or home dialysis. Write a one-line definition and denominator for each. The quality-rate calculator gives each rate a confidence interval, so the board can see how much a small unit&rsquo;s number can move by chance.</p>
{{key:No denominator, no indicator.}}
"""),
        ("variation", "Reading change", "Read the trend, not the month", """
{{fig:duo18a}}
<p>Plot each indicator monthly with its median. A single bad month is usually noise. A run of several points on one side of the median, or a steady trend, is a signal worth investigating.[[uom_perla2011]] Small units see large swings by chance, so react to patterns, not to one number.</p>
{{key:Investigate signals; watch single points.}}
"""),
        ("ownership", "What the evidence says", "Ownership, ratings, and outcomes", """
<p>Ownership and structure are associated with outcomes, and a board should know it. A meta-analysis of eight observational studies, covering more than 500,000 patient-years, found that care at private for-profit United States centers was associated with higher adjusted mortality than at nonprofit centers (relative risk 1.08, 95% confidence interval 1.04 to 1.13).[[duo_devereaux2002]] Among large chains, for-profit chain affiliation was associated with 19% to 24% higher mortality than a nonprofit chain.[[duo_zhang2011]] When a study reports a relative effect, ask for the absolute difference and the number needed to treat (NNT); calculator 9 does the arithmetic. These are associations from another payment system; case mix and practice differences, not ownership itself, may explain much of them. Many for-profit units perform very well.</p>
<p>Public ratings track some of this. In Korea, patients at low-rated facilities had higher mortality (hazard ratio 1.11).[[duo_park2023]] In the United States, star-rating improvements came mostly from measures facilities directly control, and independent facilities improved less than large chains.[[duo_salerno2021]] The lesson for an owner is not about ownership type. It is that what a board measures and acts on shows up in outcomes.</p>
{{key:Ownership type does not decide quality. What the board measures and does about it does.}}
"""),
        ("actions", "From data to action", "A dashboard that drives action", """
{{fig:duo18b}}
<p>Give every indicator five columns: the indicator and its denominator, the trend, the interpretation by the clinical head, the action with an owner and a date, and the proof it worked. A dashboard with no actions column is a report, not governance. Use the unit&rsquo;s QAPI meeting to feed it, and review the actions column first at every board meeting.</p>
{{key:Read the actions column first.}}
"""),
    ],
    "debrief": ["""
<p><strong>What was wrong.</strong> Twenty-two indicators, none of them about the risks that were killing patients, and no actions column.</p>
<p><strong>What to add.</strong> Missed sessions per 100 scheduled, admissions per patient-year (with causes), deaths with a short review of each, and the long-gap day. Cut the dashboard to a dozen indicators with denominators.</p>
<p><strong>How to know it worked.</strong> Run charts over the next six months, with each action&rsquo;s proof recorded.</p>
"""],
    "skills": {"title": "Board dashboard and assurance action register",
               "intro": "Rebuild a fictional unit&rsquo;s dashboard with a dozen indicators and an action register.",
               "items": [("Defines each indicator with a denominator.", False),
                         ("Reads a run chart and distinguishes a signal from a single point.", False),
                         ("Describes ownership evidence as observational and avoids blaming ownership type.", False),
                         ("Includes missed sessions, admissions, and deaths.", True),
                         ("Gives every indicator an owned action with a date and proof.", False),
                         ("Reviews the actions column first at each meeting.", False)],
               "placement": "Take your unit&rsquo;s current dashboard and add a denominator and an owner to every line."},
    "quiz": [
        ("Which is a well-defined indicator?",
         ["Infections this month", "Bloodstream infections per 1,000 catheter-days", "Good care score", "Number of happy patients"],
         1, "A denominator makes rates comparable."),
        ("On a run chart, which is a signal?",
         ["One high point", "Several consecutive points on one side of the median", "Any change", "The latest month"],
         1, "Runs and trends are signals; single points are usually noise."),
        ("The Devereaux meta-analysis found for-profit United States centers were associated with:",
         ["Lower mortality", "Higher adjusted mortality, relative risk 1.08", "No difference", "Higher transplant rates"],
         1, "Eight observational studies; association only."),
        ("What did Salerno and colleagues find about star-rating improvement?",
         ["It came mostly from measures facilities directly control", "Ratings never changed", "Independent facilities improved most", "Ratings were random"],
         0, "Independents improved less than large chains."),
        ("Which column turns a report into governance?",
         ["Color", "Action, owner, and date", "Logo", "Font size"],
         1, "Indicators should lead to decisions."),
        ("A dashboard is all green, but patients are dying of fluid overload. The likeliest problem is:",
         ["Too few colors", "It does not measure the risks that matter", "The printer", "Too many denominators"],
         1, "Choose indicators that track real risks."),
    ],
    "terms": [("Median", "The middle value; half the points are above and half below.")],
    "readings": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement.")],
    "calcs": ["calc-dialysis-clinical-head-toolkit.html#c3", "calc-dialysis-clinical-head-toolkit.html#c9", "calc-dialysis-qapi-scorecard.html"],
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
