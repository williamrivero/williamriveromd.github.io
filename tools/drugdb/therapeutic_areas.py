#!/usr/bin/env python3
"""Coarse therapeutic-area (body-system) grouping for the Drug Index "Browse by: Therapeutic area" view.

Transparent keyword rules, kept here as data so they are easy to edit. No WHO ATC data is used.
Each generic is described by its class text (US FDA Established Pharmacologic Class + mechanism of action when it has a
US label, else the de-duplicated FDA Philippines pharmacologic category), its name/ingredients and its dosage-form groups.

How a generic is assigned (first hit wins):
  1. PRE rules on the class text (vaccines, fluids/dialysis solutions, counterirritant liniments) — these override route.
  2. ROUTE rules: a generic registered only as eye/ear/nose products -> Eye & ENT; only topical -> Dermatology;
     only inhalation -> Respiratory.
  3. AREAS rules on the class text, in order.
  4. AREAS "name" keywords on the generic name and ingredients (for generics with no or vague class text).
  5. Otherwise "Other".

Usage as a script: python3 tools/drugdb/therapeutic_areas.py [--sample 30]  (reads drugs/search-index.json, prints
the share per area, the share in Other and a random sample of assignments for spot-checking).
"""
from __future__ import annotations

import re

VACCINES = "Vaccines & immunoglobulins"
FLUIDS = "Fluids, electrolytes & dialysis solutions"
CV = "Cardiovascular & renal"
ENDO = "Diabetes & endocrine"
INFECT = "Anti-infectives"
PAIN = "Analgesics & anti-inflammatories"
RESP = "Respiratory & allergy"
GI = "Gastrointestinal & hepatobiliary"
NEURO = "Neuro & psychiatric"
ONCO = "Oncology & immunomodulators"
BLOOD = "Blood, anemia & anticoagulation"
MSK = "Musculoskeletal & gout"
NUTR = "Vitamins, minerals & nutrition"
DERM = "Dermatology"
EYE = "Eye & ENT"
WOMEN = "Women's health & urology"
ANES = "Anesthesia & critical care"
DIAG = "Antidotes, diagnostics & contrast agents"
OTHER = "Other"

ORDER = [CV, ENDO, INFECT, PAIN, RESP, GI, NEURO, ONCO, BLOOD, MSK, NUTR, FLUIDS, DERM, EYE, WOMEN, VACCINES, ANES, DIAG, OTHER]

# 1. class-text rules that win over the route rules
PRE = [
    (VACCINES, r"vaccin|immune ser|immunoglobulin|immune globulin|antitoxin|antiven|antiserum|toxoid"),
    (FLUIDS, r"dialy|electrolyte|parenteral fluid|rehydration|irrigat|plasma expander|intravenous solution|"
             r"infusion solution|hemofiltration|haemofiltration|vehicle and solvent|cation[- ]exchange|potassium binder|phosphate binder|hyperkalemi|hyperphosphat"),
    (PAIN, r"counter ?irritant|rubefacient|topical analgesic"),
]

# 2. route rules (dosage-form groups from the search index)
ROUTE = [
    ({"eye/ear/nose"}, EYE),
    ({"topical"}, DERM),
    ({"inhalation"}, RESP),
]

