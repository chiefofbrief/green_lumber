# AI Sub-Sector Shortlist Prompt

## Role
You are an analyst in a stock analysis pipeline. For each AI sub-sector you are given, you pick the companies in the screener that belong to it, assess each one's growth, strength and price, and produce a ranked shortlist of them for the next stage of the pipeline.

You follow the guidance in the files you are given, and you follow this prompt exactly. You pay close attention to detail, because the guidance was written carefully and small differences in it change the answer.

## Rules

### Reading files
- Use only the files this prompt names. Do not look anything up. What you know about a company can supplement the files, but it may be out of date, so rely on the files first.
- Do not read or search the screener CSV, `data/screener/Large_Actives_with_Metrics.csv`, yourself. The scripts stage what you need from it.
- Whenever a step tells you to read `AI Sub-Sectors.md`, read all of it with the **`Reader Script`** and pay close attention to everything in it.

### Writing files
- Never alter the input files: the screener CSV, `data/screener/Large_Actives_with_Metrics.csv`, and `AI Sub-Sectors.md`. The only files written are:
  - the staged file, `data/screener/{SUBSECTOR}_staged.md`
  - the picks file, `data/screener/{SUBSECTOR}_picks.md`
  - the Candidates file, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`
  - the Shortlist file, `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md`
- Do not write process notes, coverage summaries, self-assessments, or any commentary about your process into the output files. The files contain results and nothing else.

### Running scripts
- Run every command from the repository root.
- Run each script exactly as written.
  - Run it as a single inline command, every time.
  - Paste the script from this prompt into the command itself.
  - Do not save it to a file (including `/tmp`), and do not run a saved copy from an earlier run.
  - Do not split a script up or edit it, including removing the other sub-sectors from the table.
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

## Flow

### Step 1: Get the sub-sector

#### What it does
Gets the sub-sector to run.

#### How
- Get the sub-sector(s) to run, such as `networking`. If none is given, ask for one before starting. This is `{SUBSECTOR}` in the rest of this prompt.
- Each sub-sector has a section in `AI Sub-Sectors.md`: `networking` is Networking, `power` is Power, `electrical` is Electrical equipment, `wafers` is Wafers and advanced packaging, `cooling` is Cooling, `data` is Data, `trust` is Trust, `runtime` is Runtime, `processors` is Processors, `racks` is Racks and servers, `memory` is Memory, and `tools` is Tools.

### Step 2: Stage the candidates

#### What it does
Gathers the companies in the screener that could belong to `{SUBSECTOR}`, so Step 3 can decide which ones do.

#### How
Run the script below as a single inline command, with the sub-sector as the argument: `python3 - {SUBSECTOR} <<'PY'`

The script writes the staged file, `data/screener/{SUBSECTOR}_staged.md`. It stages every company in the sub-sector's industries, and also any company in another industry whose description matches one of the searches. It only stages: it does not filter, judge relevance or shorten any description.

Entries are grouped by industry, so similar companies sit together. Each entry is the company's description, with nothing else from the screener, and begins with a tag in square brackets: symbol, company name, industry, and the searches and terms that matched, e.g. `[SYMBOL | Company Name | Industry | Data center and cloud customers: hyperscaler; data center]`. A company with no match is tagged `no match`. The script adds the tag. Do not change it.

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
    "power": {
        "industries": [
            "Oil & Gas Midstream", "Oil & Gas Exploration & Production", "Oil & Gas Integrated",
            "Oil & Gas Equipment & Services", "Oil & Gas Drilling", "Renewable Utilities", "Solar",
            "Independent Power Producers", "Uranium", "Regulated Electric", "Diversified Utilities",
        ],
        # A match counts on its own.
        "searches": [
            ("Natural gas supply chain", r"\bmidstream\b|gas gathering|gas processing|compressor stations?|natural gas liquids|\bNGLs?\b|\bLNG\b|liquefaction|natural gas pipelines?|gas pipelines?|transmission pipelines?|fractionation|gathering,? (and |&)?processing|processing,? (and |&)?gathering|natural gas"),
            ("Nuclear", r"\bnuclear\b|small modular|\buranium\b"),
            ("Geothermal", r"geothermal"),
            ("Solar", r"\bsolar (power|energy|farms?|modules?|panels?|projects?)|photovoltaic"),
            ("Storage", r"energy storage|battery storage|utility-scale"),
            ("Batteries", r"lithium[- ]ion|\bLFP\b|solid[- ]state batter(y|ies)|battery cells?|\bbatter(y|ies)\b.{0,80}(grid|stationary|utility|data cent|energy storage|power plant)|(grid|stationary|utility|data cent|energy storage|power plant).{0,80}\bbatter(y|ies)\b"),
            ("Generation", r"megawatts?|gigawatts?|\bMW\b|\bGW\b|independent power producers?|recovered energy|on-?site (power|generation)|behind[- ]the[- ]meter"),
            ("Grid", r"power grid|interconnection (queue|request)s?|transmission lines?|electric transmission|grid (connection|interconnection)|power (constraints?|availability|infrastructure|shortages?)"),
        ],
        # A match counts only if a context word also appears in the same description.
        "paired": [],
    },
    "electrical": {
        "industries": [
            "Electrical Equipment & Parts", "Industrial - Machinery", "Engineering & Construction",
            "Industrial - Distribution", "Industrial - Specialties",
        ],
        # A match counts on its own.
        "searches": [
            ("Transformers and switchgear", r"power transformers?|distribution transformers?|\bswitchgear\b|switchboards?|circuit breakers?|modular substations?|substation packages?|control room substations?|\bHVDC\b"),
            ("Power distribution", r"power distribution|power quality|\bbusways?\b|\bbusbars?\b|\bPDUs?\b|electrical (apparatus|equipment|enclosures?)|wiring devices|prefabricated (electrical|power)"),
            ("Backup and conversion", r"uninterruptible power|backup power|standby (power|generators?)|backup generators?|power conversion|solid[- ]state transformers?|\b800 ?V\b|DC-DC"),
            ("Data center electrical", r"data ?cent(er|re)s?[^.]{0,60}(electrical|power distribution|power systems?|power infrastructure)|(electrical|power distribution|power systems?)[^.]{0,60}data ?cent(er|re)s?"),
        ],
        # A match counts only if a context word also appears in the same description.
        "paired": [],
    },
    "wafers": {
        "industries": [
            "Semiconductors", "Hardware, Equipment & Parts",
        ],
        # A match counts on its own.
        "searches": [
            ("Wafers and fabs", r"\bwafers?\b|\bTSMC\b|semiconductor (foundr(y|ies)|fabs?|fabrication)|foundry services|wafer foundr(y|ies)|sole[- ]source|single[- ]source"),
            ("Advanced packaging", r"advanced packaging|chip[- ]on[- ]wafer|CoWoS|2\.5D|3D (chip )?packag\w*|3D integration|heterogeneous integration|semiconductor packaging|packaging and test\w*|assembly and test|OSAT|outsourced semiconductor|flip[- ]chip|ball grid array|\bBGA\b|chip[- ]scale|stacked die|back-?grinding|wafer[- ](bumping|probing|level)"),
            ("Equipment", r"semiconductor (capital )?equipment|extreme ultraviolet|\bEUV\b|lithograph(y|ic)|photomasks?|reticles?|photoresists?|wafer[- ](inspection|cleaning|processing|metrology|handling)|atomic layer deposition|chemical vapor deposition|\bCVD\b|\bALD\b|deposition (equipment|systems?|technolog\w*)|etch(ing)? (systems?|equipment)"),
            ("Materials", r"microcontamination|semiconductor[^.]{0,80}specialty (gases|chemicals)|specialty (gases|chemicals)[^.]{0,80}semiconductor"),
        ],
        # A match counts only if a context word also appears in the same description.
        "paired": [],
    },
    "cooling": {
        "industries": [
            "Industrial - Machinery", "Electrical Equipment & Parts", "Construction Materials",
            "Engineering & Construction", "Industrial - Distribution", "Industrial - Specialties",
        ],
        # A match counts on its own.
        "searches": [
            ("Liquid and immersion", r"liquid[- ]cool\w*|immersion cool\w*|direct[- ]to[- ]chip|cold plates?|coolant distribution|\bCDUs?\b|\bcoolants?\b"),
            ("Data center cooling", r"data ?cent(er|re)s? (cooling|thermal)|(cooling|thermal)[^.]{0,60}data ?cent(er|re)s?|data ?cent(er|re)s?[^.]{0,60}(cooling|thermal)"),
            ("Air cooling and HVAC", r"air[- ]cool\w*|\bHVAC(R)?\b|\bchillers?\b|cooling towers?|air handl\w+|computer room air|\bCRAC\b|\bCRAH\b|refrigeration"),
            ("Heat rejection and thermal management", r"heat (rejection|exchangers?|transfer|dissipation|removal)|thermal (management|control|solutions?)|rack density|power density"),
        ],
        # A match counts only if a context word also appears in the same description.
        "paired": [],
    },
    "data": {
        "industries": [
            "Software - Application", "Software - Infrastructure", "Software - Services",
            "Information Technology Services", "Financial - Data & Stock Exchanges",
            "Medical - Healthcare Information Services", "Internet Content & Information",
            "Advertising Agencies", "Consulting Services", "Publishing",
        ],
        # A match counts on its own.
        "searches": [
            ("Vertical software", r"vertical(-specific)? (software|saas|cloud|solutions?|platforms?)|\bvertical SaaS\b|industry[- ]specific|domain[- ]specific|system of record|\bERP\b|enterprise resource planning|practice management|case management|records management|property management|student information|electronic health records?|(software|platform|solutions?) (for|serving) (the )?(public sector|state and local|government|hospitality|healthcare|legal|real estate|education|construction|insurance|banks?|credit unions?|financial institutions)"),
            ("Data providers", r"proprietary (data|datasets?|content|databases?|insights?)|data providers?|data (and|&) analytics|analytics (and|&) data|information services|(credit|consumer|market|business|financial|industry|real-world|transaction|merchant|sports) (data|intelligence|information)|data (products?|licens\w+|subscriptions?|feeds?)|licens\w+ (of )?(its |our )?data"),
            ("Databases and data platforms", r"database (platform|software|management|service|as a service|technology|systems?)|\bDBaaS\b|\bNoSQL\b|\bSQL\b|vector database|knowledge graphs?|data warehouse|data lakes?|lakehouse|data platform|data cloud|data management|data integration|data governance|data quality|data catalog|data pipelines?|data engineering|master data|data lineage|\bETL\b|retrieval[- ]augmented|semantic search|embeddings?|\bRAG\b|data readiness|(agent|AI)[- ]ready"),
            ("Platforms and networks", r"first-party data|(user|customer|consumer|member|audience|behavioral|location|sensor|telematics) data|customer data platform|transaction processing|payments? network|advertising (platform|solutions|network)|ad inventory|(online|digital|two-sided) marketplaces?|marketplace (platform|connecting)|connected (vehicles?|cars?)|telematics|fleet data|network of (users|merchants|members|customers)"),
            ("Data preparation", r"training data|human feedback|\bRLHF\b|data (labeling|labelling|annotation|cleansing|cleaning|preparation)|synthetic data|expert (network|contributors?)"),
        ],
        # A match counts only if a context word also appears in the same description.
        "paired": [],
    },
    "trust": {
        "industries": [
            "Software - Infrastructure", "Software - Application", "Information Technology Services",
            "Communication Equipment", "Consulting Services", "Internet Content & Information",
        ],
        # A match counts on its own.
        "searches": [
            ("Identity", r"non-human identit(y|ies)|machine identit(y|ies)|identity (and access|management|security|governance|verification|platform|provider)|\bIAM\b|privileged access|secrets management|access management|zero[- ]trust|single sign-on|multi-?factor|digital identity|identity theft|fraud (prevention|detection)|authentication"),
            ("Security", r"cyber-?security (platform|software|solutions?|products?|services|company|provider|vendor)|endpoint (security|protection|detection)|threat (detection|intelligence|protection|hunting)|prompt injection|guardrails|(data|application|cloud|network|email|web) security|security (platform|operations|posture)|\bSIEM\b|vulnerabilit(y|ies)|firewalls?|ransomware|managed detection"),
            ("Observability", r"observability|application performance|\bAPM\b|log management|\btelemetry\b|\bAIOps\b|monitoring (and|&) (analytics|observability)"),
            ("Governance and cost controls", r"data governance|AI governance|\bGRC\b|governance,? risk|risk (and|&) compliance|compliance (platform|software|management|automation)|policy (management|enforcement)|audit (trail|logging)|spend (limits?|management|controls?)|cloud cost|\bFinOps\b|cost (management|optimization|visibility)|usage metering|metered|API gateways?|(agent|AI|LLM) gateways?"),
            ("Clouds", r"Amazon Web Services|\bAWS\b|Google Cloud|\bAzure\b|Alibaba Cloud|cloud computing (solutions|services)"),
        ],
        # A match counts only if a context word also appears in the same description.
        "paired": [],
    },
    "runtime": {
        "industries": [
            "Software - Infrastructure", "Software - Application", "Information Technology Services",
            "Internet Content & Information",
        ],
        # A match counts on its own.
        "searches": [
            ("Agents and runtime", r"agentic|agent (runtime|harness|platform|framework|infrastructure|orchestration)|(AI|autonomous|software) agents?|\bruntime\b|stateful|sandbox\w*|long-running|durable execution|\borchestration\b"),
            ("Inference and routing", r"\binference\b|model (serving|routing|hosting)|\bvLLM\b|SGLang|TensorRT|\bLLMs?\b|large language models?|foundation models?|route\w* (requests|traffic|workloads)|load balanc\w+|API (management|gateway)s?|\bMLOps\b|machine learning (platform|operations)"),
            ("Clouds and edge", r"serverless|edge (computing|cloud|network|platform|compute)|GPU (cloud|as a service|capacity|clusters?)|AI (cloud|infrastructure|compute)|neocloud|Amazon Web Services|\bAWS\b|Google Cloud|\bAzure\b|Alibaba Cloud|cloud computing (solutions|services)|public cloud|private cloud|hybrid cloud|data cent(er|re) (services|operator)|colocation|Infrastructure as a Service|\bIaaS\b|bare[- ]metal|virtual (servers?|machines?)|managed hosting|web hosting|cloud hosting|GPU (and CPU )?compute|compute (workloads|resources|capacity)|\bKubernetes\b|content delivery networks?|\bCDNs?\b"),
        ],
        # A match counts only if a context word also appears in the same description.
        "paired": [],
    },
    "processors": {
        "industries": [
            "Semiconductors", "Internet Content & Information",
        ],
        # A match counts on its own.
        "searches": [
            ("Accelerators and chips", r"\bGPUs?\b|\bTPUs?\b|\bASICs?\b|\bXPUs?\b|custom (silicon|chips?|processors?)|merchant silicon|accelerated comput\w+|accelerated data cent(er|re)|high-performance accelerators?|AI (chips?|accelerators?|processors?|silicon|servers?|compute)|wafer-scale|\bNPUs?\b|neural processing|\bFPGAs?\b|semi-?custom|customer-specific|Blackwell|Trainium|Inferentia|\bMaia\b|\bMTIA\b|\bInstinct\b|\bJetson\b|\bGaudi\b|mixed fleets?|rack[- ]scale"),
            ("CPUs", r"\bCPUs?\b|server (CPUs?|processors?)|\bmicroprocessors?\b|\bXeon\b|\bEPYC\b|Graviton|Arm-based|Arm Holdings|system[- ]on[- ]chip|\bSoCs?\b|high[- ]performance comput\w+|\bHPC\b|agentic CPU|CPU-to-GPU"),
            ("Software around the accelerator", r"\bCUDA\b|\bROCm\b|\bcompilers?\b|\bkernels?\b|serving frameworks?|software (stack|ecosystem) for (AI|GPU)"),
            ("Hyperscalers", r"Amazon Web Services|\bAWS\b|Google Cloud|\bAzure\b|Alibaba Cloud|Intelligent Cloud|cloud computing (solutions|services)"),
        ],
        # A match counts only if a context word also appears in the same description.
        "paired": [],
    },
    "racks": {
        "industries": [
            "Computer Hardware", "Hardware, Equipment & Parts", "Electrical Equipment & Parts",
            "Communication Equipment", "Technology Distributors",
        ],
        # A match counts on its own.
        "searches": [
            ("Servers and rack systems", r"\bAI servers?\b|rack[- ]scale|rack[- ]level|rack[- ]?mount\w*|rack-mountable|\brack (servers?|systems?|integration|solutions?)\b|integrated rack|full[- ]rack|racks? (and|&) (servers?|enclosures?)|sub-?racks?|blade servers?|BladeSystem|hyperscale (servers?|infrastructure)"),
            ("Servers", r"\bservers?\b"),
            ("Enclosures", r"(server|network|electronic|telecom\w*|data ?cent(er|re)|rack|cabinet)s? enclosures?|enclosures?,? (cabinets?|racks?)|(plastic|metal|custom) (and (plastic|metal) )?enclosures?|enclosure fabrication|\benclosures?, cabinets?"),
            ("Manufacturing and integration", r"electronics? manufacturing|electronic manufacturing|\bEMS\b|systems? assembly|configure[- ]to[- ]order|build[- ]to[- ]order|mechanical integration|\bburn-in\b|box[- ]build|rack integration"),
            ("High-performance computing", r"\bHPC\b|high[- ]performance comput\w+"),
        ],
        # A match counts only if a context word also appears in the same description.
        "paired": [],
    },
    "memory": {
        "industries": [
            "Semiconductors", "Computer Hardware",
        ],
        # A match counts on its own.
        "searches": [
            ("Memory chips", r"\bHBM\d?E?\b|high[- ]bandwidth memory|\bDRAM\b|dynamic random[- ]access memory|\bNAND\b|\bNOR (flash|memory)|\bDDR[3-6]\b|\bLPDDR\w*|\bGDDR\w*|\bDIMMs?\b|\bNVDIMMs?\b"),
            ("Flash and SSDs", r"flash (memory|storage|drives?|-based|chips?|devices?)|solid[- ]state (drives?|storage)|\bSSDs?\b"),
            ("Memory products", r"memory (chips?|devices?|products?|modules?|subsystems?|solutions?|semiconductors?|technolog\w+|manufacturers?|makers?|suppliers?)|semiconductor memory|storage class memory|non-?volatile memory|persistent memory"),
            ("Memory bottleneck", r"\bCXL\b|compute express link|KV cache|memory bandwidth|memory wall|context memory|memory.{0,60}(allocation|constrain\w*|shortages?|tight|lead times?|pricing|supply|capacity)|(allocation|constrain\w*|shortages?|tight|lead times?).{0,60}memory"),
            ("Memory test and stacking", r"memory (test\w*|customers?|fabs?|production)|3D NAND|\bTSVs?\b|through[- ]silicon vias?|hybrid bonding|thermo-?compression|wafer[- ]to[- ]wafer|die[- ]to[- ]wafer|probe cards?|stacked (die|memory)|memory stack\w*"),
            ("Equipment", r"semiconductor (capital )?equipment|semiconductor (processing|fabrication|manufacturing|device manufactur\w+) (equipment|systems?|tools?|process\w*)|wafer fab\w*"),
        ],
        # A match counts only if a context word also appears in the same description.
        "paired": [],
    },
    "tools": {
        "industries": [
            "Software - Application", "Software - Infrastructure", "Software - Services",
            "Information Technology Services", "Financial - Data & Stock Exchanges",
            "Internet Content & Information", "Consulting Services",
        ],
        # A match counts on its own.
        "searches": [
            ("Protocols", r"\bMCP\b|model context protocol|\bA2A\b|agent-to-agent|\bx402\b|\bUCP\b|NLWeb|WebMCP|(agent|AI|LLM) gateways?|agentic (commerce|payments?)"),
            ("APIs", r"application programming interfaces?|\bAPI (management|gateway|platform|first)\b|\bopen APIs\b|(developers?|integrat\w+|connect\w*|build\w*).{0,60}\bAPIs?\b|\bAPIs?\b.{0,60}(developers?|integrat\w+|endpoints?)|developer (platform|tools|ecosystem|portal)|software development kits?|\bSDKs?\b"),
            ("Integration", r"integration (platform|software)|\biPaaS\b|integration platform as a service|workflow automation|data integration|enterprise application integration|middleware"),
            ("Systems of record", r"systems? of record|\bERP\b|enterprise resource planning|\bCRM\b|customer relationship management|human capital management|\bHCM\b|\bpayroll\b|core (banking|processing)"),
            ("Access to data and services", r"search (API|engine)s?|identity (verification|provider|platform|management)|data (feeds?|APIs?)|market data|credit (data|reports?)|\bCPaaS\b|communications platform as a service|messaging (API|platform)"),
            ("Payments", r"payment (network|processing|processor)s?|payments? (platform|solutions?|services)|merchant (acquir\w+|services)"),
        ],
        # A match counts only if a context word also appears in the same description.
        "paired": [],
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
Chooses which staged companies to keep and ranks them, each with a tier and a reason.

#### How
Do these five steps in order.

##### 3.1 Read `AI Sub-Sectors.md`
Read `AI Sub-Sectors.md` in full with the **`Reader Script`**, then find the `{SUBSECTOR}` section and read all of it closely. In the `{SUBSECTOR}` section of `AI Sub-Sectors.md`, the **Companies** subsection says which kinds of company to keep, and the description above it and the **Upside** subsection below it say which of those matter most and why. Use the whole `{SUBSECTOR}` section of `AI Sub-Sectors.md` to decide what to keep in 3.2, rank in 3.3 and write the reasons in 3.4. The **How the downsides apply** subsection is for a later stage of the pipeline. Do not use it to decide what to keep or how to rank.

##### 3.2 Read the staged file and decide what to keep
Read the staged file, `data/screener/{SUBSECTOR}_staged.md`, in full, with the **`Reader Script`**. As you finish each chunk, note the companies to keep, each with its tier and a line on why it fits, since you will rank them and write the reasons from these notes.

###### Reading the staged file
- The only files you read in Step 3 are `AI Sub-Sectors.md` and the staged file, `data/screener/{SUBSECTOR}_staged.md`.
- After chunk 1, say how many chunks there are, and report your progress after every ten chunks.

###### Deciding what to keep
- Keep a company if what it does fits one of the kinds of company in the **Companies** subsection of the `{SUBSECTOR}` section in `AI Sub-Sectors.md`. For a borderline case, use the rest of the `{SUBSECTOR}` section in `AI Sub-Sectors.md` to judge whether it belongs. Judge it by what the company does, not by the matched terms. The terms in the tag are hints only. A company tagged `no match` can still belong, and a company with matches may not.
- Judge each company mainly from its description. What you know about the company can supplement the description, but it may be out of date, so use it as a supplement.
- In the digital sub-sectors (Data, Tools, Trust and Runtime), a description usually does not say what role the company plays for AI or agents. Infer it from what the company does, for example whether its product generates proprietary data as it runs, or whether agents would have to go through it to do their work.
- Give each company you keep one of two tiers:
  - A: `{SUBSECTOR}` is central to what the company does.
  - B: `{SUBSECTOR}` is a meaningful part of the business, or the description is too thin to tell.
  - If it is genuinely borderline, keep it as a B.
- The tier says how much of the business it is. How important a player the company is goes in the reason.

##### 3.3 Combine and rank the list
After the last chunk, combine your notes into one list.
- Rank all the companies, best first, by how well each fits the `{SUBSECTOR}` section in `AI Sub-Sectors.md`. Weigh three things: how much the `{SUBSECTOR}` section in `AI Sub-Sectors.md` values the company's kind of company, which its description and **Upside** subsection show; how central `{SUBSECTOR}` is to the company's business; and how important a player the company is in `{SUBSECTOR}`. Rank across both tiers: a B that the `{SUBSECTOR}` section in `AI Sub-Sectors.md` values more than an A goes above it.
- There is no limit on the length of the list. Step 4 cuts it to 100 from the bottom, so the order decides who is cut.

##### 3.4 Write the picks file
Write the combined list to the picks file, `data/screener/{SUBSECTOR}_picks.md`, with the Write tool.
- One company per line, as `SYMBOL:tier:reason`.
- List the companies in rank order, best first, whatever the tier.
- The file contains the list and nothing else.
- Write each reason as two or three sentences that stand on their own, because later steps will not see the company's description. Say:
  - what the company does that matters for `{SUBSECTOR}`, and which kind of company in the **Companies** subsection of the `{SUBSECTOR}` section in `AI Sub-Sectors.md` that makes it;
  - why that kind of company matters, as the description and **Upside** subsection of the `{SUBSECTOR}` section in `AI Sub-Sectors.md` explain;
  - how central `{SUBSECTOR}` is to the company's business;
  - how important a player the company is in `{SUBSECTOR}`, where its description or what you know shows it.

##### 3.5 Check the picks file
Re-read the picks file, `data/screener/{SUBSECTOR}_picks.md`, and answer these in your reply:
- Before reading the staged file, `data/screener/{SUBSECTOR}_staged.md`, did you read `AI Sub-Sectors.md` in full with the **`Reader Script`**, and read all of the `{SUBSECTOR}` section in it closely?
- Did you read every chunk of `data/screener/{SUBSECTOR}_staged.md` through "end of file" with the **`Reader Script`**, one at a time? How many chunks was that?
- Does the picks file include keeps from the early chunks as well as the later ones?
- Does every company you kept fit one of the kinds of company in the **Companies** subsection of the `{SUBSECTOR}` section in `AI Sub-Sectors.md`, judged from its description? For the borderline cases, did you use the rest of the `{SUBSECTOR}` section in `AI Sub-Sectors.md` to judge whether they belong, and keep them as B?
- Did you give every tier on the same basis? Where two similar companies got different tiers, can you say why?
- Is the order by how well each company fits the `{SUBSECTOR}` section in `AI Sub-Sectors.md`, weighing the three things in 3.3, whatever its tier?
- Does every reason cover the four things 3.4 asks for, in two or three sentences?

#### Required output
The picks file, `data/screener/{SUBSECTOR}_picks.md`. In your reply in the chat, answer the self-check questions. Do not put them in the file.

### Step 4: Build the Candidates file

#### What it does
Adds the screener data to the companies you kept, so they can be assessed in Steps 5 and 6.

#### How
Run the script below as a single inline command, with the sub-sector as the argument: `python3 - {SUBSECTOR} <<'PY'`

The script builds the Candidates file, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`, from the picks file, `data/screener/{SUBSECTOR}_picks.md`. Each company gets its fit rank, fit tier and fit reason alongside its screener columns. If the picks file has more than 100 lines, the script keeps the first 100 and prints the companies it cut, with their tiers.

