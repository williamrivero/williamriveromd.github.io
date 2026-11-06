# Blueprint: Fever and Kidney Injury in the Tropics — Scrub Typhus, Malaria, and the Philippine Febrile-AKI Hub

**File:** `guides/tropical-infection-aki.html`
**Canonical:** `https://renalcarematters.com/guides/tropical-infection-aki.html`
**Status:** New guide. Implementation handoff for Claude Code (`/setup-guide tropical-infection-aki.html`), to be opened in its own thread.
**Shape:** Dual-mode (Patients & Families / Clinicians). Patient mode EN/TL/CEB/KAP; clinician mode English-only.
**Index section:** `philippines` (amber-orange `#c2410c`) or `nephrology` — match where `leptospirosis-nephropathy.html` and `dengue-aki-kidney.html` sit in `guides/index.html`.
**Template to copy:** `guides/leptospirosis-nephropathy.html` (closest sibling: Philippine infection-AKI guide, dual-mode). Glossary: `guides/complement-mediated-kidney-disease.html`.
**Origin:** Journal review of 6 November 2026, item NG-4 (priority 4).
**Evidence check:** Skim level (6 Nov 2026). ✔ = read in the paper; **[verify]** = confirm in full text or official source. Build all citations from PubMed (APA 7).
**Review status:** Draft blueprint. Not medically reviewed.

---

## 0. Why this guide, and how it fits

The site already has strong single-infection guides for leptospirosis (`leptospirosis-nephropathy.html` + `calc-leptospirosis-aki-risk.html`), dengue (`dengue-aki-kidney.html` + `calc-dengue-aki-risk.html`), and hantavirus (`hantavirus-ckd.html` + `calc-hfrs-severity.html`). What is missing:

1. **Scrub typhus** — mentioned in one guide only, yet endemic in the "tsutsugamushi triangle," which includes Southeast Asia, and easy to miss because the eschar is small and tests are scarce.
2. **Malaria** — present in parts of the Philippines (historically Palawan and some Mindanao provinces) **[verify current DOH endemicity and elimination status]**; severe falciparum malaria causes AKI.
3. **A hub** — "fever plus kidney injury" is how patients actually present, before anyone knows the organism. A page that walks through the differential (lepto, dengue, scrub typhus, malaria, hantavirus, sepsis, drug-induced) and points to each deep guide is the most useful frame for Filipino clinicians.

**Decision:** one guide with two deep sections (scrub typhus, malaria) and a hub layer (comparison table, first-24-hour approach, links). Do not duplicate lepto/dengue content; summarize in one row each and link out.

**Out of scope:** antimalarial or antibiotic dosing tables beyond what WHO/DOH guidance states and renal adjustment notes; travel medicine; tuberculosis (has its own guide).

---

## 1. Source papers

| # | File (Mac, `~/Downloads/Journals/`) | Type | Contribution | Key data |
|---|---|---|---|---|
| S1 | `Kidney International_20260620/Unique-aspects-of-acute-kidney-injury-associated-w.pdf` | Mini review, Shankar, Karam, Aoun Bahous, Davidson, Kumar, Sharma, Vareesangthip, Rosner, Wijewickrama, KI 2026;110:61–69, doi 10.1016/j.kint.2026.02.025 | Spine for all four infections and resource-limited care | ✔ Leptospirosis ≈1.03 million cases and 58,900 deaths/year; pooled AKI 49.2% (95% CI 38.2–60.2), oliguria 31.5%, KRT 14.4% **[verify which disease these pooled figures belong to — they appear in the leptospirosis section]**. ✔ Scrub typhus: *Orientia tsutsugamushi*, larval chigger (trombiculid mite) bite; tsutsugamushi triangle incl. Southeast Asia; untreated case fatality 30–70%; AKI in 18–53%; KRT in 5–10%; mechanisms: prerenal (fever, vomiting, capillary leak), acute tubulointerstitial nephritis, rhabdomyolysis, immune vasculitis, tubular injury; early doxycycline essential; azithromycin when doxycycline resistance **[verify pregnancy/children wording]**. ✔ Malaria: 5 *Plasmodium* species; 263 million cases in 2023 (94% Africa); AKI pathogenesis Fig 3 — hemolysis, hyperviscosity, hyperbilirubinemia, intravascular coagulation, rhabdomyolysis, RAAS activation, ATN; IV artesunate first-line for severe malaria (WHO). ✔ Dengue: AKI mechanisms incl. rhabdomyolysis, HUS, secondary HLH (Fig 2). ✔ Peritoneal dialysis is effective for infection-AKI and useful where hemodialysis is unavailable. **[verify]** malaria AKI incidence/mortality figures, dialysis indications, and the paper's Table 2 (risk factors per infection). |

