#!/usr/bin/env python3
"""Fetch the best US FDA drug label (openFDA) for every generic in the drug database.

Workstream B of the renalcarematters.com Drug Database.

Input   data/drugs/generics.json   {slug: {name, ingredients[], products, categories[]}}
Output  data/drugs/labels/<slug>.json   one file per matched generic
        data/drugs/labels/_missing.json slugs with no matching US label
        data/drugs/labels/_changes.json slugs added or changed in this run (weekly review list)

Two sources:
  --source api   openFDA search API, one paged query per generic (fine for a few hundred)
  --source bulk  openFDA bulk download (all label partitions, streamed); no daily cap
  --source auto  (default) api for <= 200 generics, bulk otherwise

Matching: a label matches a generic when every label substance (openfda.substance_name,
falling back to openfda.generic_name) is one of the generic's ingredients and every
ingredient is present. A substance matches an ingredient when the ingredient's words are
all in the substance name and every extra word is a salt/hydrate word
("amlodipine" ~ "AMLODIPINE BESYLATE", "dapagliflozin" ~ "DAPAGLIFLOZIN PROPANEDIOL").
Biosimilar suffixes ("EPOETIN ALFA-EPBX") do NOT match the reference product's generic.

Ranking: a label whose route matches the PH registrations (data/drugs/registry) first, then
human Rx before OTC. Default --prefer innovator: NDA/BLA, then the lowest NDA/BLA number
(the original reference listed drug rather than a later 505(b)(2) reformulation or a
biosimilar), then the original manufacturer over a repackager, then a true brand over an
authorized generic, then newest effective_time. --prefer recent (the literal brief): newest
effective_time, then NDA/BLA. Recent alone tends to pick repackager copies.
Labels with no openfda block (some biologics) fall back to a single-ingredient match on the
start of spl_product_data_elements; such files carry selection.match = "unindexed-spl".

Incremental: a slug whose stored set_id + effective_time is unchanged is not rewritten.
The section text is copied verbatim from the label; nothing is paraphrased.

Standard library only; uses ijson for streaming in bulk mode when it is installed.
"""
from __future__ import annotations

import argparse
import datetime as dt
import functools
import io
import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.parse
import urllib.request
import zipfile
from pathlib import Path

REPO = Path(__file__).resolve().parents[2]
DEFAULT_GENERICS = REPO / "data" / "drugs" / "generics.json"
DEFAULT_OUT = REPO / "data" / "drugs" / "labels"

API = "https://api.fda.gov/drug/label.json"
DOWNLOAD_MANIFEST = "https://api.fda.gov/download.json"
UA = "RenalCareMattersDrugDB/1.0 (+https://renalcarematters.com)"
MANILA = dt.timezone(dt.timedelta(hours=8))
SCHEMA_VERSION = 1

# Words that may follow (or precede) an ingredient name in an FDA substance name without
# changing the active moiety: counter-ions, esters used as salts, hydrates, forms.
SALT_WORDS = set("""
acetate acetonide anhydrous arginine aspartate benzathine benzoate besylate besilate bicarbonate
bisulfate bitartrate bromide butyrate calcium camsylate carbonate chloride citrate cypionate
decanoate diacetate dihydrate dihydrochloride dimesylate dimaleate dipotassium dipropionate
disodium disoproxil edisylate enanthate erbumine esylate estolate ethanolate ethylsuccinate
fumarate gluceptate gluconate glycinate hcl hemifumarate hemihydrate hemisulfate heptahydrate
hexahydrate hyclate hydrobromide hydrochloride hydrogen hydroxide iodide isethionate lactate
lactobionate lysine magnesium maleate malate mandelate medoxomil megluminate meglumine mesilate
mesylate methylbromide methylsulfate monohydrate monosodium napsylate nitrate oxalate
pamoate pentahydrate phosphate potassium propanediol propionate saccharate salicylate sesquihydrate
sodium stearate succinate sulfate sulphate tartrate tebutate teoclate tetrahydrate tosylate
trifenatate trihydrate trometamol tromethamine valerate xinafoate zinc amorphous crystalline
""".split())

