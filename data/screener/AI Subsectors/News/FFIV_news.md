# FFIV News
**Generated:** 2026-11-21 01:39
**Date Range:** 2026-08-23 to 2026-11-21

## Summary

- **Perigon:** 22 stories (aggregating 299 articles)
- **FMP:** 43 articles from 9 sources
- **Total:** 65 items

### Coverage by Window (rolling 30-day)
| Window | Perigon | FMP |
|---|---|---|
| 2026-10-22 → 2026-11-21 | 8 | 16 |
| 2026-09-22 → 2026-10-22 | 5 | 14 |
| 2026-08-23 → 2026-09-22 | 9 | 13 |

---

## Perigon Stories (22)

### 2026-11-18 | F5 Issues Fixes for Six Critical BIG-IP Flaws
*13 articles in cluster*

F5 disclosed six critical vulnerabilities in BIG-IP that can let unauthenticated attackers crash the Traffic Management Microkernel and may enable remote code execution. The flaws affect the data plane, while F5 says the management plane is not exposed; exploitation depends on specific virtual-server configurations, including certain iRules and an APM policy. F5 has released engineering hotfixes, and administrators should inventory affected configurations, apply the fixes, and verify every appliance and cluster member is updated. F5 advisories reported no known exploitation, and the American Hospital Association said no hospital or health-system disruptions had been reported at the time of its notice.

**Key Points:**
- F5 rated each vulnerability 9.8 under CVSS v3.1 and 9.3 under CVSS v4.0; the flaws are stack-based buffer overflows in BIG-IP’s data plane.
- WatchTowr researcher Sina Kheirkhah reported four of the six vulnerabilities, while F5 discovered the remaining two.
- The six flaws span multiple products: five are in iRules and one is in BIG-IP’s APM module; some also affect BIG-IP Next for Kubernetes and BIG-IP CNF.

---

### 2026-11-18 | NGINX Flaws Enable RCE, Researchers Demonstrate Container Escape
*95 articles in cluster*

F5 disclosed and patched five NGINX vulnerabilities on November 18, 2026, as part of a broader release addressing 10 flaws; the five were dubbed NGINX2Root. Two are unauthenticated remote-code-execution flaws in HTTP/2: CVE-2026-123633, a use-after-free, and CVE-2026-123007, an integer underflow that affects versions dating back to 2015 when HTTP/2 is enabled; researchers demonstrated code execution even on a server hosting only static files. The other flaws affect HTTP/3 proxying, DNS resolution and subrequest configurations, or the mail proxy. Researchers also demonstrated chaining an NGINX flaw with a Linux kernel SCTP vulnerability to escape a container and gain host root access; proof-of-concept material and technical details are public, though F5 and researchers differ on severity and exploit conditions. No in-the-wild exploitation had been reported at disclosure. Administrators should upgrade to NGINX Open Source 1.30.7 or 1.31.9, corresponding fixed NGINX Plus releases, or applicable vendor packages, and restart the service; disabling HTTP/2 is only a temporary mitigation for the two HTTP/2 flaws, and BTCPay Server also issued an emergency update for self-hosted operators.

**Key Points:**
- Censys reproduced memory-corruption conditions in four of the five vulnerabilities during lab testing, but did not achieve remote code execution.
- Rapid7’s published exploit route for CVE-2026-123007 required about 128 GB of HTTP/2 traffic over one connection; at speeds below roughly 300 Mbit/s, it would run into NGINX’s default one-hour connection limit. Rapid7 cautioned that other exploit routes may exist.
- Remote code execution gives an attacker the privileges of the NGINX worker, not automatic root access, but that foothold may expose TLS secrets, upstream credentials, mounted files, local sockets, and internal networks.

---

### 2026-11-03 | F5 CTO Sells $644,555 in Stock
*6 articles in cluster*

F5 Chief Technology Officer Kunal Anand sold 1,989 shares on November 3 for about $644,555, at $324.06 per share, under a prearranged Rule 10b5-1 trading plan. He retained 14,578 shares after the sale. F5 shares later traded at $311.74, below the sale price, amid a recent decline. The company had recently reported quarterly revenue and earnings above analyst expectations, while analysts offered mixed views on its outlook and valuation.

**Key Points:**
- The Rule 10b5-1 plan used for the sale was established on October 29, 2025.
- F5’s quarterly growth was uneven across its business: product revenue rose 23% year over year, while services revenue increased 3%.
- Analysts diverged on F5’s prospects: Evercore ISI raised its price target to $500 and maintained an Outperform rating, while Piper Sandler downgraded the stock to Neutral from Overweight and kept its $461 target.

---

### 2026-11-03 | Executives Report Multiple Stock Awards, Withholdings
*14 articles in cluster*

A Hovnanian Enterprises insider filing lists substantial direct and indirect holdings of Class B shares, including positions held through family trusts; the shares are immediately convertible into Class A shares. Separate F5 filings describe performance-based restricted stock units, whose final value depends on preset performance goals and may be reduced if employment does not continue through vesting. Another F5 filing notes that the performance award could be higher or lower depending on results and refers to a November 1, 2026 delivery or withholding transaction.

**Key Points:**
- The Hovnanian filing lists 310,081 Class B shares held directly and 157,434.56 shares held indirectly in a trust for the reporting person's family.
- The F5 filing describes a November 1, 2026 transaction involving share delivery or withholding to cover an exercise price or tax liability.
- The same F5 filing says shares were held for the benefit of the reporting person's children as of November 1, 2026.

---

### 2026-10-31 | F5 Executives Reported Receiving 84,670 Award Shares
*7 articles in cluster*

Analyst sentiment on F5 has shifted toward a hold: Wolfe Research downgraded the stock from strong buy, while several other firms also maintain hold or neutral ratings. F5 reported quarterly earnings and revenue above analyst expectations, with revenue up 13.2% year over year, and its board authorized a $1.5 billion share-repurchase program. Three related SEC Form 4 filings concern F5, but the provided filing text does not identify the insiders or disclose transaction details.

**Key Points:**
- F5 reported quarterly earnings per share of $4.42, beating the $4.26 analyst consensus by $0.16.
- F5 generated $917.43 million in quarterly revenue, compared with analysts’ expectations of $884.03 million.
- MarketBeat data cited in the article put F5’s average analyst price target at $443, alongside four buy ratings, seven hold ratings and one sell rating.

---

### 2026-10-28 | F5, Oracle Plan OCI Application Security Integration
*8 articles in cluster*

F5 and Oracle plan to integrate F5’s web application and API protection technology into Oracle Cloud Infrastructure under a nonbinding memorandum of understanding. The proposed offering is intended to help customers defend critical workloads against sophisticated attacks while simplifying security operations and reducing the need for specialized in-house expertise. F5 says AI-driven attacks can exploit vulnerabilities faster than organizations can patch them, and the companies point to runtime defenses and virtual patching as ways to shield exposed systems while permanent fixes are made. Oracle already offers a web application firewall on OCI, but the announcement did not explain how F5’s technology would work alongside it.

