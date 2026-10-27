# Lens 05: Speed-loss problems (slow response loses money)

Research date: 27 October 2026. Researcher: lens-05 subagent.

Limits on this pass (please read first):
- WebFetch could not open any page. The session's egress proxy refused every page fetch I tried (clio.com, invoca.com, instalily.ai, businesswire.com, autoremarketing.com gave "CONNECT tunnel failed, 403" or ENOTFOUND). So every finding below comes from search-engine result summaries, not from reading the full source page. Treat exact figures as "as reported in search summaries of that page". Where a summary merged several pages and I cannot tell which page held a number, I say so.
- The shared web-search budget (200 searches per turn across all agents) ran out after about 22 of my searches. I could not run planned searches on: Clio's own 2025/2026 AI intake products, legal intake call-center pricing (e.g. Alert Communications, Lex Reception), auto BDC / AI BDC pricing (Impel, Numa, Toma, Conversica), EliseAI and PMS-native leasing AI pricing, freight spot-quote win-rate baselines, recruitment-agency speed-to-submit data, med spa (AmSpa) data, home care inquiry data, US company counts per industry, and owner/operator forum quotes (Reddit, Facebook groups, podcasts). Reddit, G2, Capterra and Upwork were never reached. These gaps are listed under each question.
- Almost all speed-to-lead numbers in 2025-2026 come from companies that sell a fix (call tracking, AI receptionists, AI leasing, mystery-shop firms). I mark them "vendor claim". Independent, peer-reviewed 2025-2026 studies were not found for any industry.

## Q1. Which industries have the best 2025-2026 evidence that response time drives conversion?

### Takeaway
The best recent evidence (large samples, mystery shops, 2025-2026 dates) exists for home services calls, auto/powersports web leads, legal intake, multifamily leasing and hotel group RFPs. Evidence that speed moves win rates (not only that firms are slow) is weakest everywhere and is mostly vendor-published. B2B quoting (job shops, distributors, freight) has the strongest stated speed-to-win link but the thinnest independent data.

### Cited Findings

