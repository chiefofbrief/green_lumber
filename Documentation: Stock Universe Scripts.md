# Documentation: Fetching All US Stocks

## Overview

There are three scripts which all run independently and create their own CSV file. 
* **master_stock_universe.py**: Captures all US stocks, including OTC, on the following exchanges: NASDAQ, NYSE, AMEX, CBOE, OTC, PNK. Each exchange is pulled in 3 type-slices (ETF / fund / common) to stay under the screener's 10,000-row-per-call cap; any slice still at the cap is re-split by isActivelyTrading (true/false). Partitioning is by type and trading state, never market cap, so null-market-cap names are never dropped.
* **active_stock_universe.py**: Filters the master universe to exclude ETFs, mutual funds, and stocks that are not actively trading: isEtf=false, isFund=false, isActivelyTrading=true. CBOE is dropped here (only master includes it); exchanges are NASDAQ, NYSE, AMEX, OTC, PNK.
* **large_actives_with_metrics.py**: Filters the active stock universe (marketCap ≥ $1B, dollar volume price×volume ≥ $1M/day, prior-TTM sales ≥ $10M USD) and drops non-comparable / price-driven / lottery industries before enriching (banks, insurers, REITs, asset managers, monetary metals, biotech). Each surviving name is ranked by percentile (0–100, higher = better) on every axis, with a composite score as the default sort.

Commands:
* python3 Scripts/master_stock_universe.py
* python3 Scripts/active_stock_universe.py
* python3 Scripts/large_actives_with_metrics.py

-------------

## Data Points

**master_stock_universe.py**
* symbol
* companyName
* marketCap
* sector
* industry
* volume
* exchange
* isEtf
* isFund
* isActivelyTrading

**active_stock_universe.py**
* same as master_stock_universe.py

**large_actives_with_metrics.py**

Percentile columns (`pctl_*`): each is the name's rank of the underlying raw value across all names in the file — 0 (lowest) to 100 (highest), computed as (# names with a strictly lower value) ÷ (N − 1) × 100, recomputed every run. Higher = better; "inverted" means a lower raw value is better, so the rank is flipped (100 − rank). Blank if the raw value is missing (excluded from that ranking).

* symbol: ticker
* company_name: company name
* industry: FMP industry label (also drives the exclusion filter)
* market_cap_usd: market capitalization in USD (from the screener)
* composite: default sort. Weighted average of three 0–100 pillar scores — growth ×0.50, profitability ×0.30, affordability ×0.20. Growth = 0.5 × avg(pctl_growth_ttm, pctl_growth_latest_q) + 0.5 × avg(pctl_accel_ttm, pctl_accel_4q). Profitability = avg(pctl_gross_margin, pctl_fcf_margin). Affordability = pctl_ev_sales. Any missing piece drops out and the remaining weights re-normalize. debt_flag is not included.
* pctl_growth_ttm: rank of sales_growth_ttm_vs_prior_ttm_pct (faster growth = higher)
* pctl_growth_latest_q: rank of sales_growth_latest_q_yoy_pct
* pctl_accel_ttm: rank of sales_growth_ttm_accel_pp
* pctl_accel_4q: rank of sales_growth_4q_net_accel_pp
* pctl_gross_margin: rank of gross_profit_to_sales_ttm_pct
* pctl_fcf_margin: rank of fcf_to_sales_ttm_pct
* pctl_ev_sales: rank of ev_to_sales_ttm, inverted (cheaper = higher)
* pctl_gm_vs_trough: rank of gross_profit_to_sales_vs_5yr_trough_pp, inverted (nearer its 5-yr trough = higher). Context only — not in composite.
* pctl_fcf_vs_trough: rank of fcf_to_sales_vs_5yr_trough_pp, inverted. Context only — not in composite.
* debt_flag: "neg FCF" if the company carries debt but TTM free cash flow ≤ 0 (can't service debt from cash flow at all); "high >10x" if total_debt_to_fcf > 10; blank otherwise. Never flagged if it has no debt or FCF can't be computed.
* analyst_sell_pct: (sell + strongSell) ÷ (strongBuy + buy + hold + sell + strongSell) × 100
* analyst_count: total analyst grades (strongBuy + buy + hold + sell + strongSell)
* ipo_date: IPO date (from the company profile)
* sales_ttm_usd: trailing-twelve-month sales = sum of the last 4 reported quarters, converted to USD at the spot FX rate. Blank if that currency's FX rate can't be resolved (name is then dropped).
* sales_growth_ttm_vs_prior_ttm_pct: (TTM sales ÷ the prior 4-quarter TTM sales − 1) × 100
* sales_growth_latest_q_yoy_pct: (most recent quarter's sales ÷ the same quarter one year earlier − 1) × 100
* sales_growth_ttm_accel_pp: recent TTM growth − prior-year TTM growth, in percentage points (change in the annual growth rate)
* sales_growth_4q_net_accel_pp: latest quarter's YoY growth − the YoY growth of the quarter four periods earlier, in percentage points (net change in quarterly growth over the last year)
* gross_profit_to_sales_ttm_pct: (TTM gross profit ÷ TTM sales) × 100
* fcf_to_sales_ttm_pct: (TTM free cash flow ÷ TTM sales) × 100
* total_debt_to_fcf: total debt (latest quarter) ÷ TTM free cash flow — a multiple (4.0 = debt is 4× TTM FCF). Negative when TTM FCF is negative. Same currency top and bottom, so no FX needed.
* gross_profit_to_sales_vs_5yr_trough_pp: gross_profit_to_sales_ttm_pct − the lowest annual gross-profit/sales of the last 5 years, in percentage points. Blank if < 5 years of data.
* fcf_to_sales_vs_5yr_trough_pp: fcf_to_sales_ttm_pct − the lowest annual FCF/sales of the last 5 years, in percentage points. Blank if < 5 years.
* ev_to_sales_ttm: (market_cap_usd + total debt − cash) ÷ sales_ttm_usd. Debt and cash are latest quarter, converted to USD.
* pe_ratio_ttm: market_cap_usd ÷ TTM net income (net income converted to USD). Blank if TTM net income ≤ 0.
* shares_outstanding_yoy_change_pct: (latest annual diluted weighted-average shares ÷ prior year − 1) × 100. Positive = dilution, negative = buyback.
* exchange: listing exchange
* volume: daily share volume (from the screener)
* description: business description (from the company profile)

-------------

## Data Sources

All scripts rely solely on FMP endpoints. 

**master_stock_universe.py**
* **/stable/company-screener**: All columns

**active_stock_universe.py**
* **/stable/company-screener**: All columns

**large_actives_with_metrics.py**
* **/stable/company-screener**: symbol, company_name, market_cap_usd, industry, volume, exchange
* **stable/profile**: description, ipoDate
* **stable/income-statement?period=quarter (12Q)**: sales_ttm_usd, sales_growth_ttm_vs_prior_ttm_pct, sales_growth_latest_q_yoy_pct, sales_growth_ttm_accel_pp, sales_growth_4q_net_accel_pp, gross_profit_to_sales_ttm_pct
* stable/income-statement?period=annual (8y): gross_profit_to_sales_vs_5yr_trough_pp, shares_outstanding_yoy_change_pct
* **stable/cash-flow-statement?period=quarter**: fcf_to_sales_ttm_pct, total_debt_to_fcf
* **stable/cash-flow-statement?period=annual**: fcf_to_sales_vs_5yr_trough_pp
* **stable/balance-sheet-statement?period=quarter**: total_debt_to_fcf
* **stable/grades-consensus**: analyst_sell_pct, analyst_count
