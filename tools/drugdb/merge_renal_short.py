#!/usr/bin/env python3
"""
merge_renal_short.py — copy APPROVED kidney-strip text (short + level) into the renal files.

Source:  data/drugs/renal-short/<slug>.json
         {slug, review_status, reviewed_by, reviewed_date,
          items: {egfr_ge60|egfr_30_59|egfr_15_29|egfr_lt15|hd|pd|crrt|pirrt|peds_<same keys>: {short, level}}}
Target:  data/drugs/renal/<slug>.json (schema in DRUGDB-CONTRACT.md):
         bands[i].short/level; hd/pd/crrt/pirrt become {text, short, level} (text kept verbatim);
         pediatric.renal[i] and pediatric.hd/pd/crrt/pirrt likewise.

Rules
- Copies only when the renal-short file is review_status "approved" AND the renal file is "approved".
  Approved recommendation text is never edited: band "recommendation" strings and the hd/pd/crrt text are
  preserved exactly (a plain string is wrapped as {"text": <same string>, ...}).
- If a renal-short file is NOT approved (or is missing), any short/level previously merged into the renal file
  is removed again and wrapped strings are unwrapped back to plain text, so the strip never shows unapproved text.
- Bands are matched by their range text (≥60, 30–59, 15–29, <15), not by position.
- Idempotent; writes a file only when it changes. --dry-run reports without writing.

Usage:
  python3 tools/drugdb/merge_renal_short.py [--dry-run] [--only slug1,slug2] [--data-dir data/drugs]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

LEVELS = {"none", "adjust", "avoid", "nodata", "hide"}
MODALITIES = ("hd", "pd", "crrt", "pirrt")
MAX_SHORT = 40


def band_key(rng: str) -> str | None:
    r = (rng or "").replace(" ", "")
    if re.search(r"[≥>]=?60", r):
        return "egfr_ge60"
    if re.search(r"30[–-]59", r):
        return "egfr_30_59"
    if re.search(r"15[–-]29", r):
        return "egfr_15_29"
    if re.search(r"<15", r):
        return "egfr_lt15"
    return None


def text_of(v):
    return v.get("text") if isinstance(v, dict) else v


def apply(renal: dict, items: dict | None, errors: list, slug: str) -> None:
    """items=None strips previously merged fields."""
    def band_list(bands, prefix):
        for b in bands or []:
            if not isinstance(b, dict):
                continue
            k = band_key(b.get("range", ""))
            it = (items or {}).get(prefix + k) if (items is not None and k) else None
            if it:
                b["short"], b["level"] = it["short"], it["level"]
            else:
                if items is not None and k:
                    errors.append(f"{slug}: no item for {prefix}{k}")
                b.pop("short", None)
                b.pop("level", None)

    def modality(obj, prefix):
        for m in MODALITIES:
            if obj.get(m) in (None, "", []):
                continue
            it = (items or {}).get(prefix + m) if items is not None else None
            txt = text_of(obj[m])
            if it:
                obj[m] = {"text": txt, "short": it["short"], "level": it["level"]}
            else:
                if items is not None:
                    errors.append(f"{slug}: no item for {prefix}{m}")
                obj[m] = txt

    band_list(renal.get("bands"), "")
    modality(renal, "")
    ped = renal.get("pediatric")
    if isinstance(ped, dict):
        band_list(ped.get("renal"), "peds_")
        modality(ped, "peds_")
    if items is None:
        renal.pop("strip_review", None)


def validate(short: dict, slug: str, errors: list) -> bool:
    ok = True
    for k, v in (short.get("items") or {}).items():
        if not isinstance(v, dict) or v.get("level") not in LEVELS or not (v.get("short") or "").strip():
            errors.append(f"{slug}.{k}: missing short or bad level")
            ok = False
        elif len(v["short"]) > MAX_SHORT:
            errors.append(f"{slug}.{k}: short longer than {MAX_SHORT} characters")
            ok = False
    return ok


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data-dir", default="data/drugs")
    ap.add_argument("--only", default="")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args(argv)
    d = Path(a.data_dir)
    only = {s.strip() for s in a.only.split(",") if s.strip()}
    errors, changed, merged, stripped = [], [], 0, 0
    for rf in sorted((d / "renal").glob("*.json")):
        slug = rf.stem
        if slug.startswith("_") or (only and slug not in only):
            continue
        raw = rf.read_text(encoding="utf-8")
        renal = json.loads(raw)
        sf = d / "renal-short" / f"{slug}.json"
        short = json.loads(sf.read_text(encoding="utf-8")) if sf.exists() else None
        ok = (renal.get("review_status") == "approved" and isinstance(short, dict)
              and short.get("review_status") == "approved" and validate(short, slug, errors))
        if ok:
            apply(renal, short["items"], errors, slug)
            renal["strip_review"] = {"source": f"renal-short/{slug}.json",
                                     "reviewed_by": short.get("reviewed_by"), "reviewed_date": short.get("reviewed_date")}
            merged += 1
        else:
            apply(renal, None, errors, slug)
            stripped += 1
        out = json.dumps(renal, ensure_ascii=False, indent=2) + "\n"
        if out != raw and json.loads(out) != json.loads(raw):
            changed.append(slug)
            if not a.dry_run:
                rf.write_text(out, encoding="utf-8")
    print(f"merged {merged}, not approved {stripped}, files changed {len(changed)}{' (dry run)' if a.dry_run else ''}")
    for s in changed:
        print("  changed:", s)
    for e in errors:
        print("  WARN:", e, file=sys.stderr)
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
