# AI Scenarios

This file defines the two scenarios that sub-sectors and companies are assessed against over the next year or two. In the base scenario, the buildout continues and AI adoption keeps growing, with some delays and higher funding costs. In the pessimistic scenario, spending is cut or demand proves weaker than expected. Each scenario is defined first, then followed by how each sub-sector is likely to be affected. The longer-term downsides in `AI Sub-Sectors.md` are outside both.

## Base scenario

- **The buildout continues.** Hyperscalers keep spending on data centers and accelerators.
- **Funding stays available.** Hyperscalers, the labs and others funding the buildout can still raise the capital they need. However, capital costs more, and weaker borrowers find it harder to get.
- **Most data centers get built.** Most planned data centers are completed and put into use. Some finish later than planned, mostly because of shortages in power, electrical equipment or permits, which moves their demand later. A few don't go ahead.
- **AI adoption keeps growing.** More people and companies use AI, and agents get much more usage. Adoption is low today, so there is a lot of room to grow, and growth is well above the pessimistic case. There are some bumps along the way, and it is slower than the optimistic projections.
- **AI keeps getting cheaper.** Running AI models costs less for each request, because efficiency gains get more out of the hardware that exists. However, the fall is not drastic, because larger drops only come as new data centers and accelerators come online.

### Physical sub-sectors

- **Processors:** Accelerator purchases keep growing, and mixed fleets spread that growth beyond GPUs. Agent adoption adds demand for CPUs. Demand exceeds supply, so delays at one site shift supply to other buyers.
- **Wafers and advanced packaging:** Demand keeps growing with accelerator volume. Equipment and materials suppliers benefit from the added output. Supply stays tight, because capacity is concentrated at TSMC and slow to add. Demand exceeds supply, so delays at one site shift supply to other buyers.
- **Memory:** Demand keeps growing with accelerators and with the context agents carry. Supply stays tight in HBM, DRAM and flash. Demand exceeds supply, so delays at one site shift supply to other buyers.
- **Networking:** Orders keep growing as clusters get larger, led by optical links between racks and between data centers. Inside the rack, the industry is moving from copper toward optical, at an uncertain pace. Some orders could arrive later where data centers finish late, but that demand is delayed, not lost.
- **Cooling:** Liquid cooling keeps growing as accelerators get denser. Air cooling grows with every finished facility. Some orders could arrive later where data centers finish late, but that demand is delayed, not lost.
- **Racks and servers:** As accelerator purchases grow, the companies that specialize in putting accelerators, memory, networking and cooling together into working systems get the volume. New rack designs add to demand. Some orders could arrive later where data centers finish late, but that demand is delayed, not lost.
- **Power:** Demand stays strong as data centers are built. Natural gas captures most of it near term, so its supply chain is where the shortage sits. Some power is bought before a site is finished, so the timing of demand is uncertain.
- **Electrical equipment:** Demand grows with the number of data centers and the power per rack. Long lead times keep the equipment scarce. Shortages of it are part of what delays some sites, which keeps demand strong. Equipment is ordered well ahead of construction, so orders come as sites are planned.

### Digital sub-sectors

- **Data:** As agents are adopted, they need data that models lack for a specific task. Two groups gain by supplying it: companies that hold the data, and companies that make enterprise data usable. Holders can also build models and applications on it, though how widely those are adopted is unclear. Adoption could come in slightly slower where late data centers keep computing scarce.
- **Tools:** Agent usage grows, so agents do far more tasks inside other companies' systems, such as looking up records and making payments. Companies that let agents in gain, mostly through access that already exists. Adoption could come in slightly slower where late data centers keep computing scarce.
- **Trust:** Demand grows for controls over agents as they are used more: identity, security, governance and observability. If agents take on work with more access and more risk, each one needs more of these controls. Adoption could come in slightly slower where late data centers keep computing scarce.
- **Runtime:** Agents, which get much more usage, generate far more inference per task than chat does. That inference has to be run in production, with each request routed to a model and chip and an agent's context kept across long tasks. Cloud providers and software vendors that handle this see demand grow. Adoption could come in slightly slower where late data centers keep computing scarce.

