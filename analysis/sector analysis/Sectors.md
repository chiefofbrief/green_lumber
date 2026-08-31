# Sector Analyses

## Reading Notes [Not incorporated into the main Takeaways yet]
* 

--------------------

## AI

### S-Curves
* **Applications - Software**: Early-mid acceleration.
   * With the exception of foundation models there are no household names.  
* **Applications - Physical**: Experimentation-early acceleration.
   * LLMs have lowered the barrier to deployment/adoption.
* **Infrastructure - Hardware**: Mid-Late acceleration, but depends on the type of hardware.
   * Hardware has been decommoditized (innovation matters), but scaling appears to be leading to lower marginal returns. 
* **Infrastructure - Energy**: Unsure; a mix of old technologies being ramped up/repurposed and new technologies being developed.

### General Principles
* **Cost/token will decrease over time. Lower cost = More usage.**
  * Cheaper tokens do not just mean more queries. They mean each query is allowed to think longer.
  * Cheaper inference does not shrink the semiconductor pool; units, content per unit, and workload count all rise.
* **It's uncertain how cost/token will decrease. It could be by lowering production costs, squeezing more out of existing hardware, deploying new hardware, new architectures, etc.**
* **In the race to lower cost/token, there will be an oversupply of infrastructure. The uncertainty is when, how, and where (chips, power, models, everything, etc.). Potential ways to hedge are to favor low-cost producers and spread bets.**
  * In a supply glut, everyone competes on price, killing margins.
* **As infrastructure and applications evolve, new constraints and alternatives present themselves, making the "final shape" uncertain. Potential ways to hedge are to focus on providers that win regardless of the alternatives (e.g., winners of both GPUs and custom chips) and spread bets.**
* **The most value in the entire AI trade will accrue at the application layer. The infrastructure layer will become commoditized, although it is currently decommoditized.**
  *  Unlike the internet, there is a real marginal cost per customer. Software built on AI currently suffers from poor margins because developers must pay for expensive frontier models.
  *  Applications will be the biggest beneficiaries of lower cost/token.
* **Increased profits in one layer hurts the profits of downstream layers (e.g., memory prices up, Nvidia/AMD profits down). This can temporarily suppress profits (leading to undervaluation), and/or put sustained pressure on profits that inhibits production (e.g., end users not using expensive models).**

### Applications
* **Physical AI has the biggest upside, but timeline and initial scale is uncertain.**
  * Robots need a higher level of reliability to deploy than software (LLMs).
  * There is no equivalent of internet data (LLMs) for robotics. The model and posttraining are critical.
* **Vertical models (domain/task-specific) will be among the leading applications given their data advantage.**
  * For model training, data quality is the most important thing. 
  * There are two model training phases: Pretraining (create a base model using as much knowledge as possible), and posttraining (smaller, more custom datasets).
  * Historically, data plus compute has outperformed encoding knowledge (e.g., Alphago). Vertical models would need to buck this trend, and proprietary data/user interaction data may be the key.
* **Good vertical models start with a well-defined workflow, enable superhuman capabilities, and have an immediate ROI**
  * Well-defined, repeatable workflows (low ambiguity).
  * AI enables superhuman capabilities (e.g., 24/7 work, 100X more data analysis, pattern recognition).
  * Start with one worfklow, then expand it others after bulding trust. The entry point should have immediate ROI.
* **'Trace' data (the though behind a solution) is/will become critical. LLMs have been trained on all the internet data, but don't know the thought that went into a post.**
* **The first tradeable AI applications may be existing SAAS companies. But they need to get more usage in an agentic world, have a data advantage (proprietary, complex domain), have an engineering/R&D team that can create meaningful AI capabilities, and have leadership that leans into the opportunity so that a meaningful % of sales come from AI.**
  * Vertical SAAS companies (FICO, Tyler, Agilsys) provide the domain-specific data that AI needs to expand beyond general models.
  * Does its product get more usage in an agentic world? (e.g., more usage, more API calls, etc.)
  * Does it have the kind of dataset a foundation model or new entrant couldn’t reconstruct in 12 months? Is the data proprietary?
  * Is the domain complex? (how regulated, specialized, or expert-dependent)
  * Does it have the engineering team, R&D investment, and leadership DNA to build real AI capabilities — not just bolt on a chatbot?
  * Is it deeply embedded in customers’ operations?
  * What % of sales are AI (and rate of change)?

### Infrastructure
* **Lower Cost/Token = more FLOPS/Dollar of compute.**
* **The largest areas of opportunity in hardware for lowering cost/token are getting more out of existing chips, creating new chips, increasing the speed of communication between chips, improving memory efficiency, increasing chip utilization (cooling, electricity, gas), lowering energy cost.**
  * **Custom chips**: Custom ASIC shipments are growing 44.6% in 2026 against 16.1% for merchant GPUs, heading toward roughly 40% of AI servers by 2030.
  * **Networking/Optical**: If the fiber cables in the ground are the highways, optical transceivers are the cars, and Co-Packaged Optics (CPO) is the next-generation engine. Because AI computers have to constantly talk to each other ("east-west" traffic), data centers need incredibly fast lasers to push data across those newly laid fiber cables. Co-Packaged Optics (CPO) saves massive amounts of electricity and reduces heat.
  * **Memory**: Find a balance between off-chip memory for capacity (DRAM) and on-chip memory for speed (SRAM). Also, improve KV cache compression so less memory is needed.
  * **Energy**: Models translate compute into intelligence, and they need energy to do that; and the less energy, the more expensive the tokens. There is a shortage of energy which must be solved to reduce token costs (GE Vernova’s turbine backlog and reservations: 116 GW, sold out into 2031).
