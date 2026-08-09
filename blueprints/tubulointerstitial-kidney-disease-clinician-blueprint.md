# Beyond the Glomerulus — Build Blueprint (v2, repo-accurate + evidence-verified)

## Claude Code editorial + implementation handoff

**Series title:** Beyond the Glomerulus: A Philippine Clinician's Guide to Tubulointerstitial Kidney Disease
**Platform:** renalcarematters.com (repo `williamriveromd.github.io`, static site, Cloudflare Pages)
**Audience:** Clinicians only — internists, GPs, hospitalists, EM, nephrologists + trainees, renal pathologists, ID, oncology, rheumatology, urology, transplant teams
**Content level:** Clinician-only, layered generalist-essentials → nephrology deep dive
**Translation:** None (English-only clinician series → **single-mode**, see §B)
**Evidence reviewed through:** August 2026
**Primary source:** Cornell, L. D. (2026). Tubulointerstitial diseases: An updated framework for diverse and emerging entities. *Kidney International*. Advance online publication. https://doi.org/10.1016/j.kint.2026.02.042
**Status:** Build specification + editorial handoff. NOT a clinical practice guideline.

> **How this v2 differs from the uploaded draft.** Two things were wrong-for-this-repo in the original and are fixed here:
> 1. **Architecture.** The draft assumed a React / MDX / YAML-frontmatter component app. This repo is **standalone inline-HTML guides** (~2,000–4,500 lines each) committed straight to `main`, styled by a master-CSS patch script, with a fixed page-tail and a battery of patch/audit scripts. §B and §J rewrite the whole build layer to match.
> 2. **Evidence.** Every citation in the draft was re-checked (7-agent verification workflow). Real corrections are baked in (Cornell pagination, KDIGO-AKI-is-a-draft, MGRS is 2019 not 2018, nedosiran is PH1-only, ICI incidence is a range). New 2019–2026 evidence is added (AIN biomarkers, MGRS 2025/2026, VEXAS renal, FDA inebilizumab). See §D + §E. **Every citation still needs a final line-by-line PubMed/DOI proofread — see the ⚠ flags.**

---

## A. Executive decision (unchanged thesis, confirmed)

There is enough material for a major guide, but the source is too broad and pathology-dense for one page. Build a **clinician-only, five-page series**: one hub + four parts.

**Unifying thesis:**
> Tubulointerstitial nephritis is a *pattern* of kidney injury — not a final etiologic diagnosis, and not automatically a drug reaction.

**One memorable clinical sequence (repeat it on every page):**
> Recognize the compartment → define the phenotype → search all eight cause categories → biopsy when it changes management → treat the cause, not the label.

Do **not** title the project "Acute Interstitial Nephritis" — that excludes chronic TIN, ATI, toxic/crystal nephropathies, reflux/obstruction, inherited disease, monoclonal processes, and mimics.

**Why a Philippine edition** (localization changes probabilities, not biology): pretest probabilities, exposure history, diagnostic sequencing, infection safeguards, resource-tiered testing, biopsy logistics, referral pathways, access caveats. Frame as **"a Philippine practice framework informed by international evidence,"** never a Philippine guideline — there are no local biopsy-registry data to claim a national TIN-cause distribution.

### The five pages (all slugs verified free on disk — no collision)

| # | Page | Reserved slug (`-clinician` convention) | Body class |
|---|---|---|---|
| Hub | Beyond the Glomerulus | `tubulointerstitial-kidney-disease-clinician.html` | `physician-mode single-mode` |
| Part 1 | When the Tubules Are the Problem | `recognizing-tubulointerstitial-kidney-disease-clinician.html` | `physician-mode single-mode` |
| Part 2 | What Is Injuring the Tubules? | `tubulointerstitial-disease-causes-clinician.html` | `physician-mode single-mode` |
| Part 3 | From Pattern to Cause | `tubulointerstitial-nephritis-workup-biopsy-clinician.html` | `physician-mode single-mode` |
| Part 4 | Emerging Tubulointerstitial Diseases | `emerging-tubulointerstitial-diseases-clinician.html` | `physician-mode single-mode` |

Out-of-scope spin-offs the slug audit surfaced (**do not build in this series**, note as future work): a general-AKI hub (only `acute-kidney-injury-on-ckd.html` exists), a standalone ANCA-vasculitis guide (only `calc-anca-renal-risk` exists), and an obstructive-uropathy / post-renal-AKI guide (none exists).

---

## B. Repo architecture — how these guides are ACTUALLY built (read first)

This section overrides the uploaded draft's §13 (React components) and §22 (build steps) entirely.

### B.1 One self-contained HTML file per page
- Each guide is a single inline-HTML document: **all CSS in `<style>`, all JS in `<script>`, no external stylesheet, no build step.** Commit to `main` → Cloudflare Pages deploys in 30–60s.
- **Clone a sibling clinician guide's scaffold and replace content.** There is nothing to `import`. Canonical single-mode clinician exemplars: `ai-in-nephrology-practice.html` (the reference for APA references), `unlocking-urine-electrolytes-clinician.html`, `crrt-continuous-renal-replacement-therapy.html`, `neonatal-acute-kidney-injury-clinician.html`, `highly-sensitized-kidney-transplant-candidates-clinician.html`.

### B.2 Clinician-only = single-mode (NOT the dual-mode audience toggle)
Because this series is English-only clinician content, use **single-mode**, not the patient/clinician tab system:
- `<body class="physician-mode single-mode">` — `physician-mode` selects the periwinkle clinician palette; `single-mode` makes the lone circular-vignette hero bleed like a patient hero.
- **NO** `audience-tabs`, **NO** `mode-patient` content, **NO** four-language `data-lang` spans, **NO** `header-lang` lang pills.
- Hero may use **either** the circular vignette (`figure.hero-figure` + `.hero-vignette`) **or** the clinician Evidence-Snapshot aside (`aside.hero-cards.mode-physician`). For this series, use the **Evidence-Snapshot card** on Parts 1–4 (clinical metrics read better) and the **circular vignette** on the Hub.
- **Skip `patch_mode_restore.py`** (single-mode has no mode to restore) and **skip `patch_clinician_lang_lock.py`** (no lang pills).

