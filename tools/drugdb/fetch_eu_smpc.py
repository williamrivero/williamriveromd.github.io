#!/usr/bin/env python3
"""Fetch the EU Summary of Product Characteristics (EMA EPAR product information) for every drug-database
generic that has no US FDA label, plus link-only prescribing-information links from national regulators.

Input   data/drugs/labels/_missing.json   generics with no US FDA label (written by fetch_fda_labels.py)
        data/drugs/generics.json          {slug: {name, ingredients[], ...}}
        data/drugs/aliases.json           variant spellings (skipped; the main slug is fetched instead)
        data/drugs/registry/*.json        PH registrations (dosage forms, to prefer the PH route)
Output  data/drugs/labels-eu/<slug>.json  verbatim SmPC sections 4.1-4.6, 4.8, 4.9, 5.1, 5.2 + renal excerpts
        data/drugs/labels-eu/_missing.json  generics with no EMA product (or a failed fetch/parse)
        data/drugs/labels-eu/_changes.json  added / changed / removed since the last full run (weekly review)
        data/drugs/labels-intl/<slug>.json  "links" only: national prescribing information, metadata + URL,
                                            never text (other fields in these files are left untouched)

EMA sources (the official medicines data download, refreshed twice a day by EMA):
  medicine pages JSON  https://www.ema.europa.eu/en/documents/report/medicines-output-medicines_json-report_en.json
  EPAR documents JSON  https://www.ema.europa.eu/en/documents/report/documents-output-epar_documents_json-report_en.json
  product information  the "EPAR - Product Information" PDF (English) of the chosen medicine

Matching mirrors fetch_fda_labels.py: an EMA medicine matches a generic when every active substance is one of
the generic's ingredients and every ingredient is present (salts, hydrates and esters ignored; INN and US names
both accepted through INN_TO_USAN; combinations matched ingredient-for-ingredient). Only authorised human
medicines count.

Ranking: the originator (not a generic, hybrid or biosimilar; earliest Commission decision) first, then the
SmPC whose pharmaceutical form matches the PH registrations' route (and form class). A product-information PDF
that holds several SmPCs (tablets + oral solution) is split, and the SmPC matching the PH route is used.

Licensing (data/drugs/SOURCES.md): EMA content "may be reproduced ... provided that EMA is always acknowledged as
the source", so SmPC text is stored verbatim with that acknowledgment. National sources whose terms do not clearly
permit reproduction (MHRA, HPRA, Medsafe data sheets, Health Canada product monographs) are stored as metadata and
a deep link only.

Incremental: a slug whose candidate set and product-information dates are unchanged is not refetched. Partial runs
(--only) merge into _missing.json / _changes.json instead of replacing them.

Standard library only; needs pdftotext (poppler-utils) on PATH.
"""
from __future__ import annotations

import argparse
import csv
import datetime as dt
import hashlib
import html as htmlmod
import io
import json
import re
import subprocess
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from fetch_fda_labels import (SALT_WORDS, PH_FORM_GROUPS, expand_ingredients, ing_tokens,  # noqa: E402
                              load_ph_profile, ph_form_class, tokens, write_if_changed)

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / "data" / "drugs"
OUT = DATA / "labels-eu"
INTL = DATA / "labels-intl"
UA = "Mozilla/5.0 (compatible; RenalCareMattersDrugDB/1.0; +https://renalcarematters.com)"
MANILA = dt.timezone(dt.timedelta(hours=8))
SCHEMA_VERSION = 1
EXTRACT_REV = 1   # bump when extraction changes; older files are rewritten once

EMA_MEDICINES = "https://www.ema.europa.eu/en/documents/report/medicines-output-medicines_json-report_en.json"
EMA_DOCUMENTS = "https://www.ema.europa.eu/en/documents/report/documents-output-epar_documents_json-report_en.json"
EMA_PI_PATTERN = "https://www.ema.europa.eu/en/documents/product-information/{slug}-epar-product-information_en.pdf"
EMA_LICENSE = ("© European Medicines Agency. EMA content \"may be reproduced and/or distributed, totally or in part\" "
               "provided EMA is acknowledged as the source (EMA legal notice, "
               "https://www.ema.europa.eu/en/about-us/legal-notice).")

DPD_ZIP = "https://www.canada.ca/content/dam/hc-sc/documents/services/drug-product-database/allfiles.zip"
DPD_INFO = "https://health-products.canada.ca/dpd-bdpp/info?lang=eng&code={code}"

# SmPC sections kept, in display order (number, our key)
SECTIONS = [("4.1", "indications"), ("4.2", "posology"), ("4.3", "contraindications"), ("4.4", "warnings"),
            ("4.5", "interactions"), ("4.6", "pregnancy_lactation"), ("4.8", "undesirable_effects"),
            ("4.9", "overdose"), ("5.1", "pharmacodynamics"), ("5.2", "pharmacokinetics")]
KEEP = {n for n, _ in SECTIONS}
# QRD human product-information template headings (used when a long heading wraps onto a second line in the PDF)
QRD_TITLES = {"4.1": "Therapeutic indications", "4.2": "Posology and method of administration",
              "4.3": "Contraindications", "4.4": "Special warnings and precautions for use",
              "4.5": "Interaction with other medicinal products and other forms of interaction",
              "4.6": "Fertility, pregnancy and lactation", "4.7": "Effects on ability to drive and use machines",
              "4.8": "Undesirable effects", "4.9": "Overdose", "5.1": "Pharmacodynamic properties",
              "5.2": "Pharmacokinetic properties"}

RENAL_RX = re.compile(r"\brenal\b|\bkidney|dialys|haemofiltration|hemofiltration|creatinine clearance|\bCrCl\b|\bGFR\b|"
                      r"\beGFR\b|nephr", re.I)
