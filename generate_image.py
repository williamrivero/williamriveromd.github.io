#!/usr/bin/env python3
"""
generate_image.py — image generator for williamriveromd.com guides.

Calls the OpenAI gpt-image API, saves PNG + WebP (q88) into images/, and
enforces a 5-images/minute rate limit. The API key is read at runtime from
$OPENAI_API_KEY or, failing that, from ~/.secrets/openai_key — it is never
stored in this file or committed.

Usage (run from repo root):

  # single image
  python3 generate_image.py "A photorealistic ..." --name el-nino-heat-dialysis-hero --size 1536x1024

  # clinician algorithm (auto-applies the conservative flowchart style)
  python3 generate_image.py "Outpatient hyperkalemia pathway ..." \
      --name poa2-hyperkalemia --style algorithm

  # batch: JSON array of {"name","prompt","size"?,"style"?}
  python3 generate_image.py --batch prompts.json

  # preview prompts without calling the API or spending credits
  python3 generate_image.py --batch prompts.json --dry-run
"""

import argparse
import base64
import json
import os
import sys
import time
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent
IMAGES_DIR = REPO_ROOT / "images"
SECRET_FALLBACK = Path.home() / ".secrets" / "openai_key"

DEFAULT_MODEL = os.environ.get("IMAGE_MODEL", "gpt-image-2")
FALLBACK_MODEL = "gpt-image-1"
WEBP_QUALITY = 88

# Rate limit: 5 images/min -> 14s between images, 65s between batches of 5.
PER_IMAGE_SLEEP = 14
BATCH_SIZE = 5
BATCH_SLEEP = 65

# Conservative clinical-flowchart style anchor (the proven "v3" look).
ALGORITHM_STYLE = (
    " Clean medical textbook clinical flowchart. White background. Simple "
    "rectangular boxes with thin black borders. Diamond shapes for decision "
    "nodes. Plain black arrows. Minimal color: light grey for neutral steps, "
    "soft red for urgent or critical branches, soft yellow for action or "
    "treatment boxes, light blue for section headers. Dense clinical text, "
    "small readable sans-serif font. No icons, no 3D elements, no gradients, "
    "no decorative graphics, no illustrations. Publication-quality clinical "
    "algorithm infographic."
)

# Always appended — the AJKD-watermark lesson: never let the model render
# journal / guideline / brand names as literal text in the image.
NO_WATERMARK_GUARD = (
    " No journal names, guideline acronyms, brand names, organization names, "
    "signatures, or watermarks anywhere in the image."
)


def load_api_key() -> str:
    key = os.environ.get("OPENAI_API_KEY", "").strip()
    if not key and SECRET_FALLBACK.exists():
        key = SECRET_FALLBACK.read_text().strip()
    if not key:
        sys.exit(
            "ERROR: no API key. Set OPENAI_API_KEY or place it in "
            f"{SECRET_FALLBACK}"
        )
    return key


def build_prompt(prompt: str, style: str | None) -> str:
    final = prompt.strip()
    if style == "algorithm":
        final += ALGORITHM_STYLE
    return final + NO_WATERMARK_GUARD


def save_outputs(image_bytes: bytes, name: str) -> tuple[Path, Path]:
    from PIL import Image
    import io

    IMAGES_DIR.mkdir(parents=True, exist_ok=True)
    png_path = IMAGES_DIR / f"{name}.png"
    webp_path = IMAGES_DIR / f"{name}.webp"

    png_path.write_bytes(image_bytes)
    img = Image.open(io.BytesIO(image_bytes)).convert("RGB")
    img.save(webp_path, "WEBP", quality=WEBP_QUALITY, method=6)
    return png_path, webp_path


def generate_one(client, item: dict) -> dict:
    name = item["name"]
    size = item.get("size", "1024x1024")
    final_prompt = build_prompt(item["prompt"], item.get("style"))

    model = DEFAULT_MODEL
    try:
        resp = _call(client, model, final_prompt, size)
    except Exception as e:
        msg = str(e).lower()
        if "model" in msg and ("not" in msg or "exist" in msg or "access" in msg):
            print(f"       model {model} unavailable -> falling back to {FALLBACK_MODEL}")
            model = FALLBACK_MODEL
            resp = _call(client, model, final_prompt, size)
        else:
            raise

    image_bytes = base64.b64decode(resp.data[0].b64_json)
    png_path, webp_path = save_outputs(image_bytes, name)
    return {"name": name, "png": str(png_path), "webp": str(webp_path),
            "model": model, "status": "ok"}


def _call(client, model: str, prompt: str, size: str):
    return client.images.generate(model=model, prompt=prompt, n=1, size=size)


def run(items: list[dict], dry_run: bool) -> list[dict]:
    for i, it in enumerate(items, 1):
        if "name" not in it or "prompt" not in it:
            sys.exit(f"ERROR: item {i} needs both 'name' and 'prompt'")

    if dry_run:
        for i, it in enumerate(items, 1):
            print(f"\n[{i}/{len(items)}] {it['name']}  ({it.get('size','1024x1024')})")
            print(build_prompt(it["prompt"], it.get("style")))
        print(f"\nDRY RUN — {len(items)} prompt(s), no API calls made.")
        return []

    import openai
    client = openai.OpenAI(api_key=load_api_key())

    results = []
    for i, it in enumerate(items):
        if i > 0 and i % BATCH_SIZE == 0:
            print(f"\n-- rate-limit batch pause: {BATCH_SLEEP}s --\n")
            time.sleep(BATCH_SLEEP)
        elif i > 0:
            time.sleep(PER_IMAGE_SLEEP)

        n = i + 1
        print(f"[{n}/{len(items)}] {it['name']} ...")
        try:
            r = generate_one(client, it)
            print(f"       OK  {r['png']}  +  {r['webp']}  ({r['model']})")
            results.append(r)
        except Exception as e:
            print(f"       FAILED: {e}")
            results.append({"name": it["name"], "status": "failed", "error": str(e)})

    ok = sum(1 for r in results if r.get("status") == "ok")
    print(f"\nDone: {ok}/{len(items)} succeeded.")
    return results


def main():
    ap = argparse.ArgumentParser(description="Image generator for williamriveromd.com")
    ap.add_argument("prompt", nargs="?", help="Prompt text (single-image mode)")
    ap.add_argument("--name", help="Output filename stem (no extension)")
    ap.add_argument("--size", default="1024x1024",
                    help="1024x1024 | 1536x1024 | 1024x1536 (default 1024x1024)")
    ap.add_argument("--style", choices=["algorithm"],
                    help="Apply a preset style anchor (algorithm = clinical flowchart)")
    ap.add_argument("--batch", help="Path to a JSON array of image specs")
    ap.add_argument("--dry-run", action="store_true",
                    help="Print final prompts without calling the API")
    args = ap.parse_args()

    if args.batch:
        items = json.loads(Path(args.batch).read_text())
    elif args.prompt and args.name:
        items = [{"name": args.name, "prompt": args.prompt,
                  "size": args.size, **({"style": args.style} if args.style else {})}]
    else:
        ap.error("provide either --batch FILE, or PROMPT with --name")

    run(items, args.dry_run)


if __name__ == "__main__":
    main()
