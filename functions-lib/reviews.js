// Shared helpers for the site review API (Cloudflare Pages Functions, Nov 26 2026, Dr. Rivero).
// Storage: a private Cloudflare D1 database bound to the Pages project as REVIEWS_DB.
// Secret: REVIEWS_ADMIN_TOKEN (Pages > Settings > Variables and Secrets) guards approvals.
// Turnstile (Cloudflare's human check): TURNSTILE_SITE_KEY (public, sent to the page) and TURNSTILE_SECRET.
// Once TURNSTILE_SECRET is set, every submission must pass the check.
// Nothing is public until approved: the average counts approved ratings only; comments show only when approved.

export const SCHEMA = `CREATE TABLE IF NOT EXISTS reviews (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  created TEXT NOT NULL,
  stars INTEGER NOT NULL CHECK (stars BETWEEN 1 AND 5),
  a_ease INTEGER, a_design INTEGER, a_read INTEGER, a_nav INTEGER, a_content INTEGER, a_useful INTEGER, a_learn INTEGER,
  features TEXT,
  improve TEXT,
  comment TEXT,
  name TEXT,
  role TEXT,
  status TEXT NOT NULL DEFAULT 'pending',
  iph TEXT,
  page TEXT
)`;
// Aspects (optional, 1-5): ease of use, design (look and feel), readability, navigation, content quality, usefulness
// (worded "Clinical usefulness" for clinicians/students/staff, "Helps me understand and manage my condition" otherwise),
// learning value (Academy modules; asked only of clinicians, students and staff, or anyone who picks Academy).
export const ASPECTS = ["a_ease", "a_design", "a_read", "a_nav", "a_content", "a_useful", "a_learn"];
// "What do you like most?": up to 3 of these keys ("free" = the site being free to use). "improve" is private (admin only); "comment" is public once approved.
export const FEATURES = ["guides", "calculators", "drugs", "scheduler", "interactions", "academy", "atlas",
  "physiology", "languages", "offline", "free", "other"];
// Every submission starts 'pending' (Dr. Rivero, Nov 26 2026: ratings are validated too).
// status: 'pending' | 'approved' (rating counts, comment shown) | 'rating_only' (rating counts, comment hidden)
//         | 'rejected' (excluded from everything)
export const COUNTED = "status IN ('approved','rating_only')";

export const ROLES = ["patient", "family", "clinician", "staff", "student", "other"];

export function json(data, status = 200, extra = {}) {
  return new Response(JSON.stringify(data), {
    status,
    headers: { "content-type": "application/json; charset=utf-8", "cache-control": "no-store", ...extra },
  });
}

export async function db(env) {
  if (!env.REVIEWS_DB) return null;
  await env.REVIEWS_DB.prepare(SCHEMA).run();
  return env.REVIEWS_DB;
}

export async function hashIp(request, env) {
  const ip = request.headers.get("cf-connecting-ip") || "";
  const salt = env.REVIEWS_ADMIN_TOKEN || "rcm-reviews";
  const buf = await crypto.subtle.digest("SHA-256", new TextEncoder().encode(salt + "|" + ip));
  return Array.from(new Uint8Array(buf)).slice(0, 16).map((b) => b.toString(16).padStart(2, "0")).join("");
}

export function clean(s, max) {
  if (typeof s !== "string") return "";
  // drop control and invisible formatting characters (keep newlines); collapse runs of blank lines
  s = s.replace(/[\u0000-\u0009\u000B-\u001F\u007F\u200B-\u200F\u2028-\u202E\u2060\uFEFF]/g, "").replace(/\n{3,}/g, "\n\n").trim();
  return s.slice(0, max);
}

export function authorized(request, env) {
  const want = env.REVIEWS_ADMIN_TOKEN || "";
  const got = (request.headers.get("authorization") || "").replace(/^Bearer\s+/i, "");
  if (!want || got.length !== want.length) return false;
  let diff = 0;
  for (let i = 0; i < want.length; i++) diff |= want.charCodeAt(i) ^ got.charCodeAt(i);
  return diff === 0;
}

export async function turnstileOk(request, env, token) {
  if (!env.TURNSTILE_SECRET) return true;                 // not set up yet: rely on the other filters
  if (!token || typeof token !== "string") return false;
  const form = new FormData();
  form.append("secret", env.TURNSTILE_SECRET);
  form.append("response", token);
  const ip = request.headers.get("cf-connecting-ip");
  if (ip) form.append("remoteip", ip);
  try {
    const r = await fetch("https://challenges.cloudflare.com/turnstile/v0/siteverify", { method: "POST", body: form });
    const j = await r.json();
    return !!j.success;
  } catch (e) { return false; }
}
