
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

### Own Infrastructure Now, Rotate to Applications Later

**Hold infrastructure while its constraints bind, and rotate to applications as they ease.** Applications are held back by constraints that take time to ease. Infrastructure earns while it removes them, and then competes on price, which is why the margin ends up in applications.

**Plan for slower adoption.** The narrative runs ahead of the constraints, which take time to ease, so adoption is likely to come in slower than expected. Positions priced for fast growth are the most exposed, and AI-native applications, which depend on the most constraints easing, move later still.

**The main constraints on applications are the ones that infrastructure removes.**
* **Cost to serve.** Inference is paid per use and capacity is limited. It eases as data centers come online and efficiency gains accrue.
* **Trust, reliability, and cost predictability.** Autonomy needs controls, and enterprises may hold back until they can predict and cap spend. It eases as the controls get built.
* **Data readiness.** Enterprise data is often messy and not agent ready. It eases as that data gets cleaned and structured.
* **Physical limits.** Machines with brains are limited by models, hardware, irreversible errors, and a lack of public data. It eases as models improve and machines in the field generate data.
* **Access.** AI-native applications are private. It eases through listings or acquisitions, and until then existing software is the stand-in.

**The first investable applications are likely to be task- or domain-specific.** They offer higher-quality output with fewer inputs, and helping enterprises use their own data more effectively may be one of the first. Early versions may wrap foundation models with persistent, task-specific context so users no longer supply it each time, with vertical models that build in domain knowledge following.

--------------------

### Buy the Physical Bottlenecks That Stay Binding

**Physical constraints are worth owning only while they bind, and the price already assumes when that ends.** Over the next year or two, the question is which ones keep binding. There are six that keep accelerators from being made, deployed, or fully used (wafers and advanced packaging, memory, networking, CPUs, cooling, and power), and they are not equally worth owning. Within the constraints worth owning, pick the strongest companies at prices that do not assume the shortage is permanent.

#### The Fewer and Harder the Levers, the Better the Constraint

**The constraints worth owning have few levers, and hard ones.** A lever is something a customer can do to get around a constraint, and there are three kinds:
* **Get more of it.** New capacity is the hardest, since it takes fabs, plants, pipelines, or construction. Idle supply that already exists coming online is easier.
* **Use less of it.** Efficiency gains (e.g., efficient architectures, compression, caching, smarter routing) get more tokens from each accelerator, watt, and byte moved. They are the fastest and cheapest lever, but the gains are significant, not drastic, and they act most directly on memory, networking, and CPUs.
* **Use something else.** An existing solution can last longer than expected (e.g., copper, air cooling, the grid), which slows adoption of the newer one.

#### Data Center Development Is the Swing Factor

**Whether data centers get built on time decides how long a constraint pays, and the reason for a delay matters.** Development can run on schedule, be delayed, or be cancelled:
* **A delay caused by the constraints themselves** (power, equipment, permits) supports those constraints. Revenue shifts later, but the shortage is real.
* **A delay caused by funding or weak demand** is worse, because it reduces spending instead of moving it.

#### How the Constraints Stack Up

**The constraints sit at two points in the buildout.** Upstream constraints (wafers and packaging, memory, CPUs) are bought when accelerators and servers are made, so they depend on accelerator orders, which can outrun deployments (the overhang, covered below). Downstream constraints (power, cooling, networking) are bought when sites are built, so they depend on data center development.

**Natural gas and wafers and packaging hold up best across scenarios.** Their levers are few and hard, and each has one main exposure.
* **Natural gas and its supply chain.** Power limits how many accelerators can run, and gas is the only source that reliably supplies it now.
  * **Where to look:** The processing, gathering, and transmission infrastructure is as much the trade as the gas itself, since that is where the shortage sits.
  * **Relief:** Alternatives (nuclear, geothermal, solar with batteries) are further out. The nearer lever is the grid: faster, more flexible connections could reduce the need for on-site gas, but that is early.
  * **Exposure:** Downstream, so delays apply, mainly permits and last-mile pipeline connections. Gas also has demand beyond data centers, which cushions a slowdown.
* **Wafers and advanced packaging.** Every accelerator needs both, so demand tracks accelerator volume.
  * **Where to look:** Both are concentrated at TSMC, so the exposure is largely one company. Samsung and Intel are the other major foundries, at smaller scale.
  * **Relief:** Capacity is hard to add elsewhere and slow to add at TSMC, which reportedly plans to roughly double advanced packaging capacity by 2028. Intel and outside packagers (e.g., Amkor, ASE) are emerging alternatives, in smaller volumes.
  * **Exposure:** Upstream, so the overhang applies. Orders can slow if accelerators are made faster than they are deployed.

