# Deep dive 01: Problem cards for (P1) retailer deductions and compliance fines against CPG brands, and (P2) AI-faked damage photos and fraudulent refund claims in e-commerce

Research date: 27 October 2026. US first, then UK and Australia. USD.

**Method and limits (read first).**
- This round used all 30 allowed web searches. One WebFetch test failed (supplypike.com, DNS ENOTFOUND). A direct curl to the Census API (api.census.gov) was refused by the egress proxy with a 403. So **every finding below comes from search-result summaries**, not from opened pages. Treat every number as "reported by" the cited page. Spot-check before publishing.
- The first-round notes (lens02 for P1, lens06 for P2) are not repeated here. Where I build on them, I say "(lens02)" or "(lens06)".
- Labels used:
  - **Vendor claim**: the number comes from a company that sells a fix.
  - **Estimate**: my own math, with the working shown.
  - **Inference**: my reasoning, not sourced.
  - **Prior knowledge, not re-verified**: background knowledge that I could not check this session.
- Reddit and forum threads were not reached. One query aimed at Reddit returned only trade-press and vendor pages. So operator quotes come from trade press, founder content and job posts, not forums.
- When a search summary did not clearly tie a fact to one URL, I give the most likely URL and mark it "URL not confirmed".

---

## Q1. The exact task, in plain words

### Takeaway
- **P1:** Every week, an AR or deductions person logs into each retailer and distributor portal. They pull the short-pay or deduction lines and match each one to the PO, invoice, bill of lading, proof of delivery and promo agreement. They decide whether it is valid. If it is not, they file a dispute with evidence before the deadline, then chase and post the repayment.
- **P2:** Every day, a customer-service agent opens each "item arrived damaged or defective" claim. They look at the photos or video and check the order, the customer's history and any reused or AI-made images. Then they approve, deny, or ask for more proof (live video, or a return) before issuing a refund or replacement.

