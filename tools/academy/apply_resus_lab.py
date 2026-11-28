#!/usr/bin/env python3
"""Emergency Readiness section and the Resuscitation Lab Practice Lab (Nov 28 2026; signed off by Dr. Rivero the same day).
Idempotent. publish_academy.py runs it right after apply_emergency_cards.py.

  1. fingerprints assets/academy-resus-lab.js as assets/academy-resus-lab.<hash>.js (older copies pruned);
  2. builds academy/emergency-readiness.html (the cross-track section hub: Act / Learn / Practice, role readiness matrix)
     and academy/resuscitation-lab-practice.html (recognition trainer, timed megacodes, facilitator recorder and shared
     display), both from the landing page's head, header and footer; data from data/academy-resus/recognition.json and
     data/academy-cases/rl-*.json;
  3. puts an "Emergency Readiness" block on the landing page right after the Emergency quick cards callout
     (EMERGENCY-READINESS markers);
  4. puts a readiness badge (BLS / ALS / PALS, draft) on each track hub (RL-BADGE markers, before the qualifications box);
  5. adds "Why this step?" links from each Emergency Quick Card to the module that teaches it (RL-WHY markers; the
     signed-off card text is not touched);
  6. while DRAFT is True: a DRAFT banner and <meta name="robots" content="noindex"> on every Resuscitation Lab page and
     the section hub (RL-DRAFT markers). Set DRAFT = False after clinical sign-off and run again.

    python3 tools/academy/apply_resus_lab.py [--dry-run]
"""
import hashlib, html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY, ASSETS = ROOT / "academy", ROOT / "assets"
DRAFT = False   # signed off by Dr. Rivero, November 28, 2026
NAME = "academy-resus-lab"
SITE = "https://renalcarematters.com/academy/"
HUB = "resuscitation-lab"
PRACTICE, READY = "resuscitation-lab-practice.html", "emergency-readiness.html"
DHUB, DNAME = "disaster-preparedness", "academy-disaster-lab"     # Disaster Preparedness and Response (Nov 28 2026; signed off)
DPRACTICE = DHUB + "-practice.html"
LS, LE = "<!-- EMERGENCY-READINESS-START -->", "<!-- EMERGENCY-READINESS-END -->"
BS, BE = "<!-- RL-BADGE-START -->", "<!-- RL-BADGE-END -->"
WS, WE = "<!-- RL-WHY-START -->", "<!-- RL-WHY-END -->"
DS, DE = "<!-- RL-DRAFT-START -->", "<!-- RL-DRAFT-END -->"
ROBOTS = '<meta name="robots" content="noindex"><!-- RL-DRAFT-ROBOTS -->'

MODS = {}   # filled from the generated hub: number -> (file, title)
DMODS = {}  # the same for Disaster Preparedness and Response


def modules(hub=HUB, out=None):
    out = MODS if out is None else out
    for f in sorted(ACADEMY.glob(hub + "-[0-9][0-9]-*.html")):
        if re.search(r" \d+\.html$", f.name):
            continue
        n = int(f.name.split("-")[2])
        t = re.search(r"<h1[^>]*>(.*?)</h1>", f.read_text(encoding="utf-8"), re.S)
        out[n] = (f.name, re.sub(r"<[^>]+>", "", t.group(1)).strip() if t else f.name)
    return out


# Readiness level per track hub (draft Academy recommendation; verified Philippine rules flagged)
LEVEL = {
    "ALS": ["nephrology-nursing", "dialysis-charge-nurse", "dialysis-head-nurse", "special-dialysis-nurse-roles", "peritoneal-dialysis-nurse",
            "transplant-nurse", "nephrology-nursing-educator", "physician-on-duty", "dialysis-clinical-head", "attending-nephrologist",
            "nephrology-trainee", "vascular-surgeon"],
    "PALS": ["pediatric-dialysis-nurse", "attending-pediatric-nephrologist"],
    "BLS": ["hemodialysis-technician", "water-treatment-technician", "dialysis-biomedical-technician", "dialyzer-reprocessing-technician",
            "dialysis-nurse-assistant", "dialysis-unit-support-staff", "renal-dietitian", "occupational-physical-therapist", "social-worker",
            "medical-records-officer", "transplant-coordinator"],
    "BLS recommended": ["dialysis-unit-manager", "philhealth-claims", "dialysis-unit-owner"],
}
VERIFIED = {
    "nephrology-nursing": "Philippine rule: current BLS for dialysis nurses, and at least one nurse per shift with updated ACLS (DOH, PSN).",
    "dialysis-charge-nurse": "Philippine rule: current BLS; at least one ACLS-trained nurse per shift, often the charge nurse (DOH, PSN).",
    "dialysis-head-nurse": "Philippine rule: current BLS/ACLS from a DOH-accredited provider (PSN).",
    "physician-on-duty": "Philippine rule: current ACLS from a DOH-accredited provider (DOH, PSN).",
}
WHY = {  # quick card id -> module numbers that teach it
    "code": [4, 5, 7], "leak": [7], "hypotension": [3, 7], "access-bleeding": [9], "air-embolism": [7], "hemolysis": [9],
    "anaphylaxis": [9], "chest-pain": [6, 12], "arrhythmia": [6], "hyperkalemia": [8], "hypoglycemia": [9], "seizure": [9],
}


def fingerprint(dry, NAME=NAME):
    data = (ASSETS / (NAME + ".js")).read_bytes()
    out = f"{NAME}.{hashlib.sha256(data).hexdigest()[:10]}.js"
    if not dry:
        (ASSETS / out).write_bytes(data)
        for old in ASSETS.glob(NAME + ".*.js"):
            if old.name != out and re.fullmatch(re.escape(NAME) + r"\.[0-9a-f]{10}\.js", old.name):
                old.unlink()
    return out


def sub_meta(head, title, desc, url):
    head = re.sub(r"<title>.*?</title>", f"<title>{title}</title>", head, count=1, flags=re.S)
    for prop, val in (("og:title", title), ("twitter:title", title), ("og:description", desc), ("twitter:description", desc), ("og:url", url), ("twitter:url", url)):
        head = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*(")' % re.escape(prop), lambda m: m.group(1) + val + m.group(2), head)
    head = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + desc + m.group(2), head, count=1)
    head = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + url + m.group(2), head, count=1)
    og = ROOT / "images" / "og" / (url.rsplit("/", 1)[-1] + "-og.jpg")   # a dedicated share card, once made (image prompt pack, Part 4)
    if og.exists():
        img = "https://renalcarematters.com/images/og/" + og.name
        head = re.sub(r'(<meta (?:property|name)="(?:og:image|twitter:image)" content=")[^"]*(")', lambda m: m.group(1) + img + m.group(2), head)
        head = re.sub(r'(<meta property="og:image:(?:width|height)" content=")[^"]*(")', lambda m: m.group(1) + ("1200" if "width" in m.group(0) else "630") + m.group(2), head)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', "", head, flags=re.S)
    head = re.sub(r'<meta name="robots"[^>]*>(<!-- RL-DRAFT-ROBOTS -->)?\s*', "", head)
    return head


def shell(land, title, desc, url, main, scripts=""):
    head, rest = land.split("</head>", 1)
    head = sub_meta(head + "</head>", title, desc, url)
    body_open = rest[:rest.index("</header>") + len("</header>")]
    tail = rest[rest.index('<footer class="guide-footer">'):]
    tail = re.sub(r'<button class="print-btn".*?</button>\s*', "", tail, count=1, flags=re.S)
    tail = re.sub(r'\n?<script src="[^"]*assets/(academy-|schola|tech-course|guide-rail|share-buttons|image-lightbox)[^"]*" defer></script>', "", tail)
    page = head + body_open + "\n" + main + "\n" + tail
    i = page.rfind("</body>")
    return page[:i] + scripts + page[i:]


