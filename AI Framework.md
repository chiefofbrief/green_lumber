# AI Framework

## Context

"AI" (machine learning, language models, vision models, accelerators, data centers, power, physical AI, etc.) is the "umbrella" for the majority of our investments. To assist in analyzing these companies, this document houses our assumptions, insights, and predictions related to the broader AI ecosystem. Rather than attempting to map every technical detail or predict the future with 100% accuracy, this framework is designed to be a living document that evolves as we encounter new data.

Growth, and the risks to that growth, drive our investment decisions. Drivers of growth exist at both the company level (individual ability to scale) and the sector level (broader expansion of its sector). This document aids in assessing the latter (sector growth and risks) by analyzing current market drivers, market and product potential, sales and margin vulnerabilities, and projected timelines.

-----------------------------------------

## Context

*ai is a productivity ool.*

"AI" has become the umbrella term for a variety of advances in hardware, software, infrastructure, and applications. By being attached to all four categories at the same time, it lends itself easily to too much optimism or pessimism depending on the framing (e.g., optimistic about new approaches to memory, pessimistic about token cost). The real challenge is to identify where the optimism and pessimism are justified in the near term. 

A focus on the near-term is key since being right on the wrong timeline can be the same as being wrong. As with previous technologies, AI enthusiasts are likely overly optimistic about the capabilities, the timeline for deployment of those capabilities, and people's willingness to change behaviors. In the case of AI, it's not purely enthusiasm but also the fact that the loudest advocates are those building and investing in the infrastructure, incentivizing them to paint an overly optimistic picture. Instead of using the consensus timeline, it's prudent to adopt a more conservative timeline which acknowledges that adoption of technology applications at scale is usually not realized for years (even decades) after the potential is visible.

AI infrastructure and AI applications are not the same thing. If AI follows a similar pattern to previous information technologies, applications (digital or physical) will capture the most value. However, to this point, publicly-traded AI-native applications are almost nonexistent, and private AI-native applications lack strong brand recognition, with the exception of a sprinkling of domain/task-specific models (e.g., Cursor, Lovable, Harvey). This indicates there is still work to be done in the infrastructure layer.

The primary purpose of infrastructure is to lower the cost of deployment for applications, expressed for AI as cost per token. As the infrastructure improves, the cost/token will decrease. As cost/token decreases, running models becomes cheaper, resulting in more models, model usage, and applications. There are two major components of AI infrastructure, both of which are being developed at the same time: Physical infrastructure (hardware, data centers, power, etc.) and Digital infrastructure (models, data, architectures, protocols, etc.). 

Accelerator utilization is the central focus for physical infrastructure. Accelerators are designed to do massive amounts of specialized math simultaneously, requiring sufficient compute (executes the math), fast memory (where weights and state live), and high-speed fabric/interconnects (dictates how far data travels and how fast can it move). Data centers are the facilities that house accelerators; energy is what provides the electricity to run them. Reliable sources of power and thermal management (to keep accelerators from overheating) are needed to maximize utilization. 

*accelerator utlization, model architectures. if gpu proces dont decrease then spftwsre is rhe lever* Autonomous systems are the central focus for digital infrastructure. These systems could perform specific tasks, or perform a variety of tasks within a specific domain. Deployment at scale requires creating infrastructure for probabilistic (not deterministic) systems that are free to execute actions within user constraints. It also requires providing the necessary context to expand beyond general capabilities and chat-based reasoning: Domain-specific data, data traces (the thought that went into an output), and 'persistent' memory (history, preferences, etc.) are needed to expand beyond foundation models. 

Infrastructure needs and constraints shift over time. Oversupply leads to price competition (and lower margins). Satisfying demand for one component can expose a shortage in another. Changes in how applications serve customers (e.g., a shift from chat-based interfaces to background processes) change which pieces matter the most. Novel solutions can make existing constraints obsolete. Therefore, it's best to assess the current needs without assuming they will exist indefinitely, while hedging against scenarios in which they disappear unexpectedly. The most practical way to mitigate risk is to invest in the strongest providers in the fastest growing sub-sectors (which are ideally also one of the low-cost producers).

## Landscape

To identify what actually matters in the near term, it helps to work backward from a likely future state (roughly 5 years from today). It's impossible to predict what will happen, and there are many things that can happen simultaneously. Therefore, this section acts more like a list of likely possibilities rather than an exact mapping. It may be the case that AI adoption is underwhelming or significantly delayed (perhaps due to its probabilistic nature in a deterministic world), but for this exercise the focus is on what needs to happen for adoption at scale. 

The promise of AI is autonomy, the idea that machines can perform a variety of actions with limited (or zero) human input. Whether this will come to fruition is uncertain, but the building blocks towards autonomy will likely be the focus of AI enthusiasts. These building blocks will be spread across Applications, Digital infrastructure, and Physical infrastructure. 

