# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this site is

`williamriveromd.com` is a static patient-education website for Dr. William Gregory M. Rivero, MD (Nephrology, Internal Medicine, Philippines). It consists of ~90 standalone HTML guides on kidney disease topics, a homepage (`index.html`), and a small Node.js proxy server for an AI feature.

## Development commands

```bash
# Local preview server (serves the static site at localhost:3000)
npm start                         # runs williamriveromd-server/server.js

# Install server dependencies (only needed once)
npm run install-server

# Python patch scripts — run from the repo root
python3 patch_master_css.py               # apply master CSS to all guides
python3 patch_master_css.py --dry-run     # preview changes without writing
python3 patch_master_css.py --guide anemia-management.html  # single guide

python3 patch_font_link.py                # set Google Fonts <link> → Inter/Manrope/Nunito Sans (drops Lora/DM Sans)
python3 patch_font_link.py --dry-run      # preview changes without writing
python3 patch_font_link.py --guide anemia-management.html   # single guide

python3 patch_kdigo2026.py                # apply KDIGO 2026 terminology fixes
python3 patch_kdigo2026.py --dry-run

python3 add_kap_toggle.py                 # add Kapampangan language button
python3 add_kap_toggle.py --dry-run

python3 fix_setlang_kap.py                # patch setLang() JS to support 'kap'
python3 fix_setlang_kap.py --dry-run

python3 patch_last_reviewed.py            # add/update Last Reviewed badges + JSON-LD on all guides
python3 patch_last_reviewed.py --dry-run
python3 patch_last_reviewed.py --guide anemia-management.html  # single guide

python3 patch_published_time.py           # stamp every guide with article:published_time (date + time, +08:00)
python3 patch_published_time.py --dry-run
python3 patch_published_time.py --guide hmo-ckd-coverage.html  # single guide

python3 patch_reading_time.py             # add/refresh the "Reading time" estimate in every guide hero
python3 patch_reading_time.py --dry-run
python3 patch_reading_time.py --guide understanding-ckd.html   # single guide

python3 patch_references_accordion.py            # accordion References section before the signature block (all guides)
python3 patch_references_accordion.py --report   # audit per-guide reference coverage (no writes)
python3 patch_references_accordion.py --dry-run
python3 patch_references_accordion.py --overrides refs.json  # supply citations for guides with no footer references
python3 patch_references_accordion.py --guide igan-guide.html  # single guide

python3 audit_apa_references.py                 # check APA-7 compliance of every guide's References accordion
python3 audit_apa_references.py --details       # show failing citation samples (which fields are missing)
python3 audit_apa_references.py --guide igan-guide.html  # single guide; exits 1 if anything fails (CI-friendly)

python3 patch_hero_meta.py                # hero byline: drop "Author" row, show Published date + References count
python3 patch_hero_meta.py --dry-run
python3 patch_hero_meta.py --guide understanding-ckd.html  # single guide

python3 patch_symptom_widget.py           # install the floating Symptom-Checker widget on every content guide
python3 patch_symptom_widget.py --report  # audit which eligible guides lack the widget (no writes)
python3 patch_symptom_widget.py --dry-run
python3 patch_symptom_widget.py --guide hmo-ckd-coverage.html  # single guide

python3 generate_latest_guides.py         # regenerate the "Latest guides" strip on guides/index.html
python3 generate_latest_guides.py --dry-run
python3 generate_latest_guides.py --count 6   # show N cards (default 12; the strip scrolls horizontally)

python3 generate_latest_calculators.py    # regenerate the "Latest calculators" carousel atop guides/calculators.html
python3 generate_latest_calculators.py --dry-run
python3 generate_latest_calculators.py --count 16  # show N cards (default 12; scrolls horizontally)

python3 generate_sitemap.py               # regenerate sitemap.xml from files on disk
python3 generate_sitemap.py --dry-run     # preview added/removed URLs without writing

python3 patch_hero_fetchpriority.py             # make each guide's hero (LCP) image load eager + high priority
python3 patch_hero_fetchpriority.py --dry-run   # preview changes without writing
python3 patch_hero_fetchpriority.py --guide understanding-ckd.html  # single guide
```

Run `patch_hero_fetchpriority.py` after adding any new guide so its first
(LCP) image ships with `fetchpriority="high" loading="eager"`. The script is
idempotent — a guide whose hero is already patched is skipped.

```bash
python3 patch_hero_fullwidth.py              # make every guide's hero image full-width
python3 patch_hero_fullwidth.py --dry-run    # preview changes without writing
python3 patch_hero_fullwidth.py --guide understanding-ckd.html  # single guide
```

Run `patch_hero_fullwidth.py` after adding any new guide to ensure the hero
(LCP) image figure has no `max-width` constraint and no centering `auto` margin,
and that the `<img>` itself has `width:100%;height:auto;display:block`. Safe to
re-run (idempotent). Run after `patch_hero_fetchpriority.py`.

```bash
python3 patch_hero_maxwidth.py               # cap every guide's hero image at max-width 600px, centered
python3 patch_hero_maxwidth.py --dry-run     # preview changes without writing
python3 patch_hero_maxwidth.py --guide diabetes-kidneys.html  # single guide
```

