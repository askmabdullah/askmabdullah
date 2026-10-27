# Lens 04: New Rules (2025-2027) That Create Recurring Compliance Work

Research date: 27 October 2026. Scope: US first, then UK and Australia.

**Method and access limits (read first).** This session ran 12 web searches before the shared search budget ran out ("limit: 200 WebSearch calls per turn, shared by every agent"). After that, WebFetch failed on every domain tried (getaddrinfo ENOTFOUND for lw.com, dwt.com, austrac.gov.au, ato.gov.au, gov.uk, cms.gov). Direct HTTPS to gov.uk, ato.gov.au and austrac.gov.au was refused by the session's egress proxy (403). As a result:
- **Verified this session:** statuses and numbers that carry a URL below come from search-result summaries of law-firm, government or trade pages dated 2025-2026. I could not open the full pages, so treat each detail as "reported by" that source.
- **Not re-verified this session:** anything marked **[UNVERIFIED: training knowledge, pre-mid-2026]** comes from background knowledge. It must be re-checked before anyone relies on it. This applies to every UK and Australian rule, plus CMS-0057-F, the CCPA regulations, CTA/BOI, 1099-K, Texas TRAIGA, Illinois HB 3773, NYC LL144, PCI DSS, EAA, OSHA heat and the DOL rules.
- **Labels:** "vendor claim" marks a number from a company that sells a fix. "Estimate" marks my own arithmetic, with the math shown.

---

## Key Question 1: Which 2025-2027 rules create ongoing (not one-off) work, and what is each rule's current status as of Oct 2026?

### Takeaway
Many headline 2024-2025 rules were vacated, delayed, replaced or narrowed by October 2026, or never finalized. Examples: FinCEN real-estate reporting (vacated), FTC click-to-cancel (vacated), the TCPA one-to-one consent rule (vacated), FSMA 204 (moved to 2028), the HIPAA Security Rule update (still proposed, target July 2027), the Colorado AI Act (replaced, Jan 2027), ADA Title II (pushed to 2027/2028), SB 261 (enjoined) and IEEPA tariffs (struck down). The rules still producing **weekly** work are mostly older or state-level rules with active private lawsuits or enforcement: Washington pay transparency, CCPA opt-outs, and customs/tariff churn. New sector regimes add to these: CMMC, Australia's AML/CTF Tranche 2 and UK Awaab's Law. Climate, AI-audit and privacy-assessment rules are mostly **annual or one-off** work.

### Cited Findings

**Status table (US)**

