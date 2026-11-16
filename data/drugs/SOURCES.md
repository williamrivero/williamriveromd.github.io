# Drug database: official Philippine sources for `pnf.json` and `prices.json`

Built by `tools/drugdb/build_pnf.py` and `tools/drugdb/build_prices.py`. Both resolve names to the
contract slugs through `tools/drugdb/pnf_price_slugs.py`, which reuses `ingredients_of` / `slug_of` from
`tools/drugdb/build_registry.py`. When a government list spells a generic differently from the PH FDA
registry (salts, synonyms, typos), the record is copied under every matching `generics.json` slug and the
copy carries `"same_as": "<primary slug>"`.

Source documents are downloaded by `.github/workflows/drugdb-fetch-pnf-prices.yml` (manual dispatch).
The list of URLs is `tools/drugdb/sources/pnf_price_urls.txt`. The workflow commits the PDFs, their
`pdftotext -layout` text and a fetch log (`tools/drugdb/sources/fetch-log.tsv`, with HTTP status and
UTC retrieval time) to `tools/drugdb/sources/raw/`. The documents below were retrieved on
**November 16, 2026**.

No MIMS, Mercury Drug, Watsons, Southstar or other drugstore data is used. Their terms forbid scraping.
Pages may link out to them only.

## `pnf.json`: Philippine National Formulary (PNF) and PhilHealth GAMOT

| Source | Edition / as-of date | URL | How it is used |
|---|---|---|---|
| DOH PNF Essential Medicines List (EML), Volume I, 8th edition (2019) | As of November 2, 2022 | https://www.philhealth.gov.ph/partners/providers/pdf/PNF-EML_11022022.pdf | Main list. Parsed from the PDF text layer (two-column layout). PNF codes are turned into `restriction_notes`: (1) specialist expertise or equipment, (2) limited indications, (A1)/(A2) dangerous drugs or controlled chemicals, (B) bioequivalence list. Reserve antimicrobials and program-only notes ("For use by the National Tuberculosis Control Program …") are kept too. |
| PhilHealth Advisory PA2024-0026 | Additions as of April 25, 2024 | https://www.philhealth.gov.ph/advisories/2024/PA2024-0026.pdf | Medicines added in 2022–2024 (DOH-DC 2022-0593, 2023-0059/0060/0061/0169/0282, 2024-0051). |
| PhilHealth Advisory PA2025-0013 | Additions as of January 27, 2025 | https://www.philhealth.gov.ph/advisories/2025/PA2025-0013.pdf | Medicines added in 2024 (DOH-DC 2024-0051, 2024-0498). |
| PhilHealth Advisory PA2025-0060 | ePNF additions as of September 19, 2025 | https://www.philhealth.gov.ph/advisories/2025/PA2025-0060_v1.pdf | Medicines added in 2025 (DOH-DC 2025-0094, 2025-0341). The annex is a scanned image; it was transcribed visually. |
| PhilHealth Circular PC2025-0013, Annex A.i (GAMOT List) | 75 molecules; master copy stamped July 28, 2025 | https://www.philhealth.gov.ph/circulars/2025/PC2025-0013.pdf | The original GAMOT list. Sets `philhealth_gamot: true` and flags the 21 drugs also covered by PhilHealth YAKAP, formerly Konsulta (`konsulta_yakap`). |
| PhilHealth Circular PC-2026-0018, Annex A.i (GAMOT List), the **current** list | 81 molecules; master copy stamped October 13, 2026 | https://www.philhealth.gov.ph/circulars/2026/PC-2026-0018.pdf | Adds tobramycin + dexamethasone, losartan + hydrochlorothiazide, and first-line anti-TB drugs (ethambutol; isoniazid + rifampicin; isoniazid + rifampicin + pyrazinamide; isoniazid + rifampicin + pyrazinamide + ethambutol). `gamot_source` cites this circular; `gamot_listed_since` gives the date of the circular that first listed the molecule. |
| GAMOT Fixed Fee Schedule (Annex A.2 of both circulars) | 242 rows (2025) and 249 rows (2026) | both PDFs | Also sets `philhealth_gamot` for molecules priced there. |

The hand transcriptions live in `tools/drugdb/sources/pnf_additions.json`, `gamot_list.json` and
`gamot_fixed_fee_pc2025-0013.tsv` / `gamot_fixed_fee_pc2026-0018_additions.tsv`. Each one names its source document.
The PhilHealth PDFs are scans with a poor text layer, so prices were read from the page images (fees are always
whole centavos, e.g. ₱1.75), not from the OCR text.

`philhealth_gamot` is `true` for generics on the GAMOT list and `false` for PNF generics that are not on it. The value is `null` only if a
record exists for some other reason. Generics absent from `pnf.json` were not found in these documents. That
does **not** prove they are absent from the live ePNF.

