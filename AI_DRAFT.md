
## The Basics of Investing in New Technology

### It's all About Growth

Expected sales growth, and the risks to that growth, dictate a company's stock price. New technology provides the potential for abnormal sales growth, and therefore, the potential for extreme stock price increases.

**Start by identifying which sub-sectors will experience the most rapid growth**. New technology expands sectors, so several companies can benefit, not just one, and if there is sufficient demand, “all” companies in a sub-sector may benefit temporarily. That makes the choice of sub-sector the main decision. Good starting points are recent sales growth and constraints to adoption.

**Next, identify the companies within those sub-sectors that are best positioned to benefit.** Start with the strongest. Then, among the strongest, look for those where the price does not already reflect all of the expected growth. Characteristics of the strongest companies include:
* Low costs.
* Healthy financials.
* Strong brands.
* Real distribution.
* Scarce IP.

### Prioritize Applications, Buy Infrastructure in the Meantime

**Applications are where the value ends up.** New technology breaks into two major sub-sectors, applications and infrastructure. The vast majority of value accrues at the application layer, which is where investments should ultimately be concentrated. Applications depend on infrastructure, which comes first.

**The first applications to gain traction are novel approaches to existing activities.** Applications initially get more traction by reinventing existing activities rather than inventing new ones: e-commerce reinvented mail-order catalogs, and LLMs are a substitute for web search. Once the technology is well-established, entirely new behaviors gain traction and become investable.

**Within infrastructure, identify the sub-sectors best poised for growth.** The primary purpose of infrastructure is to lower the cost of deployment for applications. The binding constraints on deployment are the most obvious areas for growth, and the ones to focus on are those that are hard to work around and can pay off in the near term. The growth lasts only while a constraint is binding, and the companies solving it eventually become commodities as constraints shift. Constraints shift for several reasons:
* Oversupply leads to price competition and lower margins.
* Solving one constraint can expose another.
* Changes in how applications serve customers change which pieces matter most (e.g., a shift from chat to background processes).
* Novel solutions can make existing constraints obsolete.

**Within those sub-sectors, identify the companies best positioned to benefit.** Start with the strongest, since they are best able to withstand oversupply. But even the strongest can experience huge price decreases when a constraint breaks, so look among them for those where the price does not already reflect all of the expected growth. Avoid companies priced as if the constraint is permanent.

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
* State and memory are what a system carries across a task and across sessions, such as history and preferences. They are not sourced, they accumulate as the system runs, and they have to be stored and retrieved, typically in databases.

Compute and context are bound together by memory. Every token generated requires fetching context, so compute sits idle whenever it cannot be fetched fast enough. Adding compute does not help if the context cannot reach it. Memory is a hierarchy, and context that does not fit in a faster tier has to sit in a slower one:
* HBM sits next to the accelerator. It is the fastest tier and the most expensive per bit.
* DRAM is the server’s main memory. It is larger and slower.
* Flash (NAND, the chips in SSDs) is slower again and much cheaper per bit.

### Training and Inference are the Two Jobs

Training is building the model: compute is applied to data so the model learns patterns. It happens before deployment and is paid for up front.

Inference is using the model. It happens every time, and it is paid for every time.

Inference has two stages. Prefill processes the prompt and is limited by compute. Decode generates the response one token at a time and is limited by memory bandwidth, so decode is usually the constraint. Three things explain why:
* To produce each token, the accelerator has to read the model's weights and the session's context from memory, and does only a small amount of math on each piece before moving on. Its compute cores, the units that do the math, spend much of their time waiting on memory.
* That is an imbalance between compute and memory bandwidth. Compute has grown far faster than the speed at which memory can feed it, and that doesn't seem to be changing.
* Training avoids the imbalance by processing very large batches, so each read of memory feeds a lot of math. Inference serves requests one at a time unless they are grouped, so the imbalance shows up there.

This changes the economics of software. Traditional software costs almost nothing to serve one more user. AI applications pay for inference on every use, so cost scales with usage and margins depend on what inference costs.

### Physical Infrastructure Maximizes Accelerator Utilization

Accelerators, which are designed to do massive amounts of specialized math simultaneously, perform the computations. They hold context in memory and run the math against it. GPUs and custom ASICs (e.g., TPUs) are two forms.

