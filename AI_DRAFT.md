
## The Basics of Investing in New Technology

### It's all About Growth

Expected sales growth, and the risks to that growth, dictate a company's stock price. New technology provides the potential for abnormal sales growth, and therefore, the potential for extreme stock price increases.

Technology expands sectors, not just companies. If there is sufficient demand, "all" companies in a sub-sector may benefit temporarily. Start by identifying which sub-sectors will experience the most rapid growth. Good starting points are recent sales growth and constraints to adoption.

Next, identify the companies within the high-growth sub-sectors which are best positioned to benefit from that growth. The strongest companies (low costs, healthy financials, strong brands) are a good starting point. 

### Prioritize Applications, Buy Infrastructure in the Meantime

New technology can be broken into two major sub-sectors, Applications and Infrastructure. The vast majority of value ultimately accrues at the application layer, which is ultimately where investments should be concentrated.  

Applications initially get more traction by reinventing existing activities rather than inventing new ones. For example, e-commerce reinvented mail-order catalogs, and LLMs are a substitute for web search. Start with novel approaches to existing activities. Once the technology is well-established, entirely new behaviors gain traction and become investable.   

The primary purpose of infrastructure is to lower the cost of deployment for applications. The companies benefit while they are solving a constraint to deployment, but eventually become commodities as constraints shift. Oversupply (leading to price competition), changes in how applications serve customers, and novel solutions can all shift constraints. The strongest companies (low costs, healthy financials, strong brands) are a good starting point as they are best able to withstand oversupply, but even they can experience huge price decreases.  

### Be Early, but not Too Early

Being right on the wrong timeline can be similar to being wrong. A balance must be struck between being early enough to enjoy growth while not being so early that a return is not available for years. The ideal investment experiences sales growth in the near-term, which is about 2 years. 

However, the worst possible scenario is being late, so the absolute likelihood of sales growth, regardless of timeline, is the starting point. Among sub-sectors and companies where growth is relatively certain, prioritize by the likelihood of that growth appearing in the near-term.   

Be conservative when estimating the timeline for adoption. It's easy to make the mistake of being too early in new technology. Adoption of applications at scale is usually not realized until well after the potential is visible. The infrastructure takes time to build, and people's behaviors need time to adapt. 

-----------------

## The Basics of AI

### Productivity is the Value Proposition

In its current form, AI is a productivity tool; it provides a better ratio of outputs to inputs. 

This can mean fewer inputs, more outputs, and/or higher-quality outputs. 

### Autonomy is the Goal

At the extreme end of the productivity spectrum are autonomous systems that perform a variety of actions with limited (or zero) human input. The building blocks towards autonomy will likely be the focus of AI development.

### Context and Compute are the Fuel

Compute is the processing power that lets AI models learn patterns and generate outputs.

Context is everything a model learns from and works with, including data, state, and memory. 

### Training and Inference are the Two Jobs

Training is the process of building a model: compute is applied to data so the model learns patterns. Inference is using the trained model to generate outputs.

Training happens before a model is deployed. Inference happens every time it is used.

Inference has two stages: prefill (processing the initial prompt) and decode (generating the response token by token). Decode is typically the constraint because it is limited by memory bandwidth, the speed at which data can be fetched.

### Accelerators are the Critical Piece of Hardware

Accelerators, such as GPUs and custom ASICs (e.g., TPUs), perform the computations. They also store context in memory.

Accelerators are designed to do massive amounts of specialized math simultaneously, which requires three things working together: processing cores (execute the math), fast memory (where weights and state live), and high-speed fabric/interconnects (dictate how far data travels and how fast it can move). 

Programming determines how well those pieces are used. Accelerators don't reach their full capacity out of the box; they need a software stack (kernels, compilers, serving frameworks) to approach their theoretical throughput.

### Data Centers are Where Accelerators Live

Data centers are the facilities that house accelerators. Accelerators, racks, networking, cooling, and power must all work together to keep accelerators fully utilized.

Power (electricity) keeps accelerators running. Cooling removes the heat accelerators produce. Networking connects accelerators to each other so they can share data fast enough to work as one system.

### Model Architectures are the Critical Piece of Software

Architecture is the design that determines how much compute and memory a model needs. The transformer is the basis for today's foundation models.

A new base architecture could change things drastically. Until then, efficiency comes from modifying the transformer to use less compute and less memory, and from hybrids that blend in alternative designs. MoE is one example, activating only part of the model for each token.

### Data is Necessary to Expand Beyond Foundation Models