### Cited Findings
#### P1
- A real job post from a small brand describes the task. True Sea Moss is hiring a "Distributor Deductions and Chargeback Specialist (UNFI / KeHE)". The duties are "monitoring the portals, validating every charge against source documents, disputing what isn't owed". The role is part-time to start (~15–20 hrs/week), contract/1099, remote — [Djinni job post](https://djinni.co/jobs/831947-distributor-deductions-and-chargeback-special/)
- UNFI pays invoices net of deductions and codes each one by family. The deduction comes with a code, so the clerk's first step is to sort by code.
  - 01: shortages
  - 02: pricing discrepancies
  - 05: unsaleables and damages
  - 10–12: advertising and promo, including manufacturer chargebacks (MCBs) and off-invoice promotions
  - 30 and above: compliance and logistics fees
  - Shortages are the family most often reported as invalid.
  - The guide sorts every charge into outcomes such as "disputable" (it cites a rule you did not break, or the distributor's own records contradict it) and "valid, fix upstream".
  - Source: [Endless Commerce playbook, KeHE and UNFI deductions](https://endlesscommerce.com/playbook/kehe-and-unfi-deductions-codes-and-clocks/) (vendor content).
- Walmart deductions split into two streams:
  - AR-side chargebacks, which are penalties Walmart says the supplier owes (for example OTIF fines).
  - AP-side deductions, which withhold payment on an invoice.
  - Carbon6's RecoveryPro disputes 13 deduction types, including carton shortages and pricing mismatches.
  - Source: [Business Wire, Carbon6 RecoveryPro launch, 17 Sep 2024](https://businesswire.com/news/home/20240917341442/en); [SPS Commerce: Walmart supplier deductions](https://www.spscommerce.com/community/articles/walmart-supplier-deductions)
- Portal filing step: iNymbus's DeductionsXchange "uploads denied claim packets into retail vendor portals" using cloud robotic automation — [Slashdot listing](https://slashdot.org/software/p/iNymbus/)
- Walmart Retail Link is the supplier portal for compliance scorecards, purchase orders, AP disputes and supplier agreements. It is gated to suppliers with an approved 9-digit Vendor Number — [8th & Walton, May 2026](https://www.8thandwalton.com/blog/what-is-retail-link-for)

#### P2
- Many merchants decide refunds from photos without ever seeing the item. AI tools can create plausible fake damage images that "pass online inspections, especially by automated refund systems" — [Practical Ecommerce](https://practicalecommerce.com/ai-makes-refund-evidence-easier-to-fake)
- Loop's return-policy tool includes a customer photo-upload step. Its fraud tools are blocklists and return-eligibility rules. So the photo is collected, but a human still has to judge it — [Loop vs Redo (vendor page)](https://www.loopreturns.com/compare/loop-vs-redo); [LateShipment roundup](https://www.lateshipment.com/alternatives/loop-returns/)
- In shipping-protection claims ("arrived damaged" or "not received"), Corso scores each claim on eight factors before it is resolved:
  - media reuse (whether earlier photos or videos appear again in other claims)
  - device fingerprinting
  - IP patterns
  - a cross-check against Shopify order data
  - Vendor description. Source: [Corso shipping protection](https://www.corso.com/shipping-protection)

### Inferences
- P1 is batch work that runs to a deadline (days to weeks). P2 is queue work with a customer waiting (hours to a day). That difference shapes offshore delivery (see Q12).
- In P1 the evidence lives in the brand's own systems (ERP, 3PL, carrier POD) and in retailer portals. In P2 the evidence is the customer's photo plus Shopify order history, so the AI step is image forensics plus pattern matching.

### Gaps
- No screen-by-screen walkthrough of the UNFI or KeHE supplier portals was found. The Kroger, Costco and regional-grocer dispute steps were not researched this round.

---

## Q2. Who feels it (job title) and who approves the money (job title)

### Takeaway
- **P1:** The work is done by a Deductions Specialist or Analyst, AR Specialist, or a part-time contractor at small brands. It is approved by the founder or CEO at brands under about $10M, and by the Controller, VP Finance or (fractional) CFO above that.
- **P2:** The work is done by CX agents, the CX or Returns Manager, or a "Returns, Fraud and Abuse" analyst at large retailers. It is approved by the Head of CX, the COO or the founder. At mid-market brands the CEO may notice it personally.

### Cited Findings
#### P1
- At a small brand the founder hires directly: True Sea Moss posted a 1099 contract role for UNFI/KeHE deductions — [Djinni](https://djinni.co/jobs/831947-distributor-deductions-and-chargeback-special/)
- C.A. Fortune (remote, USA, about $45K–$50K): "Some of our clients are seeking a dedicated Deductions Specialist to assist them with managing, reconciling, and clearing deductions." It requires CPG deductions experience, and UNFI and/or KeHE experience is a plus — [Built In Charlotte](https://builtincharlotte.com/job/deductions-specialist/8318357); [RemoteFirstJobs](https://remotefirstjobs.com/companies/ca-fortune/jobs/deductions-specialist-680582)
  - C.A. Fortune is a CPG sales and marketing agency (prior knowledge, not re-verified). So agencies staff this role on behalf of brand clients.
- At large CPG the role sits inside the trade-promotion team. Keurig Dr Pepper's "Deductions Specialist – Trade Promotion" (Frisco, TX) is hybrid, 3 days in the office — [KDP careers](https://careers.keurigdrpepper.com/fr-ca/emploi/frisco/deductions-specialist-trade-promotion/42849/77034168640)
- "Deductions Analyst" remote listings, reviewed 21 Oct 2026, ask for 2–4 years in CPG or trade promotion. One requires local presence in Coppell, TX — [Virtual Vocations](https://www.virtualvocations.com/job/deductions-analyst-3310826-i.html)
- SPS publishes an "ROI calculator to justify deduction management tools to your CFO". That shows the vendor's view that the CFO approves the spend (vendor content) — [SPS Commerce](https://www.spscommerce.com/community/articles/justify-deduction-management-tools-roi-calculator)

#### P2
- Boll & Branch's CEO, Scott Tannen, personally spotted a $489 sheet-set claim. The "torn" fabric did not match how cotton frays, and one image carried an AI watermark. He posted about it on LinkedIn — [eCommerce Fastlane, Apr 2026](https://ecommercefastlane.com/ai-generated-fakes-shopify-merchants-2026/); original coverage in Modern Retail (lens06)
- Large retailers have dedicated teams:
  - Abercrombie & Fitch "Associate Analyst, Returns", posted 3 May 2026, Columbus OH, hybrid. The team covers returns, fraud losses and policy abuse — [Swooped](https://swooped.co/job-postings/associate-analyst-returns-af-co-columbus-aampf-management-co-00476). The related posting says "The Returns, Fraud, and Abuse department is dedicated to safeguarding customer trust and business integrity" — [RemoteFirstJobs](https://remotefirstjobs.com/companies/abercrombie-and-fitch-co/jobs/associate-analystfraud-loss-abuse-739115)
  - Walmart Marketplace "Manager, Returns – Fraud and Abuse", with KPIs such as refund rates and fraud cancellations — [Walmart careers](https://careers.walmart.com/us/jobs/WD2118571-manager-technology-operations-business-analysis-and-insight-mp-fraud-and-abuse)
  - Chewy "Associate Director, Returns Abuse", covering a $180M+ portfolio (listing removed July 2025) — [Built In](https://builtin.com/job/sr-program-manager/6267733)

### Inferences
- In P1 the pain and the budget sit in finance. In P2 the pain sits in CX, but the budget sits with ops or the founder. At mid-market brands CX teams are rarely given a fraud budget, which makes P2 harder to sell (inference).
- Dedicated returns-fraud roles appear only at very large retailers (A&F, Walmart, Chewy). That fits a gap at mid-market brands, but it also suggests mid-market brands do not yet feel the problem is big enough to staff.

### Gaps
- No survey of who approves deduction-recovery or returns-fraud spend was found.

---

## Q3. How often it happens and how many hours it eats (math shown)

### Takeaway
- **P1:** Weekly, tied to every remittance. One real small-brand job post budgets **15–20 hours a week** for UNFI/KeHE deductions alone. My estimate for a $20M brand is about 6–30 hours a week, depending on deduction size and evidence quality.
- **P2:** Daily. For a $20M-GMV DTC brand I estimate about 1.5–10 hours a week of photo-claim review. The AI-faked share is unknown per brand.

### Cited Findings
#### P1
- About 15–20 hrs/week (part-time to start) for UNFI/KeHE deductions at one brand — [Djinni, True Sea Moss](https://djinni.co/jobs/831947-distributor-deductions-and-chargeback-special/)
- An AR clerk writes off anything under about $250, because "twenty minutes hunting for delivery paperwork costs more than the claim". This is one anecdote — probably [CallSphere blog](https://callsphere.ai/blog/retail-link-vendor-central-and-kehe-connect-have-no-export-button-now-.md) (an AI vendor), URL not confirmed.
- Per-deduction cost:
  - $200–$300 to fully research and resolve one deduction (lens02, Stealth Agents citing others).
  - $3.20–$5.00 per claim falling to about $1 when portal filing is automated (lens02, iNymbus case study). This is a vendor claim.
- Recovery falls from 80% to 20% as disputes near the 90-day mark (lens02, HighRadius, vendor claim). So cadence must be weekly, not monthly.

#### P2
- Ravelin 2026 (6,200+ consumers in the UK, Germany and France): 1 in 4 shoppers abused refund policies in the past year, with a 98% success rate. Vendor survey. — [BRC associate insight](https://brc.org.uk/news-and-events/news/associate-insight/2026/the-state-of-refund-abuse-repeat-offenders-eroding-loyalty-and-ais-impact/)
- 67% of merchants report receiving AI-generated fake refund evidence. Vendor survey, June 2026. — [The Paypers](https://thepaypers.com/fraud-and-fincrime/thought-leader-insights/ravelin-report-key-takeaways-global-fraud-trends-2026)
- Forter's CEO, Michael Reitblat, says AI-doctored refund claims rose by more than 15% globally since the start of the year. Vendor claim, December 2025. — [Dataconomy, 24 Dec 2025](https://dataconomy.com/2025/12/24/retailers-struggle-to-spot-ai-doctored-images-in-refund-requests)

### Inferences (estimates, math shown)
- **P1 estimate, $20M CPG brand:**
  - Deducted: $20M × 2–5% = $400K–$1M a year (lens02 vendor ranges). Mid-case: 3% = $600K a year.
  - Count: at an assumed average deduction of $300–$1,000, that is 600–2,000 deductions a year, or about 12–40 a week.
  - Time: at 30–45 minutes each (triage, evidence pull, portal filing, follow-up; assumption), that is **6–30 hours a week**.
  - The 15–20 hours a week in the True Sea Moss post falls inside this range.
- **P2 estimate, $20M-GMV DTC brand:**
  - Orders: $20M / assumed $100 AOV = 200K orders a year.
  - Claims: assume 1–3% of orders raise a photo-backed damage or defect claim. That gives 2,000–6,000 claims a year, or about 40–115 a week.
  - Time: at 2–5 minutes of review each, that is **about 1.5–10 hours a week**.
  - All inputs are assumptions, not sourced. Claim rates vary hugely by category; fragile, home and furniture goods are highest.

### Gaps
- No independent survey of hours spent per week on deductions or on damage-claim review.
- No per-brand rate of photo-based damage claims, or of the AI-faked share, was found.

---

## Q4. What it costs a typical company per month (math shown; estimates labelled)

### Takeaway
- **P1:** For a $20M brand, I estimate about **$5K–$21K a month** of invalid deductions written off or left unrecovered, plus about $1.9K–$2.7K a month of labour. At $5M revenue the leak shrinks to about $1K–$5K a month, which is too small for a big retainer.
- **P2:** For a $20M-GMV brand, I estimate AI-faked photo refund losses of about **$0.8K–$5K a month**. They are larger only in high-ticket categories. Industry-wide returns fraud and abuse is large ($100B by Appriss for 2025; about $76B by the NRF/Happy Returns method), but the photo-claim slice per brand is small.

### Cited Findings
#### P1
- SPS estimates about 6% of revenue deducted for Amazon suppliers, 5.8% for Walmart and 5% for Kroger, and 2–10% of annual revenue in recoverable deductions overall. Vendor claim, via search summary; URL tie not fully confirmed — [SPS Commerce, Q4 deductions Walmart vs Kroger](https://www.spscommerce.com/community/articles/retailer-deductions-in-q4-how-walmart-and-kroger-compare)
- SPS also says suppliers lose 5–7% of revenue to retailer chargebacks, and claims up to 75% of eligible deductions are reclaimed. Vendor claim. — [SPS deduction management](https://www.spscommerce.com/deduction-management/)
- SupplyPike says fines and fees can reach 12% of the amount billed to Walmart. The article is older and undated, and the URL was not confirmed in the snippet.
- Founder example (TeaSquares): an invoice of $32,000 to KeHE was paid out at $21,000 after deductions and fees. The founder says many deductions "are erroneously charged to brands, and it's up to them to contest it." — Foodbevy guide ([guide.foodbevy.com/?p=1150](https://guide.foodbevy.com/?p=1150) or [?p=747](https://guide.foodbevy.com/?p=747); snippet did not say which)
- Distributor fees: UNFI and KeHE take a 20–28% margin plus a 7–12% freight allowance (lens02, EightX).
- Labour price: C.A. Fortune Deductions Specialist, about $45K–$50K a year — [Built In Charlotte](https://builtincharlotte.com/job/deductions-specialist/8318357)

#### P2
- Appriss Retail, 2026 Total Retail Loss Benchmark (2025 data). Appriss sells returns-fraud software, so these are vendor claims.
  - $706B of merchandise was returned in 2025.
  - 14.2% (about $100B) was preventable loss from fraud and abuse: abuse 12%, fraud 2%.
  - Total retail loss was $796B.
  - Method: more than 1,000 consumers surveyed, plus 250M customer identifiers analysed.
  - Source: [Business Wire, 19 Feb 2026](https://www.businesswire.com/news/home/20260219293604/en/Appriss-Retail-Benchmark-Report-Uncovers-%24796B-in-Total-Retail-Loss); [Chain Store Age](https://chainstoreage.com/study-returns-shrink-totaled-nearly-800b-2025)
- **Conflict:** NRF and Happy Returns put 2025 returns at $849.9B with about 9% fraudulent (lens06). Range: about $76B–$100B in fraud plus abuse. The two studies define returns, fraud and abuse differently, so do not compare them directly.
- Single claims run to hundreds of dollars ($489 sheet set) — [eCommerce Fastlane](https://ecommercefastlane.com/ai-generated-fakes-shopify-merchants-2026/)
- AI fakes in expense receipts average about $100 each (lens06). This is a different domain; it is shown only as a size anchor.

### Inferences (estimates, math shown)
- **P1, $20M brand:**
  - Deducted: $600K–$1M a year = $50K–$83K a month.
  - Invalid share: 10–25% (lens02) = **$5K–$21K a month** of invalid deductions.
  - Labour: 15–20 hrs/week × $22–$24/hr ($45–50K / 2,080 hrs) × 1.3 loading × 4.33 weeks ≈ **$1.9K–$2.7K a month**.
- **P1, $5M brand:**
  - Deducted at 2–5%: $100K–$250K a year.
  - Invalid share: 10–25% = $10K–$62.5K a year ≈ **$0.8K–$5.2K a month**.
- **P1 fee pool at 20–25% contingency (hypothetical rate):**
  - Assume 60–75% of invalid dollars are won.
  - $20M brand: $5K–$21K × 0.6–0.75 × 0.2–0.25 ≈ **$600–$3.9K a month per client**.
  - $5M brand: about $100–$1K a month.
- **P2, $20M-GMV brand:**
  - Fakes: assume 5–10% of the 2,000–6,000 photo claims a year are AI-faked or AI-edited = 100–600 fakes.
  - Loss: at about $100 average = $10K–$60K a year ≈ **$0.8K–$5K a month**.
  - High-ticket brands (mattresses, furniture, electronics, luxury) scale this up roughly in line with AOV.
  - Fully assumption-based.

### Gaps
- There is no independent (non-vendor) benchmark of CPG deduction rates, and no Kroger, UNFI or KeHE invalid-rate data.
- No per-brand data on photo-claim fraud loss was found.

---

## Q5. How companies handle it today and what they pay (staff, contingency firms, software)

### Takeaway
- **P1:** Brands use in-house or part-time staff ($45K–$50K a year, or 15–20 hours a week of contract labour), SaaS, or contingency recovery firms. Visible SaaS prices:
  - SupplyPike: about $810 a month for suppliers with under $10M of Walmart sales.
  - Promomash: $349–$1,250 a month.
  - Glimpse: a small monthly fee plus a commission.
  - Carbon6: fee on recovered funds only.
  - No published contingency **percentage** for deductions was found.
- **P2:** CX agents eyeball photos. Returns apps ($23–$155 a month and up) collect photos and apply rules. Enterprise fraud vendors charge per transaction (Riskified about 0.4%). Video-capture apps cost $29–$99 a month. AI-image-detection APIs cost $0.0005–$0.04 per image. Dedicated human review exists only at big retailers.

### Cited Findings
#### P1
- **SupplyPike / SPS Commerce:**
  - "Deductions Navigator" at $810 a month for suppliers with under $10M of annual Walmart sales. Aggregator listing, updated 28 Apr 2026, single source — [SoftwareSuggest](https://www.softwaresuggest.com/supplypike)
  - The vendor says pricing is a flat rate based on business size and data volume — [SupplyPike enterprise](https://supplypike.com/enterprise)
  - Software Advice says it is an annual flat-rate fee per retailer — [Software Advice](https://www.softwareadvice.com/product/451076-SupplyPike)
  - TrustRadius lists no pricing — [TrustRadius](https://www.trustradius.com/products/supplypike/pricing)
- **iNymbus:**
  - No public pricing ("contact vendor") — [G2](https://www.g2.com/products/inymbus-deduction-management-software/pricing)
  - Rated 4.3/5 by 6 users — [GetApp UK](https://www.getapp.co.uk/software/2059775/inymbus)
  - Vendor case study: $1 per claim after an 80% cost cut — [casestudies.com](https://www.casestudies.com/company/inymbus/case-study/how-warner-brothers-reduced-deductions-and-chargeback-processing-costs-by-80)
- **Glimpse:**
  - "A modest commission on winbacks + small monthly software fee" — [SalesboxAI 2026 roundup](https://salesbox.ai/blog/top-deduction-management-platforms-2026); [Foodbevy roundup](https://www.foodbevy.com/?p=38999)
  - 25% off the first year for Foodbevy brands — [Foodbevy](https://www.foodbevy.com/?p=38999)
  - Risk-free trial and a 12-month audit look-back — [BevNET PR, 29 Oct 2025](https://www.bevnet.com/pr/2025/10/29/glimpse-and-presence-enter-into-strategic-partnership-to-bring-aipowered-deduction-management-to-cpg-brands)
  - Claims 4–5x average ROI, up to 33x (vendor claim)
- **Promomash:**
  - Capterra lists Seed $349 a month (600 events), Growth $599 a month (1,200 events) and Scale $1,250 a month (2,400 events), billed annually — [Capterra UK](https://www.capterra.co.uk/software/210477/promomash)
  - Software Advice says "starting $500/month" — [Software Advice](https://www.softwareadvice.com/trade-promotion-management/promomash-profile/)
  - Deduction management is a separate add-on, a turnkey service "with our team of experts".
  - **Conflict:** SalesboxAI calls $349–$1,250 the price of Promomash's deduction tooling, but Capterra frames those tiers as trade-promotion "events".
- **Vividly:** no public pricing. Tiers are based on functionality and integrations — [Gartner Peer Insights](https://www.gartner.com/reviews/product/vividly); [G2 compare](https://g2.com/compare/promomash-inc-promomash-vs-vividly)
- **Carbon6 RecoveryPro (Walmart 1P):**
  - Suppliers pay a fee only on funds recovered; the rate is not public — [Business Wire, Sep 2024](https://businesswire.com/news/home/20240917341442/en); [Carbon6](https://www.carbon6.io/?p=10055)
  - Claims $2B+ recovered across Walmart, Amazon and Target (vendor claim) — [Altss profile](https://altss.com/profile/carbon6)
- **Inmar DeductionsLink:** claims an "85–95% increase in recovery" of invalid deductions. Vendor claim; no pricing — [Inmar](https://www.inmar.com/expertise/martech/deductions-management)
- **BELAY Solutions (US virtual-staff firm):** offers a service that "tracks, manages, and disputes deductions incurred from your retailer and distributor relationships", with reports on deductions as a percent of revenue and dollars disputed versus repaid. No price found — [BELAY blog](https://blog.belaysolutions.com/service-spotlight-deductions-management)
- **HighRadius:** enterprise (Kraft Heinz case, lens02). Pricing not found.
- **"Cash Flow Mining-type" recovery firms:** a search for "Cash Flow Mining" returned nothing relevant. RevRecoup ("pure contingency", rate not stated) is in lens02.
- **Contingency % for deductions:** not found in two targeted searches. Anchors from adjacent markets (lens02): chargebacks 25% (Chargeflow), collections 25–35%.

#### P2
- **Forter:** custom, transaction-based pricing, not public. Lists "Abuse Prevention" for returns, promo and reseller abuse — [Chargeflow: Riskified vs Forter](https://www.chargeflow.io/es/blog/riskified-vs-forter) (competitor content)
- **Riskified:** pay-as-you-go from about 0.4% per transaction, no setup fees or monthly commitments (blog) — [Ringly](https://www.ringly.io/blog/riskified-alternatives)
- **Signifyd:** priced as a % of order value with a 100% chargeback guarantee. ERP Research says its returns-abuse detection is "not evidenced in public documentation" — [ERP Research](https://erpresearch.com/erp-add-ons/fraud-risk/forter-vs-signifyd)
- **Customer-size mix on G2 (small samples):**
  - Forter: 44.8% of reviews from mid-market
  - Riskified: 48.6% from mid-market
  - Signifyd: 52.1% from small business
  - Source: [G2 compare](https://www.g2.com/compare/forter-vs-signifyd-vs-riskified)
- **Loop:** from about $155 a month (roundup). Has photo upload, blocklists and eligibility rules — [LateShipment](https://www.lateshipment.com/alternatives/loop-returns/)
- **AfterShip Returns:**
  - From $23 a month for 60 returns; API on the Premium plan at $99 a month — [Refundid roundup](https://refundid.com/item/aftership-alternatives-for-ecommerce-returns)
  - Fraud checks (vendor claim): weight discrepancies, fake or expired tracking numbers, customer behaviour, item grading — [AfterShip vs Redo](https://www.aftership.com/compare/redo)
- **Redo:** pricing unclear across sources (per-order coverage fee, or tiered from about $23 a month) — [LateShipment](https://www.lateshipment.com/alternatives/redo/)
- **Narvar:** no returns-fraud or photo-forensics information surfaced in this round's searches (not found).
- **DamageProof (Shopify app):**
  - Asks customers for timestamped video instead of photos, with live capture that "prevents uploading AI-altered photo / video".
  - Free tier (5 most recent video claims); PRO $29 a month (unlimited claims); Enterprise $99 a month (third-party integrations).
  - Source: [Shopify App Store](https://apps.shopify.com/damageproof-io)
- **AI-image-forensics APIs:**
  - Apify actor: $5 per 1,000 detections — [Apify](https://apify.com/george.the.developer/ai-deepfake-detector/pricing)
  - Another Apify actor: $0.005 per image, listing insurance damage-photo screening as a use case
  - Winston AI via Eden AI: from $0.0145 per image — [Eden AI](https://www.edenai.co/expert-models/winstonai-ai-image-detection)
  - Resemble AI: from $0.04 per request — [Eden AI](https://www.edenai.co/expert-models/resemble-ai-image-detection)
  - Sightengine deepfake detection is also listed — [Eden AI](https://www.edenai.co/expert-models/sightengine-image-deepfake-detection)
  - SilverAI: about $0.0005 per image (URL not confirmed)
  - No accuracy or false-positive rates were published in the snippets.
- **Shipping protection (Corso, Route, Protega):**
  - Corso: claim-risk scoring including media reuse — [Corso](https://www.corso.com/shipping-protection)
  - Protega: AI fraud detection for fake "not received" claims — [ShipAid comparison](https://www.shipaid.com/blogs/shopify-app-comparisons/corso-vs-protega-post-purchase-care-comparison)
  - Route: AI-driven automatic claim resolution — [ATTN Agency, Mar 2026](https://www.attnagency.com/blog/route-shopify-review)
- **Logistics:** a UPS subsidiary introduced AI inspection technology for returns in the 2025 holiday season — [Dataconomy](https://dataconomy.com/2025/12/24/retailers-struggle-to-spot-ai-doctored-images-in-refund-requests); [PYMNTS](https://www.pymnts.com/?p=3529076)

### Inferences
- P1 buyers already pay three ways: SaaS ($349–$1,250+ a month), a blend (Glimpse), and pure success fees (Carbon6, RevRecoup). The market accepts paying on results.
- P2 buyers pay for software only. No done-for-you "claim review desk" with published pricing turned up. That is either a gap or a sign that buyers will not pay for it.

### Gaps
- Actual contingency percentages for deduction recovery (Carbon6, RevRecoup, SPS Revenue Recovery, Glimpse commission) were not found.
- HighRadius mid-market pricing, Narvar fraud features and Forter returns-abuse pricing were not found.

---

## Q6. Proof: real operator quotes, surveys and job posts (with links and dates)

### Takeaway
P1 has strong job-post proof, including small brands hiring offshore and part-time for UNFI/KeHE deductions, plus one founder account. P2 has strong survey proof (Ravelin, Appriss, Forter, all vendors) and one named CEO case. Its job posts sit only at large retailers.

### Cited Findings
#### P1
- **Job post (offshore, small brand):** True Sea Moss, "Distributor Deductions and Chargeback Specialist (UNFI / KeHE)", posted on Djinni. Djinni is a Ukraine-centred tech job board (prior knowledge, not re-verified). Part-time, ~15–20 hrs/week, 1099. Undated in the snippet; seen Oct 2026 — [Djinni](https://djinni.co/jobs/831947-distributor-deductions-and-chargeback-special/)
- **Job post (agency, on behalf of brands):** C.A. Fortune Deductions Specialist, remote USA, about $45K–$50K — [Built In Charlotte](https://builtincharlotte.com/job/deductions-specialist/8318357)
- **Job post (offshore, vendor's human-in-the-loop):** Glimpse is hiring Deductions Specialists in the Philippines (pay in PHP) "to act as the expert human-in-the-loop behind our AI-powered deductions platform" — [Indeed Philippines](https://ph.indeed.com/q-glimpse-jobs.html)
- **Job posts (mid and large CPG):**
  - Deductions Analyst, reviewed 21 Oct 2026 — [Virtual Vocations](https://www.virtualvocations.com/job/deductions-analyst-3310826-i.html)
  - Deductions Management Specialist, remote, entry level — [Built In](https://builtin.com/job/deductions-management-specialist/3641304)
  - Keurig Dr Pepper Deductions Specialist – Trade Promotion — [KDP](https://careers.keurigdrpepper.com/fr-ca/emploi/frisco/deductions-specialist-trade-promotion/42849/77034168640)
  - Trade Spend Specialist, $24+/hr, remote, Toronto — [TalentSphere](https://talentsphere.catsone.com/careers/26769-TalentSphere-Canada-USA/jobs/16550512-Trade-Spend-Specialist)
- **Founder account:** TeaSquares invoiced KeHE $32,000 and received $21,000 after deductions and fees. "Many of them are erroneously charged to brands, and it's up to them to contest it." — [Foodbevy guide](https://guide.foodbevy.com/?p=1150) (exact page among ?p=1150 / ?p=747 not confirmed)
- **Podcast:** Foodbevy episode 98, "Breaking Down Distributor Deductions and Chargebacks" — [Foodbevy](https://www.foodbevy.com/?p=29363)
- **Vendor-side opinion:**
  - SPS: distributors "sometimes impose these fees on the supplier in error" — [SPS Commerce](https://www.spscommerce.com/community/articles/disputing-distributor-deductions-and-chargebacks)
  - A consultant quoted saying suppliers are "forced to write off millions in invalid claims" (anecdotal) — [BriefGlance](https://briefglance.com/articles/the-hidden-billions-how-ai-audits-uncover-lost-revenue-for-suppliers)
- **Platform friction (headline only):** "Retail Link, Vendor Central and KeHE Connect have no export button now" — [CallSphere](https://callsphere.ai/blog/retail-link-vendor-central-and-kehe-connect-have-no-export-button-now-.md)

#### P2
- **Named operator:** Boll & Branch CEO Scott Tannen flagged an AI-faked $489 claim on LinkedIn — [eCommerce Fastlane, Apr 2026](https://ecommercefastlane.com/ai-generated-fakes-shopify-merchants-2026/). Bogg Bag also reported AI-falsified refund proof — [Practical Ecommerce](https://practicalecommerce.com/ai-makes-refund-evidence-easier-to-fake)
- **Surveys:**
  - Ravelin 2026: 65% of consumers say AI has made false refund claims easier, and 59% agree "AI supercharges refund abuse" — [Ravelin blog](https://ravelin.com/blog/ai-powered-refund-abuse-dispute-fraud)
  - UK consumers lead: 37% have engaged in or are considering refund abuse, vs France 33% and Germany 25% — [IT Brief UK](https://itbrief.co.uk/story/uk-shoppers-lead-europe-in-refund-abuse-study-finds)
  - 67% of merchants report receiving AI-generated fake refund evidence, and refund abuse now ranks above fraudulent chargebacks in negative impact (June 2026) — [The Paypers](https://thepaypers.com/fraud-and-fincrime/thought-leader-insights/ravelin-report-key-takeaways-global-fraud-trends-2026); [Crowdfund Insider, Jun 2026](https://www.crowdfundinsider.com/2026/06/286653-ravelin-report-finds-hope-challenge-in-merchant-fraud-fight/)
  - All Ravelin figures are vendor claims.
- **Incident records:**
  - Vinted and e-commerce AI-image refund fraud (2 Mar 2026) — [OECD AI](https://oecd.ai/en/incidents/2026-03-02-16b3)
  - AI fake product images for refund fraud (30 Aug 2025) — [OECD AI](https://oecd.ai/en/incidents/2025-08-30-db88)
  - Wired: "Scammers in China Are Using AI-Generated Images to Get Refunds" (Dec 2025) — [Wired](https://www.wired.com/story/scammers-in-china-are-using-ai-generated-images-to-get-refunds)
- **Job posts:**
  - A&F Associate Analyst Returns (3 May 2026) — [Swooped](https://swooped.co/job-postings/associate-analyst-returns-af-co-columbus-aampf-management-co-00476)
  - ESW eCommerce Fraud/Risk Analyst, Dublin; refund and returns abuse is a nice-to-have; removed 28 May 2026 — [Built In](https://builtin.com/job/ecommerce-fraud-analyst/9359937)
  - Inabia eCommerce Fraud Investigator/Analyst (O2C), Redmond WA, onsite, "U.S. citizen or green card holders only", investigating "new orders, upgrades, returns" — [CareerBuilder](https://www.careerbuilder.com/job-details/ecommerce-fraud-investigator-analyst-order-to-cash-o2c-redmond-wa--0c10d20a-79e7-4eee-80d1-4702969a9799)
  - Walmart Marketplace Manager, Returns Fraud & Abuse — [Walmart](https://careers.walmart.com/us/jobs/WD2118571-manager-technology-operations-business-analysis-and-insight-mp-fraud-and-abuse)
  - Veepee Warehouse Return Fraud Specialist (Spain) — [Lever](https://jobs.lever.co/veepee/388d98ce-6cef-466f-b83f-d4bcf50e6b16)

### Inferences
- P1 has buyer-side proof: brands pay people to do exactly this, including offshore. P2's proof is mostly attacker-side (consumer surveys) and enterprise-side (big-retailer roles). That is weaker evidence that mid-market brands will pay.

### Gaps
- No Reddit, r/shopify, r/ecommerce or CPG Slack quotes were reached.
- No 2026 Grocery Dive or Supply Chain Dive article on deductions turned up in the one trade-press query.

---

## Q7. Who else sells a fix, at what price, to what customer size, and how crowded it is

### Takeaway
- **P1 is crowded, and the exact proposed model is already taken.** Glimpse ($10M Series A, April 2025; 140–200+ brands) sells AI plus offshore human review for KeHE and UNFI emerging brands on a small monthly fee plus commission. SPS/SupplyPike, Carbon6, iNymbus, Inmar, Promomash, Vividly, HighRadius and ARPflow cover the rest. BELAY sells US virtual staff for the task.
- **P2 is moderately crowded at the software layer and empty at the service layer.** Enterprise fraud vendors charge per transaction. Returns apps and shipping-protection apps add rules and media-reuse checks. Cheap capture apps ($29–$99 a month) and per-image APIs undercut a pure detection service.

### Cited Findings
#### P1 (vendor, model, price, target size)
- **Glimpse:**
  - Model: monthly fee plus commission; built for KeHE and UNFI natural and specialty channels.
  - Customers: 140+ brands (Oct 2025 PR), with a later review citing 200+ — [BevNET PR](https://www.bevnet.com/pr/2025/10/29/glimpse-and-presence-enter-into-strategic-partnership-to-bring-aipowered-deduction-management-to-cpg-brands); [SalesboxAI](https://salesbox.ai/blog/top-deduction-management-platforms-2026)
  - Funding: $10M Series A, April 2025. This answers the lens02 date gap — [Food Industry Executive, Apr 2025](https://foodindustryexecutive.com/2025/04/glimpse-secures-10m-to-automate-deduction-management-for-cpg-brands/)
  - Staffing: Philippines-based human-in-the-loop specialists — [Indeed PH](https://ph.indeed.com/q-glimpse-jobs.html)
- **SPS Commerce / SupplyPike:** flat-rate SaaS; about $810 a month for suppliers with under $10M of Walmart sales (single aggregator). The SPS "Revenue Recovery" product claims $2B+ recovered — [SoftwareSuggest](https://www.softwaresuggest.com/supplypike); [SPS](https://www.spscommerce.com/deduction-management/)
- **Carbon6 RecoveryPro:** contingency, Walmart 1P first. Target, Home Depot and Costco were "in the works" at the Sept 2024 launch — [Business Wire](https://businesswire.com/news/home/20240917341442/en)
- **iNymbus:** RPA portal filing, quote-only; a review calls it pricier (lens02) — [G2](https://www.g2.com/products/inymbus-deduction-management-software/pricing)
- **Promomash:** trade-promotion SaaS from $349 or $500 a month, plus a deductions service add-on — [Capterra UK](https://www.capterra.co.uk/software/210477/promomash)
- **Vividly:** trade promotion plus deductions, quote-only — [Gartner](https://www.gartner.com/reviews/product/vividly)
- **Inmar DeductionsLink:** enterprise — [Inmar](https://www.inmar.com/expertise/martech/deductions-management)
- **HighRadius:** enterprise (Kraft Heinz; lens02)
- **ARPflow:** an AI platform for CPG deductions and disputes with 170+ clients in India. Its agents ingest data from email and retailer portals — [LinkedIn](https://www.linkedin.com/company/arpflow)
- **BELAY:** US virtual-staff service; price not found — [BELAY](https://blog.belaysolutions.com/service-spotlight-deductions-management)
- **Genpact–Advantage Solutions alliance:** AI and analytics to recover deductions. From a search summary; URL not confirmed (possibly [Outsource Accelerator](https://news.outsourceaccelerator.com/?p=70439))
- **Others named in lens02:** Doss, Endless Commerce, RevRecoup.
- **Settle partner directory:** lists Glimpse as a tech partner — [Settle](https://partners.settle.com/tech-partners/glimpse)

#### P2 (vendor, model, price, target size)
- **Forter, Riskified, Signifyd:** per-transaction or % of order value; enterprise and mid-market (G2 mix above). All claim returns-abuse modules — [G2](https://www.g2.com/compare/forter-vs-signifyd-vs-riskified); [Ringly](https://www.ringly.io/blog/riskified-alternatives)
- **Loop** (~$155+ a month), **AfterShip** ($23–$99+ a month) and **Redo** (unclear): returns workflow with photo upload and rules. None showed AI damage-photo detection in this round's results — [Loop](https://www.loopreturns.com/compare/loop-vs-redo); [AfterShip](https://www.aftership.com/compare/redo)
- **DamageProof:** video-capture claims, $0–$99 a month; small Shopify brands — [Shopify App Store](https://apps.shopify.com/damageproof-io)
- **Corso, Route, Protega:** shipping protection with built-in claim fraud scoring — [Corso](https://www.corso.com/shipping-protection); [ShipAid](https://www.shipaid.com/blogs/shopify-app-comparisons/corso-vs-protega-post-purchase-care-comparison)
- **AI-image-forensics APIs** (Winston AI, Resemble AI, Sightengine, Apify actors): $0.0005–$0.04 per image — [Eden AI](https://www.edenai.co/expert-models/winstonai-ai-image-detection); [Apify](https://apify.com/george.the.developer/ai-deepfake-detector/pricing)
- **Hyperverge:** an identity-verification vendor publishing on AI refund fraud, so a possible entrant — [Hyperverge blog](https://hyperverge.co/blog/ecommerce-ai-refund-blog/)
- **Switch Labs:** a playbook vendor (lens06).

### Inferences
- **P1 crowding: high.** The "long tail is unserved" thesis from lens02 is weakened. Glimpse targets exactly that tail (KeHE and UNFI) with exactly the AI plus offshore human model, and distributes through Foodbevy, PRESENCE and Settle. The remaining white space is probably:
  - regional grocers and Costco or club channels not yet automated
  - non-food CPG (beauty, household) selling through other distributors
  - brands that want a named human team that also fixes root causes (prevention), not just a dashboard
- **P2 crowding: medium for software, low for services.** But the cheap capture controls (video, live capture, media reuse) solve much of the problem without human review.

### Gaps
- Glimpse's actual fee and commission rates; Carbon6's contingency rate; Narvar's fraud features; any AI-photo-forensics vendor built specifically for e-commerce claims (none found besides capture apps and generic APIs).

---

## Q8. Will the problem grow or shrink as AI models improve over the next 24 months?

### Takeaway
- **P1:** The problem stays the same size. It is driven by retailer policies, not AI. But better AI shrinks the **service** margin: vendors such as Glimpse, ARPflow and iNymbus automate triage, evidence matching and portal filing. Human work narrows to judgment calls and retailer back-and-forth.
- **P2:** Attacks clearly grow. The share of human review may shrink as defence moves to capture controls (live video, media-reuse checks, content credentials) built into cheap apps.

### Cited Findings
#### P1
- Vendors are already pushing AI agents into the full loop. ARPflow's agents "ingest data from emails and retailer portals, validate each deduction, and autonomously manage disputes" — [ARPflow](https://www.linkedin.com/company/arpflow). Glimpse pairs AI with human-in-the-loop staff in the Philippines — [Indeed PH](https://ph.indeed.com/q-glimpse-jobs.html)
- Carbon6 planned to expand from Walmart to Target, Home Depot and Costco — [Business Wire](https://businesswire.com/news/home/20240917341442/en)
- Inmar argues service-based deduction firms "add people to a broken process", and says the shift is toward platforms (vendor opinion) — [Inmar blog](https://www.inmar.com/blog/insights/martech/how-automating-deductions-management-protects-margins)

#### P2
- Ravelin: 65% of consumers say AI makes false refund claims easier — [Ravelin](https://ravelin.com/blog/ai-powered-refund-abuse-dispute-fraud)
- Forter: AI-doctored claims rose more than 15% in 2025 (vendor claim) — [Dataconomy](https://dataconomy.com/2025/12/24/retailers-struggle-to-spot-ai-doctored-images-in-refund-requests)
- Inpainting damage onto a real photo "defeats whole-image detection" (lens06, Switch Labs). This pushes defence toward controlled capture: DamageProof live video at $29 a month — [Shopify App Store](https://apps.shopify.com/damageproof-io) — and media-reuse checks — [Corso](https://www.corso.com/shipping-protection)
- Headline: "80 per cent of retail fraud uses AI and returns abuse rising" (body not read) — [Home of Direct Commerce](https://homeofdirectcommerce.com/?p=58174)

### Inferences
- **P1:** AI makes it cheap to dispute $50–$250 deductions that are written off today, so recoverable volume per brand rises. But it rises for everyone, including SaaS vendors. A services firm must compete on price per recovered dollar and on coverage of messy portals. Window: 12–24 months before the long tail is productised (inference).
- **P2:** Better generators make photo review harder for humans as well as detectors. So the durable fix is policy (video, live capture, return-required thresholds), not review labour. A human review desk adds most value on high-value claims and on finding abuse rings across accounts.

### Gaps
- There is no neutral forecast of AI-generated refund fraud volume, and no data on whether retailers use AI to raise deduction volume.

---

## Q9. How to reach these buyers (associations, events, newsletters, podcasts, partners, marketplaces, communities)

### Takeaway
- **P1:** The best channels are the ones Glimpse already uses, which is both a validation and a warning:
  - Foodbevy (community and podcast)
  - BevNET
  - brokers such as PRESENCE
  - Settle's partner directory
  - Expo West (3,200+ exhibitors, 66,000 registrants in 2026)
  - CPG sales agencies (C.A. Fortune staffs deductions roles for brand clients)
  - Walmart supplier educators (8th & Walton)
- **P2:**
  - Shopify App Store
  - returns-platform and shipping-protection partner ecosystems (Loop, AfterShip, Corso)
  - DTC publications (Modern Retail, Practical Ecommerce, eCommerce Fastlane)
  - BRC associate content in the UK

### Cited Findings
#### P1
- Expo West 2026 (3–6 March, Anaheim): about 3,200 exhibitors and brands and 66,000 registered attendees — [New Hope, 8 May 2026](https://www.newhope.com/natural-products-expos/natural-products-expo-west-2026-numbers-data-certifications). Nearly two-thirds of attendees were qualified buyers — [TSNN](https://www.tsnn.com/trade-shows-conferences/natural-products-expo-west-2026-dished-up-health-conscious-product-launches-and-innovations)
- Foodbevy: community with a Glimpse discount (25% off the first year) and a podcast episode on distributor deductions — [Foodbevy roundup](https://www.foodbevy.com/?p=38999); [Foodbevy ep. 98](https://www.foodbevy.com/?p=29363)
- BevNET press releases, plus a Glimpse partnership with PRESENCE — [BevNET](https://www.bevnet.com/pr/2025/10/29/glimpse-and-presence-enter-into-strategic-partnership-to-bring-aipowered-deduction-management-to-cpg-brands). PRESENCE is a natural-products broker (prior knowledge, not re-verified).
- Settle tech-partner directory — [Settle](https://partners.settle.com/tech-partners/glimpse)
- 8th & Walton (Walmart supplier education; new-supplier checklist, June 2025) — [8th & Walton](https://www.8thandwalton.com/hubfs/8W%20Downloads/New%20Supplier%20Checklist/Walmart%20New%20Supplier%20Checklist%20-%20June%202025.pdf?hsLang=en)
- SPS Commerce community and "SupplyPike Fast Pitch" webinars (competitor-owned) — [SPS](https://www.spscommerce.com/community/unlock-your/supplypike-fast-pitch-winning-back-retailer-deductions)
- KeHE events (Trend Finder, "Golden Ticket" assortment slots for innovators) — [Progressive Grocer](https://progressivegrocer.com/node/67334); [Shelby Report, 2021](https://theshelbyreport.com/2021/05/26/kehe-reveals-golden-ticket-winners-from-trend-finder-event)
- C.A. Fortune (agency staffing deductions roles for clients) — [Built In Charlotte](https://builtincharlotte.com/job/deductions-specialist/8318357)
- Fractional CFO firms such as EightX (lens02).

#### P2
- Shopify App Store. DamageProof shows the category exists — [Shopify App Store](https://apps.shopify.com/damageproof-io)
- Returns and post-purchase platforms (Loop, AfterShip, Redo) and shipping protection (Corso, Route, Protega) — see Q7 URLs
- Publications:
  - eCommerce Fastlane (Shopify-focused) — [eCommerce Fastlane](https://ecommercefastlane.com/ai-generated-fakes-shopify-merchants-2026/)
  - Practical Ecommerce — [Practical Ecommerce](https://practicalecommerce.com/ai-makes-refund-evidence-easier-to-fake)
  - PYMNTS — [PYMNTS](https://www.pymnts.com/?p=3529076)
- UK: British Retail Consortium associate-insight channel (Ravelin publishes there) — [BRC](https://brc.org.uk/news-and-events/news/associate-insight/2026/the-state-of-refund-abuse-repeat-offenders-eroding-loyalty-and-ais-impact/)
- Also from lens06, not re-checked: Gorgias and Zendesk marketplaces, eTail, Shoptalk, NRF, IMRG.

### Inferences
- **P1:** Go where Glimpse does not yet reach:
  - regional-grocer and Costco suppliers
  - non-food CPG
  - CPG fractional-CFO and bookkeeping firms as white-label partners
  - NetSuite or QuickBooks partners serving CPG
  - Not verified this round: Nielsen/SPINS partner programmes, Grocery Dive, Startup CPG.
- **P2:** The most efficient route is a partnership or listing with a returns app or helpdesk, selling a "high-value claim review" add-on. Direct selling to brands is harder, because the buyer (CX) has no fraud budget.

### Gaps
- No pricing or membership data for Foodbevy, Startup CPG or NOSH. Partner-programme terms for Loop, AfterShip and Gorgias were not checked. Nielsen/SPINS partner ecosystems were not researched.

---

## Q10. Roughly how many US companies have this problem

### Takeaway
- **P1:** About 42,700 US food and beverage manufacturing establishments (2022). UNFI has about 10,000–11,000 suppliers and KeHE about 4,100 suppliers (8,500 brands). My estimate of the core addressable pool (brands of $2M–$100M selling to distributors or big-box retailers) is **about 3,000–6,000 brands**, excluding non-food CPG.
- **P2:** About 1.07M live US Shopify stores (Feb 2026). My estimate of brands large enough to buy a claim-review service ($5M+ GMV, physical goods with photo-claim exposure) is **about 5,000–20,000**, with low confidence.

### Cited Findings
#### P1
- 42,708 US food and beverage manufacturing establishments in 2022, per the Census County Business Patterns — [USDA ERS](https://www.ers.usda.gov/topics/food-markets-prices/processing-marketing/food-and-beverage-manufacturing)
  - California 6,569 (15%), Texas 2,898, New York 2,748.
  - 1.7M workers (2021).
  - Older comparison: in 2007, almost 30,000 plants were owned by about 24,500 companies — [ERS archive](https://webarchive.library.unt.edu/web/20170124182042/https://www.ers.usda.gov/topics/food-markets-prices/processing-marketing/manufacturing.aspx)
  - These are establishments (plants), not firms.
- UNFI: "nearly 10,000 suppliers", 11 owned brands and about 230,000 SKUs — [UNFI 2025 Impact Report](https://s205.q4cdn.com/522321978/files/doc_financials/2025/sr/2025_UNFI_Impact_Report.pdf). The investor deck says about 11,000 suppliers and about 250,000 SKUs as of 3 May 2025 — [UNFI July 2025 deck](https://s205.q4cdn.com/522321978/files/doc_presentations/2025/Jul/16/Introduction-to-UNFI-July-2025-FINAL.pdf). The 10-K says about 230,000 products — [SEC 10-K FY2025](https://www.sec.gov/Archives/edgar/data/1020859/000102085925000054/unfi-20250802.htm)
- KeHE: "over 4,100 suppliers and 8,500 brands" — [KeHE](https://kehe.com/brands). It reported 6,100 suppliers after the 2023 DPI acquisition — [Food Manufacturing](https://www.foodmanufacturing.com/supply-chain/news/22865377/kehe-distributors-completes-acquisition-of-dpi-specialty-foods). These conflict; the count method may differ.
- Third-party NAICS 311 "entity" counts (59,044 and 42,880) have no year or source given and are not reliable — [naics.com](https://www.naics.com/naics-code-description/?code=311); [naicslist](https://naicslist.com/naics/311)
- Census API: direct query blocked by the proxy (403). The exact 2023 CBP firm count was not retrieved.

#### P2
- Shopify store counts (secondary blogs citing StoreLeads and BuiltWith):
  - StoreLeads: 1,070,098 live US Shopify stores (updated 6 Feb 2026).
  - BuiltWith: 3,748,162 US Shopify sites, including dormant ones.
  - StoreLeads: 2,898,351 live stores globally (Q2 2026).
  - Sources disagree on the US share of merchants (44% vs 57%).
  - Source: [LinkMyBooks, 2 Mar 2026](https://linkmybooks.com/blog/how-many-sellers-are-on-shopify); [DemandSage](https://demandsage.com/shopify-statistics/); [Webtonic](https://www.webtonic.io/blog/e-commerce-shopify-statistics)

### Inferences (estimates)
- **P1 estimate:**
  - UNFI (~10–11K) and KeHE (~4.1K) suppliers overlap heavily (assumption), so there are perhaps 10,000–12,000 unique distributor-channel suppliers.
  - Assume 30–50% are in the $2M–$100M band where manual deductions hurt and HighRadius does not fit. That gives **3,000–6,000 brands**.
  - Add Walmart, Target and Kroger direct suppliers that are not in the distributor channel, plus non-food CPG (not counted). The upper bound could be about 2x.
- **P2 estimate:**
  - Take 1.07M live US stores. Assume 0.5–2% exceed $5M GMV (assumption; no source found). That gives about 5,000–21,000.
  - Only part of these sell goods where photo damage claims are common (home, apparel, accessories, electronics).
  - Low confidence.

### Gaps
- 2023 CBP or SUSB firm counts by NAICS (311, 312, 3256) could not be pulled (proxy 403). There is no Shopify revenue-band distribution from a primary source, and no Walmart, Target or Kroger supplier counts.

---

## Q11. The strongest argument against each opportunity

### Takeaway
- **P1:** A funded competitor already does exactly the proposed model for exactly the proposed long tail. Glimpse runs AI plus an offshore (Philippines) human-in-the-loop for KeHE and UNFI brands on a small monthly fee plus commission, with 140–200+ brands and distribution through Foodbevy, PRESENCE and Settle. And for brands under $10M, the recoverable dollars ($0.8K–$5K a month) leave a thin fee.
- **P2:** The per-brand loss is small (about $0.8K–$5K a month for a $20M brand, by estimate). The fix is shifting to cheap capture controls ($29–$99 a month video apps, media-reuse checks) rather than human review. Wrongly denying real customers has a direct cost. The CX buyer has no fraud budget.

### Cited Findings
- P1, Glimpse model and reach — [Indeed PH](https://ph.indeed.com/q-glimpse-jobs.html); [BevNET](https://www.bevnet.com/pr/2025/10/29/glimpse-and-presence-enter-into-strategic-partnership-to-bring-aipowered-deduction-management-to-cpg-brands); [Foodbevy](https://www.foodbevy.com/?p=38999); [Food Industry Executive](https://foodindustryexecutive.com/2025/04/glimpse-secures-10m-to-automate-deduction-management-for-cpg-brands/)
- P1, the platform-versus-service argument (vendor opinion) — [Inmar](https://www.inmar.com/blog/insights/martech/how-automating-deductions-management-protects-margins)
- P2, cheap capture tools — [DamageProof](https://apps.shopify.com/damageproof-io); [Corso](https://www.corso.com/shipping-protection)
- P2, enterprise vendors already list returns-abuse modules — [G2](https://www.g2.com/compare/forter-vs-signifyd-vs-riskified)

### Inferences
- **P1 counter-counter:** Glimpse's focus (natural and specialty distributors) leaves room in other channels:
  - Costco and club stores
  - regional grocers (for example H-E-B, Publix, Wegmans; no evidence gathered)
  - c-store distributors (McLane, Core-Mark)
  - non-food CPG
  - "prevention" consulting (fix the root cause upstream)
- **P2 counter-counter:** high-ticket DTC brands (furniture, mattresses, premium bedding like Boll & Branch, electronics) and cross-merchant ring detection may still justify human review. That is a niche, not a mass market.

### Gaps
- Glimpse's churn, pricing and channel coverage beyond KeHE and UNFI are unknown.

---

## Q12. Delivery constraints for an offshore (non-US) team

### Takeaway
- **P1 is offshore-friendly.** Work is batch and deadline-driven (days to weeks), not real-time. Glimpse already uses Philippines staff, and a small US brand recruits on a Ukraine-centred job board. Access needs are portal seats (Retail Link/APDP, Vendor Central, KeHE Connect, UNFI's portal), ERP or accounting read access, and 3PL/carrier POD. No retailer rule barring offshore handling was found, but supplier agreements were not read.
- **P2 is partly offshore-friendly.** It needs Shopify staff access, the helpdesk and the returns app, which means customer personal data. Turnaround must be within hours, but a +9–10 hour time zone can clear the overnight queue. Some enterprise buyers restrict this work to US persons.

### Cited Findings
#### P1
- Retail Link is gated to suppliers with an approved 9-digit Vendor Number — [8th & Walton](https://www.8thandwalton.com/blog/what-is-retail-link-for)
- Third-party data connections run through Scintilla (higher tier includes API access) — [8th & Walton](https://www.8thandwalton.com/blog/what-is-retail-link-for); [SPS: apps, APIs and integrations in Retail Link](https://www.spscommerce.com/community/articles/connecting-apps-apis-and-integrations-in-retail-link)
- Offshore precedents:
  - Glimpse Philippines deductions specialists — [Indeed PH](https://ph.indeed.com/q-glimpse-jobs.html)
  - True Sea Moss UNFI/KeHE role on Djinni — [Djinni](https://djinni.co/jobs/831947-distributor-deductions-and-chargeback-special/)
  - ARPflow (India-based clients) — [LinkedIn](https://www.linkedin.com/company/arpflow)
- Deadlines:
  - Walmart allows disputes for up to 2 years (lens02).
  - Recovery falls from 80% to 20% as disputes near 90 days (lens02, vendor).
  - So the work needs weekly throughput, not real-time.
- Some US deductions roles require local presence (Coppell, TX) or hybrid office time (KDP). That reflects employer preference, not a retailer rule — [Virtual Vocations](https://www.virtualvocations.com/job/deductions-analyst-3310826-i.html); [KDP](https://careers.keurigdrpepper.com/fr-ca/emploi/frisco/deductions-specialist-trade-promotion/42849/77034168640)
- Export friction (headline only): "Retail Link, Vendor Central and KeHE Connect have no export button now" — [CallSphere](https://callsphere.ai/blog/retail-link-vendor-central-and-kehe-connect-have-no-export-button-now-.md)

#### P2
- An enterprise e-commerce fraud analyst role (Inabia, Redmond WA) is onsite and limited to "U.S. citizen or green card holders only" — [CareerBuilder](https://www.careerbuilder.com/job-details/ecommerce-fraud-investigator-analyst-order-to-cash-o2c-redmond-wa--0c10d20a-79e7-4eee-80d1-4702969a9799)
- The ESW fraud analyst role is based in Dublin, so non-US fraud teams exist — [Built In](https://builtin.com/job/ecommerce-fraud-analyst/9359937)

### Inferences
- **P1 data access (prior knowledge, not re-verified):**
  - Retail Link and Vendor Central let the supplier's admin add user seats. Use named seats for the service team, never shared founder logins.
  - Expect MFA tied to phone or email. Plan for MFA delegation (shared authenticator, or a client-side approver).
  - Walmart, Amazon and distributor supplier agreements may carry confidentiality clauses on portal data. These should be checked per client. None were found in search.
- **P2 data access (prior knowledge, not re-verified):**
  - Shopify staff accounts with limited permissions (orders, customers).
  - Gorgias or Zendesk agent seats.
  - Returns-app seats.
  - US state privacy laws (for example CCPA) expect a service-provider contract.
  - UK and EU customer data adds GDPR international-transfer duties (UK IDTA or SCCs).
- **Business hours:**
  - P1 needs no US real-time cover; a weekly cadence with 24–48 hour turnaround on retailer queries is enough.
  - P2 needs a same-day answer. Pakistan or India time zones (UTC+5 to +5:30, about 9–10 hours ahead of US Eastern) suit overnight queue clearing. A small overlap window is needed for escalations.

### Gaps
- No Walmart, Amazon, UNFI or KeHE contract text on third-party or offshore access to supplier portals was found. No Shopify Partner terms on offshore staff access were found.

---

## Q13. Where to find 15 named prospects within 14 days, and the buyer title

### Takeaway
- **P1:** Mine these lists. Contact the founder or CEO under $10M revenue, and the Controller or VP Finance (or fractional CFO) above that. Named signals found so far: True Sea Moss (hiring for UNFI/KeHE deductions), TeaSquares (public KeHE deduction pain), and C.A. Fortune (agency hiring for clients, a partner prospect).
  - Expo West 2026 exhibitor list (about 3,200 brands)
  - KeHE's brand pages
  - job boards (Djinni, Indeed, Built In) for "deductions specialist" or "UNFI/KeHE" posts
  - Foodbevy and BevNET press releases
- **P2:** Mine these lists. Contact the Head of CX, Director of Customer Experience, Returns/Operations Manager, COO or founder. Named signals: Boll & Branch and Bogg Bag (public AI-photo fraud cases).
  - Shopify App Store reviewers of DamageProof, Loop, AfterShip and Corso
  - StoreLeads US store lists filtered by category and size
  - brands quoted in Modern Retail and eCommerce Fastlane

### Cited Findings
#### P1
- Expo West exhibitor scale (3,200+) — [New Hope](https://www.newhope.com/natural-products-expos/natural-products-expo-west-2026-numbers-data-certifications). NBC Los Angeles also published an exhibitor list — [NBC LA](https://nbclosangeles.com/news/local/see-the-exhibitors-at-natural-products-expo-west-2026-in-anaheim/3856941). Named exhibitors include Chobani, Lifeway and Simple Mills (too large for the target band) — [TSNN](https://www.tsnn.com/trade-shows-conferences/natural-products-expo-west-2026-dished-up-health-conscious-product-launches-and-innovations)
- State delegations to Expo West list smaller brands, for example the Minnesota Department of Agriculture pavilion — [MDA](https://www.mda.state.mn.us/minnesota-brings-its-best-natural-products-expo-west)
- KeHE brand directory — [KeHE](https://kehe.com/brands)
- Hiring signals:
  - True Sea Moss — [Djinni](https://djinni.co/jobs/831947-distributor-deductions-and-chargeback-special/)
  - C.A. Fortune — [Built In Charlotte](https://builtincharlotte.com/job/deductions-specialist/8318357)
- Pain signal: TeaSquares — [Foodbevy](https://guide.foodbevy.com/?p=1150)

#### P2
- DamageProof listing (its reviews name merchants) — [Shopify App Store](https://apps.shopify.com/damageproof-io)
- StoreLeads US Shopify store data (1.07M live) — [LinkMyBooks](https://linkmybooks.com/blog/how-many-sellers-are-on-shopify)
- Named brands with AI-photo cases: Boll & Branch and Bogg Bag — [Practical Ecommerce](https://practicalecommerce.com/ai-makes-refund-evidence-easier-to-fake)

### Inferences
- **14-day plan, P1 (inference):**
  1. Day 1–3: pull 100 Expo West exhibitors from state pavilions and the "Fresh Ideas" or new-brand zones. Cross-check KeHE and UNFI presence on their store-locator pages.
  2. Day 3–5: search Indeed, LinkedIn and Djinni for "deductions" and "UNFI", "KeHE", "chargeback" posts from brands under 200 staff.
  3. Day 5–14: find the founder or VP Finance on LinkedIn. Offer a free 12-month look-back audit, matching Glimpse's offer.
- **14-day plan, P2 (inference):** filter StoreLeads for US home, bedding, furniture and electronics stores with 50+ staff or 10K+ monthly orders. Cross-reference reviewers of returns apps and of DamageProof.

### Gaps
- I did not compile the 15 named prospects themselves. Exhibitor-list pages and app-review pages could not be opened. No UNFI public supplier list was found.

---

## Q14. Pricing shapes buyers already accept (with sources)

### Takeaway
- **P1:** Buyers accept all of these:
  - pure contingency (Carbon6, RevRecoup)
  - small monthly fee plus commission (Glimpse)
  - flat-rate SaaS by size and retailer (SupplyPike about $810 a month)
  - tiered SaaS ($349–$1,250 a month, Promomash)
  - part-time contractor hours (15–20 hours a week)
  - salaried staff ($45K–$50K)
  - No deduction-specific contingency % was published. The nearest anchors are 25% (chargebacks) and 25–35% (collections), both from lens02.
- **P2:** Buyers accept:
  - % of transaction (Riskified about 0.4%; Signifyd % of order value with a guarantee)
  - SaaS tiered by return volume (AfterShip from $23 a month; Loop about $155+ a month)
  - app subscriptions ($29–$99 a month, DamageProof)
  - per-image API fees ($0.0005–$0.04)
  - 25% success fee on recovered chargebacks (Chargeflow, lens02)

### Cited Findings
#### P1
- Carbon6: fee only on funds recovered — [Business Wire](https://businesswire.com/news/home/20240917341442/en)
- Glimpse: monthly fee plus commission — [SalesboxAI](https://salesbox.ai/blog/top-deduction-management-platforms-2026)
- SupplyPike: $810 a month (under $10M of Walmart sales; single aggregator) — [SoftwareSuggest](https://www.softwaresuggest.com/supplypike); annual flat rate per retailer — [Software Advice](https://www.softwareadvice.com/product/451076-SupplyPike)
- Promomash: $349 / $599 / $1,250 a month — [Capterra UK](https://www.capterra.co.uk/software/210477/promomash)
- Contractor hours: [Djinni](https://djinni.co/jobs/831947-distributor-deductions-and-chargeback-special/)
- Salary: [Built In Charlotte](https://builtincharlotte.com/job/deductions-specialist/8318357)
- Free 12-month look-back audit as the entry offer — [BevNET](https://www.bevnet.com/pr/2025/10/29/glimpse-and-presence-enter-into-strategic-partnership-to-bring-aipowered-deduction-management-to-cpg-brands)

#### P2
- Riskified about 0.4% per transaction — [Ringly](https://www.ringly.io/blog/riskified-alternatives)
- Signifyd % of order value with a guarantee — [ERP Research](https://erpresearch.com/erp-add-ons/fraud-risk/forter-vs-signifyd)
- AfterShip $23 for 60 returns, $99 for API access — [Refundid](https://refundid.com/item/aftership-alternatives-for-ecommerce-returns)
- Loop about $155 a month — [LateShipment](https://www.lateshipment.com/alternatives/loop-returns/)
- DamageProof $0 / $29 / $99 a month — [Shopify App Store](https://apps.shopify.com/damageproof-io)
- Per-image APIs — [Eden AI](https://www.edenai.co/expert-models/winstonai-ai-image-detection); [Apify](https://apify.com/george.the.developer/ai-deepfake-detector/pricing)

### Inferences
- **P1 workable shape (inference):**
  - a free look-back audit, then
  - either 15–25% of recovered dollars with no minimum (to beat Glimpse on risk), or
  - a $500–$1,500 monthly retainer plus 10–15% for brands with more than $15M in revenue.
- **P2 workable shape (inference):** a per-claim review fee (for example $1–$3 per escalated claim) or a $1,000–$3,000 monthly retainer for a high-value queue. A "% of fraud prevented" fee is hard to measure. Each must clear the $29–$99 a month app alternative.

### Gaps
- Real contingency % for deduction recovery, Glimpse's commission rate, and Forter returns-abuse pricing were not found.

---

## Halal / Shariah flags (no rulings given)

### Takeaway
Both problems are mostly clean, but some segments may raise a Shariah question.

### Cited Findings
- **P1:** CPG suppliers to Walmart, Kroger, Costco and Amazon include alcohol brands, plus pork, tobacco and vape products in grocery and convenience channels. BevNET (a P1 channel) covers alcohol as well as non-alcoholic beverages (prior knowledge, not re-verified). Settle, a Glimpse partner channel, also offers working-capital financing (prior knowledge, not re-verified), so partnering with lenders may raise an interest (riba) question — [Settle partners](https://partners.settle.com/tech-partners/glimpse)
- **P2:**
  - Shipping-protection products (Route, Corso, Protega) are insurance-adjacent. Reviewing claims for them may raise an insurance-related question — [Corso](https://www.corso.com/shipping-protection)
  - AI-image-detector vendors market insurance damage-claim screening — [Apify](https://apify.com/george.the.developer/ai-deepfake-detector/pricing)
  - Generating synthetic "fake damage" images to test detectors may touch the "deepfake creation" exclusion.

### Inferences
- Screen out alcohol-centred brands, and decide upfront on pork and tobacco CPG.
- Keep P2 work on merchant refund claims, not insurer claims.
- Benchmark detectors with public datasets rather than producing new fakes.
- Success-fee or contingency structures are common commercial practice. The client may still want a scholar's view on them (no ruling).

### Gaps
- No Shariah-specific source was consulted (out of scope).
