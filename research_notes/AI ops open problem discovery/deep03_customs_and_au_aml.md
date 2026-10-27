# Deep dive 03: Problem cards for (1) US customs entry prep, tariff churn and IEEPA refunds, and (2) Australia's AML/CTF Tranche 2

Research date: 27 October 2026. Problem 1 covers the US; problem 2 covers Australia.

**Method and access limits (read first)**
- **Page fetches failed again.** A WebFetch of austrac.gov.au returned "getaddrinfo ENOTFOUND", the same failure as round one. Every finding below comes from search-result summaries of the cited pages; none of the full pages was opened. Treat each detail as "reported by" the cited source, and re-open the page before publishing anything.
- **Search budget.** I used all 30 searches allowed and did not repeat any round-one query. Round-one facts are reused with their original links and are marked "(round 1)".
- **Labels used:**
  - "Vendor claim": a number published by a company that sells a fix.
  - "Estimate": my own arithmetic, with the working shown.
  - "Inference": my reasoning, not sourced.
  - "[UNVERIFIED background]": prior knowledge I could not re-check this session.
- **Currency.** AUD is converted at an **assumed 1 AUD = 0.65 USD**. I did not verify this rate; re-check it before use.
- **Correction to round one.** The modernised customs broker regulations (19 CFR Part 111) were published on 18 October 2022 and took effect on 19 December 2022 ([Mondaq](https://www.mondaq.com/unitedstates/international-trade-amp-investment/1261146/new-rules-for-customs-brokers-bringing-your-brokerage-into-compliance-with-the-modernized-part-111)). This was not a 2024 rule.

---

## Q0. Current legal and regulatory status, as of 27 Oct 2026 (the verification priority)

### Takeaway
- **Problem 1 (US customs) is now verified.**
  - IEEPA tariffs were struck down on 20 Feb 2026.
  - CBP's CAPE refund portal opened on 20 Apr 2026, and CAPE Phase 3 was scheduled to deploy on 6 Oct 2026. By mid-September about $134.7B of refunds had been accepted and about $122B (including interest) had been sent to Treasury for payment.
  - The Section 122 surcharge expired on 24 Jul 2026. New Section 301 "forced labor" tariffs of 10% or 12.5% on 60 economies took effect the same day.
  - The de minimis suspension survived the Supreme Court ruling under a separate executive order.
- **Problem 2 (Australia Tranche 2) is now confirmed in force.**
  - Obligations began on 1 July 2026, and enrolment opened on 31 March 2026.
  - The enrolment deadline was 29 July 2026, though one source gives a different date.
  - AUSTRAC began issuing section 167 notices to non-enrolled businesses on 28 August 2026.
  - Enrolment is far from complete: roughly 40–50% of accounting and real estate firms, and about 12–14% of law firms, had enrolled by 29 July 2026 (law-firm estimate).

### Cited Findings

**Problem 1: US tariffs, refunds and de minimis**
- **IEEPA ruling.** *Learning Resources v. Trump* (6-3, 20 Feb 2026) held that IEEPA does not authorise tariffs and ordered no automatic refunds. About $11.4B sits in finally liquidated entries that CBP says it will not refund without a court order (round 1) — [ABA Procurement Lawyer, Fall 2026](https://www.americanbar.org/groups/public_contract_law/resources/procurement-lawyer/2026-fall/ieepa-tariffs-struck-down-replacement-tariffs-expired/); [Great Lakes Customs Law (sells refund services)](https://greatlakescustomslaw.com/ieepa-tariff-refunds/)
- **CAPE launch.** CAPE launched on 20 Apr 2026 amid "high volume" error messages ("The system is currently experiencing high volume, please try again later") — [Yahoo Finance](https://finance.yahoo.com/economy/policy/articles/tariff-refund-portal-off-bumpy-172203826.html). It "has run better than expected in its first week", and CBP said refunds would start 60–90 days after entries are accepted — [Supply Chain Dive](https://supplychaindive.com/news/cbps-tariff-refund-portal-is-performing-better-than-expected/818955/)
- **CAPE Phase 3 and progress to mid-September** — [C.H. Robinson client advisory, 17 Sep 2026](https://www.chrobinson.com/en-au/resources/insights-and-advisories/client-advisories/2026q3/09-17-26-cbp-cape-phase-3-ieepa-refunds/):
  - CBP confirmed Phase 3 would deploy on 6 Oct 2026. Phase 3 covers finally liquidated entries that are subject to court-ordered reliquidation (the plaintiffs' path).
  - Importers who gave CBP a valid importer-of-record (IOR) number by 30 Jul 2026 could start filing Phase 3 declarations.
  - By mid-September: about 286,000 declarations submitted, about $134.7B of potential and certified refunds accepted, and about $122B (including interest) sent to Treasury for payment.
  - 20,184 refunds worth $1.3B were on hold because importers had not supplied ACH bank details.
  - I found no October source confirming the actual go-live or the Phase 3 filing instructions (gap).
- **Rejections and pool size.**
  - CBS headline: "Feds have rejected 15% of businesses' tariff refund claims" (body not read) — [CBS News](https://www.cbsnews.com/amp/news/tariff-refund-portal-trump-cbp/)
  - Another outlet's headline puts the pool at "$166 Billion" — [WebProNews](https://www.webpronews.com/tariff-refund-rush-importers-swarm-new-u-s-portal-for-166-billion-in-struck-down-duties/)
  - Round 1 found estimates of $35.46B to $165B (round 1, ABA / Great Lakes).
  - Range now: $134.7B accepted (C.H. Robinson) against a $165–166B total pool (two sources).
- **CAPE filing mechanics.**
  - Bulk filing allows up to 9,999 entries per declaration (Thomson Reuters analysis, via [pulse.bot](https://www.pulse.bot/govtech/news/the-cape-tariff-refund-system-is-here-is-your-global-trade-team-ready-82e77133-00f2-4c75-9990-7e30f4b4db59/))
  - Only the IOR or an authorised licensed broker may submit a CAPE declaration in the ACE Portal (vendor guide) — [cape-guide](https://cape-guide.pages.dev/blog/lawyer-broker-recovery-firm-who-files-ieepa-refund/)
- **Section 122 surcharge.** A Section 122 surcharge started on 24 Feb 2026 and expired on 24 Jul 2026 (round 1, ABA). Sources disagree on the rate: 10% "expected to rise to 15%" in one ([NatLawReview](https://natlawreview.com/article/post-scotus-tariff-reset-trump-replaces-ieepa-duties-temporary-section-122-10)), 15% in another (per search summary).
- **Section 301 "forced labor" tariffs**, effective 12:01 a.m. EDT on 24 Jul 2026:
  - **Rates and reach.** 10% or 12.5% on most imports from 60 economies, which USTR says account for about 99.4% of US imports. There are many product and country exclusions.
  - **Two tiers.** Lower rates apply to economies that have adopted, or committed to adopt, forced-labour import bans.
  - **Goods in transit.** Goods already on the water qualified for an exemption only if entered by 28 Jul 2026.
  - **Section 232 carve-out.** Goods under Section 232 duties are excluded: steel, aluminium, copper, autos and parts, medium/heavy vehicles, buses, and timber/lumber.
  - **Planned quotas.** Tariff-rate quotas are planned for Bangladesh, Cambodia, Indonesia and Malaysia.
  - Sources: [Thomson Reuters, 24 Jul 2026](https://www.thomsonreuters.com/en-us/help/onesource-global-trade/regulatory-insights/2026/july-24th/us-imposes-section-301-forced-labor-tariffs-60.html); [GT Law](https://www.gtlaw.com/de/insights/2026/7/ustr-imposes-new-section-301-forced-labor-tariffs-on-imports-from-60-economies); [BDO](https://www.bdo.com/insights/tax/double-digit-section-301-tariffs-hit-imports-from-60-economies); [Clark Hill](https://www.clarkhill.com/news-events/news/ustr-section-301-forced-labor-tariffs-imports/); [Livingston](https://www.livingstonintl.com/ustr-section-301-forced-labor-duties-take-effect-july-24-2026/); [Kuehne+Nagel](https://mykn.kuehne-nagel.com/news/article/us-administration-imposes-new-section-301)
- **De minimis.**
  - The Supreme Court ruling did not restore de minimis. A 20 Feb 2026 executive order (named EO 14388 in one analysis) continued the suspension for all countries, using a contingency clause in EO 14324 — [Thomson Reuters, 25 Feb 2026](https://www.thomsonreuters.com/en-us/help/onesource-global-trade/regulatory-insights/2026/february-25th/de-min-suspension-means-global-trade-prof.html); [Sandler Travis (STR)](https://www.strtrade.com/trade-news-resources/str-trade-report/trade-report/february/de-minimis-suspension-remains-in-place)
  - The postal duty rate was tied to the Section 122 rate "until the expiration date of the Section 122 tariff, or until the effective date of the new entry process for postal shipments established by CBP" (same sources).
  - **Postal treatment after Section 122 expired on 24 Jul 2026 is NOT confirmed** (gap).
  - One blog claims a non-postal suspension effective 24 Jun 2026 and a permanent end in 2027. This is unverified — [GetTransport blog](https://blog.gettransport.com/logistics-guide/us-de-minimis-suspension-2026-importer-status-guide/)
- **New IOR clean-up (more recurring paperwork).**
  - CBP deactivated about 4.8M IOR accounts with no entry in the prior year. From 16 Jul 2026, accounts with no entry in 366 days move to "Inactive for Entry Purposes."
  - Enforcement, including immediate voiding of IOR numbers with inaccurate CBP Form 5106 data, began on 18 Sep 2026.
  - Sources: [Federal Register, 19 Aug 2026 (2026-16911)](https://www.govinfo.gov/content/pkg/FR-2026-08-19/html/2026-16911.htm); [Thomson Reuters, 17 Sep 2026](https://www.thomsonreuters.com/en-us/help/onesource-global-trade/regulatory-insights/2026/september-17th/cbp-importer-of-record-data-accuracy-begins); [Shopappy](https://shopappy.com/trade/tariffs-customs/cbp-importer-number-voiding-begins). The search summary did not tie the 4.8M figure to one of these pages.

**Problem 2: Australia Tranche 2**
- **Who is covered.** Obligations took effect on 1 July 2026 for real estate professionals, dealers in precious stones and metals, lawyers, conveyancers, accountants, and trust and company service providers. Coverage depends on which "designated services" a firm provides, not on the profession as a whole — [AUSTRAC summary of Tranche 2 obligations](https://austrac.gov.au/node/1158); [Cooper Grace Ward guide, July 2026](https://cgw.com.au/wp-content/uploads/2026/07/AML-CTF-Reforms-2026-Guide-for-Advisers-post-1-July-Cooper-Grace-Ward-3447-3531-7325.pdf); [LSEG glossary](https://www.lseg.com/en/risk-intelligence/glossary/aml/tranche-2)
- **Enrolment dates.** Enrolment opened on 31 March 2026 — [AUSTRAC news](https://www.austrac.gov.au/new-and-media/news/austrac-opens-enrolment-new-professions-next-step-aml-reforms); [Legl](https://legl.com/articles/austrac-opens-enrolment-for-tranche-2-professions-what-law-firms-need-to-know-before-1-july). The deadline was 29 July 2026 per [Clyde & Co, Aug 2026](https://www.clydeco.com/en/insights/2026/08/austrac-takes-compliance-action-in-relation-to-tra). Another source says "within 28 days of commencing designated services" ([Persona](https://withpersona.com/blog/tranche-2-australia) / [Didit](https://updates.didit.me/blog/austrac-tranche-2-kyc-aml-accountants-australia/)); these two framings may describe the same rule.
- **Enforcement has started.** From 28 August 2026 AUSTRAC began issuing **section 167 notices** to businesses that appear to provide designated services but have not enrolled — [Clyde & Co](https://www.clydeco.com/en/insights/2026/08/austrac-takes-compliance-action-in-relation-to-tra)
- **Rule timing.** The new AML/CTF Rules (two instruments: general Rules and Class Exemption Rules) applied to existing reporting entities from 31 March 2026. Their threshold and suspicious-matter reporting stays the same until 2029. Tranche 2 obligations started on 1 July 2026 — [Brightlaw](https://www.brightlaw.com.au/new-finalised-aml-ctf-rules-published/); [AUSTRAC new Rules page](https://www.austrac.gov.au/amlctf-reform/new-amlctf-rules); [PEXA key dates](https://www.pexa.com.au/aml/key-dates-tranche-2/)
- **Duties for real estate agents** (vendor guide, [Didit](https://didit.me/blog/austrac-tranche-2-real-estate-agents-guide/)):
  - Verify **both buyers and sellers** (name, date of birth, residential address) before or during the designated service.
  - Lodge a threshold transaction report for cash of A$10,000 or more within 10 business days.
  - New threshold and suspicious-matter report forms were released on 1 July 2026 (one source).
- **Delayed CDD for property.** The reforms allow customer due diligence to be delayed around settlement in real estate transactions where parties share the identity-check workload — [VinciWorks](https://vinciworks.com/blog/australias-tranche-2-aml-ctf-reforms-whats-changed-whos-in-scope-and-what-to-do-now/)
- **Regulator's early posture.**
  - AUSTRAC's CEO reportedly said AUSTRAC would not pursue small businesses over administrative glitches, and the Law Society of NSW welcomed this — [Law Society NSW](https://www.lawsociety.com.au/solicitors-welcome-austrac-assurances-amlctf)
  - Industry bodies say the first 12 months will be "education-led" — [CCP Accountants](https://www.ccp.com.au/news/tranche-2-aml-ctf-obligations-accountants/); [easyAML](https://knowledge.easyaml.com/can-i-stop-offering-designated-services)
- **Unclear transition window.** One source mentions a transition window to 30 March 2029 "for existing entities" (search summary of [Persona](https://withpersona.com/blog/tranche-2-australia)). It is unclear what this covers; it probably refers to Tranche 1 reporting forms, not Tranche 2 CDD (see Gaps).

### Inferences
**One-screen problem cards**

| | P1: US customs entry prep + tariff churn + refunds | P2: AU Tranche 2 CDD and monitoring |
|---|---|---|
| Status | Live. Tariff stack changed again on 24 Jul 2026; CAPE Phase 3 Oct 2026 | Live since 1 Jul 2026; enforcement letters started 28 Aug 2026 |
| Core recurring task | Invoice and packing list → HTS lines → tariff-layer check → ABI entry, every shipment | CDD on every new designated-service client, ongoing monitoring, reporting |
| Buyer | Small licensed brokerage (owner or licensed broker) | Principal or practice manager (often also the AML/CTF compliance officer) |
| Monthly pain (estimate) | $4.4k–$13.2k labour per 100 entries/week | A$760–A$2,600 (US$490–$1,690) for a small agency; government estimate A$1,940/month ongoing |
| Biggest risk | Bundled AI in CargoWise; US records/server rules; refund work fades in 2027 | Small-ticket buyers; cheap per-check tools; incumbents inside practice software |
| Verdict | Still strong for broker back-office support; refund add-on is short-lived | Still strong on demand; weaker on price per client |

### Gaps
- No October 2026 primary source confirms that CAPE Phase 3 actually went live on 6 October, or what its filing rules are.
- The de minimis postal rate after Section 122 expired, and any statutory end date, were not verified.
- The Tranche 2 enrolment deadline is given two ways (29 July, or 28 days after starting). The "30 March 2029" transition item is unexplained.
- The AUSTRAC site could not be opened. All AUSTRAC facts come from search summaries.

---

## Q1. The exact task, in plain words

### Takeaway
- **P1** is per-shipment keying and judgement: reading invoices, classifying products, stacking tariff layers and filing in ABI, plus a newer stream of refund and IOR clean-up paperwork.
- **P2** is per-client identity and ownership checking, plus ongoing monitoring and reporting, run under a written AML/CTF program.

### Cited Findings
**Problem 1**
- "A junior entry writer compares the commercial invoice against the packing list and keys the data into the customs system" (round 1) — [Forwarder Insights, Apr 2026](https://forwarderinsights.blogspot.com/2026/04/how-automation-and-ai-are-changing.html)
- CargoWise's own invoice parsing pulls goods descriptions, quantities, values and country of origin into the job; staff then review flagged fields (vendor-adjacent page, May 2026) — [viago](https://viago-website.pages.dev/cargowise-ai-features.html); [WiseTech-affiliated LinkedIn post](https://ie.linkedin.com/in/annmarieday)
- Tariff-layer check now includes:
  - Which Section 301 forced-labour rate applies by country (10% or 12.5%).
  - Whether a Section 232 exclusion applies (metals, autos, timber).
  - Product and country exclusions.
  - Sources: [GT Law](https://www.gtlaw.com/de/insights/2026/7/ustr-imposes-new-section-301-forced-labor-tariffs-on-imports-from-60-economies); [Thomson Reuters](https://www.thomsonreuters.com/en-us/help/onesource-global-trade/regulatory-insights/2026/july-24th/us-imposes-section-301-forced-labor-tariffs-60.html)
- Refund stream: a CAPE declaration (up to 9,999 entries) filed by the IOR or an authorised broker, with ACH bank details on file. 20,184 refunds were held for missing ACH details — [C.H. Robinson](https://www.chrobinson.com/en-au/resources/insights-and-advisories/client-advisories/2026q3/09-17-26-cbp-cape-phase-3-ieepa-refunds/); [pulse.bot / Thomson Reuters](https://www.pulse.bot/govtech/news/the-cape-tariff-refund-system-is-here-is-your-global-trade-team-ready-82e77133-00f2-4c75-9990-7e30f4b4db59/)
- Client data stream: keep each client's IOR record (CBP Form 5106) accurate, or the IOR number is voided from 18 Sep 2026 — [Federal Register 2026-16911](https://www.govinfo.gov/content/pkg/FR-2026-08-19/html/2026-16911.htm)

**Problem 2**
- For each buyer and seller, the agent verifies full legal name, date of birth and residential address before or during the designated service (vendor guide) — [Didit](https://didit.me/blog/austrac-tranche-2-real-estate-agents-guide/)
- Accountants are caught by a defined set of services, such as forming companies or trusts, acting as director or trustee, and handling client money. If a firm provides any of them, it is a reporting entity for the whole firm. It must name an AML/CTF compliance officer who is a natural person within the firm — [Beancount blog, 28 Jul 2026](https://beancount.io/blog/2026/07/28/austrac-tranche-2-accountants-bookkeepers-guide); [CCP](https://www.ccp.com.au/news/tranche-2-aml-ctf-obligations-accountants/)
- The full outsourced bundle on the market today: program design, CDD, sanctions and PEP screening, transaction monitoring, staff training and regulatory reporting (vendor description) — [AML Partners press release, Aug 2026](https://www.aap.com.au/aapreleases/globenewswire9804986/)

### Inferences
**Plain-words task, P1:** "Each time a client's container or air shipment is coming, the entry writer:
1. opens the supplier's commercial invoice and packing list (PDF, scan or Excel);
2. matches each line to the client's parts list, or classifies new items to a 10-digit HTS code;
3. checks country of origin and which extra tariffs apply (Section 301 forced-labour rate by country, Section 232 metals/autos/timber, older China 301 lists, exclusions);
4. computes values, weights and fees;
5. keys the entry into the ABI software (CargoWise, Descartes, Magaya or similar);
6. fixes CBP rejects.

On the side, the brokerage builds CAPE refund declarations for past IEEPA entries and keeps client IOR records current. A licensed broker reviews and signs off."

**Plain-words task, P2:** "Each time a firm takes on a client for a covered service (selling a house, setting up a trust or company, holding client money), a staff member:
1. collects ID for every individual, and for companies and trusts traces who really owns or controls them;
2. screens names against sanctions and politically exposed person (PEP) lists;
3. rates the client's risk and, for higher-risk clients, asks where the money comes from;
4. files the evidence so it can be produced later;
5. keeps watching existing clients for changes or suspicious activity, and lodges reports to AUSTRAC when needed.

The firm's compliance officer owns the written program and reviews it."

### Gaps
- No source gave the exact share of entries that need fresh HTS classification versus reuse of a client's parts list.
- Whether Tranche 2 requires CDD on pre-1 July existing clients (and on what trigger) was not verified.

---

## Q2. Who feels it, and who approves the money

### Takeaway
- **P1:** entry writers and licensed brokers feel it; the brokerage owner, president or VP customs approves spend. For refund work at importers, the controller or CFO approves.
- **P2:** the newly appointed AML/CTF compliance officer (usually a partner, principal or practice manager) both feels it and approves.

### Cited Findings
- **P1 job titles in 2026 postings:** "Customs Entry Writer", "Customs Specialist – Entry Writer", "Entry Writer Specialist – Customs" — [Prosimo.io via General Catalyst job board, 9 Oct 2026](https://jobs.generalcatalyst.com/companies/prosimo-io-2/jobs/96375269-customs-entry-writer); [DSV](https://www.marketingmonk.so/jobboard/jobs/customs-specialist-entry-writer-at-dsv-g51j8e); [RXO](https://www.marketingmonk.so/jobboard/jobs/entry-writer-specialist-customs-at-rxo-inc-49gwl1)
- **P1 supervision:** individual licensed brokers (sole proprietors, licensed partners or officers) must exercise "responsible supervision and control" over the customs business — [eCFR 19 CFR 111.28](https://www.ecfr.gov/current/title-19/chapter-I/part-111/subpart-C/section-111.28)
- **P2:** "in most small practices this role will fall to a partner, practice manager or senior manager already carrying a full workload" — [CCP](https://www.ccp.com.au/news/tranche-2-aml-ctf-obligations-accountants/) / [Beancount](https://beancount.io/blog/2026/07/28/austrac-tranche-2-accountants-bookkeepers-guide) (search summary; exact page not confirmed)
- **P2:** ALPMA published a whitepaper on how to hire an AML Compliance Officer (AMLCO) for Australian law firms — [ALPMA whitepapers](https://www.alpma.com.au/whitepapers)

### Inferences
- **P1 approver:** at a 2–50 person brokerage, the owner or licensed principal signs any outsourcing contract, because their licence carries the supervision duty.
- **P2:** in real estate, the licensee-in-charge or principal approves. In law firms it is the managing partner or practice manager; in accounting firms, the principal.

### Gaps
- No survey of who signs AML vendor contracts in Australian SMB firms.

---

## Q3. How often it happens and how many hours it eats (math shown)

### Takeaway
- **P1:** continuous, every shipment.
  - A small broker filing 100 entries a week spends about 25–75 staff hours a week on entry prep (estimate).
  - Each tariff change adds a re-mapping burst across client parts lists.
- **P2:** every new covered client.
  - A small real estate agency doing 10 sales a month spends about 12 hours a month (estimate).
  - A small accounting practice with 8 new covered clients a month spends about 9–10 hours a month (estimate).

### Cited Findings
- **Average entries per brokerage:** ACE processed over 9 million import entries from more than 14,000 licensed brokers (year unconfirmed; round 1) — [Mordor Intelligence](https://mordorintelligence.com/industry-reports/united-states-customs-brokerage-market). About 6,200 brokerage firms (vendor blog; round 1) — [Camtom](https://www.camtomx.com/en/blog/what-is-a-customs-broker)
- **Classification time:** 12 minutes per product manual versus 2.5 minutes AI-assisted, from an unverified "2025 study of 50 US customs brokerages" cited by a vendor (round 1) — [Camtom](https://camtomx.com/blog/ai-transforming-customs-brokerage-2026)
- **Tariff churn:**
  - "53 tariff changes" in 2025 (vendor claim; round 1) — [Flexport](https://www.flexport.com/solutions/simplify-customs/)
  - 2026 has added IEEPA invalidation (Feb), Section 122 (Feb–Jul), Section 301 forced labour (Jul) and the IOR clean-up (Jul–Sep) — see Q0 sources.
- **Price tiers by line count:** basic entry with 1–3 lines $150–$250; 5+ lines with multiple HTS codes $250–$400 (broker marketing blog) — [Suaid Global](https://suaidglobal.pages.dev/insights/customs-broker-fees-2026)
- **P2:** AUSTRAC/sponsor guidance requires verifying buyers and sellers (two customers per sale) — [Didit](https://didit.me/blog/austrac-tranche-2-real-estate-agents-guide/)

### Inferences (estimates, math shown)

**P1 entry volume.** Average firm: 9M entries ÷ 6,200 firms ≈ 1,450 entries a year ≈ 28 a week. The distribution is heavily skewed, so I use a "small active broker" scenario of 100 entries a week (assumption).

**P1 minutes per entry (assumptions):**
- 10–20 minutes to key and check invoice and packing list data.
- Plus 0–2 new SKUs × 12 minutes classification (vendor figure above), i.e. 0–24 minutes.
- Plus about 5 minutes for the tariff-layer check.
- Total: **15–45 minutes per entry**.

**P1 weekly hours:**
- 100 × 15–45 minutes = 1,500–4,500 minutes = **25–75 hours a week**, or 0.6–1.9 FTE.

**P1 tariff-change burst:**
- A client with 2,000 active SKUs × 1 minute re-check per SKU ≈ 33 hours per rule change, per client (assumption).

**P1 refund work:**
- A client with 400 IEEPA-era entries × 5 minutes to check liquidation, protest and eligibility status ≈ 33 hours one-off. CAPE bulk filing (up to 9,999 entries) makes the filing itself fast; the reconciliation is the work.

**P2 real estate agency (assumptions):**
- 10 sales a month × 2 customers = 20 CDD files.
- Mix: 80% individuals at about 20 minutes, 20% companies or trusts at about 60 minutes, giving an average of 0.8 × 20 + 0.2 × 60 = 28 minutes.
- 20 × 28 minutes ≈ 9.3 hours, plus about 3 hours a month for monitoring, rescreening, suspicious-matter triage and records.
- Total: **about 12 hours a month**.

**P2 small accounting practice (assumptions):**
- 8 new covered clients a month, half of them entities: 4 × 20 + 4 × 75 minutes = 380 minutes ≈ 6.3 hours.
- Plus annual review of 150 existing covered clients at 15 minutes each = 37.5 hours a year ≈ 3.1 hours a month.
- Total: **about 9–10 hours a month**.

**P2 conveyancing or law firm (assumptions):**
- 30 property matters a month × 25 minutes ≈ 12.5 hours a month, plus entity matters.

### Gaps
- No independent minutes-per-entry or minutes-per-CDD-file study was found. All hour figures are estimates.
- Real distribution of entries per small broker: CBP does not publish it per filer in what I could see.

---

## Q4. What it costs a typical firm per month (math shown; estimates labelled)

### Takeaway
- **P1:** about $4,400–$13,200 a month in entry-prep labour for a broker filing 100 entries a week (estimate). That is roughly 7–20% of that broker's entry-fee revenue (estimate).
- **P2:** about A$760–A$2,600 a month (US$490–$1,690) for a small agency in staff time plus ID checks (estimate). This brackets the government's estimate of A$23,250 a year (about A$1,940 a month) in ongoing cost for an average small business.

### Cited Findings
- **Entry writer pay, 2026 postings:**
  - Dallas: $60k–$75k base (Apr 2026) — [Altius Talent via career.com](https://www.career.com/job/altius-talent-freight-forwarding-recruitment/customs-entry-writer/j202601221606264689051)
  - Elk Grove Village, IL: up to $75k (9 Oct 2026) — [Prosimo.io](https://jobs.generalcatalyst.com/companies/prosimo-io-2/jobs/96375269-customs-entry-writer)
  - Richmond, VA: $58,760; another Estes listing pays $24–$32.50 an hour — [Estes Forwarding via Tallo](https://tallo.com/talent/job/design-and-media/writer/va/richmond/customs-entry-writer-28597be0)
  - West Valley City, UT: $22–$30 an hour — [DSV](https://www.marketingmonk.so/jobboard/jobs/customs-specialist-entry-writer-at-dsv-g51j8e)
  - Long Beach / New York: $55k–$80k — [ZipRecruiter](https://www.ziprecruiter.com/Jobs/Customs-Brokerage-Entry-Writer/3)
  - General "customs clearance" average: $75,242 (9 Jun 2026) — [ZipRecruiter](https://www.ziprecruiter.com/Jobs/Customs-Clearance/3)
- **Broker fee per entry:** $75–$400 depending on complexity (broker marketing pages, not fee schedules) — [FreightAmigo](https://www.freightamigo.com/en/blog/logistics/customs-broker-guide-costs-definition-and-essential-services-in-2026/); [Suaid Global](https://suaidglobal.pages.dev/insights/customs-broker-fees-2026); [LandedCost guide](https://landedcost-2fn.pages.dev/guides/customs-brokerage-fees/)
- **P2 government estimate:** the Regulation Impact Statement estimates "upfront compliance costs of up to $28,650, with ongoing costs estimated at $23,250 per year for the average small business" (as quoted by an ID-verification vendor) — [Scantek](https://scantek.com/how-much-will-aml-ctf-tranche-2-compliance-cost-your-business/)
- **P2 AML compliance officer pay:** average A$70,181, range A$54k–A$87k (aggregated estimate) — [Payscale](https://www.payscale.com/research/AU/Job=Compliance_Officer/Salary/144706e6/Anti-Money-Laundering-AML)
- **P2 ID checks:** A$13–A$40 per individual, A$28–A$65 per business or trust, plus a A$59–A$300+ monthly platform fee (low-quality guide; unverified) — [niftycomputing guide (attribution per search summary)](https://niftycomputing-au.pages.dev/toolkit/real-estate/aml-ctf-guide)

### Inferences (estimates)
**P1:**
- Loaded entry-writer cost = $65k midpoint × 1.3 load (assumed) = $84,500 a year ≈ $40.60 an hour (÷ 2,080 hours).
- 25–75 hours a week × $40.60 × 4.33 weeks = **$4,400–$13,200 a month**.
- Revenue context: 100 entries a week × 4.33 × $150 (assumed average fee) ≈ $65,000 a month in fees, so entry-prep labour is about 7–20% of fee revenue.
- Not counted: rejects, CBP penalties, and the tariff-change rework bursts (33 hours per client per change at $40.60 ≈ $1,340 per client per event).

**P1 importer side (refunds):**
- An importer that paid $2M in IEEPA duties and is charged a 5% broker fee pays about $100,000. At a blended 20% contingency it would pay about $400,000 (fee shapes in Q14).

**P2 small agency:**
- About 12 hours a month × A$42 an hour = **A$504** (staff cost: A$70k × 1.25 on-costs ÷ 2,080 hours; the 1.25 load is assumed).
- If a principal does the work at an assumed A$150 an hour opportunity cost: **A$1,800**.
- Plus 20 checks × A$13–A$40 = A$260–A$800 a month.
- Total: **A$760–A$2,600 a month (US$490–$1,690)**.

**P2 upfront cost** of a program setup: A$4,500–A$11,000 consultant fixed fee (Q5), against the government's A$28,650 upper estimate (US$2,925–$7,150 against US$18,600).

### Gaps
- No real broker P&L or Australian practice AML-cost survey was found.
- The 1.3 and 1.25 load factors are assumptions.

---

## Q5. How firms handle it today and what they pay

### Takeaway
- **P1:** in-house entry writers ($50k–$80k a year in postings), ABI software (CargoWise, Descartes, Magaya and others), add-on extraction tools that feed CargoWise, and a fast-growing refund-recovery market charging 3–28%.
- **P2:** a mix of free law-society templates, A$490-a-year program software, A$4,500–A$11,000 consultant setups, per-check ID tools, and fully outsourced managed services. AML Partners claims 300–400 clients.

### Cited Findings
**Problem 1**
- **In-house staff:** salaries as in Q4.
- **CargoWise:**
  - Native commercial-invoice AI parsing through eDocs (configured per document type; accuracy "improves as the system sees more documents from each supplier") — [viago (vendor-adjacent)](https://viago-website.pages.dev/cargowise-ai-features.html)
  - A comparison blog says CargoWise is complex, implementation takes months, and it is "not a tool for small brokerages processing a few entries per week" — [Lido (vendor)](https://www.lido.app/blog/best-customs-document-processing-software)
- **Descartes:**
  - Hosted ABI that "scales from small independent brokers to global enterprises" (vendor) — [Descartes US customs declarations](https://descartes.com/solutions/customs-and-regulatory-compliance/customs-declarations/united-states)
  - An aggregator lists "from €200 per month", €800 setup, and €66 per concurrent user per month. This is unverified and may describe a European product — [FitGap](https://us.fitgap.com/products/021173/descartes-customs-compliance-suite)
- **Third-party extraction into CargoWise:** Expedock, Cargo Docket (pricing undisclosed), CargoIQ, FreightMynd, Wove — [Expedock](https://expedock.com/integration/expedock-for-cargowise); [Clutch: Cargo Docket](https://clutch.co/profile/cargo-docket); [CargoIQ](https://cargoiq.pages.dev/integrations/cargowise); [Wove](https://wove.com/document-extraction)
- **Refund recovery** (prices in Q14) — [Clearit](https://clearitusa.com/ieepa-refund-pricing-what-importers-need-to-know/); [Tariff Refund Solutions FAQ](https://v0-tariff-refund-solutions.pages.dev/faq); [Leyton Phase 3](https://leyton.com/us/ieepa-customs-tariff-refund/ieepa-tariff-refunds-phase-3/)

**Problem 2**
- **Free templates:** the Law Society of NSW released a free AML/CTF Implementation Guide for sole practitioners and small practices, available to all NSW solicitors whether or not they are members — [Law Society NSW](https://www.lawsociety.com.au/new-guidance-help-small-practice-amlctf-compliance); [Lawyers Weekly](https://www.lawyersweekly.com.au/sme-law/44137-new-aml-guide-released-for-small-law-firms-ahead-of-major-compliance-shake-up)
- **Consultant fixed fees:** solo/micro package A$4,500, medium practice A$11,000, independent review add-on about A$1,500 (vendor page, unverified) — [GateCrown](https://gatecrown.pages.dev/accounting)
- **Custom legal drafting:** A$5,000–A$15,000 — [Scantek](https://scantek.com/how-much-will-aml-ctf-tranche-2-compliance-cost-your-business/)
- **Program software:** a "program-only" tier at A$490 a year (A$41 a month), including GST (the search summary calls the vendor "Duely") — [vendor pricing page](https://sentine-web.pages.dev/pricing)
- **Managed outsourcing:** AML Partners says it serves about 300–400 Tranche 2 businesses with a "fully outsourced" platform, while the agency keeps the customer relationship (vendor claim, Aug 2026) — [AAP release](https://www.aap.com.au/aapreleases/globenewswire9804986/); [Real Estate Business](https://www.realestatebusiness.com.au/industry/32233-how-australian-businesses-can-outsource-compliance-and-meet-their-tranche-2-aml-obligations-with-aml-partners)
- **Financial-adviser subscription:** Kit Legal launched an AML/CTF subscription service (price not shown) — [IFA](https://www.ifa.com.au/kit-legal-releases-aml-ctf-subscription-service-ahead-of-tranche-2-reforms)
- **Training:** First AML sells online training at $99 per person, with a 30% discount on program setup or independent audit — [First AML one-stop-shop offer](https://firstaml.com/au/about/company/partners/one-stop-shop)

### Inferences
- P1 buyers already pay for labour and software; the open question is whether they will pay a third party per entry. Brokers already sell per entry to importers, so a per-entry back-office price is natural.
- P2 buyers are spread across a very wide price band (free to managed service). A service must sit above the per-check tools on judgement (entities, trusts, source of funds) and below a full-time hire.

### Gaps
- Magaya pricing was not found.
- No public CargoWise price for small brokers.
- AML Partners' and First AML's platform prices were not found.

---

## Q6. Proof: operator quotes, surveys and job posts

### Takeaway
- Evidence of pain is strong for **P2**: a 1,700-person accountant survey, law-society action, enrolment shortfalls and enforcement letters.
- **P1** evidence is mostly market signals: refund fees, job posts, CAPE strain and the Loadstar headlines. Direct broker quotes remain thin, because article bodies could not be read.

### Cited Findings
**Problem 1**
- A Seko Logistics brokerage director: "We have not seen a delay in CBP actions or clearances." He also said CBP information requests had grown in volume and complexity, and: "My larger concern with these postings is whether the added staff is versed in this extremely complicated environment." The quote appeared in search results alongside The Loadstar article "tariff turmoil sees CBP recruit retirees to deal with the havoc"; attribution to that article is inferred — [The Loadstar](https://theloadstar.com/tariff-turmoil-sees-cpb-recruit-retirees-to-deal-with-the-havoc/)
- Loadstar headline: "Customs brokers eyeing 10% to 15% of US tariff refunds, claim" (body not read) — [The Loadstar](https://theloadstar.com/?p=308226)
- Analyst comment: "resource‑constrained compliance departments also face the dilemma of allocating staff to refund pursuits without jeopardizing day‑to‑day customs filings" (Thomson Reuters analysis) — [pulse.bot](https://www.pulse.bot/govtech/news/the-cape-tariff-refund-system-is-here-is-your-global-trade-team-ready-82e77133-00f2-4c75-9990-7e30f4b4db59/)
- A broker-focused guide warns that some brokers filed CAPE declarations without importer consent (vendor) — [TariffCenter](https://tariffcenter.ai/blog/broker-filed-cape-without-you-reclaim-refund)
- Round 1: The Loadstar, "Customs brokers fear US import rule changes are pushing them towards AI" — [The Loadstar](https://theloadstar.com/customs-brokers-fear-us-import-rule-changes-are-pushing-them-towards-ai/)
- **Job posts (2026):**
  - Altius Talent (Dallas, Apr 2026)
  - Prosimo.io (Elk Grove Village, 9 Oct 2026)
  - Estes Forwarding (Richmond / North Chesterfield, VA)
  - DSV (Utah), DP World, RXO
  - Sources: see Q4 links; [DP World](https://www.marketingmonk.so/jobboard/jobs/customs-entry-writer-at-dp-world-64563t)

**Problem 2**
- **Access Group survey** of 1,700+ accounting professionals: only 6% felt "on top of" the rules, 32% had not started, and 62% were unclear. Access Group (which sells practice software) — [Accounting Times](https://www.accountingtimes.com.au/profession/access-group-warns-of-guidance-gap-ahead-of-tranche-2-aml-ctf); [IT Brief](https://itbrief.com.au/story/australian-accountants-face-aml-reform-readiness-gap)
- **Access Group's David Boyar** framed it as a stacking effect: practices had just absorbed the expanded TASA Code of Conduct, and "small practices with no dedicated compliance resource face acute operational pressure" (paraphrase in search summary). Accountants lack "worked examples and service-specific guidance" — same sources.
- **Enrolment shortfall** at 29 July 2026: about 50% of accounting practices, about 40% of real estate agencies, 12–14% of law firms and about 10% of jewellers had enrolled (Clyde & Co estimate from media and compliance data) — [Clyde & Co](https://www.clydeco.com/en/insights/2026/08/austrac-takes-compliance-action-in-relation-to-tra)
- **Exit option:** some small firms are weighing whether to stop offering designated services — [easyAML](https://knowledge.easyaml.com/can-i-stop-offering-designated-services)
- **Penalties:** a Lawyers Weekly opinion piece cites possible fines "as high as $200,000" for small firms (law-firm commentary; article attribution from search summary) — [Lawyers Weekly](https://www.lawyersweekly.com.au/sme-law/43785-how-one-law-firm-is-future-proofing-against-australia-s-new-aml-ctf-reforms)
- **Hiring signal:** ALPMA's whitepaper on hiring an AMLCO; its 2025 salary survey covered 345 law offices but did not break out AML roles — [ALPMA](https://www.alpma.com.au/whitepapers)

### Inferences
- P2 shows a classic first-year gap: a law is in force, half the market is not enrolled, and the regulator has started sending letters. That is the moment buyers seek outsourced help.
- In P1, the refund market (brokers taking a cut of 5–15%) shows that brokers are monetising refunds themselves. A back-office provider would serve brokers rather than compete with them.

### Gaps
- Article bodies at The Loadstar, JOC, FreightWaves, Accountants Daily and AFR were not readable. No NCBFAA survey was found.
- No Australian "AML compliance officer" job posts at small firms were found; only salary aggregates.

---

## Q7. Who else sells a fix, at what price, for what size, and how crowded

### Takeaway
- **P1** is crowded and VC-funded at the software layer: CargoWise native AI, Gaia Dynamics ($7M seed), Amari AI ($4.5M), Alchemize (YC, AI-native brokerage), Raft, Expedock, Camtom, Zonos. Filing software already includes AI extraction (CargoWise eDocs).
- The gap for P1 is a done-for-you, broker-supervised back office for small brokers who cannot run CargoWise-class implementations.
- **P2** is crowded at the ID-check layer: First AML, InfoTrack, Didit, Persona, NameScan, Scantek, APLYiD, easyAML, AMLHUB. It is less crowded for judgement-heavy CDD, monitoring and program upkeep, where AML Partners and consultants compete.

### Cited Findings
**Problem 1 competitors**

| Vendor | What it does | Price found | Target size | Source |
|---|---|---|---|---|
| CargoWise (WiseTech) | ABI filing plus native AI invoice parsing (eDocs) | Not public | Mid/large; "not for small brokerages" per Lido | [viago](https://viago-website.pages.dev/cargowise-ai-features.html); [Lido](https://www.lido.app/blog/best-customs-document-processing-software) |
| Descartes | Hosted ABI, post-entry compliance | "From €200/month" (aggregator, unverified) | Small independent to enterprise (vendor) | [Descartes](https://descartes.com/solutions/customs-and-regulatory-compliance/customs-declarations/united-states); [FitGap](https://us.fitgap.com/products/021173/descartes-customs-compliance-suite) |
| Magaya | ABI and forwarding software | Not found | Small/mid forwarders [UNVERIFIED background] | Gap |
| Zonos Classify | HS classification API | 100k classifications $3,100; 250k $5,125; 500k $5,500; platform includes 10k; subscription $3,000/yr + $4,000 setup or $2,500/$4,000 plans (conflicting) | Ecommerce brands | [Zonos Classify pricing](https://zonos.com/zh-tw/docs/supply-chain/classify/pricing); [Zonos Shopify pricing](https://zonos.com/zh-hk/docs/global-ecommerce/shopify/shopify-pricing) |
| Avalara / 3CE | Classification; publishes refund guides | Not found | Mid/enterprise | [Avalara blog (round 1)](https://www.avalara.com/blog/en/north-america/2026/02/how-to-request-tariff-refunds.html) |
| Gaia Dynamics | AI HTS classification, tariff calculation, entry audits; Tariff Audit Engine for IEEPA refunds (Mar 2026); "92% accuracy within 30 seconds" (company claim); $7M seed | Tiered from free to enterprise, 30-day trial | Importers, brokerages, law firms; NCBFAA 2025 exhibitor | [NCBFAA exhibitor page](https://ncbfaa.org/membership-benefits/conferences-events/annual-conference-2025/exhibitors/current-exhibitors-and-floorplan/gaia-dynamics); [Pulse 2.0](https://pulse2.com/gaia-dynamics-raises-7-million-seed-round-led-by-corazon-capital); [PR, 3 Mar 2026](https://business.mammothtimes.com/mammothtimes/article/prunderground-2026-3-3-gaia-dynamics-launches-tariff-audit-engine-to-help-importers-unlock-refund-opportunities-after-supreme-court-ieepa-decision); [FreightWaves](https://www.freightwaves.com/?p=526089) |
| Amari AI | "Autonomous AI platform" for customs clearance, HTS classification, filing; seed 19 Feb 2026, $4.5M total | Not found | Logistics firms | [Caplight](https://www.caplight.com/company/amari) |
| Alchemize | AI-native customs brokerage (YC Spring 2026, about $500K; dates inconsistent) | Not found | Importers (competes with brokers) | [NeuronFeed](https://neuronfeed.com/startups/alchemize) |
| Expedock, Cargo Docket, CargoIQ, Wove | Extraction into CargoWise | Not public | Forwarders/brokers on CargoWise | Q5 links |
| Raft, Camtom, Deep Cognition, iCustoms (round 1); Nabu, Digicust (EU) | AI customs automation | Not found | Various | [Raft](https://www.raft.ai/resources/blog-posts/why-customs-compliance-breaks-down-and-how-forwarders-can-fix-it-in-2025); [Nabu](https://www.pulse.bot/supply-chain/news/nabu-raises-3m-to-scale-digital-customs-in-europe-e3edf5ed-4f74-40b2-b0cf-bdb564a85431/); [Digicust](https://www.vestbee.com/insights/articles/digicust-secures-2-3-m); [iCustoms](https://www.multimodal.org.uk/article/icustoms-raises-2-2-million-to-revolutionise-trade-compliance-with-ai) |
| Flexport | Customs for its own customers; tariff tooling | Not found | Its own shippers | [Flexport (round 1)](https://www.flexport.com/solutions/simplify-customs/) |
| Passport | Duty drawback | Not found; "over 85% of eligible businesses never file" (vendor claim; round 1) | DTC/importers | [Passport](https://passportglobal.com/blog/recover-us-import-tariffs-duty-drawback-explained/) |
| Refund firms (Tariff Refund Solutions, Clearit, Leyton, law firms) | CAPE, protests, litigation | 3–28% contingency; 5% norm; flat fee + % | Importers | Q14 |

**Problem 2 competitors**
- **First AML:** signed "six of Australia's top ten largest law firms" and is the "preferred AML partner" of the Real Estate Institute of Australia (REIA). Its platform covers ID verification, risk assessment, ongoing monitoring and audit readiness. These are vendor claims from July 2025 — [AAP release](https://www.aap.com.au/aapreleases/cision20250702ae22703). It also runs a one-stop-shop partner offer ($99 training) — [First AML](https://firstaml.com/au/about/company/partners/one-stop-shop)
- **InfoTrack:** a Tranche 2 "Compliance Centre" and an AML/CTF readiness roadshow (sponsored content). LEAP links to "Preparing for AML/CTF Tranche 2 Reforms with LEAP and InfoTrack." No prices found — [Lawyers Weekly: InfoTrack Compliance Centre](https://www.lawyersweekly.com.au/sme-law/44132-prepare-for-aml-ctf-tranche-2-with-infotrack-s-compliance-centre); [Lawyers Weekly: roadshow](https://www.lawyersweekly.com.au/biglaw/43062-infotrack-leads-the-profession-on-aml-ctf-readiness-a-roadshow-for-2026-and-beyond); [LEAP](https://www.leap.com.au/system-requirements)
- **Forms Live** (real estate forms platform) integrates easyAML, First AML, AMLHUB and APLYiD. Free pilots were common until 1 July 2026 — [Forms Live webinar](https://www.formslive.com.au/resources/webinars/aml-for-real-estate-webinar/)
- **Per-check ID tools:**
  - Didit lists US$0.15 per ID verification, a US$0.33 identity bundle and US$0.20 per AML screen (vendor) — [Didit](https://didit.me/blog/austrac-tranche-2-aml-ctf-customer-due-diligence/)
  - ARCaml uses prepaid credits (1 credit = 1 entity) (per search summary)
  - Market range A$13–A$40 per individual check (unverified; Q4)
- **Program software and consultants:** A$490 a year (program software); A$4,500 / A$11,000 fixed fees (GateCrown); A$5,000–A$15,000 legal drafting (Q5)
- **Managed services:** AML Partners (300–400 clients, vendor claim); Kit Legal subscription (Q5)
- **Practice software:** Smokeball lists $49 per user per month with no AML module mentioned — [Capterra](https://www.capterra.com/p/133656/smokeball/). No AML module was confirmed for LEAP itself (it partners with InfoTrack) or for Xero Practice Manager.
- **Not found:** Kyckr's Australian Tranche 2 pricing (gap).
- **Other vendors publishing Tranche 2 content:** Persona, Zyphe, Legl, NameScan, Scantek, VinciWorks, Fenergo, Tookitaki — [Persona](https://withpersona.com/blog/tranche-2-australia); [NameScan](https://namescan.io/insights/austrac-tranche-2-what-real-estate-agents-must-do-before-1-july-2026/); [Tookitaki](https://tookitaki.com/compliance-hub/tranche-2-aml-reforms-australia)

### Inferences
- **P1 crowding is high for software and rising for refunds.** It is moderate for "outsourced entry-writing desk for small brokers": no vendor found sells per-entry human-checked preparation in the US. Offshore customs back-office firms likely exist [UNVERIFIED background], so this needs one more check.
- **P2 crowding is high for ID checks** (cents to tens of dollars). It is moderate for entity/trust CDD and ongoing-monitoring services. Incumbents sit inside the buyers' workflow tools (Forms Live, LEAP and InfoTrack, REIA–First AML).

### Gaps
- Prices not found: Magaya, CargoWise, Avalara classification, First AML, InfoTrack, Kyckr, AML Partners.
- I could not check whether offshore BPOs already sell US entry writing per entry.

---

## Q8. Will the problem grow or shrink as AI improves over 24 months? How long will tariff churn and refund work last?

### Takeaway
- **P1:** raw keying will shrink, because AI parsing is now inside CargoWise and classification AI claims 92% accuracy. The licensed-broker review, tariff-stack logic and exception work stay.
- **P1 refund work** is a 12–18 month tail, from now to roughly late 2027 (inference). Section 301 churn has no end date found.
- **P2:** demand grows as enforcement starts and about half the market is still not enrolled. AI makes individual ID checks almost free, so value moves to entity/trust ownership tracing, monitoring, suspicious-matter judgement and program upkeep.

### Cited Findings
- CargoWise ships native AI commercial-invoice parsing (May 2026 page) — [viago](https://viago-website.pages.dev/cargowise-ai-features.html)
- Gaia Dynamics claims 92% HTS accuracy within 30 seconds (company claim) — [Pulse 2.0](https://pulse2.com/gaia-dynamics-raises-7-million-seed-round-led-by-corazon-capital)
- AI-native brokerages are appearing (Alchemize, YC Spring 2026) — [NeuronFeed](https://neuronfeed.com/startups/alchemize)
- Refund progress: $134.7B accepted and $122B sent for payment by mid-September 2026; Phase 3 targets finally liquidated, court-ordered entries — [C.H. Robinson](https://www.chrobinson.com/en-au/resources/insights-and-advisories/client-advisories/2026q3/09-17-26-cbp-cape-phase-3-ieepa-refunds/)
- Section 301 forced-labour tariffs replaced Section 122, with tariff-rate quotas still to be set up for four economies (more changes ahead) — [Thomson Reuters](https://www.thomsonreuters.com/en-us/help/onesource-global-trade/regulatory-insights/2026/july-24th/us-imposes-section-301-forced-labor-tariffs-60.html)
- P2 enforcement has begun (s167 notices, 28 Aug 2026), while enrolment was about 12–50% by sector — [Clyde & Co](https://www.clydeco.com/en/insights/2026/08/austrac-takes-compliance-action-in-relation-to-tra)
- ID verification is priced at cents (US$0.15 per check, Didit, vendor) — [Didit](https://didit.me/blog/austrac-tranche-2-aml-ctf-customer-due-diligence/)

### Inferences
**P1 timing:**
- IEEPA duties were collected from about February 2025 to February 2026. Entries normally liquidate about 314 days after entry, and protests are due within 180 days of liquidation [UNVERIFIED background].
- On those timelines, refund, protest and reliquidation work tails off between mid-2027 and late 2027. After that, the refund line of business disappears unless new tariffs are struck down.

**P1 durability:**
- Tariff churn is policy-driven. Section 301 actions have no automatic expiry found, the quotas are still to come, and Section 232 lists keep expanding [UNVERIFIED background]. Plan for continued churn through 2027, but with uncertainty.
- Within 24 months, per-entry keying labour may fall 50%+ at brokers who adopt CargoWise AI (inference). The service must sell exception handling and checked output, not keystrokes.

**P2 durability:**
- Year 1 (2026–27) is setup plus a CDD backlog. Years 2+ bring recurring CDD, monitoring, independent reviews and AUSTRAC reporting.
- Per-check price compression is certain. Recurring work persists because the law requires risk-based judgement and a named officer.

### Gaps
- No source on AUSTRAC's planned supervision intensity for 2027.
- No source on whether Section 301 forced-labour rates have a sunset or review date.

---

## Q9. How to reach these buyers

### Takeaway
- **P1:** NCBFAA (the annual conference and its exhibitor floor, where Gaia exhibited), regional broker associations, software ecosystems (CargoWise, Descartes, Magaya partners), trade press (The Loadstar, JOC, FreightWaves, Supply Chain Dive), and the CBP CSMS email list.
- **P2:** state law societies (NSW already publishes small-firm AML guides), the Law Council, ALPMA, REIA and state REIs (REIA endorses First AML), Forms Live and PEXA as embedded channels, CPA Australia, CA ANZ, IPA, and the trade press (Lawyers Weekly, Accounting Times, Real Estate Business, IFA, Accountants Daily).

### Cited Findings
- **NCBFAA:** the 2025 Annual Conference exhibitor list (Gaia Dynamics exhibited) — [NCBFAA exhibitors](https://ncbfaa.org/membership-benefits/conferences-events/annual-conference-2025/exhibitors/current-exhibitors-and-floorplan/gaia-dynamics)
- **CBP CSMS** (govdelivery) announces broker-list updates and is the channel brokers read — [CSMS bulletin](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/3d7f2c6)
- **Australian law:**
  - Law Society of NSW small-practice guide and FAQs — [Law Society NSW](https://www.lawsociety.com.au/anti-money-laundering-and-counter-terrorism-financing-reforms-faqs)
  - Law Council and state law society tools "now live" — [Legl](https://legl.com/resources/resource/five-weeks-to-tranche-2-what-australian-law-firms-must-still-get-right-before-1-july)
  - ALPMA event "Money and matters – a lawyer's guide to navigating Tranche 2" — [ALPMA](https://www.alpma.com.au/events/money-and-matters-a-lawyers-guide-to-navigating-tranche-2/)
  - Queensland Law Society's Proctor covers Tranche 2 — [QLS Proctor](https://www.qlsproctor.com.au/?p=24942)
- **Australian real estate:** REIA–First AML partnership — [AAP](https://www.aap.com.au/aapreleases/cision20250702ae22703). Forms Live AML integrations — [Forms Live](https://www.formslive.com.au/resources/webinars/aml-for-real-estate-webinar/). PEXA AML hub — [PEXA](https://www.pexa.com.au/aml/key-dates-tranche-2/). Trade press — [Real Estate Business](https://www.realestatebusiness.com.au/commercial/32209-aml-partners-on-track-to-serve-over-300-tranche-2-businesses-with-fully-outsourced-austrac-compliance-platform)
- **Australian accounting:** Accounting Times — [Accounting Times](https://www.accountingtimes.com.au/profession/access-group-warns-of-guidance-gap-ahead-of-tranche-2-aml-ctf). Financial advisers — [IFA](https://www.ifa.com.au/kit-legal-releases-aml-ctf-subscription-service-ahead-of-tranche-2-reforms)

### Inferences
- **P1:** sell to brokers, not importers. Brokers own the licence and the client, and have shown they will monetise refunds (the Loadstar 10–15% headline). Regional associations: Los Angeles Customs Brokers & Freight Forwarders Association, the NY/NJ forwarders and brokers association, the Florida Customs Brokers & Forwarders Association, the Laredo and Texas broker associations, and the Chicago customs broker association [UNVERIFIED background: names not re-checked].
- **P2:** the fastest route is partnership with a channel that lacks a human service layer. Examples: a smaller state REI not tied to First AML, an accounting software or practice-management vendor, or a law society's referral list. Selling directly to principals works through Lawyers Weekly SME and REI events.

### Gaps
- No 2026–27 event dates were verified (NCBFAA annual conference, REIA, CPA Congress).
- Accountants Daily returned no results in my search.

---

## Q10. Roughly how many companies have the problem

### Takeaway
- **P1:**
  - 14,454 licensed individual brokers (CBP) and about 6,200 brokerage firms (vendor estimate).
  - CBP publishes a quarterly Permitted Customs Broker Listing.
  - More than 400,000 importers (unconfirmed market report); CBP also deactivated about 4.8M dormant IOR accounts in 2026.
- **P2:**
  - About 80,000–100,000 newly regulated businesses (AUSTRAC/commentary).
  - About 17,000 law practices and about 45,500 real estate services businesses.
  - No current official count of accounting practices; about 27,500 is implied (low-confidence estimate).
  - About 40,600 Tranche 2 enrolments by 17 September 2026 (unverified vendor table).

### Cited Findings
- **Licensed brokers:** about 14,454 active licensed customs brokers — [CBP](https://cbp.gov/trade/programs-administration/customs-brokers/becoming-customs-broker) (round 1)
- **Brokerage firms:** 6,200 (vendor, "as of 2026") — [Camtom](https://www.camtomx.com/en/blog/what-is-a-customs-broker) (round 1)
- **Aggregator count:** one aggregator lists 2,483 customs brokers in its database (unit unclear) — [Base](https://open-gov.usebase.io/companies?page=224)
- **Importers:** more than 400,000 US importers in 2025, up about 60% since 2019, 38% of them micro-importers (exact page unconfirmed; round 1) — [Mordor Intelligence](https://mordorintelligence.com/industry-reports/united-states-customs-brokerage-market)
- **Dormant IOR accounts:** about 4.8M deactivated — [Thomson Reuters](https://www.thomsonreuters.com/en-us/help/onesource-global-trade/regulatory-insights/2026/september-17th/cbp-importer-of-record-data-accuracy-begins) / [Shopappy](https://shopappy.com/trade/tariffs-customs/cbp-importer-number-voiding-begins) (attribution approximate)
- **CAPE:** about 286,000 declarations by mid-September 2026 — [C.H. Robinson](https://www.chrobinson.com/en-au/resources/insights-and-advisories/client-advisories/2026q3/09-17-26-cbp-cape-phase-3-ieepa-refunds/)
- **AUSTRAC's projection:** the regulated population grows "from around 19,000 to close to 100,000" (AUSTRAC, via search summary) — [AUSTRAC news](https://www.austrac.gov.au/new-and-media/news/austrac-opens-enrolment-new-professions-next-step-aml-reforms). "18,000 … to approximately 100,000" — [Persona](https://withpersona.com/blog/tranche-2-australia). "Over 80,000" — [AML Intelligence, Aug 2025](https://www.amlintelligence.com/2025/08/news-austrac-publishes-new-aml-rules-for-80000-tranche-2-businesses/). 80,000–90,000 per a law firm guide (search summary).
- **Enrolments to 17 Sep 2026** (vendor table, unverified; conflicts with Clyde & Co's statement that exact figures are unavailable) — [Zyphe enrolment guide](https://www.zyphe.com/resources/blog/austrac-tranche-2-enrolment-guide) / [Zyphe news](https://www.zyphe.com/resources/news/austrac-tranche-2-aml-reforms-july-2026); which page holds the table is unconfirmed:
  - Real estate 18,350
  - Accounting/professional services 13,780
  - Lawyers 6,580
  - Conveyancers 1,600
  - Jewellers/dealers 320
  - Total about 40,630
- **Law:** nearly 17,000 private law practices; 97,500 solicitors (2024); over 90% of practices have fewer than five principals — [Law Society NSW](https://www.lawsociety.com.au/australian-legal-profession-records-strong-growth-more-women-enter-profession)
- **Real estate:** 45,522 real estate services businesses (2026) — [IBISWorld](https://img2.ibisworld.com/australia/number-of-businesses/real-estate-services/539/)
- **Accounting:** the only official count is 9,860 practices in 2001–02 (old) — [ABS 8668.0](https://www.abs.gov.au/AUSSTATS/abs@.nsf/7d12b0f6763c78caca257061001cc588/4c030f60cdaba0bdca256d330080dfd6!OpenDocument)

### Inferences (estimates, cross-source, low confidence)
- **Real estate:** 18,350 enrolled ÷ about 40% enrolled (Clyde & Co) ≈ 45,900 agencies. This is consistent with IBISWorld's 45,522.
- **Accounting:** 13,780 ÷ about 50% ≈ 27,600 accounting practices in scope (estimate).
- **Law:** 6,580 ÷ 12–14% ≈ 47,000–55,000, which does **not** fit about 17,000 practices. Possible reasons:
  - the Zyphe figure may count individual enrolments or later dates;
  - Clyde & Co's percentage may use a different base;
  - many law practices may not provide designated services.
  - Treat the law-firm numbers as unresolved.
- **P1 serviceable market:** about 6,200 firms; the skew suggests about 4,000–5,000 are small (under 50 staff) (inference).

### Gaps
- No AGD Regulation Impact Statement sector breakdown was found.
- The CBP Permitted Broker Listing row count was not read (fetch blocked).
- No current ABS count of accounting practices.

---

## Q11. The strongest argument against each opportunity

### Takeaway
- **P1:** the buyer (a small broker) is itself a service business with thin margins. Its software vendor now bundles AI extraction, and US rules keep records and legal control onshore. The refund windfall, which would fund early sales, ends in 2027.
- **P2:** revenue per client is small, about A$500–A$2,600 a month. Incumbents sit inside the forms and practice software, regulators promise leniency in the first year, and some firms will simply stop offering designated services.

### Cited Findings
- **P1 counter-evidence:**
  - CargoWise native parsing — [viago](https://viago-website.pages.dev/cargowise-ai-features.html)
  - Original records, including electronic ones, must sit within the US customs territory — [19 CFR 111.23 (Cornell)](https://www.law.cornell.edu/cfr/text/19/111.23)
  - VC-funded entrants — [Gaia](https://pulse2.com/gaia-dynamics-raises-7-million-seed-round-led-by-corazon-capital); [Amari](https://www.caplight.com/company/amari); [Alchemize](https://neuronfeed.com/startups/alchemize)
  - Refunds are largely processed already ($122B sent for payment) — [C.H. Robinson](https://www.chrobinson.com/en-au/resources/insights-and-advisories/client-advisories/2026q3/09-17-26-cbp-cape-phase-3-ieepa-refunds/)
- **P2 counter-evidence:**
  - The CEO's leniency assurance — [Law Society NSW](https://www.lawsociety.com.au/solicitors-welcome-austrac-assurances-amlctf)
  - Firms exiting designated services — [easyAML](https://knowledge.easyaml.com/can-i-stop-offering-designated-services)
  - REIA–First AML — [AAP](https://www.aap.com.au/aapreleases/cision20250702ae22703)
  - Forms Live integrations — [Forms Live](https://www.formslive.com.au/resources/webinars/aml-for-real-estate-webinar/)
  - Free NSW guide — [Law Society NSW](https://www.lawsociety.com.au/new-guidance-help-small-practice-amlctf-compliance)
  - A$490-a-year software — [vendor](https://sentine-web.pages.dev/pricing)

### Inferences
- **P1** survives only as "white-label prep desk for small brokers": AI extraction plus an offshore checker, with the US licensed broker signing. The buyer must trust an outsider with entry data and supervision risk. Sales cycles will be relationship-driven.
- **P2** is attractive mainly at "bundle" price points (A$500–A$1,500 a month per firm) and only with very low delivery cost per file. A founder needs many clients (for example, 100 firms × A$800 = A$80k a month, about US$52k) to build a meaningful business (estimate).

### Gaps
- No churn or price-sensitivity data for Australian AML services.

---

## Q12. Delivery constraints for an offshore (non-US / non-Australian) team

### Takeaway
- **P1:** an offshore team can prepare data, but cannot be the broker of record.
  - A US licensed broker must exercise "responsible supervision and control."
  - Original records, including electronic ones, must be kept within the US customs territory. In 2012 CBP said electronic records must sit on a server physically in the US.
  - Turnaround is tied to US cargo arrival hours, which means night shifts for an Asia-based team.
- **P2:** the reporting entity stays responsible for CDD done by others (Division 7). Reliance on third parties is allowed through a written "CDD arrangement" (s37A) or case by case (s38). The AML/CTF compliance officer must be a natural person within the firm. Australian time zones overlap well with South Asia (inference).

### Cited Findings
**Problem 1**
- **Supervision duty:** sole-proprietor brokers and licensed officers must exercise responsible supervision and control, and the firm must employ enough licensed brokers relative to the work — [eCFR 111.28](https://www.ecfr.gov/current/title-19/chapter-I/part-111/subpart-C/section-111.28)
- **CBP's supervision factors** include training, instructions to employees, business volume, reject rates, employee access to current regulations, and availability of licensed brokers for consultation — [CBP fact sheet (2022)](https://cbp.gov/sites/default/files/assets/documents/2022-Oct/Fact%20Sheet%20-%20Responsible%20Supervision%20and%20Control_0.pdf)
- **Record location:** "A licensed customs broker must maintain originals of the records … including any records stored in electronic formats, within the customs territory of the United States," for at least 5 years — [19 CFR 111.23 (Cornell)](https://www.law.cornell.edu/cfr/text/19/111.23)
- **Servers:** in the 2012 rule, CBP said electronic documentation must sit on a server physically within US customs territory where CBP can issue a summons — [Federal Register 2012 (CBP Dec. 12-12)](https://www.govinfo.gov/content/pkg/FR-2012-06-08/pdf/2012-13907.pdf)
- **Offshore backups:** a 2020 ruling (HQ H292868) answered WiseTech's question about backups in Australia and the UK. The outcome was not visible in search results — [Base: H292868](https://open-gov.usebase.io/rulings/H292868)
- **CAPE filers:** only the IOR or an authorised licensed broker may submit CAPE declarations — [cape-guide](https://cape-guide.pages.dev/blog/lawyer-broker-recovery-firm-who-files-ieepa-refund/)

**Problem 2**
- **Liability stays with the firm:** "Division 7 of the AML/CTF Act provides that in general a reporting entity is ultimately responsible for the actions of anyone else who conducts customer due diligence on its behalf" — [Corrs](https://corrs.com.au/insights/changes-to-anti-money-laundering-laws-have-come-into-effect-what-now)
- **Reliance routes:** s37A allows ongoing reliance on a third party's identification under a written "CDD arrangement"; s38 allows case-by-case reliance — [AUSTRAC reliance guidance](https://www.austrac.gov.au/business/core-guidance/customer-identification-and-verification/reliance-customer-identification-procedures-third-party). The reforms widened reliance — [HSF Kramer](https://www.hsfkramer.com/insights/2024-12/unwrapping-the-aml-ctf-reforms-passed-by-parliament-and-austracs-consultation-paper)
- **Program obligations:** a new section 26G sets AML/CTF program obligations, including complying with CDD — [Mallesons](https://www.mallesons.com/au/en/insights/latest-thinking/aml-ctf-amendment-bill-introduced-into-parliament)
- **Compliance officer:** must be a natural person within the firm — [CCP](https://www.ccp.com.au/news/tranche-2-aml-ctf-obligations-accountants/) / [Beancount](https://beancount.io/blog/2026/07/28/austrac-tranche-2-accountants-bookkeepers-guide)
- **Outsourced model in market:** the agency keeps the customer relationship and the provider does the regulator-facing work — [Real Estate Business](https://www.realestatebusiness.com.au/industry/32233-how-australian-businesses-can-outsource-compliance-and-meet-their-tranche-2-aml-obligations-with-aml-partners)

### Inferences
**P1 operating model:**
- Offshore staff work inside the broker's US-hosted ABI system (for example, CargoWise cloud or Descartes hosted) through remote access. They prepare data and do not file or sign.
- The broker's licensed staff review before transmission.
- Keep all documents in the broker's US system, with no local copies.
- Check the outcome of H292868 and whether CBP views remote access from abroad as acceptable. **[UNVERIFIED]:** 19 CFR 111.28(b) requires brokers to report employee details to CBP. Whether offshore contractors count as "employees" and must be reported was not checked.

**P1 real-time needs:**
- Truck border entries (Laredo and similar) and air entries need near-real-time work during US hours. Ocean entries can be prepared before arrival (inference).
- A South Asia team would need night shifts for US Eastern and Pacific time.

**P2 operating model:**
- Act as an outsourced service provider (agent) under a written agreement.
- The firm's compliance officer approves risk ratings and decisions to proceed. Records stay in the firm's or vendor's system.
- **[UNVERIFIED background]:** CDD records must be kept for 7 years, and the Privacy Act's cross-border disclosure principle (APP 8) applies when personal information goes offshore. The client must take "reasonable steps" to ensure the overseas recipient complies.
- Consider Australian data hosting to ease buyer concerns. No AUSTRAC data-residency rule was found.

**P2 time zones (inference):**
- AEDT is UTC+11 in October; Pakistan is UTC+5 (6 hours behind Sydney). A 9 a.m.–6 p.m. Pakistan shift covers 3 p.m.–midnight Sydney.
- Pre-settlement CDD deadlines can be met by working overnight to an Australian morning.

### Gaps
- No CBP guidance on foreign-located entry preparers or ACE Portal access from abroad was found.
- No AUSTRAC text on offshore agents; no AML/CTF Rules text on outsourced CDD controls.
- Whether the new Rules require an Australia-resident compliance officer is unverified.

---

## Q13. Where to find 15 named prospects within 14 days

### Takeaway
- **P1:** pull the CBP Permitted Customs Broker Listing (public, quarterly; filer code, name, city/state, phone, email). Filter to single-office brokers at busy ports, then cross-check job boards for firms hiring "customs entry writers" (a live pain signal). Contact the owner/president or the licensed broker who runs operations.
- **P2:** no public AUSTRAC list of enrolled entities was found. Use state law society "find a lawyer" directories, CPA Australia, CA ANZ and IPA "find an accountant" directories, state REI member directories, and the Australian Institute of Conveyancers directory. Contact the principal or practice manager (the likely AML/CTF compliance officer).

### Cited Findings
- **CBP Permitted Customs Broker Listing:** public at cbp.gov/about/contact/brokers-listing, updated quarterly, built from the National Permit record in ACE. It includes filer code, broker name, city/state, phone and email — [CBP CSMS bulletin](https://content.govdelivery.com/accounts/USDHSCBP/bulletins/3d7f2c6); [CBP brokers listing](https://www.cbp.gov/about/contact/brokers-listing)
- **Broker profiles by filer code** (aggregator) — [Base](https://open-gov.usebase.io/companies?page=224)
- **Firms hiring entry writers in 2026:**
  - Estes Forwarding (Richmond / North Chesterfield, VA)
  - Prosimo.io (Elk Grove Village, IL)
  - An Altius Talent client in Dallas (unnamed)
  - DSV, DP World, RXO (large; not ideal targets)
  - Sources: see Q4 links.
- **NCBFAA 2025 exhibitor list**, useful for mapping competitors — [NCBFAA](https://ncbfaa.org/membership-benefits/conferences-events/annual-conference-2025/exhibitors/current-exhibitors-and-floorplan/gaia-dynamics)
- **Real estate firms already buying outsourced help** (AML Partners' 300–400 clients; competitor's customers) — [Real Estate Business](https://www.realestatebusiness.com.au/commercial/32209-aml-partners-on-track-to-serve-over-300-tranche-2-businesses-with-fully-outsourced-austrac-compliance-platform)
- **Law firm structure:** over 90% of Australian law practices have fewer than five principals, so most prospects are micro-firms — [Law Society NSW](https://www.lawsociety.com.au/australian-legal-profession-records-strong-growth-more-women-enter-profession)

### Inferences
**P1 14-day plan:**
1. Download the CBP listing.
2. Filter it to Laredo, Miami, Los Angeles/Long Beach, NY/NJ, Chicago and Atlanta.
3. Drop the top 50 brokers.
4. Pick 15 one- or two-office firms with a website showing 2–30 staff and a CargoWise, Descartes or Magaya mention.
5. Email the listed address, then follow up by phone.
6. Add NCBFAA member directory and regional association member lists [UNVERIFIED that they are public].

**P2 14-day plan:**
1. Start with conveyancers (AIC state divisions) and boutique accounting firms that offer company/trust set-up, since they are clearly in scope.
2. Add real estate agencies in REINSW, REIV or REIQ directories with 1–3 offices.
3. Look for firms named in Lawyers Weekly SME or Real Estate Business stories about Tranche 2.
4. Treat a firm's website "AML" or "verification of identity" page as a pain signal.

**Halal screen during listing:**
- P1: drop brokers whose sites centre on wine, spirits or beer imports.
- P2: drop firms whose main clients are lenders, casinos or bookmakers (see Q14).

### Gaps
- I did not confirm whether AUSTRAC publishes any searchable list of Tranche 2 enrolled entities. None was found.
- I did not confirm the availability of the NCBFAA member directory, or of CPA Australia, CA ANZ, IPA and REI directories (background knowledge only).
- No named Australian small-firm prospects were found in search results.

---

## Q14. Pricing shapes buyers already accept

### Takeaway
- **P1:** importers already accept:
  - per entry ($75–$400), plus per PGA line ($15–$50), ISF ($25–$50) and bonds;
  - refund contingency (3–28%, with about 5% the recent broker norm and 10–15% claimed);
  - flat fee plus percentage;
  - classification per SKU (cents per API call at volume).
  - Brokers buy software by monthly subscription and per user.
- **P2:** firms already accept per-check fees (A$13–A$40 individual, A$28–A$65 entity, unverified), a monthly platform fee (A$59–A$300+), fixed-fee program builds (A$4,500–A$11,000), annual software (A$490), per-person training ($99), and managed-service retainers (AML Partners, price unknown).

### Cited Findings
**Problem 1**
- **Per entry:** $150–$400+ in one source, $100–$250 in another, $75–$250 plus disbursements in a third. Tiers by line count of $150–$250 (1–3 lines) and $250–$400 (5+ lines). PGA filings $15–$50 per line. ISF $25–$50. Continuous bond $400–$750 a year — [FreightAmigo](https://www.freightamigo.com/en/blog/logistics/customs-broker-guide-costs-definition-and-essential-services-in-2026/); [Suaid Global](https://suaidglobal.pages.dev/insights/customs-broker-fees-2026); [LandedCost guide](https://landedcost-2fn.pages.dev/guides/customs-brokerage-fees/); [StrixSmart](https://strixsmart.com/resources/blog/customs-broker-cost)
- **Merchandise processing fee (government) FY2026:** 0.3464% of value, minimum $33.58, maximum $651.50. Another source gives a $33.68 minimum — [MPF calculator](https://merchandise-processing-fee-checker.pages.dev/)
- **Refund contingency:**
  - 3–28% by claim size and path; a blended example of about 20% on a $2M claim (vendor) — [Tariff Refund Solutions FAQ](https://v0-tariff-refund-solutions.pages.dev/faq)
  - Flat fee plus a small %, starting at $200 for the first entry for recoveries under $5,000 (vendor) — [Clearit](https://clearitusa.com/ieepa-refund-pricing-what-importers-need-to-know/)
  - 5% service fee capped at $20,000, minimum $500 (pooled-account agreement PDF) — [Constant Contact-hosted agreement](https://files.constantcontact.com/1f332db5401/cadad9cd-0aef-44fc-aab1-a30b11d6a5ec.pdf)
  - Brokers taking 3–10%, with 5% "the loose market norm" (vendor guide) — [cape-guide](https://cape-guide.pages.dev/blog/lawyer-broker-recovery-firm-who-files-ieepa-refund/)
  - 10–15% headline — [The Loadstar](https://theloadstar.com/?p=308226)
- **Classification:** Zonos roughly $0.011–$0.031 per classification at 100k–500k volume — [Zonos](https://zonos.com/zh-tw/docs/supply-chain/classify/pricing)
- **Software:** Descartes "from €200/month" plus per-user fees (aggregator, unverified) — [FitGap](https://us.fitgap.com/products/021173/descartes-customs-compliance-suite)

**Problem 2**
- **Per check and platform fees** (unverified guide) — [niftycomputing](https://niftycomputing-au.pages.dev/toolkit/real-estate/aml-ctf-guide). Didit US$0.15–US$0.53 per check bundle (vendor) — [Didit](https://didit.me/blog/austrac-tranche-2-aml-ctf-customer-due-diligence/)
- **Fixed-fee programs:** A$4,500 / A$11,000; review about A$1,500 — [GateCrown](https://gatecrown.pages.dev/accounting)
- **Annual software:** A$490 — [vendor](https://sentine-web.pages.dev/pricing)
- **Training:** $99 per person — [First AML](https://firstaml.com/au/about/company/partners/one-stop-shop)
- **Government cost benchmark:** A$28,650 upfront and A$23,250 a year ongoing — [Scantek citing the RIS](https://scantek.com/how-much-will-aml-ctf-tranche-2-compliance-cost-your-business/)

### Inferences (pricing hypotheses for a founder; not sourced prices)

**P1 white-label prep desk for brokers:**
- About $15–$35 per prepared entry (10–25% of the broker's $150 average fee), or a monthly retainer of $3,000–$8,000 for about 100 entries a week. That sits below the $4,400–$13,200 labour cost in Q4 (estimate).
- Refund add-on: a share of the broker's 5% fee, ending in 2027.

**P2 per-firm bundle:**
- A$600–A$1,500 a month (US$390–$975) covering CDD file preparation (ID checks passed through at cost), entity/trust beneficial-ownership tracing, monthly rescreening and records.
- A$2,500–A$5,000 one-off for program set-up or uplift. Price per CDD file for overflow: A$40–A$120 per individual or entity file (estimate). This undercuts the A$1,940-a-month government estimate.

**Shariah flags (no rulings given):**
- **P1:**
  - CAPE refunds include interest ($122B "including interest").
  - A contingency fee on a refund that includes interest may raise a question.
  - Many small brokers serve wine and spirits importers.
  - Customs bonds are surety/insurance products.
  - Pooled refund accounts may hold funds in interest-bearing accounts.
- **P2:**
  - Tranche 2 clients include dealers in precious metals (gold and silver trade has its own Shariah rules).
  - Accountants' and lawyers' end clients may include conventional lenders, casinos or bookmakers.
  - Most property sales use interest-bearing mortgages.
  - The CDD service itself is a compliance service, but client screening is advisable.

### Gaps
- No Australian source for per-file pricing of human-performed CDD (only per-check tool prices and fixed program fees).
- No US source for per-entry pricing of outsourced entry preparation, as opposed to the broker's fee to the importer.
