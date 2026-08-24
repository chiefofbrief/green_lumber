# Data Extraction Prompt

## Role
You extract verbatim qualitative excerpts for a stock analysis pipeline. You "read" the long documents — earnings-call transcripts, news, 10-Ks, 10-Qs, and the rest — by running the grep searches below, staging their raw output, then reading that staged output and copying every passage relevant to the eleven questions below into one flat Excerpts file. You do not analyze the data. You may use judgment only to decide relevance and to drop obvious noise from grep output — never to alter, shorten, or add to the text you keep.

All output lands in `data/companies/{TICKER}/{TICKER} Excerpts.md`.

## Rules
- Extract qualitative narrative only: management commentary, explanations, disclosures, risk language, analyst questions, and news framing. The quantitative data already lives in the data summary — do not reproduce financial tables, price targets, or rating changes as data.
- Do not read full files. Grep only, using the terms below. Reading full files destroys session context.
- Run every grep. Skip none.
- Copy relevant excerpts verbatim — no condensing or truncation.
- When a passage you keep contains figures, year-over-year comparisons, dollar amounts, or qualifications, copy them exactly — do not strip numbers or hedging out of the narrative.
- Do not paraphrase, compress, or restate — not even one sentence.
- Do not add commentary or transitions between passages.
- End every excerpt with its source file in parentheses, e.g. `(AAPL_10k.txt)`.
- A passage is worth keeping if it helps answer any one of the eleven questions below — judge each passage against all eleven at once. The output is one flat, unstructured list of excerpts, in the order you encounter them — do not create section headers or otherwise group excerpts by question.
- If the same passage, or a near-duplicate of it, appears more than once in the staging file, include it in the Excerpts file once.
- Do not write process notes, coverage summaries, self-assessments, or any commentary about the extraction itself into the Excerpts file — the file contains excerpts and nothing else.

## The eleven questions
These are relevance criteria, used in Step 1 (as labels on the grep commands) and Step 3 (to judge each passage). They are not output sections.

1. How does the company make money?
2. What are its competitive advantages?
3. How and why are sales growing?
4. Is there a reasonable expectation of accelerated or continued future sales growth?
5. Is it highly dependent on a small number of customers?
6. Does it have a worthwhile gross margin? If not, is there a good reason why the margin is low?
7. Is it generating FCF? If not, is there a good reason why?
8. Are liabilities and expenses reasonable and manageable?
9. Do accounting choices appear to be inflating or depressing reported earnings?
10. What is the financial community's current appraisal of the company and its growth prospects?
11. What catalyst(s) may force the financial community's appraisal to converge with ours?

## Flow

### Step 1 — Stage every grep
Set `SRC="/workspaces/green_lumber/data/companies/{TICKER}"`. Every grep runs across all of the ticker's files — `$SRC/*.md $SRC/*.txt`. Do not narrow to specific documents.

Run every command below, in a single script, appending all output to one staging file (e.g. `/tmp/{TICKER}_greps.txt`). Run every grep — skip none, even where one pattern covers several questions. The script only stages raw matches — it must not filter, judge relevance, or truncate anything.

**Q1 — money**
```bash
grep -niE -A8 "reportable segment|operating segment|revenue by segment|segment revenue|disaggregation of revenue|net (sales|revenue) by|principal products|products and services|sources of revenue|we (generate|derive|earn) .*revenue|we (sell|offer|provide)|business line|product line|recurring revenue|subscription|transaction-based|license revenue" $SRC/*.md $SRC/*.txt
```

**Q2 — competitive advantage**
```bash
grep -niE -A5 "competit|(competitive|cost|technology|strategic|sustainable|structural) advantage|differentiat|patent|intellectual property|proprietary|trade secret|trademark|market leader|leading provider|market share|economies of scale|barrier to entry|switching cost|network effect|moat|pricing power|dominant (position|player|share)|scale advantage|first[- ]mover" $SRC/*.md $SRC/*.txt
```

**Q3 — sales growing**
```bash
grep -niE -B1 -A6 "(revenue|sales) (increased|decreased|grew|declined)|increased? .*due to|driven (primarily )?by|primarily due to|attributable to|growth .*driven by|partially offset|organic (growth|revenue)|acquisition|acquired|(unit price|volume|pricing|price increase).{0,60}(increase|decrease|higher|lower|driven|due to|growth|declin)|new (product|service|offering|customer|contract)|product launch|introduc|new market|expansion into" $SRC/*.md $SRC/*.txt
```

