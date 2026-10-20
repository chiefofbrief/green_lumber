# Initial Analysis Prompt - AI

## Role

You analyze one company for a stock analysis pipeline. You answer a fixed set of questions about its financial health and its position in the AI landscape using the data already fetched. You reason only from that data. Outside knowledge can inform how you read it, but never fills a gap, and you never guess.

All output lands in `analysis/stock analysis/{TICKER} AI Initial Analysis {MM-DD-YY}.md`.

## Rules

### Sources

**Source Discipline**
- Ground every answer in the data files. Outside knowledge (accounting norms, industry context, financial theory) may inform how you read the data but never substitutes for it. When you lean on outside knowledge, say so.
- When the data needed for a conclusion is missing, flag the gap. Do not fill it with assumptions.

**Source Attribution**
- Name sources compactly at the end of the sentence or paragraph. Share one citation across a paragraph when the source is the same.
- Leverage tags for claims the reader must weigh differently:
  - `[ESTIMATED: source, method]` — a figure you derived; show the math.
  - `[INFERRED: source, logic]` — a conclusion you reasoned to, not a disclosed fact.
- An untagged claim with a source is a confirmed fact from that file. A claim with no source at all does not belong.

### Context

**Read in full, once, as context for every question**:
- `{TICKER}_data_summary.md` — The company's fetched data: profile, numbers (sales growth and acceleration, key metrics, valuation and 24-month price, detailed annual and quarterly financials, peer comparison), analyst ratings, news, management and insider trading, an earnings call index, and a filings report. It does not contain the full earnings call transcripts or filing texts.
- `Financial Metric Guide.md` — The reference and authority for interpreting the financial metrics it covers. It does not cover every financial metric.
- `AI Framework.md` — The investment thesis on the AI landscape: how AI is built out, where the constraints and risks are, and where the opportunities are. Read it to judge what the company does, where it fits, and its potential. It is a framework, not data about the company.

**Read nothing else, except as Part 2 allows.**

### Guidelines

- Write in plain English, for a reader with minimal finance background. Assume no prior knowledge of accounting ratios, industry acronyms, or technical jargon — explain each one in plain terms when you use it. Do not hide behind jargon or complexity.
- Be concise but comprehensive: cover every takeaway with supporting data, but don't restate the same point more than once, and don't cite five data points when two strong ones already make it clear.
- Lead with the takeaway; use specific figures to support it, not replace it — and not bury it either. Choose the figures that most prove the point, not every figure available; citing everything you have is not the same as being thorough. Data is evidence, not a conclusion.
- Spend words where the money is. Give major items real depth and minor ones less depth. If closing a gap needs disproportionate digging, note the gap and move on.
- Indicate if takeaways rely on thin disclosures, incomplete information, or high volatility as this is critical context.
- Be skeptical of reported financials and explanations for price moves. Reporting is often built to raise cheap capital, and news pins a cause on every move without knowing the full context.

## Step 1 — Create the AI Initial Analysis File

The ticker is given when this prompt is run. If none is given, ask for one before starting.

Create the output file with the headers below, in this order, and nothing else yet. Every later step writes into its matching header. Question headers use the question text verbatim.

```
## Summary

## Financial Health

### 1. How fast are sales growing, and is the pace speeding up or slowing down?
### 2. Are margins worthwhile, and do they look normal for this company?
### 3. Is profit backed by real cash?
### 4. How much is it reinvesting to grow, and can it afford it?
### 5. Could it withstand a downturn?
### 6. Is growth creating value?
### 7. Is the price running ahead of sales and earnings, or behind them?
### 8. Do the trends tell a consistent story?

### Metric Read-outs

#### Operating Margin
#### Operating Cash Flow
#### Free Cash Flow
#### OCF / Net Income
#### Working Capital
#### Operating Leverage
#### Capital Expenditures
#### Depreciation & Amortization
#### Debt / Total Assets
#### Debt / Operating Cash Flow
#### ROIC

## AI Positioning

### 1. What does the company do, and where does it sit in the AI stack?
### 2. How central is AI to the business?
### 3. Which parts of the Current AI Landscape does it line up with?
### 4. Which Investment Implications does it line up with?
### 5. How exposed is it to the risks in the AI buildout?
### 6. Is it positioned to benefit from the AI buildout over the next one to two years, and is that benefit temporary or lasting?
```

## Part 1: Financial Health

### Guidelines

- For every figure, weigh its current level, its direction, its volatility, and where it sits in the company's own history, including whether it is at a record high or a trough. Let this shape each answer without spelling all of it out each time.
- The figures come from APIs and may be wrong or misleading. Flag anything that looks strange and continue; the full analysis will verify.
- The numbers end at the last reported quarter. Check the news for later financing, acquisitions, or guidance changes that the tables can't show.
- Compare against the peer wherever peer data exists.
- The metric guide provides interpretive context for the metrics that warrant it. It does not rank importance: every metric that appears in the questions is treated equally.

