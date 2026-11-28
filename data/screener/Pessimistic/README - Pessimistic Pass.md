# Pessimistic Pass

## Context
I'm building a watchlist of AI companies. The working list is `data/screener/AI Watchlist (working).md` (170 companies). Earlier passes wrote reads on each company's AI role, growth, valuation and financial status. This pass writes one read per company on how it would fare if the pessimistic scenario in `AI Scenarios.md` came to pass. It is one of several separate pieces of data; it is not the full analysis of the company. Each company is assessed on its own, without comparing it to others.

## The file
`data/screener/Pessimistic/Pessimistic.md` has one row per company:
- **Inputs:** Symbol, Company, **Sub-sectors** and **AI Role** (from the AI Role pass), **Current growth** (from the Current Growth pass), and **Gross margin vs 5-yr low** (from the screener).
- **Output, empty until filled:** **Pessimistic**.

## Guidance
**Pessimistic** asks one question: if the pessimistic scenario comes to pass, how much of this company's demand and earnings is at risk, and what cushions it?

The pessimistic scenario is defined in `AI Scenarios.md`, under **Pessimistic scenario**, with an entry for each sub-sector. Use the entry for each of the company's sub-sectors, and the paragraph in **Company Scenario Considerations** on a company's businesses outside its sub-sector. Work from the scenario as written rather than restating it.

Answer the question by reading the inputs against the scenario:
- **Where the company's business sits in it.** The harm is not spread evenly across a sub-sector. Use AI Role to place the company within the entry for each of its sub-sectors.
- **How much of the business is exposed.** How much of the company AI is, how much of its current growth comes from it, and how concentrated its customers are.
- **What cushions it,** where the inputs show it: contracted backlog or long-term agreements, demand the scenario says is more likely delayed than lost, and businesses outside AI, judged on their own prospects as the scenario file says.
- **Whether earnings would fall further than sales.** Gross margin vs 5-yr low shows how far gross margin over the last four quarters is above its lowest yearly level of the last five years. A large gap means pricing may soften if the shortage behind it eases, so earnings would fall further than sales. The five-year low can be an unusually weak year, so treat a large gap as a possible sign, not proof.

**End with the overall judgment:** how much of the company's demand and earnings is at risk in the pessimistic scenario, and what cushions it.

## Steps
1. Before the first row, read `AI Scenarios.md` in full.
2. Find the first row where **Pessimistic** is empty. Start there.
3. For each row, write **Pessimistic**: a paragraph or two, about 250-300 words, working through the guidance above and ending with the overall judgment. Spend the words where the exposure is; you do not need to work through every point for every sub-sector. State the evidence you rely on.
4. Do five rows, then stop and ask whether to continue.

## Rules
- Base the read on the row's inputs and `AI Scenarios.md`. Inferences are fine if they are reasonable, supported by the inputs and worded as inferences; mark anything drawn from your own knowledge as such.
- Do not judge how likely the pessimistic scenario is. Assess the company as if it comes to pass.
- Use only the pessimistic scenario. Leave out the base scenario, the considerations on strength and price, and the longer-term downsides in `AI Sub-Sectors.md`.
- A dash means the figure is not available, not zero.
- Weight each sub-sector by how much of the business it is. A minor one gets a brief mention or a clause, not its own analysis.
- Customer concentration: use what AI Role shows, or your own knowledge if marked. If neither shows anything, leave it out rather than guess, and do not stretch weak hints (a list of research partners does not show who buys the equipment).
- Backlog: use it where the inputs give it. If it is a main cushion and its terms are not given, say once, briefly, that its firmness is not known; do not repeat the caveat otherwise.
- AI and non-AI businesses: use any split AI Role gives; otherwise a marked inference is fine. Judge non-AI businesses briefly, as the scenario file says, without estimating their growth rates.
- Write in complete sentences, without a summary rating or label.
- Do not compare the company with others, and do not assess the balance sheet, valuation or whether the company belongs on the watchlist.
- Do not use the `|` character in a cell.
- Commit and push to main once, after all rows are done.
