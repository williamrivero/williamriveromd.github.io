# -*- coding: utf-8 -*-
"""Convert the UOM/UMH v2 Markdown packet (tools/techcourses/uom/src/*.md) into the native module files
(m01.py ... m19.py) read by generate_tech_courses.py. Run from the repo root:

    python3 tools/techcourses/uom/packet_to_package.py

The Markdown packet stays the editorial source. Re-run this after editing a module, then run
python3 generate_tech_courses.py --course uom --patch.
"""
import html
import re
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "src"

# In-text author-year citations in the packet -> reference keys ([[key]] in the module text).
CITES = [
    (r"\(Starmer et al\., \*NEJM\* 2014\)", "uom_starmer2014"),
    (r"\(Patel et al\., \*AJKD\* 2013\)", "dch_patel2013"),
    (r"\(Li et al\., \*JAMA Network Open\* 2024\)", "uom_li2024"),
    (r"\(Plantinga et al\., \*JAMA Network Open\* 2024; Module 03\)", "uom_plantinga2024"),
    (r"\(Yoder et al\., \*AJKD\* 2013; Plantinga et al\., \*JAMA Network Open\* 2024\)", "uom_yoder2013]][[uom_plantinga2024"),
    (r"\(Plantinga et al\., \*JAMA Network Open\* 2024\)", "uom_plantinga2024"),
    (r"\(Yoder et al\., \*AJKD\* 2013\)", "uom_yoder2013"),
    (r"\(Lurie et al\., \*AJKD\* 2015\)", "dch_lurie2015"),
    (r"\(Kelman et al\., \*AJKD\* 2015\)", "uom_kelman2015"),
    (r"\(Cohen et al\., \*Kidney Medicine\* 2020\)", "uom_cohen2020"),
    (r"\(Yi et al\., \*Infection Control and Hospital Epidemiology\* 2016\)", "uom_yi2016"),
    (r"\(Saran et al\., \*Kidney International\* 2006\)", "uom_saran2006"),
    (r"\(Saran et al\., \*Kidney International\* 2003\)", "dch_saran2003"),
    (r"\(Perla, Provost and Murray, \*BMJ Quality & Safety\* 2011\)", "uom_perla2011"),
    (r"\(Lee and Cha, \*Scientific Reports\* 2023\)", "uom_leecha2023"),
    (r"\(Gray et al\., \*Nephrology\* 2015\)", "uom_gray2015"),
    (r"\(Foley et al\., \*NEJM\* 2011\)", "dch_foley2011"),
    (r"\(CDC, \*MMWR Recommendations and Reports\* 2001\)", "uom_cdc2001"),
    (r"\(CDC NHSN\)", "cdc_dialysis"),
    (r"\(\*MMWR\* 1996\)", "uom_cdc1996"),
]
# First mention of a named source in a module gets a citation after it.
FIRST = [
    (r"DOH AO 2012-0001", "doh2012"),
    (r"(?:DOH )?AO 2013-0003", "dch_doh2013"),
    (r"RA 9173 §29", "pd_ra9173"),
    (r"RA 10173", "dch_ra10173"),
    (r"PhilHealth Circular 2024-0023 \(Revision 2\)", "dch_philhealth2024"),
    (r"PSN 2024 HD Guidelines \(3rd ed\.\)", "psn2024"),
    (r"KDOQI \(2015\)", "dch_kdoqi2015"),
    (r"The HEMO trial \(2002\)", "uom_eknoyan2002"),
    (r"KDIGO advises against routinely targeting high hemoglobin with ESAs", "uom_kdigo_anemia2012"),
    (r"KDIGO's guideline on HCV in CKD \(2018\)", "uom_kdigo_hcv2018"),
    (r"ISO 23500 series \(second edition 2024\)", "iso23500_1"),
    (r"in Caruaru, Brazil", "dch_jochimsen1998"),
    (r"within 72 hours of knowledge", "dch_npc1603"),
    (r"Wage Order NCR-28 raised", "uom_wo_ncr28"),
    (r"15% of monthly salary credit \(MSC\)", "uom_sss2025"),
    (r"PhilHealth Advisory 2025-0002", "uom_ph_pa2025"),
    (r"Pag-IBIG Circular 460", "uom_hdmf460"),
    (r"Labor Code Art\. 83", "uom_laborcode"),
    (r"Under Art\. 83", "uom_laborcode"),
    (r"PD 851", "uom_pd851"),
    (r"RA 11210", "uom_ra11210"),
    (r"PRDR data as reported by NKTI", "dch_philhealth_news2024"),
    (r"ISO 23500 for the water system", "iso23500_1"),
    (r"PSN and DOH-aligned reprocessing policy", "psn2024"),
    (r"Ease of Paying Taxes Act \(RA 11976, 2024\)", "uom_ra11976"),
    (r"submitted to PhilHealth or other payer", "dch_philhealth2024"),
    (r"action level 50, maximum 100 under the facility program\)", "iso23500_1"),
    (r"Medical Director decides on early dialysis", "dch_lurie2015"),
    (r"has used 152 of 156 sessions", "dch_philhealth2024"),
]

