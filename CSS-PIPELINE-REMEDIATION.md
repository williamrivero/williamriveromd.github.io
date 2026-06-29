# CSS Pipeline Remediation — Findings & Recommendation

**Repo:** `williamrivero/williamriveromd.github.io`
**Date:** 2026-06-19
**Author:** Claude (Opus 4.8) working session
**Status:** Advisory — no remediation performed yet (only a safe, additive indent fix was shipped)

---

## TL;DR

The "single source of truth" CSS workflow described in `CLAUDE.md` is **broken in practice**:

1. **`patch_master_css.py` is stale.** Its embedded `MASTER_CSS` string is missing
   ~7,000 lines of CSS that the live guides already ship (e.g. `.calc-cards-wrap`
   and other newer components). Running it as intended (`python3 patch_master_css.py`)
   **regresses the whole site** — in testing it produced **222 files changed,
   −7,038 deletions**, stripping live styles.
2. **The deployed CSS has fragmented.** The first `<style>` block is **no longer
   uniform** across guides — there are **42 distinct variants across 224 guides**.
   There is no longer one "master" block to re-sync the script to.

Because of this, the documented workflow (edit the `MASTER_CSS` string → re-run the
script to propagate) is currently **unsafe**. Any global CSS change must, for now,
be applied **additively and surgically** (see "Interim safe pattern" below) until
the pipeline is remediated.

---

## Evidence

### 1. The script is behind the deployed CSS

| Check | Result |
|---|---|
| `.calc-cards-wrap` in `patch_master_css.py` `MASTER_CSS` | **0 occurrences** |
| `.calc-cards-wrap` in committed `guides/anemia-management.html` | **2 occurrences** |
| Full dry-run of `patch_master_css.py` | **222 files would change** |
| Net effect of a real run (guides only) | **+26,739 / −7,038 lines** |

A "no-op" master-CSS re-apply should produce ~zero changes. Instead it deletes
thousands of lines — proof the script's `MASTER_CSS` predates the CSS now live.

### 2. The deployed CSS is fragmented (42 variants)

Hashing the first `<style>…</style>` block of every guide:

```
distinct first-<style> blocks across 224 guides: 42
   97 files  cdb0b1f0…  e.g. dialysis-access-care.html
   51 files  d0992085…  e.g. calc-urine-anion-gap.html
   25 files  0263da12…  e.g. understanding-ckd.html
    8 files  f7bff55d…  e.g. calc-vasopressor-inotrope.html
    6 files  25cd44c0…  e.g. esa-dose-cancer-risk.html
    1 file   2891eda9…  e.g. calc-hf-staging.html
   … (42 groups total)
```

If the master CSS were truly centralized, this number would be **1** (or a small
handful for intentional sub-themes like calculators). 42 indicates drift —
guides have been edited directly and/or partial updates were applied to subsets.

### How this likely happened

- Direct per-guide `<style>` edits that were never folded back into the script.
- New components (calc cards, etc.) added to live guides but not to `MASTER_CSS`.
- Partial/scoped rollouts that touched some guides but not all.
- `CLAUDE.md` says "do not edit CSS directly in guide files," but enforcement is
  manual, so drift accumulated silently.

---

## Why a naive fix is dangerous

- **Running `patch_master_css.py` now** overwrites every guide's first `<style>`
  block with the stale string → mass regression (loss of calc cards and other
  newer styling on 200+ pages).
- **Re-syncing the script to "the" deployed CSS** is not possible as-is, because
  there isn't one deployed version — there are 42. Picking any single variant as
  the new master would regress the other 41 groups.

---

## Interim safe pattern (what was used for the indent fix)

Until the pipeline is fixed, apply global CSS changes **additively**, never by
rewriting the whole block:

1. Pick a **stable anchor** that exists in every target file
   (e.g. `.section p:last-child { margin-bottom: 0; }` — present in 222/224 guides).
2. Insert only the **new rule** immediately after the anchor.
3. Make it **idempotent** with a unique marker comment (skip files that already
   contain it).
4. Verify the batch diff is **additive only** (`git diff --numstat` → deletions = 0).