# Philippine/INN names -> US (USAN) names used in openFDA substance names.
INN_TO_USAN = {
    "paracetamol": "acetaminophen", "salbutamol": "albuterol", "chlorphenamine": "chlorpheniramine",
    "glibenclamide": "glyburide", "frusemide": "furosemide", "adrenaline": "epinephrine",
    "noradrenaline": "norepinephrine", "hyoscine": "scopolamine", "lignocaine": "lidocaine",
    "ciclosporin": "cyclosporine", "colecalciferol": "cholecalciferol", "mesalazine": "mesalamine",
    "pethidine": "meperidine", "phytomenadione": "phytonadione", "rifampicin": "rifampin",
    "aciclovir": "acyclovir", "valaciclovir": "valacyclovir", "cefalexin": "cephalexin",
    "cefradine": "cephradine", "isoprenaline": "isoproterenol", "beclometasone": "beclomethasone",
    "thiamazole": "methimazole", "orciprenaline": "metaproterenol", "oestradiol": "estradiol",
    "ethinylestradiol": "ethinyl estradiol", "glyceryl trinitrate": "nitroglycerin",
    "dexamfetamine": "dextroamphetamine", "amfetamine": "amphetamine", "levothyroxine sodium": "levothyroxine",
    "sodium valproate": "valproate", "valproic acid": "valproic acid", "dimeticone": "dimethicone",
    "simeticone": "simethicone", "lactulose": "lactulose", "bendroflumethiazide": "bendroflumethiazide",
    "benzylpenicillin": "penicillin g", "phenoxymethylpenicillin": "penicillin v",
    "flucloxacillin": "flucloxacillin", "co-trimoxazole": "sulfamethoxazole and trimethoprim",
    "cotrimoxazole": "sulfamethoxazole and trimethoprim", "clavulanic acid": "clavulanate",
    "tenofovir disoproxil": "tenofovir disoproxil", "dextromethophan": "dextromethorphan",
    "ipratropium bromide": "ipratropium", "chlorhexidine gluconate": "chlorhexidine",
    "torasemide": "torsemide", "sulfasalazine": "sulfasalazine", "metamizole": "dipyrone",
    "ergocalciferol": "ergocalciferol", "alfacalcidol": "alfacalcidol", "ketoprofen": "ketoprofen",
    "trihexyphenidyl": "trihexyphenidyl", "levonorgestrel": "levonorgestrel", "retinol": "vitamin a",
    "tocopherol": "vitamin e", "insulin isophane human": "insulin isophane human",
}
# Words in a PH ingredient string that are not part of the drug name.
NOISE_WORDS = {"as", "in", "rdna", "dna", "recombinant", "regular", "usp", "bp", "equivalent", "to"}

# US label route -> group; PH dosage-form words -> group (used to prefer a label whose route
# matches what is registered in the Philippines, e.g. oral calcitriol over the topical ointment).
US_ROUTE_GROUP = {
    "ORAL": "oral", "SUBLINGUAL": "oral", "BUCCAL": "oral", "OROPHARYNGEAL": "oral",
    "INTRAVENOUS": "inj", "SUBCUTANEOUS": "inj", "INTRAMUSCULAR": "inj", "INTRATHECAL": "inj",
    "EPIDURAL": "inj", "INTRADERMAL": "inj", "INFILTRATION": "inj", "INTRAPERITONEAL": "inj",
    "INTRA-ARTERIAL": "inj", "INTRAVESICAL": "inj", "PERINEURAL": "inj", "INTRACAVERNOUS": "inj",
    "INTRA-ARTICULAR": "inj", "INTRAVITREAL": "ophth",
    "TOPICAL": "topical", "CUTANEOUS": "topical", "TRANSDERMAL": "transdermal",
    "OPHTHALMIC": "ophth", "AURICULAR (OTIC)": "otic", "NASAL": "nasal",
    "RESPIRATORY (INHALATION)": "inhal", "INHALATION": "inhal", "VAGINAL": "vaginal",
    "RECTAL": "rectal", "DENTAL": "topical", "PERIODONTAL": "topical",
}
PH_FORM_GROUPS = [  # first hit wins, so specific before generic
    ("ophth", r"ophthalmic|\beye\b"), ("otic", r"\botic\b|\bear\b"), ("nasal", r"nasal"),
    ("inhal", r"inhal|nebul|metered|respule|turbuhaler|accuhaler|rotacap|dry powder"),
    ("vaginal", r"vaginal|pessar|ovule"), ("rectal", r"suppositor|rectal|enema"),
    ("transdermal", r"transdermal|\bpatch"),
    ("inj", r"inject|infusion|\bi\.?v\b|\bi\.?m\b|\bs\.?c\b|vial|ampul|lyophili|intravenous|"
            r"subcutaneous|intramuscular|intrathecal|pre-?filled|\bpen\b|intraperitoneal|dialysis"),
    ("topical", r"cream|ointment|\bgel\b|lotion|topical|shampoo|liniment|cutaneous|dusting|"
                r"medicated plaster|scalp|skin|soap|wash\b|mouthwash|gargle|oromucosal|dental|paste"),
    ("oral", r"tablet|capsule|caplet|syrup|suspension|oral|granule|sachet|elixir|lozenge|drops|"
             r"softgel|chewable|powder|solution|emulsion|liquid"),
]
REPACKAGER_HINTS = re.compile(
    r"repack|pd-rx|bryant ranch|proficient rx|quality care|a-s medication|nucare|direct[_ ]?rx|"
    r"preferred pharmaceuticals|aphena|cardinal health|medsource|lake erie medical|henry schein|"
    r"northwind|asclemed|denton pharma|qpharma|golden state medical|american health packaging|"
    r"aidarex|rebel distributors|unit dose services|safecor|contract pharmacy|coupler|advanced rx|"
    r"blenheim|liberty pharmaceuticals|physicians total care|stat rx|readymeds|clinical solutions|"
    r"dispensing solutions|altura|carilion|h\.j\. harkins|keltman|legacy pharmaceutical packaging|"
    r"medvantx|major pharmaceuticals|st\. mary|lifeline|med-health|precision dose|marlex|"
    r"ncs healthcare|remedy|avera mckennan|mckesson|medline|chartwell rx|asclemed|proficient|"
    r"hawaii|nubratori|zydus lifesciences? .*repack|a&z pharm|safecor|direct_rx|quallent|"
    r"henry schein|preferred pharm|bi-coastal|shopko|kaiser|walgreen|cvs|rite aid|target|walmart|"
    r"kroger|meijer|h-e-b|publix|wal-mart|dolgencorp|family dollar|amazon|costco|sam's",
    re.I)