- **Colorado AI Act (SB 24-205): REPLACED and NARROWED.** Gov. Polis signed SB 26-189 on May 14, 2026. It repeals and replaces SB 24-205 and moves the effective date to **January 1, 2027**. The new law shifts toward consumer transparency and rights (an "ADMT" regime), and one source says it drops the duty of care, risk programs and impact assessments. Votes were 57-6 in the House and 34-1 in the Senate. Enforcement of the original law was stayed by stipulation on April 27, 2026, after xAI sued on April 9 and DOJ filed a companion complaint on April 24. One source says the AG will not enforce SB 24-205 or any successor until rulemaking is complete. Sources: [McDermott](https://www.mcdermottlaw.com/insights/colorado-ai-law-in-flux-comprehensive-replacement-bill-signed-after-federal-court-blocks-predecessors-enforcement/); [Eckert Seamans](https://www.eckertseamans.com/legal-updates/colorado-repeals-and-replaces-its-landmark-ai-statute-what-businesses-need-to-know); [TechTimes, Jul 1 2026](https://www.techtimes.com/articles/319420/20260701/colorado-ai-law-reset-discrimination-duty-dropped-disclosure-takes-its-place.htm)
- **ADA Title II web/mobile accessibility rule: IN FORCE BUT DEADLINES DELAYED ONE YEAR.** A DOJ Interim Final Rule on April 20, 2026 moved the deadlines to **April 26, 2027** for public entities serving 50,000 or more people, and to **April 26, 2028** for smaller entities and special districts. WCAG 2.1 AA is unchanged. DOJ cited resource and staffing limits, slower-than-expected technology, "including limits of generative artificial intelligence for remediation," and litigation risk. Private suits can still be brought. Sources: [Duane Morris](https://www.duanemorris.com/alerts/doj_extends_ada_title_ii_digital_accessibility_deadlines_one_year_0426.html); [Seyfarth ADA Title III blog](https://www.adatitleiii.com/2026/04/doj-extends-ada-title-ii-website-accessibility-deadlines-for-governmental-entities-but-litigation-and-compliance-risks-remain/); [UPCEA](https://upcea.edu/doj-extends-accessibility-deadline-to-april-2027-policy-matters-april-2026/). Sources disagree on the original date (April 22, 24 or 26, 2026).
- **HHS Section 504 web accessibility (recipients of HHS funds, such as hospitals and clinics):** In April 2026, Jackson Lewis said "HHS's May 2026 deadline still looms" ([Jackson Lewis](https://www.jacksonlewis.com/insights/doj-extends-public-entities-compliance-deadline-ada-related-website-accessibility-hhss-may-2026-deadline-still-looms)). A Level Access post (vendor) is titled "The ADA Title II and Section 504 Extensions," which suggests 504 was later extended too ([Level Access](https://www.levelaccess.com/blog/the-ada-title-ii-extension-what-it-doesnt-change/)). **Current 504 deadline not confirmed.**
- **FinCEN Residential Real Estate Rule: VACATED.** On March 19, 2026, the E.D. Texas vacated the rule nationwide in *Flowers Title Companies, LLC v. Bessent*. FinCEN says reporting persons need not file. As of September 2026 an appeal was pending and the vacatur stayed in effect. Sources: [Gibson Dunn](https://www.gibsondunn.com/fincen-residential-real-estate-reporting-rule-vacated-nationwide/); [Foley](https://www.foley.com/insights/publications/2026/03/federal-court-vacates-fincen-residential-real-estate-reporting-rule/); [AIDE-RE Sept 2026](https://www.aide-re.com/post/fincen-residential-real-estate-rule-update-september-2026)
- **HIPAA Security Rule overhaul: STILL PROPOSED.** The NPRM was published January 6, 2025, and comments closed March 7, 2025. More than 4,700 comments were filed, and 100+ hospital and provider groups asked for withdrawal. The Unified Agenda now targets final action in **July 2027** (not binding). Sources: [Alston & Bird, Jul 2026](https://www.alston.com/en/insights/publications/2026/07/hhs-delays-hipaa-security-rule-2027); [HIPAA Journal](https://www.hipaajournal.com/hipaa-updates-hipaa-changes/)
- **California SB 253 (GHG emissions): IN FORCE, first report due November 10, 2026** for Scope 1 and 2. CARB moved it from August 10. OAL approved CARB's amended regulations in October 2026. **SB 261 (climate risk): ENJOINED** by the Ninth Circuit pending appeal, and CARB will not enforce it while the injunction stands. Oral argument was held in January 2026, with no ruling found as of October 2026. Both are **annual** obligations. Sources: [Morgan Lewis, Oct 2026](https://www.morganlewis.com/pubs/2026/10/californias-climate-disclosure-regulations-receive-final-approval-ahead-of-november-reporting-deadline); [Crowell](https://www.crowell.com/en/insights/client-alerts/ca-sb-253-as-november-10-deadline-approaches-carb-issues-letter-to-potentially-covered-entities-plaintiffs-remind-ninth-circuit-of-pending-decision); [Simpson Thacher, Nov 2025](https://www.stblaw.com/docs/default-source/Publications/esgalert_11_19_25)
- **IEEPA tariffs: STRUCK DOWN.** On February 20, 2026, *Learning Resources v. Trump* held 6-3 that IEEPA does not authorize tariffs. The Court ordered no automatic refunds. CBP opened phase one of a refund process on April 20, 2026. Refunds run through CBP's "CAPE" process, and Phase 3 went live October 6, 2026. One practitioner says about **$11.4B** sits in finally liquidated entries that CBP will not refund without a court order naming the importer. A 10% **Section 122** global surcharge started February 24, 2026. The CIT ruled against it on May 7 for three named plaintiffs (stayed on appeal), and it **expired July 24, 2026**. The same day, new **Section 301 "forced labor" tariffs** of 10% or 12.5% took effect on imports from 60 economies. Refund-pool estimates differ: about $35.46B (principal plus interest, about 8.3M entries) in one source and about $165B in another. Sources: [ABA Procurement Lawyer, Fall 2026](https://www.americanbar.org/groups/public_contract_law/resources/procurement-lawyer/2026-fall/ieepa-tariffs-struck-down-replacement-tariffs-expired/); [Great Lakes Customs Law (sells refund services)](https://greatlakescustomslaw.com/ieepa-tariff-refunds/); [Troutman Pepper Locke](https://www.troutman.com/insights/supreme-court-strikes-down-ieepa-tariffs-trump-responds-with-section-122-global-surcharge/); [Avalara (vendor)](https://www.avalara.com/blog/en/north-america/2026/02/how-to-request-tariff-refunds.html)
- **FDA FSMA 204 Food Traceability: DELAYED to July 20, 2028.** The Continuing Appropriations Act, 2026 (November 2025) directs FDA not to enforce before then. The rule's substance is unchanged. Sources: [NC State Extension](https://foodbusiness.ces.ncsu.edu/news/fda-fsma-204-food-traceability-rule-july-20-2028/); [J.J. Keller, Jul 2026](https://jjkellercompliancenetwork.com/news/fsma-204-food-traceability-upcoming-fda-requirements-explained)
- **FTC Negative Option ("click-to-cancel") amendments: VACATED** by the Eighth Circuit on July 8, 2025. The FTC published an ANPRM on March 11, 2026 (comments due April 13, 2026). There is no proposed rule text yet. Enforcement continues under ROSCA and state auto-renewal laws (e.g., FTC v. Uber). Sources: [Mondaq](https://www.mondaq.com/unitedstates/advertising-marketing-branding/1766518/ftc-issues-call-for-comments-on-new-negative-option-rule); [NatLawReview](https://natlawreview.com/article/ftc-seeks-resuscitate-click-cancel-rule)
- **FCC TCPA one-to-one consent rule: VACATED** by the Eleventh Circuit on January 24, 2025 (*Insurance Marketing Coalition v. FCC*). The **"revoke-all" consent-revocation provision was DELAYED** to January 31, 2027 by order DA-26-12 (January 6, 2026). Sources: [ComplianceHub summary](https://compliancehub.wiki/tcpa-2026-consent-revocation-one-to-one-rule-vacated-compliance/); [JD Supra topic page](https://www.jdsupra.com/topics/consent/tcpa/fcc). Both are secondary sources; check against the FCC docket.
- **CMMC (defense contractors): Phase 1 in force; Phase 2 status DISPUTED.** Several cost and timeline pages say Phase 2, with mandatory third-party (C3PAO) Level 2 certification, starts November 10, 2026 ([cmmccost.com](https://cmmccost.com/); [IBSS (vendor)](https://ibsscorp.com/cmmc-level-2-cost-complete-2026-budget-guide-for-defense-contractors/)). A Latham & Watkins article is titled "What Defense Contractors Should Know About DOD's Suspension of CMMC Phase 2" ([Latham](https://www.lw.com/en/insights/what-defense-contractors-should-know-about-dod-suspension-of-cmmc-phase-2)). The page failed to load, so the date and scope of the suspension are **not confirmed**.
- **CCPA enforcement (2026), focused on opt-outs and the Global Privacy Control (GPC):**
  - Disney/ABC paid **$2.75M** (AG, February 11, 2026) for honoring GPC only on the signalling device.
  - PlayOn Sports paid **$1.1M** (CPPA, March 3, 2026) even though it had remediated before contact.
  - Ford paid **$375,703** (CPPA, March 5, 2026) for forcing email verification before an opt-out.
  - GM paid **$12.75M** (May 8, 2026) over connected-vehicle data.
  - One vendor blog totals **$17.1M across five settlements in 2026 through September 29** (vendor claim).
  - Per-violation maximums are $2,663 (unintentional) and $7,988 (intentional or involving minors).
  - Sources: [Koley Jessen](https://www.koleyjessen.com/insights/publications/lessons-for-businesses-from-2026s-first-california-privacy-enforcement-actions); [Buchanan Ingersoll](https://www.bipc.com/california%E2%80%99s-record-setting-enforcement-signals-heightened-privacy-oversight); [Clym (vendor)](https://www.clym.io/blog/ccpa-penalties-and-fines-what-businesses-need-to-know); [DataTrue (vendor)](https://datatrue.com/en/resources/enforcement-watch/disney-ccpa-settlement-2026/)
- **Washington pay transparency (EPOA, RCW 49.58.110): IN FORCE with heavy private litigation.**
  - Clockspot (a time-tracking vendor, not a pay-transparency vendor) reports **300+ class actions since June 2024**, mostly in King County over postings without a salary range ([Clockspot](https://www.clockspot.com/articles/pay-transparency-laws-by-state)).
  - The Association of Washington Business counts more than 250 suits, with one Seattle firm filing 75%. It says the law "undergoes key fixes" ([AWB](https://www.awb.org/was-pay-transparency-law-undergoes-key-fixes-but-challenges-remain/)).
  - Washington employment class actions overall rose from 54 (2023) to 773 (2025), with 658 more in H1 2026. Six mostly California firms filed almost 700 suits across 2025-26 ([Davis Wright Tremaine, Aug 2026](https://www.dwt.com/blogs/employment-labor-and-benefits/2026/08/washington-employment-class-action-surge)).
  - Settlements: Talkdesk **$2.79M** ([ClaimDepot](https://www.claimdepot.com/settlements/epoa-settlement-tdi)); Hermanson Co. LLP **$4.75M** ([ClaimDepot](https://www.claimdepot.com/settlements/epoa-settlement-hc-llp)).
  - The WA Supreme Court read "job applicant" broadly ([NatLawReview](https://natlawreview.com/article/washington-state-supreme-court-broadly-defines-job-applicants-covered-pay)).

**Rules NOT re-verified this session ([UNVERIFIED: training knowledge, pre-mid-2026]; re-check before use)**

- *CMS-0057-F:* prior-auth decision clocks (72 hours expedited, 7 calendar days standard) and annual public posting of PA metrics from 2026, with the first posting due March 31, 2026. The PA, Patient Access, Provider Access and Payer-to-Payer APIs are due January 1, 2027. It covers MA organizations, Medicaid/CHIP FFS and managed care, and QHP issuers on the FFEs. Verify at cms.gov (blocked here).
- *CCPA regulations on risk assessments, cybersecurity audits and ADMT:* approved September 2025 and effective January 1, 2026. ADMT compliance from January 1, 2027. Risk-assessment attestations due by April 2028. Cybersecurity audits phased 2028-2030 by revenue. These are annual or periodic, not weekly.
- *Corporate Transparency Act/BOI:* a FinCEN interim final rule (March 2025) exempted domestic companies and US persons; only foreign reporting companies must report. Effectively narrowed to near-zero recurring work for US SMBs.
- *1099-K:* the July 2025 reconciliation act ("One Big Beautiful Bill") reportedly restored the $20,000 / 200-transaction threshold. That reduces, not adds, work.
- *Texas TRAIGA:* effective January 1, 2026. Obligations fall mostly on government entities plus a narrow list of prohibited practices. Little recurring private work.
- *Illinois HB 3773 (AI in employment):* effective January 1, 2026. Notice and anti-discrimination duties, no audit mandate. Mostly one-off notices.
- *NYC Local Law 144:* bias audits are required **annually**, so it fails test (a). A late-2025 NY State Comptroller audit reportedly criticized weak enforcement.
- *PCI DSS 4.0:* future-dated requirements became mandatory March 31, 2025. These include 11.6.1, change and tamper detection on payment pages at least weekly, and 6.4.3, a script inventory. A January 2025 SAQ A revision reportedly removed these for merchants who fully outsource payment pages. That is a weekly task, but mainly for mid-size merchants hosting their own payment pages.
- *European Accessibility Act:* applied from June 28, 2025 to e-commerce and other services sold to EU consumers, including by US and UK exporters.
- *EU AI Act:* general-purpose AI obligations from August 2, 2025. High-risk obligations were due August 2, 2026, but a November 2025 "digital omnibus" proposal sought to delay them to about December 2027. **Final status unknown.**
- *OSHA heat rule:* proposed in August 2024 with hearings in mid-2025. **No final rule known**, so treat as not in force.
- *DOL rules:* the 2024 overtime rule was vacated in November 2024. In May 2025 DOL announced it would not enforce the 2024 independent-contractor rule, and it planned rescission. Neither creates new work.
- *Google/Yahoo (February 2024) and Microsoft Outlook (May 2025) bulk-sender rules:* SPF, DKIM and DMARC, one-click unsubscribe, spam rate under 0.3%. 10DLC registration has been carrier-enforced since 2023.
- *UK rules:*
  - MTD for Income Tax: from April 6, 2026 for sole traders and landlords with qualifying income over £50k, over £30k from April 2027 and over £20k from April 2028. Quarterly updates plus a final declaration, with points-based late-submission penalties.
  - ECCTA: Companies House identity verification mandatory from November 18, 2025 (existing directors verify at their next confirmation statement). The "failure to prevent fraud" offence has applied to large organizations since September 1, 2025.
  - UK B2B/B2G e-invoicing: announced for April 2029.
  - Renters' Rights Act: Royal Assent October 2025, main tenancy reforms from May 1, 2026, PRS database and ombudsman later.
  - Awaab's Law: social landlords from October 27, 2025 (damp, mould and emergency hazards), extending to more hazards in 2026 and 2027.
- *Australian rules:*
  - Payday Super: from July 1, 2026, super must reach the fund within 7 days of payday. The Small Business Superannuation Clearing House closed (closed to new users October 2025, fully by July 1, 2026).
  - AML/CTF Amendment Act 2024: existing reporting entities' new obligations from March 31, 2026. Tranche 2 sectors (lawyers, accountants, conveyancers, real estate agents, trust and company service providers, dealers in precious stones and metals) from July 1, 2026.
  - Privacy Act: statutory privacy tort from June 10, 2025. Automated-decision transparency in privacy policies from December 10, 2026.
  - Scams Prevention Framework Act: passed February 2025. Sector designation and codes for banks, telcos and digital platforms were pending.
  - Mandatory climate reporting: Group 1 from January 1, 2025, Group 2 from July 1, 2026, Group 3 from July 1, 2027. Annual.

### Inferences
- The best "rules lens" opportunities in late 2026 are not the famous AI or climate rules. Those are annual, or delayed or narrowed. The better ones are rules where (1) private plaintiffs or regulators act on each instance (each job posting, each website tag change, each import entry, each new client, each tenant report), and (2) the rule changes often, so monitoring never ends.
- Regulatory whiplash is itself a recurring-work generator. US importers faced IEEPA tariffs, then refunds, then Section 122, then Section 301 within about 9 months of 2026. That is evidence that "watch the rule and re-apply it to my transactions every week" is real paid work. Note that Lens "money leaks" may also claim tariff refunds.

### Gaps
- Could not confirm the CMMC Phase 2 suspension date or scope (the Latham page failed to load).
- Could not re-verify any UK or Australian status, or CMS-0057-F, after mid-2026. Regulator sites were blocked (gov.uk, ato.gov.au and austrac.gov.au refused by proxy; cms.gov DNS failure) and the search budget was exhausted.
- Section 504 (HHS) current web-accessibility deadline is unconfirmed.
- Whether the de minimis suspension (August 2025) survived the IEEPA ruling was not checked.

---

## Key Question 2: For each rules-driven recurring problem, who must comply, what is the recurring task, how much does it cost, what do they pay today, and who sells a fix?

### Takeaway
Eight problems are recorded. Six pass all six tests on available evidence, though one of those six (Australia's AML Tranche 2) has an unverified status, and two (CMS-0057-F and UK MTD) are borderline or fail. The strongest by pain and evidence are:
- **US import tariff/customs re-classification and refund recovery**
- **Australia AML/CTF Tranche 2 client due diligence** (status unverified)
- **Washington-led pay-transparency job-posting monitoring**
- **Accessibility remediation of public-sector documents** (ADA Title II, now deadlines in 2027/2028)

Payday Super and MTD for Income Tax mostly fail test (f) because payroll and accounting software bundles the fix.

### Cited Findings

#### P1. Tariff and customs re-application for small and mid-size US importers (classification, stacking, refunds)
- **Problem (one line):** Every import shipment must be re-checked against tariff rules that changed several times in 2026, and money is lost through overpaid duties and missed refund windows.
- **Industry:** Consumer-product brands (e-commerce), distributors, small manufacturers importing inputs.
- **Size where it hurts:** About $2M-$200M revenue. Too small for an in-house trade-compliance team; big enough to import weekly (inference).
- **Exact task:**
  - For each entry, confirm the HTS code, country of origin and which tariff layers apply (Section 301 forced-labor tariffs since July 24, 2026; any Section 232 metals).
  - Track entries eligible for IEEPA refunds through CBP's CAPE phases.
  - Watch liquidation dates so entries do not become "finally liquidated." About $11.4B already sits in finally liquidated entries that CBP says it won't refund without a court order ([Great Lakes Customs Law, which sells refund services](https://greatlakescustomslaw.com/ieepa-tariff-refunds/)).
- **Rule status:** IEEPA tariffs struck down February 20, 2026. Section 122 expired July 24, 2026. Section 301 forced-labor tariffs live from July 24, 2026 ([ABA](https://www.americanbar.org/groups/public_contract_law/resources/procurement-lawyer/2026-fall/ieepa-tariffs-struck-down-replacement-tariffs-expired/)).
- **Who feels it / who approves:** Ops or supply-chain manager and controller feel it; CFO or owner approves.
- **Frequency/hours:** Weekly or per shipment. Estimate for an importer with 20 entries per month and 300 active SKUs: a 15-minute re-check of each entry after each rule change is about 5 hours per change. Refund-eligibility review of 12 months of entries at 10 minutes each is about 40 hours one-off. Overall, about 2-6 hours per week ongoing (estimate).
- **Dollar evidence:** Refund pool estimates range from **about $35.46B to about $165B** (sources disagree; see KQ1).
- **Handled today:** Licensed customs brokers and forwarders (Flexport, C.H. Robinson), trade lawyers, and classification software (Avalara, a vendor, publishes refund guides). **Prices not verified this session.**
- **Competition:** Moderately crowded. Brokers, forwarders, tax-tech vendors and law firms all offer refund services.
- **AI trend:** Grows. Rule churn plus document-heavy entry data suit AI. A licensed broker must still sign, which is the "human checker."
- **Buyer reach:** Customs broker partnerships (NCBFAA), Shopify/Amazon seller communities, NASBITE, trade-finance newsletters (inference; not verified).
- **Companies affected:** Not found this session.
- **Shariah flag:** CBP refunds include interest ("principal plus interest" per search results). That is a possible issue for the client.
- **Against:** Policy may stabilize, and refunds are a one-time windfall. Brokers own the client relationship and legal liability. Big forwarders already market free refund help.

#### P2. Pay-transparency job-posting monitoring for multi-state employers
- **Problem:** Job ads posted or re-posted anywhere without a compliant pay range trigger class actions, especially in Washington.
- **Industry:** Staffing agencies, healthcare systems, retail and hospitality chains, tech, trades and construction. Construction example: Hermanson Co. LLP, $4.75M settlement ([ClaimDepot](https://www.claimdepot.com/settlements/epoa-settlement-hc-llp)).
- **Size where it hurts:** About 50-5,000 employees hiring across several states.
- **Exact task:**
  - Weekly crawl of all live postings: own careers site, Indeed, LinkedIn, aggregators and agency re-posts.
  - Check each against each jurisdiction's rule (range, benefits description, remote roles that "could be filled" in WA).
  - Fix within any cure window and log evidence.
- **Rule status:** WA EPOA in force, with 300+ suits since June 2024 ([Clockspot](https://www.clockspot.com/articles/pay-transparency-laws-by-state)) and "key fixes" enacted ([AWB](https://www.awb.org/was-pay-transparency-law-undergoes-key-fixes-but-challenges-remain/)). The 2025-26 laws in IL, MN, NJ, VT, MA and Cleveland are [UNVERIFIED: training knowledge].
- **Who feels it / approves:** Talent-acquisition lead and HR director feel it; CHRO, COO or owner approves.
- **Frequency/hours:** Weekly. Estimate: 40 open roles × 5 boards = 200 live postings × 2 minutes = about 6.7 hours per week.
- **Dollar evidence:** Settlements of $2.79M (Talkdesk) and $4.75M (Hermanson). Statutory damages of $100-$5,000 per applicant are [UNVERIFIED: training knowledge].
- **Handled today:** ATS pay-range fields (Greenhouse, Workday, etc.), employment counsel, recruiters. Pay-equity platforms (Syndio, Payscale, Trusaic) mostly do analysis, not posting surveillance (inference; pricing not verified).
- **Competition:** Low to moderate for monitoring of third-party re-posts (inference).
- **AI trend:** Grows as more states add laws. AI makes crawling and checking cheap, so ATS vendors could bundle it.
- **Buyer reach:** SHRM state chapters, staffing associations (ASA), ATS marketplaces.
- **Companies affected:** Not found.
- **Against:** WA's 2025 fixes (cure period) may cut new suits. Exposure is concentrated in one state. It could look like a one-time template fix.

#### P3. Privacy opt-out and tracker monitoring for consumer websites and apps (CCPA plus about 20 state laws)
- **Problem:** Marketing adds tags weekly, and GPC or opt-out flows silently break, drawing fines.
- **Industry:** E-commerce, media, auto, education/ed-tech, sports streaming.
- **Size where it hurts:** About $25M+ revenue (the CCPA threshold) up to mid-enterprise.
- **Exact task:**
  - Weekly scan of every page and app release for new pixels.
  - Test that GPC and "Do Not Sell" are honored across devices and logged-in accounts. Disney paid $2.75M for honoring GPC only per device ([Koley Jessen](https://www.koleyjessen.com/insights/publications/lessons-for-businesses-from-2026s-first-california-privacy-enforcement-actions)).
  - Remove friction from opt-outs. Ford paid $375,703 for requiring email verification.
  - Keep evidence.
- **Who feels it / approves:** Privacy counsel and marketing ops feel it; GC or CMO approves.
- **Dollar evidence:** $17.1M in 2026 CCPA settlements through September (vendor claim, [Clym](https://www.clym.io/blog/ccpa-penalties-and-fines-what-businesses-need-to-know)). PlayOn was fined $1.1M despite self-remediation.
- **Handled today:** Consent platforms (OneTrust, Osano, Usercentrics, Cookiebot) and tag auditors (ObservePoint, DataTrue, a vendor). **Prices not verified.** Basic consent-banner tools for small sites are commonly under $100 per month [UNVERIFIED].
- **Competition:** Crowded.
- **AI trend:** Grows in volume. AI browsing agents make scripted opt-out testing cheaper, which is good for a lean entrant but also for incumbents.
- **Buyer reach:** IAPP, privacy newsletters, Shopify Plus agencies.
- **Shariah flag:** Some buyers will be ad-tech, gambling or media sites; screen clients.
- **Against:** Crowded with funded CMP vendors, and enforcement hits large brands more than SMBs.

#### P4. CMMC / NIST SP 800-171 continuous evidence for small defense suppliers
- **Problem:** Small machine shops and engineering subcontractors must keep 110 security controls working and documented, or lose DoD work.
- **Industry:** Defense manufacturing and subcontracting.
- **Size:** 10-500 employees. The SBA says **>120,000 small businesses** would need compliance, with only about 100 approved assessors (per search results citing SBA comments).
- **Exact task (recurring part):** Weekly audit-log review, vulnerability-scan follow-up, access reviews, POA&M updates, SSP upkeep and evidence collection, plus annual affirmations.
- **Rule status:** Phase 1 in force. Phase 2 (C3PAO, November 10, 2026) is reported **suspended** in a Latham title, details unconfirmed.
- **Cost evidence:**
  - DoD estimate for a small entity's Level 2 C3PAO cycle: **$101,752 initial / $104,670 over three years**, with C3PAO engagement $31,234 ([Defense Compliance Report](https://thedefensecompliancereport.com/cmmc-certification-cost/)).
  - SBA estimate: **$593,800** per C3PAO certification.
  - Market: $75k-$150k for SMB Level 2 total, assessment fees $30k-$70k (vendor claims, [IBSS](https://ibsscorp.com/cmmc-level-2-cost-complete-2026-budget-guide-for-defense-contractors/); [Elevate](https://elevateconsult.com/insights/cmmc-certification-cost-breakdown-hidden-level-2-expenses-defense-contractors-miss-in-2026/)).
- **Who feels it / approves:** IT manager or outsourced MSP feels it; president or owner approves.
- **Handled today:** MSPs/MSSPs, Registered Provider Organizations, GCC High enclaves, GRC tools.
- **Competition:** Moderate. The MSP channel dominates.
- **AI trend:** Grows. Evidence and narrative drafting are a good AI fit.
- **Against:** If Phase 2 is truly suspended, urgency falls. Much of the work is infrastructure, not paperwork.

#### P5. Accessibility remediation of public-sector digital content (ADA Title II, possibly HHS 504)
- **Problem:** Cities, counties, school districts, transit agencies and public universities publish new PDFs, agendas, forms and videos every week that must meet WCAG 2.1 AA.
- **Size:** Entities serving 50k+ people by April 26, 2027; smaller ones by April 26, 2028 ([Duane Morris](https://www.duanemorris.com/alerts/doj_extends_ada_title_ii_digital_accessibility_deadlines_one_year_0426.html)).
- **Exact task:** Tag and repair each new document, write alt text, caption media, and check third-party portals. Humans verify with assistive technology.
- **Frequency:** Weekly (council packets, minutes, notices).
- **Hours/cost:** Not found this session. Per-page remediation pricing was not verified.
- **Who feels it / approves:** City clerk, communications or web manager, university accessibility office; CIO, city manager or provost approves.
- **Evidence of an AI gap:** DOJ itself cited "limits of generative artificial intelligence for remediation" as a reason to delay ([Duane Morris](https://www.duanemorris.com/alerts/doj_extends_ada_title_ii_digital_accessibility_deadlines_one_year_0426.html)).
- **Handled today:** Manual staff work, remediation vendors (Level Access, AudioEye, accessiBe; vendor pages), Acrobat Pro auto-tag (cheap, partial).
- **Competition:** Moderate. Overlays are discredited, and quality remediation is scarce (inference).
- **Companies affected:** About 90,000 US local governments [UNVERIFIED: Census of Governments, training knowledge].
- **Against:** Slow public procurement, the deadline was pushed out a year (and might be pushed again), and budgets are small.

#### P6. Prior-authorization clocks and metrics under CMS-0057-F (health plans)
- **Status:** [UNVERIFIED: decision clocks from January 2026, APIs January 2027].
- **Task:** Every prior-auth request must be decided within 72 hours or 7 days, and denial reasons must be written.
- **Buyers:** Regional MA and Medicaid plans.
- **Competition:** Crowded (UM vendors, clearinghouses). Buyers are large.
- **Shariah flag:** Conventional insurance.

#### P7. UK Awaab's Law hazard-response workflow (social landlords)
- **Status:** [UNVERIFIED: in force from October 27, 2025 for damp, mould and emergency hazards].
- **Task:** Triage every tenant report daily. Investigate and issue written summaries within fixed working-day clocks (emergency within 24 hours). Keep evidence for the Housing Ombudsman.
- **Who feels it / approves:** Head of repairs feels it; property director approves.
- **Handled today:** Housing-management systems (NEC, MRI, Civica, Aareon) and damp sensors.
- **Against:** Physical inspection dominates the work, and incumbents can add modules.

#### P8. Australia AML/CTF Tranche 2 client due diligence
- **Status:** [UNVERIFIED: obligations from July 1, 2026 for real estate agents, conveyancers, lawyers, accountants, TCSPs and precious-goods dealers].
- **Task:**
  - Customer due diligence for every new client.
  - Beneficial-owner tracing for entities and trusts, plus source-of-funds review.
  - Ongoing monitoring and suspicious-matter reports.
- **Frequency:** Weekly. Estimate: an agency taking 10 listings a week × 30-45 minutes of CDD = 5-7.5 hours per week.
- **Who feels it / approves:** Principal or practice partner (feels it and approves).
- **Handled today:** ID-check tools (InfoTrack, First AML, etc.; prices unverified) and compliance consultants.
- **Against:** AUSTRAC is likely lenient early on, small firms may use cheap templates, and practice-software vendors could bundle CDD.

#### Failed / weak (recorded for completeness)
- **UK MTD for Income Tax** [UNVERIFIED status]: quarterly work is real for accountancy practices. HMRC lists free or cheap recognized software, and bookkeeping AI (Dext, Hubdoc) already exists, so it **fails (f)**.
- **AU Payday Super** [UNVERIFIED]: every pay run is affected, but payroll software (Xero, MYOB, Employment Hero) bundles super payment, so it **fails (f)**. Shariah flag: super funds hold interest-bearing assets.

### Inferences

**Six-test results** (a = at least weekly, b = measurable money, c = already paid for, d = buyer can approve, e = AI plus human checker, f = not solved under $100/month):

| Problem | a | b | c | d | e | f | Score | Reason |
|---|---|---|---|---|---|---|---|---|
| P1 Tariffs | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **7** | Brokers charge per entry but don't proactively re-check |
| P2 Pay transparency | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **6** | ATS fields don't watch third-party re-posts |
| P3 Privacy monitoring | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ for mid-size, ✗ for small sites | **5** | Crowded |
| P4 CMMC | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **5** | Phase 2 uncertainty |
| P5 Accessibility | ✓ | ✓ (litigation, federal funds) | ✓ | ~ (procurement) | ✓ | ✓ | **6** | Acrobat auto-tag is only partial |
| P6 Prior auth | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ | **4** | Crowded, large buyers |
| P7 Awaab's Law | ✓ | ✓ | ✓ | ✓ | partial | ✓ | **6** | Physical inspection limits AI share |
| P8 AU AML Tranche 2 | ✓ | ✓ | ✓ | ✓ | ✓ | ✓ for full CDD (ID checks alone are cheap) | **7** | Conditional on status |

### Gaps
- No verified vendor pricing for remediation, CDD tools, privacy monitors, or broker per-entry fees (pricing pages unreachable).
- No verified US/UK/AU counts of affected firms except SBA's 120,000 CMMC figure.
- Hours-per-week figures are estimates, not survey data.

---

## Key Question 3: Which rules hit small and mid-size firms that cannot afford a compliance team or enterprise GRC software?

### Takeaway
SMB-heavy exposure is greatest in:
- **Pay transparency** (any employer posting in WA)
- **Tariffs** (small importers)
- **CMMC** (120,000+ small defense suppliers)
- **AU Tranche 2** (small real-estate, law and accounting firms)
- **ADA Title II** for small towns and special districts (deadline April 2028)

Climate (SB 253: over $1B revenue [UNVERIFIED threshold]), UK failure-to-prevent-fraud (large organizations only) and CCPA cybersecurity audits are large-company or annual work.

### Cited Findings
- The SBA says CMMC would require more than 120,000 small businesses to seek compliance through a system with about 100 assessors, at $593,800 per certification (SBA estimate as reported in [Defense Compliance Report](https://thedefensecompliancereport.com/cmmc-certification-cost/) / [IBSS](https://ibsscorp.com/cmmc-level-2-cost-complete-2026-budget-guide-for-defense-contractors/)).
- Washington suits hit mid-size firms such as a mechanical contractor (Hermanson, $4.75M) and a contact-center software firm (Talkdesk, $2.79M) ([ClaimDepot](https://www.claimdepot.com/settlements/epoa-settlement-tdi)).
- DOJ gave smaller public entities and special districts until April 26, 2028 ([Duane Morris](https://www.duanemorris.com/alerts/doj_extends_ada_title_ii_digital_accessibility_deadlines_one_year_0426.html)).

### Inferences
- SMB buyers in these groups use MSPs, brokers, bookkeepers or outside counsel rather than Vanta, Drata or OneTrust. A "service plus AI" offer sold through those intermediaries is the likely channel.

### Gaps
- NFIB, US Chamber, FSB and ASBFEO burden surveys could not be retrieved (search budget exhausted).
