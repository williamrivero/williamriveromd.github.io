#!/usr/bin/env python3
"""Apply the Renal Care Academy taxonomy to every academy page (idempotent).

One source of truth for how the Academy is organized (set by Dr. Rivero, Nov 2026):

  Nephrology Nursing Track      By Specialization: Hemodialysis Nurse, Peritoneal Dialysis Nurse, Kidney Transplant Nurse
                                By Role: Head Nurse, Charge Nurse
  Renal Care Physicians Track   Dialysis Clinical Head, Attending Nephrologist, Physician-on-Duty
  Renal Technicians Track       Dialysis Technician, Water Treatment Technician, Biomedical Equipment Technician
  Ancillary Staff Track         Renal Dietitian, Medical Records Officer/Custodian, Dialysis Unit Support Staff
  Administrative Staff Track    Unit Operations Manager/Unit Manager, PhilHealth Liaison/Claims Officer

For each page it sets: the hero tag ("<Group> Track · <By ...> · Module n of N"), the breadcrumb
(Renal Care Academy › <Group> Track › <By ...> › <Track> › ...), the track name in <title>/og/twitter titles
and image alt text, and the course-home H1. Page slugs never change.

tools/academy/publish_academy.py runs this after every generator run, so a rebuild keeps the taxonomy.

    python3 tools/academy/apply_taxonomy.py [--dry-run]
"""
import re, sys, importlib.util
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
DRY = "--dry-run" in sys.argv
_q = importlib.util.spec_from_file_location("acad_qual", Path(__file__).with_name("qualifications.py"))
Q = importlib.util.module_from_spec(_q); _q.loader.exec_module(Q)
QSTART, QEND = "<!-- ACAD-QUAL-START -->", "<!-- ACAD-QUAL-END -->"


def qual_box(slug):
    role, items = Q.QUAL[slug]
    lis = "".join(f"<li>{i}</li>" for i in items)
    return (f'{QSTART}\n<section class="section" id="qualifications">\n  <div class="section-tag">Philippine requirements</div>\n'
            f'  <h2>Who can hold this role</h2>\n  <div class="alert alert-teal"><div class="alert-icon">📋</div><div class="alert-body">'
            f'<h4>{role}: qualifications at a glance</h4><ul class="acad-qual">{lis}</ul>'
            f'<p class="q-note">{Q.SOURCES} The full table for every role is on the <a href="./#qualifications">Academy home</a>.</p></div></div>\n'
            f'<style>.acad-qual{{margin:6px 0 8px;padding-left:20px;}}.acad-qual li{{margin:4px 0;}}.q-src{{display:inline-block;margin-left:4px;padding:0 6px;border-radius:999px;font-size:11px;font-weight:700;letter-spacing:.03em;color:var(--teal);border:1px solid var(--border);}}.q-note{{font-size:12.5px;color:var(--text-muted);}}</style>\n</section>\n{QEND}\n')

GROUPS = {
    "nursing":        ("Nephrology Nursing Track", "track-nursing"),
    "physicians":     ("Renal Care Physicians Track", "track-physicians"),
    "technicians":    ("Renal Technicians Track", "renal-technician-program"),
    "ancillary":      ("Ancillary Staff Track", "track-ancillary"),
    "administrative": ("Administrative Staff Track", "track-administrative"),
}
SUBS = {"spec": ("By Specialization", "nursing-specialization"), "role": ("By Role", "nursing-role")}

