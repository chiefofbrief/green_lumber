
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
* State and memory are what a system carries across a task. They are not sourced, they accumulate as the system runs, and they have to be stored and retrieved, typically in databases.

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

A model on its own only produces outputs. Everything around it turns those outputs into work. Harnesses manage memory, interfaces, and tool execution. Inference runtime software decides how requests are batched, served, and routed. Agent runtime software sits between applications and cloud infrastructure and runs agents in production: it isolates the code they run and saves their state so a failure does not lose the work. Security, identity, observability, and governance make up trust: who a system is, what it can access, what it is allowed to do, and whether anyone can see what it did. That surrounding layer has to change as systems become autonomous, which breaks three assumptions:
* Most software is stateless: each request is handled independently, with no memory of prior requests, which makes it easy to scale up or down on demand ("elastic"). Autonomous systems are stateful. They retain information between requests, so requests must be routed back to the infrastructure that holds their state.
* Most software is deterministic: the same input produces the same output. Models are probabilistic, so outputs vary, and cloud infrastructure may need to adapt to that. Early use cases mostly involve verifiable tasks, which behave more like deterministic systems, so the change may come gradually. Observability and governance stay critical either way.
* They also have to act on a world built for humans, so new protocols are needed for them to communicate with each other, execute transactions, and more (e.g., A2A for agent-to-agent communication). At the same time, the human-facing world adapts to non-human actors, with websites, software, and payment providers becoming operable by systems as well as people.

--------------------

## The Current AI Landscape

### The Sector Is Early

Infrastructure is further along than applications, and within infrastructure, physical is further along than digital. None of it is late.

### The Model Layer is Diversifying

AI is still largely synonymous with LLMs, and within LLMs, with frontier models. But image, video, vision, vision-action, and world models are all in use, and within any type, models vary in size, cost, context, and where they can run. 

Users are exploring rather than defaulting to the frontier. They are looking for a workable mix of capability, cost, and privacy. Examples include:
* Open-source versus closed.
* Local models, which run on a user’s own hardware. Efficiency techniques like quantization, sparse activation, and MoE make them more practical, and the hardware for running them is improving.
* Cheaper models from outside the frontier labs (e.g., Kimi, DeepSeek), which some startups already use because they cost less and are not much worse.

Taken together, these point to general capability commoditizing: open-weight models have closed much of the gap and cap what labs can charge for it. Where models are close substitutes, requests can be routed to whichever fits best on cost, complexity, and domain. Providers then compete to be the one chosen, which may push prices down.

Enterprises are going a step further. Rather than choosing among general models, they are building their own on their own data. A frontier model knows what is public; it does not know how a particular company works.

### Task-Specific Data Is the Scarce Input

Proprietary data is valuable right now. General models have absorbed what the internet offers, so what improves performance on a specific task is the data held by whoever does the work,  hosts the work, or collects it on purpose. 

Data originates with the people doing the work: a law firm, a hospital, a manufacturer. They hold both the output and the reasoning behind it, and they are using it to build and augment their own models. Holding the data is not the same as being able to use it. Enterprise data is often messy and not agent ready, so usable data is scarcer than data that exists.

Vertical software companies hold data as a byproduct, since the work runs inside their systems (e.g., Tyler, Agilysys). Because that data is generated inside software, it may be more structured than what enterprises hold, and so closer to agent ready. 

A third industry is forming to build it deliberately (e.g., Mercor). These companies supply traces, the reasoning behind expert work rather than the output, to the labs.

### Inference (and Cost) is the Central Concern

Inference is where cost and capacity pressure accumulate as usage grows. Decode is the main issue. Serving also gets more complex as the number of models and accelerators grows, since inference runtime software has to route each request to a model and an accelerator based on factors like cost, availability, and latency. Solutions are being pursued at every layer: model architecture and compression, inference runtime software (e.g., vLLM, SGLang, TensorRT-LLM), chip design, and data center design. Software is likely the fastest and cheapest of these, since it gets more throughput from existing chips instead of waiting on new ones.