An accelerator needs three things working together: cores to execute the math, memory to hold weights and state, and interconnect to move data in and out. Utilization is set by whichever of those is slowest. Software sets how much of that is reached, since accelerators do not hit their rated throughput without kernels, compilers, and serving frameworks built for them. An accelerator therefore cannot be judged apart from the system around it: cost per token is set by the system, not the chip alone.

Software maturity varies by chip and keeps improving, so performance at one point in time may understate what a chip can reach later. That applies to every chip, including Nvidia, but the gap is likely larger for chips with newer software ecosystems.

Accelerators are the most expensive part of the stack, so an idle one is the cost. Everything else in physical infrastructure exists to keep them busy. Data centers house them. Power runs them. Cooling removes their heat so they do not throttle. Networking connects them so they can work as one system instead of waiting on each other. CPUs run the software around them, including the orchestration and tool calls that agents depend on.

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

Infrastructure is further along than applications, and within infrastructure, physical is further along than digital. Adoption therefore trails the stack: applications depend on infrastructure that is still being built, so adoption is early. None of it is late.

### The Model Layer is Diversifying

AI is still largely synonymous with LLMs, and within LLMs, with frontier models. But image, video, vision, vision-action, and world models are all in use, and within any type, models vary in size, cost, context, and where they can run. 

Users are exploring rather than defaulting to the frontier. They are looking for a workable mix of capability, cost, and privacy. Examples include:
* Open-source versus closed.
* Local models, which run on a user’s own hardware. Efficiency techniques like quantization, sparse activation, and MoE make them more practical, and the hardware for running them is improving.
* Cheaper models from outside the frontier labs (e.g., Kimi, DeepSeek), which some startups already use because they cost less and are not much worse.

Taken together, these point to general capability commoditizing: open-weight models have closed much of the gap and cap what labs can charge for it. Where models are close substitutes, requests can be routed to whichever fits best on cost, complexity, and domain. Providers then compete to be the one chosen, which may push prices down.

Enterprises are going a step further. Rather than choosing among general models, they are building their own on their own data. A frontier model knows what is public; it does not know how a particular company works.

### Task-Specific Data Is the Scarce Input

Proprietary data is valuable right now. General models have absorbed what the internet offers, so what improves performance on a specific task is the data held by whoever does the work, hosts the work, or collects it on purpose. Because foundation models are still the default, the user has to supply the task context, and it does not persist. 

Data originates with the people doing the work: a law firm, a hospital, a manufacturer. They hold both the output and the reasoning behind it, and they are using it to build and augment their own models. Holding the data is not the same as being able to use it. Enterprise data is often messy and not agent ready, so usable data is scarcer than data that exists.

Vertical software companies hold data as a byproduct, since the work runs inside their systems (e.g., Tyler, Agilysys). Because that data is generated inside software, it may be more structured than what enterprises hold, and so closer to agent ready. 

A third industry is forming to build it deliberately (e.g., Mercor). These companies supply traces, the reasoning behind expert work rather than the output, to the labs.

### Inference (and Cost) is the Central Concern

Inference is where cost and capacity pressure accumulate as usage grows. Decode is the main issue. Serving also gets more complex as the number of models and accelerators grows, since inference runtime software has to route each request to a model and an accelerator based on factors like cost, availability, and latency. Solutions are being pursued at every layer: model architecture and compression, inference runtime software (e.g., vLLM, SGLang, TensorRT-LLM), chip design, and data center design. Software is likely the fastest and cheapest of these, since it gets more throughput from existing chips instead of waiting on new ones (e.g., software updates and retuning alone raised throughput on the same AMD chip several-fold in three months). 

Cost per token is falling through efficiency gains within existing designs, which are significant but not drastic. A drastic decline would require a change in supply or design: more accelerators coming online as data centers are finished, a new base architecture, or new accelerator designs. In the meantime, the marginal gains come from both digital and physical infrastructure:
* **Digital**
  * Architectures, such as MoE, that use less compute and memory.
  * Compression, which shrinks the model and the data being moved.
  * Smaller task- or domain-specific models, which need less compute because general models carry more than a given task needs.
  * Inference runtime software, which batches requests and routes each one to the model and chip that fits it on cost, complexity, domain, and availability.
  * Caching, which reads back what the model has already computed for a repeated prompt instead of recomputing it. Providers charge less for cached input tokens.
