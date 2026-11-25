#!/usr/bin/env python3
"""Idempotently apply the Dialysis Nurse Assistant / PCA registrations to shared files (taxonomy, qualifications,
publish prefixes, share-card tracks, landing re-wire hook). Safe to run on any checkout; already-present edits are skipped."""
from pathlib import Path
R = Path(__file__).resolve().parents[2]
done = []


def edit(rel, test, fn):
    p = R / rel
    s = p.read_text(encoding="utf-8")
    if test in s:
        return
    n = fn(s)
    assert n != s, f"{rel}: anchor not found"
    p.write_text(n, encoding="utf-8")
    done.append(rel)


def prefixes(s):
    i = s.index("PREFIXES = ("); j = s.index(")\n", i)
    return s[:j] + ', "dialysis-nurse-assistant"' + s[j:]


edit("tools/academy/publish_academy.py", '"dialysis-nurse-assistant"', prefixes)

A = '    "dialysis-charge-nurse": ("nursing", "role", "Charge Nurse", "Charge <em>Nurse</em>", ["Dialysis Charge Nurse"], []),\n'
edit("tools/academy/apply_taxonomy.py", '"dialysis-nurse-assistant"', lambda s: s.replace(A, A +
     '    "dialysis-nurse-assistant": ("nursing", "role", "Dialysis Nurse Assistant / Patient Care Assistant (PCA)", '
     '"Dialysis Nurse Assistant / <em>PCA</em>", ["Dialysis Nurse Assistant / PCA"], []),\n', 1))

Q = ' "dialysis-unit-support-staff": ('
edit("tools/academy/qualifications.py", '"dialysis-nurse-assistant"', lambda s: s.replace(Q,
     ' "dialysis-nurse-assistant": ("Dialysis Nurse Assistant / Patient Care Assistant (PCA)", [\n'
     '   "PSN describes nursing assistants as BS Nursing graduates awaiting registration, BS Nursing undergraduates who completed at least second year, or BS Midwifery graduates, working under supervision. <span class=q-src>PSN</span>",\n'
     '   "Not a registered nurse and not counted as one; a nursing degree without PRC registration does not authorize nursing practice. <span class=q-src>DOH, PSN</span>",\n'
     '   "No national assistant license or TESDA equivalence; scope is the employer&rsquo;s written job description plus the tasks signed off under RN supervision.",\n'
     '   "Ratio: DOH sets no more than 1 nurse to 4 stations; PSN discusses 1:6 patients when an assistant is present. Confirm with DOH licensing before relying on any exception. <span class=q-src>DOH, PSN</span>"]),\n' + Q, 1))

O = '    "physician-on-duty": ('
edit("build_academy_og.py", '"dialysis-nurse-assistant"', lambda s: s.replace(O,
     '    "dialysis-nurse-assistant": ("academy/dialysis-nurse-assistant.html", "nursing", "Dialysis Nurse Assistant / PCA",\n'
     '                                 "BY ROLE · SUPERVISED SUPPORT", "12 modules · worked scenarios · assistant toolkit"),\n' + O, 1))

H = "            print((r3.stdout or r3.stderr).strip()[-300:])\n"
edit("generate_tech_courses.py", "generate_dialysis_nurse_assistant", lambda s: s.replace(H, H +
     '        if (ROOT / "generate_dialysis_nurse_assistant.py").exists():   # keep the Dialysis Nurse Assistant / PCA landing links\n'
     '            r4 = subprocess.run([sys.executable, "-c", "import generate_dialysis_nurse_assistant as D; print(\'dialysis-nurse-assistant links:\', D.wire_parent())"], cwd=ROOT, capture_output=True, text=True)\n'
     '            print((r4.stdout or r4.stderr).strip()[-300:])\n', 1))
print("edited:", done or "nothing (already applied)")