FIG_A = "{{fig:uom%sa}}"
FIG_B = "{{fig:uom%sb}}"
FIG_C = "{{fig:uom%sc}}"

READINGS = {
    "01": [("dialysis-qapi-vs-cqi.html", "How dialysis units organize quality assessment and improvement."),
           ("nephrology-workforce-crisis-or-opportunity.html", "The people side of running a kidney service.")],
    "02": [("dialysis-qapi-vs-cqi.html", "Quality programs an inspector will ask to see.")],
    "03": [("nephrology-workforce-crisis-or-opportunity.html", "Workforce pressures in nephrology and what helps.")],
    "04": [("dialysis-adequacy.html", "Why time on dialysis and dose matter."),
           ("hemodialysis-transfer-guide.html", "Moving a patient safely between units.")],
    "05": [("dialysis-access-infection.html", "Access infections, from the patient side."),
],
    "06": [("dialysis-water-treatment-systems.html", "The full clinical and engineering reference on dialysis water.")],
    "07": [("code-blue-acls-dialysis-unit.html", "Running a cardiac arrest in a dialysis unit."),
           ("hemodialysis-complications.html", "The complications staff must recognize during treatment.")],
    "08": [("dialysis-machine-assignment.html", "Assigning machines and stations safely.")],
    "09": [("dialysis-qapi-vs-cqi.html", "Quality assessment and continuous improvement in dialysis."),
           ("dialysis-adequacy.html", "What Kt/V measures and what it does not.")],
    "10": [("zero-balance-billing-philhealth.html", "No balance billing and what patients may be charged."),
           ("dialysis-qapi-vs-cqi.html", "Quality records that support a clean claim.")],
    "11": [("zero-balance-billing-philhealth.html", "How PhilHealth rules shape the money side of a unit.")],
    "12": [("typhoon-disaster-preparedness-dialysis.html", "Typhoon preparedness for dialysis patients."),
           ("climate-extremes-kidney-care.html", "Heat, floods and kidney care.")],
    "13": [("hemodialysis-transfer-guide.html", "Transfers between units and hospitals.")],
    "14": [("hemodialysis-complications.html", "Complications staff must recognize during treatment.")],
    "15": [("nephrology-workforce-crisis-or-opportunity.html", "Burnout, retention and team culture."),
           ("dialysis-access-care.html", "Access care, from the patient side.")],
    "16": [("zero-balance-billing-philhealth.html", "Billing rules behind the receivables.")],
    "17": [("nephrology-workforce-crisis-or-opportunity.html", "Why fair pay and schedules keep teams together.")],
    "18": [("nephrology-workforce-crisis-or-opportunity.html", "Retention and the employment relationship.")],
    "19": [("typhoon-disaster-preparedness-dialysis.html", "The patient side of the capstone scenario."),
           ("dialysis-qapi-vs-cqi.html", "Turning findings into improvement.")],
}
CALCS = {k: ["calc-dialysis-clinical-head-toolkit.html"] for k in ("03", "04", "08", "11", "12", "19")}
B_SECTION = {"01": "Doing it on Monday", "02": "Writing a CAPA", "03": "Doing it on Monday", "04": "Rescheduling after",
             "05": "Serology", "06": "Doing it on Monday", "07": "Readiness checklist", "08": "Recall and quarantine",
             "09": "The data dictionary", "10": "Calculator CALC-07", "11": "Revenue, recognition", "12": "Calculator CALC-12",
             "13": "Healthcare waste", "14": "Balancing", "15": "Coaching", "16": "Purchasing and payment", "17": "Cutoff review",
             "18": "Statutory leaves", "19": "Sample scenario"}
