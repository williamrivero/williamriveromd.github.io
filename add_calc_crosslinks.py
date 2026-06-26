#!/usr/bin/env python3
"""
add_calc_crosslinks.py — inject a "Related Calculators" sibling block into each
calculator page, driven by a cluster map. Idempotent: the block between the
<!-- CALC-CROSSLINK-START --> / END markers is stripped and re-inserted each run,
so editing CLUSTERS and re-running refreshes every page.

The block is placed as the last child of <main> (before the closing </main>),
reusing the master-CSS .section / .related-cards / .related-card classes (which
are dark-mode-safe), so no new CSS is required.

Short labels come from guides/calculators.html (each calc's .related-card-title),
keeping cross-link labels consistent with the index. Run AFTER any new calculator
is registered in calculators.html.

Usage:
    python3 add_calc_crosslinks.py [--dry-run] [--guide calc-foo.html]
"""
import argparse
import os
import re
import sys

GUIDES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "guides")
INDEX = os.path.join(GUIDES, "calculators.html")

START = "<!-- CALC-CROSSLINK-START -->"
END = "<!-- CALC-CROSSLINK-END -->"

# Max sibling links shown per page.
CAP = 6

# Clinical clusters. A page inherits the union of siblings from every cluster it
# belongs to (deduped, self excluded, capped at CAP, in first-seen order).
CLUSTERS = {
    "renal-dosing": [
        "calc-cockcroft-gault", "calc-vancomycin-auc", "calc-aminoglycoside-dosing",
        "calc-metformin-ckd-safety", "calc-sglt2i-eligibility", "calc-qtc",
    ],
    "diabetes-ckd": [
        "calc-sglt2i-eligibility", "calc-metformin-ckd-safety", "calc-eag-hba1c",
        "calc-insulin-dose", "calc-dkd-risk",
    ],
    "dialysis-fluid": [
        "calc-dry-weight-estimator", "calc-ultrafiltration-rate", "calc-idwg-fluid",
    ],
    "hd-adequacy": [
        "calc-dialysis-adequacy-ktv", "calc-npcr", "calc-hd-adequacy-npcr",
        "calc-dialysis-prescription",
    ],
    "pd": [
        "calc-pd-adequacy", "calc-pd-glucose-absorption", "calc-dialysis-prescription",
    ],
    "stones": [
        "calc-urine-supersaturation", "calc-stone-prevention-fluid",
        "calc-stone-passage-risk",
    ],
    "nutrition-wasting": [
        "calc-sarcopenia-sarcf", "calc-frailty-assessment", "calc-nutrition-screening",
        "calc-nri", "calc-npcr", "calc-ckd-nutrition-rx",
    ],
    "mental-qol": [
        "calc-phq9", "calc-psqi", "calc-stop-bang", "calc-dialysis-prom",
    ],
    "endemic-aki": [
        "calc-leptospirosis-aki-risk", "calc-dengue-aki-risk", "calc-hfrs-severity",
        "calc-aki-staging",
    ],
    "sepsis": [
        "calc-qsofa-sofa", "calc-sirs-sepsis",
    ],
    "albuminuria": [
        "calc-uacr-trend", "calc-proteinuria-uacr", "calc-urine-protein-excretion",
        "calc-kfre",
    ],
    "ckd-mbd": [
        "calc-phosphorus-load", "calc-vitamin-d-dose", "calc-ckd-mbd",
        "calc-corrected-calcium",
    ],
    "af-anticoag": [
        "calc-cha2ds2-vasc", "calc-has-bled", "calc-af-anticoagulation",
    ],
    "cardiometabolic-risk": [
        "calc-ckm-staging", "calc-prevent-cvd", "calc-lipid-panel",
        "calc-cha2ds2-vasc", "calc-af-anticoagulation", "calc-uacr-trend",
    ],
    "function-egfr": [
        "calc-egfr-ckd-epi", "calc-egfr-cystatin", "calc-cockcroft-gault",
        "calc-measured-crcl", "calc-kfre",
    ],
    "potassium": [
        "calc-potassium-load", "calc-ttkg",
    ],
}


