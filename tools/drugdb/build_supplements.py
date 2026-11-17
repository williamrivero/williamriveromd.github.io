#!/usr/bin/env python3
"""Normalize the PH FDA food-supplement crawl into data/drugs/supplements/.

Food supplements are registered with the FDA Philippines as FOOD products (FR-... numbers,
API key "fdafoodproducts"), not as drugs, so they are kept apart from the drug registry.

Input:
  --supp-file FILE   ph-fda-supplements.json (full crawl) or ph-fda-supplements-sample.json:
                     a dict keyed by ACCOUNTCODE with PRODUCT_NAME, BRAND_NAME, COMPANY_NAME,
                     TYPE_FOOD_PRODUCT_LABEL, DENIAL_DATE (actually the decision/issue date),
                     DATE_VALIDITY, LOW_RISK_DECISION, APPLICATION_TYPE_LABEL, IS_CANCELED.
                     A list of such records is also accepted.
Output (under --out-dir, default data/drugs):
  supplements/<a-z|0>.json   products, sharded by the first character of the brand slug (each < 5 MB)
  supplements.json           brand-level index {as_of, source, counts, brands{slug: {...}}}
  supplements/_report.json   counts plus excluded records (canceled, expired, not a supplement)

Foods for special medical purposes (FSMP: "FOOD FOR SPECIAL MEDICAL PURPOSES … for the dietary management of …",
e.g. the renal formulas Nepro, Kidneypro, Fresubin Renal, Nephrisol) are kept as type "fsmp" (category "fsmp",
"Medical nutrition (FSMP)") with sub-tags (renal, diabetes, high-protein, peptide, pediatric, general), the registered
"dietary management" use, the flavor and, for renal formulas, the LP/HP variant. Registrations of one renal product
line are grouped on one brand (Nepro HP + Nepro LP -> "Nepro"; Nephrisol + Nephrisol-D -> "Nephrisol").
Foods for special DIETARY use (FSDU: "FOOD FOR SPECIAL DIETARY USE", e.g. Glucerna, Efione Nu Reno, Efione Nu Lopo) are a
separate FDA category, kept as type "fsdu" (category "fsdu", "Special dietary food (FSDU)") with the same sub-tags, registered
use and flavor; renal ones (dialysis, CKD) also get "renal_formula" and join the renal list. FSMP wording wins over FSDU
when a product name carries both.

Registrations that are neither FSMP, FSDU nor a stated food supplement (the product name says FOOD/DIETARY/HERBAL/
BOTANICAL SUPPLEMENT, or "SUPPLEMENT CAPSULE/TABLET/SOFTGEL", or carries "no approved therapeutic claims") are type "other"
("Other food registration", category "food"): milk supplements, adult nutrition drinks, ready-to-use supplementary foods,
lipid-based nutrient supplements, snack wafers. They make no supplement claim, so the pages give them a neutral banner.

Brand families (tools/drugdb/supplement_brand_families.json) merge registrations filed under spelling or line variants of
one brand onto a single page (Ferolip + Ferolip CT + Ferolip Chews -> "Ferolip"); each product keeps its registered brand in
"brand_registered", the brand index lists the other names under "aka", and "retired" maps the merged slugs to the main one.

A product is excluded when it is canceled (IS_CANCELED = "Y" or a "cancel this authorization"
application), past its validity date, not approved, a raw material, or not a food supplement
(coffee mixes, teas, juices, wine and similar foods that came back from the same search).
"""
import argparse, datetime as dt, json, os, re, sys, unicodedata
from collections import Counter, defaultdict

# ─────────────────────────────────────────────────────────────────────────────
# Text helpers
# ─────────────────────────────────────────────────────────────────────────────
def fold(s):
    return unicodedata.normalize("NFKD", s or "").encode("ascii", "ignore").decode()

def ws(s):
    return re.sub(r"\s+", " ", (s or "")).strip()

def slugify(s):
    s = fold(s).lower().replace("&", " and ")
    s = re.sub(r"[^a-z0-9]+", "-", s).strip("-")
    return re.sub(r"-{2,}", "-", s)[:80].strip("-")

def parse_date(s):
    s = ws(s)
    for f in ("%d %B %Y", "%d %b %Y", "%B %d, %Y", "%Y-%m-%d", "%m/%d/%Y"):
        try:
            return dt.datetime.strptime(s, f).date()
        except ValueError:
            pass
    return None

# The boilerplate registration phrase, with its many spellings (sometimes truncated by the API).
REG_PHRASE = re.compile(r"\(?\s*REGISTERED\s+AS\s+(?:A\s+)?FOOD\s+SUPPLEMENT[^)]*(?:\)|$)", re.I)
REG_PHRASE2 = re.compile(r"\(?\s*REGISTERED\s+AS\s*$", re.I)

def clean_product_name(raw):
    t = ws(raw)
    t = REG_PHRASE.sub(" ", t)
    t = REG_PHRASE2.sub(" ", t)
    t = re.sub(r"\(\s*\)", " ", t)
    return ws(t).strip(" -,;")

# ─────────────────────────────────────────────────────────────────────────────
# Form
# ─────────────────────────────────────────────────────────────────────────────
FORMS = [  # order matters: first match wins
    ("softgel", r"soft\s*-?\s*gel|soft\s+gelatin"),
    ("effervescent tablet", r"effervescent"),
    ("chewable tablet", r"chewable"),
    ("gummy", r"gumm(?:y|ies)"),
    ("jelly", r"\bjelly\b"),
    ("capsule", r"\bcap(?:sule|let)?s?\b|vegicap|veggie\s*cap"),
    ("tablet", r"\btab(?:let)?s?\b|film[- ]coated"),
    ("powder", r"powder|sachet|granule|drink mix|stick pack"),
    ("liquid", r"liquid|syrup|drops?\b|shot\b|emulsion|solution|suspension|tonic|\boil\b|drink\b|juice|elixir"),
    ("lozenge", r"lozenge|candy|candies"),
    ("tea", r"\btea\b"),
]

def form_of(text):
    t = text.lower()
    for name, rx in FORMS:
        if re.search(rx, t):
            return name
    return "other"

