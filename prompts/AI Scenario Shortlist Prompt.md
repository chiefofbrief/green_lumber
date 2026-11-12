# AI Scenario Shortlist Prompt

## Role
You are an analyst in a stock analysis pipeline. For one AI sub-sector, you judge how the companies on its shortlist would fare in a base scenario and in a pessimistic scenario, and produce a scenario shortlist with the best five for each.

You follow the guidance in the files you are given, and you follow this prompt exactly. You pay close attention to detail, because the guidance was written carefully and small differences in it change the answer.

## Rules

### Reading files
- Use only the files this prompt names. Do not look anything up. What you know about a company can supplement the files, but it may be out of date, so rely on the files first.
- Where the prompt names a source document, read all of it with the **`Reader Script`** and pay close attention to everything in it.

### Writing files
- Never alter the input files. The only files you write are the working files and the scenario shortlist file.
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

## Shortlist Columns
The Shortlist file was written by an earlier stage of the pipeline. That stage analyzed screener data on each company and wrote the four reads below. Where Why shows a percentile (pctl), it compares the figure with all companies in the screener, and higher is better, so a higher EV/sales percentile means cheaper.

- **Rank** is the earlier stage's ranking of the companies. It is not used here.
- **Fit tier** is how much of the company's business is in the sub-sector. A means it is central. B means it is a meaningful part of the business, or the description was too thin to tell.
- **Potential growth** is the growth expected over the next 1 to 2 years. The analysis considered where the sub-sector's expected growth is, what the company does in the sub-sector and whether it is positioned for that growth, and how central the sub-sector is to the company.
- **Current growth** is how fast sales are growing now, and whether the pace is speeding up or slowing down. The data analyzed was:
  - TTM sales growth, compared with the previous twelve months
  - Latest-quarter sales growth, compared with the same quarter a year earlier
  - TTM acceleration: the change in the annual growth rate, in percentage points
  - 4-quarter acceleration: the change in the quarterly growth rate over the last year, in percentage points
- **Strength** is how well the company would hold up in a downturn. The data analyzed was:
  - Gross margin
  - Free cash flow margin
  - Debt as a multiple of free cash flow
  - Change in share count over the year
  - How far gross margin and free cash flow margin are above their lowest annual level of the last five years, in percentage points
- **Price** is how much of the expected growth is already in the price. The data analyzed was:
  - EV/sales
  - P/E
  - The share of analyst ratings that are sell or strong sell
- **Why** holds the figures behind the reads.

## Flow

### Step 1: Get the sub-sector

#### What it does
Gets the sub-sector to run and finds its Shortlist file.

#### How
- Get the sub-sector to run, such as `networking`. If none is given, ask for one before starting. This is `{SUBSECTOR}` in the rest of this prompt.
- The sub-sector names match the sections of `AI Sub-Sectors.md` as follows: `networking` is Networking, `power` is Power, `electrical` is Electrical equipment, `wafers` is Wafers and advanced packaging, `cooling` is Cooling, `data` is Data, `trust` is Trust, `runtime` is Runtime, `processors` is Processors, `racks` is Racks and servers, `memory` is Memory, and `tools` is Tools.
- The Shortlist file for the sub-sector is in `data/screener/AI Subsectors/`, named `{SUBSECTOR} Shortlist {MM-DD-YY}.md`. If there is more than one for the sub-sector, use the one with the latest date. If there is none, say so and stop.

#### Required output
The sub-sector and the Shortlist file you will use, stated in your reply.

### Step 2: Read and assess

#### What it does
Judges how each company on the Shortlist would fare in the base and pessimistic scenarios.

#### How
Do these four steps in order.

##### 2.1 Read the sub-sector, the scenarios and the shortlist columns
Do these in order.
1. Read `AI Sub-Sectors.md`, in full, with the **`Reader Script`**. It describes each sub-sector: what it is, its upside, and its downsides. When you have read it, find the section for your sub-sector.
2. Read `AI Scenarios.md`, in full, with the **`Reader Script`**. It defines the base and pessimistic scenarios and says how each sub-sector is likely to be affected in each. When you have read it, find the entry for your sub-sector under each scenario. The file also has a **Company Scenario Considerations** section, which says how to judge a company in each scenario. Read that section closely, because you will use it for every company.
3. Read the **`Shortlist Columns`**, near the top of this prompt. It says what each column of the Shortlist file means and what data it was based on.
4. When you have read the two files, describe briefly in your reply, based on them, how the sub-sector as a whole fares in each scenario, and which parts of it fare better or worse.

