# Research

## Stocks

* TBBB
* APP
* LPG
* FICO
* ADI
* GPOR
* EXE

## Sectors

* How diversified are cloud sales for AWS/Azure?
* How diversified are GPU sales for Nvidia?
* Will custom ASICs take a meaningful chunk of market share away from Nvidia's GPUs?
   * What is the difference between a GPU and a custom ASIC?
   * AVGO, GUC, Wiwynn (wiwynn suppliers: TE connectivity, mpley, foci, browave, senko, afl)
* Is at least a portion of TSM's sales guaranteed?
* Are token costs decreasing?
* How could decreasing token costs impact the need for compute, chips, etc.?
* How does the usage of Chinese models compare to US models?
   * What is the leading Chinese model?
* Do we really need more compute?
* Do we really need more data centers?
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
 

------------

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
