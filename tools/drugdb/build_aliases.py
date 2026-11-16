#!/usr/bin/env python3
"""Map variant / misspelled PH FDA generic names to their main molecule page.

The FDA Philippines registry carries many spellings of the same generic ("Allopurino",
"AcicIovir", "Ambroxol Hydrchloride", "Losartan Potassiumn", "Amiodarone Hydrochloride Bp",
INN vs USAN names such as Aciclovir vs Acyclovir). Each spelling gets its own generic slug and
therefore its own thin drug page. This script finds the main page for each variant so the
generator can send readers there.

Output: data/drugs/aliases.json
  {variant_slug: {"main": canonical_slug, "reason": "typo|salt|spelling|inn-usan|combination-order",
                  "confidence": "high|medium", "note": "..."}}
Report: a Markdown review list (default /home/claude/work/aliases-report.md, or --report PATH).

Rules
- Ingredients are normalized first: text after " as " is dropped (salt statements), salt and form words are
  removed (hydrochloride, potassium, bp, usp, base, monohydrate, ...; the salt list is shared with
  build_registry.py and fetch_fda_labels.py), punctuation is ignored, and the INN -> USAN alias list from
  fetch_fda_labels.py is applied. Two generics with the same normalized ingredient set are the same molecule.
- Typo matching: a token that is not a known drug word may be corrected to a known token at edit distance
  <= 2 (tokens of 6+ characters) or <= 1 (shorter tokens), only when the correction is unique.
  "Known" tokens come from generics with a US label, approved content, or 3+ products, plus the salt list.
  A token that is itself a real drug word (PNF, price lists, US label substance names, or any generic with
  3+ products) is never "corrected", so cefixime can never map to cefuroxime.
- Combinations must match ingredient-for-ingredient. A combination that only matches after re-splitting
  its ingredients (e.g. "aluminum hydroxide magnesium hydroxide" written as one ingredient) is medium.
- The main must be richer than the variant: approved kidney or summary content, a US label, or 3x the
  products. For exact normalized matches (salt / spelling / INN-USAN) the richest member of the group is the
  main whenever it is strictly richer.
- Manual corrections: tools/drugdb/alias_overrides.json
  {"reject": ["variant", "variant>main"], "force": {"variant": {"main": "...", "reason": "...", "confidence": "..."}}}

Usage: python3 tools/drugdb/build_aliases.py [--data-dir data/drugs] [--report PATH] [--dry-run]
"""
from __future__ import annotations

import argparse
import importlib.util
import json
import re
import sys
import unicodedata
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent


