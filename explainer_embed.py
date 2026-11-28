#!/usr/bin/env python3
"""Cartoon explainer embed: a small thumbnail card that opens a VIDEO LIGHTBOX (Nov 28 2026, Dr. Rivero:
"display a small-sized thumbnail which zooms in when touched and plays full width ... like the lightbox for images").

One source for every embedded explainer (Drug Index, Med Scheduler, Interaction Checker, Calculo, Paratus,
Megacode shared monitor). The card is a div, not a <figure>, so the image lightbox and the side rail's
Graphics gallery (both take every 'figure img') leave its thumbnail alone. Used by generate_drug_pages.py, build_calc_app.py and tools/academy/apply_resus_lab.py;
the Megacode card is written by assets/academy-resus-lab.js with the same markup (keep them in step).

    card(name)   -> the thumbnail card HTML (no CSS / JS)
    ASSETS       -> <style id="xpl-css"> + <script id="xpl-js">, once per page (the script is guarded and uses
                    event delegation, so a card added later by another script works too)
    embed(name)  -> ASSETS + card(name)

Card: the poster with a play button and the length, the title, "Cartoon explainer", Share (the watch page
/watch/<name>, never the video file) and a folded transcript. Its size is set by the inline CSS, so nothing
shifts when the script loads. The thumbnail is a link to /watch/<name>: without JavaScript it opens the watch page.
Tap: the dark lightbox of the image viewer (assets/image-lightbox.js look: rgba(0,0,0,.93), round x top right),
the video zooming out of the thumbnail and playing full width (100% of the screen width on phones, up to 1280 px),
with the title and Share under it. Close: x, a tap outside the video, Esc or the Back button (history state).
Closing stops the video and unloads it.
Dark mode uses [data-theme~="dark"] on purpose: build_theme_dim.py collects every [data-theme="dark"] rule site-wide,
and a new one would re-date the Dim CSS on every page; these card colors suit Dim as they are. Player: no download menu, no playback-rate menu, no picture-in-picture.
"""
import html
from pathlib import Path

REPO = Path(__file__).resolve().parent

# name -> (video path, title, length label, length m:ss, accent, accent in dark mode)
VIDEOS = {
    "drug-index": ("/videos/dosis/drug-index-explainer.mp4", "Meet the Drug Index and Dosis", "1 min 26 s", "1:26", "#0e4a50", "#8fd3d8"),
    "med-scheduler": ("/videos/dosis/med-scheduler-explainer.mp4", "How the Med Scheduler works", "1 min 18 s", "1:18", "#0e4a50", "#8fd3d8"),
    "interaction-checker": ("/videos/dosis/interaction-checker-explainer.mp4", "How the Interaction Checker works", "1 min 13 s", "1:13", "#0e4a50", "#8fd3d8"),
    "calculo": ("/videos/calculo/calculo-explainer.mp4", "Meet Calculo", "1 min 13 s", "1:13", "#312e81", "#c7d2fe"),
    "paratus": ("/videos/paratus/paratus-explainer.mp4", "Meet Paratus", "1 min 23 s", "1:23", "#0e4a50", "#8fd3d8"),
    "megacode-shared-monitor": ("/videos/academy/megacode-shared-monitor-explainer.mp4", "The shared monitor display", "59 s", "0:59", "#0e4a50", "#8fd3d8"),
}

SHARE_SVG = ('<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/>'
             '<circle cx="18" cy="19" r="3"/><path d="M8.6 13.5l6.8 4M15.4 6.5l-6.8 4"/></svg>')
PLAY_SVG = '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M8 5.5v13l11-6.5z"/></svg>'