**Q4 — growth opportunity**
```bash
grep -niE -A6 "market share|addressable market|total addressable|penetration|growth opportunity|invest(ing)? .*growth|(demand|expand(ing|sion)?|scal(e|ing)|adoption).{0,60}(customer|market|capacity|business|growth|product)|artificial intelligence|machine learning|generative|automation|(long[- ]term|multi-year).{0,60}(growth|strategy|opportunity|demand|contract|agreement)|new (product|service|offering)|product launch|introduc|pipeline (of|for) (new|customer|product)|innovation|road ?map|new market" $SRC/*.md $SRC/*.txt
```

**Q4 — ARR / retention**
```bash
grep -niE -B1 -A2 "annual recurring revenue|recurring revenue|\bARR\b|net (dollar )?retention|net revenue retention|\bNRR\b|\bDBNRR\b|retention rate|bookings|remaining performance obligation|\bRPO\b|backlog|deferred revenue|billings|renewal|churn|subscriber|subscription" $SRC/*.md $SRC/*.txt
```

**Q4 — headwinds**
```bash
grep -niE -B1 -A4 "headwind|challenge|(margin|cost|pricing|demand) pressure|uncertainty|slowdown|soft(ness)?|weak(ness|er)?|macroeconomic|(adverse|unfavorable|negatively) (impact|effect|affected)|constrain|investigation|antitrust|lawsuit|litigation|probe|regulatory (change|scrutiny|action|investigation)" $SRC/*.md $SRC/*.txt
```

**Q4, Q6, Q7, Q11 — guidance / outlook**
```bash
grep -niE -B1 -A8 "guidance|outlook|forecast|we (expect|anticipate|plan|intend|estimate) (to|that)|reaffirm|raise[d]? .*guidance|lower[ed]? .*guidance|(full[ -]year|next quarter|for (the remainder of )?fiscal).{0,60}(guidance|outlook|expect|anticipate|revenue|growth|margin|EPS)" $SRC/*.md $SRC/*.txt
```

**Q5 — customer concentration**
```bash
grep -niE -B1 -A8 "significant customer|major customer|customer concentration|no (single|one) customer|largest customer|(one|two|three) customers?|top .*customers|(accounted for|represented) .*% of .*(revenue|sales)|concentration of credit|dependence on|reliance on" $SRC/*.md $SRC/*.txt
```

**Q6 — margin**
```bash
grep -niE -B1 -A5 "margin.{0,60}(driven|due to|primarily|reflect|attribut|expand|contract|improv|declin|pressure|compress|benefit|headwind|offset)|(driven|due to|primarily|reflect|attribut|expand|contract|improv|declin|pressure|compress|benefit|headwind|offset).{0,60}margin|gross profit (increase|decrease|driven|due to)|cost of (revenue|sales|goods) (increase|decrease|driven|due to|as a percentage)" $SRC/*.md $SRC/*.txt
```

**Q7 — free cash flow**
```bash
grep -niE -B1 -A5 "free cash flow|cash flow (increase|decrease|generat|from operations)|cash from operations|cash (provided|used) (by|in) operating|cash generation|cash conversion|capital allocation|return .*capital|repurchase|buyback|accelerated share repurchase|\bASR\b|dividend (increase|paid|declared)|debt paydown" $SRC/*.md $SRC/*.txt
```

**Q8 — liabilities / liquidity**
```bash
grep -niE -A8 "liquidity|capital resources|(debt|indebtedness) (increase|decrease|level|matur|covenant|outstanding)|borrowings|notes payable|credit facility|revolving|term loan|senior notes|covenant (compliance|violation|breach)|leverage ratio|interest expense|maturit|refinanc|commitments and contingencies|purchase obligation|(operating|finance) lease (obligation|commitment|expense)|contingent liabilit|off-balance" $SRC/*.md $SRC/*.txt
```

**Q9 — critical accounting estimates**
```bash
grep -niE -A15 "critical accounting (estimate|polic)|significant accounting polic|use of estimates|change(s|d)? (in|to) .*(estimate|accounting|policy)|newly adopted|recently (adopted|issued) accounting|accounting standards update|\bASU\b" $SRC/*.md $SRC/*.txt
```