SECTION_FIELDS = [
    "boxed_warning",
    "indications_and_usage",
    "dosage_and_administration",
    "dosage_forms_and_strengths",
    "contraindications",
    "warnings_and_cautions",
    "drug_interactions",
    "adverse_reactions",
    "use_in_specific_populations",
    "pregnancy",
    "lactation",
    "pediatric_use",
    "geriatric_use",
    "overdosage",
    "mechanism_of_action",
    "pharmacokinetics",
]
# label field -> our field, used when the primary field is absent
FALLBACKS = {
    "warnings_and_cautions": ["warnings", "precautions"],
    "lactation": ["nursing_mothers"],
    "pharmacokinetics": ["clinical_pharmacology"],
    "mechanism_of_action": [],
}
META_FIELDS = ["brand_name", "manufacturer_name", "application_number", "route",
               "product_type", "generic_name", "substance_name", "product_ndc", "rxcui"]

RENAL_HEAD = (r"(?:Patients\s+with\s+)?(?:Renal\s+Impairment|Renal\s+Insufficiency|"
              r"Impaired\s+Renal\s+Function|Renal\s+Disease|Kidney\s+Impairment)")
OTHER_POP_HEADS = (r"Hepatic\s+Impairment|Hepatic\s+Insufficiency|Impaired\s+Hepatic|Geriatric|"
                   r"Pediatric|Elderly|Gender|Sex\b|Race\b|Ethnicity|Body\s+Weight|Obesity|Age\b|"
                   r"Drug\s+Interaction|Drug-Drug|Pregnan|Lactation|Nursing|Smok|Heart\s+Failure|"
                   r"Cardiac|Patients\s+with\s+(?!Renal|Kidney|End)")


# --------------------------------------------------------------------------- matching
@functools.lru_cache(maxsize=None)
def _tokens(s: str) -> tuple:
    return tuple(t for t in re.split(r"[^a-z0-9]+", s.lower()) if t)


def tokens(s: str) -> list[str]:
    return list(_tokens(s))


@functools.lru_cache(maxsize=None)
def usan(ingredient: str) -> str:
    s = " " + ingredient.lower().strip() + " "
    for inn, us in INN_TO_USAN.items():
        s = re.sub(r"(?<![a-z])" + re.escape(inn) + r"(?![a-z])", us, s)
    return s.strip()


@functools.lru_cache(maxsize=None)
def ing_tokens(ingredient: str) -> tuple:
    return tuple(t for t in tokens(usan(ingredient)) if t not in NOISE_WORDS and not t.isdigit())


@functools.lru_cache(maxsize=1 << 20)
def substance_matches(ingredient: str, substance: str) -> bool:
    it, st = ing_tokens(ingredient), tokens(substance)
    if not it or not st:
        return False
    iset, sset = set(it), set(st)
    if not iset <= sset:
        return False
    return (sset - iset) <= SALT_WORDS


def split_generic_names(names: list[str]) -> list[str]:
    out: list[str] = []
    for n in names:
        for part in re.split(r",|\s+and\s+|/|\+", n, flags=re.I):
            if part.strip():
                out.append(part.strip())
    return out


def label_substance_sets(label: dict) -> list[list[str]]:
    """Candidate ingredient lists for a label: openfda.substance_name (UNII names), then
    openfda.generic_name. Both are tried because UNII names sometimes drop a word the
    generic name keeps (Epogen: substance "EPOETIN", generic "EPOETIN ALFA")."""
    of = label.get("openfda") or {}
    sets = []
    subs = [x for x in of.get("substance_name") or [] if x.strip()]
    if subs:
        sets.append(subs)
    gen = split_generic_names(of.get("generic_name") or [])
    if gen and gen != subs:
        sets.append(gen)
    return sets


def label_substances(label: dict) -> list[str]:
    sets = label_substance_sets(label)
    return sets[0] if sets else []


def label_matches_any(ingredients: list[str], label: dict) -> bool:
    return any(label_matches(ingredients, subs) for subs in label_substance_sets(label))


