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
a label whose dosage FORM matches what is registered in the Philippines (immediate-release
oral solid vs extended-release vs oral liquid; powder-for-injection vial vs ready-to-use
solution vs premixed bag), then human Rx before OTC. Default --prefer innovator: NDA/BLA, then the lowest NDA/BLA number
(the original reference listed drug rather than a later 505(b)(2) reformulation or a
biosimilar), then the original manufacturer over a repackager, then a true brand over an
authorized generic, then newest effective_time. --prefer recent (the literal brief): newest
effective_time, then NDA/BLA. Recent alone tends to pick repackager copies.
Labels with no openfda block are skipped unless --unindexed-fallback is given (a weak match
on the start of spl_product_data_elements; such files carry selection.match = "unindexed-spl"
and selection.confidence = "low"). In testing it picked wrong products about half the time.

Per-slug overrides (tools/drugdb/label_overrides.json) pin the primary label to a set ID,
application number, route and/or form, and can add secondary "alternate" labels (e.g. the
IV acyclovir label next to the oral one, stored under "alternate_labels"). Each override is a
list of criteria tried in order; the first criterion that any candidate satisfies wins and the
normal ranking breaks ties within it. When no criterion matches, the normal ranking applies
and the record carries selection.override.matched = null so the miss is visible.

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
trifenatate trihydrate trometamol axetil proxetil pivoxil cilexetil mofetil
etexilate dipivoxil hexetil marboxil tromethamine valerate xinafoate zinc amorphous crystalline
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
    "isophane insulin human": "insulin isophane human", "leuprorelin": "leuprolide",
    "clomifene": "clomiphene", "methylergometrine": "methylergonovine", "carmellose": "carboxymethylcellulose",
    "dicycloverine": "dicyclomine", "co-amoxiclav": "amoxicillin and clavulanate",
    "amoxicillin clavulanic acid": "amoxicillin and clavulanate", "benzylpenicillin benzathine": "penicillin g benzathine",
    "benzathine benzylpenicillin": "penicillin g benzathine", "procaine benzylpenicillin": "penicillin g procaine",
    "eformoterol": "formoterol", "cholecalciferol": "cholecalciferol", "levosalbutamol": "levalbuterol",
    "tretinoin": "tretinoin", "busulfan": "busulfan", "lidocaine": "lidocaine", "mitoxantrone": "mitoxantrone",
    "sodium cromoglicate": "cromolyn sodium", "cromoglicate": "cromolyn", "ethamsylate": "etamsylate",
    "trimeprazine": "alimemazine", "acetylcysteine": "acetylcysteine", "prednisolone": "prednisolone",
    "cetrizine": "cetirizine", "desloratidine": "desloratadine", "doxycyline": "doxycycline",
    "potasium": "potassium", "potassiumn": "potassium", "co-amoxoclav": "amoxicillin and clavulanate",
    "guiafenesin": "guaifenesin",
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
    "pharmacodynamics",
    "pharmacokinetics",
    "adverse_reactions_table",   # HTML frequency tables, kept for the drug page
]
EXTRACT_REV = 3   # bump when build_record() starts extracting something new; older files are rewritten once
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
    s = " " + re.sub(r"\s*-\s*", "-", ingredient.lower().strip()) + " "
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
    if gen and gen != subs and (not subs or len(gen) == len(subs)):
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
    """spl_product_data_elements reads "<Brand> <generic name> <ACTIVE> <MOIETY> <inactives...>".
    Require the ingredient to appear within the first 60 characters and at least twice in the
    first 200 (generic name + active ingredient), which excludes inactive ingredients."""
    words = ing_tokens(ingredient)
    if not words:
        return False
    pat = r"(?<![a-z0-9-])" + r"[\s,]+".join(map(re.escape, words)) + r"(?![a-z0-9]|-[a-z])"
    hits = [m.start() for m in re.finditer(pat, text[:200].lower())]
    return len(hits) >= 2 and hits[0] < 60


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


# --------------------------------------------------------------------------- dosage forms
# Form classes shared by the PH registry side and the US label side.
#   oral_ir      immediate-release tablet/capsule      oral_er   extended/sustained/modified release
#   oral_liquid  suspension/solution/syrup/granules    inj_powder  powder/lyophilized "for injection" (vial)
#   inj_solution solution for injection (vial/ampule)  inj_premix  premixed bag / Galaxy / Duplex / ready-to-use
ER_RX = re.compile(r"extended[\s-]*release|sustained[\s-]*release|controlled[\s-]*release|prolonged[\s-]*release|"
                   r"modified[\s-]*release|slow[\s-]*release|extended[\s-]*released", re.I)
