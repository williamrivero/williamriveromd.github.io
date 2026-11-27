#!/usr/bin/env python3
"""Academy "Same event, every role" drill (Dr. Rivero, Nov 27 2026). Idempotent.

One hemodialysis event followed minute by minute through four roles (Hemodialysis Nurse, Physician-on-Duty,
Technician, Head Nurse), so each learner sees what the others are doing and where the handoffs happen.

  data/academy-drills/same-event.json   the drill content (edit this): roles, events, phases, handoffs,
                                        stop-and-call points, "where it breaks", debrief questions, module links

This patcher:
  1. writes academy/same-event-every-role.html, built on the landing page's head, header and footer (like the
     review deck). The page is fully rendered HTML (works without JavaScript, offline in Schola, readable by
     search engines); a small inline script only switches the event and the role view (?event=water&role=tech);
  2. puts a "Team drill" card on the landing page after Study tools (CROSS-ROLE markers, nav pill "Team drill");
  3. puts a short callout on each applicable track hub, just before the qualifications box (CROSS-ROLE-HUB markers).

Clinical content follows the track modules (water: total chlorine 0.1 mg/L, worker then polisher tank, as in Water
Treatment Technician Module 4; intradialytic hypotension: POD Module 13) and defers to the unit protocol and the
Attending Nephrologist. Needs Dr. Rivero's sign-off before it is pushed to main.

    python3 tools/academy/apply_cross_role.py             # apply
    python3 tools/academy/apply_cross_role.py --dry-run   # report only
"""
import html, json, re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
DATA = ROOT / "data" / "academy-drills" / "same-event.json"
PAGE = "same-event-every-role.html"
URL = "https://renalcarematters.com/academy/same-event-every-role"
TITLE = "Same Event, Every Role · Renal Care Academy"
DESC = ("One hemodialysis event, four roles: how the hemodialysis nurse, physician-on-duty, technician and head nurse "
        "each handle intradialytic hypotension or a chlorine breakthrough in the water system, and where the handoffs happen.")
ORDER = ("nurse", "pod", "tech", "hn")
LAND_START, LAND_END = "<!-- CROSS-ROLE-START -->", "<!-- CROSS-ROLE-END -->"
HUB_START, HUB_END = "<!-- CROSS-ROLE-HUB-START -->", "<!-- CROSS-ROLE-HUB-END -->"
PILL = '<a class="nav-pill" href="#team-drill">Team drill</a>'
# hub file -> (role id, event ids the hub's role takes part in)
HUBS = {
    "nephrology-nursing.html": ("nurse", ("idh", "water")),
    "physician-on-duty.html": ("pod", ("idh", "water")),
    "hemodialysis-technician.html": ("tech", ("idh",)),
    "water-treatment-technician.html": ("tech", ("water",)),
    "dialysis-head-nurse.html": ("hn", ("idh", "water")),
}

e = html.escape


def role_name(D, ev, r):
    return ev["tech"]["name"] if r == "tech" else D["roles"][r]["name"]


def ul(items):
    if not items:
        return '<p class="cr-idle">Not yet involved</p>'
    return "<ul>" + "".join(f"<li>{e(x)}</li>" for x in items) + "</ul>"


def flags(ph, r):
    out = ""
    if ph.get("handoff", {}).get(r):
        out += f'<p class="cr-ho"><b>Handoff</b> {e(ph["handoff"][r])}</p>'
    if ph.get("stop", {}).get(r):
        out += f'<p class="cr-stop"><b>Stop and call</b> {e(ph["stop"][r])}</p>'
    return out