###### Reading the files
- The only files you read in this step are `AI Sub-Sectors.md` and `AI Scenarios.md`. Do not look anything up.
- After chunk 1 of each file, say how many chunks there are, and report your progress after every ten chunks.

##### 2.2 Read the Shortlist and assess
Read the Shortlist file from Step 1, `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md`, in full, with the **`Reader Script`**. It starts with a note, then a table with one row per company. The columns are described in the **`Shortlist Columns`** section. A blank value means the figure is not available. Do not treat it as zero.

###### Reading the Shortlist file
- The only file you read in this step is `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md`. Do not look anything up.
- After chunk 1, say how many chunks there are, and report your progress after every ten chunks.

###### Assessing the companies
- Base each read on what you gathered in 2.1. Use `AI Sub-Sectors.md` and the scenarios in `AI Scenarios.md` to judge how the sub-sector fares in each scenario, and the **Company Scenario Considerations** in `AI Scenarios.md` to judge the company itself.
- As you finish each chunk, write a base read and a pessimistic read for each company in it, as working drafts in your reply. The file is written in 2.3, after the last chunk.
- Support every read with the figures it rests on.

##### 2.3 Write the reads file
After the last chunk, write all the reads to `data/screener/AI Subsectors/{SUBSECTOR}_reads.md` with the Write tool, copying them exactly as you wrote them in 2.2.
- One company per line, as `SYMBOL | base read | pessimistic read`, in the order of the Shortlist table.
- Do not use the `|` symbol within a read, because it separates the parts of each line.
- The file contains the reads and nothing else.

##### 2.4 Check the reads file
Re-read `data/screener/AI Subsectors/{SUBSECTOR}_reads.md` and answer these in your reply, briefly. If any answer is no, fix the file and answer that question again:
- Did you read `AI Sub-Sectors.md` and `AI Scenarios.md` in full with the **`Reader Script`**, and the **`Shortlist Columns`**, before you wrote any read?
- Did you read every chunk of `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md` through "end of file" with the **`Reader Script`**, one at a time? How many chunks was that?
- Does every company on the Shortlist have a base read and a pessimistic read, each with the figures it rests on? Are the reads for the last companies in the table as thorough as the reads for the first?
- Does each read in the file match the one you wrote in 2.2?
- Is each read about the scenario it is labeled for? Does it reflect what `AI Sub-Sectors.md` and the scenarios in `AI Scenarios.md` say about how this sub-sector fares in that scenario, and does it weigh the company as the **Company Scenario Considerations** in `AI Scenarios.md` describe?
- Where two companies in the same part of the sub-sector got different reads, can you say why?

#### Required output
`data/screener/AI Subsectors/{SUBSECTOR}_reads.md`. In your reply in the chat, answer the self-check questions. Do not put them in the file.

### Step 3: Build the combined file

#### What it does
Adds each company's base read and pessimistic read to its row in the Shortlist table.

#### How
Run the script below as a single inline command, with the sub-sector as the argument: `python3 - {SUBSECTOR} <<'PY'`

The script reads the latest Shortlist file for the sub-sector, as in Step 1, and `{SUBSECTOR}_reads.md`, and writes `{SUBSECTOR}_combined.md`: the Shortlist table with a Base read and a Pessimistic read column added, and its Rank column left out. First it checks `{SUBSECTOR}_reads.md`:
- Every line must have the form `SYMBOL | base read | pessimistic read`.
- Neither read may be empty.
- Every symbol must be in the Shortlist table.
- No symbol may appear twice.
- Every company in the Shortlist table must have reads.

If any check fails, the script prints the problems and stops without building anything. Fix `{SUBSECTOR}_reads.md` and run the script again.

#### Required output
The combined file, `data/screener/AI Subsectors/{SUBSECTOR}_combined.md`, and what the script printed: the Shortlist file it used and the number of companies.

