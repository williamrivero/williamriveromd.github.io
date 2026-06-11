#!/usr/bin/env python3
"""
Generate the patient companion PDF for the "Holiday Kidney Syndrome" guide.

Builds downloads/wgmr-holiday-kidney-syndrome-guide.pdf from the guide's
images plus condensed survival rules — a printable handout for patients on
the go. Re-run after updating any of the guide's infographics.

Usage:
    python3 generate_holiday_companion_pdf.py
Requires: reportlab, Pillow  (pip install reportlab pillow)
"""

import io
from pathlib import Path

from PIL import Image
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas

ROOT = Path(__file__).parent
OUT = ROOT / "downloads" / "wgmr-holiday-kidney-syndrome-guide.pdf"
IMAGES = ROOT / "images"

NAVY = HexColor("#1f3864")
TEAL = HexColor("#1a6b72")
RED = HexColor("#b91c1c")
GREEN = HexColor("#166534")
AMBER = HexColor("#92400e")
TEXT = HexColor("#1e2a38")
MUTED = HexColor("#4a5568")
FAINT = HexColor("#8a96a3")
GREEN_SOFT = HexColor("#f0fdf4")
AMBER_SOFT = HexColor("#fffbeb")
RED_SOFT = HexColor("#fff0f0")
TEAL_SOFT = HexColor("#eef6f7")

W, H = A4            # 595 x 842 pt
M = 42               # margin
CW = W - 2 * M       # content width

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
pdfmetrics.registerFont(TTFont("DJV", FONT_DIR / "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DJV-B", FONT_DIR / "DejaVuSans-Bold.ttf"))