* **Physical**
  * Networking, which moves data faster so chips wait less on each other.
  * Cooling, which keeps chips from throttling.
  * Mixed fleets, which use different chips for training, prefill, and decode, since their compute and memory needs differ.

Accelerator prices remain elevated on demand, and frontier models are too expensive for most applications to run profitably. Demand keeps climbing regardless. Agents consume far more tokens per task than chat does, and agentic adoption is early, so the mix is still shifting toward the expensive workload. However, prices may decrease if accelerators that have already been bought but not yet deployed come online, since providers with spare capacity may compete for routed workloads on price and other terms.

### The Accelerator Layer is Diversifying

Training was one problem, and it favored one accelerator: the fastest. Inference is many problems. Models differ widely in size, contexts in length, and users in how fast they need a response, so chat, agents, batch jobs, and latency-sensitive traffic stress the machine in different places.

Accelerators are specializing in response, as models are (e.g., Nvidia pairing GPUs for prefill with a separate accelerator for decode). Performance is a property of the system, not the accelerator, so no single design is likely to dominate every workload, and mixed fleets are likely to be the default. The added complexity of running several accelerator types may limit how far this goes.

Startups are also building new designs that could change things drastically (e.g., Cerebras, Etched). Few have taken real share yet, GPUs remain the default by a wide margin, and deployment at scale could take a while.

### Every Physical Constraint Shows Up as an Idle Accelerator

Physical constraints leave accelerators idle in three ways:
* **Deployed, but below full utilization**. Most deployed accelerators, including Nvidia GPUs, run below full utilization in practice. Memory leaves cores waiting on data, weak networking leaves chips waiting on each other, CPU-bound work leaves them waiting on the host, heat forces throttling, and missing power leaves chips unused.
* **Bought, but not yet deployed**. Some accelerators sit in inventory because the data center they are meant for is not ready, whether because the building is unfinished or because power, cooling, or networking is not yet in place.
* **Wanted, but not yet made.** Foundry capacity limits how many accelerators can be built.

Accelerator supply starts at the foundry. Leading-edge wafers and advanced packaging, the step that joins each accelerator to its memory, are both tight, and packaging is reportedly the narrower of the two. Both are concentrated at a single supplier, so capacity is hard to add elsewhere quickly

