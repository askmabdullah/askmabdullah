# Lens 02: Money Leaks (where revenue quietly leaks out of businesses every week)

Research date: 27 October 2026. Geography: US first, then UK/Australia. Pricing in USD unless stated.

**Method and access caveats (read first).**
- Evidence below comes from web search result summaries gathered in this session. Every attempt to open a full page failed: WebFetch returned DNS errors (ENOTFOUND) for every domain tried (experianplc.com, fiercehealthcare.com, 8vc.com, quickbooks.intuit.com, techtarget.com, spscommerce.com, clio.com, withum.com, pages.dev). Reddit was blocked outright ("unable to fetch from www.reddit.com"). Direct curl was refused by the egress proxy (403). The shared web search budget (200 searches per turn across all agents) ran out after about 20 searches by this researcher.
- So numbers come from search snippets and could not be checked against the full source. Where a snippet did not clearly tie a number to one URL, I say so or move it to Gaps.
- **No real owner or operator quotes were collected.** Reddit was blocked, and no forum, review or job post page could be opened. No quotes are invented here. The quoted lines below come from vendors, consultancies or industry bodies and are labelled that way.
- "Vendor claim" marks numbers from companies that sell a fix. "Estimate" marks my own math, with the working shown. "Inference" marks my reasoning, which is not sourced.
- Prior-knowledge items that I could not re-check this session are labelled "(prior knowledge, not re-verified)".

---

## Q1. Which revenue leaks are largest and most measurable in 2025-2026?

### Takeaway
The leaks with the best data and the clearest weekly cadence are: (1) healthcare claim denials and underpayments, which have the strongest independent data; (2) retailer deductions and compliance fines against CPG brands, where the data is mostly vendor-sourced but the cadence is weekly and the economics favour contingency pricing; (3) freight, LTL and parcel invoice errors; (4) unbilled T&M and field work; and (5) slow B2B receivables. Supplier rebates, duty drawback and Amazon FBA reimbursements are real leaks but are less frequent, more regulated, or already handled by cheap tools.

### Cited Findings

