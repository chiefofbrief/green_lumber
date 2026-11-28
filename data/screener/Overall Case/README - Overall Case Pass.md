# Overall Case Pass

## Context
I'm building a watchlist of AI companies. The working list is `data/screener/AI Watchlist (working).md` (170 companies), and every company stays on it. Earlier passes wrote four reads per company: Potential growth, Valuation, Financial status and Pessimistic. This pass draws them together into one read per company: the case for and against prioritizing it as a candidate for a deep dive. A later step uses these reads to choose which companies to prioritize. Each company is assessed on its own, without comparing it to others.

## The file
`data/screener/Overall Case/Overall Case.md` has one row per company:
- **Inputs:** Symbol, Company, **Potential growth**, **Valuation**, **Financial status** and **Pessimistic**, copied from the master file.
- **Output, empty until filled:** **Overall case**.

## Guidance
**Overall case** asks one question: is this company worth prioritizing as a candidate for a deep dive, and why?

Everything revolves around growth. Potential growth is the growth itself: how much is expected over the next 1-2 years, and how much of it is still ahead rather than already visible. It carries the most weight. The other three reads are the context for that growth:
- **Valuation** is what the price already pays for it. A price above average is acceptable only when the growth still ahead clearly supports it.
- **Financial status** is whether the company can sustain it, funding it from the cash its business generates.
- **Pessimistic** is whether it holds up if the pessimistic scenario comes to pass.

Read the four together, not as a checklist. None is a filter on its own, and weakness in one can be outweighed by strength in the others, but without meaningful growth still ahead there is no case. Count each concern once: a margin far above history, for example, may appear in several reads, but it is one concern.

Write three paragraphs:
- **The case for:** what in the reads makes the company worth prioritizing, if anything.
- **The case against:** what holds it back.
- **What it hinges on:** a short third paragraph beginning "What it hinges on", naming the one or two things the decision turns on. Do not make the decision itself.

## Steps
1. Find the first row where **Overall case** is empty. Start there.
2. For each row, write **Overall case**: three paragraphs, about 200-300 words in all, separated by `<br><br>`: the case for, the case against, and what it hinges on.
3. Do five rows, then stop and ask whether to continue.

## Rules
- Base the read on the four input reads. Do not redo them or add facts they do not contain; mark any inference as an inference.
- Cite the input reads' own conclusions rather than redoing them, but weigh them against each other where they pull in different directions.
- Where an input read marks a point as background knowledge, keep the marking when you use it. Do not add background knowledge of your own.
- If the reads show little growth still ahead, say so plainly as a description, for example "the reads show little growth still ahead, so the case for is thin." Do not go further and say whether the company should be prioritized.
- Do not say whether the company should be prioritized, and do not give a rating or label.
- Do not compare the company with others.
- Write in complete sentences.
- Do not use the `|` character in a cell.
- Commit and push to main once, after all rows are done.
