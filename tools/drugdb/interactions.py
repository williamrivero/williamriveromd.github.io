#!/usr/bin/env python3
"""
interactions.py — data for the Dosis interaction checker (drugs/interactions.html), Nov 2026.

Source rows: the APPROVED "key_interactions" of data/drugs/summary/<slug>.json (each row: drug_or_class, effect,
action, severity). Nothing here writes clinical text: the checker shows each row's own wording and grade. This module
only works out WHICH selected drugs a row's drug_or_class refers to:
  * named drugs  — every ingredient name, salt-stripped name and synonym (tools/drugdb/synonyms.py via the
                   generator's Ctx.single_slug) found in the text, as a molecule id (single-agent page slug, else the
                   normalized name);
  * classes      — tools/drugdb/interaction_classes.json ('detect' regex on the text; members by name, member_rx and
                   included classes; "nephrotoxic" = every ingredient tagged in data/drugs/nephrotox.json).
Rows about food, alcohol, lab tests or procedures ('nondrug') are listed per drug under "Also check", and rows that
match nothing are listed per drug under "Other listed interactions", so no approved row is ever dropped.

Grades (most to least severe): ci = Contraindicated (the row's action starts with an unconditional "Contraindicated"),
avoid = Avoid, adjust = Adjust or monitor, minor = Minor.

  python3 tools/drugdb/interactions.py --report      # resolution coverage and the rows that matched nothing
"""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
CLASSES = REPO / "tools" / "drugdb" / "interaction_classes.json"
SEV = {"avoid": "avoid", "adjust or monitor": "adjust", "minor": "minor"}
CI = re.compile(r"^contraindicated(?: in this PI)?\s*[.;]", re.I)
SALT = re.compile(r"\s+(?:as|hydrochloride|hcl|dihydrochloride|sodium|potassium|calcium|magnesium|carbonate|sulfate|sulphate|"
                  r"citrate|maleate|besylate|besilate|mesylate|mesilate|tartrate|succinate|fumarate|acetate|phosphate|"
                  r"hydrobromide|disodium|trihydrate|monohydrate|dihydrate|gluconate|lactate|bitartrate|dipropionate|"
                  r"propionate|valerate|furoate|bromide|chloride|tromethamine|meglumine|hyclate|axetil|pivoxil|"
                  r"dipivoxil|disoproxil fumarate|base|anhydrous|usp|bp)\b.*$", re.I)


STOPWORD = re.compile(r"^(?:oral|beta|alpha|plus|forte|extract|complex|vitamin|vitamins|multivitamins?|minerals?|other|"
                      r"tablets?|capsules?|solution|syrup|injection|cream|drops|powder|mixed|active|natural)$")
CYP3A = re.compile(r"CYP3A4? inhibitors?", re.I)


def norm(s: str) -> str:
    return re.sub(r"\s+", " ", (s or "").strip().lower())


class Resolver:
    def __init__(self, ctx):
        self.ctx = ctx
        spec = json.loads(CLASSES.read_text(encoding="utf-8"))
        self.spec = spec
        self.nondrug = re.compile(spec["nondrug"], re.I)
        stop = {norm(x) for x in spec.get("stop_names", [])}
        self.classes = {c["key"]: c for c in spec["classes"]}
        self.detect = [(c["key"], re.compile(c["detect"], re.I)) for c in spec["classes"]]
        # molecules: id -> set of names
        self.names: dict[str, set[str]] = {}
        for g in ctx.generics.values():
            for ing in g.get("ingredients") or []:
                self.mol(ing)
        sys.path.insert(0, str(REPO / "tools" / "drugdb"))
        import synonyms as SYN
        for grp in SYN.GROUPS:            # US/British names onto the molecule that has a page (rifampin -> rifampicin)
            ms = [self.ctx.single_slug(n) for n, _ in grp]
            m = next((x for x in ms if x), None)
            if m:
                self.names.setdefault(m, set()).update(norm(n) for n, _ in grp)
        vocab = {}
        for m, ns in self.names.items():
            for n in ns:
                if len(n) >= 5 and n not in stop and not re.fullmatch(r"[\d\s.%/-]+", n) and not STOPWORD.search(n):
                    vocab.setdefault(n, m)
        # longest names first so "tenofovir alafenamide" wins over "tenofovir"
        self.vocab = sorted(vocab.items(), key=lambda kv: -len(kv[0]))
        self.vocab_rx = [(re.compile(r"(?<![a-z0-9])" + re.escape(n) + r"(?![a-z0-9])"), m) for n, m in self.vocab]
        nx = (ctx.nephrotox or {}).get("ingredients") or {}
        self.nx_keys = set(nx)
        self._members: dict[str, set[str]] = {}

    def mol(self, name: str) -> str:
        """Molecule id for an ingredient or drug name (single-agent page slug, else the salt-stripped name)."""
        n = norm(name)
        base = norm(SALT.sub("", n)) or n
        m = self.ctx.single_slug(n) or self.ctx.single_slug(base) or base.replace(" ", "-")
        s = self.names.setdefault(m, set())
        s.update({n, base, m.replace("-", " ")})
        return m

    def mol_names(self, m: str) -> set[str]:
        return self.names.get(m, {m.replace("-", " ")})

    def members(self, key: str, seen=None) -> set[str]:
        """Molecule ids in a class (memoized)."""
        if key in self._members:
            return self._members[key]
        seen = (seen or set()) | {key}
        c = self.classes[key]
        out: set[str] = set()
        for n in c.get("members") or []:
            out.add(self.mol(n))
        if c.get("member_rx"):
            rx = re.compile(c["member_rx"], re.I)
            out |= {m for m, ns in self.names.items() if any(rx.search(n) for n in ns)}
        if key == "nephrotoxic":
            out |= {m for m, ns in self.names.items() if any(n in self.nx_keys or any(n.startswith(k + " ") for k in self.nx_keys) for n in ns)}
        for inc in c.get("includes") or []:
            if inc not in seen:
                out |= self.members(inc, seen)
        self._members[key] = out
        return out

    def classes_of(self, m: str) -> list[str]:
        return [k for k in self.classes if k != "alloral" and m in self.members(k)]

    def resolve(self, text: str) -> dict:
        t = norm(text)
        if self.nondrug.search(t) and not re.search(r"\bdrugs?\b|medicines?|inhibitors?|antagonists?", t):
            # a row about food, alcohol, tests or procedures (a drug named in it still counts, e.g. "Paracetamol, halothane")
            pass
        cls = [k for k, rx in self.detect if rx.search(text) and k not in ("strong3a4inh", "mod3a4inh")]
        if CYP3A.search(text):        # strength-qualified, or both strong and moderate when the row names none
            strong = re.search(r"(strong|potent)[^;)]*CYP3A", text, re.I)
            mod = re.search(r"(moderate|mild)[^;)]*CYP3A", text, re.I)
            weak = re.search(r"weak[^;)]*CYP3A", text, re.I)
            if strong or not (mod or weak):
                cls.append("strong3a4inh")
            if mod or not (strong or weak):
                cls.append("mod3a4inh")
        mols, rest = [], t
        for rx, m in self.vocab_rx:
            if rx.search(rest):
                if m not in mols:
                    mols.append(m)
                rest = rx.sub(" ", rest)
        nd = bool(self.nondrug.search(t)) and not mols and not cls
        return {"m": mols, "c": cls, "nd": nd}