def _load(name):
    spec = importlib.util.spec_from_file_location(name, HERE / f"{name}.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


REG = _load("build_registry")
FETCH = _load("fetch_fda_labels")

# hydrate / form / pharmacopeia words: removed from every ingredient
FORM_WORDS = {"bp", "usp", "ph", "eur", "ep", "jp", "base", "salt", "hydrate", "micronized", "micronised", "anhydrous",
              "monohydrate", "dihydrate", "trihydrate", "tetrahydrate", "pentahydrate", "hexahydrate", "heptahydrate",
              "hemihydrate", "sesquihydrate", "amorphous", "crystalline", "equivalent", "hc1"}
# words that make a different drug or a non-interchangeable product, so they are never stripped
# (benzathine vs plain benzylpenicillin, hyoscine butylbromide vs hydrobromide, mycophenolate mofetil vs sodium,
#  tenofovir disoproxil vs alafenamide, isosorbide mononitrate vs dinitrate, aluminum hydroxide, ...)
PROTECTED = {"benzathine", "procaine", "methylbromide", "butylbromide", "mofetil", "disoproxil", "alafenamide",
             "mononitrate", "dinitrate", "hydroxide", "oxide", "carbonate", "bicarbonate", "iodide", "trisilicate",
             "dipropionate", "propionate", "valerate", "acetonide", "furoate", "decanoate", "enanthate", "cypionate",
             "palmitate", "undecanoate", "pamoate", "embonate", "xinafoate"}
# salt words removed from a drug name (not from a leading-active name such as "potassium chloride")
DROP_WORDS = ((set(REG.SALT_WORDS) | set(FETCH.SALT_WORDS) | set(FETCH.NOISE_WORDS) | FORM_WORDS)
              - {"in", "to", "recombinant", "regular", "rdna", "dna"} - PROTECTED)
PRE_NORMALIZE = [(re.compile(r"\bn?[\s-]*butyl[\s-]*bromide\b"), "butylbromide"),
                 (re.compile(r"\bisosorbide[\s-]+5[\s-]+"), "isosorbide ")]
LEADING_ACTIVE = set(REG.LEADING_ACTIVE)
# entries in the fetcher's INN->USAN list that are misspellings, not name pairs
TYPO_ALIASES = {"cetrizine", "desloratidine", "doxycyline", "potasium", "potassiumn", "co-amoxoclav",
                "guiafenesin", "dextromethophan", "trimetazidime"}
INN_USAN = {k: v for k, v in FETCH.INN_TO_USAN.items() if k != v}


def fold(s: str) -> str:
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()


def raw_tokens(ingredient: str) -> list[str]:
    s = fold(ingredient)
    for rx, rep in PRE_NORMALIZE:
        s = rx.sub(rep, s)
    s = re.sub(r"\([^)]*\)?", " ", s)
    s = re.sub(r"\bas\b.*$", " ", s)              # "cefuroxime as axetil0", "amlodipine as"
    # numbers are kept: "5% dextrose in 0.3% sodium chloride" is not "... 0.9% ...", PCV13 is not PCV15
    return [t for t in re.split(r"[^a-z0-9]+", s) if t]


def osa(a: str, b: str, cap: int = 3) -> int:
    """Optimal string alignment distance (adjacent transposition = 1), early exit above cap."""
    if abs(len(a) - len(b)) > cap:
        return cap + 1
    prev2, prev = None, list(range(len(b) + 1))
    for i in range(1, len(a) + 1):
        cur = [i] + [0] * len(b)
        for j in range(1, len(b) + 1):
            c = 0 if a[i - 1] == b[j - 1] else 1
            cur[j] = min(prev[j] + 1, cur[j - 1] + 1, prev[j - 1] + c)
            if i > 1 and j > 1 and a[i - 1] == b[j - 2] and a[i - 2] == b[j - 1]:
                cur[j] = min(cur[j], prev2[j - 2] + 1)
        if min(cur) > cap:
            return cap + 1
        prev2, prev = prev, cur
    return prev[-1]


def max_dist(tok: str) -> int:
    return 2 if len(tok) >= 6 else 1


def plausible_typo(tok: str, cand: str, d: int) -> bool:
    """Distance 1 anywhere; distance 2 only for long words that share their first three letters
    (rejects tenoxicam/meloxicam, reteplase/alteplase, nadifloxacin/gatifloxacin, folinic/folic)."""
    if d <= 1:
        return True
    return len(tok) >= 8 and tok[:3] == cand[:3]


class Builder:
    def __init__(self, data_dir: Path):
        self.d = data_dir
        self.g = json.loads((data_dir / "generics.json").read_text())
        self.info = {}
        for slug, e in self.g.items():
            self.info[slug] = {"label": (data_dir / "labels" / f"{slug}.json").exists(),
                               "approved": self._approved(slug), "products": int(e.get("products") or 0)}
        self._real_words()
        self._vocab()

    def _approved(self, slug):
        for sub in ("renal", "summary"):
            p = self.d / sub / f"{slug}.json"
            if p.exists():
                try:
                    if str(json.loads(p.read_text()).get("review_status", "")).lower() == "approved":
                        return True
                except Exception:
                    pass
        return False

    def richness(self, slug):
        i = self.info[slug]
        return (1 if i["approved"] else 0, 1 if i["label"] else 0, i["products"])

    def richer(self, main, var):
        m, v = self.info[main], self.info[var]
        if m["approved"] and not v["approved"]:
            return True
        if v["approved"] and not m["approved"]:
            return False
        if m["label"] and not v["label"]:
            return True
        return m["products"] >= 3 * max(1, v["products"])

    def _real_words(self):
        """Words that are known drug names in their own right (never typo-corrected)."""
        real = set()
        for f in ("pnf.json", "prices.json"):
            p = self.d / f
            if p.exists():
                for k in json.loads(p.read_text()):
                    if not k.startswith("_"):
                        real.update(t for t in k.split("-") if t)
        for p in (self.d / "labels").glob("*.json"):
            try:
                lab = json.loads(p.read_text()).get("label") or {}
            except Exception:
                continue
            for k in ("substance_name", "generic_name"):
                v = lab.get(k)
                for x in (v if isinstance(v, list) else [v]):
                    real.update(t for t in re.split(r"[^a-z0-9]+", fold(str(x or ""))) if t)
        for slug, e in self.g.items():
            if self.info[slug]["products"] >= 3 or self.info[slug]["approved"]:
                for ing in e.get("ingredients") or []:
                    real.update(raw_tokens(ing))
        real -= TYPO_ALIASES
        self.real = real

    def _vocab(self):
        v = set(DROP_WORDS) | set(LEADING_ACTIVE) | PROTECTED
        self.freq = defaultdict(int)
        for t in v:
            self.freq[t] += 1000      # salt / form words are always preferred over a rare spelling
        for slug, e in self.g.items():
            i = self.info[slug]
            for ing in e.get("ingredients") or []:
                for t in raw_tokens(ing):
                    self.freq[t] += i["products"]
            if i["label"] or i["approved"] or i["products"] >= 3:
                for ing in e.get("ingredients") or []:
                    v.update(t for t in raw_tokens(ing) if t not in TYPO_ALIASES)
        self.vocab = v
        self.vocab_by_len = defaultdict(list)
        for t in v:
            self.vocab_by_len[len(t)].append(t)

    def correct(self, tok):
        """(corrected token, distance) or (tok, 0) when known / uncorrectable."""
        if tok in self.vocab or tok in self.real or len(tok) < 4 or tok.isdigit():
            return tok, 0
        md = max_dist(tok)
        best, bd = [], md + 1
        for L in range(len(tok) - md, len(tok) + md + 1):
            for c in self.vocab_by_len.get(L, ()):
                d = osa(tok, c, md)
                if d < bd:
                    best, bd = [c], d
                elif d == bd:
                    best.append(c)
        if len(best) > 1:      # tie: take the dominant spelling (10x more products), else give up
            best.sort(key=lambda c: -self.freq[c])
            if self.freq[best[0]] >= 10 * max(1, self.freq[best[1]]):
                best = best[:1]
        if bd <= md and len(best) == 1 and plausible_typo(tok, best[0], bd):
            return best[0], bd
        return tok, 0

    def norm_ingredient(self, ing, use_typo):
        toks, fixes = raw_tokens(ing), []
        if use_typo:
            out = []
            for t in toks:
                c, d = self.correct(t)
                if d:
                    fixes.append((t, c, d))
                out.append(c)
            toks = out
        if not toks:
            return "", fixes
        drop = FORM_WORDS if toks[0] in LEADING_ACTIVE else DROP_WORDS
        kept = [t for t in toks if t not in drop]
        if not kept:
            kept = toks
        phrase = " ".join(kept)
        return phrase, fixes

    def key(self, slug, use_typo=False, inn=True):
        ings, fixes, innhit = [], [], False
        for ing in self.g[slug].get("ingredients") or []:
            p, f = self.norm_ingredient(ing, use_typo)
            fixes += f
            if inn:
                q = FETCH.usan(p) if p else p
                q = re.sub(r"[^a-z0-9 ]+", " ", q.replace("-", " "))
                q = " ".join(q.split())
                if q != p:
                    innhit = innhit or any(k in p for k in INN_USAN if k not in TYPO_ALIASES and k in p)
                    p = q
            for part in re.split(r"\s+and\s+", p):
                if part:
                    ings.append(part.replace(" ", ""))
        self._dups = len(ings) != len(set(ings))
        return tuple(sorted(set(ings))), fixes, innhit

    def build(self):
        exact = defaultdict(list)          # key without typo correction
        for slug in self.g:
            k, _, _ = self.key(slug)
            if k:
                exact[k].append(slug)
        out, rejected = {}, []

        def best_of(slugs):
            return max(slugs, key=lambda s: (self.richness(s), -len(s), s))

        # 1. exact normalized groups (salt / spelling / INN-USAN)
        for k, slugs in exact.items():
            if len(slugs) < 2:
                continue
            main = best_of(slugs)
            for v in slugs:
                if v == main:
                    continue
                if not (self.richness(main) > self.richness(v)):
                    rejected.append((v, main, "not richer than the variant"))
                    continue
                kv, km = self.key(v, inn=False)[0], self.key(main, inn=False)[0]
                if kv != km:
                    reason, note = "inn-usan", "INN and US (USAN) names of the same molecule"
                elif self._salt_diff(v, main):
                    reason, note = "salt", "same molecule; salt, form or pharmacopeia words differ"
                else:
                    reason, note = "spelling", "same molecule; punctuation or spacing differs"
                if any(t in TYPO_ALIASES for ing in self.g[v]["ingredients"] for t in raw_tokens(ing) + [fold(ing)]):
                    reason, note = "typo", "known misspelling"
                self.key(v)
                conf = "high"
                if self._dups:
                    conf, note = "medium", note + "; the variant lists an ingredient twice (multi-tablet pack?)"
                out[v] = {"main": main, "reason": reason, "confidence": conf, "note": note}

        # 2. typo matches against richer generics
        by_key = defaultdict(list)
        for k, slugs in exact.items():
            by_key[k].extend(slugs)
        for v in self.g:
            if v in out:
                continue
            k2, fixes, _ = self.key(v, use_typo=True)
            if not fixes or not k2:
                continue
            cands = [s for s in by_key.get(k2, []) if s != v]
            if not cands:
                continue
            main = best_of(cands)
            if main in out:
                main = out[main]["main"]
            if not self.richer(main, v):
                rejected.append((v, main, "candidate not richer (needs US label, approved content or 3x products)"))
                continue
            only_salt = all(c in DROP_WORDS for _, c, _ in fixes)
            hi = all(t[:2] == c[:2] or t[1:] == c[1:] or t == c[1:] or t[1:] == c for t, c, d in fixes) \
                and self.info[v]["products"] <= 2
            hi = hi or all(t in TYPO_ALIASES for t, _, _ in fixes)
            hi = hi and (only_salt or self.info[main]["label"] or self.info[main]["approved"]
                         or self.info[main]["products"] >= 10 * max(1, self.info[v]["products"]))
            fx = ", ".join(f"{t} -> {c}" for t, c, _ in fixes)
            out[v] = {"main": main, "reason": "typo", "confidence": "high" if hi else "medium",
                      "note": f"misspelling corrected: {fx}"}

        # 3. combinations that only match when their ingredient words are re-split
        word_key = defaultdict(list)
        for v in self.g:
            toks = []
            for ing in self.g[v].get("ingredients") or []:
                p, _ = self.norm_ingredient(ing, True)
                toks += p.split()
            word_key[tuple(sorted(toks))].append(v)
        for wk, slugs in word_key.items():
            if len(slugs) < 2 or len(wk) < 2:
                continue
            main = best_of(slugs)
            if main in out:
                continue
            for v in slugs:
                if v == main or v in out:
                    continue
                if len(self.g[v]["ingredients"]) == len(self.g[main]["ingredients"]):
                    continue   # same count: would have matched above; different molecules
                if not self.richer(main, v):
                    rejected.append((v, main, "combination re-split candidate not richer"))
                    continue
                vt = [self.norm_ingredient(i, True)[0].split() for i in self.g[v]["ingredients"]]
                mt = [self.norm_ingredient(i, True)[0].split() for i in self.g[main]["ingredients"]]
                ok = all(any(self._contig(m, x) for x in vt) for m in mt)
                out[v] = {"main": main, "reason": "combination-order", "confidence": "high" if ok else "medium",
                          "note": "same ingredients written without separators" if ok
                          else "same ingredient words, split differently into ingredients"}

        # chains: a main that is itself a variant
        for v, e in out.items():
            seen = {v}
            while e["main"] in out and e["main"] not in seen:
                seen.add(e["main"])
                e["main"] = out[e["main"]]["main"]
        return out, rejected

    @staticmethod
    def _contig(sub, seq):
        n = len(sub)
        return n > 0 and any(seq[i:i + n] == sub for i in range(len(seq) - n + 1))

    def _salt_diff(self, a, b):
        def words(s):
            return {t for ing in self.g[s]["ingredients"] for t in raw_tokens(ing)}
        return bool((words(a) ^ words(b)) & DROP_WORDS) or any(" as " in f" {fold(i)} " for i in self.g[a]["ingredients"])


def apply_overrides(out, rejected, path: Path, g):
    if not path.exists():
        return
    ov = json.loads(path.read_text())
    for r in ov.get("reject", []):
        v, _, m = r.partition(">")
        if v in out and (not m or out[v]["main"] == m):
            rejected.append((v, out[v]["main"], "rejected in alias_overrides.json"))
            del out[v]
    for v, e in (ov.get("force") or {}).items():
        if v in g and e.get("main") in g:
            out[v] = {"main": e["main"], "reason": e.get("reason", "typo"), "confidence": e.get("confidence", "high"),
                      "note": e.get("note", "set by hand in alias_overrides.json")}


def write_report(path: Path, out, rejected, b: Builder):
    by_conf = defaultdict(list)
    for v, e in out.items():
        by_conf[e["confidence"]].append((v, e))
    lines = ["# Drug database: variant generic names mapped to a main page", "",
             f"Generated by `tools/drugdb/build_aliases.py`. {len(out)} mappings "
             f"({len(by_conf['high'])} high, {len(by_conf['medium'])} medium).", "",
             "High-confidence variant pages show a banner to the main monograph, carry a canonical link to it and are "
             "`noindex`; their products are also listed on the main page. Medium-confidence pages only show a "
             "\"Did you mean\" link. To drop a wrong mapping, add the variant slug to `reject` in "
             "`tools/drugdb/alias_overrides.json` and rebuild.", ""]
    for conf in ("high", "medium"):
        lines += [f"## {conf.capitalize()} confidence ({len(by_conf[conf])})", "",
                  "| Variant page | Registered as | Products (brands) | Main page | Main products | Reason | Note |",
                  "|---|---|---|---|---|---|---|"]
        for v, e in sorted(by_conf[conf], key=lambda x: (x[1]["reason"], x[0])):
            gv, gm = b.g[v], b.g[e["main"]]
            brands = sorted({x for x in gv.get("_brands", [])})
            lines.append(f"| `{v}` | {' / '.join(gv.get('registered_names', [])[:2])} | {gv['products']}"
                         f"{' (' + ', '.join(brands[:4]) + ')' if brands else ''} | `{e['main']}` ({gm['name']}) | "
                         f"{gm['products']}{' · US label' if b.info[e['main']]['label'] else ''}"
                         f"{' · approved' if b.info[e['main']]['approved'] else ''} | {e['reason']} | {e['note']} |")
        lines.append("")
    lines += [f"## Rejected candidates ({len(rejected)})", "", "| Variant | Candidate main | Why not mapped |", "|---|---|---|"]
    for v, m, why in sorted(rejected):
        lines.append(f"| `{v}` ({b.g[v]['products']}) | `{m}` ({b.g.get(m, {}).get('products', '?')}) | {why} |")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("\n".join(lines) + "\n")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--data-dir", default=str(REPO / "data" / "drugs"))
    ap.add_argument("--report", default="/home/claude/work/aliases-report.md")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    d = Path(a.data_dir)
    b = Builder(d)
    # brand names per generic, for the report
    for f in sorted((d / "registry").glob("*.json")):
        for p in json.loads(f.read_text()):
            s = p.get("generic_slug")
            if s in b.g and (p.get("brand_name") or "").strip():
                b.g[s].setdefault("_brands", []).append(p["brand_name"].strip())
    out, rejected = b.build()
    apply_overrides(out, rejected, HERE / "alias_overrides.json", b.g)
    out = dict(sorted(out.items()))
    cnt = defaultdict(int)
    for e in out.values():
        cnt[(e["confidence"], e["reason"])] += 1
    print(f"{len(out)} mappings: " + ", ".join(f"{c}/{r} {n}" for (c, r), n in sorted(cnt.items()))
          + f"; {len(rejected)} rejected")
    if a.report:
        write_report(Path(a.report), out, rejected, b)
        print("report:", a.report)
    if not a.dry_run:
        (d / "aliases.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n")


if __name__ == "__main__":
    main()