SUBTAGS = [("hemodialysis", re.compile(r"dialys|haemofiltration|hemofiltration|\bCRRT\b", re.I)),
           ("renal", re.compile(r"\brenal\b|\bkidney|creatinine clearance|\bGFR\b", re.I)),
           ("hepatic", re.compile(r"hepatic|liver", re.I)),
           ("pediatric", re.compile(r"paediatric|pediatric|children|adolescent|infant|neonat", re.I)),
           ("elderly", re.compile(r"elderly|older|geriatric", re.I))]


# --------------------------------------------------------------------------- http
def http_get(url: str, retries: int = 4, timeout: int = 180) -> bytes:
    delay = 3.0
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "*/*"})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code in (404, 410):
                return b""
            if e.code in (403, 429, 500, 502, 503, 504) and attempt < retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            raise
        except (urllib.error.URLError, TimeoutError, ConnectionError):
            if attempt < retries - 1:
                time.sleep(delay)
                delay *= 2
                continue
            raise
    return b""


def records_of(doc) -> list[dict]:
    """The list of records in an EMA JSON report, whatever the wrapper ({data: [...]}, {meta, data}, [...])."""
    if isinstance(doc, list):
        return [x for x in doc if isinstance(x, dict)]
    if isinstance(doc, dict):
        best = []
        for v in doc.values():
            if isinstance(v, list) and len(v) > len(best) and v and isinstance(v[0], dict):
                best = v
        return best
    return []


def norm_keys(rec: dict) -> dict:
    return {re.sub(r"[^a-z0-9]+", "_", str(k).lower()).strip("_"): v for k, v in rec.items()}


def val(rec: dict, *keys) -> str:
    for k in keys:
        v = rec.get(k)
        if isinstance(v, list):
            v = "; ".join(str(x) for x in v if x not in (None, ""))
        if v not in (None, ""):
            return re.sub(r"\s+", " ", str(v)).strip()
    return ""


def pick(rec: dict, pattern: str) -> str:
    """First non-empty value whose key matches a regex (EMA renames columns from time to time)."""
    rx = re.compile(pattern)
    for k, v in rec.items():
        if rx.search(k) and v not in (None, "", []):
            return val(rec, k)
    return ""


def is_yes(v) -> bool:
    return str(v).strip().lower() in ("yes", "true", "1", "y")


def parse_date(s: str) -> str:
    """'25/03/2019', '2019-03-25', '2019-03-25T10:00:00Z' -> '2019-03-25' ('' if unknown)."""
    s = (s or "").strip()
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return m.group(0)
    m = re.match(r"(\d{1,2})/(\d{1,2})/(\d{4})", s)
    if m:
        return f"{m.group(3)}-{int(m.group(2)):02d}-{int(m.group(1)):02d}"
    return ""


# --------------------------------------------------------------------------- matching
def sub_tokens(s: str) -> tuple:
    return ing_tokens(re.sub(r"\([^)]*\)", " ", s))


def eu_substance_matches(ingredient: str, substance: str) -> bool:
    """Ingredient words all in the substance, and any extra substance word a salt/hydrate word. The substance is
    tried without its parenthetical ("amlodipine (as besilate)") and with it ("vaccine (recombinant, adjuvanted)")."""
    it = ing_tokens(ingredient)
    if not it:
        return False
    iset = set(it)
    for st in (sub_tokens(substance), ing_tokens(substance)):
        sset = set(st)
        if sset and iset <= sset and (sset - iset) <= SALT_WORDS:
            return True
    return False


def split_substances(s: str) -> list[str]:
    parts = re.split(r"\s*/\s*|\s*;\s*|,\s*(?![^()]*\))|\s+\+\s+|\s+and\s+(?![^()]*\))", s or "", flags=re.I)
    return [p.strip() for p in parts if p and p.strip() and not re.fullmatch(r"\(?\s*\)?", p)]


def matches(ingredients: list[str], substances: list[str]) -> bool:
    if not substances or not ingredients:
        return False
    ings = expand_ingredients(tuple(ingredients))
    return (all(any(eu_substance_matches(i, s) for i in ings) for s in substances)
            and all(any(eu_substance_matches(i, s) for s in substances) for i in ings))


class Medicine:
    def __init__(self, rec: dict):
        r = norm_keys(rec)
        self.raw = r
        self.name = val(r, "name_of_medicine", "medicine_name", "name")
        self.number = val(r, "ema_product_number", "product_number")
        self.url = val(r, "medicine_url", "url")
        self.status = val(r, "medicine_status", "authorisation_status", "status")
        self.category = val(r, "category")
        self.inn = val(r, "international_non_proprietary_name_common_name", "inn_common_name", "inn")
        self.substance = val(r, "active_substance")
        self.mah = (val(r, "marketing_authorisation_developer_applicant_holder", "marketing_authorisation_holder",
                        "marketing_authorisation_holder_company_name") or pick(r, r"holder"))
        self.generic = is_yes(pick(r, r"^generic")) or "generic" in val(r, "generic_or_hybrid").lower()
        self.biosimilar = is_yes(pick(r, r"biosimilar"))
        self.hybrid = is_yes(pick(r, r"hybrid"))
        self.decision = parse_date(val(r, "european_commission_decision_date", "marketing_authorisation_date",
                                       "date_of_issue_of_marketing_authorisation_valid_throughout_the_european_union"))
        self.updated = parse_date(val(r, "last_updated_date", "revision_date"))
        self.revision = val(r, "revision_number")
        self.pi_url = ""
        self.pi_updated = ""

    @property
    def human_authorised(self) -> bool:
        return (self.category.lower() in ("human", "") and self.status.lower().startswith("authori"))

    @property
    def originator(self) -> bool:
        return not (self.generic or self.biosimilar or self.hybrid)

    def substance_sets(self) -> list[list[str]]:
        out = []
        for s in (self.inn, self.substance):
            parts = split_substances(s)
            if parts and parts not in out:
                out.append(parts)
        return out

    def matches(self, ingredients) -> bool:
        return any(matches(ingredients, subs) for subs in self.substance_sets())

    @property
    def url_slug(self) -> str:
        return urllib.parse.urlparse(self.url).path.rstrip("/").rsplit("/", 1)[-1] if self.url else ""

    @property
    def epar_url(self) -> str:
        return self.url or (f"https://www.ema.europa.eu/en/medicines/human/EPAR/{self.url_slug}" if self.url_slug else "")

    def pi(self) -> str:
        if self.pi_url:
            return self.pi_url
        return EMA_PI_PATTERN.format(slug=self.url_slug) if self.url_slug else ""


