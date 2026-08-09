# Accuracy & Credibility Remediation Report

**Project:** renalcarematters.com
**Workstream:** Immediate accuracy and credibility remediation (KDIGO reconciliation)
**Date:** 2026-08-09
**Branch:** `claude/renalcarematters-guides-update-phouyb`
**Status:** Code + validation complete — **pending nephrologist review before deployment.**

This report accompanies the correction of four patient-facing guides whose wording,
calculators, decision rules, or evidence attribution did not fully match current KDIGO
guidance. Every clinically material correction was mirrored across all four languages
(English, Tagalog, Cebuano, Kapampangan). A "Last updated: Aug 9, 2026" badge (4 languages),
a JSON-LD `dateModified`/`article:modified_time` stamp, and an "Evidence review updated
August 2026" notice were added to each guide.

---

## 1. Files changed

| File | Nature of change |
|---|---|
| `guides/metabolic-acidosis-ckd.html` | Reframe 22–26 as lab reference interval, not a KDIGO treatment target; Practice-Point labeling; association vs causation; calculator disclaimer |
| `guides/contrast-nephropathy.html` | Retitle to Contrast-Associated AKI (CA-AKI); CA-AKI vs contrast-induced distinction; don't-delay messaging; Mehran renamed PCI-specific; volume heuristic; KDIGO 2026 draft-labeled |
| `guides/polycystic-kidney-disease.html` | Re-anchor to final KDIGO 2025 ADPKD; **MIC calculator disabled** (unsafe fixed-htTKV logic) with non-interactive replacement + morphology gate; staged tolvaptan; REMS localization; conditional water; SGLT2i correction |
| `guides/anemia-management.html` | Population selector (HD/non-HD/PD/transplant/pediatric); HD vs non-HD iron thresholds; ESA-before-HIF-PHI; withhold limits 700/40%; calculator safeguards |
| `guides/index.html` | Contrast tile title/teaser/spotlight + search synonyms updated to CA-AKI |
| `latest_guides.json` | Regenerated so corrected contrast + metabolic titles are in sync |

URLs were preserved — no file was renamed or deleted.

---

## 2. High-risk claims removed or rewritten

### Metabolic acidosis
- Removed the universal **"KDIGO 2024 target bicarbonate range 22–26"** and "treat below 22" framing everywhere (hero deck, Evidence-Snapshot cards, reference band, clinician stat card, clinician narrative, references list, image alt text).
- **22–26 mmol/L** now described as a *laboratory reference interval*, not a KDIGO treatment target.
- **`<18 mmol/L`** now labeled a KDIGO 2024 **Practice Point** *example*, not a graded recommendation or a universal prescription threshold.
- Corrected the clinician paragraph that had called the alkali guidance a *graded recommendation*; now the ungraded Practice Point (3.10.1–3.10.2), with explicit note that BiCARB (2020) and VALOR-CKD (2023) did not show benefit on hard outcomes and the precise threshold is uncertain.
- Added **"association does not prove causation"** framing for the bicarbonate–outcome relationship.
- Softened the marketing title from "That Accelerates Kidney Loss" → "Linked to Faster Kidney Loss."

### Contrast
- New visible/H1/meta/JSON-LD title: **"Contrast and the Kidneys: Understanding Contrast-Associated AKI Without Delaying Needed Care."**
- Distinguished **CA-AKI** (temporal) from **contrast-induced AKI** (causal subset); added "association does not prove causation"; a post-contrast creatinine rise no longer "confirms" causation.
- Added route/context section (routine IV CT vs intra-arterial PCI vs unstable emergency); explicit statement not to defer a life-saving scan solely for low eGFR (**benefit exceeds the risk**).
- Removed "one of the leading causes of hospital-acquired AKI" (as proven causal) and unqualified "largely preventable"; blanket "aggressive hydration 1.5 mL/kg/hr" → individualized isotonic saline for high-risk without overload; "iso-osmolar only" → "low- or iso-osmolar"; universal 72-h creatinine → risk-based.
- Medication section: no universal holds; metformin reframed (lactic-acidosis-if-AKI, not direct nephrotoxicity); ACEi/ARB/SGLT2i individualized; ACR referenced. Added **Philippine implementation note**.
- KDIGO 2026 AKI/AKD content **labeled a public-review draft.**

