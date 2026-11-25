# -*- coding: utf-8 -*-
"""Dialysis Unit Owner, Module 6: Feasibility and community access. Written for this course from published sources."""

MODULE = {
    "image_alt": "A provincial Philippine town of tin roofs and rice fields, with one small modern clinic at a crossroads and a road leading to a distant city.",
    "objectives": [
        "Estimate the need for hemodialysis in a catchment area and the travel burden patients carry today.",
        "Describe the local market without assuming that more units always means better access.",
        "Test a plan under bad assumptions with sensitivity analysis and the break-even calculator.",
        "Commit money in stages, through four investment gates.",
    ],
    "big": """
{{plain:A feasibility study is a weather forecast for a voyage. It cannot tell you exactly what will happen, but it tells you which storms are likely and whether your boat can survive them.}}
<p>The picture has a limit. A sailor can turn back when the weather changes. A dialysis unit that opens has patients who cannot be told to come back next season. That is why the forecast must include the bad case, and why money should be released in stages.</p>
{{cards:Key terms for this module|Catchment area::The places your patients would come from, usually set by travel time.|Sensitivity analysis::Re-running a plan with worse assumptions to see which one sinks it.|Investment gate::A checkpoint at which money is released only if its evidence exists.|Market concentration::How much of a local market a few providers hold.}}
<p>Your work here is honest: estimate need, map travel, find the assumption that can sink you, and refuse to open a unit you cannot staff.</p>
""",
    "case": {"title": "Forty kilometers", "html": """
<p>Mrs. Teresita Manalo, a retired teacher, and her two children want to open a 10-station unit in a municipality in Nueva Ecija. The nearest unit is 40 kilometers away, and patients ride a tricycle and a bus for about ninety minutes each way, three times a week. The family&rsquo;s plan assumes 60 patients by month six, claims paid in 30 days, and two nurses hired from the town.</p>
<p>Their spreadsheet shows a profit from month four. Their bank asks for a feasibility memo.</p>
""", "questions": ["Which assumption worries you most?", "How would you test the plan?", "What should happen before any building work starts?"]},
    "sections": [
        ("need", "Need", "Estimating need and travel", """
<p>Start with people, not chairs. Ask the nearest units, the provincial hospital&rsquo;s nephrologist, and local physicians how many patients from your area already dialyze elsewhere, how many are close to starting, and how long they travel. Philippine patients face long distances, out-of-pocket costs, and gaps in services, and travel time itself is a burden that leads to missed sessions.[[pc_pajimna2023]]</p>
<p>Convert need into station-sessions. Each patient on three sessions a week needs three station-sessions. With two shifts a day, six days a week, one station gives twelve station-sessions a week, enough for four patients with no slack. Keep slack for make-up sessions, as Module 2 explained.</p>
{{key:Count the patients and their travel time before you count the chairs.}}
"""),
        ("market", "The market", "Reading the local market", """
<p>More units do not always mean more choice. In the United States, a decade of consolidation left local dialysis markets highly concentrated, with an average Herfindahl-Hirschman Index (HHI) of 0.46, where 1 means a single provider; patients&rsquo; choices did not shrink only because new facilities kept opening to meet demand.[[duo_erickson2017]] The Philippine market is different, but the lesson transfers. Ask who already serves your area, whether they are full, and whether your unit adds access or only divides the same patients.</p>
<p>A unit that only divides patients will compete on inducements, and Module 19 explains why that harms them. A unit that shortens a ninety-minute trip to twenty minutes adds real access.</p>
{{key:Build where you add access, not where you only divide patients.}}
"""),
        ("sensitivity", "Sensitivity", "Find the assumption that can sink you", """
{{fig:duo06b}}
<p>Every plan rests on a few assumptions: sessions per month, net revenue per session, days to collect, staff cost, supply prices, and rent. Change each one to a realistic bad value, one at a time, and see how far the result moves. The assumption that moves it most is the one to test hardest.</p>
<p><strong>Worked example (fictional).</strong> Fixed costs are 630,000 pesos a month. Net facility revenue is 6,000 pesos a session after the professional fee share and deductions, and variable cost is 3,900 pesos. Contribution is 2,100 pesos a session, so break-even is 630,000 &divide; 2,100 = 300 sessions a month: 25 patients on three sessions a week. The family&rsquo;s 60 patients would be comfortably above break-even, but only if they arrive. At 30 patients in month six, the unit earns a small margin; at 20, it loses money every month.</p>
<p>Then test cash. If claims take 75 days instead of 30, the unit must finance about two and a half months of revenue before cash catches up. Module 17 shows how to size that.</p>
{{key:Run the bad case for volume and for collection time before you sign a lease.}}
"""),
        ("gates", "Investment gates", "Four gates before you build", """
{{fig:duo06a}}
<p>Release money in stages. Each gate opens only when its evidence exists.</p>
<div class="table-wrap"><table>
<thead><tr><th>Gate</th><th>Evidence needed</th></tr></thead>
<tbody>
<tr><td>1. Need and travel</td><td>Named sources for patient numbers; travel times; letters of interest from referring physicians</td></tr>
<tr><td>2. Staff and water</td><td>A clinical head who has agreed in principle; a realistic hiring plan for nurses; a water source tested for treatment design</td></tr>
<tr><td>3. Money under the bad case</td><td>Break-even, cash runway, and loan coverage under low volume and slow collection</td></tr>
<tr><td>4. Permits and accreditation path</td><td>Permit to construct, design reviewed against DOH guidelines, and a timeline for license and accreditation</td></tr>
</tbody></table></div>
<p>Gate 2 is the one families most often skip. A building without nurses, or with water that cannot be treated to standard, is not a unit.</p>
{{key:No gate, no money. Staff and water come before the building.}}
"""),
    ],
    "debrief": ["""
<p><strong>The worrying assumptions.</strong> Sixty patients by month six and claims paid in 30 days. Both are optimistic. Two nurses from the town are also unlikely to cover two shifts at the DOH limit.</p>
<p><strong>The test.</strong> Run the break-even calculator at 20, 30, and 60 patients and the cash calculator at 75 days to collect. Ask the bank for a facility that survives the bad case.</p>
<p><strong>Before building.</strong> Pass Gate 1 with real patient counts, Gate 2 with a clinical head and a staffing plan that meets the license, and Gate 3 with a funded reserve. Only then sign the construction contract.</p>
"""],
    "skills": {"title": "Feasibility memo with sensitivity and investment gates",
               "intro": "Write a two-page feasibility memo for a fictional site and present it to a mock lender.",
               "items": [("Estimates need from named sources and states travel times.", False),
                         ("Converts patients into station-sessions with make-up slack.", False),
                         ("Runs break-even and cash for a base case and a bad case.", False),
                         ("Names the assumption with the widest effect and how it will be tested.", False),
                         ("Refuses to release construction money before staffing and water are secured.", True),
                         ("Lists the four gates with the evidence each requires.", False)],
               "placement": "Call one nearby unit and ask, with permission, how many patients travel from your area and how far."},
    "quiz": [
        ("What should a feasibility study count first?",
         ["Chairs", "Patients who need dialysis and how far they travel", "Parking spaces", "Competitors&rsquo; prices"],
         1, "Need and travel time decide whether the unit adds access."),
        ("Fixed costs are 630,000 pesos a month and contribution is 2,100 pesos a session. What is break-even?",
         ["210 sessions", "300 sessions", "630 sessions", "2,100 sessions"],
         1, "630,000 &divide; 2,100 = 300 sessions a month."),
        ("What does a sensitivity analysis tell you?",
         ["The exact future profit", "Which assumption moves the result most when it turns bad", "The best-case outcome", "The tax due"],
         1, "It ranks assumptions by their effect, so you test the dangerous ones."),
        ("Which gate do families most often skip, with the most harm?",
         ["Choosing a paint color", "Securing staff and treatable water", "Buying furniture", "Printing flyers"],
         1, "A building without nurses or water to standard cannot safely treat patients."),
        ("What did Erickson and colleagues find about United States dialysis markets?",
         ["Markets were perfectly competitive", "Local markets were highly concentrated, with a mean HHI of 0.46", "Patient choice disappeared", "Prices fell sharply"],
         1, "Markets stayed concentrated; new facilities offset some effects of consolidation on choice."),
        ("Claims take 75 days to pay instead of 30. What changes most?",
         ["Break-even volume", "The cash the unit must finance before collections arrive", "The DOH license", "The water standard"],
         1, "Collection time changes cash needs, not accounting break-even."),
    ],
    "terms": [("Station-session", "One station used for one treatment slot."),
              ("Letter of interest", "A written statement from a referring physician of intent to refer patients.")],
    "readings": [],
    "calcs": ["calc-dialysis-owner-toolkit.html#c1", "calc-dialysis-owner-toolkit.html#c3"],
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
