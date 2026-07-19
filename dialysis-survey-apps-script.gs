/**
 * Google Apps Script backend for guides/dialysis-satisfaction-survey.html
 * Appends each submitted survey as one row in a Google Sheet.
 *
 * ── SETUP (one time) ─────────────────────────────────────────────────────────
 * 1. Create a new Google Sheet (this will hold the responses).
 * 2. In that Sheet:  Extensions ▸ Apps Script.
 * 3. Delete the sample code, paste THIS whole file, and Save.
 * 4. (Optional) Put the Sheet's ID between the quotes in SHEET_ID below. If you
 *    leave it blank, the script writes to the Sheet it is bound to (the one you
 *    opened in step 2), which is what you normally want.
 * 5. Deploy ▸ New deployment ▸ type "Web app".
 *      - Description:      Dialysis satisfaction survey
 *      - Execute as:       Me
 *      - Who has access:   Anyone
 *    Click Deploy, authorize when prompted, and COPY the Web app URL
 *    (it looks like https://script.google.com/macros/s/AKfy.../exec).
 * 6. Open guides/dialysis-satisfaction-survey.html and paste that URL into:
 *      var SHEET_ENDPOINT = "";     // ← paste between the quotes
 *    Commit + push. Submissions now land in your Sheet.
 *
 * To change the form later, no Sheet changes are needed: this script adds a new
 * column automatically the first time it sees a new field name.
 * ─────────────────────────────────────────────────────────────────────────────
 */

var SHEET_ID   = "";          // leave blank to use the bound Sheet
var SHEET_NAME = "Responses"; // tab name; created if missing

function doPost(e) {
  var lock = LockService.getScriptLock();
  lock.tryLock(30000); // serialize concurrent submissions
  try {
    var ss = SHEET_ID ? SpreadsheetApp.openById(SHEET_ID) : SpreadsheetApp.getActiveSpreadsheet();
    var sh = ss.getSheetByName(SHEET_NAME) || ss.insertSheet(SHEET_NAME);

    var data = JSON.parse(e.postData.contents);

    // Read (or create) the header row.
    var headers = sh.getLastColumn() > 0
      ? sh.getRange(1, 1, 1, sh.getLastColumn()).getValues()[0]
      : [];
    if (headers.length === 0) {
      headers = ["Submitted at"];
      sh.getRange(1, 1, 1, 1).setValues([headers]);
      sh.setFrozenRows(1);
    }

    // Add any new field names as new columns (keeps old rows aligned).
    var changed = false;
    Object.keys(data).forEach(function (k) {
      if (headers.indexOf(k) === -1) { headers.push(k); changed = true; }
    });
    if (changed) sh.getRange(1, 1, 1, headers.length).setValues([headers]);

    // Build the row in header order.
    var row = headers.map(function (h) {
      if (h === "Submitted at") return new Date();
      return (data[h] !== undefined && data[h] !== null) ? data[h] : "";
    });
    sh.appendRow(row);

    return ContentService
      .createTextOutput(JSON.stringify({ ok: true }))
      .setMimeType(ContentService.MimeType.JSON);
  } catch (err) {
    return ContentService
      .createTextOutput(JSON.stringify({ ok: false, error: String(err) }))
      .setMimeType(ContentService.MimeType.JSON);
  } finally {
    lock.releaseLock();
  }
}

// Lets you open the /exec URL in a browser to confirm the deployment is live.
function doGet() {
  return ContentService.createTextOutput("Dialysis survey endpoint is running.");
}
