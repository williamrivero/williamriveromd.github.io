# -*- coding: utf-8 -*-
"""Dialyzer Reprocessing Technician, Module 02: The Dialyzer and Why Reuse Exists. v0.1 RT02, expanded with the evidence."""

MODULE = {
    "image_alt": "A hollow-fiber dialyzer cut open lengthwise on a clean bench, showing thousands of fine fibers, beside a magnifying glass.",
    "objectives": [
        "Explain how a dialyzer removes waste and water by diffusion and ultrafiltration across thousands of hollow fibers.",
        "Explain why clotted or protein-coated fibers reduce the dose of dialysis, and how total cell volume (TCV) estimates open fibers.",
        "Describe what the Hemodialysis (HEMO) Study showed about clearance as dialyzers are reused.",
        "Summarize the outcome evidence on reuse and state how strong it is.",
        "Name the reasons units reuse dialyzers and the limits of each reason.",
    ],
    "big": """
{{plain:Picture a kitchen sieve made of ten thousand tiny straws. Blood runs through the straws; clean fluid runs around them the other way. Small waste slips through the straw walls into the clean fluid and is carried away. If some straws are plugged, the blood is squeezed into fewer straws, and less waste gets out.}}
<p>The picture has a limit. The straw walls are not just holes. They are a membrane with pores of a designed size, and the blood leaves a thin protein layer on them during every treatment. Germicides and cleaning agents can change that layer and the pores themselves. So a reused dialyzer is not the same dialyzer it was on day one, and the patient&rsquo;s dose can drift without anyone seeing it.</p>
{{cards:Key terms for this module|Hollow fiber::One of the thousands of thin tubes inside a dialyzer. Blood flows inside, dialysis fluid outside.|Diffusion::Movement of a dissolved substance from higher to lower concentration across the membrane.|Ultrafiltration::Removal of water by pressure across the membrane.|Clearance::How much blood is completely cleared of a substance per minute.|Total cell volume (TCV)::The volume of the blood compartment, measured to estimate how many fibers remain open.|Middle molecules::Larger waste molecules, such as beta-2-microglobulin, that pass the membrane slowly.}}
<p>Your work is not to calculate the dose; that belongs to the nurse and the nephrologist. Your work is to return a dialyzer whose fibers are open, whose membrane is intact, and whose history is complete, so that the dose the nephrologist prescribes is the dose the patient receives.</p>
""",
    "case": {"title": "The fourth use", "html": """
<p>Mrs. Corazon Villaflor, 58, dialyzes three times a week at a unit in Pampanga. Her dialyzer is reused under the unit&rsquo;s program. Over two months, the nurse notices that her monthly adequacy result has drifted down, although her blood flow, session time and dialyzer type have not changed.</p>
<p>The reprocessing technician, Mr. Rommel Pangilinan, pulls the records. Her dialyzers have tended to come back with partly clotted headers. Their volume results have been passing, but each one lower than the last: 92%, 88%, 84%, 81% of baseline by the fourth use.</p>
""", "questions": ["How can a dialyzer that passes every test still deliver less dialysis?",
                  "What does the research say about clearance as dialyzers are reused?",
                  "What should Mr. Pangilinan report, and to whom?"]},
    "sections": [
        ("how-it-works", "How it cleans", "How a dialyzer cleans blood", """
{{fig:dialyzer_anatomy}}
<p>A dialyzer is a plastic cylinder packed with thousands of hollow fibers. Blood enters one end, flows through the inside of the fibers, and leaves the other end. Dialysis fluid flows around the outside of the fibers in the opposite direction, which keeps the concentration difference high along the whole length.</p>
<p>Two processes do the work. In diffusion, small waste molecules such as urea move from the blood, where they are concentrated, into the dialysis fluid, where they are not. In ultrafiltration, pressure pushes water out of the blood, and some solutes are carried with it. Both depend on surface: the more open fiber wall the blood touches, the more waste crosses.</p>
<div class="table-wrap"><table>
<thead><tr><th>What happens to the fibers</th><th>Effect on the dialyzer</th><th>What you may see in the room</th></tr></thead>
<tbody>
<tr><td>Clot blocks some fibers</td><td>Less surface; small-molecule clearance falls</td><td>Dark streaks in the bundle; clot in the header; lower TCV</td></tr>
<tr><td>Protein coats the inner wall</td><td>Larger molecules pass less easily</td><td>Usually nothing visible</td></tr>
<tr><td>Germicide or bleach alters the membrane</td><td>Pores may tighten or widen, depending on membrane and method</td><td>Nothing visible; only measured clearance shows it</td></tr>
<tr><td>A fiber breaks</td><td>Blood and dialysis fluid can mix</td><td>A failed integrity test</td></tr>
</tbody></table></div>
{{key:Every closed fiber is surface the patient no longer gets. Every broken fiber is a path between blood and dialysis fluid.}}
"""),
        ("dose", "What reuse does to the dose", "What reuse does to the dose", """
{{fig:rt02_fibers}}
<p>The best measurement study comes from the HEMO Study, a large United States trial. Cheung and colleagues measured clearance in dialyzers reprocessed with several germicides and methods. Urea clearance fell by about 1% to 2% for every ten reuses, whatever the membrane or method. Clearance of beta-2-microglobulin, a middle molecule, fell, stayed the same, or rose substantially, depending on the membrane material and the reprocessing technique.[[rt_cheung1999]] The study measured clearance, a surrogate; it did not measure how patients felt or lived.</p>
<p>Smaller studies show why the floor matters. In one crossover study, the blood-compartment volume of dialyzers fell between the first and second use with standard heparin.[[rt_kerr1994]] In another, adjusting heparin doses improved measured urea clearance without changing the measured blood-compartment volume.[[rt_wei1994]] Clotting during treatment closes fibers; the reuse room only measures what the floor sends.</p>
<p>New membranes are still being studied. A 2025 study from Thailand reused super high-flux dialyzers with peracetic acid up to 15 times in five patients. Beta-2-microglobulin clearance was similar at the first and fifteenth use, but removal of two larger or protein-bound toxins fell, and albumin leakage into the dialysis fluid dropped sharply after the first use.[[rt_prapunwatana2025]] The study was very small; it suggests that reuse affects different toxins differently, not that 15 reuses are safe.</p>
{{key:A dialyzer can pass its volume test and still clean less than it did on day one. Report a falling trend, not just a failure.}}
"""),
        ("evidence", "The outcome evidence", "Does reuse change how patients do?", """
{{fig:rt02_evidence}}
<p>No randomized trial has compared reuse with single use on outcomes that patients feel. What exists is observational, and it points in different directions.</p>
<div class="table-wrap"><table>
<thead><tr><th>Study</th><th>Design and size</th><th>Finding</th><th>What it cannot show</th></tr></thead>
<tbody>
<tr><td>Galvao and colleagues, 2012</td><td>Systematic review of 14 studies, 956,807 patients; evidence graded very low quality</td><td>No consistent difference in death between reuse and single use; differences varied by germicide, period and unit[[rt_galvao2012]]</td><td>That reuse is safe, or unsafe</td></tr>
<tr><td>Lacson and colleagues, 2011</td><td>23 facilities that stopped peracetic acid reuse, before and after</td><td>Single use was associated with lower death risk (adjusted hazard ratio 0.74) and lower C-reactive protein (CRP), an inflammation marker[[rt_lacson2011]]</td><td>Cause and effect; other changes over time may explain it</td></tr>
<tr><td>Bond and colleagues, 2011</td><td>Large provider; instrumental-variable and propensity analyses</td><td>No difference in death; 13.8 million dialyzers and about 10,000 metric tons of waste avoided[[rt_bond2011]]</td><td>Safety of a poorly run program</td></tr>
<tr><td>Argyropoulos and colleagues, 2015</td><td>Secondary analysis of HEMO</td><td>The survival advantage of high-flux dialyzers seen with little reuse reversed with extensive reuse[[rt_argyropoulos2015]]</td><td>A safe maximum number of reuses</td></tr>
</tbody></table></div>
<p>Reviewers disagree on what to make of this. One editorial argued that cheap biocompatible membranes weaken the case for reuse;[[rt_robinson2005]] another weighed safety against cost and waste in settings where cost still decides access.[[rt_upadhyay2019]] The honest summary: outcome evidence is weak in both directions. The harms that are well documented, covered in Modules 4 to 6, came from failures of execution.</p>
{{key:The research does not prove reuse harmful or harmless. It proves that badly executed reuse hurts patients.}}
"""),
        ("why-reuse", "Why units reuse", "Why units reuse, and the limits of each reason", """
<div class="table-wrap"><table>
<thead><tr><th>Reason</th><th>What is true</th><th>The limit</th></tr></thead>
<tbody>
<tr><td>Cost</td><td>A reused dialyzer spreads its price over several treatments. PhilHealth&rsquo;s package allows up to five uses per dialyzer.[[rt_phic0023]]</td><td>Savings never justify keeping a dialyzer that fails a gate.</td></tr>
<tr><td>Waste</td><td>Reuse cuts plastic waste; one provider avoided about 10,000 metric tons.[[rt_bond2011]] Dialysis is among the most resource-intensive therapies.[[rt_barraclough2020]]</td><td>Reprocessing uses water and chemicals; the net environmental effect has not been measured well.</td></tr>
<tr><td>First-use reactions</td><td>Older cellulose membranes caused reactions on first use that reuse reduced.</td><td>Modern synthetic membranes rarely cause them, so this reason has largely faded.[[rt_robinson2005]]</td></tr>
</tbody></table></div>
{{key:Cost and waste explain why units reuse. They never decide whether this dialyzer is safe.}}
"""),
    ],
    "debrief": ["""
<p><strong>How can a passing dialyzer deliver less?</strong> A volume result of 81% still meets the 80% floor, but it means about a fifth of the blood compartment is gone, mostly from closed fibers. Less open surface means less urea crosses. The HEMO data also show that clearance falls a little with reuse even when volume is kept.[[rt_cheung1999]]</p>
<p><strong>What does the research say?</strong> Urea clearance falls slightly with reuse; middle-molecule clearance depends on membrane and method. Outcome studies are observational and inconsistent.</p>
<p><strong>What should Mr. Pangilinan report?</strong> The trend, with the dialyzer numbers and dates: falling volumes and repeated header clots. He reports to the head nurse and the nurse caring for Mrs. Villaflor, who will tell the nephrologist. The fix may be on the floor, in heparin or end-of-treatment rinsing, not in the room. Whether to change her dialyzer or limit its uses is the nephrologist&rsquo;s decision.</p>
"""],
    "skills": {"title": "Reading a dialyzer and its history",
               "intro": "Use a cut-open training dialyzer and a set of synthetic processing records.",
               "items": [
                   ("Identifies the blood ports, the dialysate ports, the headers and the fiber bundle.", True),
                   ("Explains diffusion and ultrafiltration in one sentence each.", False),
                   ("Recognizes clot in a header and dark streaks in a fiber bundle.", True),
                   ("Calculates retained volume for three records and identifies a falling trend that still passes.", True),
                   ("States what the outcome evidence on reuse does and does not show.", False),
                   ("Names the people who receive a trend report and what they may decide.", False),
               ],
               "placement": "For two weeks, list every dialyzer whose volume fell by more than ten points between two uses. Review the list with your preceptor."},
    "quiz": [
        ("Why does a clotted fiber reduce the dose of dialysis?",
         ["It changes the dialysis fluid", "It removes membrane surface the blood can touch", "It raises the blood flow", "It adds germicide to the blood"], 1,
         "Diffusion depends on surface. Closed fibers remove surface."),
        ("In the HEMO analysis, how much did urea clearance change with reuse?",
         ["It fell about 1% to 2% per 10 reuses", "It fell by half after five reuses", "It did not change", "It rose with each reuse"], 0,
         "A small, consistent fall regardless of membrane or method."),
        ("In the same analysis, what happened to beta-2-microglobulin clearance?",
         ["It always fell", "It always rose", "It fell, stayed, or rose depending on membrane and method", "It was not measured"], 2,
         "Middle-molecule clearance depends on the membrane material and the reprocessing technique."),
        ("What did the 2012 systematic review conclude about reuse and death?",
         ["Reuse doubles mortality", "No consistent difference, with very low quality evidence", "Single use is proven safer", "Reuse is proven safer"], 1,
         "Fourteen observational studies; very low quality; no consistent difference."),
        ("What kind of study was the 2011 report of facilities that stopped peracetic acid reuse?",
         ["A randomized trial", "A before-and-after observational comparison", "A laboratory study", "A meta-analysis"], 1,
         "Before-and-after designs cannot exclude changes over time, so the finding is an association."),
        ("A dialyzer&rsquo;s volume has gone 92%, 88%, 84%, 81%. What is the best action?",
         ["Nothing, it is still passing", "Report the falling trend to the head nurse and the patient&rsquo;s nurse", "Discard it at once without a record", "Reset its baseline"], 1,
         "The trend is information for the floor and the nephrologist. The baseline is never reset."),
        ("Where does most fiber clotting begin?",
         ["In the storage rack", "During treatment on the floor", "In the germicide", "In the factory"], 1,
         "Clotting happens while blood flows. Heparin and rinsing at the end of treatment matter."),
        ("What did the 2025 study of super high-flux dialyzer reuse show?",
         ["Fifteen reuses are proven safe", "Some toxins were removed less well with reuse, in a very small study", "Albumin loss rose with reuse", "Reuse improved every clearance"], 1,
         "Five patients, 15 dialyzers: beta-2-microglobulin kept, other toxins fell. A small study only suggests."),
        ("Which reason for reuse has largely faded with modern membranes?",
         ["Cost", "Waste", "Reducing first-use reactions", "Patient preference"], 2,
         "First-use reactions were mainly a problem of older cellulose membranes."),
        ("What does total cell volume estimate?",
         ["The germicide strength", "How many fibers remain open", "The patient&rsquo;s blood volume", "The water quality"], 1,
         "The blood-compartment volume shrinks as fibers close."),
        ("A colleague says reuse is proven safe. What is the most accurate reply?",
         ["Yes, many trials prove it", "The outcome studies are observational and inconsistent; documented harms come from poor execution", "No, reuse is proven to kill", "Only the cost matters"], 1,
         "The honest summary is uncertainty about outcomes and certainty that execution failures cause harm."),
        ("Which outcome is a surrogate?",
         ["Death", "Hospitalization", "Urea clearance", "Bloodstream infection"], 2,
         "Clearance is a laboratory measure. It matters, but it is not an outcome the patient feels."),
    ],
    "terms": [("Hollow fiber", "A thin tube inside a dialyzer; blood flows inside, dialysis fluid outside."),
              ("Diffusion", "Movement of a dissolved substance from higher to lower concentration."),
              ("Ultrafiltration", "Removal of water from blood by pressure across the membrane."),
              ("Clearance", "The volume of blood completely cleared of a substance per minute."),
              ("Middle molecules", "Larger waste molecules that cross the membrane slowly."),
              ("Surrogate outcome", "A measurement used in place of an outcome patients feel."),
              ("Systematic review", "A study that gathers and appraises all studies on one question."),
              ("Hazard ratio", "A comparison of how fast an event happens in one group compared with another.")],
    "readings": [("dialysis-adequacy.html", "How the dose of dialysis is measured."),
                 ("green-nephrology.html", "The environmental footprint of dialysis.")],
    "calcs": ["calc-reprocessing-technician-toolkit.html#c1"],
}


# Spread the keyed answers across positions A to D.
import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("rt_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
