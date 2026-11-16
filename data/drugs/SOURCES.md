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

# `controlled.json`: Philippine dangerous drugs (S2) and controlled precursors

Built by `tools/drugdb/build_controlled.py` from the hand-curated `tools/drugdb/sources/ddb_schedules.tsv`
(one row per scheduled substance with medical use; every row names the issuances that schedule it). Generics
not in `controlled.json` follow their FDA Philippines registration classification (`dispensing`: Rx / OTC / HR,
normalized by `build_registry.py`). The documents were downloaded by `.github/workflows/drugdb-fetch-ddb.yml`
(URL list `tools/drugdb/sources/ddb_urls.txt`, log `tools/drugdb/sources/ddb-fetch-log.tsv`) on
**November 16, 2026** and are kept with their text (`pdftotext`, or Tesseract OCR for scans, `*.ocr.txt`) in
`tools/drugdb/sources/raw/ddb/`. Nothing was scheduled from memory.

| Source id | Issuance | Date | URL | Used for |
|---|---|---|---|---|
| `ddb-list-2026` | DDB, *Updated Lists of Scheduled Controlled Substances* (DDB-LEGAL) | as of July 20, 2026 | https://ddb.gov.ph/wp-content/uploads/2026/08/2026_7-Updated-Lists-of-controlled-substances.pdf | The master list: 1988 Convention Tables I–II (as of Dec 3, 2024), 1961 Single Convention Schedules I–IV (as of June 9, 2025), 1971 Convention Schedules I–IV (as of Dec 6, 2025), and the Philippine Schedule (DDB regulations). |
| `ra9165` | Republic Act No. 9165, Comprehensive Dangerous Drugs Act of 2002 | June 7, 2002 | https://ddb.gov.ph/wp-content/uploads/2022/01/RA-9165.pdf | Sec. 3(j) definition of dangerous drugs; Secs. 18–19 prescriptions; Sec. 93 reclassification. |
| `br1-2014` | DDB Board Regulation No. 1, s. 2014 (amends BR 3 s. 2003) | June 19, 2014 | https://ddb.gov.ph/images/Board_Regulation/2014/BD.REG1.14.pdf (mirror: WTO import-licensing site, same file) | Sec. 2(2) domestic additions = Philippine Schedule 5; Sec. 4 preparations and exemptions (4(2)(b) buprenorphine patches; 4(4)(a) oral Schedule 4 and 5 preparations on ordinary triplicate prescription; 4(5) oral ergometrine, ergotamine and norephedrine preparations and potassium permanganate solutions exempt); Sec. 6(3) S-2 license; Sec. 6(14)–(15) phenylpropanolamine ≤ 25 mg OTC; Sec. 31 prescriptions (special form, triplicate, one drug, no refill, 30/60-day supply). |
| `br3-2020` | DDB Board Regulation No. 3, s. 2020 | Sept. 24, 2020 | https://ddb.gov.ph/images/Board_Regulation/2020/BOARD_REG_NO._3_S._2020.pdf | CBD drug products (≤ 0.1% THC) in Philippine Schedule 4; Sec. 1 defines Philippine Schedules 1, 2 and 4 by their UN-convention equivalents (Schedule 2 = 1961 I–II and 1971 II; Schedule 4 = 1961 III and 1971 IV). |
| `br1-2020` | DDB Board Regulation No. 1, s. 2020 | June 18, 2020 | https://ddb.gov.ph/images/Board_Regulation/2020/2020-BRD._REG.__1_-_Immediate_Adoption_of_Changes_in_the_Scope_of_Control_of_Substance_Pursuant_to_the_Three_3_United_Nation_International_Drug_Conve.pdf | Immediate adoption of UN scope-of-control changes (e.g., carisoprodol, 1971 Schedule IV). |
| `br10-2025` | DDB Board Regulation No. 10, s. 2025 | June 26, 2025 | https://ddb.gov.ph/wp-content/uploads/2025/07/BOARD-REGULATION-NO.-10-SERIES-OF-2025_Preemptive-Response-to-Emerging-Public-Health-Concerns-through-Temporary-Authorization-of-Ordinary-Prescriptions-for-Dangerous-Drugs-2.pdf | S-2 licensed practitioners may prescribe any dangerous-drug preparation on an ordinary prescription in triplicate (originally until June 30, 2026). |
| `br5-2026` | DDB Board Regulation No. 5, s. 2026 | June 23, 2026 | https://ddb.gov.ph/wp-content/uploads/2026/06/Board-Regulation-No.-5-Series-of-2026.pdf | Extends BR 10 s. 2025 until **June 30, 2027**. |
| `br3-2005` | DDB Board Regulation No. 3, s. 2005 | July 19, 2005 | https://ddb.gov.ph/images/Board_Regulation/2005/Bd.%20Reg.%203%2005.pdf | Ketamine (salts, isomers) a dangerous drug; vial/prescription exception (≤ 50 mg/mL × 10 mL; ≤ 1.5 g/day, ≤ 30 days). |
| `br5-2021` | DDB Board Regulation No. 5, s. 2021 | July 29, 2021 | https://ddb.gov.ph/images/Board_Regulation/2021/BOARD_REG_NO._5_S._2021.pdf | Esketamine (ketamine isomer) nasal spray device on ordinary triplicate prescription. |
| `br1-2010` | DDB Board Regulation No. 1, s. 2010 | Dec. 16, 2010 | https://ddb.gov.ph/images/Board_Regulation/2010/BD.REG1%20%2010.pdf | Nalbuphine a dangerous drug; special form, max 40 mg per prescription. |
| `br4-2005` | DDB Board Regulation No. 4, s. 2005 | July 19, 2005 | https://ddb.gov.ph/images/Board_Regulation/2005/Bd.%20Reg.%204%2005.pdf | Ephedrine and pseudoephedrine (and preparations) reclassified as dangerous drugs; Sec. 2 exemption criteria; Sec. 4 no OTC sale or samples. |
| `br1-2018` | DDB Board Regulation No. 1, s. 2018 | Jan. 24, 2018 | https://ddb.gov.ph/images/Board_Regulation/2018/2018_Board_Regulation_No._1_-__RECLASSIFYING_EPHEDRINE_AND_PSUEDOEPHERINE.pdf | Amends BR 4 s. 2005 Sec. 1 (isomers, halogenated/alkylated forms, any mixture or preparation). |
| `br2-2013` | DDB Board Regulation No. 2, s. 2013 | Sept. 12, 2013 | https://ddb.gov.ph/images/Board_Regulation/2013/BD.REG2%2013.pdf | Methylephedrine a dangerous drug. |

