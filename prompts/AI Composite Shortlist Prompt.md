# AI Composite Shortlist Prompt

## Role
You are an analyst in a stock analysis pipeline. Across all the AI sub-sectors, you judge how the companies on their Scenario Shortlists would fare in a base scenario and in a pessimistic scenario, compared with each other, and produce a composite shortlist of the best of them for in-depth analysis later in the pipeline.

You follow the guidance in the files you are given, and you follow this prompt exactly. You pay close attention to detail, because the guidance was written carefully and small differences in it change the answer.

## Rules

### Reading files
- Use only the files this prompt names. Do not look anything up. What you know about a company can supplement the files, but it may be out of date, so rely on the files first.
- Whenever a step tells you to read a file, read all of it with the **`Reader Script`** and pay close attention to everything in it.

### Writing files
- Never alter the input files. The only files you write are the working files and the Composite Shortlist file.
- Do not write process notes, coverage summaries, self-assessments, or any commentary about your process into the output files. The files contain results and nothing else.

### Running scripts
- Run every command from the repository root.
- Run each script exactly as written.
  - Run it as a single inline command, every time.
  - Paste the script from this prompt into the command itself.
  - Do not save it to a file (including `/tmp`), and do not run a saved copy from an earlier run.
  - Do not split a script up or edit it.
  - The only things you supply are the arguments shown in each step.

### Reader Script
When a step tells you to read a file in full:
- Read it in full, using the script below, and only through it. Do not use the Read tool on it, and do not run `head`, `cat`, `tail`, `grep`, or `ls` on it.
- Run it as `python3 - "<path>" <chunk number> <<'PY'`, starting at chunk 1 and continuing in sequence. Each chunk's header says which chunk it is and how many there are in total. Never assume a chunk's contents or skip ahead. Read every chunk through the last one, the one marked "end of file." Truncation is not allowed.
- Run one chunk per command. Wait for each chunk's output before running the next. Do not loop, run several chunks together, or add other lines to the command. A command's output is cut off at about 30,000 characters, and each chunk is about 20,000.

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

## Combined File Columns
The combined file, `data/screener/AI Subsectors/all_combined.md`, built in Step 1, has one row per company. Three things about it matter in every step:
- The companies are already strong. Each one was among the best in its sub-sector in the base scenario, the pessimistic scenario or both. The differences between them are fine ones, and a weakness that would not matter in a wider field can decide a company's place here.
- Every earlier comparison is within one sub-sector. The earlier stages compared each company only with the other companies in its own sub-sector, so "cheapest" or "fastest growing" in their reads means within that sub-sector. This stage is the first to compare companies across sub-sectors.
- Percentiles are the exception. A percentile (pctl) ranks a figure against a broad list of companies that reaches well beyond the AI sub-sectors. Higher is better, so a higher EV/sales percentile means cheaper.

The columns come from each sub-sector's Scenario Shortlist. The first earlier stage wrote the reads on growth, strength and price, and the second judged how each company would fare in the base and pessimistic scenarios.

A company on more than one Scenario Shortlist appears once. Columns that depend on the sub-sector hold one part for each sub-sector, labeled with it, such as `networking (A): ...; processors (B): ...`. Columns about the company as a whole hold one copy.

Columns that depend on the sub-sector:
- **Sub-sectors** lists each sub-sector whose Scenario Shortlist the company is on, with its fit tier. A means the sub-sector is central to the business. B means it is a meaningful part, or the description was too thin to tell.
- **Fit reason** says what the company does in the sub-sector, which kind of company it is there and why that kind matters, how central the sub-sector is to its business, and how important a player it is.
- **Potential growth** is the growth expected over the next 1 to 2 years. The analysis considered where the sub-sector's expected growth is, whether the company's business sits where that growth is, and how central the sub-sector is to the company.
- **Why** says what put the company where it was in the sub-sector's ranking.
- **Sub-sector base read** and **Sub-sector pessimistic read** say how the company would fare in each scenario. They are a starting point to test, not to copy.

Columns about the company as a whole:
- **Current growth** is how fast sales are growing now, and whether the pace is speeding up or slowing down. The data analyzed was:
  - TTM sales growth, compared with the previous twelve months
  - Latest-quarter sales growth, compared with the same quarter a year earlier
  - TTM acceleration: the change in the annual growth rate, in percentage points
  - 4-quarter acceleration: the change in the quarterly growth rate over the last year, in percentage points
- **Strength** is how well the company would hold up through a downturn, and be positioned to prosper after it. The data analyzed was:
  - Gross margin
  - Free cash flow margin
  - Debt as a multiple of free cash flow
  - Change in share count over the year
  - Size: market cap and sales
- **Price** is how much of the expected growth is already in the price. The data analyzed was:
  - EV/sales
  - P/E
  - The share of analyst ratings that are sell or strong sell, and how many ratings there are

