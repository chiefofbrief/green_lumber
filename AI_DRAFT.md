
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



The overall AI sector still has substantial room for near-term growth. AI-native applications are not even publicly traded yet. Infrastructure is much further along, but there are still sub-sectors within infrastructure with the potential for substantial growth.




If there is sufficient demand, "all" companies may benefit in the near term. However, when demand shifts, it's likely that only the strongest companies (low costs, healthy financials, strong brands) will benefit, or that all companies will suffer from a deceleration.
* Buying the strongest companies in the fastest-growing sub-sectors is the best way to enjoy growth while mitigating risk.

"AI" has become the umbrella term for a variety of advances in hardware, software, infrastructure, and applications. By being attached to all four categories at the same time, it lends itself easily to too much optimism or pessimism depending on the framing (e.g., optimistic about agents, pessimistic about memory limitations).

In its current form, AI is a productivity tool; it provides a better ratio of outputs to inputs. At the extreme end of the productivity spectrum is autonomous systems that perform a variety of actions with limited (or zero) human input. Whether this will come to fruition is uncertain, but the building blocks towards autonomy will likely be the focus of AI enthusiasts.

AI infrastructure and AI applications are not the same thing. An AI-native application is a user-facing product, purpose-built around a specific task, that uses AI as its core reasoning engine and ships with everything needed to complete that task out of the box (foundation models are not applications by this definition).

To this point, publicly-traded AI-native applications are almost nonexistent, and private AI-native applications lack strong brand recognition, with the exception of a sprinkling of domain/task-specific models (e.g., Cursor, Lovable, Harvey).

As the infrastructure improves, the cost/token will decrease. As cost/token decreases, running models becomes cheaper, resulting in more models, model usage, and applications. There are two major components of AI infrastructure, both of which are being developed at the same time: Physical infrastructure (hardware, data centers, power, etc.) and Digital infrastructure (models, data, architectures, protocols, etc.).

Physical AI is AI that understands and interacts with the laws of physics and the physical world. Physical AI's upside is larger if it arrives, but the path there runs through real-world deployment, data collection, and hardware, none of which digital AI has to contend with to the same degree.

Infrastructure needs and constraints shift over time. Oversupply leads to price competition (and lower margins). Satisfying demand for one component can expose a shortage in another. changes in how applications serve customers (e.g., a shift from chat-based interfaces to background processes) change which pieces matter the most. Novel solutions can make existing constraints obsolete. Therefore, it's best to assess the current needs without assuming they will exist indefinitely, while hedging against scenarios in which they disappear unexpectedly.

Accelerator utilization is the central focus for physical infrastructure. Accelerators are designed to do massive amounts of specialized math simultaneously, requiring sufficient compute (executes the math), fast memory (where weights and state live), and high-speed fabric/interconnects (dictates how far data travels and how fast can it move).

Data centers are the facilities that house accelerators. 

Domain-specific data, data traces (the thought that went into an output), and 'persistent' memory (history, preferences, etc.) are needed to expand beyond foundation models.

Autonomous systems are the central focus for digital infrastructure.

Consistent with the reinvention pattern, existing activities are being reshaped first: content generation (text/image/video), web search, web/app design, coding, and e-commerce (likely next) on the digital side, and driving, product design, manufacturing, and warehouse operations on the physical side. Application-layer traction is concentrated in a small number of standouts (e.g., Cursor, Midjourney, Kling); recognized within the field, but none have crossed into mainstream brand recognition, and none are publicly traded.

Some existing public companies are rebuilding core parts of their business around AI-native models internally (e.g., AppLovin in ad serving, Unity in game development, Datadog in observability), making them investable exposure to the same shift without waiting for AI-native startups to go public.

AI is currently synonymous with models. LLMs have gotten the majority of the attention, but there are also generative image models, generative video models, vision models, vision-action models, world models, etc. Within models, the focus has been on foundation models, general-purpose models trained on broad data that can be adapted to many different tasks. And within foundation models, the focus has been on frontier models, a foundation model at (or near) the current cutting edge of capability. But, this focus is shifting, and will continue to do so. Rather than just relying on frontier models, users are exploring alternative models that offer a better mix of capabilities, cost, and privacy; the open-source vs. closed debate is the current iteration of this exploration. The conversation will eventually shift to domain/task-specific models, which actually meet the definition of an AI application.

Models need context (data, memory, guidance, etc.) to be effective. More broadly, in order for an autonomous system to choose the right action and execute it properly, persistent, task-specific context is critical.