**Q9 — revenue recognition**
```bash
grep -niE -B1 -A6 "revenue recognition|recognize(d)? revenue|point-in-time|ratably|ASC 606|performance obligation|deferred revenue|unearned|unbilled|days sales outstanding|allowance for (doubtful|credit)|accounts receivable (increase|decrease|reserve|allowance)|inventor(y|ies) (reserve|write-?down|obsolete|excess)|channel (partner|inventory|stuffing|fill)" $SRC/*.md $SRC/*.txt
```

**Q9 — accruals / reserves**
```bash
grep -niE -B1 -A5 "accru(e|ed|al)|(reserve|provision|allowance) (for|of|increase|decrease|release|establish)|expense recognition|cookie.jar" $SRC/*.md $SRC/*.txt
```

**Q9 — capitalization / depreciation**
```bash
grep -niE -B1 -A5 "capitaliz|useful li(fe|ves)|depreciat|amortiz|impair(ment|ed) (charge|loss|test|assessment)" $SRC/*.md $SRC/*.txt
```

**Q9 — one-time items**
```bash
grep -niE -B1 -A5 "one-time|one time|non-recurring|nonrecurring|unusual|infrequent|extraordinary|special (charge|item)|certain (charges|items)|discrete|write-?off|write-?down|impairment (charge|loss)|restructuring|severance|workforce reduction|reduction in force|facility (closure|exit)|exit cost" $SRC/*.md $SRC/*.txt
```

**Q9 — non-GAAP adjustments**
```bash
grep -niE -B1 -A5 "non-gaap|adjusted (ebitda|earnings|net income|eps|operating income)|core earnings|excluding.{0,40}(charge|expense|cost|impact|item)|add-?back|stock-based compensation|share-based|rebate" $SRC/*.md $SRC/*.txt
```

**Q9 — circular / round-trip financing**
```bash
grep -niE -B1 -A5 "circular|round.trip|vendor financing|customer financing|counterparty|reciprocal|factor(ing|ed)|securitiz|reclassif" $SRC/*.md $SRC/*.txt
```

**Q9 — off-balance-sheet / lease / goodwill**
```bash
grep -niE -B1 -A8 "off-balance|unconsolidated|variable interest entit|\bVIE\b|letter of credit|(operating|finance) lease (obligation|commitment|term|expense)|related.party (transaction|arrangement)|contingent (liabilit|loss)|guarantee(d)? (obligation|debt|of)|pension (plan|obligation|expense)|post.?retirement|OPEB|goodwill (impair|write-?down)|auditor|independent registered public accounting|audit fee" $SRC/*.md $SRC/*.txt
```

**Q10 — analyst quotes**
```bash
grep -niE -A15 "\(Analyst" $SRC/*.md $SRC/*.txt
```

**Q10 — sentiment**
```bash
grep -niE -B1 -A3 "bullish|bearish|optimistic|pessimistic|skeptic|sentiment|narrative|thesis|momentum|overhang|out of favor|priced (in|for)|undervalued|overvalued|attractive|compelling|on sale|compounder|Wall Street|the Street|analysts?|investors?|the market|concern|caution|worried|fears?|doubt|conviction" $SRC/*.md $SRC/*.txt
```

**Q11 — catalysts**
```bash
grep -niE -A6 "look forward|upcoming|later this year|next (fiscal|generation)|(product|service) launch|introduc(e|ing|tion) (of|a new)|rollout|roll out|new product|road ?map|pipeline (of|for)|on track|will begin|ramp (up|ing)|milestone|catalyst|coming (months|quarters)|approval|certif|partnership|go[- ]live" $SRC/*.md $SRC/*.txt
```

### Step 2 — Deduplicate mechanically
Remove exact-duplicate lines from the staging file, preserving original order (e.g. `awk '!seen[$0]++' staging_file > deduped_file`). This is a structural step, not a judgment call — it only removes byte-identical repeated lines, never anything based on meaning or relevance.

### Step 3 — Read and fill the Excerpts file
Read the deduplicated staging file in full. If it's too large for one read, read it in sequential chunks that cover it completely — never assume a chunk's contents or skip ahead; if a read stops short of the file's end, continue reading from that point until the entire file has been read. Truncation is not allowed.

Judge each passage against the eleven questions above. Copy every relevant passage verbatim into `data/companies/{TICKER}/{TICKER} Excerpts.md`, one flat list, in the order you encounter them.

### Step 4 — Clean up
Delete the staging file and the deduplicated file created in Steps 1–2. They are scratch files, not output.