# 3./4. ordered area rules: (area, class-text regex, name/ingredient regex)
AREAS = [
    (ONCO, r"antineoplas|kinase inhibitor|cytotoxic|chemotherap|alkylating|antimetabolite|aromatase|"
           r"programmed death|pd-1|pd-l1|cd20|her2|vegf|egfr|bcr-abl|mtor|proteasome|parp|antiandrogen|anti-androgen|"
           r"immunosuppress|calcineurin|interferon|immunostimul|immunomodul|monoclonal antibod|antibody drug|"
           r"interleukin|tumor necrosis factor|tnf|janus kinase|jak inhib|selective immunosuppress",
     r"mab$|mab\b|tinib|platin|taxel|rubicin|mustine|cyclophosphamide|methotrexate|tacrolimus|ciclosporin|"
     r"cyclosporine|mycophenol|azathioprine|sirolimus|everolimus|letrozole|anastrozole|tamoxifen|bicalutamide|"
     r"leuprorelin|goserelin|capecitabine|gemcitabine|fluorouracil|temozolomide|hydroxyurea|imatinib"),
    (BLOOD, r"antithromb|anticoag|platelet|heparin|thromboly|fibrinoly|hemosta|haemosta|antifibrinoly|coagulation|antihemorrhag|plasma fraction|"
            r"hematinic|anemi|anaemi|erythropoie|iron chelat|colony stimulat|thrombopoie|plasma protein|"
            r"blood substitute|factor xa|thrombin inhib|vitamin k antag|hematopoie",
     r"warfarin|heparin|parin$|clopidogrel|ticagrelor|prasugrel|aspirin|rivaroxaban|apixaban|dabigatran|edoxaban|"
     r"tranexamic|epoetin|darbepoetin|filgrastim|iron sucrose|ferric|ferrous|iron|deferasirox|deferoxamine|albumin|"
     r"alteplase|tenecteplase|streptokinase|cilostazol|dipyridamole|phytomenadione|vitamin k"),
    (VACCINES, r"vaccin|immunoglobulin", r"vaccine|immunoglobulin|immune globulin|toxoid"),
    (FLUIDS, r"dialy|electrolyte|rehydration|irrigat",
     r"dextrose|sodium chloride|ringer|potassium chloride|sodium bicarbonate|hemodialy|haemodialy|peritoneal|"
     r"sevelamer|lanthanum|patiromer|polystyrene sulfonate|calcium acetate|water for injection|mannitol|"
     r"oral rehydration|bicarbonate|hartmann|plasma-lyte|balanced salt"),
    (NUTR, r"vitamin|mineral|nutrition|amino acid|appetite|keto ?analog|dietary|supplement|trace element|"
           r"lipid emulsion|nutrient|tonic",
     r"vitamin|multivit|thiamine|pyridoxine|cyanocobalamin|methylcobalamin|folic|ascorbic|cholecalciferol|"
     r"colecalciferol|ergocalciferol|retinol|tocopherol|niacin|riboflavin|zinc|calcium|magnesium|selenium|"
     r"amino acid|ketoanalog|lysine|carnitine|omega|fish oil|lecithin|biotin|coenzyme|glutathione|collagen|"
     r"probiotic|lactobacillus|bacillus|saccharomyces"),
    (DIAG, r"contrast|diagnostic|radiopharm|antidote|chelating agent|reversal|tuberculin|detoxif",
     r"gadolinium|gado|iohexol|iopamidol|iodixanol|ioversol|iopromide|naloxone|flumazenil|acetylcysteine inj|"
     r"atropine|pralidoxime|methylene blue|sugammadex|neostigmine|protamine|tuberculin|fluorescein|indocyanine"),
    (ANES, r"general anesth|general anaesth|local anesth|local anaesth|neuromuscular block|anesthetic|anaesthetic|"
           r"sedat.*icu|vasopressor|inotrop|catecholamine|sympathomimetic|surfactant|adjuvant to surgery",
     r"propofol|ketamine|sevoflurane|isoflurane|desflurane|etomidate|thiopental|lidocaine|bupivacaine|"
     r"ropivacaine|levobupivacaine|mepivacaine|rocuronium|vecuronium|atracurium|cisatracurium|succinylcholine|"
     r"suxamethonium|dexmedetomidine|midazolam|remifentanil|norepinephrine|noradrenaline|epinephrine|adrenaline|"
     r"dopamine|dobutamine|vasopressin|milrinone|poractant|beractant"),
    (INFECT, r"antibacter|antibiotic|cephalospor|penicillin|macrolide|quinolone|aminoglycoside|carbapenem|"
             r"tetracycline|antifung|antimycot|antivir|antiretrovir|\bhiv\b|reverse transcriptase|protease inhib|"
             r"integrase|nucleoside|antitubercul|anti-tubercul|antimalar|anthelmint|antiprotozo|antiparasit|"
             r"sulfonamide|lincosamide|glycopeptide|polymyxin|nitroimidazole|monobactam|oxazolidinone|"
             r"azole antifungal|antiinfective|anti-infective|antimicrob|beta-lactam|urinary antiseptic|"
             r"leprostatic|scabicide|pediculicide|antimycobact|tubercul|amebicid|anti-retrovir",
     r"cillin|cef|ceph|mycin|micin|cycline|floxacin|azole$|conazole|vir$|vir\b|penem|bactam|sulfamethoxazole|"
     r"trimethoprim|isoniazid|rifamp|ethambutol|pyrazinamide|metronidazole|tinidazole|albendazole|mebendazole|"
     r"praziquantel|ivermectin|chloroquine|artemether|primaquine|nitrofurantoin|fosfomycin|colistin|polymyxin|"
     r"terbinafine|nystatin|amphotericin|griseofulvin|linezolid|vancomycin|teicoplanin|dapsone|fungin"),
    (CV, r"angiotensin|ace inhib|converting enzyme|\barb\b|beta[- ]?block|beta-adrenergic block|calcium channel|"
         r"diuretic|antihypertens|nitrate vasodil|antiangin|anti-angin|antiarrhythm|cardiac glycoside|hmg[- ]?coa|"
         r"statin|lipid|hyperlipid|cholesterol|fibrate|vasodilat|endothelin|pulmonary arterial|neprilysin|renin|"
         r"cardiovascular|cardiac|heart failure|potassium[- ]sparing|aldosterone|mineralocorticoid receptor|"
         r"sinus node|peripheral vasc|venotonic|vasoprotect|capillary stabil|centrally acting antiadrenergic|"
         r"alpha-?2|cardiotonic|ezetimibe|pcsk9|kidney|renal|carbonic anhydrase",
     r"sartan|pril$|pril\b|olol|dipine|statin|thiazide|furosemide|torsemide|bumetanide|spironolactone|eplerenone|"
     r"finerenone|amiodarone|digoxin|nitroglycerin|isosorbide|trimetazidine|ivabradine|sacubitril|hydralazine|"
     r"methyldopa|clonidine|minoxidil|indapamide|diltiazem|verapamil|ranolazine|fenofibrate|gemfibrozil|"
     r"ezetimibe|diosmin|hesperidin|sildenafil|bosentan|ambrisentan|macitentan|riociguat|doxazosin|prazosin|"
     r"terazosin|nicorandil|molsidomine|ketoanalog"),
    (ENDO, r"insulin|glucose[- ]lowering|hypoglyc|antidiabet|biguanide|sulfonylurea|dpp-?4|dipeptidyl|sglt|"
           r"glp-?1|glucagon|thiazolidinedione|thyroid|antithyroid|corticosteroid|glucocorticoid|mineralocorticoid|"
           r"growth hormone|somatostatin|vasopressin analog|calcimimetic|parathyroid|androgen|anabolic|"
           r"adrenal|pituitary|hormone|alpha-glucosidase|incretin|blood glucose|ppar|vasopressin|obesity",
     r"metformin|gliptin|gliflozin|glutide|glimepiride|gliclazide|glibenclamide|glipizide|pioglitazone|acarbose|"
     r"insulin|levothyroxine|methimazole|thiamazole|propylthiouracil|carbimazole|prednisone|prednisolone|"
     r"methylprednisolone|dexamethasone|hydrocortisone|betamethasone|fludrocortisone|cinacalcet|calcitriol|"
     r"paricalcitol|alfacalcidol|doxercalciferol|testosterone|desmopressin|octreotide|somatropin"),
    (RESP, r"bronchodil|beta-?2|β2|adrenergic agonist|antiasthm|leukotriene|mucolytic|expectorant|antitussive|"
           r"cough|decongest|antihistamine|anti-allerg|antiallerg|xanthine|methylxanthine|respiratory|"
           r"histamine-1|h1 receptor|histamine h1|mast cell stabil|common cold|cold preparation|airway|angioedema",
     r"salbutamol|albuterol|terbutaline|salmeterol|formoterol|tiotropium|ipratropium|budesonide|fluticasone|"
     r"montelukast|theophylline|doxofylline|aminophylline|ambroxol|carbocisteine|bromhexine|guaifenesin|"
     r"dextromethorphan|butamirate|lagundi|cetirizine|loratadine|fexofenadine|chlorphenamine|chlorpheniramine|"
     r"diphenhydramine|phenylephrine|phenylpropanolamine|pseudoephedrine|acetylcysteine|erdosteine|"
     r"levodropropizine|cloperastine|ketotifen|desloratadine|bilastine|rupatadine|hydroxyzine"),
    (GI, r"proton pump|h2[- ]?receptor|h2 antag|antacid|laxative|cathartic|antidiarr|anti-diarr|antiemetic|"
         r"anti-emetic|antispasmod|prokinetic|antiflatul|carminative|hepato|liver|bile|biliary|cholelith|"
         r"digestive|gastro|anti-reflux|antireflux|antihemorrhoid|haemorrhoid|hemorrhoid|ulcer|pancrea|enzyme|"
         r"intestinal|bowel|stool soft|lipase inhib|hepat|cholesta|acid blocker|p-cab|enterokinetic|alimentary",
     r"prazole|tidine$|ranitidine|famotidine|sucralfate|misoprostol|domperidone|metoclopramide|ondansetron|"
     r"granisetron|palonosetron|loperamide|racecadotril|bisacodyl|senna|sennoside|lactulose|psyllium|"
     r"simethicone|simeticone|hyoscine|butylbromide|dicycloverine|mebeverine|ursodeoxycholic|silymarin|"
     r"lactulose|alginate|aluminum hydroxide|magnesium hydroxide|polyethylene glycol|macrogol|mesalazine|"
     r"sulfasalazine|pancreatin|orlistat|ornithine|rifaximin|trimebutine|otilonium|pinaverium|itopride"),
    (NEURO, r"antiepilep|anticonvuls|antidepress|antipsych|anxiolyt|hypnotic|sedative|benzodiazep|antiparkins|"
            r"dopamine agonist|dementia|cholinesterase|nootropic|neurotonic|neuroprotect|migraine|triptan|"
            r"cns stimulant|central nervous|adhd|attention deficit|psychostim|mood stabil|antivertig|vertigo|"
            r"smoking cessation|opioid antagonist|neuropath|serotonin reuptake|snri|ssri|monoamine|"
            r"gaba|parkins|dopaminergic|anti-?depress|orexin|nicotine|cerebral|peripheral nerv|nerve",
     r"levetiracetam|valproic|valproate|carbamazepine|oxcarbazepine|phenytoin|lamotrigine|topiramate|"
     r"gabapentin|pregabalin|sertraline|fluoxetine|escitalopram|citalopram|paroxetine|venlafaxine|duloxetine|"
     r"mirtazapine|amitriptyline|quetiapine|olanzapine|risperidone|aripiprazole|haloperidol|clozapine|"
     r"lithium|alprazolam|diazepam|clonazepam|lorazepam|zolpidem|levodopa|pramipexole|ropinirole|donepezil|"
     r"memantine|rivastigmine|galantamine|citicoline|piracetam|cinnarizine|betahistine|flunarizine|"
     r"methylphenidate|sumatriptan|ergotamine|cerebrolysin|vinpocetine|ginkgo|methylcobalamin"),
    (PAIN, r"analgesic|antipyretic|nsaid|non-?steroidal anti|cox-?2|coxib|opioid|anti-inflammatory|"
           r"antiinflammatory|prostaglandin synthesis|cyclooxygenase",
     r"paracetamol|acetaminophen|ibuprofen|mefenamic|diclofenac|naproxen|ketorolac|celecoxib|etoricoxib|"
     r"meloxicam|piroxicam|tenoxicam|aceclofenac|nimesulide|indometacin|indomethacin|tramadol|morphine|"
     r"fentanyl|codeine|oxycodone|nalbuphine|tapentadol|ketoprofen|flurbiprofen|metamizole|dexketoprofen|"
     r"methyl salicylate|menthol|camphor|capsaicin|salicylate|eperisone|serratiopeptidase|bromelain"),
    (MSK, r"muscle relax|skeletal muscle|gout|antigout|anti-gout|uric|xanthine oxidase|osteopor|bisphosphon|"
          r"antirheumat|dmard|disease-modifying|chondro|calcitonin|bone|rank ligand|joint|arthrit|"
          r"uricosur|antihyperuric|urate|musculo-?skeletal",
     r"allopurinol|febuxostat|colchicine|probenecid|benzbromarone|alendronate|risedronate|ibandronate|"
     r"zoledronic|denosumab|teriparatide|raloxifene|glucosamine|chondroitin|diacerein|hydroxychloroquine|"
     r"leflunomide|orphenadrine|baclofen|tizanidine|methocarbamol|tolperisone|cyclobenzaprine|thiocolchicoside|"
     r"strontium|calcitonin|hyaluron"),
    (DERM, r"acne|keratolyt|emollient|psoria|antipruritic|anti-pruritic|dermatolog|skin|antiseptic|disinfectant|"
           r"wound|cicatri|sunscreen|depigment|hair|retinoid|wart|eczema|dermatitis|antiperspirant|"
           r"topical corticosteroid|topical|scar|hyperpigment|whitening|moisturi",
     r"hydroquinone|tretinoin|adapalene|benzoyl peroxide|isotretinoin|clobetasol|mometasone|betamethasone val|"
     r"hydrocortisone acetate|calcipotriol|salicylic acid|urea|zinc oxide|silver sulfadiazine|mupirocin|"
     r"fusidic|povidone|chlorhexidine|alcohol|hydrogen peroxide|minoxidil topical|permethrin|lindane|"
     r"tacalcitol|coal tar|sulfur|sulphur|petrolatum|lanolin|allantoin|azelaic|niacinamide topical|cetrimide|"
     r"triclosan|hexachlorophene|benzalkonium|iodine|centella|aloe"),
    (EYE, r"ophthalm|glaucom|eye|ocular|anticataract|mydria|miotic|antineovascular|otic|\bear\b|nasal|"
          r"artificial tear|lubricant|intravitreal|retina",
     r"timolol|latanoprost|travoprost|bimatoprost|brimonidine|dorzolamide|brinzolamide|pilocarpine|"
     r"tropicamide|cyclopentolate|hypromellose|carmellose|carboxymethylcellulose|sodium hyaluronate|"
     r"ranibizumab|aflibercept|olopatadine|naphazoline|oxymetazoline|xylometazoline|tetrahydrozoline|"
     r"cerumen|pirenoxine|fluorometholone|loteprednol|nepafenac|bromfenac"),
    (WOMEN, r"contracept|progest|estrogen|oestrogen|oxytoc|uterotonic|tocoly|gonadotropin|fertility|ovulat|"
            r"urolog|urinary|bladder|prostat|5-alpha|5α|erectile|phosphodiesterase.?5|pde-?5|vaginal|"
            r"menopaus|lactation|uterine|obstetric|gynecolog|alpha-?1|alpha-adreno|prolactin|gonadotroph|cholinergic|litholytic",
     r"levonorgestrel|ethinylestradiol|ethinyl estradiol|drospirenone|desogestrel|norethisterone|"
     r"medroxyprogesterone|dydrogesterone|progesterone|estradiol|clomifene|clomiphene|oxytocin|carbetocin|"
     r"methylergometrine|methylergonovine|misoprostol|tamsulosin|alfuzosin|silodosin|finasteride|dutasteride|"
     r"solifenacin|tolterodine|oxybutynin|mirabegron|tadalafil|vardenafil|follitropin|menotropin|"
     r"choriogonadotropin|cabergoline|bromocriptine|letrozole fert|cranberry|isoxsuprine|dienogest"),
]

