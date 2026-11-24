# Strength

Inputs and output for the Strength pass. Figures are computed by `run_financials.py` from FMP statements fetched November 24, 2026 (raw files in `raw/`). TTM is the last four reported quarters, or the last two half-years for half-yearly reporters (LSEGY, RELX, SBGSY). FCF margin (last 5 FY) is free cash flow over sales for each of the last five fiscal years, oldest first. Share count change compares the basic weighted average share count in the latest period with the same period a year earlier. Debt / OCF is total debt (FMP's figure, which includes lease liabilities) divided by TTM operating cash flow, in years. Net debt or net cash is total debt minus cash and short-term investments, from the latest balance sheet, in the company's reporting currency. Gross margin vs 5-yr low is from the screener (mid-November 2026), as used in the Valuation pass. A dash means the figure is not available.

| # | Symbol | Company | OCF margin (TTM) | FCF margin (TTM) | FCF margin (last 5 FY) | Share count change (YoY) | Debt / OCF | Net debt or net cash | Gross margin vs 5-yr low | Strength |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | AAON | AAON, Inc. | 7.4% | -1.5% | FY2021 1.1% / FY2022 0.8% / FY2023 4.7% / FY2024 -0.3% / FY2025 -13.2% | -0.6% | 2.6 yrs | net debt 0.4B (USD) | -0.3pp |  |
| 2 | AMAT | Applied Materials, Inc. | 25.7% | 18.0% | FY2022 17.9% / FY2023 28.6% / FY2024 27.6% / FY2025 20.1% / FY2026 18.0% | -0.1% | 0.7 yrs | net cash 2.8B (USD) | +3.5pp |  |
| 3 | AMZN | Amazon.com, Inc. | 21.1% | -5.9% | FY2021 -3.1% / FY2022 -3.3% / FY2023 5.6% / FY2024 5.2% / FY2025 1.1% | +1.2% | 1.6 yrs | net debt 157.7B (USD) | +9.3pp |  |
| 4 | ANET | Arista Networks, Inc. | 44.1% | 42.2% | FY2021 32.3% / FY2022 10.2% / FY2023 34.1% / FY2024 52.5% / FY2025 47.2% | +0.3% | 0.0 yrs | net cash 14.4B (USD) | +1.8pp |  |
| 5 | APH | Amphenol Corporation | 19.6% | 15.5% | FY2021 10.8% / FY2022 14.2% / FY2023 17.2% / FY2024 14.1% / FY2025 19.0% | +1.0% | 2.8 yrs | net debt 12.6B (USD) | +7.5pp |  |
| 6 | AVGO | Broadcom Inc. | 45.6% | 44.2% | FY2021 48.5% / FY2022 49.1% / FY2023 49.2% / FY2024 37.6% / FY2025 42.1% | +1.1% | 1.5 yrs | net debt 35.4B (USD) | +7.4pp |  |
| 7 | CEG | Constellation Energy Corporation | 16.9% | 3.9% | FY2021 -13.6% / FY2022 -16.5% / FY2023 -31.0% / FY2024 -21.3% / FY2025 5.0% | +13.1% | 4.0 yrs | net debt 22.4B (USD) | +22.2pp |  |
| 8 | CLS | Celestica Inc. | 7.7% | 3.0% | FY2021 3.1% / FY2022 1.4% / FY2023 2.5% / FY2024 3.1% / FY2025 3.7% | +4.8% | 0.6 yrs | net cash 3.1B (USD) | +2.8pp |  |
| 9 | CRM | Salesforce, Inc. | 35.8% | 34.5% | FY2022 19.9% / FY2023 20.1% / FY2024 27.2% / FY2025 32.8% / FY2026 34.7% | -14.2% | 2.7 yrs | net debt 30.3B (USD) | +3.9pp |  |
| 10 | DDOG | Datadog, Inc. | 29.6% | 27.4% | FY2021 24.4% / FY2022 21.1% / FY2023 29.7% / FY2024 31.1% / FY2025 29.2% | +2.9% | 1.0 yrs | net cash 3.9B (USD) | +2.4pp |  |
| 11 | DELL | Dell Technologies Inc. | 8.0% | 5.7% | FY2022 7.4% / FY2023 0.5% / FY2024 6.7% / FY2025 2.0% / FY2026 7.5% | -4.9% | 2.8 yrs | net debt 22.9B (USD) | -0.2pp |  |
| 12 | EME | EMCOR Group, Inc. | 8.1% | 7.5% | FY2021 2.9% / FY2022 4.1% / FY2023 6.5% / FY2024 9.2% / FY2025 7.0% | -1.6% | 0.3 yrs | net cash 0.2B (USD) | +5.3pp |  |
| 13 | EPD | Enterprise Products Partners L.P. | 14.5% | 7.5% | FY2021 15.4% / FY2022 10.4% / FY2023 8.7% / FY2024 6.4% / FY2025 5.6% | -0.2% | 3.7 yrs | net debt 34.2B (USD) | +0.9pp |  |
| 14 | ETN | Eaton Corporation plc | 15.3% | 11.9% | FY2021 8.1% / FY2022 9.3% / FY2023 12.4% / FY2024 14.1% / FY2025 12.9% | -0.1% | 4.3 yrs | net debt 20.1B (USD) | +2.9pp |  |
| 15 | FFIV | F5, Inc. | 28.1% | 25.4% | FY2022 15.2% / FY2023 21.3% / FY2024 27.1% / FY2025 29.4% / FY2026 25.4% | -1.5% | 0.2 yrs | net cash 1.4B (USD) | +3.3pp |  |
| 16 | FIX | Comfort Systems USA, Inc. | 24.0% | 19.5% | FY2021 5.1% / FY2022 6.1% / FY2023 10.5% / FY2024 10.5% / FY2025 11.3% | -0.5% | 0.1 yrs | net cash 1.8B (USD) | +7.7pp |  |
| 17 | FTNT | Fortinet, Inc. | 46.8% | 43.5% | FY2021 36.0% / FY2022 32.8% / FY2023 32.6% / FY2024 31.6% / FY2025 32.7% | -2.8% | 0.1 yrs | net cash 4.3B (USD) | +4.3pp |  |
| 18 | GEV | GE Vernova Inc. | 43.6% | 38.9% | FY2021 -6.8% / FY2022 -2.1% / FY2023 1.3% / FY2024 4.9% / FY2025 9.7% | -2.2% | 0.1 yrs | net cash 13.9B (USD) | +10.1pp |  |
| 19 | GOOG | Alphabet Inc. | 38.1% | 4.2% | FY2021 26.0% / FY2022 21.2% / FY2023 22.6% / FY2024 20.8% / FY2025 18.2% | +1.4% | 0.8 yrs | net cash 123.2B (USD) | +5.5pp |  |
| 20 | INTU | Intuit Inc. | 42.3% | 41.3% | FY2022 29.2% / FY2023 33.5% / FY2024 29.0% / FY2025 32.4% / FY2026 40.4% | -4.3% | 0.8 yrs | net debt 2.4B (USD) | +2.8pp |  |
| 21 | KLAC | KLA Corporation | 31.1% | 27.8% | FY2022 32.6% / FY2023 31.7% / FY2024 30.9% / FY2025 30.8% / FY2026 27.7% | -0.9% | 1.3 yrs | net debt 1.3B (USD) | +1.7pp |  |
| 22 | LRCX | Lam Research Corporation | 29.0% | 25.0% | FY2022 14.8% / FY2023 26.8% / FY2024 28.6% / FY2025 29.4% / FY2026 21.1% | -1.1% | 0.5 yrs | net cash 3.7B (USD) | +6.4pp |  |
| 23 | LSEGY | London Stock Exchange Group plc | 41.2% | 39.6% | FY2021 29.7% / FY2022 22.9% / FY2023 33.7% / FY2024 27.0% / FY2025 37.6% | -6.6% | 3.4 yrs | net debt 9.2B (GBP) | +23.9pp |  |
| 24 | META | Meta Platforms, Inc. | 55.1% | 11.9% | FY2021 33.2% / FY2022 16.3% / FY2023 32.5% / FY2024 32.9% / FY2025 22.9% | +1.4% | 0.8 yrs | net debt 29.6B (USD) | +2.7pp |  |
| 25 | MSFT | Microsoft Corporation | 56.5% | 17.3% | FY2022 32.9% / FY2023 28.1% / FY2024 30.2% / FY2025 25.4% / FY2026 20.2% | -0.1% | 0.7 yrs | net debt 69.3B (USD) | -0.3pp |  |
| 26 | MU | Micron Technology, Inc. | 67.3% | 44.3% | FY2022 10.1% / FY2023 -39.4% / FY2024 0.5% / FY2025 4.5% / FY2026 44.3% | +0.9% | 0.1 yrs | net cash 38.3B (USD) | +89.8pp |  |
| 27 | NOW | ServiceNow, Inc. | 34.6% | 30.8% | FY2021 30.5% / FY2022 30.0% / FY2023 30.1% / FY2024 31.1% / FY2025 34.5% | -0.5% | 1.6 yrs | net debt 3.8B (USD) | -4.0pp |  |
| 28 | NVDA | NVIDIA Corporation | 43.9% | 41.1% | FY2022 30.2% / FY2023 14.1% / FY2024 44.4% / FY2025 46.6% / FY2026 44.8% | -0.9% | 0.2 yrs | net cash 59.6B (USD) | +17.7pp |  |
| 29 | NVT | nVent Electric plc | 14.6% | 12.1% | FY2021 13.6% / FY2022 15.2% / FY2023 17.3% / FY2024 18.9% / FY2025 9.6% | -0.6% | 3.0 yrs | net debt 1.2B (USD) | +0.7pp |  |
| 30 | ONTO | Onto Innovation Inc. | 19.9% | 18.9% | FY2021 20.7% / FY2022 11.8% / FY2023 18.3% / FY2024 21.7% / FY2025 29.8% | -0.1% | 5.6 yrs | net debt 0.2B (USD) | +2.0pp |  |
| 31 | PANW | Palo Alto Networks, Inc. | 37.8% | 34.3% | FY2022 32.6% / FY2023 38.2% / FY2024 38.6% / FY2025 37.6% / FY2026 35.8% | +20.6% | 0.6 yrs | net cash 0.4B (USD) | +1.6pp |  |
| 32 | PWR | Quanta Services, Inc. | 10.9% | 8.5% | FY2021 1.5% / FY2022 4.1% / FY2023 5.5% / FY2024 6.2% / FY2025 5.7% | +1.0% | 1.8 yrs | net debt 5.2B (USD) | +2.5pp |  |
| 33 | QLYS | Qualys, Inc. | 46.0% | 44.9% | FY2021 42.6% / FY2022 35.7% / FY2023 42.5% / FY2024 38.1% / FY2025 45.5% | -3.9% | 0.2 yrs | net cash 0.5B (USD) | +5.1pp |  |
| 34 | RELX | RELX Plc | 30.1% | 29.9% | FY2021 27.7% / FY2022 28.0% / FY2023 26.7% / FY2024 27.8% / FY2025 29.8% | -3.7% | 3.0 yrs | net debt 8.7B (GBP) | -0.3pp |  |
| 35 | SAP | SAP SE | 25.0% | 23.2% | FY2021 20.5% / FY2022 16.2% / FY2023 17.5% / FY2024 12.9% / FY2025 22.9% | -1.5% | 1.1 yrs | net debt 1.2B (EUR) | +0.6pp |  |
| 36 | SKHY | SK hynix Inc. | 61.9% | 45.8% | FY2021 14.7% / FY2022 -11.1% / FY2023 -12.4% / FY2024 19.8% / FY2025 25.5% | +4.5% | 0.1 yrs | net cash 58,406.6B (KRW) | +83.4pp |  |
| 37 | SNDK | Sandisk Corporation | 60.6% | 59.9% | FY2022 7.6% / FY2023 -15.3% / FY2024 -7.1% / FY2025 -1.6% / FY2026 56.8% | -0.7% | 0.0 yrs | net cash 4.9B (USD) | +72.9pp |  |
| 38 | TER | Teradyne, Inc. | 26.6% | 20.5% | FY2021 26.1% / FY2022 13.1% / FY2023 15.9% / FY2024 16.8% / FY2025 14.1% | -1.5% | 0.1 yrs | net cash 0.3B (USD) | +1.9pp |  |
| 39 | TSM | Taiwan Semiconductor Manufacturing Company Limited | 63.9% | 30.5% | FY2021 16.6% / FY2022 23.0% / FY2023 13.3% / FY2024 30.1% / FY2025 26.1% | +0.0% | 0.3 yrs | net cash 2,947.2B (TWD) | +14.2pp |  |
| 40 | TT | Trane Technologies plc | 18.0% | 16.4% | FY2021 9.7% / FY2022 7.6% / FY2023 11.8% / FY2024 14.0% / FY2025 13.2% | -0.5% | 1.0 yrs | net debt 3.0B (USD) | +3.9pp |  |
| 41 | VEEV | Veeva Systems Inc. | 48.2% | 47.5% | FY2022 40.5% / FY2023 35.6% / FY2024 37.4% / FY2025 38.9% / FY2026 43.4% | -0.5% | 0.1 yrs | net cash 7.1B (USD) | +3.6pp |  |
| 42 | VRT | Vertiv Holdings Co | 27.7% | 23.8% | FY2021 2.5% / FY2022 -4.6% / FY2023 11.2% / FY2024 14.2% / FY2025 18.4% | +0.9% | 0.9 yrs | net cash 0.4B (USD) | +9.7pp |  |
| 43 | VST | Vistra Corp. | 28.0% | 9.4% | FY2021 -10.3% / FY2022 -5.9% / FY2023 25.6% / FY2024 14.4% / FY2025 0.7% | -1.0% | 3.7 yrs | net debt 18.4B (USD) | +30.1pp |  |
| 44 | ZS | Zscaler, Inc. | 34.8% | 22.8% | FY2022 21.2% / FY2023 20.6% / FY2024 27.0% / FY2025 27.2% / FY2026 25.4% | +2.9% | 1.5 yrs | net cash 2.0B (USD) | -0.0pp |  |
| 45 | AMD | Advanced Micro Devices, Inc. | 20.1% | 15.5% | FY2021 19.6% / FY2022 13.2% / FY2023 4.9% / FY2024 9.3% / FY2025 19.4% | +0.6% | 1.0 yrs | net cash 6.9B (USD) | +8.8pp |  |
| 46 | APP | AppLovin Corporation | 64.4% | 64.1% | FY2021 12.9% / FY2022 14.6% / FY2023 57.4% / FY2024 65.0% / FY2025 71.9% | -1.4% | 0.7 yrs | net debt 0.3B (USD) | +33.4pp |  |
| 47 | ASML | ASML Holding N.V. | 57.6% | 53.6% | FY2021 53.2% / FY2022 34.0% / FY2023 11.8% / FY2024 32.1% / FY2025 33.9% | -1.1% | 0.1 yrs | net cash 10.8B (EUR) | +4.9pp |  |
| 48 | ATEN | A10 Networks, Inc. | 26.9% | 22.5% | FY2021 18.0% / FY2022 19.7% / FY2023 13.4% / FY2024 29.9% / FY2025 22.3% | +0.7% | 2.5 yrs | net cash 0.1B (USD) | +0.6pp |  |
| 49 | DT | Dynatrace, Inc. | 27.7% | 26.4% | FY2022 25.1% / FY2023 28.8% / FY2024 24.6% / FY2025 25.5% / FY2026 26.1% | -4.5% | 2.6 yrs | net cash 0.6B (USD) | +0.3pp |  |
| 50 | FIG | Figma, Inc. | 17.6% | 16.0% | FY2023 206.2% / FY2024 -9.2% / FY2025 23.3% | +32.0% | 0.4 yrs | net cash 1.6B (USD) | - |  |
| 51 | HUBB | Hubbell Incorporated | 16.8% | 14.1% | FY2021 10.8% / FY2022 9.2% / FY2023 13.3% / FY2024 14.4% / FY2025 15.0% | -0.6% | 4.6 yrs | net debt 4.8B (USD) | +7.9pp |  |
| 52 | HUBS | HubSpot, Inc. | 25.3% | 21.6% | FY2021 13.6% / FY2022 10.5% / FY2023 11.6% / FY2024 21.3% / FY2025 22.6% | -6.1% | 0.2 yrs | net cash 1.1B (USD) | +2.9pp |  |
| 53 | KC | Kingsoft Cloud Holdings Limited | 55.8% | 12.7% | FY2021 -15.9% / FY2022 -15.3% / FY2023 -30.3% / FY2024 -39.2% / FY2025 -9.8% | +20.8% | 1.1 yrs | net debt 2.1B (CNY) | +11.2pp |  |
| 54 | MDB | MongoDB, Inc. | 24.3% | 24.0% | FY2022 -0.1% / FY2023 -1.6% / FY2024 6.9% / FY2025 6.0% / FY2026 20.3% | -0.7% | 0.0 yrs | net cash 2.4B (USD) | +2.4pp |  |
| 55 | MELI | MercadoLibre, Inc. | 36.1% | 31.8% | FY2021 5.0% / FY2022 23.1% / FY2023 30.7% / FY2024 34.0% / FY2025 37.3% | -0.0% | 0.9 yrs | net debt 5.6B (USD) | -0.5pp |  |
| 56 | MOD | Modine Manufacturing Company | 3.7% | -1.0% | FY2022 -1.4% / FY2023 2.5% / FY2024 5.3% / FY2025 5.0% / FY2026 3.3% | +2.3% | 6.4 yrs | net debt 0.7B (USD) | +6.6pp |  |
| 57 | MRVL | Marvell Technology, Inc. | 23.3% | 18.3% | FY2022 14.2% / FY2023 18.1% / FY2024 18.5% / FY2025 24.1% / FY2026 17.0% | +4.0% | 2.4 yrs | net debt 1.4B (USD) | +10.1pp |  |
| 58 | NTNX | Nutanix, Inc. | 32.1% | 29.5% | FY2022 1.2% / FY2023 11.1% / FY2024 27.8% / FY2025 29.6% / FY2026 29.5% | +0.7% | 1.7 yrs | net cash 0.8B (USD) | +7.1pp |  |
| 59 | RDDT | Reddit, Inc. | 39.0% | 38.8% | FY2021 -27.3% / FY2022 -15.0% / FY2023 -10.6% / FY2024 16.6% / FY2025 31.1% | +2.4% | 0.0 yrs | net cash 3.0B (USD) | +7.3pp |  |
| 60 | SANM | Sanmina Corporation | 6.5% | 3.7% | FY2022 2.4% / FY2023 0.5% / FY2024 3.0% / FY2025 5.8% / FY2026 3.7% | -0.1% | 2.5 yrs | net debt 0.7B (USD) | +1.7pp |  |
| 61 | SBGSY | Schneider Electric S.E. | 17.2% | 14.7% | FY2021 9.5% / FY2022 9.5% / FY2023 12.7% / FY2024 12.1% / FY2025 12.1% | -0.6% | 2.6 yrs | net debt 14.7B (EUR) | +2.5pp |  |
| 62 | SMCI | Super Micro Computer, Inc. | -11.7% | -12.0% | FY2022 -9.4% / FY2023 8.8% / FY2024 -17.4% / FY2025 7.0% / FY2026 -17.8% | +0.2% | n/a (OCF negative) | net debt 1.7B (USD) | +0.8pp |  |
| 63 | SMERY | Siemens Energy AG | 22.3% | 17.8% | FY2022 3.7% / FY2023 1.3% / FY2024 4.0% / FY2025 10.5% / FY2026 18.1% | +0.0% | 0.3 yrs | net cash 9.8B (EUR) | +19.8pp |  |
| 64 | SNOW | Snowflake Inc. | 23.1% | 22.0% | FY2022 6.7% / FY2023 24.0% / FY2024 27.8% / FY2025 24.4% / FY2026 23.9% | +4.6% | 2.2 yrs | net debt 0.4B (USD) | +4.6pp |  |
| 65 | TEAM | Atlassian Corporation | 24.5% | 24.1% | FY2022 26.8% / FY2023 23.8% / FY2024 32.5% / FY2025 27.1% / FY2026 20.1% | -4.2% | 0.7 yrs | net debt 0.1B (USD) | +4.0pp |  |
| 66 | TWLO | Twilio Inc. | 20.3% | 19.0% | FY2021 -5.2% / FY2022 -8.7% / FY2023 8.8% / FY2024 14.7% / FY2025 18.7% | +0.8% | 0.9 yrs | net cash 1.8B (USD) | +1.2pp |  |
| 67 | ZETA | Zeta Global Holdings Corp. | 15.9% | 15.1% | FY2021 3.8% / FY2022 6.6% / FY2023 7.5% / FY2024 9.2% / FY2025 14.2% | +5.1% | 0.9 yrs | net cash 0.1B (USD) | +9.3pp |  |
| 68 | ALAB | Astera Labs, Inc. Common Stock | 28.1% | 22.1% | FY2022 -49.8% / FY2023 -13.4% / FY2024 25.8% / FY2025 33.1% | +4.0% | 0.0 yrs | net cash 1.4B (USD) | - |  |
| 69 | AR | Antero Resources Corporation | 37.1% | 21.2% | FY2021 26.7% / FY2022 34.8% / FY2023 19.3% / FY2024 18.1% / FY2025 24.8% | -0.4% | 2.1 yrs | net debt 4.7B (USD) | +22.0pp |  |
| 70 | ASMIY | ASM International N.V. | 29.6% | 19.7% | FY2021 12.9% / FY2022 13.8% / FY2023 15.9% / FY2024 18.2% / FY2025 26.8% | +0.1% | 0.1 yrs | net cash 1.3B (EUR) | +4.5pp |  |
| 71 | ASX | ASE Technology Holding Co., Ltd. | 16.2% | -14.1% | FY2021 1.4% / FY2022 4.6% / FY2023 8.9% / FY2024 0.5% / FY2025 -3.1% | +1.3% | 0.0 yrs | net debt 0.0B (TWD) | +5.9pp |  |
| 72 | ATEYY | Advantest Corporation | 34.7% | 32.2% | FY2021 14.6% / FY2022 8.3% / FY2023 2.5% / FY2024 34.2% / FY2025 26.8% | -1.1% | 0.2 yrs | net cash 296.3B (JPY) | +17.6pp |  |
| 73 | BE | Bloom Energy Corporation | 18.0% | 11.4% | FY2021 -11.4% / FY2022 -25.7% / FY2023 -34.2% / FY2024 2.2% / FY2025 2.8% | +25.5% | 4.0 yrs | net debt 0.3B (USD) | +20.0pp |  |
| 74 | CIEN | Ciena Corporation | 17.5% | 13.5% | FY2021 12.8% / FY2022 -7.1% / FY2023 1.4% / FY2024 9.4% / FY2025 13.9% | +0.2% | 0.2 yrs | net cash 2.4B (USD) | +2.0pp |  |
| 75 | CRDO | Credo Technology Group Holding Ltd | 31.4% | 27.6% | FY2022 -45.5% / FY2023 -25.2% / FY2024 8.9% / FY2025 6.6% / FY2026 30.5% | +8.2% | 0.0 yrs | net cash 0.7B (USD) | +9.4pp |  |
| 76 | ECG | Everus Construction Group, Inc. | 6.8% | 5.1% | FY2021 2.8% / FY2022 -2.3% / FY2023 4.8% / FY2024 4.0% / FY2025 2.4% | -0.1% | 2.2 yrs | net debt 0.4B (USD) | +3.4pp |  |
| 77 | ENB | Enbridge Inc. | 13.6% | 0.4% | FY2021 2.5% / FY2022 12.0% / FY2023 21.4% / FY2024 10.6% / FY2025 4.8% | +0.6% | 9.3 yrs | net debt 109.4B (CAD) | -3.8pp |  |
| 78 | FICO | Fair Isaac Corporation | 42.3% | 41.9% | FY2022 36.6% / FY2023 30.7% / FY2024 35.4% / FY2025 38.7% / FY2026 42.2% | -10.3% | 4.9 yrs | net debt 5.1B (USD) | +8.1pp |  |
| 79 | FN | Fabrinet | 3.4% | -3.7% | FY2022 1.5% / FY2023 5.7% / FY2024 12.7% / FY2025 6.0% / FY2026 0.1% | +0.3% | 0.4 yrs | net cash 0.7B (USD) | -0.0pp |  |
| 80 | FORM | FormFactor, Inc. | 26.2% | 18.5% | FY2021 9.5% / FY2022 8.9% / FY2023 1.3% / FY2024 10.4% / FY2025 1.5% | +1.2% | 0.1 yrs | net cash 0.4B (USD) | +10.5pp |  |
| 81 | IESC | IES Holdings, Inc. | 8.1% | 4.5% | FY2022 -0.6% / FY2023 5.7% / FY2024 6.6% / FY2025 6.5% / FY2026 4.5% | +0.3% | 0.2 yrs | net cash 0.4B (USD) | +11.2pp |  |
| 82 | INOD | Innodata Inc. | 37.3% | 33.6% | FY2021 1.1% / FY2022 -9.8% / FY2023 0.4% / FY2024 16.0% / FY2025 14.2% | +8.0% | 0.0 yrs | net cash 0.2B (USD) | +6.3pp |  |
| 83 | KLIC | Kulicke and Soffa Industries, Inc. | 6.1% | 4.2% | FY2022 24.4% / FY2023 17.4% / FY2024 2.1% / FY2025 14.7% / FY2026 4.2% | +0.4% | 0.5 yrs | net cash 0.5B (USD) | +10.1pp |  |
| 84 | LGN | Legence Corp. Class A Common stock | 8.5% | 6.9% | FY2022 0.1% / FY2023 1.0% / FY2024 0.5% / FY2025 8.6% | +31.5% | 3.2 yrs | net debt 0.9B (USD) | - |  |
| 85 | LITE | Lumentum Holdings Inc. | 25.7% | 9.5% | FY2022 21.5% / FY2023 2.9% / FY2024 -8.0% / FY2025 -6.4% / FY2026 10.0% | +31.6% | 1.5 yrs | net cash 0.5B (USD) | +27.4pp |  |
| 86 | LSCC | Lattice Semiconductor Corporation | 36.0% | 31.5% | FY2021 30.6% / FY2022 32.6% / FY2023 33.8% / FY2024 23.5% / FY2025 25.3% | +2.9% | 3.2 yrs | net debt 0.8B (USD) | +5.1pp |  |
| 87 | MYRG | MYR Group Inc. | 5.8% | 3.2% | FY2021 3.4% / FY2022 3.0% / FY2023 -0.4% / FY2024 0.3% / FY2025 6.3% | +0.3% | 1.1 yrs | net debt 0.3B (USD) | +4.3pp |  |
| 88 | OKE | ONEOK, Inc. | 13.7% | 5.9% | FY2021 10.7% / FY2022 7.6% / FY2023 16.0% / FY2024 13.2% / FY2025 7.3% | +0.6% | 4.8 yrs | net debt 28.3B (USD) | +6.1pp |  |
| 89 | OKTA | Okta, Inc. | 32.1% | 31.6% | FY2022 6.7% / FY2023 3.4% / FY2024 21.6% / FY2025 28.0% / FY2026 29.6% | -0.7% | 0.1 yrs | net cash 2.2B (USD) | +8.6pp |  |
| 90 | PLTR | Palantir Technologies Inc. | 56.2% | 55.6% | FY2021 20.8% / FY2022 9.6% / FY2023 31.3% / FY2024 39.8% / FY2025 46.9% | +1.8% | 0.1 yrs | net cash 10.3B (USD) | +6.8pp |  |
| 91 | SHOP | Shopify Inc. | 18.9% | 18.8% | FY2021 10.5% / FY2022 -3.3% / FY2023 12.8% / FY2024 18.0% / FY2025 17.4% | -1.0% | 0.1 yrs | net cash 4.5B (USD) | -0.6pp |  |
| 92 | SPXC | SPX Technologies, Inc. | 14.4% | 8.7% | FY2021 13.5% / FY2022 -10.5% / FY2023 10.6% / FY2024 12.5% / FY2025 10.6% | +4.0% | 3.6 yrs | net debt 1.2B (USD) | +4.5pp |  |
| 93 | ADSK | Autodesk, Inc. | 37.2% | 36.4% | FY2022 33.4% / FY2023 40.5% / FY2024 23.3% / FY2025 25.6% / FY2026 33.4% | -1.4% | 1.3 yrs | net cash 0.5B (USD) | +0.8pp |  |
| 94 | AGYS | Agilysys, Inc. | 23.9% | 23.3% | FY2022 16.8% / FY2023 13.7% / FY2024 16.9% / FY2025 19.0% / FY2026 21.3% | +0.9% | 0.2 yrs | net cash 0.1B (USD) | +2.3pp |  |
| 95 | AMPL | Amplitude, Inc. | 8.6% | 8.0% | FY2021 -20.9% / FY2022 -4.7% / FY2023 8.1% / FY2024 3.9% / FY2025 8.2% | -4.1% | 0.1 yrs | net cash 0.1B (USD) | +1.6pp |  |
| 96 | APPF | AppFolio Inc. | 26.1% | 25.9% | FY2021 0.7% / FY2022 4.0% / FY2023 7.5% / FY2024 23.4% / FY2025 25.1% | -1.3% | 0.1 yrs | net cash 0.3B (USD) | +4.0pp |  |
| 97 | AVPT | AvePoint, Inc. | 20.8% | 19.8% | FY2021 1.3% / FY2022 -2.7% / FY2023 11.5% / FY2024 26.0% / FY2025 19.4% | -0.7% | 0.2 yrs | net cash 0.4B (USD) | +1.4pp |  |
| 98 | BAND | Bandwidth Inc. | 13.1% | 10.3% | FY2021 -2.8% / FY2022 -5.1% / FY2023 3.2% / FY2024 9.3% / FY2025 8.9% | +6.5% | 4.7 yrs | net debt 0.4B (USD) | -0.7pp |  |
| 99 | ESTC | Elastic N.V. | 19.8% | 19.6% | FY2022 -0.2% / FY2023 3.1% / FY2024 11.5% / FY2025 17.7% / FY2026 18.5% | -0.7% | 1.6 yrs | net cash 0.8B (USD) | +3.2pp |  |
| 100 | EXLS | ExlService Holdings, Inc. | 13.9% | 11.6% | FY2021 13.1% / FY2022 8.6% / FY2023 9.7% / FY2024 12.1% / FY2025 14.3% | -5.4% | 1.9 yrs | net debt 0.3B (USD) | +1.9pp |  |
| 101 | FROG | JFrog Ltd. | 33.5% | 32.3% | FY2021 11.5% / FY2022 6.0% / FY2023 20.6% / FY2024 25.2% / FY2025 26.8% | +5.5% | 0.5 yrs | net cash 0.8B (USD) | +1.6pp |  |
| 102 | FRSH | Freshworks Inc. | 28.8% | 28.4% | FY2021 0.6% / FY2022 -3.0% / FY2023 13.1% / FY2024 20.3% / FY2025 28.2% | -8.5% | 0.1 yrs | net cash 0.7B (USD) | +6.2pp |  |
| 103 | FSLY | Fastly, Inc. | 18.2% | 6.8% | FY2021 -25.1% / FY2022 -34.7% / FY2023 -6.3% / FY2024 -3.8% / FY2025 10.5% | +8.0% | 3.1 yrs | net debt 0.0B (USD) | +14.2pp |  |
| 104 | GTLB | GitLab Inc. | 21.2% | 20.3% | FY2022 -21.1% / FY2023 -19.7% / FY2024 5.8% / FY2025 -8.9% / FY2026 23.2% | +1.7% | 0.0 yrs | net cash 1.3B (USD) | -1.6pp |  |
| 105 | GWRE | Guidewire Software, Inc. | 21.1% | 19.7% | FY2022 -7.3% / FY2023 2.3% / FY2024 18.1% / FY2025 24.5% / FY2026 25.6% | -1.8% | 2.3 yrs | net cash 0.0B (USD) | +17.8pp |  |
| 106 | INTA | Intapp, Inc. | 26.9% | 25.3% | FY2022 5.0% / FY2023 5.6% / FY2024 15.0% / FY2025 24.2% / FY2026 23.6% | -4.1% | 0.1 yrs | net cash 0.1B (USD) | +13.0pp |  |
| 107 | IOT | Samsara Inc. | 15.6% | 13.8% | FY2022 -44.6% / FY2023 -20.9% / FY2024 -2.4% / FY2025 8.9% / FY2026 12.8% | +2.5% | 0.2 yrs | net cash 0.8B (USD) | +5.4pp |  |
| 108 | MNDY | monday.com Ltd. | 17.1% | 15.7% | FY2021 0.8% / FY2022 1.6% / FY2023 28.1% / FY2024 30.4% / FY2025 25.2% | -17.6% | 0.8 yrs | net cash 0.9B (USD) | +1.4pp |  |
| 109 | NTAP | NetApp, Inc. | 25.7% | 22.3% | FY2022 15.6% / FY2023 13.6% / FY2024 24.4% / FY2025 20.4% / FY2026 27.0% | -2.5% | 1.3 yrs | net cash 1.0B (USD) | +4.5pp |  |
| 110 | NTSK | Netskope, Inc. Class A Common Stock | -5.1% | -8.5% | FY2023 -51.2% / FY2024 -28.1% / FY2025 2.1% | +6.0% | n/a (OCF negative) | net cash 0.3B (USD) | - |  |
| 111 | PCOR | Procore Technologies, Inc. | 25.2% | 19.1% | FY2021 1.8% / FY2022 -5.1% / FY2023 4.9% / FY2024 15.4% / FY2025 16.3% | +0.3% | 2.6 yrs | net debt 0.4B (USD) | +1.6pp |  |
| 112 | PL | Planet Labs PBC | 31.1% | 6.2% | FY2022 -43.6% / FY2023 -45.3% / FY2024 -42.2% / FY2025 -24.0% / FY2026 18.7% | +18.2% | 3.8 yrs | net cash 0.4B (USD) | +18.7pp |  |
| 113 | RBRK | Rubrik, Inc. | 22.1% | 19.9% | FY2022 -20.4% / FY2023 -2.5% / FY2024 -2.7% / FY2025 3.5% / FY2026 19.2% | +5.1% | 3.3 yrs | net cash 0.6B (USD) | +26.9pp |  |
| 114 | RDVT | Red Violet, Inc. | 32.3% | 21.8% | FY2021 8.4% / FY2022 6.8% / FY2023 9.8% / FY2024 31.6% / FY2025 31.9% | +9.4% | 0.1 yrs | net cash 0.1B (USD) | +13.0pp |  |
| 115 | S | SentinelOne, Inc. | 5.2% | 3.5% | FY2022 -51.7% / FY2023 -50.2% / FY2024 -14.0% / FY2025 0.8% / FY2026 7.6% | +2.5% | 0.0 yrs | net cash 0.7B (USD) | +13.2pp |  |
| 116 | SAIL | SailPoint, Inc. | 17.2% | 15.6% | FY2022 -2.9% / FY2023 -59.3% / FY2024 -36.4% / FY2025 -13.9% / FY2026 4.8% | +2.2% | 0.0 yrs | net cash 0.3B (USD) | +15.7pp |  |
| 117 | TEM | Tempus AI, Inc. | -7.2% | -10.0% | FY2021 -86.8% / FY2022 -58.2% / FY2023 -46.8% / FY2024 -30.5% / FY2025 -19.3% | +3.6% | n/a (OCF negative) | net debt 0.8B (USD) | +32.0pp |  |
| 118 | TOST | Toast, Inc. | 9.3% | 8.4% | FY2021 -1.0% / FY2022 -6.9% / FY2023 2.4% / FY2024 6.2% / FY2025 9.9% | -1.0% | 0.0 yrs | net cash 1.9B (USD) | +8.5pp |  |
| 119 | TTAN | ServiceTitan, Inc. | 13.2% | 10.9% | FY2023 -45.5% / FY2024 -13.7% / FY2025 2.0% / FY2026 8.9% | +5.3% | 0.3 yrs | net cash 0.4B (USD) | - |  |
| 120 | VRNS | Varonis Systems, Inc. | 18.6% | 16.4% | FY2021 -0.8% / FY2022 0.1% / FY2023 10.9% / FY2024 19.7% / FY2025 21.6% | +0.0% | 3.9 yrs | net cash 0.1B (USD) | -2.8pp |  |
| 121 | WAY | Waystar Holding Corp. | 24.9% | 20.9% | FY2021 15.9% / FY2022 12.1% / FY2023 3.8% / FY2024 15.1% / FY2025 25.8% | +10.1% | 4.7 yrs | net debt 1.2B (USD) | +2.9pp |  |
| 122 | WK | Workiva Inc. | 22.4% | 22.2% | FY2021 10.4% / FY2022 1.4% / FY2023 10.9% / FY2024 11.7% / FY2025 15.6% | -3.0% | 3.2 yrs | net cash 0.1B (USD) | +5.1pp |  |
| 123 | YOU | Clear Secure, Inc. | 46.2% | 43.0% | FY2021 16.0% / FY2022 31.2% / FY2023 32.4% / FY2024 36.8% / FY2025 38.1% | +5.5% | 0.2 yrs | net cash 0.5B (USD) | +8.8pp |  |
| 124 | BRZE | Braze, Inc. | 11.1% | 10.0% | FY2022 -16.7% / FY2023 -11.0% / FY2024 -0.6% / FY2025 4.0% / FY2026 8.4% | +4.2% | 1.0 yrs | net cash 0.3B (USD) | -0.7pp |  |
| 125 | CDNS | Cadence Design Systems, Inc. | 32.1% | 28.8% | FY2021 34.6% / FY2022 31.4% / FY2023 30.5% / FY2024 24.1% / FY2025 30.0% | +1.0% | 1.4 yrs | net debt 1.4B (USD) | -0.4pp |  |
| 126 | DUOL | Duolingo, Inc. | 36.9% | 33.9% | FY2021 2.2% / FY2022 13.0% / FY2023 28.3% / FY2024 36.5% / FY2025 35.6% | +1.9% | 0.2 yrs | net cash 1.3B (USD) | +0.9pp |  |
| 127 | KVYO | Klaviyo, Inc. | 18.7% | 15.7% | FY2021 -12.7% / FY2022 -8.8% / FY2023 15.8% / FY2024 15.9% / FY2025 15.4% | -5.2% | 0.5 yrs | net cash 0.6B (USD) | +2.7pp |  |
| 128 | NU | Nu Holdings Ltd. (Nubank) | -15.0% | -15.2% | FY2021 -195.2% / FY2022 14.2% / FY2023 14.2% / FY2024 20.0% / FY2025 22.0% | -0.1% | n/a (OCF negative) | net cash 35.2B (USD) | - |  |
| 129 | SNPS | Synopsys, Inc. | 31.2% | 29.2% | FY2021 33.3% / FY2022 34.7% / FY2023 28.5% / FY2024 21.0% / FY2025 19.1% | +19.6% | 3.7 yrs | net debt 7.2B (USD) | -4.6pp |  |
| 130 | U | Unity Software Inc. | 28.5% | 27.8% | FY2021 -13.8% / FY2022 -8.4% / FY2023 8.2% / FY2024 15.1% / FY2025 21.8% | +4.1% | 3.7 yrs | net cash 0.3B (USD) | +1.2pp |  |