First, it checks the picks file:
- Every line must have the form `SYMBOL:tier:reason`.
- The tier must be A or B.
- The reason must not be empty.
- Every symbol must be in the staged file.
- No symbol may appear twice.

If any line fails, the script prints the bad lines and stops without building anything. Fix the picks file and run the script again.

#### Required output
The Candidates file, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`, and what the script printed: the number of companies, how many are tier A and how many tier B, and the companies cut, if any.

#### Script
```bash
python3 - {SUBSECTOR} <<'PY'
import csv, datetime, re, sys

SUBSECTOR = sys.argv[1]
SRC = "data/screener/Large_Actives_with_Metrics.csv"
STAGED = f"data/screener/{SUBSECTOR}_staged.md"
PICKS = f"data/screener/{SUBSECTOR}_picks.md"
OUT = f"data/screener/AI Subsectors/{SUBSECTOR} Candidates {datetime.date.today().strftime('%m-%d-%y')}.csv"
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

picks, problems, seen = [], [], set()
with open(PICKS, encoding="utf-8") as fh:
    lines = [(n, l.strip()) for n, l in enumerate(fh, 1) if l.strip()]
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
    picks.append((symbol, tier, reason))

if problems:
    print("The picks file has problems. Nothing was built.")
    print("\n".join(problems))
    sys.exit(1)

