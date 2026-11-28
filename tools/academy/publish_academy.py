#!/usr/bin/env python3
"""Move the Renal Care Academy pages out of guides/ into academy/ (idempotent).

The course generators (generate_nursing_course.py, generate_tech_courses.py) write and patch their pages in
guides/, because the house patch pipeline only works there. This script then moves every academy page to
academy/, so the staff-training section has its own URLs (/academy/<slug>) and never appears in the Guides
index, the guide search index, or the Latest strip. Both generators call it automatically.

    python3 tools/academy/publish_academy.py [--dry-run]

What it rewrites in each moved page:
  - canonical / og:url / JSON-LD / share links: /guides/<slug>  ->  /academy/<slug>   (landing page -> /academy/)
  - relative links to ordinary guides and calculators: x.html -> ../guides/x.html   (links between academy pages stay relative)
  - header navigation: adds ACADEMY (marked current) after DRUGS
  - nursing pages: adds the "Renal Care Academy" breadcrumb the technician pages already carry
"""
import os, re, sys
from pathlib import Path
from urllib.parse import quote

ROOT = Path(__file__).resolve().parents[2]
GUIDES, ACADEMY = ROOT / "guides", ROOT / "academy"
SITE = "https://renalcarematters.com"
LANDING = "renal-care-academy.html"
PREFIXES = ("nephrology-nursing", "hemodialysis-technician", "water-treatment-technician", "dialysis-biomedical-technician", "physician-on-duty", "renal-dietitian", "dialysis-clinical-head", "peritoneal-dialysis-nurse", "philhealth-claims", "dialysis-unit-manager", "transplant-nurse", "attending-nephrologist", "attending-pediatric-nephrologist", "medical-records-officer", "dialysis-head-nurse", "dialysis-unit-support-staff", "dialysis-charge-nurse", "special-dialysis-nurse-roles", "dialyzer-reprocessing-technician", "dialysis-nurse-assistant", "vascular-surgeon", "transplant-coordinator", "occupational-physical-therapist", "social-worker", "dialysis-unit-owner", "pediatric-dialysis-nurse", "nephrology-trainee", "resuscitation-lab", "disaster-preparedness")
DRY = "--dry-run" in sys.argv


def is_academy(name):
    if re.search(r" \d+\.html$", name):   # iCloud "page 2.html" copies are never academy pages
        return False
    return name == LANDING or (name.endswith(".html") and any(name == p + ".html" or name.startswith(p + "-") for p in PREFIXES))


def academy_names():
    names = {f.name for f in GUIDES.glob("*.html") if is_academy(f.name)}
    if ACADEMY.is_dir():
        names |= {f.name for f in ACADEMY.glob("*.html") if is_academy(f.name)}
        if (ACADEMY / "index.html").exists():
            names.add(LANDING)
    return names


def rewrite(text, name, names):
    for n in names:
        slug = n[:-5]
        new = f"{SITE}/academy/" if n == LANDING else f"{SITE}/academy/{slug}"
        old = f"{SITE}/guides/{slug}"
        for a, b in ((old, new), (quote(old, safe=""), quote(new, safe=""))):
            text = re.sub(re.escape(a) + r"(?![A-Za-z0-9\-])", lambda _m: b, text)

    def link(m):
        target, rest = m.group(2), m.group(3) or ""
        if target == LANDING:
            return f'{m.group(1)}="./{rest}"' if rest else f'{m.group(1)}="./"'
        if target in names:
            return m.group(0)
        return f'{m.group(1)}="../guides/{target}{rest}"'
    text = re.sub(r'\b(href)="([A-Za-z0-9][A-Za-z0-9._\-]*\.html)([#?][^"]*)?"', link, text)
    if 'href="/academy/"' not in text.split("</header>")[0]:
        text = re.sub(r'(<a href="/drugs/"[^>]*>DRUGS</a>)', r'\1<a href="/academy/" class="is-current" aria-current="page">ACADEMY</a>', text, count=1)
    if name.startswith("nephrology-nursing") and "Renal Care Academy</a>" not in text.split("<main")[0]:
        text = text.replace('<div class="nc-bar">', '<div class="nc-bar"><a href="./">Renal Care Academy</a><span class="nc-sep">›</span>', 1)
    return text


