
## The Basics of Investing in New Technology

### It's all About Growth

Expected sales growth, and the risks to that growth, dictate a company's stock price. New technology provides the potential for abnormal sales growth, and therefore, the potential for extreme stock price increases.

Technology expands sectors, not just companies. If there is sufficient demand, "all" companies in a sub-sector may benefit temporarily. Start by identifying which sub-sectors will experience the most rapid growth. Good starting points are recent sales growth and constraints to adoption.

Next, identify the companies within the high-growth sub-sectors which are best positioned to benefit from that growth. The strongest companies (low costs, healthy financials, strong brands) are a good starting point. 

### Prioritize Applications, Buy Infrastructure in the Meantime

New technology can be broken into two major sub-sectors, Applications and Infrastructure. The vast majority of value ultimately accrues at the application layer, which is ultimately where investments should be concentrated.  

Applications initially get more traction by reinventing existing activities rather than inventing new ones. For example, e-commerce reinvented mail-order catalogs, and LLMs are a substitute for web search. Start with novel approaches to existing activities. Once the technology is well-established, entirely new behaviors gain traction and become investable.   

The primary purpose of infrastructure is to lower the cost of deployment for applications. The companies benefit while they are solving a constraint to deployment, but eventually become commodities as constraints shift. Oversupply (leading to price competition), changes in how applications serve customers, and novel solutions can all shift constraints. The strongest companies (low costs, healthy financials, strong brands) are a good starting point as they are best able to withstand oversupply, but even they can experience huge price decreases.  

### Try to Be Early, But Definitely Don't Be Late

Being right on the wrong timeline can be similar to being wrong. A balance must be struck between being early enough to enjoy growth while not being so early that a return is not available for years. The ideal investment experiences sales growth in the near-term, which is about 2 years. 

However, the worst possible scenario is being late, so the absolute likelihood of sales growth, regardless of timeline, is the starting point. Among sub-sectors and companies where growth is relatively certain, prioritize by the likelihood of that growth appearing in the near-term.   

Be conservative when estimating the timeline for adoption. It's easy to make the mistake of being too early in new technology. Adoption of applications at scale is usually not realized until well after the potential is visible. The infrastructure takes time to build, and people's behaviors need time to adapt. 

Being early only pays if you still own it when the growth arrives. The usual failure isn't bad analysis, it's giving up on the position before the payoff. 

-----------------

## The Basics of AI

### Productivity is the Value Proposition, Autonomy is the Goal

In its current form, AI is a productivity tool; it provides a better ratio of outputs to inputs. This can mean fewer inputs, more outputs, and/or higher-quality outputs. 

At the extreme end of the productivity spectrum are autonomous systems that perform a variety of actions with limited (or zero) human input. The building blocks towards autonomy are the focus of AI development.

What limits autonomy is reliability. Models are probabilistic, not deterministic: the same input can produce different outputs, and a wrong one looks like a right one. Reliability varies by task in ways that are hard to predict. Autonomy has arrived first where outputs can be verified, and is likely to be more prevalent where the cost of errors is low. 

### Infrastructure and Applications are Both Digital and Physical

AI infrastructure has two components. Physical infrastructure is the hardware: accelerators, racks, networking, power, and cooling. Digital infrastructure is the software and context: models, architectures, data, and protocols.

AI applications split the same way. An AI-native application is a user-facing product, purpose-built around a specific task, that uses AI as its core reasoning engine and ships with everything needed to complete that task out of the box. Digital applications works with information, such as text, images, and video. Physical applications understand and interact with the physical world, as in robots, autonomous vehicles, and industrial systems.

### Context and Compute are the Fuel

Compute is the processing power that lets AI models learn patterns and generate outputs. Training spends it to learn patterns from data; inference spends it every time the model is used. It is the input you can buy, so it scales with money and with how fast data centers get built. 

The industry assumes scale works: more compute and more data produce better models, predictably, and it has held over several orders of magnitude. That assumption is what justifies the spending. It is an empirical observation, not a law, and architecture is the most likely thing to break it.

