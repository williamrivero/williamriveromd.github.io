# -*- coding: utf-8 -*-
"""Attending Nephrologist (AN) track: course definition in the Physician on Duty (POD) package schema.
Built from the v2 blueprint (clinical content signed off by Dr. Rivero, November 24, 2026). Every case is fictional."""
import json as _json
from pathlib import Path as _Path

HUB = "attending-nephrologist"
_HB = "Illustrated clinical vignette, warm natural light, Filipino clinicians and patients, no text in image. "

COURSE = {
    "title": "Attending Nephrologist",
    "short": "Attending Nephrologist",
    "hub_slug": HUB,
    "label": "Training track for attending nephrologists in adult practice",
    "tag": "Physician Practice",
    "icon": "🩺",
    "no_branch": True,
    "audience": ("Practicing nephrologists &middot; senior nephrology fellows &middot; internists who share longitudinal kidney care "
                 "in the clinic, ward, ICU, dialysis unit, and home"),
    "audience_type": "Nephrologists and senior nephrology fellows",
    "level": "Physicians with nephrology training, written in plain language",
    "review_date": "2026-11-24",
    "draw": 5,
    "mastery": "4 of 5",
    "keywords": ("attending nephrologist training Philippines, nephrology consult, AKI follow-up, hyperkalemia emergency, CRRT delivered dose, "
                 "KDIGO 2024 CKD, KFRE, KDIGO 2026 anemia, hemodialysis adequacy Kt/V, PD peritonitis ISPD 2022, kidney transplant referral, "
                 "conservative kidney management, PhilHealth hemodialysis 156 sessions, dialysis typhoon preparedness"),
    "page_title": "Attending Nephrologist: A Training Track",
    "desc": ("A free 24-module training track for attending nephrologists in the Philippines: taking responsibility, the consult, AKI and "
             "electrolyte emergencies, acute KRT and CRRT, CKD and glomerular disease, dialysis initiation, HD and PD, transplant referral, "
             "conservative care, PhilHealth claims, disasters, and quality improvement. Each module moves from intuition to physiology, "
             "evidence, and practice."),
    "h1": "Attending <em>Nephrologist</em>",
    "sub": ("A training track for physicians who carry longitudinal responsibility for adults with kidney disease. Learn why each decision "
            "makes physiologic sense, how strong the evidence is, and who owns the next step."),
    "disclaimer": ("Educational material for physicians. Completing it is an Academy learning record only. It does not confer CPD units, "
                   "PSN certification, privileges, or PhilHealth accreditation, and it does not replace current guidelines, regulations, "
                   "your institution&rsquo;s protocols, or clinical judgment."),
    "scope_note": ("This module is study material for attending nephrologists and senior fellows in adult practice. It explains the reasoning "
                   "behind common decisions; it is not a protocol. Doses and thresholds must be checked against current product labels, "
                   "guidelines, and your institution&rsquo;s approved protocols. Regulatory and benefit rules change: confirm them on the date "
                   "of service. Every case is fictional."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Attending nephrologists",
    "branch_blurb": ("For nephrologists and senior fellows: the consult, AKI and emergencies, CRRT, CKD and glomerular disease, HD and PD, "
                     "transplant and supportive care, PhilHealth claims, disasters, and quality."),
    "academy_meta": "24 modules &middot; a capstone &middot; calculators in every module",
    "hero_alt": "A physician takes a phone call at a corridor window, looking toward a lit dialysis unit across the courtyard.",
    "start_h2": "The doctor who answers at 2 a.m.",
    "start_html": """
<p>An attending appointment is a promise that someone with the right authority will answer when a patient deteriorates in the middle of the night. The attending nephrologist (AN) owns each patient&rsquo;s renal plan: the diagnosis, the treatment goals, the initial and maintenance orders, the periodic review, and the decision to change course. The physician on duty (POD) and the dialysis nurse respond at the bedside; the AN decides what happens next, and makes sure the decision has an owner.</p>
<p>The track follows a patient through every setting an attending works in: the referral clinic, the ward, the intensive care unit (ICU), the hemodialysis (HD) unit, peritoneal dialysis (PD) at home, the transplant referral, and supportive care. Every module moves in the same order. It starts with a plain-language picture, explains the physiology, states what the best human evidence shows and how certain it is, and ends with what the attending does.</p>
{{cards:What this track will help you do|Own the consult and transition::Prioritize urgency, name the decision owner, and confirm that the handoff was received.|Manage urgent renal syndromes::Recognize time-critical findings, start a coordinated response, and reassess.|Manage chronic kidney disease (CKD) and complex disease::Integrate trajectory, cause, risk, medication safety, and the patient&rsquo;s goals.|Prescribe and review kidney replacement therapy::Justify modality, access, prescription, safety checks, and the criteria for change.|Coordinate transplantation and supportive care::Write a referral that can be acted on, and a plan built on the patient&rsquo;s values.|Protect patients and improve care::Reconcile claims, report incidents, teach the team, and measure improvement.}}
{{fig:an_t_03}}
<p>Every new term is explained when it first appears. Every module has figures, a case, a skills checklist, linked calculators, and a five-question self-assessment.</p>
""",
    "exam_draw": 40,
    "is_not": ("It is a training track written independently from published guidelines, trials, laws, and regulations. It is not a license, "
               "Philippine Society of Nephrology (PSN) certification, CPD credit, hospital privileges, or PhilHealth accreditation. Clinical competence requires observation by "
               "a local assessor and facility credentialing."),
    "pathways_tag": "Six blocks",
    "pathways_h2": "Twelve weeks of study, in six blocks",
    "pathways_nav": "Blocks",
    "pathways_html": """
<p>The 24 modules are grouped into six blocks of four, studied at two modules a week. Each block ends with a work sample that a preceptor reviews.</p>
{{cards:The six blocks|Block 1 &middot; Taking responsibility::Modules 1 to 4. Credentials and coverage, the consult, communication, consent and reconciliation.|Block 2 &middot; Acute and critical care::Modules 5 to 8. Acute kidney injury (AKI), electrolyte emergencies, acute kidney replacement therapy (KRT) in the ICU, and continuous kidney replacement therapy (CRRT) delivery.|Block 3 &middot; Chronic and complex disease::Modules 9 to 12. CKD progression and complications, glomerular disease, and tubulointerstitial, vascular, and inherited disease.|Block 4 &middot; Kidney failure and HD::Modules 13 to 16. Planning the start, the HD prescription, HD emergencies, and vascular access.|Block 5 &middot; Home therapy and transitions::Modules 17 to 20. PD prescription, peritonitis, transplant referral, and conservative care.|Block 6 &middot; Professional practice::Modules 21 to 24. PhilHealth claims, disasters, quality improvement, and the capstone.}}
""",
    "modules_h2": "Twenty-four modules in six blocks",
    "modules_intro": ("Study the modules in order. Each one moves from intuition to physiology, then to the evidence, and ends with what "
                      "the attending does."),
    "syllabus_note": ("Plan about 90 minutes per module for study, case discussion, and self-check, plus 12 hours of observed work or "
                      "simulation and a 4-hour capstone, about 52 hours in all."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions; the mastery mark is 4 of 5. The end-of-track examination draws 40 questions from all 24 banks. The capstone follows one patient through every setting and is scored on five areas, 0 to 2 each; a pass is 8 of 10 with every critical action met.</p>
{{fig:an24_b}}
""",
    "sources_html": """
<p>The track is built from published sources: the Kidney Disease: Improving Global Outcomes (KDIGO) guidelines for chronic kidney disease (CKD), acute kidney injury (AKI), anemia, glomerular disease, and transplantation; the Kidney Disease Outcomes Quality Initiative (KDOQI) guidelines for hemodialysis adequacy and vascular access; the International Society for Peritoneal Dialysis (ISPD) recommendations; the landmark trials they rest on; and Philippine requirements from the Department of Health (DOH), PhilHealth, and the Philippine Society of Nephrology (PSN). Each module lists its own sources.</p>
<p>Evidence was reviewed on November 24, 2026. The KDIGO 2026 guideline for AKI and acute kidney disease is cited only as a public-review draft. PhilHealth rates and forms must be confirmed on the date of service.</p>
""",
    "trainers_intro": ("A nephrology program director or a senior attending can use these modules as the guided-study part of an attending&rsquo;s orientation or a fellow&rsquo;s final year. "),
    "trainer_h2": "Using the track to prepare an attending",
    "trainer_html": """
<p>A practical plan is two modules a week over twelve weeks, each block closed by a work sample the preceptor reviews: a coverage map, a renal consult note, a delivered-dose audit, a chronic kidney disease plan that records cause, glomerular filtration rate (GFR) category, and albuminuria, a biopsy conference, a modality decision, a goal-directed PD plan, a claim reconciliation, and a quality-improvement rate analysis. Run a baseline case in week 1 and use the same six competency domains at the final review.</p>
<p>The final assessment is four scenario stations of 12 minutes each, followed by the capstone defense. Score each station 0 to 10; a pass is 8 with every critical action met. A missed critical action means feedback and a repeat with a different case.</p>
{{fig:an_tr_a}}
""",
    "completion_html": """
<p>You have finished the Attending Nephrologist track. Your completion is an Academy learning record of self-study. Competence in practice is confirmed separately, by a local assessor who observes your work and by your facility&rsquo;s credentialing.</p>
""",
    "related": [("aki-icu-dialysis-decisions.html", "When and how to start dialysis in the ICU."),
                ("slowing-ckd-progression.html", "Layered protection for chronic kidney disease."),
                ("dialysis-adequacy.html", "What Kt/V measures, and what it misses.")],
}

_BLOCKS = {1: "Block 1 &middot; Taking responsibility", 2: "Block 2 &middot; Acute and critical care",
           3: "Block 3 &middot; Chronic and complex disease", 4: "Block 4 &middot; Kidney failure and HD",
           5: "Block 5 &middot; Home therapy and transitions", 6: "Block 6 &middot; Professional practice"}

MODULES = []
for _id, _slug, _title, _sub in _json.loads((_Path(__file__).resolve().parent / "_rows.json").read_text(encoding="utf-8")):
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub + ".", "part": _BLOCKS[(int(_id) - 1) // 4 + 1],
                    "card_img": f"{HUB}-{_id}-card.webp", "hero_brief": _HB + _title})
