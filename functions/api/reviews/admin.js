// Admin API for the review queue (header Authorization: Bearer <REVIEWS_ADMIN_TOKEN>)
// GET  /api/reviews/admin?status=pending|approved|rating_only|rejected|all
//      -> items with ids plus pattern flags: same_conn (other submissions from the same hashed connection)
//         and burst (submissions from that connection within 10 minutes of this one)
// POST /api/reviews/admin  {ids:[...], action: "approve" | "rating_only" | "reject" | "delete"}
import { db, json, authorized } from "../../../functions-lib/reviews.js";

const ACTIONS = {
  approve: "UPDATE reviews SET status='approved' WHERE id=?",
  rating_only: "UPDATE reviews SET status='rating_only' WHERE id=?",
  reject: "UPDATE reviews SET status='rejected' WHERE id=?",
  delete: "DELETE FROM reviews WHERE id=?",
};

export async function onRequestGet({ request, env }) {
  if (!authorized(request, env)) return json({ error: "unauthorized" }, 401);
  const d = await db(env);
  if (!d) return json({ error: "not_configured" }, 503);
  const status = new URL(request.url).searchParams.get("status") || "pending";
  const where = status === "all" ? "" : "WHERE r.status=?";
  const sql = `SELECT r.id, r.created, r.stars, r.a_ease, r.a_design, r.a_read, r.a_nav, r.a_content, r.a_useful, r.a_learn, r.features, r.improve,
      r.comment, r.name, r.role, r.status, r.page,
      (SELECT COUNT(*) FROM reviews o WHERE o.iph=r.iph AND o.id<>r.id) AS same_conn,
      (SELECT COUNT(*) FROM reviews o WHERE o.iph=r.iph AND o.id<>r.id
         AND abs(strftime('%s',o.created)-strftime('%s',r.created))<=600) AS burst
    FROM reviews r ${where} ORDER BY r.id DESC LIMIT 300`;
  const q = status === "all" ? d.prepare(sql) : d.prepare(sql).bind(status);
  const rows = await q.all();
  const counts = await d.prepare("SELECT status, COUNT(*) AS n FROM reviews GROUP BY status").all();
  return json({ items: rows.results || [], counts: Object.fromEntries((counts.results || []).map((r) => [r.status, r.n])) });
}

export async function onRequestPost({ request, env }) {
  if (!authorized(request, env)) return json({ error: "unauthorized" }, 401);
  const d = await db(env);
  if (!d) return json({ error: "not_configured" }, 503);
  let body;
  try { body = await request.json(); } catch (e) { return json({ error: "bad_request" }, 400); }
  const sql = ACTIONS[body.action];
  const ids = (Array.isArray(body.ids) ? body.ids : [body.id]).map(Number).filter(Number.isInteger).slice(0, 300);
  if (!sql || !ids.length) return json({ error: "bad_request" }, 400);
  await d.batch(ids.map((id) => d.prepare(sql).bind(id)));
  return json({ ok: true, updated: ids.length });
}
