# AI Sub-Sectors

This file describes the AI sub-sectors, one section each. The map shows how they fit together. Each group, physical and digital, starts with a list of downsides that could affect any sub-sector in it. Each sub-sector section then describes the sub-sector and its companies, its upside, how the shared downsides apply to it, and any downside specific to it. "Longer term" means beyond the next year or two.

## Sub-sector map

### Physical map

- At the center are **processors**. **Accelerators** (GPUs and custom chips) deliver the compute. Everything around them exists to keep them running, so a constraint anywhere leaves them idle. **CPUs** run the software around the accelerators, including the orchestration and tool calls agents depend on.
- **Wafers and advanced packaging** decide how many accelerators can be made.
- **Memory** feeds data to the accelerators' cores.
- **Networking** connects accelerators so they act as one system.
- **Cooling** removes the heat accelerators produce so they don't throttle.
- **Racks and servers** are where accelerators, memory, networking and cooling come together.
- **Power** runs them. **Electrical equipment** connects the data center to that power and distributes it.

This hardware is housed in data centers. How fast data centers get built tends to drive demand for most of it.

### Digital map

Models do the reasoning. They have no entry of their own, because Data captures them: public companies are building models and applications on the data they hold, and the labs that build foundation models are mostly private. Four sub-sectors turn a model's outputs into work:

- **Data** is the task-specific context models lack, and the tools that make it usable by agents.
- **Tools** are the software, data and services agents call to act, reached through existing access points and new protocols.
- **Trust** controls what agents can access, do and spend, and lets someone see what they did and what it cost.
- **Runtime** keeps models and agents running in production, from saving the state of long-running agents to routing requests across models and chips.

These sub-sectors are what autonomous AI systems need to operate. Agents are how autonomy is showing up now. How fast they are adopted tends to drive demand.

## Physical sub-sectors

### Downsides that could affect any physical sub-sector

- **Data center buildout slows.** Delays or cancellations mean fewer data centers are finished on schedule. Data centers house the hardware, so less hardware is installed. The cause matters:
  - A delay caused by shortages in power, electrical equipment or permits, including local opposition, moves demand for the hardware later.
  - A delay caused by funding or weak demand reduces it.
- **Funding pullback.** A hyperscaler cuts its spending on data centers. An AI lab fails to raise the capital it needs to buy computing.
- **Slower AI adoption.** Fewer people and companies use AI than expected, in chat and in agents, so demand for computing grows more slowly. Adoption is still early and is likely to keep growing. It may come in more slowly than optimistic estimates, because infrastructure takes time to build and behavior takes time to change, and how far it goes is unknown.
- **Accelerators ordered ahead of the completion of the data centers.** Accelerators may have been ordered before the data centers meant to house them were finished. Buyers may pause new orders until those sites catch up.
- **Software and model efficiency.** Better software and more efficient models let the same work be done with less computing hardware. Software gains are likely the fastest and cheapest, and they cut the hardware needed meaningfully, though by less than new chip designs or a new architecture could.
- **New accelerator designs (longer term).** Newer chip designs could do more work per chip or change how much supporting hardware is needed.
- **New base architecture (longer term).** A new model architecture could change how much computing, memory and networking is needed.
- **Compute moves to smaller sites or the edge (longer term).** More AI computing runs in small sites or on devices instead of large data centers.
- **New capacity (longer term).** Suppliers add capacity, which can ease the shortage and lower prices.

### Processors

Everything in physical AI hardware rotates around the accelerator. An idle accelerator is the most expensive waste.

**Accelerators**
- **Mixed fleets.** GPUs are the standard today, but other accelerators are being adopted alongside them, such as custom ASICs built for specific workloads (e.g., TPUs). Inference workloads differ in what limits them (cores, memory, or interconnect), and different accelerators have different strengths, so clusters will be mixed.
- **The system around the chip.** The system, not only the chip, sets an accelerator's performance, which dictates its cost per token. Cores, memory and interconnect have to work together, and software decides how much of that capability is used: an accelerator does not reach its rated throughput without kernels, compilers and serving frameworks built for it. This applies to every accelerator, including Nvidia's. The gap is likely larger for newer software ecosystems, which people know less well.
- **Volume.** The number of accelerators bought is expected to keep growing, and mixed fleets spread that growth beyond GPUs. Most accelerator makers benefit, but the ones with the most mature, easiest-to-use software, which get the best utilization, are likely to get the most usage.

**CPUs**

CPUs run the software around the accelerator, including the orchestration and tool calls that agents depend on. The more agents run, the more CPUs are needed, so CPU demand follows agent adoption, which is still early.

#### Companies

- **Accelerators:** GPU makers, custom silicon and ASIC designers (e.g., Broadcom), the hyperscalers building their own chips, companies with new accelerator designs (e.g., Cerebras), and companies that supply the software around the accelerator.
- **CPUs:** server CPU suppliers. Several companies supply them, so the bet is likely on volume more than on who wins.

#### Upside

**Accelerators**

Demand grows with the number of accelerators bought, which is expected to keep growing.
- Agent adoption adds demand. Agents generate far more tokens per task than chat does, so more agents mean more inference.
- Training and fine-tuning add demand. Every new model, and every company fine-tuning on its own data, needs accelerators.
- Mixed fleets spread the growth beyond GPUs. Custom ASICs and other accelerators are adopted alongside them, for the workloads they suit.
- The accelerators with the most mature software ecosystems are likely to get the most usage, because they reach more of their rated throughput.

