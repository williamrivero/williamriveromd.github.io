#!/usr/bin/env python3
"""
patch_zoomable_dblclick.py

Adds a tiny JS snippet to every guide that has img.zoomable elements so that
double-clicking (desktop) or double-tapping (mobile) any zoomable image opens
the full-size image in a new tab.

Usage:
  python3 patch_zoomable_dblclick.py            # patch all guides
  python3 patch_zoomable_dblclick.py --dry-run  # preview without writing
  python3 patch_zoomable_dblclick.py --guide practical-outpatient-algorithms.html
"""

import argparse
import os
import re
import sys

GUIDES_DIR = os.path.join(os.path.dirname(__file__), 'guides')

SNIPPET_MARKER = 'zoomable-dblclick-handler'

SNIPPET = """\
<script>/* %s */
(function(){
  var _last={el:null,t:0};
  document.addEventListener('click',function(e){
    var img=e.target.closest?e.target.closest('img.zoomable'):null;
    if(!img&&e.target.matches&&e.target.matches('img.zoomable'))img=e.target;
    if(!img)return;
    var now=Date.now();
    if(_last.el===img&&now-_last.t<400){
      window.open(img.src,'_blank','noopener,noreferrer');
      _last={el:null,t:0};
    }else{
      _last={el:img,t:now};
    }
  });
})();
</script>""" % SNIPPET_MARKER

INSERT_BEFORE = '</body>'


def patch_file(path, dry_run=False):
    with open(path, 'r', encoding='utf-8') as f:
        html = f.read()

    if 'class="zoomable"' not in html and "class='zoomable'" not in html:
        return 'skip'

    if SNIPPET_MARKER in html:
        return 'already'

    if INSERT_BEFORE not in html:
        return 'no-body-tag'

    new_html = html.replace(INSERT_BEFORE, SNIPPET + '\n' + INSERT_BEFORE, 1)

    if not dry_run:
        with open(path, 'w', encoding='utf-8') as f:
            f.write(new_html)
    return 'patched'


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--guide', help='Single guide filename (e.g. practical-outpatient-algorithms.html)')
    args = parser.parse_args()

    if args.guide:
        files = [os.path.join(GUIDES_DIR, args.guide)]
    else:
        files = sorted(
            os.path.join(GUIDES_DIR, f)
            for f in os.listdir(GUIDES_DIR)
            if f.endswith('.html')
        )

    counts = {'patched': 0, 'already': 0, 'skip': 0, 'no-body-tag': 0}
    for path in files:
        result = patch_file(path, dry_run=args.dry_run)
        counts[result] += 1
        if result == 'patched':
            label = '[DRY RUN] would patch' if args.dry_run else 'patched'
            print(f'  {label}: {os.path.basename(path)}')
        elif result == 'no-body-tag':
            print(f'  WARNING: no </body> tag in {os.path.basename(path)}')

    print(f"\nDone. patched={counts['patched']}  already={counts['already']}  "
          f"skip (no zoomable)={counts['skip']}  warnings={counts['no-body-tag']}")


if __name__ == '__main__':
    main()