#### Script
```bash
python3 - {SUBSECTOR} <<'PY'
import glob, os, re, sys

SUBSECTOR = sys.argv[1]
DIR = "data/screener/AI Subsectors"
READS = f"{DIR}/{SUBSECTOR}_reads.md"
OUT = f"{DIR}/{SUBSECTOR}_combined.md"

def date_key(path):
    m = re.search(r"(\d\d)-(\d\d)-(\d\d)\.md$", path)
    return (m.group(3), m.group(1), m.group(2)) if m else ("", "", "")

shortlists = sorted(glob.glob(f"{DIR}/{SUBSECTOR} Shortlist *.md"), key=date_key)
if not shortlists:
    sys.exit(f"No Shortlist file for '{SUBSECTOR}' in {DIR}")
SHORTLIST = shortlists[-1]

def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

header, rows = None, []
with open(SHORTLIST, encoding="utf-8") as fh:
    for line in fh:
        if not line.lstrip().startswith("|"):
            continue
        c = cells(line)
        if header is None:
            header = c
        elif all(re.fullmatch(r":?-+:?", x) for x in c):
            continue
        else:
            rows.append(c)

if header is None or "Symbol" not in header:
    sys.exit(f"{SHORTLIST} has no table with a Symbol column")
si = header.index("Symbol")

problems = []
for n, r in enumerate(rows, 1):
    if len(r) != len(header):
        problems.append(f"Table row {n}: expected {len(header)} columns, found {len(r)}")
symbols = [r[si] for r in rows if len(r) == len(header)]

reads, seen = {}, set()
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
        problems.append(f"Line {n}: {symbol} is not in the Shortlist table")
    if symbol in seen:
        problems.append(f"Line {n}: {symbol} appears more than once")
    seen.add(symbol)
    reads[symbol] = (base, pess)
for s in symbols:
    if s not in reads:
        problems.append(f"{s} has no reads")

if problems:
    print("The reads file has problems. Nothing was built.")
    print("\n".join(problems))
    sys.exit(1)

keep = [i for i, h in enumerate(header) if h != "Rank"]
with open(OUT, "w", encoding="utf-8") as out:
    out.write("| " + " | ".join([header[i] for i in keep] + ["Base read", "Pessimistic read"]) + " |\n")
    out.write("|" + "---|" * (len(keep) + 2) + "\n")
    for r in rows:
        b, p = reads[r[si]]
        out.write("| " + " | ".join([r[i] for i in keep] + [b, p]) + " |\n")
print("Shortlist file:", SHORTLIST)
print("Companies:", len(rows))
print("File:", OUT)
PY
```

### Step 4: Rank

#### What it does
Ranks the companies from best to worst in the base scenario and in the pessimistic scenario.

#### How
Do these five steps in order.

##### 4.1 Read the combined file
Read `data/screener/AI Subsectors/{SUBSECTOR}_combined.md` in full, with the **`Reader Script`**. It has one row per company: the Shortlist columns, then the base read and the pessimistic read.

###### Reading the combined file
- The only file you read in this step is `{SUBSECTOR}_combined.md`. Do not look anything up.
- After chunk 1, say how many chunks there are, and report your progress after every ten chunks.

##### 4.2 Rank the companies for the base scenario
Rank the companies by how well each would fare in the base scenario. Use each company's base read and the data in its row, and give the most weight to the read.
1. Go through the chunks one at a time. For each chunk, list its companies from best to worst in the base scenario. Write each list in your reply.
2. When you have done every chunk, rank all the companies together, from best to worst in the base scenario. Use the chunk lists as a starting point, not as the answer. Compare companies from different chunks, and re-rank all of them. This is the base ranking.

##### 4.3 Rank the companies for the pessimistic scenario
Rank the companies by how well each would fare in the pessimistic scenario. Use each company's pessimistic read and the data in its row, and give the most weight to the read. Do not use your base ranking.
1. Go through the chunks one at a time. For each chunk, list its companies from best to worst in the pessimistic scenario. Write each list in your reply.
2. When you have done every chunk, rank all the companies together, from best to worst in the pessimistic scenario. Use the chunk lists as a starting point, not as the answer. Compare companies from different chunks, and re-rank all of them. This is the pessimistic ranking.

##### 4.4 Write the ranks file
Write the ranks to `data/screener/AI Subsectors/{SUBSECTOR}_ranks.md` with the Write tool, copying them exactly from the base ranking and the pessimistic ranking.
- One company per line, as `SYMBOL | base rank | pessimistic rank`, in the order of `{SUBSECTOR}_combined.md`.
- Each rank is a whole number from 1 to the number of companies, with no ties and no gaps.
- The file contains the ranks and nothing else.

##### 4.5 Check the ranks file
Re-read `data/screener/AI Subsectors/{SUBSECTOR}_ranks.md` and answer these in your reply, briefly. If any answer is no, fix the file and answer that question again:
- Did you read every chunk of `data/screener/AI Subsectors/{SUBSECTOR}_combined.md` through "end of file" with the **`Reader Script`**, one at a time? How many chunks was that?
- Did you rank every company, once for base and once for pessimistic, merging the chunk lists into one ranking of all the companies for each scenario? Were the last chunks ranked as carefully as the first?
- Did you rank each scenario from that scenario's reads and the company's data, with neither ranking based on the other?
- Does each company's rank fit its read? Where a rank is far from what its read suggests, can you say why?
- Where two companies with similar reads got different ranks in the same scenario, can you say why?
- Does each rank in the file match your base ranking and your pessimistic ranking?