Context is what the model works with. It takes three forms, and they behave differently.
* Training data is what the model learns from before it is deployed. General models have already absorbed the public internet, so what remains scarce is domain-specific data and traces, meaning the thinking behind the work rather than just the output. That sits with whoever does the work: end customers, data providers, and vertical software companies. Physical AI has no public equivalent to start from.
* Prompt context is what the model is given at the moment it runs. It is supplied by the user or the application, and it is the difference between a generic answer and a correct one.
* State and memory are what a system carries across a task. They are not sourced, they accumulate as the system runs, and they have to be stored and retrieved.

Compute and context are bound together by memory. Every token generated requires fetching context, so compute sits idle whenever it cannot be fetched fast enough. Adding compute does not help if the context cannot reach it.

### Training and Inference are the Two Jobs

Training is building the model: compute is applied to data so the model learns patterns. It happens before deployment and is paid for up front.

Inference is using the model. It happens every time, and it is paid for every time.

Inference has two stages. Prefill processes the prompt and is limited by compute. Decode generates the response one token at a time and is limited by memory bandwidth, so decode is usually the constraint. This changes the economics of software. Traditional software costs almost nothing to serve one more user. AI applications pay for inference on every use, so cost scales with usage and margins depend on what inference costs.

### Physical Infrastructure Maximizes Accelerator Utilization

Accelerators, which are designed to do massive amounts of specialized math simultaneously, perform the computations. They hold context in memory and run the math against it. GPUs and custom ASICs (e.g., TPUs) are two forms.

An accelerator needs three things working together: cores to execute the math, memory to hold weights and state, and interconnect to move data in and out. Utilization is set by whichever of those is slowest. Software sets how much of that is reached, since accelerators do not hit their rated throughput without kernels, compilers, and serving frameworks built for them.

Accelerators are the most expensive part of the stack, so an idle one is the cost. Everything else in physical infrastructure exists to keep them busy. Data centers house them. Power runs them. Cooling removes their heat so they do not throttle. Networking connects them so they can work as one system instead of waiting on each other.

### Digital Infrastructure Makes Models Useful

Digital infrastructure has two layers: the model, and everything around it. A model is any system trained to produce outputs from patterns in data. LLMs are one type. Image, video, vision, vision-action, and world models are others. Within a type, models vary in size, cost, context, and where they can run.

Architecture is the design that determines what a model can do and how much compute and memory it needs. The transformer is the basis for today's foundation models. A new base architecture would change things drastically. Until then, efficiency comes from modifying the transformer to use less compute and less memory, and from hybrids that blend in alternative designs (e.g., MoE).

A model on its own only produces outputs. Everything around it turns those outputs into work. Runtime software decides how requests are batched and served. Observability and governance determine what systems are allowed to do and whether anyone can see what they did. That surrounding layer has to change as systems become autonomous, which breaks two assumptions:
* Most software is stateless: each request is handled independently, with no memory of prior requests, which makes it easy to scale up or down on demand ("elastic"). Autonomous systems are stateful. They retain information between requests, so requests must be routed back to the infrastructure that holds their state.
* They also have to act on a world built for humans, so new protocols are needed for them to communicate with each other, execute transactions, and more (e.g., A2A for agent-to-agent communication). At the same time, the human-facing world adapts to non-human actors, with websites, software, and payment providers becoming operable by systems as well as people.

--------------------

## The Current AI Landscape

### The Model Layer is Diversifying

AI is still largely synonymous with LLMs, and within LLMs, with frontier models. But image, video, vision, vision-action, and world models are all in use, and within any type, models vary in size, cost, context, and where they can run. 

Users are exploring rather than defaulting to the frontier. They are looking for a workable mix of capability, cost, and privacy. Open-source versus closed is one version of that search. Local models, which run on a user's own hardware, are another. Taken together, these point to general capability commoditizing: open-weight models have closed much of the gap and cap what labs can charge for it.

Enterprises are going a step further. Rather than choosing among general models, they are building their own on their own data. A frontier model knows what is public; it does not know how a particular company works.

### Task-Specific Data Is the Scarce Input

