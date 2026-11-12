# AI Scenarios

This file defines the two scenarios that sub-sectors and companies are assessed against over the next year or two. In the base scenario, the buildout continues and AI adoption keeps growing, with some delays and higher funding costs. In the pessimistic scenario, spending is cut or demand proves weaker than expected. Each scenario is defined first, then followed by how each sub-sector is likely to be affected. The last section lists the considerations for judging a company in each scenario. The longer-term downsides in `AI Sub-Sectors.md` are outside both.

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

## Company Scenario Considerations
Each company is judged in two scenarios, base and pessimistic, which are defined above. This section lists the considerations for judging a company in each.

### Factors in both scenarios

#### Growth
Expected sales growth, and the risks to that growth, dictate a company's stock price. Growth has two parts.
- **Potential growth** is the growth expected over the next 1 to 2 years. It rests on three things:
  - Where the expected growth is in the sub-sector. Take this from the entry for your sub-sector in `AI Sub-Sectors.md`.
  - The company's position. Is it positioned for that growth, and how will it benefit, if at all?
  - How central the sub-sector is to the company. The more central it is, the more of the company's own sales growth depends on it.
- **Current growth** is how fast sales are growing now. It is the starting point and an indicator of potential growth, but it is not the same thing. A company growing fast now may not keep doing it.

#### Strength
Strength is how well the company would hold up through a downturn, and be positioned to prosper after it. It depends on four things:
- **Earning its way.** Low costs and good margins make a company strong. Low costs show up as good gross margin and good free cash flow margin. A low margin is fine when the company is reinvesting the money in growth. Margins far above normal are a problem, as described below.
- **Funding itself.** Growth that can be funded from free cash flow.
- **Debt.** Debt that is manageable compared with free cash flow.
- **Size.** Larger, stronger companies are more likely to survive a downturn and to keep their pricing power and distribution advantages afterward.

#### Price
Price is how much of the expected growth is already in the price. We want companies where the price does not already reflect all of it. A price running well ahead of sales or earnings is a warning. Look at two things:
- **Valuation.** How much the market is paying for the company's sales and earnings. Valuation is measured at current margins, so also ask what the price implies on earnings at normal margins.
- **Sentiment.** Optimism can mean the growth is already priced in, and pessimism can mean it is not. Valuation reflects sentiment, and so do analyst ratings, where available.

#### Margins far above history or peers
Margins and free cash flow far above the company's own five-year lows, or its peers' (the other companies in the same sub-sector), usually come from something temporary, such as a shortage. The bigger the gap, the more competition works to close it. This affects all three factors:
- Growth: part of the company's position may be temporary. Growth that comes with high margins may be higher prices more than higher volume, and it fades when the prices do.
- Strength: the company may look stronger than it is. Ask whether it would still be healthy once margins fall back.
- Price: valuation looks cheaper at high margins. Where margins are far above normal, pessimism may be the market already pricing them falling.

The five-year low can be an unusually weak year, so treat a large gap as a flag, not proof.

### Base scenario
Use the base scenario above as the context for judging each company. In base, look for sustainable growth at a reasonable price.

#### Growth
- Potential growth is the most important factor. The sub-sector's upside, described in its entry in `AI Sub-Sectors.md`, may not be spread evenly across the companies in a sub-sector, so look for the companies whose business sits in the areas where the base scenario above shows demand growing.
- Current growth shows whether a company is already capturing the sub-sector's upside. Strong current growth in a company positioned for the upside may mean it is already capturing some of it. Weak current growth can mean two things:
  - If the company's peers are growing, it may not be capturing the upside.
  - If its peers' growth is low as well, the upside may not have arrived yet.

#### Strength
- Strength matters less than potential growth, but it indicates how sustainable the growth is. All else equal, larger companies with higher margins, higher free cash flow and lower debt are better. Two caveats apply to margins and free cash flow:
  - Margins far above the company's own history may reflect shortage pricing. That may not last, and profitability may fall when margins revert.
  - Lower margins and free cash flow may reflect reinvestment in growth. Sales growth indicates whether that is the case.

#### Price
- All else equal, companies at lower valuations are better. A fair or somewhat high valuation can be worth paying for strong growth.
- Avoid extreme valuations. An extreme valuation leaves little room for a shortfall in growth, even when growth is strong.

### Pessimistic scenario
Use the pessimistic scenario above as the context for judging each company. In pessimistic, look for companies that hold up when spending is cut or demand is weaker than expected.

#### Growth
- Potential growth still matters, but counts less than in base. The effect of pessimistic may not be spread evenly across the companies in a sub-sector, so look for the companies whose business sits in the areas where the pessimistic scenario above shows the least harm.
- Current growth shows whether a company is already capturing some of the sub-sector's upside, which may leave it better positioned to hold up in a downturn. However, a downturn hurts the whole sub-sector, so strong current growth does not guarantee the company holds up.

#### Strength
- Strength matters more than in base, because it indicates how well a company holds up when demand falls. All else equal, larger companies with higher margins, higher free cash flow and lower debt are better. Three things stand out:
  - Debt may matter more than in base, because payments continue while revenue falls.
  - Larger, established companies are more likely to keep their customers and orders, and smaller players are more likely to be pushed aside.
  - Margins far above the company's own history are a bigger flag than in base, because the conditions behind them may not last.

#### Price
- All else equal, companies at lower valuations are better. The most expensive companies are the most exposed, because their prices assume growth that may not arrive.
