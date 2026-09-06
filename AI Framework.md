# AI Framework

## Context

**Purpose of this document**: 
"AI" (machine learning, language models, vision models, accelerators, data centers, power, physical AI, etc.) is the "umbrella" for the majority of our investments. To assist in analyzing these companies, this document houses our assumptions, insights, and predictions related to the broader AI ecosystem. 

Rather than attempting to map every technical detail or predict the future with 100% accuracy, this framework is designed to be a living document. It will evolve as we encounter new data. The goal is to build an antifragile mental model of the AI landscape: specific enough to drive actionable decisions, yet flexible enough to adapt quickly when our assumptions are challenged. 

**How to use this document**:
Growth and risk drive our investment decisions. While both are critical, a company must demonstrate strong growth potential to even be considered. Growth has two main drivers: a company's individual ability to scale, and the broader expansion of its sector. Risk similarly exists at both the company and sector levels. This document estimates sector growth and risk by analyzing current market drivers, market and product potential, sales and margin vulnerabilities, and projected timelines.  

-----------------------------------------

## Insights

**Throughout human history, retail, advertising, content, and infrastructure have been extremely lucrative. This has been/will be the same for AI.**
* Retail: Helping people sell things.
* Advertising: Helping people advertise what they're selling.
* Content: Helping people find information or entertainment.
* Infrastructure: Supports the other components. 

**AI models are powerful applications. But as with all technologies, enthusiasts are overly optimistic about their future capabilities, the timeline for deployment of those capabilities, and people's willingness to change existing behaviors. Things will likely progress more slowly than optimistic estimates.** 

**AI infrastructure and AI applications are not the same thing. The majority of value will ultimately accrue at the application layer, but we are in the infrastructure buildout phase, during which the primary goal is to lower the cost of deploying applications. Many investors conflate the two, which is why they are overly optimistic/pessimistic about AI capex.** 

**There will be overinvestment in AI infrastructure, lowering the cost for application providers but leading to price competition (and lower margins) among infrastructure providers, which strongly favors low-cost producers. The timeline for oversupply is uncertain, but it's likely longer than the mainstream assumption and can be approximated as slowing equipment orders (at least for physical infrastructure).** 

**It's possible that investment in AI infrastructure temporarily stalls. A sustained lack of FCF (along with depressed stock prices) for hyperscalers is a likely cause. Slowing equipment orders may be an early signal.** 
* Hyperscalers have moved down the capital curve from FCF to debt to equity; if they do not revert to FCF, investors may punish them.

**There are two primary components of AI infrastructure, both of which are being developed at the same time: Physical infrastructure (hardware, data centers, power, etc.) and Digital infrastructure (models, data, architectures, protocols, etc.). Both are critical for cost-effective deployment of AI applications at scale.**  

**The hot areas within physical infrastructure are split between the chips themselves (accelerators) and the facilities that house them (data centers). Compute (what executes the math?), memory (where do weights and state live?), and fabric (how far must data travel and how fast can it move?) are the three primary levers for accelerators. Powering accelerators and keeping their utilization high requires a reliable source of electricity and thermal management.** 
* Accelerators are designed to do massive amounts of specialized math simultaneously. This requires sufficient compute, fast memory, and high-speed interconnects that link chips. 
* Data centers take in electricity and output heat.
  * The U.S. electrical grid was not built for the sudden load growth driven by AI, and securing electricity is so difficult that developers are increasingly bypassing the public grid entirely.
  * As electricity is converted into heat, cooling must scale with compute. Standard air conditioning systems can no longer physically move air fast enough to dissipate the heat, pushing the focus to advanced thermal management, with liquid cooling (D2C, immersion, RDHx) as the leading solution. 

**Natural gas is currently the only reliable source of electricity. There may be a deficit of natural gas starting in 2028, not necessarily because there isn't enough gas under the ground, but rather because of a lack of infrastructure for cost-effective deployment. Advanced geothermal is the wildcard solution.** 
* Processing is the first major constraint. Gathering is another constraint.
* While solar, batteries, and nuclear may be options in the future, they are currently constrained.
  * Solar panels are getting cheaper, but the other costs involved with them (land, labor, transmission, etc.) are not, and the lack of transmission lines is maybe the biggest problem.
  * Batteries are getting cheaper, but other costs involved with them (e.g., lithium) are not.
  * Nuclear is a long-term play; there are only so many existing plants, new plants take time to build, and new nuclear technologies are not proven.
