# Blueprint: Getting Fit for a Kidney Transplant — Prehabilitation, Nutrition and Life After Surgery

**File:** `guides/transplant-prehabilitation.html`
**Canonical:** `https://renalcarematters.com/guides/transplant-prehabilitation.html`
**Status:** New guide. Implementation handoff for Claude Code (`/setup-guide transplant-prehabilitation.html`), to be opened in its own thread.
**Shape:** Dual-mode (Patients & Families / Clinicians). Patient mode EN/TL/CEB/KAP; clinician mode English-only. Patient side is the priority; this is a practical, motivating guide.
**Index section:** `lifestyle` (violet `#7c3aed`) or `nutrition` (green `#2e6b3e`); match where `exercise-guide-ckd.html` sits in `guides/index.html`.
**Template to copy:** `guides/exercise-guide-ckd.html` (patient-first lifestyle guide) for layout; `guides/anemia-management.html` for dual-mode wiring if the exercise guide is single-mode.
**Origin:** Journal review of 6 November 2026, item NG-5 (priority 5).
**Evidence check:** Skim level (6 Nov 2026). ✔ = read in the paper; **[verify]** = confirm in full text. Build all citations from PubMed (APA 7).
**Review status:** Draft blueprint. Not medically reviewed.

---

## 0. Why this guide

The word "prehabilitation" appears nowhere on the site. Frailty is common among transplant candidates, it predicts worse outcomes after transplant, and people on the waiting list often lose fitness while they wait. The Journal of Renal Nutrition (May 2026) editorial reviews the evidence for multimodal prehabilitation (exercise + nutrition + psychological support), centered on the first RCT in kidney transplant candidates (FRAILMar). Two companion pieces in the same issue support the nutrition side: diet quality in transplant recipients and an exercise-plus-nutrition meta-analysis in nondialysis CKD. The September 2026 GOAL trial (already cited in `hemodialysis-elderly.html` and `calc-frailty-assessment.html`) adds the lesson that a one-off assessment without follow-through does not change outcomes.

