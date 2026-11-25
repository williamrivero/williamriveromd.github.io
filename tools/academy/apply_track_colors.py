"""Color-code the Academy landing hero tiles by track family (Dr. Rivero, Nov 25 2026). Idempotent.

Each hero tile (<a class="acad-track"> in academy/index.html) gets data-family="nursing|physicians|technicians|
ancillary|administrative", read from the landing page's own Tracks section (the h3 family headings and the track
cards under each), so a new track picks up its family's color without editing this file. Tiles the section does not
list (the nursing subtracks: peritoneal dialysis, transplant, nurse assistant, ...) fall back to FALLBACK, then to
nursing. Colors are the share-card palette in build_academy_og.py (GROUP), with lighter tints in Dim/Dark.
A legend line under the tiles names the five families. Runs after every publish (publish_academy.py).

    python3 tools/academy/apply_track_colors.py
"""
import re
from pathlib import Path

PAGE = Path(__file__).resolve().parents[2] / "academy" / "index.html"

FAMILIES = [  # key, heading word to match in the Tracks section, legend label
    ("nursing", "nursing", "Nursing"),
    ("physicians", "physician", "Physicians"),
    ("technicians", "technician", "Technicians"),
    ("ancillary", "ancillary", "Ancillary staff"),
    ("administrative", "administrative", "Administrative staff"),
]
FALLBACK = {"peritoneal-dialysis-nurse.html": "nursing", "transplant-nurse.html": "nursing",
            "dialysis-nurse-assistant.html": "nursing", "special-dialysis-nurse-roles.html": "nursing"}

CSS = """<style id="academy-track-colors">
/* Hero tiles color-coded by track family (same palette as the Academy share cards). */
.acad-track[data-family]{--fam:#1a6b72;background:color-mix(in srgb,var(--fam) 7%,#fff);box-shadow:inset 0 3px 0 var(--fam);}
.acad-track[data-family="physicians"]{--fam:#1f3864;}
.acad-track[data-family="technicians"]{--fam:#c55a11;}
.acad-track[data-family="ancillary"]{--fam:#2e6b3e;}
.acad-track[data-family="administrative"]{--fam:#4b3280;}
.acad-track[data-family] .acad-track-ico{background:var(--fam);}
.acad-track.acad-subtrack[data-family]{border-left-color:var(--fam);}
.acad-track[data-family]:hover{background:#fff;box-shadow:inset 0 3px 0 var(--fam),0 8px 22px rgba(18,58,54,.14);}
.acad-legend{display:flex;flex-wrap:wrap;gap:6px 16px;margin:12px 0 0;font-size:.8rem;color:#3d635e;}
.acad-legend span{display:inline-flex;align-items:center;gap:6px;}
.acad-legend i{width:10px;height:10px;border-radius:3px;background:var(--fam);display:inline-block;}
.acad-legend [data-family="nursing"]{--fam:#1a6b72;}
.acad-legend [data-family="physicians"]{--fam:#1f3864;}
.acad-legend [data-family="technicians"]{--fam:#c55a11;}
.acad-legend [data-family="ancillary"]{--fam:#2e6b3e;}
.acad-legend [data-family="administrative"]{--fam:#4b3280;}
html[data-theme="dark"] .acad-track[data-family]{background:color-mix(in srgb,var(--fam) 16%,transparent);box-shadow:inset 0 3px 0 var(--fam);}
html[data-theme="dark"] .acad-track[data-family]:hover{background:color-mix(in srgb,var(--fam) 26%,transparent);box-shadow:inset 0 3px 0 var(--fam);}
html[data-theme="dark"] .acad-track[data-family="nursing"],html[data-theme="dark"] .acad-legend [data-family="nursing"]{--fam:#3fb0a9;}
html[data-theme="dark"] .acad-track[data-family="physicians"],html[data-theme="dark"] .acad-legend [data-family="physicians"]{--fam:#7d9be0;}
html[data-theme="dark"] .acad-track[data-family="technicians"],html[data-theme="dark"] .acad-legend [data-family="technicians"]{--fam:#f08a4b;}
html[data-theme="dark"] .acad-track[data-family="ancillary"],html[data-theme="dark"] .acad-legend [data-family="ancillary"]{--fam:#5fbf7a;}
html[data-theme="dark"] .acad-track[data-family="administrative"],html[data-theme="dark"] .acad-legend [data-family="administrative"]{--fam:#a48bdc;}
html[data-theme="dark"] .acad-track[data-family] .acad-track-ico{background:color-mix(in srgb,var(--fam) 55%,#0b1a24);}
html[data-theme="dark"] .acad-legend{color:rgba(232,246,241,.78);}
</style>"""

STYLE_RE = re.compile(r'\n?<style id="academy-track-colors">.*?</style>', re.S)
LEGEND_RE = re.compile(r'\n?\s*<div class="acad-legend"[^>]*>.*?</div>', re.S)


def families_from_page(s):
    """href -> family, from the h3 headings and track cards in the landing page's Tracks section."""
    sec = s[s.find('id="tracks"'):] if 'id="tracks"' in s else ""
    out, cur = {}, None
    for m in re.finditer(r'<h3[^>]*>(.*?)</h3>|<a class="tc-branch[^"]*" href="([^"]+)"', sec):
        if m.group(1) is not None:
            head = re.sub(r"<[^>]+>", "", m.group(1)).lower()
            cur = next((k for k, w, _ in FAMILIES if w in head), None)
        elif cur:
            out.setdefault(m.group(2), cur)
    return out


def apply(s):
    s = STYLE_RE.sub("", s)
    s = LEGEND_RE.sub("", s)
    fam = {**FALLBACK, **families_from_page(s)}

    def tag(m):
        a = re.sub(r'\s*data-family="[^"]*"', "", m.group(0))
        href = re.search(r'href="([^"]+)"', a).group(1)
        f = fam.get(href) or ("nursing" if "acad-subtrack" in a else None)
        return a if not f else a[:-1] + f' data-family="{f}">'

    s = re.sub(r'<a class="acad-track[^"]*"[^>]*>', tag, s)
    used = [k for k, _, _ in FAMILIES if f'data-family="{k}"' in s]
    legend = ('\n    <div class="acad-legend" aria-label="Track families">'
              + "".join(f'<span data-family="{k}"><i></i>{lab}</span>' for k, _, lab in FAMILIES if k in used)
              + "</div>")
    s = re.sub(r'(<nav class="acad-tracks"[^>]*>.*?</nav>)', lambda m: m.group(1) + legend, s, count=1, flags=re.S)
    return s.replace("</head>", CSS + "\n</head>", 1)


def main():
    if not PAGE.exists():
        return
    old = PAGE.read_text(encoding="utf-8")
    new = apply(old)
    if new != old:
        PAGE.write_text(new, encoding="utf-8")
    n = len(re.findall(r'class="acad-track[^"]*"[^>]*data-family=', new))
    print(f"academy track colors: {n} hero tiles tagged" + (" (updated)" if new != old else " (unchanged)"))


if __name__ == "__main__":
    main()
