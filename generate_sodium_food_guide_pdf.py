#!/usr/bin/env python3
"""
Generate the expanded patient companion PDF for the Sodium & Salt Reduction CKD guide.

Produces downloads/wgmr-sodium-food-guide.pdf — a comprehensive printable
handout covering daily targets, the Filipino sodium map, smart cooking swaps,
label reading, hidden sodium, eating-out rules, the salt-substitute warning,
and the 7-day reduction plan.

Usage:
    python3 generate_sodium_food_guide_pdf.py
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

ROOT  = Path(__file__).parent
OUT   = ROOT / "downloads" / "wgmr-sodium-food-guide.pdf"
IMGS  = ROOT / "images"

# ── Colour palette ─────────────────────────────────────────────────────────
NAVY        = HexColor("#1f3864")
TEAL        = HexColor("#1a6b72")
RED         = HexColor("#b91c1c")
GREEN       = HexColor("#166534")
AMBER       = HexColor("#92400e")
TEXT        = HexColor("#1e2a38")
MUTED       = HexColor("#4a5568")
FAINT       = HexColor("#8a96a3")
WHITE       = HexColor("#ffffff")
GREEN_SOFT  = HexColor("#f0fdf4")
AMBER_SOFT  = HexColor("#fffbeb")
RED_SOFT    = HexColor("#fff0f0")
TEAL_SOFT   = HexColor("#e1f5f0")
BG          = HexColor("#f9fafb")
BORDER      = HexColor("#e2e6eb")

W, H   = A4          # 595 × 842 pt
M      = 40          # page margin
CW     = W - 2 * M  # content width
BOTTOM = 55          # minimum y before footer — nothing drawn below this

FONT_DIR = Path("/usr/share/fonts/truetype/dejavu")
pdfmetrics.registerFont(TTFont("DJV",   FONT_DIR / "DejaVuSans.ttf"))
pdfmetrics.registerFont(TTFont("DJV-B", FONT_DIR / "DejaVuSans-Bold.ttf"))
pdfmetrics.registerFont(TTFont("DJV-I", FONT_DIR / "DejaVuSans.ttf"))   # italic unavailable; use regular


# ── Image helper ─────────────────────────────────────────────────────────────
def jpeg_reader(name: str, max_w: int = 1200) -> tuple:
    im = Image.open(IMGS / name).convert("RGB")
    if im.width > max_w:
        im = im.resize((max_w, int(im.height * max_w / im.width)), Image.LANCZOS)
    buf = io.BytesIO()
    im.save(buf, "JPEG", quality=82, optimize=True)
    buf.seek(0)
    return ImageReader(buf), im.width / im.height


class Doc:
    def __init__(self):
        self.c    = canvas.Canvas(str(OUT), pagesize=A4)
        self.page = 0

    # ── Page management ───────────────────────────────────────────────────
    def footer(self):
        self.page += 1
        c = self.c
        c.setFont("DJV", 7)
        c.setFillColor(FAINT)
        c.drawString(M, 22,
            "williamriveromd.com — patient education only; always follow your nephrologist's personal advice")
        c.drawRightString(W - M, 22, f"Page {self.page}")

    def new_page(self):
        self.footer()
        self.c.showPage()

    def ensure_space(self, y: float, needed: float) -> float:
        """If fewer than `needed` points remain above BOTTOM, start a new page."""
        if y - needed < BOTTOM:
            self.new_page()
            return H - M - 10
        return y

    # ── Text helpers ──────────────────────────────────────────────────────
    def wrap(self, text: str, font: str, size: float, width: float) -> list:
        out, line = [], ""
        for word in text.split():
            t = (line + " " + word).strip()
            if pdfmetrics.stringWidth(t, font, size) <= width:
                line = t
            else:
                if line:
                    out.append(line)
                line = word
        if line:
            out.append(line)
        return out or [""]

    def text_block(self, y: float, text: str, font="DJV", size=9.5,
                   color=TEXT, width=None, x=None, leading=None) -> float:
        c = self.c
        x       = x       if x       is not None else M
        width   = width   if width   is not None else CW
        leading = leading if leading is not None else size + 3
        c.setFont(font, size)
        c.setFillColor(color)
        for ln in self.wrap(text, font, size, width):
            y = self.ensure_space(y, leading + 2)
            c.drawString(x, y, ln)
            y -= leading
        return y - 3

    # ── Section headings ──────────────────────────────────────────────────
    def heading(self, y: float, eyebrow: str, title: str, rule=True) -> float:
        c = self.c
        c.setFont("DJV-B", 8)
        c.setFillColor(TEAL)
        c.drawString(M, y, eyebrow.upper())
        y -= 18
        c.setFont("DJV-B", 16)
        c.setFillColor(NAVY)
        c.drawString(M, y, title)
        y -= 6
        if rule:
            c.setStrokeColor(TEAL)
            c.setLineWidth(1.2)
            c.line(M, y, W - M, y)
        return y - 10

    def subheading(self, y: float, text: str) -> float:
        y = self.ensure_space(y, 24)
        c = self.c
        c.setFont("DJV-B", 11)
        c.setFillColor(NAVY)
        c.drawString(M, y, text)
        return y - 14

    # ── Image ─────────────────────────────────────────────────────────────
    def image(self, y: float, name: str, caption: str = None) -> float:
        img, ratio = jpeg_reader(name)
        w = CW * 0.8
        h = w / ratio
        # If the image is taller than available space, scale it down further
        avail = y - BOTTOM - 10
        if h > avail:
            h = avail
            w = h * ratio
        x_offset = M + (CW - w) / 2
        self.c.drawImage(img, x_offset, y - h, width=w, height=h)
        y -= h
        if caption:
            self.c.setFont("DJV-I", 7.5)
            self.c.setFillColor(MUTED)
            y -= 10
            self.c.drawString(M, y, caption)
        return y - 8

    # ── Coloured box ──────────────────────────────────────────────────────
    def box(self, y: float, title: str, body: str,
            fill, border, title_color, size=9, pad=10) -> float:
        lines = self.wrap(body, "DJV", size, CW - 2 * pad - 4)
        h = pad * 2 + 14 + len(lines) * (size + 3)
        y = self.ensure_space(y, h + 12)
        c = self.c
        c.setFillColor(fill)
        c.setStrokeColor(border)
        c.setLineWidth(1.2)
        c.roundRect(M, y - h, CW, h, 7, stroke=1, fill=1)
        ty = y - pad - 9
        c.setFillColor(title_color)
        c.setFont("DJV-B", size + 0.5)
        c.drawString(M + pad, ty, title)
        ty -= 13
        c.setFillColor(TEXT)
        c.setFont("DJV", size)
        for ln in lines:
            c.drawString(M + pad, ty, ln)
            ty -= size + 3
        return y - h - 10

    # ── Bullets ───────────────────────────────────────────────────────────
    def bullets(self, y: float, items: list, size=9, gap=4, x=None) -> float:
        c   = self.c
        x   = x if x is not None else M
        bw  = CW - (x - M) - 14
        for item in items:
            if "|" in item:
                lead, _, rest = item.partition("|")
                text = lead + " — " + rest
            else:
                lead = None
                text = item
            lines = self.wrap(text, "DJV", size, bw)
            item_h = len(lines) * (size + 3) + gap + 2
            y = self.ensure_space(y, item_h)
            first = True
            for ln in lines:
                c.setFillColor(TEAL)
                c.setFont("DJV-B", size)
                if first:
                    c.drawString(x, y, "•")
                if first and lead and ln.startswith(lead):
                    c.setFillColor(TEXT)
                    c.setFont("DJV-B", size)
                    c.drawString(x + 12, y, lead)
                    c.setFont("DJV", size)
                    lw = pdfmetrics.stringWidth(lead, "DJV-B", size)
                    c.drawString(x + 12 + lw, y, ln[len(lead):])
                else:
                    c.setFillColor(TEXT)
                    c.setFont("DJV", size)
                    c.drawString(x + 12, y, ln)
                y -= size + 3
                first = False
            y -= gap
        return y

    # ── Sodium food table (with mid-table page breaks) ────────────────────
    def _table_header(self, y: float, c1, c2, c3, c4, size) -> float:
        pad = 5
        hh  = 18
        self.c.setFillColor(NAVY)
        self.c.rect(M, y - hh, CW, hh, stroke=0, fill=1)
        self.c.setFillColor(WHITE)
        self.c.setFont("DJV-B", size - 0.5)
        for label, cx in [("Food / item",     M + pad),
                           ("Serving",         M + c1 + pad),
                           ("Sodium (mg)",     M + c1 + c2 + pad),
                           ("% of 2,000 mg",  M + c1 + c2 + c3 + pad)]:
            self.c.drawString(cx, y - 12, label)
        return y - hh

    def sodium_table(self, y: float, rows: list, col_widths=None,
                     size=7.8) -> float:
        c = self.c
        if col_widths is None:
            c1, c2, c3, c4 = 160, 100, 70, 80
        else:
            c1, c2, c3, c4 = col_widths
        pad = 5
        lh  = size + 2.5
        BADGE = {
            "green": (GREEN_SOFT, GREEN),
            "amber": (AMBER_SOFT, AMBER),
            "red":   (RED_SOFT,   RED),
        }

        y = self._table_header(y, c1, c2, c3, c4, size)

        for i, row in enumerate(rows):
            if len(row) == 1:
                # section divider
                sh = lh + 4
                y = self.ensure_space(y, sh + 20)
                c.setFillColor(TEAL_SOFT)
                c.rect(M, y - sh, CW, sh, stroke=0, fill=1)
                c.setFillColor(TEAL)
                c.setFont("DJV-B", size - 0.5)
                c.drawString(M + pad, y - sh + 4, row[0].upper())
                y -= sh
                continue

            food, serving, sodium, pct, level = row
            food_lines = self.wrap(food, "DJV", size, c1 - 2 * pad)
            rh = max(1, len(food_lines)) * lh + 2 * pad - 1

            # Page break mid-table: reprint header on new page
            if y - rh < BOTTOM:
                self.new_page()
                y = H - M - 10
                y = self._table_header(y, c1, c2, c3, c4, size)

            fill = HexColor("#ffffff") if i % 2 == 0 else BG
            c.setFillColor(fill)
            c.rect(M, y - rh, CW, rh, stroke=0, fill=1)
            c.setStrokeColor(BORDER)
            c.setLineWidth(0.5)
            c.line(M, y - rh, M + CW, y - rh)

            ty = y - pad - size + 1
            c.setFillColor(TEXT)
            c.setFont("DJV", size)
            for ln in food_lines:
                c.drawString(M + pad, ty, ln)
                ty -= lh

            srv_lines = self.wrap(serving, "DJV", size, c2 - 2 * pad)
            ty = y - pad - size + 1
            for ln in srv_lines:
                c.drawString(M + c1 + pad, ty, ln)
                ty -= lh

            c.setFont("DJV-B", size)
            c.setFillColor(NAVY)
            c.drawString(M + c1 + c2 + pad, y - pad - size + 1, str(sodium))

            bf, bc = BADGE.get(level, BADGE["amber"])
            self._badge(M + c1 + c2 + c3 + pad, y - pad - 1, pct, bf, bc, size - 0.5)

            y -= rh

        return y - 8

    def _badge(self, x, y, label, fill, color, size=7.5) -> float:
        bw = pdfmetrics.stringWidth(label, "DJV-B", size) + 8
        bh = size + 4
        self.c.setFillColor(fill)
        self.c.roundRect(x, y - bh + 2, bw, bh, 3, stroke=0, fill=1)
        self.c.setFillColor(color)
        self.c.setFont("DJV-B", size)
        self.c.drawString(x + 4, y - size + 2, label)
        return x + bw + 4

    # ── Swap table ────────────────────────────────────────────────────────
    def swap_table(self, y: float, rows: list, size=8.5) -> float:
        c  = self.c
        lh = size + 2.5
        c1 = (CW - 20) // 2
        hh = 16

        def draw_header(y):
            c.setFillColor(NAVY)
            c.rect(M, y - hh, CW, hh, stroke=0, fill=1)
            c.setFillColor(WHITE)
            c.setFont("DJV-B", size - 0.5)
            c.drawString(M + 6, y - 11, "INSTEAD OF …")
            c.drawString(M + c1 + 26, y - 11, "TRY THIS …")
            return y - hh

        y = draw_header(y)

        for i, (frm, to) in enumerate(rows):
            from_lines = self.wrap(frm, "DJV", size, c1 - 8)
            to_lines   = self.wrap(to,  "DJV", size, c1 - 8)
            rh = max(len(from_lines), len(to_lines)) * lh + 10

            if y - rh < BOTTOM:
                self.new_page()
                y = H - M - 10
                y = draw_header(y)

            fill = HexColor("#ffffff") if i % 2 == 0 else BG
            c.setFillColor(fill)
            c.rect(M, y - rh, CW, rh, stroke=0, fill=1)
            c.setStrokeColor(BORDER)
            c.setLineWidth(0.4)
            c.line(M, y - rh, M + CW, y - rh)

            ty = y - 6 - size + 1
            c.setFillColor(RED)
            c.setFont("DJV-B", size - 0.5)
            for ln in from_lines:
                c.drawString(M + 6, ty, ln)
                ty -= lh

            c.setFillColor(FAINT)
            c.setFont("DJV-B", size + 1)
            c.drawString(M + c1 + 6, y - rh // 2 - 4, "→")

            ty = y - 6 - size + 1
            c.setFillColor(GREEN)
            c.setFont("DJV", size)
            for ln in to_lines:
                c.drawString(M + c1 + 26, ty, ln)
                ty -= lh

            y -= rh

        return y - 8

    # ── Two-column feature cards ──────────────────────────────────────────
    def two_col_cards(self, y: float, cards: list, size=8.5) -> float:
        c   = self.c
        cw  = (CW - 8) // 2
        pad = 10
        lh  = size + 2.5
        DOT = {
            "teal": TEAL, "green": GREEN, "amber": AMBER,
            "red":  RED,  "navy":  NAVY,  "gold":  HexColor("#b8962e"),
        }
        col_x = [M, M + cw + 8]
        col_y = [y, y]

        for i, (dot, title, body) in enumerate(cards):
            col = i % 2
            # At start of each pair (col 0), ensure both cards will fit
            if col == 0:
                # measure both cards in this pair
                def card_h(t, b):
                    tl = self.wrap(t, "DJV-B", size, cw - 2 * pad - 10)
                    bl = self.wrap(b, "DJV",   size, cw - 2 * pad - 4)
                    return pad * 2 + (len(tl) + len(bl)) * lh + 8
                next_cards = cards[i: i + 2]
                pair_h = max(card_h(t, b) for _, t, b in next_cards)
                if col_y[0] - pair_h < BOTTOM:
                    self.new_page()
                    col_y = [H - M - 10, H - M - 10]

            cx = col_x[col]
            ty = col_y[col]

            title_lines = self.wrap(title, "DJV-B", size, cw - 2 * pad - 10)
            body_lines  = self.wrap(body,  "DJV",   size, cw - 2 * pad - 4)
            h = pad * 2 + (len(title_lines) + len(body_lines)) * lh + 8

            c.setFillColor(BG)
            c.setStrokeColor(BORDER)
            c.setLineWidth(0.8)
            c.roundRect(cx, ty - h, cw, h, 6, stroke=1, fill=1)

            ity = ty - pad - size + 1
            dot_color = DOT.get(dot, TEAL)
            c.setFillColor(dot_color)
            c.circle(cx + pad + 4, ity + 3, 4, stroke=0, fill=1)
            c.setFillColor(NAVY)
            c.setFont("DJV-B", size)
            for ln in title_lines:
                c.drawString(cx + pad + 12, ity, ln)
                ity -= lh

            ity -= 2
            c.setFillColor(TEXT)
            c.setFont("DJV", size)
            for ln in body_lines:
                c.drawString(cx + pad + 4, ity, ln)
                ity -= lh

            col_y[col] = ty - h - 8

        return min(col_y) - 4

    # ── Warning box ───────────────────────────────────────────────────────
    def warning_box(self, y: float, title: str, lines: list, size=9) -> float:
        c   = self.c
        pad = 12
        lh  = size + 3
        all_lines = []
        for ln in lines:
            all_lines += self.wrap(ln, "DJV", size, CW - 2 * pad - 4)
            all_lines.append("")
        h = pad * 2 + 22 + len(all_lines) * lh + 4
        y = self.ensure_space(y, h + 12)
        c.setFillColor(RED_SOFT)
        c.setStrokeColor(RED)
        c.setLineWidth(2)
        c.roundRect(M, y - h, CW, h, 8, stroke=1, fill=1)
        ty = y - pad - 10
        c.setFillColor(RED)
        c.setFont("DJV-B", size + 2)
        c.drawString(M + pad, ty, "  " + title)
        ty -= 16
        c.setFillColor(TEXT)
        c.setFont("DJV", size)
        for ln in all_lines:
            c.drawString(M + pad, ty, ln)
            ty -= lh
        return y - h - 10

    # ── 7-day plan grid ───────────────────────────────────────────────────
    def day_plan_grid(self, y: float, days: list, size=8.5) -> float:
        c   = self.c
        nc  = 3
        cw  = (CW - (nc - 1) * 6) // nc
        pad = 8
        lh  = size + 2.5

        cards = []
        for day, body in days:
            body_lines = self.wrap(body, "DJV", size, cw - 2 * pad - 4)
            h = pad * 2 + 14 + len(body_lines) * lh
            cards.append((day, body_lines, h))

        col_x = [M + i * (cw + 6) for i in range(nc)]
        row_i = 0
        while row_i * nc < len(cards):
            row    = cards[row_i * nc: row_i * nc + nc]
            row_h  = max(card[2] for card in row)
            y = self.ensure_space(y, row_h + 8)
            for col_j, (day, body_lines, _) in enumerate(row):
                cx = col_x[col_j]
                c.setFillColor(TEAL_SOFT)
                c.setStrokeColor(TEAL)
                c.setLineWidth(0.8)
                c.roundRect(cx, y - row_h, cw, row_h, 6, stroke=1, fill=1)
                c.setFillColor(TEAL)
                c.setFont("DJV-B", size - 0.5)
                c.drawString(cx + pad, y - pad - size + 2, day.upper())
                ity = y - pad - size - 6
                c.setFillColor(TEXT)
                c.setFont("DJV", size)
                for ln in body_lines:
                    c.drawString(cx + pad, ity, ln)
                    ity -= lh
            y -= row_h + 6
            row_i += 1
        return y - 4


# ════════════════════════════════════════════════════════════════════════════
def build():
    d = Doc()
    c = d.c
    c.setTitle("Sodium & Salt Reduction — CKD Patient Companion")
    c.setAuthor("W. G. M. Rivero, MD, FPCP, DPSN")

    # ════════════════════════════════════════════════════════════════════════
    # PAGE 1 — COVER
    # ════════════════════════════════════════════════════════════════════════
    y = H - M - 4
    c.setFont("DJV-B", 8)
    c.setFillColor(TEAL)
    c.drawString(M, y, "NEPHROLOGY · NUTRITION · WILLIAMRIVEROMD.COM")
    y -= 28

    c.setFont("DJV-B", 22)
    c.setFillColor(NAVY)
    c.drawString(M, y, "Sodium & Salt Reduction in CKD")
    y -= 18
    c.setFont("DJV-B", 12)
    c.setFillColor(TEAL)
    c.drawString(M, y, "Your most powerful daily choice for protecting your kidneys")
    y -= 14
    c.setFont("DJV", 9)
    c.setFillColor(MUTED)
    c.drawString(M, y,
        "W. G. M. Rivero, MD, FPCP, DPSN — Internal Medicine · Nephrology · Clinical Nutrition")
    y -= 16

    y = d.image(y, "sodium-hero.png")
    y -= 4

    # Key stats row
    stats = [
        ("< 2,000 mg",    "sodium / day",   "CKD target"),
        ("4,500–6,000 mg","sodium / day",   "Filipino average"),
        ("1 g salt",      "= 400 mg sodium","The key conversion"),
    ]
    sw = CW / 3
    for i, (val, unit, label) in enumerate(stats):
        sx = M + i * sw
        c.setFillColor(TEAL)
        c.roundRect(sx + 3, y - 52, sw - 6, 52, 6, stroke=0, fill=1)
        c.setFillColor(HexColor("#d4af4f"))
        c.setFont("DJV-B", 11)
        c.drawCentredString(sx + sw / 2, y - 18, val)
        c.setFillColor(WHITE)
        c.setFont("DJV", 8)
        c.drawCentredString(sx + sw / 2, y - 30, unit)
        c.setFillColor(HexColor("#c8e8ea"))
        c.setFont("DJV-B", 7)
        c.drawCentredString(sx + sw / 2, y - 44, label.upper())
    y -= 62

    y = d.text_block(y,
        "Of all the things a CKD patient can change about their diet, sodium reduction "
        "has the strongest evidence and the largest measurable benefit — and it's the "
        "area where most Filipinos have the most room to improve.",
        size=9.5)

    y = d.box(y, "Why it works so powerfully",
        "Every 2.3 g reduction in daily sodium lowers systolic BP by 5 mmHg and reduces "
        "proteinuria by ~25% in patients on ACE inhibitors or ARBs — amplifying the effect "
        "of every kidney-protective drug you take. Each extra 1 g/day above target raises "
        "cardiovascular event risk by 17%, independent of blood pressure (PURE study, NEJM 2014).",
        TEAL_SOFT, TEAL, TEAL, size=9)

    y -= 6
    y = d.subheading(y, "Daily sodium targets by patient group")
    y -= 2

    # Targets table (inline — small enough to always fit)
    target_rows = [
        ("General CKD Stage 1–4",               "< 2,000 mg/day",  "< 5 g salt (1 tsp)"),
        ("CKD with hypertension or proteinuria", "< 1,500 mg/day",  "< 3.75 g (¾ tsp)"),
        ("CKD with heart failure / edema",       "< 1,500 mg/day",  "< 3.75 g (¾ tsp)"),
        ("Haemodialysis (HD)",                   "< 2,000 mg/day",  "+ fluid ≤ 1 L/day"),
        ("Peritoneal dialysis (PD)",             "2,000–2,500 mg",  "Still far below typical PH intake"),
        ("Per-meal practical target",            "< 600 mg / meal", "3 × 600 + snacks ≤ 200 = ~2,000 mg"),
    ]
    lh_t      = 10.5
    th        = 16
    row_cols  = [160, 110, CW - 160 - 110]
    c.setFillColor(NAVY)
    c.rect(M, y - th, CW, th, stroke=0, fill=1)
    c.setFillColor(WHITE); c.setFont("DJV-B", 7.5)
    c.drawString(M + 5, y - 11, "Patient group")
    c.drawString(M + row_cols[0] + 5, y - 11, "Daily sodium target")
    c.drawString(M + row_cols[0] + row_cols[1] + 5, y - 11, "Notes / salt equivalent")
    y -= th
    for i, (grp, tgt, note) in enumerate(target_rows):
        rh = lh_t + 8
        y = d.ensure_space(y, rh + 4)
        c.setFillColor(WHITE if i % 2 == 0 else BG)
        c.rect(M, y - rh, CW, rh, stroke=0, fill=1)
        c.setStrokeColor(BORDER); c.setLineWidth(0.4)
        c.line(M, y - rh, M + CW, y - rh)
        c.setFillColor(TEXT); c.setFont("DJV", 8.5)
        c.drawString(M + 5, y - rh + 5, grp)
        c.setFont("DJV-B", 8.5); c.setFillColor(NAVY)
        c.drawString(M + row_cols[0] + 5, y - rh + 5, tgt)
        c.setFont("DJV", 8); c.setFillColor(MUTED)
        c.drawString(M + row_cols[0] + row_cols[1] + 5, y - rh + 5, note)
        y -= rh
    y -= 6

    y = d.ensure_space(y, 14)
    c.setFont("DJV-I", 8); c.setFillColor(MUTED)
    c.drawString(M, y,
        "Source: KDIGO 2024 CKD guideline · AHA recommendations · WHO sodium intake guideline 2012")

    d.new_page()

    # ════════════════════════════════════════════════════════════════════════
    # PAGE 2 — FILIPINO SODIUM MAP PART 1
    # ════════════════════════════════════════════════════════════════════════
    y = H - M - 4
    y = d.heading(y, "The Filipino Sodium Map — Part 1",
                  "Where the sodium actually hides in Filipino food")
    y = d.image(y, "sodium-filipino-foods.png")
    y -= 4

    y = d.text_block(y,
        "All values are per typical Filipino serving. The % column shows what fraction of "
        "the 2,000 mg CKD daily target each single serving consumes.",
        size=8.5)
    y -= 4

    rows_p2 = [
        ("Condiments and sauces",),
        ("Patis (fish sauce)",            "1 tbsp (15 mL)", "1,420", "71%", "red"),
        ("Bagoong alamang",               "1 tbsp",         "1,370", "69%", "red"),
        ("Bagoong isda (sardine paste)",  "2 tbsp",         "1,500", "75%", "red"),
        ("Toyo (regular soy sauce)",      "1 tbsp",         "900",   "45%", "red"),
        ("Toyomansi (toyo + calamansi)",  "1 tbsp",         "820",   "41%", "red"),
        ("Reduced-sodium toyo",           "1 tbsp",         "540",   "27%", "amber"),
        ("Banana ketchup",                "1 tbsp",         "165",   "8%",  "amber"),
        ("Vinegar (suka)",                "1 tbsp",         "2",     "< 1%","green"),
        ("Calamansi juice",               "1 tbsp",         "1",     "< 1%","green"),
        ("Bouillon, seasoning powders, instant mixes",),
        ("Knorr bouillon cube",           "1 cube (10 g)",  "1,500", "75%", "red"),
        ("Maggi Magic Sarap",             "1 sachet (8 g)", "1,200", "60%", "red"),
        ("Powdered sinigang mix",         "1 sachet (44 g)","1,540", "77%", "red"),
        ("Powdered adobo mix",            "1 sachet",       "1,200", "60%", "red"),
        ("Pancit canton seasoning packet","1 packet",       "1,720", "86%", "red"),
        ("Instant noodles and ready meals",),
        ("Lucky Me Pancit Canton",        "1 pack (80 g)",  "1,720", "86%", "red"),
        ("Nissin Cup Noodles",            "1 cup (60 g)",   "1,800", "90%", "red"),
        ("Lucky Me Beef Mami",            "1 pack",         "1,520", "76%", "red"),
        ("Nissin Yakisoba",               "1 pack",         "1,650", "83%", "red"),
        ("Canned goods",),
        ("Corned beef",                   "½ cup (100 g)",  "950",   "48%", "red"),
        ("Spam",                          "2 oz slice (56 g)","790", "40%", "amber"),
        ("Sardines in tomato sauce",      "½ can (70 g)",   "480",   "24%", "amber"),
        ("Vienna sausage",                "4 pieces (60 g)","470",   "24%", "amber"),
        ("Luncheon meat (CDO / Purefoods)","1 slice (30 g)","380",   "19%", "amber"),
        ("Tuna flakes in oil, drained",   "½ can (70 g)",   "250",   "13%", "amber"),
    ]
    y = d.sodium_table(y, rows_p2, size=7.8)

    d.new_page()

    # ════════════════════════════════════════════════════════════════════════
    # PAGE 3 — FILIPINO SODIUM MAP PART 2
    # ════════════════════════════════════════════════════════════════════════
    y = H - M - 4
    y = d.heading(y, "The Filipino Sodium Map — Part 2",
                  "Cured meats, ulam, fast food, snacks, and safer choices")

    rows_p3 = [
        ("Cured / processed meats and fish",),
        ("Daing na bangus",               "100 g",             "1,200","60%","red"),
        ("Tinapa (smoked fish)",          "1 piece (80 g)",    "900",  "45%","red"),
        ("Tapa",                          "100 g",             "850",  "43%","red"),
        ("Longganisa (sweet)",            "2 pieces (80 g)",   "750",  "38%","amber"),
        ("Tocino",                        "100 g",             "670",  "34%","amber"),
        ("Hotdog (Tender Juicy/Purefoods)","2 pieces (90 g)",  "540",  "27%","amber"),
        ("Embutido",                      "1 slice (60 g)",    "420",  "21%","amber"),
        ("Common ulam and carinderia dishes",),
        ("Pancit canton (carinderia plate)","1 plate (~300 g)","1,800","90%","red"),
        ("Sinigang (with mix sachet)",    "1 bowl (~400 mL)",  "1,500","75%","red"),
        ("Pancit palabok",                "1 plate",           "1,400","70%","red"),
        ("Adobo (chicken / pork)",        "1 cup (~250 g)",    "1,200","60%","red"),
        ("Kare-kare with bagoong",        "1 cup + 1 tbsp bagoong","1,800","90%","red"),
        ("Lugaw with patis",              "1 bowl",            "800",  "40%","amber"),
        ("Tinola (no patis added)",       "1 bowl",            "520",  "26%","amber"),
        ("Inihaw na liempo (no marinade)","100 g",             "180",  "9%", "green"),
        ("Fast food",),
        ("Jollibee Chickenjoy",           "1 piece",           "690",  "35%","amber"),
        ("Jollibee Spaghetti",            "1 plate",           "1,100","55%","red"),
        ("McDo Crispy Chicken Fillet",    "1 piece",           "740",  "37%","amber"),
        ("McDo Big Mac",                  "1 sandwich",        "970",  "49%","red"),
        ("Mang Inasal (chicken + rice)",  "1 meal",            "1,250","63%","red"),
        ("KFC Original Recipe",           "1 piece",           "820",  "41%","amber"),
        ("Snacks, bread, and safer choices",),
        ("Boy Bawang (garlic corn nuts)", "1 pack (100 g)",    "600",  "30%","amber"),
        ("Pringles",                      "1 small can (50 g)","530",  "27%","amber"),
        ("Sky Flakes crackers",           "4 crackers (30 g)", "260",  "13%","amber"),
        ("Pandesal",                      "2 pieces (50 g)",   "240",  "12%","amber"),
        ("Nova multigrain",               "1 pack (40 g)",     "180",  "9%", "green"),
        ("Plain steamed rice (kanin)",    "1 cup",             "< 5",  "< 1%","green"),
        ("Fresh bangus, baked, no salt",  "100 g",             "75",   "4%", "green"),
        ("Boiled egg, no added salt",     "1 large",           "70",   "4%", "green"),
        ("Fresh fruit (any)",             "per serving",       "0–10", "< 1%","green"),
    ]
    y = d.sodium_table(y, rows_p3, size=7.8)

    y -= 8
    y = d.box(y, "The hardest truth in this table",
        "One bowl of sinigang made with a sinigang mix sachet consumes three-quarters of "
        "your daily sodium budget. One pack of pancit canton nearly the entire day. The food "
        "itself is not the problem — it is the seasoning packets and condiment culture wrapped "
        "around it. Replace the packets, keep the dish.",
        AMBER_SOFT, HexColor("#d97706"), AMBER, size=9)

    d.new_page()

    # ════════════════════════════════════════════════════════════════════════
    # PAGE 4 — SMART SWAPS + READING LABELS
    # ════════════════════════════════════════════════════════════════════════
    y = H - M - 4
    y = d.heading(y, "Smart Swaps",
                  "Lower-sodium versions of the food you already cook")
    y = d.image(y, "sodium-cooking-swaps.png")
    y -= 2

    swap_rows = [
        ("Patis on eggs / fried rice (1 tbsp = 1,420 mg)",
         "Calamansi juice + crushed garlic + black pepper (~5 mg). Add a drop of patis at the end only if needed (~120 mg)."),
        ("Sinigang mix sachet (1,540 mg)",
         "Fresh sampalok pulp boiled and strained, or kamias, or unripe green mango. Add a small amount of patis at the end only (~150 mg total)."),
        ("Knorr / Maggi cube in soup (1,400–1,500 mg)",
         "Homemade broth: chicken bones + onion + ginger + leeks, simmered 1 hour, strained, frozen in portions. ~80 mg/cup."),
        ("Pancit canton with seasoning packet (1,720 mg)",
         "Same noodles — throw out the packet. Sauté with garlic, ginger, cabbage, carrot, light low-sodium toyo (~400 mg total)."),
        ("Corned beef breakfast (950 mg/serving)",
         "Fresh ground beef sautéed with onion, garlic, tomato, calamansi, pepper (~120 mg)."),
        ("Daing na bangus (1,200 mg)",
         "Fresh bangus baked or grilled with calamansi, garlic, onion, pepper (~75 mg)."),
        ("Adobo with full toyo (1,200 mg/serving)",
         "Adobo with half the toyo + double the vinegar + extra garlic and bay leaf (~520 mg)."),
        ("Hotdog, 2 pieces (540 mg)",
         "Fresh chicken or pork strips marinated in calamansi / garlic / pepper, pan-grilled (~80 mg)."),
        ("Toyomansi dipping sauce (820 mg/tbsp)",
         "Pure calamansi + garlic + chili (~10 mg). Add 1 tsp toyo only if needed (~300 mg)."),
        ("Bagoong on kare-kare (1,370 mg/tbsp)",
         "Slow-roasted shrimp paste mixed with toasted garlic and chili — use ½ tsp instead of 1 tbsp (~230 mg)."),
        ("Instant noodle breakfast (1,720 mg)",
         "Lugaw made with homemade broth, ginger, and scallions; one boiled egg on top (~250 mg)."),
    ]
    y = d.swap_table(y, swap_rows, size=8)

    y -= 8
    y = d.subheading(y, "Reading nutrition labels — the 4 numbers that matter")
    y -= 4

    label_cards = [
        ("green", "< 140 mg per serving — LOW",
         "Buy freely. Two or three servings still keep you well under target. "
         "Look for this on canned goods, sauces, and snacks."),
        ("amber", "140–400 mg per serving — MODERATE",
         "Acceptable in limited amounts (1–2 servings per day max). "
         "Account for it in the day's running total."),
        ("red",   "400–800 mg per serving — HIGH",
         "One serving is 20–40% of your day's allowance. Use sparingly "
         "or find a lower-sodium alternative."),
        ("navy",  "> 800 mg per serving — VERY HIGH",
         "Avoid for daily eating. A single serving consumes nearly half "
         "the day's budget. Reserve for rare occasions."),
    ]
    y = d.two_col_cards(y, label_cards, size=8.5)

    y -= 4
    y = d.bullets(y, [
        'Servings per container|a small can of corned beef lists "2.5 servings" — the sodium '
        'on the front is per serving, not per can. Multiply.',
        '"Reduced sodium" ≠ low sodium|it means 25% less than the original. '
        'If the original was 1,800 mg, "reduced" is still 1,350 mg.',
        '"No salt added" ≠ sodium-free|always check the actual milligram number.',
        'Potassium chloride on the ingredient list|means it is a salt substitute. '
        'DANGEROUS in CKD — see the warning on the next page.',
        'MSG (E621), sodium bicarbonate, sodium nitrite, sodium phosphate|all count '
        'toward your daily sodium limit even though they are not "salt."',
    ], size=8.5)

    d.new_page()

    # ════════════════════════════════════════════════════════════════════════
    # PAGE 5 — COOKING TIPS + HIDDEN SODIUM + EATING OUT
    # ════════════════════════════════════════════════════════════════════════
    y = H - M - 4
    y = d.heading(y, "Cooking Without Salt",
                  "How to make Filipino food taste Filipino — with less sodium")

    cooking_cards = [
        ("green", "Lean on acid",
         "Calamansi, vinegar (suka), tamarind (sampalok), kamias, unripe green mango, sili "
         "leaves. Acid sharpens flavour the way salt does — without the sodium load."),
        ("amber", "Use heat and aromatics",
         "Sili labuyo, black pepper, ginger, lots of garlic, sibuyas, kutsay (leeks), "
         "tanglad, dahon ng laurel, oregano. Bloom them in oil first for maximum aroma."),
        ("teal", "Build your own broth",
         "Save bones in the freezer. Simmer 2–3 hrs with onion, ginger, carrot, peppercorns. "
         "Strain, portion into 1-cup containers, freeze. Replaces every Maggi cube."),
        ("navy", "Salt at the table, not the pot",
         "Sodium on the surface tastes stronger than sodium dissolved through. A small pinch "
         "sprinkled at serving time equals a much larger amount added during cooking."),
        ("red", "Rinse canned goods",
         "Drain canned tuna, sardines, beans, or vegetables into a strainer and rinse under "
         "running water for 60 seconds — removes 30–40% of the sodium."),
        ("gold", "Grill, bake, inihaw",
         "High-heat dry cooking concentrates natural flavour and reduces the need for added "
         "salt. Grilled bangus with garlic and pepper rivals any salted version for taste."),
    ]
    y = d.two_col_cards(y, cooking_cards, size=8.5)

    y -= 6
    y = d.subheading(y, "Hidden sodium — sources you would never suspect")
    y = d.image(y, "sodium-hidden.png")
    y -= 2

    hidden_rows = [
        ("Pandesal / sliced bread",       "120–150 mg/piece",  "Salt controls yeast activity — 4–6 pieces a day adds up."),
        ("Breakfast cereals",             "180–250 mg/cup",    "Cornflakes, Special K — not necessarily low-sodium."),
        ("Processed cheese (Eden)",       "300–400 mg/slice",  "Sodium emulsifies the cheese and extends shelf life."),
        ("Pickles / atchara",             "500–700 mg/serving","Pickled in salt brine — even 'unsweetened' versions."),
        ("Frozen pre-marinated fish",     "400–800 mg/piece",  "Supermarket bangus often soaked in salt water for shelf life."),
        ("Antacids (Maalox, Kremil, eno)","200–500 mg/dose",   "Sodium bicarbonate base — significant if taken several times daily."),
        ("3-in-1 coffee sachets",         "40–80 mg/sachet",   "Sodium emulsifiers in the creamer; 4 cups = 200+ mg from coffee alone."),
        ("Bottled salad dressing",        "200–500 mg/tbsp",   "Make your own with calamansi, suka, garlic — zero sodium."),
        ("Isotonic / sports drinks",      "40–200 mg/serving", "Sodium added for electrolyte balance. Always read the label."),
    ]

    hc  = [160, 110, CW - 160 - 110]
    sz8 = 7.8
    lh8 = sz8 + 2.5
    hth = 15

    def draw_hidden_header(y):
        c.setFillColor(NAVY); c.rect(M, y - hth, CW, hth, stroke=0, fill=1)
        c.setFillColor(WHITE); c.setFont("DJV-B", 7.5)
        c.drawString(M + 4, y - 10, "Hidden source")
        c.drawString(M + hc[0] + 4, y - 10, "Typical sodium")
        c.drawString(M + hc[0] + hc[1] + 4, y - 10, "Why it is there")
        return y - hth

    y = draw_hidden_header(y)
    for i, (src, amt, why) in enumerate(hidden_rows):
        why_lines = d.wrap(why, "DJV", sz8, hc[2] - 8)
        rh = max(1, len(why_lines)) * lh8 + 6
        if y - rh < BOTTOM:
            d.new_page()
            y = H - M - 10
            y = draw_hidden_header(y)
        c.setFillColor(WHITE if i % 2 == 0 else BG)
        c.rect(M, y - rh, CW, rh, stroke=0, fill=1)
        c.setStrokeColor(BORDER); c.setLineWidth(0.4)
        c.line(M, y - rh, M + CW, y - rh)
        ty = y - rh + 4
        c.setFillColor(TEXT); c.setFont("DJV-B", sz8)
        c.drawString(M + 4, ty, src)
        c.setFont("DJV", sz8)
        c.drawString(M + hc[0] + 4, ty, amt)
        for ln in why_lines:
            c.drawString(M + hc[0] + hc[1] + 4, ty, ln)
            ty += lh8
        y -= rh
    y -= 10

    y = d.subheading(y, "Eating out and carinderia survival")
    eat_cards = [
        ("green", "Order grilled and steamed",
         "Inihaw na isda, tinolang manok (no patis), grilled liempo, pinakbet without bagoong, "
         "chopsuey, fresh lumpia, kanin. Typically 300–600 mg per serving."),
        ("red",   "Avoid breaded, brined, and soup-based",
         "Pancit (any), sinigang (the broth holds all the sodium), kare-kare with bagoong, "
         "fast-food breakfast sets. Often > 1,000 mg per plate."),
        ("amber", '"Pakitabi lang po ang sauce."',
         "Ask for toyo, bagoong, or gravy on the side and dip lightly. One meal can drop "
         "600–800 mg of sodium by this single change alone."),
        ("navy",  "Skip or share the soup",
         "Restaurant soup broths are the highest-sodium item on the menu. "
         "If you order soup, share it, eat the solids, and leave most of the broth."),
    ]
    y = d.two_col_cards(y, eat_cards, size=8.5)

    d.new_page()

    # ════════════════════════════════════════════════════════════════════════
    # PAGE 6 — SALT SUBSTITUTES WARNING + 7-DAY PLAN
    # ════════════════════════════════════════════════════════════════════════
    y = H - M - 4
    y = d.heading(y, "Critical Warning",
                  "Why \"low-sodium salt\" can be lethal in advanced CKD")

    y = d.warning_box(y, "POTASSIUM CHLORIDE DANGER", [
        "Almost every commercial salt substitute (LoSalt, Pansalt, Morton Lite Salt, "
        "and most \"heart-healthy\" salts) replaces sodium with potassium chloride — "
        "50-70% by weight.",
        "One teaspoon contains 1,500–2,000 mg of potassium. In a CKD patient with "
        "impaired potassium excretion, this can produce life-threatening hyperkalemia "
        "within hours. Hyperkalemia at > 6.0 mEq/L is a cardiac arrhythmia emergency; "
        "the first symptom may be cardiac arrest.",
        "AVOID COMPLETELY in CKD Stage 3b–5, in dialysis patients, and in anyone "
        "on an ACE inhibitor, ARB, or spironolactone.",
        "Safe in early CKD Stage 1–2 ONLY if serum potassium is normal and monitored.",
        "Also hidden in many packaged \"low-sodium\" canned goods and sauces — always "
        "read the ingredient list. If \"potassium chloride\" appears, do not buy.",
    ], size=8.8)

    y -= 4
    y = d.box(y, "The safe alternatives",
        "The safe flavour boosters are not salt substitutes at all — they are calamansi, "
        "vinegar, sampalok, garlic, ginger, sili, bay leaf, black pepper, kutsay, "
        "and tanglad: zero sodium, maximum Filipino flavour.",
        GREEN_SOFT, GREEN, GREEN, size=9)

    y -= 6
    y = d.subheading(y, "The 7-Day Reduction Plan")
    y = d.text_block(y,
        "Going from a 5-gram day to a 2-gram day overnight sets most people up for failure. "
        "Replace the highest-impact sources first, in an order that builds momentum.",
        size=9)
    y -= 4

    day_cards = [
        ("Day 1", "Move the salt shaker off the dining table to a cabinet. Add salt during cooking only. "
                  "Typically cuts ~300 mg per day."),
        ("Day 2", "Replace breakfast patis with calamansi + garlic + pepper on eggs or fried rice. "
                  "Reclaims ~1,400 mg every morning."),
        ("Day 3", "One day without instant noodles. Replace with rice + boiled egg + sautéed kangkong. "
                  "Saves ~1,500 mg."),
        ("Day 4", "If you do eat instant noodles today, throw out the seasoning packet — sauté with "
                  "garlic, ginger, and low-sodium toyo. Saves ~1,000 mg."),
        ("Day 5", "No bouillon cubes. Make a small batch of homemade chicken broth. "
                  "Use it wherever a recipe calls for water + Maggi/Knorr. Saves ~1,500 mg per cube avoided."),
        ("Day 6", "Read every label before buying at the grocery. Avoid anything > 400 mg per serving. "
                  "Check the ingredient list for potassium chloride."),
        ("Day 7", "Eat out only once, choose well: grilled fish, inihaw, or a vegetable dish. "
                  "Ask for sauce on the side. Skip the soup. Drink water, not soft drinks."),
    ]
    y = d.day_plan_grid(y, day_cards, size=8)

    y -= 6
    y = d.box(y, "By the end of Week 1",
        "Most patients who follow this plan reach 2,000–2,500 mg per day — already a "
        "meaningful improvement over the typical 5,000 mg starting point. Two more weeks "
        "of consistency and the new pattern becomes the default. Blood pressure responds "
        "within 3–4 weeks. Proteinuria responds within 6–8 weeks.",
        GREEN_SOFT, GREEN, GREEN, size=9)

    d.new_page()

    # ════════════════════════════════════════════════════════════════════════
    # PAGE 7 — CHECKLIST + DOCTOR CARD + DISCLAIMER
    # ════════════════════════════════════════════════════════════════════════
    y = H - M - 4
    y = d.heading(y, "Quick Reference",
                  "Sodium & Salt Reduction — Pocket Checklist")

    y = d.subheading(y, "Kitchen substitutions to make this week")
    y = d.bullets(y, [
        "Replace Maggi / Knorr cube with a small jar of dried onion + dried garlic + black pepper — "
        "use 1 teaspoon in soups and stews.",
        "Keep a bottle of reduced-sodium toyo within reach; move the regular toyo to the back of the cupboard.",
        "Buy 4–5 calamansi a week. Squeeze fresh into eggs, rice, soup, fish, even into water.",
        "Make and freeze one batch of homemade chicken broth. Use it everywhere a recipe calls for water + bouillon.",
        "Move the salt shaker off the dining table to discourage casual sprinkling.",
    ], size=9.5)

    y -= 6
    y = d.subheading(y, "Flavour boosters that add zero sodium")
    zero_na = [
        ("teal",  "Calamansi juice",      "Brightens any dish. Excellent on eggs, fish, rice, lugaw."),
        ("green", "Suka (vinegar)",        "The foundation of adobo and dipping sauces. Zero sodium."),
        ("amber", "Garlic & ginger",       "Sauté in oil first to build deep base flavour."),
        ("red",   "Sili (chili)",          "Any variety — labuyo, siling mahaba — adds heat with no sodium."),
        ("navy",  "Sampalok / kamias",     "Natural souring agents for sinigang — skip the mix."),
        ("gold",  "Black pepper",          "Ground fresh adds intensity. Pairs well with calamansi."),
    ]
    y = d.two_col_cards(y, zero_na, size=8.5)

    y -= 6
    y = d.subheading(y, "When to call your nephrologist — sodium red flags")
    y = d.bullets(y, [
        "Blood pressure consistently > 140/90 mmHg despite medication — sodium load may be undermining the drugs.",
        "Sudden weight gain of > 2 kg in 1–2 days — sodium-driven fluid retention.",
        "Swelling (edema) of the feet, ankles, or face worsening week over week.",
        "Urine output noticeably decreasing — sodium restriction + diuretics need re-titration.",
        "Potassium level > 5.5 mEq/L — check for hidden potassium chloride in the diet.",
    ], size=9.5)

    # Doctor card
    y -= 10
    y = d.ensure_space(y, 92)
    c.setFillColor(NAVY)
    c.roundRect(M, y - 82, CW, 82, 8, stroke=0, fill=1)
    c.setFillColor(WHITE); c.setFont("DJV-B", 12)
    c.drawString(M + 14, y - 18, "W. G. M. Rivero, MD, FPCP, DPSN")
    c.setFont("DJV", 9); c.setFillColor(HexColor("#c8e8ea"))
    c.drawString(M + 14, y - 32, "Internal Medicine · Nephrology · Clinical Nutrition")
    c.setFont("DJV", 9); c.setFillColor(HexColor("#d0dce8"))
    for i, line in enumerate([
        "Practicing integrative, evidence-based nephrology",
        "across Quezon City, Pampanga, and Bulacan.",
        "Book: seriousmd.com/doc/williamrivero",
        "Website: williamriveromd.com",
    ]):
        c.drawString(M + 14, y - 46 - i * 11, line)
    y -= 92

    # References
    y -= 4
    y = d.ensure_space(y, 20)
    c.setFont("DJV-I", 7); c.setFillColor(MUTED)
    refs = ("References: KDIGO 2024 CKD Guideline · WHO Sodium Intake Guideline 2012 · "
            "PURE Study, NEJM 2014 · He & MacGregor, Cochrane 2013 · "
            "Philippine FNRI Food Composition Tables.")
    for ln in d.wrap(refs, "DJV-I", 7, CW):
        y = d.ensure_space(y, 10)
        c.drawString(M, y, ln)
        y -= 9

    y -= 6
    # Disclaimer
    disc_lines = d.wrap(
        "MEDICAL DISCLAIMER — This handout is patient education material produced by "
        "W. G. M. Rivero, MD for general information only. It does not replace the advice "
        "of your own physician or dietitian. Sodium targets, dietary restrictions, and "
        "medication interactions vary by individual; always follow your nephrologist's "
        "specific instructions. Do not use potassium-based salt substitutes without "
        "explicit approval from your doctor.",
        "DJV", 7.5, CW - 16)
    dh = 10 * 2 + len(disc_lines) * 9.5
    y = d.ensure_space(y, dh + 4)
    c.setFillColor(AMBER_SOFT)
    c.setStrokeColor(HexColor("#d97706")); c.setLineWidth(1)
    c.roundRect(M, y - dh, CW, dh, 6, stroke=1, fill=1)
    ty = y - 10 - 7.5 + 1
    c.setFillColor(AMBER)
    for ln in disc_lines:
        c.drawString(M + 8, ty, ln)
        ty -= 9.5

    d.footer()
    c.save()
    print(f"Saved → {OUT}")


if __name__ == "__main__":
    build()