*'Incumbents' (pre-2023 companies) are providing/building the majority of the infrastructure, and that is unlikely to change in the near-term.  However, because of the amount of investment, even minor efficiency improvements can have a huge impact, attracting new ideas and companies. It's likely that in the near-term the established vendors do most of the work, in the near to medium-term new entrants steal some market share, and in the long-term prices drop and everyone gets hurt (until the cycle resets).*

*The main focus area of AI infrastructure investments at the moment is inference. Inference is when a model applies its training to produce output (often in real time) in two stages, prefill (processing the initial prompt) and decode (generating the response token by token). The decoding phase is the constraint as it's severely limited by memory bandwidth (the speed data is fetched). There are multiple levers in digital and physical infrastructure that are used to alleviate the issue. Solar panels are getting cheaper, but the other costs involved with them (land, labor, transmission, etc.) are not, and the lack of transmission lines is maybe the biggest problem.*

### Applications

An AI-native application is a user-facing product that uses AI as its central reasoning engine. Initial applications will reinvent existing activities for autonomous systems, in the same way that existing activities were re-imagined for the internet's distribution architecture. Models are already making a significant impact on digital activities including content generation (text/image/video), web search, web/app design, and coding. E-commerce is just a matter of time. Existing physical activities using AI include driving, product design, manufacturing, and warehouse operations. 

In order for an autonomous system to choose the right action and execute it properly, persistent, task-specific context is critical. It makes little sense for every company and individual to provide this context in isolation. Domain and/or task-specific applications will fill this gap; these may be domain/task-specific models, or applications that augment foundation models with task-specific data. Providers of this context could develop their own applications or be part of the digital infrastructure. Persistent context may also require adjustments to cloud infrastructure, which was built for stateless execution.

While foundation models are currently in the spotlight, the conversation has already shifted to the open-source vs. closed debate, which is really a conversation about cost and privacy. The conversation will eventually shift to domain/task-specific models, which provide a higher ROI.

**Good vertical models (aka domain-specific) start with a well-defined workflow, enable superhuman capabilities, and have an immediate ROI.** 
* Well-defined, repeatable workflows (low ambiguity).
* AI enables superhuman capabilities (e.g., 24/7 work, 100X more data analysis, pattern recognition).
* Start with one worfklow, then expand it others after bulding trust. The entry point should have immediate ROI.

**The applications with the biggest upside may be in physical AI, but the timeline and initial use cases are uncertain. There is a lot of excitement around robotics since the barrier to training has been lowered by language and vision models, but these models are more likely to initially serve as the 'brain' for existing infrastructure. World models are key to unlocking a variety of use cases, and as with software, domain/task-specific models are the likely end state.**    
* Physical AI is simply AI that understands and interacts with the laws of physics and the physical world. A world model is an AI that understands the laws of physics; instead of predicting the next word in a sentence, it predicts the next frame of a video.
* LLMs acts as the brain that reasons through what needs to be done, and vision models translate the text-based logic into physical, mechanical execution.
* A foundation model for robots means they can pick up a new task with limited training instead of being built for specific tasks. However, the ROI may be higher for robots trained on specific environments.  
* Instead of getting all the data prior to deployment, machines just need to get good enough that they can be deployed and gather data to improve. Domains where collecting data is easy will have better physical AI even if they are physically challenging.

The applications with the biggest upside may be in physical AI, but the timeline and initial use cases are uncertain. There is a lot of excitement around robotics since the barrier to training has been lowered by language and vision models, but within the next five years its more likely that 1) These models serve as the 'brain' for existing machines and 2) New machines are deployed into existing enterprise applications (e.g., manufacturing) rather than into brand new applications. World models, and possible foundation models for robotics, are key to unlocking a variety of use cases. 

### Digital infrastructure

Digital infrastructure is adapting, and will continue to adapt, to enable these applications. The focus on improving the performance of existing models will remain; adjustments to model architectures, model training methods, and improved accelerator utilization provide the most leverage. A transition from the transformer architecture, or a significant adjustment to it, could open up entirely new possibilities. Existing accelerators are not being run at 100% utilization, and with increasing supply, its likely that there will be both underutilization of existing accelerators and excess compute capacity which can be resold. 

Autonomous systems need infrastructure for executing actions. For digital applications, actions may include browsing websites, connecting to tools, communicating with other autonomous systems, registering for services, making purchases, etc. Existing products and services (websites, software, payment providers, etc.) will adapt to be more friendly to these systems. Digital infrastructure needs to enable autonomy. Model routing will allow systems to choose the most effective model for a given task. Runtime infrastructure, including the cloud, will adjust to the inference needs of models and their probabilistic nature. Websites will incorporate agent-centric designs. New payment methods will allow systems to execute transactions. Existing infrastructure was built for deterministic systems, but generative AI is probabilistic. Assuming models retain their probabilistic nature, observability (monitoring what is being done) and governance (controlling what can be done) will continue to be critical. Given that cloud infrastructure was built for deterministic execution, new runtime infrastructure and approaches to cloud inference may be areas of focus. 

