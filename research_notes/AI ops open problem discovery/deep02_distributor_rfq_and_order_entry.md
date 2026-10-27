# Deep dive 02: Distributor / job-shop RFQ quote turnaround (P1) and emailed/PDF/fax/phone PO re-keying into the ERP (P2)

Research date: 27 October 2026. Researcher: deep-02 subagent. USD unless stated.

Research conditions (read first):
- Exactly 30 web searches were used (the full budget). None repeats a first-round query. The first-round notes read were lens05 (speed), lens03 (paperwork), lens09 (VC money flow) and lens07 (bad software). Their facts are referenced, not repeated, except where needed for the math.
- One page fetch was tried early: WebFetch on paperlessparts.com/pricing failed with "getaddrinfo ENOTFOUND". The US Census CBP API (api.census.gov) was refused by the egress proxy ("CONNECT tunnel failed, response 403"). So every finding below comes from search-engine result summaries, not from reading full pages. Treat exact figures as "as reported in the search summary of that page".
- Where a search summary merged several result pages and I could not tell which page held a figure, I say "exact page not pinned" and list the candidate pages.
- Labels: "vendor claim" = number from a company that sells a fix. "estimate" = my own math, with inputs shown. "assumption" = an input I chose, not sourced.
- P1 = slow RFQ/quote turnaround at industrial, electrical, MRO and building-products distributors and at CNC/fabrication job shops. P2 = emailed/PDF/fax/phone POs retyped into the ERP (sales order entry) at wholesale distributors and make-to-order manufacturers.

---

## Q1. The exact task, in plain words

### Takeaway
P1 has two different tasks. At a distributor, an inside sales rep matches and prices a list of parts. At a job shop, an estimator works out the cost of making a part from a drawing. P2 is the same at every company: a customer-service or order-entry rep reads a PO and keys each line into the ERP as a sales order, then fixes the exceptions.