CSS = """<style id="rl-lab-css">
.rl-main{max-width:960px;}
.rl-panels{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin:16px 0;}
.rl-panels.two{grid-template-columns:repeat(2,1fr);}
.rl-panels.two .rl-panel.act{grid-column:1/-1;display:flex;align-items:center;gap:22px;}
.rl-panels.two .rl-panel.act img{flex:0 0 38%;width:38%;align-self:stretch;height:auto;min-height:200px;margin:-16px 0 -16px -18px;aspect-ratio:auto;object-fit:cover;border-radius:9px 0 0 9px;}
.rl-act-t{flex:1;}
.rl-colh{font:800 12.5px/1.3 Inter,system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:var(--text-muted);margin:6px 2px -4px;}
.rl-panel{display:block;text-decoration:none;color:var(--text);background:var(--white);border:1px solid var(--border);border-top:5px solid var(--teal);border-radius:14px;padding:16px 18px;}
.rl-panel:hover{border-color:var(--teal);}
.rl-panel.act{border-top-color:var(--red);} .rl-panel.prac{border-top-color:var(--amber,#b45309);} .rl-panel.dis{border-top-color:#1f3864;}
.rl-panel small{display:block;font:800 12px/1.2 Inter,system-ui,sans-serif;letter-spacing:.08em;text-transform:uppercase;color:var(--text-muted);}
.rl-panel img{display:block;width:calc(100% + 36px);margin:-16px -18px 12px;height:auto;aspect-ratio:16/9;object-fit:cover;border-radius:9px 9px 0 0;}
.rl-panel b{display:block;font:800 18px/1.25 Inter,system-ui,sans-serif;margin:4px 0 6px;color:var(--text);}
.rl-panel span{display:block;font-size:14.5px;line-height:1.5;color:var(--text-mid);}
.rl-draft{border:2px solid var(--red);background:var(--red-soft);color:var(--text);border-radius:12px;padding:10px 14px;margin:14px auto;max-width:860px;font-size:14.5px;line-height:1.45;}
.rl-draft b{color:var(--red);}
.rl-ctl{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:flex-end;margin:10px 0;}
.rl-fs{border:1px solid var(--border);border-radius:10px;padding:8px 12px;margin:0;}
.rl-fs legend{font-weight:700;font-size:13px;color:var(--text-mid);padding:0 4px;}
.rl-fs label{display:block;font-size:14.5px;margin:3px 0;}
.rl-btn{display:inline-block;font:700 14.5px/1 Inter,system-ui,sans-serif;background:var(--teal);color:#fff;border:0;border-radius:999px;padding:10px 16px;cursor:pointer;text-decoration:none;}
html[data-theme="dark"] .rl-btn{background:#0e4a50;}
.rl-btn.rl-ghost{background:transparent;color:var(--teal);border:1px solid var(--teal);}
html[data-theme="dark"] .rl-btn.rl-ghost{color:var(--text);border-color:var(--text-muted);}
.rl-btn:disabled{opacity:.5;cursor:default;}
.rl-meta,.rl-note{font-size:13.5px;color:var(--text-muted);}
.rl-card{background:var(--white);border:1px solid var(--border);border-radius:14px;padding:16px 18px;margin:12px 0;}
.rl-top{display:flex;gap:12px;align-items:center;justify-content:space-between;margin-bottom:6px;flex-wrap:wrap;}
.rl-type{font:800 12px/1.2 Inter,system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:var(--teal);}
html[data-theme="dark"] .rl-type{color:var(--text-mid);}
.rl-count,.rl-clock,.rl-timer{font:700 14px/1 Inter,system-ui,sans-serif;color:var(--text-mid);font-variant-numeric:tabular-nums;}
.rl-timer.warn,.rl-budget.warn{color:var(--red);}
.rl-stem,.rl-prompt{font-size:16.5px;line-height:1.5;margin:6px 0 10px;}
.rl-strip,.rl-mstrip{display:block;width:100%;height:80px;border-radius:8px;background:#0b1220;}
.rl-find{font-size:15px;margin:8px 0;}
.rl-opts{display:grid;gap:8px;}
.rl-opt{text-align:left;font:500 15px/1.4 Manrope,system-ui,sans-serif;color:var(--text);background:var(--bg);border:1px solid var(--border);border-radius:10px;padding:10px 12px;cursor:pointer;}
.rl-opt:hover:not(:disabled){border-color:var(--teal);}
.rl-opt.right{border-color:var(--green,#2e6b3e);box-shadow:inset 4px 0 0 var(--green,#2e6b3e);}
.rl-opt.wrong{border-color:var(--red);box-shadow:inset 4px 0 0 var(--red);}
.rl-order .rl-opt.picked{opacity:.7;}
.rl-order .rl-opt.picked::before{content:attr(data-n) ". ";font-weight:800;color:var(--teal);}
.rl-orow{margin-top:10px;display:flex;gap:8px;flex-wrap:wrap;align-items:center;}
.rl-oseq{font-size:14px;color:var(--text-mid);flex-basis:100%;}
.rl-fb{margin-top:10px;}
.rl-verdict.ok{color:var(--green,#2e6b3e);font-weight:800;} .rl-verdict.no{color:var(--red);font-weight:800;}
html[data-theme="dark"] .rl-verdict.ok{color:#7ee2a0;}
.rl-tag{font-size:14px;color:var(--text-mid);font-style:italic;}
.rl-review{padding-left:20px;} .rl-review li{margin:8px 0;} .rl-review li.no b{color:var(--red);}
.rl-mon{background:#0b1220;border-radius:12px;padding:10px;margin:10px 0;color:#e6edf6;}
.rl-mon-grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(120px,1fr));gap:6px;margin-bottom:8px;}
.rl-mc-c{background:#13203a;border-radius:8px;padding:6px 8px;}
.rl-mc-c span{display:block;font-size:11.5px;color:#a9b8cc;} .rl-mc-c b{font:700 15px/1.25 Inter,system-ui,sans-serif;color:#f4f8fc;}
.rl-mc-c.alarm{outline:2px solid #ff6b6b;}
.rl-mon-lab{font-size:13px;color:#a9b8cc;margin-top:6px;}
.rl-scene p{font-size:15px;}
.rl-crit{border-left:4px solid var(--red);padding:6px 10px;background:var(--red-soft);}
.rl-why{font-size:14px;color:var(--text-mid);}
.rl-roles{display:grid;grid-template-columns:repeat(auto-fill,minmax(170px,1fr));gap:8px;margin:8px 0;}
/* shared display: preview + live thumbnail, rhythm playlist */
.rl-views{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin-top:12px;} @media (max-width:760px){.rl-views{grid-template-columns:1fr;}}
.rl-view{margin:0;min-width:0;} .rl-view figcaption{display:flex;justify-content:space-between;align-items:center;gap:8px;font:600 13px Inter,system-ui,sans-serif;color:var(--text-mid);margin-bottom:4px;}
.rl-view .rl-mstrip{margin:0;}
.rl-xpl{margin:4px 0 14px;border:1px solid var(--border);border-radius:12px;background:var(--white);overflow:hidden;}
.rl-xpl>figcaption{display:flex;align-items:center;gap:10px;padding:10px 14px;font:700 15px Inter,system-ui,sans-serif;color:var(--teal);}
.rl-xpl-play{display:inline-flex;align-items:center;justify-content:center;width:28px;height:28px;border-radius:50%;background:#0e4a50;color:#fff;font-size:11px;padding-left:2px;box-sizing:border-box;}
.rl-xpl video{display:block;width:100%;height:auto;background:#000;}
.rl-xpl-share{margin-left:auto;display:inline-flex;align-items:center;gap:6px;font:700 13.5px Inter,system-ui,sans-serif;color:#fff;background:#0e4a50;border:0;border-radius:999px;padding:7px 14px;cursor:pointer;}
.rl-xpl-share svg{width:16px;height:16px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;} .rl-xpl-share:hover{background:#1a6b72;}
.rl-xpl-tr{padding:6px 14px 10px;} .rl-xpl-tr summary{cursor:pointer;font:600 13.5px Inter,system-ui,sans-serif;color:var(--text-muted);} .rl-xpl-tr p{font-size:14px;line-height:1.6;color:var(--text-mid);margin:8px 0 0;}
@media print{.rl-xpl{display:none!important;}}
.rl-thumb{position:relative;width:100%;aspect-ratio:16/9;overflow:hidden;clip-path:inset(0 round 10px);border-radius:10px;background:#000;} .rl-thumb[hidden]{display:none;}
.rl-thumb iframe{position:absolute;top:0;left:0;width:1280px;height:720px;min-height:720px;max-height:720px;border:0;transform-origin:0 0;pointer-events:none;}
.rl-thumb-tog{font:600 12px Inter,system-ui,sans-serif;border:1px solid var(--border);background:transparent;color:var(--teal);border-radius:6px;padding:2px 10px;cursor:pointer;}
.m-thumbview .m-fs,.m-thumbview .m-beep,.m-thumbview .m-tap{display:none!important;}
.rl-pl{margin-top:18px;border-top:1px solid var(--border);padding-top:12px;} .rl-pl h4{margin:0 0 6px;font-size:17px;color:var(--text);}
.rl-pl-bar{display:flex;flex-wrap:wrap;gap:8px;align-items:center;margin:8px 0;} .rl-pl-bar .rl-lab{display:inline-flex;gap:6px;align-items:center;margin:0;}
.rl-pl-bar select,.rl-pl-bar input{max-width:260px;}
.rl-pl .rl-pl-list{list-style:none;margin:8px 0!important;padding:0!important;display:grid;gap:6px;}
.rl-pl-step{display:flex;flex-wrap:wrap;align-items:center;gap:10px;border:1px solid var(--border);border-radius:10px;padding:8px 10px;background:var(--white);}
.rl-pl-step.on{border-color:var(--teal);box-shadow:inset 0 0 0 2px var(--teal);}
.rl-pl-go{min-width:78px;} .rl-pl-txt{flex:1 1 220px;display:flex;flex-direction:column;min-width:0;color:var(--text);} .rl-pl-txt small{color:var(--text-muted);font-size:13px;}
.rl-pl-sh{font-size:13px;color:var(--text-mid);display:inline-flex;gap:6px;align-items:center;margin:0;}
.rl-pl-ord{display:inline-flex;gap:4px;} .rl-pl-ord button{border:1px solid var(--border);background:transparent;color:var(--text-mid);border-radius:6px;width:32px;height:32px;cursor:pointer;}
.rl-pl-empty{color:var(--text-muted);font-size:14px;}
.rl-roles label:has(.rl-d-lab){grid-column:span 2;} @media (max-width:420px){.rl-roles label:has(.rl-d-lab){grid-column:auto;}}
.rl-roles label{font-size:13.5px;color:var(--text-mid);display:block;}
.rl-roles input,.rl-roles select,.rl-lab select{width:100%;padding:8px;border:1px solid var(--border);border-radius:8px;background:var(--white);color:var(--text);font:inherit;box-sizing:border-box;}
.rl-evs{display:grid;grid-template-columns:repeat(auto-fill,minmax(140px,1fr));gap:8px;margin:10px 0;}
.rl-ev{font:700 14px/1.2 Inter,system-ui,sans-serif;padding:12px 8px;border-radius:10px;border:1px solid var(--border);background:var(--bg);color:var(--text);cursor:pointer;}
.rl-ev:active{transform:scale(.98);} .rl-ev[data-ev="shock"],.rl-ev[data-ev="ROSC"]{border-color:var(--red);}
.rl-log{max-height:220px;overflow:auto;font-variant-numeric:tabular-nums;padding-left:22px;}
.rl-rbar{display:flex;gap:8px;flex-wrap:wrap;align-items:center;margin:8px 0;}
.rl-matrix td,.rl-matrix th{vertical-align:top;}
.rl-list{columns:2;column-gap:28px;padding-left:20px;} .rl-list li{margin:4px 0;break-inside:avoid;}
body.rl-display-mode>*:not(.rl-display){display:none!important;}
.rl-display{position:fixed;inset:0;background:#050a14;color:#e8f0fa;display:flex;flex-direction:column;justify-content:center;padding:4vw;gap:2vw;}
.rl-dgrid{display:grid;grid-template-columns:repeat(3,1fr);gap:2vw;}
.rl-dgrid span{display:block;font-size:2.2vw;color:#9fb0c6;} .rl-dgrid b{font:800 7vw/1 Inter,system-ui,sans-serif;color:#5ee08a;}
.rl-dstrip{width:100%;height:28vh;background:#0b1220;border-radius:12px;}
.d-lab{font-size:2.4vw;color:#c9d6e6;} .rl-dnote{font-size:1.4vw;color:#6f8098;}
.rl-chk{display:block;margin:10px 0 8px;font-size:14.5px;color:var(--text);} .rl-chk input{margin-right:6px;vertical-align:-2px;}
/* bedside-monitor display (?display=1) */
.rl-mon2{background:#000;color:#e8f0fa;justify-content:flex-start;padding:10px 12px calc(8px + env(safe-area-inset-bottom,0px));gap:8px;font-family:Inter,system-ui,sans-serif;}
.m-top{display:flex;align-items:center;gap:12px;min-height:36px;}
.m-lab{font:700 15px/1.2 Inter,system-ui,sans-serif;color:#9fb0c6;max-width:28%;}
.m-alarm{flex:1;text-align:center;font:800 18px/1.25 Inter,system-ui,sans-serif;letter-spacing:.06em;padding:5px 10px;border-radius:6px;min-height:1.25em;}
.m-alarm.red{background:#c1121f;color:#fff;} .m-alarm.yel{background:#f2c200;color:#111;}
.m-clock{font:600 15px Inter,system-ui,sans-serif;color:#9fb0c6;font-variant-numeric:tabular-nums;}
.m-fs{font:700 14px Inter,system-ui,sans-serif;background:#1f2937;color:#e5e7eb;border:1px solid #475569;border-radius:8px;padding:8px 12px;cursor:pointer;transition:opacity .3s;}
.m-beep{font:700 14px Inter,system-ui,sans-serif;background:#1f2937;color:#e5e7eb;border:1px solid #475569;border-radius:8px;padding:8px 12px;cursor:pointer;transition:opacity .3s;white-space:nowrap;}
.m-idle .m-fs,.m-idle .m-beep{opacity:0;}
.m-tap{font:800 14px Inter,system-ui,sans-serif;background:#f2c200;color:#111;border:0;border-radius:8px;padding:8px 12px;cursor:pointer;}
.m-tap[hidden]{display:none;}
.m-main{flex:1 1 0;display:grid;grid-template-columns:1fr minmax(210px,28%);gap:10px;min-height:0;}
.rl-mon2{overflow:hidden;} .rl-mon2>.m-top,.rl-mon2>.m-defib,.rl-mon2>.m-note{flex:none;}   /* the monitor area gives way; the display never overflows its screen */
.m-main>*,.m-waves>*{min-width:0;}
.m-waves{display:grid;grid-template-rows:3fr 2fr 2fr;gap:8px;min-height:0;min-width:0;}
.m-ecg{position:relative;background:#0b1220;border-radius:8px;min-height:0;display:flex;overflow:hidden;}
.m-ecg .rl-dstrip,.m-ecg .rl-dpleth,.m-ecg .rl-dco2{display:block;flex:1;width:100%;height:100%;min-height:0;border-radius:8px;}
.m-pl .m-lead{color:#22d3ee;} .m-co2 .m-lead{color:#fbbf24;} .m-co2 .m-lead small{font-weight:600;opacity:.8;}
.m-plno{position:absolute;right:12px;top:6px;font:800 13px Inter,system-ui,sans-serif;letter-spacing:.06em;color:#facc15;}
.m-plno[hidden]{display:none;}
.m-lead{position:absolute;left:10px;top:6px;color:#4ade80;font:700 13px Inter,system-ui,sans-serif;}
.m-par{display:grid;grid-template-rows:repeat(4,1fr);gap:8px;min-height:0;}
.m-box{container-type:inline-size;min-width:0;background:#0b1220;border-radius:8px;padding:8px 12px;display:flex;flex-direction:column;justify-content:center;border:2px solid transparent;min-height:0;}
.m-k{font:700 14px Inter,system-ui,sans-serif;} .m-k small{font-weight:600;opacity:.8;}
.m-v{font:800 clamp(34px,8.5vh,96px)/1 Inter,system-ui,sans-serif;font-variant-numeric:tabular-nums;}
.m-bp .m-v{font-size:clamp(22px,min(8vh,22cqi),84px);white-space:nowrap;}
.m-hr .m-k,.m-hr .m-v{color:#4ade80;} .m-co2b .m-k,.m-co2b .m-v{color:#fbbf24;} .m-sp .m-k,.m-sp .m-v{color:#22d3ee;} .m-bp .m-k,.m-bp .m-v{color:#f1f5f9;}
.m-box.yel{border-color:#facc15;} .m-box.yel .m-v,.m-box.yel .m-k{color:#facc15;}
.m-box.red{border-color:#ff4d4d;} .m-box.red .m-v,.m-box.red .m-k{color:#ff4d4d;}
.m-lim,.m-sub{font:600 13px Inter,system-ui,sans-serif;color:#9fb0c6;margin-top:4px;} .m-sub i{font-style:normal;color:#e2e8f0;}
.m-flash .m-box.red{animation:mflash 1s steps(2,start) infinite;} .m-flash .m-alarm.red{animation:mflash2 1s steps(2,start) infinite;}
@keyframes mflash{50%{background:#4a0a0a;}} @keyframes mflash2{50%{background:#6d0912;}}
.m-defib{display:flex;flex-wrap:wrap;gap:8px;align-items:center;background:#111827;border-radius:8px;padding:8px 10px;}
.m-defib{zoom:2;row-gap:6px;padding:6px 8px;} .m-defib .m-dstat{flex:1 1 100%;} @media (max-width:700px){.m-defib{zoom:1.4;}}
@media (max-width:700px){.m-top{flex-wrap:wrap;gap:6px;}.m-top .m-clock{display:none;}.m-top .m-alarm{order:5;flex:1 1 100%;}.m-top .m-lab{display:none;}.m-top .m-fs,.m-top .m-beep,.m-top .m-tap{padding:7px 10px;font-size:13px;}.m-top>.m-tap,.m-top>.m-beep{margin-left:auto;}}   /* defibrillator panel at 200% (Nov 28 2026) */
.m-defib[hidden]{display:none;}
.m-dstat{font:700 15px Inter,system-ui,sans-serif;color:#e2e8f0;flex:1 1 260px;} .m-dst{color:#fde68a;}
.m-charged .m-dst{color:#ff6b6b;} .m-charging .m-dst{color:#fbbf24;}
.m-defib label{font:600 14px Inter,system-ui,sans-serif;color:#cbd5e1;}
.m-j{font:700 16px Inter,system-ui,sans-serif;background:#000;color:#fde68a;border:1px solid #475569;border-radius:6px;padding:6px;margin-left:4px;}
.m-b{font:800 15px Inter,system-ui,sans-serif;border-radius:8px;padding:10px 14px;border:1px solid #475569;background:#1f2937;color:#e5e7eb;cursor:pointer;min-height:44px;}
.m-charge{background:#b45309;border-color:#b45309;color:#fff;} .m-shock{background:#b91c1c;border-color:#b91c1c;color:#fff;}
.m-charged .m-shock{box-shadow:0 0 0 3px #fecaca;} .m-b:disabled{opacity:.35;cursor:default;}
.m-sync.on{background:#0e7490;border-color:#0e7490;color:#fff;}
.m-count{font:700 14px Inter,system-ui,sans-serif;color:#cbd5e1;}
.m-zap{background:#fff!important;}
.m-note{font-size:12px;color:#6f8098;margin:0;text-align:center;}
@media (max-width:700px){.m-main{grid-template-columns:1fr;grid-template-rows:minmax(300px,1fr) auto;}.m-par{grid-template-columns:repeat(2,1fr);grid-template-rows:none;}.m-v{font-size:32px;}.m-bp .m-v{font-size:clamp(20px,22cqi,32px);}.m-lab{display:none;}.m-alarm{font-size:14px;}}
@media (prefers-reduced-motion:reduce){.m-flash .m-box.red,.m-flash .m-alarm.red{animation:none;}}
@media (max-width:760px){.rl-panels,.rl-panels.two{grid-template-columns:1fr;}.rl-list{columns:1;}
 .rl-panels.two .rl-panel.act{display:block;} .rl-panels.two .rl-panel.act img{width:calc(100% + 36px);min-height:0;height:auto;margin:-16px -18px 12px;aspect-ratio:16/9;border-radius:9px 9px 0 0;}
 .rl-colh.r1{order:1;} .rl-panel.o2{order:2;} .rl-panel.o3{order:3;} .rl-colh.r2{order:4;margin-top:10px;} .rl-panel.o5{order:5;} .rl-panel.o6{order:6;}}
.rl-sample-box{border:1px solid var(--border);border-left:5px solid var(--teal);border-radius:14px;background:var(--white);padding:14px 18px;margin:12px 0;}
.rl-steps{margin:0;padding-left:22px;} .rl-steps>li{margin:0 0 16px;font-size:15.5px;line-height:1.55;} .rl-steps>li:last-child{margin-bottom:4px;}
.rl-steps>li>b:first-child{color:var(--text);} .rl-steps .rl-btn{margin-top:8px;}
.rl-sitem{border:1px solid var(--border);border-radius:12px;background:var(--bg);padding:10px 14px;margin:10px 0 4px;}
.rl-sitem .rl-stem{font-size:15.5px;margin:4px 0 6px;}
.rl-sw{padding:10px 0;border-top:1px solid var(--border);} .rl-sw:first-child{border-top:0;padding-top:2px;} .rl-sw .rl-strip{height:64px;margin:4px 0;}
.rl-sample-note ul{margin:6px 0;padding-left:20px;} .rl-sample-note li{margin:4px 0;}
.rl-sopts{margin:0;padding-left:20px;font-size:14.5px;line-height:1.45;} .rl-sopts li{margin:4px 0;color:var(--text-mid);} .rl-sopts li b{color:var(--text);}
.rl-sopts li.ok b{color:var(--green,#2e6b3e);} .rl-sopts li.ok::marker{color:var(--green,#2e6b3e);font-weight:800;}
.rl-sample-note{border:1px dashed var(--teal);border-radius:10px;padding:8px 12px;}
.rl-why-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:14px 0;}
.rl-why-grid>div{border:1px solid var(--border);border-top:4px solid var(--teal);border-radius:12px;padding:12px 14px;background:var(--white);font-size:15px;line-height:1.55;color:var(--text-mid);}
.rl-why-grid b{display:block;color:var(--text);margin-bottom:4px;}
.rl-rules{padding-left:22px;} .rl-rules li{margin:8px 0;font-size:15.5px;line-height:1.55;}
.rl-rot-in{display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px;margin:8px 0;}
.rl-rot-in label{font-size:13.5px;color:var(--text-mid);display:block;}
.rl-rot-in input{width:100%;padding:8px;border:1px solid var(--border);border-radius:8px;background:var(--white);color:var(--text);font:inherit;box-sizing:border-box;}
.rl-rot-wrap{overflow-x:auto;margin:10px 0;} .rl-rot-t{border-collapse:collapse;font-size:14px;min-width:760px;width:100%;}
.rl-rot-t th,.rl-rot-t td{border:1px solid var(--border);padding:6px 8px;text-align:left;vertical-align:top;} .rl-rot-t th{background:var(--bg);font-weight:700;}
.rl-rot-t td.cmb{color:var(--text-muted);font-style:italic;} .rl-rot-t tr.sel td{background:var(--teal-soft,rgba(26,107,114,.08));}
.rl-cov{font-size:14px;line-height:1.5;padding-left:20px;} .rl-cov li{margin:3px 0;}
.rl-rcs{display:grid;grid-template-columns:1fr 1fr;gap:12px;margin:12px 0;}
.rl-rc{border:1px solid var(--border);border-left:5px solid var(--teal);border-radius:12px;background:var(--white);padding:12px 16px;font-size:14.5px;line-height:1.5;}
.rl-rc:first-child{grid-column:1/-1;border-left-color:var(--red);}
.rl-rc header{display:flex;align-items:center;gap:10px;flex-wrap:wrap;margin-bottom:4px;}
.rl-rc h3{margin:0;font:800 17px/1.25 Inter,system-ui,sans-serif;color:var(--text);}
.rl-rc-n{flex:none;width:26px;height:26px;border-radius:50%;background:var(--teal);color:#fff;font:800 13px/26px Inter,system-ui,sans-serif;text-align:center;}
.rl-rc:first-child .rl-rc-n{background:var(--red);}
.rl-rc-held{margin-left:auto;font-size:13px;color:var(--text-muted);} .rl-rc-held b{display:inline-block;min-width:56px;border-bottom:1px solid var(--text-muted);color:var(--text);}
.rl-rc-who{margin:4px 0 6px;color:var(--text-mid);} .rl-rc-who b{color:var(--text);}
.rl-rc h4{margin:10px 0 3px;font:800 12px/1.2 Inter,system-ui,sans-serif;letter-spacing:.06em;text-transform:uppercase;color:var(--teal);}
.rl-rc ul{margin:0;padding-left:18px;} .rl-rc li{margin:3px 0;color:var(--text-mid);}
.rl-rc ul.rl-say li{color:var(--text);font-weight:600;} .rl-rc ul.rl-never li{color:var(--red);}
.rl-rc-mod{margin:8px 0 0;font-size:12.5px;color:var(--text-muted);}
@media (max-width:760px){.rl-why-grid,.rl-rcs{grid-template-columns:1fr;}}
@media (max-width:1100px){.rl-main .rl-host,.rl-main #dp-tt,.rl-main #dp-call,.rl-main #dp-evac,.rl-main .rl-sample-box{margin-right:52px;}}
@media print{.rl-ctl,.rl-evs,.rl-rbar,#recognition,#megacodes,#sample{display:none!important;}
 body.rl-print-rc main>*:not(#roles){display:none!important;} body.rl-print-rc #roles>p,body.rl-print-rc #roles>.section-tag,body.rl-print-rc #roles>h2{display:none!important;}
 body.rl-print-rc .rl-rcs{display:block;} body.rl-print-rc .rl-rc{break-inside:avoid;margin:0 0 10px;border-left-width:3px;}
 body.rl-print-rot main>*:not(#rotation){display:none!important;} body.rl-print-rot #rotation>*:not(#rl-rot):not(h3){display:none!important;}
 body.rl-print-roles main>*:not(#facilitator){display:none!important;}}
</style>"""


