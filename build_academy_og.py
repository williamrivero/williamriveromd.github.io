#!/usr/bin/env python3
"""Build the Renal Care Academy share (Open Graph) cards: 1200 x 630 JPEG, <= 300 KB.

GPT supplies text-free art (1536 x 1024, left 42% kept as a quiet field). This script crops it
to 1.91:1, lays a legibility gradient over the left side, and sets every word itself, so titles
are always spelled right and every track card shares one typographic system.

  python3 build_academy_og.py --art "<folder with GPT art>"           # build all cards found
  python3 build_academy_og.py --art "<folder>" --only dialysis-head-nurse
  python3 build_academy_og.py --art "<folder>" --patch                  # also point og:image at the new cards
  python3 build_academy_og.py --preview                                 # template preview with no art

Art file names: <slug>.png / .jpg / .webp (slug = the track page name, or academy-index).
Output: images/og/academy/<slug>.jpg
"""
import argparse, glob, io, os, re, sys
from PIL import Image, ImageDraw, ImageFont, ImageFilter

W, H = 1200, 630
OUT = "images/og/academy"
LIMIT = 300 * 1024
SITE = "https://renalcarematters.com/"

GROUP = {  # accent colors from the locked site palette
    "academy":    ("#1A6B72", "RENAL CARE ACADEMY"),
    "nursing":    ("#1A6B72", "NEPHROLOGY NURSING TRACK"),
    "physicians": ("#1F3864", "RENAL CARE PHYSICIANS TRACK"),
    "technician": ("#C55A11", "RENAL TECHNICIANS TRACK"),
    "ancillary":  ("#2E6B3E", "ANCILLARY STAFF TRACK"),
    "administrative": ("#4B3280", "ADMINISTRATIVE STAFF TRACK"),
    "emergency":  ("#B91C1C", "EMERGENCY READINESS"),
}

