# Sector Analyses

## Topics to Explore

* What happens when companies stop using expensive models?
* How important are custom chips?
* Liquid cooling.
* Networking: Selectics, Elite Materials. 
* Fiber (instead of copper): Corning.
* Energy: Advanced Energy, Delta.
* Vertical models: Abridge, EliseAI, Evenup, Fieldguide
* TAAS (Token as a service): Together, Fireworks, Baseten.
* Together AI - Open-source model recently raised $800M.
* Memory: Hanmi, PSMC
* Optics: Mediatek, Cargan, Aoet
* ASIC: Guc, Wiwynn (wiwynn suppliers: TE connectivity, mpley, foci, browave, senko, afl)


## AI 

**Principles**
* The most value will accrue at the application layer.
     * Industries become more framgmented over time. Domain/task-specific models ('vertical' models) will eclipse the foundation models, but it'll take time.
     * AI-native startups will prefer lower-cost base models over expensive foundation models. Growth at all costs is tricky since there is a real marginal cost per customer.  
* AI and chips/memory/power are not the same thing.
      * Everything besides applications will be 'commoditized,' although infrastructure is currently an area of innovation.
* Increased profits in one layer hurts the profits of downstream layers (e.g., memory prices up, Nvidia/AMD profits down; foundation model profits up, software profits down).
* With abundant supply, everyone competes on price. This transforms high margins into low margins, favoring low-cost producers. 
* AI bulls are betting on a sustained acceleration in demand.
     * The amount of 'organic' demand/sales is hard to determine due to a lot of circular financing and sales.
     * Even assuming there is healthy demand, customer concentration is very high.
     * If demand decelerates, hyperscalers can use FCF to subsidize capex, but margins, ROIC, and growth decrease, which will compress multiples. 

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

**Application Overview**:
* Finetuning:
     * Data quality is the most important thing. Data diversity is also important.
     * Training is easier on a dataset with a clear right/wrong answer. 
     * During model training, you add data, calculate the loss (difference between the the desired and actual response), and update the weights. There are two training phases: Pretraining (create a base model using as much knowledge as possible), and posttraining (smaller, more custom datasets).
     * After model training comes evaluation.
     * A larger model's capabilities can be distilled into a smaller model.
  *  Historically, data plus compute has outperformed encoding knowledge (e.g., Alphago). Vertical models would need to buck this trend, and user interaction data may be the key.
  *  Alternative models are already being used - Cursor used RL on Kimi for its model. 

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
 
   



