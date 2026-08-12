# AMZN Q2 Earnings

Amazon.com (AMZN) — Q2 2026 (period ending June 30, 2026). Sources: Q2 2026 earnings call (CALL), 10-Q MD&A (MDA), 10-Q Notes (NOTES). Citations are source:line and map to the Excerpts section below.

---

## Q1 — What is the ROI on AI spend?

**Bottom line: Amazon never states an ROI figure, but the answer is that AI is already throwing off real revenue at high margins, and Jassy's whole message is "judge us on the cycle, not this quarter's cash flow." The returns show up now in the P&L and are set to compound as data centers get reused — but reported free cash flow is deliberately depressed by building ahead of demand.**

The return is already visible:
- AWS operating income of **$16.6B on $42.2B revenue — a ~39% margin, up 650bps YoY** (520bps excluding a one-time energy-derivative gain) (CALL:209,257,265).
- **AI revenue run rate over $25B, growing triple digits**, plus a *separate* chips run rate over $25B, also triple digits (CALL:45).
- AWS overall: **$169B run rate, revenue +36.7%** (fifth straight acceleration), adding **$4.6B quarter-over-quarter — ~80% more than its largest-ever increase** (CALL:41,43,201).

Why Jassy says the returns compound (his framework):
- **Servers/networking: break even in under 3 years**, 5-6 year life, most AI capacity on 5-year contracts → "significant free cash flow in the two to three years after we break even" (CALL:107,109).
- **Data centers: 30+ year life, reused across "five to six generations" of servers**, with each later generation earning *better* economics because the upfront cost isn't repeated (CALL:111).
- Demand-gated: "**if the demand isn't there, we won't spend the capital**"; track record of pulling break-evens forward and extending useful life (CALL:107,109).
- He claims AI's margins and returns are tracking the original AWS business "**a little ahead**" (CALL:115).

The cost, and the near-term drag:
- Capex **$53.1B in Q2, $96.3B in H1 2026** vs. $55.6B a year earlier (MDA:2061); full-year guide raised to **~$220B from ~$200B** purely on memory-chip costs (CALL:115,117).
- Demand exceeds supply: "**still not have enough capacity to meet all the demand**" in 2026, likely 2027 too, and 2028 demand is "**striking**" (CALL:117,119).
- Explicit **near-term FCF headwind** until data centers come online and monetize (CALL:111).

Two caveats on the *quality* of the return:
- The **useful-life assumption is the single biggest lever** on reported AWS profit, and the 10-Q says it's reviewed "on an ongoing basis" (NOTES:15) — historically extended (a tailwind), so any shortening would hurt.
- The quarter's headline net income is inflated by a **$50.5B non-operating markup on the Anthropic stake** (MDA:2409, NOTES:350) — not an operating return.

---

## Q2 — How concentrated is the growth in cloud revenue and the backlog?

**Bottom line: It's a split answer. Reported AWS revenue is broad-based, and AI is still only ~15% of it — but the $496B backlog's recent growth is dominated by two customers, Anthropic and OpenAI, and Amazon is partly financing both.**

Revenue growth is broad; AI is still the minority:
- **AI run rate over $25B against AWS's $169B run rate (~15%)**; the 36.7% growth is "driven by both core and AI" (CALL:45,201,203).
- Diversity signals in the core: **Graviton used by 98% of the top 1,000 EC2 customers**; Trainium adoption well beyond the labs (Uber, Pinterest, plus many startups/unicorns); Amazon Q's roster spans 3M, Allianz, AstraZeneca, BMW, Exxon (CALL:91,73).

The backlog is where the concentration sits:
- **$496B, "primarily related to AWS," 6.4-year weighted life, RPO now 2.5x a year ago** (CALL:43, MDA:799, CALL:425).
- **OpenAI expanded its commitment by $100B over 8 years** (on top of an existing $38B), and **Anthropic by "more than $100 billion over 10 years"** — both explicitly tied to AWS chips (MDA:800,801).
- → **$200B+ of the backlog comes from just two AI labs.**