@functools.lru_cache(maxsize=None)
def expand_ingredients(ingredients: tuple) -> list[str]:
    return [p for i in ingredients for p in re.split(r"\s+and\s+", usan(i))]


def label_matches(ingredients: list[str], substances: list[str]) -> bool:
    if not substances or not ingredients:
        return False
    # an alias may expand to a combination ("co-trimoxazole")
    ingredients = expand_ingredients(tuple(ingredients))
    # every substance must be one of the ingredients (no extras)
    for s in substances:
        if not any(substance_matches(i, s) for i in ingredients):
            return False
    # every ingredient must be present
    for i in ingredients:
        if not any(substance_matches(i, s) for s in substances):
            return False
    return True


def unindexed_match(ingredient: str, text: str) -> bool:
    words = ing_tokens(ingredient)
    if not words:
        return False
    pat = r"(?<![a-z0-9-])" + r"[\s,]+".join(map(re.escape, words)) + r"(?![a-z0-9]|-[a-z])"
    return re.search(pat, text.lower()) is not None


class Matcher:
    """Inverted index ingredient word -> generic slugs, for scanning the bulk files."""

    def __init__(self, generics: dict):
        self.generics = generics
        self.index: dict[str, set[str]] = {}
        for slug, g in generics.items():
            for ing in g["ingredients"]:
                words = [t for t in ing_tokens(ing) if t not in SALT_WORDS] or ing_tokens(ing)
                for w in words:
                    self.index.setdefault(w, set()).add(slug)
        self.single = {slug: g["ingredients"][0] for slug, g in generics.items()
                       if len(g["ingredients"]) == 1}

    def candidates(self, words) -> set[str]:
        out: set[str] = set()
        for w in words:
            out |= self.index.get(w, set())
        return out

    def fallback(self, label: dict) -> list[str]:
        """Labels with no openfda block (common for some biologics): single-ingredient
        generics whose name opens the SPL product data elements."""
        if (label.get("openfda") or {}).get("substance_name") or (label.get("openfda") or {}).get("generic_name"):
            return []
        head = join_text(label.get("spl_product_data_elements"))[:300]
        if not head:
            return []
        return [slug for slug in self.candidates(tokens(head))
                if slug in self.single and unindexed_match(self.single[slug], head)]

    def match(self, label: dict) -> list[str]:
        sets = label_substance_sets(label)
        if not sets:
            return []
        cands = self.candidates(w for subs in sets for s in subs for w in tokens(s))
        return [slug for slug in cands if label_matches_any(self.generics[slug]["ingredients"], label)]


# --------------------------------------------------------------------------- ranking
def first(v):
    if isinstance(v, list):
        return v[0] if v else ""
    return v or ""


def product_rank(label: dict) -> int:
    pt = " ".join((label.get("openfda") or {}).get("product_type") or []).upper()
    if "PRESCRIPTION" in pt:
        return 0
    if "OTC" in pt:
        return 1
    return 2


def is_innovator(label: dict) -> bool:
    apps = (label.get("openfda") or {}).get("application_number") or []
    return any(a.upper().startswith(("NDA", "BLA")) for a in apps)


def app_number(label: dict) -> int:
    nums = [int(re.sub(r"\D", "", a) or 0) for a in (label.get("openfda") or {}).get("application_number") or []
            if a.upper().startswith(("NDA", "BLA"))]
    return min(nums) if nums else 10**9


def generic_branded(label: dict) -> int:
    """1 when the brand name is just the generic name (authorized generic), 0 for a true brand."""
    of = label.get("openfda") or {}
    b = set(tokens(first(of.get("brand_name")))) - SALT_WORDS
    g = {t for n in of.get("generic_name") or [] for t in tokens(n)} - SALT_WORDS
    return 1 if (not b or b <= g) else 0


def is_repackager(label: dict) -> bool:
    return bool(REPACKAGER_HINTS.search(first((label.get("openfda") or {}).get("manufacturer_name"))))


def label_route_groups(label: dict) -> set[str]:
    return {US_ROUTE_GROUP.get(r.upper(), r.lower()) for r in (label.get("openfda") or {}).get("route") or []}


def route_weight(label: dict, ph_routes: dict | None) -> int:
    if not ph_routes:
        return 0
    return max((ph_routes.get(g, 0) for g in label_route_groups(label)), default=0)


def rank_key(label: dict, prefer: str, ph_routes: dict | None = None):
    """Smaller sorts first. Route match to the PH registrations, then Rx>OTC, then:
    innovator: NDA/BLA, original manufacturer (not a repackager), newest effective_time
               (lowest NDA/BLA number = the original reference product, not a later
               505(b)(2) reformulation or biosimilar)
    recent:    newest effective_time, NDA/BLA (the literal brief)"""
    eff = str(label.get("effective_time") or "0")
    inn = 0 if is_innovator(label) else 1
    rep = 1 if is_repackager(label) else 0
    eff_key = "".join(chr(255 - ord(c)) for c in eff.ljust(8, "0"))  # descending date
    head = (-route_weight(label, ph_routes), product_rank(label))
    if prefer == "innovator":
        return head + (inn, app_number(label), rep, generic_branded(label), eff_key, label.get("id", ""))
    return head + (eff_key, inn, label.get("id", ""))


