# NVDA Growth Analysis — Is NVDA's growth decelerating?

## Synthesis (the answer)

**Short version: No — NVDA's growth is not decelerating right now. It's re-accelerating. But that's the easy half of the question. The harder half — how durable that growth is — looks weaker than the headline, and the risks are all trending the wrong way.**

**Near-term: growth is accelerating.** Revenue grew 85% year-over-year last quarter, the third straight quarter of acceleration after a five-quarter slide. But the slide had a specific, one-off cause (the China H20 export ban), so the rebound is partly just lapping an easy comparison. Underneath the optics, sequential growth has settled at a steady ~20% a quarter — very strong, but "steady," not "accelerating" — and the smoothed trailing-twelve-month growth rate is still falling. So the honest read is *strong and steady*, not *accelerating*, once you strip the base effects.

**What the growth rests on is narrow.** Almost the entire company is Data Center (~92% of revenue, ~96% of the growth), and it leans on about five hyperscalers that are roughly half the business — with customer concentration actually *rising*, not falling. Robotics and edge, the supposed next leg, are ~8% of revenue and shrinking as a share; they're a long-dated call option, not a near-term driver.

**Two things make the growth lower-quality than it looks.** First, circular financing: the hyperscaler core is genuine, self-funded demand, but NVDA is pouring money into its own customers (\$18.6B in a single quarter) and booking huge paper gains on those stakes — a self-reinforcing loop that flatters results now and would reverse hard in a downturn. Second, and most serious, custom ASICs: NVDA's own biggest customers — Google, Anthropic, OpenAI, Meta — are committing gigawatts to custom chips from Broadcom, Amazon, and Google. Broadcom's AI-silicon business alone is \$56B this year, guided above \$100B next year, and it's now taking networking share too.

**Bottom line — dollar for how many cents:** The near-term numbers are strong and real, so anyone calling growth "decelerating" today is wrong on the facts. But the growth is concentrated, partly self-financed, and increasingly contested by the very customers it depends on. The demand is not in doubt; the question is how much of *NVDA's* share of it survives. So: **growth is accelerating now, but the quality and durability of that growth is weakening** — the current quarter is worth close to a dollar, the years beyond it are worth meaningfully less than the headline implies.

---

## SQ1 — Is NVDA's sales growth decelerating? (quarterly)

**Short answer:** Not in the near term — it has *re-accelerated* for three straight quarters after a five-quarter slide. But the rebound is flattered by an easy comp created by a policy shock (China H20 ban), and the underlying signal is "very strong and steady," not "accelerating," once you strip the optics.

### The trend (total revenue, YoY growth rate)

| Quarter | Rev $B | YoY % | Seq % | Accel (pp) |
|---|--:|--:|--:|--:|
| 2025Q2 | 30.04 | 122.4 | 15.3 | — |
| 2025Q3 | 35.08 | 93.6 | 16.8 | −28.8 |
| 2025Q4 | 39.33 | 77.9 | 12.1 | −15.7 |
| 2026Q1 | 44.06 | 69.2 | 12.0 | −8.8 |
| 2026Q2 | 46.74 | **55.6** ← trough | 6.1 | −13.6 |
| 2026Q3 | 57.01 | 62.5 | 22.0 | +6.9 |
| 2026Q4 | 68.13 | 73.2 | 19.5 | +10.7 |
| 2027Q1 | 81.61 | 85.2 | 19.8 | +12.0 |

*Source: FMP quarterly income statements (`NVDA_quarterly_growth.md`).* The YoY rate fell for five quarters (122% → 55.6%), bottomed in **FY26 Q2 (ended Jul 27 2025)**, then rose three straight quarters — a clean V. Management's framing matches: "our third consecutive quarter of year-over-year acceleration" (`NVDA_earnings_remarks.md:15`, 2027Q1). The +12.0 pp latest-quarter acceleration equals the CSV's `sales_growth_q_accel_pp` of +12.01.

### What drove the deceleration (data-supported)

**1. The China H20 export ban — the concrete cause of the trough. [Confirmed]**
- FY26 Q1: a **$4.5B charge** "associated with H20 for excess inventory and purchase obligations, as the demand for H20 diminished" (`NVDA_mda.md:27`).
- China Data Center Hopper revenue was **$4.6B in FY26 Q1, then zero**: "No shipments of Data Center Hopper products to China occurred during the quarter, compared with $4.6 billion in the first quarter of fiscal year 2026" (`NVDA_mda.md:589`).
- At the trough, the CFO: Data Center "grew sequentially despite the $4 billion decline in H20 revenue," and China fell "to low single digits percentage of data center revenue" (`NVDA_ecall_2026Q2.md`, prepared remarks). The trough in YoY (55.6%) and the weakest sequential quarter in the series (+6.1%) both land here — the fingerprint of that ~$4B hole.

**2. Base effect. [Inferred from revenue levels]** Sequential dollars never stopped rising through the deceleration ($30B → $46.7B). Most of the falling YoY % was arithmetic — a rapidly growing denominator — not shrinking demand.

