
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

--------------------

### Prioritize Applications, Buy Infrastructure in the Meantime

**Applications are where the value ends up.** New technology breaks into two major sub-sectors, applications and infrastructure. The vast majority of value accrues at the application layer, which is where investments should ultimately be concentrated. Applications depend on infrastructure, which comes first.

**The first applications to gain traction are novel approaches to existing activities.** Applications initially get more traction by reinventing existing activities rather than inventing new ones: e-commerce reinvented mail-order catalogs, and LLMs are a substitute for web search. Once the technology is well-established, entirely new behaviors gain traction and become investable.

**Within infrastructure, identify the sub-sectors best poised for growth.** The primary purpose of infrastructure is to lower the cost of deployment for applications. The binding constraints on deployment are the most obvious areas for growth, and the ones to focus on are those that are hard to work around and can pay off in the near term. The growth lasts only while a constraint is binding, and the companies solving it eventually become commodities as constraints shift. Constraints shift for several reasons:
* Oversupply leads to price competition and lower margins.
* Solving one constraint can expose another.
* Changes in how applications serve customers change which pieces matter most (e.g., a shift from chat to background processes).
* Novel solutions can make existing constraints obsolete.

**Within those sub-sectors, identify the companies best positioned to benefit.** Start with the strongest, since they are best able to withstand oversupply. But even the strongest can experience huge price decreases when a constraint breaks, so look among them for those where the price does not already reflect all of the expected growth. Avoid companies priced as if the constraint is permanent.

--------------------

### Try to Be Early, But Definitely Don't Be Late

**Be early enough to enjoy growth.** Being right on the wrong timeline can be similar to being wrong. There are two ways to miss: being too early, so that a return is not available for years, or being too late. The ideal investment experiences sales growth in the near-term, which is about 2 years.

**Being late is the worst outcome, so start with the likelihood of growth.** The absolute likelihood of sales growth, regardless of timeline, is the starting point. Among sub-sectors and companies where growth is relatively certain, prioritize by the likelihood of that growth appearing in the near-term.

**The sweet spot is hard to hit because the timeline is hard to gauge, so be conservative.** It's easy to make the mistake of being too early in new technology. Adoption of applications at scale is usually not realized until well after the potential is visible, because the infrastructure takes time to build and people's behaviors need time to adapt. The mainstream narrative tends to run ahead of that build, so estimate the timeline for adoption more conservatively than it suggests.

**Once a position is right, hold it to ride the growth.** Being early only pays if the position is still held when the growth arrives, and the usual failure isn't bad analysis, it's giving up on the position before the payoff. If a position turns out to be too early, holding is usually the safest option, but it is worth reevaluating whether the growth is still coming.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## The Basics of AI

### Productivity is the Value Proposition, Autonomy is the Goal

**In its current form, AI is a productivity tool.** It provides a better ratio of outputs to inputs. This can mean fewer inputs, more outputs, and/or higher-quality outputs.

**Autonomy is the extreme end of the productivity spectrum.** Autonomous systems perform a variety of actions with limited (or zero) human input. The building blocks towards autonomy are the focus of AI development.

**Reliability is what limits autonomy.** Models are probabilistic, not deterministic: the same input can produce different outputs, and a wrong one looks like a right one. The output may not be wrong at all, just weaker than it could have been, and that is harder to catch. Autonomy therefore needs poor outputs to be either caught or tolerated, which is why it has arrived first where outputs can be verified and is likely to be more prevalent where the cost of errors is low. Even there, a system is only given autonomy as far as it can be trusted, which takes controls around it, not just a powerful model.

--------------------

### Infrastructure and Applications are Both Digital and Physical

**AI infrastructure has two components:**
* Physical infrastructure is the hardware: accelerators, CPUs, racks, networking, power, and cooling.
* Digital infrastructure is the software and context: models, architectures, data, and protocols.

**AI applications split the same way.** An AI-native application is a user-facing product, purpose-built around a specific task, that uses AI as its core reasoning engine and ships with everything needed to complete that task out of the box:
* Digital applications work with information, such as text, images, and video.
* Physical applications understand and interact with the physical world, as in robots, autonomous vehicles, and industrial systems.

--------------------

### Context and Compute are the Fuel