# ─────────────────────────────────────────────────────────────────────────────
# Ingredient normalization
# ─────────────────────────────────────────────────────────────────────────────
# Botanicals: common (PH or English) name -> canonical "Common name (Latin name)". Latin names are matched too.
BOTANICALS = [
    ("Guyabano", "Annona muricata", r"guyabano|graviola|soursop|annona\s+muricata|anona\s+muricata"),
    ("Moringa, malunggay", "Moringa oleifera", r"malunggay|moringa"),
    ("Sambong", "Blumea balsamifera", r"sambong|blumea\s+balsamifera"),
    ("Ampalaya, bitter gourd", "Momordica charantia", r"ampalaya|bitter\s+(?:gourd|melon)|momordica"),
    ("Turmeric", "Curcuma longa", r"turmeric|curcuma\s+longa"),
    ("Milk thistle", "Silybum marianum", r"milk\s+thistle|silybum|silymarin"),
    ("Mangosteen", "Garcinia mangostana", r"mangosteen|garcinia\s+mangostana|xanthone"),
    ("Garcinia cambogia", "Garcinia gummi-gutta", r"garcinia\s+cambogia|garcinia\s+gummi"),
    ("Green tea", "Camellia sinensis", r"green\s+tea|camellia\s+sinensis|\begcg\b|epigallocatechin"),
    ("Ginger", "Zingiber officinale", r"\bginger\b|zingiber"),
    ("Lagundi", "Vitex negundo", r"lagundi|vitex\s+negundo"),
    ("Banaba", "Lagerstroemia speciosa", r"banaba|lagerstroemia"),
    ("Tawa-tawa", "Euphorbia hirta", r"tawa[- ]?tawa|euphorbia\s+hirta"),
    ("Uva ursi, bearberry", "Arctostaphylos uva-ursi", r"uva[- ]ursi|bearberry|arctostaphylos"),
    ("Cranberry", "Vaccinium macrocarpon", r"cranberr|vaccinium\s+macrocarpon"),
    ("Lingonberry", "Vaccinium vitis-idaea", r"lingonberr|vitis[- ]idaea"),
    ("Bilberry", "Vaccinium myrtillus", r"bilberr|vaccinium\s+myrtillus"),
    ("Stonebreaker", "Phyllanthus niruri", r"phyll?anth?us\s+niruri|stone\s*breaker|chanca\s+piedra"),
    ("Phyllanthus urinaria", "Phyllanthus urinaria", r"phyll?anth?us\s+urinaria"),
    ("Rosemary", "Rosmarinus officinalis", r"rosemary|rosmarinus"),
    ("Basil", "Ocimum basilicum", r"\bbasil\b|ocimum\s+basilicum"),
    ("Holy basil, tulsi", "Ocimum tenuiflorum", r"holy\s+basil|tulsi|ocimum\s+(?:sanctum|tenuiflorum)"),
    ("Ashitaba", "Angelica keiskei", r"ashitaba|angelica\s+keiskei"),
    ("Gotu kola", "Centella asiatica", r"centella|gotu\s+kola|takip[- ]kuhol"),
    ("Punarnava", "Boerhavia diffusa", r"boerhaa?via|punarnava"),
    ("Dandelion", "Taraxacum officinale", r"dandelion|taraxacum"),
    ("Parsley", "Petroselinum crispum", r"parsley|petroselinum"),
    ("Horsetail", "Equisetum arvense", r"horsetail|equisetum"),
    ("Stinging nettle", "Urtica dioica", r"nettle|urtica"),
    ("Ginkgo", "Ginkgo biloba", r"g[iy]n[gk]+o"),
    ("Ginseng", "Panax ginseng", r"ginseng|panax"),
    ("Saw palmetto", "Serenoa repens", r"saw\s+palmetto|serenoa"),
    ("White mulberry", "Morus alba", r"mulberry|morus\s+alba"),
    ("White kidney bean", "Phaseolus vulgaris", r"(?:white\s+)?kidney\s+bean|phaseolus"),
    ("Barley grass", "Hordeum vulgare", r"barley"),
    ("Spirulina", "Arthrospira platensis", r"spirulina|arthrospira"),
    ("Chlorella", "Chlorella vulgaris", r"chlorella"),
    ("Noni", "Morinda citrifolia", r"\bnoni\b|morinda"),
    ("Dragon fruit", "Hylocereus undatus", r"dragon\s*fruit|pitaya|hylocereus|selenicereus"),
    ("Couch grass", "Elymus repens", r"couch\s+grass|agropyron|elymus\s+repens"),
    ("Cramp bark", "Viburnum opulus", r"cramp\s+bark|viburnum"),
    ("Buchu", "Agathosma betulina", r"buchu|agathosma|barosma"),
    ("Olive leaf", "Olea europaea", r"olive\s+leaf|olea\s+europaea"),
    ("Fennel", "Foeniculum vulgare", r"fennel|foeniculum"),
    ("Artichoke", "Cynara scolymus", r"artichoke|cynara"),
    ("Schisandra", "Schisandra chinensis", r"schisandra|schizandra"),
    ("Pomegranate", "Punica granatum", r"pomegranate|punica"),
    ("Grape seed", "Vitis vinifera", r"grape\s*seed|vitis\s+vinifera"),
    ("Garlic", "Allium sativum", r"\bgarlic\b|allium\s+sativum"),
    ("Cinnamon", "Cinnamomum spp.", r"cinnamon|cinnamomum"),
    ("Gymnema", "Gymnema sylvestre", r"gymnema"),
    ("Echinacea", "Echinacea purpurea", r"echinacea"),
    ("Elderberry", "Sambucus nigra", r"elderberr|sambucus"),
    ("Boswellia", "Boswellia serrata", r"boswellia"),
    ("Black pepper extract, piperine", "Piper nigrum", r"piperine|black\s+pepper|piper\s+nigrum"),
    ("Thyme", "Thymus vulgaris", r"\bthyme\b|thymus\s+vulgaris"),
    ("Sonchus arvensis", "Sonchus arvensis", r"sonchus"),
    ("Mimosa pudica", "Mimosa pudica", r"mimosa\s+pudica"),
    ("Gloriosa superba", "Gloriosa superba", r"gloriosa"),
    ("Alfalfa", "Medicago sativa", r"alfalfa|medicago"),
    ("Jute leaves, saluyot", "Corchorus olitorius", r"saluyot|jute\s+leaves|corchorus"),
    ("Reishi, lingzhi", "Ganoderma lucidum", r"reishi|lingzhi|ganoderma"),
    ("Cordyceps", "Cordyceps spp.", r"cordyceps"),
    ("Mangosteen pericarp", "Garcinia mangostana", r"mangosteen\s+pericarp"),
    ("Psyllium", "Plantago ovata", r"psyllium|ispaghula|plantago"),
    ("Chia seed", "Salvia hispanica", r"\bchia\b"),
    ("Pandan", "Pandanus amaryllifolius", r"pandan"),
    ("Alingatong", "Dendrocnide meyeniana", r"alingatong"),
    ("Pine bark", "Pinus pinaster", r"pine\s+bark|pycnogenol|pinus"),
    ("Green coffee bean", "Coffea arabica", r"green\s+coffee"),
    ("Astragalus", "Astragalus membranaceus", r"astragalus"),
    ("Rhubarb", "Rheum spp.", r"rhubarb|rheum\b"),
    ("Licorice", "Glycyrrhiza glabra", r"licorice|liquorice|glycyrrhiza"),
    ("Cat's whiskers, balbas pusa", "Orthosiphon aristatus", r"orthosiphon|cat'?s\s+whisker|java\s+tea|balbas[- ]?pusa"),
]
_BOT = [(c, l, re.compile(rx, re.I)) for c, l, rx in BOTANICALS]

