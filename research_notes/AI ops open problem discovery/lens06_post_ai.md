# Lens 06: Post-AI problems (business problems that AI adoption or AI misuse itself created, 2024-2026)

Research date: 27 October 2026. Scope: problems that exist because of AI, recur weekly, cost money, and could be handled on a monthly retainer by AI plus human experts. US first, then UK and Australia. USD.

**How this was researched, and its limits (read first).**
- I ran 28 web searches. Then the shared web-search budget ran out ("limit: 200 WebSearch calls per turn, shared by every agent").
- Direct page fetches did not work. WebFetch returned DNS errors (ENOTFOUND) for escape.tech, financialprofessionals.org, retailgazette.co.uk, modernretail.co and gartner.com. curl through the egress proxy was refused with 403 for the same hosts plus zylo.com and scopenine.com.
- So every figure below comes from search-engine summaries of the cited pages. I did not open the primary pages. The report writer should treat headline numbers as "reported by" the cited page and spot-check them before publication.
- Reddit, Upwork, G2, Capterra, Facebook groups and YouTube were not reached at all, because the search budget ran out first. They were not blocked by the sites themselves. So I have very few verbatim owner or operator quotes.
- Some (f)-test checks rest on my own background knowledge rather than a source found in this session. These are marked **[prior knowledge, not re-verified, no URL]** and must be checked before use.
- "Vendor claim" = the number comes from a company that sells a fix.

---

## Key Question 1: Which AI-created problems have the strongest 2025-2026 evidence?

### Takeaway
The strongest, best-quantified AI-created problems are:
- AI-forged documents and AI impersonation hitting finance teams (FBI IC3 now has a dedicated AI section).
- AI-faked refund and damage claims in e-commerce.
- Insecure or unmaintainable "vibe-coded" apps.
- Shadow-AI data leakage.
- AI search cutting website clicks.
- Fake and AI-assisted job candidates.
- Stalled or abandoned AI pilots.
- Hallucinated content in professional work product.

Evidence quality varies. Fraud and search-click data come from neutral bodies (FBI, AFP, Pew, Seer). Vibe-code security, shadow-AI and refund-fraud figures come mostly from vendors. The "95% of pilots fail" figure is widely disputed.

### Cited Findings

