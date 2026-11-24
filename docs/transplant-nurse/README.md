# Transplant Nurse subtrack · implementation notes

Renal Care Academy → Nephrology Nursing → Transplant Nurse. Built 24 November 2026 from the handoff blueprint in
`/Volumes/Storage/Renal Care Academy/KT Nurse` (CLAUDE.md, SYLLABUS.md, ASSESSMENT.md, PRACTICE-AND-JOBS.md, SOURCES.md, twelve module
manuscripts and quiz-bank.json).

## Routes

Flat Academy URLs (the site's convention; the blueprint's nested route was a candidate only):

| Page | Route |
|---|---|
| Subtrack hub | `/academy/transplant-nurse` |
| Modules 1–12 | `/academy/transplant-nurse-01-role-and-referral` … `/academy/transplant-nurse-12-capstone` |
| End-of-course knowledge check | `/academy/transplant-nurse-final-exam` |
| New calculator | `/guides/calc-tacrolimus-level-check` |
| Entry link 1 | `/academy/nephrology-nursing-11-transplantation-special-populations#transplant-nurse` |
| Entry link 2 | `/academy/nephrology-nursing#specialty` (specialty card) |

## How it is built

- Content: `tools/transplant_nurse/content/` (`course.py`, `m01.py`–`m12.py`, `images.py`). Edit these, never the pages.
- Generator: `generate_transplant_nurse.py` imports the Nephrology Nursing chrome (header, course CSS, quiz markup,
  glossary, related cards) so the subtrack matches its parent. `--patch` runs the /setup-guide pipeline,
  `--calc` rebuilds the calculator, `--check` validates only. Pages are published to `academy/` by
  `tools/academy/publish_academy.py` (prefix `transplant-nurse` added).
- References: PubMed-verified metadata in `data/transplant-nurse/refs_pubmed_raw.json`; per-page APA lists in
  `data/transplant-nurse/refs-overrides.json`. All pages pass `audit_apa_references.py` and
  `audit_acronym_expansion.py`.
- Quiz engine: `assets/nursing-course.js` gained two opt-in attributes (`data-stratify`, `data-pass`); pages
  without them behave exactly as before. Verified with jsdom: 10/12 → "Passed", 9/12 → "Not yet passed"; each
  sitting draws exactly one question from each of the 12 modules.
- `generate_nursing_course.py` now re-applies the two entry links after it republishes the parent course.

## What changed from the blueprint

- Each module expanded from about 280 words to a full lesson in the Academy voice (intuition → physiology →
  evidence with certainty language → bedside practice → Philippine context), with tables, flows and stop-and-call
  boxes.
- Evidence added and verified: Wolfe 1999 and Tonelli 2011 (survival), KDIGO 2020 candidate, 2017 living donor and
  2009 recipient guidelines, Muzaale 2014, Mjøen 2014 and Garg 2015 (donor risk), Declaration of Istanbul 2018,
  World Brain Death Project 2020, Moers 2009 (machine perfusion), BEST-Fluids 2023 (balanced crystalloid),
  Cochrane ureteric stents 2013, ELITE-Symphony 2007, BENEFIT 2016, Thölking 2014 (C/D ratio), Shuker 2015 (IPV),
  Dew 2007 (nonadherence), Schinstock 2019 (dnDSA and graft loss), Banff 2022, Bloom 2017 (dd-cfDNA),
  Ho 2022 (biopsy complications), Lim 2021 (desmopressin), 4th CMV consensus 2025, Limaye 2023 (letermovir),
  2nd BK consensus 2024, AST PJP, vaccine and TB guidance 2019, Engels 2011 (cancer), PTDM consensus 2024,
  Foster 2011 (transition), McAdams-DeMarco 2015 (frailty), Shah 2019 (pregnancy), Jagodage 2024 (teach-back).
- Philippine policy checked against official issuances: PhilHealth PC 2024-0035, PC 2025-0011, PC 2025-0012 and
  Advisory 2026-0026 (signed 31 March 2026; registry mandatory from 1 May 2026; manual Annex G until 30 April 2026;
  designated facility system users; compliance considered at contract renewal). Package amounts deliberately not
  reproduced.
- Knowledge checks: 15-item bank per module (random 5 per visit) plus 3 parallel exam items per module (36-item
  pool, one drawn per module, pass 10/12), all with per-option rationales.
- Each case keeps the blueprint's debrief (as Assess / Communicate / Teach / Escalate) and adds its second-round
  prompt from the syllabus.
- Calculators: new Tacrolimus Level Check (trough timing validity, C/D ratio, IPV); existing tools linked per module
  (KFRE, EPTS, KDPI, DGF risk, AKI staging, frailty, donor risk, tacrolimus dosing, allograft eGFR trend,
  interaction checker, transplant PROMs, dengue and leptospirosis risk, QI toolkit).

## Open items before release

1. Clinical review by a transplant nurse educator and a transplant nephrologist; benefits and regulatory review of
   Module 10 (blueprint acceptance check). The PC 2024-0035 PDF is not machine-readable; its annexes were not
   re-read.
2. `build_calc_app.py` could not finish in the remote workspace because many image files in the iCloud-synced
   folder are not downloaded locally; run it on the Mac (or let the sitemap workflow run it on push) so Calculo's
   offline manifest includes the new calculator.
3. Images: 13 heroes and 12 figures are specified in `GPT-IMAGE-PROMPTS.md`; pages show no figure until the files
   exist in `images/`.
4. The Academy landing page (`academy/index.html`) does not yet list the subtrack separately; it is reached from the
   Nephrology Nursing hub and Module 11.