Also fetched and read (no product in the registry depends on them): BR 3 s. 2003 and BR 9 s. 2003 (superseded
or adopted by BR 1 s. 2014), BR 7 s. 2007, BR 4 s. 2009, BR 3 s. 2018, BR 8 s. 2019 (unregistered products for
personal use), BR 3 s. 2019 (plants), BR 1 and BR 2 s. 2008 (oripavine, amineptine), BR 13 s. 2025, BR 2 s. 2024
(Lianhua Qingwen provisional removal, one year from March 8, 2024; no later extension appears on the DDB list or
Board Regulations page), the July 2023 consolidated list, and the DDB Board Regulations, Board Resolutions and
Regulatory Control index pages.

**How categories are assigned.** "S2 — Dangerous drug" = a substance in the 1961 or 1971 Convention schedules
adopted by RA 9165 Sec. 3(j), or in the Philippine Schedule by DDB regulation. "Controlled precursor / essential
chemical" = a 1988 Convention Table I/II chemical that is not also a dangerous drug (ephedrine and pseudoephedrine
are Table I chemicals but the DDB reclassified them as dangerous drugs, so they are S2). A combination product takes
the status of the scheduled ingredient it contains (BR 1 s. 2014 Sec. 4(1)); dangerous drug outranks precursor.
Each item keeps `review[]` for points that need Dr. Rivero's judgment; `pnf_crosscheck[]` lists every disagreement
with the PNF A1/A2 codes in `pnf.json` (never merged automatically). `unmatched_substances[]` lists curated
substances with no registered product.

**Checked and not scheduled** on the July 20, 2026 list or in any DDB regulation found: tramadol, butorphanol,
thiopental, methylergometrine (a distinct compound from ergometrine), gabapentin, pregabalin, and dextromethorphan
(the list notes it is not under international control).

**Updating.** When the DDB posts a new consolidated list or Board Regulation, add its URL to
`tools/drugdb/sources/ddb_urls.txt`, dispatch `drugdb-fetch-ddb`, update `ddb_schedules.tsv` (and `SOURCES` in
`build_controlled.py` for a new issuance), then run `python3 tools/drugdb/build_controlled.py`.