CSS = """<style id="xpl-css">
.xpl{--xpl-bg:#fff;--xpl-bd:#d9e1ea;--xpl-tx:#475569;display:grid;grid-template-columns:auto minmax(0,1fr);column-gap:14px;align-items:center;margin:16px 0 0;max-width:540px;padding:10px;border:1px solid var(--xpl-bd);border-radius:14px;background:var(--xpl-bg);box-shadow:0 4px 14px rgba(15,30,51,.07);box-sizing:border-box;text-align:left;}
.xpl-thumb{position:relative;display:block;width:176px;aspect-ratio:16/9;border-radius:9px;overflow:hidden;background:#0b1220;cursor:zoom-in;}
.xpl-thumb img{display:block;width:100%;height:100%;object-fit:cover;transition:transform .25s ease;}
.xpl-thumb:hover img,.xpl-thumb:focus-visible img{transform:scale(1.05);}
.xpl-thumb:focus-visible{outline:3px solid #b8860b;outline-offset:2px;}
.xpl-play{position:absolute;left:50%;top:50%;width:42px;height:42px;margin:-21px 0 0 -21px;border-radius:50%;background:var(--xpl-ac);box-shadow:0 4px 14px rgba(0,0,0,.35);display:flex;align-items:center;justify-content:center;transition:transform .2s ease;}
.xpl-thumb:hover .xpl-play{transform:scale(1.1);}
.xpl-play svg{width:20px;height:20px;fill:#fff;margin-left:2px;}
.xpl-dur{position:absolute;right:6px;bottom:6px;font:700 11px/1 Inter,system-ui,sans-serif;color:#fff;background:rgba(0,0,0,.72);border-radius:5px;padding:3px 6px;}
.xpl .xpl-cap{min-width:0;display:flex;flex-direction:column;align-items:flex-start;gap:3px;margin:0;padding:0;text-align:left;font-size:inherit;color:inherit;}
.xpl-t{font:700 15.5px/1.3 Inter,system-ui,sans-serif;color:var(--xpl-ac);}
.xpl-s{font:500 13px/1.35 Manrope,system-ui,sans-serif;color:var(--xpl-tx);}
.xpl-acts{display:flex;flex-wrap:wrap;align-items:center;gap:8px;margin-top:5px;}
.xpl-share{display:inline-flex;align-items:center;gap:6px;font:700 12.5px/1 Inter,system-ui,sans-serif;color:#fff;background:var(--xpl-ac);border:0;border-radius:999px;padding:7px 12px;cursor:pointer;}
.xpl-share svg{width:14px;height:14px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;}
.xpl-share:hover{filter:brightness(1.15);}
.xpl .xpl-tr{grid-column:1/-1;margin:8px 0 0;text-align:left;} .xpl-tr summary{cursor:pointer;font:600 13px Inter,system-ui,sans-serif;color:var(--xpl-tx);}
.xpl-tr p{font-size:14px;line-height:1.6;color:var(--xpl-tx);margin:8px 0 2px;text-align:left;}
html[data-theme~="dark"] .xpl{--xpl-bg:#161d2b;--xpl-bd:#2b3647;--xpl-tx:#c3ccd9;box-shadow:none;}
html[data-theme~="dark"] .xpl-t{color:var(--xpl-ac-d);}
@media (max-width:520px){.xpl{column-gap:12px;padding:8px;}.xpl-thumb{width:132px;}.xpl-play{width:36px;height:36px;margin:-18px 0 0 -18px;}.xpl-t{font-size:14.5px;}}
@media print{.xpl{display:none!important;}}
#vid-lb{display:none;position:fixed;inset:0;z-index:100050;background:rgba(0,0,0,.93);flex-direction:column;align-items:center;justify-content:center;padding:20px 16px 16px;box-sizing:border-box;cursor:pointer;opacity:0;transition:opacity .22s ease;}
#vid-lb.open{display:flex;} #vid-lb.shown{opacity:1;}
#vid-lb .vlb-body{width:min(95vw,1280px,calc((100vh - 190px) * 16 / 9));cursor:default;transform-origin:0 0;}
#vid-lb video{display:block;width:100%;height:auto;aspect-ratio:16/9;background:#000;border-radius:8px;box-shadow:0 8px 48px rgba(0,0,0,.7);}
#vid-lb .vlb-cap{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-top:0;padding:12px 16px;background:rgba(255,255,255,.07);border:1px solid rgba(255,255,255,.13);border-top:none;border-radius:0 0 8px 8px;}
#vid-lb .vlb-t{flex:1 1 200px;color:rgba(255,255,255,.92);font:700 15px/1.3 Inter,system-ui,sans-serif;}
#vid-lb .vlb-share{display:inline-flex;align-items:center;gap:6px;font:700 13px/1 Inter,system-ui,sans-serif;color:#fff;background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.3);border-radius:999px;padding:8px 14px;cursor:pointer;}
#vid-lb .vlb-share:hover{background:rgba(255,255,255,.26);} #vid-lb .vlb-share svg{width:15px;height:15px;fill:none;stroke:currentColor;stroke-width:2.2;stroke-linecap:round;stroke-linejoin:round;}
#vid-lb .vlb-close{position:fixed;top:16px;right:20px;z-index:100051;width:40px;height:40px;display:flex;align-items:center;justify-content:center;color:#fff;font-size:24px;line-height:1;background:rgba(255,255,255,.13);border:1px solid rgba(255,255,255,.25);border-radius:50%;cursor:pointer;}
#vid-lb .vlb-close:hover{background:rgba(255,255,255,.28);}
#vid-lb .vlb-hint{margin:14px 0 0;color:rgba(255,255,255,.4);font:500 11px Inter,system-ui,sans-serif;text-align:center;letter-spacing:.02em;pointer-events:none;}
@media (max-width:600px){#vid-lb{padding:64px 0 12px;justify-content:center;}#vid-lb .vlb-body{width:100vw;}#vid-lb video{border-radius:0;}#vid-lb .vlb-cap{border-radius:0;border-left:0;border-right:0;}}
@media (max-height:500px) and (orientation:landscape){#vid-lb{padding:0;}#vid-lb .vlb-body{width:min(100vw,calc(100vh * 16 / 9));}#vid-lb video{border-radius:0;max-height:100vh;}#vid-lb .vlb-cap,#vid-lb .vlb-hint{display:none;}#vid-lb .vlb-close{top:8px;right:8px;}}
@media (prefers-reduced-motion:reduce){#vid-lb{transition:none;}.xpl-thumb img,.xpl-play{transition:none;}}
@media print{#vid-lb{display:none!important;}}
html.vlb-lock,html.vlb-lock body{overflow:hidden!important;}
</style>"""

