# Blueprint: Dialyzer Reuse in Modern Times (Deep-Dive Companion)
**Slug:** `guides/dialyzer-reprocessing-reuse.html`
**Status:** New guide
**Priority:** Tier 1 companion deep-dive to `green-nephrology.html`
**Target audience:** Hemodialysis patients and families (core); nephrology clinicians and trainees (appendix)
**Estimated sections:** 8 patient-facing + 1 clinical appendix + FAQ
**Clinical authority:** KDIGO 2026 Green Dialysis report; ANSI/AAMI RD47:2020; ISO 23500-3; CDC/HICPAC 2008
**Date of last evidence:** June 2026
**Source doc:** `blueprints/Blueprint_Dialyzer_Reprocessing_Modern_Times.docx`

---

## Positioning, in one line

> Reuse never died in the developing world; what is new is that high-income nephrology is being forced to reconsider it as a sustainability lever — even as the infection and quality-control cautions remain fully intact.

Companion to the parent **Green Nephrology 2026** guide. Same voice, same KDIGO 2026 framing, expanded physiology and process detail.

Angle (balanced): ~55% fundamentals (what reprocessing is, the membrane, the process), ~45% modern context (the green renaissance, KDIGO 2026, the global regulatory split, the honest environmental accounting, Philippine priorities).

---

## SEO / Meta

```
title: Dialyzer Reuse in Modern Times: Is It Making a Comeback?
description: What dialyzer reprocessing is, why the rich world dropped it, and why green nephrology and KDIGO 2026 are reviving reuse — explained by a nephrologist.
url: /guides/dialyzer-reprocessing-reuse.html
primary keyword: dialyzer reuse / dialyzer reprocessing
secondary keywords: is dialyzer reuse safe, hemodialysis filter reuse, peracetic acid dialyzer, dialyzer reuse Philippines, green nephrology dialyzer, KDIGO 2026 green dialysis, sustainable dialysis waste, AAMI RD47
internal links: green-nephrology (primary), slowing-ckd-progression, dialysis-coming-pre-eskd, dialysis-prescription, dialysis-access-infection, el-nino-heat-dialysis
schema: MedicalWebPage + FAQPage (6 questions)
og:locale: en_PH
theme-color: #0F1E33
```

---

## Section spine (implemented)

| # | ID | Section tag | Patient/Clinical |
|---|---|---|---|
| 1 | `#hook` | Hook · The Question Patients Actually Ask | Patient |
| 2 | `#what-dialyzer` | The Membrane | Patient |
| 3 | `#process` | Step by Step (6 steps) | Patient |
| 4 | `#germicides` | The Disinfectants (4-row table + ClearFlux mention) | Patient |
| 5 | `#walked-away` | The First Half of the Story | Patient |
| 6 | `#renaissance` | The Centerpiece — Green Renaissance | Patient |
| 7 | `#honest` | The Counter-Evidence | Patient |
| 8 | `#philippines` | In the Philippines + 6 questions checklist + red flags | Patient |
| 9 | `#faq` | FAQ (8 questions, cards) | Patient |
| 10 | `#appendix` | Clinical / Technical Appendix (subsections A–G) | Clinician |
| 11 | `#closing` | The Bottom Line | Both |

---

## Clinical appendix sub-headings

- **A.** Where reuse sits in the KDIGO 2026 framework (tier-2 / value equation)
- **B.** The global regulatory split (table: Japan/AU/EU vs US vs LMICs)
- **C.** Regulatory & standards framework (AAMI RD47, ISO 23500, CDC/HICPAC)
- **D.** Germicide modalities compared (peracetic / formaldehyde / glutaraldehyde / heat+citrate)
- **E.** Quality-assurance metrics (TCV ≥ 80%, integrity, residual germicide, labeling, water, audit)
- **F.** The physiology argument, restated (first-use syndrome → biocompatible membranes)
- **G.** One-line bottom-line for clinicians

---

## Wiring done

- [x] HTML file at `guides/dialyzer-reprocessing-reuse.html`
- [x] Tile added to `guides/index.html` under "Advanced & Emerging Topics" (count 13 → 14)
- [x] `related_guides.json` — new entry + back-reference from `green-nephrology.html`
- [x] `sitemap.xml` regenerated (129 URLs)
- [x] `patch_signature_position.py` clean
- [x] JSON-LD: MedicalWebPage + FAQPage
- [ ] Hero image generation (see image-planning blueprint)
- [ ] Run `patch_hero_*.py` once hero image is present

---

## Translations

English only (`en-PH`), matching parent Green Nephrology 2026 guide. No TL/CEB/KAP variants in this release.

---

## Image assets

See companion **image-planning blueprint** generated via `williamriveromd-infographic-skill`. Designed to maximize patient learning across the dialyzer physiology → reprocessing chain → germicide history → waste hierarchy → KDIGO value equation → unit-questions journey.

---

## Source & reference shortlist

- KDIGO 2026 Green Dialysis report — Barraclough KA, et al. Kidney Int. 2026;110:42–60. doi:10.1016/j.kint.2026.01.015
- Green Nephrology 2026 (companion guide) — /guides/green-nephrology.html
- UpToDate — "Reuse of dialyzers"
- PMC4086247 — Does hemodialyzer reuse have a place in current ESRD care?
- PMC6788837 — Dialyzer reuse: is it safe and worth it?
- PubMed 25149841 — Dialyzer reuse: justified cost saving for South Asian region
- PubMed 28839314 — Reusing dialyzer in low-income countries: cost saving with complex ethics
- ANSI/AAMI RD47:2020 — Reprocessing of hemodialyzers
- ISO 23500 series — Quality of dialysis fluids and water
- CDC/HICPAC Guideline for Disinfection and Sterilization (2008)
