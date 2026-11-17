#!/usr/bin/env python3
"""Related guides for the Drug Database: which renalcarematters.com guides discuss each drug or supplement.

Scans each content guide's English text (data-lang="en" spans and untranslated text; tl/ceb/kap spans, the header,
nav, footer, references, glossary, share bar, signature block and related-guides block are skipped) for drug names:
  * single-ingredient generics: the generic name, its ingredient, the ingredient without a trailing salt word
    (amlodipine besilate -> amlodipine) and nonproprietary synonyms from tools/drugdb/synonyms.py;
  * combinations: every component must be mentioned (scores add up);
  * brand names of 5+ characters, matched case-sensitively (Renvela, RENVELA), skipped when the word also appears in
    lowercase in the guides (a common word) or when the brand is shared by more than two generics.
Score per (drug, guide): a hit in the guide title +10 (qualifies on its own), each mention in a heading x3, each body
mention x1. A guide qualifies with a title or heading hit, or 3+ body mentions; guides scoring under a quarter of the
drug's best guide are dropped; the top 4 are kept.

Supplements: the same scan for the supplement ingredient and category keys the brand pages use (top three
ingredients of a brand, plus probiotic / omega-3 / ketoanalogue / fiber categories) and for supplement brand names;
generate_supplement_pages.py combines a brand's keys and keeps the top 3.

Manual overrides: tools/drugdb/related_guides_overrides.json
  {"drugs": {"<slug>": {"add": ["guide.html"], "remove": ["guide.html"]}},
   "supplements": {"<brand-slug>": {"add": [...], "remove": [...]}},
   "supplement_keys": {"<key>": {"add": [...], "remove": [...]}}}
"add" puts a guide first (score 100); "remove" drops it.

Output: data/drugs/related_guides.json
  {"guides": {file: {t, d, img, url}}, "drugs": {slug: [[file, score], ...]},
   "supplement_keys": {key: [[file, score], ...]}, "supplement_brands": {slug: [[file, score], ...]}}

  python3 tools/drugdb/build_related_guides.py              # build
  python3 tools/drugdb/build_related_guides.py --show sevelamer dapagliflozin   # print picks with scores
"""
from __future__ import annotations

import argparse
import glob
import html
import json
import os
import re
import sys
import unicodedata
from collections import Counter, defaultdict
from html.parser import HTMLParser
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent
sys.path.insert(0, str(HERE))
sys.path.insert(0, str(REPO))
import synonyms  # noqa: E402
from patch_symptom_widget import eligible  # noqa: E402  (same content-guide eligibility as the widget/share bar)

SITE = "https://renalcarematters.com"
OVERRIDES = HERE / "related_guides_overrides.json"
OUT = REPO / "data" / "drugs" / "related_guides.json"
EXTRA_SKIP = {"kidney-physiology.html", "lab-interpreter-guide.html", "drug-index.html"}

# ── text extraction ──────────────────────────────────────────────────────────
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "param", "source", "track", "wbr"}
SKIP_TAGS = {"script", "style", "nav", "header", "footer", "template", "noscript", "svg", "button", "select", "dialog"}
SKIP_CLASS = re.compile(r"\b(?:ref-acc|ref-section|glossary-acc|glossary-section|related-guides|related-cards|dr-card-wrap|"
                        r"dr-card|nav-strip|hero-meta|rcm-share|site-header|guide-footer|audience-tabs|hero-toc|"
                        r"translation-notice|header-lang|float-controls|print-btn|dl-fab)\b")
HEAD = {"h1", "h2", "h3", "h4"}