* Advanced geothermal sits in the middle of natural gas, solar, and nuclear (runs 24/7, leverages existing oil and gas drilling equipment, zero emissions).

**The hot areas within digital infrastructure are data, models, runtime infrastructure, and autonomous systems (primarily 'agents'). Autonomous systems leveraging domain/task-specific models is a likely end state; domain-specific data, data 'traces' (the thought that went into an output), and infrastructure for autonomous systems are necessary to make it possible.** 
* Domain-specific data is necessary to expand beyond general models. Potential sources include end customers (e.g., a law firm providing its data), third-party model trainers (e.g., Mercor), and vertical SAAS companies (e.g., Tyler, Agilsys).
* AI has only distilled the end state of human thought by being trained on internet data.
* Cloud infrastructure was built for stateless, deterministic execution. AI requires stateful (retaining context), probabilistic execution (varying outcomes).  
* Solutions for agents are mainly focused on observability (monitoring what is being done with agents) and governance (controlling what can be done with agents) for enterprises. But for autonomous systems to reach their potential, better infrastructure is needed and is currently being built (e.g., A2A for communication between agents, x402 for agentic payments).

**While foundation models are currently in the spotlight, the conversation has already shifted to the open-source vs. closed debate, which is really a conversation about cost and privacy. The conversation will eventually shift to domain/task-specific models, which provide a higher ROI.**  
   * Unlike the internet, there is a real marginal cost per customer. But most investors don't realize that open-source models are not free and still have a marginal cost for inference.
   * Historically, data plus compute has outperformed encoding knowledge (e.g., Alphago). Vertical models would need to buck this trend, and proprietary data/user interaction data may be the key.

**'Incumbents' (pre-2023 companies) are providing/building the majority of the infrastructure, and that is unlikely to change in the near-term.  However, because of the amount of investment, even minor efficiency improvements can have a huge impact, attracting new ideas and companies. It's likely that in the near-term the established vendors do most of the work, in the near to medium-term new entrants steal some market share, and in the long-term prices drop and everyone gets hurt (until the cycle resets).**  
* Existing SAAS companies that provide agentic infrastructure are well-positioned (assuming the push for agentic workflows continues). The main question is 'do they get more usage in an agentic world?'
* Vertical SAAS companies have data for domain-specific models. 
* The extent of the US onshoring manufacturing to compete with China is likely overrated.
* In the near-term there is enough demand to support 'all' vendors, but this will eventually change. 

**As the infrastructure improves, the cost/token will decrease. As cost/token decreases, running models becomes cheaper, resulting in more models, model usage, and applications.** 

**Good vertical models (aka domain-specific) start with a well-defined workflow, enable superhuman capabilities, and have an immediate ROI.** 
* Well-defined, repeatable workflows (low ambiguity).
* AI enables superhuman capabilities (e.g., 24/7 work, 100X more data analysis, pattern recognition).
* Start with one worfklow, then expand it others after bulding trust. The entry point should have immediate ROI.

**The applications with the biggest upside may be in physical AI, but the timeline and initial use cases are uncertain. There is a lot of excitement around robotics since the barrier to training has been lowered by language and vision models, but these models are more likely to initially serve as the 'brain' for existing infrastructure. World models are key to unlocking a variety of use cases, and as with software, domain/task-specific models are the likely end state.**    
* Physical AI is simply AI that understands and interacts with the laws of physics and the physical world. A world model is an AI that understands the laws of physics; instead of predicting the next word in a sentence, it predicts the next frame of a video.
* LLMs acts as the brain that reasons through what needs to be done, and vision models translate the text-based logic into physical, mechanical execution.
* A foundation model for robots means they can pick up a new task with limited training instead of being built for specific tasks. However, the ROI may be higher for robots trained on specific environments.  
* Instead of getting all the data prior to deployment, machines just need to get good enough that they can be deployed and gather data to improve. Domains where collecting data is easy will have better physical AI even if they are physically challenging.

---------------------------



-----------------------

