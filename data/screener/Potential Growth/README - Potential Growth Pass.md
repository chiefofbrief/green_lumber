# Potential Growth Pass

## Context
I'm building a watchlist of AI companies. The working list is `data/screener/AI Watchlist (working).md` (130 companies). Earlier passes described each company's role in AI (from its description and three months of news) and its current sales growth. This pass uses them to write one read per company on its potential growth. It is one of several separate pieces of data; it is not the full analysis of the company. Each company is assessed on its own, without comparing it to others.

## The file
`data/screener/Potential Growth/Potential Growth.md` has one row per company:
- **Inputs:** Symbol, Company, **Sub-sectors**, **AI Role**, **Current growth**, **Sales TTM**, and **Market cap** (mid-November 2026).
- **Output, empty until filled:** **Potential growth**.

## Guidance
**Potential growth** is the growth expected over the next 1 to 2 years. It rests on four things, read together:
- **Where the growth is in the company's sub-sectors.** Take this from the Upside subsection of each of its sub-sectors in `AI Sub-Sectors.md`, with the description above it as context.
- **The company's position.** From AI Role: what the company does in AI, whether that sits where the Upside says demand is growing, and how much of its business it is. The growth in a sub-sector does not reach every company in it evenly, and the more of the business it is, the more of the company's own growth depends on it.
- **Its size relative to the opportunity.** The same opportunity adds far more to a small company's growth than to a large one's, so weigh it against the company's sales (Sales TTM). Market cap is useful context alongside it, since it is how investors usually gauge a company's size, but judge the effect on growth against sales.
- **Its current growth.** From the Current growth read: whether the company is already capturing the upside. Strong current growth in a well-placed company suggests it is. Weak current growth may mean it isn't, or that the upside hasn't arrived yet. If the read notes margins far above history, part of the growth may be temporary.

The read should say how much of the potential growth is already visible in current growth and how much is still ahead.

**Timing.** The upside in the digital sub-sectors may come quickly or slowly. Do not assume it comes later than in the physical sub-sectors, and do not mark a company down on that assumption.

## Steps
1. Before the first row, read `AI Sub-Sectors.md` in full.
2. Find the first row where **Potential growth** is empty. Start there.
3. For each row, write **Potential growth**: a short paragraph or two weighing the four things above, ending with how much of the potential growth is already visible in current growth and how much is still ahead.
4. Do five rows, then stop and ask whether to continue.

## Rules
- Base the read on the row's inputs and `AI Sub-Sectors.md`. Inferences are fine if they are reasonable, supported by the inputs and worded as inferences; mark anything drawn from your own knowledge as such.
- Leave out the sub-sectors' downsides; they are assessed separately.
- A dash means the figure is not available, not zero.
- Write in complete sentences, without a summary rating or label.
- Do not compare the company with others, and do not assess valuation, strength or whether the company belongs on the watchlist.
- Do not use the `|` character in a cell.
- Do not commit or push unless asked.
