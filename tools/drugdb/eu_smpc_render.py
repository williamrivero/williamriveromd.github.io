"""HTML for EU SmPC (EMA) text and link-only national prescribing information on drug pages.

Used by generate_drug_pages.py only when a generic has no US FDA label. Data: data/drugs/labels-eu/<slug>.json
(tools/drugdb/fetch_eu_smpc.py) and the "links" list of data/drugs/labels-intl/<slug>.json. SmPC text is verbatim
(British spelling kept, as quoted); every heading and note written here is American English.
"""
from __future__ import annotations

import datetime as dt
import html
import re

# Set False to show the EU SmPC as metadata + link only (no verbatim text); see data/drugs/SOURCES.md.
EU_VERBATIM = True

EU_CHIP = '<span class="dd-src dd-src-eu">EU SmPC (EMA)</span>'
esc = lambda s: html.escape("" if s is None else str(s), quote=True)


def _url(u) -> str:
    u = str(u or "").strip()
    return u if re.match(r"https://[\w.-]+/", u) else ""


def us_date(iso: str) -> str:
    try:
        d = dt.date.fromisoformat(str(iso)[:10])
    except ValueError:
        return str(iso or "")
    return f"{d.strftime('%B')} {d.day}, {d.year}"


def usable(eu) -> bool:
    return isinstance(eu, dict) and isinstance(eu.get("sections"), dict) and bool(eu["sections"]) \
        and isinstance(eu.get("source"), dict)


def blocks_html(blocks) -> str:
    out = []
    for b in blocks or []:
        if not isinstance(b, dict):
            continue
        if b.get("h"):
            out.append(f'<p class="dd-eu-h">{esc(b["h"])}</p>')
        elif b.get("p"):
            out.append(f"<p>{esc(b['p'])}</p>")
        elif b.get("li"):
            out.append('<ul class="dd-uselist">' + "".join(f"<li>{esc(x)}</li>" for x in b["li"]) + "</ul>")
        elif b.get("pre"):
            out.append(f'<div class="dd-tables"><pre class="dd-pre">{esc(b["pre"])}</pre></div>')
    return "".join(out)


def _acc(title, body, open_=False, aid="") -> str:
    if not body:
        return ""
    return (f'<details class="dd-acc"{f" id={chr(34)}{aid}{chr(34)}" if aid else ""}{" open" if open_ else ""}>'
            f'<summary><span>{esc(title)} {EU_CHIP}</span></summary><div class="dd-acc-body">{body}</div></details>')


def section(eu, num: str, open_=False) -> str:
    """One SmPC section as a collapsible block titled with its SmPC number ("4.2 Posology and method of ...")."""
    if not (EU_VERBATIM and usable(eu)):
        return ""
    s = eu["sections"].get(num)
    if not isinstance(s, dict):
        return ""
    return _acc(f"SmPC {num} {s.get('title') or ''}".strip(), blocks_html(s.get("blocks")), open_,
                aid=f"smpc-{num.replace('.', '-')}")


def subsection(eu, tag: str, label: str) -> str:
    """The 4.2 population subsection(s) with a tag (pediatric, elderly, hepatic), verbatim, open."""
    if not (EU_VERBATIM and usable(eu)):
        return ""
    subs = [s for s in (eu.get("subsections") or {}).get("4.2", []) if tag in (s.get("tags") or [])]
    if not subs:
        return ""
    body = "".join((f'<p class="dd-eu-h">{esc(s["heading"])}</p>' if s.get("heading") else "") + blocks_html(s["blocks"])
                   for s in subs)
    return _acc(f"{label} (SmPC 4.2)", body, open_=True)


def renal_html(eu) -> str:
    """Verbatim renal-impairment excerpts from SmPC 4.2 and 5.2 for the kidney panel ('' if none)."""
    if not (EU_VERBATIM and usable(eu)):
        return ""
    parts = []
    for x in eu.get("renal_impairment") or []:
        if not isinstance(x, dict) or not x.get("blocks"):
            continue
        where = f"SmPC {x.get('section', '')} {x.get('section_title', '')}".strip()
        head = f"{where} · {x['heading']}" if x.get("heading") else f"{where} (renal excerpts)"
        parts.append(f'<div class="dd-kidney-src">{esc(head)}</div>{blocks_html(x["blocks"])}')
    return "".join(parts)


def attribution_text(eu) -> str:
    src = eu["source"]
    rev = us_date(src.get("revision_date")) if src.get("revision_date") else ""
    return (f'EU Summary of Product Characteristics (EMA), {esc(src.get("product") or "")}'
            + (f", revised {esc(rev)}" if rev else ""))