def load_labels():
    """Map calc-x.html -> short title from the index .related-card markup."""
    html = open(INDEX, encoding="utf-8").read()
    labels = {}
    for m in re.finditer(
        r'<a class="related-card" href="(calc-[a-z0-9-]+\.html)">\s*'
        r'(?:<div class="related-card-tag">.*?</div>\s*)?'
        r'<div class="related-card-title">(.*?)</div>',
        html, re.S,
    ):
        href, title = m.group(1), re.sub(r"\s+", " ", m.group(2)).strip()
        labels[href] = title
    return labels


def siblings_for(stem):
    """Union of siblings across every cluster containing `stem`, capped."""
    out = []
    for members in CLUSTERS.values():
        if stem in members:
            for s in members:
                if s != stem and s not in out:
                    out.append(s)
    return out[:CAP]


def build_block(stems, labels):
    cards = []
    for s in stems:
        href = s + ".html"
        label = labels.get(href)
        if not href_exists(href) or not label:
            continue
        cards.append(
            f'<a class="related-card" href="{href}">\n'
            f'<div class="related-card-tag">Calculator</div>\n'
            f'<div class="related-card-title">{label}</div>\n'
            f'</a>'
        )
    if not cards:
        return None
    return (
        f"{START}\n"
        f'<section class="section" aria-label="Related calculators" '
        f'style="border-bottom:none;padding-top:36px;">\n'
        f'<div class="section-tag">Related Calculators</div>\n'
        f'<h2 style="font-size:1.25rem;">Use this with</h2>\n'
        f'<div class="related-cards">\n' + "\n".join(cards) + "\n</div>\n"
        f"</section>\n"
        f"{END}"
    )


def href_exists(href):
    return os.path.exists(os.path.join(GUIDES, href))


def strip_existing(html):
    return re.sub(
        re.escape(START) + r".*?" + re.escape(END) + r"\s*",
        "", html, flags=re.S,
    )


def patch_file(path, labels, dry):
    stem = os.path.splitext(os.path.basename(path))[0]
    sibs = siblings_for(stem)
    if not sibs:
        return None  # not in any cluster
    html = open(path, encoding="utf-8").read()
    cleaned = strip_existing(html)
    block = build_block(sibs, labels)
    if not block:
        return None
    # Insert before the LAST </main>
    idx = cleaned.rfind("</main>")
    if idx == -1:
        return ("SKIP (no </main>)", stem)
    new = cleaned[:idx] + block + "\n" + cleaned[idx:]
    if new == html:
        return ("unchanged", stem)
    if not dry:
        open(path, "w", encoding="utf-8").write(new)
    return ("updated", stem)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--dry-run", action="store_true")
    ap.add_argument("--guide", help="single calc-*.html file")
    args = ap.parse_args()

    labels = load_labels()
    if args.guide:
        files = [os.path.join(GUIDES, args.guide)]
    else:
        files = sorted(
            os.path.join(GUIDES, f)
            for f in os.listdir(GUIDES)
            if f.startswith("calc-") and f.endswith(".html")
        )

    changed = 0
    for path in files:
        res = patch_file(path, labels, args.dry_run)
        if res is None:
            continue
        status, stem = res
        if status == "updated":
            changed += 1
            print(f"  {stem:34} -> {'[DRY] ' if args.dry_run else ''}updated "
                  f"({len(siblings_for(stem))} links)")
        elif status != "unchanged":
            print(f"  {stem:34} -> {status}")
    tag = "[DRY RUN] " if args.dry_run else ""
    print(f"\n{tag}Summary: {changed} page(s) "
          f"{'would be ' if args.dry_run else ''}changed.")


if __name__ == "__main__":
    main()