DRAFT_TEXT = {
    "resus": ("An educational reviewer and practice resource; not an American Heart Association course, not Basic Life Support (BLS), "
              "Advanced Cardiovascular Life Support (ACLS) or Pediatric Advanced Life Support (PALS) certification. "
              "Your unit protocol decides every real event."),
    "disaster": ("An educational course and drill resource; not a hospital disaster plan and not a licensing requirement. Your unit protocol, "
                 "the attending nephrologist and your local disaster authorities decide every real event."),
    "both": ("Educational courses and practice resources. The Resuscitation Lab is not an American Heart Association course and gives no "
             "Basic Life Support (BLS), Advanced Cardiovascular Life Support (ACLS) or Pediatric Advanced Life Support (PALS) certification; "
             "Disaster Preparedness and Response is not a hospital disaster plan. Your unit protocol decides every real event."),
}


def draft_banner(kind="resus"):
    return (f'{DS}<div class="rl-draft" role="note"><b>DRAFT, pending clinical sign-off by Dr. William Gregory Rivero.</b> Not for clinical use. '
            f'{DRAFT_TEXT[kind]}</div>{DE}') if DRAFT else ""


def hero(crumb, h1, tagline):
    return f"""<section class="hero">
  <div class="container">
    <div class="nc-bar"><a href="./">Renal Care Academy</a><span class="nc-sep">›</span>{crumb}</div>
    <h1>{h1}</h1>
    <p class="hero-tagline">{tagline}</p>
  </div>
</section>"""