The reads on growth, strength and price also considered how far gross margin and free cash flow margin are above their lowest annual level of the last five years. A large gap was counted as one concern about the company, not once for each read.

## Flow

### Step 1: Combine the Scenario Shortlists

#### What it does
Gathers every sub-sector's Scenario Shortlist into one file, with one row per company.

#### How
Run the script below as a single inline command: `python3 - <<'PY'`

The script builds the combined file, `data/screener/AI Subsectors/all_combined.md`, from the latest Scenario Shortlist file for each sub-sector, `data/screener/AI Subsectors/{SUBSECTOR} Scenario Shortlist {MM-DD-YY}.md`. The file has the columns described in **`Combined File Columns`**:
- There is one row per company, sorted by symbol.
- For a company on more than one Scenario Shortlist, the columns that depend on the sub-sector hold a labeled part for each. The columns about the company as a whole are taken from one of them, since they describe the same company.
- The earlier ranks are left out, because they only compare companies within one sub-sector.

First, it checks:
- Every sub-sector has a file.
- Each file has the columns it needs.
- Every row is complete.
- No symbol appears twice in one file.

If a check fails, it prints the problems and stops without building anything. Fix the problems and run the script again.

#### Required output
`data/screener/AI Subsectors/all_combined.md`, and what the script printed: the files it used, the number of companies for each sub-sector, the total number of companies, and the companies on more than one Scenario Shortlist.

#### Script
```bash
python3 - <<'PY'
import glob, os, re, sys

DIR = "data/screener/AI Subsectors"
OUT = f"{DIR}/all_combined.md"
SUBSECTORS = ["networking", "power", "electrical", "wafers", "cooling", "data",
              "trust", "runtime", "processors", "racks", "memory", "tools"]
NEEDED = ["Symbol", "Company", "Fit tier", "Fit reason", "Potential growth", "Current growth",
          "Strength", "Price", "Why", "Base read", "Pessimistic read"]
PER_SUB = [("Fit reason", "Fit reason"), ("Potential growth", "Potential growth"), ("Why", "Why"),
           ("Base read", "Sub-sector base read"),
           ("Pessimistic read", "Sub-sector pessimistic read")]
WHOLE = ["Current growth", "Strength", "Price"]

def date_key(path):
    m = re.search(r"(\d\d)-(\d\d)-(\d\d)\.md$", path)
    return (m.group(3), m.group(1), m.group(2)) if m else ("", "", "")

def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

problems, used, entries = [], [], {}
for sub in sorted(SUBSECTORS):
    files = sorted(glob.glob(f"{DIR}/{sub} Scenario Shortlist *.md"), key=date_key)
    if not files:
        problems.append(f"No Scenario Shortlist file for '{sub}' in {DIR}")
        continue
    path = files[-1]
    header, table = None, []
    with open(path, encoding="utf-8") as fh:
        for line in fh:
            if not line.lstrip().startswith("|"):
                continue
            c = cells(line)
            if header is None:
                header = c
            elif all(x and set(x) <= set(":-") for x in c):
                continue
            else:
                table.append(c)
    if header is None:
        problems.append(f"{path} has no table")
        continue
    missing = [n for n in NEEDED if n not in header]
    if missing:
        problems.append(f"{path} has no column: {', '.join(missing)}")
        continue
    bad = [i for i, r in enumerate(table, 1) if len(r) != len(header)]
    if bad or not table:
        problems.append(f"{path}: {'no rows' if not table else 'rows with the wrong number of columns: ' + ', '.join(map(str, bad))}")
        continue
    idx = {n: header.index(n) for n in NEEDED}
    syms = [r[idx["Symbol"]] for r in table]
    dupes = sorted({s for s in syms if syms.count(s) > 1})
    if dupes:
        problems.append(f"{path}: symbols that appear more than once: {', '.join(dupes)}")
        continue
    for r in table:
        entries.setdefault(r[idx["Symbol"]], []).append((sub, {n: r[idx[n]] for n in NEEDED}))
    used.append((sub, path, len(table)))

if problems:
    print("The Scenario Shortlists have problems. Nothing was built.")
    print("\n".join(problems))
    sys.exit(1)

order = ["Symbol", "Company", "Sub-sectors", "Fit reason", "Potential growth", "Current growth", "Strength", "Price",
         "Why", "Sub-sector base read", "Sub-sector pessimistic read"]
rows = []
for symbol in sorted(entries):
    es = entries[symbol]
    first = es[0][1]
    row = {"Symbol": symbol, "Company": first["Company"],
           "Sub-sectors": ", ".join(f"{sub} ({e['Fit tier']})" for sub, e in es)}
    for old, new in PER_SUB:
        row[new] = "; ".join(f"{sub} ({e['Fit tier']}): {e[old]}" for sub, e in es)
    for n in WHOLE:
        row[n] = first[n]
    rows.append([row[h] for h in order])

with open(OUT, "w", encoding="utf-8") as out:
    out.write("| " + " | ".join(order) + " |\n")
    out.write("|" + "---|" * len(order) + "\n")
    for r in rows:
        out.write("| " + " | ".join(r) + " |\n")

repeated = [s for s in sorted(entries) if len(entries[s]) > 1]
for sub, path, n in used:
    print(f"{sub}: {n} companies ({os.path.basename(path)})")
print("Companies:", len(rows))
print("On more than one Scenario Shortlist:", ", ".join(f"{s} ({', '.join(sub for sub, _ in entries[s])})" for s in repeated) if repeated else "none")
print("File:", OUT)
PY
```

