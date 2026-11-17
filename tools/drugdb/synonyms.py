#!/usr/bin/env python3
"""
synonyms.py — nonproprietary-name synonyms for the Drug Database (Nov 2026).

One table of well-established names for the same molecule under different naming systems:
international nonproprietary names (INN), US adopted names (USAN), British approved names (BAN,
including former BANs harmonized to the INN), and plain chemical descriptions. Brand names are
never listed here (they are already searchable from the registry).

Used by generate_drug_pages.py for
  * index search  — "acetaminophen" finds Paracetamol and every combination that contains it;
  * page display  — "Also known as: acetaminophen (US name)" under the generic title, JSON-LD
                    alternateName and meta keywords;
  * component cross-reference — ingredient name -> single-agent page slug (Task B pages).

Table format
  GROUPS:  each group is one molecule; a list of (name, systems). systems is a space-separated
           subset of SYSTEMS keys. An empty systems string marks a lookup-only spelling (salt form,
           punctuation variant): it is matched and searchable but never displayed.
  MISSPELLINGS: {misspelling or misnomer: a name in GROUPS}. Search-only; never displayed.
           (e.g. "ferrous sucrose" is a misnomer for iron sucrose, which is ferric iron.)
  COMBOS:  names for fixed-dose combinations (co-trimoxazole, co-amoxiclav, ...), keyed by the set
           of component names.

Never map different molecules together: sucroferric oxyhydroxide (a phosphate binder) is NOT iron
sucrose; hyoscine butylbromide is NOT hyoscine (scopolamine) hydrobromide.

  python3 tools/drugdb/synonyms.py            # print the table summary and a self-check
"""
from __future__ import annotations

import re
import unicodedata

SYSTEMS = {
    "inn": "international nonproprietary name",
    "usan": "US name",
    "ban": "British name",
    "fban": "former British name",
    "chem": "chemical description",
}

