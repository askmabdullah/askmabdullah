# Lens: VC Money Flow. Where vertical AI agent funding went in 2025-2026, and which customers the funded startups ignore

Research date: 27 October 2026. Scope: only this lens (VC funding as a pain signal, plus the customers left out). Pricing is in USD.

**Method and access limits (read first):**
- I ran about 37 web searches. Then the shared web search budget for this turn ran out (200 calls across all agents).
- Every WebFetch call failed DNS resolution (ENOTFOUND). This hit menlovc.com, news.crunchbase.com, extruct.ai, unite.ai, aiweekly.co and b2bsalestools-com.pages.dev.
- The US Census County Business Patterns API (api.census.gov) was refused by the egress proxy (403).
- As a result, most facts below come from search result summaries of named articles, not from full-page reads. I confirmed each round across two or more outlets where I could.
- I did not retrieve any G2 or Capterra review text.
- I could not verify segment counts (number of US companies), so they appear under Gaps. Where a number is my own estimate, it is labelled "estimate".

---

## 1. Which vertical AI agent categories raised the most money in 2025-2026?

### Takeaway
The money went mainly to agents that replace phone, fax, email and document labour inside regulated or high-volume back offices.
- **Biggest clusters by round size:** healthcare admin and patient access, freight and logistics, legal (personal injury), home services voice, property management, accounting, and insurance underwriting.
- **Smaller seed and Series A clusters:** distributor order entry, accounts receivable (AR), government contracting, construction, and auto dealers.
- Healthcare is the largest single vertical by spend.

### Cited Findings

