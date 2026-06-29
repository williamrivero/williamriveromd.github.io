#!/usr/bin/env python3
"""Wire the circular vignette hero into guides whose square *-vignette-hero.png
was uploaded but not yet wired into the page.

For each target guide this wraps the existing hero `<div class="container">`
contents in `<div class="hero-grid"><div class="hero-copy"> … </div>` and appends
a `<figure class="hero-figure"><div class="hero-vignette">` holding the
`<picture>` (webp + png) right before the container closes, producing the
two-column circular hero used across the site. Idempotent: a guide whose hero
already references its `-vignette-hero` image is skipped.

Usage:
    python3 patch_vignette_hero.py [--dry-run] [--guide <file.html>]
"""
import os
import re
import sys

ROOT = os.path.dirname(os.path.abspath(__file__))
GUIDES = os.path.join(ROOT, "guides")

# guide stem -> alt text for the circular vignette
TARGETS = {
    "dialysis-prescription": "Circular vignette hero illustration for the dialysis prescription guide.",
    "glp1-ozempic-ckd": "Circular vignette hero illustration for the GLP-1 agonists and CKD guide.",
    "green-nephrology": "Circular vignette hero illustration for the green nephrology guide.",
    "hemodiafiltration-deep-dive": "Circular vignette hero illustration for the hemodiafiltration deep-dive guide.",
    "hemodialysis-modalities": "Circular vignette hero illustration for the hemodialysis modalities guide.",
    "high-flux-hd-optimization": "Circular vignette hero illustration for the high-flux hemodialysis optimization guide.",
    "innovative-technologies-ckd": "Circular vignette hero illustration for the innovative technologies in CKD guide.",
    "medication-operational-guide": "Circular vignette hero illustration for the CKD prescriber's medication operational guide.",
    "microbiome-probiotics-health": "Circular vignette hero illustration for the microbiome, probiotics, and kidney health guide.",
    "new-therapeutic-agents-ckd": "Circular vignette hero illustration for the new therapeutic agents in CKD guide.",
    "practical-outpatient-algorithms": "Circular vignette hero illustration for the practical outpatient nephrology algorithms guide.",
    "stem-cells-ckd": "Circular vignette hero illustration for the stem cells and CKD guide.",
    "acute-kidney-injury-on-ckd": "Circular vignette hero illustration for the AKI-on-CKD guide.",
    "advance-care-planning-dialysis": "Circular vignette hero illustration for the advance care planning in dialysis guide.",
    "alcohol-ckd": "Circular vignette hero illustration for the alcohol and CKD guide.",
    "buko-juice-alkaline-water-ckd": "Circular vignette hero illustration for the buko juice and alkaline water CKD guide.",
    "caffeine-ckd": "Circular vignette hero illustration for the caffeine and CKD guide.",
    "cardiovascular-death-dialysis": "Circular vignette hero illustration for the cardiovascular death in dialysis guide.",
    "ckd-financial-stress": "Circular vignette hero illustration for the CKD financial stress guide.",
    "dialysis-coming-pre-eskd": "Circular vignette hero illustration for the preparing for dialysis (pre-ESKD) guide.",
    "el-nino-heat-dialysis": "Circular vignette hero illustration for the El Niño heat and dialysis guide.",
    "hemodialysis-transfer-guide": "Circular vignette hero illustration for the hemodialysis transfer guide.",
    "hemoperfusion-blood-purification": "Circular vignette hero illustration for the hemoperfusion and blood purification guide.",
    "philhealth-z-packages": "Circular vignette hero illustration for the PhilHealth Z-packages guide.",
    "substance-abuse-ckd": "Circular vignette hero illustration for the substance abuse and CKD guide.",
    "tuberculosis-kidney-disease": "Circular vignette hero illustration for the tuberculosis and kidney disease guide.",
    "typhoon-disaster-preparedness-dialysis": "Circular vignette hero illustration for the typhoon and disaster preparedness in dialysis guide.",
    "viral-infections-vaccinations-ckd": "Circular vignette hero illustration for the viral infections and vaccinations in CKD guide.",
    "zero-balance-billing-philhealth": "Circular vignette hero illustration for the PhilHealth zero-balance-billing guide.",
}

FIGURE_TMPL = (
    '    <figure class="hero-figure">\n'
    '      <div class="hero-vignette">\n'
    '        <picture>\n'
    '          <source srcset="../images/{stem}-vignette-hero.webp" type="image/webp">\n'
    '          <img src="../images/{stem}-vignette-hero.png" alt="{alt}" width="1254" height="1254" fetchpriority="high" loading="eager" decoding="async">\n'
    '        </picture>\n'
    '      </div>\n'
    '    </figure>\n'
)


def find_container_close(html, open_end):
    """Return the index of the `</div>` that closes the container div whose
    opening tag ends at `open_end` (depth counting over <div>/</div>)."""
    depth = 1
    for m in re.finditer(r"<div\b[^>]*>|</div>", html[open_end:]):
        if m.group(0).startswith("</div"):
            depth -= 1
            if depth == 0:
                return open_end + m.start()
        else:
            depth += 1
    return -1


def patch(stem, alt, dry_run):
    path = os.path.join(GUIDES, stem + ".html")
    if not os.path.exists(path):
        print(f"  MISSING  {stem}.html")
        return False
    html = open(path, encoding="utf-8").read()

    if f"{stem}-vignette-hero" in html:
        print(f"  skip     {stem}.html (vignette already wired)")
        return False

    # locate the hero region (either <section class="hero"> or <div class="hero">)
    hero = re.search(r'<(section|div) class="hero">', html)
    if not hero:
        print(f"  NO HERO  {stem}.html")
        return False

    # first container div inside the hero
    cont = re.search(r'<div class="container">', html[hero.end():])
    if not cont:
        print(f"  NO CONT  {stem}.html")
        return False
    cont_open_start = hero.end() + cont.start()
    cont_open_end = hero.end() + cont.end()

    close_idx = find_container_close(html, cont_open_end)
    if close_idx == -1:
        print(f"  UNBALANCED  {stem}.html")
        return False

    figure = FIGURE_TMPL.format(stem=stem, alt=alt)

    new_html = (
        html[:cont_open_end]
        + '\n<div class="hero-grid">\n<div class="hero-copy">'
        + html[cont_open_end:close_idx].rstrip("\n")
        + "\n    </div>\n"          # close hero-copy
        + figure
        + "    </div>\n"            # close hero-grid
        + html[close_idx:]
    )

    if dry_run:
        print(f"  WOULD WIRE  {stem}.html")
    else:
        open(path, "w", encoding="utf-8").write(new_html)
        print(f"  wired    {stem}.html")
    return True


def main():
    dry_run = "--dry-run" in sys.argv
    only = None
    if "--guide" in sys.argv:
        only = sys.argv[sys.argv.index("--guide") + 1].replace(".html", "")
    n = 0
    for stem, alt in TARGETS.items():
        if only and stem != only:
            continue
        if patch(stem, alt, dry_run):
            n += 1
    print(f"\n{'Would wire' if dry_run else 'Wired'} {n} guide(s).")


if __name__ == "__main__":
    main()
