# Cartoon explainers (Nov 28 2026)

Short animated explainers for Academy pages, made in the sandbox: an original cartoon guide (nurse in teal scrubs)
whose mouth follows the voice, drawn on a canvas (`anim.html`, `render(frame)`), voiced with Piper "Lessac"
(en-us-lessac-medium, from the rhasspy/piper v0.0.2 GitHub release; Hugging Face is blocked in the sandbox).

Per explainer folder: `script.txt` (one line per scene), `timeline.json` (scene frame counts, speech length,
per-frame mouth amplitude), `anim.html` (scenes), `render.py` (Playwright frames -> one MP4 per scene).
Pipeline: Piper each line -> pad 0.5 s / 0.8 s -> timeline.json -> render.py -> concat -> add voice (AAC)
-> watermark "© renalcarematters.com" (drawtext, top right) -> `videos/academy/<name>.mp4` + poster `.jpg`.
Pages show them in a `details.rl-xpl` ("Watch the 1-minute explainer", preload none, transcript).
Clinical lines need Dr. Rivero's check.

Per-explainer voices: Lessac (female guide) for megacode, med-scheduler, interaction-checker, calculo; Ryan high (male guide, `head.js` in `paratus/`) for paratus. `tl.py` builds `timeline.json` + `voice.wav` from `s1..sN.wav`; `render.py [scene ...]` re-renders only the listed scenes.