And Amazon is funding those same two customers (a circular loop):
- **Anthropic:** $8B of notes + $10B of preferred this quarter + a facility up to $20B (now $15B remaining); carried at **$92.5B preferred / $97.9B notes** after the markup (NOTES:349,350,351).
- **OpenAI:** **$50B committed, $28.7B funded by June 30**, remaining $21.3B funded right after quarter-end (MDA:947,949).
- Amazon discloses **no per-customer percentage**, so the exact share is not stated — but the direction is unambiguous.

---

## Q3 — How is AMZN positioning for the future of AI, and what is its view of that future?

**Bottom line: Jassy's thesis is that AI is still early and the biggest wave — enterprises moving their everyday production workloads onto AI — hasn't started yet. Amazon's bet is to win by owning the whole stack and staying model-neutral, not by building the single best model, aiming at a $1 trillion AWS.**

His view of the future — demand is back-end loaded:
- The "**barbell**": AI labs burning compute + runaway apps (Claude Code, ChatGPT) on one end; enterprises already saving costs on the other; and the **untapped middle — most production workloads "most of which aren't" using inference yet — which he expects to become "the largest absolute segment"** (CALL:353,355,357).
- Capacity for 2027 is "**largely reserved**," with some 2028 capacity already reserved and 2028 demand "striking" (CALL:351,119).
- Structural runway: **85% of global IT spend is still on-premises**, expected to "flip" over the next 10-20 years (CALL:323,325).
- Ambition: AWS could be a **$1 trillion** business — up from a prior view of "a few hundred billion," now "at least double that" (CALL:121,365).

Pillar 1 — own the full stack, stay model-neutral:
- "**There is not going to be one model to rule the world**" — all models offered in Bedrock (CALL:279,285).
- Says Amazon can win "**without its own frontier model**," but is building one anyway for cost control, prioritization and speed; expects "**half a dozen**" comparable models, one being Amazon's (CALL:291,297).
- Bedrock traction: **customers spent more this quarter than in all prior quarters combined** (CALL:257).

Pillar 2 — custom silicon as the cost edge:
- Trainium (AI) + Graviton (CPU) = a **$25B+ chips run rate growing triple digits**; Graviton5 ramping ~2x faster than Graviton4 (CALL:89,93).
- Keeps the **Nvidia** partnership for "choice," and is exploring **selling Trainium into third-party data centers** (CALL:93,371).

Pillar 3 — the AI-core flywheel:
- Post-training, reinforcement learning and agentic tool-use largely run on CPUs like Graviton, so **AI growth pulls the core cloud business along** (CALL:51,327).

Pillar 4 — move up into the application/agent layer:
- **Kiro** (agentic coding, "up to 50% more cost-effective," usage tripled QoQ) (CALL:67).
- **Amazon Q** (AI work companion, now with autonomous background agents and broad enterprise adoption) (CALL:69,73,403).
- **Continuum** (uses frontier models to find and remediate security vulnerabilities) (CALL:79,407,409).

---

## Excerpts (verbatim)

### Earnings call (CALL)

**[CALL:41]** Revenue growth of 36.7% year-over-year, accelerating for the fifth straight quarter, our fastest growth in 18 quarters back when AWS was less than half its current revenue size. We added over $4.6 billion in revenue quarter-over-quarter, about 80% more than our largest increase ever.

**[CALL:43]** Our backlog stands at $496 billion, growing triple digits year-over-year. AWS is now a $169 billion annualized revenue run rate business, which, for perspective, would place it 24th on the Fortune 500 list if it was a standalone company.

**[CALL:45]** Our chips business now has an annual revenue run rate of over $25 billion, growing triple-digit percentages year-over-year. Our AI revenue run rate climbed significantly quarter-over-quarter, and is now also over $25 billion, growing triple-digit percentages year-over-year.

**[CALL:51]** Growth in AI drives core because post-training reinforcement learning and agent tool use is mostly done on CPUs versus AI accelerators. This is an advantage for AWS, as our Graviton chip is the strongest CPU chip, offering up to 30%-40% better price performance than other options.

**[CALL:67]** While companies will construct their own purpose-built agents from the ground up, most will also use turnkey agentic services. Coding agents are a good example, and there are several successful ones, including Claude Code, Codex, and our own spec-driven Kiro, which is up to 50% more cost-effective than others and tripled in usage quarter-over-quarter.