CRIT_WORDS = re.compile(r"\b(hold|release|drill|ratio|isolation|recall|reconcil|evacuat|disconnect|serology|competenc)", re.I)


def esc(s):
    return html.escape(s, quote=False)


def inline(s):
    s = esc(s)
    s = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", lambda m: m.group(1), s)       # packet-internal links -> text
    s = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", s)
    s = re.sub(r"(?<![\w*])\*(?!\s)(.+?)(?<!\s)\*(?![\w*])", r"<em>\1</em>", s)
    s = re.sub(r"`([^`]+)`", r"<code>\1</code>", s)
    s = s.replace(" - ", " &ndash; ")
    s = re.sub(r"&amp;([a-z]+|#\d+);", r"&\1;", s)                       # named entities written in the Markdown
    s = re.sub(r"&lt;(/?(?:br|strong|em|sup|sub))&gt;", r"<\1>", s)        # a few inline tags allowed in macros
    return s


def blocks(lines):
    """Minimal Markdown -> HTML for the packet's subset (paragraphs, lists, tables, h3)."""
    out, i = [], 0
    while i < len(lines):
        ln = lines[i]
        if not ln.strip():
            i += 1
            continue
        if ln.lstrip().startswith("{{"):
            buf = [ln.strip()]
            while not buf[-1].endswith("}}") and i + 1 < len(lines):
                i += 1
                buf.append(lines[i].strip())
            out.append(inline(" ".join(buf)))
            i += 1
        elif ln.startswith("### "):
            out.append(f"<h3>{inline(ln[4:].strip())}</h3>")
            i += 1
        elif ln.lstrip().startswith("|"):
            rows = []
            while i < len(lines) and lines[i].lstrip().startswith("|"):
                rows.append(lines[i].strip())
                i += 1
            cells = [[c.strip() for c in r.strip("|").split("|")] for r in rows]
            head, body = cells[0], [c for c in cells[2:]]
            t = ["<div class=\"table-wrap\"><table>", "<thead><tr>" + "".join(f"<th>{inline(c)}</th>" for c in head) + "</tr></thead>", "<tbody>"]
            t += ["<tr>" + "".join(f"<td>{inline(c)}</td>" for c in r) + "</tr>" for r in body]
            t.append("</tbody></table></div>")
            out.append("\n".join(t))
        elif re.match(r"^\s*- ", ln):
            items = []
            while i < len(lines) and re.match(r"^\s*- ", lines[i]):
                items.append(re.sub(r"^\s*- (\[[ x]\] )?", "", lines[i]).strip())
                i += 1
            out.append("<ul>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ul>")
        elif re.match(r"^\s*\d+\. ", ln):
            items = []
            while i < len(lines) and re.match(r"^\s*\d+\. ", lines[i]):
                items.append(re.sub(r"^\s*\d+\. ", "", lines[i]).strip())
                i += 1
            out.append("<ol>" + "".join(f"<li>{inline(x)}</li>" for x in items) + "</ol>")
        else:
            para = []
            while i < len(lines) and lines[i].strip() and not re.match(r"^(\s*- |\s*\d+\. |\s*\||### |\s*\{\{)", lines[i]):
                para.append(lines[i].strip())
                i += 1
            out.append(f"<p>{inline(' '.join(para))}</p>")
    return "\n".join(out)