**Cooling and networking are strong if the buildout proceeds, but exposed to the pace of adoption.** Both are downstream, and both have an existing solution (air, copper) that could last longer than expected.
* **Cooling, especially liquid.** Liquid is better than air for higher-power accelerators, so demand grows as density rises.
  * **Where to look:** Liquid cooling is a system, so the exposure spans the racks and cold plates, the coolant distribution units and pumps, and heat rejection.
  * **Relief:** Air is the existing solution and still cools much of the facility, so the question is how fast liquid replaces it at the chip. Adoption is gradual, which makes demand long rather than spiky.
  * **Exposure:** Downstream, so delays hit it hardest, since it is installed when a site or rack is finished.
* **Networking, especially optical.** Networking keeps accelerators from waiting on each other, and links are being added up, out, and across.
  * **Where to look:** Optical beyond the rack is already standard, and scale out and scale across keep adding links. Within optical, the value depends on the design: lasers are needed by every design, silicon photonics may gain under co-packaged optics, and DSP chips are tied to pluggables, which co-packaged designs would largely remove.
  * **Relief:** Copper is the existing solution inside the rack and may last longer than expected, so optical inside the rack is upside, not the base case. Software can also cut data movement.
  * **Exposure:** Downstream, so delays apply, and so does the pace of the newer designs, which are likely to reach large scale over the next few years.

**Memory and CPUs are conditional, for different reasons.** Memory has several levers, mostly easy ones. CPUs depend on whether agent adoption holds.
* **Memory.** Memory limits how fast tokens are generated and how much context an accelerator can hold. High-bandwidth memory (HBM) addresses both, and supply has not kept up with demand.
  * **Where to look:** HBM leads, but DRAM and flash are tight as well, since suppliers have put capital into HBM and added little NAND capacity.
  * **Relief:** Several levers, mostly the easy kind: software and model architecture that cut memory per token, higher utilization through cluster layout and networking, and new accelerator designs. More tiers move context down into DRAM and flash, which relieves HBM but not memory overall, since those are tight too.
  * **Exposure:** Upstream, so the overhang applies.
* **CPUs.** Agents run orchestration, tool calls, and code execution on CPUs, so demand follows agent adoption. Server CPU supply has tightened, with price increases and long lead times reported.
  * **Where to look:** Nvidia, AMD, Intel, and Arm-based designs all supply them, so the bet is likely on volume more than on who wins.
  * **Relief:** Software efficiency in agent runtimes, and reallocating capacity (e.g., shifting wafers from PC to data center chips), can relieve it relatively quickly.
  * **Exposure:** Agent adoption, which is still early (e.g., Intel reports the CPU-to-GPU ratio moving from about 1:8 to 1:4, and possibly 1:1 in agentic cases). CPUs are upstream and ride with servers, so the overhang applies.

#### Accelerators and Dense Sites Underpin the Buildout, and Both Could Change

**Accelerators are the volume exposure beneath the constraints.** Two things shape it:
* **Mixed fleets are likely to be the default.** An accelerator cannot be judged apart from the system around it, so picking the winner matters less than owning the growth in accelerators bought. Nvidia, the custom-silicon designers, and the hyperscalers building their own can all be held for the same reason.
* **There may be an overhang.** Sites are still being built, so some accelerators have been bought ahead of the sites that will run them, and how many is hard to know. Prices reflect the accelerators running, not those waiting, so when they come online, scarcity could ease and future purchases could be lower. This is also the exposure for the upstream constraints.

**Two longer-term changes could reset several constraints at once:**
* **Where compute runs.** The buildout assumes compute keeps concentrating in large, dense sites. If inference spreads to smaller sites or the edge, the downstream constraints (power, cooling, networking) are hit first, while wafers, memory, and CPUs are still needed. Edge is a small share of inference today, and large models and overflow still need data centers, so this looks longer term than the next year or two.
* **New accelerator designs.** A more efficient design could change how much memory, networking, and cooling are needed. Gas is the least affected. It is the most drastic change, but the least predictable.

#### Within the Constraints, Own the Strongest Companies That Aren't Priced for Permanence