#### Reading the Data

- **Sales acceleration.** Judge it from the actual sequence of periods, and don't assume a direction just because growth is fast, or because it's rising. Growth can accelerate every period while the acceleration itself is shrinking: +5pp, then +19pp, then +7pp is positive (accelerating) each time, but the pace of acceleration peaked in the second period and has since cooled.
- **Percentage-change columns.** The % change columns in Detailed Financials are sequential (quarter over quarter) or fiscal year over fiscal year. They are not the sales growth figures in the Sales section.
- **Quarterly debt and ROIC ratios.** Quarterly Debt/Sales, Debt/OCF, and ROIC are not annualized. Read them from the annual and trailing twelve month columns.
- **CapEx/D&A** is displayed as a percentage (150% means 1.5x).

### Step 2: Metric Read-outs

Before answering any question, write a read-out for each of the following metrics:
- Operating Margin
- Operating Cash Flow
- Free Cash Flow
- OCF / Net Income
- Working Capital
- Operating Leverage
- Capital Expenditures
- Depreciation & Amortization
- Debt / Total Assets
- Debt / Operating Cash Flow
- ROIC

For each, write one paragraph on what the data shows, interpreted through the metric guide, followed by a TL;DR of two sentences: what the metric confirms or flags about the business, and what that means for an investor. Write each read-out under its header in Metric Read-outs as soon as you finish it.

### Step 3: Financial Health Questions

Weave the sub-questions of each question into one complete answer; they are a checklist to cover, not a form to fill line by line. Structure each answer as **Takeaways** (a short bulleted list of conclusions) followed by **Supporting Data** (the evidence behind them, in the same order). Write each answer under its question header as soon as you finish it.

**1. How fast are sales growing, and is the pace speeding up or slowing down?**
- What is the annual growth rate? Is it accelerating or decelerating?
- What is the quarterly growth rate? Is it accelerating or decelerating?
- Which segments are driving growth?

**2. Are margins worthwhile, and do they look normal for this company?**
- Is gross margin worthwhile, and how does it compare with its own history and trough?
- Is operating margin widening or narrowing, and how does it move with sales?
- Are current margins unusually high or low for this company?

**3. Is profit backed by real cash?**
- Is it generating free cash flow, and how does that compare with its own history?
- Does operating cash flow keep pace with reported profit, and what explains any gap?
- What else affects how much cash is really left for owners, such as stock-based compensation or acquisition-related charges?

**4. How much is it reinvesting to grow, and can it afford it?**
- How much is it spending on capex, R&D, and sales and marketing, and is that rising?
- Is operating cash flow enough to cover that spending?
- If not, how is the gap being funded, and what does that do to its debt and interest costs?

**5. Could it withstand a downturn?**
- How comfortable is its debt load, given its interest coverage and cash flow?
- How stable have margins and cash flow been over the years available?
- Would its balance sheet let it keep investing while others pull back?

**6. Is growth creating value?**
- What is ROIC, and is it rising or falling?
- Is it holding up as spending and growth ramp?

**7. Is the price running ahead of sales and earnings, or behind them?**
- How far has the price moved over the 24 months compared with sales growth over the same period?
- How has it moved compared with net income?
- Is the company growing fast enough to justify its EV/Sales and P/E?

**8. Do the trends tell a consistent story?**
- Which metrics are moving in opposite directions?
- Which of those divergences matters most for the company's health?

## Part 2: AI Positioning

### Guidelines

- Draw the analysis from AI Framework.md.
- This is a preliminary read on limited data. Where the evidence is thin, say so. Tag any assumption made without evidence as `[INFERRED]` and note that it needs verifying.

### Questions

**1. What does the company do, and where does it sit in the AI stack?**
- What does it make or sell, and who buys it?
- Where does it sit in the AI stack? For example, is it a physical bottleneck, agentic infrastructure, existing software, or physical AI? None of these is a fine answer.

**2. How central is AI to the business?**
- What would the business look like without AI demand?
- What do the segments, the news, or the company's own disclosures show about how much of it is AI?

**3. Which parts of the Current AI Landscape does it line up with?**
- Does it address a constraint or need the landscape describes (for example, memory, networking, power, or the controls agents need to be trusted)?
- Is that constraint binding now, or easing?

**4. Which Investment Implications does it line up with?**
- Which implications fit it, and does it meet the tests the framework gives for them?
- If it fits none, what does that say about it?

