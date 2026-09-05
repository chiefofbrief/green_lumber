# Sectors

"AI" (machine learning, models, accelerators, data centers, power, software applications, edge, robotics, etc.) is the umbrella which impacts the majority of our investments. We don't aim to understand every detail, nuance, or future development; rather, we want to develop a flexible, antifragile picture of the current and future landscapes which is (just) specific enough to be actionable.

----------

## ASSUMPOTIONS

AI models are powerful applications. But as with all technologies, enthusiasts are overly optimistic about their future capabilities, the timeline for deployment of those capabilities, and people's willingness to change existing behaviors. Things will likely progress more slowly than optimistic estimates. 

AI infrastructure and AI applications are not the same thing. The majority of value will ultimately accrue at the application layer, but we are in the infrastructure buildout phase, during which the primary goal is to lower the cost of deploying applications. Many investors conflate the two, which is why they are overly optimistic/pessimistic about AI capex. 

There will be overinvestment in AI infrastructure, lowering the cost for application providers but leading to price competition (and lower margins) among infrastructure providers, which strongly favors low-cost producers. The timeline for oversupply is uncertain, but it's likely longer than the mainstream assumption and can be approximated as slowing equipment orders (at least for physical infrastructure). 

It's possible that investment in AI infrastructure temporarily stalls. A sustained lack of FCF (along with depressed stock prices) for hyperscalers is a likely cause. Slowing equipment orders may be an early signal. 
* Hyperscalers have moved down the capital curve from FCF to debt to equity; if they do not revert to FCF, investors may punish them.

There are two primary components of AI infrastructure, both of which are being developed at the same time: Physical infrastructure (hardware, data centers, power, etc.) and Digital infrastructure (models, data, architectures, protocols, etc.). Both are critical for cost-effective deployment of AI applications at scale.  

The hot areas within physical infrastructure are split between the chips themselves (accelerators) and the facilities that house them (data centers). Custom chips, more efficient memory, and networking (increasing the speed of communication between chips) are levers being explored to improve accelerators. Reliable sources of electricity (mainly natural gas) and sufficient cooling are big concerns for data centers. 
* Accelerators are designed to do massive amounts of specialized math simultaneously, which requires compute (cores), fast memory, and fabric (high-speed interconnects that link chips). 
* Data centers take in electricity and output heat.
  * To get electricity, the only functional source is natural gas; while solar, batteries, and nuclear may be options in the future, they are currently constrained. But, advanced geothermal is a wildcard. 
   * Solar panels are getting cheaper, but the other costs involved with them (land, labor, transmission, etc.) are not. The lack of transmission lines is maybe the biggest problem.
   * Batteries are getting cheaper, but other costs involved with them (e.g., lithium) are not.
   * Nuclear is a long-term play. There are only so many existing plants, new plants take time to build, and new nuclear technologies are not proven.
   * Advanced geothermal sits in the middle of natural gas, solar, and nuclear (runs 24/7, leverages existing oil and gas drilling equipment, zero emissions).
  * Overhauling cooling systems to maintain/improve chip utilization is needed to remove heat. 

The hot areas within digital infrastructure are data, models, and autonomous systems (primarily 'agents'). Autonomous actions leveraging domain/task-specific models is a likely end state, and domain-specific data, data 'traces' (the thought that went into an output), and agentic infrastructure are necessary to make it possible. 
* AI has only distilled the end state of human thought by being trained on internet data. 
* Domain-specific data is necessary to expand beyond general models. Potential sources include end customers (e.g., a law firm providing its data), third-party model trainers (e.g., Mercor), and vertical SAAS companies (e.g., Tyler, Agilsys).
* While foundation models are currently in the spotlight, the conversation has already shifted to the open-source vs. closed debate, which is really a conversation about cost and privacy. The conversation will eventually shift to domain/task-specific models, which provide a higher ROI.  
   * Most investors don't realize that open-source models are not free and in fact have a marginal cost for inference.
   * Historically, data plus compute has outperformed encoding knowledge (e.g., Alphago). Vertical models would need to buck this trend, and proprietary data/user interaction data may be the key.
 * Solutions for agents are mainly focused on observability (monitoring what is being done with agents) and governance (controlling what can be done with agents) for enterprises. But for autonomous systems to reach their potential, better infrastructure is needed and is currently being built (e.g., A2A for communication between agents, x402 for agentic payments). 