**Within the constraints worth owning, pick the strongest companies at prices that do not assume the shortage is permanent.** The levers rank which constraints to own, so the rest of the decision is the company.

**Start with the strongest companies, since they best withstand the end of the shortage.** Oversupply and price competition arrive when it ends. Low costs and healthy financials get a company through the downturn, and strong brands, real distribution, and scarce IP keep its customers afterward.

**Among the strongest, avoid those priced as if the shortage is permanent.** A shortage can last a year or two and still pay. The problem is a price that needs it to last far longer. Two things to check:
* **Margins show whether the earnings are temporary.** Margins well above a company's history or its peers' usually come from the shortage itself (e.g., price increases and long lead times). The bigger the margin, the more competition works to remove the constraint: new supply, substitutes, and customers' own efforts to get around it.
* **The valuation shows whether the market assumes they last.** A normal multiple on shortage-level earnings assumes those margins are permanent, so the test is what the price implies on earnings at normal margins. A price running well ahead of sales or earnings is a more obvious warning.

**The break is hard to time, so rely on strength instead.** Aside from funding, which can be tracked through capex reported every quarter, the signals are difficult to track reliably, and the public ones can be thin or talked up by the people selling into the constraint. A position in the strongest companies should survive the break without being timed.

--------------------

### Own the Companies Providing Durable Agentic Infrastructure

**Autonomy is the goal, and agents are how it is showing up now.** Companies that supply what agents need benefit as adoption grows.

**Most of the supply can be owned today, because it is coming from incumbents.** Returns over the next year or two could show up in data, tools, trust, runtime, memory, and cost controls, because incumbents are extending what they already sell and already have what agents need:
* Products, customers, and distribution already in place.
* Data and context, for the software companies among them, since the work runs inside their systems.
* Tools, for the same companies, since an agent's tools are mostly the functions of existing software exposed through APIs.

#### Importance and Durability Make a Piece Worth Owning

**The pieces worth owning are the ones holding adoption back now and still needed in a year or two.** Two questions:
* **Is it holding adoption back now?** The pieces not yet in place are the barriers agents have to get past.
* **How durable is the need?** A durable need is core infrastructure. A less durable one is a workaround that models, clouds, or a shift in standards could absorb.

#### Agent Adoption Is the Swing Factor

**How fast agents are adopted decides how fast these pieces grow, and the reason for any slowdown matters.** Adoption is early, and how far it goes is unknown.
* **A slowdown caused by barriers** (trust, cost predictability, data readiness, infrastructure still being built) supports the pieces that remove them. The delay is what creates the demand.
* **A slowdown caused by weak value or demand** hurts all of them. Recent growth may overstate real demand, since some of it was tokenmaxxing (enterprises pushing token use for its own sake), which is now shifting as buyers get cost conscious.

#### How the Pieces Stack Up

**Data, tools, trust, and runtime are core and durable.** Data and tools are what make an agent useful. Trust and runtime are what let it run on its own.
* **Data.** A model is of little use for a task without the right context, and the context that matters is task-specific and not public.
  * **Where to look:**
    * Software companies that hold organized data as a byproduct (e.g., Tyler, Agilysys).
    * Vendors that clean, organize, and structure messy enterprise data.
    * Database vendors making their databases usable by agents.
  * **Durability:** The data itself is durable, since a proprietary asset persists. The cleanup tooling is less durable, since models may get better at messy data.
