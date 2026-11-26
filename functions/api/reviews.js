// GET  /api/reviews  -> public summary of APPROVED ratings: average, count, distribution, approved comments
// POST /api/reviews  -> submit a rating (1-5) with an optional comment, name and role; held for approval
import { db, json, hashIp, clean, ROLES, turnstileOk, COUNTED, ASPECTS, FEATURES } from "../../functions-lib/reviews.js";

export async function onRequestGet({ env }) {
  const d = await db(env);
  if (!d) return json({ error: "not_configured" }, 503);
  const agg = await d.prepare(`SELECT stars, COUNT(*) AS n FROM reviews WHERE ${COUNTED} GROUP BY stars`).all();
  const dist = [0, 0, 0, 0, 0];
  let count = 0, sum = 0;
  for (const r of agg.results || []) { dist[r.stars - 1] = r.n; count += r.n; sum += r.n * r.stars; }
  const asp = await d.prepare(`SELECT ${ASPECTS.map((k) => `AVG(${k}) AS ${k}, COUNT(${k}) AS n_${k}`).join(", ")} FROM reviews WHERE ${COUNTED}`).first() || {};
  const aspects = {};
  for (const k of ASPECTS) aspects[k] = { average: asp[k] == null ? null : Math.round(asp[k] * 10) / 10, count: asp["n_" + k] || 0 };
  const featRows = await d.prepare(`SELECT features FROM reviews WHERE ${COUNTED} AND features IS NOT NULL`).all();
  const features = {};
  for (const r of featRows.results || []) for (const f of String(r.features).split(",")) if (FEATURES.includes(f)) features[f] = (features[f] || 0) + 1;
  const rows = await d.prepare(
    "SELECT stars, comment, name, role, substr(created,1,10) AS date FROM reviews WHERE status='approved' AND comment IS NOT NULL ORDER BY id DESC LIMIT 60"
  ).all();
  return json({
    count,
    average: count ? Math.round((sum / count) * 10) / 10 : null,
    distribution: dist,
    aspects,
    features,
    turnstile: env.TURNSTILE_SITE_KEY || null,
    comments: (rows.results || []).map((r) => ({ stars: r.stars, text: r.comment, name: r.name || "", role: r.role || "", date: r.date })),
  }, 200, { "cache-control": "public, max-age=60" });
}

export async function onRequestPost({ request, env }) {
  const d = await db(env);
  if (!d) return json({ error: "not_configured" }, 503);
  let body;
  try { body = await request.json(); } catch (e) { return json({ error: "bad_request" }, 400); }
  if (body.website) return json({ ok: true });                       // honeypot: quietly ignore bots
  if (typeof body.elapsed === "number" && body.elapsed < 2500) return json({ error: "too_fast" }, 429);
  const stars = Number(body.stars);
  if (!Number.isInteger(stars) || stars < 1 || stars > 5) return json({ error: "stars" }, 400);
  const comment = clean(body.comment, 1000);
  const name = clean(body.name, 60).replace(/\n/g, " ");
  const role = ROLES.includes(body.role) ? body.role : "";
  const page = clean(body.page, 200);
  const improve = clean(body.improve, 1000);
  const asp = {};
  for (const k of ASPECTS) {
    const v = body.aspects && body.aspects[k] != null ? Number(body.aspects[k]) : null;
    if (v != null && !(Number.isInteger(v) && v >= 1 && v <= 5)) return json({ error: "aspects" }, 400);
    asp[k] = v;
  }
  const feats = (Array.isArray(body.features) ? body.features : []).filter((f) => FEATURES.includes(f));
  const features = [...new Set(feats)].slice(0, 3).join(",");
  if (/https?:\/\/|www\./i.test(comment + " " + name + " " + improve)) return json({ error: "links" }, 400);
  const ts = await turnstileOk(request, env, body.turnstile);
  if (!ts.ok) return json({ error: "human_check", codes: ts.codes }, 403);
  const iph = await hashIp(request, env);
  const recent = await d.prepare("SELECT COUNT(*) AS n FROM reviews WHERE iph=? AND created > datetime('now','-1 day')").bind(iph).first();
  if (recent && recent.n >= 3) return json({ error: "limit" }, 429);
  await d.prepare(`INSERT INTO reviews (created, stars, ${ASPECTS.join(", ")}, features, improve, comment, name, role, status, iph, page)
      VALUES (datetime('now'), ${["?", ...ASPECTS.map(() => "?"), "?", "?", "?", "?", "?"].join(", ")}, 'pending', ?, ?)`)
    .bind(stars, ...ASPECTS.map((k) => asp[k]), features || null, improve || null, comment || null, name || null, role || null, iph, page || null).run();
  return json({ ok: true });
}