# slug: (page, group, title, tag line under group, stats line)
TRACKS = {
    "academy-index": ("academy/index.html", "academy", "Training for the people who deliver kidney care",
                      None, "Self-study · onboarding · a new role · free"),   # tag line: live counts, see landing_stats()
    "nephrology-nursing": ("academy/nephrology-nursing.html", "nursing", "Hemodialysis Nurse",
                           "BY SPECIALIZATION", "16 core + 1 advanced module · two paths"),
    "transplant-nurse": ("academy/transplant-nurse.html", "nursing", "Kidney Transplant Nurse",
                         "BY SPECIALIZATION", "12 modules · referral to graft care"),
    "pediatric-dialysis-nurse": ("academy/pediatric-dialysis-nurse.html", "nursing", "Pediatric Dialysis Nurse",
                                 "BY SPECIALIZATION", "20 modules · PD and hemodialysis for children"),
    "peritoneal-dialysis-nurse": ("academy/peritoneal-dialysis-nurse.html", "nursing", "Peritoneal Dialysis Nurse",
                                  "BY SPECIALIZATION", "12 modules · five skills stations · final exam"),
    "dialysis-head-nurse": ("academy/dialysis-head-nurse.html", "nursing", "Head Nurse",
                            "BY ROLE", "13 modules · staffing, safety, and the roster"),
    "dialysis-charge-nurse": ("academy/dialysis-charge-nurse.html", "nursing", "Charge Nurse",
                              "BY ROLE", "18 modules · the shift, chair by chair"),
    "dialysis-nurse-assistant": ("academy/dialysis-nurse-assistant.html", "nursing", "Dialysis Nurse Assistant / PCA",
                                 "BY ROLE · SUPERVISED SUPPORT", "12 modules · worked scenarios · assistant toolkit"),
    "physician-on-duty": ("academy/physician-on-duty.html", "physicians", "Physician-on-Duty",
                          "SHIFT COVERAGE", "First-shift modules open · three tiers"),
    "attending-nephrologist": ("academy/attending-nephrologist.html", "physicians", "Attending Nephrologist",
                               "CONSULTANT", "24 modules · calculators in every module"),
    "attending-pediatric-nephrologist": ("academy/attending-pediatric-nephrologist.html", "physicians", "Attending Pediatric Nephrologist",
                                         "PEDIATRIC CONSULTANT", "29 modules · seven on dialysis"),
    "nephrology-trainee": ("academy/nephrology-trainee.html", "physicians", "Nephrology Fellow / Resident / Intern",
                           "PHYSICIANS IN TRAINING", "36 modules · six pathways, adult and pediatric"),
    "vascular-surgeon": ("academy/vascular-surgeon.html", "physicians", "Vascular Surgeon",
                         "ACCESS SURGERY", "20 modules · referral to rescue"),
    "dialysis-clinical-head": ("academy/dialysis-clinical-head.html", "physicians", "Dialysis Clinical Head",
                               "SERVICE LEADERSHIP", "14 modules · governance to the first 90 days"),
    "renal-dietitian": ("academy/renal-dietitian.html", "ancillary", "Renal Dietitian",
                        "MEDICAL NUTRITION THERAPY", "16 modules · four parts · final exam"),
    "hemodialysis-technician": ("academy/hemodialysis-technician.html", "technician", "Dialysis Technician",
                                "FOUNDATION · CHAIRSIDE", "12 modules · skills checklists · final exam"),
    "water-treatment-technician": ("academy/water-treatment-technician.html", "technician",
                                   "Water Treatment Technician", "SPECIALIST · WATER ROOM",
                                   "12 modules · skills checklists · final exam"),
    "dialysis-biomedical-technician": ("academy/dialysis-biomedical-technician.html", "technician",
                                       "Biomedical Equipment Technician", "SPECIALIST · WORKSHOP",
                                       "12 modules · skills checklists · final exam"),
    "dialysis-unit-manager": ("academy/dialysis-unit-manager.html", "administrative", "Unit Operations Manager/Unit Manager",
                              "UNIT MANAGEMENT", "19 modules · freestanding and hospital paths"),
    "dialysis-unit-owner": ("academy/dialysis-unit-owner.html", "administrative", "Dialysis Unit Owner",
                            "GOVERNANCE AND STEWARDSHIP", "24 modules · 8 owner calculators · capstone"),
    "philhealth-claims": ("academy/philhealth-claims.html", "administrative", "PhilHealth Liaison/Claims Officer",
                          "CLAIMS", "10 modules + practicum · 5 calculators"),
    "medical-records-officer": ("academy/medical-records-officer.html", "ancillary", "Medical Records Officer/Custodian",
                                "RECORDS", "14 modules · capstone · calculator toolkit"),
    "transplant-coordinator": ("academy/transplant-coordinator.html", "ancillary", "Renal Transplant Coordinator",
                               "TRANSPLANT COORDINATION", "20 modules · two learner paths · seven-tool toolkit"),
    "social-worker": ("academy/social-worker.html", "ancillary", "Renal Social Worker",
                      "RENAL SOCIAL WORK", "20 modules · two learner paths · six-tool toolkit"),
    "occupational-physical-therapist": ("academy/occupational-physical-therapist.html", "ancillary", "Occupational and Physical Therapist",
                                        "RENAL REHABILITATION", "20 modules · OT and PT pathways · six-tool toolkit"),
    "resuscitation-lab": ("academy/resuscitation-lab.html", "emergency", "Dialysis Team Resuscitation Lab",
                          "BLS-, ALS- AND PALS-ALIGNED REVIEW", "13 modules · 17 megacodes · Practice Lab"),
}

FONT_DIRS = ["/usr/share/fonts/opentype/inter", os.path.expanduser("~/Library/Fonts"), "/Library/Fonts",
             "/System/Library/Fonts/Supplemental"]

def font(weight, size):
    names = {"bold": ["Inter-Bold.otf", "Inter-Bold.ttf", "Arial Bold.ttf"],
             "semi": ["Inter-SemiBold.otf", "Inter-SemiBold.ttf", "Arial Bold.ttf"],
             "reg": ["Inter-Regular.otf", "Inter-Regular.ttf", "Arial.ttf"]}[weight]
    for d in FONT_DIRS:
        for n in names:
            p = os.path.join(d, n)
            if os.path.exists(p):
                return ImageFont.truetype(p, size)
    return ImageFont.load_default(size)

def hexrgb(h):
    h = h.lstrip("#"); return tuple(int(h[i:i+2], 16) for i in (0, 2, 4))