def attribution(eu) -> str:
    """Top-of-page attribution block, replacing the 'US label not yet available' placeholder."""
    src = eu["source"]
    epar, pi = _url(src.get("epar_url")), _url(src.get("pi_url"))
    links = " · ".join(x for x in (
        f'<a href="{esc(epar)}" rel="noopener" target="_blank">EPAR page</a>' if epar else "",
        f'<a href="{esc(pi)}" rel="noopener" target="_blank">product information (PDF)</a>' if pi else "") if x)
    mah = f" Marketing authorization holder: {esc(src['mah'])}." if src.get("mah") else ""
    if not EU_VERBATIM:
        return (f'<div class="dd-attrib"><strong>Prescribing information:</strong> {attribution_text(eu)}'
                f'{" (" + links + ")" if links else ""}.{mah} No US FDA label text has been matched to this entry. '
                '<strong>Philippine-approved indications and doses may differ: check the PH package insert.</strong></div>')
    return (f'<div class="dd-attrib dd-attrib-eu"><strong>Label text on this page:</strong> {attribution_text(eu)}, '
            f'reproduced with acknowledgment of the source{" (" + links + ")" if links else ""}.{mah} '
            'Text is quoted verbatim, in the original British spelling. No US FDA label text has been matched to this entry. '
            '<strong>Philippine-approved indications and doses may differ: check the PH package insert.</strong></div>')


def reference(eu) -> str:
    src = eu["source"]
    rev = us_date(src.get("revision_date")) if src.get("revision_date") else ""
    url = _url(src.get("epar_url")) or _url(src.get("pi_url"))
    return (f'European Medicines Agency. {esc(src.get("product") or "")}: EPAR, product information, Annex I, '
            f'Summary of Product Characteristics [EU SmPC{", last updated " + esc(rev) if rev else ""}; no US FDA label].'
            + (f' <a href="{esc(url)}" rel="noopener" target="_blank">{esc(url)}</a>' if url else "")
            + " © European Medicines Agency; reproduced with acknowledgment of the source.")


def links_of(intl) -> list[dict]:
    if not isinstance(intl, dict):
        return []
    return [x for x in intl.get("links") or [] if isinstance(x, dict) and _url(x.get("url"))]


def search_links_of(intl) -> list[dict]:
    """External national search pages (Spain CIMA), stored only after the fetcher checked they return a product."""
    if not isinstance(intl, dict):
        return []
    return [x for x in intl.get("search_links") or [] if isinstance(x, dict) and _url(x.get("url"))]


def has_links(intl) -> bool:
    return bool(links_of(intl) or search_links_of(intl))


def links_html(intl) -> str:
    """'Prescribing information' link list from link-only national regulators (metadata + URL, no text)."""
    ls, ss = links_of(intl), search_links_of(intl)
    if not (ls or ss):
        return ""
    items = []
    for x in ls:
        name = esc(x.get("product") or "Product record")
        meta = ", ".join(esc(v) for v in (x.get("holder"), f"DIN {x['din']}" if x.get("din") else "") if v)
        pm = _url(x.get("monograph_url"))
        pm_html = (f' · <a href="{esc(pm)}" rel="noopener" target="_blank">product monograph (PDF)</a>'
                   + (f", dated {esc(us_date(x['monograph_date']))}" if x.get("monograph_date") else "")) if pm else ""
        items.append(f'<li><strong>{esc(x.get("agency_short") or x.get("agency") or "")}:</strong> '
                     f'<a href="{esc(x["url"])}" rel="noopener" target="_blank">{name}</a>'
                     f'{" (" + meta + ")" if meta else ""}{pm_html}</li>')
    for x in ss:
        items.append(f'<li><a href="{esc(x["url"])}" rel="noopener" target="_blank">{esc(x.get("label") or x.get("agency_short") or "")}</a>'
                     f'{": search for " + chr(8220) + esc(x["query"]) + chr(8221) if x.get("query") else ""} '
                     '<span class="dd-sub">(external search; text not reproduced)</span></li>')
    note = ("Links only. These regulators' terms do not clearly permit reproducing the documents, so no text is shown "
            "here." if ls else "External search; text not reproduced.")
    return ('<div class="dd-placeholder dd-pi-links"><strong>Prescribing information</strong> (no matched US FDA label or EU SmPC '
            'for this generic):<ul class="dd-uselist">' + "".join(items) + f'</ul><p class="dd-note">{note} Check the '
            "Philippine package insert in the products table.</p></div>")