### What drove the re-acceleration (data-supported)

**1. Blackwell / GB300 ramp. [Confirmed]** Beginning at the trough: "began production shipments of GB300 in Q2… approximately 1,000 racks per week… expected to accelerate even further throughout the third quarter" (`NVDA_ecall_2026Q2.md`). By 2027Q1, "the fastest product ramp in our company's history" (`NVDA_earnings_remarks.md:15`). Sequential growth jumped +6.1% → +22.0% the next quarter.

**2. Networking tripling. [Confirmed]** "Data center networking revenue of $15 billion nearly tripled year over year" (2027Q1, `:15`); "$11 billion… up more than 3.5x year-over-year" (2026Q4, `:30`).

**3. Inference-demand inflection. [Confirmed]** "We capitalized on the inflection in inference demand by ramping Blackwell systems across our diverse end customer base" (2027Q1, `:15`).

**Crucially, this is ex-China:** NVDA excluded China Data Center compute from guidance in both the trough call and 2027Q1 ("consistent with last quarter, we are not including any China data center compute revenue in our outlook," `:15`). The rebound is not China returning — it's Blackwell demand overwhelming the lost China revenue.

### The honest two-sided read

- **Yes, near-term growth is accelerating** — three consecutive quarters, management-confirmed, matched by the acceleration math.
- **But temper it three ways:**
  1. **Easy comps. [Inferred]** The H20 ban depressed mid-FY26, so the YoY re-acceleration partly reflects lapping a policy-suppressed trough, not purely fresh demand.
  2. **Sequential growth — the cleaner signal — has plateaued, not accelerated.** Seq went 6.1 → 22.0 → 19.5 → 19.8%; the YoY "re-acceleration" is largely that one depressed +6.1% quarter recovering to a steady ~20% sequential clip.
  3. **TTM growth is still decelerating** even now: the CSV's `sales_growth_ttm_accel_pp` is **−15.49**, because the trailing-twelve-month window still carries the older, higher-growth quarters.

**Bottom line:** The deceleration into mid-FY26 was real but had a specific, non-recurring cause (the China H20 ban) on top of an unavoidable base effect. The re-acceleration since is genuine and demand-driven (Blackwell/GB300, networking, inference), explicitly excluding China. Calling growth "decelerating" today would be wrong on the near-term quarterly signal; calling it "accelerating" needs the asterisk that it's a rebound off a policy-driven trough, sequential growth is steady (~20%) rather than accelerating, and the smoothed TTM rate is still falling.

---

## SQ2 — How diversified are NVDA's sales? Real diversity, or dependence on frontier labs and hyperscalers?

**Short answer:** By product, NVDA is barely diversified at all — roughly 92% of revenue is Data Center. By customer, a genuine long tail is starting to form, but the business today still rests on a small set of frontier labs and hyperscalers, and the hardest concentration metrics are moving toward *more* dependence, not less.

### Product mix: essentially a single line of business

At the segment level there is little to discuss. Data Center generated **$75.2B of the $81.6B total, about 92% of all revenue**, while Edge Computing — the entire remainder, covering gaming, workstations, automotive and robotics — came to just **$6.4B, or ~7.8%** (`NVDA_mda.md:589–590`; segment table `NVDA_notes.md:3550`). Whatever diversification exists has to be found *inside* Data Center, because everything outside it is a rounding error against the AI-infrastructure engine.

### The central dependence fact: five hyperscalers are roughly half the company

The most important number for this question is not the disclosed-customer list — it's management's own admission that the **top-five hyperscalers "collectively account for a little over 50% of our data center revenue"** (`NVDA_earnings_remarks.md:30`). Since Data Center is ~92% of the company, that means **about 46% of NVDA's entire revenue depends on five buyers.** Everything else in the diversification debate is a second-order adjustment around that fact. [Confirmed]

### Customer concentration is high — and, on a like-for-like basis, rising

The filings disclose customers that individually exceed 10% of revenue. In Q1 FY27 there were three of them, at 21%, 17% and 16% (`NVDA_mda.md:727`); a year earlier there were only two, at 16% and 14% (`NVDA_mda.md:728`). The cleanest way to read the trend is customer-by-customer rather than by the raw sum: the **largest customer grew from 16% to 21% of total revenue, and the top two together grew from 30% to 38%** — and on top of that, a *third* buyer crossed the 10% threshold, which is itself a signal that reliance on a handful of giant accounts is deepening rather than dispersing. [Confirmed]

The accounts-receivable disclosure makes the direction unmistakable because it compares the same number of customers across periods. **Three direct customers held 56% of receivables in January 2026 and 64% just one quarter later in April 2026, with the single largest rising from 25% to 30%** (`NVDA_notes.md:3149`). Concentration tightening that much in a single quarter is the strongest same-basis evidence that dependence is currently increasing. [Confirmed]