Proprietary data is valuable right now. General models have absorbed what the internet offers, so what improves performance on a specific task is the data held by whoever does the work,  hosts the work, or collects it on purpose. 

Data originates with the people doing the work: a law firm, a hospital, a manufacturer. They hold both the output and the reasoning behind it, and they are using it to build and augment their own models.

Vertical software companies hold data as a byproduct, since the work runs inside their systems (e.g., Tyler, Agilysys). 

A third industry is forming to build it deliberately (e.g., Mercor). These companies supply traces, the reasoning behind expert work rather than the output, to the labs.

### Inference (and Cost) is the Central Concern

Inference is where cost and capacity pressure accumulate as usage grows. Decode is the main issue. Solutions are being pursued at every layer: model architecture and compression, runtime software (e.g., vLLM, SGLang, TensorRT-LLM), chip design, and data center design.

Cost per token is falling, but only through efficiency gains within existing designs: architectures that use less compute and memory (e.g., MoE), quantization that shrinks the data being moved, runtime software that batches requests, and networking that moves data faster. A drastic decline would require more accelerator supply or a step change through a new base architecture or new accelerator designs. 

Accelerator prices remain elevated on demand, and frontier models are too expensive for most applications to run profitably. Demand keeps climbing regardless, since agents consume far more tokens per task than chat does.

### Every Physical Constraint Shows Up as an Idle Accelerator

Most deployed accelerators, including Nvidia GPUs, run below full utilization in practice. Memory leaves cores waiting on data, weak networking leaves chips waiting on each other, heat forces throttling, and missing power leaves chips unused.

Memory is the hardest constraint to relieve. Bandwidth, not compute, sets how fast tokens can be generated in decode, and capacity sets how much context a chip can hold. High-bandwidth memory addresses both, but supply has not kept up with demand and prices have stayed high. One response is to stop using the same chip for everything. Training, prefill, and decode have different compute and memory needs, so data centers are running mixed fleets and routing each job to the silicon that fits it. GPUs remain the default by a wide margin, but the field is widening beyond the chips best suited to training.

Networking is being extended up, out, and across. Scale up links chips within a rack so they act like one larger accelerator. Scale out links racks across the data center. Scale across links data centers. Copper still handles most connections within a rack, but it runs into distance and heat limits as racks get denser. Optical moves data as light, carrying more with less latency and heat, and everything beyond a rack already runs on it. Ethernet is the protocol for scaling out and across.

Cooling is shifting to liquid, gradually. Air is the default, but as accelerators are packed more densely and run hotter it struggles to keep up. Liquid removes heat at the chip and sustains higher density. 

Power limits how many accelerators can run, and natural gas is the only source that can reliably supply it now. Even gas is constrained, since processing, gathering, and transmission infrastructure is insufficient for cost-effective deployment. 
* Nuclear is not a five-year solution: existing plants are limited, new ones take years, and newer reactor designs are not yet reliable.
* Solar and batteries are getting cheaper on the hardware, but land, transmission, and storage at scale are not.
* Advanced geothermal may be the wildcard, running constantly with zero emissions while reusing existing oil and gas drilling equipment.

### Agents Are Autonomy in Practice, and Digital Infrastructure Is Being Built Around Them

Where a chatbot answers, an agent acts. It carries context across a long task, uses tools, and makes decisions along the way.

Errors compound across a long task, so observability and governance are becoming critical as agents are given more autonomy: someone has to see what they did and limit what they can do. New protocols are emerging to let agents do what they cannot natively, such as communicate with each other and execute transactions (e.g., A2A for agent-to-agent communication, x402 for agentic payments).

Serving agents is a different problem than serving software, and cloud providers are rearchitecting around it. Sessions run for minutes or hours rather than milliseconds, capacity cannot be added or removed freely, and a failure loses the work rather than just the request.

Agents act on software through APIs. MCP has become the leading protocol for exposing them to agents, and adoption is already deep in large enterprises, but agents call ordinary APIs too. Software that exposes comprehensive access gets used by agents; software that does not gets routed around.

### Incumbents Are Leading the Buildout (for Now)

