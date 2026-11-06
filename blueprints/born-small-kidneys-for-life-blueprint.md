# Blueprint: Born Small, Kidneys for Life

**File:** `guides/born-small-kidneys-for-life.html`
**Canonical:** `https://renalcarematters.com/guides/born-small-kidneys-for-life.html`
**Status:** New guide, implementation handoff for Claude Code (`/setup-guide born-small-kidneys-for-life.html`)
**Shape:** Dual-mode (Patients & Families / Clinicians); patient mode in EN/TL/CEB/KAP, clinician mode English-only
**Index section:** `nephrology` (teal `#1a6b72`), tile icon `data-icon="kidney"`
**Template to copy:** `guides/anemia-management.html` (dual-mode wiring, Evidence Snapshot aside, patient-scoped vignette). Question-builder copy/print pattern: `guides/first-nephrology-visit-guide.html` (`qb-*`).
**Source manuscript:** `born-small-kidneys-for-life-guide.md` (supplied draft, dated 6 November 2026). This blueprint overrides it wherever §4 lists a correction.
**Evidence check:** 6 November 2026 (Asia/Manila). Primary study, both neonatal consensus papers, and all journal references verified against PubMed metadata; the two consensus papers read in full text (PMC).
**Review status:** Prepared draft. Not yet medically reviewed. Do not write a review date, `datePublished`, or "Last Reviewed" value that has not happened; the patch scripts stamp those at merge.

---

## 0. What changed from the source blueprint

The supplied blueprint was framework-agnostic because no repository had been inspected. The repo is now inspected, and checking the two neonatal consensus papers in full turned up clinical gaps that matter for exactly this guide's audience.

| # | Change | Why |
|---|---|---|
| 1 | Route is `guides/born-small-kidneys-for-life.html`, not extensionless | Site canonical rule (CLAUDE.md, Deployment). Related-reading links in the manuscript are extensionless and must become `.html`. |
| 2 | Architecture mapped to real repo conventions: self-contained HTML, master CSS in block 1, all bespoke CSS in block 2, logic in `assets/born-small-planner.js` with a Node test in `tests/born-small-planner.cjs` | Matches `assets/ckd-anemia-2026.js` + `tests/ckd-anemia-2026.cjs`. Avoids master-CSS clobbering. |
| 3 | **SGA/FGR is now part of the neonatal follow-up pathway**, not absent from it | Starr 2024 set birth weight <1,500 g as a high-risk criterion explicitly as a proxy for growth restriction. The 2026 preterm workgroup report (Slagle) lists IUGR/FGR, SGA, and VLBW as modifying risk factors that move a 28 to <34-week infant into the high-risk, comprehensive-assessment group. The manuscript's §15 omitted this. |
| 4 | Infants born ≥34 weeks with **Stage 1** AKI get a comprehensive assessment at 2 years; the high-risk ≥34-week group is defined precisely | Starr 2024. The manuscript said only "severe or recurrent AKI." |
| 5 | Critical cardiac disease pathway added | Starr 2024 has a separate pathway; the planner already asks about congenital heart disease but the clinician text never says what follows. |
| 6 | "Comprehensive kidney assessment" now names its components (BP, creatinine **plus cystatin C** for eGFR, urine albumin/creatinine, ± ultrasound) | Both consensus papers. Creates a valid, scoped link to the existing `calc-ckid-u25-egfr.html`. |
| 7 | "Not a lifelong schedule" message rebalanced | Starr 2024 states CKD risk is lifelong, screening should continue beyond 2 years, and should be strongly considered around puberty, personalized by shared decision-making. The guide must say both things: no fixed universal schedule, and the risk does not expire at age 2. |
| 8 | Discharge "kidney disease present" criteria stated, with the creatinine threshold discordance flagged | Starr 2024 uses SCr ≥0.5 mg/dL; Slagle 2026 writes >0.5 mg/dL. Neither is a general pediatric or adult cutoff. |
| 9 | Planner gains four deterministic prompts (very low birth weight, preterm + documented SGA/FGR, cardiac, adolescent growth period) | Each maps to a consensus population, phrased as a question, never a risk label. |
| 10 | Study data lives in one JSON file; a test asserts the static no-JS table matches it | Resolves the "single source" requirement on a no-build static site. |
| 11 | Study chart is code-native SVG, never an AI-generated image | Image generators misdraw numbers. AI prompts are reserved for conceptual figures (prompt pack in `blueprints/image-prompts-born-small-kidneys-for-life.md`). |
| 12 | Cross-organ physiology made explicit (nephron number → glomerular hemodynamics → BP and albuminuria; preterm birth → later diabetes risk) with certainty labels | Medical-teaching standard: intuition → physiology → evidence → application, with verbs matched to evidence. |
| 13 | References rebuilt in APA 7 from PubMed metadata; four undated web sources flagged because they will fail the audit gate | `audit_apa_references.py` requires a `(YYYY)` year. |
| 14 | Unverifiable study details flagged for full-text confirmation before publish | The Danish paper is not in PMC. The abstract verifies the core numbers; several methods details in the manuscript do not appear in the abstract. |

---

## 1. Purpose and audience

The guide helps a reader keep a birth history alive in the medical record, understand why it makes the kidney less tolerant of stress, and walk into a clinic visit with the right questions. It should reassure without dismissing the evidence. Primary readers are parents, adolescents, and adults born small, early, or after a difficult newborn course. Secondary readers are pediatricians, family physicians, internists, nephrologists, nurses, and trainees.

The patient voice is warm and specific. The clinician voice is appraisal-grade. Neither voice should imply that a birth weight is a diagnosis.

Out of scope, permanently: a personalized AKI, CKD, nephron-count, or dialysis-risk calculator; SGA or FGR inferred from raw weight and gestation; fluid prescriptions; pediatric BP classification inside this page.

---

## 2. Head, meta, and structured data