### Is the "diversified" half of Data Center really diverse, or the same labs one step removed?

Data Center now splits almost evenly between Hyperscale ($37.9B) and ACIE — AI Clouds, Industrial and Enterprise ($37.4B) — and ACIE is the faster grower, up 31% sequentially against Hyperscale's 12% (`NVDA_notes.md:3550`; `NVDA_mda.md:589`). Management frames that second half explicitly as customer diversification. The complication is that ACIE's fastest-growing component is AI-cloud revenue, which "more than tripled year over year" (`NVDA_earnings_remarks.md:15`), and AI clouds such as CoreWeave largely *resell* their capacity to the same frontier labs that also buy directly from the hyperscalers. NVDA's own disclosure confirms the pass-through: "one AI research and deployment company contributed a meaningful amount of our revenue **by purchasing cloud services from our customers**" (`NVDA_mda.md:731`), and Jensen describes expanding Anthropic's capacity "across Azure, AWS, CoreWeave" (`:15`) — a single lab spanning both halves of Data Center. So some meaningful part of what is counted as diversification is really the same underlying frontier-lab demand routed through a different buyer. The mechanism is confirmed in the filings; the exact size is not disclosed, so this remains a bounded inference rather than a measured figure. [Mechanism confirmed; magnitude inferred]

### The counterweight: management's case that the base is genuinely broadening

This deserves real weight, because it is not just spin — the fastest-growing parts of the business are the diversifying parts. Jensen's structural argument is that beyond the handful of hyperscalers lies a second and third category — AI-native startups, on-premise enterprise, industrial deployments, sovereign AI, and the robotic edge — that "represents **hundreds of thousands of companies** around the world," each of which needs to build AI and for which NVDA's full-stack, buy-it-and-operate-it solution is the enabler (`NVDA_earnings_qa.md:23`). The numbers partly support the trajectory: ACIE growing more than twice as fast as Hyperscale sequentially, **sovereign revenue up more than 80% year over year**, NVDA infrastructure now deployed across "nearly 40 countries representing $50 trillion in GDP," and partner data centers above 10 megawatts having "nearly doubled in just one year… surpassing 80 sites" (`NVDA_earnings_remarks.md:15`). The bull reading is that today's concentration simply reflects an early phase in which a few well-capitalized hyperscalers move first, and that as this long tail compounds, NVDA's dependence on any single cohort should structurally decline.

The honest rebuttal is that this is a trajectory and a forecast, not the present mix — and management itself concedes the point, noting that "you expect the second category to develop slower than hyperscale, and you could see that in the numbers." So the diversification is real and directionally encouraging, but it has not yet grown large enough to offset the concentration that dominates the business today.

### Bottom line

NVDA's revenue is about 92% a single product and is anchored by roughly five hyperscalers that together make up about half of Data Center revenue — that concentration is the dominant reality, and the same-basis metrics (receivables tightening from 56% to 64% in a quarter, the largest customer rising from 16% to 21% of revenue) show it currently deepening rather than easing. At the same time, a genuine long tail is forming beneath that core — AI clouds, sovereign, enterprise — and it is growing faster than the hyperscale base, which is management's credible case that dependence broadens over time. But that broadening is still a trajectory rather than today's mix, and part of the fast-growing "diverse" bucket traces back to the same frontier labs buying through intermediaries. The fair conclusion for the key question is that NVDA's growth is **not broadly diversified today — it remains concentrated in AI Data Center demand from a small set of frontier labs and hyperscalers — even as real diversification builds at the edges.** It is a concentrated business that may be broadening, not a diversified one.

---

## SQ3 — Fastest-growing segments, their size, and how much they move overall growth

**Short answer:** The growth is almost entirely Data Center — ~96% of the year-over-year dollar increase. Inside it, the *fastest-growing* meaningful line is networking (nearly tripled); the *largest dollar driver* is compute (~$26B). Everything outside Data Center — including robotics — added under 4%, so nothing else moves the number yet.

### How NVDA reports revenue (two platforms)

NVDA now reports **two market platforms** (`NVDA_mda.md:528–532`):

- **Data Center — $75.2B (~92% of revenue)**, split into two sub-markets:
  - **Hyperscale — $37.9B**, public clouds + largest consumer-internet companies
  - **ACIE — $37.4B**, AI Clouds, Industrial & Enterprise (incl. sovereign)
- **Edge Computing — $6.4B (~7.8%)** — a separate platform: PCs/gaming, workstations, AI-RAN, robotics, automotive.

A *second, orthogonal* cut of Data Center appears only in the call — by **product type**: compute vs. networking. That's a different slice of the same $75.2B, so the two cuts shouldn't be summed.

### The fastest growers, by rate

- **By customer (platform):** Hyperscale **+115% YoY**, ACIE +74%, Data Center +92%, Edge +29% (recast table, `NVDA_notes.md:3550`; `NVDA_mda.md:589–590`).
- **By product:** Data Center **networking $15B, "nearly tripled" (~+200%)** — the fastest meaningful line — vs. compute $60B, +77% (`NVDA_earnings_remarks.md:15`). The audited GAAP cut agrees on location: Compute & Networking +88% vs. Graphics +58% (`NVDA_mda.md:660–682`).

