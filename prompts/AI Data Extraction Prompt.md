# AI Extraction Prompt

## Role
You extract verbatim excerpts about AI from a company's documents for a stock analysis pipeline. You run scripts that find the passages, then review them and remove only what does not belong. You do not analyze the data, and you never alter, shorten, paraphrase, or add to the text you keep.

The final output is `/workspaces/green_lumber/data/companies/{TICKER}/{TICKER}_ai_extracts.md`.

## Rules
- Do not read the source documents. The scripts search them for you.
- Run each script exactly as written.
  - Run it as a single inline command, every time.
  - Paste the script from this prompt into the command itself.
  - Do not save it to a file (including `/tmp`), and do not run a saved copy from an earlier run.
  - Do not split a script up or edit it.
  - The only things you supply are the arguments shown in each step.
- You never write, edit, shorten, or paraphrase any excerpt text. Your only input to the process is the list of line numbers to remove.
  - Do not alter any text. Passages are removed whole, by line number. Nothing is edited, shortened, or added.
  - Do not paraphrase, compress, or restate — not even one sentence.
  - Do not add commentary or transitions between passages.
  - Do not write process notes, coverage summaries, self-assessments, or any commentary about the extraction itself into the extracts file — the file contains excerpts and nothing else.

## Flow

### Step 1 — Ticker
Get the `{TICKER}`. If none is given, ask for one before starting.

### Step 2 — Stage every search

#### What it does
Searches every `.md` and `.txt` file in `/workspaces/green_lumber/data/companies/{TICKER}/` except the data summary, the numbers file, the Excerpts file, and earlier extracts, and stages the matches in a raw file, `{TICKER}_ai_extracts_raw.md`, in the same folder.

#### How
- Run the script below as a single inline command, with the ticker as the argument: `python3 - {TICKER} <<'PY'`
- Run every search — skip none.
- The script flattens each file into one line (so phrases wrapped across lines still match) and collects every match from all 23 searches, each with the text around it. Within a file, it merges any matches whose surrounding text overlaps, whichever search found them, so no text is written twice. It then cuts each merged stretch into passages of at most about 2,000 characters and writes them to the raw file, file by file, in the order they appear in the document.
- The script only stages raw matches. It must not filter, judge relevance, or truncate anything.
- Each excerpt begins with a tag in square brackets: the source file, the searches that found it, and the terms that matched, e.g. `[CLS_earnings_2026Q1.md | 2. AI Exposure, Revenue, and Customers; 3d. Physical Infrastructure: Networking | hyperscaler; 800g]`. The script adds it. Do not change it.

#### Required output
The raw file, and the raw file size printed by the script.

#### Script
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
("11. Growth Drivers and Outlook", r"(revenue|sales)s?\b.{0,60}\b(increased|decreased|grew|declined|rose|fell)\b|\b(increase|decrease|growth|decline) in (revenue|sales)|(primarily|mainly|largely) (due to|driven by|attributable to|as a result of)|driven (primarily |mainly )?by|partially offset|organic (growth|revenue)|new (programs?|customers?|contracts?|wins?)|ramp(ing)? (up|of)|addressable market|market opportunity|growth opportunit|\bguidance\b|(our|the|business|financial|revenue|market) outlook|we (expect|anticipate|project) (that )?(revenue|sales|growth|demand)|reaffirm|(next|coming|following) (quarter|fiscal year)", 400),
("12. Headwinds and Risks to Growth", r"headwinds?|slowdown|softness|weakness|demand (pressure|softness|decline|reduction)|(pressure|downturn|decline|reduction|slowdown|delays?) (in|on|to) (demand|orders|spending|programs?)|macroeconomic|tariffs?|supply chain (disruption|constraint)|customer (delays?|cancell?ations?|push[- ]?outs?)|inventory (digestion|correction)|loss of (a |one |our )?(major |significant )?customer|reduc(e|tion)s? in (orders|demand|spending)", 400),
]

CAP = 2000

texts = {}
for f in FILES:
    with open(os.path.join(SRC, f), encoding="utf-8", errors="ignore") as fh:
        texts[f] = re.sub(r"\s+", " ", fh.read())

def clean(term):
    term = re.sub(r"\s+", " ", term.lower()).strip()
    for ch in "[]|;":
        term = term.replace(ch, "")
    return term[:40]

rxs = [re.compile(pat, re.I) for _, pat, _ in SECTIONS]