**Compute is the processing power that lets AI models learn patterns and generate outputs.** Training spends it to learn patterns from data; inference spends it every time the model is used. It is the input you can buy, so it scales with money and with how fast data centers get built.

**Context is what the model works with, and a model is of little use for a task without it.** It takes three forms, and they behave differently:
* Training data is what the model learns from before it is deployed. General models have already absorbed the public internet, so what remains scarce is domain-specific data and traces, meaning the thinking behind the work rather than just the output. That sits with whoever does the work: end customers, data providers, and vertical software companies. Physical AI has no public equivalent to start from.
* Prompt context is what the model is given at the moment it runs. It is supplied by the user or the application, and it is the difference between a generic answer and a correct one.
* State and memory are what a system carries across a task and across sessions, such as history and preferences. They are not sourced, they accumulate as the system runs, and they have to be stored and retrieved, typically in databases.

**The industry assumes scale works.** More compute and more data produce better models, predictably, and that has held over several orders of magnitude. That assumption is what justifies the spending. It is an empirical observation, not a law, and architecture is the most likely thing to break it.

**In practice, compute and context are bound together by memory.** Every token generated requires fetching context, so compute sits idle whenever it cannot be fetched fast enough. Memory comes in tiers that trade speed for capacity, and context that does not fit in the fastest tier has to sit in a slower one, so where context sits sets how quickly it can reach compute:
* HBM sits next to the accelerator. It is the fastest tier and the most expensive per bit, and it holds the least.
* DRAM is the server's main memory. It is larger and slower.
* Flash (NAND, the chips in SSDs) is slower again and much cheaper per bit.

--------------------

### Training and Inference are the Two Jobs

**Training is building the model.** Compute is applied to data so the model learns patterns. It happens before deployment and is paid for up front.

**Inference is using the model.** It happens every time, and it is paid for every time. It has two stages: prefill processes the prompt and is limited by compute, and decode generates the response one token at a time and is limited by memory bandwidth, so decode is usually the constraint. Three things explain why decode is limited by memory bandwidth:
* To produce each token, the accelerator has to read the model's weights and the session's context from memory, and does only a small amount of math on each piece before moving on. Its compute cores, the units that do the math, spend much of their time waiting on memory.
* Accelerators have gained compute speed far faster than memory has gained bandwidth, so the gap between how fast they can do math and how fast memory can supply the data keeps widening, and that doesn't seem to be changing.
* Training avoids the gap by processing very large batches, so each read of memory feeds a lot of math. Inference serves requests one at a time unless they are grouped, so the gap shows up there.

**Inference changes the economics of software.** Traditional software costs almost nothing to serve one more user. AI applications pay for inference on every use, so cost scales with usage and margins depend on what inference costs.

--------------------

### Physical Infrastructure Maximizes Accelerator Utilization

**Accelerators are the hardware that delivers compute.** Training and inference both rely on specialized math, which an accelerator performs in parallel, with many operations running at once. It keeps the model's weights and the context it is working on in memory, and runs that math against them. Main forms of accelerators include GPUs, which are general-purpose, and custom ASICs, which are built for specific workloads (e.g., TPUs).

**An accelerator's performance, which dictates its cost per token, is set by the system around it.** An accelerator needs three things working together, and its utilization is set by whichever is slowest:
* Cores to execute the math.
* Memory to hold weights and state.
* Interconnect to move data in and out.

Software decides how much of that capability is actually used. An accelerator does not reach its rated throughput without kernels, compilers, and serving frameworks built for it. That software keeps improving, so a measurement taken at one point in time may understate what the accelerator can reach later. The gap applies to every accelerator, including Nvidia's, but it is likely larger for those with newer software ecosystems.

**Accelerators are the most expensive part of the stack, so an idle accelerator is the most expensive waste.** Everything else in physical infrastructure exists to keep accelerators running:
* Data centers house them.
* Power runs them.
* Cooling removes their heat so they do not throttle.
* Networking connects them so they can work as one system instead of waiting on each other.
* CPUs run the software around them, including the orchestration and tool calls that agents depend on.

--------------------

### Digital Infrastructure Makes Models Useful

