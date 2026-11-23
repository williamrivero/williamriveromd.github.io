
## 4. Build instructions for Claude Code

1. **Split and write modules.** For each expanded track, create `tools/techcourses/<package>/m01.py … m12.py` from the module briefs above. Reuse the existing six module files: move sections to their new module as the Origin column states, then write the new sections. Keep the module schema, macros, and tuple formats already used. Update `MODULES` in each `course.py` (ids, slugs, titles, subs, `card_img`, `hero_brief`).
2. **Sources.** Keep limits and requirements tied to `shared.REFS` (ISO 23500 series, IEC 60601-1, IEC 60601-2-16, IEC 62353, WHO maintenance guidance, DOH AO 2012-0001, PSN 2024). Add references only after verifying them. State a number only when a cited source or the facility's own procedure supports it; otherwise say "per the manual" or "per unit procedure".
3. **Figures.** Add each produced image to `tools/techcourses/figs.py` (file, alt from the manifest, caption) and place it with `{{fig:key}}` in the section named in the manifest. Until an image exists, keep the current HTML flow strips and card grids in place so no page loses a figure.
4. **Slugs changed by the split.** Six Water Treatment and six Biomedical page addresses change. Nothing is live yet, so no redirects are needed; if the pages have been deployed by then, add `_redirects` entries from the old slugs.
5. **Rebuild.** `python3 tools/techcourses/build_image_brief.py`, `python3 tools/techcourses/prep_assets.py`, `python3 generate_tech_courses.py --patch`, `python3 tools/academy/wire_academy.py`, then the sitemap generator.
6. **Verify.** `generate_tech_courses.py --check`; every academy link resolves; figure numbers run in order; quiz draws and scores; trainer pages list all checklists; mobile and print layouts hold.

## 5. Review before publication

- Dr. Rivero: all lesson content, every keyed answer (`docs/tech-courses/QUIZ-KEY-REGISTER.md`), and every image.
- Chief technician or water system supplier: Water Treatment Modules 2 to 7 and 9 to 11 against the installed systems.
- Manufacturer-trained biomedical engineer: Biomedical Modules 3 to 7 and 9 to 11 against the service manuals in use.
- Facility electrical engineer: Biomedical Module 11 (outlets, grounding, backup power).

## 6. Files

| File | Purpose |
|---|---|
| `tools/techcourses/image_plan_hd.py`, `image_plan_water.py`, `image_plan_biomed.py` | Source of this blueprint and of every prompt |
| `docs/tech-courses/GPT-IMAGE-PROMPTS.md` | Copy-ready Constitution v1.0 prompts, one per image, with a production list |
| `docs/tech-courses/image-prompts-manifest.json` | Filenames, canvas, placement, alt text, reviewers |