def tile(name):
    """A tile image for a panel, only when the file exists (images arrive after the pages)."""
    if not (ROOT / "images" / name).exists():
        return ""
    return f'<img src="../images/{name}" alt="" loading="lazy" decoding="async" width="640" height="360">'


def draft_cards_note():
    """While the disaster quick cards are drafts, point reviewers to their review page (built by apply_emergency_cards.py)."""
    if not (ACADEMY / "emergency-cards-disaster-draft.html").exists():
        return ""
    return ('  <p class="rl-note"><b>In review:</b> five disaster quick cards (power failure, earthquake, fire, typhoon warning, water failure) '
            'are drafted and waiting for clinical sign-off. They are not on the live quick card page yet. '
            '<a href="emergency-cards-disaster-draft.html">Read the drafts</a>.</p>')


def paratus_xpl():
    """Meet Paratus cartoon explainer (Nov 28 2026, Dr. Rivero): always visible, preload none, no download,
    Share = the watch page /watch/paratus. Uses the .rl-xpl styles in CSS. Transcript from the explainer's script.txt."""
    if not (ROOT / "videos" / "paratus" / "paratus-explainer.mp4").exists():
        return ""
    sp = ROOT / "tools" / "academy" / "explainers" / "paratus" / "script.txt"
    tr = html.escape(" ".join(sp.read_text(encoding="utf-8").split())) if sp.exists() else ""
    return ('<figure class="rl-xpl" id="explainer"><figcaption><span class="rl-xpl-play" aria-hidden="true">&#9654;</span> Meet Paratus (1 min 23 s)'
            '<button type="button" class="rl-xpl-share" data-xpl-share="/watch/paratus" aria-label="Share this explainer video">'
            '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/>'
            '<path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/></svg><span>Share</span></button></figcaption>\n'
            '<video controls playsinline preload="none" controlslist="nodownload noplaybackrate" disablepictureinpicture oncontextmenu="return false" '
            'poster="/videos/paratus/paratus-explainer.jpg" width="1280" height="720"><source src="/videos/paratus/paratus-explainer.mp4" type="video/mp4"></video>\n'
            + (f'<details class="rl-xpl-tr"><summary>Read the transcript</summary><p>{tr}</p></details>' if tr else "") + "</figure>"
            """<script>(function(){var b=document.querySelector('[data-xpl-share="/watch/paratus"]');if(!b)return;b.addEventListener('click',function(){
var u='https://renalcarematters.com/watch/paratus',l=b.querySelector('span');function done(m){l.textContent=m;setTimeout(function(){l.textContent='Share';},2200);}
if(navigator.share){navigator.share({title:'Meet Paratus',url:u}).catch(function(){});return;}
if(navigator.clipboard)navigator.clipboard.writeText(u).then(function(){done('Link copied');},function(){prompt('Copy this link',u);});else prompt('Copy this link',u);});})();</script>""")


def ready_main():
    rows = []
    for lvl, hubs in LEVEL.items():
        names = []
        for h in hubs:
            f = ACADEMY / f"{h}.html"
            if f.exists():
                t = re.search(r"<h1[^>]*>(.*?)</h1>", f.read_text(encoding="utf-8"), re.S)
                names.append(f'<a href="{h}.html">{re.sub(r"<[^>]+>", "", t.group(1)).strip() if t else h}</a>')
        rows.append(f"<tr><td><b>{lvl}</b></td><td>{', '.join(names)}</td></tr>")
    mods = "".join(f'<li><a href="{f}">Module {n}: {t}</a></li>' for n, (f, t) in sorted(MODS.items()))
    dmods = "".join(f'<li><a href="{f}">Module {n}: {t}</a></li>' for n, (f, t) in sorted(DMODS.items()))
    return f"""{hero('<span class="nc-cur">Emergency Readiness</span>', 'Emergency <em>Readiness</em>', 'Act, learn and practice for emergencies and disasters on the dialysis floor')}
{CSS}
<main class="container rl-main">
<section class="section" id="parts">
  <div class="section-tag">Cross-track section</div>
  <h2>Act, learn, practice</h2>
  <p>Emergency Readiness sits beside the role tracks because emergencies cut across every role. A nurse assistant starts compressions; a technician brings the defibrillator; the circuit nurse manages the machine; the physician-on-duty leads. When a typhoon, an earthquake or a fire hits, the same team keeps the patients on the machines safe and keeps every patient dialyzed until the unit reopens. There are two courses: one for the arrest at the chair, one for the events that harm many patients at once.</p>
{paratus_xpl()}
  <div class="rl-panels two">
    <a class="rl-panel act" href="emergency-cards.html">{tile("emergency-readiness-card.webp")}<div class="rl-act-t"><small>Act</small><b>Emergency Quick Cards</b><span>Nineteen one-screen action cards: the first minutes at the chair, plus power failure, earthquake, fire, a typhoon warning and water failure. Saved for use with no signal; open these during a real event.</span></div></a>
    <div class="rl-colh r1">Resuscitation: the arrest at the chair</div><div class="rl-colh r2">Disasters: events that harm many patients at once</div>
    <a class="rl-panel o2" href="{HUB}.html">{tile(HUB + "-card.webp")}<small>Learn</small><b>Dialysis Team Resuscitation Lab</b><span>Thirteen modules: the basic algorithms, algorithm recognition, BLS at the chair, adult ACLS-aligned care, arrest on the machine, hyperkalemia, children, ROSC and the team.</span></a>
    <a class="rl-panel dis o5" href="{DHUB}.html">{tile(DHUB + "-card.webp")}<small>Learn</small><b>Disaster Preparedness and Response</b><span>Twelve modules: why disasters hurt dialysis patients twice, the unit plan and command, ready patients, typhoons and floods, earthquakes, fire, power and water, heat and ashfall, keeping everyone dialyzed, reopening and drills.</span></a>
    <a class="rl-panel prac o3" href="{PRACTICE}">{tile(HUB + "-practice-card.webp")}<small>Practice</small><b>Megacode Practice Lab</b><span>Algorithm recognition rounds, timed megacodes, and a facilitator recorder with a shared monitor display for resuscitation drills.</span></a>
    <a class="rl-panel prac o6" href="{DPRACTICE}">{tile(DHUB + "-practice-card.webp")}<small>Practice</small><b>Disaster Drills</b><span>A tabletop simulator with timed injects, a call-down drill timer, and a printable evacuation and patient-accounting sheet.</span></a>
  </div>
{draft_cards_note()}
  <p>Also: the facilitator kits for <a href="{HUB}-trainer.html">resuscitation</a> and <a href="{DHUB}-trainer.html">disaster drills</a>, the <a href="../guides/calc-resuscitation-lab-toolkit.html">Resuscitation Lab toolkit</a>, and <a href="same-event-every-role.html">Same event, every role</a>.</p>
</section>
<section class="section" id="readiness">
  <div class="section-tag">Who needs which level</div>
  <h2>Resuscitation readiness by track</h2>
  <p>The table is an Academy recommendation. Two levels are verified Philippine rules: dialysis nurses hold a current BLS certificate, and the physician-on-duty and at least one nurse on every shift hold current ACLS from a DOH-accredited provider (DOH Administrative Order No. 2012-0001; Philippine Society of Nephrology 2024 guidelines). No DOH or PSN requirement for PALS in units that treat children was verified; it is shown as an Academy recommendation. Certificates come only from an authorized training center.</p>
  <div class="table-wrap"><table class="rl-matrix"><thead><tr><th>Level</th><th>Tracks</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>
  <h3>Disaster modules by role</h3>
  <div class="table-wrap"><table class="rl-matrix"><thead><tr><th>Role group</th><th>Disaster Preparedness and Response</th></tr></thead><tbody>
  <tr><td>Hemodialysis, charge and head nurses</td><td>All modules; Modules 6 to 8 hands-on; emergency take-off drill passed</td></tr>
  <tr><td>Safety nurse (or head nurse)</td><td>All modules, plus the Module 12 facilitator capstone</td></tr>
  <tr><td>Physician-on-duty, Dialysis Clinical Head, attending nephrologist</td><td>Modules 1, 3, 5, 8, 10, 11</td></tr>
  <tr><td>Technicians (dialysis, water treatment, biomedical, reprocessing)</td><td>Modules 1, 2, 6, 7, 8, 11</td></tr>
  <tr><td>Nurse assistants, support staff</td><td>Modules 1, 6, 7; the evacuation drill</td></tr>
  <tr><td>Unit manager, unit owner</td><td>Modules 1, 2, 3, 10, 11, 12</td></tr>
  <tr><td>Social worker, records officer, dietitian</td><td>Modules 1, 3, 4, 10</td></tr>
  </tbody></table></div>
</section>
<section class="section" id="modules">
  <div class="section-tag">Learn</div>
  <h2>The modules</h2>
  <h3><a href="{HUB}.html">Dialysis Team Resuscitation Lab</a></h3>
  <ul class="rl-list">{mods}</ul>
  <h3><a href="{DHUB}.html">Disaster Preparedness and Response</a></h3>
  <ul class="rl-list">{dmods}</ul>
</section>
<section class="section" id="drills">
  <div class="section-tag">Who runs the drills</div>
  <h2>Every drill has an owner, a facilitator and a record</h2>
  <p>A drill with no named owner does not happen. The table is the Academy&rsquo;s suggested division of work; your unit may assign it differently, but every row needs a name and a deputy for leave and night shifts.</p>
  <div class="table-wrap"><table class="rl-matrix"><thead><tr><th>Drill</th><th>Owns the schedule</th><th>Runs it (facilitator)</th><th>Takes part</th><th>Signs the record</th></tr></thead><tbody>
  <tr><td colspan="5"><b>Resuscitation (Dialysis Team Resuscitation Lab)</b></td></tr>
  <tr><td>Weekly five-minute refresher at handover</td><td>Head nurse</td><td>Charge nurse on the shift</td><td>Everyone on that shift</td><td>Charge nurse</td></tr>
  <tr><td>Monthly megacode</td><td>Head nurse</td><td>Charge nurse or physician-on-duty with current Advanced Cardiovascular Life Support (ACLS); Pediatric Advanced Life Support (PALS) for a pediatric case</td><td>The shift team in rotating roles, plus a named watcher</td><td>Head nurse</td></tr>
  <tr><td>Quarterly integrated megacode</td><td>Dialysis Clinical Head</td><td>Unit educator or a certified Basic Life Support (BLS) or ACLS instructor</td><td>Nurses, technicians, nursing assistants, physician-on-duty</td><td>Dialysis Clinical Head</td></tr>
  <tr><td>Same-day debrief after a real resuscitation</td><td>Charge nurse</td><td>Charge nurse or physician-on-duty</td><td>Everyone involved</td><td>Head nurse; system findings to the Dialysis Clinical Head</td></tr>
  <tr><td colspan="5"><b><a href="{DHUB}.html">Disaster Preparedness and Response</a></b></td></tr>
  <tr><td>Patient call-list check (call-down drill), before typhoon season</td><td>Unit manager</td><td>Safety nurse (or head nurse)</td><td>Charge nurses, records officer, social worker</td><td>Unit manager</td></tr>
  <tr><td>Disaster tabletop exercise, before typhoon season</td><td>Unit manager</td><td>Safety nurse (or head nurse), with the Dialysis Clinical Head leading the clinical decisions</td><td>Head nurse, charge nurses, technicians (water and power), biomedical technician, social worker, records officer</td><td>Unit manager; findings to the unit owner</td></tr>
  <tr><td>Power-loss and blood-return-without-power drill, twice a year</td><td>Head nurse</td><td>Safety nurse (or head nurse) with the biomedical technician</td><td>Nurses and technicians on the shift, at an empty station</td><td>Head nurse</td></tr>
  <tr><td>Earthquake drill, timed with the quarterly Nationwide Simultaneous Earthquake Drill (NSED) where possible</td><td>Unit manager</td><td>Safety nurse (or head nurse)</td><td>Whole shift; patients take part only in the &ldquo;protect in place&rdquo; step if they agree</td><td>Unit manager</td></tr>
  <tr><td>Evacuation and patient-accounting drill, yearly</td><td>Unit manager</td><td>Safety nurse (or head nurse), with the building or facilities officer</td><td>Whole shift, with no patients on machines</td><td>Unit manager; findings to the unit owner</td></tr>
  <tr><td>Same-day debrief after a real disruption</td><td>Unit manager</td><td>Safety nurse (or head nurse) or Dialysis Clinical Head</td><td>Everyone involved</td><td>Unit manager; system findings to the unit owner</td></tr>
  </tbody></table></div>
  <h3>Who facilitates disaster preparedness and response</h3>
  <p>The facilitator is the unit&rsquo;s <a href="special-dialysis-nurse-roles-07-safety-and-emergency-preparedness.html">safety nurse</a> (Special Dialysis Nurse Roles, Module 7): the nurse designated to plan, check readiness and run drills. Most units have not yet designated one; until they do, the head nurse facilitates, and naming a safety nurse is recommended. Three people stand behind that role. The <b>unit manager</b> owns the disaster plan, the drill schedule, the receiving-unit agreements and the budget. The <b>Dialysis Clinical Head</b> leads the clinical decisions in a tabletop: who dialyzes early before a storm, who is placed first when the roster must move, and the emergency diet with the dietitian. The <b>unit owner</b> receives the findings and funds the fixes. During a real event the safety nurse does not command: the charge nurse and the physician direct the response, and licensed engineers and technicians handle the building, water and machines.</p>
  <p>A hospital-based unit runs its drills inside the hospital&rsquo;s own disaster plan and emergency preparedness committee, built under the Department of Health&rsquo;s National Policy on Disaster Risk Reduction and Management in Health (DRRM-H), Administrative Order No. 2019-0046, and the Hospitals Safe from Disasters policy, Administrative Order No. 2013-0014. A freestanding unit should still coordinate with its city or municipal disaster risk reduction and management office, set up under Republic Act No. 10121, for evacuation routes and community warnings. Who must attend which drill is a unit decision; this page does not state a licensing requirement.</p>
  <p><b>Two rules for every drill.</b> No drill on a working floor without a named watcher whose only job is the patients still dialyzing. Every system problem a drill finds gets an owner and a date, the same as a problem found in a real event.</p>
  <p><b>The practice record.</b> For each drill: the date, the scenario, who took which role, the one or two learning goals and whether they were met, the timeline, and each action with its owner and date. The head nurse keeps resuscitation records and the unit manager keeps disaster records; the Dialysis Clinical Head reviews both each quarter, with any real events.</p>
</section>
<section class="section" id="cadence">
  <div class="section-tag">Practice</div>
  <h2>A practice rhythm for the unit</h2>
  <p>Onboarding: Modules 1 to 4 and 7, a crash-cart and defibrillator orientation, an observed BLS check, one team scenario. Weekly: a five-minute refresher at handover. Monthly: one megacode on the shared display, with a five-question debrief. Quarterly: an integrated megacode with role rotation and the facilitator recorder. After any real event or equipment change: a targeted rehearsal. Disaster drills: a call-down check and a tabletop exercise before typhoon season, a power-loss drill twice a year, an earthquake drill with the quarterly NSED, and an evacuation drill yearly. This cadence is an Academy teaching choice; studies support spaced practice but do not define the best interval for a dialysis unit.</p>
  <div class="alert alert-amber"><div class="alert-icon">⚠️</div><div class="alert-body"><h4>Not certification</h4><p>The Emergency Readiness section is an educational reviewer and practice resource. It is not an American Heart Association course, it gives no BLS, ACLS or PALS certification, and online completion does not establish hands-on competence. Your unit protocol, crash-cart stock and machine manufacturer&rsquo;s instructions govern every real event; always ask the attending nephrologist for guidance.</p></div></div>
</section>
</main>"""