'Incumbents' (pre-2023 companies) are providing/building the majority of the infrastructure, and that is unlikely to change. Preferred vendors will remain the preferred vendors. They stand to benefit in the near-term as the infrastructure is built and used, and suffer in the longer-term as prices drop.
* The likelihood of the US onshoring manufacturing to compete with China is likely overrated (e.g., US probably won't build fabs that compete with TSMC).

The applications with the biggest upside may be in physical AI, but the timeline is uncertain. The barrier to deployment has been lowered by LLMs, which allow training through conversation, and could be accelerated further by 3 things: 1) Foundation models for robotics, 2) World models to assist in creating those foundation models, and 3) Data collection. 
 * A foundation model for robots means they can pick up a new task with limited training instead of being built for specific tasks.
 * Instead of getting all the data prior to deployment, robots just need to get good enough that they can be deployed and gather data to improve. Domains where collecting data is easy will have better robotics even if they are physically challenging.

As with all previous eras, there will be leading applications that help vendors sell things and advertise what they're selling. 







---------------



Strong existing solutions/providers are probably better bets than novel ones. The main reasons: 

## Notes [LLMs should ignore this section]

Chips will move to a hybrid approach, where GPUs and custom chips could work together in the same data center. Currently the trend is to disaggregate prefill and decide to improve GPU utlilization, which requires faster interconnects to transfer the KV cache. 

Because of the amount of investment in data centers/AI, even minor efficiency improvements can have a huge impact (and make a lot of money).

Advanced geothermal is one of the most interesting sources of energy today. 
 
LLMs help you create human-type inputs. Deep learning (reinforcement learning) helps you identify things humans wouldn't think of. 

A deficit of natural gas will arrive in 2028. It will be felt the most in electricity prices. Before the AI buildout, LNG was the main driver of demand. There is more gas under the ground; the problem is not that we are literally running out of gas, but rather cost-effective deployment. Processing is the first major constraint. Gathering is another constraint. Natural has is the primary fuel to power AI. The winners may be gas producers. Solar could benefit as well as electricity prices increase, but the infrastructure has issues. The biggest winners in the stock market thus far have been providers of turbines or distributed power, but these industries are cyclical. Drillers make drilling decisions based on oil, gas is a byproduct. The US is the leading exporter of gas; fi there is a gas shortage, curtailing exports of LNG is possible but unlikely given the dependency from other countries. Portable power also needs gas. Power sources like solar that don't require gas or electric are interesting, but are they cost-effective?






---------------


* Will custom ASICs take a meaningful chunk of market share away from Nvidia's GPUs?
   * What is the difference between a GPU and a custom ASIC?
   * AVGO, GUC, Wiwynn (wiwynn suppliers: TE connectivity, mpley, foci, browave, senko, afl)
   * AWS has been heavily promoting its Trainium and Graviton chips as alternatives to Nvidia Corp.’s graphics processing units
* How does the usage of Chinese models compare to US models?
   * What is the leading Chinese model?
