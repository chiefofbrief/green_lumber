# AI Extraction Prompt

## Role
You extract verbatim excerpts about AI for a stock analysis pipeline. You do this by running one script that greps the company's long documents (earnings call transcripts, 10-K, 10-Q) and writes the matches to an extracts file. You do not read the documents, analyze the matches, or alter any text.

All output lands in `/workspaces/green_lumber/data/companies/{TICKER}/{TICKER}_ai_extracts.md`.

## Rules
- Run the script in Step 2 exactly as written. Do not add, remove, or edit any search term, section title, or snippet width.
- Do not read the extracts file or any source document. Only the script output (the per-section hit counts) is needed.
- Empty sections are expected. A company will not touch most layers.
- Do not write commentary or summaries into the extracts file. It contains section headers and excerpts only.

## Flow

### Step 1 — Ticker
Get the `{TICKER}`. If none is given, ask for one before starting.

### Step 2 — Run the extraction
Run the following in a single script. Replace `{TICKER}` with the ticker. The script flattens each file into one line (so phrases wrapped across lines still match), writes each section's matches under its own header, prints each section's hit count, and removes exact-duplicate lines at the end.

```bash
SRC="/workspaces/green_lumber/data/companies/{TICKER}"
OUT="$SRC/{TICKER}_ai_extracts.md"
FILES=$(ls $SRC/*.md $SRC/*.txt | grep -v -e "_data_summary" -e "Excerpts" -e "_ai_extracts")
: > "$OUT"

ex() {  # $1 = section title, $2 = pattern, $3 = snippet width (default 150)
  w=${3:-150}
  hits=$(for f in $FILES; do
    tr '\n' ' ' < "$f" | grep -oiE ".{0,$w}($2).{0,$w}" | sed "s|^|($(basename "$f")) |"
  done)
  echo -e "\n## $1\n" >> "$OUT"
  [ -n "$hits" ] && echo "$hits" >> "$OUT"
  echo "$1: $(echo -n "$hits" | grep -c .) hits"
}

ex "1. Business and Segments" "reportable segments?|operating segments?|end markets?|principal products|we design|we manufacture"

ex "2. AI Exposure, Revenue, and Customers" "\bAI\b.{0,100}(revenue|demand|customers?|infrastructure|workloads?|servers?|programs?)|artificial intelligence|hyperscal(er|ers|e)|cloud service providers?|data cent(er|re)s?|significant customers?|largest customers?|major customers?|customer concentration|customers?.{0,80}(accounted for|represented).{0,60}(%|percent)|OpenAI|Anthropic|CoreWeave"

ex "3a. Physical Infrastructure: Accelerators and Chips" "\bGPUs?\b|\bTPUs?\b|\bASICs?\b|\bXPUs?\b|custom silicon|merchant silicon|AI accelerators?|accelerated comput|AI servers?|rack-scale|Blackwell|Rubin|Trainium|\bchips?\b|semiconductors?|mixed fleets?"

ex "3b. Physical Infrastructure: Memory" "\bHBM\b|high[- ]bandwidth memory|\bDRAM\b|\bNAND\b|\bCXL\b|KV cache|memory bandwidth|memory (shortage|supply|pricing|capacity)|flash storage" 250

ex "3c. Physical Infrastructure: Wafers, Foundry, and Packaging" "wafers?|foundr(y|ies)|TSMC|CoWoS|advanced packaging|2\.5D|3D packaging|sole[- ]source|single[- ]source|Amkor|leading[- ]edge" 250

ex "3d. Physical Infrastructure: Networking" "optical|transceivers?|co-packaged|\bCPO\b|silicon photonics|\blasers?\b|InfiniBand|Ethernet|NVLink|UALink|\bAEC\b|\bcopper\b|pluggables?|scale[- ]up|scale[- ]out|scale[- ]across|\b(400|800)G\b|1\.6T|1\.6 terabit|data center interconnect|AI networking" 250

ex "3e. Physical Infrastructure: CPUs" "\bCPUs?\b|server CPUs?|agentic CPU|\bXeon\b|\bEPYC\b|Graviton|Arm-based|CPU-to-GPU" 250

ex "3f. Physical Infrastructure: Cooling" "liquid[- ]cool(ing|ed)|air[- ]cool(ing|ed)|coolants?|cold plates?|\bCDUs?\b|direct-to-chip|immersion cooling|heat rejection|thermal management|rack density|power density" 250

ex "3g. Physical Infrastructure: Power" "natural gas|gas turbines?|behind-the-meter|on-site (power|generation)|grid (connection|interconnection)|power (constraint|availability|infrastructure|shortage)|megawatts?|gigawatts?|\bGW\b|nuclear|geothermal|energy storage|transformers?|switchgear" 250

ex "3h. Physical Infrastructure: Data Center Buildout" "data cent(er|re) (construction|capacity|delays?|buildout|build-out|development)|powered shell|colocation|time to power|permits?.{0,80}data cent|data cent.{0,80}permits?|capacity coming online|bought but not deployed|deployment delays" 250

ex "4a. Digital Infrastructure: Models and Inference" "\binference\b|\bLLMs?\b|large language models?|foundation models?|AI-native|quantization|\btokens?\b.{0,60}(cost|price|pricing|usage)|usage-based pricing|consumption-based pricing|fine-tun(ed|ing)"

ex "4b. Digital Infrastructure: Agents, Runtime, and Orchestration" "agentic|\bagents?\b.{0,80}(AI|model|LLM|software|autonomous)|(AI|model|LLM|autonomous).{0,80}\bagents?\b|runtime|orchestration|harness|stateful|sandbox|agent memory|vector database|knowledge graph"

ex "4c. Digital Infrastructure: Trust and Security" "non-human identity|machine identity|privileged access|prompt injection|guardrails|(governance|observability).{0,100}(AI|agents?|model)|(AI|agents?|model).{0,100}(governance|observability)" 250

ex "4d. Digital Infrastructure: Protocols and Tools" "\bMCP\b|model context protocol|\bA2A\b|agent-to-agent|x402|NLWeb|agent gateways?" 250

ex "4e. Digital Infrastructure: Data and Proprietary IP" "proprietary data|domain-specific|system of record|AI-(powered|enabled)|embedded AI|data readiness|(intellectual property|proprietary).{0,100}(AI|data|model|software)|(AI|data|model|software).{0,100}(intellectual property|proprietary)"

ex "5. Physical AI" "robots?|robotics|humanoid|actuators?|roller screws?|harmonic drive|rare[- ]earth|magnets?|motor controllers?|lidar|force sensors?|torque sensors?|machine vision|autonomous (vehicles?|systems?)|edge (AI|inference)|world models?|vision-action|warehouse automation|predictive maintenance" 250

ex "6. Shortage, Pricing, and Backlog" "(shortages?|lead times?|supply constraints?).{0,100}(memory|HBM|DRAM|NAND|wafers?|packaging|components?|power|transformers?|optical|lasers?|GPUs?|chips?|AI|data cent)|(memory|HBM|DRAM|NAND|wafers?|packaging|components?|power|transformers?|optical|lasers?|GPUs?|chips?|AI|data cent).{0,100}(shortages?|lead times?|supply constraints?)|sold out|supply[- ]constrained|capacity constrained|price (increases?|decreases?)|pricing (power|actions?)|backlog|remaining performance obligations?|\bRPO\b|book-to-bill|design wins?|multi-?year (agreements?|contracts?|visibility|programs?)|customer commitments?"

ex "7. AI Investments" "capital expenditures?|\bcapex\b|capacity (expansion|addition|investment)|new (facility|plant|factory|campus|fab)|production ramp|ramp(ing)? (up )?(production|capacity)|greenfield|brownfield|purchase commitments?|bolt-on|tuck-in|joint venture|(acquisitions?|acquired).{0,100}(AI|data cent|capacity|manufacturing|infrastructure|capabilit)|(AI|data cent|capacity|manufacturing|infrastructure|capabilit).{0,100}(acquisitions?|acquired)"

ex "8. Funding for AI Investments" "equity offerings?|public offerings?|follow-on|at-the-market|convertible (notes|debt)|senior notes|term loans?|credit facilit(y|ies)|revolving|special purpose (vehicle|entity)|\bSPV\b|variable interest|off-balance|vendor financing|customer financing|circular (demand|financing|arrangements?)|(customers?|suppliers?).{0,80}(equity investment|loans?|financing)|advance payments?" 250

ex "9. Management Commentary on AI" "(we are investing|our priority|our priorities|we remain (confident|committed)|we are committed).{0,150}(AI|data cent|capacity|infrastructure)|\bAI\b.{0,150}(risks?|uncertain(ty|ties)?|challenges?|headwinds?|cautious|digestion|slowdown|normaliz(e|ation)|lumpy)|(risks?|uncertain(ty|ties)?|headwinds?|digestion|slowdown|lumpy).{0,150}\bAI\b|overcapacity|oversupply|overbuild|capex (cuts?|reductions?)|cancell?ations?"

ex "10. AI's Effect on the Financials" "(gross margin|operating margin|margins?).{0,150}(AI|inference|compute)|(AI|inference|compute).{0,150}(gross margin|operating margin|margins?)|inference costs?|cost to serve|compute costs?|margin pressure|dilutive to (gross )?margin|AI revenue|AI-related revenue|AI (bookings|pipeline|run rate)|return on (investment|capital)|\bROIC\b|payback|(free cash flow|cash flow).{0,150}(AI|data cent)|(AI|data cent).{0,150}(free cash flow|cash flow)"

awk '!seen[$0]++' "$OUT" > "$OUT.tmp" && mv "$OUT.tmp" "$OUT"
```

### Step 3 — Report
Report the hit count for each section, as printed by the script, and the final file size (`wc -c "$OUT"`). Do not summarize the contents.