def cite(text, used):
    for pat, key in CITES:
        text = re.sub(r"\s?" + pat, "[[" + key + "]]", text)
    used |= set(re.findall(r"\[\[([a-z0-9_]+)\]\]", text))
    for pat, key in FIRST:
        if key in used:
            continue
        m = re.search(pat, text)
        if m:
            text = text[:m.end()] + "[[" + key + "]]" + text[m.end():]
            used.add(key)
    return text


def after_first_para(h, fig):
    j = h.find("</p>")
    return h[:j + 4] + "\n" + fig + "\n" + h[j + 4:] if j >= 0 else fig + "\n" + h


def slugify(s):
    s = re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")
    return s[:40].rstrip("-")


def parse(path):
    mid = path.name[:2]
    raw = path.read_text(encoding="utf-8")
    used = set()
    body, sep, bank = raw.partition("\n## Question bank")
    raw = cite(body, used) + sep + bank
    title = re.search(r"^# \d+\. (.+)$", raw, re.M).group(1).strip()
    wm = re.search(r"^> \*\*Why this matters\.\*\* (.+)$", raw, re.M)
    why = wm.group(1).strip() if wm else ""
    secs = re.split(r"^## ", raw, flags=re.M)[1:]
    mod = {"objectives": [], "sections": [], "debrief": [], "quiz": [], "readings": READINGS.get(mid, [])}
    if mid in CALCS:
        mod["calcs"] = CALCS[mid]
    mod["big"] = f"<p>{inline(why)}</p>" if why else ""
    for sec in secs:
        head, _, body = sec.partition("\n")
        head = head.strip()
        lines = body.splitlines()
        if head == "The big picture":
            mod["big"] = blocks(lines)
        elif head == "Learning objectives":
            mod["objectives"] = [inline(re.sub(r"^\d+\. ", "", l).strip()) for l in lines if re.match(r"^\d+\. ", l)]
        elif head.startswith("Field case"):
            ctitle = head.split(":", 1)[1].strip() if ":" in head else "A day in the unit"
            text = "\n".join(lines)
            if "**Case review.**" in text:
                pre, _, post = text.partition("**Case review.**")
                qs = []
                if "**Before reading on, decide:**" in pre:
                    pre, _, qblock = pre.partition("**Before reading on, decide:**")
                    qs = [inline(re.sub(r"^\s*- ", "", l).strip()) for l in qblock.splitlines() if l.strip().startswith("- ")]
                pre = pre.replace("**Situation.** ", "", 1)
                mod["case"] = {"title": inline(ctitle[:1].upper() + ctitle[1:]).rstrip("."),
                               "html": blocks(pre.strip().splitlines()),
                               "questions": qs or ["What must you protect first, and whose decision is it?",
                                                   "Which facts would you confirm before you act?", "What would you record, and where?"]}
                post = post.strip()
                mod["debrief"] = [("" if "{{fig:uom%sc}}" % mid in raw else FIG_C % mid + "\n") + blocks(post.splitlines())]
                continue
            sit = re.search(r"\*\*Situation\.\*\* (.+?)(?=\n\n)", text, re.S)
            situation = sit.group(1).strip() if sit else ""
            rest = text.replace(sit.group(0), "") if sit else text
            mod["case"] = {"title": inline(ctitle[:1].upper() + ctitle[1:]).rstrip("."),
                           "html": f"<p>{inline(situation)}</p>",
                           "questions": ["What must you protect first, and whose decision is it?",
                                         "Which facts would you confirm before you act?",
                                         "What would you record, and where?"]}
            mod["debrief"] = [FIG_C % mid + "\n" + blocks(rest.strip().splitlines())]
        elif head == "Supervised practice":
            items = [re.sub(r"^- \[ \] ", "", l).strip() for l in lines if l.startswith("- [ ]")]
            mod["skills"] = {"title": "Supervised practice", "intro": "Complete these with your preceptor at your own unit, using fictional or de-identified data.",
                             "items": [(inline(x), bool(CRIT_WORDS.search(x))) for x in items], "placement": ""}
        elif head == "Question bank":
            for q in re.split(r"\n(?=\*\*Q\d+\.\*\*)", "\n".join(lines).strip()):
                if not q.startswith("**Q"):
                    continue
                stem = re.match(r"\*\*Q\d+\.\*\* (.+)", q).group(1).strip()
                opts = re.findall(r"^- \[( |x)\] (.+)$", q, re.M)
                why_q = re.search(r"^> (.+)$", q, re.M).group(1).strip()
                ans = [k for k, (mk, _) in enumerate(opts) if mk == "x"][0]
                mod["quiz"].append((inline(stem), [inline(t) for _, t in opts], ans, inline(why_q)))
        elif head == "Sources":
            continue
        else:
            hhtml = blocks(lines)
            nav = re.split(r"[:(]", head)[0].strip()
            nav = nav if len(nav) <= 28 else re.sub(r"[ ,]+(and|of|the|for|to|a)?$", "", nav[:28].rsplit(" ", 1)[0]).rstrip(",")
            mod["sections"].append([slugify(head), nav, inline(head), hhtml])
    if "case" not in mod:                       # Module 19: the capstone scenario is the case
        k = next(k for k, x in enumerate(mod["sections"]) if x[2].startswith("Sample scenario"))
        raw_sec = re.search(r"^## Sample scenario.*?\n(.*?)(?=^## )", raw, re.S | re.M).group(1)
        before, _, after = raw_sec.partition("**What a strong response includes**")
        mod["case"] = {"title": inline(mod["sections"][k][2].split(":", 1)[1].strip().strip('"&quot;')),
                       "html": blocks(before.strip().splitlines()),
                       "questions": ["Which inject threatens a patient first?", "Who owns each decision?", "Which calculator answers which question?"]}
        mod["debrief"] = ["<p><strong>What a strong response includes</strong></p>\n" + blocks(after.strip().splitlines())]
        mod["sections"][k][3] = ""
        mod["sections"] = [x for x in mod["sections"] if x[3]]
        port = next(x for x in mod["sections"] if x[2].startswith("The readiness and improvement portfolio"))
        port[3] = after_first_para(port[3], FIG_C % mid)
        B_SECTION["19"] = "How the capstone works"
    if "skills" not in mod:                     # Module 19: the portfolio and the safety gates are the checklist
        rows = re.findall(r"^\| (?!Artifact|---)([^|]+?) \| (\d\d(?: or \d\d)?) \|", raw, re.M)
        crit = {"01", "06", "07", "12"}
        items = [(f"{inline(a)} (Module {n})", n in crit) for a, n in rows]
        items += [("No missed safety hold during the simulation", True),
                  ("No clinical decision made outside the manager&rsquo;s authority", True),
                  ("No clearance or release step bypassed", True),
                  ("No patient data disclosed outside the need-to-know rule", True)]
        mod["skills"] = {"title": "Capstone portfolio and safety gates",
                         "intro": "Assemble each artifact with fictional or de-identified data, then defend it. A zero on any safety gate stops the capstone.",
                         "items": items, "placement": ""}
    # Figures: A after the first paragraph of the first lesson section; B in the "Monday" section (else the last section).
    allhtml = str(mod["sections"]) + str(mod.get("big", "")) + str(mod["debrief"])
    s0 = mod["sections"][0]
    if (FIG_A % mid) not in allhtml:
        s0[3] = after_first_para(s0[3], FIG_A % mid)
    want = B_SECTION.get(mid, "doing it on monday").lower()
    bi = next((k for k, s in enumerate(mod["sections"]) if s[2].lower().startswith(want)), len(mod["sections"]) - 1)
    if (FIG_B % mid) not in allhtml:
        mod["sections"][bi][3] += "\n" + FIG_B % mid
    mod["sections"] = [tuple(s) for s in mod["sections"]]
    nocite = lambda t: re.sub(r"\[\[[a-z0-9_\]\[]+\]\]", "", t)   # quiz, checklist and objectives render without reference links
    mod["quiz"] = [(nocite(a), [nocite(o) for o in b], c, nocite(d)) for a, b, c, d in mod["quiz"]]
    mod["skills"]["items"] = [(nocite(t), k) for t, k in mod["skills"]["items"]]
    mod["objectives"] = [nocite(o) for o in mod["objectives"]]
    mod["image_alt"] = title
    return mid, title, mod


