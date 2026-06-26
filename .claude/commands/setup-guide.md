# Setup New Guide

Build a new patient-education guide in `guides/` to house style, then run all
post-creation patch scripts.

**Usage:** `/setup-guide <filename>`
**Example:** `/setup-guide dry-weight-determination.html`

The user passes a guide filename (with or without `.html`) as `$ARGUMENTS`. If the
file does not exist yet, author it first using **Part A**; if it already exists, skip
to **Part B** (the patch pipeline).

---

## Part A — Authoring a new guide (scaffold & house style)

New guides are self-contained HTML documents that match the existing library. The
fastest reliable way to build one is to **copy the structure of an existing sibling**
and replace its content — do not invent a new layout.

- **Pick the right template by shape:**
  - *Dual-mode* (patient + clinician tabs), e.g. `filipino-nephrologist-challenges.html`,
    `kain-pa-rin.html`, `post-dialysis-fatigue.html` — use when the guide has both a
    lay narrative and clinician-facing evidence/algorithms.
  - *Single-mode* patient guide — use most other guides as the template.
- **Languages.** Every translatable string in **patient-mode** content needs four
  sibling spans, always in order `en`, `tl`, `ceb`, `kap` (en has no class; the other
  three carry `class="lang-hidden"`):
  ```html
  <span data-lang="en">…</span>
  <span data-lang="tl" class="lang-hidden">…</span>
  <span data-lang="ceb" class="lang-hidden">…</span>
  <span data-lang="kap" class="lang-hidden">…</span>
  ```
  Omitting a language makes that section blank in that language. **Clinician-mode**
  (`mode-physician`) sections may be English-only (see `post-dialysis-fatigue.html`).
  Keep fixed technical terms (e.g. "Body Composition Monitor (BCM)", "bioimpedance",
  lab units) untranslated, with a short plain gloss per language.
- **Dual-mode toggle.** Use a per-guide localStorage key (`wgmr-<slug>-mode` /
  `wgmr-<slug>-lang`). Sections are `class="section mode-patient"` or
  `class="section mode-physician"`; nav pills are `mode-patient-pill` /
  `mode-physician-pill`. Include the pre-paint restore snippet right after `<body>`
  (never a post-paint restore — that reintroduces CLS; see `patch_mode_cls.py`).
- **Components — use only house classes** (no bespoke CSS in the master block):
  - Callout boxes: `<div class="alert alert-{teal|red|amber|green|purple}">` with an
    `.alert-icon` (house style uses an emoji glyph, e.g. 💡 ⚠️ ⛔ ✅ 🔬) and `.alert-body`
    (`<h4>` + `<p>`). teal = key idea/tip, red = STOP/danger, amber = caution,
    green = do-this, purple = myth-vs-mechanism / honesty.
  - Tables: `<div class="table-wrap"><table>…`.
  - Numbered algorithms: `.algo-card` → `.algo-header` + `.algo-row`
    (`.algo-step-num` + `.algo-content`).
  - FAQ: `.qa-item` → `.qa-q` + `.qa-a`.
  - Calculator embeds = **link cards**, not iframes:
    ```html
    <div class="calc-cards-wrap">
      <div class="calc-cards-label"><span data-lang="en">Try the Calculators</span>…</div>
      <a href="calc-SLUG.html" class="calc-card">
        <div class="calc-card-icon">⌬</div>
        <div class="calc-card-body">
          <div class="calc-card-title">Calculator name</div>
          <div class="calc-card-desc">One-line description.</div>
        </div>
        <span class="calc-card-arrow">Open →</span>
      </a>
    </div>
    ```
    Confirm each `calc-*.html` slug actually exists in `guides/` before linking.
  - Inline figures: `<figure>` with `<picture>` (webp `<source>` + png `<img>`),
    descriptive `alt`, and a `<figcaption class="fig-desc">` plain description
    (optionally `<dl class="fig-abbrevs">`). Reference `../images/<slug>-NN-name.{webp,png}`
    even if the images don't exist yet (generate them via the image skills afterward).