```
<title>Born Small, Kidneys for Life: Birth History and Kidney Health · W Rivero, MD</title>
description: Being born early, small for gestational age, or after a hard newborn course can lower kidney reserve. What the 2026 Danish study found, what to check, and a birth-history visit planner.
keywords: small for gestational age kidney, fetal growth restriction kidney, low birth weight kidney Philippines, preterm birth CKD, nephron endowment, acute kidney injury children, NICU graduate kidney follow-up
canonical: https://renalcarematters.com/guides/born-small-kidneys-for-life.html
og:type article · og:locale en_PH · og:site_name Renal Care Matters
og:image: https://renalcarematters.com/images/born-small-kidneys-for-life-og.webp  (1200 × 630; width/height/alt tags required)
og:image:alt: Born Small, Kidneys for Life — renalcarematters.com
twitter:card summary_large_image (same image)
JSON-LD: Article + MedicalWebPage on renalcarematters.com; author = real author record (W.G.M. Rivero, MD);
         about: Infant, Small for Gestational Age; Premature Birth; Acute Kidney Injury; Chronic Kidney Disease
         audience: Patient + MedicalAudience
         datePublished / dateModified: leave to patch_published_time.py and patch_last_reviewed.py
```

No `williamriveromd.com` anywhere. Run the pre-push grep from CLAUDE.md.

---

## 3. Page structure (house chrome)

```
<body>  (pre-paint mode-restore snippet first, injected by patch_mode_restore.py; key wgmr-born-small-mode / wgmr-born-small-lang)
header.site-header → a.brand · div.header-lang (glb-en/tl/ceb/kap) · nav.header-nav (direct child)
div.audience-tabs → "Patients & Families" | "Clinicians"
section.hero → div.hero-grid
    div.hero-copy           H1, subtitle (Nunito Sans), hero-meta (Reading time, Published, References — added by patchers; NO author row)
    aside.hero-cards.mode-physician   Evidence Snapshot (§6)
    figure.hero-figure.mode-patient > .hero-vignette   (patient-only vignette; clinician hero has none)
</section>
div.container   one-minute answer + urgent-help callout   (outside hero-grid — never a hero-grid child)
nav pills (mode-patient-pill / mode-physician-pill)
<main>  patient sections P1–P10 (class="section mode-patient"), clinician sections C1–C10 (class="section mode-physician")
</main>
<!-- GLOSSARY-START --> details.glossary-acc <!-- GLOSSARY-END -->
<!-- REFERENCES-ACC-START --> details.ref-acc (built by patch_references_accordion.py --overrides) 
calc-cards-wrap (clinician-scoped)
<!-- DR CARD --> div.dr-card-wrap → div.related-guides → footer.guide-footer  (no references line in footer)
float controls, symptom widget, image-lightbox.js (added by patchers)
```

**Hero copy**

- H1 (EN): Born Small, Kidneys for Life
- Subtitle (EN): Why your birth history belongs in your kidney care
- Hero tag: Kidney development · Prevention
- Drafts for native-speaker review (do not ship unreviewed):
  - TL: Ipinanganak na Maliit, Bato Habambuhay / Bakit kabilang ang kasaysayan ng iyong pagsilang sa pangangalaga ng iyong bato
  - CEB: Natawo nga Gamay, Kidney sa Tibuok Kinabuhi / Nganong apil ang kasaysayan sa imong pagkatawo sa pag-atiman sa imong kidney
  - KAP: Mibait a Malati, Batu Angga king Bie / Nanung kailangan ing kasaysayan ning kekang pangabait king pamanalaga king kekang batu

**One-minute answer and urgent help.** Keep the manuscript's four bullets and the "Need help now?" text (red `alert`, ⛔). Add one sentence to the help box: "For a newborn or young infant, fewer wet diapers, poor feeding, or unusual sleepiness needs same-day assessment." The urgent box must render in both modes.

---

## 4. Manuscript corrections (apply before building)

Each item gives the location in the supplied manuscript and the replacement. Wording follows the certainty ladder: observational findings use "is associated with," consensus uses "recommends," mechanism uses "may" or "is thought to."

**4.1 §15 Follow-up after neonatal care — replace the whole section with:**

> **Consensus, with population limits.** The 2024 NICU-graduate consensus (Starr et al.) covers three groups: infants born before 34 weeks, critically ill infants with AKI, and infants with critical cardiac disease. All of them should leave the NICU with a properly measured BP, a serum creatinine, and kidney-health education for the family. Kidney disease already present at discharge (creatinine ≥0.5 mg/dL, BP above the 95th percentile, treated hypertension, nephrocalcinosis, or CAKUT) warrants pediatric nephrology follow-up. The 2026 preterm workgroup report (Slagle et al.) writes the creatinine criterion as >0.5 mg/dL; both describe a consensus discharge threshold for preterm infants, not a diagnostic cutoff for older children or adults.
>
> *Preterm, 28 to <34 weeks, no added risk factor (at risk):* BP at every health encounter, kidney education, and a 2-year review; a comprehensive assessment is optional and may be done at the primary clinician's discretion.
> *Preterm, high risk:* birth before 28 weeks, or 28 to <34 weeks with a modifying risk factor. Starr 2024 names birth weight <1,500 g (chosen to capture growth-restricted infants) and AKI or dialysis. Slagle 2026 adds documented IUGR/FGR and SGA (<10th percentile). These infants should have a comprehensive kidney assessment at 2 years of age, earlier if new risks appear.
> *Born ≥34 weeks with AKI:* Stage 1 AKI → comprehensive assessment at 2 years. Stage 2–3 AKI, dialysis, recurrent AKI, or AKI with severe comorbidity (ECMO, congenital diaphragmatic hernia, HIE) → assessment within 6 months of discharge and again at 2 years. A normal 2-year assessment returns the child to routine care with annual BP and continued education.
> *Critical cardiac disease:* comprehensive assessment by 2 years; with an added risk (Stage 2–3 AKI, single ventricle, heart transplant, HIE, preterm <34 weeks, ECMO, or a daily nephrotoxic drug at discharge), assessment every 6 months through age 2 plus annual nephrology follow-up.
>
> A comprehensive assessment means BP, serum creatinine **and** cystatin C to estimate GFR (the consensus suggests the CKiD U25 equation), urine albumin/creatinine (urine protein/creatinine is acceptable, interpreted against age-specific normals), and kidney ultrasound at the nephrologist's discretion. Equations based on creatinine and cystatin C were not designed for infants under 1 year and need cautious interpretation.
>
> The consensus focuses on the first 2 years because GFR matures by then, not because risk ends. Its authors note that CKD risk is lifelong and that screening should continue past age 2, especially around puberty, with frequency set by shared decision-making. Neither paper tested whether this schedule improves outcomes; both are expert consensus. In the Philippines, arrange what primary or pediatric care can provide now; an incomplete panel should never block a BP check or a referral.

