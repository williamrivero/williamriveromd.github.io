# -*- coding: utf-8 -*-
"""Vascular Surgeon, Module 9: Maturation and the first cannulation. Written for this track from published sources (v2.0 blueprint)."""

MODULE = {
    "image_alt": "A surgeon and a senior dialysis nurse examine a forearm fistula together, the nurse marking a straight needle segment with a skin pen.",
    "objectives": [
        "Distinguish a patent access from a usable one, using examination and ultrasound.",
        "Apply the evidence on ultrasound predictors of maturation, and explain why they are surrogates.",
        "Explain why the timing of first cannulation and the cannulation technique matter, with the strength of the evidence.",
        "Agree a written first-use plan with the authorized dialysis team and confirm it was received.",
    ],
    "big": """
{{plain:A thrill under your fingers is like hearing an engine running. It tells you the engine is on. It does not tell you whether the car has wheels, whether the road is paved, or whether a learner can drive it.}}
<p>The picture has a limit. An engine and a car are separate parts. In a fistula, flow and usability are linked, but loosely. Flow drives remodeling; remodeling produces the diameter, wall thickness and superficial straight segment a nurse needs. A fistula can have good flow and still be too deep, too short, or too tortuous to needle twice each session.</p>
{{cards:Key terms for this module|Patent::Open, with flow.|Usable (mature)::Able to deliver the prescribed dialysis reliably with two needles.|Look, feel and listen::The bedside examination of an access: inspection, palpation for thrill and pulse, auscultation of the bruit.|Rope-ladder cannulation::Rotating needle sites along the whole segment.|Buttonhole cannulation::Using the same site and angle each time to create a tract.}}
<p>Silence is not permission to cannulate. Your work is to decide, with the dialysis team, whether the fistula is ready, where it may be needled, and what happens if the first attempt fails.</p>
""",
    "case": {"title": "Six weeks and a thrill", "html": """
<p>Ms. Josefina Aquino, 44, had a left radiocephalic fistula created six weeks ago. She dialyzes through a right jugular catheter that has needed two lock treatments for poor flow. The charge nurse at her unit, Mr. Arnel Pascual, calls: &ldquo;There is a good thrill, doctor. Six weeks is enough, right? Can we start needling today and pull the catheter?&rdquo;</p>
<p>You have not seen her since the operation. Her duplex this morning, ordered by her nephrologist, shows a minimum vein diameter of 3.6 mm, flow of 420 mL/min, and a vein 7 mm deep at the planned needle zone, with a large side branch 5 cm from the anastomosis.</p>
""", "questions": [
        "Is this fistula ready to cannulate today?",
        "What would you do about the findings?",
        "What should the first-use plan say?"]},
    "sections": [
        ("readiness", "Patent versus usable", "From patent to usable: what predicts it", """
<p>Robbin and colleagues studied 69 new fistulas with ultrasound within four months of creation. Fistulas with a minimum vein diameter of 4 mm or more were adequate for dialysis in 89%, compared with 44% below 4 mm; flow of 500 mL/min or more gave 84% versus 43%. When both criteria were met, 95% were adequate; when neither was, only 33% were.[[vs_robbin2002]] These were retrospective single-center data, and diameter and flow are surrogates for usability, but the pattern has held up, and the NEAT study later used flow of at least 500 mL/min and vein diameter of at least 4 mm as its definition of physiologic suitability.[[vs_lok2017]]</p>
{{fig:vs09_a}}
<p>Depth and length matter as much. A vein deeper than about 6 mm is hard to needle reliably, and a short straight segment leaves no room for rotation. An older expert benchmark, the &ldquo;rule of 6s&rdquo; (diameter of at least 6 mm, depth under 6 mm, flow above 600 mL/min at 6 weeks), is opinion-based and stricter than the Robbin criteria; use it as a prompt, not a rule.</p>
<p>The UK Kidney Association (UKKA) 2025 guideline recommends an initial maturity assessment between 2 and 6 weeks after formation, with investigation for non-maturity persisting beyond 6 weeks (statement 3.9, grade 1C), and suggests that the decision to start cannulation follow individualized assessment, balancing the risk of miscannulation against the need for prompt access (3.10, grade 2C).[[vs_ukka]]</p>
{{key:Calendar time and a thrill do not establish readiness. Diameter, flow, depth and a usable straight segment, judged together, do.}}
"""),
        ("timing", "Timing and technique", "When and how to start needling", """
<p>Needling too early can injure an immature vein: infiltration, hematoma and compression of a fragile segment. In the Dialysis Outcomes and Practice Patterns Study (DOPPS), fistulas first cannulated within 14 days of creation had about twice the risk of later failure (relative risk 2.1). Fistulas first cannulated at 15 to 28 days did no worse than those first cannulated at 43 to 84 days.[[vs_rayner2003]] This was observational, and early cannulation may have been chosen for patients with better fistulas or more urgent need, so it does not prove a safe threshold. It does argue against needling in the first two weeks.</p>
{{fig:vs09_b}}
<p>Technique affects infection and aneurysm. UKKA recommends rope-ladder or buttonhole cannulation for fistulas, and rope-ladder for grafts, in preference to area puncture (statement 3.14, grade 1C).[[vs_ukka]] A systematic review found that buttonhole cannulation appeared to carry more local and systemic infections than rope-ladder, with equivocal effects on pain.[[vs_wong2014]] Another review found access-related infections about three times as frequent with buttonhole across trials and observational studies.[[vs_muir2014]] KDOQI 2019 favors rope-ladder as the routine method and reserves buttonhole for selected patients.[[vs_kdoqi]]</p>
<div class="table-wrap"><table>
<thead><tr><th>Finding at assessment</th><th>What it suggests</th><th>Usual action</th></tr></thead>
<tbody>
<tr><td>Diameter and flow adequate, superficial, long segment</td><td>Ready</td><td>Written first-use plan; experienced cannulator</td></tr>
<tr><td>Good flow, vein too deep</td><td>Usable after superficialization</td><td>Discuss superficialization or transposition</td></tr>
<tr><td>Low flow with a large side branch</td><td>Flow diverted</td><td>Consider branch ligation</td></tr>
<tr><td>Low flow, strong pulse at anastomosis only</td><td>Juxta-anastomotic stenosis</td><td>Imaging and angioplasty or revision</td></tr>
</tbody></table></div>
"""),
        ("handoff", "The first-use plan", "Writing the first-use plan", """
<p>The first cannulation is a team event. UKKA recommends an access assessment before every cannulation, by a trained cannulator (3.12, grade 1C), and unit policies to minimize cannulation complications, which may include ultrasound-assisted cannulation or single-needle dialysis for new or difficult access (3.15, grade 1C).[[vs_ukka]] Your contribution is a clear, written plan.</p>
{{flow:The first-use plan|Readiness::State that the access is ready, and on what basis.|Permitted segment::Mark it on a drawing or the skin; name segments to avoid.|Who needles::An experienced cannulator for the first sessions; ultrasound if available.|How to start::Needle size and flow are the unit&rsquo;s protocol; your plan says if a gentle start is needed.|If it fails::Stop after a set number of attempts, keep the catheter, and call the named surgeon.|Catheter removal::After a defined number of successful sessions.}}
{{scene:Dialysis unit, fictional|<p>On the first two-needle session of a new fistula, the arterial needle infiltrates. The nurse follows the written plan: she stops, applies pressure, uses the catheter for the session, and calls you. A week later, with ultrasound guidance, cannulation succeeds.</p><p class="tc-scene-take"><b>What this shows.</b> A plan for failure turns a miscannulation into a delay instead of a lost fistula.</p>}}
{{call:Do not authorize first cannulation by phone without an assessment and a written plan. Confirm the dialysis unit received the plan before the first session.}}
"""),
    ],
    "debrief": [
        "<p><strong>Ready today?</strong> Not yet. At six weeks her vein is under 4 mm, flow is under 500 mL/min, the vein is 7 mm deep at the planned zone, and a large side branch is diverting flow. By the Robbin criteria she meets neither, a group in which only about a third of fistulas were adequate. The thrill only shows flow.</p>",
        "<p><strong>What to do.</strong> UKKA advises investigating non-maturity beyond six weeks. See her this week. Consider ligating the side branch to redirect flow, and plan superficialization if the vein remains deep. Keep the catheter, and ask the nephrologist about lock therapy or exchange if its flow worsens.</p>",
        "<p><strong>The plan to write.</strong> Not ready; reason; planned procedure and date; reassessment date; the catheter stays. When she is ready, the first-use plan will mark the permitted segment, name an experienced cannulator, state what to do after a failed attempt, and when to remove the catheter. Call Mr. Pascual back and have him read it back.</p>",
    ],
    "skills": {"title": "Joint readiness assessment and first-use handoff",
               "intro": "Performed with a dialysis nurse and assessed by a qualified surgeon.",
               "items": [("Examines the access using look, feel and listen, and checks the hand", False),
                         ("Interprets diameter, flow and depth together, not singly", True),
                         ("Marks the permitted cannulation segment and segments to avoid", False),
                         ("Writes a plan for failed cannulation and catheter removal", True),
                         ("Confirms receipt of the plan by the dialysis team", True)],
               "placement": "Access clinic with dialysis nurse"},
    "quiz": [
        ("A fistula is six weeks old and has a thrill. Is that enough to authorize first use?",
         ["Yes, always", "Yes, if the appointment is delayed", "No; usability and a cannulation plan still need assessment",
          "Yes, if the patient agrees"],
         2, "Calendar age and patency do not alone establish safe cannulation."),
        ("Which routine cannulation strategy does KDOQI favor for most fistulas?",
         ["Rope-ladder, with site rotation", "Area puncture", "Buttonhole for every access", "Single-site puncture without rotation"],
         0, "KDOQI favors rope-ladder and reserves buttonhole for selected patients, given infection concerns."),
        ("In Robbin&rsquo;s study, what share of fistulas meeting both diameter of at least 4 mm and flow of at least 500 mL/min were adequate for dialysis?",
         ["33%", "50%", "75%", "95%"],
         3, "95% when both criteria were met, versus 33% when neither was."),
        ("What did the Dialysis Outcomes and Practice Patterns Study (DOPPS) associate with a higher risk of later fistula failure?",
         ["Cannulation within 14 days of creation", "Cannulation at 15 to 28 days", "Rope-ladder cannulation", "Ultrasound mapping"],
         0, "Relative risk 2.1 for cannulation within 14 days; observational evidence."),
        ("UKKA recommends investigation when non-maturity persists beyond how many weeks?",
         ["2 weeks", "6 weeks", "12 weeks", "26 weeks"],
         1, "Statement 3.9 (grade 1C): assess between 2 and 6 weeks and investigate non-maturity beyond 6."),
    ],
    "terms": [("Infiltration", "A needle passing through the vein wall, so blood leaks into tissue."),
              ("Side-branch ligation", "Tying off a branch vein to redirect flow into the main channel.")],
    "readings": [("dialysis-access-care.html", "Cannulation from the patient&rsquo;s and nurse&rsquo;s side."),
                 ("avf-aneurysm-and-changes.html", "How fistulas change with time and needling.")],
    "calcs": ["calc-av-fistula-maturation.html"],
}

import importlib.util as _u
from pathlib import Path as _P
_s = _u.spec_from_file_location("vs_quizutil", _P(__file__).resolve().parent / "quizutil.py")
_q = _u.module_from_spec(_s); _s.loader.exec_module(_q)
MODULE["quiz"] = _q.balance(MODULE["quiz"])