## Pessimistic scenario

Spending is cut, or demand proves weaker than expected. This can happen in four ways:
- A hyperscaler cuts its spending.
- An AI lab fails to raise the capital it needs.
- Adoption slows because of weak value or demand, or because enterprises cap what they spend on AI.
- A prolonged delay in data centers, whatever the cause, means computing arrives much later than planned.

The result is less computing, weaker returns for AI companies, and the return on AI questioned. Buyers who ordered accelerators ahead of finished data centers pause new orders. Where computing is short, agents cost more to run and adoption slows further.

### Physical sub-sectors

- **Processors:** Fewer accelerators and CPUs are ordered. If data centers are not built fast enough, accelerators already ordered sit waiting and buyers stop ordering more. Orders already placed still deliver, so near-term revenue may hold while new orders fall. Demand no longer exceeds supply, so supply that buyers don't take has no other buyer. Training still supports accelerator demand, but CPU demand follows agent adoption, so it may fall further.
- **Wafers and advanced packaging:** Wafer and packaging orders follow accelerator orders, so fewer are placed. Demand no longer exceeds supply, so the tightness eases. Capacity is concentrated at TSMC and slow to add, which may limit how far pricing falls, though it does not protect volume. Equipment and materials suppliers follow the output, so their orders slow too.
- **Memory:** Less memory is bought, because fewer accelerators and servers are ordered and agents hold less context as adoption slows. Demand no longer exceeds supply, so the shortage eases and pricing may soften. The efforts to relieve the bottleneck bear fruit, which reduces memory's leverage as a constraint and softens pricing further.
- **Networking:** Fewer links are bought, because accelerator orders fall and fewer data centers are finished, so clusters stop growing larger. The optical links between racks and between data centers grow with cluster size, so they may slow most. With fewer new racks built, optical inside the rack may also be adopted more slowly.
- **Cooling:** Both liquid and air cooling are hit, through different causes. Fewer accelerator orders mean fewer racks, so less liquid cooling is needed. Fewer finished data centers mean less air cooling is needed.
- **Racks and servers:** Racks and servers are where accelerators, memory, networking and cooling come together, so fewer are needed when fewer of those are ordered and fewer data centers are finished. Buyers may switch vendors fairly easily, so assemblers could compete on price for the fewer orders. With fewer new racks built, new rack designs may also be adopted more slowly.
- **Power:** Less power is needed if fewer data centers are needed or built than projected, or if some are cancelled. At sites that continue, power is still the constraint, so demand there is more likely delayed than lost. Power bought before a site is finished may protect near-term revenue, though whether it can be undone is unclear.
- **Electrical equipment:** Less electrical equipment is needed if fewer data centers are needed or built than projected. Equipment is ordered well ahead, so backlog may support near-term revenue, depending on whether orders can be cancelled.

### Digital sub-sectors

- **Data:** If adoption slows, agents need less task-specific data, so both groups that supply it are affected. Holders keep data that models cannot bundle, but sell less of it, including to labs that fail to raise capital. The models and applications they built on it may earn little after the cost of serving them. Companies that make enterprise data usable could see the AI projects they support cut or delayed.
- **Tools:** If adoption slows or enterprises cap what agents spend, agents do fewer tasks inside other companies' systems. Companies that rebuilt their products and pricing for agents get less payoff, which could shrink their margins. The companies whose systems hold the work, such as Salesforce and SAP, lose volume but not their place, because agents still have to work in them.
- **Trust:** Demand for controls over agents falls as fewer agents are deployed. Security concerns and enterprise spending caps may offset part of that, because both need controls to enforce them.
- **Runtime:** If adoption slows or enterprises cap what agents spend, less inference has to be run, so cloud providers and the software vendors that help run it see less demand. A lab that fails to raise capital cuts that demand further, because it buys less computing from cloud providers.