# Role rotation and role cards (Practice Lab; Dr. Rivero, Nov 28 2026)
ROT = '''<section class="section" id="rotation">
  <div class="section-tag">4 &middot; Role rotation</div>
  <h2>Rotate the roles: everyone practices every role in their scope</h2>
  <p>In a real arrest the roles go to whoever is on the shift. The roster changes, night and Sunday shifts are thin, and small teams combine roles (Module 13). The person who always records may be the only one free to compress; the nurse who always compresses becomes the circuit nurse the day her own patient collapses. A role you have only watched is a role you will hesitate in. So the Academy asks every unit to rotate the roles in its drills, drill after drill, until everyone has held every role their license and training allow.</p>
  <div class="rl-why-grid">
    <div><b>Every role has a failure that only practice fixes.</b> In the Module 13 case, two physicians gave conflicting orders for a minute, one dose of epinephrine was given twice because orders went to the room, and the watcher was pulled into compressions while another patient&rsquo;s blood pressure fell unnoticed for ten minutes. Each failure belongs to a role: the leader handover, the recorder, the watcher.</div>
    <div><b>Each role teaches the others.</b> A leader who has compressed knows that compressors tire within about two minutes, before they notice. A compressor who has led knows why every pause has to stay under 10 seconds. A recorder who has given drugs knows what the leader needs called before anyone asks.</div>
    <div><b>Rotation tests the unit, not just the people.</b> A new person in a role finds what the regular one quietly works around: pads stored out of reach, a drug box only one nurse can open, a recliner that sticks halfway, an ambulance number that is no longer posted.</div>
    <div><b>It lets the huddle assign anyone.</b> Roles are named at the start of every shift from the real roster (Module 1). When everyone has practiced every role in their scope, the charge nurse can fill the roles from whoever came to work.</div>
  </div>
  <h3>How to rotate</h3>
  <ol class="rl-rules">
    <li><b>Rotate within scope.</b> Leading follows your unit protocol: the physician-on-duty, and the nurse with current Advanced Cardiovascular Life Support (ACLS) until the physician arrives. Medicines and the manual defibrillator go only to staff whose license and unit protocol allow them; an automated external defibrillator (AED) is for any trained staff member. Airway, circuit nurse and watcher are nursing roles (a trained technician may be circuit nurse where your protocol allows). Compressions, recording and running are for every person trained in Basic Life Support (BLS), including technicians and assistants.</li>
    <li><b>Everyone compresses.</b> Compressors swap at every two-minute rhythm check, or sooner if tiring. In any drill longer than a few minutes, every free BLS-trained person takes a turn, whatever their named role.</li>
    <li><b>A new role each drill.</b> Nobody holds the same role two drills running. The planner below spreads the roles so that over a series of drills everyone holds every role in their scope at least once.</li>
    <li><b>Build in a leader handover.</b> Often enough that it is routine, let the ACLS-current nurse lead the first minutes and hand over when the physician-on-duty &ldquo;arrives&rdquo;: a 15-second summary, &ldquo;I am taking the lead,&rdquo; &ldquo;You have the lead.&rdquo;</li>
    <li><b>The watcher rotates too, and watches real patients.</b> On a working floor nobody plays the watcher: the watcher&rsquo;s job is the patients still dialyzing, and the watcher never joins the drill.</li>
    <li><b>Record who held which role.</b> The practice record lists the roles for every drill (see the Emergency Readiness page). The head nurse keeps it, and the Dialysis Clinical Head reviews coverage each quarter: who has not yet led, recorded, run the circuit or watched.</li>
  </ol>
  <p class="rl-note">Rotation is an Academy teaching choice, not a guideline requirement. Studies support repeated, spaced team practice but do not set a rotation schedule; your unit decides the pace.</p>
  <h3>Rotation planner</h3>
  <p>Enter initials only. The planner fills the scarce roles first (leader, medicines and defibrillator, the nursing roles), gives each person the role they have held least, never repeats a role two drills running when anyone else can take it, and marks a role &ldquo;combine&rdquo; when there are not enough people (combine as in Module 13). Choose a drill and send its roles to the recorder above.</p>
  <div id="rl-rot" class="rl-host"><noscript><p>The rotation planner needs JavaScript.</p></noscript></div>
</section>'''

def card(n, rid, title, who, combine, blocks, mod):
    h = f'<article class="rl-rc" id="role-{rid}" data-role="{title}"><header><span class="rl-rc-n">{n}</span><h3>{title}</h3><span class="rl-rc-held">Held by: <b data-held>&nbsp;</b></span></header>'
    h += f'<p class="rl-rc-who"><b>Who holds it:</b> {who}' + (f' <b>Small team:</b> {combine}' if combine else '') + '</p>'
    for head, cls, items in blocks:
        h += f'<h4>{head}</h4><ul class="{cls}">' + "".join(f"<li>{i}</li>" for i in items) + "</ul>"
    h += f'<p class="rl-rc-mod">Taught in {mod}.</p></article>'
    return h