**[CALL:69]** Another of these agentic services is Amazon Q, an intelligent AI work companion that helps you manage, search, and automate your digital workload across email, calendar, local or cloud files, and custom workflows. Unlike other offerings in this space, Q also lets you manage across leading SaaS tools like Slack, Salesforce, Jira, Teams, and ServiceNow.

**[CALL:73]** In Q2, we made Q even more capable, adding autonomous agents that customers set up in plain language to run continuously in the background and carry out multi-step tasks, a personalized activity feed that pulls email, messages, calendars, and tasks into one prioritized view, and 16 new integrations, including Adobe, Moody's, and Snowflake. Q has momentum, with 3M, Allianz, AstraZeneca, Autodesk, BMW, Exxon, FINRA, Hyundai, Intuit, Mondelēz International, Moody's, the NBA, the NFL, Sun Life, and Southwest Airlines all using it.

**[CALL:79]** We recently released AWS Continuum, which discovers, prioritizes, validates, and remediates code vulnerabilities. It starts by ingesting the backlog of vulnerabilities a team already has and then leverages the new frontier models to run comprehensive scans.

**[CALL:89]** I mentioned earlier that our chips revenue run rate is now over $25 billion. We are unusually well-positioned for this AI inflection, given our leading price-performance chips in both AI with Trainium and CPU with Graviton.

**[CALL:91]** In addition to the two leading AI labs in the world, Anthropic and OpenAI, making multi-year, multi-gigawatt commitments to Trainium, an increasing number of AI startups are also adopting Trainium, including unicorns like Neurorobotics and Odyssey, joining startups like Twelve Labs, Descartes Labs, Poolside AI, Karakuri, Metagenomi, NetoAI, and Splash Music, and larger companies like Uber and Pinterest all adopting Trainium. Graviton is used by 98% of our top 1,000 EC2 customers.

**[CALL:93]** The revenue commitments have increased nearly three times quarter-over-quarter, and Graviton5 is growing nearly 2x faster as Graviton4 did. We also continue to have a deep partnership with Nvidia, and we'll continue making AWS the best place to run Nvidia chips, as we have customers who will run on Nvidia for as long as we can foresee, and we believe strongly that customers want choice.

**[CALL:107]** For servers and networking equipment, on average, it takes a little less than three years to break even on that investment. The servers currently have a useful life of at least five to six years, and most of our AI capacity these days is being contracted for at least five-year terms.

**[CALL:109]** That means that we're driving significant free cash flow on the servers and networking equipment in the two to three years after we break even. It's also worth noting that AWS has a strong track record of pulling forward break evens on server equipment where we've already made meaningful progress and finding ways to extend the useful life of this equipment without sacrificing customer experience.

**[CALL:111]** For our data centers, which have 30-plus-year useful lives, we should get at least five to six generations of server economics, like I explained earlier, with subsequent generations after the first having even better overall economics because we don't have to repeat that upfront data center investment I mentioned earlier. This means in the short term, when demand is necessitating so many data centers being built simultaneously in advance of when we can start monetizing them, we'll spend a lot of CapEx and encounter free cash flow headwinds until these data centers come online, can be monetized, and we get a few years into these servers being utilized.

**[CALL:115]** We see the margins and returns in AI tracking what we saw with Core at the same point of evolution, actually a little ahead. We now believe we will spend approximately $220 billion in cash CapEx in 2026.

**[CALL:117]** The higher cost of memory pushing this number up from our prior estimate of about $200 billion. Even at that amount, we will still not have enough capacity to meet all the demand we have in 2026, and I believe this dynamic will also be true in 2027, too.

**[CALL:119]** In fact, the demand we already have for 2028 is striking. Remember, enterprises are still very early in using inference at scale in their current production applications.

**[CALL:121]** We long believed AWS could become a few hundred billion-dollar revenue business and now believe it'll be at least double that, and very possibly be a trillion-dollar annual revenue business for us in time, with very appealing accompanying free cash flow and return on invested capital. I'll now turn to Stores.