**4.2 §8 life-stage table, first row.** Replace the question with: "Were my baby's blood pressure and creatinine checked before going home, was there any kidney injury, and who will do the two-year kidney check?"

**4.3 §8, add a row after Adolescence:** "Puberty and growth spurts | 'Should my kidney checks be repeated while I am growing quickly?'" (Starr 2024 limitation statement.)

**4.4 §10 FAQ "Should everyone born below 2,500 grams see a nephrologist?"** Append: "Babies born before 28 weeks, under 1,500 grams, or early with growth restriction or newborn kidney injury have a recommended two-year kidney check, which a pediatrician can often coordinate."

**4.5 §2 nephron paragraph.** Keep. Add one sentence of cross-organ physiology after the kitchen analogy, walked back to the real mechanism: "In the body, the 'busier stations' are the remaining nephrons, each filtering more blood at higher pressure. Over many years that extra workload may show up as higher blood pressure or protein in the urine, which is why your doctor checks both."

**4.6 §13 Mechanism (clinician) — add after the first paragraph:**

> **Cross-organ chain (certainty labels in brackets).** Fewer nephrons at birth [established developmental physiology; human autopsy and animal data, Sutherland & Black 2023] → compensatory single-nephron hyperfiltration and glomerular hypertension [mechanism supported in animal models, cited by Slagle 2026] → albuminuria and systemic hypertension → further nephron loss [mechanistic hypothesis for the human life course]. Preterm birth is also associated with later type 1 and type 2 diabetes and insulin resistance at population level [observational, summarized by Slagle 2026], a second route by which kidney and cardiometabolic risk compound. Maternal preeclampsia and tobacco exposure are associated with offspring kidney disease [observational]. None of these links was measured in the Danish cohort.

**4.7 §12 appraisal — items to confirm against the Danish full text before publish.** The PubMed abstract confirms: cohort dates (Aug 1995–Feb 2022), group sizes (585,624 and 21,900), SGA definition (<10th percentile), all four 25-year risks, both aHRs with CIs, and that AKI was defined biochemically from plasma creatinine. The following manuscript statements are not in the abstract and must be checked against the paper (Table 3 and Methods) or removed: the 25-year risk CIs; median follow-up (9.2 and 7.7 years); laboratory follow-up end (July 2024); cohort entry 30 days after the estimated due date; "approximately 60% lacked baseline creatinine"; the adjustment set; recurrent-event and measured-baseline sensitivity results; volume/issue reading 110(5). If any cannot be confirmed, delete it rather than soften it.

**4.8 §12, add LGA context** (abstract-verified): LGA 25-year risks were 3.1% without defects and 10.1% with defects, close to AGA. Show in the clinician table only; do not show an LGA hazard ratio unless confirmed from the paper.

**4.9 §14 guideline anchors.** Keep, and state grades honestly: the KDIGO 2024 statement listing preterm birth and small gestational size as CKD risk factors sits in a risk-factor table and practice points, not a graded recommendation. Say "KDIGO 2024 lists" rather than "KDIGO recommends."

**4.10 Related reading.** Replace the three extensionless URLs with `neonatal-acute-kidney-injury-clinician.html`, `how-to-properly-assess-kidney-function.html`, `aki-does-not-end-at-discharge.html`.