Run `patch_hero_maxwidth.py` after adding any new guide (and after
`patch_hero_fullwidth.py`) to cap the hero (LCP) `<img>` at `max-width:600px`
and center it (`margin:<top> auto <bot> auto`), so square (1:1) and portrait
(2:3) heroes don't render magnified at the full ~860px column width. The two
scripts coexist: `patch_hero_fullwidth.py` keeps the enclosing `<figure>`
full-width while this script caps and centers the `<img>` inside it (it only
touches the img's `max-width`/`margin`, which fullwidth never strips). The
script canonicalizes the hero's inline `style` — preserving `border-radius`,
`box-shadow`, and any author-set vertical margins, repairing missing-semicolon
merge bugs (e.g. `height:automax-width`) — and is idempotent. Banners using
`object-fit:cover` (deliberate fixed-height crops) are skipped.

```bash
python3 patch_mode_cls.py                 # remove physician-mode restore-on-load (CLS fix)
python3 patch_mode_cls.py --dry-run       # preview changes without writing
python3 patch_mode_cls.py --guide el-nino-heat-dialysis.html  # single guide
```

`patch_mode_cls.py` strips the bottom-of-page IIFE that restored physician
mode from `localStorage` *after first paint* — that post-render patient→
physician swap was the Cloudflare-RUM CLS of 0.364 on
`body.physician-mode>div.mode-physician`. `setMode()` still writes the choice
to `localStorage`, so in-page tab toggling is unaffected. Never reintroduce a
*post-paint* restore-on-load; run this script after adding any new dual-mode
guide, then run `patch_mode_restore.py` (below) to add the safe restorer.

```bash
python3 patch_mode_restore.py                 # add pre-paint physician-mode restore (no CLS)
python3 patch_mode_restore.py --dry-run       # preview changes without writing
python3 patch_mode_restore.py --guide igan-guide.html  # single guide
```

`patch_mode_restore.py` makes the clinician-tab choice survive page refresh
*without* reintroducing the CLS bug: it injects a tiny synchronous script
immediately after the opening `<body>` tag that applies `physician-mode`
**before first paint** (zero layout shift), reading the guide's own mode
localStorage key. Tab-button active states sync on DOMContentLoaded (a
color-only change). The invariant pair: mode restores are allowed **only**
pre-paint (this script); post-paint restores are forbidden
(`patch_mode_cls.py` removes them). Run both, in that order, after adding
any new dual-mode guide. Idempotent.

```bash
python3 patch_signature_position.py              # move dr-card + related-guides to right before footer
python3 patch_signature_position.py --dry-run    # preview changes without writing
python3 patch_signature_position.py --guide obesity-ckd.html  # single guide
```

Run `patch_signature_position.py` after adding any new guide or calculator section to ensure
the canonical page-tail order is: `</main>` → `<!-- DR CARD -->` → `<div class="dr-card-wrap">`
→ `<div class="related-guides">` → `<footer class="guide-footer">`. Nothing should intervene
between the signature block and the related-guides block, or between the related-guides block
and the footer. The script is idempotent. **When building a new guide, always place the
dr-card-wrap and related-guides immediately before `<footer class="guide-footer">`, outside
`<main>`, as the very last HTML before the footer.**

### Guide-wide content policies (every guide, from here on)

Invariants every guide must satisfy. The `/setup-guide` command runs the scripts in order.

1. **Date- and time-stamped publish date (= the merge/publish-to-main date).** Every guide carries
   an immutable `<meta property="article:published_time" content="YYYY-MM-DDTHH:MM:SS+08:00">`
   recording *when it went live* (Manila time). `patch_published_time.py` derives it from the
   guide's first git-commit datetime (for direct-to-main commits this is the merge moment) or
   "now" when stamped at merge time, and never overwrites an existing stamp. It also aligns the
   JSON-LD `datePublished`.

2. **Auto-appears in the Latest guides strip.** The strip is data-driven (newest
   `article:published_time` first), so a freshly stamped guide shows up automatically — **always
   re-run `generate_latest_guides.py` after adding any guide, even if not explicitly asked.** A
   `SessionStart` hook (`.claude/settings.json`) also runs `patch_published_time.py` +
   `generate_latest_guides.py` each session as a safety net, so a new guide is never left out.

3. **Reading-time estimate in the hero.** `patch_reading_time.py` adds a "Reading time" row to the
   `.hero-meta` block, computed from the guide's English word count (translations carried as
   `lang-hidden` data-lang siblings are excluded so the count is not inflated 4×) at 200 wpm. The
   badge uses inline styles so `patch_master_css.py` will not clobber it.

4. **No Author byline in the hero.** The author is credited in the signature/dr-card block at the
   end of the page, so `patch_hero_meta.py` strips any "Author: W Rivero…" row from `.hero-meta`
   and instead shows a **Published** date row and a **References** count row (the number of items
   in the accordion). Inline-styled, idempotent; never add an author line to a new guide's hero.

