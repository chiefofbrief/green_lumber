# Sector Analyses

## Notes

### https://www.datagravity.dev/p/who-makes-money-when-inference-gets
* Inference getting 10x cheaper is the mechanism of this market, not a threat to it. The deflation is manufactured at the silicon layer and sold at 75% gross margin. It passes through hyperscalers, who convert it into $1.7 trillion of contracted backlog and permanently higher capital intensity. It reaches the labs as a treadmill that grew revenue an order of magnitude while blended margins lagged the software benchmark, though serving margins reportedly hit 70% by mid-2026, the first hard evidence the deflation is reaching the labs’ own P&L. And it lands at the application layer as the best input cost curve in software history, capturable by whoever prices outcomes instead of reselling tokens. Underneath it all, the one layer with rising unit prices, power and land and grid capacity, holds the pricing power everyone else has to engineer. 
* While silicon gets cheaper, electricity, land, and interconnection queues cannot be artificially deflated by engineers. Owners of scarce megawatts now hold the ultimate pricing power.
* Software built on AI currently suffers from poor margins because developers must pay for expensive frontier models to stay competitive. However, as underlying compute costs fall, apps that charge users for resolved tasks—rather than just reselling access to AI models—stand to inherit the best profit margins in software history.
* Cheaper tokens do not just mean more queries. They mean each query is allowed to think longer. Inference-time scaling made tokens-per-task a design variable, and memory, networking, and power all inherit the consequence.
* Semiconductors hold the strangest position in the stack. They are the source of the deflation, and they get paid more every year for manufacturing it.
* Merchant GPU or custom ASIC, every accelerator in this piece routes through the same fabs. TSMC is the one company for whom the ASIC-versus-Nvidia fight is a rounding error.
* The risk to the design layer is share, not demand. Custom ASIC shipments are growing 44.6% in 2026 against 16.1% for merchant GPUs (TrendForce), heading toward roughly 40% of AI servers by 2030, funded by the same four boardrooms that supply most of Nvidia’s revenue. Broadcom booked $30 billion-plus of AI orders in a single quarter and sees $100 billion in 2027; Trainium crossed a $25 billion run rate. Cheaper inference does not shrink the semiconductor pool; units, content per unit, and workload count all rise. It does redistribute the pool toward whoever owns the cost-per-token roadmap, and purpose-built inference silicon is closing that gap faster than it ever did in training.
* Networking rides the same curve with a sturdier margin: Nvidia’s networking segment tripled to $15 billion in a quarter, Arista raised guidance to $12.6 billion with purchase commitments up nearly 3x, and Ethernet optics are on a path to a $100 billion market by 2030 (LightCounting).
* Memory stays a trade, not a holding. It is currently the best trade in the stack, set against the strongest base rate in semiconductors: three well-capitalized suppliers adding capacity into 70%+ margins has always, eventually, mean-reverted. HBM has real reasons to run longer than the usual DRAM clock. Packaging qualification, CoWoS coupling, and multi-year hyperscaler contracts all slow the supply response. Longer is not never. Networking is the durable half of the pair: Arista’s 62-64% gross margins sit on software moats and switching costs the memory names do not have, which is why the prior piece scored it overweight while scoring HBM a trade.
* GE Vernova’s turbine backlog and reservations: 116 GW, sold out into 2031. The scarce input under a 10x-cheaper token is not silicon. It is the interconnection queue, where the median project waits more than five years.

* Positioning. As a stance: own the deflation manufacturers (Nvidia, TSMC) and the un-deflatable bottom (power, grid equipment, and scarce-megawatt owners: the Vertiv and GE Vernova layer). Both ends hold pricing power the middle cannot reach. Treat memory as a trade while the shortage holds, since the capacity response is funded and dated, and hold the networking half of that pair, where the moats are software.

### https://www.globaldatacenterhub.com/p/fiber-is-the-second-queue-why-power 
* Electricity is pushing projects to new areas. Because major cities are running out of power to run massive new data centers, builders are buying land in smaller, less developed towns where electricity is still available.
* Internet cables are the new bottleneck. While these smaller towns have electricity, they do not have the massive underground internet cables required to run a data center. AI needs a totally different cable setup. Older data centers just needed enough cables to send websites to normal internet users. AI computers, however, constantly talk to each other at lightning speed while processing information, which requires ten times as many cables.
* If the fiber cables in the ground are the highways, optical transceivers are the cars, and Co-Packaged Optics (CPO) is the next-generation engine. Because AI computers have to constantly talk to each other ("east-west" traffic), data centers need incredibly fast lasers to push data across those newly laid fiber cables. The industry is rapidly upgrading to ultra-fast optical speeds (800G and 1.6T).
* Co-Packaged Optics (CPO) is a new design where the lasers are attached directly onto the main processing chips, rather than plugged into the front of a metal box. This saves massive amounts of electricity and reduces heat — which is critical because, as the article noted, these buildings are already starving for power.
* The article highlighted a major warning: getting legal permits to lay fiber can delay a data center by 12 to 24 months. If a data center cannot open because it lacks internet cables, the tech companies building them might tell Celestica or Sanmina to pause shipments of the networking racks. While demand is sky-high, these underground cable delays could make revenue for manufacturing companies somewhat choppy or unpredictable quarter-to-quarter.