def wrap(draw, text, f, maxw):
    lines, cur = [], ""
    for w in text.split():
        t = (cur + " " + w).strip()
        if draw.textlength(t, font=f) <= maxw: cur = t
        else: lines.append(cur); cur = w
    lines.append(cur); return lines

def fit_art(path):
    im = Image.open(path).convert("RGB")
    r = W / H
    w, h = im.size
    if w / h > r:   # too wide: trim sides, keep the right (subject) side
        nw = int(h * r); im = im.crop((w - nw, 0, w, h))
    else:           # too tall: center crop vertically (GPT 3:2 loses ~110 px top and bottom)
        nh = int(w / r); top = (h - nh) // 2; im = im.crop((0, top, w, top + nh))
    return im.resize((W, H), Image.LANCZOS)

def placeholder():
    im = Image.new("RGB", (W, H))
    d = ImageDraw.Draw(im)
    a, b = hexrgb("#dcefe8"), hexrgb("#f5efdc")
    for x in range(W):
        t = x / W; d.line([(x, 0), (x, H)], fill=tuple(int(a[i] + (b[i] - a[i]) * t) for i in range(3)))
    d.rounded_rectangle((560, 70, 1150, 560), 30, outline=hexrgb("#9bbab4"), width=3)
    d.text((855, 315), "GPT art zone", font=font("semi", 30), fill=hexrgb("#6c8f89"), anchor="mm")
    return im

# Cards whose art holds a blank screen get a QR code on it (Dr. Rivero, Nov 25 2026): the screen box in the final
# 1200 x 630 card (measured on the fitted art) and the URL it opens. Only for that art; new art needs a new box.
QR_SCREENS = {"academy-index": ((757, 446, 896, 548), SITE + "academy/")}