def load_ema(cache: Path) -> tuple[list[Medicine], dict]:
    meds_raw = json.loads(fetch_cached(EMA_MEDICINES, cache / "ema-medicines.json"))
    meds = [Medicine(r) for r in records_of(meds_raw)]
    docs: dict[str, tuple[str, str]] = {}
    try:
        docs_raw = json.loads(fetch_cached(EMA_DOCUMENTS, cache / "ema-epar-documents.json"))
        for d in records_of(docs_raw):
            d = norm_keys(d)
            name, typ, url = val(d, "name", "title"), val(d, "type", "document_type"), val(d, "document_url", "url")
            if not url or not re.search(r"product[\s_-]*information", f"{name} {typ} {url}", re.I):
                continue
            if not re.search(r"_en\.pdf$|-en\.pdf$", url, re.I) or re.search(r"tracked|annotated|\bold\b", url, re.I):
                continue
            key = val(d, "ema_product_number") or val(d, "medicine_name").lower()
            prev = docs.get(key)
            upd = parse_date(val(d, "last_updated_date", "first_published_date"))
            if not prev or upd > prev[1]:
                docs[key] = (url, upd)
    except Exception as e:   # the medicine pages alone still give a usable URL pattern
        print(f"  ! EPAR documents JSON unavailable ({e}); using the product-information URL pattern", file=sys.stderr)
    for m in meds:
        hit = docs.get(m.number) or docs.get(m.name.lower())
        if hit:
            m.pi_url, m.pi_updated = hit
    return meds, docs


def fetch_cached(url: str, path: Path) -> bytes:
    if path.exists() and time.time() - path.stat().st_mtime < 6 * 3600:
        return path.read_bytes()
    data = http_get(url)
    if not data:
        raise RuntimeError(f"empty response from {url}")
    path.write_bytes(data)
    return data


# --------------------------------------------------------------------------- PDF -> SmPC sections
def pdf_text(pdf: bytes) -> str:
    with tempfile.NamedTemporaryFile(suffix=".pdf") as f:
        f.write(pdf)
        f.flush()
        r = subprocess.run(["pdftotext", "-layout", "-enc", "UTF-8", f.name, "-"], capture_output=True, timeout=180)
    return r.stdout.decode("utf-8", "replace")


HEAD_SUB = re.compile(r"^[ \t]{0,8}(\d{1,2})\.(\d{1,2})\.?[ \t]+(\S.{1,110}?)[ \t]*$", re.M)
HEAD_TOP = re.compile(r"^[ \t]{0,8}(\d{1,2})\.?[ \t]+([A-Z][A-Z0-9 ,'’()/&\-]{3,90}?)[ \t]*$", re.M)


def split_smpcs(text: str) -> list[str]:
    """Annex I of an EMA product-information PDF, split into its SmPCs (one per pharmaceutical form group)."""
    text = text.replace("\f", "\n")
    start = re.search(r"SUMMARY\s+OF\s+PRODUCT\s+CHARACTERISTICS", text)
    if start:
        text = text[start.start():]
    end = re.search(r"^\s*ANNEX\s+II\s*$", text, re.M)
    if end:
        text = text[:end.start()]
    starts = [m.start() for m in re.finditer(r"^[ \t]*1\.?[ \t]+NAME OF THE MEDICINAL PRODUCT[ \t]*$", text, re.M)]
    if not starts:
        return [text] if text.strip() else []
    return [text[a:b] for a, b in zip(starts, starts[1:] + [len(text)])]


def smpc_sections(smpc: str) -> dict[str, tuple[str, str]]:
    """{'4.2': (title as published, raw layout text)} for every numbered section, in document order."""
    heads = []
    for m in HEAD_SUB.finditer(smpc):
        title = m.group(3).strip()
        if not re.match(r"[A-Z]", title) or re.search(r"\s{3,}", title):
            continue
        heads.append(((int(m.group(1)), int(m.group(2))), title, m.start(), m.end()))
    for m in HEAD_TOP.finditer(smpc):
        if len(m.group(2).split()) >= 1 and m.group(2).upper() == m.group(2):
            heads.append(((int(m.group(1)), 0), m.group(2).strip(), m.start(), m.end()))
    heads.sort(key=lambda h: h[2])
    kept, last = [], (0, -1)
    for h in heads:   # headings must advance (4.1 < 4.2 < ... < 5 < 5.1); stray "4.5 mg" lines never do in order
        if h[0] > last and h[0][0] <= 12 and (h[0][0] - last[0]) <= 1:
            kept.append(h)
            last = h[0]
    out = {}
    for i, (key, title, s, e) in enumerate(kept):
        end = kept[i + 1][2] if i + 1 < len(kept) else len(smpc)
        num = f"{key[0]}.{key[1]}" if key[1] else str(key[0])
        body = smpc[e:end]
        full = QRD_TITLES.get(num)
        if full and title != full and full.lower().startswith(title.lower()):
            # wrapped heading: drop the continuation line ("products and other forms of interaction")
            rest = full[len(title):].strip().lower()
            m = re.match(r"\s*\n[ \t]*(\S[^\n]*)", body)
            if m and rest and rest.startswith(m.group(1).strip().lower()[:12]):
                body = body[m.end():]
            title = full
        out[num] = (title, body)
    return out


def _is_table_line(line: str) -> bool:
    return bool(re.search(r"\S[ \t]{3,}\S", line.strip()))


