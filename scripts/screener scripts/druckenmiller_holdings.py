#!/usr/bin/env python3
"""
Druckenmiller Holdings Tracker
===============================

Pulls Duquesne Family Office's (Stanley Druckenmiller) latest 13F holdings,
attaches a cost-basis estimate per position, and diffs against the last saved
snapshot to flag new buys, full exits, and share-count changes.

Caveat: 13F filings disclose shares/value only, never purchase price.
`avgPricePaid` below is FMP's own derived estimate, not an exact per-lot cost basis.

Outputs:
    data/institutional_holders/DUQUESNE/latest.json   raw snapshot (overwritten each run)
    data/institutional_holders/DUQUESNE/latest.md      readable summary + diff

Usage:
    python "druckenmiller_holdings.py"
"""

import sys
import os
import time
import requests
from datetime import datetime

sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "stock scripts"))
from shared_utils import ensure_directory_exists, save_json, load_json

FMP_BASE = "https://financialmodelingprep.com/stable"
FMP_API_KEY = os.getenv("FMP_API_KEY")

CIK = "0001536411"          # Duquesne Family Office LLC
INVESTOR_NAME_MATCH = "DUQUESNE"

OUTPUT_DIR = "/workspaces/green_lumber/data/institutional_holders/DUQUESNE"
API_CALL_DELAY = 0.25


def fetch(url, label):
    try:
        r = requests.get(url, timeout=30)
        if r.status_code != 200:
            print(f"  [{label}] HTTP {r.status_code}: {r.text[:200]}", file=sys.stderr)
            return None
        return r.json()
    except requests.exceptions.RequestException as e:
        print(f"  [{label}] Request error: {e}", file=sys.stderr)
        return None


def find_latest_quarter():
    """Walk backward from the current quarter until one has filed holdings."""
    now = datetime.now()
    year, quarter = now.year, (now.month - 1) // 3 + 1
    for _ in range(6):
        url = f"{FMP_BASE}/institutional-ownership/extract?cik={CIK}&year={year}&quarter={quarter}&apikey={FMP_API_KEY}"
        data = fetch(url, f"extract {year}Q{quarter}")
        if isinstance(data, list) and data:
            return year, quarter, data
        quarter -= 1
        if quarter == 0:
            quarter, year = 4, year - 1
        time.sleep(API_CALL_DELAY)
    return None, None, None


def attach_cost_basis(holdings, year, quarter):
    """For each holding, look up avgPricePaid / firstAdded, filtered to Duquesne."""
    results = []
    for i, h in enumerate(holdings, 1):
        symbol = h.get("symbol")
        print(f"  [{i}/{len(holdings)}] {symbol}...", file=sys.stderr)

        row = {
            "symbol": symbol,
            "securityName": h.get("securityName"),
            "shares": h.get("sharesNumber"),
            "marketValue": h.get("marketValue"),
            "weight": h.get("weight"),
            "isNew": h.get("isNew"),
            "avgPricePaid": None,
            "firstAdded": None,
        }

        if symbol:
            url = f"{FMP_BASE}/institutional-ownership/extract-analytics/holder?symbol={symbol}&year={year}&quarter={quarter}&limit=100&apikey={FMP_API_KEY}"
            data = fetch(url, f"analytics {symbol}")
            if isinstance(data, list):
                for entry in data:
                    if INVESTOR_NAME_MATCH in (entry.get("investorName") or "").upper():
                        row["avgPricePaid"] = entry.get("avgPricePaid")
                        row["firstAdded"] = entry.get("firstAdded")
                        break
            time.sleep(API_CALL_DELAY)

        results.append(row)
    return results


def diff_snapshots(current, previous):
    if not previous:
        return None
    prev_by_symbol = {p["symbol"]: p for p in previous.get("holdings", [])}
    curr_by_symbol = {p["symbol"]: p for p in current}

    added = [p for sym, p in curr_by_symbol.items() if sym not in prev_by_symbol]
    removed = [p for sym, p in prev_by_symbol.items() if sym not in curr_by_symbol]
    changed = [
        {"symbol": sym, "prevShares": prev_by_symbol[sym].get("shares"), "newShares": p.get("shares")}
        for sym, p in curr_by_symbol.items()
        if sym in prev_by_symbol and p.get("shares") != prev_by_symbol[sym].get("shares")
    ]
    return {"added": added, "removed": removed, "changed": changed}


def fmt_money(v):
    return f"${v:,.0f}" if isinstance(v, (int, float)) else "N/A"


def fmt_price(v):
    return f"${v:.2f}" if isinstance(v, (int, float)) else "N/A"