EXTRA_ABBR = {"POD": "physician on duty", "QAPI": "quality assessment and performance improvement",
              "PRDR": "Philippine Renal Disease Registry", "NHSN": "National Healthcare Safety Network", "PM": "preventive maintenance",
              "CAPA": "corrective and preventive action", "CFU": "colony-forming units", "EU": "endotoxin units",
              "LTO": "license to operate", "PDD": "Philippine Health Insurance Corporation (PhilHealth) Dialysis Database", "SSS": "Social Security System",
              "HDMF": "Home Development Mutual Fund", "MSC": "monthly salary credit", "BSI": "bloodstream infection",
              "RO": "reverse osmosis", "ICU": "intensive care unit", "ER": "emergency room", "FTE": "full-time equivalent",
              "PPE": "personal protective equipment", "SOA": "statement of account", "RA": "Republic Act", "NPC": "National Privacy Commission",
              "ISO": "International Organization for Standardization", "CDC": "Centers for Disease Control and Prevention",
              "KDOQI": "Kidney Disease Outcomes Quality Initiative", "IRR": "incidence rate ratio", "DOPPS": "Dialysis Outcomes and Practice Patterns Study"}


def abbr_table():
    import sys
    root = HERE.parents[2]
    sys.path.insert(0, str(root))
    import generate_nursing_course as N
    t = {k: v[0] for k, v in N.ABBR.items()}
    t.update(EXTRA_ABBR)
    return t


