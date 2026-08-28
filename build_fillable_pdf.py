#!/usr/bin/env python3
"""
Render a companion booklet as an INTERACTIVE FILLABLE PDF (AcroForm).

WeasyPrint cannot emit form fields. It can emit link annotations with exact
rectangles, so this script works in three passes:

  1. HTML transform — every write-in primitive in the companion markup is wrapped
     in an anchor carrying a synthetic URI that encodes the field name:
         <td class="wr">            ->  <a href="field:NAME">   text field
         <span class="fl">          ->  <a href="field:NAME">   text field
         <span class="chk">         ->  <a href="check:NAME">   checkbox
     Field names are derived from the page title, the numbered section, the row
     index and the column header, so they come out semantic and stable —
     e.g. `medicines-and-supplements-1-of-3.01.r03.how-i-actually-take-it`
     (blueprint §10.4: "form field names unique and semantically meaningful").

  2. WeasyPrint render — the anchors become /Link annotations whose /Rect is the
     exact on-page geometry of the writing area.

  3. pypdf pass — each such annotation is rewritten in place as a /Widget with
     /FT /Tx or /FT /Btn, collected into an /AcroForm. Tall cells get the
     multiline flag. The print layout is untouched, so the same file prints
     blank for handwriting and fills in on screen.

Usage:
    python3 build_fillable_pdf.py personal-medical-journal-booklet
    python3 build_fillable_pdf.py personal-medical-journal-booklet --pages 1-11
    python3 build_fillable_pdf.py <name> --pages 1-11 --suffix -fillable-sample
    python3 build_fillable_pdf.py <name> --keep-html   # keep the transformed HTML

Requires: weasyprint, pypdf   (pip install weasyprint pypdf)
Writes:   downloads/<name><suffix>.pdf   (default suffix: -fillable)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).parent
DL = ROOT / "downloads"

# Cells shorter than this render as a single line; taller ones become multiline.
MULTILINE_MIN_PX = 30


# ──────────────────────────────────────────────────────────────────────────
# helpers
# ──────────────────────────────────────────────────────────────────────────
def strip_tags(html):
    t = re.sub(r"<[^>]+>", " ", html)
    t = (t.replace("&mdash;", "-").replace("&ndash;", "-").replace("&nbsp;", " ")
          .replace("&amp;", "&").replace("&middot;", " ").replace("&rsquo;", "'")
          .replace("&ldquo;", "").replace("&rdquo;", "").replace("&deg;", ""))
    return re.sub(r"\s+", " ", t).strip()


def slug(text, maxlen=34):
    s = re.sub(r"[^a-z0-9]+", "-", strip_tags(text).lower()).strip("-")
    return (s[:maxlen].rstrip("-") or "field")


def page_slug(page_html, index):
    m = re.search(r'class="page-hdr-title"[^>]*>(.*?)</(?:div|h[1-6])>', page_html, re.S)
    if m:
        title = re.sub(r'<span class="wb-doh">.*?</span>', ' ', m.group(1), flags=re.S)
        return slug(title, maxlen=44)
    if re.search(r'class="hero-title"', page_html):
        return "cover"
    return f"page-{index:02d}"


def table_headers(tbl):
    """Column labels for a table: <th> row, else the first <tr class="h">."""
    ths = re.findall(r"<th[^>]*>(.*?)</th>", tbl, re.S)
    if ths:
        return [slug(t) for t in ths]
    m = re.search(r'<tr class="h">(.*?)</tr>', tbl, re.S)
    if m:
        return [slug(t) for t in re.findall(r"<td[^>]*>(.*?)</td>", m.group(1), re.S)]
    return []


# ──────────────────────────────────────────────────────────────────────────
# pass 1 — HTML transform
# ──────────────────────────────────────────────────────────────────────────
def transform(html, pages_wanted=None):
    head, *pages = re.split(r'(?=<div class="page")', html)
    if pages_wanted:
        keep = [p for i, p in enumerate(pages, 1) if i in pages_wanted]
    else:
        keep = pages
    used = {}
    out_pages, n_text, n_check = [], 0, 0

    def uniq(name):
        used[name] = used.get(name, 0) + 1
        return name if used[name] == 1 else f"{name}-{used[name]}"

    for idx, page in enumerate(keep, 1):
        pslug = page_slug(page, idx)
        sec = {"n": 0}

        # numbered sections give the field names their middle segment
        def bump(m):
            sec["n"] += 1
            return m.group(0)

        # walk tables so cells can be named from their column header
        def do_table(tm):
            tbl = tm.group(0)
            cols = table_headers(tbl)
            snum = f"{sec['n']:02d}"
            rows = re.split(r"(?=<tr)", tbl)
            r_i = {"n": 0}

            def do_row(rm):
                row = rm.group(0)
                if 'class="wr"' not in row:
                    return row
                r_i["n"] += 1
                c_i = {"n": -1}

                def do_cell(cm):
                    c_i["n"] += 1
                    attrs = cm.group(1)
                    hm = re.search(r"height:(\d+)px", attrs)
                    tall = int(hm.group(1)) >= MULTILINE_MIN_PX if hm else False
                    col = cols[c_i["n"]] if c_i["n"] < len(cols) else f"c{c_i['n']+1:02d}"
                    name = uniq(f"{pslug}.{snum}.r{r_i['n']:02d}.{col}")
                    kind = "field" if not tall else "field"
                    ml = "1" if tall else "0"
                    return (f'<td class="wr"{attrs}>'
                            f'<a class="fld" href="{kind}:{ml}:{name}">&nbsp;</a></td>')

                return re.sub(r'<td class="wr"([^>]*)></td>', do_cell, row)

            return re.sub(r"<tr[\s\S]*?</tr>", do_row, tbl)

        page = re.sub(r'<span class="sec-num[^"]*">\d+</span>', bump, page)
        page = re.sub(r'<table class="pl-tbl"[\s\S]*?</table>', do_table, page)

        # inline rules and checkboxes anywhere on the page
        def do_fl(m):
            wide = m.group(1) or ""
            name = uniq(f"{pslug}.line")
            return f'<a class="fld fld-inline{wide}" href="field:0:{name}">&nbsp;</a>'

        def do_chk(m):
            return f'<a class="chk chk-fld" href="check:0:{uniq(pslug + ".chk")}">&nbsp;</a>'

        # cover identity block: the writing area is the bordered cell itself
        def do_cover(m):
            label = slug(m.group(2))
            return (f'<td{m.group(1)}><span class="lbl">{m.group(2)}</span>'
                    f'<a class="fld" href="field:0:{uniq(pslug + "." + label)}">&nbsp;</a>&nbsp;</td>')

        def do_cover_tbl(tm):
            return re.sub(r'<td([^>]*)><span class="lbl">(.*?)</span>&nbsp;</td>',
                          do_cover, tm.group(0))

        page = re.sub(r'<table class="wb-cover-fields"[\s\S]*?</table>', do_cover_tbl, page)
        page = re.sub(r'<span class="fl( wide)?"></span>', do_fl, page)
        page = re.sub(r'<span class="chk"></span>', do_chk, page)

        n_text += len(re.findall(r'href="field:', page))
        n_check += len(re.findall(r'href="check:', page))
        out_pages.append(page)

    return head + "".join(out_pages), n_text, n_check


# ──────────────────────────────────────────────────────────────────────────
# pass 3 — annotations -> AcroForm widgets
# ──────────────────────────────────────────────────────────────────────────
def acroform(pdf_in, pdf_out):
    from pypdf import PdfReader, PdfWriter
    from pypdf.generic import (
        ArrayObject, BooleanObject, DictionaryObject, FloatObject, NameObject,
        NumberObject, TextStringObject,
    )

    reader = PdfReader(str(pdf_in))
    writer = PdfWriter()
    writer.append_pages_from_reader(reader)

    helv = DictionaryObject({
        NameObject("/Type"): NameObject("/Font"),
        NameObject("/Subtype"): NameObject("/Type1"),
        NameObject("/BaseFont"): NameObject("/Helvetica"),
        NameObject("/Encoding"): NameObject("/WinAnsiEncoding"),
    })
    helv_ref = writer._add_object(helv)
    zadb = writer._add_object(DictionaryObject({
        NameObject("/Type"): NameObject("/Font"),
        NameObject("/Subtype"): NameObject("/Type1"),
        NameObject("/BaseFont"): NameObject("/ZapfDingbats"),
    }))

    fields, converted, checks = [], 0, 0

    for page in writer.pages:
        annots = page.get("/Annots")
        if not annots:
            continue
        for ref in list(annots):
            an = ref.get_object()
            act = an.get("/A") or {}
            uri = act.get("/URI") or ""
            if not (uri.startswith("field:") or uri.startswith("check:")):
                continue
            kind, ml, name = uri.split(":", 2)
            x0, y0, x1, y1 = [float(v) for v in an["/Rect"]]
            rect = ArrayObject([FloatObject(round(v, 2)) for v in
                                (min(x0, x1), min(y0, y1), max(x0, x1), max(y0, y1))])

            an.clear()
            an.update({
                NameObject("/Type"): NameObject("/Annot"),
                NameObject("/Subtype"): NameObject("/Widget"),
                NameObject("/Rect"): rect,
                NameObject("/T"): TextStringObject(name),
                NameObject("/F"): NumberObject(4),          # print
                NameObject("/MK"): DictionaryObject(),      # no border, no bg
                NameObject("/P"): page.indirect_reference,
            })
            if kind == "field":
                flags = 4096 if ml == "1" else 0            # bit 13 = multiline
                an.update({
                    NameObject("/FT"): NameObject("/Tx"),
                    NameObject("/Ff"): NumberObject(flags),
                    NameObject("/DA"): TextStringObject("/Helv 9 Tf 0 g"),
                    NameObject("/V"): TextStringObject(""),
                })
                converted += 1
            else:
                an.update({
                    NameObject("/FT"): NameObject("/Btn"),
                    NameObject("/Ff"): NumberObject(0),
                    NameObject("/DA"): TextStringObject("/ZaDb 0 Tf 0 g"),
                    NameObject("/V"): NameObject("/Off"),
                    NameObject("/AS"): NameObject("/Off"),
                })
                checks += 1
            fields.append(ref)
        # row order == reading order for this table-heavy layout
        page[NameObject("/Tabs")] = NameObject("/R")

    writer._root_object[NameObject("/AcroForm")] = writer._add_object(DictionaryObject({
        NameObject("/Fields"): ArrayObject(fields),
        NameObject("/NeedAppearances"): BooleanObject(True),
        NameObject("/DA"): TextStringObject("/Helv 9 Tf 0 g"),
        NameObject("/DR"): DictionaryObject({
            NameObject("/Font"): DictionaryObject({
                NameObject("/Helv"): helv_ref,
                NameObject("/ZaDb"): zadb,
            })
        }),
    }))

    with open(pdf_out, "wb") as fh:
        writer.write(fh)
    return converted, checks


# ──────────────────────────────────────────────────────────────────────────
def main(argv):
    names = [a for a in argv if not a.startswith("-")]
    if not names:
        print(__doc__)
        return 1
    pages = None
    if "--pages" in argv:
        spec = argv[argv.index("--pages") + 1]
        pages = set()
        for part in spec.split(","):
            if "-" in part:
                a, b = part.split("-")
                pages.update(range(int(a), int(b) + 1))
            else:
                pages.add(int(part))
    suffix = argv[argv.index("--suffix") + 1] if "--suffix" in argv else "-fillable"

    stem = names[0].replace(".html", "")
    src = DL / f"{stem}.html"
    if not src.exists():
        print(f"✗ {src} not found")
        return 1

    from weasyprint import HTML

    html, n_text, n_check = transform(src.read_text(encoding="utf-8"), pages)
    tmp_html = DL / f"_{stem}{suffix}.tmp.html"
    tmp_html.write_text(html, encoding="utf-8")

    tmp_pdf = DL / f"_{stem}{suffix}.tmp.pdf"
    HTML(str(tmp_html), base_url=str(DL)).write_pdf(str(tmp_pdf))

    out = DL / f"{stem}{suffix}.pdf"
    converted, checks = acroform(tmp_pdf, out)

    if "--keep-html" not in argv:
        tmp_html.unlink(missing_ok=True)
    tmp_pdf.unlink(missing_ok=True)

    print(f"  ✓ {out.name}  ({out.stat().st_size // 1024} KB)")
    print(f"    anchors marked : {n_text} text, {n_check} checkbox")
    print(f"    fields created : {converted} text, {checks} checkbox")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