* How is data center construction progressing?
   * What is required for an operational data center?
      * compute, networking, storage, power, cooling
      * Vertiv, Schneider Electric, Eaton, Jacobs, Phaidra, Procore, PTC, Siemens, Switch, Trane Technologies, Cadence, and Dassault Systèmes, GE Vernova
      * Target Hospitality is a company that provides workforce lodging and other temporary, modular housing used for oil, gas and mining operations
   * Which energy sources are powering data centers?
      * The most formidable accelerant of gas burn for structural growth—lasting generation demand—is data center load.
      * Nuclear stocks are gaining attention due to the massive electricity demand projected from the AI data center buildout (BWX, Cameco)
   * What raw materials are necessary? Are there enough?
      * Cameco’s uranium-positioning detail goes beyond “high-grade mines”: the company is described as producing about 15% of the 164 million pounds of uranium produced in 2025, behind Kazatomprom at 20%.
      * Energy Fuels Inc. (UUUU) is currently the leading producer of uranium in the United States
   * Why is cooling changing?
      * Are chips that require liquid cooling being deployed?
      * 45 percent use a fully air-cooled system, while 42 percent use a hybrid air-and-liquid-cooled system. Just 12 percent use liquid cooling only.
      * Schneider Electric, Vertiv, Johnson Controls, Hewlett Packard Enterprise, Green Revolution Cooling, Submer, LiquidStack, and Asetek Inc.
* What's the big deal with CPO?
   * Is CPO reaching commercial deployment?
   * Is electrical/copper networking good enough for now?
* Is networking a real bottleneck? (WTF does it mean)
   * More memory in a system allows model providers to: 1. fit a larger model (more parameters). 2. serve more concurrent requests, i.e. more users (more KV Cache). 3. support larger context windows, i.e. larger sequence lengths per request (more KV Cache). Inference providers make a business out of using all the above, which is why memory capacity per GPU is increasing. Not only that, but usable memory is not limited to a single package, since a workload can be sharded over multiple chips and aggregate memory can be pooled together within a scale up fabric. That’s why networking is such a key competitive battleground for all the AI hardware companies.
   * Nvidia and Broadcom are the two market leaders in CPO, as both are leaders in switching ASICs. Nvidia has the largest networking business in the world.
   * POET, Coherent, Lumentum,  Applied Optoelectronics, Mediatek, Cargan, Aoet, Corning (fiber), Selectics, Elite Materials
   * terbium and dysprosium
* How are chips made?
   * Steps in the chip manufacturing process: 1. Deposition: Different materials – conductors, insulating films and semiconductors – are deposited onto a silicon wafer. 2. Photoresist coating: The wafer is coated with a light-sensitive layer called photoresist. 3. Lithography: The microchip pattern is printed by using light to project it onto the wafer. 4. Baking and developing: The wafer is baked and developed to fix the pattern in the photoresist. 5. Etching: Reactive gases are used to etch away excess material, leaving the circuit pattern behind. 6. Ion implantation: The wafer may be bombarded with ions to tune the semiconductor’s properties. 7. Photoresist
   * advanced packaging with Amkor and SPIL
* What are substrates and wafers?
   * demand from AI GPUs, ASICs, and CPO could trigger another supply shortage of high-end ABF substrates by 2027
   * AXT Inc surged recently due to intense AI-driven demand for indium phosphide substrates
   * indium phosphide (InP) wafers
* Which raw materials are critical for the AI supply chain?
   * MP Materials Corp. (MP) is the largest producer of rare earth materials in the Western Hemisphere
   * Ucore is strategically positioned to break the Chinese monopoly on heavy rare earth separation, specifically targeting high-premium elements like Terbium and Dysprosium.
   * NioCorp Developments Ltd. (NB) slated to become one of the only domestic producers of niobium, scandium, and titanium.
* What is the AI software stack?
   * Data: Databricks ($4.8B), Snowflake ($4.68B), and MongoDB ($2.46B)
   * TAAS (Token as a service): Together AI, Fireworks, Baseten
   * Public: Tempus AI (TEM), SoundHound AI (SOUN), Evolv Technology (EVLV),  Jabil Inc. (JBL)