**[CALL:201]** While operating margin may fluctuate and progress may not always be linear, we take a deliberate approach to achieving sustained long-term improvement in our cost to serve. Moving to the AWS segment, revenue was $42.2 billion, up 36.7% year-over-year, driven by both core and AI services.

**[CALL:203]** AWS now has an annualized revenue run rate of $169 billion. Customers continue to increase cloud migrations and scale up their use of AWS core services.

**[CALL:209]** AWS operating income was $16.6 billion, which reflects our strong growth, coupled with our focus on driving efficiencies across the business. Our investments in software and process improvements optimize server capacity and help to develop a more efficient network using our lower cost custom silicon and custom network gear.

**[CALL:257]** Can you just talk about the drivers of the 39% AWS operating margin in 2Q and just how we should think about sustainability? Andy, strong Amazon Bedrock traction with customers spending more in the quarter than in all the prior quarters combined.

**[CALL:265]** You're seeing, despite the large investments, AWS margins have continued to remain strong, and we're up 650 basis points year-over-year. 520 basis points if you exclude the derivative accounting gain that I mentioned.

**[CALL:279]** My view of it is that AWS and Amazon can have a wildly successful business without its own frontier model. A lot of that is because there is not going to be one model to rule the world.

**[CALL:285]** We have all of them in Bedrock, and it's one of the many reasons why Bedrock is growing so quickly. If you're a company that's building important AI applications, you want to make sure that you have the ability to use all the available models.

**[CALL:291]** All that said, we are pursuing our own frontier model, and we're doing it for a few reasons. First of which is it just gives us additional control over cost.

**[CALL:297]** My view of it is that within the next few years, you're going to have at least a half dozen models that are comparably good to each other. They'll all be in Bedrock, one of them will be ours.

**[CALL:323]** One is that increasingly more enterprises are building their transformation plan to move from on-premises to the cloud. Remember, by the way, that 85% of the global IT spend is still on premises.

**[CALL:325]** That equation is going to flip in the next 10 to 20 years. You see more and more enterprises that are moving and building plans to move to the cloud, we're winning the lion's share of those with the capabilities I mentioned earlier and the advantages.

**[CALL:327]** AI is growing, at such a rapid rate, and it's pulling along core alongside of it. That's because the post-training and the reinforcement learning and all the agentic tool use is being driven on CPU and core.

**[CALL:351]** Well, on the first question, Brian, we have so much demand right now. Apart from what we've talked about in 2026, the lion's share of capacity in 2027, we're adding a lot of capacity, as I mentioned just a few minutes ago, is largely reserved, and we have quite a bit of capacity that's already been reserved for 2028.

**[CALL:353]** I think it's actually kind of useful to look at at least our view of what we see in the demand and adoption curve right now, which is we see this adoption curve in AI right now is very barbellled. There is, on one end of the barbell, the AI labs are consuming gobs and gobs of compute, and there are a few runaway successful generative AI applications like Claude Code and ChatGPT.

**[CALL:355]** On the other end of the barbell are enterprises who are getting real value from AI in cost avoidance and productivity. These are things like automating customer service or business process automation or fraud or things like that.

**[CALL:357]** In the middle of the barbell is all of the current enterprise production workloads, some of which are using inference in a pervasive way, but most of which aren't. That is going to change very significantly over time.

**[CALL:365]** We think, as I mentioned earlier, it has the potential to be a $1 trillion revenue business for AWS, and we intend on continuing to be the leaders. On the question about selling Trainium, we're quite excited about what's happening in our chips business.

**[CALL:371]** There are a lot of customers who are very excited about using it in the form that we're providing right now. We do have an increasing number of customers who are interested in us providing the Trainium chips to them, separate from our cloud, and we're actively having those conversations and exploring, and I expect there's a real chance we'll do that in the future.

**[CALL:403]** That's really this next instantiation of Amazon Q. As I mentioned in my opening comments, it's pretty remarkable not only how fast it's taken off inside Amazon, but how many external enterprises have put it into production with a very large number of people at their companies.

**[CALL:407]** AWS Transform, which makes it much easier to migrate software, is super useful for enterprises. In the latest one we just launched with Continuum, it's really hard to have a conversation with a large company about AI right now where they don't actually ask you about security, with just all the noise and the hype about the security risks with the most current, powerful models.

