# -*- coding: utf-8 -*-
"""Occupational and Physical Therapist (OT/PT) track of the Renal Care Academy (Ancillary Staff Track).
Built from the owner's handoff package (/Volumes/Storage/Renal Care Academy/OT-PT, v1, November 25, 2026) and the
improved blueprint v2 (OT-PT-BLUEPRINT-v2.md, same date). Every case, name, and identifier in the series is fictional.
Clinical, occupational therapy, physical therapy and payer-policy review status: draft. Do not deploy without the
owner's authorization. Rendered by generate_tech_courses.py; never hand-edit the pages."""
import html as _html
import json as _json
import re as _re
from pathlib import Path as _P

HUB = "occupational-physical-therapist"
_SRC = _P(__file__).resolve().parent / "src"

COURSE = {
    "title": "Occupational and Physical Therapist",
    "short": "OT/PT",
    "hub_slug": HUB,
    "label": "Renal rehabilitation track for licensed occupational and physical therapists",
    "tag": "Ancillary Staff",
    "icon": "🦵",
    "no_branch": True,
    "exam_stratify": True,
    "audience": ("Philippine-registered occupational therapists and physical therapists who see people with kidney disease &middot; "
                 "rehabilitation leads, physiatrists and renal teams who refer to them &middot; students on an observer pathway"),
    "audience_type": "Licensed occupational and physical therapists in renal care",
    "level": "Professional (licensed OT or PT); college reading level; two practice pathways plus an observer pathway",
    "review_date": "2026-11-25",
    "draw": 5,
    "mastery": "4 of 5",
    "exam_draw": 20,
    "keywords": ("renal rehabilitation course Philippines, physical therapy hemodialysis, occupational therapy kidney disease, "
                 "intradialytic exercise program, exercise for dialysis patients, falls prevention dialysis, frailty kidney failure, "
                 "kidney transplant prehabilitation, PhilHealth PMRS, RA 5680, RA 11241, renal care academy"),
    "page_title": "Occupational and Physical Therapist: Renal Rehabilitation Track",
    "desc": ("A free 20-module renal rehabilitation track for licensed occupational and physical therapists in the Philippines: why "
             "kidney failure makes movement expensive, how to screen and escalate safely, protect the access, measure function, "
             "design exercise and daily-life plans across CKD, hemodialysis, PD, AKI recovery and transplantation, and navigate "
             "PhilHealth rehabilitation pathways."),
    "h1": "Occupational and Physical <em>Therapist</em>",
    "sub": ("Kidney failure makes every movement cost more and every recovery take longer. This track teaches licensed OTs and PTs "
            "why, and what to do about it: screen before you move, protect the access, measure what matters, raise capacity, "
            "lower the demand of daily tasks, and work inside the renal team&rsquo;s plan."),
    "disclaimer": ("Educational material for licensed occupational and physical therapists. Completing it is an Academy learning "
                   "record only. It is not a PRC, DOH, PhilHealth or PSN credential, not CPD units, and not a workplace privilege. "
                   "Your license, your referral or prescription, your employer&rsquo;s privileges and the renal team&rsquo;s plan govern "
                   "what you may do."),
    "scope_note": ("Study material for licensed occupational therapists (RA 11241) and physical therapists (RA 5680) working with "
                   "people who have kidney disease. It explains the reasoning behind renal rehabilitation; it is not a hospital "
                   "protocol. It never authorizes changes to dialysis settings, handling of a needled access or catheter, medicine "
                   "decisions or benefit promises. Exercise parameters come from the referring physician and your unit&rsquo;s "
                   "agreed sheet: per unit protocol, but always ask the attending nephrologist&rsquo;s guidance. Every case, name and "
                   "number in the cases is fictional and illustrative."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Occupational and physical therapists",
    "branch_blurb": ("Renal rehabilitation for licensed OTs and PTs: safe screening, access protection, function testing, exercise, "
                     "fatigue, falls, home access and participation across CKD, dialysis, AKI recovery and transplantation."),
    "academy_meta": "20 modules &middot; OT and PT pathways &middot; a six-tool rehabilitation toolkit &middot; eight practical stations",
    "hero_alt": ("A Filipino physical therapist and an occupational therapist working with an older man on hemodialysis: one guides a "
                 "sit-to-stand from a dialysis chair, the other sets out a kitchen task on a low table."),
    "start_h2": "Movement is expensive in kidney failure. Your job is to make it affordable.",
    "start_html": """
<p>Ask a person on hemodialysis (HD) what they want back, and the answer is rarely a laboratory number. They want to walk to the jeepney stop without stopping, cook for their grandchildren, go back to work, climb to the third floor of their apartment, or simply get through a dialysis day without sleeping through the evening. Those are functional goals, and they are what occupational therapists (OTs) and physical therapists (PTs) are trained to restore.</p>
{{plain:Picture a household budget. Every task in a day costs energy, strength and balance. Healthy people earn far more than they spend. Kidney failure cuts the income: muscle shrinks, blood carries less oxygen, blood pressure wobbles when standing, nerves and bones weaken. Dialysis then takes twelve sitting hours a week and leaves a tired evening after each session. The person is left spending almost everything they have on ordinary tasks, with nothing in reserve.}}
<p>The picture has a limit. Energy is not one currency. A person may have enough aerobic capacity to walk but not enough leg strength to rise from a low chair, or enough strength but too little balance to turn safely. Your assessment finds which account is short. Then the two professions work from opposite sides of the same gap: <strong>physical therapy raises capacity</strong> (strength, endurance, balance, transfers), and <strong>occupational therapy lowers demand</strong> (pacing, routines, equipment, home and work redesign). The evidence is real: in the largest trial so far, twelve months of supervised exercise during dialysis improved how many times patients could stand up from a chair in a minute and how far they walked, while patients receiving usual care declined.[[otpt_andingrost2023]]</p>
{{fig:otpt00_capacity_gap}}
{{cards:What this track will help you do|Work inside your authority::Verify the referral or prescription, consent and the renal team&rsquo;s plan, and route dialysis decisions to the people who own them.|Screen before you move::Use a unit-agreed parameter sheet, recognize deterioration, stop, and hand over with SBAR.|Protect the access::Know what never touches a fistula arm or a catheter, and why compression clots a fistula.|Measure what matters::Gait speed, sit-to-stand, the Short Physical Performance Battery, six-minute walk, and occupational performance.|Raise capacity and lower demand::Design exercise, pacing, routines, equipment and home changes that fit the dialysis week.|Navigate the system::RA 5680, RA 11241, DOH rules and PhilHealth&rsquo;s rehabilitation pathway, without promising what you cannot deliver.}}
<p>Both professions study all twenty modules, because the patient needs both of you to understand the whole picture. Practice differs: OT learners demonstrate occupational analysis and adaptation; PT learners demonstrate mobility and exercise prescription. Each module has an opening case, real situations, a skills checklist for your preceptor, and a self-assessment drawn from a bank of ten questions.</p>
""",
    "is_not": ("It is a training track written independently from published laws, regulations, guidelines and research. It is not a "
               "PRC, DOH, PhilHealth or Philippine Society of Nephrology (PSN) credential, not continuing professional development "
               "(CPD) units, and not a workplace privilege. No PSN renal therapist certificate and no national dialysis OT or PT "
               "staffing ratio exists, and this track does not imply one. It sets no universal exercise-clearance numbers: those "
               "come from the referring physician and your unit&rsquo;s agreed parameters."),
    "pathways_tag": "Two practice pathways",
    "pathways_h2": "One renal foundation, two professions, five parts",
    "pathways_nav": "Pathways",
    "pathways_html": """
<p>Occupational and physical therapists learn the same renal foundations and then demonstrate different practice. Neither profession&rsquo;s pathway authorizes the other&rsquo;s interventions; in a module that emphasizes the other profession, you observe, analyze the co-referral, and produce the collaboration piece within your own scope.</p>
{{cards:Choose your pathway|Occupational therapist::All 20 modules. Practical stations OS01, OS02, OS03, OS04, OS05 and OS08: referral and readiness, access-safe transfer, deterioration response, occupational assessment and adaptation, fatigue and participation plan, and the integrated handoff.|Physical therapist::All 20 modules. Practical stations OS01, OS02, OS03, OS06, OS07 and OS08: referral and readiness, access-safe transfer, deterioration response, functional mobility assessment, exercise prescription and progression, and the integrated handoff.|Observer::Students and other staff study the modules and simulations and receive a knowledge record only, never a clinical competency sign-off.}}
{{cards:The five parts|Part 1 &middot; Foundations::Modules 1 to 5. The role and the referral, kidney disease as a functional problem, screening and escalation, access and infection, assessment and goals.|Part 2 &middot; Daily life and movement::Modules 6 to 10. Fatigue and routines, self-care and cognition, transfers and falls, exercise design, rehabilitation during hemodialysis.|Part 3 &middot; Across the pathway::Modules 11 to 14. Peritoneal and home dialysis, AKI and critical illness, transplantation, frailty, bone, neuropathy and limb loss.|Part 4 &middot; Participation and systems::Modules 15 to 19. Home and community, mental health and work, children and equity, Philippine governance and PhilHealth, documentation and quality.|Part 5 &middot; Capstone::Module 20. One integrated case and your profession&rsquo;s sign-off.}}
""",
    "modules_h2": "Twenty modules in five parts",
    "modules_intro": ("Study in order. Each module starts with what is happening in the body, moves to what the evidence shows and how "
                      "strong it is, and ends with what you do in your next session."),
    "syllabus_note": ("Each module plans five hours: two of guided study (classroom), two of case workshop and simulation (skills lab), "
                      "and one of supervised practice and portfolio work (placement). That is 100 hours in all, including the final "
                      "examination and practical stations in Module 20. These are Academy design proposals, not a PRC, DOH or "
                      "PhilHealth minimum."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions drawn at random from a bank of 10; a good target is 4 of 5 on two different sets. Every question explains why the best answer is best. The end-of-course examination draws one question from each of the twenty modules (20 in all); the proposed pass is 16, 80 percent.</p>
<p>Clinical completion needs more than the examination: every portfolio artifact, every <span class="tc-crit">Critical</span> checklist step demonstrated to a preceptor, and your profession&rsquo;s six practical stations at 8 of 10 or better with no critical failure. A critical failure is never averaged into a pass. The <a href="occupational-physical-therapist-trainer.html">trainer page</a> has the eight stations, the scoring rule, and ten printable working templates.</p>
""",
    "sources_html": """
<p>The track is built from published sources. Professional authority follows the Physical Therapy law (RA 5680) and the Philippine Occupational Therapy Law (RA 11241) through the Professional Regulation Commission;[[otpt_ra5680]][[otpt_ra11241]] facility duties follow DOH Administrative Order 2012-0001;[[otpt_doh2012]] and payer rules follow PhilHealth&rsquo;s rehabilitation circular and advisories.[[otpt_pc2025_0003]][[otpt_pa2025_0014]] Clinical frameworks follow the Kidney Disease: Improving Global Outcomes (KDIGO) 2024 chronic kidney disease guideline, the UK Kidney Association exercise and lifestyle guideline, and the International Society for Peritoneal Dialysis (ISPD) and Global Renal Exercise Network practice points.[[otpt_kdigo2024]][[otpt_baker2022]][[otpt_bennett2022]]</p>
<p>Statements about outcomes rest on peer-reviewed trials, cohorts and reviews, including the DiaTT, PEDAL, CYCLE-HD and EXCITE trials of exercise in dialysis, a Cochrane review, and cohorts on falls, fractures, cognition, depression and physical performance.[[otpt_andingrost2023]][[otpt_greenwood2021]][[otpt_grahambrown2021]][[otpt_manfredini2017]][[otpt_heiwe2011]][[otpt_cook2006]][[otpt_roshanravan2013]] Where evidence is observational, the text says &ldquo;associated with&rdquo;; where an outcome is a surrogate (a heart scan, a vein diameter), it says so. Regulatory statements were checked on November 25, 2026; confirm every circular&rsquo;s current status before you rely on it.</p>
""",
    "trainers_intro": ("A rehabilitation lead, a physiatrist, a senior OT or PT, or a renal nurse educator can use these modules as the guided-study part of a therapist&rsquo;s renal orientation. "),
    "trainer_h2": "Using the track to prepare a renal OT or PT",
    "trainer_audience": "Rehabilitation leads, physiatrists, senior occupational and physical therapists, renal nurse educators and attending nephrologists",
    "completion_html": """
<ul>
<li>Self-assessments: 4 of 5 on two different sets for each module, with every missed question reviewed.</li>
<li>Every portfolio artifact submitted (deidentified) and every <span class="tc-crit">Critical</span> step demonstrated to a preceptor in simulation or supervised practice.</li>
<li>Your profession&rsquo;s six practical stations at 8 of 10 or better, with no critical failure. OT: OS01, OS02, OS03, OS04, OS05, OS08. PT: OS01, OS02, OS03, OS06, OS07, OS08.</li>
<li>End-of-course examination: 16 of 20 or higher. Two sittings are proposed, separated by targeted review; after a second shortfall, the trainer writes an individual remediation plan.</li>
</ul>
<p>Completion is an Academy learning record. A clinical sign-off records the profession and the scope observed. It is not a PRC, DOH, PhilHealth or PSN credential, CPD units, or a workplace privilege.</p>
""",
    "related": [("calc-renal-rehabilitation-toolkit.html", "Six measurement tools for renal OT and PT practice."),
                ("exercise-guide-ckd.html", "The patient guide to exercise with kidney disease."),
                ("physical-activity-sports-ckd.html", "Physical activity and sports with CKD, for patients and families.")],
}


# ───────────────────────── trainer page: program, stations and printable templates ─────────────────────────
def _md_form(path):
    """The package's original blank templates (forms/*.md) as printable HTML."""
    lines = path.read_text(encoding="utf-8").splitlines()
    title = lines[0].lstrip("# ").strip()
    note, fields = "", []
    for ln in lines[1:]:
        ln = ln.strip()
        if not ln or set(ln) == {"_"}:
            continue
        m = _re.match(r"\*\*(.+)\*\*$", ln)
        if m:
            fields.append(m.group(1))
        elif not note:
            note = ln
    rows = "".join(f"<tr><td><strong>{_html.escape(f)}</strong></td><td style=\"min-width:55%\">&nbsp;</td></tr>" for f in fields)
    return (f'  <h3 class="nc-print-break">{_html.escape(title)}</h3>\n  <p>{_html.escape(note)}</p>\n'
            f'  <div class="table-wrap"><table class="nc-sign"><tbody>{rows}</tbody></table></div>')


def _stations():
    st = _json.loads((_SRC / "osce-stations.json").read_text(encoding="utf-8"))
    out = []
    for s in st:
        items = "".join(f"<tr><td>{_html.escape(i)}</td><td></td><td></td><td></td></tr>" for i in s["items"])
        mods = ", ".join(f"Module {int(x[1:])}" for x in s["module_ids"])
        out.append(f'  <h3 class="nc-print-break">{s["id"]} &middot; {_html.escape(s["title"])} ({_html.escape(s["role"])})</h3>\n'
                   f'  <p>{mods}. {s["minutes"]} minutes. Score each item 0, 1 or 2; pass {s["pass_score"]} of {s["max_score"]} with no critical failure.</p>\n'
                   f'  <div class="table-wrap"><table class="nc-sign"><thead><tr><th>Item</th><th>0</th><th>1</th><th>2</th></tr></thead><tbody>{items}</tbody></table></div>\n'
                   f'  <div class="tc-stop"><span class="tc-lab">Critical failure</span>{_html.escape(s["critical_failure"])}</div>')
    return "\n".join(out)


_FORMS = "\n".join(_md_form(p) for p in sorted((_SRC / "forms").glob("*.md")))

COURSE["trainer_html"] = """
<p>The track supports orientation; it does not replace it. A practical plan is eight weeks at two to three modules a week, each paired with a supervised session in the learner&rsquo;s own service using deidentified or simulated cases, then observed practice as real referrals allow. Pair an OT and a PT educator where you can, and bring a dialysis nurse into every access and intradialytic simulation and a physician or designated medical reviewer into every escalation debrief.</p>
{{flow:Suggested eight-week sequence|Week 1::Modules 1 to 3. Scope and readiness decisions; build your unit&rsquo;s parameter sheet with the nephrologist.|Week 2::Modules 4 and 5. Access safety and a baseline battery on a colleague.|Week 3::Modules 6 to 8. Fatigue, daily-living and mobility plans.|Week 4::Modules 9 and 10. An exercise prescription and an intradialytic activity plan.|Week 5::Modules 11 to 13. Home dialysis, acute care and transplant pathways.|Week 6::Modules 14 and 15. Multimorbidity and an environment plan.|Week 7::Modules 16 to 18. Participation, equity and governance.|Week 8::Modules 19 and 20. An audit, the examination and the capstone stations.}}
<p><strong>Scoring the stations.</strong> Each station allows 12 minutes: 2 to read, 8 to perform, 2 for feedback. Score each of five items 0 (absent or unsafe), 1 (incomplete or prompted) or 2 (complete, accurate and independent). Pass is 8 of 10 with no critical failure. Apply the critical-failure rule even when the total is high, stop the station, debrief, retrain, and reassess on a different case.</p>
<p><strong>Protect patients while learners learn.</strong> Use simulation before real encounters. The responsible clinician confirms consent, readiness and supervision. A supervisor may stop any task for safety. Learners never act outside their license or local privileges.</p>
</section>

<section class="section" id="stations">
  <div class="section-tag">Printable</div>
  <h2>The eight practical stations</h2>
""" + _stations() + """
</section>

<section class="section" id="templates">
  <div class="section-tag">Printable</div>
  <h2>Ten working templates</h2>
  <p>Original Academy learning templates for supervised practice and local adaptation. They are not official PhilHealth or DOH forms; keep official eligibility and authorization forms as links to the current agency source. Keep identifiable patient data only in the approved clinical record.</p>
""" + _FORMS + "\n"

COURSE["hub_sections"] = [
    {"id": "authority", "before": "modules", "nav": "Authority", "tag": "Before you begin",
     "h2": "Your license, your referral, and the renal team&rsquo;s plan",
     "html": """
<p>Three things must be true before you treat anyone in this track. First, you hold current Professional Regulation Commission (PRC) registration: physical therapists under Republic Act (RA) 5680, occupational therapists under RA 11241, which made occupational therapy a separate regulated profession in 2019.[[otpt_ra5680]][[otpt_ra11241]] Second, the referral is in place: RA 5680 requires a physician&rsquo;s prescription for PT treatment, and OT works on referral within RA 11241 and current PRC rules. Third, the renal team&rsquo;s plan says what is safe today. A dialysis unit must have competent staff, medical oversight and safe systems under DOH Administrative Order 2012-0001, but that order sets no renal OT or PT staffing ratio.[[otpt_doh2012]]</p>
{{call:You never change ultrafiltration, dialysate or any machine setting, touch a needled access or catheter, give or adjust a medicine, or promise PhilHealth coverage. When exercise and dialysis conflict, stop and call: per unit protocol, but always ask the attending nephrologist&rsquo;s guidance.}}
"""},
]

P1, P2, P3, P4, P5 = ("Part 1 &middot; Foundations", "Part 2 &middot; Daily life and movement", "Part 3 &middot; Across the kidney care pathway",
                      "Part 4 &middot; Participation and systems", "Part 5 &middot; Capstone")
_HB = ("Illustrated clinical vignette, warm natural light, Filipino therapists, patients and families, modern Philippine hospital "
       "rehabilitation and dialysis settings, no text and no legible names or numbers in image. ")

_ROWS = [
    ("01", "role-scope-and-referral", "The Renal Therapist Role and the First Referral", P1,
     "Why function predicts outcomes in kidney disease, what an OT and a PT each own, and how to read a referral before you touch a patient.",
     "An occupational therapist and a physical therapist reading a referral together at a rehabilitation desk beside a dialysis unit doorway."),
    ("02", "kidney-disease-and-function", "Kidney Disease Through a Functional Lens", P1,
     "The capacity&ndash;demand gap: how muscle wasting, anemia, acidosis, fluid shifts, neuropathy and bone disease turn into slow walking and hard stairs.",
     "A therapist and an older man on a landing halfway up a hospital staircase, the man resting a hand on the rail."),
    ("03", "screening-and-escalation", "Screen Before Movement and Respond to Deterioration", P1,
     "Why blood pressure falls on standing after dialysis, why a normal pulse can mislead, the unit parameter sheet, and stopping with SBAR.",
     "A physical therapist kneeling beside a seated patient and asking how he feels before a walk, a nurse nearby."),
    ("04", "vascular-access-and-infection", "Protect Vascular Access and Prevent Infection", P1,
     "How a fistula works and why pressure clots it, catheter rules, what exercise can and cannot do for a new fistula, and infection control for shared equipment.",
     "An occupational therapist showing a patient a soft hand-squeeze exercise with the fistula arm resting free and uncovered."),
    ("05", "assessment-and-shared-goals", "Assess Function and Agree Measurable Goals", P1,
     "Gait speed, sit-to-stand, the Short Physical Performance Battery, the six-minute walk and occupational performance, turned into goals the patient chose.",
     "A therapist timing a patient's walk along a taped four-meter course in a bright corridor."),
    ("06", "fatigue-pacing-and-participation", "Manage Fatigue and Rebuild Daily Routines", P2,
     "Why dialysis days drain people, recovery time after a session, the deconditioning spiral, and energy budgeting that protects what matters most.",
     "An occupational therapist and a middle-aged woman planning a week on a large paper calendar at a kitchen table."),
    ("07", "adl-cognition-and-self-management", "Support Self-Care, Cognition and Treatment Routines", P2,
     "Cognitive impairment that nobody has diagnosed, health literacy, and routines for medicines, fluids and daily care that survive a tired day.",
     "An occupational therapist watching an older man sort tablets into a labeled pill organizer while his daughter looks on."),
    ("08", "transfers-gait-and-falls", "Transfers, Gait and Falls Prevention", P2,
     "Why people on dialysis fall after sessions, fracture more, and fear walking, and how to make transfers and walking safe.",
     "A physical therapist guarding an older woman with a walker as she steps away from a dialysis chair."),
    ("09", "exercise-design-and-progression", "Design and Progress an Individualized Exercise Plan", P2,
     "What training does to uremic muscle and heart, FITT-VP in kidney failure, effort-based intensity, and progression that survives a dialysis week.",
     "A patient doing seated knee extensions with an ankle weight while a physical therapist counts."),
    ("10", "intradialytic-rehabilitation", "Rehabilitation During Hemodialysis", P2,
     "When and how to exercise in the chair, what DiaTT and PEDAL each showed, and how to build a program patients actually keep.",
     "A patient pedaling a small bed cycle attached to a reclining dialysis chair, the machine in soft focus."),
    ("11", "peritoneal-and-home-dialysis", "Daily Function with Peritoneal and Home Dialysis", P3,
     "Pressure inside a full abdomen, protecting the catheter and exit site, timing activity around dwells, and lifting, work and sport at home.",
     "A man on peritoneal dialysis and an occupational therapist practicing a safe lift of a dialysis solution box from a low shelf."),
    ("12", "aki-hospital-and-icu-recovery", "AKI Hospitalization and Recovery After Critical Illness", P3,
     "Intensive care unit-acquired weakness, early mobility with lines in place, and why recovery from AKI and critical illness takes months.",
     "Two therapists helping a weak man sit at the edge of an intensive care bed with a continuous kidney replacement machine nearby."),
    ("13", "transplant-prehabilitation-and-recovery", "Transplant Prehabilitation and Recovery", P3,
     "Why frailty matters before a transplant, prehabilitation while waiting, and safe lifting and return to activity after surgery.",
     "A kidney transplant candidate doing step-ups on a low platform in a rehabilitation gym while a physical therapist coaches."),
    ("14", "frailty-bone-neuropathy-and-limb-loss", "Frailty, Bone Disease, Neuropathy and Limb Loss", P3,
     "The frail dialysis patient, fragile bones, numb feet, and amputation: assessment and rehabilitation when several problems stack up.",
     "A physical therapist checking the fit of a below-knee prosthesis on a seated man in a rehabilitation clinic."),
    ("15", "home-equipment-and-community-access", "Home Equipment and Community Access", P4,
     "The person&ndash;environment fit: stairs, toilets, bathing, commuting to dialysis, and equipment that costs little and helps a lot.",
     "An occupational therapist measuring a narrow bathroom doorway in a Filipino home while the family watches."),
    ("16", "mental-health-work-and-supportive-care", "Mental Health, Work and Supportive Kidney Care", P4,
     "Depression and symptom burden, returning to work around dialysis, and rehabilitation goals in conservative and end-of-life care.",
     "An occupational therapist and a man in work clothes reviewing a shift schedule beside a dialysis calendar."),
    ("17", "children-equity-and-remote-care", "Children, Equity and Remote Rehabilitation", P4,
     "Play, school and growth in children with kidney disease, barriers of distance and cost, and what remote rehabilitation can and cannot do.",
     "A pediatric therapist playing a balance game with a school-age child while a parent watches in a bright clinic."),
    ("18", "philippine-governance-and-philhealth", "Philippine Governance and PhilHealth Rehabilitation Pathways", P4,
     "Who authorizes what: RA 5680, RA 11241, DOH dialysis rules, and PhilHealth&rsquo;s rehabilitation package and its limits.",
     "A rehabilitation coordinator and a therapist reviewing printed circulars with colored tabs at an office desk."),
    ("19", "documentation-quality-and-international-models", "Documentation, Quality and International Service Models", P4,
     "Notes that carry the decision, measures that show improvement, and what to borrow from the United States, United Kingdom, Australia and Canada.",
     "Two therapists reviewing a run chart of patient sit-to-stand scores on a monitor in a quiet office."),
    ("20", "integrated-capstone", "Integrated Renal Rehabilitation Capstone", P5,
     "One patient, every skill: a near fall, fatigue, a new fistula and a PhilHealth question, assessed through your profession&rsquo;s stations.",
     "An occupational therapist and a physical therapist presenting a case plan to a small team in a training room."),
]
MODULES = []
for _id, _slug, _title, _part, _sub, _brief in _ROWS:
    _row = {"id": _id, "slug": _slug, "title": _title, "sub": _sub, "part": _part, "hours": (2, 2, 1),
            "card_img": f"{HUB}-{_id}-card.webp", "hero_brief": _HB + _brief}
    if not (_P(__file__).resolve().parent / f"m{_id}.py").exists():   # a module shows as "in preparation" until written
        _row["status"] = "planned"
    MODULES.append(_row)