* What is a robot made of? How far along is development?
   * What is the supply chain for Unitree, Agility, Apptronik, Figure, Tesla? (robotics)  - Actuator Copper Cooling  LiDAR Camera Gearbox Motor Chinese suppliers to US comps: Sunday Robotics, Dyna, and XDOF.
   * Leaders including 1X, AGIBOT, Agility, Agile Robots, Boston Dynamics, Figure, Hexagon Robotics, Humanoid, Mentee, and NEURA Robotics are building the next generation of humanoids using Cosmos world models, Isaac Sim and Isaac Lab to accelerate the development and validation of their robots. With a global install base exceeding 2 million robots, FANUC, ABB Robotics, Yaskawa, and KUKA are integrating NVIDIA Omniverse libraries and NVIDIA Isaac simulation frameworks into their virtual commissioning solutions.
   * NVDA, TSM, ROK, UBTECH, FANUY, ABB, YASKY, TER, SYM, AMZN, ISGR, SERV, RR, MGA, Foxconn
* What is "Edge AI"?
   * WebAI, FemtoAI, PolarGrid, Aizip Mirai, and OpenInfer, Perceptron
* Is there a domestic supply chain for high-precision mechanical parts?
* Vertical models?
   * Abridge, EliseAI, Evenup, Fieldguide

L2 Semiconductor Equipment & EDA/IP 
ASML: Sole manufacturer of EUV lithography — every advanced AI chip on the planet is physically impossible without it, making it the single most upstream gate   in the entire supply chain.
KLAC: Near-monopoly in process control and yield monitoring — the tools that verify chip quality at every fabrication step, a distinct and independent constraint from lithography.
L3 Foundries & Advanced Packaging
TSMC: The only foundry capable of producing leading-edge AI silicon at scale — N3 utilization on track to exceed 100% in H2 2026, making it the central bottleneck in the entire stack.
AMKR: Primary recipient of TSMC's CoWoS packaging overflow — shows that even if wafer supply were unconstrained, advanced packaging is a separate, independent Chokepoint.
L4 Compute Silicon
NVDA: Dominant GPU platform with CUDA ecosystem lock-in — the whale that sets the pace for every other layer in the stack.
AMD: The only credible GPU challenger, with the $100B Meta deal as the clearest test of whether AI compute wins are NVDA-only or genuinely broadening.
L5 Memory Silicon
HXSCL: HBM technology leader and primary Nvidia supplier — demand for the next three years already exceeds their available supply, making them the memory layer's binding constraint.
MU: Cost-differentiated US-listed HBM player — shows whether the memory boom is concentrated in SK Hynix or whether a second supplier is capturing meaningful Share
L6 Networking & Custom Silicon
AVGO: Google and Meta's primary custom ASIC partner, contracted through 2031 — the clearest window into whether hyperscaler custom silicon is delivering real, durable revenue.
MRVL: AWS and Azure's custom ASIC partner, also building a full optical connectivity platform — shows a second hyperscaler custom silicon program and whether the displacement of NVDA is structural.
L7 Optical & Physical Connectivity
COHR: Vertically integrated optical components supplier with a strategic Nvidia investment — direct validation from the dominant GPU vendor that optical connectivity is a critical dependency.
NOK: Optical networking equipment with +56% YoY optical revenue and the most aggressive upward revision to hyperscaler CapEx estimates of any public vendor — a strong pure-play signal on AI connectivity demand.
L8 Power Generation & Grid
GEV: Gas turbine oligopolist with a $200B backlog stretching past 2029 — the clearest public confirmation that grid-scale power is structurally constrained, not just temporarily tight.
BE: Behind-the-meter fuel cell manufacturer with Oracle (2.8GW) and AEP (1GW) as anchor customers — shows that hyperscalers are paying significant premiums to bypass the grid entirely.
L9 Data Center Infrastructure
VRT: Dominant power and cooling infrastructure provider — liquid cooling has crossed from optional to mandatory for AI-dense deployments, and less than 10% of existing US inventory is compliant. 
EQIX: Carrier-neutral colocation operator with pre-leasing at record levels — the demand-side commitment signal showing hyperscalers are locking up DC capacity well ahead of construction completion.

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