### Step 2: Read and assess

#### What it does
Assesses every company for the base scenario and the pessimistic scenario.

#### How
Do these four steps in order.

##### 2.1 Read the sub-sectors, the scenarios and the combined file columns
Do these in order.
1. Read `AI Sub-Sectors.md` in full with the **`Reader Script`**. It describes each sub-sector: what it is, its upside, and its downsides.
2. Read `AI Scenarios.md` in full with the **`Reader Script`**. It defines the base and pessimistic scenarios and says how each sub-sector is likely to be affected in each. Its **Company Scenario Considerations** section says how to judge a company in each scenario. Read that section closely, because you will use it for every company.
3. Read the **`Combined File Columns`**, near the top of this prompt. It says what each column of the combined file means and what the earlier reads were based on.

###### Reading the files
- The only files you read in 2.1 are `AI Sub-Sectors.md` and `AI Scenarios.md`. Do not look anything up.
- After chunk 1 of each file, say how many chunks there are, and report your progress after every ten chunks.

##### 2.2 Read the combined file and assess
Read the combined file, `data/screener/AI Subsectors/all_combined.md`, in full, with the **`Reader Script`**. It has one row per company, with the columns described in **`Combined File Columns`**.

###### Reading the combined file
- The only file you read in 2.2 is `data/screener/AI Subsectors/all_combined.md`. Do not look anything up.
- After chunk 1, say how many chunks there are, and report your progress after every ten chunks.

###### Assessing the companies
As you finish each chunk, write a base read and a pessimistic read for each company in it, as working drafts in your reply. Judge each company on its own, for how it would fare in each scenario. Step 4 compares the companies with each other. Every company here was already among the best in its sub-sector, so look closely at what could hold it back.

Judge each read from two sources:
- How the company's sub-sectors fare in that scenario: `AI Scenarios.md` and `AI Sub-Sectors.md`.
- How the company itself fares: the **Company Scenario Considerations** in `AI Scenarios.md`.

Use the company's row like this:
- Everything in the row compared the company only with others in its sub-sector, apart from the percentiles. Use the sub-sector reads as a starting point to test, not to copy.
- For a company on more than one Scenario Shortlist, judge how each of its sub-sectors fares in that scenario and how that affects the company. Weight each sub-sector by how central it is to the company, from its fit tier and fit reason. Then write one read that combines them and names each sub-sector's effect.

Each read is two or three complete sentences and includes the figures it rests on, taken from the earlier reads. A company on more than one Scenario Shortlist may need more, to cover each of its sub-sectors.

##### 2.3 Write the reads file
After the last chunk, write all the reads to the reads file, `data/screener/AI Subsectors/all_reads.md`, with the Write tool, copying them exactly as you wrote them in 2.2.
- One company per line, as `SYMBOL | base read | pessimistic read`, in the order of `data/screener/AI Subsectors/all_combined.md`.
- Do not use the `|` symbol within a read, because it separates the parts of each line.
- The file contains the reads and nothing else.

##### 2.4 Check the reads file
Re-read the reads file, `data/screener/AI Subsectors/all_reads.md`, and answer these in your reply. If any answer is no, fix the file and answer that question again:
- Before you wrote any read, did you read `AI Sub-Sectors.md` and `AI Scenarios.md` in full with the **`Reader Script`**, and the **`Combined File Columns`**?
- Did you read every chunk of `data/screener/AI Subsectors/all_combined.md` through "end of file" with the **`Reader Script`**, one at a time? How many chunks was that?
- Does every company in the combined file have a base read and a pessimistic read, each with the figures it rests on? Are the reads for the last companies as thorough as the reads for the first?
- Does each read in the file match the one you wrote in 2.2?
- Is each read about the scenario it is labeled for? Does it reflect how the company's sub-sectors fare in that scenario, as `AI Sub-Sectors.md` and `AI Scenarios.md` describe it, and does it weigh the company as the **Company Scenario Considerations** in `AI Scenarios.md` describe?
- Did you judge each company on its own, testing the sub-sector reads rather than copying them?
- For each company on more than one Scenario Shortlist, does each read name the effect of each of its sub-sectors, weighted by its fit tier and fit reason?
- Where two companies with similar figures got different reads, can you say why?

