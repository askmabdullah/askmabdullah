# Deep dive 05: Roll-up multi-entity close (P1) and AP payment-change fraud (P2)

Research date: 27 October 2026. Notes for the report writer. This file adds to `lens08_ownership_change.md` (P1) and `lens06_post_ai.md` (P2). I did not repeat facts already in those files unless a calculation needs them; where I reuse one, it is marked "(lens08)" or "(lens06)".

**Method caveats (read first)**
- I used exactly 30 web searches, the full budget. My one WebFetch attempt (reachreporting.com/pricing) failed with `getaddrinfo ENOTFOUND`. So **every figure below comes from search-engine result summaries, not pages I opened.** Each figure is attributed to the URL the search tool tied it to; where that tie was unclear, I say so.
- "Vendor claim" = the number comes from a company that sells a fix. "Estimate" = my own math, shown in full. "[prior knowledge, not verified, no URL]" = background knowledge I could not re-source this session. It must be checked before use.
- No verbatim operator quotes from podcasts or forums could be opened. The quotes below are the few the search tool returned verbatim.
- UK and Australia: I gathered UK and AU fraud data for P2. I gathered **nothing for P1 outside the US**.

**Problem cards at a glance (details under each question)**
- **P1, roll-up close: still strong, but more crowded and cheaper than lens08 implied.** The pain is the data clean-up before consolidation, not the arithmetic. Buyers pay $120K-$175K+ base for a multi-entity controller. Outsourced multi-entity bookkeeping is quoted at $1.5K-$4K+/month. Well-funded AI accounting roll-ups (Crete, $500M budget) and AI-native ERPs (Rillet, Campfire, DualEntry) are moving into this space. The work suits an offshore team: it runs to a monthly deadline and can be done out of US hours.
- **P2, payment-change fraud: weakened as a stand-alone service.** The losses are real (IC3 BEC $3.046B in 2025; AU payment redirection A$166.8M, up 9.3%). But the software already carries **$1M loss guarantees** (Eftsure, Trustpair). Nacha's 2026 rules push banks to monitor credit-push fraud. Account-ownership checks are now API calls. Courts tend to put losses on whoever was "best positioned" to prevent them, which would be the verifier. And the work needs real-time callbacks in US business hours. It fits better as an add-on to a broader AP or close service than as a product on its own.

---

## Q1. The exact task, in plain words

### Takeaway
**P1.** Every month, the platform controller pulls N separate ledgers, mostly QuickBooks/Xero, each with its own chart of accounts and close calendar. They clean and map each one to the group chart, book accruals, intercompany charges and eliminations, and consolidate. Then they write site benchmarks and commentary for the sponsor pack, typically due 10-20 business days after month-end. First-time owners do a one-entity version: convert the seller's cash-basis books to accrual and produce a monthly investor update.

**P2.** An AP clerk receives a request to change a supplier's bank account, or an invoice that looks off. The clerk must:
- confirm the request through a channel the fraudster does not control (a call to the number already on file);
- check that the new account belongs to the supplier;
- get a second approver;
- record the evidence before the next payment run.