### What actually drives the overall growth rate (absolute-dollar contribution)

Total revenue grew **$37.55B** YoY ($81.6B − $44.06B). Share of that increase by piece:

| Piece | YoY $ growth | Share of total growth | Basis |
|---|--:|--:|---|
| **Data Center (all)** | +$36.1B | **~96%** | exact (recast table) |
| — Hyperscale | +$20.3B | ~54% | exact (recast table) |
| — ACIE | +$15.9B | ~42% | exact (recast table) |
| Edge Computing | +$1.4B | ~4% | exact (recast table) |
| *DC compute (product cut)* | *~$26B* | *~69%* | *estimated from call* |
| *DC networking (product cut)* | *~$10B* | *~27%* | *estimated ("nearly tripled")* |

*(The platform rows are subtraction/division of figures NVDA reported for both years in the recast table — no assumptions. Only the two italic product-cut rows are estimated, and networking's is the softest, since "nearly tripled" spans ~2.7–3.0x.)*

**Two takeaways: the fastest grower and the biggest dollar-driver are different lines.** Networking is the standout on rate (nearly 3x) and is unusual in being both large and fastest. Compute is the standout on absolute dollars (~$26B of the ~$37.5B total). And on the customer cut, Hyperscale — despite being the "less diversified" half — still contributed the most absolute growth (~54%).

### The fast-but-still-small lines (real, not yet moving the number)

- **Vera CPU** — new line, "visibility to nearly $20 billion in total CPU revenue this year," a claimed "$200 billion TAM… we have never addressed before" (`NVDA_earnings_remarks.md:15`). Strategically large, essentially pre-revenue at the Q1 snapshot.
- **Sovereign** — "up more than 80% year over year" (`:15`), a sub-slice of ACIE.
- **Physical AI** — "exceeding $9 billion… over the last 12 months" (`:15`), cross-cutting Edge and some Data Center (the core of SQ4).

### Bottom line

For the key question, the composition matters as much as the rate: NVDA's growth is a Data Center story and almost nothing else — ~96% of the dollar increase. The two engines inside it are compute (biggest by dollars, ~$26B) and networking (fastest by rate, ~3x, and already 18% of revenue). The customer cut shows Hyperscale still supplying the most absolute growth even as ACIE grows faster in percentage terms. Robotics/Edge and everything non-Data-Center contributed under 4% of the growth, so — for now — they are not what's driving the number. The genuinely fast emerging lines (Vera CPU, sovereign, physical AI) are real and worth tracking, but none is yet large enough to change the overall growth rate.

---

## SQ4 — Is robotics / edge AI a meaningful chunk of revenue? Growth, and could an inflection make a real difference?

**Short answer:** No — not today. Edge Computing is ~7.8% of revenue and *shrinking* as a share, growing far slower than the company and contributing only ~4% of the growth. The more interesting cut, "physical AI" at ~$9B trailing, is growing faster (~50%) but is still ~3.6% of revenue. Robotics/edge is a legitimate long-dated call option on a future inflection — not a current driver, and nothing in the numbers shows that inflection has started.

### Sizing it: ~8%, and receding

Edge Computing generated **$6.4B, up 29% YoY and 10% sequentially** (`NVDA_earnings_remarks.md:15`; `NVDA_mda.md:590`) — **7.8% of the $81.6B total.** The trend of that share matters: a year earlier Edge was **$4.95B of $44.06B = 11.2%** (recast table, `NVDA_notes.md:3550`). Because Edge grew 29% while the company grew 85%, **its share fell from 11.2% to 7.8%** — relative to the business, robotics/edge is getting *less* meaningful, not more, and it added only ~4% (~$1.4B) of the year's $37.5B revenue increase. Even the +29% is mixed: "robust Blackwell workstation demand… while consumer demand fell modestly due to higher memory and system prices" (`NVDA_earnings_remarks.md:15`) — more AI-workstation than robotics/consumer.

### The better lens: "physical AI" (a cross-cutting measure)

NVDA reports a **physical AI** figure spanning platforms (edge devices + some Data Center training/simulation): "exceeding **$9 billion** in revenue over the last 12 months" (`NVDA_earnings_remarks.md:15`), up from "over **$6 billion** in… fiscal year 2026" (`:30`). Roughly **+50%** [Estimated — periods don't align perfectly], faster than the Edge platform because it captures the Data-Center side of robotics/AV work. But at ~$9B against ~$253B trailing revenue (CSV `sales_ttm_usd`), it's still **~3.6% of the company.**

### Could an inflection make a "real difference"? The scale math says: not soon

To move the overall growth rate, robotics/physical AI must become large relative to Data Center's ~$300B annualized run-rate. Off a ~$9B base, even sustained ~50% annual growth takes about **five years to reach ~$70B** (~1.5⁵ ≈ 7.6x) — meaningful eventually (~23% of today's Data Center), but years away and dependent on that rate holding [Estimated — illustrative arithmetic, not a forecast]. Near-to-medium term, the base is too small to swing the number.

### The bull optionality (real, but unproven on timing)

The counter-case: physical AI is the *next* leg and NVDA is uniquely positioned — the Uber robotaxi partnership "across nearly 30 cities and four continents by 2028," robotics adoption "across… industrial, surgical, and humanoid applications" (`NVDA_earnings_remarks.md:15`), NVDA as practically the only full-stack supplier. If robotaxi/humanoid deployment inflects, the TAM is large and NVDA captures much of it. But that's a future story; the current numbers show steady ~50% growth off a small base, not the exponential inflection the thesis needs.

### Bottom line

Robotics/edge is **not meaningful to NVDA's growth today** — Edge is ~8% of revenue and *falling* as a share, adding only ~4% of this year's growth. The physical-AI cut (~$9B trailing, ~50% growth) is more encouraging but still ~3.6% of revenue and cross-counts Data Center. To "make a real difference" it needs a genuine multi-year inflection (robotaxi/humanoid at scale); the scale math means even strong growth off today's base can't move the overall rate for years. It belongs in the analysis as a **long-dated call option with real optionality** — explicitly *not* part of the current growth engine.

---

## SQ5 — Is the growth organic, or inflated by circular financing, vendor financing, or round-tripping?

**Short answer:** The core — roughly half the company, the hyperscalers — is clearly organic, self-funded demand. But NVDA is aggressively building a large, fast-growing ring of circular and vendor-financing arrangements around the frontier-lab / neocloud *other* half, and that ring is where the marginal growth and nearly all the paper gains now concentrate. The filings confirm the mechanism and its scale in NVDA's own words; they do not let us quantify how much revenue actually round-trips. The Groq acquisition adds zero revenue — ruled out.

### The organic core: hyperscalers fund themselves

About 46% of the company is the top-five hyperscalers (`NVDA_earnings_remarks.md:30`, established in SQ2), and those buyers finance their own capital spending — analyst-tracked hyperscale CapEx "up nearly $120 billion since the start of the year and approaching $700 billion" (`NVDA_earnings_remarks.md:30`). NVDA does not fund Microsoft, Amazon, Google or Meta. So roughly half the revenue base is unambiguously organic — real end-demand paid for with the customers' own money.

### The circular ring: stated by NVDA, and scaling fast

The concern is real and NVDA describes it plainly. In **a single quarter** it invested **$18.6 billion in private companies and infrastructure funds**, and says outright that "some of these investments include **AI model makers that may indirectly purchase or use our products in the cloud**" (`NVDA_mda.md:446`). For context, the *entire prior fiscal year* was $17.5 billion (`NVDA_mda.md:35`) — so the investment pace roughly quadrupled. The 10-K is even more explicit that the loop exists: investees "include AI model makers that **purchase our products directly or through CSPs**" (`NVDA_mda.md:35`). That is the round-trip, in NVDA's own words: NVDA funds a model maker, the model maker buys NVDA GPUs (directly or via a cloud), and the cash returns as revenue.

The named nodes are the ones you'd expect: NVDA is "**finalizing an investment and partnership agreement with OpenAI**" (`NVDA_mda.md:415`), holds an Intel stake (`NVDA_mda.md:327`), is expanding **Anthropic's** capacity "across Azure, AWS, CoreWeave," and works with **CoreWeave** — a company that is simultaneously an investee/partner and a buyer (`NVDA_earnings_remarks.md:15`).

Beyond equity, NVDA extends **vendor-financing-style backstops**: "$3.5 billion in land, power, and shell **guarantees** to early-stage companies" (`NVDA_mda.md:39`), and facility-lease guarantees taken "in exchange for warrants," with partners posting $712 million in escrow (`NVDA_notes.md:3293`). In effect NVDA underwrites customers' ability to build the very data centers that house its chips. And the flow runs both ways: NVDA has committed to **buy $30 billion of multi-year cloud services** from CSPs (`NVDA_notes.md:3366`) — it is a customer of its own customers.

### The reflexivity tell: the paper gains

This ring is visibly self-reinforcing. NVDA booked **~$15.9 billion of "other income" this quarter, almost entirely investment gains** (`NVDA_mda.md:802`). So the loop is: NVDA invests in an AI company → that company's valuation rises (partly *because* NVDA's demand and endorsement inflate the whole ecosystem) → NVDA marks up the stake and books a gain → the company uses its capital to buy more NVDA compute. That is a textbook reflexive loop — it amplifies results on the way up and would amplify them just as hard on the way down.