def expand_first_use(mod, table):
    """Expand each acronym at its first use in page order (objectives, big picture, case, lessons, debrief,
    checklist, quiz). Headings and table headers are skipped, as the audit does."""
    slots = []                                     # (getter, setter) in render order
    def add(get, put):
        slots.append((get, put))
    for i in range(len(mod["objectives"])):
        add(lambda i=i: mod["objectives"][i], lambda v, i=i: mod["objectives"].__setitem__(i, v))
    add(lambda: mod["big"], lambda v: mod.__setitem__("big", v))
    add(lambda: mod["case"]["html"], lambda v: mod["case"].__setitem__("html", v))
    for i in range(len(mod["sections"])):
        add(lambda i=i: mod["sections"][i][3], lambda v, i=i: mod["sections"][i].__setitem__(3, v))
    for i in range(len(mod["debrief"])):
        add(lambda i=i: mod["debrief"][i], lambda v, i=i: mod["debrief"].__setitem__(i, v))
    for i in range(len(mod["skills"]["items"])):
        add(lambda i=i: mod["skills"]["items"][i][0],
            lambda v, i=i: mod["skills"]["items"].__setitem__(i, (v, mod["skills"]["items"][i][1])))
    for i in range(len(mod["quiz"])):
        def g(i=i):
            return mod["quiz"][i][0]
        def p(v, i=i):
            q = list(mod["quiz"][i]); q[0] = v; mod["quiz"][i] = q
        add(g, p)
        for j in range(4):
            def g2(i=i, j=j):
                return mod["quiz"][i][1][j]
            def p2(v, i=i, j=j):
                q = list(mod["quiz"][i]); o = list(q[1]); o[j] = v; q[1] = o; mod["quiz"][i] = q
            add(g2, p2)
        def g3(i=i):
            return mod["quiz"][i][3]
        def p3(v, i=i):
            q = list(mod["quiz"][i]); q[3] = v; mod["quiz"][i] = q
        add(g3, p3)
    skip_open = re.compile(r"<(h[1-4]|a)\b", re.I)
    skip_close = re.compile(r"</(h[1-4]|a)>", re.I)
    for tok, full in table.items():
        pat = re.compile(r"(?<![A-Za-z0-9\-/])" + re.escape(tok) + r"(s?)(?![A-Za-z0-9])")
        for get, put in slots:
            h = get()
            parts, depth, hit = re.split(r"(<[^>]+>)", h), 0, None
            for k, seg in enumerate(parts):
                if seg.startswith("<"):
                    depth += 1 if skip_open.match(seg) else (-1 if skip_close.match(seg) and depth else 0)
                    continue
                if depth:
                    continue
                for m in pat.finditer(seg):
                    nxt, prev = seg[m.end():m.end() + 3], seg[max(0, m.start() - 6):m.start()]
                    if re.match(r"-\d", nxt) or re.search(r"\d:?\d*\s?$", prev) and tok in ("PM", "AM"):
                        continue                       # asset IDs (HD-07) and clock times (6:00 PM)
                    if tok == "PD" and re.match(r" \d", nxt):
                        continue                       # Presidential Decree numbers (PD 851)
                    if re.search(r"(Guidelines|2024) $", prev) or nxt.startswith(" Gu"):
                        continue                       # titles such as "PSN 2024 HD Guidelines"
                    hit = (k, m)
                    break
                if hit:
                    break
            if not hit:
                continue
            k, m = hit
            seg = parts[k]
            after, before = seg[m.end():m.end() + 2], seg[max(0, m.start() - 1):m.start()]
            closed = before == "(" and seg[m.end():m.end() + 1] == ")"
            if not (after.startswith(" (") or after.startswith("(") or closed):
                pl = m.group(1)
                parts[k] = seg[:m.start()] + f"{full}{pl} ({tok}{pl})" + seg[m.end():]
                put("".join(parts))
            break


