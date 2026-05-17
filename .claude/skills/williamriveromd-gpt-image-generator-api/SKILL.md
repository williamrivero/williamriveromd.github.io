---
name: williamriveromd-gpt-image-generator-api
description: >
  Generate medical education images for williamriveromd.com using the OpenAI gpt-image-2 API
  (requires the OPENAI_API_KEY environment variable).
  Trigger this skill whenever Dr. Rivero says "GPT image: [description]", or whenever the
  williamriveromd-image-planner skill has finished producing a complete image plan and prompts
  are ready for execution. This skill takes a structured 10-point image prompt (from the image
  planner or typed directly), calls gpt-image-2 via the OpenAI API, displays the result inline,
  saves it to disk with the correct filename, and enforces the 5-images-per-minute rate limit.
  Always trigger when image planner prompts are ready for generation, even if Dr. Rivero does
  not explicitly say "GPT image" — if an image plan has just been produced, offer to execute it.
---

# WilliamRiveroMD — GPT Image Generator

Generates images for williamriveromd.com using `gpt-image-2` via the OpenAI API.
Accepts prompts directly or from the image planner skill output.
Displays inline + saves to disk. Enforces rate limits automatically.

---

## Prerequisites

- **API key**: Read from environment variable `OPENAI_API_KEY`. Never hardcode.
- **Python packages**: `openai`, `Pillow`, `requests` — install if missing:
  ```bash
  pip install openai Pillow requests --break-system-packages -q
  ```
- **Model**: `gpt-image-2` (snapshot: `gpt-image-2-2026-04-21`)
- **Endpoint**: `v1/images/generations`

---

## Step 1 — Parse Input

Accept input in two modes:

### Mode A — Direct invocation
User types: `GPT image: [description or 10-point prompt block]`
Extract the prompt text. If it is a full 10-point block from the image planner, parse fields
7 (COLOR PALETTE), 10 (DIMENSIONS), and use the full block as the generation prompt.

### Mode B — Image planner handoff (integrated mode)
The image planner has produced a complete IMAGE PLAN document. Detect this when:
- The conversation contains a structured IMAGE PLAN with 10-point prompt blocks, AND
- Dr. Rivero says "generate", "execute", "run", "go ahead", or similar confirmation.

In Mode B: extract ALL image prompts from the plan in order, note their filenames and
dimensions, then proceed to Step 2.

---

## Step 2 — Build the Generation Request

For each image prompt, construct the API call:

```python
import openai, os, base64, time
from pathlib import Path

client = openai.OpenAI(api_key=os.environ["OPENAI_API_KEY"])

def generate_image(prompt: str, size: str, filename: str, output_dir: str) -> str:
    """
    Call gpt-image-2, save to disk, return local file path.
    size: OpenAI size string — see dimension mapping below.
    """
    response = client.images.generate(
        model="gpt-image-2",
        prompt=prompt,
        n=1,
        size=size,
        response_format="b64_json",   # base64 — avoids URL expiry issues
        quality="high",               # always high for medical education content
    )
    image_data = base64.b64decode(response.data[0].b64_json)
    out_path = Path(output_dir) / filename
    out_path.write_bytes(image_data)
    return str(out_path)
```

### Dimension mapping (from image planner → OpenAI size string)

| Image planner dimension | OpenAI `size` value |
|---|---|
| 1536×1024 (hero) | `"1536x1024"` |
| 1024×768 (inline educational) | `"1024x1024"` ← nearest supported; note in output |
| 1280×960 (infographic) | `"1280x960"` or `"1024x1024"` fallback |
| 1400×1000 (flowchart) | `"1536x1024"` ← use landscape; note in output |
| 768×512 (reference card) | `"1024x1024"` ← square fallback; note in output |

Always note any dimension substitution in the output log.

### Prompt construction rule
Pass the **full 10-point prompt block** as the generation prompt — do not truncate.
Prepend this system framing line before the prompt body:

```
Medical education infographic for williamriveromd.com. Filipino healthcare context.
Clinically accurate. Restrained professional aesthetic. [THEN: full 10-point prompt]
```

---

## Step 3 — Rate Limiting (MANDATORY)

`gpt-image-2` on Tier 1 accounts: **5 images per minute hard limit.**