def print_table(results):
    print(f"\n{'Symbol':<8} {'Shares':>14} {'Mkt Value':>16} {'Avg Price Paid':>15} {'First Added':>12} {'New?':>5}")
    print("-" * 78)
    for r in sorted(results, key=lambda x: -(x["marketValue"] or 0)):
        shares = f"{r['shares']:,}" if r["shares"] is not None else "N/A"
        new = "YES" if r["isNew"] else ""
        print(f"{r['symbol']:<8} {shares:>14} {fmt_money(r['marketValue']):>16} {fmt_price(r['avgPricePaid']):>15} {(r['firstAdded'] or 'N/A'):>12} {new:>5}")


def print_diff(diff):
    if diff is None:
        print("\nNo prior snapshot to compare against — this is the first run.")
        return
    if not diff["added"] and not diff["removed"] and not diff["changed"]:
        print("\nNo changes vs. last saved quarter.")
        return
    if diff["added"]:
        print(f"\n+ NEW POSITIONS ({len(diff['added'])}):")
        for p in diff["added"]:
            print(f"    {p['symbol']:<8} {p['shares']:,} shares, {fmt_money(p['marketValue'])}, avg paid {fmt_price(p['avgPricePaid'])}")
    if diff["removed"]:
        print(f"\n- EXITED POSITIONS ({len(diff['removed'])}):")
        for p in diff["removed"]:
            print(f"    {p['symbol']:<8} (was {p['shares']:,} shares)")
    if diff["changed"]:
        print(f"\n~ SHARE COUNT CHANGES ({len(diff['changed'])}):")
        for c in diff["changed"]:
            direction = "+" if (c["newShares"] or 0) > (c["prevShares"] or 0) else "-"
            print(f"    {c['symbol']:<8} {c['prevShares']:,} -> {c['newShares']:,} ({direction})")


def build_markdown(year, quarter, results, diff):
    lines = [
        f"# Duquesne Family Office (Stanley Druckenmiller) — {year} Q{quarter}",
        f"*Generated: {datetime.now().strftime('%Y-%m-%d')}*",
        "",
        "Cost basis (`avgPricePaid`) is FMP's derived estimate — 13F filings "
        "don't disclose actual purchase price.",
        "",
        "## Holdings",
        "",
        "| Symbol | Shares | Market Value | Avg Price Paid | First Added | New? |",
        "|---|---|---|---|---|---|",
    ]
    for r in sorted(results, key=lambda x: -(x["marketValue"] or 0)):
        shares = f"{r['shares']:,}" if r["shares"] is not None else "N/A"
        new = "Yes" if r["isNew"] else ""
        lines.append(f"| {r['symbol']} | {shares} | {fmt_money(r['marketValue'])} | {fmt_price(r['avgPricePaid'])} | {r['firstAdded'] or 'N/A'} | {new} |")

    lines.append("")
    lines.append("## Changes vs. Last Snapshot")
    lines.append("")
    if diff is None:
        lines.append("*First run — no prior snapshot to compare.*")
    elif not diff["added"] and not diff["removed"] and not diff["changed"]:
        lines.append("*No changes.*")
    else:
        if diff["added"]:
            lines.append(f"**New positions:** {', '.join(p['symbol'] for p in diff['added'])}")
        if diff["removed"]:
            lines.append(f"**Exited positions:** {', '.join(p['symbol'] for p in diff['removed'])}")
        if diff["changed"]:
            lines.append(f"**Share count changes:** {', '.join(c['symbol'] for c in diff['changed'])}")

    return "\n".join(lines) + "\n"


def main():
    if not FMP_API_KEY:
        print("Error: FMP_API_KEY environment variable not set", file=sys.stderr)
        sys.exit(1)

    ensure_directory_exists(OUTPUT_DIR)

    year, quarter, holdings = find_latest_quarter()
    if not holdings:
        print("No holdings data found for any recent quarter.")
        sys.exit(1)

    print(f"=== Duquesne Family Office holdings: {year} Q{quarter} ({len(holdings)} positions) ===", file=sys.stderr)
    results = attach_cost_basis(holdings, year, quarter)

    snapshot_path = os.path.join(OUTPUT_DIR, "latest.json")
    previous = load_json(snapshot_path)
    diff = diff_snapshots(results, previous)

    print_table(results)
    print_diff(diff)

    save_json({"year": year, "quarter": quarter, "holdings": results}, snapshot_path)

    md_path = os.path.join(OUTPUT_DIR, "latest.md")
    with open(md_path, "w") as f:
        f.write(build_markdown(year, quarter, results, diff))

    print(f"\nSaved: {snapshot_path}")
    print(f"Saved: {md_path}")


if __name__ == "__main__":
    main()