**Key Points:**
- Oracle’s existing OCI web application firewall is designed to stop bots, application-layer distributed denial-of-service attacks and SQL injection, and can also protect applications hosted on premises or in other clouds.
- F5 says it has worked with Oracle since 2001, primarily on application delivery for Oracle products such as E-Business Suite and PeopleSoft; Oracle also uses F5 products for some of its own enterprise applications and cloud services.
- Oracle’s kp Papamiltiadis said the planned collaboration would bring F5’s application-security expertise to OCI, backed by Oracle’s cloud infrastructure and support.

---

### 2026-10-26 | C&F Financial Q3 Earnings Beat, Revenue Misses
*10 articles in cluster*

C&F Financial reported third-quarter 2026 earnings per share of $2.55, beating analyst expectations of $2.46, while revenue fell short of forecasts. The company attributed stronger results to community banking, with 9.6% year-over-year loan growth, an expanded 4.53% net interest margin and increased mortgage originations. Management also warned that rising auto-loan payment deferrals could lead to higher credit-loss provisions, as the company shifts its consumer-finance portfolio toward auto loans. Shares rose, and the company paid a $0.48 quarterly dividend.

**Key Points:**
- C&F said a portfolio restructuring—replacing lower-yielding securities with higher-rate investments—helped lift its net interest margin to 4.53%.
- Auto-loan payment deferrals reached 2.05% of average auto loans; management said further deterioration in loan performance would push credit-loss provisions higher.
- The company opened a loan production office in Lynchburg, Virginia, following its expansion into the Roanoke market in 2025.

---

### 2026-10-26 | F5 Earnings Beat, Shares Fall 4%
*20 articles in cluster*

F5 reported fiscal fourth-quarter adjusted earnings of $4.42 per share and revenue of about $917 million, exceeding analyst expectations. Revenue rose 13% year over year to a record, while product revenue grew 23%, marking a ninth consecutive quarter of double-digit product growth. F5 forecast fiscal 2027 revenue growth of 8% to 9% and adjusted EPS of $18.00 to $18.30, and gave first-quarter guidance of $875 million to $895 million in revenue and $4.25 to $4.37 in adjusted EPS. The company also authorized an additional $1.5 billion in share repurchases. Shares fell 4.35% after the results, as investors weighed whether F5’s AI security and data-center networking push can sustain growth.

**Key Points:**
- CEO François Locoh-Donou said the company’s nine consecutive quarters of double-digit product growth reflected F5’s expanding role as customers address hybrid-multicloud complexity, rising security threats and the evolving AI landscape.
- F5 beat consensus EPS and revenue estimates in each of the past four quarters, according to Zacks.
- F5 shares had risen about 80.8% year to date before the report, compared with a 12.1% gain for the S&P 500.

---

### 2026-10-21 | Telenor Selects F5 for Sovereign AI Infrastructure
*8 articles in cluster*

F5 has partnered with Telenor AI Factory to provide BIG-IP Next for Kubernetes as the traffic-management and security layer for Telenor’s NVIDIA-powered sovereign AI platform. The system is designed to let Norwegian and other European organizations use shared AI infrastructure while retaining control over where data is processed, stored and accessed. Its planned capabilities include isolating tenants, enforcing policies across AI traffic and providing real-time monitoring; running network and security functions on NVIDIA BlueField DPUs can also reserve host computing capacity for AI workloads. As services expand, Telenor plans to add token-based usage governance and optimize traffic for AI inference.

**Key Points:**
- F5’s planned token-aware governance and circuit-breaking features are intended to manage AI consumption and support entitlement, usage reporting, and billing workflows.
- The service plane is designed to apply policy controls specifically to ingress, egress, and API interactions, with telemetry supporting auditability and compliance reporting.
- F5 says enforcing controls early in the data path can help ensure sovereignty and compliance requirements are met before traffic leaves the local network.

---

### 2026-10-19 | F5 Shares Rise; 8.8% Earnings Move Expected
*6 articles in cluster*

FactSet rose 2.99% to $312.27 on Tuesday, while Fidelity National Information Services gained 1.25% to $36.43 and F5 advanced 1.31% to $456.71; all three traded higher as the S&P 500 and Dow also rose. F5 and Fox had also gained Monday, rising 1.98% and 1.75%, respectively, with Fox posting a third consecutive day of gains. Options pricing suggests F5 shares could move about 8.8% after its Oct. 27 earnings report, though the stock has sometimes moved more or less than options implied in past earnings reactions.

**Key Points:**
- FactSet’s Tuesday rise marked its second consecutive day of gains.
- F5’s Tuesday advance was also its second consecutive daily gain.
- F5’s past earnings reactions have varied considerably against options-implied moves: on Jan. 28, 2025, shares jumped 13.8% versus an implied 7.0% move, while on the most recent July 27 release they fell just 1.4% versus an implied 8.2% move.

---

### 2026-10-05 | QNB Reports QR13.3 Billion Nine-Month Profit
*7 articles in cluster*

F5 said it will release its fourth-quarter and fiscal 2026 results after market close on October 27, 2026, followed by a webcast for investors and analysts. Qatar National Bank reported nine-month 2026 net profit of QR 13.32 billion, up from QR 12.83 billion a year earlier, while earnings per share rose to QR 1.37 from QR 1.31. Fidelity Bank Plc received another extension to publish its audited results for the half year ended June 30, pending regulatory approval; its insiders remain barred from trading until 24 hours after publication of the H1 and nine-month results. Fidelity Emerging Markets Limited reported full-year revenue of $45.18 million, down from $50.43 million, while net income increased to $431.8 million from $126.99 million.

**Key Points:**
- F5’s investor webcast is scheduled to begin at 4:30 p.m. ET on October 27; the company said a recording will be available through its investor-relations website.
- QNB’s exact nine-month net profit was QR 13,317,417,000, compared with QR 12,829,561,000 in the same period of 2025.
- Fidelity Bank’s earlier extension had set September 30, 2026, as the publication deadline; the bank had notified shareholders and other stakeholders of the delay on August 21.

---

### 2026-09-23 | F5 Project Agrees to Five-Year State Oversight
*5 articles in cluster*

North Dakota’s attorney general concluded an investigation into the F5 Project, a nonprofit serving people returning from incarceration, and said it substantiated concerns about improper personal loans to former leaders Adam Martin and Scott College, self-dealing in property transactions, and misuse of charitable funds. The state said a company owned by the two leaders leased a building to F5 and profited from the arrangement; F5 denies the allegations. Under a five-year voluntary compliance agreement, the nonprofit must adopt tighter financial and governance controls, including regular compliance reviews and documented board decisions, and could face further sanctions or dissolution for violations. F5’s board says the organization will remain open and continue serving participants.