**Market-level**
- Menlo Ventures (2025) puts vertical (industry-specific) AI at about $3.5B of a roughly $37B enterprise generative AI market. Healthcare is the largest vertical buyer, at about 43% of vertical AI spend (about $1.5B). This comes from secondary summaries; menlovc.com did not resolve for fetch. — [HIT Consultant summary of Menlo report](https://hitconsultant.net/?p=92028); [Menlo healthcare AI report PDF, Oct 2025](https://menlovc.com/wp-content/uploads/2025/10/menlo_ventures_healthcare_ai_report-2025.pdf)
- Menlo's separate healthcare report (21 Oct 2025) cites $1.4B in healthcare AI spend. It also says 22% of healthcare organisations have implemented domain-specific AI tools, 7x the 2024 level. The $1.4B vs $1.5B gap likely reflects different scope. — [Menlo: State of AI in Healthcare 2025](https://menlovc.com/perspective/2025-the-state-of-ai-in-healthcare); [Starkville Daily News / GlobeNewswire release, 21 Oct 2025](https://business.starkvilledailynews.com/starkvilledailynews/article/gnwcq-2025-10-21-healthcare-adopts-ai-22x-faster-than-other-industries-driving-record-14b-in-ai-spending)
- Crunchbase estimated about $10.7B of seed-to-growth funding into AI-powered health tech in 2025 at the time of writing, 24.4% above the $8.6B raised in 2024. Read via search summary; the page was blocked for fetch. — [Crunchbase News](https://news.crunchbase.com/health-wellness-biotech/ai-healthcare-funding-rises-2025/)

**Freight and logistics**
- **HappyRobot, Series B:** $44M, September 2025. Led by Base10, with a16z and YC. Valuation about $500M (per a source familiar). Agents negotiate rates, book appointments and collect payments. Customers include DHL, Ryder and Flexport. Revenue grew 10x since the Series A. — [tech.eu, 3 Sep 2025](https://tech.eu/2025/09/03/happyrobot-raises-44m-series-b-to-scale-ai-agents-for-the-supply-chain/); [Reuters via The Star](https://www.thestar.com.my/tech/tech-news/2025/09/03/happyrobot-raises-44-million-to-expand-ai-agents-for-freight-operators)
- **HappyRobot, Series C:** $150M at a $1.2B post-money valuation, reported 4 Aug 2026.
  - Leads conflict: most outlets name Prysm Capital and Eurazeo. Fortune names other leads.
  - The company reports 150+ enterprise customers, including DHL, Uber and Kuehne + Nagel. Revenue is up more than 5x since the Series B. The pitch is now "enterprise superintelligence", which moves it beyond freight.
  - Sources: [Fortune, 4 Aug 2026](https://fortune.com/2026/08/04/happyrobot-worth-1-2-billion-founder-says-just-getting-started/); [WilmerHale deal note](https://www.wilmerhale.com/en/insights/news/20260805-happyrobot-raises-150-million-series-c-to-build-enterprise-superintelligence)
- **Pallet, Series B:** $27M, 27 May 2025. Led by General Catalyst, with Bain Capital Ventures, Activant and Bessemer. $50M raised in total. It sells an "AI workforce" (CoPallet) to freight brokers, 3PLs, forwarders, carriers and shippers. Vendor claim: admin workflows run about 10x faster at half the cost of traditional staffing. — [Business Wire](https://www.businesswire.com/news/home/20250527164246/en); [Built In](https://builtin.com/articles/pallet-raises-27m-series-b-20250529)

**Healthcare: referral intake and patient access**
- **Tennr, Series C:** $101M, 18 June 2025, at a $605M valuation. Led by IVP, with a16z, Lightspeed, GV and ICONIQ. Less than a year after a $37M Series B. — [Fortune](https://fortune.com/2025/06/18/tennr-health-tech-ai-patient-referral-ivp-a16z-lightspeed-iconiq-series-c/)
- Tennr describes the problem it solves this way: specialists receive referrals by fax, email or e-portal, which "often requir[es] hours of manual review and back-and-forth communication". It also says more than one-third of Americans are referred each year. — [HIT Consultant](https://hitconsultant.net/2025/06/18/tennr-raises-101m-to-solve-healthcares-patient-referral-black-hole/)
- **Assort Health, Series B:** $76M, 30 Sep 2025. Led by Lightspeed. $102M raised in total; the Series A was $22M in April 2025. Product: specialty-specific voice, text and web agents for scheduling, refills, referrals and labs.
  - Conflict: TechCrunch, citing unnamed sources, reported about $50M at a $750M valuation.
  - A Felicis page mentions a $120M Series C in 2026, which I could not verify.
  - Sources: [Fierce Healthcare](https://www.fiercehealthcare.com/ai-and-machine-learning/assort-health-brings-total-funding-102m-four-months); [TechCrunch](https://techcrunch.com/?p=3040176); [Felicis](https://www.felicis.com/portfolio/assort-health)

**Legal (personal injury)**
- **EvenUp, Series E:** $150M, 7 Oct 2025, at a valuation above $2B. Led by Bessemer, with REV (the RELX venture arm), B Capital, SignalFire, Bain Capital and Lightspeed. $385M raised in total. Vendor claim: 2,000+ law firms, including 20% of the Top 100 US PI firms. — [Business Wire](https://www.businesswire.com/news/home/20251007138957/en/EvenUp-Raises-150M-Series-E-at-2B-Valuation-to-Redefine-Personal-Injury-Law-and-Level-the-Playing-Field-for-Injury-Victims); [LawNext](https://lawnext.com/2025/10/evenup-ai-platform-for-personal-injury-lawyers-raises-150m-at-2b-valuation.html)

**Home services voice**
- **Avoca:** more than $125M raised across seed, Series A and Series B, at a $1B valuation, announced 27 Apr 2026.
  - Series B led by Meritech and General Catalyst. Series A led by Kleiner Perkins. YC seed.
  - Serves 800+ customers in HVAC, plumbing, roofing and electrical. Partners include ServiceTitan and Nexstar.
  - Plans to expand into moving, automotive and property management.
  - Sources: [Pulse 2.0](https://pulse2.com/avoca-125-million-raised-at-1-billion-valuation-to-power-services-economy-with-ai/); [Let's Data Science](https://letsdatascience.com/news/avoca-raises-125m-reaches-1b-valuation-1f84b3d8); [Munich Startup feed](https://insights.munich-startup.de/news/feed/avoca-raises-125m-at-1b-valuation-to-automate-america-s-services-economy-with-ai)
- **Netic, Series B:** $23M, 13 Nov 2025, at a $450M valuation. Led by Founders Fund; the Series A ($20M) was in June 2025. Product: call intake, triage and booking for home services. Example: a roofer received 600+ calls in 90 minutes after a St. Louis tornado. — [Bloomberg](https://www.bloomberg.com/news/articles/2025-11-13/founders-fund-backs-startup-bringing-ai-to-plumbers-and-roofers); [Insurance Journal](https://www.insurancejournal.com/news/national/2025/11/13/847406.htm)

**Property management**
- **EliseAI, Series E:** $250M, 20 Aug 2025, at about a $2.2B valuation. Led by a16z, with Bessemer, Sapphire and Navitas. Product: leasing, maintenance and resident communications; it also serves healthcare. — [SiliconANGLE](https://siliconangle.com/2025/08/20/property-management-startup-eliseai-nabs-250m-2-2b-valuation/); [Business Wire](https://www.businesswire.com/news/home/20250820023566/en)

**Accounting**
- **Basis, Series B:** $100M, February 2026, at a $1.15B valuation. Led by Accel, with GV. Sells agents to accounting firms. Says it works with about 30% of the Top 25 accounting firms. The Series A was $34M in December 2024, led by Khosla. — [Fintech Futures](https://www.fintechfutures.com/venture-capital-funding/basis-raises-100m-series-b); [Built In, 26 Feb 2026](https://builtin.com/articles/basis-raises-100m-series-b-20260226)

**Accounts receivable (AR)**
- **Stuut, Series A:** $29.5M, November 2025, led by a16z. Covers collections, cash application, deductions and disputes. — [Crowdfund Insider](https://www.crowdfundinsider.com/2025/11/255763-stuut-technologies-raises-29-5-million-series-a/)
- **Fazeshift, Series A:** $17M, May 2026, led by F-Prime. $22M raised in total. Vendor claim: automates more than 90% of manual AR tasks. — [The Paypers](https://thepaypers.com/fintech/news/fazeshift-obtains-usd-17-mln-in-series-a-round-for-ai-accounts-receivable); [Crunchbase News](https://news.crunchbase.com/fintech/fazeshift-accounts-receivable-ai-finance-ops-startup-funding/)
- **Monk, Series A:** $25M, April 2026. Co-led by Footwork and Acrew. — [FinTech Global](https://fintech.global/2026/04/22/monk-raises-25m-series-a-to-automate-receivables/)

**Insurance underwriting**
- **Federato, Series D:** $100M, 18 Nov 2025. Led by Growth Equity at Goldman Sachs Alternatives. More than $180M raised in total; revenue more than tripled. Product: submission triage and risk ranking for underwriters. — [FinTech Global](https://fintech.global/2025/11/18/federato-secures-100m-to-expand-ai-native-insurance-platform); [Reinsurance News](https://www.reinsurancene.ws/federato-raises-100m-series-d-to-accelerate-global-expansion/)
- **Sixfold, Series B:** $30M, 29 Jan 2026. Led by Brewer Lane, with Guidewire as a strategic investor. More than $50M raised in total. — [Insurance Edge](https://insurance-edge.net/2026/01/29/deals-sixfold-raises-30m-in-series-b-round/); [Coverager](https://coverager.com/sixfold-raises-30m-series-b/)
- **Pibit.ai, Series A:** $7M, November 2025. Led by Stellaris, with YC. — [Pulse 2.0](https://pulse2.com/pibit-ai-7-million-series-a/)

**Construction**
- **Trunk Tools, Series B:** $40M, 24 Jul 2025. Led by Insight Partners. $70M raised in total. Product: agents for RFIs, submittals, specs and schedules. The funds are intended partly to reach mid-market and smaller contractors. — [insideHPC](https://insidehpc.com/2025/07/trunk-tools-closes-40m-series-b-for-construction-ai/); [Commercial Observer](https://commercialobserver.com/2025/07/trunk-tools-contech-series-b/)

**Auto dealers**
- **Toma, Series A:** $17M, June 2025. Led by a16z (Seedtable lists a different lead). Deployed in 100+ dealerships; handles service scheduling, parts and sales calls. Founder claim: 45% of dealership calls go unanswered. — [a16z announcement](https://a16z.com/announcement/investing-in-toma/); [AIM Research](https://aimresearch.co/ai-startups/toma-answers-the-call-of-auto-dealerships-with-17m-series-a)

**Government contracting**
- **GovDash, Series B:** $30M, 15 Jan 2026. Led by Mucker Capital and BCI, with Northzone and YC. Nearly 200 customers. Vendor claim: customers won more than $5B in contracts in 2025. — [GovDash press release](https://www.govdash.com/blog/press-govdash-raises-30m-series-b-to-help-companies-win-and-manage-government-contracts-with-ai); [SiliconANGLE](https://siliconangle.com/2026/01/15/govdash-secures-30m-expand-ai-driven-government-contracting-software/)

**Distributor order entry (mostly seed stage)**
- **Pepper, Series C:** $50M, April 2026, led by Lead Edge. Its order agent ingests PDFs and voice memos into a distributor's ERP (foodservice). — [Pulse.bot](https://www.pulse.bot/ai/deals/pepper-raises-50m-series-c-led-by-lead-edge-capital-to-expand-ai-powered-foodservice-platform-2208d6ae-0811-4329-a718-c9b24baa3cbc)
- **Anchr:** $5.8M (reported as seed or pre-seed), about March 2026. Ingests orders from email, text and voicemail for food distributors. — [StartupHub](https://www.startuphub.ai/news/anchr-secures-5-8m-seed-round); [Infor Capital](https://inforcapital.com/news/anchr-raises-58m-to-automate-americas-food-supply-chain-with-ai)
- **Comena (YC S25):** reads purchase orders from emails and PDFs into ERP for distributors and manufacturers. Amount undisclosed. — [Seedtable](https://seedtable.com/companies/comena/funding-rounds/seed-2025-07)
- **Burnt (YC S25):** reported $3.8M seed; order and invoice processing for food distributors. Aggregator source, unverified. — [funded-pulse](https://funded-pulse.pages.dev/companies/burnt.html)

### Inferences
- **Ranking by disclosed 2025-2026 dollars (approximate, from rounds verified above):**
  1. Healthcare admin and patient access: Tennr $101M + Assort $76M, plus others not verified this pass.
  2. Property management: EliseAI $250M.
  3. Freight: HappyRobot $194M (Series B + C) + Pallet $27M.
  4. Legal PI: EvenUp $150M.
  5. Home services: Avoca $125M+ cumulative + Netic $43M.
  6. Accounting: Basis $100M.
  7. Insurance underwriting: Federato $100M + Sixfold $30M + Pibit $7M.
  8. AR: Stuut, Fazeshift and Monk, about $72M combined.
  9. Construction: Trunk Tools $40M.
  10. Government contracting: GovDash $30M.
  11. Auto dealers: Toma $17M.
- Distributor order entry is the most fragmented cluster: many seed rounds, one $50M round.
- The common thread is replacing phone, fax, email and PDF handling done by coordinators. Few of these agents do core professional judgement.

### Gaps
- I could not verify these rounds this pass (search budget ran out): Infinitus, AKASA, SmarterDx, Hello Patient, Thoughtful, Commure, Kalepa, Strala, Avallon, Rillet, Campfire, Numeric, DualEntry, Maximor, Stacks, Puzzle, Harvey, Eve, Supio, Clio acquisitions, Sameday, Viva, Impel, Buildpass, Endeavor, Conexiom, Lace, Aurora, Augment, Vooma, FleetWorks, Fleetline.
- Arini (dental): the only verified round is a $500K seed in February 2024 ([Signalbase](https://www.trysignalbase.com/news/funding/arini-raises-500k-seed-funding)). A Caplight listing of "early funding" in May 2026 has no amount and is unverified ([Caplight](https://www.caplight.com/company/arini-ai)).
- I found no Crunchbase or PitchBook ranking of vertical AI categories that I could read in full. Search snippets mentioned "PitchBook: vertical AI applications led AI deal volume with 663 transactions in Q3 2025" and "Crunchbase: legal tech record $4.6B", but I did not capture source URLs for them, so they are excluded.
- I did not research restaurants, recruiting and staffing agents, or tax and compliance agents (search budget ran out).

---

## 2. Who each cluster sells to, what it does NOT serve, and what customers complain about

### Takeaway
Funded leaders sell top-down to enterprise or upper mid-market buyers, on quote-only pricing and integration-heavy deployments:
- HappyRobot: the largest freight brokers.
- Basis: Top 25 accounting firms.
- Avoca: contractors at $3M+ revenue on ServiceTitan.
- Federato and Sixfold: carriers.

Public evidence of who they explicitly exclude is thin. The exclusion shows up through price floors, integration prerequisites and the logos they publicise.

### Cited Findings
- **HappyRobot:** reports 150+ enterprise customers. A search summary of coverage says eight of the 10 largest US freight brokers run its agents in production. I did not open that page; source cited as Sacra. — [Sacra](https://sacra.com/c/happyrobot/)
  - Its 2024 a16z backer said "even small to midsize freight brokers can make and receive hundreds, if not thousands, of calls per day". That describes the need, not a small-broker product. — [VKTR, 2024](https://www.vktr.com/the-wire/happyrobot-raises-156-million-series-a-funding-led-by-a16z-to-transform-logistics-with-agentic-ai)
  - No public price list exists. — [Forkast](https://forkast.news/happyrobot-wants-1-2-billion-to-run-your-freight-by-voice/)
- **Avoca:** pricing is quote-based and per minute. These are third-party or competitor estimates:
  - Cost: $1,000-$3,000 per month, or $1,500-$5,000+ for mid-to-large operators.
  - Best fit: "$3M+ home services operations on ServiceTitan", or alternatively "20+ CSRs and $10M+ revenue".
  - Sources: [Macha, competitor content](https://www.getmacha.com/blog/avoca-ai-pricing-explained); [FieldCamp review](https://fieldcamp.ai/reviews/avoca-ai/); [ContractorToolStack](https://contractortoolstack.com/software/avoca-ai/)
- **Tennr:** pricing is listed as enterprise-only, with workflow, module and implementation terms on request (third-party profile). — [AI for Medical](https://aiformedical.pages.dev/products/tennr/)
  - Users include practices, home health agencies, DME suppliers and care coordination teams. — [Capterra](https://www.capterra.ca/software/1105625/Tennr)
  - Vendor benchmark (vendor claim): independent providers lose about 10% of revenue a year to preventable paperwork mistakes. — [Tennr benchmark via finanzen.net, Oct 2025](https://www.finanzen.net/nachricht/aktien/independent-healthcare-providers-already-operate-on-thin-margins-where-every-dollar-counts-tennr-s-benchmark-report-reveals-they-lose-10-of-their-revenue-every-year-to-preventable-paperwork-mistakes-14933837)
- **EvenUp:** moved to per-case pricing in May 2025 and publishes no dollar figures. Third-party estimates (unverified):
  - $200-$800 per case.
  - About $30K-$120K a year depending on volume.
  - EvenUp says it suits sole practitioners writing as few as six demand letters a year.
  - Sources: [AI Lawyer Tools Compared](https://ailawyertoolscompared-com.pages.dev/tool/evenup/); [B2B Sales Tools PI guide](https://b2bsalestools-com.pages.dev/guides/best-legal-ai-personal-injury-firms/)
- **Basis:** its reference customers are big firms (about 30% of the Top 25). — [Fintech Futures](https://www.fintechfutures.com/venture-capital-funding/basis-raises-100m-series-b)
- **Sixfold:** Guidewire is a strategic investor. — [Coverager](https://coverager.com/sixfold-raises-30m-series-b/)
- **Federato:** Goldman's diligence cited ROI compared with legacy core systems, which signals a carrier-level buyer. — [Intelligent Insurer](https://www.intelligentinsurer.com/ai-powers-federato-to-dollar100m-in-goldman-sachs-led-fundraise)
- **Trunk Tools:** said it will use the Series B to reach "mid-market and smaller contractors". This is explicit down-market intent. — [insideHPC](https://insidehpc.com/2025/07/trunk-tools-closes-40m-series-b-for-construction-ai/)
- **GovDash:** nearly 200 customers. A small base, likely contractors who already bid federal work. — [GovDash](https://www.govdash.com/blog/press-govdash-raises-30m-series-b-to-help-companies-win-and-manage-government-contracts-with-ai)
- **Avoca:** expanding horizontally into moving, automotive and property management, rather than down to smaller contractors. — [Munich Startup feed](https://insights.munich-startup.de/news/feed/avoca-raises-125m-at-1b-valuation-to-automate-america-s-services-economy-with-ai)

### Inferences
- **Price floors (estimate):** Avoca's estimated $1,000-$5,000 per month equals $12K-$60K a year. EvenUp's estimated $30K-$120K a year is above what a 1-3 attorney PI firm or a sub-$2M contractor will commit to without proof.
- **Integration prerequisites act as exclusions:** ServiceTitan for Avoca, a TMS for freight agents, an EHR for Tennr, a core policy system for Sixfold and Federato. Customers on spreadsheets, old on-prem ERPs, fax and paper fall outside.
- **Geography:** every verified leader except HappyRobot (Spain/Mexico roots, global customers) sells US-specific workflows: US PI demand letters, US payer referrals and prior auth, ServiceTitan. UK and Australian equivalents are not served by these funded players.

### Gaps
- I found no vendor statement of a minimum contract size or excluded segment for any company.
- I did not retrieve G2 or Capterra complaint text about implementation burden, price or accuracy (search budget ran out; review sites were not fetched). This is the biggest evidence gap in this section.
- Job posts revealing target customer size were not checked.

---

## 3. What investor reports say about vertical AI, and what is still unsolved

### Takeaway
Investors frame vertical AI as "services as software". The labour and outsourcing budget is the target, and is described as far larger than software budgets. YC's 2026 Requests for Startups explicitly ask for AI-native services firms that sell finished work in accounting, tax, audit, compliance, insurance brokerage and healthcare admin. This is the same model a human-in-the-loop services firm would run.

### Cited Findings
- **YC 2026 RFS** (secondary write-ups):
  - Highlights insurance brokerage, accounting, tax, audit, compliance and healthcare administration as areas where AI could replace outsourced services.
  - Describes "AI-native agencies that sell finished work rather than tools".
  - Asks for rebuilt ERP and supply chain software.
  - Sources: [Let's Data Science](https://www.letsdatascience.com/news/yc-requests-ai-native-startups-across-industries-1c422935); [VC Cafe, Summer 2026](https://www.vccafe.com/requests-for-startups-summer-2026-edition/); [Epsilla, Mar 2026](https://epsilla.com/blogs/2026-03-08-yc-rfs-2026-agentic-economy)
- **a16z framing** (secondary): services spend is about 10x the software market, and agents can address it. Businesses pay for "a system that takes responsibility for business outcomes", not a smarter chat window. — [Echai Ventures summary](https://echai.ventures/how-founders-use-ai/ai-agents/is-there-a-real-startup-opportunity-in-building-vertical-ai-agents); [KuCoin news summary of a16z](https://www.kucoin.com/news/flash/a16z-ai-application-opportunities-lie-beyond-general-models)
- **Bessemer:** its State of AI 2025 report (September 2025) argues vertical AI companies may have an early edge over horizontal ones (podcast summary). — [Metrics Brothers podcast](https://pocketcasts.com/podcast/the-metrics-brothers-fka-saas-talk/4434b080-f1a2-013b-f517-0acc26574db2/bessemers-state-of-ai-2025-report/5c7e1c9d-a90b-4ae0-a415-d6f083baf433)
  - Bessemer 2024 (labelled 2024) defined vertical AI as targeting "high-cost, repetitive language-based tasks". — [SiliconANGLE, Jun 2024](https://siliconangle.com/?p=661323)
- **Menlo:** healthcare is the largest vertical buyer, at about 43% of vertical AI spend. — [HIT Consultant summary](https://hitconsultant.net/?p=92028)

### Inferences
- What investors leave unsolved is distribution to fragmented, low-ACV customers. VC-backed software needs $20K-$100K+ ACVs to justify sales cost (estimate based on the price floors above).
- YC asking for "AI-native services" shows investors think the services wrapper is needed for some buyers, and is a credible model.

### Gaps
- I could not read the primary text of the Menlo 2025 enterprise report, the Bessemer State of AI 2025, the a16z "services as software" essay, Sequoia, Greylock, NFX, Lightspeed or General Catalyst. menlovc.com failed DNS; the others were not reachable within the search budget.
- I have no direct investor quote on "what remains unsolved" beyond the secondary summaries above.

---

## 4. Which YC batches in 2025-2026 were heavy in vertical agents, and in which industries?

### Takeaway
Spring and Summer 2025 (X25/S25) were the peak of AI agent startups at YC, about half of each batch. W26 shifted toward deep tech, with agents down to about 19%. The vertical agents that remain are in dental front desk, law firm operations, supply chain, distributor order entry and healthcare voice.

### Cited Findings
- **YC W26:** 199 companies. 37 are AI agents (19%), down from about half in Spring and Summer 2025. Examples include an AI dental receptionist, an AI law firm operator and an AI supply chain manager. Extruct was blocked for fetch, so this is a search summary. — [Extruct W26 breakdown](https://www.extruct.ai/research/ycw26)
- **W24-W26 cohort analysis:** autonomous agents cluster in fintech, healthcare and sales/marketing. Voice AI concentrates in healthcare and customer support. — [Towards AI](https://pub.towardsai.net/i-analyzed-every-yc-company-from-winter-2024-to-winter-2026-heres-what-s-actually-changing-2e9d9d40d0da)
- **S25 examples:** Comena (distributor PO intake) and Burnt (food distributor orders). — [Seedtable](https://seedtable.com/companies/comena/funding-rounds/seed-2025-07); [funded-pulse](https://funded-pulse.pages.dev/companies/burnt.html)
- **YC alumni among the funded leaders:** HappyRobot, Avoca, Toma, Arini, GovDash and Pibit. — sources cited in section 1.

### Inferences
- YC is still seeding seat-replacement agents in the same verticals the large rounds validated: dental, legal operations, supply chain, distribution. Expect more seed competitors chasing small customers in these verticals over 2026-2027. This raises down-market risk for a services firm in voice reception and order entry.

### Gaps
- I found no per-industry counts for W25, S25, F25 or S26 from the official YC directory. The secondary analyses differ in method.

---

## 5. Where the gap is for a services-led, human-in-the-loop provider (problem records)

### Takeaway
The best openings are where funded startups prove the pain but price, integration or geography excludes a large tail. The strongest examples:
- Small freight brokers and agents.
- Independent specialty practices and DME suppliers doing fax referral intake.
- Small distributors on legacy ERPs doing PO entry.
- Non-US personal injury firms.

Plain voice reception (home services, dental, auto) is weaker. It is likely already served under $100 a month, though I did not verify this pass. Insurance and AR openings carry Shariah questions.

### Cited Findings
- The evidence used in the records below is cited in sections 1-2. New items:
  - Netic's tornado example (600+ calls in 90 minutes) shows peak-load pain for contractors. — [Insurance Journal](https://www.insurancejournal.com/news/national/2025/11/13/847406.htm)
  - Toma: founder claim that 45% of dealership calls go unanswered. — [AIM Research](https://aimresearch.co/ai-startups/toma-answers-the-call-of-auto-dealerships-with-17m-series-a)

### Inferences (problem records)

How to read the records:
- Six tests: (a) happens weekly; (b) costs measurable money; (c) someone already pays for it; (d) the person who feels it approves spend; (e) AI plus a human checker can do most of it in 2026; (f) not solved under $100 a month or free from a platform.
- Attractiveness is blind: pain x willingness to pay x low competition x staying power, on a scale of 1-10.
- Unless cited, hours and dollar figures are estimates with the math shown.

#### P1. Carrier-side phone and email operations for small freight brokers and freight agents
- **Problem:** Small brokers lose loads and margin because they cannot answer carrier calls, do check calls and chase PODs fast enough.
- **Industry:** freight brokerage / 3PL (US first; UK and Australian forwarders second).
- **Company size:**
  - Hurts most at brokers with 1-25 staff and at independent freight agents.
  - Funded startups target the top 10 US brokers and enterprises: DHL, Uber, Kuehne + Nagel ([Fortune](https://fortune.com/2026/08/04/happyrobot-worth-1-2-billion-founder-says-just-getting-started/); [Sacra](https://sacra.com/c/happyrobot/)).
- **Task:** answer carrier calls on posted loads; quote within a rate band; vet the carrier; send the rate confirmation; run check calls ("where is the truck"); book dock appointments; chase PODs and invoices; update the TMS.
- **Who feels it / who approves:** carrier sales rep and ops manager / broker owner.
- **Frequency:** daily. "Even small to midsize freight brokers can make and receive hundreds, if not thousands, of calls per day" (a16z, 2024, [VKTR](https://www.vktr.com/the-wire/happyrobot-raises-156-million-series-a-funding-led-by-a16z-to-transform-logistics-with-agentic-ai)).
- **Dollar cost:** vendor claim: Pallet does this work at half the cost of staffing ([Business Wire](https://www.businesswire.com/news/home/20250527164246/en)). Estimate: if one ops hire costs about $4,000 a month fully loaded (assumption, unverified), automating half of check-call and booking time frees about $2,000 a month per seat.
- **Handled today:** in-house reps; offshore virtual assistants; quote-only enterprise agents.
- **Who sells a fix:** HappyRobot, Pallet (verified); Vooma, FleetWorks, Augment (not verified this pass). Enterprise pricing. Crowded at the top, thin at the bottom (inference).
- **24-month trend:** grows. Cheaper voice AI makes outcomes cheaper to deliver, but HappyRobot is moving horizontal ("enterprise superintelligence"), not down.
- **Down-market likelihood (24 months):** medium. Seed-stage freight agents and load-board or TMS bundling are the main threat.
- **How to reach buyers:** TIA (Transportation Intermediaries Association), FreightCaviar podcast and community ([FreightCaviar](https://freightcaviar.com/podcast/e205-how-happyrobot-is-changing-freight-brokerages-with-ai-Yvlv2MXh6cg)), DAT/Truckstop ecosystems, freight agent host programmes.
- **US count in ignored segment:** not verified (Census API blocked; see Gaps).
- **Strongest argument against:** thin margins in a soft freight market. Fraud and double-brokering liability. Load boards and TMS vendors may bundle "good enough" AI.
- **Tests:**
  - a: pass (daily).
  - b: pass (lost loads, labour).
  - c: pass (staff and virtual assistants).
  - d: pass (owner).
  - e: pass (voice AI plus human approval of rates).
  - f: pass, likely (no sub-$100 tool books loads and writes to the TMS; unverified).
- **Attractiveness:** 7.

#### P2. Fax and portal referral intake, eligibility checks and missing-document chasing for independent specialty practices, DME and home health
- **Problem:** Referrals arrive by fax and email, incomplete. Staff spend hours keying them in and chasing missing documents, and patients leak away.
- **Industry:** outpatient healthcare admin (US only; the payer workflow is US-specific).
- **Company size:**
  - Hurts most at independent groups with 1-15 providers, small DME suppliers and home health agencies.
  - Funded startups use enterprise pricing ([AI for Medical](https://aiformedical.pages.dev/products/tennr/)).
- **Task:** read the faxed referral; extract demographics and insurance; run eligibility; check required documents (orders, notes); request what is missing from the referring office; enter it in the EHR; schedule.
- **Who feels it / who approves:** intake coordinator / practice administrator or owner.
- **Frequency and hours:** daily. "Hours of manual review and back-and-forth" ([HIT Consultant](https://hitconsultant.net/2025/06/18/tennr-raises-101m-to-solve-healthcares-patient-referral-black-hole/)).
- **Dollar cost:** vendor claim of about 10% of revenue lost to preventable paperwork errors ([Tennr benchmark](https://www.finanzen.net/nachricht/aktien/independent-healthcare-providers-already-operate-on-thin-margins-where-every-dollar-counts-tennr-s-benchmark-report-reveals-they-lose-10-of-their-revenue-every-year-to-preventable-paperwork-mistakes-14933837)).
- **Handled today:** front-desk staff; offshore medical virtual assistants; RCM vendors.
- **Who sells a fix:** Tennr ($101M), Assort ($76M), and others not verified. Enterprise and quote-only.
- **24-month trend:** grows. Document AI improves; the human is still needed for payer rules and accountability.
- **Down-market likelihood:** medium-high. Tennr already serves DME and home health; EHR vendors may bundle intake AI.
- **How to reach buyers:** state DME associations, AAHomecare, specialty societies, EHR marketplaces.
- **US count:** not verified.
- **Strongest argument against:** HIPAA and BAA liability; EHR integration fragmentation; Tennr moving down-market.
- **Tests:** a pass; b pass; c pass; d pass; e pass; f pass (no free or sub-$100 tool does this).
- **Attractiveness:** 8.

#### P3. Email, PDF and phone purchase-order entry into legacy ERPs for small and mid-size distributors
- **Problem:** Customer-service reps re-key orders from emails, PDFs and voicemails into old ERPs, which causes errors, slow confirmations and lost reorders.
- **Industry:** wholesale distribution and light manufacturing (US, UK, Australia).
- **Company size:**
  - Hurts most at distributors with $5M-$50M revenue (estimate band) on on-prem or legacy ERPs, in niche sub-verticals such as industrial MRO, electrical and building materials.
  - Funded startups cluster in foodservice (Pepper, Anchr, Burnt).
- **Task:** parse the PO; map customer part numbers to SKUs; check price and stock; key it into the ERP; send confirmation; flag exceptions.
- **Who feels it / who approves:** inside sales or customer-service rep / ops director, owner or CFO.
- **Frequency:** daily (inference from the product descriptions of [Pepper](https://www.pulse.bot/ai/deals/pepper-raises-50m-series-c-led-by-lead-edge-capital-to-expand-ai-powered-foodservice-platform-2208d6ae-0811-4329-a718-c9b24baa3cbc) and [Anchr](https://inforcapital.com/news/anchr-raises-58m-to-automate-americas-food-supply-chain-with-ai)).
- **Dollar cost:** not verified. Estimate: 1-3 order-entry staff at about $4,000 a month (assumption) = $4K-$12K a month addressable.
- **Handled today:** customer-service reps; offshore data entry; EDI for large customers only.
- **Who sells a fix:** Pepper, Anchr, Burnt, Comena (verified); Conexiom, Endeavor, Lace (not verified). Crowded at seed stage in food; thin outside food (inference).
- **24-month trend:** grows. Extraction is improving, and legacy ERP write-back stays messy, which favours a human or RPA hybrid.
- **Down-market likelihood:** medium. Many YC seeds are attacking this; ERP vendors may add order capture.
- **How to reach buyers:** NAW and sub-vertical distributor associations (e.g., NAED, ISA, NBMDA; not verified), ERP reseller and VAR partners, MDM newsletter ([MDM](https://www.mdm.com/category/technology/technology-provider-news/page/2/)).
- **US count:** not verified.
- **Strongest argument against:** a crowded seed field; ERP integration cost per client; buyers may hold out for cheap SaaS.
- **Tests:** a pass; b pass; c pass; d pass; e pass; f pass.
- **Attractiveness:** 7.

#### P4. Medical-record chronologies and demand or claim packs for small PI firms and for UK and Australian injury firms
- **Problem:** Paralegals spend hours turning medical records into chronologies and demand packages, which delays settlements.
- **Industry:** legal (plaintiff personal injury).
- **Company size:**
  - Hurts most at 1-5 attorney US firms, and at UK and Australian injury firms (not served by US-centric tools; inference).
  - EvenUp claims 2,000+ firms and 20% of the Top 100 ([Business Wire](https://www.businesswire.com/news/home/20251007138957/en/EvenUp-Raises-150M-Series-E-at-2B-Valuation-to-Redefine-Personal-Injury-Law-and-Level-the-Playing-Field-for-Injury-Victims)).
- **Task:** collect and sort records and bills; build a chronology; total the specials; draft the demand; attorney reviews.
- **Who feels it / who approves:** paralegal and case manager / managing partner.
- **Frequency:** weekly or more at active firms (inference).
- **Dollar cost:** third-party estimate for EvenUp of $200-$800 per case, so the market already pays per case ([AI Lawyer Tools Compared](https://ailawyertoolscompared-com.pages.dev/tool/evenup/)).
- **Handled today:** paralegals; outsourced medical-chronology vendors.
- **Who sells a fix:** EvenUp (verified); Eve and Supio (not verified). Crowded in the US.
- **24-month trend:** shrinks in the US as EvenUp-class tools get cheaper. Steady outside the US.
- **Down-market likelihood:** high in the US (EvenUp already courts solo practitioners); low-medium in the UK and Australia.
- **How to reach buyers:** state trial-lawyer associations; APIL (UK) and Australian Lawyers Alliance (not verified); PI practice-management partners.
- **US count:** not verified.
- **Halal:** contingency fees are not interest. However, litigation funding attached to cases is often interest-bearing, so flag it.
- **Strongest argument against:** EvenUp already serves small US firms. UK and Australian legal regimes differ, so the product has to be rebuilt per jurisdiction.
- **Tests:** a pass; b pass; c pass; d pass; e pass; f pass.
- **Attractiveness:** 6 (US 4, UK/Australia 7).

#### P5. Bid discovery and proposal drafting for small government contractors (state and local plus small federal)
- **Problem:** Small contractors miss bids or submit weak proposals because no one has time to scan portals and write responses.
- **Industry:** government contracting (US; UK and Australian public tenders).
- **Company size:**
  - Hurts most at contractors with under 50 staff bidding state and local or small-business set-asides.
  - GovDash has nearly 200 customers ([GovDash](https://www.govdash.com/blog/press-govdash-raises-30m-series-b-to-help-companies-win-and-manage-government-contracts-with-ai)).
- **Task:** monitor portals; qualify bids; pull requirements into a compliance matrix; draft from past proposals; human review; submit.
- **Who feels it / who approves:** owner or business-development lead / owner.
- **Frequency:** weekly for active bidders (inference).
- **Dollar cost:** vendor claim that GovDash customers won more than $5B in 2025. Freelance proposal writers are the incumbent spend (pricing not verified).
- **Handled today:** owner's evenings; proposal consultants; bid-alert subscriptions.
- **Who sells a fix:** GovDash (verified); others not verified this pass.
- **24-month trend:** grows. Drafting quality is improving; compliance checks still need a human.
- **Down-market likelihood:** medium.
- **How to reach buyers:** APEX Accelerators (formerly PTACs; not verified), SBA programmes, state procurement fairs.
- **US count:** not verified.
- **Strongest argument against:** low win rates make outcome pricing risky; established consultants; portal fragmentation.
- **Tests:** a pass; b pass; c pass; d pass; e pass; f pass, likely.
- **Attractiveness:** 6.

#### P6. Commercial submission intake and ACORD data entry for small MGAs and independent agencies (HALAL FLAG)
- **Problem:** Agency and MGA staff re-key broker submissions (ACORD forms, loss runs, SOVs) before underwriting, which slows quotes and loses business.
- **Industry:** P&C insurance distribution.
- **Company size:**
  - Hurts most at small MGAs and wholesalers and at independent agencies.
  - Funded startups sell to carriers and large MGAs (inference from Goldman's diligence and the Guidewire link: [Intelligent Insurer](https://www.intelligentinsurer.com/ai-powers-federato-to-dollar100m-in-goldman-sachs-led-fundraise); [Coverager](https://coverager.com/sixfold-raises-30m-series-b/)).
- **Task:** extract submission data; populate the rater or agency management system; flag missing information; request it from the retail broker.
- **Who feels it / who approves:** account manager or underwriting assistant / agency principal.
- **Frequency:** daily (inference).
- **Dollar cost:** not verified.
- **Who sells a fix:** Federato, Sixfold, Pibit (verified). Agency management system vendors are likely to bundle (unverified).
- **Down-market likelihood:** medium.
- **How to reach buyers:** Big I (IIABA), state agent associations, AAMGA (not verified).
- **Shariah question:** conventional insurance. No ruling given.
- **Strongest argument against:** the Shariah concern; agency management system bundling; E&O liability.
- **Tests:** a pass; b pass; c pass; d pass; e pass; f pass, likely.
- **Attractiveness:** 6.

#### P7. Month-end close and bookkeeping cleanup for small CPA and bookkeeping firms and their messy SMB clients
- **Problem:** Small firms cannot hire enough staff to clean miscategorised books and close monthly on time.
- **Industry:** accounting services (US, UK, Australia; Xero-heavy outside the US).
- **Company size:**
  - Hurts most at firms with under 20 staff.
  - Basis targets the Top 25 firms ([Fintech Futures](https://www.fintechfutures.com/venture-capital-funding/basis-raises-100m-series-b)).
- **Task:** bank and card reconciliation; recategorisation; accrual and close checklist; review notes for the CPA.
- **Who feels it / who approves:** staff accountant / firm partner.
- **Frequency:** weekly to monthly.
- **Dollar cost:** not verified.
- **Who sells a fix:** many bookkeeping BPOs and sub-$100 categorisation tools (not verified this pass). Crowded.
- **24-month trend:** shrinks as QuickBooks and Xero ship native agents (inference).
- **Down-market likelihood:** high. YC explicitly asks for AI-native accounting services ([Let's Data Science](https://www.letsdatascience.com/news/yc-requests-ai-native-startups-across-industries-1c422935)).
- **Strongest argument against:** platform bundling and offshore price competition.
- **Tests:** a pass; b pass; c pass; d pass; e pass; f borderline (categorisation is cheap, but cleanup plus close is not).
- **Attractiveness:** 4.

#### P8. B2B AR follow-up, remittance matching and deduction disputes for $5M-$50M companies (HALAL FLAG)
- **Problem:** Invoices go unpaid and deductions go unchallenged because no one chases them systematically.
- **Industry:** cross-industry finance operations.
- **Company size:**
  - Hurts most at small and mid-size B2B firms.
  - Funded startups target mid-market and enterprise (inference from round sizes: [Crowdfund Insider](https://www.crowdfundinsider.com/2025/11/255763-stuut-technologies-raises-29-5-million-series-a/); [FinTech Global](https://fintech.global/2026/04/22/monk-raises-25m-series-a-to-automate-receivables/)).
- **Task:** dunning emails and calls; match remittances to invoices; dispute short-pays.
- **Who feels it / who approves:** AR clerk / controller or CFO.
- **Frequency:** daily.
- **Dollar cost:** vendor claim from Fazeshift of more than 90% of manual AR tasks automatable ([The Paypers](https://thepaypers.com/fintech/news/fazeshift-obtains-usd-17-mln-in-series-a-round-for-ai-accounts-receivable)).
- **f test:** QuickBooks and Xero include basic reminders (not verified this pass).
- **Down-market likelihood:** medium-high.
- **Shariah question:** proximity to debt collection and to late-fee interest. No ruling given.
- **Strongest argument against:** free reminders in accounting platforms; collection-agency overlap.
- **Tests:** a pass; b pass; c pass; d pass; e pass; f borderline.
- **Attractiveness:** 5.

#### Rejected or weak: basic voice reception for home services, dental and auto service lanes
- Pain is proven: Avoca, Netic and Toma rounds; 45% of dealer calls unanswered (founder claim).
- Likely fails test (f): sub-$100-per-month AI receptionists exist, and field-service platforms are bundling AI. I did not verify this this pass.
- Only a done-for-you estimate follow-up and dispatch service may survive.
- **Attractiveness:** 3-4.

### Gaps
- US counts for every ignored segment (freight brokers by size, DME suppliers, distributors by revenue, PI firms by headcount, small government contractors, MGAs) are not verified. Census CBP was blocked (403) and the search budget ran out. Suggested sources: FMCSA broker authority counts; Census CBP for NAICS 488510, 621610, 532283, 423/424, 541110, 524210, 541211.
- Hourly time studies per task are not found.
- Pricing for sub-$100 competitors is not verified, so the (f) verdicts for P7, P8 and the rejected voice-reception segment are provisional.
- UK and Australian specifics (market size, local funded players) are not researched.