def is_human(label: dict) -> bool:
    pt = " ".join((label.get("openfda") or {}).get("product_type") or []).upper()
    return (not pt) or "HUMAN" in pt


# --------------------------------------------------------------------------- extraction
def join_text(v) -> str:
    if isinstance(v, list):
        return "\n\n".join(x.strip() for x in v if isinstance(x, str) and x.strip())
    return (v or "").strip() if isinstance(v, str) else ""


def extract_renal_from_populations(text: str) -> str:
    # PLR labels: "8.6 Renal Impairment ..." up to the next "8.x " heading
    m = re.search(r"(?:^|\s)(8\.\d+)\s+" + RENAL_HEAD, text)
    if m:
        start = m.start(1)
        nxt = re.search(r"\s8\.\d+\s+[A-Z]|\s10\s+OVERDOSAGE", text[m.end():])
        end = m.end() + nxt.start() if nxt else len(text)
        return text[start:end].strip()
    return ""


def extract_renal_from_pk(text: str) -> str:
    # A title-case heading inside clinical pharmacology / pharmacokinetics.
    m = re.search(r"(?:^|\s)(" + RENAL_HEAD + r")(?!\s*\(\d)(?=\s*[:.\-–—]|\s+[A-Z(])", text)
    if not m:
        return ""
    start = m.start(1)
    rest = text[m.end(1):]
    nxt = re.search(r"(?:[.:)\]]\s+|\n\s*|\s{2,})(?:" + OTHER_POP_HEADS + r")|\s1[2-9]\.\d+\s+[A-Z]|\s1[3-9]\s+[A-Z]{3}",
                    rest)
    end = m.end(1) + (nxt.start() + 1 if nxt else min(len(rest), 4000))
    return text[start:end].strip()


def extract_renal_from_dosing(text: str) -> str:
    """PLR: every "2.x ..." subsection whose heading mentions renal function, kidney, eGFR,
    creatinine clearance or dialysis (but not "Normal Renal Function"), verbatim and in order."""
    heads = list(re.finditer(r"(?:^|\s)(2\.\d+)\s+(?=[A-Z])", text))
    found = []
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(text)
        dfm = re.search(r"\s3\s+DOSAGE FORMS", text[h.start():end])
        if dfm:
            end = h.start() + dfm.start()
        chunk = text[h.start(1):end].strip()
        title = re.sub(r"^2\.\d+\s+", "", chunk)[:110]
        title = title[:6] + re.split(r"(?<=[a-z0-9)])\s+(?:The|For|Administer|No|Reduce|Adjust|Avoid|Initiate|"
                                     r"If|When|Before|Measure|Assess|Monitor|A|An|In|It|This|Because)\s",
                                     title[6:])[0]
        if (re.search(r"Renal|Kidney|eGFR|Creatinine Clearance|Dialysis|CrCl|Hemodialysis", title)
                and not re.search(r"Normal Renal", title)):
            found.append(chunk)
    if found:
        return "\n\n".join(found)
    if heads:  # PLR label without a renal dosing subsection
        return ""
    return extract_renal_from_pk(text)


def build_record(slug: str, g: dict, label: dict, n_candidates: int, prefer: str,
                 match: str = "openfda", ph_routes: dict | None = None) -> dict:
    of = label.get("openfda") or {}
    sections: dict[str, str] = {}
    section_sources: dict[str, str] = {}
    for f in SECTION_FIELDS:
        txt = join_text(label.get(f))
        src = f
        if not txt:
            for alt in FALLBACKS.get(f, []):
                txt = join_text(label.get(alt))
                if txt:
                    src = alt
                    break
        if txt:
            sections[f] = txt
            if src != f:
                section_sources[f] = src

    renal: list[dict] = []
    if join_text(label.get("renal_impairment")):
        renal.append({"source": "renal_impairment", "text": join_text(label.get("renal_impairment"))})
    pop = join_text(label.get("use_in_specific_populations"))
    if pop:
        t = extract_renal_from_populations(pop)
        if t:
            renal.append({"source": "use_in_specific_populations", "text": t})
    t = extract_renal_from_dosing(join_text(label.get("dosage_and_administration")))
    if t:
        renal.insert(0, {"source": "dosage_and_administration", "text": t})
    for f in ("pharmacokinetics", "clinical_pharmacology"):
        t = extract_renal_from_pk(join_text(label.get(f)))
        if t and not any(t in r["text"] or r["text"] in t for r in renal):
            renal.append({"source": f, "text": t})
            break
    if renal:
        sections["renal_impairment"] = "\n\n".join(r["text"] for r in renal)

    set_id = label.get("set_id", "")
    meta = {
        "set_id": set_id,
        "id": label.get("id", ""),
        "version": label.get("version", ""),
        "effective_time": label.get("effective_time", ""),
        "brand_name": first(of.get("brand_name")),
        "manufacturer_name": first(of.get("manufacturer_name")),
        "application_number": first(of.get("application_number")),
        "route": of.get("route") or [],
        "product_type": first(of.get("product_type")),
        "generic_name": first(of.get("generic_name")),
        "substance_name": of.get("substance_name") or [],
        "innovator": is_innovator(label),
    }
    return {
        "schema_version": SCHEMA_VERSION,
        "slug": slug,
        "name": g.get("name", slug),
        "ingredients": g["ingredients"],
        "source": {
            "publisher": "U.S. Food and Drug Administration",
            "via": "openFDA drug label endpoint",
            "dailymed_url": f"https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid={set_id}" if set_id else "",
            "api_url": f"{API}?search=set_id:%22{set_id}%22" if set_id else "",
            "license_note": "U.S. government work; label text reproduced verbatim.",
        },
        "selection": {"candidates": n_candidates, "rule": prefer, "match": match,
                      "ph_routes": ph_routes or {}, "repackager": is_repackager(label)},
        "label": meta,
        "sections": sections,
        "section_sources": section_sources,
        "renal_impairment_sources": renal,
        "fetched_at": dt.datetime.now(MANILA).isoformat(timespec="seconds"),
    }


