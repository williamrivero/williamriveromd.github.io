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
- **Circular vignette hero — single-mode only.** The oversized circular
  vignette disc (`figure.hero-figure > .hero-vignette`) is the *single-mode*
  hero treatment: it applies to patient-only guides and to clinician-only
  guides marked `<body class="… single-mode">`. **Dual-mode guides must NOT
  render the vignette in clinician mode** — the clinician hero is the
  Evidence-Snapshot aside (`<aside class="hero-cards mode-physician">`) on
  the left with copy on the right, not a portrait disc. To enforce this on a
  dual-mode guide, scope the figure to patient mode by adding `mode-patient`
  to its class — `<figure class="hero-figure mode-patient">` — so
  `body.physician-mode .mode-patient { display:none }` hides it cleanly when
  the clinician tab is active. (Leaving the figure unscoped lets it bleed
  into the clinician hero, fighting the Evidence-Snapshot card for space.)
  See `anemia-management.html` for the canonical wiring.
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
- **Evidence Snapshot (clinician mode).** Dual-mode guides whose clinician hero
  carries an Evidence Snapshot card use `<aside class="hero-cards mode-physician">
  → <div class="ov-card"> → <div class="ov-list"> → <div class="ov-stat">
  (<span class="v"> + <span class="l">)`. `MASTER_CSS` pins every `.ov-stat` to a
  fixed-column grid (`grid-template-columns:104px 1fr`) so every label (`.l`)
  starts at the same x regardless of value (`.v`) width. Keep `.v` content short
  (≤ ~8 chars — `"0"`, `"−7 mmHg"`, `"AHA 2023"`, `"G4–G5"`); longer values wrap
  inside the 104 px column rather than pushing the label right. Do **not** add
  per-guide `min-width`/`flex-shrink` on `.ov-stat .v`.
- **WCAG AA contrast in both modes.** Every text element in the new guide must
  hit **≥ 4.5:1** for normal text and **≥ 3:1** for large text (`≥ 18.66 px`
  bold or `≥ 24 px`) against its actual rendered background, in **both** light
  mode and `html[data-theme="dark"]`. Always check the guide in dark mode
  before reporting it complete. Rules of thumb:
  - Use the design tokens (`var(--text)`, `var(--text-mid)`, `var(--text-muted)`,
    `var(--text-faint)`, `var(--teal)`, `var(--navy)`, `var(--bg)`, `var(--white)`,
    `var(--border)`) — never hard-code literal colours like `#1f3864` or
    `#7a859a`, they bypass the dark-mode token swap.
  - Any heading or value that uses `color:var(--navy)` on a card whose `--bg`
    flips dark in dark mode needs a per-guide remap:
    `html[data-theme="dark"] .my-card h4 { color: var(--text-mid) }`.
  - Light-background cards that stay light in dark mode (e.g. `.illus-wrap-light`)
    must pin their text to a dark colour, not inherit the light dark-mode text.
  - White-on-`var(--teal)` chips fail in dark mode — use `#0e4a50` for the
    dark variant.
- **Justified body text.** All narrative body paragraphs (`<p>` inside
  `<section class="section">`) render fully justified with automatic hyphenation —
  enforced by `MASTER_CSS` (`.section p { text-align: justify; hyphens: auto }`).
  When authoring: keep every body paragraph **inside** a `<section class="section">`
  wrapper and do **not** add inline `style="text-align:left"` or stray top-level
  `<p>` between sections. Hero copy, alert callouts, captions, FAQ answers (`.qa-a`),
  and table cells stay ragged-right by design (justifying short text creates
  whitespace rivers); only long-form section paragraphs are justified.
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
- **Pick the right category section.** `guides/index.html` is split into
  `<div class="guide-section" data-section="…">` blocks (nephrology, internal,
  nutrition, lifestyle, advanced, dialysis, philippines, download) — each with
  its own colour bar. The guide's category is its **visual identity**: the
  matching colour propagates to its Latest-guides card (generated by
  `generate_latest_guides.py` which reads the tile's parent `data-section`)
  AND to the tile's leading icon chip (which inherits the section's
  `--cat-color`). Adding the tile to the wrong section paints the wrong
  colour everywhere. After tiling, **always re-run `generate_latest_guides.py`**
  so the new card picks up its category tint.
