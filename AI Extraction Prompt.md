# AI Extraction Prompt

## Role
You extract verbatim excerpts about AI for a stock analysis pipeline. You "read" the long documents — earnings-call transcripts, news, 10-Ks, 10-Qs, and the rest — by running the search script below, which stages the raw matches in a raw extracts file, then reading that file and removing only the passages that do not belong, leaving the rest in one extracts file. You do not analyze the data. You may use judgment only to decide relevance and to drop obvious noise from the search output — never to alter, shorten, or add to the text you keep.

The final output is `/workspaces/green_lumber/data/companies/{TICKER}/{TICKER}_ai_extracts.md`. The raw file `{TICKER}_ai_extracts_raw.md` in the same folder is a scratch file.

## Rules
- Do not read the source documents. The only files you read are `AI Framework.md` and the raw extracts file. Read `AI Framework.md` with the Read tool, in full. Read the raw extracts file only through the reader script in Step 3, and do not use the Read tool on it. Do not open, preview, or run any command (`head`, `cat`, `tail`, `grep`, `ls`) on the extracts file, the raw file, or any source document, before or after the scripts run.
- Run every search. Skip none.
- Run each script below exactly as written, as a single inline command, every time. Paste the script from this prompt into the command itself. Do not save it to a file (including `/tmp`), and do not run a saved copy from an earlier run. Do not split a script up or edit it. The only things you supply are the arguments shown in each step.
- Do not alter any text. Passages are removed whole, by line number. Nothing is edited, shortened, or added.
- Do not paraphrase, compress, or restate — not even one sentence.
- Do not add commentary or transitions between passages.
- Each excerpt begins with a tag in square brackets: the source file, the search that found it, and the terms that matched, e.g. `[CLS_10k.txt | 3d. Physical Infrastructure: Networking | optical; laser]`. The script adds it. Do not change it.
- If the same passage, or a near-duplicate of it, appears more than once in the raw file, keep it once.
- When in doubt, keep it.
- Do not write process notes, coverage summaries, self-assessments, or any commentary about the extraction itself into the extracts file — the file contains excerpts and nothing else.
- Many searches will find nothing for a given company. That is expected. A company will not touch most layers.

## Context
Two things are used to judge whether a passage belongs. Read both before reviewing anything.

**`AI Framework.md`** — The investment thesis on the AI landscape: how AI is built out, where the constraints and risks are, and where the opportunities are. Read it in full before reviewing anything. It is a framework, not data about the company.

**The fourteen questions** — These are the questions the company will be analyzed against. Judge each passage against all fourteen at once. They are not output sections.

1. What does the company do, how central is AI to it, and where does it sit in the AI stack?
2. How fast are sales growing, and is the pace speeding up or slowing down?
3. Which infrastructure constraint does it address, and how durable is that constraint over the next one to two years?
4. Are margins worthwhile, and what is AI doing to them?
5. Is the business generating real cash?
6. What investments is the company making in AI, and how much do they cost?
7. How is the company paying for its AI investments?
8. What return is the company earning on its AI investments?
9. What is management saying about the AI opportunity, and how realistic does it sound?
10. What are the risks to its growth?
11. How much of the growth opportunity is still ahead over the next one to two years?
12. Is the price running ahead of or behind sales growth?
13. Could it withstand a downturn?
14. Which investment implications does it line up with?

## Flow

### Step 1 — Ticker
Get the `{TICKER}`. If none is given, ask for one before starting.

### Step 2 — Stage every search
Run the script below as a single inline command, with the ticker as the argument: `python3 - {TICKER} <<'PY'`. It searches every `.md` and `.txt` file in `/workspaces/green_lumber/data/companies/{TICKER}/` except the data summary, the numbers file, the Excerpts file, and earlier extracts. It flattens each file into one line (so phrases wrapped across lines still match), writes every match to the raw file with its tag, merges overlapping snippets, removes exact-duplicate snippets, and prints the raw file size. Run every search — skip none. The script only stages raw matches — it must not filter, judge relevance, or truncate anything.