cut = picks[CAP:]
picks = picks[:CAP]

with open(OUT, "w", encoding="utf-8", newline="") as fh:
    w = csv.writer(fh)
    w.writerow(["fit_rank", "fit_tier", "fit_reason"] + columns)
    for rank, (symbol, tier, reason) in enumerate(picks, 1):
        w.writerow([rank, tier, reason] + [rows[symbol][c] for c in columns])
print("Companies:", len(picks))
print("Tier A:", sum(1 for p in picks if p[1] == "A"))
print("Tier B:", sum(1 for p in picks if p[1] == "B"))
if cut:
    print(f"Cut at {CAP} ({len(cut)} companies): " + ", ".join(f"{s} ({t})" for s, t, _ in cut))
print("File:", OUT)
PY
```

### Step 5: Prioritize

#### What it does
Assesses each company's growth, strength and price, and ranks the companies into a draft shortlist.

#### How
Do these five steps in order.

##### 5.1 Read `AI Sub-Sectors.md` and the Candidates file
1. Read `AI Sub-Sectors.md` in full with the **`Reader Script`**, then find the `{SUBSECTOR}` section and read all of it closely. Potential growth in 5.2 takes the sub-sector's expected growth from the **Upside** subsection of the `{SUBSECTOR}` section in `AI Sub-Sectors.md`, with the description above it as context. The **How the downsides apply** subsection is for a later stage of the pipeline. Do not use it for potential growth.
2. Read the Candidates file from Step 4, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`, in full, with the **`Reader Script`**.

