#!/usr/bin/env python3
"""
add_related_guides.py — williamriveromd.com
Generates a related-guides relationship map using Claude, then injects
"Related Guides" cards into every guide page.

Steps this script performs:
  1. Scans guides/ to build a catalogue (filename → title)
  2. Calls Claude API to generate 3-4 related guides per guide (once)
  3. Saves the relationship map to related_guides.json (review/edit manually if needed)
  4. Injects the Related Guides section into each guide HTML file
  5. Supports EN / TL / CEB / KAP section headers

Usage:
    # Full run (generate map + inject)
    python3 add_related_guides.py --api-key sk-ant-...

    # Step 1 only: generate/update the JSON map
    python3 add_related_guides.py --api-key sk-ant-... --map-only

    # Step 2 only: inject cards using existing related_guides.json
    python3 add_related_guides.py --inject-only

    # Preview injection without writing files
    python3 add_related_guides.py --inject-only --dry-run
"""

import re
import sys
import json
import time
import argparse
from pathlib import Path

try:
    import anthropic
except ImportError:
    print("ERROR: Run: pip3 install anthropic beautifulsoup4")
    sys.exit(1)

try:
    from bs4 import BeautifulSoup
except ImportError:
    print("ERROR: Run: pip3 install anthropic beautifulsoup4")
    sys.exit(1)


# ── Config ─────────────────────────────────────────────────────────────────────

SECTION_LABELS = {
    "en":  "Related Guides",
    "tl":  "Mga Kaugnay na Gabay",
    "ceb": "Mga May Kalabtan nga Giya",
    "kap": "Ding Kaugnay nga Gabay",
}

# CSS matches the existing guide design system exactly
RELATED_CSS = """
<style>
.related-guides {
  margin: 48px 0 32px;
  padding-top: 32px;
  border-top: 2px solid var(--border, #e2e6eb);
}
.related-guides h2 {
  font-size: 1.15rem;
  font-weight: 700;
  color: var(--navy, #0f1e2e);
  margin-bottom: 18px;
  text-transform: uppercase;
  letter-spacing: 0.04em;
}
.related-cards {
  display: grid;
  grid-template-columns: repeat(auto-fill, minmax(220px, 1fr));
  gap: 14px;
}
.related-card {
  display: flex;
  flex-direction: column;
  background: #fff;
  border: 1px solid var(--border, #e2e6eb);
  border-radius: 10px;
  padding: 16px 18px;
  text-decoration: none;
  color: inherit;
  transition: box-shadow 0.18s, border-color 0.18s;
  cursor: pointer;
}
.related-card:hover {
  border-color: var(--teal, #1a6b72);
  box-shadow: 0 4px 16px rgba(26,107,114,0.10);
}
.related-card-tag {
  font-size: 0.68rem;
  font-weight: 700;
  color: var(--teal, #1a6b72);
  text-transform: uppercase;
  letter-spacing: 0.06em;
  margin-bottom: 6px;
}
.related-card-title {
  font-size: 0.92rem;
  font-weight: 600;
  color: var(--navy, #0f1e2e);
  line-height: 1.35;
  margin-bottom: 6px;
}
.related-card-desc {
  font-size: 0.80rem;
  color: var(--text-muted, #5a6472);
  line-height: 1.45;
  flex: 1;
}
.related-card-arrow {
  font-size: 0.80rem;
  color: var(--teal, #1a6b72);
  font-weight: 700;
  margin-top: 10px;
  align-self: flex-end;
}
/* Dark mode */
body.dark .related-card {
  background: #1a2535;
  border-color: #2a3a4a;
}
body.dark .related-card:hover {
  border-color: var(--teal, #1a6b72);
}
body.dark .related-card-title {
  color: #e8edf2;
}
</style>
"""


# ── Helpers ────────────────────────────────────────────────────────────────────

def find_project_dir(script_path: Path) -> Path:
    candidates = [
        script_path.parent,
        script_path.parent.parent,
        Path.home() / "Desktop" / "williamriveromd",
    ]
    for c in candidates:
        if (c / "guides").is_dir() and (c / "index.html").exists():
            return c
    raise FileNotFoundError(
        "Cannot find williamriveromd project root. "
        "Run from ~/Desktop/williamriveromd/"
    )


def extract_guide_meta(path: Path) -> dict:
    """Extract title, subtitle, and section tag from a guide HTML file."""
    try:
        soup = BeautifulSoup(path.read_text(encoding="utf-8"), "html.parser")
    except Exception:
        return {"filename": path.name, "title": path.stem, "subtitle": "", "tag": ""}

    # Title: first data-lang="en" in .hero h1, or <title>
    title = ""
    hero = soup.find(class_="hero")
    if hero:
        h1 = hero.find("h1")
        if h1:
            en = h1.find(attrs={"data-lang": "en"})
            title = (en or h1).get_text(strip=True)
    if not title:
        t = soup.find("title")
        title = t.get_text(strip=True).split("|")[0].strip() if t else path.stem

    # Subtitle
    subtitle = ""
    if hero:
        p = hero.find("p")
        if p:
            en = p.find(attrs={"data-lang": "en"})
            subtitle = (en or p).get_text(strip=True)[:120]

    # Section tag (first .section-tag text)
    tag = ""
    st = soup.find(class_="section-tag")
    if st:
        en = st.find(attrs={"data-lang": "en"})
        tag = (en or st).get_text(strip=True)

    return {
        "filename": path.name,
        "title": title,
        "subtitle": subtitle,
        "tag": tag,
    }