GROUPS: list[list[tuple[str, str]]] = [
    # ── analgesics, antipyretics, NSAIDs
    [("paracetamol", "inn ban"), ("acetaminophen", "usan")],
    [("aspirin", "ban usan"), ("acetylsalicylic acid", "inn")],
    [("metamizole", "inn"), ("metamizole sodium", ""), ("dipyrone", "usan ban")],
    [("indometacin", "inn ban"), ("indomethacin", "usan")],
    [("pethidine", "inn ban"), ("meperidine", "usan")],
    # ── respiratory
    [("salbutamol", "inn ban"), ("albuterol", "usan")],
    [("levosalbutamol", "inn"), ("levalbuterol", "usan")],
    [("formoterol", "inn usan ban"), ("eformoterol", "fban")],
    [("beclometasone", "inn ban"), ("beclomethasone", "usan")],
    [("guaifenesin", "inn usan ban"), ("guaiphenesin", "fban")],
    [("carbocisteine", "inn ban"), ("carbocysteine", "usan")],
    [("acetylcysteine", "inn usan ban")],
    [("cromolyn", "usan"), ("cromolyn sodium", ""), ("sodium cromoglicate", "ban"), ("cromoglicic acid", "inn"),
     ("sodium cromoglycate", "fban"), ("cromoglicate", ""), ("cromoglycate", "")],
    [("glycopyrronium bromide", "inn ban"), ("glycopyrronium", ""), ("glycopyrrolate", "usan")],
    # ── antihistamines, antiemetics, antispasmodics
    [("chlorphenamine", "inn ban"), ("chlorpheniramine", "usan")],
    [("dexchlorphenamine", "inn"), ("dexchlorpheniramine", "usan")],
    [("meclozine", "inn ban"), ("meclizine", "usan")],
    [("alimemazine", "inn ban"), ("trimeprazine", "usan")],
    [("levomepromazine", "inn ban"), ("methotrimeprazine", "usan")],
    [("hyoscine", "ban"), ("scopolamine", "usan"), ("hyoscine hydrobromide", ""), ("scopolamine hydrobromide", "")],
    [("hyoscine butylbromide", "ban"), ("butylscopolamine bromide", "inn"), ("hyoscine n butylbromide", ""),
     ("hyoscine n butyl bromide", ""), ("hyoscine butyl bromide", ""), ("butylscopolamine", "")],
    [("dicycloverine", "inn ban"), ("dicyclomine", "usan")],
    [("mesalazine", "inn ban"), ("mesalamine", "usan")],
    [("sulfasalazine", "inn usan"), ("sulphasalazine", "fban")],
    [("ursodeoxycholic acid", "inn ban"), ("ursodiol", "usan")],
    [("dimeticone", "inn ban"), ("dimethicone", "usan")],
    [("simeticone", "inn ban"), ("simethicone", "usan")],
    [("carmellose", "inn ban"), ("carboxymethylcellulose", "chem")],
    [("oxetacaine", "inn"), ("oxethazaine", "usan")],
    # ── cardiovascular, kidney, diuretics
    [("furosemide", "inn usan ban"), ("frusemide", "fban")],
    [("torasemide", "inn ban"), ("torsemide", "usan")],
    [("chlortalidone", "inn ban"), ("chlorthalidone", "usan")],
    [("bendroflumethiazide", "inn usan ban"), ("bendrofluazide", "fban")],
    [("epinephrine", "inn usan"), ("adrenaline", "ban")],
    [("norepinephrine", "inn usan"), ("noradrenaline", "ban")],
    [("isoprenaline", "inn ban"), ("isoproterenol", "usan")],
    [("glyceryl trinitrate", "ban"), ("nitroglycerin", "usan")],
    [("pentoxifylline", "inn usan"), ("oxpentifylline", "fban")],
    [("deferoxamine", "inn usan"), ("desferrioxamine", "ban")],
    # ── anesthesia
    [("lidocaine", "inn usan ban"), ("lignocaine", "fban")],
    [("tetracaine", "inn usan"), ("amethocaine", "fban")],
    [("thiopental", "inn usan"), ("thiopentone", "fban")],
    [("suxamethonium", "inn ban"), ("succinylcholine", "usan"), ("suxamethonium chloride", ""), ("succinylcholine chloride", "")],
    # ── endocrine, metabolic, women's health
    [("glibenclamide", "inn ban"), ("glyburide", "usan")],
    [("levothyroxine", "inn usan"), ("levothyroxine sodium", ""), ("thyroxine", "fban"), ("thyroxine sodium", "")],
    [("thiamazole", "inn"), ("methimazole", "usan")],
    [("estradiol", "inn usan ban"), ("oestradiol", "fban")],
    [("ethinylestradiol", "inn ban"), ("ethinyl estradiol", "usan"), ("ethinyloestradiol", "")],
    [("norethisterone", "inn ban"), ("norethindrone", "usan")],
    [("clomifene", "inn ban"), ("clomiphene", "usan"), ("clomifene citrate", ""), ("clomiphene citrate", "")],
    [("dexamfetamine", "inn ban"), ("dextroamphetamine", "usan")],
    [("leuprorelin", "inn ban"), ("leuprolide", "usan")],
    [("ergometrine", "inn ban"), ("ergonovine", "usan")],
    [("methylergometrine", "inn"), ("methylergonovine", "usan")],
    [("colecalciferol", "inn ban"), ("cholecalciferol", "usan")],
    [("phytomenadione", "inn ban"), ("phytonadione", "usan")],
    [("etamsylate", "inn"), ("ethamsylate", "ban")],
    # ── anti-infectives
    [("rifampicin", "inn ban"), ("rifampin", "usan")],
    [("aciclovir", "inn ban"), ("acyclovir", "usan")],
    [("valaciclovir", "inn ban"), ("valacyclovir", "usan")],
    [("cefalexin", "inn ban"), ("cephalexin", "usan")],
    [("cefradine", "inn ban"), ("cephradine", "usan")],
    [("cefazolin", "inn usan"), ("cephazolin", "fban")],
    [("cefalotin", "inn"), ("cephalothin", "usan")],
    [("amoxicillin", "inn usan ban"), ("amoxycillin", "fban")],
    [("flucloxacillin", "inn ban"), ("floxacillin", "usan")],
    [("benzylpenicillin", "inn ban"), ("penicillin g", "usan")],
    [("phenoxymethylpenicillin", "inn ban"), ("penicillin v", "usan")],
    [("benzathine benzylpenicillin", "inn ban"), ("penicillin g benzathine", "usan")],
    [("procaine benzylpenicillin", "inn ban"), ("penicillin g procaine", "usan")],
    [("sulfamethoxazole", "inn usan"), ("sulphamethoxazole", "fban")],
    [("clavulanic acid", "inn ban"), ("clavulanate potassium", "usan"), ("potassium clavulanate", ""), ("clavulanate", "")],
    [("ciclosporin", "inn ban"), ("cyclosporine", "usan")],
    # ── oncology, immunology, hematology
    [("hydroxycarbamide", "inn ban"), ("hydroxyurea", "usan")],
    [("calcium folinate", "inn ban"), ("leucovorin calcium", "usan"), ("leucovorin", ""), ("folinic acid", "chem")],
    [("busulfan", "inn usan"), ("busulphan", "fban")],
    [("tioguanine", "inn"), ("thioguanine", "usan")],
    # ── neurology, psychiatry
    [("trihexyphenidyl", "inn usan"), ("benzhexol", "fban")],
    [("phenobarbital", "inn usan"), ("phenobarbitone", "fban")],
    [("dosulepin", "inn ban"), ("dothiepin", "fban")],
    # ── parenteral iron (kidney care). Each is a different product: never merge them.
    [("iron sucrose", "usan"), ("iron saccharate", "chem"), ("ferric hydroxide sucrose complex", "chem"),
     ("iron iii hydroxide sucrose complex", "")],
    [("ferric carboxymaltose", ""), ("iron carboxymaltose", "")],
    [("ferric derisomaltose", ""), ("iron isomaltoside", ""), ("iron isomaltoside 1000", "")],
    [("sodium ferric gluconate complex", ""), ("ferric sodium gluconate complex", ""), ("sodium ferric gluconate", "")],
    [("iron dextran", "")],
    [("ferumoxytol", "")],
    [("sucroferric oxyhydroxide", "")],   # phosphate binder; listed only so nothing else can claim it
]