**Digital infrastructure has two layers: the model, and everything around it.** A model is any system trained to produce outputs from patterns in data. LLMs are one type. Image, video, vision, vision-action, and world models are others. Within a type, models vary in size, cost, context, and where they can run.

**Architecture determines what a model can do and how much compute and memory it needs.** The transformer is the basis for today's foundation models. A new base architecture would change things drastically. Until then, efficiency comes from changes that make the transformer cheaper to run, such as mixture of experts and sparse attention, which reduce the compute and memory used per token.

**A model on its own only produces outputs, so everything around it is what turns those outputs into work.** Some of the major components of that surrounding layer include:
* **Harnesses**, which manage memory, interfaces, and tool execution.
* **Runtime software**, which keeps models and agents running in production: it decides how requests are batched, served, and routed, and it runs agents, isolating the code they run and saving their state so a failure does not lose the work.
* **Trust**, which covers who a system is (identity), what it can access (security), what it is allowed to do (governance), and whether anyone can see what it did (observability).

**That surrounding layer has to change as systems become autonomous, which breaks three assumptions most software makes:**
* **Most software is stateless:** each request is handled independently, with no memory of prior requests, which makes it easy to scale up or down on demand ("elastic"). Autonomous systems are stateful. They retain information between requests, so requests must be routed back to the infrastructure that holds their state.
* **Most software is deterministic:** the same input produces the same output. Models are probabilistic, so outputs vary, and cloud infrastructure may need to adapt to that. Early use cases mostly involve verifiable tasks, which behave more like deterministic systems, so the change may come gradually. Observability and governance stay critical either way.
* **Most software is built for humans to operate.** Autonomous systems have to act in that world, so new protocols are needed for them to communicate with each other, execute transactions, and more (e.g., A2A for agent-to-agent communication). At the same time, the human-facing world is adapting to non-human actors, with websites, software, and payment providers becoming operable by systems as well as people.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

## The Current AI Landscape

### The Sector Is Early

**AI is still being built out, and none of it is late.** Applications depend on the infrastructure beneath them, and both layers are still being adapted for AI:
* Physical infrastructure is furthest along, but is still being expanded to make AI cost effective. Some of its sub-sectors remain investable.
* Digital infrastructure is earlier, and is being adapted so systems can operate autonomously.
* Applications are earliest. Few exist yet, and the ones that do face barriers to adoption: reliability, trust, and cost.

--------------------

### The Model Layer is Diversifying

**AI is still largely synonymous with language models, and within them, with frontier models (e.g., ChatGPT, Claude).** But image, video, vision, vision-action, and world models are all in use, and within any type, models vary in size, cost, context, and where they can run.

**Users are exploring rather than defaulting to the frontier, looking for a workable mix of capability, cost, and privacy.** Examples include:
* Open-source versus closed.
* Local models, which run on a user's own hardware. Efficiency techniques like quantization, sparse activation, and MoE make them more practical, and the hardware for running them is improving.
* Cheaper models from outside the frontier labs (e.g., Kimi, DeepSeek), which some startups already use because they cost less and are not much worse.
* Models enterprises build themselves on their own data, rather than choosing among general models. A frontier model knows what is public; it does not know how a particular company works.

**Together, these options point to general capability commoditizing.** The gap between frontier and non-frontier models is narrowing. Where models are close substitutes, requests can be routed to whichever offers the best mix of capability, cost, and privacy, and providers compete to be the one chosen.

--------------------

### Task-Specific Data Is the Scarce Input

**Proprietary data is valuable because foundation models lack the context for a specific task.** They have already absorbed what the internet offers, so the missing context is not public. Until models are built on that data, the user has to supply it. Task-specific data comes from three places:
* **The people doing the work** (e.g., a law firm, a hospital, a manufacturer). They hold both the output and the reasoning behind it, and they are using it to build and augment their own models. Holding the data is not the same as being able to use it. Enterprise data is often messy and not agent ready, so usable data is scarcer than data that exists.
* **Vertical software companies**, which hold data as a byproduct, since the work runs inside their systems (e.g., Tyler, Agilysys). Because that data is generated inside software, it may be more structured than what enterprises hold, and so closer to agent ready.
* **A third industry, forming to build it deliberately** (e.g., Mercor). These companies supply traces, the reasoning behind expert work rather than the output, to the labs.