ER_ABBR = re.compile(r"\b(?:ER|XR|XL|SR|CR|MR|LA|ODT-ER)\b")
SOLID_RX = re.compile(r"tablet|capsule|caplet", re.I)
LIQUID_RX = re.compile(r"suspension|syrup|elixir|oral solution|solution,? oral|granules|for oral solution|drops", re.I)
PREMIX_RX = re.compile(r"galaxy|pre-?mix|plastic container|flexible (?:plastic )?(?:container|bag)|ready[\s-]to[\s-]use|"
                       r"\bduplex\b|iso-?osmotic|\bfrozen\b|intravia|viaflex", re.I)
PREMIX_NAME_RX = re.compile(r"\b(?:and|in)\s+(?:\d[\d.]*\s*%\s*)?(?:sodium chloride|dextrose)", re.I)
POWDER_RX = re.compile(r"for injection|lyophili[sz]ed|\bpowder\b|for (?:intravenous )?infusion|pharmacy bulk package|"
                       r"for (?:injectable )?suspension", re.I)


def _seg(text: str) -> list[str]:
    return [x for x in re.split(r"\s*(?:•|·|;|\n|(?<=[a-z0-9)])\.\s+(?=[A-Z]))\s*", text or "") if x.strip()]


def label_form_text(label: dict) -> str:
    """Short, product-describing text: section 3 (PLR), else the description, else the carton panel."""
    for f in ("dosage_forms_and_strengths", "description", "package_label_principal_display_panel"):
        t = join_text(label.get(f))
        if t:
            return t[:1500]
    return ""


def label_forms(label: dict) -> set[str]:
    of = label.get("openfda") or {}
    groups = label_route_groups(label)
    names = " ".join((of.get("brand_name") or []) + (of.get("generic_name") or []))
    text = label_form_text(label)
    out: set[str] = set()
    if "oral" in groups:
        if ER_RX.search(names) or ER_ABBR.search(" ".join(of.get("brand_name") or [])):
            out.add("oral_er")
        for seg in _seg(text) or [names]:
            er = bool(ER_RX.search(seg) or ER_ABBR.search(seg))
            if SOLID_RX.search(seg):
                out.add("oral_er" if er else "oral_ir")
            if LIQUID_RX.search(seg):
                out.add("oral_liquid")
        if "oral_er" in out and (ER_RX.search(names) or ER_ABBR.search(" ".join(of.get("brand_name") or []))):
            out.discard("oral_ir")           # an ER-branded label never counts as immediate release
    if "inj" in groups:
        head = " ".join([names, text, join_text(label.get("package_label_principal_display_panel"))[:1500]])
        if PREMIX_RX.search(head) or PREMIX_NAME_RX.search(names):
            out.add("inj_premix")
        elif POWDER_RX.search(text or names):
            out.add("inj_powder")
        else:
            out.add("inj_solution")
    for g in groups - {"oral", "inj"}:
        out.add(g)
    return out


def ph_form_class(form: str) -> str | None:
    """PH registry dosage_strength_form -> form class (None when the route group is unknown)."""
    f = (form or "").lower()
    grp = next((g for g, pat in PH_FORM_GROUPS if re.search(pat, f)), None)
    if grp == "oral":
        if ER_RX.search(f) or re.search(r"\b(er|xr|xl|sr|cr|mr)\b|extended|sustained|prolonged|modified|controlled", f):
            return "oral_er"
        if SOLID_RX.search(f):
            return "oral_ir"
        return "oral_liquid"
    if grp == "inj":
        if re.search(r"pre-?mix|infusion bag|ready[\s-]to[\s-]use|\bin\s+(?:\d[\d.]*\s*%\s*)?(?:sodium chloride|dextrose)", f):
            return "inj_premix"
        if re.search(r"powder|lyophili", f):
            return "inj_powder"
        return "inj_solution"
    return grp