5. **Accordion References section before the signature block — APA 7 format.** Every guide's
   References block is a collapsible `<details class="ref-acc">` rendered by
   `patch_references_accordion.py` and inserted immediately before `.dr-card-wrap`.
   **The accordion is the only rendered References location.** Do NOT add a
   `<p>References: A · B · C</p>` line to the guide's `<footer class="guide-footer">` —
   the old footer-references placement is deprecated and must be removed on touch
   (references appearing twice — once in the footer, once in the accordion — is a
   duplication bug). For the patcher's data source, supply citations via
   `--overrides refs.json` (`{ "<file>": ["APA citation 1", …] }`); the patcher
   preserves an existing accordion's `<ol>` on subsequent runs, so once built the
   accordion is self-sourced. Each `<li>` in the rendered accordion **must be
   in APA 7 format**: `Author, A. A., Author, B. B., & Author, C. C. (Year). Sentence-case
   title. <em>Journal Name</em>, <em>Volume</em>(Issue), pages. <a href="https://doi.org/…">https://doi.org/…</a>`.
   - Up to 20 authors → list all (comma + `&` before the last). 21+ → first 19, `... `, final author.
   - Titles in **sentence case** (only first word + first word after a colon/em-dash capitalised);
     preserve acronyms (CKD, AKI, ChatGPT, SaMD, etc.).
   - Journal name in full title-case (not the PubMed abbreviation), italicised via `<em>`.
     Volume italicised via `<em>`; issue in parens (not italicised).
   - DOI rendered as a real `<a href="https://doi.org/...">…</a>` link. The patcher's tag
     whitelist preserves `<em>`, `<strong>`, `<b>`, `<i>`, and `<a>` in each citation —
     other inline tags are stripped. **Do not paste short-form citations** like
     "Smith 2023 (Nature)" — those are pre-APA legacy and must be migrated when touched.
   The canonical reference exemplar is `guides/ai-in-nephrology-practice.html` (26 sources,
   PubMed-verified via the `mcp__PubMed__*` MCP). For a guide that cites sources only inline,
   supply them with `--overrides refs.json` (`{ "<file>": ["APA citation 1", …] }`).
   **Never fabricate medical citations** — list only sources the guide actually relies on, and
   verify author/year/journal/volume/pages/DOI against PubMed before publishing.
   - `patch_references_accordion.py --report` audits coverage (count only).
   - **`audit_apa_references.py`** checks each citation's APA-7 compliance (italics for
     journal+volume, DOI/URL link, year, author block, page range) and reports the per-guide
     compliance ratio. **Run this before declaring a new guide done — a 0/N or partial
     compliance score means legacy short-form citations ("Smith 2023 NEJM", "KDIGO 2026",
     "EO 192 s.2015") slipped in and must be rewritten to full APA via PubMed lookups.** Pure interactive tools (calculators, symptom-checker, label
     scanner, recipe analyzer, interpreters, blank logs, the atlas/physiology reference
     pages) have no citable sources and are the documented exceptions — they're excluded
     by both the patcher and the audit.

6. **Justified body text.** Every guide's narrative body — every `<p>` inside a
   `<section class="section">` — is **fully justified** with automatic hyphenation
   (`text-align: justify; hyphens: auto`). This is enforced by `MASTER_CSS` in
   `patch_master_css.py` (`.section p` rule), so no per-guide override is needed. **Do not
   author `<p>` with inline `style="text-align:left"` or wrap body paragraphs outside
   `<section class="section">`** — that escapes the policy. Hero copy, alert-body `<p>`,
   figure captions, FAQs (`.qa-a`), and table cells are intentionally left ragged-right
   because justifying short or constrained-width content opens distracting rivers of
   whitespace; only the long-form section paragraphs are justified.

7. **Evidence Snapshot card — fixed value column.** Clinician-mode guides surface
   an "Evidence Snapshot" card (`<aside class="hero-cards mode-physician"> →
   .ov-card → .ov-list → .ov-stat (.v + .l)`). Value column (`.v`) widths vary —
   `"0"` vs `"−7 mmHg"` vs `"G4–G5"` vs `"AHA 2023"` — and with the original flex
   layout each row's label (`.l`) started at a different x. `MASTER_CSS` now
   pins every `.ov-stat` to `display:grid; grid-template-columns:104px 1fr`
   (with `!important` to defeat any stray per-guide overrides). The 104 px is
   wide enough for the longest typical clinical value; wider entries wrap inside
   the column rather than pushing the label right. Every description column now
   shares the same x-position. **Never re-add per-guide `min-width`/`flex-shrink`
   on `.ov-stat .v` and do not author a `.v` value longer than ~8 characters** —
   the 104 px column is fixed by design. Values are **center-aligned** within
   the column (`text-align:center`) so short ("0") and wide ("−7 mmHg") entries
   read as a balanced metrics column.