BULLET = re.compile(r"^\s*(?:[•▪●◦‣∙·\-–—*]|o(?=\s)|\(?[a-z]\)|\d{1,2}\))\s+")


def blocks_of(raw: str) -> list[dict]:
    """Layout text -> [{'h': heading} | {'p': paragraph} | {'li': [items]} | {'pre': table text}], verbatim words."""
    lines = [ln.rstrip() for ln in raw.split("\n")]
    lines = [ln for ln in lines if not re.fullmatch(r"\s*\d{1,3}\s*", ln)]          # page numbers
    paras, cur = [], []
    for ln in lines:
        if ln.strip():
            cur.append(ln)
        elif cur:
            paras.append(cur)
            cur = []
    if cur:
        paras.append(cur)
    width = max((len(ln.strip()) for p in paras for ln in p), default=80)
    # tables: a paragraph with table-like column gaps, plus short rows sandwiched between such paragraphs
    tab = [sum(1 for ln in p if _is_table_line(ln)) for p in paras]
    is_tab = [t >= 1 and t >= 0.4 * len(p) for t, p in zip(tab, paras)]
    for i in range(1, len(paras) - 1):
        if not is_tab[i] and len(paras[i]) <= 3 and is_tab[i - 1] and any(is_tab[i + 1:i + 3]):
            is_tab[i] = True
    out: list[dict] = []
    run: list[list[str]] = []

    def flush_run():
        if not run:
            return
        if sum(len(p) for p in run) >= 2 and sum(1 for p in run for ln in p if _is_table_line(ln)) >= 2:
            ind = min(len(ln) - len(ln.lstrip()) for p in run for ln in p)
            out.append({"pre": "\n\n".join("\n".join(ln[ind:] for ln in p) for p in run)})
        else:
            for p in run:
                out.append({"p": join_lines([ln.strip() for ln in p])})
        run.clear()
    for k, p in enumerate(paras):
        if is_tab[k]:
            run.append(p)
            continue
        flush_run()
        first = p[0].strip()
        if (len(p) == 1 and len(first) <= 90 and not re.search(r"[.;:,]$", first) and re.match(r"[A-Z(]", first)
                and len(first.split()) <= 12 and not BULLET.match(p[0])):
            out.append({"h": first})
            continue
        if (len(p) > 1 and len(first) <= 95 and len(first) < 0.75 * width and not re.search(r"[.;:,]$", first)
                and re.match(r"[A-Z]", first) and len(first.split()) <= 14 and not BULLET.match(p[0])
                and re.match(r"[A-Z(]", p[1].strip())):
            out.append({"h": first})
            p = p[1:]
        items, buf = [], []
        for ln in p:
            s = ln.strip()
            if BULLET.match(ln) and buf:
                items.append(buf)
                buf = [s]
            else:
                buf.append(s)
        if buf:
            items.append(buf)
        texts = [join_lines(b) for b in items]
        if len(texts) > 1 or (texts and BULLET.match(p[0])):
            lead = [] if BULLET.match(p[0]) else [texts.pop(0)]
            if lead:
                out.append({"p": lead[0]})
            out.append({"li": [BULLET.sub("", t, count=1) for t in texts]})
        elif texts and texts[0]:
            out.append({"p": texts[0]})
    flush_run()
    return out


def join_lines(lines: list[str]) -> str:
    s = ""
    for ln in lines:
        if not s:
            s = ln
        elif s.endswith("-") and not s.endswith(" -"):
            s += ln
        else:
            s += " " + ln
    return re.sub(r"[ \t]+", " ", s).strip()


def block_text(b: dict) -> str:
    return b.get("h") or b.get("p") or b.get("pre") or " ".join(b.get("li") or [])


def subsections(blocks: list[dict]) -> list[dict]:
    """Heading-delimited parts of a section ({'heading', 'tags', 'blocks'}), for the population subsections."""
    out, cur = [], None
    for b in blocks:
        if "h" in b:
            cur = {"heading": b["h"], "blocks": []}
            out.append(cur)
        elif cur is not None:
            cur["blocks"].append(b)
        else:
            # an inline lead-in ("Renal impairment: ...") counts as its own subsection
            t = block_text(b)
            m = re.match(r"((?:Patients with |Use in )?[A-Z][\w ()/-]{3,50}?)\s*[:.]\s+\S", t)
            if m and any(rx.search(m.group(1)) for _, rx in SUBTAGS):
                out.append({"heading": m.group(1), "blocks": [b]})
    for s in out:
        s["tags"] = [tag for tag, rx in SUBTAGS if rx.search(s["heading"])]
    return [s for s in out if s["blocks"]]


def inline_subs(blocks: list[dict]) -> list[dict]:
    """Paragraphs that start with a population lead-in inside a section with no separate headings."""
    out = []
    for b in blocks:
        t = block_text(b)
        m = re.match(r"((?:Patients with |Use in |In )?[A-Z][\w ()/-]{3,60}?)\s*[:.–-]\s+\S", t)
        if m and any(rx.search(m.group(1)) for _, rx in SUBTAGS):
            out.append({"heading": m.group(1).strip(), "tags": [tag for tag, rx in SUBTAGS if rx.search(m.group(1))],
                        "blocks": [b]})
    return out


def renal_excerpts(sections: dict) -> list[dict]:
    """Verbatim renal-impairment parts of 4.2 and 5.2: the headed subsection, else renal paragraphs."""
    out = []
    for num in ("4.2", "5.2"):
        sec = sections.get(num)
        if not sec:
            continue
        subs = [s for s in subsections(sec["blocks"]) + inline_subs(sec["blocks"])
                if {"renal", "hemodialysis"} & set(s["tags"])]
        seen = set()
        for s in subs:
            key = json.dumps(s["blocks"], ensure_ascii=False)
            if key in seen:
                continue
            seen.add(key)
            out.append({"section": num, "section_title": sec["title"], "heading": s["heading"], "tags": s["tags"],
                        "match": "subsection", "blocks": s["blocks"]})
        if not subs:
            paras = [b for b in sec["blocks"] if "h" not in b and RENAL_RX.search(block_text(b))]
            if paras:
                out.append({"section": num, "section_title": sec["title"], "heading": "", "tags": ["renal"],
                            "match": "keyword", "blocks": paras[:8]})
    return out