### B.3 The two-`<style>`-block rule (load-bearing — get it wrong and the page renders unstyled)
- `patch_master_css.py` overwrites **only the FIRST `<style>` block** with its `MASTER_CSS` string. Design tokens live there: `--navy #1f3864`, `--teal #1a6b72`, `--text #1e2a38`, `--bg #f9fafb`, plus `--text-mid/-muted/-faint` and semantic `--red/-amber/-green/-purple (+ -soft)`.
- **Any bespoke component CSS you add (evidence badges, custom cards, dark-mode contrast remaps) MUST go in a SECOND `<style>` block** after the first, or the next master-CSS run strips it.
- **Prefer house classes over inventing new ones:** `.alert.alert-{teal|red|amber|green|purple}`, `.algo-card`/`.algo-row`, `.tier-badge.tier-{1..4}`, `.ov-stat` (`.v`+`.l`), `.qa-item`/`.qa-q`/`.qa-a`, `.nav-strip`, `.section`.
- **WCAG AA in BOTH light and dark mode** (`html[data-theme="dark"]`): ≥4.5:1 normal, ≥3:1 large, walked through the real ancestor-background chain. Guide-specific dark remaps go in the second `<style>` block.

### B.4 Canonical page-tail order (everything OUTSIDE `<main>`, exact order)
```
</main>
  → [optional <div class="calc-cards-wrap"> …calc link cards…]
  → <!-- GLOSSARY-START --> <details class="glossary-acc"> …two <dl>: Abbreviations + Terms… </details> <!-- GLOSSARY-END -->
  → <!-- REFERENCES-ACC-START --> <details class="ref-acc"> …APA-7 <ol>… </details>   ← the ONLY rendered references location
  → <!-- DR CARD --> <div class="dr-card-wrap">
  → <div class="related-guides">
  → <footer class="guide-footer">      ← NO references line here (duplication bug)
  → inline <script> … then deferred asset scripts before the LAST </body>
```
Nothing may intervene between glossary → references → dr-card → related-guides → footer. `patch_signature_position.py` enforces the dr-card→related-guides→footer segment.

### B.5 Evidence badges — reuse, don't invent
The draft's `EvidenceStrengthBadge` maps to the repo's **`.tier-badge.tier-1..4`** classes (already styled) and the clinician hero **Evidence-Snapshot** card (`.ov-stat` with `.v` value ≤ ~8 chars pinned to a `104px 1fr` grid, center-aligned). Use `.tier-badge` inline in prose for the High/Moderate/Low/Very-low/Practice-safeguard scale (§D.1). Only add a new class in the second `<style>` block if genuinely unavoidable.