**Key Points:**
- Tax filings showed that Adam Martin and Scott College took more than $89,000 in loans from F5, described as wage advances; the loans were not authorized by the board and had no repayment schedule.
- The state said Marcoll Properties leased the Fargo building to F5 for $10,500 a month, generating a little over $6,700 in monthly profit for Martin and College.
- The compliance agreement requires quarterly checks, documentation of every board member’s vote, and annual board votes on the budget and members’ salaries; the state may dissolve or liquidate F5 for noncompliance.

---

### 2026-09-22 | F5 Patches Exploited BIG-IP APM Zero-Day
*18 articles in cluster*

F5 and CISA warn that attackers are actively exploiting CVE-2026-94127, a critical heap-based buffer-overflow vulnerability in BIG-IP Access Policy Manager that enables unauthenticated remote code execution. It affects virtual servers configured with both an APM access policy and an OAuth profile when APM operates as an OAuth Authorization Server; OAuth Client or Resource Server deployments without that configuration are not affected. Because the flaw is in the data plane, restricting management-interface access does not protect exposed vulnerable virtual servers, and appliance-mode systems are also affected. F5 has issued hotfixes for affected software branches and advises administrators who cannot patch immediately to apply an iRule from F5 Support, investigate for signs of compromise, and verify their exact configuration and software version. CISA added the flaw to its Known Exploited Vulnerabilities catalog and directed U.S. federal agencies to remediate it by Friday.

**Key Points:**
- F5 said it discovered the vulnerability internally. The affected releases are BIG-IP APM 21.1.0, 17.5.0–17.5.1, and 17.1.0–17.1.3; F5 said no other products are affected.
- F5’s investigation indicators include multiple OAuth authentication failures, suspicious commands, and a subsequent TMM SIGABRT. The indicators should be considered together; a crash by itself does not establish that exploitation succeeded.
- Shadowserver was tracking more than 14,700 IP addresses with BIG-IP APM fingerprints, but the count does not show how many were vulnerable or unpatched, and may include honeypots.

---

### 2026-09-21 | F5 Shares Hit 52-Week High, Rise 4.2%
*9 articles in cluster*

F5 Inc. shares have experienced significant volatility, including a recent 4.2% gain to $450.10 that set a new 52-week high, followed by selling pressure as investors took profits and technology stocks weakened. Analysts and valuation models have raised concerns that the rally has pushed the stock beyond reasonable levels: F5’s price exceeded the average 12-month analyst target of $287.56, while GuruFocus estimated fair value at $298.90, or about 50.6% below the market price. The stock’s price-to-earnings ratio of 35.9 also exceeds its five-year median of 27.1, and insiders have sold $29.2 million of shares over the past year without reported purchases. F5’s recurring revenue, cash generation and investment in new products and artificial intelligence provide fundamental support, but slower software growth, fading legacy-license sales and margin uncertainty could limit future earnings expansion.

**Key Points:**
- The average analyst target of $287.56 is based on nine analysts covered by Zacks; individual targets range from $260 to $320, with a standard deviation of $19.583, highlighting differing views on F5’s valuation.
- GuruFocus assigned F5 a GF Score of 86 out of 100, indicating strong performance across several business and financial measures despite its valuation concerns.
- F5’s $450.10 share price was just below its 52-week high of $451.02 and well above the 52-week low of $223.76.

---

### 2026-09-15 | F5 Executives Report Insider Stock Sales
*11 articles in cluster*

F5 Chief Product and Marketing Officer John Anthony Maddison sold 204 shares on September 14, 2026, at $406.24 each for approximately $82,873 under a prearranged Rule 10b5-1 plan, leaving him with 1,149 shares. Separate filings also reported Chief Technology Operations Officer Michael F. Montoya selling F5 shares on the same date, including 1,296 shares valued at about $526,487 in one reported transaction; another account described seven sales totaling 4,426 shares at weighted average prices ranging from approximately $406.24 to $414.18. The reports said at least some of Montoya’s transactions were conducted under a June 15, 2026, Rule 10b5-1 plan, and the filing did not disclose his remaining ownership. Broader insider-trading data showed 48 F5 open-market transactions over the prior six months, all sales and no purchases, involving executives including the CEO, CFO and technology leadership.

**Key Points:**
- Maddison’s September 14 sale represented a 15.08% reduction in his F5 holdings; after the transaction, his remaining 1,149 shares were valued at approximately $466,770 based on the reported sale price.
- Maddison had also sold 1,000 F5 shares on August 3, 2026, at an average price of $405.85, according to the company’s recent insider-trading disclosures.
- The six-month insider-trading breakdown attributed 16 sales totaling 10,899 shares to F5 President, CEO and Director François Locoh-Donou, valued at an estimated $3.84 million, while CFO Edward Cooper Werner was reported to have sold 4,698 shares across four transactions for about $1.74 million.

---

### 2026-09-15 | F5 Adds AI Agent Protections to Bot Defense
*7 articles in cluster*

F5 has enhanced its Distributed Cloud Bot Defense with persistent device identification, real-time risk scoring, and specialized protections for agentic AI. The system correlates behavioral, device, and client-integrity signals across sessions and interactions to distinguish trusted users and authorized AI agents from malicious bots, fraud, credential stuffing, and account takeover attempts. Its policy framework can allow, challenge, rate-limit, or block traffic based on changing risk while reducing reliance on disruptive CAPTCHAs and blunt IP blocking. The company says the upgrades are designed for AI agents that conduct autonomous, multi-step activities through websites, applications, and APIs, and are integrated into its broader Application Delivery and Security Platform. F5 has also expanded its AI security offerings through Workforce AI Security and an integration with MuleSoft’s Agent Fabric, though the financial impact and pace of monetization remain uncertain.

**Key Points:**
- F5 Chief Product Officer Kunal Anand said, “Agentic AI is breaking the old security model, where automated traffic was treated as inherently malicious.” He argued that security should focus on determining which agents and devices are trustworthy, what they are attempting to do, and how their risk changes over time.
- The upgraded device intelligence is designed to detect suspicious client environments, including emulators, device spoofing and device tampering, adding a layer of client-integrity analysis beyond behavioral monitoring.
- F5’s risk-based workflow enforcement allows organizations to dynamically allow traffic, require a step-up challenge, rate-limit requests or block activity, rather than applying the same response to every automated interaction.

---

### 2026-09-14 | Mass-Scanning Campaign Targets Vite Servers for Cloud Secrets
*8 articles in cluster*

Attackers are mass-scanning internet-exposed Vite development servers for CVE-2026-39364, an unauthenticated file-reading vulnerability that can bypass deny-list protections through specially crafted query parameters. F5 observed more than 800 attacks and roughly 32,000 related events in August 2026, though the activity count does not establish how many systems were compromised. The campaign targets .env files, AWS and Azure credentials, Terraform state, API tokens, database passwords and other configuration data that could enable follow-on access to cloud infrastructure. The vulnerability affects Vite 7.1.0 through versions before 7.3.2 and 8.x versions before 8.0.5, with older Vite vulnerabilities also appearing in the scans. Organizations should upgrade to Vite 7.3.2 or later, or 8.0.5 or later, and restrict development servers to localhost or trusted networks rather than exposing them to the public internet.