Cost per token is falling through efficiency gains within existing designs, which are significant but not drastic. A drastic decline would require a change in supply or design: more accelerators coming online as data centers are finished, a new base architecture, or new accelerator designs. In the meantime, the marginal gains come from both digital and physical infrastructure:
* **Digital**
  * Architectures, such as MoE, that use less compute and memory.
  * Compression, which shrinks the model and the data being moved.
  * Smaller task- or domain-specific models, which need less compute because general models carry more than a given task needs.
  * Inference runtime software, which batches requests and routes each one to the model and chip that fits it on cost, complexity, domain, and availability.
* **Physical**
  * Networking, which moves data faster so chips wait less on each other.
  * Cooling, which keeps chips from throttling.
  * Mixed fleets, which use different chips for training, prefill, and decode, since their compute and memory needs differ.

Accelerator prices remain elevated on demand, and frontier models are too expensive for most applications to run profitably. Demand keeps climbing regardless. Agents consume far more tokens per task than chat does, and agentic adoption is early, so the mix is still shifting toward the expensive workload.

### Every Physical Constraint Shows Up as an Idle Accelerator

Most deployed accelerators, including Nvidia GPUs, run below full utilization in practice. Memory leaves cores waiting on data, weak networking leaves chips waiting on each other, heat forces throttling, and missing power leaves chips unused.

Memory is the hardest constraint to relieve with hardware. Bandwidth, not compute, sets how fast tokens can be generated in decode, and capacity sets how much context a chip can hold. High-bandwidth memory addresses both, but supply has not kept up with demand and prices have stayed high. Other responses, in rough order of how soon they help:
* Software and model architecture, the near-term fix, since they reduce how much memory each token needs (e.g., quantization, cache compression, MoE).
* Higher utilization through cluster layout and networking. Existing chips can be arranged and linked differently, such as racks built for memory and racks built for compute, so cores wait less on data.
* New chip designs that are more efficient. GPUs remain the default by a wide margin, but the field is widening beyond the chips best suited to training.

Networking is being extended up, out, and across. Scale up links chips within a rack so they act like one larger accelerator. Scale out links racks across the data center. Scale across links data centers. Copper still handles most connections within a rack, but it runs into distance and heat limits as racks get denser. Optical moves data as light, carrying more with less latency and heat, and everything beyond a rack already runs on it. Ethernet is the protocol for scaling out and across.

Cooling is shifting to liquid, gradually. Air is the default, but as accelerators are packed more densely and run hotter it struggles to keep up. Liquid removes heat at the chip and sustains higher density. 

Power limits how many accelerators can run, and natural gas is the only source that can reliably supply it now. Even gas is constrained, since processing, gathering, and transmission infrastructure is insufficient for cost-effective deployment. 
* Nuclear is not a five-year solution: existing plants are limited, new ones take years, and newer reactor designs are not yet reliable.
* Solar and batteries are getting cheaper on the hardware, but land, transmission, and storage at scale are not.
* Advanced geothermal may be the wildcard, running constantly with zero emissions while reusing existing oil and gas drilling equipment.

### Agents Are Autonomy in Practice, and Digital Infrastructure Is Being Built Around Them

Where a chatbot answers, an agent acts. It makes decisions, carries context across a long task, and uses tools. Each creates a need that existing infrastructure was not built for.

Agents make decisions along the way. Because models are probabilistic and a wrong output can look like a right one, errors compound across a long task, and an agent's output cannot be assumed correct. Autonomy is therefore given only to the extent that agents can be trusted, and that trust has to come from controls around them, so adoption may lag until those controls are in place. Trust has four parts:
* **Security**: agents hold access to sensitive systems and data, so a compromised or misbehaving agent can do damage.
* **Identity**: each agent needs its own credentials, so it is a non-human identity, and who it is and what it can access has to be defined.
* **Observability**: someone has to see what they did.
* **Governance**: someone has to limit what they can do.

Carrying context across a long task makes serving agents a different problem than serving software. Sessions run for minutes or hours rather than milliseconds, capacity cannot be added or removed freely, and a failure loses the work rather than just the request. Cloud providers are rearchitecting around this, and agent runtime software is the layer being built to keep agents running through failures. Memory also has to persist across sessions, and databases built for transactions and batch queries may need to adapt to serve it.