VITAMINS = [  # canonical, regex
    ("Vitamin A", r"vitamin\s*a\b|retinol|retinyl|beta[- ]carotene"),
    ("Vitamin B1 (thiamine)", r"vitamin\s*b\s*1\b|thiamin|benfotiamine"),
    ("Vitamin B2 (riboflavin)", r"vitamin\s*b\s*2\b|riboflavin"),
    ("Vitamin B3 (niacin)", r"vitamin\s*b\s*3\b|niacin|nicotinamide|nicotinic acid"),
    ("Vitamin B5 (pantothenic acid)", r"vitamin\s*b\s*5\b|pantothen"),
    ("Vitamin B6 (pyridoxine)", r"vitamin\s*b\s*6\b|pyridox"),
    ("Vitamin B7 (biotin)", r"vitamin\s*b\s*7\b|biotin"),
    ("Vitamin B9 (folate)", r"vitamin\s*b\s*9\b|folic|folate|methylfolate"),
    ("Vitamin B12 (cobalamin)", r"vitamin\s*b\s*12\b|cobalamin|cyanocobal"),
    ("Vitamin B complex", r"vitamin\s*b[- ]?complex|b vitamins"),
    ("Vitamin C", r"vitamin\s*c\b|ascorb"),
    ("Vitamin D3 (cholecalciferol)", r"vitamin\s*d\s*3?\b|c[h]?olecalciferol"),
    ("Vitamin D2 (ergocalciferol)", r"vitamin\s*d\s*2\b|ergocalciferol"),
    ("Vitamin E", r"vitamin\s*e\b|tocopher|tocotrienol"),
    ("Vitamin K2 (menaquinone)", r"vitamin\s*k\s*2\b|menaquinone|mk-?7"),
    ("Vitamin K1 (phytonadione)", r"vitamin\s*k\s*1?\b|phytonadione|phylloquinone"),
    ("Multivitamins", r"multi[- ]?vitamin|vitamins?\s*(?:and|&)\s*minerals?|vitamins?\s+complex|^vitamins?$"),
]
_VIT = [(c, re.compile(rx, re.I)) for c, rx in VITAMINS]
MINERALS = ["zinc", "calcium", "magnesium", "iron", "selenium", "chromium", "potassium", "copper", "iodine",
            "manganese", "molybdenum", "boron", "silica", "phosphorus", "sodium"]
MINERAL_RX = re.compile(r"\b(" + "|".join(MINERALS) + r")\b|ferrous|ferric|minerals?\b", re.I)

GENERA = {"l": "Lactobacillus", "b": None, "s": None, "e": "Enterococcus", "lc": "Lactococcus", "p": "Pediococcus"}
B_BIFIDO = {"longum", "bifidum", "breve", "infantis", "lactis", "animalis", "adolescentis"}
B_BACILLUS = {"coagulans", "subtilis", "clausii", "licheniformis", "cereus"}
PROBIOTIC_GENERA = r"lactobacill|bifidobacter|streptococcus\s+thermophilus|bacillus\s+(?:coagulans|subtilis|clausii)|saccharomyces|" \
                   r"enterococcus|lactococcus|lacticaseibacillus|lactiplantibacillus|limosilactobacillus|ligilactobacillus|pediococcus|" \
                   r"leuconostoc|probiotic|\bcfu\b|clostridium\s+butyricum"

def norm_strain(p):
    """'L. ACIDOPHILUS' -> 'Lactobacillus acidophilus'; 'BIFIDOBACTERIUM LONGUM' -> 'Bifidobacterium longum'."""
    p = re.sub(r"\b(?:probiotics?|strains?|blend|capsules?|tablets?|powder)\b", " ", p, flags=re.I)
    m = re.match(r"^\s*([A-Za-z]{1,2})\.\s*([A-Za-z]+)(.*)$", p)
    if m:
        g, sp, rest = m.group(1).lower(), m.group(2).lower(), m.group(3)
        genus = GENERA.get(g)
        if g == "b":
            genus = "Bifidobacterium" if sp in B_BIFIDO else ("Bacillus" if sp in B_BACILLUS else None)
        elif g == "s":
            genus = "Streptococcus" if sp == "thermophilus" else ("Saccharomyces" if sp in ("boulardii", "cerevisiae") else None)
        if genus:
            return f"{genus} {sp}{rest.rstrip()}".strip()
    m = re.match(r"^\s*([A-Za-z]+)\s+([A-Za-z]+)(.*)$", p)
    if m and re.match(PROBIOTIC_GENERA, m.group(1) + " " + m.group(2), re.I):
        return f"{m.group(1).capitalize()} {m.group(2).lower()}{m.group(3)}".strip()
    return None

# other named substances: canonical -> regex
OTHERS = [
    ("Ketoanalogues of essential amino acids", r"keto[- ]?anal?og|ketoacid analog|alpha[- ]keto(?:acid)?\s+anal"),
    ("Essential amino acids", r"essential\s+amino\s+acid"),
    ("Omega-3 fatty acids (fish oil)", r"fish\s+oil|omega[- ]?3|\bepa\b|\bdha\b|eicosapentaen|docosahexaen|krill|salmon\s+oil|omego"),
    ("Gamma-linolenic acid", r"gamma[- ]linolenic|\bgla\b|evening\s+primrose|borage"),
    ("Alpha-lipoic acid", r"alpha[- ]?lipoic|thioctic|\bala\b"),
    ("Coenzyme Q10", r"co-?enzyme\s*q\s*10|coq10|ubiquin|ubidecarenone"),
    ("N-acetylcysteine", r"n-?acetyl[- ]?(?:l-)?cysteine|\bnac\b"),
    ("Glutathione", r"glutathione"),
    ("Collagen", r"collagen"),
    ("L-carnitine", r"carnitine"),
    ("Creatine", r"creatine"),
    ("Whey protein", r"whey"),
    ("Glucosamine", r"glucosamine"),
    ("Chondroitin", r"chondroitin"),
    ("Palmitoylethanolamide", r"palmitoylethanolamide|\bpea\b"),
    ("Lutein", r"lutein"),
    ("Melatonin", r"melatonin"),
    ("Chlorophyll", r"chlorophyll"),
    ("Lecithin / phosphatidylcholine", r"lecithin|phosphatidylcholine"),
    ("Inulin", r"inulin"),
    ("Fructooligosaccharides", r"fructo-?oligosacchar|\bfos\b"),
    ("Galactooligosaccharides", r"galacto-?oligosacchar|\bgos\b"),
    ("Glucomannan", r"glucomannan|konjac"),
    ("Resistant dextrin", r"resistant\s+dextrin|indigestible\s+maltodextrin|polydextrose"),
    ("Dietary fiber", r"\bfib(?:er|re)s?\b"),
    ("Diosmin", r"diosmin"),
    ("Hesperidin", r"hesperidin"),
    ("Quercetin", r"quercetin"),
    ("Resveratrol", r"resveratrol"),
    ("Astaxanthin", r"astaxanthin"),
    ("Uridine monophosphate", r"uridine"),
    ("Nicotinamide mononucleotide", r"\bnmn\b|nicotinamide\s+mononucleotide"),
    ("Alpha-ketoglutarate", r"alpha[- ]?keto[- ]?glutar"),
    ("Medium-chain triglycerides", r"\bmct\b|caprylic|capric"),
    ("Conjugated linoleic acid", r"conjugated\s+linoleic|\bcla\b"),
    ("Raspberry ketone", r"raspberry\s+ketone"),
]
_OTH = [(c, re.compile(rx, re.I)) for c, rx in OTHERS]

