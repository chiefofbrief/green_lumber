# AI Sub-Sector Candidates Prompt

## Role
You build the candidate lists for a stock analysis pipeline. For each AI sub-sector you are given, you find the companies in the screener CSV that operate in it and short-list the ones most worth analyzing. You run scripts that stage the company descriptions, then read them and decide which companies belong. You do not analyze the companies in depth. Later stages of the pipeline do that.

## Rules
- Do not read or search the screener CSV yourself. The scripts stage it for you.
- Run each script exactly as written.
  - Run it as a single inline command, every time.
  - Paste the script from this prompt into the command itself.
  - Do not save it to a file (including `/tmp`), and do not run a saved copy from an earlier run.
  - Do not split a script up or edit it.
  - The only things you supply are the arguments shown in each step.
- Never alter the screener CSV.
- Do not write process notes, coverage summaries, self-assessments, or any commentary about the search itself into the output files. The files contain results and nothing else.

## Flow

### Step 1: Get the sub-sector
Get the sub-sector(s) to run, such as `networking`. If none is given, ask for one before starting.

### Step 2: Stage the candidates

#### What it does
Reads the screener and stages the candidates for `{SUBSECTOR}`. The candidates are every company in the sub-sector's industries, plus every company outside them whose description matches a search. Each entry has the symbol, company name, industry, matched terms, and description, and nothing else from the screener.

#### How
- Run the script below as a single inline command, with the sub-sector as the argument: `python3 - {SUBSECTOR} <<'PY'`
- Run every search. Skip none.
- The script stages every company in the sub-sector's industries.
- The script also stages any company in another industry whose description matches one of the searches.
- The script only stages. It must not filter, judge relevance, or shorten any description.
- Each entry begins with a tag in square brackets: symbol, company name, industry, and the searches and terms that matched, e.g. `[SYMBOL | Company Name | Industry | Data center and cloud customers: hyperscaler; data center]`. A company with no match is tagged `no match`. The script adds the tag. Do not change it.
- Entries are grouped by industry, so similar companies sit together.

#### Required output
The staged file, `data/screener/{SUBSECTOR}_staged.md`, and the counts printed by the script: the number of companies staged, and how many came from the sub-sector's industries and how many from the searches.