CARDS = [
 card(0, "first", "Everyone: the first person at the chair", "Whoever reaches the patient first: nurse, technician, assistant, physician or clerk.", "",
  [("When a patient slumps", "", ["Check in 10 seconds: unresponsive, not breathing normally (gasping is not breathing), no definite pulse.",
     "Shout for help and call the code so the whole unit hears it; the runner calls the ambulance at once.",
     "Flatten the recliner and start compressions; do not wait for the defibrillator or the physician.",
     "Hand over to the named roles as they arrive, and take the role the leader gives you."]),
   ("Say it aloud", "rl-say", ["&ldquo;Code at Station 7! Call the ambulance! Bring the cart!&rdquo;"]),
   ("Never", "rl-never", ["Treat the pressure first: in arrest, saline before compressions wastes the critical minute.",
     "Take gasping for breathing."])], "Modules 3 and 4"),
 card(1, "leader", "Leader", "The physician-on-duty; the ACLS-current nurse leads until the physician arrives.", "Leader plus defibrillator and drugs when only three staff are present.",
  [("Before the shift", "", ["Run the two-minute role huddle from the real roster; confirm an ACLS-current nurse is present.",
     "Know where the highest-risk patients sit, the ambulance number and the realistic travel time."]),
   ("When the code is called", "", ["Name every role aloud, combining roles safely for the team size.",
     "Stay hands-off whenever staffing allows, so you can see the whole room.",
     "Call each rhythm check and keep it under 10 seconds; decide shock or no shock by the algorithm.",
     "Give every order to a named person and wait for the read-back.",
     "Decide with the circuit nurse on the blood; decide whether compressions can continue in the chair.",
     "Think of the dialysis causes taught in Modules 8 and 9: high potassium, and the circuit (air, hemolysis, a reaction, a needle out)."]),
   ("Say it aloud", "rl-say", ["&ldquo;Stop compressions. Rhythm check.&rdquo;",
     "When another leader arrives, give the 15-second summary: time down, rhythms, shocks, drugs and times, circuit status, suspected cause.",
     "The new leader: &ldquo;I am taking the lead.&rdquo; You: &ldquo;You have the lead,&rdquo; then take a named role."]),
   ("Never", "rl-never", ["Give orders to the room.", "Let two leaders give orders at once.", "Pull the watcher into the arrest."])], "Modules 1, 3, 5, 8, 9 and 13"),
 card(2, "compressor", "Compressors 1 and 2", "Any BLS-trained staff, including technicians and assistants.", "Compressor 2 also takes the airway, swapping every two minutes.",
  [("Start", "", ["Flatten the recliner fully; if it sticks halfway, compress as flat as it goes while someone works the mechanism.",
     "Slide a backboard under when a second person is free; kneel on the chair edge or use a step stool to lock your elbows.",
     "Never move a connected patient until the circuit nurse says the lines are safe."]),
   ("Compress", "", ["5 to 6 cm deep, 100 to 120 a minute, full recoil: do not lean.",
     "30 compressions to 2 breaths until an advanced airway is placed.",
     "Keep compressing while the pads go on and while the defibrillator charges.",
     "Swap at every two-minute rhythm check, or sooner if tiring, with the next compressor ready beside the chair."]),
   ("Say it aloud", "rl-say", ["&ldquo;Charging, continue compressions.&rdquo;", "After the shock: &ldquo;Compressions.&rdquo;", "&ldquo;Swap at the next check.&rdquo;"]),
   ("Never", "rl-never", ["Stop for the machine.", "Touch the patient, chair, lines or machine after &ldquo;Everyone clear.&rdquo;"])], "Module 4"),
 card(3, "airway", "Airway", "A nurse or physician.", "Combined with compressor 2.",
  [("Ventilate", "", ["Bag-valve-mask with oxygen attached; two people when possible: one holds the mask with both hands and lifts the jaw into it, the other squeezes slowly over about one second.",
     "Give just enough to see the chest rise; give the 2 breaths in each 30:2 pause."]),
   ("When it does not work", "", ["Chest does not rise: two-hand seal, head tilt and jaw lift, an oral airway in an unresponsive patient.",
     "Stomach swells: smaller, slower breaths.", "Vomit: turn the head if safe, suction, continue."]),
   ("Never", "rl-never", ["Give large, fast breaths: they fill the stomach and cut blood return to the heart."])], "Module 4"),
 card(4, "defib", "Defibrillator and drugs", "The ACLS-current nurse for the manual defibrillator and medicines; any trained staff member for an AED.", "Combined with the leader when only three staff are present.",
  [("Defibrillator", "", ["Bring the cart; put the pads on while compressions continue: anterolateral or front-and-back, on dry skin, clear of the catheter exit site, dressings and the access arm.",
     "Check the chair, blanket and floor are dry; move wet drapes.",
     "Charge during compressions (manual), then clear and shock; compressions restart at once."]),
   ("Medicines", "", ["Only on a named order from the leader, read back, and only within your license and the unit protocol.",
     "Use the port the circuit nurse names (the secured venous needle or a catheter limb after the lock is aspirated); flush after each drug.",
     "Report each drug as done, with the time, for the recorder."]),
   ("Say it aloud", "rl-say", ["&ldquo;Pads on.&rdquo;", "&ldquo;Everyone clear: patient, chair, lines, machine. Shocking.&rdquo;",
     "Read-back: &ldquo;Epinephrine 1 milligram IV.&rdquo; Done: &ldquo;Epinephrine 1 milligram in, 10:43.&rdquo;"]),
   ("Never", "rl-never", ["Shock while anyone touches the lines or the machine.", "Give a drug ordered &ldquo;to the room.&rdquo;",
     "Push a catheter lock (heparin or citrate) into the patient."])], "Modules 4, 5 and 7"),
 card(5, "circuit", "Circuit nurse", "The patient&rsquo;s own dialysis nurse, who knows the access, the fluid removed and the machine (a trained technician where your protocol allows).", "Becomes the recorder once the circuit is safe.",
  [("First minute", "", ["Stop fluid removal at once.", "Make the blood decision: return the blood with saline, or clamp and disconnect. Air, hemolysis, a severe reaction or an open line end forbid returning it.",
     "Stop the blood pump when the decision requires it; the amount and speed of saline follow your unit protocol and the leader.",
     "Announce the decision once, clearly, so the recorder writes it with the time."]),
   ("Before every shock", "", ["When in doubt, clamp and disconnect before the first shock: it takes seconds.",
     "Let go of the lines when the leader calls &ldquo;clear&rdquo;; never delay a shock for VF to finish disconnecting."]),
   ("Access for drugs", "", ["Keep the venous needle secured and flushed, and tell the leader which port to use.",
     "Catheter: aspirate the lock first (at least the limb volume printed on the clamp), flush, give, flush, clamp.",
     "No peripheral IV in the fistula arm unless the leader decides it is the last resort."]),
   ("Say it aloud", "rl-say", ["&ldquo;Fluid removal off.&rdquo;", "&ldquo;Blood returned.&rdquo; or &ldquo;Clamped, not returned.&rdquo;"]),
   ("Never", "rl-never", ["Interrupt compressions or cross the compressor to reach the machine.", "Leave the circuit to fetch equipment."])], "Module 7"),
 card(6, "recorder", "Recorder and timer", "Any staff member who can write and keep time.", "Combined with the runner.",
  [("During the arrest", "", ["Start the clock when the code is called; write every action with its time on the code record sheet.",
     "Call the two-minute rhythm checks and the drug intervals before they are due.",
     "Write the blood decision and every drug as it is reported done, so no dose is given twice.",
     "Give the leader the timeline for the 15-second summary and the ambulance handover."]),
   ("Say it aloud", "rl-say", ["&ldquo;Two minutes: rhythm check.&rdquo;", "&ldquo;Next epinephrine due 10:47.&rdquo;"]),
   ("After", "", ["Bring the sheet to the debrief: it is the first question, &ldquo;What happened?&rdquo;"]),
   ("Never", "rl-never", ["Be a passive scribe: the recorder keeps the clock and calls what is due next."])], "Module 13"),
 card(7, "watcher", "Watcher", "A nurse who stays with the other patients.", "Never combined with the arrest.",
  [("During the arrest", "", ["Stay with every other connected patient: pressures, alarms, needles and lines.",
     "Answer the other machines&rsquo; alarms and keep the other patients calm.",
     "Tell the charge nurse at once if another patient needs help."]),
   ("In a drill", "", ["On a working floor the watcher watches the real patients; nobody plays this role."]),
   ("Never", "rl-never", ["Join the compressions, even when asked: in the Module 13 case another patient&rsquo;s pressure fell unnoticed for ten minutes."])], "Modules 1 and 13"),
 card(8, "runner", "Runner", "A technician, assistant or clerk.", "Combined with the recorder.",
  [("When the code is called", "", ["Call the ambulance at once, not after the first rhythm check; the numbers are posted where you will look.",
     "Fetch what the leader asks for: oxygen, suction, extra supplies.",
     "Call the physician-on-duty or the attending nephrologist as your unit protocol says.",
     "Meet the ambulance at the door, guide the crew to the chair, and bring what the unit agreed to send with the patient."]),
   ("Never", "rl-never", ["Wait for the leader to ask before calling the ambulance."])], "Modules 1 and 12"),
]

ROLES = '''<section class="section" id="roles">
  <div class="section-tag">5 &middot; Role cards</div>
  <h2>What each role does</h2>
  <p>One card per role: who holds it, what to do and say, and what never to do. Read your card before every drill, then read a card you have never held. The names written into the recorder&rsquo;s roles appear on the cards when you print them, so each person can hold their card during the drill. Doses and energies follow your unit protocol and the 2025 American Heart Association (AHA) guidelines taught in the modules; give medicines only within your license.</p>
  <div class="rl-rbar"><button type="button" class="rl-btn rl-print-rc">Print the role cards</button></div>
  <div class="rl-rcs">''' + "\n".join(CARDS) + '''</div>
  <p class="rl-note">The cards summarize the modules for drills. They do not replace your unit protocol, the crash-cart dose card or the instructions of the attending nephrologist.</p>
</section>'''


def practice_main(rec, cases):
    mods = "".join(f'<li><a data-rl-mod="{n}" href="{f}">Module {n}: {t}</a></li>' for n, (f, t) in sorted(MODS.items()))
    mc = "".join(f'<li><a href="{c["page"]}#sim">{c["title"]}</a> <small>(Module {int(c["page"].split("-")[2])})</small></li>' for c in cases)
    rec_j = json.dumps(rec, ensure_ascii=False).replace("</", "<\\/")
    cases_j = json.dumps(cases, ensure_ascii=False).replace("</", "<\\/")
    return f"""{hero(f'<a href="{READY}">Emergency Readiness</a><span class="nc-sep">›</span><span class="nc-cur">Megacode Practice Lab</span>', 'Megacode Practice <em>Lab</em>', 'Recognize the algorithm, run the megacode, record the drill')}
{CSS}
<main class="container rl-main">
<section class="section" id="sample">
  <div class="section-tag">Start here &middot; a sample case</div>
  <h2>How to use the Megacode Practice Lab: collapse at Station 7</h2>
  <p>One fictional event, run through the three tools in the order a team uses them. Tuesday, 9:40 a.m.: Mr. Arnel Gutierrez, 61, two hours into dialysis, collapses in the chair. First you learn to name the algorithm, then you run the event against the clock, then the unit drills it together and debriefs from the log.</p>
  <div class="rl-sample-box"><ol class="rl-steps">
    <li><b>Recognize the algorithm.</b> Recognition rounds mix six kinds of item. Below is one of each, fully answered, with the reason for every choice: what Practice mode shows you after each answer.
      <div id="rl-sample-item" class="rl-sitem"></div>
      <button type="button" class="rl-btn rl-ghost" data-rl-sample="rec">Go to a practice round</button></li>
    <li><b>Run it against the clock.</b> The same event is the timed megacode &ldquo;Collapse at Station 7&rdquo; (Module 5). You lead until the physician-on-duty returns; each decision has a time budget, and the feedback and timeline wait until the end.
      <br><button type="button" class="rl-btn" data-rl-sample="mcw" data-case="rl05-station-7">Show the worked megacode</button> <button type="button" class="rl-btn rl-ghost" data-rl-sample="mc" data-case="rl05-station-7">Run it myself, timed</button></li>
    <li><b>Drill it with the team.</b> On the unit, the facilitator writes initials into the roles, starts the clock and taps each action as it happens; the shared display shows the monitor on a second screen. Load the worked sample to see the roles filled in, a finished log of twenty actions, the summary (first compression, pads, first shock, fluid removal off, compression fraction, longest pause), the monitor set for the drill, and how the facilitator reads it in the debrief. In the next drill, rotate: the planner in section 4 gives everyone a new role, and section 5 has a card for each role.
      <br><button type="button" class="rl-btn" data-rl-sample="log">Load the worked drill</button></li>
  </ol>
  <p class="rl-note">Names, initials and times in the sample are fictional. Your unit protocol and the attending nephrologist decide every real event.</p></div>
</section>
<section class="section" id="recognition">
  <div class="section-tag">1 &middot; Algorithm recognition</div>
  <h2>Which algorithm are we in?</h2>
  <p>Recognition is its own skill. These rounds mix short vignettes, rhythm strips with patient findings, missing assessments, step ordering, unsafe actions and patients who change. A rhythm strip never appears without findings at the patient, because a trace alone cannot show a pulse, perfusion or stability. Practice mode explains every answer; the timed round gives 30 seconds an item and explains at the end; <i>Repeat my misses</i> brings back what you got wrong. Results stay on this device.</p>
  <div id="rl-rec" class="rl-host"><noscript><p>The recognition trainer needs JavaScript.</p></noscript></div>
</section>
<section class="section" id="megacodes">
  <div class="section-tag">2 &middot; Megacodes</div>
  <h2>Timed megacodes</h2>
  <p>The same seventeen megacodes that sit in the modules, run here against the clock: each decision has a time budget, feedback waits until the end, and the debrief shows a timestamped timeline with the reasoning for every choice, through to return of spontaneous circulation (ROSC) and handover. Run a megacode guided in its module first, then timed here, then as a facilitated team drill. Simulation success is an educational result, not a prediction of patient survival.</p>
  <div id="rl-mc" class="rl-host"></div>
  <details><summary>All megacodes, guided in their modules</summary><ul class="rl-list">{mc}</ul></details>
</section>
<section class="section" id="facilitator">
  <div class="section-tag">3 &middot; Facilitated unit drill</div>
  <h2>Facilitator recorder and shared display</h2>
  <p>For a drill with your real team and equipment: assign roles from the roster, start the clock, tap each action as it happens, and copy the log into the <a href="../guides/calc-resuscitation-lab-toolkit.html#tool-2">timeline analyzer</a> for the debrief. The shared display shows a monitor on a second screen while you control it privately. Scripts, role cards, the observation checklist and the debrief prompts are in the <a href="{HUB}-trainer.html">facilitator kit</a>. Protect the real patients: drill at an empty station with a named watcher.</p>
  <div id="rl-recorder" class="rl-host"></div>
</section>
{ROT}
{ROLES}
<section class="section" id="links">
  <div class="section-tag">Where each topic is taught</div>
  <h2>Modules</h2>
  <ul class="rl-list">{mods}</ul>
</section>
</main>
<script type="application/json" id="rl-rec-data">{rec_j}</script>
<script type="application/json" id="rl-cases-data">{cases_j}</script>"""


