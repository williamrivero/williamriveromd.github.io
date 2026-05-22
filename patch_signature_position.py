#!/usr/bin/env python3
"""
patch_signature_position.py
============================
Ensures every guide ends with the canonical page tail:

    [all content / </main>]
    <!-- DR CARD -->
    <div class="dr-card-wrap">…</div>
    <!-- RELATED-GUIDES-START -->          (if present)
    <div class="related-guides">…</div>
    <!-- RELATED-GUIDES-END -->            (if present)
    <footer class="guide-footer">…</footer>
    [any trailing elements: scroll-top button, scripts, </body>, </html>]

Usage:
    python3 patch_signature_position.py              # all guides
    python3 patch_signature_position.py --dry-run    # preview only
    python3 patch_signature_position.py --guide obesity-ckd.html
"""

import re
import os
import glob
import argparse

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------

def _extract_div_block(text, start_idx):
    """
    Starting at start_idx (which must be the '<' of an opening <div …>),
    walk forward counting div opens/closes and return (block_str, end_idx)
    where end_idx is the character just after the closing tag.

    Handles the case where some guides use </section> to close the outer
    <div class="related-guides"> (mismatched but browser-tolerated).
    """
    depth = 0
    i = start_idx
    n = len(text)
    while i < n:
        if text[i:i+4] == '<div':
            if i + 4 < n and text[i+4] in ' \t\n\r>/':
                depth += 1
        if text[i:i+6] == '</div>':
            depth -= 1
            if depth == 0:
                end = i + 6
                return text[start_idx:end], end
        # Some guides close the related-guides <div> with </section> (mismatched HTML)
        if text[i:i+10] == '</section>' and depth == 1:
            end = i + 10
            return text[start_idx:end], end
        i += 1
    return None, -1


def _strip_leading_whitespace_and_comment(text, pos):
    """
    Walk *backwards* from pos, consuming whitespace and an optional
    <!-- ... --> comment (the DR CARD or RELATED-GUIDES-START comments).
    Returns the new start position.
    """
    i = pos - 1
    # Strip trailing whitespace before the block
    while i >= 0 and text[i] in ' \t\n\r':
        i -= 1
    # If we hit '-->' it's a closing comment tag; eat the whole comment
    if text[max(0,i-2):i+1] == '-->':
        j = text.rfind('<!--', 0, i)
        if j != -1:
            i = j - 1
            # Strip whitespace before that too
            while i >= 0 and text[i] in ' \t\n\r':
                i -= 1
    return i + 1


def _strip_trailing_whitespace_and_comment(text, pos):
    """
    Walk *forwards* from pos, consuming whitespace and an optional
    <!-- ... --> comment (RELATED-GUIDES-END).
    Returns the new end position.

    Does NOT consume whitespace that immediately precedes a non-comment element
    (to avoid eating the newline before <footer>).
    """
    n = len(text)
    i = pos
    # Consume a single trailing newline sequence after the closing tag
    if i < n and text[i] == '\n':
        i += 1
        if i < n and text[i] == '\r':
            i += 1
    # Consume horizontal whitespace
    while i < n and text[i] in ' \t':
        i += 1
    # If we see a comment, consume it and one more newline
    if i < n and text[i:i+4] == '<!--':
        j = text.find('-->', i)
        if j != -1:
            i = j + 3
            if i < n and text[i] == '\n':
                i += 1
    return i


