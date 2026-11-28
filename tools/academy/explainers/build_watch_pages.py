#!/usr/bin/env python3
"""Watch pages for the cartoon explainers (Nov 28 2026, Dr. Rivero).

Facebook, Messenger and Viber show a link as a preview card and never play a video hosted on another site, so each
explainer gets a small page, /watch/<name>, whose share card is the video's own frame with a big play button and its
length. Tapping the card opens the page with the video and a button to the tool. The Share button on each embedded
video shares this page.

Writes:
  watch/<name>.html                    the watch page (canonical https://renalcarematters.com/watch/<name>)
  images/og/watch/<name>.jpg           1200 x 630 share card (play button + length), under 300 KB

Run after adding or re-rendering an explainer:
    python3 tools/academy/explainers/build_watch_pages.py
"""
import html
import json
import subprocess
from pathlib import Path

from PIL import Image, ImageDraw, ImageFilter, ImageFont

REPO = Path(__file__).resolve().parents[3]
SITE = "https://renalcarematters.com"
FONT = "/usr/share/fonts/opentype/inter/Inter-Bold.otf"

VIDEOS = [
    {"name": "megacode-shared-monitor", "video": "/videos/academy/megacode-shared-monitor-explainer.mp4",
     "poster": "videos/academy/megacode-shared-monitor-explainer.jpg",
     "title": "The shared monitor display: a 1-minute explainer",
     "desc": "How the Megacode Practice Lab turns a second screen into a bedside monitor: rhythms, capnography, "
             "the defibrillator and rhythm playlists. Free on the Renal Care Academy.",
     "tool": "/academy/resuscitation-lab-practice#explainer", "tool_label": "Open the Megacode Practice Lab",
     "script": "megacode-shared-monitor"},
    {"name": "med-scheduler", "video": "/videos/dosis/med-scheduler-explainer.mp4",
     "poster": "videos/dosis/med-scheduler-explainer.jpg",
     "title": "Med Scheduler: a cartoon explainer",
     "desc": "Turn a long prescription into one clear daily timetable around meals, bedtime and dialysis days. "
             "Free in Dosis, the Drug Index on renalcarematters.com. For clinicians.",
     "tool": "/drugs/med-scheduler", "tool_label": "Open the Med Scheduler", "script": "med-scheduler"},
    {"name": "calculo", "video": "/videos/calculo/calculo-explainer.mp4",
     "poster": "videos/calculo/calculo-explainer.jpg",
     "title": "Meet Calculo: a cartoon explainer",
     "desc": "More than 250 free clinical calculators across every specialty: search, sample data, shared patient inputs, "
             "formulas and sources, and one download for use with no signal.",
     "tool": "/guides/calculators", "tool_label": "Open the calculators", "script": "calculo"},
    {"name": "interaction-checker", "video": "/videos/dosis/interaction-checker-explainer.mp4",
     "poster": "videos/dosis/interaction-checker-explainer.jpg",
     "title": "Interaction Checker: a cartoon explainer",
     "desc": "Add a patient's medicines and see graded interactions, kidney checks and kidney dosing. "
             "Free in Dosis, the Drug Index on renalcarematters.com. For clinicians.",
     "tool": "/drugs/interactions", "tool_label": "Open the Interaction Checker", "script": "interaction-checker"},
]


def duration(path: Path) -> str:
    s = float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(path)],
                             capture_output=True, text=True, check=True).stdout.strip())
    s = int(round(s))
    return f"{s // 60}:{s % 60:02d}"


