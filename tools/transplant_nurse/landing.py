#!/usr/bin/env python3
"""Academy landing page (academy/index.html): show Transplant Nurse as a subtrack of Nephrology Nursing.
Idempotent; Python 3.9+, no other repo imports, so generate_transplant_nurse.wire_parent(),
the tech-course generator hook and reapply_after_merge.py can all call it."""
import re, sys
from pathlib import Path

START, END = "<!-- TN-SUBTRACK-START -->", "<!-- TN-SUBTRACK-END -->"
BLK = re.compile(re.escape(START) + r".*?" + re.escape(END) + r"\n?", re.S)
CARD = '    <a class="tc-branch" href="nephrology-nursing.html">'
NAV = '    <a class="acad-track" href="nephrology-nursing.html">'

OPEN = START + """
    <div class="tn-group">
<style id="tn-subtrack-css">
.tn-group{display:flex;flex-direction:column;gap:10px;min-width:0;}
.tn-group>.tc-branch{flex:1 1 auto;}
.tc-subtrack{display:flex;flex-direction:column;margin-left:22px;padding:0;border:2px solid var(--border);border-left:5px solid var(--teal);border-radius:12px;background:var(--white);color:var(--text);text-decoration:none;position:relative;}
.tc-subtrack::before{content:"";position:absolute;left:-19px;top:-12px;width:12px;height:32px;border-left:2px solid var(--border);border-bottom:2px solid var(--border);border-bottom-left-radius:8px;}
.tc-subtrack:hover,.tc-subtrack:focus-visible{border-color:var(--teal);}
.tc-subtrack-img{display:block;width:100%;height:auto;aspect-ratio:16/7;object-fit:cover;object-position:50% 35%;background:var(--bg);border-radius:7px 10px 0 0;}
@media (max-width:480px){.tc-subtrack{margin-left:16px;}}
.tc-subtrack-t{display:flex;flex-direction:column;gap:3px;min-width:0;padding:10px 14px 12px;}
.tc-subtrack small{font-size:.72rem;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);font-weight:700;}
.tc-subtrack b{font-family:Inter,system-ui,sans-serif;font-size:.98rem;}
.tc-subtrack span.tc-subtrack-d{font-size:13.5px;line-height:1.5;color:var(--text-mid);}
.tc-subtrack-go{font-weight:700;color:var(--teal);}
.acad-track.acad-subtrack{margin-left:0;border-left:4px solid #1a6b72;}
</style>
""" + END + "\n"

CLOSE = START + """
    <a class="tc-subtrack" href="transplant-nurse.html" aria-label="Transplant Nurse, a subtrack of Nephrology Nursing">
      <img class="tc-subtrack-img" src="../images/transplant-nurse-card.webp" alt="" loading="lazy" decoding="async" width="640" height="360">
      <span class="tc-subtrack-t"><small>Nephrology Nursing subtrack</small><b>Transplant Nurse <span class="tc-subtrack-go" aria-hidden="true">&rarr;</span></b><span class="tc-subtrack-d">12 modules for kidney transplant ward and clinic nurses, entered from Module 11. Referral, donation, immunosuppression, graft and infection surveillance, PhilHealth benefits, and a simulation capstone.</span></span>
    </a>
    </div>
""" + END + "\n"

NAV_ITEM = (START + "\n"
    '    <a class="acad-track acad-subtrack" href="transplant-nurse.html"><span class="acad-track-ico"><svg viewBox="0 0 24 24" aria-hidden="true">'
    '<path d="M12 21c-4-2.5-6-6-6-10a6 6 0 0 1 12 0c0 4-2 7.5-6 10z"/><path d="M12 8v6M9 11h6"/></svg></span>'
    '<span class="acad-track-t"><strong>Transplant Nurse</strong><small>12 modules</small></span></a>\n' + END + "\n")
OLD_NAV = re.compile(r'^    <a class="acad-track" href="transplant-nurse\.html">.*?</a>\n', re.M | re.S)


def wire(path):
    p = Path(path)
    s = BLK.sub("", p.read_text(encoding="utf-8"))
    s = OLD_NAV.sub("", s)
    i = s.find(CARD)
    if i < 0:
        return "anchor not found: Nephrology Nursing card"
    j = s.find("</a>", i)
    j = s.find("\n", j) + 1
    s = s[:i] + OPEN + s[i:j] + CLOSE + s[j:]
    k = s.find(NAV)
    if k >= 0:
        e = s.find("\n", s.find("</a>", k)) + 1
        s = s[:e] + NAV_ITEM + s[e:]
    p.write_text(s, encoding="utf-8")
    return "ok"


if __name__ == "__main__":
    print(wire(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).resolve().parents[2] / "academy" / "index.html"))