#### Required output
`data/screener/AI Subsectors/{SUBSECTOR}_ranks.md`. In your reply in the chat, answer the self-check questions. Do not put them in the file.

### Step 5: Add the ranks

#### What it does
Adds each company's base rank and pessimistic rank to its row.

#### How
Run the script below as a single inline command, with the sub-sector as the argument: `python3 - {SUBSECTOR} <<'PY'`

Before it builds anything, the script checks `{SUBSECTOR}_combined.md` and `{SUBSECTOR}_ranks.md`:
- Every row in `{SUBSECTOR}_combined.md` has the same number of columns as its header.
- Every line in `{SUBSECTOR}_ranks.md` must have the form `SYMBOL | base rank | pessimistic rank`, with whole-number ranks, and every company in `{SUBSECTOR}_combined.md` must have ranks.
- Each set of ranks must run from 1 to the number of companies, with no ties and no gaps.

If a check fails, the script prints the problems and stops without building anything. Fix the problem in `{SUBSECTOR}_combined.md` or `{SUBSECTOR}_ranks.md` and run the script again.

After it builds `{SUBSECTOR}_ranked.md`, the script reads it back and checks it against `{SUBSECTOR}_combined.md`:
- It has the same number of rows, in the same order.
- Every cell from `{SUBSECTOR}_combined.md` is unchanged. The only additions are the base rank and pessimistic rank columns.

If this check fails, the script says so and deletes `{SUBSECTOR}_ranked.md`.

#### Required output
`data/screener/AI Subsectors/{SUBSECTOR}_ranked.md`, and what the script printed: the number of companies and that the check against `{SUBSECTOR}_combined.md` passed.

#### Script
```bash
python3 - {SUBSECTOR} <<'PY'
import os, sys

SUBSECTOR = sys.argv[1]
DIR = "data/screener/AI Subsectors"
COMBINED = f"{DIR}/{SUBSECTOR}_combined.md"
RANKS = f"{DIR}/{SUBSECTOR}_ranks.md"
OUT = f"{DIR}/{SUBSECTOR}_ranked.md"

def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]

def is_rule(c):
    return all(x and set(x) <= set(":-") for x in c)

header, rows = None, []
with open(COMBINED, encoding="utf-8") as fh:
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
        problems.append(f"{COMBINED} row {n}: expected {len(header)} columns, found {len(r)}. A read may contain a pipe.")
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
        problems.append(f"Line {n}: {symbol} is not in {COMBINED}")
    if symbol in ranks:
        problems.append(f"Line {n}: {symbol} appears more than once")
    ranks[symbol] = (int(b), int(p))
for s in symbols:
    if s not in ranks:
        problems.append(f"{s} has no ranks")
N = len(symbols)
for i, name in ((0, "base"), (1, "pessimistic")):
    got = sorted(v[i] for v in ranks.values())
    if got != list(range(1, N + 1)) and not problems:
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
    check.append(f"{OUT} has {len(built) - 1} rows, {COMBINED} has {len(rows)}")
else:
    if built[0][:-2] != header:
        check.append("The header columns changed")
    for orig, new in zip(rows, built[1:]):
        if new[:-2] != orig:
            check.append(f"The row for {orig[si]} changed")
if check:
    os.remove(OUT)
    print(f"The check against {COMBINED} failed. {OUT} was deleted.")
    print("\n".join(check))
    sys.exit(1)
print("Companies:", len(rows))
print(f"Check against {COMBINED}: passed")
print("File:", OUT)
PY
```

### Step 6: Review

#### What it does
Reviews each company's reads and ranks against its figures, and corrects the ones that do not hold up.

#### How
Do these seven steps in order.

##### 6.1 Re-read the sub-sector, the scenarios and the shortlist columns
Read these three again, in this order.
1. `AI Sub-Sectors.md`, in full, with the **`Reader Script`**. Find the section for your sub-sector.
2. `AI Scenarios.md`, in full, with the **`Reader Script`**. Find the entry for your sub-sector under each scenario.
3. The **`Shortlist Columns`**, near the top of this prompt.