Companies that existed before 2023 are both funding the buildout and supplying it. A handful of hyperscalers are putting up most of the money. A wider set of incumbents is selling into it, because they already have the manufacturing, the relationships, the products, the data, and the software.

Hyperscalers are the linchpin, since they sit on both sides. They fund the spending and they sell into it. That creates two problems:

Some of the demand is circular. They buy from each other, invest in each other, and commit to each other's capacity, so a share of what looks like end demand is the group paying itself. How much is unknown.
The funding is getting more expensive. It has moved down the capital curve: operating cash flow first, then debt, and now equity and off-balance-sheet structures. Each step costs more and leaves less room, and at some point the spending has to be supported by cash the assets generate.

The money involved is drawing in startups, since even minor efficiency improvements are worth a great deal at this scale. Few have taken real share yet, though some are making headway (e.g., Cerebras). When they do, they compete on price, which is how infrastructure margins come down.

### AI-Native Applications Are Early

Existing activities are being reshaped before new ones are invented, which is the usual pattern. Content generation (text, image, video) came first, since the output is the product. Coding followed, since the output can be checked. Web search is being substituted, and web and app design after it. E-commerce is the likely next one, since it is a transaction an agent can carry out.

Traction is concentrated in a small number of standouts (e.g., Cursor, Midjourney, Kling). They are recognized within the field, but none has crossed into mainstream brand recognition, and none are publicly traded. That is the gap between what is working and what is investable.

Inference cost is the constraint on the business model. Applications pay for every use, so margins depend on what inference costs, and most cannot yet run frontier models profitably. Until that changes, the better application is not necessarily the better business.

### Physical AI is Coming, but Still Needs Time

Robotics excitement has grown because language and vision models lowered the barrier to training robots. For now, these models are more likely to serve as the brain for existing machines than to power entirely new ones, and the machines that get deployed are more likely to go into existing enterprise applications like manufacturing than into new categories.

Driving, product design, manufacturing, and warehouse operations are where it is showing up.

The constraints go beyond the models. Hardware to sense and act on the physical world is expensive and slow to iterate. Errors are not reversible, which raises the reliability bar. And there is no public equivalent to the internet data that trained language models. World models, video, and simulation are being explored as substitutes, but the robots themselves during deployment are the most likely source at scale.

World models, and possibly foundation models for robotics, are what could broaden physical AI beyond its current applications.

-------------------------

## Investment Implications

### Buy the Physical Bottlenecks

The total spend is not the trade. The trade is whatever is scarce while it is scarce. The best of these are the ones others are not already crowded into, and the ones that survive a change in architecture or chip design.

**Natural gas and its supply chain**. Power is the hardest constraint on how many accelerators can run, and gas is the only source that reliably supplies it now. This is the safest of the five. It is the raw input, so it does not care which architecture wins, which chip is deployed, or how fast cost per token falls. The processing, gathering, and transmission infrastructure is as much the trade as the gas itself, since that is where the shortage sits.

**Cooling, especially liquid**. Density keeps rising and air cannot keep up. Adoption is gradual, which makes the demand long rather than spiky, and it is not yet crowded. Like gas, it is indifferent to what runs on the chips.

**Networking, especially optical**. Everything beyond a rack already runs on light, and scale out and scale across keep adding links. More deployment means more connections regardless of whose silicon is in the racks.

**Accelerators broadly**. Mixed fleets mean picking the winning chip matters less than owning the growth in chips deployed. Nvidia, the custom-silicon designers, and the hyperscalers building their own can all be held for the same reason. The bet is on volume, not on who wins.

**Memory**. The most obvious of the five and the most crowded. Demand is real and scales directly with inference volume, but current margins reflect shortage pricing, and shortage pricing reverts. Own it knowing the margin is what gives back, not the demand.

### Within Each Bottleneck, Find the Strongest and the Best-Priced

Do not buy something priced as if the bottleneck is permanent. A company earning shortage margins is being valued on earnings that do not survive the shortage, so the more inflated the margin, the more the price assumes the constraint never breaks.

