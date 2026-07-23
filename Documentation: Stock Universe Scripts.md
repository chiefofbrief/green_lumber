# Documentation: Fetching All US Stocks

## Overview

There are three scripts which all run independently and create their own CSV file. 
* **master_stock_universe.py**: Captures all US stocks, including OTC, on the following exchanges: NASDAQ, NYSE, AMEX, CBOE, OTC, PNK. Each exchange is pulled in 3 type-slices (ETF / fund / common) to stay under the screener's 10,000-row-per-call cap; any slice still at the cap is re-split by isActivelyTrading (true/false). Partitioning is by type and trading state, never market cap, so null-market-cap names are never dropped.
* **active_stock_universe.py**: Filters the master universe to exclude ETFs, mutual funds, and stocks that are not actively trading: isEtf=false, isFund=false, isActivelyTrading=true. CBOE is dropped here (only master includes it); exchanges are NASDAQ, NYSE, AMEX, OTC, PNK.
* **large_actives_with_metrics.py**: Filters the active stock universe for market cap, trading volume, and sales, and adds a variety of additional metrics: marketCap ≥ $1B, dollar volume (price×volume) ≥ $1M/day, prior-TTM sales ≥ $10M USD.

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
* symbol
* company_name
* market_cap_usd
* ipo_date
* growth_score: 0.25·P(sales_growth_ttm_vs_prior_ttm_pct) + 0.25·P(sales_growth_latest_q_yoy_pct) + 0.25·P(sales_growth_ttm_accel_pp) + 0.25·P(sales_growth_q_accel_pp) — P(x) = percentile rank within the batch (0–100; blanks re-normalize)
* risk_score: higher = safer. 0.30·(100 − P(total_debt_to_sales_pct)) + 0.15·P(gross_profit_to_sales_ttm_pct) + 0.15·P(gross_profit_to_sales_yoy_change_pp) + 0.20·P(market_cap_usd) + 0.10·P(fcf_to_sales_ttm_pct) + 0.10·P(fcf_to_sales_yoy_change_pp)
* ev_to_sales_ttm: (market_cap_usd + total debt − cash) / sales_ttm_usd (total debt & cash from the latest quarter, converted to USD)
* pe_ratio_ttm: market_cap_usd / TTM net income (converted to USD; blank if net income ≤ 0)
* analyst_sell_pct: (sell + strongSell) / (strongBuy + buy + hold + sell + strongSell) × 100
* analyst_count: strongBuy + buy + hold + sell + strongSell
* industry
* description
* sales_ttm_usd: TTM sales (sum of the last 4 quarters), converted to USD at the spot FX rate
* sales_growth_ttm_vs_prior_ttm_pct: (TTM sales / prior-year TTM sales − 1) × 100
* sales_growth_latest_q_yoy_pct: (latest-quarter sales / the same quarter one year earlier − 1) × 100
* sales_growth_ttm_accel_pp: (recent TTM sales growth − prior-year TTM sales growth), in percentage points
* sales_growth_q_accel_pp: (latest-quarter YoY growth − previous-quarter YoY growth), in percentage points
* gross_profit_to_sales_ttm_pct: (TTM gross profit / TTM sales) × 100
* gross_profit_to_sales_yoy_change_pp: (TTM gross-profit/sales) − (prior-year TTM gross-profit/sales), in percentage points
* fcf_to_sales_ttm_pct: (TTM free cash flow / TTM sales) × 100
* fcf_to_sales_yoy_change_pp: (TTM fcf/sales) − (prior-year TTM fcf/sales), in percentage points
* total_debt_to_sales_pct: (total debt [latest quarter] / TTM sales) × 100
* sales_growth_vs_5yr_trough_pp: sales_growth_ttm_vs_prior_ttm_pct − lowest annual sales growth of the last 5 years — blank if < 5 years of history
* gross_profit_to_sales_vs_5yr_trough_pp: gross_profit_to_sales_ttm_pct − lowest annual gross-profit/sales of the last 5 years — blank if < 5 years
* fcf_to_sales_vs_5yr_trough_pp: fcf_to_sales_ttm_pct − lowest annual FCF/sales of the last 5 years — blank if < 5 years
* shares_outstanding_yoy_change_pct: (latest annual diluted weighted-average shares / prior year − 1) × 100 (positive = dilution, negative = buyback)
* exchange
* volume

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
* **stable/income-statement?period=quarter (12Q)**: sales_ttm_usd, sales_growth_ttm_vs_prior_ttm_pct, sales_growth_latest_q_yoy_pct, sales_growth_ttm_accel_pp, sales_growth_q_accel_pp, gross_profit_to_sales_ttm_pct, gross_profit_to_sales_yoy_change_pp
* stable/income-statement?period=annual (8y): sales_growth_vs_5yr_trough_pp, gross_profit_to_sales_vs_5yr_trough_pp, shares_outstanding_yoy_change_pct
* **stable/cash-flow-statement?period=quarter**: fcf_to_sales_ttm_pct, fcf_to_sales_yoy_change_pp
* **stable/cash-flow-statement?period=annual**: fcf_to_sales_vs_5yr_trough_pp
* **stable/balance-sheet-statement?period=quarter**: total_debt_to_sales_pct
* **stable/grades-consensus**: analyst_sell_pct, analyst_count
