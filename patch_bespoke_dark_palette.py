#!/usr/bin/env python3
"""Bump contrast-failing values in per-guide bespoke dark palettes.

Many guides define their own html[data-theme="dark"] { --navy: ...;
--text-muted: ...; ... } block in their second <style>. The historical
values for --text-muted (#7a859a) and --text-faint default to ~3.9:1
contrast on dark cards — fails WCAG AA. This script bumps those tokens
to the same values master CSS now uses (#9ba6b8 / #9aa4b8) so guide
text inherits the corrected contrast.

Idempotent: only rewrites when an old value is detected.
"""
import re, sys, pathlib

GUIDES_DIR = pathlib.Path(__file__).parent / "guides"

# (token, old-value, new-value)
BUMPS = [
    # --text-muted: bump anything below 4.5:1 on a dark card to a safe value
    ("--text-muted", "#7a859a", "#9ba6b8"),
    ("--text-muted", "#7A859A", "#9ba6b8"),
    ("--text-muted", "#8a95a8", "#9ba6b8"),
    ("--text-muted", "#8A95A8", "#9ba6b8"),
    ("--text-muted", "#8a97a8", "#9ba6b8"),
    ("--text-muted", "#8A97A8", "#9ba6b8"),
    # --text-faint defaults
    ("--text-faint", "#8090a4", "#9ba6b8"),
    ("--text-faint", "#8090A4", "#9ba6b8"),
    # advance-care-planning's overly-light --navy was being used as a
    # header background — keep its purpose but darken so anti-aliased
    # white text on it reaches ≥4.5:1
    ("--navy", "#4a72c4", "#1f3864"),
    ("--navy", "#4A72C4", "#1f3864"),
]

# Match `html[data-theme="dark"] { ... }` blocks (greedy until the matching `}` on its own line)
DARK_BLOCK = re.compile(
    r'(html\[data-theme="dark"\]\s*\{[^}]*\})',
    re.DOTALL,
)


def patch_file(path: pathlib.Path, dry: bool) -> bool:
    src = path.read_text(encoding="utf-8")
    new = src
    for m in DARK_BLOCK.finditer(src):
        block = m.group(1)
        fixed = block
        for tok, old, new_v in BUMPS:
            fixed = re.sub(
                rf"({re.escape(tok)}\s*:\s*){re.escape(old)}",
                rf"\g<1>{new_v}",
                fixed,
            )
        if fixed != block:
            new = new.replace(block, fixed)
    if new == src:
        return False
    if not dry:
        path.write_text(new, encoding="utf-8")
    return True


def main():
    dry = "--dry-run" in sys.argv
    only = None
    for i, a in enumerate(sys.argv):
        if a == "--guide" and i + 1 < len(sys.argv):
            only = sys.argv[i + 1]

    targets = sorted(GUIDES_DIR.glob("*.html"))
    if only:
        targets = [GUIDES_DIR / only]

    changed = 0
    for p in targets:
        if patch_file(p, dry):
            print(f"  {p.name:55s} → {'would change' if dry else 'patched'}")
            changed += 1
    print(f"\nSummary: {changed} file(s) {'would be ' if dry else ''}changed")


if __name__ == "__main__":
    main()