**[CALL:409]** Continuum really allows them to use those models productively to find their own vulnerabilities in their code, to design the fixes, and to help them deploy them. Those are kind of the first set of them.

**[CALL:425]** First, your RPO reported as two and a half times that of the third quarter of 2025 when you gave us the doubling of capacity comments for year-end 2027. How does that RPO number and the massive expansion there impact your outlook for future capacity?

### 10-Q MD&A (MDA)

**[MDA:799]** Additionally, we have performance obligations, primarily related to AWS, associated with commitments in customer contracts for future services that we expect to fulfill but have not yet been recognized in our financial statements. For contracts with original terms that exceed one year, those commitments not yet recognized were approximately $496 billion as of June 30, 2026. The weighted-average remaining life of our long-term contracts is 6.4 years. The amount and timing of revenue recognition will be driven by customer usage and our performance in accordance with contractual obligations, which can extend beyond the original contractual duration and commitment.

**[MDA:800]** In Q1 2026, AWS and OpenAI Group PBC (“OpenAI”) announced an expansion of the existing $38.0 billion multi-year commitment and commercial arrangement with OpenAI by $100.0 billion over 8.0 years, which includes contractual obligations related to the performance of AWS chips.

**[MDA:801]** In Q2 2026, AWS and Anthropic announced an expansion of the strategic collaboration and existing multi-year commitment by more than $100.0 billion over 10.0 years, which includes contractual obligations related to the performance of AWS chips.

**[MDA:947]** — In Q1 2026, we and OpenAI entered into (i) a commercial arrangement primarily for the provision of AWS cloud services, which includes the use and performance of AWS chips, and (ii) a joint collaboration agreement pursuant to which certain services using OpenAI models will be made available to the Company and on AWS. We also invested $15.0 billion in Series C Preferred Stock of OpenAI and entered into an equity commitment letter agreement (the “Letter Agreement”), pursuant to which we agreed to purchase additional shares of Series C Preferred Stock (the “Commitment Shares”) with an aggregate purchase price of $35.0 billion (the “Commitment Amount”). In Q2 2026, we invested $13.7 billion of the Commitment Amount in Series C Preferred Stock. We account for our $28.7 billion investment in Series C Preferred Stock recorded on our consolidated balance sheet as of June 30, 2026, and the remaining Commitment Amount as a component of our equity investments in private companies not accounted for under the equity-method, with future adjustments for observable changes in prices or impairments representing Level 3 fair value measurements recognized in “Other income (expense), net” on our consolidated statements of operations.

**[MDA:949]** Subsequent to June 30, 2026, we invested the remaining $21.3 billion Commitment Amount in shares of Series C Preferred Stock of OpenAI.

**[MDA:2061]** Cash provided by (used in) investing activities corresponds with cash capital expenditures, including leasehold improvements, incentives received from property and equipment vendors, proceeds from asset sales, cash outlays for acquisitions, investments in other companies and intellectual property rights, and purchases, sales, and maturities of marketable securities. Cash provided by (used in) investing activities was $(39.4) billion and $(79.2) billion for Q2 2025 and Q2 2026, and $(69.2) billion and $(143.5) billion for the six months ended June 30, 2025 and 2026, with the variability caused primarily by purchases, sales, and maturities of marketable securities and cash capital expenditures. Cash capital expenditures were $31.4 billion and $53.1 billion during Q2 2025 and Q2 2026, and $55.6 billion and $96.3 billion for the six months ended June 30, 2025 and 2026, which primarily reflect investments in technology infrastructure (the majority of which is to support AWS business growth) and in additional capacity to support our fulfillment network, both of which we expect to increase in 2026. We made cash payments, net of acquired cash, related to acquisition and other investment activity of $1.7 billion and $24.4 billion during Q2 2025 and Q2 2026, and $1.7 billion and $39.8 billion for the six months ended June 30, 2025 and 2026. In Q2 2025, we invested $1.3 billion in convertible notes from Anthropic. We invested $28.7 billion in OpenAI’s Series C Preferred Stock for the six months ended June 30, 2026, including $13.7 billion invested in Q2 2026. Subsequent to June 30, 2026, we funded