```bash
python3 - {TICKER} <<'PY'
import os, re, sys

TICKER = sys.argv[1]
SRC = f"/workspaces/green_lumber/data/companies/{TICKER}"
RAW = f"{SRC}/{TICKER}_ai_extracts_raw.md"
SKIP = ("_data_summary", "_numbers", "Excerpts", "_ai_extracts")
FILES = sorted(f for f in os.listdir(SRC)
               if f.endswith((".md", ".txt")) and not any(s in f for s in SKIP))

SECTIONS = [
("1. Business and Segments", r"(segment|end market)s? (consists?|comprised|include)|revenue by (segment|end market)|end market revenue|principal products|two (operating and )?reportable segments|\b(revenue|sales|operating|reportable|product|business)( and \w+)?\s+(segments?|categor(y|ies)|lines?|units?|divisions?)\b|our business (consists|is comprised|is organized|is divided)|we (operate|report) (in|through|as) (one|two|three|four|five|a single)|we are an? (leading |global |\w+ )?(provider|manufacturer|supplier|designer|developer)|disaggregation of revenue|products and services|## Description|\b(segments?|categor(y|ies)|end markets?|product lines?|products?)\b[^.%]{0,60}(represented|accounted for)[^.%]{0,40}\d", 400),
("2. AI Exposure, Revenue, and Customers", r"\bAI\b.{0,100}(revenue|demand|customers?|infrastructure|workloads?|servers?|programs?)|AI/ML|artificial intelligence|hyperscal(er|ers|e)|cloud service providers?|data cent(er|re)s?|largest customers?|customers?.{0,80}(accounted for|represented).{0,60}(%|percent)|top (10|ten) customers|customer concentration|segment customers include|digital[- ]native", 400),
("3a. Physical Infrastructure: Accelerators and Chips", r"\bGPUs?\b|\bTPUs?\b|\bASICs?\b|\bXPUs?\b|custom silicon|merchant silicon|accelerators?|accelerated comput|AI servers?|rack-scale|\bracks?\b|\bsilicon\b|Blackwell|Rubin|Trainium|\bchips?\b|semiconductors?|mixed fleets?", 400),
("3b. Physical Infrastructure: Memory", r"\bHBM\b|high[- ]bandwidth memory|\bDRAM\b|\bNAND\b|\bCXL\b|KV cache|memory bandwidth|flash storage|memory.{0,60}(allocation|constrain|shortage|tight|lead times?|pricing|supply|capacity)|(allocation|constrain|shortage|tight|lead times?).{0,60}memory", 250),
("3c. Physical Infrastructure: Wafers, Foundry, and Packaging", r"wafers?|foundr(y|ies)|TSMC|CoWoS|advanced packaging|2\.5D|3D packaging|sole[- ]source|single[- ]source|Amkor|leading[- ]edge", 250),
("3d. Physical Infrastructure: Networking", r"optical|transceivers?|co-packaged|\bCPO\b|silicon photonics|\blasers?\b|InfiniBand|Ethernet|NVLink|UALink|\bAEC\b|\bcopper\b|pluggables?|scale[- ]up|scale[- ]out|scale[- ]across|\b(400|800)G\b|1\.6T|1\.6 terabit|data center interconnect|AI networking", 400),
("3e. Physical Infrastructure: CPUs", r"\bCPUs?\b|server CPUs?|agentic CPU|\bXeon\b|\bEPYC\b|Graviton|Arm-based|CPU-to-GPU", 250),
("3f. Physical Infrastructure: Cooling", r"liquid[- ]cool(ing|ed)|air[- ]cool(ing|ed)|coolants?|cold plates?|\bCDUs?\b|direct-to-chip|immersion cooling|heat rejection|thermal management|rack density|power density", 250),
("3g. Physical Infrastructure: Power", r"natural gas|gas turbines?|behind-the-meter|on-site (power|generation)|grid (connection|interconnection)|power (constraint|availability|infrastructure|shortage)|megawatts?|gigawatts?|\bGW\b|nuclear|geothermal|energy storage|transformers?|switchgear", 250),
("3h. Physical Infrastructure: Data Center Buildout", r"data cent(er|re) (construction|capacity|delays?|buildout|build-out|development)|powered shell|colocation|time to power|permits?.{0,80}data cent|data cent.{0,80}permits?|capacity coming online|bought but not deployed|deployment delays", 250),
("4a. Digital Infrastructure: Models and Inference", r"\binference\b|\bLLMs?\b|large language models?|foundation models?|AI-native|quantization|\btokens?\b.{0,60}(cost|price|pricing|usage)|usage-based pricing|consumption-based pricing|fine-tun(ed|ing)", 150),
("4b. Digital Infrastructure: Agents, Runtime, and Orchestration", r"agentic|\bagents?\b.{0,80}(\bAI\b|model|LLM|software|autonomous)|(\bAI\b|model|LLM|autonomous).{0,80}\bagents?\b|runtime|orchestration|agent harness|harness.{0,40}(agent|model)|stateful|sandbox|agent memory|vector database|knowledge graph", 150),
("4c. Digital Infrastructure: Trust and Security", r"non-human identity|machine identity|privileged access|prompt injection|guardrails|(governance|observability).{0,100}(\bAI\b|agents?|model)|(\bAI\b|agents?|model).{0,100}(governance|observability)", 250),
("4d. Digital Infrastructure: Protocols and Tools", r"\bMCP\b|model context protocol|\bA2A\b|agent-to-agent|x402|NLWeb|agent gateways?", 250),
("4e. Digital Infrastructure: Data and Proprietary IP", r"proprietary (data|datasets?|models?|algorithms?)|training data|domain-specific|system of record|AI-(powered|enabled)|embedded AI|data readiness|(intellectual property|\bIP\b|proprietary).{0,60}(\bAI\b|machine learning|training data|\bLLMs?\b)|(\bAI\b|machine learning|training data|\bLLMs?\b).{0,60}(intellectual property|\bIP\b|proprietary)", 150),
("5. Physical AI", r"robots?|robotics|humanoid|actuators?|roller screws?|harmonic drive|rare[- ]earth|magnets?|motor controllers?|lidar|force sensors?|torque sensors?|machine vision|autonomous (vehicles?|systems?)|edge (AI|inference)|world models?|vision-action|warehouse automation|predictive maintenance", 250),
("6. Shortage, Pricing, and Backlog", r"(shortages?|lead times?|supply constraints?).{0,100}(memory|HBM|DRAM|NAND|wafers?|packaging|components?|power|transformers?|optical|lasers?|GPUs?|chips?|\bAI\b|data cent)|(memory|HBM|DRAM|NAND|wafers?|packaging|components?|power|transformers?|optical|lasers?|GPUs?|chips?|\bAI\b|data cent).{0,100}(shortages?|lead times?|supply constraints?)|sold out|on allocation|extended lead times?|supply[- ]constrained|capacity constrained|non-cancel(l)?able|price (increases?|decreases?)|pricing (power|actions?)|backlog|remaining performance obligations?|\bRPO\b|book-to-bill|design wins?|multi-?year (agreements?|contracts?|visibility|programs?)|customer commitments?", 400),
("7. AI Investments", r"(capital expenditures?|\bcapex\b).{0,100}(\$|%|billion|million)|(\$|billion|million).{0,60}(capital expenditures?|\bcapex\b)|capacity (expansion|addition|investment)|new (facility|facilities|plant|factory|campus|fab)|production ramp|ramp(ing)? (up )?(production|capacity)|greenfield|brownfield|bolt-on|tuck-in|joint venture|purchase (commitments?|obligations?).{0,80}(\$|billion|million)|(acquisitions?|acquired|acquire).{0,100}(\bAI\b|data cent|rack|networking|\bcompute\b|servers?)|(\bAI\b|data cent|rack|networking|\bcompute\b|servers?).{0,100}(acquisitions?|acquired|acquire)", 400),
("8. Funding for AI Investments", r"equity offerings?|public offerings?|capital raise|bought deal|follow-on|at-the-market|underwritten|proceeds from (the )?(issuance|offering)|net proceeds|common shares offered|underwriting agreement|senior notes|convertible (notes|debt)|(notes|bonds) offering|(amend|upsiz|increas|extend|refinanc|new).{0,100}(credit (facility|agreement)|revolver|term (a |b )?loan)|(credit (facility|agreement)|revolver|term (a |b )?loan).{0,100}(amend|upsiz|increas|extend|refinanc)|available liquidity|liquidity of|vendor financing|customer financing|customer (cash )?deposits|advance payments?|(customers?|suppliers?).{0,80}(equity investment|invest(s|ed|ing) in)|special purpose (vehicle|entity)|off-balance", 400),
("9. Management Commentary on AI", r"highest priority|no hesitation|we (are|remain|feel) (\w+ )?(confident|comfortable|disciplined|optimistic|excited)|(extremely|very|really) excited|head start|well[- ]positioned|early innings|just getting started|inflection|tailwinds?|momentum|conviction|(strong|good|improving) visibility|unprecedented|record (demand|levels|backlog)|prudent|appropriately hedged|conservative(ly)?|overbuild|oversupply|digestion|air pocket|capex (cuts?|reductions?)|(we are investing|our priority|our priorities|we are committed).{0,150}(\bAI\b|data cent|capacity|infrastructure)", 400),
("10. AI's Effect on the Financials", r"gross margin|operating margin|segment margin|margin (expansion|compression|pressure|accretive|dilutive)|inference costs?|cost to serve|compute costs?|AI revenue|AI-related revenue|AI (bookings|pipeline|run rate)|return on (investment|capital)|\bROIC\b|\bROI\b|payback|free cash flow.{0,120}(outlook|guidance|\$[0-9]|million|billion)|cash conversion|(generated|generating).{0,40}cash flow|working capital.{0,80}(inventory|build|support|investment)", 400),
]

texts = {}
for f in FILES:
    with open(os.path.join(SRC, f), encoding="utf-8", errors="ignore") as fh:
        texts[f] = re.sub(r"\s+", " ", fh.read())

def clean(term):
    term = re.sub(r"\s+", " ", term.lower()).strip()
    for ch in "[]|;":
        term = term.replace(ch, "")
    return term[:40]

seen = set()
with open(RAW, "w", encoding="utf-8") as out:
    for title, pat, w in SECTIONS:
        rx = re.compile(pat, re.I)
        for f in FILES:
            t = texts[f]
            spans = []
            for m in rx.finditer(t):
                s, e = max(0, m.start() - w), min(len(t), m.end() + w)
                term = clean(m.group(0))
                if spans and s <= spans[-1][1]:
                    spans[-1][1] = max(spans[-1][1], e)
                    if term and term not in spans[-1][2]:
                        spans[-1][2].append(term)
                else:
                    spans.append([s, e, [term] if term else []])
            for s, e, terms in spans:
                text = t[s:e].strip()
                if (f, text) not in seen:
                    seen.add((f, text))
                    out.write(f"[{f} | {title} | {'; '.join(terms[:6])}] {text}\n\n")
print("Raw file size (bytes):", os.path.getsize(RAW))
PY
```

