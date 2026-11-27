// GET  /api/certs            -> { ready: true, turnstile: <site key or null> }  (503 when the database is not bound)
// GET  /api/certs?c=<code>   -> the certificate record for /verify (404 when unknown)
// POST /api/certs            -> register a certificate: {name, track, exam, modules, score, total, exam_min, study_min,
//                               turnstile, website (honeypot)} -> { code, issued }
import { db, json, hashIp, clean, turnstileOk, PASS, manilaDate, newCode, publicRecord } from "../../functions-lib/certs.js";

const CODE_RE = /^RCA-[A-Z]{1,4}-\d{6}-[0-9A-F]{8}$/;

export async function onRequestGet({ request, env }) {
  const d = await db(env);
  if (!d) return json({ error: "not_configured" }, 503);
  const c = (new URL(request.url).searchParams.get("c") || "").trim().toUpperCase();
  if (!c) return json({ ready: true, turnstile: env.TURNSTILE_SITE_KEY || null });
  if (!CODE_RE.test(c)) return json({ error: "not_found" }, 404);
  const r = await d.prepare("SELECT * FROM certificates WHERE code=?").bind(c).first();
  if (!r) return json({ error: "not_found" }, 404);
  return json(publicRecord(r));
}

function int(v, lo, hi) {
  const n = Number(v);
  return Number.isInteger(n) && n >= lo && n <= hi ? n : null;
}

export async function onRequestPost({ request, env }) {
  const d = await db(env);
  if (!d) return json({ error: "not_configured" }, 503);
  let b;
  try { b = await request.json(); } catch (e) { return json({ error: "bad_request" }, 400); }
  if (b.website) return json({ error: "bad_request" }, 400);                 // honeypot
  const name = clean(b.name, 70).replace(/\s+/g, " ");
  const track = clean(b.track, 120).replace(/\s+/g, " ");
  const exam = clean(b.exam, 120);
  if (name.length < 2 || !track || !/^[a-z0-9-]+-final-exam$/.test(exam)) return json({ error: "bad_request" }, 400);
  if (/https?:\/\/|www\.|[<>]/i.test(name + track)) return json({ error: "bad_request" }, 400);
  const score = int(b.score, 0, 500), total = int(b.total, 1, 500);
  if (score == null || total == null || score > total || score / total < PASS) return json({ error: "not_passed" }, 400);
  const modules = int(b.modules, 0, 200), modulesPassed = int(b.modules_passed, 0, 200), activeMin = int(b.active_min, 0, 100000), examMin = int(b.exam_min, 0, 1440), studyMin = int(b.study_min, 0, 100000);
  if (modules && (modulesPassed == null || modulesPassed < modules)) return json({ error: "modules" }, 400);
  const ts = await turnstileOk(request, env, b.turnstile);
  if (!ts.ok) return json({ error: "human_check", codes: ts.codes }, 403);
  const iph = await hashIp(request, env);
  const recent = await d.prepare("SELECT COUNT(*) AS n FROM certificates WHERE iph=? AND created > datetime('now','-1 day')").bind(iph).first();
  if (recent && recent.n >= 10) return json({ error: "limit" }, 429);
  // Same person, same track, same day and result: hand back the existing code instead of a new one.
  const issued = manilaDate();
  const same = await d.prepare("SELECT code FROM certificates WHERE name=? AND exam=? AND issued=? AND score=? AND total=? AND status='valid'")
    .bind(name, exam, issued, score, total).first();
  if (same) return json({ code: same.code, issued });
  for (let i = 0; i < 4; i++) {
    const code = newCode(track, issued);
    try {
      await d.prepare(`INSERT INTO certificates (code, created, issued, name, track, exam, modules, modules_passed, active_min, score, total, exam_min, study_min, status, iph)
          VALUES (?, datetime('now'), ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, 'valid', ?)`)
        .bind(code, issued, name, track, exam, modules, modulesPassed, activeMin, score, total, examMin, studyMin, iph).run();
      return json({ code, issued });
    } catch (e) { /* code collision: try another */ }
  }
  return json({ error: "server" }, 500);
}