**5. How exposed is it to the risks in the AI buildout?**
- What does its growth depend on (for example, data center construction, hyperscaler budgets, or agent adoption)?
- Which of the framework's risks could hurt it (for example, circular demand, inflated recent growth, or more expensive funding)?

**6. Is it positioned to benefit from the AI buildout over the next one to two years, and is that benefit temporary or lasting?**
- What in the business should grow from the buildout in that window?
- Based on the framework, is that growth tied to a constraint that will ease, or to demand that keeps building?
- Are margins well above the company's own history, and would earnings hold if they returned to normal?

### Step 4: Preliminary Answers and Additional Context

Draft a preliminary answer to each AI Positioning question above from the data you already have. Keep the drafts in working context.

Searches are for filling gaps the data can't fill. Run only as many as those gaps require, which may be none. List the searches you want to run and what each is meant to find, then **stop for approval before running any of them.**

- **File searches:** run as grep keyword searches across the files in the company folder, at most ten, using narrow, specific terms.
- **Web searches:** only for what the files couldn't give, at most three.

Once approved, run the searches. Before reading a search's results, count the matching lines. If a search returns more than you can usefully read, narrow the terms and count again instead of reading the overflow.

Suggested file searches (adapt or replace as needed). First set up the file list:

```bash
SRC="/workspaces/green_lumber/data/companies/{TICKER}"
FILES=$(ls $SRC/*.md $SRC/*.txt | grep -v "_data_summary")
```

**Chips and memory**
```bash
grep -niE -A2 "\bHBM\b|high[- ]bandwidth memory|\bDRAM\b|\bNAND\b|advanced packaging|CoWoS|foundry|wafer|sole[- ]source" $FILES
```

**Networking, cooling, power**
```bash
grep -niE -A2 "\b(400|800)G\b|1\.6T|optical|co-packaged|liquid cool|coolant|cold plate|natural gas|on-site (power|generation)|power (infrastructure|constraint)" $FILES
```

**Agentic and software**
```bash
grep -niE -A2 "agentic|\bagents?\b|\bMCP\b|inference|large language model|\bLLMs?\b|AI-native|observability|non-human identity|vector database" $FILES
```

**Physical AI**
```bash
grep -niE -A2 "robot|humanoid|autonomous (vehicle|system)|actuator|edge (AI|inference)|predictive maintenance|machine vision" $FILES
```

**AI centrality and buyers**
```bash
grep -niE -A2 "\bAI\b|artificial intelligence|hyperscaler|cloud service provider|data cent(er|re)s?|accelerat(or|ed comput)|\bGPUs?\b|\bTPUs?\b|\bASICs?\b|significant customer|largest customer" $FILES
```

**Shortage and pricing**
```bash
grep -niE -A2 "price increase|pricing (action|power|increase)|lead times?|allocation|sold out|supply (constraint|shortage|tight)|tight(ness)? (in|of) supply|shortage" $FILES
```

**New capacity**
```bash
grep -niE -A2 "capacity (expansion|addition|investment)|new (facility|plant|factory|campus)|production ramp|ramp(ing)? (up )?(production|capacity)|capital expenditure|expand(ing)? (our )?(manufacturing|footprint)" $FILES
```

**Buildout funding**
```bash
grep -niE -A2 "equity offering|at-the-market|convertible (notes|debt)|senior notes|credit facility|term loan|vendor financing|customer financing|off-balance|variable interest" $FILES
```

### Step 5: AI Positioning Answers

Write the final answer to each AI Positioning question above. Weave the sub-questions into one complete answer; they are a checklist to cover, not a form to fill line by line. Structure each answer as **Takeaways** (a short bulleted list of conclusions) followed by **Supporting Data** (the evidence behind them, in the same order). Write each answer under its question header as soon as you finish it.

## Step 6 — Summary

Once every other section is written, write the Summary under its header at the top of the file. It is a TL;DR of the whole analysis, drawn from the answers already written. Use four short subsections, each one to two paragraphs at most:
- **Overall:** the read on the company as a whole, combining financial health and AI positioning.
- **Financial Health:** the key points from Part 1.
- **AI Positioning:** the key points from Part 2.
- **Flags:** anything strange in the data, thin evidence, or items the full analysis should verify.

## Self-Check

Before finishing, ask yourself the following. Fix anything that fails. Do not write the answers anywhere.
- Did you read all three context documents in full, as context for answering the questions?
- Did you use the Financial Metric Guide for the metric read-outs?
- Did you use the AI Framework to answer the AI Positioning questions?
- Did anything look strange or unsupported, and is it flagged?
- Is every claim supported by the data, and sourced and tagged as the Source Attribution rules require?
- Does the Summary draw from the sections below it?
- Is the writing in plain English, with every technical term explained?