def parse_smpc(smpc: str) -> dict:
    secs = smpc_sections(smpc)
    name = " ".join(blocks_of(secs.get("1", ("", ""))[1])[0].values()) if secs.get("1") and blocks_of(secs["1"][1]) else ""
    form = " ".join(block_text(b) for b in blocks_of(secs.get("3", ("", ""))[1])[:3]) if secs.get("3") else ""
    out = {"name": name if isinstance(name, str) else "", "pharmaceutical_form": form[:400], "sections": {}}
    for num, key in SECTIONS:
        if num in secs:
            title, raw = secs[num]
            bl = blocks_of(raw)
            if bl:
                out["sections"][num] = {"key": key, "title": title, "blocks": bl}
    return out


def smpc_route(sm: dict) -> tuple[str | None, str | None]:
    text = f"{sm.get('name', '')} {sm.get('pharmaceutical_form', '')}".lower()
    grp = next((g for g, pat in PH_FORM_GROUPS if re.search(pat, text)), None)
    return grp, ph_form_class(text)


# --------------------------------------------------------------------------- selection
def choose(slug: str, g: dict, cands: list[Medicine], ph_routes: dict, ph_forms: dict, pdf_cache: dict,
           max_pdfs: int, log) -> tuple[Medicine | None, dict | None, dict, list[str]]:
    """Download up to max_pdfs product-information PDFs, best-ranked first, and pick (medicine, smpc)."""
    errors = []
    order = sorted(cands, key=lambda m: (not m.originator, m.decision or "9999", m.name.lower()))
    routes = ph_routes.get(slug) or {}
    forms = ph_forms.get(slug) or {}
    top_route = max(routes, key=routes.get) if routes else None
    best, best_key = None, None
    tried = 0
    for m in order:
        if tried >= max_pdfs:
            break
        url = m.pi()
        if not url:
            continue
        tried += 1
        if url not in pdf_cache:
            try:
                data = http_get(url)
                pdf_cache[url] = [parse_smpc(s) for s in split_smpcs(pdf_text(data))] if data[:4] == b"%PDF" else None
                if pdf_cache[url] is None:
                    errors.append(f"{m.name}: not a PDF ({url})")
                time.sleep(0.5)
            except Exception as e:
                pdf_cache[url] = None
                errors.append(f"{m.name}: {e}")
        for i, sm in enumerate(pdf_cache[url] or []):
            if not sm["sections"]:
                continue
            grp, fc = smpc_route(sm)
            key = (0 if (top_route and grp == top_route) else 1 if (grp and grp in routes) else 2 if not routes else 3,
                   0 if m.originator else 1,
                   0 if (fc and forms.get(fc)) else 1,
                   -len(sm["sections"]), m.decision or "9999", i)
            if best_key is None or key < best_key:
                best, best_key = (m, sm, {"route": grp, "form_class": fc, "smpc_index": i}), key
        if best_key and best_key[0] == 0 and best_key[1] == 0:
            break          # originator in the main PH route: done
    if not best:
        return None, None, {}, errors
    m, sm, info = best
    info.update({"ph_routes": routes, "route_match": best_key[0] <= 1 if routes else None,
                 "originator": m.originator, "candidates": len(cands), "pdfs_checked": tried,
                 "ranked": [f"{c.name} ({'originator' if c.originator else 'generic/hybrid/biosimilar'}"
                            f"{', ' + c.decision if c.decision else ''})" for c in order[:6]]})
    log(f"  {slug}: {m.name} [{info['route']}/{info['form_class']}] of {len(cands)} candidate(s)")
    return m, sm, info, errors


def build_record(slug: str, g: dict, m: Medicine, sm: dict, info: dict, cand_key: str) -> dict:
    secs = sm["sections"]
    rec = {
        "slug": slug, "name": g.get("name", slug), "ingredients": g.get("ingredients", []),
        "schema_version": SCHEMA_VERSION, "extract_rev": EXTRACT_REV,
        "source": {
            "agency": "EMA", "agency_full": "European Medicines Agency",
            "document": "EU Summary of Product Characteristics (Annex I of the EPAR product information)",
            "product": m.name, "smpc_title": sm.get("name", ""), "pharmaceutical_form": sm.get("pharmaceutical_form", ""),
            "mah": m.mah, "ema_product_number": m.number, "active_substance": m.substance, "inn": m.inn,
            "epar_url": m.epar_url, "pi_url": m.pi(), "revision_date": m.pi_updated or m.updated,
            "medicine_page_updated": m.updated, "ec_decision_date": m.decision,
            "license_note": EMA_LICENSE,
        },
        "selection": dict(info, candidates_key=cand_key),
        "sections": {n: {"title": s["title"], "key": s["key"], "blocks": s["blocks"]} for n, s in secs.items()},
        "renal_impairment": renal_excerpts(secs),
        "subsections": {},
    }
    for num in ("4.2", "5.2"):
        if num in secs:
            subs = [{"heading": s["heading"], "tags": s["tags"], "blocks": s["blocks"]}
                    for s in subsections(secs[num]["blocks"]) + inline_subs(secs[num]["blocks"]) if s["tags"]]
            if subs:
                rec["subsections"][num] = subs
    return rec