AMINO_RX = re.compile(r"\bl-[a-z]+|amino\s+acid|arginine|glutamine|lysine|taurine|leucine|\bbcaa\b|protein|peptide|"
                      r"collagen|glutathione|carnitine|creatine|whey|cysteine|aspartate|ornithine|citrulline|glycine", re.I)
FIBER_RX = re.compile(r"\bfib(?:er|re)s?\b|inulin|oligosacchar|\bfos\b|\bgos\b|psyllium|ispaghula|glucomannan|konjac|prebiotic|"
                      r"resistant\s+dextrin|maltodextrin|polydextrose|beta[- ]glucan|pectin|guar", re.I)
HERB_RX = re.compile(r"extract|\bherb|leaf|leaves|\broot|\bbark|\bseed|\bflower|\bfruit|\bberr|botanical|plant|mushroom|algae", re.I)
LATIN_RX = re.compile(r"\b([A-Z][a-z]{3,})\s+([a-z]{4,}(?:-[a-z]+)?)\b")

DOSE_RX = re.compile(r"\b\d[\d.,]*\s*(?:mg|mcg|µg|g|iu|i\.u\.|ml|%|billion|million|b\s*cfu|cfu|units?)\b[^,+&;]*", re.I)
TAIL_RX = re.compile(
    r"\b(?:(?:herbal\s+)?(?:food|dietary|nutritional)\s+supplement|probiotics?\s+(?:food\s+)?supplement|"
    r"herbal\s+supplement|supplement\s+(?:capsule|tablet)s?)\b.*$", re.I)
GENERIC_WORDS = re.compile(r"^(?:probiotics?|probiotic\s+blend|blend|\d+\s+probiotic\s+strains?|complex|proprietary\s+blend|"
                           r"vitamins?|minerals?|herbal\s+blend|herbal\s+extracts?|extracts?|formula|multi[- ]herb\s+formula)$", re.I)

def split_top(s, seps=r",|;|\+|&|\band\b|\bwith\b|/(?!\s*\d)"):
    """Split on separators that are not inside parentheses."""
    out, buf, depth = [], "", 0
    i = 0
    rx = re.compile(seps, re.I)
    while i < len(s):
        c = s[i]
        if c in "([":
            depth += 1
        elif c in ")]":
            depth = max(0, depth - 1)
        if depth == 0:
            m = rx.match(s, i)
            if m and m.end() > i:
                # "and"/"with" only as whole words (regex guarantees \b)
                out.append(buf); buf = ""; i = m.end(); continue
        buf += c
        i += 1
    out.append(buf)
    return [ws(x) for x in out if ws(x)]

def ingredient_text(clean):
    """The ingredient part of the cleaned product name (before the 'FOOD SUPPLEMENT CAPSULE' tail)."""
    t = TAIL_RX.sub("", clean)
    t = re.sub(r"\b(?:soft\s*gel(?:atin)?|hard\s*gel(?:atin)?|film[- ]coated|chewable|effervescent)?\s*"
               r"(?:capsules?|tablets?|softgels?|caplets?|powder|sachets?|gummies|jelly|liquid|syrup|drops)\s*$", "", t, flags=re.I)
    return ws(t).strip(" -,;")

def normalize_one(p):
    """Map one raw ingredient fragment to (canonical name, kind) where kind in probiotic|botanical|vitamin|mineral|other|raw."""
    raw = ws(DOSE_RX.sub(" ", p)).strip(" -,.;:")
    raw = re.sub(r"\(\s*\)", "", raw).strip()
    if not raw or len(raw) < 2:
        return None
    s = norm_strain(raw)
    if s:
        return s, "probiotic"
    low = raw.lower()
    for c, rx in _OTH:
        if rx.search(low):
            return c, "other"
    for c, l, rx in _BOT:
        if rx.search(low):
            return f"{c} ({l})", "botanical"
    for c, rx in _VIT:
        if rx.search(low):
            return c, "vitamin"
    m = MINERAL_RX.search(low)
    if m and len(low.split()) <= 4:
        word = (m.group(1) or ("iron" if re.search("ferr", low) else "minerals")).lower()
        return word.capitalize(), "mineral"
    # Latin binomial left as is (e.g. "Hylocereus undatus")
    mm = LATIN_RX.search(fold(raw).title().replace(" Extract", "")) if raw.isupper() else LATIN_RX.search(raw)
    t = raw if not raw.isupper() else raw.capitalize()
    t = re.sub(r"\s+", " ", t)
    return t[:80], "raw"

def parse_ingredients(clean):
    text = ingredient_text(clean)
    parts = []
    for p in split_top(text):
        inner = re.search(r"\(([^()]*[,+&][^()]*)\)", p)
        outer = ws(re.sub(r"\([^()]*\)", " ", p))
        if inner and (GENERIC_WORDS.match(outer) or not outer or re.search(r"blend|probiotic|strain|complex", outer, re.I)):
            parts.extend(split_top(inner.group(1)))
        else:
            parts.append(p)
    out, kinds = [], []
    for p in parts:
        r = normalize_one(p)
        if not r:
            continue
        name, kind = r
        if GENERIC_WORDS.match(name) and len(parts) > 1:
            continue
        if name.lower() not in [x.lower() for x in out]:
            out.append(name); kinds.append(kind)
    if not out:  # only generic words ("VITAMINS AND MINERALS", "MULTI-HERB FORMULA")
        for p in parts:
            r = normalize_one(p)
            if r and r[0].lower() not in [x.lower() for x in out]:
                out.append(r[0]); kinds.append(r[1])
    return out, kinds, text

