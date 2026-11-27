// Renal Care Academy certificates of completion: online verification (Nov 27 2026, Dr. Rivero).
// Same private D1 database as the site reviews (binding REVIEWS_DB), its own table. Admin key: REVIEWS_ADMIN_TOKEN.
// The learner chooses to register: the name, track and result are stored so anyone holding the certificate can scan
// its QR code and see it at /verify?c=<code>. Turnstile (TURNSTILE_SITE_KEY / TURNSTILE_SECRET) guards issuing.
// Limit: the examination is scored in the browser, so a record shows that the site issued the certificate after a
// passing result was reported, not that the learner sat the exam unaided. /verify says so.
export { json, hashIp, clean, authorized, turnstileOk } from "./reviews.js";

export const SCHEMA = `CREATE TABLE IF NOT EXISTS certificates (
  code TEXT PRIMARY KEY,
  created TEXT NOT NULL,
  issued TEXT NOT NULL,
  name TEXT NOT NULL,
  track TEXT NOT NULL,
  exam TEXT NOT NULL,
  modules INTEGER,
  score INTEGER NOT NULL,
  total INTEGER NOT NULL,
  exam_min INTEGER,
  study_min INTEGER,
  status TEXT NOT NULL DEFAULT 'valid',
  iph TEXT
)`;
export const PASS = 0.8;

export async function db(env) {
  if (!env.REVIEWS_DB) return null;
  await env.REVIEWS_DB.prepare(SCHEMA).run();
  return env.REVIEWS_DB;
}

// Issue date in Philippine time (YYYY-MM-DD).
export function manilaDate(d = new Date()) {
  return new Date(d.getTime() + 8 * 3600 * 1000).toISOString().slice(0, 10);
}

// RCA-<track initials>-<yymmdd>-<8 random hex>
export function newCode(track, issued) {
  const ini = track.split(/\s+/).map((w) => w.charAt(0)).join("").toUpperCase().replace(/[^A-Z]/g, "").slice(0, 4) || "X";
  const r = crypto.getRandomValues(new Uint8Array(4));
  const hex = Array.from(r).map((b) => b.toString(16).padStart(2, "0")).join("").toUpperCase();
  return `RCA-${ini}-${issued.replace(/-/g, "").slice(2)}-${hex}`;
}

export function publicRecord(r) {
  return {
    code: r.code, status: r.status, issued: r.issued, name: r.name, track: r.track, exam: r.exam,
    modules: r.modules, score: r.score, total: r.total, exam_min: r.exam_min, study_min: r.study_min,
  };
}
