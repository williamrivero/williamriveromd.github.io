#!/usr/bin/env python3
"""Crawl the PH FDA Verification Portal search API for registered drug products.

The portal (https://verification.fda.gov.ph) only exposes a search endpoint
(/api/search?q=...), so the registry is enumerated by:
  1. registration-number prefix queries (DR-XY, DRP-, BR-, ...), then
  2. a saturation sweep: every distinct word from generic names found so far is
     queried until no new registration numbers appear.
Polite: one request at a time with a pause between requests. Resumable: query
results are cached in cache/<sha1>.json, so a rerun only fetches new queries.

Outputs (in this folder):
  ph-fda-drugs.json      products (category "cdrr"), keyed by registration_number
  ph-fda-pipil.json      package-insert / leaflet links (category "cdrr_PIPIL")
  ph-fda-vat-exempt.json VAT-exempt health products (category "vat_exempt")
  crawl-log.txt
"""
import hashlib, json, os, re, sys, time, urllib.parse, urllib.request

HERE = os.path.dirname(os.path.abspath(__file__))
CACHE = os.path.join(HERE, "cache"); os.makedirs(CACHE, exist_ok=True)
UA = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130 Safari/537.36"
PAUSE = 2.0
PREFIXES = ["DR-XY", "DR-X", "DRP-", "DRHR-", "DRP", "BR-", "BRP-", "HRP-", "DRI-", "VR-", "DR-"]
STOP = set("as and with in of for the hcl hydrochloride sodium potassium calcium tablet capsule mg film coated "
           "solution injection suspension oral powder per ml mcg iu equivalent to base anhydrous monohydrate "
           "dihydrate trihydrate sulfate sulphate phosphate acetate maleate besilate besylate mesylate tartrate "
           "citrate magnesium hydrobromide succinate fumarate chloride bromide dipropionate propionate".split())

log = open(os.path.join(HERE, "crawl-log.txt"), "a")
def say(*a):
    s = time.strftime("%H:%M:%S ") + " ".join(str(x) for x in a)
    print(s, flush=True); log.write(s + "\n"); log.flush()

def query(q):
    key = os.path.join(CACHE, hashlib.sha1(q.lower().encode()).hexdigest() + ".json")
    if os.path.exists(key):
        try: return json.load(open(key))
        except Exception: pass
    url = "https://verification.fda.gov.ph/api/search?q=" + urllib.parse.quote(q)
    for attempt in range(4):
        try:
            req = urllib.request.Request(url, headers={"User-Agent": UA, "Accept": "application/json"})
            with urllib.request.urlopen(req, timeout=180) as r:
                data = json.loads(r.read().decode("utf-8", "replace"))
            json.dump(data, open(key, "w"))
            time.sleep(PAUSE)
            return data
        except urllib.error.HTTPError as e:
            if e.code == 422: return {}
            say("HTTP", e.code, q, "attempt", attempt); time.sleep(10 * (attempt + 1))
        except Exception as e:
            say("ERR", type(e).__name__, q, "attempt", attempt); time.sleep(10 * (attempt + 1))
    return {}

def as_list(v):
    if not v: return []
    return v if isinstance(v, list) else list(v.values()) if isinstance(v, dict) else []

drugs, pipil, vat = {}, {}, {}
def absorb(d):
    new = 0
    for r in as_list(d.get("cdrr")):
        rn = (r.get("registration_number") or "").strip()
        if rn and rn not in drugs: drugs[rn] = r; new += 1
    for r in as_list(d.get("cdrr_PIPIL")):
        k = (r.get("registration_number") or "") + "|" + (r.get("version") or "") + "|" + (r.get("file_link") or "")
        pipil[k] = r
    for r in as_list(d.get("vat_exempt")):
        k = "|".join(str(r.get(x, "")) for x in ("generic_name", "dosage_strength", "dosage_form"))
        vat[k] = r
    return new

def words(name):
    for w in re.split(r"[^A-Za-z]+", name or ""):
        w = w.lower()
        if len(w) >= 4 and w not in STOP: yield w

done = set()
def run(q):
    if q.lower() in done: return 0
    done.add(q.lower())
    n = absorb(query(q))
    say(f"q={q!r:28} +{n:5} total={len(drugs)}")
    return n

def save(final=False):
    json.dump(drugs, open(os.path.join(HERE, "ph-fda-drugs.json"), "w"), ensure_ascii=False, indent=0)
    json.dump(list(pipil.values()), open(os.path.join(HERE, "ph-fda-pipil.json"), "w"), ensure_ascii=False, indent=0)
    json.dump(list(vat.values()), open(os.path.join(HERE, "ph-fda-vat-exempt.json"), "w"), ensure_ascii=False, indent=0)
    if final: say("DONE products", len(drugs), "PI/PIL", len(pipil), "VAT-exempt", len(vat), "queries", len(done))

for p in PREFIXES: run(p)
save()
# saturation sweep over generic-name words (repeat until no new words)
i = 0
while True:
    pending = sorted({w for r in drugs.values() for w in words(r.get("generic_name"))} - done)
    if not pending: break
    say("sweep: pending words", len(pending))
    for w in pending:
        run(w); i += 1
        if i % 50 == 0: save()
save(final=True)
