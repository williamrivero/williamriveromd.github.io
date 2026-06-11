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

python3 patch_kdigo2026.py                # apply KDIGO 2026 terminology fixes
python3 patch_kdigo2026.py --dry-run

python3 add_kap_toggle.py                 # add Kapampangan language button
python3 add_kap_toggle.py --dry-run

python3 fix_setlang_kap.py                # patch setLang() JS to support 'kap'
python3 fix_setlang_kap.py --dry-run

python3 patch_last_reviewed.py            # add/update Last Reviewed badges + JSON-LD on all guides
python3 patch_last_reviewed.py --dry-run
python3 patch_last_reviewed.py --guide anemia-management.html  # single guide

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
`body.physician-mode>div.mode-physician`. Dual-mode guides must always start
in patient mode (the default CSS state). `setMode()` still writes the choice
to `localStorage`, so in-page tab toggling is unaffected. Never reintroduce a
restore-on-load; run this script after adding any new dual-mode guide.

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

```bash
python3 generate_holiday_companion_pdf.py    # rebuild downloads/wgmr-holiday-kidney-syndrome-guide.pdf
```

Run `generate_holiday_companion_pdf.py` (requires `pip install reportlab pillow`)
after updating any of the Holiday Kidney Syndrome guide's images — it rebuilds the
patient companion PDF from `images/holiday-kidney-syndrome-*.png` plus condensed
guide text.

The server requires `williamriveromd-server/.env` with `ANTHROPIC_API_KEY=...`.

There are no automated tests or linters.

## Architecture

### Static HTML guides (`guides/*.html`)

Each of the 90 guide files is a self-contained HTML document with:
- **Inline `<style>`** — all CSS lives inside the file, not in an external stylesheet
- **Inline `<script>`** — all JS at the bottom of the file
- **Multi-language content** — English, Tagalog, Cebuano, and Kapampangan text coexisting in the DOM, toggled by class

**Do not edit CSS directly in guide files.** The master CSS is maintained in `patch_master_css.py` (`MASTER_CSS` string near the top of the file) and batch-applied with the script. One-off edits to a guide's `<style>` block will be overwritten on the next `patch_master_css.py` run.

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
