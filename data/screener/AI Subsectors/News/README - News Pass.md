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
- Describe only what the news says, and attribute it ("Q3 coverage reported...", "William Blair said...", "headlines frame it as..."). Do not state facts about the company in your own voice, and do not add inferences or conclusions the news does not make.
- **News AI** (three to five sentences): how the news describes the company's role in AI, if it does; then the AI-related figures, deals, customers and products it reports; then how the coverage frames the company overall, or that the news says little or nothing about AI.
- **News Sentiment** (two to four sentences): the tone of the coverage; then the stock moves, analyst actions and bull or bear arguments it reports; then any caveats it raises.
- Cite concrete evidence from the file: figures, named products or customers, dates.
- Flag thin coverage (few articles).
- Do not use the `|` character in a cell.
- Do not judge whether the company belongs on the watchlist.

Most files are FMP articles only. 24 also include Perigon stories, which carry fuller summaries.