def event_html(D, ev, first):
    names = {r: role_name(D, ev, r) for r in ORDER}
    s = [f'<section class="cr-event" id="{ev["id"]}" data-event="{ev["id"]}"{"" if first else " data-later"}>']
    s.append(f'<div class="cr-scen"><p class="cr-kicker">{e(ev["label"])}</p><h2>{e(ev["title"])}</h2><p>{e(ev["setup"])}</p>'
             '<div class="cr-facts">' + "".join(f'<span>{e(f)}</span>' for f in ev["facts"]) + "</div></div>")
    s.append('<div class="cr-legend"><span class="cr-lg-ho">Handoff: information passes to another role</span>'
             '<span class="cr-lg-stop">Stop and call: per unit protocol, but always ask the Attending Nephrologist for guidance</span></div>')
    # side-by-side table
    s.append(f'<div class="cr-tablewrap"><table class="cr-grid"><caption>{e(ev["label"])}: what each role does, phase by phase</caption><thead><tr><th scope="col">Phase</th>')
    s += [f'<th scope="col" class="cr-c-{r}">{e(names[r])}</th>' for r in ORDER]
    s.append("</tr></thead><tbody>")
    for ph in ev["phases"]:
        s.append(f'<tr><th scope="row"><b>{e(ph["name"])}</b><span>{e(ph["time"])}</span></th>')
        s += [f'<td class="cr-c-{r}">{ul(ph.get(r))}{flags(ph, r)}</td>' for r in ORDER]
        s.append("</tr>")
    s.append("</tbody></table></div>")
    # one column per role (phones, and the single-role view)
    for r in ORDER:
        s.append(f'<div class="cr-stack" data-role="{r}"><h3 class="cr-c-{r}">{e(names[r])}</h3>')
        for ph in ev["phases"]:
            others = [f"<b>{e(names[o])}:</b> {e(ph[o][0])}" for o in ORDER if o != r and ph.get(o)]
            meanwhile = (f'<p class="cr-meanwhile"><span>Meanwhile</span>' + "<br>".join(others) + "</p>") if others else ""
            s.append(f'<div class="cr-step"><p class="cr-when"><b>{e(ph["name"])}</b> {e(ph["time"])}</p>'
                     f'<div>{ul(ph.get(r))}{flags(ph, r)}{meanwhile}</div></div>')
        links = " · ".join(f'<a href="{e(f)}">{e(t)}</a>' for f, t in ev["links"].get(r, []))
        if links:
            s.append(f'<p class="cr-deeper">Study this in your track: {links}</p>')
        s.append("</div>")
    s.append('<h3 class="cr-sub">Where it breaks</h3><div class="cr-cards">' +
             "".join(f'<div class="cr-card"><b>{e(h)}</b>{e(p)}</div>' for h, p in ev["breaks"]) + "</div>")
    s.append('<h3 class="cr-sub">Team debrief</h3><ol class="cr-debrief">' + "".join(f"<li>{e(q)}</li>" for q in ev["debrief"]) + "</ol>")
    s.append('<h3 class="cr-sub">Go deeper in each track</h3><div class="cr-cards">')
    for r in ORDER:
        hub = ev["tech"]["hub"] if r == "tech" else D["roles"][r]["hub"]
        mods = "".join(f'<a href="{e(f)}">{e(t)}</a>' for f, t in ev["links"].get(r, []))
        s.append(f'<div class="cr-card cr-c-{r}"><b><a href="{e(hub)}">{e(names[r])}</a></b>{mods}</div>')
    s.append("</div></section>")
    return "\n".join(s)


