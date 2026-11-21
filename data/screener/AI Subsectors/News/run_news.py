#!/usr/bin/env python3
"""
One-off news run for the AI watchlist. FMP only: this script makes no Perigon calls.

Uses the FMP fetch from the existing news script (scripts/stock scripts/news.py),
unchanged, and writes one flat file per ticker into this folder. No raw JSON is saved.

Usage (from the repository root):
    python3 "data/screener/AI Subsectors/News/run_news.py" fetch TICKER [TICKER ...]
    python3 "data/screener/AI Subsectors/News/run_news.py" fetch --all
    python3 "data/screener/AI Subsectors/News/run_news.py" headlines TICKER

fetch      Pulls 3 months of FMP news (one FMP call per 30-day window, 3 calls per
           ticker) into {TICKER}_news.md.
           --all reads every symbol from data/screener/AI Watchlist (working).md.
           Existing files are skipped unless --force is given.
headlines  Prints every headline in a ticker's file, with its date and source.
"""

import os
import re
import sys
import time
from datetime import datetime

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "scripts", "stock scripts"))

from news import fetch_fmp  # noqa: E402  (FMP only; Perigon functions are never imported)
from shared_utils import get_date_range_months_back  # noqa: E402

MONTHS = 3
WATCHLIST = os.path.join(REPO, "data", "screener", "AI Watchlist (working).md")


def out_path(ticker):
    return os.path.join(HERE, f"{ticker}_news.md")


def watchlist_tickers():
    tickers = []
    for line in open(WATCHLIST, encoding="utf-8"):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) > 2 and cells[0].isdigit():
            tickers.append(cells[1])
    return tickers


def to_markdown(ticker, articles, from_date, to_date):
    sources = {a.get("publisher") or a.get("site") for a in articles if (a.get("publisher") or a.get("site"))}
    md = [f"# {ticker} News", f"**Generated:** {datetime.now().strftime('%Y-%m-%d %H:%M')}",
          f"**Date Range:** {from_date} to {to_date}", "**Source:** FMP only", "",
          f"## FMP Articles ({len(articles)} from {len(sources)} sources)", ""]
    for a in articles:
        date = (a.get("publishedDate") or "")[:10] or "Unknown"
        md.append(f"### {date} | {a.get('title', 'Untitled')}")
        md.append(f"**Source:** {a.get('publisher') or a.get('site') or 'Unknown'}")
        if a.get("url"):
            md.append(f"**URL:** {a['url']}")
        md.append("")
        if a.get("text"):
            md += [a["text"], ""]
        md += ["---", ""]
    return "\n".join(md)


def fetch(ticker, force=False):
    path = out_path(ticker)
    if os.path.exists(path) and not force:
        print(f"{ticker}: exists, skipped")
        return True
    from_date, to_date = get_date_range_months_back(MONTHS)
    articles = fetch_fmp(ticker, MONTHS)
    if not articles:
        print(f"{ticker}: FAILED, no FMP news")
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(to_markdown(ticker, articles, from_date, to_date))
    print(f"{ticker}: FMP {len(articles)} articles")
    return True


def headlines(ticker):
    md = open(out_path(ticker), encoding="utf-8").read()
    print(f"# {ticker} headlines")
    for title, src in re.findall(r"^### (\d{4}-\d\d-\d\d \| .*)\n\*\*Source:\*\* (.*)$", md, re.M):
        print(f"- {title} ({src})")


def main():
    if len(sys.argv) < 3 or sys.argv[1] not in ("fetch", "headlines"):
        print(__doc__)
        sys.exit(1)
    cmd, args = sys.argv[1], sys.argv[2:]
    if cmd == "headlines":
        headlines(args[0].upper())
        return
    force = "--force" in args
    tickers = watchlist_tickers() if "--all" in args else [a.upper() for a in args if not a.startswith("--")]
    failed = []
    for i, t in enumerate(tickers, 1):
        print(f"[{i}/{len(tickers)}] ", end="", flush=True)
        try:
            if not fetch(t, force):
                failed.append(t)
        except Exception as e:
            print(f"{t}: FAILED, {e}")
            failed.append(t)
        time.sleep(0.5)
    print(f"\nDone. {len(tickers) - len(failed)} ok, {len(failed)} failed: {', '.join(failed) or 'none'}")


if __name__ == "__main__":
    main()