def patch_guide(path, dry_run=False):
    with open(path, encoding='utf-8') as fh:
        original = fh.read()

    text = original

    # -----------------------------------------------------------------------
    # 1. Fix the malformed  <section <!-- DR CARD -->  tag (obesity-ckd only)
    # -----------------------------------------------------------------------
    text = re.sub(r'<section\s+<!--\s*DR CARD\s*-->\s*\n', '<!-- DR CARD -->\n', text)

    # -----------------------------------------------------------------------
    # 2. Locate <footer class="guide-footer"
    # -----------------------------------------------------------------------
    footer_m = re.search(r'(<footer class="guide-footer")', text)
    if not footer_m:
        return False, "no guide-footer found"
    footer_start = footer_m.start()   # position of the < of <footer

    # -----------------------------------------------------------------------
    # 3. Locate the dr-card-wrap block
    # -----------------------------------------------------------------------
    dr_m = re.search(r'<div class="dr-card-wrap">', text)
    if not dr_m:
        return False, "no dr-card-wrap found"

    dr_block, dr_end = _extract_div_block(text, dr_m.start())
    if dr_block is None:
        return False, "could not parse dr-card-wrap block"

    # Expand to include any preceding <!-- DR CARD --> comment
    dr_block_start = _strip_leading_whitespace_and_comment(text, dr_m.start())
    # Expand to include any trailing whitespace
    dr_block_end_ext = dr_end
    while dr_block_end_ext < len(text) and text[dr_block_end_ext] in ' \t':
        dr_block_end_ext += 1
    # Consume one trailing newline
    if dr_block_end_ext < len(text) and text[dr_block_end_ext] == '\n':
        dr_block_end_ext += 1

    full_dr_block = text[dr_block_start:dr_block_end_ext]

    # -----------------------------------------------------------------------
    # 4. Locate the related-guides block (if present)
    #    Search from after the dr-card-wrap to avoid matching a second
    #    related-guides div that may exist inside physician-mode content.
    # -----------------------------------------------------------------------
    rg_m_rel = re.search(r'<div class="related-guides"[^>]*>', text[dr_m.start():])
    # Adjust to absolute position in text
    rg_abs_start = (dr_m.start() + rg_m_rel.start()) if rg_m_rel else None

    full_rg_block = ''
    rg_block_start = rg_block_end = -1

    if rg_abs_start is not None:
        rg_block, rg_end = _extract_div_block(text, rg_abs_start)
        if rg_block is None:
            return False, "could not parse related-guides block"

        # Expand to include preceding comment/whitespace
        rg_block_start = _strip_leading_whitespace_and_comment(text, rg_abs_start)
        # Expand to include trailing comment/whitespace (RELATED-GUIDES-END)
        rg_block_end = _strip_trailing_whitespace_and_comment(text, rg_end)

        full_rg_block = text[rg_block_start:rg_block_end]

    # Keep a truthy flag consistent with original rg_m usage
    rg_m = rg_m_rel

    # -----------------------------------------------------------------------
    # 5. Check whether signature + related-guides are already right before footer
    # -----------------------------------------------------------------------
    # Build what should come right before the footer (ignoring whitespace)
    def _squish(s):
        return re.sub(r'\s+', '', s)

    if rg_m:
        expected_pre_footer = _squish(full_dr_block + full_rg_block)
    else:
        expected_pre_footer = _squish(full_dr_block)

    # Grab the text between the last of {dr_end, rg_block_end} and footer_start
    last_block_end = rg_block_end if (rg_m and rg_block_end != -1) else dr_block_end_ext
    gap = text[last_block_end:footer_start]
    gap_squished = _squish(gap)

    # If there is nothing substantial between the blocks and the footer,
    # and they appear in the right order (dr before rg before footer), skip.
    already_correct = (
        dr_m.start() < footer_start and
        (not rg_m or (rg_abs_start > dr_m.start() and rg_abs_start < footer_start)) and
        gap_squished == '' and
        dr_block_start >= 0 and
        (not rg_m or rg_block_start > dr_block_start)
    )

    if already_correct:
        if text != original:
            # Only the malformed section tag was fixed
            pass
        else:
            return False, "already correct"

    # -----------------------------------------------------------------------
    # 6. Remove dr-card and related-guides from their current positions
    # -----------------------------------------------------------------------
    # Work on positions; remove higher-index block first to preserve indices.
    blocks = []
    blocks.append((dr_block_start, dr_block_end_ext, full_dr_block))
    if rg_m:
        blocks.append((rg_block_start, rg_block_end, full_rg_block))

    # Sort descending by start so removals don't shift earlier indices
    blocks.sort(key=lambda x: x[0], reverse=True)

    working = text
    for bstart, bend, _ in blocks:
        working = working[:bstart] + working[bend:]

    # -----------------------------------------------------------------------
    # 7. Clean up extra blank lines left by the removal
    # -----------------------------------------------------------------------
    working = re.sub(r'\n{3,}', '\n\n', working)

    # -----------------------------------------------------------------------
    # 8. Re-locate footer in the modified text and insert signature tail
    # -----------------------------------------------------------------------
    footer_m2 = re.search(r'(<footer class="guide-footer")', working)
    if not footer_m2:
        return False, "footer disappeared after extraction"

    insert_at = footer_m2.start()

    # Build the tail: newline + DR CARD comment + dr_block + rg_block
    dr_html = full_dr_block.strip()
    tail = '\n\n<!-- DR CARD -->\n' + dr_html + '\n'

    if rg_m:
        rg_html = full_rg_block.strip()
        # Make sure there's a RELATED-GUIDES-START comment if not already in block
        if '<!-- RELATED-GUIDES-START -->' not in rg_html:
            rg_html = '<!-- RELATED-GUIDES-START -->\n' + rg_html + '\n<!-- RELATED-GUIDES-END -->'
        tail += '\n' + rg_html + '\n'

    result = working[:insert_at] + tail + working[insert_at:]

    # -----------------------------------------------------------------------
    # 9. Final cleanup: collapse runs of 3+ blank lines again
    # -----------------------------------------------------------------------
    result = re.sub(r'\n{4,}', '\n\n', result)

    if result == original:
        return False, "no change"

    if dry_run:
        print(f"[DRY-RUN] Would patch: {path}")
        return True, "would patch"

    with open(path, 'w', encoding='utf-8') as fh:
        fh.write(result)
    return True, "patched"


# ---------------------------------------------------------------------------
# CLI
# ---------------------------------------------------------------------------

def main():
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument('--dry-run', action='store_true',
                        help='Preview changes without writing files')
    parser.add_argument('--guide', metavar='FILENAME',
                        help='Process a single guide (filename only, e.g. obesity-ckd.html)')
    args = parser.parse_args()

    if args.guide:
        candidates = [os.path.join('guides', args.guide)]
    else:
        candidates = sorted(glob.glob('guides/*.html'))

    patched = skipped = errors = 0
    for path in candidates:
        changed, reason = patch_guide(path, dry_run=args.dry_run)
        if changed:
            print(f"  PATCHED : {path}")
            patched += 1
        elif reason == "already correct" or reason == "no change":
            skipped += 1
        else:
            print(f"  SKIP    : {path}  ({reason})")
            errors += 1

    print(f"\n{'DRY-RUN ' if args.dry_run else ''}Done — patched={patched}  skipped={skipped}  errors/skipped={errors}")


if __name__ == '__main__':
    main()