--------------------

### Inference (and Cost) is the Central Concern

**Inference is where cost and capacity pressure accumulate as usage grows, and decode is the main issue.** Decode is limited by memory bandwidth: to produce each token, the accelerator reads the model's weights and the session's context from memory, so its cores spend much of their time waiting. Each token therefore takes a lot of accelerator capacity for little math.

**Agents increase the decode load in two ways.** They generate far more tokens per task than chat does, so there are many more decode steps, and they carry long context across long tasks, so each step has to read more from memory. Agentic adoption is early, so this load is likely to keep growing.

**The decode load falls on the accelerators in service, which are scarce.** Prices remain elevated on demand and the cost of each token stays high. That is why frontier models are too expensive for most applications to run profitably.

**Efficiency gains lower the cost to serve each token by getting more tokens out of the accelerators already in service, significantly but not drastically.** They do it by cutting the compute and memory each token needs, sharing each read of memory across more requests, avoiding repeated work, or keeping accelerators from waiting. They come from both digital and physical infrastructure:
* **Digital**
  * Architectures, such as MoE, that use less compute and memory.
  * Compression, which shrinks the model and the data being moved.
  * Smaller task- or domain-specific models, which need less compute because general models carry more than a given task needs.
  * Inference runtime software (e.g., vLLM, SGLang, TensorRT-LLM), which batches requests and routes each one to the model and chip that fits it on cost, complexity, domain, and availability. This matters more as the number of models and accelerators grows.
  * Caching, which reads back what the model has already computed for a repeated prompt instead of recomputing it. Providers charge less for cached input tokens.
* **Physical**
  * Networking, which moves data faster so chips wait less on each other.
  * Cooling, which keeps chips from throttling.
  * Mixed fleets, which use different chips for training, prefill, and decode, since their compute and memory needs differ.

Of these, software is likely the fastest and cheapest, since it gets more throughput from existing chips instead of waiting on new ones (e.g., software updates and retuning alone raised throughput on the same AMD chip several-fold in three months).

**A drastic decline in the cost to serve each token would require a change in supply or design:**
* More accelerators coming online as data centers are finished. Prices may decrease if accelerators that have already been bought but not yet deployed come online, since providers with spare capacity may compete for routed workloads on price and other terms.
* A new base architecture.
* New accelerator designs.

--------------------

### The Accelerator Layer is Diversifying

**Inference has no single best accelerator the way training did.** Training is largely one kind of workload, large batches of parallel math limited by compute, and GPUs, which are built for that, became the standard. Inference workloads differ in model size, context length, and how fast the user needs a response, so chat, agents, batch jobs, and latency-sensitive traffic can each be limited by a different part of the system: cores, memory, or interconnect.

**Accelerators are specializing because inference workloads differ, as models are.** For example, Nvidia pairs GPUs for prefill with a separate accelerator for decode. Performance is a property of the system, not the accelerator, so no single design is likely to dominate every workload, and mixed fleets are likely to be the default.

**Startups are building new accelerator designs (e.g., Cerebras, Etched), drawn by the money at stake.** Spending is large enough that even small efficiency gains are worth a great deal. Inference workloads also differ, so a design that is best at one can find a market without beating GPUs at everything. Few have taken real share yet, GPUs remain the default by a wide margin, and deployment at scale could take a while.

--------------------

### Every Physical Constraint Shows Up as an Idle Accelerator

**Physical constraints leave accelerators idle in three ways:**
* **Wanted, but not yet made.** Foundry capacity limits how many accelerators can be built.
* **Deployed, but below full utilization.** Most deployed accelerators, including Nvidia GPUs, run below full utilization in practice. Memory leaves cores waiting on data, weak networking leaves chips waiting on each other, CPU-bound work leaves them waiting on the host, heat forces throttling, and missing power leaves chips unused.
* **Bought, but not yet deployed.** Some accelerators sit in inventory because the data center they are meant for is not ready, whether because the building is unfinished or because power, cooling, or networking is not yet in place.

#### Wafers and Advanced Packaging

**Wafers and advanced packaging limit how many accelerators can be made.** Leading-edge wafers and advanced packaging are both tight. Both are concentrated at a single supplier, so capacity is hard to add elsewhere quickly.

