#!/usr/bin/env python3
"""Audit that every acronym/abbreviation is expanded on FIRST USE in the content.

Site policy (CLAUDE.md rule 13): the first time an abbreviation or acronym is
used in a guide's visible body content, it must be accompanied by what it stands
for, in parentheses — either order is accepted:

    Continuous Quality Improvement (CQI)     ← Expansion (ACRONYM)
    CQI (Continuous Quality Improvement)     ← ACRONYM (Expansion)

Subsequent uses may be the bare acronym. This mirrors audit_apa_references.py:
it is a lightweight *structural* check (does a parenthetical carrying the acronym
sit at/around its first use), not a semantic validation of the expansion text.

Scope of "content" (what is audited):
  * English text only — TL/CEB/KAP `lang-hidden` sibling spans are stripped so a
    translation is never treated as the first use.
  * The running body: `<main>` plus intro/alert callouts. Excluded as display
    chrome or non-prose: the hero <h1> title, the section nav-strip pills, the
    hero-meta byline, the Glossary accordion (it is the dictionary), the
    References accordion, the dr-card, related-guides, footer, and all
    <script>/<style>.

Acronym source (what counts as an acronym to check), per guide:
  * the guide's own Glossary "Abbreviations" list, if it has one (authoritative
    per CLAUDE.md rule 12), UNION
  * a curated global list (below) of acronyms common across the site,
  intersected with the acronyms that actually appear in that guide's content.

Usage:
    python3 audit_acronym_expansion.py                 # site summary
    python3 audit_acronym_expansion.py --details       # list every violation
    python3 audit_acronym_expansion.py --guide igan-guide.html
    python3 audit_acronym_expansion.py --report        # per-guide ratios, no exit-fail

Exits 1 if any audited guide has a first-use violation (CI-friendly), unless
--report is given.

Pure interactive tools and non-narrative pages are skipped (same set as
audit_apa_references.py / patch_symptom_widget.py).
"""
import re, sys, pathlib

GUIDES = pathlib.Path(__file__).parent / "guides"

SKIP_EXACT = {
    "index.html", "calculators.html", "ckd-dri-calculator.html",
    "symptom-checker.html", "lab-interpreter-guide.html",
    "ckd-label-scanner.html", "ckd-recipe-analyzer.html",
    "dyslipidemia-management-tool.html",
    "bp-log-blank.html", "bp-monitoring-log.html", "alcohol-drinking-log.html",
    "nephrology-atlas.html", "kidney-physiology.html",
}
SKIP_SUFFIX = ("-log.html", "-log-blank.html", "-blank.html")


def is_auditable(name):
    if name in SKIP_EXACT: return False
    if name.startswith("calc-"): return False   # calculators: mostly UI labels, audited on request
    if name.endswith(SKIP_SUFFIX): return False
    return True


# ── Curated global acronym set (detection tokens only) ─────────────────────────
# These are acronyms that recur across the site and should be spelled out on
# first use. Units (mg, dL, mL, kg, mmHg…) are intentionally NOT here. Extend as
# new acronyms enter the library.
GLOBAL_ACRONYMS = {
    # kidney / nephrology core
    "CKD","ESRD","ESKD","AKI","AKD","eGFR","CrCl","ACR","UACR","RRT","KRT",
    "CKD-MBD","RAAS","ADPKD","IgAN","FSGS","RPGN","DKD","CVD","LVH","PAD","ABI","TBI",
    # dialysis
    "HD","PD","HDF","CRRT","CVVH","CVVHD","CVVHDF","SLED","UFR","IDWG",
    "URR","nPCR","RKF","RRF","CVC","AVF","AVG","AAMI","ISO","EBCT","CFU","LAL",
    # anemia / iron / MBD labs
    "ESA","EPO","ERI","TSAT","Hgb","MCV","RBC","WBC","CBC","PTH","FGF23",
    # electrolytes / labs
    "BUN","BMP","CMP","LFT","INR","HbA1c","LDL","HDL","ALT","AST","CRP","ESR","BNP",
    "NT-proBNP","TSH","PSA","UTI",
    # infection / micro / vaccines
    "BSI","CRBSI","CLABSI","NHSN","CDC","SIR","HBV","HCV","HIV","MRSA","VRE",
    "COVID-19","HAI","PPE",
    # nutrition / body comp
    "BMI","BCM","NRI","SGA","PEW","BIA","DRI","RDA",
    # cardiology / emergencies
    "ACLS","BLS","CPR","ECG","EKG","ACS","CHF","ROSC","SCD","IDH",
    # measures / QI / stats
    "QAPI","QA","CQI","TQM","PDSA","PDCA","FOCUS-PDCA","DMAIC","SPC","RCA","FMEA",
    "RPN","VSM","PIP","KPI","SMR","SHR","NNT","NNH","RCT","PROM","HRQoL","KDQOL",
    "DSI","IPOS","ICH-CAHPS","QoL",
    # guidelines / orgs / regulatory
    "KDIGO","KDOQI","NKF","ISPD","ASN","PSN","DOH","LTO","PRDR","REDCOP",
    "PhilHealth","PHIC","CMS","CfC","CFR","FDA","WHO","AHA","ADA",
    "IRR","POD","UOM","DCH","PWD","HMO","DRG",
    # imaging / procedures
    "CT","MRI","MRA","DSA","PTA",
    # meds / conditions
    "NSAID","ACEi","ARB","ARNI","SGLT2","SGLT2i","GLP-1","MRA","T2DM","T1DM",
    "SLE","OSA","ICU","ADL","IADL",
}

