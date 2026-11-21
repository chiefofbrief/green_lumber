# News Pass

Adds two columns of news data to `data/screener/AI Watchlist (working).md`: **News AI** and **News Sentiment**. This is data for a later analysis, not the analysis itself.

## Steps
1. Find the first row in the watchlist where **News AI** is empty. That is the next company.
2. Read that company's news file in this folder, `{SYMBOL}_news.md`, in full.
3. Fill in the two cells for that row:
   - **News AI:** what the company is actually doing in AI and what it is known for in AI, according to the news: products, customers, deals, AI-related revenue or demand. If there are no AI stories or headlines, say so plainly.
   - **News Sentiment:** what people are saying about the company: the tone (excited, worried, mixed, indifferent) and why.
4. Move to the next company. Commit and push every 10 companies or so.

## For each entry
- Answer both every time, in two or three sentences each.
- Cite concrete evidence from the file: figures, named products or customers, dates.
- Flag thin coverage (few articles).
- Do not use the `|` character in a cell.
- Report what the news says. Do not judge whether the company belongs on the watchlist.

Most files are FMP articles only. 24 also include Perigon stories, which carry fuller summaries.
