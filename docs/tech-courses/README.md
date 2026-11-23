# Technical-workforce courses — build notes

Three study series built on the Nephrology Nursing course format:

| Series | Hub | Modules | Content source |
|---|---|---|---|
| Hemodialysis Technician | `academy/hemodialysis-technician.html` | 12 | Markdown in `tools/techcourses/hd_technician/src/NN/` (copied from `~/Documents/HD Technicians`) plus the `enrich` blocks in `hd_technician/course.py` |
| Water Treatment System Technician | `academy/water-treatment-technician.html` | 6 | `tools/techcourses/water_treatment/m01.py` … `m06.py` |
| Hemodialysis Center Biomedical Technician | `academy/dialysis-biomedical-technician.html` | 6 | `tools/techcourses/biomed/m01.py` … `m06.py` |

Each series also has a trainer page (`<hub>-trainer.html`) that gathers every skills checklist for printing.

## Where things live

| What | Path |
|---|---|
| Generator | `generate_tech_courses.py` (imports chrome and CSS from `generate_nursing_course.py`) |
| Shared abbreviations, references, reading titles | `tools/techcourses/shared.py` |
| Illustration library (existing site images, alt text, captions) | `tools/techcourses/figs.py` |
| Image sizes for files that cannot be read locally | `tools/techcourses/img_dims.json` |
| Asset preparation (heroes, card thumbnails, quiz script) | `tools/techcourses/prep_assets.py` |
| Site wiring (index tiles, related guides, Latest strip) | `tools/techcourses/wire_courses.py` |
| Quiz script | `assets/tech-course.js` (built from `assets/nursing-course.js`) |
| Reference lists for the accordion | `data/tech-courses/refs-overrides.json` |
| Quiz key register, image manifest | `docs/tech-courses/` |

## Rebuild

```bash
python3 tools/techcourses/prep_assets.py "$HOME/Documents/HD Technicians"   # only when sources or images change
python3 generate_tech_courses.py --check
python3 generate_tech_courses.py --patch
python3 tools/academy/wire_academy.py
python3 generate_sitemap.py && python3 generate_search_index.py && python3 patch_audience_chips.py && python3 generate_latest_guides.py
```

Needs Python 3.10+ with Pillow. Do not hand-edit the generated pages.

## Content macros (in `enrich` blocks and native modules)

`{{fig:key}}` or `{{fig:key|caption}}` an illustration from `figs.py` · `{{flow:Title|Step::text|…}}` numbered flow strip ·
`{{cards:Title|Head::text|…}}` card grid · `{{plain:…}}` "In plain words" · `{{key:…}}` "Remember" · `{{stop:…}}` "Stop and report" ·
`{{formula:…}}` formula box · `[[refkey]]` a reference from `shared.REFS`.

## Before publication

- Clinical and technical sign-off by Dr. Rivero on all pages; the Water Treatment and Biomedical series are newly written and have not been reviewed.
  `QUIZ-KEY-REGISTER.md` lists every keyed answer for review.
- Numeric limits (ISO 23500 water and dialysis fluid limits, carbon contact time, IEC 62353 earth resistance) should be checked against the
  standard editions the facility follows.
- Hero pictures: the Hemodialysis Technician heroes are cut from the Opener images. The Biomedical series has no hero pictures yet;
  `image-manifest.json` carries a brief for each (`hero_brief`) for GPT production. Drop finished files in `images/<page-slug>-vignette-hero.png` and re-run.
- The Hemodialysis Technician teaching diagrams are the flat diagrams from the source folder. Replace
  `images/<slug>-teaching-diagram.png` with illustrated versions when produced; no code change is needed.
- Nothing has been committed or deployed.

## Renal Care Academy (added 2026-11-23)

All staff-training courses, including the Nephrology Nursing course, now live in their own section: `academy/`
(URLs `/academy/` and `/academy/<slug>`). They are no longer listed in the Guides index, the guide search index,
`related_guides.json`, or the Latest strip; the Guides index carries one signpost tile to `/academy/`.

- Landing page: `academy/index.html` (content in `tools/techcourses/shared.py`, `ACADEMY`; planned tracks are listed there).
- The generators still write and patch in `guides/` (the patch pipeline only works there), then
  `tools/academy/publish_academy.py` moves the pages to `academy/` and rewrites their links. Both generators call it.
- `tools/academy/wire_academy.py` replaces the two older wiring scripts, which are retired.
- `patch_nav_academy.py` adds ACADEMY to the standard header navigation.
- To add a track (for example Physician on Duty or Renal Dietitian): add its slug prefix to `PREFIXES` in
  `publish_academy.py`, add a package under `tools/techcourses/`, and list it in `PACKAGES` in `generate_tech_courses.py`.
