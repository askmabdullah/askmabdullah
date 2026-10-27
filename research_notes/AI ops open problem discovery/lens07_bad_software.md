# Lens 07: Bad Software (legacy and hated vertical systems that force weekly manual workarounds)

*Limits of this research (read first): this pass ended early. Capterra, G2, TrustRadius, Software Advice, GetApp and Trustpilot could not be opened directly (the fetch tool returned DNS failures, "ENOTFOUND"), and Reddit was blocked outright. After 9 successful web searches, the web-search budget shared by every research agent (200 per turn) ran out. The fetch tool then failed DNS on every host, including vendor sites, Business Wire and vendor community forums, and a curl fallback was denied. So every review quote below comes from search-engine snippets of review pages. The snippets show no review dates, and they cannot be pinned to one exact review. Many per-problem fields (hours, prices, company counts) are still gaps. A follow-up pass should verify them, starting with the Gaps lists. Figures labelled "estimate" show their math. Figures from companies that sell a fix are labelled "vendor claim".*

## Q1. Which vertical systems draw consistent complaints, what do users beg for, and is the vendor closing the gap?

### Takeaway
The best-evidenced workaround pains in this pass are: dental insurance verification keyed into Dentrix/Eaglesoft-era systems; weekly report extraction and cleanup from Yardi Voyager; freight-broker email-to-TMS keying; home health referral intake from fax; and agency commission reconciliation. The surprise is that the main vendors (Applied Systems, WellSky, McLeod) shipped AI features in 2025-2026 that target exactly these workarounds. That shrinks the window for an outside service inside those ecosystems and moves the openings to long-tail or on-premise systems and to cross-system work.

### Cited Findings