def jpeg_reader(png_name, max_w=1400):
    """Load a guide PNG, downscale, and re-encode as JPEG for a small PDF."""
    im = Image.open(IMAGES / png_name).convert("RGB")
    if im.width > max_w:
        im = im.resize((max_w, int(im.height * max_w / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=80, optimize=True)
    buf.seek(0)
    return ImageReader(buf), im.width / im.height


class Doc:
    def __init__(self):
        self.c = canvas.Canvas(str(OUT), pagesize=A4)
        self.page = 0

    # ── primitives ────────────────────────────────────────────────────────
    def footer(self):
        c = self.c
        self.page += 1
        c.setFont("DJV", 7.5)
        c.setFillColor(FAINT)
        c.drawString(M, 24, "williamriveromd.com — patient education only; follow your own nephrologist's advice")
        c.drawRightString(W - M, 24, f"Page {self.page}")

    def new_page(self):
        self.footer()
        self.c.showPage()

    def heading(self, y, eyebrow, title, rule=True):
        c = self.c
        c.setFont("DJV-B", 9)
        c.setFillColor(TEAL)
        c.drawString(M, y, eyebrow.upper())
        c.setFont("DJV-B", 17)
        c.setFillColor(NAVY)
        c.drawString(M, y - 22, title)
        if rule:
            c.setStrokeColor(TEAL)
            c.setLineWidth(1.2)
            c.line(M, y - 30, W - M, y - 30)
        return y - 44

    def image(self, y, png, caption=None):
        img, ratio = jpeg_reader(png)
        h = CW / ratio
        self.c.drawImage(img, M, y - h, width=CW, height=h)
        y -= h
        if caption:
            self.c.setFont("DJV", 8.5)
            self.c.setFillColor(MUTED)
            y -= 13
            self.c.drawString(M, y, caption)
        return y - 10

    def wrap(self, text, font, size, width):
        out, line = [], ""
        for word in text.split():
            t = (line + " " + word).strip()
            if pdfmetrics.stringWidth(t, font, size) <= width:
                line = t
            else:
                out.append(line)
                line = word
        if line:
            out.append(line)
        return out

    def bullets(self, y, items, size=10, gap=5, bullet="•", color=TEXT, bold_lead=True, x=None, width=None):
        c = self.c
        x = M if x is None else x
        width = (CW if width is None else width) - 16
        for item in items:
            lead, _, rest = item.partition("|")
            first = True
            if bold_lead and rest:
                lines = self.wrap(lead + " — " + rest, "DJV", size, width)
                lead_str = lead + " — "
            else:
                lines = self.wrap(item.replace("|", " — "), "DJV", size, width)
                lead_str = None
            for ln in lines:
                if first:
                    c.setFillColor(TEAL)
                    c.setFont("DJV-B", size)
                    c.drawString(x, y, bullet)
                c.setFillColor(color)
                if first and lead_str and ln.startswith(lead):
                    c.setFont("DJV-B", size)
                    c.drawString(x + 14, y, lead)
                    c.setFont("DJV", size)
                    c.drawString(x + 14 + pdfmetrics.stringWidth(lead, "DJV-B", size), y, ln[len(lead):])
                else:
                    c.setFont("DJV", size)
                    c.drawString(x + 14, y, ln)
                y -= size + 3
                first = False
            y -= gap
        return y

    def box(self, y, title, body, fill, border, title_color, size=9.5, pad=10):
        c = self.c
        lines = self.wrap(body, "DJV", size, CW - 2 * pad)
        h = pad * 2 + 14 + len(lines) * (size + 3)
        c.setFillColor(fill)
        c.setStrokeColor(border)
        c.setLineWidth(1.2)
        c.roundRect(M, y - h, CW, h, 8, stroke=1, fill=1)
        ty = y - pad - 9
        c.setFillColor(title_color)
        c.setFont("DJV-B", size + 1)
        c.drawString(M + pad, ty, title)
        ty -= 15
        c.setFillColor(TEXT)
        c.setFont("DJV", size)
        for ln in lines:
            c.drawString(M + pad, ty, ln)
            ty -= size + 3
        return y - h - 12

    def card_list(self, y, title, items, fill, border, title_color, size=8.6, pad=10):
        """A colored rounded card with a bold title and lead-bolded bullet items."""
        c = self.c
        lh = size + 2.6
        # pre-measure
        measured = []
        for item in items:
            lead, _, rest = item.partition("|")
            lines = self.wrap(lead + " — " + rest if rest else lead, "DJV", size, CW - 2 * pad - 12)
            measured.append((lead, lines))
        n_lines = sum(len(ls) for _, ls in measured)
        h = pad * 2 + 16 + n_lines * lh + len(items) * 2.5
        c.setFillColor(fill)
        c.setStrokeColor(border)
        c.setLineWidth(1.2)
        c.roundRect(M, y - h, CW, h, 8, stroke=1, fill=1)
        ty = y - pad - 9
        c.setFillColor(title_color)
        c.setFont("DJV-B", size + 1.4)
        c.drawString(M + pad, ty, title)
        ty -= 16
        for lead, lines in measured:
            first = True
            for ln in lines:
                if first:
                    c.setFillColor(title_color)
                    c.setFont("DJV-B", size)
                    c.drawString(M + pad, ty, "•")
                c.setFillColor(TEXT)
                if first and ln.startswith(lead):
                    c.setFont("DJV-B", size)
                    c.drawString(M + pad + 10, ty, lead)
                    c.setFont("DJV", size)
                    c.drawString(M + pad + 10 + pdfmetrics.stringWidth(lead, "DJV-B", size), ty, ln[len(lead):])
                else:
                    c.setFont("DJV", size)
                    c.drawString(M + pad + 10, ty, ln)
                ty -= lh
                first = False
            ty -= 2.5
        return y - h - 10

    def fruit_table(self, y, rows, size=8.6):
        """Three-column fruit table: fruit / risk badge / rule."""
        c = self.c
        col1, col2 = 130, 88           # fruit, risk widths
        col3 = CW - col1 - col2
        pad = 6
        lh = size + 2.8
        # header
        c.setFillColor(NAVY)
        c.roundRect(M, y - 20, CW, 20, 4, stroke=0, fill=1)
        c.setFillColor(HexColor("#ffffff"))
        c.setFont("DJV-B", size)
        c.drawString(M + pad, y - 14, "Holiday fruit")
        c.drawString(M + col1 + pad, y - 14, "Potassium risk")
        c.drawString(M + col1 + col2 + pad, y - 14, "The trap / the rule")
        y -= 20
        for i, (fruit, risk, risk_color, risk_fill, rule) in enumerate(rows):
            fruit_lines = self.wrap(fruit, "DJV-B", size, col1 - 2 * pad)
            rule_lines = self.wrap(rule, "DJV", size, col3 - 2 * pad)
            rh = max(len(fruit_lines), len(rule_lines)) * lh + 2 * pad - 2
            if risk == "NEVER":
                c.setFillColor(RED_SOFT)
            else:
                c.setFillColor(HexColor("#ffffff") if i % 2 else HexColor("#f7f9fb"))
            c.rect(M, y - rh, CW, rh, stroke=0, fill=1)
            c.setStrokeColor(HexColor("#e2e6eb"))
            c.setLineWidth(0.6)
            c.line(M, y - rh, M + CW, y - rh)
            ty = y - pad - size + 1
            c.setFillColor(TEXT)
            c.setFont("DJV-B", size)
            for ln in fruit_lines:
                c.drawString(M + pad, ty, ln)
                ty -= lh
            # risk badge
            bw = pdfmetrics.stringWidth(risk, "DJV-B", size - 0.6) + 10
            c.setFillColor(risk_fill)
            c.roundRect(M + col1 + pad, y - pad - size - 2.5, bw, size + 5, 3, stroke=0, fill=1)
            c.setFillColor(risk_color)
            c.setFont("DJV-B", size - 0.6)
            c.drawString(M + col1 + pad + 5, y - pad - size + 1, risk)
            ty = y - pad - size + 1
            c.setFillColor(TEXT)
            c.setFont("DJV", size)
            for ln in rule_lines:
                c.drawString(M + col1 + col2 + pad, ty, ln)
                ty -= lh
            y -= rh
        return y - 10


def build():
    d = Doc()
    c = d.c
    c.setTitle('"Holiday Kidney Syndrome" — Patient Companion')
    c.setAuthor("W. G. M. Rivero, MD, FPCP, DPSN")

    # ── PAGE 1 · COVER ─────────────────────────────────────────────────────
    y = H - M - 4
    c.setFont("DJV-B", 9)
    c.setFillColor(TEAL)
    c.drawString(M, y, "NEPHROLOGY · PATIENT COMPANION · WILLIAMRIVEROMD.COM")
    y -= 30
    c.setFont("DJV-B", 24)
    c.setFillColor(NAVY)
    c.drawString(M, y, '"Holiday Kidney Syndrome"')
    y -= 24
    c.setFont("DJV-B", 14)
    c.drawString(M, y, "Surviving Fiestas, Reunions & the Holidays with CKD")
    y -= 18
    c.setFont("DJV", 10)
    c.setFillColor(MUTED)
    c.drawString(M, y, "W. G. M. Rivero, MD, FPCP, DPSN — Internal Medicine · Nephrology · Clinical Nutrition")
    y -= 16
    y = d.image(y, "holiday-kidney-syndrome-hero.png")
    y -= 8
    intro = ("Every December and every fiesta season, kidney patients are rushed to emergency rooms — and "
             "some die — because of food, drinks, and skipped dialysis sessions at celebrations. We call this "
             'pattern "Holiday Kidney Syndrome." It is preventable. This pocket companion is the plan: what to '
             "eat, what to skip, how to protect your dialysis schedule, and when to go to the ER.")
    c.setFont("DJV", 10.5)
    c.setFillColor(TEXT)
    for ln in d.wrap(intro, "DJV", 10.5, CW):
        c.drawString(M, y, ln)
        y -= 14
    y -= 6
    y = d.box(y, "The one-sentence version",
              "Enjoy the party — but plan your plate, count your fruit, budget your fluid, take your medicines, "
              "and never, ever stretch your dialysis gap for a celebration.",
              TEAL_SOFT, TEAL, TEAL)
    d.new_page()

    # ── PAGE 2 · THE DANGER ────────────────────────────────────────────────
    y = d.heading(H - M - 6, "Why it happens", "The Most Dangerous 72 Hours of the Year")
    y = d.image(y, "holiday-kidney-syndrome-long-gap.png")
    y -= 4
    y = d.bullets(y, [
        "The long gap|on a 3×/week schedule you already have one 2-day gap. Large studies (32,065 patients) show the day after it is the deadliest day of the week: +23% deaths, +77% heart-failure admissions, +90% dangerous heart rhythms.",
        "Holidays stretch the gap|a closed unit or a \"moved\" session turns 2 days into 3–4 — and the feast lands exactly when your body has no way to remove potassium and fluid.",
        "No cheat days in kidney failure|what you eat waits in your blood until your next session. There are only portions you planned and portions you will regret.",
    ])
    y = d.box(y, "The two golden rules",
              "1) Move holiday sessions EARLIER, never later — never let your gap exceed about 72 hours.  "
              "2) Schedule celebrations right AFTER dialysis, when potassium and fluid are at their weekly lowest.",
              GREEN_SOFT, GREEN, GREEN)
    d.new_page()

    # ── PAGE 3 · PARTY FOOD IMAGE ──────────────────────────────────────────
    y = d.heading(H - M - 6, "The buffet, decoded", "Party Food: Hidden Risks")
    y = d.image(y, "holiday-kidney-syndrome-party-food.png")
    y -= 4
    y = d.bullets(y, [
        "Plate strategy|half plate rice + safest dishes, then TWO small favorites. One plate, one pass — walang balikan.",
        "These are general rules|your own dietitian's advice — based on your latest potassium and phosphorus levels — always overrides the lists on the next page.",
    ])
    d.new_page()

    # ── PAGE 4 · PARTY FOOD TRAFFIC LIGHT CARDS ────────────────────────────
    y = d.heading(H - M - 6, "Traffic light", "Filipino Celebration Dishes — Enjoy, Taste, or Skip")
    y = d.card_list(y, "SAFER CHOICES — enjoy in normal portions", [
        "Steamed white rice|your safest base; fill from here first.",
        "Inihaw na isda / grilled fish|skip heavy marinades and toyo-calamansi dips.",
        "Grilled or roasted chicken, skin removed|plain inasal-style without the basting sauce.",
        "Lumpiang sariwa (fresh)|go light on the sweet garlic sauce and skip the crushed peanuts.",
        "Puto, kutsinta (plain, no cheese topping)|rice-based kakanin are among the safer desserts.",
        "Pancit bihon (small plate)|ask the cook to go easy on soy sauce; one fist-sized serving.",
    ], GREEN_SOFT, GREEN, GREEN)
    y = d.card_list(y, "SMALL TASTE ONLY — 2–3 bites, once", [
        "Lechon|small piece of lean meat; leave the skin and the liver sauce.",
        "Christmas ham (hamonado) & keso de bola|very high salt and phosphorus; a thin slice of each at most.",
        "Filipino spaghetti, embutido, hotdogs|processed meat and cheese mean sodium plus hidden phosphorus.",
        "Fruit salad / buko salad|condensed milk + cream + fruits = potassium, phosphorus, sugar, and fluid in one cup. Two spoonfuls, not a bowl.",
        "Bibingka & puto bumbong|the rice cake itself is fine; the salted egg, cheese, and coconut on top are the problem. Ask for it plain.",
        "Leche flan|egg yolks and condensed milk carry phosphorus; one thin slice.",
    ], AMBER_SOFT, AMBER, AMBER)
    y = d.card_list(y, "SKIP THESE — the highest-risk party dishes", [
        "Dinuguan|blood is one of the most concentrated potassium and phosphorus sources on any table.",
        "Kare-kare with bagoong|peanut sauce is potassium-rich; bagoong is one of the saltiest foods that exists.",
        "Sisig, chicharon, crispy pata|organ meats, deep-fried skin: phosphorus, sodium, and fat together.",
        "Itlog na maalat (salted egg)|extreme sodium in a small package.",
        "Salty chips, mixed nuts, cornick|the \"harmless\" grazing bowls beside the karaoke — potassium + sodium + phosphorus you never count.",
        "Gravy, instant sauces, all-day sabaw pots (bulalo, nilaga)|salt plus fluid; broth counts entirely against your fluid limit.",
    ], RED_SOFT, RED, RED)
    d.new_page()

    # ── PAGE 5 · FRUIT TRAP IMAGE ──────────────────────────────────────────
    y = d.heading(H - M - 6, "The #1 holiday trap", 'The Fruit Trap: "It\'s Just Fruit" Is How It Starts')
    y = d.image(y, "holiday-kidney-syndrome-fruit-trap.png")
    y -= 4
    y = d.bullets(y, [
        "The rule|ONE fruit, ONE serving, ONCE that day — decided before you sit down.",
        "Why you lose count|each piece is small, so twenty rambutan over an afternoon of chatting is a massive potassium load — landing on a stretched holiday gap with nowhere to go except your heart's electrical system.",
    ], size=9.5)
    y = d.box(y, "NEVER: star fruit (balimbing) — at any amount",
              "Star fruit contains a toxin (caramboxin) that failing kidneys cannot remove. Even one fruit or one "
              "glass of juice can cause unstoppable hiccups, confusion, seizures, and death. Hiccups that will not "
              "stop after eating balimbing = go to the ER immediately and say what you ate.",
              RED_SOFT, RED, RED)
    d.new_page()

    # ── PAGE 6 · FRUIT TABLE ───────────────────────────────────────────────
    y = d.heading(H - M - 6, "Fruit by fruit", "Holiday Fruits — Risk and the Rule")
    rows = [
        ("Balimbing (star fruit)", "NEVER", HexColor("#ffffff"), RED,
         "Toxic to kidney patients regardless of potassium — see the warning on the previous page."),
        ("Durian", "Very high", HexColor("#ffffff"), RED,
         "One seed-section is already a big load; at a reunion nobody eats just one."),
        ("Rambutan", "High in quantity", AMBER, AMBER_SOFT,
         "Small per piece — but who eats one? Count out 5 pieces, walk away from the bowl."),
        ("Lanzones", "High in quantity", AMBER, AMBER_SOFT,
         "Same trap as rambutan — eaten by the handful. 5–8 pieces maximum, once."),
        ("Langka (jackfruit)", "High", AMBER, AMBER_SOFT,
         "In fruit salad, turon, and halo-halo too — it hides in desserts."),
        ("Saging (banana)", "High", AMBER, AMBER_SOFT,
         "Includes banana cue and turon at street parties."),
        ("Melon & pakwan (watermelon)", "High", AMBER, AMBER_SOFT,
         "High potassium AND counts as fluid — a double hit for dialysis patients."),
        ("Chico, atis, dalandan / orange", "High", AMBER, AMBER_SOFT,
         "Holiday-season favorites; treat like rambutan — strict small portion."),
        ("Mangga (mango)", "Moderate", TEAL, TEAL_SOFT,
         "Half of one small ripe mango is a reasonable single serving."),
        ("Ubas (grapes)", "Moderate", TEAL, TEAL_SOFT,
         'The New Year "12 grapes" tradition is fine — 12 grapes, not 12 bunches.'),
        ("Pinya (pineapple)", "Lower", GREEN, GREEN_SOFT,
         "One of the better fruit choices at a party, in one normal slice."),
        ("Mansanas (apple), peras (pear)", "Lower", GREEN, GREEN_SOFT,
         "The classic \"safe\" fruits — a whole small apple is fine for most patients."),
    ]
    y = d.fruit_table(y, rows)
    y -= 2
    y = d.box(y, "Never graze from the fruit bowl",
              "Decide your portion before you sit down, put it on a small plate, and move away from the bandehado. "
              "Decisions made in advance survive temptation; decisions made at the table do not.",
              TEAL_SOFT, TEAL, TEAL, size=9)
    d.new_page()

    # ── PAGE 7 · FIESTA PLATE IMAGE ────────────────────────────────────────
    y = d.heading(H - M - 6, "Your game plan", "The Fiesta Plate")
    y = d.image(y, "holiday-kidney-syndrome-fiesta-plate.png")
    y -= 4
    y = d.bullets(y, [
        "The goal|balance and moderation — small choices today, better tomorrows.",
        "Two favorites enjoyed slowly|beat ten favorites regretted at the ER. The full 8-step plan is on the next page.",
    ])
    d.new_page()

    # ── PAGE 8 · BUILD YOUR FIESTA PLATE — 8 STEPS ─────────────────────────
    y = d.heading(H - M - 6, "Step by step", "How to Build Your Fiesta Plate — 8 Steps")
    steps = [
        ("Don't arrive starving.",
         "Eat a normal, kidney-safe meal or snack before you leave the house. Hunger at a buffet defeats every plan ever made."),
        ("Bring your binders.",
         "If you are prescribed phosphate binders, they belong in your pocket at every party and must be taken WITH the party meal — that is exactly the meal they exist for."),
        ("Survey the whole table before touching anything.",
         "Walk the length of the buffet first. Decide your two favorites. A plan made with your eyes is stronger than one made with your stomach."),
        ("Half your plate: rice and the safest dishes.",
         "Then add your TWO chosen favorites in small portions. Two favorites enjoyed slowly beat ten favorites regretted at the ER."),
        ("One plate, one pass — walang balikan.",
         "Fill it once, then leave the buffet zone. Sit far from the food table and the grazing bowls."),
        ("Decide fruit and drink before the party.",
         "One fruit, one serving. One small cup, refilled within your budget. Decisions made in advance survive temptation; decisions made at the table do not."),
        ('Have your "no, thank you" script ready.',
         'Filipino hosts insist — it is love. Try: "Masarap talaga, pero bawal sa dialysis ko. Tikim na lang ako para hindi ako ma-ospital sa Pasko!" Said with a smile, it works.'),
        ("Take all your medicines on schedule — party or no party.",
         "Set phone alarms. The celebration is not a holiday from your BP medicines, binders, or insulin. And never \"fix\" the morning-after headache with NSAIDs (mefenamic acid, ibuprofen) — they injure whatever kidney function you have left."),
    ]
    for i, (lead, body) in enumerate(steps, 1):
        # numbered circle
        c.setFillColor(TEAL)
        c.circle(M + 9, y + 3, 9, stroke=0, fill=1)
        c.setFillColor(HexColor("#ffffff"))
        c.setFont("DJV-B", 9.5)
        c.drawCentredString(M + 9, y, str(i))
        # lead + body
        tx = M + 26
        tw = CW - 26
        c.setFillColor(NAVY)
        c.setFont("DJV-B", 10)
        c.drawString(tx, y, lead)
        y -= 13.5
        c.setFillColor(TEXT)
        c.setFont("DJV", 9.3)
        for ln in d.wrap(body, "DJV", 9.3, tw):
            c.drawString(tx, y, ln)
            y -= 12
        y -= 8
    d.new_page()

    # ── PAGE 9 · SCHEDULE ──────────────────────────────────────────────────
    y = d.heading(H - M - 6, "Non-negotiable", "Protect Your Dialysis Schedule")
    y = d.image(y, "surviving-fiestas-holidays-ckd-timing-pearl.png")
    y -= 4
    y = d.bullets(y, [
        "By December 1|check whether Dec 24, 25, 31, or Jan 1 lands on your session day; ask the unit for its holiday schedule early — good slots go fast.",
        "Move sessions EARLIER, never later|if your session falls on the holiday itself, request the day before, not the day after.",
        "The smartest party trick|book a morning slot on Dec 24 / Dec 31 and celebrate that evening — same food, far less danger.",
        "Traveling to the province?|book guest dialysis at the destination BEFORE booking the bus or flight.",
        "Never trade a session for a party|attend after your session, arrive late, leave early, or move the family celebration — your family would rather move the party than visit you in the ICU.",
    ], size=9.5)
    d.new_page()

    # ── PAGE 10 · WARNING SIGNS + WALLET CARD ─────────────────────────────
    y = d.heading(H - M - 6, "Emergency", "Warning Signs — Do NOT Wait for Your Next Session")
    c.setFont("DJV", 9.5)
    c.setFillColor(TEXT)
    for ln in d.wrap("During or after any celebration, any of these signs means go to the emergency room NOW — at "
                     "midnight, on Christmas, whenever. High potassium can stop the heart with little warning, and "
                     "the early symptoms are easy to dismiss as party fatigue.", "DJV", 9.5, CW):
        c.drawString(M, y, ln)
        y -= 12.5
    y -= 6
    y = d.bullets(y, [
        "Chest heaviness or chest pain.",
        "Palpitations|racing, skipping, or irregular heartbeat.",
        "Muscle weakness or heaviness|of the arms and legs — a classic high-potassium sign.",
        "Numbness or tingling|around the lips and fingers.",
        "Shortness of breath|cannot lie flat, frothy cough — fluid overload.",
        "Sudden swelling|of face or legs with a big weight jump.",
        "Confusion, extreme drowsiness|or decreased alertness.",
        "Hiccups that will not stop after star fruit|an emergency even if you feel \"okay\".",
    ], size=9.3, gap=2.5, bullet="!")
    y -= 2
    y = d.box(y, "Say this at the ER — exact words",
              '"I am a dialysis patient (or: I have stage __ CKD). My last dialysis was on ___. I ate a large amount '
              'of high-potassium food today. Please check my potassium and do an ECG now."',
              RED_SOFT, RED, RED, size=9)

    # wallet card (blank, fillable by pen)
    card_h = 150
    cw = CW * 0.72
    c.setStrokeColor(TEAL)
    c.setLineWidth(1.6)
    c.setFillColor(HexColor("#ffffff"))
    c.roundRect(M, y - card_h, cw, card_h, 8, stroke=1, fill=1)
    ty = y - 18
    c.setFont("DJV-B", 10)
    c.setFillColor(NAVY)
    c.drawString(M + 12, ty, "KIDNEY PATIENT — EMERGENCY CARD")
    c.setStrokeColor(TEAL)
    c.setLineWidth(1)
    c.line(M + 12, ty - 5, M + cw - 12, ty - 5)
    fields = ["Name:", "Diagnosis:   [ ] CKD stage ___   [ ] Hemodialysis   [ ] PD",
              "Dialysis days: ______________    Dry weight: _______ kg",
              "Dialysis unit & phone:", "Nephrologist:", "Allergies:"]
    ty -= 21
    c.setFont("DJV", 8.5)
    c.setFillColor(TEXT)
    for f in fields:
        c.drawString(M + 12, ty, f)
        if f.endswith(":"):
            c.setStrokeColor(HexColor("#b9c4cf"))
            c.line(M + 12 + pdfmetrics.stringWidth(f, "DJV", 8.5) + 6, ty - 1, M + cw - 12, ty - 1)
        ty -= 15
    c.setFont("DJV-B", 7.5)
    c.setFillColor(RED)
    for ln in d.wrap("IN EMERGENCY: check serum potassium + ECG immediately. Patient may need urgent dialysis.",
                     "DJV-B", 7.5, cw - 24):
        c.drawString(M + 12, ty, ln)
        ty -= 10
    c.setFont("DJV", 8)
    c.setFillColor(MUTED)
    note_x = M + cw + 12
    for i, ln in enumerate(d.wrap("Fill out in ink, cut along the border, and laminate. Keep one in your wallet and "
                                  "give one to a family member. An online fillable version is on the guide page.",
                                  "DJV", 8, CW - cw - 24)):
        c.drawString(note_x, y - 24 - i * 11, ln)
    y -= card_h + 16
    d.new_page()

    # ── PAGE 11 · CHECKLIST + REFERENCES ──────────────────────────────────
    y = d.heading(H - M - 6, "Before every celebration", "Pre-Party Checklist")
    checks = [
        "Dialysis schedule for the holiday week confirmed — session moved EARLIER if needed",
        "Phosphate binders and all medicines in pocket or bag",
        "Ate a kidney-safe meal before leaving — not arriving hungry",
        "Fruit decision made: which one, how much, once",
        "Fluid budget set; small-cup strategy ready",
        '"No thank you" script practiced',
        "Nearest open ER on a holiday identified; unit phone number saved",
        "One family member briefed on the warning signs",
        "Weigh yourself the morning after — bring the number to your next session",
    ]
    c.setFont("DJV", 10.5)
    for item in checks:
        c.setStrokeColor(TEAL)
        c.setLineWidth(1.2)
        c.rect(M, y - 3, 10, 10, stroke=1, fill=0)
        c.setFillColor(TEXT)
        c.drawString(M + 18, y, item)
        y -= 21
    y -= 8
    y = d.box(y, "For your family and hosts",
              "Food is love — and the most loving thing you can do for a kidney patient is make safe eating easy: "
              "cook one plain grilled dish, serve sauces on the side, accept their \"no\" the first time, keep the "
              "fruit bowl out of grazing distance, and know the warning signs.",
              TEAL_SOFT, TEAL, TEAL)
    y -= 4
    c.setFont("DJV-B", 9.5)
    c.setFillColor(NAVY)
    c.drawString(M, y, "References & full guide")
    y -= 14
    c.setFont("DJV", 8.5)
    c.setFillColor(MUTED)
    for ln in ["Foley RN et al., N Engl J Med 2011;365:1099-107 (long interdialytic interval)",
               "Ettinger PO et al., Am Heart J 1978 (holiday heart) · Wakasugi M et al., J Ren Nutr 2023",
               "KDOQI Clinical Practice Guideline for Nutrition in CKD: 2020 Update",
               "Full interactive guide (EN · TL · CEB · KAP): williamriveromd.com/guides/surviving-fiestas-holidays-ckd.html"]:
        c.drawString(M, y, ln)
        y -= 12
    y -= 10
    c.setFont("DJV", 8)
    c.setFillColor(FAINT)
    for ln in d.wrap("This companion is for general education and does not replace the advice of your own nephrologist "
                     "and renal dietitian. \"Holiday Kidney Syndrome\" is a descriptive teaching term used in this "
                     "practice, not an official diagnosis. © 2026 W. G. M. Rivero, MD — williamriveromd.com",
                     "DJV", 8, CW):
        c.drawString(M, y, ln)
        y -= 11
    d.footer()
    c.save()
    print(f"Wrote {OUT} ({OUT.stat().st_size // 1024} KB, {d.page} pages)")


if __name__ == "__main__":
    build()