def emit(mid, title, mod):
    from pprint import pformat
    body = pformat(mod, width=130, sort_dicts=False)
    return (f'# -*- coding: utf-8 -*-\n"""Dialysis Unit Operations Manager / Unit Manager in Hospital, Module {mid}: {title}.\n'
            f'Generated by packet_to_package.py from src/{mid}-*.md. Edit the Markdown, then re-run the converter."""\n\n'
            f"MODULE = {body}\n")


def main():
    global TABLE
    TABLE = abbr_table()
    titles = {}
    for p in sorted(SRC.glob("[0-1][0-9]-*.md")):
        mid, title, mod = parse(p)
        # spread answer keys evenly (same rule as the other tracks' quizutil.balance)
        out = []
        for i, (stem, opts, ans, why) in enumerate(mod["quiz"]):
            opts = list(opts)
            target = (i * 3 + 1) % 4
            if target != ans:
                opts[target], opts[ans] = opts[ans], opts[target]
            out.append((stem, opts, target, why))
        mod["quiz"] = out
        mod["sections"] = [list(x) for x in mod["sections"]]
        expand_first_use(mod, TABLE)
        # the trainer page lists every checklist on one page, so each module's checklist also expands on its own
        sk = {"objectives": [], "big": "", "case": {"html": ""}, "sections": [], "debrief": [], "skills": mod["skills"], "quiz": []}
        expand_first_use(sk, TABLE)
        mod["sections"] = [tuple(x) for x in mod["sections"]]
        mod["quiz"] = [tuple(q) for q in mod["quiz"]]
        (HERE / f"m{mid}.py").write_text(emit(mid, title, mod), encoding="utf-8")
        titles[mid] = title
    print(f"wrote {len(titles)} modules")


if __name__ == "__main__":
    main()