### Cited Findings
- P1 distributor: electrical-distributor inside-sales job posts list "managing Requests for Quotes (RFQs), preparing accurate pricing" as core duties (Insight Global postings for electrical-distributor quoting roles). — [Insight Global, Chesapeake VA](https://jobs.insightglobal.com/find_a_job/virginia/job-486748); [Insight Global, National City CA](https://jobs.insightglobal.com/find_a_job/california/job-534489/)
- P1 job shop: an estimator role "focuses on cost estimates for labor, material, cycle time, and outside processing" (Actalent, Bloomington MN, 2026). — [career.com / Actalent](https://www.career.com/job/actalent/estimator/j202604180555052797508). A Winter Park FL "Manufacturing Estimator" role handles RFQs and quoting inside ProShop ERP (2026). — [career.com / Yeager Manufacturing](https://www.career.com/job/yeager-manufacturing-technologies/manufacturing-estimator/j202606170249332631169)
- P1 job shop: quoting "depends on the most experienced members on the shop floor, who are already maxed out". Estimating new work is called "one of the biggest bottlenecks in machining" (vendor framing). — [CloudNC news release](https://cloudnc.com/news-room/new-ai-solution-launched-to-accelerate-the-cnc-machining-estimating-process-and-eliminate-quoting-bottlenecks)
- P1 job shop: Paperless Parts' engineering blog explains "why automated estimation of machined parts is hard" (title only; not read). — [Medium, Paperless Parts tech blog](https://medium.com/paperless-parts-tech-blog/why-automated-estimation-of-machined-parts-is-hard-2ab0d0e4af6f)
- P2: the AI order-import workflow for Prophet 21 reads the PO, matches lines to the item master and cross-references, applies contract pricing, and stages a draft order that a person approves before posting (third-party guide). — [Airdev, P21 order import](https://www.airdev.co/erp/prophet-21/order-import)
- P2: WizCommerce describes Ella's job as reading POs "in many formats", mapping "customer part numbers to internal SKUs", validating pricing and creating ERP-ready orders (vendor). — [WizCommerce AI order entry](https://wizcommerce.com/product/ai-order-entry-software/)
- P2: an order-entry job post says the role ensures "purchase orders are accurately reviewed, validated, and entered into internal systems", and includes "cleaning up and standardizing order entry workflows—particularly within Sage" (Insight Global, Portland OR, 2026). — [Insight Global job 529276](https://insightglobal.com/jobs/find_a_job/job-529276)
- P2: an Orlando FL post describes "accurate and timely entry of complex technical orders into the ERP system" (2026; exact page not pinned among [mediabistro](https://www.mediabistro.com/jobs/3275738259-order-entry-specialist), [snagajob](https://www.snagajob.com/jobs/1265976294) and [career.com Starfire Direct](https://www.career.com/job/starfire-direct/customer-service-order-entry-specialist/j202604251114500570981)).

### Inferences
- P1, distributor version (plain words): an inside sales rep opens an emailed RFQ or contractor bill of materials with 5 to 200 lines. For each line the rep finds the item (often a manufacturer part number or a loose description) and cross-references it to the distributor's SKU or an approved substitute. The rep checks stock across branches and supplier lead times, and asks the manufacturer for a special price on large or non-stock lines. The rep applies the customer's price level or contract, then sets the margin, with the branch or sales manager approving anything below the margin floor. Finally the rep builds the quote in the ERP (P21, Eclipse, Infor, Acumatica, NetSuite) and emails a PDF back, ideally within an hour.
- P1, job-shop version (plain words): an estimator downloads the drawing or 3D model, reads the material, tolerances, finish and quantity, and requests a material price. The estimator plans the routing, estimates setup and cycle time, and gets outside-processing quotes (plating, heat treat). The owner or GM then sets the price and margin based on load and how much the shop wants the customer, and the quote goes out.
- P2 (plain words): a CSR opens an emailed PDF PO, or a fax, spreadsheet or voicemail, and finds the customer account and ship-to. For each line the CSR maps the customer's part number or description to the SKU, checks the price against the quote or contract, and checks stock and ship date. The CSR saves the sales order, sends an acknowledgment, and calls the customer or salesperson about any mismatch.
- Only the human judgment in P1 (margin, substitutes, supplier special pricing) differs materially from P2. P2 is mostly lookup plus keying, which is why it is commoditising faster (see Q7 and Q8).

### Gaps
- No time-and-motion study of a distributor RFQ (lines per quote, minutes per line) was found from any independent source.

---

## Q2. Who feels it and who approves the money

### Takeaway
P1: inside sales reps and estimators feel it. The VP Sales or Inside Sales Manager (distributor) or the owner/president or GM (job shop) approves spend. P2: order-entry/CSR staff and their supervisor feel it. The VP Operations, COO, CFO or owner approves. In practice, at sub-$100M firms the owner/president signs both.

### Cited Findings
- Job titles in 2026 postings: "Inside Sales Representative" (OneSource Distributors/Sonepar, Crescent Electric Supply, Exco/All Current), "Order Entry Specialist", "Customer Service / Order Entry Specialist", "Order Management Specialist", "Estimator", "CNC Machinist/Estimator", "Manufacturing Estimator". — [career.com OneSource](https://www.career.com/job/onesource-distributors/inside-sales-representative/j202510230009116148919); [career.com Crescent Electric](https://www.career.com/job/crescent-electric-supply-company/inside-sales-representative/j202604272035516503495); [All Current / Exco](https://careers.ebscoind.com/allcurrent/job/Houston-Inside-Sales-TX-77020/1405158700/); [career.com Empire Distributing CS/Order Entry](https://www.career.com/job/empire-distributing/customer-service-order-entry-specialist/j202604061402294941899); [Insight Global Order Management Specialists](https://insightglobal.com/jobs/find_a_job/job-529276); [career.com CNC Machinist/Estimator](https://www.career.com/job/cnc-machine-shop/cnc-machinist-estimator/j202605050702057048470)
- Comena (YC S25) names "inside sales and customer service teams" at industrial distributors and manufacturers as its users. — [YC profile mirror](https://amanydv2112-suggest-orgs.hf.space/company/yc/comena); [YC launch page](https://www.ycombinator.com/launches/O3U-comena-ai-agents-that-automate-order-processing-for-distributors-and-manufacturers)
- The quote-speed anecdote on Instalily's site comes from the "chief commercial officer of a national industrial distributor", so at large distributors the commercial chief owns quote speed (vendor-hosted). — [Instalily case study](https://instalily.ai/case-studies/quoting-speed)
- Distribution Strategy's 2017 inside-sales survey: the most-cited inside-sales effectiveness measures were gross profit dollars (50%), overall sales growth (35%) and "order entry quantity and quality" (31%). So order entry is managed as an inside-sales KPI (2017). — [Distribution Strategy, 2017](https://distributionstrategy.com/2017/04/inside-sales-in-2017-survey-results/)

### Inferences
- Buyer titles to target. P1 distributor: VP Sales, Director of Inside Sales, or President at $10M-$300M firms. P1 job shop: Owner/President, GM, or Estimating Manager. P2: VP Operations, Customer Service Manager, COO/CFO, or President.
- Because order entry is scored inside the sales org (31% in 2017), P1 and P2 often share the same budget owner at distributors. One buyer can sign for both.

### Gaps
- No 2025-2026 survey of who signs AI or outsourcing contracts at distributors was found.

---

## Q3. How often it happens and how many hours it eats (math shown)

### Takeaway
P1 job shops: 20 to 120 estimator hours a week at a busy shop (one consultancy estimate: 80 RFQs × 45-90 minutes). P1 distributors: an estimated 75 inside-sales hours a week at a mid-size branch network (my model). P2: 6 to 20 minutes per order per vendor figures, so 30-100 hours a week for a distributor keying 300 orders a week.

### Cited Findings
- P1 job shop: a shop handling 80 RFQs a week at 45-90 minutes each spends 60-120 estimator hours a week (consultancy/vendor estimate). — [Leanware](https://leanware.co/insights/rfq-automation-job-shops-mgas)
- P1 job shop: BensonsCNC quoting time fell 83%, "from 3 hours to 30 minutes for five quotes" (vendor case study, AMFG). — [casestudies.com / AMFG](https://www.casestudies.com/company/amfg/case-study/bensonscnc-cuts-quoting-time-by-83-with-amfg). Another AMFG case: CNC Solutions cut quoting time 50%. — [casestudies.com / AMFG](https://www.casestudies.com/company/amfg/case-study/cnc-solutions-customer-case-study)
- P1 job shop: a skilled estimator may take 2-4 hours on a complex quote, and a complex quote can take about two hours (vendor blogs; exact page not pinned between [ProdGenius blog 1](https://prodgenius-ai.pages.dev/blog/job-shop-estimating-quote-faster-win-more/) and [ProdGenius blog 2](https://prodgenius-ai.pages.dev/blog/manufacturing-quoting-automation/)). One case reports complex RFQs that "sometimes took more than a week" (AMFG case; page not pinned).
- P1 distributor: the national industrial distributor's reported median quote response time was "three to four hours" (vendor-hosted anecdote). — [Instalily case study](https://instalily.ai/case-studies/quoting-speed)
- P1 distributor: Instalily says it automated portions of an industrial supplier's complex RFQ process, "returning hundreds of thousands of work hours annually to the commercial team" (vendor claim, large enterprise). — [MDM, Instalily $60M](https://www.mdm.com/news/technology/ai/instalily-raises-60m-launches-ai-engineer-for-enterprise-operations/)
- P2: about 6 minutes of manual labour per order. For a distributor with 200 orders a day, that is about $130,000 a year fully loaded, falling to about $17,000 at 80% touchless processing (vendor worked example). — [WorkD](https://www.workd.com/insights/articles/automating-order-entry/)
- P2: about 20 minutes per order manual, under two minutes with Ella (vendor claim). — [WizCommerce](https://wizcommerce.com/product/ai-order-entry-software/); [Distribution Strategy, June 2026](https://distributionstrategy.com/2026/06/wizcommerce-launches-ai-order-entry-tool-for-distributors/)
- P2: "10 minutes to 10 seconds" (NetSuite add-on vendor headline). — [Anchor Group](https://www.anchorgroup.tech/blog/net-suite-sales-order-automation-10-minutes-to-10-seconds)
- P2 (first round): 20 minutes and $10-12 per order (WizCommerce), and emailed orders consuming 20-40% of several CSRs' time (2016). — see lens03.

### Inferences
- Estimate, P1 job shop, small shop: 20 RFQs/week × 60 min = 20 estimator hours/week. Busy shop: the Leanware range of 60-120 h/week. Inputs: 20 RFQs/week is an assumption; 60 min sits inside the 36 min (BensonsCNC: 3 h ÷ 5 quotes) to 2-4 h vendor range.
- Estimate, P1 distributor, mid-size (8 inside reps, several branches): 150 RFQs/week, with this mix (all assumptions):
  - 70% simple, 5 lines, 10 min
  - 25% medium, 20 lines, 45 min
  - 5% project bids, 100+ lines, 240 min
  - Weighted average = 0.70×10 + 0.25×45 + 0.05×240 = 30.25 min. 150 × 30 min = 75 hours/week, or about 1.9 FTE of pure quoting time.
- Estimate, P2: 300 orders/week (assumption carried from lens03) × 6-20 min = 30-100 hours/week, or 0.75-2.5 FTE.
- Frequency: both problems are daily at any distributor or shop of 10+ staff (inference from the job titles existing as full-time roles).

### Gaps
- No independent count of RFQs per week per distributor or per shop; the volumes above are assumptions.
- Paperless Parts and Docket benchmark reports on RFQ volume: not found in this session's searches.

---

## Q4. What it costs a typical company per month, including lost deals and errors (math shown)

### Takeaway
Labour alone: P1 is about $3K-$26K a month (job shop) or about $9K-$16K a month (mid-size distributor). P2 is about $3K-$15K a month. The lost-deal cost of slow quotes is larger than the labour but rests on assumptions: roughly $6.5K a month in gross profit at a small job shop and about $21K at a mid-size distributor, if faster quotes add 5 points of win rate. P2 error costs add an estimated $3K-$10K a month (vendor-based inputs).

### Cited Findings
- Pay inputs (2026 job posts; see Q6 for links): estimator $55K-$80K a year; distributor inside sales $47K-$77K base, with some roles adding $9K-$12K commission; order entry $16.25-$26 an hour, with ZipRecruiter's US average for "sales order" at $19.88 an hour (range $16.35-$22.84, as of 4 Jun 2026). — [ZipRecruiter](https://www.ziprecruiter.com/Jobs/Sales-Order/3)
- Win-rate inputs (all vendor): a distributor's quoted-business win rate rose from under 40% to 61% in 90 days of quote automation — [Mirage blog](https://mirage-blog.pages.dev/blog/electrical-distributor-automation-quote-to-po-90-seconds/). Under 2 hours = 90%+ win; 5+ days = under 5% — [Docket blog](https://www.docket.io/blog/speed-to-quote-is-the-1-win-rate-variable-in-manufacturing-sales). The distributor CCO: "If you respond within an hour, your probability of getting the business is higher… It takes two hours, it drops." — [Instalily](https://instalily.ai/case-studies/quoting-speed). (First two also in lens05.)
- Error inputs (vendor): 1-3% of manually entered orders have errors, and errors raise the cost of an affected order to about $250 (Conexiom CEO; via lens03). — [Medium, Conexiom CEO interview](https://medium.com/inside-the-salesforce-ecosystem/platform-chronicles-ray-grady-conexiom-954eaa39054b)
- Per-order manual cost range across vendors: $8.30 (Conexiom, lens03); $10-12 (WizCommerce, lens03); $17.50 (Y Meadows ROI calculator) — [Y Meadows ROI calc](https://www.ymeadows.com/en/roi-calc); $14-$54 (Beam AI) — [Beam AI](https://beam.ai/es/agentic-insights/ai-agents-for-order-management). Range: $8.30-$54 per order (all vendor claims).
- Netguru analysis (cited by WorkD): AI order management cuts per-order cost by $5-$15 (vendor-linked). — [WorkD](https://www.workd.com/insights/articles/automating-order-entry/)

### Inferences
Loaded hourly cost (estimate; 1.3 benefit load and 2,080 hours a year are assumptions):
- Estimator: $55K-$80K × 1.3 ÷ 2,080 = $34-$50/h.
- Inside sales: $47K-$77K × 1.3 ÷ 2,080 = $29-$48/h.
- Order entry: $16.25-$26 × 1.3 = $21-$34/h.

P1 job shop, labour (estimate):
- Small shop: 20 h/week × $34 × 4.33 = $2,944/month.
- Busy shop: 120 h/week × $50 × 4.33 = $25,980/month.

P1 job shop, lost deals (estimate; all inputs are assumptions):
- Inputs: 20 RFQs/week, $5,000 average job, 20% base win rate, +5 points of win rate from same-day quoting.
- Result: 20 × 0.05 = 1 extra job/week × $5,000 × 4.33 = $21,650/month extra revenue. At a 30% contribution margin (assumption) that is about $6,500/month.

P1 distributor, labour (estimate): 75 h/week × $29-$48 × 4.33 = $9,420-$15,590/month.

P1 distributor, lost deals (estimate; all inputs are assumptions):
- Inputs: 150 RFQs/week, $3,000 average quote, +5 points of win rate.
- Result: 7.5 extra wins/week × $3,000 × 4.33 = $97,400/month revenue. At a 22% gross margin (assumption, not sourced) that is about $21,400/month in gross profit.
- Calibration: the Mirage vendor claim (under 40% to 61%) implies +21 points, which would quadruple this figure. I use +5 to stay conservative.

P2, labour (estimate): 30-100 h/week × $21-$34 × 4.33 = $2,728-$14,722/month.

P2, errors (estimate, vendor inputs):
- 300 orders/week × 4.33 = 1,300 orders/month.
- × 1-3% error rate = 13-39 bad orders × $250 = $3,250-$9,750/month.

Totals (estimate):
- P1: about $10K-$47K/month (labour plus lost GP), with lost deals the bigger part.
- P2: about $6K-$24K/month (labour plus errors).
- The P2 figure is easier to prove to a buyer, because labour is visible on payroll. The P1 figure is bigger but rests on an assumed win-rate lift.

### Gaps
- Average quote value, win rate and gross margin for small distributors and job shops: not found from independent sources. These drive the P1 lost-deal figure.
- The $17,800 "average cost of a B2B order error" (lens03) remains unverified and is excluded from the math.

---

## Q5. How companies handle it today and what they pay

### Takeaway
Mostly in-house staff: inside sales at $47K-$77K plus commission, order-entry specialists at $16-$26 an hour (often contract-to-hire through staffing agencies), and estimators at $55K-$80K. Offshore data entry runs $5-$12 an hour (vendor-reported). Software spend is CPQ at about $63-$150 per user per month, job-shop quoting tools from about $195 a month, and quote-only order-capture software (Conexiom). Big customers go via EDI. Job shops also take marketplace work (Xometry), where the marketplace keeps about a third of the job value as gross margin.

### Cited Findings
- Contract-to-hire and staffing-agency order entry is common: Robert Half (Bethlehem PA, $23-$26/h), Insight Global (Portland OR, $19-$24 or $20-$25/h), and Itasca IL and Arlington Heights IL contract-to-hire posts at $20-$24 and $21-$26/h (2026). — [Robert Half via Hire Heroes](https://jobs.hireheroesusa.org/jobs/558691601-order-entry-specialist-at-robert-half); [Insight Global](https://jobs.insightglobal.com/find_a_job/oregon/job-529276/). The Itasca and Arlington Heights pages were not pinned (candidates: [mediabistro](https://www.mediabistro.com/jobs/3275738259-order-entry-specialist), [ZipRecruiter Order Entry](https://www.ziprecruiter.com/Jobs/Order-Entry/3)).
- Offshore rates (outsourcing-vendor sources, 2026): Philippines data entry $5-$9/h, India $4-$8/h, US onshore $18-$25/h. Per-record or per-document pricing is common for OCR-heavy queues, and contracts typically require 98% field accuracy. A Philippine provider lists back-office support at $8-$12/h. English e-commerce support runs $8-$18/h, up to $25 for technical accounts. — [Outsource Accelerator](https://www.outsourceaccelerator.com/glossary/data-entry/); [VA Masters](https://vamasters.com/philippine-outsourcing-rates-by-industry/); [Helpware](https://helpware.com/blog/ecommerce-outsourcing-philippines) (which page holds which figure is not fully pinned)
- CPQ software: DealHub about $65/user/month (Professional, 5-user minimum, billed annually) and about $100 (Enterprise), about $78K/year for 100 seats before implementation (third-party guide) — [ERP Research](https://erpresearch.com/erp-add-ons/cpq/dealhub-cpq/pricing). IBISWorld 2026 benchmark $63.1/user/month — [IBISWorld](https://img2.ibisworld.com/united-states/procurement/cpq-software/31275394). CPQing $78/user/month — [Capterra](https://www.capterra.com/p/10014422/CPQing/). SAP CPQ entry tier $10/user/month — [Capterra](https://www.capterra.com/p/153456/CallidusCloud-CPQ/pricing/). KBMax $150/user/month (Capterra; page not pinned). "Implementation costs usually exceed the first-year subscription" (search summary).
- Job-shop quoting software: Paperless Parts Growth $300/month and Professional $750/month, sourced to a 2019 press release (2019, likely outdated). Current pricing is "request pricing" — [FitGap](https://us.fitgap.com/products/paperless-parts); [Capterra](https://www.capterra.com/p/179259/paperlessPARTS/). Uptool from $195/month for small shops (page not pinned; surfaced alongside [Capterra job shop software](https://capterra.com/job-shop-software/)).
- Marketplace route: Xometry had 4,996 Active Suppliers at 31 Dec 2025 (+17% year on year) and a record 35.7% marketplace gross margin in Q3 2025. — [CIMdata, Q4 2025 release](https://www.cimdata.com/en/industry-summary-articles/item/29521-xometry-reports-record-fourth-quarter-and-strong-full-year-2025-results); [Barchart, Q3 2025](https://www.barchart.com/story/news/35886037/xometry-reports-record-third-quarter-2025-results)
- Job-shop ERP: JobBOSS implementation is "measured in months, not weeks" and "pricing is rarely transparent" (reseller). — [ERP Research JobBOSS](https://erpresearch.com/erp/jobboss)
- A mid-size distributor executive says order entry is the company's top AI use: customer PDFs are read for PO number, quantity and item number, and reps no longer key those orders (archived interview, date not confirmed). — [Distribution Strategy archive](https://archive.distributionstrategy.com/?p=6067)

### Inferences
- The staffing-agency pattern matters: distributors already pay an outside firm (Robert Half, Insight Global) a marked-up hourly rate for order entry. "Paying an outsider per hour for order entry" is an accepted purchase.
- Offshore labour at $5-$12/h vs US loaded $21-$34/h leaves a 2-4x labour gap. A human-in-the-loop service can price between the two.
- Xometry's roughly 36% marketplace margin shows what job shops give up when they let someone else win and price work for them (inference; not a take rate).

### Gaps
- No public price for Conexiom, Instalily, Endeavor, Comena, Proton, WizCommerce Ella or Y Meadows (see Q7).
- No source on how many distributors already use offshore staff for quoting or order entry.

---

## Q6. Proof: operator quotes and job posts with pay

### Takeaway
Job posts are plentiful and current (April-July 2026) and show the work is paid for as full-time roles. Genuine operator quotes are still thin; the best ones are vendor-hosted (Instalily) or from trade-press interviews (Distribution Strategy, Electrical Wholesaling, the Distribution At The Crossroads podcast). No Reddit, forum or G2 text was reachable.

### Cited Findings

Operator voice (P1)
- Chief commercial officer, national industrial distributor: "If you respond within an hour, your probability of getting the business is higher… It takes two hours, it drops." Reported median response time: three to four hours (vendor-hosted, undated). — [Instalily case study](https://instalily.ai/case-studies/quoting-speed)
- Small job-shop owner on software fit: "doesn't need this giant, expensive ERP system" (paraphrased in a search summary; page not pinned, surfaced with [Capterra job shop software](https://capterra.com/job-shop-software/)).
- Older survey (2017): 69% of inside salespeople spend under 10% of their time on proactive outbound calls, implying most of the day is reactive (quotes, orders). 75% of respondents were distributors, most with 1-10 branches. — [Distribution Strategy, 2017](https://distributionstrategy.com/2017/04/inside-sales-in-2017-survey-results/). MDM (2012): nearly half of respondents said inside reps proactively sell less than 10% of the time. — [MDM, 25 May 2012](https://www.mdm.com/2012/05/25/)

Operator voice (P2)
- Mid-size distributor executive (Distribution Strategy interview): order entry is the top AI use. Orders arrive as PDF attachments, AI pulls PO number, quantity and item number, and reps do not do data entry for these orders (date unconfirmed). — [Distribution Strategy archive](https://archive.distributionstrategy.com/?p=6067)
- Distribution At The Crossroads podcast (host Nick Pericle), episode with Ben Albu, 30 March 2026: the host argues order-entry automation is the most overlooked high-ROI AI application for distributors. — [Audible listing](https://www.audible.com/es_US/podcast/Distribution-At-The-Crossroads/B0FTP1RM2M)
- Electrical Wholesaling podcast with Canals CEO Michael Delgado (June 2026): AI for order entry, RFQs and AR/AP at electrical distributors (vendor CEO). — [EW podcast](https://www.ewweb.com/business-management/e-biz/podcast/55387937/how-ai-can-help-electrical-distributors-save-time-and-money); [Canals blog](https://www.canals.ai/blog/how-ai-can-help-electrical-distributors-save-time-and-money)
- National Fluid Power Association article "Crawl, walk, run with AI: from order entry to quoting to pricing" (title only, undated). — [NFPA](https://www.nfpa.com/news/crawl-walk-run-with-ai-from-order-entry-to-quoting-to-pricing)
- Conexiom Capterra review (first round): "A bit pricey but understandable…" — see lens03.

Job posts with pay (US unless stated; posted ranges, 2026 unless stated)

| Title | Employer / place | Pay | Link |
|---|---|---|---|
| Inside Sales Rep (remote) | OneSource Distributors (Sonepar), Fullerton CA | $27-$35/h (reported Jan 2026; URL ID suggests Oct 2025) | [career.com](https://www.career.com/job/onesource-distributors/inside-sales-representative/j202510230009116148919) |
| Inside Sales Rep | OneSource, San Francisco | $28-$37/h | same search; page not pinned |
| Inside Sales Rep | Crescent Electric Supply, Joliet IL (May 2026) | $62,076-$85,193 (Salary.com estimate shown on post) | [career.com](https://www.career.com/job/crescent-electric-supply-company/inside-sales-representative/j202604272035516503495) |
| Inside Sales | Exco Electric / All Current, Houston TX | $56,100-$77,100 | [All Current](https://careers.ebscoind.com/allcurrent/job/Houston-Inside-Sales-TX-77020/1405158700/) |
| Inside Sales (electrical distributor quoting) | Insight Global, Chesapeake VA | $47K-$57K base + $9K-$12K commission | [Insight Global](https://jobs.insightglobal.com/find_a_job/virginia/job-486748) |
| Inside Sales (electrical distributor quoting) | Insight Global, National City CA | est. $50K-$75K | [Insight Global](https://jobs.insightglobal.com/find_a_job/california/job-534489/) |
| Inside Sales Rep (technical sales) | Consolidated Electrical Distributors (PayScale avg) | $32,362 base (looks low; treat cautiously) | [PayScale](https://www.payscale.com/research/US/Job=Inside_Sales_Representative/Salary/ef006601/Consolidated-Electrical-Distributors-Inc.-Technical-Sales) |
| CNC Machinist/Estimator | Schaumburg IL (posted 5 May 2026) | $80,000 target | [career.com](https://www.career.com/job/cnc-machine-shop/cnc-machinist-estimator/j202605050702057048470) |
| Estimator | Actalent, Bloomington MN | $70,000-$75,000 | [career.com](https://www.career.com/job/actalent/estimator/j202604180555052797508) |
| Estimator (contract machining) | Prince Industries, Pepperell | $55,000-$65,000 | [Workable](https://apply.workable.com/prince-industries-llc/jobs/view/2BBD8F42C9.md) |
| Manufacturing Estimator (ProShop ERP) | Yeager Manufacturing, Winter Park FL | not shown | [career.com](https://www.career.com/job/yeager-manufacturing-technologies/manufacturing-estimator/j202606170249332631169) |
| Estimator (UK) | Gi Group, Nottingham | £27,000-£45,000 | [Gi Group](https://uk.gigroup.com/job-offer-detail/nottingham-nottinghamshire-estimator/5305694156167/) |
| Estimator (UK) | Entech, Woking; also Burntcommon | £45,000 (+ bonus at Entech) | page not pinned among [CV-Library](https://www.cv-library.co.uk/job/225199894/Estimator) and [Jobbird](https://www.jobbird.com/uk/job/25570421-estimator) |
| Order Entry Specialist (contract) | Robert Half, Bethlehem PA | $23-$26/h | [Hire Heroes](https://jobs.hireheroesusa.org/jobs/558691601-order-entry-specialist-at-robert-half) |
| Order Management Specialists (Sage) | Insight Global, Portland OR | $19-$24 or $20-$25/h | [Insight Global](https://insightglobal.com/jobs/find_a_job/oregon/portland/order-management-specialists/job-529276/) |
| Order entry (creates POs in ERP), contract-to-hire | Itasca IL | $20-$24/h | page not pinned (search set above) |
| Order entry (ERP/CRM such as SAP, Oracle) | Arlington Heights IL | $21-$26/h | page not pinned |
| Order Entry Specialist I (distributed products) | Baton Rouge LA | $16.75-$21.75/h | page not pinned (candidate [snagajob](https://www.snagajob.com/jobs/1265976294)) |
| Technical order entry (ERP) | Orlando FL | $16.25-$21.25/h | page not pinned |
| CS / Order Entry Specialist | Empire Distributing (posted ~6 Apr 2026) | not captured | [career.com](https://www.career.com/job/empire-distributing/customer-service-order-entry-specialist/j202604061402294941899) |
| "Sales order" US average | ZipRecruiter (4 Jun 2026) | $19.88/h (range $16.35-$22.84) | [ZipRecruiter](https://www.ziprecruiter.com/Jobs/Sales-Order/3) |

### Inferences
- US 2026 pay bands: order entry $16-$26/h; distributor inside sales about $47K-$85K (some hourly at $27-$37/h); estimator $55K-$80K. UK estimator £27K-£45K.
- Live "order entry specialist" and "inside sales – quoting" postings are a ready-made prospect signal: each one marks a company paying for this exact work right now (see Q13).
- Halal flag: "Empire Distributing" may be a wine-and-spirits wholesaler (the name matches one in the US Southeast; not verified). It shows that order-entry job searches will surface alcohol distributors, which should be screened out.

### Gaps
- No Reddit, Facebook group, G2 or Capterra complaint text (fetch blocked; no forum results surfaced).
- Distribution Talks and MDM podcast episodes on these topics were not found or heard.
- No operator quote from a small job-shop owner about losing a job to a slow quote, other than vendor case studies.

---

## Q7. Who else sells a fix, at what price, to what size, and how crowded

### Takeaway
Both problems are crowded at the software layer, and prices are almost all quote-only.
- P1 distributor quoting: enterprise-funded (Instalily, nearly $100M raised; Proton; Endeavor). Small distributors are thinly served.
- P1 job-shop quoting: mature, with a long tail of priced tools (Paperless Parts, AMFG, DigiFabster, Uptool from $195 a month, CloudNC, SpecSync).
- P2: the most crowded. At least 15 named vendors, ERP partner tie-ups (Conexiom with Epicor P21, Eclipse and Kinetic), an OrderScan tier "from $100", and vendor ROI math down to $1.50 per order.
- ERP-native AI (P21, NetSuite, Acumatica) does not yet read unstructured emailed POs. Partners fill that gap.

### Cited Findings

P1: distributor quoting
- InstaLILY: Series A $25M (August 2025, led by Insight Partners). Series B $60M (14 July 2026, led by Energize Capital, with Insight, Home Depot Ventures and United Rentals). Nearly $100M raised; revenue up 5x in a year. Distribution customers: SRS Distribution, Imperial Brady, SunSource, Parts Town, Copper State Bolt & Nut, TricorBraun, Radwell, Harrington Process Solutions. Price not public. Target: large distributors (inference from logos). — [MDM, $60M](https://www.mdm.com/news/technology/ai/instalily-raises-60m-launches-ai-engineer-for-enterprise-operations/); [MDM, $25M](https://mdm.com/news/technology/ai/ai-powered-distributor-automation-platform-instalily-raises-25m-in-funding/); [Distribution Strategy, Aug 2025](https://distributionstrategy.com/2025/08/instalily-ai-raises-25-million-to-scale-industry-specific-ai-agents/)
- InstaLILY hired a former association executive to lead distribution expansion (August 2026). — [Distribution Strategy, Aug 2026](https://distributionstrategy.com/2026/08/instalily-hires-former-association-executive-to-lead-distribution-expansion/)
- Proton.ai "Order & Quote Entry AI": no public prices; early access and white-glove onboarding for high-volume distributors. — [Proton.ai](https://www.proton.ai/quote-and-order)
- Endeavor (San Francisco): $7M seed led by Craft Ventures, with Heartland Ventures, Contrary, BoxGroup and executives from Palantir and AWS. Automates order entry, quoting, invoice matching and supply-chain workflows for manufacturers and distributors. Date conflict: CB Insights says 31 Oct 2024; a job page cites a 14 Oct 2025 news item. It hires "Forward Deployed Engineers". No price found. — [CB Insights](https://www.cbinsights.com/company/endeavor-6/financials); [Business Insider India](https://businessinsider.in/tech/news/endeavor-is-using-ai-to-modernize-manufacturing-check-out-the-9-slide-deck-it-used-to-raise-a-7-million-seed-round-/slidelist/114822920.cms); [Simplify job post](https://simplify.jobs/p/40e2fdfc-acb5-47d6-8840-3499fd5901c8/Forward-Deployed-Engineer)
- Canals (electrical distributors): AI for order entry, RFQs and AR/AP; price not found. — [Electrical Wholesaling podcast](https://www.ewweb.com/business-management/e-biz/podcast/55387937/how-ai-can-help-electrical-distributors-save-time-and-money)
- Docket: the "Docket" behind the speed-to-quote blog appears to be a Seattle AI "virtual sales engineer" startup (GeekWire 2023: raised $5.35M per an SEC filing). A "DocketAI" shows a $15M Series A (26 Jul 2024, led by Mayfield; single unverified source). It is not a manufacturing-specific quoting engine, and whether the two are the same company is unconfirmed. No price found. — [GeekWire, 2023](https://www.geekwire.com/2023/entrepreneur-who-sold-last-startup-to-zoominfo-is-raising-cash-for-new-seattle-ai-startup/); [Raising.fi](https://raising.fi/company/docketai)
- CPQ tools (general, not distributor-specific): $10-$150 per user per month list prices; implementation often exceeds first-year subscription (see Q5). — [ERP Research DealHub](https://erpresearch.com/erp-add-ons/cpq/dealhub-cpq/pricing); [IBISWorld](https://img2.ibisworld.com/united-states/procurement/cpq-software/31275394)
- ERP-native (P21): Epicor's generative assistant and "Item Advisor" have been available to cloud P21 customers since May 2025, with agentic features from May 2026. These are cloud-only and do not process unstructured emailed POs (third-party guide). — [Airdev, P21 AI](https://www.airdev.co/erp/prophet-21/ai)
- ERP-native quoting in Infor, Eclipse and Acumatica: not found (no search budget left to check each).

P1: job-shop quoting
- Paperless Parts: $30M Series B (13 Sep 2021, led by OpenView); no later round found. Targets job shops and contract manufacturers. Pricing request-only now; $300 and $750/month tiers date from 2019. — [Business Wire, 2021](https://www.businesswire.com/news/home/20210913005163/en/Paperless-Parts-Announces-30M-Series-B-Funding-Led-by-OpenView-Partners); [FitGap](https://us.fitgap.com/products/paperless-parts)
- AMFG: "estimates parts in 90 seconds" with "+/- 10% accuracy" (vendor claim). — [AMFG job shop page](https://www.amfg.ai/job-shop)
- DigiFabster AI Quote Agent: "80% less time on quotes" (vendor claim). — [DigiFabster](https://digifabster.com/products/ai-quote-agent/)
- CloudNC: an AI CNC estimating product (vendor). — [CloudNC](https://cloudnc.com/news-room/new-ai-solution-launched-to-accelerate-the-cnc-machining-estimating-process-and-eliminate-quoting-bottlenecks)
- SpecSync: launched March 2026 at Work Truck Week for custom-manufacturing quoting, with a Wabash National partnership. — [BriefGlance](https://briefglance.com/articles/specsync-launches-ai-platform-to-overhaul-custom-manufacturing-quoting)
- Uptool: from $195/month for small shops (page not pinned).
- IMTS article "Quote Us: AI for Faster, Better Quotes" (title only). — [IMTS](https://www.imts.com/read/article-details/Quote-Us-AI-for-Faster-Better-Quotes/2253/type/Read/1)
- Xometry-style marketplaces: 4,996 active suppliers; 35.7% marketplace gross margin (Q3 2025). — [CIMdata](https://www.cimdata.com/en/industry-summary-articles/item/29521-xometry-reports-record-fourth-quarter-and-strong-full-year-2025-results); [Barchart](https://www.barchart.com/story/news/35886037/xometry-reports-record-third-quarter-2025-results)

P2: order capture
- Conexiom: quote-only, no free trial. Priced as an annual SaaS fee per trading partner, a per-document fee, or a mix, with a one-off setup fee. FitGap lists a "Professional" tier with up to 12,000 captured documents a month (price not published). The "$1/user/year" directory listings are placeholders. Epicor partnership covers Prophet 21, Eclipse and Kinetic (Airdev dates the announcement to 14 Jul 2026, unconfirmed). — [ERP Research](https://erpresearch.com/erp-add-ons/distribution/conexiom/pricing); [SpotSaaS](https://www.spotsaas.com/product/conexiom/pricing); [FitGap](https://us.fitgap.com/products/conexiom); [Conexiom Epicor partnership](https://info.conexiom.com/epicor-partnership); [Epicor partner directory](https://prep.epicor.com/en/partners/isv-partners/directory/industry-category/distribution/conexiom)
- Epicor also has an older "AutoOrder" module listed as a P21 option. — [Epicor partner directory](https://prep.epicor.com/en/partners/isv-partners/directory/industry-category/distribution/conexiom)
- Y Meadows: custom, usage-based monthly subscription. Its ROI calculator shows $1.50 per order vs $17.50 manual (vendor projection, not a list price). — [Y Meadows FAQ](https://www.ymeadows.com/en/faq/); [Y Meadows ROI calc](https://www.ymeadows.com/en/roi-calc); [ZoftwareHub](https://zoftwarehub.com/products/y-meadows/pricing)
- WizCommerce Ella: launched about 29 May 2026. Connects to NetSuite, QuickBooks, SAP and Microsoft Dynamics, with "most ERP connections live within the first two weeks". Implementation is included in the subscription; no price published. WizCommerce has announced an $8M raise. — [WizCommerce](https://wizcommerce.com/product/ai-order-entry-software/); [Distribution Strategy, June 2026](https://distributionstrategy.com/2026/06/wizcommerce-launches-ai-order-entry-tool-for-distributors/); [TechIntelPro](https://techintelpro.com/news/wizcommerce-launches-ella-ai-order-entry-tool)
- Comena (Munich, YC S25): reads POs and RFQs from email, PDF and Excel; matches free text to SKUs; pushes to the ERP "with or without human review"; targets industrial distributors and manufacturers (fastener and MRO example); customers in the US and Germany. Funding conflicts: $130K, $500K, or a $2.5M seed in April 2026. "Six-figure ARR added in the last month" (one profile). Price not found. — [YC launch](https://www.ycombinator.com/launches/O3U-comena-ai-agents-that-automate-order-processing-for-distributors-and-manufacturers); [NeuronFeed](https://neuronfeed.com/startups/comena); [Standout](https://standout.work/companies/comena-gmbh)
- Other named order-entry vendors: Canals AI, Ordermatic, Esker, Fluent, Enlighten.Net (WizCommerce's comparison list) — [WizCommerce blog](https://wizcommerce.com/blog/best-ai-order-entry-software-for-epicor/). Also Proton.ai — [Proton](https://www.proton.ai/quote-and-order) — and Airbricks OrderPilot for NetSuite (co-founder post) — [LinkedIn](https://linkedin.com/in/jleipzig).
- Priced order-entry tools: OrderSync "from $1,000/month plus per-order fees" — [SourceForge](https://sourceforge.net/software/product/OrderSync/); OrderScan "starts at $100", usage-based — [SourceForge](https://sourceforge.net/software/product/OrderScan/).
- NetSuite and Acumatica native AI: no built-in feature found for creating sales orders from emailed PDFs; third-party add-ons fill the gap:
  - Anchor Group NetSuite Sales Order Automation app — [Anchor Group](https://www.anchorgroup.tech/products/netsuite-sales-order-automation-app)
  - IIG "PO Recognition – PDF Extract" on the Acumatica Marketplace (listing from 2021) — [Acumatica Marketplace](https://www.acumatica.com/acumatica-marketplace/information-integration-group-po-recognition-pdf-extract)
  - Artsyl webinar on AI sales-order capture for Acumatica (March 2026) — [Artsyl](https://www.artsyltech.com/events/AI-Automation-Sales-Order-and-Invoice-Processing-for-Acumatica)
- Food distribution (first round, lens09): Pepper ($50M Series C), Anchr ($5.8M), Burnt (about $3.8M seed). Not re-searched.
- Lace: Lace AI (Bulgaria/US) raised $19M in total ($14M seed, April 2025), but it is call analytics for home services (HVAC, plumbing, roofing), not order entry. No order-entry company named "Lace" was found. — [bne IntelliNews](https://intellinews.com/bulgaria-s-fastest-growing-startup-lace-ai-raises-19mn-in-seed-funding-377918); [citybiz](https://www.citybiz.co/article/686168/lace-ai-raises-14m-seed-funding/)

### Inferences
- Crowding:
  - P2 is very crowded: more than 15 vendors, two priced under $1,000 a month, ERP-partner bundling under way, and YC seeds.
  - P1 distributor quoting is crowded at the enterprise end (Instalily and Proton) but thin below about $100M revenue.
  - P1 job-shop quoting has mature software, but the tools assist the estimator rather than replace them.
- Customer size targeted:
  - Instalily: large distributors (SRS, Radwell, Parts Town).
  - Conexiom: mid and large (per-trading-partner pricing, setup fees, a 12,000-document tier).
  - WizCommerce Ella and OrderScan reach down to small firms (QuickBooks connection; from $100).
  - Comena: mid-market industrial.
  - Paperless Parts: job shops of most sizes.
- Minimum contract sizes are not public for any vendor. The only floors found are OrderSync's $1,000 a month, DealHub's 5-user minimum and OrderScan's $100 entry.
- Endeavor's "Forward Deployed Engineer" hiring signals heavy services work in delivery, which is the same model as a human-in-the-loop service. That makes it a competitor for the service, not just the software.

### Gaps
- No public price or minimum for Instalily, Proton, Endeavor, Comena, Conexiom, Ella, Y Meadows, Canals or Paperless Parts (current).
- Infor CloudSuite Distribution, Epicor Eclipse, Acumatica and Sage 100 native AI quoting or order capture: not verified.
- Paperless Parts' and Docket's own benchmark reports: not found.

---

## Q8. Will the problem grow or shrink as AI gets better over the next 24 months?

### Takeaway
P2 shrinks as a paid service. Extraction and SKU mapping are becoming cheap software features, already reaching QuickBooks-level customers and ERP partner directories. Only exception handling and posting into legacy, API-less ERPs stays human. P1 holds up better. Better models will cut the reading and matching work, but the price and margin decision, supplier special pricing and drawing-based cost judgment keep a human accountable. Buyers' own AI may also send more RFQs to more suppliers, which raises the premium on speed.

### Cited Findings
- P2 commoditisation signals:
  - Ella connects to QuickBooks with ERP connections live in two weeks — [WizCommerce](https://wizcommerce.com/product/ai-order-entry-software/)
  - OrderScan from $100 — [SourceForge](https://sourceforge.net/software/product/OrderScan/)
  - $1.50 per order vendor projection — [Y Meadows](https://www.ymeadows.com/en/roi-calc)
  - Conexiom inside Epicor's partner directory — [Epicor](https://prep.epicor.com/en/partners/isv-partners/directory/industry-category/distribution/conexiom)
  - Epicor shipped cloud generative and agentic features in 2025-2026, not yet for unstructured POs — [Airdev](https://www.airdev.co/erp/prophet-21/ai)
- P2: the typical AI workflow still stages a draft order "that a person approves before posting". — [Airdev](https://www.airdev.co/erp/prophet-21/order-import). Comena runs "with or without human review". — [NeuronFeed](https://neuronfeed.com/startups/comena)
- P1: AMFG's ±10% estimating accuracy claim shows machine estimates are still approximate. — [AMFG](https://www.amfg.ai/job-shop). Paperless Parts' own engineers describe why automated estimation of machined parts is hard. — [Medium](https://medium.com/paperless-parts-tech-blog/why-automated-estimation-of-machined-parts-is-hard-2ab0d0e4af6f)
- P1: Instalily raised $60M in July 2026 and launched an "AI engineer for enterprise operations", so funded players are moving fast at the top end. — [MDM](https://www.mdm.com/news/technology/ai/instalily-raises-60m-launches-ai-engineer-for-enterprise-operations/)

### Inferences
- P2, 24 months:
  - The labour per order falls 70-90% (vendor claims of 20 minutes down to under 2).
  - What remains is unknown part numbers, price disputes, partial-ship rules, phone and voicemail orders, and green-screen or on-prem ERPs without an API.
  - A service priced per order will face software at $1-$2 per order. The defensible version is "guaranteed same-day, accurate entry plus exception chasing" for legacy-ERP shops, not keying.
- P1, 24 months:
  - Line matching and stock checks for catalogue items become near-automatic.
  - Project bids, substitutes, supplier special-pricing requests and job-shop cost judgment remain.
  - The human checker's role shifts from building quotes to approving and defending them. Value shifts from labour saved to win rate.
  - Risk: buyer-side AI may flood suppliers with RFQs (inference, no source), raising volume but cutting win rates per quote.

### Gaps
- No source measured AI accuracy on distributor RFQs or PO extraction independently.
- No source on buyer-side AI procurement agents sending structured orders (which would shrink P2 further).

---

## Q9. How to reach these buyers

### Takeaway
The channels competitors are already using:
- Trade press: MDM, Distribution Strategy Group, Electrical Wholesaling.
- Associations: Instalily hired a former association executive to lead distribution.
- ERP partner directories: Epicor ISV directory, Acumatica Marketplace, NetSuite SuiteApp partners.
- Podcasts: Distribution At The Crossroads, Electrical Wholesaling.

Associations with known membership counts: ISA (145 distributors and 225 manufacturers, 1,400+ US locations; undated) and NAED (4,263 member locations in 2007). For job shops: NTMA (publishes "The Record", with a "2025 By the Numbers" section), PMA and FMA (counts not found).

### Cited Findings
- ISA: members include 225 manufacturers and 145 distributors across 1,400+ US locations (undated media kit). — [Multiview ISA media kit](https://mediakitpublic.multiview.com/ISA); [ISA about](https://www.isapartners.org/about)
- NAED: 4,263 member locations and about 75,000 distributor employees (NAED database, April 2007; 2007). — [Wikipedia](https://en.wikipedia.org/wiki/National_Association_of_Electrical_Distributors)
- NAW: about 250,000 wholesale distribution companies across North America (NAW SmartBrief text, June 2026). MDM's 2026 Top Distributors List covers 220+ North American distributors across 20 categories. — [NAW SmartBrief copy](https://politicalemails.org/messages/2293786/html_body)
- NTMA: The Record, Feb/Mar 2026 issue, includes "How NTMA delivered in 2025" and "2025 By the Numbers" (member count not visible in the snippet). — [NTMA The Record PDF](https://ntma.org/wp-content/uploads/2026/03/The-Record-February_March_2026.pdf)
- NFPA (fluid power) publishes AI order-entry and quoting content for its members. — [NFPA](https://www.nfpa.com/news/crawl-walk-run-with-ai-from-order-entry-to-quoting-to-pricing)
- Media and podcasts:
  - MDM — [MDM Instalily coverage](https://www.mdm.com/news/technology/ai/instalily-raises-60m-launches-ai-engineer-for-enterprise-operations/)
  - Distribution Strategy Group — [Distribution Strategy](https://distributionstrategy.com/2026/06/wizcommerce-launches-ai-order-entry-tool-for-distributors/)
  - Electrical Wholesaling podcast — [EW](https://www.ewweb.com/business-management/e-biz/podcast/55387937/how-ai-can-help-electrical-distributors-save-time-and-money)
  - Distribution At The Crossroads — [Audible](https://www.audible.com/es_US/podcast/Distribution-At-The-Crossroads/B0FTP1RM2M)
  - Industrial Distribution (ISA member reports) — [inddist.com](https://www.inddist.com/associations/news/13769481/isa-members-are-in-growth-mode)
- ERP partner marketplaces:
  - Epicor ISV partner directory, distribution category (Conexiom listed) — [Epicor](https://prep.epicor.com/en/partners/isv-partners/directory/industry-category/distribution/conexiom)
  - Acumatica Marketplace (IIG PO Recognition) — [Acumatica](https://www.acumatica.com/acumatica-marketplace/information-integration-group-po-recognition-pdf-extract)
  - NetSuite partner apps (Anchor Group) — [Anchor Group](https://www.anchorgroup.tech/products/netsuite-sales-order-automation-app)
- Events: IMTS publishes AI-quoting content — [IMTS](https://www.imts.com/read/article-details/Quote-Us-AI-for-Faster-Better-Quotes/2253/type/Read/1). SpecSync launched at Work Truck Week 2026 — [BriefGlance](https://briefglance.com/articles/specsync-launches-ai-platform-to-overhaul-custom-manufacturing-quoting)

### Inferences
- Channels named in the brief but not verified this session (background knowledge; check dates and terms before use):
  - PTDA (power transmission distributors)
  - AIM (not identified with confidence; possibly AIM/R, an independent manufacturers'-representatives group)
  - PMA (Precision Machined Products Association)
  - FMA and its FABTECH show
  - NAW Distribution Executive Summit
  - The Prophet 21 and Eclipse user groups
  - Infor and Sage 100 VAR networks
- Best wedge channel (inference): ERP VARs and consultants for P21, Eclipse, Sage 100, Acumatica and NetSuite. They already sell add-ons into exactly these accounts and earn from referrals. Partner directories show that AI order-capture vendors are listed there.

### Gaps
- Current member counts for NAED, NAW (direct members), PTDA, NTMA, PMA and FMA: not found.
- 2027 event dates (NAED National, ISA convention, FABTECH, IMTS 2026 already held in September 2026): not verified.

---

## Q10. Roughly how many US companies have this problem

### Takeaway
Job shops: about 16,600-18,000 US machine shops (IBISWorld, VerticalIQ, First Research; 2025 estimates; Census CBP not reachable). Distributors: NAW says about 250,000 wholesale distribution companies across North America (2026). The 2002 Economic Census counted 260,445 employer establishments in NAICS 423 durable-goods wholesale. A size-band count from SUSB was not retrievable. By my assumption-driven estimate, about 25,000-40,000 US durable-goods wholesalers have 20-499 employees, the band where both problems bite.

### Cited Findings
- Machine shops (NAICS 33271/332710): IBISWorld 16,627 businesses in 2025 (an earlier edition said 16,710) — [IBISWorld](https://www.ibisworld.com/united-states/number-of-businesses/machine-shop-services/645/). VerticalIQ about 17,100 companies, 259,000 workers, $44.7B revenue — [VerticalIQ](https://verticaliq.com/product/machine-shops). First Research (Nov 2025) about 18,000 establishments (page not pinned; candidate [BVR](https://www.bvresources.com/articles/aid/90171)). These are modelled estimates, not Census counts.
- Durable-goods wholesale (NAICS 423): 260,445 employer establishments and about 3.36M paid employees (2002 Economic Census, archived; 2002). — [Census 2002 archive](https://webarchive.library.unt.edu/eot2008/20090507022842/http:/www.census.gov/econ/census02/data/industry/E42.HTM)
- All wholesale (NAICS 42): IBISWorld shows 731,356 vs 748,139 businesses in 2026 in two versions with placeholder fields (unreliable). — [IBISWorld](https://www.ibisworld.com/industry-statistics/number-of-businesses/wholesale-trade-united-states/)
- North America: about 250,000 wholesale distribution companies (NAW, June 2026). — [NAW SmartBrief copy](https://politicalemails.org/messages/2293786/html_body)
- 35 distributors are on the 2025 Fortune 500 (the top end, which funded vendors target). — [MDM](https://www.mdm.com/article/featured/featured-blog/heres-where-distributors-rank-on-the-2025-fortune-500/)
- The Census CBP API was refused by the proxy (403) this session.

### Inferences
- Estimate, distributors (assumption-driven):
  - Take about 200,000-260,000 US durable-goods wholesale employer establishments (anchored on 2002's 260,445 and NAW's 250,000 for North America).
  - Assume about 12-15% are firms with 20-499 employees (assumption; SUSB not retrieved).
  - Result: about 24,000-39,000 firms. Industrial, electrical, MRO and building-products are a subset. NAICS 4236 (electrical), 4237 (hardware, plumbing, HVAC), 4238 (machinery and supplies) and 4233 (lumber and construction materials) plausibly hold about half (assumption), so about 12,000-20,000 target distributors.
- Estimate, job shops: about 17,000 machine shops. Excluding firms under 5 staff (assumption: about 40%) and ITAR/defense-heavy shops (unknown share; see Q12) leaves several thousand addressable. Fabrication shops (NAICS 332312/332322/332323) add more, but no count was found.
- Make-to-order manufacturers for P2 were not counted.

### Gaps
- Census CBP and SUSB 2022 counts by size band for NAICS 423 sub-sectors and NAICS 332710: not retrieved (API 403; search did not surface the tables). Exact table: SUSB 2022 "U.S., 6-digit NAICS by enterprise employment size".
- UK (ONS) and Australian (ABS) counts: not searched (budget).

---

## Q11. The strongest argument against this opportunity

### Takeaway
P1: pricing is the distributor's or shop's core judgment and most guarded data. Owners rarely hand margin decisions to outsiders. An offshore team cannot touch defense-related drawings (ITAR), and well-funded players are moving fast at the top. P2: it is turning into a cheap software feature (from $100 a month; $1.50 per order vendor projection; ERP partner bundles), so a services margin gets squeezed within 24 months.

### Cited Findings
- P1: funded enterprise competitor with association-led distribution push — [MDM](https://www.mdm.com/news/technology/ai/instalily-raises-60m-launches-ai-engineer-for-enterprise-operations/); [Distribution Strategy](https://distributionstrategy.com/2026/08/instalily-hires-former-association-executive-to-lead-distribution-expansion/)
- P1 job shops: ITAR treats release of controlled drawings to foreign persons, including by email, screen-share or portal login, as an export. — [Cofactr](https://www.cofactr.com/articles/a-practical-guide-to-itar-compliance-for-manufacturers-and-engineers); [ITAR consultant blog](https://itarconsultant.pages.dev/blog/why-itar-applies-to-small-machine-shops-a-complete-guide/)
- P1 job shops: estimating depends on the most experienced people on the shop floor (vendor). — [CloudNC](https://cloudnc.com/news-room/new-ai-solution-launched-to-accelerate-the-cnc-machining-estimating-process-and-eliminate-quoting-bottlenecks)
- P2: cheap and bundled options exist:
  - OrderScan from $100 — [SourceForge](https://sourceforge.net/software/product/OrderScan/)
  - Ella with a QuickBooks connector — [WizCommerce](https://wizcommerce.com/product/ai-order-entry-software/)
  - Conexiom through Epicor — [Epicor partner directory](https://prep.epicor.com/en/partners/isv-partners/directory/industry-category/distribution/conexiom)
  - Y Meadows' $1.50 per order projection — [Y Meadows](https://www.ymeadows.com/en/roi-calc)
- P2: "why order automation still feels manual even when you've automated it" (lens03, Advantive). This cuts both ways: exceptions persist, which supports a human-in-the-loop service.

### Inferences
- P1: the service can only prepare the quote. The client's own rep must still press send on price. Value is speed and win rate, which is harder to prove than labour saved, and sales cycles will be long.
- P2: the buyer can buy software at $1-$2 per order. A service must justify itself on accuracy guarantees, legacy-ERP posting and exception chasing.
- Combined view (inference): P2 works best as the low-risk wedge (easy ROI proof, payroll-visible), with P1 the higher-value upsell to the same buyer.

### Gaps
- No churn or failure data for any order-entry or quoting vendor.

---

## Q12. Delivery constraints for an offshore (non-US) team

### Takeaway
- ERP access is workable but per-client: browser or cloud ERPs (cloud P21, NetSuite, Acumatica) are easy; on-prem legacy ERPs (Eclipse, Sage 100, JobBOSS, Dynamics GP) need VPN, RDP or Citrix logins that the client controls.
- Export control is the hard line: ITAR job shops and CMMC/CUI holders must be excluded unless the team is US persons.
- Timing: same-day, within-the-hour quoting and same-day order entry mean the team must work US business hours. That is a night shift from South Asia.

### Cited Findings
- ITAR:
  - Foreign nationals without US permanent residency, including employees on H-1B or L-1 work visas, are generally "foreign persons" needing a license or exemption to access ITAR technical data. Accidental disclosure still counts as a violation. — [PreVeil](https://www.preveil.com/blog/top-itar-questions/)
  - A release to a foreign national inside the US is a deemed export, and "the physical location of the data is irrelevant". — [Mondaq deemed-export guide](https://webiis10.mondaq.com/unitedstates/export-controls-trade-investment-sanctions/1111630/guide-to-foreign-person-deemed-export-licenses); [ITAR consultant](https://itarconsultant.pages.dev/blog/why-itar-applies-to-small-machine-shops-a-complete-guide/)
  - Technical data includes CAD models, drawings, CNC programs, inspection records and process specs. Disclosure can be "an email, a shared CAD model, a drawing review, a screen-share, a supplier portal login". — [Cofactr](https://www.cofactr.com/articles/a-practical-guide-to-itar-compliance-for-manufacturers-and-engineers); [NFFS](https://www.nffs.org/news/itar-fundamentals-what-every-foundry-should-know)
  - Example: a Canadian machine shop's $390 quote was passed over because releasing the technical data package abroad would need State Department authorization. — [Cofactr](https://www.cofactr.com/articles/a-practical-guide-to-itar-compliance-for-manufacturers-and-engineers) (page not fully pinned)
  - Foreign-national managers with ERP access to controlled drawings are a named risk. — [ITAR consultant](https://itarconsultant.pages.dev/blog/why-itar-applies-to-small-machine-shops-a-complete-guide/)
- CMMC is separate: it governs how Controlled Unclassified Information (CUI) is protected in systems. ITAR governs who can access data, and CMMC alone does not satisfy ITAR. — [PreVeil](https://www.preveil.com/blog/top-itar-questions/); [JD Supra on outsourcing sensitive manufacturing](https://jdsupra.com/legalnews/outsourcing-manufacturing-of-sensitive-2607936)
- ERP access:
  - P21's AI features are "cloud-only", showing P21 runs in both cloud and on-prem forms — [Airdev](https://www.airdev.co/erp/prophet-21/ai)
  - JobBOSS deployments take months — [ERP Research](https://erpresearch.com/erp/jobboss)
  - Order-entry job posts name Sage, SAP, Oracle and Dynamics — [Insight Global](https://insightglobal.com/jobs/find_a_job/job-529276)
  - Offshore order-form work is "commonly treated as safe to send to a vetted provider", with 98% field-accuracy terms (outsourcing vendor) — [Outsource Accelerator](https://www.outsourceaccelerator.com/glossary/data-entry/)
- Timing: "If you respond within an hour… two hours, it drops" (P1) — [Instalily](https://instalily.ai/case-studies/quoting-speed). 67% of buyers expect a quote in under 24 hours (lens05, Paperless Parts webinar, vendor).

### Inferences
- Segment rule: exclude any job shop that is DDTC-registered or ITAR/CMMC-bound, or that quotes defense or aerospace prints. Exclude distributors' defense-contract quote desks too. Commercial job shops (EAR99 parts) and industrial, electrical and MRO distributors are the deliverable segment.
- EAR caveat (background knowledge, unverified): some commercial technical data carries an ECCN, and EAR licence needs depend on the destination country's country-group listing. Pakistan, for example, appears in several restrictive EAR country groups, and many Pakistani entities are on the Entity List. A US export-control lawyer should confirm before any drawing or technical-data work is routed to a Pakistan-based team. Plain commercial price lists and PO data are generally not technical data (inference).
- Shift math (estimate): US Central business hours of 8am-5pm CDT (UTC-5) equal 6pm-3am in Pakistan (UTC+5). In winter (CST, UTC-6) they equal 7pm-4am. Eastern hours run one hour earlier. Same-day work needs a night shift or a split shift, or a US/Latin America overlap person.
- Access model (inference): each client gives named user logins (VPN or RDP for on-prem; browser for cloud), MFA on client devices, and least-privilege roles (for example, P2 can create but not approve orders; P1 can draft but not release quotes). An NDA plus data-processing terms will be needed because customer price files are commercially sensitive.

### Gaps
- No source on whether P21, Eclipse or Sage 100 licence terms allow third-party or offshore users or bots, or on per-user licence costs the client would bear.
- EAR treatment of job-shop drawings for Pakistan-based staff: not researched (background only).
- UK and Australian export-control equivalents (UK Export Control Order; Australian Defence Trade Controls Act): not researched.

---

## Q13. Where to find 15 named prospects within 14 days

### Takeaway
The fastest public source is live job postings for "order entry specialist", "customer service – order entry" and "inside sales – quoting" at distributors. Each is a company paying for the work now. Then add association directories (ISA has 145 distributor members; NAED, NTMA, PMA), ERP partner case-study pages, and peers of the logos that funded vendors announce. Buyer titles: VP Sales or Inside Sales Manager (P1 distributor), Owner/President or Estimating Manager (P1 job shop), VP Operations or Customer Service Manager (P2).

### Cited Findings
- Job-post sources already showing distributor hiring for this work:
  - OneSource Distributors (Sonepar) — [career.com](https://www.career.com/job/onesource-distributors/inside-sales-representative/j202510230009116148919)
  - Crescent Electric Supply — [career.com](https://www.career.com/job/crescent-electric-supply-company/inside-sales-representative/j202604272035516503495)
  - Exco Electric / All Current — [All Current](https://careers.ebscoind.com/allcurrent/job/Houston-Inside-Sales-TX-77020/1405158700/)
  - Insight Global electrical-distributor clients (unnamed) — [Insight Global](https://jobs.insightglobal.com/find_a_job/virginia/job-486748)
  - Robert Half and Insight Global order-entry clients (unnamed) — [Robert Half](https://jobs.hireheroesusa.org/jobs/558691601-order-entry-specialist-at-robert-half)
  - ZipRecruiter "Order Entry" and "Sales Order" listings — [ZipRecruiter Order Entry](https://www.ziprecruiter.com/Jobs/Order-Entry/3)
- Job shops hiring estimators:
  - Schaumburg IL CNC shop — [career.com](https://www.career.com/job/cnc-machine-shop/cnc-machinist-estimator/j202605050702057048470)
  - Prince Industries — [Workable](https://apply.workable.com/prince-industries-llc/jobs/view/2BBD8F42C9.md)
  - Yeager Manufacturing Technologies — [career.com](https://www.career.com/job/yeager-manufacturing-technologies/manufacturing-estimator/j202606170249332631169)
- ISA member base (145 distributors, 1,400+ US locations) — [ISA media kit](https://mediakitpublic.multiview.com/ISA). MDM 2026 Top Distributors List (220+ firms; mostly large) — [NAW SmartBrief copy](https://politicalemails.org/messages/2293786/html_body).
- Competitor logos show the type of buyer, though they are taken accounts. Their peers are prospects:
  - Instalily: Copper State Bolt & Nut, Harrington Process Solutions, SunSource — [MDM](https://www.mdm.com/news/technology/ai/instalily-raises-60m-launches-ai-engineer-for-enterprise-operations/)
  - WizCommerce: Howard Elliott — [WizCommerce story](https://wizcommerce.com/customer-stories/howard-elliott-order-entry-automation/)
- ERP partner pages listing order-capture partners (whose own customer stories name distributors) — [Epicor ISV directory](https://prep.epicor.com/en/partners/isv-partners/directory/industry-category/distribution/conexiom); [Acumatica Marketplace](https://www.acumatica.com/acumatica-marketplace/information-integration-group-po-recognition-pdf-extract)

### Inferences
14-day plan (inference):
- Days 1-3: pull 40 live US postings for "order entry specialist" and "inside sales" plus "quote" at NAICS 4236/4237/4238 distributors from Indeed and ZipRecruiter. Screen out alcohol, food-with-alcohol and firearms distributors.
- Days 3-6: cross-check against the ISA and NAED member directories and Epicor P21/Eclipse customer-story pages. Find the VP Sales or VP Operations on LinkedIn.
- Days 5-10: for job shops, use the NTMA and PMA member directories and ThomasNet "CNC machining" listings in two or three states. Exclude any shop that advertises ITAR registration or AS9100 defense work.
- Days 10-14: shortlist 15 with a named contact.

Do not use Paperless Parts' or Conexiom's case-study customers as prospects: they already have tools. Use them only to understand the profile.

### Gaps
- Not done: an actual list of 15 named prospects. The search budget ran out, and job boards and directories could not be opened.
- ThomasNet, NTMA "find a member", PMA directory and FABTECH exhibitor-list URLs and access terms: not verified.

---

## Q14. Pricing shapes buyers already accept

### Takeaway
Buyers in this space already pay in five ways:
- Per seat per month (CPQ, $10-$150 per user per month; Paperless Parts' 2019 tiers of $300-$750 a month).
- Per document or per order, or per trading partner per year (Conexiom, OrderScan, OrderSync's $1,000 a month base plus per-order fees, Y Meadows' usage-based subscription).
- Per hour or FTE through staffing agencies and BPOs ($5-$26 an hour).
- A marketplace margin on each job (Xometry, about 36%).
- A salary for in-house staff.

A monthly retainer with a per-order or per-quote overage fits all of these.

### Cited Findings
- Per seat:
  - DealHub about $65-$100/user/month, 5-user minimum — [ERP Research](https://erpresearch.com/erp-add-ons/cpq/dealhub-cpq/pricing)
  - CPQ benchmark $63.1/user/month — [IBISWorld](https://img2.ibisworld.com/united-states/procurement/cpq-software/31275394)
  - CPQing $78/user/month — [Capterra](https://www.capterra.com/p/10014422/CPQing/)
- Flat monthly tiers: Paperless Parts $300 and $750/month (2019) — [FitGap](https://us.fitgap.com/products/paperless-parts); Uptool from $195/month (page not pinned).
- Per trading partner per year, per document, or a mix, plus setup — [SpotSaaS](https://www.spotsaas.com/product/conexiom/pricing); [ERP Research](https://erpresearch.com/erp-add-ons/distribution/conexiom/pricing)
- Base plus per order: OrderSync from $1,000/month plus per-order fees — [SourceForge](https://sourceforge.net/software/product/OrderSync/)
- Usage-only: OrderScan from $100 — [SourceForge](https://sourceforge.net/software/product/OrderScan/)
- Usage-based monthly subscription: Y Meadows ("predictable monthly subscription pricing based on usage"; $1.50/order ROI projection) — [Y Meadows FAQ](https://www.ymeadows.com/en/faq/); [ROI calc](https://www.ymeadows.com/en/roi-calc)
- Subscription with implementation included: WizCommerce Ella — [WizCommerce](https://wizcommerce.com/product/ai-order-entry-software/)
- Hourly outsourced: staffing-agency order entry $19-$26/h (Robert Half, Insight Global) — [Robert Half](https://jobs.hireheroesusa.org/jobs/558691601-order-entry-specialist-at-robert-half). Offshore $5-$12/h, and per-document pricing for OCR queues — [Outsource Accelerator](https://www.outsourceaccelerator.com/glossary/data-entry/)
- Marketplace margin: Xometry 35.7% marketplace gross margin (Q3 2025) — [Barchart](https://www.barchart.com/story/news/35886037/xometry-reports-record-third-quarter-2025-results)

### Inferences
P2 price (estimate):
- Software anchors are $1.50 per order (Y Meadows projection) and $8-$17.50 manual (vendor figures).
- A service at $2-$4 per order with a monthly minimum fits. Example: 1,300 orders/month × $3 = $3,900/month, against an estimated $2.7K-$14.7K/month in labour (Q4).
- The minimum monthly fee covers setup, customer cross-reference building and exception handling.

P1 price (estimate):
- Per-quote pricing ties fee to volume, not wins. Suggested shape: a monthly retainer for a defined quote capacity with a same-day SLA, plus a per-quote overage. Distributor example: 600 quotes/month at about $8-$15 per quote = $4,800-$9,000/month, against an estimated $9.4K-$15.6K/month in labour plus lost GP (Q4). Job-shop example: 80 quotes/month × $25-$40 = $2,000-$3,200/month.
- A win-based or success fee is untested in this market (no source found). Avoid it until a client's baseline win rate can be measured.

### Gaps
- No public evidence of buyers paying per quote to an outside firm (other than marketplaces).
- No data on minimum contract lengths (annual vs monthly) for these tools.

---

## Halal / ethics flags (applies across questions)
- Screen out: alcohol (beer, wine, spirits) wholesalers (NAICS 4248, which also turn up in "order entry" job searches; see the Empire Distributing example, unverified); foodservice distributors whose lines are alcohol-centred (Pepper, Anchr and Burnt serve foodservice, so check the line mix); and firearms, ammunition or gambling-equipment distributors (inside NAICS 4239).
- Defense and weapons job shops: ITAR-controlled work is also often weapons-related, a possible ethical question for the end client. It is excluded anyway for offshore delivery (Q12).
- No interest-based lending, gambling or adult content was found in the core industrial, electrical, MRO or building-products segments. Distributors may run trade credit or floor-plan financing, but that is not part of these tasks.
- No rulings given; flag for a scholar where relevant.

## Remaining gaps (summary)
1. Census CBP/SUSB size-band counts for NAICS 423x and 332710 (API blocked; search did not surface tables).
2. Public prices or minimums for Instalily, Proton, Endeavor, Comena, Conexiom, Ella, Y Meadows, Canals, and current Paperless Parts.
3. ERP-native AI quoting or order capture in Infor, Eclipse, Acumatica, Sage 100 and NetSuite (only P21 partly checked).
4. Independent win-rate-vs-speed data for distributors and job shops (all vendor).
5. Forum, Reddit and G2 operator quotes; Distribution Talks and MDM podcast episodes.
6. ERP licence terms for third-party or offshore users; EAR exposure for a Pakistan-based team.
7. UK and Australian counts, channels and competitors (only UK estimator pay found).
8. Fifteen actual named prospects (method given; list not built).