# --------------------------------------------------------------------------- network
def http_get(url: str, retries: int = 5, timeout: int = 120) -> bytes:
    delay = 2.0
    for attempt in range(retries):
        req = urllib.request.Request(url, headers={"User-Agent": UA})
        try:
            with urllib.request.urlopen(req, timeout=timeout) as r:
                return r.read()
        except urllib.error.HTTPError as e:
            if e.code == 404:
                return b""
            if e.code in (429, 500, 502, 503, 504) and attempt < retries - 1:
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


class Api:
    def __init__(self, key: str | None, min_interval: float):
        self.key = key
        self.min_interval = min_interval
        self.last = 0.0
        self.requests = 0

    def get(self, params: dict) -> dict:
        wait = self.min_interval - (time.time() - self.last)
        if wait > 0:
            time.sleep(wait)
        if self.key:
            params = {**params, "api_key": self.key}
        url = API + "?" + urllib.parse.urlencode(params, safe=':+"()')
        self.last = time.time()
        self.requests += 1
        raw = http_get(url)
        return json.loads(raw) if raw else {}


class Collector:
    """Keeps the best label per slug (indexed openfda match first, unindexed fallback second),
    the candidate counts, and a few near-miss substance sets for diagnosing misses."""

    def __init__(self, generics: dict, prefer: str, ph_routes: dict):
        self.generics, self.prefer, self.ph_routes = generics, prefer, ph_routes
        self.best: dict[str, dict] = {}
        self.best_fb: dict[str, dict] = {}
        self.counts: dict[str, int] = {s: 0 for s in generics}
        self.counts_fb: dict[str, int] = {s: 0 for s in generics}
        self.near: dict[str, set] = {}
        self.errors: set[str] = set()

    def _better(self, slug, a, b) -> bool:
        r = self.ph_routes.get(slug)
        return rank_key(a, self.prefer, r) < rank_key(b, self.prefer, r)

    def add(self, slug: str, label: dict, fallback: bool = False):
        store, counts = (self.best_fb, self.counts_fb) if fallback else (self.best, self.counts)
        counts[slug] += 1
        cur = store.get(slug)
        if cur is None or self._better(slug, label, cur):
            store[slug] = label

    def near_miss(self, slug: str, label: dict):
        s = self.near.setdefault(slug, set())
        if len(s) < 8:
            subs = label_substances(label)
            s.add(" + ".join(subs) if subs else "(no openfda) " + join_text(label.get("spl_product_data_elements"))[:80])

    def result(self, slug: str):
        if slug in self.best:
            return self.best[slug], "openfda", self.counts[slug]
        if slug in self.best_fb:
            return self.best_fb[slug], "unindexed-spl", self.counts_fb[slug]
        return None, None, 0


def api_candidates(api: Api, g: dict, max_pages: int) -> list[dict]:
    clauses = []
    for ing in g["ingredients"]:
        for part in re.split(r"\s+and\s+", usan(ing)):
            words = [t for t in ing_tokens(part) if t not in SALT_WORDS] or ing_tokens(part)
            phrase = " ".join(words)
            clauses.append(f'(openfda.substance_name:"{phrase}"+openfda.generic_name:"{phrase}")')
    out: list[dict] = []
    for page in range(max_pages):
        data = api.get({"search": "+AND+".join(clauses), "limit": 100, "skip": page * 100})
        res = data.get("results") or []
        out.extend(res)
        total = (data.get("meta") or {}).get("results", {}).get("total", 0)
        if len(res) < 100 or (page + 1) * 100 >= total:
            break
    return out