8. **Text contrast in both light and dark mode (WCAG AA).** Every visible text
   element in a guide must pass **≥ 4.5:1** contrast against its background for
   normal text (`< 18.66 px` or `< 24 px` non-bold) and **≥ 3:1** for large text
   (`≥ 18.66 px` bold or `≥ 24 px`) **in both light and dark mode**, with the
   contrast walked through the actual ancestor-background chain (translucent
   parents flattened). Always test the new guide with `html[data-theme="dark"]`
   active before declaring it done. Common failure patterns to avoid:
   - **`color:var(--navy)` on text inside a card that uses a dark `--bg` in dark
     mode** — navy-on-navy is invisible. Use `var(--text)` or `var(--text-mid)`
     for body text and remap any per-guide navy heading via
     `html[data-theme="dark"] .my-card h4 { color: var(--text-mid) }`.
   - **Light-bg cards (`.illus-wrap-light`, hard-coded `#fff` cards) that keep
     their light background in dark mode** — the inherited dark-mode text colour
     turns invisible. Either pin the bg to dark in dark mode, or pin the text to
     a dark value (e.g. `#2a3548`) inside the light-bg card.
   - **White-on-`var(--teal)` chips** (`.fig-letter`, `.nt-section-tag`,
     `.unit-btn.active`) — `--teal` brightens in dark mode and the ratio drops
     below 4.5:1. Use a deep teal (`#0e4a50`) for the dark variant.
   - **`color:var(--text-faint)`** on small text — bumped to `#9ba6b8` in dark
     mode to clear 4.5:1 on the standard `#1a2535` dark card; never lower it.
   - **Hardcoded literal colours** (`#1f3864`, `#7a859a`, etc.) bypass the
     dark-mode token swap entirely. Always use the design tokens (`--text`,
     `--text-mid`, `--text-muted`, `--text-faint`, `--teal`, `--navy`, `--bg`,
     `--white`, `--border`) so the colour adapts automatically.

   Site-wide patterns are caught by `MASTER_CSS` dark-mode remaps (see the
   "Dark-mode contrast remaps" block in `patch_master_css.py`); guide-specific
   ones must live in the **second `<style>` block** of the guide so
   `patch_master_css.py` does not strip them.

10. **Category-tinted tile icons.** Every `.guide-tile` in `guides/index.html`
    renders its leading icon as a **uniform rounded square** (`30 × 30 px`,
    `border-radius: 8px`) tinted to the **parent section's category colour**.
    The tint is wired via a single `--cat-color` custom property set on each
    `.guide-section[data-section="…"]` in master CSS; `.tile-icon` resolves
    it with `background: color-mix(in srgb, var(--cat-color) 14%, transparent)`
    and `color: var(--cat-color)`. **Do not author per-tile `.tile-icon.calc`
    / `.read` / `.tool` / `.ph` / `.dl` overrides** — those classes are
    inert and the icon now derives its hue from category only. **Pick an
    icon (`data-icon="…"`) that actually depicts the guide's subject** —
    heart for cardio-renal, kidney for renal anatomy, drop for fluid/
    dialysis, flask for labs, etc. Available icon keys are defined in the
    `ICONS` map near the bottom of `guides/index.html`; add a new key
    there if no existing glyph fits.

11. **Image lightbox with plain-language descriptions.** Every content guide
    must (a) load `assets/image-lightbox.js` via a single deferred script tag
    just before `</body>`, and (b) give every inline `<figure>` a structured
    `<figcaption>` the lightbox can read. The v2.0 shape:

    ```html
    <figcaption>
      <p class="fig-desc">Plain-language description of the image.</p>
      <dl class="fig-abbrevs">
        <dt>SERCA</dt><dd>Sarco/endoplasmic reticulum Ca²⁺-ATPase</dd>
        <dt>UF</dt><dd>Ultrafiltration</dd>
      </dl>
    </figcaption>
    ```

    Behavior: single tap opens the lightbox with the `.fig-desc` line and
    any abbreviations panel; double-tap opens the full image in a new tab.
    A copyright-only figcaption is not enough — the lightbox caption panel
    will be blank. **When authoring a new figure, the plain-language
    description is required; the abbreviation list is required whenever
    the image contains any acronym.** `patch_image_lightbox.py` installs
    the script tag idempotently — it inserts it if missing and swaps any
    legacy `image-open.js` reference.

12. **Glossary & abbreviations accordion (`<!-- GLOSSARY-START --> … END -->`).**
    Every narrative content guide carries a collapsible `<details class="glossary-acc">`
    section placed immediately after `</main>` and before `<!-- REFERENCES-ACC-START -->`.
    It has two `<dl>` blocks: **Abbreviations** (every acronym or initialism used
    anywhere in the guide, defined once) and **Terms** (any specialised word a
    lay reader would not know — mechanisms, anatomical zones, physiology
    concepts). The section header is `Glossary & abbreviations` with EN/TL/CEB/KAP
    translations wired via `data-lang` spans exactly like every other translatable
    string. It gates only on narrative content — the same exclusion set as
    `audit_apa_references.py` and `patch_symptom_widget.py` (calculators,
    printable logs, the atlas/physiology reference pages) skip it. Rationale:
    the glossary is the on-page dictionary the lightbox's per-figure
    `<dl class="fig-abbrevs">` blocks point back to, and it is what patients
    and clinicians alike open first when a term is unfamiliar. **A new guide
    is not done until this section is present with every acronym in it.**

