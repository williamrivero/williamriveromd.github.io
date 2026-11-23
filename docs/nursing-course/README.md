# Nephrology Nursing & Hemodialysis — build notes

A 12-module self-study series for registered nurses, with a course hub and an educator page.

## Pages (all under `guides/`, canonical URLs are extensionless)

| Page | File |
|---|---|
| Course hub | `nephrology-nursing.html` |
| Educator and preceptor resource | `nephrology-nursing-educator.html` |
| Modules 1–12 | `nephrology-nursing-NN-<slug>.html` |

## Where things live

| What | Path |
|---|---|
| Module content (edit here) | `tools/nursing/content/m01.py` … `m12.py` |
| Course metadata, abbreviations, references | `tools/nursing/content/common.py` |
| Plain link titles for readings and calculators | `tools/nursing/content/display.py` |
| Generator | `generate_nursing_course.py` |
| Site wiring (index tile, related guides, Latest strip) | `tools/nursing/wire_course.py` |
| Image brief builder | `tools/nursing/build_image_brief.py` |
| Quiz and progress script | `assets/nursing-course.js` |
| PubMed metadata and generated reference lists | `data/nursing-course/` |
| Browser test | `tests/nursing-course.cjs` |
| Source register, crosswalk, quiz key register, image brief and manifest, verification notes | `docs/nursing-course/` |

## Rebuild

```bash
python3 generate_nursing_course.py --check          # content validation only
python3 generate_nursing_course.py --patch          # write pages, run the /setup-guide patch pipeline on each
python3 tools/nursing/wire_course.py                # idempotent: index tile, related_guides.json, Latest-strip skip
python3 tools/nursing/build_image_brief.py          # regenerate the GPT brief from the module image blocks
python3 generate_sitemap.py && python3 generate_search_index.py && python3 patch_audience_chips.py && python3 generate_latest_guides.py
node tests/nursing-course.cjs [screenshot-dir]      # needs playwright-core + Google Chrome
```

The generator picks a Python 3.10+ interpreter for the patch pipeline on its own (macOS `python3` is 3.9 and `patch_hero_fetchpriority.py` needs 3.10+).

Do not hand-edit the generated pages. The generator carries over each page's `article:published_time`; on go-live day run `python3 generate_nursing_course.py --patch --reset-published` so the stamp is the real publish moment, then `generate_latest_guides.py`.

## Rules the generator enforces

- Exactly one keyed answer and four options per question; unknown reference keys, missing readings, and calculators without a display title stop the build.
- Every abbreviation in `common.ABBR` that appears on a page is listed in that page's glossary. If one is used without ever being introduced, its first use in running text is expanded automatically and logged; headings and link text are never rewritten.
- Citations are numbered in order of first appearance and rendered through `patch_references_accordion.py --overrides data/nursing-course/refs-overrides.json`.
- A module shows a hero picture only when `images/<page-slug>-vignette-hero.png` exists.

## Adding or changing a reference

PubMed sources: add `key: PMID` to `PUBMED_REFS`, fetch the record into `data/nursing-course/refs_pubmed_raw.json` (E-utilities `esummary`), and add the full journal name to `JOURNALS` if new. Other sources: add a hand-built APA 7 string to `MANUAL_REFS`. Then update `SOURCE-REGISTER.md`.