def categories_of(text, ingredients, kinds):
    t = (text + " " + " ".join(ingredients)).lower()
    cats = []
    if "probiotic" in kinds or re.search(PROBIOTIC_GENERA, t):
        cats.append("probiotic")
    if "botanical" in kinds or (HERB_RX.search(t) and "raw" in kinds):
        cats.append("herbal/botanical")
    if "vitamin" in kinds or "mineral" in kinds or re.search(r"vitamin|multivitamin", t):
        cats.append("vitamin/mineral")
    if re.search(r"omega[- ]?3|fish oil|\bepa\b|\bdha\b|krill|salmon oil|omego", t):
        cats.append("omega-3")
    if re.search(r"keto[- ]?anal?og", t):
        cats.append("ketoanalogue")
    if AMINO_RX.search(t) and "ketoanalogue" not in cats:
        cats.append("amino acid/protein")
    if FIBER_RX.search(t) and not re.search(r"maltodextrin", t) or re.search(r"prebiotic|inulin|oligosacch|psyllium", t):
        cats.append("fiber/prebiotic")
    return cats or ["other"]

# ─────────────────────────────────────────────────────────────────────────────
# Kidney-marketed flag
# ─────────────────────────────────────────────────────────────────────────────
# Brands Dr. Rivero named, plus common PH kidney-marketed supplement brands.
CURATED_KIDNEY = ["renadyl", "renakult", "cudo", "cudo forte", "renalin", "venamax", "flavos", "probiorenal", "renoprotect",
                  "renoprime", "renoaid", "nephriclear", "trinephron", "neprisafe", "renalsia", "renalcare", "renosafe", "renomax",
                  "renalof", "nephrolit", "renochlor", "equirenal", "kidneylife", "kidneypro", "kidnycare", "renalite", "uniherb kidney care",
                  "royale kidney complex", "finamin nephro", "fin-montabon", "renivra"]
NOT_KIDNEY = re.compile(r"vrenala|prenal|(?:white\s+)?kidney\s+(?:beans?|extract)|gokidneybean", re.I)
KIDNEY_NAME = re.compile(r"kidn?ey|renal|\breno|\brena|\brenbio|\brenpro|nephr|\buric\b|\buric\s*acid|\buric|urinar|dialysis|\bkidny", re.I)

# Herbs sold in the Philippines for kidney stones or "kidney cleansing" (not P. emblica/amla or P. amarus)
KIDNEY_HERBS = re.compile(r"phyll?anth?us\s+(?:niruri|urinaria)|chanca\s+piedra|stone\s*breaker|sambong|blumea|orthosiphon|balbas[- ]?pusa|cat'?s\s+whisker", re.I)

def kidney_flag(brand, clean, ingredients):
    b = fold(brand).lower()
    if any(re.search(r"(?<![a-z])" + re.escape(c) + r"(?![a-z])", b) for c in CURATED_KIDNEY):
        return True, "curated brand list"
    bb = NOT_KIDNEY.sub(" ", b)
    if KIDNEY_NAME.search(bb):
        return True, "brand name"
    pn = NOT_KIDNEY.sub(" ", fold(clean).lower())
    if re.search(r"\bkidney\b|\brenal|dialysis|urinary|\buric\b|\bnephr", pn):
        return True, "product name"
    if any(i.startswith("Ketoanalogues") for i in ingredients) or re.search(r"keto[- ]?anal?og", pn):
        return True, "ketoanalogue"
    if KIDNEY_HERBS.search(pn) or any(KIDNEY_HERBS.search(i) for i in ingredients):
        return True, "kidney-associated herb"
    return False, ""

# ─────────────────────────────────────────────────────────────────────────────
NOT_SUPP = re.compile(r"\b(?:wine|beer|liquor|vodka|whisk(?:e)?y|rum|gin|soda|coffee|tea|juice|candy|chocolate|snack|chips|"
                      r"cookies?|biscuits?|cereal|noodles?|sauce|vinegar|milk\s+drink|drink\s+mix)\b", re.I)

def is_supplement(rec, clean):
    pn = (rec.get("PRODUCT_NAME") or "").upper()
    if "RAW MATERIAL" in (rec.get("TYPE_FOOD_PRODUCT_LABEL") or "").upper():
        return False, "raw material"
    if "SUPPLEMENT" not in pn:
        return False, "not a food supplement"
    # "RENAL NUTRITIONAL LIQUID SUPPLEMENT" and "... DRINK MIX ... FOOD SUPPLEMENT" stay; wine/beer never
    if re.search(r"\b(?:wine|beer|liquor|vodka|whisk(?:e)?y)\b", pn, re.I):
        return False, "not a food supplement"
    return True, ""

STATED_SUPP_RX = re.compile(r"\b(?:FOOD|FODD|DIETARY|HERBAL|BOTANICAL)\s+(?:[A-Z]+\s+)?SUPPLEMENTS?\b|"
                            r"\bSUPPLEMENTS?\s+(?:CAPSULES?|TABLETS?|SOFT\s*GELS?|CAPLETS?)\b", re.I)

def is_stated_supplement(raw):
    """The registration says it is a food supplement: 'FOOD SUPPLEMENT', 'DIETARY SUPPLEMENT', 'HERBAL SUPPLEMENT',
    'FOOD LIQUID SUPPLEMENT', '... SUPPLEMENT CAPSULE', or the 'no approved therapeutic claims' statement. 'MILK SUPPLEMENT',
    'NUTRITIONAL SUPPLEMENT DRINK', 'SUPPLEMENTARY FOOD/SNACKS' and 'LIPID-BASED NUTRIENT SUPPLEMENT' are not."""
    return bool(STATED_SUPP_RX.search(raw or "") or re.search(r"no\s+approved\s+therapeutic", raw or "", re.I))

# ─────────────────────────────────────────────────────────────────────────────
# Brand families: registrations of one brand filed under variant names, merged onto one page
# ─────────────────────────────────────────────────────────────────────────────
FAMILIES_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "supplement_brand_families.json")

def load_families(path=FAMILIES_FILE):
    """{main slug: {"name": display name or None, "members": [slug, ...]}} from supplement_brand_families.json."""
    if not os.path.exists(path):
        return {}
    raw = json.load(open(path, encoding="utf-8")).get("families") or {}
    out = {}
    for main, v in raw.items():
        if isinstance(v, list):
            v = {"members": v}
        out[slugify(main)] = {"name": v.get("name"), "members": [slugify(m) for m in v.get("members") or [] if slugify(m) != slugify(main)]}
    return out