CSS = """
<style id="cr-page">
.cr-hero{padding:34px 0 22px;}
.cr-hero h1{margin:10px 0 6px;}
.cr-hero .hero-tagline{font-size:17px;color:var(--text-mid);margin:0;}
.cr-main{max-width:1240px;margin:0 auto;padding:10px 32px 40px;--cr-nurse:#1a6b72;--cr-pod:#1f3864;--cr-tech:#c55a11;--cr-hn:#4b3280;}
html[data-theme="dark"] .cr-main{--cr-nurse:#2ba8b0;--cr-pod:#7fa3e0;--cr-tech:#f0904a;--cr-hn:#b49ae8;}
.cr-main h2,.cr-main h3{font-family:Inter,system-ui,sans-serif;color:var(--text);}
.cr-intro{font-size:15.5px;line-height:1.65;color:var(--text-mid);max-width:860px;}
.cr-controls{padding:10px 0;margin:14px 0 6px;display:none;flex-wrap:wrap;gap:10px 18px;align-items:center;border-bottom:1px solid var(--border);}
.cr-js .cr-controls{display:flex;}
.cr-controls .cr-lab{font-size:12px;letter-spacing:.06em;text-transform:uppercase;color:var(--text-muted);}
.cr-seg{display:inline-flex;flex-wrap:wrap;border:1px solid var(--border);border-radius:10px;overflow:hidden;}
.cr-seg button{border:0;border-right:1px solid var(--border);background:var(--white);color:var(--text);padding:8px 13px;font:inherit;font-size:14px;cursor:pointer;}
.cr-seg button:last-child{border-right:0;}
.cr-seg button[aria-pressed="true"]{background:var(--teal);color:#fff;font-weight:600;}
.cr-seg button:focus-visible{outline:3px solid #c55a11;outline-offset:-3px;}
.cr-event{margin:18px 0 34px;}
.cr-js .cr-event[hidden]{display:none;}
.cr-scen{background:var(--white);border:1px solid var(--border);border-left:5px solid var(--teal);border-radius:12px;padding:16px 20px;}
.cr-scen h2{margin:2px 0 8px;font-size:21px;}
.cr-scen p{margin:0;font-size:15px;line-height:1.6;color:var(--text-mid);}
.cr-kicker{font-size:12px!important;letter-spacing:.07em;text-transform:uppercase;color:var(--teal)!important;font-weight:700;}
.cr-facts{display:flex;flex-wrap:wrap;gap:8px;margin-top:12px;}
.cr-facts span{font-size:13px;border:1px solid var(--border);border-radius:999px;padding:3px 11px;background:var(--bg);color:var(--text);}
.cr-legend{display:flex;flex-wrap:wrap;gap:8px 20px;font-size:13px;color:var(--text-muted);margin:14px 0 10px;}
.cr-legend span::before{content:"";display:inline-block;width:12px;height:12px;border-radius:3px;margin-right:6px;vertical-align:-1px;}
.cr-lg-ho::before{background:var(--amber);} .cr-lg-stop::before{background:var(--red);}
.cr-tablewrap{overflow-x:auto;border:1px solid var(--border);border-radius:12px;}
.cr-grid{border-collapse:collapse;width:100%;min-width:940px;font-size:14px;line-height:1.5;background:var(--white);}
.cr-grid caption{position:absolute;left:-9999px;}
.cr-grid th,.cr-grid td{vertical-align:top;text-align:left;padding:12px;border-top:1px solid var(--border);border-left:1px solid var(--border);}
.cr-grid thead th{border-top:0;border-bottom:3px solid var(--cr-col,var(--border));background:var(--bg);font-size:14.5px;color:var(--text);}
.cr-grid tbody th{width:120px;background:var(--bg);font-weight:400;color:var(--text-muted);font-size:13px;}
.cr-grid tbody th b{display:block;color:var(--text);font-size:14.5px;}
.cr-grid tr>*:first-child{border-left:0;}
.cr-grid ul,.cr-stack ul{margin:0;padding-left:18px;}
.cr-grid li,.cr-stack li{margin:0 0 6px;color:var(--text-mid);}
.cr-c-nurse{--cr-col:var(--cr-nurse);} .cr-c-pod{--cr-col:var(--cr-pod);} .cr-c-tech{--cr-col:var(--cr-tech);} .cr-c-hn{--cr-col:var(--cr-hn);}
.cr-idle{margin:0;color:var(--text-faint);font-style:italic;}
.cr-ho,.cr-stop{margin:8px 0 0;padding:7px 10px;border-radius:8px;font-size:13px;line-height:1.5;color:var(--text);}
.cr-ho{background:var(--amber-soft);border-left:3px solid var(--amber);}
.cr-stop{background:var(--red-soft);border-left:3px solid var(--red);}
.cr-ho b,.cr-stop b{display:block;font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;}
.cr-stack{display:none;margin:18px 0;}
.cr-stack h3{border-left:5px solid var(--cr-col);padding-left:10px;font-size:18px;margin:0 0 6px;}
.cr-step{display:grid;grid-template-columns:150px 1fr;gap:16px;border-top:1px solid var(--border);padding:13px 0;font-size:14.5px;}
.cr-when{margin:0;color:var(--text-muted);font-size:13px;} .cr-when b{display:block;color:var(--text);font-size:15px;}
.cr-meanwhile{display:none;margin:10px 0 0;font-size:13px;line-height:1.55;color:var(--text-muted);border-left:2px solid var(--border);padding-left:10px;}
.cr-meanwhile span{display:block;font-size:11.5px;letter-spacing:.06em;text-transform:uppercase;}
.cr-deeper{font-size:14px;margin:6px 0 0;color:var(--text-muted);}
.cr-sub{font-size:17px;margin:28px 0 12px;padding-bottom:6px;border-bottom:2px solid var(--border);}
.cr-cards{display:grid;grid-template-columns:repeat(auto-fit,minmax(250px,1fr));gap:12px;}
.cr-card{background:var(--white);border:1px solid var(--border);border-top:4px solid var(--cr-col,var(--teal));border-radius:12px;padding:13px 15px;font-size:14px;line-height:1.55;color:var(--text-mid);}
.cr-card b{display:block;margin-bottom:4px;color:var(--text);font-size:15px;}
.cr-card a{display:block;margin-top:4px;}
.cr-debrief{font-size:15px;line-height:1.65;color:var(--text-mid);}
.cr-howto{font-size:15px;line-height:1.65;color:var(--text-mid);max-width:860px;}
.cr-note{font-size:13px;color:var(--text-muted);border-top:1px solid var(--border);padding-top:14px;margin-top:30px;max-width:860px;}
/* single-role view: that role's column, with what the others are doing */
.cr-main[data-view]:not([data-view="all"]) .cr-tablewrap{display:none;}
.cr-main[data-view="nurse"] .cr-stack[data-role="nurse"],.cr-main[data-view="pod"] .cr-stack[data-role="pod"],
.cr-main[data-view="tech"] .cr-stack[data-role="tech"],.cr-main[data-view="hn"] .cr-stack[data-role="hn"]{display:block;}
.cr-main[data-view]:not([data-view="all"]) .cr-meanwhile{display:block;}
@media (max-width:900px){
  .cr-tablewrap{display:none;}
  .cr-main:not([data-view]) .cr-stack,.cr-main[data-view="all"] .cr-stack{display:block;}
  .cr-step{grid-template-columns:1fr;gap:6px;}
}
@media (max-width:640px){.cr-main{padding:8px 16px 32px;}}
@media print{.cr-controls{display:none!important;}.cr-event[hidden]{display:block!important;}.cr-tablewrap{display:none;}.cr-stack{display:block!important;}.cr-meanwhile{display:none!important;}}
</style>
"""