```python
RATE_LIMIT = 5          # max images per window
WINDOW_SECONDS = 62     # 62s (2s buffer over 60s)

def batch_generate(prompts: list[dict], output_dir: str):
    """
    prompts: list of {prompt, size, filename}
    Handles batching and rate limiting automatically.
    """
    results = []
    for i, item in enumerate(prompts):
        if i > 0 and i % RATE_LIMIT == 0:
            print(f"Rate limit pause — waiting {WINDOW_SECONDS}s before next batch...")
            time.sleep(WINDOW_SECONDS)
        print(f"Generating image {i+1}/{len(prompts)}: {item['filename']}")
        path = generate_image(item["prompt"], item["size"], item["filename"], output_dir)
        results.append(path)
        print(f"  ✓ Saved: {path}")
    return results
```

**Before starting any batch**, announce to Dr. Rivero:
- Total image count
- Number of batches required
- Estimated total time

Example:
> "Generating 5 images — 1 batch. Estimated time: ~60–90 seconds."
> "Generating 6 images — 2 batches with a 62-second pause between them. Estimated time: ~2–3 minutes."

---

## Step 4 — Save to Disk

Default output directory: `/mnt/user-data/outputs/images/`
Create if it does not exist:
```python
Path("/mnt/user-data/outputs/images/").mkdir(parents=True, exist_ok=True)
```

Filename: use the `suggested filename` from the image planner prompt block exactly.
If no filename was specified, generate one:
```
[guide-topic-slug]-[image-type]-[YYYYMMDD].png
```

Always save as `.png` regardless of API response format.

---

## Step 5 — Display and Present

After each image is saved:
1. Call `present_files` with the saved path so it renders inline in chat.
2. Print a one-line log entry:
   ```
   ✓ IMAGE 1 — hero | ckd-acidosis-hero.png | 1536×1024 | saved
   ```

After all images are complete, show a summary table:

```
GENERATION COMPLETE
──────────────────────────────────────────────
 #  Filename                        Size      
──────────────────────────────────────────────
 1  ckd-acidosis-hero.png           1536×1024 
 2  ckd-acidosis-kidney.png         1024×1024 
 3  ckd-acidosis-triad.png          1280×960  
──────────────────────────────────────────────
 Output: /mnt/user-data/outputs/images/
```

---

## Step 6 — Error Handling

| Error | Action |
|---|---|
| `OPENAI_API_KEY` not set | Stop immediately. Tell Dr. Rivero: "Please set the OPENAI_API_KEY environment variable and retry." |
| Rate limit error (429) | Wait 62 seconds, retry once. If it fails again, pause and notify Dr. Rivero. |
| Content policy rejection | Log the filename as SKIPPED. Note the rejection. Continue with remaining images. Do not retry without modifying the prompt. |
| Network timeout | Retry once after 10 seconds. If it fails again, log as FAILED and continue. |
| Invalid size string | Fall back to `"1024x1024"`. Note the substitution in the output log. |

Never abort the full batch due to a single image failure — always continue and report at the end.

---

## Integration with Image Planner (Mode B detail)

When the image planner skill has just completed an IMAGE PLAN, this skill should:

1. **Detect** the completed plan in conversation context.
2. **Offer** to execute: "Image plan ready — shall I generate all [n] images now with gpt-image-2?"
3. **Wait** for Dr. Rivero's confirmation ("yes", "go", "generate", etc.).
4. **Extract** all 10-point prompt blocks in IMAGE PLAN order.
5. **Map** each prompt's DIMENSIONS field to the OpenAI size string (Step 2 table).
6. **Use** each prompt's `suggested filename` as the output filename.
7. **Run** batch_generate() with rate limiting (Step 3).
8. **Present** all saved files inline (Step 5).

The image planner and this skill form a two-step pipeline:
```
Guide URL → [image planner] → IMAGE PLAN → [gpt-image-generator] → PNG files on disk
```

---

## Quality Rules (always apply)

- `quality="high"` — never use `"standard"` for williamriveromd.com content.
- Never truncate prompts — pass the full 10-point block.
- Always prepend the Filipino medical context framing line.
- Always save as PNG.
- Always present files inline after saving.
- Never expose the API key in any output, log, or chat message.