def apply_families(products, families):
    """Move each member slug's products onto its main slug. Returns {retired slug: main slug}."""
    member_of = {m: main for main, f in families.items() for m in f["members"]}
    retired = {}
    for p in products:
        main = member_of.get(p["brand_slug"])
        if main or p["brand_slug"] in families:
            p.setdefault("brand_registered", p["brand"])
        if main:
            retired[p["brand_slug"]] = main
            p["brand_slug"] = main
    for main, f in families.items():
        ps = [p for p in products if p["brand_slug"] == main]
        if not ps:
            continue
        name = f.get("name")
        if not name:  # the main slug's own registered name, mixed case preferred
            own = Counter(p["brand_registered"] for p in ps if slugify(p["brand_registered"]) == main) or Counter(p["brand"] for p in ps)
            name = sorted(own, key=lambda n: (n.isupper(), -own[n], n))[0]
        for p in ps:
            p["brand"] = name
    return retired

# ─────────────────────────────────────────────────────────────────────────────
# Foods for special medical purposes (FSMP)
# ─────────────────────────────────────────────────────────────────────────────
FSMP_RX = re.compile(r"SPECIAL\s+MEDICAL\s+PURPOSE|\bFSMP\b|\bENTERAL\b|MEDICAL\s+NUTRITION", re.I)
RENAL_RX = re.compile(r"renal|kidney(?!\s*beans?)|dialy|nephr|\besrd\b|\bckd\b", re.I)
PEDIA_RX = re.compile(r"infant|child|\bmonths\b|years?\s+old|\d\s*-\s*\d+\s*years|pedia|toddler|faltering\s+growth", re.I)
FSMP_TAGS = ["renal", "diabetes", "high-protein", "peptide", "pediatric", "general"]
FLAVORS = ["milky vanilla", "vanilla caramel", "vanilla", "chocolate", "cappuccino", "strawberry", "white grape", "tropical fruit",
           "tropical mix", "tropical", "peach tea", "japanese rice", "orange", "banana", "lemon", "coffee", "caramel", "wheat",
           "milk", "neutral", "unflavored", "plain"]
FLAVOR_RX = re.compile(r"\b(" + "|".join(re.escape(f) for f in FLAVORS) + r")(?=\s*(?:flavou?r|flavored|\b-|\)|$|,|\s+[-–]))|"
                       r"flavou?r(?:ed)?\s*[-:(]?\s*(" + "|".join(re.escape(f) for f in FLAVORS) + r")\b", re.I)

def is_fsmp(rec):
    return bool(FSMP_RX.search(rec.get("PRODUCT_NAME") or ""))

FSDU_RX = re.compile(r"SPECIAL\s+DIETARY", re.I)
MEDFOOD = ("fsmp", "fsdu")

def is_fsdu(rec):
    """FOOD(S) FOR SPECIAL DIETARY USE(S), 'SPECIAL DIETARY POWDER DRINK MIX', 'FOOD FOR SPECIAL DIETARY MANAGEMENT'."""
    return bool(FSDU_RX.search(rec.get("PRODUCT_NAME") or "")) and not is_fsmp(rec)

def _balance(t):
    """Drop unmatched parentheses."""
    out, stack = list(t), []
    for i, c in enumerate(t):
        if c == "(":
            stack.append(i)
        elif c == ")":
            if stack:
                stack.pop()
            else:
                out[i] = ""
    for i in stack:
        out[i] = ""
    return ws("".join(out))

FSMP_PHRASE = re.compile(r"\(?\s*(?:foods?|formula|powder)?\s*(?:for\s+)?special\s+(?:medical\s+purposes?|dietary\s+uses?)\s*\)?", re.I)

def fsmp_use(raw):
    """The registered 'for the dietary management of …' text, cleaned to lower case."""
    m = re.search(r"for\s+(?:the\s+)?dietary\s+management\s+(?:of\s+|in\s+)?(.*)", raw, re.I)
    if m:
        t = m.group(1)
    else:  # "… FOOD FOR SPECIAL MEDICAL PURPOSES WITH HIGH PROTEIN FOR RENAL INSUFFICIENCY IN DIALYSIS STAGE"
        m = re.search(r"\bfor\s+((?:renal|kidney|patients|people|persons|individuals|diabetics|infants|chronic|children|young)\b.*)",
                      FSMP_PHRASE.sub(" ", raw), re.I)
        t = m.group(1) if m else ""
    t = FSMP_PHRASE.sub(" ", t)
    fl = "|".join(re.escape(f) for f in FLAVORS)
    t = re.sub(r"\s*[-–]?\s*(?:\b(?:" + fl + r")\b\s*)+(?:flavou?r(?:ed)?)?\s*\)?\s*$", "", ws(t), flags=re.I)
    t = re.sub(r"\s*[-–]\s*(?:[a-z ]+\s+)?flavou?r.*$|\s*[-–]\s*\d+\s*g\b.*$|\s*[-–]\s*reformulated.*$", "", t, flags=re.I)
    t = _balance(ws(t).strip(" -–,;:"))
    t = t.strip(" -–,;:")
    if not t:
        return None
    t = t.lower()
    for a in ("ckd", "esrd", "gi", "aki", "g.i."):
        t = re.sub(rf"(?<![a-z]){re.escape(a)}(?![a-z])", a.upper(), t)
    return t[:200]

def use_label(raw, use):
    """The registered use as a sentence: 'For the dietary management of …' when the record says so, else 'For …'."""
    if not use:
        return None
    if re.search(r"dietary\s+management", raw, re.I):
        return "For the dietary management of " + use
    return "For " + use

def fsmp_flavor(raw):
    m = FLAVOR_RX.search(raw)
    if not m:
        return None
    return (m.group(1) or m.group(2)).capitalize()

def fsmp_variant(brand, raw, brand_only=False):
    """'LP' (lower protein, CKD not on dialysis) or 'HP' (higher protein, dialysis) for renal formulas.
    brand_only (FSDU): only an LP/HP label in the brand counts; the stage wording is not read as a protein variant."""
    b, t = brand.upper(), ("" if brand_only else raw.upper())
    if re.search(r"\bLP\b|LOWER\s+PROTEIN|LOW\s+PROTEIN", b):
        return "LP"
    if re.search(r"\bHP\b|HIGH(?:ER)?\s+PROTEIN|-\s*D\b", b):
        return "HP"
    if re.search(r"NOT\s+REQUIRING\s+DIALYSIS|PRE-?\s*DIALYSIS|LOW(?:ER)?\s+PROTEIN|STAGES?\s+1\s*(?:TO|-)\s*[45]\b", t):
        return "LP"
    if re.search(r"HIGH(?:ER)?\s+PROTEIN|ON\s+DIALYSIS|UNDERGOING\s+DIALYSIS|UNDER\s+DIALYSIS|REQUIRING\s+DIALYSIS|"
                 r"DIALYSIS\s+STAGE|\(DIALYSIS\)|STAGE\s+5\b|END\s+STAGE", t):
        return "HP"
    return None