JS = """
<script>
(function(){
  var main=document.getElementById('cr-main'); if(!main) return;
  main.classList.add('cr-js');
  var evs=[].slice.call(main.querySelectorAll('.cr-event'));
  var roles=JSON.parse(main.getAttribute('data-roles'));
  var st={event:evs[0].id, view:'all'};
  var q=new URLSearchParams(location.search), h=location.hash.slice(1);
  if(evs.some(function(x){return x.id===h})) st.event=h;
  if(evs.some(function(x){return x.id===q.get('event')})) st.event=q.get('event');
  if(q.get('role') in roles.idh) st.view=q.get('role');
  function seg(id,items,key){
    var box=document.getElementById(id); box.innerHTML='';
    items.forEach(function(it){var b=document.createElement('button');b.type='button';b.textContent=it[1];
      b.setAttribute('aria-pressed',String(st[key]===it[0]));
      b.onclick=function(){st[key]=it[0];draw(true)};box.appendChild(b)});
  }
  function draw(push){
    evs.forEach(function(x){x.hidden=x.id!==st.event});
    main.setAttribute('data-view',st.view);
    var names=roles[st.event];
    seg('cr-ev',evs.map(function(x){return [x.id,x.querySelector('.cr-kicker').textContent]}),'event');
    seg('cr-role',[['all','All roles']].concat(Object.keys(names).map(function(k){return [k,names[k]]})),'view');
    if(push){try{var u=new URL(location.href);u.searchParams.set('event',st.event);
      if(st.view==='all')u.searchParams.delete('role');else u.searchParams.set('role',st.view);
      u.hash='';history.replaceState(null,'',u)}catch(e){}}
  }
  draw(false);
})();
</script>
"""