def disaster_practice_main(tt, cases):
    mods = "".join(f'<li><a href="{f}">Module {n}: {t}</a></li>' for n, (f, t) in sorted(DMODS.items()))
    cs = "".join(f'<li><a href="{c["page"]}#sim">{c["title"]}</a> <small>(Module {int(c["page"].split("-")[2])})</small></li>' for c in cases)
    tt_j = json.dumps(tt, ensure_ascii=False).replace("</", "<\\/")
    return f"""{hero(f'<a href="{READY}">Emergency Readiness</a><span class="nc-sep">›</span><a href="{DHUB}.html">Disaster Preparedness and Response</a><span class="nc-sep">›</span><span class="nc-cur">Disaster Drills</span>', 'Disaster <em>drills</em>', 'Run the tabletop, test the call list, print the evacuation sheet')}
{CSS}
<main class="container rl-main">
<section class="section" id="sample">
  <div class="section-tag">Start here &middot; a sample case</div>
  <h2>How to use the drills: a sample typhoon week</h2>
  <p>A fictional 24-station unit runs all three tools before and during typhoon season. Each sample below is fully worked: load it to see the finished result and how the facilitator reads it, then clear it and run your own.</p>
  <div class="rl-sample-box"><ol class="rl-steps">
    <li><b>Run the tabletop.</b> The facilitator picks &ldquo;Typhoon: Signal No. 3 by Thursday,&rdquo; starts the clock and reads each inject aloud; the team decides out loud, and the recorder taps each action as it is said. The sample shows six injects over about 40 minutes, the actions the team said with how long each took, two actions nobody said, and the timeline for the hot wash.
      <br><button type="button" class="rl-btn" data-dp-sample="dp-tt">Load the worked exercise</button></li>
    <li><b>Test the call list.</b> Enter how many people are on the list, start the drill, and tap one outcome per call. The sample: 58 people, 53% reached within 2 hours, 76% within 6 hours and 90% within 24 hours, with 3 wrong numbers to fix before the season.
      <br><button type="button" class="rl-btn" data-dp-sample="dp-call">Load the worked call-down</button></li>
    <li><b>Print the evacuation sheet.</b> Make the sheet from your chair count and print it blank for every shift; the charge nurse fills in mobility and helpers at the start of the shift. The sample shows a 12-station sheet filled during a fire drill.
      <br><button type="button" class="rl-btn" data-dp-sample="dp-evac">Show the worked sheet</button></li>
  </ol>
  <p class="rl-note">Every number, initial and time in the samples is fictional. The call-down sample is kept on this device like a real drill; press Clear to remove it.</p></div>
</section>
<section class="section" id="tabletop">
  <div class="section-tag">1 &middot; Tabletop simulator</div>
  <h2>Disaster tabletop simulator</h2>
  <p>For a facilitator and a team around one screen. Pick a scenario (typhoon, earthquake, fire, long power outage, ashfall) and start the clock. Injects arrive on the exercise clock, or when the facilitator releases them. The facilitator reads each inject aloud, the team decides out loud, and the recorder taps each action as it is said. At the end, a timeline shows each inject, the actions recorded and how long they took, against the scenario&rsquo;s teaching points: the evidence for the hot wash and the after-action report (Module 12). <b>Shared display</b> shows the current inject full screen. No individual is scored, and nothing leaves this device.</p>
  <div id="dp-tt"><noscript><p>The tabletop simulator needs JavaScript.</p></noscript></div>
  <p class="rl-note">Run it with a named watcher if any patients are still dialyzing (the watcher rule). The scenarios follow the modules; your unit protocol and the attending nephrologist decide every real event.</p>
</section>
<section class="section" id="calldown">
  <div class="section-tag">2 &middot; Call-down drill</div>
  <h2>Call-down drill timer</h2>
  <p>Test the call list before typhoon season. The safety nurse (or head nurse) starts the timer, the team phones every person on the list, and each call is marked: reached, message left, no answer, wrong number, or not able to come. The timer reports the share reached within 2, 6 and 24 hours and the wrong numbers to fix. It counts outcomes only: no names or phone numbers are entered, and the counts stay on this device. The 24-hour figure is your unit&rsquo;s own measure; no external standard is claimed.</p>
  <div id="dp-call"></div>
</section>
<section class="section" id="evacuation">
  <div class="section-tag">3 &middot; Evacuation sheet</div>
  <h2>Evacuation and patient-accounting sheet</h2>
  <p>A one-page sheet made from your chair count: each station&rsquo;s mobility category (walks alone, walks with help, wheelchair, stretcher), the assigned helper, the time off by staff, and a check-off column for the census nurse at the assembly point. Print it blank and fill it in at the start of every shift. Nothing is stored online; the filled sheet is a unit record under the Data Privacy Act.</p>
  <div id="dp-evac"></div>
</section>
<section class="section" id="cases">
  <div class="section-tag">Interactive cases</div>
  <h2>Ten branching cases, one in each module</h2>
  <p>Each case puts you on the shift with a unit board (time, alert, power, water, patients on machines, staff, roads) and asks for one decision at a time. Every case has at least one choice that breaks a hard rule, so you can see why the rule exists.</p>
  <ul class="rl-list">{cs}</ul>
</section>
<section class="section" id="links">
  <div class="section-tag">Where each topic is taught</div>
  <h2>Modules</h2>
  <ul class="rl-list">{mods}</ul>
  <p>The drill program, the facilitator&rsquo;s role and the observed stations are in the <a href="{DHUB}-trainer.html">facilitator kit</a>.</p>
</section>
</main>
<script type="application/json" id="dp-tt-data">{tt_j}</script>"""


BOLT = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M13 2 4 14h7l-1 8 9-12h-7z"/></svg>'


