"""Color-code the Academy landing hero tiles by track family (Dr. Rivero, Nov 25 2026). Idempotent.

Each hero tile (<a class="acad-track"> in academy/index.html) gets data-family="nursing|physicians|technicians|
ancillary|administrative", read from the landing page's own Tracks section (the h3 family headings and the track
cards under each), so a new track picks up its family's color without editing this file. Tiles the section does not
list (the nursing subtracks: peritoneal dialysis, transplant, nurse assistant, ...) fall back to FALLBACK, then to
nursing. Colors are the share-card palette in build_academy_og.py (GROUP), with lighter tints in Dim/Dark.
The tiles are regrouped into one column per family (Dr. Rivero, Nov 25 2026: "5 columns, each column a track"),
each headed by the family name; on tablets and phones the families stack, tiles two to a row. Runs after every publish (publish_academy.py).

    python3 tools/academy/apply_track_colors.py
"""
import re
from pathlib import Path

PAGE = Path(__file__).resolve().parents[2] / "academy" / "index.html"

FAMILIES = [  # key, heading word to match in the Tracks section, column heading
    ("nursing", "nursing", "Nursing"),
    ("physicians", "physician", "Physicians"),
    ("technicians", "technician", "Technicians"),
    ("ancillary", "ancillary", "Ancillary staff"),
    ("administrative", "administrative", "Administrative"),
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
.acad-tracks.acad-cols{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px;align-items:start;}
.acad-col{display:flex;flex-direction:column;gap:8px;min-width:0;}
.acad-col[data-family="nursing"]{--fam:#1a6b72;}
.acad-col[data-family="physicians"]{--fam:#1f3864;}
.acad-col[data-family="technicians"]{--fam:#c55a11;}
.acad-col[data-family="ancillary"]{--fam:#2e6b3e;}
.acad-col[data-family="administrative"]{--fam:#4b3280;}
.acad-col-h{display:flex;align-items:baseline;justify-content:space-between;gap:6px;margin:0 0 2px;padding:0 2px 6px;
  border-bottom:3px solid var(--fam);font:700 .74rem/1.2 Inter,system-ui,sans-serif;letter-spacing:.07em;text-transform:uppercase;color:#17312e;}
.acad-col-h small{font-weight:600;letter-spacing:0;color:#3d635e;}
.acad-col{gap:6px;}
.acad-col-h{font-size:.68rem;letter-spacing:.05em;}
.acad-cols .acad-track{padding:8px 9px;gap:0;border-radius:10px;position:relative;overflow:hidden;}
.acad-cols .acad-track-t{position:relative;z-index:1;}
.acad-cols .acad-track[data-family] .acad-track-ico{position:absolute;right:-8px;bottom:-10px;width:52px;height:52px;margin:0;padding:0;background:none;box-shadow:none;border-radius:0;color:var(--fam);opacity:.16;pointer-events:none;z-index:0;}
.acad-cols .acad-track[data-family] .acad-track-ico svg{width:100%;height:100%;stroke:currentColor;stroke-width:1.6;fill:none;}
.acad-cols .acad-track-t strong{font-size:.8rem;line-height:1.25;overflow-wrap:break-word;hyphens:manual;}
.acad-cols .acad-track-t small{font-size:.7rem;}
@media (min-width:901px){.acad-tracks.acad-cols{max-width:660px;gap:8px;}
  .acad-col-h{font-size:.6rem;letter-spacing:.04em;}
  .acad-cols .acad-track{padding:7px 8px;}
  .acad-cols .acad-track-t strong{font-size:.72rem;line-height:1.22;}
  .acad-cols .acad-track-t small{font-size:.63rem;}
  .acad-cols .acad-track[data-family] .acad-track-ico{width:42px;height:42px;right:-6px;bottom:-8px;}}
@media (max-width:900px){.acad-tracks.acad-cols{grid-template-columns:1fr;gap:16px;}
  .acad-col{display:grid;grid-template-columns:1fr 1fr;gap:8px;}.acad-col-h{grid-column:1/-1;}}
html[data-theme="dark"] .acad-track[data-family]{background:color-mix(in srgb,var(--fam) 16%,transparent);box-shadow:inset 0 3px 0 var(--fam);}
html[data-theme="dark"] .acad-track[data-family]:hover{background:color-mix(in srgb,var(--fam) 26%,transparent);box-shadow:inset 0 3px 0 var(--fam);}
html[data-theme="dark"] [data-family="nursing"]{--fam:#3fb0a9;}
html[data-theme="dark"] [data-family="physicians"]{--fam:#7d9be0;}
html[data-theme="dark"] [data-family="technicians"]{--fam:#f08a4b;}
html[data-theme="dark"] [data-family="ancillary"]{--fam:#5fbf7a;}
html[data-theme="dark"] [data-family="administrative"]{--fam:#a48bdc;}
html[data-theme="dark"] .acad-track[data-family] .acad-track-ico{background:color-mix(in srgb,var(--fam) 55%,#0b1a24);}
html[data-theme="dark"] .acad-cols .acad-track[data-family] .acad-track-ico{background:none;color:color-mix(in srgb,var(--fam) 60%,#fff);opacity:.2;}
html[data-theme="dark"] .acad-col-h{color:#eef7f4;}
html[data-theme="dark"] .acad-col-h small{color:rgba(232,246,241,.74);}
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
    # let long "A/B" titles break at the slash in narrow columns
    s = re.sub(r'(<span class="acad-track-t"><strong>)(.*?)(</strong>)',
               lambda m: m.group(1) + re.sub(r"/(?!<wbr>)", "/<wbr>", m.group(2)) + m.group(3), s)
    def columns(m):
        tiles = re.findall(r'<a class="acad-track[^"]*"[^>]*>.*?</a>', m.group(2), re.S)
        cols = []
        for k, _, lab in FAMILIES:
            mine = [t for t in tiles if f'data-family="{k}"' in t]
            if mine:
                cols.append(f'      <div class="acad-col" data-family="{k}"><div class="acad-col-h">{lab}<small>{len(mine)}</small></div>\n'
                            + "\n".join("        " + t for t in mine) + "\n      </div>")
        rest = [t for t in tiles if "data-family=" not in t]   # untagged tiles keep their place at the end
        body = "\n".join(cols + ["      " + t for t in rest])
        return f'<nav class="acad-tracks acad-cols"{m.group(1)}>\n{body}\n    </nav>'

    s = re.sub(r'<nav class="acad-tracks[^"]*"([^>]*)>(.*?)</nav>', columns, s, count=1, flags=re.S)
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