def build_main(D):
    roles_js = {ev["id"]: {r: role_name(D, ev, r) for r in ORDER} for ev in D["events"]}
    events = "\n".join(event_html(D, ev, i == 0) for i, ev in enumerate(D["events"]))
    return f"""
<!-- ═══ HERO ════════════════════════════════════ -->
<section class="hero cr-hero">
  <div class="container">
    <div class="nc-bar"><a href="./">Renal Care Academy</a><span class="nc-sep">›</span><span>Team drill</span></div>
    <h1>Same Event, Every Role</h1>
    <p class="hero-tagline">One emergency on the dialysis floor, seen through four pairs of hands</p>
  </div>
</section>
{CSS}
<main class="container cr-main" id="cr-main" data-roles='{e(json.dumps(roles_js))}'>
  <p class="cr-intro">An emergency in a hemodialysis unit is never one person&rsquo;s event. Each drill follows a single event, phase by phase, through the Hemodialysis Nurse at the chair, the Physician-on-Duty, the technician, and the Head Nurse. Read your own column first. Then read the others, to learn what your colleagues need from you, and when. On a phone, or after you pick one role, you see that role&rsquo;s actions with a short &ldquo;Meanwhile&rdquo; line for what everyone else is doing.</p>
  <div class="cr-controls" role="group" aria-label="Drill controls">
    <span class="cr-lab">Event</span><div class="cr-seg" id="cr-ev"></div>
    <span class="cr-lab">View</span><div class="cr-seg" id="cr-role"></div>
  </div>
{events}
  <section class="cr-howto" id="huddle">
    <h2>Running it as a team drill</h2>
    <p>Use one event at a monthly huddle or skills day. Give each person a role card that is not their usual job: a technician reads the Physician-on-Duty column, a nurse reads the Head Nurse column. Read the scenario aloud, then walk the phases in order, each person saying what they would do and who they would tell. Stop at every handoff and ask the receiving role what they heard. Finish with the debrief questions and one change your unit will make. It takes about 20 minutes.</p>
  </section>
  <p class="cr-note">For self-study and onboarding only, not a protocol. Your unit&rsquo;s written procedures, your Attending Nephrologist&rsquo;s orders, and the manufacturers&rsquo; instructions for your machines and water system come first. Water limits follow the international standard for dialysis water (ISO 23500; total chlorine 0.1 mg/L), as taught in the Water Treatment Technician track. Intradialytic hypotension follows the Physician-on-Duty track (European Best Practice Guidelines, 2015). Patients, units and numbers are illustrative.</p>
</main>
{JS}"""


def sub_meta(head):
    head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", head, count=1, flags=re.S)
    for prop, val in (("og:title", TITLE), ("twitter:title", TITLE), ("og:description", DESC), ("twitter:description", DESC), ("og:url", URL)):
        head = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*(")' % re.escape(prop), lambda m: m.group(1) + val + m.group(2), head)
    head = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + DESC + m.group(2), head, count=1)
    head = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + URL + m.group(2), head, count=1)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', "", head, flags=re.S)
    return head


def build_page(D, land):
    head, rest = land.split("</head>", 1)
    head = sub_meta(head + "</head>")
    body_open = rest[:rest.index("</header>") + len("</header>")]
    tail = rest[rest.index('<footer class="guide-footer">'):]
    tail = re.sub(r'<button class="print-btn".*?</button>\s*', "", tail, count=1, flags=re.S)
    tail = re.sub(r'\n?<script src="[^"]*assets/(academy-(?!review)|tech-course|guide-rail|share-buttons|image-lightbox)[^"]*" defer></script>', "", tail)
    return head + body_open + "\n" + build_main(D) + "\n" + tail