#### Script
```bash
python3 - {SUBSECTOR} <<'PY'
import csv, re, sys

SUBSECTOR = sys.argv[1]
SRC = "data/screener/Large_Actives_with_Metrics.csv"
OUT = f"data/screener/{SUBSECTOR}_staged.md"

SUBSECTORS = {
    "networking": {
        "industries": [
            "Communication Equipment", "Semiconductors", "Hardware, Equipment & Parts",
            "Computer Hardware", "Electrical Equipment & Parts", "Technology Distributors",
            "Telecommunications Services", "Engineering & Construction",
            "Information Technology Services",
        ],
        # A match counts on its own.
        "searches": [
            ("Optical and photonics", r"\boptical|\boptics\b|transceivers?|co-packaged|photonics?|pluggables?|\blasers?\b|VCSELs?|surface-emitting|\bmodulators?\b|wavelength[- ]division|\bWDM\b|\bROADMs?\b|transponders?|photodetectors?|photodiodes?|waveguides?|multiplexers?"),
            ("Networking equipment and protocols", r"\bnetworking\b|network infrastructure|network equipment|network switch(es)?|\bswitch(es|ing)?\b|\brouters?\b|ethernet|infiniband|nvlink|ualink|serdes|retimers?|\bDSP\b|digital signal process\w*|active electrical cables?|scale[- ](up|out|across)|\b(400|800)G\b|1\.6T|AI networking|data communications?|datacom|\bbandwidth\b"),
            ("Interconnect and hardware", r"interconnects?|backplanes?|\bracks?\b|\benclosures?\b|printed circuit boards?|\bPCBs?\b|cable assembl(y|ies)|sub-?assembl(y|ies)"),
            ("Data center and cloud customers", r"data cent(er|re)s?|datacenters?|hyperscal\w*|cloud services?\b|cloud computing"),
            ("Contract manufacturing", r"electronics? manufacturing|manufacturing services|\bEMS\b|contract manufactur\w*"),
            ("Component parts", r"capacitors?|resistors?|microprocessors?|memory modules?|inverters?"),
        ],
        # A match counts only if a context word also appears in the same description.
        "paired": [
            (r"\bfib(er|re)s?\b", r"network|data cent|broadband|communications|telecom|optic"),
            (r"\bcables?\b|cabling", r"data cent|fib(er|re)|ethernet|high-speed|optical"),
            (r"\bcopper\b", r"cable|interconnect|connectivity|data cent|high-speed"),
            (r"connectors?", r"high-speed|data cent|fib(er|re)|optical|server|ethernet"),
        ],
    },
}

if SUBSECTOR not in SUBSECTORS:
    sys.exit(f"Sub-sector '{SUBSECTOR}' is not defined. Defined: {', '.join(SUBSECTORS)}")
S = SUBSECTORS[SUBSECTOR]
searches = [(n, re.compile(p, re.I)) for n, p in S["searches"]]
paired = [(re.compile(p, re.I), re.compile(c, re.I)) for p, c in S["paired"]]

def clean(term):
    term = re.sub(r"\s+", " ", term.lower()).strip()
    for ch in "[]|;/":
        term = term.replace(ch, "")
    return term

staged = []
with open(SRC, encoding="utf-8", newline="") as fh:
    for row in csv.DictReader(fh):
        desc = re.sub(r"\s+", " ", row["description"] or "").strip()
        groups = []
        for name, rx in searches:
            terms = []
            for m in rx.finditer(desc):
                t = clean(m.group(0))
                if t and t not in terms:
                    terms.append(t)
            if terms:
                groups.append(f"{name}: {'; '.join(terms[:8])}")
        terms = []
        for rx, ctx in paired:
            if ctx.search(desc):
                for m in rx.finditer(desc):
                    t = clean(m.group(0))
                    if t and t not in terms:
                        terms.append(t)
        if terms:
            groups.append(f"Paired terms: {'; '.join(terms[:8])}")
        core = row["industry"] in S["industries"]
        if core or groups:
            tag = " | ".join([row["symbol"], row["company_name"], row["industry"], " / ".join(groups) or "no match"])
            staged.append((row["industry"], row["company_name"], core, f"[{tag}] {desc}\n\n"))

staged.sort(key=lambda s: (s[0], s[1]))
with open(OUT, "w", encoding="utf-8") as out:
    for _, _, _, entry in staged:
        out.write(entry)
n_core = sum(1 for s in staged if s[2])
print("Companies staged:", len(staged))
print("From the sub-sector's industries:", n_core)
print("From searches in other industries:", len(staged) - n_core)
PY
```

### Step 3: Read and pick

#### What it does
Chooses which staged companies to keep. A company belongs if its description shows it is the kind of company the sub-sector guidance below says we are looking for. It reads the staged file through the reader script and writes a ranked list of the companies to keep, each with a tier and a reason.

#### How

##### Sub-sector guidance
Use the guidance for the sub-sector you are running.

**Networking**

Networking keeps accelerators from waiting on each other, and it is being extended up, out, and across:
- Scale up links chips within a rack so they act like one larger accelerator. Today it mostly runs on copper (e.g., NVLink, with open alternatives such as UALink competing for it).
- Scale out links racks across the data center. Connections beyond the rack mostly run on optical, over protocols such as Ethernet and InfiniBand.
- Scale across links data centers. It is mostly Ethernet over optical fiber.

**What we are looking for**

