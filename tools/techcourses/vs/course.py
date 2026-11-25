# -*- coding: utf-8 -*-
"""Vascular Surgeon (VS) subtrack of the Renal Care Physicians Track: course definition in the POD package schema.
Built from the v2.0 final blueprint (06-final-blueprint.md, November 25, 2026). Clinical review pending. Every case is fictional."""

HUB = "vascular-surgeon"
_HB = ("Illustrated clinical vignette, warm natural light, Filipino surgeons, nurses and patients in a Philippine hospital "
       "or dialysis unit, no text in image, no visible operative field. ")

COURSE = {
    "title": "Vascular Surgeon",
    "short": "Vascular Surgeon",
    "hub_slug": HUB,
    "label": "Training track for surgeons who create and maintain dialysis access",
    "tag": "Renal Care Physicians",
    "icon": "🩺",
    "no_branch": True,
    "audience": ("Vascular and cardiovascular surgeons with a renal access practice &middot; surgical fellows &middot; general surgeons "
                 "working under supervision in an institutionally approved access service"),
    "audience_type": "Vascular surgeons and supervised surgical trainees",
    "level": "Surgeons, written in plain language",
    "review_date": "2026-11-25",
    "draw": 5,
    "mastery": "4 of 5",
    "keywords": ("vascular access surgeon training Philippines, arteriovenous fistula, arteriovenous graft, KDOQI 2019 vascular access, "
                 "UKKA 2025 vascular access guideline, ESKD Life-Plan, vein mapping, fistula maturation, first cannulation, access stenosis, "
                 "drug-coated balloon, stent graft, access thrombosis, steal syndrome, digital brachial index, access hemorrhage, "
                 "catheter-related bloodstream infection, central venous stenosis, high-flow access, PSN 2024 hemodialysis guidelines"),
    "page_title": "Vascular Surgeon: A Dialysis Access Training Track",
    "desc": ("A free 20-module training track for surgeons who create and maintain hemodialysis access in the Philippines: the access "
             "Life-Plan, vessel assessment and mapping, readiness and creation, grafts and catheters, maturation and first use, "
             "dysfunction and endovascular choices, thrombosis, hand ischemia, bleeding, infection, high flow, complex access, "
             "documentation and quality. Each module moves from intuition to physiology, evidence, and practice."),
    "h1": "Vascular <em>Surgeon</em>",
    "sub": ("A training track for surgeons whose operations a patient will depend on three times a week. Learn why each access decision "
            "makes physiologic sense, how strong the evidence is, and who owns the next step after you close the wound."),
    "disclaimer": ("Educational material for surgeons. Completing it is an Academy learning record only. It does not confer CPD units, "
                   "board certification or eligibility, hospital privileges, or PhilHealth accreditation, and it does not teach operative "
                   "technique. It does not replace current guidelines, regulations, your institution&rsquo;s protocols, or clinical judgment. "
                   "Clinical review of this track is pending."),
    "scope_note": ("This module is study material for surgeons and supervised surgical trainees in adult dialysis access. It explains the "
                   "reasoning behind access decisions; it is not an operative manual or a protocol. Device instructions, drug doses and "
                   "local escalation contacts belong in your institution&rsquo;s approved protocols. Benefit rules change: confirm them on "
                   "the date of service. Every case is fictional. Clinical review of this track is pending."),
    "branch_img": f"{HUB}-card.webp",
    "branch_role": "Vascular access surgeons",
    "branch_blurb": ("For surgeons and supervised trainees: the access Life-Plan, mapping and creation, grafts and catheters, first use, "
                     "salvage, hand ischemia, bleeding and infection, complex access, and quality."),
    "academy_meta": "20 modules &middot; a capstone &middot; calculators &middot; end-of-course exam",
    "hero_alt": "A surgeon examines a patient&rsquo;s forearm fistula with a dialysis nurse beside the chair.",
    "start_h2": "The operation the patient uses three times a week",
    "start_html": """
<p>Most operations end when the wound heals. A dialysis access starts working when the wound heals, and it has to keep working, twelve needle punctures a month, for as long as the patient needs hemodialysis (HD). The measure of your work is not a patent anastomosis on the table. It is whether the patient dialyzes reliably, without a catheter, with the fewest procedures, while keeping the next site available.</p>
<p>The Philippine Society of Nephrology (PSN) 2024 hemodialysis guidelines make the attending nephrologist responsible for coordinating vascular access with a vascular surgeon or a trained general surgeon (Section 1.2, b3).[[an01_1]] This track is written for the other end of that call. It follows a patient from referral through planning, creation, first cannulation, failure and rescue, and into the service that holds it together.</p>
{{cards:What this track will help you do|Plan access inside the patient&rsquo;s life::Build a Life-Plan with a present access, a contingency and a successor, and document the patient&rsquo;s choice.|Assess and choose::Read the arm, the history and the map, and justify the configuration, including what you rejected.|Create and hand off safely::Prepare the patient, follow the consent, and write a handoff the dialysis unit can act on.|Get from patent to usable::Judge maturation, investigate delay, and agree a first-cannulation plan.|Rescue without losing the future::Separate emergencies from elective dysfunction and choose salvage that preserves the next site.|Run an access service::Close every referral, audit functional outcomes, and teach the team.}}
<p><strong>How the role works in Philippine practice.</strong> The surgeon is usually a consultant to the hemodialysis center (HDC), not its staff. The attending nephrologist owns the dialysis prescription and the kidney plan; the dialysis nurse cannulates within an authorized scope; the physician on duty (POD) manages the shift. Your privileges come from the hospital where you operate, not from the dialysis unit and not from this course. The cases are written from that position: called by a unit you do not run, about a patient you may meet for the first time.</p>
<p>Every new term is explained when it first appears. Every module has a case, figures, a skills checklist, linked calculators, and a five-question self-assessment.</p>
""",
    "exam_draw": 40,
    "is_not": ("It is a training track written independently from published guidelines, trials, and Philippine regulations. It is not a license, "
               "board certification or eligibility, CPD credit, hospital privileges, or PhilHealth accreditation, and it does not teach operative "
               "technique. Competence requires observation by a qualified local assessor and your hospital&rsquo;s credentialing. Clinical review of "
               "this track is pending."),
    "pathways_tag": "Four blocks",
    "pathways_h2": "Ten weeks of study, in four blocks",
    "pathways_nav": "Blocks",
    "pathways_html": """
<p>The 20 modules are grouped into four blocks and studied at two modules a week. The emergency modules (12 to 16) can be opened directly when you need them.</p>
{{cards:The four blocks|Block 1 &middot; Responsibility and planning::Modules 1 to 4. The surgeon in the kidney care team, the Life-Plan, examining and preserving vessels, mapping and choosing.|Block 2 &middot; Creation and safe use::Modules 5 to 9. Readiness, the autogenous fistula, grafts, catheters and central veins, maturation and first cannulation.|Block 3 &middot; Dysfunction and rescue::Modules 10 to 16. The failing access, stenosis and endovascular choices, thrombosis, hand ischemia, aneurysm and bleeding, infection and sepsis, high flow and central veins.|Block 4 &middot; Complex care and governance::Modules 17 to 20. The difficult access, care beyond the access, Philippine documentation and quality, and the integrated access service.}}
""",
    "modules_h2": "Twenty modules in four blocks",
    "modules_intro": ("Study the modules in order. Each one moves from intuition to physiology, then to the evidence, and ends with what "
                      "the surgeon does."),
    "syllabus_note": ("Plan about 90 minutes per module for study, case discussion and self-check (30 hours), plus 16 hours of observed work or "
                      "simulation and a 4-hour capstone: 50 planned hours. These hours are an Academy design choice, not a national requirement, "
                      "and they do not qualify anyone for independent surgery."),
    "assessment_html": """
<p>Each module ends with a self-assessment of 5 questions; the mastery mark is 4 of 5. The end-of-track examination draws 40 questions from the 100-question bank; the proposed learning target is 32 of 40, and every missed safety item calls for review even when the total passes. Supervised clinical assessment is separate: the observation form, four emergency stations and the capstone are on the trainer page. A browser score is a study record, not a competence decision.</p>
""",
    "sources_html": """
<p>The track is built from published sources: the Kidney Disease Outcomes Quality Initiative (KDOQI) 2019 vascular access guideline and its implementation tools, the UK Kidney Association (UKKA) 2025 vascular access guideline, the European Society for Vascular Surgery (ESVS) 2018 guideline, the Society for Vascular Surgery (SVS) guideline and reporting standards, the randomized trials and meta-analyses they rest on, and Philippine requirements from the Department of Health (DOH), PhilHealth, and the PSN. UKKA statements are quoted with UKKA&rsquo;s own grades; no grade is translated between systems. Each module lists its own sources.</p>
<p>Evidence was reviewed on November 25, 2026. The ESVS has a replacement access guideline in development; none of its unpublished recommendations is used. PhilHealth rules must be confirmed on the date of service. Clinical review by a vascular surgeon, a nephrologist, a dialysis nurse and a Philippine policy reviewer is pending.</p>
""",
    "trainers_intro": ("A vascular surgery program director, an access service lead or a senior access surgeon can use these modules as the guided-study part of a fellow&rsquo;s access rotation or a new consultant&rsquo;s orientation. "),
    "trainer_h2": "Using the track to prepare an access surgeon",
    "trainer_html": """
<p>A practical plan is two modules a week over ten weeks. Allocate the 16 practice hours as: three in planning and mapping review, three in perioperative and procedural observation, three in first-use and dysfunction conferences, four in hemorrhage, ischemia, sepsis and access-loss simulations, and three in documentation, audit and service handoffs. Simulation may stand in for a live case when none is available, but it stays labeled simulation.</p>
<p>Record supervision as observation only, direct supervision, immediately available supervision, or institutionally authorized independent practice; only the hospital can grant the last. Use direct observation for assessment, consent, mapping interpretation and handoff; case discussion for reasoning; and procedural assessment only where the learner is already authorized to take part. There is no Academy minimum number of operations that guarantees competence.</p>
<p><strong>Observation form.</strong> Score four domains 0 to 2 (assessment and reasoning; communication and consent; safety and escalation; follow-through and documentation). Satisfactory is at least 6 of 8 with every critical action met.</p>
<p><strong>Four emergency stations</strong> (10 minutes each, 5-minute debrief): hemorrhage from threatened skin; new pain and motor deficit after creation; a draining access with hypotension; a thrombosed access after a missed session with breathlessness. Score recognition, initial response, escalation, contingency and communication 0 to 2 each; satisfactory is 8 of 10 with no critical miss. A failed station is repeated with a changed scenario after feedback.</p>
<p><strong>Capstone.</strong> A fictional 58-year-old with diabetes, a prior right internal jugular catheter, an incomplete access history, and a home three hours from the access center. The examiner introduces delayed usability, then threatened skin, then an access interruption. The learner submits a two-page access plan, a one-page dialysis handoff and a one-page improvement proposal, and defends them orally. Five domains 0 to 2; a pass is 8 of 10 with every emergency recognized and escalated.</p>
""",
    "completion_html": """
<p>You have completed the Vascular Surgeon self-study track. This browser record documents learning activity only. Clinical competence, CPD recognition, board certification, professional accreditation and procedural privileges are determined separately by the relevant institutions and authorities.</p>
""",
    "related": [("hemodialysis-access-lifeline.html", "The access as a lifeline that lasts."),
                ("dialysis-access-care.html", "Caring for a fistula, graft or catheter."),
                ("dialysis-access-infection.html", "When the access gets infected.")],
}

