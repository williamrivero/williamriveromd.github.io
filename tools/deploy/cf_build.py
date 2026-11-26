#!/usr/bin/env python3
"""Cloudflare Pages build step: copy only the files the website serves into _site/.

Cloudflare Pages accepts at most 20,000 files per deployment, and the repo also holds
generators, data sources, prompts and docs that the site never serves. This script
publishes the tracked website files and leaves the rest out.

Cloudflare Pages settings (Settings > Builds):
  Build command:           python3 tools/deploy/cf_build.py
  Build output directory:  _site

Local check (no copying):  python3 tools/deploy/cf_build.py --dry-run
"""
import os, shutil, subprocess, sys
from collections import Counter

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
OUT = os.path.join(ROOT, "_site")
LIMIT = 20000

# Folders the site never serves (build sources, prompts, notes, tests).
EXCLUDE_DIRS = ("tools/", "image-prompts/", "blueprints/", "wgmr-image-prompts/", "work/", "tmp/",
                "scripts-qa/", "scripts_i18n/", "tests/", "olmocr/", "docs/", ".github/", ".claude/",
                "functions/", "functions-lib/")   # Pages Functions source (compiled by Cloudflare, never served as files)
# data/ holds generator inputs; only these subfolders are read by pages in the browser.
DATA_SERVED = ("data/drugs/supplements/", "data/allocation-calculators/")
EXCLUDE_EXT = (".py", ".pyc", ".md", ".sh", ".cjs", ".log", ".command")


def served(path):
    if path.startswith(DATA_SERVED):
        return True
    if path.startswith("data/"):
        return False
    if path.startswith(EXCLUDE_DIRS):
        return path.startswith("tools/") and path.endswith(".html")   # keep any standalone tool page
    if "__pycache__/" in path or path.endswith(EXCLUDE_EXT):
        return False
    return True


def main():
    files = subprocess.run(["git", "ls-files", "-z"], cwd=ROOT, capture_output=True, check=True).stdout.decode().split("\0")
    files = [f for f in files if f]
    keep = [f for f in files if served(f)]
    left = Counter(f.split("/")[0] for f in files if not served(f))
    print(f"tracked files: {len(files)}  published: {len(keep)}  left out: {len(files) - len(keep)}")
    print("left out by folder:", ", ".join(f"{k} {v}" for k, v in left.most_common(8)))
    if len(keep) > LIMIT:
        sys.exit(f"ERROR: {len(keep)} files exceeds the Cloudflare Pages limit of {LIMIT}")
    if "--dry-run" in sys.argv:
        return
    shutil.rmtree(OUT, ignore_errors=True)
    for f in keep:
        src = os.path.join(ROOT, f)
        if not os.path.isfile(src):          # skip submodules or missing files
            continue
        dst = os.path.join(OUT, f)
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        try:
            os.link(src, dst)                 # hard link: fast, no extra disk
        except OSError:
            shutil.copy2(src, dst)
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