def draw_qr(im, box, url):
    import qrcode
    q = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_M, border=2, box_size=1)
    q.add_data(url); q.make(fit=True)
    m = q.get_matrix()                      # includes the 2-module quiet zone
    x0, y0, x1, y1 = box
    side = min(x1 - x0, y1 - y0) - 4
    px = max(2, side // len(m))             # whole pixels per module: crisp edges survive JPEG
    size = px * len(m)
    cx, cy = (x0 + x1) // 2, (y0 + y1) // 2
    left, top = cx - size // 2, cy - size // 2
    d = ImageDraw.Draw(im)
    d.rounded_rectangle((left - 2, top - 2, left + size + 1, top + size + 1), 5, fill=(255, 255, 255))
    for r, row in enumerate(m):
        for c, on in enumerate(row):
            if on:
                d.rectangle((left + c * px, top + r * px, left + (c + 1) * px - 1, top + (r + 1) * px - 1), fill=(10, 30, 30))

def landing_stats(page="academy/index.html"):
    """Track / subtrack / module counts read from the landing page's stat chips (written by the generator from the
    course data), so the share card never drifts from the page: "5 TRACKS · 18 SUBTRACKS · 256 MODULES"."""
    s = open(page, encoding="utf-8").read()
    got = {w: n for n, w in re.findall(r'<span class="acad-stat"><b>([\d,]+)</b>\s*(tracks|subtracks|modules)</span>', s)}
    missing = [w for w in ("tracks", "subtracks", "modules") if w not in got]
    if missing:
        sys.exit(f"landing stat chips not found for: {', '.join(missing)} ({page})")
    return " · ".join(f"{got[w]} {w.upper()}" for w in ("tracks", "subtracks", "modules"))

def compose(slug, art_path=None):
    page, grp, title, tag, stats = TRACKS[slug]
    if tag is None:
        tag = landing_stats(page)
    accent, gname = GROUP[grp]
    base = fit_art(art_path) if art_path else placeholder()
    # legibility veil: solid mint on the left, fading out by 62% width
    veil = Image.new("RGBA", (W, H), (0, 0, 0, 0)); vd = ImageDraw.Draw(veil)
    mint = hexrgb("#eef7f2")
    for x in range(W):
        t = x / W
        a = 236 if t < 0.40 else max(0, int(236 * (1 - (t - 0.40) / 0.22)))
        vd.line([(x, 0), (x, H)], fill=mint + (a,))
    im = Image.alpha_composite(base.convert("RGBA"), veil).convert("RGB")
    d = ImageDraw.Draw(im)
    X = 64
    ac = hexrgb(accent)
    # wordmark
    d.rectangle((X, 58, X + 6, 92), fill=ac)
    d.text((X + 18, 58), "RENAL CARE ACADEMY", font=font("bold", 20), fill=hexrgb("#1A6B72"))
    sub = gname if grp == "academy" else f"{gname}  ·  {tag}"
    if grp == "academy": sub = tag
    d.text((X + 18, 80), sub, font=font("semi", 15), fill=hexrgb("#3d635e"))
    # title
    size = 60
    while True:
        tf = font("bold", size); lines = wrap(d, title, tf, 470)
        if (len(lines) <= 3 and max(d.textlength(l, font=tf) for l in lines) <= 470) or size <= 40: break
        size -= 4
    lh = int(size * 1.12)
    y = 330 - (len(lines) * lh) // 2 - 10
    for ln in lines:
        d.text((X, y), ln, font=tf, fill=hexrgb("#123a36")); y += lh
    d.text((X, y + 16), stats, font=font("reg", 23), fill=hexrgb("#2f5752"))
    # footer
    d.text((X, H - 74), "renalcarematters.com/academy", font=font("semi", 19), fill=hexrgb("#1A6B72"))
    d.text((X, H - 50), "Free · no account · English", font=font("reg", 16), fill=hexrgb("#3d635e"))
    d.rectangle((0, H - 10, W, H), fill=ac)
    if slug in QR_SCREENS and art_path:
        draw_qr(im, *QR_SCREENS[slug])
    return im

def save(im, slug):
    os.makedirs(OUT, exist_ok=True)
    dst = f"{OUT}/{slug}.jpg"
    for q in (92, 88, 84, 80, 76, 72, 68):
        buf = io.BytesIO(); im.save(buf, "JPEG", quality=q, optimize=True, progressive=True)
        if buf.tell() <= LIMIT: break
    data = buf.getvalue()
    open(dst, "wb").write(data)          # stable name, kept for links already shared
    # Fingerprinted copy for og:image: /images/* is cached for 30 days, so a card rebuilt under the same name
    # kept showing the old picture on Facebook (Nov 25 2026). A new name per content is fetched fresh.
    import hashlib
    fp = f"{OUT}/{slug}.{hashlib.sha1(data).hexdigest()[:10]}.jpg"
    for old in glob.glob(f"{OUT}/{slug}.*.jpg"):
        if old != fp and re.fullmatch(rf"{re.escape(slug)}\.[0-9a-f]{{10}}\.jpg", os.path.basename(old)):
            os.remove(old)
    open(fp, "wb").write(data)
    return fp, buf.tell()

def patch(slug, dst):
    page = TRACKS[slug][0]
    s = open(page, encoding="utf-8").read()
    url = SITE + dst
    s = re.sub(r'(<meta property="og:image" content=")[^"]*', r'\g<1>' + url, s, 1)
    s = re.sub(r'(<meta name="twitter:image" content=")[^"]*', r'\g<1>' + url, s, 1)
    for k, v in (("og:image:width", "1200"), ("og:image:height", "630"), ("og:image:type", "image/jpeg")):
        if f'property="{k}"' in s:
            s = re.sub(rf'(<meta property="{k}" content=")[^"]*', r'\g<1>' + v, s, 1)
        else:
            s = s.replace(f'<meta name="twitter:image" content="{url}">',
                          f'<meta property="{k}" content="{v}">\n<meta name="twitter:image" content="{url}">', 1)
    open(page, "w", encoding="utf-8").write(s)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--art"); ap.add_argument("--only"); ap.add_argument("--patch", action="store_true")
    ap.add_argument("--preview", action="store_true")
    a = ap.parse_args()
    slugs = [a.only] if a.only else list(TRACKS)
    for slug in slugs:
        art = None
        if a.art:
            hits = [p for e in ("png", "jpg", "jpeg", "webp") for p in glob.glob(os.path.join(a.art, f"{slug}.{e}"))]
            if not hits: print(f"skip {slug}: no art"); continue
            art = hits[0]
        elif not a.preview:
            sys.exit("give --art <folder> or --preview")
        dst, n = save(compose(slug, art), slug if not a.preview else f"preview-{slug}")
        print(f"{dst}  {n // 1024} KB")
        if a.patch and art: patch(slug, dst)

if __name__ == "__main__":
    main()
