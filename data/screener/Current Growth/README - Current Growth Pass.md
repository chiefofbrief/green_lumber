# Current Growth Pass

## Context
I'm building a watchlist of AI companies. The working list is `data/screener/AI Watchlist (working).md` (130 companies). This pass writes one read per company on its current sales growth. It is one of several separate pieces of data; it is not the full analysis of the company. Each company is assessed on its own, without comparing it to others.

## The file
`data/screener/Current Growth/Current Growth.md` has one row per company:
- **Inputs:** Symbol, Company, and five figures from the screener (mid-November 2026): Sales growth TTM, Sales growth latest Q (YoY), TTM growth accel, 4Q growth accel, and Gross margin vs 5-yr low.
- **Output, empty until filled:** **Current growth**.

## Guidance
**Current growth** is how fast sales are growing now, and whether the pace is speeding up or slowing down. It is the starting point and an indicator of what comes next, but a company growing fast now may not keep doing it.

Two figures give the level of growth:
- **Sales growth TTM:** sales over the last four reported quarters compared with the four quarters before, as a percentage.
- **Sales growth latest Q (YoY):** the latest quarter's sales compared with the same quarter a year earlier.

Two figures give the change in growth:
- **TTM growth accel:** the change in the annual growth rate, in percentage points. Positive means speeding up.
- **4Q growth accel:** the change in the quarterly growth rate over the last year, in percentage points. Positive means speeding up.

Read the level and the change together, not mechanically. High growth that is slowing can still be strong growth. Sharp acceleration from a low level can still be modest growth. The strongest picture is high growth that is also speeding up.

A fifth figure speaks to where the growth is coming from:
- **Gross margin vs 5-yr low:** how far gross margin, what the company keeps from each sale after the direct cost of making it, is above its lowest annual level of the last five years, in percentage points. A gap far above history may mean part of the growth is coming from higher prices rather than more volume, and that it may be temporary if prices fall back. The five-year low can be an unusually weak year, so treat a large gap as a possible sign, not proof.

## Steps
1. Find the first row where **Current growth** is empty. Start there.
2. For each row, write **Current growth**: a short paragraph on the level of growth and its change, read together, stating each figure, and on what the gross margin gap may say about where the growth is coming from.
3. Do five rows, then stop and ask whether to continue.

## Rules
- Use only the figures in the row and the guidance above.
- A dash means the figure is not available, not zero. For the gross margin gap it usually means fewer than five years of data. Say so where it matters.
- Write in complete sentences.
- Do not compare the company with others, and do not assess potential growth, valuation, strength or whether the company belongs on the watchlist.
- Do not use the `|` character in a cell.
- Do not commit or push unless asked.