**CPUs**

Demand for CPUs follows agent adoption.
- Agents use CPUs for orchestration and tool calls, so more agents mean more CPUs.
- Adoption is still early, so there is room to grow.

#### How the downsides apply

- **Data center buildout slows.** Fewer accelerators and CPUs are deployed.
- **Funding pullback.** Fewer accelerators and CPUs are ordered.
- **Slower AI adoption.**
  - Accelerators: fewer are needed, though training still drives demand.
  - CPUs: agents drive CPU demand, so slower agent adoption hits CPUs harder than accelerators.
- **Accelerators ordered ahead of the completion of the data centers.** Fewer new orders are placed until the data centers catch up.
- **Software and model efficiency.** The same work needs fewer accelerators and CPUs.
- **New accelerator designs (longer term).** A new design shifts demand among accelerator makers. A more efficient design could reduce the total number needed.
- **New base architecture (longer term).** A new architecture could change how many accelerators and CPUs are needed.
- **Compute moves to smaller sites or the edge (longer term).** Processors are still needed in smaller sites and on devices.
- **New capacity (longer term).** More wafer and packaging capacity increases accelerator supply. Added server CPU capacity would ease tight CPU supply.

### Wafers and advanced packaging

Wafers and advanced packaging limit how many accelerators can be made. Every accelerator needs both, so demand tracks accelerator volume.

Leading-edge wafers and advanced packaging are both tight. Both are concentrated at a single supplier, TSMC. Capacity is hard to add elsewhere quickly. It is slow to add at TSMC, which reportedly plans to roughly double advanced packaging capacity by 2028. Other foundries and outside packagers are emerging alternatives, in smaller volumes.

#### Companies

- **Foundries and outside packagers:** the companies that make leading-edge wafers and do advanced packaging, which means TSMC and the alternatives to it.
- **Equipment and materials suppliers:** the companies that supply the equipment (e.g., lithography) and materials used to make leading-edge wafers and for advanced packaging.

#### Upside

Demand tracks accelerator volume, which is expected to keep growing. Capacity is concentrated at TSMC and slow to add, so supply stays tight.
- TSMC holds the concentrated capacity.
- Other foundries and outside packagers gain volume as alternatives, in smaller volumes.
- Equipment and materials suppliers gain from more wafers and more advanced packaging.

#### How the downsides apply

- **Data center buildout slows.** Fewer accelerators are deployed. Orders for wafers and packaging slow.
- **Funding pullback.** Fewer accelerators are ordered. Fewer wafers and less packaging are needed.
- **Slower AI adoption.** Fewer accelerators are needed. Demand for wafers and packaging grows more slowly.
- **Accelerators ordered ahead of the completion of the data centers.** Orders for wafers and packaging slow until the data centers catch up.
- **Software and model efficiency.** The same work needs fewer accelerators. Fewer wafers and less packaging are needed.
- **New accelerator designs (longer term).** A new design still needs leading-edge wafers and advanced packaging.
- **New base architecture (longer term).** A new architecture could change how many accelerators are needed. That would change wafer and packaging demand.
- **Compute moves to smaller sites or the edge (longer term).** Chips in smaller sites and on devices still need leading-edge wafers.
- **New capacity (longer term).** TSMC reportedly plans to roughly double advanced packaging capacity by 2028. Other foundries and outside packagers are adding volume. This would ease the shortage.

### Memory

Memory feeds data to the accelerator's cores, and inference is why it matters. Inference is how a trained model produces its output, one token at a time. To produce each token, the accelerator reads the model's weights and the session's context from memory, so its cores spend much of their time waiting for data. Agents raise the load. They generate far more tokens per task than chat does, and they carry long context across long tasks, so each step reads more from memory. Memory limits the accelerator in two ways:
- **Bandwidth,** how fast memory delivers data, sets how fast tokens can be generated. Compute has outgrown memory bandwidth, and that doesn't seem to be changing.
- **Capacity,** how much memory can hold, sets how much context a chip can work with. Agents carry memory across sessions, and caching stores earlier computation instead of recomputing it, so more context has to be held in memory.

Memory comes in tiers that trade speed for capacity. Context that does not fit in the faster tiers can sit in the slower ones:
- **HBM** sits next to the accelerator. It is the fastest tier and the most expensive per bit, and it holds the least. It addresses both bandwidth and capacity.
- **DRAM** is the server's main memory. It is larger and slower.
- **Flash** (NAND, the chips in SSDs) is slower again and much cheaper per bit.

Every tier is tight. Supply of HBM has not kept up with demand and prices have stayed high, and suppliers have put capital into HBM and DRAM and added little NAND capacity. Because memory is the most visible bottleneck, many parties are working to relieve it, and it has more ways around it than wafers and advanced packaging, cooling or networking: software and model changes that use less memory, more memory tiers, better cluster layout and networking, new chip designs, and added capacity.

#### Companies

Several companies make more than one tier.
- **HBM makers.** The fastest tier, next to the accelerator.
- **DRAM makers.** The server's main memory.
- **Flash (NAND) makers.** The slowest and cheapest tier per bit.
- **Equipment and materials suppliers.** They make the equipment and materials used to build memory capacity.

#### Upside