### What the data cannot tell us

NVDA does not disclose how much of its revenue comes from entities it funds, so this can only be bounded, not measured. The one direct hint is the indirect-customer line: "one AI research and deployment company contributed a meaningful amount of our revenue by **purchasing cloud services from our customers**" (`NVDA_mda.md:731`) — confirming a single funded lab is material to revenue while leaving the amount undisclosed.

### Groq: ruled out

The Groq deal was a license-plus-acquihire, not a revenue source: "**No customer contracts, existing products, or equity interests were purchased**" (`NVDA_notes.md:124`), against $14.4B of goodwill. Acquisitions are not inflating the top line.

### Bottom line

Growth is **organic at the core and increasingly circular at the margin.** The hyperscaler half is self-funded, genuine demand. But around the frontier-lab and neocloud half, NVDA is rapidly scaling a ring of investments (from $17.5B/year to $18.6B/quarter), guarantees, warrants, and $30B of reverse cloud commitments — feeding customers who feed revenue back to NVDA, with the resulting valuation gains booked as income. The mechanism is confirmed and reflexive; the magnitude is undisclosed. For the key question this matters because the *circular* portion appears to be growing faster than the *organic* core — so some of the very re-acceleration identified in SQ1 may be partly self-financed, and reflexive loops unwind violently when sentiment turns.

