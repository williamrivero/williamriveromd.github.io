// Admin API for certificates (header Authorization: Bearer <REVIEWS_ADMIN_TOKEN>)
// GET  /api/certs/admin?q=<name or code>   -> latest 300 records (all fields except the hashed connection)
// POST /api/certs/admin {codes:[...], action: "revoke" | "restore" | "delete"}
//      revoke keeps the record, and /verify then says the certificate was revoked; delete removes it (a learner's
//      request to erase their name), and /verify then says the code is not on record.
import { db, json, authorized } from "../../../functions-lib/certs.js";

const ACTIONS = {
  revoke: "UPDATE certificates SET status='revoked' WHERE code=?",
  restore: "UPDATE certificates SET status='valid' WHERE code=?",
  delete: "DELETE FROM certificates WHERE code=?",
};

export async function onRequestGet({ request, env }) {
  if (!authorized(request, env)) return json({ error: "unauthorized" }, 401);
  const d = await db(env);
  if (!d) return json({ error: "not_configured" }, 503);
  const q = (new URL(request.url).searchParams.get("q") || "").trim();
  const cols = "code, created, issued, name, track, exam, modules, modules_passed, active_min, score, total, exam_min, study_min, status";
  const rows = q
    ? await d.prepare(`SELECT ${cols} FROM certificates WHERE name LIKE ? OR code LIKE ? ORDER BY created DESC LIMIT 300`).bind(`%${q}%`, `%${q.toUpperCase()}%`).all()
    : await d.prepare(`SELECT ${cols} FROM certificates ORDER BY created DESC LIMIT 300`).all();
  return json({ items: rows.results || [] });
}

export async function onRequestPost({ request, env }) {
  if (!authorized(request, env)) return json({ error: "unauthorized" }, 401);
  const d = await db(env);
  if (!d) return json({ error: "not_configured" }, 503);
  let b;
  try { b = await request.json(); } catch (e) { return json({ error: "bad_request" }, 400); }
  const sql = ACTIONS[b.action];
  const codes = Array.isArray(b.codes) ? b.codes.filter((c) => typeof c === "string").slice(0, 200) : [];
  if (!sql || !codes.length) return json({ error: "bad_request" }, 400);
  await d.batch(codes.map((c) => d.prepare(sql).bind(c)));
  return json({ ok: true, changed: codes.length });
}
