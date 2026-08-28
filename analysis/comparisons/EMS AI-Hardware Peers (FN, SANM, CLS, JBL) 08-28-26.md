# EMS / AI-Hardware Peer Comparison — FN, SANM, CLS, JBL

## Context

Fabrinet (FN), Sanmina (SANM), Celestica (CLS), and Jabil (JBL) all do roughly the same thing: contract manufacturing / EMS (electronics manufacturing services), building hardware to customer designs (or, increasingly, co-designing it) rather than selling their own branded products. All four have been swept up in the AI-infrastructure buildout to varying degrees, and each has its own full single-company analysis in `analysis/stock analysis/`. This note isn't a repeat of those — it's a narrower, focused comparison across the four on the dimension that matters most for the investment case: **growth** — how fast each is actually growing right now, how much of that is real, and which is best positioned to keep growing. A brief affordability comparison (EV/Sales, P/E) is included at the end, but de-emphasized relative to growth.

Full single-company write-ups: `FN 08-28-26.md`, `SANM 08-24-26.md`, `CLS 08-26-26.md`, `JBL 08-27-26.md` (all in `analysis/stock analysis/`).

---

## 1) Current growth — the qualitative picture

**On reported headline numbers, the order is SANM > CLS > FN > JBL — but that ordering is misleading for SANM.** Strip out its acquisition and the real organic order becomes **CLS > FN > JBL > SANM**.

