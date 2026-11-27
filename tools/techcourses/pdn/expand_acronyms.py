# -*- coding: utf-8 -*-
"""First-use acronym pass for the Pediatric Dialysis Nurse pages (CLAUDE.md rule 13).

generate_tech_courses.py's auto_expand() skips an acronym when its expansion appears anywhere on the page, so the first
use in reading order (an objective, a quiz stem, a reading-list title) can stay bare. This pass asks the site's own audit
(audit_acronym_expansion.audit_guide) which acronyms fail on each published page and expands the first prose occurrence
inside <main>, exactly where the audit looks. Idempotent: a page that passes is left untouched.

Run from the repo root after every rebuild of the track:
    python3 generate_tech_courses.py --course pdn --patch
    python3 tools/techcourses/pdn/expand_acronyms.py
"""
import importlib.util
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT))
import audit_acronym_expansion as AUD  # noqa: E402


def _load(p, name):
    s = importlib.util.spec_from_file_location(name, p)
    m = importlib.util.module_from_spec(s)
    s.loader.exec_module(m)
    return m


def _abbr():
    """Expansions: shared techcourse table, nursing table and this track's table."""
    table = {}
    for p in (ROOT / "tools" / "techcourses" / "shared.py",):
        try:
            table.update(getattr(_load(p, "pdn_shared_abbr"), "ABBR", {}))
        except Exception:
            pass
    for p in sorted((ROOT / "tools" / "techcourses").glob("*/abbr.py")):
        try:
            table.update(_load(p, "abbr_" + p.parent.name).ABBR)
        except Exception:
            pass
    table.update(_load(Path(__file__).with_name("abbr.py"), "pdn_abbr").ABBR)
    extra = {"CKD": ("chronic kidney disease",), "AKI": ("acute kidney injury",), "HD": ("hemodialysis",),
             "PD": ("peritoneal dialysis",), "ICU": ("intensive care unit",), "PhilHealth": ("Philippine Health Insurance Corporation",),
             "DOH": ("Department of Health",), "PRC": ("Professional Regulation Commission",), "PSN": ("Philippine Society of Nephrology",),
             "KDIGO": ("Kidney Disease: Improving Global Outcomes",), "UF": ("ultrafiltration",), "ESA": ("erythropoiesis-stimulating agent",),
             "eGFR": ("estimated glomerular filtration rate",), "AVF": ("arteriovenous fistula",), "AVG": ("arteriovenous graft",),
             "CRRT": ("continuous kidney replacement therapy",), "ISPD": ("International Society for Peritoneal Dialysis",),
             "DOPPS": ("Dialysis Outcomes and Practice Patterns Study",), "CKD-MBD": ("CKD&ndash;mineral and bone disorder",),
             "SARC-F": ("strength, assistance, rise, climb and falls questionnaire",), "MRI": ("magnetic resonance imaging",),
             "ESRD": ("end-stage renal disease",), "CPD": ("continuing professional development",), "AO": ("Administrative Order",),
             "MET": ("metabolic equivalent of task",), "CAPD": ("continuous ambulatory peritoneal dialysis",),
             "APD": ("automated peritoneal dialysis",), "BSI": ("bloodstream infection",), "CA-BSI": ("catheter-associated bloodstream infection",),
             "HDF": ("hemodiafiltration",), "BMI": ("body mass index",), "ECG": ("electrocardiogram",), "GFR": ("glomerular filtration rate",), "BSA": ("body surface area",), "SCOPE": ("Standardizing Care to Improve Outcomes in Pediatric End-Stage Kidney Disease",)}
    for k, v in extra.items():
        table.setdefault(k, v)
    return table


SKIP_OPEN = re.compile(r"<(h[1-4]|button|summary|svg|title|script|style)\b", re.I)
SKIP_CLOSE = re.compile(r"</(h[1-4]|button|summary|svg|title|script|style)>", re.I)


def expand_first(body, tok, exp):
    pat = re.compile(r"(?<![A-Za-z0-9\-])" + re.escape(tok) + r"(?![A-Za-z0-9\-])")
    parts = re.split(r"(<[^>]+>)", body)
    depth = 0
    in_script = False
    for i, seg in enumerate(parts):
        if in_script:          # JSON inside <script> (interactive cases) holds tag-like text; ignore it
            if re.match(r"</script>", seg, re.I):
                in_script = False
                depth = max(0, depth - 1)
            continue
        if seg.startswith("<"):
            if re.match(r"<script\b", seg, re.I):
                in_script = True
                depth += 1
            elif SKIP_OPEN.match(seg):
                depth += 1
            elif SKIP_CLOSE.match(seg):
                depth = max(0, depth - 1)
            continue
        if depth:
            continue
        m = pat.search(seg)
        if m:
            parts[i] = seg[:m.start()] + f"{exp} ({tok})" + seg[m.end():]
            return "".join(parts), True
    return body, False


def fix(path, table):
    fails = AUD.audit_guide(path)[1]
    if not fails:
        return 0, []
    s = path.read_text(encoding="utf-8")
    a, b = s.find("<main"), s.find("</main>")
    if a < 0 or b < 0:
        return 0, [t for t, _ in fails]
    head, body, tail = s[:a], s[a:b], s[b:]
    done, left = 0, []
    for tok, _ in fails:
        exp = (table.get(tok) or (None,))[0]
        if not exp:
            left.append(tok)
            continue
        body, ok = expand_first(body, tok, exp)
        done += ok
        if not ok:
            left.append(tok)
    path.write_text(head + body + tail, encoding="utf-8")
    return done, left


def main():
    table = _abbr()
    pages = sorted((ROOT / "academy").glob("pediatric-dialysis-nurse*.html"))
    for _ in range(3):   # an expansion can move another acronym's first use; repeat until stable
        changed = 0
        for p in pages:
            n, _left = fix(p, table)
            changed += n
        if not changed:
            break
    bad = {p.name: [t for t, _ in AUD.audit_guide(p)[1]] for p in pages}
    bad = {k: v for k, v in bad.items() if v}
    print(f"acronym first-use: {len(pages) - len(bad)}/{len(pages)} pages pass")
    for k, v in bad.items():
        print("  still failing", k, v)


if __name__ == "__main__":
    main()
