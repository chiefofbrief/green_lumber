#!/usr/bin/env python3
"""
One-off financials run for the AI watchlist's Strength pass.

Uses the existing numbers script (scripts/stock scripts/numbers.py) unchanged: it calls that
script's own fetch_all() to pull FMP statements for each ticker, saves the combined raw data
as one flat JSON file per ticker, and computes only the Strength figures.

Usage (from the repository root):
    python3 "data/screener/Strength/run_financials.py" fetch TICKER [TICKER ...]
    python3 "data/screener/Strength/run_financials.py" fetch --all
    python3 "data/screener/Strength/run_financials.py" show TICKER [TICKER ...]

fetch   Fetches statements into raw/{TICKER}_financials.json (skips existing unless --force).
show    Prints the Strength figures computed from the saved raw file.

Figures (TTM = last four quarters, or last two half-years for half-yearly reporters):
    OCF margin, FCF margin, FCF margin for the last five fiscal years, share count change
    (latest period vs a year earlier, basic weighted average), Debt / OCF, net debt or net cash
    (total debt minus cash and short-term investments, latest balance sheet).
"""

import importlib.util
import json
import os
import sys
import time
from datetime import date

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
RAW = os.path.join(HERE, "raw")
WATCHLIST = os.path.join(REPO, "data", "screener", "AI Watchlist (working).md")

# numbers.py shadows the stdlib `numbers` module, so load it under another name.
_spec = importlib.util.spec_from_file_location(
    "fmp_numbers", os.path.join(REPO, "scripts", "stock scripts", "numbers.py"))
fmp = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(fmp)
sf, div = fmp.sf, fmp.div


def raw_path(t):
    return os.path.join(RAW, f"{t}_financials.json")


def watchlist_tickers():
    out = []
    for line in open(WATCHLIST, encoding="utf-8"):
        c = [x.strip() for x in line.strip().strip("|").split("|")]
        if len(c) > 2 and c[0].isdigit():
            out.append(c[1])
    return out


def fetch(t, force=False):
    if os.path.exists(raw_path(t)) and not force:
        print(f"{t}: exists, skipped")
        return True
    raw = fmp.fetch_all(t)
    if not raw:
        print(f"{t}: FAILED, missing required statements")
        return False
    os.makedirs(RAW, exist_ok=True)
    with open(raw_path(t), "w", encoding="utf-8") as f:
        json.dump(raw, f)
    print(f"{t}: saved")
    return True


def _desc(lst):
    return sorted([x for x in (lst or []) if x.get("date")], key=lambda x: x["date"], reverse=True)


def figures(t):
    raw = json.load(open(raw_path(t), encoding="utf-8"))
    inc = _desc(raw.get("inc_q")); cf = _desc(raw.get("cf_q")); bal = _desc(raw.get("bal_q"))
    d = [date.fromisoformat(x["date"]) for x in inc[:2]]
    semi = len(d) == 2 and (d[0] - d[1]).days > 120
    n = 2 if semi else 4
    cf_by = {x["date"]: x for x in cf}
    rows = [(i, cf_by.get(i["date"])) for i in inc[:n]]
    out = {"half_yearly": semi}
    if len(rows) == n and all(c for _, c in rows):
        s = lambda src, k: sum(sf(x.get(k)) or 0 for x in src)
        rev = s([i for i, _ in rows], "revenue")
        ocf = s([c for _, c in rows], "operatingCashFlow")
        fcf = s([c for _, c in rows], "freeCashFlow")
        out.update(ocf_margin=div(ocf, rev), fcf_margin=div(fcf, rev), ocf=ocf)
    if bal:
        b = bal[0]
        debt = sf(b.get("totalDebt"))
        cash = sf(b.get("cashAndShortTermInvestments")) or sf(b.get("cashAndCashEquivalents"))
        out.update(debt=debt, cash=cash,
                   net_debt=(debt - cash) if debt is not None and cash is not None else None,
                   debt_to_ocf=div(debt, out.get("ocf")) if out.get("ocf") and out["ocf"] > 0 else None)
    if len(inc) > n:
        # Basic, not diluted: diluted counts jump when a loss-maker turns profitable and its
        # options or convertibles start counting, which looks like issuance but isn't.
        cur = sf(inc[0].get("weightedAverageShsOut")) or sf(inc[0].get("weightedAverageShsOutDil"))
        ago = sf(inc[n].get("weightedAverageShsOut")) or sf(inc[n].get("weightedAverageShsOutDil"))
        out["share_change"] = div(cur - ago, ago) if cur is not None and ago else None
    ia = {x["date"]: x for x in (raw.get("inc_a") or [])}
    hist = []
    for c in _desc(raw.get("cf_a"))[:5]:
        i = ia.get(c["date"])
        if i:
            hist.append((fmp.period_label(i), div(sf(c.get("freeCashFlow")), sf(i.get("revenue")))))
    out["fcf_history"] = list(reversed(hist))
    out["currency"] = (inc[0].get("reportedCurrency") if inc else None)
    return out


def fmt(t):
    f = figures(t)
    p = lambda v: "-" if v is None else f"{v*100:.1f}%"
    nd = f.get("net_debt")
    netdebt = "-" if nd is None else (f"net cash {abs(nd)/1e9:,.1f}B" if nd < 0 else f"net debt {nd/1e9:,.1f}B")
    if f.get("currency"):
        netdebt += f" ({f['currency']})"
    if f.get("debt_to_ocf") is not None:
        dto = f"{f['debt_to_ocf']:.1f} yrs"
    elif f.get("ocf") is not None and f["ocf"] <= 0:
        dto = "n/a (OCF negative)"
    else:
        dto = "-"
    hist = " / ".join(f"{lbl} {p(v)}" for lbl, v in f["fcf_history"]) or "-"
    sc = "-" if f.get("share_change") is None else f"{f['share_change']*100:+.1f}%"
    return {"OCF margin (TTM)": p(f.get("ocf_margin")), "FCF margin (TTM)": p(f.get("fcf_margin")),
            "FCF margin (last 5 FY)": hist, "Share count change (YoY)": sc,
            "Debt / OCF": dto, "Net debt or net cash": netdebt, "half_yearly": f["half_yearly"]}


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("fetch", "show"):
        print(__doc__); sys.exit(1)
    cmd, args = sys.argv[1], sys.argv[2:]
    tickers = watchlist_tickers() if "--all" in args else [a.upper() for a in args if not a.startswith("--")]
    if cmd == "show":
        for t in tickers:
            print(t, fmt(t))
        return
    failed = []
    for i, t in enumerate(tickers, 1):
        print(f"[{i}/{len(tickers)}] ", end="", flush=True)
        try:
            if not fetch(t, "--force" in args):
                failed.append(t)
        except Exception as e:
            print(f"{t}: FAILED, {e}"); failed.append(t)
        time.sleep(0.3)
    print(f"\nDone. {len(tickers) - len(failed)} ok, {len(failed)} failed: {', '.join(failed) or 'none'}")


if __name__ == "__main__":
    main()