### Cited Findings
**P1: roll-up platform**
- Roll-ups inherit, per acquisition, a separate general ledger, chart of accounts, close calendar and definition of revenue. "Acquired companies bring six general ledgers, six charts of accounts, six close calendars, and six definitions of revenue, and someone has to make those agree before consolidation." The same guide says "AI does not clean the data, and that is where most roll-up finance pain lives." Guide or affiliate content, not an operator. — [WorkWise Solutions](https://workwisesolutions.org/guides/best-ai-roll-up-consolidation-software.html)
- PE sponsors typically expect a core monthly reporting package within about 15-20 business days of month-end, and some push for a 10-day close. Outsourcing-firm blog. — [Madras Accountancy](https://madrasaccountancy.com/blog-posts/outsourced-financial-reporting-private-equity-portfolio)
- Consolidation tools describe the mechanical steps: sync actuals from NetSuite or QuickBooks, align charts of accounts across entities, handle FX, book intercompany eliminations, and produce consolidated statements. Vendor. — [Cube](https://www.cubesoftware.com/cube-for-controllers)
- Intuit Enterprise Suite runs each entity in its own instance, with a separate consolidated instance for reporting. This matters for migration and permissions. — [TechRepublic review 2026](https://www.techrepublic.com/article/intuit-enterprise-suite-reviews/) (the search summary did not say which review this came from; treat as approximate)

**P1: first-time owner (search fund / SBA)**
- A SearchFunder post describes a PE firm moving a newly acquired company from cash to accrual, because "cash basis of accounting made it difficult for the PE firm to track profitability and report to LPs." Vendor-authored post. — [SearchFunder](https://searchfunder.com/post/from-cash-flow-to-clearer-financial-picture-helping-client-thrive)
- Typical post-acquisition deliverables are monthly reporting packages, cash-flow forecasting, KPI dashboards and a tighter month-end close. "Financial operations can quickly become strained if processes remain manual or overly dependent on individuals." Vendor-authored. — [SearchFunder: How Accountants Support Search Funds After the Deal](https://searchfunder.com/post/how-accountants-support-search-funds-after-the-deal)
- A common outsourced model has a controller review the GL monthly, issue financial statements and lock the period. A 10-15 business-day close is cited as standard. Vendor. — [Cocountant](https://cocountant.com/blog/bookkeeping/when-to-use-scale-up-bookkeeping-features-kpis-accrual/)

**P2: AP payment-change verification**
- Recommended control: verify bank-detail changes by calling back a pre-approved number in the vendor master record, never a number given in the email. Treat as warning signs a sudden change in the beneficiary bank's country, or pressure to switch to wire or crypto. Vendor guidance. — [Corpay](https://www.corpay.com/resources/blog/prevent-vendor-impersonation-fraud-accounts-payable)
- Typical attack: criminals intercept or copy a real invoice and change only the bank details. Recommended controls are to phone a contact on the number already on file and to have a second person sign off any bank-detail change. — [Canberra Times](https://www.canberratimes.com.au/story/9218144/beware-the-urgent-email-at-the-end-of-the-working-day/); [Eftsure blog](https://www.eftsure.com/blog/industry-news/$167m-lost-in-2025-why-bec-scams-keep-costing-australians/) (vendor)
- Real case: the City of Baltimore's AP department made two EFT payments totalling **$1,524,621.04** to an unauthorised account in early 2025. A fraudster had got into the vendor's Workday supplier account and changed the bank details there. — [Security Affairs](https://securityaffairs.com/181772/cyber-crime/fraudster-stole-over-1-5-million-from-city-of-baltimore.html)
- Vendor-master job posts list the same duties: sanctions screening, bank verification and fraud checks (Volkswagen Group Canada); TIN matching and W-9 upkeep (West Fraser). — [VW Group Canada posting](https://jobs.volkswagen-group.com/Volkswagen/job/Ajax-AP-Vendor-Master-Specialist-ON-L1S-7G7/1371770033); [West Fraser posting](https://www.westfraser.com/jobs/sr-ap-vendor-master-data-specialist)

### Inferences
- **P1 task card:** "Each month the platform controller exports 10-30 QuickBooks or Xero trial balances, maps each to the group chart of accounts, fixes miscoded items, books accruals (payroll, provider pay, unbilled work, membership or maintenance-plan deferred revenue), books intercompany management fees and eliminations, consolidates, and writes the site benchmark and variance commentary for the sponsor's pack by business day 10-20. Each new add-on adds a one-time onboarding: an opening balance sheet, cash-to-accrual conversion and chart mapping."
- **P2 task card:** "An AP clerk gets an email or portal change asking to switch a supplier's bank account. The clerk freezes payments to that supplier, calls the supplier on the number already in the vendor file (not the number in the email), runs an account-ownership check, gets a second approver, logs the evidence for the auditor and insurer, and releases or blocks before the next payment run. The same desk screens 'urgent' invoices whose bank details differ from history."
- The Baltimore case shows the change can come through the **supplier's portal or ERP account**, not only email, so a "check the email" control is not enough.

### Gaps
- No operator-voiced description of the P1 task (podcasts and SearchFunder threads could not be opened).

---

## Q2. Who feels it, and who approves the money

### Takeaway
**P1:** The pain sits with the platform controller, VP Finance or holding-company controller, and the site managers being chased for data. Money is approved by the platform CFO or CEO, with strong influence from the sponsor's operating partner. For search-fund and SBA buyers, the owner-CEO feels it and approves it.

**P2:** The pain sits with AP specialists, vendor-master specialists and the AP manager. Money is approved by the controller or CFO, sometimes with treasury or the CISO.

### Cited Findings
**P1**
- A lower-middle-market PE firm in Clayton, MO, with about a dozen operating companies, is hiring a **holding-company Controller**: max salary $160,000, 10-20% bonus, 5+ years' experience (posted 14 Jan 2026). — [PCRecruiter job board](https://host.pcrecruiter.net/pcrbin/jobboard/job/Controller/b/LAD7CGTS6ZMHSILH2XDSJU6XWBWSXRIDZTODGWAFRETOKJZZM7MA2LMN3SG5LUM3MWJVATBIU4) (the search tool tied this posting to the result set; the exact URL match is likely but not certain)
- Robert Half "Controller - Private Equity" in Fort Lauderdale (posted 19 Dec 2025) covers all accounting, finance, tax and treasury across a multi-entity portfolio. Salary not shown. — [Career.com / Robert Half](https://www.career.com/job/robert-half/financial-controller/j202512051542082879100)
- Other 2026 multi-entity controller postings: Grand Rapids, MI ($150K-$165K, a portfolio of operating entities); West Hollywood, CA ($145K-$170K plus bonus, 10-15 legal entities); Red Lion, PA ($150K-$175K, multi-entity real estate); Visalia, CA (PE-backed, $120K-$150K base). — [Mediabistro posting 1](https://www.mediabistro.com/jobs/3523129567-controller); [Mediabistro posting 2](https://www.mediabistro.com/jobs/3523131918-controller); [Tallo, Red Lion PA](https://tallo.com/talent/job/finance/treasurer-or-controller/pa/red-lion/controller-57986a96) (the search summary did not map each salary to its URL; Red Lion matches the Tallo URL; the others are spread across these listings)
- Search-fund CEOs report to investor boards monthly or quarterly (lens08, [SearchFunder](https://searchfunder.com/post/standards-for-investor-updates)).

**P2**
- Vendor-master roles range from entry level to senior:
  - Discount Tire asks for 1+ year of vendor-master experience and a high-school diploma; certification "in vendor setup or fraud prevention" is a plus. — [Discount Tire](https://careers.discounttire.com/ap-vendor-master-data-specialist-i/job/E4BCF05C5BF5EFB97E4AF7774D34845B)
  - An analyst posting asks for 5-8 years in AP or vendor-master work and procure-to-pay knowledge. — [AP Master Vendor Analyst listing](https://www.jofdav.com/jobs/49374269-ap-master-vendor-analyst) (the search summary named the employer as Vericast; the URL match is uncertain)
- A November 2025 AP conference deck lists "vendor master file change rate" as a KPI and calls "changes to banking information (most critical for preventing fraud)". — [Jamie Umpleby, "KPIs Every AP Should Track" deck](https://divcomevents2-static.s3.amazonaws.com/uploads/sites/3/2025/10/THURS-105-Milano-VI-KPIs-Every-AP-Should-Track-Jamie-Umpleby.pdf)
- Public-sector example: Minneapolis Finance does quarterly control testing on a sample of new vendor setups and changes, "augmented by the AP Manager who will scan and review new vendors and vendor changes on a monthly basis." — [City of Minneapolis audit response](https://www2.minneapolismn.gov/media/content-assets/www2-documents/departments/wcms1p-103480.pdf)
- A mid-market CFO reviewing Trustpair on G2 called it a must-have to avoid wire fraud. That is a CFO acting as buyer. — [G2 Trustpair pricing](https://www.g2.com/products/trustpair/pricing)

### Inferences
- In P1 the payer (platform CFO) and the person in pain (controller) usually sit close together, which helps a sale. In P2 the AP clerk feels the work daily, but the CFO only feels it after a loss. That makes P2 a harder, insurance-style sale.
- A job post for a holding-company controller is a direct buying signal for P1: the firm is about to spend about $160K-$190K a year (base plus 10-20% bonus).

### Gaps
- No pay data for a dedicated "AP fraud analyst" title (not found).
- No sourced split of approval authority between operating partner and platform CFO.

---

## Q3. How often it happens and how many hours it eats (math shown)

### Takeaway
**P1:** Monthly, plus a one-time onboarding for each add-on. Estimate: **about 70-140 staff hours a month for a 14-entity platform** (about 0.45-0.9 FTE), and 140-280 hours for 30 entities.

**P2:** Daily to weekly. Estimate: **about 9-65 hours a month** for a mid-market AP team. Hours are not the main cost; response time and the loss tail are.

### Cited Findings
- No sourced hours-per-entity or hours-per-close benchmark was found for P1.
- Vendor time-saving claims (vendor claims, not benchmarks):
  - ScaleXP says QuickBooks and Xero users save 3-5 days a month. — [ScaleXP](https://www.scalexp.com/integrations/quickbooks/)
  - A vet group cut its close from up to 23 days to 6-7 days after moving to Sage Intacct (lens08, BTerrell).
- Close-cycle expectations: 15-20 business days to the sponsor pack, with some sponsors pushing for 10 days. — [Madras Accountancy](https://madrasaccountancy.com/blog-posts/outsourced-financial-reporting-private-equity-portfolio)
- No published benchmark exists for vendor-master changes per month or minutes per bank-change verification. APQC does not publish a universal cost per vendor-master record. — [Stealth Agents (secondary, citing APQC)](https://stealthagents.com/research/small-business-vendor-master-data-maintenance-statistics-2026)
- APQC median supplier setup cycle: 3.0 calendar days across 3,047 companies (secondary). — [Stealth Agents citing APQC](https://stealthagents.com/research/small-business-vendor-master-data-maintenance-statistics-2026)
- IOFM's expert: "There is no industry standard for holding payments…" after a bank change. The rest of the answer is paywalled. — [IOFM Ask the Expert](https://www.iofm.com/ask-the-expert/vendor-banking-change-safeguards-and-payment-hold-guidelines)
- 45% of US companies with revenue of $500M+ spent multiple days responding to a single fraud incident (vendor-commissioned survey). — [Trustpair 2026 Fraud Report press release](https://www.businesswire.com/news/home/20260126508647/en/AI-Fraud-Outpaces-Human-Defenses-as-71-of-U.S.-Companies-Report-Rise-in-Attacks-Trustpair-Report-Finds)

### Inferences (all estimates; the assumptions are mine)
**P1, 14-entity platform (QuickBooks sites with a local bookkeeper):**

| Step | Hours per entity per month |
|---|---|
| Pull trial balance and map | 0.5-1 |
| Review and reclass miscodes | 1-3 |
| Accruals and intercompany | 1-2 |
| Reconciliation and balance-sheet checks | 1-2 |
| **Total per entity** | **about 4-8** |

- Group-level work (consolidation, eliminations, pack, commentary, chasing): 15-30 hours.
- 14 entities: 14 × 4-8 = 56-112, plus 15-30 = **71-142 hours a month** (0.45-0.9 FTE at 160 hours a month).
- 30 entities: 30 × 4-8 = 120-240, plus 20-40 = **140-280 hours a month** (0.9-1.75 FTE).
- Each add-on adds about 20-60 one-time hours (opening balance sheet, cash-to-accrual, mapping). At 1-2 add-ons a month, that is another 20-120 hours a month.

**P1, first-time owner (one entity):** 15-30 hours for the accrual close plus 4-8 hours for the investor pack = **about 19-38 hours a month**.

**P2, mid-market firm (about 500-2,000 employees, about 2,000 invoices a month):**
- Bank-detail change requests: 5-20 a week × 15-30 minutes (callback, no-answer retries, account-ownership check, evidence log) = 1.25-10 hours a week.
- Suspicious-invoice review: 1-3% of about 460 invoices a week = about 5-14 flags × 10-20 minutes = 0.8-4.6 hours a week.
- Total: about 2-15 hours a week, or **about 9-65 hours a month**.
- **Timing constraint:** each change must clear before the next payment run, usually daily or weekly.

### Gaps
- No sourced hours per entity, entities per platform controller, or verification minutes. All P1 and P2 hours above are estimates, to be checked in buyer interviews.

---

## Q4. What it costs a typical company each month (math shown)

### Takeaway
**P1:** Estimate **$5.8K-$16.9K a month** in staff time for a 14-entity platform. Software adds $280-$950 a month (Fathom or Reach) up to $12K-$186K a year (Intuit Enterprise Suite or NetSuite OneWorld). A material EBITDA error can be worth roughly 9x its size at exit.

**P2:** Estimate **$0.3K-$2.6K a month** in staff time plus **$0.5K-$2.6K a month** in expected fraud loss, with a tail of single losses above $1.5M. Real but modest monthly value, which caps price.

### Cited Findings
**P1**
- Multi-entity controller base pay in 2026 postings: $120K-$175K, plus 10-20% bonus where stated (see Q2 sources). A staffing firm's 2026 guide puts controllers at $115K-$185K base, and corporate controllers at audited multi-entity companies at $175K-$235K. The firm earns fees on hires. — [KORE1 controller salary guide](https://www.kore1.com/controller-salary-guide/)
- Intuit Enterprise Suite (third-party estimates; Intuit sells by quote only):
  - single entity about $7.8K-$8K a year; 2-5 companies $12K-$15K; 5+ companies $15K+;
  - implementation extra;
  - TechRepublic says "low-to-mid five figures" for multi-entity.
  - Sources: [ERP Research](https://erpresearch.com/en-us/intuit-enterprise-suite-pricing) (reseller-style site); [TechRepublic](https://www.techrepublic.com/article/intuit-enterprise-suite-reviews/)
- NetSuite OneWorld (estimates conflict across sources):
  - module about $24K-$30K a year, plus about $9K-$12K a year per extra legal entity — [Houseblend](https://www.houseblend.io/articles/en/netsuite-oneworld-vs-netsuite-erp-tarifs-fonctionnalites);
  - each subsidiary is a recurring annual line with a 5-10% compounding escalator — [Oracle Licensing Experts](https://oraclelicensingexperts.com/blog/netsuite-oneworld-licensing/);
  - cap of 250 subsidiaries — [send.win](https://blog.send.win/?p=8273).
- Sage Intacct: the multi-entity add-on is about $3K-$10K+ a year, scaling with entity count — [send.win](https://blog.send.win/?p=8273). Typical mid-market deployments run $20K-$90K a year, against $30K-$150K for NetSuite — [TechVendorIndex](https://techvendorindex.pages.dev/compare/netsuite-vs-sage-intacct/)
- The MSP median exit multiple is about 9x EBITDA (lens08, [Aventis](https://aventis-advisors.com/who-is-buying-msps/)).

**P2**
- IC3 2025: BEC losses $3.046B from 24,768 complaints (lens06, [iTnews](https://www.itnews.com.au/news/ai-assisted-fraud-makes-big-debut-in-fbis-cybercrime-stats-624819)).
- One in four US companies with revenue of $500M+ reported six-figure fraud losses in the past year. 250 respondents, Dynata, fielded November 2025, commissioned by Trustpair (vendor claim). — [Trustpair via BusinessWire](https://www.businesswire.com/news/home/20260126508647/en/AI-Fraud-Outpaces-Human-Defenses-as-71-of-U.S.-Companies-Report-Rise-in-Attacks-Trustpair-Report-Finds)
- Baltimore lost $1,524,621.04 in two EFT payments (early 2025). — [Security Affairs](https://securityaffairs.com/181772/cyber-crime/fraudster-stole-over-1-5-million-from-city-of-baltimore.html)
- Insurance offsets less than buyers think:
  - social-engineering sublimits were historically about $100K-$250K — [Insurance Journal (Lowenstein), 2023](https://www.insurancejournal.com/news/national/2023/03/02/710068.htm);
  - some cyber policies carry $250K-$500K social-engineering sublimits — [Business Insurance](https://www.businessinsurance.com/crime-cover-tackles-phishing-risk-scams-social-engineering-fraud/);
  - a missed callback condition limits coverage — [Bank Director](https://www.bankdirector.com/?p=5427).
- AP vendor-master specialist pay: about $47.1K-$58.6K a year (Fanatics, Jacksonville; a Tallo estimate, not a posted range). — [Tallo](https://tallo.com/jobs/finance/bookkeeper-accounting-clerk/fl/duval/ap-specialist-vendor-master-data)

### Inferences (estimates)
**P1, staff time at a 14-entity platform**
- Loaded controller cost: $120K-$175K base × 1.3 (bonus and benefits) = $156K-$228K a year. Divided by 1,920 hours, that is $81-$119 an hour.
- 71-142 hours × $81-$119 = **$5.8K-$16.9K a month**.
- Full-time alternative (Clayton MO example): $160K × 1.15 bonus × 1.25 benefits ≈ $230K a year ≈ **$19K a month**.

**P1, software for 14 entities**
- Fathom Gold $400 or Reach $550 a month (lens08).
- Intuit Enterprise Suite about $15K+ a year (about $1.25K+ a month).
- NetSuite OneWorld: $24K-$30K + 13 × $9K-$12K = **$141K-$186K a year**. This uses the Houseblend per-entity figure, which other sources may not support; treat it as the top of the range.

**P1, cost of a wrong number (illustration, not a sourced loss)**
- A $100K EBITDA misstatement at a 9x multiple is about $900K of enterprise value at exit or in a lender test.
- Late packs damage sponsor trust; no dollar figure was found.

**P1, first-time owner:** 19-38 hours × $81-$119 = $1.5K-$4.5K a month equivalent, against $450-a-month bookkeeping offers on SearchFunder (Q5) and $6K-$12K fractional CFOs (lens08).

**P2, staff time**
- Loaded AP specialist: $47K-$59K × 1.3 / 1,920 ≈ $32-$40 an hour.
- 9-65 hours × $32-$40 = **$290-$2,600 a month**.

**P2, expected loss**
- Average BEC complaint: $3.046B / 24,768 ≈ **$123K**.
- Assume a mid-market firm faces a 5-25% annual chance of a six-figure loss. The upper bound is Trustpair's figure for larger firms; the lower bound is my assumption.
- Expected loss = $123K × 5-25% = **$6.2K-$30.8K a year, or about $0.5K-$2.6K a month**.
- Add incident response: 45% of firms spend multiple days per incident.

**P2, total:** about **$0.8K-$5.2K a month** per mid-market company, plus a fat tail (Baltimore $1.5M; insurance sublimits often $100K-$500K). That points to a price ceiling around **$1K-$3K a month**, unless the service is bundled or carries a guarantee.

### Gaps
- No AFP figure for the share of firms with an *actual loss*, as opposed to attempted fraud (the full report costs $295; not reached).
- No sourced cost of a late or wrong sponsor pack.
- No mid-market (sub-$500M revenue) loss-probability data.

---

## Q5. How companies handle it today and what they pay

### Takeaway
**P1:** Mid-size platforms hire a holding-company controller ($120K-$175K base) or a fractional CFO ($6K-$25K a month). They outsource bookkeeping at about $1.5K-$4K+ a month for multi-entity, or about $450-$1,750+ a month for smaller firms. They stitch it together in Fathom or Reach, then migrate to Intuit Enterprise Suite, Sage Intacct or NetSuite OneWorld.

**P2:** AP teams rely on:
- manual callbacks and dual approval;
- ERP or AP-suite change workflows (BILL, Dynamics 365);
- bank positive pay and Nacha-driven bank monitoring;
- at larger firms, vendor-verification SaaS (Trustpair, Eftsure, Paymode, Early Warning, Plaid). These are quote-priced and come with $1M loss guarantees.

### Cited Findings
**P1: services**
- Pilot CFO services start at $1,750 a month (August 2026 comparison). Multi-entity is "customized pricing" on its Plus plan. The Pilot Core entry price conflicts: $699 a month (2024 blog) vs $599 a month for under $30K monthly expenses (recent piece). — [Pilot blog: ProvenCFO alternatives](https://pilot.com/blog/provencfo-alternatives); [The Digital Merchant](https://thedigitalmerchant.com/?p=77506) (the summary did not map each figure to its URL)
- Kruze (2024, per a Pilot competitor blog): Basic from $600 a month for startups with under $150K monthly expenses; Founder Timesaver from $850; Premium $750 for $150K-$300K; custom above that. Kruze focuses on funded Delaware C-corps from pre-seed to Series C/D. — [Pilot: Escalon alternatives](https://pilot.com/blog/escalon-services-alternatives) (competitor content, 2024)
- indinero starts at $750 a month, fixed-price and month-to-month, and lists multi-entity consolidation. — same Pilot comparison set (URL tie uncertain)
- Escalon: no public price. It markets fractional CFO, monthly close and multi-state tax and payroll as one vendor, against Pilot, Bench and Kruze. — [Escalon](https://escalon.services/new-home)
- Fixed monthly plans for multi-entity or inventory-heavy companies cost about **$1,500-$4,000+ a month**. Per-transaction pricing is $0.50-$2.00 a transaction with a $200-$300 monthly minimum. Catch-up clean-up costs $500-$5,000 one-time. Single vendor's estimates. — [Ecosire](https://ecosire.com/blog/outsourced-bookkeeping-cost-2026)
- Bookkeeping offered on SearchFunder starts at $450 a month, with a free pre-acquisition assessment (promotional). — [SearchFunder bookkeepers thread](https://searchfunder.com/post/bookkeepers-please-introduce-yourself-here)
- Offshore F&A providers market directly to PE portfolios:
  - Personiv offers "comprehensive offshore finance and accounting solutions" for PE firms and cites ISO and PCI certifications — [Personiv](https://www.personiv.com/private-equity);
  - QX Accounting sells PE outsourcing — [QX](https://qxaccounting.com/usa/blog/how-accounting-outsourcing-benefits-your-pe-firm/);
  - PKF O'Connor Davies says it can replace all or part of a portfolio company's accounting function — [PKF O'Connor Davies](https://www.pkfod.com/industries/financial-services/outsourced-corporate-accounting).

**P1: software** (see Q4 for Intuit Enterprise Suite, NetSuite and Sage Intacct; Fathom and Reach in lens08)
- Rillet: about $20K-$35K a year by third-party benchmark, priced by complexity rather than seats. G2 multi-entity score 8.9 (36 reviews). — [ERP Research AI-native ERP](https://erpresearch.com/en-us/ai-native-erp); [G2](https://www.g2.com/compare/dualentry-vs-rillet)
- DualEntry: tiers by entity count (up to 3, up to 20, unlimited). No list price. G2 multi-entity score 9.3 (75 reviews). — [RFP.wiki](https://www.rfp.wiki/accounting-finance/rillet/dualentry); [G2](https://www.g2.com/compare/dualentry-vs-rillet)
- Campfire: native multi-entity consolidation. No price found. — [DualEntry blog (competitor)](https://www.dualentry.com/blog/campfire-erp-alternatives)
- ScaleXP: a "Full AI Close" for QuickBooks with multi-entity consolidation (vendor). — [ScaleXP](https://www.scalexp.com/integrations/quickbooks/)
- LiveFlow: multi-entity consolidation into Google Sheets (vendor). — [Google Workspace Marketplace: LiveFlow](https://workspace.google.com/marketplace/app/liveflow/329923094148)

**P2: built-in controls**
- BILL: when a user saves a manual vendor bank change, BILL emails the vendor to confirm and shows old and new details side by side. **The confirmation is not required before payments to that vendor can be scheduled.** — [BILL help center](https://vendorpayhelp.bill.com/hc/en-us/articles/360056648731)
- Microsoft Dynamics 365 Finance has a vendor-bank-account approval workflow. — [Microsoft Learn](https://learn.microsoft.com/en-us/dynamics365/finance/accounts-payable/vendor-bank-account-workflow)
- Gatekeeper markets an agent that screens bank-detail changes against fraud patterns before payment (vendor). — [Gatekeeper](https://www.gatekeeperhq.com/blog/bank-details-validator-screen-vendor-bank-detail-changes-against-fraud-patterns-before-payment)
- Ramp published a guide to the 2026 Nacha rule changes (14 May 2026). Ramp's own bank-change features were not confirmed. — [Ramp blog](https://ramp.com/blog/2026-nacha-rule-changes)

**P2: verification SaaS and bank services**
- Trustpair:
  - quote-based; G2 entry plan is "Platform Access" plus a fixed number of vendor evaluations a year, price "Contact Us"; G2 cost rating "$$$$$" (2 reviews) — [G2](https://www.g2.com/products/trustpair/pricing); [Capterra](https://www.capterra.com/p/187396/Trustpair/);
  - bank-account ownership checks in 190+ countries, IBAN/ACH checks, TIN matching, and **up to $1M liability coverage on the enterprise plan** — [ERP Research](https://erpresearch.com/erp-add-ons/fraud-risk/trustpair).
- Eftsure:
  - price scales with **annual expenditure and the number of new vendors onboarded each month**; all features bundled — [Eftsure pricing](https://eftsure.com/pricing);
  - the **Eftsure Guarantee**, included for agreements signed after 10 March 2025, covers up to $1M if a verified payment is lost to social engineering — [Eftsure pricing](https://eftsure.com/pricing);
  - vendor claim: protects $120B+ in payments a year — [Eftsure](https://www.eftsure.com/blog/industry-news/protecting-over-5-billion-eft-payments/).
- Early Warning Verify Account returns account status, an ownership match and a match score. Price only through account managers. — [Early Warning Verify Account brief](https://www.earlywarning.com/sites/default/files/2024-02/Verify-account-product-brief-v3-20240202.pdf)
- Plaid Identity Match:
  - a per-request flat fee; prices are visible only after Production access; pay-as-you-go and Growth plans — [Plaid billing docs](https://plaid.com/docs/account/billing);
  - Vendr: most Plaid products cost about $0.10-$0.60 per successful call (unverified, not specific to Identity Match) — [Vendr](https://www.vendr.com/marketplace/plaid).
- Paymode (Bottomline): "contact vendor". Vendor claim: verifies member businesses on 300+ data points, with digital bank authentication and OFAC screening. — [Capterra](https://www.capterra.com/p/234113/Bottomline-Paymode-X/); [Bottomline document](https://www.bottomline.com/download_file/410be7c0-79d9-414b-902e-9ee2639d1bde/1564)
- Reliance on mainly manual validation fell from 69% to 48% year on year among $500M+ US firms (vendor claim). — [Trustpair via BusinessWire](https://www.businesswire.com/news/home/20260126508647/en/AI-Fraud-Outpaces-Human-Defenses-as-71-of-U.S.-Companies-Report-Rise-in-Attacks-Trustpair-Report-Finds)
- Only 17% of firms use AI to fight payments fraud (lens06, AFP 2026).

### Inferences
- P1 already has a services market at $450-$4,000+ a month and a hire at about $160K-$230K a year. An AI-plus-human multi-entity close service fits at about **$2K-$8K a month** for 5-30 entities, clearly below a hire and above commodity bookkeeping.
- P2: BILL's confirmation is optional, and many mid-market firms sit below Trustpair and Eftsure's enterprise focus. That leaves a gap, but it is narrow.

### Gaps
- Not found: Fuelfinance prices; Bench successor (Bench shut down and was acquired in late 2024/early 2025 [prior knowledge, not verified, no URL]); Jirav prices; Escalon prices; Paymentus vendor-verification offering; AppZen, Medius and Coupa prices.

---

## Q6. Proof: operator quotes, surveys and job posts

### Takeaway
**P2** has strong neutral survey and loss data:
- IC3, AFP, ACCC and UK Finance;
- vendor surveys (Trustpair, 71% report rising AI attacks);
- regulatory change (Nacha 2026).

**P1** has job-post and vendor evidence but almost no verbatim operator quotes.

### Cited Findings
**P2: surveys and statistics**
- AFP 2026 Payments Fraud and Control Survey (2025 data):
  - 76% of organisations had attempted or actual payments fraud, slightly down from 2024;
  - most-targeted methods: checks 58%, ACH debits 30%, wires 25%;
  - BEC hit about three-quarters of organisations;
  - first-time questions on AI and deepfake impersonation of executives **and vendors**;
  - sources: [AFP report page](https://www.financialprofessionals.org/publications-data-tools/reports/survey-research-economic-data/Details/payments-fraud); [Truist key-highlights PDF](https://www.truist.com/content/dam/truist-bank/us/en/documents/info/cci/2026-afp-payments-fraud-control-survey-report-key-highlights.pdf).
- AFP 2025 survey (2024 data):
  - vendor impersonation was cited by **60%** of respondents, and third-party impersonation was the most frequent BEC type at **63%**;
  - wires were the method BEC targeted most (63%, up from 39%), and **ACH credits rose to 50%**;
  - source: [AFP report page](https://www.financialprofessionals.org/publications-data-tools/reports/survey-research-economic-data/Details/payments-fraud) (the search summary attributed these to the 2025 report; check against the 2025 PDF).
- Trustpair 2026 Fraud Report (vendor claim; 250 senior finance decision-makers at US firms with $500M+ revenue; Dynata; November 2025):
  - 71% report more AI-powered fraud attempts;
  - 47% say AI-generated fraud is one of their biggest challenges;
  - BEC affected 62%, fake websites 48%, SMS scams 45%;
  - one in four had six-figure losses.
  - Source: [BusinessWire](https://www.businesswire.com/news/home/20260126508647/en/AI-Fraud-Outpaces-Human-Defenses-as-71-of-U.S.-Companies-Report-Rise-in-Attacks-Trustpair-Report-Finds); [Trustpair](https://trustpair.com/blog/press-release-2026-fraud-report-is-out/)
- Nacha 2026 fraud-monitoring rules:
  - Phase 1 from 20 March 2026 (larger institutions); Phase 2 from 19 June 2026, in practice Monday 22 June 2026;
  - originators (ODFIs and originating third parties) must monitor for entries that are unauthorised or "authorized under false pretenses", which covers BEC and vendor or payroll impersonation;
  - RDFIs with 10M+ receipts in 2023 must monitor incoming credits;
  - not every entry must be screened individually, but "no monitoring" is not acceptable;
  - sources: [Nacha rules page](https://www.nacha.org/rules/risk-management-topics-fraud-monitoring-phase-2); [American Banker](https://www.americanbanker.com/news/new-nacha-fraud-rules-to-take-effect-in-2026); [Eftsure blog](https://www.eftsure.com/blog/industry-news/nachas-2026-fraud-monitoring-rules-what-every-finance-team-needs-to-know/).
  - **Sources conflict on account validation.** Ramp says the 2026 changes include "mandatory account verification before sending an ACH credit" — [Ramp](https://ramp.com/blog/2026-nacha-rule-changes). Eftsure says account validation was a long-standing best practice "now formalized" — [Eftsure](https://www.eftsure.com/blog/industry-news/nachas-2026-fraud-monitoring-rules-what-every-finance-team-needs-to-know/). Both are vendors; check the Nacha rule text.
- Australia (ACCC / National Anti-Scam Centre via secondary sources):
  - payment redirection losses **A$166.8M in 2025, up 9.3%** from A$152.6M, one of the only top-five categories to rise;
  - small businesses filed 2,228 scam reports with A$9.5M in losses; false billing was their most common category;
  - sources: [Eftsure blog](https://www.eftsure.com/blog/industry-news/$167m-lost-in-2025-why-bec-scams-keep-costing-australians/) (vendor); [Canberra Times](https://www.canberratimes.com.au/story/9218144/beware-the-urgent-email-at-the-end-of-the-working-day/); [IT Brief](https://itbrief.com.au/story/no-one-s-just-a-number-the-finance-team-blind-spot-behind-australia-s-rising-payment-scams). Not checked against the ACCC primary report.
- UK (UK Finance Annual Fraud Report 2026, via secondary sources):
  - 2025 payment-fraud losses about £1.28bn (+4%); confirmed cases 4.06M (+11%);
  - APP losses £576.4m (+19%), about 61% reimbursed;
  - invoice and mandate, CEO and impersonation fraud fell to multi-year lows, now under a quarter of APP losses, down from more than half in 2020;
  - one outlet gives 2025 invoice and mandate losses as £41.3m (unverified); H1 2025 was £19.9m, down 24%;
  - sources: [Payment Expert](https://paymentexpert.com/2026/06/15/uk-finance-fraud-report-2026/); [FinTech Futures](https://www.fintechfutures.com/financial-crime-fraud-prevention/uk-payment-fraud-losses-topped-1-28bn-in-2025-new-uk-finance-report-finds); [Ground News](https://groundnews.lakegeneva.lib.wi.us/article/redirected-invoice-scams-down-but-fraud-remains-a-national-security-threat); [Today's Conveyancer](https://todaysconveyancer.co.uk/invoice-and-mandate-scams-fall-but-fraud-remains-a-major-threat/).
- Singapore Police advisory (20 May 2026): at least 66 BEC cases involving "requests to update vendors" since 1 January 2026, with losses of at least $19M (currency presumably SGD). Victims usually found out only when the vendor said it had not been paid. — [Singapore Police Force](https://www.police.gov.sg/Media-Hub/News/2026/05/20260520_police_advisory_on_business_email_compromise_scams_involving_requests_to_update_vendors)

**P2: quotes (verbatim per search summaries)**
- IOFM expert: "There is no industry standard for holding payments…" after a bank change. — [IOFM](https://www.iofm.com/ask-the-expert/vendor-banking-change-safeguards-and-payment-hold-guidelines)
- AP KPI deck: banking-information changes are "most critical for preventing fraud." — [Umpleby deck, Nov 2025](https://divcomevents2-static.s3.amazonaws.com/uploads/sites/3/2025/10/THURS-105-Milano-VI-KPIs-Every-AP-Should-Track-Jamie-Umpleby.pdf)
- AFP practitioner "Ward" on LLM-polished phishing (lens06).
- No named AP-manager quote describing a lost payment was found.

**P2: job posts**
- VW Group Canada (AP Vendor Master Specialist: sanctions, bank verification, fraud checks); West Fraser (Sr AP Vendor Master Data Specialist); Discount Tire (AP Vendor Master Data Specialist I); Fanatics (AP Specialist, Vendor Master Data, about $47.1K-$58.6K Tallo estimate); Addison Group, Washington DC (AP Vendor Management Specialist). — [VW](https://jobs.volkswagen-group.com/Volkswagen/job/Ajax-AP-Vendor-Master-Specialist-ON-L1S-7G7/1371770033); [West Fraser](https://www.westfraser.com/jobs/sr-ap-vendor-master-data-specialist); [Discount Tire](https://careers.discounttire.com/ap-vendor-master-data-specialist-i/job/E4BCF05C5BF5EFB97E4AF7774D34845B); [Tallo/Fanatics](https://tallo.com/jobs/finance/bookkeeper-accounting-clerk/fl/duval/ap-specialist-vendor-master-data); [Career.com/Addison](https://www.career.com/job/addison-group/accounts-payable-vendor-management-specialist/j202605222203068036390). Posting dates were mostly not shown in the snippets.

**P1: quotes and evidence**
- Guide quote: "AI does not clean the data, and that is where most roll-up finance pain lives." — [WorkWise](https://workwisesolutions.org/guides/best-ai-roll-up-consolidation-software.html) (guide, not an operator)
- SearchFunder post: "Cash basis of accounting made it difficult for the PE firm to track profitability and report to LPs." — [SearchFunder](https://searchfunder.com/post/from-cash-flow-to-clearer-financial-picture-helping-client-thrive) (vendor-authored)
- Job posts: Clayton MO holding-company Controller (about a dozen opcos, max $160K + 10-20% bonus, 14 Jan 2026); Robert Half "Controller - Private Equity", multi-entity (19 Dec 2025); Grand Rapids $150K-$165K; West Hollywood $145K-$170K for 10-15 entities; Red Lion PA $150K-$175K; Visalia PE-backed $120K-$150K (see Q2 for URLs and caveats).
- A career guide notes that portfolio-company CFO and finance director roles often carry equity (MIPs). — [LearnSignal](https://www.learnsignal.com/blog/private-equity-finance-career-guide-2026/)

### Inferences
- P2 is the better-evidenced problem. P1 is the better-shaped business: the buyer is closer to the pain, and the work is regular and asynchronous.
- The UK data is a warning for P2: once banks carry reimbursement duties and run Confirmation of Payee, invoice and mandate fraud falls to multi-year lows. US Nacha rules move in that direction, so P2 may shrink in the US the way it did in the UK (inference).

### Gaps
- No podcast or interview quotes from operating partners, portfolio CFOs or search-fund CEOs were reachable.
- AFP 2026 vendor-impersonation and ACH-credit BEC percentages not found (paywalled, $295).
- No IOFM survey statistics (paywalled).
- IC3 2025 primary PDF not opened (figures from lens06 secondary sources).
- FinCEN deepfake alert not searched (budget).

---

## Q7. Who else sells a fix, at what price, for which customer size, and how crowded

### Takeaway
**P1** is crowded in software at every size, and is getting crowded in services:
- AI-native ERPs (Rillet, Campfire, DualEntry);
- Intuit Enterprise Suite at $12K-$15K+ a year;
- Fathom and Reach at $280-$950 a month;
- PE- and VC-funded AI accounting roll-ups (Crete with a $500M budget, Modus, Multiplier; Basis sells agents to big firms);
- offshore F&A shops already pitch PE portfolios.

The opening is platforms of 5-30 entities before ERP migration, and search or SBA owners, who want a checked close, not another tool.

**P2** software is enterprise-focused and moderately crowded: Trustpair (500+ enterprise customers), Eftsure (merged with Sis ID; Nacha Preferred Partner), Paymode, Early Warning, Plaid, AppZen, Medius, Coupa+Trustpair. Several bundle $1M guarantees. A done-for-you service layer is thin, but software and banks are absorbing it.

### Cited Findings
**P1 competitor table** (price / target / source)

| Competitor | Price | Target size | Source |
|---|---|---|---|
| Fathom | $53-$720 a month; 10/25/50-entity tiers | Advisors, SMB | lens08 |
| Reach Reporting | $149-$950 a month | Advisors, SMB | lens08 |
| Jirav | "Contact Us" | SMB / mid-market FP&A | lens08 |
| Datarails / Vena | Vendr medians about $33K-$34K a year | Mid-market FP&A | lens08 |
| Intuit Enterprise Suite | Quote only; est. $12K-$15K+ a year multi-entity; ProAdvisor discount up to 60% (one vendor guide, unverified) | Mid-market QuickBooks graduates | [ERP Research](https://erpresearch.com/en-us/intuit-enterprise-suite-pricing); [Fourlane](https://www.fourlane.com/?p=9672) or [Synder](https://synder.com/blog/intuit-enterprise-suite-pros-and-cons/) (summary did not say which) |
| NetSuite OneWorld | About $24K-$30K module + $9K-$12K per entity a year (disputed); up to 250 subsidiaries | Mid-market and up | [Houseblend](https://www.houseblend.io/articles/en/netsuite-oneworld-vs-netsuite-erp-tarifs-fonctionnalites); [send.win](https://blog.send.win/?p=8273) |
| Sage Intacct multi-entity | Add-on about $3K-$10K+ a year; suite $20K-$90K a year | Mid-market | [send.win](https://blog.send.win/?p=8273); [TechVendorIndex](https://techvendorindex.pages.dev/compare/netsuite-vs-sage-intacct/) |
| Rillet | About $20K-$35K a year (third-party) | VC-backed / mid-market | [ERP Research](https://erpresearch.com/en-us/ai-native-erp) |
| DualEntry | Tiers by entity count (3/20/unlimited), quote | SMB / mid-market | [RFP.wiki](https://www.rfp.wiki/accounting-finance/rillet/dualentry) |
| Campfire | Not found | Mid-market | [DualEntry blog](https://www.dualentry.com/blog/campfire-erp-alternatives) |
| Pilot | Core $599-$699 a month; CFO from $1,750; multi-entity custom | Startups | see Q5 |
| Kruze | $600-$850+ a month (2024) | VC-backed C-corps, pre-seed to Series D | see Q5 |
| Escalon | Not public | Startups / SMB | [Escalon](https://escalon.services/new-home) |
| indinero | From $750 a month; lists multi-entity consolidation | SMB | see Q5 |
| Outsourced multi-entity bookkeeping (generic) | $1,500-$4,000+ a month | SMB / lower mid-market | [Ecosire](https://ecosire.com/blog/outsourced-bookkeeping-cost-2026) |
| Personiv, QX, PKF O'Connor Davies | Quote | PE portfolios | see Q5 |

**AI accounting roll-ups and firms**
- Crete Professionals Alliance (Thrive-backed) plans to spend $500M+ over two years buying US accounting firms and equipping them with OpenAI-powered tools. It already has $300M+ revenue across 20+ firms. — [Yahoo Finance](https://finance.yahoo.com/news/thrive-backed-accounting-firm-crete-130200467.html)
- Modus: audit-first AI roll-up, reported $85M combined seed and Series A (April 2026), five acquisitions planned for 2026. — [StartupIntros](https://startupintros.com/news/2026-04-08-modus-seed)
- Multiplier: raised $62.5M and bought 8 firms (2026 overview). — [Jupid](https://jupid.com/blog/who-is-buying-accounting-firms-2026); [TechCrunch, June 2025](https://techcrunch.com/2025/06/18/multiplier-founded-by-ex-stripe-exec-nabs-27-5m-to-fuel-ai-powered-accounting-roll-up)
- Basis: $100M Series B (February 2026); sells agents to accounting firms, including about 30% of the Top 25 (lens09).
- FiscalIQ: private beta of an AI-native ledger with "predictive close" for CPA firms running dozens of client ledgers (vendor, unverified). — [FiscalIQ](https://fiscaliq.pages.dev/)
- No firm was found selling a *multi-entity close for roll-ups* as an AI-plus-human service specifically. The search returned nothing on that angle.

**P2 competitor list**
- **Trustpair:** quote-based, "$$$$$" on G2; ERP Research reports 500+ enterprise customers and lists the company size as Enterprise; Capterra says 150+ large companies use it; 23.5% of G2 reviewers are from firms with 51-1,000 employees; up to $1M liability coverage (enterprise plan); 20+ native P2P connectors; Coupa expanded its partnership on 28 April 2026. — [ERP Research](https://erpresearch.com/erp-add-ons/fraud-risk/trustpair); [Capterra](https://www.capterra.com/p/187396/Trustpair/); [G2](https://www.g2.com/products/trustpair/pricing); [FinTech Global](https://fintech.global/2026/04/28/coupa-expands-trustpair-tie-up-to-fight-vendor-fraud/)
- **Eftsure:** about 460 Australian customer organisations (older blog post); launched in the US in May 2024 with a US-based global CEO (Jon Soldan); merged with France's Sis ID (June 2025); Nacha Preferred Partner (July 2025); price scales with spend and new vendors each month; $1M guarantee. — [Eftsure](https://www.eftsure.com/blog/industry-news/protecting-over-5-billion-eft-payments/); [Newswire, US launch](https://www.newswire.com/news/anti-fraud-platform-launches-in-us-appoints-global-ceo-22333368); [Newswire, acquisition](https://www.newswire.com/news/eftsure-closes-strategic-acquisition-to-form-world-s-largest-payment-22596941); [BusinessWire, Nacha](https://www.businesswire.com/news/home/20250702900778/en/Eftsure-Now-a-Nacha-Preferred-Partner); [Eftsure pricing](https://eftsure.com/pricing)
- **Early Warning** (bank-owned network): Verify Account / Verify Payment, quote. — [Early Warning](https://www.earlywarning.com/protecting-payments)
- **Plaid** Identity Match: per request. — [Plaid](https://plaid.com/docs/account/billing)
- **Paymode** (Bottomline): contact vendor. — [Capterra](https://www.capterra.com/p/234113/Bottomline-Paymode-X/)
- **PaymentWorks:** no published price; G2 reviewers preferred Trustpair. — [G2](https://www.g2.com/compare/paymentworks-vs-trustpair)
- **AppZen / Medius:** no entry price on G2. Medius reviews are 65.3% mid-market; AppZen's are 69.8% enterprise. — [G2](https://www.g2.com/compare/appzen-appzen-vs-medius)
- **Finexio:** mid-market and enterprise payments with fraud prevention; price not found. — [SourceForge](https://www.sourceforge.net/software/compare/Bottomline-Paymode-vs-Finexio)
- **BILL** (built-in, optional confirmation); **Dynamics 365** (workflow); **Gatekeeper** (agent); **Corpay** (guidance and payments) — see Q5.
- Paymentus: **not found**. Ramp built-in bank-change controls: **not confirmed**.

### Inferences
- **P1 crowding: high.** Software is commoditised; services are getting crowded fast and attracting AI capital. The service must be sold as "your monthly group close, mapped, checked and signed by a named reviewer by business day 10", priced per entity, not as dashboards.
- **P2 crowding: moderate-high in software, low in services.** The $1M guarantees set a buyer expectation a small service firm cannot match without insurance. The most realistic role is **implementation and exception-desk partner** for Eftsure or Trustpair at mid-market clients, or a bundle inside a P1-style finance-ops retainer.

### Gaps
- Not found: Fuelfinance; Bench successors; Paymentus; AppZen, Medius and Coupa prices; Ramp features; Eftsure US customer count.

---

## Q8. Will the problem grow or shrink as AI models improve over the next 24 months?

### Takeaway
**P1: the tool gap shrinks; the need for a checked, accountable close holds.** Volume holds too: 13,509 US PE-backed companies, and add-ons are about 75% of buyouts. Expect price pressure as AI-native ERPs and AI accounting roll-ups automate mapping.

**P2: attacks grow; the human share of defence shrinks.** Banks (Nacha 2026), account-ownership networks and verification SaaS automate the clean cases. Voice cloning weakens the callback itself, so the remaining human work moves to exceptions and redesigned verification.

### Cited Findings
- P1, shrink forces:
  - AI-native ERPs with native multi-entity consolidation: Rillet, Campfire, DualEntry — [ERP Research](https://erpresearch.com/en-us/ai-native-erp);
  - Intuit Enterprise Suite automated intercompany eliminations — [TechRepublic](https://www.techrepublic.com/article/intuit-enterprise-suite-reviews/);
  - ScaleXP "Full AI Close" — [ScaleXP](https://www.scalexp.com/integrations/quickbooks/);
  - AI-equipped accounting roll-ups: Crete $500M — [Yahoo Finance](https://finance.yahoo.com/news/thrive-backed-accounting-firm-crete-130200467.html).
- P1, grow or hold forces:
  - 13,509 US PE-backed companies at end-Q2 2026 (PitchBook via secondary sources), up from 13,143 at Q4 2025; 33,575 global PE-owned companies awaiting exit — [Windsor Drake](https://windsordrake.com/market-intelligence/reports/files/the-sponsor-exit-2026-report-report.pdf); [Penn Mutual AM, 22 Oct 2026](https://www.pennmutualam.com/market-insights/blogs/chart-of-the-week/2026-10-22-private-equitys-unsold-backlog-keeps-growing-as-exit-routes-narrow);
  - the data clean-up is the residual pain — [WorkWise](https://workwisesolutions.org/guides/best-ai-roll-up-consolidation-software.html).
- P2, grow forces:
  - 71% of $500M+ US firms report rising AI-powered attempts (vendor claim) — [Trustpair](https://www.businesswire.com/news/home/20260126508647/en/AI-Fraud-Outpaces-Human-Defenses-as-71-of-U.S.-Companies-Report-Rise-in-Attacks-Trustpair-Report-Finds);
  - AFP 2026 adds deepfake impersonation of vendors — [AFP](https://www.financialprofessionals.org/publications-data-tools/reports/survey-research-economic-data/Details/payments-fraud);
  - IC3 AI section, $893M (lens06);
  - AU payment redirection up 9.3% — [Eftsure](https://www.eftsure.com/blog/industry-news/$167m-lost-in-2025-why-bec-scams-keep-costing-australians/).
- P2, shrink forces:
  - Nacha 2026 monitoring duties on originators and receiving banks — [Nacha](https://www.nacha.org/rules/risk-management-topics-fraud-monitoring-phase-2);
  - account-ownership APIs — [Early Warning](https://www.earlywarning.com/sites/default/files/2024-02/Verify-account-product-brief-v3-20240202.pdf); [Plaid](https://plaid.com/docs/account/billing);
  - Coupa+Trustpair bundling — [FinTech Global](https://fintech.global/2026/04/28/coupa-expands-trustpair-tie-up-to-fight-vendor-fraud/);
  - UK invoice and mandate fraud fell to multi-year lows once banks were made to act — [Payment Expert](https://paymentexpert.com/2026/06/15/uk-finance-fraud-report-2026/).

### Inferences
- P1: better models cut the provider's cost per entity (mapping, anomaly flags, commentary drafts). That suits a lean offshore AI-plus-human team, but competitors get the same gain, so expect **falling prices per entity**. What stays valuable is accountability (a named reviewer), sponsor-format packs and chasing the sites.
- P2: as voice and video cloning improve, a callback alone stops being proof. Verification must combine the known number, an account-ownership API match, a crowdsourced bank-detail history (Eftsure-style) and a second approver. Most of that is software. The human role narrows to judging exceptions and keeping evidence for insurers.

### Gaps
- No neutral forecast of how fast AI-native ERPs will take the lower-mid-market roll-up segment.
- No data on deepfake-voice attacks defeating callbacks specifically.

---

## Q9. How to reach these buyers

### Takeaway
**P1:**
- ACG: 58-61 chapters, 13,000-14,500 members, individual membership $475 in 2026, DealMAX in April;
- SearchFunder (over 80% of searchers keep an account; it has a bookkeeper-introductions thread);
- SBA lenders and search-fund investors;
- Intuit ProAdvisor / Enterprise Suite, Sage Intacct and Fathom/Reach partner ecosystems.

**P2:**
- AFP, IOFM and AP conferences;
- Nacha Preferred Partner programme;
- commercial crime insurers and brokers (callback conditions);
- Coupa, BILL and NetSuite ecosystems;
- reseller or partner terms with Eftsure or Trustpair;
- UK: ICAEW; AU: CPA Australia.

### Cited Findings
**P1**
- ACG pages give conflicting counts: 58 chapters and 14,500 members on some pages; 59 chapters and 13,000 members on others; one says 61 chapters. 2026 individual membership is $475. DealMAX 2026 was in Las Vegas, 27-29 April. — [ACG Join or Renew](https://www.acg.org/101/membership-tools/join-or-renew); [ACG](https://www.acg.org/node/1396)
- Chapter advisory-board announcements list named dealmakers, which can serve as prospect lists. — [ACG St. Louis 2026 Chapter Advisory Board](https://www.acg.org/node/153810)
- SearchFunder: "over 80% of people involved in search funds" keep an account; cached pages show plans at $29 and $79 a month (conflict). A bookkeepers' introduction thread is a direct service channel. — [SearchFunder](https://searchfunder.com/post/-200) (the summary did not say which page held the 80% claim); [SearchFunder bookkeepers thread](https://searchfunder.com/post/bookkeepers-please-introduce-yourself-here)
- Stanford GSB 2026 Search Fund Study (lens08). — [Stanford GSB](https://www.gsb.stanford.edu/faculty-research/case-studies/2026-search-fund-study-selected-observations)
- Intuit ProAdvisor programme: accountants can get up to 60% off Enterprise Suite list price for qualifying clients (single vendor guide; verify). — [Fourlane](https://www.fourlane.com/?p=9672) / [Synder](https://synder.com/blog/intuit-enterprise-suite-pros-and-cons/) (summary did not say which)
- PE firms push portfolio companies toward SOC compliance, which suggests SOC-ready providers win PE referrals. — [Barnes Dennig](https://www.barnesdennig.com/soc-reporting-for-private-equity-companies/)
- SBA lenders (Live Oak, Huntington, First Internet) and CPA Trendlines and Accounting Today for CPA roll-ups (lens08).

**P2**
- AFP (survey publisher; report $295 for non-members). — [AFP](https://www.financialprofessionals.org/publications-data-tools/reports/survey-research-economic-data/Details/payments-fraud)
- IOFM Ask the Expert (AP practitioners; paywalled). — [IOFM](https://www.iofm.com/ask-the-expert/best-practices-for-changing-vendor-banking-information)
- AP conference circuit: the "KPIs Every AP Should Track" deck, November 2025, DivCom Events. — [deck](https://divcomevents2-static.s3.amazonaws.com/uploads/sites/3/2025/10/THURS-105-Milano-VI-KPIs-Every-AP-Should-Track-Jamie-Umpleby.pdf)
- Nacha Preferred Partner programme (Eftsure joined July 2025). — [BusinessWire](https://www.businesswire.com/news/home/20250702900778/en/Eftsure-Now-a-Nacha-Preferred-Partner)
- Banks publish Nacha guides for corporate clients, so treasury teams are a referral path. — [U.S. Bank PDF](https://www.usbank.com/content/dam/usbank/en/documents/pdfs/corporate-and-commercial-banking/Nacha-USBank-fraud-monitoring-rule-changes.pdf); [Bottomline](https://www.bottomline.com/learning-center/2026-nacha-compliance-rules-risks-and-how-prepare); [CorporateOne](https://www.corporateone.coop/resources/newsletter/february-2026-nacha-rules)
- Insurers and brokers: Amwins advises narrowing authentication provisions; an excess carrier (Intact) sits above primary policies that carry callback conditions. — [Amwins](https://www.amwins.com/resources-and-insights/market-insights/article/how-cyber-and-crime-insurance-policies-respond-to-social-engineering); [Intact FAQ (Apr 2025)](https://portal.intactinsurance.com/system/files/mydocuments/Update-Excess%20SEF%20External%20FAQ_EN_04.09.25.pdf)
- Coupa ecosystem (Trustpair partnership). — [FinTech Futures](https://www.fintechfutures.com/press-releases/trustpair-and-coupa-expand-partnership-to-help-enterprises-prevent-ai-driven-vendor-payment-fraud)

### Inferences
- The best P1 channel is probably **ACG chapter events plus operating-partner introductions**, combined with **QuickBooks/Intuit Enterprise Suite partner status**, because platforms graduating from QuickBooks are the ideal buyer.
- The best P2 channel is probably **crime-insurance brokers**. Their clients must prove callback controls to keep cover, so a recorded, out-of-band verification log is something the broker can recommend.

### Gaps
- Fathom and Reach partner programme terms not checked; no Xero or Sage Intacct partner-directory counts.
- AFP and IOFM membership numbers and event dates not found; no newsletter subscriber counts (CFO Dive, CFO Brew).

---

## Q10. Roughly how many US companies have this problem

### Takeaway
**P1:** 13,509 US PE-backed companies. My estimate is **about 1,700-2,700 platforms with 5+ entities on fragmented ledgers**, plus about 6,100 SBA acquisitions a year, about 860 search funds cumulative and 1,200-1,400 independent sponsors (lens08).

**P2:** About **107,700 US firms with 100+ employees** (2021 SUSB via a secondary chart). Applying AFP's 76% gives about 82,000 firms with attempted or actual fraud a year (estimate). IC3 logged 24,768 BEC complaints in 2025.

### Cited Findings
- 13,509 US PE-backed companies at end-Q2 2026 (PitchBook, via secondary sources); 13,143 at Q4 2025 (secondary, called a "record" by a non-PitchBook site). — [Windsor Drake](https://windsordrake.com/market-intelligence/reports/files/the-sponsor-exit-2026-report-report.pdf); [Penn Mutual AM](https://www.pennmutualam.com/market-insights/blogs/chart-of-the-week/2026-10-22-private-equitys-unsold-backlog-keeps-growing-as-exit-routes-narrow)
- About 5,500 US add-ons a year (lens08 estimate from PitchBook's 74.9% add-on share).
- Census SUSB 2021 (via an Apollo Academy chart, secondary): **88,023 firms with 100-499 employees; 19,688 with 500+.** — [Apollo Academy chart](https://apolloacademy.com/wp-content/uploads/2024/07/070724-Chart.pdf). 2022 figures not found.
- IC3 2025: 24,768 BEC complaints (lens06).
- AU: 2,228 small-business scam reports in 2025. — [Canberra Times](https://www.canberratimes.com.au/story/9218144/beware-the-urgent-email-at-the-end-of-the-working-day/)

### Inferences (estimates)
- **P1 platforms:** assume 25-40% of 13,509 PE-backed companies are buy-and-build platforms, giving 3,400-5,400. Assume about half are lower-middle-market platforms still on mixed ledgers: **about 1,700-2,700**. Both percentages are my assumptions.
- **P1 first-time owners:** about 6,100 SBA change-of-ownership deals a year (lens08). The Main Street tail (median price $350K) cannot pay. Assume 20-30% are above about $3M revenue: **about 1,200-1,800 new buyers a year**.
- **P2:** 107,711 firms with 100+ employees × 76% = **about 82,000** with attempted or actual fraud each year. AFP respondents skew large, so this probably overstates. The serviceable slice is firms of 100-999 employees without Trustpair or Eftsure. SUSB 500-999 band not found.

### Gaps
- No PitchBook count of platforms vs add-ons in the active inventory.
- SUSB 2022 primary table not reached.
- No count of US firms already using vendor-verification software.

---

## Q11. The strongest argument against each opportunity

### Takeaway
**P1:** It is turning into a crowded, capital-heavy race. AI accounting roll-ups (Crete $500M; Modus; Multiplier; Basis-equipped Top 25 firms), AI-native ERPs and offshore F&A shops all target the same platforms. Each platform eventually standardises on one ERP and hires a $160K controller. Sponsors may want a US CPA firm's name on the numbers.

**P2:**
- Liability and real-time demands land on the service provider.
- Software vendors give $1M guarantees, and banks now carry Nacha monitoring duties.
- The expected monthly value per mid-market firm is only about $0.8K-$5.2K (estimate), so a stand-alone retainer is hard to justify.

### Cited Findings
- Crete $500M AI roll-up; Modus $85M; Multiplier $62.5M. — [Yahoo Finance](https://finance.yahoo.com/news/thrive-backed-accounting-firm-crete-130200467.html); [StartupIntros](https://startupintros.com/news/2026-04-08-modus-seed); [Jupid](https://jupid.com/blog/who-is-buying-accounting-firms-2026)
- Offshore F&A for PE portfolios already exists. — [Personiv](https://www.personiv.com/private-equity)
- Eftsure $1M guarantee; Trustpair up to $1M coverage. — [Eftsure pricing](https://eftsure.com/pricing); [ERP Research](https://erpresearch.com/erp-add-ons/fraud-risk/trustpair)
- BEC cases often put liability on "payors that fail to verify suspicious payment instructions, even if the attack originated with a compromise of the payee's computer system." — [Arnall Golden Gregory](https://www.agg.com/news-insights/publications/business-email-compromise-fraud-should-the-party-best-positioned-to-avoid-the-fraud-bear-the-loss/)

### Inferences
- P1: the counter-argument is that the 5-30-entity, QuickBooks-based tier is below the AI roll-ups' sweet spot (they buy CPA firms that serve many SMBs) and below NetSuite economics. A focused, cheaper, per-entity service can live there. It is still a price-competitive services business.
- P2: an AI-plus-human verifier that misses a fraud becomes the "best positioned" party in a dispute. Without insurance and tight contract caps, one $1.5M Baltimore-type loss could end a small firm.

### Gaps
- No sourced data on how often sponsors require Big-4 or US CPA involvement in monthly packs.

---

## Q12. Delivery constraints for an offshore (non-US) team

### Takeaway
**P1 suits offshore delivery well.** It needs accountant-user access to QuickBooks/Xero/ERP and read-only bank feeds. The deadline is monthly (business day 10-20), so the work is asynchronous. No legal SOC 2 requirement was found, but PE buyers increasingly expect SOC 2 Type II or ISO 27001 plus MFA, VPN and least-privilege access.

**P2 fits offshore delivery poorly unless redesigned.**
- Callbacks must reach US vendors in US business hours before payment runs. From Pakistan or India that means night shifts: US Eastern 9am-5pm is about 7pm-3am PKT or 6:30pm-2:30am IST in winter.
- Insurers' callback conditions dictate the method, and some require recorded out-of-band verification.
- Loss liability tends to fall on whoever was best positioned to stop the payment.
- Contracts must cap liability, and the client must keep the final release decision.

### Cited Findings
- No regulation requires SOC 2 for outsourced accounting. Vendor guides recommend SOC 2 Type II and ISO 27001 as selection filters, review of audit scope and tested controls, and contractual evidence of compliance. They also recommend end-to-end encryption, MFA, VPN, narrow permissions and a tested incident plan. — [QX Accounting](https://qxaccounting.com/usa/blog/cybersecurity-best-practices-when-outsourcing-accounting/)
- PE firms are "emerging as powerful drivers, pushing their portfolio companies toward SOC compliance" (broker-style article). — [Barnes Dennig](https://www.barnesdennig.com/soc-reporting-for-private-equity-companies/)
- BEC liability:
  - courts mostly apply the UCC "imposter rule" by analogy: loss falls on whoever could most cheaply have prevented the fraud;
  - outcomes vary on similar facts; *Beau Townsend Ford v. Don Hinds Ford* (6th Cir. 2018, older) left "best position" to the factfinder;
  - at least one court rejected the imposter-rule analogy (*Peeples v. Carolina Container*; outcome cut off in the summary);
  - BEC cases are "often fact-intensive and generally not decided before trial" (Foley Hoag, April 2026);
  - sources: [Arnall Golden Gregory](https://www.agg.com/news-insights/publications/business-email-compromise-fraud-should-the-party-best-positioned-to-avoid-the-fraud-bear-the-loss/); [Foley Hoag](https://www.foleyhoag.com/news-and-insights/blogs/security-privacy-and-the-law/2026/april/business-email-compromises-current-legal-trends-and-key-strategies/); [JD Supra](https://www.jdsupra.com/legalnews/business-email-compromises-current-3417161/).
- Insurance:
  - callback conditions vary by carrier: any underwriter-approved method, a callback to a preset number, or **recorded out-of-band verification** — [Bank Director](https://www.bankdirector.com/?p=5427);
  - some policies require verification through a different channel from the request — [Insurance Journal (2023)](https://www.insurancejournal.com/news/national/2023/03/02/710068.htm);
  - courts have mostly held that computer-fraud coverage does not apply when a human makes the transfer decision — [Ward and Smith](https://www.wardandsmith.com/article/social-engineering-fraud-and-your-crime-policy-why-your-insurer-may-deny-the-claim-and-what-you-can-do-about-it).
- Nacha 2026 puts monitoring duties on ODFIs **and originating third parties**. A service provider that originates payments for clients would be in scope; one that only verifies would not. Inference from rule scope. — [Nacha](https://www.nacha.org/rules/risk-management-topics-fraud-monitoring-phase-2)

### Inferences
- **P1 delivery design:**
  - offshore team works US-overnight on the close;
  - a US-hours lead (or overlapping shift) chases site managers and joins the sponsor review call;
  - accountant-user access only; no bank-payment permissions;
  - SOC 2 Type II within 12-18 months of launch, to pass PE vendor reviews;
  - an engagement letter that limits liability to fees and states the client signs the financials.
- **P2 delivery design (if pursued):**
  - never hold payment-release rights; recommend "release" or "hold", and the client executes;
  - cap liability at fees, and carry errors-and-omissions or crime insurance;
  - run a US-hours callback shift, or use a US-number dialler with recorded calls;
  - align the method with each client's crime-policy callback wording.
  - Caller ID from overseas numbers may itself look like fraud to US vendors (inference).
- Without that design, P2 offshore delivery fails the constraint test.

### Gaps
- Not researched: SOC 2 subservice-organisation carve-outs for offshore staff; US state rules on non-CPA firms doing bookkeeping (none known to apply to non-attest work [prior knowledge, not verified, no URL]); GLBA or data-privacy duties for vendor bank data; professional-liability insurance costs for an offshore provider.

---

## Q13. Where to find 15 named prospects within 14 days

### Takeaway
**P1:**
- PE platform add-on press releases and deal trackers (CPA Trendlines, Capstone residential services, OPTIS insurance agency, PitchBook via Becker's);
- ACG chapter advisory-board and sponsor pages;
- multi-entity controller job posts (a live signal);
- SearchFunder "recently acquired" posts.

Target title: **platform CFO / VP Finance / holding-company controller**; for search funds, the **CEO**.

**P2:**
- companies posting AP vendor-master and fraud roles;
- public-sector AP audit reports (municipal victims publish them);
- Trustpair and Eftsure testimonials and the Coupa ecosystem.

Target title: **Controller or AP Manager**, with the **CFO** as approver.

### Cited Findings
**P1: named platforms with heavy add-on pace**
- From lens08: Apex Service Partners (about 60 add-ons in 2025), Southern Veterinary Partners (139 since 2021), Specialized Dental Partners (55), Ivy Rehab (24), Vertex Service Partners (30 in 3 years), BroadStreet (69 agency deals in 2025), Evergreen Services Group (23 MSP deals 2023-25).
- Lower-middle-market sponsors using Chronograph: Summit Park, LongWater, FPE Capital. Their portfolio platforms are prospects (lens08).
- Live hiring signal: the Clayton, MO lower-middle-market PE firm with about a dozen opcos hiring a holding-company Controller (14 Jan 2026). The firm is not named in the snippet. — [PCRecruiter](https://host.pcrecruiter.net/pcrbin/jobboard/job/Controller/b/LAD7CGTS6ZMHSILH2XDSJU6XWBWSXRIDZTODGWAFRETOKJZZM7MA2LMN3SG5LUM3MWJVATBIU4)
- Robert Half "Controller - Private Equity" multi-entity search (Fort Lauderdale). — [Career.com](https://www.career.com/job/robert-half/financial-controller/j202512051542082879100)
- Lists:
  - ACG St. Louis 2026 Chapter Advisory Board — [ACG](https://www.acg.org/node/153810);
  - CPA Trendlines PE deal tracker (527 deals) and Capstone's October 2026 residential services report (lens08);
  - BTerrell Sage Intacct veterinary page (lens08).

**P2: named organisations showing the pain**
- City of Baltimore ($1.52M loss, 2025). — [Security Affairs](https://securityaffairs.com/181772/cyber-crime/fraudster-stole-over-1-5-million-from-city-of-baltimore.html)
- City of Minneapolis (AP vendor-change audit response). — [Minneapolis](https://www2.minneapolismn.gov/media/content-assets/www2-documents/departments/wcms1p-103480.pdf)
- Tarrant County, TX (FY2022 audit: "Accounts Payable Managers Vendor Master Data Change Review", 2022). — [Tarrant County](https://access.tarrantcounty.com/content/dam/main/auditor/AuditReports/audits-issued-fy2022/32._Auditors_Report_-_FY2022_Accounts_Payable_Managers_Vendor_Master_Data_Change_Review_CO138406.pdf)
- icare NSW (Australia; partnered with Eftsure). — [icare](https://icare.nsw.gov.au/news-and-stories/icare-strengthens-payment-security-for-service-providers)
- Employers posting vendor-master and fraud roles: Volkswagen Group Canada, West Fraser, Discount Tire, Fanatics, Cargill (APAC). — see Q6 URLs; [Cargill](https://careers.cargill.com/ko/직무/saraburi/apac-master-data-analyst/35670/96769199408)

### Inferences
- The named P1 platforms above (Apex, SVP and others) are probably **too large** and already on an ERP with in-house teams. Better P1 prospects are platforms with 5-30 sites announced in 2025-2026 press releases ("platform investment" + "first add-on"), found through ACG chapter sponsor lists and Capstone or OPTIS deal tables. A 14-day sprint could plausibly assemble 15 names from 2-3 sector deal trackers plus ACG sponsor pages (inference, not tested).
- P2's public-sector names are reachable but slow (procurement). The mid-market private names would come from Coupa or BILL user communities and AP conference speaker lists. The large-enterprise employers above already staff the function and are poor targets.

### Gaps
- No Trustpair or Eftsure **US** customer case-study names found. No ACG sponsor lists or partner-directory entries were opened.
- A 15-name list was not assembled; only sources and examples are given.

---

## Q14. Pricing shapes buyers already accept

### Takeaway
**P1:**
- fixed monthly retainers ($450-$4,000+ for bookkeeping; $6K-$25K for fractional CFO);
- monthly-expense bands (Pilot, Kruze);
- per-entity or per-connection software tiers (Fathom, Reach, DualEntry, NetSuite per subsidiary);
- per-transaction ($0.50-$2.00) and one-time clean-up ($500-$5,000).

A **base + per entity per month** service fits buyer habits.

**P2:**
- Eftsure prices by **annual spend + new vendors onboarded per month**;
- Trustpair by **platform access + number of vendor evaluations a year**;
- Plaid and Early Warning **per request**;
- guarantees bundled.

A **monthly retainer with N verifications included, plus per-verification overage** fits.

### Cited Findings
- P1, services:
  - fixed monthly multi-entity $1,500-$4,000+; per-transaction $0.50-$2.00 with a $200-$300 minimum; clean-up $500-$5,000 — [Ecosire](https://ecosire.com/blog/outsourced-bookkeeping-cost-2026);
  - indinero fixed price month-to-month from $750; Kruze by monthly expense band — [Pilot blog](https://pilot.com/blog/escalon-services-alternatives);
  - fractional CFO $6K-$25K a month; hourly $200-$600 (lens08).
- P1, software:
  - Fathom by entity count (10/25/50); Reach by connections (1/10/25/50) (lens08);
  - DualEntry tiers by entity count (3/20/unlimited) — [RFP.wiki](https://www.rfp.wiki/accounting-finance/rillet/dualentry);
  - NetSuite per subsidiary (about $9K-$12K a year each, disputed; 5-10% escalator) — [Houseblend](https://www.houseblend.io/articles/en/netsuite-oneworld-vs-netsuite-erp-tarifs-fonctionnalites); [Oracle Licensing Experts](https://oraclelicensingexperts.com/blog/netsuite-oneworld-licensing/);
  - Intuit Enterprise Suite by number of companies — [ERP Research](https://erpresearch.com/en-us/intuit-enterprise-suite-pricing);
  - Rillet by complexity, not seats — [ERP Research](https://erpresearch.com/en-us/ai-native-erp).
- P2:
  - Eftsure: spend + new vendors a month, $1M guarantee included — [Eftsure pricing](https://eftsure.com/pricing);
  - Trustpair: platform access + fixed vendor evaluations a year — [G2](https://www.g2.com/products/trustpair/pricing);
  - Plaid Identity Match: per request, flat fee — [Plaid](https://plaid.com/docs/account/billing); about $0.10-$0.60 per call (Vendr, unverified) — [Vendr](https://www.vendr.com/marketplace/plaid);
  - Early Warning: quote via account managers — [Early Warning](https://www.earlywarning.com/sites/default/files/2024-02/Verify-account-product-brief-v3-20240202.pdf).

### Inferences (proposed shapes, not tested with buyers)
- **P1 roll-up:** about $1,500 a month base (group consolidation, pack, commentary) + $200-$450 per entity a month + $1,500-$4,000 one-time per new add-on.
  - 14 entities ≈ $4.3K-$7.8K a month, below the $5.8K-$16.9K staff-time estimate and the $19K-a-month controller.
  - 30 entities ≈ $7.5K-$15K a month.
- **P1 first-time owner:** $1,200-$2,500 a month for accrual close + investor pack, between the $450 bookkeeping offers and the $6K fractional CFO.
- **P2:** $750-$2,500 a month for up to 20-60 verified changes or flagged invoices, then $25-$50 per extra verification. This sits inside the $0.8K-$5.2K monthly value estimate. A loss guarantee is **not** advisable without insurance, and it raises a Shariah question (below).

### Gaps
- No public per-entity price for any outsourced multi-entity close service. No public per-verification price for Trustpair or Eftsure.

---

### Halal / Shariah flags (questions only; no rulings given)
- **P1:**
  - Most roll-up platforms and SBA or search-fund buyers carry interest-bearing acquisition debt and seller notes. Bookkeeping for the operating company is one question.
  - Preparing **lender covenant compliance certificates and borrowing-base certificates** is a closer question: it exists to service interest-bearing loans. Consider scoping it out, or flagging it to the end client.
  - Avoid platforms centred on alcohol (liquor retail, bars), gambling or adult content.
  - Insurance-agency roll-ups raise the conventional-insurance question (lens08).
- **P2:**
  - Fraud prevention for operating companies looks low-concern.
  - Possible questions: (a) offering an **Eftsure-style loss guarantee**, which works like insurance; (b) referral or reseller deals with conventional banks or crime insurers; (c) client mix: avoid interest-based lenders, casinos and alcohol-centred businesses.
  - Deepfake **detection** is in scope; deepfake creation is not.
