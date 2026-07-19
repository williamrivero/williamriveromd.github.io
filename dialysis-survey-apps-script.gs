/**
 * Google Apps Script backend for guides/dialysis-satisfaction-survey.html
 *
 * Logs each submitted survey to a Google Sheet for tallying. Branch email
 * notifications are handled separately by Web3Forms (see WEB3FORMS_KEYS in the
 * survey page) — this script only writes the Sheet.
 *
 * Each response is written twice:
 *   • "Responses"  — the master tab: every submission, for HQ tallying.
 *   • a per-branch tab (e.g. "SJB — Quezon Avenue") — that branch's own copy,
 *     so a branch can review just its results by opening its tab.
 *
 * NOTE ON ACCESS: Google Sheets sharing is per-file, not per-tab. Per-branch
 * tabs group the data conveniently, but anyone you share the file with can see
 * all tabs. If a branch must see ONLY its own data, give it a separate
 * spreadsheet — ask and this script can be pointed at one file per branch.
 *
 * ── SETUP (one time) ─────────────────────────────────────────────────────────
 * 1. Create a Google Sheet to hold responses.
 * 2. Extensions ▸ Apps Script. Delete the sample, paste THIS file, Save.
 * 3. (Optional) put the Sheet ID in SHEET_ID below; blank = the bound Sheet.
 * 4. Deploy ▸ New deployment ▸ Web app.
 *      Execute as: Me   ·   Who has access: Anyone
 *    Deploy, authorize, and COPY the /exec URL.
 * 5. In guides/dialysis-satisfaction-survey.html set:
 *      var SHEET_ENDPOINT = "...paste the /exec URL...";
 *    Commit + push.
 *
 * Add a new question later? No Sheet changes needed — a new column is created
 * automatically the first time this script sees a new field name.
 * ─────────────────────────────────────────────────────────────────────────────
 */

var SHEET_ID    = "";           // blank = use the bound Sheet
var MASTER_TAB  = "Responses";  // every submission lands here

// Branch key (sent by the page) → friendly per-branch tab name.
var BRANCH_TABS = {
  "sjb-qave":        "SJB — Quezon Avenue",
  "sjb-marikina":    "SJB — Marikina",
  "sjb-caloocan":    "SJB — Caloocan",
  "core-santillan":  "Core — Santillan",
  "sjrc-concepcion": "St Josef — Concepcion",
  "sjrc-marilao":    "St Josef — Marilao"
};

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(30000); // serialize concurrent submissions
  try {
    var ss = SHEET_ID ? SpreadsheetApp.openById(SHEET_ID) : SpreadsheetApp.getActiveSpreadsheet();
    var data = JSON.parse(e.postData.contents);

    appendRow_(ss, MASTER_TAB, data);

    var branchTab = BRANCH_TABS[data["Branch key"]] || "Other / unspecified";
    appendRow_(ss, branchTab, data);

    return json_({ ok: true });
  } catch (err) {
    return json_({ ok: false, error: String(err) });
  } finally {
    lock.releaseLock();
  }
}

// Append `data` to the named tab, auto-creating the tab and any new columns.
function appendRow_(ss, tabName, data) {
  var sh = ss.getSheetByName(tabName) || ss.insertSheet(tabName);

  var headers = sh.getLastColumn() > 0
    ? sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0]
    : [];
  if (headers.length === 0) {
    headers = ["Submitted at"];
    sh.getRange(1, 1, 1, 1).setValues([headers]);
    sh.setFrozenRows(1);
  }

  var changed = false;
  Object.keys(data).forEach(function (k) {
    if (headers.indexOf(k) === -1) { headers.push(k); changed = true; }
  });
  if (changed) sh.getRange(1, 1, 1, headers.length).setValues([headers]);

  var row = headers.map(function (h) {
    if (h === "Submitted at") return new Date();
    return (data[h] !== undefined && data[h] !== null) ? data[h] : "";
  });
  sh.appendRow(row);
}

function json_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj))
    .setMimeType(ContentService.MimeType.JSON);
}

// Open the /exec URL in a browser to confirm the deployment is live.
function doGet() {
  return ContentService.createTextOutput("Dialysis survey endpoint is running.");
}