def fsmp_tags(brand, raw, brand_only=False):
    t = brand + " " + raw
    tags = []
    if RENAL_RX.search(t):
        tags.append("renal")
    if re.search(r"diabet|glucose|glycemic|blood\s+sug", t, re.I):
        tags.append("diabetes")
    ped = bool(PEDIA_RX.search(raw))
    if re.search(r"high(?:er)?\s+protein|increased\s+protein|protein\s+content|loss\s+of\s+muscle", t, re.I) or \
            ("renal" in tags and fsmp_variant(brand, raw, brand_only) == "HP") or (re.search(r"\bHP\b", brand) and not ped):
        tags.append("high-protein")
    if re.search(r"peptide", t, re.I):
        tags.append("peptide")
    if ped:
        tags.append("pediatric")
    return tags or ["general"]

def fsmp_family(brand):
    """Product-line name with the renal variant suffix removed (Nepro HP -> Nepro, Nephrisol-D -> Nephrisol)."""
    b = re.sub(r"\s*\(?\s*(?:LOWER|HIGHER|LOW|HIGH)\s+PROTEIN\s*\(?\s*(?:LP|HP)?\s*\)?\s*$", "", brand, flags=re.I)
    b = re.sub(r"[\s-]*\(?\b(?:LP|HP)\)?\s*$", "", b, flags=re.I)
    b = re.sub(r"(?<=[A-Za-z])-D$", "", b)
    return ws(b).strip(" -") or brand

SHARD_MAX = int(4.5 * 1024 * 1024)

def brand_display(b):
    b = ws(fold(re.sub(r"[®™©]|\(R\)|\(TM\)", " ", b or "")))
    return b.strip(" -.,")