General models need domain-specific data and data "traces" (the thought that went into human output) to go beyond what the internet provides. The likely sources are the holders of that work: end customers, specialized data providers, and vertical software companies.

Data for physical AI is more limited since there is no equivalent to internet data. Approaches such as world models, video, and simulation are being used, but the most likely source of substantial data is the robots themselves during deployment.

### Infrastructure and Applications are Both Digital and Physical

AI infrastructure has two components. Physical infrastructure is the hardware: accelerators, racks, networking, power, and cooling. Digital infrastructure is the software and context: models, architectures, data, and protocols.

AI applications split the same way. Digital AI works with information, such as text, images, and video. Physical AI understands and interacts with the physical world, as in robots, autonomous vehicles, and industrial systems.

### Digital Infrastructure Needs to Adapt to Autonomous Software

Most software is stateless: each request is handled independently, with no memory of prior requests, which makes it easy to scale up or down on demand ("elastic"). Autonomous systems are stateful: they retain information between requests, and requests must be routed back to the infrastructure that holds their state.  

Autonomous systems have to act on a world built for humans, so new protocols are needed for them to communicate with each other, execute transactions, and more (e.g., A2A for agent-to-agent communication). At the same time, the human-facing world adapts to non-human actors, with websites, software, and payment providers becoming operable by systems as well as people. 

### Inference Makes AI Costs Variable

Traditional software costs almost nothing to serve to one more user. AI applications pay for inference (priced in tokens) every time they are used, so their costs scale with usage and their margins depend on what inference costs.


-------------------------

## The Current Landscape of AI

### "AI" Is Too Broad to Have One View On

"AI" is an umbrella term for advances in hardware, software, infrastructure, and applications. Because it covers all of them at once, it invites too much optimism or pessimism depending on the framing (e.g., optimistic about agents, pessimistic about memory limitations).

### The Focus Is Shifting from the Best Model to the Right Model

AI is currently synonymous with models, and within models, with LLMs, foundation models, and frontier models. 

But there are other types of models, including image, video, vision, vision-action, and world models. Even within a single type, models vary in size, context, cost, and where they can run. 

That variety is why the focus is shifting. Users are looking for a better mix of capability, cost, and privacy rather than defaulting to the frontier. The open-source vs. closed debate is one version of that search. Local models, which run on a user's own hardware, are another, and enterprises building their own domain-specific models are a third.

### Agents Are Autonomy in Practice, and Digital Infrastructure Is Being Built Around Them

Autonomy is the goal, and agents are how it is showing up in practice today. Where a chatbot answers, an agent acts: it carries context across a long task, uses tools, and makes decisions along the way.

Much of the current work on digital infrastructure is aimed at making agents workable. New protocols are emerging to let agents do what they couldn't natively, such as communicate with each other and execute transactions (e.g., A2A for agent-to-agent communication, x402 for agentic payments). Observability (monitoring what agents are doing) and governance (controlling what they can do) are becoming critical as agents are given more autonomy.

### Task-Specific Data Is Valuable

For an autonomous system to choose the right action and execute it properly, it needs persistent, task-specific context. 

General models have already absorbed most of what the internet offers, so the data that is scarce now is the domain-specific data and traces held by the people who do the work. Potential sources include end customers (e.g., a law firm providing its data and thought process), third-party model trainers and data providers (e.g., Mercor), and vertical SaaS companies (e.g., Tyler, Agilysys).

### Every Physical Constraint Shows Up as an Idle Accelerator

Accelerators are the most expensive part of the stack, so physical infrastructure is currently organized around keeping them busy. Memory bandwidth leaves cores waiting on data, weak networking leaves chips waiting on each other, heat forces throttling, and missing power leaves chips unused. Most deployed accelerators, including Nvidia GPUs, run below 100% utilization in practice.

### Inference Is Constrained by Memory Bandwidth








### physical infra is focused on accelerator utlilization

Accelerator utilization is the central focus for physical infrastructure. 

The biggest point of leverage, though, is accelerators; new designs that better balance memory and compute, as well as speed and throughput, will alleviate or eliminate some of the current constraints and workarounds.

Inference serving frameworks (vLLM, SGLang, TensorRT-LLM) close some of this gap through techniques like continuous batching, speculative decoding, and quantization, extracting more throughput from existing chips rather than waiting on new ones. Mastering the software layer is the faster, cheaper lever before new accelerator designs arrive.

Accelerators aren't used at full capacity out of the box; they require a software stack (kernels, compilers, serving frameworks) to actually reach their theoretical throughput, and most deployed accelerators, including Nvidia GPUs, run below 100% utilization in practice.