# Search-only misspellings / misnomers -> a name in GROUPS. Never displayed as a synonym.
MISSPELLINGS = {
    "ferrous sucrose": "iron sucrose",            # misnomer: iron sucrose is ferric (Fe3+) iron
    "iron sucrose complex": "iron sucrose",
    "scopolamine butylbromide": "hyoscine butylbromide",
    "n acetylcysteine": "acetylcysteine",
    "l thyroxine": "levothyroxine",
}

# Fixed-dose combination names: (component names, [(name, systems)], [search-only names])
COMBOS: list[tuple[tuple[str, ...], list[tuple[str, str]], list[str]]] = [
    (("sulfamethoxazole", "trimethoprim"), [("co-trimoxazole", "ban")],
     ["cotrimoxazole", "trimethoprim sulfamethoxazole", "tmp smx", "smx tmp"]),
    (("amoxicillin", "clavulanic acid"), [("co-amoxiclav", "ban"), ("amoxicillin and clavulanate potassium", "usan")],
     ["amoxicillin clavulanate", "amoxiclav", "co amoxiclav"]),
    (("codeine", "paracetamol"), [("co-codamol", "ban")], []),
    (("carbidopa", "levodopa"), [("co-careldopa", "ban")], []),
    (("benserazide", "levodopa"), [("co-beneldopa", "ban")], []),
    (("amiloride", "hydrochlorothiazide"), [("co-amilozide", "ban")], []),
    (("atenolol", "chlortalidone"), [("co-tenidone", "ban")], []),
    (("ethambutol", "isoniazid", "pyrazinamide", "rifampicin"), [], ["hrze", "rhze"]),
    (("isoniazid", "pyrazinamide", "rifampicin"), [], ["hrz", "rhz"]),
]

_SALT = {"hydrochloride", "hcl", "hc1", "sodium", "potassium", "sulfate", "sulphate", "citrate", "maleate", "malaeate",
         "besilate", "besylate", "mesylate", "mesilate", "tartrate", "bitartrate", "fumarate", "hydrobromide",
         "monohydrate", "dihydrate", "trihydrate", "hemihydrate", "anhydrous", "acetate", "phosphate", "succinate",
         "dipotassium", "disodium", "micronized", "usp", "bp"}


def norm(s: str) -> str:
    s = unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode().lower()
    return re.sub(r"[^a-z0-9]+", " ", s).strip()


# a name that is only a mineral after salt removal keeps its salt ("magnesium sulfate" is not "magnesium")
_MINERAL = {"magnesium", "zinc", "ferrous", "ferric", "iron", "calcium", "potassium", "sodium", "copper", "manganese",
            "lithium", "aluminum", "aluminium", "barium", "chromium", "selenium", "cupric", "strontium", "silver"}


def _strip(s: str) -> str:
    """'Chlorphenamine maleate (as ...)' -> 'chlorphenamine'; leading-salt and mineral names are kept."""
    s = re.sub(r"\(.*?\)", " ", (s or "").lower())
    s = re.sub(r"\bas\s+\w+.*$", " ", s)
    full = norm(s).split()
    w = list(full)
    while len(w) > 1 and w[-1] in _SALT:
        w.pop()
    if len(w) == 1 and w[0] in _MINERAL:
        w = full
    return " ".join(w)


def _compact(s: str) -> str:
    return re.sub(r"\bn\b", "", norm(s)).replace(" ", "")