- **FN** — growing very fast (mid-40s% YoY) and still building. The AI-specific piece (Data Center revenue) is growing even faster than the company overall and is now over half of sales. This is real, organic growth, and by management's own account currently constrained by supply (components), not demand.
- **CLS** — growing fast (low-60s% YoY) and has accelerated every quarter for a full year, entirely organic. The AI/cloud piece (CCS) grows meaningfully faster than the company average, and the highest-margin sub-piece within it (HPS, the co-designed business) is growing rapidly too and is now a large minority of total revenue.
- **SANM** — the headline (high-50s%, briefly triple-digits in one quarter) is **overwhelmingly an artifact of the ZT Systems acquisition** (closed October 2025), not organic demand doubling. In the quarter that spiked to ~100%+, ZT alone contributed roughly half of total revenue against a prior-year comp of zero (Sanmina didn't own it yet) — that's mechanically how a spike that size happens. Strip ZT out and "Core Sanmina" is growing low-double-digits — real, but the *slowest* organic growth of the four. The subsequent deceleration (from ~100% to ~70%) also isn't a demand slowdown: it's ZT's own revenue falling quarter-over-quarter as legacy programs wound down ahead of the next-gen ramp. The true YoY comp-base effect from lapping the acquisition hasn't even hit yet.
- **JBL** — slowest of the four, and it just decelerated sharply (roughly halved quarter over quarter). Checked directly against segment data: the slowdown was concentrated almost entirely in Jabil's own AI-exposed segment (Intelligent Infrastructure), which itself decelerated from the low-50s% down to the low-20s% — more than enough on its own to explain the whole-company slowdown. The segments outside the AI story (Regulated Industries, Connected Living/Digital Commerce) were flat-to-improving over the same stretch. So this is the opposite of "AI held up while the rest dragged it down" — the AI segment cooled while the rest stayed steady. One nuance: within that segment, networking specifically stayed very strong (aided by an India ramp); it was the cloud/data-center-infrastructure and capital-equipment pieces that slowed.

**AI-specific growth, isolated from total revenue:**

| | AI/cloud-specific growth | vs. total company growth, same period |
|---|---|---|
| FN | Data Center revenue ~68% YoY | ~45% |
| CLS | CCS ~84% YoY (HPS sub-piece +58%) | ~62% |
| SANM | Organic (ex-ZT) Comms/Cloud/AI ~33% YoY | Consolidated ~70% (ZT-inflated, not comparable) |
| JBL | Company-defined "AI-related revenue" ~50% YoY (full year) | ~18% |

FN's and CLS's AI-specific growth runs *faster* than their already-fast totals; SANM's real (ex-ZT) AI growth is solid but a fraction of the headline number; JBL's AI revenue is growing far faster than its total company number, which is exactly why the deceleration inside that segment matters so much to the overall picture.

## 2) Potential future growth — positioning vs. the sector thesis

Per `Sectors.md`, AI infrastructure hardware overall sits in "**Mid-Late acceleration**" — currently decommoditized (innovation still matters) but headed toward commoditization that eventually favors low-cost producers. Within hardware, **networking/optics is called out as the durable exception** — "Ethernet optics on a path to a $100 billion market by 2030," with moats "closer to software" than the rest of the stack. Custom-ASIC racks are also called out as a rising share of AI servers (~40% by 2030). Aerospace/defense is flagged separately as its own real-demand growth theme.

- **CLS — best positioned.** Sits squarely in the "durable" networking/optics category: first production-scale CPO switch (Broadcom Tomahawk 6), AMD Helios, OpenAI/Broadcom custom rack. Management says most of this doesn't hit volume until 2027–2029 — the runway is long and largely still ahead, not already captured in today's growth rate.
- **FN — close second.** The purest play on the same durable niche (DCI, transceivers, HPC), but further along its current S-curve (~$1B DCI run-rate already). Its next leg (CPO/NPO, new hyperscaler-direct and merchant transceiver programs) is explicitly early. Near-term growth is capped by component supply, not demand.
- **SANM — weaker positioning.** Exposed to the custom-ASIC-share trend via AMD/ZT, but the next-gen program isn't even in guidance yet, and its pace depends on AMD's own ramp decisions — described in the 10-Q as "largely outside of our control." This sits more in the eventually-commoditizing compute-assembly bucket than in the durable networking category (see moat discussion below), and Sanmina isn't positioned as the low-cost producer that wins that later phase.
- **JBL — most diversified, least concentrated bet.** Real AI upside (3rd hyperscaler ramping FY27–28, power/liquid-cooling build via Hanley/Mikros — relevant to the power/cooling bottleneck the sector notes flag), but growth is spread across a broader mix including recovering-but-cyclical auto/industrial. Best floor, least explosive ceiling.

**Ranking, best-to-worst positioned for continued/accelerating growth: CLS > FN > SANM > JBL.**

### On "moat" — none of the four has one

None of the four has a real, defensible moat, and this is consistent across all four company analyses. Every 10-K in the set says some version of the same thing: patents "have not played a significant role," R&D is negligible-to-modest (FN ~0%, JBL 0.1%, SANM 0.3–0.4%, CLS the highest at ~1.0% — still low), and dual-sourcing the same program across competitors is standard industry practice. What they lean on instead is soft, execution-based advantage: multi-month customer qualification processes that create switching costs, manufacturing scale, and long-standing certifications (aerospace, medical, automotive) — not patents or brand. That's true of all four; it isn't a differentiator between them.

The "eventually commoditize" framing applied more to SANM above isn't about its business model being different from the others — they're all the same low-moat contract-manufacturing model. It's about **which specific AI product layer** each company's incremental growth is coming from. `Sectors.md` draws a line within AI hardware: general compute/server assembly (racks, servers) is the more generic, commoditizing layer, while networking/optics (switches, transceivers, interconnects) is called out as the durable exception because of how fast that layer's technology turns over and how much qualification-driven lock-in it creates. SANM's fastest-growing product right now (ZT's AMD racks) sits in the more generic assembly layer; CLS's and FN's fastest-growing products (switches, DCI, transceivers, CPO) sit in the layer flagged as unusually durable. JBL's AI growth is a mix of both, plus networking specifically — which, notably, is the one piece of its AI segment that didn't decelerate.

### Aerospace/defense exposure

| | Exposure | Size |
|---|---|---|
| **SANM** | Real — SCI subsidiary, 60+ year history, defense primes and U.S. government/allied customers (aircraft systems, tactical comms, drones, missile guidance, satellite control) | Not broken out; bundled into a combined "Industrial, Medical, Defense & Aerospace, Automotive" segment (~$3.78B over the first 9 months of FY26 — one of four pieces of that bucket) |
| **CLS** | Real — Aerospace & Defense is one of four named businesses in the ATS segment | Not broken out; ATS overall was $3.2B (FY25, 27% of revenue), but A&D shares that with Industrial, HealthTech, and Capital Equipment (named customers include semicap names like Applied Materials/LAM, suggesting A&D is a modest slice, not most, of the $3.2B) |
| **FN** | None as a business — holds an AS9100 aerospace quality certification only | N/A — actual end markets are Data Center, Communications Infrastructure, Automotive/Industrial/Other |
| **JBL** | None disclosed | N/A — its three segments have no aerospace/defense category |

SANM has the largest, most established aerospace exposure of the four (a genuine 60-year-old defense franchise), CLS has a real but smaller/unsized slice, and FN and JBL have none.

## Bonus: affordability (light touch)

| | EV/Sales | GAAP P/E | Adj. P/E |
|---|---|---|---|
| FN | 3.18x (priciest) | 31.94x | 29.93x |
| SANM | 0.83x (cheapest) | 32.61x | 17.67x |
| CLS | 2.28x | 31.57x | 37.56x |
| JBL | 1.05x | 38.46x | 25.98x |

Notable mismatch: SANM is cheapest on EV/Sales despite the highest headline growth rate — the market is discounting it for being mostly acquisition-driven. CLS carries the richest EV/Sales after FN, consistent with it having the cleanest organic-acceleration story of the four.