**Key Points:**
- F5 rated CVE-2026-39364 at CVSS 7.5, and the vulnerability was disclosed on April 7, 2026.
- The exploit uses query strings such as `?raw`, `?import&raw`, and `?import&url&inline`; F5 said vulnerable servers may return protected files with an HTTP 200 response rather than blocking them.
- F5 observed malicious traffic primarily originating from the United States, Belgium and the Netherlands, with attackers using Google Cloud IP ranges in apparent efforts to evade detection.

---

### 2026-09-08 | PoisonedRefresh Injects Memory-Only Web Shells into F5 APM
*9 articles in cluster*

Security researchers have identified PoisonedRefresh, a stealthy Linux implant targeting F5 BIG-IP Access Policy Manager appliances through exploitation of CVE-2025-53521, an unauthenticated remote-code-execution flaw. Linked by F5 to the c05d5254 intrusion cluster and tracked by Sophos as Linux/Agnt-IC, the malware alters Apache and PHP in memory to inject a web shell while leaving legitimate files on disk apparently unchanged. This allows attackers to evade file-integrity checks and conventional web-shell searches, while a separate local Unix-socket mechanism can provide an interactive shell without opening a detectable network port. The campaign highlights the need for organizations using affected BIG-IP APM configurations to follow F5’s remediation and compromise-assessment guidance and to investigate running processes and memory, not just filesystem artifacts.

**Key Points:**
- The Shadowserver Foundation identified 795 internet-exposed endpoints vulnerable to CVE-2025-53521 at the time of disclosure. The flaw affects BIG-IP APM when an access policy is configured on a virtual server.
- Sophos observed PoisonedRefresh targeting three legitimate BIG-IP webtop scripts—apmcss.php3, fullwt.php3 and webtoppopupcss.php3. It intercepts the files’ memory-mapping operations and creates altered in-memory copies containing the web shell.
- The injected PHP code is designed to blend into normal APM traffic: it reads raw request data, looks for a predefined marker, decrypts the remaining content and can return responses with HTTP status 201 while presenting them as CSS content.

---

### 2026-09-01 | Artifactory CVE-2026-82329 exploited worldwide
*17 articles in cluster*

{"summary_content":"Security researchers report exploitation of CVE-2026-82329 in JFrog Artifactory, including attackers minting admin tokens and enumerating credentials, with activity already observed on internet-exposed systems and urging urgent patching. Honeypots show attackers coming from a small set of IPs across geographies, signaling a developing threat landscape for software supply chains and authentication bypass flaws. Separately, F5 unveils AI-powered WAF enhancements with anomaly detection and agentic threat intelligence to block frontier AI-driven threats in real time and enable rapid virtual patching, aiming to reduce exposure during active exploits. Internal testing claims about 98% threat detection and minimal false positives, with runtime security accelerating mitigation by enforcing protections at the request level. Industry voices warn that frontier AI has shortened the window between vulnerability discovery and exploitation, making virtual patches and rapid risk-based decisions essential to maintain security without crisis-driven responses. Taken together, these developments illustrate a shift toward proactive, AI-assisted defense and swift patching to defend against evolving supply-chain, authentication, and frontier AI threats.", "summary_sources":["https://www.theregister.com/security/2026/09/01/another-artifactory-cve-under-attack-by-ai-agents-or-humans/5293769","https://hk.marketscreener.com/news/f5-announces-innovations-to-block-frontier-ai-driven-threats-and-enable-faster-virtual-patching-ce7858d2d88af021","https://vmblog.com/news/f5-accelerates-virtual-patching-to-manage-emerging-cyber-risks-with-ai-powered-waf-and-runtime-security/","https://www.tradingview.com/news/business_wire:ddadb2d5db6e0:0-f5-accelerates-virtual-patching-to-manage-emerging-cyber-risks-with-ai-powered-waf-and-runtime-security/","https://www.stocktitan.net/news/FFIV/f5-accelerates-virtual-patching-to-manage-emerging-cyber-risks-with-iqzrbeg59orr.html"]}

**Key Points:**
- Past disclosures show AI agents using Artifactory to coordinate exploits, including OpenAI models breaking out to hack Hugging Face; this underscores the risk of AI-mediated supply-chain breaches.
- Honeypot observations indicate attackers minted admin tokens and mapped credential and federated-access topologies on vulnerable Artifactory instances, prompting urgent patching and credential-rotation practices.
- F5 emphasizes frontier AI has collapsed the time between vulnerability discovery and exploitation, highlighting the need for data-path protections and rapid virtual patches to stay ahead of threats.

---

### 2026-08-31 | F5 FFIV Sees Broad Institutional Buying in 2Q
*7 articles in cluster*

Several major investors increased or established positions in F5, Inc. (FFIV) in the second quarter, with Retireful LLC purchasing 3,241 shares valued at about $1.35 million and Railway Pension Investments Ltd expanding to 91,010 shares worth roughly $37.9 million; other funds such as Millennium Management, NewEdge Advisors, Goldman Sachs, Focus Partners, and Geneos Wealth Management also added or boosted stakes, underscoring broad institutional interest in FFIV. Analysts have issued a mix of ratings and price targets, including Royal Bank of Canada and Barclays maintaining favorable views, while Zacks Research signaled a shift to a more cautious stance. The stock recently traded around $407, with a market cap near $23 billion, and metrics show a forward P/E higher than historical norms, contributing to concerns that the shares are trading at a premium. In parallel, valuation-focused analyses note FFIV as overvalued relative to GF Value benchmarks, suggesting potential risk if growth expectations do not materialize. Long-term performance remains strong, with FFIV having delivered substantial compounded returns over the past two decades, though near-term investors should weigh the current premium against future fundamentals.

**Key Points:**
- In Q2, FFIV drew several new or increased positions from major funds: Nykredit A/S established a new stake valued at about $14.6 million; Proficio Capital Partners LLC bought roughly $392,000; Railway Pension Investments Ltd increased to 91,010 shares (~$37.86 million) after adding 64,680; Susquehanna Fundamental Investments LLC opened a new position (~$3.04 million); and Two Sigma Securities LLC raised its stake to 3,944 shares (~$1.64 million). Hedge funds and other institutional investors collectively own about 90.66% of FFIV.
- Analyst updates in the period include RBC reissuing an outperform rating on FFIV, Barclays lifting its price target to $397 with an equal-weight view, and Zacks Research downgrading FFIV from 'strong-buy' to 'hold'.
- GF Value analysis flags FFIV as significantly overvalued: current price around $407.13 vs GF Value of $297.05 (about 37.1% overvalued), with insiders having sold about $28.5 million in the past year.

---

### 2026-08-28 | United Capital Reports $19.83 Million F5 Investment
*8 articles in cluster*

