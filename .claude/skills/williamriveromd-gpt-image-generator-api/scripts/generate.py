#!/usr/bin/env python3
"""
williamriveromd-gpt-image-generator/scripts/generate.py

Standalone script for batch image generation via gpt-image-2.
Called by Claude when executing an image plan from williamriveromd-image-planner.

Usage:
    python generate.py --prompts prompts.json --output /mnt/user-data/outputs/images/

prompts.json format:
[
  {
    "filename": "ckd-acidosis-hero.png",
    "size": "1536x1024",
    "prompt": "Medical education infographic for williamriveromd.com. Filipino healthcare context. Clinically accurate. Restrained professional aesthetic.\n1. IMAGE TYPE: Hero\n2. PRIMARY VISUAL STYLE: EDITORIAL_PHOTO\n..."
  },
  ...
]
"""

import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path

try:
    import openai
except ImportError:
    print("Installing openai...")
    os.system("pip install openai --break-system-packages -q")
    import openai

# ── Constants ──────────────────────────────────────────────────────────────────
MODEL = "gpt-image-2"
RATE_LIMIT = 5          # images per window
WINDOW_SECONDS = 62     # seconds between batches (60s + 2s buffer)
QUALITY = "high"

CONTEXT_PREFIX = (
    "Medical education infographic for williamriveromd.com. "
    "Filipino healthcare context. Clinically accurate. "
    "Restrained professional aesthetic.\n\n"
)

# ── Valid OpenAI sizes ─────────────────────────────────────────────────────────
VALID_SIZES = {
    "1536x1024", "1024x1536", "1024x1024",
    "1280x960",  "960x1280",
    "1792x1024", "1024x1792",
}

SIZE_FALLBACK_MAP = {
    "1024x768":  "1024x1024",
    "1280x960":  "1280x960",
    "1400x1000": "1536x1024",
    "768x512":   "1024x1024",
    "1536x1024": "1536x1024",
    "1024x1024": "1024x1024",
}


def resolve_size(requested: str) -> tuple[str, str | None]:
    """Return (openai_size, substitution_note_or_None)."""
    if requested in VALID_SIZES:
        return requested, None
    fallback = SIZE_FALLBACK_MAP.get(requested)
    if fallback:
        return fallback, f"Dimension {requested} → substituted {fallback}"
    return "1024x1024", f"Dimension {requested} unrecognised → fallback 1024x1024"


def generate_one(client, prompt: str, size: str, filename: str, output_dir: Path) -> str:
    """Generate one image. Returns saved file path."""
    full_prompt = CONTEXT_PREFIX + prompt if not prompt.startswith("Medical education") else prompt

    response = client.images.generate(
        model=MODEL,
        prompt=full_prompt,
        n=1,
        size=size,
        response_format="b64_json",
        quality=QUALITY,
    )

    image_bytes = base64.b64decode(response.data[0].b64_json)
    out_path = output_dir / filename
    out_path.write_bytes(image_bytes)
    return str(out_path)


def batch_generate(prompts: list[dict], output_dir: Path) -> list[dict]:
    """
    Generate all images with rate limiting.
    Returns list of result dicts: {filename, path, status, note}.
    """
    api_key = os.environ.get("OPENAI_API_KEY")
    if not api_key:
        print("ERROR: OPENAI_API_KEY environment variable is not set.", file=sys.stderr)
        sys.exit(1)

    client = openai.OpenAI(api_key=api_key)
    output_dir.mkdir(parents=True, exist_ok=True)

    total = len(prompts)
    n_batches = (total + RATE_LIMIT - 1) // RATE_LIMIT
    est_minutes = n_batches + (n_batches - 1)

    print(f"\n{'─'*55}")
    print(f"  gpt-image-2 Batch Generator — williamriveromd.com")
    print(f"{'─'*55}")
    print(f"  Images:     {total}")
    print(f"  Batches:    {n_batches}  ({RATE_LIMIT}/min limit)")
    print(f"  Est. time:  ~{est_minutes}–{est_minutes+1} min")
    print(f"  Output dir: {output_dir}")
    print(f"{'─'*55}\n")

    results = []

    for i, item in enumerate(prompts):
        # Rate limit pause between batches
        if i > 0 and i % RATE_LIMIT == 0:
            print(f"\n⏸  Rate limit pause — waiting {WINDOW_SECONDS}s...\n")
            time.sleep(WINDOW_SECONDS)

        filename = item["filename"]
        requested_size = item.get("size", "1024x1024")
        prompt = item["prompt"]

        resolved_size, note = resolve_size(requested_size)

        print(f"[{i+1}/{total}] {filename}  ({resolved_size})")
        if note:
            print(f"       ⚠ {note}")

        try:
            path = generate_one(client, prompt, resolved_size, filename, output_dir)
            print(f"       ✓ Saved: {path}")
            results.append({"filename": filename, "path": path, "status": "ok", "note": note or ""})

        except openai.RateLimitError:
            print(f"       ↺ Rate limit hit — retrying after 62s...")
            time.sleep(62)
            try:
                path = generate_one(client, prompt, resolved_size, filename, output_dir)
                print(f"       ✓ Saved (retry): {path}")
                results.append({"filename": filename, "path": path, "status": "ok", "note": "rate limit retry"})
            except Exception as e:
                print(f"       ✗ FAILED after retry: {e}")
                results.append({"filename": filename, "path": None, "status": "failed", "note": str(e)})

        except openai.BadRequestError as e:
            print(f"       ✗ SKIPPED — content policy: {e}")
            results.append({"filename": filename, "path": None, "status": "skipped", "note": f"content policy: {e}"})

        except Exception as e:
            print(f"       ↺ Error — retrying after 10s: {e}")
            time.sleep(10)
            try:
                path = generate_one(client, prompt, resolved_size, filename, output_dir)
                print(f"       ✓ Saved (retry): {path}")
                results.append({"filename": filename, "path": path, "status": "ok", "note": "network retry"})
            except Exception as e2:
                print(f"       ✗ FAILED: {e2}")
                results.append({"filename": filename, "path": None, "status": "failed", "note": str(e2)})

    # ── Summary ────────────────────────────────────────────────────────────────
    ok = [r for r in results if r["status"] == "ok"]
    failed = [r for r in results if r["status"] == "failed"]
    skipped = [r for r in results if r["status"] == "skipped"]

    print(f"\n{'─'*55}")
    print(f"  GENERATION COMPLETE")
    print(f"{'─'*55}")
    print(f"  ✓ Success:  {len(ok)}/{total}")
    if skipped:
        print(f"  ⊘ Skipped:  {len(skipped)} (content policy)")
    if failed:
        print(f"  ✗ Failed:   {len(failed)}")
    print(f"{'─'*55}")
    for r in results:
        status_icon = "✓" if r["status"] == "ok" else ("⊘" if r["status"] == "skipped" else "✗")
        print(f"  {status_icon}  {r['filename']}")
    print(f"{'─'*55}\n")

    return results


def main():
    parser = argparse.ArgumentParser(description="gpt-image-2 batch generator for williamriveromd.com")
    parser.add_argument("--prompts", required=True, help="Path to prompts JSON file")
    parser.add_argument("--output", default="/mnt/user-data/outputs/images/", help="Output directory")
    args = parser.parse_args()

    with open(args.prompts) as f:
        prompts = json.load(f)

    results = batch_generate(prompts, Path(args.output))

    # Write results JSON for Claude to parse
    results_path = Path(args.output) / "_generation_results.json"
    with open(results_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"Results written to: {results_path}")


if __name__ == "__main__":
    main()