- **CSS placement (critical).** `patch_master_css.py` replaces **only the first
  `<style>` block** with `MASTER_CSS`. Component CSS that is *not* in `MASTER_CSS`
  (`.calc-card*`, `.qa-item`/`.qa-q`/`.qa-a`, `.algo-card*`, `.tier-badge`, etc.) must
  live in a **second `<style>` block** after the first, or the patch step will strip it.
  Harvest these blocks from a guide that already uses them (e.g.
  `post-dialysis-fatigue.html`, `fluid-management-dialysis.html`).
- **Page-tail order (enforced by `patch_signature_position.py`).** End every guide,
  outside `<main>`, as: `</main>` → optional `calc-cards-wrap` → `<!-- DR CARD -->`
  `<div class="dr-card-wrap">` → `<div class="related-guides">` → `<footer class="guide-footer">`.
- **Head/meta.** Set a unique `<title>`, `description`, `keywords`, `canonical`,
  full Open Graph + Twitter tags (`og:image` → `../images/<slug>-og.png`, 1200×630,
  `og:locale en_PH`), and JSON-LD (`Article` + `MedicalWebPage`). `patch_last_reviewed.py`
  manages the Last-Reviewed badge.
- **Wire the guide in:** add a card to `guides/index.html` under the right category,
  add a `related_guides.json` entry (and add it to the related arrays of its siblings),
  and add it to any relevant `Start Here — I have…` pathway. Then regenerate the sitemap.

> When in doubt, diff your new file's structure against the chosen template and make
> sure only the *content* differs, not the scaffold, class names, or script wiring.

---

## Part B — Post-creation patch pipeline

1. Normalize the filename — ensure it ends in `.html`.

2. Confirm the file exists at `guides/<filename>`. If it does not exist, build it first (Part A).

3. Run each script below in order, passing `--guide <filename>`. Report each step briefly.
   If a script fails, stop and show the error.

```bash
python3 patch_master_css.py --guide <filename>     # themed master CSS (pastel hero, Inter/Manrope/Nunito Sans)
python3 patch_font_link.py --guide <filename>       # Google Fonts <link> → Inter/Manrope/Nunito Sans (drops Lora/DM Sans)
python3 patch_hero_fetchpriority.py --guide <filename>
python3 patch_hero_fullwidth.py --guide <filename>
python3 patch_hero_maxwidth.py --guide <filename>
python3 patch_image_lightbox.py --guide <filename>
python3 patch_mode_cls.py --guide <filename>
python3 patch_signature_position.py --guide <filename>
python3 patch_last_reviewed.py --guide <filename>
python3 generate_sitemap.py
```

> **Dual-mode guides only:** after `patch_mode_cls.py`, also run
> `python3 patch_mode_restore.py --guide <filename>` to add the safe **pre-paint**
> physician-mode restorer (the pair is: post-paint restore forbidden, pre-paint restore
> required). Skip for single-mode guides.

> **Theme note:** The site uses the pastel hero theme with Inter (headlines/titles/numbers),
> Manrope (body), and Nunito Sans (hero subtitle). Both `patch_master_css.py` and
> `patch_font_link.py` must run. The optional `patch_hero_theme.py` (circular vignette +
> clinician cards) is **opt-in** — only for guides with a real hero photo and dual-mode
> clinical sections.

4. After all scripts succeed, stage the new guide and any modified files, then commit and push to `main`:

```bash
git add guides/<filename> sitemap.xml related_guides.json guides/index.html
git commit -m "Add <filename> with full structure setup"
git push -u origin main
```

5. Remind the user of two things to check manually in the guide HTML:
   - Each inline `<figure>` image should have a `<figcaption>` with `<p class="fig-desc">` (plain description) and optionally `<dl class="fig-abbrevs">` for any abbreviations used in the image — the lightbox will display both.
   - The guide's script tag `<script src="../assets/image-lightbox.js" defer></script>` should be present near `</body>` (patch_image_lightbox.py adds it if missing).
