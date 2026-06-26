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
python3 patch_master_css.py --guide <filename>     # themed master CSS (pastel hero, Inter/Manrope/Nunito Sans)
python3 patch_font_link.py --guide <filename>       # Google Fonts <link> → Inter/Manrope/Nunito Sans (drops Lora/DM Sans)
python3 patch_hero_fetchpriority.py --guide <filename>
python3 patch_hero_fullwidth.py --guide <filename>
python3 patch_hero_maxwidth.py --guide <filename>
python3 patch_image_lightbox.py --guide <filename>
python3 patch_mode_cls.py --guide <filename>
python3 patch_signature_position.py --guide <filename>
python3 patch_last_reviewed.py --guide <filename>          # "Last Reviewed" badge + article:modified_time + JSON-LD
python3 patch_published_time.py --guide <filename>         # article:published_time stamp (date + time, +08:00) — when made/published
python3 patch_reading_time.py --guide <filename>           # "Reading time" estimate in the hero
python3 patch_references_accordion.py --guide <filename>   # accordion References section before the signature block
python3 generate_sitemap.py
python3 generate_latest_guides.py                          # refresh the "Latest guides" strip on guides/index.html
```

> **Theme note:** The site uses the pastel hero theme with Inter (headlines/titles/numbers),
> Manrope (body), and Nunito Sans (hero subtitle). Both `patch_master_css.py` and
> `patch_font_link.py` must run so the guide gets the themed CSS **and** loads the matching
> fonts. The optional `patch_hero_theme.py` (circular vignette + clinician cards) is **opt-in**
> — only run it on guides that have a real hero photo and dual-mode clinical sections (e.g.
> `epilepsy-seizures-ckd.html`); most guides should keep the plain themed hero.

> **Every new guide must (policy):**
> 1. **Be date- and time-stamped of when it was made and published.** `patch_published_time.py`
>    writes an immutable `<meta property="article:published_time">` (Manila time). This is what
>    orders the **Latest guides** strip — so always re-run `generate_latest_guides.py` afterwards.
> 2. **Show a reading-time estimate in its hero.** `patch_reading_time.py` adds it to `.hero-meta`.
> 3. **Have an accordion-structured References section before the signature block.**
>    `patch_references_accordion.py` builds a collapsible `<details>` References block and places
>    it right before `.dr-card-wrap`. It sources citations from the guide's footer
>    `<p>References: A · B · C</p>` line (or the hero-meta `Guidelines:` value), so **author the
>    guide with a real footer references line** (· separated). For a guide whose sources are only
>    cited inline, pass a JSON file of citations:
>    `python3 patch_references_accordion.py --overrides refs.json` where `refs.json` is
>    `{ "<filename>": ["Citation 1", "Citation 2", …] }`. **Never fabricate citations** — list only
>    sources the guide actually relies on. Run `--report` to audit reference coverage site-wide.

4. After all scripts succeed, stage the new guide and any modified files, then commit and push to `main`:

```bash
git add guides/<filename> guides/index.html sitemap.xml latest_guides.json
git commit -m "Add <filename> with full structure setup"
git push -u origin main
```

5. Remind the user of two things to check manually in the guide HTML:
   - Each inline `<figure>` image should have a `<figcaption>` with `<p class="fig-desc">` (plain description) and optionally `<dl class="fig-abbrevs">` for any abbreviations used in the image — the lightbox will display both.
   - The guide's script tag `<script src="../assets/image-lightbox.js" defer></script>` should be present near `</body>` (patch_image_lightbox.py adds it if missing).
