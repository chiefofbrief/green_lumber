#!/usr/bin/env python3
"""
One-off news run for the AI watchlist.

Uses the existing news script (scripts/stock scripts/news.py) unchanged: it calls
that script's own fetch and markdown functions and writes one flat file per
ticker into this folder. No raw JSON is saved.

Usage (from the repository root):
    python3 "data/screener/AI Subsectors/News/run_news.py" fetch TICKER [TICKER ...]
    python3 "data/screener/AI Subsectors/News/run_news.py" fetch --all
    python3 "data/screener/AI Subsectors/News/run_news.py" headlines TICKER

fetch      Pulls 3 months of news (Perigon + FMP) into {TICKER}_news.md.
           --all reads every symbol from data/screener/AI Watchlist (working).md.
           Existing files are skipped unless --force is given.
headlines  Prints every Perigon story title (with its article count) and every
           FMP headline (with its source), each with its date. Nothing is dropped.
"""

import os
import re
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", ".."))
sys.path.insert(0, os.path.join(REPO, "scripts", "stock scripts"))

import news  # noqa: E402
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


def fetch(ticker, force=False):
    path = out_path(ticker)
    if os.path.exists(path) and not force:
        print(f"{ticker}: exists, skipped")
        return True
    from_date, to_date = get_date_range_months_back(MONTHS)
    stories = news.fetch_perigon(ticker, MONTHS)
    articles = news.fetch_fmp(ticker, MONTHS)
    if not stories and not articles:
        print(f"{ticker}: FAILED, no news from Perigon or FMP")
        return False
    with open(path, "w", encoding="utf-8") as f:
        f.write(news.generate_markdown(ticker, stories, articles, MONTHS, from_date, to_date))
    print(f"{ticker}: Perigon {len(stories)} stories, FMP {len(articles)} articles")
    return True


def headlines(ticker):
    md = open(out_path(ticker), encoding="utf-8").read()
    perigon, _, fmp = md.partition("## FMP Articles")
    print(f"# {ticker} headlines")
    print(md.split("\n")[2])  # date range line
    print("\n## Perigon stories")
    for title, n in re.findall(r"^### (\d{4}-\d\d-\d\d \| .*)\n\*(\d+) articles in cluster\*", perigon, re.M):
        print(f"- {title} ({n} articles)")
    print("\n## FMP headlines")
    for title, src in re.findall(r"^### (\d{4}-\d\d-\d\d \| .*)\n\*\*Source:\*\* (.*)$", fmp, re.M):
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
        print(f"[{i}/{len(tickers)}] ", end="")
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