**Healthcare denials (strongest independent data)**
- 41% of providers report denial rates of 10% or higher, up from 30% in 2022 and 38% in 2024. Experian Health State of Claims 2025: 250 healthcare finance/billing decision-makers, fielded 23 June to 3 July 2025 — [Business Wire, 22 Sep 2025](https://www.businesswire.com/news/home/20250922969006/en/Experian-Health%E2%80%99s-3rd-Annual-State-of-Claims-Survey-Finds-Denials-Still-on-the-Rise-Amid-Escalating-Challenges); [Managed Healthcare Executive, 22 Sep 2025](https://www.managedhealthcareexecutive.com/view/claim-denial-rates-increase-for-third-consecutive-year-survey-shows); trend figures (30%, 38%) per [TechTarget](https://www.techtarget.com/revcyclemanagement/news/366631271/Claim-denial-rates-arent-improving-but-AI-could-help). Experian sells denial tools, but the survey was run by a third-party panel.
- Top denial causes (2025): missing or inaccurate data 50% (up from 46% in 2024), authorizations 35%, patient registration errors 32%. 54% say claim errors are rising and 43% say they are understaffed. 67% think AI could help, but only 14% use it — [Business Wire](https://www.businesswire.com/news/home/20250922969006/en/Experian-Health%E2%80%99s-3rd-Annual-State-of-Claims-Survey-Finds-Denials-Still-on-the-Rise-Amid-Escalating-Challenges)
- Hospitals spend about $19.7B a year fighting denials. About $10.6B of that is "wasted arguing over claims that should have been paid at the time of submission", and 54.3% of denials were later overturned. This is a Premier survey of 516 hospitals covering 2022 claims, published March 2024 (older) — [Fierce Healthcare](https://www.fiercehealthcare.com/providers/providers-wasted-106b-2022-overturning-claims-denials-survey-finds); [AHA Market Scan, Apr 2024](https://www.aha.org/aha-center-health-innovation-market-scan/2024-04-02-payer-denial-tactics-how-confront-20-billion-problem). Premier sells revenue-cycle services.
- A later Premier page says claims adjudication costs providers "more than $25.7 billion", 23% above the earlier $19.7B, with about 70% of denials overturned. The page's year could not be confirmed (likely the 2025 or 2026 cycle) — [Premier newsroom](https://premierinc.com/newsroom/80-premier-members-call-for-medicare-advantage-changes-to-address-payment-denials-and-delays)
- Final (not initial) denial rates are much lower: the median rose from 2.5% (2024) to 2.7% (2025). This is vendor data from Kodiak, reported by [Fierce Healthcare](https://www.fiercehealthcare.com/finance/payer-audits-denial-amounts-rise-again-2025-vendor-data-show)
- MGMA's 2023 DataDive put the first-submission denial rate for single-specialty groups at 8%, the same as 2019. An MGMA Stat poll (5 March 2024) found 60% of medical group leaders saw denials rise year on year and only 11% saw a fall — [MGMA](https://mgma.com/mgma-stat/strategic-improvements-in-your-rcm-to-reduce-your-practices-claim-denials). Older than 2025.
- Commercial underpayments are said to cost providers 1% to 11% of net revenue a year, growing about 14% a year from 2019 to 2023. Vendor claim — [HelpSquad](https://helpsquad.com/blog/beyond-denials-how-outsourced-payer-underpayment-recovery-finds-revenue-your-denial-reports-miss/)
- Headline only (body not read): "AI is making claim denials worse for physician practices", 19 June 2026 — [Healthcare Guys](https://healthcareguys.com/2026/06/19/ai-is-making-claim-denials-worse-for-physician-practices-heres-why/)

**CPG retailer deductions and compliance fines (mostly vendor data)**
- Vendor estimates of deductions as a share of a supplier's gross revenue: "1% to 7%", "2–5%" and "up to 3%". One outlier claims up to 30%. These figures appear across [Doss](https://www.doss.com/blog/how-to-automate-deduction-management-walmart-target-amazon-and-kroger), [Endless Commerce](https://endlesscommerce.com/playbook/deduction-management-for-cpg-brands) and [Salesbox](https://salesbox.ai/blog/top-deduction-management-platforms-2026). All are vendor claims, and the snippet did not tie each number to one page.
- "The average Walmart supplier loses 5.8% of their invoices to deductions." Vendor claim — [SupplyPike](https://supplypike.com/walmart). SupplyPike now publishes under SPS Commerce.
- Share of deductions that are invalid or disputable:
  - 10–25% per industry experts; Promomash's own review of more than $100M of deductions found 17% invalid and disputable. Vendor claim — [Promomash ebook](https://go.promomash.com/hubfs/Ebooks/How%20to%20manage%20deductions%20-%20Ebook%20-%20Promomash%20-%20V2%20(1).pdf)
  - "Up to 20%" disputable, per Inmar Intelligence's John Helmle — [PYMNTS](https://www.pymnts.com/?p=1229791)
  - 40–60%, citing the Finortal CPG AR Benchmark (not verified) — [Stealth Agents research page](https://stealthagents.com/research/ai-deduction-management-automation-statistics-2026)
- Recovery rates fall from 80% to 20% as disputes approach the 90-day industry average. Kraft Heinz recovers $124M a year in invalid deductions, a 3.1% net recovery rate against an industry average of 2%. Vendor claim — [HighRadius case study](https://www.highradius.com/resources/case-studies/kraft-heinz-dms/)
- Walmart OTIF fine: 3% of the value of goods delivered late, early, short or mispackaged — [SPS Commerce/SupplyPike](https://www.spscommerce.com/community/articles/how-to-dispute-walmart-otif-chargebacks). Kroger charged $500 a day for deliveries outside a two-day window — [Grocery Dive](https://www.grocerydive.com/news/grocery--walmart-and-kroger-fine-suppliers-for-late-or-incomplete-deliveries/534461/) (older, around 2018). Walmart deductions can only be disputed within 2 years — [SPS Commerce](https://www.spscommerce.com/community/articles/how-to-dispute-a-walmart-deduction)
- Opinion from Fractal (consultancy): most deductions are written off "not because they are valid, but because they are not worth the cost to investigate" — [Fractal](https://fractal.ai/article/deductions-margin-leakage-cpg/)

**Freight, LTL and parcel invoice errors (vendor data, wide range)**
- Share of freight invoices with errors:
  - 3–6%, with accessorials the highest-error category — [Stealth Agents](https://stealthagents.com/research/ai-freight-audit-automation)
  - 5–10% of freight and parcel invoices, a Tompkins Ventures benchmark — [GingerControl](https://gingercontrol.com/blog/freight-invoice-audit-guide)
  - 5–6% — [Beancount, Sep 2026](https://beancount.io/blog/2026/09/21/freight-invoice-audit-recover-overcharges-duplicate-charges-guide)
  - 20–25% — [ParcelPath](https://parcelpath.com/freight-ltl/freight-freight-class-and-documentation/freight-audit/)
  - 40–60% for container-related bills — [BlueCargo](https://www.bluecargo.io/post/why-are-there-so-many-errors-in-container-related-invoices)
  - All are vendor or vendor-adjacent claims.
- Recovery of 2–4% of total freight spend through systematic audit — [ParcelPath](https://parcelpath.com/freight-ltl/freight-freight-class-and-documentation/freight-audit/); 3–7% — [TransImpact](https://transimpact.com/solutions/freight-audit-pay). Vendor claims.
- One year after the August 2025 density-based NMFC change, LTL executives (mid-August 2026) still see shipper confusion. That confusion drives reclass charges and disputes — [CarrierAtlas](https://carrieratlas.com/news/ltl-carriers-say-shippers-still-dont-get-density-based-nmfc-a-year-in)

**Unbilled T&M and field work**
- 15–25% of T&M labor is "never invoiced — not late, never". In the vendor's own sample, only 46% of jobs were fully invoiced, though some uninvoiced jobs are legitimate (warranty work, service-agreement visits). Vendor claim — [Level](https://level-4f4.pages.dev/blog/unbilled-work-jobs-never-invoiced/). Rhumbix cites the same 15–25% for manual tracking, attributing it to ServiceTitan and Sera research — [Rhumbix](https://www.rhumbix.com/blog/how-much-money-are-you-losing-on-unbilled-tm-work-industry-benchmark-report). The Rhumbix page also carries a banner saying Autodesk signed a deal to acquire Rhumbix.
- Lower estimates:
  - Up to 5% of annual revenue, attributed to PTC/ServiceMax research — [FieldPromax](https://www.fieldpromax.com/blog/improve-work-order-management/)
  - 3–5% of revenue in unbilled work orders — [Oxmaint](https://oxmaint.com/industries/facility-management/sap-sales-distribution-for-facility-service-operations)
  - 5–15% — [Fieldproxy](https://www.fieldproxy.ai/blog/how-to-stop-losing-money-on-unbilled-service-calls-in-cleaning-busines-d1-20)
  - 5–9% — [FieldCamp](https://fieldcamp.ai/blog/service-business-profitability/)
  - All vendor claims.
- Law firms (Clio Legal Trends, all-firm averages): utilization 38% (about 3.0 billable hours captured in an 8-hour day), realization 88% (2.6 hours invoiced), collection 93% (2.4 hours collected) — [Clio benchmarks](https://clio.com/resources/legal-trends/benchmarks/). Mid-size firms: 49% / 86% / 93%, with total lockup of 64 days (28 days realization, 25 days collection) — [Clio Mid-Size Report 2026](https://www.clio.com/wp-content/uploads/2026/02/202603-Legal-Trends-Report-for-Mid-Size-Law-Firms-Reduced.pdf). Clio sells practice-management software.

**Slow and unpaid B2B receivables (SMB)**
- US (Intuit QuickBooks 2025 Late Payments Report; 2,487 businesses with 0–100 employees, January 2025): 56% are owed money on unpaid invoices, averaging about $17,500, and about 1 in 10 invoices is more than 30 days overdue — [QuickBooks US](https://quickbooks.intuit.com/r/small-business-data/small-business-late-payments-report-2025/). Secondary coverage cites about $17,000 and a sample of 1,700+, so the write-ups differ — [AOL](https://www.aol.com/articles/small-businesses-owed-17-500-150003790.html)
- UK edition: 62% owed, averaging £21.4K, with 11% of invoices more than 30 days overdue — [QuickBooks UK](https://quickbooks.intuit.com/uk/blog/small-business-late-payments-report-2025/)
- Atradius 2025 US, via a secondary blog (n=240, sample skewed toward mid-size manufacturers and distributors): 43% of B2B invoice value overdue, 52% paid on time, 5% written off; average terms 45 days. Top causes: customer liquidity 45%, slow customer payment processes 33%, invoice disputes 23% — [Lonely Entrepreneur](https://lonelyentrepreneur.com/founder-days-to-get-paid/). Atradius 2024 US: about half of invoices overdue, bad debt averaging 8% of B2B credit sales — [Atradius 2024](https://atradius.us/knowledge-and-research/reports/b2b-payment-practices-trends-united-states-2024)
- UK: late payment costs the economy almost £11bn a year and causes about 4,000 business closures a year (government and Small Business Commissioner research) — [Small Business Commissioner](https://www.smallbusinesscommissioner.gov.uk/new-powers-for-the-small-business-commissioner-as-part-of-government-package-to-tackle-late-payments/). Good Business Pays (a campaign group) counted £109.2bn of invoices paid late from January to September 2025 — [NOT Ltd](https://notltd.co.uk/news/uk-companies-late-invoice-payments-2025)

**Other leaks tested**
- Supplier rebates: "4% of potential rebate revenue typically goes unclaimed". 57% of US distributors leave rebate revenue unclaimed (2019 piece), and in the 2024 State of Volume Rebates, 52% doubt they receive their full rebates. Enable is a rebate-software vendor, so these are vendor claims, and the snippet did not tie each number to one Enable page — [Enable](https://enable.com/articles/regain-control-of-your-supplier-rebates-and-maximize-your-rebate-revenue); [Enable blog](https://enable.com/blog/the-supplier-rebate-model-is-broken-and-its-costing-distributors); [Enable 5 ways](https://enable.com/blog/5-ways-your-wholesale-distribution-business-can-earn-more-rebate-revenue). Root cause: procurement negotiates the rebate, AP pays the invoices that earn it, and nobody adds up the spend at period end — [Corpay](https://www.corpay.com/resources/blog/vendor-rebates)
- Duty drawback: "over 85% of eligible businesses never file a single claim" (vendor claim) — [Passport](https://passportglobal.com/blog/recover-us-import-tariffs-duty-drawback-explained/). Drawback refunds up to 99% of duties. US annual drawback claims grew from $838M (2017) to an estimated $3.9B (2023), unverified against CBP data — [Consyn](https://consyn.substack.com/p/how-consyn-has-delivered-millions). Tariff drivers in 2025: Section 301, IEEPA duties, reciprocal tariffs and the end of de minimis — [Passport](https://passportglobal.com/blog/recover-us-import-tariffs-duty-drawback-explained/)
- Amazon FBA reimbursements: from March 2025, Amazon reimburses lost or damaged inventory at manufacturing cost rather than retail price (sources give 10 March or 31 March). Post-order losses are still paid at sale price minus fees — [eComEngine](https://www.ecomengine.com/blog/fba-reimbursement-policy); [Shopifreaks](https://www.shopifreaks.com/amazon-changes-its-reimbursement-policy-to-the-detriment-of-sellers/). The claim window for most cases dropped to 60 days (reported from 23 October 2024) — [Cahoot](https://www.cahoot.ai/amazon-fba-reimbursement-changes-threaten-seller-payouts/)
- Dealer warranty reimbursement: by one count, 49 states have retail-compensation laws for warranty parts and 27 have zero-cost-parts provisions — [Digital Dealer, 2017](https://digitaldealer.com/news/retail-warranty-reimbursement-leveling-playing-field/87856/). Dealers can request rate increases once a year — [Withum](https://www.withum.com/industries/dealerships/warranty-reimbursement); [JD Supra (California)](https://jdsupra.com/legalnews/warranty-reimbursement-rates-under-the-23817). Wyoming passed a 2025 law tying parts reimbursement to the dealer's retail markup — [Wyoming SF0106 (2025)](https://www.wyoleg.gov/2025/Enroll/SF0106.pdf)

### Inferences
- Healthcare denials are the most measurable leak, with independent multi-year trend data. CPG deductions are the most "contingency-native": a disputed deduction is a discrete dollar amount with a yes or no outcome.
- The retail-rate warranty uplift happens once a year, so it fails the weekly test. Warranty claim rejections and OEM chargebacks may recur weekly, but I found no data on them.
- Leak sizes in percent of revenue, rough ranking (all wide ranges, mostly vendor-sourced): unbilled T&M (3–25% of T&M revenue) > CPG deductions (1–7% of gross revenue, of which 10–25% invalid) > freight errors (2–7% of freight spend recoverable) > healthcare underpayments (1–11% of net revenue, vendor claim) and denials (≥10% initial denials at 41% of providers).

### Gaps
- No independent (non-vendor) benchmark of CPG deduction rates. No Kroger, UNFI or KeHE specific deduction rates were found.
- A freight-audit vendor blog claimed an average reclass overcharge of about $145 per corrected shipment, 4–6% of LTL shipments facing reclass disputes, and 70–82% recovery when challenged. I could not tie these to a specific URL, so they are excluded from findings.
- Ecommerce chargeback volume and friendly-fraud statistics for 2025-26 (Mastercard, Visa, Chargebacks911) were not retrieved before the search budget ran out.
- Telecom and utility bill audit, SaaS renewal leakage, quote follow-up leakage, insurance subrogation, sales-tax refunds and involuntary churn were not researched (budget ran out). Treat them as untested, not rejected.
- No owner or operator quotes were collected (Reddit blocked; no pages could be opened).

---

## Q2. Per-problem records: size, owner, approver, current handling, competition, AI trajectory, buyer channels, counter-argument, and the six-test pass/fail

### Takeaway
Six to eight problems qualify for review. Two pass all six tests most cleanly: CPG retailer deductions for emerging and mid-size brands, and denials and underpayments for small independent medical practices. Freight/LTL audit, unbilled T&M work and supplier rebate leakage pass with caveats. B2B SMB collections, ecommerce chargebacks and Amazon FBA reimbursements fail test (f), because cheap or bundled tools already exist.

### Cited Findings
(Facts here repeat or extend Q1 sources. Owner, approver and channel fields are inferences unless a URL is shown.)

#### P1. Retailer deductions and compliance fines against CPG and consumer brands
- **Problem:** Retailers and distributors short-pay invoices (shortages, promo or allowance deductions, OTIF and compliance fines). Many deductions are invalid, but brands lack the staff to dispute them within the window.
- **Industry:** CPG food, beverage, personal care and household goods selling to Walmart, Target, Kroger, Amazon Vendor Central, UNFI, KeHE and regional grocers.
- **Size where it hurts most (inference):** brands with about $5M–$250M revenue. They are big enough to have many deductions but too small for HighRadius-class software or a deductions team.
- **Exact task:** Staff download remittance advice and deduction backup from retailer portals (Walmart APDP, Amazon Vendor Central, UNFI and KeHE portals). They match each deduction to the PO, bill of lading, proof of delivery and promo agreement, decide if it is valid, file a dispute with evidence in the portal before the window closes, then chase and post the repayment.
- **Who feels it / who approves (inference):** AR or deductions analyst, controller; approved by the CFO, a fractional CFO, or the founder or CEO at smaller brands.
- **Frequency and hours:** Weekly, since remittances arrive with each payment cycle. Manual cost is $200–$300 to research and resolve one deduction, per [Stealth Agents](https://stealthagents.com/research/ai-deduction-management-automation-statistics-2026) citing Smyyth and Versapay. iNymbus says manual processing cost $3.20–$5.00 per claim, falling to about $1 when automated (vendor case study) — [casestudies.com/iNymbus](https://www.casestudies.com/company/inymbus/case-study/how-warner-brothers-reduced-deductions-and-chargeback-processing-costs-by-80). The two figures differ by about 50x, probably because they measure different things (full research versus portal filing).
- **Dollar cost:** 1–7% of gross revenue deducted (vendor), Walmart average 5.8% of invoices (vendor), 10–25% of that invalid (vendor). See Q1.
  - **Estimate:** a $20M brand × 2–5% deducted = $400K–$1M a year. × 10–25% invalid = $40K–$250K recoverable. At a hypothetical 25% contingency, that is $10K–$62K a year in fees per client.
- **Handled today:** In-house AR staff. SaaS such as SupplyPike/SPS Commerce, iNymbus, HighRadius, Glimpse and Promomash. Contingency recovery firms such as RevRecoup ("pure contingency — pay only on recovery") — [RevRecoup](https://revrecoup.com/go/manufacturing/). One review says iNymbus "price points seem to be a little higher than other options" — [GetApp NZ](https://www.getapp.co.nz/software/2059775/inymbus).
  - Vendor case study: a manual process had 90.73% of disputes cancelled and only 2.71% approved — [SPS Commerce](https://www.spscommerce.com/community/articles/level-up-maximizes-dispute-win-rate-over-50x).
- **Competition:** Crowded and rising. Glimpse raised a $10M Series A to automate deductions — [8VC](https://8vc.com/resources/glimpses-10m-series-a-to-rescue-cpg-margins); [SalesTechStar](https://salestechstar.com/?p=246270); date not confirmed. Others include Carbon6, Doss, Endless Commerce, HighRadius and SPS/SupplyPike. Published contingency rates for this niche were not found. General collection contingency is 25–35% — [Boostly glossary](https://invoice.boostly.com/glossary/contingency-fee).
- **AI trajectory (inference): grows.** More AI lets one human reviewer handle more disputes, and the long tail (UNFI, KeHE, regional grocers, Costco, distributors) is messy and portal-specific. Risk: SaaS vendors automate the top retailers (Walmart, Amazon) first, which squeezes services margins there.
- **Reach buyers (inference, not verified this session):** Expo West/East, NOSH, BevNET, the Startup CPG community, CPG-focused fractional CFO and bookkeeping firms, food brokers, and KeHE/UNFI supplier events. Grocery Dive and Supply Chain Dive newsletters.
- **US company count:** not found.
- **Strongest argument against:** Funded SaaS (SPS/SupplyPike, HighRadius, Glimpse, iNymbus) already automates Walmart, Amazon and Target. A services firm's edge is limited to the long tail, which is harder to automate and where fewer dollars are recoverable per brand. Recoveries also drop sharply after 90 days, so you must onboard fast.
- **Six tests:** (a) weekly — pass; (b) measurable — pass; (c) already paid for — pass; (d) approver feels it — pass; (e) AI+human — pass (portal automation is brittle); (f) no tool under $100/month and no free platform feature found — pass. **6/6 (preliminary).**

#### P2. Denied and underpaid claims at small independent medical practices
- **Problem:** Payers deny or underpay claims. Small practices lack staff to work every denial, so recoverable claims age out of appeal windows.
- **Industry:** US healthcare: independent physician groups, PT/OT, behavioral health, chiropractic, specialty clinics, ASCs.
- **Size where it hurts most (inference):** 1–50 provider practices without a dedicated denials team.
- **Exact task:** A biller pulls the denial or underpayment from the ERA/835. They read the reason code, check eligibility, authorization and coding, compare the paid amount against the payer contract fee schedule, fix and resubmit, or write and send an appeal letter with records. Then they track it to payment.
- **Who feels it / who approves (inference):** Billing manager or practice administrator; approved by the practice owner, physician partner, or a CFO at larger groups.
- **Frequency:** Daily or weekly (ERAs arrive continuously). Staffing strain: 43% understaffed (Experian 2025). Hours data not found.
- **Dollar cost:** 41% of providers have ≥10% initial denial rates (Experian 2025). Hospitals spend $19.7B a year fighting denials (Premier, 2024 report), and 54–70% of denials are eventually overturned (Premier). Underpayments are 1–11% of net revenue (vendor).
  - **Estimate:** a practice billing $3.3M a year with a 10% initial denial rate has $330K denied. If 54% is recoverable on appeal (Premier's 2024 figure), about $178K is at stake. At a 25% contingency, about $45K a year in fees.
- **Handled today:** In-house billers; outsourced billing companies (typically paid a % of collections, rate not verified this session); RCM platforms. Contingency denial recovery at 25% of recovered, no recovery no fee (vendor, PT and mental health) — [Relvio](https://relvio-health.pages.dev/). Medicare RAC benchmark fees of 9–12.5% (older, around 2009–2017) — [CPBJ](https://www.cpbj.com/cms-we-have-a-recovery-audit-contractor-problem).
- **Competition:** Very crowded: thousands of billing companies, Waystar, Experian Health, plus AI-RCM startups (prior knowledge, not re-verified). Only 14% of providers use AI in claims so far (Experian 2025).
- **AI trajectory (inference): grows.** Payers are using AI to deny more (see the Healthcare Guys June 2026 headline), so appeal volume rises. LLMs are good at drafting appeals from records.
- **Reach buyers (inference):** MGMA, HFMA, AAPC, specialty groups (e.g., APTA Private Practice section), PM/EHR marketplaces (athenahealth, Tebra), white-label partnerships with billing companies.
- **US company count:** not found.
- **Strongest argument against:** The most crowded market here. Every buyer already has a biller or billing company, HIPAA/BAA compliance raises costs, and PM/EHR vendors keep adding AI denial worklists.
- **Six tests:** **6/6 (preliminary).** (f) passes because PM/EHR claim scrubbers prevent some denials, but appeal and underpayment labor is not bundled in any sub-$100 tool found.

#### P3. Freight, LTL and parcel invoice overcharges and accessorials
- **Problem:** Carriers bill wrong rates, duplicate invoices, phantom accessorials, wrong fuel surcharges and reclass/reweigh charges. Mid-size shippers pay without auditing.
- **Industry:** Manufacturers, distributors, ecommerce and wholesale shippers.
- **Size where it hurts most (inference):** about $1M–$25M a year in freight spend. That is below the threshold where enterprise audit firms (Cass, TransImpact, etc.) are cost-effective for the client, but above where errors are trivial.
- **Exact task:** An AP clerk or logistics coordinator receives carrier invoices weekly by PDF, EDI or portal. They check each against the contracted tariff, quote, BOL and PO: weight, class, accessorials, fuel index, duplicates. They dispute errors with the carrier and track credits.
- **Who feels it / who approves (inference):** Logistics or transportation manager, AP; approved by the VP of operations or supply chain, or the CFO.
- **Frequency:** Weekly invoice cycles. NMFC density change confusion continues in 2026 (CarrierAtlas).
- **Dollar cost:** 3–25% of invoices with errors (range across vendors); recoverable 2–7% of freight spend (vendor).
  - **Estimate:** $5M freight spend × 2–4% = $100K–$200K a year recoverable.
- **Handled today:** Freight audit and pay firms, TMS audit modules, 3PL audit. Contingency rates were not found this session.
- **Competition:** Crowded at enterprise; the mid-market is less clear.
- **AI trajectory (inference): shrinks in price.** Invoice-versus-contract checks are easy for LLMs, so this will be commoditized into TMS and AP software within 24 months.
- **Reach buyers (inference):** NASSTRAC, SMC3, CSCMP, 3PL and freight-broker partners, ShipStation and Shopify app ecosystems.
- **Strongest argument against:** Mature audit vendors already exist, and the work commoditizes fast. Small shippers often use broker all-in rates, so there is less to audit.
- **Six tests:** **6/6 for LTL/accessorials (preliminary).** Weaker for parcel, where cheap or free refund services historically existed (prior knowledge, not re-verified; I could not check current pricing).

#### P4. Unbilled or under-billed T&M and field work (subcontractors, field service, MSPs, law firms)
- **Problem:** Work gets done (extra labor, materials, change orders, after-hours calls, billable time) but never reaches an invoice.
- **Industry:** Specialty trade subcontractors, commercial field service, facility services, IT MSPs, agencies, law firms.
- **Size where it hurts most (inference):** 10–200 employees with manual or paper time and materials capture.
- **Exact task:** An office admin or PM compares timesheets, field tickets, dispatch notes, photos, PSA tickets and change orders against what was invoiced. They find gaps, build the missing invoice lines or change order paperwork, and send them to the customer.
- **Who feels it / who approves (inference):** Controller, operations manager, PM; approved by the owner or CEO.
- **Frequency:** Weekly billing cycles.
- **Dollar cost:** 15–25% of T&M labor never invoiced (vendor); 3–15% of revenue (various vendors). Law: an all-firm average of 3.0 hours captured but 2.6 invoiced per 8-hour day (Clio).
  - **Estimate:** a 0.4 hour/day gap × an assumed $300/hour × 230 days ≈ $27.6K per lawyer per year. Some of that gap is deliberate write-downs, not leakage.
- **Handled today:** Office staff; FSM/PSA software (ServiceTitan, Jobber, HaloPSA, ConnectWise; prior knowledge); T&M capture tools (Rhumbix, now being acquired by Autodesk; Level).
- **Competition:** Moderate. The capture problem is behavioral, not only software.
- **AI trajectory (inference): grows short term, then gets absorbed into FSM/PSA platforms.** AI can read voice notes, photos and tickets to draft invoice lines.
- **Reach buyers (inference):** ASA (subcontractors), MCAA, NECA, PHCC, ACCA; ServiceTitan, Procore and ConnectWise marketplaces; MSP communities.
- **Strongest argument against:** Contingency pricing is awkward, because the client must bill its own customers retroactively, which strains relationships. It also needs deep access to field data. Platform vendors are adding AI capture.
- **Six tests:** **5/6 (preliminary).** (c) is weak: buyers pay for software and admins, but rarely for "leakage recovery" as a line item. (f) passes provisionally.

#### P5. Supplier rebate and volume-discount leakage (distributors, multi-site buyers)
- **Problem:** Earned rebates go unclaimed because agreement terms sit in PDFs and nobody reconciles purchases against thresholds.
- **Industry:** Wholesale distribution, building products, foodservice, multi-site operators.
- **Size where it hurts most (inference):** $20M–$500M distributors.
- **Exact task:** Pull rebate terms from supplier agreements. Match purchase and sales data each period against tiers and thresholds. Compute what is owed, file claims, and chase payment.
- **Who feels it / who approves:** Purchasing or rebate manager, AP; approved by the CFO (inference).
- **Frequency:** Claims are monthly or quarterly; purchase tracking is weekly. This makes test (a) borderline.
- **Dollar cost:** 4% of potential rebate revenue unclaimed (vendor, Enable).
- **Handled today:** Spreadsheets, ERP modules, Enable (SaaS). Recovery audit firms likely exist, but I found no contingency pricing.
- **Competition:** Low to moderate in the mid-market (inference).
- **AI trajectory (inference): grows.** Extracting contract terms is a strong LLM task.
- **Reach buyers (inference):** NAW, buying groups such as Affiliated Distributors, ERP partner channels (Epicor, Infor, NetSuite).
- **Strongest argument against:** Thin independent evidence, and only 4% of rebate value is at stake. Claims are periodic, not weekly.
- **Six tests:** **5/6 (preliminary)**, failing (a) because cadence is borderline.

#### P6. Duty drawback and tariff refunds for small and mid importers and DTC brands
- **Problem:** Importers that export, return or destroy goods are owed up to 99% of duties back but never file.
- **Industry:** DTC and ecommerce brands, importers and manufacturers.
- **Size where it hurts most (inference):** $5M–$100M importers hit by 2025 tariffs.
- **Exact task:** Match import entries (duty paid) to export, return or destruction records. Prepare and file drawback claims through a licensed customs broker in ACE.
- **Who feels it / who approves:** Logistics or finance manager; approved by the CFO (inference).
- **Frequency:** Records accumulate weekly; claims are filed periodically.
- **Dollar cost:** More than 85% of eligible businesses never file (vendor claim, Passport). US drawback claims reached an estimated $3.9B in 2023 (Consyn, unverified).
- **Handled today:** Drawback specialists (Passport, Consyn) and customs brokers. Pricing not found.
- **AI trajectory (inference): grows** while tariffs stay high.
- **Strongest argument against:** Needs a licensed customs broker. Depends on tariff policy, which can reverse. Overlaps the "new rules" lens.
- **Six tests:** **4/6 (preliminary).** (a) borderline. (e) is partial, because a licensed broker must file.

#### P7. B2B SMB slow pay and unpaid invoices (pre-collection follow-up)
- **Problem:** SMBs are owed about $17.5K on average (US), and staff chase invoices by hand.
- **Industry:** All B2B SMBs, especially manufacturers, distributors and agencies.
- **Exact task:** Send reminder emails and calls, resolve disputes (23% of late payments cite disputes, Atradius 2025 via blog), and resend invoices or POs.
- **Who feels it / who approves:** Bookkeeper or owner.
- **Handled today:** QuickBooks/Xero reminders (included in subscriptions — prior knowledge, not re-verified); Chaser from $259/month — [Capterra](https://capterra.com/p/157101/CHASER/) — or about £199/month Compact tier — [ERP Research](https://erpresearch.com/erp-add-ons/ar-collections/chaser). Collection agencies charge 25–35% contingency (Boostly glossary).
- **AI trajectory (inference): shrinks.** It is being absorbed into accounting platforms.
- **Halal flag:** Recovery models that add late-payment interest touch riba concerns. UK statutory late-payment interest, which the March 2026 package makes mandatory at 8% above Bank of England base rate per the [Small Business Commissioner](https://www.smallbusinesscommissioner.gov.uk/new-powers-for-the-small-business-commissioner-as-part-of-government-package-to-tackle-late-payments/), is an example. So are factoring and debt collection on interest-bearing debt. No ruling given.
- **Strongest argument against:** Cheap bundled tools, and the slow-pay often reflects customer cash problems (45% liquidity), which AI cannot fix.
- **Six tests:** **Fails (f):** automated reminders are bundled free in QuickBooks/Xero (prior knowledge); Chaser costs $259/month.

#### P8. Ecommerce payment chargebacks and friendly fraud
- **Handled today:** Chargeflow charges a 25% success fee on recovered chargebacks with no contracts or minimums, $29 per deflected alert, and Prevent at $0.20–$0.40 per scanned transaction (pricing inconsistent across pages) — [Redo comparison](https://redo.com/resources/articles/comparisons/chargeflow-pricing); [Chargeflow vs Stripe](https://chargeflow.io/chargeflow-vs-stripe-smart-disputes); [Shopify App Store](https://apps.shopify.com/chargeflow?locale=en). Stripe Smart Disputes is bundled into Stripe; Chargeflow's own comparison shows Stripe coming out $3,503 ahead on the same inputs (vendor-produced).
- **Six tests:** **Fails (f):** crowded, success-fee-only tools with no minimums plus processor-native dispute tools. Attractiveness is low.

#### P9. Amazon FBA lost and damaged inventory reimbursements
- **Six tests:** **Fails (f) and shrinking.** Amazon's March 2025 switch to manufacturing-cost reimbursement and the 60-day window cut the recoverable pool (eComEngine; Cahoot). The market is crowded with low-fee contingency tools (prior knowledge; current prices not re-verified).

#### P10. Dealer warranty reimbursement (retail rate)
- Withum charges a flat $7,500 per parts or labor submission, or $10,500 for both, with no contingency — [Withum](https://www.withum.com/industries/dealerships/warranty-reimbursement).
- **Six tests:** **Fails (a):** submissions happen once a year. The weekly part (claim rejections and OEM chargebacks) is not evidenced.

### Inferences
- Contingency pricing fits best where each item has a discrete dollar value and a clear win or lose outcome: deductions, denials and underpayments, freight overcharges, rebates and drawback. It fits badly for unbilled work, which hits the client's own customer relationships, and for AR, where there is a halal risk if interest is involved.
- Blind attractiveness (pain × willingness to pay × low competition × staying power):

| Problem | Score |
|---|---|
| P1 CPG deductions | 8 |
| P2 Healthcare denials and underpayments | 7 |
| P3 Freight/LTL audit | 6 |
| P4 Unbilled T&M | 6 |
| P5 Supplier rebates | 6 |
| P6 Duty drawback | 5 |
| P7 SMB AR | 4 |
| P10 Dealer warranty | 4 |
| P8 Ecommerce chargebacks | 3 |
| P9 Amazon FBA reimbursements | 2 |

### Gaps
- Contingency rates for deduction recovery, freight audit, rebate audit and drawback could not be found. Pricing for SPS/SupplyPike, iNymbus, Glimpse and HighRadius is not public in the snippets I saw.
- Outsourced medical billing rates (% of collections) were not verified (search budget ran out).
- US company counts for each segment were not found.
- Hours-per-week evidence was found only as per-deduction cost ($200–$300); no hours data for the other problems.
- Owner quotes: none collected.

---

## Q3. What do recovery vendors charge, how crowded is each market, and which leaks are already handled by cheap or free tools?

### Takeaway
Published pricing is scarce. What exists: chargeback recovery at a 25% success fee with no minimums (Chargeflow); healthcare denial recovery at 25% contingency (a small vendor); general collections at 25–35% contingency; dealer warranty rate filings at a flat $7,500–$10,500. Chargebacks, AR reminders and FBA reimbursements are commoditized. Deductions, denials and freight are crowded at enterprise level, but mid-market and long-tail pricing is opaque.

### Cited Findings
- Chargeflow: 25% of recovered chargebacks; alerts $29 per deflected chargeback (volume discounts above 50 a month); Prevent $0.20 per scan (reduced from $0.40 list), first 1,000 free; "4x ROI guarantee" — [Redo](https://redo.com/resources/articles/comparisons/chargeflow-pricing); [Chargeflow](https://chargeflow.io/chargeflow-vs-stripe-smart-disputes)
- Denial recovery: 25% of recovered, no recovery no fee, no contracts (vendor) — [Relvio](https://relvio-health.pages.dev/). Medicare RAC base fees 9–12.5%, and 14–17.5% for DME (older) — [CPBJ](https://www.cpbj.com/cms-we-have-a-recovery-audit-contractor-problem)
- Collections contingency is typically 25–35% — [Boostly](https://invoice.boostly.com/glossary/contingency-fee)
- Deductions: RevRecoup works on pure contingency (rate not stated) — [RevRecoup](https://revrecoup.com/go/manufacturing/). iNymbus pricing is seen as "a little higher" (review) — [GetApp NZ](https://www.getapp.co.nz/software/2059775/inymbus). Glimpse raised a $10M Series A — [8VC](https://8vc.com/resources/glimpses-10m-series-a-to-rescue-cpg-margins)
- AR: Chaser costs $259/month — [Capterra](https://capterra.com/p/157101/CHASER/)
- Dealer warranty: Withum charges $7,500 per submission or $10,500 combined, with no contingency — [Withum](https://www.withum.com/industries/dealerships/warranty-reimbursement)
- The UK Small Business Commissioner (a free government service) has recovered £10M in late payments since 2017, including almost £1M in the current financial year (January 2026 report) — [SBC](https://www.smallbusinesscommissioner.gov.uk/10-million-of-late-payments-got-back-by-small-business-commissioner/)

### Inferences
- Test (f) checks, one per problem:
  - P7 AR fails (bundled reminders in accounting software; Chaser $259/month is above $100).
  - P8 chargebacks fails (success-fee tools with no minimums; Stripe/Shopify built-ins).
  - P9 FBA fails (crowded low-fee tools; Amazon cut values).
  - P1, P2, P3 (LTL), P5 and P6 pass: no sub-$100 tool or free platform feature does the dispute or appeal work end to end.
- A 25% success fee is the visible market anchor. A services firm could price at 15–30% contingency, or a monthly retainer plus a smaller success fee (inference).

### Gaps
- Pricing for freight audit firms, rebate audit firms, drawback brokers, and SPS/SupplyPike, HighRadius or Glimpse.
- Current pricing for parcel refund services and FBA reimbursement tools (not re-verified).
- Whether Stripe or Shopify now include free automated dispute filing at the level that would make chargeback services fully redundant (only vendor comparisons seen).

---

## Q4. Which leaks are too small or messy for the funded vendors, leaving a gap?

### Takeaway
Funded vendors concentrate on large retailers (Walmart, Amazon, Target), hospital systems and enterprise shippers. The likely gaps are long-tail deductions from distributors and regional grocers (UNFI, KeHE, Costco, regional chains), small practices' underpayments against contract fee schedules, mid-market LTL accessorial and reclass disputes after the 2025 NMFC change, and mid-market rebate reconciliation. These gaps are inferred from where the vendors focus; no direct gap data was found.

### Cited Findings
- Deduction vendors' marketing is built around Walmart, Target, Amazon and Kroger (e.g., [Doss](https://www.doss.com/blog/how-to-automate-deduction-management-walmart-target-amazon-and-kroger); [SupplyPike](https://supplypike.com/walmart)). HighRadius's flagship case is Kraft Heinz, a very large CPG company — [HighRadius](https://www.highradius.com/resources/case-studies/kraft-heinz-dms/)
- Distributor economics for small brands are heavy: distributors such as UNFI and KeHE take a 20–28% margin plus a 7–12% freight allowance and other fees — [EightX (fractional CFO firm)](https://eightx.co/blog/cpg-broker-distributor-fees). The snippet did not tie this to one of EightX's two pages.
- Many deductions are written off because they are "not worth the cost to investigate" (Fractal opinion) — [Fractal](https://fractal.ai/article/deductions-margin-leakage-cpg/). Manual cost is $200–$300 per deduction — [Stealth Agents](https://stealthagents.com/research/ai-deduction-management-automation-statistics-2026)
- Underpayments look "paid and closed", so standard denial workflows miss them (vendor) — [HelpSquad](https://helpsquad.com/blog/beyond-denials-how-outsourced-payer-underpayment-recovery-finds-revenue-your-denial-reports-miss/)
- LTL density-based classification confusion persists a year after the August 2025 change — [CarrierAtlas](https://carrieratlas.com/news/ltl-carriers-say-shippers-still-dont-get-density-based-nmfc-a-year-in)

### Inferences
- The economic gap: if a manual dispute costs $200–$300, deductions under about $300–$1,000 are written off by default. AI plus human review could cut the cost per dispute enough to make the small-ticket long tail worth recovering. That is where a contingency services firm beats both in-house staff and enterprise SaaS.
- Small medical practices' underpayments against negotiated contracts need the contract fee schedule loaded and compared line by line. Billing companies paid a % of collections have little incentive to audit their own posted payments, which leaves room for an independent second-look audit on contingency.
- Shariah notes: P1–P6 do not inherently involve interest. P7 (AR and collections) is flagged if late-payment interest, statutory interest, factoring or interest-bearing debt collection is involved. Insurance subrogation (not researched) may need review because it works through conventional insurance. Healthcare patient-balance collection (not in scope above) should be checked for medical credit or financing links.

### Gaps
- No direct interviews, forum posts or reviews confirming the long-tail gap (Reddit blocked; pages could not be opened).
- No count of US brands selling into UNFI or KeHE, or of independent practices doing their own billing, was found this session.
- The web search budget ran out before testing telecom/utility audit, SaaS renewal leakage, quote follow-up, involuntary churn, insurance subrogation and sales-tax refunds. These should be treated as untested.