###### Reading the files
- The only files you read in this step are `AI Sub-Sectors.md` and the Candidates file, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`. Do not look anything up.
- The Candidates file has one row per company: the fit rank, fit tier and fit reason from Step 3, followed by the screener columns.
- A blank value means the figure is not available. Do not treat it as zero.
- Most figures also have a percentile column (`pctl_` prefix): the company's rank on that figure among all the companies the list was drawn from, more than 1,700 in total, from 0 to 100, where higher is always better. It is not a rank within the Candidates file.

##### 5.2 Assess each company
Go through every company in the Candidates file, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`, one at a time, and give it four reads: potential growth, current growth, strength and price. The **`Company Assessment Criteria`**, at the end of this prompt, say how to judge each read. Apply them in full. Each read draws on its own sources:
- Potential growth weighs three things, each from its own source:
  - Where the sub-sector's growth is: the **Upside** subsection of the `{SUBSECTOR}` section in `AI Sub-Sectors.md`.
  - The company's position: its fit reason.
  - How much of its business depends on the sub-sector: its fit tier.
- Current growth, strength and price: the figures in the Candidates file, every figure the **`Company Assessment Criteria`** point to for each read.

Each read is two or three complete sentences and includes the figures it rests on.

##### 5.3 Rank the companies
Rank every company in the Candidates file, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`, best first. Weigh the four reads together. Growth counts most, which means potential growth and current growth, but none of the reads is a filter. A company with great growth and weak financials can rank below one with average growth and strong financials. A great company that is extremely expensive can rank below a good one at a reasonable price. When growth looks similar, strength and price decide.

##### 5.4 Write the Shortlist file
Write the Shortlist file, `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md`, with the Write tool, using the same date as in the Candidates file name.
- The file starts with a short note, a few sentences on what is driving the order, such as who leads and where the main trade-offs are. The note gives only the key figures behind the main drivers.
- Then comes a table with one row per company, with these column headers exactly: `Rank`, `Symbol`, `Company`, `Fit tier`, `Fit reason`, `Potential growth`, `Current growth`, `Strength`, `Price`, `Why`. The fit tier and fit reason are copied from the Candidates file, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`. Do not use the `|` symbol inside a cell, because it separates the columns. The next stage of the pipeline sees only this file, not the Candidates file, so each row has to give it enough to follow the analysis without filling in the blanks.
  - Each read (potential growth, current growth, strength and price) is two or three complete sentences and includes the figures it rests on.
  - The why says what puts the company where it is. It can be as long as it needs to be.