**Honest framing (must run through the whole guide):** prehabilitation improves fitness measures in small trials, but no trial has yet shown better transplant outcomes (graft survival, complications, length of stay) in kidney transplant candidates **[verify against the editorial's conclusion]**, and gains faded after the supervised program ended in FRAILMar. The guide should motivate without promising a better transplant.

**Out of scope:** transplant eligibility criteria (link `kidney-transplant.html`), immunosuppression, living donor evaluation (link `organ-donation-philippines.html`).

---

## 1. Source papers (on the Mac, `~/Downloads/Journals/`)

| # | File | Type | Contribution | Key data |
|---|---|---|---|---|
| S1 | `Journal of Renal Nutrition_20260629/The-Emerging-Role-of-Prehabilitation-in-Kidney-Tra.pdf` | Editorial, Lorenz et al., J Ren Nutr 2026;36(3):335–340, doi 10.1053/j.jrn.2026.04.001 | Spine: definition, evidence, open questions | ✔ Frailty common in candidates (US estimate 91,738 frail candidates). ✔ Prehabilitation = multimodal: exercise, nutritional optimization, psychological support. ✔ Mostly small pilot studies, exercise-only. ✔ FRAILMar RCT (single center, Spain): 121 waitlisted candidates, mean age 63, 76% men, 40% Fried ≥2; aerobic + resistance + inspiratory muscle training 3×/week for 8 weeks (in person or video) + protein supplement after each session vs standard care; improved exercise capacity (CPET maximal workload), handgrip, respiratory muscle strength, rectus femoris thickness; one-third of eligible patients declined; at 6 months, despite monthly phone support, physical activity, muscle thickness and frailty scores worsened again. ✔ Non-transplant surgery evidence: moderate-intensity exercise gives the largest preoperative gains; multimodal prehab improves preoperative capacity but postoperative benefit uncertain; preoperative nutrition supplements reduce infectious complications (meta-analysis, 2,475 patients) **[verify RR]**. ✔ Home-based programs: better reach, poorer adherence/higher attrition than center-based. ✔ Open question: optimal timing when waiting time is unpredictable (non-transplant prehab is 2–6 weeks). **[verify]** the editorial's list of research priorities and any statement on transplant-outcome RCTs. |
| S2 | `Journal of Renal Nutrition_20260629/Diet,-Dietary-Guideline-Adherence,-and-Clinical-De.pdf` | Cross-sectional (Active Care after Transplantation study, Netherlands), J Ren Nutr 2026;36(3):341–352, doi 10.1053/j.jrn.2025.10.008 | After-transplant diet | ✔ 167 recipients (~147 days post-transplant; 40% female; age 51.9). ✔ Low adherence: fruit ≥200 g/day 22%; vegetables ≥200 g/day 28%; fiber ≥25 g/day 26%; plant-to-total protein ≥0.50 only 12%. ✔ Diet similar to the general population. ✔ Lower adherence with deceased donor and polypharmacy. Dutch guidelines; translate to Filipino food cautiously. |
| S3 | `Journal of Renal Nutrition_20260629/Efficacy-of-Combined-Exercise-and-Nutritional-Inte.pdf` | Systematic review/meta-analysis (Japan), J Ren Nutr 2026;36(3):410–418, doi 10.1053/j.jrn.2025.10.018 | Exercise + nutrition in nondialysis CKD | ✔ 5 RCTs, 339 participants. ✔ VO₂ peak +2.70 mL/kg/min (95% CI 1.22–4.18); no difference in kidney function. ✔ Few studies, heterogeneity, risk of bias; more RCTs needed. |
| S4 | `Kidney International_20260922/A-cluster-randomized-controlled-trial-(GOAL-trial).pdf` and `Comprehensive-geriatric-assessment-for-older-peopl.pdf` | Cluster RCT + commentary | Context: assessment alone is not an intervention | Use the figures already verified in `guides/hemodialysis-elderly.html` (GOAL sub-block). GOAL was not done in transplant candidates; say so. |

**External anchors to verify on PubMed:** FRAILMar primary publication (cited in S1); McAdams-DeMarco frailty and post-transplant outcomes papers (cited in S1); KDIGO 2020 transplant candidate evaluation guideline (frailty assessment statement and grade); KDOQI 2020 nutrition guideline (protein targets for transplant recipients); Fried phenotype original paper (for the calculator link).

---

## 2. Head, meta, structured data

```
<title>Getting Fit for a Kidney Transplant: Prehabilitation, Nutrition and Recovery · W Rivero, MD</title>
description: Waiting for a kidney transplant? How exercise, protein and mental preparation (prehabilitation) build strength before surgery, what the first trials found, and how to eat well after transplant.
keywords: prehabilitation kidney transplant, frailty kidney transplant Philippines, exercise before transplant, protein dialysis exercise, diet after kidney transplant
canonical: https://renalcarematters.com/guides/transplant-prehabilitation.html
og image: images/transplant-prehabilitation-og.webp (1200×630)
JSON-LD: Article + MedicalWebPage; about: Kidney Transplantation; Frailty; Preoperative Exercise; Diet. audience Patient + MedicalAudience.
localStorage keys: wgmr-prehab-mode / wgmr-prehab-lang
```

---

## 3. Page structure

House chrome per CLAUDE.md. Hero: H1 "Getting Fit for a Kidney Transplant"; subtitle "Build strength while you wait, recover better after"; tag "Transplant · Exercise · Nutrition".

**One-minute answer (patient, 4 languages)**
1. Many people waiting for a transplant become weaker while on dialysis. Getting stronger before surgery ("prehabilitation") is safe for most and helps you feel and move better.
2. A good plan combines exercise (walking or cycling plus light strength work), enough protein and calories, and support for stress and mood.
3. Early trials show better fitness and strength, but the benefit fades if you stop, so make it a routine, not a short program.
4. After transplant, most people need to shift to a heart-healthy diet with more vegetables, fruit and fiber; ask your team what is right for you.

**Safety box (amber, both modes):** before starting, ask your nephrologist or transplant team, especially if you have chest pain, heart disease, a fistula arm (no heavy weights on it), very high potassium, or recent hospital stay. Stop exercising and seek care for chest pain, fainting, severe breathlessness, or palpitations.

---

## 4. Section map

### Patient mode (EN/TL/CEB/KAP)

| Anchor | Pill | Content |
|---|---|---|
| `#why-fitness` | Why | Frailty explained (weak grip, slow walking, exhaustion, weight loss, low activity — Fried criteria in plain words); why it matters for surgery and recovery |
| `#what-prehab-is` | Prehab | Three pillars: exercise, nutrition, mind; FRAILMar in plain words (8 weeks, 3 sessions/week, protein after each session; stronger legs, lungs and grip; benefits faded after 6 months) |
| `#exercise-plan` | Exercise | Starter weekly plan: walking/cycling, chair stands, light weights, breathing exercises; intradialytic cycling option; home vs center; tracking progress (link `exercise-guide-ckd.html`, `calc-exercise-hr-zones.html`, `calc-physical-activity-met.html`) |
| `#nutrition-before` | Eat before | Adequate protein and energy on dialysis (link `eating-on-dialysis.html`, `calc-ckd-nutrition-rx.html`); protein timing after exercise; Filipino protein sources within potassium/phosphorus limits |
| `#mind` | Mind | Stress, sleep, mood; family support; screening (link `ckd-mental-health-sleep.html`, `calc-phq9.html`) |
| `#keep-going` | Keep going | Why gains fade (FRAILMar); habits; group or buddy exercise; dialysis-unit programs |
| `#after-transplant` | After | Diet after transplant (S2): more fruit, vegetables, fiber, plant protein; watch weight gain; food safety with immunosuppression; drug–food interactions (grapefruit/pomelo with tacrolimus **[verify]**) |
| `#questions` | Ask | Question builder: "Am I frail?", "Can I join a program?", "How much protein should I eat?" |
| `#faq` | FAQ | Will exercise get me a kidney sooner? Is it safe with a fistula? Can I exercise on dialysis days? |

### Clinician mode

| Anchor | Pill | Content |
|---|---|---|
| `#md-frailty` | Frailty | Prevalence, outcomes, measurement (Fried, CFS, SPPB **[verify which S1 cites]**); link `calc-frailty-assessment.html`, `calc-sarcopenia-sarcf.html` |
| `#md-evidence` | Evidence | S1 synthesis: pilot studies, FRAILMar appraisal (single center, 121 patients, one-third declined, surrogate outcomes, waning at 6 months), non-transplant prehab meta-analyses, S3 (VO₂ peak +2.70, no kidney-function change) |
| `#md-prescription` | Prescription | Components and dose (moderate-intensity aerobic + resistance + inspiratory muscle training), protein supplementation, psychological support; center vs home trade-offs; timing problem with unpredictable waits |
| `#md-goal-lesson` | GOAL lesson | Assessment without an intervention pathway does not change outcomes (S4); embed prehab into routine dialysis care |
| `#md-post-tx-diet` | Post-Tx diet | S2 numbers and determinants (deceased donor, polypharmacy); KDOQI targets **[verify]** |
| `#md-philippines` | Philippines | Access to cardiac/pulmonary rehab-style programs, dialysis-unit exercise, PhilHealth coverage for rehab **[verify]**; link `cardiac-rehab-ckd-post-mi.html` |
| `#md-research` | Gaps | Open questions from S1 (timing, delivery, maintenance, transplant outcomes) |

**Evidence Snapshot (`.v` ≤ 8 chars)**

| `.v` | `.l` |
|---|---|
| n=121 | FRAILMar: first prehabilitation RCT in transplant candidates |
| 8 wk | FRAILMar: 3 sessions/week + protein supplement |
| 6 mo | Gains in fitness and muscle faded after the program ended |
| +2.70 | VO₂ peak (mL/kg/min) with exercise + nutrition in CKD (5 RCTs) |
| 12% | Recipients meeting the plant-protein target after transplant |

---

## 5. Figures

1. Hero vignette (patient-only): Filipino patient doing chair stands at home with a family member counting, dialysis schedule on the wall.
2. Three-pillar infographic (infographic skill): exercise · nutrition · mind, with weekly targets.
3. Simple figure: "fitness while waiting" curve — decline on usual care vs maintained with prehab vs fade after stopping (conceptual; label as illustrative, not data).
4. Code-native SVG (not AI): S2 adherence bars (fruit 22%, vegetables 28%, fiber 26%, plant protein 12%).

---

## 6. Calculators and related guides

Link: `calc-frailty-assessment.html`, `calc-sarcopenia-sarcf.html`, `calc-exercise-hr-zones.html`, `calc-physical-activity-met.html`, `calc-ckd-nutrition-rx.html`, `calc-nutrition-screening.html`, `calc-phq9.html`, `calc-epts.html`.
Related: `kidney-transplant.html`, `exercise-guide-ckd.html`, `physical-activity-sports-ckd.html`, `eating-on-dialysis.html`, `hemodialysis-elderly.html`, `organ-donation-philippines.html`, `muscle-building-supplements-ckd.html`, `ckd-mental-health-sleep.html`. Add this guide to `related_guides.json` for `kidney-transplant.html` and `exercise-guide-ckd.html`.

## 7. Glossary seed

CFS, CI, CKD, CPET, KDIGO, KDOQI, KT, PHQ-9, RCT, RRT, SPPB, VO₂ peak. Terms: prehabilitation, frailty, sarcopenia, inspiratory muscle training, resistance training, plant-to-total protein ratio, polypharmacy.

## 8. Build checklist

1. Read S1–S3 in full (and the FRAILMar primary paper via PubMed); resolve every **[verify]**.
2. Confirm KDIGO transplant-candidate and KDOQI nutrition statements and grades.
3. Build from the template; four languages in patient mode; dark-mode check.
4. `/setup-guide transplant-prehabilitation.html`; APA + acronym audits; `validate_hero_grid.py`; `generate_latest_guides.py`; `generate_sitemap.py`.
5. Independent verification pass before pushing.