#### Required output
`data/screener/AI Subsectors/all_reads.md`. In your reply in the chat, answer the self-check questions. Do not put them in the file.

### Step 3: Build the assessed file

#### What it does
Adds each company's base read and pessimistic read to its row.

#### How
Run the script below as a single inline command: `python3 - <<'PY'`

The script builds the assessed file, `data/screener/AI Subsectors/all_assessed.md`: the combined file, `data/screener/AI Subsectors/all_combined.md`, with a Base read and a Pessimistic read column added from the reads file, `data/screener/AI Subsectors/all_reads.md`.

First, it checks:
- Every row of the combined file is complete.
- Every line of the reads file has the form `SYMBOL | base read | pessimistic read`, and neither read is empty.
- Every symbol in the reads file is in the combined file, and none appears twice.
- Every company in the combined file has reads.

If a check fails, the script prints the problems and stops without building anything. Fix the reads file and run the script again.

#### Required output
`data/screener/AI Subsectors/all_assessed.md`, and what the script printed: the number of companies.

#### Script
```bash
python3 - <<'PY'
import sys

DIR = "data/screener/AI Subsectors"
COMBINED = f"{DIR}/all_combined.md"
READS = f"{DIR}/all_reads.md"
OUT = f"{DIR}/all_assessed.md"

def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

header, rows = None, []
with open(COMBINED, encoding="utf-8") as fh:
    for line in fh:
        if not line.lstrip().startswith("|"):
            continue
        c = cells(line)
        if header is None:
            header = c
        elif all(x and set(x) <= set(":-") for x in c):
            continue
        else:
            rows.append(c)
si = header.index("Symbol")
symbols = [r[si] for r in rows]

problems, reads = [], {}
for n, r in enumerate(rows, 1):
    if len(r) != len(header):
        problems.append(f"{COMBINED} row {n}: expected {len(header)} columns, found {len(r)}")
with open(READS, encoding="utf-8") as fh:
    lines = [(n, l.strip()) for n, l in enumerate(fh, 1) if l.strip()]
for n, line in lines:
    parts = [p.strip() for p in line.split("|")]
    if len(parts) != 3:
        problems.append(f"Line {n}: not in the form SYMBOL | base read | pessimistic read, or a read contains a pipe: {line[:80]}")
        continue
    symbol, base, pess = parts
    if not base or not pess:
        problems.append(f"Line {n}: a read is empty ({symbol})")
    if symbol not in symbols:
        problems.append(f"Line {n}: {symbol} is not in {COMBINED}")
    if symbol in reads:
        problems.append(f"Line {n}: {symbol} appears more than once")
    reads[symbol] = (base, pess)
for s in symbols:
    if s not in reads:
        problems.append(f"{s} has no reads")

if problems:
    print("There are problems. Nothing was built.")
    print("\n".join(problems))
    sys.exit(1)

with open(OUT, "w", encoding="utf-8") as out:
    out.write("| " + " | ".join(header + ["Base read", "Pessimistic read"]) + " |\n")
    out.write("|" + "---|" * (len(header) + 2) + "\n")
    for r in rows:
        b, p = reads[r[si]]
        out.write("| " + " | ".join(r + [b, p]) + " |\n")
print("Companies:", len(rows))
print("File:", OUT)
PY
```

### Step 4: Rank

#### What it does
Ranks the companies from best to worst in the base scenario and in the pessimistic scenario.

#### How
Do these five steps in order.

##### 4.1 Read the assessed file
Read the assessed file, `data/screener/AI Subsectors/all_assessed.md`, in full, with the **`Reader Script`**. It has one row per company: the columns described in **`Combined File Columns`**, then the base read and the pessimistic read.

###### Reading the assessed file
- The only file you read in this step is `data/screener/AI Subsectors/all_assessed.md`. Do not look anything up.
- After chunk 1, say how many chunks there are, and report your progress after every ten chunks.

##### 4.2 Rank the companies for the base scenario
Rank the companies by how well each would fare in the base scenario, compared with the companies from every sub-sector. Comparisons in the rows are only within one sub-sector. This ranking is the first across all of them. Base the ranking on the base reads, and use the rest of each row as support. Leave out the pessimistic reads. Judge what counts most in base as the **Company Scenario Considerations** in `AI Scenarios.md` describe.
1. Go through the chunks one at a time. For each chunk, list its companies from best to worst in the base scenario. Write each list in your reply.
2. When you have done every chunk, rank all the companies together, from best to worst. Use the chunk lists as a starting point, not as the answer. Compare companies from different chunks, and re-rank all of them. This is the base ranking.