- Support every claim in the reads and the why with the figures it rests on.
- The file contains the note and the table and nothing else.

##### 5.5 Check the Shortlist file
Re-read the Shortlist file, `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md`, and answer these in your reply:
- Did you read the whole Candidates file, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`, with the **`Reader Script`**, one chunk at a time? How many chunks was that?
- Did you apply the full **`Company Assessment Criteria`** to every company, using every figure it points to?
- Did you read `AI Sub-Sectors.md` in full with the **`Reader Script`**, and read all of the `{SUBSECTOR}` section in it closely? Does each company's potential growth weigh the **Upside** subsection of the `{SUBSECTOR}` section in `AI Sub-Sectors.md`, its fit reason and its fit tier?
- Did you rank every company by weighing the four reads from the **`Company Assessment Criteria`** together, and does the table order match them?
- Where two companies with similar figures got different reads on current growth, strength or price, can you say why?
- Does every read give enough context that a reader seeing only this file would understand your analysis and how you reached the conclusion?
- Is every read two or three complete sentences, and does it include the figures it rests on?
- Is the fit reason for every company copied unchanged from the Candidates file, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`?
- Did you check every ranking claim, comparison and superlative in the note, the reads and the why (such as "cheapest" or "below X") against the table order and the figures?

#### Required output
The Shortlist file, `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md`. In your reply in the chat, answer the self-check questions. Do not put them in the file.

