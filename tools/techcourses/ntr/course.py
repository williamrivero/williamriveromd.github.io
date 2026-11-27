# -*- coding: utf-8 -*-
"""Nephrology Fellow / Resident / Medical Intern (NTR) track: course definition in the Physician on Duty (POD) package schema.
Built from Blueprint v2 (November 27, 2026): 36 modules, six learner pathways (medical intern, internal medicine resident,
pediatric resident, adult nephrology fellow, pediatric nephrology fellow), adapted to Philippine practice. Pediatric
pathways take their pediatric depth from the Attending Pediatric Nephrologist track. Clinical content is a draft pending
Dr. Rivero's sign-off. Every case is fictional."""
import json as _json
from pathlib import Path as _Path

HUB = "nephrology-trainee"
_HB = "Illustrated clinical vignette, warm natural light, Filipino physicians in training and patients, no text in image. "

_PATHWAYS = """
<div class="table-wrap"><table><thead><tr><th>Pathway</th><th>Who it is for</th><th>Required modules</th><th>About</th></tr></thead><tbody>
<tr><td><strong>Medical Intern</strong></td><td>Post-graduate interns on a medicine or pediatrics rotation, before the Physician Licensure Examination</td><td>1&ndash;9, 11&ndash;13, 16, 20, 22, 25&ndash;26, 32&ndash;34, 36 (21 modules)</td><td>4 weeks, ~42 hours</td></tr>
<tr><td><strong>Internal Medicine Resident</strong></td><td>Residents in Philippine College of Physicians (PCP)-accredited programs, on the renal rotation, in the intensive care unit (ICU), or covering dialysis</td><td>All except 18, 19, 29 and 30 (32 modules)</td><td>8&ndash;12 weeks, ~64 hours</td></tr>
<tr><td><strong>Pediatric Resident</strong></td><td>Residents in Philippine Pediatric Society (PPS)-accredited programs</td><td>1&ndash;9, 11, 16, 20&ndash;22, 26, 32&ndash;34, 36 (19 modules), with Attending Pediatric Nephrologist modules 2, 3, 4, 7, 9 and 15 recommended</td><td>6 weeks, ~38 hours</td></tr>
<tr><td><strong>Adult Nephrology Fellow</strong></td><td>Fellows in Philippine Society of Nephrology (PSN)-accredited training institutions</td><td>All 36 modules</td><td>Overlay on the 24-month fellowship, ~110 hours</td></tr>
<tr><td><strong>Pediatric Nephrology Fellow</strong></td><td>Fellows in Pediatric Nephrology Society of the Philippines (PNSP)-accredited programs</td><td>1&ndash;10, 16, 17, 22, 26, 31&ndash;36 (20 modules), plus all 29 <a href="attending-pediatric-nephrologist.html">Attending Pediatric Nephrologist</a> modules as the pediatric spine</td><td>Overlay on the fellowship, ~60 hours here</td></tr>
</tbody></table></div>
<p>Every module is open to everyone. The pathway only sets what counts as required for your own study record. Hours are study estimates, not CPD units or training hours, and your clinical rotations come on top of them.</p>
{{cards:A fellow&rsquo;s 24-month overlay (themes, not rotation assignments)|Months 1&ndash;3::Acute core: Modules 1 to 10.|Months 4&ndash;6::CKD clinic and medicines: Modules 11 to 16.|Months 7&ndash;9::Hemodialysis and access: Modules 22 to 26.|Months 10&ndash;12::Peritoneal dialysis and the annual review: Modules 27 and 28.|Months 13&ndash;15::Glomerular and systemic disease: Modules 17 to 21.|Months 16&ndash;18::Transplant and critical care: Modules 29 to 31, and Module 10 again.|Months 19&ndash;21::Supportive care, governance, PhilHealth and research: Modules 32 to 35.|Months 22&ndash;24::Capstone and teaching: Module 36.}}
"""