* **Tools.** An agent can only act through the software it can call, and software that is easier for agents to use gets more usage.
  * **Where to look:**
    * Companies that make their software, data, and sites usable by agents through APIs and standards such as MCP (including search sold as an API).
    * Integration and API-management vendors that connect agents to enterprise software.
    * MCP and agent gateway vendors, and identity vendors in the same path.
    * Payment networks and processors building for agent purchases (e.g., Visa's Intelligent Commerce).
  * **Durability:** The need is lasting. The protocols are less durable, since several are competing and none has settled.
* **Trust: identity, security, governance, observability.** Agents can only be given autonomy as far as they can be trusted, so adoption may lag until these controls are in place. They cover who an agent is, what it can access, what it is allowed to do, and what it did.
  * **Where to look:** Existing vendors in each part.
    * Identity, including machine and non-human identity, and privileged access and secrets management, since agents hold credentials.
    * Security vendors adding agent-specific protection, such as guardrails and defenses against prompt injection.
    * Observability vendors that trace what agents did and what it cost.
    * Governance platforms that set policies, permissions, and spend limits.
  * **Durability:** High. Any non-human actor holding access needs these controls.
* **Runtime.** Agents run long and hold state, so they need infrastructure built to keep them running through failures, not just to serve short requests.
  * **Where to look:**
    * Cloud providers, the infrastructure agents run on, which are rebuilding for stateful, long-running work.
    * Agent runtime software, a layer on top that keeps agents running through failures by saving their state and isolating the code they run. Cloud providers offer versions of it, and specialized vendors do too.
  * **Durability:** High. The need comes from what agents are, long-running and stateful, so it does not go away as models improve. What is open is whether clouds or specialized vendors capture it.

**Memory and cost controls are needed, but less durable or less certain.**
* **Memory.** Agents that carry context across sessions need it to persist, and the harder problem is retrieval.
  * **Where to look:**
    * Database vendors, both incumbents adapting existing products and newer retrieval-oriented ones (e.g., vector databases, knowledge graphs).
    * Clouds and agent frameworks building memory into their agent platforms.
    * Dedicated memory vendors, which are mostly private.
  * **Durability:** Uncertain. The need is likely lasting, but it is unclear who captures it. The best structures are still settling, and it is unclear how much will stay a separate product to buy versus being built into clouds, agent frameworks, or model providers.
* **Cost controls.** Identical tasks cost different amounts and spend is hard to forecast, so enterprises may hold back until they can predict and cap it.
  * **Where to look:** Likely the same governance and observability vendors, plus clouds and gateways that meter usage.
  * **Durability:** Moderate. The need to know what things cost is lasting, but the form could shift a lot if providers bundle spend caps or pricing becomes more predictable.

#### Existing Software Is the Most Direct Proxy for Applications

**AI-native applications are private, and the nearest public equivalent is what existing software companies build themselves.** Domain- or task-specific models and apps built on the data they hold are the form this takes now, and they already have customers to deploy them to. It is a stand-in until AI-native applications become investable, since applications are where the value ends up.

#### Own the Strongest Companies Whose Offering Is Durable

**Start with the strongest companies, since they are best placed to absorb the cost of leaning in and to keep their customers if new competitors arrive.** Low costs and healthy financials get a company through the cost, and strong brands, real distribution, and scarce IP hold its customers.

**Among the strongest, test how long what each one provides will last.** This applies to every company above, whether it sells infrastructure, applications, or both. Four questions:
* **Can it build something real for agents, or only add a bolt-on?** A feature added to an old product is easy to copy and does not hold customers. Three things show which one a company can build:
  * **How proprietary its data is.** Accumulated judgment about how work gets done is hard to reproduce. Transaction records and configuration settings mostly are not.
  * **How strong its technical team is.** Look for a record of shipping substantial new products, not only maintaining the old one.
  * **Whether the AI deepens the product or sits on top of it.** For software, a domain model built on its own data deepens the product, while a chat interface on the old one sits on top. For an infrastructure vendor, it is a product built for agents versus the old product with an agent label.
* **Is agent demand big enough to matter to it?** The core business works without agents, so it is the floor, and the agentic slice is the upside.
  * **How large the slice is** decides how much faster adoption helps the company.
  * **The price** should reflect the floor, not fast adoption.
* **Is what it provides safe from replacement?** Replacement means something else absorbing what the company sells, or going around it. It can happen in three ways:
  * **Absorbed by a bigger layer.** Clouds, model providers, or a shift in standards could bundle what it sells (e.g., runtime, memory, spend caps).
  * **Routed around by agents.** The companies exposing comprehensive access become the systems agents call. The ones that do not become a layer agents skip.
  * **Taken by AI-native entrants** that win its customers. This is a longer-term threat.

The harder its data is to replicate, the safer its position.
* **Can it afford to lean in?** Serving agents costs more, since inference is paid per use and agents use far more of it. This matters most for companies running inference. Margins could fall, and the gross margin trend shows it. Three things show whether a company can absorb it:
  * **Lower the cost,** through cheaper models, routing between models, and smaller domain-specific models built on its own data.
  * **Raise the price,** but only if the return to the customer justifies it. Usage-based pricing is the default for AI products.
  * **Make up the difference with usage,** since more volume can offset thinner margins if demand holds.

--------------------

### Physical AI Is a Supplier and Machine-Maker Trade

**Physical AI shows up first in the categories where machines already operate.** That means manufacturing, warehouses, driving, agriculture, and construction. Much of the attention goes to new robot companies, which are private, unproven, and years from scale, and a lot of that attention is hype.

**Physical AI is best held as an option on how fast machines with brains spread.** Models are making machines easier to train and deploy, so the number of machines with brains, not only robots, could grow much faster than it does today. How fast is unknown, and this is the furthest from scale of anything here, so it is upside, not a base case, and the price shouldn't assume a fast ramp. The exposure is the companies that supply the components and materials, and the existing machine makers adding AI.

#### Components and Materials Are the Infrastructure for Physical AI

**Their demand grows with machines deployed, whichever company wins.** A machine needs to sense, move, run its models, and power itself:
* **Movement.** Actuators seem to be the largest share of a machine's cost and the most specialized part, which makes movement the most interesting piece.
  * **Where to look:**
    * Precision gearing and roller screws, specialized parts that seem slow to scale.
    * Rare-earth magnets for motors. Processing is concentrated in China, so look at the largest Chinese producers and at suppliers building capacity elsewhere.
    * Motors and motor controllers, which overlap with EV and industrial supply.
  * **Durability:** Specialized parts are slow to expand, which supports them if deployment ramps, but capacity built for a fast ramp goes unused if it doesn't. Robot makers designing their own parts, or new designs, could also move demand.
* **Sensing.** Machines need visual, audio, force, and touch sensing, and it is as necessary as movement.
  * **Where to look:**
    * Cameras and depth sensors for visual sensing, and microphones for audio.
    * Force and torque sensors, and touch sensors for hands.
  * **Durability:** Which sensors machines use is unsettled (e.g., cameras only versus cameras with lidar), and touch sensing has no standard design, so demand for any one type could shift.
* **Onboard compute.** A machine acting in the physical world seems to need to run its models locally, since it cannot wait on a network connection.
  * **Where to look:** Chips and modules for running models at the edge, from the accelerator makers and from embedded and automotive chip makers.
  * **Durability:** Demand follows deployment, but how much of a machine's thinking runs on board versus in the cloud could shift as models get more efficient.
* **Power.** Batteries and charging.
  * **Where to look:** Battery makers and charging suppliers, which already operate at scale for EVs.
  * **Durability:** Demand is steady, but supply is unlikely to be scarce, so it is less of an upside.

#### Existing Machine Makers Adding AI Are the Nearest Public Stand-In for Physical Applications

**They put the brains into machines that already have buyers.** The models go into machines with installed bases, in the categories where machines operate today, so deployment doesn't wait on a new market. AI adds value in those machines through:
* Predictive maintenance.
* Material movement.
* Inspection.
* Autonomous process control.

**Installed bases are an advantage, because machines in the field are the likely source of training data.** There is no public equivalent of the data that trained language models, and the machines doing the work produce it. The makers with the largest installed bases have the advantage, especially those building the AI into the machine's core and not on top of it.

--------------------

### Watch the Signals That Say When to Hold or Rotate

**Track these regularly:**
* **Capex and funding.** Hyperscaler capex plans and the cost and form of new financing. Sustained capex supports the infrastructure positions, while cuts or more expensive funding are the warning.
* **Margins and valuations of companies in a constraint.** Margins well above a company's history, with a price that assumes they last, mean the market is treating the shortage as permanent.
* **Gross margins of software that is leaning in.** Falling gross margins show the cost of serving agents is hitting.
* **Token prices from the leading labs.** Prices that stall or fall show the cost to serve easing, which is a step toward rotating.
* **New capacity in a constraint.** Added packaging, memory, and gas infrastructure is the main thing that ends a shortage.
* **Listings and acquisitions of AI-native applications.** They show application exposure becoming available.
* **AI revenue.** Cloud companies, software companies, and machine makers that break out AI revenue show whether adoption is showing up in sales.

**Stay aware of these:**
* **Accelerators bought but not yet deployed.** If many come online at once, scarcity could ease and future purchases could fall.
* **Pullbacks in spending or data center plans, and their cause,** such as enterprises capping AI spend or data centers being delayed or cancelled. Pullbacks from the constraints themselves support those constraints, while pullbacks from funding or weak demand hurt them.
* **Agents moving from pilots to production in higher-stakes work.** It means the barriers are easing, which supports the pieces that remove them and moves rotation closer.
* **A major buyer adopting a new architecture or accelerator design at scale.** It would change several positions at once, since memory, networking, and cooling needs would shift.

