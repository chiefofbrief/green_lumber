# AI Role Pass

## Context
I'm building a watchlist of AI companies. The working list is `data/screener/AI Watchlist (working).md` (130 companies). An earlier pipeline tagged each company with AI sub-sectors from `AI Sub-Sectors.md`, but it judged them from short company descriptions, which were often incomplete. Since then, a news pass collected three months of news per company and summarized what each company is doing in AI (the **News AI** column). This pass uses that to describe each company's role in AI more accurately. It is one of several separate pieces of data; it is not the full analysis of the company.

## The file
`data/screener/AI Role/AI Role.md` has one row per company:
- **Inputs:** Symbol, Company, **Previous sub-sectors** (from the earlier pipeline, with its A/B fit tier: A meant the sub-sector is central to the business, B a meaningful part), **Description** (from the screener), **News AI** (from the news pass).
- **Outputs, empty until filled:** **Sub-sectors** and **AI Role**.

## Steps
1. Before the first row, read `AI Sub-Sectors.md` in full. It describes the twelve sub-sectors and the kinds of companies in each.
2. Find the first row where **Sub-sectors** is empty. Start there.
3. For each row, read its Previous sub-sectors, Description and News AI, then fill in:
   - **Sub-sectors:** the sub-sectors from `AI Sub-Sectors.md` the company belongs to, as a plain comma-separated list using these names: networking, power, electrical, wafers, cooling, data, trust, runtime, processors, racks, memory, tools. Start from the previous sub-sectors, then add, drop or keep each based on the description and the news. No tiers. If none fit, write "none".
   - **AI Role:** a short paragraph or two on what the company does in AI: its products or services, its customers, how much of its business that is, and how important a player it is in each of its sub-sectors. Cite the evidence (figures, named products, customers, dates) and say whether it comes from the description or the news.
4. Do five rows, then stop and ask whether to continue.

## Rules
- Use only the description and News AI. Do not add facts or conclusions they do not support. Where they are thin or conflict, say so.
- Write in complete sentences.
- Do not assess growth, valuation or whether the company belongs on the watchlist.
- Do not use the `|` character in a cell.
- Do not commit or push unless asked.