def card(v: dict, dur: str, out: Path) -> None:
    im = Image.open(REPO / v["poster"]).convert("RGB")
    w, h = 1200, 630
    im = im.resize((w, round(im.height * w / im.width)), Image.LANCZOS)
    top = (im.height - h) // 2
    im = im.crop((0, top, w, top + h))
    # darken slightly so the play button reads
    shade = Image.new("RGB", (w, h), (8, 16, 30))
    im = Image.blend(im, shade, 0.28)
    d = ImageDraw.Draw(im, "RGBA")
    cx, cy, r = w // 2, h // 2, 92
    halo = Image.new("RGBA", (w, h), (0, 0, 0, 0))
    ImageDraw.Draw(halo).ellipse((cx - r - 18, cy - r - 18, cx + r + 18, cy + r + 18), fill=(0, 0, 0, 110))
    im.paste(halo.filter(ImageFilter.GaussianBlur(14)), (0, 0), halo.filter(ImageFilter.GaussianBlur(14)))
    d = ImageDraw.Draw(im, "RGBA")
    d.ellipse((cx - r, cy - r, cx + r, cy + r), fill=(255, 255, 255, 240))
    t = r * 0.62
    d.polygon([(cx - t * 0.45, cy - t * 0.75), (cx - t * 0.45, cy + t * 0.75), (cx + t * 0.85, cy)], fill=(14, 74, 80, 255))
    f = ImageFont.truetype(FONT, 30)
    label = f"▶ {dur}"
    tw = d.textlength(label, font=f)
    d.rounded_rectangle((w - tw - 56, h - 74, w - 24, h - 24), radius=14, fill=(15, 23, 42, 220))
    d.text((w - tw - 40, h - 68), label, font=f, fill=(255, 255, 255))
    f2 = ImageFont.truetype(FONT, 26)
    d.rounded_rectangle((24, h - 74, 24 + d.textlength("Watch on renalcarematters.com", font=f2) + 32, h - 24), radius=14,
                        fill=(14, 74, 80, 235))
    d.text((40, h - 66), "Watch on renalcarematters.com", font=f2, fill=(255, 255, 255))
    out.parent.mkdir(parents=True, exist_ok=True)
    q = 88
    while True:
        im.save(out, "JPEG", quality=q, optimize=True, progressive=True)
        if out.stat().st_size < 300_000 or q <= 60:
            break
        q -= 6


def transcript(v: dict) -> str:
    p = REPO / "tools" / "academy" / "explainers" / v["script"] / "script.txt"
    return html.escape(" ".join(p.read_text(encoding="utf-8").split("\n")).strip()) if p.exists() else ""


PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{title} · Renal Care Matters</title>
<meta name="description" content="{desc}">
<link rel="canonical" href="{url}">
<meta property="og:type" content="video.other">
<meta property="og:site_name" content="Renal Care Matters">
<meta property="og:title" content="{title}">
<meta property="og:description" content="{desc}">
<meta property="og:url" content="{url}">
<meta property="og:image" content="{img}">
<meta property="og:image:width" content="1200">
<meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{title}: a frame from the video with a play button">
<meta property="og:video" content="{vurl}">
<meta property="og:video:secure_url" content="{vurl}">
<meta property="og:video:type" content="video/mp4">
<meta property="og:video:width" content="1280">
<meta property="og:video:height" content="720">
<meta name="twitter:card" content="summary_large_image">
<meta name="twitter:title" content="{title}">
<meta name="twitter:description" content="{desc}">
<meta name="twitter:image" content="{img}">
<link rel="icon" type="image/x-icon" href="/favicon.ico">
<link rel="icon" type="image/png" sizes="32x32" href="/favicon-32x32.png">
<script type="application/ld+json">{jsonld}</script>
<style>
:root{{--navy:#1f3864;--teal:#1a6b72;--dteal:#0e4a50;--text:#1e2a38;--mid:#475569;--bg:#f4f7f9;}}
*{{box-sizing:border-box;}} body{{margin:0;background:var(--bg);color:var(--text);font-family:Inter,Manrope,system-ui,-apple-system,"Segoe UI",sans-serif;}}
.top{{background:var(--navy);padding:14px 22px;}} .top a{{color:#fff;text-decoration:none;font-weight:800;letter-spacing:.02em;}}
main{{max-width:980px;margin:0 auto;padding:26px 18px 40px;}}
h1{{font-size:clamp(24px,4vw,36px);line-height:1.2;margin:4px 0 10px;color:var(--navy);}}
.lead{{font-size:16.5px;line-height:1.6;color:var(--mid);margin:0 0 18px;}}
.player{{border-radius:14px;overflow:hidden;background:#000;box-shadow:0 10px 30px rgba(15,30,46,.18);}}
.player video{{display:block;width:100%;height:auto;}}
.row{{display:flex;flex-wrap:wrap;gap:10px;align-items:center;margin:18px 0 6px;}}
.btn{{display:inline-flex;align-items:center;gap:8px;font:700 16px Inter,system-ui,sans-serif;text-decoration:none;border-radius:999px;padding:12px 20px;border:0;cursor:pointer;}}
.btn-main{{background:var(--dteal);color:#fff;}} .btn-main:hover{{background:var(--teal);}}
.btn-ghost{{background:#fff;color:var(--dteal);border:2px solid rgba(14,74,80,.35);}}
.btn svg{{width:18px;height:18px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;}}
details{{margin-top:16px;background:#fff;border:1px solid #dfe6f0;border-radius:12px;padding:10px 14px;}}
summary{{cursor:pointer;font-weight:700;color:var(--mid);}} details p{{line-height:1.6;color:var(--mid);}}
footer{{text-align:center;font-size:13.5px;color:#64748b;padding:18px;}} footer a{{color:inherit;}}
</style>
</head>
<body>
<div class="top"><a href="/">RENAL CARE MATTERS</a></div>
<main>
<h1>{title}</h1>
<p class="lead">{desc}</p>
<div class="player"><video controls playsinline preload="metadata" controlslist="nodownload noplaybackrate" disablepictureinpicture oncontextmenu="return false" poster="/{poster}" width="1280" height="720"><source src="{video}" type="video/mp4"></video></div>
<div class="row">
<a class="btn btn-main" href="{tool}">{tool_label} &rarr;</a>
<button type="button" class="btn btn-ghost" id="share"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/></svg><span>Share</span></button>
</div>
{tr_block}
</main>
<footer>&copy; 2026 renalcarematters.com &middot; <a href="/terms">Terms of use</a></footer>
<script>(function(){{var b=document.getElementById('share'),l=b.querySelector('span'),u='{url}';
b.addEventListener('click',function(){{if(navigator.share){{navigator.share({{title:document.title,url:u}}).catch(function(){{}});return;}}
function done(m){{l.textContent=m;setTimeout(function(){{l.textContent='Share';}},2200);}}
if(navigator.clipboard)navigator.clipboard.writeText(u).then(function(){{done('Link copied');}},function(){{prompt('Copy this link',u);}});else prompt('Copy this link',u);}});}})();</script>
</body>
</html>
"""


def main() -> None:
    for v in VIDEOS:
        mp4 = REPO / v["video"].lstrip("/")
        if not mp4.exists():
            print("skip (no video):", v["name"]); continue
        dur = duration(mp4)
        img = REPO / "images" / "og" / "watch" / f"{v['name']}.jpg"
        card(v, dur, img)
        url = f"{SITE}/watch/{v['name']}"
        tr = transcript(v)
        jsonld = json.dumps({"@context": "https://schema.org", "@type": "VideoObject", "name": v["title"], "description": v["desc"],
                             "thumbnailUrl": f"{SITE}/images/og/watch/{v['name']}.jpg", "contentUrl": SITE + v["video"],
                             "duration": f"PT{int(dur.split(':')[0])}M{int(dur.split(':')[1])}S", "uploadDate": "2026-11-28",
                             "url": url, "inLanguage": "en"}).replace("</", "<\\/")
        page = PAGE.format(title=html.escape(v["title"]), desc=html.escape(v["desc"]), url=url,
                           img=f"{SITE}/images/og/watch/{v['name']}.jpg", vurl=SITE + v["video"], jsonld=jsonld,
                           poster=v["poster"], video=v["video"], tool=v["tool"], tool_label=html.escape(v["tool_label"]),
                           tr_block=(f'<details><summary>Read the transcript</summary><p>{tr}</p></details>' if tr else ""))
        out = REPO / "watch" / f"{v['name']}.html"
        out.parent.mkdir(exist_ok=True)
        out.write_text(page, encoding="utf-8")
        print(f"watch/{v['name']}.html  ({dur}, card {img.stat().st_size // 1000} KB)")


if __name__ == "__main__":
    main()