What you are selecting for is durability, at two levels. Start with the constraints that break later; for example, gas doesn't care which architecture wins or whose chip gets deployed. Then, within them, own the strongest companies: low cost, healthy financials, strong brands, real distribution. They hold up when supply catches up and competition arrives.

Tracking the constraint directly is sharper, but the data is often not public, and what is public can be wrong or talked up by the people selling into it. You will not see the break coming, so the position has to survive it without you.

### Own Agentic Infrastructure

Agents are where autonomy is showing up, and the layer serving them is being built now. Most of it is coming from incumbents extending what they already sell, which makes this ownable today in a way the applications are not.

**Task-specific data**. What an agent needs to act correctly rather than generically. It sits with whoever does the work, hosts it, or collects it on purpose.

**Observability and governance**. The tools that record what agents did and limit what they can do. The existing observability and security vendors are selling it.

**APIs and access**. How agents reach software. MCP leads, but agents call ordinary APIs too, and gateway and identity vendors sit in the same path.

**The agent-readable web**. Sites made parseable, search sold as an API instead of a results page, catalogs and content structured for systems rather than people.

**Cloud and runtime**. The providers rebuilding for sessions that hold state and run long.

**Agentic commerce**. Merchants, marketplaces, and the rails underneath all have to handle a buyer that is not a person. Several standards are competing and none has settled.

### Own Existing Software as the Application Proxy and Data Holder

The application layer is where value ends up, but the AI-native ones are private and cannot run profitably yet. Existing software companies are the way to own that layer now. They hold the domain data by default, since the work runs inside their systems, and they have the customers and distribution already.

Some of these companies are also the ones AI replaces. Owning the category does not work; three things separate them:
* Is the data hard to replicate, or incidental? Accumulated judgment about how work gets done is not reproducible. Transaction records and configuration settings mostly are.
* Do agents use them, or route around them? The ones exposing comprehensive access become the systems agents call. The ones that do not become a layer agents skip.
* Does AI deepen the product, or sit on top of it? Domain-specific models built on their own data are a different thing from a chat interface added to the existing one.

Task-specific models are where this goes. The companies holding the data are the ones positioned to build them.

### Physical AI Is a Supplier and Machine-Maker Trade

Robots are mostly private, unproven, and years from scale. The companies supplying the parts and the machines are neither.

Sensors, cameras, and actuators. What a machine needs to perceive and act. Demand grows with units deployed regardless of which robot company deploys them.

Existing machine makers adding AI. Manufacturing equipment, warehouse systems, agricultural and construction machinery. The models go into machines that already have buyers and installed bases rather than into new categories.

Deployment is slower here than in digital AI. The hardware is expensive and slow to iterate, errors are not reversible, and there is no public data to train on.

### Rotate to AI-Native Applications Later

This is where the value ends up. It is also the one position that cannot be taken yet: the standouts are private, and inference costs more than most applications can carry. What has to change:
* Inference cost. Applications pay per use. Until that falls far enough, the better product is not the better business.
* Access. Nothing here is publicly traded. Listings, or acquisitions that put the exposure inside something that is.
* Reliability. Autonomy has arrived where outputs can be verified. The applications that scale next are the ones where that holds.

Existing software is the proxy until then. When these change, the rotation is out of infrastructure and into applications, because infrastructure eventually competes on price and applications are where the margin ends up.








---------------------------------------------------------------------------------------
-----------------------------------------------------------------------------------------












## STOP!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

----------------------------------------------------------------

### Productivity is the Value Proposition, Autonomy is the Goal

In its current form, AI is a productivity tool; it provides a better ratio of outputs to inputs. This can mean fewer inputs, more outputs, and/or higher-quality outputs. 

At the extreme end of the productivity spectrum are autonomous systems that perform a variety of actions with limited (or zero) human input. The building blocks towards autonomy are the focus of AI development.

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

AI applications split the same way. An AI-native application is a user-facing product, purpose-built around a specific task, that uses AI as its core reasoning engine and ships with everything needed to complete that task out of the box. Digital applications works with information, such as text, images, and video. Physical applications understand and interact with the physical world, as in robots, autonomous vehicles, and industrial systems.


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