def build_catalogue(guides_dir: Path) -> list[dict]:
    files = sorted(f for f in guides_dir.glob("*.html") if f.name != "index.html")
    catalogue = []
    for f in files:
        meta = extract_guide_meta(f)
        catalogue.append(meta)
    return catalogue


# ── Step 1: Generate relationship map via Claude API ──────────────────────────

RELATIONSHIP_PROMPT = """You are helping organize a medical patient education website for a nephrologist (kidney specialist) in the Philippines.

Below is a catalogue of {n} patient guides. For each guide, suggest 3-4 related guides that a patient reading that guide would genuinely benefit from reading next.

Rules:
- Prefer thematic and clinical relevance (e.g. a CKD diet guide relates to CKD stages, protein, phosphorus guides)
- Do not suggest a guide as related to itself
- Spread connections — don't just cluster everything around the same 5 guides
- Prioritize guides the patient is most likely to need next in their care journey

Return a JSON object only — no preamble, no markdown fences. Format:
{{
  "filename.html": ["related1.html", "related2.html", "related3.html"],
  ...
}}

Catalogue:
{catalogue}
"""


def generate_relationship_map(catalogue: list[dict], client: anthropic.Anthropic) -> dict:
    catalogue_text = "\n".join(
        f"{i+1}. {g['filename']} — {g['title']}"
        + (f" [{g['tag']}]" if g["tag"] else "")
        + (f": {g['subtitle'][:80]}" if g["subtitle"] else "")
        for i, g in enumerate(catalogue)
    )

    prompt = RELATIONSHIP_PROMPT.format(n=len(catalogue), catalogue=catalogue_text)

    print(f"  Sending {len(catalogue)} guides to Claude for relationship mapping...")
    msg = client.messages.create(
        model="claude-opus-4-5",
        max_tokens=4096,
        messages=[{"role": "user", "content": prompt}],
    )

    raw = msg.content[0].text.strip()
    # Strip markdown fences if present
    raw = re.sub(r"^```json\s*", "", raw)
    raw = re.sub(r"```\s*$", "", raw)

    try:
        mapping = json.loads(raw)
    except json.JSONDecodeError as e:
        print(f"  ERROR parsing Claude response: {e}")
        print(f"  Raw response (first 500 chars):\n{raw[:500]}")
        sys.exit(1)

    # Validate filenames exist in catalogue
    valid_files = {g["filename"] for g in catalogue}
    cleaned = {}
    for guide, related in mapping.items():
        if guide not in valid_files:
            continue
        cleaned[guide] = [r for r in related if r in valid_files and r != guide][:4]

    return cleaned


# ── Step 2: Inject related cards into guide HTML ───────────────────────────────

def build_cards_html(guide_filename: str, related_filenames: list[str],
                     meta_map: dict[str, dict]) -> str:
    """Build the full Related Guides HTML block."""
    cards_html = []
    for rel_file in related_filenames:
        meta = meta_map.get(rel_file, {})
        title = meta.get("title", rel_file.replace("-", " ").replace(".html", "").title())
        subtitle = meta.get("subtitle", "")[:100]
        tag = meta.get("tag", "Guide")
        href = rel_file  # relative link — both files are in guides/

        cards_html.append(f"""        <a class="related-card" href="{href}">
          <div class="related-card-tag">{tag or "Guide"}</div>
          <div class="related-card-title">{title}</div>
          {'<div class="related-card-desc">' + subtitle + '</div>' if subtitle else ''}
          <div class="related-card-arrow">Read →</div>
        </a>""")

    # Build multilingual header
    span_parts = []
    for lang, label in SECTION_LABELS.items():
        hidden_attr = ' class="lang-hidden"' if lang != "en" else ""
        span_parts.append(f'<span data-lang="{lang}"{hidden_attr}>{label}</span>')
    header_spans = "\n          ".join(span_parts)

    cards_block = "\n".join(cards_html)

    return f"""
      <div class="related-guides">
        <h2>
          {header_spans}
        </h2>
        <div class="related-cards">
{cards_block}
        </div>
      </div>"""


RELATED_MARKER_START = "<!-- RELATED-GUIDES-START -->"
RELATED_MARKER_END   = "<!-- RELATED-GUIDES-END -->"