def api_fallback(api: Api, g: dict) -> list[dict]:
    """Unindexed labels (no openfda block): search the SPL product data elements."""
    if len(g["ingredients"]) != 1:
        return []
    phrase = " ".join(ing_tokens(g["ingredients"][0]))
    data = api.get({"search": f'spl_product_data_elements:"{phrase}"+AND+_missing_:openfda', "limit": 100})
    return data.get("results") or []


def run_api(generics: dict, col: Collector, args):
    api = Api(os.environ.get("OPENFDA_API_KEY") or None, args.min_interval)
    for n, (slug, g) in enumerate(sorted(generics.items()), 1):
        try:
            labels = api_candidates(api, g, args.max_pages)
            for l in labels:
                if is_human(l) and label_matches_any(g["ingredients"], l):
                    col.add(slug, l)
                else:
                    col.near_miss(slug, l)
            if slug not in col.best:
                for l in api_fallback(api, g):
                    head = join_text(l.get("spl_product_data_elements"))[:300]
                    if is_human(l) and unindexed_match(g["ingredients"][0], head):
                        col.add(slug, l, fallback=True)
                    else:
                        col.near_miss(slug, l)
        except Exception as e:  # keep going; record as a miss with the reason
            print(f"[{n}/{len(generics)}] {slug}: ERROR {e}", file=sys.stderr)
            col.errors.add(slug)
            continue
        _, how, c = col.result(slug)
        print(f"[{n}/{len(generics)}] {slug}: {len(labels)} returned, {c} matched ({how or 'none'})")
    print(f"openFDA requests: {api.requests}")


def iter_bulk_labels(path: Path):
    with zipfile.ZipFile(path) as z:
        for name in z.namelist():
            if not name.endswith(".json"):
                continue
            with z.open(name) as fh:
                try:
                    import ijson  # type: ignore
                except ImportError:
                    ijson = None
                if ijson:
                    yield from ijson.items(fh, "results.item", use_float=True)
                else:
                    data = json.load(io.TextIOWrapper(fh, encoding="utf-8"))
                    yield from data.get("results", [])
                    del data


def run_bulk(generics: dict, col: Collector, args):
    manifest = json.loads(http_get(DOWNLOAD_MANIFEST))
    meta = manifest["results"]["drug"]["label"]
    parts = meta["partitions"]
    print(f"bulk: {len(parts)} partitions, export date {meta.get('export_date')}", flush=True)
    matcher = Matcher(generics)
    seen = 0
    with tempfile.TemporaryDirectory() as td:
        for i, p in enumerate(parts, 1):
            dest = Path(td) / f"part{i}.zip"
            t0 = time.time()
            for attempt in range(4):
                try:
                    req = urllib.request.Request(p["file"], headers={"User-Agent": UA})
                    with urllib.request.urlopen(req, timeout=600) as r, open(dest, "wb") as out:
                        while chunk := r.read(1 << 20):
                            out.write(chunk)
                    break
                except Exception as e:
                    if attempt == 3:
                        raise
                    print(f"  retry part {i}: {e}", flush=True)
                    time.sleep(15 * (attempt + 1))
            for label in iter_bulk_labels(dest):
                seen += 1
                if not is_human(label):
                    continue
                hits = matcher.match(label)
                for slug in hits:
                    col.add(slug, label)
                if not hits:
                    for slug in matcher.fallback(label):
                        col.add(slug, label, fallback=True)
            dest.unlink()
            print(f"bulk part {i}/{len(parts)} done in {time.time() - t0:.0f}s; {seen} labels scanned, "
                  f"{len(col.best)} generics matched (+{len(set(col.best_fb) - set(col.best))} unindexed)",
                  flush=True)


# --------------------------------------------------------------------------- PH routes
def load_ph_routes(registry_dir: Path) -> dict[str, dict[str, int]]:
    """slug -> {route group: number of PH products}, from data/drugs/registry/*.json."""
    out: dict[str, dict[str, int]] = {}
    files = sorted(registry_dir.glob("*.json")) if registry_dir.is_dir() else []
    single = registry_dir.with_suffix(".json")
    if not files and single.exists():
        files = [single]
    for f in files:
        try:
            rows = json.loads(f.read_text(encoding="utf-8"))
        except Exception:
            continue
        for p in rows if isinstance(rows, list) else []:
            slug, form = p.get("generic_slug"), (p.get("dosage_strength_form") or "").lower()
            if not slug or not form:
                continue
            for grp, pat in PH_FORM_GROUPS:
                if re.search(pat, form):
                    d = out.setdefault(slug, {})
                    d[grp] = d.get(grp, 0) + 1
                    break
    return out