def group_fsmp(products):
    """One page per renal product line: strip LP/HP/-D suffixes; a brand that holds both renal and non-renal FSMP
    registrations (Fresubin) gets its renal line as '<brand> Renal'. Display name prefers the mixed-case spelling."""
    fs = [p for p in products if p.get("type") in MEDFOOD]
    base = defaultdict(list)
    for p in fs:
        base[slugify(p["brand"])].append(p)
    mixed = {b for b, ps in base.items() if any(p.get("renal_formula") for p in ps) and any(not p.get("renal_formula") for p in ps)}
    fam = defaultdict(list)
    for p in fs:
        if not p.get("renal_formula"):
            continue
        name = fsmp_family(p["brand"])
        if slugify(p["brand"]) in mixed and not RENAL_RX.search(name):
            name = name + (" RENAL" if name.isupper() else " Renal")
        p["brand"] = name
        fam[slugify(name)].append(p)
    for slug, ps in fam.items():
        names = Counter(p["brand"] for p in ps)
        pick = sorted(names, key=lambda n: (n.isupper(), -names[n], n))[0]
        for p in ps:
            p["brand"], p["brand_slug"] = pick, slug

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--supp-file", required=True, help="ph-fda-supplements.json or ph-fda-supplements-sample.json")
    ap.add_argument("--out-dir", default=os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "..", "data", "drugs"))
    ap.add_argument("--as-of", help="YYYY-MM-DD for the validity check (default today)")
    a = ap.parse_args()
    today = dt.date.fromisoformat(a.as_of) if a.as_of else dt.date.today()
    src = json.load(open(a.supp_file, encoding="utf-8"))
    recs = list(src.values()) if isinstance(src, dict) else list(src)

    products, excluded = [], defaultdict(list)
    for r in recs:
        rid = ws(r.get("ACCOUNTCODE"))
        if not rid:
            continue
        raw = ws(r.get("PRODUCT_NAME"))
        clean = clean_product_name(raw)
        brand = brand_display(r.get("BRAND_NAME"))
        raw_mat = "RAW MATERIAL" in (r.get("TYPE_FOOD_PRODUCT_LABEL") or "").upper()
        kind = "fsmp" if (is_fsmp(r) and not raw_mat) else "fsdu" if (is_fsdu(r) and not raw_mat) else "supplement"
        if kind == "supplement" and not is_stated_supplement(raw):
            kind = "other"              # food registration with no supplement statement (milk supplement, nutrition drink, RUSF, snack)
        fsmp = kind in MEDFOOD          # FSMP or FSDU: registered use + tags, no ingredient parsing
        ok, why = (True, "") if fsmp else is_supplement(r, clean)
        valid = parse_date(r.get("DATE_VALIDITY"))
        app = ws(r.get("APPLICATION_TYPE_LABEL"))
        canceled = (ws(r.get("IS_CANCELED")).upper() == "Y") or bool(re.search(r"cancel", app, re.I))
        reason = None
        if not ok:
            reason = why
        elif canceled:
            reason = "canceled"
        elif ws(r.get("LOW_RISK_DECISION")) and ws(r.get("LOW_RISK_DECISION")).lower() != "approved":
            reason = "not approved"
        elif valid and valid < today:
            reason = "expired"
        if reason:
            excluded[reason].append({"id": rid, "brand": brand, "product_name": raw[:160],
                                     "valid_until": valid.isoformat() if valid else None})
            continue
        if fsmp:
            # the FDA record names the product type and its registered use, not a composition
            ings, kinds, ing_text = [], [], ""
            kflag, kwhy = False, ""
        elif kind == "other":
            # a food product name, not an ingredient list; kidney marketing is still flagged (Neprisafe)
            ings, kinds, ing_text = [], [], ""
            kflag, kwhy = kidney_flag(brand, clean, ings)
        else:
            ings, kinds, ing_text = parse_ingredients(clean)
            kflag, kwhy = kidney_flag(brand, clean, ings)
        dname = brand or ingredient_text(clean)[:60] or rid
        decision = parse_date(r.get("DENIAL_DATE"))
        p = {
            "id": rid,
            "brand": dname,
            "brand_slug": slugify(dname) or slugify(rid),
            "product_name": raw,
            "product_name_clean": clean,
            "ingredients": ings,
            "ingredients_raw": ing_text,
            "form": form_of(clean),
            "company": ws(r.get("COMPANY_NAME")).rstrip(" ,."),
            "valid_until": valid.isoformat() if valid else None,
            "decision_date": decision.isoformat() if decision else None,
            "canceled": False,
            "risk_type": ws(r.get("TYPE_FOOD_PRODUCT_LABEL")).replace(" Food Product", "") or None,
            "application_type": app or None,
            "no_therapeutic_claims": bool(re.search(r"no\s+approved\s+therapeutic", raw, re.I)),
            "categories": [kind] if fsmp else ["food"] if kind == "other" else categories_of(ing_text, ings, kinds),
            "kidney_marketed": kflag,
            "type": kind,
        }
        if fsmp:
            tags = fsmp_tags(brand, raw, kind == "fsdu")
            p["fsmp_tags"] = tags
            p["fsmp_use"] = fsmp_use(raw)
            p["use_label"] = use_label(raw, p["fsmp_use"])
            p["flavor"] = fsmp_flavor(raw)
            if "renal" in tags:
                p["renal_formula"] = True
                p["variant"] = fsmp_variant(brand, raw, kind == "fsdu")
        if kind == "other":
            u = fsmp_use(raw) if re.search(r"dietary\s+management|\bfor\s+(?:pregnant|patients|children|older\s+infants|adults?)\b", raw, re.I) else None
            if u:
                p["use_label"] = use_label(raw, u)
            fl = fsmp_flavor(raw)
            if fl:
                p["flavor"] = fl
        if kflag:
            p["kidney_reason"] = kwhy
        products.append(p)

    group_fsmp(products)
    retired = apply_families(products, load_families())

    # shards by first character of the brand slug
    sdir = os.path.join(a.out_dir, "supplements")
    os.makedirs(sdir, exist_ok=True)
    for f in os.listdir(sdir):
        if re.fullmatch(r"[a-z0][a-z0-9]?\.json", f):
            os.remove(os.path.join(sdir, f))
    # One shard per first character; a shard that would pass ~4.5 MB is split by the first two characters.
    first = defaultdict(list)
    for p in sorted(products, key=lambda p: (p["brand_slug"], p["id"])):
        c = p["brand_slug"][:1]
        first[c if c.isalpha() else "0"].append(p)
    shards = {}
    for c, lst in first.items():
        size = len(json.dumps(lst, ensure_ascii=False, separators=(",", ":")).encode("utf-8"))
        if size <= SHARD_MAX:
            shards[c] = lst
            continue
        for p in lst:
            k = (c + (p["brand_slug"][1:2] if p["brand_slug"][1:2].isalnum() else "0")) if c != "0" else "0"
            shards.setdefault(k, []).append(p)
    shard_of = {}
    for c, lst in shards.items():
        path = os.path.join(sdir, f"{c}.json")
        with open(path, "w", encoding="utf-8") as fh:
            json.dump(lst, fh, ensure_ascii=False, separators=(",", ":"))
        if os.path.getsize(path) > 5 * 1024 * 1024:
            print(f"  ! shard {c}.json exceeds 5 MB", file=sys.stderr)
        for p in lst:
            shard_of[p["brand_slug"]] = c

    brands = {}
    by = defaultdict(list)
    for p in products:
        by[p["brand_slug"]].append(p)
    for slug, ps in sorted(by.items()):
        names = Counter(p["brand"] for p in ps)
        brands[slug] = {
            "brand": names.most_common(1)[0][0],
            "shard": shard_of[slug],
            "ids": [p["id"] for p in ps],
            "companies": sorted({p["company"] for p in ps if p["company"]}),
            "forms": sorted({p["form"] for p in ps}),
            "categories": sorted({c for p in ps for c in p["categories"]}),
            "kidney_marketed": any(p["kidney_marketed"] for p in ps),
            "type": (lambda ts: ts.pop() if len(ts) == 1 else "mixed")({p.get("type", "supplement") for p in ps}),
            "types": dict(Counter(p.get("type", "supplement") for p in ps).most_common()),
        }
        aka = sorted({p["brand_registered"] for p in ps if p.get("brand_registered") and p["brand_registered"].lower() != brands[slug]["brand"].lower()})
        if aka:
            brands[slug]["aka"] = aka
        if any(p.get("renal_formula") for p in ps):
            brands[slug]["renal_formula"] = True
        tags = sorted({t for p in ps for t in p.get("fsmp_tags", [])}, key=FSMP_TAGS.index)
        if tags:
            brands[slug]["fsmp_tags"] = tags
        vs = sorted({p["variant"] for p in ps if p.get("variant")})
        if vs:
            brands[slug]["variants"] = vs
    counts = {"records_in": len(recs), "products": len(products), "brands": len(brands),
              "kidney_marketed_brands": sum(1 for b in brands.values() if b["kidney_marketed"]),
              "fsmp_products": sum(1 for p in products if p.get("type") == "fsmp"),
              "fsmp_brands": sum(1 for s, b in brands.items() if any(p.get("type") == "fsmp" for p in by[s])),
              "fsdu_products": sum(1 for p in products if p.get("type") == "fsdu"),
              "fsdu_brands": sum(1 for s, b in brands.items() if any(p.get("type") == "fsdu" for p in by[s])),
              "other_food_products": sum(1 for p in products if p.get("type") == "other"),
              "other_food_brands": sum(1 for s, b in brands.items() if any(p.get("type") == "other" for p in by[s])),
              "mixed_type_brands": sorted(s for s, b in brands.items() if len(b["types"]) > 1),
              "renal_fsmp_brands": sum(1 for b in brands.values() if b.get("renal_formula")),
              "fsmp_tags": dict(Counter(t for p in products for t in p.get("fsmp_tags", [])).most_common()),
              "excluded": {k: len(v) for k, v in sorted(excluded.items())},
              "categories": dict(Counter(c for p in products for c in p["categories"]).most_common()),
              "forms": dict(Counter(p["form"] for p in products).most_common())}
    index = {"as_of": today.isoformat(), "source": os.path.basename(a.supp_file),
             "source_note": "FDA Philippines food-product registrations (fdafoodproducts); DENIAL_DATE field read as the decision/issue date.",
             "counts": counts, "brands": brands, "retired": dict(sorted(retired.items()))}
    with open(os.path.join(a.out_dir, "supplements.json"), "w", encoding="utf-8") as fh:
        json.dump(index, fh, ensure_ascii=False, separators=(",", ":"))
    with open(os.path.join(sdir, "_report.json"), "w", encoding="utf-8") as fh:
        json.dump({"as_of": today.isoformat(), "counts": counts, "excluded": excluded,
                   "kidney_marketed": sorted(({"brand": b["brand"], "slug": s} for s, b in brands.items() if b["kidney_marketed"]),
                                             key=lambda x: x["brand"]),
                   "renal_formulas": sorted(({"brand": b["brand"], "slug": s, "variants": b.get("variants", [])}
                                             for s, b in brands.items() if b.get("renal_formula")), key=lambda x: x["brand"])}, fh, ensure_ascii=False, indent=1)
    print(json.dumps(counts, indent=1))

if __name__ == "__main__":
    main()