Memory demand grows with inference, because every token an accelerator generates is read out of memory.
- More accelerators mean more memory. Each one needs HBM beside it, and the servers around it need DRAM and flash.
- Agents add demand for bandwidth and capacity. They generate far more tokens per task, and each step reads more context.
- Context moving down the tiers adds demand for DRAM and flash.
- Supply is tight in every tier, which supports volumes and prices for the memory makers.
- Adding memory capacity requires equipment and materials, so their suppliers gain as the makers build capacity. Their gain is from volume.

#### How the downsides apply

- **Data center buildout slows.** Fewer accelerators and servers are deployed. Less memory is installed.
- **Funding pullback.** Fewer accelerators and servers are ordered. Less memory is needed.
- **Slower AI adoption.** Fewer agents mean fewer tokens generated and less context held, so demand for both bandwidth and capacity grows more slowly.
- **Accelerators ordered ahead of the completion of the data centers.** HBM sits next to the accelerator. Memory orders slow until the data centers catch up.
- **Software and model efficiency.** Software and model architecture can reduce how much memory each token needs. Efficiency acts most directly on memory, networking and CPUs.
- **New accelerator designs (longer term).** More efficient chip designs could change how much memory is needed.
- **New base architecture (longer term).** A new architecture could change how much memory is needed.
- **Compute moves to smaller sites or the edge (longer term).** Smaller sites and devices still need memory.
- **New capacity (longer term).** More capacity in any tier would ease that tier's shortage. The same capacity that benefits equipment suppliers eventually ends the shortage for the memory makers.

#### Specific to Memory

- **More memory tiers.** Context that does not fit in HBM can sit in DRAM or flash. This eases demand for HBM. DRAM and flash are tight as well, so memory overall is not relieved.
- **Better cluster layout and networking.** Existing chips can be arranged and linked differently, such as racks built for memory and racks built for compute. Cores wait less on data.

### Networking

Networking keeps accelerators from waiting on each other. It connects them so they work as one system, and when data has to move between chips, they wait for it. Moving data faster between chips and racks also lets a cluster work around memory limits, which is part of why networking gets so much attention now. The links run at three levels:
- **Scale up** links chips within a rack so they act like one larger accelerator. Today it mostly runs on copper (e.g., NVLink, with open alternatives such as UALink competing for it).
- **Scale out** links racks across the data center. Connections beyond the rack mostly run on optical, over protocols such as Ethernet and InfiniBand.
- **Scale across** links data centers. It is mostly Ethernet over optical fiber.