class Extract(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.stack: list[tuple[str, bool, bool]] = []   # (tag, skipping, heading)
        self.body: list[str] = []
        self.heads: list[str] = []
        self.title = ""
        self.meta: dict[str, str] = {}
        self._in_title = False
        self._title_done = False

    def _skipping(self):
        return bool(self.stack) and self.stack[-1][1]

    def _heading(self):
        return bool(self.stack) and self.stack[-1][2]

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "meta":
            k = a.get("name") or a.get("property")
            if k and a.get("content") is not None and k not in self.meta:
                self.meta[k] = a["content"]
            return
        if tag == "title" and not self._title_done:
            self._in_title = True
        if tag in VOID:
            return
        lang = a.get("data-lang")
        skip = (self._skipping() or tag in SKIP_TAGS or (lang is not None and lang != "en")
                or bool(SKIP_CLASS.search(a.get("class") or "")))
        self.stack.append((tag, skip, self._heading() or tag in HEAD))

    def handle_endtag(self, tag):
        if tag == "title":
            self._in_title, self._title_done = False, True
        if tag in VOID:
            return
        for i in range(len(self.stack) - 1, -1, -1):
            if self.stack[i][0] == tag:
                del self.stack[i:]
                return

    def handle_data(self, data):
        if self._in_title:
            self.title += data
            return
        if self._skipping():
            return
        (self.heads if self._heading() else self.body).append(data)


def fold(s: str) -> str:
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()


TOK = re.compile(r"[A-Za-z0-9]+")


def toks(s: str) -> list[str]:
    return TOK.findall(fold(s))


def ngrams(tokens: list[str], nmax: int = 5) -> Counter:
    c = Counter()
    for n in range(1, nmax + 1):
        for i in range(len(tokens) - n + 1):
            c[" ".join(tokens[i:i + n])] += 1
    return c


class Guide:
    def __init__(self, path: Path):
        raw = path.read_text(encoding="utf-8", errors="ignore")
        x = Extract()
        x.feed(raw)
        self.file = path.name
        t = html.unescape(x.meta.get("og:title") or x.title or path.stem)
        self.title = re.sub(r"\s*[·|–—-]\s*(?:Renal Care Matters|W\.? ?Rivero.*|Dr\.? .*Rivero.*)$", "", t).strip()
        self.desc = ws(html.unescape(x.meta.get("description") or x.meta.get("og:description") or ""))
        self.img = local_img(x.meta.get("og:image") or "")
        body, heads = " ".join(x.body), " ".join(x.heads)
        tb, th, tt = toks(body), toks(heads), toks(self.title)
        self.body_lc, self.head_lc, self.title_lc = (ngrams([w.lower() for w in t]) for t in (tb, th, tt))
        self.body_cs, self.head_cs, self.title_cs = ngrams(tb, 3), ngrams(th, 3), ngrams(tt, 3)


def ws(s):
    return re.sub(r"\s+", " ", s or "").strip()


def local_img(u: str) -> str:
    """og:image -> a site-relative path when the file is in the repo (thumbnail), else ''."""
    m = re.match(r"^(?:https?://(?:www\.)?renalcarematters\.com)?(/?(?:\.\./)?images/[^?#\s]+)$", u.strip())
    if not m:
        return ""
    rel = re.sub(r"^/?(?:\.\./)?", "", m.group(1))
    if not (REPO / rel).exists() or not re.search(r"\.(?:jpe?g|png|webp)$", rel, re.I):
        return ""
    return "/" + rel


# ── drug terms ───────────────────────────────────────────────────────────────
SALTS = {"hydrochloride", "hcl", "sodium", "potassium", "calcium", "magnesium", "besilate", "besylate", "maleate", "mesylate",
         "mesilate", "tartrate", "succinate", "fumarate", "citrate", "sulfate", "sulphate", "phosphate", "acetate", "bromide",
         "chloride", "carbonate", "dihydrate", "monohydrate", "trihydrate", "hemihydrate", "hyclate", "propionate", "valerate",
         "dipropionate", "furoate", "xinafoate", "trometamol", "tromethamine", "medoxomil", "cilexetil", "disoproxil", "alafenamide",
         "bitartrate", "hydrobromide", "lactate", "gluconate", "pamoate", "embonate", "nitrate", "anhydrous", "base", "free"}
# Words that name a body substance, lab value or nutrient more often than a medicine: never a term on their own.
NOT_ALONE = {"calcium", "potassium", "sodium", "magnesium", "phosphorus", "phosphate", "glucose", "dextrose", "albumin",
             "water", "oxygen", "iron", "zinc", "bicarbonate", "chloride", "urea", "creatinine", "protein", "insulin",
             "vitamin", "vitamins", "minerals", "amino acids", "multivitamins", "electrolytes", "lactate", "citrate",
             "acetate", "glycine", "sugar", "salt", "fat", "fiber", "copper", "selenium", "iodine", "folate", "carbon",
             "charcoal", "alcohol", "ethanol", "nitrogen", "hydrogen", "air", "saline", "heme",
             "cholesterol", "uric acid", "collagen", "melatonin", "caffeine", "nicotine", "lecithin", "glutathione", "tea"}
EXTRA_TERMS = {   # component -> extra spellings (lowercase)
    "ketoanalogues": ["ketoanalogue", "keto analogue", "ketoacid analogue", "keto acid analogue", "ketoanalog", "keto analog",
                      "ketoacid", "keto acid"],
    "alpha ketoanalogues": ["ketoanalogue", "keto analogue", "ketoacid analogue", "keto acid analogue", "ketoanalog", "ketoacid"],
    "ketoanalogues essential amino acids": ["ketoanalogue", "keto analogue", "ketoacid analogue", "ketoanalog", "ketoacid"],
    "epoetin alfa": ["epoetin", "erythropoietin"],
    "epoetin beta": ["epoetin", "erythropoietin"],
    "darbepoetin alfa": ["darbepoetin"],
    "methoxy polyethylene glycol epoetin beta": ["mircera", "cera"],
    "sevelamer": ["sevelamer carbonate", "sevelamer hydrochloride"],
}


# Drug-class wording guides use instead of the molecule name (component -> class terms, lowercase).
_SGLT2 = ["sglt2 inhibitor", "sglt2i", "sglt 2 inhibitor", "gliflozin"]
_ESA = ["esa", "erythropoiesis stimulating agent", "erythropoietin stimulating agent"]
_BINDER = ["phosphate binder", "phosphorus binder"]
_MRA_NS = ["nonsteroidal mra", "non steroidal mra", "nonsteroidal mineralocorticoid receptor antagonist"]
_HIF = ["hif phi", "hif ph inhibitor", "hif prolyl hydroxylase inhibitor"]
CLASS_TERMS = {
    "dapagliflozin": _SGLT2, "empagliflozin": _SGLT2, "canagliflozin": _SGLT2, "ertugliflozin": _SGLT2,
    "epoetin alfa": _ESA, "epoetin beta": _ESA, "epoetin zeta": _ESA, "darbepoetin alfa": _ESA,
    "methoxy polyethylene glycol epoetin beta": _ESA,
    "sevelamer": _BINDER, "lanthanum carbonate": _BINDER, "sucroferric oxyhydroxide": _BINDER, "ferric citrate": _BINDER,
    "finerenone": _MRA_NS,
    "roxadustat": _HIF, "daprodustat": _HIF, "vadadustat": _HIF,
    "patiromer": ["potassium binder"], "sodium zirconium cyclosilicate": ["potassium binder"],
    "iron sucrose": ["iv iron", "intravenous iron"], "ferric carboxymaltose": ["iv iron", "intravenous iron"],
    "iron dextran": ["iv iron", "intravenous iron"], "ferric derisomaltose": ["iv iron", "intravenous iron"],
}


def norm_term(s: str) -> str:
    return " ".join(w.lower() for w in toks(s))


def strip_salt(s: str) -> str:
    w = norm_term(s).split()
    while len(w) > 1 and w[-1] in SALTS:
        w.pop()
    return " ".join(w)


def comp_terms(ing: str) -> set[str]:
    out = {norm_term(ing), strip_salt(ing)}
    st = synonyms.search_terms([ing], ing)
    for k in ("own", "ing", "miss"):
        out.update(norm_term(x) for x in st.get(k) or [])
    out.update(norm_term(x) for x in EXTRA_TERMS.get(norm_term(ing), []))
    out.update(norm_term(x) for x in CLASS_TERMS.get(norm_term(ing), []) + CLASS_TERMS.get(strip_salt(ing), []))
    out = {t for t in out if t and len(t) >= 4 and t not in NOT_ALONE}
    return out


def with_plurals(terms):
    return {t for x in terms for t in (x, x + "s")}


def count(g: Guide, terms) -> tuple[int, int, int]:
    """(title, heading, body) mentions of any of the terms (longest-first, so 'iron sucrose' is not also counted as 'iron')."""
    ts = sorted(with_plurals(terms), key=lambda t: -len(t))
    def c(ctr):
        n, seen_long = 0, []
        for t in ts:
            k = ctr.get(t, 0)
            # subtract mentions already counted as part of a longer term containing this one
            for L in seen_long:
                if (" " + t + " ") in (" " + L + " "):
                    k -= ctr.get(L, 0)
            if k > 0:
                n += k
            seen_long.append(t)
        return n
    return c(g.title_lc), c(g.head_lc), c(g.body_lc)


def count_cs(g: Guide, forms) -> tuple[int, int, int]:
    return (sum(g.title_cs.get(f, 0) for f in forms), sum(g.head_cs.get(f, 0) for f in forms),
            sum(g.body_cs.get(f, 0) for f in forms))


def score(tc) -> tuple[int, bool]:
    t, h, b = tc
    return 10 * min(t, 1) + 3 * h + b, bool(t or h or b >= 3)


def pick(cands: dict[str, int], keep=4) -> list[list]:
    if not cands:
        return []
    top = max(cands.values())
    out = sorted(((f, s) for f, s in cands.items() if s >= max(3, top * 0.25)), key=lambda x: (-x[1], x[0]))
    return [[f, s] for f, s in out[:keep]]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--show", nargs="*", help="print the picks for these drug slugs (or supplement keys / brand slugs)")
    ap.add_argument("--out", default=str(OUT))
    a = ap.parse_args()

    files = [Path(f) for f in sorted(glob.glob(str(REPO / "guides" / "*.html")))]
    files = [f for f in files if eligible(f.name) and f.name not in EXTRA_SKIP]
    guides = [Guide(f) for f in files]
    gmeta = {g.file: {"t": g.title, "d": g.desc[:240], "img": g.img, "url": f"{SITE}/guides/{g.file[:-5]}"} for g in guides}

    data = REPO / "data" / "drugs"
    generics = json.load(open(data / "generics.json", encoding="utf-8"))

    # lowercase occurrences of each single word across the guides: a brand that is also an ordinary word is skipped
    lower_words = Counter()
    for g in guides:
        for k, v in g.body_cs.items():
            if " " not in k and k.islower():
                lower_words[k] += v

    # brands per generic slug from the registry
    brand_slugs = defaultdict(set)
    for f in sorted(glob.glob(str(data / "registry" / "*.json"))):
        for p in json.load(open(f, encoding="utf-8")):
            b = ws(re.sub(r"[®™©]|\(R\)", " ", p.get("brand_name") or ""))
            if b and p.get("generic_slug"):
                brand_slugs[b].add(p["generic_slug"])
    generic_words = {norm_term(g.get("name", "")) for g in generics.values()} | {norm_term(i) for g in generics.values() for i in g.get("ingredients") or []}
    brands_of = defaultdict(set)
    for b, slugs in brand_slugs.items():
        nb = norm_term(b)
        if len(nb.replace(" ", "")) < 5 or len(slugs) > 2 or nb in generic_words or nb in NOT_ALONE:
            continue
        if any(lower_words.get(w, 0) for w in nb.split()):
            continue                                   # an ordinary English word (or part of one)
        if re.search(r"\d", nb) and not re.search(r"[a-z]{5}", nb):
            continue
        for s in slugs:
            brands_of[s].add(b)

    def brand_forms(b):
        t = toks(b)
        return {" ".join(t), " ".join(w.upper() for w in t), " ".join(w[:1].upper() + w[1:].lower() for w in t)}

    drugs = {}
    for slug, g in generics.items():
        ings = g.get("ingredients") or []
        if not ings:
            continue
        comps = [comp_terms(i) for i in ings]
        if any(not c for c in comps):
            comps = [c for c in comps if c]
            if not comps or len(ings) == 1:
                comps = []
        bforms = set().union(*(brand_forms(b) for b in brands_of.get(slug, ()))) if brands_of.get(slug) else set()
        cands = {}
        for gd in guides:
            tot, ok = 0, True if comps else False
            for c in comps:
                s, q = score(count(gd, c))
                if s == 0:
                    ok = False
                    break
                tot += s
                ok = ok and (q or len(comps) > 1)
            if comps and ok and len(comps) > 1:
                ok = score_combo_ok(gd, comps)
            if bforms:
                bs, bq = score(count_cs(gd, bforms))
                if bs:
                    tot += bs
                    ok = ok or bq
            if ok and tot:
                cands[gd.file] = tot
        picks = pick(cands)
        if picks:
            drugs[slug] = picks

    # supplement keys: top-3 ingredients of each brand plus a few categories, and supplement brand names
    sdir = data / "supplements"
    prods = []
    for f in sorted(sdir.glob("*.json")):
        if not f.name.startswith("_"):
            prods.extend(json.load(open(f, encoding="utf-8")))
    by = defaultdict(list)
    for p in prods:
        by[p["brand_slug"]].append(p)
    keys = set()
    for slug, ps in by.items():
        keys.update(supp_keys(ps))
    skeys = {}
    for k in sorted(keys):
        terms = supp_key_terms(k)
        if not terms:
            continue
        cands = {}
        for gd in guides:
            s, q = score(count(gd, terms))
            if q and s:
                cands[gd.file] = s
        picks = pick(cands, 3)
        if picks:
            skeys[k] = picks
    sbrands = {}
    for slug, ps in by.items():
        names = {p["brand"] for p in ps} | {p.get("brand_registered") for p in ps if p.get("brand_registered")}
        forms = set()
        for n in names:
            nb = norm_term(n)
            if len(nb.replace(" ", "")) < 5 or nb in generic_words or any(lower_words.get(w, 0) for w in nb.split()):
                continue
            forms |= brand_forms(n)
        if not forms:
            continue
        cands = {}
        for gd in guides:
            s, q = score(count_cs(gd, forms))
            if q and s:
                cands[gd.file] = s
        picks = pick(cands, 3)
        if picks:
            sbrands[slug] = picks

    ov = json.load(open(OVERRIDES, encoding="utf-8")) if OVERRIDES.exists() else {}
    for sect, target in (("drugs", drugs), ("supplements", sbrands), ("supplement_keys", skeys)):
        for k, v in (ov.get(sect) or {}).items():
            cur = [x for x in target.get(k, []) if x[0] not in set(v.get("remove") or []) and x[0] not in set(v.get("add") or [])]
            cur = [[f, 100] for f in v.get("add") or [] if f in gmeta] + cur
            if cur:
                target[k] = cur[:4]
            else:
                target.pop(k, None)

    used = {f for d in (drugs, skeys, sbrands) for v in d.values() for f, _ in v}
    out = {"_doc": "Built by tools/drugdb/build_related_guides.py; do not edit (overrides: tools/drugdb/related_guides_overrides.json).",
           "guides": {f: m for f, m in sorted(gmeta.items()) if f in used},
           "drugs": dict(sorted(drugs.items())), "supplement_keys": dict(sorted(skeys.items())),
           "supplement_brands": dict(sorted(sbrands.items()))}
    Path(a.out).write_text(json.dumps(out, ensure_ascii=False, separators=(",", ":")), encoding="utf-8")
    reverse = Counter(f for v in drugs.values() for f, _ in v)
    print(f"guides scanned {len(guides)} · drugs with related guides {len(drugs):,} of {len(generics):,} · "
          f"supplement keys {len(skeys)} · supplement brands by name {len(sbrands)} · "
          f"guides that would gain a 'Drugs mentioned' block {len(reverse)}")
    for s in a.show or []:
        v = drugs.get(s) or skeys.get(s) or sbrands.get(s)
        print(f"  {s}: " + ("; ".join(f"{f} ({sc})" for f, sc in v) if v else "none"))


def score_combo_ok(gd, comps) -> bool:
    """A combination needs every component mentioned, and at least one heading/title hit or 3+ body mentions overall."""
    t = h = b = 0
    for c in comps:
        x = count(gd, c)
        if not any(x):
            return False
        t, h, b = t + x[0], h + x[1], b + x[2]
    return bool(t or h or b >= 3)


SUPP_CAT_KEYS = {"probiotic": "cat:probiotic", "omega-3": "cat:omega-3", "ketoanalogue": "cat:ketoanalogue",
                 "fiber/prebiotic": "cat:fiber"}
CAT_TERMS = {"cat:probiotic": ["probiotic", "synbiotic"], "cat:omega-3": ["omega 3", "fish oil"],
             "cat:ketoanalogue": EXTRA_TERMS["ketoanalogues"] + ["ketoanalogues"],
             "cat:fiber": ["dietary fiber", "fiber supplement", "psyllium", "prebiotic", "inulin"]}


def supp_keys(ps) -> list[str]:
    """The keys a supplement brand page looks up: its top-3 ingredients (by registration count) and category keys."""
    c = Counter(i for p in ps for i in (p.get("ingredients") or [])[:6])
    ks = [i for i, _ in c.most_common(3)]
    cats = {x for p in ps for x in p.get("categories") or []}
    ks += [SUPP_CAT_KEYS[x] for x in sorted(cats) if x in SUPP_CAT_KEYS]
    return ks


def supp_key_terms(k: str) -> set[str]:
    if k.startswith("cat:"):
        return {norm_term(x) for x in CAT_TERMS.get(k, [])}
    if re.match(r"(?:Lactobacillus|Bifidobacterium|Streptococcus|Saccharomyces|Bacillus|Lactococcus|Enterococcus)\b", k):
        return set()                                  # strains: covered by cat:probiotic
    if k.startswith("Ketoanalogues"):
        return {norm_term(x) for x in CAT_TERMS["cat:ketoanalogue"]}
    out = set()
    m = re.match(r"^(.*?)\s*\(([^)]*)\)\s*$", k)
    parts = [m.group(1), m.group(2)] if m else [k]
    for part in parts:
        for x in re.split(r",\s*", part):
            t = norm_term(x)
            if t and len(t) >= 4:
                out.add(t)
    if k == "Iron":
        return {"iron supplement", "oral iron", "iron tablet", "ferrous sulfate", "ferrous", "iron"}
    return {t for t in out if t not in NOT_ALONE - {"iron"}}


if __name__ == "__main__":
    main()