## AI Applications

**S-Curves**: 
* **AI applications - Software**: Early-mid acceleration - With the exception of foundation models there are no household names.  
* **AI applications - Physical (edge, robotics, etc.)**: Experimentation-early acceleration - Barriers to deployment/adoption are being removed.

**The most value in the entire AI trade will accrue at the application layer**

**Physical AI will have the biggest upside, but reliability and data are a challenge**
* Robots may not need AI for tasks in controlled environments (although they will likely use it), but definitely do for tweaked tasks in real world environments.
* Robots need a higher level of reliability to deploy than software (LLMs).
* There is no equivalent of internet data (LLMs) for robotics. The model and posttraining are critical.
    * There are two model training phases: Pretraining (create a base model using as much knowledge as possible), and posttraining (smaller, more custom datasets).

**World models may solve the data problem for physical AI**
* World Models use sensors, video, GPS, etc. to provide synthetic training environments, reducing the data bottleneck for robotics training.

**Vertical models (domain/task-specific) will eclipse the foundation models, but it'll take time**
* A larger model's capabilities can be distilled into a smaller model.

**Data is key for vertical models**
* Historically, data plus compute has outperformed encoding knowledge (e.g., Alphago). Vertical models would need to buck this trend, and proprietary data/user interaction data may be the key.
* For model training, data quality is the most important thing. Data diversity is also important.

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
 
**Cost is a major concern (and profit lever) for applications**
* Unlike the internet, there is a real marginal cost per customer.

**Good vertical models start with a well-defined workflow, enable superhuman capabilities, and have an immediate ROI**
* Well-defined, repeatable workflows (low ambiguity).
* AI enables superhuman capabilities (e.g., 24/7 work, 100X more data analysis, pattern recognition).
* Start with one worfklow, then expand it others after bulding trust. The entry point should have immediate ROI.

**AI doesn't know the thought that went into an output.**
* AI has been trained on all internet data. But it doesn't have the traces (e.g., the thought that went into a post).

**AI is a productivity tool, but consumers don't care about being more productive.**

--------------

## AI Infrastructure

**S-Curves**:
* **Hardware**: Mid-Late acceleration - Hardware has been decommoditized (innovation matters). But more data/compute is leading to lower marginal returns. 
* **Energy**: ?...Maybe the same, maybe not.

**There is a shortage of energy which must be solved to reduce token costs**
* Models translate compute into intelligence, and they need energy to do that; and the less energy, the more expensive the tokens.

**Inputs into world models (e.g., sensors) may be critical for physical AI**

**The US may invest in infrastructure for physical AI, although reliance on China may be the reality**
* China has a huge advantage in robotics —> US companies rely on China for supplies —> US government/VCs will invest a lot in a US supply chain to catch up and decrease dependency.

**Hardware is currently an area of innovation. But it will be 'commoditized,' favoring low-cost producers**
* AI and chips/memory/power are not the same thing.
* With abundant supply, everyone competes on price. This transforms high margins into low margins, favoring low-cost producers.

**There are 3 ways to improve deep learning on hardware: 1) More cores, 2) Increase communication between cores, 3) Bring memory closer to compute**
* Within the AI investment theme, there is nowhere that the supply chain shifts faster than in networking.

**Increased profits in one layer hurts the profits of downstream layers**
* Memory prices up, Nvidia/AMD profits down.

**How models and usage evolve will have a big impact on the fate of infrastructure providers**
* More customization (e.g., ASICs) may decrease demand for out of the box solutions (e.g., Nvidia GPUs).
* Longer conversations need more memory. But if models get smaller (fewer parameters), less memory may be needed.
* CPUs are critical for agents. But if agent usage is overhyped, CPUs are too.

**Past a certain threshold of intelligence, developers prefer faster tokens to smarter tokens**

**Data centers can take over 4 years from land purchase to datacenter delivery. Power and permits are necessary before they can even be taken seriously**

**The shortage of compute will may get worse before it gets better, which may lead to investment in alternatives**
* It takes longer to make a fab than a data center.
* TSMC didn't build enough capacity in the past few years, so big tech may seek alternatives to avoid another shortage.

**Energy will be the lasting benefit of the AI bubble, although energy producers may end up like telecoms**

--------------

## Energy

**There is a shortage of energy for AI**
* Models translate compute into intelligence, and they need energy to do that; and the less energy, the more expensive the tokens.

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

