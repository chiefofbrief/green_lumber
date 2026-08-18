# Sector Analyses


## Key Sectors Analysis (based on screener output)

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

--------------

## AI Infrastructure

**S-Curves**:
* **Hardware**: Mid-Late acceleration - Hardware has been decommoditized (innovation matters). But more data/compute is leading to lower marginal returns. 
* **Energy**: ?...Maybe the same, maybe not.

**There is a shortage of energy which must be solved to reduce token costs**
* Models translate compute into intelligence, and they need energy to do that; and the less energy, the more expensive the tokens.

**Inputs into world models (e.g., sensors) may be critical for physical AI**

**The US will invest in infrastructure for physical AI**
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

--------------