Data is perhaps the most important component of context. For software, domain-specific data and data 'traces' (the thought that went into human output) are necessary to augment beyond general models. Potential sources include end customers (e.g., a law firm providing its data and thought process), third-party model trainers and data providers (e.g., Mercor), and vertical SAAS companies (e.g., Tyler, Agilsys).

Data for physical AI is currently more limited since there is no equivalent to internet data; various approaches such as world models, videos, and simulations are being used, but the most likely source of substantial data is from the robots themselves during deployment.

Most software is stateless; each request is handled independently, with no memory of prior requests, which makes it easy to scale up or down on demand ('elastic'). Stateful systems retain information between requests and need to route users back to infrastructure that holds their state.

Observability (monitoring what is being done) and governance (controlling what can be done) will continue to be critical.

For autonomous systems to reach their potential, they need to act on a world built for humans. New protocols are emerging to let systems do what they couldn't natively, communicate with each other, execute transactions, and more (e.g., A2A for agent-to-agent communication, x402 for agentic payments). At the same time, the human-facing world reshapes itself to be operable by non-human actors, with websites, software, and payment providers adapting to systems rather than people.

Inference, when a model applies its training to produce output, has two stages: prefill (processing the initial prompt) and decode (generating the response token by token). Decode is the constraint, severely limited by memory bandwidth (the speed data is fetched). Solving for this constraint happens at two levels: the software running on chips, and the design of the chips and data centers themselves.

Accelerators aren't used at full capacity out of the box; they require a software stack (kernels, compilers, serving frameworks) to actually reach their theoretical throughput, and most deployed accelerators, including Nvidia GPUs, run below 100% utilization in practice. Inference serving frameworks (vLLM, SGLang, TensorRT-LLM) close some of this gap through techniques like continuous batching, speculative decoding, and quantization, extracting more throughput from existing chips rather than waiting on new ones. Mastering the software layer is the faster, cheaper lever before new accelerator designs arrive.

The biggest point of leverage, though, is accelerators; new designs that better balance memory and compute, as well as speed and throughput, will alleviate or eliminate some of the current constraints and workarounds.

hybrid chip combinations (ASICs, GPUs, TPUs) will be standard for data centers. 

Data centers traditionally rely on air cooling, but as accelerators are packed more densely and run hotter, air cooling struggles to keep up, forcing chips to throttle (reduce performance) to avoid damage. Liquid cooling, which removes heat directly at the chip, is one current approach to sustaining higher density without throttling.

Optical networking, which moves data as light rather than electrical signal, is one current approach to carrying more data with less latency and heat than copper as clusters scale to thousands of chips.

Both are today's leading approaches, not permanent ones; better chip design could ease these demands directly, on the same uncertain timeline as before. All of this runs inside the data center, and the data center itself requires electricity to operate.

Data centers need electricity, and the only reliable source at the moment is natural gas. processing, gathering, and transmission infrastructure is insufficient for cost-effective deployment.

Nuclear could fill the gap but isn't a five-year solution; existing plants are limited in number, new ones take years to build, and newer reactor designs aren't yet reliable. Solar and batteries are getting cheaper on the hardware itself, but surrounding costs (e.g., land, transmission, storage at scale) are not. Advanced geothermal may be the wildcard: it sits between gas, solar, and nuclear, running 24/7 with zero emissions while reusing existing oil and gas drilling equipment.

'Incumbents' (pre-2023 companies) are providing/building the majority of the infrastructure, and that is unlikely to change in the near-term.  However, because of the amount of investment, even minor efficiency improvements can have a huge impact, attracting new ideas and companies. It's likely that in the near-term the established vendors do most of the work, in the near to medium-term new entrants steal some market share, and in the long-term prices drop and everyone gets hurt (until the cycle resets).

Much of the above applies to physical AI as well; it runs on much of the same compute infrastructure, shares many of the same models, and faces many of the same digital constraints.

Robotics excitement has grown because language and vision models lowered the barrier to training. But within the next five years, these models are more likely to serve as the 'brain' for existing machines than to power entirely new ones, and the new machines that do get built are more likely to be deployed into existing enterprise applications, like manufacturing, than into new categories.

World models, and possibly foundation models for robotics, are what unlock a wider range of use cases; a foundation model lets a robot pick up new tasks with limited training, though as with software, ROI will likely be higher for models trained on a specific environment.

Physical AI also requires something digital AI does not: the means to sense and act on the physical world. Sensing spans vision, audio, and other sensors; acting spans movement, dexterity, spatial awareness, and coordination with other autonomous systems.

Existing SAAS companies that provide agentic infrastructure are well-positioned (assuming the push for agentic workflows continues). The main question is 'do they get more usage in an agentic world?'