# slug: group, sub, name, H1, [old full names], [(old short, new short)]
TRACKS = {
    "nephrology-nursing": ("nursing", "spec", "Hemodialysis Nurse", "Hemodialysis <em>Nurse</em>",
                           ["Nephrology Nursing &amp; Hemodialysis", "Nephrology Nursing & Hemodialysis"], [("Nephrology Nursing Module", "Hemodialysis Nurse Module")]),
    "peritoneal-dialysis-nurse": ("nursing", "spec", "Peritoneal Dialysis Nurse", "Peritoneal Dialysis <em>Nurse</em>", [], []),
    "transplant-nurse": ("nursing", "spec", "Kidney Transplant Nurse", "Kidney Transplant <em>Nurse</em>",
                         ["Transplant Nurse"], [("Transplant Nurse Module", "Kidney Transplant Nurse Module")]),
    "dialysis-head-nurse": ("nursing", "role", "Head Nurse", "Head <em>Nurse</em>", ["Dialysis Head Nurse"], []),
    "special-dialysis-nurse-roles": ("nursing", "role", "Special Dialysis Nurse Roles", "Special Dialysis <em>Nurse Roles</em>", [], []),
    "dialysis-charge-nurse": ("nursing", "role", "Charge Nurse", "Charge <em>Nurse</em>", ["Dialysis Charge Nurse"], []),
    "dialyzer-reprocessing-technician": ("technicians", None, "Dialyzer Reprocessing Technician", "Dialyzer Reprocessing <em>Technician</em>", [], []),
    "dialysis-clinical-head": ("physicians", None, "Dialysis Clinical Head", "Dialysis <em>Clinical Head</em>", [], []),
    "attending-nephrologist": ("physicians", None, "Attending Nephrologist", "Attending <em>Nephrologist</em>", [], []),
    "physician-on-duty": ("physicians", None, "Physician-on-Duty", "Physician-on-<em>Duty</em>",
                          ["Physician on Duty in the Dialysis Unit"], [("Physician on Duty Module", "Physician-on-Duty Module")]),
    "hemodialysis-technician": ("technicians", None, "Dialysis Technician", "Dialysis <em>Technician</em>", [], []),
    "water-treatment-technician": ("technicians", None, "Water Treatment Technician", "Water Treatment <em>Technician</em>",
                                   ["Water Treatment System Technician"], []),
    "dialysis-biomedical-technician": ("technicians", None, "Biomedical Equipment Technician", "Biomedical Equipment <em>Technician</em>",
                                       ["Hemodialysis Center Biomedical Technician"], [("Dialysis Biomedical Technician Module", "Biomedical Equipment Technician Module")]),
    "renal-dietitian": ("ancillary", None, "Renal Dietitian", "Renal <em>Dietitian</em>", [], []),
    "medical-records-officer": ("ancillary", None, "Medical Records Officer/Custodian", "Medical Records <em>Officer/Custodian</em>",
                                ["Medical Records Officer and Custodian"], [("Records Officer Module", "Medical Records Officer Module")]),
    "dialysis-unit-support-staff": ("ancillary", None, "Dialysis Unit Support Staff", "Dialysis Unit <em>Support Staff</em>",
                                    [], [("Dialysis Support Staff Module", "Dialysis Unit Support Staff Module")]),
    "dialysis-unit-manager": ("administrative", None, "Unit Operations Manager/Unit Manager", "Unit Operations Manager/<em>Unit Manager</em>",
                              ["Dialysis Unit Operations Manager"], []),
    "philhealth-claims": ("administrative", None, "PhilHealth Liaison/Claims Officer", "PhilHealth Liaison/<em>Claims Officer</em>",
                          ["PhilHealth Liaison, Claims Officer and Clerk"], []),
}
# hero-tag prefixes any generator may emit (old and new), longest first
OLD_TAGS = sorted([
    "Renal Care Academy &middot; Nephrology Nursing &middot; Specialty subtrack", "Renal Care Academy &middot; Transplant Nurse",
    "Nursing Education", "Nursing Specialty", "Nursing Leadership", "Physician Leadership", "Physician Practice", "Physician Education",
    "Renal Technician Program", "Dietitian Education", "Health Information", "Unit Operations", "Claims &amp; Coverage",
    "Nephrology Nursing &middot; Specialization", "Nephrology Nursing &middot; Role", "Renal Care Physicians", "Renal Technicians",
    "Ancillary Staff", "Administrative Staff", "Nephrology Nursing &middot; Support Staff",
    "Nephrology Nursing Track &middot; By Specialization", "Nephrology Nursing Track &middot; By Role", "Renal Care Physicians Track",
    "Renal Technicians Track", "Ancillary Staff Track", "Administrative Staff Track"], key=len, reverse=True)


