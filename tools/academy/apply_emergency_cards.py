#!/usr/bin/env python3
"""Academy emergency quick cards (Dr. Rivero, Nov 27 2026). Idempotent.

One-screen action cards for the first minutes at the dialysis chair, readable with no signal:
  * cards 1 and 2 (Code during hemodialysis, Blood leak alarm): CODE_CARD / LEAK_CARD below
  * cards 3 to 14 (Nov 27 2026 expansion): data in emergency_cards_data.py, rendered by card_html(); drafts until
    REVIEW in that file records a reviewer. Review packet: tools/academy/EMERGENCY_CARDS_REVIEW.md

This patcher:
  1. writes academy/emergency-cards.html (built on the landing page's head, header and footer, like the review deck;
     all card CSS and the small save-offline script are inline, so the page works from one saved file);
  2. puts an "Emergency quick cards" callout on the landing page (between EMERGENCY-CARDS markers, right after the
     nav strip) and a short link box in the modules that teach these emergencies (MODULE_LINKS);
  3. build_schola.py lists the page in SHARED_PAGES, so every Schola track download saves it too. The page's own
     "Save for offline use" button saves just this page into the Schola cache, for staff who download nothing else.

Clinical content follows the Academy's own modules (Charge Nurse 12, Nephrology Nursing 9, Physician-on-Duty 15 and 16)
and guides/code-blue-acls-dialysis-unit.html, which carries the drug table. Doses are those printed in that guide
(AHA adult advanced life support). Everything defers to the unit protocol and the attending nephrologist.
Edit the card text in CARDS below, then run this script (publish_academy.py runs it after apply_review.py).

    python3 tools/academy/apply_emergency_cards.py             # apply
    python3 tools/academy/apply_emergency_cards.py --dry-run   # report only
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
ACADEMY = ROOT / "academy"
PAGE = "emergency-cards.html"
URL = "https://renalcarematters.com/academy/emergency-cards"
TITLE = "Emergency quick cards for the dialysis floor · Renal Care Academy"
DESC = ("One-screen action cards for the first minutes of a hemodialysis emergency: code, blood leak, low blood pressure, "
        "needle dislodgement, air, hemolysis, reactions, chest pain, arrhythmia, potassium, low sugar, seizure, stroke and fever.")
START, END = "<!-- EMERGENCY-CARDS-START -->", "<!-- EMERGENCY-CARDS-END -->"
MSTART, MEND = "<!-- EQC-LINK-START -->", "<!-- EQC-LINK-END -->"

# modules that teach these emergencies -> which card(s) to point at
# modules that teach these emergencies -> which card(s) to point at (Nov 27 2026: 14 cards)
MODULE_LINKS = {
    "dialysis-charge-nurse-12-first-ten-minutes-emergency.html": ("code",),
    "dialysis-charge-nurse-07-mid-session-surveillance.html": ("hypotension", "hypoglycemia"),
    "dialysis-charge-nurse-11-water-and-machines-hold-release.html": ("hemolysis", "fever-rigors"),
    "nephrology-nursing-07-hd-vascular-access-infection-prevention.html": ("fever-rigors", "access-bleeding"),
    "nephrology-nursing-09-hd-session-complication-response.html": ("code", "hypotension", "access-bleeding", "air-embolism", "hemolysis", "anaphylaxis", "leak"),
    "physician-on-duty-06-water-and-dialysate.html": ("hemolysis", "fever-rigors"),
    "physician-on-duty-12-first-sessions-and-unusual-sessions.html": ("seizure",),
    "physician-on-duty-13-when-the-pressure-falls.html": ("hypotension",),
    "physician-on-duty-15-heart-emergencies-in-the-chair.html": ("chest-pain", "arrhythmia", "code"),
    "physician-on-duty-16-when-the-circuit-fails.html": ("air-embolism", "hemolysis", "anaphylaxis", "access-bleeding", "leak", "code"),
    "physician-on-duty-17-fever-and-bloodstream-infection.html": ("fever-rigors",),
    "physician-on-duty-18-potassium-sugar-and-the-brain.html": ("hyperkalemia", "hypoglycemia", "seizure", "stroke"),
    "physician-on-duty-19-bleeding-and-heparin.html": ("access-bleeding",),
    "physician-on-duty-22-diabetes-on-dialysis.html": ("hypoglycemia",),
    "attending-nephrologist-06-electrolyte-emergencies.html": ("hyperkalemia",),
    "attending-nephrologist-15-hd-emergencies.html": ("code", "hypotension", "air-embolism", "hemolysis", "anaphylaxis", "leak"),
    "attending-nephrologist-16-vascular-access-infection.html": ("fever-rigors",),
    "dialysis-head-nurse-04-vascular-access-and-bleeding.html": ("access-bleeding",),
    "dialysis-head-nurse-07-deterioration-and-emergencies.html": ("code", "hypotension", "leak"),
    "hemodialysis-technician-09-the-hemodialysis-session.html": ("leak", "air-embolism"),
    "hemodialysis-technician-10-complications-emergency-response.html": ("code", "hypotension", "air-embolism", "access-bleeding", "leak"),
    "dialysis-biomedical-technician-07-protective-systems-alarm-testing.html": ("leak", "air-embolism"),
    "dialysis-nurse-assistant-07-access-protection-monitoring.html": ("access-bleeding",),
    "dialysis-nurse-assistant-08-deterioration-emergencies.html": ("code", "hypotension", "hypoglycemia"),
    "pediatric-dialysis-nurse-15-emergencies-and-resuscitation.html": ("code",),
    "special-dialysis-nurse-roles-07-safety-and-emergency-preparedness.html": ("code", "leak"),
}
CARD_NAMES = {"code": "Code during hemodialysis", "leak": "Blood leak alarm"}


CODE_CARD = """
<article class="eqc eqc-code" id="code" aria-labelledby="code-h">
  <header class="eqc-head">
    <div class="eqc-kicker">Emergency quick card 1</div>
    __STATUS_code__
    <h2 id="code-h">Code during hemodialysis</h2>
    <p class="eqc-when">Unresponsive, not breathing normally (gasping counts), no pulse in 10 seconds.</p>
  </header>
  <ol class="eqc-steps">
    <li><span class="eqc-n">1</span><div><b>Call the code.</b> Crash cart, defibrillator, oxygen. Note the time.</div></li>
    <li><span class="eqc-n">2</span><div><b>Chair flat, compress now.</b> 100&ndash;120 a minute, 5&ndash;6 cm, full recoil; 30:2 with a bag-valve-mask.</div></li>
    <li><span class="eqc-n">3</span><div><b>Pads on; shock a shockable rhythm.</b> Hands off the patient, lines and machine, then compress again at once.</div></li>
    <li class="eqc-stop"><span class="eqc-n">4</span><div><b>Stop fluid removal.</b> Air, hemolysis or a dialyzer reaction? <b>Clamp, do not return the blood.</b> Otherwise return it quickly, or clamp and disconnect.</div></li>
    <li><span class="eqc-n">5</span><div><b>Keep the needles or catheter in</b> for drugs. Epinephrine 1 mg every 3&ndash;5 minutes.</div></li>
    <li><span class="eqc-n">6</span><div><b>Think potassium.</b> Calcium gluconate, then insulin with dextrose, per protocol.</div></li>
    <li><span class="eqc-n">7</span><div><b>Roles by name,</b> plus a watcher for the other patients. Call the attending.</div></li>
  </ol>
  <details class="eqc-det">
    <summary>Drugs, other causes, roles and after a pulse returns</summary>
    <ul>
      <li><b>Compressions never wait for the machine.</b> Pauses under 10 seconds; swap compressors every 2 minutes. One dialysis nurse manages the circuit while compressions continue: stop ultrafiltration (UF), then return the blood with saline or clamp and disconnect, leaving the access in place for intravenous (IV) drugs. A saline bolus through the circuit treats hypovolemia from UF. Use a defibrillator or automated external defibrillator (AED); pads go clear of the access and any wet area.</li>
      <li><b>Drugs</b> (American Heart Association (AHA) adult advanced life support, as in the site&rsquo;s <a href="../guides/code-blue-acls-dialysis-unit.html">dialysis code guide</a>): epinephrine 1 mg IV every 3&ndash;5 minutes, as soon as possible in asystole or pulseless electrical activity (PEA), after the 2nd shock in ventricular fibrillation or pulseless ventricular tachycardia (VF/pVT). Amiodarone 300 mg, then 150 mg, for VF/pVT that persists after shocks and epinephrine.</li>
      <li><b>Suspected hyperkalemia</b> (missed session, after the long weekend gap, a short or poor session): give intravenous calcium, then insulin with glucose, as the unit&rsquo;s order set directs, and check glucose afterward. Never give calcium and bicarbonate in the same line. Guidelines differ on these drugs during arrest: the ERC recommends calcium and bicarbonate for hyperkalemic arrest, while the AHA 2025 guideline calls their effectiveness in arrest uncertain; your unit protocol decides. Emergency dialysis is the only real potassium removal: plan it early with the attending (<a href="#hyperkalemia">Card 10</a>).</li>
      <li><b>Other causes common on dialysis:</b> hypovolemia from UF (saline bolus through the circuit), hypoglycemia, bleeding from a dislodged needle (lift the blanket; <a href="#access-bleeding">Card 4</a>), air embolism (<a href="#air-embolism">Card 5</a>), a dialyzer reaction (<a href="#anaphylaxis">Card 7</a>).</li>
      <li><b>Roles:</b> leader &middot; compressions (swap every 2 minutes) &middot; airway &middot; defibrillator and drugs &middot; circuit nurse &middot; recorder and timer &middot; watcher of the other patients &middot; runner to call the attending nephrologist and the ambulance or code team.</li>
      <li><b>After a pulse returns:</b> do not restart dialysis unless the attending says so. 12-lead electrocardiogram (ECG), potassium, glucose, blood gas; arrange transfer. Hand off time on the machine, fluid removed, last potassium, the access, and whether the blood was returned. Tell the family, document, debrief.</li>
    </ul>
  </details>
  <p class="eqc-foot">Your unit&rsquo;s protocol and crash-cart stock decide. Learn it: <a href="dialysis-charge-nurse-12-first-ten-minutes-emergency.html">Charge Nurse 12</a> &middot; <a href="physician-on-duty-15-heart-emergencies-in-the-chair.html">Physician-on-Duty 15</a> &middot; <a href="nephrology-nursing-09-hd-session-complication-response.html">Nephrology Nursing 9</a>.__SOURCES_code__</p>