- **Tile icon: rounded-square chip, category-coloured, content-appropriate.**
  Every tile renders its `<div class="tile-icon" data-icon="…">` as a
  uniform `30 × 30 px` rounded square; the background is a soft tint of
  the parent section's `--cat-color` and the SVG strokes the same hue —
  no per-tile colour overrides allowed (`.tile-icon.calc/.read/.tool/
  .ph/.dl` legacy classes no longer paint anything). The hue is automatic
  the moment the tile sits in the correct `<div class="guide-section">`.
  **Choose `data-icon` to match the guide's subject** (heart → cardio-renal,
  kidney → renal anatomy, drop → fluid/dialysis, flask → labs, dna →
  genetics, brain → neuro, alert → red-flag/refractory, scale → balance/
  electrolytes, etc.). The full icon library lives in the `ICONS = { … }`
  map near the bottom of `guides/index.html`; add a new key there if no
  existing glyph fits.

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
python3 patch_symptom_widget.py --guide <filename>      # floating Symptom-Checker widget (../assets/symptom-checker-widget.js)
python3 patch_mode_cls.py --guide <filename>
python3 patch_signature_position.py --guide <filename>
python3 patch_last_reviewed.py --guide <filename>          # "Last Reviewed" badge + article:modified_time + JSON-LD
python3 patch_published_time.py --guide <filename>         # article:published_time stamp (= merge/publish date, +08:00)
python3 patch_reading_time.py --guide <filename>           # "Reading time" estimate in the hero
python3 patch_references_accordion.py --guide <filename>   # accordion References section before the signature block
python3 audit_apa_references.py --guide <filename>         # HARD-FAIL gate: every citation must be APA-7 (italic journal, DOI link, year, author block)
python3 patch_hero_meta.py --guide <filename>              # hero byline: drop Author, show Published date + References count
python3 generate_sitemap.py
python3 generate_latest_guides.py                          # refresh the "Latest guides" strip on guides/index.html (new guide auto-appears)
python3 generate_latest_calculators.py                     # if a calc-* page: refresh the "Latest calculators" carousel on calculators.html
```

> **References audit is a hard gate.** `audit_apa_references.py --guide <file>`
> exits 1 if any citation in the footer line fails the APA-7 heuristics (italic
> `<em>` journal, `doi.org` or URL link, `(YYYY)` year, `Author, X.` block,
> page range). Do NOT declare the new guide done until the audit reports
> `N/N` compliant. If you see partial compliance, the footer `References:`
> line still carries legacy short-form snippets ("Smith 2023 NEJM", "KDIGO
> 2026", "EO 192 s.2015") — rewrite them to full APA via the PubMed MCP
> (`mcp__PubMed__lookup_article_by_citation` + `mcp__PubMed__get_article_metadata`).

> **Dual-mode guides only:** after `patch_mode_cls.py`, also run
> `python3 patch_mode_restore.py --guide <filename>` to add the safe **pre-paint**
> physician-mode restorer (the pair is: post-paint restore forbidden, pre-paint restore
> required). Skip for single-mode guides.

> **Theme note:** The site uses the pastel hero theme with Inter (headlines/titles/numbers),
> Manrope (body), and Nunito Sans (hero subtitle). Both `patch_master_css.py` and
> `patch_font_link.py` must run. The optional `patch_hero_theme.py` (circular vignette +
> clinician cards) is **opt-in** — only for guides with a real hero photo and dual-mode
> clinical sections.

> **Every new guide must (policy):**
> 1. **Be date- and time-stamped of when it was merged/published.** `patch_published_time.py`
>    writes an immutable `<meta property="article:published_time">` (Manila time) — the **publish
>    date equals the merge/publish-to-main date** (when the guide goes live). This orders the
>    **Latest guides** strip.
> 2. **Auto-appear in the Latest guides strip.** Because the strip (`generate_latest_guides.py`,
>    between `LATEST-GUIDES-START/END` on `guides/index.html`) is data-driven — newest
>    `article:published_time` first — a freshly stamped guide appears automatically. **Always
>    re-run `generate_latest_guides.py` after adding any guide; never skip it, even if not asked.**
>    A `SessionStart` hook also stamps + regenerates as a safety net so a new guide is never left
>    out of the strip.
> 3. **Show a reading-time estimate in its hero.** `patch_reading_time.py` adds it to `.hero-meta`.
> 4. **Carry no Author byline in the hero.** The author is credited in the signature/dr-card block
>    at the end of the page. `patch_hero_meta.py` strips any "Author: W Rivero…" row from
>    `.hero-meta` and instead shows a **Published** date row and a **References** count row. Do not
>    add an author line to a new guide's hero.
> 5. **Have an accordion-structured References section before the signature block, in APA 7 format.**
>    `patch_references_accordion.py` builds a collapsible `<details>` References block and places
>    it right before `.dr-card-wrap`, sourced from the guide's footer
>    `<p>References: A · B · C</p>` line (or the hero-meta `Guidelines:` value). **Every citation
>    in that footer line must be APA 7:** `Author, A. A., …, & Author, Z. Z. (Year). Sentence-case
>    title. <em>Journal Name</em>, <em>Volume</em>(Issue), pages. <a href="https://doi.org/…">https://doi.org/…</a>`.
>    Up to 20 authors → list all (`, & ` before the last); 21+ → first 19, ellipsis, final author.
>    Sentence-case title with acronyms preserved (CKD, AKI, ChatGPT, SaMD). Full title-case
>    journal name (not the PubMed abbreviation), italicised via `<em>`. DOIs as live
>    `<a href="https://doi.org/...">` links. The patcher preserves `<em>`, `<strong>`, `<b>`,
>    `<i>`, and `<a>` from the footer line; other inline tags are stripped.
>    **Build APA citations from PubMed metadata** — use the `mcp__PubMed__lookup_article_by_citation`
>    + `mcp__PubMed__get_article_metadata` MCP tools to fetch verified author lists, volume, issue,
>    pages, and DOI; never write a citation from memory. For a guide whose sources are only cited
>    inline, pass a JSON file of citations:
>    `python3 patch_references_accordion.py --overrides refs.json` where `refs.json` is
>    `{ "<filename>": ["APA citation 1", "APA citation 2", …] }`. **Never fabricate citations** —
>    list only sources the guide actually relies on. Run `--report` to audit reference coverage
>    site-wide. The canonical APA exemplar is `guides/ai-in-nephrology-practice.html`.

