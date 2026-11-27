# -*- coding: utf-8 -*-
"""Attending Pediatric Nephrologist (APN) track: course definition in the Physician on Duty (POD) package schema.
Built from Blueprint v2 (November 27, 2026), which consolidates the 33-entry handoff into 29 pages and expands dialysis
to seven modules at Dr. Rivero's request. Clinical content is a draft pending his sign-off. Every case is fictional."""
import json as _json
from pathlib import Path as _Path

HUB = "attending-pediatric-nephrologist"
_HB = "Illustrated clinical vignette, warm natural light, Filipino clinicians, children and families, no text in image. "

COURSE = {
    "title": "Attending Pediatric Nephrologist",
    "short": "Attending Pediatric Nephrologist",
    "hub_slug": HUB,
    "label": "Training track for attending pediatric nephrologists",
    "tag": "Renal Care Physicians",
    "icon": "🧸",
    "no_branch": True,
    "audience": ("Pediatric nephrologists &middot; pediatric nephrology fellows &middot; adult nephrologists, intensivists and neonatologists "
                 "who share kidney care for children in the clinic, ward, NICU, PICU, dialysis unit and home"),
    "audience_type": "Pediatric nephrologists and pediatric nephrology fellows",
    "level": "Physicians with pediatric nephrology training, written in plain language",
    "review_date": "2026-11-27",
    "draw": 5,
    "mastery": "4 of 5",
    "keywords": ("pediatric nephrology training Philippines, attending pediatric nephrologist, KDIGO 2025 nephrotic syndrome in children, "
                 "CKiD U25 eGFR, pediatric hypertension AAP 2017, ESCAPE trial, PREDICT vesicoureteral reflux, hemolytic uremic syndrome, "
                 "neonatal AKI AWAKEN, pediatric CKRT fluid overload, pediatric peritoneal dialysis, ISPD 2022 peritonitis, pediatric hemodialysis, "
                 "vascular access children, pediatric kidney transplant, PhilHealth pediatric PD Z package, APD pilot"),
    "page_title": "Attending Pediatric Nephrologist: A Training Track",
    "desc": ("A free 29-module training track for attending pediatric nephrologists in the Philippines: the growing kidney, fluids and "
             "electrolyte emergencies, hypertension, CAKUT and UTI, nephrotic and nephritic disease, HUS, neonatal and pediatric AKI, CKRT, "
             "CKD and growth, peritoneal dialysis and hemodialysis in children, transplantation, medicines, safeguarding and PhilHealth. "
             "Each module moves from intuition to physiology, evidence, and practice."),
    "h1": "Attending <em>Pediatric Nephrologist</em>",
    "sub": ("A training track for physicians who carry responsibility for children with kidney disease, from the newborn to the young adult "
            "handed over to adult care. Learn why each decision makes physiologic sense in a growing body, how strong the evidence is, and "
            "who owns the next step."),
    "disclaimer": ("Educational material for physicians. Completing it is an Academy learning record only. It does not confer CPD units, "
                   "PNSP or board certification, privileges, or PhilHealth accreditation, and it does not replace current guidelines, "
                   "regulations, your institution&rsquo;s pediatric protocols and formulary, or clinical judgment."),
    "scope_note": ("This module is study material for attending pediatric nephrologists and fellows. It explains the reasoning behind common "
                   "decisions; it is not a protocol and it gives no doses. Doses, fill volumes and thresholds must come from current pediatric "
                   "guidelines, product labels, your institution&rsquo;s approved pediatric protocols and a pediatric pharmacist. Benefit rules "
                   "change: confirm them on the date of service. Every case is fictional."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Attending pediatric nephrologists",
    "branch_blurb": ("For pediatric nephrologists and fellows: the growing kidney, emergencies, glomerular and structural disease, AKI and CKRT, "
                     "CKD and growth, PD and HD in children, transplant, medicines, safeguarding and PhilHealth."),
    "academy_meta": "29 modules &middot; seven on dialysis &middot; a capstone &middot; calculators in every module",
    "hero_alt": "A pediatric nephrologist kneels beside a young child in a hospital playroom while the mother watches, a dialysis machine in soft focus behind them.",
    "start_h2": "The doctor a child&rsquo;s whole family calls",
    "start_html": """
<p>A child with kidney disease is never one patient. Behind every creatinine is a growth chart, a school record, a mother who learned peritoneal dialysis (PD) exchanges at the kitchen table, and a father working abroad who calls after every clinic visit. The attending pediatric nephrologist (APN) owns the child&rsquo;s renal plan: the diagnosis, the treatment goals, the dialysis and transplant decisions, the periodic review, and the decision to change course. The pediatric resident, the physician on duty (POD), the intensivist, the dialysis nurse and the family act at the bedside; the attending decides what happens next and makes sure every decision has an owner.</p>
<p>The track follows children through every setting a pediatric nephrologist works in: the newborn nursery and neonatal intensive care unit (NICU), the clinic, the ward, the pediatric intensive care unit (PICU), the PD home, the hemodialysis (HD) unit, the transplant program, and the handover to adult care. Every module moves in the same order. It starts with a plain-language picture, explains the physiology of a growing kidney, states what the best evidence in children shows and how certain it is, and ends with what the attending does.</p>
{{cards:What this track will help you do|Assess a growing child::Read creatinine against height and age, blood pressure against percentiles, and urine against the child&rsquo;s story.|Treat the emergencies that kill children quickly::Hyperkalemia, symptomatic dysnatremia, hypertensive emergency, fluid overload, hemolytic uremic syndrome (HUS), peritonitis and catheter sepsis.|Manage glomerular, structural and inherited disease::Know when to give steroids, when to biopsy, and when to test genes.|Prescribe dialysis for children::PD at home, HD in a unit built for adults, and continuous kidney replacement therapy (CKRT) in the PICU, matched to the child&rsquo;s size.|Carry a child to transplant and beyond::A safe bladder, an ethical donor, and an adolescent who keeps taking the tablets.|Protect the child and the service::Safe prescribing, safeguarding, truthful PhilHealth documentation, transition, teaching and quality improvement.}}
<p><strong>How the role works in Philippine practice.</strong> Pediatric nephrologists are few and concentrated in a handful of centers, so one attending may cover several hospitals and receive most calls by phone or Viber from pediatric residents, general pediatricians and adult nephrologists. Many children on hemodialysis are treated in adult units, where the nurses and the physician on duty are skilled with adults but see a child only occasionally. PhilHealth now funds a pediatric PD package that names the attending pediatric nephrologist on its forms. The cases in this track are written from that position: often off site, reached by phone, responsible for the plan, and the person the family trusts most.</p>
<p>Seven modules (16 and 20 to 25) teach dialysis in children in depth: CKRT, PD access and prescription, home PD and its non-infectious complications, PD peritonitis, the HD prescription, vascular access, and HD emergencies in adult units. Every new term is explained when it first appears. Every module has figures, a case, real situations, a skills checklist, linked calculators, and a five-question self-assessment.</p>
""",
    "exam_draw": 40,
    "is_not": ("It is a training track written independently from published guidelines, trials, laws, and regulations. It is not a license, "
               "Pediatric Nephrology Society of the Philippines (PNSP) or board certification, CPD credit, hospital privileges, or PhilHealth "
               "accreditation. Clinical competence requires observation by a local assessor and facility credentialing."),
    "pathways_tag": "Eight blocks",
    "pathways_h2": "Fifteen weeks of study, in eight blocks",
    "pathways_nav": "Blocks",
    "pathways_html": """
<p>The 29 modules are grouped into eight blocks, studied at about two modules a week. Each block ends with a work sample that a preceptor reviews.</p>
{{cards:The eight blocks|Block 1 &middot; The child, the role and the bedside::Modules 1 to 4. Responsibility and credentials, the growing kidney, fluids and sodium, electrolyte emergencies.|Block 2 &middot; Pressure, structure and infection::Modules 5 to 8. Hypertension, congenital anomalies and valves, urinary tract infection and reflux, tubulopathies and inherited disease.|Block 3 &middot; Glomerular and systemic disease::Modules 9 to 13. Nephrotic syndrome, nephritic syndromes, lupus and vasculitis, hemolytic uremic syndrome.|Block 4 &middot; Acute and critical care::Modules 14 to 16. Neonatal acute kidney injury (AKI), pediatric AKI, and CKRT in the PICU.|Block 5 &middot; CKD and choosing therapy::Modules 17 to 19. Chronic kidney disease (CKD) and growth, CKD complications, choosing kidney replacement therapy with families.|Block 6 &middot; Peritoneal dialysis::Modules 20 to 22. Access and prescription, home PD and its complications, peritonitis.|Block 7 &middot; Hemodialysis::Modules 23 to 25. The prescription, vascular access, emergencies and water in adult units.|Block 8 &middot; Transplant and professional practice::Modules 26 to 29. Transplant preparation and follow-up, medicines and safeguarding, and the capstone.}}
""",
    "modules_h2": "Twenty-nine modules in eight blocks",
    "modules_intro": ("Study the modules in order. Each one moves from intuition to physiology, then to the evidence, and ends with what "
                      "the attending does."),
    "syllabus_note": ("Plan about 2 hours per module for study, case discussion, and self-check, plus observed work or simulation logged with "
                      "a preceptor and a 4-hour capstone, about 60 hours of guided study in all."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions; the mastery mark is 4 of 5. The end-of-track examination draws 40 questions from all 29 banks. The capstone follows one child through every setting and is scored on five areas, 0 to 2 each; a pass is 8 of 10 with every critical action met.</p>
""",
    "sources_html": """
<p>The track is built from published sources: the Kidney Disease: Improving Global Outcomes (KDIGO) guidelines for nephrotic syndrome in children (2025), immunoglobulin A nephropathy and vasculitis (2025), lupus nephritis (2024), chronic kidney disease (2024), anemia (2026) and acute kidney injury; the International Pediatric Nephrology Association (IPNA) recommendations; the American Academy of Pediatrics (AAP) guidelines on blood pressure, urinary tract infection and intravenous fluids; the International Society for Peritoneal Dialysis (ISPD) recommendations; the trials they rest on, including ESCAPE, RIVUR, PREDICT, PREDNOS, AWAKEN and TAKE-IT; and Philippine requirements from the Department of Health (DOH), PhilHealth and the Pediatric Nephrology Society of the Philippines (PNSP). Each module lists its own sources.</p>
<p>Evidence was reviewed on November 27, 2026. The KDIGO 2026 guideline for AKI and acute kidney disease is cited only as a public-review draft. The PhilHealth pediatric automated PD (APD) pilot was extended to July 31, 2026; its status after that date is unresolved in this track and must be confirmed with your PhilHealth liaison. PhilHealth rates and forms must be confirmed on the date of service.</p>
""",
    "trainers_intro": ("A pediatric nephrology program director or a senior attending can use these modules as the guided-study part of an "
                       "attending&rsquo;s orientation or a fellow&rsquo;s final year. "),
    "trainer_h2": "Using the track to prepare a pediatric attending",
    "trainer_html": """
<p>A practical plan is two modules a week over fifteen weeks, each block closed by a work sample the preceptor reviews: a credential and coverage map, an age-corrected assessment of a referred child, a fluid order that avoids hyponatremia, an ambulatory blood pressure interpretation, a reflux and prophylaxis decision, a nephrotic course classification, an HUS escalation, a neonatal nephrotoxin review, a CKRT fluid-overload calculation, a growth and nutrition plan, a PD prescription and caregiver-training record, a peritonitis response, an HD circuit-volume check, a vascular access plan, a transplant readiness checklist, and a transition letter.</p>
<p>The final assessment is four scenario stations of 12 minutes each, followed by the capstone defense. Score each station 0 to 10; a pass is 8 with every critical action met. A missed critical action means feedback and a repeat with a different case. Simulated evidence is labeled simulated, and no completion grants a privilege.</p>
""",
    "completion_html": """
<p>You have finished the Attending Pediatric Nephrologist track. Your completion is an Academy learning record of self-study. Competence in practice is confirmed separately, by a local assessor who observes your work and by your facility&rsquo;s credentialing.</p>
""",
    "related": [("ckd-children-young-adults.html", "Kidney disease in children and young adults."),
                ("nephrotic-syndrome.html", "Nephrotic syndrome, from podocyte to plan."),
                ("peritoneal-dialysis-ckd.html", "Peritoneal dialysis at home.")],
}

_BLOCKS = [(1, 4, "Block 1 &middot; The child, the role and the bedside"),
           (5, 8, "Block 2 &middot; Pressure, structure and infection"),
           (9, 13, "Block 3 &middot; Glomerular and systemic disease"),
           (14, 16, "Block 4 &middot; Acute and critical care"),
           (17, 19, "Block 5 &middot; CKD and choosing therapy"),
           (20, 22, "Block 6 &middot; Peritoneal dialysis"),
           (23, 25, "Block 7 &middot; Hemodialysis"),
           (26, 29, "Block 8 &middot; Transplant and professional practice")]


def _block(n):
    for a, b, name in _BLOCKS:
        if a <= n <= b:
            return name
    return _BLOCKS[-1][2]


MODULES = []
for _id, _slug, _title, _sub in _json.loads((_Path(__file__).resolve().parent / "_rows.json").read_text(encoding="utf-8")):
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub + ".", "part": _block(int(_id)),
                    "card_img": f"{HUB}-{_id}-card.webp", "hero_brief": _HB + _title})