with open(RAW, "w", encoding="utf-8") as out:
    for f in FILES:
        t = texts[f]
        hits = []
        for i, (title, pat, w) in enumerate(SECTIONS):
            for m in rxs[i].finditer(t):
                hits.append((max(0, m.start() - w), min(len(t), m.end() + w), i, clean(m.group(0))))
        hits.sort()
        regions = []
        for h in hits:
            if regions and h[0] <= regions[-1][1]:
                regions[-1][1] = max(regions[-1][1], h[1])
                regions[-1][2].append(h)
            else:
                regions.append([h[0], h[1], [h]])
        for S, E, hs in regions:
            a = S
            while a < E:
                b = min(E, a + CAP)
                if b < E:
                    dot = t.rfind(". ", a, b)
                    if dot > a + CAP // 2:
                        b = dot + 1
                    else:
                        sp = t.rfind(" ", a, b)
                        if sp > a:
                            b = sp
                piece = t[a:b].strip()
                idxs = sorted({h[2] for h in hs if h[0] < b and h[1] > a})
                terms = []
                for h in hs:
                    if h[0] < b and h[1] > a and h[3] and h[3] not in terms:
                        terms.append(h[3])
                out.write(f"[{f} | {'; '.join(SECTIONS[i][0] for i in idxs)} | {'; '.join(terms[:8])}] {piece}\n\n")
                a = b
print("Raw file size (bytes):", os.path.getsize(RAW))
PY
```

### Step 3 — Read and review

#### What it does
Chooses which passages in the raw file to remove. A passage belongs if it helps explain how the company is involved in AI, what is driving its growth, what is holding it back, or how it is investing and paying for it. It does not need to contain the word "AI". It uses the AI framework and the fourteen questions as context, reads the raw file through the reader script, and produces a list of line numbers to remove.

#### How

##### Context
- Read `AI Framework.md` in full, for context on the AI landscape. If a read stops short, continue until the entire file has been read. Truncation is not allowed.
- Read the fourteen questions below, for context on what the analysis of this company needs to answer. They are not output sections:
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

##### Deciding what to remove
- Remove a passage when it does not help answer any of the fourteen questions and has no bearing on AI as the framework describes it. Judge it by what it is about, not by whether it says "AI". A sentence about a "Cloud and Data Center segment" belongs even though it never says AI.
  - If it is genuinely borderline, keep it.
- Remove a passage as a duplicate only if its entire text already appears inside another passage you are keeping.

##### Reading the raw file
- The only files you read in this step are `AI Framework.md` and the raw file `/workspaces/green_lumber/data/companies/{TICKER}/{TICKER}_ai_extracts_raw.md`.
- Read the raw file in full, using the reader script below, and only through it. Do not use the Read tool on it, and do not run `head`, `cat`, `tail`, `grep`, or `ls` on it. The reader prints one numbered chunk of a file at a time, and every line carries its real line number.
- Run it as `python3 - "<path>" <chunk number> <<'PY'`, starting at chunk 1 and continuing in sequence. Each chunk's header says which chunk it is and how many there are in total. Never assume a chunk's contents or skip ahead; read every chunk through the last one, the one marked "end of file." Truncation is not allowed.
- Note the line numbers to remove as you finish each chunk, and combine them into one list at the end. Do not edit, shorten, or add to any line.

#### Required output
One combined list of the line numbers to remove (or none).

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

### Step 4 — Apply the removals and report

#### What it does
Writes the final extracts file from the raw file, minus the removed lines.

#### How
- Run the script below as a single inline command, with the ticker followed by every line number to remove as arguments: `python3 - {TICKER} 12 45 78 <<'PY'`
- Use the numbers exactly as the reader showed them. If there is nothing to remove, give the ticker alone.
- The script prints, for each of the 23 searches, how many passages it found, how many were kept, and how many were removed. A passage found by several searches is counted under each of them, so those counts add up to more than the number of passages. The last count line, "All passages", counts each passage once.
- It overwrites the final extracts file if one already exists. That is expected. Do not look at the old file first.

#### Required output
- The final extracts file.
- A report of each search's found, kept and removed counts, the "All passages" line, and the final file size, exactly as printed by the script. Do not summarize the contents.

#### Apply script
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
    "11. Growth Drivers and Outlook",
    "12. Headwinds and Risks to Growth",
]

stats = {t: [0, 0] for t in TITLES}
total = [0, 0]
lines = open(RAW, encoding="utf-8").read().split("\n")
out = []
for i, line in enumerate(lines, 1):
    if not line.strip():
        continue
    titles = line[1:line.index("] ")].split(" | ")[1].split("; ") if line.startswith("[") and "] " in line else []
    removed = i in REMOVE
    for t in titles:
        if t not in stats:
            stats[t] = [0, 0]
        stats[t][1 if removed else 0] += 1
    total[1 if removed else 0] += 1
    if not removed:
        out.append(line + "\n")
open(FINAL, "w", encoding="utf-8").write("\n".join(out))
for s, (k, r) in stats.items():
    print(f"{s}: found {k + r}, kept {k}, removed {r}")
print(f"All passages: found {sum(total)}, kept {total[0]}, removed {total[1]}")
print("Final file size (bytes):", os.path.getsize(FINAL))
PY
```

### Step 5 — Clean up
Delete the raw file `/workspaces/green_lumber/data/companies/{TICKER}/{TICKER}_ai_extracts_raw.md`. It is a scratch file, not output. Do not delete the final extracts file.