Memory is the hardest constraint to relieve with hardware, in part because compute has outgrown memory bandwidth and that doesn’t seem to be changing. Bandwidth, not compute, sets how fast tokens can be generated in decode, and capacity sets how much context a chip can hold. Demand for both is likely to keep growing as systems retain and reuse more context: agents carry memory across sessions, and caching stores earlier computation instead of recomputing it. High-bandwidth memory addresses both, but supply has not kept up with demand and prices have stayed high. Other responses, in rough order of how soon they help:
* Software and model architecture, the near-term fix, since they reduce how much memory each token needs (e.g., quantization, cache compression, MoE).
* More memory tiers. Context that does not fit in HBM can sit in DRAM or flash (e.g., Nvidia's CMX, which adds a flash tier for cached context).
* Higher utilization through cluster layout and networking. Existing chips can be arranged and linked differently, such as racks built for memory and racks built for compute, so cores wait less on data.
* New chip designs that are more efficient. GPUs remain the default by a wide margin, but the field is widening beyond the chips best suited to training.

The shortage is therefore not limited to HBM. Context pushed down the tiers adds demand for DRAM and flash, and suppliers have put capital into HBM and DRAM and added little NAND capacity, so DRAM and NAND are tight as well.

Networking is being extended up, out, and across:
* **Scale up** links chips within a rack so they act like one larger accelerator. It runs largely on Nvidia's proprietary NVLink today, with open alternatives, including UALink and Ethernet-based designs, competing for it.
* **Scale out** links racks across the data center. It uses both Nvidia's InfiniBand and Ethernet, and has been moving toward Ethernet.
* **Scale across** links data centers, since a single site can run out of power. It is mostly Ethernet-based.

Copper still handles most connections within a rack and is strongest at short reach, but it runs into distance and heat limits as racks get denser. Optical moves data as light, carrying more with less latency and heat, and most connections beyond a rack already run on it. Optical replacing copper within the rack is not a foregone conclusion, though. It has been the next thing for a while, and several approaches are likely to coexist: copper at short reach, pluggable optics, which are today's standard, and newer designs that put the optics next to or on the chip, known as near-packaged and co-packaged optics (CPO). The newer designs may not reach large scale until 2027 to 2028 or later.

Agents also lean on CPUs. Orchestration, tool calls, code execution, and API requests run on CPUs, and an accelerator can sit idle while it waits for them. As agent use grows, demand for CPUs is likely to grow with it, and server CPU supply has tightened, with price increases and long lead times reported.

Cooling is shifting to liquid, gradually. Air is the default, but as accelerators are packed more densely and run hotter it struggles to keep up. Liquid removes heat at the chip and sustains higher density, but it is a system, and it sits alongside air rather than replacing it:
* A system, not a single product: the racks, with cold plates on the chips; coolant distribution units (CDUs) and pumps that move the liquid; and heat rejection that carries the heat out of the building.
* Alongside air: equipment that is not cooled at the chip, such as networking gear and power supplies, still needs air, so many facilities use both. 

Power limits how many accelerators can run, and natural gas is the only source that reliably supplies it now. The usual route, connecting a new data center to the electric utility, can take years and delay projects, so some developers generate power on site with gas. Even gas is constrained, since processing, gathering, and transmission infrastructure is insufficient for cost-effective deployment, and on-site generation still needs a last-mile connection from a main pipeline, which can take a year or more. 
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

Cost predictability is a second brake on adoption. Because models are probabilistic, identical tasks can take different numbers of steps and cost very different amounts, and spend that scales with usage is hard to forecast. Cheaper tokens do not fully solve this, since agents use far more of them, so enterprises may hold back until they can predict and cap what agents spend.

Carrying context across a long task makes serving agents a different problem than serving software. Sessions run for minutes or hours rather than milliseconds, capacity cannot be added or removed freely, and a failure loses the work rather than just the request. Cloud providers are rearchitecting around this, and agent runtime software is the layer being built to keep agents running through failures.

Carrying context across sessions also means memory has to persist. Retaining more context adds infrastructure cost, and storage is only part of the problem: memory is useful only if the right prior context is retrieved at the right moment. Databases built for transactions and batch queries may need to adapt to serve it, and newer structures such as vector databases, which retrieve by similarity, and knowledge graphs, which store the relationships between pieces of information, are also used for it.

Using tools means acting on a world built for humans. New protocols are emerging to let agents do what they cannot natively:
* Communicate with each other (e.g., A2A).
* Execute transactions (e.g., x402 for payments, UCP for what commerce actions mean to an agent). Micropayments are only viable if transactions get cheaper, which is why new payment protocols are being pursued.
* Work with websites (e.g., NLWeb, WebMCP). websites).

Agents act on software through APIs, so software that exposes comprehensive access gets used by agents and software that does not gets routed around. MCP has become the leading protocol for that exposure, and adoption is already deep in large enterprises, but agents call ordinary APIs too, so MCP adds to APIs rather than replacing them.

### Incumbents Are Leading the Buildout (for Now)

Companies that existed before 2023 are both funding the buildout and supplying it. A handful of hyperscalers are putting up most of the money. A wider set of incumbents is selling into it, because they already have the manufacturing, the relationships, the products, the data, and the software. 

New technology does not mean new companies. Much of the new technology in the buildout (e.g., liquid cooling, optical networking, agentic infrastructure) is being brought to market by existing companies extending what they already sell, not by startups.

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

Inference cost is the constraint on the business model because applications pay for every use. Token prices from the leading labs have stopped falling, and token costs are unlikely to fall much soon because GPU costs are not falling. Until the economics work, the better application is not necessarily the better business. Application providers are responding in two ways:
* The first is switching to alternative models from outside the frontier labs (e.g., Kimi, DeepSeek), which offer lower token prices, so margins may improve even if token costs do not fall quickly.
* The second is focusing on a task or domain (e.g., Cursor for coding), where a higher return per use may support higher prices and justify not being replaced by a foundation model. Task- or domain-specific models offer higher quality output with fewer inputs, and likely start with a well-defined task where AI enables capabilities beyond a human’s, such as 24/7 work, analysis of far more data, and pattern recognition.

### Physical AI is Coming, but Still Needs Time