**Housekeeping found during planning:** this same DOI (10.1016/j.kint.2026.02.025) is currently cited in `guides/hivan-hiv-kidney-disease.html`. Check whether that citation is correct (the paper is about tropical infection AKI, not HIVAN); fix it in this thread if wrong.

**External anchors to verify:** WHO Guidelines for malaria (latest version; severe malaria criteria including AKI definition, artesunate); Philippine DOH malaria program and scrub typhus surveillance data (PIDSR) **[verify]**; KDIGO AKI guideline (staging); any Philippine scrub typhus case series on PubMed (search "scrub typhus Philippines"); doxycycline renal dosing (no adjustment) from the label.

---

## 2. Head, meta, structured data

```
<title>Fever and Kidney Injury in the Tropics: Scrub Typhus, Malaria, Leptospirosis and Dengue · W Rivero, MD</title>
description: Fever with kidney injury in the Philippines: how leptospirosis, dengue, scrub typhus and malaria harm the kidneys, the clues that tell them apart, what to do in the first 24 hours, and when dialysis is needed.
keywords: scrub typhus kidney Philippines, malaria acute kidney injury, fever kidney failure, tropical infection AKI, leptospirosis dengue kidney, eschar doxycycline
canonical: https://renalcarematters.com/guides/tropical-infection-aki.html
og image: images/tropical-infection-aki-og.webp (1200×630)
JSON-LD: Article + MedicalWebPage; about: Acute Kidney Injury; Scrub Typhus; Malaria; Leptospirosis; Dengue. audience Patient + MedicalAudience.
localStorage keys: wgmr-tropaki-mode / wgmr-tropaki-lang
```

---

## 3. Page structure

House chrome per CLAUDE.md. Hero: H1 "Fever and Kidney Injury in the Tropics"; subtitle "Scrub typhus, malaria, leptospirosis and dengue: telling them apart early"; tag "Infection · Acute kidney injury".

**One-minute answer (patient, 4 languages)**
1. Several tropical infections can injure the kidneys within days: leptospirosis, dengue, scrub typhus and malaria.
2. Warning signs are the same: fever plus much less urine, dark urine, yellow eyes, muscle pain, swelling or breathlessness.
3. Tell the doctor where you have been: flood water or farm work, grassy or bushy areas (mite bites), forests or known malaria areas, mosquito exposure.
4. Most of these are treatable, and kidney function often recovers when treatment starts early.

**Urgent box (red, both modes):** fever with very little or no urine for 12 hours, confusion, breathlessness, bleeding, yellow eyes with dark urine, or a black scab-like spot on the skin with high fever. Go to a hospital today.

---

## 4. Section map

### Patient mode (EN/TL/CEB/KAP)

| Anchor | Pill | Content |
|---|---|---|
| `#fever-kidneys` | Fever & kidneys | Why fever infections hurt the kidneys: dehydration, low blood pressure, muscle breakdown, direct infection/inflammation (one plain diagram) |
| `#four-infections` | The four | Comparison cards: how you catch it · key clue · test · treatment · kidney risk (lepto, dengue, scrub typhus, malaria); each links to the deep guide where one exists |
| `#scrub-typhus` | Scrub typhus | Mite bites in grassy/bushy areas; the eschar (painless black scab, often in skin folds — check armpits, groin, waistline); fever, headache, rash; doxycycline works fast; AKI in about 1 in 5 to 1 in 2 |
| `#malaria` | Malaria | Mosquito-borne; where in the Philippines **[verify]**; fever cycles; severe malaria can cause dark urine and kidney failure; treated in hospital with IV artesunate |
| `#prevention` | Prevention | Boots and gloves in flood water (lepto), mosquito control (dengue, malaria), long clothes and repellent in grassland (scrub typhus); do not self-medicate with NSAIDs or herbal remedies |
| `#recovery` | Recovery | Kidney recovery is common; follow-up creatinine after discharge (link `aki-does-not-end-at-discharge.html`) |
| `#faq` | FAQ | Is it contagious? Will I need dialysis forever? Can I give blood after malaria? |

### Clinician mode