#### P1. Insecure or unmaintainable AI-built ("vibe-coded") apps and automations
- Escape.tech scanned about 5,600 publicly available vibe-coded apps built on Lovable, Bolt.new and Create.xyz (2025). It covered about 14,600 assets and found 2,000+ vulnerabilities, 400+ exposed secrets and 175 instances of leaked personal data. It used passive scanning, so these are likely undercounts. Vendor claim: Escape sells app-security scanning. — [Escape.tech methodology](https://escape.tech/blog/methodology-how-we-discovered-vulnerabilities-apps-built-with-vibe-coding/); numbers via secondary summary [vibecodedirectory](https://vibecodedirectory.beehiiv.com/p/the-hidden-cost-of-speed-why-45-of-vibe-coded-apps-have-security-vulnerabilities-and-how-to-fix-it)
- RedAccess investigated apps built on Lovable, Replit, Base44 and Netlify. About 40% leaked private information, including medical records, financial data, corporate strategy documents and customer chatbot logs. Vendor claim. — [The Next Web](https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed)
- Lovable: 170 of 1,645 Lovable-created web apps (about 10.3%, my math) shared the same critical flaw. Separately, a broken-access-control (BOLA) bug stayed open for 48 days after a bug-bounty report was closed without escalation. — [The Next Web](https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed)
- Tenzai built 3 identical apps with each of 5 AI coding tools. It found 69 vulnerabilities across the 15 apps, 6 of them critical. None of the tools produced exploitable SQL injection or XSS, but access-control and authorization logic was weak. Vendor claim. — [The Next Web](https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed)
- Astra gave 4 tools (Emergent, Replit, Lovable, Base44) the same prompt and reported 137 vulnerabilities across the resulting apps. Vendor claim. — [Astra](https://www.getastra.com/reports/vibe-coding-security-risks-study)
- Fastly surveyed 791 developers (July 2025):
  - 28% spend so much time fixing AI-generated code that it wipes out most of the time savings.
  - Only 14% rarely need to make changes.
  - About a third of seniors (10+ years) say more than half their shipped code is AI-generated.
  - One outlet reports 65% frequently have to go back over AI code.
  - Source: [Fastly blog](https://www.fastly.com/blog/senior-developers-ship-more-ai-code); [The New Stack](https://thenewstack.io/fastly-senior-devs-ship-2-5x-more-ai-code-than-juniors/); [ITPro](https://itpro.com/software/development/senior-developers-are-all-in-on-vibe-coding-but-junior-staff-lack-the-experience-to-spot-critical-flaws)
- Typical production breakpoints in Lovable apps: users randomly logged out, a redirect loop after login, and data visible to the wrong user. Lovable does not handle payment and limit logic, load, integrations or ongoing maintenance. Agency blogs, so commercially interested. — [Agence Scroll](https://agence-scroll.com/en/blog/why-your-lovable-app-wont-hold-1000-users-and-what-to-do-before-production); [Megumethod](https://www.megumethod.com/blog/lovable-app-to-production)
- Scale of the installed base:
  - Lovable became a unicorn with a $200M Series A eight months after launch (July 2025). — [TechCrunch](https://techcrunch.com/2025/07/17/lovable-becomes-a-unicorn-with-200m-series-a-just-8-months-after-launch)
  - "How Lovable Reached 2.3M Users" (secondary newsletter). — [Catalaize](https://catalaize.substack.com/p/lovables-path-from-open-source-to)
- Widely reported 2025 incidents that I could not re-source this session: Replit's agent deleted a SaaStr production database (July 2025), and the Tea app image leak (July 2025). **[prior knowledge, not re-verified, no URL]**

#### P2. Stalled or abandoned AI pilots and agents with no owner
- MIT NANDA, "The GenAI Divide: State of AI in Business 2025" (Aug 2025): about 5% of AI pilots achieve rapid revenue acceleration, and the vast majority stall with little or no measurable P&L impact. Fortune describes the sample as 150 leader interviews, a 350-employee survey and analysis of 300 public deployments. — [Fortune, 18 Aug 2025](https://fortune.com/2025/08/18/mit-report-95-percent-generative-ai-pilots-at-companies-failing-cfo)
- Dispute about the 95% figure:
  - DX cites 53 structured interviews plus 153 senior-leader survey responses, and says the authors frame it as a "directionally accurate snapshot." — [DX](https://getdx.com/blog/the-ai-divide/)
  - Critics say "failure" was defined narrowly: no quantifiable revenue or cost benefit within 6 months. That is unrealistic for financial institutions on 12-24 month cycles. — [NayaOne](https://nayaone.com/?p=50646)
  - Critics also say it ignores productivity gains and rests on a thin, conference-heavy sample. — [critic mirror](https://neonvagabond.xyz/mirrors/mit-report-lacks-evidence.html)
  - Even critics concede "it captures something many enterprise teams are quietly feeling." — [BigDATAwire](https://www.bigdatawire.com/?p=89626)
  - Range to report: "about 95% show no measurable P&L impact within 6 months" (MIT) versus "methodologically weak; failure definition too narrow" (critics).
- S&P Global / 451 Research (1,006 IT and line-of-business respondents, North America and Europe): the share of companies abandoning most of their AI initiatives rose from 17% in 2024 to 42% in 2025. Secondary summary; primary not retrieved. — [Horwath HTL summary](https://workshop.horwathhtl.com/resources/case-studies/genai-abandonment-landscape)
- Gartner (June 2025 forecast): more than 40% of agentic AI projects will be cancelled by end-2027, due to escalating costs, unclear business value or inadequate risk controls.
  - The supporting January 2025 poll was of webinar attendees. 19% said their organisation had made significant agentic investments.
  - An analyst said most projects are "early-stage experiments or proof of concepts."
  - This is a forecast, not an observed rate.
  - Source: [Outlook Business](https://www.outlookbusiness.com/artificial-intelligence/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-says-gartner); [CDO Magazine](https://www.cdomagazine.tech/aiml/over-40-of-agentic-ai-projects-likely-to-be-abandoned-by-2027-gartner-forecast)
- AI spend sprawl that feeds orphaned tools: Zylo 2026 SaaS Management Index (29 Jan 2026). Vendor claim: Zylo sells SaaS management.
  - Spend on AI-native apps is up 108% year over year overall, and up 393% at organisations with more than 10,000 employees.
  - Use of AI-category apps grew 181%.
  - AI apps arrive "frequently through employee credit cards and expense reports," and ChatGPT is now the most-expensed app.
  - Large enterprises add about 21 apps per month.
  - Source: [Zylo news](https://zylo.com/news/2026-saas-management-index)

#### P3. Staff pasting confidential data into AI tools (shadow AI), plus the new duty to keep an AI inventory
- IBM Cost of a Data Breach 2025:
  - About 1 in 5 organisations reported a breach tied to shadow AI.
  - Organisations with high shadow-AI use paid about $670,000 more per breach. Kiteworks' summary puts this at $4.63M vs $3.96M.
  - Only 37% have policies to manage AI or detect shadow AI.
  - Source: [Kiteworks](https://www.kiteworks.com/cybersecurity-risk-management/ibm-2025-data-breach-report-ai-risks/); [TechRepublic](https://www.techrepublic.com/article/news-ai-breach-risks-rise-as-governance-lags/)
- IBM 2025, continued:
  - 97% of organisations that reported an AI-related breach lacked proper AI access controls. This is a share of AI-breached organisations, not of all organisations.
  - Shadow-AI incidents exposed personal data in 65% of cases and IP in 40%, vs 53% and 33% overall.
  - Source: [Nudge Security](https://www.nudgesecurity.com/post/shadow-ai-the-emerging-security-threat-in-ibms-2025-cost-of-a-data-breach-report); [DBTA](https://www.dbta.com/Editorial/News-Flashes/IBMs-%E2%80%98Cost-of-a-Data-Breach-Report-Signals-Need-for-Greater-Security-and-Governance-for-AI-170893.aspx)
- Harmonic Security, Q2 2025: 1M prompts and 20,000 files across 300 GenAI and AI-enabled SaaS tools. 22% of files (4,400) and 4.37% of prompts (43,700) included sensitive data. Vendor claim. — [Help Net Security](https://www.helpnetsecurity.com/2025/08/05/genai-sensitive-data-exposure/)
- Harmonic Security, Q3 2025 (US and UK, 3M+ prompts and uploads). Vendor claim.
  - 26.4% of file uploads to AI tools held sensitive data.
  - 21.81% of the sensitive data went to tools that train on user inputs.
  - 11.84% of exposures happened through free or personal accounts.
  - 57% of exposed data was business or legal information, and 25% was technical (source code, credentials).
  - Source: [BusinessWire, 13 Nov 2025](https://www.businesswire.com/news/home/20251113987633/en/Over-a-Quarter-26-of-Uploads-to-GenAI-Tools-Contain-Sensitive-Data-an-Increase-of-Over-4-in-Just-Three-Months)
- Earlier baseline (Q4 2024 data): 8.5% of prompts posed potential security risks, and 45.8% of those risked exposing customer data. Vendor claim. — [Campus Technology, Jan 2025](https://campustechnology.com/Articles/2025/01/22/Study-1-in-10-AI-Prompts-Could-Expose-Sensitive-Data.aspx)

#### P4. AI Overviews and AI search cutting website clicks and leads
- Pew Research (July 2025; browsing data from 900 US adults):
  - Users who saw an AI summary clicked a traditional result on 8% of visits, vs 15% without one.
  - Only 1% clicked a link inside the summary.
  - 26% of sessions ended on pages with an AI summary, vs 16% without.
  - About 18% of Google searches produced an AI summary.
  - Google called the methodology "flawed."
  - Source: [Search Engine Roundtable](https://www.seroundtable.com/pew-google-ai-overviews-39808.html); [Sistrix](https://www.sistrix.com/blog/pew-research-ai-overviews-halve-click-through-rates/); Google rebuttal: [MediaPost](https://www.mediapost.com/publications/article/407651/google-hits-back-at-pew-report)
- Seer Interactive (Sept 2025 update; 3,119 terms, 42 client organisations, 25.1M organic impressions, June 2024 to Sept 2025):
  - Organic CTR on informational queries with AI Overviews fell 61% (1.76% to 0.61%).
  - Paid CTR on the same queries fell 68%.
  - Even queries without AI Overviews fell: 1.45%, down 46% YoY per Seer, or 1.62%, down 41% per MediaPost.
  - Seer says it cannot prove that being cited causes higher CTR.
  - Seer is an agency, so this is a vendor claim.
  - Source: [Seer Interactive](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-september-2025-update); [MediaPost](https://www.mediapost.com/publications/article/410452/google-ai-overviews-drive-ctrs-down.html)
- A "53 brands, Jan 2025 to Feb 2026" Seer figure appears only on low-quality secondary sites. Not verified. — [relevantaudience](https://relevantaudience.com/seo/ai-overview-impact-on-organic-search-2026)

#### P5. AI-forged documents and AI impersonation in finance operations (fake receipts and invoices, vendor-change requests, deepfake executive voice or video)
- FBI IC3 2025 Internet Crime Report (April 2026):
  - BEC reported losses were $3.046B from 24,768 complaints, the second-costliest category. BEC was about $2.8B in 2024.
  - More than $30M of BEC losses had a confirmed AI nexus.
  - This is the first year with a dedicated AI-fraud section: 22,364 complaints and about $893M in losses.
  - The FBI says AI-generated executive impersonation and voice cloning are being used to authorize fraudulent transfers.
  - Total reported losses were $20.88B, up 26%.
  - Source: [iTnews](https://www.itnews.com.au/news/ai-assisted-fraud-makes-big-debut-in-fbis-cybercrime-stats-624819); [Enterprise Security Tech](https://www.enterprisesecuritytech.com/post/fbi-cybercrime-report-losses-hit-record-20-88-billion-as-ai-powered-fraud-and-bec-attacks-surge); [Insurance Business](https://www.insurancebusinessmag.com/us/news/cyber/business-email-fraud-drives-bulk-of-us-cybercrime-losses-analysis-590687.aspx)
- AFP 2026 Payments Fraud and Control Survey (April 2026; 465 respondents; covers 2025):
  - "Over 75%" of US firms experienced attempted or actual payments fraud. The search summary also says this was slightly lower than in 2024.
  - 74% were hit by BEC. A separate AFP article says 70% cite BEC as the top avenue; the two measure different things.
  - Only 17% use AI to fight payments fraud. Of those, 45% report better deepfake detection.
  - Checks remain the most-targeted payment method (58%).
  - The full report is $295 for non-members.
  - Source: [AFP press release](https://www.financialprofessionals.org/about/learn-more/press-releases/Details/over-75-percent-of-us-firms-experienced-payments-fraud-in-2025-while-ai-adoption-for-fraud-mitigation-lags); [AFP report page](https://www.financialprofessionals.org/publications-data-tools/reports/survey-research-economic-data/Details/payments-fraud)
- Practitioner quote (AFP article): "One of the things that used to tip you off was a grammatical error or a spelling error," said Ward, meaning LLM-polished phishing removes that tell. The speaker's full name and title were not captured. — [AFP: From BEC to deepfakes](https://www.financialprofessionals.org/training-resources/resources/articles/Details/from-bec-to-deepfakes-payments-fraud-is-only-getting-more-sophisticated)
- AppZen (vendor claim): AI-generated receipts were about 14% of fraudulent documents in September 2025, vs 0% a year earlier (reported by the FT and ICAEW). — [TechRadar](https://www.techradar.com/pro/security/workers-are-scamming-their-employers-using-ai-generated-fake-expense-receipts); [RPG Crouch Chapman (UK)](https://www.rpgcrouchchapman.co.uk/resources/blog/pw-news/ai-receipts-raise-new-risks-for-expense-claims)
- AppZen (vendor claim), later data:
  - The AI share of fake-receipt flags rose from 0% (March 2025) to 70.8% (mid-May 2026).
  - Sample: 1,471 AI fakes from 745 employees at 174 companies, totalling $148,143.
  - This is the make-up of detected fraud, not a fraud rate.
  - AI fakes average about $100 each, vs $182 for template fakes.
  - Source: [Accounting Today](https://www.accountingtoday.com/news/use-of-ai-receipts-in-expense-fraud-soars); [Ohio CPA, 26 Jun 2026](https://ohiocpa.com/for-the-public/news/2026/06/26/use-of-ai-generated-receipts-in-expense-fraud-soars); [PYMNTS](https://www.pymnts.com/?p=3892615)
- Estimate from the AppZen sample: $148,143 / 174 companies is about $851 per company over about 14 months. So employee receipt fraud is small per company. The big money is BEC and vendor-payment fraud.

#### P6. AI-faked damage photos and refund claims in e-commerce
- Modern Retail (2 March 2026):
  - A $489 Boll & Branch sheet return came with photos of "tearing" that did not match how cotton frays. One image carried an AI watermark.
  - Bogg Bag is seeing AI-generated photos in its customer-service queue.
  - Retailers say fakes are not new (lifted review photos, Photoshop). What changed is that AI makes them faster and easier.
  - Source: [Modern Retail](https://www.modernretail.co/technology/from-boll-branch-to-bogg-brands-are-battling-a-surge-of-ai-driven-return-fraud/)
- Forter (vendor claim): AI-made damage claims are the fastest-growing form of return abuse. Fraud rings offer "returns-as-a-service" for a cut. UK coverage, June 2026. — [Retail Gazette](https://www.retailgazette.co.uk/blog/2026/06/retailers-face-surge-in-ai-generated-fake-damage-claims-and-refund-scams/)
- Hardest case: a real photo of a real item with damage added defeats whole-image detection. Suggested controls:
  - controlled in-app capture
  - binding the photo to the transaction
  - server-side timestamps
  - human-review thresholds by claim value
  - Vendor or agency claim. Source: [Switch Labs](https://www.switchlabs.dev/post/ai-faked-damage-photos-playbook)
- Scale (not AI-specific): NRF and Happy Returns put US 2025 returns at about $849.9B, with about 9% fraudulent.
  - Estimate: 9% x $849.9B is about $76B in fraudulent or abusive returns from all causes.
  - Ravelin 2026: 1 in 3 refund abusers use or are considering AI (vendor claim).
  - Pindrop: 3 in 10 retail fraud attempts are AI-generated (vendor claim).
  - Source: [Practical Ecommerce](https://practicalecommerce.com/ai-makes-refund-evidence-easier-to-fake); [eCommerce Fastlane](https://ecommercefastlane.com/ai-generated-fakes-shopify-merchants-2026/)
- China: Taobao and Tmall deployed AI against refund-only claims that used AI-generated defect photos, after a state broadcaster exposé (Jan 2026). — [OECD AI incident](https://oecd.ai/en/incidents/2026-01-21-2ae9)

#### P7. Fake candidates and floods of AI-written applications (including North Korean IT-worker schemes)
- Gartner (31 July 2025):
  - Predicts 1 in 4 candidate profiles worldwide will be fake by 2028. This is a forecast.
  - In a Q2 2025 survey of about 3,000 candidates, 6% admitted interview fraud (posing as someone else, or using a stand-in).
  - Only half of candidates trusted that the jobs they applied for were real.
  - Source: [Gartner press release](https://www.gartner.com/en/newsroom/press-releases/2025-07-31-gartner-survey-shows-just-26-percent-of-job-applicants-trust-ai-will-fairly-evaluate-them); [Personnel Today](https://www.personneltoday.com/hr/by-2028-one-in-four-candidate-profiles-will-be-fake)
- Gartner 2024 survey, cited by Greenhouse (a vendor): 54% of recruiting leaders agreed AI had made candidate fraud significantly larger, and only 7% used ID-document validation. — [Greenhouse guidance](https://www.greenhouse.com/guidance/mitigate-rising-candidate-fraud-through-identity-verification)
- DOJ (2026 coordinated action, "Operation Lonestar Roundup"):
  - More than 70 US companies were affected.
  - 14 people indicted, 2 arrested, about 187 devices seized from Texas laptop farms, in a $3M scheme.
  - Victims included healthcare, communications, cyber support, retail and manufacturing.
  - Source: [DOJ](https://justice.gov/opa/pr/justice-department-announces-coordinated-actions-combat-north-korean-remote-it-worker); [Staffing Industry Analysts, 14 Oct 2026](https://www.staffingindustry.com/news/global-daily-news/14-indicted-in-3-million-north-korean-it-scheme-doj-says)
- An earlier DOJ sweep (date not confirmed): searches of 29 laptop farms in 16 states, 29 financial accounts and 21 fake websites seized, and actors employed at more than 100 US companies. — [MeriTalk](https://meritalk.com/?p=199230)
- Greenhouse 2025 AI in Hiring Report surveyed 4,100+ job seekers, recruiters and hiring managers in the US, UK, Ireland and Germany. — [HR Tech Edge](https://hrtechedge.com/greenhouse-report-exposes-a-hiring-system-in-crisis-ai-hacks-fraud-fears-ghost-jobs-and-collapsing-trust)

#### P8. Hallucinated content in client-facing professional work (legal filings, consulting reports)
- Damien Charlotin's database (crowd-sourced):
  - About 1,600 cases from 35 countries, 1,116 of them from the US (AFP news agency, June 2026).
  - Hallucinations in filings rose eightfold year over year.
  - Source: [The Star / AFP, 15 Jun 2026](https://www.thestar.com.my/tech/tech-news/2026/06/15/courts-cracking-down-on-error-strewn-ai-assisted-legal-briefs)
- MSBA (27 July 2026):
  - 1,240 US instances in total.
  - 2026 to date: 668 instances, with 58 monetary sanctions and 21 disciplinary referrals.
  - In 2026, lawyers account for 256 instances and pro se litigants for 405.
  - Source: [MSBA](https://www.msba.org/site/content/News-and-Publications/News/General-News/Confronting_the_Hard%20Numbers_Behind_Lawyers_AI_and_Phantom_Precedents.aspx)
- A UNC library post (June 2026) gives a different split: about 60% pro se and 40% attorney, across 1,058 US cases. — [UNC Law Library](https://library.law.unc.edu/?p=3055)
- US courts imposed more than $145,000 in AI-hallucination sanctions in Q1 2026, including a record $110,000 Oregon penalty. Secondary blog; treat with caution. — [Compliance Hub](https://compliancehub.wiki/legal-ai-hallucination-reckoning-2026/)
- Australia: Deloitte agreed to refund the final instalment of an A$440,000 contract with the Department of Employment and Workplace Relations (DEWR) (Oct 2025).
  - The report had fabricated references and a fabricated quote from a court judgment. It used an Azure OpenAI GPT-4o toolchain.
  - Senator Barbara Pocock argued for a full refund.
  - Source: [The Register, 6 Oct 2025](https://www.theregister.com/2025/10/06/deloitte_ai_report_australia/)

#### Candidates tested and rejected or kept as secondary
- **AI crawlers and bots running up hosting bills**
  - Read the Docs (2024): one crawler pulled 73 TB in May 2024. "This cost us over $5,000 in bandwidth charges, and we had to block the crawler." — [Boing Boing (2024)](https://boingboing.net/2024/07/29/ai-crawlers-run-up-a-websites-hosting-bill.html)
  - Clutch (Nov 2025): 42% of small businesses report performance or bandwidth strain from bots. — [Clutch](https://clutch.co/resources/bot-traffic-rise-manage-bandwidth-strain)
  - Imperva: 51% of 2024 web traffic was bots. — [Clutch](https://clutch.co/resources/bot-traffic-rise-manage-bandwidth-strain)
  - Cloudflare: AI bot traffic rose 757% in 2024 (secondary). — [WebProNews](https://www.webpronews.com/the-machines-are-hungry-ai-crawlers-now-account-for-nearly-half-of-all-internet-traffic-and-the-web-is-buckling/)
  - Blocking is hard because new crawlers keep appearing. — [Sherwood](https://sherwood.news/tech/ai-companies-content-crawlers-are-saddling-website-owners-with-unexpected)
- **AI customer-service bots that need human rescue**
  - Gartner (10 June 2025) predicts that by 2027, 50% of organisations that planned big customer-service headcount cuts will abandon those plans.
  - Gartner's poll of 163 service leaders (March 2025): 95% plan to keep human agents.
  - Analyst Brian Weber: an agentless contact centre is "not yet technically feasible, nor is it operationally desirable."
  - 62% of consumers fear AI will make it harder to reach a human.
  - Source: [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-10-gartner-predicts-50-percent-of-organizations-will-abandon-plans-to-reduce-customer-service-workforce-due-to-ai); [The Register](https://www.theregister.com/2025/06/11/gartner_ai_customer_service/)
- **Fake-review extortion on Google Business Profiles**
  - Scammers post a burst of fake 1-star reviews (15+ in 24 hours), then demand crypto or gift cards to remove them.
  - Cases: a Tennessee wedding photographer (Jan 2026) and an Arizona roofer (March 2026).
  - Google reportedly removed 221M fake reviews in 2025 (secondary).
  - Fake Review Watch tracked 150+ targeted businesses.
  - The AI link is mostly implicit in these sources. They describe scale and automation, not confirmed AI generation.
  - Source: [Washington Times, 16 Jan 2026](https://m.washingtontimes.com/news/2026/jan/16/living-dying-review-online-extortionists-flood-businesses-fake/); [WSMV, 18 Jan 2026](https://www.wsmv.com/2026/01/18/overseas-criminals-hijack-google-reviews-middle-tennessee-business); [NRCA, Mar 2026](https://nrca.net/RoofingNews/Fake%20Google%20reviews%20are%20a%20common%20scam%20affecting%20small-business%20owners.9-03-2026.13486/Details/Story); [Digitaleer](https://www.digitaleer.com/fake-review-extortion-how-to-fight-back)

### Inferences
- The strongest neutral-source evidence is fraud (FBI IC3, AFP), AI search clicks (Pew, plus Seer as an agency) and legal hallucinations (court-record database).
- The weakest is vibe-code security and shadow AI, where nearly every number is a vendor scan.
- "Failed pilots" has big headline numbers but disputed methodology. The S&P 17% to 42% abandonment jump is the cleanest number; the MIT 95% is the most quoted and most contested.
- Several "AI-created" problems are really AI making an old problem cheaper to commit: receipts, refunds, BEC, reviews, candidate impersonation. That is good for staying power, because the attacker's cost keeps falling.

### Gaps
- No primary pages could be opened, so every number is from search snippets or summaries (see the top note).
- Not researched because the search budget ran out:
  - Ahrefs and Similarweb zero-click studies
  - McKinsey State of AI 2025, Menlo Ventures, BCG
  - Cyberhaven and Menlo Security shadow-AI data
  - Verizon DBIR 2025
  - FinCEN deepfake alert
  - Sumsub and Experian fraud reports
  - LinkedIn application-volume data
  - Upwork and Fiverr "fix my Lovable app" gig counts
  - Reddit and owner-forum quotes
- I did not find the S&P Global primary report. The 42% figure is from a secondary summary.

---

## Key Question 2: For each problem, who feels it, who pays, how often, what it costs, how it is handled today, who sells fixes, and the six-test verdict

### Takeaway
Eight problems survive as plausible monthly-retainer services.
- Ranked top: finance-ops AI-forgery control and e-commerce AI-faked claims review. Both have high pain and daily volume, AI-plus-human fits them well, and their fixes are either enterprise-priced or not bundled for mid-market buyers.
- Partly undercut by bundled features: shadow-AI governance (Microsoft Purview), candidate fraud (Greenhouse plus CLEAR) and legal citation checks (Westlaw/Lexis).
- Real but very crowded: AI search visibility (GEO).

### Cited Findings (per-problem records)

#### P1. Vibe-coded app "care plan": security, maintenance and change requests for AI-built apps
- **One line:** Founders and SMBs ship apps and automations built with Lovable, Replit, Bolt or Base44. The apps leak data and break in production, and the owners cannot maintain them.
- **Industry:** Cross-industry. Non-technical founders, SMB internal tools, agencies.
- **Size where it hurts most:** 1 to 50 employees; pre-seed and seed startups; ops teams at mid-market firms building internal tools.
- **Task in plain words:**
  - Weekly: security scans (access rules, exposed keys, auth), bug fixes, small feature changes, and dependency and platform updates.
  - Monthly: an "is my data safe" report.
- **Who feels it / who approves:** Founder, CEO or ops lead / the same person (founder approves).
- **Frequency and hours:**
  - 28% of developers lose most of AI's time savings to fixing AI code. — [Fastly](https://www.fastly.com/blog/senior-developers-ship-more-ai-code)
  - Weekly frequency for live apps is an inference. I found no hours-per-week survey for non-technical owners.
- **Dollar cost:**
  - Market bands (pricing guide, vendor-adjacent): marketplace fixes $25 to $500; freelance specialists $200 to $400/hr; fixed-scope rescues about $1,000 to $15,000; agency rebuilds $25k to $50k. — [vibecoding.app](https://vibecoding.app/blog/vibe-coding-cleanup-cost)
  - The average completed Upwork vibe-code cleanup invoice is about $7,200 (vendor-blog claim; Upwork not reached). — [vibecoding.app](https://vibecoding.app/blog/vibe-coding-cleanup-cost); [Scope Nine](https://scopenine.com/vibe-code-cleanup-cost)
  - The downside risk is a data breach (see P3 for IBM breach costs).
- **How it's handled today / what they pay:** The founder re-prompts the AI, hires Upwork or Fiverr freelancers, or buys a fixed-fee rescue. Examples:
  - Valletta: $199 audit. — [Valletta](https://vallettasoftware.com/vibe-coding-cleanup)
  - Techpotions: $297 two-day triage, then $2,497 two-week stabilisation. — [Techpotions](https://techpotions.com/solutions/vibe-coding-cleanup)
  - Afterbuild Labs: $49 audit, $1,999 production pass. — [Afterbuild](https://afterbuildlabs.com/solutions/clean-up-ai-generated-code)
  - Triple Minds: from $4K. — [Triple Minds](https://tripleminds.co/ai/vibe-coding-cleanup-services/)
  - Offshore specialists from $15/hr. — [Suffescom](https://www.suffescom.com/remote-developers/vibe-coding-cleanup-specialist)
  - Stabilisation often costs $2,500 to $7,500. — [Zlatko Marjanovic](https://zlatkomarjanovic.com/blog/how-to-hire-a-developer-to-fix-your-lovable-app)
- **Who sells a fix / crowding:** Many small agencies plus marketplace freelancers, and app-security scanners (Escape, Astra). The market is crowded at the cheap one-off end. I found few productised monthly "care plans."
- **(f) check:**
  - Free or cheap scanners cover only configuration-level issues: Supabase Security Advisor, GitHub Dependabot, Lovable's built-in security scan. **[prior knowledge, not re-verified, no URL]**
  - Escape and Tenzai show the biggest problems are business-logic and access-control flaws, which scanners miss. — [The Next Web](https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed)
  - Verdict: passes, marginally.
- **Grow or shrink (24 months):**
  - Shrinks: platforms add safer defaults and built-in scans, and models write better auth code.
  - Grows: the installed base keeps growing (Lovable unicorn, 2.3M users), and Tenzai found weak access-control logic even in top tools. Apps that gain users need integrations, payments and compliance, which AI platforms don't handle.
  - Net: one-off rescues shrink; ongoing care grows.
- **How to reach buyers:** Lovable, Replit, Bolt and Supabase communities and Discords; r/lovable and r/vibecoding (not checked); Indie Hackers; Product Hunt launches; platform partner or expert directories (unverified); no-code agency networks.
- **Rough US count:** Not found. Lovable's 2.3M users are individuals, not businesses.
- **Strongest argument against:** Buyers are small and price-sensitive, offshore rivals charge $15/hr, the work is lumpy, and the platforms will absorb the easy fixes. Many of these apps die before they need a retainer.
- **Six tests:**
  - a: likely (inference)
  - b: yes
  - c: yes
  - d: yes
  - e: yes
  - f: marginal pass
  - **6/6 (f marginal; a inferred)**

#### P2. Orphaned AI pilots, agents and automations: an "AI run-and-improve" retainer
- **One line:** Companies bought or built AI pilots, copilots and agents that stall, drift or get abandoned because nobody owns evaluation, upkeep or adoption. Meanwhile AI tool spend balloons.
- **Industry:** Cross-industry. Financial services, insurance, healthcare administration, manufacturing, professional services.
- **Size:** Mid-market (200 to 5,000 employees) and divisions of enterprises.
- **Task in plain words:**
  - Weekly: check each live AI workflow's accuracy against test cases, fix prompts and integrations, retire unused tools, and track AI licences and spend.
  - Monthly: report value delivered.
- **Who feels it / who approves:** VP Ops, Head of AI or Transformation, CIO / CFO or COO. It is often unclear who owns an orphaned pilot.
- **Frequency:** Weekly upkeep is an inference. There is no source on hours per week.
- **Dollar cost:**
  - 42% of companies abandoned most AI initiatives in 2025, up from 17% in 2024. — [S&P via Horwath HTL](https://workshop.horwathhtl.com/resources/case-studies/genai-abandonment-landscape)
  - Gartner cites "escalating costs, unclear business value" as the reasons agentic projects get cancelled. — [Outlook Business](https://www.outlookbusiness.com/artificial-intelligence/over-40-of-agentic-ai-projects-will-be-scrapped-by-2027-says-gartner)
  - AI-native app spend is up 108% YoY, and up 393% at 10k+ employee firms. — [Zylo](https://zylo.com/news/2026-saas-management-index)
  - No sourced dollar figure per failed pilot was found.
- **How it's handled today:** Internal IT; big consultancies; vendor-supplied engineers; SaaS management tools for spend (Zylo is a vendor). Prices not found.
- **Who sells a fix / crowding:**
  - Consultancies (Accenture, Deloitte and others) and boutique "AI implementation" agencies are crowded at the build stage.
  - Ongoing "run" services are less crowded. This is an inference.
- **(f) check:** LLM observability tools (Langfuse open source, LangSmith) are cheap. **[prior knowledge, not re-verified, no URL]** They monitor; they don't own outcomes. Verdict: passes.
- **Grow or shrink:**
  - Grows: more agents in production; Gartner expects many to be cancelled, which is the market for rescue. AI spend is rising fast.
  - Shrinks: model vendors ship turnkey agents with built-in evaluations, and enterprise platforms (Microsoft, Salesforce, ServiceNow) bundle agent management.
- **How to reach buyers:** CIO, COO and CFO peer groups (Gartner, Evanta), mid-market ERP and CRM partner ecosystems, AI-vendor partner programmes, industry associations (insurance, healthcare administration).
- **Rough US count:** Not found.
- **Strongest argument against:** "Orphaned" means no budget owner, so selling a retainer to nobody is hard. Consultancies and platform vendors already own the relationship. The disputed MIT figure may overstate the failure rate.
- **Six tests:**
  - a: inferred
  - b: yes
  - c: yes
  - d: weak (no clear owner)
  - e: yes
  - f: pass
  - **5/6 (d weak)**

#### P3. Shadow-AI data leakage and AI-use inventory for regulated SMBs
- **One line:** Staff paste client, patient or financial data and source code into personal AI accounts, and owners can't say which AI tools are in use.
- **Industry:** Healthcare practices, law and accounting firms, financial advisers, SaaS, manufacturing (IP).
- **Size:** 20 to 1,000 employees, without a full security team.
- **Task in plain words:**
  - Weekly: review flagged prompts and uploads, keep a live inventory of AI tools and accounts, move staff to approved tools, and update the policy.
  - Monthly: a board or insurer report.
- **Who feels it / who approves:** IT director, compliance officer or MSP; in small firms the managing partner or practice owner / CFO or managing partner.
- **Frequency:** Daily. Harmonic saw sensitive data in 4.37% of 1M prompts and 22% of 20k files in one quarter. — [Help Net Security](https://www.helpnetsecurity.com/2025/08/05/genai-sensitive-data-exposure/)
- **Dollar cost:**
  - $670,000 extra per breach for organisations with high shadow-AI use, and 1 in 5 organisations had a shadow-AI breach. — [Kiteworks](https://www.kiteworks.com/cybersecurity-risk-management/ibm-2025-data-breach-report-ai-risks/)
  - Note: IBM's sample skews large, and the SMB-level dollar cost is not quantified.
- **How it's handled today:** Firewall blocks on ChatGPT, written policies, MSP add-ons, and enterprise DLP or SASE (Netskope, Zscaler). Only 37% of organisations have policies. — [TechRepublic](https://www.techrepublic.com/article/news-ai-breach-risks-rise-as-governance-lags/)
- **Who sells / crowding:** Harmonic, Cyberhaven, Nightfall, Nudge Security, Kiteworks and SASE vendors. Very crowded on software. Prices not found this session (gap).
- **(f) check:**
  - Microsoft Purview "DSPM for AI" is bundled in Microsoft 365 E5 / E5 Compliance, and Google Workspace has DLP. **[prior knowledge, not re-verified, no URL]**
  - Most SMBs are on lower Microsoft tiers, so coverage is partial.
  - Verdict: partial fail for E5 shops.
- **Grow or shrink:**
  - Grows: AI is embedded inside every SaaS tool (Harmonic tracks 300), and AI apps arrive on expense cards. — [Zylo](https://zylo.com/news/2026-saas-management-index)
  - Shrinks: enterprise AI plans with no-training defaults, and Microsoft and Google bundling.
  - Overlaps the "new rules" lens (AI inventories under the EU AI Act, state laws, ISO 42001).
- **How to reach buyers:** MSP channels (CompTIA, ConnectWise and Kaseya communities), state bar associations, AICPA/CPA societies, MGMA (medical practices), ISACA, IAPP, cyber-insurance brokers.
- **Rough US count:** Not found.
- **Strongest argument against:** This is a feature, not a service. Microsoft, Google and MSPs will bundle it. Most of the dollar evidence is enterprise breach cost, not SMB.
- **Six tests:**
  - a: yes
  - b: yes (enterprise evidence)
  - c: yes
  - d: yes
  - e: yes
  - f: partial
  - **5/6 (f partial: Purview in M365 E5)**

#### P4. AI search eating clicks and leads (AI visibility, GEO/AEO)
- **One line:** Google AI Overviews, AI Mode and ChatGPT answer the question, so fewer people click through to the site and inbound leads fall.
- **Industry:** B2B SaaS, professional services, e-commerce, local services, publishers.
- **Size:** SMB to mid-market with content-driven lead generation.
- **Task in plain words:**
  - Weekly: track whether the brand is named in AI answers for key buyer questions, fix the pages, FAQs and schema that AI cites, and win mentions on the third-party sites AI cites (reviews, Reddit, directories).
  - Monthly: a share-of-answer report.
- **Who feels it / who approves:** Head of Marketing or Growth, SEO lead, or the owner / CMO or CEO.
- **Frequency:** Continuous. The AI-summary click rate is 8% vs 15% without a summary. — [Search Engine Roundtable](https://www.seroundtable.com/pew-google-ai-overviews-39808.html)
- **Dollar cost:**
  - Organic CTR on queries with AI Overviews fell 61%, and paid CTR fell 68%, which also hurts ad ROI. — [Seer](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-september-2025-update)
  - Lost-lead dollars per firm: not found.
- **How it's handled today / what they pay:**
  - GEO agency services cost $1,500 to $50,000 a month. — [Nutshell](https://www.nutshell.com/blog/geo-costs)
  - GEO audits cost $1,500 to $3,500. — [Over The Top SEO](https://www.overthetopseo.com/?p=60191)
  - Traditional SEO retainers cost $1,000 to $2,500 a month (Backlinko, Dec 2025, cited by an agency). — [Derivatex](https://derivatex.agency/blog/cheap-geo-agency-hidden-costs/)
- **Who sells / crowding:** Very crowded. Tools:
  - Otterly: $29 / $189 / $489 a month. — [upGrowth](https://upgrowth.in/ai-visibility-pricing-india/)
  - Profound: "from $99" for one engine. — [Piabo comparison](https://munich2026.piabo.net/comparisons/geo-platforms-compared). Note: this may conflict with Profound's higher published tiers; verify.
  - Peec: about $95 to $495, or from €70. — [Pepper](https://www.pepper.inc/blog/geo-platform-pricing-guide-2026/)
  - Ahrefs Brand Radar and Semrush AI Visibility: about $139 to $199. — [Muddy River News](https://muddyrivernews.com/business/5-best-geo-ai-visibility-tools-for-seo-agencies-with-flexible-pricing-2026/20260417074744/)
  - HubSpot also has AEO features. — [Piabo](https://munich2026.piabo.net/comparisons/geo-platforms-compared)
  - Every SEO agency now sells GEO.
- **(f) check:**
  - Monitoring is solved under $100 a month (Otterly Lite at $29).
  - The fix (content, PR, citations) is labour. — [Pepper](https://www.pepper.inc/blog/geo-platform-pricing-guide-2026/)
  - Verdict: pass for the fix, fail for measurement alone.
- **Grow or shrink:**
  - Grows: AI search share keeps rising, and clicks fall even on queries without AI Overviews.
  - Shrinks: GEO merges back into SEO, Google may change its click policy, and tactics are unstable. Seer itself cannot prove that being cited causes clicks.
- **How to reach buyers:** Search Engine Land and Roundtable audiences, SMX and BrightonSEO (UK), MozCon, HubSpot Solutions Partners, B2B SaaS marketing communities, local-business associations.
- **Rough US count:** Not found.
- **Strongest argument against:** The most crowded of the eight. ROI attribution is murky. Incumbent SEO agencies already own the client.
- **Six tests:**
  - a: yes
  - b: yes
  - c: yes
  - d: yes
  - e: yes
  - f: pass for the fix
  - **6/6 (monitoring alone fails f: Otterly $29/mo)**

#### P5. AI-forged documents and impersonation in finance ops: an outsourced "payment-control desk"
- **One line:** AI makes fake receipts, invoices, vendor bank-change letters and executive voice or video cheap and convincing. AP and expense teams can no longer trust what they see or hear.
- **Industry:** Cross-industry. Construction, logistics, healthcare, nonprofits, education and manufacturing all run big AP flows.
- **Size:** Mid-market, 100 to 5,000 employees, with a 2 to 15 person AP or finance team. Small firms with no segregation of duties are also exposed.
- **Task in plain words:**
  - Daily or weekly: independently verify every vendor bank-detail change by callback, run AI forensics on invoices and receipts, screen urgent "CEO" payment requests, and keep a vendor master file of verified contacts.
  - Monthly: a control report for the auditor or insurer.
- **Who feels it / who approves:** AP manager, controller, T&E manager / CFO or controller.
- **Frequency:**
  - 74% of organisations saw BEC in 2025. — [AFP](https://www.financialprofessionals.org/about/learn-more/press-releases/Details/over-75-percent-of-us-firms-experienced-payments-fraud-in-2025-while-ai-adoption-for-fraud-mitigation-lags)
  - Vendor changes and expense reports flow weekly (inference).
- **Dollar cost:**
  - BEC: $3.046B reported US losses in 2025. AI-nexus BEC: more than $30M. AI-fraud section: about $893M. — [iTnews](https://www.itnews.com.au/news/ai-assisted-fraud-makes-big-debut-in-fbis-cybercrime-stats-624819)
  - AI receipts average about $100 each; about $851 per company in AppZen's sample (estimate above). — [Accounting Today](https://www.accountingtoday.com/news/use-of-ai-receipts-in-expense-fraud-soars)
- **How it's handled today:** Manual callbacks by AP staff, bank positive pay, and AI tools at a minority of firms (only 17% use AI against payments fraud). — [AFP](https://www.financialprofessionals.org/about/learn-more/press-releases/Details/over-75-percent-of-us-firms-experienced-payments-fraud-in-2025-while-ai-adoption-for-fraud-mitigation-lags)
- **Who sells / crowding:**
  - AppZen (enterprise audit). Prices not found.
  - Vendor-verification tools (e.g. Trustpair, Eftsure in Australia), AP automation suites, and bank treasury services. **[prior knowledge, not re-verified, no URL; prices not found]**
  - Moderately crowded on software; thin on done-for-you service.
- **(f) check:**
  - Spend platforms such as Ramp and Expensify reportedly added AI-receipt detection in 2025 at no extra cost. **[prior knowledge, not re-verified, no URL]**
  - So expense-receipt detection alone likely fails f for firms on those platforms.
  - Vendor-payment verification and deepfake-call protocols are not bundled.
  - Verdict: partial.
- **Grow or shrink:**
  - Grows strongly: image and voice generation keeps improving, the AI share of detected fake receipts went from 0% to 70.8% in about 14 months, and the FBI now tracks AI fraud separately.
  - Shrinks: detection gets bundled into spend and AP platforms, content-provenance metadata spreads, and e-invoicing mandates make invoices verifiable (overlaps the paperwork and new-rules lenses).
- **How to reach buyers:** AFP, IOFM (AP professionals), ACFE, IMA, CFO peer groups; partner channels such as NetSuite, Sage Intacct, Bill.com and QuickBooks ProAdvisors; commercial-crime and cyber insurers; regional banks' treasury teams. UK: ICAEW. Australia: CPA Australia and Eftsure's audience.
- **Rough US count:** Not found. AFP says more than 75% of respondent organisations are affected, but there is no base count.
- **Strongest argument against:**
  - Banks and AP platforms will bundle controls.
  - A service firm that verifies payments takes on liability if fraud slips through.
  - Receipt fraud is small per firm (about $851 per company in the AppZen sample). The big losses (BEC) are spiky rather than steady, so the buyer may prefer insurance and software.
- **Six tests:**
  - a: yes
  - b: yes
  - c: yes
  - d: yes
  - e: yes
  - f: partial
  - **5/6 (f fails for receipt detection on Ramp/Expensify; passes for vendor-payment verification)**
- **Halal note:** Avoid taking lenders' synthetic-identity or credit-fraud work if the client is an interest-based lender (possible Shariah issue; no ruling given).

#### P6. AI-faked damage photos and refund claims: an outsourced "claims-evidence review desk" for e-commerce
- **One line:** Customers and fraud rings submit AI-generated or AI-edited "damage" photos to get refunds without returning goods.
- **Industry:** DTC e-commerce and retail (home goods, apparel, accessories), marketplaces and food delivery. Adjacent: property-damage, rental and insurance claims.
- **Size:** Brands with $5M to $500M GMV and customer-service teams of 5 to 100. Enterprises buy Forter-type tools.
- **Task in plain words:**
  - Daily: check every photo or video claim above a value threshold for AI generation or editing, metadata, duplicate images and reuse across accounts, and for repeat-abuser links. Approve, deny or request in-app live capture.
  - Monthly: a report on abuse rings and policy changes.
- **Who feels it / who approves:** CX/CS manager, ops manager, returns lead / COO, founder or CFO.
- **Frequency:** Daily. Bogg Bag sees AI photos in its customer-service queue. — [Modern Retail](https://www.modernretail.co/technology/from-boll-branch-to-bogg-brands-are-battling-a-surge-of-ai-driven-return-fraud/)
- **Dollar cost:**
  - Single claims run to hundreds of dollars ($489 sheet set). — [Modern Retail](https://www.modernretail.co/technology/from-boll-branch-to-bogg-brands-are-battling-a-surge-of-ai-driven-return-fraud/)
  - About $76B in US fraudulent returns from all causes (estimate: 9% x $849.9B). — [Practical Ecommerce](https://practicalecommerce.com/ai-makes-refund-evidence-easier-to-fake)
- **How it's handled today:** Customer-service agents eyeball photos; brands require returns or video; enterprise fraud vendors (Forter, plus Ravelin and Pindrop data cited) for large brands. Prices not found (gap).
- **Who sells / crowding:** Enterprise fraud vendors (Forter, Signifyd, Riskified, Ravelin) moving into returns abuse; small agency and tool startups (Switch Labs). Moderately crowded at the enterprise level; the mid-market service gap is an inference.
- **(f) check:** No sub-$100 tool for claim-photo forensics was found. Shopify's free fraud analysis covers orders, not damage claims **[prior knowledge, not re-verified, no URL]**. Verdict: likely pass (unverified).
- **Grow or shrink:**
  - Grows: inpainting real photos defeats whole-image detectors — [Switch Labs](https://www.switchlabs.dev/post/ai-faked-damage-photos-playbook). "Returns-as-a-service" rings are spreading — [Retail Gazette](https://www.retailgazette.co.uk/blog/2026/06/retailers-face-surge-in-ai-generated-fake-damage-claims-and-refund-scams/).
  - Shrinks: brands move to controlled in-app capture with server timestamps, platforms like Taobao and Tmall build detection in-house, and enterprise vendors push down-market.
- **How to reach buyers:** Shopify Plus agency and partner network; returns-platform partners (Loop, Happy Returns, ReturnGO); helpdesk app stores (Gorgias, Zendesk); eTail, Shoptalk and NRF events; DTC newsletters and communities; IMRG (UK).
- **Rough US count:** Not found.
- **Strongest argument against:**
  - The value per claim is low, so many brands will just eat the loss or require returns.
  - Enterprise fraud vendors can bundle photo forensics.
  - Being wrong (denying real customers) costs customers, so the risk is two-sided.
- **Six tests:**
  - a: yes
  - b: yes
  - c: yes
  - d: yes
  - e: yes
  - f: likely pass
  - **6/6 (f unverified)**

#### P7. Fake and AI-flooded job candidates: a "candidate verification desk"
- **One line:** AI-written applications, deepfaked interviews, stand-in interviewees and North Korean IT-worker schemes flood remote-role hiring.
- **Industry:** Tech and IT services, staffing agencies and RPOs, remote customer-support, healthcare administration and finance roles. Victims in DOJ cases include healthcare, communications, retail and manufacturing.
- **Size:** 50 to 5,000 employees hiring remote roles; staffing firms.
- **Task in plain words:**
  - Daily: screen inbound applicants for fake identity signals, check identity and location before interviews, flag deepfake or proxy interviews, and verify references.
  - Before the start date: check device shipping address and payroll details (the laptop-farm signals).
- **Who feels it / who approves:** Recruiter, TA manager, hiring manager, CISO / Head of TA, CHRO or CFO.
- **Frequency:** Daily. 6% of candidates admit interview fraud. — [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-07-31-gartner-survey-shows-just-26-percent-of-job-applicants-trust-ai-will-fairly-evaluate-them)
- **Dollar cost:**
  - DOJ case: a $3M scheme across 70+ companies. — [SIA](https://www.staffingindustry.com/news/global-daily-news/14-indicted-in-3-million-north-korean-it-scheme-doj-says)
  - Gartner says the cybersecurity risk can exceed the cost of a bad hire (paraphrase of Jamie Kohn). — [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-07-31-gartner-survey-shows-just-26-percent-of-job-applicants-trust-ai-will-fairly-evaluate-them)
  - Recruiter hours lost: not quantified here (gap).
- **How it's handled today:** Manual screening, in-person final rounds, background checks. Only 7% used ID-document validation (Gartner 2024, via Greenhouse). — [Greenhouse](https://www.greenhouse.com/guidance/mitigate-rising-candidate-fraud-through-identity-verification)
- **Who sells / crowding:**
  - Greenhouse plus CLEAR selfie and ID verification inside Greenhouse Real Talent (since June 2025). — [Greenhouse newsroom](https://greenhouse.com/newsroom/greenhouse-and-clear-announce-partnership-to-enable-candidate-verification)
  - Other ID and deepfake-interview tools exist; prices not found (gap).
  - Crowding is rising.
- **(f) check:** The main ATS (Greenhouse) bundles ID verification. Verdict: partial fail for Greenhouse customers. Other ATSs and staffing agencies are not covered by this source.
- **Grow or shrink:**
  - Grows: Gartner forecasts 1 in 4 fake profiles by 2028, and deepfake video keeps improving.
  - Shrinks: ATS and LinkedIn identity verification become standard, and in-person steps return.
- **How to reach buyers:** SHRM, ERE and RecruitCon, RecFest (UK), the American Staffing Association and SIA, ATS partner marketplaces (Greenhouse, Ashby, Lever), CISO communities for the North Korea angle.
- **Rough US count:** The DOJ floor is 100+ companies employing North Korean workers (earlier sweep) and 70+ in the 2026 action. — [MeriTalk](https://meritalk.com/?p=199230)
- **Strongest argument against:**
  - ATS and background-check incumbents are bundling verification.
  - Discrimination and privacy liability (EEOC; biometric laws such as Illinois BIPA).
  - Hiring slowdowns cut volume.
- **Six tests:**
  - a: yes
  - b: yes
  - c: yes
  - d: yes
  - e: yes
  - f: partial
  - **5/6 (f partial: Greenhouse + CLEAR bundled)**

#### P8. Independent QA for AI-assisted client deliverables (citations, facts, quotes)
- **One line:** Lawyers, consultants and advisers ship AI-drafted work with fabricated citations, quotes or facts, leading to sanctions, refunds and reputational damage.
- **Industry:** Small and mid-size law firms, consultancies, government contractors, research and policy firms. US, UK and Australia.
- **Size:** Solo practitioners to 50-lawyer firms; consultancies of 10 to 500.
- **Task in plain words:** Before filing or sending: check that every citation, quote and statistic exists and says what the document claims, and produce a verification log.
- **Who feels it / who approves:** Litigation associate, paralegal, engagement manager / managing partner or practice leader. Malpractice insurers have an interest.
- **Frequency:**
  - Estimate: 668 US instances in 2026 through late July, about 29.5 weeks, is about 23 per week. Lawyers account for about 9 a week (256 / 29.5).
  - Only the caught cases are counted. — [MSBA](https://www.msba.org/site/content/News-and-Publications/News/General-News/Confronting_the_Hard%20Numbers_Behind_Lawyers_AI_and_Phantom_Precedents.aspx)
- **Dollar cost:**
  - More than $145k in sanctions in Q1 2026, with a $110k record (secondary). — [Compliance Hub](https://compliancehub.wiki/legal-ai-hallucination-reckoning-2026/)
  - Deloitte refunded the final instalment of an A$440k contract. — [The Register](https://www.theregister.com/2025/10/06/deloitte_ai_report_australia/)
- **How it's handled today:** Paralegal cite-checking; legal research platforms.
- **Who sells / crowding:** Legal research incumbents and legal-AI vendors. Prices not found.
- **(f) check:**
  - Westlaw and Lexis brief-analysis and citator tools are included in vertical legal research subscriptions. **[prior knowledge, not re-verified, no URL]**
  - Verdict: likely fails f for law firms. No bundled equivalent for consulting reports.
- **Grow or shrink:**
  - Shrinks: grounded, retrieval-based legal AI cites real sources, and courts require AI disclosure.
  - Grows: an eightfold rise in caught cases in a year, and AI use spreading to every kind of document.
- **How to reach buyers:** State bar associations and CLE providers, ILTA, malpractice insurers, consulting and government-contractor associations (in Australia, procurement panels after Deloitte).
- **Rough US count:** Not found.
- **Strongest argument against:**
  - Lawyers have a non-delegable duty and won't outsource verification of their own filings.
  - The vertical incumbents bundle checks.
  - Most cases come from pro se litigants (405 vs 256 lawyers in 2026), who are not buyers.
- **Six tests:**
  - a: yes
  - b: yes
  - c: yes
  - d: yes
  - e: yes
  - f: likely fails for legal
  - **5/6 (fails f for law firms: Westlaw/Lexis brief checks bundled, unverified)**

#### Rejected or secondary candidates, one line each
- **AI crawlers and bot scraping costs.** Fails f: Cloudflare offers free AI-crawler blocking on its free plan **[prior knowledge, not re-verified, no URL]**. Cost per small site is small ($155 forum overage; $5k at Read the Docs in 2024). — [Boing Boing (2024)](https://boingboing.net/2024/07/29/ai-crawlers-run-up-a-websites-hosting-bill.html)
- **AI customer-service bot rescue.** Partly fails f: helpdesk vendors bundle AI QA **[prior knowledge, not re-verified]**. Overlaps the labour/BPO lens. Demand is real: 95% of service leaders plan to keep humans. — [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-06-10-gartner-predicts-50-percent-of-organizations-will-abandon-plans-to-reduce-customer-service-workforce-due-to-ai)
- **Fake-review extortion.** The AI link is weak in the sources. Google removes reviews for free. Hits local SMBs (photographers, roofers) — [WSMV](https://www.wsmv.com/2026/01/18/overseas-criminals-hijack-google-reviews-middle-tennessee-business). Halal flag: restaurant and bar clients may be alcohol-centred.
- **AI tool sprawl and spend.** Folded into P2. Overlaps the "money leaks" lens. Evidence: [Zylo](https://zylo.com/news/2026-saas-management-index)

### Inferences
- **Blind attractiveness (1 to 10 = pain x willingness to pay x low competition x staying power):**
  - P5 finance-ops forgery desk: 7
  - P6 e-commerce claims-evidence desk: 7
  - P1 vibe-code care plan: 6
  - P7 candidate verification desk: 6
  - P2 AI run-and-improve: 6
  - P3 shadow-AI governance: 5
  - P4 GEO: 5
  - P8 deliverable QA: 4
- The common shape of the best opportunities: a daily queue of AI-generated items (claims, invoices, applicants) where AI does first-pass triage and a human makes the judgment call. That is retainer-friendly. Software-only vendors leave the human-review step to the client.
- Halal flags:
  - P3, if clients are interest-based lenders or banks.
  - P4, if clients include casinos, alcohol brands or prediction markets.
  - Review-extortion work for bars.
  - Deepfake detection (P5, P7) is in scope; deepfake creation is not.

### Gaps
- Not found this session: vendor prices for Harmonic, Cyberhaven, Nightfall, Microsoft Purview tiers, Forter, Signifyd, AppZen, Trustpair, Eftsure, CLEAR-in-Greenhouse, deepfake-interview detectors, and Reality Defender/Pindrop.
- Recruiter hours spent on fake applicants; dollar cost per failed AI pilot; US counts of affected companies for most problems.
- Verbatim owner quotes from Reddit and forums (not reached; search budget exhausted).
- Six-test (a) weekly frequency is inferred, not measured, for P1 and P2.

---

## Key Question 3: Will each problem grow or shrink as AI models improve over the next 24 months?

### Takeaway
- **Adversarial problems grow** as models improve: forged documents, faked refund evidence, fake candidates, review attacks. Better generators beat whole-image and voice detectors, so the human-plus-AI review layer gains value.
- **Quality problems are most at risk of shrinking**: vibe-code bugs, hallucinated citations. Better models and platform guardrails remove some of them, though the sheer volume of AI output may keep absolute counts rising.
- **Structural problems keep growing** whatever the model quality: AI search clicks, shadow AI, AI spend sprawl.

### Cited Findings
- Growth signals:
  - The AI share of detected fake receipts went from 0% to 70.8% in about 14 months (vendor claim). — [Accounting Today](https://www.accountingtoday.com/news/use-of-ai-receipts-in-expense-fraud-soars)
  - The FBI added its first dedicated AI-fraud section ($893M). — [iTnews](https://www.itnews.com.au/news/ai-assisted-fraud-makes-big-debut-in-fbis-cybercrime-stats-624819)
  - Legal hallucination filings rose eightfold year over year. — [The Star/AFP](https://www.thestar.com.my/tech/tech-news/2026/06/15/courts-cracking-down-on-error-strewn-ai-assisted-legal-briefs)
  - Gartner forecasts 1 in 4 fake candidate profiles by 2028. — [Gartner](https://www.gartner.com/en/newsroom/press-releases/2025-07-31-gartner-survey-shows-just-26-percent-of-job-applicants-trust-ai-will-fairly-evaluate-them)
  - Abandonment of AI initiatives rose from 17% to 42%. — [Horwath HTL](https://workshop.horwathhtl.com/resources/case-studies/genai-abandonment-landscape)
  - Sensitive file uploads rose from 22% to 26.4% in one quarter. — [BusinessWire](https://www.businesswire.com/news/home/20251113987633/en/Over-a-Quarter-26-of-Uploads-to-GenAI-Tools-Contain-Sensitive-Data-an-Increase-of-Over-4-in-Just-Three-Months)
- Detection arms race:
  - Inpainting damage onto real photos "defeats whole-image detection almost entirely." Suggested controls are process-based (capture, binding, timestamps, human-review thresholds). — [Switch Labs](https://www.switchlabs.dev/post/ai-faked-damage-photos-playbook)
- Shrink signals:
  - None of the 5 coding tools produced exploitable SQL injection or XSS. Weaknesses were concentrated in access-control logic, so code quality is improving on basic classes of flaw. — [The Next Web](https://thenextweb.com/news/lovable-vibe-coding-security-crisis-exposed)
  - Greenhouse bundled CLEAR verification. — [Greenhouse](https://greenhouse.com/newsroom/greenhouse-and-clear-announce-partnership-to-enable-candidate-verification)
  - Taobao and Tmall built in-house AI detection. — [OECD](https://oecd.ai/en/incidents/2026-01-21-2ae9)
  - Platforms absorbing fixes is the main shrink force.
- AI search:
  - Clicks fell even on queries without AI Overviews (down 41% to 46% YoY), suggesting a broad structural shift rather than a model-quality issue. — [Seer](https://www.seerinteractive.com/insights/aio-impact-on-google-ctr-september-2025-update); [MediaPost](https://www.mediapost.com/publications/article/410452/google-ai-overviews-drive-ctrs-down.html)
  - Google disputes the Pew methodology. — [MediaPost](https://www.mediapost.com/publications/article/407651/google-hits-back-at-pew-report)
- Customer-service bots: Gartner says an agentless contact centre is "not yet technically feasible." Better models may close this gap and shrink the "human rescue" need. — [The Register](https://www.theregister.com/2025/06/11/gartner_ai_customer_service/)

### Inferences
- **P1 vibe-code.** Mixed.
  - Shrinks: bugs per app fall as models and platforms add guardrails.
  - Grows: the number of live AI-built apps, and their business-logic and compliance needs.
  - Net: favours ongoing maintenance over one-off rescue.
- **P2 orphaned pilots.** Grows short-term (2026-27 cancellation wave). After that, platform vendors may bundle agent operations.
- **P3 shadow AI.** Grows in exposure, but software bundling (Microsoft, Google) shrinks the service share.
- **P4 AI search.** Grows structurally. Tactics will change often, which favours a retainer over a one-off.
- **P5 and P6 forgery and fake claims.** Grow most clearly. Every model improvement helps attackers, and detection must move to process controls plus human judgment.
- **P7 candidate fraud.** Grows. Incumbents' bundling caps the service share.
- **P8 hallucination QA.** Most likely to shrink per document as grounding improves, though volume may offset this through 2027.

### Gaps
- No neutral forecast was found for AI-generated refund-fraud volume or vibe-coded app counts.
- Model-improvement effects are argued from mechanism, not measured.