# --------------------------------------------------------------------------- national links (metadata + URL only)
class DPD:
    """Health Canada Drug Product Database data extract (marketed products)."""

    def __init__(self, cache: Path):
        z = zipfile.ZipFile(io.BytesIO(fetch_cached(DPD_ZIP, cache / "dpd-allfiles.zip")))
        rd = lambda name: list(csv.reader(io.TextIOWrapper(z.open(name), encoding="utf-8", errors="replace")))
        names = {Path(n).name.lower(): n for n in z.namelist()}
        self.drugs, self.ings, self.comp, self.route = {}, {}, {}, {}
        for r in rd(names["drug.txt"]):
            if len(r) > 4 and r[2].strip().lower() == "human":
                self.drugs[r[0]] = {"brand": r[4].strip(), "din": r[3].strip()}
        for r in rd(names["ingred.txt"]):
            if len(r) > 2 and r[0] in self.drugs:
                self.ings.setdefault(r[0], []).append(r[2].strip())
        if "comp.txt" in names:
            for r in rd(names["comp.txt"]):
                if len(r) > 3 and r[0] in self.drugs:
                    self.comp.setdefault(r[0], r[3].strip())
        if "route.txt" in names:
            for r in rd(names["route.txt"]):
                if len(r) > 2 and r[0] in self.drugs:
                    self.route.setdefault(r[0], []).append(r[2].strip().lower())
        self.by_word: dict[str, set] = {}
        for code, ings in self.ings.items():
            for i in ings:
                for w in sub_tokens(i):
                    if w not in SALT_WORDS:
                        self.by_word.setdefault(w, set()).add(code)

    def find(self, ingredients: list[str], routes: dict) -> list[dict]:
        words = {w for i in expand_ingredients(tuple(ingredients)) for w in ing_tokens(i) if w not in SALT_WORDS}
        if not words:
            return []
        codes = set.intersection(*(self.by_word.get(w, set()) for w in words))
        hits = [c for c in codes if matches(ingredients, self.ings[c])]
        top = max(routes, key=routes.get) if routes else None

        def rgrp(c):
            t = " ".join(self.route.get(c, []))
            return next((gname for gname, pat in PH_FORM_GROUPS if re.search(pat, t)), None)
        hits.sort(key=lambda c: (0 if top and rgrp(c) == top else 1, self.drugs[c]["brand"].lower()))
        out, seen = [], set()
        for c in hits:
            b = self.drugs[c]["brand"]
            if b.lower() in seen:
                continue
            seen.add(b.lower())
            out.append({"agency": "Health Canada", "agency_short": "Health Canada DPD",
                        "kind": "Product monograph (Drug Product Database record)",
                        "product": b, "holder": self.comp.get(c, ""), "din": self.drugs[c]["din"],
                        "url": DPD_INFO.format(code=c), "reuse": "link only"})
            if len(out) >= 2:
                break
        return out


def dpd_monograph(link: dict) -> None:
    """Add the product-monograph PDF URL and date from the DPD record page, when the page shows them."""
    try:
        page = http_get(link["url"], retries=2, timeout=60).decode("utf-8", "replace")
    except Exception:
        return
    m = re.search(r'href="(https?://pdf\.hres\.ca/dpd_pm/[^"]+\.(?:PDF|pdf))"', page)
    if m:
        link["monograph_url"] = htmlmod.unescape(m.group(1))
    d = re.search(r"(?:Date of )?[Pp]roduct [Mm]onograph[^<]{0,40}?(?:</[^>]+>\s*)*(?:<[^>]+>\s*)*(\d{4}-\d{2}-\d{2})", page)
    if d:
        link["monograph_date"] = d.group(1)


# --------------------------------------------------------------------------- probe (debug)
def probe(args, targets, generics, cache):
    print("== EMA medicines JSON")
    raw = json.loads(fetch_cached(EMA_MEDICINES, cache / "ema-medicines.json"))
    print("top-level:", type(raw).__name__, list(raw)[:10] if isinstance(raw, dict) else len(raw))
    recs = records_of(raw)
    print("records:", len(recs))
    if recs:
        print(json.dumps(recs[0], ensure_ascii=False, indent=1)[:2500])
        from collections import Counter
        r0 = [norm_keys(r) for r in recs]
        for k in ("category", "medicine_status"):
            print(k, Counter(val(r, k) for r in r0).most_common(8))
        for k in r0[0]:
            if re.search(r"generic|biosimilar|hybrid|status|date", k):
                print("  key", k, Counter(str(r.get(k))[:30] for r in r0).most_common(4))
    print("== EPAR documents JSON")
    try:
        d = json.loads(fetch_cached(EMA_DOCUMENTS, cache / "ema-epar-documents.json"))
        drecs = records_of(d)
        print("records:", len(drecs))
        pis = [x for x in drecs if re.search(r"product[\s_-]*information", json.dumps(x), re.I)]
        print("product-information-like:", len(pis))
        for x in pis[:3]:
            print(json.dumps(x, ensure_ascii=False)[:900])
        from collections import Counter
        print(Counter(val(norm_keys(x), "type") for x in drecs).most_common(15))
    except Exception as e:
        print("EPAR documents failed:", e)
    meds, _ = load_ema(cache)
    ok = [m for m in meds if m.human_authorised]
    print(f"authorised human medicines: {len(ok)} of {len(meds)}; with PI URL from documents: {sum(1 for m in ok if m.pi_url)}")
    hits = 0
    for slug in list(targets)[:400]:
        c = [m for m in ok if m.matches(generics[slug]["ingredients"])]
        if c:
            hits += 1
            if hits <= 25:
                print(f"  match {slug}: " + "; ".join(f"{m.name} ({'orig' if m.originator else 'gen'}, {m.decision})" for m in c[:5]))
    print(f"matched {hits} of first {min(400, len(targets))} targets")
    sample = [s for s in (args.only or []) if s in generics] or []
    for slug in sample[:3]:
        c = [m for m in ok if m.matches(generics[slug]["ingredients"])]
        if not c:
            continue
        url = sorted(c, key=lambda m: (not m.originator, m.decision or "9999"))[0].pi()
        print("== PDF", slug, url)
        data = http_get(url)
        print("bytes", len(data), data[:8])
        t = pdf_text(data)
        sm = split_smpcs(t)
        print("smpcs:", len(sm))
        if sm:
            secs = smpc_sections(sm[0])
            print("sections:", [(k, v[0][:40]) for k, v in secs.items()])
            raw42 = secs.get("4.2", ("", ""))[1]
            print(raw42[:3000])
            p = parse_smpc(sm[0])
            print(json.dumps(p["sections"].get("4.2", {}), ensure_ascii=False, indent=1)[:2500])
            print(json.dumps(renal_excerpts(p["sections"]), ensure_ascii=False, indent=1)[:2000])
            print(json.dumps(p["sections"].get("4.8", {}), ensure_ascii=False, indent=1)[:3000])
            print(f"<<<DUMP {slug}>>>")
            print("\n<<<SMPC>>>\n".join(sm))
            print(f"<<<END {slug}>>>")
    print("== Health Canada DPD")
    try:
        z = zipfile.ZipFile(io.BytesIO(fetch_cached(DPD_ZIP, cache / "dpd-allfiles.zip")))
        print(z.namelist())
        for n in z.namelist():
            if re.search(r"(drug|ingred|comp|route)\.txt$", n, re.I):
                print(n, z.open(n).read(400).decode("utf-8", "replace").splitlines()[:2])
        dpd = DPD(cache)
        print("human marketed products:", len(dpd.drugs))
        for slug in ["betahistine", "alfacalcidol", "ambroxol", "trimetazidine", "domperidone", "bilastine"]:
            if slug not in generics:
                continue
            links = dpd.find(generics[slug]["ingredients"], {})
            print(" ", slug, links[:2])
            if links:
                pg = http_get(links[0]["url"], retries=2).decode("utf-8", "replace")
                i = pg.find("onograph")
                print("   info page", len(pg), re.sub(r"\s+", " ", pg[max(0, i - 600):i + 900]))
                break
    except Exception as e:
        print("DPD failed:", e)
    for label, url in (("HPRA", "https://www.hpra.ie/find-a-medicine/results?query=aceclofenac"),
                       ("Medsafe", "https://www.medsafe.govt.nz/Medicines/infoSearch.asp")):
        try:
            pg = http_get(url, retries=1).decode("utf-8", "replace")
            print("==", label, len(pg), re.findall(r'href="[^"]{0,140}"', pg)[:25])
        except Exception as e:
            print("==", label, "failed:", e)
    return 0