def form_weight(label: dict, ph_forms: dict | None) -> int:
    """2 = the label covers a main PH form (at least half as many PH products as the top form),
    1 = it covers a minor PH form, 0 = none. Coarse on purpose: near-ties (tablets 180 vs syrups 179)
    fall through to the innovator ordering instead of flipping on a product count."""
    if not ph_forms:
        return 0
    top = max(ph_forms.values())
    w = 0
    for c in label_forms(label):
        n = ph_forms.get(c, 0)
        if n and 2 * n >= top:
            return 2
        if n:
            w = 1
    return w


# --------------------------------------------------------------------------- per-slug overrides
DEFAULT_OVERRIDES = Path(__file__).resolve().parent / "label_overrides.json"


def load_overrides(path: Path) -> dict:
    if not path or not path.exists():
        return {}
    data = json.loads(path.read_text(encoding="utf-8"))
    return {k: v for k, v in data.items() if not k.startswith("_") and isinstance(v, dict)}


def _as_list(v) -> list:
    return v if isinstance(v, list) else ([] if v in (None, "") else [v])


def criterion_matches(label: dict, c: dict) -> bool:
    """Every key given in the criterion must hold:
    set_id, application_number (exact, or a prefix such as "ANDA"), route (any of), form (any of),
    not_form (none of), text_regex (on the dosage-forms text, e.g. the PH strengths), brand_regex,
    manufacturer_regex, require_sections (default ["dosage_and_administration"]; [] to allow any)."""
    of = label.get("openfda") or {}
    if c.get("set_id") and label.get("set_id") not in _as_list(c["set_id"]):
        return False
    if c.get("application_number"):
        apps = [a.upper() for a in of.get("application_number") or []]
        want = [w.upper() for w in _as_list(c["application_number"])]
        if not any(a == w or (w.isalpha() and a.startswith(w)) for a in apps for w in want):
            return False
    if c.get("route"):
        routes = {r.upper() for r in of.get("route") or []}
        if not routes & {r.upper() for r in _as_list(c["route"])}:
            return False
    forms = label_forms(label) if (c.get("form") or c.get("not_form")) else set()
    if c.get("form") and not forms & set(_as_list(c["form"])):
        return False
    if c.get("not_form") and forms & set(_as_list(c["not_form"])):
        return False
    if c.get("text_regex") and not re.search(c["text_regex"], label_form_text(label), re.I | re.S):
        return False
    # A pinned label must carry real prescribing text (some SPL records index only the carton).
    for f in _as_list(c.get("require_sections", ["dosage_and_administration"])):
        if not join_text(label.get(f)):
            return False
    if c.get("brand_regex") and not re.search(c["brand_regex"], " ".join(of.get("brand_name") or []), re.I):
        return False
    if c.get("manufacturer_regex") and not re.search(c["manufacturer_regex"], " ".join(of.get("manufacturer_name") or []), re.I):
        return False
    return True


def rank_key(label: dict, prefer: str, ph_routes: dict | None = None, ph_forms: dict | None = None):
    """Smaller sorts first. Route match to the PH registrations, then dosage-form match (IR vs ER
    oral solid, vial vs premixed bag; see label_forms), then Rx>OTC, then:
    innovator: NDA/BLA, original manufacturer (not a repackager), newest effective_time
               (lowest NDA/BLA number = the original reference product, not a later
               505(b)(2) reformulation or biosimilar)
    recent:    newest effective_time, NDA/BLA (the literal brief)"""
    eff = str(label.get("effective_time") or "0")
    inn = 0 if is_innovator(label) else 1
    rep = 1 if is_repackager(label) else 0
    eff_key = "".join(chr(255 - ord(c)) for c in eff.ljust(8, "0"))  # descending date
    head = (-route_weight(label, ph_routes), -form_weight(label, ph_forms), product_rank(label))
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