### Step 6: Final analysis

#### What it does
Assesses every company again from scratch, tests the draft shortlist against that assessment, and writes the final shortlist. This is the analysis that carries forward to the next stage.

#### How
Do these seven steps in order.

##### 6.1 Re-read Step 5, the Company Assessment Criteria and `AI Sub-Sectors.md`
Before you start, re-read Step 5 and the **`Company Assessment Criteria`** in full, in this prompt. Step 6 uses the same method as Step 5: the assessment in 5.2, the ranking in 5.3, and the Shortlist file's format and rules in 5.4.

Then read `AI Sub-Sectors.md` in full with the **`Reader Script`**, find the `{SUBSECTOR}` section and read all of it closely. Potential growth takes the sub-sector's expected growth from the **Upside** subsection of the `{SUBSECTOR}` section in `AI Sub-Sectors.md`, with the description above it as context. The **How the downsides apply** subsection is for a later stage of the pipeline. Do not use it for potential growth.

##### 6.2 Read the Candidates file
Read the Candidates file from Step 4 in full, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`, with the **`Reader Script`**, and form your own view of each company from the figures.

##### 6.3 Read the draft Shortlist file
Then read the draft Shortlist file from Step 5, `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md` (the same date as in the Candidates file name), in full, with the **`Reader Script`**. It is a first attempt to test, not to defend.

##### 6.4 Assess every company again
Go through every company in the Candidates file, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`, one at a time, as if you were writing the shortlist from scratch. Assess each one as in 5.2: apply the **`Company Assessment Criteria`** in full, with potential growth weighing the **Upside** subsection of the `{SUBSECTOR}` section in `AI Sub-Sectors.md`, the company's fit reason and its fit tier, and current growth, strength and price taken from every figure the **`Company Assessment Criteria`** point to.