##### 4.3 Rank the companies for the pessimistic scenario
Rank the companies by how well each would fare in the pessimistic scenario, compared with the companies from every sub-sector. Comparisons in the rows are only within one sub-sector. This ranking is the first across all of them. Base the ranking on the pessimistic reads, and use the rest of each row as support. Leave out the base reads, and do not use your base ranking. Judge what counts most in pessimistic as the **Company Scenario Considerations** in `AI Scenarios.md` describe.
1. Go through the chunks one at a time. For each chunk, list its companies from best to worst in the pessimistic scenario. Write each list in your reply.
2. When you have done every chunk, rank all the companies together, from best to worst. Use the chunk lists as a starting point, not as the answer. Compare companies from different chunks, and re-rank all of them. This is the pessimistic ranking.

##### 4.4 Write the ranks file
Write both rankings to the ranks file, `data/screener/AI Subsectors/all_ranks.md`, with the Write tool, copying them exactly.
- One company per line, as `SYMBOL | base rank | pessimistic rank`, in the order of `data/screener/AI Subsectors/all_assessed.md`.
- Each rank is a whole number from 1 to the number of companies, with no ties and no gaps.
- The file contains the ranks and nothing else.

##### 4.5 Check the ranks file
Re-read the ranks file, `data/screener/AI Subsectors/all_ranks.md`, and answer these in your reply. If any answer is no, fix the file and answer that question again:
- Did you read every chunk of `data/screener/AI Subsectors/all_assessed.md` through "end of file" with the **`Reader Script`**, one at a time? How many chunks was that?
- Did you rank every company in each scenario, re-ranking all of them together after the chunk lists? Were the last chunks ranked as carefully as the first?
- Did you rank each scenario from its own reads, leaving out the other scenario's, and without using one ranking for the other?
- Does each company's rank fit its read? Where it does not, can you say why?
- Where two companies with similar reads got different ranks, can you say why?
- Does each rank in the file match your rankings?

#### Required output
`data/screener/AI Subsectors/all_ranks.md`. In your reply in the chat, answer the self-check questions. Do not put them in the file.

### Step 5: Build the ranked file

#### What it does
Adds each company's base rank and pessimistic rank to its row.

#### How
Run the script below as a single inline command: `python3 - <<'PY'`

The script builds the ranked file, `data/screener/AI Subsectors/all_ranked.md`: the assessed file, `data/screener/AI Subsectors/all_assessed.md`, with a Base rank and a Pessimistic rank column added from the ranks file, `data/screener/AI Subsectors/all_ranks.md`.

First, it checks:
- Every row of the assessed file is complete.
- Every line of the ranks file has the form `SYMBOL | base rank | pessimistic rank`, with whole-number ranks.
- Every company in the assessed file has ranks, and none appears twice.
- Each set of ranks runs from 1 to the number of companies, with no ties and no gaps.

If a check fails, the script prints the problems and stops without building anything. Fix the assessed file or the ranks file, and run the script again.

After it builds the ranked file, it reads it back and checks it against the assessed file. It must have the same rows in the same order, with every cell unchanged and only the two rank columns added. If this check fails, the script says so and deletes the ranked file.

#### Required output
`data/screener/AI Subsectors/all_ranked.md`, and what the script printed: the number of companies and that the check against the assessed file passed.