def main():
    names = academy_names()
    moved = []
    for n in sorted(names):
        src = GUIDES / n
        if not src.exists():
            continue
        dst = ACADEMY / ("index.html" if n == LANDING else n)
        moved.append(n)
        if DRY:
            continue
        ACADEMY.mkdir(exist_ok=True)
        text = rewrite(src.read_text(encoding="utf-8"), n, names)
        os.replace(src, dst)                 # rename, so nothing is left behind in guides/
        dst.write_text(text, encoding="utf-8")
    print(("would move " if DRY else "moved ") + f"{len(moved)} academy page(s) to academy/")
    if not DRY:   # keep the Academy taxonomy (groups, breadcrumbs, track names) after every generator run
        import importlib.util
        spec = importlib.util.spec_from_file_location("apply_taxonomy", Path(__file__).with_name("apply_taxonomy.py"))
        T = importlib.util.module_from_spec(spec); spec.loader.exec_module(T); T.main()
        spec = importlib.util.spec_from_file_location("apply_type_scale", Path(__file__).with_name("apply_type_scale.py"))
        S = importlib.util.module_from_spec(spec); spec.loader.exec_module(S); S.main()   # larger reading type
        spec = importlib.util.spec_from_file_location("apply_track_colors", Path(__file__).with_name("apply_track_colors.py"))
        C = importlib.util.module_from_spec(spec); spec.loader.exec_module(C); C.main()   # hero tiles by track family
        spec = importlib.util.spec_from_file_location("apply_study_tools", Path(__file__).with_name("apply_study_tools.py"))
        ST = importlib.util.module_from_spec(spec); spec.loader.exec_module(ST); ST.main()   # landing: Study tools section
        spec = importlib.util.spec_from_file_location("apply_notes", Path(__file__).with_name("apply_notes.py"))
        N = importlib.util.module_from_spec(spec); spec.loader.exec_module(N); N.main()   # highlights, notes, bookmarks + Schola scripts
        spec = importlib.util.spec_from_file_location("apply_listen", Path(__file__).with_name("apply_listen.py"))
        L = importlib.util.module_from_spec(spec); spec.loader.exec_module(L); L.main()   # Listen player (read aloud)
        spec = importlib.util.spec_from_file_location("apply_certificate", Path(__file__).with_name("apply_certificate.py"))
        CE = importlib.util.module_from_spec(spec); spec.loader.exec_module(CE); CE.main()   # certificate of completion on final exams
        spec = importlib.util.spec_from_file_location("apply_study_record", Path(__file__).with_name("apply_study_record.py"))
        SR = importlib.util.module_from_spec(spec); spec.loader.exec_module(SR); SR.main()   # Personal Study Record (hubs + checklist sign-off dates)
        spec = importlib.util.spec_from_file_location("apply_placement", Path(__file__).with_name("apply_placement.py"))
        PL = importlib.util.module_from_spec(spec); spec.loader.exec_module(PL); PL.main()   # placement pre-test (experienced hires)
        spec = importlib.util.spec_from_file_location("apply_cases", Path(__file__).with_name("apply_cases.py"))
        CA = importlib.util.module_from_spec(spec); spec.loader.exec_module(CA); CA.main()   # interactive branching cases
        spec = importlib.util.spec_from_file_location("apply_cross_role", Path(__file__).with_name("apply_cross_role.py"))
        CR = importlib.util.module_from_spec(spec); spec.loader.exec_module(CR); CR.main()   # "Same event, every role" team drill
        spec = importlib.util.spec_from_file_location("apply_review", Path(__file__).with_name("apply_review.py"))
        RV = importlib.util.module_from_spec(spec); spec.loader.exec_module(RV); RV.main()   # spaced-repetition review deck
        spec = importlib.util.spec_from_file_location("apply_skills", Path(__file__).with_name("apply_skills.py"))
        SK = importlib.util.module_from_spec(spec); spec.loader.exec_module(SK); SK.main([])   # preceptor sign-off on the learner's device
        spec = importlib.util.spec_from_file_location("apply_emergency_cards", Path(__file__).with_name("apply_emergency_cards.py"))
        EQ = importlib.util.module_from_spec(spec); spec.loader.exec_module(EQ); EQ.main()   # emergency quick cards page + links
        spec = importlib.util.spec_from_file_location("apply_resus_lab", Path(__file__).with_name("apply_resus_lab.py"))
        RL = importlib.util.module_from_spec(spec); spec.loader.exec_module(RL); RL.main()   # Emergency Readiness section + Resuscitation Lab Practice Lab
        spec = importlib.util.spec_from_file_location("apply_updates", Path(__file__).with_name("apply_updates.py"))
        UP = importlib.util.module_from_spec(spec); spec.loader.exec_module(UP); UP.main([])   # "Updated since you read it" flags
        spec = importlib.util.spec_from_file_location("apply_tools", Path(__file__).with_name("apply_tools.py"))
        TL = importlib.util.module_from_spec(spec); spec.loader.exec_module(TL); TL.main([])   # inline Calculo / Dosis tools
        spec = importlib.util.spec_from_file_location("apply_pager", Path(__file__).with_name("apply_pager.py"))
        PG = importlib.util.module_from_spec(spec); spec.loader.exec_module(PG); PG.main([])   # editorial module pager (prev / next)
        spec = importlib.util.spec_from_file_location("strip_symptom_widget", Path(__file__).with_name("strip_symptom_widget.py"))
        W = importlib.util.module_from_spec(spec); spec.loader.exec_module(W); W.main()   # no Symptom Checker in the Academy
        spec = importlib.util.spec_from_file_location("patch_site_nav", Path(__file__).resolve().parents[2] / "patch_site_nav.py")
        NV = importlib.util.module_from_spec(spec); spec.loader.exec_module(NV); sys.argv = sys.argv[:1]; NV.main()  # nav order + phone menu
        spec = importlib.util.spec_from_file_location("patch_share_slot", Path(__file__).resolve().parents[2] / "patch_share_slot.py")
        SS = importlib.util.module_from_spec(spec); spec.loader.exec_module(SS); sys.argv = sys.argv[:1]; SS.main()  # pre-sized hero share row (no layout shift)
        spec = importlib.util.spec_from_file_location("apply_glossary_terms", Path(__file__).with_name("apply_glossary_terms.py"))
        GT = importlib.util.module_from_spec(spec); spec.loader.exec_module(GT); GT.main([])   # tap-to-define glossary terms
        spec = importlib.util.spec_from_file_location("apply_search", Path(__file__).with_name("apply_search.py"))
        SR = importlib.util.module_from_spec(spec); spec.loader.exec_module(SR); SR.main([])   # Academy-wide search (Pagefind index + dialog)
        spec = importlib.util.spec_from_file_location("build_schola", Path(__file__).with_name("build_schola.py"))
        S2 = importlib.util.module_from_spec(spec); spec.loader.exec_module(S2); S2.main()  # Schola app: offline file list
        spec = importlib.util.spec_from_file_location("build_paratus", Path(__file__).with_name("build_paratus.py"))
        PA = importlib.util.module_from_spec(spec); spec.loader.exec_module(PA); PA.main()  # Paratus app: /paratus/ copies + offline list


if __name__ == "__main__":
    main()