| Anchor | Pill | Content |
|---|---|---|
| `#md-approach` | First 24 h | Algorithm: febrile AKI → exposure history, eschar search, platelet/bilirubin/CK, malaria smear/RDT, dengue NS1/IgM, lepto MAT/PCR/RDT, scrub typhus IgM/PCR → empirical doxycycline when lepto or scrub typhus is plausible and dengue/malaria tests are pending **[verify that this mirrors S1 and local guidance]** → fluids guided by volume status → KRT criteria |
| `#md-comparison` | Comparison | S1-based table: agent · vector · kidney lesion (ATN, ATIN, rhabdo, HUS/TMA, glomerulonephritis) · electrolyte signature (lepto hypokalemia and non-oliguria) · test · treatment · KRT need |
| `#md-scrub-typhus` | Scrub typhus | S1 numbers; mechanisms; doxycycline vs azithromycin; severe disease (myocarditis, ARDS, meningoencephalitis); local data **[verify]** |
| `#md-malaria` | Malaria | Severe malaria AKI definition (WHO), mechanisms (S1 Fig 3), blackwater fever, artesunate, quinine-era hypoglycemia note, renal dosing, exchange transfusion only per WHO **[verify]** |
| `#md-krt` | Dialysis | Timing, modality in resource-limited settings, PD for infection-AKI (S1), anticoagulation with thrombocytopenia (dengue, lepto) |
| `#md-climate` | Climate | Climate change, floods, and expansion of vectors (S1 introduction); link `typhoon-disaster-preparedness-dialysis.html`, `el-nino-heat-dialysis.html` |
| `#md-evidence` | Evidence | Claim · source · evidence type |

**Evidence Snapshot (`.v` ≤ 8 chars)**

| `.v` | `.l` |
|---|---|
| 18–53% | Scrub typhus: patients developing AKI |
| 5–10% | Scrub typhus: kidney replacement therapy needed |
| 30–70% | Scrub typhus: untreated case fatality |
| 49.2% | Leptospirosis: pooled AKI incidence **[verify attribution]** |
| IV AS | Severe malaria first-line: IV artesunate (WHO) |

---

## 5. Figures

1. Hero vignette (patient-only): Filipino farmer with fever being examined; rice field/grassland in background.
2. Eschar teaching figure (simple-figure skill, illustrated, not a clinical photo): where to look (axilla, groin, waistband, behind ears).
3. Comparison infographic (infographic skill): four infections × vector × key clue × kidney lesion.
4. Algorithm (algorithm-generator skill): febrile AKI first-24-hour approach.

---

## 6. Calculators and related guides

Link: `calc-leptospirosis-aki-risk.html`, `calc-dengue-aki-risk.html`, `calc-hfrs-severity.html`, `calc-aki-staging.html`, `calc-mcmahon-rhabdo.html`, `calc-fluid-overload.html`, `calc-renal-abx-dosing.html`. Possible future calculator: a scrub typhus severity score, only if a validated one exists **[verify]**.

Related: `leptospirosis-nephropathy.html`, `dengue-aki-kidney.html`, `hantavirus-ckd.html`, `acute-kidney-injury-on-ckd.html`, `aki-does-not-end-at-discharge.html`, `typhoon-disaster-preparedness-dialysis.html`, `viral-infections-vaccinations-ckd.html`. Add this guide to `related_guides.json` for the lepto, dengue and hantavirus guides, and add a one-line hub link in each of them.

## 7. Glossary seed

AKI, ARDS, ATIN, ATN, CK, CI, DOH, HLH, HUS, IgM, KRT, MAT, NS1, NSAID, PCR, PD, PIDSR, RAAS, RDT, TMA, WHO. Terms: eschar, chigger, zoonosis, blackwater fever, rhabdomyolysis, capillary leak, tsutsugamushi triangle.

## 8. Build checklist

1. Read S1 in full; resolve every **[verify]**; confirm the pooled-figure attribution.
2. Verify Philippine epidemiology (DOH malaria endemic provinces, scrub typhus reports) and WHO malaria criteria.
3. Check and, if needed, fix the S1 DOI citation in `hivan-hiv-kidney-disease.html`.
4. Build from the leptospirosis template; four languages in patient mode; dark-mode check.
5. `/setup-guide tropical-infection-aki.html`; APA + acronym audits; `validate_hero_grid.py`; `generate_latest_guides.py`; `generate_sitemap.py`; update `related_guides.json` and add hub links in sibling guides.
6. Independent verification pass before pushing.