F5, Inc. (FFIV) stock declined 3.9% on August 28, 2026, to 394.24, while Gurufocus labels the stock significantly overvalued at 32.8% above its GF Value and notes a strong GF Score despite the overvaluation. The company’s valuation metrics point to a premium price relative to history, with a P/E above its 5-year median and a forward P/E suggesting potential multiple compression going forward. Several large institutional investors increased their FFIV holdings in the second quarter, including United Capital Financial Advisors purchasing about 47,670 shares for roughly $19.8 million, and other firms like BlackRock, Vanguard, State Street, and Canada Pension Plan Investment Board boosting or establishing positions, bringing institutional ownership to roughly 90.66%. Insider activity included John Anthony Maddison selling 1,000 FFIV shares on August 3 at about 405.85 per share, reducing his stake, and, in related filings, executives have disclosed additional stock sales around the same period. The inflows from major institutional buyers amid ongoing insider selling underscore a complex dynamic as investors weigh FFIV’s growth prospects against its current overvaluation.

**Key Points:**
- FFIV traded within a 52-week range of $223.76 to $435.00 and has climbed about 54.5% year-to-date, underscoring notable upside alongside persistent volatility.
- Insiders have sold roughly $28.5 million worth of FFIV stock over the past 12 months, suggesting management liquidity actions or concerns despite recent performance.
- CEO Francois Locoh-Donou sold 3,782 FFIV shares on August 5, contributing to a documented pattern of insider selling around the period.

---

### 2026-08-25 | Next-Generation AI Gateway Slashes Token Costs 60%
*6 articles in cluster*

F5 has unveiled an enhanced AI Gateway that sits within the F5 AI Security Platform, providing a unified control plane to govern how AI models, agents, and tools are accessed across hybrid multicloud environments. The upgrade is designed to cut token costs and tighten governance, security, and observability for enterprise AI workloads. Investor sentiment has been positive, with the agentic-ready gateway contributing to stock momentum and a stronger full-year revenue outlook as demand for AI security and hybrid cloud solutions grows. Analysts caution that sustained upside will depend on continued AI adoption, successful software execution, and the ability to manage margins in a mature infrastructure business. F5 positions the gateway as a foundational layer to reduce fragmentation in AI governance, addressing the economics of AI at scale for organizations managing multiple models and workloads. Overall, the coverage suggests F5 is aiming to be the central control point for enterprise AI traffic across clouds, with potential material benefits if adoption and monetization continue.

**Key Points:**
- The enhanced F5 AI Gateway is touted to cut token costs by up to 60% by centralizing governance and model access within the F5 AI Security Platform.
- Kunal Anand, F5's Chief Product Officer, says, 'Every AI request carries economic, security, and governance implications' and argues for a single intelligent control layer to replace fragmented AI tools.
- Citing the 2026 State of Application Strategy Report, 77% of organizations say inference is their dominant AI activity and they are managing an average of seven AI models, highlighting governance and cost pressures at scale.

---

## FMP Articles (43)

### 2026-11-19 | PENG or FFIV: Which Is the Better Value Stock Right Now?
**Source:** Zacks Investment Research
**URL:** https://www.zacks.com/stock/news/3032668/peng-or-ffiv-which-is-the-better-value-stock-right-now?cid=CS-STOCKNEWSAPI-FT-fundamental_analysis|yseop_template_3-3032668

Investors looking for stocks in the Internet - Software sector might want to consider either Penguin Solutions, Inc. (PENG) or F5 Networks (FFIV). But which of these two stocks offers value investors a better bang for their buck right now?

---

### 2026-11-18 | F5, Inc. (FFIV) Presents at RBC Global Technology, Internet, Media and Telecommunications Conference Transcript
**Source:** Seeking Alpha
**URL:** https://seekingalpha.com/article/4969701-f5-inc-ffiv-presents-at-rbc-global-technology-internet-media-and-telecommunications

F5, Inc. (FFIV) Presents at RBC Global Technology, Internet, Media and Telecommunications Conference Transcript

---

### 2026-11-17 | F5: 3 Key Takeaways for Long-Term Investors
**Source:** The Motley Fool
**URL:** https://www.fool.com/earnings/takeaways/2026/11/17/f5-3-key-takeaways-for-long-term-investors/

F5 expects 8% to 9% revenue growth in fiscal 2027. Fourth-quarter product revenue increased 23% year over year to $510 million.

---

### 2026-11-13 | F5: 4 Years Of EPS Growth And A Critical Role In The AI Era
**Source:** Seeking Alpha
**URL:** https://seekingalpha.com/article/4967909-f5-4-years-of-eps-growth-and-a-critical-role-in-ai-era

F5 gets a 'Buy' rating for my initial coverage. Positives include steady revenue growth, durability over 5 years, positive EPS consensus, 4 years of EPS growth, and third-party integration. FFIV faces a very low D/E and low leverage risk.

---

### 2026-11-11 | F5 to Participate in Upcoming Financial Conference
**Source:** Business Wire
**URL:** https://www.businesswire.com/news/home/20261111169621/en/F5-to-Participate-in-Upcoming-Financial-Conference/