---

## SQ6 — Are custom ASICs stealing share / growing in demand? Do they have capabilities out-of-the-box GPUs don't?

**Short answer:** Yes — decisively. Custom ASICs are now a very large and explosively growing business, led by Broadcom at **$56B of AI-silicon revenue this fiscal year and guided above $100B next year**, backed by **multi-gigawatt commitments from the exact frontier labs NVDA depends on** (Anthropic, OpenAI, Google, Meta). The edge is economics and custom fit — price/performance, perf/watt, vertical cost control on stable/inference workloads — **not** capabilities GPUs lack, and every hyperscaler still buys NVDA's Vera Rubin. But Broadcom is now also taking networking share, NVDA's fastest-growing adjacent line. This is the most serious threat to the *durability and mix* of NVDA's growth — not its current level.

*(Terms: a **GPU** — what NVDA sells — is a general-purpose AI chip that runs any model. A custom **ASIC** is a chip built for one company's workload: Google's **TPU**, Amazon's **Trainium**, Meta's **MTIA**, Microsoft's **Maia**. **Broadcom** is the merchant designer that co-develops most of those custom chips — it calls the category **XPU** — so its results are effectively the scoreboard for how much demand is shifting from buying NVDA GPUs to building custom silicon.)*

### Broadcom: the custom-ASIC business is now at NVDA-comparable scale trajectory

Broadcom is the pure-play custom-silicon vendor, and its 2026 Q2 call (ended Apr 30 2026) removes any doubt that ASICs are taking real, large, growing demand (AVGO 2026Q2 call, Tan):

- **AI semiconductor revenue $10.8B in the quarter, up 143% YoY**, with **networking ~40%** of it.
- **Bookings over $30 billion against $10.8B shipped** — a backlog roughly 3x current shipments.
- **Full-year FY26 AI-silicon revenue $56B (+~180%)**, and **FY27 guided above $100B.** For scale, NVDA's Data Center is ~$300B annualized — so Broadcom's custom-AI silicon alone is already on track to be roughly a third of NVDA's Data Center within a year, growing far faster.

### The commitments come from NVDA's own key customers — quantified

This is what matters for the key question. In SQ2 we showed NVDA leans on ~5 hyperscalers and a few frontier labs; SQ6 shows those same names committing gigawatts to custom silicon (AVGO 2026Q2, Tan):

- **Google:** long-term agreement for "multiple generations of TPUs and AI networking" (7th-gen Ironwood).
- **Anthropic:** >1 GW of Broadcom TPU compute in 2026, **+5 GW of next-gen TPU beginning 2027.**
- **OpenAI:** 1.3 GW in 2027, part of a **10-GW-by-2029** agreement.
- **Meta:** MTIA XPUs, **3 GW through 2028.**

Amazon corroborates from the other side: "the two leading AI labs… **Anthropic and OpenAI, making multi-year, multi-gigawatt commitments to Trainium**," with the chips business "over **$25 billion** run rate, growing triple-digit" (AMZN Q2 2026, Jassy). Google is now **selling TPU systems into external customer data centers "for the first time," ramping into 2027** (GOOG Q2 2026, Ashkenazi). Microsoft's **Maia 200 delivers "30% better performance per dollar" and runs OpenAI's own models** (MSFT FY26 Q4, Nadella). The frontier-lab demand driving NVDA's SQ1 re-acceleration and SQ2 concentration is multi-sourcing across all three ASIC tracks at once.

### The second front: networking

Broadcom is not only attacking compute — it is taking share in **networking**, NVDA's fastest-growing adjacent line (SQ3: NVDA networking nearly tripled to ~$15B). Tan: "We are clearly **gaining share in networking**… Tomahawk 6 [100-terabit Ethernet]… capturing demand from hyperscalers, **whether they use XPUs or GPUs**." That last clause is the sting — even clusters full of NVDA GPUs may use Broadcom Ethernet instead of NVDA's InfiniBand/Spectrum-X, putting NVDA's networking growth partly at risk regardless of who wins compute.

### Capabilities, or economics? Still economics — which is where NVDA's own defense holds

Crucially, none of the four claims a capability GPUs *can't* match. Every stated advantage is **price/performance, perf-per-dollar, or perf-per-watt** (Maia +30% perf/$, Graviton +30–40% perf/$, Axion +30% perf/$), plus custom fit to the owner's model and vertical cost control. ASICs anchor to stable, known workloads — serving a fixed internal model (Maia↔OpenAI, TPU↔Gemini, Trainium↔Anthropic) — i.e., cost-sensitive inference. This actually *validates* NVDA's own argument: general-purpose GPUs stay ahead where models churn, for frontier training, for the merchant market, and for the fragmented long tail that "buys systems rather than… custom chips" and where "NVIDIA is practically the only company serving them" (`NVDA_earnings_qa.md:24,33`). The real erosion is the **software moat** — Google's "workload portability across GPUs and TPUs" via JAX/PyTorch/vLLM/SGLang chips away at CUDA lock-in.

### And everyone still buys NVIDIA — it's dual-track, not either/or

Each hyperscaler explicitly frames it as "choice" and is still deploying Vera Rubin: MSFT ("among the first… to deploy NVIDIA Vera Rubin"), AMZN ("deep partnership with Nvidia… customers who will run on Nvidia for as long as we can foresee"), GOOG ("Google and NVIDIA, including the new NVIDIA Vera Rubin platform, and TPU"). NVDA keeps the default for frontier training, general-purpose, merchant, external-customer, and long-tail work; ASICs take the owner's-own-model and cost-sensitive-inference slice.

### What the data proves — and doesn't

It does **not** prove NVDA's share is falling: the pie is growing so fast that NVDA and the ASICs both grow, and NVDA claims it is "growing share in inference" (unverified). What it **does** prove is that the ASIC alternatives are now (a) at NVDA-comparable scale trajectory (Broadcom $56B→$100B+), (b) growing triple digits, (c) externalizing (Google selling TPU systems; Amazon exploring merchant Trainium), (d) attacking both compute *and* networking, and (e) winning multi-gigawatt commitments from the precise hyperscalers and frontier labs that are NVDA's most concentrated exposure.

### Bottom line

Custom ASICs are real, scaled, and accelerating — Broadcom alone is a $56B (heading to $100B+) AI-silicon business, with Anthropic, OpenAI, Google, and Meta all committing gigawatts, plus AWS Trainium ($25B+, triple-digit), Google TPU (now sold externally), and Microsoft Maia. Their edge is economics and custom fit on inference/known workloads, not capability, and everyone still buys Vera Rubin for frontier and general-purpose compute. For the key question this is the most serious structural qualifier of all six, and it compounds SQ2 and SQ5: **NVDA's largest customers are simultaneously its largest competitors — funding, designing, and committing gigawatts to the alternatives, while Broadcom also attacks NVDA's networking.** The near-term growth level is intact; the multi-year durability — especially the inference and networking share NVDA is counting on — faces a credible, well-capitalized, and fast-growing custom-silicon alternative built by the very buyers NVDA depends on.

---

## Excerpts (only those used)

## NVDA — quarterly revenue series (FMP)
Revenue ($B), YoY%, Seq%, Accel(pp) per quarter — see the SQ1 table (2025Q2 122.4% → 2026Q2 trough 55.6% → 2027Q1 85.2%).

## NVDA — screener metrics (`Large_Actives_with_Metrics.csv`)
- `growth_context`: "Strong · Decelerating · Aligned"; `sales_ttm_usd`: $253.5B
- `sales_growth_latest_q_yoy_pct`: 85.23; `sales_growth_ttm_vs_prior_ttm_pct`: 70.68
- `sales_growth_q_accel_pp`: **+12.01**; `sales_growth_ttm_accel_pp`: **−15.49**

## NVDA — 10-Q (MD&A + Notes)
- "$4.5 billion charge… associated with H20… as the demand for H20 diminished." (`mda:27`)
- "No shipments of Data Center Hopper products to China occurred during the quarter, compared with $4.6 billion in the first quarter of fiscal year 2026." (`mda:589`)
- Revenue $81.6B; Data Center $75.2B (+92%); Edge $6.4B (+29%). (`mda:588–590`)
- Recast Market Platform table: DC 75,246 / 39,112; Hyperscale 37,869 / 17,599; ACIE 37,377 / 21,513; Edge 6,369 / 4,950; Total 81,615 / 44,062. (`notes:3550`)
- "We will have two market platforms – Data Center and Edge Computing." / Edge "includes… PCs, game consoles, workstations, AI-RAN base stations, robotics and automotive." (`mda:528–532`)
- GAAP segments: Compute & Networking $74,550M (+88%); Graphics $7,065M (+58%). (`mda:660–682`)
- "three direct customers represented 21%, 17%, and 16% of total revenue." (`mda:727`) / prior "two direct customers represented 16% and 14%." (`mda:728`)
- "Three direct customers accounted for 30%, 18%, and 16% of our accounts receivable… as of April 26, 2026" vs "25%, 18%, and 13%… as of January 25, 2026." (`notes:3149`)
- "one AI research and deployment company contributed… by purchasing cloud services from our customers." (`mda:731`)
- "$18.6 billion in private companies and infrastructure funds. Some of these investments include AI model makers that may indirectly purchase or use our products in the cloud." (`mda:446`)
- "$17.5 billion in private companies… include AI model makers that purchase our products directly or through CSPs." (`mda:35`)
- "$3.5 billion in land, power, and shell guarantees to early-stage companies." (`mda:39`)
- "finalizing an investment and partnership agreement with OpenAI." (`mda:415`) / Intel investment gains (`mda:327`)
- "guarantee partners' facility lease obligations… in exchange for warrants"; "placed $712 million in escrow." (`notes:3293`)
- "Multi-year cloud service agreement commitments as of April 26, 2026, were $30 billion… used to support our research and development efforts." (`notes:3366`)
- Total other income, net $16,367M — "unrealized gains… publicly-held equity securities of $13.4 billion and non-marketable equity securities of $2.6 billion." (`mda:802`)
- Groq: "No customer contracts, existing products, or equity interests were purchased." $14.4B goodwill. (`notes:124`)
- Open-source competitors line (the only competition mention in the MD&A). (`mda:443`)

## NVDA — earnings calls
- **2027Q1 remarks:** "third consecutive quarter of year over year acceleration"; "the fastest product ramp in our company's history"; "data center networking revenue of $15 billion nearly tripled"; "data center computing revenue of $60 billion was up 77%"; "capitalized on the inflection in inference demand"; "we are not including any China data center compute revenue in our outlook"; "top 5 cloud providers and hyperscalers who collectively account for a little over 50% of our data center revenue"; ACIE "AI cloud revenue that more than tripled"; "Sovereign revenue increased more than 80%"; "nearly 40 countries representing $50 trillion in GDP"; partner data centers >10MW "nearly doubled… surpassing 80 sites"; Vera CPU "$200 billion TAM… ~$20 billion in total CPU revenue this year"; "physical AI… exceeding $9 billion… over the last 12 months"; Anthropic "across Azure, AWS, CoreWeave"; Uber robotaxi "nearly 30 cities and four continents by 2028."
- **2026Q4 remarks:** networking "$11 billion… up more than 3.5x"; "Physical AI… over $6 billion in… fiscal year 2026."
- **2027Q1 Q&A:** "we are the only company that builds all of the technology components… full stack" (`qa:15`); "buying systems rather than designing or building custom chips" (`qa:24`); "NVIDIA is practically the only company serving them today… growing share in inference" (`qa:33`); "hundreds of thousands of companies" (`qa:23`).
- **2026Q2 trough call (retired; used in SQ1 only):** "grew sequentially despite the $4 billion decline in H20 revenue"; China "to low single digits percentage of data center revenue"; "began production shipments of GB300 in Q2… approximately 1,000 racks per week… expected to accelerate… throughout the third quarter."

## Competitors — earnings calls (SQ6)
- **AVGO 2026Q2 (Tan):** "AI semiconductor revenue at a record $10.8 billion, up 143%… Networking… almost 40%"; "bookings… over $30 billion against the $10.8 billion we shipped"; "full year 2026… $56 billion, up ~180%"; "fiscal year 2027… in excess of $100 billion." Google "multiple generations of TPUs and AI networking"; Anthropic ">1 gigawatt… another 5 gigawatts… beginning in 2027"; OpenAI "1.3 gigawatts in 2027… 10-gigawatt by 2029"; Meta "3 gigawatts through the end of 2028." "gaining share in networking… whether they use XPUs or GPUs." AI XPU platform "with Apollo, Blackstone… more than 20 gigawatts… first tranche… $35 billion."
- **AMZN Q2 2026 (Jassy):** "chips business now has an annual revenue run rate of over $25 billion, growing triple-digit"; "Anthropic and OpenAI, making multi-year, multi-gigawatt commitments to Trainium"; "customers… run on Nvidia for as long as we can foresee… customers want choice."
- **GOOG Q2 2026 (Ashkenazi/Pichai):** "began to recognize revenues from TPU system sales… to customer data centers for the first time… vast majority… realized in 2027"; "Google and NVIDIA, including the new NVIDIA Vera Rubin platform, and TPU"; "Axion CPU provides 30% better performance per dollar"; "workload portability across GPUs and TPUs."
- **MSFT FY26 Q4 (Nadella):** "Maia 200… 30% better performance per dollar than the latest-generation hardware in our fleet… supporting both OpenAI and MAI models"; "among the first cloud providers to deploy… NVIDIA Vera Rubin."