Using tools means acting on a world built for humans. New protocols are emerging to let agents do what they cannot natively:
* Communicate with each other (e.g., A2A).
* Execute transactions (e.g., x402 for payments, UCP for what commerce actions mean to an agent). Micropayments are only viable if transactions get cheaper, which is why new payment protocols are being pursued.
* Work with websites (e.g., NLWeb, WebMCP). websites).

Agents act on software through APIs, so software that exposes comprehensive access gets used by agents and software that does not gets routed around. MCP has become the leading protocol for that exposure, and adoption is already deep in large enterprises, but agents call ordinary APIs too, so MCP adds to APIs rather than replacing them.

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

Inference cost is the constraint on the business model because applications pay for every use. Token prices from the leading labs have stayed high, and token costs are unlikely to fall soon because GPU costs are not falling. Until the economics work, the better application is not necessarily the better business. Application providers are responding in two ways:
* The first is switching to alternative models from outside the frontier labs (e.g., Kimi, DeepSeek), which offer lower token prices, so margins may improve even if token costs do not fall quickly.
* The second is focusing on a task or domain (e.g., Cursor for coding), where a higher return per use may support higher prices and justify not being replaced by a foundation model. Task- or domain-specific models offer higher quality output with fewer inputs, and likely start with a well-defined task where AI enables capabilities beyond a human’s, such as 24/7 work, analysis of far more data, and pattern recognition.

### Physical AI is Coming, but Still Needs Time

Robots are becoming smarter with AI. Robotics excitement has grown because language and vision models lowered the barrier to training robots. For now, these models are more likely to serve as the brain for existing machines (e.g., predictive maintenance, inspection, autonomous process control, material movement) than to power entirely new ones, and the machines that get deployed are more likely to go into existing enterprise applications like manufacturing than into new categories. Several models act as the brain:
* A world model understands the laws of physics. Instead of predicting the next word in a sentence, it predicts the next frame of a video, which lets the machine anticipate the physical consequences of an action.
* An LLM reasons through what needs to be done.
* Vision models translate that reasoning into physical, mechanical execution.

Driving, product design, manufacturing, and warehouse operations are where it is showing up.

Robotics has many more dimensions than language or vision, which makes the models harder to build. And the constraints go beyond the models. Hardware to sense and act on the physical world is expensive and slow to iterate. Errors are not reversible, which raises the reliability bar. And there is no public equivalent to the internet data that trained language models. World models, video, and simulation are being explored as substitutes, but the robots themselves during deployment are the most likely source at scale.

World models, and possibly foundation models for robotics, are what could broaden physical AI beyond its current applications. A foundation model lets a robot pick up new tasks with limited training, which is what widens the range of uses. As with software, the return is likely higher for models trained on a specific environment.

-------------------------

## Investment Implications

### Buy the Physical Bottlenecks

A bottleneck is worth owning until it is solved, and the price already contains a guess about when that happens. The position is the difference between that guess and the truth. There are currently five major constraints in the physical supply chain:
* **Natural gas and its supply chain**. Power limits how many accelerators can run, and gas is the only source that reliably supplies it now. The processing, gathering, and transmission infrastructure is as much the trade as the gas itself, since that is where the shortage sits.
* **Cooling, especially liquid**. Density keeps rising and air cannot keep up. Liquid removes heat at the chip and sustains higher density. Adoption is gradual, which makes the demand long rather than spiky.
* **Networking, especially optical**. Everything beyond a rack already runs on light, and scale out and scale across keep adding links. More deployment means more connections regardless of whose silicon is in the racks.
* **Accelerators broadly**. Mixed fleets mean picking the winning chip matters less than owning the growth in chips deployed. Nvidia, the custom-silicon designers, and the hyperscalers building their own can all be held for the same reason.
* **Memory**. Bandwidth sets how fast tokens can be generated in decode, and capacity sets how much context a chip can hold. High-bandwidth memory addresses both, and supply has not kept up with demand.

