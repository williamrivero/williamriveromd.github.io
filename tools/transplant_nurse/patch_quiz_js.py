#!/usr/bin/env python3
"""Add two opt-in features to assets/nursing-course.js (idempotent):
  data-stratify  draw one question per data-group (used by the Transplant Nurse end-of-course check)
  data-pass      show a pass / not-yet-passed line against a pass mark
Pages without these attributes behave exactly as before."""
from pathlib import Path
p = Path(__file__).resolve().parents[2] / "assets" / "nursing-course.js"
s = p.read_text(encoding="utf-8")
if "data-stratify" in s:
    print("nursing-course.js already patched"); raise SystemExit
old = "      var pick = shuffle(bank.slice()).slice(0, drawN);\n"
new = """      var pick = shuffle(bank.slice()).slice(0, drawN);
      if (form.hasAttribute('data-stratify')) {
        /* one question per data-group, groups in random order */
        var groups = {}, keys = [];
        bank.forEach(function (q) { var g = q.getAttribute('data-group') || ''; if (!groups[g]) { groups[g] = []; keys.push(g); } groups[g].push(q); });
        pick = shuffle(keys.map(function (g) { return groups[g][rand(groups[g].length)]; })).slice(0, drawN);
      }
"""
assert old in s, "draw anchor not found"
s = s.replace(old, new, 1)
old2 = "      result.appendChild(strong); result.appendChild(p);\n"
new2 = """      result.appendChild(strong); result.appendChild(p);
      var passMark = parseInt(form.getAttribute('data-pass'), 10);
      if (passMark) {
        var line = document.createElement('span');
        line.className = 'nc-verdict-line';
        var passed = score >= passMark;
        line.textContent = passed
          ? 'Passed (' + score + ' of ' + total + '; pass mark ' + passMark + '). Your self-study is complete. Simulation and workplace competency are assessed separately.'
          : 'Not yet passed (' + score + ' of ' + total + '; pass mark ' + passMark + '). Review the modules for the questions you missed, then try a new set.';
        result.classList.add(passed ? 'nc-result-pass' : 'nc-result-fail');
        result.appendChild(line);
      }
"""
assert old2 in s, "result anchor not found"
s = s.replace(old2, new2, 1)
p.write_text(s, encoding="utf-8")
print("patched nursing-course.js")