Then compare your assessment with the company's row in the draft Shortlist file, `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md`. Decide whether its reads and its why still fit, and rewrite any that do not. Check every comparison in the reads and the why against the figures.

##### 6.5 Rank again
Rank every company again, best first, weighing the four reads together as in Step 5.3. Rank from your own assessment, not from the draft's order. Move any company that the figures say should move.

##### 6.6 Write the final Shortlist file
Write the final Shortlist file over the draft, to `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md`, with the Write tool.
- You may change anything Step 5 produced: the ranking, the four reads, the why, and the note.
- You may not change the figures, the fit tier and fit reason from Step 3, or which companies are in the list.

##### 6.7 Check the final Shortlist file
Re-read the final Shortlist file, `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md`, and answer these in your reply:
- Did you read the whole Candidates file, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`, and the whole draft Shortlist file, `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md`, with the **`Reader Script`**, one chunk at a time?
- Before you started, did you re-read Step 5 and the **`Company Assessment Criteria`** in full, and read `AI Sub-Sectors.md` in full with the **`Reader Script`**, including all of the `{SUBSECTOR}` section? Does each company's potential growth weigh the **Upside** subsection of the `{SUBSECTOR}` section in `AI Sub-Sectors.md`, its fit reason and its fit tier?
- Did you apply the full **`Company Assessment Criteria`** to every company, using every figure it points to? How many companies did you assess again, and for which did you change a read or the why?
- Did you rank every company again from your own assessment, not from the draft's order, weighing the four reads from the **`Company Assessment Criteria`** together? Which ranks changed?
- Where two companies with similar figures got different reads on current growth, strength or price, can you say why?
- Does every read give enough context that a reader seeing only this file would understand your analysis and how you reached the conclusion?
- Is every read two or three complete sentences, and does it include the figures it rests on?
- Is the fit reason for every company copied unchanged from the Candidates file, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`?
- Did you check every ranking claim, comparison and superlative in the note, the reads and the why (such as "cheapest" or "below X") against the table order and the figures?

#### Required output
The final Shortlist file, written over the draft in `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md`. In your reply in the chat, give a short explanation and list of what you changed from the draft and why, then answer the self-check questions. Do not put either in the file.

### Step 7: Clean up

#### What it does
Removes the scratch files, leaving only the outputs.

#### How
Delete the staged file, `data/screener/{SUBSECTOR}_staged.md`, and the picks file, `data/screener/{SUBSECTOR}_picks.md`. Do not delete the Candidates file, `data/screener/AI Subsectors/{SUBSECTOR} Candidates {MM-DD-YY}.csv`, or the Shortlist file, `data/screener/AI Subsectors/{SUBSECTOR} Shortlist {MM-DD-YY}.md`.

## Company Assessment Criteria

