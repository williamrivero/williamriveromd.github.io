# Setup New Guide

Run all post-creation patch scripts for a new guide file in `guides/`.

**Usage:** `/setup-guide <filename>`
**Example:** `/setup-guide diabetes-and-ckd.html`

---

The user will pass a guide filename (with or without the `.html` extension) as `$ARGUMENTS`.

Steps:

1. Normalize the filename — ensure it ends in `.html`. If the user omitted the extension, append it.

2. Confirm the file exists at `guides/<filename>`. If it does not exist, stop and tell the user to create it first.

3. Run each script below in order, passing `--guide <filename>`. Report the output of each step briefly. If a script fails, stop and show the error.

```bash
python3 patch_master_css.py --guide <filename>
python3 patch_hero_fetchpriority.py --guide <filename>
python3 patch_hero_fullwidth.py --guide <filename>
python3 patch_hero_maxwidth.py --guide <filename>
python3 patch_image_lightbox.py --guide <filename>
python3 patch_mode_cls.py --guide <filename>
python3 patch_signature_position.py --guide <filename>
python3 patch_last_reviewed.py --guide <filename>
python3 generate_sitemap.py
```

4. After all scripts succeed, stage the new guide and any modified files, then commit and push to `main`:

```bash
git add guides/<filename> sitemap.xml
git commit -m "Add <filename> with full structure setup"
git push -u origin main
```

5. Remind the user of two things to check manually in the guide HTML:
   - Each inline `<figure>` image should have a `<figcaption>` with `<p class="fig-desc">` (plain description) and optionally `<dl class="fig-abbrevs">` for any abbreviations used in the image — the lightbox will display both.
   - The guide's script tag `<script src="../assets/image-lightbox.js" defer></script>` should be present near `</body>` (patch_image_lightbox.py adds it if missing).