# --------------------------------------------------------------------------- main
def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--generics-file", default=str(DATA / "generics.json"))
    ap.add_argument("--missing-file", default=str(DATA / "labels" / "_missing.json"),
                    help="generics without a US label (targets); '' = every generic without labels/<slug>.json")
    ap.add_argument("--only", nargs="*", help="limit to these slugs")
    ap.add_argument("--force", action="store_true", help="re-download and re-extract every PDF")
    ap.add_argument("--national", action="store_true", help="also refresh link-only national sources")
    ap.add_argument("--max-pdfs", type=int, default=4, help="product-information PDFs to check per generic")
    ap.add_argument("--cache-dir", default=str(Path(tempfile.gettempdir()) / "eu-smpc-cache"))
    ap.add_argument("--probe", action="store_true", help="print the structure of every source and exit")
    args = ap.parse_args()

    cache = Path(args.cache_dir)
    cache.mkdir(parents=True, exist_ok=True)
    generics = json.loads(Path(args.generics_file).read_text(encoding="utf-8"))
    aliases = json.loads((DATA / "aliases.json").read_text(encoding="utf-8")) if (DATA / "aliases.json").exists() else {}
    variant = {k for k, v in aliases.items() if not k.startswith("_") and isinstance(v, dict) and v.get("main")
               and v["main"] != k}
    if args.missing_file:
        miss = json.loads(Path(args.missing_file).read_text(encoding="utf-8"))
        targets = [m["slug"] for m in miss.get("missing", [])]
    else:
        targets = [s for s in generics if not (DATA / "labels" / f"{s}.json").exists()]
    targets = [s for s in dict.fromkeys(targets) if s in generics and generics[s].get("ingredients") and s not in variant
               and not (DATA / "labels" / f"{s}.json").exists()]
    if args.only:
        want = set(args.only)
        targets = [s for s in targets if s in want] + [s for s in args.only if s in generics and s not in targets
                                                        and s not in variant]
    if args.probe:
        return probe(args, targets, generics, cache)

    OUT.mkdir(parents=True, exist_ok=True)
    INTL.mkdir(parents=True, exist_ok=True)
    print(f"{len(targets)} generics without a US label ({len(variant)} alias variants skipped)", flush=True)
    meds, _ = load_ema(cache)
    ok = [m for m in meds if m.human_authorised]
    print(f"EMA: {len(ok)} authorised human medicines ({sum(1 for m in ok if m.pi_url)} with a product-information "
          f"document in the EPAR documents JSON)", flush=True)
    index: dict[str, set] = {}
    for i, m in enumerate(ok):
        for subs in m.substance_sets():
            for s in subs:
                for w in sub_tokens(s):
                    if w not in SALT_WORDS:
                        index.setdefault(w, set()).add(i)
    ph_routes, ph_forms = load_ph_profile(DATA / "registry")
    pdf_cache: dict = {}
    added, changed, removed, missing, unchanged = [], [], [], [], 0
    log = lambda s: print(s, flush=True)
    for n, slug in enumerate(targets, 1):
        g = generics[slug]
        words = {w for i in expand_ingredients(tuple(g["ingredients"])) for w in ing_tokens(i) if w not in SALT_WORDS}
        pool = set.intersection(*(index.get(w, set()) for w in words)) if words else set()
        cands = [ok[i] for i in sorted(pool) if ok[i].matches(g["ingredients"])]
        path = OUT / f"{slug}.json"
        old = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
        if not cands:
            missing.append({"slug": slug, "name": g.get("name", slug), "ingredients": g["ingredients"],
                            "reason": "no centrally authorised EU (EMA) product"})
            if old:
                path.unlink()
                removed.append({"slug": slug, "name": g.get("name", slug),
                                "previous": {"product": old["source"].get("product"),
                                             "revision_date": old["source"].get("revision_date")}})
            continue
        cand_key = hashlib.sha1(json.dumps(sorted((m.number, m.name, m.pi(), m.pi_updated or m.updated)
                                                  for m in cands)).encode()).hexdigest()[:16]
        if (old and not args.force and old.get("extract_rev", 0) >= EXTRACT_REV
                and (old.get("selection") or {}).get("candidates_key") == cand_key):
            unchanged += 1
            continue
        m, sm, info, errors = choose(slug, g, cands, ph_routes, ph_forms, pdf_cache, args.max_pdfs, log)
        if not m:
            missing.append({"slug": slug, "name": g.get("name", slug), "ingredients": g["ingredients"],
                            "reason": "EMA product found but the SmPC could not be fetched or parsed",
                            "candidates": [c.name for c in cands[:5]], "errors": errors[:3]})
            continue           # keep any previous file: a fetch error is not a removal
        rec = build_record(slug, g, m, sm, info, cand_key)
        rec["retrieved"] = dt.datetime.now(MANILA).date().isoformat()
        write_if_changed(path, rec, ignore=("retrieved",))
        entry = {"slug": slug, "name": g.get("name", slug), "product": m.name, "mah": m.mah,
                 "originator": m.originator, "revision_date": rec["source"]["revision_date"],
                 "pi_url": rec["source"]["pi_url"], "sections": sorted(rec["sections"]),
                 "renal_excerpts": len(rec["renal_impairment"])}
        if not old:
            added.append(entry)
        elif (old["source"].get("pi_url"), old["source"].get("revision_date")) != (rec["source"]["pi_url"],
                                                                                  rec["source"]["revision_date"]):
            entry["previous"] = {"product": old["source"].get("product"), "revision_date": old["source"].get("revision_date")}
            changed.append(entry)
        if n % 50 == 0:
            print(f"  … {n}/{len(targets)}", flush=True)

    # US label appeared since: the EU file is no longer used
    for f in sorted(OUT.glob("*.json")):
        if not f.name.startswith("_") and (DATA / "labels" / f.name).exists() and (not args.only or f.stem in args.only):
            f.unlink()
            removed.append({"slug": f.stem, "reason": "now has a US FDA label"})

    if args.national:
        national_links(targets, generics, cache, ph_routes)

    now = dt.datetime.now(MANILA).isoformat(timespec="seconds")
    partial = bool(args.only)
    mpath, cpath = OUT / "_missing.json", OUT / "_changes.json"
    missing_doc = {"generated_at": now, "count": len(missing), "targets": len(targets),
                   "note": "Generics without a US FDA label that also have no usable EMA (EU) SmPC.", "missing": missing}
    changes_doc = {"generated_at": now, "note": "EU SmPCs (EMA) added, changed or removed since the last full run; "
                                                "for Dr. Rivero's weekly review.",
                   "added": added, "changed": changed, "removed": removed}
    if partial:
        ran = set(targets)
        if mpath.exists():
            prev = json.loads(mpath.read_text(encoding="utf-8"))
            merged = sorted([x for x in prev.get("missing", []) if x["slug"] not in ran] + missing, key=lambda x: x["slug"])
            missing_doc = {**prev, "missing": merged, "count": len(merged)}
        if cpath.exists():
            prev = json.loads(cpath.read_text(encoding="utf-8"))
            mine = {e["slug"] for e in added + changed + removed}
            changes_doc = prev if not mine else {**prev, "generated_at": now, **{
                k: sorted([e for e in prev.get(k, []) if e["slug"] not in mine] + new, key=lambda e: e["slug"])
                for k, new in (("added", added), ("changed", changed), ("removed", removed))}}
    write_if_changed(mpath, missing_doc, ignore=("generated_at",))
    write_if_changed(cpath, changes_doc, ignore=("generated_at",))
    have = sum(1 for f in OUT.glob("*.json") if not f.name.startswith("_"))
    print(f"EU SmPC files: {have}; this run added {len(added)}, changed {len(changed)}, removed {len(removed)}, "
          f"unchanged {unchanged}, missing {len(missing)} of {len(targets)}")
    return 0