This was used to ship the "increase bullet indent" change: **222 files, +1,332
insertions, 0 deletions**, no regressions. It does not fix the drift, but it lets
you make safe global tweaks in the meantime. Downside: it widens drift slightly
(one more rule the script doesn't know about), so it is a stopgap, not a cure.

---

## Recommended remediation

Pick **Option A** (recommended) or **Option B** depending on appetite.

### Option A — Re-baseline the master, then keep it authoritative (recommended)

1. **Choose the canonical CSS.** Diff the 42 variants and assemble the superset of
   *intended* current rules (most pages are covered by the top 3–4 hashes, which
   account for ~170 of 224 files — start there). Resolve conflicts deliberately.
2. **Rebuild `MASTER_CSS`** in `patch_master_css.py` from that canonical CSS
   (replace the stale string wholesale).
3. **Dry-run and inspect.** `python3 patch_master_css.py --dry-run`; review the
   diff for a handful of representative guides per variant group. Expect *small*,
   intentional diffs — anything large means the baseline is wrong.
4. **Allow legitimate sub-themes.** If calculators or a few pages genuinely need
   extra CSS, keep that in a **second `<style>` block** (the script only rewrites
   the first), so the master stays single-purpose. `CLAUDE.md` already hints at
   this ("Guide-specific CSS belongs in a second `<style>` block").
5. **Apply, verify, commit** once diffs look clean across all 42 groups.
6. **Re-assert the rule:** from then on, all shared CSS lives only in `MASTER_CSS`;
   guide-specific CSS only in second blocks.

### Option B — Retire "rewrite the whole block"; go additive-by-design

1. Stop using `patch_master_css.py` to overwrite the first `<style>` block.
2. Treat shared CSS as an **append-only ledger** of anchored, idempotent rule
   insertions (the interim pattern, formalized into a small tool).
3. Pros: never regresses existing styles; safe for partial states.
   Cons: no dedup/cleanup — the block grows and can accumulate stale/overridden
   rules over time. Best paired with periodic manual pruning.

### Option C — External stylesheet (larger refactor, best long-term)

1. Extract the canonical CSS into a single `assets/guide.css` and replace each
   guide's inline first `<style>` block with `<link rel="stylesheet" href="/assets/guide.css">`.
2. Pros: genuinely one source of truth; smaller HTML; browser-cached across pages.
   Cons: bigger one-time migration; loses the current "fully self-contained HTML"
   property; must verify no per-guide inline overrides are silently lost; check
   GitHub Pages caching/versioning (cache-bust on deploy).

---

## Guardrails to add regardless of option

- **Drift check (CI or pre-commit):** hash each guide's first `<style>` block; fail
  if more than *N* distinct hashes exist (ideally 1, allowing a known calculator
  variant). This catches re-fragmentation early.
- **Lint rule:** flag direct edits to a guide's first `<style>` block in PRs.
- **`CLAUDE.md` update:** document the second-`<style>`-block convention explicitly,
  and add "never run `patch_master_css.py` without `--dry-run` + diff review until
  re-baselined."
- **Idempotency markers:** every shared rule carries a unique comment marker so
  tools can detect presence and avoid duplicates.

---

## Suggested sequencing

1. **Now:** freeze use of `patch_master_css.py` (dry-run only); keep shipping global
   tweaks via the additive pattern.
2. **Short term:** Option A re-baseline (1–2 focused sessions; start with the top
   4 hash groups covering ~85% of pages).
3. **Add guardrails:** drift check + lint + `CLAUDE.md` update.
4. **Long term (optional):** evaluate Option C (external stylesheet) if you want to
   end inline-CSS maintenance entirely.

---

## Appendix — commands used to diagnose

```bash
# Is the script behind the live CSS?
grep -c "calc-cards-wrap" patch_master_css.py            # -> 0  (missing)
git show HEAD:guides/anemia-management.html | grep -c "calc-cards-wrap"   # -> 2 (present)
python3 patch_master_css.py --dry-run                    # -> 222 files would change

# How fragmented is the deployed CSS?
python3 - <<'PY'
import re, hashlib, glob
h={}
for f in glob.glob('guides/*.html'):
    m=re.search(r'<style>(.*?)</style>', open(f,encoding='utf-8').read(), re.DOTALL)
    if m: h.setdefault(hashlib.md5(m.group(1).encode()).hexdigest(), []).append(f)
print("distinct first-<style> blocks:", len(h))
PY

# Verify a global change is additive-only (no regression)
git diff --numstat guides/ | awk '$2>0'    # any line with deletions = a regression
```