def extract_hepatic(pop: str, dosing: str) -> str:
    """Verbatim hepatic-impairment text: "8.x Hepatic Impairment" from Use in Specific Populations, plus any
    "2.x ..." dosing subsection whose heading mentions hepatic impairment."""
    found = []
    m = re.search(r"(?:^|\s)(8\.\d+)\s+(?:Patients\s+with\s+)?(?:Hepatic\s+Impairment|Hepatic\s+Insufficiency|Impaired\s+Hepatic)", pop or "")
    if m:
        nxt = re.search(r"\s8\.\d+\s+[A-Z]|\s10\s+OVERDOSAGE", pop[m.end():])
        found.append(pop[m.start(1):m.end() + nxt.start() if nxt else len(pop)].strip())
    heads = list(re.finditer(r"(?:^|\s)(2\.\d+)\s+(?=[A-Z])", dosing or ""))
    for i, h in enumerate(heads):
        end = heads[i + 1].start() if i + 1 < len(heads) else len(dosing)
        chunk = dosing[h.start(1):end].strip()
        if re.match(r"2\.\d+\s+[^.]{0,80}\b(Hepatic|Liver)\b", chunk):
            found.append(chunk)
    return "\n\n".join(found)


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


def extract_sections(label: dict) -> tuple[dict, dict, list]:
    """(sections, section_sources, renal_impairment_sources), verbatim from one openFDA label."""
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
    hep = extract_hepatic(join_text(label.get("use_in_specific_populations")),
                          join_text(label.get("dosage_and_administration")))
    if hep:
        sections["hepatic_impairment"] = hep
    return sections, section_sources, renal


def label_meta_block(label: dict) -> dict:
    of = label.get("openfda") or {}
    return {
        "set_id": label.get("set_id", ""),
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
        # openFDA pharmacologic classes (public domain; used for the drug-page "At a glance" card)
        "pharm_class_epc": of.get("pharm_class_epc") or [],
        "pharm_class_moa": of.get("pharm_class_moa") or [],
        "pharm_class_pe": of.get("pharm_class_pe") or [],
        "pharm_class_cs": of.get("pharm_class_cs") or [],
        "innovator": is_innovator(label),
        "forms": sorted(label_forms(label)),
        "extract_rev": EXTRACT_REV,
    }


def source_block(set_id: str) -> dict:
    return {
        "publisher": "U.S. Food and Drug Administration",
        "via": "openFDA drug label endpoint",
        "dailymed_url": f"https://dailymed.nlm.nih.gov/dailymed/drugInfo.cfm?setid={set_id}" if set_id else "",
        "api_url": f"{API}?search=set_id:%22{set_id}%22" if set_id else "",
        "license_note": "U.S. government work; label text reproduced verbatim.",
    }


def build_alternate(alt: dict, label: dict, matched: dict) -> dict:
    """A secondary label for the same generic (e.g. the IV acyclovir label beside the oral one).
    Same shape as a primary record's label/source/sections so the page generator can reuse its helpers."""
    sections, section_sources, renal = extract_sections(label)
    meta = label_meta_block(label)
    return {
        "role": alt.get("role", ""),
        "heading": alt.get("title") or f"US label: {alt.get('role', 'alternate')}",
        "route": meta["route"],
        "set_id": meta["set_id"],
        "matched": matched,
        "source": source_block(meta["set_id"]),
        "label": meta,
        "sections": sections,
        "section_sources": section_sources,
        "renal_impairment_sources": renal,
    }


