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

**Cost/token will decrease over time. Lower cost = More usage.**
* Cheaper tokens do not just mean more queries. They mean each query is allowed to think longer.
* Cheaper inference does not shrink the semiconductor pool; units, content per unit, and workload count all rise.

**The interesting question is how cost/token will decrease. It could be by lowering production costs, squeezing more out of existing hardware, deploying new hardware, new architectures, etc.**

**There will be an oversupply of infrastructure; the only uncertainty is when it affects the suppliers, and whether it will be in chips, power, models, or all of the above. We can hedge against this by favoring low-cost producers with sustainable margins.**
* In a supply glut, everyone competes on price. 

**The most value in the entire AI trade will accrue at the application layer, particularly as cost/token decreases. The infrastructure layer will become commoditized, but is currently decommoditized.**
*  Unlike the internet, there is a real marginal cost per customer. Software built on AI currently suffers from poor margins because developers must pay for expensive frontier models.
 
**When there is a shortage/constraint, companies invest in alternatives, and we should focus on providers that win regardless of the alternatives.**
* Example: Focus on companies that benefit from both 'out-of-the-box' GPU adoption and custom chips, as it is uncertain what portion of future chips will be custom.

**Increased profits in one layer hurts the profits of downstream layers, and we should be aware of what being bullish on one layer means for others.**
* Memory prices up, Nvidia/AMD profits down.

### Applications

**Physical AI has the biggest upside, but timeline and initial scale is uncertain.**
* Robots need a higher level of reliability to deploy than software (LLMs).
* There is no equivalent of internet data (LLMs) for robotics. The model and posttraining are critical.

**Vertical models (domain/task-specific) will be among the leading applications given their data advantage.**
* For model training, data quality is the most important thing. Data diversity is also important.
* There are two model training phases: Pretraining (create a base model using as much knowledge as possible), and posttraining (smaller, more custom datasets).
* Historically, data plus compute has outperformed encoding knowledge (e.g., Alphago). Vertical models would need to buck this trend, and proprietary data/user interaction data may be the key.



**Cost/token can be improved by lowering production costs, squeezing more out of existing hardware, deploying new hardware, and new architectures. The ultimate goal is more FLOPS/dollar of compute. Currently, major areas of opportunity include: Custom chips, communication between chips (networking, optical), memory, higher chip utilization (cooling, electricity, gas), domain-specific models.**
* **Custom chips**: Custom ASIC shipments are growing 44.6% in 2026 against 16.1% for merchant GPUs, heading toward roughly 40% of AI servers by 2030.
* **Networking**: If the fiber cables in the ground are the highways, optical transceivers are the cars, and Co-Packaged Optics (CPO) is the next-generation engine. Because AI computers have to constantly talk to each other ("east-west" traffic), data centers need incredibly fast lasers to push data across those newly laid fiber cables. Co-Packaged Optics (CPO) saves massive amounts of electricity and reduces heat.
* **Memory**: Find a balance between off-chip memory for capacity (DRAM) and on-chip memory for speed (SRAM). Also, improve KV cache compression so less memory is needed. 
* **Energy**: Models translate compute into intelligence, and they need energy to do that; and the less energy, the more expensive the tokens. There is a shortage of energy which must be solved to reduce token costs (GE Vernova’s turbine backlog and reservations: 116 GW, sold out into 2031).





There are 3 ways to improve deep learning on hardware: 1) More cores, 2) Increase communication between cores, 3) Bring memory closer to compute.





**Data centers are a primary point of leverage for decreasing cost/token, but the timeline for construction/deployment is uncertain and subject to uncontrollable items (e.g., regulation). This presents both upside and downside for potential investments: Component suppliers benefit from the buildout, but are also at risk of order delays/cancellations due to a slowdown. The best way to track progress is to check the sales of equipment providers (e.g., GEV), not announcements.**
* Developers now order power equipment years before a project has a customer or a final go-ahead. Large power transformers, the equipment that converts the very high voltage carried by long-distance power lines into a voltage a building can actually use, now average 128 weeks from order to delivery.
* Because major cities are running out of power to run massive new data centers, builders are buying land in smaller, less developed towns where electricity is still available. While these smaller towns have electricity, they do not have the massive underground internet cables required to run a data center. AI needs a totally different cable setup.






**Inputs into world models (e.g., sensors) may be critical for physical AI**

**The US may invest in infrastructure for physical AI, although reliance on China may be the reality**
* China has a huge advantage in robotics —> US companies rely on China for supplies —> US government/VCs will invest a lot in a US supply chain to catch up and decrease dependency.



**World models may solve the data problem for physical AI**
* World Models use sensors, video, GPS, etc. to provide synthetic training environments, reducing the data bottleneck for robotics training.

**Good vertical models start with a well-defined workflow, enable superhuman capabilities, and have an immediate ROI**
* Well-defined, repeatable workflows (low ambiguity).
* AI enables superhuman capabilities (e.g., 24/7 work, 100X more data analysis, pattern recognition).
* Start with one worfklow, then expand it others after bulding trust. The entry point should have immediate ROI.

**AI doesn't know the thought that went into an output.**
* AI has been trained on all internet data. But it doesn't have the traces (e.g., the thought that went into a post).

**Legacy SAAS may be a beneficiary, particularly as a source of data. But software is getting cheaper to build**
* Bull case:
    * Vertical SAAS companies (FICO, Tyler, Agilsys) provide the domain-specific data that AI needs to expand beyond general models.
    * SAAS might leverage their data and customer relationships to provide AI applications. 
* Bear case:
    * Cheaper to build software is probably cheaper to buy, narrowing margins.
    * The shift from per-seat/licensing to token-based pricing also hurts margins.
    * The sales process was designed around seat-based, not token-based, pricing.
* Key questions:
    * Does its product get more usage in an agentic world? (e.g., more usage, more API calls, etc.)
    * Does it have the kind of dataset a foundation model or new entrant couldn’t reconstruct in 12 months? Is the data proprietary?
    * Is the domain complex? (how regulated, specialized, or expert-dependent)
    * Does it have the engineering team, R&D investment, and leadership DNA to build real AI capabilities — not just bolt on a chatbot
    * Is it deeply embedded in customers’ operations?
    * What % of sales are AI (and rate of change)?
    * What is the market share (and rate of change)?






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