COURSE = {
    "title": "Nephrology Fellow / Resident / Medical Intern",
    "short": "Nephrology Trainee",
    "hub_slug": HUB,
    "label": "Training track for nephrology fellows, residents and medical interns",
    "tag": "Renal Care Physicians",
    "icon": "🩺",
    "no_branch": True,
    "audience": ("Adult and pediatric nephrology fellows &middot; internal medicine and pediatric residents &middot; medical interns "
                 "on medicine, pediatrics, ICU and dialysis rotations, and residents who work shifts as dialysis physicians on duty"),
    "audience_type": "Nephrology fellows, residents and medical interns",
    "level": "Physicians in training, from intern to fellow, written in plain language",
    "review_date": "2026-11-27",
    "draw": 5,
    "mastery": "4 of 5",
    "keywords": ("nephrology fellowship Philippines, PSN accredited training, PNSP pediatric nephrology fellowship, internal medicine residency renal rotation, "
                 "medical intern nephrology, AKI leptospirosis dengue, dysnatremia correction limit, hyperkalemia, KDIGO 2024 CKD, KDIGO 2026 anemia, "
                 "SGLT2 inhibitor finerenone semaglutide CKD, hemodialysis prescription Kt/V, PD peritonitis ISPD 2022, kidney transplant referral, "
                 "physician on duty dialysis, PhilHealth 156 hemodialysis sessions, renal POCUS VExUS"),
    "page_title": "Nephrology Fellow / Resident / Medical Intern: A Training Track",
    "desc": ("A free 36-module training track for nephrology fellows, residents and medical interns in the Philippines: renal physiology and "
             "the consult, fluids and electrolytes, AKI including tropical causes, ICU dialysis, CKD and kidney protection, glomerular disease, "
             "hemodialysis, PD, transplant, supportive care, PhilHealth and Philippine rules. Six pathways, adult and pediatric."),
    "h1": "Nephrology Fellow / Resident / <em>Medical Intern</em>",
    "sub": ("One track for everyone learning kidney medicine on the ward, in the ICU and in the dialysis unit, from the intern who first notices "
            "the falling urine output to the fellow who decides what happens next. Choose your pathway; every module tells you what is yours "
            "to do at your stage."),
    "disclaimer": ("Educational self-study for physicians in training. Clinical tasks need your institution&rsquo;s authorization and supervision. "
                   "Completing this track is an Academy learning record only. It does not confer licensure, specialist status, PSN or PNSP "
                   "membership or board eligibility, procedural privileges, CPD units, or completion of an institutional training program, "
                   "and it does not replace current guidelines, regulations, your institution&rsquo;s protocols and formulary, or your supervisor."),
    "scope_note": ("Study material for medical interns, residents and fellows. It explains the reasoning behind common decisions; it is not a "
                   "protocol and gives no drug doses. Doses, rates and order sets come from current guidelines, product labels, your "
                   "institution&rsquo;s approved protocols and your supervising physician. Benefit rules change: confirm them on the date of "
                   "service. Every case is fictional."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Fellows, residents and interns",
    "branch_blurb": ("For nephrology fellows (adult and pediatric), residents and medical interns: physiology and the consult, fluids and "
                     "electrolytes, AKI, CKD, glomerular disease, HD, PD, transplant, supportive care and Philippine practice."),
    "academy_meta": "36 modules &middot; six pathways, adult and pediatric &middot; calculators in every module",
    "hero_alt": "A nephrology fellow, an internal medicine resident and a medical intern review a patient's chart and urine sample together at a ward station, a dialysis unit visible through the glass behind them.",
    "start_h2": "Who owns the next step",
    "start_html": """
<p>Most kidney emergencies in a Philippine hospital are first seen by someone in training. The intern notices that the urine bag has barely filled since noon. The resident on duty takes the 2 a.m. call about a potassium of 7.1. The fellow decides whether the patient needs dialysis tonight, and calls the attending. In between, many residents and fellows spend their weekends as the physician on duty (POD) in a freestanding hemodialysis (HD) unit, where they may be the only physician in the building.</p>
<p>This track is written for all of them. It follows a kidney problem from the first abnormal number to the long-term plan. Every module moves in the same order. It starts with a plain-language picture, then explains the physiology, states what the best evidence shows and how certain it is, and ends with what you do. Every module also tells you, in three objectives, what is expected of an intern, a resident and a fellow.</p>
{{cards:What this track will help you do|Do the renal consult well::A timeline, a urine you looked at yourself, a problem statement, and a named owner for the next step.|Keep the acute patient alive::Hyperkalemia, symptomatic hyponatremia, acidosis, fluid overload and acute kidney injury (AKI), including leptospirosis, dengue and other tropical causes.|Protect kidneys over years::Chronic kidney disease (CKD) staging and risk, blood pressure, the four pillars of kidney protection, anemia, bone and nutrition.|Prescribe and troubleshoot dialysis::HD, peritoneal dialysis (PD) and kidney replacement in the ICU, and the emergencies that happen in the chair.|Carry patients beyond dialysis::Transplant referral and follow-up, supportive care and honest conversations with families.|Work inside Philippine rules::What your license, appointment and privileges allow, PhilHealth documentation, research ethics and teaching.}}
<p><strong>How the role works in Philippine practice.</strong> An intern works under direct supervision and does not sign orders. A resident is licensed but acts within the residency&rsquo;s rules and the attending&rsquo;s plan. A fellow carries more of the plan but still answers to a consultant. A resident or fellow who takes a paid POD shift must meet the Department of Health (DOH) and Philippine Society of Nephrology (PSN) requirements for that post, and the rule in every module is the same: follow the unit protocol, but always ask the attending nephrologist for guidance. The cases are set where you work: a provincial emergency room after a flood, a Metro Manila ICU with one dialysis machine, a Saturday-night HD shift, a family meeting with relatives calling from abroad.</p>
<p>Pediatric residents and pediatric nephrology fellows study the shared core here, with an &ldquo;In children&rdquo; panel in every clinical module, and take their pediatric depth from the <a href="attending-pediatric-nephrologist.html">Attending Pediatric Nephrologist</a> track. Every new term is explained when it first appears. Every module has figures, a case, real situations, a skills checklist, linked calculators and a five-question self-assessment.</p>
""",
    "exam_draw": 40,
    "is_not": ("It is a training track written independently from published guidelines, trials, laws and regulations. It is not a license, "
               "a PSN or PNSP training program, board eligibility, CPD credit, the PSN-accredited POD course, hospital privileges or PhilHealth "
               "accreditation. Clinical competence is confirmed by your training program, through observed work and local credentialing."),
    "pathways_tag": "Six pathways",
    "pathways_h2": "Choose your pathway",
    "pathways_nav": "Pathways",
    "pathways_html": _PATHWAYS,
    "modules_h2": "Thirty-six modules in six blocks",
    "modules_intro": ("Study in order, or follow your pathway. Each module moves from intuition to physiology, then to the evidence, and ends "
                      "with what you do at your stage."),
    "syllabus_note": ("Plan about 2 hours per module as an intern or resident and about 3 hours as a fellow, for study, the case and the "
                      "self-check, plus observed work logged with your supervisor."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions, one for each stage objective plus two applied cases; the mastery mark is 4 of 5. The end-of-track examination draws 40 questions from all 36 banks. It is a formative self-study examination, not a board or in-service examination. Workplace assessment (observed encounters, case discussions, direct observation of procedures where you are privileged, and scenario stations) is described on the trainer page and is done by your program, not by this website.</p>
""",
    "sources_html": """
<p>The track is built from published sources: the Kidney Disease: Improving Global Outcomes (KDIGO) guidelines for chronic kidney disease (2024), anemia (2026), blood pressure (2021), diabetes (2022), glomerular disease and its updated chapters (lupus nephritis 2024, ANCA vasculitis 2024, IgA nephropathy 2025), ADPKD (2025), CKD&ndash;mineral and bone disorder (2017), transplant candidates (2020) and living donors (2017); the KDIGO 2012 acute kidney injury guideline and the KDIGO 2026 AKI and acute kidney disease guideline, cited only as a public-review draft; the 2025 American Heart Association and American College of Cardiology blood pressure guideline; the Kidney Disease Outcomes Quality Initiative (KDOQI) and International Society for Peritoneal Dialysis (ISPD) recommendations; the trials they rest on; and Philippine law and policy from the Professional Regulation Commission (PRC), DOH, PhilHealth and PSN. Each module lists its own sources.</p>
<p>Evidence was reviewed on November 27, 2026. The PhilHealth kidney transplant Z benefit (Revision 1, PhilHealth Circular No. 2026-0019, signed October 26, 2026) takes effect 15 days after its publication; confirm the effective date, and every PhilHealth rate and form, with your PhilHealth liaison on the date of service.</p>
""",
    "trainers_intro": ("A training officer, program director or consultant can use these modules as the guided-study part of an intern rotation, "
                       "a residency renal rotation or a nephrology fellowship. "),
    "trainer_h2": "Using the track in a training program",
    "trainer_html": """
<p><strong>Entrustable activities.</strong> Eight activities to observe, not permissions: E1 assess and present a renal consult; E2 recognize and escalate a renal emergency; E3 plan CKD follow-up and prevention; E4 propose and review kidney replacement; E5 assess access or procedure suitability; E6 evaluate a transplant problem; E7 coordinate transitions and resource use; E8 improve care and teach. Record supervision as O (observes), D (does with direct supervision), I (does with the supervisor immediately available) or R (reviewed after, only where specifically authorized). An intern is never at R, and no one reaches R by finishing this course.</p>
<p><strong>Workplace evidence (suggested, not a PSN or PNSP minimum).</strong> Intern: two observed presentations, one teach-back and one handoff. Resident: four mini clinical evaluation exercises (Mini-CEX), four case-based discussions, two acute simulations and a medication or chart audit. Fellow: six Mini-CEX and six case-based discussions a year, procedure observations as your institution requires, multisource feedback, a quality improvement or research output, and two portfolio reviews a year.</p>
<p><strong>Scenario stations.</strong> Eight 10-minute stations: AKI consult, electrolyte emergency, CKD follow-up, dialysis review, infection and water event, transplant dysfunction, shared modality decision, and handoff and Philippine scope. Interns use stations 1, 2, 5 and 8; residents 1 to 5, 7 and 8; fellows all eight. Score each domain 0 to 3; a pass is at least 2 in every observed safety domain with no critical failure. A missed critical action means feedback and a repeat with a different case.</p>
<p><strong>Capstones.</strong> Interns present an AKI and electrolyte case and hand it over. Residents manage a CKD patient admitted with acute deterioration. Fellows defend a longitudinal case from proteinuric CKD through dialysis to transplant or supportive care, critique a trial and teach a junior. All forms stay unsigned on this site; signatures belong on your program&rsquo;s own records.</p>
""",
    "completion_html": """
<p>You have finished the Nephrology Fellow / Resident / Medical Intern track. Your completion is an Academy learning record of self-study. It does not confer licensure, specialist status, PSN or PNSP membership or board eligibility, procedural privileges, CPD units, or completion of an institutional training program. Competence in practice is confirmed by your training program.</p>
""",
    "related": [("aki-does-not-end-at-discharge.html", "AKI does not end at discharge."),
                ("understanding-ckd.html", "Understanding chronic kidney disease."),
                ("dysnatremia.html", "Dysnatremia: hyponatremia and hypernatremia.")],
}

_BLOCKS = [(1, 4, "Block A &middot; Foundation and the consult"),
           (5, 10, "Block B &middot; Fluids, electrolytes and acute kidney disease"),
           (11, 16, "Block C &middot; Longitudinal kidney health"),
           (17, 21, "Block D &middot; Disease mechanisms and populations"),
           (22, 28, "Block E &middot; Kidney replacement care"),
           (29, 36, "Block F &middot; Advanced and professional practice")]


def _block(n):
    for a, b, name in _BLOCKS:
        if a <= n <= b:
            return name
    return _BLOCKS[-1][2]


MODULES = []
for _id, _slug, _title, _sub in _json.loads((_Path(__file__).resolve().parent / "_rows.json").read_text(encoding="utf-8")):
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub + ".", "part": _block(int(_id)),
                    "card_img": f"{HUB}-{_id}-card.webp", "hero_brief": _HB + _title,
                    **({} if (_Path(__file__).resolve().parent / f"m{_id}.py").exists() else {"status": "planned"})})