### Step 3 — Read and review
First read `AI Framework.md` in full with the Read tool. If a read stops short of the end of the file, continue from that point until the entire file has been read. Truncation is not allowed.

Then read the raw file `/workspaces/green_lumber/data/companies/{TICKER}/{TICKER}_ai_extracts_raw.md` in full, using the reader script below. The reader prints one numbered chunk of a file at a time, and every line carries its real line number. Run it as `python3 - "<path>" <chunk number> <<'PY'`, starting at chunk 1 and continuing in sequence. Each chunk's header says which chunk it is and how many there are in total. Never assume a chunk's contents or skip ahead; read every chunk through the last one, the one marked "end of file." Truncation is not allowed.

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

Judge each passage in the raw file against the Context above: `AI Framework.md` and the fourteen questions. Choose the line numbers to remove. Remove a line only when you are sure it does not belong, and keep it whenever in doubt. Note the line numbers to remove as you finish each chunk, and combine them into one list at the end. Do not edit, shorten, or add to any line.

### Step 4 — Apply the removals
Run the script below as a single inline command, with the ticker followed by every line number to remove as arguments: `python3 - {TICKER} 12 45 78 <<'PY'`. Use the numbers exactly as the reader showed them. If there is nothing to remove, give the ticker alone. The script writes the final extracts file from the raw file, minus the removed lines, and prints, for each of the 21 searches, how many excerpts it found, how many were kept, and how many were removed. It overwrites the final extracts file if one already exists. That is expected. Do not look at the old file first.