**Property management (Yardi Voyager)**
- Reviewers complain that Yardi is "fairly inflexible in allowing direct access to your data so that you can get a raw data dump to pivot in another application". Snippet from Yardi Voyager review pages; date and exact review not visible in the snippet. — [Capterra Yardi Voyager reviews](https://www.capterra.com/p/33832/Yardi-Voyager/reviews/); [Software Advice Yardi Voyager reviews](https://www.softwareadvice.com/property/yardi-voyager-profile/reviews/); [TrustRadius Yardi Voyager reviews](https://www.trustradius.com/products/yardi-voyager/reviews/all)
- Reviewers cite "limitations in customisation, particularly around reporting and dashboard configuration". They also say report names don't match report types and filters are not specific enough. — same review pages as above (snippet, undated)
- Performance: "some of the reports take a very long time to pull the information" — same review pages (snippet, undated)
- Excel exports: a review says it "merges columns in an attempt to maintain the aesthetic which results in data that can't easily be sorted". This appeared on a Rent Manager vs Yardi comparison page, so it is ambiguous which product the review refers to. — [Software Advice Rent Manager vs Yardi Voyager](https://www.softwareadvice.com/property/rent-manager-profile/vs/yardi-voyager/)
- Counterpoint (positive): "Reports are easy to find and I love being able to pull them as Excel spreadsheets" — [Capterra Yardi Voyager reviews](https://www.capterra.com/p/33832/Yardi-Voyager/reviews/) (snippet, undated)

**Dental practice management (Dentrix; Eaglesoft not yet covered)**
- Dentrix reviewers say it is "difficult to create insurance fee schedules", that the "insurance component is outdated and difficult to maintain", and that they are "limited to the Payor ID insurance database", which is not kept up to date. — [Software Advice Dentrix reviews](https://www.softwareadvice.com/dental/dentrix-profile/reviews/); [G2 Dentrix reviews](https://www.g2.com/products/dentrix/reviews); [TrustRadius Dentrix reviews](https://www.trustradius.com/products/dentrix/reviews/all) (snippets, undated; some may be pre-2025 and about Dentrix Core or Enterprise rather than Ascend)
- Slowness and age: "reports take a long time to run"; "system is much too slow" when generating reports; "outdated visually"; "isn't cloud based"; support holds "no less than 20 minutes". — same Dentrix review pages (snippets, undated)
- Handling time per verification, CAQH Index 2024: about 12 minutes for a manual dental eligibility check, 7 for a portal or other partly electronic check, and 4 for a fully electronic check. There were 1.2 billion dental eligibility and benefit verifications in 2023. — cited secondhand by [Stealth Agents research page](https://stealthagents.com/research/dental-insurance-verification-workload-statistics-2026). Stealth Agents sells outsourced staff, so this is a vendor page, though the figures are attributed to CAQH. Verify against the primary CAQH Index.
- Weekly math: 150 checks a week is 30 direct staff hours at the manual benchmark, versus 10 hours fully electronic, before exceptions and patient calls. — [Stealth Agents staffing statistics](https://stealthagents.com/research/dental-insurance-verification-staffing-statistics-2026) (vendor page; the math checks out: 150 × 12 min = 30 h)
- Practice owners estimate the front desk spends 30-40% of its week on insurance verification, claim follow-up, denial appeals and payment posting. These are bundled tasks, an owner estimate rather than a study, and a vendor claim. — [DentalBase blog](https://www.dentalbase.ai/blogs/dental-insurance-for-dental-practices)
- DSOs hire dedicated "Insurance Verification Specialist" staff, which shows someone already pays for this work. — [MB2 Dental job posting](https://dentalcareers-mb2dental.icims.com/jobs/21339/insurance-verification-specialist/job); [MB2 Dental job posting 2](https://jobs-mb2dental.icims.com/jobs/23276/insurance-verification-specialist/job); [DentalPost insurance front office job, San Antonio](https://www.dentalpost.net/dental-jobs/job-post/551266/insurance-dental-front-office-job-in-san-antonio-tx)

**Insurance agency management (Applied Epic)**
- Applied's own marketing calls carrier commission and payables reconciliation a long-standing manual, time-consuming task. It says statements arrive as PDFs, spreadsheets, CSVs and paper (vendor framing). Its AI product "Applied Recon" extracts and matches statement lines, using signals such as policy number and term dates, and posts reconciled or suspended statements to the Epic general ledger. — [Applied Recon product page](https://int.appliedsystems.com/en-us/solutions/for-agents/financial-management/applied-recon/)
- Applied Recon covers direct-bill commission statements now. Agency-bill payables are listed as "new in July 2026". — [Applied Recon brochure (PDF)](https://www1.appliedsystems.com/siteassets/all-documents/resources/brochures-data-sheets/applied-recon-product-brochure_en-us.pdf)
- Epic's own help says the reconciliation method varies by carrier. Direct-bill commissions can be imported from a spreadsheet, or downloaded only where the carrier supports it. — [Applied Epic 2023.2 help](https://help.appliedsystems.com/Help/Epic/2023.2en-US/General_Ledger/Reconciliations/Recs_Add_Direct_Bill_Rec.htm)
- A consultant describes the manual steps: enter carrier commission deposits as receipts in the general ledger, finalize them, then match them to reconciliation entries. — [Kite Tech Group](https://www.kitetechgroup.com/?p=13813)

**Trucking and freight brokerage TMS (McLeod)**
- A 2026 guide describes AI inbox agents that sort each broker email as a capacity offer, quote request, check call, rate confirmation or noise. The agents then extract the structured fields "a human used to retype". Vendor-reported no-touch automation rates run "from 70 to 94 percent depending on a broker's data discipline, its choice of TMS and how cleanly its operations run" (vendor claims relayed by the guide). — [GetTransport blog, 2026](https://blog.gettransport.com/trends-in-logistic/ai-agents-freight-brokers-2026-quote-automation/)
- McLeod's own (non-AI, roughly 2016) eRate Confirmation sends carriers a web link. The carrier's submitted data flows into PowerBroker. — [McLeod Software](https://www.mcleodsoftware.com/?p=7119)
- McLeod's version 25.2 (December 2025) is billed as "a completely re-engineered user interface and workflows for trucking operations". Trade-press headlines promise "faster invoicing and AI-powered operations". — [Truckinginfo / HDT](https://truckinginfo.com/news/mcleods-new-tms-release-promises-smarter-planning-faster-invoicing-and-ai-powered-operations-for-trucking-companies-and-freight-brokers); [TT News](https://www.ttnews.com/articles/mcleod-unveils-automated-tools-logistics-firms-brokers); [FleetOwner](https://fleetowner.com/technology/article/21693262/mcleod-unveils-new-solutions-for-logistics-companies)

**Home health and hospice EMR (WellSky)**
- WellSky's January 2026 release adds AI to Enterprise Referral Manager. Each inbound referral is scored for completeness against intake requirements, then accepted, declined or routed for review "with human oversight". AI extraction also summarizes items such as anticipated services. — [Business Wire, 27 Jan 2026](https://www.businesswire.com/news/home/20260127232204/en/WellSky-Launches-New-AI-Capabilities-to-Automate-and-Scale-Referral-Intake)
- WellSky's May 2025 release pulls referrals from CarePort, eFax and Direct secure messaging into one dashboard. — [Business Wire, May 2025](https://www.businesswire.com/news/home/20250508205101/en)
- CarePort Referral Intake uses "WellSky Summarize" (SkySense AI) to read referral packets, including referrals sent by eFax. — [HomeCare Magazine](https://www.homecaremag.com/news/wellsky-launches-ai-powered-careport-referral-intake-solution); [HME News](https://www.hmenews.com/article/wellsky-launches-next-generation-intake-solution-enhanced-with-ai); [Business Wire, 24 Sep 2025](https://www.businesswire.com/news/home/20250924208380/en)

**Construction accounting (Sage 300 CRE)**
- In a Sage Community thread, Sage's Senior Product Manager for Construction said there are "absolutely no plans to 'end of life' Sage 300 CRE" and later reconfirmed it. The thread says a salesperson had told customers end of life was a few years away and that they should move to Sage Intacct quickly. A partner (Anterra) quotes a Sage director at CFMA National in May 2025: the product "isn't going away for years and years and years. And anyone telling you it is, is lying." — [Sage Community Hub thread](https://communityhub.sage.com/us/sage_construction_and_real_estate/f/sage-300-construction-and-real-estate/246072/end-of-life-for-sage300cre)
- Users are weighing a move from Sage 300 CRE to Sage Intacct and ask what functionality would be lost. — [Sage Community Hub thread](https://communityhub.sage.com/us/sage_construction_and_real_estate/f/sage-300-construction-and-real-estate/262861/migrating-from-sage-300-cre-to-intacct)

**Mid-market ERP end-of-life (Microsoft Dynamics GP)**
- Microsoft (announced September 2024): GP product enhancements, regulatory (tax) updates and technical support end on 31 December 2029. Security updates continue until 30 April 2031. Microsoft points customers to Dynamics 365 Business Central. — [Microsoft Dynamics 365 blog](https://www.microsoft.com/en-us/dynamics-365/blog/?p=194353); [Stoneridge Software](https://stoneridgesoftware.com/how-to-plan-for-dynamics-gp-end-of-support-what-you-need-to-know/); [Forvis Mazars, Oct 2024](https://www.forvismazars.us/forsights/2024/10/microsoft-dynamics-gp-end-of-support-announcement)
- The final US and Canadian payroll update comes at the end of 2029, and the 2029 date was changed from Microsoft's original timeline. — [Stoneridge Software](https://stoneridgesoftware.com/how-to-plan-for-dynamics-gp-end-of-support-what-you-need-to-know/)

**Nonprofit CRM (Blackbaud Raiser's Edge NXT)**
- Blackbaud Community answer: gifts can be imported into Raiser's Edge from a spreadsheet, but not into a batch, which is a separate function. — [Blackbaud Community, batch gift entry](https://community.blackbaud.com/discussion/comment/224574/); [Blackbaud Community, importing donor payments](https://community.blackbaud.com/discussion/comment/228746)
- An ImportOmatic reviewer complains about poor phone-number matching, and says ZIP weighting ("a +4 on a ZIP code will significantly impact the similarity score") forces extra manual record review. — [GetApp UK ImportOmatic](https://www.getapp.co.uk/software/111547/importomatic) (snippet, undated)

### Inferences
- The pattern across Applied (Recon), WellSky (AI referral intake) and McLeod (25.2) is that dominant vendors are productizing the exact manual workaround. An outside "AI plus human checker" service is most defensible where the system is (a) on-premise or old (Sage 300 CRE, Dynamics GP, Dentrix desktop), (b) a smaller vendor without AI budget (HawkSoft, AMS360-tier, HCHB/Axxess, unverified), or (c) the work spans several systems, which no single vendor's AI covers.
- Yardi complaints focus on getting data out (raw data access, slow reports, messy exports). That points to a reporting or data-extraction layer as the user's ask, more than to new transactional features.
- Sage's insistence that 300 CRE is not end-of-life means on-premise construction shops will stay on it for years. That gives a long runway for workaround services (inference; no complaint data on specific tasks was collected).

### Gaps
- No dated 1-3 star review quotes from 2025-2026. Review sites were unreachable and snippets carried no dates. Not covered at all this session: AppFolio, Entrata, RealPage, Buildium, Rent Manager, Eaglesoft, Open Dental, Cornerstone, AVImark, ezyVet, AMS360, HawkSoft, EZLynx, TMW/Trimble, Aljex, Tailwind, Viewpoint Vista, Foundation, Procore integrations, Homecare Homebase, Axxess, behavioral health EHRs, CDK, Reynolds and Reynolds, Dealertrack, Vantaca, CINC, TOPS, funeral home software, Epicor, JobBOSS, Sage 100, SAP Business One, small-firm legal, school and local government systems.
- Vendor AI add-on details not verified this session: Yardi Virtuoso, AppFolio Realm-X, Entrata ELI, HawkSoft and AMS360 AI features, McLeod 25.2 AI specifics.
- No hours-per-week evidence found for property management reporting, freight email keying, home health intake, construction AP or agency commission reconciliation.

## Q2. Do vendors block integrations (closed APIs, partner fees, lawsuits)?

### Takeaway
Yardi gates third-party access tightly: annual per-interface license fees (reported at about $25k a year per interface by a third party), plus eligibility rules (a two-year-old company with three active Voyager clients) and a separate data agreement per interface type. Outsiders are therefore pushed toward working through the user's own login (browser agents, report exports) rather than official APIs. Evidence for the other vendors was not gathered.

### Cited Findings
- Yardi's partner pages say the Standard Interface Partnership charges an annual license fee per interface. The amount varies by interface type and sometimes by transaction. A company must be two years old and have at least three active Voyager clients to qualify, and each interface type needs its own Data Exchange Agreement. — [Yardi: Become an Interface Partner](https://www.yardi.com/?p=359162); [Yardi: Become an Interface Partner (alt)](https://yardi.com/?p=2754)
- Third-party estimate: about $25,000 per agreement or interface per year. This comes from a company that sells unofficial API access to legacy systems, so it is a vendor claim and not a published Yardi rate. — [Supergood API Report Card: Yardi Systems](https://supergood.ai/api-report-card/yardi-systems); [Supergood: Yardi Voyager](https://supergood.ai/api-report-card/yardi-voyager)
- RentCafe API terms set fees by reference to "the Agreement", with no public amounts. — [Yardi RentCafe API Terms of Use](https://resources.yardi.com/?p=18614)
- An integration-platform vendor has published a guide to "overcoming legacy API constraints" with Yardi and RealPage (content not retrieved). — [Truto blog](https://truto.one/blog/overcoming-legacy-api-constraints-when-integrating-with-yardi-and-realpage/)
- McLeod has a partner ecosystem. Parade says its McLeod PowerBroker integration syncs load data, carrier assignments and rate confirmations both ways (vendor claim). — [Parade McLeod integration](https://www.parade.ai/integrations/mcleod)
- Applied Epic supports carrier commission downloads only "where the carrier supports it". Otherwise it is a spreadsheet import. — [Applied Epic help](https://help.appliedsystems.com/Help/Epic/2023.2en-US/General_Ledger/Reconciliations/Recs_Add_Direct_Bill_Rec.htm)

### Inferences
- With fees around $25k a year per interface (if accurate) and a three-client minimum, a small new service cannot get official Yardi API access at first. Early delivery would have to run on the client's own credentials and exports, which needs a check of each client's Yardi license terms on automated access (inference).
- Any service that automates payer portals (dental) or carrier portals (insurance) faces each portal's terms of service and bot defenses. This is a delivery risk for browser-agent approaches (inference; no source collected).

### Gaps
- Not verified this session: auto DMS data-access disputes (CDK, Reynolds and Reynolds, Authenticom history), any Yardi vs Entrata or RealPage data-access litigation, partner terms for Henry Schein Dentrix and Patterson Eaglesoft, the Open Dental API price, Applied Epic SDK fees, Vertafore API terms, Blackbaud SKY API limits, WellSky, HCHB and Axxess partner terms.

## Q3. Who sells add-ons or services that fix these gaps today, and at what price?

### Takeaway
Where prices were found, the cheapest fix is in nonprofit gift import: ImportOmatic lists from $100 a year and Importacular has a free tier. That fails test (f). Everywhere else the sellers are the main vertical vendor's own AI add-on (Applied Recon, WellSky referral AI, McLeod 25.2) or VC-funded AI startups (freight). No prices were found for any of them.

### Cited Findings
- ImportOmatic (Omatic): a plug-in for Raiser's Edge and RE NXT that transforms outside data (MailChimp, Classy, DonorDrive, Luminate Online, Artez) before import. Software Advice lists a starting price of $100 a year; when that price was set is unconfirmed. — [Software Advice: Omatic / ImportOmatic](https://www.softwareadvice.com/data-quality/importomatic-profile/)
- Importacular's free version is suggested by Blackbaud Community users as a way to import constituents and gifts. — [Blackbaud Community](https://community.blackbaud.com/discussion/comment/228746)
- Applied Recon is Applied Systems' own AI reconciliation product for Epic. No price found. — [Applied Recon](https://int.appliedsystems.com/en-us/solutions/for-agents/financial-management/applied-recon/)
- WellSky sells AI referral intake inside its own platform. No price found. — [Business Wire, Jan 2026](https://www.businesswire.com/news/home/20260127232204/en/WellSky-Launches-New-AI-Capabilities-to-Automate-and-Scale-Referral-Intake)
- Freight AI vendors with McLeod links: Parade (carrier sales, rate cons) and Augment ("Augie"). The search summary reported an August 2026 Augment–McLeod integration for carrier selection and track and trace, with CRST as an early live customer. The exact source article was not pinned (it appeared among the TT News, FleetOwner and Truckinginfo results). Numeo also positions itself against McLeod for growing carriers. — [Parade](https://www.parade.ai/integrations/mcleod); [Numeo vs McLeod](https://www.numeo.ai/post/numeo-vs-mcleod-tms-enterprise-power-vs-ai-automation-for-growing-carriers)
- Dental verification is handled today by in-house staff and outsourced virtual assistants. Stealth Agents publishes research to sell staffing (vendor). — [Stealth Agents](https://stealthagents.com/research/dental-insurance-verification-staffing-statistics-2026); [MB2 Dental job](https://dentalcareers-mb2dental.icims.com/jobs/21339/insurance-verification-specialist/job)

### Inferences
- Freight broker inbox automation looks crowded: several funded vendors, plus McLeod's own roadmap.
- Dental verification is probably crowded too, but no tool prices were verified this session, so test (f) is open.

### Gaps
- No prices found for: Applied Recon, WellSky AI intake, Parade, Augment, Yardi Virtuoso, AppFolio Realm-X, dental verification tools, construction AP automation tools, or ERP order-entry automation (Conexiom-type tools).
- Outsourced and BPO prices per verification, per referral or per invoice: not found.

## Q4. Problem records and preliminary six-test screen

Tests: (a) at least weekly; (b) measurable cost; (c) someone already pays; (d) the person who feels it can approve spend; (e) AI plus a human checker can do most of it in 2026; (f) not already solved by a tool under $100/month or bundled free by a big platform or the main vertical vendor.

### Takeaway
There are 8 candidate problems across 8 industries. On current evidence the strongest are dental verification and property-management reporting extraction. The weakest is nonprofit gift import, which fails (f). Several problems are "provisional" because hours and price evidence is missing.

### Cited Findings (per problem; all sourced items repeat URLs above)

**P1. Dental insurance verification keyed into the practice system**
- Problem: front desks re-check each patient's insurance on payer portals or by phone, then type the benefits into Dentrix or Eaglesoft.
- Industry: dental (Dentrix, Eaglesoft). Hurts most: 1-20 location groups and DSOs.
- Exact task: for tomorrow's schedule, log into payer portals or call; record eligibility, frequencies and coverage percentages; type them into the practice system; flag gaps.
- Who feels it: front-desk or insurance coordinator. Who approves: owner dentist, or the DSO's head of revenue cycle (inference).
- Frequency and hours: daily. 150 checks/week = 30 hours manual vs 10 hours fully electronic ([Stealth Agents, citing CAQH 2024](https://stealthagents.com/research/dental-insurance-verification-staffing-statistics-2026)).
- Dollar cost estimate: 30 h/week × $20-25/h assumed wage = $600-750/week, or $31k-39k/year per practice doing 150 checks a week. The wage is an assumption, not sourced.
- Today: in-house staff and dedicated specialists ([MB2 job](https://dentalcareers-mb2dental.icims.com/jobs/21339/insurance-verification-specialist/job)), plus outsourced virtual assistants (vendor).
- Who sells a fix: not verified this session.
- 24-month outlook: it shrinks as payers move to fully electronic checks, the 12 to 4 minute gap in the CAQH figures (inference). But the benefit-breakdown detail and entry into old practice systems persist.
- Reach buyers (not verified): dental state societies, DSO conferences, Dentrix and Eaglesoft user groups.
- Count of US practices: not found.
- Strongest argument against: crowded tool market plus electronic payer checks; payer-portal terms block bots.
- Screen: a ✓, b ✓, c ✓, d ✓, e ✓ (portal ToS risk), f unverified. Result: 5/6 provisional.
- Shariah flag: the revenue process depends on conventional insurance claims, a possible issue.

**P2. Weekly property reports rebuilt by hand from Yardi**
- Problem: staff export Yardi Voyager reports every week and rebuild them in Excel for owners and asset managers.
- Industry: multifamily and commercial property management (Yardi Voyager, plus RealPage and Entrata in mixed portfolios). Hurts most: mid-size operators and fee managers.
- Task: run occupancy, leasing and delinquency reports; fix exports with merged columns; combine across properties or systems; send the pack.
- Who feels it: an asset or reporting analyst. Who approves: VP asset management, COO or CFO (inference).
- Evidence: complaints about raw-data access, slow reports, limited report customization and messy exports (review pages above). Official API access is gated (Yardi partner terms; about $25k a year per interface, vendor claim).
- Hours and dollars: not found.
- Who sells a fix: Yardi, AppFolio and Entrata AI add-ons (unverified); Supergood-style unofficial APIs (vendor).
- 24-month outlook: vendor AI reporting will close part of the gap. Cross-system portfolios keep the problem alive (inference).
- Reach buyers (not verified): NAA and NMHC events, IREM, Yardi user conferences.
- Strongest argument against: Yardi controls access and is building its own AI.
- Screen: a ✓, b unverified, c ✓, d ✓, e ✓, f unverified. Result: 4/6 provisional.

**P3. Freight broker email-to-TMS keying**
- Problem: brokers retype quotes, rate confirmations and check calls from email into the TMS.
- Industry: freight brokerage and asset carriers (McLeod PowerBroker or LoadMaster, Aljex, Tailwind). Hurts most: brokers with 5-200 staff.
- Evidence: an inbox agent extracts fields "a human used to retype"; vendor-reported no-touch automation of 70-94% ([GetTransport](https://blog.gettransport.com/trends-in-logistic/ai-agents-freight-brokers-2026-quote-automation/)). McLeod's 25.2 adds automation.
- Hours: not found.
- Screen: a ✓, b likely, c ✓, d ✓, e ✓, f at risk (crowded field: Parade, Augment, Numeo, plus McLeod's own roadmap). Result: 5/6 provisional.
- Strongest argument against: crowding and vendor roadmap.

**P4. Home health and hospice referral intake from fax into the EMR**
- Industry: home health and hospice (WellSky, HCHB, Axxess). Hurts most: agencies with several branches.
- Who feels it: intake coordinator. Who approves: administrator or owner.
- Evidence: WellSky shipped AI completeness scoring and extraction in January 2026 ([Business Wire](https://www.businesswire.com/news/home/20260127232204/en/WellSky-Launches-New-AI-Capabilities-to-Automate-and-Scale-Referral-Intake)).
- Screen: a ✓ (daily), b likely (slow intake loses referrals; not quantified), c ✓, d ✓, e ✓ (needs HIPAA BAA), f at risk for WellSky shops. Result: 5/6 provisional.
- Strongest argument against: the EMR vendors are building it in.

**P5. Agency direct-bill commission reconciliation**
- Industry: P&C and benefits agencies (Applied Epic, AMS360, HawkSoft). Hurts most: agencies with 10-200 staff and many carriers.
- Task: download or parse carrier statements (PDF, CSV, paper), match them to policies, post to the general ledger, chase differences.
- Frequency: monthly per carrier, so roughly weekly across many carriers (inference).
- Evidence: [Applied Recon](https://int.appliedsystems.com/en-us/solutions/for-agents/financial-management/applied-recon/); [Epic help](https://help.appliedsystems.com/Help/Epic/2023.2en-US/General_Ledger/Reconciliations/Recs_Add_Direct_Bill_Rec.htm).
- Screen: 5/6, but fails (f) for Epic shops where Applied Recon is adopted (price not found). The non-Epic long tail is unverified.
- Shariah flag: conventional insurance, a possible issue.

**P6. Construction AP and job-cost double entry**
- Problem: double entry between field and project tools (Procore) and on-premise accounting (Sage 300 CRE, Viewpoint Vista).
- Hurts most: contractors with $20M-500M revenue (estimate; not sourced).
- Evidence this session: only the Sage end-of-life thread (long runway).
- Screen: a ✓ (weekly AP, inference), b unverified, c ✓, d ✓ (controller or CFO), e ✓, f unverified. Result: 4/6 provisional.

**P7. Order entry into ageing mid-market ERPs**
- Problem: staff key customer purchase orders and documents into old ERPs (Dynamics GP, plus Sage 100 and Epicor, untested).
- Context: GP support ends 31 December 2029 and security updates end 30 April 2031 ([Microsoft](https://www.microsoft.com/en-us/dynamics-365/blog/?p=194353)). Companies freeze spending on add-ons for the old ERP but still need relief from keying.
- Screen: 4/6 provisional (b and f unverified).
- Staying power: shrinks by 2031 as users migrate.

**P8. Nonprofit gift import into Raiser's Edge NXT**
- Fails (f): ImportOmatic from $100 a year ([Software Advice](https://www.softwareadvice.com/data-quality/importomatic-profile/)) and Importacular free tier ([Blackbaud Community](https://community.blackbaud.com/discussion/comment/228746)).
- Residual gap: duplicate matching ([GetApp review](https://www.getapp.co.uk/software/111547/importomatic)).

### Inferences
- Blind attractiveness (pain × willingness to pay × low competition × staying power), all provisional: P1 6, P2 6, P6 5, P4 5, P3 4, P5 4, P7 4, P8 2.

### Gaps
- Missing for every problem: US company counts, verified hours, fix prices, buyer channels.
- Auto dealer DMS, veterinary, HOA, funeral, legal and behavioral health were not tested.
