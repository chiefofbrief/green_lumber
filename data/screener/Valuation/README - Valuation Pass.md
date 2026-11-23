# Valuation Pass

## Context
I'm building a watchlist of AI companies. The working list is `data/screener/AI Watchlist (working).md` (130 companies). Earlier passes wrote a potential growth read and a news sentiment summary for each company. This pass writes one read per company on its valuation. It is one of several separate pieces of data; it is not the full analysis of the company. Each company is assessed on its own, without comparing it to others.

## The file
`data/screener/Valuation/Valuation.md` has one row per company:
- **Inputs:** Symbol, Company, **EV/sales** and **P/E** (at prices as of the November 20, 2026 close), **1-yr price change**, **vs 52-week high**, **Gross margin vs 5-yr low**, **News Sentiment** and **Potential growth**.
- **Output, empty until filled:** **Valuation**.

## Guidance
**Valuation** asks one question: how much of the expected growth is already in the price? We want companies where the price does not already reflect all of it. Answer it by working through the figures together. No single figure answers it alone, and each one changes how the others should be read.

**Start with what the market is paying.** EV/sales and P/E show how much investors pay for each dollar of sales and of earnings. EV/sales leads, because every company has it. P/E is blank when net income is zero or negative, and can be very high when earnings are thin or a company has only just turned profitable, so use it alongside EV/sales where earnings are meaningful. P/E uses reported (GAAP) net income over the last four quarters, so acquisition costs or one-off charges can push it up. On their own, the multiples only describe the price. What matters is what that price is buying.

**Then set the price against the growth.** The Potential growth read says how much growth is expected and how much is still ahead. A high multiple can be justified when exceptional growth is still ahead. The same multiple for growth that is modest or already fully visible means much of it is already priced in. Extreme multiples leave little room for a shortfall, even when growth is strong.

**Then check whether today's margins flatter the multiples.** They are measured at current margins. Gross margin vs 5-yr low shows how far the last four quarters' gross margin is above its lowest yearly level of the last five years. A negative figure means the last four quarters are below every yearly level of the last five years, so margins are not flattering the multiples. If it is far above, the multiples look cheaper than they would at normal margins, so ask what the price implies if margins fall back. A low P/E may mean the market is already pricing that fall.

**Then look at how the market got here.** The 1-year price change and the distance from the 52-week high show how far the price has already moved, and News Sentiment shows why. Read together with the growth, they show whether a move reflects mood or a real change in the business:
- **A large fall with growth still intact and pessimistic sentiment** may mean the price has fallen behind the business.
- **A large fall that comes with weakening growth** may be justified.
- **A large rise with optimistic sentiment** may mean much is already priced in.

**End with the overall judgment:** how much of the expected growth appears to be in the price, and why.

## Steps
1. Find the first row where **Valuation** is empty. Start there.
2. For each row, write **Valuation**: a paragraph or two, usually about 200-300 words (longer if the company genuinely needs it), working through the guidance above and ending with the overall judgment. State the figures you rely on.
3. Do five rows, then stop and ask whether to continue.

## Rules
- Base the read on the row's inputs and the guidance above. Inferences are fine if they are reasonable, supported by the inputs and worded as inferences; mark anything drawn from your own knowledge as such.
- A dash means the figure is not available, not zero.
- The news predates the November 20 prices. Where they differ, use the input figures for anything priced, and the news for context and reasons.
- Multiples worked out from the inputs, such as EV/sales on annualized latest-quarter revenue, are fine alongside the given figures if you say how you got them. They do not replace the given figures.
- Write in complete sentences, without a summary rating or label.
- Do not compare the company with others, and do not assess strength or whether the company belongs on the watchlist.
- Do not use the `|` character in a cell.
- Do not commit or push unless asked.