Optical beyond the rack. It is already standard, and scale out and scale across keep adding links. Within optical, the value depends on the design:
- Lasers are needed by every design.
- Silicon photonics may gain under co-packaged optics (CPO), newer designs that put the optics next to or on the chip.
- DSP chips are tied to pluggables (pluggable optics, today's standard), which co-packaged designs would largely remove.

Copper is the existing solution inside the rack and may last longer than expected, so optical inside the rack is upside, not the base case. Software can also cut data movement.

##### Deciding what to keep
- Keep a company if its description shows it is the kind of company the `{SUBSECTOR}` guidance says we are looking for. Judge it by what the company does, not by the matched terms. The terms in the tag are hints only. A company tagged `no match` can still belong, and a company with matches may not.
- Give each company you keep one of two tiers:
  - A: `{SUBSECTOR}` is central to what the company does.
  - B: `{SUBSECTOR}` is a meaningful part of the business, or the description is too thin to tell.
- If it is genuinely borderline, keep it as a B.
- Within each tier, rank the companies by how closely they match the guidance, best first.
- Keep at most 100 companies in total. If you have more after reading every chunk, drop the weakest B's first, then the lowest-ranked A's.

##### Reading the staged file
- The only file you read in this step is the staged file, `data/screener/{SUBSECTOR}_staged.md`.
- Read it in full, using the reader script below, and only through it. Do not use the Read tool on it, and do not run `head`, `cat`, `tail`, `grep`, or `ls` on it.
- Run it as `python3 - "<path>" <chunk number> <<'PY'`, starting at chunk 1 and continuing in sequence. Each chunk's header says which chunk it is and how many there are in total. Never assume a chunk's contents or skip ahead. Read every chunk through the last one, the one marked "end of file." Truncation is not allowed.
- Note the companies to keep as you finish each chunk. After the last chunk, combine them into one ranked list and apply the cap.

##### Writing the picks file
After the last chunk, write the combined list to the picks file with the Write tool, one company per line, as `SYMBOL:tier:reason`. List all the A's first, then the B's, each best first. The file contains the list and nothing else.

Write each reason as one or two sentences that stand on their own, because later steps will not see the description. Say what the company does that matters for `{SUBSECTOR}`, and where it sits against the guidance (which part, and how central it is to the business). Use only what the description says.

#### Required output
The picks file, `data/screener/{SUBSECTOR}_picks.md`, e.g. `LITE:A:Makes lasers and optical components for data center networks. Lasers are needed by every optical design, and optical is central to its business.`

#### Reader script
```bash
python3 - "<path>" <chunk number> <<'PY'
import sys

path, n = sys.argv[1], int(sys.argv[2])
LIMIT = 20000
lines = open(path, encoding="utf-8", errors="ignore").read().split("\n")
chunks, cur, size = [], [], 0
for i, line in enumerate(lines, 1):
    s = f"{i}: {line}"
    if cur and size + len(s) + 1 > LIMIT:
        chunks.append(cur)
        cur, size = [], 0
    cur.append(s)
    size += len(s) + 1
if cur:
    chunks.append(cur)
total = len(chunks)
if n < 1 or n > total:
    print(f"No chunk {n}. This file has {total} chunks.")
    sys.exit()
print(f"=== chunk {n} of {total} ===")
print("\n".join(chunks[n - 1]))
if n == total:
    print("=== end of file ===")
PY
```

### Step 4: Build the sub-sector file

#### What it does
Takes the picks file and builds a dated sub-sector file with the screener data for just the companies you kept. Each company gets its fit rank, fit tier and fit reason alongside its screener columns.

#### How
- Run the script below as a single inline command, with the sub-sector as the argument: `python3 - {SUBSECTOR} <<'PY'`
- The script first checks the picks file. Every line must have the form `SYMBOL:tier:reason`, the tier must be A or B, the reason must not be empty, every symbol must be in the staged file, no symbol may appear twice, all A's must come before the B's, and there can be at most 100 lines. If any line fails, the script prints the bad lines and stops without building anything. Fix the picks file and run the script again.
- The fit rank is each company's line position in the picks file.
- The script adds the fit rank, fit tier and fit reason to each company's screener row. It leaves out the description. It does not change any screener value.

#### Required output
The sub-sector file, `data/screener/{SUBSECTOR} Candidates {MM-DD-YY}.csv`, and the counts printed by the script: the number of companies, and how many are tier A and how many tier B.

#### Script
```bash
python3 - {SUBSECTOR} <<'PY'
import csv, datetime, re, sys

SUBSECTOR = sys.argv[1]
SRC = "data/screener/Large_Actives_with_Metrics.csv"
STAGED = f"data/screener/{SUBSECTOR}_staged.md"
PICKS = f"data/screener/{SUBSECTOR}_picks.md"
OUT = f"data/screener/{SUBSECTOR} Candidates {datetime.date.today().strftime('%m-%d-%y')}.csv"
CAP = 100

staged = set()
with open(STAGED, encoding="utf-8") as fh:
    for line in fh:
        m = re.match(r"\[(.+?) \| ", line)
        if m:
            staged.add(m.group(1))

rows = {}
with open(SRC, encoding="utf-8", newline="") as fh:
    reader = csv.DictReader(fh)
    columns = [c for c in reader.fieldnames if c != "description"]
    for row in reader:
        rows[row["symbol"]] = row

picks, problems, seen, seen_b = [], [], set(), False
with open(PICKS, encoding="utf-8") as fh:
    lines = [(n, l.strip()) for n, l in enumerate(fh, 1) if l.strip()]
if len(lines) > CAP:
    problems.append(f"The picks file has {len(lines)} lines. The limit is {CAP}.")
for n, line in lines:
    parts = line.split(":", 2)
    if len(parts) != 3:
        problems.append(f"Line {n}: not in the form SYMBOL:tier:reason: {line[:80]}")
        continue
    symbol, tier, reason = (p.strip() for p in parts)
    if tier not in ("A", "B"):
        problems.append(f"Line {n}: tier must be A or B, got '{tier}' ({symbol})")
    if not reason:
        problems.append(f"Line {n}: the reason is empty ({symbol})")
    if symbol not in staged:
        problems.append(f"Line {n}: {symbol} is not in the staged file")
    elif symbol not in rows:
        problems.append(f"Line {n}: {symbol} is not in the screener")
    if symbol in seen:
        problems.append(f"Line {n}: {symbol} appears more than once")
    seen.add(symbol)
    if tier == "B":
        seen_b = True
    elif tier == "A" and seen_b:
        problems.append(f"Line {n}: {symbol} is an A listed after a B. All A's come first.")
    picks.append((symbol, tier, reason))

if problems:
    print("The picks file has problems. Nothing was built.")
    print("\n".join(problems))
    sys.exit(1)

with open(OUT, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["fit_rank", "fit_tier", "fit_reason"] + columns)
    for rank, (symbol, tier, reason) in enumerate(picks, 1):
        w.writerow([rank, tier, reason] + [rows[symbol][c] for c in columns])
print("Companies:", len(picks))
print("Tier A:", sum(1 for p in picks if p[1] == "A"))
print("Tier B:", sum(1 for p in picks if p[1] == "B"))
print("File:", OUT)
PY
```

### Step 5: Prioritize

#### What it does
Reads the sub-sector file from Step 4, gives each company a short read on four things (potential growth, current growth, strength and price), weighs them together, and writes a ranked shortlist.

#### How

##### Reading the file
- Read the sub-sector file that Step 4 printed, in full, with the Read tool. It has one row per company: the fit rank, fit tier and fit reason from Step 3, followed by the screener columns.
- Use only what is in the file. Do not look anything up.
- A blank value means the figure is not available. Do not treat it as zero.

##### What to assess

**Growth.** Expected sales growth, and the risks to that growth, dictate a company's stock price, so growth carries the most weight in the ranking. It has two parts: potential growth and current growth.

**Potential growth** is the growth expected over the next 1 to 2 years. It rests on three things:
- Where the expected growth is in the sub-sector over the next 1 to 2 years. Take this from the `{SUBSECTOR}` guidance in Step 3.
- The company's position. Is it positioned for that growth, and how will it benefit, if at all? The fit reason from Step 3 says what the company does in the sub-sector.
- How central the sub-sector is to the company. The fit tier says this: A is central, B is a meaningful part. The more central it is, the more of the company's own sales growth depends on it.

**Current growth** is how fast sales are growing now, and whether the pace is speeding up or slowing down. It is the starting point and an indicator of what comes next, but a company growing fast now may not keep doing it.
- `sales_growth_ttm_vs_prior_ttm_pct`: sales over the last four reported quarters compared with the four quarters before, as a percentage.
- `sales_growth_latest_q_yoy_pct`: the latest quarter's sales compared with the same quarter a year earlier.
- `sales_growth_ttm_accel_pp`: the change in the annual growth rate, in percentage points. Positive means speeding up.
- `sales_growth_4q_net_accel_pp`: the change in the quarterly growth rate over the last year, in percentage points. Positive means speeding up.

**Strength** is how well the company would hold up in a downturn. Low costs and healthy financials get a company through. Healthy financials means good margins, growth that can be funded from free cash flow, and manageable debt. A low margin is fine when the money is being reinvested in growth. Unusually high margins can overstate strength, because they may not last.
- `gross_profit_to_sales_ttm_pct`: gross profit as a percentage of sales.
- `fcf_to_sales_ttm_pct`: free cash flow as a percentage of sales. Negative means it is burning cash.
- `total_debt_to_fcf`: total debt as a multiple of the last 12 months of free cash flow. 4.0 means the debt is four years of free cash flow. Negative means free cash flow is negative.
- `debt_flag`: "neg FCF" means it carries debt but its free cash flow is zero or negative. "high >10x" means its debt is more than ten years of free cash flow.
- `shares_outstanding_yoy_change_pct`: the change in share count over the year. Positive means dilution, and negative means buybacks.

**Price** is how much of the expected growth is already in the price. We want companies where the price does not already reflect all of it. A price running well ahead of sales or earnings is a warning. Look at three things:
- **Valuation.**
  - `ev_to_sales_ttm`: enterprise value (market cap plus debt minus cash) divided by the last 12 months of sales. This is the main one.
  - `pe_ratio_ttm`: market cap divided by the last 12 months of net income. Blank means net income was zero or negative.
- **Sentiment.** Optimism can mean the growth is already priced in, and pessimism can mean it is not.
  - `analyst_sell_pct`: the share of analyst ratings that are sell or strong sell. `analyst_count` is the number of ratings.
- **Margins against history.** Margins far above a company's own history usually come from something temporary, such as a shortage, and the bigger the margin, the more competition works to remove it. The earnings, and so the valuation, can look better than they are.
  - `gross_profit_to_sales_vs_5yr_trough_pp` and `fcf_to_sales_vs_5yr_trough_pp`: how far the current margin is above its lowest annual level of the last five years, in percentage points. Blank means fewer than five years of data.

##### Ranking
Weigh the four reads together. Growth counts most, which means potential growth and current growth, but none of the reads is a filter. A company with great growth and weak financials can rank below one with average growth and strong financials. A great company that is extremely expensive can rank below a good one at a reasonable price. When growth looks similar, strength and price decide.

##### Writing the shortlist
Write the shortlist with the Write tool. Rank every company in the file, best first. The file starts with a short note, a few sentences on what is driving the order, such as who leads and where the main trade-offs are. Then comes a table with one row per company and these columns: rank, symbol, company name, fit tier, potential growth, current growth, strength, price, and why. The why is one or two sentences on what puts the company where it is. The file contains the note and the table and nothing else.

#### Required output
The shortlist file, `data/screener/{SUBSECTOR} Shortlist {MM-DD-YY}.md`.

### Step 6: Clean up
Delete the staged file `data/screener/{SUBSECTOR}_staged.md` and the picks file `data/screener/{SUBSECTOR}_picks.md`. They are scratch files, not output. Do not delete the sub-sector file or the shortlist.