#### Script
```bash
python3 - <<'PY'
import os, sys

DIR = "data/screener/AI Subsectors"
ASSESSED = f"{DIR}/all_assessed.md"
RANKS = f"{DIR}/all_ranks.md"
OUT = f"{DIR}/all_ranked.md"

def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

def is_rule(c):
    return all(x and set(x) <= set(":-") for x in c)

header, rows = None, []
with open(ASSESSED, encoding="utf-8") as fh:
    for line in fh:
        if not line.lstrip().startswith("|"):
            continue
        c = cells(line)
        if header is None:
            header = c
        elif is_rule(c):
            continue
        else:
            rows.append(c)
si = header.index("Symbol")
symbols = [r[si] for r in rows]

problems, ranks = [], {}
for n, r in enumerate(rows, 1):
    if len(r) != len(header):
        problems.append(f"{ASSESSED} row {n}: expected {len(header)} columns, found {len(r)}. A read may contain a pipe.")
with open(RANKS, encoding="utf-8") as fh:
    lines = [(n, l.strip()) for n, l in enumerate(fh, 1) if l.strip()]
for n, line in lines:
    parts = [p.strip() for p in line.split("|")]
    if len(parts) != 3:
        problems.append(f"Line {n}: not in the form SYMBOL | base rank | pessimistic rank: {line[:80]}")
        continue
    symbol, b, p = parts
    if not (b.isdigit() and p.isdigit()):
        problems.append(f"Line {n}: ranks must be whole numbers ({symbol})")
        continue
    if symbol not in symbols:
        problems.append(f"Line {n}: {symbol} is not in {ASSESSED}")
    if symbol in ranks:
        problems.append(f"Line {n}: {symbol} appears more than once")
    ranks[symbol] = (int(b), int(p))
for s in symbols:
    if s not in ranks:
        problems.append(f"{s} has no ranks")
N = len(symbols)
if not problems:
    for i, name in ((0, "base"), (1, "pessimistic")):
        if sorted(v[i] for v in ranks.values()) != list(range(1, N + 1)):
            problems.append(f"The {name} ranks must be 1 to {N} with no ties and no gaps")

if problems:
    print("There are problems. Nothing was built.")
    print("\n".join(problems))
    sys.exit(1)

with open(OUT, "w", encoding="utf-8") as out:
    out.write("| " + " | ".join(header + ["Base rank", "Pessimistic rank"]) + " |\n")
    out.write("|" + "---|" * (len(header) + 2) + "\n")
    for r in rows:
        b, p = ranks[r[si]]
        out.write("| " + " | ".join(r + [str(b), str(p)]) + " |\n")

built, check = [], []
with open(OUT, encoding="utf-8") as fh:
    for line in fh:
        c = cells(line)
        if c and not is_rule(c):
            built.append(c)
if len(built) != len(rows) + 1:
    check.append(f"{OUT} has {len(built) - 1} rows, {ASSESSED} has {len(rows)}")
else:
    if built[0][:-2] != header:
        check.append("The header columns changed")
    for orig, new in zip(rows, built[1:]):
        if new[:-2] != orig:
            check.append(f"The row for {orig[si]} changed")
if check:
    os.remove(OUT)
    print(f"The check against {ASSESSED} failed. {OUT} was deleted.")
    print("\n".join(check))
    sys.exit(1)
print("Companies:", len(rows))
print(f"Check against {ASSESSED}: passed")
print("File:", OUT)
PY
```

### Step 6: Review

#### What it does
Reviews each company's reads and ranks against its row, and corrects the ones that do not hold up.

#### How
Do these seven steps in order.

##### 6.1 Re-read the sub-sectors, the scenarios and the combined file columns
Read these again, in this order:
1. `AI Sub-Sectors.md`, in full, with the **`Reader Script`**.
2. `AI Scenarios.md`, in full, with the **`Reader Script`**, including its **Company Scenario Considerations** section.
3. The **`Combined File Columns`**, near the top of this prompt.

###### Reading the files
- After chunk 1 of each file, say how many chunks there are, and report your progress after every ten chunks.

##### 6.2 Read the ranked file
Read the ranked file, `data/screener/AI Subsectors/all_ranked.md`, in full, with the **`Reader Script`**. It has one row per company: the columns described in **`Combined File Columns`**, the base read, the pessimistic read, the base rank and the pessimistic rank.

###### Reading the ranked file
- The only files you read in Step 6 are `AI Sub-Sectors.md`, `AI Scenarios.md` and `data/screener/AI Subsectors/all_ranked.md`. Do not look anything up.
- After chunk 1, say how many chunks there are, and report your progress after every ten chunks.

##### 6.3 Review the reads
The reads and ranks in the file are a first attempt to test, not to defend. Do not anchor to them. You may disagree with any read or rank.

Go through the chunks one at a time, and every company in each chunk. Assess each company again as if you were doing it for the first time, and check each of its reads:
- Does it follow from the rest of the row? Check every comparison in it against the earlier reads, and remember that their comparisons are only within one sub-sector.
- Does it reflect how the company's sub-sectors fare in that scenario, as `AI Sub-Sectors.md` and `AI Scenarios.md` describe?
- Does it weigh the company as the **Company Scenario Considerations** in `AI Scenarios.md` describe?
- For a company on more than one Scenario Shortlist, does it name the effect of each sub-sector, weighted by its fit tier and fit reason?

Write each read you would change, and the new read, in your reply.

##### 6.4 Review the ranks
After the last chunk, review the base ranking and then the pessimistic ranking, each across all the companies. Review each ranking from its own scenario's reads, without the other scenario's. For each ranking, check:
- Does each company's rank fit its read, with the reads as you changed them in 6.3?
- Does the order make sense when all the companies are compared together, across sub-sectors? Take the most care over the top of each ranking, because the Composite Shortlist is drawn from the companies that rank well.

Write each rank you would change in your reply.

##### 6.5 Make the corrections
The ranked file is built from the assessed file and the ranks file, so make the corrections in those two files and rebuild it. Do not edit the ranked file.
1. Reads: for each read you changed in 6.3, edit it in the assessed file, `data/screener/AI Subsectors/all_assessed.md`, with the Edit tool. Do not use the `|` symbol within a read.
2. Ranks: write all the ranks again, with your changes from 6.4, to the ranks file, `data/screener/AI Subsectors/all_ranks.md`, with the Write tool, in the format from 4.4. Each ranking still runs from 1 to the number of companies, with no ties and no gaps.
3. Run the Step 5 script again. It rebuilds the ranked file with the new reads and ranks.