**4.11 Acronyms.** Expand on first body use in EN: SGA, AGA, LGA, FGR, IUGR, LBW, VLBW, AKI, CKD, NICU, KRT, BP, GFR, eGFR, CAKUT, HIE, ECMO, NSAID, CI, HR, aHR, KDIGO, AAP, WHO, CKiD, KFRE, ACR, U25. (BP is on the audit's exempt list; expand anyway in patient mode.)

---

## 5. Section map, stable anchors, and teaching sequence

Every section follows intuition → physiology → evidence → application. Patient sections carry all four languages. Nav pill labels are bare display chrome.

### Patient mode

| Anchor | Pill | Content (manuscript §) | Component | Teaching move |
|---|---|---|---|---|
| `#patient-overview` | Overview | Opening, one-minute answer | intro callout, red help alert | Intuition: "your kidneys were built before you were born" |
| `#birth-terms` | 4 terms | §1 | 4-card grid + overlap note (Fig 2) | Distinguish weight, timing, size-for-age, growth process |
| `#kidney-reserve` | Reserve | §2 + 4.5 | Fig 3 mechanism figure; teal alert "Birth weight cannot count nephrons" | Physiology: fewer stations, more work each |
| `#study-findings` | The study | §3 | Study Findings Explorer (§8) + static table | Evidence: absolute numbers first |
| `#aki-and-ckd` | AKI vs CKD | §4 | purple alert (myth vs mechanism) | Different outcomes, different studies |
| `#birth-history` | Records | §5 | checklist | Application |
| `#kidney-checks` | Checks | §6 | table | Application; what each test answers |
| `#daily-protection` | Protect | §7 | 3 green/amber alerts | Medication, fluids, growth |
| `#life-stages` | Life stages | §8 + 4.2, 4.3 | Fig 4 timeline + HTML step list | Handoffs, puberty row |
| `#visit-planner` | Planner | §9 | Planner (§7) | Prepare the visit |
| `#patient-faq` | FAQ | §10 + 4.4 | `.qa-item` disclosures | Plain answers |

### Clinician mode (English-only)

| Anchor | Pill | Content | Component |
|---|---|---|---|
| `#clinical-position` | Position | §11 | evidence-label key (`tier-badge`: Guideline / Consensus / Observational / Practice proposal) |
| `#study-appraisal` | Appraisal | §12 + 4.7, 4.8 | full table (AGA/SGA/LGA), caveats list |
| `#developmental-mechanism` | Mechanism | §13 + 4.6 | Fig 3 reused; cross-organ chain |
| `#clinical-assessment` | Assessment | §14 + 4.9 | `.algo-card` 4-step workflow (Fig 6 optional image) |
| `#neonatal-follow-up` | NICU grads | §15 replaced by 4.1 | stratification table (§9) |
| `#referral` | Referral | §16 | red/amber alerts |
| `#clinical-transitions` | Transitions | §17 | copyable record template |
| `#calculator-scope` | Tools | §18 | scope text + calc link cards |
| `#evidence-uncertainty` | Uncertainty | §19 | table |

A direct link to any clinician anchor switches to clinician mode and focuses the heading (the pre-paint restorer reads the mode key; add a hash check in the same snippet so `#neonatal-follow-up` opens clinician mode without post-paint swapping).

---

## 6. Evidence Snapshot (clinician hero, `.ov-stat`, `.v` ≤ 8 characters)

| `.v` | `.l` |
|---|---|
| 607,524 | Danish birth cohort, 1995–2022 (observational) |
| aHR 1.20 | SGA vs AGA, first AKI, no major birth defects |
| aHR 1.45 | SGA vs AGA, first AKI, with major birth defects |
| +5/1000 | Absolute 25-yr difference, no defects (3.7% vs 3.2%) |
| +53/1000 | Absolute 25-yr difference, with defects (15.2% vs 9.9%) |
| 34–36 wk | Nephrogenesis approaches completion |
| 2 yr | Consensus comprehensive review for high-risk NICU graduates |

`+53/1000` is 8 characters; keep it. Use tokens, not literal colors, and check dark mode.

---

## 7. Birth History & Kidney Visit Planner

### 7.1 Files

- `assets/born-small-planner.js`: pure functions, UMD export (`module.exports` for Node, `window.BornSmallPlanner` in browser): `normalizeWeight`, `normalizeGestation`, `validate`, `buildSummary`, `buildPrompts`, `toPlainText`.
- Guide markup: the form with ids prefixed `bs-` (`bs-audience`, `bs-weight`, `bs-weight-unit`, `bs-oz`, `bs-ga-weeks`, `bs-ga-days`, `bs-sga`, `bs-fgr`, `bs-nicu`, `bs-aki`, `bs-dialysis`, `bs-cakut`, `bs-cardiac`, `bs-concern`, `bs-source`), the summary region `bs-summary` (`aria-live="polite"`), buttons `bs-generate`, `bs-copy`, `bs-print`, `bs-clear`, `bs-print-blank`.
- CSS for the planner, explorer, and print rules goes in the **second** `<style>` block.
- Note: `assets/calc-handoff.js` keys off `-age`, `-weight`, `-scr` id suffixes on calculator pages. This is not a calculator page and the `bs-weight` id must not be loaded with that script; confirm `patch_calc_handoff.py` skips non-`calc-*` files.

### 7.2 Input contract

Unchanged from the source blueprint (`HistoryAnswer` tri-state, `SourceConfidence`, no name, date of birth, address, hospital number, lab values, uploads, or free text). Only "who is this for" is required. Blank means unknown, never "no." Nothing preselected except "unknown."

### 7.3 Normalization and validation

Keep every rule from the source blueprint: kg × 1,000; lb × 453.59237 + oz × 28.349523125 with integer pounds and ounces 0 to <16; weeks a nonnegative integer, days 0–6, blank days preserved as unspecified; reject zero, negative, nonfinite, or malformed input (`2abc`, `2,5,0`); typo-confirm below 300 g, above 7,000 g, below 22 or above 42 weeks; compare unrounded, round only for display; never infer SGA, FGR, or AGA; keep dialysis-yes with AKI-no and ask for clarification; inline errors plus a focusable error summary; never export a stale summary.

Add one threshold label: a known normalized weight strictly below 1,500 g is displayed as "reported birth weight below 1,500 g" (the consensus very-low-birth-weight criterion). At exactly 1,500 g it is not below. Same unrounded comparison.

### 7.4 Output contract

Never output a risk tier, score, percentage, diagnosis, test order, or computed follow-up date. Always output: what you entered (with "reported" labels for recollection), records that may help, questions for the visit, blank clinician-plan lines (next review, tests if any, medicine advice, responsible clinician), and the scope line: "This summary organizes reported history. It does not diagnose kidney disease or predict your risk."

### 7.5 Deterministic prompt rules

Editorial organization rules, not a clinical algorithm. Show all matches, deduplicated, in table order, never ranked by urgency.

| ID | Trigger | Prompt |
|---|---|---|
| `Q-base` | always | The four universal questions in manuscript §9 |
| `Q-record` | any history answer unknown, or source ≠ medical record | "Could a birth record or newborn discharge summary clarify this history?" |
| `Q-weight` | known weight < 2,500 g | "Does my birth weight, together with the rest of my history, change the assessment you recommend?" |
| `Q-vlbw` (new) | known weight < 1,500 g | "Was a kidney check around age two planned or done, and what did it show?" |
| `Q-gestation` | reported completed weeks < 37 | "Was a kidney follow-up plan included in neonatal care?" |
| `Q-preterm-growth` (new) | reported weeks < 34 **and** documented SGA or FGR = yes | "Babies born early who were also small for their age are often offered a kidney check around age two. Was that planned or done?" |
| `Q-growth` | documented SGA or FGR = yes | "Can we keep the documented size and growth history distinct in my record?" |
| `Q-neonatal` | AKI or dialysis = yes | "Can we review the newborn kidney event and the discharge follow-up plan?" |
| `Q-congenital` | CAKUT or cardiac = yes | "Should the existing specialist and my usual clinician coordinate the kidney follow-up plan?" |
| `Q-cardiac` (new) | cardiac = yes | "Has my heart team included kidney checks in the regular heart follow-up?" |
| `Q-current` | current concern = yes | "Who is following this concern, and when should I be reviewed?" |
| `Q-inconsistent` | dialysis = yes and AKI ≠ yes | "The reported dialysis and AKI history need clarification from the newborn record." |
| `Q-growth-years` (new) | audience = adolescent **and** any of weeks < 37, weight < 2,500 g, SGA/FGR yes, AKI/dialysis yes | "Should my kidney checks be repeated while I am growing quickly?" |

`Q-vlbw` and `Q-preterm-growth` must work when gestation days are blank: a reported completed week of 33 already satisfies "< 34."

### 7.6 Privacy

Memory only. No localStorage, sessionStorage, URL parameters, analytics payloads, logs, or network requests carrying entered values (the guide's own `wgmr-born-small-mode/lang` keys are unrelated and allowed). Verify the symptom-checker widget and any analytics snippet do not capture form or DOM text. Copy uses `navigator.clipboard.writeText` (pattern in `first-nephrology-visit-guide.html`) with a selectable `<textarea readonly>` fallback on failure. Clear wipes form and summary.

### 7.7 No-JS state

The blank form renders with a visible "Print blank planner" path (CSS print of the empty form with writable lines). Generate/copy buttons are hidden by a `.js-only` class that the script removes.

---

## 8. Study Findings Explorer

### 8.1 Data file

`assets/born-small-evidence-data.json` is the single numeric source. Shape:

```json
{
  "source": "Fog-Høyer et al., Kidney International 2026;110(5):1294–1303. doi:10.1016/j.kint.2026.06.037",
  "endpoint": "First AKI episode, creatinine-defined",
  "horizon_years": 25,
  "estimate_type": "Aalen–Johansen cumulative risk (competing risks)",
  "cohorts": [
    {"id": "no-defects", "label": "Without major birth defects", "n": 585624,
     "groups": [
       {"id": "AGA", "risk_pct": 3.2, "ci": [3.1, 3.3], "ahr": null},
       {"id": "SGA", "risk_pct": 3.7, "ci": [3.5, 4.0], "ahr": 1.20, "ahr_ci": [1.13, 1.27]},
       {"id": "LGA", "risk_pct": 3.1, "ci": null, "ahr": null}
     ],
     "expected": {"diff_pp": 0.5, "diff_per1k": 5}},
    {"id": "defects", "label": "With major birth defects", "n": 21900,
     "groups": [
       {"id": "AGA", "risk_pct": 9.9, "ci": [9.3, 10.6], "ahr": null},
       {"id": "SGA", "risk_pct": 15.2, "ci": [13.2, 17.6], "ahr": 1.45, "ahr_ci": [1.29, 1.64]},
       {"id": "LGA", "risk_pct": 10.1, "ci": null, "ahr": null}
     ],
     "expected": {"diff_pp": 5.3, "diff_per1k": 53}}
  ],
  "verification": {"abstract_verified": ["n", "risk_pct", "ahr", "ahr_ci"], "confirm_from_full_text": ["ci"]}
}
```

The `ci` values come from the manuscript and are not in the abstract; leave the `verification` block until they are checked against Table 3, then delete it.

### 8.2 Behavior

Title "What the Danish study observed"; subtitle "Estimated first AKI over 25 years in study groups, not an individual prediction." Two panels on a shared 0–20% axis (zero-based, never truncated), AGA and SGA bars with CI whiskers when the CI is confirmed. Toggle percent ↔ per 1,000 (`per1k = pct × 10`; differences `SGA − AGA`). No CIs on differences, no risk ratios from HRs, no "your risk," no prompt asking which group describes the reader. Clinician mode shows LGA rows and HRs in the table, never as bar heights.

The static `<table>` is authored in HTML with the same numbers so the page works without JS. `tests/born-small-planner.cjs` parses that table and asserts equality with the JSON, so the two copies cannot drift.

Chart: inline SVG built by the guide's script from the JSON, `role="img"` with `aria-labelledby` title and description, color-independent labels, tokens for color, dark-mode checked. It is not an AI image.

---

## 9. Clinician stratification table (`#neonatal-follow-up`)

Render as a `.table-wrap` table with a caption naming both sources. All rows are **Consensus**.

| Population | Group | Before discharge | Follow-up |
|---|---|---|---|
| All three groups below | — | Measured BP, serum creatinine, family kidney education | Kidney disease at discharge → pediatric nephrology |
| Preterm 28 to <34 wk, no modifier | At risk | as above | BP every encounter; education; 2-yr review, comprehensive assessment optional |
| Preterm <28 wk, or 28 to <34 wk with modifier (BW <1,500 g; AKI/dialysis; IUGR/FGR or SGA per 2026 report) | High risk | as above | Comprehensive assessment at 2 yr, sooner if new risks |
| ≥34 wk, Stage 1 AKI | At risk | as above | Comprehensive assessment at 2 yr |
| ≥34 wk, Stage 2–3 AKI, dialysis, recurrent AKI, or AKI with ECMO/CDH/HIE | High risk | as above | Within 6 mo of discharge and at 2 yr; normal at 2 yr → routine care, annual BP |
| Critical cardiac disease | At risk | as above | Comprehensive assessment by 2 yr |
| Critical cardiac disease + added risk (Stage 2–3 AKI, single ventricle, transplant, HIE, <34 wk, ECMO, daily nephrotoxin) | High risk | as above | Every 6 mo through 2 yr + annual nephrology |

Footer note under the table: "Expert consensus from US workshops (2024). Not tested for outcome benefit, not calibrated to Philippine practice, and not a schedule for every child born under 2,500 g. Risk continues beyond age 2."

---

## 10. Calculator link cards (clinician mode only)

Confirmed to exist in `guides/`:

- `calc-pediatric-bp.html`: "Pediatric BP percentile (AAP 2017). For children 1–17 years; not for infants or adults."
- `calc-ckid-u25-egfr.html`: "CKiD U25 eGFR (creatinine and cystatin C), the equation the NICU-graduate consensus suggests. Not validated under 1 year."

Do not link `calc-kfre.html`, adult eGFR calculators, `calc-pediatric-dehydration.html`, or `calc-pediatric-growth-percentiles.html` from this page; none answers the guide's question and two invite misuse.

---

## 11. Graphics plan

All AI-generated assets follow the two-stage pipeline: Stage 1 prompts in `blueprints/image-prompts-born-small-kidneys-for-life.md` (full required schema, approved fonts named, `renalcarematters.com` attribution, light backgrounds, no guideline or journal names), Stage 2 via `williamriveromd-local-image-generator`. Every inline figure gets `<picture>` (webp + png), real `width`/`height`, and a v2.0 figcaption with `p.fig-desc` and, where acronyms appear, `dl.fig-abbrevs`.

| # | Asset | Skill | Size | Placement | Notes |
|---|---|---|---|---|---|
| 1 | Vignette hero | `williamriveromd-hero-vignette` (Scaffold B still-life, archetype I, top-down) | 2048 × 2048 | `figure.hero-figure.mode-patient` | No people, no text. Decorative beside H1 → `alt=""` is acceptable |
| 2 | Four birth terms | `williamriveromd-simple-figure` (Scaffold E variant, 2 × 2 grid) | 1792 × 1024 | `#birth-terms` | HTML cards carry the same text; image is supplementary |
| 3 | Nephron development and reserve | `williamriveromd-biomedical-mechanism-figure` | 1792 × 1024 | `#kidney-reserve`, reused in `#developmental-mechanism` | Footer label "Conceptual. Birth weight does not measure nephron number." |
| 4 | Life-course handoffs | `williamriveromd-simple-figure` (Scaffold C, 6 steps incl. puberty) | 1792 × 1024 | `#life-stages` | No ages or dates on steps except "about age 2" |
| 5 | OG card | `williamriveromd-infographic-skill` | 1200 × 630 (fixed) | `og:image` | Light background, title text only |
| 6 | Clinician pathway (optional) | `williamriveromd-simple-figure` (Scaffold A, flat flowchart, no 3D/icons) | 1024 × 1536 | `#clinical-assessment` | HTML `.algo-card` is the primary; image may be skipped |
| — | Study chart | code-native SVG | responsive | `#study-findings` | Not generated by AI, ever |

Naming: `images/born-small-kidneys-for-life-vignette-hero.{png,webp}`, `images/born-small-kidneys-for-life-NN-<desc>.{png,webp}`, `images/born-small-kidneys-for-life-og.{png,webp}`.

---

## 12. Glossary & abbreviations accordion

**Abbreviations:** AAP, ACR (albumin-to-creatinine ratio), AGA, aHR, AKI, BP, CAKUT, CDH, CI, CKD, CKiD, ECMO, eGFR, FGR, GFR, HIE, HR, IUGR, KDIGO, KFRE, KRT, LBW, LGA, NICU, NSAID, SGA, U25, VLBW, WHO.

**Terms:** nephron; nephrogenesis; nephron endowment; kidney reserve (renal functional reserve); hyperfiltration; gestational age (completed weeks + days); percentile; corrected age; cystatin C; creatinine; competing risk; hazard ratio; absolute risk; confidence interval; cohort study; consensus statement.

Header string in four languages via `data-lang` spans. Add any new acronym to the global list in `audit_acronym_expansion.py` if missing.

---

## 13. References (APA 7, for `refs.json` overrides)

Numbering follows the manuscript. Journal items verified against PubMed metadata on 6 November 2026.

1. Fog-Høyer, S., Heide-Jørgensen, U., Nørgaard, M., Henriksen, T. B., Carrero, J.-J., & Christiansen, C. F. (2026). Fetal growth restriction and acute kidney injury in children and young adults. <em>Kidney International</em>, <em>110</em>(5), 1294–1303. <a href="https://doi.org/10.1016/j.kint.2026.06.037">https://doi.org/10.1016/j.kint.2026.06.037</a>
2. World Health Organization. *Preterm and low birth weight infants* [Web page]. **Year needed:** the page could not be fetched from this session; confirm a dated WHO source (for example the WHO preterm birth fact sheet) or the audit will fail.
3. Lees, C. C., Stampalija, T., Baschat, A., da Silva Costa, F., Ferrazzi, E., Figueras, F., Hecher, K., Kingdom, J., Poon, L. C., Salomon, L. J., & Unterscheider, J. (2020). ISUOG practice guidelines: Diagnosis and management of small-for-gestational-age fetus and fetal growth restriction. <em>Ultrasound in Obstetrics &amp; Gynecology</em>, <em>56</em>(2), 298–312. <a href="https://doi.org/10.1002/uog.22134">https://doi.org/10.1002/uog.22134</a>
4. Sutherland, M. R., & Black, M. J. (2023). The impact of intrauterine growth restriction and prematurity on nephron endowment. <em>Nature Reviews Nephrology</em>, <em>19</em>(4), 218–228. <a href="https://doi.org/10.1038/s41581-022-00668-8">https://doi.org/10.1038/s41581-022-00668-8</a>
5. Crump, C., Sundquist, J., Winkleby, M. A., & Sundquist, K. (2019). Preterm birth and risk of chronic kidney disease from childhood into mid-adulthood: National cohort study. <em>BMJ</em>, <em>365</em>, l1346. <a href="https://doi.org/10.1136/bmj.l1346">https://doi.org/10.1136/bmj.l1346</a>
6. Kidney Disease: Improving Global Outcomes (KDIGO) CKD Work Group. (2024). KDIGO 2024 clinical practice guideline for the evaluation and management of chronic kidney disease. <em>Kidney International</em>, <em>105</em>(4S), S117–S314. <a href="https://doi.org/10.1016/j.kint.2023.10.018">https://doi.org/10.1016/j.kint.2023.10.018</a>
7. Starr, M. C., Harer, M. W., Steflik, H. J., Gorga, S., Ambalavanan, N., Beck, T. M., Chaudhry, P. M., Chmielewski, J. L., Defreitas, M. J., Fuhrman, D. Y., Hanna, M., Joseph, C., Kwiatkowski, D. M., Krawczeski, C. D., Liberio, B. M., Menon, S., Mohamed, T. H., Rumpel, J. A., Sanderson, K. R., . . . Selewski, D. T. (2024). Kidney health monitoring in neonatal intensive care unit graduates: A modified Delphi consensus statement. <em>JAMA Network Open</em>, <em>7</em>(9), e2435043. <a href="https://doi.org/10.1001/jamanetworkopen.2024.35043">https://doi.org/10.1001/jamanetworkopen.2024.35043</a> *(PubMed lists a trailing collective author; confirm on the journal page whether it, not Selewski, is the final author in the APA ellipsis form.)*
8. Slagle, C. L., Chmielewski, J. L., Rumpel, J. A., Sanderson, K. R., Schuh, M. P., Starr, M. C., Segar, J. L., Ambalavanan, N., Askenazi, D., Selewski, D., Charlton, J. R., & Harer, M. W. (2026). Kidney care at NICU discharge and follow-up recommendations for preterm infants <34 weeks. <em>Journal of Perinatology</em>, <em>46</em>(3), 498–507. <a href="https://doi.org/10.1038/s41372-026-02597-x">https://doi.org/10.1038/s41372-026-02597-x</a> *(Confirm whether a collective author follows Harer.)*
9. Flynn, J. T., Kaelber, D. C., Baker-Smith, C. M., Blowey, D., Carroll, A. E., Daniels, S. R., de Ferranti, S. D., Dionne, J. M., Falkner, B., Flinn, S. K., Gidding, S. S., Goodwin, C., Leu, M. G., Powers, M. E., Rea, C., Samuels, J., Simasek, M., Thaker, V. V., Urbina, E. M., & Subcommittee on Screening and Management of High Blood Pressure in Children. (2017). Clinical practice guideline for screening and management of high blood pressure in children and adolescents. <em>Pediatrics</em>, <em>140</em>(3), e20171904. <a href="https://doi.org/10.1542/peds.2017-1904">https://doi.org/10.1542/peds.2017-1904</a> *(19 named authors + subcommittee = 20, so all are listed; confirm the subcommittee name on the journal page.)*
10. National Institute of Diabetes and Digestive and Kidney Diseases. *Keeping kidneys safe: Smart choices about medicines* [Web page]. **Year needed** (use the page's "last reviewed" year).
11. NHS. *Dehydration* [Web page]. **Year needed** (use "page last reviewed").
12. National Institute of Diabetes and Digestive and Kidney Diseases. *Kidney disease in children* [Web page]. **Year needed.**

Optional addition, already APA-formatted elsewhere on the site (`why-kidney-disease-is-silent.html`): Mueller, T. F., & Luyckx, V. A. (2024). Renal functional reserve: Compensation, concealment and clinical implications. <em>Current Opinion in Nephrology and Hypertension</em>, <em>33</em>(1), 130–135. https://doi.org/10.1097/MNH.0000000000000930. Use it only if §2/§13 cite it.

Author counts from PubMed: Flynn 2017 has 19 named authors (Flynn through Urbina) plus one collective entry, so all 20 are listed. Starr 2024 has 28 named authors plus a collective entry, so it takes the 21+ form (first 19, ellipsis, final author). Slagle 2026 has 12 named authors plus a collective entry. Recount on the journal pages before rendering.

---

## 14. Claim ledger (medical-teaching standard)

| Claim | Rung | Verb | Source | Status |
|---|---|---|---|---|
| Nephrogenesis approaches completion at ~34–36 wk | Established physiology | "is completed by about" | Sutherland 2023; Slagle 2026 | Verified |
| Prematurity and growth restriction can lower nephron number | Established developmental physiology (human autopsy + animal) | "can reduce" | Sutherland 2023 | Verified (review) |
| Fewer nephrons → hyperfiltration → later BP/albuminuria | Mechanistic hypothesis for humans | "may," "is thought to" | Slagle 2026 (animal); Sutherland 2023 | Label as mechanism |
| SGA associated with higher first-AKI hazard to early adulthood | Observational | "is associated with" | Fog-Høyer 2026 | Abstract-verified |
| Absolute 25-yr differences 5 and 53 per 1,000 | Descriptive arithmetic | "were" | Fog-Høyer 2026 | Computed from verified values |
| Preterm birth associated with diagnosed CKD to age 43 (aHR 1.94; <28 wk 3.01) | Observational | "is associated with" | Crump 2019 | Verified |
| Follow-up schedules for NICU graduates | Expert consensus | "recommends" | Starr 2024; Slagle 2026 | Full text read |
| BP measurement <3 yr when SGA, VLBW, or preterm <32 wk | Guideline | "recommends" | Flynn 2017 (AAP) | Confirm Table 9 wording when writing |
| Preterm/SGA are CKD risk factors | Guideline risk-factor listing (ungraded) | "lists" | KDIGO 2024 | Confirm table number |
| Preterm birth associated with later diabetes | Observational | "is associated with" | Slagle 2026 (summary) | Secondary; cite as such |
| Screening improves outcomes in this population | Not tested | — | — | Say explicitly that it is untested |

Surrogates to label as surrogates: eGFR, albuminuria, BP. The patient-important outcome in the Danish study is AKI (a laboratory-defined event); dialysis and death were not reported as outcomes here.

---

## 15. Index, related guides, discovery

- `guides/index.html`: add a tile in `data-section="nephrology"`, `data-icon="kidney"`, `data-tags="new nephrologist pediatric clinician patient prevention"`, rich `data-text` (SGA, FGR, IUGR, low birth weight, preterm, nephron endowment, NICU graduate, AKI, CKD, Danish cohort, consensus follow-up, birth history planner, Philippines). Add the filename to the `dual` Set in the page script. Add to the relevant "Start Here" pathway if one covers prevention or children.
- `related_guides.json` entry: `["neonatal-acute-kidney-injury-clinician.html", "ckd-children-young-adults.html", "how-to-properly-assess-kidney-function.html", "aki-does-not-end-at-discharge.html", "personal-medical-journal-health-history.html", "nsaid-kidney-injury.html", "why-kidney-disease-is-silent.html", "ckd-and-pregnancy.html"]`.
- Reciprocal: add `born-small-kidneys-for-life.html` to the arrays of `neonatal-acute-kidney-injury-clinician.html`, `how-to-properly-assess-kidney-function.html`, `aki-does-not-end-at-discharge.html`, `personal-medical-journal-health-history.html`. Create an entry for `ckd-children-young-adults.html` (it has none) that includes this guide.
- Run `generate_sitemap.py` and `generate_latest_guides.py` (the pipeline does).

---

## 16. Print

Buttons: Print patient guide · Print clinician guide · Print both · Print planner summary · Print blank planner. Implement with a `data-print` attribute on `<body>` toggled before `window.print()` and print-only CSS in block 2. Hide nav, hero vignette, floating controls, symptom widget, and empty tool shells; open all `<details>`; print all study groups with source line; keep table headers with rows. Planner print shows the scope line, "reported" labels, and blank clinician-plan lines. Footer shows canonical URL and the evidence date; print date is separate. Test on A4 and Letter.

---

## 17. Localization

Patient-mode strings need EN/TL/CEB/KAP siblings in order, or the section blanks in that language. Keep untranslated: SGA, FGR, AKI, CKD, NICU, creatinine, cystatin C, unit symbols, reference numbers. Planner labels, errors, prompts, and print labels live in a `STRINGS` map in `assets/born-small-planner.js` keyed by language; no sentence assembled from fragments. The planner reads the active language from the existing `setLang` state.

Translation is a publish blocker. If drafts are prepared by Claude, mark them in the PR-less commit message as "draft translations, pending native review" and keep the guide off the index until reviewed, or ship patient mode with the house fallback pattern the site already uses. Do not present machine drafts as reviewed.

Key glosses: SGA → TL "maliit para sa edad ng pagbubuntis"; nephron → keep "nephron" with the gloss "maliliit na pansala ng bato"; "growth restriction" → TL "pagkabansot ng paglaki sa sinapupunan". All drafts need native review.

---

## 18. Build and verification

### Pipeline (from `/setup-guide`, in order)

```bash
python3 patch_master_css.py --guide born-small-kidneys-for-life.html
python3 patch_font_link.py --guide born-small-kidneys-for-life.html
python3 patch_hero_fetchpriority.py --guide born-small-kidneys-for-life.html
python3 patch_hero_fullwidth.py --guide born-small-kidneys-for-life.html
python3 patch_hero_maxwidth.py --guide born-small-kidneys-for-life.html
python3 patch_image_lightbox.py --guide born-small-kidneys-for-life.html
python3 patch_symptom_widget.py --guide born-small-kidneys-for-life.html
python3 patch_mode_cls.py --guide born-small-kidneys-for-life.html
python3 patch_mode_restore.py --guide born-small-kidneys-for-life.html     # dual-mode
python3 patch_signature_position.py --guide born-small-kidneys-for-life.html
python3 patch_last_reviewed.py --guide born-small-kidneys-for-life.html
python3 patch_published_time.py --guide born-small-kidneys-for-life.html
python3 patch_reading_time.py --guide born-small-kidneys-for-life.html
python3 patch_references_accordion.py --guide born-small-kidneys-for-life.html --overrides refs.json
python3 audit_apa_references.py --guide born-small-kidneys-for-life.html   # must be N/N
python3 audit_acronym_expansion.py --guide born-small-kidneys-for-life.html  # must be N/N
python3 patch_hero_meta.py --guide born-small-kidneys-for-life.html
python3 validate_hero_grid.py
python3 generate_sitemap.py
python3 generate_latest_guides.py
node tests/born-small-planner.cjs
node scripts-qa/qa_render.js /tmp/qa-born-small guides/born-small-kidneys-for-life.html
```

### `tests/born-small-planner.cjs` must cover

| Case | Expected |
|---|---|
| All unknown | base + record prompts; no "normal," "low risk," or tier text |
| 2.5 kg / 2.499 kg | 2,500 g not below LBW; 2,499 g below |
| 1.5 kg / 1.499 kg | 1,500 g not below VLBW; 1,499 g triggers `Q-vlbw` |
| 36 w 6 d / 37 w 0 d | preterm boundary correct |
| 33 w, days blank, SGA yes | `Q-preterm-growth` fires; days stay unspecified |
| 34 w 0 d, SGA yes | `Q-preterm-growth` does not fire; `Q-growth` does |
| days = 7, fractional weeks, 0 or negative weight, `2abc` | error, no summary |
| lb/oz, ounces = 16 | correct grams; 16 oz rejected |
| dialysis yes, AKI no | both kept; `Q-inconsistent` |
| cardiac yes | `Q-cardiac` and `Q-congenital` |
| adolescent + preterm | `Q-growth-years` |
| recollection source | "reported" label in summary and plain text |
| edit after generate | stale summary invalidated |
| static table vs JSON | identical values; differences equal `expected` |
| no output contains `%` tied to the user, or the words "your risk" | pass |

### Manual checks

Keyboard-only use, screen-reader error announcements, focus visible, no traps; light and `html[data-theme="dark"]` contrast ≥4.5:1 (planner chips, white-on-teal buttons use `#0e4a50` in dark); 320/375/768/1024/1440 px; 200% zoom and 400% reflow; reduced motion; no-JS (full article, static study table, references, blank planner); network panel shows no request while typing, generating, copying, or clearing; print variants on A4 and Letter.

### Definition of done

Manuscript integrated with §4 corrections; all 4.7 items confirmed or removed; patient mode translated and reviewed (or held per §17); both audits N/N; planner tests pass; images generated and wired with v2.0 figcaptions, or the guide reads completely without them; glossary present; index, `dual` Set, related links, sitemap, and Latest strip updated; no invented review metadata. Commit directly to `main` per CLAUDE.md once the author approves; deployment is a push to `main`, so do not push until the content review is done.
