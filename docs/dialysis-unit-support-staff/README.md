# Dialysis Unit Support Staff subtrack · blueprint v2 and implementation notes

Renal Care Academy → Nephrology Nursing → Dialysis Unit Support Staff (orderlies and environmental service aides).
Built 24 November 2026 from the owner's blueprint package in `/Volumes/Storage/Renal Care Academy/Dialysis Unit Support Staff`
(CURRICULUM_BLUEPRINT.md, REGULATORY_REVIEW.md, JOB_DESCRIPTIONS.md, CLAUDE_CODE_HANDOFF.md, curriculum.json, sources.json, educator files),
under CLAUDE.md guide policies, the /setup-guide pipeline and the medical-teaching-standard skill, in the voice of the POD modules.
Status: **draft for clinical, infection prevention and regulatory review** (not published).

## What changed from the v1 blueprint

| Area | v1 | v2 |
|---|---|---|
| Modules | 12, about 6.5 KB each, one fictional case, 3 questions | 15 full lessons (intuition, physiology, evidence with certainty language, practice, Philippine context), each with a named Filipino case, debrief (Notice / Communicate / Do / Escalate), outcome, harder second round, 15-question bank (random 5 per visit, rationale for every option) and 3 parallel exam items |
| Hours | 48 (24 + 24) | 58 (30 guided + 28 practice), about 8 days; still Academy proposals, not minimums |
| Aseptic technique | inside hand hygiene and cleaning modules | new Module 3 (how germs and blood travel: chain of infection, hepatitis B and C survival, invisible blood) and new Module 5 (aseptic habits: clean-to-dirty, no double-dipping, clean and dirty zones, items that never return, hepatitis B isolation rules) |
| Waste | combined with linen | stand-alone Module 10 (segregation at source, DOH 2020 categories and colors (brown for chemical and pharmaceutical, yellow puncture-proof sharps containers) with "facility chart governs", dialysis waste streams, three-quarters rule, route, storage time in hot climates, authorized hauler, RA 9003, RA 6969, Joint DENR-DOH AO 2005-02); linen moved to Module 8 |
| Transport | one module | two modules: Module 11 (escort and transport, built on post-dialysis orthostatic hypotension physiology and fall data) and Module 12 (transfers, falls and protecting your back, with the NIOSH lifting equation and patient-handling limit) |
| Evidence | regulatory and guidance sources | plus 27 PubMed-verified studies and guidelines (APA 7, all pages pass `audit_apa_references.py`), each claim with calibrated verbs and stated limits |
| Calculators | none | new Support Staff Toolkit (`guides/calc-dialysis-support-staff-toolkit.html`): label dilution and contact-time planner (uses only label numbers), station turnover time budget, safe lift check (revised NIOSH equation, occasional lifts), audit tally with 95% Wilson interval; verified with jsdom against the worked examples |
| Images | none | image plan blueprint plus GPT prompt pack: 16 heroes and 43 teaching figures (Understand 12, Apply 25, Appreciate 6) |
| Capstone | six stations | kept, mapped to modules; critical failures never averaged; two observed occasions before authorization |

The v1 safety invariants are preserved everywhere: clinical clearance and patient departure precede station disinfection; environmental completion is not technical or clinical release; no generic dilution, universal contact time or imported waste colors; no learner pathway grants clinical or technician scope; no online action records competence; DOH, PhilHealth, PSN, PRC CPD and BLS recognition are not claimed.

## Evidence added (PubMed-verified)