# Ubiquitous or symbol/formula tokens where a parenthetical on first use adds
# noise rather than clarity: element symbols, dialysis-dose notation, and a few
# near-universal abbreviations. These are never flagged.
EXEMPT = {
    "IV","PO","SC","IM","US","OR","ER","GI","BP","DM","CV","MI","AF","RR","HR","CI",
    "RA","EO","UA","AG","TB","CNS","LOS",
    "Na","K","Cl","Ca","PO4","Mg","HCO3","A1c",
    "Kt/V","spKt/V","eKt/V","wKt/V",   # formula notation, not an initialism
}


ABBR_DT_RE = re.compile(r'<dt[^>]*>\s*([A-Za-z0-9][A-Za-z0-9/\-\.–‑ ]{0,18}?)\s*</dt>')


def strip_lang_hidden(html):
    """Remove TL/CEB/KAP spans so only English is considered first-use."""
    return re.sub(
        r'<span[^>]*\bclass="[^"]*lang-hidden[^"]*"[^>]*>.*?</span>',
        ' ', html, flags=re.DOTALL)


def content_region(html):
    """Return the English body-content HTML to audit (chrome/glossary/refs removed)."""
    html = strip_lang_hidden(html)
    # cut the head
    b = html.find('<body')
    if b != -1:
        html = html[b:]
    # remove scripts/styles
    html = re.sub(r'<script\b.*?</script>', ' ', html, flags=re.DOTALL)
    html = re.sub(r'<style\b.*?</style>', ' ', html, flags=re.DOTALL)
    # remove chrome / non-prose blocks
    html = re.sub(r'<h1\b.*?</h1>', ' ', html, flags=re.DOTALL)
    html = re.sub(r'<nav class="nav-strip[^"]*"[^>]*>.*?</nav>', ' ', html, flags=re.DOTALL)
    html = re.sub(r'<div class="hero-meta[^"]*"[^>]*>.*?</div>', ' ', html, flags=re.DOTALL)
    html = re.sub(r'<p class="hero-sub[^"]*"[^>]*>.*?</p>', ' ', html, flags=re.DOTALL)  # subtitle is chrome
    # glossary + references + tail
    for marker in ('<!-- GLOSSARY-START -->', '<!-- REFERENCES-ACC-START -->',
                   '<!-- DR CARD -->', '<div class="dr-card-wrap"',
                   '<!-- RELATED-GUIDES-START -->', '<footer'):
        i = html.find(marker)
        if i != -1:
            html = html[:i]
    # Section headings are labels, not prose — an acronym in a heading is expanded
    # in the following body text. Drop heading text so first-use is judged on prose.
    html = re.sub(r'<h[2-4]\b.*?</h[2-4]>', ' ', html, flags=re.DOTALL)
    html = re.sub(r'<div class="section-tag[^"]*"[^>]*>.*?</div>', ' ', html, flags=re.DOTALL)
    return html


def to_text(html):
    t = re.sub(r'<sup>.*?</sup>', ' ', html, flags=re.DOTALL)   # drop citation markers
    t = re.sub(r'<[^>]+>', ' ', t)
    t = (t.replace('&amp;', '&').replace('&ndash;', '-').replace('&mdash;', '-')
           .replace('&nbsp;', ' ').replace('&sect;', '#').replace('&ge;', '>=')
           .replace('&le;', '<=').replace('&lt;', '<').replace('&gt;', '>'))
    return re.sub(r'\s+', ' ', t)