Change only the base and pessimistic reads and ranks. Do not change any other column, or which companies are in the file.

##### 6.6 Write the note
Write a short note to the note file, `data/screener/AI Subsectors/all_note.md`, with the Write tool.
- A few sentences on what put companies in the Both scenarios table (the companies with the best average of their base rank and pessimistic rank, which Step 7 keeps), what drove the top of the base ranking and the top of the pessimistic ranking, and why the other companies fell short. Give only the key figures.
- The file contains the note and nothing else.

##### 6.7 Check the ranked file
Re-read the ranked file, `data/screener/AI Subsectors/all_ranked.md`, and answer these in your reply. If any answer is no, fix it and answer that question again:
- Did you re-read `AI Sub-Sectors.md` and `AI Scenarios.md` in full with the **`Reader Script`**, and the **`Combined File Columns`**?
- Did you read every chunk of the ranked file through "end of file" with the **`Reader Script`**, one at a time? How many chunks was that?
- Did you review every company's reads and both rankings as if for the first time? How many reads and ranks did you change?
- Does each read follow from the rest of its row, and from how `AI Sub-Sectors.md`, `AI Scenarios.md` and the **Company Scenario Considerations** describe its sub-sectors and the scenario?
- Does each rank fit its read, with each ranking based only on its own scenario's reads? Where two companies with similar reads got different ranks, can you say why?
- Did you make the corrections in the assessed file and the ranks file, and run the Step 5 script again?
- Did you check every ranking claim, comparison and superlative in the note against the final ranks and the rows?

#### Required output
The ranked file, `data/screener/AI Subsectors/all_ranked.md`, rebuilt with your corrections, and the note file, `data/screener/AI Subsectors/all_note.md`. In your reply in the chat, list what you changed and why. Then answer the self-check questions. Do not put either in the file.

### Step 7: Build the Composite Shortlist

#### What it does
Builds the Composite Shortlist file: the note, the companies that fare best across both scenarios, and the companies that fare best in each.

#### How
Run the script below as a single inline command: `python3 - <<'PY'`

The script builds the Composite Shortlist file, `data/screener/AI Subsectors/AI Composite Shortlist {MM-DD-YY}.md`, dated today, from the ranked file, `data/screener/AI Subsectors/all_ranked.md`, and the note file, `data/screener/AI Subsectors/all_note.md`. The note comes first, as one paragraph, then three tables:
- Both scenarios: the companies with the best average of their base rank and pessimistic rank, with equal weight. It keeps the best 30. If companies tie at 30th place, it keeps all of them, so the list can run over 30.
- Base: the top 10 of the base ranking, and whether each is in the Both scenarios table.
- Pessimistic: the top 10 of the pessimistic ranking, and whether each is in the Both scenarios table.

First, it checks:
- The note file exists and is not empty.
- The ranked file has the columns it needs, and every row is complete.
- The base ranks and the pessimistic ranks each run from 1 to the number of companies, with no ties and no gaps, and no symbol appears twice.

If a check fails, the script prints the problems and stops without building or deleting anything. Fix the note file, or fix the assessed file or the ranks file and run the Step 5 script again. Then run this script again.

After it writes the file, it reads it back and checks that it matches the rows it chose. If it does not, it deletes the new file and nothing else. If it does, it deletes the working files: `all_combined.md`, `all_reads.md`, `all_assessed.md`, `all_ranks.md`, `all_ranked.md` and `all_note.md`.

#### Required output
The Composite Shortlist file, `data/screener/AI Subsectors/AI Composite Shortlist {MM-DD-YY}.md`, and what the script printed: the number of companies in the Both scenarios table and its cutoff, the companies in it that are on more than one Scenario Shortlist, the companies in the base and pessimistic top 10 that are not in it, and the files it deleted.