### Inference is a Central Concern

Inference is where cost and capacity pressure accumulate as usage grows, and decode is the issue.

Solutions are being pursued at every layer of the stack, from model architecture and compression to runtime software (e.g., vLLM, SGLang, TensorRT-LLM), chip design, and data center design. These are leading approaches, and no single one has settled the constraint.

### Cooling Innovations Reduce Idle Accelerators, but Adoption Is Gradual

Air cooling is the default way to cool accelerators in data centers. As accelerators are packed more densely and run hotter, it struggles to keep up.

Liquid cooling, which removes heat directly at the chip, is the new alternative gaining attention for sustaining higher density.

For now, both are being used. Liquid cooling adoption is real, but it needs to keep scaling.

### Networking Is Being Extended Up, Out, and Across to Reduce Idle Accelerators

Scale up links chips within a rack so they act like one larger accelerator. Scale out links racks across the data center, and scale across links data centers. All three are being explored to ease the inference bottleneck and work around limited GPU supply.

Copper is the default within a rack. Optical is the hot alternative. It moves data as light rather than electrical signals, carrying more data with less latency and heat as clusters scale to thousands of chips.

Ethernet is the approach for scaling across long distances.

### Power Limits How Many Accelerators Can Run, and Natural Gas Is the Only Reliable Source Today

Data centers need large, constant supplies of electricity, and natural gas is the only source that can reliably provide it now. Even gas is constrained, since the processing, gathering, and transmission infrastructure is insufficient for cost-effective deployment.

The alternatives each fall short on something different. Nuclear isn't a five-year solution: existing plants are limited in number, new ones take years to build, and newer reactor designs aren't yet reliable. Solar and batteries are getting cheaper on the hardware itself, but the surrounding costs (land, transmission, storage at scale) are not.

Advanced geothermal may be the wildcard. It sits between gas, solar, and nuclear, running 24/7 with zero emissions while reusing existing oil and gas drilling equipment.

### Cost per Token Is Falling Only Incrementally, and GPU Prices Are Rising

GPUs dominate the accelerators available in the market, and their prices keep rising. 

Cost per token is currently falling only through efficiency. Current techniques deliver incremental gains within existing designs: model architectures that use less compute and memory (e.g., MoE), quantization that shrinks the data being moved, runtime software that batches requests and generates tokens faster, and networking that moves data faster.

A drastic decline would require a step change in technology, either a new base architecture or new accelerator designs. or more accelerators being deployed. 

### Incumbents Are Building Most of the Infrastructure, although it's Attracting New Entrants

"Incumbents" (companies that existed before 2023) are providing and building the majority of the infrastructure, and that is unlikely to change in the near term.

But the amount of investment and the constraints on current infrastructure are attracting new ideas and companies since even minor efficiency improvements can have a huge impact. These entrants are not gaining major share yet, but may over time.

### AI-Native Applications Are Early, and Existing Activities Are Being Reshaped First

Consistent with the reinvention pattern, AI-native applications are reshaping existing activities first: content generation (text, image, video), web search, web and app design, coding, and e-commerce (likely next) on the digital side, and driving, product design, manufacturing, and warehouse operations on the physical side.

Traction is concentrated in a small number of standouts (e.g., Cursor, Midjourney, Kling). They are recognized within the field, but none has crossed into mainstream brand recognition or are publicly traded. 

### Physical AI is Coming, but Still Needs Time

Robotics excitement has grown because language and vision models lowered the barrier to training robots. But for now, these models are more likely to serve as the "brain" for existing machines than to power entirely new ones. The machines that get deployed are more likely to go into existing enterprise applications, like manufacturing, than into new categories.

World models, and possibly foundation models for robotics, are what could broaden physical AI beyond its current applications.

Physical AI faces major constraints beyond the models themselves, including the hardware needed to sense and act on the physical world and the lack of an equivalent to the internet data that trained language models. World models, video, and simulation are being explored as data sources, but the robots themselves during deployment are the most likely source of substantial data.

### Applications Have the Most Room, and Infrastructure Is Further Along



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