def guide_glossary_acronyms(html):
    """Acronyms listed in the guide's Glossary 'Abbreviations' <dl>, if present."""
    g = re.search(r'<!-- GLOSSARY-START -->(.*?)<!-- GLOSSARY-END -->', html, re.DOTALL)
    if not g:
        return set()
    block = g.group(1)
    # Abbreviations dl is the first <dl> after the "Abbreviations" heading
    m = re.search(r'Abbreviations</h4>(.*?)(?:<h4|$)', block, re.DOTALL)
    seg = m.group(1) if m else block
    out = set()
    for dt in ABBR_DT_RE.findall(seg):
        dt = dt.strip()
        if dt in EXEMPT:            # e.g. "Kt/V" — do not split into Kt + V
            continue
        # split "AVF / AVG", "HBV/HCV", "Hb / Hgb" into individual tokens too
        for tok in re.split(r'\s*/\s*', dt):
            tok = tok.strip()
            # keep only real initialisms: >=2 chars, at least one capital, and not a
            # formula/element token that would be split nonsensically (Kt, V, PO4…)
            if len(tok) >= 2 and re.search(r'[A-Z]', tok) and tok not in EXEMPT:
                out.add(tok)
    return out


def first_use_expanded(text, acro):
    """True if `acro`'s first appearance in text carries a parenthetical either order."""
    tok = re.escape(acro)
    # Match the acronym as a token, allowing a plural 's' (CVCs, KPIs, PIPs) — the
    # negative lookbehind still anchors the start so "SCr" won't match "SC".
    m = re.search(r'(?<![A-Za-z0-9])' + tok + r's?(?![A-Za-z0-9])', text)
    if not m:
        return None  # not present in content
    i, j = m.start(), m.end()
    # (a) "ACRO (…)" — a parenthetical opens right after the acronym, possibly past
    # a suffix like "-36" (KDQOL-36) or "/AVG" (AVF/AVG) or a plural already consumed.
    if re.match(r'(?:[-–/][A-Za-z0-9.]+)*\s*\(', text[j:j + 40]):
        return True
    # (b) "Expansion (ACRO)" / "(… ACRO …)" — the acronym sits INSIDE a parenthetical.
    # Detect by walking a window on each side: an unmatched '(' before it and the
    # next ')' after it not preceded by a new '('.
    seg_before = text[max(0, i - 160):i]
    seg_after = text[j:j + 160]
    open_before = seg_before.rfind('(') > seg_before.rfind(')')
    nxt_close = seg_after.find(')')
    nxt_open = seg_after.find('(')
    close_after = nxt_close != -1 and (nxt_open == -1 or nxt_close < nxt_open)
    if open_before and close_after:
        return True
    return False


def audit_guide(path):
    html = path.read_text(encoding='utf-8')
    region = content_region(html)
    text = to_text(region)
    acros = (GLOBAL_ACRONYMS | guide_glossary_acronyms(html)) - EXEMPT
    present, violations = [], []
    for a in sorted(acros, key=lambda s: (-len(s), s)):
        r = first_use_expanded(text, a)
        if r is None:
            continue
        present.append(a)
        if not r:
            m = re.search(r'(?<![A-Za-z0-9])' + re.escape(a) + r's?(?![A-Za-z0-9])', text)
            ctx = text[max(0, m.start() - 45):m.start() + len(a) + 20].strip() if m else ''
            violations.append((a, ctx))
    return present, violations


def main():
    details = '--details' in sys.argv
    report = '--report' in sys.argv
    only = None
    for i, a in enumerate(sys.argv):
        if a == '--guide' and i + 1 < len(sys.argv):
            only = sys.argv[i + 1].replace('.html', '') + '.html'

    targets = [GUIDES / only] if only else sorted(GUIDES.glob('*.html'))
    clean, dirty, total_v, examined = [], [], 0, 0
    for p in targets:
        if not is_auditable(p.name):
            continue
        examined += 1
        present, violations = audit_guide(p)
        if not present:
            continue
        if violations:
            dirty.append((p.name, len(present), violations))
            total_v += len(violations)
            if details or only:
                print(f"\n✗ {p.name}  ({len(present)-len(violations)}/{len(present)} expanded on first use)")
                for a, ctx in violations:
                    print(f"    {a:12} …{ctx}…")
        else:
            clean.append((p.name, len(present)))
            if only:
                print(f"✓ {p.name}: {len(present)}/{len(present)} acronyms expanded on first use")

    print("\n=== Acronym first-use expansion audit ===")
    print(f"Examined:            {examined} guides")
    print(f"Fully compliant:     {len(clean)}")
    print(f"With violations:     {len(dirty)}")
    print(f"Total violations:    {total_v}")
    if dirty and not details and not only:
        worst = sorted(dirty, key=lambda x: -len(x[2]))[:15]
        print("\nMost violations (top 15) — run --details or --guide <f> to see them:")
        for name, n, v in worst:
            print(f"  {len(v):3} {name}")

    if not report and not only and total_v:
        sys.exit(1)


if __name__ == '__main__':
    main()
