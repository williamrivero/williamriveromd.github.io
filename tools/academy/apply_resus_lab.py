#!/usr/bin/env python3
"""Emergency Readiness section and the Resuscitation Lab Practice Lab (Nov 28 2026, DRAFT pending Dr. Rivero's sign-off).
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
DRAFT = True
NAME = "academy-resus-lab"
SITE = "https://renalcarematters.com/academy/"
HUB = "resuscitation-lab"
PRACTICE, READY = "resuscitation-lab-practice.html", "emergency-readiness.html"
DHUB, DNAME = "disaster-preparedness", "academy-disaster-lab"     # Disaster Preparedness and Response (Nov 28 2026, DRAFT)
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
@media (max-width:760px){.rl-panels{grid-template-columns:1fr;}.rl-list{columns:1;}}
@media print{.rl-ctl,.rl-evs,.rl-rbar,#recognition,#megacodes{display:none!important;}
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
  <div class="rl-panels">
    <a class="rl-panel act" href="emergency-cards.html">{tile("emergency-readiness-card.webp")}<small>Act</small><b>Emergency Quick Cards</b><span>Fourteen one-screen action cards for the first minutes at the chair, saved for use with no signal. Open these during a real event.</span></a>
    <a class="rl-panel" href="{HUB}.html">{tile(HUB + "-card.webp")}<small>Learn</small><b>Dialysis Team Resuscitation Lab</b><span>Thirteen modules: the basic algorithms, algorithm recognition, BLS at the chair, adult ACLS-aligned care, arrest on the machine, hyperkalemia, children, ROSC and the team.</span></a>
    <a class="rl-panel dis" href="{DHUB}.html">{tile(DHUB + "-card.webp")}<small>Learn</small><b>Disaster Preparedness and Response</b><span>Twelve modules: why disasters hurt dialysis patients twice, the unit plan and command, ready patients, typhoons and floods, earthquakes, fire, power and water, heat and ashfall, keeping everyone dialyzed, reopening and drills.</span></a>
    <a class="rl-panel prac" href="{PRACTICE}">{tile(HUB + "-practice-card.webp")}<small>Practice</small><b>Practice Lab</b><span>Algorithm recognition rounds, timed megacodes, and a facilitator recorder with a shared monitor display for resuscitation drills.</span></a>
    <a class="rl-panel prac" href="{DPRACTICE}">{tile(DHUB + "-practice-card.webp")}<small>Practice</small><b>Disaster drills</b><span>A tabletop simulator with timed injects, a call-down drill timer, and a printable evacuation and patient-accounting sheet.</span></a>
  </div>
{draft_cards_note()}
  <p>Also: the facilitator kits for <a href="{HUB}-trainer.html">resuscitation</a> and <a href="{DHUB}-trainer.html">disaster drills</a>, the <a href="../guides/calc-resuscitation-lab-toolkit.html">Resuscitation Lab toolkit</a>, and <a href="same-event-every-role.html">Same event, every role</a>.</p>
</section>
<section class="section" id="readiness">
  <div class="section-tag">Who needs which level</div>
  <h2>Resuscitation readiness by track (draft)</h2>
  <p>The table is a draft Academy recommendation. Two levels are verified Philippine rules: dialysis nurses hold a current BLS certificate, and the physician-on-duty and at least one nurse on every shift hold current ACLS from a DOH-accredited provider (DOH Administrative Order No. 2012-0001; Philippine Society of Nephrology 2024 guidelines). No DOH or PSN requirement for PALS in units that treat children was verified; it is shown as an Academy recommendation. Certificates come only from an authorized training center.</p>
  <div class="table-wrap"><table class="rl-matrix"><thead><tr><th>Level</th><th>Tracks</th></tr></thead><tbody>{''.join(rows)}</tbody></table></div>
  <h3>Disaster modules by role (draft)</h3>
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
  <p>A drill with no named owner does not happen. The table is the Academy&rsquo;s suggested division of work (draft); your unit may assign it differently, but every row needs a name and a deputy for leave and night shifts.</p>
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


def practice_main(rec, cases):
    mods = "".join(f'<li><a data-rl-mod="{n}" href="{f}">Module {n}: {t}</a></li>' for n, (f, t) in sorted(MODS.items()))
    mc = "".join(f'<li><a href="{c["page"]}#sim">{c["title"]}</a> <small>(Module {int(c["page"].split("-")[2])})</small></li>' for c in cases)
    rec_j = json.dumps(rec, ensure_ascii=False).replace("</", "<\\/")
    cases_j = json.dumps(cases, ensure_ascii=False).replace("</", "<\\/")
    return f"""{hero(f'<a href="{READY}">Emergency Readiness</a><span class="nc-sep">›</span><span class="nc-cur">Practice Lab</span>', 'Practice <em>Lab</em>', 'Recognize the algorithm, run the megacode, record the drill')}
{CSS}
<main class="container rl-main">
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
    return f"""{hero(f'<a href="{READY}">Emergency Readiness</a><span class="nc-sep">›</span><a href="{DHUB}.html">Disaster Preparedness and Response</a><span class="nc-sep">›</span><span class="nc-cur">Disaster drills</span>', 'Disaster <em>drills</em>', 'Run the tabletop, test the call list, print the evacuation sheet')}
{CSS}
<main class="container rl-main">
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


LAND = f"""{LS}
<style id="rl-landing-css">
.rl-land{{max-width:860px;margin:14px auto 0;padding:0 32px;}}
.rl-land-box{{border:1px solid var(--border);border-left:5px solid var(--teal);border-radius:14px;padding:14px 18px;background:var(--white);}}
.rl-land-box h2{{font:800 18px/1.25 Inter,system-ui,sans-serif;margin:0 0 6px;color:var(--text);}}
.rl-land-box p{{margin:0 0 8px;font-size:14.5px;line-height:1.5;color:var(--text-mid);}}
.rl-land-links{{display:flex;flex-wrap:wrap;gap:8px;}}
.rl-land-links a{{font:700 14px/1 Inter,system-ui,sans-serif;text-decoration:none;border:1px solid var(--border);border-radius:999px;padding:8px 12px;color:var(--teal);}}
html[data-theme="dark"] .rl-land-links a{{color:var(--text);}}
@media (max-width:640px){{.rl-land{{padding:0 16px;}}}}
@media print{{.rl-land{{display:none;}}}}
</style>
<div class="rl-land" id="emergency-readiness"><div class="rl-land-box"><h2>&#9889; Emergency Readiness: act, learn, practice</h2>
<p>A cross-track section for the whole unit: the Emergency Quick Cards, the Dialysis Team Resuscitation Lab (BLS-, ALS- and PALS-aligned review with algorithm recognition and megacodes), Disaster Preparedness and Response (typhoons, earthquakes, fire, power and water, keeping everyone dialyzed), and practice tools for unit drills.{" <b>Draft, pending clinical sign-off.</b>" if DRAFT else ""}</p>
<div class="rl-land-links"><a href="{READY}">Section home</a><a href="emergency-cards.html">Act: quick cards</a><a href="{HUB}.html">Learn: Resuscitation Lab</a><a href="{DHUB}.html">Learn: Disaster Preparedness</a><a href="{PRACTICE}">Practice Lab</a><a href="{DPRACTICE}">Disaster drills</a></div></div></div>
{LE}"""


def put(text, start, end, block, anchor_re, after=False):
    text = re.sub(r"\n?" + re.escape(start) + r".*?" + re.escape(end), "", text, flags=re.S)
    m = re.search(anchor_re, text, flags=re.S)
    if not m:
        return text, False
    i = m.end() if after else m.start()
    return text[:i] + ("\n" if after else "") + block + ("" if after else "\n") + text[i:], True


def badge(hub, lvl):
    v = VERIFIED.get(hub, "Academy recommendation (draft); confirm your unit&rsquo;s requirement.")
    return (f'{BS}\n<div class="alert alert-red" style="max-width:860px;margin:18px auto;"><div class="alert-body"><p style="margin:0;">'
            f'<strong>&#9889; Required readiness: {lvl}.</strong> {v} Practice it in <a href="{READY}" style="color:var(--teal);font-weight:600;">Emergency Readiness</a>: '
            f'the quick cards, the <a href="{HUB}.html" style="color:var(--teal);font-weight:600;">Resuscitation Lab</a> and the Practice Lab.'
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
    write(ACADEMY / PRACTICE, draft_marks(shell(new_land, "Practice Lab: Algorithm Recognition and Megacodes · Renal Care Academy",
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