### B.6 Head / meta / structured data (renalcarematters.com only)
- Unique `<title>` (`Topic – W Rivero, MD`), `description`, `keywords`.
- `canonical` + all `og:*` + `twitter:*` on `https://renalcarematters.com/guides/<slug>.html`.
- `article:published_time` (+08:00 Manila) stamped by `patch_published_time.py` at merge.
- JSON-LD: `MedicalWebPage` + `MedicalAudience` (clinician) + `BreadcrumbList`; hub also `CollectionPage`. Named reviewers, `datePublished`/`dateModified`, visible author credentials.
- **Purge every `williamriveromd.com`** (retired, 301'd). Only legitimate occurrences: repo path `williamriveromd.github.io`, the `@williamriveromd` Twitter handle, dev local paths. Run the pre-push grep guardrail from CLAUDE.md.

### B.7 Glossary + figures + acronyms (hard requirements)
- **Glossary & abbreviations accordion (rule 12):** every guide carries `<details class="glossary-acc">` with two `<dl>` (Abbreviations = every acronym used; Terms = every specialised word). Single-mode/clinician-only, so English-only content (no `data-lang` spans).
- **Figures (rule 11):** every inline `<figure>` needs `<figcaption><p class="fig-desc">plain-language description</p>` + `<dl class="fig-abbrevs">` whenever the image contains an acronym; `assets/image-lightbox.js` reads them.
- **Acronym expansion (rule 13):** expand every acronym on FIRST body use (either order). `audit_acronym_expansion.py` hard-fails otherwise.

---

## C. Editorial goals, non-goals, safeguards (from the draft — still binding)

### C.1 A generalist finishes the series able to
1. Explain filter (glomerulus) vs recovery system (tubule/interstitium).
2. Distinguish AIN vs ATI vs chronic TIN.
3. Recognize tubular dysfunction even with bland sediment / modest proteinuria.
4. Understand why fever/rash/eosinophilia/urine-eosinophils cannot rule AIN in or out.
5. Build a medication/supplement/infection/occupational/obstructive exposure timeline.
6. Use the eight etiologic categories as overlapping, not mutually exclusive.
7. Order a focused first-line workup, avoid indiscriminate serology.
8. Know when infection, obstruction, glomerular disease, or malignancy is the more urgent competitor.
9. Identify when referral/biopsy changes management.
10. Avoid reflex glucocorticoids before infection and competitors are addressed.

### C.2 A nephrologist additionally can
Connect biopsy pattern → etiologic/attributive diagnosis; brief renal pathology before tissue processing; recognize IgG4-TIN, ICI-TIN, VEXAS, anti-brush-border disease, ADTKD, monoclonal lesions, crystal disease, infiltrative mimics; state the evidence limits around biomarkers, biopsy, steroids, and disease-specific therapy.

### C.3 Non-goals (the series must NOT)
Present a numeric AIN probability score · imply negative urine eosinophils exclude AIN · treat any single histologic feature as pathognomonic · infer drug causality from temporal association alone · equate all infection-associated AKI with TIN · equate sterile pyuria with GU-TB · label agricultural CKD endemic in PH without data · recommend universal serologic panels · give a universal steroid regimen as if high-certainty · recommend stopping anti-TB/ART/immunotherapy/chemo without the owning team · imply a negative gene panel excludes inherited TIN · position itself as a substitute for biopsy, pathology, microbiology, or specialist judgment.

---

## D. Evidence architecture (updated)

### D.1 On-page evidence badges (map to `.tier-badge`)
| Badge | Meaning |
|---|---|
| **High** | RCT or strong guideline-supported |
| **Moderate** | Consistent cohort, consensus, validated clinical evidence |
| **Low** | Retrospective cohort, biopsy series, indirect evidence |
| **Very low / emerging** | Case series, rare-disease descriptions, preclinical/early molecular |
| **Practice safeguard** | Risk-management principle not needing an RCT |

### D.2 Required uncertainty statements (unchanged + updated)
- Foreign cause distributions (Japan/NA/Europe) are **not** Philippine prevalence.
- Biopsy series are shaped by referral/biopsy-selection bias.
- Histology narrows but rarely completes the etiologic diagnosis.
- The 2025 AIN-treatment systematic review suggests possible steroid benefit but is **low-certainty** (23 heterogeneous studies, meta-analysis of only 3).
- **The KDIGO 2026 AKI/AKD guideline is a PUBLIC-REVIEW DRAFT as of Aug 2026 (posted March 2026, comment period extended to May 11 2026) — cite as a draft, never as a finalized recommendation. Update on final publication.**

### D.3 ⚠ Global verification caveat (do not skip)
Every citation in §E was verified via **web-search snippets only** — PubMed/Crossref/Europe PMC/publisher sites were egress-blocked (403) for all research agents. **Before publishing, run a line-by-line PubMed/DOI proofread of every DOI, volume/issue/page, and especially every full author list.** `audit_apa_references.py` will hard-fail on placeholder `[to be transcribed]` bylines, so complete the author lists first. Never fabricate an author, DOI, or number.

---

## E. Verified evidence table (34 sources) — the citation spine for `refs.json`

Legend: ✅ verified · ✳ new (not in draft) · ✎ corrected · ⚠ = must resolve before publish. APA-7 shown; `<em>` marks journal + volume for the accordion.

### E.1 Core AIN / TIN framework
| # | Source (APA-7) | Badge | Note / ⚠ flag |
|---|---|---|---|
| 1 | ✎ Cornell, L. D. (2026). Tubulointerstitial diseases: An updated framework for diverse and emerging entities. *Kidney International*. Advance online publication. https://doi.org/10.1016/j.kint.2026.02.042 | Low | Sole author, title, journal, 2026, DOI confirmed. ⚠ **Draft's `110:318-336` NOT confirmable** (snippets said `109:821-824`, also unconfirmed) — cite as **advance online publication** until an issue is verified. |
| 2 | ✅ Moledina, D. G., & Perazella, M. A. (2021). The challenges of acute interstitial nephritis: Time to standardize. *Kidney360*, *2*(6), 1051–1055. | Low | Editorial. ⚠ numeric DOI (`10.34067/KID.xxxx`) unconfirmed — use LWW article URL, not a guessed DOI. |
| 3 | ✅ Muriithi, A. K., Nasr, S. H., & Leung, N. (2013). Utility of urine eosinophils in the diagnosis of acute interstitial nephritis. *Clinical Journal of the American Society of Nephrology*, *8*(11), 1857–1862. https://doi.org/10.2215/CJN.01330213 | Moderate | PMID 24052222. At 1% cutoff: sens 30.8%, spec 68.2%, PPV 15.6%, NPV 83.7% → supports "abandon urine eosinophils." |
| 4 | ✅ Muriithi, A. K., Leung, N., Valeri, A. M., … (2014). Biopsy-proven acute interstitial nephritis, 1993–2011: A case series. *American Journal of Kidney Diseases*, *64*(4), 558–566. https://doi.org/10.1053/j.ajkd.2014.04.027 | Moderate | PMID 24927897, n=133. **Confirms the ~10%** fever+rash+eosinophilia triad; causes: antibiotics 49%, PPIs 14%, NSAIDs 11%. ⚠ transcribe full author list from PubMed. |
| 5 | ✅ [authors ⚠]. (2025). A systematic review of treatment for acute interstitial nephritis. *Kidney International Reports*. Advance online publication. https://pubmed.ncbi.nlm.nih.gov/40814598/ | Low | 23 studies (3 RCT, 4 case series, 16 retrospective), 1983–2024, 1205 pts (952 treated). Steroid benefit **low-certainty**. ⚠ authors/vol/issue/pages unconfirmed. |
| 6 | ✎ KDIGO AKI Work Group. (2026). KDIGO 2026 clinical practice guideline for the management of AKI and AKD [Public review draft]. https://kdigo.org/guidelines/acute-kidney-injury/ | Practice safeguard | **DRAFT, not final** (Aug 2026). Combined AKI+AKD framework, functional + structural-biomarker criteria. |
| 7 | ✳ Moledina, D. G., … & Perazella, M. A. (2019). Urine TNF-α and IL-9 for clinical diagnosis of acute interstitial nephritis. *JCI Insight*, *4*(10), e127456. https://doi.org/10.1172/jci.insight.127456 | Moderate | n=218, 15% AIN. TNF-α aOR 10.9, IL-9 aOR 7.5; AUC 0.62→0.84. ⚠ full authors. |
| 8 | ✳ Moledina, D. G., … (2023). Identification and validation of urinary CXCL9 as a biomarker for diagnosis of acute interstitial nephritis. *The Journal of Clinical Investigation*, *133*(13), e168950. https://doi.org/10.1172/JCI168950 | Moderate | PMID 37395276. **Strongest single validated AIN biomarker to date.** ⚠ full authors. |

### E.2 ICI / onco-nephrology
| # | Source (APA-7) | Badge | Note / ⚠ flag |
|---|---|---|---|
| 9 | ✅ Herrmann, S. M., Abudayyeh, A., Gupta, S., … Kitchlu, A. (2025). Diagnosis and management of immune checkpoint inhibitor–associated nephrotoxicity: A position statement from the American Society of Onco-nephrology. *Kidney International*, *107*(1), 21–32. https://doi.org/10.1016/j.kint.2024.09.017 | Practice safeguard | **FINAL** society statement, PMID 39455026. ⚠ verify full 16-author byline. |
| 10 | ✅ Gupta, S., Short, S. A. P., Sise, M. E., … (2021). Acute kidney injury in patients treated with immune checkpoint inhibitors. *Journal for ImmunoTherapy of Cancer*, *9*(10), e003467. https://doi.org/10.1136/jitc-2021-003467 | Moderate | n=429, 30 sites. AIN in **~83% of the 151 biopsied** (keep "of biopsied" explicit); recurrence after rechallenge 20/121 = 16.5%. ⚠ full authors + exact 82.7%. |
| 11 | ✅ Ho, C.-W., Kang, N.-W., Yeh, T.-H., … (2025). Immune checkpoint inhibitors–associated acute kidney injury: A systematic review and meta-analysis of incidence, kidney recovery, and recurrent risk. *Cancer Immunology, Immunotherapy*, *74*, Article 324. https://doi.org/10.1007/s00262-025-04147-4 | Moderate | 16 studies, 10,726 pts. Steroids ↑ recovery; recurrence 18.0%; **steroids at rechallenge did NOT reduce recurrence**. ⚠ issue/authors. |
| 12 | ✅ Gupta, S., … (2022). Diagnosis and management of immune checkpoint inhibitor-associated acute kidney injury. *Nature Reviews Nephrology*, *18*, 794–805. https://doi.org/10.1038/s41581-022-00630-8 | Moderate | Source for incidence — present as a **definition-dependent range ≈1.4–5.7%**, not a fixed 2–5%. ⚠ full authors. |

### E.3 Emerging immune entities
| # | Source (APA-7) | Badge | Note / ⚠ flag |
|---|---|---|---|
| 13 | ✅ Stone, J. H., … Katz, G. (2025). Inebilizumab for treatment of IgG4-related disease. *New England Journal of Medicine*, *392*(12), 1168–1177. https://doi.org/10.1056/NEJMoa2409712 | **High** | MITIGATE, phase 3 RCT. **All numbers verified:** n=135 (68/67); flare 7/68 (10%) vs 40/67 (60%); HR 0.13 (95% CI 0.06–0.28). Disease-wide, **not** a kidney-specific endpoint. ⚠ transcribe full byline. |
| 14 | ✅ U.S. FDA / Amgen. (2025, April 3). Uplizna (inebilizumab-cdon) approved for IgG4-related disease. | Practice safeguard | First & only FDA-approved IgG4-RD therapy, based on MITIGATE. Do NOT conflate with the separate Dec-2025 gMG approval. ⚠ **PH FDA availability = to-verify.** |
| 15 | ✅ Takahashi, N., … (2017). Tubulointerstitial nephritis with IgM-positive plasma cells. *Journal of the American Society of Nephrology*, *28*(12), 3688–3698. https://doi.org/10.1681/ASN.2016101074 | Very low / emerging | Defining Japanese series n=13. Distal RTA 100%, Fanconi 92%, AMA 82%; PBC ~46%, Sjögren ~31%; steroid-responsive. ⚠ full authors. |
| 16 | ✅ Larsen, C. P., Trivin-Avillach, C., … Salant, D. J. (2018). LDL receptor-related protein 2 (megalin) as a target antigen in human kidney anti-brush border antibody disease. *Journal of the American Society of Nephrology*, *29*(2), 644–653. https://doi.org/10.1681/ASN.2017060664 | Low | Antigen-defining. **Update: add cubilin (CUBN) + amnionless (AMN) — three ABBA antigens.** ⚠ verify byline order. |
| 17 | ✅ Beck, D. B., Ferrada, M. A., Sikora, K. A., … Kastner, D. L. (2020). Somatic mutations in UBA1 and severe adult-onset autoinflammatory disease. *New England Journal of Medicine*, *383*(27), 2628–2638. https://doi.org/10.1056/NEJMoa2026834 | Moderate | VEXAS defining paper. **Pair with a renal-specific ref** — Ronsin 2022 (Kidney Int 101(6):1295–1297, VEXAS-TIN; ⚠ note 2022 corrigendum) + the 2025 systematic review of 23 biopsy-confirmed renal cases. ⚠ full byline. |

### E.4 Genetic / monoclonal / metabolic
| # | Source (APA-7) | Badge | Note / ⚠ flag |
|---|---|---|---|
| 18 | ✅ Econimo, L., Schaeffer, C., Zeni, L., Cortinovis, R., Alberici, F., Rampoldi, L., Scolari, F., & Izzi, C. (2022). Autosomal dominant tubulointerstitial kidney disease: An emerging cause of genetic CKD. *Kidney International Reports*, *7*(11), 2332–2344. https://doi.org/10.1016/j.ekir.2022.08.012 | Moderate | PMID 36531871. Six loci (UMOD, MUC1, REN, HNF1B, SEC61A1, DNAJB11). **MUC1 VNTR missed by standard short-read NGS** — needs SNaPshot/VNtyper. Fully verified. |
| 19 | ✅ KDIGO Conference Participants. (2022). Genetics in chronic kidney disease: Conclusions from a KDIGO Controversies Conference. *Kidney International*, *101*(6), 1126–1141. https://doi.org/10.1016/j.kint.2022.03.019 | High | PMID 35460632. ⚠ proofread final DOI/pages. |
| 20 | ✎ Leung, N., Bridoux, F., Batuman, V., … Nasr, S. H. (2019). The evaluation of monoclonal gammopathy of renal significance: A consensus report of the International Kidney and Monoclonal Gammopathy Research Group. *Nature Reviews Nephrology*, *15*(1), 45–59. https://doi.org/10.1038/s41581-018-0077-4 | High | **Cite as 2019, not 2018** (print 15(1):45–59, PMID 30510265). Correction NRN 2019 15(2):121. No longer sole authority — pair with #21/#22. |
| 21 | ✳ Nasr, S. H., Royal, V., Best Rocha, A., … Bridoux, F., & D'Agati, V. D. (2025). RPS/IKMG consensus on pathologic definitions and terminology of monoclonal gammopathy–associated kidney lesions. *Kidney International*, *108*(2), 184–193. https://pubmed.ncbi.nlm.nih.gov/40280412/ | High | PMID 40280412. ⚠ DOI ambiguous (`…2025.04.007` vs `.011`) — use PMID; middle authors reconstructed. |
| 22 | ✳ Sprangers, B., Cohen, C., Gnemmi, V., … Wetzels, J. F. (2026). Executive summary of the European consensus report on the diagnosis and treatment of monoclonal gammopathy of renal significance. *Clinical Kidney Journal*, *19*(6), sfag163. | High | ⚠ DOI `10.1093/ckj/sfag163` inferred from OUP article ID — verify. Companions: NDT 2026 41(3):445; BSH good-practice BJH 2025 (10.1111/bjh.19956). |
| 23 | ✅ Garrelfs, S. F., Frishberg, Y., Hulton, S. A., … Lieske, J. C. (2021). Lumasiran, an RNAi therapeutic for primary hyperoxaluria type 1. *New England Journal of Medicine*, *384*(13), 1216–1226. https://doi.org/10.1056/NEJMoa2021712 | High | ILLUMINATE-A, PMID 33789010. 24-h urinary oxalate −65.4% vs −11.8%. Targets **HAO1/glycolate oxidase**. |
| 24 | ✎ Baum, M. A., Langman, C., Cochat, P., … Russell, K. (2023). PHYOX2: A pivotal randomized study of nedosiran in primary hyperoxaluria type 1 or 2. *Kidney International*, *103*(1), 207–217. https://doi.org/10.1016/j.kint.2022.07.025 | High | PMID 36007597. **Efficacy PH1 only — NO consistent PH2 effect.** Nedosiran (Rivfloza) FDA-approved 29 Sep 2023 **PH1 only**; targets **LDHA**. ⚠ confirm pediatric age cutoff on current FDA label (sources conflict ≥2 vs ≥9 yr). |
| 25 | ✅ Lamarche, J., Nair, R., Peguero, A., & Courville, C. (2011). Vitamin C-induced oxalate nephropathy. *International Journal of Nephrology*, *2011*, 146927. https://doi.org/10.4061/2011/146927 | Low | High-dose vitamin C → oxalate. Case-based. |
| 26 | ✅ Nasr, S. H., D'Agati, V. D., Said, S. M., … Markowitz, G. S. (2008). Oxalate nephropathy complicating Roux-en-Y gastric bypass. *Clinical Journal of the American Society of Nephrology*, *3*(6), 1676–1683. https://doi.org/10.2215/CJN.02940608 | Moderate | PMID 18701613. Enteric hyperoxaluria after RYGB/fat-malabsorption. |

### E.5 Philippine context / infection / transplant
| # | Source (APA-7) | Badge | Note / ⚠ flag |
|---|---|---|---|
| 27 | ✅ Kotton, C. N., Kamar, N., Wojciechowski, D., … (2024). The second international consensus guidelines on the management of BK polyomavirus in kidney transplantation. *Transplantation*, *108*(9), 1834–1866. https://doi.org/10.1097/TP.0000000000004976 | High | **FINAL**, PMID 38605438, PMC11335089. Screen monthly plasma BKPyV-DNAemia to month 9, then q3 mo to 2 yr (3 yr peds). ⚠ full authors. |
| 28 | ✅ Gupta, S. K., Anderson, A. M., Ebrahimi, R., … Flaherty, J. F. (2014). Fanconi syndrome accompanied by renal function decline with tenofovir disoproxil fumarate. *PLOS ONE*, *9*(3), e92717. https://doi.org/10.1371/journal.pone.0092717 | Moderate | PMID 24651857. TDF proximal tubulopathy (phosphate wasting, glucosuria, aminoaciduria); mostly reversible ~2 mo after stopping. Contrast lower-risk TAF. |
| 29 | ✅ Andrade, L., de Francesco Daher, E., & Seguro, A. C. (2008). Leptospiral nephropathy. *Seminars in Nephrology*, *28*(4), 383–394. https://doi.org/10.1016/j.semnephrol.2008.04.008 | Moderate | PMID 18620961. Characteristic **nonoliguric, hypokalemic** AKI (NKCC2/NHE3 downregulation). PH companion: PSN Leptospirosis Renal guideline PDF. Do NOT assert a national incidence without DOH/WHO. |
| 30 | ✅ WHO Philippines. (2025, June 11). UNAIDS, WHO support DOH's call for urgent action as the Philippines faces the fastest-growing HIV surge in the Asia Pacific region. | Moderate | Cite figures **as the agencies' statement** (≈550% rise, 4,400→29,600; ~252,800 PLHIV 2025). Use this exact URL/date. |
| 31 | ✎ FDA Philippines. (2025). FDA verification portal. https://verification.fda.gov.ph/ | Practice safeguard | **Now a single unified portal** (relaunched 2025). Advisories at fda.gov.ph/advisories. ⚠ launch advisory number conflict (2025-0106 vs 2026-0106) — confirm. |
| 32 | ✅ Philippine Society of Nephrology. (n.d.). Find a nephrologist. https://psn.org.ph/patients-corner/find-a-nephrologist/ | Practice safeguard | Use the exact slug — bare `/find-a-nephrologist` 404s. |
| 33 | ✎ NIH, UP Manila. (n.d.). Institute of Human Genetics. https://nih.upm.edu.ph/institute/institute-human-genetics | Practice safeguard | **URL corrected** — draft's `/institute/ihg` does not resolve. Referral home for MUC1/ADTKD testing. |
| 34 | ✎ DOH National Tuberculosis Control Program. (n.d.). About NTP. https://ntp.doh.gov.ph/about-ntp/ | Practice safeguard | Documented strategy is **DOTS** — ⚠ "iDOTS" not confirmed as an official NTP term; reword to DOTS / NTP patient-pathway. |

---

## F. Coverage gaps to close before build (completeness critique)

The evidence agents did **not** cover these TIN entities — decide which belong in the series and research + verify each before writing:
- **TINU syndrome** (tubulointerstitial nephritis with uveitis) — belongs in Part 2 (autoimmune) + Part 4.
- **Sarcoidosis-associated granulomatous TIN** — Part 2/Part 3 (granuloma differential).
- **Aristolochic acid / Chinese-herb nephropathy + Balkan endemic nephropathy** — Part 2 (supplements/toxic) — high relevance to the PH unregulated-herbal theme.
- **Lithium nephropathy** and **calcineurin-inhibitor chronic TIN** — Part 2 (drug/toxic) + Part 4 (transplant).
- **Karyomegalic interstitial nephritis (FAN1)** — Part 4 (genetic).
- **Mesoamerican nephropathy / CKDu (heat-stress TIN)** — Part 2 agricultural/heat module. **Directly relevant to Philippine agricultural workers** but must keep the "biologically plausible, not proven endemic locally" caveat.
- **Comprehensive culprit-drug table** — the case series give top agents (antibiotics/PPIs/NSAIDs) but a fuller current offender list (incl. the ICI class) needs a dedicated verified source.
- **Optional prognosis biomarker:** 2021 urine IL-9/TNF-α steroid-response study (⚠ PMID 33125471) — include only if a prognosis angle is wanted; verify first.

There is **no** Philippine TIN/AIN incidence, drug-attribution, or biopsy-registry data — do not invent any; cite only attributed DOH/PSN/WHO figures.

---

## G. Content specifications (per page)

Preserves the draft's clinical teaching; only the build layer changed. Reading-time targets are computed by `patch_reading_time.py`, not authored.

### G.1 Hub — Beyond the Glomerulus
`CollectionPage`. Modules: hero + clinical thesis · 60-second orientation · simplified nephron map (Image H-1) · why the series exists · three tissue-pattern cards (AIN/ATI/chronic TIN, Image H-3) · eight-cause overview (Image H-4) · start-with-the-patient router · four part cards · download pack · key myths · references + reviewers + version stamp.

**60-second orientation (verbatim copy):**
> The glomerulus begins urine formation by filtering plasma. The tubules then reclaim most filtered water and solute, control acid-base balance, regulate potassium and phosphate, concentrate or dilute urine, and return valuable molecules to the circulation. Injury to this recovery system may present as AKI, progressive CKD, electrolyte wasting, glycosuria, sterile pyuria, modest proteinuria, or a surprisingly bland urine sediment. The biopsy pattern may be inflammatory, predominantly tubular, fibrotic, crystalline, infiltrative, infectious, immune, toxic, or inherited. The real diagnostic task is to identify the cause.

**Router (`.algo-card`):** New AKI / rising creatinine / sterile pyuria / tubular abnormalities → Part 1 · suspected medicine/infection/supplement/occupation/obstruction → Part 2 · persistent unexplained injury / steroid question / possible biopsy → Part 3 · systemic/oncologic/hematologic/transplant/familial clues → Part 4.

### G.2 Part 1 — When the Tubules Are the Problem
Default layer generalist essentials. **Opening composite case** (revisit at each step, never reveal a single culprit):
> A 58-year-old develops rising creatinine after pneumonia treatment. Urine protein is modest, sediment not strongly nephritic, no rash or eosinophilia. Meds: an antibiotic, a newly added PPI, intermittent mefenamic acid, an unlabeled supplement. Ultrasound has not yet excluded obstruction. What is the phenotype, which explanations compete, and what evidence would justify calling this drug-induced AIN?

Sections: **A** filter vs recovery system (glomerulus / proximal / loop / distal / interstitium) · **B** three patterns not one disease (table below) + a 4th "secondary/mimic" caution card · **C** clinical phenotypes (AKI/AKD/CKD; bland sediment; sterile pyuria; WBC casts; modest proteinuria; glycosuria; hypophosphatemia; hypokalemia; NAGMA; hypouricemia; concentrating defect; LMW proteinuria; imaging clues) · **D** six myth cards (no rash / no fever / no eosinophilia / negative urine eosinophils / bland sediment / partial fluid response) with the evidence callout below · **E** major competitors table · **F** first-24-hour actions (10 steps).

| Pattern | Simplified tissue definition | Clinical caution |
|---|---|---|
| **AIN** | Interstitial inflammation + edema, tubular injury/tubulitis, little fibrosis/atrophy | Onset may be quiet; cause not always a drug |
| **ATI** | Tubular epithelial injury, little inflammation | Often ischemic/toxic/septic/pigment/cast/crystal |
| **Chronic TIN** | IFTA with variable inflammation | "Chronic" = tissue damage, not symptom duration |

**Evidence callout (badge Moderate):** In the biopsy-proven series (Muriithi 2014, n=133), the classic fever-rash-eosinophilia triad occurred in only ~10%; urine eosinophils performed poorly vs biopsy (Muriithi 2013). **New (badge Moderate):** modern non-invasive markers — urine CXCL9 (validated, JCI 2023) and urine TNF-α + IL-9 (JCI Insight 2019) — outperform eosinophils, though not yet universally available.

### G.3 Part 2 — What Is Injuring the Tubules? (eight-bucket differential)
Preserve Cornell's eight overlapping categories (interlocking cards, not silos). Each category card uses the **standard 10-part microarchitecture**: mechanistic intuition · typical clues · representative exposures/entities · initial feasible tests · what argues against · when biopsy helps · generalist action · nephrology deep dive · Philippine practice note · evidence badge.

| Category | Representative entities | PH bedside priority |
|---|---|---|
| Drug effect | Antibiotic/PPI/NSAID AIN, vancomycin ATI/casts, lithium, chemo, crystals | Very high |
| Autoimmune / immune-mediated | Sjögren, **TINU**, sarcoidosis, IgG4-RD, anti-brush-border, ANCA | Moderate-high |
| Infection-associated | Pyelonephritis, adenovirus, BK, TB-associated, infection-triggered | High (precedes immunosuppression) |
| Hereditary / genetic | ADTKD, nephronophthisis, Dent, mitochondrial, **karyomegalic (FAN1)**, VEXAS overlap | Selected phenotype |
| Toxic / metabolic | Oxalate, phosphate, urate, bile, heme, light chains, heavy metals, **aristolochic acid**, **heat-stress CKDu** | High when exposure fits |
| Monoclonal protein-associated | Cast nephropathy, LC proximal tubulopathy, MIDD | High-stakes; urgent heme-neph |
| Mimics | Leukemia, lymphoma, myeloma, EMH, severe GN-associated inflammation | Critical when biopsy ≠ story |
| Idiopathic / other | ALECT2, obstruction, reflux, unresolved TIN | Diagnosis of exclusion |

Reusable modules (keep from draft): **"Before calling this idiopathic TIN, ask:"** exposure callout · high-yield medicine table (immune AIN / direct toxicity / crystal-cast / ICI / multifactorial) · **PH infection modules** (TB-or-treatment two-sided differential; leptospirosis multi-mechanism; HIV + tenofovir tubulopathy; transplant graft dysfunction incl. BK) · supplements & unregulated products (photo, FDA verification portal, undeclared NSAID/steroid/heavy-metal/aristolochic-acid, batch shared in household) · agricultural/heat/chemical exposure (framed as a domain, not a local epidemic, with the required caveat).

### G.4 Part 3 — From Pattern to Cause (workup, biopsy, management)
Main 10-step workflow (Image WF-7). **Resource-tiered PH workup** (Core / Expanded / Biopsy-center / Selected-advanced) — the Expanded tier is **phenotype-gated, never a universal order set**. Tubular-phenotype table (glycosuria / phosphate wasting / NAGMA / hypokalemia / concentrating defect / non-albumin proteinuria → localization + confounders; cross-link `unlocking-urine-electrolytes-clinician.html`). Biopsy triggers + **PH biopsy logistics** (confirm LM/IF/EM availability, don't put the whole core in formalin if IF/EM needed, prearrange fresh tissue for micro, brief pathology fully). Clinicopathologic integration (pattern vs etiologic vs attributive diagnosis; histologic-clue → directions table). **Treatment architecture** (universal principles + the glucocorticoid section).

**Glucocorticoid section title (verbatim):**
> Steroids may help selected immune-mediated AIN; the evidence does not support an automatic one-size-fits-all prescription.

Frame steroid benefit as **low-certainty** (2025 systematic review: 23 studies, meta-analysis of 3). Require the visible **Steroid Safety Gate** (8 checks) before empirical therapy; output unresolved issues only, never a treatment directive; never embed a fixed universal dose (any representative regimen goes in a nephrologist-only expandable, ICI-AIN distinguished from conventional AIN, labeled specialist-directed).

### G.5 Part 4 — Emerging Tubulointerstitial Diseases
Badge Advanced/Nephrology. Entity cards (What it is → mechanism → clinical clues → biopsy clues → competing dx → confirmatory workup → treatment evidence → PH access note):
- **ICI-associated TIN** — incidence **≈1.4–5.7% range** (Gupta 2022); AIN dominant in ~83% of biopsied ICI-AKI (Gupta 2021); recovery associated with steroids, recurrence ~18% and **steroids at rechallenge don't reduce it** (Ho 2025); base practice on ASON 2025. Rechallenge = individualized onco-neph decision.
- **IgG4-related TIN** — plasma-cell-rich TIN, storiform fibrosis, ↑IgG4+ plasma cells, TBM deposits, other-organ disease, hypocomplementemia (none in isolation). **MITIGATE**: inebilizumab, phase 3, flare 7/68 vs 40/67, HR 0.13 — **disease-wide, not a kidney endpoint**. FDA approval Apr 3 2025; **PH availability to-verify**.
- **IgM plasma-cell TIN** — newly characterized (Takahashi 2017, n=13); Sjögren/PBC subset; no validated global prevalence/standard therapy.
- **Anti-brush-border antibody disease** — anti-LRP2/megalin **+ cubilin + amnionless**; specialized pathology/serology.
- **VEXAS-associated TIN** — somatic UBA1 (Beck 2020); neutrophil-rich TIN mimicking pyelonephritis; older male, macrocytic anemia/cytopenias, chondritis, skin/marrow clues; renal series (Ronsin 2022 + 2025 review).
- **ADTKD & genetic TIN** — bland-sediment CKD, little albuminuria, family history, early gout, syndromic clues; **MUC1 missed by standard NGS** — order a MUC1-specific assay (refer UP Manila NIH-IHG).
- **Primary hyperoxaluria & treatable metabolic genetics** — lumasiran (PH1, HAO1; ILLUMINATE-A) vs nedosiran (**PH1 only**, LDHA; PHYOX2); PH2 (GRHPR)/PH3 (HOGA1) = unmet need; secondary oxalate (high-dose vitamin C, malabsorption, bariatric).
- **Monoclonal protein-associated lesions** — cast nephropathy, LC proximal tubulopathy (crystalline/noncrystalline), MIDD, crystal-storing histiocytosis; IKMG/MGRS safeguard (a serum clone alone does not name the kidney lesion — needs integrated biopsy + heme workup); cite Leung 2019 **+ RPS/IKMG 2025 + EU 2026**.
- **Mimics** — leukemia, lymphoma, myeloma, EMH, GN-secondary inflammation; if tissue and clinical dx disagree, re-ask whether the infiltrate is reactive, malignant, hematopoietic, infectious, or from another compartment.

---

## H. Audience layering, tools, downloads (repo-mapped)

### H.1 Layering
Two layers **within single-mode** (no dual-mode tabs): render **generalist essentials** in the default DOM (search/print/accessibility) and collapse **nephrology deep dive** into `<details>` accordions — but **never hide safety-critical material** behind a toggle. Standard reading order per section: clinical problem → intuition → physiology → evidence → PH bedside application → generalist actions → nephrology refinement → referral/biopsy gate → tools/downloads.

### H.2 Interactive tools (build as standalone `calc-*.html` where a tool is a calculator; otherwise as in-guide JS in the second `<style>`/`<script>`)
1. **Medication & Exposure Timeline Builder** — chronological, never outputs a probability or names a culprit; always shows "temporal association supports investigation but does not prove drug causality."
2. **Eight-Bucket Differential Builder** — checkbox phenotype/exposure → relevant categories **without ranking**; no numeric score, no green/red diagnosis.
3. **Tubular Dysfunction Pattern Finder** — inputs (K, HCO₃, glucose, urine glucose, PO₄, Mg, urate, urine pH, protein pattern, polyuria, diuretics, SGLT2i, CKD stage, specimen timing) → possible proximal/distal/concentrating/mixed phenotype + confounders; mandatory label "Pattern recognition only — does not identify the cause or diagnose AIN."
4. **Biopsy Conversation Checklist** → A4 clinician-to-pathologist handoff.
5. **Steroid Safety Gate** — unresolved-issues output only, never a directive.
6. **Calculators:** do NOT build a TIN diagnostic calculator in phase 1. **Link existing** `.calc-card`s (verified present): `calc-aki-staging`, `calc-akin-aki`, `calc-rifle-aki`, `calc-fena-feurea`, `calc-urine-anion-gap`, `calc-egfr-ckd-epi`, `calc-which-kidney-test`, `calc-proteinuria-uacr`, `calc-anca-renal-risk`. Optional later: **Tubular Handling Workbench** (paired-specimen validation, unit tests for FE/TmP-GFR; warns on non-steady-state AKI/CKD/diuretics; never infers etiology). All calculators are English-only (`patch_calc_english_only.py`) and get `add_calc_nav_pill.py` + `patch_calc_handoff.py`.

### H.3 Download pack (WeasyPrint pipeline — NOT a component)
Build each handout as `downloads/<name>.html` linking `_companion-style.css` (classes only, no inline `<style>`), then `python3 build_companion_pdfs.py`. One `.page` div = one A4 page. Surface via the guide's `.dl-fab`. Set: (1) recognition & referral card · (2) eight-bucket differential — PH edition · (3) 60-second PH exposure history · (4) medication/exposure timeline worksheet · (5) initial workup by resource level · (6) biopsy request & handoff · (7) infection-safety questions before empirical steroids · (8) tubular abnormality interpretation table · (9) pathology glossary · (10) teaching slide "the classical AIN triad is uncommon" · (11) series PDF bundle with QR codes to versioned pages.

---

## I. Internal linking (all targets VERIFIED on disk)

**Link out to (do NOT recreate):** `how-to-properly-assess-kidney-function.html` · `unlocking-urine-electrolytes-clinician.html` (natural clinician sibling) · `acute-kidney-injury-on-ckd.html` · `dengue-aki-kidney.html` · `neonatal-acute-kidney-injury-clinician.html` · `nsaid-kidney-injury.html` · `pain-management-ckd.html` · `herbal-nephropathy.html` · `natural-supplements-kidney.html` · `medicines-and-your-kidneys.html` · `hivan-hiv-kidney-disease.html` · `managing-kidney-stones.html` · `prostate-enlargement.html` · `kidney-transplant.html` · `transplant-allograft-failure.html` · `highly-sensitized-kidney-transplant-candidates-clinician.html` · `glomerulonephritis.html` · `lupus-nephritis.html` · `diabetes-kidneys.html` · `diabetes-kidney-disease-not-always-diabetic.html`.

**Back-link the new series INTO** the `related_guides.json` arrays of: `nsaid-kidney-injury`, `hivan-hiv-kidney-disease`, `acute-kidney-injury-on-ckd`, `unlocking-urine-electrolytes-clinician`, `medicines-and-your-kidneys` (+ `herbal-nephropathy`, `glomerulonephritis`, `lupus-nephritis` for Parts 2/4).

---

## J. Claude Code implementation runbook (do this, in order, per guide)

### J.1 Scaffold
1. Copy a single-mode clinician exemplar (e.g. `guides/unlocking-urine-electrolytes-clinician.html`) to the new slug. Set `<body class="physician-mode single-mode">`.
2. Replace `<head>` meta (title/description/keywords/canonical/og/twitter/JSON-LD) — all URLs on `renalcarematters.com`. Add `MedicalWebPage` + `MedicalAudience` + `BreadcrumbList` (+ `CollectionPage` on the hub) with named reviewers.
3. Author content into `<main>`: `.nav-strip` pills → `.section` blocks → `.alert.alert-*` callouts → `.algo-card` routers/workflows → `.tier-badge` evidence chips → `.qa-item` FAQs. Deep-dive content in `<details>`; safety content stays in default DOM.
4. Author the **glossary** accordion (every acronym + every specialised term) and every `<figure>`'s `<figcaption>` (`.fig-desc` + `.fig-abbrevs`).
5. Put ALL bespoke CSS in a **second `<style>` block**; add dark-mode contrast remaps there.

### J.2 refs.json + citations
6. Write `refs-<slug>.json` (`{ "<file>.html": ["APA-7 citation", …] }`) from §E — **only** the sources that guide actually cites. **Complete every ⚠ author list from PubMed first.**
7. `python3 patch_references_accordion.py --guide <file>.html --overrides refs-<slug>.json`

### J.3 Patch + audit pipeline (exact order; single-mode → skip mode-restore + lang-lock)
```
python3 patch_master_css.py           --guide <file>.html
python3 patch_font_link.py            --guide <file>.html
python3 patch_hero_fetchpriority.py   --guide <file>.html
python3 patch_hero_fullwidth.py       --guide <file>.html
python3 patch_hero_maxwidth.py        --guide <file>.html
python3 patch_image_lightbox.py       --guide <file>.html
python3 patch_symptom_widget.py       --guide <file>.html
python3 patch_mode_cls.py             --guide <file>.html
#   SKIP patch_mode_restore.py  (single-mode)
#   SKIP patch_clinician_lang_lock.py (no lang pills)
python3 patch_signature_position.py   --guide <file>.html
python3 patch_last_reviewed.py        --guide <file>.html
python3 patch_published_time.py       --guide <file>.html
python3 patch_reading_time.py         --guide <file>.html
python3 patch_hero_meta.py            --guide <file>.html
python3 audit_apa_references.py       --guide <file>.html     # HARD-FAIL GATE → must be N/N
python3 audit_acronym_expansion.py    --guide <file>.html     # HARD-FAIL GATE → must be N/N
python3 validate_hero_grid.py                                  # hero-grid direct-children check
```

### J.4 Wire into the site (manual + generators)
8. Add a `.guide-tile` to `guides/index.html` under `data-section="nephrology"` (Hub + Parts 1–3) or `data-section="advanced"` (Part 4) with a subject-appropriate `data-icon` from the `ICONS` map (kidney/drop/flask/etc.; add a new key if none fits).
9. Add each new file to `related_guides.json` (its own array + the sibling arrays in §I).
10. `python3 generate_latest_guides.py` and `python3 generate_sitemap.py` (the SessionStart hook also runs these + `patch_published_time.py`).
11. Pre-push guardrail: `git diff --name-only <base> | xargs grep -n "williamriveromd\.com"` — legitimate hits only in the repo path, `@williamriveromd`, dev paths.

### J.5 Clinical QA gates (must all pass)
No urine-eosinophil rule-out · no universal AIN score · no automatic drug causality · no automatic steroid recommendation · no immunosuppression before the infection safety gate · no PH prevalence claims from foreign registries · no unilateral ART/TB/chemo/ICI changes · every advanced entity states an evidence badge + access caveat · every citation APA-7 and PubMed-proofread (no `[to be transcribed]`).

### J.6 Technical acceptance
No broken internal links · valid structured data · no console errors · deterministic tool outputs · downloads render on A4 + grayscale · mobile (320px) + desktop QA · WCAG AA light + dark · references open to DOI/PubMed/official source · `dateModified` + evidence-review date visible.

---

## K. Phased release (mapped to real files)

- **Phase 1 (MVP):** Hub + Part 1 + Part 2; downloads 1–3; Timeline Builder + Eight-Bucket Builder.
- **Phase 2 (diagnostic depth):** Part 3; resource-tier selector; Biopsy Checklist; Steroid Safety Gate; pathology glossary; bidirectional links.
- **Phase 3 (precision layer):** Part 4; ICI module; IgG4 / monoclonal / genetic deep dives; optional Tubular Handling Workbench (after formula/unit validation).
- **Phase 4 (local refinement):** de-identified analytics on used exposure domains, unavailable tests, stalled referrals, printed downloads, no-result searches — never presented as epidemiology.

## L. Review requirements
Practicing nephrologist (native-kidney biopsy) · renal pathologist · ID/TB clinician (PH pathways) · onco-nephrology reviewer (Part 4 ICI) · transplant nephrologist (transplant subsection) · clinical geneticist/counselor (inherited module). Assign scope explicitly.

## M. Image system
Visual house style, the required image list, alt-text specs, and the **production-ready ChatGPT Image Generator prompts** live in the companion file **`image-prompts-tubulointerstitial-kidney-disease-clinician.md`** (generated via the `williamriveromd-*` graphic skills). House constraints: Inter only; navy `#0f1e2e`, clinical teal `#1a6b72`, renal green `#1f7a4d`, amber `#b8860b` (caution only), clinical red `#b91c1c` (danger only), light backgrounds only; `© renalcarematters.com` bottom-right ~65% opacity; **never fabricate diagnostic photomicrographs** — licensed pathology images with attribution or clearly-labeled schematics only. og:image is wired per guide once images are received.

## N. Final editorial test
Success = a local clinician finishes thinking: *"A rising creatinine with modest urine findings is not diagnostically empty. Define whether the tubules are responding appropriately, reconstruct all exposures, exclude infection and obstruction, keep the full etiologic framework open, and biopsy when it will change what I do."*
Failure = *"AIN equals drug allergy, urine eosinophils diagnose it, and steroids are the default."*

---

### Appendix — process provenance
Evidence verified and repo conventions mapped by a 7-agent supervised workflow (5 evidence-domain agents + 1 repo-conventions agent + 1 supervising synthesis agent), Aug 2026. **All citations were web-search-verified only (publisher/PubMed egress was blocked); a final line-by-line PubMed/DOI proofread — especially of every full author byline and of the ⚠-flagged items — is mandatory before publication.** Never fabricate a citation, author, DOI, or number.