###### Reading the files
- After chunk 1 of each file, say how many chunks there are, and report your progress after every ten chunks.

##### 6.2 Read the ranked file
Read `data/screener/AI Subsectors/{SUBSECTOR}_ranked.md` in full, with the **`Reader Script`**. It has one row per company: the Shortlist columns, the base read, the pessimistic read, the base rank and the pessimistic rank.

###### Reading the ranked file
- After chunk 1, say how many chunks there are, and report your progress after every ten chunks.

##### 6.3 Review the reads
The reads and ranks in the file are a first attempt to test, not to defend. Do not anchor to them. You may disagree with any read or rank.

Go through the chunks one at a time, and every company in each chunk. Assess each company again as if you were doing it for the first time. For each company, check:
- Does each read follow from the company's figures? Check every comparison in the read against the figures.
- Does each read follow `AI Sub-Sectors.md` and the scenarios in `AI Scenarios.md`, including the sub-sector's upside and downsides in that scenario and how they affect this company?
- Does it weigh the company as the **Company Scenario Considerations** in `AI Scenarios.md` describe?

Write each read you would change, and the new read, in your reply.

##### 6.4 Review the ranks
After the last chunk, review the base ranking and then the pessimistic ranking, each across all the companies. For each ranking, check:
- Does each company's rank fit its read, with the reads as you changed them in 6.3?
- Does the order make sense when all the companies are compared together? Take the most care over the top of the ranking, because the best five in each scenario are the ones that carry forward.

Write each rank you would change in your reply.

##### 6.5 Make the corrections
The ranked file is built from `{SUBSECTOR}_combined.md` and `{SUBSECTOR}_ranks.md`, so make the corrections in those two files and rebuild it. Do not edit the ranked file.
1. Reads: for each read you changed in 6.3, edit it in `{SUBSECTOR}_combined.md` with the Edit tool. Do not use the `|` symbol within a read.
2. Ranks: write all the ranks again, with your changes from 6.4, to `{SUBSECTOR}_ranks.md` with the Write tool, in the format from 4.4. Each ranking still runs from 1 to the number of companies, with no ties and no gaps.
3. Run the Step 5 script again. It rebuilds `{SUBSECTOR}_ranked.md` with the new reads and ranks.

Change only the base and pessimistic reads and ranks. Do not change the figures, the other Shortlist columns, or which companies are on the list.

##### 6.6 Write the note
Write a short note to `data/screener/AI Subsectors/{SUBSECTOR}_note.md` with the Write tool.
- A few sentences on what drove the picks in base and in pessimistic, and why the other companies fell short. Give only the key figures.
- The file contains the note and nothing else.

##### 6.7 Check the file
Re-read `{SUBSECTOR}_ranked.md` and answer these in your reply, briefly. If any answer is no, fix it and answer that question again:
- Did you read `AI Sub-Sectors.md` and `AI Scenarios.md` in full with the **`Reader Script`**, and the **`Shortlist Columns`**?
- Did you read every chunk of `{SUBSECTOR}_ranked.md` through "end of file" with the **`Reader Script`**, one at a time? How many chunks was that?
- Did you review every company's reads and both rankings as if for the first time? How many reads and ranks did you change?
- Does each read follow from the company's figures and from `AI Sub-Sectors.md`, the scenarios in `AI Scenarios.md` and the **Company Scenario Considerations** in `AI Scenarios.md`?
- Does each rank fit its read? Where a rank is far from what its read suggests, can you say why? Where two companies with similar reads got different ranks in the same scenario, can you say why?
- If you made corrections, did you make them in `{SUBSECTOR}_combined.md` and `{SUBSECTOR}_ranks.md` and run the Step 5 script again?
- Did you check every ranking claim, comparison and superlative in the note against the final ranks and the figures?

#### Required output
`{SUBSECTOR}_ranked.md`, rebuilt with your corrections, and `data/screener/AI Subsectors/{SUBSECTOR}_note.md`. In your reply in the chat, list what you changed and why. Then answer the self-check questions. Do not put either in the file.

### Step 7: Build the Scenario Shortlist

#### What it does
Builds the Scenario Shortlist: the five best companies in each scenario, with the note at the top.

#### How
Run the script below as a single inline command, with the sub-sector as the argument: `python3 - {SUBSECTOR} <<'PY'`

The script builds the Scenario Shortlist from `{SUBSECTOR}_ranked.md` and `{SUBSECTOR}_note.md`. First it checks:
- `{SUBSECTOR}_note.md` exists and is not empty.
- `{SUBSECTOR}_ranked.md` has the columns it needs, every row is complete, and no symbol appears twice.
- The base ranks and the pessimistic ranks each run from 1 to the number of companies, with no ties and no gaps.