def inject_related_section(path: Path, related_filenames: list[str],
                            meta_map: dict[str, dict], dry_run: bool = False) -> str:
    html = path.read_text(encoding="utf-8")

    cards_html = build_cards_html(path.name, related_filenames, meta_map)
    block = f"\n    {RELATED_MARKER_START}{cards_html}\n    {RELATED_MARKER_END}\n"

    # If already injected, replace
    if RELATED_MARKER_START in html:
        new_html = re.sub(
            re.escape(RELATED_MARKER_START) + r".*?" + re.escape(RELATED_MARKER_END),
            RELATED_MARKER_START + cards_html + "\n    " + RELATED_MARKER_END,
            html,
            flags=re.DOTALL,
        )
        status = "updated"
    else:
        # Insert before </main> or before <footer class="guide-footer">
        target_patterns = [
            r'(<footer\s+class=["\']guide-footer["\'])',
            r'(</main>)',
        ]
        inserted = False
        new_html = html
        for pattern in target_patterns:
            if re.search(pattern, new_html, re.IGNORECASE):
                new_html = re.sub(pattern, block + r"\1", new_html, count=1, flags=re.IGNORECASE)
                inserted = True
                break

        if not inserted:
            return "WARN: could not find insertion point"
        status = "injected"

    # Inject CSS into <head> if not already there
    if "related-guides" not in new_html:
        new_html = new_html.replace("</head>", RELATED_CSS + "\n</head>", 1)
    elif "</head>" in new_html and ".related-guides {" not in new_html:
        new_html = new_html.replace("</head>", RELATED_CSS + "\n</head>", 1)

    if not dry_run:
        path.write_text(new_html, encoding="utf-8")

    return f"✓ {status} ({len(related_filenames)} cards)"


# ── Main ───────────────────────────────────────────────────────────────────────

def main():
    parser = argparse.ArgumentParser(
        description="Add Related Guides section to williamriveromd.com guide pages"
    )
    parser.add_argument("--api-key", help="Anthropic API key (required for --map-only or full run)")
    parser.add_argument("--map-only", action="store_true", help="Generate JSON map only, don't inject")
    parser.add_argument("--inject-only", action="store_true", help="Inject using existing related_guides.json")
    parser.add_argument("--dry-run", action="store_true", help="Preview without writing files")
    args = parser.parse_args()

    script_path = Path(__file__).resolve()
    try:
        project_dir = find_project_dir(script_path)
    except FileNotFoundError as e:
        print(f"ERROR: {e}")
        sys.exit(1)

    guides_dir = project_dir / "guides"
    map_path = project_dir / "related_guides.json"

    print(f"Project: {project_dir}")
    print(f"Guides:  {guides_dir}")

    # Build catalogue
    print("\nScanning guides...")
    catalogue = build_catalogue(guides_dir)
    print(f"Found {len(catalogue)} guides")
    meta_map = {g["filename"]: g for g in catalogue}

    # ── Generate map ──
    if not args.inject_only:
        if not args.api_key:
            print("ERROR: --api-key required to generate relationship map")
            sys.exit(1)
        client = anthropic.Anthropic(api_key=args.api_key)
        print("\nGenerating relationship map via Claude API...")
        mapping = generate_relationship_map(catalogue, client)

        if not args.dry_run:
            map_path.write_text(json.dumps(mapping, indent=2), encoding="utf-8")
            print(f"✓ Saved relationship map → {map_path}")
        else:
            print("[DRY RUN] Would save relationship map:")
            print(json.dumps(dict(list(mapping.items())[:5]), indent=2))
            print(f"  ... ({len(mapping)} total entries)")

        if args.map_only:
            print("\nDone. Review related_guides.json, then run:")
            print("  python3 add_related_guides.py --inject-only")
            return
    else:
        # Load existing map
        if not map_path.exists():
            print(f"ERROR: {map_path} not found. Run without --inject-only first.")
            sys.exit(1)
        mapping = json.loads(map_path.read_text(encoding="utf-8"))
        print(f"Loaded relationship map: {len(mapping)} entries")

    # ── Inject cards ──
    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Injecting related guide cards...")
    ok = 0
    warn = 0
    for guide_file, related in mapping.items():
        path = guides_dir / guide_file
        if not path.exists():
            print(f"  SKIP {guide_file} — file not found")
            continue
        if not related:
            print(f"  SKIP {guide_file} — no related guides defined")
            continue
        status = inject_related_section(path, related, meta_map, args.dry_run)
        if "✓" in status:
            ok += 1
            print(f"  {guide_file:55s} → {status}")
        else:
            warn += 1
            print(f"  {guide_file:55s} → {status}")

    print(f"\n{'[DRY RUN] ' if args.dry_run else ''}Summary:")
    print(f"  Guides processed: {ok}")
    print(f"  Warnings:         {warn}")

    if not args.dry_run and ok > 0:
        print("\nNext step — push to live:")
        print("  git add .")
        print('  git commit -m "Add related guides section to all guide pages"')
        print("  git push")


if __name__ == "__main__":
    main()