def build(ctx, slugs: list[str], forms_of, oral_of, local_of) -> tuple[dict, dict]:
    """(client data, report). slugs = generic pages in the index; *_of(slug) -> bool helpers from the generator."""
    R = Resolver(ctx)
    rows, report = [], {"rows": 0, "matched": 0, "nondrug": 0, "unmatched": []}
    owners_with_rows = set()
    for slug in slugs:
        sm = ctx.summary(slug)
        if not sm or sm.get("review_status") != "approved":
            continue
        for r in sm.get("key_interactions") or []:
            if not isinstance(r, dict) or not (r.get("drug_or_class") or "").strip():
                continue
            sev = SEV.get(norm(r.get("severity")), "adjust")
            if sev == "avoid" and CI.match((r.get("action") or "").strip()):
                sev = "ci"
            res = R.resolve(r["drug_or_class"])
            report["rows"] += 1
            if res["m"] or res["c"]:
                report["matched"] += 1
            elif res["nd"]:
                report["nondrug"] += 1
            else:
                report["unmatched"].append((slug, r["drug_or_class"]))
            rows.append([slug, sev, r["drug_or_class"], r.get("effect") or "", r.get("action") or "",
                         res["m"], res["c"], 1 if res["nd"] else 0])
            owners_with_rows.add(slug)
    G = {}
    for slug in slugs:
        g = ctx.generics.get(slug) or {}
        ings = g.get("ingredients") or []
        mols = list(dict.fromkeys(R.mol(i) for i in ings)) or [slug]
        cls = sorted({k for m in mols for k in R.classes_of(m)})
        ow = [slug] + [m for m in mols if m != slug and m in owners_with_rows]
        e = {"m": mols}
        if cls:
            e["c"] = cls
        ow = [o for o in ow if o in owners_with_rows]
        if ow:
            e["ow"] = ow
        if oral_of(slug):
            e["o"] = 1
        if local_of(slug):
            e["loc"] = 1
        G[slug] = e
    data = {"v": 1, "cls": {k: c["label"] for k, c in R.classes.items()}, "rows": rows, "g": G}
    return data, report


if __name__ == "__main__":
    import importlib.util
    import datetime as dt
    spec = importlib.util.spec_from_file_location("gen", REPO / "generate_drug_pages.py")
    gen = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(gen)
    ctx = gen.Ctx(REPO / "data" / "drugs", dt.date.today())
    slugs = sorted(s for s in ctx.generics if ctx.by_slug.get(s))
    data, rep = build(ctx, slugs, None, lambda s: False, lambda s: False)
    print(f"rows {rep['rows']}: matched {rep['matched']}, food/lab/procedure {rep['nondrug']}, unmatched {len(rep['unmatched'])}")
    if "--report" in sys.argv:
        for s, t in rep["unmatched"]:
            print(f"  {s:30s} | {t}")
        if "--rows" in sys.argv:
            for r in data["rows"]:
                print(f"  {r[0]:22s} {r[1]:6s} {r[2][:70]:70s} -> m={r[5][:6]} c={r[6]}")