_BLOCKS = {1: "Block 1 &middot; Responsibility and planning", 2: "Block 2 &middot; Creation and safe use",
           3: "Block 3 &middot; Dysfunction and rescue", 4: "Block 4 &middot; Complex care and governance"}


def _block(i):
    return 1 if i <= 4 else 2 if i <= 9 else 3 if i <= 16 else 4


_ROWS = [
    ("01", "the-surgeon-in-the-kidney-care-team", "The surgeon in the kidney care team",
     "Separate surgical responsibility from dialysis governance, triage a referral, and close it with a named owner"),
    ("02", "the-lifetime-access-plan", "The lifetime access plan",
     "Build an end-stage kidney disease (ESKD) Life-Plan with a present access, a contingency and a successor, chosen with the patient"),
    ("03", "examine-and-preserve-the-vessels", "Examine and preserve the vessels",
     "Take a vessel history, examine both arms, and protect the veins the patient will need"),
    ("04", "mapping-and-choosing-an-access", "Mapping and choosing an access",
     "Read a vessel map for construction and cannulation, and justify the choice you make"),
    ("05", "make-the-patient-ready-for-surgery", "Make the patient ready for surgery",
     "Reconcile dialysis timing, potassium, bleeding risk and anesthesia, and obtain consent that means something"),
    ("06", "plan-and-create-an-autogenous-fistula", "Plan and create an autogenous fistula",
     "Plan a fistula as a future cannulation site, follow the consent, and hand off what you found"),
    ("07", "grafts-and-alternative-configurations", "Grafts and alternative configurations",
     "Choose a graft for the right reasons and set its first-use conditions from the device and the patient"),
    ("08", "dialysis-catheters-and-central-veins", "Dialysis catheters and central veins",
     "Give every catheter an indication, a site that protects the future, and an exit date"),
    ("09", "maturation-and-the-first-cannulation", "Maturation and the first cannulation",
     "Tell a patent access from a usable one and agree a written first-use plan"),
    ("10", "recognize-a-failing-access", "Recognize a failing access",
     "Link a clinical change to anatomy before imaging decides for you"),
    ("11", "stenosis-and-endovascular-choices", "Stenosis and endovascular choices",
     "Treat the lesion that causes the problem, with the device that protects the next site"),
    ("12", "thrombosis-and-urgent-dialysis", "Thrombosis and urgent dialysis",
     "Run dialysis safety and access salvage in parallel, and treat the cause of the clot"),
    ("13", "hand-ischemia-and-neurologic-injury", "Hand ischemia and neurologic injury",
     "Recognize a threatened hand, grade it, and escalate before the thrill reassures anyone"),
    ("14", "aneurysm-and-life-threatening-bleeding", "Aneurysm and life threatening bleeding",
     "Read the skin over an aneurysm and stop a bleed with pressure, help and a plan"),
    ("15", "access-infection-and-sepsis", "Access infection and sepsis",
     "Treat sepsis first, then decide what source control the access needs"),
    ("16", "high-flow-and-central-venous-obstruction", "High flow and central venous obstruction",
     "Formulate the mechanism of breathlessness or arm swelling before choosing an operation"),
    ("17", "the-difficult-access-and-changing-modality", "The difficult access and changing modality",
     "Reconstruct the history, run a complex access conference, and revisit modality with the patient"),
    ("18", "kidney-care-beyond-the-access", "Kidney care beyond the access",
     "Route limb, renal artery and transplant problems to the right service and protect kidney function"),
    ("19", "philippine-documentation-and-quality", "Philippine documentation and quality",
     "Keep the clinical record, the claim and the audit separate, with honest definitions and denominators"),
    ("20", "the-integrated-vascular-access-service", "The integrated vascular access service",
     "Defend one patient&rsquo;s pathway and one service improvement, with every handoff owned"),
]

MODULES = []
for _id, _slug, _title, _sub in _ROWS:
    MODULES.append({"id": _id, "slug": _slug, "title": _title, "sub": _sub + ".", "part": _BLOCKS[_block(int(_id))],
                    "card_img": f"{HUB}-{_id}-card.webp", "hero_brief": _HB + _title})

# Module 8 images were replaced Nov 26 2026; new file names bypass the 30-day image cache.
MODULES[7]["hero_file"] = f"{HUB}-08-dialysis-catheters-and-central-veins-vignette-hero-v2"