LAND = f"""{LS}
<style id="rl-landing-css">
/* Emergency Readiness drawer (Dr. Rivero, Nov 28 2026: a left drawer above Schola, not boxes on the page) */
.erd-tab{{position:fixed;z-index:9996;left:0;top:50%;transform:translateY(calc(-100% - 66px));display:flex;flex-direction:column;align-items:center;gap:8px;
  padding:12px 7px;border:0;border-radius:0 12px 12px 0;background:#B91C1C;color:#fff;cursor:pointer;box-shadow:4px 6px 20px rgba(15,30,46,.25);}}
.erd-tab:hover{{background:#991b1b;}}
.erd-tab svg{{width:26px;height:26px;}}
.erd-tab span{{writing-mode:vertical-rl;transform:rotate(180deg);font:700 13px Inter,system-ui,sans-serif;letter-spacing:.04em;}}
.erd-scrim{{position:fixed;inset:0;z-index:100000;background:rgba(10,18,32,.45);opacity:0;pointer-events:none;transition:opacity .2s;}}
.erd-scrim.erd-open{{opacity:1;pointer-events:auto;}}
.erd{{position:fixed;z-index:100001;top:0;left:0;bottom:0;width:min(460px,94vw);overflow-y:auto;overscroll-behavior:contain;box-sizing:border-box;
  background:var(--white);color:var(--text);border-right:1px solid var(--border);border-radius:0 16px 16px 0;box-shadow:6px 0 28px rgba(15,30,46,.18);
  padding:20px 22px calc(24px + env(safe-area-inset-bottom,0px));transform:translateX(-105%);visibility:hidden;transition:transform .22s ease,visibility 0s linear .22s;
  font-family:"Nunito Sans",system-ui,-apple-system,"Segoe UI",Arial,sans-serif;}}
.erd.erd-open{{transform:none;visibility:visible;transition:transform .22s ease;}}
.erd-head{{display:flex;gap:14px;align-items:center;margin-bottom:8px;}}
.erd-hic{{flex:none;width:44px;height:44px;border-radius:11px;background:#B91C1C;color:#fff;display:flex;align-items:center;justify-content:center;}}
.erd-hic svg{{width:26px;height:26px;}}
.erd-head h2{{font:800 21px/1.2 Inter,Manrope,system-ui,sans-serif;color:var(--text);margin:0 0 3px;}}
.erd-head p{{margin:0;color:var(--text-mid);font-size:15px;line-height:1.4;}}
.erd-x{{margin-left:auto;align-self:flex-start;border:0;background:none;font-size:28px;line-height:1;color:var(--text-muted);cursor:pointer;padding:0 4px;}}
.erd-k{{font:800 12px Inter,system-ui,sans-serif;letter-spacing:.09em;text-transform:uppercase;color:var(--text-muted);margin:18px 0 8px;}}
.erd-card{{display:block;text-decoration:none;color:var(--text);border:1px solid var(--border);border-left:5px solid var(--teal);border-radius:12px;padding:11px 14px;margin:0 0 9px;}}
.erd-card:hover{{border-color:var(--teal);}}
.erd-card b{{display:block;font:800 16px/1.25 Inter,system-ui,sans-serif;color:var(--teal);margin-bottom:3px;}}
.erd-card .t{{display:block;font-size:14px;line-height:1.45;color:var(--text-mid);}}
.erd-card.erd-act{{background:var(--red-soft);border-color:rgba(185,28,28,.25);border-left-color:var(--red);}}
.erd-card.erd-act b{{color:var(--red);}}
.erd-get{{display:flex;align-items:center;gap:12px;margin:14px 0 4px;padding:12px 14px;border-radius:14px;text-decoration:none;color:#fff;
  background:linear-gradient(135deg,#b91c1c,#7f1d1d);box-shadow:0 6px 18px rgba(127,29,29,.28);}}
.erd-get:hover{{filter:brightness(1.06);}} .erd-get img{{flex:none;border-radius:10px;box-shadow:0 0 0 2px rgba(255,255,255,.35);}}
.erd-get b{{display:block;font:800 16px Inter,system-ui,sans-serif;color:#fff;}} .erd-get small{{display:block;font-size:13px;line-height:1.45;color:#fee2e2;margin-top:2px;}}
.erd-home{{display:inline-block;margin-top:10px;font:700 14.5px Inter,system-ui,sans-serif;color:var(--teal);text-decoration:none;}}
html[data-theme="dark"] .erd-card b,html[data-theme="dark"] .erd-home{{color:var(--text);}}
html[data-theme="dark"] .erd-card.erd-act b{{color:#f4a3a3;}}
@media (max-width:640px){{.erd-tab{{top:auto;left:24px;transform:none;bottom:calc(156px + env(safe-area-inset-bottom,0px));width:44px;height:44px;padding:0;border-radius:50%;justify-content:center;}}
  .erd-tab span{{display:none;}} html.sch-app .erd-tab{{margin-bottom:calc(60px + env(safe-area-inset-bottom,0px));}}}}
@media print{{.erd-tab,.erd,.erd-scrim{{display:none!important;}}}}
</style>
<button type="button" class="erd-tab no-print" aria-controls="emergency-readiness" aria-expanded="false" aria-label="Open Emergency Readiness: quick cards, courses and drills">{BOLT}<span>Emergency</span></button>
<div class="erd-scrim no-print"></div>
<aside class="erd no-print" id="emergency-readiness" aria-label="Emergency Readiness" aria-hidden="true">
<div class="erd-head"><span class="erd-hic">{BOLT}</span><div><h2>Emergency Readiness</h2><p>Act, learn, practice: one section for the whole dialysis unit.</p></div><button type="button" class="erd-x" aria-label="Close">&times;</button></div>
<a class="erd-get" href="/paratus/#paratus"><img src="/images/app/paratus-192.png" alt="" width="44" height="44"><span><b>Get Paratus</b><small>The Emergency Readiness app: install it and download once, and the cards, courses and practice labs work with no signal. Separate from Schola.</small></span></a>
<h3 class="erd-k">Act</h3>
<a class="erd-card erd-act" href="emergency-cards.html"><b>&#128680; Emergency quick cards</b><span class="t">One-screen action cards for the first minutes at the chair: a code, the blood leak alarm, low blood pressure, a needle out, air, hemolysis, reactions, chest pain, rhythm, potassium, sugar, seizure, stroke and fever, plus power failure, earthquake, fire, a typhoon warning and water failure. Save them on your phone for use with no signal, or print them for the crash cart.</span></a>
<h3 class="erd-k">Learn</h3>
<a class="erd-card" href="{HUB}.html"><b>Dialysis Team Resuscitation Lab</b><span class="t">A BLS-, ALS- and PALS-aligned review with algorithm recognition and megacodes, built around the patient who collapses on the machine.</span></a>
<a class="erd-card" href="{DHUB}.html"><b>Disaster Preparedness and Response</b><span class="t">Typhoons, earthquakes, fire, power and water, keeping everyone dialyzed until the unit reopens.</span></a>
<h3 class="erd-k">Practice</h3>
<a class="erd-card" href="{PRACTICE}"><b>Megacode Practice Lab</b><span class="t">Algorithm recognition rounds, timed megacodes and a facilitator recorder for resuscitation drills.</span></a>
<a class="erd-card" href="{DPRACTICE}"><b>Disaster Drills</b><span class="t">A tabletop simulator with timed injects, a call-down drill timer and a printable evacuation sheet.</span></a>
<a class="erd-home" href="{READY}">Open the Emergency Readiness page &rarr;</a>{" <b>Draft, pending clinical sign-off.</b>" if DRAFT else ""}
</aside>
<script>
(function(){{var t=document.querySelector('.erd-tab'),p=document.getElementById('emergency-readiness'),s=document.querySelector('.erd-scrim');if(!t||!p||!s)return;
function o(){{p.classList.add('erd-open');s.classList.add('erd-open');p.setAttribute('aria-hidden','false');t.setAttribute('aria-expanded','true');var x=p.querySelector('.erd-x');if(x)x.focus();}}
function c(){{p.classList.remove('erd-open');s.classList.remove('erd-open');p.setAttribute('aria-hidden','true');t.setAttribute('aria-expanded','false');}}
t.addEventListener('click',function(){{p.classList.contains('erd-open')?c():o();}});p.querySelector('.erd-x').addEventListener('click',function(){{c();t.focus();}});s.addEventListener('click',c);
document.addEventListener('keydown',function(e){{if(e.key==='Escape'&&p.classList.contains('erd-open')){{c();t.focus();}}}});
function h(){{if(location.hash==='#emergency-readiness')o();}}window.addEventListener('hashchange',h);if(location.hash==='#emergency-readiness')setTimeout(o,300);}})();
</script>
{LE}"""


def put(text, start, end, block, anchor_re, after=False):
    text = re.sub(r"\n?" + re.escape(start) + r".*?" + re.escape(end), "", text, flags=re.S)
    m = re.search(anchor_re, text, flags=re.S)
    if not m:
        return text, False
    i = m.end() if after else m.start()
    return text[:i] + ("\n" if after else "") + block + ("" if after else "\n") + text[i:], True


def badge(hub, lvl):
    v = VERIFIED.get(hub, "Academy recommendation; confirm your unit&rsquo;s requirement.")
    return (f'{BS}\n<div class="alert alert-red" style="max-width:860px;margin:18px auto;"><div class="alert-body"><p style="margin:0;">'
            f'<strong>&#9889; Required readiness: {lvl}.</strong> {v} Practice it in <a href="{READY}" style="color:var(--teal);font-weight:600;">Emergency Readiness</a>: '
            f'the quick cards, the <a href="{HUB}.html" style="color:var(--teal);font-weight:600;">Resuscitation Lab</a> and the Megacode Practice Lab.'
            f'{" Draft, pending clinical sign-off." if DRAFT else ""}</p></div></div>\n{BE}')


def why_links(text):
    text = re.sub(re.escape(WS) + r".*?" + re.escape(WE), "", text, flags=re.S)
    for cid, nums in WHY.items():
        links = " &middot; ".join(f'<a href="{MODS[n][0]}">Resuscitation Lab Module {n}</a>' for n in nums if n in MODS)
        if not links:
            continue
        pat = re.compile(r'(<article class="eqc[^"]*" id="%s".*?)(</article>)' % re.escape(cid), re.S)
        text = pat.sub(lambda m: m.group(1) + f'{WS}<p class="eqc-foot">Why this step? {links}.</p>{WE}' + m.group(2), text, count=1)
    return text


def draft_marks(text, kind="resus"):
    text = re.sub(r"\n?" + re.escape(DS) + r".*?" + re.escape(DE) + r"\n*", "\n", text, flags=re.S)
    text = text.replace(ROBOTS + "\n", "").replace(ROBOTS, "")
    if not DRAFT:
        return text
    text = text.replace("<head>", "<head>\n" + ROBOTS, 1)
    m = re.search(r"<main[^>]*>", text)
    if m:
        rest = text[m.end():].lstrip("\n")
        text = text[:m.end()] + "\n" + draft_banner(kind) + "\n\n" + rest
    return text


def crumb(text):
    """Renal Care Academy > Emergency Readiness > (the course) in the breadcrumb of every course page."""
    a = '<a href="./">Renal Care Academy</a><span class="nc-sep">›</span>'
    g = f'<a class="nc-group" href="{READY}">Emergency Readiness</a><span class="nc-sep">›</span>'
    if g in text:
        return text
    return text.replace(a, a + g, 1)


def write(path, new, dry, changed):
    old = path.read_text(encoding="utf-8") if path.exists() else None
    if new != old:
        changed.append(path.name)
        if not dry:
            path.write_text(new, encoding="utf-8")


def main():
    dry = "--dry-run" in sys.argv
    changed = []
    js = fingerprint(dry)
    djs = fingerprint(dry, DNAME)
    modules()
    modules(DHUB, DMODS)
    land_p = ACADEMY / "index.html"
    land = land_p.read_text(encoding="utf-8")
    # 3. landing block after the quick cards callout (else after the nav strip)
    new_land, ok = put(land, LS, LE, LAND, r"<!-- EMERGENCY-CARDS-END -->", after=True)
    if not ok:
        new_land, ok = put(land, LS, LE, LAND, r'<nav class="nav-strip">.*?</nav>', after=True)
    write(land_p, new_land, dry, changed)
    # 2. pages
    rec = json.loads((ROOT / "data" / "academy-resus" / "recognition.json").read_text(encoding="utf-8"))
    cases = [json.loads(p.read_text(encoding="utf-8")) for p in sorted((ROOT / "data" / "academy-cases").glob("rl*.json"))]
    tag = f'\n<script src="../assets/{js}" defer></script>\n'
    write(ACADEMY / READY, draft_marks(kind="both", text=shell(new_land, "Emergency Readiness: Act, Learn, Practice · Renal Care Academy",
          "The Renal Care Academy Emergency Readiness section: Emergency Quick Cards, the Dialysis Team Resuscitation Lab, Disaster Preparedness and Response, and practice tools for unit drills.",
          SITE + READY[:-5], ready_main())), dry, changed)
    write(ACADEMY / PRACTICE, draft_marks(shell(new_land, "Megacode Practice Lab: Algorithm Recognition and Megacodes · Renal Care Academy",
          "Algorithm recognition rounds, timed megacodes and a facilitator recorder with a shared monitor display for dialysis team resuscitation drills.",
          SITE + PRACTICE[:-5], practice_main(rec, cases), tag)), dry, changed)
    # 2b. disaster drills page (tabletop simulator, call-down timer, evacuation sheet)
    tt = json.loads((ROOT / "data" / "academy-disaster" / "tabletop.json").read_text(encoding="utf-8"))
    dcases = [json.loads(p.read_text(encoding="utf-8")) for p in sorted((ROOT / "data" / "academy-cases").glob("dp*.json"))]
    write(ACADEMY / DPRACTICE, draft_marks(kind="disaster", text=(shell(new_land, "Disaster Drills: Tabletop, Call-Down and Evacuation · Renal Care Academy",
          "A disaster tabletop simulator with timed injects, a call-down drill timer and a printable evacuation and patient-accounting sheet for dialysis units.",
          SITE + DPRACTICE[:-5], disaster_practice_main(tt, dcases), f'\n<script src="../assets/{djs}" defer></script>\n'))), dry, changed)
    # 4. hub badges
    for lvl, hubs in LEVEL.items():
        for h in hubs:
            f = ACADEMY / f"{h}.html"
            if not f.exists():
                continue
            old = f.read_text(encoding="utf-8")
            new, ok = put(old, BS, BE, badge(h, lvl), r"<!-- ACAD-QUAL-START -->")
            if not ok:
                new, ok = put(old, BS, BE, badge(h, lvl), r'<section class="section" id="modules"')
            if ok:
                write(f, new, dry, changed)
    # 5. quick card links
    eq = ACADEMY / "emergency-cards.html"
    if eq.exists():
        write(eq, why_links(eq.read_text(encoding="utf-8")), dry, changed)
    # 6. draft marks and the section crumb on the generated course pages (the two built pages carry them already)
    for f in sorted(list(ACADEMY.glob(HUB + "*.html")) + list(ACADEMY.glob(DHUB + "*.html"))):
        if f.name in (PRACTICE, DPRACTICE):
            continue
        write(f, crumb(draft_marks(f.read_text(encoding="utf-8"), "disaster" if f.name.startswith(DHUB) else "resus")), dry, changed)
    print(f"academy emergency readiness ({js}): {len(changed)} page(s) updated" + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