# --------------------------------------------------------------------------- output
def write_if_changed(path: Path, obj: dict, ignore: tuple[str, ...] = ()) -> bool:
    if path.exists():
        try:
            old = json.loads(path.read_text(encoding="utf-8"))
            strip = lambda d: {k: v for k, v in d.items() if k not in ignore}
            if strip(old) == strip(obj):
                return False
        except Exception:
            pass
    path.write_text(json.dumps(obj, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    return True


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--generics-file", default=str(DEFAULT_GENERICS))
    ap.add_argument("--registry-dir", default=str(REPO / "data" / "drugs" / "registry"),
                    help="PH registry (for dosage-form routes); optional")
    ap.add_argument("--out-dir", default=str(DEFAULT_OUT))
    ap.add_argument("--source", choices=["auto", "api", "bulk"], default="auto")
    ap.add_argument("--prefer", choices=["innovator", "recent"], default="innovator",
                    help="after route match and Rx>OTC: innovator = NDA/BLA, non-repackager, newest; "
                         "recent = newest effective_time, then NDA/BLA")
    ap.add_argument("--only", nargs="*", help="limit to these slugs")
    ap.add_argument("--force", action="store_true", help="rewrite every file even if unchanged")
    ap.add_argument("--max-pages", type=int, default=10, help="API pages (x100) per generic")
    ap.add_argument("--min-interval", type=float, default=0.3, help="seconds between API calls")
    args = ap.parse_args()

    gpath = Path(args.generics_file)
    if not gpath.is_absolute():
        gpath = (Path.cwd() / gpath).resolve()
    generics = json.loads(gpath.read_text(encoding="utf-8"))
    generics = {k: v for k, v in generics.items() if v.get("ingredients")}
    if args.only:
        generics = {k: v for k, v in generics.items() if k in set(args.only)}
    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)
    ph_routes = load_ph_routes(Path(args.registry_dir))

    source = args.source
    if source == "auto":
        source = "api" if len(generics) <= 200 else "bulk"
    print(f"{len(generics)} generics from {gpath.name}; source={source}; prefer={args.prefer}; "
          f"PH routes known for {sum(1 for s in generics if s in ph_routes)}", flush=True)
    col = Collector(generics, args.prefer, ph_routes)
    (run_api if source == "api" else run_bulk)(generics, col, args)

    added, changed, unchanged, missing = [], [], 0, []
    stats = {"openfda": 0, "unindexed-spl": 0, "innovator": 0, "repackager": 0}
    for slug, g in sorted(generics.items()):
        label, how, n_cand = col.result(slug)
        if label is None:
            m = {"slug": slug, "name": g.get("name", slug), "ingredients": g["ingredients"],
                 "reason": "fetch error" if slug in col.errors else "no matching US FDA human label"}
            if col.near.get(slug):
                m["near_misses"] = sorted(col.near[slug])
            missing.append(m)
            continue
        stats[how] += 1
        stats["innovator"] += is_innovator(label)
        stats["repackager"] += is_repackager(label)
        path = out_dir / f"{slug}.json"
        old_meta = None
        if path.exists():
            try:
                old_meta = json.loads(path.read_text(encoding="utf-8")).get("label", {})
            except Exception:
                old_meta = None
        new_key = (label.get("set_id", ""), label.get("effective_time", ""))
        old_key = (old_meta.get("set_id"), old_meta.get("effective_time")) if old_meta else None
        if old_key == new_key and not args.force:
            unchanged += 1
            continue
        rec = build_record(slug, g, label, n_cand, args.prefer, how, ph_routes.get(slug))
        path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        entry = {"slug": slug, "name": g.get("name", slug), "brand_name": rec["label"]["brand_name"],
                 "application_number": rec["label"]["application_number"],
                 "set_id": new_key[0], "effective_time": new_key[1],
                 "dailymed_url": rec["source"]["dailymed_url"]}
        if old_key is None:
            added.append(entry)
        elif old_key != new_key:
            entry["previous"] = {"set_id": old_key[0], "effective_time": old_key[1]}
            changed.append(entry)
        # a forced rewrite of an unchanged label is not a review item

    now = dt.datetime.now(MANILA).isoformat(timespec="seconds")
    mpath = out_dir / "_missing.json"
    if args.only and mpath.exists():  # subset run: keep earlier misses for other slugs
        prev = json.loads(mpath.read_text(encoding="utf-8")).get("missing", [])
        missing = sorted([m for m in prev if m["slug"] not in generics] + missing, key=lambda m: m["slug"])
    write_if_changed(mpath, {"generated_at": now, "generics_file": gpath.name, "count": len(missing),
                             "missing": missing}, ignore=("generated_at",))
    write_if_changed(out_dir / "_changes.json", {
        "generated_at": now,
        "note": "US FDA labels added or changed in the latest run; for Dr. Rivero's weekly review.",
        "source": source, "added": added, "changed": changed,
    }, ignore=("generated_at",))

    total = len(generics)
    hits = total - len(missing)
    print(f"matched {hits}/{total} ({100 * hits / max(total, 1):.1f}%) {stats}; added {len(added)}, "
          f"changed {len(changed)}, unchanged {unchanged}, missing {len(missing)}")
    for m in missing[:60]:
        print(f"  missing: {m['slug']} ({m['reason']}) {m.get('near_misses', [])[:3]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