4. After all scripts succeed, stage the new guide and any modified files, then commit and push to `main`:

```bash
git add guides/<filename> guides/index.html sitemap.xml related_guides.json latest_guides.json
git commit -m "Add <filename> with full structure setup"
git push -u origin main
```

5. Remind the user of three things to check manually in the guide HTML:
   - Each inline `<figure>` image **must** have a `<figcaption>` with `<p class="fig-desc">` (plain-language description) — the lightbox reads this into its caption panel. A copyright-only figcaption is not enough. Add `<dl class="fig-abbrevs">` for any acronym shown in the image (`SERCA`, `UF`, `ABI`, etc.). See CLAUDE.md rule 11.
   - The guide's script tag `<script src="../assets/image-lightbox.js" defer></script>` should be present near `</body>` (patch_image_lightbox.py adds it if missing — idempotent).
   - A **Glossary & abbreviations** accordion (`<!-- GLOSSARY-START --> … <!-- GLOSSARY-END -->`) must sit immediately after `</main>` and before `<!-- REFERENCES-ACC-START -->`, listing every acronym used anywhere in the guide plus any specialised term a lay reader would not know. Two `<dl>` blocks: **Abbreviations** and **Terms**. Header string wired via `data-lang="en|tl|ceb|kap"` spans like every other translatable string. See CLAUDE.md rule 12; canonical exemplar is `guides/dialysis-cramps-stasis-pigmentation.html`. **The guide is not done until this section exists.**