Each of the five ends for a different reason. Four things can end them:
* **Supply catching up**. New supply is slow where it needs fabs, plants, or construction. But some supply already exists and is not running: accelerators have been bought that are not racked, because power, shell, and cooling are not ready. Those come online without anything being built.
* **Technology change**. A new architecture or a different chip changes what is needed, which can end a constraint without relieving it. Gas is indifferent to both, since it is the raw input.
* **Density**. The buildout assumes compute keeps concentrating in large, dense sites. Gas, cooling, and networking are only needed there, since they exist to solve density. If inference spreads to smaller sites instead, those three are not bought, while accelerators and memory still are. On-prem and edge deployment is growing, and whether it reaches a scale that changes data center demand remains to be seen.
* **Software**. Software changes faster than chips, architectures, or physical supply, since the others require fabrication or construction. It cannot produce electricity or remove heat, so power and cooling sit outside its reach. It works on the other three: utilization on accelerators, bytes per token on memory through quantization and cache compression, and data movement on networking.



### Within Each Bottleneck, Find the Strongest and the Best-Priced

Do not buy something priced as if the bottleneck is permanent. A company earning shortage margins is being valued on earnings that do not survive the shortage, so the more inflated the margin, the more the price assumes the constraint never breaks. The margin is also what funds the attack on it; the most profitable constraint is the one with the most people working to remove it.

What you are selecting for is durability, at two levels. Start with the constraints that break later; for example, gas doesn't care which architecture wins or whose chip gets deployed. Then, within them, own the strongest companies: low cost, healthy financials, strong brands, real distribution. They hold up when supply catches up and competition arrives.

Tracking the constraint directly is sharper, but the data is often not public, and what is public can be wrong or talked up by the people selling into it. You will not see the break coming, so the position has to survive it without you. 

The capex break is the exception. The growth has to continue to justify both the prices and the capex, and unlike the physical constraints, that is reported quarterly.

### Own Agentic Infrastructure

Agents are where autonomy is showing up, and the layer serving them is being built now. Most of it is coming from incumbents extending what they already sell, which makes this ownable today in a way the applications are not.

**Task-specific data**. What an agent needs to act correctly rather than generically. It sits with whoever does the work, hosts it, or collects it on purpose. Much of it is messy and not agent ready, so companies that make it usable may benefit, either by cleaning, organizing, and structuring it, by making the databases it sits in usable by agents, or by already holding it in an organized form (e.g., vertical software companies).

**Trust**: security, identity, observability, and governance. The tools that secure agents, define who each one is and what it can access, record what it did, and limit what it can do. The existing observability, security, and identity vendors are selling it.

**APIs and access**. How agents reach software. MCP leads, but agents call ordinary APIs too, and gateway and identity vendors sit in the same path.

**The agent-readable web**. Sites made parseable, search sold as an API instead of a results page, catalogs and content structured for systems rather than people.

**Cloud, runtime, and databases**. The providers rebuilding for sessions that hold state and run long.

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

Robot components. What a machine needs to perceive, move, and run. Perception takes depth, navigation, and proximity sensors, cameras, and microphones. Movement takes actuators and motor controllers. Power takes batteries and charging. Demand grows with units deployed regardless of which robot company deploys them.

Existing machine makers adding AI. Manufacturing equipment, warehouse systems, agricultural and construction machinery. The models go into machines that already have buyers and installed bases rather than into new categories. Where physical AI creates value includes predictive maintenance, material movement, inspection, and autonomous process control.

Deployment is slower here than in digital AI. The hardware is expensive and slow to iterate, errors are not reversible, and there is no public data to train on.

### Rotate to AI-Native Applications Later

This is where the value ends up. It is also the one position that cannot be taken yet: the standouts are private, and inference costs more than most applications can carry. What has to change:

* **Inference cost**. Applications pay for every use, and token costs are unlikely to fall soon. Until the return per use supports the price, the better product is not the better business.
* **Access**. Nothing here is publicly traded. Listings, or acquisitions that put the exposure inside something that is.
* **Reliability**. Autonomy has arrived where outputs can be verified. The applications that scale next are the ones where that holds.

The first investable applications are likely to be task- or domain-specific, because they offer higher quality output with fewer inputs. They may start with a well-defined task where AI enables capabilities beyond a human's, such as 24/7 work, analysis of far more data, and pattern recognition. Helping enterprises use their own data more effectively may be one of the first, since it draws on those capabilities.

Existing software is the proxy until these conditions change. When they do, the rotation is out of infrastructure and into applications, because infrastructure eventually competes on price and applications are where the margin ends up.