def track_of(name):
    for slug in sorted(TRACKS, key=len, reverse=True):
        if name == slug + ".html" or name.startswith(slug + "-"):
            return slug
    return None


def tag_for(slug):
    g, sub = TRACKS[slug][0], TRACKS[slug][1]
    return GROUPS[g][0] + (f" &middot; {SUBS[sub][0]}" if sub else "")


def crumbs(slug):
    g, sub, name = TRACKS[slug][:3]
    out = ['<a href="./">Renal Care Academy</a>', f'<a class="nc-group" href="./#{GROUPS[g][1]}">{GROUPS[g][0]}</a>']
    if sub:
        out.append(f'<a class="nc-group" href="./#{SUBS[sub][1]}">{SUBS[sub][0]}</a>')
    return out, name


SEP = '<span class="nc-sep">›</span>'
CHAIN = re.compile(r'<a href="\./">Renal Care Academy</a>(?:\s*<span class="nc-sep">›</span>\s*<a (?:class="nc-group" )?href="[^"]*">[^<]*</a>)*(?:\s*<span class="nc-sep">›</span>\s*<span class="nc-cur">[^<]*</span>)?')


def apply(name, s):
    slug = track_of(name)
    if not slug:
        return s
    g, sub, new, h1, olds, shorts = TRACKS[slug]
    hub = name == slug + ".html"
    # hero tag
    def fix_tag(m):
        t = m.group(2)
        for a in OLD_TAGS:
            if t == a or t.startswith(a + " &middot; "):
                return m.group(1) + tag_for(slug) + t[len(a):] + m.group(3)
        return m.group(0)
    s = re.sub(r'(<div class="hero-tag">)([^<]*)(</div>)', fix_tag, s, count=1)
    # breadcrumb
    bar = s.find('class="nc-bar"')
    if bar >= 0:
        m = CHAIN.search(s, bar)
        if m and m.start() - bar < 200:
            parts, nm = crumbs(slug)
            chain = SEP.join(parts) + SEP + (f'<span class="nc-cur">{nm}</span>' if hub else f'<a href="{slug}.html">{nm}</a>')
            rest = s[m.end():]
            if hub:   # drop the old "current page" crumb some generators emit right after the chain
                rest = re.sub(r'^\s*<span class="nc-sep">›</span>\s*<span>([^<]*)</span>',
                              lambda r: "" if r.group(1) in [nm] + olds + [o.replace("&amp;", "&") for o in olds] else r.group(0), rest, count=1)
            s = s[:m.start()] + chain + rest
    # track name in titles, social titles, image alt, JSON-LD names
    head, sep_, body = s.partition("</head>")
    for old in olds:
        rx = r'(?<![A-Za-z])' + re.escape(old) + r'(?=:| ·| &middot;|"|<| End| Trainer)'
        if old == "Transplant Nurse":
            rx = r'(?<!Kidney )' + rx
        head = re.sub(rx, new, head)
    for a, b in shorts:
        guard = f"(?<!{re.escape(b[:-len(a)])})" if b.endswith(a) and b != a else ""
        head = re.sub(guard + r'(?<![A-Za-z])' + re.escape(a), b, head)
    s = head + sep_ + body
    if hub:
        s = re.sub(r'<h1>.*?</h1>', f'<h1>{h1}</h1>', s, count=1, flags=re.S)
        s = re.sub(re.escape(QSTART) + r".*?" + re.escape(QEND) + r"\n?", "", s, flags=re.S)
        i = s.find('<section class="section"', s.find("<main"))
        i = s.find('<section class="section"', i + 10) if i > 0 else i   # after the opening section
        if i > 0 and slug in Q.QUAL:
            s = s[:i] + qual_box(slug) + s[i:]
    return s


def main():
    changed = 0
    for p in sorted(ACADEMY.glob("*.html")):
        if p.name == "index.html":
            continue
        s = p.read_text(encoding="utf-8")
        t = apply(p.name, s)
        if t != s:
            changed += 1
            if not DRY:
                p.write_text(t, encoding="utf-8")
    print(("would update " if DRY else "taxonomy applied to ") + f"{changed} academy page(s)")


if __name__ == "__main__":
    main()