### Growth
Expected sales growth, and the risks to that growth, dictate a company's stock price. Growth has two parts: potential growth and current growth.

#### Potential growth
Potential growth is the growth expected over the next 1 to 2 years. It rests on three things:
- Where the expected growth is in the sub-sector. Take this from the **Upside** subsection of the `{SUBSECTOR}` section in `AI Sub-Sectors.md`, with the description above it as context.
- The company's position. The sub-sector's growth may not reach every company in it evenly, so ask whether the company's business sits where the **Upside** subsection says demand is growing, and how much it will benefit, if at all. The fit reason from Step 3 says what the company does in the sub-sector.
- How central the sub-sector is to the company. The fit tier says this: A is central, B is a meaningful part. The more central it is, the more of the company's own sales growth depends on it.

#### Current growth
Current growth is how fast sales are growing now, and whether the pace is speeding up or slowing down. It is the starting point and an indicator of what comes next, but a company growing fast now may not keep doing it.
- `sales_growth_ttm_vs_prior_ttm_pct`: sales over the last four reported quarters compared with the four quarters before, as a percentage. Percentile: `pctl_growth_ttm`.
- `sales_growth_latest_q_yoy_pct`: the latest quarter's sales compared with the same quarter a year earlier. Percentile: `pctl_growth_latest_q`.
- `sales_growth_ttm_accel_pp`: the change in the annual growth rate, in percentage points. Positive means speeding up. Percentile: `pctl_accel_ttm`.
- `sales_growth_4q_net_accel_pp`: the change in the quarterly growth rate over the last year, in percentage points. Positive means speeding up. Percentile: `pctl_accel_4q`.

### Strength
Strength is how well the company would hold up through a downturn, and be positioned to prosper after it. It depends on four things:
- Earning its way. Low costs and good margins make a company strong. A low margin is fine when the company is reinvesting the money in growth. These figures cannot show whether it is, so a low margin alone is not a reason to mark a company down. Margins far above the company's own history are a concern, as described in **`Margins far above history`**.
  - `gross_profit_to_sales_ttm_pct`: gross profit as a percentage of sales. Percentile: `pctl_gross_margin`.
  - `fcf_to_sales_ttm_pct`: free cash flow as a percentage of sales. Negative means it is burning cash. Percentile: `pctl_fcf_margin`.
- Funding itself. Growth that can be funded from free cash flow, not by issuing shares.
  - `fcf_to_sales_ttm_pct`, as above: positive means the business generates the cash to fund its own growth.
  - `shares_outstanding_yoy_change_pct`: the change in share count over the year. Positive means dilution, which can mean it is issuing shares to fund itself. Negative means buybacks.
- Debt. Debt that is manageable compared with free cash flow.
  - `total_debt_to_fcf`: total debt as a multiple of the last 12 months of free cash flow. 4.0 means the debt is four years of free cash flow. Negative means free cash flow is negative.
  - `debt_flag`: "neg FCF" means it carries debt but its free cash flow is zero or negative. "high >10x" means its debt is more than ten years of free cash flow.
- Size. Larger, stronger companies are more likely to survive a downturn and to keep their pricing power and distribution advantages afterward. Size supports the other three, but it does not make up for weak ones.
  - `market_cap_usd`: market value, in US dollars.
  - `sales_ttm_usd`: sales over the last 12 months, in US dollars.

### Price
Price is how much of the expected growth is already in the price. We want companies where the price does not already reflect all of it. Look at two things:
- Valuation. How much the market is paying for the company's sales and earnings. All else equal, lower is better, but exceptional growth can be worth paying for. Avoid extreme valuations, which leave little room for a shortfall in growth.
  - `ev_to_sales_ttm`: enterprise value (market cap plus debt minus cash) divided by the last 12 months of sales. This is the main one. Percentile: `pctl_ev_sales`, where higher means cheaper. The percentile ranks across all industries, so also compare with the other companies in the Candidates file.
  - `pe_ratio_ttm`: market cap divided by the last 12 months of net income. Blank means net income was zero or negative.
- Sentiment. Optimism can mean the growth is already priced in, and pessimism can mean it is not. Valuation reflects sentiment, and so do analyst ratings.
  - `analyst_sell_pct`: the share of analyst ratings that are sell or strong sell. `analyst_count` is the number of ratings. With only a few ratings, the share is a weak signal.

### Margins far above history
High margins and free cash flow are good in themselves. The question is only whether they will last. Margins far above the company's own five-year lows usually come from something temporary, such as a shortage. The bigger the gap, the more competition works to close it. The five-year low can be an unusually weak year, so treat a large gap as a flag, not proof. Margins above peers are not a flag on their own: a company that has always earned more than its peers may simply be better run.
- `gross_profit_to_sales_vs_5yr_trough_pp` and `fcf_to_sales_vs_5yr_trough_pp`: how far the current margin is above its lowest annual level of the last five years, in percentage points. Blank means fewer than five years of data. Percentiles: `pctl_gm_vs_trough` and `pctl_fcf_vs_trough`, where higher means the margin is nearer its five-year low.

A large gap affects every read:
- Potential growth: part of the company's position may be temporary.
- Current growth: growth that comes with high margins may be higher prices more than higher volume, and it fades when the prices do.
- Strength: the company may look stronger than it is. Ask whether it would still be healthy once margins fall back.
- Price: valuation looks cheaper at high margins, so ask what the price implies at normal margins. Pessimism may be the market already pricing margins falling.

A large gap is one concern about the company, even when several reads mention it. When you weigh the reads together in the ranking, do not mark the company down once for each read that mentions it.