JS = r"""<script id="xpl-js">(function(){if(window.__rcmXpl)return;window.__rcmXpl=1;
var SITE='https://renalcarematters.com',lb,vid,ttl,shareBtn,from=null,pushed=false,reduce=matchMedia('(prefers-reduced-motion: reduce)').matches;
function share(path,btn,title){var u=SITE+path,l=btn.querySelector('span');
 function done(m){if(!l)return;l.textContent=m;setTimeout(function(){l.textContent='Share';},2200);}
 if(navigator.share){navigator.share({title:title||document.title,url:u}).catch(function(){});return;}
 if(navigator.clipboard)navigator.clipboard.writeText(u).then(function(){done('Link copied');},function(){prompt('Copy this link',u);});else prompt('Copy this link',u);}
function build(){lb=document.createElement('div');lb.id='vid-lb';lb.setAttribute('role','dialog');lb.setAttribute('aria-modal','true');lb.setAttribute('aria-label','Video player');
 lb.innerHTML='<button type="button" class="vlb-close" aria-label="Close the video">×</button><div class="vlb-body"><video controls playsinline preload="auto" controlslist="nodownload noplaybackrate" disablepictureinpicture></video>'+
 '<div class="vlb-cap"><span class="vlb-t"></span><button type="button" class="vlb-share">__SHARE__<span>Share</span></button></div></div><p class="vlb-hint">Tap outside the video, press Esc or go back to close</p>';
 document.body.appendChild(lb);vid=lb.querySelector('video');ttl=lb.querySelector('.vlb-t');shareBtn=lb.querySelector('.vlb-share');
 vid.addEventListener('contextmenu',function(e){e.preventDefault();});
 lb.querySelector('.vlb-close').addEventListener('click',function(e){e.stopPropagation();close();});
 lb.addEventListener('click',function(e){if(e.target===lb||e.target.classList.contains('vlb-hint'))close();});
 shareBtn.addEventListener('click',function(){share(shareBtn.getAttribute('data-path'),shareBtn,ttl.textContent);});}
function open(a){if(!lb)build();from=a;
 ttl.textContent=a.getAttribute('data-xpl-title')||'';shareBtn.setAttribute('data-path',a.getAttribute('href'));
 vid.setAttribute('poster',(a.querySelector('img')||{}).currentSrc||a.querySelector('img').getAttribute('src'));vid.src=a.getAttribute('data-xpl-src');
 document.documentElement.classList.add('vlb-lock');lb.classList.add('open');
 var p=vid.play();if(p&&p.catch)p.catch(function(){});
 var body=lb.querySelector('.vlb-body');
 if(!reduce){var r=a.getBoundingClientRect(),b=body.getBoundingClientRect(),k=r.width/Math.max(1,b.width);
  body.style.transition='none';body.style.transform='translate('+(r.left-b.left)+'px,'+(r.top-b.top)+'px) scale('+k+')';body.getBoundingClientRect();
  body.style.transition='transform .32s cubic-bezier(.2,.8,.2,1)';body.style.transform='none';}
 requestAnimationFrame(function(){lb.classList.add('shown');});
 lb.querySelector('.vlb-close').focus({preventScroll:true});
 try{history.pushState({vlb:1},'',location.href);pushed=true;}catch(e){pushed=false;}}
function close(fromPop){if(!lb||!lb.classList.contains('open'))return;
 try{vid.pause();}catch(e){}vid.removeAttribute('src');try{vid.load();}catch(e){}
 lb.classList.remove('shown','open');document.documentElement.classList.remove('vlb-lock');
 var body=lb.querySelector('.vlb-body');body.style.transition='none';body.style.transform='none';
 if(from)try{from.focus({preventScroll:true});}catch(e){}
 if(pushed&&!fromPop){pushed=false;try{history.back();}catch(e){}}pushed=false;}
document.addEventListener('click',function(e){var a=e.target.closest&&e.target.closest('.xpl-thumb');
 if(a){if(e.button||e.ctrlKey||e.metaKey||e.shiftKey||e.altKey)return;e.preventDefault();open(a);return;}
 var s=e.target.closest&&e.target.closest('.xpl-share');if(s){var f=s.closest('.xpl'),t=f&&f.querySelector('.xpl-thumb');if(t)share(t.getAttribute('href'),s,t.getAttribute('data-xpl-title'));}});
document.addEventListener('keydown',function(e){if(e.key==='Escape'&&lb&&lb.classList.contains('open'))close();});
window.addEventListener('popstate',function(){if(lb&&lb.classList.contains('open'))close(true);});
})();</script>""".replace("__SHARE__", SHARE_SVG)

