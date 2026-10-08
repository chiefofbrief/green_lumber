
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

### The Sector Is Early

Infrastructure is further along than applications, and within infrastructure, physical is further along than digital. None of it is late.

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

Accelerator prices remain elevated on demand, and frontier models are too expensive for most applications to run profitably. Demand keeps climbing regardless. Agents consume far more tokens per task than chat does, and agentic adoption is early, so the mix is still shifting toward the expensive workload.

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

Hyperscalers are the linchpin, since they sit on both sides. They fund the spending and they sell into it.

The money involved is drawing in startups, since even minor efficiency improvements are worth a great deal at this scale. Few have taken real share yet, though some are making headway (e.g., Cerebras). When they do, they compete on price, which is how infrastructure margins come down.

### Earnings are Real, Sustainability is Uncertain

Prices for several of the major companies have risen with earnings, not ahead of them. The usual bubble test does not apply. Three things work against the earnings continuing:
* Some of the demand is circular. They buy from each other, invest in each other, and commit to each other’s capacity, so a share of what looks like end demand is the group paying itself. How much is unknown.
* Some of the recent token revenue came from tokenmaxxing, enterprises pushing usage for its own sake rather than for work. That has turned as buyers get cost conscious, so recent growth rates overstate the baseline. It hits the model providers first and the hardware later, since capex is committed against expected token demand.
* The funding is getting more expensive. It has moved down the capital curve: operating cash flow first, then debt, and now equity and off-balance-sheet structures. Each step costs more and leaves less room, and at some point the spending has to be supported by cash the assets generate.

With agentic adoption still early, how durable the demand is remains unclear. 

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

Three of the five are bets on density, not on AI. Gas, cooling, and networking exist to solve concentration, so they are only bought where compute is packed tightly. Accelerators and memory travel with the workload and get bought wherever inference runs. On-prem deployment is mostly a change in who owns the facility rather than how dense it is, so this is a watch item rather than a live risk, but it inverts the ranking above.

### Within Each Bottleneck, Find the Strongest and the Best-Priced

Do not buy something priced as if the bottleneck is permanent. A company earning shortage margins is being valued on earnings that do not survive the shortage, so the more inflated the margin, the more the price assumes the constraint never breaks. The margin is also what funds the attack on it; the most profitable constraint is the one with the most people working to remove it.

What you are selecting for is durability, at two levels. Start with the constraints that break later; for example, gas doesn't care which architecture wins or whose chip gets deployed. Then, within them, own the strongest companies: low cost, healthy financials, strong brands, real distribution. They hold up when supply catches up and competition arrives.

Tracking the constraint directly is sharper, but the data is often not public, and what is public can be wrong or talked up by the people selling into it. You will not see the break coming, so the position has to survive it without you. 

The capex break is the exception. The growth has to continue to justify both the prices and the capex, and unlike the physical constraints, that is reported quarterly.

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

