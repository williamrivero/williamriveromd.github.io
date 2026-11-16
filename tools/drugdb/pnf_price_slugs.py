"""Shared name -> generic-slug resolver for the PNF (build_pnf.py) and price (build_prices.py) builders.

Slugs follow the contract via build_registry.ingredients_of / slug_of. Government lists (PNF, DPRI, GAMOT) and the
PH FDA registry spell many generics differently (salts, synonyms, word order, typos), so resolve() returns:
  primary  - the slug to key the record under (a registry slug when one matches, else the contract slug of the name)
  matches  - every generics.json slug judged to be the same generic (the record is copied under each)
"""
import json, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from build_registry import ingredients_of, slug_of, SALT_WORDS  # noqa: E402

REPO = os.path.dirname(os.path.dirname(HERE))

# whole-name rewrites for list headings written "Name, Qualifier" or under a non-registry name
NAME_FIXES = [
    (r"^Albumin, Human", "Human Albumin"), (r"^Alcohol, Ethyl", "Ethyl Alcohol"), (r"^Calamine, Plain", "Calamine"),
    (r"^Dextran, High Molecular Weight.*", "Dextran 70"), (r"^Immunoglobulin Normal, Human.*", "Human Normal Immunoglobulin"),
    (r"^Regular, Insulin.*", "Human Insulin"), (r"^Amino Acids, Crystalline Standard", "Amino Acids"),
    (r"^Penicillin G Benzathine.*", "Benzathine Benzylpenicillin"), (r"^Penicillin G Crystalline.*", "Benzylpenicillin"),
    (r"^Phenoxymethyl Penicillin.*", "Phenoxymethylpenicillin"), (r"^Glyceryl trinitrate.*", "Nitroglycerin"),
    (r"^Fusidate Sodium / Fusidic Acid", "Fusidic Acid"), (r"^Lagundi.*|^Vitex Negundo.*", "Vitex negundo L."),
    (r"^Sambong.*", "Blumea balsamifera"), (r"^Tsaang Gubat.*", "Carmona retusa"),
    (r"^Ferrous Salt \(Iron Preparations\)|^Iron \(Ferrous Salt\)", "Ferrous Salt"),
    (r"^Folic acid \+ Iron Ferrous", "Ferrous Salt + Folic Acid"),
    (r"^Co-amoxiclav \(Amoxicillin \+ Clavulanic acid\)", "Amoxicillin + Clavulanic acid"),
    (r"^Oral Rehydration Salts.*", "Oral Rehydration Salts"), (r"^Potassium \(as citrate\)", "Potassium Citrate"),
    (r"^Monobasic/Dibasic Sodium Phosphate", "Sodium Phosphate"),
]
WORD_FIXES = {
    "lumefantrin": "lumefantrine", "anastrazole": "anastrozole", "polymixin": "polymyxin", "tenofuvir": "tenofovir",
    "dapirivine": "dapivirine", "flouride": "fluoride", "ceftaxidime": "ceftazidime", "latanoporst": "latanoprost",
    "leuproreline": "leuprorelin", "benyzylpenicillin": "benzylpenicillin", "chlopheniramine": "chlorphenamine",
    "phytonadione": "phytomenadione", "sevelemer": "sevelamer", "formeterol": "formoterol",
    "diptheria": "diphtheria", "alendronate": "alendronic acid", "tamsnlosin": "tamsulosin",
}
# words ignored when comparing a list name with a registry generic (salt forms, origin qualifiers)
DROP = set(SALT_WORDS) | {"etexilate", "human", "recombinant", "dna", "equine", "base", "salt", "as", "l", "anhydrous"}


def _fix(name):
    n = name.strip()
    for pat, rep in NAME_FIXES:
        if re.match(pat, n, flags=re.I):
            n = re.sub(pat, rep, n, flags=re.I)
            break
    for a, b in WORD_FIXES.items():
        n = re.sub(r"\b%s\b" % a, b, n, flags=re.I)
    return n


def _reduce(ings):
    out = []
    for i in ings:
        w = [x for x in re.split(r"[\s\-]+", i) if x and x not in DROP]
        out.append(" ".join(w) or i)
    return frozenset(out)


class Resolver:
    def __init__(self, generics_path=None):
        path = generics_path or os.path.join(REPO, "data", "drugs", "generics.json")
        self.generics = json.load(open(path, encoding="utf-8"))
        self.index = {}
        for k, v in self.generics.items():
            self.index.setdefault(_reduce(v.get("ingredients") or [k]), []).append(k)

    def candidates(self, name):
        n = _fix(name)
        cands = []
        if "+" in n and not re.search(r"\([^)]*\+[^)]*\)", n):
            cands.append(re.sub(r"\([^)]*\)", " ", n))            # plain combination
        cands.append(n)
        cands.append(re.sub(r"\([^)]*\)", " ", n))
        for g in re.findall(r"\(([^()]*)\)", n):
            if not re.match(r"\s*(as|equiv|for|e\.g|type|types|\d)", g, re.I) and len(g) > 3:
                cands.append(g)
        seen, out = set(), []
        for c in cands:
            ings = ingredients_of(c)
            s = slug_of(ings)
            if ings and s not in seen:
                seen.add(s)
                out.append((s, ings))
        return out

    def resolve(self, name):
        cands = self.candidates(name)
        if not cands:
            return "unknown", []
        matches = []
        for s, ings in cands:                      # first candidate with an exact registry slug wins
            if s in self.generics:
                matches = [s] + [h for h in self.index.get(_reduce(ings), [])[:6] if h != s]
                break
        if not matches:
            for s, ings in cands:
                hit = self.index.get(_reduce(ings), [])
                if hit:
                    matches = hit[:6]
                    break
        primary = matches[0] if matches else cands[0][0]
        return primary, matches