Robots are becoming smarter with AI. Robotics excitement has grown because language and vision models lowered the barrier to training robots. For now, these models are more likely to serve as the brain for existing machines (e.g., predictive maintenance, inspection, autonomous process control, material movement) than to power entirely new ones, and the machines that get deployed are more likely to go into existing enterprise applications like manufacturing than into new categories. Several models act as the brain:
* A world model understands the laws of physics. Instead of predicting the next word in a sentence, it predicts the next frame of a video, which lets the machine anticipate the physical consequences of an action.
* An LLM reasons through what needs to be done.
* Vision-action models translate that reasoning into physical, mechanical execution.

Driving, product design, manufacturing, and warehouse operations are where it is showing up.

Robotics has many more dimensions than language or vision, which makes the models harder to build. And the constraints go beyond the models. Hardware to sense and act on the physical world is expensive and slow to iterate. Errors are not reversible, which raises the reliability bar. And there is no public equivalent to the internet data that trained language models. World models, video, and simulation are being explored as substitutes, but the robots themselves during deployment are the most likely source at scale.

World models, and possibly foundation models for robotics, are what could broaden physical AI beyond its current applications. A foundation model lets a robot pick up new tasks with limited training, which is what widens the range of uses. As with software, the return is likely higher for models trained on a specific environment.

-------------------------

## Investment Implications

### Buy the Physical Bottlenecks

A bottleneck is worth owning until it is solved, and the price already contains a guess about when that happens. The position is the difference between that guess and the truth. There are currently seven major constraints in the physical supply chain. Most are supplied by existing companies, even where the technology is new (e.g., liquid cooling, optical networking), so the positions can be taken today:
* **Natural gas and its supply chain**. Power limits how many accelerators can run, and gas is the only source that reliably supplies it now. The processing, gathering, and transmission infrastructure is as much the trade as the gas itself, since that is where the shortage sits.
* **Cooling, especially liquid**. Density keeps rising and air cannot keep up at the chip. Liquid removes heat at the chip and sustains higher density. Adoption is gradual, which makes the demand long rather than spiky. Liquid cooling is a system, so the exposure spans the racks and cold plates, the coolant distribution units and pumps, and heat rejection.
* **Networking, especially optical**. Most connections beyond a rack already run on light, and scale out and scale across keep adding links. More deployment means more connections beyond the rack regardless of whose silicon is in the racks. Two things are less certain:
  * Optical inside the rack. Copper keeps short reach, and the newer designs may not reach large scale until 2027 to 2028 or later.
  * Where the value sits. It may be in scarce optical IP more than in assembling modules, but the pieces differ by design. Lasers are needed by every optical design, silicon photonics may gain under co-packaged designs, and DSP chips are tied to pluggables, which co-packaged designs would largely remove.
* **Accelerators broadly**. Mixed fleets are likely to be the default, and an accelerator cannot be judged apart from the system around it, so picking the winning accelerator matters less than owning the growth in accelerators bought. Nvidia, the custom-silicon designers, and the hyperscalers building their own can all be held for the same reason. A nearer-term risk is that more accelerators have been bought than are in service. Prices today reflect the accelerators running, not those waiting to be installed, so when they come online, scarcity could ease and future purchases could be lower.
* **CPUs**. Agents run orchestration, tool calls, and code execution on CPUs, so demand follows agent adoption, which is still early, and not only accelerator volume. Server CPU supply has tightened. Nvidia, AMD, Intel, and Arm-based designs all supply them, so, as with accelerators, the bet is likely on volume more than on who wins.
* **Wafers and advanced packaging**. Every accelerator needs both, whoever designs it, so the exposure does not depend on which accelerator wins. Both are tight and concentrated at a single supplier, so capacity is hard to add elsewhere quickly.
* **Memory**. Bandwidth sets how fast tokens can be generated in decode, and capacity sets how much context a chip can hold. High-bandwidth memory (HBM) addresses both, and supply has not kept up with demand. Demand is likely to keep growing as systems retain and reuse more context, through agent memory and caching. HBM leads, but the exposure is wider, since context that does not fit in HBM moves down the tiers:
* DRAM, where supply is also tight, since suppliers have put capacity toward HBM.
* Flash, where demand is growing as AI servers use more enterprise SSDs and context storage, and suppliers have added little NAND capacity because DRAM and HBM earn higher margins.