CDC 2001 dialysis infection-control recommendations; Bond 1981 (hepatitis B survives drying for a week); Doerrbecker 2011 (hepatitis C up to 5 days on steel); Girou 2008 (11% of dialysis-unit surfaces with blood traces, hepatitis C RNA in some); Rao 2013 and Thompson 2009 (outbreaks from ordinary lapses); Mitchell 2015 (prior-occupant odds about 2.1); Pittet 2006 (five-step hand transmission); Pittet 2000 (hospital-wide hand hygiene program, before-after); Fuller 2011 (less hand hygiene when gloved); Tomas 2015 (46% contamination on PPE removal, cut by training); West 2019 (no killing after a disinfectant dries; lab, manufacturer co-author); Rutala 2019 (bundle approach); Carling 2006 (47% of targets cleaned); Ray 2017 (better cleaning, no fall in C. difficile); REACH 2019 (VRE infections RR 0.63); Donskey 2013; Dumas 2020 and 2021 (cleaning products and airway disease); Bouya 2020 (44.5% yearly needlestick prevalence); Kuhar 2013 (HIV PEP); Schillie 2013 and 2018 (hepatitis B protection and PEP); Cook 2006 (1.60 falls per person-year in older HD patients); Waters 1993 and 2007, NIOSH 1994 (lifting equation, 16 kg patient-handling limit); Engst 2005 and Lee 2019 (lift programs). Philippine and international policy sources from the v1 register are carried forward (DOH AO 2012-0001, PSN 2024, PhilHealth PC 2024-0029, DOH HCWM manual 2020, RA 10173, NPC 2024, RA 11058, NKTI 2025, OSHA 1910.1030, CDC station checklist, DART, Appendix B2, wall boxes).

## Routes and files

| Item | Path |
|---|---|
| Hub | `/academy/dialysis-unit-support-staff` |
| Modules | `/academy/dialysis-unit-support-staff-01-role-and-orientation` … `-15-records-improvement-and-capstone` |
| Knowledge check | `/academy/dialysis-unit-support-staff-final-exam` (one item per module, pass 12 of 15) |
| Calculator | `/guides/calc-dialysis-support-staff-toolkit` |
| Content | `tools/dialysis_support_staff/content/` (`course.py`, `m01.py`–`m15.py`, `images.py`) |
| Generator | `generate_dialysis_support_staff.py` (`--check`, `--patch`, `--calc`) |
| Calculator builder | `tools/dialysis_support_staff/build_calc_toolkit.py` |
| Image prompts | `tools/dialysis_support_staff/build_image_prompts.py` → `docs/dialysis-unit-support-staff/` |
| References | `data/dialysis-unit-support-staff/refs_pubmed_raw.json`, `refs-overrides.json` |
| Entry link | `academy/nephrology-nursing-07-hd-vascular-access-infection-prevention.html#support-staff` (added by the generator) |
| Publish prefix | `tools/academy/publish_academy.py` gains `dialysis-unit-support-staff` |

Checks run: `--check` clean; `audit_apa_references.py` 0 non-compliant citations across all 17 pages and the calculator; `audit_acronym_expansion.py` 0 violations; headless Chrome render of hub, Module 7 (light and dark) and the exam with no script errors (5 questions drawn per module, 15 in the exam).

## Open items before release

1. **Placement decision.** v1 placed the subtrack under Nephrology Nursing. The Academy taxonomy (Nov 2026) also has an Ancillary Staff Track. Decide which parent shows it on the Academy landing page; neither `academy/index.html` nor the Nephrology Nursing hub's specialty cards were changed.
2. **Clinical and regulatory review** by the clinical head, nurse educator, IPC, EVS, waste, safety and transport leads, and resolution of the v1 REGULATORY_REVIEW items (DC 2026-0112 and current DOH tool, PSN infectious-disease updates, readable PhilHealth provisions).
3. **Waste colors.** Aligned to Table 4 of the DOH Health Care Waste Management Manual, 4th edition (2020); each unit should still confirm against its posted facility chart.
4. **Run on the Mac:** `python3 generate_dialysis_support_staff.py --calc --patch`, then `build_calc_app.py` and `generate_latest_calculators.py`, so Calculo's offline manifest and the calculators page include the toolkit (the remote workspace had no image files, so those outputs were not shipped).
5. **Images:** 16 heroes and 43 figures specified in `GPT-IMAGE-PROMPTS.md`; pages show no figure until the files exist in `images/`.
6. **Educator package:** the v1 printable logs, local SOP worksheet, preceptor guide and task authorization record remain in the owner's folder and are not yet rendered as Academy pages.