### ADPKD
- Re-anchored to the **final KDIGO 2025 ADPKD guideline** (added as reference #1); "What changed in KDIGO 2025" panel + Last-evidence-review line.
- Removed "tolvaptan eligibility confirmed" auto-verdict and the "must enroll in REMS" instruction; REMS explained as a **US FDA** requirement; **Philippine implementation note** added.
- "≥3 L/day most accessible disease-modifying intervention" corrected to KDIGO's conditional ~2–3 L/day (eGFR ≥30, not on tolvaptan, no contraindication), supportive not proven; hyponatremia/HF/advanced-CKD cautions; PH heat/typhoon individualization.
- SGLT2i "early TKV-benefit" claim removed; states KDIGO 2025 does not advise SGLT2i specifically for ADPKD; mTOR/non-diabetic-metformin not recommended to slow ADPKD; categorical "never NSAIDs" replaced with a nuanced pain pathway; risk-based (not universal) aneurysm screening.

### Anemia
- Removed "oral iron is largely ineffective at this stage" and "IV route is standard of care."
- Split **HD** (IV generally preferred; ferritin ≤500 & TSAT ≤30% initiation) from **non-dialysis CKD** (ferritin <100 & TSAT <40%, or 100–300 & TSAT <25%; oral or IV individualized).
- Withhold limits corrected to **ferritin >700 or TSAT ≥40%**; suspend during active infection.
- ESA: no universal Hb trigger; lowest effective dose; **do not maintain Hb ≥11.5 g/dL**; no CV/kidney-outcome overclaim.
- HIF-PHI: **ESA generally preferred**; do not combine; malignancy/thrombosis cautions; reassess ~3–4 months; **"long-term safety remains uncertain"**; PH implementation note.
- Added KDIGO 2026 terminology: **"systemic iron deficiency"** and **"iron-restricted erythropoiesis."**

---

## 3. Calculator logic changed

| Guide | Tool | Change |
|---|---|---|
| Metabolic acidosis | Acid-base / anion-gap calculator | Never displayed a KDIGO target or auto-prescribed; added disclaimer that the shown bicarbonate range is a lab interval (not a KDIGO target) + a "What this tool cannot decide" note. |
| Contrast | Mehran / CI calculators | Renamed **"Original Mehran PCI-Associated AKI Risk Score"**; output = "post-PCI AKI risk under the original model" (not "contrast nephropathy probability"); PCI-only scope warnings; max-volume relabeled a historical heuristic (no "safe" language); verdicts reworked to a discussion pathway; "What this tool cannot decide" notes. Scoring math untouched. |
| ADPKD | Mayo Imaging Classification / tolvaptan-eligibility | **DISABLED.** It assigned Class 1A–1E from invalid fixed htTKV cutoffs, had no morphology gate, and output an automatic eligibility verdict + REMS instruction. Replaced with a non-interactive explanation, a typical-vs-atypical morphology gate, a prognostic-only growth-rate table (1C flagged non-automatic), and a pointer to the validated Mayo calculator + specialist. |
| Anemia | `calcAnemia`, `calcERI` | Required population selector first; thresholds branched by population; infection/inflammation guard; high-ferritin/low-TSAT not called proven deficiency; consider/evaluate/discuss wording; Hb unit guard; confounder warnings; "What this tool cannot decide" note. |

---

## 4. Visual assets flagged for regeneration

Alt text/captions were corrected in the HTML, but these images have **outdated claims baked into their pixels** and should be re-rendered:

- **Metabolic acidosis:** `metabolic-acidosis-bicarb-explainer`, `metabolic-acidosis-kidney-damage`, `metabolic-acidosis-treatment`, `metabolic-acidosis-monitoring`, `metabolic-acidosis-ckd-clinician-infographic` (all show "KDIGO target 22–26" / "treat <22").
- **Contrast:** `contrast-injury-mechanism` (CIN-as-cause framing — this is also the current OG/Twitter share image), `contrast-nephropathy-vignette-hero` (old CIN concept). A **new 1200×630 OG card** prompt was produced (`contrast-ca-aki-og-card.png`); once generated, `og:image`/`twitter:image` + width/height/alt will be wired and `latest_guides.json` re-synced.
- **ADPKD:** `pkd-visual-clinical-abstract-umj`, `pkd-treatment-hydration-bp-nsaid-lifestyle`, `pkd-living-well-water-exercise-monitoring-daily` (3–4 L/day water, "NSAIDs absolutely contraindicated").
- **Anemia:** `anemia-kdigo-targets-infographic`, `anemia-thresholds-reference`, `anemia-diagnosis-infographic`, `anemia-iv-iron-algorithm` (universal thresholds, ferritin-800 hold).

---

## 5. Verification / build commands run

- Custom regression check (forbidden-string absence + required-string presence + hero badge in 4 languages + `dateModified`): **PASS** on all four guides.
- `audit_apa_references.py` (all four guides): **0 non-compliant**.
- `audit_acronym_expansion.py` (all four guides): **0 violations**.
- `validate_hero_grid.py`: **all hero-grids valid**.
- `generate_latest_guides.py`: regenerated; `generate_sitemap.py --dry-run`: already in sync (387 URLs).
- HTML tag-balance parity checked against `origin/main` for each edited guide (no new imbalance); `node --check` on anemia/ADPKD JS (agents).

---

## 6. Remaining uncertainties — require physician review

- **Numeric thresholds** (metabolic `<18`; anemia HD ferritin ≤500/TSAT ≤30, non-HD <100/<40 or 100–300/<25, withhold >700/≥40%) were applied from the handoff's KDIGO specification and should be confirmed against the source KDIGO PDFs before deployment.
- **ADPKD MIC growth-rate boundaries** shown (1A <1.5%…1E >6%/yr) are the KDIGO-aligned figures; the exact validated Irazabal class-assignment equation was deliberately **not** implemented (calculator disabled). Confirm before any future re-enable.
- **Citations/DOIs:** the KDIGO 2025 ADPKD DOI could not be independently confirmed with egress restricted (verified article URL used instead); the contrast guide's KDIGO 2024 and ACR reference metadata use institutional/report form rather than invented volume/page numbers. Verify against PubMed/CrossRef.
- **Metabolic title** softening ("Linked to Faster Kidney Loss") is a reversible editorial choice.
- Legacy shorthand **"CIN"** still appears in a few non-material contrast labels/captions (now accurate as the defined older term); could be swept in a later pass.

---

## 7. Physician-review matrix

| Page | Claim / threshold | Source | Evidence status | Location | Sign-off |
|---|---|---|---|---|---|
| Metabolic acidosis | Alkali therapy to prevent acidosis with clinical implications; `<18 mmol/L` example | KDIGO 2024 CKD, PP 3.10.1–3.10.2 | **Practice Point (ungraded)** | Hero, ref-band, clinician narrative | ☐ |
| Metabolic acidosis | 22–26 = laboratory reference interval, not a treatment target | Lab convention / KDIGO 2024 | Definitional | Deck, cards, calculator disclaimer | ☐ |
| Metabolic acidosis | No proven kidney-outcome benefit from bicarbonate normalization | BiCARB 2020, VALOR-CKD 2023 | RCT (neutral) | Clinician narrative | ☐ |
| Contrast | CA-AKI vs contrast-induced AKI (temporal vs causal) | KDIGO 2024; ACR | Terminology | Intro, #what, #context | ☐ |
| Contrast | Do not defer a life-saving scan solely for low eGFR | KDIGO 2024; ACR | Consensus | #context | ☐ |
| Contrast | Original Mehran score is PCI-specific, not a universal CT score | Mehran 2004 derivation | Model-scope limitation | Calculator | ☐ |
| Contrast | KDIGO 2026 AKI/AKD is a public-review **draft** | KDIGO 2026 draft (Mar 2026) | **Draft — verify final** | Update notice, references | ☐ |
| ADPKD | MIC is prognostic; requires typical morphology + validated calculator | KDIGO 2025 ADPKD | Recommendation + method | Disabled-calc replacement | ☐ |
| ADPKD | Tolvaptan: eGFR ≥25 + rapid-progression evidence + SDM (initiation vs continuation) | KDIGO 2025 ADPKD | Recommendation | Tolvaptan section | ☐ |
| ADPKD | Water ~2–3 L/day conditional; not guaranteed disease-modifying | KDIGO 2025 ADPKD | Suggestion (conditional) | Water/climate section | ☐ |
| ADPKD | REMS is US-specific; follow PH FDA product information | US FDA / PH FDA | Regulatory (localized) | Philippine implementation note | ☐ |
| Anemia | HD vs non-HD iron thresholds are different | KDIGO 2026 anemia | Recommendation / PP | Targets table, calculator | ☐ |
| Anemia | Do not use ESA to maintain Hb ≥11.5 g/dL; lowest effective dose | KDIGO 2026 anemia | Recommendation | ESA section | ☐ |
| Anemia | ESA generally preferred over HIF-PHI; long-term safety uncertain | KDIGO 2026 anemia | Suggestion | HIF-PHI section | ☐ |

_Generated as part of the KDIGO reconciliation remediation. Do not deploy until the sign-off column is complete._