Each of the seven ends for a different reason. Four things can end them:
* **Supply catching up**. New supply is slow where it needs fabs, plants, or construction. But some supply already exists and is not running: accelerators have been bought that are not racked, because power, shell, and cooling are not ready. Those come online without anything being built.
* **Technology change**. A new architecture or a different chip changes what is needed, which can end a constraint without relieving it. Gas is indifferent to both, since it is the raw input.
* **Density**. The buildout assumes compute keeps concentrating in large, dense sites. Gas, cooling, and networking are only needed there, since they exist to solve density. If inference spreads to smaller sites instead, those three are not bought, while accelerators, CPUs, memory, and wafers and packaging still are. On-prem and edge deployment is growing, and whether it reaches a scale that changes data center demand remains to be seen.
* **Software**. Software changes faster than chips, architectures, or physical supply, since the others require fabrication or construction. It cannot produce electricity or remove heat, so power and cooling sit outside its reach. It works on others: utilization on accelerators, bytes per token on memory through quantization and cache compression, and data movement on networking.



### Within Each Bottleneck, Find the Strongest and the Best-Priced

Do not buy something priced as if the bottleneck is permanent. A company earning shortage margins is being valued on earnings that do not survive the shortage, so the more inflated the margin, the more the price assumes the constraint never breaks. The margin is also what funds the attack on it; the most profitable constraint is the one with the most people working to remove it.

What you are selecting for is durability, at two levels. Start with the constraints that break later; for example, gas doesn't care which architecture wins or whose chip gets deployed. Then, within them, own the strongest companies: low cost, healthy financials, strong brands, real distribution. They hold up when supply catches up and competition arrives.

Tracking the constraint directly is sharper, but the data is often not public, and what is public can be wrong or talked up by the people selling into it. You will not see the break coming, so the position has to survive it without you. 

The capex break is the exception. The growth has to continue to justify both the prices and the capex, and unlike the physical constraints, that is reported quarterly.

### Own Agentic Infrastructure

Agents are where autonomy is showing up, and the layer serving them is being built now. Most of it is coming from incumbents extending what they already sell, which makes this ownable today in a way the applications are not.

**Task-specific data**. What an agent needs to act correctly rather than generically. It sits with whoever does the work, hosts it, or collects it on purpose. Much of it is messy and not agent ready, so companies that make it usable may benefit, either by cleaning, organizing, and structuring it, by making the databases it sits in usable by agents, or by already holding it in an organized form (e.g., vertical software companies).

**Trust**: security, identity, observability, and governance. The tools that secure agents, define who each one is and what it can access, record what it did, and limit what it can do, including what it can spend. The existing observability, security, and identity vendors are selling it.

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

* **Inference cost**. Applications pay for every use, and token costs are unlikely to fall much soon. Until the return per use supports the price, the better product is not the better business.
* **Access**. Nothing here is publicly traded. Listings, or acquisitions that put the exposure inside something that is.
* **Reliability**. Autonomy has arrived where outputs can be verified. The applications that scale next are the ones where that holds.

The first investable applications are likely to be task- or domain-specific, because they offer higher quality output with fewer inputs. They may start with a well-defined task where AI enables capabilities beyond a human’s, such as 24/7 work, analysis of far more data, and pattern recognition. Helping enterprises use their own data more effectively may be one of the first, since it draws on those capabilities. Early versions may wrap foundation models with persistent, task-specific context so users no longer supply it each time, with vertical models that build in domain knowledge following.

Existing software is the proxy until these conditions change. When they do, the rotation is out of infrastructure and into applications, because infrastructure eventually competes on price and applications are where the margin ends up.

### Plan for Slower Adoption

The safest assumption is that adoption comes in slower than assumed, which means demand may be delayed. Most of the slowdown comes from barriers, such as trust, data readiness, cost predictability, and infrastructure still being built, not from a lack of value. Under that assumption:

What holds up:
* Companies that remove the barriers, since the delay is what creates demand for them.
* The strongest, lowest-cost suppliers, which are best able to withstand the oversupply and price competition that slower demand can bring.
* Existing software, which may have more time to build or adopt AI before AI-native competitors become investable.

What is exposed:
* Positions priced for fast growth, including AI-native applications, which move later still.
* Scarcity positions, to the extent they depend on committed spending continuing.
* Anything funded by circular demand or expensive capital.

