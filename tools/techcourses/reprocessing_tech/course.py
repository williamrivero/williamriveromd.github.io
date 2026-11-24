# -*- coding: utf-8 -*-
"""Dialyzer Reprocessing Technician: a Nephrology Nursing subtrack, in the POD/PD package schema.
Blueprint: /Volumes/Storage/Renal Care Academy/Reprocessing Technician/REPROCESSING_TECHNICIAN_BLUEPRINT_v1.0.md
(supersedes the v0.1 handoff package of November 25, 2026). One canonical proficiency (RCM-DIALYZER-REPROCESSING)
shared with the Dialysis Technician and Biomedical Equipment Technician tracks. Every case, name and identifier is fictional.
Modules m01.py to m12.py are authored natively; hours are (theory, skills lab, supervised workplace) = 84, 60, 336."""

HUB = "dialyzer-reprocessing-technician"
TOOLKIT = "calc-reprocessing-technician-toolkit.html"

COURSE = {
    "title": "Dialyzer Reprocessing Technician",
    "short": "Reprocessing Technician",
    "hub_slug": HUB,
    "label": "Nephrology Nursing subtrack for the dialyzer reuse room",
    "tag": "Nephrology Nursing &middot; Role subtrack",
    "icon": "♻️",
    "no_branch": True,
    "audience": ("Reprocessing operators and dialysis technicians in Philippine hemodialysis units &middot; biomedical technicians who service reprocessors &middot; "
                 "head nurses and medical directors who supervise reuse programs"),
    "audience_type": "Dialyzer reprocessing technicians",
    "level": "High-school graduates in supervised training; written in plain language",
    "review_date": "2026-11-25",
    "draw": 5,
    "mastery": "4 of 5",
    "exam_draw": 40,
    "keywords": ("dialyzer reprocessing technician Philippines, dialyzer reuse training, total cell volume TCV 80 percent, PhilHealth dialyzer five uses, "
                 "peracetic acid dialyzer reuse, hemodialyzer reprocessing course, dialysis reuse technician, AAMI RD47, Renal Care Academy"),
    "page_title": "Dialyzer Reprocessing Technician: A Renal Care Academy Track",
    "desc": ("A free twelve-module track for the dialyzer reuse room: the dialyzer and the evidence on reuse, Philippine rules, infection and chemical "
             "safety, water, identity and custody, cleaning, testing, storage and handoff, equipment faults, and quality. Cases, skills checklists, "
             "a self-assessment in every module, and a training toolkit."),
    "h1": "Dialyzer Reprocessing <em>Technician</em>",
    "sub": ("A track for the people who clean, test and return a patient&rsquo;s own dialyzer. Learn why every gate exists, and why one failed gate "
            "stops the dialyzer no matter how many others pass."),
    "disclaimer": ("Educational study material. Completing it is an Academy learning record only. It is not a DOH, PSN, PhilHealth, TESDA or PRC credential, "
                   "it does not authorize anyone to release a dialyzer, and it does not replace the unit&rsquo;s approved reuse program, the device and germicide "
                   "instructions for use, or supervised practice."),
    "scope_note": ("This module is study material for dialyzer reprocessing. It explains the reasoning behind each step; it is not a procedure. "
                   "Concentrations, contact times, storage limits and test thresholds come from the germicide and dialyzer instructions for use and your unit&rsquo;s "
                   "validated procedure, never from this page. The medical director decides who is eligible for reuse; the nurse decides whether a dialyzer is used "
                   "on a patient. Every case, name and identifier is fictional. Pending clinical review."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Role subtrack &middot; technicians",
    "branch_blurb": ("For the reuse room: the dialyzer, the rules, infection and chemical safety, water, identity, cleaning, testing, storage and handoff, "
                     "equipment faults, and quality. Shared with the Dialysis Technician and Biomedical tracks."),
    "parent": ("nephrology-nursing.html", "Nephrology Nursing",
               "The parent course. The reuse room is part of the nursing service that the head nurse and medical director supervise."),
    "academy_meta": "12 modules &middot; 480 planned hours &middot; a six-tool training toolkit",
    "hero_alt": "A Filipino reprocessing technician in a face shield and gown checking the label of a hollow-fiber dialyzer at a clean reprocessing station.",
    "start_h2": "The room behind the dialysis floor",
    "start_html": f"""
<p>Many Philippine hemodialysis units reuse each patient&rsquo;s dialyzer. After a session it goes to a small room behind the floor, where a technician rinses it, cleans it, tests it, fills it with germicide, labels it, and stores it until the same patient returns. Done well, reuse is uneventful. Done badly, it has given patients fever and rigors, bloodstream infection, hepatitis C, and a dose of disinfectant.[[rt_beck1990]][[rt_duong2016]][[rt_roth2000]]</p>
<p>The outcome studies of reuse are weak in both directions. The harms that are well documented come from execution: a germicide mixed unevenly, water that was not clean, a label that was not checked.[[rt_galvao2012]][[rt_roth2000]] That is the technician&rsquo;s work, and it is why this track exists.</p>
{{{{cards:What this track will help you do|Understand::Explain what a dialyzer does, what clotting and germicide do to it, and what the evidence on reuse shows.|Work safely::Keep clean and dirty apart, handle germicides, and protect yourself.|Prove each gate::Identity, eligibility, water, cleaning, volume, integrity, disinfection, storage, rinse and residual test, each with a record.|Stop::Quarantine a dialyzer, a batch, or the whole room when the evidence fails.|Hand off::Return the right dialyzer to the right nurse for the right patient, with two people checking.|Improve::Read the room&rsquo;s numbers without rewarding unsafe reuse.}}}}
<p>The rule that runs through all twelve modules: <strong>if you cannot prove it, do not release it.</strong> The track pairs with the <a href="{TOOLKIT}">Reprocessing Technician Toolkit</a>, six training calculators that never give a release decision.</p>
""",
    "is_not": ("It is study material written independently from Philippine issuances, international standards and published research. It is not a license, "
               "a TESDA qualification, PSN technician training, or a PhilHealth staffing credential. PSN guidance expects dialysis technicians to complete a "
               "structured training program of three months or longer;[[psn2024]] this track can form the guided-study part of such a program but is not that program. "
               "It does not authorize the release of any dialyzer: that authority is granted by the facility after an observed practical assessment on its own equipment."),
    "pathways_tag": "Three pathways, one proficiency",
    "pathways_h2": "One body of knowledge, three jobs",
    "pathways_nav": "Pathways",
    "pathways_html": """
<p>Reprocessing is one technical competency shared by several jobs. The track teaches it once. What each job may do with it differs.</p>
<div class="table-wrap"><table>
<thead><tr><th>Pathway</th><th>Who</th><th>Emphasis</th><th>What completion never grants</th></tr></thead>
<tbody>
<tr><td><strong>Reprocessing operator</strong></td><td>Staff hired into the reuse room</td><td>All twelve modules; workplace hours in receiving, processing, testing, storage and handoff</td><td>Release authority, which the facility grants after the operator practical assessment</td></tr>
<tr><td><strong>Dialysis Technician</strong></td><td>Learners on the Dialysis Technician track</td><td>Builds on Dialysis Technician Module 11; adds the evidence, water, germicide and acceptance-gate depth</td><td>Credit for Modules 7 to 10 by title similarity alone</td></tr>
<tr><td><strong>Biomedical Equipment Technician</strong></td><td>Staff who service reprocessors and water systems</td><td>Modules 1 to 6 and 11; the 96 processing hours become setup verification, measurement assurance and fault analysis</td><td>Any clinical release authority</td></tr>
</tbody></table></div>
<p>A person who holds two roles must pass both practical gates.</p>
""",
    "modules_h2": "Twelve modules, 480 planned hours",
    "modules_intro": ("Study the modules in order. Each one starts from a plain picture, moves to the mechanism and the evidence, and ends with what you do "
                      "at the bench, in the record, and when something fails."),
    "syllabus_note": ("Theory 84 hours, skills lab 60 hours, supervised workplace 336 hours, over at least three calendar months. These are academy design "
                      "proposals, not requirements of any regulator. Extend supervised practice until competence is demonstrated."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions drawn from a bank of 12. The mastery mark is 4 of 5 on two different sets. The questions are for learning; they show what to reread, not whether you can do the work.</p>
<div class="table-wrap"><table>
<thead><tr><th>Milestone</th><th>What it involves</th><th>Who records it</th></tr></thead>
<tbody>
<tr><td><strong>1 &middot; Knowledge</strong></td><td>All twelve self-assessments and the end-of-track examination (40 questions from all banks)</td><td>You, in your own learning record</td></tr>
<tr><td><strong>2 &middot; Faculty check</strong></td><td>Short-answer questions marked by a person and kept off the public pages</td><td>Nurse educator or chief technician</td></tr>
<tr><td><strong>3 &middot; Supervised practice</strong></td><td>Workplace hours on the unit&rsquo;s own reprocessor, logged with the equipment model and SOP version</td><td>Assessor</td></tr>
<tr><td><strong>4 &middot; Practical assessment</strong></td><td>Six observed full cycles, including one failed volume test and one failed integrity test handled correctly; two two-person handoffs; one water sample; one splash drill</td><td>Assessor, every critical item met</td></tr>
<tr><td><strong>5 &middot; Facility authorization</strong></td><td>A written decision by the facility on the scope you may perform</td><td>Medical director or designate</td></tr>
</tbody></table></div>
<p>A score never hides a critical failure. Watching a video, ticking a box, or time on a page is not observed performance. Milestone 5 is a decision made outside this website.</p>
""",
    "sources_html": """
<p>Philippine requirements follow the Department of Health (DOH) licensing order for dialysis facilities and its water monitoring order, the Philippine Society of Nephrology (PSN) hemodialysis guidelines, and PhilHealth&rsquo;s hemodialysis circulars.[[doh2012]][[doh_water]][[psn2024]][[rt_phic0023]][[rt_phic0029]] International comparisons use the United States conditions for coverage and Malaysia&rsquo;s 2026 national standards, each labeled with its country.[[rt_cfr494]][[rt_my2026]] Technical content follows the reprocessing standard of the Association for the Advancement of Medical Instrumentation (AAMI) and the ISO 23500 series for dialysis fluids.[[aami_reuse]][[iso23500_3]]</p>
<p>The research behind the teaching is cited in each module: outcome studies of reuse, the clearance analysis of the Hemodialysis (HEMO) Study, outbreak investigations by the Centers for Disease Control and Prevention (CDC), and occupational exposure studies.[[rt_galvao2012]][[rt_cheung1999]][[rt_beck1990]][[rt_casey2017]] Where the evidence is strong, the text says so; where it rests on observation or a single small study, it says that instead.</p>
<p>Reconfirm the PhilHealth circulars, the DOH water order details and the editions of the AAMI and ISO standards your facility follows before any compliance decision.</p>
""",
    "trainers_intro": "A head nurse, chief technician or medical director can use these modules as the guided-study part of a reuse-room training program. ",
    "trainer_h2": "Running the track in your unit",
    "trainer_html": """
<p><strong>Preparation.</strong> Obtain the approved reuse program, the reprocessor operating manual, the germicide and dialyzer instructions for use, the safety data sheets, and blank logs. Use training dialyzers and synthetic labels (for example, RU-0412) until workplace eligibility is confirmed. Never use patient identifiers in classroom material.</p>
{{flow:Suggested sequence|Weeks 1 and 2::Modules 1 to 4; induction, safety orientation, observation in the reuse room.|Weeks 3 and 4::Modules 5 to 7; water sampling lab, germicide handling lab, receiving and labeling practice.|Weeks 5 and 6::Modules 8 and 9; cleaning and testing on training dialyzers, then supervised cycles.|Weeks 7 and 8::Module 10; storage, rinse, residual testing and two-person handoffs.|Weeks 9 and 10::Module 11; calibration walk-through, fault and quarantine drills, power and water failure drill.|Weeks 11 to 13 or later::Module 12; audit exercise, capstone, remaining supervised hours, practical assessment.}}
<p>Record each observation with the learner, date, equipment model, SOP version, simulated or real, critical items met, and the assessor&rsquo;s signature, in the facility&rsquo;s own system. Reassess after a change of device or germicide, a serious incident, a long absence, and yearly.</p>
""",
    "completion_html": """
<ul>
<li>Self-assessments at 4 of 5 on two different sets for each module, with missed questions reviewed.</li>
<li>The end-of-track examination and the faculty short-answer check.</li>
<li>All supervised workplace hours logged, and every critical item of the practical assessment met.</li>
<li>A written facility authorization stating the scope you may perform.</li>
</ul>
<p>Completing the Academy track is a learning record. It does not authorize the release of a dialyzer.</p>
""",
    "related": [(TOOLKIT, "Six training calculators: volume retained, use counter, germicide dilution, contact and storage clock, water log, and a monthly audit."),
                ("dialyzer-reprocessing-reuse.html", "The site&rsquo;s reference guide to dialyzer reprocessing and reuse."),
                ("dialysis-water-treatment-systems.html", "How dialysis water is made and monitored.")],
}

P1 = "Part 1 &middot; Foundations"
P2 = "Part 2 &middot; Safety and supplies"
P3 = "Part 3 &middot; The cycle"
P4 = "Part 4 &middot; When things go wrong, and getting better"

_ROWS = [
    ("01", "role-scope-and-the-team", "The Reuse Room and Your Place in It", P1, (8, 6, 24),
     "One proficiency and three jobs, who decides what, the limits of your scope, and what to do when two people disagree about a dialyzer."),
    ("02", "dialyzer-science-and-evidence", "The Dialyzer and Why Reuse Exists", P1, (6, 2, 0),
     "How a dialyzer cleans blood, what clotting and germicides do to it, and what the research on reuse does and does not show."),
    ("03", "rules-and-jurisdictions", "The Rules: Philippine Governance and Other Countries", P1, (6, 4, 0),
     "DOH, PSN and PhilHealth requirements, how other countries differ, and why the strictest rule that applies wins."),
    ("04", "infection-and-occupational-protection", "Infection Prevention and Protecting Yourself", P2, (6, 4, 0),
     "How bloodborne viruses spread in a dialysis unit, clean and dirty flow, protective equipment, eligibility by infection status, and exposure response."),
    ("05", "water-for-reprocessing", "Water for Reprocessing", P2, (6, 6, 40),
     "Why water quality matters even more in the reuse room, the DOH monitoring schedule, ISO limits and action levels, and sampling."),
    ("06", "germicides-and-chemical-safety", "Germicides and Chemical Safety", P2, (6, 4, 0),
     "How the common germicides kill, why mixing and potency matter, and how to protect your lungs, eyes and skin."),
    ("07", "identity-and-chain-of-custody", "Identity and Chain of Custody", P3, (4, 4, 40),
     "Labels, two identifiers, similar names, transport, and a use count that is never reset."),
    ("08", "receiving-and-cleaning", "Receiving, Rinsing and Cleaning", P3, (6, 6, 48),
     "Time to processing, rinsing and reverse ultrafiltration, header cleaning, cleaning agents, and what the approved procedure controls."),
    ("09", "testing-and-acceptance", "Performance Testing and Acceptance", P3, (6, 4, 48),
     "Total cell volume and its baseline, the integrity test, inspection, independent acceptance gates, and repeats without gaming."),
    ("10", "disinfection-storage-and-handoff", "Disinfect, Store, Rinse and Hand Off", P3, (10, 8, 48),
     "Germicide fill and contact time, storage and expiry, rinsing, presence and residual tests, and two-person verification with the nurse."),
    ("11", "equipment-incidents-and-continuity", "Machines, Faults and When Things Go Wrong", P4, (12, 6, 40),
     "Reprocessor calibration, service boundaries, tracing dialyzers after a fault, reactions in patients, quarantine, and power or water failure."),
    ("12", "records-quality-and-capstone", "Records, Quality and the Capstone", P4, (8, 6, 48),
     "What a complete record proves, audits, reuse numbers without perverse incentives, waste, and the integrated capstone."),
]

# Modules held as "In preparation" until all their images are produced and wired (hero + figures A and B).
_PENDING = set()

MODULES = []
for _id, _slug, _title, _part, _hrs, _sub in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part, "hours": _hrs,
                    "card_img": f"{HUB}-{_id}-card.webp"})
    if _id in _PENDING:
        MODULES[-1]["status"] = "planned"