9. **Category-tinted Latest-guides cards.** Each section in `guides/index.html`
   (`<div class="guide-section" data-section="…">`) has its own colour — visible
   as the small `.section-color-bar` ("|") before the section title:
   - `nephrology` → `#1a6b72` (teal)
   - `internal` → `#c55a11` (orange)
   - `nutrition` → `#2e6b3e` (green)
   - `lifestyle` → `#7c3aed` (violet)
   - `advanced` → `#6b46c1` (purple)
   - `dialysis` → `#1f3864` (navy)
   - `philippines` → `#c2410c` (amber-orange)
   - `download` → `#92710a` (gold)

   `generate_latest_guides.py` reads each guide's category from its tile in
   `guides/index.html` (via `data-section` on the parent `.guide-section`) and
   emits `style="--card-color:<hex>"` on every `.latest-card`. The `.latest-card`
   CSS uses that variable for both the gradient background and the hover shadow,
   so each card carries its category's identity across the strip. **Always
   re-run `generate_latest_guides.py` after** (a) adding a new guide tile,
   (b) moving a guide to a different section, or (c) editing the `SECTION_COLORS`
   palette. New categories added to the index need a matching entry in the
   `SECTION_COLORS` dict at the top of the generator. The same colour scheme is
   the single source of truth for any future category-tinted UI (filter pills,
   guide-tile accents, related-guide chips).

The **Latest guides** strip lives on `guides/index.html` between `<!-- LATEST-GUIDES-START -->`
and `<!-- LATEST-GUIDES-END -->` (above the mobile filter bar / "Continue reading" rail). Each
card shows the guide title, its publish date, and the guide's OG share image *peeking* on the
right edge (an absolutely-positioned, mask-faded thumbnail — the same treatment as the
`.spotlight-thumb` cards). The strip scrolls horizontally (fixed-width cards + scroll-snap) and
is regenerated by `generate_latest_guides.py` (newest publish time first) — do not hand-edit the
block; `latest_guides.json` is written alongside as the ordered data.

The **Latest calculators** carousel sits at the top of `guides/calculators.html` (between
`<!-- LATEST-CALCS-START -->` and `<!-- LATEST-CALCS-END -->`, just above `<main>`), the same
peeking-thumb horizontal-scroll treatment for the newest `calc-*` pages. It is regenerated by
`generate_latest_calculators.py` (writes `latest_calculators.json`); the block carries its own
scoped `lc-`-prefixed `<style>` so it survives `patch_master_css.py`.

**Calculator cards are colour-coded by category.** Each calculator grid `<section>` on
`guides/calculators.html` carries `style="--sec-color:#hex"`; the override `<style>` tints every
`.calc-results .related-card` by that inherited colour (via `color-mix` over a dark base, so white
text stays readable) instead of a uniform navy. The Latest-calculators carousel cards are tinted
to the same per-category colours by `generate_latest_calculators.py` (it reads each calculator's
section colour from the grid). Keep new calculators inside the correct category section so they
inherit the right colour.

**Floating Symptom-Checker widget.** Every content guide loads
`assets/symptom-checker-widget.js` (a vanilla-JS floating 🩺 button that opens the
symptom checker in a modal iframe) via a single deferred `<script>` before the final
`</body>`. `patch_symptom_widget.py` installs it, repairs the legacy broken
`../js/…` path, and is idempotent. It skips non-narrative pages: the guides index,
`symptom-checker.html` itself (the widget self-disables there anyway), calculators
(`calc-*`, the calculators index, `ckd-dri-calculator.html`), the pure
interpreter/atlas tools, and printable log/blank sheets. Run it (or rely on
`/setup-guide`) after adding any new guide; `--report` audits coverage.

```bash
python3 add_calc_nav_pill.py               # add floating bottom-center nav pill to all calculator pages
python3 add_calc_nav_pill.py --dry-run     # preview (shows each page's right-hand guide target)
python3 add_calc_nav_pill.py --guide calc-kfre.html  # single calculator page
```

Run `add_calc_nav_pill.py` after adding any new calculator page. It injects a
floating, fixed bottom-center rounded "pill" (between `<!-- CALC-NAV-PILL-START -->`
/ `END` markers, just before the final `</body>`) split into two chevron links:
the left chevron returns to the calculators index, the right chevron opens that
calculator's primary related guide — auto-detected as the first real content
guide in the page's Related Guides block (calculators/index/symptom-checker are
skipped; falls back to `understanding-ckd.html`, with per-page exceptions in the
script's `OVERRIDES` map). Targets `guides/calc-*.html` plus
`ckd-dri-calculator.html`. Idempotent — the existing block is stripped and
re-inserted each run, so right-hand targets refresh if Related Guides change.
Inserts before the **last** `</body>` so JS print-popup strings
(`win.document.write('…</body></html>')`) are never touched.

```bash
python3 patch_calc_handoff.py              # install the shared cross-calculator input handoff on all calculators
python3 patch_calc_handoff.py --dry-run
python3 patch_calc_handoff.py --guide calc-cockcroft-gault.html  # single calculator
```