#### Script
```bash
python3 - <<'PY'
import datetime, os, sys

DIR = "data/screener/AI Subsectors"
RANKED = f"{DIR}/all_ranked.md"
NOTE = f"{DIR}/all_note.md"
OUT = f"{DIR}/AI Composite Shortlist {datetime.date.today().strftime('%m-%d-%y')}.md"
SCRATCH = [f"{DIR}/all_{name}.md" for name in ("combined", "reads", "assessed", "ranks", "ranked", "note")]
TOP = 30
SCENARIO_TOP = 10

def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

def is_rule(c):
    return all(x and set(x) <= set(":-") for x in c)

if not os.path.exists(NOTE) or not open(NOTE, encoding="utf-8").read().strip():
    sys.exit(f"{NOTE} is missing or empty. Nothing was built.")
note = " ".join(open(NOTE, encoding="utf-8").read().split())

header, rows = None, []
with open(RANKED, encoding="utf-8") as fh:
    for line in fh:
        if not line.lstrip().startswith("|"):
            continue
        c = cells(line)
        if header is None:
            header = c
        elif is_rule(c):
            continue
        else:
            rows.append(c)

need = ["Symbol", "Company", "Sub-sectors", "Fit reason", "Potential growth", "Current growth", "Strength",
        "Price", "Why", "Base read", "Pessimistic read", "Base rank", "Pessimistic rank"]
missing = [n for n in need if n not in header]
if missing:
    sys.exit(f"{RANKED} has no column: {', '.join(missing)}")
ix = {n: header.index(n) for n in need}
N = len(rows)

problems = []
for i, r in enumerate(rows, 1):
    if len(r) != len(header):
        problems.append(f"Table row {i}: expected {len(header)} columns, found {len(r)}")
if not problems:
    for name in ("Base rank", "Pessimistic rank"):
        vals = [r[ix[name]] for r in rows]
        if not all(v.isdigit() for v in vals) or sorted(int(v) for v in vals) != list(range(1, N + 1)):
            problems.append(f"The {name} column must be the whole numbers 1 to {N}, with no ties and no gaps")
    if len({r[ix["Symbol"]] for r in rows}) != N:
        problems.append("A symbol appears more than once")
if problems:
    print(f"{RANKED} has problems. Nothing was built.")
    print("\n".join(problems))
    sys.exit(1)

def br(r): return int(r[ix["Base rank"]])
def pr(r): return int(r[ix["Pessimistic rank"]])

companies = sorted(rows, key=lambda r: (br(r) + pr(r), min(br(r), pr(r)), r[ix["Symbol"]]))
cutoff = br(companies[min(TOP, N) - 1]) + pr(companies[min(TOP, N) - 1])
composite = [r for r in companies if br(r) + pr(r) <= cutoff]
on_composite = {r[ix["Symbol"]] for r in composite}

comp_header = ["Symbol", "Company", "Sub-sectors", "Fit reason", "Potential growth", "Current growth", "Strength",
               "Price", "Why", "Base read", "Pessimistic read", "Base rank", "Pessimistic rank", "Average rank"]
comp_rows = [[r[ix[n]] for n in comp_header[:-1]] + [f"{(br(r) + pr(r)) / 2:.1f}"] for r in composite]

def scenario_table(rank_col, read_col, other_col):
    top = sorted(rows, key=lambda r: int(r[ix[rank_col]]))[:SCENARIO_TOP]
    h = ["Symbol", "Company", "Sub-sectors", rank_col, other_col, "In Both scenarios table", read_col]
    return h, [[r[ix["Symbol"]], r[ix["Company"]], r[ix["Sub-sectors"]], r[ix[rank_col]], r[ix[other_col]],
                "yes" if r[ix["Symbol"]] in on_composite else "no", r[ix[read_col]]] for r in top]

tables = [("Both scenarios", comp_header, comp_rows),
          ("Base", *scenario_table("Base rank", "Base read", "Pessimistic rank")),
          ("Pessimistic", *scenario_table("Pessimistic rank", "Pessimistic read", "Base rank"))]

with open(OUT, "w", encoding="utf-8") as out:
    out.write(note + "\n")
    for title, h, rs in tables:
        out.write(f"\n## {title}\n\n")
        out.write("| " + " | ".join(h) + " |\n")
        out.write("|" + "---|" * len(h) + "\n")
        for r in rs:
            out.write("| " + " | ".join(r) + " |\n")

built, current = {}, None
with open(OUT, encoding="utf-8") as fh:
    first = fh.readline().strip()
    for line in fh:
        if line.startswith("## "):
            current = line[3:].strip()
            built[current] = []
        elif line.lstrip().startswith("|") and current:
            c = cells(line)
            if not is_rule(c):
                built[current].append(c)
if first != note or any(built.get(t) != [h] + rs for t, h, rs in tables):
    os.remove(OUT)
    sys.exit(f"The file written does not match the rows chosen from {RANKED}. {OUT} was deleted. Nothing else was deleted.")

for path in SCRATCH:
    if os.path.exists(path):
        os.remove(path)
print("Both scenarios:", len(comp_rows), f"companies (average rank cutoff {cutoff / 2:.1f}; {max(0, len(comp_rows) - TOP)} above {TOP} because of ties)")
print("On more than one Scenario Shortlist:", ", ".join(r[0] for r in comp_rows if "), " in r[2]) or "none")
for title, h, rs in tables[1:]:
    missed = [r[0] for r in rs if r[5] == "no"]
    print(f"{title} top {len(rs)}, not in the Both scenarios table:", ", ".join(missed) or "none")
print("Deleted:", ", ".join(os.path.basename(p) for p in SCRATCH))
print("File:", OUT)
PY
```