def landing_block():
    return f"""{LAND_START}
<section class="section" id="team-drill">
  <div class="section-tag">Team drill</div>
  <h2>Same event, every role</h2>
  <p>Emergencies on the dialysis floor are handled by a team, so learn them as one. <a href="{PAGE}"><strong>Same Event, Every Role</strong></a> follows one event through four roles, phase by phase: what the Hemodialysis Nurse, the Physician-on-Duty, the technician, and the Head Nurse each do, where the handoffs happen, and where it usually breaks. Read it alone, or run it at a huddle with everyone playing a role that is not their own.</p>
  <div class="tc-cards tc-two">
    <div class="tc-card"><b><a href="{PAGE}?event=idh">Intradialytic hypotension</a></b>Hour 3, Station 7: a patient with a large weight gain feels faint as her blood pressure falls.</div>
    <div class="tc-card"><b><a href="{PAGE}?event=water">Water system alarm</a></b>6:10 a.m.: total chlorine is high after the first carbon tank, with patients already connected.</div>
  </div>
</section>
{LAND_END}
"""


def hub_block(role, events, D):
    evs = {ev["id"]: ev for ev in D["events"]}
    links = " or ".join(f'<a href="{PAGE}?event={i}&amp;role={role}">{e(evs[i]["label"].lower())}</a>' for i in events)
    return (f'{HUB_START}\n<div class="alert alert-teal cr-hub"><div class="alert-icon">🤝</div><div class="alert-body">'
            f'<h4>Team drill: same event, every role</h4><p>See how your role fits with the others during {links}: what you do, '
            f'what the rest of the team is doing at the same moment, and every handoff between you. '
            f'<a href="{PAGE}">Open the drill</a>.</p></div></div>\n{HUB_END}\n')


def put_block(text, start, end, block, anchor, before=True):
    text = re.sub(re.escape(start) + r".*?" + re.escape(end) + r"\n?", "", text, flags=re.S)
    i = text.find(anchor)
    if i < 0:
        return text, False
    if not before:
        i += len(anchor)
    return text[:i] + block + text[i:], True


def main():
    dry = "--dry-run" in sys.argv
    D = json.loads(DATA.read_text(encoding="utf-8"))
    for ev in D["events"]:
        for ph in ev["phases"]:
            for k in list(ph.get("handoff", {})) + list(ph.get("stop", {})):
                assert k in ORDER, f"{ev['id']}: unknown role {k}"
        for r, lst in ev["links"].items():
            for f, _ in lst:
                assert (ACADEMY / f).exists(), f"{ev['id']}: missing link target {f}"
    land_path = ACADEMY / "index.html"
    land = land_path.read_text(encoding="utf-8")
    changed = []
    # 1. landing block (after Study tools) + nav pill
    new_land, ok = put_block(land, LAND_START, LAND_END, landing_block(), "<!-- STUDY-TOOLS-END -->\n", before=False)
    if ok and PILL not in new_land:
        new_land = new_land.replace('<a class="nav-pill" href="#tools">Study tools</a>', '<a class="nav-pill" href="#tools">Study tools</a>\n' + PILL, 1)
    if new_land != land:
        changed.append("index.html")
        if not dry:
            land_path.write_text(new_land, encoding="utf-8")
    # 2. drill page (from the landing page as it now stands)
    page = build_page(D, new_land)
    dst = ACADEMY / PAGE
    if not dst.exists() or dst.read_text(encoding="utf-8") != page:
        changed.append(PAGE)
        if not dry:
            dst.write_text(page, encoding="utf-8")
    # 3. hub callouts
    for name, (role, events) in HUBS.items():
        f = ACADEMY / name
        if not f.exists():
            continue
        old = f.read_text(encoding="utf-8")
        new, ok = put_block(old, HUB_START, HUB_END, hub_block(role, events, D), "<!-- ACAD-QUAL-START -->")
        if ok and new != old:
            changed.append(name)
            if not dry:
                f.write_text(new, encoding="utf-8")
    print(f"academy team drill: {len(changed)} page(s) updated" + (" [dry run]" if dry else "") + (": " + ", ".join(changed) if changed else ""))


if __name__ == "__main__":
    main()