def build_record(slug: str, g: dict, label: dict, n_candidates: int, prefer: str,
                 match: str = "openfda", ph_routes: dict | None = None, ph_forms: dict | None = None,
                 override: dict | None = None, alternates: list | None = None) -> dict:
    sections, section_sources, renal = extract_sections(label)
    meta = label_meta_block(label)
    set_id = meta["set_id"]
    selection = {"candidates": n_candidates, "rule": prefer, "match": match,
                 "confidence": "high" if match == "openfda" else "low",
                 "ph_routes": ph_routes or {}, "ph_forms": ph_forms or {}, "repackager": is_repackager(label)}
    if override is not None:
        selection["override"] = override
    rec = {
        "schema_version": SCHEMA_VERSION,
        "slug": slug,
        "name": g.get("name", slug),
        "ingredients": g["ingredients"],
        "source": source_block(set_id),
        "selection": selection,
        "label": meta,
        "sections": sections,
        "section_sources": section_sources,
        "renal_impairment_sources": renal,
        "fetched_at": dt.datetime.now(MANILA).isoformat(timespec="seconds"),
    }
    if alternates:
        rec["alternate_labels"] = [build_alternate(a, l, m) for a, l, m in alternates]
    return rec


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
    the candidate counts, and a few near-miss substance sets for diagnosing misses.
    For slugs with an override it also keeps the best label per override criterion (primary and
    each alternate), so bulk mode honors overrides without holding every candidate in memory."""

    def __init__(self, generics: dict, prefer: str, ph_routes: dict, ph_forms: dict | None = None,
                 overrides: dict | None = None):
        self.generics, self.prefer, self.ph_routes = generics, prefer, ph_routes
        self.ph_forms = ph_forms or {}
        self.overrides = overrides or {}
        self.best: dict[str, dict] = {}
        self.best_fb: dict[str, dict] = {}
        self.best_ov: dict[tuple, dict] = {}     # (slug, "primary"|alt index, criterion index) -> label
        self.counts: dict[str, int] = {s: 0 for s in generics}
        self.counts_fb: dict[str, int] = {s: 0 for s in generics}
        self.near: dict[str, set] = {}
        self.errors: set[str] = set()

    def _better(self, slug, a, b) -> bool:
        r, f = self.ph_routes.get(slug), self.ph_forms.get(slug)
        return rank_key(a, self.prefer, r, f) < rank_key(b, self.prefer, r, f)

    def _keep(self, store, key, slug, label):
        cur = store.get(key)
        if cur is None or self._better(slug, label, cur):
            store[key] = label

    def add(self, slug: str, label: dict, fallback: bool = False):
        store, counts = (self.best_fb, self.counts_fb) if fallback else (self.best, self.counts)
        counts[slug] += 1
        self._keep(store, slug, slug, label)
        ov = self.overrides.get(slug)
        if ov and not fallback:
            for i, c in enumerate(ov.get("primary") or []):
                if criterion_matches(label, c):
                    self._keep(self.best_ov, (slug, "primary", i), slug, label)
            for j, alt in enumerate(ov.get("alternates") or []):
                for i, c in enumerate(alt.get("criteria") or []):
                    if criterion_matches(label, c):
                        self._keep(self.best_ov, (slug, j, i), slug, label)

    def near_miss(self, slug: str, label: dict):
        s = self.near.setdefault(slug, set())
        if len(s) < 8:
            subs = label_substances(label)
            s.add(" + ".join(subs) if subs else "(no openfda) " + join_text(label.get("spl_product_data_elements"))[:80])

    def _override_pick(self, slug: str, which, criteria: list) -> tuple[dict | None, int | None]:
        for i in range(len(criteria)):
            lab = self.best_ov.get((slug, which, i))
            if lab is not None:
                return lab, i
        return None, None

    def override_info(self, slug: str) -> dict | None:
        ov = self.overrides.get(slug)
        if not ov:
            return None
        _, i = self._override_pick(slug, "primary", ov.get("primary") or [])
        return {"reason": ov.get("reason", ""), "matched": None if i is None else (ov.get("primary") or [])[i],
                "criterion_index": i}

    def alternates(self, slug: str) -> list[tuple[dict, dict, dict]]:
        """[(alternate config, label, matched criterion)] for the alternates that found a label."""
        out = []
        primary = self.result(slug)[0]
        for j, alt in enumerate((self.overrides.get(slug) or {}).get("alternates") or []):
            lab, i = self._override_pick(slug, j, alt.get("criteria") or [])
            if lab is not None and (primary is None or lab.get("set_id") != primary.get("set_id")):
                out.append((alt, lab, (alt.get("criteria") or [])[i]))
        return out

    def result(self, slug: str):
        ov = self.overrides.get(slug)
        if ov and slug in self.best:
            lab, _ = self._override_pick(slug, "primary", ov.get("primary") or [])
            if lab is not None:
                return lab, "openfda", self.counts[slug]
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
            if slug not in col.best and args.unindexed_fallback:
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
        if getattr(args, "explain", False):
            ok = [l for l in labels if is_human(l) and label_matches_any(g["ingredients"], l)]
            r, f = col.ph_routes.get(slug), col.ph_forms.get(slug)
            ok.sort(key=lambda l: rank_key(l, args.prefer, r, f))
            for l in ok[:args.explain]:
                of = l.get("openfda") or {}
                print(f"    {first(of.get('application_number')):<12} {first(of.get('brand_name'))[:40]:<40} "
                      f"{first(of.get('manufacturer_name'))[:30]:<30} {','.join(of.get('route') or [])[:24]:<24} "
                      f"{','.join(sorted(label_forms(l))):<24} {l.get('effective_time')} {l.get('set_id')}")
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
                if not hits and args.unindexed_fallback:
                    for slug in matcher.fallback(label):
                        col.add(slug, label, fallback=True)
            dest.unlink()
            print(f"bulk part {i}/{len(parts)} done in {time.time() - t0:.0f}s; {seen} labels scanned, "
                  f"{len(col.best)} generics matched (+{len(set(col.best_fb) - set(col.best))} unindexed)",
                  flush=True)


# --------------------------------------------------------------------------- PH routes
def load_ph_routes(registry_dir: Path) -> dict[str, dict[str, int]]:
    """slug -> {route group: number of PH products}, from data/drugs/registry/*.json."""
    return load_ph_profile(registry_dir)[0]


def load_ph_profile(registry_dir: Path) -> tuple[dict[str, dict[str, int]], dict[str, dict[str, int]]]:
    """(routes, forms): slug -> {route group: n} and slug -> {form class: n} (see ph_form_class)."""
    routes: dict[str, dict[str, int]] = {}
    forms: dict[str, dict[str, int]] = {}
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
                    d = routes.setdefault(slug, {})
                    d[grp] = d.get(grp, 0) + 1
                    break
            fc = ph_form_class(form)
            if fc:
                d = forms.setdefault(slug, {})
                d[fc] = d.get(fc, 0) + 1
    return routes, forms


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
    ap.add_argument("--unindexed-fallback", action="store_true",
                    help="also match labels with no openfda block by their SPL product data "
                         "(low confidence; off by default because it picks wrong products)")
    ap.add_argument("--overrides", default=str(DEFAULT_OVERRIDES),
                    help="per-slug label overrides (JSON; see label_overrides.json); '' to disable")
    ap.add_argument("--force", action="store_true", help="rewrite every file even if unchanged")
    ap.add_argument("--explain", type=int, default=0, metavar="N",
                    help="api mode: print the top N ranked candidates per generic (with form classes)")
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
    ph_routes, ph_forms = load_ph_profile(Path(args.registry_dir))
    overrides = load_overrides(Path(args.overrides)) if args.overrides else {}

    source = args.source
    if source == "auto":
        source = "api" if len(generics) <= 200 else "bulk"
    print(f"{len(generics)} generics from {gpath.name}; source={source}; prefer={args.prefer}; "
          f"PH routes known for {sum(1 for s in generics if s in ph_routes)}", flush=True)
    if overrides:
        print(f"label overrides: {', '.join(sorted(k for k in overrides if k in generics)) or '(none in this run)'}")
    col = Collector(generics, args.prefer, ph_routes, ph_forms, overrides)
    (run_api if source == "api" else run_bulk)(generics, col, args)

    added, changed, removed, unchanged, missing = [], [], [], 0, []
    stats = {"openfda": 0, "unindexed-spl": 0, "innovator": 0, "repackager": 0}
    for slug, g in sorted(generics.items()):
        label, how, n_cand = col.result(slug)
        if label is None:
            m = {"slug": slug, "name": g.get("name", slug), "ingredients": g["ingredients"],
                 "reason": "fetch error" if slug in col.errors else "no matching US FDA human label"}
            if col.near.get(slug):
                m["near_misses"] = sorted(col.near[slug])
            missing.append(m)
            stale = out_dir / f"{slug}.json"
            if stale.exists() and slug not in col.errors:  # previously matched, no longer does
                try:
                    old = json.loads(stale.read_text(encoding="utf-8")).get("label", {})
                except Exception:
                    old = {}
                stale.unlink()
                removed.append({"slug": slug, "name": g.get("name", slug), "previous": {
                    "set_id": old.get("set_id"), "effective_time": old.get("effective_time"),
                    "brand_name": old.get("brand_name")}})
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
        alts = col.alternates(slug)
        ov_info = col.override_info(slug)
        if ov_info is not None:
            print(f"  override {slug}: {first((label.get('openfda') or {}).get('brand_name'))} "
                  f"{first((label.get('openfda') or {}).get('application_number'))} set {label.get('set_id')} "
                  f"(criterion {ov_info['criterion_index']}); alternates: "
                  + (", ".join(f"{a.get('role')}={l.get('set_id')}" for a, l, _ in alts) or "none"))
        new_alt = [(l.get("set_id", ""), l.get("effective_time", "")) for _, l, _ in alts]
        old_alt, old_ov = [], None
        if path.exists() and old_meta is not None:
            try:
                old_rec = json.loads(path.read_text(encoding="utf-8"))
                old_alt = [(a.get("label", {}).get("set_id"), a.get("label", {}).get("effective_time"))
                           for a in old_rec.get("alternate_labels") or []]
                old_ov = (old_rec.get("selection") or {}).get("override")
            except Exception:
                pass
        # Records written by an older build_record() (no pharm_class_*, no hepatic_impairment, no
        # adverse_reactions_table) are rewritten once, silently.
        if (old_key == new_key and new_alt == old_alt and ov_info == old_ov and not args.force
                and (old_meta or {}).get("extract_rev", 0) >= EXTRACT_REV):
            unchanged += 1
            continue
        if ov_info is not None and ov_info["matched"] is None:
            print(f"  WARNING {slug}: no candidate met any override criterion; normal ranking used", file=sys.stderr)
        rec = build_record(slug, g, label, n_cand, args.prefer, how, ph_routes.get(slug), ph_forms.get(slug),
                           ov_info, alts)
        path.write_text(json.dumps(rec, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        entry = {"slug": slug, "name": g.get("name", slug), "brand_name": rec["label"]["brand_name"],
                 "application_number": rec["label"]["application_number"],
                 "set_id": new_key[0], "effective_time": new_key[1],
                 "dailymed_url": rec["source"]["dailymed_url"]}
        if alts:
            entry["alternate_labels"] = [{"role": a["role"], "set_id": a["set_id"],
                                          "brand_name": a["label"]["brand_name"],
                                          "application_number": a["label"]["application_number"]}
                                         for a in rec["alternate_labels"]]
        if old_key is None:
            added.append(entry)
        elif old_key != new_key or new_alt != old_alt:
            entry["previous"] = {"set_id": old_key[0], "effective_time": old_key[1]}
            if new_alt != old_alt:
                entry["previous"]["alternate_labels"] = [{"set_id": a, "effective_time": b} for a, b in old_alt]
            changed.append(entry)
        # a forced rewrite of an unchanged label is not a review item

    now = dt.datetime.now(MANILA).isoformat(timespec="seconds")
    # A partial run (a list other than the full generics.json, or --only) must not clobber the
    # full-catalog review files: it merges into them instead of replacing them.
    partial = bool(args.only) or gpath.resolve() != DEFAULT_GENERICS.resolve()
    mpath, cpath = out_dir / "_missing.json", out_dir / "_changes.json"
    missing_doc = {"generated_at": now, "generics_file": gpath.name, "count": len(missing), "missing": missing}
    changes_doc = {"generated_at": now,
                   "note": "US FDA labels added, changed or removed since the last full run; "
                           "for Dr. Rivero's weekly review.",
                   "source": source, "added": added, "changed": changed, "removed": removed}
    if partial:
        ran = set(generics)
        if mpath.exists():
            prev = json.loads(mpath.read_text(encoding="utf-8"))
            merged = sorted([m for m in prev.get("missing", []) if m["slug"] not in ran] + missing,
                            key=lambda m: m["slug"])
            missing_doc = {**prev, "missing": merged, "count": len(merged)}
        if cpath.exists():
            prev = json.loads(cpath.read_text(encoding="utf-8"))
            mine = {e["slug"] for e in added + changed + removed}
            if not mine:
                changes_doc = prev
            else:
                changes_doc = {**prev, "generated_at": now}
                for key, new in (("added", added), ("changed", changed), ("removed", removed)):
                    changes_doc[key] = sorted([e for e in prev.get(key, []) if e["slug"] not in mine] + new,
                                              key=lambda e: e["slug"])
    write_if_changed(mpath, missing_doc, ignore=("generated_at",))
    write_if_changed(cpath, changes_doc, ignore=("generated_at",))

    total = len(generics)
    hits = total - len(missing)
    print(f"matched {hits}/{total} ({100 * hits / max(total, 1):.1f}%) {stats}; added {len(added)}, "
          f"changed {len(changed)}, removed {len(removed)}, unchanged {unchanged}, missing {len(missing)}")
    for m in missing[:60]:
        print(f"  missing: {m['slug']} ({m['reason']}) {m.get('near_misses', [])[:3]}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