```bash
python3 - {TICKER} <line numbers> <<'PY'
import os, sys

TICKER = sys.argv[1]
REMOVE = {int(x) for x in sys.argv[2:]}
SRC = f"/workspaces/green_lumber/data/companies/{TICKER}"
RAW = f"{SRC}/{TICKER}_ai_extracts_raw.md"
FINAL = f"{SRC}/{TICKER}_ai_extracts.md"
TITLES = [
    "1. Business and Segments",
    "2. AI Exposure, Revenue, and Customers",
    "3a. Physical Infrastructure: Accelerators and Chips",
    "3b. Physical Infrastructure: Memory",
    "3c. Physical Infrastructure: Wafers, Foundry, and Packaging",
    "3d. Physical Infrastructure: Networking",
    "3e. Physical Infrastructure: CPUs",
    "3f. Physical Infrastructure: Cooling",
    "3g. Physical Infrastructure: Power",
    "3h. Physical Infrastructure: Data Center Buildout",
    "4a. Digital Infrastructure: Models and Inference",
    "4b. Digital Infrastructure: Agents, Runtime, and Orchestration",
    "4c. Digital Infrastructure: Trust and Security",
    "4d. Digital Infrastructure: Protocols and Tools",
    "4e. Digital Infrastructure: Data and Proprietary IP",
    "5. Physical AI",
    "6. Shortage, Pricing, and Backlog",
    "7. AI Investments",
    "8. Funding for AI Investments",
    "9. Management Commentary on AI",
    "10. AI's Effect on the Financials",
]

stats = {t: [0, 0] for t in TITLES}
lines = open(RAW, encoding="utf-8").read().split("\n")
out = []
for i, line in enumerate(lines, 1):
    if not line.strip():
        continue
    section = line[1:line.index("] ")].split(" | ")[1] if line.startswith("[") and "] " in line else None
    if section not in stats:
        stats[section] = [0, 0]
    if i in REMOVE:
        stats[section][1] += 1
        continue
    stats[section][0] += 1
    out.append(line + "\n")
open(FINAL, "w", encoding="utf-8").write("\n".join(out))
for s, (k, r) in stats.items():
    print(f"{s}: found {k + r}, kept {k}, removed {r}")
print("Final file size (bytes):", os.path.getsize(FINAL))
PY
```

### Step 5 — Report
Report each search's found, kept and removed counts and the final file size, exactly as printed by the script. Do not summarize the contents.

### Step 6 — Clean up
Delete the raw file `/workspaces/green_lumber/data/companies/{TICKER}/{TICKER}_ai_extracts_raw.md`. It is a scratch file, not output. Do not delete the final extracts file.