Run `patch_calc_handoff.py` after adding any new calculator. Every calculator
loads `assets/calc-handoff.js`, a self-activating script that **carries the
common patient inputs across the whole calculator library** — age, sex, eGFR,
height (cm), weight (kg), serum creatinine (mg/dL) — via the `wgmr-rx-patient`
localStorage key, so entering them once prefills every related calculator. It
keys off the library's id-suffix convention (`<prefix>-age`, `-sex`, `-egfr`,
`-height`/`-ht`, `-weight`, `-scr`/`-creat`), prefills **only empty** fields
(never clobbers a user's entry), and is **unit-guarded** — weight/creatinine are
read and written only in their default units (no active `<prefix>-wbtn-lb` /
`<prefix>-cbtn-si` toggle), so a kg value is never pushed into a lb field. New
calculators inherit the feature automatically as long as their inputs follow the
`<prefix>-<field>` id convention. The script supersedes the old per-page
`RX-HANDOFF` blocks (removed on patch). Inserts before the **last** `</body>`.

```bash
python3 patch_calc_english_only.py         # strip translations from all calculators (English-only)
python3 patch_calc_english_only.py --dry-run
python3 patch_calc_english_only.py --guide calc-kfre.html  # single calculator
```

**Calculators are English-only.** `patch_calc_english_only.py` removes every
`data-lang="tl|ceb|kap"` translation element (depth-aware) and the `setLang`/
`wgmr-lang` language-restore machinery from each calculator (the on-load restore
would otherwise hide the English spans and blank the page for a visitor whose
last-used language wasn't English). Run it after adding any new calculator.
Because the shared patch scripts add multilingual hero-meta labels, the
calc-touching ones are **calculator-aware** and emit English-only labels for
`calc-*` pages so translations never return: `patch_reading_time.py` (Read time),
`patch_hero_meta.py` (Published / References), `patch_references_accordion.py`
(References).

```bash
python3 build_companion_pdfs.py                 # render every downloads/*.html companion to PDF
python3 build_companion_pdfs.py --list          # list buildable companions
python3 build_companion_pdfs.py wgmr-gout-uric-acid-guide   # render a single companion
```

All downloadable **patient companion PDFs** (the `downloads/` filter on
`guides/index.html`) share one house style and are built HTML→PDF with WeasyPrint
(`pip install weasyprint`). The single source of truth for their look is
`downloads/_companion-style.css` (top-strip → navy hero + doctor badge → yellow
knowledge band → numbered sections → navy running headers → heat-map/data tables →
branded footer with page numbers). The canonical reference layout is
`downloads/wgmr-diabetic-diet-guide.html`.

To add or edit a companion: create/edit `downloads/<name>.html` linking the shared
stylesheet (`<link rel="stylesheet" href="_companion-style.css">`) — use **only**
classes defined in that CSS, never an inline `<style>` block — then run
`build_companion_pdfs.py` to (re)render `downloads/<name>.pdf`. Each `<div class="page">`
must fit exactly one A4 page; physical PDF page count should equal the number of
`.page` divs. Adjust shared colours/spacing in `_companion-style.css` only, so the
whole set stays uniform. Files beginning with `_` are partials and are not rendered.

Standard credential line (top-strip, every companion):
`W.G.M. Rivero MD · FPCP · DPSN ·  · williamriveromd.com · <year>`.

> The old per-PDF reportlab generators (`generate_holiday_companion_pdf.py`,
> `generate_sodium_food_guide_pdf.py`) have been **removed** — they produced a
> different, inconsistent look and would revert those PDFs out of the shared style.
> Do not reintroduce them; build companions via the shared HTML pipeline above. The
> PSN HD endorsement form is an official external document and is intentionally left
> in its original style.

The server requires `williamriveromd-server/.env` with `ANTHROPIC_API_KEY=...`.

There are no automated tests or linters.

## Architecture

### Static HTML guides (`guides/*.html`)

Each of the 90 guide files is a self-contained HTML document with:
- **Inline `<style>`** — all CSS lives inside the file, not in an external stylesheet
- **Inline `<script>`** — all JS at the bottom of the file
- **Multi-language content** — English, Tagalog, Cebuano, and Kapampangan text coexisting in the DOM, toggled by class

**Do not edit CSS directly in guide files.** The master CSS is maintained in `patch_master_css.py` (`MASTER_CSS` string near the top of the file) and batch-applied with the script. One-off edits to a guide's `<style>` block will be overwritten on the next `patch_master_css.py` run.

**Guide-specific CSS must live in a SECOND `<style>` block.** `patch_master_css.py` rewrites **only the first** `<style>` block in each file (see its `replace_style_block`). Any bespoke styling — especially for **standalone printable handouts/forms** (e.g. `bp-log-blank.html`, `bp-monitoring-log.html`, `alcohol-drinking-log.html`, with their `.toolbar`/`.page`/`.bp-log` layouts) — must be placed in a **second `<style>` block after the first**, so a master-CSS run never clobbers it. The first (master) block still supplies the design tokens (`--navy`, `--teal`, …) and base resets, so the second block can rely on them. ⚠️ Symptom of getting this wrong: the page renders **completely unstyled** after a `patch_master_css.py` run because its only `<style>` block was overwritten with the generic guide CSS (this is exactly what repeatedly "damaged" `bp-log-blank.html`). When building any standalone form, give it two style blocks from the start.

### Site-wide chrome conventions (lock-in)

These are the load-bearing layout conventions every guide must follow. All of them live in MASTER_CSS (in `patch_master_css.py`) plus a small number of HTML patchers. **Re-run the relevant patchers after adding any new guide, or after a manual edit, to lock the conventions back in.**

1. **Top nav bar** (`<header class="site-header">` — direct children, in order):
   - `<a class="brand">` — left
   - `<div class="header-lang">` — Lang chips (multilingual guides only)
   - `<nav class="header-nav">` — **must be a direct child** of `.site-header`; `margin-left:auto` flushes it to the right. The 4 links: **CALCULATORS · PHYSIOLOGY · ATLAS · ALL GUIDES**, with the current page rendered gold + non-clickable (`.is-current`).
   - ⚠️ Do NOT wrap `.header-nav` in another `<div>` — that breaks the auto-margin push. Run `patch_relocate_toggles.py` if a guide was built before the convention, or use the same patcher idiom for fresh guides.
2. **Floating toggle widgets** (every guide).
   - Bottom-right `.float-controls`: dark/light toggle (44 px circle, white in light theme, charcoal in dark).
   - Bottom-left `.float-controls-left`: desktop/mobile toggle when present, sitting below the print button.
   - Left-side stack (top → bottom): `.dl-fab` (download, `bottom:136px`, when present) → `.print-btn` (`bottom:80px`) → `.float-controls-left` (`bottom:24px`).
   - The symptom-checker FAB is automatically shifted left (`right:88px`) so it never overlaps the dark widget.
   - Run `patch_relocate_toggles.py` to migrate any guide built with the old in-bar dark/desktop buttons; the script is idempotent.
3. **Audience tabs** (dual-mode guides only — patient/clinician toggle below the header):
   - Labels are uniform: **"Patients & Families"** and **"Clinicians"** (no "For " prefix, no role emoticons).
   - `.audience-tabs` background **inherits the hero palette** — mint when patient mode is active, periwinkle when clinician mode is active — so the bar reads as one continuous strip with the hero. Hard-coded in MASTER_CSS.
4. **Hero must be properly closed** with its `</div>`. A missing close lets the hero engulf the rest of the page (symptom: hero background bleeds down to the footer). See `hematuria-blood-in-urine.html` commit for the canonical fix.
   - **Direct children of `<div class="hero-grid">` must be only**: `hero-copy`, `hero-cards`, `hero-figure`, `hero-toc`. Any other element (intro-callout, urgent-banner, translation-notice, stray `<h1>`/`<p>`, etc.) becomes an extra grid column and starves `.hero-copy` to near-zero width (symptom: title wraps one word per line, hero grows to 2000+ px tall). Content blocks like callouts/banners belong **outside** the hero, in a fresh `<div class="container">` right after `</section>`. Run `python3 validate_hero_grid.py` to scan all guides for this bug.
5. **Calculator index** (`guides/calculators.html`): main-grid `<a class="related-card">` cards show titles + descriptions only, **no** peeking thumbs. Only the Latest-Calculators carousel at the top shows category-hero thumbs (`generate_latest_calculators.py`). The carousel auto-includes **any** new calc that has an `article:published_time` — if the calc has no `og:image`, the script falls back to the matching `images/hero-cat-{section}.webp`, so a brand-new calc is **never silently dropped** from the Latest strip.
6. **Lang chips** (multilingual guides): exactly four (`glb-en/tl/ceb/kap`) inside `<div class="header-lang">` adjacent to the brand. Calculators and tools are English-only (no lang chips).

**Theme & typography.** Guides/calculators use the pastel hero theme — light mint hero
(patient) / light periwinkle hero (clinician) with dark text — and an all-sans type system:
**Inter** for headlines, section titles, and numbers; **Manrope** for body text and UI;
**Nunito Sans** for the hero subtitle. Lora and DM Sans have been removed. The fonts are
declared in `MASTER_CSS` *and* loaded via the `<head>` Google Fonts `<link>`, which is managed
by `patch_font_link.py` (run it alongside `patch_master_css.py`). The homepage (`index.html`),
the guides listing (`guides/index.html`), and `nephrology-atlas.html` keep their own font
stacks and are excluded from both. The optional `patch_hero_theme.py` adds the epilepsy-style
circular-vignette + clinician cards and is **opt-in** (only for guides with a hero photo +
dual-mode clinical sections), not part of the default rollout.

**Circular-vignette hero placement (convention).** On desktop (≥821px) a guide's circular
vignette (`figure.hero-figure > .hero-vignette`) renders as an **oversized disc that bleeds
off the top and right** of the hero — copy on the left (z-index above the disc), disc anchored
`top:-64px; left:58%` so it touches/clips the top border and overflows the right. The MASTER_CSS
rule is scoped to `:is(body:not(.physician-mode), body.single-mode)`, i.e. it applies to
patient-mode heroes **and** to **single-tab guides**. A single-tab guide (one with no
Patient/Clinician mode toggle — including **physician/clinician-only** guides) must carry the
`single-mode` class on `<body>` so its lone vignette bleeds like a patient hero; without it a
physician-only guide (`<body class="physician-mode">`) would be excluded and the disc would
render small and contained. **When building any single-tab guide, add `single-mode` to the
body class** (e.g. `<body class="physician-mode single-mode">`). The bleed is desktop-only;
the ≤820px mobile stack is untouched, and `.hero{overflow:hidden}` clips the disc to the hero.

### Language system

All pages use the same in-DOM multilingual pattern:

```html
<span data-lang="en">English text</span>
<span data-lang="tl" class="lang-hidden">Tagalog text</span>
<span data-lang="ceb" class="lang-hidden">Cebuano text</span>
<span data-lang="kap" class="lang-hidden">Kapampangan text</span>
```

`setLang(lang)` iterates `['en','tl','ceb','kap']`, toggling `lang-hidden` on all `[data-lang]` elements, then persists the selection to `localStorage`. The active language button gets the `active` CSS class.

- **Homepage** (`index.html`): button IDs `lb-en`, `lb-tl`, `lb-ceb`, `lb-kap`
- **Guides** (`guides/*.html`): button IDs `glb-en`, `glb-tl`, `glb-ceb`, `glb-kap`

When adding new translatable text to a guide, always add sibling `data-lang` spans for all four languages; omitting one causes that language to show no content in that section.

### CSS color tokens

Two token sets exist — **do not mix them**:

| Token | Homepage (`index.html`) | Guides (master CSS) |
|---|---|---|
| Body text | `--text: #111827` | `--text: #1e2a38` |
| Background | `--cream: #f4f6f9` | `--bg: #f9fafb` |
| Accent | `--teal: #145c63` | `--teal: #1a6b72` |

Guides also expose `--text-mid`, `--text-muted`, `--text-faint`, `--red`, `--red-soft`, `--amber`, `--amber-soft`, `--green`, `--green-soft`, `--purple`, `--purple-soft`. All foreground/background combinations are WCAG AA verified (≥4.5:1 normal text, ≥3:1 large text).

Dark mode on the homepage is `html[data-theme="dark"]`. Guides do not currently have dark mode.

### Node.js proxy server (`williamriveromd-server/`)

An Express server that:
1. Serves the static site (fallback: `index.html` for any unknown route)
2. Exposes `POST /api/analyze` — proxies to `https://api.anthropic.com/v1/messages`, hard-codes model to `claude-haiku-4-5-20251001` and caps `max_tokens` at 2000, rate-limited to 20 req / 15 min

This server is not used in GitHub Pages production (which serves only static files). It supports local development and any alternative hosting where server-side API key protection is needed.

### Supporting data files

- `related_guides.json` — maps each guide filename to an array of related guide filenames; consumed by the "Related Guides" section rendered in each guide
- `sitemap.xml` — generated by `generate_sitemap.py`; run it after adding or removing any page (it preserves existing per-URL changefreq/priority and only adds/removes entries). Do not hand-edit.
- `downloads/` — PDF patient handouts; referenced from guides and the homepage

### Deployment

GitHub Pages via `CNAME` pointing to `williamriveromd.com`. There is no build step — commit HTML files directly. The `sitemap.xml` and `robots.txt` are static files in the repo root.

## Git workflow

**Commit directly to `main`.** Do not create feature branches, do not open PRs, do not ask about PRs. Edit files in place and push straight to `main`. Only use a branch + PR workflow if the user explicitly asks for "review mode" or a PR.

## graphify

This project has a knowledge graph at graphify-out/ with god nodes, community structure, and cross-file relationships.

Rules:
- For codebase questions, first run `graphify query "<question>"` when graphify-out/graph.json exists. Use `graphify path "<A>" "<B>"` for relationships and `graphify explain "<concept>"` for focused concepts. These return a scoped subgraph, usually much smaller than GRAPH_REPORT.md or raw grep output.
- If graphify-out/wiki/index.md exists, use it for broad navigation instead of raw source browsing.
- Read graphify-out/GRAPH_REPORT.md only for broad architecture review or when query/path/explain do not surface enough context.
- After modifying code, run `graphify update .` to keep the graph current (AST-only, no API cost).

## PDF handling

This project has the `markitdown` MCP server configured (`.mcp.json`, package
`markitdown-mcp`) for converting documents to Markdown. **Whenever the user
shares or references a PDF (uploaded file or local path), use the `markitdown`
MCP tool to convert it to Markdown instead of reading the raw PDF directly** —
it produces cleaner structured text (headings, tables, lists) than ad hoc PDF
text extraction. This applies to reference PDFs, lab reports, journal articles,
etc. provided for a guide. Pure image PDFs (scans with no text layer) may still
need a different approach.
