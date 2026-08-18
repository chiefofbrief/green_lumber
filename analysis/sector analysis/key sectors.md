# Sector Analyses


## Key Sectors

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

## AI 

**Principles**
* The most value will accrue at the application layer.
     * Industries become more framgmented over time. Domain/task-specific models ('vertical' models) will eclipse the foundation models, but it'll take time.
     * AI-native startups will prefer lower-cost base models over expensive foundation models. Growth at all costs is tricky since there is a real marginal cost per customer.  
* AI and chips/memory/power are not the same thing.
      * Everything besides applications will be 'commoditized,' although infrastructure is currently an area of innovation.
* Increased profits in one layer hurts the profits of downstream layers (e.g., memory prices up, Nvidia/AMD profits down; foundation model profits up, software profits down). If a company is making bank because their AI tools are tremendous, and their revenues are surging…it means that other companies are paying for that product.
* With abundant supply, everyone competes on price. This transforms high margins into low margins, favoring low-cost producers. 
* AI bulls are betting on a sustained acceleration in demand.
     * The amount of 'organic' demand/sales is hard to determine due to a lot of circular financing and sales.
     * Even assuming there is healthy demand, customer concentration is very high.
     * If demand decelerates, hyperscalers can use FCF to subsidize capex, but margins, ROIC, and growth decrease, which will compress multiples.
* LLMs are SAAS. AI may expand the software market.
* Companies would rather pay someone to manage software, and that won’t change. 

**S-Curves**:
* **AI infrastructure**: Mid-Late acceleration - Hardware is being decommoditized (innovation matters). But more data/compute is leading to lower marginal returns. 
* **AI applications - Software**: Early-mid acceleration - With the exception of foundation models there are no household names.  
* **AI applications - Physical (edge, robotics, etc.)**: Experimentation-early acceleration - Barriers to deployment/adoption are being removed.

**Infrastructure Overview**:
* Hardware is currently decommoditized thanks to AI (but will become a commodity again).
* How models and usage evolve will have a big impact on the fate of infrastructure providers. There may not be oversupply yet, but there probably will be in some areas at least. 
     * More customization (e.g., ASICs) may decrease demand for out of the box solutions (e.g., Nvidia GPUs). 
     * Longer conversations need more memory. But if models get smaller (fewer parameters), less memory may be needed.
     * CPUs are critical for agents. But if agent usage is overhyped, CPUs are too.  
* A large part of 'demand' is hyperscaler capex, which is already slowing (based on the derivative of the growth rate).
     * To this point, hyperscaler capex has been like a performative auction. When frugality becomes the status symbol instead, this may become a big problem.
* As cash flow becomes exhausted, more companies may be taking on debt to pay for capex. If demand decelerates, this could be a big problem.
* World Models use sensors, video, GPS, etc. to provide synthetic training environments, reducing the data bottleneck for robotics training.
* Data is the necessary context agents need in order to act. As models become commodities, context becomes more important (data, access, logs, etc.).
* Building an AI factory requires electricians, pipefitters, welders, ironworkers, HVAC technicians, and networking and computer specialists. This buildout extends far beyond the data center. It spans semiconductor fabs, advanced packaging facilities, server and supercomputer assembly, power generation, transmission lines, substations, and the vast upstream supply chains and downstream services.
* By leasing compute capacity from neoclouds, hyperscalers shift their cost timeline from being a large upfront capex outflow to an operational expense outflow spread over long-term contracts
* Within the AI investment theme, there is nowhere that the supply chain shifts faster than in networking
* semiconductor market revenue is highly concentrated, and value extraction is even more so
* Past a certain threshold of intelligence, developers prefer faster tokens to smarter tokens.
* Data centers can take over 4 years from land purchase to datacenter delivery. Power and permits are necessary before they can even be taken seriously. 

**Application Overview**:
* Finetuning:
     * Data quality is the most important thing. Data diversity is also important.
     * Training is easier on a dataset with a clear right/wrong answer. 
     * During model training, you add data, calculate the loss (difference between the the desired and actual response), and update the weights. There are two training phases: Pretraining (create a base model using as much knowledge as possible), and posttraining (smaller, more custom datasets).
     * After model training comes evaluation.
     * A larger model's capabilities can be distilled into a smaller model.
  *  Historically, data plus compute has outperformed encoding knowledge (e.g., Alphago). Vertical models would need to buck this trend, and user interaction data may be the key.
  *  Alternative models are already being used - Cursor used RL on Kimi for its model.
  *  Vertical AI = Vertical SAAS (SAAS —> AI)
  *  Robots need a higher level of reliability to deploy than software (LLMs). Robots are better for high frequency, low consequence tasks within a constrained space.
  *  China has a huge advantage in robotics —> US companies rely on China for supplies —> US government/VCs will invest a lot in a US supply chain to catch up and decrease dependency.
  *  As coding becomes easier, the non-code stuff (expertise, relationships) become more important, especially since the output is probabilistic and you need someone to complain to/about when it doesn’t work
  *  The workflow you ship on day one is not the moat. The loop that production usage creates over time is.
  *  Cheaper to build software is probably cheaper to buy, resulting in more customers. 

**Critical players in each S-curve**:  
* **AI infrastructure**:
    * All roads lead to TSMC.
    * Chips: Nvidia, TSMC, ASML, KLAC.
         * Custom chips - Broadcom, Google, Amazon, Microsoft, but unsure if they are critical.
         * Memory - Micron, SK Hynix. Custom HBM is a thing (Marvell, Nvidia).  
    * Power - GEV, Bloom Energy. 
    * Cloud - ? Maybe Coreweave, Nebius, but not sure if they are critical. Maybe Google/Amazon/Microsoft. 
* **AI applications - Software**: Google, Nvidia, TSMC, ASML.
     * Foundation models: Google, Anthropic, OpenAI.
     * Data:
     * Domain models: 
*  **AI applications - Physical**:
      * Foundation models: Nvidia
      * Data: 
      * Robotics:
      * Edge:

**Good vertical models**:
* Well-defined, repeatable workflows (low ambiguity).
* AI enables superhuman capabilities (e.g., 24/7 work, 100X more data analysis, pattern recognition).
* Start with one worfklow, then expand it others after bulding trust. The entry point should have immediate ROI. 
 
**Evaluating legacy software as AI applications**:
   * What % of sales are AI (and rate of change)?
   * What is the market share (and rate of change)?
   * Software can be AI apps, but there is a strong bear case:
        * Easier to make software now.
        * Per-seat/licensing model is shifting to tokens, which narrows margins.
        * The sales process was designed around seat-based, not token-based, pricing.
    * Vertical saas companies are older than horizontal ones (so they might be less fragile). Examples: FICO, Tyler, Agilsys. They provide the domain-specific data that AI needs to expand beyond general models
    * Public software companies that are agentic infra (APIs, databases, data) are being celebrated (prices going up).The focus seems to be: will a company’s existing product and monetization will thrive in a world where agents are doing more and more work?
        * Does it have the kind of dataset a foundation model or new entrant couldn’t reconstruct in 12 months? Is the data proprietary?
        * Does its product get more usage in an agentic world? (e.g., more usage, more API calls, etc.)
        * Is it deeply embedded in customers’ operations?
        * Does it have the engineering team, R&D investment, and leadership DNA to build real AI capabilities — not just bolt on a chatbot
        * Is the domain complex? (how regulated, specialized, or expert-dependent)


 
   


