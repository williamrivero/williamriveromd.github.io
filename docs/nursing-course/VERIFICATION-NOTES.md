# Verification notes — Nephrology Nursing & Hemodialysis

Build date: 2026-11-23 (Asia/Manila). Status: **built and verified locally; not committed, not pushed, not deployed.** Clinical sign-off is pending.

## What was built

- Course hub, educator and preceptor page, and 12 module pages in `guides/` (14 pages, about 29,000 words of original prose, 12 fictional nursing cases, 36 scored single-best-answer items with a rationale for each of the 144 options, 12 reflective prompts, 12 supervised-practice checklists).
- A generator, content files, quiz script, wiring script, image-brief builder, and browser test (see `README.md`).
- Source register, curriculum crosswalk, quiz key register, GPT image brief, and image manifest in this folder.
- Site wiring: one course tile on the Guides index (Dialysis → Dialysis Unit Operations & Safety, tagged for the Dialysis Staff / HD Tech filter and labeled "Registered Nurses"); 14 entries in `related_guides.json`; 14 URLs in `sitemap.xml`; search index rebuilt; the hub appears in the Latest guides strip.

## What was checked, and the result

| Check | Result |
|---|---|
| `generate_nursing_course.py --check` (reference keys, reading and calculator targets, one key and four options per item) | Pass |
| House patch pipeline from `/setup-guide`, run per page | All steps ran on all 14 pages (with Python 3.13; see note 3 under "Other observations") |
| `audit_apa_references.py` per page | 14 of 14 compliant |
| `audit_acronym_expansion.py` per page | 14 of 14 compliant |
| `patch_canonical_clean_urls.py --check` | Already extensionless |
| `tests/nursing-course.cjs` in headless Chrome | 915 checks, 0 failed |
| Old-domain guardrail (`williamriveromd.com` in changed files) | No new occurrences |

The browser test covers, on every page: loads without script errors; no dead local links, anchors, or assets; exactly one `h1`; no sideways scroll at 375 px. On every module: three questions, four labeled options each, exactly one key; rationales hidden until checked; a prompt and focus move when a question is unanswered; selection by Space and arrow keys; correct score text; a rationale shown under all 12 options; verdicts stated in words as well as color; focus moved to the live-region result; inputs locked after checking; retry restores a clean form; nothing stored unless the reader opts in; opted-in progress stored and erased on untick; **no network request made by the quiz**; previous and next links resolve. On the hub: default order; Hemodialysis path reorders to 1, 6, 7, 8, 9, 2, 3, 4, 5, 10, 11, 12 from the keyboard; saved progress shown and cleared.

Screenshots of the hub, Module 6 (light and dark, with the quiz checked), Module 9 on a phone, and the educator page were reviewed by eye. They are in `tmp/nursing-shots/` (untracked).

Not tested: a real screen reader (structure is fieldset, legend, labeled radios, `aria-describedby` feedback, `role="status"` result); printed output of the preceptor checklist on paper; Safari and Firefox.

## Decisions that differ from the handoff, and why

1. **URLs are flat.** `/guides/nephrology-nursing` and `/guides/nephrology-nursing-NN-<slug>`, not a `/guides/nephrology-nursing/` folder. Every guide on the site is a flat file and the patch scripts, sitemap generator, and search index all assume that.
2. **All 12 modules are complete.** No "forthcoming" labels were needed. The handoff's publication sequence can still be followed by choosing which pages to commit.
3. **Hero images follow the site's circular-vignette convention**: square 2048 × 2048 masters named `<page-slug>-vignette-hero.png`, not 16:9 files named `renal-nursing-NN-…`. The short names survive as work IDs in the brief. Share cards (1200 × 630) are derived by the site's own script.
4. **No new nurse filter.** Role filters on the index are fixed buttons; one course does not justify another. The tile uses the existing Dialysis Staff / HD Tech filter and says "Registered Nurses" on its face.
5. **Only the hub has an index tile.** Thirteen more tiles would crowd the section, and thirteen more cards would flood the Latest guides strip, so `generate_latest_guides.py` now skips files beginning `nephrology-nursing-` (one-line change). Module titles and keywords are folded into the hub tile's search text so the index search still finds them.
6. **Pages are English-only, single-audience clinician pages.** That is the existing template for staff-facing guides, and it shows no language chips.
7. **Module content lives in Python files, not JSON**, so long HTML passages need no escaping.
8. **The series makes no accreditation or CPD claim**, and says so on the hub and the educator page. The 480 hours are labeled as a proposal.

## Open dependencies before publication

**Clinical review (required).** Dr. Rivero's sign-off on all pages, and subject review of the high-risk content. Flags are listed per module in `QUIZ-KEY-REGISTER.md`. In priority order:

1. Module 9 emergency first actions (hypotension, dislodgement, hemolysis, air, dialyzer reaction, cardiac arrest): medical director and senior hemodialysis nurse; match to the unit protocol.
2. Module 8 water limits and release criteria: technician or biomedical engineer; confirm the adopted standard and edition.
3. Module 7 access, asepsis, and hepatitis B isolation: vascular access nurse, infection control.
4. Module 4 hyperkalemia escalation: nephrologist.
5. Module 11 pediatric, pregnancy, and transplant content: the relevant specialist nurse or physician.
6. Module 3 medicines (binders, iron, erythropoiesis-stimulating agents): pharmacist. Dialysis-specific anemia thresholds were deliberately left to the prescriber.
7. Module 10 peritonitis and contamination response: peritoneal dialysis nurse.

**Source checks still owed** (detail in `SOURCE-REGISTER.md`):

- Sources marked B were verified bibliographically in PubMed; the recommendation or section behind each statement was not re-read. A reviewer should confirm the specific numbers: KDIGO 2024 referral thresholds; KDOQI 2015 targets; the KDIGO hyperkalemia severity grid; ISPD 2022 diagnostic criteria; DAPA-CKD and EMPA-KIDNEY event rates.
- Republic Act 9173, Section 28: the scope summary in Module 12 should be compared with the statute text.
- DOH AO 2012-0001: the statement that free-standing units must have emergency transport and a receiving-hospital arrangement was written from the order's known structure; confirm the clause. AO 2013-0003 testing frequencies were not read in full; the schedule quoted is from the PSN 2024 guidance.
- ISO 23500-3:2024 is paywalled; limits were taken from the catalog summary and agree with the site's water-treatment guide.
- The DOH assessment tool and the PRC provider record named in the handoff were not opened.

**Things that may change and should be rechecked at publication:**

- KDIGO 2026 AKI/AKD guideline: public-review draft only as of the build date. Module 4 teaches the 2012 criteria and says so.
- ANNA Core Curriculum: 7th edition current; 8th announced.
- NNCC examination blueprint: under revision in 2026; the crosswalk uses domain names without weights.
- Philippine nursing law: replacement bills pending in the 20th Congress.
- Newer DOH or HFSRB issuances on dialysis facilities: none found, but the search was not exhaustive.
- PhilHealth benefit packages: intentionally not quantified.

**Assets.** No module hero images exist yet; pages render without a hero picture until the files arrive. Share previews fall back to `images/hero-cat-dialysis.webp`. `GPT-IMAGE-BRIEF.md` and `image-manifest.json` are ready to hand over. Two instructional diagrams (Module 6 transport and circuit; Module 8 water train) are specified as reviewed vector or site-native builds, not free image generation.

**Publish stamps.** Each page carries a placeholder `article:published_time` of 23 Nov 2026 so the Latest strip and hero byline render. On go-live day run `python3 generate_nursing_course.py --patch --reset-published`, then `generate_latest_guides.py`.

**Provider-led program.** Separate from the public series. It needs a training provider to confirm prerequisites, supervision, placement, sign-off, and any recognition sought.

## Calculators

Twenty-six existing site calculators are linked from the modules (for example, kidney function estimate and kidney failure risk in Modules 1 and 2; nutrition screening and dietary load estimators in Module 3; acute kidney injury staging in Module 4; dialysis adequacy, ultrafiltration-rate check, and weight-gain calculators in Modules 6 and 9; access infection rate and catheter exposure in Module 7; peritoneal dialysis adequacy in Module 10; run chart, improvement worksheets, and quality scorecard in Module 12). No new calculator was built. Two candidates for a later build, if wanted: (1) a process-audit compliance calculator that returns the percentage with a confidence interval for small samples, to pair with the Module 12 capstone; (2) a one-screen fluid-goal worksheet that adds treatment inputs line by line, to pair with Module 6. Both overlap partly with existing tools, so neither was added without a decision.

## Other observations (existing site, not changed)

1. `guides/fluid-management-dialysis.html` has the wrong `<title>`: it reads "Hurt Without Harm: A Guide to Safe Pain Relief in Kidney Disease," which belongs to `pain-management-ckd.html`.
2. Re-running `generate_latest_guides.py` also changed one unrelated thumbnail path in the strip (`inno-ckd-biomarker-timeline.png` → `.jpg`) and updated guide counts from 207 to 208 on the homepage and Guides index. The count change is expected; the thumbnail change reflects files already on disk.
3. macOS `python3` is 3.9, and `patch_hero_fetchpriority.py` uses 3.10+ syntax, so it fails under the default interpreter. The course generator selects `/opt/homebrew/bin/python3.13` for the pipeline.
4. The floating symptom-checker button is installed on the course pages by the standard pipeline, as on other clinician guides. It can be excluded for this course if it seems out of place for a nurse audience.
5. `graphify update .` was not run.