</article>
"""

LEAK_CARD = """
<article class="eqc eqc-leak" id="leak" aria-labelledby="leak-h">
  <header class="eqc-head">
    <div class="eqc-kicker">Emergency quick card 2</div>
    __STATUS_leak__
    <h2 id="leak-h">Blood leak alarm</h2>
    <p class="eqc-when">The machine reports blood in the used dialysate. Treat it as real until it is proven false.</p>
  </header>
  <ol class="eqc-steps">
    <li><span class="eqc-n">1</span><div><b>Patient first.</b> Awake? Pressure, pulse, chills, chest or back pain?</div></li>
    <li class="eqc-stop"><span class="eqc-n">!</span><div><b>Blood in the lines translucent or &ldquo;port-wine&rdquo;?</b> Hemolysis, not a leak: stop, clamp, <b>do not return it,</b> call now (<a href="#hemolysis">Card 6</a>).</div></li>
    <li><span class="eqc-n">2</span><div><b>Check the dialysate outflow line</b> for a pink tinge.</div></li>
    <li><span class="eqc-n">3</span><div><b>Test the used dialysate</b> with a blood test strip, per protocol.</div></li>
    <li><span class="eqc-n">4</span><div><b>Positive: stop on this dialyzer.</b> Pump off, clamp. <b>No rinse-back by habit:</b> only if protocol and the attending say so.</div></li>
    <li><span class="eqc-n">5</span><div><b>Negative: reset once.</b> Alarms again: call the technician. <b>Never bypass the detector.</b></div></li>
    <li><span class="eqc-n">6</span><div><b>Call the attending</b> for any confirmed leak. Keep the dialyzer, record the lot, watch for fever.</div></li>
  </ol>
  <details class="eqc-det">
    <summary>Why, the machine, false alarms and reporting</summary>
    <ul>
      <li><b>The machine:</b> most stop ultrafiltration (UF) and send the dialysate to bypass on a blood leak alarm; some also stop the blood pump. Know your models.</li>
      <li><b>Why no automatic rinse-back:</b> a torn membrane lets blood out into the dialysate, and non-sterile dialysate may reach the blood. Practice on returning the blood differs with the size of the leak and rests on custom, not trial evidence; if unsure, keep it clamped until you have asked.</li>
      <li><b>Hemolysis</b> is a different emergency: blood in the lines looks translucent, cherry-red or &ldquo;port-wine&rdquo;, often with chest, back or belly pain, and the circuit blood carries released potassium. Call the physician at once. Check every patient on the same water and concentrate supply, and keep the circuit and dialysate for investigation.</li>
      <li><b>Where to look and test:</b> the dialysate outflow line runs from the dialyzer to the machine; take the sample from that side. <b>False alarms</b> come from air bubbles in the dialysate or a dirty or fogged detector. A detector that cannot be made to pass is a machine out of service, not a sensor to work around.</li>
      <li><b>After a confirmed leak:</b> estimate and record the blood lost in the circuit; record the dialyzer brand, lot and, if reprocessed, the reuse number. A new dialyzer and lines, and any restart, only on the attending nephrologist&rsquo;s order. Check temperature and blood pressure before the patient goes home.</li>
      <li><b>Report:</b> incident report; tell the reprocessing staff and the biomedical technician. Repeated failures from one dialyzer lot are reported to the supplier, per unit policy.</li>
    </ul>
  </details>
  <p class="eqc-foot">Your unit&rsquo;s protocol decides. Learn it: <a href="physician-on-duty-16-when-the-circuit-fails.html">Physician-on-Duty 16</a> &middot; <a href="hemodialysis-technician-09-the-hemodialysis-session.html">Dialysis Technician 9</a> &middot; <a href="dialysis-biomedical-technician-07-protective-systems-alarm-testing.html">Biomedical Technician 7</a>.__SOURCES_leak__</p>