**[MDA:2409]** Other income (expense), net was $1.1 billion and $53.4 billion during Q2 2025 and Q2 2026, and $3.9 billion and $69.1 billion for the six months ended June 30, 2025 and 2026. The primary components of other income (expense), net are related to equity securities valuations and adjustments, equity warrant valuations, foreign currency, and reclassification adjustments for gains (losses) on available-for-sale debt securities. The net gain of $1.1 billion in Q2 2025 is primarily from equity warrant valuations. The net gain of $3.9 billion for the six months ended June 30, 2025 is primarily from the reclassification adjustment for the gain on available-for-sale debt securities from the portion of our convertible notes investments in Anthropic that were converted to nonvoting preferred stock during the three months ended March 31, 2025. The net gain of $53.4 billion in Q2 2026 and $69.1 billion for the six months ended June 30, 2026 is primarily from upward adjustments for observable changes in price relating to our nonvoting preferred stock in Anthropic and the reclassification adjustment for the gains on available-for-sale debt securities from the portions of our convertible notes investments in Anthropic that were converted to nonvoting preferred stock during the three months ended March 31, 2026.

### 10-Q Notes (NOTES)

**[NOTES:15]** The preparation of financial statements in conformity with GAAP requires estimates and assumptions that affect the reported amounts of assets and liabilities, revenues and expenses, and related disclosures of contingent liabilities in the consolidated financial statements and accompanying notes. Estimates are used for, but not limited to, collectability of receivables, commitments and contingencies, impairment of property and equipment and operating leases, income taxes, inventory valuation, self-insurance liabilities, stock-based compensation forfeiture rates, the determination of when to capitalize certain costs relating to new products or service offerings, useful lives of equipment, valuation and impairment of investments, valuation of acquired intangibles and goodwill, valuation of derivative instruments, vendor funding, and viewing patterns of capitalized video content. Actual results could differ materially from these estimates. We review the useful lives of equipment on an ongoing basis.

**[NOTES:349]** In Q2 2026, we invested $5.0 billion in Anthropic Series G nonvoting preferred stock. We also amended our commercial arrangement primarily for the provision of AWS cloud services, which includes contractual obligations related to the performance of AWS chips. Additionally, we entered into a financing arrangement to make available to Anthropic an aggregate facility not to exceed $20.0 billion that will expire 30 months after an Anthropic liquidity event, including an initial public offering (“IPO”). At inception, there is no amount available to be drawn against and as we reach certain delivery milestones of compute capacity under the amended commercial arrangement, amounts under this facility are made available for Anthropic to draw upon at its discretion. Draws against the facility will be in the form of new Anthropic convertible notes or, after an IPO or other liquidity event and subject to our ownership cap, Anthropic common stock, which will be issued to us in exchange for cash. Under this financing arrangement, in Q2 2026, we exercised our option to participate in subsequent Anthropic equity financings by investing $5.0 billion in Anthropic Series H nonvoting preferred stock, which reduced the amount available under the facility to $15.0 billion.

**[NOTES:350]** We recorded upward adjustments of approximately $50.5 billion in Q2 2026 and $62.8 billion for the six months ended June 30, 2026 to our nonvoting preferred stock in “Other income (expense), net” to reflect observable changes in price related to Anthropic’s fundings. In making these Level 3 fair value measurements, we utilized valuation methods based on information available, including the rights and obligations of the nonvoting preferred stock, other outstanding classes of securities, estimates of expected time to and type of liquidity events and anticipated securities offerings, and discounts for lack of marketability.

**[NOTES:351]** As of December 31, 2025 and June 30, 2026, the amounts recorded on our consolidated balance sheets for nonvoting preferred stock were approximately $14.8 billion and $92.5 billion. As of December 31, 2025 and June 30, 2026, the estimated fair value of our convertible notes recorded on our consolidated balance sheets was approximately $45.8 billion and $97.9 billion, and the associated unrealized gain included in “Accumulated other comprehensive income (loss)” was $39.5 billion and $92.0 billion.