#### Memory

**Memory is difficult to relieve with hardware.** Memory feeds data to the accelerator's cores, and it constrains them in two ways:
* **Bandwidth**, how fast memory delivers data, sets how fast tokens can be generated in decode. Compute has outgrown memory bandwidth, so cores wait on data, and that doesn't seem to be changing.
* **Capacity**, how much memory can hold, sets how much context a chip can work with. Demand is growing as systems retain and reuse more context: agents carry memory across sessions, and caching stores earlier computation instead of recomputing it.

High-bandwidth memory (HBM) addresses both bandwidth and capacity, but supply has not kept up with demand and prices have stayed high. Many other levers are being pulled to relieve the memory constraint, including:
* Software and model architecture, which reduce how much memory each token needs (e.g., quantization, cache compression, MoE).
* More memory tiers. Context that does not fit in HBM can sit in DRAM or flash (e.g., Nvidia's CMX, which adds a flash tier for cached context). That moves demand down the tiers, and DRAM and NAND are tight as well: suppliers have put capital into HBM and DRAM and added little NAND capacity.
* Higher utilization through cluster layout and networking. Existing chips can be arranged and linked differently, such as racks built for memory and racks built for compute, so cores wait less on data.
* New chip designs that are more efficient.

#### Networking

**Networking keeps accelerators from waiting on each other, and it is being extended up, out, and across:**
* **Scale up** links chips within a rack so they act like one larger accelerator. Today it mostly runs on copper (e.g., NVLink, with open alternatives such as UALink competing for it). Optical is likely to enter first where scale up extends beyond a single rack.
* **Scale out** links racks across the data center. Connections beyond the rack mostly run on optical, over protocols such as Ethernet and InfiniBand, and it has been moving toward Ethernet.
* **Scale across** links data centers, since a single site can run out of power. It is mostly Ethernet over optical fiber.

**Whether optical replaces copper inside the rack is uncertain.** Copper is strongest at short reach, but it runs into distance and heat limits as racks get denser. Optical carries more with less latency and heat, and is already common beyond the rack. It has been the next thing for a while, and the shift is likely to be gradual, with several approaches coexisting:
* Copper, at the shortest reach.
* Pluggable optics, today's standard.
* Near-packaged and co-packaged optics (CPO), newer designs that put the optics next to or on the chip. They are reportedly shipping in some switches already, and are likely to reach large scale over the next few years, with use inside the scale-up domain later still.

#### CPUs

**Agents lean on CPUs, so CPU-bound work can leave accelerators idle.** Between model calls, orchestration, tool calls, code execution, and API requests run on CPUs, and an accelerator can sit idle while it waits for them. Demand for CPUs is likely to grow with agent use, and server CPU supply has tightened, with price increases and long lead times reported.

#### Cooling

**Cooling for accelerators is shifting from air to liquid as they are packed more densely and run hotter.** Air is the default way to cool data center equipment, but it struggles to remove heat as fast as dense accelerators produce it, and when heat builds up, chips throttle. Liquid removes heat directly at the chip, so it sustains higher density. The shift applies to the accelerators, not the whole facility, and it is gradual for two reasons:
* **Liquid cooling is a system, not a single product.** It takes racks with cold plates on the chips, coolant distribution units (CDUs) and pumps that move the liquid, and heat rejection that carries the heat out of the building.
* **Air still cools much of the facility.** Equipment that is not cooled at the chip, such as networking gear and power supplies, still needs air, so many facilities use both.

#### Power

**Power limits how many accelerators can run, and natural gas is the only source that reliably supplies it now.** New power needs a source that generates it reliably and a way to deliver it to the data center. Delivery is usually through the electric utility's grid, but connecting a new data center can take years and delay projects. Some developers therefore generate power on site, which skips the wait, and gas is the source that can do that now: it can be deployed at the site and runs constantly. However, gas faces its own constraints:
* **Capacity to move gas:** processing, gathering, and transmission infrastructure is insufficient for cost-effective deployment.
* **Reaching the site:** on-site generation still needs a last-mile connection from a main pipeline, which can take a year or more.

**Other power sources are further out than gas.** Alternatives include nuclear, solar, batteries, and advanced geothermal. Of these, advanced geothermal may have the most potential in the near term:
* **Advanced geothermal** runs constantly, like gas, with zero emissions, and reuses existing oil and gas drilling equipment.
* **Nuclear** is not a five-year solution: existing plants are limited, new ones take years, and newer reactor designs are not yet proven at scale.
* **Solar and batteries** are both getting cheaper on the hardware, but land, transmission, and storage at scale are not.

--------------------

### Agents Are Autonomy in Practice, and Digital Infrastructure Is Being Built Around Them

**An agent acts where a chatbot answers, and each way it acts creates a need that existing infrastructure was not built for:**
* **Makes decisions**, so it needs controls that make it trustworthy and costs that can be predicted.
* **Carries context** across a long task and across sessions, so it needs infrastructure built for long-running work that holds state, and memory that persists.
* **Uses tools and accesses data**, so it needs protocols to communicate, transact, and fetch the data it needs.

#### Trust and Cost

**Agents can only be given autonomy to the extent they can be trusted, and the controls that provide that trust are still being built.** Models are probabilistic, so errors compound across a long task and an agent's output cannot be assumed correct. Until the controls are in place, adoption may lag. Trust has four parts:
* **Identity:** each agent needs its own credentials, so it is a non-human identity, and who it is has to be defined.
* **Security:** agents hold access to sensitive systems and data, so a compromised or misbehaving agent can do real damage.
* **Governance:** what an agent is allowed to do, including how much it can spend, has to be limited.
* **Observability:** someone has to be able to see what an agent did and what it cost.

**Autonomy also makes cost hard to predict.** An agent decides how many steps a task takes, so identical tasks can cost very different amounts. Agents also use far more tokens than chat does, so total spend is hard to forecast. Companies are now more cost conscious after recent tokenmaxxing (encouraging employees to use as many tokens as possible), so enterprises may hold back until they can predict and cap what agents spend.

#### Runtime and Memory

**Carrying context across a long task makes serving agents a different problem than serving software.** Cloud providers are rearchitecting around it, and agent runtime software is the layer being built to keep agents running through failures by saving their state. Ordinary software handles short, independent requests, and agents differ in three ways:
* **Sessions run long.** They last minutes or hours rather than milliseconds.
* **Capacity cannot be added or removed freely.** An agent's state sits on the machine running it, so requests have to return there.
* **A failure loses the work,** not just the request.

**Agents that carry context across sessions need memory that persists.** Retaining more context adds infrastructure cost, and the harder problem is retrieval: memory is useful only if the right prior context is retrieved at the right moment. Databases built for transactions and batch queries may need to adapt, and newer database structures are built for retrieval. Examples include:
* **Vector databases,** which retrieve by similarity.
* **Knowledge graphs,** which store the relationships between pieces of information.

#### Protocols and APIs

**New protocols are emerging to let agents act in a world built for humans.** Agents need to be able to do several things there, and protocols are emerging for each:
* Communicate with each other (e.g., A2A).
* Execute transactions (e.g., x402 for payments, UCP for what commerce actions mean to an agent). Micropayments are only viable if transactions get cheaper, which is why new payment protocols are being pursued.
* Work with websites (e.g., NLWeb, WebMCP).
* Use tools and access data (e.g., MCP, which has become the leading protocol for this, with deep adoption in large enterprises).

**In an agentic world, software and data that are easier for agents to use get more usage.** Companies can make themselves more accessible by adopting these protocols, or by making existing data more accessible, for example through well-built APIs, which agents call directly too.

--------------------

### Incumbents Are Leading the Buildout (for Now)

**Companies that existed before 2023 are leading the buildout:**
* **Funding:** a handful of hyperscalers are putting up most of the money.
* **Supplying:** a wider set of incumbents sells into the buildout, across physical and digital infrastructure. They already have the manufacturing, the relationships, the products, the data, and the software. Hyperscalers sell into it too, so they sit on both sides of the spending.

**New technology does not mean new companies.** Much of the new technology in the buildout (e.g., liquid cooling, optical networking, agentic infrastructure) is being brought to market by existing companies extending what they already sell, not by startups.

**New companies are entering the buildout, and are likely to help commoditize infrastructure over time.** The money involved is drawing them in, since even small efficiency gains are worth a great deal at this scale. Few have taken real share yet, though some are making headway (e.g., Cerebras). As they gain share, they compete on price, which is how infrastructure margins come down.

--------------------

### Earnings are Real, Sustainability is Uncertain

**Prices for many of the major companies have risen with earnings, not ahead of them.** That is not the usual bubble pattern. But three things make it uncertain how durable those earnings are:
* **Circular demand.** The major companies buy from each other, invest in each other, and commit to each other's capacity (e.g., Broadcom's reported loan to Anthropic, which buys its chips), so a share of what looks like end demand is the group paying itself. How much is unknown.
* **Unclear real demand.** Some of the recent token revenue came from tokenmaxxing, enterprises pushing usage for its own sake rather than for work. That has turned as buyers get cost conscious, so recent growth rates overstate the baseline, and with agentic adoption still early, how durable the real demand is remains unclear.
* **More expensive funding.** The funding has moved down the capital curve: operating cash flow first, then debt, and now equity and off-balance-sheet structures. Each step costs more and leaves less room. With the amount being spent so large and the return and real demand still unclear, funding is getting more expensive (e.g., CoreWeave's recent loan, reportedly priced wider than its earlier ones). At some point the spending has to be supported by cash the assets generate.

--------------------

### AI-Native Applications Are Early

**AI-native applications are early.** These are user-facing products purpose-built around a specific task that use AI as their core reasoning engine, not the foundation models themselves. They are appearing first by reshaping existing activities:
* **Content generation** (text, image, video), since the output is the product.
* **Coding**, since the output can be checked.
* **Web search**, which foundation models and search APIs built for AI are substituting for.
* **Web and app design.**
* **E-commerce**, likely next, since it is a transaction an agent can carry out.

**Traction is concentrated in a few standouts, and in practice none of them are publicly traded.** Cursor, Midjourney, and Lovable are known within the field, but day-to-day use is still mostly inside the foundation models themselves, so there is little to own directly today.

**Inference cost limits whether an application can scale profitably.** Early on, funding, building the product, and getting adoption come first. Inference cost arrives with success, because an application pays for every use, so its cost grows with its usage. Token prices from the leading labs have stopped falling, and token costs are unlikely to fall much soon because GPU costs are not falling. There are two ways to widen the margin:
* **Lower the cost.** Startups are already switching to cheaper models from outside the frontier labs (e.g., Kimi, DeepSeek), so margins may improve even if token costs do not fall.
* **Raise the price.** A higher price has to be justified by a higher return for the customer, and focusing on a task or domain is how an application offers one (e.g., Cursor for coding). Task- or domain-specific models offer higher quality output with fewer inputs, and likely start with a well-defined task where AI enables capabilities beyond a human's, such as 24/7 work, analysis of far more data, and pattern recognition.

--------------------

### Physical AI is Coming, but Still Needs Time

**Robots are getting smarter because AI models have made them easier to train.** The brain is several models working together:
* A world model understands the laws of physics. Instead of predicting the next word in a sentence, it predicts the next frame of a video, which lets the machine anticipate the physical consequences of an action.
* An LLM reasons through what needs to be done.
* Vision-action models translate that reasoning into physical, mechanical execution.

**For now, these models are more likely to serve as the brain for existing machines than to power entirely new ones.** The machines that get deployed are more likely to go into existing enterprise applications than into new categories. It is showing up in driving, manufacturing, and warehouse operations (e.g., predictive maintenance, inspection, autonomous process control, and material movement).

**Several constraints explain why physical AI is limited to existing machines for now:**
* **Models** are harder to build, since robotics has many more dimensions than language or vision.
* **Hardware** to sense and act on the physical world is expensive and slow to iterate.
* **Errors** are not reversible, which raises the reliability bar.
* **Data** has no public equivalent to the internet data that trained language models. World models, video, and simulation are being explored as substitutes, but the robots themselves during deployment are the most likely source at scale.

**Better models could broaden what physical AI is used for.** World models, and possibly foundation models for robotics, could ease the model and data limits. A foundation model lets a robot pick up new tasks with limited training, which is what widens the range of uses. As with software, the return is likely higher for models trained on a specific environment.

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

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