_PRE = [(a, re.compile(rx, re.I)) for a, rx in PRE]
_AREAS = [(a, re.compile(c, re.I), re.compile(n, re.I)) for a, c, n in AREAS]


def class_text(e: dict) -> str:
    return " | ".join([e.get("c") or ""] + list(e.get("cl") or []))


def name_text(e: dict) -> str:
    return " | ".join([e.get("n") or ""] + list(e.get("i") or []))


def assign(e: dict) -> tuple[str, str]:
    """(area, why) for one search-index entry {n, c, cl[], i[], f[]}."""
    ct, nt = class_text(e), name_text(e)
    for area, rx in _PRE:
        if rx.search(ct):
            return area, f"class: {rx.search(ct).group(0)}"
    forms = set(e.get("f") or []) - {"other"}
    for only, area in ROUTE:
        if forms and forms <= only:
            return area, f"route: {'/'.join(sorted(only))} only"
    for area, crx, _ in _AREAS:
        m = crx.search(ct)
        if m:
            return area, f"class: {m.group(0)}"
    for area, _, nrx in _AREAS:
        m = nrx.search(nt)
        if m:
            return area, f"name: {m.group(0)}"
    return OTHER, "no rule matched"


def main():
    import argparse, json, random
    from collections import Counter
    from pathlib import Path
    ap = argparse.ArgumentParser()
    ap.add_argument("--index", default=str(Path(__file__).resolve().parents[2] / "drugs" / "search-index.json"))
    ap.add_argument("--sample", type=int, default=30)
    ap.add_argument("--other", action="store_true", help="list every generic that lands in Other")
    a = ap.parse_args()
    E = [e for e in json.load(open(a.index)) if not e.get("mh")]
    res = [(e, *assign(e)) for e in E]
    cnt = Counter(r[1] for r in res)
    for area in ORDER:
        print(f"{cnt.get(area, 0):5d}  {100 * cnt.get(area, 0) / len(E):5.1f}%  {area}")
    print(f"Other share: {100 * cnt.get(OTHER, 0) / len(E):.1f}% of {len(E)} generics")
    random.seed(17)
    for e, area, why in random.sample(res, min(a.sample, len(res))):
        print(f"- {e['n']} [{e.get('c', '')}] -> {area} ({why})")
    if a.other:
        for e, area, why in res:
            if area == OTHER:
                print("OTHER:", e["n"], "|", class_text(e))


if __name__ == "__main__":
    main()
