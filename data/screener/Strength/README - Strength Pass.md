# Strength Pass

## Context
I'm building a watchlist of AI companies. The working list is `data/screener/AI Watchlist (working).md` (130 companies). Earlier passes wrote reads on each company's AI role, growth and valuation. This pass writes one read per company on its financial strength. It is one of several separate pieces of data; it is not the full analysis of the company. Each company is assessed on its own, without comparing it to others.

## The file
`data/screener/Strength/Strength.md` has one row per company:
- **Inputs:** Symbol, Company, **OCF margin (TTM)**, **FCF margin (TTM)**, **SBC (% of sales, TTM)**, **FCF margin (last 5 FY)**, **Share count change (YoY)**, **Debt / OCF**, **Net debt or net cash** and **Gross margin vs 5-yr low**. The file's header says how each is calculated.
- **Output, empty until filled:** **Strength**.

## Guidance
**Strength** asks one question: can the company keep funding its own growth from the cash its business generates, in good times and in a downturn? Answer it in three parts, each built on the one before: how much the company reinvests and whether its own cash pays for it; how dependable that cash is; and when the cash falls short, what fills the gap and whether it could hold up in a downturn. No single figure answers any part alone, and each one changes how the others should be read.

### How much it reinvests, and whether its own cash pays for it
**Start with whether operations generate cash.** OCF margin is the cash the business generates from operations as a share of sales. It is harder to dress up than earnings: a company can flatter its profits with accounting choices, but not its cash. Negative OCF means the business itself is consuming cash and has to be funded from cash on hand, new debt or new shares.

**Then see how much of it goes back into the business.** FCF margin is what remains after capital spending, so the gap between OCF and FCF is how much the company is reinvesting in equipment, facilities and capacity. Heavy investment funded by strong operating cash is very different from operating cash burn: a company with strong OCF and negative FCF is choosing to invest from a position of strength, while a company with negative OCF has no such choice. Capital intensity differs by industry. A manufacturer or infrastructure company has to spend more on equipment to grow than a software company, so a thin FCF margin is not weakness on its own if OCF is healthy. The gap shows capital spending only. Spending on research and development is already taken out of OCF, and acquisitions do not appear in it, so a small gap does not mean a company is not investing.

**Then see how much of that cash is real.** Stock-based compensation pays employees in shares instead of cash, so it is a real cost that OCF and FCF do not show: it is added back to operating cash flow. SBC as a share of sales is how much of the cash flow depends on paying people in stock. Where it is large compared with FCF, FCF minus SBC is a truer measure of what the business generates for its owners, and it may be small or negative even when FCF looks strong. A company can keep its share count flat by spending cash on buybacks to offset the dilution, in which case the dilution does not show in the share count but the cash is still spent.

### How dependable that cash is
**Check whether it is consistent.** The last five fiscal years of FCF margin show whether today's figure is typical, improving, or an unusual year. Steady positive FCF is the sign of a self-funding business. A single year can be distorted by a one-off, such as a large settlement or a termination fee received, so read the history as a pattern. Fewer than five years usually means a recent listing.

**Then ask whether today's cash flow rests on temporary margins.** Gross margin vs 5-yr low shows how far gross margin over the last four quarters is above its lowest yearly level of the last five years. If it is far above, part of today's cash flow may come from conditions such as a shortage, and the company may look stronger than it would be once margins fall back. Ask whether it could still afford its current level of investment then. The five-year low can be an unusually weak year, so treat a large gap as a possible sign, not proof. A negative figure means margins are below every recent yearly level.

### When the cash falls short, what fills the gap, and whether it could hold up in a downturn
**See whether the gap is filled by issuing stock.** Share count change is the change in basic weighted shares over the year. A clear rise while cash flow is weak suggests the company is funding itself by selling shares. A rise while cash flow is strong more likely comes from stock compensation, which the SBC figure shows, or an acquisition paid in stock. A large jump around an IPO in the past year reflects the listing, not ongoing dilution. A fall means buybacks.

**Then judge whether it could carry its debt in a downturn.** Debt / OCF is how many years of operating cash flow would repay all its debt: under 3 years is strong, 3 to 6 moderate, over 6 weak. Net debt or net cash shows whether its cash would cover the debt anyway; a company with net cash is protected even if its cash flow falls. Debt matters more in a downturn, because the payments continue while revenue falls. When OCF is negative, Debt / OCF cannot be calculated, so the cash on hand, and how long it would last, become the question.

**End with the overall judgment,** covering the three parts: how much the company reinvests and whether it pays for that itself, how dependable that cash is, and what fills any gap and how well it would hold up in a downturn, and why.

## Steps
1. Find the first row where **Strength** is empty. Start there.
2. For each row, write **Strength**: a paragraph or two, usually about 200-300 words (longer if the company genuinely needs it), working through the three parts above and ending with the overall judgment. State the figures you rely on.
3. Do five rows, then stop and ask whether to continue.

## Rules
- Base the read on the row's inputs and the guidance above. Inferences are fine if they are reasonable, supported by the inputs and worded as inferences; mark anything drawn from your own knowledge as such.
- A dash means the figure is not available, not zero.
- Total debt includes lease liabilities, so a company with large leases can show debt without having borrowed.
- Net debt or net cash is in the company's reporting currency, shown in brackets; do not convert it.
- Judge strength on the figures, not on the company's size.
- A low gross margin reflects the business model, so it is not a reason to mark a company down.
- Nubank (NU) is a bank: its cash flow and debt reflect deposits and lending, so these measures do not apply in the usual way. Say so, and judge what the figures can still show.
- Write in complete sentences, without a summary rating or label.
- Do not compare the company with others, and do not assess growth, valuation or whether the company belongs on the watchlist.
- Do not use the `|` character in a cell.
- Do not commit or push unless asked.