The near-term value in digital infrastructure are solutions that enable autonomous, probabilistic systems to perform specific tasks, or a variety of tasks within a specific domain. The current focus is on the subset of autonomous systems called 'agents.' Domain-specific data is necessary to expand beyond general models; potential sources include end customers (e.g., a law firm providing its data), third-party model trainers (e.g., Mercor), and vertical SAAS companies (e.g., Tyler, Agilsys). Data 'traces' (the thought that went into an output) are also necessary given that AI has only distilled the end state of human thought by being trained on internet data. New approaches to runtime infrastructure are also needed as cloud infrastructure was built for stateless, deterministic execution; AI requires stateful (retaining context), probabilistic execution (varying outcomes). Solutions for agents are mainly focused on observability (monitoring what is being done with agents) and governance (controlling what can be done with agents) for enterprises. But for autonomous systems to reach their potential, better infrastructure is needed and is currently being built (e.g., A2A for communication between agents, x402 for agentic payments).

This may be especially true for AI, where better software programming leads to improved hardware utilization. 

Existing SAAS companies that provide agentic infrastructure are well-positioned (assuming the push for agentic workflows continues). The main question is 'do they get more usage in an agentic world?'


### Physical infrastructure

physical infea. chips. power. cooling. robots. vision, audio, sensors. For physical applications, actions may include movement, vision, spatial awareness, dexterity, communicating with other autonomous systems, etc. The amount of investment in physical infrastructure invites novel solutions. The biggest point of leverage is accelerators; new designs that better balance memory and compute, as well as speed and throughput, will alleviate or eliminate some of the current constraints and workarounds. However, while this is certain to happen at some point, whether these new designs are commercially viable in the next 5 years is uncertain. Assuming that chip innovation takes longer than five years, hybrid chip combinations (ASICs, GPUs, TPUs), liquid cooling, and optical networking will be standard for data centers.  

Data centers need electricity. The only reliable source of electricity at the moment is natural gas. There may be a deficit of natural gas starting in 2028, not necessarily because there isn't enough gas under the ground, but rather because of a lack of infrastructure for cost-effective deployment (processing, gathering, and transmission are constraints). To meet demand, other sources of power may be expedited, including advanced geothermal, solar, batteries, and nuclear, although nuclear is not a five-year solution, and the others may not be either. Solar panels and batteries are getting cheaper, but the other costs involved with them are not. There are only so many existing nuclear plants, and new plants take time to build (not to mention that new nuclear technologies lack reliability). Advanced geothermal may be the wildcard solution given how it sits in the middle of natural gas, solar, and nuclear; it runs 24/7, leverages existing oil and gas drilling equipment, and has zero emissions. 

-----------------------------------------
-----------------------------------------

The near-term value in physical infrastructure exists in workarounds for bottlenecks, particularly accelerator utilization. Physical infrastructure can be decomposed into three categories: Accelerators (the chips doing the operations), data centers (the facilities that house chips), and energy (the power needed for the facilities). Accelerators have three primary levers: Compute (what executes the math?), memory (where do weights and state live?), and fabric (how far must data travel and how fast can it move?). Designing and deploying a new chip is a major investment, and it's likely that data centers will include a variety of accelerators (GPUs, TPUs, ASICs) to meet a variety of use cases, so investing in new chip designs is not a near-term play. Data centers and energy are where approaches to improve accelerator utilization, without having to design new chips, can be implemented.

Investing in infrastructure carries four major risks: 1) Oversupply, leading to price competition (and lower margins) among providers; 2) A decrease in investment and purchase orders; 3) Changes in how application providers serve the technology to their customers; 4) Novel solutions that make existing constraints/solutions obsolete. In the near-term, oversupply is the most pressing risk, followed by decreasing capex. In the long-term, novel solutions and changes in delivery are the biggest risks; however, in the near-term, they should be monitored rather than driving investment decisions. 

A decrease in investment would be the result of one or more hyperscalers pulling back spending, with a likely catalyst being shareholder pressure to increase FCF (in the form of a depressed stock price) since hyperscalers have moved down the capital curve from FCF to debt to equity to fund investments.

## Insights

**Throughout human history, retail, advertising, content, and infrastructure have been extremely lucrative. This has been/will be the same for AI.**
* Retail: Selling things.
* Advertising: Helping people advertise what they're selling.
* Content: Providing information or entertainment.
* Infrastructure: Supports the other components. 

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