ASSETS = CSS + "\n" + JS


def transcript(name: str) -> str:
    sp = REPO / "tools" / "academy" / "explainers" / name / "script.txt"
    return html.escape(" ".join(sp.read_text(encoding="utf-8").split())) if sp.exists() else ""


def card(name: str, el_id: str = "explainer") -> str:
    src, title, dur_label, dur, ac, ac_d = VIDEOS[name]
    poster = src[:-4] + ".jpg"
    tr = transcript(name)
    return (f'<div class="xpl" id="{el_id}" role="group" aria-label="Video: {html.escape(title)}" style="--xpl-ac:{ac};--xpl-ac-d:{ac_d}">'
            f'<a class="xpl-thumb" href="/watch/{name}" data-xpl-src="{src}" data-xpl-title="{html.escape(title)}" '
            f'aria-label="Play the video: {html.escape(title)}, {dur_label}">'
            f'<img src="{poster}" alt="" width="1280" height="720" decoding="async" fetchpriority="low">'
            f'<span class="xpl-play" aria-hidden="true">{PLAY_SVG}</span><span class="xpl-dur" aria-hidden="true">{dur}</span></a>'
            f'<div class="xpl-cap"><span class="xpl-t">{html.escape(title)}</span>'
            f'<span class="xpl-s">Cartoon explainer &middot; {dur_label}</span>'
            f'<span class="xpl-acts"><button type="button" class="xpl-share" aria-label="Share this explainer video">{SHARE_SVG}<span>Share</span></button></span></div>'
            + (f'<details class="xpl-tr"><summary>Read the transcript</summary><p>{tr}</p></details>' if tr else "")
            + "</div>")


def embed(name: str, el_id: str = "explainer") -> str:
    return ASSETS + "\n" + card(name, el_id)


if __name__ == "__main__":
    print(embed("drug-index"))