Also downloaded and checked, but they contain no medicine list or price data: PC2026-0002 (GAMOT
supplemental guidelines), PC2026-0007 (YAKAP clinical and pharmaceutical standards), PA2026-0007 (the 21
YAKAP medicines remain available; the PDF has no text layer), PA2026-0018, PA2026-0043, PA2024-0062 (2024
GAMOT fees for 13 drugs, superseded by PC2025-0013), TS_PC2025-0013 (Filipino Q&A) and DOH DC 2026-0312 (call
for clinical practice guidelines). All are in `tools/drugdb/sources/raw/`.

## `prices.json`: government price references (not retail prices)

| Source | Edition / as-of date | URL | `price_type` |
|---|---|---|---|
| DOH Drug Price Reference Index (DPRI), 9th edition | 2021 (as of September 17, 2021); based on 2019–2020 government purchase orders | https://caro.doh.gov.ph/wp-content/uploads/2021/09/2021DPRI-as-of-9-17-2021.pdf (hosted by DOH CHD–Cordillera) | `dpri_range`: `price_low`–`price_high` is the lowest–highest procurement price, and `reference_price` is the 2021 DPRI ceiling (median). The highest price is usable only in GIDA areas. `dpri_reference` is a single published price with no range; `price_low` = `price_high` = reference. Footnote markers become `notes` (COBAC 2020 price, MWP-based, no inflation allowance). |
| PhilHealth GAMOT Fixed Fee Schedule (PC-2026-0018 Annex A.2, 249 preparations) | 2026 (master copy stamped October 13, 2026) | https://www.philhealth.gov.ph/circulars/2026/PC-2026-0018.pdf | `philhealth_gamot_fixed_fee`: the PhilHealth payment per unit dispensed. `price_low` = `price_high`. 242 rows were transcribed from the scanned PC2025-0013 annex (`gamot_fixed_fee_pc2025-0013.tsv`), and the 7 anti-TB rows from PC-2026-0018 (`gamot_fixed_fee_pc2026-0018_additions.tsv`). Every other fee in PC-2026-0018 was compared, in order, with its text layer and is unchanged. |

All prices are PHP and VAT-inclusive as published. `unit` is taken from the preparation wording ("per tablet",
"per vial", "per bottle"; "per unit" when none is stated).

### The current DPRI edition is not yet in `prices.json`

The newest edition is the **2026 Interim DPRI, 14th edition**. Its legal basis is DOH Department Circular
2026-0303 (June 10, 2026), which sets the interim framework: a lowest-to-highest price range instead of a
median, with up to 6.8% added for 2026–2027 inflation. DC 2026-0313 (June 16, 2026) released the electronic
edition. Both circulars are in `tools/drugdb/sources/raw/`. The 14th edition is published **only** on
https://dpri.doh.gov.ph/, which returns HTTP 403 to GitHub's servers and to this sandbox. It needs a
Philippine connection.

On a Philippine connection, export the table to `tools/drugdb/sources/dpri_2026.tsv` with these header lines:

```
# source: DOH Drug Price Reference Index 2026 (Interim, 14th edition), DC 2026-0313; https://dpri.doh.gov.ph/
# date: 2026-06-16
drugname	price_low	price_high
Amlodipine 5 mg Tablet	0.20	2.68
```

Then rerun `python3 tools/drugdb/build_prices.py`. It picks up any `dpri_*.tsv` automatically.

## Documents that need a Philippine connection

| What | URL | Status from GitHub Actions / sandbox |
|---|---|---|
| Live electronic PNF (ePNF), the authoritative current list, including additions after September 19, 2025 | https://pnf.doh.gov.ph/ | DNS does not resolve outside the Philippines |
| DPRI 2026 (14th edition) price table | https://dpri.doh.gov.ph/ (search: https://dpri.doh.gov.ph/index.php?page=search) | HTTP 403 |
| DOH Pharmaceutical Division DPRI pages and issuances | https://pharma.doh.gov.ph/dpri/ and https://pharma.doh.gov.ph/drug-price-reference-index/ | Connection fails |
| Possible PNF additions since September 2025. The HTA Council issued 2026 recommendations with Secretary of Health decisions (for example ezetimibe, erlotinib/gefitinib/afatinib, and pneumococcal vaccines for adults 60 and older); these decisions have not been checked here | https://hta.dost.gov.ph/issuances/ and the PhilHealth 2026 advisories list https://www.philhealth.gov.ph/advisories/2026/archives.php | No 2026 PhilHealth PNF advisory existed as of the retrieval date. Check the ePNF. |

## Updating

1. Add or replace URLs in `tools/drugdb/sources/pnf_price_urls.txt`, then dispatch the
   `drugdb-fetch-pnf-prices` workflow. It commits to `tools/drugdb/sources/raw/`.
2. When a new PhilHealth PNF advisory or GAMOT circular appears, add its rows to `pnf_additions.json`,
   `gamot_list.json` or the fixed-fee TSV (keep the `source` and dates).
3. Run `python3 tools/drugdb/build_pnf.py --report` and `python3 tools/drugdb/build_prices.py --report`.
   `--report` lists the names that did not match a registry generic. Add spelling fixes to
   `tools/drugdb/pnf_price_slugs.py` (`NAME_FIXES`, `WORD_FIXES`).