def national_links(targets, generics, cache, ph_routes):
    """labels-intl/<slug>.json "links": metadata + deep link only (no text), for generics with no EU SmPC."""
    try:
        dpd = DPD(cache)
    except Exception as e:
        print(f"  ! Health Canada DPD unavailable: {e}", file=sys.stderr)
        dpd = None
    today = dt.datetime.now(MANILA).date().isoformat()
    n_links = 0
    for slug in targets:
        if (OUT / f"{slug}.json").exists():
            want = []           # the EU SmPC already gives the text; no link list needed
        else:
            g = generics[slug]
            want = []
            if dpd:
                for link in dpd.find(g["ingredients"], ph_routes.get(slug) or {}):
                    dpd_monograph(link)
                    want.append(link)
                    time.sleep(0.3)
        path = INTL / f"{slug}.json"
        doc = json.loads(path.read_text(encoding="utf-8")) if path.exists() else None
        if not want:
            if doc and "links" in doc:
                doc.pop("links", None)
                doc.pop("links_retrieved", None)
                if set(doc) <= {"slug"}:
                    path.unlink()
                else:
                    path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
            continue
        n_links += 1
        doc = doc or {"slug": slug}
        if doc.get("links") != want:
            doc["links"] = want
            doc["links_retrieved"] = today
            doc["links_note"] = ("Metadata and deep links only. These regulators' terms do not clearly permit "
                                 "reproducing the documents, so no text is stored or shown.")
            path.write_text(json.dumps(doc, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"national links: {n_links} generics with at least one link", flush=True)


if __name__ == "__main__":
    sys.exit(main())