</article>
"""

import json as _json, importlib.util as _ilu
_spec = _ilu.spec_from_file_location("emergency_cards_data", Path(__file__).with_name("emergency_cards_data.py"))
D = _ilu.module_from_spec(_spec); _spec.loader.exec_module(D)
REFS = _json.loads((ROOT / "data" / "academy-emergency-cards-refs.json").read_text(encoding="utf-8"))
FIXED_REFS = {"code": ["aha9", "aha10", "lott", "hofacker", "handbook"], "leak": ["saha", "handbook"]}
CARD_NAMES.update({c["id"]: c["index"] for c in D.CARDS})
GROUP_COLOR = {"arrest": "arrest", "circuit": "circuit", "deterioration": "deter", "infection": "infect"}


def status_html(cid):
    """Visible review status line in a card header (text, not color alone)."""
    r = D.REVIEW.get(cid)
    if r and r.get("status") == "reviewed":
        return '<p class="eqc-stat ok">Validate against your own unit protocols</p>'
    if r and r.get("status") == "pending":
        return f'<p class="eqc-stat pend">{r["note"]}</p>'
    return '<p class="eqc-stat draft"><b>DRAFT</b> &middot; Clinical review required<span class="eqc-x"> &middot; not yet for bedside use</span></p>'


def sources_html(keys):
    for k in keys:
        assert k in REFS, f"unknown reference key {k}"
    links = " &middot; ".join(f'<a href="#ref-{k}">{D.SHORT[k]}</a>' for k in keys)
    return f' <span class="eqc-src">Sources: {links}. Checked {D.CHECKED}.</span>'


def learn_html(files):
    out = []
    for f in files:
        assert (ACADEMY / f).exists(), f"Learn-it lesson missing: {f}"
        out.append(f'<a href="{f}">{D.LESSONS[f]}</a>')
    return " &middot; ".join(out)


def card_html(c):
    cls = GROUP_COLOR[c["group"]]
    steps, n = [], 0
    for who, txt, same in c["steps"]:
        n += 1
        chip = ""
        if who or same:
            lab = ("At the same time &middot; " if same else "") + (who or "")
            chip = f'<span class="eqc-who">{lab.rstrip(" &middot;")}</span> '
        steps.append(f'    <li><span class="eqc-n">{n}</span><div>{chip}{txt}</div></li>')
    det = []
    for key, head in D.DET_ORDER:
        det.append(f'      <h3>{head}</h3>\n      <p>{c["det"][key]}</p>')
    return f"""
<article class="eqc eqc-{cls}" id="{c['id']}" aria-labelledby="{c['id']}-h">
  <header class="eqc-head">
    <div class="eqc-kicker">Emergency quick card {c['num']}</div>
    {status_html(c['id'])}
    <h2 id="{c['id']}-h">{c['title']}</h2>
    <p class="eqc-when"><b>Recognize:</b> {c['when']}</p>
  </header>
  <ol class="eqc-steps">
{chr(10).join(steps)}
  </ol>
  <div class="eqc-warn" role="note"><span class="eqc-warn-l">&#9888; Critical</span> {c['warn']}</div>
  <details class="eqc-det">
    <summary>Details: other causes, monitoring, circuit, blood return, escalation, restart, records</summary>
    <div class="eqc-detb">
{chr(10).join(det)}
    </div>
  </details>
  <p class="eqc-foot">Your unit&rsquo;s protocol decides. Learn it: {learn_html(c['learn'])}.{sources_html(c['refs'])}</p>