**hybrid chip combinations (ASICs, GPUs, TPUs) will be standard for data centers.**

### cost needs to decrease, but GPU prices are increasing



### GPUs are the best current option, but not the best option





### inference is a bottleneck

Decode is the constraint, severely limited by memory bandwidth (the speed data is fetched). Solving for this constraint happens at two levels: the software running on chips, and the design of the chips and data centers themselves.

### Data centers need natural gas

Data centers need electricity, and the only reliable source at the moment is natural gas. processing, gathering, and transmission infrastructure is insufficient for cost-effective deployment.

Nuclear could fill the gap but isn't a five-year solution; existing plants are limited in number, new ones take years to build, and newer reactor designs aren't yet reliable. Solar and batteries are getting cheaper on the hardware itself, but surrounding costs (e.g., land, transmission, storage at scale) are not. Advanced geothermal may be the wildcard: it sits between gas, solar, and nuclear, running 24/7 with zero emissions while reusing existing oil and gas drilling equipment.

### Innovative approaches to cooling and networking are gaining traction slowly

Data centers traditionally rely on air cooling, but as accelerators are packed more densely and run hotter, air cooling struggles to keep up, forcing chips to throttle (reduce performance) to avoid damage. Liquid cooling, which removes heat directly at the chip, is one current approach to sustaining higher density without throttling.

Optical networking, which moves data as light rather than electrical signal, is one current approach to carrying more data with less latency and heat than copper as clusters scale to thousands of chips.

### 'Incumbents' (pre-2023 companies) are providing/building the majority of the infrastructure

'Incumbents' (pre-2023 companies) are providing/building the majority of the infrastructure, and that is unlikely to change in the near-term.  However, because of the amount of investment, even minor efficiency improvements can have a huge impact, attracting new ideas and companies. It's likely that in the near-term the established vendors do most of the work, in the near to medium-term new entrants steal some market share, and in the long-term prices drop and everyone gets hurt (until the cycle resets).

### physical AI is coming along slowly

Robotics excitement has grown because language and vision models lowered the barrier to training. But within the next five years, these models are more likely to serve as the 'brain' for existing machines than to power entirely new ones, and the new machines that do get built are more likely to be deployed into existing enterprise applications, like manufacturing, than into new categories.

World models, and possibly foundation models for robotics, are what unlock a wider range of use cases; a foundation model lets a robot pick up new tasks with limited training, though as with software, ROI will likely be higher for models trained on a specific environment.

Physical AI also requires something digital AI does not: the means to sense and act on the physical world. Sensing spans vision, audio, and other sensors; acting spans movement, dexterity, spatial awareness, and coordination with other autonomous systems.

### AI-Native Applications are Currently Limited, but Will Grow

An AI-native application is a user-facing product, purpose-built around a specific task, that uses AI as its core reasoning engine and ships with everything needed to complete that task out of the box (foundation models are not applications by this definition).

Consistent with the reinvention pattern, existing activities are being reshaped first: content generation (text/image/video), web search, web/app design, coding, and e-commerce (likely next) on the digital side, and driving, product design, manufacturing, and warehouse operations on the physical side. 

Application-layer traction is concentrated in a small number of standouts (e.g., Cursor, Midjourney, Kling); recognized within the field, but none have crossed into mainstream brand recognition, and none are publicly traded. 

As the infrastructure improves, infrastructure cost for applications will decrease. As cost decreases, running models becomes cheaper, resulting in more models, model usage, and applications.

### "Legacy Software" is the Application Trade in the Meantime

Some existing public companies are rebuilding core parts of their business around AI-native models, including running their own models (e.g., AppLovin in ad serving, Unity in game development) and helping customers deploy agents (e.g., Joule SAP).  

These companies provide exposure to the same shift without waiting for AI-native startups to go public. 

Existing SAAS companies that provide agentic infrastructure are well-positioned (assuming the push for agentic workflows continues). The main question is 'do they get more usage in an agentic world?'

### stages of growth

The overall AI sector still has substantial room for near-term growth. AI-native applications are not even publicly traded yet. Infrastructure is much further along, but there 

------------------------


### Physical AI

Physical AI's upside is larger if it arrives, but the path there runs through real-world deployment, data collection, and hardware, none of which digital AI has to contend with to the same degree.

Much of the above applies to physical AI as well; it runs on much of the same compute infrastructure, shares many of the same models, and faces many of the same digital constraints.

are still sub-sectors within infrastructure with the potential for substantial growth.