_INDEX: dict[str, int] = {}
for _gi, _grp in enumerate(GROUPS):
    for _n, _ in _grp:
        k = norm(_n)
        if k in _INDEX and _INDEX[k] != _gi:
            raise ValueError(f"synonym {_n!r} is in two groups")
        _INDEX[k] = _gi
for _m, _t in MISSPELLINGS.items():
    if norm(_m) in _INDEX:
        raise ValueError(f"misspelling {_m!r} is also a listed name")


def group_of(name: str) -> int | None:
    """Group index of an ingredient name (exact, then with trailing salt words and parentheses removed)."""
    for k in (norm(name), _strip(name)):
        if k in _INDEX:
            return _INDEX[k]
    return None


def canonical(name: str) -> str:
    """Normalized key that is the same for every name of one molecule (first name of its group)."""
    gi = group_of(name)
    return norm(GROUPS[gi][0][0]) if gi is not None else _strip(name)


def label_of(systems: str) -> str:
    return " and ".join(SYSTEMS[s] for s in systems.split())


def _combo(ingredients) -> tuple | None:
    key = frozenset(canonical(i) for i in ingredients)
    for comps, names, search in COMBOS:
        if frozenset(canonical(c) for c in comps) == key:
            return names, search
    return None


def display_synonyms(ingredients: list[str], page_name: str = "", own: list[str] | None = None) -> list[dict]:
    """Displayable names for a generic page: [{"name", "label", "for"}] ("for" = component, combos only).
    own: the page's own ingredient names when `ingredients` come from another page (variant spellings)."""
    own = ingredients if own is None else own
    if len(ingredients) > 1:      # a combination's component names are never its synonyms
        own = list(own) + list(ingredients)
    out, seen = [], {_compact(page_name)} | {_compact(i) for i in own} | {_compact(_strip(i)) for i in own}
    c = _combo(ingredients) if len(ingredients) > 1 else None
    for n, systems in (c[0] if c else []):
        if _compact(n) not in seen:
            seen.add(_compact(n))
            out.append({"name": n, "label": label_of(systems), "for": ""})
    for ing in ingredients:
        gi = group_of(ing)
        if gi is None:
            continue
        for n, systems in GROUPS[gi]:
            if systems and _compact(n) not in seen:
                seen.add(_compact(n))
                out.append({"name": n, "label": label_of(systems), "for": ing if len(ingredients) > 1 else ""})
    return out


def search_terms(ingredients: list[str], page_name: str = "") -> dict:
    """{"own": names of this exact product, "ing": names of its components (combos), "miss": search-only}."""
    skip = {norm(page_name)} | {norm(i) for i in ingredients}
    own, ing_terms, miss = [], [], []
    single = len(ingredients) == 1
    c = _combo(ingredients) if len(ingredients) > 1 else None
    if c:
        own += [n for n, _ in c[0]]
        miss += c[1]
    for ing in ingredients:
        gi = group_of(ing)
        if gi is not None:
            (own if single else ing_terms).extend(n for n, _ in GROUPS[gi])
            names = {norm(n) for n, _ in GROUPS[gi]}
            miss += [m for m, t in MISSPELLINGS.items() if norm(t) in names]
    dedup = lambda xs: [x for x in dict.fromkeys(xs) if norm(x) not in skip]
    return {"own": dedup(own), "ing": dedup(ing_terms), "miss": dedup(miss)}


def _selfcheck():
    assert group_of("iron sucrose") != group_of("sucroferric oxyhydroxide")
    assert group_of("hyoscine butylbromide") != group_of("hyoscine")
    assert group_of("Hyoscine-N-Butylbromide") == group_of("hyoscine butylbromide")
    assert group_of("chlorphenamine maleate") == group_of("chlorpheniramine")
    assert group_of("hyoscine hydrobromide") == group_of("scopolamine")
    assert "ferrous sucrose" not in [d["name"] for d in display_synonyms(["iron sucrose"], "Iron sucrose")]
    assert "ferrous sucrose" in search_terms(["iron sucrose"])["miss"]
    assert not search_terms(["sucroferric oxyhydroxide"])["miss"]
    assert canonical("magnesium sulfate") != canonical("magnesium")
    assert display_synonyms(["paracetamol"], "Paracetamol") == [{"name": "acetaminophen", "label": "US name", "for": ""}]


if __name__ == "__main__":
    _selfcheck()
    n_names = sum(len(g) for g in GROUPS)
    shown = sum(1 for g in GROUPS for _, s in g if s)
    print(f"{len(GROUPS)} molecule groups, {n_names} names ({shown} displayable), {len(MISSPELLINGS)} search-only "
          f"misspellings, {len(COMBOS)} combination entries. Self-check OK.")
