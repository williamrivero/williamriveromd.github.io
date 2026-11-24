#!/usr/bin/env python3
"""Add an opt-in safety-critical rule to assets/nursing-course.js (idempotent).

  data-critical="1" on a question fieldset marks it safety-critical;
  data-critical-pass on the form means a pass also needs every safety-critical question answered correctly.
Used by the Special Dialysis Nurse Roles end-of-course check. Pages without these attributes behave exactly as before."""
from pathlib import Path
p = Path(__file__).resolve().parents[2] / "assets" / "nursing-course.js"
s = p.read_text(encoding="utf-8")
if "data-critical-pass" in s:
    print("nursing-course.js already has the critical-item rule"); raise SystemExit
old1 = "      var score = 0;\n      questions.forEach(function (q) {\n        var chosen = q.querySelector('input:checked');\n        var right = chosen.getAttribute('data-correct') === '1';\n        if (right) score++;\n"
new1 = "      var score = 0, critMissed = 0;\n      questions.forEach(function (q) {\n        var chosen = q.querySelector('input:checked');\n        var right = chosen.getAttribute('data-correct') === '1';\n        if (right) score++;\n        else if (q.getAttribute('data-critical') === '1') critMissed++;\n"
assert old1 in s, "score anchor not found"
s = s.replace(old1, new1, 1)
old2 = "        var passed = score >= passMark;\n        line.textContent = passed\n"
new2 = """        var passed = score >= passMark;
        if (form.hasAttribute('data-critical-pass') && critMissed > 0) {
          passed = false;
          line.textContent = 'Not yet passed (' + score + ' of ' + total + '), because ' + critMissed + (critMissed === 1 ? ' safety-critical question was' : ' safety-critical questions were') +
            ' missed. A safety-critical answer must be right even when the total is high. Review that module, then try a new set.';
        } else
        line.textContent = passed
"""
assert old2 in s, "pass anchor not found"
s = s.replace(old2, new2, 1)
p.write_text(s, encoding="utf-8")
print("patched nursing-course.js (data-critical-pass)")