</article>"""


def index_html():
    items = {g: [] for g, _ in D.GROUPS}
    for c in D.FIXED_INDEX + D.CARDS:
        items[c["group"]].append(c)
    out = ['  <div class="eqc-index" role="navigation" aria-label="Card index">']
    for g, label in D.GROUPS:
        out.append(f'    <div class="eqc-ig eqc-ig-{GROUP_COLOR[g]}"><h2>{label}</h2><ul>')
        for c in sorted(items[g], key=lambda x: x["num"]):
            st = D.REVIEW.get(c["id"], {}).get("status")
            tag = "" if st in ("reviewed", "pending") else ' <span class="eqc-dr">draft</span>'
            out.append(f'      <li><a href="#{c["id"]}"><span class="eqc-in">{c["num"]}</span>{c["index"]}{tag}</a></li>')
        out.append('    </ul></div>')
    out.append('  </div>')
    return "\n".join(out)


CIRCUIT_WORDS = """  <details class="eqc-words">
    <summary>Circuit words used on every card</summary>
    <dl>
      <dt>Stop ultrafiltration (UF)</dt><dd>Fluid removal stops. Blood keeps flowing through the dialyzer.</dd>
      <dt>Stop the blood pump</dt><dd>Blood stops moving. The patient is still connected.</dd>
      <dt>Clamp</dt><dd>Close the line clamps (and needle or catheter clamps) so nothing moves in or out.</dd>
      <dt>Return the blood</dt><dd>Rinse the blood in the circuit back to the patient with saline. Each card says whether to.</dd>
      <dt>Disconnect</dt><dd>Separate the lines from the needles or catheter, which stay in place as access.</dd>
      <dt>End the treatment</dt><dd>The session is over for today. A restart needs a physician&rsquo;s order.</dd>
    </dl>
  </details>"""

STYLE = """
<style id="eqc-page">
.eqc-hero{padding:30px 0 18px;}
.eqc-hero h1{margin:10px 0 6px;}
.eqc-hero .hero-tagline{font-size:17px;color:var(--text-mid);margin:0;}
.eqc-main{max-width:900px;margin:0 auto;padding:8px 28px 40px;}
.eqc-bar{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:4px 0 14px;}
.eqc-jump{display:inline-flex;align-items:center;gap:8px;font:700 15px/1.2 Inter,system-ui,sans-serif;text-decoration:none;
  padding:12px 16px;border-radius:12px;color:#fff;background:#b91c1c;min-height:44px;box-sizing:border-box;}
.eqc-jump.leak{background:#9a3412;}
.eqc-jump:hover{filter:brightness(1.08);}
.eqc-btn{font:600 14.5px/1.2 Inter,system-ui,sans-serif;padding:11px 15px;border-radius:12px;border:1.5px solid var(--border);
  background:var(--white);color:var(--text);cursor:pointer;min-height:44px;}
.eqc-btn:hover{border-color:var(--teal);}
.eqc-save{border-color:var(--teal);color:var(--teal);}
.eqc-status{font-size:14px;color:var(--text-mid);margin:0 0 6px;}
.eqc-status.ok{color:var(--green);font-weight:600;}
.eqc-note{font-size:14px;line-height:1.55;color:var(--text-mid);background:var(--amber-soft,#fff7e6);border-left:3px solid var(--amber);
  padding:10px 14px;border-radius:8px;margin:0 0 18px;}
.eqc{background:var(--white);border:1px solid var(--border);border-radius:16px;overflow:hidden;margin:0 0 26px;
  box-shadow:0 2px 10px rgba(15,23,42,.06);scroll-margin-top:70px;}
.eqc-head{background:#b91c1c;color:#fff;padding:14px 20px 12px;}
.eqc-leak .eqc-head{background:#9a3412;}
.eqc-kicker{font:700 11.5px/1 Inter,system-ui,sans-serif;letter-spacing:.09em;text-transform:uppercase;opacity:.92;}
.eqc-head h2{font:800 25px/1.15 Inter,system-ui,sans-serif;margin:6px 0 6px;color:#fff;border:0;padding:0;}
.eqc-when{margin:0;font-size:15px;line-height:1.45;color:#fff;}
.eqc-when b{color:#fff;}
.eqc-when a{color:#fff;text-decoration:underline;font-weight:700;}
.eqc-refs a{color:var(--teal);word-break:break-all;}
.eqc-steps{list-style:none;margin:0;padding:6px 14px 4px;}
.eqc-steps>li{display:flex;gap:12px;align-items:flex-start;padding:8px 4px;border-bottom:1px solid var(--border);
  font-size:15.5px;line-height:1.5;color:var(--text);}
.eqc-steps>li:last-child{border-bottom:0;}
.eqc-steps b{color:var(--text);}
.eqc-n{flex:0 0 30px;height:30px;border-radius:50%;background:var(--navy,#1F3864);color:#fff;font:800 15px/30px Inter,system-ui,sans-serif;
  text-align:center;margin-top:1px;}
.eqc-stop{background:var(--red-soft);border-radius:10px;margin:2px 0;padding-left:8px !important;padding-right:8px !important;}
.eqc-stop .eqc-n{background:#b91c1c;}
.eqc-split{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin:8px 0;}
.eqc-split>div{border-radius:10px;padding:10px 12px;font-size:15px;line-height:1.48;}
.eqc-no{background:var(--red-soft);border-left:4px solid var(--red);}
.eqc-yes{background:var(--green-soft,#edf7ef);border-left:4px solid var(--green);}
.eqc-k{display:inline-block;font:700 12px/1 Inter,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.06em;color:var(--red);
  margin:6px 0 2px;}
.eqc-k::after{content:"";display:block;}
.eqc-det{border-top:1px solid var(--border);padding:0 20px;}
.eqc-det summary{cursor:pointer;font:700 14.5px/1.3 Inter,system-ui,sans-serif;color:var(--teal);padding:12px 0;min-height:24px;}
.eqc-det ul{margin:0 0 12px;padding-left:18px;}
.eqc-det li{font-size:14.5px;line-height:1.55;color:var(--text);margin:0 0 7px;}
.eqc-det a{color:var(--teal);}
.eqc-foot{margin:0;padding:10px 20px 14px;font-size:13.5px;line-height:1.5;color:var(--text-mid);border-top:1px solid var(--border);}
.eqc-foot a,.eqc-steps a{color:var(--teal);}
.eqc-more h2{font-family:Inter,system-ui,sans-serif;}
.eqc-more p,.eqc-more li{font-size:15.5px;line-height:1.65;color:var(--text-mid);}
.eqc-refs li{font-size:13.5px;line-height:1.5;margin:0 0 8px;color:var(--text-mid);}
.eqc-stat{display:inline-block;margin:6px 0 2px;padding:3px 9px;border-radius:999px;font:600 12px/1.35 Inter,system-ui,sans-serif;
  background:rgba(255,255,255,.18);color:#fff;border:1px solid rgba(255,255,255,.5);}
.eqc-stat.draft{background:#fff;color:#7a1a1a;border-color:#fff;}
.eqc-deter .eqc-head{background:#4B3280;}
.eqc-infect .eqc-head{background:#0e5a61;}
.eqc-arrest .eqc-head{background:#b91c1c;}
.eqc-circuit .eqc-head{background:#9a3412;}
.eqc-who{display:inline-block;font:700 11.5px/1.3 Inter,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.04em;
  color:var(--text-mid);border:1px solid var(--border);border-radius:6px;padding:1px 6px;margin:0 4px 2px 0;vertical-align:1px;}
.eqc-warn{margin:4px 14px 12px;padding:10px 12px;border-radius:10px;background:var(--red-soft);border:2px solid var(--red);
  font-size:15px;line-height:1.48;color:var(--text);}
.eqc-warn-l{display:inline-block;font:800 12.5px/1.3 Inter,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.05em;color:var(--red);margin-right:4px;}
.eqc-warn a{color:var(--teal);}
.eqc-detb h3{font:700 14px/1.3 Inter,system-ui,sans-serif;margin:10px 0 3px;color:var(--text);}
.eqc-detb p{font-size:14.5px;line-height:1.55;color:var(--text);margin:0 0 6px;}
.eqc-detb{padding-bottom:10px;}
.eqc-src{display:block;margin-top:4px;}
.eqc-index{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 18px;margin:0 0 16px;}
.eqc-ig h2{font:800 13px/1.3 Inter,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.06em;margin:0 0 6px;padding:0 0 4px;
  border-bottom:3px solid var(--red);color:var(--text);}
.eqc-ig-circuit h2{border-color:#9a3412;}
.eqc-ig-deter h2{border-color:#4B3280;}
.eqc-ig-infect h2{border-color:#0e5a61;}
.eqc-ig ul{list-style:none;margin:0;padding:0;}
.eqc-ig li{margin:0 0 6px;}
.eqc-ig a{display:flex;align-items:center;gap:8px;min-height:44px;box-sizing:border-box;padding:8px 10px;border:1px solid var(--border);
  border-radius:10px;background:var(--white);color:var(--text);text-decoration:none;font:600 15px/1.25 Inter,system-ui,sans-serif;}
.eqc-ig a:hover{border-color:var(--teal);}
.eqc-in{flex:0 0 26px;height:26px;border-radius:50%;background:var(--navy,#1F3864);color:#fff;font:800 13px/26px Inter,system-ui,sans-serif;text-align:center;}
.eqc-dr{margin-left:auto;font:700 11px/1.2 Inter,system-ui,sans-serif;text-transform:uppercase;letter-spacing:.05em;color:var(--text-mid);
  border:1px dashed var(--text-mid);border-radius:5px;padding:2px 5px;}
.eqc-words{border:1px solid var(--border);border-radius:12px;padding:0 14px;margin:0 0 20px;background:var(--white);}
.eqc-words summary{cursor:pointer;font:700 14.5px/1.3 Inter,system-ui,sans-serif;color:var(--teal);padding:12px 0;}
.eqc-words dl{margin:0 0 12px;display:grid;grid-template-columns:max-content 1fr;gap:6px 14px;font-size:14.5px;line-height:1.45;}
.eqc-words dt{font-weight:700;color:var(--text);}
.eqc-words dd{margin:0;color:var(--text-mid);}
html[data-theme="dark"] .eqc-deter .eqc-head{background:#3d2970;}
html[data-theme="dark"] .eqc-infect .eqc-head{background:#0b474d;}
html[data-theme="dark"] .eqc-arrest .eqc-head{background:#8f1d1d;}
html[data-theme="dark"] .eqc-circuit .eqc-head{background:#7c2d12;}
html[data-theme="dark"] .eqc-in{background:#2d4a7a;}
html[data-theme="dark"] .eqc-stat.draft{background:#fff;color:#7a1a1a;}
html[data-theme="dark"] .eqc-head{background:#8f1d1d;}
html[data-theme="dark"] .eqc-leak .eqc-head{background:#7c2d12;}
html[data-theme="dark"] .eqc-jump{background:#8f1d1d;}
html[data-theme="dark"] .eqc-jump.leak{background:#7c2d12;}
html[data-theme="dark"] .eqc-n{background:#2d4a7a;}
html[data-theme="dark"] .eqc-stop .eqc-n{background:#8f1d1d;}
html[data-theme="dark"] .eqc-yes{background:#13261a;}
html[data-theme="dark"] .eqc-note{background:#2a1f0a;}
@media (max-width:640px){
  .eqc-main{padding:6px 12px 30px;}
  .eqc-head{padding:10px 14px 9px;}
  .eqc-kicker{display:none;}
  .eqc-head h2{font-size:21px;margin:0 0 4px;}
  .eqc-when{font-size:14px;}
  .eqc-steps{padding:2px 8px;}
  .eqc-steps>li{font-size:14.5px;line-height:1.4;gap:9px;padding:6px 2px;}
  .eqc-det{padding:0 14px;}
  .eqc-foot{padding:8px 14px 10px;font-size:12.5px;}
  .eqc-det summary{padding:9px 0;font-size:14px;}
  .eqc-n{flex-basis:26px;height:26px;line-height:26px;font-size:13.5px;}
  .eqc-split{grid-template-columns:1fr;}
  .eqc-index{grid-template-columns:1fr;gap:10px;}
  .eqc-x{display:none;}
  .eqc-stat{font-size:11px;padding:2px 8px;margin:0 0 4px;}
  .eqc-when{font-size:13.5px;line-height:1.4;}
  .eqc-head h2{font-size:19.5px;line-height:1.18;}
  .eqc-steps>li{font-size:14px;line-height:1.36;padding:5px 2px;}
  .eqc-who{font-size:9.5px;padding:0 4px;margin-right:3px;letter-spacing:.02em;}
  .eqc-warn{font-size:13.5px;line-height:1.4;padding:8px 10px;}
  .eqc-words dl{grid-template-columns:1fr;gap:2px;}
  .eqc-words dd{margin-bottom:6px;}
  .eqc-warn{margin:4px 8px 10px;font-size:14.5px;}
  .eqc-who{font-size:10.5px;}
}
@media print{
  @page{size:A4;margin:10mm;}
  .site-header,.guide-footer,.eqc-bar,.eqc-status,.eqc-hero,.eqc-index,.eqc-note,.rcm-share,.rcm-share-slot,.float-controls,.float-controls-left{display:none !important;}
  .eqc-more{break-before:page;}
  html,body,main.eqc-main,.eqc,.eqc-words,.eqc-det,.eqc-more{background:#fff !important;color:#111 !important;}
  .eqc-steps>li,.eqc-steps b,.eqc-det li,.eqc-det li b,.eqc-detb p,.eqc-detb h3,.eqc-foot,.eqc-words dt,.eqc-words dd,.eqc-refs li,.eqc-more h2,.eqc-warn{color:#111 !important;}
  .eqc-steps>li{border-color:#ccc !important;}
  .eqc-warn{background:#fff0f0 !important;border-color:#b91c1c !important;}
  .eqc-stop{background:#fff0f0 !important;}
  .eqc-who{color:#333 !important;border-color:#999 !important;}
  .eqc a,.eqc-refs a,.eqc-words summary,.eqc-det summary{color:#0e4a50 !important;}
  .eqc-n,.eqc-in{background:#1F3864 !important;color:#fff !important;}
  .eqc-more>p{display:none;}
  .eqc-main{max-width:none;padding:0;}
  .eqc{box-shadow:none;break-before:page;border-color:#999;}
  .eqc-steps>li,.eqc-warn,.eqc-detb h3,.eqc-detb p,.eqc-words dt,.eqc-words dd{break-inside:avoid;}
  .eqc-detb h3{break-after:avoid;}
  .eqc-head,.eqc-warn,.eqc-stat,.eqc-in{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
  .eqc-head,.eqc-n,.eqc-no,.eqc-yes,.eqc-stop{-webkit-print-color-adjust:exact;print-color-adjust:exact;}
  .eqc-steps>li{font-size:12.5px;padding:5px 2px;}
  .eqc-det li{font-size:11.5px;margin:0 0 4px;}
  .eqc a::after{content:none !important;}
  .eqc-det summary{padding:6px 0;}
  .eqc-split>div{font-size:12px;}
}
</style>
"""

SCRIPT = r"""
<script>
/* Emergency quick cards: save this one page into the Schola offline cache (works with no signal later). */
(function () {
  var KEY = '/academy/emergency-cards', CACHE = 'schola-saved', MAN = '/academy/schola-offline.json';
  var btn = document.getElementById('eqc-save'), st = document.getElementById('eqc-status');
  var pr = document.getElementById('eqc-print');
  if (pr) pr.addEventListener('click', function () { window.print(); });
  var opened = [];   /* printed cards carry the details too */
  window.addEventListener('beforeprint', function () {
    opened = [].filter.call(document.querySelectorAll('details.eqc-det, details.eqc-words'), function (d) { return !d.open; });
    opened.forEach(function (d) { d.open = true; });
  });
  window.addEventListener('afterprint', function () { opened.forEach(function (d) { d.open = false; }); opened = []; });
  if (!btn || !st) return;
  var ok = ('serviceWorker' in navigator) && ('caches' in window);
  var ios = /iPad|iPhone|iPod/.test(navigator.userAgent) || (navigator.platform === 'MacIntel' && navigator.maxTouchPoints > 1);
  var standalone = (window.matchMedia && matchMedia('(display-mode: standalone)').matches) || navigator.standalone === true;
  function say(t, good) { st.textContent = t; st.className = 'eqc-status' + (good ? ' ok' : ''); }
  function when(s) { try { return new Date(s).toLocaleDateString('en-US', { month: 'short', day: 'numeric', year: 'numeric' }); } catch (e) { return ''; } }
  if (!ok) { btn.hidden = true; say('This browser cannot save pages for offline use. Print the cards instead.'); return; }
  navigator.serviceWorker.register('/academy/schola-sw.js', { scope: '/academy/' }).catch(function () {});
  var iosTip = ios && !standalone ? ' On iPhone or iPad, Safari may clear saved pages after a few weeks: add Schola to the Home Screen and save from there.' : '';
  caches.open(CACHE).then(function (c) { return c.match(KEY); }).then(function (r) {
    if (r) {
      var at = ''; try { at = localStorage.getItem('rcm-eqc-saved') || ''; } catch (e) {}
      say('Saved on this device' + (at ? ' on ' + when(at) : '') + '. These cards open with no signal.' + iosTip, true);
      btn.textContent = 'Update saved copy';
    }
  }).catch(function () {});
  btn.addEventListener('click', function () {
    btn.disabled = true; say('Saving…');
    if (navigator.storage && navigator.storage.persist) navigator.storage.persist().catch(function () {});
    var hash = '';
    fetch(MAN, { cache: 'no-cache' }).then(function (r) { return r.ok ? r.json() : null; }).catch(function () { return null; })
      .then(function (m) {
        if (m && m.files) for (var i = 0; i < m.files.length; i++) if (m.files[i][0] === KEY) { hash = m.files[i][1]; break; }
        return fetch(KEY, { cache: 'no-cache', credentials: 'same-origin' });
      })
      .then(function (r) {
        if (!r.ok) throw new Error(r.status);
        var type = r.headers.get('Content-Type') || 'text/html; charset=utf-8';
        return r.blob().then(function (b) {
          var h = { 'Content-Type': type }; if (hash) h['X-RCM-Hash'] = hash;
          return caches.open(CACHE).then(function (c) { return c.put(KEY, new Response(b, { headers: h })); });
        });
      })
      .then(function () {
        var now = new Date().toISOString(); try { localStorage.setItem('rcm-eqc-saved', now); } catch (e) {}
        say('Saved on this device on ' + when(now) + '. These cards open with no signal.' + iosTip, true);
        btn.textContent = 'Update saved copy'; btn.disabled = false;
      })
      .catch(function () { btn.disabled = false; say('Could not save: check your connection and tap again.'); });
  });
})();
</script>
"""


def used_refs():
    keys = []
    for k in FIXED_REFS["code"] + FIXED_REFS["leak"] + [k for c in D.CARDS for k in c["refs"]]:
        if k not in keys:
            keys.append(k)
    return sorted(keys, key=lambda k: re.sub(r"<[^>]+>|&[a-z]+;", "", REFS[k]).lower())


def fixed_cards():
    out = []
    for cid, html in (("code", CODE_CARD), ("leak", LEAK_CARD)):
        html = html.replace(f"__STATUS_{cid}__", status_html(cid)).replace(f"__SOURCES_{cid}__", sources_html(FIXED_REFS[cid]))
        out.append(html)
    return out


def main_html():
    refs = "\n".join(f'      <li id="ref-{k}">{REFS[k]}</li>' for k in used_refs())
    code, leak = fixed_cards()
    new = "\n".join(card_html(c) for c in sorted(D.CARDS, key=lambda c: c["num"]))
    ndraft = sum(1 for c in D.CARDS if D.REVIEW.get(c["id"], {}).get("status") != "reviewed")
    total = len(D.CARDS) + 2
    return f"""
<!-- ═══ HERO ════════════════════════════════════ -->
<section class="hero eqc-hero">
  <div class="container">
    <div class="nc-bar"><a href="./">Renal Care Academy</a><span class="nc-sep">›</span><span>Emergency quick cards</span></div>
    <h1>Emergency quick cards</h1>
    <p class="hero-tagline">{total} cards, one screen each, for the first minutes at the chair</p>
  </div>
</section>
{STYLE}
<main class="container eqc-main">
  <div class="eqc-bar" role="group" aria-label="Save and print">
    <button type="button" class="eqc-btn eqc-save" id="eqc-save">Save for offline use</button>
    <button type="button" class="eqc-btn" id="eqc-print">Print cards</button>
  </div>
  <p class="eqc-status" id="eqc-status" aria-live="polite">Save these cards once while you have signal; they then open on this device with no signal. Saving any track in Schola saves them too.</p>
  <p class="eqc-note">These cards are a memory aid for trained adult hemodialysis staff, not a protocol. <b>Your unit&rsquo;s protocol decides, and the attending nephrologist is called for every event.</b> Drugs are named without doses: doses, limits and stock are set by your unit. {("Validate every card against your own unit protocols before use.") if ndraft == 0 else (str(ndraft) + " of the " + str(total) + " cards are marked <b>DRAFT</b> until a clinical reviewer signs them off.")}</p>
{index_html()}
{CIRCUIT_WORDS}
{code}
{leak}
{new}
  <section class="eqc-more" id="about-cards">
    <h2>About these cards</h2>
    <p>Sudden cardiac death is the most common cause of death in people on hemodialysis, and in a United States registry of cardiac arrests in outpatient dialysis clinics, most patients received staff-started cardiopulmonary resuscitation (CPR), but a defibrillator was applied in only about six in ten. The first minute is decided by people who have rehearsed it. Each card follows the Academy modules linked at its foot, where the reasoning, the evidence and practice cases are.</p>
    <p>Each card lists who acts, which circuit step to take, and whether the blood is returned. Steps marked &ldquo;At the same time&rdquo; run alongside the step before them. Every card names someone to watch the other patients on the floor. Print a set for the crash cart and the nurses&rsquo; station, and run a five-minute drill from one card at the start of a shift.</p>
    <p>The AHA (American Heart Association) and ERC (European Resuscitation Council) guidelines below apply in the dialysis unit as everywhere; the ERC guideline has a section on cardiac arrest in the dialysis unit. Where sources disagree, the card says so and leaves the choice to the unit protocol. References were checked on {D.CHECKED}.</p>
    <h2>References</h2>
    <ol class="eqc-refs">
{refs}
    </ol>
  </section>
</main>
"""


def sub_meta(head):
    head = re.sub(r"<title>.*?</title>", f"<title>{TITLE}</title>", head, count=1, flags=re.S)
    for prop, val in (("og:title", TITLE), ("twitter:title", TITLE), ("og:description", DESC), ("twitter:description", DESC), ("og:url", URL), ("twitter:url", URL)):
        head = re.sub(r'(<meta (?:property|name)="%s" content=")[^"]*(")' % re.escape(prop), lambda m: m.group(1) + val + m.group(2), head)
    head = re.sub(r'(<meta name="description" content=")[^"]*(")', lambda m: m.group(1) + DESC + m.group(2), head, count=1)
    head = re.sub(r'(<link rel="canonical" href=")[^"]*(")', lambda m: m.group(1) + URL + m.group(2), head, count=1)
    head = re.sub(r'<script type="application/ld\+json">.*?</script>\s*', "", head, flags=re.S)
    head = re.sub(r'<meta name="robots"[^>]*>\s*', "", head)
    return head


def build_page():
    land = (ACADEMY / "index.html").read_text(encoding="utf-8")
    head, rest = land.split("</head>", 1)
    head = sub_meta(head + "</head>")
    body_open = rest[:rest.index("</header>") + len("</header>")]
    tail = rest[rest.index('<footer class="guide-footer">'):]
    tail = re.sub(r'<button class="print-btn".*?</button>\s*', "", tail, count=1, flags=re.S)
    tail = re.sub(r'\n?<script src="[^"]*assets/(academy-|schola|tech-course|guide-rail|share-buttons|image-lightbox)[^"]*" defer></script>', "", tail)
    page = head + body_open + "\n" + main_html() + "\n" + tail
    i = page.rfind("</body>")
    return page[:i] + SCRIPT + page[i:]


CALLOUT = f"""{START}
<style id="eqc-callout-css">
.eqc-callout{{max-width:860px;margin:18px auto 0;padding:0 32px;}}
.eqc-callout a{{display:flex;line-height:1.3;gap:14px;align-items:center;text-decoration:none;background:var(--red-soft);border:1px solid rgba(185,28,28,.25);
  border-left:5px solid var(--red);border-radius:14px;padding:14px 18px;color:var(--text);}}
.eqc-callout a:hover{{border-color:var(--red);}}
.eqc-callout .eqc-ic{{font-size:26px;line-height:1;}}
.eqc-callout b{{display:block;font:800 16.5px/1.25 Inter,system-ui,sans-serif;color:var(--red);}}
.eqc-callout span.t{{display:block;font-size:14.5px;line-height:1.45;color:var(--text-mid);}}
@media (max-width:640px){{.eqc-callout{{padding:0 16px;}}}}
@media print{{.eqc-callout{{display:none;}}}}
</style>
<div class="eqc-callout"><a href="emergency-cards.html"><span class="eqc-ic" aria-hidden="true">&#128680;</span><span><b>Emergency quick cards</b><span class="t">One-screen action cards for the first minutes at the chair: a code, the blood leak alarm, low blood pressure, a needle out, air, hemolysis, reactions, chest pain, rhythm, potassium, sugar, seizure, stroke and fever. Save them on your phone for use with no signal, or print them for the crash cart.</span></span></a></div>
{END}"""


def module_box(cards):
    links = " &middot; ".join(f'<a href="emergency-cards.html#{c}" style="color:var(--teal);font-weight:600;">{CARD_NAMES[c]}</a>' for c in cards)
    label = "Emergency quick card" + ("s" if len(cards) > 1 else "")
    return (f'{MSTART}\n<div class="alert alert-red" style="max-width:860px;margin:18px auto;">'
            f'<div class="alert-body"><p style="margin:0;"><strong>&#128680; {label}:</strong> {links}. '
            f'One screen each, saved for use with no signal. Print a copy for the crash cart.</p></div></div>\n{MEND}')


def patch_landing(dry):
    p = ACADEMY / "index.html"
    old = p.read_text(encoding="utf-8")
    text = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", old, flags=re.S)
    m = re.search(r'<nav class="nav-strip">.*?</nav>\n?', text, flags=re.S)
    if not m:
        print("landing page: no nav strip found; callout not placed")
        return 0
    text = text[:m.end()] + CALLOUT + "\n" + text[m.end():]
    if text != old:
        if not dry:
            p.write_text(text, encoding="utf-8")
        return 1
    return 0


def patch_modules(dry):
    n = 0
    for name, cards in MODULE_LINKS.items():
        p = ACADEMY / name
        if not p.exists():
            print(f"  module not found, skipped: {name}")
            continue
        old = p.read_text(encoding="utf-8")
        text = re.sub(r"\n?" + re.escape(MSTART) + r".*?" + re.escape(MEND), "", old, flags=re.S)
        m = re.search(r'<section class="section" id="(skills|quiz)"', text)
        if not m:
            print(f"  no skills/quiz section, skipped: {name}")
            continue
        text = text[:m.start()] + module_box(cards) + "\n" + text[m.start():]
        if text != old:
            n += 1
            if not dry:
                p.write_text(text, encoding="utf-8")
    return n


def main():
    dry = "--dry-run" in sys.argv
    page = build_page()
    dst = ACADEMY / PAGE
    changed = 0
    if not dst.exists() or dst.read_text(encoding="utf-8") != page:
        changed += 1
        if not dry:
            dst.write_text(page, encoding="utf-8")
    changed += patch_landing(dry)
    changed += patch_modules(dry)
    print(f"academy emergency quick cards: {changed} page(s) updated" + (" [dry run]" if dry else ""))


if __name__ == "__main__":
    main()