Home services (HVAC, plumbing, electrical, garage doors, lawn, pest, cleaning)
- Invoca 2026 Home Services Lead Conversion Benchmarks: 52% of inbound home-services calls are answered by a person; 65% for calls over 15 seconds; 73% for calls over 30 seconds. 38% of calls from digital marketing are leads, and 45% of those leads convert on the call. Vendor claim (Invoca sells call tracking/AI). — [Invoca 2026 report page](https://invoca.com/reports/the-invoca-home-services-lead-conversion-benchmarks-report-2026); a secondary write-up gives 71% (not 73%) for over-30-second calls — [JustCall](https://justcall.io/blog/missed-call-statistics.html)
- CallRail January 2025 small-business benchmark: home services missed 14% of calls (reported secondhand; primary CallRail page not reached). Other vendor estimates run 20-45% (SkipCalls) and 27-30% for HVAC/plumbing (secondary citation of Invoca). Range across sources: 14% to 48% missed. — [SkipCalls 2025 benchmarks](https://skipcalls.com/blog/missed-call-benchmarks-2025-contractors); [Stealth Agents research page](https://stealthagents.com/research/home-services-missed-call-revenue-statistics-2026). A 62% figure from Layer3 Labs could not be traced to a study and is excluded — [Layer3 Labs](https://www.layer3labs.io/guides/ai-answering-service-for-home-services)
- Pied Piper PSI 2026 Home Services Lead Handling Effectiveness study: 31 of the largest home-services brands, 3,211 mystery-shop evaluations, October 2025 to January 2026. 42% of retail locations scored below 30 (an "ineffective interaction": phone not answered, no follow-up, little help). Only 12% scored 70 or higher. Precision Garage Door, Mister Sparky and Mr. Electric scored below 30 less than 20% of the time; The Maids, Lawn Doctor, Pinch A Penny, ForeverLawn and Camp Bow Wow scored below 30 more than 75% of the time. Pied Piper sells measurement/training (an interested party). — [Green Industry Pros, May 2026](https://www.greenindustrypros.com/business-management/marketing/press-release/22965698/pied-piper-management-co-llc-home-services-lead-failure-rate-hits-42-in-2026); [Pied Piper press release, April 2026](https://www.piedpiperpsi.com/press/press-release-precision-garage-door-ranked-1-in-customer-lead-handling-effectiveness-TM-home-services-study-521.htm)
- ServiceTitan 2025 platform data (secondhand): 9.8% (October) to 14.1% (June) of HVAC calls arrive outside business hours. CallRail 2025 consumer survey (secondhand): 78% of consumers have abandoned a business after an unanswered call. — [FieldCamp after-hours call statistics (vendor blog)](https://fieldcamp.ai/ai-receptionist/after-hours-call-statistics/)

Auto and powersports dealers (internet leads)
- Pied Piper 2026 Internet Lead Effectiveness (ILE) auto study: mystery inquiries to 3,290 dealership websites, responses scored over 24 hours. About three-quarters of online customers got a phone call (two-thirds the prior year). Texting answered the customer's question 54% of the time (38% prior year). Dealers did both a call and email/text 62% of the time (49% prior year). "Failed to respond" rate about 5% in auto vs 9% in powersports. Infiniti ranked highest. No sales-lift figure is published; Pied Piper says its scores track practices "mathematically likely to generate sales". — [Auto Remarketing (Infiniti 2026)](https://www.autoremarketing.com/ar/retail/infiniti-dealers-post-record-high-score-in-study-of-responsiveness-to-online-leads/); [2026 powersports study: Indian Motorcycle top, "5th year of stagnant performance"](https://am920theanswer.com/business/indian-motorcycle-ranked-highest-in-2026-web-lead-response-study-industry-enters/f18119d5b0bc4c4a9723ce7fe47a9727)
- Pied Piper 2026 dealer-group study: Napleton ranked first for the fifth year; average dealer-group score 74; 87% of Napleton's leads got a phone call within 15 minutes vs a 50% dealer-group average. The 50% figure appeared in one search summary but a second search could not confirm it; treat as unverified. — [Auto Remarketing (Napleton)](https://www.autoremarketing.com/ar/study-finds-napleton-tops-auto-groups-in-responding-to-website-customers); [Business Wire release, May 2026](https://www.businesswire.com/news/home/20260510538565/en/)
- Pied Piper 2023 ILE: industry average 58, highest in 13 years of measurement, 5,428 dealer websites (2023). 2012 baseline: 64% responded within 24 hours, 10% never responded (2012). — [F&I and Showroom](https://www.fi-magazine.com/news/pied-piper-sees-improvement-in-internet-lead-response-times); [WardsAuto archive](https://www.wardsauto.com/news/archive-wards-study-shows-vast-variability-in-how-car-dealers-field-e-inquiries/788292/)

Legal intake (personal injury, family, criminal, immigration)
- Clio secret-shopper study, 2024 Legal Trends Report: 1,000 firms contacted by email and phone across five practice areas. 67% did not respond to the email (33% did). 40% answered the phone; 52% answered or returned the call, down from 73% in 2019. The 2024 report also tested chatbots and intake forms. — [2civility (Illinois Supreme Court Commission on Professionalism), 2024](https://www.2civility.org/2024-clio-legal-trends-report-fixing-the-first-impression-problem-for-law-firms/); [Lawyers Mutual NC](https://www.lawyersmutualnc.com/risk-management-resources/articles/clio-legal-trends-report-the-legal-services-market-paradox)
- An earlier Clio release (search summaries disagree on year; the figures match the 2019 study) said 60% of firms did not respond to email and 27% did not answer the phone, and that 73% of legal shoppers would not recommend firms they contacted because of poor responsiveness. — [Clio press release](https://www.clio.com/about/press/clios-legal-trends-report-reveals-law-firms-struggle-to-respond-to-client-inquiries/)
- Some secondary sources attribute "33% of firms answer prospective-client emails" to the 2025 report; others attribute it to 2024. Unconfirmed for 2025. Clio's 2025 report did report that firms broadly adopting AI were about 3x as likely to report revenue growth. — [Canadian Lawyer on Clio 2025 report](https://www.canadianlawyermag.com/news/general/many-legal-clients-have-asked-artificial-intelligence-legal-questions-clio-report/393228); [Hyperleap legal intake stats 2026 (vendor)](https://hyperleap.ai/blog/legal-client-intake-statistics-2026)
- 79% of legal consumers expect a response within 24 hours (Clio 2019 consumer research, cited secondhand). — [Hyperleap (vendor)](https://hyperleap.ai/blog/legal-client-intake-statistics-2026); [Stealth Agents](https://stealthagents.com/research/legal-intake-response-time-statistics-2026)
- ClaireAI 2026 legal intake benchmark (vendor claim): 35% of inbound calls to law firms go to voicemail, and fewer than 10% of those callers leave a message. — [ClaireAI 2026 report](https://claireaiwebsite.pages.dev/blog/2026-legal-intake-benchmark-report)

Cross-industry service businesses
- Blazeo (ApexChat) 2026 Speed-to-Lead Benchmark, published 24 Feb 2026, 573 companies in six service industries (vendor claim): 35.4% of leaders say a 5-minute response is essential, but only 62.1% of those meet it. Over 40% of high-intent web inquiries arrive evenings/weekends; nearly 1 in 4 companies respond slowly or not at all to them. With a formal SLA, 54.9% hit 15 minutes vs 29.5% without. Firms using AI or automated routing were about 60% more likely to meet 15 minutes. — [Blazeo report page](https://discover.blazeo.com/speed-to-lead-2026-report); [TechDash coverage](https://techdash.in/blazeo-unveils-2026-speed-to-lead-benchmark-report-revealing-businesses-are-failing-their-own-response-time-standards/)

Multifamily leasing
- Nurture Boss "Multifamily Revenue Gap 2026" (vendor claim; platform data + secret shop of 1,100+ communities): 52.93% average unanswered leasing-call rate; average follow-up 36 hours vs under 8 hours for top properties; 8 touchpoints to get a tour, 10+ to get an application; 47.6% of properties stop before reaching either. — [Nurture Boss 2026 PDF](https://info.nurtureboss.io/hubfs/The%20Multifamily%20Revenue%20Gap%202026%20%E2%80%94%20Nurture%20Boss.pdf)
- Digible (2024): nearly 49% of calls to leasing offices never answered (cited by Layer3 Labs, vendor). Digible/Fiona analysis of 170,825 calls: up to 60.8% missed (cited by AI Front Desk, vendor). Range: 49% to 61%. — [Layer3 Labs](https://www.layer3labs.io/guides/ai-answering-service-for-property-management); [My AI Front Desk](https://www.myaifrontdesk.com/blog-posts/the-real-cost-of-missed-leasing-calls-at-apartment-communities)
- Zuma (vendor claim; 1.5M conversations): 23% of leads lost by the 18-minute mark; 70% of tours book within 1 hour of inquiry. Zuma's blog elsewhere says teams slower than 90 minutes lose 50% of leads (inconsistent with the 18-minute claim). — [Zuma Prospect Response Time Report](https://www.getzuma.com/report/prospect-response-time-report)
- Rent. survey (2024): 75% of multifamily professionals miss at least some leads; on average they cannot respond to 16% of leads. — [Rent. press release via Silicon UK, 2024](https://www.silicon.co.uk/press-release/more-than-75-of-leasing-teams-are-missing-qualified-leads-rent-study-finds)
- Thrive Communities case (AI vendor case in Apartment List article): after-hours follow-up lifted immediate response from 43% to 55% of leads over 60 days, and lead-to-application from 7% to 11%. Vendor claim. — [Apartment List](https://www.apartmentlist.com/rental-management/how-to-measure-ai-leasing-performance)
- Betterbot (vendor) says 60% of multifamily prospect engagement happens outside business hours, citing Zuma. — [Betterbot](https://betterbot.com/resources/4-hour-lead-response-delay)

Senior living
- Bild & Co. mystery shops (2023 data, reported Feb 2024): 250+ web and phone shops; 53% of web inquiries got no response within two hours; 13% of phone-shop calls never got any response. A Bild white paper reported 22% inquiry-to-tour conversion and 15% of shoppers never getting a return call. A later Bild quarter showed an average response lag of about 21 hours and an average 24.4% lead-to-tour conversion per month. (Exact article for each figure not verified because pages could not be fetched.) — [Senior Housing News, Feb 2024](https://seniorhousingnews.com/2024/02/12/senior-living-operators-level-up-sales-to-beat-alarming-trends-in-conversions/); [McKnight's Senior Living](https://www.mcknightsseniorliving.com/news/customized-tours-quick-response-are-keys-to-improving-tour-conversion-rates/)
- Enquire Solutions (2016, 1,000+ communities): 31% of call-ins never reached the CRM; 68% of web leads not converted; communities using call centers averaged 61% appointment conversion vs 37% without. — [Senior Housing News, 2016](https://seniorhousingnews.com/2016/03/09/senior-living-sales-suffer-missed-opportunities/)
- A Place for Mom mystery shopping (2010-2012): communities responding within 24 hours rose from 51% to 71%; some operators reported conversion gains up to 40% (2012). — reported in Senior Housing News coverage surfaced by search (exact URL not verified).

Hotel and venue group business (B2B RFPs)
- Cvent 2025 Planner Sourcing Report: 80% of planners expect a hotel/venue reply to an RFP within four days. Cvent's October 2025 pulse: only 57% of planners got a reply in four days or less, down from 70% the year before. — [Cvent blog, 20 Nov 2025](https://www.cvent.com/en/blog/hospitality/what-planners-really-think-october-pulse-takeaways-hotels); [Cvent blog, Jan 2026](https://www.cvent.com/en/blog/hospitality/inside-planner-behavior-what-data-reveals-about-group-hotel-bookings)
- Hospitality RFP win rates average 5-7%; planners send each RFP to about 10 venues (vendor claim, no method stated). — [HippoVideo 2025 playbook](https://www.hippovideo.io/blog/the-2025-playbook-6-field-tested-rfp-best-practices-for-hospitality-sales/)
- Aria Resort and Casino (Cvent case study): being among the first six responders improved RFP win odds by about 30%; 27% faster bid rate. Vendor case study; also a casino property (see halal flag). — [Cvent case study](https://www.casestudies.com/company/cvent/case-study/aria-resort-and-casino-customer-case-study)

B2B quoting (job shops, distributors)
- "Early Paperless Parts data": manufacturers that return quotes within two hours have a 90%+ win rate; shops that take five days or more win less than 5%. Reported secondhand by vendor blogs; primary data not found. Vendor claim. — [Docket blog](https://www.docket.io/blog/speed-to-quote-is-the-1-win-rate-variable-in-manufacturing-sales); [Broadn blog](https://www.broadn.io/blogs/fast-quoting-increases-manufacturing-win-rates)
- Paperless Parts webinar: 67% of buyers expect a quote in under 24 hours; if a quote has not gone out in 24 hours, "the job is likely already lost". Vendor claim. — [Paperless Parts webinar](https://www.paperlessparts.com/resources/webinar-how-to-increase-your-win-rate-when-quoting-machining-jobs/)
- Precision Machine: about 80% of the shop's revenue comes from quotes sent within an hour of draft-to-send time. BTM Industries cut turnaround from 2-3 days to under a day. Vendor case studies. — [Precision Machine case](https://www.paperlessparts.com/case-studies/precision-machine/); [BTM Industries case](https://www.paperlessparts.com/case-studies/btm-industries-improves-quoting-speed-and-consistency-with-paperless-parts/)
- Regional electrical distributor: quoted-business win rate below 40% rose to 61% within 90 days of quote automation. Vendor blog, no named data. — [Mirage blog](https://mirage-blog.pages.dev/blog/electrical-distributor-automation-quote-to-po-90-seconds/)
- Aberdeen 2025 is cited as finding 28% higher win rates for CPQ-enabled teams (unconfirmed; general CPQ, not distributors). — [Stealth Agents quote-automation stats](https://stealthagents.com/research/ai-quote-generation-automation-statistics-2026)
- A $12B distributor cut quote cycle times in half with automation (title-level only; page not read). Vendor case. — [ProfitOptics](https://www.profitoptics.com/how-a-12b-distributor-cut-quote-cycle-times-in-half-with-conversion-automation)

Freight brokers and forwarders (spot quotes)
- Under 15 minutes is called the "gold standard"; replies over 30 minutes "noticeably cut" win odds in a busy spot market (broker-tech guide, no data). Another vendor blog: manual quotes average 2-4 hours vs under 5 minutes automated, with win rates of 31% vs 14% (data source not named). — [Item.com brokerage quoting](https://www.item.com/transportation-management-system/freight-brokerage-spot-market-quoting); [Etheric Solution blog](https://etheric-solution.pages.dev/blog/why-speed-matters-so-much-in-freight-quoting/) (which of these two pages holds which figure was not verifiable)
- Tai TMS: instantly responding to quote requests raises win ratio "up to 30%". Vendor press claim. — [IT Supply Chain](https://itsupplychain.com/?p=47332)
- Freight forwarders: average quote response 90 hours; winners respond in under 30 minutes. Vendor claim, source not identified. — [GoFreight](https://gofreight.com/blog/education/quote-faster-win-more-speed-to-lead)

B2B SaaS inbound demo requests
- Workato (2022) test of 114 B2B companies: 11h54m average to send a personalized email; 14h29m to call. — [Workato, 2022](https://workato.com/the-connector/lead-response-time-study)
- RevenueHero (2024, n=1,000 websites): average response 1 day 5h17m; only 365 of 1,000 responded at all; manual demo-request handling averaged 2 days 3h11m. — [RevenueHero](https://www.revenuehero.io/blog/b2b-lead-response-times)
- Chili Piper: about 55% of companies took longer than an hour; over 80% took more than five minutes or did not respond. — [Chili Piper](https://www.chilipiper.com/article/chili-insights-vendor-response-time)
- Qualified report: only 7.2% respond within 5 minutes; 54% of enterprises take over an hour (report date unclear). — [Qualified](https://www.qualified.com/agentic-marketing-report)
- The much-repeated "42 hours average" and the "5-minute rule" trace to the 2011 HBR/InsideSales work (2011) and are not 2025-2026 evidence. — [Revenue Signal newsletter](https://revenueexperts.beehiiv.com/p/the-average-b2b-company-takes-42-hours-to-respond-to-a-lead)

Dental
- Peerlogic analysis of 26 dental practices (Feb 2026, vendor): 38% of calls unanswered; new-patient calls converted at 25.24% vs 55.77% for existing patients. Other vendor estimates of dental miss rates: 30-38%. — [Peerlogic](https://www.peerlogic.com/post/peerlogic-dso-case-study); [Dental Economics, "The economics of missed calls"](https://dentaleconomics.com/practice/article/55385634/the-economics-of-missed-calls-quantifying-revenue-loss-in-dental-practices) (title only; page not read)

Commercial insurance agencies
- No industry benchmark linking quote turnaround to win rate was found. A practitioner post says producers are expected to quote 900-1,500 new-business submissions a year and that a 72-hour turnaround loses to competitors who reply in about 4 hours (anecdote). — [DEV Community post](https://dev.to/rmccain_cns/the-quiet-productivity-ceiling-inside-independent-insurance-agencies-5eka)
- Vertafore/Dimond Bros (2025): commercial-lines classification step cut from about 20 minutes to about 2 minutes. Verisk marketing: time to quote "from an average of two days to 1.5 seconds". Nationwide (2022): 70%+ success bypassing data entry/classification when business info is online. Vendor claims. — [Coverager](https://coverager.com/vertafore-recognizes-dimond-bros-insurance-for-leadership-in-accelerating-small-commercial-quoting/); [Verisk LightSpeed PDF](https://www.verisk.com/siteassets/media/downloads/underwriting/small-commercial/lightspeed-small-commercial.pdf); [Nationwide, 2022](https://news.nationwide.com/accelerating-small-commercial-quoting-for-agents/)
- AI quoting case (anonymous, vendor): time to a bindable commercial indication fell from 48 hours to 2-6 hours. — [Seven Peaks Software](https://sevenpeakssoftware.com/case-studies-v2/increased-win-rate-and-improved-returns-with-an-ai-driven-quotation-engine)

### Inferences
- Ranking by quality of 2025-2026 "companies are slow" evidence: home services (Invoca 2026, Pied Piper 2026) > auto/powersports (Pied Piper 2026) > legal (Clio 2024) > multifamily (vendor 2026) > hotel RFP (Cvent 2025) > senior living (2023-24) > B2B quoting / freight / insurance (vendor anecdotes only).
- Ranking by strength of "speed changes the win rate" evidence: B2B job-shop quoting (Paperless Parts, vendor) and freight (vendor) make the strongest claims, but none is independently verified. In B2C, the clearest link is indirect: unanswered calls rarely call back (Invoca 45% on-call conversion of answered leads; ClaireAI under 10% leave voicemail).
- A key pattern: slowness is getting worse in some places (Cvent: hotel replies within 4 days fell from 70% to 57%; Clio: answer-or-callback fell from 73% in 2019 to 52% in 2024), and flat in others (powersports "5th year stagnant").

### Gaps
- No independent (non-vendor) 2025-2026 study measuring conversion lift from faster response in any industry was found.
- Clio 2025 and 2026 Legal Trends Reports: I could not confirm whether either repeated the secret-shopper test.
- Recruitment agencies (speed to submit candidates), med spas (AmSpa), home care agencies, event venues (non-hotel) and short-term rental guest messaging: no data gathered (search budget exhausted / no results). Home care: the one search found no response-time benchmark; Activated Insights cites only that 32% of people were satisfied with how businesses handled inquiry calls — [Activated Insights](https://activatedinsights.com/?p=53662).

## Q2. For each industry: current response time, lift from faster response, missed-call rates, value of a lost lead, leads per week

### Takeaway
Current-state slowness is well documented (roughly a third to a half of calls unanswered in home services, legal, multifamily and dental; hours-to-days for web leads and quotes). Lead value and weekly lead volume are the weakest data points; most dollar-loss figures are vendor models built on assumptions.

### Cited Findings
- Home services: answer rate 52% (all calls) to 73% (calls over 30s) — [Invoca 2026](https://invoca.com/reports/the-invoca-home-services-lead-conversion-benchmarks-report-2026). After-hours share of HVAC calls 9.8-14.1% (ServiceTitan 2025 data, secondhand) — [FieldCamp](https://fieldcamp.ai/ai-receptionist/after-hours-call-statistics/). Dollar-loss estimates of "$45,000-$120,000 per year" per business appear in vendor content but rest on assumed inputs — [FieldCamp](https://fieldcamp.ai/ai-receptionist/after-hours-call-statistics/).
- Legal: phone answered 40%, answered-or-returned 52%, email answered 33% (2024) — [2civility](https://www.2civility.org/2024-clio-legal-trends-report-fixing-the-first-impression-problem-for-law-firms/). Voicemail 35% of calls, <10% leave a message (vendor) — [ClaireAI](https://claireaiwebsite.pages.dev/blog/2026-legal-intake-benchmark-report). Case value per lost PI/immigration lead: not found.
- Auto: ~75% of web leads get a phone call; ~5% no response in 24 hours (auto), 9% (powersports) — [Auto Remarketing](https://www.autoremarketing.com/ar/retail/infiniti-dealers-post-record-high-score-in-study-of-responsiveness-to-online-leads/); [AM920 powersports](https://am920theanswer.com/business/indian-motorcycle-ranked-highest-in-2026-web-lead-response-study-industry-enters/f18119d5b0bc4c4a9723ce7fe47a9727).
- Multifamily: unanswered leasing calls 49-61% (vendor) — [Layer3 Labs](https://www.layer3labs.io/guides/ai-answering-service-for-property-management); [My AI Front Desk](https://www.myaifrontdesk.com/blog-posts/the-real-cost-of-missed-leasing-calls-at-apartment-communities); average follow-up 36 hours (vendor) — [Nurture Boss](https://info.nurtureboss.io/hubfs/The%20Multifamily%20Revenue%20Gap%202026%20%E2%80%94%20Nurture%20Boss.pdf). Value: RentCafe August 2026 national average rent $1,771, about $59 of lost income per vacant day — [My AI Front Desk citing RentCafe](https://www.myaifrontdesk.com/blog-posts/the-real-cost-of-missed-leasing-calls-at-apartment-communities). Estimate: one lost lead that adds one vacant week = 7 x $59 = about $413 (estimate).
- Senior living: 53% of web inquiries no response in 2 hours; ~21-hour average lag; 22-24.4% lead-to-tour (2023-24, Bild) — [Senior Housing News](https://seniorhousingnews.com/2024/02/12/senior-living-operators-level-up-sales-to-beat-alarming-trends-in-conversions/). Value of a move-in: not found this session.
- Hotel group RFP: 57% of planners get a reply in 4 days or less (Oct 2025) — [Cvent](https://www.cvent.com/en/blog/hospitality/what-planners-really-think-october-pulse-takeaways-hotels); win rate 5-7%, ~10 venues per RFP (vendor) — [HippoVideo](https://www.hippovideo.io/blog/the-2025-playbook-6-field-tested-rfp-best-practices-for-hospitality-sales/).
- Job shops: under 2 hours = 90%+ win; 5+ days = under 5% (vendor, secondhand) — [Docket](https://www.docket.io/blog/speed-to-quote-is-the-1-win-rate-variable-in-manufacturing-sales).
- Freight: manual 2-4 hours vs automated under 5 minutes; 31% vs 14% win (vendor, unsourced) — [Etheric Solution](https://etheric-solution.pages.dev/blog/why-speed-matters-so-much-in-freight-quoting/). Vooma says its tool saves 5 minutes per quote (company claim) — [FreightWaves](https://www.freightwaves.com/news/vooma-grabs-16-6m-in-funding-as-brokers-prepare-for-market-swing).
- Insurance: 900-1,500 submissions per producer per year (practitioner anecdote) — [DEV Community](https://dev.to/rmccain_cns/the-quiet-productivity-ceiling-inside-independent-insurance-agencies-5eka). Estimate: 900/52 = about 17 to 1,500/52 = about 29 submissions per producer per week (estimate).
- B2B SaaS: average first response 1 day 5h17m; 63.5% (635 of 1,000) never responded (2024) — [RevenueHero](https://www.revenuehero.io/blog/b2b-lead-response-times).
- Dental: 38% unanswered; new-patient call conversion 25.24% (vendor, Feb 2026) — [Peerlogic](https://www.peerlogic.com/post/peerlogic-dso-case-study). New-patient first-year value $785 to $850-1,300; lifetime $8,000-10,000+ (vendor estimates) — [JustCall dental](https://justcall.io/blog/missed-dental-calls-ai-receptionist-revenue-loss.html); [Newo](https://newo.ai/dental-office-missing-patient-calls-measure-fix-revenue/).

### Inferences
- Where a lost lead is worth thousands (PI case, senior-living move-in, job-shop RFQ, hotel group block, freight load stream), even a modest service fee clears ROI with a handful of saved leads per month. Where a lead is worth a few hundred dollars (residential repair call, dental cleaning), cheap software wins on price.

### Gaps
- Leads per week per typical company: not found for any industry except the insurance anecdote above.
- Average job/case/load/group value: not found this session for home services, PI law, freight, senior living, hotels. These must be sourced before pricing any offer.
- Owner/operator quotes: none collected from forums, Facebook groups or podcasts (search budget exhausted; Reddit/Facebook not reached). The only operator voice found is a vendor-published, undated testimonial from Metalmite (machine shop) on Paperless Parts' site, paraphrased in search results as "it looks professional, and we win it faster than we're used to" (exact wording and speaker not verified) — [Paperless Parts customer story](https://www.paperlessparts.com/customer-stories/metalmite/). A senior-care podcast episode titled "Why senior care communities lose leads after hours" exists but was not heard — [SilverCore.io Growth Podcast](https://www.buzzsprout.com/2602265/episodes/19148046-why-senior-care-communities-lose-leads-after-hours).

## Q3. What do companies pay today, who sells a fix, how crowded, and what is already solved under $100/month or free?

### Takeaway
Basic call answering, missed-call text-back and instant demo booking are commodity: $29-$99/month AI tools and vertical-software add-ons (Jobber $29) cover small firms, and the mid-market is being taken by well-funded vertical AI (Avoca at a $1B valuation). Human answering services cost $230-$400/month for small minute bundles. B2B quoting (RFQs, freight spot quotes, hotel RFPs, small-commercial insurance) has no sub-$100 fix because it needs pricing data, system access and judgment.

### Cited Findings
- Sub-$100 AI receptionists (third-party/vendor comparison blogs; prices conflict): Dialzara $29 (60 min) and $99 (220 min); Rosie $49 (250 min), with booking/transfers on a $99 or $149 plan (sources disagree); Goodcall $59-$79 (per unique caller); My AI Front Desk free (20 min) and $99 (200 min); Marlie AI from $49. — [Dupple](https://dupple.com/learn/best-ai-receptionists); [Aira (Rosie alternatives)](https://www.getaira.io/blog/rosie-alternatives); [Voksha pricing guide](https://voksha-website.pages.dev/guide/ai-receptionist-pricing-guide); [Techloy](https://www.techloy.com/8-best-ai-receptionists-for-home-services-in-2026/)
- Vertical software: Jobber Receptionist add-on $29/month with 30 conversations, then $0.79 each; included unlimited on the Plus plan (another source says $99). Housecall Pro sells CSR AI / 24-7 answering separately (price not published). ServiceTitan AI features priced by quote. — [Sagnik Bhattacharya comparison](https://sagnikbhattacharya.com/blog/jobber-housecall-pro-servicetitan-ai); [Plyrium comparison](https://plyrium.com/academy/all-trades/service-business-software-comparison)
- Human answering services (third-party comparisons, 2026): Smith.ai about $95/month (50 AI calls) or $150 (75 AI calls); human tier about $300 for 30 calls; add-ons such as booking $1.50/call. Ruby about $230-$250/month for 50 minutes. AnswerConnect about $325-$395/month (300 minutes at $395). Per-minute effective rates $1.10-$2.00. — [Ringly](https://www.ringly.io/blog/best-answering-service); [Retell AI](https://www.retellai.com/blog/best-phone-answering-service); [JustCall Smith.ai alternatives](https://justcall.io/blog/best-smith-ai-alternatives.html)
- Mid-market home services AI: Avoca raised $125M+ at a $1B valuation (April 2026), Series B co-led by Meritech and General Catalyst; Series A led by Kleiner Perkins; customers include Turnpoint, 1-800-GOT-JUNK?, Goettl; partners ServiceTitan, Nexstar, Clover. Pricing not published; one third-party guide estimates $1,000-$5,000+/month for mid-to-large operators. Sameday AI: $249/month (100 calls) and $499/month (300 calls) per an aggregator. — [Pulse 2.0 on Avoca](https://pulse2.com/avoca-125-million-raised-at-1-billion-valuation-to-power-services-economy-with-ai/); [Stork comparison](https://www.stork.ai/compare/sameday-ai-vs-avoca-ai); [B2B Sales Tools guide](https://b2bsalestools-com.pages.dev/guides/best-ai-receptionist-home-services/)
- Freight: Vooma raised $16.6M (YC W23), automates email quote replies and outcome tracking, McLeod certified partner, SONAR rate-data partnership. C.H. Robinson built in-house automated truckload quoting (older report). — [FreightWaves](https://www.freightwaves.com/news/vooma-grabs-16-6m-in-funding-as-brokers-prepare-for-market-swing); [McLeod partner page](https://www.mcleodsoftware.com/certified-partners/vooma/); [Benzinga](https://benzinga.com/z/38667698)
- Job shops / distributors: Paperless Parts (job-shop quoting software); Instalily, ProfitOptics, Docket, Broadn, Rapid Automation sell quote automation to manufacturers/distributors (pricing not found). — [Paperless Parts](https://paperlessparts.com/); [ProfitOptics](https://www.profitoptics.com/how-a-12b-distributor-cut-quote-cycle-times-in-half-with-conversion-automation); [Rapid Automation](https://rapidautomation.ai/blog/true-cost-manual-quote-generation-manufacturing)
- Hotels: Cvent's own Business Intelligence tracks hotel response times and win rates; HippoVideo sells RFP response video tools. — [Cvent case study](https://www.casestudies.com/company/cvent/case-study/aria-resort-and-casino-customer-case-study); [HippoVideo RFP automation](https://www.hippovideo.io/blog/hotel-rfp-automation-2025-guide/)
- Multifamily: Nurture Boss raised $4.025M; Zuma, Betterbot, Fiona/Digible sell AI leasing/answering. — [Pulse 2.0 on Nurture Boss](https://pulse2.com/nurture-boss-4-025-million-raised-to-enable-apartment-owners-and-operators-to-convert-more-prospects/amp/); [Zuma](https://getzuma.com/post/multifamily-property-management-ai-in-2025)
- B2B SaaS: Chili Piper, RevenueHero, Qualified sell instant routing/booking and AI SDRs. — [Chili Piper](https://www.chilipiper.com/article/chili-insights-vendor-response-time); [Qualified](https://www.qualified.com/agentic-marketing-report)

### Inferences
- (f) is failed plainly by: basic missed-call answering and text-back for small home-services firms, dental and med spa offices, and solo/small law firms that only need message-taking; and by instant demo booking for B2B SaaS (scheduling routers and CRM-native AI SDRs). These niches are crowded and price-compressed.
- (f) is passed by: work that needs a human to set a price or make a judgment call, such as RFQ quoting, freight spot pricing, hotel group proposals, small-commercial insurance indications, regulated legal intake (conflict checks, statute deadlines, sign-up), and high-consideration senior-living inquiries.

### Gaps
- Not verified this session: Clio's own AI intake/receptionist products (could make legal intake fail f), Yardi/RealPage/Entrata native AI leasing and EliseAI pricing (could make multifamily fail f for mid/large operators), dealer CRM auto-responders and AI BDC pricing (Impel, Numa, Toma, Conversica), Podium/Hatch pricing, HubSpot/Salesforce free features. These were planned searches the budget did not allow.

## Q4. Where does a pure AI tool fail, so AI plus a human checker wins?

### Takeaway
Pure AI is good enough for answering, FAQs and booking open calendar slots. It fails where a wrong answer costs money or creates legal exposure: setting a price, promising capacity or dates, deciding whether a matter or customer is acceptable, and anything regulated. These are the speed-loss problems where a monthly AI-plus-human service has room.

### Cited Findings
- Vendors themselves concede limits on cheap tiers: booking, transfers and SMS often need higher plans, and "the cheap tier is realistically a trial, not a destination." — [Voksha pricing guide](https://voksha-website.pages.dev/guide/ai-receptionist-pricing-guide); [Aira](https://www.getaira.io/blog/rosie-alternatives)
- Freight quoting tools pull data from emails and pricing tools but brokers still validate pricing against market rates (SONAR partnership exists for that check). — [McLeod partner page](https://www.mcleodsoftware.com/certified-partners/vooma/); [FreightWaves on Vooma + SONAR](https://www.freightwaves.com/?p=569411)
- Insurance tools reach 70%+ automation only "when business information is accurate and visible online" (2022), implying the rest needs manual work. — [Nationwide, 2022](https://news.nationwide.com/accelerating-small-commercial-quoting-for-agents/)
- Clio 2025: among clients who asked AI legal questions, 28% were told to contact a lawyer (shows consumers already use AI first, and still need a human). — [Canadian Lawyer](https://www.canadianlawyermag.com/news/general/many-legal-clients-have-asked-artificial-intelligence-legal-questions-clio-report/393228)
- Multifamily follow-up needs 8-10+ touches; nearly half of properties quit early (vendor). Persistence plus judgment on fit (pets, income, move date) is where people still matter. — [Nurture Boss](https://info.nurtureboss.io/hubfs/The%20Multifamily%20Revenue%20Gap%202026%20%E2%80%94%20Nurture%20Boss.pdf)

### Inferences
- Human-in-the-loop wins in: (1) B2B RFQ quotes needing part cross-reference, stock checks and margin decisions; (2) freight spot quotes for small brokers without in-house pricing engines; (3) hotel/venue group proposals (dates, room blocks, F&B minimums); (4) legal intake with conflict checks, deadlines, bilingual callers and sign-up; (5) senior-living inquiries involving care level, cost and family emotion; (6) small-commercial insurance indications needing class codes and carrier appetite.
- As models improve over 24 months, pure-AI coverage will expand into (1)-(3) for standard items, so the human checker's share shrinks; the durable part is accountability (someone signs off a price or a legal step) and system access (ERP/TMS/PMS credentials).

### Gaps
- No vendor or study quantified AI error rates in quoting or intake. No source found on liability allocation when an AI quote is wrong.

## Q5. Problem records against the six tests (a-f)

### Takeaway
Six problems pass or nearly pass: B2B RFQ quoting (distributors/job shops), legal intake for PI/immigration/family firms, senior-living inquiry handling, hotel/venue group RFPs, freight spot quotes for small brokers, and small-commercial insurance quoting. Home-services missed calls, dental/med spa calls, B2B SaaS demo routing and auto dealer leads fail (f) because cheap or bundled tools already exist or funded vertical AI owns the space.

### Cited Findings
(Fields marked "inference" are researcher judgment, not sourced facts. Association/channel names are from general knowledge and were not verified this session.)

P1. B2B RFQ / quote turnaround: industrial distributors, job shops, fabricators
- Problem: RFQs sit in inboxes for days; the first credible quote usually wins.
- Industry / size: industrial and electrical distribution, CNC/fab job shops; 10-500 staff (inference).
- Task: read RFQ email/PDF/drawing, cross-reference parts, check stock and price, draft quote, human approves margin, send within hours.
- Who feels it / approves: inside sales and estimators feel it; owner, GM or VP Sales approves (inference).
- Frequency: daily (inference). Dollar evidence: 2-hour quotes 90%+ win vs 5+ days under 5% (vendor, secondhand) — [Docket](https://www.docket.io/blog/speed-to-quote-is-the-1-win-rate-variable-in-manufacturing-sales); 80% of one shop's revenue from quotes sent within an hour — [Paperless Parts](https://www.paperlessparts.com/case-studies/precision-machine/); distributor win rate under 40% to 61% (vendor) — [Mirage](https://mirage-blog.pages.dev/blog/electrical-distributor-automation-quote-to-po-90-seconds/).
- Today: in-house estimators/inside sales; quoting software (Paperless Parts) and newer AI vendors (Instalily, ProfitOptics, Docket, Broadn). Price not found. Crowding: moderate and rising.
- AI trend: grows for 24 months (more RFQs read automatically) but standard items become pure-AI; custom/engineered quotes keep the human (inference).
- Reach: NAW, MDM events/newsletter, Industrial Distribution, FMA (fabricators), AMT, ERP partners such as Epicor/Infor/P21 resellers (unverified channel names).
- US count: not found.
- Against: ERP/pricing data access is hard; buyers may prefer software they own; long sales cycles.
- Tests: a pass, b pass, c pass, d pass, e pass (with human sign-off), f pass. 6/6.

P2. Legal intake for PI, immigration, family and criminal firms
- Problem: about half of calls and two-thirds of emails get no timely answer; callers move on.
- Size: solo to 50-lawyer firms (inference).
- Task: answer 24/7, qualify, conflict check, capture facts, book consult, send retainer, bilingual; lawyer reviews.
- Who / approves: intake staff and paralegals feel it; managing partner approves.
- Evidence: 40% phone answered, 33% email answered (2024) — [2civility](https://www.2civility.org/2024-clio-legal-trends-report-fixing-the-first-impression-problem-for-law-firms/); 35% to voicemail, under 10% leave messages (vendor) — [ClaireAI](https://claireaiwebsite.pages.dev/blog/2026-legal-intake-benchmark-report).
- Today: receptionists, Smith.ai ($95-$300+), Ruby ($230-$250), AnswerConnect ($325-$395) — [Ringly](https://www.ringly.io/blog/best-answering-service). Crowded at the message-taking level.
- AI trend: grows; regulation (no legal advice, UPL) keeps a human checker (inference).
- Reach: state bar practice-management programs, AAJ and state trial-lawyer associations, AILA, Clio partner ecosystem, legal marketing agencies (unverified).
- Against: crowded with legal-specialist answering services; Clio or other practice platforms may bundle AI intake (unverified).
- Tests: 6/6 tentative (f passes only for full intake-to-signed-retainer, not plain answering). Halal: PI recoveries are mostly paid by conventional insurers, a possible Shariah question; flag for scholar.

P3. Senior living (and likely home care) inquiry response
- Problem: families inquire evenings/weekends; communities reply in about 21 hours on average.
- Size: single communities and regional operators of 2-30 communities (inference).
- Task: answer within minutes, qualify care level and budget, book tour, persistent follow-up; sales director handles the tour.
- Who / approves: sales/community relations director feels it; executive director or VP Sales approves.
- Evidence: 53% no reply in 2 hours, 13% of calls never answered (2023-24) — [Senior Housing News](https://seniorhousingnews.com/2024/02/12/senior-living-operators-level-up-sales-to-beat-alarming-trends-in-conversions/); call-center communities 61% vs 37% appointment conversion (2016) — [Senior Housing News 2016](https://seniorhousingnews.com/2016/03/09/senior-living-sales-suffer-missed-opportunities/).
- Today: in-house sales staff, CRMs (Enquire/Aline, Welcome Home), call centers, referral agencies (pricing not found).
- AI trend: grows; emotional, high-value sale keeps human (inference).
- Reach: Argentum, ASHA, NIC, state LeadingAge/assisted-living associations, Senior Housing News events (unverified).
- Against: evidence is 2016-2024, not 2025-2026; large operators run central sales centers; move-in value not sourced.
- Tests: 6/6 tentative.

P4. Hotel and event-venue group RFPs and event inquiries
- Problem: planners expect replies in 4 days; only 57% get them; first responders win more.
- Size: independent and small-brand hotels, conference centers, event venues (inference).
- Task: read RFP, check dates/space/rates, draft proposal, sales manager approves, send same day.
- Who / approves: hotel sales manager feels it; director of sales or GM approves.
- Evidence: — [Cvent Nov 2025](https://www.cvent.com/en/blog/hospitality/what-planners-really-think-october-pulse-takeaways-hotels); first-six responders +30% win odds (vendor case) — [Cvent/Aria](https://www.casestudies.com/company/cvent/case-study/aria-resort-and-casino-customer-case-study); win rate 5-7% (vendor) — [HippoVideo](https://www.hippovideo.io/blog/the-2025-playbook-6-field-tested-rfp-best-practices-for-hospitality-sales/).
- Today: hotel sales staff, brand sales centers, Cvent tools.
- Reach: HSMAI, AHLA, Cvent CONNECT, Tripleseat/Cvent partner ecosystems (unverified).
- Against: Cvent can add AI responses natively; brand-managed hotels use central systems.
- Tests: 6/6 tentative. Halal: casino resorts (gambling) and alcohol-centered venues should be excluded; most hotels serve alcohol, flag for scholar.

P5. Freight spot-quote emails for small and mid brokers (and forwarders)
- Problem: quote requests pile up; slow replies lose loads.
- Size: 5-100 person brokerages (inference).
- Task: parse quote email, pull lane rate, draft price, broker approves, reply in minutes.
- Evidence: vendor claims only (31% vs 14% win; up to 30% higher win) — [Etheric Solution](https://etheric-solution.pages.dev/blog/why-speed-matters-so-much-in-freight-quoting/); [IT Supply Chain](https://itsupplychain.com/?p=47332).
- Today: brokers and pricing desks; Vooma ($16.6M raised), TMS add-ons; large brokers build in-house — [FreightWaves](https://www.freightwaves.com/news/vooma-grabs-16-6m-in-funding-as-brokers-prepare-for-market-swing).
- AI trend: shrinks for a services firm as TMS-native AI matures (inference).
- Reach: TIA, FreightWaves events, McLeod/Turvo/Aljex partner programs (unverified).
- Against: funded software vendors, cyclical freight market, thin broker margins.
- Tests: a-e pass; f partial (no sub-$100 tool, but funded AI vendors). 5/6.

P6. Small-commercial insurance quote turnaround at independent agencies
- Problem: 48-72 hour indications lose to 4-hour competitors (anecdotal).
- Size: independent agencies with 5-50 staff (inference).
- Task: gather business info, class-code, fill carrier portals, compare, producer approves.
- Evidence: weak — [DEV Community](https://dev.to/rmccain_cns/the-quiet-productivity-ceiling-inside-independent-insurance-agencies-5eka); [Seven Peaks (vendor)](https://sevenpeakssoftware.com/case-studies-v2/increased-win-rate-and-improved-returns-with-an-ai-driven-quotation-engine).
- Today: account managers, offshore staff, comparative raters (Vertafore, EZLynx) — [Insurance Journal / EZLynx 2026](https://www.insurancejournal.com/blogs/ezlynx/2026/06/19/874221.htm).
- Reach: Big I (IIABA), state agent associations, Vertafore/Applied user groups (unverified).
- Against: carrier portals and raters are automating; win-rate link not proven.
- Tests: 5/6 (b weakly evidenced). Halal: conventional insurance is a possible Shariah issue; flag.

P7. Multifamily leasing inquiries (small and mid property managers)
- Evidence: 49-61% calls missed; 36-hour follow-up (vendor) — [Nurture Boss](https://info.nurtureboss.io/hubfs/The%20Multifamily%20Revenue%20Gap%202026%20%E2%80%94%20Nurture%20Boss.pdf); $59/vacant day — [My AI Front Desk](https://www.myaifrontdesk.com/blog-posts/the-real-cost-of-missed-leasing-calls-at-apartment-communities).
- Against: many funded AI leasing vendors; PMS-native AI likely (unverified).
- Tests: likely fails f for mid/large operators; possible pass for small managers. 5/6.

P8. Home-services missed calls and after-hours leads
- Evidence: 52% answered (Invoca 2026); 42% ineffective lead handling (Pied Piper 2026).
- Against: Jobber $29, Rosie $49, Dialzara $29-$99, Avoca $1B valuation.
- Tests: fails f for small firms (Jobber $29/mo, Rosie $49/mo). 5/6.

P9. Auto and powersports internet leads
- Fails f: dealer CRMs and AI BDC vendors already crowd it (pricing not verified); Halal: dealer sales lean on interest-based auto finance, flag.

P10. B2B SaaS inbound demo requests
- Fails f: instant scheduling/routing tools and CRM-native AI SDRs.

P11. Dental and med spa booking calls
- Fails f: sub-$100 AI receptionists and practice communication platforms. Med spa data not found.

### Inferences
- Attractiveness (blind, 1-10): P1 8, P2 7, P3 7, P4 6, P5 6, P6 5, P7 4, P8 3, P9 3, P11 3, P10 2.

### Gaps
- US company counts for every problem: not found this session.
- Recruitment agencies (speed to submit candidates) and short-term rental guest messaging: not researched (search budget exhausted).