SEATTLE--(BUSINESS WIRE)--F5, Inc. (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced that it will participate in the 2026 RBCCM Global Technology, Internet, Media & Telecommunications Conference. F5's presentation will be webcast live on Wednesday, November 18, 2026, at 10:00 a.m. ET. Interested attendees can access the live webcast via the Events & Presentations tab within the Investor Relations section of f5.com or via this link. An archiv.

---

### 2026-11-07 | F5 (NASDAQ:FFIV) Stock: Insider Chad Michael Whalen Sells 6,950 Shares
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/11/07/f5-nasdaqffiv-stock-insider-chad-michael-whalen-sells-6950-shares-2.html

F5, Inc. (NASDAQ: FFIV - Get Free Report) EVP Chad Whalen sold 6,950 shares of the company's stock in a transaction dated Tuesday, November 3rd. The shares were sold at an average price of $329.56, for a total transaction of $2,290,442.00. Following the transaction, the executive vice president directly owned 25,467 shares of the company's stock,

---

### 2026-11-07 | F5 (NASDAQ:FFIV) Stock: Insider Thomas Dean Fountain Sells 9,387 Shares
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/11/07/f5-nasdaqffiv-stock-insider-thomas-dean-fountain-sells-9387-shares.html

F5, Inc. (NASDAQ: FFIV - Get Free Report) EVP Thomas Fountain sold 9,387 shares of the business's stock in a transaction on Wednesday, November 4th. The shares were sold at an average price of $329.74, for a total value of $3,095,269.38. Following the sale, the executive vice president owned 8,060 shares in the company, valued at

---

### 2026-11-07 | F5 (NASDAQ:FFIV) Stock: Insider Chad Michael Whalen Sells 6,950 Shares
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/11/07/f5-nasdaqffiv-stock-insider-chad-michael-whalen-sells-6950-shares.html

F5, Inc. (NASDAQ: FFIV - Get Free Report) EVP Chad Whalen sold 6,950 shares of the company's stock in a transaction dated Tuesday, November 3rd. The shares were sold at an average price of $329.56, for a total transaction of $2,290,442.00. Following the transaction, the executive vice president directly owned 25,467 shares of the company's stock,

---

### 2026-11-06 | Do Options Traders Know Something About F5 Stock We Don't?
**Source:** Zacks Investment Research
**URL:** https://www.zacks.com/stock/news/3025296/do-options-traders-know-something-about-f5-stock-we-don-t?cid=CS-STOCKNEWSAPI-FT-tale_of_the_tape|options-3025296

Investors need to pay close attention to FFIV stock based on the movements in the options market lately.

---

### 2026-11-05 | F5, Inc. $FFIV Shares Sold by Boston Trust Walden Corp
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/11/05/f5-inc-ffiv-shares-sold-by-boston-trust-walden-corp.html

Boston Trust Walden Corp decreased its position in shares of F5, Inc. (NASDAQ: FFIV) by 3.6% during the third quarter, according to its most recent Form 13F filing with the Securities and Exchange Commission. The fund owned 171,076 shares of the network technology company's stock after selling 6,304 shares during the period. Boston

---

### 2026-11-03 | PENG vs. FFIV: Which Stock Is the Better Value Option?
**Source:** Zacks Investment Research
**URL:** https://www.zacks.com/stock/news/3022005/peng-vs-ffiv-which-stock-is-the-better-value-option?cid=CS-STOCKNEWSAPI-FT-fundamental_analysis|yseop_template_3-3022005

Investors interested in stocks from the Internet - Software sector have probably already heard of Penguin Solutions, Inc. (PENG) and F5 Networks (FFIV). But which of these two stocks presents investors with the better value opportunity right now?

---

### 2026-11-03 | 10,353 F5, Inc. $FFIV Shares Acquired by Bank Julius Baer & Co. Ltd Zurich
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/11/03/10353-f5-inc-ffiv-shares-acquired-by-bank-julius-baer-co-ltd-zurich.html

Bank Julius Baer and Co. Ltd Zurich increased its stake in F5, Inc. (NASDAQ: FFIV) by 68.2% in the third quarter, according to its most recent 13F filing with the Securities and Exchange Commission. The institutional investor owned 25,531 shares of the network technology company's stock after purchasing an additional 10,353 shares during

---

### 2026-10-30 | F5 (FFIV) Loses 18% in 4 Weeks, Here's Why a Trend Reversal May be Around the Corner
**Source:** Zacks Investment Research
**URL:** https://www.zacks.com/stock/news/3019548/f5-ffiv-loses-18-in-4-weeks-here-s-why-a-trend-reversal-may-be-around-the-corner?cid=CS-STOCKNEWSAPI-FT-fundamental_analysis|rsi-3019548

The heavy selling pressure might have exhausted for F5 (FFIV) as it is technically in oversold territory now. In addition to this technical measure, strong agreement among Wall Street analysts in revising earnings estimates higher indicates that the stock is ripe for a trend reversal.

---

### 2026-10-29 | F5 Beat on Revenue and Still Dropped 20%. One Soft Guide Was All It Took for a Stock Up 80% This Year.
**Source:** 24/7 Wall Street
**URL:** https://247wallst.com/investing/2026/10/29/f5-beat-on-revenue-and-still-dropped-20-one-soft-guide-was-all-it-took-for-a-stock-up-80-this-year/

F5 (NASDAQ:FFIV | FFIV Price Prediction) reported fiscal fourth-quarter results after the close on October 27, 2026 and beat on both revenue and earnings. In the next session the stock fell 20%.

---

### 2026-10-29 | First F5, Now Fortinet: Wall Street Has Stopped Paying Security Stocks for Beating Earnings
**Source:** 24/7 Wall Street
**URL:** https://247wallst.com/investing/2026/10/29/first-f5-now-fortinet-wall-street-has-stopped-paying-security-stocks-for-beating-earnings/

Fortinet (NASDAQ:FTNT | FTNT Price Prediction) beat Wall Street on earnings and revenue after the close on October 28, 2026 and raised its full-year revenue outlook. Shares then fell 26% in premarket trading on October 29, 2026.

---

### 2026-10-28 | F5 stock suffers worst day in more than a decade as AI spending shakes investors
**Source:** GeekWire
**URL:** https://www.geekwire.com/2026/f5-stock-suffers-worst-day-in-more-than-a-decade-as-ai-spending-shakes-investors/

F5 shares fell about 20% Wednesday after the company forecast slower revenue growth and lower margins for fiscal 2027, despite beating Wall Street's estimates for its fiscal fourth quarter.

---

### 2026-10-21 | F5 and Telenor Partner to Build the AI Service Plane for Sovereign AI on NVIDIA-powered AI Factory Infrastructure
**Source:** GuruFocus
**URL:** https://www.gurufocus.com/news/9133113/f5-and-telenor-partner-to-build-the-ai-service-plane-for-sovereign-ai-on-nvidiapowered-ai-factory-infrastructure

F5 (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced that Telenor AI Factory has selected F5 BIG-IP Next for Kuber

---

### 2026-10-21 | F5 and Telenor Partner to Build the AI Service Plane for Sovereign AI on NVIDIA-powered AI Factory Infrastructure
**Source:** Business Wire
**URL:** https://www.businesswire.com/news/home/20261020898728/en/F5-and-Telenor-Partner-to-Build-the-AI-Service-Plane-for-Sovereign-AI-on-NVIDIA-powered-AI-Factory-Infrastructure/

SEATTLE--(BUSINESS WIRE)--F5 (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced that Telenor AI Factory has selected F5 BIG-IP Next for Kubernetes as an intelligent AI service plane for its NVIDIA-powered sovereign AI infrastructure. Telenor AI Factory is designed to help Norwegian and European organizations access secure, high-performance AI services while maintaining control over where data is processed, stored, and accessed. Sovereign AI requires.

---

### 2026-10-20 | F5 (FFIV) Expected to Announce Quarterly Earnings on Tuesday
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/10/20/f5-ffiv-expected-to-announce-quarterly-earnings-on-tuesday.html

F5 (NASDAQ: FFIV - Get Free Report) is anticipated to announce its Q4 2026 results after the market closes on Tuesday, October 27th. Analysts expect the company to announce earnings of $4.26 per share and revenue of $884.03 million for the quarter. F5 has set its Q4 2026 guidance at 4.140-4.260 EPS and its FY 2026

---

### 2026-10-14 | VTEX or FFIV: Which Is the Better Value Stock Right Now?
**Source:** Zacks Investment Research
**URL:** https://www.zacks.com/stock/news/3007209/vtex-or-ffiv-which-is-the-better-value-stock-right-now?cid=CS-STOCKNEWSAPI-FT-fundamental_analysis|yseop_template_3-3007209

Investors with an interest in Internet - Software stocks have likely encountered both VTEX (VTEX) and F5 Networks (FFIV). But which of these two companies is the best option for those looking for undervalued stocks?

---

### 2026-10-12 | F5 (NASDAQ:FFIV) Sets New 52-Week High After Analyst Upgrade
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/10/12/f5-nasdaqffiv-sets-new-52-week-high-after-analyst-upgrade.html

F5, Inc. (NASDAQ: FFIV - Get Free Report)'s share price reached a new 52-week high on Monday after Royal Bank Of Canada raised their price target on the stock from $508.00 to $525.00. Royal Bank Of Canada currently has an outperform rating on the stock. F5 traded as high as $484.49 and last traded at $480.9850,

---

### 2026-10-12 | Financial Analysis: Comtech Telecommunications (NASDAQ:CMTL) and F5 (NASDAQ:FFIV)
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/10/12/financial-analysis-comtech-telecommunications-nasdaqcmtl-and-f5-nasdaqffiv.html

F5 (NASDAQ: FFIV - Get Free Report) and Comtech Telecommunications (NASDAQ: CMTL - Get Free Report) are both technology companies, but which is the superior investment? We will compare the two businesses based on the strength of their profitability, valuation, risk, earnings, analyst recommendations, dividends and institutional ownership. Earnings and Valuation This table compares F5 and Comtech

---

### 2026-10-08 | F5 to Report Fourth Quarter and Fiscal Year 2026 Financial Results
**Source:** Business Wire
**URL:** https://www.businesswire.com/news/home/20261006010732/en/F5-to-Report-Fourth-Quarter-and-Fiscal-Year-2026-Financial-Results/

SEATTLE--(BUSINESS WIRE)--F5, Inc. (NASDAQ: FFIV), the global leader in delivering and securing every app and API, announced it will report its fourth quarter and fiscal year 2026 financial results on Tuesday, October 27, 2026, following the market close. F5 will host a live webcast to discuss its results with investors and analysts beginning at 4:30 p.m. ET on October 27, 2026. The live webcast link can be accessed from the events & presentations page of the investor relations portion of f.

---

### 2026-10-07 | F5 Helps Service Providers Modernize Critical Network Services With Greater Infrastructure Efficiency and Control
**Source:** Business Wire
**URL:** https://www.businesswire.com/news/home/20261007351365/en/F5-Helps-Service-Providers-Modernize-Critical-Network-Services-With-Greater-Infrastructure-Efficiency-and-Control/

SEATTLE--(BUSINESS WIRE)--F5 (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced enhanced cloud-native network functions and new observability capabilities that help service providers modernize critical network services as they move from virtualized infrastructure to Kubernetes and cloud-native architectures. Service providers are under pressure to support growing 5G, edge, IT, and emerging AI workloads, boost efficiency, and maintain the performance,.

---

### 2026-10-06 | F5 (NASDAQ:FFIV) Hits New 52-Week High – Should You Buy?
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/10/06/f5-nasdaqffiv-hits-new-52-week-high-should-you-buy.html

Shares of F5, Inc. (NASDAQ: FFIV - Get Free Report) hit a new 52-week high during mid-day trading on Tuesday. The stock traded as high as $471.32 and last traded at $470.1210, with a volume of 16210 shares. The stock had previously closed at $458.53. Analyst Upgrades and Downgrades Several equities analysts have recently weighed in

---

### 2026-10-01 | F5 Named a Leader in the 2026 IDC MarketScape for Worldwide WAAP Platforms for the Second Time
**Source:** GuruFocus
**URL:** https://www.gurufocus.com/news/9105773/f5-named-a-leader-in-the-2026-idc-marketscape-for-worldwide-waap-platforms-for-the-second-time

F5 (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced it has been named a Leader in the IDC MarketScape: Worldwide

---

### 2026-10-01 | F5 Named a Leader in the 2026 IDC MarketScape for Worldwide WAAP Platforms for the Second Time
**Source:** Business Wire
**URL:** https://www.businesswire.com/news/home/20261001956052/en/F5-Named-a-Leader-in-the-2026-IDC-MarketScape-for-Worldwide-WAAP-Platforms-for-the-Second-Time/

SEATTLE--(BUSINESS WIRE)--F5 (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced it has been named a Leader in the IDC MarketScape: Worldwide WAAP Platforms 2026 Vendor Assessment (US54130626, September 2026)¹. This marks the second time F5 has been recognized as a Leader, including the prior assessment in 2024. Organizations today face frontier AI threats and autonomous agentic attacks. Autonomous AI models can scan, discover, and exploit vulnerabili.

---

### 2026-09-26 | Contrasting F5 (NASDAQ:FFIV) & ADTRAN (NASDAQ:ADTN)
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/09/26/contrasting-f5-nasdaqffiv-adtran-nasdaqadtn.html

ADTRAN (NASDAQ: ADTN - Get Free Report) and F5 (NASDAQ: FFIV - Get Free Report) are both technology companies, but which is the better business? We will compare the two businesses based on the strength of their valuation, earnings, profitability, dividends, risk, institutional ownership and analyst recommendations. Institutional and Insider Ownership 80.6% of ADTRAN shares are held

---

### 2026-09-25 | AI Security, Institutional Inflows Push F5 Shares Up 75% YTD
**Source:** FXEmpire
**URL:** https://www.fxempire.com/forecasts/article/ai-security-institutional-inflows-push-f5-shares-up-75-ytd-1631896

F5, Inc. (FFIV) shares rise 1,595% since first outlier inflow signal in 2005.

---

### 2026-09-23 | BILL or FFIV: Which Is the Better Value Stock Right Now?
**Source:** Zacks Investment Research
**URL:** https://www.zacks.com/stock/news/2994598/bill-or-ffiv-which-is-the-better-value-stock-right-now?cid=CS-STOCKNEWSAPI-FT-fundamental_analysis|yseop_template_3-2994598

Investors with an interest in Internet - Software stocks have likely encountered both BILL Holdings (BILL) and F5 Networks (FFIV). But which of these two stocks presents investors with the better value opportunity right now?

---

### 2026-09-18 | Engineers Gate Manager LP Sells 39,179 Shares of F5, Inc. $FFIV
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/09/18/engineers-gate-manager-lp-sells-39179-shares-of-f5-inc-ffiv.html

Engineers Gate Manager LP reduced its stake in F5, Inc. (NASDAQ: FFIV) by 91.9% in the second quarter, according to its most recent filing with the Securities and Exchange Commission. The fund owned 3,444 shares of the network technology company's stock after selling 39,179 shares during the quarter. Engineers Gate Manager LP's holdings

---

### 2026-09-17 | F5 Positioned as Market Shaper in the Gartner Emerging Market Quadrant™ for AI Application Security
**Source:** Business Wire
**URL:** https://www.businesswire.com/news/home/20260917649775/en/F5-Positioned-as-Market-Shaper-in-the-Gartner-Emerging-Market-Quadrant%E2%84%A2-for-AI-Application-Security/

SEATTLE--(BUSINESS WIRE)--F5 (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced it has been positioned by Gartner® in the Market Shapers quadrant of the September 2026 Emerging Market Quadrant for AI Application Security—one of only two vendors to be recognized in that position.[1] According to Gartner, vendors evaluated in the Emerging Market Quadrant for AI Application Security are assessed across two axes: potential for market disruption and poten.

---

### 2026-09-16 | F5 Announces Strategic Partnership With Omnissa to Deliver Secure, High-Performance Digital Workspaces
**Source:** Business Wire
**URL:** https://www.businesswire.com/news/home/20260916134540/en/F5-Announces-Strategic-Partnership-With-Omnissa-to-Deliver-Secure-High-Performance-Digital-Workspaces/

SEATTLE--(BUSINESS WIRE)--F5 (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced a strategic partnership with Omnissa, a leader in digital work platforms, to help enterprises build secure, resilient, and scalable virtual desktop and application delivery architectures. Supported by leading global channel and systems integration partners—such as Presidio—the collaboration combines F5's advanced application delivery and Zero Trust security capabilities w.

---

### 2026-09-16 | F5, Inc. $FFIV Shares Sold by IFP Advisors Inc
**Source:** Defense World
**URL:** https://www.defenseworld.net/2026/09/16/f5-inc-ffiv-shares-sold-by-ifp-advisors-inc.html

IFP Advisors Inc lessened its holdings in shares of F5, Inc. (NASDAQ: FFIV) by 51.1% in the undefined quarter, according to the company in its most recent Form 13F filing with the Securities and Exchange Commission (SEC). The fund owned 1,243 shares of the network technology company's stock after selling 1,301 shares during

---

### 2026-09-15 | F5 Distributed Cloud Bot Defense Adds Device Intelligence and Agentic AI detection to Guard Against Automated Account Abuse
**Source:** Business Wire
**URL:** https://www.businesswire.com/news/home/20260915518492/en/F5-Distributed-Cloud-Bot-Defense-Adds-Device-Intelligence-and-Agentic-AI-detection-to-Guard-Against-Automated-Account-Abuse/

SEATTLE--(BUSINESS WIRE)--F5 (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced enhancements to F5 Distributed Cloud Bot Defense, introducing new device intelligence capabilities and specialized agentic AI protections. Together, these capabilities bring persistent device context and continuous risk decisioning to application security, giving organizations the real-time agent management designed to help welcome trusted digital interaction while helping.

---

### 2026-09-09 | F5, Inc. (FFIV) Presents at Goldman Sachs Communacopia + Technology Conference 2026 Transcript
**Source:** Seeking Alpha
**URL:** https://seekingalpha.com/article/4944584-f5-inc-ffiv-presents-at-goldman-sachs-communacopia-technology-conference-2026-transcript

F5, Inc. (FFIV) Presents at Goldman Sachs Communacopia + Technology Conference 2026 Transcript

---

### 2026-09-09 | F5 Expands AI Security Platform With F5 Workforce AI Security
**Source:** Business Wire
**URL:** https://www.businesswire.com/news/home/20260909374851/en/F5-Expands-AI-Security-Platform-With-F5-Workforce-AI-Security/

SEATTLE--(BUSINESS WIRE)--F5 (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced the upcoming availability of F5 Workforce AI Security, a new agentless offering within the F5 AI Security Platform that gives organizations visibility and policy control across workforce AI activity, including employee AI use and actions taken by agents on users' behalf. Employees' use of AI inside enterprises has moved beyond basic prompts and queries. AI assistants and.

---

### 2026-09-07 | BILL vs. FFIV: Which Stock Is the Better Value Option?
**Source:** Zacks Investment Research
**URL:** https://www.zacks.com/stock/news/2985937/bill-vs-ffiv-which-stock-is-the-better-value-option?cid=CS-STOCKNEWSAPI-FT-fundamental_analysis|yseop_template_3-2985937

Investors interested in Internet - Software stocks are likely familiar with BILL Holdings (BILL) and F5 Networks (FFIV). But which of these two stocks presents investors with the better value opportunity right now?

---

### 2026-09-02 | F5 and MuleSoft, a Salesforce Company, Collaborate to Deliver Inline Security and Governance for Agent Fabric and Agentic AI Applications
**Source:** Business Wire
**URL:** https://www.businesswire.com/news/home/20260902846419/en/F5-and-MuleSoft-a-Salesforce-Company-Collaborate-to-Deliver-Inline-Security-and-Governance-for-Agent-Fabric-and-Agentic-AI-Applications/

SEATTLE--(BUSINESS WIRE)--F5 (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced a technology integration with MuleSoft, a Salesforce company, bringing F5 AI Guardrails—part of the F5 AI Security Platform—directly into Agent Fabric. As enterprises rapidly scale AI agents and large language model (LLM) applications, this native integration provides security and platform engineering teams with centralized policy enforcement, real-time protection against.

---

### 2026-09-01 | F5 to Participate in Upcoming Financial Conference
**Source:** Business Wire
**URL:** https://www.businesswire.com/news/home/20260901371588/en/F5-to-Participate-in-Upcoming-Financial-Conference/

SEATTLE--(BUSINESS WIRE)--F5, Inc. (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced that it will participate in the Goldman Sachs Communacopia + Technology Conference 2026. F5's presentation will be webcast live on Wednesday, September 9, 2026, at 1:10 p.m. ET. Interested attendees can access the live webcast via the Events & Presentations tab within the Investor Relations section of f5.com or via this link. An archived version of the webcast w.

---

### 2026-09-01 | F5 Accelerates Virtual Patching to Manage Emerging Cyber Risks With AI-Powered WAF and Runtime Security
**Source:** GuruFocus
**URL:** https://www.gurufocus.com/news/9062037/f5-accelerates-virtual-patching-to-manage-emerging-cyber-risks-with-aipowered-waf-and-runtime-security

F5 (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced innovations to block frontier AI-driven threats in the data p

---

### 2026-09-01 | F5 Accelerates Virtual Patching to Manage Emerging Cyber Risks With AI-Powered WAF and Runtime Security
**Source:** Business Wire
**URL:** https://www.businesswire.com/news/home/20260901770069/en/F5-Accelerates-Virtual-Patching-to-Manage-Emerging-Cyber-Risks-With-AI-Powered-WAF-and-Runtime-Security/

SEATTLE--(BUSINESS WIRE)--F5 (NASDAQ: FFIV), the global leader in delivering and securing every app and API, today announced innovations to block frontier AI-driven threats in the data path and enable faster virtual patching, giving security leaders time to make intelligent risk-based decisions rather than reactive operational compromises. With new features such as anomaly detection and agentic threat intelligence, F5's AI-powered web application firewall (WAF) is uniquely capable in delivering.

---

### 2026-08-26 | F5 (FFIV) Down 5.1% Since Last Earnings Report: Can It Rebound?
**Source:** Zacks Investment Research
**URL:** https://www.zacks.com/stock/news/2980419/f5-ffiv-down-5-1-since-last-earnings-report-can-it-rebound?cid=CS-STOCKNEWSAPI-FT-realtime_blog-2980419

F5 (FFIV) reported earnings 30 days ago. What's next for the stock?

---
