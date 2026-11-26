/* academy-piper-worker.js — "Natural voice" engine for the Academy Listen player (Nov 26 2026, Dr. Rivero).
 *
 * Piper text-to-speech (MIT, rhasspy/piper) running entirely on the learner's device, in this Web Worker so the page
 * stays smooth. The voice model is downloaded once and kept in the browser's Cache Storage ("rcm-piper-v1"); after that
 * it works without a signal. Unlike the vits-web library, the model is loaded into ONNX Runtime ONCE and the espeak-ng
 * phonemizer module is created once, so each sentence costs only one inference.
 *
 * Messages in:  {type:"init", cfg:{ortUrl, ortWasmBase, phonemizeBase, model, config}}  -> progress..., ready | error
 *               {type:"synth", id, text}                                               -> audio {id, pcm, rate} | error
 *               {type:"drop"} (forget a voice: delete it from Cache Storage)            -> dropped
 * Source file: edit this, then run tools/academy/apply_listen.py (writes academy-piper-worker.<hash>.js).
 */
"use strict";
var CACHE = "rcm-piper-v1";
var session = null, phon = null, cfgJson = null, lines = null, ready = null, ort = null, queue = null;

function post(m, t) { self.postMessage(m, t || []); }

async function fetchCached(url, label) {
  var cache = await caches.open(CACHE);
  var hit = await cache.match(url);
  if (hit) return hit.arrayBuffer();
  var res = await fetch(url, { mode: "cors" });
  if (!res.ok) throw new Error("Download failed (" + res.status + ") for " + label);
  var total = +(res.headers.get("Content-Length") || 0), got = 0, parts = [];
  var reader = res.body && res.body.getReader();
  if (!reader) { var b = await res.arrayBuffer(); await cache.put(url, new Response(b)); return b; }
  for (;;) {
    var r = await reader.read();
    if (r.done) break;
    parts.push(r.value); got += r.value.length;
    post({ type: "progress", label: label, loaded: got, total: total });
  }
  var blob = new Blob(parts);
  await cache.put(url, new Response(blob, { headers: { "Content-Type": "application/octet-stream" } }));
  return blob.arrayBuffer();
}

async function init(cfg) {
  importScripts(cfg.ortUrl, cfg.phonemizeBase + ".js");
  ort = self.ort;
  ort.env.wasm.numThreads = 1;                       // pages are not cross-origin isolated: single-threaded WASM
  ort.env.wasm.wasmPaths = cfg.ortWasmBase;
  var cbuf = await fetchCached(cfg.config, "voice settings");
  cfgJson = JSON.parse(new TextDecoder().decode(cbuf));
  var mbuf = await fetchCached(cfg.model, "voice");
  post({ type: "progress", label: "preparing", loaded: 1, total: 1 });
  session = await ort.InferenceSession.create(new Uint8Array(mbuf), { executionProviders: ["wasm"], graphOptimizationLevel: "all" });
  phon = await self.createPiperPhonemize({
    print: function (line) { if (lines) { try { lines.push(JSON.parse(line).phoneme_ids); } catch (e) {} } },
    printErr: function () {},
    locateFile: function (f) { return f.endsWith(".wasm") ? cfg.phonemizeBase + ".wasm" : f.endsWith(".data") ? cfg.phonemizeBase + ".data" : f; },
    noInitialRun: true
  });
}

function phonemize(text) {
  lines = [];
  phon.callMain(["-l", cfgJson.espeak.voice, "--input", JSON.stringify([{ text: text }]), "--espeak_data", "/espeak-ng-data"]);
  var out = lines; lines = null;
  return out;
}

async function synth(text) {
  var idsList = phonemize(text), inf = cfgJson.inference, chunks = [], total = 0;
  var gap = Math.round(cfgJson.audio.sample_rate * 0.12);           // short pause between sentences espeak split
  for (var k = 0; k < idsList.length; k++) {
    var ids = idsList[k];
    if (!ids || !ids.length) continue;
    var feeds = {
      input: new ort.Tensor("int64", BigInt64Array.from(ids.map(BigInt)), [1, ids.length]),
      input_lengths: new ort.Tensor("int64", BigInt64Array.from([BigInt(ids.length)]), [1]),
      scales: new ort.Tensor("float32", Float32Array.from([inf.noise_scale, inf.length_scale, inf.noise_w]), [3])
    };
    if (cfgJson.num_speakers > 1) feeds.sid = new ort.Tensor("int64", BigInt64Array.from([0n]), [1]);
    var out = await session.run(feeds);
    var data = out.output.data;
    chunks.push(data); total += data.length + (k ? gap : 0);
  }
  var pcm = new Float32Array(total), at = 0;
  chunks.forEach(function (c, i) { if (i) at += gap; pcm.set(c, at); at += c.length; });
  return pcm;
}

self.onmessage = function (e) {
  var m = e.data || {};
  if (m.type === "init") {
    ready = ready || init(m.cfg);
    ready.then(function () { post({ type: "ready", rate: cfgJson.audio.sample_rate }); },
               function (err) { ready = null; post({ type: "error", stage: "init", message: String(err && err.message || err) }); });
  } else if (m.type === "synth") {
    // one inference at a time on the single session; a failed sentence does not block the ones queued after it
    var job = (queue || Promise.resolve()).catch(function () {})
      .then(function () { return ready || Promise.reject(new Error("not ready")); })
      .then(function () { return synth(m.text); });
    queue = job;
    job.then(function (pcm) { post({ type: "audio", id: m.id, pcm: pcm, rate: cfgJson.audio.sample_rate }, [pcm.buffer]); },
             function (err) { post({ type: "error", stage: "synth", id: m.id, message: String(err && err.message || err) }); });
  } else if (m.type === "drop") {
    caches.delete(CACHE).then(function () { post({ type: "dropped" }); });
  }
};