If a check fails, the script prints the problems and stops without building or deleting anything. Fix `{SUBSECTOR}_note.md`, or fix `{SUBSECTOR}_ranks.md` and run the Step 5 script again to rebuild `{SUBSECTOR}_ranked.md`. Then run this script again.

Then it builds the file:
- It keeps each company ranked 1 to 5 in base, in pessimistic, or in both.
- It adds a Picked for column: `base` if the company is in the top five for base only, `pessimistic` if for pessimistic only, and `both` if for both.
- It puts the note at the top as one paragraph, above the table.
- It sorts the rows by each company's better rank in the two scenarios.

After it writes the file, it reads it back and checks that it matches the rows it chose. If it does not, it deletes the new file and nothing else. If it does, it deletes the working files: `{SUBSECTOR}_reads.md`, `{SUBSECTOR}_combined.md`, `{SUBSECTOR}_ranks.md`, `{SUBSECTOR}_ranked.md` and `{SUBSECTOR}_note.md`.

#### Required output
The Scenario Shortlist file, `data/screener/AI Subsectors/{SUBSECTOR} Scenario Shortlist {MM-DD-YY}.md`, dated today, and what the script printed: the number of companies, how many are base only, pessimistic only and both, and the files it deleted.

#### Script
```bash
python3 - {SUBSECTOR} <<'PY'
import datetime, os, sys

SUBSECTOR = sys.argv[1]
DIR = "data/screener/AI Subsectors"
RANKED = f"{DIR}/{SUBSECTOR}_ranked.md"
NOTE = f"{DIR}/{SUBSECTOR}_note.md"
OUT = f"{DIR}/{SUBSECTOR} Scenario Shortlist {datetime.date.today().strftime('%m-%d-%y')}.md"
SCRATCH = [f"{DIR}/{SUBSECTOR}_{name}.md" for name in ("reads", "combined", "ranks", "ranked", "note")]
TOP = 5

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

need = ["Symbol", "Base read", "Pessimistic read", "Base rank", "Pessimistic rank"]
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
    if len(set(r[ix["Symbol"]] for r in rows)) != N:
        problems.append("A symbol appears more than once")
if problems:
    print(f"{RANKED} has problems. Nothing was built.")
    print("\n".join(problems))
    sys.exit(1)

order = ["Symbol", "Company", "Fit tier", "Potential growth", "Current growth", "Strength", "Price", "Why",
         "Base read", "Base rank", "Pessimistic read", "Pessimistic rank"]
cols = [header.index(h) for h in order if h in header]
cols += [i for i in range(len(header)) if i not in cols]

picked = []
for r in rows:
    b, p = int(r[ix["Base rank"]]), int(r[ix["Pessimistic rank"]])
    if b <= TOP or p <= TOP:
        tag = "both" if b <= TOP and p <= TOP else ("base" if b <= TOP else "pessimistic")
        picked.append((min(b, p), b, [r[i] for i in cols] + [tag]))
picked.sort(key=lambda x: (x[0], x[1]))
final_header = [header[i] for i in cols] + ["Picked for"]

with open(OUT, "w", encoding="utf-8") as out:
    out.write(note + "\n\n")
    out.write("| " + " | ".join(final_header) + " |\n")
    out.write("|" + "---|" * len(final_header) + "\n")
    for _, _, r in picked:
        out.write("| " + " | ".join(r) + " |\n")

built = []
with open(OUT, encoding="utf-8") as fh:
    if fh.readline().strip() != note:
        built.append(["note differs"])
    for line in fh:
        if not line.lstrip().startswith("|"):
            continue
        c = cells(line)
        if c and not is_rule(c):
            built.append(c)
if built[0] != final_header or [b for b in built[1:]] != [r for _, _, r in picked]:
    os.remove(OUT)
    sys.exit(f"The file written does not match the rows chosen from {RANKED}. {OUT} was deleted. Nothing else was deleted.")

for path in SCRATCH:
    if os.path.exists(path):
        os.remove(path)
tags = [r[-1] for _, _, r in picked]
print("Companies:", len(picked))
print("Base:", tags.count("base"), "| Pessimistic:", tags.count("pessimistic"), "| Both:", tags.count("both"))
print("Deleted:", ", ".join(os.path.basename(p) for p in SCRATCH))
print("File:", OUT)
PY
```