* **More data centers should lower cost/token. The timeline for construction/deployment is uncertain and subject to uncontrollable items (component shortages, permits, utilities, regulation), but the level of investment can be assessed by checking the sales of equipment providers (e.g., GEV).**
  * Developers now order power equipment years before a project has a customer or a final go-ahead. Large power transformers, the equipment that converts the very high voltage carried by long-distance power lines into a voltage a building can actually use, now average 128 weeks from order to delivery.
  * Because major cities are running out of power to run massive new data centers, builders are buying land in smaller, less developed towns where electricity is still available. While these smaller towns have electricity, they do not have the massive underground internet cables required to run a data center. AI needs a totally different cable setup.
* **Component suppliers to data centers may be lucrative in the near term, but they do present significant risk in the event of a delay (which could lead to delayed/cancelled POs). Potential ways to hedge are to focus on leaders whose orders are less likely to be cancelled in a delay, and focus on the fastest growing segments.**
* Physical AI needs additional hardware beyond what LLMs require as they rely on world models, which use sensors, video, GPS, etc. to provide synthetic training environments, reducing the data bottleneck for robotics training. While it remains to be seen, US companies may invest in these components to reduce the reliance on China. 






--------------

## Energy

**Energy will be the lasting benefit of the AI bubble, although energy producers may end up like telecoms**
* Perhaps instead of chips, power will be the scarce resource which becomes overabundant due to overbuild.

**This is the first real load growth for US power in ~two decades, and the market isn't built for it**
* Three demand shocks are hitting at once: datacenters, electrification (EVs, heat pumps), and reshoring/industrial.
* The current providers have temporary pricing power. 

**Natural gas is filling the gap, and datacenters are increasingly bypassing the grid entirely to get it**
* Datacenter gas demand is small now but growing fast. 
* Renewables are intermittent and nuclear is slow, but gas can be built now and runs 24/7.
* "Behind-the-meter" — building gas plants on-site at the datacenter — sidesteps the pipeline and interconnection bottlenecks.

**US gas is cheap and abundant, partly because it's a byproduct of oil drilling**
* It's nearly free in some places (Waha went negative for months), and that cheap fuel is what makes behind-the-meter and LNG work.
* But the cheapest gas comes up alongside oil, so supply is partly tied to oil economics rather than gas demand.

**LNG export is a more structural, large pull on the same gas**
* What drives the exporters is the gap between cheap US gas and much higher prices in Europe (TTF) and Asia (JKM)
* It's bigger than datacenter demand today.
* Terminals take years to build, so the demand is locked in rather than on/off.

**Fuel is abundant, but everything needed to use it is scarce**
* Gas turbines, transformers, transmission, and permits.
* Cheap gas doesn't make the gas producer rich.

**Nuclear is a potential long-term answer but a poor near-term one**
* Near-term, restarting existing plants is far more credible than new construction.

-----------------------

## APPENDIX

### Key Sectors Analysis (based on screener output)

**AI, Aerospace, and Energy are the three big real-demand growth themes.**
* Financial companies were excluded despite being prominent among the top growers (banks, asset management, REITs). 
* The only strong industries that *don't* fit are **Gold** and **Biotech** — set aside.
* Source: Large_Actives_with_Metrics.csv. "High-growth" = growth_score ≥ 66 (440 companies, 366 excluding financial companies; roughly 20% of total sample). 

**Data:**

| Theme | Industry | Count (# of companies that clear the ≥66 bar) | Concentration (% of the industry that clears the ≥66 bar)  | Avg score |
|---|---|---|---|---|
| **AI** | Semiconductors ★ | 30 | 38% | 52.7 |
| | Software – Application | 25 | 23% | 45.5 |
| | Software – Infrastructure | 17 | 27% | 49.8 |
| | Hardware, Equipment & Parts | 10 | 29% | 48.7 |
| | Communication Equipment | 7 | 33% | 50.0 |
| | Computer Hardware | 7 | 54% | 59.4 |
| | Electrical Equipment & Parts | 7 | 33% | 45.8 |
| | Technology Distributors | 3 | 60% | 58.9 |
| | Copper | 4 | 80% | 63.7 |
| **Aerospace** | Aerospace & Defense ★ | 18 | 39% | 50.4 |
| **Energy** | Engineering & Construction | 10 | 37% | 48.2 |
| | Oil & Gas E&P | 10 | 28% | 46.1 |
| | Solar | 4 | 67% | 61.9 |
| | Independent Power Producers | 2 | 40% | 55.6 |


- **★** = top-10 on both breadth *and* concentration.


**Set aside:**

| Industry | Growth names | Concentration | Avg score | Why out |
|---|---|---|---|---|
| Gold ★ | 22 | 85% | 79.1 | commodity price / monetary — its own driver (strongest industry overall, but pure price) |
| Other Precious Metals ★ | 7 | 100% | 77.3 | commodity price / monetary — same driver as gold |
| Biotechnology | 26 | 28% | 44.8 | lottery — binary trial outcomes; big by count, thin by concentration |
| Industrial Materials | 4 | 44% | 58.4 | commodity materials — price-driven, no clean theme |

--------------

