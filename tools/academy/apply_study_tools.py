#!/usr/bin/env python3
"""Put a "Study tools in every module" section on the Academy landing page (academy/index.html).

Dr. Rivero (Nov 27 2026): learners need instructions on the landing page for the tools inside the modules: the reader
(Listen, Figure slideshow), highlights and notes, bookmarks, resume, offline use (Schola) and printing.

The section sits between "Ways to use the Academy" (#use) and "Tracks" (#tracks), between STUDY-TOOLS markers, with a
"Study tools" nav pill after "Ways to use it". Idempotent: the block is replaced on every run. publish_academy.py runs it.
"""
import re, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PAGE = ROOT / "academy" / "index.html"
START, END = "<!-- STUDY-TOOLS-START -->", "<!-- STUDY-TOOLS-END -->"
PILL = '<a class="nav-pill" href="#tools">Study tools</a>'

CARDS = [
    ("Listen to a module",
     "Tap <strong>Listen to this module</strong> under the module title. A player opens at the bottom of the screen and reads "
     "the module aloud, highlighting the sentence it is reading. Use the buttons to go to the previous or next "
     "section, change the speed, choose the voice, or close it. Hover over a button, or tap it, to see what it does. "
     "Come back later and tap <strong>Resume listening</strong> to continue where you stopped, or <strong>Start from the "
     "beginning</strong>."),
    ("Choose a voice",
     "Two natural voices are offered, Lessac (female) and Ryan (male). The first time, the site asks to download one "
     "(about 90 MB, once; use Wi-Fi). After that it works without a signal. Tap Cancel to use your device's built-in "
     "voice instead."),
    ("Figures while listening",
     "When the reader reaches a figure, it reads the description, opens the image full screen for 10 seconds, then "
     "reads on. To skip the pictures, tap the picture button in the player to turn this off."),
    ("Figure slideshow",
     "Tap <strong>Figure slideshow</strong> under the module title to step through just the figures: each description is read "
     "aloud and each image is shown for 10 seconds. A quick visual review before a quiz or a shift."),
    ("Highlights and notes",
     "Select any text, then pick a highlight color or tap <strong>Note</strong> to write your own. The orange pen button at the "
     "bottom left lists everything you marked in the module, and lets you export, print or back up your notes."),
    ("Bookmarks",
     "Tap the ribbon beside a section title to bookmark it. Your bookmarks are listed under the orange pen button, "
     "with your notes."),
    ("Pick up where you left off",
     "Each module remembers how far you read. Reopen it and tap <strong>Pick up where you left off</strong>. On this page, and "
     "on each track page, <strong>Continue</strong> takes you back to the last module you were reading."),
    ("Study offline with Schola",
     "Schola is the Academy as an app. Open the <a href=\"#schola\">Schola</a> tab on the left edge of this page (on a "
     "phone, the book button above the orange pen) to install it and save one track, or all of them, for reading with no signal. On an iPhone or iPad, add Schola to "
     "the Home Screen first, then save tracks from inside the app."),
    ("Light, Dim, Dark and E-paper",
     "The round button at the bottom right changes how the page looks. Each tap moves to the next setting: "
     "<strong>Auto</strong>, <strong>Light</strong>, <strong>Dim</strong> (soft charcoal for evening reading), "
     "<strong>Dark</strong> (for night or a dark room) and <strong>E-paper</strong> (muted colors and no animation, "
     "for e-ink readers, bright sun or eyes that tire easily). Auto follows your device's dark setting, or else the "
     "time of day: Light by day, Dim in the evening, Dark late at night. Your choice is remembered on every page."),
    ("Print a module",
     "Open the orange pen button and tap <strong>Print this module</strong> (or <strong>Print my notes</strong>). In the installed Schola "
     "app, use <strong>Print</strong> in the bottom bar."),
]

SAFETY = ("<b>Listening while driving?</b> Start the module and choose the voice before you set off; the player keeps "
          "going from section to section without a tap. On an iPhone or iPad the natural voice keeps reading with the "
          "screen locked. The self-assessment quiz at the end needs the screen, so do it when it is safe.")
PRIVACY = ("Your notes, highlights, bookmarks, reading place and saved tracks stay on your own device. There is no "
           "account and nothing is sent anywhere. They do not move to another phone or computer; use <b>Back up "
           "all</b> under the orange pen button to keep a copy.")


def block():
    cards = "\n".join(f'<div class="tc-card"><b>{t}</b>{d}</div>' for t, d in CARDS)
    return f"""{START}
<section class="section" id="tools">
  <div class="section-tag">Study tools</div>
  <h2>Study tools in every module</h2>
  <p>Every module has the same tools for reading, listening and studying. Here is what each one does and where to find it.</p>
<div class="tc-viz" role="group" aria-label="Study tools in every module"><p class="tc-viz-title">The tools at a glance</p><div class="tc-cards tc-two">
{cards}
</div></div>
<div class="alert alert-amber"><div class="alert-icon">🚗</div><div class="alert-body"><p>{SAFETY}</p></div></div>
<p>{PRIVACY}</p>
</section>
{END}"""


def main():
    s = PAGE.read_text(encoding="utf-8")
    t = re.sub(re.escape(START) + r".*?" + re.escape(END) + r"\n?", "", s, flags=re.S)
    anchor = '<section class="section" id="tracks">'
    if anchor not in t:
        print("apply_study_tools: #tracks section not found; nothing done", file=sys.stderr)
        return
    t = t.replace(anchor, block() + "\n" + anchor, 1)
    if PILL not in t:
        t = t.replace('<a class="nav-pill" href="#use">Ways to use it</a>',
                      '<a class="nav-pill" href="#use">Ways to use it</a>\n' + PILL, 1)
    if t != s:
        PAGE.write_text(t, encoding="utf-8")
        print("apply_study_tools: Study tools section written to academy/index.html")
    else:
        print("apply_study_tools: up to date")


if __name__ == "__main__":
    main()