**How the links are built**
- **Optical beyond the rack leads.** It is already standard, and scale out and scale across keep adding links. Within optical, the value depends on the design:
  - Lasers are needed by every design.
  - Silicon photonics may gain under co-packaged optics (CPO), newer designs that put the optics next to or on the chip.
  - DSP chips are tied to pluggables (pluggable optics, today's standard), which co-packaged designs would largely remove.
- **Copper is the existing solution inside the rack, but optical is gaining traction.** Copper is strongest at short reach, but it runs into distance and heat limits as racks get denser. Optical carries more with less latency and heat, so the industry is trying to move to it inside the rack as well. Optical inside the rack has been the next thing for a long time without arriving at scale, so the shift is likely to be gradual and may be overhyped. Copper, pluggable optics and co-packaged optics are likely to coexist. That makes it upside, not the base case.

#### Companies

The companies move data between accelerators: within a rack, between racks, and between data centers.
- **Optical beyond the rack:** the makers of lasers, optical components, silicon photonics and DSP chips.
- **Network chips and switches:** the switches and chips that run Ethernet and InfiniBand, and the links that tie chips together within a rack (e.g., NVLink, UALink).
- **Copper:** the cabling and connectors used at short reach.

#### Upside

Networking demand grows as more accelerators are deployed and clusters get larger, because every added accelerator has to be linked in.
- Optical beyond the rack keeps adding links. It is already standard, and scale out and scale across add more as clusters grow.
- Scale across grows when a single site runs out of power, because the computing then has to be spread across sites and linked.
- More inference, especially from agents, adds demand. Inference is limited by how fast data reaches the cores, and faster links between chips and racks let a cluster work around memory limits.
- Optical inside the rack would be deployed gradually, so there is room for more orders over time.
- Lasers are needed by every optical design, and silicon photonics may gain if CPO scales.

#### How the downsides apply

- **Data center buildout slows.** Networking is installed along with the accelerators. Fewer finished data centers means less networking is bought.
- **Funding pullback.** Fewer accelerators are ordered. Networking orders follow.
- **Slower AI adoption.** Fewer accelerators are deployed. Less networking is needed.
- **Accelerators ordered ahead of the completion of the data centers.** Networking orders could pause until the data centers catch up.
- **Software and model efficiency.** Less networking would be needed for the same work. Efficiency acts most directly on networking, memory and CPUs.
- **New accelerator designs (longer term).** A design that needs less connection between chips would reduce demand for networking.
- **New base architecture (longer term).** A new architecture could change how much networking is needed.
- **Compute moves to smaller sites or the edge (longer term).** Networking links accelerators within and between large data centers. Fewer large clusters means fewer links.
- **New capacity (longer term).** If suppliers add link capacity faster than demand grows, price competition would lower margins.

#### Specific to Networking

- **Copper lasts longer inside the rack.** Customers keep using copper instead of switching to optical. Optical inside the rack has been expected for a long time without arriving at scale, so the shift could take longer again.
- **Memory limits ease.** Part of networking demand is a way to work around memory limits. That demand would weaken if memory limits eased.

### Cooling

Cooling removes the heat accelerators produce so they do not throttle. It has two parts, and they coexist:
- **Liquid cooling** removes heat directly at the chip. It takes racks with cold plates on the chips, coolant distribution units (CDUs) and pumps that move the liquid, and heat rejection that carries the heat out of the building. It is a system, not a single product.
- **Air cooling** removes heat from the air around the equipment, in the racks and across the facility. Equipment that is not cooled at the chip, such as networking gear and power supplies, still needs air. Many facilities use both.

Air is the default way to cool data center equipment, but it struggles to remove heat as fast as dense accelerators produce it, and when heat builds up, chips throttle. Cooling for accelerators is therefore shifting from air to liquid as they are packed more densely and run hotter. Liquid removes heat directly at the chip, so it sustains higher density, and demand grows as density rises. The shift applies to the accelerators, not the whole facility, and it is gradual, because liquid cooling is a system and air still cools much of the facility.

#### Companies

The companies cool data centers.
- **Liquid cooling:** the racks and cold plates, the coolant distribution units and pumps, and heat rejection.
- **Air cooling:** chillers, air handlers and the rest of the equipment that cools the air.

#### Upside

Demand for cooling grows as data centers are finished and accelerators get denser. Cooling is installed when a site or rack is finished.
- Liquid cooling grows as accelerators get denser, because liquid removes heat directly at the chip and sustains higher density.
- Air cooling is still needed for the rest of each facility, so it grows with every new data center.

#### How the downsides apply

- **Data center buildout slows.** Cooling is installed when a site or rack is finished. Delays hit both liquid and air cooling directly.
- **Funding pullback.** Fewer accelerators are ordered. Liquid cooling orders follow most directly. Air cooling falls with fewer data centers.
- **Slower AI adoption.** Fewer accelerators are deployed. Less liquid cooling is needed. Air cooling is needed less as fewer facilities are built.
- **Accelerators ordered ahead of the completion of the data centers.** Cooling orders could pause until the data centers catch up. Liquid cooling is tied to the accelerators, so it is more directly affected.
- **Software and model efficiency.** The same work needs fewer accelerators. Less liquid cooling is needed.
- **New accelerator designs (longer term).** A new design could change how much liquid cooling is needed. Air cooling for the rest of the facility is less affected.
- **New base architecture (longer term).** A new architecture could change how many accelerators are needed. Liquid cooling demand follows the accelerators. Air cooling is less affected.
- **Compute moves to smaller sites or the edge (longer term).** Dense accelerators in large data centers drive demand for liquid cooling. Fewer large, dense sites means less of it. Air cooling is still needed in smaller sites.
- **New capacity (longer term).** If suppliers add cooling capacity faster than demand grows, price competition would lower margins.

#### Specific to Cooling

- **Air cooling lasts longer.** Customers keep using air instead of switching to liquid at the chip. The shift to liquid could take longer.

### Racks and servers

Accelerators are deployed in servers and racks, which is where everything comes together. A rack combines the accelerators with the memory, networking and cooling around them, and it has to work as one system:
- **Networking** links the chips within the rack (scale up) and the racks across the data center (scale out).
- **Cooling** has to fit the rack. Liquid cooling takes racks with cold plates on the chips.
- **Design** sets what the rack is built for. Existing chips can be arranged and linked differently, such as racks built for memory and racks built for compute, so cores wait less on data.

#### Companies

The companies build the servers and racks the accelerators are deployed in, and specialize in putting the parts together. Many are incumbents extending what they already make.
- **Server makers.** Companies that design and sell AI servers and rack-scale systems.
- **Contract manufacturers.** Companies that assemble servers and racks for others.
- **Rack and enclosure makers.** Companies that make the racks and enclosures the systems are built into.

#### Upside

Demand for servers and racks grows as more accelerators are bought and more data centers are built, because every accelerator has to be deployed in a rack. Racks are where networking, cooling and memory come together, so the companies that assemble the whole system get the volume. New rack designs, such as liquid-cooled racks and racks built for memory or compute, can add to demand.

#### How the downsides apply

- **Data center buildout slows.** Fewer servers and racks are installed.
- **Funding pullback.** Fewer accelerators are ordered. Server and rack orders follow.
- **Slower AI adoption.** Fewer accelerators are deployed. Fewer servers and racks are needed.
- **Accelerators ordered ahead of the completion of the data centers.** Server and rack orders could pause until the data centers catch up.
- **Software and model efficiency.** The same work needs fewer accelerators. Fewer servers and racks are needed.
- **New accelerator designs (longer term).** A new design could change what servers and racks are built for.
- **New base architecture (longer term).** A new architecture could change how many accelerators are needed. Server and rack demand follows the accelerators.
- **Compute moves to smaller sites or the edge (longer term).** Rack-scale systems are built for large data centers. Smaller sites and devices need fewer of them.
- **New capacity (longer term).** If assemblers add capacity faster than demand grows, price competition would lower margins.

#### Specific to Racks and servers

- **Price competition.** Buyers may find it easier to switch vendors for servers and racks than in other sub-sectors. Competition on price could arrive sooner.

### Power

Power limits how many accelerators can run, because a data center cannot operate without it. Meeting that takes two things: a source that generates power reliably, and a way to deliver it to the data center. Delivery is usually through the electric utility's grid, but connecting a new data center to the grid can take years and delay projects. Developers therefore work around the grid by generating power on site, which skips the wait.

Natural gas is the only source that reliably supplies power on site now. It can be deployed at the site and runs constantly. However, gas faces its own constraints, in moving the gas and in reaching the site:
- **Capacity to move gas:** processing, gathering, and transmission infrastructure is insufficient for cost-effective deployment.
- **Reaching the site:** on-site generation still needs a last-mile connection from a main pipeline, which can take a year or more.

Other potential sources of power are likely further out than gas, but may still provide value in the near term. They include nuclear, solar, batteries, and advanced geothermal. Of these, advanced geothermal may have the most potential in the near term:
- **Advanced geothermal** runs constantly, like gas, with zero emissions, and reuses existing oil and gas drilling equipment.
- **Nuclear** is not a five-year solution. Existing plants are limited, new ones take years, and newer reactor designs are not yet proven at scale.
- **Solar and batteries** are both getting cheaper on the hardware. Land, transmission, and storage at scale are not.

#### Companies

The companies produce the fuel or the electricity that powers data centers, or deliver it: fuel producers, the infrastructure that moves and processes fuel, power generators, and the utilities that deliver power.
- **Natural gas and its supply chain.** The processing, gathering, and transmission infrastructure is as much the trade as the gas itself, since that is where the shortage sits.
- **Other potential sources of power:** nuclear, solar, batteries, advanced geothermal, and any other source such as wind or hydro. Makers of technology that is itself a power source, such as solar panels and batteries, also count.

#### Upside

Demand for power grows as data centers are planned and built, since each one needs power to run, and some of it is contracted before a site is finished. Where a grid connection is slow, that demand shifts to on-site generation.
- **Natural gas and its supply chain.** Gas is the only source that reliably supplies power on site now, so it captures the near-term demand. The processing, gathering, and transmission infrastructure is where the shortage sits, so that is where the demand is felt most.
- **Other sources.** Nuclear, solar, batteries and advanced geothermal are further out but may provide value in the near term. Advanced geothermal may have the most potential, because it runs constantly, like gas.

#### How the downsides apply

- **Data center buildout slows.** Power is needed later or not at all. A delay caused by shortages in power, electrical equipment or permits, including local opposition, moves demand later. A delay caused by funding or weak demand reduces it.
- **Funding pullback.** Fewer data centers are built. Less new power is needed.
- **Slower AI adoption.** Demand for computing grows more slowly. Fewer data centers need new power.
- **Accelerators ordered ahead of the completion of the data centers.** Accelerators waiting on data centers do not draw power yet. Power demand arrives when the sites are finished.
- **Software and model efficiency.** The effect on power demand is unclear.
- **New accelerator designs (longer term).** The effect on power demand is unclear.
- **New base architecture (longer term).** The effect on power demand is unclear.
- **Compute moves to smaller sites or the edge (longer term).** Large data centers need concentrated power, which drives demand for on-site generation. Fewer large sites means less of it. Smaller sites and devices still need power.
- **New capacity (longer term).** New gas processing and pipeline capacity would ease the gas shortage. Other sources coming online would add supply beyond gas.

#### Specific to Power

- **Faster grid connections.** Fewer developers would need on-site gas.
- **Delays reaching the site.** Last-mile connections from a main pipeline can take a year or more.

### Electrical equipment

Power limits how many accelerators can run, and the power has to be connected to the data center and distributed inside it. Electrical equipment does both:
- **Connecting to the grid.** Transformers and switchgear connect the site to the grid and step the power down.
- **Distributing inside the site.** Switchgear, breakers, uninterruptible power supplies (UPS), power distribution units and busways condition the power and deliver it to the racks.

This equipment can itself hold up a site, because lead times run from about a year for switchgear to several years for large power transformers.

The equipment needed grows with the power per rack, which is rising as accelerators are packed more densely. Designs are also changing. 800 V DC distribution replaces some of the conventional AC equipment with newer power conversion equipment. When it reaches scale is unclear.

#### Companies

The companies make or install the electrical equipment that connects a data center to power and distributes it to the racks. Equipment that generates the site's main power, such as turbines, engines and fuel cells, belongs to Power.
- **Connecting to the grid and stepping power down,** such as transformers and switchgear. Large power transformers have the longest lead times.
- **Distributing and protecting power inside the site,** such as breakers, power distribution units, busways and cabling.
- **Keeping it running,** such as UPS and the batteries behind it, and backup generators.
- **Power conversion for 800 V DC designs:** rectifiers or solid-state transformers at the site perimeter, DC-DC converters in the racks, and the power chips in them.
- **Installing it,** the electrical contractors and prefabricated electrical systems that build it into the site.

#### Upside

Demand for electrical equipment grows with the number of data centers built and the power per rack, because every site needs equipment to connect and distribute its power.
- **More data centers.** Each one needs equipment to connect to the grid and distribute power inside, and electrical contractors to install it. Equipment is ordered well ahead of construction, so orders come as sites are planned.
- **More power per rack.** The power per rack is rising as accelerators are packed more densely, so each rack needs more equipment.
- **Scarcity.** Long lead times keep the equipment scarce, and equipment shortages are part of what delays some sites.
- **New designs.** 800 V DC designs add newer power conversion equipment if they reach scale. When that happens is unclear.

#### How the downsides apply

- **Data center buildout slows.** Equipment is ordered well ahead of construction, so the effect could show up later. Whether orders can be cancelled is unclear. A delay caused by shortages in power, electrical equipment or permits, including local opposition, moves demand later. A delay caused by funding or weak demand reduces it.
- **Funding pullback.** Fewer data centers are built. Whether equipment orders for those sites can be cancelled is unclear.
- **Slower AI adoption.** Demand for computing grows more slowly. Fewer data centers need new equipment.
- **Accelerators ordered ahead of the completion of the data centers.** Electrical equipment is tied to the data center build, so the effect is likely small.
- **Software and model efficiency.** The effect on electrical equipment demand is unclear.
- **New accelerator designs (longer term).** The effect on electrical equipment demand is unclear.
- **New base architecture (longer term).** The effect on electrical equipment demand is unclear.
- **Compute moves to smaller sites or the edge (longer term).** Smaller sites still need electrical equipment, in smaller sizes. Demand for the large grid-connection equipment, mainly large power transformers, could fall.
- **New capacity (longer term).** If suppliers add transformer and switchgear capacity, lead times would shorten and the shortage would ease.

#### Specific to Electrical equipment

- **Shift to 800 V DC.** Newer designs deliver power as 800 V DC, which could reduce demand for some conventional AC equipment, such as UPS, power distribution units and low-voltage switchgear, and add demand for DC equipment instead. It is likely to start in new builds, and when it reaches scale is unclear.

## Digital sub-sectors

### Downsides that could affect any digital sub-sector

- **Slower agent adoption.** Fewer companies deploy agents than expected, or deploy them more slowly. Adoption is still early and is likely to keep growing. It may come in more slowly than the optimistic projections, because infrastructure takes time to build and behavior takes time to change, and how far it goes is unknown. The cause changes the effect:
  - Barriers (trust, cost predictability, data readiness) support the sub-sectors that remove them.
  - Weak value or demand hurts all of them. Recent growth may overstate real demand, since some of it was companies pushing token use for its own sake (tokenmaxxing).
- **Data center buildout slows.** Delays or cancellations keep computing scarce. Inference stays expensive, so agents cost more to run and adoption could be slower.
- **Funding pullback.** Spending on AI is cut, in one of three ways:
  - A hyperscaler cuts its AI spending.
  - An AI lab fails to raise the capital it needs.
  - Enterprises cap what they spend on AI, as buyers become more cost conscious after tokenmaxxing.
- **Absorbed by a bigger layer.** What a sub-sector sells could be built into something larger, in three ways:
  - Clouds and model providers build it into their products.
  - Models improve enough that some of it is no longer needed.
  - A shift in standards replaces it.
- **New base architecture (longer term).** A new model architecture could change what models need and what the layer around them must do.
- **AI-native entrants (longer term).** New companies built around AI could win customers from incumbents or compete on price.

### Data

Proprietary data is valuable because foundation models lack the context for a specific task. Models have already absorbed what the internet offers, so the missing context is not public. Until models are built on that data, the user has to supply it.

Holding the data is not the same as being able to use it. Enterprise data is often messy and not agent ready, so usable data is scarcer than data that exists. Agents that carry context across sessions add a second need: that context has to persist and be retrieved. Retrieval is the harder part. Databases built for transactions and batch queries may need to adapt, while newer database structures are built for retrieval.

Holders are building models and applications on the data they hold, and some license access to it or offer it through APIs. How widely those models and applications are adopted is the open question.

#### Companies

**Companies that hold the data.** The relevant ones have data that is proprietary and valuable enough to build a substantial product on, by licensing it or by building products and models on it.
- Vertical software companies (e.g., Tyler, Agilysys), which hold data as a byproduct, since the work runs inside their systems. That data may be more structured than what enterprises hold, so it may be closer to agent ready.
- Data providers.
- Platforms, networks and marketplaces (e.g., Meta, Alphabet, AppLovin), which generate proprietary data about their users, transactions and activity as a byproduct of operating.
- Companies forming to build data deliberately (e.g., Mercor, mostly private), which supply traces, the reasoning behind expert work, to the labs.

**Companies that make data usable.**
- Vendors that clean, organize and structure messy enterprise data.
- Database vendors making their databases usable by agents, both incumbents adapting existing products and newer retrieval-oriented ones (e.g., vector databases, knowledge graphs).

#### Upside

Demand for task-specific data grows with agent adoption, because models lack the context for a specific task. Adoption is still early, so there is room to grow.
- Holders can build on their own data. A company with proprietary data and existing customers can build task- or domain-specific models and applications on it, offer access through APIs, or license it. Applications are where the value ends up. AI-native applications are private, so existing companies building on their own data are the nearest public stand-in. How widely these products are adopted is unclear.
- The harder data is to replicate, the more valuable and the safer it is. Proprietary data holds its value whichever models win. Domain-specific data, such as accumulated judgment about how work gets done, is hard to reproduce. Transaction records and configuration settings mostly are not.
- Messy data creates demand for cleanup. Most enterprise data is not agent ready, so usable data is what is scarce. Vendors that clean, organize and structure it gain as companies try to deploy agents.
- Persistent memory adds demand for retrieval. Agents that carry context across sessions need it stored and retrieved, which adds demand for databases built for retrieval.
- Cheaper inference supports adoption. Efficiency gains, accelerators coming online and any overcapacity lower the cost to serve.

#### How the downsides apply

- **Slower agent adoption.**
  - **Companies that hold the data:** Demand for task-specific data grows more slowly.
  - **Companies that make data usable:** A slowdown caused by messy enterprise data supports these companies. A slowdown caused by weak value or demand hurts them.
- **Data center buildout slows.** Agents cost more to run, so adoption could be slower. Demand for data follows agent adoption.
- **Funding pullback.**
  - **Companies that hold the data:** If a hyperscaler cuts its AI spending or an AI lab fails to raise capital, less data is bought for the labs. If enterprises cap what they spend on AI, their customers spend less on the holder's models, applications and data access. Holders that invested to build them pay to serve them, and may see little return.
  - **Companies that make data usable:** Cleanup and retrieval tools are bought to support AI projects, so when enterprises cap AI spending, these purchases could be cut or delayed.
- **Absorbed by a bigger layer.**
  - **Companies that hold the data:** The effect is likely small. Models lack this context and cannot bundle it.
  - **Companies that make data usable:** Models could get better at messy data, which would make cleanup tooling less necessary. Retrieval could be built into clouds, agent frameworks or model providers.
- **New base architecture (longer term).**
  - **Companies that hold the data:** A new architecture could change how models use data. Models would still lack the context for a specific task, so the effect is likely small.
  - **Companies that make data usable:** A new architecture could change how much cleanup and retrieval is needed. The effect is unclear.
- **AI-native entrants (longer term).**
  - **Companies that hold the data:** New companies could win customers from the software and platforms that hold data. They would not have the data the holder has already accumulated, which is hard to replicate.
  - **Companies that make data usable:** New companies could compete on price. Price competition would lower margins.

#### Specific to Data

- **Holders keep the data for their own models.** The people doing the work are using their data to build and augment their own models, so less of it may be licensed to others. That would reduce demand for companies that sell or license data.

### Tools

To go beyond chat and act in the real world, an agent needs tools, and access to them. A lot of that access already exists. Agents can already reach much of the world's existing software and data, for example through APIs.

New protocols are being built to let agents do more. Software, websites and payment systems were built for humans to operate, so new standards are being built to let agents act in that world, and the human-facing side is adapting too, with websites, software and payment providers becoming operable by systems as well as people. The protocols are still evolving, and these are examples of what they cover, not a complete list:
- **Communicate with each other** (e.g., A2A).
- **Execute transactions** (e.g., x402 for payments, UCP for what commerce actions mean to an agent). Micropayments are only viable if transactions get cheaper, which is why new payment protocols are being pursued.
- **Work with websites** (e.g., NLWeb, WebMCP).
- **Use tools and access data** (e.g., MCP, one of the leading protocols for this, with deep adoption in large enterprises).

The companies that make themselves available to agents benefit as agent adoption grows, whether through MCP, exposed APIs, data agents can use or tools agents can use. The ones that do not become a layer agents skip.

#### Companies

The companies provide software, data or services an agent would need to call to do its work. Most of the supply is coming from incumbents, since the software agents call already exists.
- **Systems where work runs** (e.g., Salesforce, SAP). The tasks agents are given run inside these systems, so agents have to call them. Many other companies depend on them.
- **Companies whose product is access.** Companies focused on providing access to data or to systems: search sold as an API, identity, and payment networks and processors building for agent purchases (e.g., Visa's Intelligent Commerce).
- **The connective layer.** Integration and API-management vendors that connect agents to enterprise software, and MCP and agent gateway vendors, with identity vendors in the same path.
- **Companies adopting protocols.** Companies that adopt protocols such as MCP in their products so agents can use them.

#### Upside

Demand for these tools grows as agents are adopted. Adoption is still early, so there is room to grow.
- Companies that make their software, data or tools available to agents gain as agents use them more. This is the near-term upside, since the access already exists.
- Companies that adopt protocols are better positioned as agents are adopted. The protocols are still evolving, so which ones matter is less certain.
- Cheaper inference supports adoption. Efficiency gains, accelerators coming online and any overcapacity lower the cost to serve.

#### How the downsides apply

- **Slower agent adoption.** Demand for these tools grows more slowly. Companies that rebuilt their products and pricing around agents get less payoff, and their margins could shrink.
- **Data center buildout slows.** Agents cost more to run, so adoption could be slower. Demand for these tools follows agent adoption.
- **Funding pullback.** If a hyperscaler cuts its AI spending or an AI lab fails to raise capital, adoption could slow. Enterprises have become more cost conscious after tokenmaxxing. If they cap what agents spend, agents would call these tools less.
- **Absorbed by a bigger layer.** Tools could be absorbed in three ways:
  - Clouds or model providers build in the connections that integration and gateway vendors provide.
  - Models improve enough to operate websites and software directly, which reduces the need for APIs, gateways and protocols.
  - A shift in standards replaces a protocol that companies have built around.
- **New base architecture (longer term).** Agents would still need software to call.
- **AI-native entrants (longer term).** Agent-first companies could win customers from incumbents that are still adapting their products for agents.

#### Specific to Tools

- **Competing protocols.** Several protocols are competing and none has settled. Which one wins could change which companies are needed. Gateway vendors built around one protocol, and companies that adopt one that loses, would be exposed.
- **Adapting to agents.** Companies built for human users have to reframe themselves around agents. That may mean moving pricing from seats toward usage or outcomes, rebuilding their offerings, and running models that cost more than traditional software. The timing cuts both ways. Moving early costs money and disruption if adoption is slow, and moving late loses ground to faster companies if adoption is quick.

### Trust

An agent is given autonomy only as far as it can be trusted, and the controls that provide that trust are still being built. Models are probabilistic, so errors compound over a long task and an agent's output cannot be assumed correct. Cost is part of trust too: an agent decides how many steps a task takes, so identical tasks can cost very different amounts, and agents use far more tokens than chat does, so total spend is hard to forecast. Until the controls are in place, adoption may lag.

Trust has four parts:
- **Identity:** each agent needs its own credentials, so it is a non-human identity. Who it is has to be defined.
- **Security:** agents hold access to sensitive systems and data, so a compromised or misbehaving agent can do real damage.
- **Governance:** what an agent is allowed to do, including how much it can spend, has to be limited.
- **Observability:** someone has to be able to see what an agent did and what it cost.

#### Companies

The companies provide the controls that make agents trustworthy and their cost predictable. Most are existing vendors extending what they already sell to cover agents.
- **Identity.** Vendors for machine and non-human identity, and privileged access and secrets management, since agents hold credentials.
- **Security.** Vendors adding agent-specific protection, such as guardrails and defenses against prompt injection, and vendors that sandbox or isolate the code agents run.
- **Governance.** Platforms that set policies, permissions and spend limits.
- **Observability.** Vendors that trace what agents did and what it cost, including clouds and gateways that meter usage.

#### Upside

Demand for these controls grows as agents are adopted and given more autonomy, since every agent that holds access needs them. Adoption is still early, so there is room to grow.
- Controls are what let companies give agents more access. As agents move from pilots to higher-stakes work, the need for them grows.
- Security and cost are the most discussed concerns right now. Security because of recent hacks, and cost because tokenmaxxing left enterprises wary of spend they can't predict or cap. Identity, governance and observability are less visible, but they are needed too, and demand for all of them can grow.
- Cheaper inference supports adoption. Efficiency gains, accelerators coming online and any overcapacity lower the cost to serve.

#### How the downsides apply

- **Slower agent adoption.** A slowdown caused by trust or cost barriers supports these companies, since the delay is what creates the demand. A slowdown caused by weak value or demand hurts them.
- **Data center buildout slows.** Agents cost more to run, so adoption could be slower. Demand for these controls follows agent adoption.
- **Funding pullback.** If a hyperscaler cuts its AI spending or an AI lab fails to raise capital, adoption could slow. Enterprises that cap what agents spend after tokenmaxxing add demand for cost controls.
- **Absorbed by a bigger layer.** Trust controls could be absorbed in three ways:
  - Clouds and model providers build controls, such as spend caps, into their platforms, which reduces the need for separate vendors.
  - Pricing becomes more predictable, or models improve enough that some controls are needed less.
  - A shift in standards replaces a control approach that companies have built around.
- **New base architecture (longer term).** A new architecture could change how reliable models are, which would change how much control is needed. The effect is unclear.
- **AI-native entrants (longer term).** New companies built for agents could win customers from existing vendors or compete on price.

### Runtime

Runtime is the software and infrastructure that keeps models and agents running in production. It does two jobs: running agents and serving models.

**Running agents.** Agents are stateful. They hold information across a long task, while ordinary software handles each short request independently. Statefulness changes what the infrastructure has to do:
- **Sessions run long.** They last minutes or hours rather than milliseconds.
- **Requests have to return to the same place.** An agent's state sits on the machine running it, so capacity cannot be added or removed freely.
- **A failure loses the work,** not just the request, so state has to be saved.

Agent runtime software saves an agent's state so a failure does not lose the work. It also isolates the code an agent runs.

**Serving models.** Requests have to be batched and routed to a model and a chip. Where models are close substitutes, a request can go to whichever offers the best mix of capability, cost and privacy. Inference runtime software does the batching and routing, picking the model and chip that fit each request on cost, complexity, domain and availability. This matters more as the number of models and accelerators grows.

#### Companies

The companies provide the infrastructure that agents and models run on, and the software that keeps them running. Most are existing companies extending what they already sell.
- **Cloud providers.** The infrastructure agents and models run on. They are rebuilding for stateful, long-running work. They provide the infrastructure for training, fine-tuning and running models. They also route requests across models and chips.
- **Agent runtime software.** Software that saves an agent's state so a failure does not lose the work. It also isolates the code agents run.
- **Inference runtime software.** Software that batches requests and routes each one to the model and chip that fits it (e.g., vLLM, SGLang, TensorRT-LLM).

#### Upside

Demand for runtime grows as agents are adopted and as more models and accelerators are in use. Adoption is still early, so there is room to grow.
- Agents are stateful, which ordinary infrastructure was not built for. Demand for agent runtime grows as agents are adopted.
- Demand for inference runtime software grows with the number of models and accelerators, since each request has to be routed to one. It also gets more work out of the hardware that exists.
- Cheaper inference supports adoption. Efficiency gains, accelerators coming online and any overcapacity lower the cost to serve.

#### How the downsides apply

- **Slower agent adoption.** Demand for agent runtime grows more slowly. Cloud providers and inference runtime software also have demand beyond agents.
- **Data center buildout slows.** Inference stays expensive, so adoption could be slower. Demand for agent runtime follows agent adoption.
- **Funding pullback.** A lab that fails to raise capital buys less computing from cloud providers. Enterprises that cap what agents spend run fewer agents.
- **Absorbed by a bigger layer.** Cloud providers offer their own versions of agent runtime software and inference runtime software. They could take that business from specialized vendors. Whether they do is open.
- **New base architecture (longer term).** Agents would still be stateful, so agent runtime would still be needed. Inference runtime software is built for today's models, so a new architecture could change what it has to do.
